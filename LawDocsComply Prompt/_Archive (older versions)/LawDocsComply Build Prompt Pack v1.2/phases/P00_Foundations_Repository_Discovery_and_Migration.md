# Phase P00 — Foundations, Repository Discovery and Migration

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** none (first phase). Reads the live lawdocscomply.com repository and production data (read-only), the Infrabyx Ecosystem Integration Specification v1.1 (committed unchanged as `docs/ecosystem/infrabyx-integration-spec.md`) and the Operations Hub Master Prompt v1.0 (reference copy `docs/ecosystem/ops-hub-master-prompt.md`).
>
> **Sequencing:** P00 → P01 → P02 (P02 starts in parallel from P01 sprint 2). Every later phase builds on the platform core delivered here. The data migration of §4.9 runs in three waves: wave 1 (content and question banks) inside P00; wave 2 (tenants, users, compliance records) at the P01 exit; wave 3 (documents and evidence) at the P07 exit. The legacy application stays live and read-write until cut-over (§5.5).
>
> **Binding appendices:** B (data model, events, error codes), Q (security, privacy, certification readiness), A (core state machines: correction entry, change request, break-glass), U (configuration framework — the `cfg` heads created here), M (export package; NN-10 contract test skeleton created here).
>
> **Requirements covered:** R-001, R-002, R-003, R-021 (storage foundations), R-031, R-033 (foundations), R-046 (CI/CD skeleton), R-068, R-071, R-074, R-075, R-081 (foundations), R-101 (verification tooling).
>
> **Decisions applied:** D-01, D-02, D-07, D-09, D-12, D-13, D-21.
>
> **Estimated effort:** 5 two-week sprints *(v1.2: +1 for the business-ID registry, aliases, lineage and the ledger keyed by business ID)*, squad of 7 (tech lead, 2 backend, 1 frontend, 1 platform/DevOps, 1 data-migration engineer, 1 QA/security engineer) plus a part-time product owner and the Company Secretary as content owner for wave 1.

> **v1.2 changes (25 October 2026)**
> - Business reference ID registry: `packages/bizid` parser and formatter, transactional allocator, segment registries (instrument codes, tenant codes, entity codes), lifecycle (reserve, activate, burn, retire, merge, split, continue), aliases and legacy IDs (FR-P00-70 to FR-P00-74; D-51, D-52, NN-56; Appendix B §B.12)
> - Ledger keyed by business ID with history index, History API, `<HistoryTimeline>` component, universal resolver and deep links (FR-P00-75 to FR-P00-77; NN-57)
> - Cross-ID links service for CompID ↔ RiskID ↔ GovID ↔ KRI/Control/AUD/LIT/ESG (FR-P00-78)
> - New screens SCR-CORE-10 and SCR-CORE-11; v1.2 settings, events, error codes, Gherkin and open items OI-P00-13 to OI-P00-15

> **v1.1 changes (25 October 2026)**
> - Region-cell architecture with a thin global control plane; IN live, EU/GCC/SG/US defined (FR-P00-62, FR-P00-63; D-42, NN-24 amended)
> - Change batches with undo windows for every bulk and import operation (FR-P00-64; NN-49)
> - Three-date value object — act, evidence, approval (FR-P00-65; NN-48)
> - Skeletons for modules `gem`, `prt`, `lit`, `esg`; `rpt` owned by P28; `gov.rpt_txn_*` naming (FR-P00-66; D-47, D-48)
> - AI foundations: adapter, data-class routing, kill-switch registry, model registry, eval runner (FR-P00-67; NN-41, NN-50, NN-51)
> - Configuration templates, sandbox tenants, FinOps tags and SLO catalogue (FR-P00-68, FR-P00-69)
> - Equator references standardised to "Equator v3.1 App …" (G5 E-15)

---

## 1. Objective and business outcome

LawDocsComply already runs in production at lawdocscomply.com: a TypeScript, React and Node.js application on MongoDB (Atlas) with Prisma, deployed on Railway with GoDaddy DNS, carrying RBI and Companies Act question banks, an admin dashboard and 21 product modules, in beta with Branch International. It was built fast and has served its purpose. It cannot carry what the owner now wants — an append-only audit ledger, bitemporal regulatory content with tenant overlays, row-level tenant isolation, India-only residency, ecosystem contracts with Finbyx, Udofin, Equator and the Operations Hub, and certification readiness for SOC 2 and ISO 27001.

P00 does three things. It **discovers** what exists and preserves every useful asset (question banks, SEO work, users, beta tenant data). It **builds the platform core** on the locked stack (D-01): monorepo, PostgreSQL with enforced RLS, the hash-chained audit ledger with Correction Entries (D-02), bitemporal patterns, transactional outbox, feature flags, the evidence store, observability and the CI/CD skeleton. It **migrates** the legacy data in controlled waves with reconciliation, so no customer re-keys anything and the beta tenant experiences no data loss.

| Outcome | Exit-gate measure |
|---|---|
| Nothing useful is lost | `docs/discovery/` inventory signed off by the owner: every legacy module, collection, question bank, user, tenant, integration, secret, DNS record and SEO asset is listed with a disposition (MIGRATE, REBUILD, RETIRE, ARCHIVE). Zero items "unknown" |
| Platform core runs | `docker compose up` and `pnpm dev` start all apps locally in ≤ 10 minutes on a fresh machine; dev, staging and uat environments deploy from `main` through CI with signed images |
| Tenant isolation is provable | RLS lint passes on every tenant table (FORCE RLS + policy); `NN-01_cross_tenant_read_denied` passes for 100% of tables with generated queries across two seeded tenants |
| Audit ledger is tamper-evident | `NN-02_*` suite passes: every material action writes a chained event in the same transaction; daily verification and signed anchor run; an attempted `UPDATE`/`DELETE` on the ledger fails even for the owner role; a super-admin override is only possible as a dual-approved Correction Entry that is visible to the tenant |
| Bitemporal content works | A seeded instrument can be amended with a future effective date; queries "as of" any valid date and "as recorded" at any instant return the correct versions (`NN-07_*`) |
| Legacy content migrated (wave 1) | Every legacy question row is present in `cnt` with a migration lineage record, row counts reconcile 100%, a 5% stratified manual sample (minimum 200 rows) is checked by the Company Secretary with ≤ 0.5% field-level defects, all fixed before exit |
| Evidence store is WORM | Evidence objects land in an Object Lock (compliance mode) bucket in ap-south-1 with SHA-256 recorded; a delete attempt within retention fails (`NN-09_*`) |
| Export contract exists | The `LDC-EXPORT-1.0` mapping registry and its CI contract test exist; a migration that adds a tenant table without an export mapping fails CI (`NN-10_*`) |
| India residency | Infrastructure-as-code denies resources outside ap-south-1/ap-south-2 (except listed global services); the Railway deployment is scheduled for decommissioning with a dated plan (`NN-24_*`) |

---

## 2. Scope (in / out)

**In scope**

- Discovery of the legacy repository, database, deployment and third-party accounts; disposition register; architecture decision records (ADRs) 0001–0020.
- Monorepo scaffold with apps and packages (§4.2), toolchain, linting, module-boundary enforcement and code ownership.
- Local stack, environments (local, dev, staging, uat, prod, dr), infrastructure as code and the hosting plan (Supabase Mumbai for non-production and beta, AWS RDS/Aurora in ap-south-1 with ap-south-2 DR before general availability — §4.3).
- CI and CD skeleton with signed artefacts, SBOM, provenance and the NN test harness (P24 hardens and completes it).
- `core` schema: tenants, legal entities, tenant domains, organisational skeleton, jurisdictions, data-class catalogue, feature flags, module entitlement cache, sequences, idempotency keys, transactional outbox and inbox, audit ledger, audit anchors, correction entries, audit annotations, access log, break-glass events.
- PostgreSQL roles, RLS framework, session context, RLS lint; field-level encryption library; blind indexes and masking.
- Bitemporal modelling library and conventions; decimal and money types; ID generation; citation value object.
- Object storage buckets (quarantine, documents, evidence, exports, backups) and the evidence ingest pipeline skeleton (P07 builds the DMS on it).
- Observability (OpenTelemetry traces, metrics and logs; PII scrubbing; error tracking), health checks, status endpoints.
- Feature-flag service and flag registry; the `cfg` registry heads used by P02.
- Design system foundations (tokens, theming, accessibility primitives) and i18n framework (English first; Hindi and other Indian languages later through P23).
- Synthetic seed data profiles (`dev`, `demo`, `load`, `beta-mirror`).
- Data migration framework and waves 1–3 (wave 1 executed here; waves 2–3 rehearsed here, executed later).
- Export-mapping registry skeleton (`xpt.export_mappings`) and the NN-10 CI contract test (P19 builds the package generator).

**Out of scope (owned later)**

- Identity, login, onboarding wizard, RBAC/ABAC decisions — P01 (P00 creates only the tables P01 needs and a stub identity provider for local development).
- Configuration Studio UI and rule-pack engine — P02 (P00 creates the `cfg` registry tables and the SDK interface).
- Regulatory content authoring, Excel import — P03 (P00 migrates legacy content into the P03 schema as defined in Appendix B; if P03 later refines the schema, the migration is replayed from the immutable wave-1 snapshot).
- Production go-live hardening, VAPT, certification evidence automation — P24.
- Mobile apps (D-01: responsive PWA only in v1.0).

---

## 3. Personas and permissions touched

| Role code | What P00 gives them |
|---|---|
| `plt_super_admin` | Seeded platform tenant `ldc-platform` and the first super-admin account (stub IdP in local/dev; Keycloak in P01). May request Correction Entries; cannot approve their own |
| `plt_security_officer` | Approves Correction Entries of class `SECURITY` and break-glass sessions; receives audit-chain alerts; owns KMS key policies |
| `plt_content_maker`, `plt_content_checker` | Run and verify the wave-1 content migration in the migration console (SCR-CORE-06) |
| `plt_auditor` | Read-only access to the platform audit chain, anchors and verification reports |
| `plt_support` | No tenant data access in P00; break-glass schema only |
| `ten_admin` (beta tenant) | Sees the "Platform corrections" register (SCR-CORE-08) for corrections applied to their tenant |
| `ten_external_auditor`, `ten_supervisor_view` | Not provisioned in P00; the anchors and verification endpoints they will use later are built here |

All permission checks in P00 are coarse (platform role only). P01 replaces them with Cerbos policies (Appendix D) without changing the APIs.

---

## 4. Functional requirements

### 4A. Discovery of the legacy system

**FR-P00-01 — Read-only discovery access.** The owner grants the agent read-only access to: the legacy GitHub repository (or a zipped copy), a MongoDB Atlas read-only user on a point-in-time restore (never the live cluster), the Railway project (viewer), GoDaddy DNS (export of the zone file), and the list of third-party accounts (email provider, payment provider if any, analytics, AI API keys). No production secret is copied into the new repository; secrets are listed by name, owner and rotation status only.

**FR-P00-02 — Inventory scripts.** Commit `tools/discovery/` with repeatable scripts that produce `docs/discovery/`:

