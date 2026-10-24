import test from "node:test";
import assert from "node:assert/strict";
import { createHandler, dispatchTicks } from "./recoveryclock.mjs";

test("scheduled calls retain a ten-second cadence without a browser", async () => {
  let time = 0;
  const starts = [];
  const result = await dispatchTicks("unit-only", {
    now: () => time,
    wait: async (ms) => { time += ms; },
    fetcher: async (url, options) => {
      starts.push(time);
      assert.equal(url, "https://revslot-one.vercel.app/api/jobs/tick");
      assert.equal(options.redirect, "manual");
      assert.equal(options.headers.Authorization, "Bearer unit-only");
      time += 300;
      return Response.json({ processed: 1, conflicts: 0, failed: 0, active_jobs: starts.length < 6 ? 1 : 0 });
    },
  });
  assert.deepEqual(starts, [0, 10000, 20000, 30000, 40000, 50000]);
  assert.deepEqual(result, { calls: 6, processed: 6, conflicts: 0, failed: 0 });
});

test("redirects and failed work stop this invocation for a later durable retry", async () => {
  let calls = 0;
  await assert.rejects(dispatchTicks("unit-only", { fetcher: async () => {
    calls++;
    return new Response(null, { status: 302, headers: { Location: "https://example.com" } });
  } }));
  assert.equal(calls, 1);
  await assert.rejects(dispatchTicks("unit-only", { fetcher: async () => Response.json({ processed: 0, conflicts: 0, failed: 1, active_jobs: 1 }) }));
});

test("public requests without Neon trigger provenance are rejected", async () => {
  const response = await createHandler({ getSecret: () => "unit-only" }).fetch(new Request("https://example.com/cron", {
    method: "POST", headers: { "content-type": "application/json" }, body: "{}",
  }));
  assert.equal(response.status, 401);
});

test("idle work exits immediately without a keep-warm loop", async () => {
  const result = await dispatchTicks("unit-only", { fetcher: async () => Response.json({ processed: 0, conflicts: 0, failed: 0, active_jobs: 0 }), wait: async () => { throw new Error("Idle queue must not wait"); } });
  assert.equal(result.calls, 1);
});

test("trusted wake returns accepted while bounded work is tracked", async () => {
  const tracked = []; let dispatched = 0;
  const handler = createHandler({ getSecret: () => "unit-only", defer: (work) => tracked.push(work), dispatch: async () => { dispatched++; return { calls: 1, processed: 0, conflicts: 0, failed: 0 }; } });
  const denied = await handler.fetch(new Request("https://example.com/wake", { method: "POST", headers: { Authorization: "Bearer wrong" } }));
  assert.equal(denied.status, 401); assert.equal(dispatched, 0);
  const accepted = await handler.fetch(new Request("https://example.com/wake", { method: "POST", headers: { Authorization: "Bearer unit-only" } }));
  assert.equal(accepted.status, 202); assert.equal(tracked.length, 1);
  await Promise.all(tracked); assert.equal(dispatched, 1);
});

test("a nonempty queue cannot turn one wake into an unbounded daemon", async () => {
  let time = 0;
  const result = await dispatchTicks("unit-only", { now: () => time, wait: async (ms) => { time += ms; }, fetcher: async () => Response.json({ processed: 0, conflicts: 0, failed: 0, active_jobs: 1 }) });
  assert.equal(result.calls, 12);
  assert.equal(time, 110000);
});
