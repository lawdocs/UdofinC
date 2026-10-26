# Appendix F — Canonical Data Model, Domain Events, Error Catalogue and API Resource Map

> Binding reference for every phase (master §5: "full DDL in Appendix F"). Where a phase file shows additional columns for a table, those columns are **additive**; where a phase file conflicts with this appendix on a name, type, key or constraint, **this appendix prevails** and the phase's migration must be aligned (raise an ADR if you disagree). DDL targets PostgreSQL 16 (Aurora PostgreSQL) with `pgcrypto`, `pg_partman`, `pgvector` and `citext`. Statements are dense: key columns, constraints, FKs, CHECKs, indexes and RLS are shown; audit columns (`created_at`, `updated_at`, `created_by`, `updated_by`) are implied on every mutable table via the `std_cols` convention (F.1.3) unless shown.

---

## F.1 Conventions

### F.1.1 Identity and naming
- **Primary keys**: column `id uuid DEFAULT uuidv7()` (time-ordered UUIDv7, RFC 9562; master X-10). PostgreSQL 18+ provides `uuidv7()` natively; on PostgreSQL 16/17 (Aurora) migration `0001_ids.sql` creates `public.uuidv7()` plus two thin legacy aliases `core.uuid_v7()` and `public.uuid_generate_v7()` so older phase snippets compile. New DDL uses `uuidv7()` only. API identifiers are the UUID string; human references are separate columns (`case_number`, `ticket_no`, `invoice_no`).
- **Foreign keys**: `<entity>_id` referencing `<schema>.<table>(id)`. Tenant FK always `tenant_id uuid NOT NULL REFERENCES core.tenants(id)` on tenant-scoped tables.
- **Case numbers**: `EQ/{VERT}/{CITY}/{YYYY}/{NNNNN}` (master §4.4), unique per tenant prefix; Private Chambers use `core.tenants.case_no_prefix`.
- **Snake case**, plural table names, singular column names; booleans `is_`/`has_` only where ambiguity exists.
- **Enumerations**: `text` + `CHECK (col IN (...))` for open-ended or tenant-extensible sets (changes are migrations reviewed under NN-21); native `ENUM` only for the case state machine (`core.case_state`, P02) and `core.vertical_code`. Value lists are in F.3.

### F.1.2 Time, money, language
- All instants `timestamptz` in UTC; legal dates without time (award date, incident date) are `date`. Working-day computations use `core.holiday_calendars` (state-wise).
- **Money (NN-13)**: `*_minor bigint` + `currency char(3)` (ISO 4217; allowed `INR, USD, EUR, GBP, SGD, AED`, CHECK via domain `core.currency_code`). Never `numeric` for stored money; rates/percentages as `numeric(9,6)`; quantities as `*_milli bigint`. Every non-INR monetary row carries `fx_rate_id` (snapshot) and `inr_equivalent_minor`. GST per line (`cgst_minor`, `sgst_minor`, `igst_minor`, `cess_minor`); TDS separately (`tds_minor`). Rounding: half-up to the minor unit at line level; totals are sums of rounded lines.
- Language codes BCP-47 (`en-IN`, `hi-IN`, …); multilingual text as `jsonb` maps `{ "en": "...", "hi": "..." }` named `*_i18n`.

### F.1.3 Standard columns, retention and deletion
- `std_cols` = `created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now(), created_by uuid, updated_by uuid` + trigger `core.set_updated_at()`.
- **No hard delete** of case, party, document, money or audit data by application roles (`DELETE` revoked). Soft delete `deleted_at timestamptz` only on configuration and profile tables.
- **Retention columns** on every personal-data-bearing table: `retention_class text NOT NULL` (FK `core.retention_classes(code)`), `retain_until date` (computed by the retention service when the triggering event occurs, e.g., case closure + 8 years), `legal_hold boolean NOT NULL DEFAULT false`, `erased_at timestamptz` (field-level erasure/redaction performed, row kept as tombstone where law requires). Defaults per master §11: case records 8 y after closure; caucus notes 12 months; AI logs 12 months; audit 10 y; POSH 7 y; call recordings ≥ 6 months (recovery) or per consent.
- **Encryption**: Tier-High/Sealed fields are application-encrypted `bytea` named `*_enc` (envelope encryption with per-tenant data key; sealed schemas use separate KMS keys). Searchable identifiers use keyed hashes `*_hmac char(64)`.

### F.1.4 Database roles
| Role | Purpose | Notes |
|---|---|---|
| `eq_owner` | migrations only | owns schemas; never used by app |
| `eq_app` | API/worker connections (alias `app_rw`, `app_core` in phase files) | RLS enforced (`FORCE ROW LEVEL SECURITY` on all tenant tables); no `DELETE` on protected tables; no `USAGE` on sealed schemas |
| `eq_platform` | platform-scope jobs (retention, reporting, verification) | RLS policies with `core.platform_scope()`; still no sealed access |
| `eq_posh`, `eq_health`, `eq_safety` | sealed services only | `USAGE` on own sealed schema; no `USAGE` on `growth`; separate connection pool and KMS key |
| `eq_growth` | CRM/CMS service | `USAGE` on `growth` only; **no** `USAGE` on `core`, `fin`…`intl`, sealed (NN-16) |
| `eq_readonly_audit` | auditor exports | `SELECT` on `audit` views with tenant filter |

Session settings set per request by the API (transaction-scoped `SET LOCAL`): `app.tenant_id`, `app.user_id`, `app.person_id`, `app.roles` (comma list), `app.case_ids` (uuid[] of cases the caller is a member of, computed by the policy engine), `app.neutral_id`, `app.staff_scope` (`tenant` for staff with tenant-wide case access), `app.request_id`, `app.platform_scope`.

### F.1.5 Known defect fixed from the old EQR set
EQR-21 declared `audit_log` and `domain_events` as `PARTITION BY RANGE(at)` with a primary key on the event ID alone. PostgreSQL rejects this: **a PRIMARY KEY or UNIQUE constraint on a partitioned table must include all partition-key columns.** Canonical fix applied throughout this appendix:
1. Partitioned tables use composite keys `PRIMARY KEY (<partition_col>, id)` (or `(id, <partition_col>)` where lookups are by ID first).
2. Global uniqueness that cannot include the partition key (idempotency keys, provider message IDs) is enforced in a small **non-partitioned side table** (e.g., `core.communication_keys`), written in the same transaction.
3. Foreign keys **to** a partitioned table reference the full composite key (child carries the partition column, e.g., `communication_planned_at`), or the relationship is logical (no FK) where the child outlives partition detachment.
4. Indexes are created on the parent (propagated to partitions); `pg_partman` pre-creates 3 months ahead and detaches (never drops) expired partitions to WORM export before dropping after retention.
5. **P07 must be aligned**: its `core.communications` snippet declares `id PRIMARY KEY` and `UNIQUE (tenant_id, idempotency_key)` on a table partitioned by `planned_at` — replace with F.4.10.

---

## F.2 Schemas, extensions and helper functions

```sql
CREATE EXTENSION IF NOT EXISTS pgcrypto; CREATE EXTENSION IF NOT EXISTS citext;
CREATE EXTENSION IF NOT EXISTS pg_partman; CREATE EXTENSION IF NOT EXISTS vector;
CREATE SCHEMA core; CREATE SCHEMA audit; CREATE SCHEMA ops; CREATE SCHEMA rls;
CREATE SCHEMA fin; CREATE SCHEMA com; CREATE SCHEMA fam; CREATE SCHEMA ins; CREATE SCHEMA wrk; CREATE SCHEMA intl; CREATE SCHEMA sec;
CREATE SCHEMA grm; CREATE SCHEMA chambers; CREATE SCHEMA academy; CREATE SCHEMA campus; CREATE SCHEMA growth;
CREATE SCHEMA posh_sealed; CREATE SCHEMA health_sealed; CREATE SCHEMA safety_sealed;
REVOKE ALL ON SCHEMA posh_sealed, health_sealed, safety_sealed FROM PUBLIC, eq_app, eq_platform, eq_growth;
GRANT USAGE ON SCHEMA posh_sealed TO eq_posh; GRANT USAGE ON SCHEMA health_sealed TO eq_health;
GRANT USAGE ON SCHEMA safety_sealed TO eq_safety; GRANT USAGE ON SCHEMA growth TO eq_growth;

-- UUIDv7 (RFC 9562): 48-bit unix ms + version/variant + random. Canonical call: uuidv7() (master X-10).
-- Shim for PostgreSQL < 18; on PG 18+ the native pg_catalog.uuidv7() takes precedence in name resolution, so the shim is inert.
CREATE FUNCTION public.uuidv7() RETURNS uuid LANGUAGE sql VOLATILE AS $$
  SELECT encode(set_bit(set_bit(overlay(uuid_send(gen_random_uuid()) PLACING
         substring(int8send((extract(epoch FROM clock_timestamp())*1000)::bigint) FROM 3) FROM 1 FOR 6),
         52, 1), 53, 1), 'hex')::uuid $$;
CREATE FUNCTION core.uuid_v7() RETURNS uuid LANGUAGE sql VOLATILE AS $$ SELECT uuidv7() $$;            -- legacy alias
CREATE FUNCTION public.uuid_generate_v7() RETURNS uuid LANGUAGE sql VOLATILE AS $$ SELECT uuidv7() $$;  -- legacy alias

CREATE DOMAIN core.currency_code AS char(3) CHECK (VALUE IN ('INR','USD','EUR','GBP','SGD','AED'));
CREATE TYPE core.vertical_code AS ENUM ('FIN','COM','FAM','INS','WRK','INT','SEC');
-- core.case_state ENUM as defined in P02 (19 values; F.3)

CREATE FUNCTION core.current_tenant() RETURNS uuid LANGUAGE sql STABLE AS
  $$ SELECT nullif(current_setting('app.tenant_id', true), '')::uuid $$;
CREATE FUNCTION core.current_user_id() RETURNS uuid LANGUAGE sql STABLE AS
  $$ SELECT nullif(current_setting('app.user_id', true), '')::uuid $$;
CREATE FUNCTION core.platform_scope() RETURNS boolean LANGUAGE sql STABLE AS
  $$ SELECT current_user = 'eq_platform' AND current_setting('app.platform_scope', true) = 'all' $$;
CREATE FUNCTION core.has_case_access(p_case uuid) RETURNS boolean LANGUAGE sql STABLE AS
  $$ SELECT p_case = ANY (coalesce(nullif(current_setting('app.case_ids', true), '')::uuid[], '{}'))
            OR current_setting('app.staff_scope', true) = 'tenant' $$;
CREATE FUNCTION core.has_role(p_role text) RETURNS boolean LANGUAGE sql STABLE AS
  $$ SELECT p_role = ANY (string_to_array(coalesce(current_setting('app.roles', true), ''), ',')) $$;

CREATE FUNCTION core.set_updated_at() RETURNS trigger LANGUAGE plpgsql AS
  $$ BEGIN NEW.updated_at := now(); NEW.updated_by := core.current_user_id(); RETURN NEW; END $$;
CREATE FUNCTION core.deny_mutation() RETURNS trigger LANGUAGE plpgsql AS
  $$ BEGIN RAISE EXCEPTION '% is append-only', TG_TABLE_NAME USING ERRCODE = '42501'; END $$;

-- Standard RLS applied to every tenant-scoped table
CREATE FUNCTION rls.enable_tenant_rls(p_schema text, p_table text) RETURNS void LANGUAGE plpgsql AS $$
BEGIN
  EXECUTE format('ALTER TABLE %I.%I ENABLE ROW LEVEL SECURITY', p_schema, p_table);
  EXECUTE format('ALTER TABLE %I.%I FORCE ROW LEVEL SECURITY', p_schema, p_table);
  EXECUTE format('CREATE POLICY tenant_isolation ON %I.%I USING (tenant_id = core.current_tenant())
                  WITH CHECK (tenant_id = core.current_tenant())', p_schema, p_table);
  EXECUTE format('CREATE POLICY platform_read ON %I.%I FOR SELECT USING (core.platform_scope())', p_schema, p_table);
END $$;
-- Case-scoped tables additionally get (RESTRICTIVE so it ANDs with tenant_isolation):
CREATE FUNCTION rls.enable_case_rls(p_schema text, p_table text) RETURNS void LANGUAGE plpgsql AS $$
BEGIN
  PERFORM rls.enable_tenant_rls(p_schema, p_table);
  EXECUTE format('CREATE POLICY case_member AS RESTRICTIVE ON %I.%I USING (core.has_case_access(case_id) OR core.platform_scope())',
                 p_schema, p_table);
END $$;
```

CI check `db:rls-catalogue` fails if any table in `core`, vertical schemas, `grm`, `chambers`, `academy`, `campus` with a `tenant_id` column lacks `relforcerowsecurity = true` and a `tenant_isolation` policy.

---

## F.3 Enumerations (canonical value sets)

| Name | Values |
|---|---|
| `vertical_code` | `FIN`, `COM`, `FAM`, `INS`, `WRK`, `INT`, `SEC` (SEC flag OFF) |
| `tenant_kind` | `institution`, `chambers`, `enterprise`, `grm_client`, `university`, `academy` |
| `case_state` | `draft`, `filed`, `under_scrutiny`, `deficient`, `accepted`, `signposted`, `rejected`, `awaiting_respondent`, `neutral_appointment`, `in_proceedings`, `outcome_drafted`, `outcome_executed`, `in_compliance`, `closed`, `on_hold`, `withdrawn`, `lapsed`, `challenged`, `in_execution` |
| `case_source` | `self_filed`, `counsel_filed`, `enterprise_console`, `bulk`, `api`, `court_referral`, `grm_escalation`, `clause_auto`, `private_chambers`, `marketplace`, `legacy_import` (master §5 set plus additive values) |
| `confidentiality_tier` | `standard`, `high`, `sealed` |
| `mechanism` | `negotiation`, `conciliation`, `mediation`, `arbitration`, `emergency_arbitration`, `med_arb`, `arb_med`, `arb_med_arb`, `expert_determination`, `appeal`, `grievance`, `posh_inquiry`, `signposting` |
| `party_role` | `claimant`, `respondent`, `co_claimant`, `co_respondent`, `intervenor`, `guarantor`, `insurer`, `third_party_beneficiary` |
| `session_kind` | `joint`, `caucus`, `shuttle`, `async_text`, `documents_only`, `preliminary`, `evidentiary`, `final_hearing`, `child_inclusive` |
| `session_mode` | `video`, `audio`, `pstn`, `in_person`, `hybrid`, `async` |
| `clock_category` | `statutory`, `contractual`, `rules_of_procedure`, `service_sla`, `informational` |
| `clock_state` | `pending_trigger`, `running`, `suspended`, `extended`, `satisfied`, `expired`, `breached`, `cancelled` |
| `notice_channel` | `email`, `sms`, `whatsapp`, `push`, `in_app`, `voice`, `speed_post`, `courier`, `hand_delivery` |
| `service_result` | `queued`, `sent`, `delivered`, `read`, `acknowledged`, `bounced`, `failed`, `refused`, `returned_unserved`, `deemed_served` |
| `document_kind` | `pleading`, `evidence`, `notice`, `order`, `award`, `settlement`, `consent`, `kyc`, `certificate`, `transcript`, `minutes`, `bundle`, `correspondence`, `report`, `other` |
| `instrument_class` | `money_settlement`, `consent_terms`, `msa_contractual`, `msa_statutory`, `award`, `order`, `immovable_transfer`, `partition_immovable`, `will`, `trust`, `power_of_attorney`, `conveyance`, `family_settlement_memo` |
| `neutral_type` | `mediator`, `conciliator`, `arbitrator`, `expert`, `ic_external_member` |
| `appointment_status` | as P03: `offered`, `declined`, `expired`, `accepted_pending_objection`, `objection_pending`, `withdrawn_by_institution`, `confirmed`, `under_challenge`, `terminated`, `completed` |
| `invoice_status` | `draft`, `issued`, `partially_paid`, `paid`, `cancelled`, `credit_noted`, `written_off` |
| `payment_status` | `created`, `authorised`, `captured`, `failed`, `refunded_partial`, `refunded`, `disputed` |
| `escrow_state` | `created`, `kyc_pending`, `funded`, `partially_released`, `released`, `refunded`, `frozen`, `closed` |
| `esign_status` | `draft`, `sent`, `partially_signed`, `signed`, `declined`, `expired`, `failed`, `voided` |
| `consent_basis` | `consent`, `legitimate_use_s7`, `legal_claim_s17_1_a`, `legal_obligation`, `s16_transfer` |
| `kyc_method` | `digilocker`, `aadhaar_offline_xml`, `pan_verify`, `ckyc_via_tenant`, `video_kyc`, `passport_mrz`, `manual_document`, `bank_penny_drop` |
| `grm_variant` | `FIN_RBI`, `SEC_LODR`, `WRK_IRCODE`, `WRK_HR`, `WRK_WHISTLE`, `EDU_UGC`, `EDU_AICTE`, `INS_IRDAI` |
| `ai_agent` | `intake_assistant`, `document_extractor`, `case_summariser`, `drafting_assistant`, `negotiation_facilitator`, `translation_agent`, `case_manager_copilot`, `voice_agent`, `grievance_responder`, `qa_auditor`, `analytics_narrator` |
| `retention_class` | `case_record`, `caucus_note`, `ai_log`, `audit`, `posh`, `health`, `family_safety`, `call_recording_recovery`, `call_recording_other`, `kyc`, `financial_tax`, `marketing_lead`, `telemetry`, `academy_record` |

---

## F.4 Core DDL

### F.4.1 Tenancy, identity and access

```sql
CREATE TABLE core.tenants (                         -- as P00 (canonical there); summary
  id uuid PRIMARY KEY DEFAULT uuidv7(), slug text NOT NULL UNIQUE CHECK (slug ~ '^[a-z0-9-]{3,40}$'),
  kind text NOT NULL CHECK (kind IN ('institution','chambers','enterprise','grm_client','university','academy')),
  legal_name text NOT NULL, display_name text NOT NULL, status text NOT NULL DEFAULT 'provisioning'
    CHECK (status IN ('provisioning','active','suspended','offboarding','archived')),
  parent_tenant_id uuid REFERENCES core.tenants(id), data_region text NOT NULL DEFAULT 'ap-south-1',
  default_locale text NOT NULL DEFAULT 'en-IN', enabled_locales text[] NOT NULL DEFAULT ARRAY['en-IN','hi-IN'],
  enabled_verticals core.vertical_code[] NOT NULL DEFAULT '{}', enabled_mechanisms text[] NOT NULL DEFAULT '{}',
  byok_key_arn text, isolation_tier text NOT NULL DEFAULT 'shared' CHECK (isolation_tier IN ('shared','dedicated_cluster')),
  case_no_prefix text, is_test boolean NOT NULL DEFAULT false, is_root boolean NOT NULL DEFAULT false
);
CREATE TABLE core.tenant_domains (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  hostname citext NOT NULL UNIQUE, purpose text NOT NULL CHECK (purpose IN ('portal','email_sender','app_links','embed')),
  acm_status text, verified_at timestamptz);
CREATE TABLE core.tenant_branding (
  tenant_id uuid PRIMARY KEY REFERENCES core.tenants(id), logo_document_id uuid, tokens jsonb NOT NULL,
  email_sender text, legal_footer jsonb NOT NULL, public_label_i18n jsonb, version int NOT NULL DEFAULT 1);

CREATE TABLE core.users (                           -- login identity; not tenant-scoped (memberships are)
  id uuid PRIMARY KEY DEFAULT uuidv7(), person_id uuid NOT NULL UNIQUE,  -- FK added after core.persons
  idp_subject text NOT NULL UNIQUE, kind text NOT NULL CHECK (kind IN ('human','machine')),
  status text NOT NULL DEFAULT 'active' CHECK (status IN ('active','locked','disabled','pending_verification')),
  primary_phone_hmac char(64), primary_email citext, preferred_locale text NOT NULL DEFAULT 'en-IN',
  mfa_required boolean NOT NULL DEFAULT false, last_login_at timestamptz, deleted_at timestamptz);
CREATE TABLE core.memberships (                     -- user × tenant × role (P01)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  user_id uuid NOT NULL REFERENCES core.users(id), role_code text NOT NULL REFERENCES core.role_codes(code),
  status text NOT NULL DEFAULT 'active' CHECK (status IN ('invited','active','suspended','revoked','expired')),
  org_unit_id uuid, sealed_ref text CHECK (sealed_ref IS NULL OR sealed_ref ~ '^sr_[a-z2-7]{26}$'),
  valid_from timestamptz NOT NULL DEFAULT now(), valid_to timestamptz, granted_by uuid,
  CHECK (role_code NOT IN ('ic_presiding_officer','ic_member','ic_external_member') OR sealed_ref IS NOT NULL));
CREATE UNIQUE INDEX memberships_one_active ON core.memberships (tenant_id, user_id, role_code) WHERE status = 'active';
-- core.role_codes(code PK, label_i18n, is_professional, requires_mfa) seeded with master §1.5 list.
CREATE TABLE core.role_grants (                     -- case-scoped / time-bound grants (counsel, auditor, break-glass)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  user_id uuid NOT NULL REFERENCES core.users(id), case_id uuid, scope text NOT NULL,   -- e.g. 'case:read','audit:read'
  purpose text NOT NULL, granted_by uuid NOT NULL, approved_by uuid, starts_at timestamptz NOT NULL DEFAULT now(),
  ends_at timestamptz NOT NULL, revoked_at timestamptz, break_glass boolean NOT NULL DEFAULT false,
  CHECK (ends_at > starts_at), CHECK (NOT break_glass OR approved_by IS NOT NULL),
  CHECK (approved_by IS NULL OR approved_by <> granted_by));
CREATE INDEX ON core.role_grants (user_id, ends_at) WHERE revoked_at IS NULL;
CREATE TABLE core.sessions_auth (
  id uuid PRIMARY KEY DEFAULT uuidv7(), user_id uuid NOT NULL REFERENCES core.users(id),
  device_id uuid, refresh_family_id uuid NOT NULL, refresh_hash char(64) NOT NULL UNIQUE,
  amr text[] NOT NULL, acr text NOT NULL, step_up_until timestamptz, ip_hmac char(64), user_agent text,
  issued_at timestamptz NOT NULL DEFAULT now(), expires_at timestamptz NOT NULL, revoked_at timestamptz, revoke_reason text);
CREATE TABLE core.mfa_factors (
  id uuid PRIMARY KEY DEFAULT uuidv7(), user_id uuid NOT NULL REFERENCES core.users(id),
  kind text NOT NULL CHECK (kind IN ('totp','webauthn','sms_otp','whatsapp_otp','email_link')),
  secret_enc bytea, webauthn_credential_id bytea UNIQUE, public_key bytea, sign_count bigint,
  label text, last_used_at timestamptz, disabled_at timestamptz);
CREATE TABLE core.api_keys (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  machine_user_id uuid NOT NULL REFERENCES core.users(id), prefix char(8) NOT NULL UNIQUE, key_hash char(64) NOT NULL,
  environment text NOT NULL CHECK (environment IN ('sandbox','production')), scopes text[] NOT NULL,
  ip_allowlist cidr[], mtls_cert_fingerprint char(64), rate_limit_per_min int NOT NULL DEFAULT 600,
  expires_at timestamptz, last_used_at timestamptz, revoked_at timestamptz,
  CHECK (NOT ('allocation:run' = ANY (scopes))));                 -- NN-03: machine clients never run allocation
CREATE TABLE core.devices (                         -- P12 FR-P12-05
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  user_id uuid NOT NULL REFERENCES core.users(id), platform text NOT NULL CHECK (platform IN ('ios','android')),
  app_variant text NOT NULL, app_version text NOT NULL, os_version text NOT NULL, model_class text,
  public_key_jwk jsonb NOT NULL, key_attestation text NOT NULL CHECK (key_attestation IN ('secure_enclave','strongbox','tee','software')),
  integrity text NOT NULL CHECK (integrity IN ('pass','degraded','fail')), local_signals int NOT NULL DEFAULT 0,
  status text NOT NULL DEFAULT 'bound' CHECK (status IN ('bound','bound_degraded','restricted','revoked','wiped')),
  last_attested_at timestamptz, last_seen_at timestamptz, revoked_reason text);
CREATE INDEX ON core.devices (user_id, status);
CREATE TABLE core.push_tokens (
  id uuid PRIMARY KEY DEFAULT uuidv7(), device_id uuid NOT NULL REFERENCES core.devices(id),
  provider text NOT NULL CHECK (provider IN ('expo','fcm','apns')), token_hmac char(64) NOT NULL UNIQUE,
  token_enc bytea NOT NULL, categories_enabled text[] NOT NULL, status text NOT NULL DEFAULT 'active', last_receipt_at timestamptz);
CREATE TABLE core.deep_link_tokens (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  purpose text NOT NULL CHECK (purpose IN ('respondent_invite','notice_view','pay','sign')), token_hash char(64) NOT NULL UNIQUE,
  contact_point_id uuid NOT NULL, case_id uuid, max_uses int NOT NULL DEFAULT 10 CHECK (max_uses BETWEEN 1 AND 50),
  use_count int NOT NULL DEFAULT 0, expires_at timestamptz NOT NULL, CHECK (use_count <= max_uses));
```
RLS: `memberships`, `role_grants`, `api_keys`, `devices`, `deep_link_tokens` use `rls.enable_tenant_rls`; `devices` adds owner policy `user_id = core.current_user_id() OR core.has_role('platform_admin') OR core.has_role('support_agent')`. `users`, `sessions_auth`, `mfa_factors` are accessible only through the `identity` module's SECURITY DEFINER functions.

### F.4.2 Directory, consent, KYC/KYB, contact