| Output file | Contents |
|---|---|
| `01-repository.md` | Languages, frameworks and versions, package manifest, dependency tree with known vulnerabilities (osv-scanner), build and deploy scripts, environment variables by name, test coverage, licence scan |
| `02-modules.md` | The 21 product modules as they exist: route list, screens, API endpoints, Prisma models used, completeness (WORKING / PARTIAL / STUB), user-visible features, defects found. Map each to the new phase that rebuilds it (P03–P23) |
| `03-data-model.md` | Every MongoDB collection and Prisma model: document count, fields, types, nullability observed, indexes, references, PII fields, size |
| `04-question-banks.md` | Every question bank (RBI NBFC Base/Middle/Upper Layer, CIC; Companies Act; any IFSCA or other banks): source instrument, row count, column coverage against template contract v2.0 (Appendix E; the owner's 30-column v1.0 sheets through the legacy map), duplicates, missing citations, encoding issues |
| `05-tenants-and-users.md` | Tenants (including the Branch International beta tenant), users by role, last login, MFA state, active sessions — counts and pseudonymised IDs only; no names or emails in the repository |
| `06-integrations.md` | Every external call (AI, email, SMS, storage, analytics, payment) with endpoint domain, credential owner, data sent, and contract status |
| `07-infrastructure.md` | Railway services, regions, databases, backups, domains, TLS, GoDaddy DNS records (A, CNAME, MX, TXT including SPF, DKIM, DMARC), CDN, monitoring |
| `08-seo-assets.md` | Public pages and URLs, titles, meta descriptions, JSON-LD blocks, `llms.txt`, `robots.txt`, sitemap, canonical tags, inbound-link-critical URLs, Search Console status — all preserved by P23 with 301 redirects where paths change |
| `09-security-findings.md` | Secrets in history (gitleaks over full history), auth weaknesses, missing tenant filters, injection risks, dependency CVEs, public buckets; each finding gets a severity and is either fixed in the legacy app before cut-over (Critical/High) or recorded as retired with the legacy app |
| `10-disposition-register.md` | One row per asset: ID, description, disposition (MIGRATE / REBUILD / RETIRE / ARCHIVE), target phase, owner, risk, notes. Signed off by the owner at the P00 exit |

**FR-P00-03 — Legacy security triage.** Any Critical or High finding in `09-security-findings.md` that exposes current users (for example, a missing tenant filter, a leaked key in Git history, an unauthenticated admin route) is reported to the owner the same day with a fix for the legacy app. Leaked secrets are rotated within 24 hours (P24 SLA floor). The legacy app keeps running until cut-over, so its security matters during P00–P07.

**FR-P00-04 — Claims hygiene of the live site.** The baseline onboarding copy says "We're ISO 27001 certified and DPDP-compliant." Until a certificate exists this claim must not appear (NN-19). Discovery lists every public certification, regulator, client-logo or performance claim on lawdocscomply.com in `08-seo-assets.md` with a recommendation (REMOVE / REWORD / KEEP WITH EVIDENCE). The owner approves the corrections; P23 enforces the claims register permanently.

### 4B. Repository, toolchain and module boundaries

**FR-P00-05 — New repository.** Create `lawdocscomply` (private) under the Infrabyx GitHub organisation. The legacy repository is renamed `lawdocscomply-legacy`, archived read-only after cut-over and retained for 8 years (it is part of the evidence of how historical records were produced).

**FR-P00-06 — Monorepo layout.**

```
lawdocscomply/
├─ apps/
│  ├─ web/          # Next.js 16 tenant application (all tenant roles, regulator view, auditor workspaces)
│  ├─ public/       # Next.js 16 marketing site, pricing, marketplace, health check, help centre (SSR/SSG, SEO)
│  ├─ console/      # Next.js 16 platform super-admin console (separate origin, separate Keycloak client)
│  ├─ delivery/     # Next.js 16 Service Delivery Console for LawDocs RMs and professionals (D-03)
│  ├─ api/          # NestJS 11 modular monolith: HTTP, webhooks, SCIM, partner APIs
│  ├─ worker/       # NestJS application context: Temporal workers, outbox relay, schedulers
│  └─ docs-site/    # Developer portal (OpenAPI/AsyncAPI rendering) — content in P18
├─ packages/
│  ├─ domain/       # Pure domain types and rules, no framework imports (per module sub-folders)
│  ├─ db/           # Drizzle schema, migrations, RLS policies, pgTAP tests, seeds
│  ├─ contracts/    # OpenAPI 3.1, AsyncAPI 3.0, JSON Schema 2020-12 (generated + ecosystem copies)
│  ├─ config/       # Settings registry SDK (P02 completes), feature-flag client
│  ├─ audit/        # Audit ledger client, canonicalisation, hash, correction-entry service
│  ├─ crypto/       # Envelope encryption, blind index, masking (server-only)
│  ├─ bitemporal/   # Valid-time / recorded-time helpers, as-of query builders
│  ├─ money/        # Decimal, money, rate, rounding modes (decimal.js, precision ≥ 40)
│  ├─ ids/          # Prefixed ULID generation and validation
│  ├─ citations/    # Citation value object (authority, instrument, version, paragraph, URL, hash)
│  ├─ ui/           # Design system (shadcn/ui + Tailwind tokens), accessibility primitives
│  ├─ i18n/         # Message catalogues, ICU formatting, Indian number formatting
│  ├─ observability/# OpenTelemetry setup, PII scrubber, log schema
│  ├─ testing/      # Factories, two-tenant fixtures, NN test helpers, golden-file helpers
│  └─ returns-kernel-client/ # Pinned client of the shared infrabyx-returns-kernel (D-05; P11)
├─ db/
│  ├─ ownership.yaml        # table → owning module
│  ├─ rls-exemptions.yaml   # global reference tables with justification
│  └─ export-mappings/      # LDC-EXPORT-1.0 mapping per table (NN-10)
├─ infra/                   # Terraform (or moved to lawdocscomply-infra, see FR-P00-17)
├─ tools/                   # discovery, migration, verification scripts
├─ docs/
│  ├─ adr/                  # ADR-0001…
│  ├─ discovery/
│  ├─ ecosystem/            # Integration Spec v1.1 (unchanged, SHA-256 checked), Ops Hub reference
│  ├─ phases/               # PXX-plan.md written before each phase
│  └─ runbooks/
└─ tests/acceptance/pXX/    # Gherkin features per phase
```

**FR-P00-07 — Toolchain.** Node.js 24 LTS pinned in `.nvmrc` and `engines` (Node 26 entered LTS in October 2026 under the last release of the old model [VERIFY: LTS promotion date]; upgrade by ADR once NestJS, Next.js and Temporal SDK support is confirmed); pnpm with workspaces; Turborepo pipelines `lint`, `typecheck`, `test`, `build`, `e2e`, `db:migrate`, `db:test`, `seed`, `nn`. TypeScript `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`. ESLint flat config with `@typescript-eslint/strict-type-checked` and `eslint-plugin-boundaries`; Prettier; commitlint (Conventional Commits); lint-staged; Husky. Versions of Next.js (16.x), React (19.x), NestJS (11.x), Drizzle, Temporal TypeScript SDK, Keycloak (26.8.x at drafting, released 13 Oct 2026) and Cerbos are pinned and recorded in ADR-0001 with dated release notes.

**FR-P00-08 — Module skeletons.** Generate a NestJS module for every bounded context in master §5 (`core`, `iam`, `cfg`, `cnt`, `tpl`, `cmp`, `chg`, `wf`, `gov`, `pol`, `dms`, `erm`, `ral`, `aud`, `ret`, `acc`, `dpc`, `tpr`, `hr`, `lab`, `grv`, `pack`, `coop`, `ai`, `int`, `xpt`, `bil`, `mkp`, `sdc`, `web`, `hlp`, `rpt`, `eng`; *(v1.1)* plus `gem`, `prt`, `lit`, `esg` — FR-P00-66). Each has `public-api.ts`, `module.ts`, `domain/`, `infra/`, `http/`, `events/`, `README.md` (purpose, owned tables, published and consumed events, settings keys, export mappings). Rules enforced in CI:

- A module may import another only through its `public-api.ts`.
- A module may read or write only tables it owns (`db/ownership.yaml`); cross-module reads go through the owner's public API or a read model the owner publishes. A CI script parses Drizzle queries and fails on violations.
- `packages/domain` may not import framework code; calculation code (ratios, capital, payroll, tax, due dates) lives there with 100% branch coverage (NN-22).
- The PostgreSQL schema name equals the module code.

**FR-P00-09 — Code ownership.** `CODEOWNERS`: `packages/db/migrations/**`, `packages/db/rls/**` → database owner + security engineer; `packages/audit/**`, `packages/crypto/**` → security engineer + tech lead; `packages/domain/**/calc/**` → tech lead + domain reviewer (CA/CS for financial and secretarial logic); `db/export-mappings/**` → data owner; `infra/**` → platform owner; `docs/ecosystem/**` → Integration Spec owner (changes only via `infrabyx-contracts`). P24 converts this into GitHub rulesets.

### 4C. Environments and hosting

**FR-P00-10 — Environment catalogue.**

| Env | Purpose | Data | Hosting | Deploy trigger | Approval |
|---|---|---|---|---|---|
| local | Developer machine | Seed `dev` | Docker Compose | — | — |
| dev | Integration of `main` | Seed `demo`, reset weekly | Supabase ap-south-1 (Mumbai) + AWS ap-south-1 compute | Merge to `main` | None |
| staging | Release candidate, E2E, performance smoke | Seed `demo` + `load` | Supabase ap-south-1 or RDS (mirrors prod engine from P24) | Tag `rc-*` | None |
| uat | Owner and beta-client acceptance, demos | Seed `demo` + curated `beta-mirror` (synthetic, never production copies) | As staging | Promotion of the same image digest | Product owner |
| prod | Live | Real | **AWS ap-south-1** RDS PostgreSQL Multi-AZ (or Aurora PostgreSQL) — see FR-P00-11 | Promotion of the same digest | 2 approvers + change record (P24) |
| dr | Warm standby | Replica + backups | AWS ap-south-2 (Hyderabad) | Terraform only | — |

Production data never leaves prod. Non-production adapters for email, SMS, WhatsApp, eSign, payment, KYC/KYB and AI are forced to sandbox or fake providers by a `provider_routing` guard that fails closed (an attempt to call a live provider from non-prod raises `LDC-CORE-014` and an alert).

**FR-P00-11 — Hosting decision (ADR-0006).** D-01 allows Supabase ap-south-1 now and RDS/Aurora later. The agent records the following in ADR-0006 and implements it unless the owner overrides:

- Supabase offers Mumbai (`ap-south-1`) only as a "specific region" and offers no Hyderabad region (Supabase regions page, checked 25 Oct 2026). Its Storage product does not provide S3 Object Lock. It is therefore suitable for local-like hosted dev, staging, uat and the beta, but a production estate serving regulated entities needs: (a) ap-south-2 disaster recovery, (b) WORM evidence storage, (c) customer audit rights over the provider chain, and (d) predictable RPO/RTO.
- **Recommendation [REC]:** production on AWS from first paid RE tenant: Amazon RDS for PostgreSQL Multi-AZ (or Aurora PostgreSQL if the cost case holds) in ap-south-1 with a cross-region read replica or Aurora Global Database in ap-south-2; S3 with Object Lock for evidence; ECS Fargate for compute. Keep the application portable (no Supabase-specific APIs: Supabase Auth, Realtime, Storage and Edge Functions are not used; only its PostgreSQL), so the move is a database migration, not a rewrite.
- Supabase must be on a plan that includes point-in-time recovery for beta data, with daily encrypted logical backups copied to an S3 bucket in ap-south-2 (RPO 24 h for region loss during beta, disclosed to the beta tenant).
- Railway is not used for anything in the new estate. The legacy Railway service and MongoDB Atlas cluster region are recorded in `07-infrastructure.md`; if either is outside India, the beta tenant is told in writing and the cut-over date is fixed (NN-24) [VERIFY: current Railway and Atlas regions of the legacy deployment].
- Cloud services used are recorded in the sub-processor register (Appendix Q §Q.9) with region, data class and contract.

**FR-P00-12 — AWS account topology.** AWS Organizations with accounts `ldc-management`, `ldc-security` (GuardDuty, Security Hub, IAM Access Analyzer, Inspector delegated admin), `ldc-log-archive` (organisation CloudTrail, AWS Config, VPC flow logs; S3 Object Lock), `ldc-shared` (ECR, CI OIDC roles, Route 53), `ldc-dev`, `ldc-staging`, `ldc-uat`, `ldc-prod`, `ldc-backup` (AWS Backup vault with vault lock, separate credentials). If the group runs one AWS Organization for all products, these are OUs under it; the Operations Hub never receives credentials into `ldc-prod` (Ecosystem Spec §4.6). Service control policies: deny regions other than ap-south-1 and ap-south-2 (allow-list global services: IAM, Organizations, Route 53, CloudFront, WAF global, ACM for CloudFront, Support); deny disabling CloudTrail, GuardDuty or Config; deny changing Object Lock configuration on evidence buckets except through the break-glass role; deny root-user actions.

**FR-P00-13 — Network and compute.** VPC across three AZs; private subnets for compute and data; egress only through an allow-list proxy (`infra/egress-allowlist.yaml`, one entry per vendor domain with owner and data class); VPC endpoints for S3, KMS, Secrets Manager, ECR, CloudWatch Logs, STS. ECS Fargate services `web`, `public`, `console`, `delivery`, `api`, `worker`, `outbox-relay`, `temporal-*` (or Temporal Cloud only if it offers India residency — [VERIFY]; default self-hosted), `keycloak`, `cerbos`, `unleash` (or flag service of ADR-0012), `clamav`, `gotenberg`, `otel-collector`. ALB with AWS WAF (managed core rule set, SQLi, known bad inputs, bot control on public routes, rate rule on `/v1/auth/*` and `/v1/public/*`). CloudFront for `public` with India origin; `console` and `delivery` are not exposed through the public CDN and accept only SSO-authenticated staff from allow-listed networks or a device posture check (P24).

**FR-P00-14 — Database topology.** One PostgreSQL cluster `ldc_core` holding all module schemas, plus a separate database `ldc_sealed` (separate cluster in prod) for sealed data classes (NN-13): POSH complaints and inquiry records, whistle-blower reports, grievance complainant identity where marked sealed, health-related HR records, board-confidential papers flagged "restricted", and the credential vault ciphertext (D-04). Core references sealed rows only by an opaque token `sealed_ref` (`sr_` + 26 random base32 characters); the token map lives only in `ldc_sealed`; no foreign key, join, search index, analytics export or AI dataset reads it. Extensions: `pgcrypto`, `btree_gist` (exclusion constraints for bitemporal ranges), `ltree` (org-unit paths), `pg_partman` (partitioning for ledger, outbox, notifications), `pg_trgm` and FTS dictionaries (search fallback), `pgvector` (AI retrieval index for platform content only; tenant embeddings follow P17 rules). PostgreSQL major version: the highest version available on both Supabase and RDS at build time (17 at minimum; 18 — released 25 Sep 2025, with `uuidv7()`, temporal `WITHOUT OVERLAPS`/`PERIOD` constraints and `OLD`/`NEW` in `RETURNING` — preferred when both hosts support it [VERIFY: Supabase major version]). Code must not depend on PostgreSQL 18-only syntax unless ADR-0002 records that both hosts support it; the bitemporal library uses `btree_gist` exclusion constraints that work on 16+.

**FR-P00-15 — Local stack.** `docker compose up` brings up PostgreSQL (same major as prod) with the extensions above and a second database `ldc_sealed`; Redis 7 (or Valkey); Temporal dev server and UI; OpenSearch 2.x (single node); MinIO with Object Lock enabled; Keycloak (dev realm import); Cerbos; Unleash; Mailpit; ClamAV; Gotenberg; OpenTelemetry Collector with Grafana LGTM. `pnpm dev` runs all apps. Make targets: `make reset-db`, `make seed PROFILE=demo`, `make verify-audit`, `make rls-lint`, `make export-contract`.

**FR-P00-16 — Domains.** `lawdocscomply.com` (public), `app.lawdocscomply.com` (tenant app; custom tenant sub-domains `<slug>.lawdocscomply.com` from P02 if enabled), `console.lawdocscomply.com` (platform), `delivery.lawdocscomply.com` (service delivery), `api.lawdocscomply.com` (APIs), `developers.lawdocscomply.com` (developer portal), `status.lawdocscomply.com` (status page). DNS moves from GoDaddy to Route 53 (or stays at GoDaddy with delegation of sub-zones) per ADR-0016; DNSSEC enabled; email authentication records (SPF, DKIM, DMARC `p=quarantine` then `p=reject`) carried over from discovery without breaking current mail.

**FR-P00-17 — Infrastructure as code.** Terraform ≥ 1.11 with S3 backend and native lockfile; separate repository `lawdocscomply-infra` if the group standard requires (OH13 repository register lists it). Modules: `org_scp`, `network`, `kms`, `rds_or_aurora`, `sealed_db`, `redis`, `opensearch`, `s3_quarantine`, `s3_documents`, `s3_evidence`, `s3_exports`, `s3_backups`, `ecs_cluster`, `ecs_service`, `alb_waf`, `cloudfront`, `temporal`, `keycloak`, `cerbos`, `flags`, `observability`, `ses`, `secrets`, `backup`, `github_oidc`. CI runs `fmt -check`, `validate`, `tflint`, `checkov` (fail on HIGH), posts the plan to the pull request; nightly drift detection opens an incident on drift.

### 4D. CI and CD skeleton (completed in P24)

**FR-P00-18 — CI on every pull request** (`.github/workflows/ci.yml`; actions pinned by commit SHA; workflow lint with `zizmor`): install with cache; `turbo run lint typecheck test` for affected packages; coverage gates (`packages/domain` ≥ 90% lines and 100% branches for `calc/`, overall ≥ 80%); OpenAPI generation and `oasdiff breaking` against `main` (breaking change fails unless labelled `api-major` with an ADR link and the deprecation notice of P24 §4F); migration job (apply all migrations to a fresh PostgreSQL Testcontainer, run RLS lint, pgTAP tests, the expand-contract checker of FR-P00-47, and the export-mapping contract test of FR-P00-55); Storybook build with axe (0 serious or critical); Playwright component tests; Semgrep (OWASP rules plus custom rules: no raw pool import, no `console.log`, no outbound `fetch` outside adapters, no decryption without `@DecryptFor`, no audit-less mutation); CodeQL; gitleaks; osv-scanner and Trivy (filesystem); Syft SBOM (CycloneDX) upload; licence policy (deny AGPL and SSPL in shipped code; services such as Unleash run as separate processes and are recorded). The **NN suite** (`pnpm nn`) is a required job; a failing `NN-*` test blocks merge.

**FR-P00-19 — CD skeleton** (`deploy.yml`): build OCI images once per commit (multi-stage, distroless Node runtime, non-root UID 10001, read-only root filesystem), sign with cosign keyless (GitHub OIDC), attach SBOM and SLSA provenance (build level 3 target, P24), push to ECR with immutable tags (git SHA). Deploy through GitHub OIDC to environment-scoped IAM roles (no long-lived keys). Order: run migrations as a one-off task (forward-only, expand-contract) → deploy `api`, `worker`, `outbox-relay` (blue/green with canary) → deploy web apps. Automatic rollback on alarm (5xx > 1% for 3 minutes, p95 latency > 800 ms for 5 minutes, SLO burn rate > 14.4 on the 1-hour window). Production approval and change-record linkage are added in P24 (Appendix Q §Q.7; OH13 `ChangeApproved` gate).

### 4E. Tenancy, row-level security and session context

**FR-P00-20 — Tenant model.** `core.tenants`: `id` (`ten_` + ULID), `slug`, `legal_name`, `display_name`, `kind` ∈ {`client` (a regulated entity, company, LLP, society or other organisation using the SaaS), `group` (a client group umbrella holding several legal entities), `platform` (LawDocsComply's own platform tenant), `ldc_group` (Infrabyx group's own compliance instance — Ecosystem Spec §9.1 `LDC_GROUP`), `provider` (a marketplace provider firm, P21), `sandbox` (customer sandbox, P02)}, `status` ∈ {`lead`, `trial`, `active`, `grace`, `suspended`, `offboarding`, `archived`} (lifecycle in Appendix A §A.3; commercial states set by P20), `data_region` (`ap-south-1` only at launch; other values reserved for D-19 international packs), `default_locale`, `enabled_locales`, `timezone` (default `Asia/Kolkata`), `fiscal_year_start` (default 1 April), `isolation_tier` (`shared` | `dedicated_db` | `dedicated_cluster`), `dedicated_key` (bool), `byok_key_arn` (customer-managed key, P19), `parent_tenant_id` (group umbrella), `ecosystem_org_id` and `reid` (Ecosystem Spec §4.1 organisation registry and RE id), `grc_mode` (`LDC_EXTERNAL` | `LDC_GROUP` — Ecosystem Spec §9.1), `contract_ref`, `created_at`, `recorded_at`. The platform tenant `ldc-platform` is seeded and cannot be suspended or deleted.

**FR-P00-21 — Legal entities.** A tenant holds one or more `core.legal_entities` (the companies, LLPs, societies, branches of foreign entities, funds or schemes it manages): `id` (`len_`), `tenant_id`, `constitution` (code table: PVT_LTD, PUBLIC_UNLISTED, PUBLIC_LISTED, OPC, SECTION_8, PRODUCER_CO, NIDHI, LLP, FOREIGN_CO, PARTNERSHIP, PROPRIETORSHIP, TRUST, SOCIETY_SRA, COOP_STATE, COOP_MSCS, BANKING_CO, STATUTORY_CORP, AIF_TRUST, MF_TRUST, REIT_TRUST, INVIT_TRUST, IFSC_UNIT, OTHER), identifiers (CIN/LLPIN/FCRN, PAN masked + blind index + token, TAN, GSTINs (child table), LEI, CoR numbers per regulator (child table `core.registrations`: authority, registration type, number, date, validity, status, verified_at, source)), registered office, incorporation date, fiscal year, entity family and sub-type references (P15 `pack` taxonomy), listing status, holding/subsidiary links (`core.entity_relationships`: type HOLDING, SUBSIDIARY, ASSOCIATE, JV, STEP_DOWN, FEDERATION_MEMBER, SPONSOR, MANAGER_OF (AMC→fund, IM→AIF, manager→REIT/InvIT), share %, from/to). Legal entities are bitemporal (constitution and registrations change over time; history is preserved).

**FR-P00-22 — Organisational skeleton.** `core.org_units` (tenant-scoped tree: `id` `oru_`, `legal_entity_id`, `parent_id`, `kind` ∈ {DEPARTMENT, FUNCTION, BRANCH, REGION, COMMITTEE_SECRETARIAT, VERTICAL, COST_CENTRE}, `code`, `name` (renameable — R-086), `canonical_function` (mapping to the platform's canonical function list used for content routing, so a tenant's "Secretarial & Legal" still receives obligations tagged "Governance & Administration"), `head_person_ref`, `valid_period`). HR (P13) and governance (P06) extend it; P00 creates only the skeleton so that every later module can scope records by org unit for ABAC.

**FR-P00-23 — Tenant resolution.** Web: Next.js middleware resolves the tenant from host (`core.tenant_domains`, cached 5 minutes) or from the user's selected membership (users with several tenants pick one; the selection is a signed context claim). API: the active tenant comes from the validated request context (P01 token claim `ldc_ctx` with tenant, legal entity, membership and act-as data) checked against `iam.memberships`; machine clients: from the client-credentials grant (P18). An unknown host returns a neutral 404 (no tenant enumeration).

**FR-P00-24 — Database roles.** `ldc_owner` (owns schemas; NOLOGIN), `ldc_migrator` (runs migrations; member of `ldc_owner`), `ldc_app` (LOGIN, NOBYPASSRLS, DML only), `ldc_platform` (LOGIN, NOBYPASSRLS; used only by `console` platform services for cross-tenant reads that are policy-checked and logged), `ldc_reporting_ro` (read replica, RLS applies), `ldc_supervisor_ro` (SELECT-only on supervisor read models, used by regulator-view sessions, D-12), `ldc_sealed_app` (LOGIN on `ldc_sealed` only, from allow-listed modules). No application role has `BYPASSRLS` or owns tables. Every tenant table has `ENABLE` and `FORCE ROW LEVEL SECURITY`.

**FR-P00-25 — Session context.** Every transaction sets `app.tenant_id`, `app.user_id`, `app.actor_type` (`user` | `service` | `vidhi` | `platform` | `delivery` | `supervisor`), `app.on_behalf_of` (for Vidhi and delegated actions), `app.request_id`, `app.legal_entity_ids` (array, when ABAC narrows), `app.break_glass_id` (when active) with `set_config(..., true)`. Data access goes only through `db.withContext(ctx, tx => …)`; a lint rule forbids importing the raw pool. If `app.tenant_id` is missing, `core.current_tenant()` returns NULL and every tenant policy returns zero rows (fail closed). Connection pooling must not leak session state: use transaction-scoped `set_config` with a pool per task; PgBouncer in transaction mode only if `set_config(..., true)` is used exclusively (ADR-0007).

**FR-P00-26 — RLS policies.** Standard policy template per tenant table:

```sql
ALTER TABLE cmp.compliance_instances ENABLE ROW LEVEL SECURITY;
ALTER TABLE cmp.compliance_instances FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON cmp.compliance_instances
  USING (tenant_id = core.current_tenant())
  WITH CHECK (tenant_id = core.current_tenant());
```

Platform-content tables (`cnt.*` base content) are readable by all tenants but writable only under `app.actor_type = 'platform'` with the content-publisher role; tenant overlays (`cnt.tenant_overlays`, `cmp.*`) are tenant-scoped. Finer row filters (legal entity, org unit, sealed flags, assignment) are applied by Cerbos-generated query plans in the application (P01) — RLS is the tenant wall, Cerbos is the room-level access control. Both are tested.

**FR-P00-27 — RLS lint and cross-tenant test.** `packages/db/tests/rls_lint.sql` enumerates every table in every module schema and fails if a table with a `tenant_id` column lacks `relrowsecurity AND relforcerowsecurity` or a policy referencing `core.current_tenant()`, unless listed in `db/rls-exemptions.yaml` with justification (global reference tables only: code tables, jurisdictions, authority list, published platform content heads). `NN-01_cross_tenant_read_denied` seeds two tenants with generated rows for every table and asserts zero leakage for SELECT, UPDATE and DELETE through `ldc_app`; it also checks Redis keys, OpenSearch indices (tenant-scoped index alias or `tenant_id` filter enforced in the search adapter), object-storage prefixes and Temporal workflow IDs carry the tenant.

**FR-P00-28 — Field-level encryption.** `packages/crypto` (server-only) implements envelope encryption with AWS KMS (AWS Encryption SDK or equivalent) and a keyring per data class (`pii`, `spi`, `financial`, `hr`, `legal`, `sealed`, `credential`, `board_confidential`) and, for `dedicated_key` tenants, per tenant. Column convention: `<field>_enc bytea` (ciphertext), `<field>_bidx bytea` (HMAC-SHA-256 blind index with a per-tenant key for equality lookups, for example PAN, mobile, email), `<field>_masked text` (display form: PAN `ABCDE****F`, mobile `98******10`, account `XXXXXX4321`). Decryption requires `@DecryptFor(purpose)`, which writes `core.access_log`. Aadhaar numbers are never stored (NN-12); only a reference to an offline-verification or DigiLocker artefact hash, the last four digits if a law requires display, and the verification result.

**FR-P00-29 — Data-class catalogue.** `core.data_classes` seeds the Ecosystem Spec §13.2 classes (`PUBLIC`, `INTERNAL`, `CONFIDENTIAL`, `PII`, `SPI`, `FINANCIAL`, `LEGAL`, `HR`; `WELLNESS` is listed only as a class LDC must reject) plus LDC classes `SEALED` (POSH, whistle-blower, sealed complainant identity), `BOARD_CONFIDENTIAL`, `CREDENTIAL` (vault secrets, D-04), `LEGAL_PRIVILEGED` *(v1.1, X1: privileged legal communications, P26; separate legal key; Appendix Q §Q.3)* and `REGULATOR_CONFIDENTIAL` (inspection reports, RBI/SEBI/IFSCA correspondence marked confidential — supervisory letters, risk-assessment reports, Monitorable Action Plans, which regulators often prohibit disclosing [VERIFY per regulator]). Every column of every table is tagged with a data class in `db/data-catalogue.yaml`; CI fails on an untagged column. The class drives encryption, masking, logging, export folder placement (Appendix M restricted folders), AI eligibility (P17) and event `dataclass`.

### 4F. Audit ledger, correction entries and access log (NN-02, D-02)

**FR-P00-30 — What is audited.** Every *material action* writes an audit event in the same database transaction as the business change, through `AuditService.append()` → `core.append_audit_event(jsonb)`. Material actions (catalogue in Appendix B §B.5, extended by every phase): create/update/state-transition of any business aggregate; content publication, amendment, supersession; tenant overlay of a question or actionable; applicability decision; maker submission, checker approval/rejection/reallocation; evidence upload, download, replacement, deletion request; status change; due-date change; assignment and reassignment; settings and permission changes; login, logout, MFA step-up, failed login; delegation; break-glass start/end; support access; decrypt or reveal of SPI/SEALED/CREDENTIAL data; export (any format, any size); AI tool call that changes data or drafts a record; payment, refund, invoice, credit note; Correction Entry lifecycle; supervisor/auditor grant lifecycle and usage.

**FR-P00-31 — Event structure and hash chain.** `core.audit_events` (partitioned by month; append-only):

| Column | Meaning |
|---|---|
| `chain_id` | Tenant id, or a platform chain id for platform/content actions (`chn_platform`, `chn_content`) |
| `seq` | Gap-free sequence per chain (allocated under a per-chain advisory lock) |
| `event_id` | `aev_` + ULID |
| `occurred_at` | Business time (when the act happened; for corrections, the true time of recording, never back-dated) |
| `recorded_at` | Database commit time (`clock_timestamp()`), never supplied by the client |
| `actor_type`, `actor_id`, `on_behalf_of`, `membership_id`, `act_as_role`, `delivery_engagement_id` | Who acted, for whom and in what capacity (a LawDocs RM acting as maker in a client tenant is recorded as `actor_type = delivery`, with the engagement) |
| `session_id`, `ip_hash`, `user_agent_hash`, `request_id`, `trace_id` | Correlation without raw PII |
| `module`, `action` (`<module>.<aggregate>.<verb>`), `aggregate_type`, `aggregate_id`, `aggregate_version` | What |
| `before_digest`, `after_digest` | SHA-256 of canonical JSON (RFC 8785 JCS) of the aggregate before and after |
| `change_set` | PII-free JSON of changed field paths with old/new values only for fields whose data class is `PUBLIC`/`INTERNAL`/`CONFIDENTIAL` (e.g., status, due date, assignee id); for higher classes, field path + digests only |
| `reason_code`, `comment_ref` | Optional reason; free text stored in the owning module (the ledger holds a reference) |
| `correction_id` | Set when this event applies a Correction Entry |
| `prev_hash`, `row_hash` | `row_hash = SHA-256(prev_hash ‖ canonical(event without row_hash))` |

The "what changed" views users see (for example, "Status changed from *In progress* to *Submitted for review* by A on 12 Oct 2026 14:03 IST") are rendered from `change_set` plus the owning module's history tables (every business table has a `*_history` companion written by trigger in the same transaction, with full before/after values under the table's own RLS and encryption). The ledger proves integrity; the history tables carry content.

