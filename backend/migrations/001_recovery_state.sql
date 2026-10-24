-- Revslot synthetic booking state and leased recovery jobs.
-- Apply to an isolated development branch before the live branch.
CREATE TABLE IF NOT EXISTS runs (
    id TEXT PRIMARY KEY,
    revision INTEGER NOT NULL,
    body TEXT NOT NULL,
    updated DOUBLE PRECISION NOT NULL
);
CREATE TABLE IF NOT EXISTS clock_jobs (
    run_id TEXT PRIMARY KEY,
    due DOUBLE PRECISION NOT NULL,
    lease_token TEXT,
    lease_until DOUBLE PRECISION NOT NULL DEFAULT 0
);
CREATE INDEX IF NOT EXISTS clock_jobs_due_idx ON clock_jobs(due,lease_until);