```sql
CREATE TABLE core.persons (                         -- a natural person; global (one record across tenants), tenant links via memberships/case_parties
  id uuid PRIMARY KEY DEFAULT uuidv7(), full_name_enc bytea NOT NULL, full_name_search_hmac char(64),
  display_name text NOT NULL,                        -- masked form for cross-party views
  dob date, is_minor boolean NOT NULL DEFAULT false, guardian_person_id uuid REFERENCES core.persons(id),
  gender text CHECK (gender IN ('female','male','non_binary','undisclosed')), nationality char(2) DEFAULT 'IN',
  pan_masked text CHECK (pan_masked IS NULL OR pan_masked ~ '^[A-Z]{5}\*{4}[A-Z]$'), pan_hmac char(64),
  aadhaar_ref_masked text CHECK (aadhaar_ref_masked IS NULL OR aadhaar_ref_masked ~ '^X{8}[0-9]{4}$'),  -- NN-14: never full
  preferred_locale text NOT NULL DEFAULT 'en-IN', accessibility_needs text[] NOT NULL DEFAULT '{}',
  retention_class text NOT NULL DEFAULT 'case_record', retain_until date, legal_hold boolean NOT NULL DEFAULT false, erased_at timestamptz,
  CHECK (NOT is_minor OR guardian_person_id IS NOT NULL));
ALTER TABLE core.users ADD FOREIGN KEY (person_id) REFERENCES core.persons(id);
CREATE TABLE core.organisations (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid REFERENCES core.tenants(id),  -- NULL = shared directory entry
  legal_name text NOT NULL, org_type text NOT NULL CHECK (org_type IN ('private_ltd','public_ltd','listed_company','llp','partnership',
    'proprietorship','bank','nbfc','hfc','mfi','arc','fintech_lsp','insurer','tpa','broker','university','government','trust','society','foreign_company','other')),
  cin text, llpin text, gstin text, pan_masked text, udyam_no text, lei char(20), rbi_cor_no text, irdai_regn_no text,
  country char(2) NOT NULL DEFAULT 'IN', is_msme boolean, kyb_status text NOT NULL DEFAULT 'pending'
    CHECK (kyb_status IN ('pending','verified','failed','expired')),
  CHECK (country <> 'IN' OR org_type = 'foreign_company' OR pan_masked IS NOT NULL OR kyb_status = 'pending'));
CREATE UNIQUE INDEX ON core.organisations (cin) WHERE cin IS NOT NULL;
CREATE TABLE core.org_signatories (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  organisation_id uuid NOT NULL REFERENCES core.organisations(id), person_id uuid NOT NULL REFERENCES core.persons(id),
  designation text NOT NULL, authority_document_id uuid, authority_limit_minor bigint CHECK (authority_limit_minor >= 0),
  currency core.currency_code NOT NULL DEFAULT 'INR', can_sign boolean NOT NULL DEFAULT true,
  can_approve_offers boolean NOT NULL DEFAULT false, valid_from date NOT NULL, valid_to date);
CREATE TABLE core.addresses (
  id uuid PRIMARY KEY DEFAULT uuidv7(), owner_kind text NOT NULL CHECK (owner_kind IN ('person','organisation')),
  owner_id uuid NOT NULL, kind text NOT NULL CHECK (kind IN ('residential','registered','correspondence','service')),
  line1_enc bytea NOT NULL, line2_enc bytea, city text NOT NULL, district text, state_code char(2), pincode char(6),
  country char(2) NOT NULL DEFAULT 'IN', verified_via text, valid_from date, valid_to date,
  CHECK (country <> 'IN' OR pincode ~ '^[1-9][0-9]{5}$'));
CREATE TABLE core.contact_points (
  id uuid PRIMARY KEY DEFAULT uuidv7(), owner_kind text NOT NULL, owner_id uuid NOT NULL,
  channel text NOT NULL CHECK (channel IN ('mobile','email','whatsapp','landline')), value_enc bytea NOT NULL,
  value_hmac char(64) NOT NULL, value_masked text NOT NULL, verified_at timestamptz, verification_method text,
  is_primary boolean NOT NULL DEFAULT false, source text NOT NULL CHECK (source IN ('self','claimant_supplied','tenant_supplied','kyc','legacy_import')),
  dnd_status text, UNIQUE (owner_kind, owner_id, channel, value_hmac));
CREATE TABLE core.consent_purposes (
  code text PRIMARY KEY, label_i18n jsonb NOT NULL, default_basis text NOT NULL, optional boolean NOT NULL,
  marketing boolean NOT NULL DEFAULT false, sensitive_category text CHECK (sensitive_category IN ('health','posh','family_safety','financial','children')));
CREATE TABLE core.notices_privacy (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid REFERENCES core.tenants(id), version text NOT NULL,
  locale text NOT NULL, purposes text[] NOT NULL, body_document_id uuid NOT NULL, sha256 char(64) NOT NULL,
  effective_from timestamptz NOT NULL, approved_by uuid NOT NULL, UNIQUE (tenant_id, version, locale));
CREATE TABLE core.consent_records (                 -- P01; NN-15 ledger, append-only (status changes = new row)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  person_id uuid NOT NULL REFERENCES core.persons(id), purpose_code text NOT NULL REFERENCES core.consent_purposes(code),
  basis text NOT NULL CHECK (basis IN ('consent','legitimate_use_s7','legal_claim_s17_1_a','legal_obligation','s16_transfer')),
  status text NOT NULL CHECK (status IN ('given','withdrawn','expired','superseded')), notice_id uuid NOT NULL REFERENCES core.notices_privacy(id),
  case_id uuid, given_by_person_id uuid NOT NULL,     -- guardian when subject is a minor
  channel text NOT NULL, evidence_sha256 char(64) NOT NULL, consent_manager_ref text, source text NOT NULL DEFAULT 'native',
  requires_reconsent boolean NOT NULL DEFAULT false, recorded_at timestamptz NOT NULL DEFAULT now(), expires_at timestamptz,
  supersedes_id uuid REFERENCES core.consent_records(id), retain_until date);   -- ≥ 7 years after withdrawal
CREATE INDEX ON core.consent_records (person_id, purpose_code, recorded_at DESC);
CREATE TRIGGER consent_append_only BEFORE UPDATE OR DELETE ON core.consent_records FOR EACH ROW EXECUTE FUNCTION core.deny_mutation();
CREATE TABLE core.contact_preferences (
  id uuid PRIMARY KEY DEFAULT uuidv7(), person_id uuid NOT NULL REFERENCES core.persons(id), tenant_id uuid,
  channel_order text[] NOT NULL, language text NOT NULL, quiet_start time, quiet_end time, read_receipts boolean NOT NULL DEFAULT true,
  marketing_opt_in boolean NOT NULL DEFAULT false, UNIQUE (person_id, tenant_id));
CREATE TABLE core.quiet_hours_policies (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid REFERENCES core.tenants(id), vertical core.vertical_code,
  recovery_related boolean NOT NULL, allowed_start time NOT NULL, allowed_end time NOT NULL, legal_rule_id uuid,
  CHECK (NOT recovery_related OR (allowed_start >= '08:00' AND allowed_end <= '19:00')));   -- NN-12 floor
CREATE TABLE core.kyc_checks (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  person_id uuid NOT NULL REFERENCES core.persons(id), method text NOT NULL, provider text NOT NULL, provider_ref text,
  result text NOT NULL CHECK (result IN ('pending','verified','failed','manual_review')), liveness_score numeric(5,4),
  face_match_score numeric(5,4), via_tenant_credentials boolean NOT NULL DEFAULT false,   -- NN-14 (CKYC/AA only via tenant)
  masked_reference text, evidence_document_id uuid, checked_at timestamptz, expires_at timestamptz,
  CHECK (method <> 'ckyc_via_tenant' OR via_tenant_credentials));
CREATE TABLE core.kyb_checks (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  organisation_id uuid NOT NULL REFERENCES core.organisations(id), check_type text NOT NULL
    CHECK (check_type IN ('mca','gstin','pan','udyam','lei','rbi_registry','irdai_registry','ubo','sanctions','foreign_registry')),
  provider text NOT NULL, result text NOT NULL, response_digest char(64), checked_at timestamptz NOT NULL);
CREATE TABLE core.dsr_requests (                    -- P01/P14 rights workflow
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  person_id uuid NOT NULL REFERENCES core.persons(id), kind text NOT NULL
    CHECK (kind IN ('access','correction','erasure','nomination','grievance','withdrawal')),
  received_at timestamptz NOT NULL DEFAULT now(), ack_due_at timestamptz NOT NULL, due_at timestamptz NOT NULL,
  legal_hold boolean NOT NULL DEFAULT false, exemption_basis text, status text NOT NULL
    CHECK (status IN ('received','acknowledged','in_progress','fulfilled','partially_fulfilled','rejected','withdrawn')),
  response_document_id uuid, closed_at timestamptz, CHECK (status NOT IN ('rejected','partially_fulfilled') OR exemption_basis IS NOT NULL));
```
RLS: `persons` is reachable only through tenant-scoped joins (`case_parties`, `memberships`) via view `core.v_tenant_persons` with `security_barrier`; `consent_records`, `kyc_checks`, `kyb_checks`, `dsr_requests`, `org_signatories` use tenant RLS; persons see their own consent rows (`person_id = current_setting('app.person_id')::uuid`).

### F.4.3 Taxonomy, cases, parties, claims

```sql
CREATE TABLE core.verticals (code core.vertical_code PRIMARY KEY, label_i18n jsonb NOT NULL, enabled_by_default boolean NOT NULL,
  feature_flag text);                                                    -- SEC → 'vertical.sec.enabled' default OFF
CREATE TABLE core.dispute_types (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid REFERENCES core.tenants(id),   -- NULL = platform taxonomy
  vertical core.vertical_code NOT NULL REFERENCES core.verticals(code), code text NOT NULL, parent_id uuid REFERENCES core.dispute_types(id),
  label_i18n jsonb NOT NULL, arbitrable text NOT NULL CHECK (arbitrable IN ('yes','no','quantum_only','property_only','non_workman_only')),
  default_mechanisms text[] NOT NULL, signposting_forum_codes text[] NOT NULL DEFAULT '{}', active boolean NOT NULL DEFAULT true,
  UNIQUE (tenant_id, vertical, code));
CREATE POLICY dt_read ON core.dispute_types FOR SELECT USING (tenant_id IS NULL OR tenant_id = core.current_tenant());

CREATE TABLE core.cases (                           -- canonical; P02 shows the full column set (additive)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  filing_reference text UNIQUE, case_number text UNIQUE, legacy_ref text,
  vertical core.vertical_code NOT NULL REFERENCES core.verticals(code), dispute_type_id uuid NOT NULL REFERENCES core.dispute_types(id),
  sub_type text, state core.case_state NOT NULL DEFAULT 'draft', hold_reason text,
  confidentiality_tier text NOT NULL CHECK (confidentiality_tier IN ('standard','high','sealed')),
  source text NOT NULL, claim_value_minor bigint CHECK (claim_value_minor >= 0), currency core.currency_code NOT NULL DEFAULT 'INR',
  fx_rate_id uuid, inr_equivalent_minor bigint, languages text[] NOT NULL DEFAULT ARRAY['en'],
  seat_city text, seat_country char(2), venue_city text, governing_law text, mechanism_requested text NOT NULL,
  ruleset_version_id uuid NOT NULL REFERENCES core.ruleset_versions(id),            -- NN-21 pins
  form_schema_version_id uuid NOT NULL REFERENCES core.form_schema_versions(id),
  procedure_rules_id uuid NOT NULL REFERENCES core.procedure_rules(id),
  fee_schedule_id uuid NOT NULL REFERENCES core.fee_schedules(id),
  fee_status text NOT NULL CHECK (fee_status IN ('pending','paid','deferred','waived','offline_verified')),
  safety_flag boolean NOT NULL DEFAULT false,         -- detail only in safety_sealed
  health_data_token text, safety_token text,          -- opaque tokens (NN-07); no FK
  is_posh boolean NOT NULL DEFAULT false CHECK (is_posh = false),                      -- NN-07
  non_arbitrable_flags text[] NOT NULL DEFAULT '{}', explorer_session_id uuid, route_decision_id uuid,
  filed_at timestamptz, accepted_at timestamptz, closed_at timestamptz, closure_reason text,
  retention_class text NOT NULL DEFAULT 'case_record', retain_until date, legal_hold boolean NOT NULL DEFAULT false,
  CONSTRAINT pinned_on_file CHECK (state = 'draft' OR (filing_reference IS NOT NULL AND filed_at IS NOT NULL)),
  CONSTRAINT fee_settled_on_file CHECK (state = 'draft' OR fee_status <> 'pending'),
  CONSTRAINT intl_currency CHECK (vertical = 'INT' OR currency = 'INR'),
  CONSTRAINT number_on_accept CHECK (state IN ('draft','filed','under_scrutiny','deficient','rejected','signposted','withdrawn','closed')
                                     OR case_number IS NOT NULL));
CREATE INDEX ON core.cases (tenant_id, state); CREATE INDEX ON core.cases (tenant_id, vertical, filed_at DESC);
SELECT rls.enable_tenant_rls('core','cases');
CREATE POLICY cases_member AS RESTRICTIVE ON core.cases USING (core.has_case_access(id) OR core.platform_scope());

CREATE TABLE core.case_parties (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  role text NOT NULL CHECK (role IN ('claimant','respondent','co_claimant','co_respondent','intervenor','guarantor','insurer','third_party_beneficiary')),
  person_id uuid REFERENCES core.persons(id), organisation_id uuid REFERENCES core.organisations(id),
  display_label text NOT NULL, is_repeat_player boolean NOT NULL DEFAULT false, vulnerability_flags text[] NOT NULL DEFAULT '{}',  -- never shown to other side
  served_status text NOT NULL DEFAULT 'not_served', joined_at timestamptz, exited_at timestamptz, exit_reason text,
  CHECK ((person_id IS NULL) <> (organisation_id IS NULL)));
CREATE INDEX ON core.case_parties (case_id); CREATE INDEX ON core.case_parties (person_id); CREATE INDEX ON core.case_parties (organisation_id);
SELECT rls.enable_case_rls('core','case_parties');
CREATE TABLE core.party_representatives (           -- counsel mandates (P01)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  case_party_id uuid NOT NULL REFERENCES core.case_parties(id), counsel_person_id uuid NOT NULL REFERENCES core.persons(id),
  bar_enrolment_no text, scope text[] NOT NULL CHECK (scope <@ ARRAY['file','respond','view','attend','negotiate','sign','receive_service']),
  mandate_document_id uuid NOT NULL, status text NOT NULL CHECK (status IN ('pending_verification','active','revoked','expired')),
  valid_from timestamptz NOT NULL, revoked_at timestamptz);
CREATE TABLE core.claims (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  kind text NOT NULL CHECK (kind IN ('claim','counterclaim','set_off')), by_case_party_id uuid NOT NULL REFERENCES core.case_parties(id),
  head text NOT NULL, amount_minor bigint CHECK (amount_minor >= 0), currency core.currency_code NOT NULL DEFAULT 'INR',
  interest_basis jsonb, facts_summary_enc bytea, limitation_status text CHECK (limitation_status IN ('within','expired','disputed','not_applicable')),
  status text NOT NULL DEFAULT 'pleaded');
CREATE TABLE core.reliefs (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  claim_id uuid REFERENCES core.claims(id), relief_type text NOT NULL, description_i18n jsonb NOT NULL,
  amount_minor bigint, currency core.currency_code, arbitrable boolean NOT NULL);
CREATE TABLE core.linked_matters (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  linked_case_id uuid REFERENCES core.cases(id), external_ref text, external_forum text,
  relationship text NOT NULL CHECK (relationship IN ('consolidated','parent','child','related','parallel_forum','sequenced','escalated_from_grm')),
  shared_clock_group_id uuid, CHECK (linked_case_id IS NOT NULL OR external_ref IS NOT NULL), CHECK (linked_case_id IS DISTINCT FROM case_id));
CREATE TABLE core.case_status_history (             -- append-only
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  from_state core.case_state, to_state core.case_state NOT NULL, event text NOT NULL, guard_result jsonb NOT NULL,
  actor_id uuid, reason text, occurred_at timestamptz NOT NULL DEFAULT now(), audit_event_id uuid NOT NULL);
CREATE TRIGGER csh_append_only BEFORE UPDATE OR DELETE ON core.case_status_history FOR EACH ROW EXECUTE FUNCTION core.deny_mutation();
CREATE TABLE core.signposting_events (               -- NN-20
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid REFERENCES core.cases(id), grm_ticket_id uuid,
  forum_code text NOT NULL, last_date_to_act date, reason_code text NOT NULL, channel text NOT NULL, language text NOT NULL,
  script_version text NOT NULL, delivered_by uuid, delivered_at timestamptz NOT NULL, acknowledged_at timestamptz,
  CHECK (case_id IS NOT NULL OR grm_ticket_id IS NOT NULL));
CREATE TABLE core.closure_policies (vertical core.vertical_code PRIMARY KEY, require_owned_clocks boolean NOT NULL,
  require_signposting boolean NOT NULL, require_registration_task_done boolean NOT NULL);
-- Trigger core.guard_case_closure() (P02) raises check_violation 'signposting_required' | 'unowned_clocks' | 'registration_pending'
```

### F.4.4 Proceedings, sessions, orders, offers, outcomes

```sql
CREATE TABLE core.proceedings (                     -- canonical per P04
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  mechanism text NOT NULL CHECK (mechanism IN ('negotiation','conciliation','mediation','arbitration','emergency_arbitration',
    'med_arb','arb_med','arb_med_arb','expert_determination','appeal')),
  phase text CHECK (phase IN ('mediation_phase','arbitration_phase','sealed_award_phase')),
  statutory_mode boolean NOT NULL DEFAULT false, documents_only boolean NOT NULL DEFAULT false,
  fast_track_s29b boolean NOT NULL DEFAULT false, expedited boolean NOT NULL DEFAULT false, ica boolean NOT NULL DEFAULT false,
  config_snapshot jsonb NOT NULL, ruleset_version_id uuid NOT NULL, procedure_rules_id uuid NOT NULL, state text NOT NULL,
  seq_no int NOT NULL, parent_proceeding_id uuid REFERENCES core.proceedings(id), tribunal_size smallint CHECK (tribunal_size IN (1,3)),
  seat_city text, seat_country char(2), language text[] NOT NULL, commenced_at timestamptz, constituted_at timestamptz,
  pleadings_completed_at timestamptz, closed_at timestamptz, outcome_code text,
  CONSTRAINT s29b_sole CHECK (NOT fast_track_s29b OR tribunal_size = 1),
  CONSTRAINT statutory_only_mediation CHECK (NOT statutory_mode OR mechanism IN ('mediation','med_arb','arb_med_arb')),
  UNIQUE (case_id, seq_no));
CREATE TABLE core.proceeding_status_history (LIKE core.case_status_history INCLUDING DEFAULTS);   -- + proceeding_id uuid NOT NULL
ALTER TABLE core.proceeding_status_history ADD COLUMN proceeding_id uuid NOT NULL REFERENCES core.proceedings(id),
  ALTER COLUMN from_state TYPE text, ALTER COLUMN to_state TYPE text;
CREATE TABLE core.sessions (                         -- hearings / mediation sessions
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  proceeding_id uuid NOT NULL REFERENCES core.proceedings(id), kind text NOT NULL, mode text NOT NULL,
  scheduled_start timestamptz NOT NULL, scheduled_end timestamptz NOT NULL, timezone text NOT NULL DEFAULT 'Asia/Kolkata',
  video_room_base text, recording_allowed boolean NOT NULL DEFAULT false, recording_consent_complete boolean NOT NULL DEFAULT false,
  interpreter_language text, status text NOT NULL CHECK (status IN ('scheduled','rescheduled','open','in_progress','adjourned','completed','cancelled')),
  minutes_document_id uuid, adjourned_by text, adjourn_reason text,
  CHECK (scheduled_end > scheduled_start), CHECK (NOT recording_allowed OR recording_consent_complete),
  CHECK (kind <> 'joint' OR mode IS NOT NULL));
-- Trigger: block kind='joint' when cases.safety_flag (SAFETY_FLAG_BLOCKS_JOINT); block recording_allowed when proceeding.mechanism IN
-- ('mediation','conciliation') or phase='mediation_phase' (NN-11 → RECORDING_FORBIDDEN).
CREATE TABLE core.session_attendance (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, session_id uuid NOT NULL REFERENCES core.sessions(id),
  case_id uuid NOT NULL, user_id uuid, case_party_id uuid, participant_role text NOT NULL, room_kind text NOT NULL,
  joined_at timestamptz NOT NULL, left_at timestamptz, join_mode text NOT NULL, liveness_result text, device_id uuid, ip_hmac char(64));
CREATE TABLE core.caucus_notes (                     -- NN-11 sealed to author
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  session_id uuid REFERENCES core.sessions(id), author_neutral_id uuid NOT NULL, note_enc bytea NOT NULL, key_id text NOT NULL,
  retention_class text NOT NULL DEFAULT 'caucus_note', retain_until date, created_at timestamptz NOT NULL DEFAULT now());
ALTER TABLE core.caucus_notes ENABLE ROW LEVEL SECURITY; ALTER TABLE core.caucus_notes FORCE ROW LEVEL SECURITY;
CREATE POLICY caucus_author_only ON core.caucus_notes
  USING (tenant_id = core.current_tenant() AND author_neutral_id = nullif(current_setting('app.neutral_id', true),'')::uuid)
  WITH CHECK (tenant_id = core.current_tenant() AND author_neutral_id = nullif(current_setting('app.neutral_id', true),'')::uuid);
-- No platform_read policy: retention job uses SECURITY DEFINER purge function that touches only retain_until/erasure.
CREATE TABLE core.orders (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, proceeding_id uuid NOT NULL REFERENCES core.proceedings(id),
  order_no int NOT NULL, kind text NOT NULL CHECK (kind IN ('procedural','direction','interim_s17','extension','adjournment','termination','s16_jurisdiction','costs','other')),
  body_document_id uuid NOT NULL, ai_draft_id uuid, status text NOT NULL CHECK (status IN ('draft','approved','issued','served','set_aside')),
  issued_by uuid, issued_at timestamptz, UNIQUE (proceeding_id, order_no));
CREATE TABLE core.offers (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, proceeding_id uuid NOT NULL REFERENCES core.proceedings(id),
  by_case_party_id uuid NOT NULL REFERENCES core.case_parties(id), kind text NOT NULL CHECK (kind IN ('open','without_prejudice','blind_bid','counter','final')),
  amount_minor bigint CHECK (amount_minor >= 0), currency core.currency_code NOT NULL DEFAULT 'INR', terms jsonb NOT NULL,
  blind_value_enc bytea, approved_by_signatory_id uuid REFERENCES core.org_signatories(id), expires_at timestamptz,
  status text NOT NULL CHECK (status IN ('draft','submitted','withdrawn','expired','accepted','rejected','crossed','superseded')),
  submitted_at timestamptz, CHECK (kind <> 'blind_bid' OR blind_value_enc IS NOT NULL));
CREATE TABLE core.settlements (                     -- canonical per P06 (+ columns)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  proceeding_id uuid REFERENCES core.proceedings(id), instrument_type text NOT NULL, instrument_class text NOT NULL, status text NOT NULL,
  execution_route text NOT NULL DEFAULT 'electronic' CHECK (execution_route IN ('electronic','physical','physical_stamp_paper')),
  enforceable_basis text NOT NULL, statutory_rights_waived boolean NOT NULL DEFAULT false CHECK (statutory_rights_waived = false),
  future_claims_discharged boolean NOT NULL DEFAULT false, value_minor bigint, currency core.currency_code,
  language_codes text[] NOT NULL, reflection_until timestamptz, stamp_request_id uuid, signed_pdf_hash char(64), executed_at timestamptz,
  CHECK (enforceable_basis <> 'mediation_s27' OR instrument_type = 'msa_statutory'),                          -- NN-05
  CHECK (instrument_class NOT IN ('immovable_transfer','partition_immovable','will','trust','power_of_attorney','conveyance')
         OR execution_route <> 'electronic'),                                                                  -- NN-08
  CHECK (executed_at IS NULL OR execution_route <> 'electronic' OR stamp_request_id IS NOT NULL));              -- NN-09
CREATE TABLE core.settlement_terms (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, settlement_id uuid NOT NULL REFERENCES core.settlements(id),
  seq int NOT NULL, term_type text NOT NULL CHECK (term_type IN ('payment','instalment','transfer_movable','transfer_immovable','noc',
    'bureau_update','withdrawal_of_proceedings','custody_parenting','maintenance','reinstatement','confidentiality','default_clause','other')),
  obligor_party_id uuid, beneficiary_party_id uuid, amount_minor bigint, currency core.currency_code, due_at timestamptz,
  text_i18n jsonb NOT NULL, lint_status text NOT NULL DEFAULT 'pending', UNIQUE (settlement_id, seq),
  CHECK (term_type NOT IN ('maintenance') OR amount_minor > 0));                  -- maintenance never waived to zero
CREATE TABLE core.awards (                          -- canonical per P06
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  proceeding_id uuid NOT NULL REFERENCES core.proceedings(id),
  award_type text NOT NULL CHECK (award_type IN ('interim','partial','final','consent','additional','corrected','emergency_order','appellate')),
  version int NOT NULL, supersedes_award_id uuid REFERENCES core.awards(id), seat_city text NOT NULL, seat_country char(2) NOT NULL,
  award_date date, signed_at timestamptz, s29a_due_at timestamptz, s29a_extension_ref uuid, reasoned boolean NOT NULL DEFAULT true,
  interest_terms jsonb, costs_terms jsonb, stamp_request_id uuid, sealed boolean NOT NULL DEFAULT false, sealed_hash char(64),
  status text NOT NULL, enforceable_basis text NOT NULL DEFAULT 'ac_s36', signed_pdf_hash char(64),
  CHECK (signed_at IS NULL OR s29a_due_at IS NULL OR signed_at <= s29a_due_at OR s29a_extension_ref IS NOT NULL),   -- NN-04
  CHECK (status NOT IN ('delivered','final','in_execution') OR seat_country <> 'IN' OR stamp_request_id IS NOT NULL), -- NN-09
  CHECK (reasoned OR award_type = 'consent'),
  CHECK (NOT sealed OR sealed_hash IS NOT NULL));
-- NN-06 trigger: INSERT into core.awards rejected when cases.non_arbitrable_flags && ARRAY['matrimonial_status','custody','guardianship',
-- 'testamentary','criminal','insolvency_in_rem'] → CASE_NOT_ARBITRABLE. Retail INS policyholder → INS_RETAIL_ARBITRATION_BLOCKED.
CREATE TABLE core.appeals (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, award_id uuid NOT NULL REFERENCES core.awards(id),
  appeal_proceeding_id uuid REFERENCES core.proceedings(id), filed_by_party_id uuid NOT NULL, grounds_document_id uuid NOT NULL,
  filed_at timestamptz NOT NULL, window_ends_at timestamptz NOT NULL, status text NOT NULL, CHECK (filed_at <= window_ends_at));
```

### F.4.5 Clocks

```sql
CREATE TABLE core.clocks (                          -- canonical per P02 (+ retention); NN-04
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid REFERENCES core.cases(id), proceeding_id uuid,
  grm_ticket_id uuid, sealed_ref text, clock_group_id uuid, kind text NOT NULL,
  category text NOT NULL CHECK (category IN ('statutory','contractual','rules_of_procedure','service_sla','informational')),
  legal_rule_id uuid REFERENCES core.legal_rules(id), trigger_event text NOT NULL, trigger_at timestamptz,
  period_value int NOT NULL CHECK (period_value > 0), period_unit text NOT NULL CHECK (period_unit IN ('hours','calendar_days','working_days','months','years')),
  calendar_code text, calendar_version int, due_at timestamptz, extension_policy jsonb NOT NULL DEFAULT '{}', extensions_used int NOT NULL DEFAULT 0,
  owner_user_id uuid, owner_role text, alert_policy_code text NOT NULL,
  breach_behaviour text NOT NULL CHECK (breach_behaviour IN ('B-CRIT','B-LAPSE','B-AUTO','B-SLA','B-INFO')),
  state text NOT NULL CHECK (state IN ('pending_trigger','running','suspended','extended','satisfied','expired','breached','cancelled')),
  cancel_reason text,
  CONSTRAINT owned_when_running CHECK (category IN ('service_sla','informational') OR state <> 'running' OR owner_user_id IS NOT NULL),
  CONSTRAINT due_when_running CHECK (state = 'pending_trigger' OR due_at IS NOT NULL),
  CONSTRAINT one_subject CHECK (num_nonnulls(case_id, grm_ticket_id, sealed_ref) = 1));
CREATE INDEX clocks_due ON core.clocks (due_at) WHERE state IN ('running','extended');
CREATE TABLE core.clock_alerts (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, clock_id uuid NOT NULL REFERENCES core.clocks(id),
  threshold text NOT NULL CHECK (threshold IN ('T-90','T-60','T-30','T-7','T-3','T-1','T-0','custom')),
  level text NOT NULL CHECK (level IN ('info','blocking_task','escalation','critical')), fired_at timestamptz NOT NULL,
  task_id uuid, acknowledged_by uuid, acknowledged_at timestamptz, UNIQUE (clock_id, threshold));
```

### F.4.6 Notices, service, documents, bundles, evidence