**FR-P00-32 — Immutability.** `core.audit_events` and `core.audit_anchors` grant only `INSERT` (through the `SECURITY DEFINER` function) to `ldc_app`; a trigger raises `LDC-CORE-001` on any `UPDATE`, `DELETE` or `TRUNCATE`, including by `ldc_owner`; partitions older than the current month are detached into a read-only tablespace or exported to Object Lock storage after verification (retention ≥ 8 years; tenant-configurable longer, never shorter). Database administrators cannot alter history without detection: the chain verification and the external anchors (FR-P00-33) expose any alteration made outside the application.

**FR-P00-33 — Verification and anchoring.** `AuditChainVerifyWorkflow` runs daily at 02:15 IST for every chain modified in the last 48 hours and weekly (Sunday 03:00 IST) for all chains. `AuditAnchorWorkflow` runs at 00:10 IST: per chain, compute a Merkle root over the previous day's `row_hash` values, sign `{chain_id, date, first_seq, last_seq, count, merkle_root, prev_anchor_hash}` with an asymmetric KMS key (ECC_NIST_P256), write it to `core.audit_anchors` and to the evidence bucket under Object Lock; optionally obtain an RFC 3161 timestamp from a trusted timestamp authority [REC; flag `audit.anchor.tsa.enabled` = OFF until a TSA contract exists]. A tenant can download its anchors and verify its own chain offline with the open-source `ldc-verify` tool shipped in the export package (P19). A mismatch emits `in.lawdocscomply.core.AuditChainBroken.v1`, opens a Critical incident, freezes Governed configuration changes platform-wide and notifies the security officer and the affected tenant admin within 24 hours with the incident reference.

**FR-P00-34 — Correction Entries (D-02).** The only way anyone — super admin, content publisher, delivery staff or tenant admin — changes a recorded fact after the fact. `core.correction_entries`:

