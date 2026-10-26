# Phase P00 — Foundations, Repository Discovery and Migration

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** none (first phase). Read-only access to the legacy lawdocs.in repository, a point-in-time restore of the MongoDB Atlas database, the Railway project (viewer), the DNS zone, the PayU merchant dashboard (read-only), the Anthropic console (usage and key list), Google Search Console and the live site. Companion documents committed unchanged under `docs/ecosystem/` with SHA-256 checks: Infrabyx Ecosystem Integration Specification v1.1, Operations Hub Master Prompt v1.0, LawDocsComply Pack v1.2 (reference only), Equator v3.1 (reference only).
> **Sequencing:** Sprint 1 discovery and repository scaffold run in parallel; sprints 2–4 build the platform core; sprint 4 starts P01 (identity) and P21 core (SSR site shell) in parallel; sprints 5–6 run migration rehearsals and the SEO cut-over. **Freeze points:** (1) the disposition register is signed off by the owner before any legacy asset is retired; (2) the `core` schema, ID prefixes, audit-event structure and export-map contract freeze at the end of sprint 4 (later phases extend, never change); (3) the 301 map freezes 10 days before DNS cut-over (T−10 d, §5.5; `web.redirects.freeze_days_before_cutover`). The legacy site stays live and read-write until cut-over (§5.5). **Customer cut-over dependency:** T0 (§5.5) needs P01's OTP sign-in, P04's vault list view and P17's order/billing mirror view running in pre-prod; if they are not ready by sprint 6, P00 exits with R1–R3 passed and every other gate item met, and the final customer migration run, DNS cut-over, decommissioning (FR-P00-83) and @P00-AT-15/16 move to a dated P00 tail that must close before the Wave 1 P23 go-live gate.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and access — coarse platform roles only in P00), K (export package `LD-EXPORT-1.0`; export-map registry created here), P (security, privacy and certification readiness), R (settings registry; heads created here), W (verification log and open items), Y (Ecosystem Spec v1.2 change request: owner code `LD`).
> **Requirements covered:** R-001, R-002, R-003, R-021 (storage foundations), R-022, R-031 (foundations), R-032 (rendering and host hygiene), R-033 (foundations), R-057 (CI/CD skeleton; detail in P23), R-067, R-068 (foundations), R-070, R-071.
> **Decisions applied:** D-01, D-02, D-08, D-09, D-10, D-14 (AI gateway stub only), D-16 · **Challenges applied:** CH-15, CH-16, CH-19 (claims hygiene of the legacy site), CH-20 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-11, NN-12, NN-15, NN-19, NN-20, NN-24, NN-25, NN-27, NN-29, NN-31, NN-32, NN-38, NN-39, NN-45, NN-46, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 1 frontend engineer, 1 platform/DevOps engineer, 1 data-migration engineer, 1 QA/security engineer, 1 web/SEO engineer) plus the owner as product owner and a part-time content reviewer for blog migration.

---

## 1. Objective and business outcome

lawdocs.in runs today as a client-side React single-page application built with Vite, an Express backend that includes a chatbot route calling the Anthropic API, MongoDB Atlas as the database, Railway as the host and an earlier PayU payment integration [VERIFY all five facts at discovery; they come from the owner, not from code inspection]. Research shows the public site is invisible to non-JavaScript crawlers (every URL returns the same title and an empty body), its sitemap lists 186 non-www URLs while only the www host serves deep pages, and `robots.txt` blocks `/buy/` while the sitemap lists 20 `/buy/*` URLs (R5 §1.1–§1.2). The stack cannot carry what the owner now wants: tenant isolation, an append-only audit ledger, India residency, immutable signed originals, portability in `LD-EXPORT-1.0`, ecosystem contracts and certification readiness.

P00 does four things:

1. **Discover and keep what works.** Inventory every route, collection, user, order, blog post, integration, secret, DNS record and SEO asset; give each a disposition; carry forward everything useful (content, users, order history, search equity).
2. **Build the platform core** on the locked stack (D-01): pnpm/Turborepo monorepo, NestJS 11 modular monolith, Next.js 16 apps, PostgreSQL with enforced RLS, the hash-chained audit ledger with Correction Entries, prefixed-ULID IDs and business reference IDs, transactional outbox, settings and flag heads, the evidence store with Object Lock, observability, the CI/CD skeleton, the NN test harness and synthetic data.
3. **Migrate** users, content and orders from MongoDB to PostgreSQL through rehearsed, reconciled, idempotent runs, so no customer re-keys anything and no order or invoice record is lost.
4. **Cut over without losing search traffic**: SSR shell from P21 core, one canonical host (`https://www.lawdocs.in`), a complete 301 map for all 186 sitemap URLs and the legacy indexed URLs, a corrected `robots.txt` and sitemap, then decommission Railway, MongoDB Atlas and PayU in a controlled order.

| Outcome | Exit-gate measure |
|---|---|
| Nothing useful is lost | `docs/discovery/10-disposition-register.md` signed by the owner; every asset has a disposition (MIGRATE, REBUILD, RETIRE, ARCHIVE); zero rows "unknown" |
| Platform core runs | `docker compose up && pnpm dev` starts all apps on a fresh machine in ≤ 10 minutes; `dev`, `test`, `staging` and `pre-prod` deploy from `main` through CI with signed images (environment names per P23 FR-P23-07) |
| Isolation is provable | `NN-01_cross_tenant_denied` passes for 100% of tenant tables across two seeded tenants for SELECT, UPDATE and DELETE; RLS lint passes |
| History is tamper-evident | `NN-02_*` suite passes: every mutating handler writes a chained ledger event in the same transaction (`NN-45_*`); `UPDATE`/`DELETE` on the ledger fails for every role including the owner role |
| Migration is exact | Final rehearsal reconciles 100% on counts and order-amount sums by month and status; field-level defect rate ≤ 0.5% on a 5% stratified sample (minimum 200 rows per entity); all defects resolved or carried as flagged rows with owner sign-off |
| Search equity preserved | 100% of the 186 sitemap URLs and every legacy URL with impressions in the last 16 months return a single-hop 301 (or a deliberate 410) to an SSR page returning 200 with a unique title, H1 and body to a no-JavaScript fetch; zero redirect chains; Search Console shows no rise in 404s above baseline + 5% in the 28 days after cut-over |
| India residency | IaC denies regions other than ap-south-1/ap-south-2 except listed global services; no tenant data outside India after cut-over (`NN-25_*`); Railway, MongoDB Atlas and the legacy chatbot key are decommissioned on the dated plan |
| Portability contract exists | `xpt.export_map` registry and its CI contract test exist; a migration that adds a tenant table without an export-map entry fails CI (`NN-11_*`) |

**What "done" looks like for users.** A returning customer signs in to the new my.lawdocs.in with their mobile or email (P01), finds their past orders and invoices under Billing, and finds the documents they bought in their Legal Vault. A visitor arriving from an old Google result for `lawdocs.in/smartdrafts/...` lands on the right new document page in one hop. Nobody sees a "page not found".

---

## 2. Scope (in / out)

**In scope**

- Discovery of the legacy repository, database, hosting, DNS, payments, AI usage, analytics and third-party accounts; security triage of the live system; disposition register.
- Monorepo scaffold (all six apps of master §1.3 plus `apps/worker`), toolchain, module skeletons for every bounded context in master §5.3, boundary enforcement and code ownership.
- Environments (`local`, `dev`, `test`, `staging`, `pre-prod`, `prod`, `dr`, plus the `mig` migration zone inside the prod account; names per P23 FR-P23-07, which governs), hosting topology, domains and infrastructure as code.
- CI/CD skeleton with branch model, signed artefacts, SBOM and the NN suite as a required check (P23 hardens and completes it).
- `packages/tenancy`, `packages/audit`, `packages/ids` (prefixed ULID + business reference IDs), `packages/money`, `packages/crypto`, `packages/db`, `packages/config` (registry heads), `packages/contracts` (generated from `infrabyx-contracts`), `packages/observability`, `packages/testing`.
- `core` schema: tenants, legal entities, brands and operating-entity profiles (D-06, D-08), tenant domains, data-class catalogue, sequences, idempotency keys, outbox and inbox, audit ledger, anchors, correction entries, access log, break-glass events, migration lineage.
- Object storage (quarantine, documents, originals with Object Lock, exports, backups) and the ingest pipeline skeleton (P04 builds the Legal Vault on it).
- Observability, error model, SLO budgets; design-token, i18n and accessibility foundations.
- NN test harness (`tests/nn/`), synthetic seed profiles.
- Data migration framework and the full MongoDB → PostgreSQL migration (users, orders, payments, blog content, leads, chatbot logs disposition, any uploaded files).
- SEO-safe cut-over with the 301 map, host canonicalisation, robots and sitemap correction (with P21 core supplying the SSR pages).
- Decommissioning of Railway, MongoDB Atlas, the legacy Anthropic key and the PayU integration.
- ADR set and the `docs/` structure.

**Out of scope (owned later)**

