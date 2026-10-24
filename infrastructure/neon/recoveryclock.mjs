import { parseTriggerDelivery } from "@neon/functions/triggers";
import { waitUntil } from "@neon/functions";
import { timingSafeEqual } from "node:crypto";

const TARGET = "https://revslot-one.vercel.app/api/jobs/tick";
const TRIGGER = "recovery-clock-every-minute";

// Bounded work covers the seeded three-hour horizon (90 real seconds).
// PostgreSQL owns jobs/leases; a 15-minute native cron retries interruptions.
// Empty queues exit immediately instead of keeping the Free database warm.
export async function dispatchTicks(secret, runtime = {}) {
  const fetcher = runtime.fetcher ?? fetch;
  const now = runtime.now ?? Date.now;
  const wait = runtime.wait ?? ((ms) => new Promise((resolve) => setTimeout(resolve, ms)));
  const started = now();
  const result = { calls: 0, processed: 0, conflicts: 0, failed: 0 };
  for (let index = 0; index < 12; index++) {
    const delay = started + index * 10_000 - now();
    if (delay > 0) await wait(delay);
    const response = await fetcher(TARGET, {
      headers: { Authorization: `Bearer ${secret}` },
      redirect: "manual",
      signal: AbortSignal.timeout(15_000),
    });
    result.calls++;
    if (!response.ok) throw new Error("Tick endpoint failed");
    const tick = await response.json();
    for (const key of ["processed", "conflicts", "failed", "active_jobs"]) {
      if (!Number.isSafeInteger(tick[key]) || tick[key] < 0) throw new Error("Invalid tick result");
      if (key !== "active_jobs") result[key] += tick[key];
    }
    if (tick.failed) throw new Error("Recovery tick retained for retry");
    if (tick.active_jobs === 0) break;
  }
  return result;
}

function authenticated(request, secret) {
  const actual = Buffer.from(request.headers.get("authorization") ?? "");
  const expected = Buffer.from(`Bearer ${secret}`);
  return actual.length === expected.length && timingSafeEqual(actual, expected);
}

export function createHandler(runtime = {}) {
  const dispatch = runtime.dispatch ?? dispatchTicks;
  const defer = runtime.defer ?? waitUntil;
  const getSecret = runtime.getSecret ?? (() => process.env.CRON_SECRET);
  const logResult = (result) => console.info(JSON.stringify({ event: "recovery_clock_tick", ...result }));
  const logFailure = () => console.error("Recovery clock invocation failed; persisted jobs remain retryable");
  return {
    async fetch(request) {
      const path = new URL(request.url).pathname;
      if (request.method !== "POST" || !["/wake", "/cron"].includes(path)) return new Response("Not found", { status: 404 });
      const secret = getSecret();
      if (!secret) return new Response("Scheduler is not configured", { status: 503 });
      if (path === "/wake") {
        if (!authenticated(request, secret)) return new Response("Unauthorized", { status: 401 });
        // Bounded post-response work reduces start latency. SQL owns durable
        // jobs, while the native cron retries interruption; this is no daemon.
        defer(dispatch(secret).then(logResult).catch(logFailure));
        return Response.json({ accepted: true }, { status: 202 });
      }
      // The native proxy strips caller-supplied x-neon-* headers.
      const parsed = await parseTriggerDelivery(request);
      if (!parsed.ok) return new Response("Invalid trigger", { status: parsed.error === "invalid_body" ? 400 : 401 });
      if (parsed.invocation.type !== "schedule" || parsed.invocation.trigger.name !== TRIGGER) return new Response("Unexpected trigger", { status: 403 });
      try {
        const result = await dispatch(secret);
        logResult(result);
        return Response.json(result);
      } catch {
        logFailure();
        return new Response("Tick failed; retry on the next schedule", { status: 502 });
      }
    },
  };
}

export default createHandler();