| Field | Rule |
|---|---|
| `id` | `cor_` + ULID |
| `tenant_id` | The tenant whose data is corrected (platform content corrections use the platform tenant and list affected tenants in `impact`) |
| `scope` | `RECORD_FIELD` (a field of an aggregate: e.g., date of compliance, status, assignee, applicability), `DOCUMENT_VERSION` (replace or withdraw an evidence or policy file version), `CONTENT` (base content erratum), `AUDIT_ANNOTATION` (mark a ledger event as erroneous, superseded or entered in error — never altering it), `SETTING`, `ENTITLEMENT`, `MASTER_DATA` (crucial client details — R-074), `DATE` (effective-date or due-date correction) |
| `target` | aggregate type, id, version, field paths, or audit `event_id` |
| `old_value_digest`, `new_value` | Digest of the old value (old value itself remains in the history table); new value encrypted per data class |
| `effective_at` | The business date the corrected value is effective from (may be in the past — this is how "change the date" is done) |
| `recorded_at` | True system time (never editable) |
| `reason_code` | `DATA_ENTRY_ERROR`, `CLIENT_REQUEST`, `REGULATOR_DIRECTION`, `AUDITOR_OBSERVATION`, `LEGAL_ORDER`, `MIGRATION_FIX`, `CONTENT_ERRATUM`, `SECURITY_INCIDENT`, `DUPLICATE`, `OTHER` |
| `justification` | ≥ 50 characters; required |
| `supporting_doc_ids` | Mandatory for `REGULATOR_DIRECTION`, `LEGAL_ORDER`, `AUDITOR_OBSERVATION`, `CLIENT_REQUEST` (the client's written request) |
| `requested_by`, `approved_by`, `second_approved_by` | Maker ≠ checker (NN-05). Platform corrections of tenant data need a platform checker **and**, unless `REGULATOR_DIRECTION`/`LEGAL_ORDER`/`SECURITY_INCIDENT`, a tenant-admin acknowledgement before or within 2 working days after application (configurable: `core.correction.tenant_ack_mode` = `PRIOR` (default for `MASTER_DATA`, `DOCUMENT_VERSION`) or `POST`) |
| `visibility` | Always `TENANT_VISIBLE` (D-02 option 1). There is no hidden mode. |
| `state` | `DRAFT → SUBMITTED → APPROVED → APPLIED`; `REJECTED`, `WITHDRAWN`; `APPLIED → REVERSED` (by a new Correction Entry) |
| `applied_event_id` | Audit event that applied it |

Effects when `APPLIED`: the target aggregate gets a new version (with `correction_id`), its history row records old and new values, the ledger event carries `correction_id`, the UI shows a "Corrected" badge with a link to the entry wherever the value appears, the tenant's **Platform corrections** register (SCR-CORE-08, Settings › Audit & history) lists it, and exports include `Corrections_Register.xlsx` (Appendix M). Corrections to documents never overwrite the old file: the old version is retained under Object Lock, marked `superseded_by_correction`. A correction can never: change `recorded_at`; remove an audit event; alter another tenant's data; bypass a legal hold (a legal hold blocks `DOCUMENT_VERSION` withdrawal until released). Super admin's "overwrite anything" (R-068, R-071) is fully served by this mechanism: any field, document, setting, date or annotation can be changed, and every change is provable.

**FR-P00-35 — Tenant self-corrections.** Tenants use the same mechanism inside their own tenant (for example, a maker entered the wrong date of compliance after the checker approved). Tenant corrections need tenant maker ≠ tenant checker; `ten_admin` cannot approve their own. Corrections that touch an item already presented to the Board, a filed return or an auditor-signed workpaper are flagged `POST_REPORTING` and notify the CCO and, where linked, the auditor.

**FR-P00-36 — Access log and break-glass.** `core.access_log` (append-only; reads of SPI/SEALED/CREDENTIAL/BOARD_CONFIDENTIAL/REGULATOR_CONFIDENTIAL data, decrypts, reveals, exports, platform-scope reads, supervisor and auditor views). `core.break_glass_events` (actor, tenant, scope, justification ≥ 30 characters, linked incident or ticket, approver for two-person mode, start, end ≤ 4 hours default, tenant admin notified at — immediately by email and in-app, DPO notified). P01 builds the UI; P00 builds schema, service and notifications (NN-30).

### 4G. Bitemporal data, identifiers, money and citations

**FR-P00-37 — Bitemporal convention (NN-07).** Tables holding regulatory content, rule packs, applicability, settings, legal-entity master data, organisational structure and any value whose "as of" history matters carry:

- `valid_from date|timestamptz`, `valid_to` (open-ended `infinity`) or a `valid_period tstzrange` — when the fact is true in the world (e.g., an amended paragraph effective 1 April 2027);
- `recorded_at timestamptz`, `superseded_at timestamptz` (open-ended `infinity`) — when the system knew it.

Rows are never updated in place: a change closes the current row (`superseded_at = now()`) and inserts the new version in the same transaction. An exclusion constraint (`EXCLUDE USING gist (key WITH =, valid_period WITH &&) WHERE (superseded_at = 'infinity')`) prevents overlapping current versions. `packages/bitemporal` provides `asOf(validDate)`, `asRecorded(instant)` and `asOfRecorded(validDate, instant)` query builders. Compliance instances pin the content version they were generated from (NN-03), so a later amendment never rewrites a completed item; it produces a change impact (P05).

**FR-P00-38 — Identifiers.** Entity IDs are opaque prefixed ULIDs (`<prefix>_` + 26 Crockford base32 chars), stored as `text` with a `CHECK` on the pattern, generated in the application by `packages/ids`. Prefix registry in Appendix B §B.1 (e.g., `ten_`, `len_`, `usr_`, `mbr_`, `ins_` instrument, `ivr_` instrument version, `cls_` clause, `obl_` obligation, `qst_` question, `cin_` compliance instance, `evd_` evidence, `doc_`, `dvr_` document version, `tsk_`, `apr_` approval, `cor_`, `aev_`, `out_` outbox). Event IDs are UUIDv7 (RFC 9562) as the Ecosystem Spec §3.2 requires. Human-facing reference numbers (compliance IDs shown in Excel column `comp_id` (v1.0: E) "CompID", ticket numbers, invoice numbers) come from `core.sequences` with tenant- and series-scoped gap-free counters where law requires gap-free series (GST invoices — Rule 46 CGST Rules: consecutive serial number unique for a financial year) and gap-tolerant counters elsewhere.

**FR-P00-39 — Money and numbers.** Amounts `NUMERIC(20,4)` with `currency char(3)` (ISO 4217; INR default); rates `NUMERIC(12,8)` (percent per annum, day count stated); ratios `NUMERIC(18,10)`; counts `bigint`. Application arithmetic uses `packages/money` (decimal.js, precision ≥ 40, explicit rounding mode per calculation; banker's rounding prohibited unless a rule says so; GST rounding per CGST rules [VERIFY]). JSON carries money as `{"amount": "125000.00", "currency": "INR"}` (Ecosystem Spec §5.1). Property-based tests for every calculation package (NN-22).

**FR-P00-40 — Citation value object.** `packages/citations` defines `Citation { authority_code, instrument_id, instrument_version_id, instrument_ref (e.g., "RBI/DoR/2025-26/XXX" or "IFSCA/2021-22/GN/REG014"), paragraph_ref (e.g., "Para 21(3)(b)", "Reg 4(2)(a)", "Rule 7(1)"), source_url, source_sha256, retrieved_at, binding_level (LAW | REGULATION | DIRECTION | CIRCULAR | GUIDANCE | FAQ | STANDARD | GOOD_PRACTICE | TENANT_POLICY) }`. Obligations, questions, AI answers, rule-pack entries and legal rules (Appendix G `LR-*`) carry citations; the UI renders them consistently with a deep link to the source paragraph where available (NN-06).

### 4H. Events, outbox, inbox and idempotency

**FR-P00-41 — Two event families.** (a) **Internal domain events** — `type` `in.lawdocscomply.<module>.<EventName>.v<major>` — flow between LDC modules and never leave LDC. (b) **Ecosystem events** — `type` `in.infrabyx.<domain>.<EventName>.v<major>` exactly as the Ecosystem Spec §3.2 and Part 6 define them (for example `in.infrabyx.grc.ObligationPublished.v1`, `in.infrabyx.grc.EvidenceSubmitted.v1`, `in.infrabyx.audit.ExternalAccessGranted.v1`), with `source` `urn:infrabyx:ldc:<tenantid>`, and are published only by the `int` gateway (P18) after data-class and consent checks. A module never emits an ecosystem event directly; it emits an internal event that `int` maps under a versioned mapping. This keeps LDC's internal refactoring from breaking other products.

**FR-P00-42 — Transactional outbox.** `core.outbox` (partitioned daily; columns per CloudEvents 1.0: `id` UUIDv7, `source`, `type`, `subject`, `time`, `datacontenttype`, `dataschema`, `data` (jsonb), `tenantid`, `reid`, `dataclass`, `schemaver`, `seq` (per subject), `correlationid`, `causationid`, `traceparent`, `consentref` or `legalbasis`, `status`, `attempts`, `next_attempt_at`, `published_at`). Written in the same transaction as the state change. `outbox-relay` publishes in `seq` order per `subject` to internal consumers (in-process for the monolith, Temporal signals or Redis streams for workers) and to `int` for ecosystem mapping; at-least-once with exponential backoff, dead-letter after 12 attempts with an alert. Retention ≥ 90 days for replay (365 days for events the Ecosystem Spec marks as long-replay).

**FR-P00-43 — Inbox and idempotency.** `core.inbox` stores `(source, id)` and business key for every consumed event before processing (deduplication); gaps in `seq` are parked 15 minutes, then a catch-up fetch is attempted, then `ReconciliationBreakRaised` (Ecosystem Spec §3.5). `core.idempotency_keys` for every mutating API: `(tenant_id, key, route, request_hash)` → stored response for 24 hours; reuse with a different body returns `idempotency-key-reuse` (422).

### 4I. Feature flags and configuration heads

**FR-P00-44 — Feature flags.** Flag service (Unleash self-hosted in ap-south-1, or the group-standard tool per ADR-0012) behind `packages/config` so code never calls the vendor SDK directly. Flags are registered in `core.feature_flags` with `key`, `owner`, `purpose`, `default`, `kill_switch` (bool), `approver_role` (for flags that gate legally or commercially sensitive features — for example `marketplace.commission.advocates.enabled`, `ret.portal_submission.enabled`, `ai.agent.autonomous_send.enabled` — which must remain OFF until the named approver records an approval with evidence), `expires_at` (temporary flags), `linked_open_item` (OI ID). Flag changes in prod are audited and, for approver flags, require maker-checker.

**FR-P00-45 — Configuration heads.** Create `cfg.settings_registry` (key, module, tier L/G/T, type, default, bounds, scope levels allowed, approver role, description, "i" help key, linked legal rule) and `cfg.setting_values` (bitemporal; scope: platform → group → tenant → legal entity → org unit → user) so that P01 and P02 can register settings from day one (NN-28). P02 builds the resolver, Studio UI and rule-pack engine on these tables without migration.

### 4J. Storage and evidence

**FR-P00-46 — Buckets** (ap-south-1, replicated to ap-south-2; all block public access; SSE-KMS; access only via VPC endpoint policies and presigned URLs valid ≤ 5 minutes):

| Bucket | Purpose | Lock / lifecycle |
|---|---|---|
| `ldc-{env}-quarantine` | All uploads land here first | Delete after 24 h |
| `ldc-{env}-documents` | Working documents, drafts, templates | Versioning; no lock; lifecycle to infrequent access after 180 days |
| `ldc-{env}-evidence` | Compliance evidence, approved policies, signed minutes, filed returns and acknowledgements, audit workpapers, anchors | Object Lock **compliance mode**; default retention 8 years from write (Companies Act 2013 s.128(5) books of account 8 years; PMLA 5 years; tenant may configure longer per class, never shorter than the platform floor); legal hold per object |
| `ldc-{env}-exports` | Generated export packages and reports | Lifecycle delete 7 days (P19 can extend for BYO transfer) |
| `ldc-{env}-backups` | Logical backups, Supabase dumps during beta | Object Lock governance mode in `ldc-backup` account; 35 days daily, 13 months monthly, 8 years FY-end |

**FR-P00-47 — Evidence ingest skeleton.** `POST /v1/documents/upload-intents` returns a presigned PUT to quarantine with required `x-amz-checksum-sha256`; on object creation `EvidenceIngestWorkflow` (1) validates MIME by magic bytes against the allow-list (PDF, DOCX, XLSX, XLS, CSV, PPTX, TXT, EML, MSG, PNG, JPEG, HEIC, TIFF, ZIP for folder intake; MP4/M4A for meeting recordings — size limits configurable through `dms.upload.max_mb`, default 100 MB per file (raised by platform setting only), 2 GB for recordings); (2) scans with ClamAV (signatures hourly) and rejects macro-enabled Office files unless the tenant allows them with a warning; (3) recomputes SHA-256 server-side and compares; (4) copies to `documents` or `evidence` by artefact class; (5) for evidence, sets retention and writes `dms.evidence_ledger` (hash-chained per tenant); (6) emits `in.lawdocscomply.dms.DocumentIngested.v1`; (7) deletes the quarantine object. Rejections return `LDC-DMS-002` (malware) or `LDC-DMS-003` (checksum mismatch). P07 builds OCR, versioning, sharing, eSign and folder intake on this pipeline.

### 4K. Observability, errors and performance budgets

**FR-P00-48 — Telemetry.** OpenTelemetry SDK in every app; traces, metrics and logs to an India-hosted backend (self-hosted Grafana LGTM on AWS ap-south-1 or a vendor with India residency — [VERIFY]; no log shipping outside India, CERT-In Directions 28 Apr 2022 require logs of ICT systems for 180 days within Indian jurisdiction). Log schema: JSON, `timestamp`, `level`, `service`, `trace_id`, `span_id`, `tenant_id` (opaque), `user_id` (opaque), `request_id`, `event`, `code`; the PII scrubber removes emails, phone numbers, PAN, Aadhaar patterns, card-number patterns, JWTs and secrets before export (NN-32; test `NN-32_log_scrubber`). Time synchronised to NTP servers of NIC/NPL or traceable to them (CERT-In Directions, item (i)).

**FR-P00-49 — Errors.** RFC 9457 problem details (Ecosystem Spec §3.9): `type` (`https://api.lawdocscomply.com/problems/<code>`), `title`, `status`, `detail` (no PII), `instance`, `code` (`LDC-<MODULE>-<NNN>`), `correlation_id`, `retryable`, `errors[]` (JSON Pointers), plus `user_message_key` for localised, actionable UI messages ("what happened, why, what you can do"). Error-code register in Appendix B §B.7.

**FR-P00-50 — Budgets and SLOs (initial; P24 confirms).** API p95 ≤ 300 ms for reads and ≤ 600 ms for writes at 200 concurrent users per tenant; tenant app first contentful paint ≤ 1.5 s on 4G for dashboards (server components, streaming); availability 99.5% monthly (Ecosystem Spec §3.8 for LawDocsComply), target 99.9% after the AWS production move; RPO ≤ 15 minutes and RTO ≤ 4 hours for prod on AWS; during the Supabase beta, RPO 24 h for region loss (disclosed).

### 4L. Design system, i18n and accessibility foundations

**FR-P00-51 — Design tokens.** Port the owner's Visual Identity and Design Tokens (baseline Part 1 "Visual Identity", "Design Tokens (Machine-Readable)") into `packages/ui/tokens` (colour, typography, spacing, radius, elevation, motion) with light and dark themes and a high-contrast theme; tenant branding (logo, primary colour) is applied only after an automatic WCAG 2.2 AA contrast check (P02). Components on shadcn/ui primitives (Radix) for keyboard and screen-reader support; data-dense grids with TanStack Table (virtualised), charts with an accessible charting library that provides data tables behind every chart (NN-21).

**FR-P00-52 — i18n.** ICU message catalogues in `packages/i18n` (English source; Hindi and other Indian languages added by P23), Indian number formatting (lakh/crore) as a user preference, dates in `DD MMM YYYY` with IST default and tenant timezone override, all timestamps stored UTC and rendered in the viewer's timezone with the zone shown on audit screens.

**FR-P00-53 — Help keys.** Every field, column, menu item and status label has a stable help key (`help.<module>.<screen>.<element>`) so that P23 can attach the "i" explanation, glossary entry and tutorial link without code changes (R-020).

### 4M. Seed data

**FR-P00-54 — Seed profiles** (synthetic only; NN: no production data outside prod): `dev` (two tenants, ten users each, a few instruments); `demo` (eight tenants across families — NBFC Middle Layer, NBFC-ICC Base Layer, Urban Co-operative Bank Tier 2, credit co-operative society (state), listed company, AIF, IFSCA Finance Company, insurance broker — with realistic synthetic compliance data, risks, committees, policies and returns calendars); `load` (500 tenants, 2 million compliance instances, 5 million evidence metadata rows); `beta-mirror` (a synthetic re-creation of the shape of the Branch International beta tenant for UAT, built from counts in `05-tenants-and-users.md`, with no real values). *(v1.1, X1)* Platform **content seeds** are distinct from synthetic tenant seeds: every environment loads the RBI Directions catalogue (`catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`, 320 rows; D-39) through P03's `CatalogueSeedWorkflow` (FR-P03-09) as instrument metadata with coverage state `PLANNED`/`IN_PREPARATION`; this is public regulatory metadata, not tenant data. P00 also creates schema `aig` (AI governance, P12 §4P) with an expand–contract migration from any v1.0 `dpc.ai_systems` table and a compatibility view for one release. Names, PANs and CINs in seeds use reserved invalid patterns (PAN with fourth character `Z`-series flagged synthetic [REC]; CIN prefix `X`) so they can never be mistaken for real identifiers.

### 4N. Data migration framework and waves

**FR-P00-55 — Migration principles.** (1) Source is a point-in-time restore of MongoDB, never the live cluster. (2) Every migrated row carries `core.migration_lineage` (`source_system = 'ldc-legacy'`, `source_collection`, `source_id`, `source_hash`, `migration_run_id`, `transform_version`). (3) Transforms are code in `tools/migration/` with unit tests and golden files. (4) Each run produces a reconciliation report (counts per entity, sums of numeric fields, null-rate deltas, orphan checks, hash of the canonical source set) stored as evidence. (5) Runs are idempotent and repeatable; the final run happens during the cut-over window. (6) Defects found in legacy data are not silently fixed: they are migrated as-is with a data-quality flag and an owner task, or corrected by a `MIGRATION_FIX` Correction Entry with the owner's approval (FR-P00-34), so the tenant can see exactly what changed.

**FR-P00-56 — Wave 1 (in P00): content.** Legacy question banks (RBI NBFC Base/Middle/Upper Layer, CIC, Companies Act and any others found) → `cnt` (authorities, instruments, instrument versions, clauses where derivable, base questions with the 30-column payload of Appendix E mapped to typed fields). Where the legacy data lacks a citation, applicability layer, type, frequency or evidence field, the row is imported in state `NEEDS_REVIEW` and appears in the content-review queue (P03) — it is not published to tenants until a content checker approves it. The IFSCA question sheets in the owner's `IFSCA Documents` folder and the Sep 2026 RBI Master Direction sheets (RBI/DoS/2026-27/460–468 [VERIFY numbering]) are imported through the P03 Excel importer once it exists; P00 only loads the legacy database banks.

**FR-P00-57 — Wave 2 (rehearsed in P00, executed at P01 exit): tenants, users, compliance records.** Tenants → `core.tenants` and `core.legal_entities`; users → Keycloak (P01; password hashes migrated only if the legacy algorithm is bcrypt/argon2 and Keycloak can import it, otherwise users reset passwords by email link at first login, and all users must enrol MFA); roles → nearest role codes with an owner-approved mapping table; compliance records, statuses, dates, comments → `cmp` with the original timestamps preserved in `occurred_at` and a synthetic ledger "genesis" event per tenant summarising imported history (`core.migration_genesis`: counts and source hash), because the legacy app had no tamper-evident ledger — the new chain starts at migration and says so.

**FR-P00-58 — Wave 3 (rehearsed in P00, executed at P07 exit): documents and evidence.** Legacy files → quarantine → ingest pipeline → `dms` with original filenames, upload dates and uploader references; checksum computed at migration (the legacy system has no prior checksum, so the export certificate states "integrity assured from migration date").

**FR-P00-59 — Dual-run and cut-over.** Before cut-over, the beta tenant uses UAT (with `beta-mirror` plus a migrated copy of their own data in a production-grade environment, never in non-prod) for two weeks of parallel run; a daily diff report compares legacy and new for counts and statuses. Cut-over runbook (§5.5) with go/no-go criteria, freeze of legacy writes, final delta migration, DNS switch, smoke tests, 48-hour hypercare, and legacy read-only access for 90 days, then archive.

### 4O. Export-mapping registry and NN-10 contract (foundation for P19)

**FR-P00-60 — Export mappings.** For every tenant table, `db/export-mappings/<schema>.<table>.yaml` declares: the export folder path in `LDC-EXPORT-1.0` (Appendix M), file name pattern, format (XLSX/CSV/JSON/DOCX/PDF/original), columns with human-readable headings, data-class handling (restricted folder for `HR`, `SEALED`, `LEGAL` privileged, `CREDENTIAL` excluded — credentials are never exported, only their metadata), and the join path to resolve references into readable names. `NN-10_export_mapping_complete` fails CI if a table with `tenant_id` lacks a mapping or a mapping references a dropped column. This is what keeps the client's folder structure stable across code changes, server changes and data-centre moves (R-021): the folder taxonomy is a versioned contract, not a by-product of the schema.

### 4P. Architecture decision records

**FR-P00-61 — ADRs to write in P00** (`docs/adr/`, MADR format, each with context, options, decision, consequences, review date):

| ADR | Subject |
|---|---|
| 0001 | Modular monolith on NestJS 11 + Next.js 16; pinned versions |
| 0002 | PostgreSQL major version; extensions; RLS as tenant wall |
| 0003 | Keycloak realms and clients (detailed in P01) |
| 0004 | Cerbos (or OPA) for RBAC+ABAC decisions (P01; Appendix D) |
| 0005 | Temporal for long-running workflows; self-hosted in ap-south-1 |
| 0006 | Hosting: Supabase Mumbai for non-prod/beta, AWS RDS/Aurora ap-south-1 + ap-south-2 DR for production |
| 0007 | Connection pooling and session context |
| 0008 | Audit ledger with hash chain, anchors and Correction Entries (D-02) |
| 0009 | Bitemporal modelling |
| 0010 | Identifiers (prefixed ULID; UUIDv7 events) |
| 0011 | Event families, outbox and ecosystem mapping |
| 0012 | Feature-flag service |
| 0013 | Search: OpenSearch with PostgreSQL FTS fallback |
| 0014 | Object storage, Object Lock and retention floors |
| 0015 | Document generation (docxtemplater + Gotenberg; Word tracked-changes generation in P07) |
| 0016 | DNS and domains |
| 0017 | Sealed database for NN-13 classes |
| 0018 | Data-class catalogue and field-level encryption |
| 0019 | Legacy migration strategy and cut-over |
| 0020 | Export contract LDC-EXPORT-1.0 as a schema-change gate |

### 4Q. Regional cells, change batches and v1.1 foundations *(v1.1)*

**FR-P00-62 — Cell architecture (D-42, NN-24 amended).** The production estate is a set of **region cells**. A cell is a complete, independently deployable copy of the data plane and application tier for one region: PostgreSQL cluster (`ldc_core` + `ldc_sealed`), S3 buckets (documents, evidence with Object Lock, exports, backups), KMS keys, Redis, OpenSearch, Temporal namespace, workers, outbox relay and an India-style DR pair inside the same legal area. Cells in v1.1: `IN` (ap-south-1, DR ap-south-2) live; `EU` (eu-central-1, DR eu-west-1 or another EU region), `GCC` (me-central-1 UAE, DR per Appendix Y), `SG` (ap-southeast-1, DR per Appendix Y), `US` (us-east-2, DR us-west-2) defined in Terraform as modules but not deployed until the owner opens them (`core.region.cells_for_sale`). A thin **global control plane** in `IN` holds only the tenant directory (tenant id, slug, home cell, status, domains), routing, the platform content plane catalogue metadata and the console; it holds no tenant business data and no personal data beyond staff accounts. Requests are routed to the home cell by host (`<slug>.lawdocscomply.com`) or by a signed tenant hint from the directory; a tenant's data never crosses cells except (a) platform content packs replicated outward from `IN` (no personal data), (b) aggregate group views across linked tenants computed from pre-aggregated, de-identified metrics, (c) a region-migration run (P24) with owner approval and tenant consent. Each cell has its own Terraform workspace, release ring (P24 FR-P24-46) and sub-processor entries (Appendix Q §Q.9).

**FR-P00-63 — Cell-aware code rules.** No code may assume a single database or bucket: connection and bucket resolution go through `packages/tenancy` (`cellFor(tenantId)`), background jobs are scheduled per cell, cron times are evaluated in each tenant's timezone and the platform 20:00 IST scan runs in `IN` while jurisdiction scans run at local evening time in their cell (Appendix Y). Identifiers stay globally unique (ULIDs) so that a tenant can move cells without re-keying (NN-11). A CI test boots two cells in Docker Compose and proves no cross-cell query exists (`NN-24_cells_isolated`).

**FR-P00-64 — Change batches and undo windows (NN-49).** `core.change_batches` (`id` `chb_`, tenant, kind — `IMPORT`, `BULK_EDIT`, `BULK_REASSIGN`, `BULK_STATUS`, `CONFIG_APPLY`, `TEMPLATE_APPLY`; actor, on-behalf-of, created_at, `undo_until`, status `OPEN/UNDONE/FINAL/PARTIAL_UNDO`) and `core.change_batch_items` (target table and id, operation `CREATE/UPDATE/DELETE`, before-image hash, after-image hash, compensating action). Every bulk or import operation in every module writes through `packages/batches`; "Undo" executes compensating actions in reverse order inside one transaction where possible, skips items changed by a later action (listed for manual decision) and writes the audit ledger. After `undo_until`, the batch is `FINAL` and changes follow normal correction rules (NN-02). Undo is not available for sealed-class records, filed returns, signed documents or anything already sent outside the tenant.

**FR-P00-65 — Three-date value object (NN-48).** `packages/domain` defines `ComplianceDates { act_date, evidence_date, approval_date, recorded_at }` used by `cmp`, `ret`, `gov`, `lab` and `lit`: the **act date** is when the obligation was actually performed or filed (taken from the acknowledgement where one exists), the **evidence date** is when proof was uploaded, the **approval date** is when the checker approved. Timeliness (`complied` vs `complied_late`) is computed from the act date against the statutory due date; internal SLA performance is computed from approval date against the internal target. Users can enter an act date in the past only with an evidence item that shows it (for example a filing acknowledgement), otherwise the act date defaults to the submission date.

**FR-P00-66 — New module skeletons (D-47, D-48).** Add modules `gem` (global entity management; sub-module of governance with its own schema), `prt` (partner network), `lit` (legal matters, notices, litigation, contracts, licences and ethics registers — P26), `esg` (sustainability — P27); module `rpt` (reports, MIS, board packs, analytics) is owned by P28. Ownership in `db/ownership.yaml`; export mappings registered before each phase exits (NN-10). In `gov`, related-party transactions use table prefix `gov.rpt_txn_*` so that `rpt` always means the reporting module.

**FR-P00-67 — AI foundations ready from day one (Appendix AA).** P00 creates the empty `ai` module with: the provider adapter interface (`AI_PORT`) and routing table keyed by data class and cell (NN-41: regulated classes never leave the home cell's legal area); the AI kill-switch registry (`ai.kill_switches`: scope platform/provider/tenant/agent/skill/mission/connector, state, set_by, set_at; propagated through Redis pub-sub and checked before every model or tool call, ≤ 60 s — NN-51); the model registry (`ai.models`: provider, model id, version, region, data classes allowed, evaluation status, approved_at); OpenTelemetry GenAI semantic conventions for traces; and an evaluation runner stub wired into CI (P24 FR-P24-48). No model is called in P00.

**FR-P00-68 — Configuration templates and sandbox foundations.** `cfg.config_templates` (name, scope family/size/group, settings bundle, version) and the ability to provision a **sandbox tenant** cloned from a tenant's configuration (no business data) for UAT and simulations (P02 FR-P02-81; P01 FR-P01-50). Sandboxes are tagged, cannot receive live provider traffic (`provider_routing` guard) and are deleted after 90 days unless renewed.

**FR-P00-69 — SLO catalogue and FinOps tags.** Every service and job carries cost-allocation tags (`tenant_cell`, `module`, `tenant_tier`) so that P24 can produce per-tenant and per-module cost dashboards (TM-168) and an SLO catalogue with error budgets (TM-165).

### 4R. Business reference IDs and history by ID *(v1.2; D-51, D-52, NN-56, NN-57; Appendix B §B.12)*

**FR-P00-70 — `packages/bizid`.** One library for every business reference ID family in Appendix B §B.12.1 (CompID platform and tenant, compliance instance, RiskID library and tenant, KRI, Control, GovID library and tenant, AUD, LIT, ESG, AIS, HC). It exposes `parse(id) → {kind, segments}` (case-insensitive, trims, rejects reserved words; LDC-CORE-030), `format(kind, segments, seq)`, `isAlias(value)`, `resolve(value) → canonical` (registry and alias lookup; LDC-CORE-031), `instanceRef(compId, period, entityCode?)` with the period rules of §B.12.1 (labels by the end year of the entity's financial year, validated against the item's frequency; LDC-CORE-034), and a Zod schema per family for API validation. The same parser ships to the web client so that pasted IDs are recognised in search, filters, conversations (`#RBI-NBFC-GOV25-0042` becomes a link) and import previews. No module may build an ID by string concatenation; a lint rule (`no-raw-bizid`) enforces this.

**FR-P00-71 — Transactional allocator.** `core.allocate_business_ids(kind, series_key, n, aggregate_type, aggregate_ids[])` is the only way to issue an ID; P03's `IdService.reserve(id_type, scope, n)` and the internal endpoint `POST /internal/ids/reserve` are this allocator (P03 FR-P03-103, OI-P03-16). It locks the `core.bizid_sequences` row, takes `n` consecutive numbers, skips any value present in `core.bizid_aliases`, inserts `core.business_ids` rows (state RESERVED or ASSIGNED per §B.12.3) and returns the IDs in the order of `aggregate_ids` (source-row order, so CompIDs follow the S. No. order of the master direction). It must run inside the transaction that creates or publishes the records (`core.require_txn_context()`; LDC-CORE-127); a rollback leaves a gap and never a duplicate. Sequences never decrease (trigger; LDC-CORE-121); a platform series widens from 4 to 5 digits only after 9999. Performance: 500 IDs in one call ≤ 200 ms p95; two concurrent importers on the same instrument serialise on the series row without deadlock (test with 20 parallel workers).

**FR-P00-72 — Segment registries.** P00 creates and seeds `core.bizid_segment_codes` (authority codes, taxonomy codes, governance types, reserved words), `cnt.inst_short_codes` (owned by P03 FR-P03-102: `<SUBJECT><YY>`, e.g. `GOV25`, `KYC16`; frozen after the first CompID reservation; LDC-CORE-032 when missing), `core.tenant_codes` in the global directory (four characters, first a letter, proposed from the organisation's name initials, editable in onboarding until the first tenant ID is issued, then locked; reserved words and authority codes refused; LDC-CORE-033, LDC-CORE-125) and `core.legal_entities.entity_code` (2–10 characters, required once a tenant adds a second legal entity). Changes to segment codes are maker-checker platform actions and ledger events.

**FR-P00-73 — Registry lifecycle.** `core.business_ids` binds each ID to exactly one aggregate for ever (immutable columns; LDC-CORE-120). State changes follow §B.12.3: RESERVED (at import or AI-draft preview) → ASSIGNED on publish, or ASSIGNED directly on creation for tenant records; RESERVED → VOID when a draft row is rejected or abandoned; ASSIGNED → RETIRED, MERGED (with `MERGED_INTO`) or split (new IDs with `SPLIT_FROM`); a provision re-cited in a replacement instrument keeps its CompID, and `CONTINUED_AS` is recorded only when the content checker treats the new provision as a different, succeeding obligation. Writes against a RETIRED, MERGED or VOID ID are refused with the successor shown (LDC-CORE-122). Retire, merge, split and alias actions are maker-checker (platform: `plt_content_maker` and `plt_content_checker`; tenant: module owner and `ten_admin` or `ten_cco`), need a reason and an effective date, and are ledger events. A daily `BizIdIntegrityCheckWorkflow` proves that every business-ID-bearing record has exactly one ASSIGNED or RESERVED registry row and vice versa, and raises an engineering incident on any mismatch.

**FR-P00-74 — Aliases and legacy IDs.** `core.bizid_aliases` stores, with the P03 alias types, IDs from the owner's v1.0 sheets (`V10_HYPHEN`), v1.1 pre-production IDs (`V11_DOTTED`), legacy LawDocsComply IDs (`MONGO`, migration waves 1 and 2), numbering from a client's own tracker or Excel (`TRACKER`, captured on import, P01 FR-P01-43 and P03), other migrated references (`MIGRATION`), replaced library placeholders (`HC_PLACEHOLDER`) and previous-format non-CompID references (`PREVIOUS_FORMAT`). An alias resolves to one canonical ID; it can never equal a live ID (LDC-CORE-123) and the allocator never issues a value that exists as an alias. Migration rule: a legacy CompID that already matches the `COMP` pattern under an approved instrument code is kept as the canonical ID and the series is set above the highest migrated number; any other legacy reference becomes an alias of a newly issued ID. The migration reconciliation report (FR-P00-55 to FR-P00-57) lists every legacy → canonical mapping for the owner's sign-off.

**FR-P00-75 — Ledger keyed by business ID (NN-57).** `core.audit_events.business_ids text[]` (GIN index per partition) is filled by `core.append_audit_event` from the aggregate's registry binding plus explicit IDs passed by the caller (the instance ref, the other side of a link, the IDs in an export or conversation). Aggregates registered in `core.bizid_aggregate_types` must never write an event with an empty array (LDC-CORE-126). The CI rule `NN-57_every_event_has_bizid` walks the action catalogue, executes each action on seeded data and fails the build if any ledger row for a business-ID-bearing aggregate lacks its ID. In the same transaction the function writes `core.bizid_history_index` rows (one per ID and event, with a category: CONTENT, ASSIGNMENT, STATUS, EVIDENCE, REVIEW, CONVERSATION, EXPORT, AI, LINK, CORRECTION, REGISTRY), which feed the per-cell OpenSearch timeline; the ledger stays authoritative and `HistoryIndexRebuildWorkflow` rebuilds the index from it.

**FR-P00-76 — History API and timeline component.** Endpoints of Appendix B §B.12.6: resolve, batch resolve, `GET /v1/history/{bizId}` (merges the platform content chain and the tenant chain; filters by date, category and actor; `include_instances` returns all periods of a CompID; `include_lineage` follows `CONTINUED_AS`, `SPLIT_FROM` and `MERGED_INTO`), history export (PDF, XLSX, CSV, JSON; optional Bharatiya Sakshya Adhiniyam 2023 s.63 certificate, NN-09) and chain verification for the returned events. Visibility follows Appendix D §D.19: actors are shown by name to roles that can see the record; external auditors and supervisors see names only within their grant; personal stars are visible only to their owner (and to auditors as counts); sealed-class field values never appear (only "changed"). The shared React component `<HistoryTimeline bizId>` (virtualised list, day separators, category chips, diff view, "verify" button, export) is used by the CompID, RiskID, GovID, KRI, Control, AUD, LIT, ESG and AIS drawers. Performance: first 50 entries ≤ 400 ms p95 on five years of history.

**FR-P00-77 — Universal resolver, deep links and search.** Route `/id/<bizId>` resolves any family and alias to the right drawer; short routes `/c/<CompID>[/<PERIOD>]`, `/r/<RiskID>`, `/g/<GovID>`, `/k/<KRI>`, `/x/<CTL>`. The global search box recognises a pasted ID or alias and opens it directly; an ID the user cannot see returns the same "not found" message as a non-existent one (no existence leak; LDC-CORE-031). Retired IDs open with a banner naming the successor.

**FR-P00-78 — Cross-ID links service.** `packages/links` manages `core.bizid_links` (typed, dated links between any two business IDs within a tenant: MITIGATES, MONITORS, ADDRESSES, GOVERNS, EVIDENCES, TESTS, RELATES, REPORTS_ON, AFFECTS; source AUTHOR, USER, AI_ACCEPTED, IMPORT). It validates both ends through the registry, refuses links to RETIRED/VOID IDs, copies platform default links (template columns 38–39) when an item becomes applicable to a tenant, and writes one ledger event carrying both IDs. The Links tab of every drawer reads it in both directions. Vidhi may suggest links; a suggestion becomes a link only when a person accepts it (source AI_ACCEPTED).

---

## 5. Workflows and state machines

### 5.1 Correction Entry (canonical; Appendix A §A.2)

```
DRAFT --submit--> SUBMITTED --approve(checker≠maker, step-up MFA)--> APPROVED --apply--> APPLIED
  |                  |--reject(reason)--> REJECTED
  |                  |--withdraw--> WITHDRAWN
APPLIED --new Correction Entry with scope=REVERSAL--> REVERSED
```

Guards: `justification.length ≥ 50`; supporting document present where the reason code requires it; target exists and is not under legal hold (for `DOCUMENT_VERSION`); for platform-initiated corrections of tenant data with `tenant_ack_mode = PRIOR`, `APPROVED → APPLIED` waits for `TenantAcknowledged` or 5 working days, after which the platform checker must re-confirm and the tenant is notified that the correction proceeded without acknowledgement (the tenant's objection, if any, is attached). Timers: SUBMITTED older than 3 working days escalates to `plt_security_officer` (platform) or `ten_cco` (tenant). Every transition writes an audit event; `APPLIED` writes the target change and the correction link in one transaction.

### 5.2 Audit chain verification incident

`VERIFY_FAILED → INCIDENT_OPEN (Critical) → CONTAINED (Governed config frozen; exports carry a banner) → ROOT_CAUSE_RECORDED → REMEDIATED (chain continues from a signed "break notice" event; never rewritten) → TENANTS_NOTIFIED → CLOSED`. A broken chain is never "repaired" by recomputing hashes; the break notice records the last verified anchor, the affected range and the investigation reference.

### 5.3 Tenant provisioning (system part; the user journey is P01)

`REQUESTED → RECORDS_CREATED (tenant, platform legal-entity stub, default org units, chain genesis) → KEYS_READY (data keys; dedicated CMK if `dedicated_key`) → BUCKET_PREFIXES_READY → SEARCH_INDEX_READY → SETTINGS_DEFAULTED (from the entity-family setting pack, P02) → ACTIVE_TRIAL` (or `ACTIVE` for contract tenants). Implemented as `TenantProvisionWorkflow` (Temporal) with compensation for each step; idempotent on `tenant_id`; emits `in.lawdocscomply.core.TenantProvisioned.v1` (internal) and, through `int`, the Ecosystem Spec provisioning acknowledgement to the Operations Hub (`ops.provisioning:ack`, business contact data only, `legalbasis = CONTRACT_PERFORMANCE_VENDOR`).

### 5.4 Migration run

`PLANNED → SNAPSHOT_TAKEN (Atlas PITR restore id, hash) → EXTRACTED → TRANSFORMED → LOADED (in a staging schema) → RECONCILED (report) → REVIEWED (content checker / owner) → PROMOTED (moved to live schema in one transaction per entity batch) | ROLLED_BACK`. A run cannot be promoted if reconciliation shows a count mismatch, an orphan, or a defect rate above the threshold (`migration.max_defect_rate` default 0.5%).

### 5.5 Cut-over runbook (summary; full text `docs/runbooks/cutover.md`)

T-14 days: parallel run starts; daily diff. T-3: go/no-go rehearsal on a fresh restore. T-1: notify users (email + in-app banner in legacy) with the window. T0: legacy set read-only (maintenance banner); final delta snapshot; waves 2 (and 3 if P07 done) final run; reconciliation; owner go/no-go; DNS switch (TTL lowered to 300 s at T-2); smoke tests by role; users receive "Welcome to the new LawDocsComply" email with MFA enrolment link. T+48 h hypercare. Rollback criterion: any reconciliation mismatch on compliance records or evidence, or P1 defect without a fix in 4 hours → revert DNS, legacy back to read-write, incident report. Legacy read-only access for 90 days, then archive (8-year retention of the archived database snapshot under Object Lock).

### 5.6 Region-cell request routing *(v1.1)*

`request → resolve tenant (host or signed hint) → directory lookup (cached 60 s) → home cell → route` — if the cell is in maintenance, the user sees a status page for that cell only; other cells are unaffected. A tenant in `MIGRATING` state is read-only until cut-over completes (P24 FR-P24-16).

### 5.7 Change batch and undo *(v1.1)*

`OPEN (undo_until in future) → UNDONE | PARTIAL_UNDO | FINAL (timer)`. Partial undo lists items changed after the batch for a manual decision; every transition writes the audit ledger (NN-45).

### 5.8 Business-ID lifecycle *(v1.2)*

`RESERVED → ASSIGNED → RETIRED | MERGED`; `RESERVED → VOID`; split creates new ASSIGNED IDs with `SPLIT_FROM`; re-cited provisions keep their CompID and only a succeeding, different obligation records `CONTINUED_AS` (Appendix B §B.12.3). Every transition is maker-checker except reservation, assignment and voiding (system, inside the creating or publishing transaction). On `CONTINUED_AS`, P05 opens a change task per tenant to move open instances to the successor; completed instances never move (NN-03). The History tab follows lineage so a user opening the successor sees the predecessor's timeline under a divider "Before 28 Nov 2025: RBI-NBFC-SBR23-0050".

---

## 6. Screens and UX

P00 screens are platform-internal and minimal; they must still meet WCAG 2.2 AA (NN-21) and use the design system.

| Screen ID | Name | App / menu path | Roles | Notes |
|---|---|---|---|---|
| SCR-CORE-01 | Platform home (health) | console › Home | plt_* | Environment, build version, flag count, outbox lag, DLQ size, last chain verification, last anchor, migration status |
| SCR-CORE-02 | Tenants (list and detail) | console › Tenants | plt_super_admin, plt_support (masked) | Read-only in P00 except provisioning; detail shows legal entities, status history, isolation tier, keys (ARNs masked) |
| SCR-CORE-03 | Feature flags | console › Platform › Flags | plt_super_admin, approver roles | Approver flags show the required approver and evidence; maker-checker on prod |
| SCR-CORE-04 | Audit explorer (platform chain) | console › Audit › Platform chain | plt_auditor, plt_security_officer | Filter by actor, action, aggregate, date; verify button runs on-demand verification of a range; export with s.63 certificate (NN-09) |
| SCR-CORE-05 | Correction Entries | console › Audit › Corrections | plt_super_admin (maker), plt_security_officer / designated checker | Create wizard: choose scope → target picker → shows current value and history → new value → effective date → reason, justification, documents → preview of effects (what tenant will see) → submit. Typed confirmation for `MASTER_DATA` and `DOCUMENT_VERSION` |
| SCR-CORE-06 | Migration console | console › Platform › Migration | plt_super_admin, plt_content_maker/checker | Runs, reconciliation reports, defect lists with assign-to, sample-review mode (side-by-side legacy vs new), promote / roll back |
| SCR-CORE-07 | Outbox and integrations health | console › Platform › Events | plt_super_admin, plt_support | Lag per subject, DLQ with replay (reason required), consumer status |
| SCR-CORE-08 | Platform corrections register (tenant view) | app › Settings › Audit & history › Platform corrections | ten_admin, ten_cco, ten_internal_auditor, ten_external_auditor | Every correction affecting the tenant: date, scope, target, old/new (per data-class rules), reason, justification, approvers, documents, acknowledgement button (PRIOR mode), objection form. Exportable. Tenant self-corrections appear in a second tab |
| SCR-CORE-09 | Chain verification (tenant) | app › Settings › Audit & history › Integrity | ten_admin, auditors | Last verification, anchors list with download, "Verify my chain" (runs server-side) and link to the offline `ldc-verify` tool |

**v1.2 screens** *(v1.2)*

| Screen ID | Name | App / menu path | Roles | Notes |
|---|---|---|---|---|
| SCR-CORE-10 | Business-ID registry | console › Content › IDs | plt_content_maker (maker), plt_content_checker (checker), plt_super_admin, plt_auditor (read) | Search by ID or alias; series view (next number, issued, burned, retired); instrument-code and tenant-code queues; retire/merge/split/alias wizards with lineage preview; integrity-check results |
| SCR-CORE-11 | History tab (shared component) | Any drawer › History; app › Settings › Audit & history › History by ID | per Appendix D §D.19 | `<HistoryTimeline bizId>`: category chips, actor filter, date range, include periods, include lineage, field diff, verify, export (PDF/XLSX/CSV/JSON, optional s.63 certificate) |

Empty states explain what will appear and why (e.g., "No platform corrections have been made to your data. If LawDocsComply ever corrects a record, it will be listed here with the reason and approvers."). Error states show the problem `code`, plain-language cause and next step. All tables support keyboard navigation, column chooser, saved views and CSV/XLSX export (export events audited).

---

## 7. Backend design

### 7.1 Modules touched

`core` (owner of everything in this phase), stubs for every other module (FR-P00-08), `xpt` (export-mapping registry tables only), `dms` (ingest skeleton), `cfg` (registry heads), `cnt` (wave-1 load target, schema per Appendix B §B.4).

### 7.2 Tables (key columns; full DDL in Appendix B)

`core.tenants`, `core.tenant_domains`, `core.legal_entities` (bitemporal), `core.registrations`, `core.gstins`, `core.entity_relationships`, `core.org_units` (bitemporal), `core.jurisdictions` (country, state/UT codes incl. Indian state codes for co-operative and labour packs), `core.data_classes`, `core.feature_flags`, `core.feature_flag_approvals`, `core.tenant_modules` (entitlement cache written by `bil`), `core.sequences`, `core.idempotency_keys`, `core.outbox`, `core.inbox`, `core.audit_events` (partitioned), `core.audit_anchors`, `core.audit_annotations`, `core.correction_entries`, `core.correction_acknowledgements`, `core.access_log`, `core.break_glass_events`, `core.migration_runs`, `core.migration_lineage`, `core.migration_genesis`, `cfg.settings_registry`, `cfg.setting_values`, `dms.upload_intents`, `dms.evidence_ledger`, `xpt.export_mappings` (loaded from YAML at deploy).

### 7.3 APIs (REST, `/v1`, OpenAPI 3.1; all mutating calls require `Idempotency-Key`)

| Method and path | Purpose | Roles |
|---|---|---|
| `GET /v1/platform/health` | Liveness/readiness (no auth for liveness; readiness internal) | — |
| `GET /v1/platform/version` | Build, commit, SBOM digest | authenticated |
| `POST /v1/platform/tenants` | Provision tenant (used by P01 onboarding and console) | system, plt_super_admin |
| `GET /v1/platform/tenants/{id}` | Tenant detail | plt_* |
| `GET /v1/audit/events` | Query tenant chain (tenant context) or platform chain (platform context); cursor pagination | ten_admin, auditors, plt_auditor |
| `POST /v1/audit/verify` | Verify a chain range | same |
| `GET /v1/audit/anchors` | List/download anchors | same |
| `POST /v1/corrections` | Create Correction Entry (DRAFT) | plt_super_admin, ten_admin, plt_content_publisher |
| `POST /v1/corrections/{id}:submit` / `:approve` / `:reject` / `:withdraw` / `:apply` / `:acknowledge` / `:object` | Lifecycle | per Appendix D |
| `GET /v1/corrections?tenant=…` | Register | ten_admin, auditors, plt_* |
| `POST /v1/documents/upload-intents` | Presigned upload | authenticated |
| `GET /v1/flags` / `PATCH /v1/flags/{key}` | Flags | plt_super_admin (+ approver) |
| `POST /v1/migration/runs` / `GET …/{id}` / `:promote` / `:rollback` | Migration | plt_super_admin, content checker |
| `GET /v1/events?after=…&types=…` | Catch-up feed for internal consumers (ecosystem feed is P18) | service |

### 7.4 Domain events (internal family; ecosystem mapping in P18)

`in.lawdocscomply.core.TenantProvisioned.v1`, `…core.TenantStatusChanged.v1`, `…core.LegalEntityRegistered.v1`, `…core.LegalEntityAmended.v1`, `…core.CorrectionSubmitted.v1`, `…core.CorrectionApplied.v1`, `…core.CorrectionReversed.v1`, `…core.AuditAnchorPublished.v1`, `…core.AuditChainBroken.v1`, `…core.BreakGlassStarted.v1`, `…core.BreakGlassEnded.v1`, `…core.FeatureFlagChanged.v1`, `…core.MigrationRunPromoted.v1`, `…dms.DocumentIngested.v1`, `…dms.DocumentRejected.v1`.

### 7.5 Jobs and Temporal workflows

`TenantProvisionWorkflow`; `AuditChainVerifyWorkflow` (daily 02:15 IST, weekly full); `AuditAnchorWorkflow` (00:10 IST); `EvidenceIngestWorkflow`; `OutboxRelay` (continuous); `InboxGapRepair` (every 15 min); `PartitionMaintenance` (daily: create future partitions, detach and archive old ones after verification); `CorrectionEscalation` (hourly); `MigrationRunWorkflow`; `DriftDetection` (nightly, infrastructure); `FlagExpiryReminder` (daily).

### 7.6 v1.2 backend additions *(v1.2)*

- **Tables:** `core.bizid_segment_codes`, `core.tenant_codes` (global directory), `cnt.inst_short_codes` (P03), `core.bizid_sequences`, `core.business_ids`, `core.bizid_aliases`, `core.bizid_lineage`, `core.bizid_links`, `core.bizid_aggregate_types`, `core.bizid_history_index`; columns `core.audit_events.business_ids`, `core.legal_entities.entity_code` (DDL in Appendix B §B.12.7).
- **APIs:** `GET /v1/bizids/{bizId}`, `POST /v1/bizids:resolve`, `POST /v1/bizids/{bizId}:retire` · `:merge` · `:split` · `:add-alias` (maker-checker), `GET /v1/history/{bizId}`, `POST /v1/history/{bizId}/exports`, `GET /v1/history/{bizId}/verify`, `GET /v1/links?bizId=` and `POST /v1/links` / `POST /v1/links/{id}:end`, `POST /internal/ids/reserve` (P03 `IdService`), `GET /v1/platform/tenant-codes:check?code=` (anonymous during onboarding, rate-limited).
- **Events:** `in.lawdocscomply.core.BusinessIdIssued.v1`, `…BusinessIdStateChanged.v1`, `…BusinessIdLineageRecorded.v1`, `…BusinessIdAliasAdded.v1`, `…BusinessIdLinkChanged.v1`, `…InstrumentCodeApproved.v1`, `…TenantCodeAssigned.v1`, `…TenantCodeLocked.v1`, `…HistoryExported.v1`.
- **Jobs:** `BizIdIntegrityCheckWorkflow` (daily 02:45 IST), `HistoryIndexRebuildWorkflow` (on demand and after restore), `HistoryExportWorkflow`, `LegacyAliasImport` (migration waves 1–2).
- **Errors:** LDC-CORE-030 to 034, LDC-CORE-120 to 127, LDC-CORE-210 (Appendix B §B.12.9).
- **Platform incident holding state (for P04, NN-60):** the status page publishes `in.lawdocscomply.core.PlatformIncidentDeclared.v1` and `…PlatformIncidentResolved.v1` (incident id, start, end, affected modules, cell), derived from `eng.IncidentDeclared.v1`; P04 pauses accountability clocks for the affected window so that a platform outage is never attributed to a person.

---

## 8. Integrations (ports and adapters)

| Port | P00 adapter(s) | Notes |
|---|---|---|
| `KMS_PORT` | AWS KMS (prod), local KMS emulator (dev) | Data keys per class; asymmetric key for anchors |
| `OBJECT_STORE_PORT` | AWS S3 (Object Lock), MinIO (local) | Presigned URLs only |
| `MAIL_PORT` | Amazon SES ap-south-1 (prod), Mailpit (local) | Transactional only in P00 (correction and incident notices) |
| `FLAG_PORT` | Unleash (or ADR-0012 choice) | Wrapped by `packages/config` |
| `AV_PORT` | ClamAV | Signatures hourly |
| `TSA_PORT` | RFC 3161 TSA (flag OFF) | For anchor timestamps |
| `LEGACY_PORT` | MongoDB read-only (restore) | Migration only; removed after archive |
| `ECOSYSTEM_PORT` | Stub that records events destined for `int` | P18 implements the Integration Spec gateway |

Non-prod routes every outbound port to sandbox or fake (`provider_routing`, FR-P00-10).

---

## 9. Settings and configuration (registered in `cfg.settings_registry`)

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `core.audit.retention_years` | G (tenant may lengthen) | 8 | ≥ 8 (L floor) | plt_super_admin; tenant admin may increase |
| `core.audit.anchor.time_ist` | L | 00:10 | — | — |
| `core.audit.anchor.tsa.enabled` | G | false | — | plt_security_officer |
| `core.correction.tenant_ack_mode` | G | PRIOR for MASTER_DATA, DOCUMENT_VERSION; POST otherwise | PRIOR \| POST | plt_super_admin with tenant agreement |
| `core.correction.justification_min_chars` | L | 50 | — | — |
| `core.correction.escalation_working_days` | T | 3 | 1–10 | ten_admin (tenant corrections) |
| `core.break_glass.max_minutes` | G | 240 | 30–480 | plt_security_officer |
| `core.break_glass.two_person` | G | true for SEALED/CREDENTIAL scopes | — | plt_security_officer |
| `core.tenant.timezone` | T | Asia/Kolkata | IANA zones | ten_admin |
| `core.tenant.fiscal_year_start` | T | 04-01 | any month start | ten_admin |
| `core.tenant.number_format` | T | indian | indian \| international | ten_admin, user |
| `dms.upload.max_mb` | G (lower_only) | 100 | 1–500 | platform / ten_admin (tenants may only lower it) |
| `dms.upload.allow_macro_office` | T | false | — | ten_admin (warning) |
| `dms.evidence.retention_years` | G/T | 8 | ≥ 8 | ten_admin may increase per class |
| `migration.max_defect_rate` | G | 0.005 | 0–0.02 | plt_super_admin |
| `platform.provider_routing.nonprod` | L | sandbox | — | — |

**v1.1 settings** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `core.region.default_cell` | L | IN | — | — |
| `core.region.cells_for_sale` | G (platform) | [IN] | IN, EU, GCC, SG, US | plt_super_admin + second approver |
| `core.batches.default_undo_hours` | G | 24 | 1–168 | ten_admin + ten_cco |
| `core.sandbox.ttl_days` | G (platform) | 90 | 30–365 | plt_super_admin |
| `ai.kill_switch.propagation_slo_seconds` | L | 60 | — | — |

**v1.2 settings** *(v1.2)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `core.bizid.reserve_on` | G (platform) | PREVIEW | PREVIEW \| SUBMIT_FOR_CHECK \| PUBLISH | plt_super_admin |
| `core.bizid.platform_seq_width` | L | 4 | — | — |
| `core.bizid.tenant_seq_width` | L | 5 | — | — |
| `core.bizid.history.default_window_days` | T | 365 | 30–3650 | ten_admin, user (view only) |
| `core.bizid.history.show_actor_names` | T | true | — (auditors and admins always see names) | ten_admin |
| `core.bizid.history.export_certificate_default` | T | false | — | ten_admin |
| `core.tenant_code.editable_until_first_id` | L | true | — | — |

---

## 10. Security, privacy and audit

- NN-01 (RLS + cross-tenant tests), NN-02 (ledger + corrections), NN-07 (bitemporal), NN-09 (Object Lock, SHA-256), NN-10 (export mapping), NN-11 (expand-contract migrations checker), NN-12 (identity minimisation in schema), NN-13 (sealed database), NN-24 (region SCPs), NN-30 (break-glass schema), NN-32 (log scrubber) are implemented and tested in this phase.
- Threat-model the platform core (STRIDE) and record it in `docs/security/threat-model-core.md` (Appendix Q §Q.2 template): tenant breakout, ledger tampering by an insider DBA, super-admin abuse (mitigated by corrections, maker-checker, tenant visibility, anchors), object-store exposure, outbox poisoning, secret leakage in CI.
- Secrets in AWS Secrets Manager (rotation for database credentials); no secrets in environment files committed to Git; gitleaks on every push and full-history scan of the legacy repository.
- Data minimisation: P00 creates no table that stores an Aadhaar number, card number or password (Keycloak owns credentials).
- The beta tenant's data during migration is handled under the existing customer agreement; the agent records its processing in the processing register (Appendix Q §Q.10).

---

## 11. AI touchpoints and guardrails

None in production in P00. The migration console may use an AI-assisted mapping suggestion for legacy question fields to the 30-column contract (for example, splitting a combined "frequency/due date" text), behind flag `migration.ai_assist.enabled` = OFF by default; suggestions are labelled, never auto-applied, and every accepted suggestion is a reviewed transform rule (NN-04, NN-14). No tenant data is sent to any AI provider in P00.

---

## 12. Acceptance criteria (`tests/acceptance/p00/*.feature`)

```gherkin
Feature: Tenant isolation
  Scenario: A user in tenant A cannot read tenant B data through any table
    Given tenants "alpha" and "beta" seeded with generated rows for every tenant table
    When the application role queries every table in tenant context "alpha"
    Then no row with tenant_id "beta" is returned
    And UPDATE and DELETE statements targeting "beta" rows affect zero rows

  Scenario: Missing tenant context fails closed
    Given a database session without app.tenant_id
    When any tenant table is queried
    Then zero rows are returned

Feature: Audit ledger immutability
  Scenario: Ledger rows cannot be updated even by the owner role
    Given an audit event exists in tenant "alpha"
    When ldc_owner executes UPDATE on core.audit_events
    Then the statement fails with LDC-CORE-001

  Scenario: Chain tampering is detected
    Given a chain of 1,000 events for tenant "alpha"
    When a test harness alters one row_hash directly in the database
    And AuditChainVerifyWorkflow runs
    Then AuditChainBroken is emitted with the first failing seq
    And Governed configuration changes are frozen

Feature: Super-admin overrides only via Correction Entries
  Scenario: Super admin corrects a client's date of compliance
    Given compliance instance "CMP-00042" in tenant "alpha" has date of compliance 10-Sep-2026
    When plt_super_admin creates a Correction Entry with new date 08-Sep-2026, reason CLIENT_REQUEST, the client's email attached and justification of 60 characters
    And a different platform checker approves it with step-up MFA
    And the tenant admin acknowledges it
    Then the instance shows 08-Sep-2026 with a "Corrected" badge
    And the history shows the original 10-Sep-2026 value with its original recorded time
    And the tenant's Platform corrections register lists the entry with both approvers
    And the audit event recorded_at is the true time of application

  Scenario: Maker cannot approve own correction
    Given a Correction Entry submitted by user U
    When U attempts to approve it
    Then the request fails with LDC-CORE-005 "Maker and checker must differ"

  Scenario: A document version under legal hold cannot be withdrawn
    Given evidence version V is under legal hold
    When a DOCUMENT_VERSION correction targeting V is applied
    Then the request fails with LDC-CORE-007 and the hold reference is shown

Feature: Bitemporal content
  Scenario: Future-dated amendment
    Given clause "Para 21" valid from 01-Apr-2025
    And an amendment recorded on 25-Oct-2026 valid from 01-Apr-2027
    When I query as of 31-Mar-2027
    Then the original text is returned
    When I query as of 01-Apr-2027
    Then the amended text is returned
    When I query as recorded on 24-Oct-2026 for valid date 01-Apr-2027
    Then the original text is returned

Feature: Evidence WORM
  Scenario: Evidence cannot be deleted inside retention
    Given an evidence object written today with 8-year compliance-mode retention
    When any principal, including the bucket owner, attempts to delete it
    Then S3 denies the deletion

Feature: Export mapping contract
  Scenario: New tenant table without export mapping fails CI
    Given a migration adds table cmp.example with a tenant_id column
    And no file db/export-mappings/cmp.example.yaml exists
    When CI runs the export-contract job
    Then the job fails with "NN-10: missing export mapping for cmp.example"

Feature: Wave-1 migration
  Scenario: Reconciliation blocks promotion on count mismatch
    Given a migration run whose loaded question count differs from the source count
    When the content checker tries to promote it
    Then promotion is refused and the mismatch report is displayed

Feature: Logs contain no PII
  Scenario: Log scrubber removes identifiers
    Given an error log line containing a PAN, a mobile number and an email address
    When it passes through the logging pipeline
    Then the exported line contains none of them
```

NN tests delivered: `NN-01_*`, `NN-02_*`, `NN-07_*`, `NN-09_*`, `NN-10_*`, `NN-11_expand_contract_checker`, `NN-12_no_aadhaar_columns`, `NN-13_sealed_db_isolation`, `NN-24_region_scp`, `NN-30_break_glass_logged`, `NN-32_log_scrubber`.

```gherkin
Feature: Region cells are isolated (v1.1)
  Scenario: No query crosses cells
    Given two cells IN and EU running locally with one tenant each
    When the cross-cell probe test runs every repository query with the IN tenant context
    Then no connection to the EU cell's database or buckets is opened

Feature: Undo a bulk change (v1.1)
  Scenario: Items changed later are not silently undone
    Given a bulk reassignment batch of 50 instances made 3 hours ago
    And 2 of those instances were later approved by a checker
    When the tenant admin undoes the batch
    Then 48 instances revert to their previous owner
    And the 2 approved instances are listed for manual decision
    And the batch status is PARTIAL_UNDO

Feature: Act date drives timeliness (v1.1)
  Scenario: Filing done on time, approved late
    Given a return due on 15 Nov whose acknowledgement shows filing on 14 Nov
    And the checker approves on 20 Nov
    Then the instance status is complied (not complied_late)
    And the internal SLA report shows the approval as late
```

NN tests added *(v1.1)*: `NN-24_cells_isolated`, `NN-48_act_date_timeliness`, `NN-49_batch_undo_compensates`, `NN-51_kill_switch_propagates_60s`.

```gherkin
Feature: Business reference IDs (v1.2)
  Scenario: CompIDs follow the order of the master direction and are never reused
    Given instrument "RBI Governance Directions 2025" with frozen short code "GOV25" for family "NBFC"
    And a 120-row question sheet reaches import preview
    Then CompIDs RBI-NBFC-GOV25-0001 to RBI-NBFC-GOV25-0120 are RESERVED in S. No. order
    When the checker rejects rows 7 and 9 and the release is published
    Then RBI-NBFC-GOV25-0007 and RBI-NBFC-GOV25-0009 are VOID and the other 118 are ASSIGNED
    And a later added question receives RBI-NBFC-GOV25-0121

  Scenario: Allocation rolls back without duplicates
    Given 20 parallel imports allocate IDs on the same instrument and 5 of them roll back
    Then no business ID appears twice in core.business_ids
    And no rolled-back number is issued later

  Scenario: Re-cited provision keeps its CompID; a succeeding obligation keeps history reachable
    Given RBI-NBFC-SBR23-0042 first published under the 2023 scale-based regulation directions
    When the 28 Nov 2025 directions re-cite the same provision
    Then the CompID stays RBI-NBFC-SBR23-0042 with change status "Re-cited" and the new citation
    Given RBI-NBFC-SBR23-0050 is replaced by a different obligation published as RBI-NBFC-GOV25-0042
    When the content checker records CONTINUED_AS and publishes
    Then RBI-NBFC-SBR23-0050 is RETIRED and opening it shows a banner naming RBI-NBFC-GOV25-0042
    And the History tab of RBI-NBFC-GOV25-0042 with "include lineage" shows the predecessor's events

  Scenario: Every event on a CompID is in its history
    Given compliance instance RBI-NBFC-GOV25-0042/2026-Q3 for tenant "RCPL"
    When it is assigned, starred, discussed, evidenced, approved and exported
    Then GET /v1/history/RBI-NBFC-GOV25-0042?include_instances=true returns all six events in order
    And each ledger row has business_ids containing "RBI-NBFC-GOV25-0042" and "RBI-NBFC-GOV25-0042/2026-Q3"

  Scenario: Tenant code locks after first use
    Given tenant "Ram Capital Private Limited" was proposed code "RCPL" during onboarding
    When the first RiskID RSK-RCPL-00001 is issued
    And an administrator tries to change the code to "RAMC"
    Then the request fails with LDC-CORE-125

  Scenario: A hidden ID looks the same as a missing one
    Given a user without access to GOV-RCPL-MIN-00004
    When the user opens /g/GOV-RCPL-MIN-00004
    Then the response is LDC-CORE-031 with the same message as for an ID that does not exist
```

NN tests added *(v1.2)*: `NN-56_bizid_immutable_never_reused`, `NN-56_alias_never_issued`, `NN-56_lineage_acyclic`, `NN-56_tenant_code_locked`, `NN-57_every_event_has_bizid`, `NN-57_history_tab_complete`.

---

## 13. Deliverables and exit gate

- [ ] `docs/discovery/01–10` complete; disposition register signed by the owner.
- [ ] Legacy Critical/High security findings fixed or mitigated in the legacy app; leaked secrets rotated.
- [ ] Public-claims corrections approved (FR-P00-04) and handed to P23.
- [ ] ADR-0001 to ADR-0020 merged.
- [ ] Monorepo, module skeletons, ownership and boundary checks green.
- [ ] Local stack and dev/staging/uat environments running; production AWS account baseline and SCPs applied (prod workloads arrive in P24).
- [ ] `core` schema, RLS framework, sealed database, encryption library, bitemporal library, IDs, money, citations, outbox/inbox, flags, `cfg` heads, buckets and evidence ingest skeleton delivered with tests.
- [ ] Audit ledger, anchors, verification, Correction Entries (platform and tenant), access log and break-glass schema delivered; SCR-CORE-01 to 09 usable.
- [ ] Wave-1 content migration promoted with reconciliation report and sample review signed by the Company Secretary.
- [ ] Waves 2 and 3 rehearsed on a restore with reconciliation reports; cut-over runbook approved.
- [ ] Export-mapping registry and NN-10 contract test live.
- [ ] Contribution to Appendix B (core DDL), Appendix Q (core threat model) and `docs/phases/P00-plan.md` five inventories (settings, events, error codes, approval actions, export mappings).
- [ ] All P00 Gherkin scenarios and listed NN tests pass in CI.

- [ ] *(v1.1)* Cell abstraction in `packages/tenancy` with the `IN` cell live and `EU`/`GCC`/`SG`/`US` Terraform modules plan-clean; global directory; change batches and undo; three-date value object; skeletons for `gem`, `prt`, `lit`, `esg`; AI foundations (adapter interface, routing table, kill-switch registry, model registry, eval runner stub); configuration templates and sandbox tenant; FinOps tags.

- [ ] *(v1.2)* Business-ID registry (`packages/bizid`, allocator, segment registries, lifecycle, aliases, lineage, links), ledger `business_ids` with history index, History API and `<HistoryTimeline>`, resolver and deep links; SCR-CORE-10 and 11; NN-56 and NN-57 tests green; legacy ID mapping signed off by the owner.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P00-01 | Region of the legacy Railway service and MongoDB Atlas cluster | Not visible without account access | Owner / CTO | Treat as outside India until confirmed; disclose to beta tenant; cut-over date fixed |
| OI-P00-02 | Supabase PostgreSQL major version and PITR plan for beta | Plan-dependent | CTO | Use features available on PostgreSQL 16; daily logical backups to ap-south-2 |
| OI-P00-03 | Temporal Cloud India residency | Vendor-dependent | CTO | Self-host Temporal in ap-south-1 |
| OI-P00-04 | Observability vendor with India residency | Vendor-dependent | CTO | Self-hosted Grafana LGTM in ap-south-1 |
| OI-P00-05 | RFC 3161 TSA provider (Indian licensed CA timestamping) | Contract | CTO / CS | `core.audit.anchor.tsa.enabled` = OFF; KMS-signed anchors only |
| OI-P00-06 | Legacy password-hash algorithm importability into Keycloak | Discovery | Tech lead | Force reset on first login |
| OI-P00-07 | Numbering and exact citations of the legacy and Sep 2026 RBI question banks (RBI/DoS/2026-27/460–468) | Need source PDFs | Company Secretary | Import as `NEEDS_REVIEW` |
| OI-P00-08 | Whether regulators' confidentiality rules (e.g., RBI inspection reports, MAPs) restrict storing supervisory correspondence with a vendor | Legal reading per regulator | Counsel | Class `REGULATOR_CONFIDENTIAL`, sealed-like handling, tenant opt-in |
| OI-P00-09 | Node.js 26 LTS promotion and framework support | Release timing | Tech lead | Stay on Node.js 24 LTS |
| OI-P00-10 | GST invoice rounding and numbering rules confirmation for `core.sequences` | Tax reading | CA | Gap-free per-FY series per GSTIN (Rule 46) |
| OI-P00-11 *(v1.1)* | Foreign cell regions and DR pairs (UAE, Singapore, US) and hosting contracts | Opened only on demand (D-42) | CTO / owner | Modules defined, not deployed |
| OI-P00-12 *(v1.1)* | Whether the global control plane may sit in IN for EU/GCC tenants' routing metadata (tenant slug, cell) | Data-transfer reading (GDPR Art. 44 for staff/contact data) | Counsel | Directory holds no personal data of customers; contact data stays in the cell |

**v1.2 open items** *(v1.2)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P00-13 | Whether legacy CompIDs already printed in clients' records (legacy app, owner's NBFC and IFSCA sheets) must be preserved as canonical IDs or may become aliases | Owner decision; affects continuity of clients' audit papers | Owner / Company Secretary | Keep pattern-conforming legacy IDs canonical; others as aliases |
| OI-P00-14 | Instrument short-code list for the 238 RBI Directions of 28 November 2025 | Content work (P03 FR-P03-102); codes freeze at the first reservation | Company Secretary / content checker | System proposals held in PROPOSED; no CompIDs reserved until approved |
| OI-P00-15 | Format of the s.63 Bharatiya Sakshya Adhiniyam 2023 certificate for history exports (Schedule form, signatories) | Legal reading | Counsel | Use the NN-09 certificate template already approved for exports |

---

## 15. Sources (checked 25 October 2026 unless stated)

1. Infrabyx Ecosystem Integration Specification v1.1 — §3.1–3.9 (topology, CloudEvents envelope, outbox/inbox, tokens, error model), §4.1, §4.6–4.7, §9.1–9.3, §13.2 (owner's corpus).
2. Infrabyx Operations Hub Master Prompt v1.0 — OH13 engineering-operations console, OH14 certification readiness (owner's corpus).
3. Equator v3.1 P00, Equator v3.1 App F, Equator v3.1 App AE (external pattern reference; not appendices of this pack) *(v1.1)*.
4. Owner's LawDocs Comply Architecture Part 1 — Architectural Principles, Layered Architecture, Core Microservices, Data Architecture, Security Architecture, Visual Identity, Design Tokens, Onboarding.
5. PostgreSQL Global Development Group, "PostgreSQL 18 Released!" (25 Sep 2025) — https://www.postgresql.org/about/news/postgresql-18-released-3142/
6. Supabase, "Available regions" — https://supabase.com/docs/guides/platform/regions
7. Keycloak release history (26.8.1, 13 Oct 2026) — https://versionlog.com/keycloak/ [VERIFY against keycloak.org]
8. InfoQ, "Node.js release model changes" (June 2026) — https://infoq.com/news/2026/06/nodejs-release-changes
9. CERT-In Directions under s.70B(6) of the IT Act, 2000 (28 Apr 2022) — https://www.cert-in.org.in/ [log retention 180 days in India; NTP; 6-hour reporting]
10. Companies Act 2013 s.128(5) (books of account 8 years); CGST Rules 2017 Rule 46 (invoice serial numbers).
11. RFC 9457 (Problem Details), RFC 9562 (UUIDv7), RFC 8785 (JSON Canonicalization Scheme), RFC 3161 (Time-Stamp Protocol), CloudEvents 1.0.2.

12. *(v1.2)* Internal: LEAD v1.2 specification §3 (ID formats) and Appendix B §B.12; PostgreSQL documentation, "GIN Indexes" (array containment) — https://www.postgresql.org/docs/current/gin.html; Bharatiya Sakshya Adhiniyam 2023, s.63 (admissibility of electronic records) — https://www.indiacode.nic.in/

---

## 16. Master integration notes (pack lead, v1.1 and v1.2, 25 October 2026)

**From v1.0 integration:** NN-34, NN-45; X-01, X-05, X-06 (licence ADR for an optional WOPI editor), X-21, X-22 (remove live-site claims), X-25 (kernel ADRs), X-26; raise the Ecosystem Spec v1.2 change requests of master §19 in sprint 1.

**Added in v1.1:** NN-24 (amended), NN-48, NN-49, NN-51; X-45, X-50; D-42, D-48.

**Added in v1.2:** D-51; NN-56, NN-57; X-63 (this phase hosts the `core` business-ID registry and the ledger keyed by business ID, FR-P00-70–78; the `IdService` may sit behind an internal API in P03 without contract change).

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