| Item | Owner phase |
|---|---|
| Login, onboarding, KYC/KYB, consent capture UI | P01 (P00 creates the `iam`/`kyc` schemas' parent tables only where `core` needs them, and a stub IdP for local development) |
| Organisation structure, user types, maker-checker engine | P02 |
| Settings Studio UI, rule engine | P03 (P00 creates the heads of `cfg.setting_definitions`, `cfg.setting_values`, `cfg.flags` and `cfg.kill_switches`; P03 owns them) |
| Legal Vault and DMS features | P04 (P00 creates buckets and ingest skeleton) |
| Public website pages, CMS, content rewrite | P21 (P00 owns the redirect map, host rules, robots/sitemap generator contract and the cut-over runbook; P21 core supplies the SSR shell and the top pages that receive redirects) |
| Billing engine, invoices, refunds | Operations Hub OH8 via `BILLING_PORT`; LawDocs mirror in P17 |
| Full CI/CD hardening, CAB, VAPT, go-live | P23 |
| Mobile apps | P22 (P00 scaffolds `apps/mobile` with Expo and the design tokens only) |
| Ecosystem connectors | P19 (P00 imports the contracts package and stubs the `ECOSYSTEM_PORT`) |

---

## 3. Personas and permissions touched

| Role code | What P00 gives them |
|---|---|
| `PLT_SUPER_ADMIN` | Seeded platform tenant `ld-platform`; first super-admin account (stub IdP in local/dev, Keycloak `ld-staff` from P01). May request Correction Entries and run migration steps; cannot approve their own request |
| `PLT_SECURITY_OFFICER` | Approves Correction Entries of class `SECURITY`, break-glass sessions and flag changes for kill-switch flags; owns KMS key policies; receives audit-chain alerts |
| `PLT_SRE` | Runs infrastructure, migrations and cut-over steps; no tenant data access outside migration staging |
| `PLT_RELEASE_MANAGER` | Promotes image digests between environments (P23 adds CAB linkage) |
| `PLT_CONTENT_EDITOR` | Reviews migrated blog posts and pages in the migration console (sample review) |
| `PLT_DPO` | Approves the disposition of personal-data collections (legacy leads, chatbot logs, enquiries) and the processing register entries |
| `PLT_AUDITOR_RO` | Read-only access to the platform chain, anchors, migration reconciliation reports |
| `OPS_CONTENT_PUBLISHER` | Verifies redirected pages render correctly before freeze (read-only console view in P00) |
| Migrated customers (`IND_OWNER`, `ORG_OWNER`) | Exist as migrated person and tenant records; activate at first login in P01 |

All checks in P00 are coarse platform-role checks behind `packages/authz`; P01/P02 replace them with Cerbos policies (Appendix D) without changing the APIs.

---

## 4. Functional requirements

### 4A. Discovery of the legacy system

**FR-P00-01 — Read-only discovery access.** The owner grants: the legacy GitHub repository (read), a MongoDB Atlas read-only user on a **point-in-time restore cluster** (never the live cluster), Railway viewer access, the DNS zone export, PayU merchant dashboard read-only (or settlement and transaction exports), the Anthropic console usage page and key names, Google Search Console (full user), Google Analytics or other analytics (read). No production secret is copied into the new repository; secrets are listed by name, location, owner and last rotation only.

**FR-P00-02 — Inventory scripts and outputs.** Commit `tools/discovery/` (repeatable, idempotent scripts) producing `docs/discovery/`:

| File | Contents |
|---|---|
| `01-repository.md` | Languages and versions (Vite, React, Express, Node, Mongoose or driver), dependency tree with vulnerabilities (osv-scanner), licences, build and deploy scripts, environment-variable names, test coverage, monorepo or split repos |
| `02-routes-and-features.md` | Every SPA route and every Express route: method, path, auth requirement, handler, collections touched, status (WORKING / PARTIAL / STUB / DEAD), user-visible feature, defects found; mapped to the new phase that rebuilds it |
| `03-data-model.md` | Every MongoDB collection: document count, observed fields and types, null rates, indexes, references, PII fields, size, oldest and newest record, GridFS buckets or external file stores (Cloudinary, S3, local disk) |
| `04-users-and-accounts.md` | User counts by type and status, auth method (password hash algorithm, OTP, Google), last-login distribution, admin accounts, duplicate emails/mobiles — counts and pseudonymised IDs only |
| `05-orders-and-payments.md` | Orders by month, status and product; PayU transaction mapping (txnid, mihpayid or equivalent), refunds, chargebacks, open orders, invoice generation method and GST details on invoices, reconciliation against PayU settlement reports |
| `06-integrations.md` | Every outbound call: Anthropic (model, endpoint, where the key lives, whether the key is reachable from the browser bundle, prompt content classes, rate limits, monthly spend), PayU, email/SMS providers, analytics tags, chat widgets, maps, Graphy links (trainings.lawdocs.in) |
| `07-infrastructure.md` | Railway services, regions, plans, cron jobs, volumes, backups; MongoDB Atlas cluster tier, **region**, backup policy; DNS records (A, AAAA, CNAME, MX, TXT incl. SPF, DKIM, DMARC, Google verification), TLS, CDN, email routing; non-www behaviour |
| `08-seo-assets.md` | All 186 sitemap URLs with HTTP status on www and non-www, rendered title/H1 (headless browser) and no-JS title/H1, canonical tag, Search Console clicks and impressions (16 months), top backlinks per URL, legacy indexed URLs not in the sitemap (`/mortgage/`, `/services/consult-lawyer`, `/legal` and any found in Search Console), `robots.txt`, structured data |
| `09-security-findings.md` | Secrets in git history (gitleaks full history), Anthropic key exposure, unauthenticated admin routes (`/addblogs`, `/edit-blog/` are disallowed in robots — test whether they are authenticated), missing authorisation on order or user APIs (IDOR), NoSQL injection, CORS, payment-callback verification (hash check of PayU responses), dependency CVEs, public buckets |
| `10-disposition-register.md` | One row per asset: ID, description, disposition, target phase, owner, risk, personal-data class, retention basis, notes |
| `11-claims-inventory.md` | Every public claim on the live site and manuals (certifications, "verified lawyers", "government-approved", success rates, client logos, testimonials) with REMOVE / REWORD / KEEP WITH EVIDENCE (NN-20) |

**FR-P00-03 — Same-day security triage.** Any Critical or High finding that exposes current users (leaked or browser-reachable Anthropic key, unauthenticated blog admin, order IDOR, unverified payment callbacks) is reported to the owner the same day with a fix for the legacy app. Leaked keys are rotated within 24 hours; an Anthropic key reachable from the browser is revoked immediately and the chatbot route is rate-limited or disabled until cut-over. The legacy app keeps running until cut-over, so its security matters throughout P00.

**FR-P00-04 — Legacy chatbot assessment.** Record for the chatbot route: model used, system prompt, whether user messages are stored and where, whether prompts carry personal data, the region of processing (Anthropic first-party API is a cross-border transfer — record it in the transfer register, R3 LG-069), whether any disclaimer is shown, and spend. Decision rule: the legacy chatbot is **retired at cut-over** and replaced by Vidhi (P09) on the AI gateway; its logs are not imported into any AI memory or training set (NN-15) — disposition per FR-P00-71.

**FR-P00-05 — Legacy payments assessment.** Record PayU merchant ID (name only), integration type (hosted redirect or seamless), whether any card data reached LawDocs servers (if a seamless form posted card fields to Express, this is a PCI DSS scope incident to record and close), callback hash verification, refund history, and open disputes. Decision rule: PayU is not used in the new estate (D-01: Razorpay via OH8); historical PayU transactions migrate as historical payment records (FR-P00-69); the PayU account is closed only after the refund and chargeback window has passed and settlements reconcile (FR-P00-83 step 7).

**FR-P00-06 — Claims hygiene.** Any claim in `11-claims-inventory.md` marked REMOVE is removed from the legacy site within 5 working days of owner approval (NN-20); the new site inherits only KEEP WITH EVIDENCE claims, each recorded in the claims register (Operations Hub OH14 claims gate, Ecosystem Spec §6.29).

**FR-P00-07 — Discovery sign-off.** The disposition register is reviewed by the owner and `PLT_DPO` (personal-data rows) and signed (the signature is a ledger event in the platform chain with the register's SHA-256). Assets with disposition MIGRATE or ARCHIVE cannot be deleted at source until their migration run is PROMOTED or the archive is verified (§5.4).

### 4B. Repository, toolchain and module boundaries

**FR-P00-08 — Repositories.** Create `lawdocs` (private) in the Infrabyx GitHub organisation, and `lawdocs-infra` if the group standard separates infrastructure (the OH13 repository register decides). Rename the legacy repository `lawdocs-legacy`, archive it read-only after decommissioning and retain it for 8 years (it evidences how historical orders and content were produced).

**FR-P00-09 — Monorepo layout.**

```
lawdocs/
├─ apps/
│  ├─ public/     # www.lawdocs.in — Next.js 16 SSR/SSG, multi-brand (LawDocs, [Consumer Help Brand]), marketplace storefront, blog/vlog, help centre
│  ├─ web/        # my.lawdocs.in — Personal and Company workspaces with context switcher
│  ├─ delivery/   # work.lawdocs.in — Delivery Console (RMs, in-house professionals, consumer case managers, practitioner workspace)
│  ├─ console/    # admin.lawdocs.in — Super Admin / platform (separate origin, separate Keycloak client)
│  ├─ mobile/     # Expo React Native (iOS + Android), brand flavours
│  ├─ api/        # NestJS 11 modular monolith: REST /v1, BFF /m/v1, webhooks, SCIM, partner APIs
│  └─ worker/     # NestJS application context: Temporal workers, outbox relay, schedulers
├─ packages/
│  ├─ tenancy/  audit/  ids/  money/  crypto/  db/  authz/  config/  rules/  workflow/
│  ├─ notify/  docgen/  redline/  dix/  ai/  agents/  connectors/  export/
│  ├─ ui/  tokens/  i18n/  a11y/  observability/  testing/
│  └─ contracts/  # generated from infrabyx-contracts (OpenAPI 3.1, AsyncAPI 3.0, JSON Schema 2020-12) + LawDocs internal contracts
├─ db/
│  ├─ ownership.yaml          # table → owning module
│  ├─ rls-exemptions.yaml     # global reference tables with justification
│  ├─ data-catalogue.yaml     # every column → data class
│  └─ export-map/             # LD-EXPORT-1.0 mapping per record type (NN-11)
├─ policies/cerbos/           # authorisation policies (P01/P02)
├─ infra/                     # OpenTofu/Terraform (or lawdocs-infra)
├─ tools/  discovery/  migration/  seo/  verify/
├─ tests/  nn/  acceptance/pxx/  e2e/  load/
└─ docs/   (structure in FR-P00-90)
```

**FR-P00-10 — Toolchain.** Node.js **24.22.1** pinned in `.nvmrc`, `engines`, Dockerfiles and CI (IPB-D-01; IPB-01 §01.4.1) *(v1.1: supersedes "24 LTS [VERIFY]")*; previously: Node.js 24 LTS pinned in `.nvmrc` and `engines` [VERIFY at P00: current LTS line and NestJS 11 / Next.js 16 / Temporal SDK support; record in ADR-0001]; pnpm workspaces; Turborepo pipelines `lint`, `typecheck`, `test`, `build`, `e2e`, `db:migrate`, `db:test`, `seed`, `nn`, `seo:check`. TypeScript `strict`, `noUncheckedIndexedAccess`, `exactOptionalPropertyTypes`. ESLint flat config with `@typescript-eslint/strict-type-checked` and `eslint-plugin-boundaries`; Prettier; commitlint (Conventional Commits); Changesets for package versions; lint-staged and Husky. Exact versions of Next.js, React, NestJS, Drizzle (or Kysely — ADR-0004), Temporal SDK, Keycloak, Cerbos, Expo and PostgreSQL are pinned with dated release notes in ADR-0001.

**FR-P00-11 — Module skeletons.** Generate a NestJS module for every code in master §5.3 (`core`, `iam`, `kyc`, `org`, `cfg`, `rul`, `wf`, `ntf`, `msg`, `dms`, `dix`, `tpl`, `drf`, `clm`, `sgn`, `ai`, `agt`, `pld`, `lit`, `ipm`, `gov`, `hr`, `lgo`, `bsv`, `tax`, `chp`, `mkp`, `aca`, `bil`, `sav`, `sdc`, `cvl`, `int`, `xpt`, `web`, `hlp`, `rpt`, `mob`, `eng`). Each has `public-api.ts`, `module.ts`, `domain/`, `infra/`, `http/`, `events/` and `README.md` (purpose, owned tables, published/consumed events, settings keys, export-map record types, help keys). CI rules:

- A module imports another only through its `public-api.ts`.
- A module reads or writes only tables it owns (`db/ownership.yaml`); a CI script parses query builders and fails on a cross-schema write or an undeclared cross-schema read.
- PostgreSQL schema name = module code.
- Only `int` may import `packages/contracts` ecosystem subjects or call `ECOSYSTEM_PORT` (NN-24); a lint rule enforces this.
- `gov` and `hr` mount `@infrabyx/governance-kernel` and `@infrabyx/hrms-kernel` as pinned dependencies; any file under `packages/**` that re-implements a kernel export fails the `NN-47_no_kernel_fork` check (hash comparison of exported symbols against the pinned kernel version).

**FR-P00-12 — Code ownership.** `CODEOWNERS`: `packages/db/migrations/**` and `db/**` → database owner + security engineer; `packages/audit/**`, `packages/crypto/**`, `packages/authz/**`, `policies/**` → security engineer + tech lead; `db/export-map/**` → data owner; `infra/**` → platform owner; `docs/ecosystem/**` and `packages/contracts/**` → Integration Spec owner (changes only via `infrabyx-contracts`); `tools/seo/**` and `apps/public/redirects/**` → web/SEO owner. P23 converts this into GitHub rulesets.

**FR-P00-13 — Mobile scaffold.** `apps/mobile` is created with Expo (managed workflow, EAS build profiles `dev`, `preview`, `production`), the design tokens, i18n and the API client generated from OpenAPI; no features (P22).

### 4C. Environments, hosting, domains and infrastructure

**FR-P00-14 — Environment catalogue.** Environment names are standardised on `dev`, `test`, `staging`, `pre-prod`, `prod` (+ `dr` region); P23 FR-P23-07 governs and adds protection rules. P00 provisions them; `mig` is a zone inside the prod account, not a separate environment.

| Env | Purpose | Data | Hosting | Deploy trigger | Approval |
|---|---|---|---|---|---|
| local | Developer machine | Seed `dev` | Docker Compose | — | — |
| dev | Integration of `main` | Seed `demo`, reset weekly | AWS ap-south-1 compute; Supabase Postgres ap-south-1 permitted (DB only) | Merge to `main` | None |
| test | Automated suites: E2E, contract, accessibility, migration rehearsal on synthetic data | Synthetic fixtures (regex scan blocks real-looking identifiers) | AWS ap-south-1 | Auto after dev smoke | None |
| staging | Release candidate, performance smoke, migration rehearsals on **synthetic** data, vendor sandboxes | Seed `demo` + `load` + `legacy-mirror` | AWS ap-south-1 (RDS engine as prod) | Tag `rc-*` | Tech leads |
| pre-prod | Final rehearsal of the exact digests and migrations; owner acceptance (UAT) and demos | Curated synthetic | As staging | Promotion of the staging digest | Product owner |
| prod | Live | Real | AWS ap-south-1: RDS PostgreSQL Multi-AZ or Aurora PostgreSQL (ADR-0007), ECS Fargate, S3 with Object Lock | Promotion of the pre-prod digest | 2 approvers + change record (P23) |
| dr | Warm standby | Cross-region replica + backups | AWS ap-south-2 (Hyderabad) | IaC only | — |
| mig (zone, not an environment) | Migration staging (real legacy data, prod-grade controls) | Restored legacy snapshot + staging schemas | Inside the prod account, isolated schema `mig_stage`, prod access controls | Manual run | `PLT_SUPER_ADMIN` + `PLT_DPO` |

Production data never leaves prod or mig. Non-production adapters for SMS, WhatsApp, email, eSign, eStamp, KYC/KYB, DigiLocker, payments and AI are forced to sandbox or fakes by a `provider_routing` guard that fails closed: a live-provider call from non-prod raises `LD-CORE-014` and an alert. Real legacy data is rehearsed only in `mig`, never in staging (R3 LG-069; NN-25).

**FR-P00-15 — Hosting decision (ADR-0007).** Production on AWS from first paid customer: RDS PostgreSQL Multi-AZ (or Aurora PostgreSQL if the cost case holds) in ap-south-1 with a cross-region replica in ap-south-2; S3 with Object Lock (compliance mode) for originals and signed files; ECS Fargate. Supabase may host non-prod Postgres only; no Supabase Auth, Storage, Realtime or Edge Functions are used anywhere, so the application stays portable (no vendor API dependency) [REC]. Railway is not used in the new estate; it may run nothing, not even synthetic previews, unless ADR-0007 records otherwise (Operations Hub permits Railway for synthetic-only dev; LawDocs chooses not to, to keep one toolchain) [REC; OWNER].

**FR-P00-16 — AWS account topology.** AWS Organizations OU `lawdocs` with accounts `ld-security` (GuardDuty, Security Hub, Inspector, IAM Access Analyzer delegated admin), `ld-log-archive` (organisation CloudTrail, Config, VPC flow logs; S3 Object Lock), `ld-shared` (ECR, CI OIDC roles, Route 53), `ld-dev`, `ld-test`, `ld-staging`, `ld-preprod`, `ld-prod`, `ld-backup` (AWS Backup vault lock; separate credentials). If the group runs one AWS Organization for all products, these are OUs under it; the Operations Hub never receives credentials into `ld-prod` (Ecosystem Spec §4.6). Service control policies deny regions other than ap-south-1 and ap-south-2 (allow-list global services: IAM, Organizations, Route 53, CloudFront, global WAF, ACM for CloudFront, Support), deny disabling CloudTrail/GuardDuty/Config, deny changing Object Lock configuration on the originals bucket except through the break-glass role, and deny root-user actions (`NN-25_region_scp`).

**FR-P00-17 — Network and compute.** VPC across three AZs; private subnets for compute and data; egress only through an allow-list proxy (`infra/egress-allowlist.yaml`: one entry per vendor domain with owner, data class and the port that uses it); VPC endpoints for S3, KMS, Secrets Manager, ECR, CloudWatch Logs and STS. ECS services: `public`, `web`, `delivery`, `console`, `api`, `worker`, `outbox-relay`, `temporal-*` (self-hosted in ap-south-1 by default; Temporal Cloud only with recorded India residency [VERIFY]), `keycloak`, `cerbos`, `flags`, `clamav`, `gotenberg`, `otel-collector`. ALB with AWS WAF (managed core rules, SQLi, known bad inputs, bot control on public routes, rate rules on `/v1/auth/*`, `/v1/public/*` and the anonymous draft endpoints). CloudFront in front of `public` with India origin. `console` and `delivery` are not exposed through the public CDN; they accept only SSO-authenticated staff from the `ld-staff` realm with device posture checks (P23).

**FR-P00-18 — Database topology.** One PostgreSQL cluster `ld_core` holding all module schemas, plus database `ld_sealed` (separate cluster in prod) for sealed classes: credential-vault ciphertext (`cvl`, NN-16), KYC verification artefacts that must be segregated (signed Aadhaar offline-verification attributes, DigiLocker URIs and verification results, guardianship and death/incapacity evidence for nominee release), and consumer-help case identity where the brand marks it sealed. Core references sealed rows only through an opaque `sealed_ref` token; no foreign key, join, search index, analytics export or AI dataset reads it. Extensions: `pgcrypto`, `btree_gist`, `ltree` (org-unit paths), `pg_partman` (ledger, outbox, notifications), `pg_trgm` + FTS dictionaries, `pgvector` (tenant-scoped embeddings; P09 rules). PostgreSQL major: highest version supported by both RDS and the non-prod host at build time, 16 minimum, 18 preferred [VERIFY]; no 18-only syntax unless ADR-0002 records support on every host.

**FR-P00-19 — Domains and DNS (ADR-0016).**

| Host | Serves |
|---|---|
| `www.lawdocs.in` | Canonical public site (`apps/public`) |
| `lawdocs.in` | 301 to `https://www.lawdocs.in` + same path and query (FR-P00-76) |
| `my.lawdocs.in` | `apps/web` |
| `work.lawdocs.in` | `apps/delivery` |
| `admin.lawdocs.in` | `apps/console` (not on public CDN; staff realm only) |
| `api.lawdocs.in` | `apps/api` (`/v1`, `/m/v1`, `/scim/v2`, `/webhooks/*`) |
| `auth.lawdocs.in` | Keycloak login theme (P01) |
| `sign.lawdocs.in` | Hosted signing ceremony pages (P08; P19 FR-P19-38; `frame-ancestors 'none'`) |
| `events.lawdocs.in`, `hooks.lawdocs.in`, `api.sandbox.lawdocs.in` | Ecosystem push receiver (mTLS), vendor callbacks and developer sandbox API (P19 FR-P19-01) |
| `developers.lawdocs.in` | Developer portal (P19) |
| `status.lawdocs.in` | Status page (hosted outside the primary region's failure domain, content contains no tenant data) |
| `trainings.lawdocs.in` | Unchanged — Graphy (D-16); DNS record carried over untouched |
| `[Consumer Help Brand domain]` | `apps/public` brand flavour (D-06); placeholder until the owner names it |

DNSSEC enabled; email authentication records (SPF, DKIM, DMARC `p=quarantine` then `p=reject` after 30 days of clean reports) carried over without breaking current mail; CAA records restrict issuers; HSTS with preload only after 30 days of clean HTTPS on all sub-domains [REC].

**FR-P00-20 — Infrastructure as code.** OpenTofu or Terraform ≥ 1.11 (ADR-0008) with S3 backend and lockfile. Modules: `org_scp`, `network`, `kms`, `rds_or_aurora`, `sealed_db`, `redis`, `opensearch`, `s3_quarantine`, `s3_documents`, `s3_originals`, `s3_exports`, `s3_backups`, `ecs_cluster`, `ecs_service`, `alb_waf`, `cloudfront`, `temporal`, `keycloak`, `cerbos`, `flags`, `observability`, `ses`, `secrets`, `backup`, `github_oidc`. CI runs `fmt -check`, `validate`, `tflint`, `checkov` (fail on HIGH) and posts the plan to the pull request; nightly drift detection opens an incident on drift.

### 4D. CI/CD skeleton and GitHub branch model (detail in P23)

**FR-P00-21 — Branch model (naming and rules owned by P23 FR-P23-03).** Trunk-based: `main` is protected and always releasable; short-lived branches `feat/<LD-1234>-<slug>`, `fix/…`, `chore/…`, `docs/…`, `refactor/…`, `perf/…`, `test/…`, `ci/…` with squash merge; `release/YYYY.MM.N` created only by `PLT_RELEASE_MANAGER` from a release tag to patch a deployed release; `hotfix/<release>-<LD-1234>-<slug>` with the fix landing on `main` first and cherry-picked to `release/*`. Branch protection on `main` from day one: pull request required, ≥ 1 reviewer (2 for paths owned by security, database or contracts), required checks (FR-P00-22), linear history, signed commits, no force-push. P23 adds rulesets, CAB linkage (OH13 `ChangeApproved`), freeze windows and environment protection.

**FR-P00-22 — CI on every pull request** (`.github/workflows/ci.yml`; actions pinned by commit SHA; `zizmor` lints workflows): install with cache; `turbo run lint typecheck test build` on affected packages; coverage gates (`packages/money`, `packages/ids`, `packages/audit` ≥ 95% lines, 100% branches on calculation code; overall ≥ 80%); OpenAPI generation from Zod and `oasdiff breaking` against `main` (breaking change fails unless labelled `api-major` with ADR link); AsyncAPI diff for internal events; migration job (apply all migrations to a fresh PostgreSQL Testcontainer; RLS lint; pgTAP; expand-contract checker FR-P00-30; export-map contract test FR-P00-87; data-catalogue check); Storybook build with axe (0 serious/critical); Semgrep (OWASP + custom rules: no raw pool import, no `console.log`, no outbound `fetch` outside `packages/connectors`, no decryption without `@DecryptFor`, no mutating handler without the audit interceptor, no Aadhaar-number regex match in fixtures or logs); CodeQL; gitleaks; osv-scanner and Trivy; Syft SBOM (CycloneDX); licence policy (deny AGPL/SSPL in shipped code); `seo:check` on `apps/public` (FR-P00-80). The **NN suite** (`pnpm nn`) is a required check; a failing NN test blocks merge.

**FR-P00-23 — CD skeleton** (`deploy.yml`): build OCI images once per commit (multi-stage, distroless Node runtime, non-root UID 10001, read-only root filesystem); sign with cosign keyless (GitHub OIDC); attach SBOM and provenance; push to ECR with immutable tags (git SHA). Deploy via GitHub OIDC to environment-scoped IAM roles (no long-lived keys). Order: migrations as a one-off task (forward-only, expand-contract) → `api`, `worker`, `outbox-relay` (blue/green with canary) → web apps. Automatic rollback on alarm (5xx > 1% for 3 minutes; p95 > 800 ms for 5 minutes; SLO burn rate > 14.4 on the 1-hour window).

**FR-P00-24 — Backups skeleton.** Automated RDS snapshots + PITR (35 days); daily logical dump of `ld_core` and `ld_sealed` to `ld-backup` (Object Lock governance mode; 35 daily, 13 monthly, 8 FY-end); a weekly automated restore test into an isolated account that runs `make verify-audit` and row-count checks and records evidence (P23 completes the drill programme).

### 4E. Tenancy package, row-level security and session context (NN-01)

**FR-P00-25 — Tenant model.** `core.tenants`: `id` (`ten_` + ULID), `slug`, `display_name`, `kind` ∈ {`PLATFORM` (`ld-platform`, seeded, cannot be suspended or deleted), `PERSONAL` (one individual's workspace; created at first sign-up in P01), `COMPANY` (company, LLP, firm, trust, society or other organisation), `PRO_FIRM` (a professional's practice or firm: advocates, CA, CS, tax practitioners), `CONSUMER_HELP` (the brand's operating tenant for case managers; customers' consumer cases live in their own PERSONAL tenants under the brand — P15), `GROUP` (umbrella for a client group of COMPANY tenants), `SANDBOX`}, `brand_code` (`LAWDOCS` default; `CONSUMER_HELP` for D-06; FK `core.brands`), `operating_entity_id` (FK `core.operating_entities` — the fiduciary and contracting entity, D-08), `status` ∈ {`PENDING_CONFIRMATION`, `TRIAL`, `ACTIVE`, `GRACE`, `SUSPENDED`, `OFFBOARDING`, `ARCHIVED`}, `data_region` (`ap-south-1` only), `default_locale`, `enabled_locales[]`, `timezone` (default `Asia/Kolkata`), `year_basis` (`CALENDAR` default for PERSONAL, `INDIAN_FY` default for COMPANY — feeds `LD-EXPORT-1.0` folder years), `parent_tenant_id` (GROUP umbrella), `ecosystem_org_id` (Ecosystem Spec §4.1 `org_id`, nullable), `isolation_tier` (`shared` | `dedicated_db`), `dedicated_key` (bool), `created_via` (`SELF_SERVE`, `PARTNER_API`, `OH_PROVISIONING`, `MIGRATION`, `CONSOLE`), `created_at`, `recorded_at`.

**FR-P00-26 — Brands and operating entities.** `core.brands` (`code`, display name, domains, logo asset, design-token theme, legal-entity default, support contacts, help-centre space) and `core.operating_entities` (`[LawDocs Operating Entity]` placeholder: legal name, CIN, GSTIN, registered office, DPO, Grievance Officer, Nodal Officer, CERT-In point of contact, NeGD contact; configurable in Super Admin → Legal entities; maker-checker on change). Every notice, invoice reference, consent artefact and grievance record carries `operating_entity_id`, so a separate Consumer Help entity is a configuration change, not a code change (D-06, D-08, NN-23).

**FR-P00-27 — Legal entities on every tenant row.** `core.legal_entities` (`ent_` + ULID): `tenant_id`, `constitution` (code table: `INDIVIDUAL`, `PVT_LTD`, `PUBLIC_UNLISTED`, `PUBLIC_LISTED`, `OPC`, `SECTION_8`, `LLP`, `PARTNERSHIP`, `PROPRIETORSHIP`, `HUF`, `TRUST`, `SOCIETY`, `COOP`, `FOREIGN_CO`, `GOVT_BODY`, `OTHER`), identifiers (CIN/LLPIN/FCRN; PAN as ciphertext + blind index + masked form; GSTINs child table; LEI; Udyam), registered address, incorporation date, fiscal-year start, `is_primary`. A PERSONAL tenant has exactly one legal entity of constitution `INDIVIDUAL` representing the person, so **every tenant row carries `tenant_id` and `legal_entity_id`** without special cases (NN-01). Legal entities are bitemporal (`valid_period`, `recorded_at`, `superseded_at`) because names, addresses and constitutions change.

**FR-P00-28 — Database roles.** `ld_owner` (owns schemas; NOLOGIN), `ld_migrator` (runs migrations), `ld_app` (LOGIN, NOBYPASSRLS, DML only), `ld_platform` (LOGIN, NOBYPASSRLS; used only by console services for policy-checked, logged cross-tenant reads), `ld_reporting_ro` (replica; RLS applies), `ld_sealed_app` (LOGIN on `ld_sealed` only, allow-listed modules), `ld_migration` (LOGIN on `mig_stage` and target schemas during runs only; disabled outside a run window). No application role has `BYPASSRLS` or owns tables. Every tenant table has `ENABLE` and `FORCE ROW LEVEL SECURITY`.

**FR-P00-29 — Session context.** Every transaction sets, via `set_config(…, true)`: `app.tenant_id`, `app.legal_entity_ids` (array, when ABAC narrows), `app.user_id`, `app.person_id`, `app.actor_type` (`user` | `guest` | `service` | `agent` | `platform` | `delivery` | `professional` | `partner`), `app.on_behalf_of`, `app.grant_id` (delivery/group/external grant in use), `app.brand_code`, `app.request_id`, `app.break_glass_id`. Data access only through `db.withContext(ctx, tx => …)`; a lint rule forbids importing the raw pool. If `app.tenant_id` is missing, `core.current_tenant()` returns NULL and every tenant policy returns zero rows (fail closed, `LD-CORE-002` logged). Pooling: transaction-scoped settings only; PgBouncer in transaction mode only if every setting is transaction-local (ADR-0009).

**FR-P00-30 — RLS policy template, lint and expand-contract checker.**

```sql
ALTER TABLE dms.documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE dms.documents FORCE ROW LEVEL SECURITY;
CREATE POLICY tenant_wall ON dms.documents
  USING (tenant_id = core.current_tenant())
  WITH CHECK (tenant_id = core.current_tenant()
              AND legal_entity_id = ANY (core.tenant_legal_entities()));
```

RLS is the tenant wall; Cerbos (P01/P02) is the room-level control through query plans. `packages/db/tests/rls_lint.sql` fails if any table with a `tenant_id` column lacks `relrowsecurity AND relforcerowsecurity` and a policy referencing `core.current_tenant()`, unless listed in `db/rls-exemptions.yaml` (global reference tables only: code tables, jurisdictions, published platform templates heads, glossary). The **expand-contract checker** (NN-12) parses each migration and fails on: `DROP COLUMN`/`DROP TABLE`/`RENAME` of an object still referenced by deployed code of the previous release; `ALTER COLUMN … TYPE` without a shadow column; `NOT NULL` added without a backfill step and a validated constraint; a backfill without an idempotency marker in `core.backfill_runs`.

**FR-P00-31 — Isolation beyond the database.** `packages/tenancy` provides tenant-scoped helpers that every adapter must use: Redis keys `t:{tenant_id}:…`; OpenSearch tenant-filtered aliases enforced in the search adapter (no raw client); S3 object keys `tenants/{tenant_id}/…` with presigning only through `packages/tenancy`; Temporal workflow IDs prefixed with the tenant; pgvector queries always filtered by tenant and permission plan. `NN-01_cross_tenant_denied` seeds two tenants with generated rows for every table and asserts zero leakage through `ld_app` for SELECT, UPDATE and DELETE, and checks Redis, OpenSearch, S3 prefixes and workflow IDs; `NN-01_idor_per_endpoint` generates a request per route with tenant B's IDs under tenant A's session and expects 404 (no existence leak).

**FR-P00-32 — Field-level encryption and masking.** `packages/crypto` (server-only): envelope encryption with AWS KMS and a keyring per data class (`pii`, `spi`, `financial`, `legal`, `legal_privileged`, `hr`, `credential`, `kyc_artefact`) and, for `dedicated_key` tenants, per tenant. Column convention: `<field>_enc bytea`, `<field>_bidx bytea` (HMAC-SHA-256 blind index with a per-tenant key for equality lookups: PAN, mobile, email), `<field>_masked text` (PAN `ABCDE****F`, mobile `98******10`). Decryption requires `@DecryptFor(purpose)`, which writes `core.access_log`. **Aadhaar numbers are never stored in any form** — not encrypted, not hashed, not tokenised (NN-04): only the last four digits where a law requires display, plus a reference to the verification artefact and its result (P01). `NN-04_no_aadhaar_column` scans the data catalogue and fails on any column named or tagged as an Aadhaar number; `NN-04_masking_fixture` asserts that the shared masking function replaces the first eight digits of any 12-digit Aadhaar-pattern number (Verhoeff-valid) in text with `XXXX XXXX` and keeps the last four.

### 4F. Audit ledger, Correction Entries, access log and break-glass (NN-02, NN-45)

**FR-P00-33 — What is audited.** Every mutating handler writes a ledger event in the same database transaction as the business change through `AuditService.append()` → `core.append_audit_event(jsonb)`; a NestJS interceptor makes this the default and Semgrep fails any mutating route that opts out without `@AuditExempt(reason)` approved by a code owner (`NN-45_mutation_writes_ledger` executes every mutating route on seeded data and asserts a ledger row in the same transaction ID). Also audited: logins, step-ups, failed logins, consent captures and withdrawals, verifications, shares and share revocations, downloads of originals, exports, decrypts and reveals, AI tool calls that change data, signing ceremony events, payments mirrored from OH8, grant lifecycle, break-glass, settings and flag changes, migration promotions.

**FR-P00-34 — Event structure and hash chain.** `core.audit_events` (partitioned by month; append-only):

| Column | Meaning |
|---|---|
| `chain_id` | Tenant ID, or `chn_platform` / `chn_content` for platform and published-content actions |
| `seq` | Gap-free sequence per chain (per-chain advisory lock) |
| `event_id` | `aev_` + ULID |
| `occurred_at` / `recorded_at` | Business time / commit time (`clock_timestamp()`, never client-supplied) |
| `actor_type`, `actor_id`, `person_id`, `on_behalf_of`, `act_as_role`, `grant_id`, `brand_code` | Who acted, in what capacity, under which grant (an RM acting as maker in a client tenant records `actor_type = delivery` and the delivery grant) |
| `session_id`, `ip_hmac`, `ua_hmac`, `device_id`, `request_id`, `trace_id` | Correlation without raw PII |
| `module`, `action` (`<module>.<aggregate>.<verb>`), `aggregate_type`, `aggregate_id`, `aggregate_version`, `business_refs[]` | What, including business reference IDs (`LD-AGR-2026-000123`) for history-by-reference queries |
| `before_digest`, `after_digest` | SHA-256 of RFC 8785 canonical JSON of the aggregate before/after |
| `change_set` | Field paths changed; old/new values only for `PUBLIC`/`INTERNAL`/`CONFIDENTIAL` fields; digests only for higher classes |
| `reason_code`, `comment_ref`, `correction_id` | Why; link to a Correction Entry when applying one |
| `prev_hash`, `row_hash` | `row_hash = SHA-256(prev_hash ‖ canonical(event without row_hash))` |

Readable "what changed" views come from `change_set` plus each module's `*_history` tables (written by trigger in the same transaction, under the table's own RLS and encryption). The ledger proves integrity; history tables carry content.

**FR-P00-35 — Immutability.** `core.audit_events`, `core.audit_anchors` and `core.access_log` grant only `INSERT` through `SECURITY DEFINER` functions; a trigger raises `LD-CORE-001` on `UPDATE`, `DELETE` or `TRUNCATE` by any role including `ld_owner` (`NN-02_ledger_append_only`). Partitions older than the current month are verified and exported to Object Lock storage; retention ≥ 8 years (tenant may lengthen, never shorten).

**FR-P00-36 — Verification and anchoring.** `AuditChainVerifyWorkflow` daily 02:15 IST for chains changed in the last 48 hours and weekly (Sunday 03:00 IST) for all chains. `AuditAnchorWorkflow` 00:10 IST: per chain, Merkle root over the previous day's `row_hash` values, signed with an asymmetric KMS key (ECC_NIST_P256), written to `core.audit_anchors` and to the originals bucket under Object Lock; optional RFC 3161 timestamp behind `core.audit.anchor_tsa.enabled` = OFF until a TSA contract exists. Tenants download anchors and verify offline with `ld-verify` shipped in every export (P20). A mismatch emits `in.lawdocs.core.AuditChainBroken.v1`, opens a Critical incident, freezes critical configuration changes and notifies `PLT_SECURITY_OFFICER` and the affected tenant owner within 24 hours. A broken chain is never recomputed; a signed break-notice event records the last verified anchor and the affected range.

**FR-P00-37 — Correction Entries.** The only way anyone (super admin, operations staff, tenant admin) changes a recorded fact after the fact (NN-02; CH-26). `core.correction_entries` (`cor_` + ULID): `tenant_id`, `scope` (`RECORD_FIELD`, `DOCUMENT_VERSION`, `MASTER_DATA` — crucial client details, `SETTING`, `ENTITLEMENT`, `DATE`, `AUDIT_ANNOTATION`, `CONTENT`), `target` (aggregate type, ID, version, field paths or ledger `event_id`), `old_value_digest`, `new_value` (encrypted per class), `effective_at`, `recorded_at` (never editable), `reason_code` (`DATA_ENTRY_ERROR`, `CLIENT_REQUEST`, `LEGAL_ORDER`, `MIGRATION_FIX`, `CONTENT_ERRATUM`, `SECURITY_INCIDENT`, `DUPLICATE`, `OTHER`), `justification` (≥ 50 characters), `supporting_doc_ids` (required for `CLIENT_REQUEST` and `LEGAL_ORDER`), `requested_by`, `approved_by` (≠ requester; SoD), `tenant_ack` (platform corrections of `MASTER_DATA` and `DOCUMENT_VERSION` need the tenant owner's prior approval by default — `core.correction.tenant_ack_mode`), `visibility = TENANT_VISIBLE` (no hidden mode), `state` (`DRAFT → SUBMITTED → APPROVED → [CLIENT_APPROVAL_PENDING] → APPLIED`; `REJECTED`, `WITHDRAWN`; `APPLIED → REVERSED` by a new entry; emergency path `APPLIED_EMERGENCY → RATIFIED | AUTO_REVERTED`; Appendix A §A.1 governs). Applied corrections show a "Corrected" badge wherever the value appears and are listed in the tenant's **Changes made by LawDocs** register (SCR-P00-08) and exported as `Corrections_Register.xlsx`. A correction can never change `recorded_at`, delete a ledger event, alter another tenant, overwrite an original (originals stay under Object Lock; a correction supersedes by reference) or bypass a legal hold.

**FR-P00-38 — Access log.** `core.access_log` (append-only): reads of `SPI`, `LEGAL_PRIVILEGED`, `KYC_ARTEFACT`, `CREDENTIAL` data; decrypts; reveals; downloads of originals; exports; platform-scope reads; delivery-grant and break-glass reads. Tenants see their own access log in Settings › Audit & history (P02 adds filters by grant).

**FR-P00-39 — Break-glass schema.** `core.break_glass_events`: actor, tenant, scope (modules, read or read-write), incident/ticket reference, justification (≥ 30 characters), approvers (two-person mandatory for any scope — NN-17), start, end (≤ 4 hours default), tenant notified at, post-session report generated at (≤ 24 hours, NN-17). P02/P18 build the request and reporting UI; P00 builds schema, service, notifications and the `NN-17_break_glass_dual_approval` test.

### 4G. Identifiers, business references, money and time

**FR-P00-40 — Entity IDs.** Opaque prefixed ULIDs (`<prefix>_` + 26 Crockford base32), stored as `text` with a `CHECK` on the pattern, generated only by `packages/ids`. The prefix registry (`packages/ids/prefixes.ts`, mirrored in `core.id_prefixes`) is seeded with every prefix in Appendix B §B.1.3 (master §5.4; X-01) plus the P00 additions `aev_` (audit event), `cor_` (correction entry), `anc_` (audit anchor), `mig_` (migration run), `bkf_` (backfill run), `brd_` (brand), `ope_` (operating entity). IDs never encode location, tenant, year or region, so a storage, region or vendor change never re-keys data (NN-12). Event IDs are UUIDv7 (RFC 9562) per the Ecosystem Spec §3.2.

**FR-P00-41 — Business reference IDs.** `packages/ids/bizref` formats and parses human-readable permanent references: `LD-<FAMILY>-<YYYY>-<NNNNNN>` with families `AGR`, `MAT`, `CAS`, `TMK`, `ENG`, `GRV`, `NTC` (master §5.4; Appendix B §B.1.4) and P00 additions `ORD` (legacy and new service orders mirror), `DOC` (vault document display reference, optional). Allocation by `core.allocate_business_ref(family, n)` inside the creating transaction; a series never decreases; a rollback leaves a gap, never a duplicate; the year segment is the allocation year and never changes when the record is later edited. The universal resolver route `/r/<ref>` opens the record if the user can see it and otherwise returns the same "not found" as a non-existent reference (no existence leak). Legacy identifiers (MongoDB `_id`, PayU `txnid`, legacy order numbers) are stored as **aliases** in `core.ref_aliases` (`alias_type` = `MONGO_ID`, `PAYU_TXN`, `LEGACY_ORDER_NO`, `LEGACY_SLUG`) and resolve to the canonical record.

**FR-P00-42 — Money.** `NUMERIC(20,4)` + `currency char(3)` (INR default); `packages/money` on decimal.js (precision ≥ 40; explicit rounding per calculation). JSON money is `{"amount": "1499.00", "currency": "INR"}` (Ecosystem Spec §5.1). LawDocs computes no tax: quotes and invoices come from OH8 through `BILLING_PORT` (D-02). Statutory fees, stamp duty, professional fees and LawDocs fees are separate line types in every money structure (NN-22).

**FR-P00-43 — Time.** Store UTC `timestamptz`; render in the viewer's timezone with the zone shown on audit screens; NTP synchronisation of all hosts to NIC/NPL servers or sources traceable to them (CERT-In Directions 28 Apr 2022, direction (i); R3 LG-079; `NN-27_ntp_config` checks container and host configuration).

### 4H. Events, outbox, inbox, idempotency and the ecosystem contracts package

**FR-P00-44 — Two event families.** Internal: `in.lawdocs.<module>.<EventName>.v<n>` (PascalCase past tense) between LawDocs modules and to tenant webhooks (P19). Ecosystem: `in.infrabyx.<domain>.<EventName>.v<major>` with `source = urn:infrabyx:lawdocs:<tenantid>`, published **only by `int`** after data-class and `consentref`/`legalbasis` checks (NN-24). A module never emits an ecosystem event; `int` maps internal events under versioned mappings. New LawDocs domains/events are proposed in Appendix Y (Ecosystem Spec v1.2 change request), never improvised.

**FR-P00-45 — Transactional outbox and inbox.** `core.outbox` (partitioned daily; CloudEvents 1.0 columns: `id` UUIDv7, `source`, `type`, `subject`, `time`, `datacontenttype`, `dataschema`, `data`, `tenantid`, `dataclass`, `schemaver`, `seq` per subject, `correlationid`, `causationid`, `traceparent`, `consentref` or `legalbasis`, `status`, `attempts`, `next_attempt_at`, `published_at`) written in the business transaction; `outbox-relay` publishes in `seq` order per subject; at-least-once; exponential backoff; dead-letter after 12 attempts with an alert; retention ≥ 90 days. `core.inbox` stores `(source, id)` and business key before processing (deduplication); `seq` gaps parked 15 minutes, then catch-up fetch, then a reconciliation break.

**FR-P00-46 — Idempotency.** `core.idempotency_keys (tenant_id, key, route, request_hash) → stored response` for 24 hours on every mutating API; key reuse with a different body returns `422 LD-CORE-020 idempotency-key-reuse`. Every adapter in `packages/connectors` requires an idempotency key for external side effects and writes a reconciliation record (`core.side_effects`: port, provider, external reference, request hash, status, reconciled_at) (`NN-46_side_effect_idempotent` replays each adapter call twice against fakes and asserts one external effect).

**FR-P00-47 — Ecosystem contracts package import.** `packages/contracts` is generated from a pinned release of the group `infrabyx-contracts` repository (OpenAPI 3.1, AsyncAPI 3.0, JSON Schema 2020-12, code tables). A `contracts.lock` records the release tag and SHA-256 of every imported schema; CI fails if a vendored schema differs from the lock or if a LawDocs handler validates an ecosystem payload against a schema not in the lock. `docs/ecosystem/infrabyx-integration-spec.md` is committed unchanged with its SHA-256 in `docs/ecosystem/CHECKSUMS`. LawDocs-specific subjects that do not yet exist in v1.1 (owner code `LD`, the LawDocs `source` URN, `documents`/`signing` events originated by LawDocs, LawDocs as a `TenantProvisioned` consumer) are drafted in Appendix Y and live in `packages/contracts/proposed/` with status `PROPOSED`; `int` refuses to publish a `PROPOSED` subject to another product until the change request is accepted (feature flag `int.ecosystem.proposed_subjects.enabled` = OFF).

**FR-P00-48 — Error model.** RFC 9457 problem details: `type` (`https://api.lawdocs.in/problems/<code>`), `title`, `status`, `detail` (no PII), `instance`, `code` (`LD-<MODULE>-<NNN>`), `correlation_id`, `retryable`, `errors[]` (JSON Pointers), `user_message_key` and `help_key` (`hlp.<module>.<term>`) for an actionable, localised message ("what happened, why, what you can do"). The error register lives in `packages/contracts/errors.yaml`; CI fails on a thrown code not in the register.

### 4I. Settings heads, feature flags, kill switches and the verification log

**FR-P00-49 — Settings registry heads (NN-29).** Create the heads of the P03 registry, `cfg.setting_definitions` (`key` `<module>.<area>.<key>`, module, tier ∈ {`PLATFORM`, `BRAND`, `PLAN`, `TENANT`, `ENTITY`, `DEPARTMENT`, `USER`}, type, default, bounds, allowed scope levels, `changed_by_roles[]`, `maker_checker` (bool), `effective_dated` (bool), `help_key`, `linked_rule` (R3 `LG-xxx`), `linked_nn`) and `cfg.setting_values` (bitemporal; scope chain platform → brand → plan → tenant → entity → department → user). `packages/config` reads only registered keys; reading an unregistered key throws at boot in non-prod and fails CI (`NN-29_settings_registered`). The registry is loaded from `cfg/registry/*.yaml` per module and published as Appendix R; P03 owns these tables and builds the resolver UI and rule engine on them without migration (P03 §7.2 lists the full columns; P00 creates only the head columns named here).

**FR-P00-50 — Feature flags.** Flag service behind `packages/config` (Unleash self-hosted in ap-south-1 or the group-standard tool per ADR-0012); flags registered in `cfg.flags` (P03 registry; P00 creates the head with `key`, owner, purpose, default, `kill_switch` bool, `approver_role`, `requires_verification_id` (link to a `[VERIFY]` row), `expires_at`, `linked_open_item`). A flag with `requires_verification_id` cannot be switched ON in prod until the linked row in `docs/compliance/verification-log.md` is marked VERIFIED with date, source and verifier (NN-38; `NN-38_verify_gated_flags`). Prod flag changes are audited; approver and kill-switch flags need maker-checker.

**FR-P00-51 — Kill-switch registry (NN-39).** One registry for the whole platform: `cfg.kill_switches` / `cfg.kill_switch_events`, owned by P03 (FR-P03-84…88; state machine Appendix A §A.17 governs, Resolution R-A-09). P00 creates the heads (code, scope ∈ {`AI_AGENT`, `REVENUE_STREAM`, `VENDOR_ADAPTER`, `CONSUMER_VERTICAL`, `OUTBOUND_CHANNEL`, `CONNECTOR`, `CREDENTIAL_REVEAL`, `BRAND`}, target key, state, engaged_by, engaged_at, reason) and emits only the canonical events `in.lawdocs.cfg.KillSwitchEngaged.v1` / `in.lawdocs.cfg.KillSwitchReleased.v1`; no `core.*` kill-switch table or event exists. Propagation by Redis pub/sub; adapters and agents check before each call; propagation SLO ≤ 60 seconds (`NN-39_kill_switch_propagation`). P00 seeds entries for every adapter port declared so far (`SMS`, `WHATSAPP`, `EMAIL`, `ESIGN`, `ESTAMP`, `KYC_*`, `DIGILOCKER`, `PAYMENT`, `AI_GATEWAY`, `LEGACY_PORT`).

**FR-P00-52 — Verification log.** `docs/compliance/verification-log.md` (rendered from `docs/compliance/verification-log.yaml`): one row per `[VERIFY]` item across the pack (ID, statement, source to check, owner, status `OPEN`/`VERIFIED`/`REJECTED`, date, evidence link, flags gated). P00 seeds it from every `[VERIFY]` tag in P00–P02 and the master prompt; later phases append. Appendix W mirrors it.

### 4J. Storage, ingest and immutable originals (NN-09)

**FR-P00-53 — Buckets** (ap-south-1, replicated to ap-south-2; block public access; SSE-KMS; VPC-endpoint policies; presigned URLs ≤ 5 minutes):

| Bucket | Purpose | Lock / lifecycle |
|---|---|---|
| `ld-{env}-quarantine` | Every upload lands here first | Delete after 24 h |
| `ld-{env}-documents` | Drafts, working copies, derived renditions (`drv_`) | Versioning; no lock |
| `ld-{env}-originals` | Original uploads and signed/executed files, evidence packs, audit anchors | **Object Lock compliance mode**; default retention 8 years from write (tenant may lengthen per class, never shorten); legal hold per object |
| `ld-{env}-exports` | Generated export packages | Lifecycle delete 7 days (P20 can extend for BYO transfer) |
| `ld-{env}-backups` | Logical backups; legacy archive | Object Lock governance mode in `ld-backup`; schedule FR-P00-24 |
| `ld-{env}-public-assets` | Public site media | CloudFront origin; no tenant data |

**FR-P00-54 — Ingest pipeline skeleton.** `POST /v1/uploads/intents` returns a presigned PUT to quarantine with required `x-amz-checksum-sha256`; on object creation `IngestWorkflow`: (1) MIME by magic bytes against the allow-list (PDF, DOCX, DOC, XLSX, XLS, CSV, PPTX, TXT, RTF, ODT, EML, MSG, PNG, JPEG, HEIC, WEBP, TIFF, ZIP for folder intake, chat-export TXT/ZIP, MP3/M4A/OGG voice notes, MP4 short video) with size limits from `dms.upload.max_mb`; (2) ClamAV scan; macro-enabled Office files rejected unless the tenant allows with a warning; (3) server-side SHA-256 recomputed and compared; (4) classify as ORIGINAL (→ originals bucket under lock) or WORKING (→ documents); (5) write `dms.document_hashes` (hash-chained per tenant); (6) emit `in.lawdocs.dms.DocumentIngested.v1`; (7) delete quarantine object. Rejections (codes owned by P04 §13; Appendix B §B.5): `LD-DMS-002` (malware), `LD-DMS-032` (checksum mismatch), `LD-DMS-001` (type not allowed). No original is ever overwritten; a "replace" creates a new version and keeps the old one locked (`NN-09_original_immutable` attempts overwrite and delete within retention and expects failure). P04 builds the Legal Vault, folders, sharing and bulk intake; P05 adds OCR and Aadhaar masking of derived text on top of this pipeline.

**FR-P00-55 — Derived-text masking hook.** The ingest pipeline exposes a `beforeDerivedTextPersist` hook that P05 must use; P00 wires the shared Aadhaar-masking function into it so that no derived text (OCR, search index, AI context, preview) ever stores the first eight digits of an Aadhaar number (NN-04).

### 4K. Observability, errors and performance budgets

**FR-P00-56 — Telemetry.** OpenTelemetry SDK in every app; traces, metrics and logs to an India-hosted backend (self-hosted Grafana LGTM in ap-south-1 or a vendor with India residency [VERIFY]); no log shipping outside India; ICT logs retained ≥ 180 days in India (CERT-In Directions direction (iv); R3 LG-079) and 400 days by default (`eng.logs.retention_days_india`, P23-owned), with DPDP Rule 6(e)/8(3) one-year floor where personal-data processing logs are concerned (R3 LG-065) — the effective floor per log class is max(180 days, 1 year where applicable, 7 years for eSign evidence logs). Log schema: JSON `timestamp`, `level`, `service`, `trace_id`, `span_id`, `tenant_id` (opaque), `user_id` (opaque), `request_id`, `event`, `code`. The scrubber removes emails, mobiles, PAN, Aadhaar patterns, card-number patterns, OTPs, JWTs, secrets and document text before export (NN-32; `NN-32_log_scrubber` feeds a corpus of seeded secrets and identifiers through every exporter and asserts none survives).

**FR-P00-57 — Health and status.** `/healthz` (liveness), `/readyz` (readiness, internal), `/v1/platform/version` (build, commit, SBOM digest). Status page publishes incidents without tenant data.

**FR-P00-58 — Initial budgets (P23 confirms).** API p95 ≤ 300 ms reads / ≤ 800 ms writes (master §14) at 200 concurrent users per tenant; public pages: Largest Contentful Paint ≤ 2.5 s at p75 on 4G mid-range Android, CLS ≤ 0.1, INP ≤ 200 ms; my.lawdocs.in first contentful paint ≤ 1.5 s; availability 99.9% monthly for apps/web, apps/api and signing (master §14); RPO ≤ 15 minutes and RTO ≤ 4 hours in prod.

### 4L. Design system, i18n and accessibility foundations (NN-28)

**FR-P00-59 — Tokens and components.** `packages/tokens` (colour, typography, spacing, radius, elevation, motion; light, dark and high-contrast themes; brand themes for LawDocs and `[Consumer Help Brand]`); `packages/ui` on shadcn/ui (Radix) with accessible primitives; contrast checked automatically for every brand theme (WCAG 2.2 AA). TanStack Table for data grids with keyboard navigation and a "table view" for every chart.

**FR-P00-60 — i18n.** ICU catalogues in `packages/i18n`; launch locales per D-07 (en, hi, bn, mr, te, ta, gu, kn, ml, pa) scaffolded with English source and pseudo-locale testing for truncation and RTL (Arabic is a reading language for documents only, D-07, but the UI must not break when an RTL document title is shown); Indian number formatting (lakh/crore) as a user preference; dates `DD MMM YYYY`.

**FR-P00-61 — Help keys and accessibility gates.** Every field, column, menu item, status and error has a stable help key (`hlp.<module>.<term>`) so P21 can attach "i" explanations without code changes (R-019). CI runs axe on Storybook and on SSR pages (0 serious/critical); manual screen-reader passes are scheduled per release by P23. No accessibility overlay script is permitted on any surface (NN-28; Semgrep rule bans known overlay domains in CSP and HTML).

### 4M. NN test harness and synthetic data

**FR-P00-62 — NN harness.** `tests/nn/` holds one spec file per NN rule (`NN-01_*.spec.ts` … `NN-50_*.spec.ts`) and `tests/nn/registry.yaml` mapping each NN to: test files, owning phase, status (`ACTIVE` — must pass; `SCAFFOLD` — placeholder test asserting the rule's precondition exists, e.g., the flag or setting key is registered; `PENDING_PHASE` — phase not started). `pnpm nn` runs all ACTIVE and SCAFFOLD tests; CI fails if a phase's exit-gate job runs while any NN owned by that phase is not `ACTIVE`. P00 activates the NN tests listed in this file's header; every other NN has a SCAFFOLD test.

**FR-P00-63 — Seed profiles (synthetic only).** `dev` (two COMPANY tenants, three PERSONAL tenants, one PRO_FIRM, ten users each); `demo` (a startup, an SME, an NBFC with legal department, a CA firm, an advocate's chamber, four individuals across life events — tenancy, property purchase, cheque-bounce dispute, vehicle sale — and a Consumer Help brand tenant with three synthetic grievances); `load` (2,000 tenants, 5 million documents metadata, 500,000 agreements, 20 million ledger events); `legacy-mirror` (synthetic re-creation of the shape of legacy data — counts, field distributions, edge cases such as duplicate emails, orders without payments, refunds — from the counts in `docs/discovery/`, no real values).

**FR-P00-64 — Synthetic identifier rules.** Seeds use reserved patterns that can never be mistaken for real identifiers: emails at `example.com`/`example.in` (RFC 2606/IANA reserved [VERIFY `.in` reservation; otherwise `example.com` only]); mobiles `+91 5xxxxxxxxx` (Indian mobile numbers begin 6–9, so a leading 5 is never a valid mobile [VERIFY current numbering plan]); PANs `ZZZPZ9999Z`-style with a `SYNTHETIC` flag column; CINs prefixed `X`; GSTINs with State code `00`; **no Aadhaar-like numbers at all**, not even synthetic — only a last-four value `0000` where a fixture needs one (NN-04). A CI check (`seed:lint`) rejects seeds containing 12-digit Verhoeff-valid numbers or mobiles beginning 6–9.

**FR-P00-65 — Fixture library.** `packages/testing` provides two-tenant fixtures, persona factories for every role code in master §1.4 / Appendix D, guest and agent principals, a fake ESP/ESP-aggregator, fake DigiLocker, fake SMS/WhatsApp/email sinks, fake OH8 billing and fake ecosystem gateway, so later phases write NN and acceptance tests without real providers.

### 4N. Data migration: MongoDB Atlas → PostgreSQL

**FR-P00-66 — Principles.** (1) Source is a point-in-time restore of Atlas, never the live cluster. (2) Every migrated row carries `core.migration_lineage` (`source_system = 'lawdocs-legacy'`, `source_collection`, `source_id`, `source_hash` (SHA-256 of canonical JSON of the source document), `migration_run_id`, `transform_version`). (3) Transforms are code in `tools/migration/` with unit tests and golden files; no hand edits in SQL consoles. (4) Each run produces a reconciliation report stored as evidence in the originals bucket. (5) Runs are idempotent (upsert on lineage key) and repeatable; the final run happens in the cut-over window as a delta from the rehearsal snapshot. (6) Legacy defects are never silently fixed: rows migrate as-is with a `dq_flags[]` value and an owner task, or are corrected by a `MIGRATION_FIX` Correction Entry approved by the owner, so the customer can see what changed. (7) Personal data is migrated only where the disposition register records a purpose and retention basis approved by `PLT_DPO`; everything else is archived or deleted (FR-P00-71).

**FR-P00-67 — Expected collection map** (to be confirmed by `03-data-model.md`; unknown collections get a disposition before the first rehearsal):

| Legacy collection (expected) | Target | Rule |
|---|---|---|
| `users` / `customers` | P01 `iam.persons`, `iam.users` (Keycloak), PERSONAL tenant per individual; COMPANY tenant where the legacy record carries a company name/GSTIN and the user confirms at first login | Email and mobile become contact points marked **unverified** until the user verifies them in P01; duplicates by email/mobile are merged only on exact match of both, else flagged `DUP_CANDIDATE` for the user to resolve at first login |
| password hashes | Keycloak credential import only if bcrypt or Argon2id with known parameters and Keycloak can import them [VERIFY Keycloak hash-provider support]; otherwise no import — users sign in by OTP (P01 default) and may set a password later | Never decrypt or re-hash plaintext; MD5/SHA-1/unsalted hashes are discarded and recorded in `09-security-findings.md` |
| `admins` | `ld-staff` realm candidates; re-provisioned from OH10, never migrated as accounts | Legacy admin accounts are disabled at cut-over |
| `orders` | OH8 historical orders (system of record) via the OH4 migration import; LawDocs `bil.order_mirror` with business ref `LD-ORD-<year>-<n>`; legacy order number as alias | Amounts as NUMERIC; status mapped by an owner-approved table (PAID, FAILED, REFUNDED, PARTIALLY_REFUNDED, CANCELLED, ABANDONED); line items split into LawDocs fee / professional fee / government fee / GST where the legacy data allows, else one line `LEGACY_UNSPLIT` |
| `payments` / PayU callbacks | OH8 payment history; LawDocs `bil.payment_mirror` | PayU `txnid` and gateway reference kept as aliases; card fields (if any exist) are **not migrated**, the collection is purged after evidence capture and the incident is recorded (PCI DSS) |
| `invoices` (PDFs or data) | Archived invoice PDFs to the customer's tenant under `10 Billing and Invoices/<FY>/` and to OH8 as historical documents; no re-issue | GST invoices are never regenerated; the archived file is the record (CGST Rules r.46 [VERIFY]) |
| `documents` / purchased drafts / uploads (GridFS, S3, Cloudinary or disk) | `dms` via the ingest pipeline into the owner's PERSONAL or COMPANY tenant; originals locked; hash computed at migration ("integrity assured from migration date") | Aadhaar masking applies to derived text; file names preserved; folder placed by document type mapping; unknown types to `Imported from old LawDocs/` |
| `blogs` / `posts` | `web.posts` (`pst_`), status `MIGRATED_REVIEW` (noindex until reviewed) or `PUBLISHED` where the content editor approves; slugs preserved or 301-mapped | Outdated law references are flagged for P21 (R5 §5) — migration does not rewrite content |
| `pages` / CMS fragments | `web.pages` (`pg_`) drafts for P21 | Copied third-party text flagged `R5_COPIED` and never published as is (D-04, R5 §4) |
| `enquiries` / `contacts` / `leads` / consultation requests | Operations Hub CRM (OH3) through the OH4 import, **only** the business-contact fields, with consent status `LEGACY_UNCONSENTED` unless a consent record exists | Marketing suppressed until fresh consent (NN-19, NN-26); service follow-up on an open request is allowed; retention 12 months from last contact then delete [REC; COUNSEL] |
| `chatlogs` / chatbot conversations | **Not migrated** to Vidhi or any AI store (NN-15). Encrypted archive in `ld-backup` for 90 days for dispute handling, then deleted with a destruction certificate, unless the owner records a lawful retention purpose [OWNER; COUNSEL] | Users are told in the post-cut-over notice that old chatbot conversations are not carried over |
| `testimonials` / `reviews` | `web.testimonials` in state `UNVERIFIED` — never published until consent and verified-purchase evidence exist (NN-49); any testimonial about an advocate is dropped (NN-21) | R5 found adapted/fabricated-looking testimonials in the manuals — these are not migrated |
| `coins` / wallet / referral balances | Disposition by owner: honour as account credit through OH8 or refund; never silently dropped [OWNER] | Consumer-protection exposure if dropped (NN-50) |
| analytics, sessions, OTP logs, tokens | Not migrated | Deleted with the cluster after archive |

**FR-P00-68 — Users without verified contacts.** A migrated person whose email and mobile are both unverified receives no marketing; at first sign-in by OTP to a migrated contact point the P01 flow verifies it and links the migrated PERSONAL tenant. Persons who never sign in within 24 months of cut-over are notified twice (at 12 and 23 months) and then erased, except order and invoice records kept for the statutory period under the tenant's legal-hold-aware retention [REC; COUNSEL].

**FR-P00-69 — Orders, payments and money reconciliation.** Reconciliation per run: counts by collection and target; order counts and sums by month × status × product; payment sums by month × gateway status against **PayU settlement reports** (not only the legacy database); refunds by month; orphans (payments without orders, orders marked PAID without a payment); currency and rounding deltas (must be zero). The final run cannot be promoted if any money delta is non-zero or unexplained (`core.migration.money_tolerance` = 0.00, LOCKED).

**FR-P00-70 — Dry runs.** Three rehearsals in `mig` before cut-over: R1 (full extract, all transforms, reconciliation, sample review), R2 (after fixes; timed end-to-end to size the cut-over window; Keycloak import and first-login test with five staff volunteers on their own legacy accounts with consent), R3 (dress rehearsal on a fresh restore with the exact runbook and the final delta procedure). Promotion of R3 into prod is not allowed — the final run repeats R3 on the cut-over snapshot.

**FR-P00-71 — Personal-data dispositions and notices.** Before R1 the owner and `PLT_DPO` approve, per personal-data collection: purpose in the new system, lawful basis (existing contract, consent record, legal obligation), retention, and the notice to be sent. The **migration notice** (email + SMS within DLT templates, NN-34) tells existing customers: the new platform and operating entity (if different, this is a change of fiduciary — counsel to confirm whether consent or notice suffices [COUNSEL]), where their data now lives (India), what was carried over, what was not (chatbot logs), how to sign in, and how to object or request erasure. SPDI Rules 2011 continue to apply until 13 May 2027 (R3 LG-075) — passwords are SPDI, so their handling follows FR-P00-67.

**FR-P00-72 — Migration console** (SCR-P00-06): runs, reconciliation reports, defect lists with assign-to, side-by-side sample review (legacy JSON vs new record), money reconciliation view, promote/roll back with maker-checker (`PLT_SUPER_ADMIN` maker, `PLT_DPO` or `PLT_SECURITY_OFFICER` checker).

**FR-P00-73 — Genesis events.** Because the legacy app had no tamper-evident ledger, each migrated tenant chain starts with a `core.migration.genesis` event summarising imported history (counts, source hash, run ID) and stating "history before <cut-over date> imported from the previous LawDocs system; integrity assured from migration". Original legacy timestamps are preserved in `occurred_at` of history rows, never in `recorded_at`.

**FR-P00-74 — Mobile and partner sessions.** If the legacy system issued long-lived tokens to any app or partner, they are revoked at cut-over; partners are given new credentials only through P19.

### 4O. SEO-safe cut-over (R5 §1, §7.4; NN-31)

**FR-P00-75 — Redirect map as data.** `web.redirects` (`id`, `source_host`, `source_path` (exact or pattern), `target_url`, `status` ∈ {301, 308, 410}, `reason` (`HOST_CANONICAL`, `SLUG_CHANGE`, `SECTION_MOVE`, `THIN_MERGE`, `DUPLICATE`, `RETIRED`), `source_list` (`SITEMAP_2026_07`, `SEARCH_CONSOLE`, `BACKLINK`, `MANUAL`), `clicks_16m`, `impressions_16m`, `owner`, `approved_by`, `effective_from`, `expires_at` NULL = permanent) seeded from `tools/seo/build-redirect-map.ts`, which joins the 186 sitemap URLs, Search Console pages with impressions, top backlink targets and the R5 group table. The map is versioned; changes after freeze need maker-checker (`OPS_CONTENT_PUBLISHER` maker, `PLT_CONTENT_EDITOR` checker). Redirects are served at the edge (CloudFront function or Next.js middleware with a compiled map) in one hop.

**FR-P00-76 — Host canonicalisation.** `http://lawdocs.in/*`, `https://lawdocs.in/*` and `http://www.lawdocs.in/*` → `https://www.lawdocs.in/*` with path and query preserved, one hop, status 301. This fixes the R5 finding that deep non-www URLs fail. Canonical tags, sitemaps, hreflang and JSON-LD `url` values all use `https://www.lawdocs.in`.

**FR-P00-77 — Rules by URL group** (186 sitemap URLs; R5 §1.2):

| Group | # | Rule |
|---|---|---|
| Core pages (`/`, about, team, career, contact, partnership, registration, legal, retainers, schedule-meeting, talk-to-lawyer, documentation-drafting, startup-services, compliance-services) | 14 | Keep path where the new IA keeps the page; `/legal` and `/talk-to-lawyer` 301 to the consult/advisory hub chosen by P21 (overlap with `/compliance-services/consult-lawyer`) |
| `/advisory/*` | 6 | Keep and expand (P21) |
| `/buy/*` | 20 | 301 each to the matching indexable document or service hub (e.g., `/buy/rent` → `/documents/property-transactions/rent`). The new purchase/checkout flow lives at non-indexable paths (`/checkout/*`) served with `noindex` and excluded from sitemaps. **Remove `Disallow: /buy/`** from robots at cut-over so crawlers can fetch the old URLs and see the 301s; a robots-blocked URL cannot pass its redirect to search engines [INTERP of search-engine behaviour; REC] |
| `/smartdrafts/*` | 19 | 301 each to `/documents/...` (R5) |
| `/compliance-services/agreements-contracts-drafting/*` | 7 | 301 to the matching document or service page; canonical to the document page |
| `/compliance-services/audit/*` (sentence-slugs) | 6 | 301 to `/compliance/audit/{service}` (P21 FR-P21-53 governs) |
| `/compliance-services/business-legal-consultation/*`, `personal-…/*`, `property-…/*` | 21 | Parent pages kept; the 18 feature-bullet URLs 301 to their parent (or 410 if they have zero clicks and zero backlinks in 16 months) |
| `/compliance-services/business-registration/*` | 17 | 301 to `/start-a-business/...` pages; trailing-hyphen slugs normalised |
| `/compliance-services/consult-lawyer/*` (city pages) | 7 | 301 to `/marketplace/legal-consultation` (P21 FR-P21-53); a city page returns only if P21 publishes genuinely local content (avoid doorway pages) |
| `/compliance-services/irdai_*`, `rbi*`, `sebi_*`, `other_registration`, `reporting`, `roc` | 50 | Keep the content; underscore slugs 301 to hyphenated slugs under `/regulated-entities/{regulator}/{service}`, except `roc/*` → `/compliance/roc-compliances/*` (P21 FR-P21-53 governs) |
| `/compliance-services/property-real-estate-documents/*` | 7 | 301 to the Documents property pages |
| `/resources/*`, `/blogs` | 4 | Keep hubs; blog posts keep slugs where possible |
| `/terms/*`, `/privacy-policy` | 3 | `/terms/Disclaimer` → `/legal/disclaimer` (lowercase); new pages added: Terms of Use, Privacy Notice (DPDP), Grievance Officer, Cookie, Refund (R5) |
| Legacy indexed URLs outside the sitemap (`/mortgage/`, `/services/consult-lawyer`, others from Search Console) | n | 301 to the nearest equivalent |

Each row in the map is checked against the P21 page inventory: the target must exist, return 200, be indexable and self-canonical. The counts above come from R5; `08-seo-assets.md` is authoritative if it differs.

**FR-P00-78 — robots.txt and sitemaps.** `robots.txt` generated from a template with settings: `Allow: /`; disallow only private and transactional paths (`/checkout/`, `/payment/`, `/account/`, `/api/`, preview routes); no `Disallow` on any path that has redirects; `Sitemap: https://www.lawdocs.in/sitemap.xml`. AI-crawler policy is a setting (P21-owned `web.crawl.ai_search_bots_allowed`, `web.crawl.ai_training_bots_allowed`, `web.crawl.google_extended_allowed`; P21 FR-P21-51; NN-31; R5 §7.4 item 7): search-retrieval bots allowed, training bots per owner decision [OWNER]. `/sitemap.xml` is a sitemap index with child sitemaps per section; every URL is www, indexable, self-canonical and carries a real `lastmod` from the CMS publish time. `/lawdocs-sitemap.xml` 301s to `/sitemap.xml`. The legacy admin and payment paths (`/addblogs`, `/edit-blog/`, `/payment-success`, `/payment-fail`) return 410 after cut-over.

**FR-P00-79 — Rendering gate.** Every indexable route on `apps/public` must return, to a fetch with JavaScript disabled, a unique `<title>`, meta description, a single H1, body copy, navigation links and JSON-LD where valid (R5 §1.1 found none of these). `tools/seo/no-js-crawl.ts` crawls the full sitemap in CI against a preview deployment and fails on any duplicate title, missing H1, empty body, `noindex` on an indexable page, non-200 status, canonical mismatch or a link to a redirecting URL.

**FR-P00-80 — `seo:check` CI job.** Runs on every PR touching `apps/public` or `web.redirects`: redirect map lint (no chains, no loops, every source unique, every target 200 + indexable), robots/sitemap consistency (no sitemap URL disallowed by robots — the R5 conflict cannot recur), title/H1 uniqueness, hreflang reciprocity, structured-data validation, and the no-JS crawl on changed routes.

**FR-P00-81 — Cut-over measurement.** Baseline 28 days before cut-over: Search Console clicks, impressions, indexed pages, 404 counts; server logs of crawler hits. After cut-over: submit the new sitemap index; monitor daily for 28 days (404s, soft 404s, redirect errors, coverage); a 404 for any URL with impressions is fixed within 1 working day by adding a map row. Redirects are permanent by default (`expires_at` NULL) [REC].

**FR-P00-82 — Brand and academy leakage.** trainings.lawdocs.in remains on Graphy (D-16); P00 records the R5 brand-leakage findings (wPractical links, lorem ipsum) in the disposition register for the owner to fix on Graphy — they are outside the LawDocs codebase.

### 4P. Decommissioning Railway, MongoDB Atlas, the legacy AI key and PayU

**FR-P00-83 — Order of shutdown.** (1) Cut-over complete and legacy cut-over hypercare passed (48 hours, §5.5; distinct from the P23 wave hypercare, FR-P23-54). (2) Legacy app read-only behind a maintenance page for 14 days (orders blocked; static notice with the new sign-in link). (3) Final Atlas snapshot exported, encrypted with a KMS key in `ld-backup`, stored in ap-south-1 under Object Lock governance mode for 8 years (order and invoice evidence; Companies Act 2013 s.128(5) books of account eight years and GST record-keeping [VERIFY CGST s.36 period] — R3 LG-128), with SHA-256 and a restore test proving readability. (4) Railway services stopped, then deleted; volumes deleted; environment variables removed. (5) Atlas cluster deleted after the archive restore test passes and the owner signs; Atlas backups and snapshots deleted; organisation API keys revoked. (6) Legacy Anthropic API key revoked; spend alerts removed. (7) PayU: callbacks disabled at cut-over; account kept only for refunds and chargebacks until the window closes [VERIFY PayU dispute window in the merchant agreement], then settlement reconciliation evidence captured and the merchant account closed. (8) DNS records pointing to Railway removed. (9) A **decommissioning certificate** per system (what was deleted, when, by whom, evidence of archive and restore test) is filed in `docs/runbooks/decommission/` and recorded as a platform ledger event.

**FR-P00-84 — Secrets rotation.** Every secret listed in `06-integrations.md` is rotated or revoked; nothing from the legacy estate is reused in the new estate.

**FR-P00-85 — Region evidence.** If Railway or Atlas hosted data outside India [VERIFY regions], the processing is recorded in the transfer register with dates; deletion evidence closes the record (NN-25).

**FR-P00-86 — Legacy repository archive.** After step 9, `lawdocs-legacy` is archived read-only and kept for 8 years; its secrets-scan report is attached.

### 4Q. Export-map registry (NN-11; foundation for P20)

**FR-P00-87 — `xpt.export_map`.** For every tenant record type, `db/export-map/<schema>.<table>.yaml` declares: record type code, the `LD-EXPORT-1.0` folder path template (Appendix K; e.g., `10 Billing and Invoices/<FY>/` for company tenants, `10 Receipts and Invoices/<Year>/` for individuals), file-name pattern using business references and human names, format (XLSX/CSV/JSON/DOCX/PDF/PDF-A/original), human-readable column headings, data-class handling (restricted folders for `HR` and `LEGAL_PRIVILEGED`; `CREDENTIAL` never exported — metadata only; Aadhaar never present), and the join path that resolves IDs to readable names. `NN-11_export_map_complete` fails CI if a table with `tenant_id` lacks an entry, an entry references a dropped column, or a folder path is derived from anything other than canonical IDs and versioned profile rules (NN-12). Because folder paths are views over canonical IDs, a code, schema, storage-vendor or region change never re-files customer data.

**FR-P00-88 — P00 entries.** Register: `core.legal_entities` → `01 Company Profile/` or `01 My Profile and IDs (masked)/`; `core.correction_entries` → `99 System Data (CSV and JSON)/Corrections_Register.xlsx`; `core.audit_events` (tenant chain) → `99 System Data (CSV and JSON)/Audit Trail/` + anchors + `ld-verify` README; `core.access_log` (tenant) → `99 System Data (CSV and JSON)/Access Log.csv`; `bil.order_mirror`, `bil.payment_mirror` and archived invoices → `10 Billing and Invoices/<FY>/` (company) or `10 Receipts and Invoices/<Year>/` (individual); migrated `dms` documents → the type-mapped folder or `08 Agreements/Imported from old LawDocs/`; `core.migration_lineage` (tenant rows only) → `99 System Data (CSV and JSON)/Migration Lineage.csv`.

### 4R. ADR set and `docs/` structure

**FR-P00-89 — ADRs written in P00** (`docs/adr/`, MADR format: context, options, decision, consequences, review date):

| ADR | Subject |
|---|---|
| 0001 | Modular monolith (NestJS 11) + Next.js 16 apps + Expo; pinned versions |
| 0002 | PostgreSQL major version, extensions, RLS as the tenant wall |
| 0003 | Keycloak realms `ld` and `ld-staff` (detailed in P01) |
| 0004 | Drizzle vs Kysely |
| 0005 | Cerbos for RBAC + ABAC (P01/P02; Appendix D) |
| 0006 | Temporal (self-hosted ap-south-1) for long-running workflows; BullMQ for short jobs |
| 0007 | Hosting: AWS ap-south-1 + ap-south-2 DR; Supabase non-prod DB only; no Railway |
| 0008 | OpenTofu or Terraform; account topology and SCPs |
| 0009 | Connection pooling and transaction-local session context |
| 0010 | Audit ledger: hash chain, anchors, Correction Entries |
| 0011 | IDs (prefixed ULID, UUIDv7 events) and business reference IDs |
| 0012 | Feature-flag service and kill-switch registry |
| 0013 | Event families, outbox, inbox; `int` as sole ecosystem publisher |
| 0014 | Object storage, Object Lock and retention floors |
| 0015 | Search: OpenSearch with PostgreSQL FTS fallback; pgvector tenancy |
| 0016 | Domains, DNS, canonical host and brand domains |
| 0017 | Sealed database and data-class catalogue; field-level encryption |
| 0018 | Legacy migration strategy, dispositions and cut-over |
| 0019 | SEO cut-over: redirect map as data, robots/sitemap rules |
| 0020 | Export contract `LD-EXPORT-1.0` as a schema-change gate |
| 0021 | AI gateway stub and provider routing by data class (D-14; NN-15) |
| 0022 | Ecosystem contracts import, `PROPOSED` subjects and Appendix Y |
| 0023 | Observability backend with India residency |
| 0024 | Document stack (docxtemplater, Gotenberg, PDF/A) and the optional WOPI licence question |

**FR-P00-90 — `docs/` structure.**

```
docs/
├─ adr/                      ADR-0001…
├─ discovery/                01…11 (FR-P00-02)
├─ ecosystem/                integration spec (unchanged) + CHECKSUMS; OH reference; Appendix Y drafts
├─ phases/                   Pxx-plan.md written before each phase; Pxx-exit.md at the gate
├─ architecture/             context, container and module diagrams; data-flow per module
├─ data/                     data-catalogue.md (generated), export-map.md (generated), retention-schedule.md
├─ security/                 threat-model-<module>.md, ASVS mapping, pen-test reports index (Appendix P)
├─ privacy/                  ROPA, notices index, consent purposes, DPIAs, transfer register, sub-processors
├─ compliance/               verification-log.md (NN-38), claims-register.md (link to OH14), rules register index
├─ seo/                      redirect-map.csv (generated), crawl reports, Search Console baselines
├─ runbooks/                 cutover.md, decommission/, incident.md, restore.md, break-glass.md, key-rotation.md
├─ api/                      generated OpenAPI/AsyncAPI renderings
└─ help-keys/                generated register of hlp.* keys
```

`docs/data/*`, `docs/seo/redirect-map.csv` and `docs/help-keys/*` are generated in CI and fail the build if stale.

---

## 5. Workflows and state machines

### 5.1 Correction Entry

| State | Entry | Allowed transitions | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| DRAFT | Create | SUBMITTED, WITHDRAWN | Requester | — | — |
| SUBMITTED | Submit | APPROVED, REJECTED, WITHDRAWN | Checker | Checker ≠ requester (person-level, across realms); step-up AAL3 for platform corrections; justification ≥ 50 chars; documents present when reason requires | `in.lawdocs.core.CorrectionSubmitted.v1`; escalation after 3 working days |
| APPROVED | Approve | CLIENT_APPROVAL_PENDING (if `tenant_ack_mode = PRIOR` or a crucial detail), else APPLIED | System | — | Tenant owner/admin task; reminders 24/72 h |
| CLIENT_APPROVAL_PENDING | Request client acknowledgement | APPLIED | Tenant owner/admin; system on timeout | Tenant owner/admin acknowledgement with step-up, or 5 working days elapsed and the platform checker re-confirms (tenant notified that it proceeded; objection attached) | — |
| APPLIED | Apply | REVERSED (by a new entry) | System | Target not under legal hold for `DOCUMENT_VERSION` | Target new version + history row + ledger event with `correction_id` in one transaction; `…CorrectionApplied.v1`; tenant notification |
| REJECTED / WITHDRAWN | — | — | — | — | Ledger event |

### 5.2 Tenant provisioning (system part; journeys in P01)

`REQUESTED → RECORDS_CREATED (tenant, legal entity, chain genesis, default folders view) → KEYS_READY (data keys; dedicated CMK if set) → STORAGE_PREFIXES_READY → SEARCH_ALIAS_READY → SETTINGS_DEFAULTED (brand + plan + workspace-type packs, P03) → READY` (status `TRIAL`, `ACTIVE` or `PENDING_CONFIRMATION` for partner/OH-originated tenants). `TenantProvisionWorkflow` (Temporal) with compensation per step; idempotent on `(created_via, external_request_id)` or `tenant_id`; emits `in.lawdocs.core.TenantProvisioned.v1`; for OH-originated requests, `int` acknowledges with `PUT /v1/provisioning-requests/{id}` (Ecosystem Spec §6.29; LawDocs as a listed product is an Appendix Y item).

### 5.3 Migration run

| State | Guard to leave | Notes |
|---|---|---|
| PLANNED | Disposition register signed; DPO approval for personal-data collections | Run config pinned (`transform_version`) |
| SNAPSHOT_TAKEN | Atlas PITR restore ID and snapshot hash recorded | Never the live cluster |
| EXTRACTED | Extract counts recorded per collection | Raw extract encrypted in `mig_stage` |
| TRANSFORMED | All transforms passed unit/golden tests | DQ flags assigned |
| LOADED | Loaded into staging schemas | No write to live schemas |
| RECONCILED | Report generated: counts, money sums, orphans, null-rate deltas, source-set hash | Money delta must be 0.00 |
| REVIEWED | Sample review complete; defect rate ≤ `core.migration.max_defect_rate` | Maker-checker |
| PROMOTED | Owner go/no-go recorded | One transaction per entity batch; `…core.MigrationRunPromoted.v1` |
| ROLLED_BACK | — | Staging dropped; evidence retained |

### 5.4 Asset disposition

`DISCOVERED → DISPOSITION_PROPOSED → APPROVED (owner; DPO for personal data) → {MIGRATED | REBUILT (target phase) | ARCHIVED (archive verified by restore test) | RETIRED} → SOURCE_DELETED (only after MIGRATED/ARCHIVED evidence) → CERTIFIED (decommissioning certificate)`. A source cannot move to `SOURCE_DELETED` without the evidence link; the transition is a platform ledger event.

### 5.5 Cut-over runbook (summary; full text `docs/runbooks/cutover.md`)

| When | Step |
|---|---|
| T−28 d | SEO baseline captured; redirect map v1 built; P21 core pages for all redirect targets exist on staging |
| T−14 d | R3 dress rehearsal; parallel run of the new site on a preview host (noindex, basic auth) with crawler tests; migration notice drafted and approved |
| T−10 d | Redirect map frozen (changes need maker-checker and a fresh `seo:check`) |
| T−3 d | Go/no-go rehearsal on a fresh restore; DNS TTL lowered to 300 s |
| T−1 d | Users notified (email + SMS + legacy-site banner) of a 2-hour window |
| T0 | Legacy set read-only (maintenance banner, orders blocked); final snapshot; final migration run; reconciliation; owner go/no-go; DNS switch; edge redirects live; robots and sitemap live; smoke tests by persona (sign-in by OTP, find migrated order, open migrated document, visit 50 sampled old URLs) |
| T+0 h | Submit sitemap index in Search Console and Bing Webmaster; IndexNow ping |
| T+48 h | Hypercare ends if no P1 open; daily SEO monitoring continues to T+28 d |
| T+14 d | Legacy read-only period ends; decommissioning sequence (FR-P00-83) starts |

**Rollback criteria:** any money reconciliation mismatch; failure of ≥ 1% of sampled redirects; P1 defect without fix in 4 hours. Rollback = DNS back to Railway, legacy read-write, new prod set read-only, incident report; the migration can be re-run because it is idempotent.

### 5.6 Feature flag with verification gate

State machine: Appendix A §A.17 governs (Resolution R-A-09); P03 §5.5 owns the kill-switch machine.

`OFF → ON_PENDING_APPROVAL (verification row VERIFIED + approver evidence) → ON` (maker-checker); `ON → OFF` immediate by authorised roles, audited (`cfg.FlagChanged`). Kill switches follow `RELEASED → ENGAGED → RELEASE_REQUESTED → RELEASED` (release by a second person; NN-39).

---

## 6. Screens and UX

P00 screens are platform-internal except SCR-P00-08 and SCR-P00-09; all meet WCAG 2.2 AA (NN-28) and use `packages/ui`.

| ID | App / path | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P00-01 | console › Home | Platform health | Environment, build, flag count, kill switches ON, outbox lag, DLQ size, last chain verification, last anchor, migration status, SEO cut-over status | "No incidents" | Read-only responsive | Live regions announce status changes politely |
| SCR-P00-02 | console › Tenants | Tenant list and detail (provisioning only in P00) | Kind, brand, operating entity, status history, legal entities, keys (ARN masked) | Neutral 404 for unknown IDs | — | Table with keyboard navigation |
| SCR-P00-03 | console › Platform › Flags & kill switches | Manage flags | Verification gate badge, approver, evidence, expiry; kill-switch toggle with reason | Gated flag shows "Blocked: verification row VL-xxx OPEN" | — | Toggle has text state, not colour only |
| SCR-P00-04 | console › Audit › Platform chain | Explore and verify | Filters (actor, action, aggregate, business ref, date); verify range; export with BSA s.63(4) certificate draft (NN-10, built fully in P08/P20) | — | — | — |
| SCR-P00-05 | console › Audit › Corrections | Create and approve Correction Entries | Wizard: scope → target → current value and history → new value → effective date → reason, justification, documents → preview of tenant view → submit; typed confirmation for `MASTER_DATA` and `DOCUMENT_VERSION` | Self-approval button absent; explanation shown | — | Each step is a heading; error summary at top |
| SCR-P00-06 | console › Platform › Migration | Migration console | Runs, reconciliation (counts, money), defects, sample review side-by-side, promote/rollback | — | — | Diff view has text equivalents |
| SCR-P00-07 | console › Platform › Events | Outbox and integration health | Lag per subject, DLQ with replay (reason required) | — | — | — |
| SCR-P00-08 | my.lawdocs.in › Settings › Audit & history › Changes made by LawDocs | Tenant view of platform corrections | Date, scope, target, old/new (per class), reason, approvers, documents, acknowledge, object | "LawDocs has not corrected any of your records. If we ever do, it will appear here with the reason and who approved it." | Card list | Plain-language labels; `hlp.core.correction_entry` |
| SCR-P00-09 | my.lawdocs.in › Settings › Audit & history › Integrity | Tenant chain verification | Last verification, anchors download, "Verify my history", link to `ld-verify` | — | Card | `hlp.core.audit_anchor` |
| SCR-P00-10 | console › Website › Redirects | Redirect map | Source, target, status, reason, clicks, approval; bulk CSV import with preview; live tester ("enter an old URL") | Conflict and chain warnings inline | — | — |
| SCR-P00-11 | console › Platform › Disposition register | Asset dispositions | Rows by system, personal-data class, disposition, evidence link, certificate | — | — | — |

**Click budgets.** Tenant owner from home to "Changes made by LawDocs": ≤ 3 clicks (Settings → Audit & history → tab). Super admin from console home to start a Correction Entry on a tenant field: ≤ 4 clicks.

**Help keys registered in P00:** `hlp.core.correction_entry`, `hlp.core.audit_ledger`, `hlp.core.audit_anchor`, `hlp.core.business_reference`, `hlp.core.legal_hold`, `hlp.core.original_vs_derived`, `hlp.core.data_residency`, `hlp.core.migrated_record`.

---

## 7. Backend design

### 7.1 Modules

`core` (owner of everything in this phase); `cfg` (registry heads); `dms` (ingest skeleton, hashes); `web` (redirects table, robots/sitemap generator contract); `xpt` (export-map registry); `bil` (order/payment mirrors for migration); `eng` (decommissioning certificates, backup evidence); stubs for all others (FR-P00-11).

### 7.2 Tables

| Table | Key columns | Indexes | RLS | Retention class |
|---|---|---|---|---|
| `core.tenants` | id, kind, brand_code, operating_entity_id, status, year_basis | slug unique | Platform-scoped (console via `ld_platform`) + tenant self-row | Life of tenant + 8 y |
| `core.brands`, `core.operating_entities` | code; legal identifiers, officers | code unique | Global reference (exempt) | Permanent |
| `core.legal_entities` | id, tenant_id, constitution, ids (enc/bidx/masked), valid_period | (tenant_id), pan_bidx | Tenant | Life + 8 y |
| `core.tenant_domains` | host, tenant_id, verified_at | host unique | Platform | Life |
| `core.data_classes`, `core.id_prefixes` | code | — | Exempt | Permanent |
| `cfg.flags`, `cfg.kill_switches`, `cfg.kill_switch_events` (heads only; owned by P03 §7.2) | key/code, scope, state, approver | key unique | Platform | 7 y (events) |
| `core.sequences`, `core.business_refs`, `core.ref_aliases` | family, year, n; alias_type, alias_value | (family, year) unique; alias unique | Tenant (refs), platform (series) | Permanent |
| `core.idempotency_keys` | tenant_id, key, route, request_hash | PK | Tenant | 24 h |
| `core.side_effects` | port, provider, ext_ref, status | (port, ext_ref) | Tenant | 8 y |
| `core.outbox`, `core.inbox` | CloudEvents columns | (subject, seq) | Tenant | ≥ 90 d |
| `core.audit_events` (partitioned) | chain_id, seq, event_id, … | (chain_id, seq) unique; GIN business_refs | Tenant chain via RLS; platform chains platform-only | ≥ 8 y, Object Lock export |
| `core.audit_anchors` | chain_id, date, merkle_root, signature | (chain_id, date) | As ledger | ≥ 8 y |
| `core.correction_entries`, `core.correction_acknowledgements` | per FR-P00-37 | (tenant_id, state) | Tenant + platform | ≥ 8 y |
| `core.access_log`, `core.break_glass_events` | actor, purpose, object | (tenant_id, at) | Tenant | ≥ 8 y |
| `core.migration_runs`, `core.migration_lineage`, `core.backfill_runs` | run_id, source refs, hashes | lineage (source_collection, source_id) unique | Tenant rows tenant-scoped | 8 y |
| `cfg.setting_definitions`, `cfg.setting_values` (heads; owned by P03) | key, tier; scope, value, valid_period | key unique | Registry exempt; values by scope | Permanent / bitemporal |
| `dms.upload_intents`, `dms.document_hashes` | tenant_id, sha256, prev_hash | (tenant_id, sha256) | Tenant | Life + 8 y |
| `web.redirects` | source_host, source_path, target_url, status | (source_host, source_path) unique | Platform/brand | Permanent |
| `xpt.export_map` | record_type, folder_template, format, version | record_type unique per version | Exempt (loaded from YAML) | Permanent |
| `bil.order_mirror`, `bil.payment_mirror` | business_ref, oh8_ref, amounts, status, aliases | (tenant_id, business_ref) | Tenant | 8 y |
| `eng.disposition_register`, `eng.decommission_certificates` | asset, disposition, evidence | — | Platform | 8 y |

### 7.3 APIs (REST `/v1`, OpenAPI 3.1; every mutating call requires `Idempotency-Key`)

| Method and path | Purpose | Scope / roles | Idempotent |
|---|---|---|---|
| `GET /healthz`, `GET /readyz`, `GET /v1/platform/version` | Health, build | public / internal / authenticated | — |
| `POST /v1/platform/tenants` | Provision (used by P01, partner API, console) | system, `PLT_SUPER_ADMIN` | Yes |
| `GET /v1/platform/tenants/{id}` | Tenant detail | `PLT_*` | — |
| `GET /v1/audit/events` | Query tenant or platform chain (cursor) | tenant owner/admin, auditors, `PLT_AUDITOR_RO` | — |
| `POST /v1/audit/verify`, `GET /v1/audit/anchors` | Verify range; anchors | same | Yes |
| `POST /v1/corrections`; `POST /v1/corrections/{id}:submit` `:approve` `:reject` `:withdraw` `:apply` `:acknowledge` `:object` | Correction lifecycle | per Appendix D | Yes |
| `GET /v1/corrections` | Register | tenant owner/admin, auditors, `PLT_*` | — |
| `POST /v1/uploads/intents` | Presigned upload | authenticated | Yes |
| `GET /v1/flags`, `PATCH /v1/flags/{key}` | Flags | `PLT_SUPER_ADMIN` + approver | Yes |
| `POST /v1/kill-switches/{code}:engage` / `:request-release` / `:release` (P03 §7.3 API; P00 ships the first version) | Kill switch | authorised roles per registry; release by a second person | Yes |
| `POST /v1/migration/runs`; `GET …/{id}`; `:promote`; `:rollback` | Migration | `PLT_SUPER_ADMIN` maker; `PLT_DPO`/`PLT_SECURITY_OFFICER` checker | Yes |
| `GET /v1/web/redirects`; `PUT /v1/web/redirects:bulk` | Redirect map | `OPS_CONTENT_PUBLISHER` maker, `PLT_CONTENT_EDITOR` checker | Yes |
| `GET /r/{businessRef}` | Universal resolver | authenticated | — |
| `GET /v1/events?after=…` | Internal catch-up feed | service | — |

### 7.4 Domain events (internal family)

`in.lawdocs.core.TenantProvisioned.v1`, `…core.TenantStatusChanged.v1`, `…core.LegalEntityRegistered.v1`, `…core.LegalEntityAmended.v1`, `…core.CorrectionSubmitted.v1`, `…core.CorrectionApplied.v1`, `…core.CorrectionReversed.v1`, `…core.AuditAnchorPublished.v1`, `…core.AuditChainBroken.v1`, `…core.BreakGlassStarted.v1`, `…core.BreakGlassEnded.v1`, `…cfg.FlagChanged.v1`, `…cfg.KillSwitchEngaged.v1`, `…cfg.KillSwitchReleased.v1` (canonical `cfg` events owned by P03; R-A-09 retires `core.FeatureFlagChanged` and `core.KillSwitchChanged`), `…core.MigrationRunPromoted.v1`, `…core.LegacySystemDecommissioned.v1`, `…dms.DocumentIngested.v1`, `…dms.DocumentRejected.v1`, `…web.RedirectMapPublished.v1`.

### 7.5 Jobs and workflows (Temporal unless noted)

`TenantProvisionWorkflow`; `AuditChainVerifyWorkflow` (daily 02:15 IST; weekly full); `AuditAnchorWorkflow` (00:10 IST); `IngestWorkflow`; `OutboxRelay` (continuous service); `InboxGapRepair` (15 min); `PartitionMaintenance` (daily); `CorrectionEscalation` (hourly); `MigrationRunWorkflow`; `MigrationDeltaWorkflow` (cut-over); `RedirectMapBuild` (on demand; nightly in the 28 days post cut-over with a 404 report); `SeoNoJsCrawl` (CI and nightly); `BackupRestoreTest` (weekly); `DriftDetection` (nightly, IaC); `FlagExpiryReminder` (daily); `KillSwitchProbeJob` (P03 job; P00 runs it every 5 min until P03 exits).

### 7.6 Error codes introduced

`LD-CORE-001` ledger is append-only · `LD-CORE-002` missing tenant context · `LD-CORE-003` cross-tenant reference rejected · `LD-CORE-010` correction requester cannot approve · `LD-CORE-011` justification too short · `LD-CORE-012` supporting document required · `LD-CORE-013` target under legal hold · `LD-CORE-014` live provider call from non-production · `LD-CORE-015` unregistered setting key · `LD-CORE-016` flag blocked by open verification · `LD-CORE-017` kill switch engaged · `LD-CORE-020` idempotency key reuse · `LD-CORE-030` business reference not found · `LD-CORE-031` invalid business reference format · `LD-CORE-040` migration reconciliation failed · `LD-CORE-041` money delta not zero · `LD-CORE-042` disposition evidence missing · `LD-DMS-002` malware detected · `LD-DMS-032` checksum mismatch · `LD-DMS-001` file type not allowed (DMS codes owned by P04; renumbered by Appendix B §B.5 to remove a collision with P04 `003` quota and `004` encrypted file). Each has a user message key and a help key. Redirect-map and robots/sitemap validation errors use P21's `LD-WEB-*` range (e.g., `LD-WEB-005` redirect chain or loop); P00 registers no `LD-WEB` codes.

---

## 8. Integrations

| Port | P00 adapter(s) | Failure behaviour / manual fallback |
|---|---|---|
| `KMS_PORT` | AWS KMS; local emulator | Fail closed (no decrypt, no write of encrypted columns) |
| `OBJECT_STORE_PORT` | S3 with Object Lock; MinIO (local) | Uploads retried; ingest parks in quarantine |
| `MAIL_PORT` | Amazon SES ap-south-1 (prod); Mailpit (local) | Queue and retry; migration notices resent |
| `SMS_PORT` | DLT-registered CPaaS adapter (JioCX or other, P01 selects) — migration notice only in P00 | Email only if SMS fails |
| `FLAG_PORT` | Unleash or ADR-0012 choice | Last known values cached; kill switches default to safe state |
| `AV_PORT` | ClamAV | Uploads held in quarantine until scanned |
| `TSA_PORT` | RFC 3161 TSA (flag OFF) | Anchors signed without TSA |
| `LEGACY_PORT` | MongoDB read-only on PITR restore | Migration only; removed after decommissioning |
| `BILLING_PORT` | Fake OH8 in non-prod; OH8 historical import interface (OH4) in mig | Orders held in `bil.order_mirror` with `oh8_ref` pending |
| `CRM_PORT` | OH3 import for legacy leads (business-contact fields only) | Leads stay in an encrypted staging table ≤ 30 days, then deleted if not imported |
| `ECOSYSTEM_PORT` | Recorder stub (P19 implements) | Events stored with status `NOT_SENT` |
| `SEARCH_CONSOLE_PORT` | Google Search Console API (read) for the SEO baseline [VERIFY scopes] | CSV export upload |
| `AI_PORT` | Gateway stub; no model calls in P00 | — |

---

## 9. Settings and configuration (registered in Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `core.audit.retention_years` | PLATFORM (tenant may lengthen) | int | 8 | `PLT_SUPER_ADMIN`; tenant owner may increase | Y |
| `core.audit.anchor_time_ist` | PLATFORM | time | 00:10 | locked | — |
| `core.audit.anchor_tsa.enabled` | PLATFORM | bool | false | `PLT_SECURITY_OFFICER` | Y |
| `core.correction.tenant_ack_mode` | PLATFORM | enum PRIOR/POST | PRIOR for MASTER_DATA, DOCUMENT_VERSION; POST otherwise | `PLT_SUPER_ADMIN` with tenant agreement | Y |
| `core.correction.justification_min_chars` | PLATFORM | int | 50 | locked | — |
| `core.correction.escalation_working_days` | TENANT | int (1–10) | 3 | tenant owner/admin | N |
| `core.break_glass.max_minutes` | PLATFORM | int (30–480) | 240 | `PLT_SECURITY_OFFICER` | Y |
| `core.break_glass.tenant_report_hours` | PLATFORM | int | 24 (max; NN-17) | locked | — |
| `core.tenant.timezone` | TENANT | IANA zone | Asia/Kolkata | tenant owner/admin | N |
| `core.tenant.year_basis` | TENANT | enum CALENDAR/INDIAN_FY | by workspace kind | tenant owner/admin | N |
| `core.tenant.number_format` | USER | enum indian/international | indian | user | N |
| `core.migration.max_defect_rate` | PLATFORM | decimal (0–0.02) | 0.005 | `PLT_SUPER_ADMIN` | Y |
| `core.migration.money_tolerance` | PLATFORM | decimal | 0.00 | locked | — |
| `core.migration.unverified_retention_months` | PLATFORM | int | 24 | `PLT_DPO` | Y |
| `core.provider_routing.nonprod` | PLATFORM | enum | sandbox | locked | — |
| `dms.upload.max_mb` | PLATFORM (tenants may lower) | int (1–500) | 100 | platform; tenant admin lower only | N |
| `dms.upload.allow_macro_office` | TENANT | bool | false | tenant admin (warning shown) | N |
| `dms.originals.retention_years` | TENANT | int ≥ 8 | 8 | tenant owner (increase only) | N |
| `eng.logs.retention_days_india` (**P23-owned**; P00 reads it; floor 180 LOCKED, 365 for personal-data logs — P23 §9) | PLATFORM | int | 400 | `PLT_SECURITY_OFFICER` | Y |
| `web.host.canonical` | BRAND | url | https://www.lawdocs.in | `PLT_SUPER_ADMIN` | Y |
| `web.crawl.ai_search_bots_allowed` (**P21-owned**; P00 reads it for the cut-over `robots.txt`; definition in P21 §9) | BRAND | bool | true | `PLT_SUPER_ADMIN` | Y (checker `PLT_SECURITY_OFFICER`) |
| `web.redirects.freeze_days_before_cutover` | PLATFORM | int | 10 | `PLT_SUPER_ADMIN` | N |
| `core.migration.ai_assist.enabled` | PLATFORM | bool (flag) | false | `PLT_SUPER_ADMIN` | Y (checker `PLT_DPO`) |
| `int.ecosystem.proposed_subjects.enabled` | PLATFORM | bool (flag) | false | `PLT_SUPER_ADMIN` after Appendix Y acceptance | Y |
| `cfg.kill_switch.propagation_seconds` (P03-owned; Appendix R §R.9.5) | PLATFORM | int | 60 | locked | — |

---

## 10. Security, privacy and audit

- **Implemented and tested here:** NN-01 (RLS + IDOR), NN-02 (ledger, corrections), NN-04 (no Aadhaar storage, masking hook), NN-09 (Object Lock originals), NN-11 (export map), NN-12 (expand-contract, canonical IDs), NN-15 (no legacy chat logs to AI), NN-19 (legacy leads only with consent status), NN-20 (claims inventory), NN-24/NN-47 (contracts import, `int`-only publishing, no kernel fork), NN-25 (region SCPs), NN-27 (NTP, India logs), NN-29 (registered settings), NN-31 (SSR, robots, private never indexable), NN-32 (log scrubber), NN-38 (verification-gated flags), NN-39 (kill switches), NN-45 (ledger in same transaction), NN-46 (idempotent side effects).
- **Threat model** (`docs/security/threat-model-core.md`, Appendix P §P.2 template): tenant breakout; ledger tampering by an insider DBA; super-admin abuse; object-store exposure; outbox poisoning; CI secret leakage; legacy-data exposure during migration (mitigated by `mig` isolation, prod-grade controls, encrypted staging, DPO approvals, deletion after promotion); SEO hijack via open redirects (redirect targets restricted to allow-listed hosts; no user-controlled redirect parameters).
- **Data classes:** every column tagged in `db/data-catalogue.yaml`; CI fails on an untagged column.
- **Secrets:** AWS Secrets Manager with rotation; gitleaks on every push; full-history scan of the legacy repository.
- **Privacy:** processing register entries for migration (purpose, data, recipients, retention, transfer from Railway/Atlas if outside India), migration notice, DPO sign-off of dispositions; legacy chatbot logs not migrated; legacy leads marketing-suppressed.
- **Audit events:** every correction, flag change, kill switch, migration promotion, redirect-map publication, decommissioning step and disposition approval.

---

## 11. AI touchpoints and guardrails

No AI in production in P00. The AI gateway stub (`packages/ai`) exists with routing by data class (Bedrock India for confidential classes; Anthropic API only for public/non-personal content; D-14, NN-15) and the kill switch, but no model is called. The migration console may offer AI-assisted mapping suggestions for legacy blog categories to the P21 taxonomy behind `core.migration.ai_assist.enabled` = OFF; only public blog content may be sent; suggestions are labelled and never auto-applied; no customer data is sent to any model in P00.

---

## 12. Acceptance criteria (`tests/acceptance/p00/*.feature`)

```gherkin
@P00-AT-01 @NN-01
Scenario: Cross-tenant read is denied on every table
  Given tenants "alpha" (COMPANY) and "ravi" (PERSONAL) seeded with generated rows for every tenant table
  When the application role queries every table in tenant context "alpha"
  Then no row of tenant "ravi" is returned
  And UPDATE and DELETE statements targeting "ravi" rows affect zero rows

@P00-AT-02 @NN-01
Scenario: IDOR attempt returns not found without leaking existence
  Given a user of tenant "alpha" is signed in
  When they request GET /v1/audit/events?aggregate_id=<an aggregate of "ravi">
  Then the response is 200 with an empty page
  And the body is identical to the response for a non-existent aggregate ID
  And GET /r/<a business reference of "ravi"> returns the same 404 "LD-CORE-030" as a non-existent reference

@P00-AT-03 @NN-02
Scenario: The ledger cannot be edited by any role
  Given an audit event exists in tenant "alpha"'s chain
  When the owner role runs UPDATE or DELETE on core.audit_events
  Then the statement fails with "LD-CORE-001"
  And the nightly chain verification still succeeds

@P00-AT-04 @NN-45
Scenario: Every mutating route writes a ledger event in the same transaction
  Given the route catalogue of apps/api
  When each mutating route is executed once on seeded data
  Then each execution produces exactly one ledger row with the same transaction ID as the business change

@P00-AT-05 @NN-02
Scenario: Super admin corrects a client's master data only with approval and visibility
  Given PLT_SUPER_ADMIN "Asha" drafts a MASTER_DATA correction of tenant "alpha"'s registered office with reason CLIENT_REQUEST and the client's letter attached
  When "Asha" tries to approve her own correction
  Then the approve action is unavailable and the API returns "LD-CORE-010"
  When PLT_SECURITY_OFFICER "Vikram" approves with step-up authentication
  And the tenant owner acknowledges
  Then the correction is APPLIED, the old value remains in history, the field shows a "Corrected" badge
  And the entry appears under Settings › Audit & history › Changes made by LawDocs for "alpha"

@P00-AT-06 @NN-09
Scenario: An original cannot be overwritten or deleted within retention
  Given a signed PDF stored as ORIGINAL with SHA-256 recorded
  When any role attempts to overwrite or delete the object
  Then the storage layer refuses the operation
  And a "replace" action creates a new version while the original stays locked

@P00-AT-07 @NN-04
Scenario: Aadhaar numbers never reach stored derived text
  Given an uploaded image whose OCR text contains a Verhoeff-valid 12-digit Aadhaar-pattern number generated at runtime (never stored in fixtures) whose last four digits are "<last4>"
  When derived text passes the beforeDerivedTextPersist hook
  Then the persisted text contains "XXXX XXXX <last4>" and not the number's first eight digits
  And the data catalogue contains no column tagged as an Aadhaar number

@P00-AT-08 @NN-32
Scenario: Logs contain no identifiers or secrets
  Given a corpus of emails, mobiles, PANs, Aadhaar patterns, OTPs, JWTs and card numbers injected into request bodies and errors
  When the telemetry pipeline exports logs and traces
  Then none of the corpus values appear in the exported data

@P00-AT-09 @NN-38
Scenario: A flag that depends on an unverified fact cannot be turned on
  Given flag "kyc.ovse.avc.enabled" linked to verification row "VL-0007" with status OPEN
  When PLT_SUPER_ADMIN tries to switch it ON in prod
  Then the change is refused with "LD-CORE-016"

@P00-AT-10 @NN-39
Scenario: Kill switch stops an adapter within 60 seconds
  Given the ESIGN adapter is active
  When an authorised user engages the "VENDOR_ADAPTER:ESIGN_AGGREGATOR_PRIMARY" kill switch with a reason
  Then within 60 seconds every worker refuses new calls to that adapter with "LD-CORE-017"
  And the change is in the platform ledger

@P00-AT-11 @NN-11
Scenario: A new tenant table without an export-map entry fails CI
  Given a migration that creates table "clm.obligation_notes" with a tenant_id column
  And no file "db/export-map/clm.obligation_notes.yaml"
  When CI runs
  Then the job "NN-11_export_map_complete" fails naming the table

@P00-AT-12 @NN-12
Scenario: A destructive migration in the same release as its replacement is rejected
  Given a migration that renames column "dms.documents.title" while the previous release reads it
  When CI runs the expand-contract checker
  Then the build fails with the rule "expand-contract: rename without shadow column"

@P00-AT-13 @NN-25
Scenario: Infrastructure outside India is denied
  Given an IaC plan creating an S3 bucket in eu-west-1
  When the plan is applied in any LawDocs account
  Then the service control policy denies the request

@P00-AT-14
Scenario: Migration cannot be promoted with a money mismatch
  Given rehearsal R2 where the sum of PAID orders for March 2025 differs from the PayU settlement report by ₹1,499.00
  When the operator tries to promote the run
  Then promotion is refused with "LD-CORE-041" and the delta is listed with the affected order aliases

@P00-AT-15
Scenario: A migrated customer finds their order and document after cut-over
  Given legacy user "meera@example.com" with one PAID order for a rent agreement and its PDF
  When she signs in to my.lawdocs.in with an email OTP after cut-over
  Then her PERSONAL workspace shows the order under Billing with reference "LD-ORD-<year>-<n>" and the legacy order number as alias
  And the PDF is in her Legal Vault, marked "Imported from old LawDocs", with integrity assured from the migration date

@P00-AT-16 @NN-31
Scenario: Every old sitemap URL redirects in one hop to a server-rendered page
  Given the 186 URLs of the 2026-07 sitemap and the legacy URLs with impressions in Search Console
  When each is requested on http and https, with and without www
  Then each returns 301 (or an approved 410) to a https://www.lawdocs.in URL in one hop
  And the target returns 200 with a unique title, one H1 and body copy when fetched without JavaScript

@P00-AT-17 @NN-31
Scenario: robots and sitemap never conflict
  Given the generated robots.txt and sitemap index
  When the seo:check job runs
  Then no sitemap URL is disallowed by robots.txt
  And no path that has redirect rules is disallowed
  And /checkout/* pages carry noindex and are absent from every sitemap

@P00-AT-18 @NN-15
Scenario: Legacy chatbot logs never reach an AI store
  Given the legacy "chatlogs" collection with disposition ARCHIVE (encrypted 90-day archive, then deletion; FR-P00-67)
  When the migration runs
  Then no chatbot message exists in any ai, agt, drf or dms table or index
  And the encrypted archive is scheduled for deletion on the approved date

@P00-AT-19 @NN-20
Scenario: Unevidenced claims do not survive cut-over
  Given the claims inventory marks "verified lawyers" and "ISO certified" as REMOVE
  When the new public site is crawled before go-live
  Then neither phrase appears on any page and the OH14 claims gate returns PASS for the published copy

@P00-AT-20 @NN-47
Scenario: Shared kernels are used, not forked
  Given the dependency @infrabyx/governance-kernel pinned at version X
  When a module adds a local copy of an exported kernel function
  Then the "NN-47_no_kernel_fork" check fails naming the symbol

@P00-AT-21 @NN-27
Scenario: Clocks and logs meet CERT-In directions
  Given production hosts and containers
  When the compliance probe runs
  Then every host syncs to an approved NTP source
  And ICT logs older than 180 days are still present in ap-south-1 storage

@P00-AT-22
Scenario: Decommissioning requires archive evidence
  Given the Atlas cluster with disposition ARCHIVE
  When an operator tries to mark it SOURCE_DELETED without a restore-test evidence link
  Then the transition is refused with "LD-CORE-042"
```

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] `docs/discovery/01…11` complete; disposition register signed by owner and DPO; claims inventory corrections applied to the legacy site.
- [ ] Monorepo, module skeletons, boundary rules, CODEOWNERS; Node/Next/Nest/Keycloak/Cerbos/PostgreSQL versions recorded in ADR-0001 with dated sources.
- [ ] Environments dev/test/staging/pre-prod/prod/dr and the `mig` zone provisioned by IaC; SCPs active; provider routing guard tested.
- [ ] CI required checks including `pnpm nn`, `seo:check`, export-map, RLS lint, expand-contract checker; CD with signed images.
- [ ] `core` schema frozen (sprint 4) with RLS, ledger, anchors, corrections, access log, break-glass schema, IDs, business refs, outbox/inbox, idempotency, flags, kill switches, settings heads.
- [ ] Buckets with Object Lock; ingest skeleton; masking hook.
- [ ] NN tests active for every NN in this file's header; SCAFFOLD tests for all others; `tests/nn/registry.yaml` complete.
- [ ] Seed profiles and synthetic identifier lint.
- [ ] Migration rehearsals R1–R3 passed; final run promoted; reconciliation evidence stored; migration notice sent.
- [ ] Cut-over done; 301 map live; robots/sitemap corrected; Search Console monitored for 28 days with 404s ≤ baseline + 5%.
- [ ] Railway, Atlas, legacy Anthropic key and PayU decommissioned in order with certificates.
- [ ] ADR-0001…0024 written; `docs/` structure in place; verification log seeded.

**Demo script (30 minutes).** (1) Two tenants, one cross-tenant query returning zero rows. (2) A super-admin correction refused for self-approval, approved by the security officer, visible to the tenant. (3) Attempted overwrite of a locked original. (4) Kill switch engaged and propagated. (5) Migration console: R3 reconciliation with zero money delta. (6) A migrated customer signs in and sees order and document. (7) Ten old URLs, including a non-www deep link and a `/buy/` URL, each landing in one hop on SSR pages; no-JS crawl report. (8) Decommissioning certificate for Railway.

**Registered in P00:** export-map entries (FR-P00-88); settings (§9); help keys (§6); error codes (§7.6); events (§7.4); screens SCR-P00-01…11.

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P00-01 | Confirm the legacy stack facts (Vite/React SPA, Express with Anthropic chatbot route, MongoDB Atlas, Railway, PayU) and their regions | Tech lead at discovery |
| OI-P00-02 | Keycloak import support for the legacy password-hash algorithm | Tech lead |
| OI-P00-03 | Whether migration to the new operating entity (if different from the legacy contracting entity) needs fresh consent or notice | [COUNSEL] |
| OI-P00-04 | Disposition of legacy chatbot logs and legacy leads; retention periods | [OWNER] + DPO + [COUNSEL] |
| OI-P00-05 | Treatment of "LawDocs Coins"/wallet or referral balances, if any | [OWNER] |
| OI-P00-06 | AI-crawler policy (training bots) | [OWNER] |
| OI-P00-07 | PayU dispute/chargeback window and account-closure timing | [OWNER] with PayU |
| OI-P00-08 | GST record-retention period confirmation (CGST s.36) and Companies Act s.128(5) for the archive | [TAX MEMO] |
| OI-P00-09 | Appendix Y change request: owner code `LD`, LawDocs as `TenantProvisioned` consumer, LawDocs-originated subjects | Integration Spec owner |
| OI-P00-10 | Observability vendor India residency | Tech lead |
| OI-P00-11 | Temporal self-hosted vs Temporal Cloud residency | Tech lead |
| OI-P00-12 | Single public phone number across site and academy (R5 §1.3) | [OWNER] |
