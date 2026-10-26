"""
Equator Resolution — reference implementation: persistence layer.

SQLite mirror of the production PostgreSQL DDL (schema_wp.sql / schema_fam.sql).
The point of this module is that the three institutional rules are enforced by
DATABASE CONSTRAINTS, not by application politeness:

  R1  a POSH matter can never sit in an ordinary case state
  R2  a settlement can never assert waiver of statutory dues
  R3  POSH records live in a separate store with no join path to ordinary cases

Standard library only. Python 3.8+.
"""
import sqlite3, uuid, datetime, os

ORDINARY_SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS party (
  id            TEXT PRIMARY KEY,
  role          TEXT NOT NULL CHECK (role IN
                  ('employee','ex_employee','employer','hr_rep','contractor','gig_worker','union_rep',
                   'spouse_a','spouse_b','borrower','lender')),
  full_name     TEXT NOT NULL,
  masked_gov_id TEXT,
  created_at    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS employer (
  id             TEXT PRIMARY KEY,
  name           TEXT NOT NULL,
  estab_size     TEXT NOT NULL CHECK (estab_size IN ('lt_10','10_49','50_99','100_299','300_plus')),
  posh_subscriber INTEGER NOT NULL DEFAULT 0,
  ic_constituted  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS employment_record (
  id               TEXT PRIMARY KEY,
  party_id         TEXT NOT NULL REFERENCES party(id),
  employer_id      TEXT NOT NULL REFERENCES employer(id),
  monthly_wages    REAL NOT NULL,
  wages_pct_of_ctc REAL NOT NULL,
  completed_years  INTEGER NOT NULL
);

-- R1 enforced here: is_posh=1 is only ever compatible with sealed/signposted/closed
CREATE TABLE IF NOT EXISTS mediation_case (
  id             TEXT PRIMARY KEY,
  case_number    TEXT UNIQUE NOT NULL,
  vertical       TEXT NOT NULL CHECK (vertical IN ('family','commercial','financial','workplace')),
  dispute_types  TEXT NOT NULL,
  status         TEXT NOT NULL CHECK (status IN
                   ('intake','triaged','posh_sealed','in_session','settlement','signposted','closed','withdrawn')),
  route          TEXT,
  employer_id    TEXT REFERENCES employer(id),
  employee_id    TEXT REFERENCES party(id),
  is_posh        INTEGER NOT NULL DEFAULT 0,
  safety_flag    INTEGER NOT NULL DEFAULT 0,
  opened_at      TEXT NOT NULL,
  CHECK (is_posh = 0 OR status IN ('posh_sealed','signposted','closed'))
);

CREATE TABLE IF NOT EXISTS screening (
  id          TEXT PRIMARY KEY,
  case_id     TEXT NOT NULL REFERENCES mediation_case(id),
  party_id    TEXT NOT NULL REFERENCES party(id),
  outcome     TEXT NOT NULL CHECK (outcome IN
                ('suitable','suitable_with_safeguards','shuttle_only','not_suitable_safety')),
  safeguards  TEXT,
  created_at  TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS session (
  id           TEXT PRIMARY KEY,
  case_id      TEXT NOT NULL REFERENCES mediation_case(id),
  mode         TEXT NOT NULL CHECK (mode IN ('joint','caucus','shuttle','online','in_person')),
  scheduled_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS caucus_note (
  id          TEXT PRIMARY KEY,
  session_id  TEXT NOT NULL REFERENCES session(id),
  neutral_id  TEXT NOT NULL,
  note_cipher BLOB NOT NULL,
  created_at  TEXT NOT NULL
);

-- R2 enforced here
CREATE TABLE IF NOT EXISTS settlement (
  id                    TEXT PRIMARY KEY,
  case_id               TEXT NOT NULL REFERENCES mediation_case(id),
  net_payable           REAL NOT NULL,
  gratuity_amount       REAL NOT NULL DEFAULT 0,
  statutory_dues_waived INTEGER NOT NULL DEFAULT 0,
  relieving_letter      INTEGER NOT NULL DEFAULT 0,
  assets_returned       INTEGER NOT NULL DEFAULT 0,
  enforceable_s27       INTEGER NOT NULL DEFAULT 1,
  signed_at             TEXT,
  CHECK (statutory_dues_waived = 0)
);

CREATE TABLE IF NOT EXISTS escrow (
  id       TEXT PRIMARY KEY,
  case_id  TEXT NOT NULL REFERENCES mediation_case(id),
  amount   REAL NOT NULL CHECK (amount >= 0),
  state    TEXT NOT NULL DEFAULT 'created'
);

CREATE TABLE IF NOT EXISTS escrow_milestone (
  id         TEXT PRIMARY KEY,
  escrow_id  TEXT NOT NULL REFERENCES escrow(id),
  name       TEXT NOT NULL,
  condition  TEXT NOT NULL,
  amount     REAL NOT NULL,
  released   INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS audit_event (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,
  actor      TEXT,
  case_id    TEXT,
  store      TEXT NOT NULL,
  action     TEXT NOT NULL,
  detail     TEXT,
  prev_hash  TEXT,
  row_hash   TEXT,
  created_at TEXT NOT NULL
);
"""

# R3: a physically separate database file. There is no SQL path from the ordinary
# store to this one — a join is impossible, not merely forbidden.
POSH_SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS posh_complaint (
  id                 TEXT PRIMARY KEY,
  complaint_number   TEXT UNIQUE NOT NULL,
  employer_ref       TEXT NOT NULL,          -- deliberately not a foreign key
  received_on        TEXT NOT NULL,
  stage              TEXT NOT NULL DEFAULT 'received',
  complainant_cipher BLOB NOT NULL,
  respondent_cipher  BLOB NOT NULL,
  particulars_cipher BLOB NOT NULL
);

CREATE TABLE IF NOT EXISTS internal_committee (
  id                 TEXT PRIMARY KEY,
  employer_ref       TEXT NOT NULL,
  presiding_officer  TEXT NOT NULL,
  member_count       INTEGER NOT NULL CHECK (member_count >= 2),
  women_members      INTEGER NOT NULL,
  external_member_id TEXT,
  CHECK (external_member_id IS NOT NULL),          -- POSH s.4
  CHECK (women_members * 2 >= member_count + 1)    -- at least half women
);

CREATE TABLE IF NOT EXISTS posh_conciliation (
  id                 TEXT PRIMARY KEY,
  complaint_id       TEXT NOT NULL REFERENCES posh_complaint(id),
  requested_by_woman INTEGER NOT NULL,
  monetary_basis     INTEGER NOT NULL DEFAULT 0,
  terms_cipher       BLOB,
  CHECK (requested_by_woman = 1),   -- POSH s.10: her request only
  CHECK (monetary_basis = 0)        -- POSH s.10: never on a monetary basis
);

CREATE TABLE IF NOT EXISTS posh_inquiry (
  id           TEXT PRIMARY KEY,
  complaint_id TEXT NOT NULL REFERENCES posh_complaint(id),
  commenced_on TEXT NOT NULL,
  concluded_on TEXT,
  finding      TEXT
);
"""


def _now():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def _uid():
    return str(uuid.uuid4())


class Store:
    """Two physically separate databases. That separation IS the POSH control."""

    def __init__(self, ordinary_path=":memory:", posh_path=":memory:"):
        self.ordinary = sqlite3.connect(ordinary_path)
        self.posh = sqlite3.connect(posh_path)
        for c in (self.ordinary, self.posh):
            c.row_factory = sqlite3.Row
            c.execute("PRAGMA foreign_keys = ON")
        self.ordinary.executescript(ORDINARY_SCHEMA)
        self.posh.executescript(POSH_SCHEMA)
        self.ordinary.commit()
        self.posh.commit()

    # ---------- audit (hash-chained) ----------
    def audit(self, action, store="ordinary", case_id=None, actor="system", detail=""):
        import hashlib
        cur = self.ordinary.execute("SELECT row_hash FROM audit_event ORDER BY id DESC LIMIT 1")
        row = cur.fetchone()
        prev = row["row_hash"] if row else ""
        payload = f"{prev}|{actor}|{case_id}|{store}|{action}|{detail}"
        h = hashlib.sha256(payload.encode()).hexdigest()
        self.ordinary.execute(
            "INSERT INTO audit_event (actor,case_id,store,action,detail,prev_hash,row_hash,created_at)"
            " VALUES (?,?,?,?,?,?,?,?)",
            (actor, case_id, store, action, detail, prev, h, _now()))
        self.ordinary.commit()
        return h

    def verify_audit_chain(self):
        """Returns (ok, first_broken_id). Detects tampering with any audit row."""
        import hashlib
        prev = ""
        for r in self.ordinary.execute(
                "SELECT id,actor,case_id,store,action,detail,prev_hash,row_hash"
                " FROM audit_event ORDER BY id"):
            payload = f"{prev}|{r['actor']}|{r['case_id']}|{r['store']}|{r['action']}|{r['detail']}"
            if hashlib.sha256(payload.encode()).hexdigest() != r["row_hash"]:
                return False, r["id"]
            prev = r["row_hash"]
        return True, None

    def close(self):
        self.ordinary.close()
        self.posh.close()
