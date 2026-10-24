"""Atomic optimistic updates. SQLite locally; optional PostgreSQL for hosted durability."""
import json
import os
import sqlite3
import time
import secrets
from contextlib import contextmanager
from pathlib import Path


class Conflict(Exception): pass
class Missing(Exception): pass


class Store:
    def __init__(self,path=None):
        self.path=path or os.getenv("REVSlot_DB_PATH") or ("/tmp/revslot.sqlite" if os.getenv("VERCEL") else str(Path(__file__).parent.parent/"runtime.sqlite"))
        self.database_url=os.getenv("DATABASE_URL")
        self._initialized=False

    def connect(self):
        if self.database_url:
            import psycopg
            return psycopg.connect(self.database_url)
        conn=sqlite3.connect(self.path,timeout=10)
        conn.execute("PRAGMA busy_timeout=10000")
        return conn

    def sql(self,text): return text.replace("?","%s") if self.database_url else text

    @contextmanager
    def connection(self):
        conn=self.connect()
        try:
            with conn:
                yield conn
        finally:
            conn.close()

    def init(self):
        if self._initialized: return
        with self.connection() as c:
            c.execute("CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY, revision INTEGER NOT NULL, body TEXT NOT NULL, updated DOUBLE PRECISION NOT NULL)")
            c.execute("CREATE TABLE IF NOT EXISTS clock_jobs(run_id TEXT PRIMARY KEY, due DOUBLE PRECISION NOT NULL, lease_token TEXT, lease_until DOUBLE PRECISION NOT NULL DEFAULT 0)")
        self._initialized=True

    def create(self,state):
        self.init()
        with self.connection() as c:
            c.execute(self.sql("INSERT INTO runs VALUES(?,?,?,?)"),(state["run_id"],state["revision"],json.dumps(state),time.time()))
        return state

    def load(self,run_id):
        self.init()
        with self.connection() as c:
            row=c.execute(self.sql("SELECT body,updated FROM runs WHERE id=?"),(run_id,)).fetchone()
        if not row or time.time()-row[1]>86400: raise Missing("Demo session expired; load a fresh scenario")
        return json.loads(row[0])

    def save(self,state,expected,*,lease_token=None):
        state["revision"]=expected+1
        with self.connection() as c:
            sql="UPDATE runs SET revision=?,body=?,updated=? WHERE id=? AND revision=?"
            args=[state["revision"],json.dumps(state),time.time(),state["run_id"],expected]
            if lease_token is not None:
                sql+=" AND EXISTS(SELECT 1 FROM clock_jobs WHERE run_id=runs.id AND lease_token=? AND lease_until>?)"
                args.extend([lease_token,time.time()])
            cur=c.execute(self.sql(sql),args)
            if cur.rowcount!=1: raise Conflict("State changed; refresh before retrying")
            control=state.get("clock_control",{})
            if control.get("running"):
                c.execute(self.sql("INSERT INTO clock_jobs(run_id,due,lease_until) VALUES(?,?,0) ON CONFLICT(run_id) DO UPDATE SET due=excluded.due"),
                          (state["run_id"],control["next_tick_at"]))
            else:
                c.execute(self.sql("DELETE FROM clock_jobs WHERE run_id=?"),(state["run_id"],))
        return state

    def claim_due(self,now,limit=3,lease_seconds=60):
        """A committed conditional lease prevents two workers claiming the same clock."""
        self.init()
        claimed=[]
        with self.connection() as c:
            rows=c.execute(self.sql("SELECT run_id FROM clock_jobs WHERE due<=? AND lease_until<=? ORDER BY due LIMIT ?"),(now,now,limit)).fetchall()
            for (rid,) in rows:
                token=secrets.token_hex(16)
                cur=c.execute(self.sql("UPDATE clock_jobs SET lease_token=?,lease_until=? WHERE run_id=? AND due<=? AND lease_until<=?"),
                              (token,now+lease_seconds,rid,now,now))
                if cur.rowcount==1: claimed.append((rid,token))
        return claimed

    def scheduled_count(self):
        self.init()
        with self.connection() as c:
            return c.execute("SELECT count(*) FROM clock_jobs").fetchone()[0]

    def release_job(self,run_id,token,*,remove=False):
        with self.connection() as c:
            if remove:
                c.execute(self.sql("DELETE FROM clock_jobs WHERE run_id=? AND lease_token=?"),(run_id,token))
            else:
                c.execute(self.sql("UPDATE clock_jobs SET lease_token=NULL,lease_until=0 WHERE run_id=? AND lease_token=?"),(run_id,token))

    @property
    def durability(self):
        return "postgres" if self.database_url else "ephemeral_sqlite" if os.getenv("VERCEL") else "sqlite"
