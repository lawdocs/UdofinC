# Appendix B — Data Model, Events and Error Codes

> Binding on all phases. Owner: stream S11 (core). Module-specific tables are specified in the owning phase files (§7.2 of each); where a phase file and this appendix differ on a column of a table owned by that phase, the phase file prevails for that column and this appendix is corrected at the next integration. Names, prefixes, envelope rules and error-code scheme in this appendix prevail over phase files. §B.9 is compiled by the lead from stream contributions.

---

## B.0 Purpose and precedence

This appendix fixes the conventions every table, event and error uses, gives representative full DDL for the platform core and the central compliance model, and defines the event and error registers. It exists so that 25 phases built by different squads produce one coherent database that can be exported (Appendix M), audited (NN-02), isolated (NN-01), versioned (NN-07) and evolved without manual customer migration (NN-11).

Precedence: master prompt → `02` decisions → this appendix (conventions, envelope, codes) → owning phase (module columns) → other appendices.

---

## B.1 Conventions

### B.1.1 Naming

- Schema = module code (Appendix list in master §5): `core`, `iam`, `cfg`, `cnt`, `tpl`, `cmp`, `chg`, `wf`, `gov`, `pol`, `dms`, `erm`, `ral`, `aud`, `ret`, `acc`, `dpc`, `tpr`, `hr`, `lab`, `grv`, `pack`, `coop`, `ai`, `int`, `xpt`, `bil`, `mkp`, `sdc`, `web`, `hlp`, `rpt`, `eng`.
- Tables plural snake_case (`compliance_instances`); columns snake_case; booleans `is_`/`has_`; timestamps `_at`; dates `_on` or `_date`; foreign keys `<entity>_id`; enumerations stored as `text` with a `CHECK` constraint or a reference to a code table (`<schema>.code_<name>` or the shared `core.code_values`) — PostgreSQL `ENUM` types are not used (they make expand-contract changes harder).
- API JSON uses snake_case fields and `UPPER_SNAKE_CASE` enum values (Ecosystem Spec §3.3).

### B.1.2 Identifiers and prefix registry

Entity IDs: `<prefix>_` + ULID (26 Crockford base32 chars), `text` column with `CHECK (id ~ '^<prefix>_[0-9A-HJKMNP-TV-Z]{26}$')`. Event IDs: UUIDv7. Human references: `core.sequences`.

| Prefix | Entity | Prefix | Entity |
|---|---|---|---|
| `ten` | tenant | `len` | legal entity |
| `reg` | registration (CoR etc.) | `oru` | org unit |
| `per` | person | `usr` | user |
| `mbr` | membership | `rgr` | role grant |
| `dlg` | delegation | `dgr` | delivery grant |
| `agr` | audit grant | `sgr` | supervisor grant |
| `inv` | invitation | `brk` | break-glass event |
| `aev` | audit event | `anc` | audit anchor |
| `cor` | correction entry | `flg` | feature flag |
| `set` | setting value | `rpk` | rule pack |
| `aut` | authority | `ins` | instrument |
| `ivr` | instrument version | `cls` | clause |
| `obl` | obligation | `qst` | base question |
| `qvr` | question version | `ovl` | tenant overlay |
| `tpl` | template definition | `imp` | import job |
| `app` | applicability decision | `cin` | compliance instance |
| `cev` | compliance evidence link | `att` | attestation |
| `exc` | exception/waiver | `src` | regulatory source |
| `sit` | source item (fetched publication) | `chn` | change notice |
| `imx` | impact assessment | `upd` | update (Updates feed item) |
| `tsk` | task | `apr` | approval |
| `ntf` | notification | `cal` | calendar event |
| `doc` | document | `dvr` | document version |
| `evd` | evidence ledger entry | `shr` | share |
| `env` | eSign envelope | `out` | outbox (UUIDv7 id; prefix used in logs only) |
| `rsk` | risk | `kri` | key risk indicator |
| `ctl` | control | `iss` | issue/finding |
| `mtg` | meeting | `com` | committee |
| `pol` | policy | `pvr` | policy version |
| `ret` | return definition | `rrn` | return run |
| `emp` | employee | `grv` | grievance |
| `tkt` | support ticket | `agt` | AI agent run |
| `con` | connector | `xpk` | export package |
| `sub` | subscription | `invc` | invoice |
| `ord` | marketplace order | `prv` | provider |
| `cred` | vault credential | `rel` | release |
| `chg` | change record | `vul` | vulnerability |

Phases add prefixes in their contribution files; the lead compiles them into §B.9 and rejects collisions.

### B.1.3 Standard columns

Every tenant-scoped table:

```sql
id              text PRIMARY KEY,
tenant_id       text NOT NULL REFERENCES core.tenants(id),
legal_entity_id text NULL REFERENCES core.legal_entities(id),   -- where the record belongs to one entity
version         integer NOT NULL DEFAULT 1,                     -- optimistic concurrency; +1 on every change
created_at      timestamptz NOT NULL DEFAULT now(),
created_by      text NOT NULL,                                  -- user/service id
updated_at      timestamptz NOT NULL DEFAULT now(),
updated_by      text NOT NULL,
source_refs     jsonb NOT NULL DEFAULT '[]',                    -- lineage: imports, migrations, ecosystem events
correction_id   text NULL REFERENCES core.correction_entries(id) -- last correction applied, if any
```

plus RLS (`ENABLE` + `FORCE` + `tenant_isolation` policy), a `*_history` companion table populated by trigger (full before/after row, `changed_at`, `changed_by`, `audit_event_id`, `correction_id`), and a data-class tag for every column in `db/data-catalogue.yaml`.

Bitemporal tables add `valid_from`, `valid_to` (or `valid_period tstzrange`), `recorded_at`, `superseded_at` and the partial exclusion constraint (P00 FR-P00-37). Soft delete is not used for business records: a record ends by state (`ended`, `withdrawn`, `superseded`) and remains; physical deletion happens only through the retention/erasure workflow (P19/P12) with an audit event and, where Object Lock applies, after retention.

### B.1.4 Types

| Kind | Type |
|---|---|
| Money amount | `numeric(20,4)` + `currency char(3)` |
| Rate (percent p.a.) | `numeric(12,8)` + day-count code |
| Ratio | `numeric(18,10)` |
| Percent share | `numeric(9,6)` |
| Quantity of securities | `numeric(24,6)` |
| Date (legal date) | `date` (IST legal day) |
| Instant | `timestamptz` (stored UTC) |
| Free text (UI) | `text` with length `CHECK` per field |
| Encrypted field | `bytea` (`_enc`) + `bytea` blind index (`_bidx`) + `text` masked (`_masked`) |
| Citation | `jsonb` validated against the `Citation` JSON Schema (P00 FR-P00-40), plus foreign keys to `cnt.instrument_versions` / `cnt.clauses` where internal |
| Multi-select codes | `text[]` with `CHECK` against code table via trigger, or a join table where the relation has attributes |

### B.1.5 Data classes

`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `PII`, `SPI`, `FINANCIAL`, `LEGAL`, `HR` (Ecosystem Spec §13.2), `SEALED`, `BOARD_CONFIDENTIAL`, `CREDENTIAL`, `REGULATOR_CONFIDENTIAL` (LDC). `WELLNESS` is rejected at the gateway. Class drives encryption (SPI, HR, SEALED, CREDENTIAL, REGULATOR_CONFIDENTIAL field-encrypted; BOARD_CONFIDENTIAL document-encrypted with a board key), logging (PII and above never logged), export placement (Appendix M restricted folders), AI eligibility (SEALED and CREDENTIAL never; HR and BOARD_CONFIDENTIAL only within the user's permissions and the tenant's AI settings; P17), event `dataclass`.

---

## B.2 `core` — platform core (owner P00)

```sql
CREATE SCHEMA core;

CREATE FUNCTION core.current_tenant() RETURNS text
  LANGUAGE sql STABLE AS $$ SELECT nullif(current_setting('app.tenant_id', true), '') $$;

CREATE TABLE core.tenants (
  id                 text PRIMARY KEY CHECK (id ~ '^ten_[0-9A-HJKMNP-TV-Z]{26}$'),
  slug               text NOT NULL UNIQUE CHECK (slug ~ '^[a-z0-9][a-z0-9-]{1,40}$'),
  legal_name         text NOT NULL,
  display_name       text NOT NULL,
  kind               text NOT NULL CHECK (kind IN ('client','group','platform','ldc_group','provider','sandbox')),
  status             text NOT NULL CHECK (status IN ('lead','trial','active','grace','suspended','offboarding','archived')),
  data_region        text NOT NULL DEFAULT 'ap-south-1' CHECK (data_region IN ('ap-south-1')),
  default_locale     text NOT NULL DEFAULT 'en-IN',
  enabled_locales    text[] NOT NULL DEFAULT ARRAY['en-IN'],
  timezone           text NOT NULL DEFAULT 'Asia/Kolkata',
  fiscal_year_start  char(5) NOT NULL DEFAULT '04-01',
  isolation_tier     text NOT NULL DEFAULT 'shared' CHECK (isolation_tier IN ('shared','dedicated_db','dedicated_cluster')),
  dedicated_key      boolean NOT NULL DEFAULT false,
  byok_key_arn       text NULL,
  parent_tenant_id   text NULL REFERENCES core.tenants(id),
  ecosystem_org_id   text NULL,
  reid               text NULL,
  grc_mode           text NULL CHECK (grc_mode IN ('LDC_EXTERNAL','LDC_GROUP')),
  sandbox_of         text NULL REFERENCES core.tenants(id),
  contract_ref       text NULL,
  trial_ends_at      timestamptz NULL,
  created_at         timestamptz NOT NULL DEFAULT now(),
  updated_at         timestamptz NOT NULL DEFAULT now(),
  version            integer NOT NULL DEFAULT 1
);
-- core.tenants is readable only via platform role or own-tenant policy:
ALTER TABLE core.tenants ENABLE ROW LEVEL SECURITY; ALTER TABLE core.tenants FORCE ROW LEVEL SECURITY;
CREATE POLICY own_tenant ON core.tenants USING (id = core.current_tenant() OR current_setting('app.actor_type', true) = 'platform');

CREATE TABLE core.tenant_domains (
  id text PRIMARY KEY, tenant_id text NOT NULL REFERENCES core.tenants(id),
  host text NOT NULL UNIQUE, kind text NOT NULL CHECK (kind IN ('subdomain','custom')),
  verification_token_hash text, verified_at timestamptz, status text NOT NULL
);