```sql
CREATE TABLE core.notices (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  to_case_party_id uuid NOT NULL REFERENCES core.case_parties(id), notice_type text NOT NULL, template_version_id uuid NOT NULL,
  language text NOT NULL, translation_status text NOT NULL CHECK (translation_status IN ('approved','machine_unofficial','source')),
  document_version_id uuid NOT NULL, content_sha256 char(64) NOT NULL, recovery_related boolean NOT NULL DEFAULT false,
  grievance_officer_block boolean NOT NULL DEFAULT false, status text NOT NULL CHECK (status IN ('draft','approved','dispatching','served','deemed_served','failed','withdrawn')),
  deemed_served_at timestamptz, service_certificate_document_id uuid,
  CHECK (NOT recovery_related OR grievance_officer_block));                      -- NN-12 GRO details in every recovery-related message
CREATE TABLE core.service_attempts (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, notice_id uuid NOT NULL REFERENCES core.notices(id),
  case_id uuid NOT NULL, channel text NOT NULL, contact_point_id uuid, address_id uuid,
  communication_id uuid, communication_planned_at timestamptz,                   -- composite FK to partitioned table (F.1.5 #3)
  attempted_at timestamptz NOT NULL, result text NOT NULL, provider_receipt jsonb, proof_document_id uuid, failure_reason text,
  FOREIGN KEY (communication_planned_at, communication_id) REFERENCES core.communications (planned_at, id));
CREATE TABLE core.documents (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid REFERENCES core.cases(id),
  owner_kind text NOT NULL CHECK (owner_kind IN ('case','neutral','tenant','person','grm_ticket','academy')), owner_id uuid,
  kind text NOT NULL, title text NOT NULL, confidentiality_tier text NOT NULL, privilege text CHECK (privilege IN ('none','without_prejudice','privileged','caucus_derived')),
  instrument_class text, uploaded_by uuid, source text NOT NULL CHECK (source IN ('upload','generated','provider','email_ingest','legacy_import','mobile_capture')),
  current_version_id uuid, exhibit_no text, ai_classification jsonb, quarantine_status text NOT NULL DEFAULT 'clean'
    CHECK (quarantine_status IN ('pending_scan','clean','quarantined','destroyed')),
  retention_class text NOT NULL DEFAULT 'case_record', retain_until date, legal_hold boolean NOT NULL DEFAULT false, deleted_at timestamptz);
CREATE INDEX ON core.documents (case_id, kind);
SELECT rls.enable_tenant_rls('core','documents');
CREATE POLICY doc_case AS RESTRICTIVE ON core.documents
  USING (case_id IS NULL OR core.has_case_access(case_id) OR core.platform_scope());
CREATE POLICY doc_tier AS RESTRICTIVE ON core.documents
  USING (confidentiality_tier <> 'sealed' OR core.has_role('case_manager') OR core.has_role('neutral_mediator')
         OR core.has_role('neutral_arbitrator') OR core.has_role('neutral_conciliator') OR uploaded_by = core.current_user_id());
CREATE TABLE core.document_versions (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, document_id uuid NOT NULL REFERENCES core.documents(id),
  version int NOT NULL, s3_bucket text NOT NULL, s3_key text NOT NULL, s3_version_id text NOT NULL, sha256 char(64) NOT NULL,
  size_bytes bigint NOT NULL CHECK (size_bytes > 0), mime_type text NOT NULL, page_count int, ocr_text_ref text, derived_from_version_id uuid,
  capture_manifest jsonb, created_at timestamptz NOT NULL DEFAULT now(), UNIQUE (document_id, version));
CREATE TABLE core.upload_sessions (                  -- P12 resumable uploads
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, user_id uuid NOT NULL, device_id uuid, case_id uuid,
  purpose text NOT NULL, filename text NOT NULL, mime_type text NOT NULL, size_bytes bigint NOT NULL CHECK (size_bytes BETWEEN 1 AND 524288000),
  sha256_declared char(64) NOT NULL, s3_upload_id text NOT NULL, parts_received int[] NOT NULL DEFAULT '{}',
  status text NOT NULL CHECK (status IN ('open','complete','quarantined','expired','failed')), quarantine_reason text, expires_at timestamptz NOT NULL);
CREATE TABLE core.bundles (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  purpose text NOT NULL CHECK (purpose IN ('hearing','execution','appeal','court_filing','regulator','party_copy')),
  manifest_sha256 char(64), bsa_63_part_a_document_id uuid, bsa_63_part_b_document_id uuid,     -- NN-10
  status text NOT NULL CHECK (status IN ('building','ready','certified','exported','superseded')), generated_at timestamptz,
  CHECK (status NOT IN ('certified','exported') OR (manifest_sha256 IS NOT NULL AND bsa_63_part_a_document_id IS NOT NULL)));
CREATE TABLE core.bundle_items (
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, bundle_id uuid NOT NULL REFERENCES core.bundles(id),
  seq int NOT NULL, document_version_id uuid NOT NULL REFERENCES core.document_versions(id), sha256 char(64) NOT NULL,
  page_from int, page_to int, label text, UNIQUE (bundle_id, seq));
CREATE TABLE core.evidence_ledger (                 -- canonical: merges P00 (storage/WORM fields) and P02 (per-case sequence)
  id uuid NOT NULL DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id), case_id uuid,   -- NULL for tenant-level artefacts
  ledger_scope uuid GENERATED ALWAYS AS (coalesce(case_id, tenant_id)) STORED, seq bigint NOT NULL,
  artefact_type text NOT NULL, item_ref uuid NOT NULL, document_version_id uuid REFERENCES core.document_versions(id),
  s3_bucket text NOT NULL, s3_key text NOT NULL, s3_version_id text NOT NULL, sha256 char(64) NOT NULL CHECK (sha256 ~ '^[0-9a-f]{64}$'),
  retention_mode text NOT NULL DEFAULT 'COMPLIANCE', retain_until timestamptz NOT NULL, legal_hold boolean NOT NULL DEFAULT false,
  provenance text NOT NULL DEFAULT 'native' CHECK (provenance IN ('native','provider','legacy_import','imported_unverified_provenance')),
  prev_hash char(64) NOT NULL, entry_hash char(64) NOT NULL, recorded_by uuid, created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (ledger_scope, seq), UNIQUE (id), UNIQUE (s3_bucket, s3_key, s3_version_id));
REVOKE UPDATE, DELETE ON core.evidence_ledger FROM eq_app;   -- legal_hold changed only via SECURITY DEFINER documents.set_legal_hold()
```

### F.4.7 Neutrals (P03 shows full columns; key constraints here)

```sql
CREATE TABLE core.neutrals (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, person_id uuid NOT NULL REFERENCES core.persons(id),
  types text[] NOT NULL CHECK (types <@ ARRAY['mediator','conciliator','arbitrator','expert','ic_external_member']),
  status text NOT NULL CHECK (status IN ('applicant','under_review','empanelled','suspended','retired','de_empanelled')),
  grade text CHECK (grade IN ('A','B','C')), languages text[] NOT NULL, cities text[] NOT NULL, verticals core.vertical_code[] NOT NULL,
  nationalities char(2)[] NOT NULL DEFAULT ARRAY['IN'], timezone text NOT NULL DEFAULT 'Asia/Kolkata', pi_cover_expiry date,
  public_profile_published boolean NOT NULL DEFAULT false, UNIQUE (tenant_id, person_id));
CREATE TABLE core.neutral_accreditations (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, neutral_id uuid NOT NULL REFERENCES core.neutrals(id),
  scheme text NOT NULL, level text, issuer text NOT NULL, issued_on date, expires_on date, evidence_document_id uuid,
  status text NOT NULL CHECK (status IN ('unverified','verified','expired','revoked')));
CREATE TABLE core.neutral_panels (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, code text NOT NULL,
  vertical core.vertical_code, neutral_type text NOT NULL, allocation_policy_version_id uuid NOT NULL, UNIQUE (tenant_id, code));
CREATE TABLE core.panel_memberships (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, panel_id uuid NOT NULL REFERENCES core.neutral_panels(id),
  neutral_id uuid NOT NULL REFERENCES core.neutrals(id), status text NOT NULL, valid_from date NOT NULL, valid_to date, UNIQUE (panel_id, neutral_id));
CREATE TABLE core.neutral_availability (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, neutral_id uuid NOT NULL REFERENCES core.neutrals(id),
  slot tstzrange NOT NULL, kind text NOT NULL CHECK (kind IN ('available','blocked','booked')), session_id uuid,
  EXCLUDE USING gist (neutral_id WITH =, slot WITH &&) WHERE (kind = 'booked'));   -- requires btree_gist
CREATE TABLE core.neutral_disclosures (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, neutral_id uuid NOT NULL REFERENCES core.neutrals(id),
  case_id uuid, form text NOT NULL CHECK (form IN ('sixth_schedule','mediator_standard','ic_external','expert')), circumstances jsonb NOT NULL,
  fifth_schedule_hits text[] NOT NULL DEFAULT '{}', seventh_schedule_hits text[] NOT NULL DEFAULT '{}', declared_independent boolean NOT NULL,
  esign_request_id uuid, submitted_at timestamptz NOT NULL, CHECK (declared_independent OR cardinality(seventh_schedule_hits) > 0));
CREATE TABLE core.neutral_challenges (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, appointment_id uuid NOT NULL,
  case_id uuid NOT NULL, by_case_party_id uuid NOT NULL, grounds text NOT NULL, filed_at timestamptz NOT NULL, decided_by text, decision text, decided_at timestamptz);
-- core.appointments and core.allocation_runs: canonical in P03 (constraints nn03_no_party_choice_repeat_player, confirm_requires_disclosure,
-- confirm_requires_seventh_clear). Added here: allocation_runs.prev_hash/row_hash char(64) (hash chain per tenant) and
-- CHECK (initiated_by NOT IN enterprise principals) enforced by trigger → APPOINTMENT_LENDER_TRIGGER_BLOCKED (NN-03).
CREATE TABLE core.neutral_scorecards (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, neutral_id uuid NOT NULL REFERENCES core.neutrals(id),
  period daterange NOT NULL, timeliness_pct numeric(5,2), orders_on_time_pct numeric(5,2), awards_challenged int, awards_set_aside int,
  feedback_avg numeric(3,2), cpd_hours numeric(5,1), CHECK (true));               -- NN-16: no win/loss or party-type outcome metrics
CREATE TABLE core.neutral_reviews (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, neutral_id uuid NOT NULL, case_id uuid NOT NULL,
  by_case_party_id uuid NOT NULL, process_rating smallint CHECK (process_rating BETWEEN 1 AND 5), comment_enc bytea, moderated boolean NOT NULL DEFAULT false,
  UNIQUE (case_id, by_case_party_id, neutral_id));
```

### F.4.8 Fees, billing, payments, escrow, FX (Appendix B §B.2 canonical for fee_schedules, quotes, quote_lines, fx_rates — master X-08; P05 canonical for tariff_items, invoice_lines, payments, escrow_milestones, ledger, plans)

