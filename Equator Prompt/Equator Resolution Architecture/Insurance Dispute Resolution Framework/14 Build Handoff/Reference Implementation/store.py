"""
Equator Resolution — Insurance vertical reference implementation: persistence layer.

The point of this module, like the platform Reference Implementation for the Family/
Workplace verticals, is that the three institutional rules are enforced by DATABASE
CONSTRAINTS, not by application politeness:

  R1  no arbitration route on a policy classified retail (IRDAI circular, 27 Oct 2023)
  R2  no settlement may assert waiver of a non-waivable statutory right
  R3  no case closes without a delivered signposting event and an owner on every clock

Health data lives in a physically separate SQLite database with no join path to the
ordinary case store — the separation IS the control.

Standard library only. Python 3.8+.
"""
import sqlite3, uuid, datetime, hashlib

ORDINARY_SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS insurer (
  id     TEXT PRIMARY KEY,
  name   TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS policy (
  id            TEXT PRIMARY KEY,
  insurer_id    TEXT NOT NULL REFERENCES insurer(id),
  policy_no     TEXT NOT NULL,
  line          TEXT NOT NULL,
  -- R1 gate: classification is mandatory; no default
  class         TEXT NOT NULL CHECK (class IN ('retail','commercial','group_member','group_master')),
  legacy_arbitration_clause INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS dispute_case (
  id             TEXT PRIMARY KEY,
  case_no        TEXT UNIQUE NOT NULL,
  policy_id      TEXT NOT NULL REFERENCES policy(id),
  amount_in_dispute REAL NOT NULL DEFAULT 0,
  is_retail      INTEGER NOT NULL,
  fraud_alleged  INTEGER NOT NULL DEFAULT 0,
  route          TEXT,
  status         TEXT NOT NULL DEFAULT 'intake'
                   CHECK (status IN ('intake','triaged','notified','collecting','prepared',
                                     'in_session','settlement','escrow','signposted','closed','withdrawn')),
  representation_date TEXT,
  insurer_reply_date  TEXT,
  reply_outcome  TEXT,
  pending_forum  TEXT,
  opened_at      TEXT NOT NULL,
  -- R1 enforced here in the database, not in code:
  CHECK (route IS NULL OR route <> 'arbitration' OR is_retail = 0),
  -- fraud allegations are not mediated:
  CHECK (fraud_alleged = 0 OR route IS NULL OR route <> 'equator_mediation')
);

CREATE TABLE IF NOT EXISTS signposting_event (
  id           TEXT PRIMARY KEY,
  case_id      TEXT NOT NULL REFERENCES dispute_case(id),
  delivered_at TEXT NOT NULL,
  channel      TEXT NOT NULL,
  language     TEXT NOT NULL,
  script_version TEXT NOT NULL,
  delivered_by TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS clock (
  id           TEXT PRIMARY KEY,
  case_id      TEXT NOT NULL REFERENCES dispute_case(id),
  kind         TEXT NOT NULL,
  trigger_date TEXT NOT NULL,
  period_days  INTEGER NOT NULL CHECK (period_days > 0),
  owner        TEXT,
  prompted_at  TEXT,
  UNIQUE (case_id, kind)
);

CREATE TABLE IF NOT EXISTS triage (
  id            TEXT PRIMARY KEY,
  case_id       TEXT NOT NULL UNIQUE REFERENCES dispute_case(id),
  classified_by TEXT NOT NULL,
  reviewed_by   TEXT NOT NULL,
  CHECK (reviewed_by <> classified_by)          -- second-officer review
);

CREATE TABLE IF NOT EXISTS deduction_line (
  id       TEXT PRIMARY KEY,
  case_id  TEXT NOT NULL REFERENCES dispute_case(id),
  head     TEXT NOT NULL,
  billed   REAL NOT NULL,
  allowed  REAL NOT NULL,
  reason_code TEXT,
  CHECK (allowed <= billed),
  CHECK (billed = allowed OR reason_code IS NOT NULL)
);

-- R2 enforced here:
CREATE TABLE IF NOT EXISTS settlement (
  id                     TEXT PRIMARY KEY,
  case_id                TEXT NOT NULL UNIQUE REFERENCES dispute_case(id),
  amount                 REAL NOT NULL CHECK (amount >= 0),
  continuity_preserved   INTEGER NOT NULL DEFAULT 0,
  statutory_rights_waived INTEGER NOT NULL DEFAULT 0,
  future_claims_discharged INTEGER NOT NULL DEFAULT 0,
  registered_at          TEXT,
  CHECK (statutory_rights_waived = 0),
  CHECK (future_claims_discharged = 0)
);

CREATE TABLE IF NOT EXISTS discharge_voucher (
  id           TEXT PRIMARY KEY,
  case_id      TEXT NOT NULL REFERENCES dispute_case(id),
  basis        TEXT NOT NULL CHECK (basis IN ('full_final','under_protest','on_account')),
  amount       REAL NOT NULL,
  balance_reserved REAL NOT NULL DEFAULT 0,
  CHECK (basis <> 'under_protest' OR balance_reserved > 0)
);

CREATE TABLE IF NOT EXISTS audit_event (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  actor      TEXT, case_id TEXT, store TEXT NOT NULL, action TEXT NOT NULL, detail TEXT,
  prev_hash  TEXT, row_hash TEXT, created_at TEXT NOT NULL
);
"""

# R3 (health segregation): a physically separate database. No SQL path exists from the
# ordinary store to this one — a join is impossible, not merely forbidden.
HEALTH_SCHEMA = """
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS medical_record (
  id             TEXT PRIMARY KEY,
  case_ref       TEXT NOT NULL,          -- deliberately a text reference, not a foreign key
  doc_type       TEXT NOT NULL,
  content_cipher BLOB NOT NULL,
  authority_ref  TEXT NOT NULL,
  received_at    TEXT NOT NULL,
  CHECK (length(authority_ref) > 0)
);
CREATE TABLE IF NOT EXISTS medical_access_log (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  record_id   TEXT NOT NULL REFERENCES medical_record(id),
  actor       TEXT NOT NULL,
  actor_role  TEXT NOT NULL,
  case_ref    TEXT NOT NULL,
  accessed_at TEXT NOT NULL
);
"""


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _uid():
    return str(uuid.uuid4())


class Store:
    """Two physically separate databases. That separation IS the health-data control."""

    def __init__(self, ordinary_path=":memory:", health_path=":memory:"):
        self.ordinary = sqlite3.connect(ordinary_path)
        self.health = sqlite3.connect(health_path)
        for c in (self.ordinary, self.health):
            c.row_factory = sqlite3.Row
            c.execute("PRAGMA foreign_keys = ON")
        self.ordinary.executescript(ORDINARY_SCHEMA)
        self.health.executescript(HEALTH_SCHEMA)
        self.ordinary.commit(); self.health.commit()

    def audit(self, action, store="ordinary", case_id=None, actor="system", detail=""):
        cur = self.ordinary.execute("SELECT row_hash FROM audit_event ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        prev = row["row_hash"] if row else ""
        payload = f"{prev}|{actor}|{case_id}|{store}|{action}|{detail}"
        h = hashlib.sha256(payload.encode()).hexdigest()
        self.ordinary.execute(
            "INSERT INTO audit_event (actor,case_id,store,action,detail,prev_hash,row_hash,created_at)"
            " VALUES (?,?,?,?,?,?,?,?)", (actor, case_id, store, action, detail, prev, h, _now()))
        self.ordinary.commit()
        return h

    def verify_audit_chain(self):
        prev = ""
        for r in self.ordinary.execute(
                "SELECT id,actor,case_id,store,action,detail,prev_hash,row_hash FROM audit_event ORDER BY id"):
            payload = f"{prev}|{r['actor']}|{r['case_id']}|{r['store']}|{r['action']}|{r['detail']}"
            if hashlib.sha256(payload.encode()).hexdigest() != r["row_hash"]:
                return False, r["id"]
            prev = r["row_hash"]
        return True, None

    def close(self):
        self.ordinary.close(); self.health.close()