CREATE TABLE core.legal_entities (
  id                 text PRIMARY KEY CHECK (id ~ '^len_[0-9A-HJKMNP-TV-Z]{26}$'),
  tenant_id          text NOT NULL REFERENCES core.tenants(id),
  entity_key         text NOT NULL,               -- stable business key across versions (= first id)
  legal_name         text NOT NULL,
  short_name         text,
  constitution       text NOT NULL,               -- code table core.code_constitution
  cin                text, llpin text, fcrn text,
  pan_enc bytea, pan_bidx bytea, pan_masked text,
  tan                text,
  lei                text CHECK (lei IS NULL OR lei ~ '^[A-Z0-9]{18}[0-9]{2}$'),
  incorporation_date date,
  registered_office  jsonb,                        -- structured address
  state_code         char(2),                      -- registered-office state (labour/co-op packs)
  fiscal_year_start  char(5),
  listing_status     text CHECK (listing_status IN ('UNLISTED','EQUITY_LISTED','DEBT_LISTED','SME_LISTED','UNITS_LISTED')),
  entity_family_codes text[] NOT NULL DEFAULT '{}', -- P15 pack taxonomy, e.g. {'RBI-NBFC','MCA-CO'}
  size_facts         jsonb NOT NULL DEFAULT '{}',  -- asset size, deposits, AUM, turnover, net worth, employees, members: each {value, as_of, source}
  valid_period       tstzrange NOT NULL DEFAULT tstzrange(now(), 'infinity'),
  recorded_at        timestamptz NOT NULL DEFAULT now(),
  superseded_at      timestamptz NOT NULL DEFAULT 'infinity',
  created_by text NOT NULL, source_refs jsonb NOT NULL DEFAULT '[]', correction_id text,
  EXCLUDE USING gist (entity_key WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')
);
CREATE INDEX ON core.legal_entities (tenant_id) WHERE superseded_at = 'infinity';
CREATE INDEX ON core.legal_entities (pan_bidx);

CREATE TABLE core.registrations (
  id text PRIMARY KEY, tenant_id text NOT NULL, legal_entity_key text NOT NULL,
  authority_code text NOT NULL,            -- RBI, SEBI, IFSCA, IRDAI, MCA, RCS-<state>, CRCS, GSTN, EPFO, ESIC, SHOPS-<state>, FIU-IND …
  registration_type text NOT NULL,         -- e.g. NBFC_CoR, AIF_CAT_II, IRDAI_BROKER_DIRECT, IFSCA_FC, MSCS_REG
  registration_no text NOT NULL, issued_on date, valid_until date,
  status text NOT NULL CHECK (status IN ('ACTIVE','SURRENDERED','CANCELLED','SUSPENDED','APPLIED')),
  verified_at timestamptz, verification_source text,
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity'
);

CREATE TABLE core.gstins (
  id text PRIMARY KEY, tenant_id text NOT NULL, legal_entity_key text NOT NULL,
  gstin char(15) NOT NULL CHECK (gstin ~ '^[0-9]{2}[A-Z0-9]{10}[0-9A-Z]Z[0-9A-Z]$'),
  state_code char(2) NOT NULL, status text, verified_at timestamptz, is_billing_default boolean DEFAULT false
);

CREATE TABLE core.entity_relationships (
  id text PRIMARY KEY, tenant_id text NOT NULL,
  from_entity_key text NOT NULL, to_entity_key text NOT NULL,
  rel_type text NOT NULL CHECK (rel_type IN ('HOLDING','SUBSIDIARY','ASSOCIATE','JV','STEP_DOWN','FEDERATION_MEMBER','SPONSOR','MANAGER_OF','TRUSTEE_OF','GROUP_COMPANY')),
  share_pct numeric(9,6), valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity'
);

CREATE TABLE core.org_units (
  id text PRIMARY KEY, tenant_id text NOT NULL, unit_key text NOT NULL,
  legal_entity_key text NULL, parent_unit_key text NULL,
  kind text NOT NULL CHECK (kind IN ('DEPARTMENT','FUNCTION','BRANCH','REGION','COMMITTEE_SECRETARIAT','VERTICAL','COST_CENTRE')),
  code text NOT NULL, name text NOT NULL,
  canonical_function text NULL,           -- platform canonical function code used by content routing
  path ltree NULL,                         -- materialised path for descendant queries (extension ltree)
  head_person_id text NULL,
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity',
  EXCLUDE USING gist (unit_key WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')
);

CREATE TABLE core.data_classes (code text PRIMARY KEY, description text NOT NULL, encryption_required boolean NOT NULL, loggable boolean NOT NULL, ai_eligible text NOT NULL CHECK (ai_eligible IN ('YES','PERMISSION_SCOPED','NEVER')), export_folder text NOT NULL);

CREATE TABLE core.feature_flags (
  key text PRIMARY KEY, owner text NOT NULL, purpose text NOT NULL,
  default_value jsonb NOT NULL, kill_switch boolean NOT NULL DEFAULT false,
  approver_role text NULL, expires_at timestamptz NULL, linked_open_item text NULL
);
CREATE TABLE core.feature_flag_approvals (id text PRIMARY KEY, flag_key text NOT NULL REFERENCES core.feature_flags(key), scope jsonb NOT NULL, new_value jsonb NOT NULL, evidence_doc_id text, requested_by text NOT NULL, approved_by text, approved_at timestamptz, CHECK (approved_by IS NULL OR approved_by <> requested_by));

CREATE TABLE core.tenant_modules (            -- entitlement cache written by bil
  tenant_id text NOT NULL, module_code text NOT NULL, status text NOT NULL CHECK (status IN ('TRIAL','ACTIVE','GRACE','DISABLED')),
  limits jsonb NOT NULL DEFAULT '{}', valid_from timestamptz NOT NULL, valid_to timestamptz, source_subscription_id text,
  PRIMARY KEY (tenant_id, module_code, valid_from)
);

CREATE TABLE core.sequences (tenant_id text NOT NULL, series text NOT NULL, period text NOT NULL, next_value bigint NOT NULL, gap_free boolean NOT NULL, PRIMARY KEY (tenant_id, series, period));

CREATE TABLE core.idempotency_keys (tenant_id text NOT NULL, key text NOT NULL, route text NOT NULL, request_hash bytea NOT NULL, response jsonb, status_code int, created_at timestamptz NOT NULL DEFAULT now(), PRIMARY KEY (tenant_id, key));
```

### B.2.1 Audit ledger, anchors, corrections, access log

```sql
CREATE TABLE core.audit_events (
  chain_id        text NOT NULL,
  seq             bigint NOT NULL,
  event_id        text NOT NULL,
  occurred_at     timestamptz NOT NULL,
  recorded_at     timestamptz NOT NULL DEFAULT clock_timestamp(),
  actor_type      text NOT NULL CHECK (actor_type IN ('user','service','vidhi','platform','delivery','supervisor','auditor','system')),
  actor_id        text NOT NULL,
  on_behalf_of    text NULL,
  membership_id   text NULL,
  act_as_role     text NULL,
  grant_ref       text NULL,               -- delivery/audit/supervisor/break-glass grant
  session_id      text NULL, ip_hash bytea NULL, ua_hash bytea NULL, request_id text NULL, trace_id text NULL,
  module          text NOT NULL,
  action          text NOT NULL,           -- '<module>.<aggregate>.<verb>'
  aggregate_type  text NOT NULL, aggregate_id text NOT NULL, aggregate_version integer NULL,
  before_digest   bytea NULL, after_digest bytea NULL,
  change_set      jsonb NOT NULL DEFAULT '{}',
  reason_code     text NULL, comment_ref text NULL,
  correction_id   text NULL,
  prev_hash       bytea NOT NULL,
  row_hash        bytea NOT NULL,
  PRIMARY KEY (chain_id, seq, recorded_at)
) PARTITION BY RANGE (recorded_at);
-- Append-only: only core.append_audit_event (SECURITY DEFINER) inserts; trigger blocks UPDATE/DELETE/TRUNCATE (LDC-CORE-001).

CREATE TABLE core.audit_anchors (
  id text PRIMARY KEY, chain_id text NOT NULL, anchor_date date NOT NULL,
  first_seq bigint NOT NULL, last_seq bigint NOT NULL, event_count bigint NOT NULL,
  merkle_root bytea NOT NULL, prev_anchor_hash bytea NULL,
  signature bytea NOT NULL, kms_key_id text NOT NULL, tsa_token bytea NULL,
  object_key text NOT NULL, created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (chain_id, anchor_date)
);

CREATE TABLE core.audit_annotations (      -- display layer over immutable events; created only by an APPLIED correction
  id text PRIMARY KEY, chain_id text NOT NULL, event_id text NOT NULL,
  annotation text NOT NULL CHECK (annotation IN ('ENTERED_IN_ERROR','SUPERSEDED','DISPUTED','EXPLAINED')),
  correction_id text NOT NULL, created_at timestamptz NOT NULL DEFAULT now()
);

CREATE TABLE core.correction_entries (
  id                 text PRIMARY KEY CHECK (id ~ '^cor_'),
  tenant_id          text NOT NULL REFERENCES core.tenants(id),
  initiated_from     text NOT NULL CHECK (initiated_from IN ('PLATFORM','TENANT','DELIVERY')),
  scope              text NOT NULL CHECK (scope IN ('RECORD_FIELD','DOCUMENT_VERSION','CONTENT','AUDIT_ANNOTATION','SETTING','ENTITLEMENT','MASTER_DATA','DATE','REVERSAL')),
  target_type        text NOT NULL, target_id text NOT NULL, target_version integer NULL,
  target_fields      text[] NULL, target_event_id text NULL,
  old_value_digest   bytea NULL,
  new_value_enc      bytea NULL, new_value_display jsonb NULL,   -- display only for classes ≤ CONFIDENTIAL
  effective_at       timestamptz NOT NULL,
  recorded_at        timestamptz NOT NULL DEFAULT clock_timestamp(),
  reason_code        text NOT NULL CHECK (reason_code IN ('DATA_ENTRY_ERROR','CLIENT_REQUEST','REGULATOR_DIRECTION','AUDITOR_OBSERVATION','LEGAL_ORDER','MIGRATION_FIX','CONTENT_ERRATUM','SECURITY_INCIDENT','DUPLICATE','OTHER')),
  justification      text NOT NULL CHECK (length(justification) >= 50),
  supporting_doc_ids text[] NOT NULL DEFAULT '{}',
  impact             jsonb NOT NULL DEFAULT '{}',   -- affected tenants/records (content corrections), POST_REPORTING flags
  requested_by       text NOT NULL,
  approved_by        text NULL, approved_at timestamptz NULL,
  second_approved_by text NULL,
  tenant_ack_mode    text NOT NULL CHECK (tenant_ack_mode IN ('PRIOR','POST','NOT_REQUIRED')),
  tenant_ack_by      text NULL, tenant_ack_at timestamptz NULL, tenant_objection_doc_id text NULL,
  state              text NOT NULL CHECK (state IN ('DRAFT','SUBMITTED','APPROVED','APPLIED','REJECTED','WITHDRAWN','REVERSED')),
  applied_event_id   text NULL,
  reverses_id        text NULL REFERENCES core.correction_entries(id),
  visibility         text NOT NULL DEFAULT 'TENANT_VISIBLE' CHECK (visibility = 'TENANT_VISIBLE'),
  CHECK (approved_by IS NULL OR approved_by <> requested_by),
  CHECK (second_approved_by IS NULL OR second_approved_by NOT IN (requested_by, approved_by))
);
ALTER TABLE core.correction_entries ENABLE ROW LEVEL SECURITY; ALTER TABLE core.correction_entries FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON core.correction_entries USING (tenant_id = core.current_tenant() OR current_setting('app.actor_type', true) = 'platform');

CREATE TABLE core.access_log (
  id text PRIMARY KEY, tenant_id text NOT NULL, at timestamptz NOT NULL DEFAULT clock_timestamp(),
  actor_type text NOT NULL, actor_id text NOT NULL, grant_ref text NULL,
  resource_type text NOT NULL, resource_id text NOT NULL, data_class text NOT NULL,
  purpose text NOT NULL, action text NOT NULL CHECK (action IN ('READ','DECRYPT','REVEAL','EXPORT','DOWNLOAD','PRINT','UNMASK')),
  row_count integer NULL, request_id text NULL
) PARTITION BY RANGE (at);

CREATE TABLE core.break_glass_events (
  id text PRIMARY KEY, tenant_id text NOT NULL, requested_by text NOT NULL,
  scope jsonb NOT NULL, justification text NOT NULL CHECK (length(justification) >= 30),
  ticket_ref text NOT NULL, approver_1 text NULL, approver_2 text NULL,
  tenant_consent_by text NULL, starts_at timestamptz NULL, ends_at timestamptz NULL,
  tenant_notified_at timestamptz NULL, dpo_notified_at timestamptz NULL, report_doc_id text NULL,
  state text NOT NULL CHECK (state IN ('REQUESTED','AWAITING_TENANT_CONSENT','APPROVED','ACTIVE','ENDED','REPORTED','DENIED')),
  CHECK (approver_1 IS NULL OR approver_1 <> requested_by)
);
```

### B.2.2 Outbox, inbox, migration lineage

```sql
CREATE TABLE core.outbox (
  id uuid NOT NULL, source text NOT NULL, type text NOT NULL, subject text NOT NULL,
  time timestamptz NOT NULL, datacontenttype text NOT NULL DEFAULT 'application/json',
  dataschema text NOT NULL, data jsonb NOT NULL,
  tenantid text NOT NULL, reid text NOT NULL DEFAULT 'none', dataclass text NOT NULL,
  schemaver text NOT NULL, seq bigint NOT NULL,
  correlationid text NULL, causationid text NULL, traceparent text NULL,
  consentref text NULL, legalbasis text NULL,
  family text NOT NULL CHECK (family IN ('INTERNAL','ECOSYSTEM')),
  status text NOT NULL DEFAULT 'PENDING' CHECK (status IN ('PENDING','PUBLISHED','DEAD')),
  attempts int NOT NULL DEFAULT 0, next_attempt_at timestamptz, published_at timestamptz,
  PRIMARY KEY (id, time),
  CHECK (dataclass NOT IN ('PII','SPI','HR','SEALED','CREDENTIAL') OR consentref IS NOT NULL OR legalbasis IS NOT NULL)
) PARTITION BY RANGE (time);
CREATE UNIQUE INDEX ON core.outbox (subject, seq, time);

CREATE TABLE core.inbox (source text NOT NULL, event_id uuid NOT NULL, type text NOT NULL, subject text, seq bigint, business_key text, received_at timestamptz NOT NULL DEFAULT now(), processed_at timestamptz, status text NOT NULL, PRIMARY KEY (source, event_id));

CREATE TABLE core.migration_runs (id text PRIMARY KEY, wave smallint NOT NULL, source_snapshot_ref text NOT NULL, source_hash bytea NOT NULL, transform_version text NOT NULL, state text NOT NULL, reconciliation_doc_id text, promoted_by text, promoted_at timestamptz);
CREATE TABLE core.migration_lineage (target_table text NOT NULL, target_id text NOT NULL, source_system text NOT NULL, source_collection text NOT NULL, source_id text NOT NULL, source_hash bytea NOT NULL, migration_run_id text NOT NULL REFERENCES core.migration_runs(id), PRIMARY KEY (target_table, target_id));
CREATE TABLE core.migration_genesis (tenant_id text PRIMARY KEY, run_id text NOT NULL, summary jsonb NOT NULL, source_hash bytea NOT NULL, audit_event_id text NOT NULL);
```

---

## B.3 `iam` — identity and access (owner P01)

```sql
CREATE TABLE iam.persons (
  id text PRIMARY KEY CHECK (id ~ '^per_'), tenant_scope text NULL,  -- NULL = cross-tenant person (identity), tenant data in memberships
  full_name_enc bytea NOT NULL, full_name_display text NOT NULL,    -- display name is PII; never logged
  preferred_name text, preferred_language text DEFAULT 'en-IN', timezone text DEFAULT 'Asia/Kolkata',
  accessibility jsonb NOT NULL DEFAULT '{}',                         -- screen_reader, reduced_motion, captions, high_contrast, text_scale
  created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE iam.contact_points (id text PRIMARY KEY, person_id text NOT NULL REFERENCES iam.persons(id), kind text NOT NULL CHECK (kind IN ('EMAIL','MOBILE','WHATSAPP')), value_enc bytea NOT NULL, value_bidx bytea NOT NULL, value_masked text NOT NULL, verified_at timestamptz, is_primary boolean DEFAULT false, UNIQUE (kind, value_bidx));
CREATE TABLE iam.users (id text PRIMARY KEY CHECK (id ~ '^usr_'), person_id text NOT NULL REFERENCES iam.persons(id), realm text NOT NULL CHECK (realm IN ('ldc','ldc-staff')), subject text NOT NULL, status text NOT NULL, mfa_enrolled boolean NOT NULL DEFAULT false, last_login_at timestamptz, UNIQUE (realm, subject));

CREATE TABLE iam.memberships (
  id text PRIMARY KEY CHECK (id ~ '^mbr_'), tenant_id text NOT NULL REFERENCES core.tenants(id), person_id text NOT NULL REFERENCES iam.persons(id),
  kind text NOT NULL CHECK (kind IN ('employee','director','external_professional','auditor','supervisor','delivery','coop_member','marketplace')),
  status text NOT NULL CHECK (status IN ('invited','active','suspended','ended')),
  designation text, hr_employee_ref text NULL, legal_entity_keys text[] NOT NULL DEFAULT '{}', org_unit_keys text[] NOT NULL DEFAULT '{}',
  valid_period tstzrange NOT NULL DEFAULT tstzrange(now(),'infinity'), created_by text NOT NULL, version int NOT NULL DEFAULT 1,
  UNIQUE (tenant_id, person_id, kind)
);
CREATE TABLE iam.role_grants (
  id text PRIMARY KEY CHECK (id ~ '^rgr_'), tenant_id text NOT NULL, membership_id text NOT NULL REFERENCES iam.memberships(id),
  role_code text NOT NULL, kmp_subtype text NULL,
  scope_type text NOT NULL CHECK (scope_type IN ('tenant','legal_entity','org_unit','instrument_pack','committee','audit_engagement','matter','module')),
  scope_ref text NULL, valid_period tstzrange NOT NULL,
  status text NOT NULL CHECK (status IN ('requested','approved','active','rejected','expired','revoked')),
  granted_by text NOT NULL, approved_by text NULL, approved_at timestamptz NULL, sod_override_id text NULL,
  CHECK (approved_by IS NULL OR approved_by <> granted_by)
);
CREATE TABLE iam.sod_rules (id text PRIMARY KEY, role_a text NOT NULL, role_b text NOT NULL, same_scope_required boolean NOT NULL DEFAULT true, severity text NOT NULL CHECK (severity IN ('BLOCK','WARN')), rationale text NOT NULL, source text NOT NULL);
CREATE TABLE iam.delegations (id text PRIMARY KEY, tenant_id text NOT NULL, from_membership_id text NOT NULL, to_membership_id text NOT NULL, role_code text NOT NULL, scope_ref text, valid_period tstzrange NOT NULL, reason text NOT NULL, status text NOT NULL, CHECK (from_membership_id <> to_membership_id));
CREATE TABLE iam.delivery_grants (id text PRIMARY KEY CHECK (id ~ '^dgr_'), tenant_id text NOT NULL, staff_person_id text NOT NULL, engagement_ref text NOT NULL, roles jsonb NOT NULL, scopes jsonb NOT NULL, valid_period tstzrange NOT NULL, proposed_by text NULL, approved_by text NULL, state text NOT NULL CHECK (state IN ('proposed','tenant_approved','active','suspended','ended','rejected')), end_reason text NULL);
CREATE TABLE iam.audit_grants (id text PRIMARY KEY CHECK (id ~ '^agr_'), tenant_id text NOT NULL, grantee_type text NOT NULL, basis_code text NOT NULL, firm_name text, engagement_ref text, grantee_person_ids text[] NOT NULL, scope jsonb NOT NULL, pii_level text NOT NULL, export_level text NOT NULL, valid_from timestamptz NOT NULL, valid_to timestamptz NOT NULL, maker text NOT NULL, checker text NULL, state text NOT NULL, CHECK (valid_to <= valid_from + interval '90 days'), CHECK (checker IS NULL OR checker <> maker));
CREATE TABLE iam.supervisor_grants (
  id text PRIMARY KEY CHECK (id ~ '^sgr_'), tenant_id text NOT NULL, reid text NULL,
  grantee_type text NOT NULL, basis_code text NOT NULL, inspection_ref text NULL, organisation text NOT NULL,
  verified_email_domain text NOT NULL, grantee_person_ids text[] NOT NULL,
  legal_entity_keys text[] NOT NULL, periods jsonb NOT NULL, dataset_catalogue jsonb NOT NULL, record_filters jsonb NOT NULL DEFAULT '{}',
  pii_level text NOT NULL CHECK (pii_level IN ('MASKED','UNMASK_ON_REQUEST','FULL')),
  export_level text NOT NULL CHECK (export_level IN ('NONE','AGGREGATE','CAPPED_RECORDS','FULL')),
  query_level text NOT NULL CHECK (query_level IN ('DASHBOARDS','REPORT_CATALOGUE','ADHOC_READONLY')),
  valid_from timestamptz NOT NULL, valid_to timestamptz NOT NULL,
  re_maker text NOT NULL, re_checker text NULL, second_approver text NULL,
  state text NOT NULL CHECK (state IN ('REQUESTED','BASIS_RECORDED','SCOPE_DEFINED','RE_APPROVED','PROVISIONED','ACTIVE','EXTENDED','EXPIRED','REVOKED','ARCHIVED')),
  federated_from text NULL,   -- Finbyx AU7 / Udofin RA2 grant id when federated
  CHECK (valid_to <= valid_from + interval '90 days'), CHECK (re_checker IS NULL OR re_checker <> re_maker)
);
CREATE TABLE iam.invitations (id text PRIMARY KEY, tenant_id text, kind text NOT NULL, addressed_to_bidx bytea NOT NULL, token_hash bytea NOT NULL UNIQUE, expires_at timestamptz NOT NULL, invited_by text NOT NULL, pending_grants jsonb NOT NULL DEFAULT '[]', state text NOT NULL);
CREATE TABLE iam.consents (id text PRIMARY KEY, person_id text NOT NULL, purpose_code text NOT NULL, notice_version text NOT NULL, given_at timestamptz, withdrawn_at timestamptz, channel text NOT NULL, artefact_hash bytea NOT NULL);
CREATE TABLE iam.kyb_facts (id text PRIMARY KEY, journey_id text NOT NULL, identifier_type text NOT NULL, identifier_bidx bytea NOT NULL, field text NOT NULL, value_enc bytea NULL, value_display jsonb NULL, source text NOT NULL, fetched_at timestamptz NOT NULL, confidence numeric(4,3), user_override jsonb NULL, override_reason text NULL);
CREATE TABLE iam.onboarding_journeys (id text PRIMARY KEY, person_id text NOT NULL, tenant_id text NULL, entry_point text NOT NULL, state text NOT NULL, step_data_enc bytea NOT NULL, started_at timestamptz NOT NULL, last_activity_at timestamptz NOT NULL, health_check_ref text NULL);
```

---

## B.4 `cfg` heads (owner P02; created in P00)

```sql
CREATE TABLE cfg.settings_registry (
  key text PRIMARY KEY CHECK (key ~ '^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$'),
  module text NOT NULL, tier text NOT NULL CHECK (tier IN ('L','G','T')),
  value_type text NOT NULL, default_value jsonb NOT NULL, bounds jsonb NULL,
  allowed_scopes text[] NOT NULL,          -- platform, group, tenant, legal_entity, org_unit, user
  changed_by_roles text[] NOT NULL, approver_role text NULL,
  merge_strategy text NOT NULL DEFAULT 'override' CHECK (merge_strategy IN ('override','narrow_only','widen_only','union','intersection')),
  help_key text NOT NULL, legal_rule_ids text[] NOT NULL DEFAULT '{}', registered_in_phase text NOT NULL, description text NOT NULL
);
CREATE TABLE cfg.setting_values (
  id text PRIMARY KEY, key text NOT NULL REFERENCES cfg.settings_registry(key),
  scope_type text NOT NULL, scope_ref text NOT NULL, tenant_id text NULL,
  value jsonb NOT NULL, reason text NULL, change_request_id text NULL,
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity',
  EXCLUDE USING gist (key WITH =, scope_type WITH =, scope_ref WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')
);
```

---

## B.5 `cnt` — regulatory content library (owner P03; representative)

The content model separates **what the law says** (authority → instrument → version → clause) from **what to do** (obligation → base question/actionable), and both from **what the tenant changed** (overlay). The 30 columns of the owner's Excel template (Appendix E) map to typed fields.

```sql
CREATE TABLE cnt.authorities (code text PRIMARY KEY, name text NOT NULL, country char(2) NOT NULL DEFAULT 'IN', state_code char(2) NULL, kind text NOT NULL CHECK (kind IN ('REGULATOR','MINISTRY','REGISTRAR','STANDARD_SETTER','SRO','EXCHANGE','INTERNATIONAL')), website text, feeds jsonb NOT NULL DEFAULT '[]');
-- e.g. RBI, SEBI, IFSCA, IRDAI, PFRDA, MCA, MEITY, CERTIN, MOLE, MOC (Cooperation), CRCS, RCS-MH, RCS-UP …, ICAI, ICSI, NSE, BSE, FIU-IND, CBIC, CBDT, EU, CA-CPPA

CREATE TABLE cnt.instruments (
  id text PRIMARY KEY CHECK (id ~ '^ins_'), instrument_key text NOT NULL UNIQUE,      -- stable, e.g. 'RBI-MD-NBFC-SBR-2023'
  authority_code text NOT NULL REFERENCES cnt.authorities(code),
  kind text NOT NULL CHECK (kind IN ('ACT','RULES','REGULATIONS','MASTER_DIRECTION','DIRECTION','MASTER_CIRCULAR','CIRCULAR','NOTIFICATION','GUIDELINES','HANDBOOK','FAQ','STANDARD','GUIDANCE_NOTE','PRESS_RELEASE','CONSULTATION','ORDER')),
  title text NOT NULL, short_title text, official_ref text,                            -- e.g. 'RBI/DoR/2023-24/105 DoR.FIN.REC.No.45/03.10.119/2023-24'
  binding_level text NOT NULL, jurisdiction text NOT NULL DEFAULT 'IN',
  subject_tags text[] NOT NULL DEFAULT '{}', status text NOT NULL CHECK (status IN ('DRAFT','IN_FORCE','PARTLY_IN_FORCE','NOT_YET_IN_FORCE','REPEALED','SUPERSEDED','WITHDRAWN')),
  superseded_by_key text NULL, created_at timestamptz NOT NULL DEFAULT now()
);
CREATE TABLE cnt.instrument_versions (
  id text PRIMARY KEY CHECK (id ~ '^ivr_'), instrument_id text NOT NULL REFERENCES cnt.instruments(id),
  version_label text NOT NULL,                 -- 'Original 19-Oct-2023', 'Updated as on 28-Nov-2025'
  issued_on date, updated_on date, effective_from date NOT NULL, effective_to date NULL,
  source_url text NOT NULL, source_sha256 bytea NOT NULL, retrieved_at timestamptz NOT NULL, original_doc_id text NOT NULL,
  ocr_confidence numeric(4,3) NULL, text_extract_doc_id text NULL,
  publication_state text NOT NULL CHECK (publication_state IN ('INGESTED','DRAFTED','IN_REVIEW','APPROVED','PUBLISHED','RETRACTED')),
  published_at timestamptz NULL, published_by text NULL, checker text NULL,
  recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity',
  CHECK (checker IS NULL OR checker <> published_by)
);
CREATE TABLE cnt.clauses (
  id text PRIMARY KEY CHECK (id ~ '^cls_'), instrument_version_id text NOT NULL REFERENCES cnt.instrument_versions(id),
  clause_key text NOT NULL,                    -- stable across versions, e.g. 'para-21-3-b'
  paragraph_ref text NOT NULL,                 -- as printed: 'Para 21(3)(b)', 'Reg 4(2)(a)'
  heading text, text_body text NOT NULL, text_sha256 bytea NOT NULL,
  parent_clause_key text NULL, ordinal int NOT NULL,
  change_vs_prior text NULL CHECK (change_vs_prior IN ('NEW','AMENDED','UNCHANGED','DELETED','RENUMBERED')),
  prior_clause_id text NULL
);
CREATE TABLE cnt.obligations (
  id text PRIMARY KEY CHECK (id ~ '^obl_'), obligation_key text NOT NULL,  -- canonical obligation_ref e.g. 'RBI/DOR/2025-26/352#124' (Ecosystem Spec §5.2 #27)
  clause_ids text[] NOT NULL, instrument_version_id text NOT NULL,
  summary text NOT NULL, obligation_type text NOT NULL,                -- maps to template column O
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity',
  EXCLUDE USING gist (obligation_key WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')
);
CREATE TABLE cnt.questions (                    -- platform base question / actionable (one row = one checkpoint)
  id text PRIMARY KEY CHECK (id ~ '^qst_'), question_key text NOT NULL,   -- stable across versions
  obligation_id text NULL REFERENCES cnt.obligations(id), instrument_version_id text NOT NULL,
  template_code text NOT NULL,                  -- LDC-TPL-<FAMILY>-v1.0 (Appendix E)
  serial_no int NOT NULL,                       -- col B
  applicability_layer text[] NOT NULL,          -- col C (family-specific vocabulary)
  applicability_type text[] NOT NULL,           -- col D (family-specific vocabulary; multi)
  comp_id text NULL,                            -- col E: system-assigned human ref, e.g. 'RBI-NBFC-SBR-0042'
  short_title text NOT NULL,                    -- col F
  question_text text NOT NULL,                  -- col G
  frequency_code text NOT NULL,                 -- col H
  due_rule jsonb NULL,                          -- machine due-date rule derived from H + clause (P04)
  clause_ref text NOT NULL,                     -- col K
  interpretation text NOT NULL,                 -- col L
  department_code text NOT NULL,                -- col M (canonical function)
  related_documents text NULL,                  -- col N
  compliance_type text NOT NULL,                -- col O
  filing_details text NULL,                     -- col P
  consequences text NULL,                       -- col Q
  risk_category text NOT NULL,                  -- col R
  conditional_applicability text NULL,          -- col S
  evidence_expected text NOT NULL,              -- col U
  control_activity text NOT NULL,               -- col V
  citations jsonb NOT NULL,                     -- NN-06
  review_state text NOT NULL CHECK (review_state IN ('NEEDS_REVIEW','DRAFT','IN_REVIEW','APPROVED','PUBLISHED','RETIRED')),
  ai_generated boolean NOT NULL DEFAULT false, ai_run_id text NULL,
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity',
  EXCLUDE USING gist (question_key WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')
);
CREATE TABLE cnt.tenant_overlays (             -- tenant change to a base question, or a tenant-authored question (R-017, NN-03)
  id text PRIMARY KEY CHECK (id ~ '^ovl_'), tenant_id text NOT NULL,
  base_question_key text NULL,                 -- NULL = tenant-authored question
  base_question_version_id text NULL,          -- version the overlay was made against
  overlay_kind text NOT NULL CHECK (overlay_kind IN ('MODIFY','ADD','SUPPRESS')),
  fields jsonb NOT NULL,                       -- only the overridden fields (col F, G, H, L, M, N, R, S, U, V …)
  reason text NOT NULL, approved_by text NULL, state text NOT NULL,
  valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity'
);
-- RLS: cnt.authorities..cnt.questions are platform content (read for all tenants, write only actor_type=platform with content roles);
--      cnt.tenant_overlays is tenant-scoped.
```

---

## B.6 `cmp`, `wf`, `dms`, `chg` — compliance workspace, workflow, documents, change (owners P04, P04, P07, P05; representative)

```sql
CREATE TABLE cmp.tenant_instruments (           -- R-087 catalogue selection
  tenant_id text NOT NULL, instrument_key text NOT NULL, legal_entity_key text NOT NULL,
  selected boolean NOT NULL, selected_by text NOT NULL, selected_at timestamptz NOT NULL,
  deselect_reason text NULL, pinned_version_id text NULL,
  PRIMARY KEY (tenant_id, instrument_key, legal_entity_key)
);
CREATE TABLE cmp.applicability_decisions (
  id text PRIMARY KEY CHECK (id ~ '^app_'), tenant_id text NOT NULL, legal_entity_key text NOT NULL,
  question_key text NOT NULL, decision text NOT NULL CHECK (decision IN ('APPLICABLE','NOT_APPLICABLE','CONDITIONAL','PENDING_CONFIRMATION')),
  basis text NOT NULL CHECK (basis IN ('RULE','USER','DELIVERY','IMPORT')), rule_version text NULL, explanation text NOT NULL,
  decided_by text NOT NULL, valid_period tstzrange NOT NULL, recorded_at timestamptz NOT NULL DEFAULT now(), superseded_at timestamptz NOT NULL DEFAULT 'infinity'
);
CREATE TABLE cmp.compliance_instances (         -- one occurrence of one checkpoint for one entity and period
  id text PRIMARY KEY CHECK (id ~ '^cin_'), tenant_id text NOT NULL, legal_entity_key text NOT NULL,
  question_key text NOT NULL, question_version_id text NOT NULL, overlay_id text NULL,   -- pinned content (NN-03)
  comp_ref text NOT NULL,                       -- human ref shown as CompID
  period_label text NOT NULL, period_start date NULL, period_end date NULL, due_on date NULL,
  org_unit_key text NULL, owner_membership_id text NULL,
  maker_membership_ids text[] NOT NULL DEFAULT '{}', checker_membership_ids text[] NOT NULL DEFAULT '{}', auditor_membership_ids text[] NOT NULL DEFAULT '{}',
  status text NOT NULL,                         -- P04 state machine (col J)
  date_of_compliance date NULL,                 -- col I
  filing_date date NULL,                        -- col Z
  maker_status_update text NULL, maker_comment text NULL,       -- col W, X
  checker_decision text NULL, checker_comment text NULL,        -- col AA, AB
  auditor_comment text NULL,                                    -- col AD
  risk_rating_override text NULL, exception_id text NULL,
  version int NOT NULL DEFAULT 1, created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now(),
  created_by text NOT NULL, updated_by text NOT NULL, source_refs jsonb NOT NULL DEFAULT '[]', correction_id text NULL
);
CREATE INDEX ON cmp.compliance_instances (tenant_id, due_on) WHERE status NOT IN ('APPROVED','NOT_APPLICABLE','CLOSED');

CREATE TABLE wf.tasks (id text PRIMARY KEY CHECK (id ~ '^tsk_'), tenant_id text NOT NULL, kind text NOT NULL, subject_type text NOT NULL, subject_id text NOT NULL, title text NOT NULL, assignee_membership_id text NULL, assignee_agent boolean NOT NULL DEFAULT false, assigned_by text NOT NULL, due_at timestamptz NULL, recurrence jsonb NULL, priority text NOT NULL, state text NOT NULL, origin text NOT NULL CHECK (origin IN ('USER','RULE','VIDHI','IMPORT','ECOSYSTEM','DELIVERY')), created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE wf.approvals (id text PRIMARY KEY CHECK (id ~ '^apr_'), tenant_id text NOT NULL, subject_type text NOT NULL, subject_id text NOT NULL, subject_version int NOT NULL, step int NOT NULL, approver_membership_id text NULL, decision text NULL CHECK (decision IN ('APPROVE','REJECT','REALLOCATE','RETURN')), decided_at timestamptz NULL, acr text NULL, comment text NULL, maker_membership_id text NOT NULL, CHECK (approver_membership_id IS NULL OR approver_membership_id <> maker_membership_id));
CREATE TABLE wf.notifications (id text PRIMARY KEY CHECK (id ~ '^ntf_'), tenant_id text NOT NULL, recipient_membership_id text NOT NULL, category text NOT NULL, subject_type text, subject_id text, title text NOT NULL, body_ref text NULL, channels text[] NOT NULL, state text NOT NULL, created_at timestamptz NOT NULL DEFAULT now(), read_at timestamptz NULL);  -- NN-27: work notifications only
CREATE TABLE wf.calendar_events (id text PRIMARY KEY CHECK (id ~ '^cal_'), tenant_id text NOT NULL, source_type text NOT NULL, source_id text NOT NULL, title text NOT NULL, starts_at timestamptz NOT NULL, ends_at timestamptz NULL, all_day boolean NOT NULL DEFAULT true, audience jsonb NOT NULL, ics_uid text NOT NULL UNIQUE, sequence int NOT NULL DEFAULT 0);

CREATE TABLE dms.documents (id text PRIMARY KEY CHECK (id ~ '^doc_'), tenant_id text NOT NULL, title text NOT NULL, doc_class text NOT NULL, data_class text NOT NULL, confidentiality text NOT NULL CHECK (confidentiality IN ('NORMAL','RESTRICTED','BOARD_ONLY','SEALED')), folder_path_logical text NOT NULL, owner_membership_id text NULL, retention_class text NOT NULL, legal_hold boolean NOT NULL DEFAULT false, current_version_id text NULL, created_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE dms.document_versions (id text PRIMARY KEY CHECK (id ~ '^dvr_'), document_id text NOT NULL REFERENCES dms.documents(id), tenant_id text NOT NULL, version_no int NOT NULL, object_key text NOT NULL, bucket text NOT NULL, sha256 bytea NOT NULL, mime text NOT NULL, size_bytes bigint NOT NULL, original_filename text NOT NULL, uploaded_by text NOT NULL, uploaded_at timestamptz NOT NULL, ocr_text_doc_id text NULL, type_copy_of text NULL, translated_from text NULL, superseded_by_correction text NULL, UNIQUE (document_id, version_no));
CREATE TABLE dms.evidence_ledger (tenant_id text NOT NULL, seq bigint NOT NULL, document_version_id text NOT NULL, sha256 bytea NOT NULL, retain_until date NOT NULL, recorded_at timestamptz NOT NULL DEFAULT clock_timestamp(), prev_hash bytea NOT NULL, row_hash bytea NOT NULL, PRIMARY KEY (tenant_id, seq));
CREATE TABLE cmp.evidence_links (id text PRIMARY KEY CHECK (id ~ '^cev_'), tenant_id text NOT NULL, compliance_instance_id text NOT NULL REFERENCES cmp.compliance_instances(id), document_version_id text NOT NULL, linked_by text NOT NULL, linked_at timestamptz NOT NULL, role text NOT NULL CHECK (role IN ('PRIMARY_EVIDENCE','SUPPORTING','FILING_ACK','WORKPAPER')));

CREATE TABLE chg.sources (id text PRIMARY KEY CHECK (id ~ '^src_'), authority_code text NOT NULL, name text NOT NULL, url text NOT NULL, kind text NOT NULL CHECK (kind IN ('RSS','HTML_LIST','API','EMAIL','MANUAL','LICENSED_FEED','NEWS')), schedule text NOT NULL, last_success_at timestamptz, last_failure_at timestamptz, freshness_sla_hours int NOT NULL, enabled boolean NOT NULL DEFAULT true);
CREATE TABLE chg.source_items (id text PRIMARY KEY CHECK (id ~ '^sit_'), source_id text NOT NULL REFERENCES chg.sources(id), fetched_at timestamptz NOT NULL, item_url text NOT NULL, title text NOT NULL, published_on date NULL, content_sha256 bytea NOT NULL, original_doc_id text NULL, classification text NULL, dedupe_key text NOT NULL UNIQUE);
CREATE TABLE chg.change_notices (id text PRIMARY KEY CHECK (id ~ '^chn_'), source_item_id text NULL, instrument_key text NULL, change_kind text NOT NULL CHECK (change_kind IN ('NEW_INSTRUMENT','AMENDMENT','CORRIGENDUM','REPEAL','FAQ_GUIDANCE','CONSULTATION','ENFORCEMENT_NEWS','NON_ACTIONABLE')), summary text NOT NULL, effective_from date NULL, state text NOT NULL, maker text NOT NULL, checker text NULL, published_at timestamptz NULL, CHECK (checker IS NULL OR checker <> maker));
CREATE TABLE chg.updates (id text PRIMARY KEY CHECK (id ~ '^upd_'), tenant_id text NULL, change_notice_id text NULL, category text NOT NULL CHECK (category IN ('REGULATORY_CHANGE','PLATFORM_ANNOUNCEMENT','PLATFORM_RELEASE','PLATFORM_CORRECTION','SECURITY_NOTICE','SUPPORT_ACCESS')), severity text NOT NULL, title text NOT NULL, what_changed text NOT NULL, why_it_matters text NOT NULL, what_to_do text NOT NULL, audience jsonb NOT NULL, published_at timestamptz NOT NULL, expires_at timestamptz NULL);  -- NN-27: Updates ≠ Notifications
```

### B.6.1 Excel template column → data model map (contract summary; Appendix E is binding for the template itself)

| Col | Header (row 2, exact) | Group (row 1) | Stored in | Who fills |
|---|---|---|---|---|
| A | Checkbox | List | not stored (UI selection) | software |
| B | Serial No. | List | `cnt.questions.serial_no` | content author |
| C | General Applicability(Layer) | List | `applicability_layer[]` | content author |
| D | General Applicability(Type) | List | `applicability_type[]` | content author |
| E | CompID | List | `comp_id` (platform) / `cmp.compliance_instances.comp_ref` (tenant) | software |
| F | Short Title | List | `short_title` | content author |
| G | Compliance Question/Actionable | List | `question_text` | content author |
| H | Due date & Frequency | List | `frequency_code` (+ `due_rule`) | content author |
| I | Date of Compliance | List | `cmp.compliance_instances.date_of_compliance` | maker |
| J | Status | List | `cmp.compliance_instances.status` | software/maker |
| K | Clause or Para no. | Details | `clause_ref` + `citations` | content author |
| L | Interpretation/Explanation | Details | `interpretation` | content author |
| M | Department | Details | `department_code` (canonical function; tenant renames apply in display) | content author |
| N | Related Document or Compliance or Weblinks, if any | Details | `related_documents` | content author |
| O | Compliance Type | Details | `compliance_type` | content author |
| P | Filing and Reporting details/Intimation | Details | `filing_details` | content author |
| Q | Consequences of Non-Compliance/Penalty/Impact | Details | `consequences` | content author |
| R | Risk Categorization | Details | `risk_category` | content author |
| S | Conditional Applicability/Exemptions | Details | `conditional_applicability` | content author |
| T | Maker User/Email ID | Maker | `cmp.compliance_instances.maker_membership_ids` | software |
| U | Upload Document or Evidence | Maker | `evidence_expected` (base) + `cmp.evidence_links` (tenant) | author / maker |
| V | Control Activity | Maker | `control_activity` | content author |
| W | Status Update by Maker User | Maker | `maker_status_update` | maker |
| X | Comments, if any, by Maker User | Maker | `maker_comment` | maker |
| Y | Checker User/Email ID | Checker | `checker_membership_ids` | software |
| Z | Filing/Compliance Date | Checker | `filing_date` | checker |
| AA | Review- Approve, Reject, Reallocate | Checker | `checker_decision` (+ `wf.approvals`) | checker |
| AB | Comments, if any, by Checker User | Checker | `checker_comment` | checker |
| AC | Assigned Auditor/Email ID | Auditor | `auditor_membership_ids` | software |
| AD | Comments, if any, by Auditor | Auditor | `auditor_comment` | auditor |

Header text, including the line break in "Due date & \nFrequency" and the absence of a space before "(Layer)"/"(Type)", is matched exactly as in the owner's sample workbook (row 2), and row 1 group labels "List", "Details", "Maker", "Checker", "Auditor" sit at A1, K1, T1, Y1 and AC1. The importer validates against the template registry (Appendix E), not against this table.

---

## B.7 Events

### B.7.1 Envelope (both families)

CloudEvents 1.0 (spec 1.0.2), structured JSON. Attributes per Ecosystem Spec §3.2: `id` (UUIDv7), `source` (`urn:infrabyx:ldc:<tenantid>`; platform events `urn:infrabyx:ldc:platform`), `type`, `subject` (aggregate id; ordering key), `time` (RFC 3339), `datacontenttype`, `dataschema` (`https://schemas.lawdocscomply.com/<module>/<EventName>/<semver>.json` for internal; the Infrabyx registry URL for ecosystem), `data`, extension attributes `tenantid`, `reid` (`none` where not an RE), `dataclass`, `schemaver`, `seq`, `correlationid`, `causationid`, `traceparent`, `consentref` or `legalbasis` (required when `data` carries personal data).

| Family | `type` pattern | Leaves LDC? | Compatibility |
|---|---|---|---|
| Internal | `in.lawdocscomply.<module>.<EventName>.v<major>` | Never | BACKWARD within major; consumers in the same release |
| Ecosystem | `in.infrabyx.<domain>.<EventName>.v<major>` (names exactly as Ecosystem Spec Part 6) | Yes, only through `int` (P18) | BACKWARD; changes only via the Ecosystem change process |

**Correction to conventions §8:** the conventions file says event `type` = `in.lawdocscomply.<module>.<EventName>.v<n>`. That is right for internal events only. Events that cross into Finbyx, Udofin, Equator or the Operations Hub must use the Ecosystem Spec pattern `in.infrabyx.<domain>.<EventName>.v<major>` with LDC as `source` (e.g., domain `grc` for `ObligationPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `PolicyAttested`, `ReturnStatusUpdated`; `audit` for `ExternalAccessGranted/Used/Revoked`; `governance` for `ResolutionPassed`; `risk` for KRI pulls). The `int` module maps internal → ecosystem events under versioned mapping packs.

### B.7.2 Core event register (P00, P01, P24)

| Event type | Producer | Consumers | Key payload | Data class |
|---|---|---|---|---|
| `in.lawdocscomply.core.TenantProvisioned.v1` | core | cfg, cnt/pack (content load), bil, int (OH ack) | tenant_id, kind, families, modules | INTERNAL |
| `in.lawdocscomply.core.TenantStatusChanged.v1` | core | iam, bil, int | from, to, reason | INTERNAL |
| `in.lawdocscomply.core.LegalEntityRegistered.v1` / `…Amended.v1` | core | pack, gov, ret, int | entity_key, constitution, families, size facts (masked) | CONFIDENTIAL |
| `in.lawdocscomply.core.CorrectionSubmitted.v1` / `…Applied.v1` / `…Reversed.v1` | core | wf (notifications), chg (Updates "Platform correction"), rpt, owning module | correction_id, scope, target, reason_code, approvers | CONFIDENTIAL |
| `in.lawdocscomply.core.AuditAnchorPublished.v1` | core | xpt (export package), eng (evidence) | chain_id, date, merkle_root | INTERNAL |
| `in.lawdocscomply.core.AuditChainBroken.v1` | core | eng (incident), cfg (freeze), chg (Security notice) | chain_id, first_bad_seq | INTERNAL |
| `in.lawdocscomply.core.BreakGlassStarted.v1` / `…Ended.v1` | core | wf, chg (Updates "Support access"), eng | scope, ticket, duration | CONFIDENTIAL |
| `in.lawdocscomply.core.FeatureFlagChanged.v1` | core | all (cache bust), eng | key, scope, value | INTERNAL |
| `in.lawdocscomply.dms.DocumentIngested.v1` / `…Rejected.v1` | dms | cmp, ai (indexing per policy), xpt | document_version_id, sha256, class | per document |
| `in.lawdocscomply.iam.UserInvited.v1`, `…UserActivated.v1`, `…MembershipEnded.v1`, `…RoleGranted.v1`, `…RoleRevoked.v1` | iam | wf, rpt, hr (sync), int (SCIM echo) | membership, role, scope | PII (consentref/legalbasis = CONTRACT_PERFORMANCE_VENDOR) |
| `in.lawdocscomply.iam.DeliveryGrantActivated.v1` / `…Ended.v1` | iam | sdc, wf, int (OH: counts only) | tenant, engagement, staff ref | INTERNAL |
| `in.lawdocscomply.iam.SupervisorGrantActivated.v1` / `…Used.v1` / `…Revoked.v1` | iam | int → `in.infrabyx.audit.ExternalAccessGranted/Used/Revoked.v1` | grant id, grantee type, basis, scope | CONFIDENTIAL |
| `in.lawdocscomply.iam.TrialStarted.v1` / `…TrialExtended.v1` / `…TrialExpired.v1` | iam | bil, web (funnel), int (OH CRM stage) | tenant, ends_at | INTERNAL |
| `in.lawdocscomply.iam.ConsentWithdrawn.v1` | iam | int (OH marketing suppression within 24 h) | person ref, purpose | PII (consentref) |
| `in.lawdocscomply.eng.ReleasePromoted.v1` / `…ReleaseHalted.v1` | eng | chg (Updates "Platform release"), int (`ReleasePublished` to OH13) | version, ring, change ids | INTERNAL |
| `in.lawdocscomply.eng.IncidentDeclared.v1` / `…IncidentClockBreached.v1` | eng | chg (Security notice to affected tenants), int (OH13 counts) | severity, tenants (count), classes | INTERNAL |

Module registers (P02–P23) are compiled into §B.9.

### B.7.3 Delivery guarantees

At-least-once; consumers idempotent on `(source, id)`; ordering per `subject` by `seq`; gap parking 15 minutes then catch-up then `ReconciliationBreakRaised` (Ecosystem Spec §3.5); replay retention ≥ 90 days (365 for long-replay domains); dead-letter after 12 attempts with alert; replays from the console require a reason and are audited.

---

## B.8 Error codes

### B.8.1 Scheme

`LDC-<MODULE>-<NNN>` (module code upper-case; 001–099 validation, 100–199 state/business rule, 200–299 authorisation/assurance, 300–399 integration/dependency, 400–499 data integrity, 900–999 internal). Returned in RFC 9457 problem details with `type = https://api.lawdocscomply.com/problems/LDC-<MODULE>-<NNN>`, `code`, `title`, `status`, `detail` (no PII), `correlation_id`, `retryable`, `errors[]`, and `user_message_key` for the localised UI message. Ecosystem-facing endpoints additionally map to the Ecosystem Spec problem codes (`schema-validation-failed`, `consent-missing`, `scope-insufficient`, `tenant-unknown`, `idempotency-key-reuse`, `request-in-progress`, `state-transition-invalid`, `regulatory-guard`, `rate-limited`, `dependency-unavailable`, `dataclass-not-permitted`, `residency-blocked`, `channel-not-confirmed`).

### B.8.2 Core codes (P00, P01, P24)

| Code | HTTP | Meaning | User message (summary) |
|---|---|---|---|
| LDC-CORE-001 | 409 | Attempt to modify or delete an immutable ledger record | "History can't be changed. Use a correction entry to record a fix." |
| LDC-CORE-002 | 409 | Optimistic concurrency conflict (version mismatch) | "Someone else changed this record. Reload to see the latest version." |
| LDC-CORE-003 | 400 | Missing tenant context | "Select a workspace to continue." |
| LDC-CORE-004 | 422 | Correction justification too short / missing document | "Add a justification of at least 50 characters and the supporting document." |
| LDC-CORE-005 | 403 | Maker and checker must differ | "You created this request, so another person must approve it." |
| LDC-CORE-006 | 409 | Correction target changed since draft | "The record changed after you drafted this correction. Review and resubmit." |
| LDC-CORE-007 | 409 | Target under legal hold | "This document is under legal hold <ref> and can't be withdrawn." |
| LDC-CORE-008 | 409 | Tenant acknowledgement pending (PRIOR mode) | "Waiting for the client's acknowledgement." |
| LDC-CORE-009 | 422 | Effective date outside allowed window for the target | "This date isn't allowed for this record type." |
| LDC-CORE-010 | 422 | Idempotency key reused with different payload | "This request was already sent with different details." |
| LDC-CORE-011 | 409 | Request with this idempotency key in progress | "We're still processing your earlier request." |
| LDC-CORE-012 | 422 | Data class not permitted for destination | "This information can't be sent to that destination." |
| LDC-CORE-013 | 422 | Residency blocked (destination outside India for class) | "This storage location isn't allowed for this type of data." |
| LDC-CORE-014 | 500 | Live provider call attempted from non-production | (internal) |
| LDC-CORE-015 | 409 | Governed changes frozen (audit chain incident) | "Configuration changes are paused while we complete a security check." |
| LDC-CORE-016 | 422 | Overlapping bitemporal version | "Another version already covers these dates." |
| LDC-CORE-017 | 409 | Migration promotion blocked by reconciliation | "Reconciliation found differences. Review the report before promoting." |
| LDC-CORE-018 | 422 | Export mapping missing (build-time, surfaced in console) | (internal) |
| LDC-DMS-001 | 415 | File type not allowed | "This file type isn't supported. Allowed: …" |
| LDC-DMS-002 | 422 | Malware detected | "This file was blocked because it may be harmful." |
| LDC-DMS-003 | 422 | Checksum mismatch | "The upload was corrupted. Please try again." |
| LDC-DMS-004 | 413 | File too large | "Files must be smaller than <n> MB." |
| LDC-IAM-001 | 400 | Invalid or stale request context | "Your session needs to refresh. Please retry." |
| LDC-IAM-003 | 403 | No membership for requested tenant/capacity | "You don't have access to this workspace." |
| LDC-IAM-010 | 403 | Action not permitted by policy | "You don't have permission to do this. Ask your administrator." |
| LDC-IAM-020 | 403 | SoD conflict: maker cannot check own item | "You prepared this item, so another checker must review it." |
| LDC-IAM-021 | 422 | Role combination blocked by SoD rule | "These roles can't be held together on the same area." |
| LDC-IAM-030 | 403 | Delivery grant inactive or out of scope | "LawDocs access for this area isn't active." |
| LDC-IAM-031 | 422 | LawDocs reviewer cannot be sole checker of LawDocs-made items | "Add a checker from your organisation." |
| LDC-IAM-040 | 403 | Supervisor grant read-only (write attempted) | (no write controls are shown; API only) |
| LDC-IAM-041 | 422 | Supervisor grant exceeds 90 days | "Access can be granted for up to 90 days at a time." |
| LDC-IAM-042 | 422 | Grantee email domain does not match recorded authority domain | "Use the official email domain of the authority." |
| LDC-IAM-050 | 403 | Break-glass required | (staff) |
| LDC-IAM-060 | 422 | Trial already used for this organisation identifier | "A trial was already used for this organisation. Contact us to extend." |
| LDC-AUTH-010 | 401 | Step-up authentication required (`required_acr`, `max_age`) | "Confirm it's you to continue." |
| LDC-AUTH-011 | 401 | Session expired | "You've been signed out for security. Sign in again." |
| LDC-AUTH-012 | 403 | MFA enrolment required for role | "Set up a second sign-in step to use this role." |
| LDC-AUTH-013 | 429 | OTP rate limit | "Too many codes requested. Try again in <n> minutes." |
| LDC-AUTH-014 | 403 | SSO enforced for domain | "Your organisation requires signing in with its account." |
| LDC-ENG-001 | 409 | Deployment without approved change | (staff) |
| LDC-ENG-002 | 409 | Deployment in freeze window without exception | (staff) |
| LDC-ENG-003 | 422 | Destructive migration in expand release | (staff, CI) |
| LDC-ENG-004 | 422 | Golden export mismatch | (staff, CI) |

Module codes are compiled in §B.9.

---

## B.9 Compiled module registers

*Compiled by the lead from stream contributions* (`_contrib/S*_events.md`, `_contrib/S*_errors.md`, prefix additions). Sections: B.9.1 event naming rule; B.9.2 module event registers; B.9.3 module error codes. ID prefixes added by phases are listed in each phase file §7.2, and the table ownership map is `db/ownership.yaml` (P00), which is the source of truth.

### B.9.1 Event naming rule (X-01)

Events that cross into Finbyx, Udofin, Equator, LawDocs or the Operations Hub use the Ecosystem Integration Specification v1.1 §3.2 pattern `in.infrabyx.<domain>.<EventName>.v<major>` with `source = urn:infrabyx:ldc:<tenantid>` and are published only by the `int` module from the outbox. Events internal to LawDocsComply and tenant webhooks use `in.lawdocscomply.<module>.<EventName>.v<n>`. `int.event_type_map` relates the two. Where a stream table below lists an ecosystem event by short name, the ecosystem type applies.

### B.9.2 Module event registers

#### Events — stream S11 (P00, P01, P24, App B, Q)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.lawdocscomply.core.TenantProvisioned.v1 | core | cfg, cnt/pack, bil, int (OH ack) | tenant_id, kind, families, modules | P00 |
| in.lawdocscomply.core.TenantStatusChanged.v1 | core | iam, bil, int | from, to, reason | P00 |
| in.lawdocscomply.core.LegalEntityRegistered.v1 / …Amended.v1 | core | pack, gov, ret, int | entity_key, constitution, families | P00 |
| in.lawdocscomply.core.CorrectionSubmitted.v1 / …Applied.v1 / …Reversed.v1 | core | wf, chg, rpt, owning module | correction_id, scope, target, reason, approvers | P00 |
| in.lawdocscomply.core.AuditAnchorPublished.v1 | core | xpt, eng | chain_id, date, merkle_root | P00 |
| in.lawdocscomply.core.AuditChainBroken.v1 | core | eng, cfg, chg | chain_id, first_bad_seq | P00 |
| in.lawdocscomply.core.BreakGlassStarted.v1 / …Ended.v1 | core | wf, chg, eng | scope, ticket, duration | P00/P01 |
| in.lawdocscomply.core.FeatureFlagChanged.v1 | core | all, eng | key, scope, value | P00 |
| in.lawdocscomply.core.MigrationRunPromoted.v1 | core | cnt, eng | run_id, wave, counts | P00 |
| in.lawdocscomply.dms.DocumentIngested.v1 / …Rejected.v1 | dms | cmp, ai, xpt | document_version_id, sha256, class | P00 |
| in.lawdocscomply.iam.UserInvited/UserActivated/MembershipEnded/RoleGranted/RoleRevoked.v1 | iam | wf, rpt, hr, int | membership, role, scope | P01 |
| in.lawdocscomply.iam.DelegationCreated.v1 | iam | wf | from, to, role, period | P01 |
| in.lawdocscomply.iam.DeliveryGrantActivated.v1 / …Ended.v1 | iam | sdc, wf, int (OH counts) | tenant, engagement, staff ref | P01 |
| in.lawdocscomply.iam.AuditGrantActivated.v1 | iam | aud, wf | grant, grantee type, scope | P01 |
| in.lawdocscomply.iam.SupervisorGrantActivated/Used/Revoked.v1 → ECO in.infrabyx.audit.ExternalAccessGranted/Used/Revoked.v1 | iam → int | RE register (Finbyx AU7), SIEM, OH (counts) | grant id, grantee type, basis, scope | P01 |
| in.lawdocscomply.iam.BreakGlassApproved.v1 | iam | core, chg | scope, approvers | P01 |
| in.lawdocscomply.iam.OnboardingStepCompleted.v1 | iam | web (funnel), int (OH CRM stage, consent) | journey, step | P01 |
| in.lawdocscomply.iam.TrialStarted/TrialExtended/TrialExpired.v1 | iam | bil, web, int | tenant, ends_at | P01 |
| in.lawdocscomply.iam.ConsentWithdrawn.v1 | iam | int (OH suppression ≤ 24 h) | person ref, purpose | P01 |
| in.lawdocscomply.iam.PrivacyRequestReceived.v1 | iam | dpc (LDC_GROUP), wf | request id, type | P01 |
| in.lawdocscomply.eng.ReleasePromoted.v1 / …ReleaseHalted.v1 → ECO ReleasePublished (OH13) | eng → int | chg (Updates), OH13 | version, ring, change ids, SBOM hash | P24 |
| ECO ChangeApproved (consumed from OH13) | OH13 | eng deploy gate | change_id, class, approvers, window | P24 |
| in.lawdocscomply.eng.VulnerabilitySlaBreached.v1 | eng | wf, OH13 | vuln id, severity | P24 |
| in.lawdocscomply.eng.RestoreTestFailed.v1 | eng | wf, OH13 | store, test id | P24 |
| in.lawdocscomply.eng.IncidentDeclared.v1 / …IncidentClockBreached.v1 | eng | chg (Security notice), OH13 (counts) | severity, tenants count, classes | P24 |
| ECO ControlEvidenceRecorded (to OH14) | eng → int | OH14 | control id, period, hash | P24 |

#### Events — stream S12 (P02, App A, C, D, U)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.lawdocscomply.cfg.SettingChanged.v1 | cfg | all modules (cache), audit | key, scope_kind, scope_id, tier, change_id | P02 |
| in.lawdocscomply.cfg.ConfigChangeRequested.v1 | cfg | wf (inbox) | request_id, keys[], scope, effective_from | P02 |
| in.lawdocscomply.cfg.ConfigChangeApproved.v1 | cfg | audit | request_id, approver_ref | P02 |
| in.lawdocscomply.cfg.ConfigChangeActivated.v1 | cfg | all modules | request_id, keys[], propagation_mode | P02 |
| in.lawdocscomply.cfg.RulePackVersionSubmitted.v1 | cfg | wf | pack_id, version | P02 |
| in.lawdocscomply.cfg.RulePackVersionActivated.v1 | cfg | cmp, gov, grv, hr, ret, ral, bil | pack_code, version, effective_from, propagation_mode | P02 |
| in.lawdocscomply.cfg.RulePackRetired.v1 | cfg | consumers | pack_code, replacement | P02 |
| in.lawdocscomply.cfg.RulePackReviewDue.v1 | cfg | wf | pack_code, owner_role, due | P02 |
| in.lawdocscomply.cfg.FallbackActivated.v1 | cfg | rpt (health) | key_or_pack, object_ref, kind | P02 |
| in.lawdocscomply.cfg.SettingPackApplied.v1 | cfg | onboarding (P01), rpt | pack_code, version, sections[] | P02 |
| in.lawdocscomply.cfg.OrgNodeChanged.v1 | cfg | cmp, wf, hr, rpt | node_id, change_kind | P02 |
| in.lawdocscomply.cfg.OrgNodesMerged.v1 | cfg | cmp, wf | source_ids[], target_id, job_id | P02 |
| in.lawdocscomply.cfg.WorkflowDefinitionPublished.v1 | cfg | wf | def_id, version, object_type | P02 |
| in.lawdocscomply.cfg.StatusSetPublished.v1 | cfg | modules | object_type, version | P02 |
| in.lawdocscomply.cfg.TenantChangeAckOverdue.v1 | cfg | wf | pack_code, tenant_id | P02 |
| in.lawdocscomply.core.CorrectionEntryRequested.v1 | core | console inbox | correction_id, target_type, target_id | P02 |
| in.lawdocscomply.core.CorrectionEntryApplied.v1 | core | read models, tenant notification, audit | correction_id, target, effective_at, recorded_at | P02 |
| in.lawdocscomply.core.EmergencyOverrideApplied.v1 | core | security | correction_id, incident_id | P02 |
| in.lawdocscomply.cfg.ConfigBundleExported.v1 | cfg | audit | bundle_id | P02 |
| in.lawdocscomply.cfg.ConfigBundleImported.v1 | cfg | audit | bundle_id, applied_counts | P02 |
| in.lawdocscomply.wf.WaitingStarted.v1 | wf | rpt | object_ref, party_type, expected_by | P02/P04 |
| in.lawdocscomply.wf.WaitingChaseSent.v1 | wf | audit | object_ref, chase_no | P02/P04 |
| in.lawdocscomply.wf.EscalationRaised.v1 | wf | notify | object_ref, level | P04 (Appendix A §A.22) |

#### Events — stream S1 (P03–P05, App F)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| cnt.InstrumentVersionCreated.v1 | cnt | chg, ai | instrument_id, version_no, sha256 | P03 |
| cnt.ContentReleasePublished.v1 | cnt | cmp, chg, int | release_id, pack, checkpoints changed | P03 |
| cnt.ObligationPublished.v1 (Ecosystem `ObligationPublished`) | cnt | cmp, Finbyx, Udofin, third-party GRC | obligation_ref, paragraph, text hash, applicability, dates, owner, status | P03 |
| cnt.CheckpointRetired.v1 | cnt | cmp | checkpoint_id, reason | P03 |
| cnt.InstrumentAdopted.v1 / cnt.InstrumentRemoved.v1 | cnt | cmp, rpt | tenant, instrument, reason | P03 |
| cnt.OverlayApproved.v1 / OverlayRebased.v1 / OverlayConflictRaised.v1 | cnt | wf, chg | overlay_id, fields | P03 |
| tpl.ImportJobCompleted.v1 | tpl | wf | job_id, counts | P03 |
| tpl.TemplateVersionActivated.v1 | tpl | ai, cnt | template_code | P03 |
| core.CorrectionEntryApproved.v1 | core | all | target, field, old, new, reason | P03 |
| cmp.InstanceCreated.v1 / InstanceSubmitted.v1 / InstanceReviewed.v1 / InstanceOverdue.v1 / InstanceEscalated.v1 | cmp | wf, rpt, int | instance_ref, status | P04 |
| cmp.EvidenceSubmitted.v1 (Ecosystem `EvidenceSubmitted`) | cmp | int | instance, hashes | P04 |
| cmp.ComplianceEventRecorded.v1 | cmp | cmp, wf | event type/date | P04 |
| cmp.ComplianceIssueRaised.v1 (Ecosystem `ComplianceIssueRaised`) | cmp | erm, aud, int | exception, severity, owner, due | P04 |
| cmp.ExceptionClosed.v1 / CertificateSigned.v1 | cmp | gov, rpt | ids | P04 |
| wf.TaskAssigned.v1 / TaskCompleted.v1 / ScheduleRunCompleted.v1 / CalendarSyncFailed.v1 | wf | notify, ai | ids | P04 |
| chg.ItemDetected.v1 / ChangeItemTriaged.v1 | chg | console | item, class, urgency | P05 |
| chg.ChangePublished.v1 | chg | cmp, int | change_id, release_id, tenants | P05 |
| chg.DueDateExtensionPublished.v1 | chg | cmp | checkpoints, periods, new due | P05 |
| chg.UpdateDelivered.v1 / UpdateAcknowledged.v1 | chg | rpt | update, tenant | P05 |
| chg.ImpactAssessmentSignedOff.v1 / ChangeImplemented.v1 | chg | gov, rpt, aud | impl_id | P05 |
| chg.SourceHealthChanged.v1 | chg | ops alerts | source, health | P05 |
| ai.StudioRunCompleted.v1 / PromptTemplatePromoted.v1 | ai | tpl, console | run_id, metrics | P05 |

#### Events — stream S2 (App E, templates)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.lawdocscomply.tpl.TemplatePublished.v1 | tpl | cnt, web (template catalogue), hlp | template_code, family_code, version, header_sha256 | P03 |
| in.lawdocscomply.tpl.TemplateDeprecated.v1 | tpl | cnt, notifications | template_code, successor_code, grace_until | P03 |
| in.lawdocscomply.tpl.ContentImportSubmitted.v1 | tpl | audit ledger, wf (review task) | job_id, scope, instrument_version_id, file_sha256, rows | P03 |
| in.lawdocscomply.tpl.ContentImportValidated.v1 | tpl | wf, notifications | job_id, errors, warnings, infos, actions{new,update,retire} | P03 |
| in.lawdocscomply.tpl.ContentImportCommitted.v1 | tpl | cnt, audit ledger | job_id, obligation_version_ids[] | P03 |
| in.lawdocscomply.cnt.ObligationPublished.v1 (Ecosystem Spec name) | cnt | cmp, chg (Updates), int (GRC connector), Finbyx/Udofin (LDC_EXTERNAL mode) | comp_id, obligation_ref, version, change_class, valid_from | P03/P05 |
| in.lawdocscomply.cnt.ObligationRetired.v1 | cnt | cmp, chg | comp_id, omitted_by, valid_to | P05 |
| in.lawdocscomply.cnt.ObligationCorrected.v1 | cnt | cmp, audit ledger, chg | comp_id, corrected_version, correction_entry_id | P05 |
| in.lawdocscomply.cmp.TenantOverlayCreated.v1 | cmp | audit ledger, chg (merge tasks) | tenant_id, comp_id, fields_changed[], approver | P03 |
| in.lawdocscomply.ai.QuestionDraftGenerated.v1 | ai | tpl, wf | run_id, family_code, rows, prompt_version, model | P05/P17 |

#### Events — stream S3 (P06–P07)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| gov.BlueprintEvaluated | gov | cmp, rpt | legal_entity_id, blueprint_version, gap_count, rule_pack_versions | P06 |
| gov.GovernanceGapDetected / GovernanceGapResolved | gov | cmp (issues), wf | requirement_key, lr_ids, status, issue_id | P06 |
| gov.CommitteeConstituted / CommitteeCompositionChanged | gov | hr, Finbyx (authority matrix), rpt | body_id, statutory_roles, members[], effective_from | P06 |
| gov.CompositionBreachDetected | gov | cmp, wf | body_id, rule_id, findings | P06 |
| gov.DirectorAppointed / DirectorCeased | gov | hr, Finbyx, Udofin (where governance projection subscribed), cmp | person_ref, din, category, effective_on | P06 |
| gov.KmpAppointed / KmpCeased | gov | hr, Finbyx, cmp | person_ref, designation, effective_on, approval_refs | P06 |
| gov.MeetingScheduled / NoticeIssued / BoardPackPublished / MeetingConcluded | gov | wf (calendar, notifications), rpt | meeting_id, body_id, scheduled_at, pack_version | P06 |
| gov.DecisionRecorded | gov | pol, cmp, wf, ret | meeting_id, item_id, outcome, resolution_ref, follow_on[] | P06 |
| gov.MinutesCirculated / MinutesSigned / MinutesSealed | gov | wf, xpt, aud | meeting_id, document_id, hash | P06 |
| gov.CircularResolutionPassed | gov | pol, cmp, wf | circular_id, tally, resolution_ref | P06 |
| gov.RegisterEntryPosted / RegisterCorrectionPosted | gov | aud, xpt | register_code, entry_id, correction_of | P06 |
| gov.FilingDue / FilingFiled / FilingOverdue | gov | cmp, wf, rpt, bil (savings ledger) | filing_instance_id, form_code, due_on, srn, additional_fee | P06 |
| gov.DeclarationSubmitted / FitAndProperCertified | gov | cmp, wf | person_ref, form_code, period | P06 |
| gov.RegulatorApprovalRecorded | gov | cmp | approval_type, portal, reference_no | P06 |
| gov.DisclosureCaseOpened / DisclosureDisseminated / DisclosureDelayed | gov | cmp, wf, rpt | case_id, para, clock_start, disseminated_at, delay_reason | P06 |
| gov.RptThresholdApproaching | gov | wf, cmp | related_party_ref, cumulative, threshold, pct | P06 |
| gov.TradingWindowClosed / TradingWindowOpened | gov | wf (notify designated persons) | window_id, from, to, reason | P06 |
| gov.SddEntryRecorded | gov | aud | sdd_id, upsi_id, recipient_ref, shared_at, hash | P06 |
| gov.AnnualReportDraftReady | gov | wf | fy, section_keys | P06 |
| pol.PolicyDrafted / PolicySubmittedForReview / PolicyReviewDecided | pol | wf | policy_id, version, stage | P07 |
| pol.PolicyReadyForApproval | pol | gov (auto agenda item), wf | policy_id, version, hash, approver_body | P07 |
| pol.PolicyApproved / PolicyEffective / PolicyRetired | pol | cmp (evidence), hr (attestation audience), xpt, Finbyx/Udofin (policy references, Ecosystem Spec `grc`) | policy_id, version, effective_on, decision_ref | P07 |
| pol.PolicyReviewDue / PolicyReviewOverdue | pol | cmp, wf | policy_id, due_on | P07 |
| pol.PolicyAttested (Ecosystem Spec name) | pol | cmp, Finbyx/Udofin (`grc`) | policy_id, version, person_ref, attested_at | P07 |
| pol.AttestationCampaignCompleted | pol | cmp, rpt | campaign_id, completion_pct | P07 |
| pol.ModelTemplatePublished | pol (platform) | chg (Updates feed), tenants | template_id, version, clause_diff_ref | P07 |
| dms.DocumentUploaded / DocumentVersioned / DocumentSealed / DocumentQuarantined | dms | ai (indexing), cmp, xpt | document_id, version, sha256, doc_type | P07 |
| dms.TypeCopyVerified / TranslationReviewed | dms | cmp, grv | document_id, verified_by | P07 |
| dms.ShareCreated / ShareAccessed / ShareRevoked | dms | aud, gov (SDD if UPSI) | share_id, items, recipient_ref | P07 |
| dms.EnvelopeSent / EnvelopeCompleted / EnvelopeDeclined | dms | gov, hr, mkp, pol | envelope_id, documents, signers_status, certificate_id | P07 |
| dms.IntakeJobCompleted | dms | wf, cmp | job_id, counts, exceptions | P07 |
| dms.LegalHoldPlaced / LegalHoldReleased / DocumentsDisposed | dms | aud, xpt | hold_id / batch_id | P07 |
| dms.EvidenceSubmitted (Ecosystem Spec name) | dms/cmp | cmp, aud, Finbyx/Udofin (`grc`) | evidence_id, obligation_ref, hashes | P07 |

#### Events — stream S4 (P08–P09, App H)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.lawdocscomply.erm.RiskRegistered.v1 | erm | rpt, aud (audit universe), ai index | risk_id, taxonomy_node, owner, legal_entity_id | P08 |
| in.lawdocscomply.erm.RiskAssessed.v1 | erm | rpt, aud, gov packs | risk_id, assessment_id, inherent, final_residual, valid_from | P08 |
| in.lawdocscomply.erm.RiskRetired.v1 | erm | rpt | risk_id, reason | P08 |
| in.lawdocscomply.erm.RasApproved.v1 | erm | rpt, gov, Finbyx (via GRC API) | ras_id, version, board_ref, effective_from | P08 |
| in.lawdocscomply.erm.RasThresholdApproved.v1 | erm | Finbyx, Udofin (pull GET /v1/grc/kris) | metric_id, levels, threshold_version, ldc_approval_ref | P08 |
| in.lawdocscomply.erm.KriDefined.v1 | erm | int (served to FX/UD) | kri_id, metric_id, thresholds | P08 |
| in.lawdocscomply.erm.KriBreachOpened.v1 | erm | wf (notifications), rpt | episode_id, kri_id, value, rag, source | P08 |
| in.lawdocscomply.erm.KriBreachCured.v1 | erm | wf, rpt | episode_id, peak, duration | P08 |
| in.lawdocscomply.erm.LimitBreachEpisodeUpdated.v1 | erm | wf, cmp (regulatory intimation task) | episode_id, limit_type, status, citation | P08 |
| in.lawdocscomply.erm.RcsaCampaignLaunched.v1 | erm | wf | campaign_id, scope, due | P08 |
| in.lawdocscomply.erm.RcsaCampaignFinalised.v1 | erm | aud (risk-based audit universe) | campaign_id, unit scores | P08 |
| in.lawdocscomply.erm.LossEventValidated.v1 | erm | ral (ICAAP op-risk), rpt | loss_event_id, version, L1/L2, net, dates | P08 |
| in.lawdocscomply.erm.RiskIssueRaised.v1 (maps to ComplianceIssueRaised for external GRC destinations) | erm | cmp, aud | issue_id, source, severity, owner, due | P08 |
| in.lawdocscomply.erm.RiskAccepted.v1 / RiskAcceptanceExpired.v1 | erm | rpt, gov | acceptance_id, authority, expires_at | P08 |
| in.lawdocscomply.erm.RmcPackFrozen.v1 (also EvidenceSubmitted in group mode) | erm/gov | gov, dms | pack_id, hash, meeting_id | P08 |
| in.lawdocscomply.erm.ControlTestRecorded.v1 | erm | cmp, aud | control_id, period, result, source | P08 |
| in.infrabyx.risk.KriBreached.v1 (inbound) | Finbyx, Udofin | erm | kri_id, metric version, value, threshold version, RAG, episode_id, status, update_seq | P08 |
| in.infrabyx.risk.LimitBreached.v1 (inbound) | Finbyx, Udofin | erm, ral | limit_id, limit_type, status, value, limit, projected, citation, pseudonymised ref | P08/P09 |
| in.infrabyx.risk.LossEventRecorded.v1 (inbound) | Finbyx, Udofin | erm | taxonomy, 3 dates, gross, recoveries, net (banded), root cause | P08 |
| in.infrabyx.risk.RiskSnapshotPublished.v1 (inbound) | Finbyx, Udofin | erm, ral | metric ids, versions, values, thresholds, RAG, certification state | P08/P09 |
| in.infrabyx.risk.CapitalRatioComputed.v1 (inbound) | Finbyx | ral | legal_entity, run type, as_of, CET1, T1, T2, RWA by class, CRAR, leverage, headroom, PCA proximity, rule-pack version | P09 |
| in.infrabyx.risk.StressTestCompleted.v1 (inbound) | Finbyx | ral | scenario id/version, horizon, snapshot hash, model versions, summary per period | P09 |
| in.infrabyx.risk.RiskSegmentSnapshotPublished.v1 (PROPOSED) | Finbyx | ral | segment-level aggregates (no PII), as_of, hash | P09 |
| in.lawdocscomply.hr.PeopleMetricPublished.v1 (inbound from P13) | hr | erm, ral | metric_id, value, population_size, suppression_applied | P08 |
| in.lawdocscomply.ral.SnapshotFrozen.v1 | ral | rpt, ret | snapshot_id, as_of, hash | P09 |
| in.lawdocscomply.ral.CapitalRunCertified.v1 | ral | rpt, ret (DNBS03 elements), erm (KRIs) | run_id, run_no, ratios, kernel/rule versions | P09 |
| in.lawdocscomply.ral.MetricValueCertified.v1 | ral | rpt, erm | metric_id, version, value, as_of, certifier | P09 |
| in.lawdocscomply.ral.MetricDefinitionChanged.v1 | ral | rpt, ret, erm | metric_id, old/new version, effective_from | P09 |
| in.lawdocscomply.ral.AlmRunCertified.v1 | ral | ret (DNBS04A/B), erm | run_id, SLS, IRS, LCR | P09 |
| in.lawdocscomply.ral.LcrBelowMinimum.v1 | ral | erm (limit episode), cmp | lcr, as_of, citation ALM para 62 | P09 |
| in.lawdocscomply.ral.StressRunApproved.v1 | ral | erm (packs), ICAAP | run_id, scenarios, results summary | P09 |
| in.lawdocscomply.ral.ReverseStressCompleted.v1 | ral | erm | target, breaking point, convergence | P09 |
| in.lawdocscomply.ral.ScenarioApproved.v1 | ral | rpt | scenario_id, version, approver | P09 |
| in.lawdocscomply.ral.IcaapStateChanged.v1 / IcaapApproved.v1 (+ EvidenceSubmitted) | ral | gov, dms, external GRC destination | cycle_id, state, board_ref, doc hash | P09 |
| in.lawdocscomply.ral.PcaStateChanged.v1 | ral | gov (restriction gates), cmp, erm | state, threshold, letter ref | P09 |

#### Events — stream S5 (P10–P11, App I–J)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| aud.AuditEngagementOpened.v1 | LDC aud (LDC-hosted) | Tenant GRC, ACB dashboard, Finbyx (if subscribed) | engagement_id, type (INTERNAL, RBIA, CONCURRENT, IS, IT, STATUTORY, SECRETARIAL, TAX, VAPT), period, scope summary, lead role, workpaper index ref | P10 |
| aud.AuditFindingRaised.v1 | LDC aud | P04, P08, ACB, Finbyx/Udofin (if finding relates to their scope) | finding_id, version, engagement_id, rating, criteria citation, owner role, due date, masked sample refs | P10 |
| aud.AuditFindingClosed.v1 | LDC aud | Same | closure evidence hashes, validator role, closed_at | P10 |
| aud.AuditPlanPublished.v1 | LDC aud | P06 (ACB), dashboards | plan_id, fy, version, acb_minute_ref | P10 |
| aud.AuditReportIssued.v1 | LDC aud | P06, P07 DMS | report_id, engagement_id, sha256, template version | P10 |
| aud.AcbPackFrozen.v1 | LDC aud | P06 agenda | pack_id, meeting_id, sha256 | P10 |
| aud.RiskAcceptanceExpiring.v1 | LDC aud | Owners, CRO, ACB | finding_id, expiry | P10 |
| aud.VulnerabilitySlaBreached.v1 | LDC aud | CISO, ITSC, P12 | vuln_id, severity, asset, due | P10 |
| aud.DNBS10Due.v1 | LDC aud | Auditor room, CFO | entity, FY, due_at | P10 |
| aud.SecretarialCheckFailed.v1 | LDC aud | CS, P06 | meeting_id, check code, clause | P10 |
| aud.InspectionRequestDue.v1 | LDC aud | CCO, owners | inspection_id, request_id, due | P10 |
| cmp.ControlTestResultPublished.v1 | LDC aud/cmp | Tenant GRC, OSCAL export | run, period, result, population hash, masked sample, artefact hashes | P10 |
| cmp.EvidenceSubmitted.v1 | LDC aud | Tenant GRC | evidence hashes, obligation refs | P10 |
| cmp.ComplianceIssueRaised.v1 | LDC aud, ret | P04, CCO | source (AUDIT, RETURN_OVERDUE, BUREAU_LATE), severity, owner, due | P10/P11 |
| ret.ReturnDue.v1 | LDC ret (native) | P04 calendar, OH (status metadata if opted in) | instance_id, regulator, portal, return_code, entity, period, due_at, alert_stage, citation | P11 |
| ret.ReturnGenerated.v1 / ReturnValidated.v1 / ReturnApproved.v1 / ReturnFiled.v1 / ReturnRevised.v1 / ReturnStatusUpdated.v1 | LDC ret (native runs) | P04, P10, dashboards, OH (Filed metadata if opted in) | per Ecosystem Spec §6.18 payloads | P11 |
| ret.BureauFileGenerated.v1 / BureauFileSubmitted.v1 / BureauRejectionReceived.v1 | LDC ret (non-Finbyx lenders) | P04, P10 | cic, layout, cycle, reference date, counts, file hash | P11 |
| ret.GstReturnPrepared.v1 / TdsStatementPrepared.v1 | LDC ret | P04, P10 | gstin/tan, period, form, package hash | P11 |
| acc.FinancialStatementsApproved.v1 | LDC acc (non-Finbyx tenants) | ret (DNBS10, audited returns), P06, P10 | entity, FY, framework, Board date, audit report date, statement hashes | P11 |
| ret.DataBatchAccepted.v1 | LDC ret | ret pipelines, P10 analytics | batch_id, dataset, period, row_count, control totals | P11 |
| ret.MappingApproved.v1 | LDC ret | Revision trigger | mapping_id, version, affected periods | P11 |
| acc.FinancialDataSetReady.v1 | LDC acc | P09 ratios, P06 annual report | entity, period, element set version | P11 |
| ret.RegistryVarianceRecorded.v1 | LDC ret | CCO dashboard | return, field, decision | P11 |
| Consumed: AuditEngagementOpened / AuditFindingRaised / AuditFindingClosed (Finbyx, Udofin) | Finbyx, Udofin | aud mirror | §6.21 | P10 |
| Consumed: Return*, Bureau*, PeriodClosed, FinancialStatementsApproved, GstReturnPrepared, TdsStatementPrepared | Finbyx | ret mirror | §6.18–6.20 | P11 |
| Consumed: ExternalAccessGranted/Used/Revoked | P01, Finbyx, Udofin | aud rooms | §6.21 | P10 |
| Consumed: EntityProfileChanged (P15), InstrumentVersionPublished (P03), PayrollRunApproved (P13), ResolutionPassed / MeetingMinutesSigned (P06), AssetRegistered / OutsourcingArrangementApproved (P12), EmployeeRoleChanged (P13) | Internal | aud/ret | — | P10/P11 |

#### Events — stream S6 (P12–P14, App T)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| ProcessingActivityApproved | dpc | cmp, rpt, xpt | activity_id, version, bases, retention_class | P12 |
| ROPAPublished | dpc | dms, xpt | view, as_of, file_hash | P12 |
| NoticePublished | dpc | web widget, int | notice_version_id, languages, url | P12 |
| ConsentRecorded (Ecosystem) | dpc (when capturer) | recipients per artefact | consent artefact | P12 |
| ConsentWithdrawn (Ecosystem) | dpc | every recipient | consentref, scope, withdrawn_at | P12 |
| DataPrincipalRequest (Ecosystem) | dpc ↔ Finbyx/Udofin | fiduciary systems | request_id, type, scope, status, due | P12 |
| RightsRequestClosed | dpc | rpt, grv | request_id, outcome, law_codes | P12 |
| DPIAApproved | dpc | erm, cmp | assessment_id, residual_score | P12 |
| IncidentReported | dpc | wf, CISO/DPO inbox | incident_id, severity, source | P12 |
| IncidentClassified | dpc | wf (clock engine), erm | classification, personal_data_breach | P12 |
| IncidentClockStarted / IncidentClockBreached | dpc | wf, rpt, Board pack | clock_key, due_at / lapsed_at | P12 |
| RegulatorNotificationSubmitted | dpc | cmp (evidence), rpt | destination, submitted_at, ack_ref | P12 |
| SecurityIncidentNotified (Ecosystem) | dpc | Finbyx/Udofin/RE GRC (linked tenants) | detected_at, notified_re_at, rbi_reported_at | P12 |
| ControlTestCompleted | dpc | cmp, aud | control_id, result, evidence_ids | P12 |
| ComplianceIssueRaised (Ecosystem) | dpc/aud | cmp, erm, ecosystem GRC | source, severity, owner, due | P12 |
| VulnerabilityOverdue | dpc | wf, CISO | finding_id, severity, sla_due_at | P12 |
| DRTestCompleted | dpc | cmp, rpt | plan_id, achieved_rto, achieved_rpo | P12 |
| VendorTierChanged | tpr | wf, erm | vendor_id, old, new | P12 |
| OutsourcingArrangementApproved | tpr | cmp, rpt | arrangement_id, kind, materiality | P12 |
| OutsourcingReviewDue | tpr | wf | arrangement_id, due_at | P12 |
| VendorIncidentReported | tpr (vendor portal) | dpc (incident + outsourced clock) | provider_detected_at | P12 |
| AISystemAssessed | dpc | erm (model risk), ai | ai_system_id, risk_level | P12 |
| EmployeeHired | hr | iam (SCIM), gov, cmp | employment_id, position, establishment | P13 |
| EmploymentConfirmed | hr | rpt | employment_id | P13 |
| EmployeeTransferred | hr | iam, cmp, hr payroll | employment_id, from/to establishment | P13 |
| RegulatedRoleAssigned / RegulatedRoleVacated | hr | gov (P06), cmp (IO/KMP intimation clocks) | role_code, person_id, effective_at | P13 |
| EmployeeSeparated | hr | iam, wf (task reassignment), WORKSPACE_PORT | employment_id, exit_effective_at | P13 |
| AccessRevocationRequested | hr | iam | person_id, deadline | P13 |
| LeaveApproved | hr | wf calendar, payroll, iam (mandatory-leave access suspension) | employment_id, dates, type (hidden if sensitive) | P13 |
| PayRunComputed / PayRunReleaseAuthorised | hr | acc, rpt | run_id, register_hash, param_versions | P13 |
| BankFileIssued / DisbursalReconciled | hr | acc | file_hash, counts, failures | P13 |
| StatutoryFileGenerated | hr/lab | cmp (evidence) | form_code, period, file_hash | P13 |
| RegisterPublished | lab | dms, cmp | register_code, establishment, period, hash | P13 |
| ThresholdCrossed | lab | cmp, wf | establishment_id, threshold_code, headcount | P13 |
| CommitteeCompositionInvalid | lab/gov | wf, cmp | committee_id, rule | P13 |
| POSHCaseClockBreached | lab_posh | sealed exception (IC PO only) | ic_id, count only | P13 |
| TrainingOverdue | hr | wf | employment_id, course_ref | P13 |
| PeopleKRIPublished | hr | erm; ecosystem `workforce` (aggregates, opt-in) | metric_id, version, value, grain | P13 |
| GrievanceRaised (Ecosystem) | Udofin/Finbyx/Equator/LDC intake | grv host | channel, category, description | P14 |
| GrievanceUpdated / GrievanceEscalated / GrievanceReopened / GrievanceRated (Ecosystem) | grv | Udofin, Finbyx | status, level, rating | P14 |
| OmbudsmanReferralRecorded (Ecosystem) | complainant declaration / RE | grv, Udofin, LDC MIS | forum, external_ref, stage | P14 |
| TicketAcknowledged | grv | channel adapters | ticket_id, ref_no | P14 |
| ClockWarning / ClockBreached | grv | wf, CCO, Board pack | clock_key, pct_elapsed / lapsed_at | P14 |
| IOReviewCreated / IODecisionOverruled | grv | IO desk / Board review | ticket_id, forward_by / overrule details | P14 |
| FinalReplySent | grv | cmp (evidence), MIS | ticket_id, decision | P14 |
| ReportSubmitted | grv | cmp | report_code, period, ack_ref | P14 |
| ConductKRIPublished | grv | erm | metric_id, value | P14 |

#### Events — stream S7 (P15–P16, App G, S)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.lawdocscomply.pack.EntityProfileActivated.v1 | pack | cmp, wf, rpt, OH (counts only) | legal_entity_id, families[], pack_versions | P15 |
| in.lawdocscomply.pack.EntityProfileAttributeChanged.v1 | pack | pack detector, rpt | attr_code, old/new (masked if confidential), source, as_of | P15 |
| in.lawdocscomply.pack.EntityClassificationChanged.v1 | pack | cmp, gov, erm, ret, wf | scheme, old, new, effective_at, change_id | P15 |
| in.lawdocscomply.pack.ProfileChangeDetected.v1 | pack | wf (tasks), notifications | scheme, proposed, impact summary, due_at | P15 |
| in.lawdocscomply.pack.ProfileChangeApproved.v1 | pack | cmp, gov, ret | change_id, approvers, effective_at | P15 |
| in.lawdocscomply.pack.ApplicabilityRecomputed.v1 | pack | cmp, rpt, chg (Updates) | tenant, added, removed, changed counts, versions | P15 |
| in.lawdocscomply.pack.ExemptionApproved.v1 / ExemptionExpired.v1 | pack | cmp, wf | obligation_ids, valid_to | P15 |
| in.lawdocscomply.pack.ApplicabilityOverlayApproved.v1 | pack | cmp, aud | obligation_id, kind, reason | P15 |
| in.lawdocscomply.pack.SectorPackApplied.v1 | pack | gov, erm, pol, ret, rpt | pack_version, seeded object counts | P15 |
| in.lawdocscomply.pack.SectorPackVersionPublished.v1 | pack (console) | chg (Updates), tenants | family, version, effective_from | P15 |
| in.lawdocscomply.pack.JurisdictionPackPublished.v1 | pack (console) | chg | iso_code, version, reviewer | P15 |
| in.lawdocscomply.pack.InvestmentMonitorBreached.v1 | pack (imported registers) | cmp (issue), erm, rpt | monitor_code, value, limit, episode_id | P15 |
| in.lawdocscomply.pack.ListedEventDisclosureDue.v1 | pack | wf, notifications | event_type, due_at | P15 |
| (consumed) PositionValued, InvestmentLimitBreached, LimitBreached, AssetAcquired, SecurityReceiptIssued, SrNavPublished | Finbyx | pack | per Integration Spec §6.22, §6.25 | P15 |
| in.lawdocscomply.coop.SocietyActivated.v1 | coop | wf, rpt | act_code, state, sor_members | P16 |
| in.lawdocscomply.coop.ByelawAmendmentRegistered.v1 | coop | pack (L3 layer), cmp | version, registrar_ref, effective_from | P16 |
| MemberAdmitted (Integration Spec §6.24 name; SoR = LDC only) | coop | Udofin, LOS | lender id, member party_ref, class, admitted_at | P16 |
| ShareCapitalPosted (SoR = LDC only) | coop | Udofin, LOS | member ref, txn type, shares after | P16 |
| in.lawdocscomply.coop.MemberStatusChanged.v1 | coop | gov (voter eligibility) | member_ref, old, new | P16 |
| in.lawdocscomply.coop.MembershipDeemedRefused.v1 | coop | cmp (Critical issue) | application_id, deadline | P16 |
| in.lawdocscomply.coop.GeneralBodyMeetingHeld.v1 / GeneralBodyMeetingDefaulted.v1 | coop | cmp, rpt | fy, held_at / due_by | P16 |
| in.lawdocscomply.coop.ElectionAuthorityInformed.v1 | coop | cmp | term_end, informed_at | P16 |
| in.lawdocscomply.coop.BoardConstituted.v1 | coop | gov, iam (roles) | members[], effective_from | P16 |
| in.lawdocscomply.coop.DirectorDisqualificationRisk.v1 | coop | notifications, cmp | person_id, trigger, days_to_breach | P16 |
| in.lawdocscomply.coop.AuditReportReceived.v1 / RectificationReportFiled.v1 | coop | aud, cmp | fy, audit_class, paras count | P16 |
| in.lawdocscomply.coop.RegistrarReturnFiled.v1 | coop | cmp, ret | return code, fy, ack ref | P16 |
| in.lawdocscomply.coop.DepositEligibilityExceptionMirrored.v1 | coop | cmp (Critical), gov (agenda) | finbyx exception ref | P16 |

#### Events — stream S8 (P17–P19, App K–M)

Ecosystem-facing events use `in.infrabyx.[domain].[EventName].v1` exactly as Ecosystem Spec v1.1 Part 6; LDC-internal use `in.lawdocscomply.[module].[EventName].v1` (see master note M-S8-01).

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| in.infrabyx.grc.ObligationPublished.v1 | LDC (`cmp`/`cnt`) | Finbyx, Udofin, products in a GRC link | obligation_ref, change type, effective dates, applicability | P18 (relay) / P03–P05 (source) |
| in.infrabyx.grc.EvidenceSubmitted.v1 (consumed) | Finbyx, Udofin, any | LDC `cmp` | control, URIs, sha256, signer | P18 |
| in.infrabyx.grc.ControlTestResultPublished.v1 (consumed; produced for STORAGE_TARGET_HEALTH) | products / LDC `xpt` | LDC `cmp` / tenant compliance destination | result, population, masked sample | P18, P19 |
| in.infrabyx.grc.ComplianceIssueRaised.v1 | any ↔ LDC | LDC, RE | source, severity, owner, due | P18 |
| in.infrabyx.grc.PolicyAttested.v1 (consumed) | products | LDC `pol` | policy, version, user ref | P18 |
| in.infrabyx.grc.ReturnStatusUpdated.v1 (consumed) | Finbyx | LDC `ret` | return_code, period, status, ack | P18 |
| in.infrabyx.grc.SecurityIncidentNotified.v1 (consumed; copy to OH without PII) | service providers | LDC `dpc`; OH13 | detected_at, class, status | P18 |
| in.infrabyx.risk.KriBreached / LossEventRecorded / CapitalRatioComputed / LimitBreached / StressTestCompleted / RiskSnapshotPublished .v1 (consumed) | Finbyx, Udofin | LDC `erm`/`ral` | per Spec §6.22; hash chain | P18 |
| in.infrabyx.audit.ExternalAccessGranted / Used / Revoked .v1 | LDC (for LDC-hosted slices) | RE register, RE GRC, SIEM; OH counts | grant id, scope, times | P18 |
| in.infrabyx.portability.ExportRequested.v1 | LDC `xpt` | tenant compliance destination; OH4/OH13 (status) | job_id, scope, classes, destination type | P19 |
| in.infrabyx.portability.ExportCompleted.v1 (signed) | LDC `xpt` | same | archive_id, standard version, folder profile, counts, bytes, manifest hash | P19 |
| in.infrabyx.portability.StorageTargetConnected.v1 | LDC `xpt` | same | target_id, provider, region, classes, key mode, write-once | P19 |
| in.infrabyx.portability.BackupCompleted.v1 | LDC `xpt` | same | archive_id, type, bytes, manifest hash, target | P19 |
| in.infrabyx.portability.RestoreTested.v1 | LDC `xpt` | same | test_id, type, result, discrepancies | P19 |
| UsageRecorded (`usage_aggregate_v1`) | LDC `bil` | Ops Hub OH8 | aggregates only | P18/P17 |
| ModuleAttached / ModuleDetached | LDC `core` | Ops Hub | module id, state | P18 |
| ReleasePublished, ControlEvidenceCollected, ConnectorCertified, ReconciliationBreakRaised | LDC | OH / registry / counterpart | metadata | P18 |
| TenantProvisioned, PlanChanged, EntitlementChanged (consumed, signed) | Ops Hub | LDC `int`/`bil` | org, plan, entitlements | P18 |
| in.lawdocscomply.ai.VidhiRunRequested / VidhiPlanProposed / VidhiActionApprovalRequested / VidhiActionApproved / VidhiRunCompleted / VidhiOutputAccepted / VidhiOutputRejected / VidhiRunFailed .v1 | `ai` | `wf` (inbox), `core` (ledger), `bil` (usage) | run_id, skill, delegating user, state, credits | P17 |
| in.lawdocscomply.ai.VidhiScheduleCreated / VidhiScheduleFired / VidhiSchedulePaused .v1 | `ai` | `wf`, owner notifications | schedule_id, fire_time, status | P17 |
| in.lawdocscomply.ai.NotebookPublished / NotebookSourceSuperseded .v1 | `ai` | tenants with pack; notebook owners | notebook id, version | P17 |
| in.lawdocscomply.ai.TypeCopySaved / TranslationSaved .v1 | `ai`/`dms` | `dms`, record owners | document id, rendition version | P17 |
| in.lawdocscomply.ai.AiBudgetThresholdReached / AiKillSwitchChanged / AiModelDefaultChanged .v1 | `ai` | admins, platform | tenant, threshold / skill, provider | P17 |
| in.lawdocscomply.int.ConnectorInstanceStateChanged / WebhookDeliveryFailed / DlqReplayRequested / DlqReplayApproved / AgentRegistered / AgentHeartbeatMissed / CalendarSyncBroken / OnboardingLookupCompleted / ComplianceModeSwitchStateChanged / ApiClientApproved / ApiClientRevoked / SecretRotated .v1 | `int` | admins, monitor, ledger | ids, states | P18 |
| in.lawdocscomply.xpt.ExportJobStateChanged / ExportReconciliationFailed / IntakeCommitted / IntakeRolledBack / ExitStateChanged / DeletionCertificateIssued / FolderProfileReleased / StorageTargetDegraded .v1 | `xpt` | admins, ledger, P24 evidence | ids, states, counts | P19 |

#### Events — stream S9 (P20–P22, App N, O, X)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| bil.TenantSelfServeCreated.v1 (new; Appendix X §X.3) | LDC bil | OH3, OH4, OH8 | tenantid, org_id, entity_family, regulators, origin, trial_plan, trial_end_at, first_admin_work_email, clickwrap_refs | P20 |
| bil.TrialStarted.v1 | bil | wf (notifications), rpt | tenantid, plan, end_at | P20 |
| bil.TrialExtended.v1 (→ OH) | bil | OH4, OH5, OH8, wf | tenantid, period_no, new_end_at, reason_code, granted_by, approved_by | P20 |
| bil.TrialExpired.v1 (→ OH) | bil | OH4, OH5, wf, xpt | tenantid, expired_at, retention_until | P20 |
| bil.TrialConverted.v1 (→ OH) | bil | OH4, OH5 | tenantid, subscription_ref, package | P20 |
| bil.ConfigurationSaved.v1 | bil | rpt (aggregate) | token_hash, segment (no PII) | P20 |
| bil.QuoteRequested.v1 | bil | OH8 (via API), wf | tenantid/org, quote_ref | P20 |
| bil.TenantPurchaseApprovalDecided.v1 | bil | wf, audit | quote_ref, approver, decision | P20 |
| ModuleAttached / ModuleDetached (Ecosystem) | bil | OH8 | tenantid, module, effective_at | P20 |
| UsageRecorded (Ecosystem) | bil | OH8 | usage_aggregate_v1 | P20 |
| bil.EntitlementApplied.v1 | bil | all modules (cache invalidation) | tenantid, entitlement_id, version | P20 |
| ReconciliationBreakRaised (Ecosystem) | bil | OH8, plt_finance | tenantid, kind, details | P20 |
| bil.StreamSwitchChanged.v1 | bil | web, bil caches, P22 | stream_code, scope, enabled | P20 |
| bil.PresentationVersionPublished.v1 | bil | web | version, catalogue_version_ref, effective_from | P20 |
| bil.CommercialOverrideApplied.v1 | bil | audit, tenant notice, OH8 | tenantid, type, reason_code, oh_ref | P20 |
| bil.SavingsSnapshotPublished.v1 | bil | rpt, gov (board pack) | tenantid, period, hash | P20 |
| bil.AddonRequested.v1 | bil | wf (admins) | tenantid, requester, component | P20 |
| bil.CancellationRequested.v1 / CancellationWithdrawn.v1 | bil | OH8, OH5, xpt | tenantid, effective_at | P20 |
| Consumed: PlanChanged, EntitlementChanged, InvoiceIssued, SubscriptionPaymentReceived, SubscriptionPaymentFailed, SubscriptionCancelled (Ecosystem) | OH8 | bil | per Ecosystem §6.27 | P20 |
| Consumed (new): CatalogueVersionPublished, CatalogueChangeRequestUpdated | OH8 | bil | version / request_id, state | P20 |
| mkp.ServiceRequested.v1 | mkp | wf, OH3 (if non-subscriber with consent) | engagement_id, offering_code, buyer_org | P21 |
| mkp.ProposalSent.v1 | mkp | wf | engagement_id, quote_ref, valid_until | P21 |
| mkp.EngagementContracted.v1 | mkp | sdc, OH8, dms | engagement_id, model, letter_hash | P21 |
| mkp.MilestoneDelivered.v1 / MilestoneAccepted.v1 | mkp | wf, OH8 (milestone invoice) | engagement_id, seq, deemed | P21 |
| mkp.EngagementClosed.v1 / EngagementCancelled.v1 | mkp | xpt, rpt | engagement_id, outcome | P21 |
| mkp.RetainerActivated.v1 / RetainerEnded.v1 | mkp | sdc (grants), OH5 | retainer_id, plan_code, dates | P21 |
| mkp.RetainerSLABreached.v1 | mkp | sdc, wf | retainer_id, metric, due_at, met_at | P21 |
| mkp.ServiceCreditIssued.v1 (new; → OH8) | mkp | OH8 | engagement_id, period, metric, credit_minor | P21 |
| mkp.MarketplaceDisputeRaised.v1 / Resolved.v1 | mkp | OH6 (M1), wf | engagement_id, category, outcome | P21 |
| mkp.ProviderSuspended.v1 | mkp (from OH9) | web, mkp | provider_id, reason | P21 |
| mkp.OfferingPublished.v1 | mkp | web (search index) | offering_code, version | P21 |
| mkp.AcademyCatalogueSynced.v1 | mkp | web | feed_hash, count | P21 |
| mkp.TrainingCertificateImported.v1 | mkp | hr, cmp (evidence) | tenantid, employee_ref, course_id | P21 |
| Consumed: ProfessionalEmpanelled, ProfessionalSuspended (OH9) | OH9 | mkp | per Ecosystem §6.29 | P21 |
| sdc.DeliveryGrantProposed.v1 / Activated / Renewed / Suspended / Revoked | iam/sdc | wf (tenant admin), audit, tpr (outsourcing register) | grant_id, staff_id, scope, valid_to | P22 |
| sdc.DeliverySessionStarted.v1 / Ended.v1 | sdc | audit | session_id, grant_id | P22 |
| sdc.CredentialEntryCreated.v1 / CredentialGrantChanged.v1 | sdc | audit | entry_id, type (no secret) | P22 |
| sdc.CredentialRevealed.v1 (tenant-only, sealed) | sdc | audit, tenant admin notification, security monitor | entry_id, grantee, purpose_ref, ts | P22 |
| sdc.CredentialRotationPrompted.v1 / CredentialRotated.v1 | sdc | wf | entry_id | P22 |
| sdc.DeliverableReleased.v1 / Accepted.v1 / Returned.v1 | sdc | dms, wf, mkp | deliverable_id, linked_record_ref | P22 |
| sdc.MasterDataChangeRequested.v1 / Applied.v1 | sdc / console | core (correction entry), tenant notice | tenantid, field, correction_id | P22 |
| sdc.ClientHealthSignal.v1 (new; → OH5) | sdc | OH5, OH2 | adoption and delivery aggregates only | P22 |
| sdc.TimesheetAggregated.v1 (new; → OH4/OH11) | sdc | OH4, OH11 | staff_id, date, client, category, hours | P22 |
| sdc.DeliveryMetricsMonthly.v1 (new; → OH10/OH11) | sdc | OH10, OH11 | staff_id, month, output metrics | P22 |
| Consumed: EmployeeOnboarded/Offboarded (oh scope), SupportTicketOpened/Resolved, InvoiceIssued, PlanChanged | OH | sdc | — | P22 |

#### Events — stream S10 (P23, App P, R)

| Event type | Producer | Consumers | Key payload | Phase |
|---|---|---|---|---|
| `in.lawdocscomply.web.HealthCheckStarted.v1` | web | analytics (internal) | session_id, family, type, utm | P23 |
| `in.lawdocscomply.web.HealthCheckCompleted.v1` | web | OH CRM (counts/band), rpt | session_id, report_id, family, type, size_band, band, confidence, bank_version, model_version | P23 |
| `in.lawdocscomply.web.HealthCheckReportShared.v1` | web | analytics | report_id, link_id (no viewer identity) | P23 |
| `in.lawdocscomply.web.LeadCaptured.v1` | web | Infrabyx Operations Hub CRM (`crm.request:write`) | lead_id, contact (enc), consent_artefact_ids, family, band, top_gap_segments, utm, partner_code, report_link (only if consent d) | P23 |
| `in.lawdocscomply.web.MarketingConsentChanged.v1` | web / OH | OH / web, iam consent ledger | lead_id, channel, granted/withdrawn, notice_version | P23 |
| `in.lawdocscomply.web.LeadErasureRequested.v1` | web | OH CRM | lead_id, requested_at | P23 |
| `in.lawdocscomply.web.TrialStartedFromHealthCheck.v1` | web | iam (P01), bil (P20), OH | report_id, tenant_id, prefill_hash | P23 |
| `in.lawdocscomply.web.WebinarRegistered.v1` | web | OH | lead_id, event_id, paid flag | P23 |
| `in.lawdocscomply.web.PagePublished.v1` / `PageUnpublished.v1` | web | CDN revalidation, IndexNow job | page_id, version_id, slug, locale | P23 |
| `in.lawdocscomply.web.ClaimApproved.v1` / `ClaimExpired.v1` | web | CMS, page re-render job, owner notifications | claim_id, bound_page_ids | P23 |
| `in.lawdocscomply.web.ExperimentConcluded.v1` | web | OH | experiment_id, winner, metrics | P23 |
| `in.lawdocscomply.hlp.GlossaryTermPublished.v1` / `GlossaryTermReviewDue.v1` | hlp | web (glossary pages), ui build check | key, version, clause_id | P23 |
| `in.lawdocscomply.hlp.TutorialPublished.v1` / `TutorialStale.v1` | hlp | help panel, release notes, OH (social) | tutorial_id, product_version, reason | P23 |
| `in.lawdocscomply.hlp.SocialAssetReady.v1` | hlp | OH social calendar | asset_ids, format (9:16/1:1/16:9), title, description, alt_text, transcript | P23 |
| `in.lawdocscomply.hlp.AccessibilityIssueReported.v1` / `AccessibilityIssueBreached.v1` | hlp | support desk, accessibility nodal officer, eng | issue_id, criterion, severity, due_at | P23 |
| `in.lawdocscomply.hlp.AcrPublished.v1` | hlp | web (trust/accessibility pages) | acr_version, release, conformance summary | P23 |
| (consumed) `cnt.InstrumentVersionPublished`, `chg.UpdatePublished`, `bil.CatalogueVersionPublished`, `mkp.ServicePublished`, `core.ReleaseDeployed` | other modules | web, hlp | — | P23 |


### B.9.3 Module error codes

Additional ranges reserved: `LDC-WEB-001–015`, `LDC-HLP-001–006` (P23), `LDC-TPL-001–040` (Appendix E), `LDC-CORE-005` = maker and checker are the same user (used by P04 and P10–P14).

#### Error codes — stream S11 (P00, P01, P24, App B, Q)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-CORE-001 | Immutable ledger modification attempted | History can't be changed. Use a correction entry. | P00 |
| LDC-CORE-002 | Version conflict | Someone else changed this record. Reload. | P00 |
| LDC-CORE-003 | Missing tenant context | Select a workspace to continue. | P00 |
| LDC-CORE-004 | Correction justification/document missing | Add a justification (≥ 50 chars) and supporting document. | P00 |
| LDC-CORE-005 | Maker = checker | Another person must approve. | P00 |
| LDC-CORE-006 | Correction target changed | Review and resubmit. | P00 |
| LDC-CORE-007 | Target under legal hold | Under legal hold <ref>. | P00 |
| LDC-CORE-008 | Tenant acknowledgement pending | Waiting for client acknowledgement. | P00 |
| LDC-CORE-009 | Effective date not allowed | Date not allowed for this record type. | P00 |
| LDC-CORE-010 | Idempotency key reuse | Request already sent with different details. | P00 |
| LDC-CORE-011 | Request in progress | Still processing earlier request. | P00 |
| LDC-CORE-012 | Data class not permitted for destination | Can't be sent to that destination. | P00 |
| LDC-CORE-013 | Residency blocked | Storage location not allowed for this data. | P00 |
| LDC-CORE-014 | Live provider from non-prod | (internal) | P00 |
| LDC-CORE-015 | Governed changes frozen | Changes paused during security check. | P00 |
| LDC-CORE-016 | Overlapping bitemporal version | Another version covers these dates. | P00 |
| LDC-CORE-017 | Migration promotion blocked | Reconciliation found differences. | P00 |
| LDC-CORE-018 | Export mapping missing | (internal) | P00 |
| LDC-DMS-001..004 | File type / malware / checksum / size | See Appendix B | P00 |
| LDC-IAM-001, 003, 010, 020, 021, 030, 031, 040, 041, 042, 050, 060 | Context, membership, policy, SoD, delivery, supervisor, break-glass, trial | See Appendix B | P01 |
| LDC-AUTH-010..014 | Step-up, session expiry, MFA enrolment, OTP rate limit, SSO enforced | See Appendix B | P01 |
| LDC-ENG-001..004 | Unapproved deployment, freeze, destructive migration, golden mismatch | (staff) | P24 |

#### Error codes — stream S12 (P02, App A, C, D, U)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-CFG-001 | Type validation failed | "This value must be a {type}." | P02 |
| LDC-CFG-002 | Out of bounds | "Allowed range is {min}–{max}." | P02 |
| LDC-CFG-003 | Child-direction violation | "You can only make this {stricter/earlier/narrower} than {parent value}." | P02 |
| LDC-CFG-004 | Outside protective bound | "This would be less protective than the legal minimum ({floor}). Set a stricter value." | P02 |
| LDC-CFG-005 | Locked by parent | "Locked by {scope}. Use Request change." | P02 |
| LDC-CFG-006 | Contrast check failed | "Colour contrast {ratio}:1 is below 4.5:1 for text." | P02 |
| LDC-CFG-010 | Locked setting | "This setting is locked for safety and compliance and cannot be changed." | P02 |
| LDC-CFG-011 | Unregistered key (internal) | "Configuration error. Reference {traceId}." | P02 |
| LDC-CFG-020 | Maker cannot approve | "You created this request, so another person must approve it." | P02 |
| LDC-CFG-021 | Citation required | "Add the regulation or paragraph this change is based on." | P02 |
| LDC-CFG-022 | Summary required | "Add a short 'what changed' summary." | P02 |
| LDC-CFG-023 | Lead time not met | "Legal changes need 24 hours before they take effect, unless marked urgent with approval." | P02 |
| LDC-CFG-024 | Preview stale | "Run preview again; the last one is older than 24 hours." | P02 |
| LDC-CFG-030 | Rule conflict | "Two rules give different results; a reviewer has been asked to resolve it." | P02 |
| LDC-CFG-080 | Golden suite failing | "Test cases do not match expected results." | P02 |
| LDC-CFG-032 | Permissive rule requires verified source | "This rule enables an action and needs a verified primary source." | P02 |
| LDC-CFG-033 | Flag review open | "This feature can be switched off but not on while its legal review is open." | P02 |
| LDC-CFG-040 | Workflow invalid | "The workflow cannot be published: {reasons}." | P02 |
| LDC-CFG-041 | High-risk items need a checker | "High-risk items must have a checker step." | P02 |
| LDC-CFG-042 | AI step cannot approve | "Vidhi can draft but cannot approve or publish." | P02 |
| LDC-CFG-043 | Retainer checker must be tenant user | "In retainer mode the checker must be an employee of the client." | P02 |
| LDC-CFG-044 | Statutory clock cannot pause | "Legal deadlines keep running while you wait on others." | P02 |
| LDC-CFG-050 | Canonical transition not allowed | "This status change is not allowed for this item type." | P02 |
| LDC-CFG-051 | Department merge has blocking items | "Some items cannot be moved: {count}. Review the list." | P02 |
| LDC-CFG-060 | Correction self-approval | "Another authorised person must approve this correction." | P02 |
| LDC-CFG-061 | Correction target on legal hold | "This record is on legal hold. Ask the hold owner." | P02 |
| LDC-CFG-062 | Not correctable | "Ledger events and sealed content cannot be corrected." | P02 |
| LDC-CFG-070 | Import value rejected | "Row {n}: {key} rejected — {reason}." | P02 |
| LDC-CFG-071 | Bundle signature invalid | "This configuration file is not signed by LawDocsComply or was altered." | P02 |
| LDC-WF-INBOX-001 | Inbox action stale | "This changed since you opened it. Reloaded." | P04 |
| LDC-WF-INBOX-002 | Snooze limit / not allowed | "Urgent items cannot be snoozed." | P04 |
| LDC-WF-INBOX-003 | Delegation not allowed | "That colleague cannot act on this item." | P04 |
| LDC-IAM-SOD-001 | SoD conflict blocked | "This role combination is not allowed ({rule})." | P01 |
| LDC-IAM-SOD-002 | SoD conflict warning | "This combination needs a reason and will be reviewed." | P01 |

#### Error codes — stream S1 (P03–P05, App F)

*Lead note (review R1, 25 Oct 2026): the P03 importer-workflow codes are numbered LDC-TPL-101 onward and the P05 AI Question Authoring Studio codes LDC-CHG-101 onward, so that they do not collide with the content-validation codes LDC-TPL-001–040 of Appendix E (authoritative) or the Vidhi codes LDC-AI-001 onward of P17.*

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-TPL-101 | Not a valid .xlsx / macros or external links present | "This file can't be imported: save it as .xlsx without macros or external links." | P03 |
| LDC-TPL-102 | Row 1 or row 2 header mismatch | "Header in cell {cell} must read '{expected}'. Download the template and copy your rows into it." | P03 |
| LDC-TPL-103 | Template not identified | "We couldn't match this file to a template. Choose the template family." | P03 |
| LDC-TPL-104 | User/system columns filled in content mode | "Columns A, E, I, J, T and W–AD must be blank when loading questions." | P03 |
| LDC-TPL-105 | Required column empty | "Row {n}: {column} is required." | P03 |
| LDC-TPL-106 | Value not in list | "Row {n}: '{value}' is not in the list for {column}. Did you mean '{suggestion}'?" | P03 |
| LDC-TPL-107 | Unknown CompID | "Row {n}: CompID {id} doesn't belong to this instrument." | P03 |
| LDC-TPL-108 | Clause reference unresolved | "Row {n}: we can't find '{ref}' in the instrument." | P03 |
| LDC-TPL-109 | Personal data in content | "Row {n} seems to contain personal data ({type}). Remove it." | P03 |
| LDC-TPL-110 | Workspace action not permitted | "Row {n}: you can't {action} this item." | P03/P04 |
| LDC-TPL-111 | Stale workspace export | "This export is older than {days} days. Confirm to merge with current data." | P03 |
| LDC-CNT-001 | Release has uncited rows | "Release blocked: {n} rows lack a resolvable citation." | P03 |
| LDC-CNT-002 | Overlay field locked | "This field can't be changed for your organisation." | P03 |
| LDC-CNT-003 | Removal needs second approver | "Removing an applicable instrument needs approval by {role}." | P03 |
| LDC-CNT-004 | Approver equals maker | "You can't approve changes you made." | P03 |
| LDC-CMP-001 | Instance closed | "This item is closed. Use a correction request." | P04 |
| LDC-CMP-002 | Missing maker status | "Select your status before submitting." | P04 |
| LDC-CMP-003 | Maker attempting review | "You can't review your own submission." | P04 |
| LDC-CMP-004 | Date of compliance in future | "Date of compliance can't be in the future." | P04 |
| LDC-CMP-010 | Evidence floor not met | "Upload evidence for: {requirements}." | P04 |
| LDC-CMP-011 | N-A claim without reason | "Explain why this does not apply." | P04 |
| LDC-CMP-012 | Remediation plan missing | "Add a remediation plan for non-compliance." | P04 |
| LDC-CMP-013 | Bulk approval not allowed for this item type | "Bulk approval is available only for item types flagged as bulk-approvable. Use Review next." (NN-46) | P04 |
| LDC-CMP-020 | Event trigger not permitted | "You can't record this event type." | P04 |
| LDC-WF-001 | Assignment outside hierarchy | "You can assign only to people in your team; send a request instead." | P04 |
| LDC-WF-002 | Calendar provider not allowed | "Your organisation hasn't enabled {provider}." | P04 |
| LDC-WF-003 | Calendar token expired | "Reconnect your calendar." | P04 |
| LDC-WF-004 | Notification floor | "This alert is mandatory for your role." | P04 |
| LDC-WF-005 | Schedule limit reached | "You have reached {n} active schedules." | P04 |
| LDC-CHG-001 | Source fetch failed | (internal) | P05 |
| LDC-CHG-002 | Parser broken | (internal) | P05 |
| LDC-CHG-003 | Publication blocked: unreviewed | "A reviewer must approve before publishing." | P05 |
| LDC-CHG-004 | Broadcast needs second approver | "Messages to all tenants need a second approver." | P05 |
| LDC-CHG-101 | Studio quota exceeded | "Your plan's AI page quota is used up for this month." | P05 |
| LDC-CHG-102 | Instrument too large | "This document exceeds {pages} pages; select chapters." | P05 |
| LDC-CHG-103 | Low extraction confidence | "Please confirm the document structure before generating." | P05 |
| LDC-CHG-104 | Run approver equals runner/editor | "Another person must approve this draft." | P05 |

#### Error codes — stream S2 (App E, templates)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-TPL-001 | [E] Not a macro-free, unencrypted .xlsx | Upload an .xlsx file saved from the LawDocsComply template (no macros, no password). | P03 |
| LDC-TPL-002 | [E] Sheet missing, renamed or reordered | The workbook must contain Sheet1, Rough and _Template_Info in that order. Download the template again. | P03 |
| LDC-TPL-003 | [E] Row-1 group headers or merged ranges changed | Row 1 of Sheet1 was changed. Rows 1–2 cannot be edited. | P03 |
| LDC-TPL-004 | [E] Row-2 header hash mismatch | The column headers in row 2 were changed (column {col}: expected '{exp}'). Restore them from the template. | P03 |
| LDC-TPL-005 | [E] Columns inserted, deleted or hidden, or data beyond AD | Columns must run from A to AD exactly, with none hidden. | P03 |
| LDC-TPL-006 | [E/I] `_Template_Info` missing, or template code unknown (E); sheet edited but code and hash valid (I) | This file does not carry a LawDocsComply template code. Use a template from Content Studio → Templates. | P03 |
| LDC-TPL-007 | [W/E] Template version deprecated (W) or retired (E) | Template {code} is {status}. Download {current} and copy your rows into it. | P03 |
| LDC-TPL-008 | [E] Template family does not match the chosen instrument's family | This is a {family} template but the instrument belongs to {instFamily}. | P03 |
| LDC-TPL-009 | [E] More than 2,000 data rows, or file over 25 MB | Split the instrument into Part A and Part B files of up to 2,000 rows. | P03 |
| LDC-TPL-010 | [E] Active content, external links, embedded objects or malware | The file contains macros, links or embedded objects and was rejected for security. | P03 |
| LDC-TPL-011 | [W] Formula or formula-like value in a content cell | Cell {cell} contained a formula; it was stored as plain text. | P03 |
| LDC-TPL-012 | [E] Required content cell empty | Row {row}: column {col} ({header}) is required. | P03 |
| LDC-TPL-013 | [W/I] System or user column not blank | Row {row}: column {col} is filled by the software; the value was ignored. | P03 |
| LDC-TPL-014 | [W] Serial number gap, duplicate or non-integer | Serial numbers are not 1..n; renumber automatically? | P03 |
| LDC-TPL-015 | [E] Value not in the family vocabulary (C, D, H, M, O, R) | Row {row}: '{value}' is not a {list} value for {family}. Did you mean '{suggestion}'? | P03 |
| LDC-TPL-016 | [I] Non-canonical delimiter normalised | Row {row}: values in column {col} were separated with '; '. | P03 |
| LDC-TPL-017 | [E] Column P does not start with a Filing-list token | Row {row}: column P must start with a filing destination from the list (or 'Not Required'). | P03 |
| LDC-TPL-018 | [W] `Due:` rule not machine-readable | Row {row}: the due-date rule will need to be set in Content Studio before publishing. | P03 |
| LDC-TPL-019 | [W] Frequency (H) inconsistent with the Due rule | Row {row}: frequency '{H}' does not match the due rule '{rule}'. | P03 |
| LDC-TPL-020 | [W] Citation (K) could not be parsed, or does not exist in the clause tree | Row {row}: the clause reference could not be matched to the instrument text. | P03 |
| LDC-TPL-021 | [W] Probable duplicate obligation | Rows {a} and {b} look like the same obligation. | P03 |
| LDC-TPL-022 | [E] Unknown CompID on re-upload | Row {row}: CompID {id} does not exist. Clear column E for new rows. | P03 |
| LDC-TPL-023 | [E] Exported CompID missing (row deleted) | CompID {id} is missing. Do not delete rows; mark omitted provisions with [RETIRED] in column F. | P03 |
| LDC-TPL-024 | [E] CompID belongs to another instrument or another tenant | Row {row}: CompID {id} belongs to a different instrument or organisation. | P03 |
| LDC-TPL-025 | [E] `[RETIRED]` row without the omitting reference in S, or on a first upload | Row {row}: give the omitting notification and date in column S. | P03 |
| LDC-TPL-026 | [W] `[VERIFY]` marker present | Row {row} contains [VERIFY]; it cannot be published until verified or waived. | P03 |
| LDC-TPL-027 | [E] Text longer than the column limit | Row {row}: column {col} exceeds {n} characters. | P03 |
| LDC-TPL-028 | [W] Non-official URL in N | Row {row}: {domain} is not an official source; keep it only as secondary reference. | P03 |
| LDC-TPL-029 | [W] Generic evidence text in U | Row {row}: name the specific document that proves compliance. | P03 |
| LDC-TPL-030 | [I] More than 70% of rows rated High | {pct}% of rows are High risk; check the calibration rule. | P03 |
| LDC-TPL-031 | [I] Row count unusual compared with the clause tree | {n} operative clauses have no row. | P03 |
| LDC-TPL-032 | [I] Control or zero-width characters removed | — | P03 |
| LDC-TPL-033 | [E] No data rows | The sheet has no rows from row 3. | P03 |
| LDC-TPL-034 | [E] Tenant upload tries to change a base obligation | This question belongs to the LawDocsComply library. Your change will be saved as your company's version." (offers overlay) | P03 |
| LDC-TPL-035 | [E] Tenant vocabulary value not registered | '{value}' is not one of your company's {list} values. Add it in Settings → Compliance vocabulary. | P03 |
| LDC-TPL-036 | [E] A newer version of the instrument is already published | A newer version ({v}) is published. Export it and edit that instead. | P03 |
| LDC-TPL-037 | [E] Another import for the same instrument version is open | An import is already in review for this instrument. | P03 |
| LDC-TPL-038 | [E] Corrupt or unreadable file | The file could not be read. | P03 |
| LDC-TPL-039 | [W] Hidden rows or active filters in Sheet1 | Hidden or filtered rows were found; all rows were imported. | P03 |
| LDC-TPL-040 | [E] Merged cells in the data area | Unmerge cells in rows 3 onwards. | P03 |

#### Error codes — stream S3 (P06–P07)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-GOV-001 | Blueprint evaluation failed: missing entity threshold input | "We need the entity's latest paid-up capital, turnover and borrowings to work out its governance requirements." | P06 |
| LDC-GOV-005 | Composition rule violated on save | "This change leaves the {committee} without the required {rule}. Save anyway as a recorded gap, or pick another member." | P06 |
| LDC-GOV-010 | Notice shorter than minimum without urgency ground | "Board meetings need 7 days' notice. Add the reason for urgency to use shorter notice." | P06 |
| LDC-GOV-012 | Matter cannot be passed by circular resolution | "This matter must be decided at a meeting ({citation})." | P06 |
| LDC-GOV-015 | Quorum not present | "Quorum is not present for this item. Adjourn or wait for members to join." | P06 |
| LDC-GOV-020 | Minutes circulation blocked pending shorter-notice ratification | "Minutes can be circulated after an independent director ratifies the decisions taken at shorter notice." | P06 |
| LDC-GOV-031 | Attempt to modify sealed minutes | "Signed minutes cannot be changed. Record a correction in the minutes of the next meeting." | P06 |
| LDC-GOV-035 | Register free-edit attempted | "Registers are updated from events. Propose an entry or a correction for checker approval." | P06 |
| LDC-GOV-040 | Filing cannot close without SRN/challan/acknowledgement | "Add the SRN, challan and acknowledgement to close this filing." | P06 |
| LDC-GOV-045 | Appointment effective without regulator approval reference | "This appointment needs RBI's prior approval. Record the approval reference first." | P06 |
| LDC-GOV-050 | SDD update/delete attempted | "Structured Digital Database entries cannot be edited. Add a new entry to correct." | P06 |
| LDC-GOV-055 | Disclosure recorded after clock without delay reason | "Disclosure was made after the deadline. Record the reason for delay." | P06 |
| LDC-GOV-060 | Interested director access restricted | "You have disclosed an interest in this item; papers are restricted by the company's setting." | P06 |
| LDC-POL-003 | Redline citation not found | "One or more citations are not in the content library. Review highlighted comments." | P07 |
| LDC-POL-007 | Reviewer equals maker | "You drafted this version and cannot review it." | P07 |
| LDC-POL-010 | Route missing required approver body | "This policy must be approved by {body} under {citation}." | P07 |
| LDC-POL-014 | Effective without signed copy | "Upload the signed or certified copy of the approved policy to make it effective." | P07 |
| LDC-POL-018 | Locked version edited | "This version is submitted for approval and locked. Create a new version to make changes." | P07 |
| LDC-DMS-002 | Malware detected — file quarantined (core code, §B.8) | "This file was quarantined by the security scan and cannot be opened." | P00/P07 |
| LDC-DMS-006 | Checked out by another user | "{name} is editing this document until {time}." | P07 |
| LDC-DMS-011 | Intake conflict requires choice | "A different file already exists at this place. Keep both as a new version or skip." | P07 |
| LDC-DMS-015 | eSign blocked for excluded instrument | "Documents of this type cannot be signed electronically under the IT Act. Use the physical execution checklist." | P07 |
| LDC-DMS-018 | BOARD_CONFIDENTIAL share needs CS approval | "Board-confidential documents can be shared only with the Company Secretary's approval." | P07 |
| LDC-DMS-021 | Sealed class not shareable externally | "This document is protected and cannot be shared from the document library." | P07 |
| LDC-DMS-025 | Disposal blocked by legal hold or retention floor | "This document is under legal hold or within its legal retention period." | P07 |
| LDC-DMS-030 | AI processing not permitted by tenant setting | "AI processing is turned off for this feature in your organisation's settings." | P07 |
| LDC-DMS-033 | Share expired or revoked | "This link has expired or was withdrawn by the sender." | P07 |

#### Error codes — stream S4 (P08–P09, App H)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-ERM-001 | Taxonomy L1 edit attempted | Level-1 categories are fixed for this pack version. Rename or add at level 2 or 3. | P08 |
| LDC-ERM-002 | Node with history deleted | This category has history; retire it with an effective date instead. | P08 |
| LDC-ERM-010 | Scale change without mapping | Provide a mapping from the old scale to the new one before submitting. | P08 |
| LDC-ERM-014 | Residual lower than inherent without tested control | Link at least one tested control before reducing the residual rating. | P08 |
| LDC-ERM-015 | Override without rationale | Add a rationale for the judgement override. | P08 |
| LDC-ERM-021 | RAS limit looser than regulatory floor | The limit is looser than the regulatory minimum ({value} vs {floor}) — {citation}. | P08 |
| LDC-ERM-022 | Cascade children exceed parent | Child limits add up to more than the parent limit. | P08 |
| LDC-ERM-023 | RAS effective before approval | The effective date cannot be earlier than the Board approval date (use a Correction Entry if needed). | P08 |
| LDC-ERM-025 | Self-approval | You cannot approve your own submission. | P08 |
| LDC-ERM-028 | Effective rating without evidence | Attach evidence or a test result to rate the control "Effective". | P08 |
| LDC-ERM-031 | Regulatory limit acceptance | Regulatory limit breaches cannot be accepted; they must be remediated and reported. | P08 |
| LDC-ERM-032 | Acceptance beyond authority | Your role cannot accept a risk at this level. | P08 |
| LDC-ERM-033 | Acceptance beyond maximum duration | Acceptance period exceeds the maximum allowed ({max} months). | P08 |
| LDC-ERM-035 | Duplicate open episode | An open breach episode already exists for this KRI. | P08 |
| LDC-ERM-041 | Loss event missing a mandatory date | Occurrence, discovery and accounting dates are required to validate an accounted loss. | P08 |
| LDC-ERM-042 | Loss version edit | Validated loss events are versioned; add a new version instead of editing. | P08 |
| LDC-ERM-051 | Inbound event signature/hash-chain failure | Event rejected: signature or hash chain did not verify. Integration team notified. | P08 |
| LDC-ERM-052 | Inbound event contains PII | Event rejected: personal data is not allowed in risk feeds. | P08 |
| LDC-ERM-061 | Pack frozen | This pack is frozen. Create an addendum to change it. | P08 |
| LDC-ERM-062 | Uncertified regulatory metric in pack | Certify the value or mark it "indicative" with a reason. | P08 |
| LDC-RAL-001 | Template header mismatch | The file does not match template {code} v{version}. Download the current template. | P09 |
| LDC-RAL-002 | PII detected in loan-level upload | Row {n}: personal data pattern detected. Use pseudonymised IDs only. | P09 |
| LDC-RAL-010 | Snapshot not frozen | Freeze the data snapshot before certifying a regulatory run. | P09 |
| LDC-RAL-012 | Reconciliation break above tolerance | Loan book differs from the trial balance by {amount} (tolerance {tol}). | P09 |
| LDC-RAL-013 | Unclassified exposures above limit | {pct}% of exposure has no risk-weight class (maximum 0.1%). | P09 |
| LDC-RAL-014 | Period not closed | The trial balance for this period is not locked in Accounting. | P09 |
| LDC-RAL-020 | Regulatory formula edit | Regulatory formulas and thresholds come from rule packs and cannot be edited. | P09 |
| LDC-RAL-021 | Metric change self-validated | A different data steward must validate this change. | P09 |
| LDC-RAL-022 | Parallel run incomplete | Complete at least one parallel period-end before approving. | P09 |
| LDC-RAL-025 | Behavioural assumptions not approved | Use an ALCO-approved assumption set for regulatory runs. | P09 |
| LDC-RAL-031 | ICAAP transition without frozen data | Freeze the ICAAP data snapshot before CRO review. | P09 |
| LDC-RAL-032 | Two ICAAP hosts | ICAAP for this cycle is hosted in {host}. | P09 |
| LDC-RAL-035 | Approved scenario edit | Approved scenarios cannot be edited; a new version has been created. | P09 |
| LDC-RAL-036 | Reverse stress did not converge | No breaking point found within bounds; widen bounds or change factor. | P09 |
| LDC-RAL-041 | PCA state change without RBI letter | Record RBI's letter to change PCA placement status. | P09 |
| LDC-RAL-042 | PCA restriction gate | This action is restricted under PCA ({threshold}) — {citation}. | P09 |
| LDC-RAL-050 | Finbyx-sourced value recompute attempted | This value is certified in Finbyx; LDC does not recompute it. | P09 |

#### Error codes — stream S5 (P10–P11, App I–J)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-AUD-409 | Invalid state transition | "This action is not available in the current state." | P10 |
| LDC-AUD-012 | Locked RBIA parameter missing basis | "Parameter {n} (IAF para 31) needs a value and basis before approval." | P10 |
| LDC-AUD-015 | Unit past policy maximum removed from plan | "This unit has passed its maximum audit interval; an ACB minute reference is required." | P10 |
| LDC-AUD-018 | Independence declaration missing | "Fieldwork cannot start until every team member has declared independence." | P10 |
| LDC-AUD-021 | Report owner not tenant IA staff (IAF para 39) | "Only the entity's internal-audit staff can own or sign this report." | P10 |
| LDC-AUD-024 | HIA business target/reporting line blocked (IAF para 43) | "The Head of Internal Audit cannot hold business targets or report to a business vertical." | P10 |
| LDC-AUD-027 | Workpaper sign-off with open review notes | "Clear the open review notes before signing off." | P10 |
| LDC-AUD-030 | Edit after file lock | "This file is locked; add an addendum instead." | P10 |
| LDC-AUD-031 | Retester not independent | "The retester must not have remediated or advised on this finding." | P10 |
| LDC-AUD-033 | Back-dated closure | "Closure date is the retest date and cannot be back-dated." | P10 |
| LDC-AUD-035 | Risk acceptance of regulatory breach without CCO | "CCO concurrence is required to accept a regulatory-breach finding." | P10 |
| LDC-AUD-037 | Locked report section removal | "This section is required by {citation} and cannot be removed." | P10 |
| LDC-AUD-040 | Mirrored object owned by another system | "Owned by {system} — make changes there." | P10 |
| LDC-AUD-042 | Sample re-run hash mismatch | "The population has changed since the sample was drawn; freeze a new population." | P10 |
| LDC-AUD-045 | Auditor ineligible (SA/Reg 24A/CB-CA) | "This auditor is not eligible: {citation}." | P10 |
| LDC-AUD-048 | Evidence integrity failure | "File verification failed for {n} items; integrity alert raised." | P10 |
| LDC-AUD-050 | External room write attempt | "External access is read-only." | P10 |
| LDC-AUD-052 | AI action prohibited | "Vidhi can draft but cannot {action}." | P10 |
| LDC-RET-409 | Invalid run transition | "This action is not available in the current state." | P11 |
| LDC-RET-GEN-001 | Generate disabled for mirrored return | "Owned by Finbyx — package available by reference." | P11 |
| LDC-RET-UNV-002 | Pack row ACTIVE_UNVERIFIED | "This return definition is awaiting verification and cannot generate a filing yet." | P11 |
| LDC-RET-TPL-003 | Template hash mismatch | "The uploaded template differs from the registered version; a template-change review has been opened." | P11 |
| LDC-RET-MAP-004 | Unmapped ledger with balance | "Ledger {name} (₹{balance}) is not mapped." | P11 |
| LDC-RET-VAL-005 | Validation ERROR | "{rule_id}: {message} ({citation})." | P11 |
| LDC-RET-REC-006 | Reconciliation break beyond tolerance | "Variance ₹{x} on {element} exceeds tolerance; explain it to proceed." | P11 |
| LDC-RET-SOD-007 | SoD conflict | "The same person cannot be maker, checker and signatory for this run." | P11 |
| LDC-RET-PII-001 | Aadhaar or prohibited identifier in upload | "Aadhaar numbers are not accepted. Remove the column and re-upload." | P11 |
| LDC-RET-BAT-008 | Unknown data template version | "Template {code} {version} is not supported; download the current version." | P11 |
| LDC-RET-CIC-009 | Forbidden character in commercial file | "Characters ~ and ^ are not allowed in commercial bureau data." | P11 |
| LDC-RET-CIC-010 | Bureau cycle late | "The {cycle} file for {CIC} is past its due date." | P11 |
| LDC-RET-GST-011 | E-invoice not applicable | "E-invoicing does not apply to this GSTIN (CGST Rules r.48(4))." | P11 |
| LDC-RET-GST-012 | Filed GSTR-3B change attempted | "Filed values cannot be edited; use GSTR-1A or the next period." | P11 |
| LDC-RET-WEB-013 | Web-form record cap exceeded | "Over {cap} records — use file upload." | P11 |
| LDC-RET-ACK-014 | Close without acknowledgement | "Upload the portal acknowledgement before closing." | P11 |
| LDC-RET-AI-002 | AI figure not supported by lineage | "The figure in this draft does not match the computed value." | P11 |
| LDC-ACC-001 | Framework change mid-year | "The accounting framework is locked for this financial year." | P11 |
| LDC-ACC-002 | Statement validation failure | "{check} failed: {detail}." | P11 |

#### Error codes — stream S6 (P12–P14, App T)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-DPC-012 | Second extension of a rights request attempted | "This request has already been extended once; the law allows only one extension." | P12 |
| LDC-DPC-020 | Incident close blocked by pending mandatory notification | "Mandatory regulator notification pending: <destination>. Submit or record not-applicable before closing." | P12 |
| LDC-DPC-021 | Clock pause attempted without Correction Entry | "Regulatory clocks cannot be paused. Raise a reasoned correction if the classification was wrong." | P12 |
| LDC-DPC-031 | CISO reporting line violates applicable direction (warning) | "CISO reports to the Head of IT — this conflicts with RBI NBFC Cyber Directions 2026 para 81. An exception has been recorded." | P12/P13 |
| LDC-DPC-040 | Processing activity approval missing mandatory fields | "Add purpose, lawful basis for each applicable law, retention class and at least one system before approval." | P12 |
| LDC-DPC-050 | Full Aadhaar entered in identity verification | "Aadhaar numbers cannot be stored. Use DigiLocker verification or mask all but the last 4 digits." | P12 |
| LDC-TPR-010 | Non-outsourceable activity registered | "This activity cannot be outsourced (NBFC Outsourcing Directions 2025 para 15). Re-scope the arrangement." | P12 |
| LDC-TPR-020 | Arrangement activation with missing mandatory clauses | "Mandatory contract clauses missing: <list>. Add them or record an approved waiver." | P12 |
| LDC-TPR-030 | Materiality downgrade by vendor owner | "The vendor owner cannot approve a materiality downgrade for their own vendor." | P12 |
| LDC-HR-021 | Leave/benefit policy below statutory floor | "This policy is below the statutory minimum (<citation>). Policies may only be more generous." | P13 |
| LDC-HR-030 | Bank-detail change within hold window | "Bank details changed within <n> days of payroll are held for checker review." | P13 |
| LDC-HR-040 | Pay run uses NOT_CONFIRMED parameter | "Parameter <code> is not confirmed. Verify against the Gazette or record a professional opinion before this run." | P13 |
| LDC-HR-041 | SECONDARY_ONLY parameter not acknowledged | "Payroll Compliance Officer must acknowledge secondary-source parameters for this run." | P13 |
| LDC-HR-050 | Same actor in two payroll roles | (uses LDC-CORE-005 maker = checker) | P13 |
| LDC-LAB-011 | POSH IC composition invalid | "At least one-half of IC members must be women and one external member is required (POSH Act s.4)." | P13 |
| LDC-LAB-012 | IC Presiding Officer conflict | "The Presiding Officer cannot be the respondent's line manager for this case." | P13 |
| LDC-LAB-020 | Register regeneration without reason | "Give a reason; the previous version is preserved." | P13 |
| LDC-GRV-010 | Reject/partial decision by drafter alone | "A different user must approve a rejection or partial resolution." | P14 |
| LDC-GRV-012 | Ticket close with pending IO review | "This complaint must be reviewed by the Internal Ombudsman before closure." | P14 |
| LDC-GRV-014 | Final reply missing external route | "External escalation route missing from the final reply." | P14 |
| LDC-GRV-018 | Internal target later than regulatory window | "Internal targets must be earlier than the regulatory deadline." | P14 |
| LDC-GRV-022 | Equator referral without consent | "Record the complainant's consent before proposing mediation or ODR." | P14 |
| LDC-GRV-030 | Locked ladder step removal | "This escalation step is required by the regulator and cannot be removed." | P14 |
| LDC-CFG-031 | Unsigned/tampered rule pack | "Rule pack signature invalid; the pack was not loaded." | P13 (shared) |

#### Error codes — stream S7 (P15–P16, App G, S)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-PACK-001 | Classification fact needs evidence | "Upload evidence (e.g., audited balance sheet or RBI letter) before activating this classification." | P15 |
| LDC-PACK-002 | UL/TL requires RBI advice | "Upper/Top Layer can only be recorded with the RBI advice reference and date." | P15 |
| LDC-PACK-003 | Downgrade requires dispensation | "Your entity stays in the current layer until the next audited balance sheet and RBI dispensation are recorded." | P15 |
| LDC-PACK-004 | Narrowing a Locked obligation without legal basis | "This obligation is statutory. Add the legal basis and a second approver to mark it not applicable." | P15 |
| LDC-PACK-005 | Same person as maker and approver | "Another authorised person must approve this change." | P15 |
| LDC-PACK-006 | Pack conflict unresolved | "Two applicable rules conflict; our content team has been notified. Both are shown until resolved." | P15 |
| LDC-PACK-007 | Stub pack dependency | "Coverage for this law is limited; acknowledge to continue." | P15 |
| LDC-PACK-008 | Regime tag immutable | "The AIF regime chosen for this commitment cannot be changed." | P15 |
| LDC-PACK-009 | Arbitrage monitor needs policy and opinion | "Record the Board policy and legal opinion before enabling arbitrage monitoring." | P15 |
| LDC-PACK-010 | Jurisdiction pack not published | "This country pack is not yet available. We will notify you when it is published." | P15 |
| LDC-PACK-011 | Profile change rollback not allowed | "Rollback is not possible after compliance under the new classification has been completed." | P15 |
| LDC-COOP-001 | RULE_LOOSENING_BLOCKED (bye-law looser than Act/Rules/order) | "This bye-law value is less strict than <provision>. Bye-laws can only add stricter rules." | P16 |
| LDC-COOP-002 | Non-bank society name contains "bank" | "A co-operative society that is not a bank cannot use 'bank', 'banker' or 'banking' in its name." | P16 |
| LDC-COOP-003 | Deposit by ineligible member class | "Only active voting members may hold deposits." | P16 |
| LDC-COOP-004 | Admission decision without resolution reference | "Record the committee resolution reference to approve this application." | P16 |
| LDC-COOP-005 | Refusal without reasons | "State the reasons for refusal; they will be communicated to the applicant." | P16 |
| LDC-COOP-006 | Appropriation below statutory minimum | "The reserve fund allocation is below the statutory minimum of <x>%." | P16 |
| LDC-COOP-007 | Edit refused — Finbyx is system of record | "Members and shares are managed in Finbyx for your society. Open in Finbyx." | P16 |
| LDC-COOP-008 | Private arbitration blocked for statutory-forum dispute | "This dispute falls under <statutory forum>; private arbitration is not available. Conciliation or mediation may be used." | P16 |
| LDC-COOP-009 | Virtual general meeting not permitted | "Your Act/bye-laws do not permit virtual general meetings." | P16 |
| LDC-COOP-010 | SoR switch without migration plan | "Attach the migration and reconciliation plan before switching the system of record." | P16 |

#### Error codes — stream S8 (P17–P19, App K–M)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-AI-001 | Skill not enabled for plan or tenant | "This Vidhi skill isn't available on your plan or has been switched off by your administrator." | P17 |
| LDC-AI-002 | AI budget exhausted | "Your AI budget for this period is used up. Ask your administrator to raise it, or try again after [date]." | P17 |
| LDC-AI-003 | Delegating user no longer valid | "This Vidhi job is paused because its owner no longer has access. Reassign or cancel it." | P17 |
| LDC-AI-004 | Tool not available to run (above ceiling / prohibited) | "Vidhi can't do that action. A person must do it in the app." | P17 |
| LDC-AI-005 | India route unavailable for regulated data | "Vidhi is queued: the India-only AI service is temporarily unavailable. Your request will continue automatically." | P17 |
| LDC-AI-006 | Sealed-class content blocked | "Vidhi can't use confidential case material for this request." | P17 |
| LDC-AI-007 | Blocking validation flag (citation/number/claim) | "This draft has an issue that must be fixed before it can be accepted: [flag]." | P17 |
| LDC-AI-008 | Approval expired | "The approval request expired. Ask Vidhi to prepare it again." | P17 |
| LDC-AI-009 | Out-of-corpus question | "Your selected sources don't cover this. Try other notebooks or ask an expert." | P17 |
| LDC-AI-010 | Unsupported file type for document intelligence | "Vidhi can't read this file type yet: [type]." | P17 |
| LDC-AI-011 | Schedule limit reached | "You have reached the maximum number of active Vidhi schedules." | P17 |
| LDC-INT-001 | Connector prerequisites missing | "Finish the setup steps: [missing]." | P18 |
| LDC-INT-002 | Webhook endpoint invalid (non-HTTPS, private IP, bad certificate) | "This webhook address can't be used: [reason]." | P18 |
| LDC-INT-003 | Webhook signature verification failed (inbound) | "The message signature didn't verify." | P18 |
| LDC-INT-004 | Embed origin not allowed | "This website isn't allowed to submit to this organisation's grievance desk." | P18 |
| LDC-INT-005 | Onboarding lookup provider timeout | "We couldn't fetch details right now. You can enter them manually." | P18 |
| LDC-INT-006 | Calendar sync token revoked | "Your calendar connection stopped. Reconnect or use the calendar link." | P18 |
| LDC-INT-007 | Statutory date edit from external calendar reverted | "This date is managed in LawDocsComply and can't be changed from your calendar." | P18 |
| LDC-INT-008 | Agent offline | "The on-premises agent is offline since [time]." | P18 |
| LDC-INT-009 | Tally company mismatch / listener disabled | "Tally isn't responding for company [name]. Check that Tally is open and the server is enabled." | P18 |
| LDC-INT-010 | Mapping pack validation failed | "The mapping has errors in [fields]." | P18 |
| LDC-INT-011 | Portal automation not permitted | "LawDocsComply prepares the file; an authorised person uploads it on the portal." | P18 |
| LDC-INT-012 | eSign not permitted for document type (IT Act First Schedule) | "This document type can't be signed electronically under the IT Act. Use physical execution." | P18 |
| LDC-INT-013 | DLT template/header not registered | "This SMS template isn't registered on DLT for your organisation." | P18 |
| LDC-INT-014 | WhatsApp use not permitted for this message category | "WhatsApp can't be used for this type of message." | P18 |
| LDC-INT-015 | Client credentials expired | "This API client's key has expired." | P18 |
| LDC-XPT-001 | Export reconciliation failed | "The export stopped because counts didn't match at the snapshot time. It will be retried." | P19 |
| LDC-XPT-002 | Approval required for scope | "This export needs approval from [role]." | P19 |
| LDC-XPT-003 | Restricted class needs DPO approval | "Restricted data needs DPO approval before it can be included." | P19 |
| LDC-XPT-004 | Storage target residency failed | "This storage location can't hold [data class]: it is outside India or couldn't be verified." | P19 |
| LDC-XPT-005 | Canary write failed | "We couldn't write a test file to this storage location: [reason]." | P19 |
| LDC-XPT-006 | Key unavailable (BYOK revoked) | "Your encryption key isn't available. Restore the key grant to continue." | P19 |
| LDC-XPT-007 | Intake conflict (version exists with different hash) | "A different file with the same version already exists; this one will be added as an imported version." | P19 |
| LDC-XPT-008 | Path too long after policy rename | "Folder names are too long; shorten the names in Folder naming settings." | P19 |
| LDC-XPT-009 | Render/PDF-A failure | "A document couldn't be converted: [file]. Our team has been alerted." | P19 |
| LDC-XPT-010 | Exit blocked by open legal hold for selected records | "Some records are under legal hold and will be kept: [list]." | P19 |

#### Error codes — stream S9 (P20–P22, App N, O, X)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-BIL-001 | Catalogue/entitlement signature invalid | "We could not verify the pricing data. Please try again shortly." | P20 |
| LDC-BIL-002 | Billing service unreachable (OH8) | "Billing is temporarily unavailable. Your access is not affected." | P20 |
| LDC-BIL-003 | Quote expired | "This quote has expired. Refresh to get a new one." | P20 |
| LDC-BIL-004 | Payment not yet confirmed | "We are confirming your payment with the bank." | P20 |
| LDC-BIL-005 | Billing profile incomplete | "Add your GSTIN and billing address before purchase." | P20 |
| LDC-BIL-006 | Invalid GSTIN format/status | "This GSTIN is not valid or not active." | P20 |
| LDC-BIL-007 | Purchase requires tenant approval | "This purchase needs approval from <approver>." | P20 |
| LDC-BIL-008 | Promo code invalid/expired/not applicable | "This code cannot be applied to your plan." | P20 |
| LDC-BIL-009 | Usage dispute window closed | "Disputes must be raised within 7 days of the statement." | P20 |
| LDC-BIL-010 | Disposable e-mail domain | "Please use a work or permanent e-mail address." | P20 |
| LDC-BIL-011 | Organisation already has a tenant / trial | "Your organisation already uses LawDocsComply. Ask your admin to invite you." | P20 |
| LDC-BIL-012 | Self extension already used | "You have already extended your trial once." | P20 |
| LDC-BIL-013 | Trial extension needs checker | "Pending second approval." | P20 |
| LDC-BIL-014 | Terms not accepted | "Accept the terms to continue." | P20 |
| LDC-BIL-015 | RE Addendum required before personal-data upload | "As a regulated entity, accept the RE Addendum before uploading documents." | P20 |
| LDC-BIL-020 | Limit reached (users/entities/modules) in plan or RESTRICTED state | "Your plan limit is reached. Ask your admin to upgrade." | P20 |
| LDC-BIL-021 | Module not in plan | "This module is not in your plan. See what it does." | P20 |
| LDC-BIL-022 | Component has dependants | "Remove dependent components first: <list>." | P20 |
| LDC-BIL-023 | Downgrade below usage | "Deactivate or reassign users before downgrading." | P20 |
| LDC-BIL-024 | AI credits exhausted | "Vidhi AI credits are used up. Buy a pack or wait for next month's allowance." | P20 |
| LDC-BIL-030 | Studio lint: package without price for market | — (console) | P20 |
| LDC-BIL-031 | Studio lint: feature row bound to unknown entitlement key | — | P20 |
| LDC-BIL-032 | Studio lint: dependency purchasable alone | — | P20 |
| LDC-BIL-033 | Studio lint: claim without claims-register reference | — | P20 |
| LDC-BIL-034 | Studio lint: badge without computed basis | — | P20 |
| LDC-BIL-035 | Studio lint: dark-pattern pattern detected (countdown, pre-ticked paid item) | — | P20 |
| LDC-BIL-036 | Maker cannot approve own change | — | P20 |
| LDC-BIL-037 | Stream not ACTIVE in OH8 | — | P20 |
| LDC-BIL-038 | Prior-price data missing for promotion | — | P20 |
| LDC-BIL-039 | Presentation version references retired SKU | — | P20 |
| LDC-MKP-001 | Offering not available for buyer entity type | "This service is not offered for your organisation type." | P21 |
| LDC-MKP-002 | RE guard-rail acknowledgement missing | "Please confirm the regulated-entity notice to continue." | P21 |
| LDC-MKP-003 | Proposal expired | "This proposal has expired." | P21 |
| LDC-MKP-004 | Engagement letter hash mismatch at signature | "The document changed; please review the latest version." | P21 |
| LDC-MKP-005 | Revisions exhausted | "Included revisions are used; request a change order." | P21 |
| LDC-MKP-006 | Hour bank exhausted without pre-approval | "Approve additional hours to continue." | P21 |
| LDC-MKP-010 | Provider not verified/suspended | — | P21 |
| LDC-MKP-011 | Offering lint failed (missing exclusions/deliverables) | — | P21 |
| LDC-MKP-012 | Profession mode forbids listing (e.g., CA in practice) | "Listings for this profession are not permitted on the marketplace." | P21 |
| LDC-MKP-013 | Forbidden field for profession render schema | — (CI) | P21 |
| LDC-MKP-014 | Commission not allowed for profession/service class | — | P21 |
| LDC-MKP-015 | Profession-rule change without counsel opinion reference | — | P21 |
| LDC-MKP-020 | Independence/impartiality conflict (certification wall, auditor) | "This provider cannot offer this service to you because of an independence conflict." | P21 |
| LDC-MKP-021 | Reserved service class not deliverable by LawDocs (M1) | — | P21 |
| LDC-MKP-030 | Academy feed stale | — | P21 |
| LDC-SDC-001 | No assignment for client | "You are not assigned to this client." | P22 |
| LDC-SDC-002 | No active delivery grant | "Ask the client admin for maker access." | P22 |
| LDC-SDC-003 | Action outside grant scope | "This action is outside your access scope." | P22 |
| LDC-SDC-004 | Grant expired | "Your access to this client has expired." | P22 |
| LDC-SDC-005 | No checker bound for scope | "A client checker must be set before you can submit." | P22 |
| LDC-SDC-006 | Grant duration exceeds policy | — | P22 |
| LDC-SDC-007 | Delivery user cannot be checker/approver/admin | "LawDocs staff cannot approve work in client workspaces." | P22 |
| LDC-SDC-008 | Only the client admin can approve a delivery grant | — | P22 |
| LDC-SDC-009 | Equator conflict check failed | — | P22 |
| LDC-SDC-010 | Vault entry type blocked (net banking, e-mail, DSC PIN, OTP seed) | "This type of credential cannot be stored." | P22 |
| LDC-SDC-011 | Reveal needs step-up | "Confirm with your security key to view." | P22 |
| LDC-SDC-012 | Client-only credential type without acknowledgement | "This credential is restricted to client users." | P22 |
| LDC-SDC-013 | Reveal locked (anomaly / outside hours) | "Access temporarily locked. Contact the client admin." | P22 |
| LDC-SDC-014 | Reveal needs client approval | "Waiting for the client to approve this view." | P22 |
| LDC-SDC-015 | DLP: credential/ID pattern in message or note | "Remove passwords or ID numbers before sending." | P22 |
| LDC-SDC-020 | Reviewer equals author | "A different reviewer must approve this deliverable." | P22 |
| LDC-SDC-021 | Payload to OH contains prohibited content | — (contract) | P22 |

#### Error codes — stream S10 (P23, App P, R)

| Code | Meaning | User message | Phase |
|---|---|---|---|
| LDC-WEB-001 | Page slug already exists for locale | "Another page already uses this address. Choose a different URL." | P23 |
| LDC-WEB-002 | Block fails JSON Schema validation | "This block has missing or invalid fields. Check the highlighted fields." | P23 |
| LDC-WEB-003 | Maker cannot approve own version | "You drafted this version, so someone else must approve it." | P23 |
| LDC-WEB-004 | Pre-publish check failed (links/alt/headings/axe) | "This page can't be published yet. Fix the items in the pre-publish panel." | P23 |
| LDC-WEB-005 | Claim not approved or expired | "This page uses a claim that isn't approved or has expired. Update the claim or remove it." | P23 |
| LDC-WEB-006 | Experiment not allowed on page type | "Experiments can't run on legal pages or on prices." | P23 |
| LDC-WEB-007 | Health-check family not enabled | "The health check for this type of organisation is coming soon. Try a related type or contact us." | P23 |
| LDC-WEB-008 | Organisation lookup rate limit exceeded | "Too many searches from your network. Enter your details manually or try again in an hour." | P23 |
| LDC-WEB-009 | Organisation lookup provider unavailable | "We couldn't reach the public registry right now. You can continue by entering your details." | P23 |
| LDC-WEB-010 | Submission below minimum answered threshold | "Please answer a few more questions before we calculate your score." | P23 |
| LDC-WEB-011 | Share link expired or revoked | "This report link has expired or was withdrawn by its owner." | P23 |
| LDC-WEB-012 | Prohibited phrase in content (NN-19) | "This text contains a phrase we can't publish (for example a regulator-approval or certification claim). Rephrase it." | P23 |
| LDC-WEB-013 | Consent required for requested action | "We need your permission to email the report. Tick 'Email me my report' or download it instead." | P23 |
| LDC-WEB-014 | Lead delivery to Operations Hub failed (internal) | (internal alert; no user message) | P23 |
| LDC-WEB-015 | Advocate bio contains non-permitted fields | "Advocate profiles can show only the details permitted by the Bar Council rules." | P23 |
| LDC-HLP-001 | "i" key used in build is not published | (build failure) "Glossary key {{key}} has no published definition." | P23 |
| LDC-HLP-002 | Legal definition missing citation | "A legal definition needs its instrument, section and version." | P23 |
| LDC-HLP-003 | Tutorial video missing corrected captions/transcript | "Add corrected captions and a transcript before publishing this video." | P23 |
| LDC-HLP-004 | Capture attempted on non-demo tenant | "Tutorials can only be captured from demo tenants." | P23 |
| LDC-HLP-005 | Accessibility release gate blocked promotion (NN-21) | "Release blocked: open serious or critical accessibility issues on changed screens." | P23 |
| LDC-HLP-006 | Tenant note exceeds length or contains script | "Your note is too long or contains content we can't display." | P23 |