The four Appendix B tables are summarised here only for orientation and are aligned with it: `fee_schedules.status` ∈ (`draft`, `in_review`, `approved`, `published`, `retired`) with maker–checker and a golden-suite run before `published` (master §7's "superseded" = `retired`); `fx_rates.rate_e8 bigint` (1 base = rate_e8 / 10^8 quote) with Appendix B sources; FX staleness = Appendix B FX-5 (snapshot older than 3 business days → `FX_RATE_STALE`); `plans.product_line` uses the P05 named lines.

```sql
CREATE TABLE core.fee_schedules (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, version int NOT NULL,
  vertical core.vertical_code, currency core.currency_code NOT NULL, board_approval_ref text, status text NOT NULL
  CHECK (status IN ('draft','in_review','approved','published','retired')), effective_from timestamptz, regulated boolean NOT NULL DEFAULT false,
  UNIQUE (tenant_id, code, version));                 -- full column set and CHECKs: Appendix B §B.2
CREATE TABLE core.quotes (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid, fee_schedule_id uuid NOT NULL REFERENCES core.fee_schedules(id),
  inputs jsonb NOT NULL, inputs_sha256 char(64) NOT NULL, total_minor bigint NOT NULL, currency core.currency_code NOT NULL, fx_rate_id uuid, expires_at timestamptz NOT NULL);
CREATE TABLE core.quote_lines (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, quote_id uuid NOT NULL REFERENCES core.quotes(id),
  tariff_item_id uuid NOT NULL, payer_case_party_id uuid, taxable_minor bigint NOT NULL, tax_minor bigint NOT NULL, explanation_i18n jsonb NOT NULL);
CREATE TABLE core.invoices (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, invoice_no text NOT NULL, series text NOT NULL,
  case_id uuid, buyer_kind text NOT NULL, buyer_id uuid NOT NULL, buyer_gstin text, place_of_supply char(2), currency core.currency_code NOT NULL,
  total_minor bigint NOT NULL CHECK (total_minor >= 0), status text NOT NULL, irn text, ack_no text, export_under_lut boolean NOT NULL DEFAULT false,
  issued_at timestamptz, due_at timestamptz, UNIQUE (tenant_id, series, invoice_no));               -- gapless series via sequence table per FY
CREATE TABLE core.refunds (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, payment_id uuid NOT NULL REFERENCES core.payments(id),
  amount_minor bigint NOT NULL CHECK (amount_minor > 0), reason_code text NOT NULL, credit_note_invoice_id uuid, provider_refund_id text UNIQUE,
  status text NOT NULL, maker_user_id uuid NOT NULL, checker_user_id uuid, CHECK (checker_user_id IS DISTINCT FROM maker_user_id));
CREATE TABLE core.payouts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, payee_kind text NOT NULL CHECK (payee_kind IN ('neutral','tenant','partner','university')),
  payee_id uuid NOT NULL, period daterange, gross_minor bigint NOT NULL, tds_minor bigint NOT NULL DEFAULT 0, net_minor bigint NOT NULL,
  currency core.currency_code NOT NULL, provider text, provider_payout_id text UNIQUE, status text NOT NULL, CHECK (net_minor = gross_minor - tds_minor));
CREATE TABLE core.payout_lines (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, payout_id uuid NOT NULL REFERENCES core.payouts(id),
  case_id uuid, invoice_line_id uuid NOT NULL, amount_minor bigint NOT NULL, tds_section_code text);
CREATE TABLE core.escrow_accounts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  provider text NOT NULL CHECK (provider IN ('razorpayx_escrow_plus','castler','bank_direct','direct_with_proof')), trustee_name text,
  virtual_account_masked text, total_minor bigint NOT NULL, currency core.currency_code NOT NULL, state text NOT NULL,
  agreement_document_id uuid NOT NULL);           -- NN-13: settlement sums never use Equator merchant account
CREATE TABLE core.instalment_plans (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, settlement_id uuid NOT NULL REFERENCES core.settlements(id),
  rail text NOT NULL CHECK (rail IN ('escrow','upi_autopay_direct','enach_direct','direct_with_proof')), count int NOT NULL CHECK (count BETWEEN 1 AND 120),
  total_minor bigint NOT NULL, currency core.currency_code NOT NULL, default_rule jsonb NOT NULL, status text NOT NULL);
CREATE TABLE core.instalments (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, plan_id uuid NOT NULL REFERENCES core.instalment_plans(id),
  seq int NOT NULL, due_on date NOT NULL, amount_minor bigint NOT NULL CHECK (amount_minor > 0), paid_minor bigint NOT NULL DEFAULT 0,
  proof_document_id uuid, status text NOT NULL CHECK (status IN ('scheduled','due','paid','partially_paid','missed','waived','cured')), UNIQUE (plan_id, seq));
CREATE TABLE core.fx_rates (id uuid PRIMARY KEY DEFAULT uuidv7(), base core.currency_code NOT NULL, quote core.currency_code NOT NULL,
  rate_e8 bigint NOT NULL CHECK (rate_e8 > 0), source text NOT NULL, as_of timestamptz NOT NULL, fetched_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (base, quote, source, as_of));                -- full definition Appendix B §B.2; staleness per Appendix B FX-5 → FX_RATE_STALE
CREATE TABLE core.plans (id uuid PRIMARY KEY DEFAULT uuidv7(), code text NOT NULL UNIQUE, product_line text NOT NULL CHECK (product_line IN ('chambers','grm_lender','grm_listed','grm_employer','grm_university','posh','enterprise_api','academy_membership')),   -- P05 FR-P05-35
  price_minor bigint NOT NULL, currency core.currency_code NOT NULL, interval text NOT NULL, allowances jsonb NOT NULL);
CREATE TABLE core.subscriptions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, plan_id uuid NOT NULL REFERENCES core.plans(id),
  status text NOT NULL, current_period tstzrange NOT NULL, provider_subscription_id text, usage jsonb NOT NULL DEFAULT '{}');
```

### F.4.9 eSign, eStamp, registration, execution, compliance (P06 canonical for compliance_obligations, stamp_duty_rules)

```sql
CREATE TABLE core.esign_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid, document_version_id uuid NOT NULL,
  instrument_class text NOT NULL, provider text NOT NULL, provider_envelope_id text UNIQUE, status text NOT NULL, expires_at timestamptz,
  audit_trail_document_id uuid,
  CHECK (instrument_class NOT IN ('immovable_transfer','partition_immovable','will','trust','power_of_attorney','conveyance')));   -- NN-08 → ESIGN_EXCLUDED_INSTRUMENT
CREATE TABLE core.esign_signers (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, esign_request_id uuid NOT NULL REFERENCES core.esign_requests(id),
  seq int NOT NULL, person_id uuid NOT NULL, signing_capacity text NOT NULL, method text NOT NULL CHECK (method IN ('aadhaar_esign','dsc','virtual_sign')),
  status text NOT NULL, signed_at timestamptz, certificate_serial text, step_up_session_id uuid, UNIQUE (esign_request_id, seq));
CREATE TABLE core.estamp_requests (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, instrument_type text NOT NULL,
  state_code char(2) NOT NULL, stamp_duty_rule_id uuid NOT NULL REFERENCES core.stamp_duty_rules(id), duty_minor bigint NOT NULL CHECK (duty_minor >= 0),
  first_party text NOT NULL, second_party text NOT NULL, provider text NOT NULL, certificate_no text, certificate_document_id uuid,
  status text NOT NULL, statutory_deadline date, stamped_at timestamptz);                     -- NN-09
CREATE TABLE core.registration_tasks (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, settlement_id uuid,
  award_id uuid, sub_registrar_office text, legal_basis text NOT NULL DEFAULT 'Registration Act 1908 s.17', checklist jsonb NOT NULL,
  appointment_at timestamptz, registered_at timestamptz, registration_no text, status text NOT NULL);           -- NN-08
CREATE TABLE core.execution_packs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL, outcome_kind text NOT NULL,
  outcome_id uuid NOT NULL, bundle_id uuid NOT NULL REFERENCES core.bundles(id), route text NOT NULL, court text, petition_status text,
  generated_at timestamptz NOT NULL);
```

### F.4.10 Communications (partitioned — defect fix), journeys, voice

```sql
CREATE TABLE core.communications (                 -- replaces P07 snippet (F.1.5 #5); other P07 columns unchanged
  id uuid NOT NULL DEFAULT uuidv7(), planned_at timestamptz NOT NULL, tenant_id uuid NOT NULL,
  case_id uuid, case_party_id uuid, person_id uuid NOT NULL, journey_run_id uuid,
  channel text NOT NULL CHECK (channel IN ('email','sms','whatsapp','push','in_app','voice','speed_post')),
  purpose_code text NOT NULL, template_variant_id uuid, legal_service boolean NOT NULL DEFAULT false, recovery_related boolean NOT NULL DEFAULT false,
  status text NOT NULL, policy_decision jsonb NOT NULL, provider_code text, provider_message_id text, content_sha256 char(64),
  idempotency_key char(64) NOT NULL, sent_at timestamptz, delivered_at timestamptz, engaged_at timestamptz,
  retention_class text NOT NULL DEFAULT 'case_record', created_at timestamptz NOT NULL DEFAULT now(),
  PRIMARY KEY (planned_at, id)) PARTITION BY RANGE (planned_at);
CREATE INDEX ON core.communications (case_id, planned_at DESC); CREATE INDEX ON core.communications (id);
SELECT partman.create_parent('core.communications', 'planned_at', 'native', 'monthly', p_premake := 3);
CREATE TABLE core.communication_keys (             -- global uniqueness outside the partitioned table
  tenant_id uuid NOT NULL, idempotency_key char(64) NOT NULL, communication_id uuid NOT NULL, planned_at timestamptz NOT NULL,
  PRIMARY KEY (tenant_id, idempotency_key));
CREATE TABLE core.communication_provider_refs (provider_code text NOT NULL, provider_message_id text NOT NULL,
  communication_id uuid NOT NULL, planned_at timestamptz NOT NULL, PRIMARY KEY (provider_code, provider_message_id));
-- NN-12 trigger on INSERT/UPDATE to status 'queued': if recovery_related and channel IN ('sms','whatsapp','voice') and local time of
-- recipient ∉ [08:00, 19:00) or an active core.contact_blackouts row exists → raise CONTACT_OUTSIDE_WINDOW / CONTACT_BLACKOUT_ACTIVE.
CREATE TABLE core.message_templates (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, channel text NOT NULL, locale text NOT NULL,
  version int NOT NULL, body text NOT NULL, safe_fields text[] NOT NULL, dlt_template_id text, wa_template_name text,
  legal_review_status text NOT NULL CHECK (legal_review_status IN ('draft','approved','rejected')), recovery_related boolean NOT NULL DEFAULT false,
  UNIQUE (tenant_id, code, channel, locale, version), CHECK (channel <> 'sms' OR dlt_template_id IS NOT NULL OR legal_review_status = 'draft'));
CREATE TABLE core.journeys (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, version int NOT NULL, definition jsonb NOT NULL, status text NOT NULL);
CREATE TABLE core.journey_runs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, journey_id uuid NOT NULL REFERENCES core.journeys(id),
  case_id uuid, person_id uuid NOT NULL, temporal_workflow_id text NOT NULL UNIQUE, status text NOT NULL, started_at timestamptz NOT NULL);
-- core.call_records: canonical in P07 (UNIQUE (voice_provider, provider_call_id); recording retention ≥ 6 months recovery; legal_hold)
CREATE TABLE core.transcripts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, source_kind text NOT NULL CHECK (source_kind IN ('call','arbitration_hearing','voice_note')),
  source_id uuid NOT NULL, case_id uuid, language text NOT NULL, engine text NOT NULL, machine_generated boolean NOT NULL DEFAULT true,
  document_version_id uuid NOT NULL, approved_by uuid, CHECK (source_kind <> 'arbitration_hearing' OR approved_by IS NOT NULL OR machine_generated));
CREATE TABLE core.case_threads (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  thread_kind text NOT NULL CHECK (thread_kind IN ('party_institution','neutral_party','all_parties')), party_scope uuid,
  confidentiality text NOT NULL CHECK (confidentiality IN ('mediation_confidential','arbitral_record','administrative')), status text NOT NULL,
  CHECK ((thread_kind = 'neutral_party') = (party_scope IS NOT NULL)));
CREATE TABLE core.case_messages (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, thread_id uuid NOT NULL REFERENCES core.case_threads(id),
  case_id uuid NOT NULL, author_user_id uuid NOT NULL, body_enc bytea, attachment_document_id uuid, created_at timestamptz NOT NULL DEFAULT now(),
  retracted_at timestamptz, moderation_flags text[] NOT NULL DEFAULT '{}', CHECK (body_enc IS NOT NULL OR attachment_document_id IS NOT NULL));
CREATE TABLE core.notifications (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, user_id uuid NOT NULL, category text NOT NULL,
  title_key text NOT NULL, params jsonb NOT NULL, deeplink text, read_at timestamptz, created_at timestamptz NOT NULL DEFAULT now());
```

### F.4.11 Rules, configuration, forms, templates (P00 canonical for rulesets, ruleset_versions, legal_rules, config_change_requests, feature_flags)

```sql
CREATE TABLE core.procedure_rules (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, version int NOT NULL,
  mechanism text NOT NULL, verticals core.vertical_code[] NOT NULL, published_document_id uuid NOT NULL, board_approval_ref text,
  effective_from timestamptz NOT NULL, status text NOT NULL, UNIQUE (tenant_id, code, version));
CREATE TABLE core.form_schemas (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, slug text NOT NULL, vertical core.vertical_code, UNIQUE (tenant_id, slug));
CREATE TABLE core.form_schema_versions (id uuid PRIMARY KEY DEFAULT uuidv7(), form_schema_id uuid NOT NULL REFERENCES core.form_schemas(id),
  version int NOT NULL, json_schema jsonb NOT NULL, ui_schema jsonb NOT NULL, i18n jsonb NOT NULL, migration_from_prev jsonb,
  status text NOT NULL CHECK (status IN ('draft','in_review','active','superseded')), legal_review_by uuid, effective_from timestamptz, UNIQUE (form_schema_id, version));
CREATE TABLE core.form_submissions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, form_schema_version_id uuid NOT NULL REFERENCES core.form_schema_versions(id),
  case_id uuid, submitted_by uuid NOT NULL, data_enc bytea NOT NULL, data_sha256 char(64) NOT NULL, status text NOT NULL CHECK (status IN ('draft','submitted','superseded')),
  assisted_by uuid, submitted_at timestamptz);
CREATE TABLE core.document_templates (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, code text NOT NULL, locale text NOT NULL, version int NOT NULL,
  instrument_class text, body_handlebars text NOT NULL, clause_refs text[] NOT NULL DEFAULT '{}', legal_review_status text NOT NULL,
  UNIQUE (tenant_id, code, locale, version));                         -- NN-23: activation requires legal_review_status='approved'
-- core.config_change_requests: maker–checker; CHECK (checker_id <> maker_id); status draft→submitted→approved→applied|rejected (P00).
```

### F.4.12 Integration, enterprise, bulk (P00/Appendix D canonical for outbox, webhook_inbox, provider_routing)

```sql
CREATE TABLE core.webhook_subscriptions (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, url text NOT NULL CHECK (url ~ '^https://'),
  event_types text[] NOT NULL, secret_enc bytea NOT NULL, status text NOT NULL,
  CHECK (array_to_string(event_types, ' ') !~ '(^| )equator\.(posh|health|safety)\.'));   -- sealed events never subscribable; the dispatcher also drops them
CREATE TABLE core.webhook_deliveries (id uuid NOT NULL DEFAULT uuidv7(), attempted_at timestamptz NOT NULL, tenant_id uuid NOT NULL,
  subscription_id uuid NOT NULL, event_id uuid NOT NULL, attempt int NOT NULL, http_status int, latency_ms int, next_retry_at timestamptz,
  PRIMARY KEY (attempted_at, id)) PARTITION BY RANGE (attempted_at);
CREATE TABLE core.bulk_jobs (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, kind text NOT NULL CHECK (kind IN ('case_intake','notice_campaign','status_writeback','grm_import')),
  source text NOT NULL CHECK (source IN ('csv_upload','sftp','api')), file_sha256 char(64), total_rows int NOT NULL, accepted int NOT NULL DEFAULT 0,
  deficient int NOT NULL DEFAULT 0, rejected int NOT NULL DEFAULT 0, status text NOT NULL, CHECK (accepted + deficient + rejected <= total_rows));
CREATE TABLE core.bulk_job_rows (bulk_job_id uuid NOT NULL REFERENCES core.bulk_jobs(id), row_no int NOT NULL, tenant_id uuid NOT NULL,
  row_hash char(64) NOT NULL, status text NOT NULL, error_codes text[] NOT NULL DEFAULT '{}', case_id uuid, PRIMARY KEY (bulk_job_id, row_no));
```

### F.4.13 AI, work queue, reports (P11 canonical for ai_interactions, ai_suggestions)

```sql
CREATE TABLE core.ai_prompt_versions (id uuid PRIMARY KEY DEFAULT uuidv7(), agent text NOT NULL, version text NOT NULL, prompt_sha256 char(64) NOT NULL,
  policy_version text NOT NULL, model_id text NOT NULL, status text NOT NULL CHECK (status IN ('draft','evaluating','approved','retired')),
  approved_by uuid, UNIQUE (agent, version));
CREATE TABLE core.ai_eval_runs (id uuid PRIMARY KEY DEFAULT uuidv7(), prompt_version_id uuid NOT NULL REFERENCES core.ai_prompt_versions(id),
  suite text NOT NULL, cases int NOT NULL, passed int NOT NULL, zero_tolerance_failures int NOT NULL, gate_result text NOT NULL CHECK (gate_result IN ('pass','fail')),
  CHECK (zero_tolerance_failures = 0 OR gate_result = 'fail'));              -- NN-01 release gate
CREATE TABLE core.ai_feedback (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, interaction_id uuid NOT NULL, by_user_id uuid NOT NULL,
  verdict text NOT NULL CHECK (verdict IN ('accepted','edited','rejected','flagged_unsafe')), note text);
-- core.ai_interactions (P11): requires_human_review boolean NOT NULL DEFAULT true CHECK (requires_human_review); no FK to sealed schemas.
CREATE TABLE core.tasks (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid, sealed_ref text, kind text NOT NULL,
  assignee_user_id uuid, assignee_role text, due_at timestamptz, blocking boolean NOT NULL DEFAULT false, clock_id uuid, status text NOT NULL);
CREATE TABLE core.reports (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, kind text NOT NULL, period daterange, params jsonb NOT NULL,
  document_id uuid, generated_at timestamptz, CHECK (kind NOT LIKE 'posh%'));   -- POSH annual reports only in posh_sealed.annual_reports
```

### F.4.14 Telecom calling compliance (M-05) and pre-suit mediation (M-06)

Implements master NN-12 (M-05: Equator places automated/AI calls itself) and M-06 (s.12A PIMS stays with the Legal Services Authority until four gates close). P07 consumes the telecom tables (`core.call_records.from_number_id` references `core.number_inventory`); P08 (COM) consumes `com.pims_referrals`.

```sql
CREATE TABLE ops.telecom_declarations (              -- Equator's own DLT/operator filings and evidence (NN-12(a),(c))
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  kind text NOT NULL CHECK (kind IN ('dlt_principal_entity','telemarketer_linkage','header','consent_template','a2p_cli_declaration',
    'operator_written_confirmation','telecom_counsel_opinion','series_1601_application','cnap_registration')),
  operator text NOT NULL,                             -- originating access provider, or 'all'
  cpaas_provider text CHECK (cpaas_provider IS NULL OR cpaas_provider IN ('exotel','plivo')),
  dlt_entity_ref text, reference text, purpose text NOT NULL,
  cli_range_start text, cli_range_end text,           -- E.164; required for a2p_cli_declaration
  number_type text CHECK (number_type IS NULL OR number_type IN ('DID','TOLLFREE','1601')),   -- never 140-series or personal mobiles
  document_id uuid NOT NULL,                          -- filing, acknowledgement, confirmation letter or opinion (ledgered)
  valid_from date NOT NULL, valid_to date,
  status text NOT NULL CHECK (status IN ('draft','filed','acknowledged','valid','expired','withdrawn','rejected')),
  recorded_by uuid NOT NULL, approved_by uuid,
  CHECK (kind <> 'a2p_cli_declaration' OR (cli_range_start IS NOT NULL AND cli_range_end IS NOT NULL AND number_type IS NOT NULL)),
  CHECK (approved_by IS NULL OR approved_by <> recorded_by),
  CHECK (valid_to IS NULL OR valid_to >= valid_from));

CREATE TABLE core.number_inventory (                  -- every calling-line identity the platform may present
  id uuid PRIMARY KEY DEFAULT uuidv7(),
  msisdn_e164 text NOT NULL UNIQUE CHECK (msisdn_e164 ~ '^\+[1-9][0-9]{6,14}$'),
  series text NOT NULL CHECK (series IN ('1600','1601','DID','TOLLFREE','INTL')),   -- 140-series and personal mobiles are never inventoried
  owner_kind text NOT NULL CHECK (owner_kind IN ('equator','tenant')), owner_tenant_id uuid REFERENCES core.tenants(id),
  telephony_provider text NOT NULL, a2p_declaration_id uuid REFERENCES ops.telecom_declarations(id),
  status text NOT NULL CHECK (status IN ('provisioning','active','suspended','released')),
  CHECK ((owner_kind = 'tenant') = (owner_tenant_id IS NOT NULL)),
  CHECK (series <> '1600' OR owner_kind = 'tenant'),   -- 1600 = RBI/SEBI/IRDAI/PFRDA-regulated entities and Government (TRAI PR 91/2026)
  CHECK (status <> 'active' OR owner_kind = 'tenant' OR series = 'INTL' OR a2p_declaration_id IS NOT NULL));   -- Equator CLIs declared as A2P ranges

CREATE TABLE core.number_authorisations (            -- lender-number mode: tenant's written authorisation to present its 1600 number (NN-12(b))
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  number_id uuid NOT NULL REFERENCES core.number_inventory(id),
  regulator text NOT NULL CHECK (regulator IN ('RBI','SEBI','IRDAI','PFRDA')),
  tenant_dlt_pe_ref text NOT NULL, equator_tm_linkage_ref text NOT NULL,     -- Equator's CPaaS linked as telemarketer on the tenant's PE
  a2p_declared_by_tenant boolean NOT NULL DEFAULT false,                     -- required before AI/automated calls (TCCCPR Third Amendment 2026, reg 4)
  purposes text[] NOT NULL CHECK (purposes <@ ARRAY['case_notices','hearing_logistics','payment_reminders','ots_offer_relay','grm_callbacks']),
  verticals core.vertical_code[] NOT NULL CHECK (verticals <@ ARRAY['FIN','INS','SEC']::core.vertical_code[]),
  authorisation_document_id uuid NOT NULL, signed_by_signatory_id uuid NOT NULL REFERENCES core.org_signatories(id),
  valid_from date NOT NULL, valid_to date NOT NULL, revoked_at timestamptz, approved_by uuid,
  status text NOT NULL CHECK (status IN ('pending_review','active','expired','revoked')),
  CHECK (valid_to > valid_from), CHECK (status <> 'active' OR approved_by IS NOT NULL));
SELECT rls.enable_tenant_rls('core','number_authorisations');
-- Trigger: number_id must be a core.number_inventory row with series '1600', owner_kind 'tenant' and owner_tenant_id = tenant_id.

CREATE TABLE core.telecom_consent_registrations (    -- explicit consent registered on the operator consent platform (NN-12(d))
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL REFERENCES core.tenants(id),
  consent_record_id uuid NOT NULL REFERENCES core.consent_records(id), contact_point_id uuid NOT NULL REFERENCES core.contact_points(id),
  operator text NOT NULL, purpose_code text NOT NULL, registration_ref text,
  registered_at timestamptz, expires_at timestamptz, revoked_at timestamptz,
  status text NOT NULL CHECK (status IN ('pending','registered','rejected','expired','revoked')),
  UNIQUE (consent_record_id, operator));
SELECT rls.enable_tenant_rls('core','telecom_consent_registrations');
ALTER TABLE core.contact_points ADD COLUMN dnd_checked_at timestamptz;   -- refreshed before every automated campaign

-- CLI guard (Contact Policy Engine at schedule and dispatch time + trigger on core.communications for channel 'voice'):
-- an automated/AI call may be queued only if the from-number is (a) a tenant 1600 number with an 'active' core.number_authorisations row
-- covering the case's tenant, vertical and purpose (and a2p_declared_by_tenant = true for AI/automated calls), or (b) an Equator number
-- with status 'active' and a valid A2P declaration while flag voice.equator_service_number.enabled is ON → else CLI_NOT_AUTHORISED.
-- Explicit-consent service calls to a DND-blocked number need a 'registered' consent registration → else TELECOM_CONSENT_NOT_REGISTERED.

CREATE TABLE com.pims_referrals (                    -- Commercial Courts Act s.12A PIMS: conducted by the Legal Services Authority (M-06)
  id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  conducted_by text NOT NULL DEFAULT 'legal_services_authority'
    CHECK (conducted_by IN ('legal_services_authority','equator_authorised_msp')),
  authority_name text NOT NULL,                        -- Authority under the PIMS Rules 2018 (G.S.R. 606(E), 3 Jul 2018), e.g. 'DLSA Jaipur'
  form1_document_id uuid NOT NULL,                     -- Form-1 application pack prepared by Equator and filed by the party
  filed_on date, authority_ref text,
  outcome text NOT NULL DEFAULT 'pending'
    CHECK (outcome IN ('pending','settled_form4','non_starter_form3','failed_form5','withdrawn')),
  outcome_document_id uuid, outcome_on date,
  parallel_voluntary_proceeding_id uuid REFERENCES core.proceedings(id),   -- voluntary contractual mediation only where lawful
  ruleset_version_id uuid NOT NULL,
  CHECK (outcome = 'pending' OR outcome = 'withdrawn' OR outcome_document_id IS NOT NULL));
SELECT rls.enable_case_rls('com','pims_referrals');
-- Guard: conducted_by = 'equator_authorised_msp' is rejected (rule COM_PIMS_CERT_NOT_ISSUABLE → MECHANISM_NOT_PERMITTED_FOR_VERTICAL) unless the
-- pinned ruleset has flag com.s12a_equator_authorised ON and all four gate rules IN_FORCE with verification = verified. While the flag is OFF, no Equator document may
-- state or imply that an Equator report satisfies s.12A (copy lint, NN-17).
```

**Feature flags introduced by M-05/M-06** (seeded OFF; turning ON is a maker–checker configuration change by an authorised legal admin that the config validator rejects unless the gate evidence below is recorded):

| Flag | Default | Gate evidence required to turn ON | NN tests (Appendix I) |
|---|---|---|---|
| `voice.equator_service_number.enabled` | OFF | `ops.telecom_declarations` rows with status `valid` for `dlt_principal_entity`, an `a2p_cli_declaration` covering every Equator number to be used, the originating operator's `operator_written_confirmation` of the permitted number type and a `telecom_counsel_opinion` | `NN-12_equator_did_requires_flag_and_evidence`, `NN-12_flag_on_requires_gate_evidence` |
| `com.s12a_equator_authorised` | OFF | Legal Rules Register entries IN_FORCE and verified, each with its notification reference: (1) Mediation Act Ninth Schedule notified (substituted s.12A); (2) MCI regulations in force and Equator recognised as a mediation service provider (s.40); (3) Central Government notification naming Equator under new s.12A(2)(ii); (4) rules replacing the PIMS Rules 2018 | `NN-05_s12a_flag_requires_four_gates`, `NN-17_s12a_claim_blocked` |

---

## F.5 Audit schema (P00 canonical; summary and partitioning)

```sql
-- audit.audit_events: PRIMARY KEY (occurred_at, id) — includes partition key (F.1.5); PARTITION BY RANGE (occurred_at), monthly;
-- chain per tenant (chain_id = tenant_id; platform chain = zero UUID); writer audit.append_event(jsonb) serialises via chain_heads row lock;
-- per-chain seq uniqueness cannot be a UNIQUE constraint across partitions without occurred_at, so it is guaranteed by the writer and
-- verified by audit.verification_runs (gap/duplicate detection) — RB-10 on failure.
CREATE TABLE audit.access_log (id uuid NOT NULL DEFAULT uuidv7(), accessed_at timestamptz NOT NULL, tenant_id uuid, user_id uuid,
  resource_type text NOT NULL, resource_id text NOT NULL, tier text NOT NULL, purpose text NOT NULL, decision text NOT NULL CHECK (decision IN ('allow','deny')),
  policy_version text NOT NULL, prev_hash char(64) NOT NULL, row_hash char(64) NOT NULL,
  PRIMARY KEY (accessed_at, id)) PARTITION BY RANGE (accessed_at);
CREATE TABLE audit.break_glass_events (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, user_id uuid NOT NULL, role_grant_id uuid NOT NULL,
  justification text NOT NULL CHECK (length(justification) >= 30), dpo_notified_at timestamptz NOT NULL, reviewed_by uuid, review_outcome text);
-- All three: REVOKE UPDATE, DELETE; trigger core.deny_mutation(); partitions exported to S3 Object Lock before detach.
```

## F.6 GRM schema (P09 canonical for grm.tickets)

```sql
CREATE TABLE grm.desks (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, variant text NOT NULL, name text NOT NULL,
  gro_user_ids uuid[] NOT NULL, io_user_ids uuid[] NOT NULL DEFAULT '{}', sla_policy_id uuid NOT NULL, public_intake_slug text UNIQUE);
CREATE TABLE grm.sla_policies (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid, variant text NOT NULL, version int NOT NULL,
  ack_hours int NOT NULL, resolve_days int NOT NULL, escalation_rules jsonb NOT NULL, legal_rule_ids uuid[] NOT NULL,
  CHECK (variant <> 'FIN_RBI' OR resolve_days <= 30));                       -- RBI 30-day RE window cannot be lengthened (NN-04)
CREATE TABLE grm.ticket_events (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, ticket_id uuid NOT NULL REFERENCES grm.tickets(id),
  event text NOT NULL, actor_id uuid, payload jsonb NOT NULL, occurred_at timestamptz NOT NULL DEFAULT now());
CREATE TABLE grm.escalations (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, ticket_id uuid NOT NULL REFERENCES grm.tickets(id),
  to_kind text NOT NULL CHECK (to_kind IN ('internal_ombudsman','equator_odr','external_forum')), consent_record_id uuid, case_id uuid,
  forum_code text, escalated_at timestamptz NOT NULL, CHECK (to_kind <> 'equator_odr' OR consent_record_id IS NOT NULL));   -- CONSENT_REQUIRED
CREATE TABLE grm.regulatory_reports (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, variant text NOT NULL, period daterange NOT NULL,
  format text NOT NULL, document_id uuid, submitted_at timestamptz, UNIQUE (tenant_id, variant, period));
```

## F.7 Sealed stores (NN-07): pattern and POSH DDL

**Pattern.** (1) Separate schema with its own DB role and connection pool; `eq_app` has no `USAGE`. (2) Separate KMS CMK per schema; payload fields envelope-encrypted. (3) Core stores only an **opaque token** — `pt_` (POSH), `ht_` (health), `st_` (safety) + 26 base32 chars generated by the sealed service; no FK in either direction; the token→row map exists only inside the sealed schema. (4) Every read writes `audit.access_log` with purpose (via sealed service call). (5) Sealed schemas are excluded from OpenSearch, analytics replicas, AI retrieval, webhooks and exports (CI scan fails on any reference outside the sealed module). (6) Retention per class (POSH 7 y default).

```sql
CREATE TABLE posh_sealed.ic_constitutions (id uuid PRIMARY KEY DEFAULT uuidv7(), employer_tenant_id uuid NOT NULL,   -- not an FK
  establishment_name_enc bytea NOT NULL, constituted_on date NOT NULL, order_document_ref text NOT NULL, valid_to date,
  member_count int NOT NULL CHECK (member_count >= 4), women_members int NOT NULL, external_member_present boolean NOT NULL,
  CHECK (women_members * 2 >= member_count),                                  -- at least one-half women (NN-07; POSH Act 2013 s.4)
  CHECK (external_member_present));
CREATE TABLE posh_sealed.ic_members (id uuid PRIMARY KEY DEFAULT uuidv7(), ic_constitution_id uuid NOT NULL REFERENCES posh_sealed.ic_constitutions(id),
  member_role text NOT NULL CHECK (member_role IN ('presiding_officer','employee_member','external_member')), user_ref text NOT NULL,   -- sealed_ref from core.memberships
  is_woman boolean NOT NULL, tenure tstzrange NOT NULL, conflict_declarations_enc bytea);
-- posh_sealed.complaints and posh_sealed.conciliations: canonical in P09 (opaque_token UNIQUE; inquiry_due_on = inquiry_clock_start + 90,
-- inquiry_clock_start defaulting to complaint receipt — s.11(4) start point open with counsel;
-- conciliations CHECK requested_by_aggrieved AND monetary_basis = false — POSH Act 2013 s.10(1) proviso).
CREATE TABLE posh_sealed.inquiry_events (id uuid PRIMARY KEY DEFAULT uuidv7(), complaint_id uuid NOT NULL REFERENCES posh_sealed.complaints(id),
  event text NOT NULL, payload_enc bytea NOT NULL, actor_ref text NOT NULL, occurred_at timestamptz NOT NULL, prev_hash char(64) NOT NULL, row_hash char(64) NOT NULL);
CREATE TABLE posh_sealed.reports (id uuid PRIMARY KEY DEFAULT uuidv7(), complaint_id uuid NOT NULL REFERENCES posh_sealed.complaints(id),
  finding text NOT NULL CHECK (finding IN ('proved','not_proved','malicious_or_false','withdrawn')), issued_on date NOT NULL,
  employer_action_due_on date GENERATED ALWAYS AS (issued_on + 60) STORED, appeal_window_ends date GENERATED ALWAYS AS (issued_on + 90) STORED,
  document_cipher bytea NOT NULL);
CREATE TABLE posh_sealed.annual_reports (id uuid PRIMARY KEY DEFAULT uuidv7(), ic_constitution_id uuid NOT NULL REFERENCES posh_sealed.ic_constitutions(id),
  year int NOT NULL, received int NOT NULL, disposed int NOT NULL, pending_over_90d int NOT NULL, workshops int NOT NULL,
  filed_with_district_officer_on date, UNIQUE (ic_constitution_id, year));
CREATE TABLE health_sealed.medical_records (id uuid PRIMARY KEY DEFAULT uuidv7(), token text NOT NULL UNIQUE CHECK (token ~ '^ht_[a-z2-7]{26}$'),
  case_token_ref text NOT NULL, record_kind text NOT NULL, document_cipher bytea NOT NULL, authority_ref text NOT NULL, erase_after date NOT NULL);
CREATE TABLE safety_sealed.screenings (id uuid PRIMARY KEY DEFAULT uuidv7(), token text NOT NULL UNIQUE CHECK (token ~ '^st_[a-z2-7]{26}$'),
  case_token_ref text NOT NULL, party_token_ref text NOT NULL,
  outcome text NOT NULL CHECK (outcome IN ('suitable','suitable_with_safeguards','shuttle_only','not_suitable_safety')),
  safeguards_enc bytea, screened_by_ref text NOT NULL, screened_at timestamptz NOT NULL, next_due_at timestamptz);
-- core.cases.safety_flag is set by the sealed service via a narrow SECURITY DEFINER function when outcome ∈ ('shuttle_only','not_suitable_safety').
```

## F.8 Vertical extension tables (1:1 or 1:N with `core.cases`; tenant RLS + case RLS)

```sql
CREATE TABLE fin.loan_accounts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  lender_org_id uuid NOT NULL REFERENCES core.organisations(id), lender_type text NOT NULL CHECK (lender_type IN ('bank','nbfc','hfc','mfi','fintech_lsp','arc','p2p','card_issuer')),
  loan_type text NOT NULL CHECK (loan_type IN ('personal','vehicle','home','gold','education','business_msme','credit_card','bnpl','microfinance','p2p')),
  loan_account_masked text NOT NULL, loan_account_hmac char(64) NOT NULL, sanction_date date, sanctioned_minor bigint,
  principal_outstanding_minor bigint, interest_outstanding_minor bigint, penal_charges_minor bigint, other_charges_minor bigint,
  dpd int, npa_date date, secured boolean NOT NULL, security_description_enc bytea, sarfaesi_action_status text,
  lsp_org_id uuid, clause_instance_id uuid, arbitration_clause_at_origination boolean NOT NULL DEFAULT false,
  currency core.currency_code NOT NULL DEFAULT 'INR' CHECK (currency = 'INR'), UNIQUE (case_id, loan_account_hmac));
CREATE TABLE fin.ots_proposals (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  loan_account_id uuid NOT NULL REFERENCES fin.loan_accounts(id), proposed_by text NOT NULL CHECK (proposed_by IN ('borrower','lender','neutral_option')),
  total_outstanding_minor bigint NOT NULL, ots_amount_minor bigint NOT NULL CHECK (ots_amount_minor > 0), upfront_minor bigint NOT NULL DEFAULT 0,
  instalments int NOT NULL DEFAULT 0, interest_waiver_minor bigint NOT NULL DEFAULT 0, penal_waiver_minor bigint NOT NULL DEFAULT 0,
  bureau_reporting text NOT NULL CHECK (bureau_reporting IN ('settled','closed','as_per_policy')), noc_on_final boolean NOT NULL DEFAULT true,
  approver_signatory_id uuid REFERENCES core.org_signatories(id),
  cooling_period_months int CHECK (cooling_period_months IS NULL OR cooling_period_months >= 12),   -- RBI (NBFC – Resolution of Stressed Assets) Directions 2025 para 95: Board-set, floor 12 months (ex-RBI/2023-24/40)
  calculator_version text NOT NULL, indicative boolean NOT NULL DEFAULT true, status text NOT NULL,
  CHECK (ots_amount_minor <= total_outstanding_minor), CHECK (upfront_minor <= ots_amount_minor));
CREATE TABLE ins.policies (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  insurer_org_id uuid NOT NULL REFERENCES core.organisations(id), policy_no_masked text NOT NULL, policy_no_hmac char(64) NOT NULL,
  policy_class text NOT NULL CHECK (policy_class IN ('retail','commercial','group_member','group_master')),
  line_of_business text NOT NULL, sum_insured_minor bigint, inception_date date, first_ever_inception date, sales_channel text,
  legacy_arbitration_clause boolean NOT NULL DEFAULT false,
  is_retail boolean GENERATED ALWAYS AS (policy_class IN ('retail','group_member')) STORED);            -- drives INS_RETAIL_ARBITRATION_BLOCKED
CREATE TABLE ins.claims (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  policy_id uuid NOT NULL REFERENCES ins.policies(id), claim_no_masked text NOT NULL, intimated_on date NOT NULL, decision_on date,
  claimed_minor bigint NOT NULL, offered_minor bigint, decision text CHECK (decision IN ('pending','repudiated','partially_settled','settled','closed_no_claim')),
  repudiation_grounds text[] NOT NULL DEFAULT '{}', representation_date date, insurer_reply_date date, fraud_alleged boolean NOT NULL DEFAULT false,
  health_data_token text, bima_bharosa_token text,
  CHECK (offered_minor IS NULL OR offered_minor <= claimed_minor), CHECK (decision_on IS NULL OR decision_on >= intimated_on));
CREATE TABLE com.contracts (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  title text NOT NULL, contract_type text NOT NULL, executed_on date, value_minor bigint, currency core.currency_code NOT NULL DEFAULT 'INR',
  has_arbitration_clause boolean NOT NULL, has_mediation_precondition boolean NOT NULL DEFAULT false, clause_text_document_id uuid,
  seat_city text, governing_law text, panel_size smallint CHECK (panel_size IN (1,3)), specified_value_commercial boolean,
  s12a_status text CHECK (s12a_status IN ('not_applicable','required','in_progress','settled','non_starter','failed','exempt_urgent_interim')),   -- mirrors the Authority's PIMS outcome (com.pims_referrals, M-06)
  msme_supplier boolean NOT NULL DEFAULT false, udyam_no text, msefc_reference_status text,
  CHECK (NOT msme_supplier OR udyam_no IS NOT NULL));
-- COM guard: arbitration proceeding requires has_arbitration_clause or a post-dispute submission agreement (COM_NO_ARB_AGREEMENT).
CREATE TABLE fam.family_members (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  person_id uuid REFERENCES core.persons(id), case_party_id uuid REFERENCES core.case_parties(id),
  relationship text NOT NULL CHECK (relationship IN ('spouse','child','parent','sibling','coparcener','karta','heir','widow','grandchild','other')),
  is_minor boolean NOT NULL, initials_only text, age_years smallint CHECK (age_years BETWEEN 0 AND 120), joined_as_party boolean NOT NULL,
  share_claimed numeric(9,6) CHECK (share_claimed BETWEEN 0 AND 1), guardian_person_id uuid,
  CHECK (NOT is_minor OR (person_id IS NULL AND initials_only IS NOT NULL)),          -- minors: initials and age only (DPDP s.9)
  CHECK (NOT is_minor OR guardian_person_id IS NOT NULL));
CREATE TABLE fam.estate_assets (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  asset_kind text NOT NULL CHECK (asset_kind IN ('immovable_residential','immovable_agricultural','immovable_commercial','bank_deposit','securities',
    'business_interest','jewellery_streedhan','vehicle','huf_property','other_movable')),
  description_enc bytea NOT NULL, state_code char(2), survey_or_property_ref_enc bytea, title_holder text,
  agreed_value_minor bigint, valuation_source text CHECK (valuation_source IN ('party_agreed','registered_valuer','circle_rate','none')),
  disputed boolean NOT NULL DEFAULT true, is_immovable boolean GENERATED ALWAYS AS (asset_kind LIKE 'immovable%' OR asset_kind = 'huf_property') STORED);
-- Settlement terms touching an is_immovable asset force instrument_class 'partition_immovable'/'immovable_transfer' → NN-08 physical route.
CREATE TABLE wrk.employment_records (id uuid PRIMARY KEY DEFAULT uuidv7(), tenant_id uuid NOT NULL, case_id uuid NOT NULL REFERENCES core.cases(id),
  employer_org_id uuid NOT NULL REFERENCES core.organisations(id), employee_case_party_id uuid NOT NULL REFERENCES core.case_parties(id),
  designation text, is_workman boolean, engagement text NOT NULL CHECK (engagement IN ('permanent','fixed_term','contract','gig','apprentice','founder')),
  joined_on date, separated_on date, separation_mode text, monthly_wages_minor bigint, ctc_monthly_minor bigint,
  wages_pct_of_ctc numeric(5,2) GENERATED ALWAYS AS (CASE WHEN ctc_monthly_minor > 0 THEN round(100.0 * monthly_wages_minor / ctc_monthly_minor, 2) END) STORED,
  completed_years numeric(5,2), gratuity_eligible boolean, establishment_size text CHECK (establishment_size IN ('lt_10','10_19','20_49','50_99','100_299','300_plus','unknown'))  -- v2: 20-worker break = IR Code GRC threshold (X-40; V5 R3));
-- WRK guard: arbitration proceeding blocked when is_workman IS DISTINCT FROM false (WRK_WORKMAN_ARBITRATION_BLOCKED); settlements cannot waive statutory dues.
CREATE TABLE intl.case_international (case_id uuid PRIMARY KEY REFERENCES core.cases(id), tenant_id uuid NOT NULL,
  ica_flag boolean NOT NULL, intl_mediation_flag boolean NOT NULL, seat_country char(2) NOT NULL, seat_city text, seat_is_ifsc boolean NOT NULL DEFAULT false,
  lex_arbitri text, law_of_agreement text, governing_law text, cisg_applicable boolean, incoterm jsonb, instrument_type text
    CHECK (instrument_type IN ('UCP600','ISP98','URDG758','none')), languages text[] NOT NULL, interpretation_required boolean NOT NULL DEFAULT false,
  enforcement_targets jsonb NOT NULL DEFAULT '[]',          -- [{country, nyc_party, india_notified_s44, singapore_conv_party, apostille_member}]
  sanctions_status text NOT NULL CHECK (sanctions_status IN ('not_screened','clear','potential_match','confirmed_hit','cleared_after_review')),
  sanctions_screened_at timestamptz, sanctions_reviewer uuid, kyc_ubo_status text NOT NULL, dpdp_transfer_basis text, gdpr_basis text,
  fema_route text CHECK (fema_route IN ('current','capital','not_applicable')), currency core.currency_code NOT NULL,
  tax_treatment text CHECK (tax_treatment IN ('export_lut','rcm','fwd','ifsc')), tpf_disclosed boolean, ai_protocol text CHECK (ai_protocol IN ('CIArb','SVAMC','none')),
  ea_requested boolean NOT NULL DEFAULT false, appellate_review_optin boolean NOT NULL DEFAULT false, presiding_nationality_neutral boolean NOT NULL DEFAULT true,
  CHECK (ica_flag OR intl_mediation_flag));
-- NN-19 registration guard (trigger on core.cases state → 'accepted' for vertical INT): requires sanctions_status IN ('clear','cleared_after_review'),
-- kyc_ubo_status='verified', dpdp_transfer_basis NOT NULL, fema_route NOT NULL → else SANCTIONS_HIT_REVIEW / INT_KYC_UBO_INCOMPLETE / DPDP_TRANSFER_BASIS_MISSING.
```

Retention: vertical rows inherit `core.cases.retain_until` (case record); `fam.family_members` rows for minors are erased with the case (C3 §3.8). Partitioning: only `audit.audit_events`, `audit.access_log`, `core.communications`, `core.webhook_deliveries`, `ops.telemetry_events` (all monthly). High-volume candidates kept unpartitioned until > 200 M rows: `core.case_status_history`, `core.service_attempts`, `core.clock_alerts`.

---

## F.9 Domain event catalogue

**Envelope (CloudEvents 1.0, JSON)**: `specversion`, `id` (UUIDv7 = outbox row id; consumer dedupe key), `type` (`equator.<context>.<entity>.<verb>.v1`), `source` (`/equator/<module>`), `time`, `subject` (aggregate id), `tenantid`, `caseid` (nullable), `traceparent`, `actor` (`{type, id, role}`), `datacontenttype`, `data`. Ordering: per `caseid` (partition key), else per `subject`. Rules: additive payload changes keep `v1`; breaking changes publish `v2` in parallel for ≥ 90 days. Payloads carry IDs, codes and amounts in minor units — never names, contact data, free text, health, POSH or safety content (NN-07, NN-16). Events marked **W** are subscribable by enterprise webhooks (tenant-filtered); sealed-context events are internal to the sealed service and never leave it. Consumers abbreviations: AUD audit projector · NOT notifications/comms · CLK clocks · BIL billing · RPT reporting/read models · SRCH OpenSearch indexer · WH webhooks · AI AI gateway context · ENT enterprise MIS · TMP Temporal workflow signal.

| # | Event type (`.v1`) | Producer | Key payload | Consumers |
|---|---|---|---|---|
| 1 | `equator.tenancy.tenant.created` | tenancy | tenant_id, kind | AUD, BIL |
| 2 | `equator.tenancy.tenant.status_changed` | tenancy | from, to, reason_code | AUD, BIL, RPT |
| 3 | `equator.tenancy.branding.published` | tenancy | version | web cache |
| 4 | `equator.identity.user.registered` | identity | user_id, kind | AUD, NOT |
| 5 | `equator.identity.membership.granted` | identity | membership_id, role_code | AUD, policy cache |
| 6 | `equator.identity.membership.revoked` | identity | membership_id, reason | AUD, policy cache, TMP |
| 7 | `equator.identity.stepup.completed` | identity | session_id, method, purpose | AUD |
| 8 | `equator.identity.session.revoked` | identity | user_id, scope, reason | AUD, mobile |
| 9 | `equator.identity.break_glass.opened` | identity | grant_id, scope | AUD, NOT (DPO) |
| 10 | `equator.identity.api_key.created` / `.revoked` | identity | key_prefix, env, scopes | AUD, ENT |
| 11 | `equator.mobile.device.registered` | identity | device_id, platform, integrity | AUD, NOT |
| 12 | `equator.mobile.device.integrity_changed` | identity | device_id, from, to | AUD, policy cache |
| 13 | `equator.mobile.device.revoked` / `.wiped` | identity | device_id, reason | AUD |
| 14 | `equator.mobile.screen.capture_detected` | mobile | route_template, tier | AUD |
| 15 | `equator.mobile.deeplink.rejected` | mobile/API | purpose, reason_code | RPT |
| 16 | `equator.consent.consent.given` | consent | person_id, purpose_code, notice_id | AUD, NOT, RPT |
| 17 | `equator.consent.consent.withdrawn` | consent | person_id, purpose_code | AUD, NOT, growth suppression, TMP |
| 18 | `equator.consent.dsr.received` | consent | dsr_id, kind, due_at | CLK, NOT (DPO) |
| 19 | `equator.consent.dsr.fulfilled` | consent | dsr_id, outcome | AUD, RPT |
| 20 | `equator.consent.dsr.breached_sla` | consent | dsr_id | NOT, ops |
| 21 | `equator.kyc.check.completed` | kyc | check_id, method, result | cases, AUD |
| 22 | `equator.kyc.kyb.completed` | kyc | organisation_id, check_type, result | enterprise, AUD |
| 23 | `equator.directory.organisation.created` | directory | organisation_id, org_type | SRCH |
| 24 | `equator.intake.explorer.session_completed` | intake | session_id, vertical, route_code, fallback_used | RPT (no text) |
| 25 | `equator.intake.form.submitted` | forms | submission_id, form_schema_version_id | intake |
| 26 | `equator.cases.case.drafted` | cases | case_id, vertical | RPT |
| 27 | `equator.cases.case.filed` **W** | cases | case_id, vertical, source, mechanism_requested, pinned versions | CLK, NOT, BIL, RPT, SRCH, WH, ENT |
| 28 | `equator.cases.scrutiny.started` | intake | case_id | CLK |
| 29 | `equator.cases.deficiency.raised` **W** | intake | case_id, deficiency_codes, cure_due_at | NOT, CLK, WH |
| 30 | `equator.cases.deficiency.cured` | intake | case_id | CLK |
| 31 | `equator.cases.case.accepted` **W** | intake | case_id, case_number, track | NOT, CLK, BIL, WH |
| 32 | `equator.cases.case.rejected` **W** | intake | case_id, reason_code | NOT, BIL (refund), WH |
| 33 | `equator.cases.case.signposted` **W** | routing | case_id, forum_code, last_date_to_act | NOT, RPT, WH |
| 34 | `equator.routing.route.decided` | routing | case_id, route_code, ruleset_version_id, blocked_routes | intake, AI (tool), RPT |
| 35 | `equator.cases.signposting.delivered` | routing | case_id, forum_code, channel, language | AUD, closure guard |
| 36 | `equator.cases.signposting.acknowledged` | routing | event_id | closure guard |
| 37 | `equator.cases.party.joined` | cases | case_id, case_party_id, role | NOT, SRCH |
| 38 | `equator.cases.respondent.responded` **W** | cases | case_id, counterclaim (bool) | CLK, NOT, BIL, WH |
| 39 | `equator.cases.counsel.mandate_activated` / `_revoked` | cases | case_id, mandate_id | policy cache, NOT |
| 40 | `equator.cases.case.linked` | cases | case_id, linked_case_id, relationship | CLK (shared group), RPT |
| 41 | `equator.cases.case.state_changed` | cases | case_id, from, to, event | RPT, SRCH, ENT |
| 42 | `equator.cases.case.on_hold` / `.resumed` | cases | case_id, reason_code, clock_policy | CLK, NOT |
| 43 | `equator.cases.case.withdrawn` **W** | cases | case_id, by_party_role | CLK (cancel), BIL (refund rules), WH |
| 44 | `equator.cases.case.lapsed` | cases | case_id, legal_basis | NOT, RPT |
| 45 | `equator.cases.case.closed` **W** | cases | case_id, closure_reason | CLK, BIL, RPT, retention, WH |
| 46 | `equator.cases.safety_flag.raised` | sealed safety svc → cases | case_id | hearings (block joint), NOT (case manager) |
| 47 | `equator.cases.non_arbitrable.flagged` | routing | case_id, flags | proceedings, outcomes |
| 48 | `equator.clocks.clock.started` | clocks | clock_id, kind, due_at, owner_role | CLK cockpit, NOT |
| 49 | `equator.clocks.clock.extended` | clocks | clock_id, new_due_at, basis_ref | NOT, AUD |
| 50 | `equator.clocks.clock.suspended` / `.resumed` | clocks | clock_id, reason | NOT |
| 51 | `equator.clocks.clock.alert_fired` | clocks | clock_id, threshold, level | NOT, tasks, RPT |
| 52 | `equator.clocks.clock.satisfied` | clocks | clock_id | RPT |
| 53 | `equator.clocks.clock.breached` | clocks | clock_id, kind, breach_behaviour | ops (Sev-1), NOT, RPT |
| 54 | `equator.clocks.clock.owner_missing` | clocks | clock_id | tasks, closure guard |
| 55 | `equator.notices.notice.approved` | notices | notice_id, case_id, notice_type | comms |
| 56 | `equator.notices.service.attempted` | notices | notice_id, channel, result | CLK, RPT |
| 57 | `equator.notices.notice.served` **W** | notices | notice_id, served_at, method | CLK, cases, WH |
| 58 | `equator.notices.notice.deemed_served` **W** | notices | notice_id, rule_ref | CLK, cases, WH |
| 59 | `equator.notices.service.failed` | notices | notice_id, exhausted_channels | tasks |
| 60 | `equator.documents.document.uploaded` | documents | document_id, case_id, kind, sha256 | SRCH (non-sealed), AI (extractor, opt-in), ledger |
| 61 | `equator.documents.upload.completed` / `.quarantined` | documents | upload_id, reason_code | NOT, AUD |
| 62 | `equator.documents.evidence.admitted` / `.rejected` | proceedings | document_id, by_neutral | ledger, RPT |
| 63 | `equator.documents.bundle.certified` | documents | bundle_id, manifest_sha256 | execution, AUD |
| 64 | `equator.documents.legal_hold.set` / `.released` | documents | scope, reason_code | retention |
| 65 | `equator.neutrals.application.submitted` | neutrals | application_id | panel tasks |
| 66 | `equator.neutrals.neutral.empanelled` | neutrals | neutral_id, types, grade | SRCH (directory), RPT |
| 67 | `equator.neutrals.neutral.suspended` / `.de_empanelled` | neutrals | neutral_id, reason_code | allocation, policy cache |
| 68 | `equator.neutrals.disclosure.submitted` | neutrals | disclosure_id, seventh_schedule_hits_count | appointments |
| 69 | `equator.neutrals.allocation.run_completed` | neutrals | allocation_run_id, method, outcome, seed_commitment | AUD, Independence Evidence Pack |
| 70 | `equator.neutrals.appointment.offered` | neutrals | appointment_id, seat, expires_at | NOT |
| 71 | `equator.neutrals.appointment.declined` / `.expired` | neutrals | appointment_id, reason_code | allocation (re-run) |
| 72 | `equator.neutrals.appointment.confirmed` **W** | neutrals | appointment_id, case_id, seat | cases, CLK, NOT, BIL, WH |
| 73 | `equator.neutrals.challenge.filed` / `.decided` | neutrals | challenge_id, outcome | CLK, NOT |
| 74 | `equator.neutrals.waiver_s12_5.executed` | neutrals | case_id, case_party_id, esign_request_id | Independence Evidence Pack |
| 75 | `equator.neutrals.availability.changed` | neutrals | neutral_id, range | scheduling |
| 76 | `equator.proceedings.proceeding.commenced` | proceedings | proceeding_id, mechanism, statutory_mode | CLK (s.29A/s.18), NOT |
| 77 | `equator.proceedings.tribunal.constituted` | proceedings | proceeding_id, size | CLK |
| 78 | `equator.proceedings.pleadings.completed` | proceedings | proceeding_id, at | CLK (s.29A start) |
| 79 | `equator.proceedings.proceeding.state_changed` | proceedings | proceeding_id, from, to | cases (derive state), RPT |
| 80 | `equator.proceedings.mandate.extended` | proceedings | proceeding_id, basis (consent/court), new_due_at | CLK |
| 81 | `equator.proceedings.mandate.terminated` | proceedings | proceeding_id, legal_basis | cases (lapsed) |
| 82 | `equator.proceedings.order.issued` **W** | proceedings | order_id, kind | NOT, CLK, WH |
| 83 | `equator.proceedings.offer.submitted` | proceedings | offer_id, kind, amount_minor (not for blind) | NOT, ENT approval |
| 84 | `equator.proceedings.offer.accepted` / `.rejected` / `.expired` | proceedings | offer_id | outcomes, NOT |
| 85 | `equator.proceedings.blind_bid.crossed` | proceedings | proceeding_id, midpoint_minor | outcomes |
| 86 | `equator.proceedings.consent.recorded` | proceedings | consent_kind (recording, same-neutral med-arb, s.12(5)) | AUD |
| 87 | `equator.proceedings.med_arb.switched` | proceedings | proceeding_id, same_neutral (bool) | allocation, NOT |
| 88 | `equator.hearings.session.scheduled` **W** | hearings | session_id, start, mode | NOT, CLK, calendar, WH |
| 89 | `equator.hearings.session.rescheduled` / `.cancelled` | hearings | session_id, reason_code | NOT |
| 90 | `equator.hearings.session.started` / `.ended` | hearings | session_id | BIL (per-session), RPT |
| 91 | `equator.hearings.participant.joined` / `.left` | hearings | session_id, role, mode | attendance |
| 92 | `equator.hearings.participant.moved_to_caucus` | hearings | session_id, room_kind | AUD |
| 93 | `equator.hearings.recording.started` / `.stopped` | hearings | session_id, consent_refs | AUD |
| 94 | `equator.hearings.session.low_bandwidth_entered` | hearings | session_id, net_class | RPT |
| 95 | `equator.outcomes.settlement.drafted` | outcomes | settlement_id, instrument_class | lint, NOT |
| 96 | `equator.outcomes.settlement.lint_failed` | outcomes | settlement_id, rule_codes | tasks |
| 97 | `equator.outcomes.settlement.executed` **W** | outcomes | settlement_id, execution_route | compliance, BIL, WH |
| 98 | `equator.outcomes.award.drafted` | outcomes | award_id, ai_assisted | maker–checker |
| 99 | `equator.outcomes.award.signed` **W** | outcomes | award_id, signed_at | estamp, CLK (s.34), BIL, WH |
| 100 | `equator.outcomes.award.sealed` / `.released` | outcomes | award_id, sealed_hash | arb-med workflow |
| 101 | `equator.outcomes.award.corrected` | outcomes | award_id, s33_kind | NOT |
| 102 | `equator.outcomes.appeal.filed` / `.decided` | outcomes | appeal_id | CLK, NOT |
| 103 | `equator.outcomes.challenge.recorded` **W** | execution | case_id, forum, provision (s.34/s.28/s.37) | cases (challenged), WH |
| 104 | `equator.esign.request.sent` | esign | esign_request_id, signers_count | NOT |
| 105 | `equator.esign.signer.signed` | esign | esign_request_id, seq | outcomes |
| 106 | `equator.esign.request.completed` / `.failed` | esign | esign_request_id, status | outcomes, AUD |
| 107 | `equator.esign.request.mobile_launched` | esign | esign_request_id | AUD |
| 108 | `equator.estamp.request.completed` / `.failed` | estamp | estamp_request_id, certificate_no | outcomes, CLK |
| 109 | `equator.execution.registration.booked` / `.completed` | execution | registration_task_id | outcomes, CLK |
| 110 | `equator.execution.pack.generated` **W** | execution | execution_pack_id, route | NOT, WH |
| 111 | `equator.execution.obligation.due` / `.verified` / `.defaulted` **W** | execution | obligation_id, obligation_type | NOT, escalation, WH |
| 112 | `equator.billing.quote.issued` | billing | quote_id, total_minor, currency | NOT |
| 113 | `equator.billing.invoice.issued` **W** | billing | invoice_id, total_minor, currency | NOT, payments, WH |
| 114 | `equator.billing.invoice.paid` **W** | billing | invoice_id | cases (fee_status), WH |
| 115 | `equator.billing.credit_note.issued` | billing | invoice_id, amount_minor | finance |
| 116 | `equator.payments.intent.created` | payments | payment_id, method_class | RPT |
| 117 | `equator.payments.payment.captured` | payments | payment_id, invoice_id, amount_minor | billing, ledger |
| 118 | `equator.payments.payment.failed` | payments | payment_id, reason_code | NOT |
| 119 | `equator.payments.refund.issued` | payments | refund_id, amount_minor | NOT, ledger |
| 120 | `equator.payments.payout.sent` / `.failed` | payments | payout_id, net_minor, tds_minor | NOT, ledger |
| 121 | `equator.payments.reconciliation.break_detected` | payments | date, break_type, amount_minor | ops (RB-08) |
| 122 | `equator.escrow.account.funded` **W** | escrow | escrow_account_id, amount_minor | compliance, NOT, WH |
| 123 | `equator.escrow.milestone.evidence_submitted` / `.objected` | escrow | milestone_id | NOT, tasks |
| 124 | `equator.escrow.milestone.released` **W** | escrow | milestone_id, amount_minor | compliance, NOT, WH |
| 125 | `equator.escrow.instalment.missed` **W** | escrow | plan_id, seq | execution (default rule), NOT, WH |
| 126 | `equator.billing.fx.snapshot_taken` | billing | fx_rate_id, pair, source | — |
| 127 | `equator.comms.message.queued` / `.sent` / `.delivered` / `.failed` | comms | communication_id, channel, purpose_code | notices, RPT |
| 128 | `equator.comms.message.blocked_by_policy` | comms | communication_id, policy_code (NN-12 window, blackout, consent) | ops dashboard |
| 129 | `equator.comms.blackout.started` / `.ended` | comms | person_id, kind | journeys |
| 130 | `equator.voice.call.completed` | voice | call_record_id, outcome, recovery_related | notices, RPT |
| 131 | `equator.voice.campaign.paused` | voice | campaign_id, reason_code | ops (RB-07) |
| 132 | `equator.notifications.push.undelivered` | notifications | notification_id | comms fallback |
| 133 | `equator.messaging.message.posted` / `.retracted` | cases | thread_id, message_id | realtime, NOT |
| 134 | `equator.rules.config_change.submitted` / `.approved` / `.applied` | rules | change_id, object_type, version | AUD, caches |
| 135 | `equator.rules.legal_rule.status_changed` | rules | legal_rule_id, from, to | feature flags (OFF if UNVERIFIED) |
| 136 | `equator.rules.ruleset.version_activated` | rules | ruleset_version_id, effective_from | routing cache |
| 137 | `equator.ai.interaction.completed` | ai | interaction_id, agent, prompt_version, guardrail_flags | AUD, RPT |
| 138 | `equator.ai.guardrail.blocked` | ai | interaction_id, gx_code | ops, eval datasets (synthetic only) |
| 139 | `equator.ai.draft.human_approved` / `.rejected` | ai | suggestion_id, by_role | AUD |
| 140 | `equator.ai.feature.kill_switched` | ai | agent, tenant_id | ops |
| 141 | `equator.enterprise.bulk_job.validated` / `.committed` **W** | enterprise | bulk_job_id, accepted, deficient, rejected | ENT, WH |
| 142 | `equator.enterprise.clause_instance.issued` / `.accepted` **W** / `.revoked` **W** | enterprise | clause_instance_id, verification_code, status | ENT, WH |
| 143 | `equator.grm.ticket.created` **W** / `.acknowledged` | grm | ticket_id, variant, category | CLK, NOT, WH |
| 144 | `equator.grm.ticket.io_routed` / `.final_reply_sent` | grm | ticket_id, outcome | CLK, RPT |
| 145 | `equator.grm.ticket.escalated_to_odr` **W** / `.external_escalated` | grm | ticket_id, case_id or forum_code | intake, WH |
| 146 | `equator.grm.ticket.clock_breached` · `equator.grm.report.generated` | grm | ticket_id, clock_id · report_id, variant, period | ops (Sev-1), NOT |
| 147 | `equator.posh.complaint.registered` · `equator.posh.annual_report.filed` | posh (sealed, internal) | opaque_token, due dates · year | sealed CLK only |
| 148 | `equator.posh.task.created` | posh → core tasks | sealed_ref, kind | NOT (content-free) |
| 149 | `equator.chambers.workspace.activated` | chambers | workspace_id, plan | BIL |
| 150 | `equator.academy.enrolment.created` / `.completed` | academy | enrolment_id, course_id | BIL, certificates |
| 151 | `equator.academy.certificate.issued` / `.revoked` | academy | certificate_id, verification_code | public verify |
| 152 | `equator.campus.competition.results_released` | campus | competition_id | NOT |
| 153 | `equator.growth.lead.created` | growth (isolated) | lead_id, source | CRM only (never consumes case events — NN-16) |
| 154 | `equator.growth.claim.expired` | growth | claim_id | CMS (unpublish) |
| 155 | `equator.audit.chain.verified` / `.broken` | audit | chain_id, range, first_bad_seq | ops (RB-10) |
| 156 | `equator.ops.incident.declared` / `.closed` | ops | incident_id, severity, category | NOT, status page |
| 157 | `equator.ops.regulatory_notification.due` / `.sent` | ops | notification_id, regulator, deadline_at | NOT |
| 158 | `equator.ops.dr_drill.completed` | ops | drill_id, rpo_seconds, rto_seconds | RPT |
| 159 | `equator.ops.launch.decision_recorded` | ops | decision, blocking_codes | AUD |
| 160 | `equator.integrations.provider.circuit_opened` / `.closed` | integrations | provider_code, kind | ops, routing |
| 161 | `equator.enterprise.report.generated` | enterprise | report_id, pack_type, manifest_sha256 | NOT, ENT |
| 162 | `equator.evidence.aa_summary.created` | integrations (AA) | case_id, summary_id, consent_ref | proceedings (neutral view), AUD |
| 163 | `equator.connectors.sync.completed` | integrations | connector, run_id, counts | ops |
| 164 | `equator.voice.number_authorisation.activated` / `.expired` / `.revoked` | voice | authorisation_id, tenant_id, series | CLI guard cache, NOT (expiry T-30) |
| 165 | `equator.ops.telecom_declaration.recorded` / `.expired` | ops | declaration_id, kind, operator | CLI guard cache, AUD |
| 166 | `equator.voice.call.blocked_by_cli_policy` | voice | communication_id, reason_code | ops dashboard |
| 167 | `equator.cases.pims_referral.filed` / `.outcome_recorded` | cases (COM) | case_id, referral_id, outcome | CLK, NOT |

Webhook delivery (P09 FR-P09-04): HMAC-SHA256 over `t + "." + raw body` (`X-Equator-Signature: t=<unix>,v1=<hex>`), 5-minute replay tolerance, 7 retries at 1 m, 5 m, 30 m, 2 h, 6 h, 12 h, 24 h (then `failed`, replayable for 30 days via `/v1/webhook-deliveries/{id}/replay`); auto-pause after 72 h of failures.

**v3.0 event contexts (23 October 2026).** v3.0 adds the contexts below. Envelope, ordering, payload rules (IDs, codes and minor-unit amounts only; never salary, bank, identifier or personal values) and the `v1`/`v2` versioning rule above apply unchanged. Each context's catalogue lives in its owning appendix, which prevails on event names; the P00 event-schema registry loads them from there.

| Context | Owner | Catalogue | Notes |
|---|---|---|---|
| `cfg` | Appendix V (settings, rule packs, watch, access); Appendix AC (connectors, workspace connections, mappings, rehearsals, mirrors) | V §V.6.3; AC §AC.12 and P21 §7.4 | `equator.cfg.setting_pack.applied.v1` (not `settings_pack`); `cfg.workspace_connection.*` replaces the former `ops.workspace.*` names; Microsoft 365/Google account lifecycle events stay `equator.hr.workspace.account_provisioned` / `.account_disabled` |
| `chm` | Appendix W | W §W.12 | v2 `equator.chambers.*.v1` events are unchanged (X-47); a chambers configuration change emits `equator.chm.config.changed.v1` and the platform `equator.cfg.setting.changed.v1` |
| `ops` | Appendix X (Operations Platform only, X-50) | X §X.17 | Adds `equator.ops.connector.engagement_received.v1` (single Brevo ingress `/webhooks/brevo` → Appendix Y `mkt.touchpoints`) |
| `mkt` | Appendix Y | Y §Y.7.6, §Y.16 | Internal bus; never delivered to tenant webhooks |
| `hr`, `pay`, `ctl` | Appendix Z | Z §Z.17.2 | Internal bus only; never delivered to tenant webhooks; leaver revocation starts on `equator.hr.employee.exit_effective.v1` (X-57) |
| `mkp`, `dir` | Appendix AA | AA §AA.19 | Research names `directory.record.*.v1` map to `equator.dir.record.*.v1` (X-59(e)); allocation and conflict engines consume only `equator.dir.panel_membership.*` |
| `rev` | Appendix AB | AB §AB.11 | Stream lifecycle and kill-switch events |
| `xpt` | Appendix AC | P21 §7.4 | `equator.xpt.export.requested` … `.expired`, import events |
| `grp` | Appendix AD | AD §AD.15.2 | Cross-company grants and agreements; never carries case data (NN-38) |
| `eng` | Appendix AE | AE §AE.12.2 | Change, release, deployment, vulnerability, restore-test and DR events |

Consumed name corrected: the consent-withdrawal event is `equator.consent.consent.withdrawn.v1` (P01). Appendix X also consumes `equator.billing.invoice.overdue.v1`, `equator.enterprise.tenant.provisioned.v1` and `equator.enterprise.clause.adopted.v1`, which no v2.1 file produces: they are registered here as v3.0 events of P05 dunning (`billing`) and P09 onboarding and clause adoption (`enterprise`), unless an ADR maps Appendix X to the existing `equator.tenancy.tenant.created.v1` and `equator.enterprise.clause_instance.*` names. **Platform-assurance events with context `ops`** (rows #156–#159 and #165 above) belong to the assurance tables that move to `eng` under master X-50 and X-65: where Appendix AE §AE.12.2 defines an equivalent (`equator.eng.dr_drill.completed.v1`, `equator.eng.vulnerability.*.v1`) the `eng` name is canonical; the remaining rows are emitted as `equator.eng.<entity>.<verb>.v1` with the same entity and verb; the `ops` names stay accepted aliases for v3.0 only (record the mapping in an ADR).

---

## F.10 Error catalogue

**Format (RFC 9457 problem+json)**: `{ "type": "https://equatorresolution.in/problems/<code-lower-kebab>", "title", "status", "code", "detail" (localised, no PII), "instance" (request id), "rule" (optional vertical rule ID, e.g. `INS-R1`), "violations": [{field, code}], "available_routes": [] }`. `code` values are stable forever; messages are i18n keys `errors.<CODE>`. Vertical-prefixed codes used in phase files (`FIN_*`, `COM_*`, `FAM_*`, `INS_*`, `WRK_*`, `INT_*`) are valid **sub-codes carried in `rule`** under the canonical `code` shown in the last column of F.10.2.

### F.10.1 Canonical codes

| Code | HTTP | Message (en) | NN / source |
|---|---|---|---|
| `VALIDATION_FAILED` | 400 | One or more fields are invalid. | — |
| `IDEMPOTENCY_KEY_REQUIRED` | 400 | This request needs an Idempotency-Key header. | master §4.4 |
| `IDEMPOTENCY_KEY_REUSED` | 409 | This Idempotency-Key was used with a different request. | — |
| `UNAUTHENTICATED` | 401 | Please sign in again. | — |
| `STEP_UP_REQUIRED` | 401 | Confirm it's you to continue. | L.1 |
| `DPOP_PROOF_INVALID` | 401 | Device proof is invalid. | P12 |
| `DEVICE_NOT_BOUND` | 401 | This device is not registered to your account. | P12 |
| `FORBIDDEN` | 403 | You do not have permission for this action. | — |
| `TENANT_MISMATCH` | 403 | This resource belongs to a different organisation. | RLS |
| `DEVICE_INTEGRITY_FAILED` | 403 | This action is unavailable on this device. | P12 |
| `SEALED_TIER_DEVICE_REQUIREMENT` | 403 | Sealed matters can only be opened on a verified device. | NN-07 |
| `SEALED_SCOPE_REQUIRED` | 403 | Additional authorisation is required for this record. | NN-07 |
| `CAUCUS_SEALED` | 403 | Caucus notes are visible only to their author. | NN-11 |
| `BREAK_GLASS_JUSTIFICATION_REQUIRED` | 403 | Emergency access needs a written justification. | L.2 |
| `NOT_FOUND` | 404 | Not found or not available to you. | API1 |
| `DEEPLINK_INVALID` | 404 | This link is invalid or has expired. | P12 |
| `UPLOAD_TYPE_NOT_ALLOWED` | 415 | This file type is not accepted. | — |
| `APP_VERSION_UNSUPPORTED` | 426 | Please update the app to continue. | P12 |
| `RATE_LIMITED` | 429 | Too many requests. Try again later. | — |
| `OTP_LOCKED` | 429 | Too many attempts. Try again in 15 minutes. | P01 |
| `INTERNAL` | 500 | Something went wrong. Reference: {instance}. | — |
| `PROVIDER_UNAVAILABLE` | 503 | A partner service is unavailable; we've queued your request. | R3 §10 |
| `FIELD_NOT_WRITABLE` | 422 | One or more fields cannot be changed. | API3 |
| `VERSION_CONFLICT` | 412 | This record changed since you opened it. | — |
| `CONSENT_REQUIRED` | 409 | A recorded consent is required before this step. | NN-15 |
| `CONSENT_WITHDRAWN` | 409 | Consent for this purpose has been withdrawn. | NN-15 |
| `GUARDIAN_CONSENT_REQUIRED` | 409 | A parent or guardian must consent for a minor. | DPDP s.9 |
| `KYC_REQUIRED` | 409 | Identity verification is required first. | SC-01 |
| `AADHAAR_UNMASKED_DETECTED` | 422 | Please mask the Aadhaar number before uploading. | NN-14 |
| `REGULATED_RAIL_TENANT_ONLY` | 403 | This data can only be fetched by the regulated entity. | NN-14 |
| `UPLOAD_HASH_MISMATCH` | 422 | The file did not upload correctly; please retry. | P12 |
| `UPLOAD_QUARANTINED` | 422 | The file failed a safety check. | — |
| `CASE_NOT_ARBITRABLE` | 422 | This matter cannot be decided by arbitration; mediation or the listed forum is available. | NN-06 |
| `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` | 422 | This mechanism is not available for this type of dispute. | master §5.2 |
| `CONSUMER_FORUM_NOT_OUSTABLE` | 422 | This clause cannot exclude the Consumer Commission. | NN-06 (Emaar MGF) |
| `SIGNPOSTING_REQUIRED` | 409 | The appropriate free or statutory forum must be shown before this step. | NN-20 |
| `CLOSURE_BLOCKED` | 409 | The case cannot close until required steps are complete. | P02 guard |
| `CLOCK_UNOWNED` | 409 | A statutory clock has no owner. | NN-04 |
| `CLOCK_EXTENSION_NOT_PERMITTED` | 422 | This time limit cannot be extended this way. | NN-04 |
| `S29A_MANDATE_LAPSED` | 409 | The tribunal's mandate has lapsed; only a court can extend it. | NN-04 |
| `BACKDATING_FORBIDDEN` | 422 | Dates cannot be set earlier than the server time of signing. | NN-04 |
| `DEFICIENCY_CURE_WINDOW_CLOSED` | 409 | The window to cure deficiencies has closed. | P02 |
| `LIMITATION_EXPIRED_STAGE_BLOCKED` | 422 | Limitation bars this stage; other routes remain. | C1 M.4 |
| `RULESET_VERSION_PINNED` | 409 | This case follows the rules in force when it was filed. | NN-21 |
| `RULESET_GUARDRAIL_VIOLATION` | 422 | This configuration breaches a platform guardrail. | master §6 |
| `LEGAL_RULE_UNVERIFIED` | 409 | This feature depends on a rule awaiting legal verification. | master §0 |
| `MAKER_CHECKER_SAME_USER` | 403 | A different person must approve this change. | NN-21 |
| `STATUTORY_MODE_OFF` | 409 | Statutory mediation mode is not enabled. | NN-05 |
| `APPOINTMENT_LENDER_TRIGGER_BLOCKED` | 403 | Enterprise clients cannot select, veto or trigger neutral selection. | NN-03 |
| `NEUTRAL_SELECTION_FORBIDDEN` | 403 | Party choice is disabled for this matter. | NN-03 |
| `S12_5_WAIVER_MISSING` | 409 | A post-dispute written waiver is required from each party. | NN-03 |
| `S12_5_WAIVER_PREDATES_DISPUTE` | 422 | A waiver signed before the dispute arose is not valid. | NN-03 |
| `DISCLOSURE_REQUIRED` | 409 | The neutral must submit a disclosure first. | A&C s.12 |
| `CONFLICT_DETECTED` | 409 | A conflict of interest prevents this appointment. | P03 |
| `CONCENTRATION_CAP_EXCEEDED` | 409 | Appointment would exceed the neutral's concentration cap for this client. | NN-03 |
| `ALLOCATION_POOL_EXHAUSTED` | 409 | No eligible neutral is available; the matter is escalated. | P03 |
| `NEUTRAL_UNAVAILABLE` | 409 | The neutral is not available at that time. | — |
| `SAME_NEUTRAL_CONSENT_MISSING` | 409 | Fresh written consent of all parties is needed for the same neutral to arbitrate. | master §5.3 |
| `CAUCUS_FIREWALL_VIOLATION` | 422 | Caucus material cannot enter the arbitral record. | master §5.3 |
| `SAFETY_FLAG_BLOCKS_JOINT` | 409 | A joint session is not available for this matter; shuttle sessions are. | NN-07 / B.5 |
| `RECORDING_FORBIDDEN` | 409 | This session cannot be recorded. | NN-11 |
| `RECORDING_CONSENT_INCOMPLETE` | 409 | All participants must consent before recording. | NN-11 |
| `SESSION_NOT_OPEN` | 409 | This session is not open for joining. | P04 |
| `LIVENESS_REQUIRED` | 403 | A liveness check is required to join. | L.1 |
| `OFFER_EXPIRED` | 409 | This offer has expired. | P04 |
| `OFFER_ABOVE_AUTHORITY` | 403 | The offer exceeds your approval limit. | P04 |
| `BLIND_BID_LOCKED` | 409 | Bids cannot be changed in this round. | P04 |
| `AWARD_NOT_REASONED` | 422 | An award must state reasons unless it is a consent award. | A&C s.31(3) |
| `AWARD_SEALED` | 403 | The sealed award is not yet released. | master §5.3 |
| `SEALED_HASH_MISMATCH` | 409 | The released award does not match the sealed record. | master §5.3 |
| `STATUTORY_WAIVER_FORBIDDEN` | 422 | Statutory rights, dues or maintenance cannot be waived. | C1 B.8 |
| `SETTLEMENT_LINT_FAILED` | 422 | The settlement has items to fix before signing. | P06 |
| `ESIGN_EXCLUDED_INSTRUMENT` | 422 | This document must be signed physically and registered. | NN-08 |
| `REGISTRATION_REQUIRED` | 409 | Registration must be completed before this step. | NN-08 |
| `ESTAMP_REQUIRED` | 409 | Stamp duty must be paid before execution. | NN-09 |
| `ESTAMP_STATE_UNSUPPORTED` | 422 | E-stamping is not available for this state; use physical stamp paper. | NN-09 |
| `VIRTUAL_SIGN_NOT_PERMITTED` | 422 | This signer must use Aadhaar eSign or DSC. | P06 |
| `BUNDLE_CERTIFICATE_MISSING` | 409 | The export needs its hash manifest and s.63(4) certificate. | NN-10 |
| `QUOTE_EXPIRED` | 409 | This quote has expired; request a new one. | P05 |
| `AMOUNT_TAMPERED` | 422 | The amount does not match the server quote. | P05 |
| `PAYMENTS_SETTLEMENT_ON_MERCHANT_FORBIDDEN` | 422 | Settlement sums are paid through escrow or directly, not to Equator. | NN-13 |
| `FEE_CONTINGENCY_FORBIDDEN` | 422 | This fee cannot depend on the outcome. | NN-18 |
| `REGULATED_FEE_IMMUTABLE` | 422 | A regulated fee schedule cannot be discounted or edited. | NN-18 |
| `FX_RATE_STALE` | 409 | The exchange rate is out of date; please refresh the quote. | NN-13 |
| `CURRENCY_NOT_PERMITTED` | 422 | This currency is not available for this matter. | master §7 |
| `REFUND_NOT_ELIGIBLE` | 409 | This payment is not eligible for a refund under the fee rules. | P05 |
| `ESCROW_MILESTONE_CONDITIONS_UNMET` | 409 | Release conditions are not yet met. | C1 B.8 |
| `PAYEE_ACCOUNT_UNVERIFIED` | 409 | The bank account must be verified first. | P05 |
| `CONTACT_OUTSIDE_WINDOW` | 409 | Contact is allowed only between 08:00 and 19:00 local time. | NN-12 |
| `CONTACT_BLACKOUT_ACTIVE` | 409 | Contact is paused for this person. | NN-12 |
| `DLT_TEMPLATE_UNREGISTERED` | 422 | This SMS template is not registered. | NN-12 |
| `GRO_DETAILS_MISSING` | 422 | Recovery-related messages must show grievance officer details. | NN-12 |
| `MARKETING_CONSENT_REQUIRED` | 409 | Marketing needs separate consent. | NN-16 |
| `CASE_DATA_TO_GROWTH_FORBIDDEN` | 403 | Case data cannot be shared with marketing systems. | NN-16 |
| `CLAIM_NOT_EVIDENCED` | 422 | This public claim has no current evidence record. | NN-17 |
| `AI_HUMAN_REVIEW_REQUIRED` | 409 | AI drafts must be reviewed by a person before use. | NN-01 |
| `AI_OUTPUT_BLOCKED` | 422 | The AI response was withheld by a safety policy. | NN-01 |
| `AI_FEATURE_NOT_PERMITTED` | 403 | This AI feature is not enabled. | P11 |
| `AI_SEALED_DATA_FORBIDDEN` | 403 | Sealed data cannot be sent to AI services. | NN-07 |
| `POSH_MUST_BE_SEALED` | 422 | POSH complaints are handled only in the sealed IC workspace. | NN-07 |
| `POSH_S10_NOT_REQUESTED` | 422 | Conciliation needs the aggrieved woman's written request. | NN-07; POSH s.10 |
| `POSH_MONETARY_TERM_BLOCKED` | 422 | Conciliation cannot be on a monetary basis. | NN-07; POSH s.10(1) |
| `IC_COMPOSITION_INVALID` | 422 | The IC needs at least one-half women members and an external member. | NN-07; POSH s.4 |
| `INS_RETAIL_ARBITRATION_BLOCKED` | 422 | Arbitration is not available against a retail policyholder. | master §1.2 |
| `WRK_WORKMAN_ARBITRATION_BLOCKED` | 422 | Arbitration is not available for workman disputes. | master §5.2 |
| `SANCTIONS_HIT_REVIEW` | 409 | Registration is on hold pending sanctions review. | NN-19 |
| `INT_KYC_UBO_INCOMPLETE` | 409 | Beneficial ownership details are incomplete. | NN-19 |
| `DPDP_TRANSFER_BASIS_MISSING` | 409 | A recorded basis for cross-border transfer is required. | NN-15/19 |
| `INT_TEST_NOT_MET` | 422 | This matter does not meet the international commercial test. | NN-19 |
| `SEC_CONNECTOR_DISABLED` | 409 | The securities connector is not enabled. | master §1.2 |
| `BULK_ROW_INVALID` | 422 | Row rejected; see row errors. | P09 |
| `WEBHOOK_URL_NOT_ALLOWED` | 422 | Webhook destination is not allowed. | API7 |
| `DEVICE_LIMIT_REACHED` | 409 | Remove a device to add this one. | P12 |
| `WAIVER_NOT_ALLOWED_NN_ITEM` | 422 | Items linked to non-negotiable rules cannot be waived. | P14 |
| `DSR_LEGAL_HOLD` | 409 | Some data must be kept under a legal hold; we've explained what was erased. | NN-15 |
| `SCOPE_NOT_GRANTABLE` | 403 | This scope cannot be granted to an API client. | NN-07; P09 |
| `CLAUSE_VARIANT_PROHIBITED` | 422 | This clause variant is not permitted. | NN-03, NN-06; P09 |
| `BULK_ROW_LIMIT` | 413 | The file has more rows than one batch allows. | P09 |
| `AA_FIU_NOT_CONFIGURED` | 412 | Account Aggregator evidence needs the lender's own FIU set-up. | NN-14; P09 |
| `DPA_REQUIRED` | 412 | An executed data-processing agreement is required first. | NN-15; P09 |
| `POSH_LIMITATION_EXTENSION_REASON_REQUIRED` | 422 | A late complaint needs the Internal Committee's recorded reason for extension. | POSH s.9(1); P09 |
| `CLI_NOT_AUTHORISED` | 409 | No authorised calling number is available for this call. | NN-12 (M-05) |
| `TELECOM_CONSENT_NOT_REGISTERED` | 409 | This call needs consent registered with the telecom operator. | NN-12 (M-05) |

(123 codes; the CI check compares this table with `packages/domain/errors.ts`.)

### F.10.2 Phase sub-code mapping (carried in `rule`)
`FIN_CONTACT_WINDOW` → `CONTACT_OUTSIDE_WINDOW`; `FIN_ARB_CLAUSE_NOT_ORIGINATION`, `FIN_DRT_EXCLUSIVE`, `FIN_SPECIAL_FORUM`, `FAM_NON_ARBITRABLE`, `NN06_NON_ARBITRABLE` → `CASE_NOT_ARBITRABLE`; `INS_RETAIL_ARBITRATION` → `INS_RETAIL_ARBITRATION_BLOCKED`; `INS_STATUTORY_WAIVER`, `WRK_STATUTORY_DUES_WAIVER` → `STATUTORY_WAIVER_FORBIDDEN`; `INS_SIGNPOSTING_REQUIRED` → `SIGNPOSTING_REQUIRED`; `INS_CLOCK_UNOWNED` → `CLOCK_UNOWNED`; `INS_FRAUD_NOT_MEDIABLE`, `FAM_PRESSURE_CONDITION` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `FAM_SAFETY_JOINT_BLOCKED` → `SAFETY_FLAG_BLOCKS_JOINT`; `FAM_REGISTRATION_REQUIRED` → `REGISTRATION_REQUIRED`; `FAM_HEIRS_NOT_JOINED`, `FAM_MINOR_PROPERTY_COURT_PERMISSION` → `CLOSURE_BLOCKED`; `COM_NO_ARB_AGREEMENT`, `COM_MSEFC_PENDING`, `COM_PIMS_CERT_NOT_ISSUABLE` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `WRK_STRUCTURAL_CONFLICT` → `CONFLICT_DETECTED`; `WRK_POSH_ROUTED_SEALED` → `POSH_MUST_BE_SEALED`; `INT_SANCTIONS_HOLD`, `SANCTIONS_HOLD` → `SANCTIONS_HIT_REVIEW`; `INT_SEAT_NOT_NOTIFIED`, `INT_OUT_OF_SCOPE_STATE` → `INT_TEST_NOT_MET`; `FX_SNAPSHOT_STALE` → `FX_RATE_STALE`; `PAY_SETTLEMENT_ROUTE_FORBIDDEN` → `PAYMENTS_SETTLEMENT_ON_MERCHANT_FORBIDDEN`; `SUCCESS_FEE_NOT_PERMITTED` → `FEE_CONTINGENCY_FORBIDDEN`; `POSH_S10_INVALID`, `POSH_CONCILIATION_REQUEST_NOT_PERMITTED` → `POSH_S10_NOT_REQUESTED`; `POSH_MONETARY_SETTLEMENT_BLOCKED` → `POSH_MONETARY_TERM_BLOCKED`; `IC_WOMEN_LESS_THAN_HALF` → `IC_COMPOSITION_INVALID`; `APPOINTMENT_TRIGGER_NOT_PERMITTED` → `APPOINTMENT_LENDER_TRIGGER_BLOCKED`; `RETAIL_ARBITRATION_BLOCKED` → `INS_RETAIL_ARBITRATION_BLOCKED`; `STATUTORY_DUES_WAIVER_BLOCKED` → `STATUTORY_WAIVER_FORBIDDEN`; `STRUCTURAL_CONFLICT` → `CONFLICT_DETECTED`; `VOICE_CLI_UNDECLARED`, `VOICE_1600_AUTHORISATION_MISSING` → `CLI_NOT_AUTHORISED`; `COM_S12A_EQUATOR_NOT_AUTHORISED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `ROW_*` → `BULK_ROW_INVALID`; `COMMS_*` → `DLT_TEMPLATE_UNREGISTERED` / `CONTACT_OUTSIDE_WINDOW` as applicable; `VOICE_*` → `FORBIDDEN` (409 for `VOICE_KILL_SWITCH_ON`); `PARTY_CHOICE_DISABLED_REPEAT_PLAYER` → `NEUTRAL_SELECTION_FORBIDDEN`. **v3.0 (23 Oct 2026; Appendix W §W.13, X-49):** `CHM_LEAVE_POLICY_BELOW_FLOOR` → `HR_LEAVE_POLICY_BELOW_FLOOR`; `CHM_MONITORING_PROHIBITED` → `HR_MONITORING_PROHIBITED`; `CHM_PAYRUN_PARAM_UNCONFIRMED` → `PAY_PARAM_NOT_CONFIRMED`; `CHM_PAYRUN_DEDUCTION_CAP` → `PAY_DEDUCTION_CAP_EXCEEDED`; `CHM_PAYRUN_GHOST_HIT_UNRESOLVED` → `PAY_GHOST_HITS_UNRESOLVED`; `CHM_STATUTORY_DUES_WAIVER` → `STATUTORY_WAIVER_FORBIDDEN`; `CHM_MAKER_CHECKER_SAME_USER` → `CTL_SELF_APPROVAL_BLOCKED`; `CHM_BANK_CHANGE_COOLING` → `CTL_COOLING_OFF_ACTIVE`; `CHM_BANK_NAME_MISMATCH` → `CTL_PENNY_DROP_MISMATCH`; `CHM_DISBURSAL_FILE_HASH_MISMATCH` → `PAY_BANK_FILE_HASH_MISMATCH`; `CHM_LABEL_PROHIBITED` → `LABEL_PROHIBITED_TERM`. No `PAY_STATUTORY_WAIVER_FORBIDDEN` is created. New sub-codes must be registered here before use (CI check on `packages/domain/errors.ts`).

### F.10.3 v2 code register (21 October 2026)

The v2 files (verticals V1–V6, appendices K–T and the phase v2 addenda) introduced the codes below. They are registered here so the CI check on `packages/domain/errors.ts` passes (X-20). Rules: (1) a code marked *canonical (v2)* is a first-class `code` with the HTTP status shown; its message text is the one given in the defining file; (2) a vertical-prefixed code is a sub-code carried in `rule`: where the defining vertical's error-mapping section (V1 §16 sub-code list, V2 §16.4, V3 §16.6, V4 C-12, V5 R-table and §16, V6 §16.7) names a canonical F.10.1 parent, the parent's code and status are returned; where it names none, the code and status below apply; (3) superseded names stay valid only as seed-loader aliases (`WRK_WORKMAN_ARBITRATION` → `WRK_WORKMAN_ARBITRATION_BLOCKED`; `MECH_NOT_PERMITTED_FOR_VERTICAL` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`; `INS_RETAIL_ARBITRATION` → `INS_RETAIL_ARBITRATION_BLOCKED`); (4) `ARB_S12_5_WAIVER_INVALID` maps to `S12_5_WAIVER_PREDATES_DISPUTE` (422) and `COPY_PROHIBITED_CLAIM` maps to `CLAIM_NOT_EVIDENCED` (422) where the claim lacks an evidence record.

| Code | HTTP | Defined in | Disposition |
|---|---|---|---|
| `INS_AUTHORITY_UNCONFIRMED` | 409 | V4 INS, P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_GATE_PENDING` | 409 | V6 INT, P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_AML_REVIEW_REQUIRED` | 409 | V6 INT, P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_EA_NOA_OVERDUE` | 409 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_TPF_UNDISCLOSED` | 409 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_RELEVANT_PERSONS_MISSING` | 409 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_SGCONV_CONVERSION_CONFLICT` | 409 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `EXPLORER_SESSION_EXPIRED` | 410 | App. K | canonical (v2) |
| `EXPLORER_QUESTION_NOT_CURRENT` | 409 | App. K | canonical (v2) |
| `MATTER_EXCLUDED` | 422 | App. K | canonical (v2) |
| `URGENT_INTERRUPT_ACTIVE` | 409 | App. K | canonical (v2) |
| `PRELIT_CONTACT_CAP_REACHED` | 409 | App. K | canonical (v2) |
| `PRELIT_CONSENT_INCOMPLETE` | 409 | App. K | canonical (v2) |
| `PRELIT_OFFER_PERIOD_TOO_SHORT` | 422 | App. K | canonical (v2) |
| `PRELIT_CONVERSION_NOT_ELIGIBLE` | 422 | App. K | canonical (v2) |
| `PACK_VALIDATION_FAILED` | 422 | App. K | canonical (v2) |
| `PACK_WIDENS_MATRIX` | 422 | App. K | canonical (v2) |
| `PACK_CODE_IN_USE` | 409 | App. K | canonical (v2) |
| `HELPLINE_UNVERIFIED` | 409 | App. K | canonical (v2) |
| `DOC_VISIBILITY_DOWNGRADE_FORBIDDEN` | 409 | App. L | canonical (v2) |
| `DOC_SERVICE_REQUIRED_ARBITRATION` | 422 | App. L | canonical (v2) |
| `DOC_PRIVILEGED_SHARE_BLOCKED` | 409 | App. L | canonical (v2) |
| `DOC_PUBLIC_VIA_PUBLICATION_ONLY` | 403 | App. L | canonical (v2) |
| `SECURE_LINK_EXPIRED` | 410 | App. L | canonical (v2) |
| `SECURE_LINK_SEALED_FORBIDDEN` | 403 | App. L | canonical (v2) |
| `LEGAL_HOLD_ACTIVE` | 409 | App. L | canonical (v2) |
| `REDACTION_INCOMPLETE` | 422 | App. L | canonical (v2) |
| `RENDER_PROFILE_UNVERIFIED` | 409 | App. L | canonical (v2) |
| `RENDER_PROFILE_LOCKED_TOKEN` | 422 | App. L | canonical (v2) |
| `COURT_EXPORT_UNTRANSLATED_ANNEXURE` | 422 | App. L | canonical (v2) |
| `COURT_EXPORT_UNRESOLVED_REFERENCE` | 422 | App. L | canonical (v2) |
| `TYPE_COPY_UNVERIFIED` | 409 | App. L | canonical (v2) |
| `TYPE_COPY_LOW_LINES_OPEN` | 422 | App. L | canonical (v2) |
| `WA_LOCALE_AMBIGUOUS` | 409 | App. L | canonical (v2) |
| `WA_EXPORT_UNRECOGNISED` | 422 | App. L | canonical (v2) |
| `TRANSLATION_NOT_CERTIFIED` | 422 | App. L | canonical (v2) |
| `LOCKED_TERM_MISSING` | 422 | App. L | canonical (v2) |
| `OCR_ROUTE_RESIDENCY_BLOCKED` | 403 | App. L | canonical (v2) |
| `AFFIDAVIT_REQUIRES_OATH` | 422 | App. L | canonical (v2) |
| `ESTAMP_REQUIRED_BEFORE_SIGNING` | 409 | App. L | canonical (v2) |
| `ZIP_UNSAFE` | 422 | App. L | canonical (v2) |
| `FILE_ENCRYPTED_UNSUPPORTED` | 422 | App. L | canonical (v2) |
| `LEGACY_FONT_DETECTED` | 409 | App. L | canonical (v2) |
| `TAG_SENSITIVE_TERM` | 422 | App. L | canonical (v2) |
| `STUDIO_UNANCHORED_FACT` | 422 | App. M | canonical (v2) |
| `STUDIO_QUOTE_MISMATCH` | 422 | App. M | canonical (v2) |
| `STUDIO_CITATION_UNVERIFIED` | 422 | App. M | canonical (v2) |
| `STUDIO_QUANTUM_MISMATCH` | 422 | App. M | canonical (v2) |
| `STUDIO_ENTAILMENT_FAILED` | 422 | App. M | canonical (v2) |
| `STUDIO_OPEN_QUESTIONS` | 422 | App. M | canonical (v2) |
| `STUDIO_SECTION_NOT_APPROVED` | 422 | App. M | canonical (v2) |
| `STUDIO_FORMAT_INVALID` | 422 | App. M | canonical (v2) |
| `STUDIO_PII_UNMASKED` | 422 | App. M | canonical (v2) |
| `STUDIO_ANNEXURE_MISMATCH` | 422 | App. M | canonical (v2) |
| `STUDIO_AFFIDAVIT_NOT_SWORN` | 422 | App. M | canonical (v2) |
| `STUDIO_STAFF_EDIT_FORBIDDEN` | 403 | App. M | canonical (v2) |
| `STUDIO_FAIR_USE_LIMIT` | 429 | App. M | canonical (v2) |
| `STUDIO_SEALED_MATTER` | 403 | App. M | canonical (v2) |
| `STUDIO_BULK_NOT_SUPPORTED` | 422 | App. M | canonical (v2) |
| `STUDIO_VERSION_CHANGED` | 409 | App. M | canonical (v2) |
| `HB_GRADE_INELIGIBLE` | 409 | App. N | canonical (v2) |
| `HB_JURISDICTION_INELIGIBLE` | 409 | App. N | canonical (v2) |
| `COMMITTEE_COMPOSITION_INVALID` | 422 | App. N | canonical (v2) |
| `COMMITTEE_MEMBER_RECUSED` | 403 | App. N | canonical (v2) |
| `DECISION_REASONS_REQUIRED` | 422 | App. N | canonical (v2) |
| `ASSESSOR_CONFLICT` | 409 | App. N | canonical (v2) |
| `ASSESSOR_EXTERNAL_REQUIRED` | 422 | App. N | canonical (v2) |
| `QAP_RESIT_TOO_EARLY` | 422 | App. N | canonical (v2) |
| `QAP_RESIT_LIMIT` | 422 | App. N | canonical (v2) |
| `GRADE_PRECHECK_UNVERIFIED` | 422 | App. N | canonical (v2) |
| `DIRECTORY_SORT_NOT_ALLOWED` | 400 | App. N | canonical (v2) |
| `FEEDBACK_OUTCOME_ITEM_FORBIDDEN` | 422 | App. N | canonical (v2) |
| `REVIEW_REPLY_TOO_LONG` | 422 | App. N | canonical (v2) |
| `COMPLAINT_CONSENT_REQUIRED` | 422 | App. N | canonical (v2) |
| `LABEL_FORBIDDEN_TERM` | 422 | App. N | canonical (v2) |
| `FORM_FIELD_PURPOSE_MISSING` | 422 | App. Q | canonical (v2) |
| `SUBPROCESSOR_NOT_APPROVED` | 409 | App. Q | canonical (v2) |
| `AI_SYSTEM_NOT_REGISTERED` | 409 | App. Q | canonical (v2) |
| `EU_REPRESENTATIVE_REQUIRED` | 409 | App. Q | canonical (v2) |
| `AI_FEATURE_DISABLED_FOR_EU_PARTY` | 403 | App. Q | canonical (v2) |
| `CARD_DATA_FORBIDDEN` | 422 | App. Q | canonical (v2) |
| `CARD_DATA_DETECTED_IN_UPLOAD` | 422 | App. Q | canonical (v2) |
| `CONTROL_EVIDENCE_STALE` | 409 | App. Q | canonical (v2) |
| `CVC_LOCKED` | 429 | App. R | canonical (v2) |
| `PUBLICATION_NOT_ELIGIBLE` | 422 | App. R | canonical (v2) |
| `PUBLICATION_CONSENT_MISSING` | 409 | App. R | canonical (v2) |
| `PUBLICATION_GATES_INCOMPLETE` | 409 | App. R | canonical (v2) |
| `PUBLICATION_EMBARGO_ACTIVE` | 409 | App. R | canonical (v2) |
| `PUBLICATION_FLAG_OFF` | 409 | App. R | canonical (v2) |
| `REDACTION_SAME_REVIEWER` | 403 | App. R | canonical (v2) |
| `REPRESENTATIVE_CANNOT_CONSENT_PUBLICATION` | 403 | App. R | canonical (v2) |
| `EXECUTION_NOT_READY` | 409 | App. R | canonical (v2) |
| `EXECUTION_STAYED` | 409 | App. R | canonical (v2) |
| `OVC_INVALID_OR_EXPIRED` | 404 | App. R | canonical (v2) |
| `CERTIFIED_COPY_LIEN_ACTIVE` | 409 | App. R | canonical (v2) |
| `ADVOCATE_NOT_VERIFIED` | 409 | App. R | canonical (v2) |
| `MEDIATION_APPLICATION_TYPE_NOT_ALLOWED` | 422 | App. R | canonical (v2) |
| `PORTAL_ROLE_MISMATCH` | 403 | App. S | canonical (v2) |
| `PHISHING_RESISTANT_MFA_REQUIRED` | 401 | App. S | canonical (v2) |
| `NETWORK_POLICY_DENIED` | 403 | App. S | canonical (v2) |
| `DEVICE_POLICY_DENIED` | 403 | App. S | canonical (v2) |
| `ACCOUNT_SUSPENDED` | 403 | App. S | alias of `FORBIDDEN` (rule carried) |
| `MANDATE_SCOPE_INSUFFICIENT` | 403 | App. S | canonical (v2) |
| `MANDATE_LIMIT_EXCEEDED` | 403 | App. S | canonical (v2) |
| `MANDATE_EXPIRED` | 409 | App. S | canonical (v2) |
| `POA_REQUIRED` | 409 | App. S | canonical (v2) |
| `REPRESENTATIVE_NOT_PERMITTED_FOR_MECHANISM` | 422 | App. S | canonical (v2) |
| `REPRESENTATIVE_CONFLICT` | 409 | App. S | canonical (v2) |
| `FOREIGN_COUNSEL_SCOPE_RESTRICTED` | 422 | App. S | canonical (v2) |
| `DELEGATION_NOT_PERMITTED` | 422 | App. S | canonical (v2) |
| `OVSE_NOT_ENABLED` | 409 | App. S | canonical (v2) |
| `CREDENTIAL_SIGNATURE_INVALID` | 422 | App. S | canonical (v2) |
| `ARB_S12_5_WAIVER_INVALID` | 422 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `IBC_MORATORIUM` | 422 | P08, V1 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FIN_OTS_POLICY_REF_MISSING` | 422 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FIN_PENAL_CAPITALISED` | 422 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `ARB_FEE_CAP_EXCEEDED` | 422 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `ARB_29A_EXPIRED` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_CHILD_CONSENT_MISSING` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_RAJNESH_DISCLOSURE_REQUIRED` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_13B_RECITALS_INCOMPLETE` | 422 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_CLOCK_PROMPT_REQUIRED` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_REVIEWER_SAME` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_NEUTRAL_CONCENTRATION` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `ESCROW_CONDITION_UNMET` | 409 | P08 | canonical (v2) |
| `INT_NATIONALITY_CONFLICT` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COPY_PROHIBITED_CLAIM` | 422 | P08 | canonical (v2) |
| `INT_TRANSFER_BASIS_MISSING` | 409 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_FOREIGN_COUNSEL_NOT_PERMITTED` | 403 | P08 | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `QI_INPUT_NOT_ALLOWED` | — (CI build failure) | App. N | build-time check |
| `TRAINING_PROVIDER_PICKER_MIN` | 500 (configuration check) | App. N | canonical (v2) |
| `PRIVACY_JURISDICTION_UNRESOLVED` | — (DPO task; warning, not a block) | App. Q | task code |
| `STATUS_LOOKUP_FAILED` | — (uniform 200 to the client; logged only) | App. R | internal log code |
| `FORUM_RULE_UNVERIFIED` | — (200 with warning flag; never blocks) | App. R | warning code |
| `NEUTRAL_NOT_ACTIVE` | 403 | App. S | alias of `FORBIDDEN` (rule carried) |
| `COM_MSMED_NOT_ELIGIBLE` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_IBC_INREM` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_IBC_S12A_WINDOW_CLOSED` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_GOVT_ARB_APPROVAL_REQUIRED` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_S442_NOT_REFERABLE` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_IP_REGISTRY_RELIEF` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_MSME_INTEREST_WAIVER_UNACKED` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `COM_SIGNATORY_AUTHORITY_MISSING` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `NN24_CRIMINAL_EXCLUDED` | 422 | V2 COM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_TRIPLE_TALAQ_BLOCKED` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_URGENT_CHILD_REMOVAL` | 409 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_DV_PRECONDITION` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_ARB_ALL_HEIRS_REQUIRED` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_BLIND_BID_VULNERABLE` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_WASIYAT_CONSENT_MISSING` | 409 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_NRI_AGRI_GIFT_BLOCKED` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_CALC_OUT_OF_SCOPE` | 409 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `FAM_CHILD_MAINT_WAIVER` | 422 | V3 FAM | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_TP_MACT_EXCLUSIVE` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_SCHEME_LADDER` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_RETAIL_CONCILIATION_FLAG_OFF` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_OMBUDSMAN_PERSONAL_LINES_ONLY` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_ARB_LIABILITY_NOT_ADMITTED` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INS_ED_RETAIL_BINDING_BLOCKED` | 422 | V4 INS | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_TIER_NOT_ELIGIBLE` | 422 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_HEAP_JOINDER_BLOCKED` | 422 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |
| `INT_ROLE_SWITCH_CONSENT_MISSING` | 409 | V6 INT | vertical sub-code (`rule`); parent per the vertical file's error-mapping section, else registered here |

### F.10.4 v3 code register (23 October 2026)

The v3.0 files (Appendices V–AF and phases P15–P21) introduce the codes below; they are registered here so the CI check on `packages/domain/errors.ts` passes (X-20). The register was **extracted by script** from the error-code tables of the defining appendices on 23 October 2026 (V §V.6.4, W §W.13, X §X.18, Y §Y.17, Z §Z.17.3, AA §AA.20, AB §AB.12, AC §AC.16, AD §AD.15.3, AE §AE.13; `MKT_COMPETITOR_FIGURE_BLOCKED`, first stated in AF §AF.10, is defined in Y §Y.17); the CI check re-runs the extraction against the merged files, and on any difference the defining appendix prevails for the message and this table for the HTTP status until an ADR reconciles them. **316 codes:** `CFG_` 29 (App. V (and AC for connector/SoR codes)) · `CHM_` 48 (App. W) · `OPS_` 35 (App. X) · `MKT_` 36 (App. Y) · `HR_` 24 (App. Z) · `PAY_` 15 (App. Z) · `CTL_` 15 (App. Z) · `MKP_` 26 (App. AA) · `DIR_` 13 (App. AA) · `REV_` 24 (App. AB) · `GRP_` 15 (App. AD) · `XPT_` 11 (App. AC) · `ENG_` 25 (App. AE); 11 of them are sub-codes. Messages: the text in the defining file (Appendix Z §Z.17.3 publishes codes and statuses only; its en/hi messages live in `packages/i18n/errors.workforce.json`).

Rules: (1) *canonical (v3)* codes are first-class `code` values with the HTTP status shown; (2) a *sub-code* is carried in `rule` and the parent's code and status are returned (F.10.2 mappings below); (3) the defining appendix owns its prefix (V `CFG_` — AC adds connector, system-of-record and workspace-connection `CFG_` codes; W `CHM_`; X `OPS_`; Y `MKT_`; Z `HR_`, `PAY_`, `CTL_`; AA `MKP_`, `DIR_`; AB `REV_`; AC `XPT_`; AD `GRP_`; AE `ENG_`); a new code with these prefixes is added in the owning appendix first; (4) **not registered:** `MKT_APPROVAL_NODE_MISSING` (replaced by `OPS_AUTOMATION_APPROVAL_REQUIRED`, Appendix X engine) and `PAY_STATUTORY_WAIVER_FORBIDDEN` (the existing canonical `STATUTORY_WAIVER_FORBIDDEN`, 422, is used); (5) the v2 sub-code `PAY_SETTLEMENT_ROUTE_FORBIDDEN` (F.10.2) keeps its meaning and parent and is not a payroll code; (6) aliases: `WORKSPACE_SKU_INSUFFICIENT_FOR_ROLE` → `HR_WORKSPACE_SKU_INSUFFICIENT`; `WORKSPACE_DELETE_BLOCKED_HOLD` → `HR_WORKSPACE_DELETE_BLOCKED_HOLD`; `MKP_PAYOUT_SOD` is a Cerbos rule name, its violation code is `MKP_PAYOUT_SOD_VIOLATION`; (7) names such as `MKP_SURFACE_ISOLATION`, `MKP_OUTCOME_METRIC_FORBIDDEN`, `CHM_CONFIDENTIALITY_WALL_MATRIX`, `CHM_LINT_PROFILE`, `REV_ORPHAN_PRICE`, `REV_KILL_SWITCH_5_MIN`, `REV_EXPLANATION_FROM_APPROVED_ONLY`, `HR_FORM_PROHIBITED_FIELD`, `OPS_CONSENT_PROPAGATION_LATE` and `DIR_PROPAGATION_OVERDUE` are CI tests, lint rules or alerts, not error codes, and `OPS_DEPARTMENT` / `OPS_CRM` are export scope names (Appendix AC §AC.13.3); (8) parents referenced by v3 files but missing from F.10.1–F.10.3 are registered now: `LABEL_PROHIBITED_TERM` (422; P10 label validator), `CLAIM_BENCHMARK_STALE` (422; Appendix T §0.4 rule (a) and P13 linter); `INTEGRATION_POLICY_REJECTED` in Appendix AC IP-06 is the D.0.2 `POLICY_REJECTED` kind mapped to the port's code.

| Code | HTTP | Defined in | Message / meaning (defining file) | Disposition |
|---|---|---|---|---|
| `CFG_UNREGISTERED_KEY` | 400 | App. V §V.6.4 | This setting is not registered. | canonical (v3) |
| `CFG_TIER_LOCKED` | 403 | App. V §V.6.4 | This value is a platform guardrail and cannot be changed here. | canonical (v3) |
| `CFG_SCOPE_NOT_ALLOWED` | 403 | App. V §V.6.4 | This setting cannot be set at this level. | canonical (v3) |
| `CFG_LOCKED_BY_PARENT` | 409 | App. V §V.6.4 | This setting is locked by {scope}. Request a change from them. | canonical (v3) |
| `CFG_APPROVAL_REQUIRED` | 409 | App. V §V.6.4 | This change needs approval; a request has been created. | canonical (v3) |
| `CFG_OUT_OF_BOUNDS` | 422 | App. V §V.6.4 | The value is outside the allowed range ({min}–{max}). | canonical (v3) |
| `CFG_DIRECTION_VIOLATION` | 422 | App. V §V.6.4 | This setting can only be made stricter at this level. | canonical (v3) |
| `CFG_VALIDATION_FAILED` | 422 | App. V §V.6.4 | The value is invalid. See the listed problems. | canonical (v3) |
| `CFG_CONTRAST_INSUFFICIENT` | 422 | App. V §V.6.4 | These colours do not meet accessibility contrast rules. | canonical (v3) |
| `CFG_CITATION_REQUIRED` | 422 | App. V §V.6.4 | A governed rule needs at least one source citation. | canonical (v3) |
| `CFG_RULE_NOT_ELIGIBLE` | 409 | App. V §V.6.4 | A cited legal rule is not verified or not in force for this effect. | canonical (v3) |
| `CFG_GOLDEN_CASES_FAILED` | 422 | App. V §V.6.4 | The rule pack fails one or more test cases. | canonical (v3) |
| `CFG_PREVIEW_STALE` | 409 | App. V §V.6.4 | Run the preview again before approving. | canonical (v3) |
| `CFG_EFFECTIVE_DATE_INVALID` | 422 | App. V §V.6.4 | The effective date does not meet the minimum lead time. | canonical (v3) |
| `CFG_RULE_CONFLICT` | 409 | App. V §V.6.4 | Two rules give different results; a legal reviewer must decide. | canonical (v3) |
| `CFG_PIN_DEADLINE_PASSED` | 409 | App. V §V.6.4 | Your organisation must move to the current rule-pack version. | canonical (v3) |
| `CFG_ADAPTATION_RELAXES_FLOOR` | 422 | App. V §V.6.4 | An adaptation may only be stricter than the platform rule. | canonical (v3) |
| `CFG_TENANT_REVIEWER_REQUIRED` | 409 | App. V §V.6.4 | A named legal reviewer of your organisation must approve this. | canonical (v3) |
| `CFG_IMPORT_SCHEMA_INVALID` | 422 | App. V §V.6.4 | The settings file is not a valid eq-settings bundle. | canonical (v3) |
| `CFG_IMPORT_CONTAINS_LOCKED` | 422 | App. V §V.6.4 | The file contains locked or out-of-range values; they were not imported. | canonical (v3) |
| `CFG_SECRET_IN_EXPORT` | 422 | App. V §V.6.4 | Secrets cannot be exported. | canonical (v3) |
| `CFG_STALE_VERSION` | 412 | App. V §V.6.4 | This setting changed since you opened it. | canonical (v3) |
| `CFG_ENTITLEMENT_REQUIRED` | 403 | App. V §V.6.4 | This setting is available on another plan. | canonical (v3) |
| `CFG_SUPPORT_SESSION_REQUIRED` | 403 | App. V §V.6.4 | Equator staff need a support session granted by your administrator. | canonical (v3) |
| `CFG_DELEGATION_EXCEEDS_GRANTOR` | 403 | App. V §V.6.4 | You cannot grant more than you hold. | canonical (v3) |
| `CFG_KYB_MISMATCH` | 409 | App. V §V.6.4 | These details differ from your verified business records. | canonical (v3) |
| `CFG_SOR_UNDECLARED` | 409 | App. AC §AC.16 | Declare the system of record for this data before enabling the connector. | canonical (v3) |
| `CFG_MAPPING_MISSING` | 409 | App. AC §AC.16 | An approved field mapping is required for this object. | canonical (v3) |
| `CFG_CONNECTION_CONSENT_REVOKED` | 409 | App. AC §AC.16 | The connected workspace has revoked Equator's access. | canonical (v3) |
| `CHM_SLUG_RESERVED` | 409 | App. W §W.13 | Slug is reserved or quarantined | canonical (v3) |
| `CHM_SLUG_TAKEN` | 409 | App. W §W.13 | Slug used by another tenant | canonical (v3) |
| `CHM_LABEL_PROHIBITED` | 422 | App. W §W.13 | Label validator failed (maps to `LABEL_PROHIBITED_TERM`) | sub-code (`rule`) of `LABEL_PROHIBITED_TERM` |
| `CHM_COPY_LINT_BLOCKED` | 422 | App. W §W.13 | Blocking lint finding(s); `violations[]` lists rule IDs | canonical (v3) |
| `CHM_BLOCK_NOT_ALLOWED_FOR_REGIME` | 422 | App. W §W.13 | Block or field outside the subject's regime allow-list | canonical (v3) |
| `CHM_THEME_CONTRAST_FAIL` | 422 | App. W §W.13 | Palette fails WCAG 2.2 contrast | canonical (v3) |
| `CHM_FONT_NOT_ALLOWED` | 422 | App. W §W.13 | Font not on the allow-list or too many families | canonical (v3) |
| `CHM_SCHEMA_PROHIBITED_TYPE` | 422 | App. W §W.13 | Prohibited structured-data type | canonical (v3) |
| `CHM_LOCALE_NOT_REVIEWED` | 409 | App. W §W.13 | Locale rendition not reviewed | canonical (v3) |
| `CHM_PUBLISH_APPROVAL_REQUIRED` | 409 | App. W §W.13 | Approval missing or approver = editor | canonical (v3) |
| `CHM_DOMAIN_UNVERIFIED` | 409 | App. W §W.13 | TXT/CNAME not found | canonical (v3) |
| `CHM_DOMAIN_IN_USE` | 409 | App. W §W.13 | Host attached to another tenant | canonical (v3) |
| `CHM_DOMAIN_CAA_BLOCKS_ISSUANCE` | 422 | App. W §W.13 | CAA records block the CA | canonical (v3) |
| `CHM_ENTITLEMENT_REQUIRED` | 403 | App. W §W.13 | Plan or add-on does not include the feature | canonical (v3) |
| `CHM_SPONSORED_INELIGIBLE` | 422 | App. W §W.13 | Not eligible for sponsored placement; reasons in `detail` | canonical (v3) |
| `CHM_EQUATOR_ENDORSEMENT_CLAIM` | 422 | App. W §W.13 | Copy implies Equator endorsement or administration | canonical (v3) |
| `CHM_TEMPLATE_LOCKED_BLOCK_REMOVED` | 422 | App. W §W.13 | Locked template block missing | canonical (v3) |
| `CHM_AWARD_TEMPLATE_INCOMPLETE` | 422 | App. W §W.13 | s.31 required element missing | canonical (v3) |
| `CHM_FEE_PROHIBITED_STRUCTURE` | 422 | App. W §W.13 | Fee structure prohibited (maps to NN-18 validator) | canonical (v3) |
| `CHM_NUMBERING_FORMAT_INVALID` | 422 | App. W §W.13 | Pattern lacks `{PFX}`/`{SEQ}` or too long | canonical (v3) |
| `CHM_NUMBERING_IMMUTABLE` | 409 | App. W §W.13 | Format already used | canonical (v3) |
| `CHM_INVOICE_SERIES_INVALID` | 422 | App. W §W.13 | Series breaches CGST Rules r.46(b) | canonical (v3) |
| `CHM_GSTIN_INVALID` | 422 | App. W §W.13 | GSTIN format, checksum or PAN mismatch | canonical (v3) |
| `CHM_STATUS_LABEL_PROHIBITED` | 422 | App. W §W.13 | Status label prohibited or changes legal meaning | canonical (v3) |
| `CHM_LEGAL_APPROVER_REQUIRED` | 409 | App. W §W.13 | G change needs `chm.config.approve.legal` | canonical (v3) |
| `CHM_ROLE_SOD_CONFLICT` | 409 | App. W §W.13 | Role or delegation creates a separation-of-duties conflict | canonical (v3) |
| `CHM_CONFIDENTIALITY_WALL` | 403 | App. W §W.13 | HR/accounts role requested case content, or case role requested HR data | canonical (v3) |
| `CHM_SALARY_ACCESS_DENIED` | 403 | App. W §W.13 | No salary scope | canonical (v3) |
| `CHM_DELEGATION_SCOPE_EXCEEDED` | 403 | App. W §W.13 | Delegation beyond delegator's scope | canonical (v3) |
| `CHM_SEAT_LIMIT` | 403 | App. W §W.13 | No seat available | canonical (v3) |
| `CHM_STAFF_CONFLICT_DECLARED` | 403 | App. W §W.13 | Assignment blocked by declared conflict | canonical (v3) |
| `CHM_ENGAGEMENT_MISCLASSIFICATION_WARNING` | 409 | App. W §W.13 | Engagement looks like employment; acknowledgement required | canonical (v3) |
| `CHM_LEAVE_POLICY_BELOW_FLOOR` | 422 | App. W §W.13 | Leave policy less generous than statutory floor (maps to `HR_LEAVE_POLICY_BELOW_FLOOR`) | sub-code (`rule`) of `HR_LEAVE_POLICY_BELOW_FLOOR` |
| `CHM_MONITORING_PROHIBITED` | 403 | App. W §W.13 | Prohibited monitoring requested (maps to `HR_MONITORING_PROHIBITED`) | sub-code (`rule`) of `HR_MONITORING_PROHIBITED` |
| `CHM_PAYRUN_PARAM_UNCONFIRMED` | 409 | App. W §W.13 | A rule-pack parameter used is `NOT_CONFIRMED` (maps to `PAY_PARAM_NOT_CONFIRMED`) | sub-code (`rule`) of `PAY_PARAM_NOT_CONFIRMED` |
| `CHM_PAYRUN_DEDUCTION_CAP` | 422 | App. W §W.13 | Deductions exceed 50% of wages (maps to `PAY_DEDUCTION_CAP_EXCEEDED`) | sub-code (`rule`) of `PAY_DEDUCTION_CAP_EXCEEDED` |
| `CHM_PAYRUN_GHOST_HIT_UNRESOLVED` | 409 | App. W §W.13 | Critical integrity hit unresolved (maps to `PAY_GHOST_HITS_UNRESOLVED`) | sub-code (`rule`) of `PAY_GHOST_HITS_UNRESOLVED` |
| `CHM_PAYRUN_DEADLINE` | 422 | App. W §W.13 | Pay date after statutory deadline | canonical (v3) |
| `CHM_STATUTORY_DUES_WAIVER` | 422 | App. W §W.13 | Attempt to waive statutory dues (maps to canonical `STATUTORY_WAIVER_FORBIDDEN`; F alias `WRK_STATUTORY_DUES_WAIVER`) | sub-code (`rule`) of `STATUTORY_WAIVER_FORBIDDEN` |
| `CHM_MAKER_CHECKER_SAME_USER` | 403 | App. W §W.13 | Checker equals maker outside D3-18 (maps to `CTL_SELF_APPROVAL_BLOCKED`) | sub-code (`rule`) of `CTL_SELF_APPROVAL_BLOCKED` |
| `CHM_SINGLE_PERSON_GAP` | 409 | App. W §W.13 | D3-18 minimum gap or hold not elapsed | canonical (v3) |
| `CHM_STEP_UP_REQUIRED` | 401 | App. W §W.13 | Phishing-resistant step-up needed | canonical (v3) |
| `CHM_BANK_CHANGE_COOLING` | 409 | App. W §W.13 | Account in cooling period or pre-pay freeze (maps to `CTL_COOLING_OFF_ACTIVE`) | sub-code (`rule`) of `CTL_COOLING_OFF_ACTIVE` |
| `CHM_BANK_NAME_MISMATCH` | 422 | App. W §W.13 | Penny-drop name match below threshold (maps to `CTL_PENNY_DROP_MISMATCH`) | sub-code (`rule`) of `CTL_PENNY_DROP_MISMATCH` |
| `CHM_DISBURSAL_FILE_HASH_MISMATCH` | 409 | App. W §W.13 | Acknowledgement does not match generated file (maps to `PAY_BANK_FILE_HASH_MISMATCH`) | sub-code (`rule`) of `PAY_BANK_FILE_HASH_MISMATCH` |
| `CHM_PAYOUT_ACCOUNT_NOT_TENANT_OWNED` | 422 | App. W §W.13 | Payout account not owned by the chambers | canonical (v3) |
| `CHM_EXPORT_SCOPE_DENIED` | 403 | App. W §W.13 | Export scope not permitted | canonical (v3) |
| `CHM_OFFBOARDING_OPEN_MATTERS` | 409 | App. W §W.13 | Step blocked while matters are open (run-off continues) | canonical (v3) |
| `OPS_CASE_FIELD_FORBIDDEN` | 422 | App. X §X.18 | A projection, import or field tried to carry non-allow-listed case data | canonical (v3) |
| `OPS_ACCESS_DENIED_CASE_CONTENT` | 403 | App. X §X.18 | Ops principal requested case content or sealed/HR data | canonical (v3) |
| `OPS_ETHICAL_WALL` | 403 | App. X §X.18 | Group ethical-wall denial | canonical (v3); Operations Platform specialisation of `GRP_ETHICAL_WALL_CONFLICT` (AD-R5) |
| `OPS_COMMERCIAL_DATA_FORBIDDEN` | 403 | App. X §X.18 | Case or neutral role requested commercial data (D3-24) | canonical (v3) |
| `OPS_SEGMENT_SOURCE_FORBIDDEN` | 422 | App. X §X.18 | Segment predicate uses a forbidden source | canonical (v3) |
| `OPS_FIELD_PROHIBITED` | 422 | App. X §X.18 | Custom field on a prohibited attribute | canonical (v3) |
| `OPS_SUPPRESSED_CONTACT` | 409 | App. X §X.18 | Contact suppressed (respondent hash, DND, opt-out) | canonical (v3) |
| `OPS_CONSENT_EVIDENCE_REQUIRED` | 422 | App. X §X.18 | Marketing eligibility or import without consent artefact | canonical (v3) |
| `OPS_DUPLICATE_RECORD` | 409 | App. X §X.18 | Exact-duplicate rule matched | canonical (v3) |
| `OPS_CROSS_COMPANY_MERGE` | 422 | App. X §X.18 | Merge across companies | canonical (v3) |
| `OPS_UNMERGE_WINDOW_EXPIRED` | 409 | App. X §X.18 | Un-merge after window | canonical (v3) |
| `OPS_IMPORT_SOURCE_PROHIBITED` | 422 | App. X §X.18 | Bar roll / institute directory / scraped source | canonical (v3) |
| `OPS_IMPORT_RECONCILIATION_MISMATCH` | 409 | App. X §X.18 | Commit counts differ from dry-run | canonical (v3) |
| `OPS_PRODUCT_NOT_SELLABLE` | 422 | App. X §X.18 | Stream disabled, killed or neutrality-restricted | canonical (v3) |
| `OPS_DISCOUNT_APPROVAL_REQUIRED` | 409 | App. X §X.18 | Discount above band | canonical (v3) |
| `OPS_STAGE_GATE_UNMET` | 422 | App. X §X.18 | Opportunity stage gate unmet | canonical (v3) |
| `OPS_PAID_PLACEMENT_FORBIDDEN` | 422 | App. X §X.18 | Placement quoted to an advocate/CA/CS/CMA or while flag OFF (NN-34) | canonical (v3) |
| `OPS_GOLIVE_SIGNOFF_INCOMPLETE` | 409 | App. X §X.18 | Go-live without required signatures/probes | canonical (v3) |
| `OPS_QBR_CONTENT_BLOCKED` | 422 | App. X §X.18 | QBR or leadership pack contains banned content (outcome rates as performance, neutral names, matter details) | canonical (v3) |
| `OPS_TICKET_CATEGORY_LOCKED` | 422 | App. X §X.18 | Top-level category change not permitted | canonical (v3) |
| `OPS_CASE_LINK_UNVERIFIED` | 403 | App. X §X.18 | Case link not chosen by the requester from their own cases | canonical (v3) |
| `OPS_AI_DRAFT_REQUIRES_REVIEW` | 409 | App. X §X.18 | Attempt to send an unreviewed AI draft | canonical (v3) |
| `OPS_GRIEVANCE_CLOCK_LOCKED` | 422 | App. X §X.18 | Attempt to pause/extend a statutory clock | canonical (v3) |
| `OPS_COMPLAINT_NOT_TRACKED` | 409 | App. X §X.18 | Activity records a complaint without a ticket link | canonical (v3) |
| `OPS_AUTOMATION_APPROVAL_REQUIRED` | 422 | App. X §X.18 | Automation reaches an approval-list action without an approval step | canonical (v3) |
| `OPS_AUTOMATION_LOOP` | 409 | App. X §X.18 | Loop or chain depth exceeded | canonical (v3) |
| `OPS_AUTOMATION_RATE_LIMITED` | 429 | App. X §X.18 | Automation rate limit | canonical (v3) |
| `OPS_CONNECTOR_REHEARSAL_MISSING` | 409 | App. X §X.18 | Connector activation without a passed rehearsal in `cfg.migration_rehearsals` (with AC's `CFG_SOR_UNDECLARED` / `CFG_MAPPING_MISSING`) | canonical (v3) |
| `OPS_CONNECTOR_DISABLED` | 409 | App. X §X.18 | Connector flag OFF | canonical (v3) |
| `OPS_WEBHOOK_UNVERIFIED` | 401 | App. X §X.18 | Inbound webhook failed verification | canonical (v3) |
| `OPS_SOR_CHANGE_FORBIDDEN` | 422 | App. X §X.18 | Attempt to make an external tool system of record for consent | canonical (v3) |
| `OPS_EXPORT_APPROVAL_REQUIRED` | 409 | App. X §X.18 | Export above personal-data threshold without checker | canonical (v3) |
| `OPS_GRANT_REQUIRED` | 403 | App. X §X.18 | Cross-company action without Appendix AD grant | canonical (v3) |
| `OPS_MEETING_CLASS_NOT_PERMITTED` | 422 | App. AC §AC.16 | This meeting must be held in an Equator hearing room. | canonical (v3) |
| `OPS_MEETING_HOST_TENANT_IS_PARTY` | 409 | App. AC §AC.16 | A meeting cannot be hosted in a party's own workspace. | canonical (v3) |
| `MKT_CLAIM_UNRESOLVED` | 422 | App. Y §Y.17 | A claim in this content is missing, inactive or expired. | canonical (v3) |
| `MKT_LINT_BLOCKED` | 422 | App. Y §Y.17 | This content breaks a publishing rule. See the lint report. | canonical (v3) |
| `MKT_REVIEW_REQUIRED` | 409 | App. Y §Y.17 | This item needs the review shown before it can move on. | canonical (v3) |
| `MKT_SELF_APPROVAL` | 403 | App. Y §Y.17 | You cannot approve an item you created or reviewed earlier. | canonical (v3) |
| `MKT_CASE_DATA_REJECTED` | 422 | App. Y §Y.17 | Case data cannot be used in marketing. | canonical (v3) |
| `MKT_CONSENT_MISSING` | 409 | App. Y §Y.17 | No valid marketing consent for this contact and purpose. | canonical (v3) |
| `MKT_SUPPRESSED_RECIPIENT` | 409 | App. Y §Y.17 | This contact is suppressed from marketing. | canonical (v3) |
| `MKT_FREQUENCY_CAP` | 409 | App. Y §Y.17 | This contact has reached the message limit for this period. | canonical (v3) |
| `MKT_QUIET_HOURS` | 409 | App. Y §Y.17 | Messages cannot be sent at this time. | canonical (v3) |
| `MKT_DLT_TEMPLATE_UNREGISTERED` | 422 | App. Y §Y.17 | The SMS template is not registered for promotional use. | canonical (v3) |
| `MKT_SENDER_DOMAIN_UNVERIFIED` | 409 | App. Y §Y.17 | The sending domain failed authentication checks. | canonical (v3) |
| `MKT_MASS_SEND_APPROVAL_REQUIRED` | 409 | App. Y §Y.17 | A second approver is needed for this send. | canonical (v3) |
| `MKT_BUDGET_APPROVAL_REQUIRED` | 409 | App. Y §Y.17 | This budget needs approval at a higher level. | canonical (v3) |
| `MKT_BUDGET_EXHAUSTED` | 409 | App. Y §Y.17 | The budget line is fully used. | canonical (v3) |
| `MKT_ASSET_RIGHTS_EXPIRED` | 409 | App. Y §Y.17 | An asset's usage rights have expired. | canonical (v3) |
| `MKT_ASSET_CONSENT_MISSING` | 409 | App. Y §Y.17 | A person shown in this asset has not consented. | canonical (v3) |
| `MKT_COBRAND_NOT_APPROVED` | 409 | App. Y §Y.17 | Co-branding for this partner is not approved. | canonical (v3) |
| `MKT_PROHIBITED_TECHNIQUE` | 422 | App. Y §Y.17 | This marketing technique is not allowed. | canonical (v3) |
| `MKT_COUNTDOWN_NOT_FIXED` | 422 | App. Y §Y.17 | Countdowns must use a fixed end time from an event or offer. | canonical (v3) |
| `MKT_SCARCITY_UNBOUND` | 422 | App. Y §Y.17 | Availability claims must come from a real capacity record. | canonical (v3) |
| `MKT_PRICE_CLAIM_UNBOUND` | 422 | App. Y §Y.17 | Prices must come from a published fee schedule or plan. | canonical (v3) |
| `MKT_TESTIMONIAL_UNVERIFIED` | 422 | App. Y §Y.17 | Testimonials need a verified, consented claim record. | canonical (v3) |
| `MKT_ADVOCATE_REWARD_BLOCKED` | 403 | App. Y §Y.17 | Referral rewards cannot be given to advocates, CAs, CSs or CMAs. | canonical (v3) |
| `MKT_SENSITIVE_TARGETING_BLOCKED` | 403 | App. Y §Y.17 | This targeting attribute is not allowed. | canonical (v3) |
| `MKT_EXPERIMENT_PROHIBITED_SURFACE` | 422 | App. Y §Y.17 | Experiments are not allowed on this surface. | canonical (v3) |
| `MKT_UTM_INVALID` | 400 | App. Y §Y.17 | The tracking link does not follow the convention. | canonical (v3) |
| `MKT_HANDOFF_INCOMPLETE` | 422 | App. Y §Y.17 | The hand-off package is missing required fields. | canonical (v3) |
| `MKT_PUBLISH_EVIDENCE_REQUIRED` | 409 | App. Y §Y.17 | Record the post URL and screenshot to complete publication. | canonical (v3) |
| `MKT_SOCIAL_ADAPTER_DISABLED` | 409 | App. Y §Y.17 | Publishing through this platform connection is switched off. | canonical (v3) |
| `MKT_PLATFORM_LIMIT_REACHED` | 429 | App. Y §Y.17 | The platform's posting limit has been reached. | canonical (v3) |
| `MKT_CRISIS_PAUSE_ACTIVE` | 409 | App. Y §Y.17 | Publishing is paused while a crisis is open. | canonical (v3) |
| `MKT_EMBARGO_ACTIVE` | 409 | App. Y §Y.17 | This release is under embargo. | canonical (v3) |
| `MKT_MOU_LEGAL_REVIEW_REQUIRED` | 409 | App. Y §Y.17 | This agreement needs legal review before approval. | canonical (v3) |
| `MKT_GROUP_SCOPE_NOT_GRANTED` | 403 | App. Y §Y.17 | No cross-company grant covers this data. | canonical (v3) |
| `MKT_ATTRIBUTION_MODEL_UNAPPROVED` | 409 | App. Y §Y.17 | This attribution model version is not approved. | canonical (v3) |
| `MKT_COMPETITOR_FIGURE_BLOCKED` | 422 | App. Y §Y.17 | A competitor figure that is self-reported, third-party or past its re-verification date cannot be published (Appendix AF FR-P13-V3-AF02). | canonical (v3) |
| `HR_REQUISITION_BUDGET_EXCEEDED` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_REPORTING_CYCLE` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_WORKER_CLASSIFICATION_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_APPOINTMENT_LETTER_MISSING` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_PREJOIN_CHECKS_INCOMPLETE` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_POLICY_ACK_PENDING` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_SECONDMENT_RECORD_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_DUPLICATE_ACTIVE_EMPLOYMENT` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_ENTITY_TRANSFER_REQUIRES_REJOIN` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_FIELD_NOT_VISIBLE` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_LEAVE_POLICY_BELOW_FLOOR` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_LEAVE_BALANCE_INSUFFICIENT` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_OVERTIME_CONSENT_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_OVERTIME_QUARTERLY_CAP` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_NIGHT_WORK_CONSENT_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_MONITORING_PROHIBITED` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_MONITORING_APPROVAL_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_REGULARISATION_WINDOW_CLOSED` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_METRIC_OUTCOME_FORBIDDEN` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_PIP_SAFEGUARD_MISSING` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_CERTIFICATION_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `HR_WORKSPACE_SKU_INSUFFICIENT` | 409 | App. Z §Z.17.3 | (alias `WORKSPACE_SKU_INSUFFICIENT_FOR_ROLE`) | canonical (v3) |
| `HR_WORKSPACE_DELETE_BLOCKED_HOLD` | 409 | App. Z §Z.17.3 | (alias `WORKSPACE_DELETE_BLOCKED_HOLD`) | canonical (v3) |
| `HR_EXIT_CLEARANCE_PENDING` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_DEDUCTION_CAP_EXCEEDED` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_FINE_EVIDENCE_MISSING` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_COMPONENT_CLASS_LOCKED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_RUN_LOCKED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_RUN_VARIANCE_UNREVIEWED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_MAKER_CHECKER_SAME_USER` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_GHOST_HITS_UNRESOLVED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_BANK_FILE_HASH_MISMATCH` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_REGIME_LOCKED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_PROOF_WINDOW_CLOSED` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_GL_PERIOD_LOCKED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_PARAM_NOT_CONFIRMED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_PARAM_ACK_REQUIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_WAGE_DEFINITION_BREACH` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `PAY_MIN_WAGE_BREACH` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_AUTHORITY_LIMIT_EXCEEDED` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_SELF_APPROVAL_BLOCKED` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_SOD_CONFLICT` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_APPROVER_CONFLICTED` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_PAYLOAD_CHANGED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_COOLING_OFF_ACTIVE` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_OOB_CONFIRMATION_PENDING` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_PENNY_DROP_MISMATCH` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_DUPLICATE_BANK_ACCOUNT` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_VENDOR_KYC_INCOMPLETE` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_COI_UNDECLARED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_EXCEPTION_REASON_REQUIRED` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_APPROVAL_EXPIRED` | 409 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_PETTY_CASH_LIMIT` | 422 | App. Z §Z.17.3 | — | canonical (v3) |
| `CTL_AUDIT_WORKSPACE_READ_ONLY` | 403 | App. Z §Z.17.3 | — | canonical (v3) |
| `MKP_PAID_PLACEMENT_OFF` | 409 | App. AA §AA.20 | Sponsored listings are not enabled | canonical (v3) |
| `MKP_SPONSOR_INELIGIBLE` | 422 | App. AA §AA.20 | Provider fails `sponsor_eligible()` (detail lists condition) | canonical (v3) |
| `MKP_SPONSOR_SLOT_CAP` | 409 | App. AA §AA.20 | No sponsored inventory left for that category-geography-month or sponsor cap reached | canonical (v3) |
| `MKP_SORT_NOT_ALLOWED` | 400 | App. AA §AA.20 | Sort parameter not in the published policy | canonical (v3) |
| `MKP_SURFACE_FORBIDDEN` | 403 | App. AA §AA.20 | Cross-surface access attempted | canonical (v3) |
| `MKP_CATEGORY_DISABLED` | 409 | App. AA §AA.20 | Category law check not signed or category OFF | canonical (v3) |
| `MKP_PROFESSIONAL_NOT_ALLOWED` | 422 | App. AA §AA.20 | Advocate or institute member cannot list in this category (AA.3.2) | canonical (v3) |
| `MKP_LABEL_FORBIDDEN` | 422 | App. AA §AA.20 | Profile or creative contains a forbidden label or claim | canonical (v3) |
| `MKP_PROVIDER_NOT_LISTED` | 409 | App. AA §AA.20 | Provider not in `listed` | canonical (v3) |
| `MKP_CONFLICT_HARD` | 409 | App. AA §AA.20 | Hard conflict found | canonical (v3) |
| `MKP_ONE_PARTY_ARBITRATION_BLOCKED` | 422 | App. AA §AA.20 | Arbitrator booking needs every party | canonical (v3) |
| `MKP_REPEAT_PLAYER_ARBITRATION_BLOCKED` | 422 | App. AA §AA.20 | Repeat-player vs individual arbitration on surface (ii) | canonical (v3) |
| `MKP_ENTERPRISE_NEUTRAL_PROCUREMENT_BLOCKED` | 403 | App. AA §AA.20 | Enterprises cannot procure neutrals for their own disputes | canonical (v3) |
| `MKP_FEE_DISCLOSURE_REQUIRED` | 409 | App. AA §AA.20 | Confirmation attempted without accepted fee disclosure | canonical (v3) |
| `MKP_BOOKING_CONFIRMATION_REQUIRED` | 422 | App. AA §AA.20 | Explicit confirmation missing | canonical (v3) |
| `MKP_TAX_MEMO_MISSING` | 409 | App. AA §AA.20 | Paid bookings blocked until tax memo recorded | canonical (v3) |
| `MKP_PAYOUT_SOD_VIOLATION` | 403 | App. AA §AA.20 | Separation of duties breached | canonical (v3) |
| `MKP_PAYEE_COOLING_OFF` | 409 | App. AA §AA.20 | Payee in cooling-off | canonical (v3) |
| `MKP_REVIEW_NOT_ELIGIBLE` | 403 | App. AA §AA.20 | Reviewer not a participant of a completed engagement | canonical (v3) |
| `MKP_REVIEW_OUTCOME_ITEM` | 422 | App. AA §AA.20 | Review form contains an outcome item | canonical (v3) |
| `MKP_REVIEW_PROFESSIONAL_FORBIDDEN` | 422 | App. AA §AA.20 | Reviews not allowed for this provider type | canonical (v3) |
| `MKP_REASONS_REQUIRED` | 422 | App. AA §AA.20 | Enforcement decision without reasons | canonical (v3) |
| `MKP_AD_CATEGORY_PROHIBITED` | 422 | App. AA §AA.20 | Advertiser category not allowed | canonical (v3) |
| `MKP_AD_PLACEMENT_FORBIDDEN` | 422 | App. AA §AA.20 | Ad slot on a prohibited page tag | canonical (v3) |
| `MKP_ADVOCATE_TARIFF_FORBIDDEN` | 422 | App. AA §AA.20 | Tariff tag for advocate commission, listing, lead or referral | canonical (v3) |
| `MKP_DARK_PATTERN_AUDIT_OVERDUE` | 409 | App. AA §AA.20 | Annual self-audit not certified | canonical (v3) |
| `DIR_CONSENT_REQUIRED` | 403 | App. AA §AA.20 | No consent for this use | canonical (v3) |
| `DIR_PURPOSE_NOT_GRANTED` | 403 | App. AA §AA.20 | Purpose not granted to consumer or recipient | canonical (v3) |
| `DIR_GDSA_MISSING` | 403 | App. AA §AA.20 | Consumer has no active GDSA | canonical (v3) |
| `DIR_FIELD_NOT_ALLOWED` | 422 | App. AA §AA.20 | Field outside the type allow-list | canonical (v3) |
| `DIR_SORT_NOT_ALLOWED` | 400 | App. AA §AA.20 | Sort other than alphabetical/seeded-random | canonical (v3) |
| `DIR_BULK_IMPORT_FORBIDDEN` | 422 | App. AA §AA.20 | Bulk creation of records attempted | canonical (v3) |
| `DIR_SOURCE_BLOCKED` | 422 | App. AA §AA.20 | Source host is a blocked roll portal | canonical (v3) |
| `DIR_VERIFIER_SAME_PERSON` | 403 | App. AA §AA.20 | Second verifier same as first | canonical (v3) |
| `DIR_RECORD_STALE` | 409 | App. AA §AA.20 | Record hidden for freshness | canonical (v3) |
| `DIR_PUBLIC_SEARCH_OFF` | 404 | App. AA §AA.20 | Public professional search disabled | canonical (v3) |
| `DIR_TENANT_SCOPE` | 403 | App. AA §AA.20 | Tenant-private data outside its tenant | canonical (v3) |
| `DIR_PER_ENGAGEMENT_PRICING_FORBIDDEN` | 422 | App. AA §AA.20 | Panel pricing by engagement, referral or success | canonical (v3) |
| `DIR_REFERRAL_REWARD_FORBIDDEN` | 422 | App. AA §AA.20 | Reward to a professional for referral | canonical (v3) |
| `REV_STREAM_NOT_FOUND` | 404 | App. AB §AB.12 | Unknown stream code | canonical (v3) |
| `REV_STREAM_NOT_LIVE` | 409 | App. AB §AB.12 | Stream not live in the caller's scope; sale, quote or render refused | canonical (v3) |
| `REV_STREAM_PROHIBITED` | 422 | App. AB §AB.12 | N4 / deny-list stream cannot be approved or priced | canonical (v3) |
| `REV_KILL_SWITCH_ACTIVE` | 423 | App. AB §AB.12 | Kill switch engaged for this scope | canonical (v3) |
| `REV_TRANSITION_INVALID` | 409 | App. AB §AB.12 | Transition not allowed from current status | canonical (v3) |
| `REV_MAKER_CHECKER_SAME_USER` | 403 | App. AB §AB.12 | Checker equals maker (NN-36) | canonical (v3) |
| `REV_COUNSEL_OPINION_REQUIRED` | 422 | App. AB §AB.12 | Counsel opinion dependency not satisfied | canonical (v3) |
| `REV_BOARD_RESOLUTION_REQUIRED` | 422 | App. AB §AB.12 | Board resolution reference missing | canonical (v3) |
| `REV_RELATED_PARTY_APPROVAL_REQUIRED` | 422 | App. AB §AB.12 | s.188 approval reference missing (RA-13) | canonical (v3) |
| `REV_TAX_MEMO_REQUIRED` | 422 | App. AB §AB.12 | Tax profile pending for a B2C scope | canonical (v3) |
| `REV_PRICE_OUT_OF_BOUNDS` | 422 | App. AB §AB.12 | Schedule or test arm outside approved bounds | canonical (v3) |
| `REV_PRICE_TEST_NOT_PERMITTED` | 422 | App. AB §AB.12 | Flag OFF, consumer scope, or prohibited line (PT-1) | canonical (v3) |
| `REV_SCOPE_NOT_PERMITTED` | 422 | App. AB §AB.12 | Case scope or segment not allowed for the rating | canonical (v3) |
| `REV_JURISDICTION_NOT_ENABLED` | 422 | App. AB §AB.12 | No published rule pack for the state or country | canonical (v3) |
| `REV_PROFESSIONAL_RULE_BLOCK` | 422 | App. AB §AB.12 | Master X-62 / deny X-21–X-22 violation | canonical (v3) |
| `REV_NEUTRALITY_CONFLICT` | 422 | App. AB §AB.12 | Attempted read path or bundle that breaches RA-11 | canonical (v3) |
| `REV_TENANT_NOT_CONFIGURABLE` | 403 | App. AB §AB.12 | Tenant tried to change a non-tenant-configurable stream | canonical (v3) |
| `REV_COUPON_INVALID` | 422 | App. AB §AB.12 | Expired, exhausted, wrong audience or ineligible line | canonical (v3) |
| `REV_COUPON_DARK_PATTERN` | 422 | App. AB §AB.12 | Coupon breaches CP-1…CP-7 | canonical (v3) |
| `REV_PACKAGE_ITEM_NOT_LIVE` | 409 | App. AB §AB.12 | A package item's stream is not live | canonical (v3) |
| `REV_MARGIN_GUARDRAIL_BREACH` | 422 | App. AB §AB.12 | Price below floor without the required approver | canonical (v3) |
| `REV_COST_DATA_RESTRICTED` | 403 | App. AB §AB.12 | Private cost or margin fields requested without grant | canonical (v3) |
| `REV_EXPLANATION_STALE` | 409 | App. AB §AB.12 | Explanation page source version not live | canonical (v3) |
| `REV_RUNOFF_REQUIRED` | 409 | App. AB §AB.12 | Retirement attempted with open obligations and no run-off plan | canonical (v3) |
| `GRP_ENTITY_ACCESS_DENIED` | 403 | App. AD §AD.15.3 | This record belongs to another company in the group. | canonical (v3) |
| `GRP_GRANT_REQUIRED` | 403 | App. AD §AD.15.3 | Access to another company's data needs an approved, current grant. | canonical (v3) |
| `GRP_GRANT_SELF_APPROVAL` | 409 | App. AD §AD.15.3 | You cannot approve your own access request. | canonical (v3) |
| `GRP_GRANT_DURATION_EXCEEDED` | 422 | App. AD §AD.15.3 | Access can be granted for a limited period only. | canonical (v3) |
| `GRP_GDSA_REQUIRED` | 409 | App. AD §AD.15.3 | A current data-sharing agreement is needed for this purpose. | canonical (v3) |
| `GRP_PURPOSE_NOT_ALLOWED` | 422 | App. AD §AD.15.3 | This purpose does not allow the requested data. | canonical (v3) |
| `GRP_MODULE_NOT_SHAREABLE` | 422 | App. AD §AD.15.3 | Case, neutral and allocation data are never shared across companies. | canonical (v3) |
| `GRP_ROLE_NOT_GRANTABLE` | 422 | App. AD §AD.15.3 | This role cannot be granted across companies. | canonical (v3) |
| `GRP_ETHICAL_WALL_CONFLICT` | 409 | App. AD §AD.15.3 | You cannot work on this matter because of a conflict of interest. | canonical (v3) |
| `GRP_DUPLICATE_EMPLOYMENT` | 409 | App. AD §AD.15.3 | This person is already employed in the group; record a secondment instead. | canonical (v3) |
| `GRP_ICSA_NOT_ACTIVE` | 409 | App. AD §AD.15.3 | No active inter-company agreement covers this charge. | canonical (v3) |
| `GRP_RELATED_PARTY_APPROVAL_PENDING` | 409 | App. AD §AD.15.3 | Related-party approval is pending for this agreement. | canonical (v3) |
| `GRP_REFERRAL_AUTHORISATION_MISSING` | 409 | App. AD §AD.15.3 | The party's authorisation is required before this referral. | canonical (v3) |
| `GRP_SHARED_ARTIFACT_FIELD_BLOCKED` | 422 | App. AD §AD.15.3 | This field cannot be shared for the selected purpose. | canonical (v3) |
| `GRP_ATTESTATION_OVERDUE` | 403 | App. AD §AD.15.3 | Complete your annual conflict attestation to continue cross-company work. | canonical (v3) |
| `XPT_SCOPE_NOT_PERMITTED` | 403 | App. AC §AC.16 | You cannot export this scope. | canonical (v3) |
| `XPT_APPROVAL_REQUIRED` | 409 | App. AC §AC.16 | This export needs a second approver. | canonical (v3) |
| `XPT_NAME_INVALID` | 422 | App. AC §AC.16 | A file or folder name is not portable. | canonical (v3) |
| `XPT_PATH_TOO_LONG` | 422 | App. AC §AC.16 | A path exceeds the portable length budget. | canonical (v3) |
| `XPT_SIGNATURE_HASH_MISMATCH` | 500 | App. AC §AC.16 | A signed original does not match its ledger hash. (Critical incident) | canonical (v3) |
| `XPT_AUDIT_EXTRACT_INVALID` | 500 | App. AC §AC.16 | The audit-trail extract failed verification. | canonical (v3) |
| `XPT_EXCLUSION_RULE_VIOLATION` | 500 | App. AC §AC.16 | The package included an item that must be excluded. (Critical incident) | canonical (v3) |
| `XPT_PUSH_VERIFY_FAILED` | 502 | App. AC §AC.16 | Files pushed to the destination did not match the manifest. | canonical (v3) |
| `XPT_ACCOUNTING_PERIOD_REEXPORT_REQUIRED` | 409 | App. AC §AC.16 | This period changed after export; re-export is required. | canonical (v3) |
| `XPT_IMPORT_RECONCILIATION_VARIANCE` | 409 | App. AC §AC.16 | Import totals do not match the source; explain or fix before closing. | canonical (v3) |
| `XPT_IMPORT_SOURCE_FORBIDDEN` | 422 | App. AC §AC.16 | This source cannot be imported. | canonical (v3) |
| `ENG_CHANGE_RECORD_REQUIRED` | 409 | App. AE §AE.13 | A production change needs an approved change record. | canonical (v3) |
| `ENG_CHANGE_NOT_APPROVED` | 409 | App. AE §AE.13 | This change record is not approved for deployment. | canonical (v3) |
| `ENG_SELF_APPROVAL_FORBIDDEN` | 403 | App. AE §AE.13 | You cannot approve a change you requested or authored. | canonical (v3) |
| `ENG_NO_ELIGIBLE_APPROVER` | 409 | App. AE §AE.13 | No eligible approver is available; the change has been escalated. | canonical (v3) |
| `ENG_CONDITIONAL_APPROVAL_MISSING` | 409 | App. AE §AE.13 | A required DPO, legal, finance or case-services approval is missing. | canonical (v3) |
| `ENG_FREEZE_ACTIVE` | 409 | App. AE §AE.13 | A change freeze is active for this service. | canonical (v3) |
| `ENG_WINDOW_CLOSED` | 409 | App. AE §AE.13 | The approved change window is not open. | canonical (v3) |
| `ENG_DIGEST_MISMATCH` | 409 | App. AE §AE.13 | The images being deployed do not match the change record. | canonical (v3) |
| `ENG_STAGING_NOT_VERIFIED` | 409 | App. AE §AE.13 | These images have not been deployed successfully to staging. | canonical (v3) |
| `ENG_GATE_FAILED` | 409 | App. AE §AE.13 | A required release gate (NN suite, AI evals or security scan) has not passed. | canonical (v3) |
| `ENG_OPEN_CRITICAL_VULN` | 409 | App. AE §AE.13 | A critical vulnerability without an approved exception affects this release. | canonical (v3) |
| `ENG_NOTICE_PERIOD_NOT_MET` | 409 | App. AE §AE.13 | The customer notice period for this breaking change has not elapsed. | canonical (v3) |
| `ENG_MIGRATION_LABEL_MISSING` | 422 | App. AE §AE.13 | Migration changes need a migration-risk label. | canonical (v3) |
| `ENG_CONTRACT_MIGRATION_TOO_EARLY` | 409 | App. AE §AE.13 | This contract migration needs the prior release in production for at least 7 days. | canonical (v3) |
| `ENG_RISK_ACCEPTANCE_INVALID` | 422 | App. AE §AE.13 | This exception is not allowed (expiry, approver or NN-control rule). | canonical (v3) |
| `ENG_RETRO_REVIEW_OVERDUE` | 409 | App. AE §AE.13 | An emergency change is overdue for retrospective review. | canonical (v3) |
| `ENG_RULESET_DRIFT` | 409 | App. AE §AE.13 | Repository protection settings differ from the approved baseline. | canonical (v3) |
| `ENG_UNRECORDED_SAAS_CHANGE` | 409 | App. AE §AE.13 | An administrative change was made without a change record. | canonical (v3) |
| `ENG_IMAGE_STALE` | 409 | App. AE §AE.13 | A running image is older than the patch cadence allows. | canonical (v3) |
| `ENG_AUDITOR_GRANT_EXPIRED` | 403 | App. AE §AE.13 | Your audit access has expired. | canonical (v3) |
| `ENG_AUDITOR_SCOPE_EXCEEDED` | 403 | App. AE §AE.13 | This item is outside the scope of your audit engagement. | canonical (v3) |
| `ENG_AUDITOR_DOWNLOAD_CAP` | 429 | App. AE §AE.13 | Daily download limit reached; request an evidence pack instead. | canonical (v3) |
| `ENG_JIT_APPROVAL_REQUIRED` | 403 | App. AE §AE.13 | Production access needs an approved just-in-time grant. | canonical (v3) |
| `ENG_LEDGER_TRAIL_TAMPER_BLOCKED` | 403 | App. AE §AE.13 | Audit-trail controls on ledger tables cannot be changed. | canonical (v3) |
| `ENG_FINDING_VALIDATION_FORBIDDEN` | 403 | App. AE §AE.13 | Only the audit function that raised this finding can validate it. | canonical (v3) |
| `LABEL_PROHIBITED_TERM` | 422 | P10 (label validator; FR-P10-01) | A tenant label or name uses a prohibited term (e.g., "court") | canonical (registered v3.0; parent of `CHM_LABEL_PROHIBITED`) |
| `CLAIM_BENCHMARK_STALE` | 422 | App. T §0.4 rule (a); P13 CMS linter | A comparative claim lacks a public-use benchmark row verified within 90 days | canonical (registered v3.0) |

---

## F.11 API resource map (`/v1`; OpenAPI 3.1 generated from code)

| Context | Top-level resources |
|---|---|
| identity | `/auth/*` (OIDC), `/me`, `/me/memberships`, `/me/devices`, `/devices`, `/push-tokens`, `/mfa-factors`, `/step-up`, `/api-keys`, `/role-grants`, `/break-glass` |
| tenancy / admin | `/tenants`, `/tenants/{id}/domains`, `/tenants/{id}/branding`, `/app/config`, `/feature-flags`, `/admin/*` |
| consent / privacy | `/consents`, `/privacy-notices`, `/dsr`, `/admin/dsr`, `/consent-purposes` |
| kyc / directory | `/persons/{id}/kyc`, `/organisations`, `/organisations/{id}/kyb`, `/organisations/{id}/signatories` |
| intake / forms | `/explorer/sessions`, `/forms/{formId}`, `/form-drafts`, `/forms/{formId}/submissions`, `/routing/evaluate` |
| cases | `/cases`, `/cases/{caseId}` + `/parties`, `/representatives`, `/claims`, `/reliefs`, `/responses`, `/links`, `/scrutiny/decision`, `/deficiencies`, `/routes`, `/signposting-events`, `/timeline`, `/threads`, `/threads/{threadId}/messages` |
| clocks | `/cases/{caseId}/clocks`, `/clocks/{clockId}:extend`, `/clocks/{clockId}:assign-owner`, `/compliance/cockpit` |
| notices | `/cases/{caseId}/notices`, `/notices/{noticeId}/service-attempts`, `/notices/{noticeId}/audio`, `/notices/{noticeId}/acknowledge` |
| documents | `/uploads`, `/cases/{caseId}/documents`, `/documents/{id}/versions`, `/cases/{caseId}/bundles`, `/bundles/{id}:certify`, `/verify/{hash}` (public) |
| neutrals | `/neutrals` (public directory), `/neutral-applications`, `/neutrals/{id}/availability`, `/neutrals/{id}/disclosures`, `/cases/{caseId}/allocation-runs`, `/appointments/{id}:accept|decline`, `/appointments/{id}/challenges`, `/cases/{caseId}/independence-pack` |
| proceedings / hearings | `/cases/{caseId}/proceedings`, `/proceedings/{id}/orders`, `/proceedings/{id}/offers`, `/proceedings/{id}/consents`, `/cases/{caseId}/proceedings/{proceedingId}/sessions`, `/sessions/{id}/join`, `/sessions/{id}/pstn`, `/sessions/{id}/caucus-notes`, `/sessions/{id}/attendance` |
| outcomes / execution | `/cases/{caseId}/settlements`, `/settlements/{id}/terms`, `/settlements/{id}/lint`, `/cases/{caseId}/awards`, `/awards/{id}:sign|seal|release|correct`, `/awards/{id}/appeals`, `/esign-requests`, `/esign-requests/{id}/mobile-launch`, `/estamp-requests`, `/registration-tasks`, `/cases/{caseId}/execution-packs`, `/compliance-obligations` |
| billing / payments / escrow | `/quotes`, `/invoices`, `/invoices/{id}/payment-intents`, `/payments/{id}`, `/refunds`, `/payouts`, `/escrow-accounts`, `/escrow-accounts/{id}/milestones`, `/instalment-plans`, `/fx-rates`, `/plans`, `/subscriptions`, `/fee-schedules` (public read) |
| comms / voice | `/journeys`, `/message-templates`, `/communications` (staff read), `/contact-preferences`, `/contact-blackouts`, `/voice/campaigns`, `/call-records`, `/number-authorisations`, `/admin/number-inventory`, `/admin/telecom-declarations` |
| rules / studio | `/rulesets`, `/ruleset-versions`, `/legal-rules`, `/procedure-rules` (public read), `/document-templates`, `/config-change-requests`, `/config-change-requests/{id}:approve` |
| ai | `/ai/interactions`, `/ai/suggestions/{id}:approve|reject`, `/ai/prompt-versions`, `/ai/eval-runs`, `/ai/kill-switches` |
| enterprise | `/clauses`, `/clause-instances`, `/bulk-jobs`, `/bulk-jobs/{id}/rows`, `/webhook-subscriptions`, `/webhook-deliveries`, `/mis/reports` |
| grm | `/grm/desks`, `/grm/tickets`, `/grm/tickets/{id}/responses`, `/grm/tickets/{id}/odr-offers`, `/grm/odr-offers/{id}/consent`, `/grm/tickets/{id}/external-refs`, `/grm/committees`, `/grm/reports` |
| posh (sealed service, separate base path `/v1/posh`, scope `posh`) | `/posh/ic-constitutions`, `/posh/complaints`, `/posh/complaints/{token}/conciliation`, `/posh/complaints/{token}/inquiry`, `/posh/complaints/{token}/report`, `/posh/annual-reports` |
| chambers / academy / campus | `/chambers/workspaces`, `/chambers/marketplace-listings`, `/academy/courses`, `/academy/cohorts`, `/academy/enrolments`, `/academy/certificates/{code}` (public verify), `/campus/competitions` |
| growth / cms (separate service) | `/cms/pages`, `/cms/claims`, `/growth/leads`, `/growth/referrals`, `/tools/*` (public calculators) |
| ops / audit | `/ops/incidents`, `/ops/security-findings`, `/ops/ropa-entries`, `/ops/dpias`, `/ops/launch-checklist`, `/ops/migration-runs`, `/ops/kpis`, `/audit/events`, `/audit/chain:verify`, `/telemetry/events` |
| webhooks inbound | `/webhooks/{provider}` (signature-verified; `core.webhook_inbox` unique `(provider, external_event_id)`) |

Conventions: cursor pagination (`limit` ≤ 100, `cursor`), allow-listed filters, `Idempotency-Key` on POST that creates money, notices, cases, signatures or messages, `If-Match` on mutable aggregates, the gateway-signed `Equator-Context` header (tenant, acting role, acting case — master X-01; P01) for multi-tenant users, with the server re-validating membership, custom methods as `:verb` suffix. `X-Tenant-Id` is not used.

---

## F.12 Open items

1. **UUID function naming** differs across phases (`core.uuid_v7()`, `uuidv7()`, `uuid_generate_v7()`); resolved by aliases in F.2 — new DDL uses `uuidv7()` (master X-10).
2. **P07 `core.communications`** has the partitioned-table PK defect; F.4.10 supersedes it.
3. **Evidence ledger** defined twice (P00 storage-centric, P02 per-case chain); F.4.6 merges them with `ledger_scope` — both phases' migrations must use F.4.6.
4. P12 and P14 describe new tables with `<entity>_id` primary-key column names in prose; implement with `id` per F.1.1.
5. Resolved: cooling period = Board policy with a 12-month floor (NBFC Resolution of Stressed Assets Directions 2025, para 95; technical write-offs per Board policy, para 96). Borrower copy may say 'at least 12 months, per lender policy'.
6. Error-code set is large by design; any code added in a phase must be registered in F.10 (CI check) — current phase files use ~60 vertical sub-codes mapped in F.10.2.
7. **M-05/M-06 additions** (F.4.14): `ops.telecom_declarations`, `core.number_inventory`, `core.number_authorisations`, `core.telecom_consent_registrations`, `core.contact_points.dnd_checked_at`, `com.pims_referrals`; flags `voice.equator_service_number.enabled` and `com.s12a_equator_authorised`; events #164–167; codes `CLI_NOT_AUTHORISED`, `TELECOM_CONSENT_NOT_REGISTERED`. P07 and P08 migrations must use these definitions.
8. **v3.0 schema `ops` (23 Oct 2026; master X-50, X-65).** From v3.0 `ops` means the business Operations Platform only (Appendix X, business database). The v2.1 platform-assurance and compliance-operations tables named in this appendix and in Appendix Q / P14 under `ops` (incidents, security findings, RoPA, DPIAs, launch checklist, migration runs, KPIs, regulatory notifications, telecom declarations in F.4.14) are created in schema `eng` in the core database with unchanged table names (`ops.security_findings` → `eng.vulnerabilities`; `ops.processed_events` → `core.processed_events`); API paths `/v1/ops/...` in F.11 become `/v1/eng/...` behind a gateway 308 redirect for v3.0, and no alias may shadow an Operations Platform route under `/v1/ops/*`. `ops.telecom_declarations` is not named in X-65; it is placed in `eng` by X-50's rule that no assurance table may be created in `ops` (confirm in an ADR).
9. **v3.0 schemas** `cfg`, `chm`, `ops`, `mkt`, `hr`, `pay`, `ctl`, `mkp`, `dir`, `rev`, `grp`, `xpt`, `eng` are specified (DDL additive to this appendix) in Appendices V, W, X, Y, Z, AA, AB, AC, AD and AE; `ops` and `mkt` live in the isolated business database with `growth` (D3-20); `dir` lives in the registry owner's separate cluster (Appendix AA §AA.2.3).
