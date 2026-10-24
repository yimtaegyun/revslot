"""Atomic optimistic updates. SQLite locally; optional PostgreSQL for hosted durability."""
import json
import os
import sqlite3
import time
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

    def init(self):
        if self._initialized: return
        with self.connect() as c:
            c.execute("CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY, revision INTEGER NOT NULL, body TEXT NOT NULL, updated DOUBLE PRECISION NOT NULL)")
        self._initialized=True

    def create(self,state):
        self.init()
        with self.connect() as c:
            c.execute(self.sql("INSERT INTO runs VALUES(?,?,?,?)"),(state["run_id"],state["revision"],json.dumps(state),time.time()))
        return state

    def load(self,run_id):
        self.init()
        with self.connect() as c:
            row=c.execute(self.sql("SELECT body,updated FROM runs WHERE id=?"),(run_id,)).fetchone()
        if not row or time.time()-row[1]>86400: raise Missing("Demo session expired; load a fresh scenario")
        return json.loads(row[0])

    def save(self,state,expected):
        state["revision"]=expected+1
        with self.connect() as c:
            cur=c.execute(self.sql("UPDATE runs SET revision=?,body=?,updated=? WHERE id=? AND revision=?"),
                (state["revision"],json.dumps(state),time.time(),state["run_id"],expected))
            if cur.rowcount!=1: raise Conflict("State changed; refresh before retrying")
        return state

    @property
    def durability(self):
        return "postgres" if self.database_url else "ephemeral_sqlite" if os.getenv("VERCEL") else "sqlite"
