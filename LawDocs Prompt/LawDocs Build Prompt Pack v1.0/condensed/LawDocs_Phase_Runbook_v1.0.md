# LAWDOCS — PHASE RUNBOOK (v1.0, 25 October 2026; second review applied)
One section per phase: the exact session prompt to paste into Claude Code, dependencies, binding appendices, the exit gate and integration notes. Run phases in the wave order of master §13. Each session starts with the plan; no code before the owner approves it.

## How to start every session

1. Make sure `docs/00-master-prompt.md`, `docs/01-decision-log.md`, `docs/phases/`, `docs/appendices/` and `docs/reference/authoring-conventions.md` are the current pack version, and `docs/ecosystem/infrabyx-integration-spec.md` matches the tagged Ecosystem Spec.
2. Paste the session prompt below for the phase.
3. Review `docs/phases/PXX-plan.md`; approve, amend or reject.
4. At the exit gate, review the hand-over report (master §0 step 5) and the checklist below before starting the next phase.

---

## Phase P00 — Foundations, Repository Discovery and Migration

**File:** `phases/P00_Foundations_Repository_Discovery_and_Migration.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** none (first phase). Read-only access to the legacy lawdocs.in repository, a point-in-time restore of the MongoDB Atlas database, the Railway project (viewer), the DNS zone, the PayU merchant dashboard (read-only), the Anthropic console (usage and key list), Google Search Console and the live site. Companion documents committed unchanged under `docs/ecosystem/` with SHA-256 checks: Infrabyx Ecosystem Integration Specification v1.1, Operations Hub Master Prompt v1.0, LawDocsComply Pack v1.2 (reference only), Equator v3.1 (reference only).
> **Sequencing:** Sprint 1 discovery and repository scaffold run in parallel; sprints 2–4 build the platform core; sprint 4 starts P01 (identity) and P21 core (SSR site shell) in parallel; sprints 5–6 run migration rehearsals and the SEO cut-over. **Freeze points:** (1) the disposition register is signed off by the owner before any legacy asset is retired; (2) the `core` schema, ID prefixes, audit-event structure and export-map contract freeze at the end of sprint 4 (later phases extend, never change); (3) the 301 map freezes 10 days before DNS cut-over (T−10 d, §5.5; `web.redirects.freeze_days_before_cutover`). The legacy site stays live and read-write until cut-over (§5.5). **Customer cut-over dependency:** T0 (§5.5) needs P01's OTP sign-in, P04's vault list view and P17's order/billing mirror view running in pre-prod; if they are not ready by sprint 6, P00 exits with R1–R3 passed and every other gate item met, and the final customer migration run, DNS cut-over, decommissioning (FR-P00-83) and @P00-AT-15/16 move to a dated P00 tail that must close before the Wave 1 P23 go-live gate.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and access — coarse platform roles only in P00), K (export package `LD-EXPORT-1.0`; export-map registry created here), P (security, privacy and certification readiness), R (settings registry; heads created here), W (verification log and open items), Y (Ecosystem Spec v1.2 change request: owner code `LD`).
> **Requirements covered:** R-001, R-002, R-003, R-021 (storage foundations), R-022, R-031 (foundations), R-032 (rendering and host hygiene), R-033 (foundations), R-057 (CI/CD skeleton; detail in P23), R-067, R-068 (foundations), R-070, R-071.
> **Decisions applied:** D-01, D-02, D-08, D-09, D-10, D-14 (AI gateway stub only), D-16 · **Challenges applied:** CH-15, CH-16, CH-19 (claims hygiene of the legacy site), CH-20 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-11, NN-12, NN-15, NN-19, NN-20, NN-24, NN-25, NN-27, NN-29, NN-31, NN-32, NN-38, NN-39, NN-45, NN-46, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 1 frontend engineer, 1 platform/DevOps engineer, 1 data-migration engineer, 1 QA/security engineer, 1 web/SEO engineer) plus the owner as product owner and a part-time content reviewer for blog migration.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P00-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

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

### Integrations to respect

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

### Exit gate, deliverables and open items

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

## Phase P01 — Identity, Onboarding, KYC/KYB and Consent

**File:** `phases/P01_Identity_Onboarding_KYC_KYB_and_Consent.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (core schema, tenancy, ledger, settings heads, flags, ingest, provider routing). External: Keycloak; a DLT-registered SMS route (JioCX or another CPaaS) and optional WhatsApp authentication templates; Google and Microsoft OIDC apps; DigiLocker Requester onboarding with NeGD; UIDAI Aadhaar secure-QR verification (Phase 1, no registration) and OVSE registration under Reg 13A (Phase 2); one licensed KYB vendor (MCA data), one GSP (GSTIN search), GLEIF (LEI); Operations Hub OH3 (consented leads), OH4 (provisioning), OH9 (professional directory).
> **Sequencing:** Starts in P00 sprint 4. Sprints 1–3: identity architecture, login methods, sessions, consent ledger, individual fast path. Sprints 4–6: verification ladder, DigiLocker, Aadhaar offline (QR), KYB, signatory authority, company wizard. Sprints 7–8: professionals, guests, guardians, nominees, partner onboarding API, accessibility pass. P02 starts in parallel from sprint 2 (it needs persons, users and memberships, which freeze at the end of sprint 2). Wave-2 migration activation (P00 users) runs at the P01 exit.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, grant types, assurance requirements), K (export folders for profile, KYC and consent records), P (security and privacy controls; DPDP programme), R (settings), W (verification log and open items), Y (ecosystem change request: LawDocs as onboarding target and `TenantProvisioned` consumer).
> **Requirements covered:** R-002, R-003, R-005, R-009, R-017 (identity for web and mobile), R-023 (consented sharing foundations), R-025 (accessible authentication), R-028, R-030, R-031, R-061 (individual identity), R-064 (maker accounts), R-072 (notices and policies in-product).
> **Decisions applied:** D-01, D-02, D-06, D-08, D-10, D-12 (KYC via provider-neutral adapters) · **Challenges applied:** CH-01, CH-02, CH-03, CH-04, CH-05, CH-06, CH-08, CH-09, CH-15, CH-16, CH-17, CH-18, CH-30 · **Non-negotiables tested:** NN-03, NN-04, NN-05, NN-06, NN-11, NN-13, NN-19, NN-20, NN-21, NN-23, NN-24, NN-26, NN-28, NN-32, NN-34, NN-38, NN-42, NN-44, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 2 frontend engineers (web + responsive/mobile flows), 1 identity and security engineer, 1 integrations engineer for KYC/KYB vendors, 1 QA and accessibility engineer).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P01_Identity_Onboarding_KYC_KYB_and_Consent.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P01-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The owner asked for "Aadhaar login", automatic fetching of details from Aadhaar, PAN, CKYC, MCA and CIBIL APIs, and very fast onboarding for individuals and companies. Research shows that LawDocs is not, and does not plan to become, an Aadhaar requesting entity (Aadhaar Act s.4(4); s.57 omitted by the 2019 Amendment Act; the good-governance route under LG-027 is a long path, never a dependency; R3 LG-021–025), cannot search or download CKYC (PML Rules r.9; R3 LG-046), is unlikely to qualify for direct PAN verification (R3 LG-047), cannot pull credit-bureau data (CICRA ss.17(4), 22; R3 LG-057–058) and has no open MCA API (R3 LG-050). P01 delivers the lawful version of the same experience, and makes it faster than the owner's design:

- **Sign-in in one step** with mobile OTP, email OTP, passkey, password + MFA, Google or Microsoft sign-in, or enterprise SSO. No Aadhaar login (NN-03, CH-01).
- **Verification only when needed**, on a four-level ladder (L0 → L3), using DigiLocker issued documents, Aadhaar secure-QR / e-Aadhaar verification and later Aadhaar Verifiable Credentials as a registered OVSE, licensed KYB vendors, GSPs, GLEIF and Entity Locker — never storing an Aadhaar number (NN-04).
- **Companies discovered from one identifier** (CIN, LLPIN, GSTIN, PAN of the entity, LEI or Udyam) with provenance per field, then the authorised signatory verified with authority evidence.
- **Professionals onboarded with real credential checks**, advocates showing only BCI Rule 36 fields (NN-21).
- **Counterparties sign without an account**, guardians manage wards, nominees get time-locked access after verified events.
- **Consent per DPDP purpose** with versioned notices, one-tap withdrawal and a privacy centre.
- **Partners and sister products** start onboarding on the customer's behalf — group products through the Operations Hub (`TenantProvisioned`), third-party partners through the P19 partner API — but every workspace starts as an invitation; nothing activates until the customer confirms, and the requester gets no access.

| Outcome | Measure (exit gate; p75 in moderated usability tests with 10 participants per journey, then production analytics) |
|---|---|
| Individual: first draft fast | Landing on a document page → first draft preview ≤ **2 minutes** for documents with ≤ 10 required questions; account creation adds ≤ 3 taps + one OTP |
| Company: set-up fast | Sign-up → company workspace with discovered profile, departments and approval model → first agreement started ≤ **10 minutes** |
| No Aadhaar login exists | `NN-03_no_aadhaar_login`: no route, IdP, Keycloak authenticator or UI string offers Aadhaar as a login method |
| No Aadhaar number stored | `NN-04_*` suite: zero Aadhaar-number columns; QR payloads discarded after verification; logs clean |
| Discovery quality | Companies with a CIN: ≥ 85% of profile fields pre-filled with provenance; discovery p50 ≤ 20 s, p95 ≤ 40 s |
| Consent integrity | 100% of optional processing has a consent artefact referencing a notice version; withdrawal propagates internally ≤ 1 hour and to the Operations Hub ≤ 1 hour (Ecosystem Spec §6.14 [REC]) |
| Accessible authentication | WCAG 2.2 AA incl. SC 3.3.8; no image CAPTCHA; every verification path has a non-visual, non-liveness alternative (R3 LG-136 [VERIFY]) |

---

### Integrations to respect

| Port | Primary / alternatives | Failure behaviour and manual fallback |
|---|---|---|
| `SMS_PORT` | DLT-registered CPaaS (JioCX or other) primary + second CPaaS | Fail over; then email OTP; then voice OTP (when enabled) |
| `WHATSAPP_PORT` | Meta Cloud API direct; BSP alternate (R6 D-31) — authentication templates only | OFF by default; fall back to SMS |
| `EMAIL_PORT` | SES ap-south-1 / Brevo transactional | Retry; status shown |
| `SOCIAL_IDP_PORT` | Google, Microsoft OIDC | Offer OTP |
| `DIGILOCKER_PORT` | DigiLocker Requester direct (R6 D-18); aggregator fallback only with NeGD-compliant terms | Other L2 methods |
| `AADHAAR_OFFLINE_PORT` | Local verification of UIDAI signatures (Phase 1); Aadhaar App AVC integration (Phase 2) | Other L2 methods; flags OFF until verified (NN-38) |
| `COMPANY_DATA_PORT` | Licensed MCA-data vendor primary + secondary (R6 D-15) | Document-first fallback with reviewer |
| `GSTIN_PORT` | GSP (R6 D-16) | Manual GSTIN entry with certificate upload |
| `LEI_PORT` | GLEIF | Skip |
| `ENTITY_LOCKER_PORT` | NeGD Entity Locker (flag OFF) | Document upload |
| `PAN_PORT` | DigiLocker PAN; vendor with lawful-upstream warranty (flag OFF) | DSC or assisted L3 |
| `PRO_DIRECTORY_PORT` | OH9 via `int` | LOCAL desk |
| `CONSENT_MANAGER_PORT` | Registered consent managers (flag OFF) | Native consent |
| `BILLING_PORT` | OH8 (plan on wizard step if purchase chosen) | Continue on free/trial |

Each adapter carries a kill switch (NN-39), idempotency key and reconciliation record (NN-46), and non-prod routes to fakes (P00).

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] Realms, clients, Keycloakify themes (LawDocs + Consumer Help brand); BFF sessions; mobile token handling.
- [ ] All login methods live; passkeys promoted; step-up working; SSO + SCIM tested with Entra ID and Google Workspace.
- [ ] Ladder L0–L3 with DigiLocker (Requester onboarding complete or flag OFF with OI), Aadhaar offline Phase 1 (flag gated), DSC, assisted L3.
- [ ] KYB discovery with one vendor + GSP + GLEIF; document-first fallback; review queue with maker-checker.
- [ ] Signatory authorities with limits read by P02 DoA.
- [ ] Professional applications with OH9 or LOCAL desk; Rule-36 preview.
- [ ] Guests, wards, nominees, consent ledger, notice versions, privacy centre, rights requests.
- [ ] Activation flow for P19 partner invitations and OH-provisioned tenants (behind the Appendix Y gate for `TenantProvisioned`).
- [ ] Individual ≤ 2 min and company ≤ 10 min journeys measured in moderated tests (10 participants each, including two screen-reader users and two Hindi-first users).
- [ ] NN tests in the header ACTIVE; acceptance scenarios pass; settings, help keys, error codes, events and export-map entries registered.
- [ ] P00 wave activation of migrated users done.

**Demo script.** Draft and save a rent agreement in under two minutes on a phone; add a passkey; verify by DigiLocker PAN; set up "Alpha Pvt Ltd" from a GSTIN, see provenance and a conflict card; Rahul becomes signatory automatically; Priya's board-resolution authority reviewed by two people; an advocate applies and sees the Rule-36-only preview; a guest opens an invitation and says "not me"; a nominee release cancelled by the owner's sign-in; marketing consent withdrawn and propagated; a partner-batch invitation activated in four taps with no partner access.

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P01-01 | DLT principal-entity registration, headers and OTP templates for the operating entity | [OWNER] |
| OI-P01-02 | UIDAI secure-QR verification specification and OVSE Reg 13A registration (fees, documents, Class 3 certificate) | [OWNER] + [COUNSEL] |
| OI-P01-03 | NeGD written confirmation on user-directed saving of DigiLocker documents; Requester onboarding | [OWNER] with NeGD |
| OI-P01-04 | Entity Locker Requester API eligibility and terms | Tech lead |
| OI-P01-05 | KYB vendor contracts with lawful-sourcing warranties (primary + secondary) and prices | [OWNER] |
| OI-P01-06 | Vendor PAN API warranty (or decision to rely on DigiLocker PAN only) | [OWNER] + [COUNSEL] |
| OI-P01-07 | Professional verification sources (State Bar Council rolls, ICAI/ICSI directories) and their terms; COP rules citation | [COUNSEL] |
| OI-P01-08 | OH9 readiness for LawDocs professional applications; interim LOCAL desk | Integration Spec owner |
| OI-P01-09 | Acceptable guardianship and incapacity evidence under DPDP Rules 10–11 | [COUNSEL] |
| OI-P01-10 | Nominee release wording vis-à-vis succession law | [COUNSEL] |
| OI-P01-11 | Consumer Help: separate fiduciary account-sharing model | [COUNSEL] |
| OI-P01-12 | Cross-product customer sign-in by token exchange (not in Appendix Y rev. of 25 Oct 2026); confirm `PARTNER_ONBOARDING_PREFILL` purpose and `TenantRegistered` acceptance | Integration Spec owner / pack lead |
| OI-P01-13 | DigiLocker as a sign-in option: kept out (NN-03); revisit only by ADR + counsel | [OWNER] |
| OI-P01-14 | Current IT Rules grievance timelines and E-Commerce Rules sub-rules | [COUNSEL] |

## Phase P02 — Tenancy, Organisation Structure, User Types and Maker-Checker

**File:** `phases/P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenants, legal entities, ledger, settings heads, flags), P01 (persons, users, memberships, invitations, verification levels, signatory authorities). External: Cerbos; Operations Hub OH10 (staff SCIM and `group_grant` memberships), OH4 (onboarding milestones); `@infrabyx/governance-kernel` for director/KMP designations when mounted (P13) or LawDocsComply when it is system of record (D-10).
> **Sequencing:** Starts in P01 sprint 2 (persons/users/memberships frozen). Sprints 1–2: org model, workspace types, context switcher, role grants, Cerbos policy framework. Sprints 3–4: maker-checker engine, DoA tables, SoD engine, delegation and out-of-office. Sprints 5–6: custom roles, group and cross-functional grants, delivery-grant interface, access reviews, role-based homes and navigation. P03 (Configuration Studio) consumes the maker-checker and DoA schemas from sprint 4; P18 builds the Delivery Console UI on the grant model frozen at the end of sprint 5.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, permission matrix, maker-checker action catalogue, SoD pairs, Cerbos conventions, grant types), P (access-control and privileged-access controls), R (settings), K (export folders for organisation and access records), W (open items), X (Operations Hub additions: group-grant feed and access-review event).
> **Requirements covered:** R-026, R-027, R-028, R-030, R-047 (configurable approvals; item types in P03), R-048 (separation of operations from super admin), R-051 (maker-checker, anti-fraud), R-058, R-059 (organisation structure foundations), R-060 (one-CLO operating model), R-064, R-065 (client section access model), R-066, R-067.
> **Decisions applied:** D-02, D-03, D-06, D-10, D-17 · **Challenges applied:** CH-14, CH-16, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-17, NN-18, NN-19, NN-23, NN-28, NN-29, NN-33, NN-43, NN-45, NN-47
> **Estimated effort:** 6 two-week sprints, squad of 8 (tech lead, 3 backend engineers, 2 frontend engineers, 1 security/authorisation engineer, 1 QA engineer).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P02_Tenancy_Org_Structure_User_Types_and_Maker_Checker.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P02-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The owner wants many user types — super admin, an operations team serving clients, company admins, makers and checkers, departmental users, individuals — each with its own features, fewer clicks and an anti-fraud design where "employees cannot cheat". P02 gives LawDocs one authorisation model that serves every workspace type, without special-case code:

- **Structure:** tenant → legal entities → branches → departments → teams → positions, renameable and effective-dated, for a one-person startup and for a listed group with forty subsidiaries.
- **Workspaces:** Personal, Company, Professional firm and the Consumer Help brand, with a context switcher that always shows *where* and *as whom* the user is acting.
- **Roles:** the binding role codes (master §1.4; Appendix D), scoped grants, a custom-role builder and positions, so that a company can model "Head – Legal (Delhi)" without asking LawDocs.
- **Approvals:** a configurable maker-checker engine per action type and a delegation-of-authority (DoA) matrix by value, document type and department, with segregation of duties enforced at person level.
- **Controlled outsiders:** LawDocs relationship managers as delegated makers, engaged professionals, external counsel, auditors, counterparties, family members, delegates and nominees — each through a scoped, time-bound grant the customer controls; Infrabyx cross-functional staff through purpose-bound group grants that are never inherited (Ecosystem Spec §4.6).
- **Integrity without surveillance:** maker ≠ checker, approvals bound to the exact version approved, quarterly access reviews and immutable logs — not keystroke or screen monitoring (NN-33; CH-24, CH-32).

| Outcome | Exit-gate measure |
|---|---|
| One model, every workspace | All persona journeys in §4L pass with the same policy engine; no `if (tenant.kind === …)` authorisation branches in handlers (Semgrep rule) |
| Maker ≠ checker everywhere | `NN-18_*` suite: for every action in the Appendix D catalogue with mode REQUIRED/LOCKED, the maker (and the maker's delegator, linked staff identity or agent sponsor) cannot approve |
| Approvals bind to content | Changing a payload after approval invalidates the approval (`LD-WF-012`) in 100% of catalogue actions |
| Outsiders are scoped | `NN-17_*`: delivery and engagement grants require client approval, expire, revoke within 60 s; break-glass needs two approvers and a client report ≤ 24 h |
| Group roles never inherited | `NN-17_group_grant_not_inherited`: membership in a parent tenant or another Infrabyx company never yields access to a child tenant without an explicit grant |
| Fewer clicks | Role-based home screens meet the click budgets of §4L in moderated tests |
| Customisation without LawDocs | A company owner creates a custom role, a new department and a DoA rule, and enables maker-checker on external sharing, without any LawDocs staff action (NN-29) |

---

### Integrations to respect

| Port / source | Use | Failure behaviour |
|---|---|---|
| `RULES_PORT` (GoRules ZEN + CEL) | DoA evaluation | Fail closed: route to `ORG_OWNER` with `LD-WF-030`; never skip approval |
| Cerbos PDP | Every authorisation decision and query plan | Fail closed (deny); health alarm |
| OH10 SCIM (staff realm) | Staff identities and `group_grant` memberships | Local expiry enforcement continues; new grants wait |
| OH4 | Onboarding grant milestones (counts only) | Queue |
| Governance kernel / LDC contracts | Directors and KMP designations | Use last confirmed snapshot; flag staleness |
| P18 Delivery Console | Renders grants, transparency log, RM workbench | — |
| P17 billing mirror | Seat counts by class; delivery grant ↔ active retainer check | Drift flag only |

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] `org` model with templates, restructures (batch + undo), positions; directors/KMP linked to the kernel or LDC.
- [ ] Workspace types and the context switcher across web and mobile; notifications labelled by context.
- [ ] Role catalogue seeded; custom-role builder; position-based grants; Cerbos policies with generated tests and query plans; Semgrep rule for `@Authorize`.
- [ ] Maker-checker engine with the Appendix D catalogue, LOCKED NN-18 set, digest binding, inbox, solo-owner rule; DoA tables, simulator and gap check.
- [ ] SoD engine (person-level), delegation, away routing, leaver handling.
- [ ] Grant model and enforcement for all grant types; transparency log writes; break-glass with dual approval; group-grant intake with local expiry.
- [ ] Access-review campaigns with evidence packs; drift scans.
- [ ] Role-based homes and navigation meeting §4L budgets in moderated tests (8 personas × 3 participants).
- [ ] NN tests in the header ACTIVE; settings, help keys, error codes, events, export-map entries registered.

**Demo script.** Ananya switches between Personal and Alpha; Neha submits an ₹18 lakh agreement routed CLO → CFO with an explanation; an edit invalidates approval; Kavita tightens external sharing without LawDocs; Vikram's delivery grant approved, used, revoked within 60 seconds; break-glass dual approval and the client report; an umbrella admin denied child data; a custom role blocked at its ceiling; access review auto-revokes an engagement grant; master-data change approved by the client in one tap.

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P02-01 | Confirm the solo-owner interpretation of NN-18 for one-person company tenants (cooling-off + notifications) | Pack lead / [OWNER] |
| OI-P02-02 | Professional record-keeping vs client data ownership in firm workspaces | [COUNSEL] |
| OI-P02-03 | Related-party and other board-approval triggers for DoA flags (Companies Act s.188 thresholds and rules) | P13 / [COUNSEL] |
| OI-P02-04 | Operations Hub additions: group-grant SCIM attributes for LawDocs roles; `AccessReviewCompleted` for LawDocs scope (Appendix X) | Integration Spec owner |
| OI-P02-05 | Default DoA rows for regulated finance-company tenants aligned with LDC rule packs | P13 / LDC owner |
| OI-P02-06 | Seat classes by role for pricing (FULL/LIGHT/FREE_GUEST) | P17 / [OWNER] |

## Phase P03 — Configuration Studio, Rule Engine and Settings

**File:** `phases/P03_Configuration_Studio_Rule_Engine_and_Settings.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `packages/config` skeleton, hash-chained audit ledger, `core.correction_entries`, transactional outbox, Temporal, Cerbos, OpenTelemetry), P01 (identity, step-up authentication, consent artefacts), P02 (tenants, legal entities, departments, positions, user types, delegations and the maker-checker engine in `wf`). External: none at runtime (GoRules ZEN and CEL are embedded libraries).
> **Sequencing:** Sprint 1 freezes four contracts that every later phase consumes: the settings SDK (`packages/config`: registry, resolver, codegen, CI lint), the tier tree and control classes, `RULES_PORT` (`packages/rules`) and the open/interim/waiting **items API** (`packages/workflow` → `wf.items`). P04, P06, P07, P08, P17 and P19 start consuming in sprint 2. Studio screens follow in sprints 2–5; rule authoring and golden-case tooling in sprints 3–5; configuration templates, sandbox and export/import in sprint 6. No phase may read a setting, evaluate a legal rule or create a waiting item through any other path after sprint 1 (NN-29).
> **Binding appendices:** A (workflows and state machines — A.13–A.17), B (data model, events and error codes), R (configuration framework and settings catalogue — binding for every key, tier and default), D (roles and access matrix), F (instrument eligibility gate — rows run in this engine), H (agent roster — autonomy keys), K (export package — configuration and items folders), W (open items), Y (Ecosystem Spec v1.2 change request). Precedence on conflict: master §18 (master → `02` → G → F → B → A → D → R → C → this phase), except that this phase wins on the defaults of the keys it owns (X-11).
> **Requirements covered:** R-027, R-030, R-047, R-026, R-028, R-019, R-025 (accessible theming), R-008 (labels per language), R-064 (RM proposes configuration), R-066 (super-admin changes through a transparent workflow), R-067, R-054 (revenue-stream switches use the registry; values in P17), R-053/R-055 (suite-neutral templates).
> **Decisions applied:** D-01, D-02, D-06, D-07, D-10, D-12, D-13, D-15 · **Challenges applied:** CH-12, CH-21, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-13, NN-18, NN-28, NN-29, NN-30, NN-34, NN-38, NN-39, NN-40, NN-43, NN-45
> **Estimated effort:** 6 two-week sprints, squad of 8 (configuration core 2 backend; rule engine 2 backend; items engine 1 backend; Studio UX 2 frontend; QA/accessibility 1).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P03_Configuration_Studio_Rule_Engine_and_Settings.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P03-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs serves an individual signing a rent agreement, a five-person startup, a 2,000-employee NBFC with a legal department, a practising advocate and a consumer-help case manager. Each wants different words, screens, reminders, approvals and defaults. Indian law also changes often: a State revises stamp duty, the IT Act First Schedule is amended, the RBI replaces its Ombudsman Scheme. The owner's brief asks for "very complete settings", a "dynamic rule and content engine, not static", customisable "open, interim and waiting-for-someone-else items", and "super admin not needed for small changes" (R-047).

P03 delivers one governed configuration system:

- a **settings registry** where every configurable value is declared once, with a tier, a control class, bounds, an owner and an "i" help key;
- a **Configuration Studio** with three faces — Super Admin console, tenant administration (company admin, department head, professional firm admin) and personal settings (every user) — so that each user type changes what it may change, immediately and with audit;
- a **rule engine** (GoRules ZEN decision tables + CEL predicates behind `RULES_PORT`) that runs legal rules, jurisdiction variants, instrument-eligibility rows, reminders and SLA policies as versioned, sourced, effective-dated data with a reviewer of record (NN-30);
- an **open / interim / waiting items engine** used by every module, with configurable item types, statuses, owners, SLA clocks and chasers, and locked legal clocks that never pause;
- **feature flags and kill switches** for every agent, revenue stream, vendor adapter, consumer vertical and outbound channel (NN-39).

| Outcome | Exit-gate measure |
|---|---|
| Small changes without LawDocs staff (R-047) | A new company admin, unaided, in ≤ 20 minutes: renames two departments, adds three custom fields to agreements, relabels two agreement statuses, sets a numbering scheme, uploads a letterhead, changes the reminder cadence for renewals, pins three menu items and two quick actions, and sets quiet hours — all audited and undoable; zero LawDocs actions |
| Individuals customise in ≤ 2 taps | From home: theme, text size, language, home widgets and reminder timing each reachable in ≤ 2 taps on mobile and ≤ 2 clicks on web |
| Legal values governed | 100% of GOVERNED changes pass maker ≠ checker, preview, citation and effective date; 0 LOCKED values changeable through any UI or API (`NN-29_*`, `NN-18_*` tests) |
| Law changes as data | A changed State stamp-duty row, a new First Schedule entry or a revised Ombudsman timeline is drafted, golden-tested, reviewed by `PLT_LEGAL_REVIEWER`, scheduled and activated with no deployment; documents already in flight keep their pinned rule version |
| Waiting items work everywhere | The items API is frozen in sprint 1 and proven by a reference adopter and contract tests at P03 exit; each adopting phase (P04, P07, P08 in Wave 1; P11, P15, P16, P18 later) must pass `items-adoption` at its own exit gate; the "Waiting on others" widget shows every item with party, age, next chase and the legal clock that keeps running |
| Safe switches | Every kill switch registered in Appendix R propagates in ≤ 60 seconds and is drilled at least quarterly |

---

### Integrations to respect

| Port | Use in P03 | Adapters | Failure behaviour |
|---|---|---|---|
| `RULES_PORT` | Evaluate rule sets and predicates | GoRules ZEN (default), CEL, JSON Logic (fallback) | Engine error → declared fallback (`block` for protective eligibility); alert |
| `NOTIFY_PORT` (`ntf`) | Render and send templates and chasers | Email (SES/Brevo transactional), SMS/WhatsApp/RCS via JioCX and other DLT-registered CPaaS, push, Teams/Google Chat connectors | Channel kill switch holds messages; retry with idempotency; fallback channel only if the policy lists it |
| `DNS_CHECK_PORT` | Sender and custom domain verification | Internal resolver | Unverified → send "on behalf of" |
| `AI_PORT` (`packages/ai`) | Change summaries, NL settings mapping, item suggestions | Claude via Bedrock India (D-14) | AI unavailable → manual forms; nothing blocks |
| `ENTITLEMENT_PORT` (`bil` mirror of OH8) | Plan limits | OH8 `EntitlementChanged` | Keep last valid signed entitlement for 30 days if OH unreachable (Ecosystem Spec §6.27) |
| `COURT_DATA_PORT`, `TRADEMARK_DATA_PORT` (P11, P12) | Status refresh for items waiting on courts/registry | Licensed aggregators | Staleness label; manual check task |

No settings cross to other products; group tenants may share configuration **templates** through `tenant_link`, never data access (NN-24).

---

### Exit gate, deliverables and open items

**Deliverables**

1. `packages/config` (registry, resolver, codegen, hooks, decorators, test helpers) with CI checks `config-registry-lint`, `appendix-r-sync`, `nn18-keys`, `help-key-lint`, `schema-boundary`.
2. `packages/rules` with `RULES_PORT`, ZEN and CEL adapters, ADR, fixtures harness, evaluation recorder; seed rule sets registered (content per owning phase).
3. `packages/workflow` items API, `wf.items` schema, seed item types (Appendix R §R.11), chase and escalation workflows, widgets.
4. Studio screens SCR-P03-01 to SCR-P03-32 (axe clean; keyboard and screen-reader paths tested; mobile personal settings).
5. Flags and kill-switch registry with probes and drill reminders; all NN-39 switches registered.
6. Configuration bundle export/import, templates library (6 seeds), sandbox, compare, "Explain my configuration".
7. `docs/config/` developer guides and runbooks.

**Exit gate**

- [ ] All §12 scenarios and listed NN tests green; zero unregistered keys; Appendix R in sync with the seed.
- [ ] p95 resolve ≤ 2 ms warm; invalidation ≤ 60 s measured across pods.
- [ ] Pilot company admin completes the §1 20-minute script unaided; pilot individual completes the 2-tap tasks on mobile web (app parity re-tested in P22).
- [ ] Items API frozen and published in `docs/interfaces/`; `items-adoption` architecture test wired into CI so that each adopting phase (FR-P03-81) fails its own exit gate without items; a reference adopter (test module) passes it.
- [ ] Every NN-39 kill switch drilled once on the test tenant.
- [ ] **Export-map entries registered** (`xpt.export_map`): `cfg.setting_values` (tenant scopes) → `99 System Data (CSV and JSON)/Settings and Customisations/settings.csv|.xlsx|.json`; `cfg.custom_field_defs`, `cfg.status_sets`, `cfg.numbering_schemes`, `cfg.form_versions`, `cfg.letterheads` → same folder (`customisations.xlsx` + JSON); `cfg.setting_changes` and `cfg.change_requests` → `99 System Data (CSV and JSON)/Settings and Customisations/Change history/`; `rul.evaluations` → alongside the parent record (`… /04 Evidence and Certificates/Rule decisions.xlsx`) and `99 System Data (CSV and JSON)/Rule Decisions/`; `rul.adoptions` → `Settings and Customisations/Rules in use.xlsx`; `wf.items` with waits, clocks, interims and chase log → human file `Open and Waiting Items.xlsx` at the parent record folder and full set under `99 System Data (CSV and JSON)/Open and Waiting Items/`; `cfg.config_bundles` → `Settings and Customisations/Configuration bundle (ld-config-1.0).json` (Appendix K §K.3.5, §K.11).
- [ ] **Settings registered** in Appendix R §R.9 (`cfg`, `rul`, `wf`, `ntf` areas) and **help keys** of FR-P03-104 registered in `hlp`.
- [ ] Error codes registered (ranges `LD-CFG-001`–`099`, `LD-RUL-001`–`049`, `LD-WF-100`–`149`; `LD-WF-001`–`099` belong to P02; X-28) — enumerated below and mirrored in Appendix B §B.5.3; codes not listed are reserved:

| Code | Meaning (user message key `hlp.<module>.err_<nnn>`) |
|---|---|
| `LD-CFG-001` | Value type or schema invalid |
| `LD-CFG-002` | Child-direction rule violated (narrow / raise / lower only) |
| `LD-CFG-003` | Text contrast below 4.5:1 |
| `LD-CFG-004` | Value outside platform, brand or plan bounds, or below a floor |
| `LD-CFG-005` | Plan limit reached (upgrade options shown, none pre-selected; NN-50) |
| `LD-CFG-006` | Value locked at a parent tier |
| `LD-CFG-010` | Setting is locked |
| `LD-CFG-012` | Governed key — create a change request |
| `LD-CFG-013` | Citation required for this key |
| `LD-CFG-014` | Impact preview older than 24 hours — refresh before submitting |
| `LD-CFG-015` | Effective date earlier than the key's lead time |
| `LD-CFG-020` | You cannot approve your own change |
| `LD-CFG-021` | Checker not eligible (delegated from the maker or same SoD group) |
| `LD-CFG-022` | Change request expired |
| `LD-CFG-030` | Numbering token duplicate |
| `LD-CFG-031` | Numbering token invalid |
| `LD-CFG-040` | Custom form fails the accessibility check |
| `LD-CFG-050` | Kill switch cannot be released by the person who engaged it |
| `LD-CFG-051` | Kill-switch drill overdue (warning) |
| `LD-CFG-060` | Sandbox promotion conflicts with live changes |
| `LD-CFG-070` | Imported row rejected (locked or out of bounds) |
| `LD-CFG-071` | Configuration bundle signature invalid |
| `LD-CFG-080` | Support session needs tenant approval |
| `LD-CFG-081` | Emergency override expired — automatically reverted |
| `LD-RUL-001` | Rule set not found or not active for this jurisdiction and date |
| `LD-RUL-002` | Rule content (JDM/CEL) invalid |
| `LD-RUL-003` | Golden suite failed — mismatches not accepted |
| `LD-RUL-004` | Citations incomplete — cannot submit |
| `LD-RUL-005` | Source hash does not match the cited source |
| `LD-RUL-006` | Rule unverified — result is advisory only (NN-38) |
| `LD-RUL-007` | Pinned version expired — re-adopt or move to current |
| `LD-RUL-008` | Adaptation outside the permitted parameters |
| `LD-RUL-009` | Evaluation input incomplete |
| `LD-RUL-010` | Emergency block in force — action blocked |
| `LD-RUL-011` | Reviewer must differ from maker |
| `LD-RUL-012` | Reviewer of record lacks the required qualification |
| `LD-RUL-013` | Cannot retire a rule set still adopted without a replacement |
| `LD-RUL-014` | A challenge to this rule set is already open |
| `LD-RUL-015` | A code release cannot change published legal content (NN-30) |
| `LD-WF-100` | Item type not allowed for this parent |
| `LD-WF-101` | Item owner cannot be resolved |
| `LD-WF-102` | Waiting party type not allowed for this item type |
| `LD-WF-103` | Expected-by date required for a waiting item |
| `LD-WF-110` | Chaser deferred — quiet hours or business calendar |
| `LD-WF-111` | Chaser stopped — stop condition met |
| `LD-WF-112` | LawDocs never contacts courts, registries or regulators automatically |
| `LD-WF-113` | Counterparty reminder cap reached (NN-34) |
| `LD-WF-114` | Pre-approved series exceeds the maximum reminders (5) |
| `LD-WF-120` | Formality pending — cannot mark executed |
| `LD-WF-121` | Agents cannot waive an item |
| `LD-WF-122` | Evidence required to resolve this item |
| `LD-WF-123` | A checker must resolve this item type |
| `LD-WF-130` | Task has open dependencies |
| `LD-WF-131` | Task evidence missing |

**Demo script (10 minutes).** Company admin renames statuses, adds custom fields, sets a numbering scheme and letterhead; individual changes theme and text size on mobile; content editor drafts a State stamp-duty row, reviewer of record approves it with a future date, preview shows impact; an agreement hits the formalities gate with registration waiting on the Sub-Registrar while the legal clock keeps counting; owner sends a one-tap chaser to the counterparty; security officer engages and a second person releases an ESP kill switch.

**Open items**

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-P03-01 | ZEN Node binding maturity and licence; CEL JavaScript implementation choice | CTO (ADR sprint 1) | JSON Logic adapter behind `RULES_PORT` |
| OI-P03-02 | State-wise stamp-duty tables and registration thresholds — primary sources per State | P08 content team + `PLT_LEGAL_REVIEWER` | Rows `SECONDARY_ONLY` → indicative; manual stamp route |
| OI-P03-03 | RB-IOS 2026 clause numbers for the RE wait and filing windows | P15 content | Advisory clocks labelled [VERIFY] |
| OI-P03-04 | Plan limits for custom fields, item types, sandboxes, templates | [OWNER] with P17 | Seeds in Appendix R |
| OI-P03-05 | Confirm that a single confirmation of an enumerated, bounded reminder series satisfies NN-13 for transactional signing/review reminders | [OWNER] + [COUNSEL] | `CONFIRM_EACH` only until confirmed |
| OI-P03-06 | TCCCPR 2026 calling windows and AI-voice disclosure parameters for `IN.ntf.tcccpr` | P19 | Voice channel flag OFF |
| OI-P03-07 | Whether an external flag service (e.g., Unleash) is adopted or the in-house registry suffices | CTO | In-house registry |

## Phase P04 — Legal Vault and Document Management System

**File:** `phases/P04_Legal_Vault_and_Document_Management_System.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (repository, S3 SSE-KMS with versioning and Object Lock, audit ledger, outbox, OpenSearch, pgvector, Temporal, `packages/dix` skeleton), P01 (accounts, OTP/passkey sessions, step-up MFA, `CP_GUEST` magic-link identities, DigiLocker requester integration in `kyc`, consent artefacts `cns_`), P02 (tenants, legal entities, departments, user types, maker-checker, delivery grants), P03 (settings registry, rule engine `RULES_PORT`, metadata-schema and retention content packs). External: DigiLocker Requester API (NeGD), malware engines, Microsoft Graph and Google Drive APIs (optional), JioCX WhatsApp BSP (optional, flagged).
> **Sequencing:** Wave 1. Sprints 1–3 build the storage core (§4A–§4E, §4M, §4N) because P06, P07 and P08 write into it; sprints 4–6 build search, sharing, intake and reminders (§4F–§4K); sprints 7–9 build family vault, nominee access, Office co-editing, mobile offline and health checks (§4L, §4O–§4R). P04 ships the **`packages/dix` baseline** (malware scan, true-type sniffing, deterministic print OCR for search, Aadhaar detection and masking) so that NN-04 holds from the first upload; P05 (Wave 2) adds handwriting, type copies, translation and extraction on the same pipeline. P20 core (Wave 1) owns the import engine and `LD-EXPORT-1.0` packaging; P04 owns the vault-side mapping UX. **Freeze point:** the canonical document model (§4A) and the folder-view rule pack format freeze at end of sprint 3; later changes follow expand → migrate → contract (NN-12).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (personas and permission matrix), F (instrument eligibility — read by health checks), K (`LD-EXPORT-1.0` folder taxonomy — vault folder views mirror it), R (settings registry), W (open items), Y (Ecosystem Spec v1.2 change request — LD as producer of `documents` events).
> **Requirements covered:** R-011, R-021, R-022, R-023, R-024, R-043, R-053, R-055, R-061, R-067, R-068; contributes to R-005 (DigiLocker pull), R-017 (mobile), R-025 (accessibility), R-027, R-030, R-044 (inputs for type copy).
> **Decisions applied:** D-01, D-07, D-10, D-12 (DigiLocker via `kyc`) · **Challenges applied:** CH-02, CH-15, CH-16, CH-28, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-11, NN-12, NN-13, NN-15, NN-17, NN-18, NN-24, NN-25, NN-26, NN-28, NN-29, NN-30, NN-32, NN-38, NN-40 (health-check input), NN-42, NN-44, NN-45, NN-46
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, web 2, mobile 1, search/data 1, QA/accessibility 1), plus a part-time content analyst for metadata schemas and retention packs.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P04_Legal_Vault_and_Document_Management_System.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P04-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs must be the app a person or a company **keeps** — the place where every agreement, ID, policy, notice, order and receipt lives, can be found in seconds, is shared exactly as far as the owner chooses, and survives code releases, vendor changes and the owner's own exit. P04 builds the **Legal Vault** (individuals and families) and the **Document Management System** (companies) as one `dms` bounded context with two experiences.

The vault is not a "DigiLocker" under the IT (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules 2016 — LawDocs is not a licensed Digital Locker Service Provider. Product copy says **"Legal Vault"**, never "DigiLocker"; DigiLocker is a source the vault pulls from with consent (R3 LG-036–038; CH-15) **[LAW]**.

| Outcome | Exit-gate measure |
|---|---|
| Keep everything, lose nothing | Every original is stored once with SHA-256 at ingest and S3 Object Lock; zero originals overwritten in the release test suite (NN-09) |
| Find anything fast | Permission-trimmed search ≤ 1.5 s p95 on 1 million documents per tenant, ≤ 800 ms p95 on 10,000 documents per individual, including OCR text and Indic queries |
| Share exactly what you mean | A share pack containing one version, pages 3–7, redacted, view-only, watermarked, expiring in 72 hours, created in ≤ 6 clicks; revocation effective ≤ 60 s; every open logged and visible to the owner |
| Structure survives change | Folder views are computed from canonical IDs and metadata; a release that renames, reorders or adds folder views changes zero stored objects (NN-12) |
| Bulk intake | A 5,000-file folder tree or ZIP maps, previews and commits in one job with duplicate detection and no overwrite; re-import of an `LD-EXPORT-1.0` package maps 100% from its manifest |
| Nothing expires unnoticed | Every document with an expiry or renewal date produces reminders at the configured offsets; dashboard of "expiring in 30/60/90 days" |
| Family and legacy | An individual can add family members, guardians for dependants and a nominee with time-locked legacy access; the nominee release flow completes with identity verification and a cancellable waiting period |
| Lawful by construction | No full Aadhaar number is ever written to storage or to derived text (NN-04); DigiLocker documents are stored as URI + verification result unless a permitted retained copy is recorded (NN-42) |
| Portable | Every record type in this phase is registered in `xpt.export_map` and exports in `LD-EXPORT-1.0` without staff help (NN-11) |

"Done" for an individual: from the home screen they photograph a rent agreement, it is auto-classified as "Rent agreement", the expiry date is extracted as a suggestion, they confirm it, a renewal reminder is set, and they share pages 1–4 with their landlord's advocate for 7 days, view-only — in under two minutes.

---

### Integrations to respect

| Port / adapter | Use | Vendors / alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `STORAGE_PORT` (S3) | Originals, renditions, quarantine | AWS S3 ap-south-1 (+ replication to ap-south-2); MinIO for non-prod | Uploads queue; reads served from DR replica | — |
| `MALWARE_PORT` | Scan | ClamAV in-cluster + commercial engine where licensed | Fail-closed: files stay `PROCESSING` | Security officer review |
| `OCR_PORT` (baseline print) | Search text | Tesseract / PaddleOCR with Indic models (self-hosted) | Document stored and searchable by metadata only; re-run later | — |
| `DIGILOCKER_PORT` (in `kyc`) | Pull issued documents | NeGD Requester API direct (R6 D-18); aggregator fallback only after ToU review | "DigiLocker unavailable" with retry | User upload (no verified badge) |
| `M365_PORT`, `GDRIVE_PORT` (P19 connectors) | Pull, co-edit | Microsoft Graph, Google Drive API | Co-edit disabled; desktop round-trip | Download/upload |
| `WHATSAPP_PORT` via `packages/notify` | Inbound forward (flagged) | JioCX BSP [VERIFY], other DLT-registered BSPs | Feature off; share-sheet path | Share sheet |
| `EMAIL_IN_PORT` | Email-in | SES inbound (ap-south-1 availability [VERIFY]) or self-hosted MTA | Bounce with retry advice | Upload |
| `SEARCH_PORT` | Index | OpenSearch; PostgreSQL FTS fallback | Degraded search banner | — |
| `EMBED_PORT` via `packages/ai` | Semantic search | Bedrock India embedding model [VERIFY availability] | Keyword search only | — |
| `BILLING_PORT` (OH8 via `bil`) | Quotas, meters | OH8 | Last known entitlement cached 24 h; never blocks viewing/export | — |

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] Storage core, pipeline (with Aadhaar mask-before-commit), versions, relationships, views and smart folders live; NN-04/09/12 tests green.
- [ ] Search (keyword + semantic for en/hi) meets latency targets on the 1M-document load fixture; permission-trimming tests green.
- [ ] Share packs, recipient viewer, access log, revocation ≤ 60 s; pen-test of share origin passed.
- [ ] Intake mapping preview with P20 importer; `LD-EXPORT-1.0` round-trip test (export → import) identical by hash.
- [ ] Retention classes, holds, recycle bin, purge with crypto-shredding, disposal certificates.
- [ ] Reminders, Expiring soon, renewal chains.
- [ ] Family, dependants, delegates, nominees and legacy release.
- [ ] Health checks with Appendix F integration (advisory).
- [ ] Office round-trip; M365/Google co-edit behind connector; mobile vault with offline cache.
- [ ] Settings registered (Appendix R); help keys registered in `hlp` (all `hlp.dms.*` above); errors `LD-DMS-001…040` registered with user messages.
- [ ] Accessibility gate (axe + manual) passed on SCR-P04-01…20.

**Demo script (12 minutes).** (1) Scan a rent agreement on a phone; masking notice on an Aadhaar page; auto-classification; set end date; reminders appear. (2) Search "किराया" and find the English lease. (3) Share pages 1–4 view-only for 72 hours; open as recipient; revoke. (4) Upload a 2,000-file folder; mapping preview; commit; intake report. (5) Place a legal hold; show purge blocked. (6) Designate a nominee; simulate inactivity claim; owner cancels. (7) Health page shows "stamp missing" on an unstamped lease with "Buy eStamp" (P08 link). (8) Export the vault and show folders matching the vault views.

**Export-map entries (`xpt.export_map`)**

| Record type | `LD-EXPORT-1.0` location |
|---|---|
| `dms.document` + `dms.version` (originals) | View path (individual `01…10`; company `01…11`), file named per §4A-07; all versions under `_versions/` sub-folder of the document's folder |
| `dms.rendition` | Beside the original, suffixed ` (OCR text).txt`, ` (Redacted).pdf`, ` (Extract p3-7).pdf` |
| `dms.relationship`, `dms.doc_link`, `dms.metadata_values`, `dms.tags` | `99 System Data (CSV and JSON)/documents.csv`, `relationships.csv`; manifest columns |
| `dms.folder` (manual), `dms.saved_view` | `00 Index.xlsx` sheet "My folders" and `99 System Data/folders.json` |
| `dms.share`, `dms.share_access_log` | `99 System Data/sharing/shares.csv`, `share_access_log.csv` |
| `dms.legal_hold`, `dms.disposal`, `dms.purge_record` | `99 System Data/retention/` (CSV) + disposal certificates as PDF under `06 Policies and Registers/Retention/` (company) |
| `dms.reminder_fact` | `99 System Data/reminders.csv` |
| `dms.nominee`, `dms.delegate` | `99 System Data/family_and_nominees.csv` (individual) |
| `dms.digilocker_ref` | `01 My Profile and IDs (masked)/DigiLocker references.csv` (URI and verification only) |
| `dms.health_finding` | `99 System Data/health_findings.csv` |

**Errors (`LD-DMS-001…040`; 033–040 reserved).** Each has a user message and help key `hlp.dms.err_<nnn>`.

| Code | Meaning → user message (short) |
|---|---|
| 001 | File type not allowed → "This file type can't be stored. Save it as PDF or an image." |
| 002 | Malware detected → "This file looks unsafe and was not stored." |
| 003 | Storage quota reached → "Your vault is full. Free up space or upgrade; viewing and export still work." |
| 004 | Encrypted/password-protected file → "Remove the password and upload again." |
| 005 | Unsafe archive (ratio, nesting, traversal) → "This ZIP can't be opened safely." |
| 006 | Aadhaar number detected (info) → "We stored a masked copy; the first 8 digits are hidden." |
| 007 | Document checked out → "<Name> is editing until <time>." |
| 008 | Version conflict → "A newer version exists; your file was saved as a new version." |
| 009 | Legal hold → "This document is on legal hold and can't be deleted." |
| 010 | Retention floor → "Signed documents and evidence are kept until <date>. You can archive it." |
| 011 / 012 | Share expired / revoked → "This share has ended." |
| 013 | OTP failed → "The code didn't match. Try again or request a new code." |
| 014 | Class guard on external share → "This document can't be shared outside your organisation without approval." |
| 015 | Nominee waiting period → "Access opens on <date> unless the owner cancels." |
| 016 | DigiLocker consent/session expired → "Reconnect DigiLocker to view this document." |
| 017 | Retained DigiLocker copy not permitted → "We keep a verified link instead of a copy." |
| 018 | Duplicate → "This file is already in your vault — linked instead." |
| 019 | Intake mapping conflict → "Choose 'new version' or 'skip'." |
| 020 | Metadata validation → field-level messages from the schema |
| 021 | Recycle-bin item already purged → "This item was permanently deleted on <date>." |
| 022 | Maker-checker required → "Sent for approval to a checker." |
| 023 | Offline not allowed for this class → "Your organisation doesn't allow this document offline." |
| 024 | Email-in sender not allowed → generic bounce, no detail |
| 025 | WhatsApp channel disabled → "Use 'Share to LawDocs' from WhatsApp instead." |
| 026 | Relationship cycle → "This would make a document supersede itself." |
| 027 | Check-out expired → "Your edit lock expired; check in as a new version." |
| 028 | Co-edit connector not connected → "Connect Microsoft 365 or Google Drive in Settings." |
| 029 | Download/print disabled by sharer → "The sender allowed viewing only." |
| 030 | Item kind not shareable (DigiLocker onward display unverified) → explanation with alternative |
| 031 | Delegate scope exceeded → "Your helper access doesn't include this." |
| 032 | Checksum mismatch at ingest (P00 pipeline) → "The file changed during upload. Please upload it again." |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P04-01 | Counsel confirmation that mask-before-commit (with pre-mask hash and user-held original) is adequate for evidence containing Aadhaar numbers | [COUNSEL] / `PLT_LEGAL_REVIEWER` |
| OI-P04-02 | Nominee access wording vis-à-vis succession law; DPDP s.14 nomination procedure under the Rules | [COUNSEL] / `PLT_DPO` |
| OI-P04-03 | NeGD written position on retained DigiLocker copies and onward display in share packs (NN-42) | `PLT_DPO` |
| OI-P04-04 | JioCX WhatsApp BSP availability, media retention and transfer assessment | Owner / `PLT_DPO` |
| OI-P04-05 | Actual Microsoft 365 plan used by the group (CH-29) and connector scopes | [OWNER] |
| OI-P04-06 | Microsoft Cloud Storage Partner Program eligibility (WOPI) vs Graph co-edit only | P00 ADR |
| OI-P04-07 | Storage quotas and overage price | [OWNER TO SET] |
| OI-P04-08 | Retention floors marked [VERIFY] (income-tax under the 2025 Act; labour records; registers) | `PLT_LEGAL_REVIEWER` |
| OI-P04-09 | Bedrock India multilingual embedding model availability and cross-lingual quality per launch language | P09 / P00 |
| OI-P04-10 | Confirm `AGT_DMS_LIBRARIAN` L3 "moves with undo" means metadata/view moves only (never delete, share or purge) in Appendix H | Pack lead |

## Phase P05 — Document Intelligence: OCR, Handwriting/Screenshot Type Copy, Translation

**File:** `phases/P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (canonical document model, `drv_` renditions, ingest workflow, `packages/dix` baseline with print OCR and Aadhaar mask-before-commit, viewer, redaction tool, confidentiality classes), P09 runtime (`packages/ai` gateway: Claude vision and text via Amazon Bedrock India, guardrails, prompt registry, evaluation harness, credit metering), P08 (`sgn` evidence ledger and `Bsa63CertificateService`), P03 (rule engine, settings registry), P16 (marketplace fulfilment for certified translation and expert Part B services — stubbed until P16 ships). External: OCR engines (self-hosted), `TRANSLATE_PORT` adapters (Bhashini [VERIFY], Google/Azure India-region fallbacks), Bedrock India.
> **Sequencing:** Wave 2. Sprints 1–2: engine router, print OCR upgrade, handwriting and screenshot reading, Aadhaar detection on derived text; sprints 3–4: type copy generator, side-by-side editor, verification and labels, WhatsApp export parser; sprint 5: language identification and machine translation with glossary locks; sprint 6: extraction, classification and PII redaction suggestions; sprint 7: evaluation sets, quality tiers, petition/claim attachment contracts with P10/P15, hardening. P10 consumes the type-copy and translation rendition contract from sprint 4 (freeze point: `drv_` kinds, labels and anchor format at end of sprint 3).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (personas), F (eligibility families — classification feeds the gate), H (agent roster — `AGT_EVIDENCE_CLERK` #8, `AGT_TRANSLATOR` #9, `AGT_DMS_LIBRARIAN` #20), K (`LD-EXPORT-1.0`), R (settings), W (open items).
> **Requirements covered:** R-044, R-045, R-046 (correct AI errors), R-008, R-043; contributes to R-007, R-012, R-061, R-079 (pleadings annexures), R-083 (grievance evidence), R-025.
> **Decisions applied:** D-07, D-14, D-15 · **Challenges applied:** CH-11, CH-28 · **Non-negotiables tested:** NN-04, NN-09, NN-10, NN-13, NN-14, NN-15, NN-25, NN-28, NN-32, NN-38, NN-43, NN-46, NN-48
> **Estimated effort:** 7 two-week sprints, squad of 8 (ML/AI engineers 2, backend 2, web 1, linguist-QA 1, evaluation/data 1, QA/accessibility 1), plus a part-time panel of language reviewers for the evaluation sets.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P05_Document_Intelligence_OCR_TypeCopy_and_Translation.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P05-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Litigants and companies in India rely on documents that machines read badly: handwritten agreements and letters, photographed registers, WhatsApp chats, screenshots of UPI payments and bank messages, regional-language notices. The brief asks that AI "reads WhatsApp screenshots and handwritten documents, attaches them to the petition/claim with the typed copy; users can correct AI errors", plus translation into English (R-044, R-045, R-046).

P05 delivers that safely. The original stays the evidence (NN-09); everything the machine produces is a **derived rendition** — labelled, versioned, anchored to the page and line it came from, with confidence shown, corrected by a human and signed off before it is used in a filing. WhatsApp evidence is ingested from the **native chat export** wherever possible, hashed at upload and supported by a BSA 2023 s.63(4) certificate workflow (CH-28; R3 LG-091). Machine translations are labelled as such; filings route to certified translation (NN-48; CH-11).

| Outcome | Exit-gate measure |
|---|---|
| Handwriting usable | On the evaluation set, printed English/Hindi OCR character error rate (CER) ≤ 2%; handwritten English CER ≤ 8%, handwritten Hindi ≤ 12% before human correction **[targets to be confirmed by baseline run]**; every line carries a confidence band and a page/line anchor |
| Human in control | 100% of type copies attached to a filing are in `USER_CORRECTED` or `VERIFIED` status, or carry an explicit "not verified" acknowledgement shown in the bundle index |
| WhatsApp done right | A native export ZIP of 10,000 messages parses in ≤ 60 s with zero dropped lines on the 12 locale fixtures; ambiguous date formats are asked, never guessed |
| Languages | Language identification on 28 languages (22 Eighth-Schedule + 6 UN official languages) with per-language quality tiers published; translation to English available for all, marked machine translation |
| Aadhaar never leaks into derived text | Zero unmasked Aadhaar numbers in OCR text, type copies, translations, extractions, search index, logs (NN-04) on the red-team set |
| Extraction saves time | Parties, dates, amounts and key clauses proposed for ≥ 85% of agreements in the evaluation set with precision ≥ 0.95 on confirmed fields; obligations proposed to P07 |
| Court-ready | One action attaches original + type copy + translation as paired annexures to a P10 petition or P15 claim, with index rows, page references and the s.63 Part A draft |

---

### Integrations to respect

| Port / adapter | Use | Vendors / alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `OCR_PORT` | Print OCR | PaddleOCR / Tesseract (self-hosted, Indic models) | Retry; vision fallback for low-confidence pages | Manual type copy (user types in the editor against the original) |
| `VISION_PORT` via `packages/ai` | Handwriting, screenshots | Claude via Bedrock India (D-14) [VERIFY model availability in India region at build — R4] | `WAITING_ENGINE`; never non-India | Manual transcription; marketplace transcriptionist |
| `TRANSLATE_PORT` | MT | Claude (Bedrock India); Bhashini [VERIFY terms, retention, coverage]; Google Cloud Translation / Azure Translator India regions for non-confidential classes [VERIFY zero-retention terms]; candidate self-hosted Indic MT model (ADR) | Fail-closed by class | Certified translator (P16) |
| `LID_PORT` | Language ID | Self-hosted LID; Indic LID adapter | Ask user | User picks language |
| `EMBED_PORT` | Back-translation similarity | In-region multilingual embedding | Skip similarity → all segments flagged for review | Human review |
| `MKP_PORT` (P16) | Certified translation, Part B experts, transcription | Marketplace providers | Waitlist | Off-platform provider, upload result |
| `SGN_EVIDENCE` (P08) | s.63 Part A generation, ledger | Internal | Flag off | Print blank Schedule form [VERIFY] |

Every adapter call carries an idempotency key and is reconciled (NN-46); vendor kill switches per adapter (NN-39).

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] Router, engine registry and kill switches; residency fail-closed tests green.
- [ ] Print OCR upgrade, vision reading, screenshot understanding, WhatsApp parser with 12 fixtures.
- [ ] Type copy generator with anchors and labels; editor (web + mobile); verification and disputes.
- [ ] LID for 28 languages and code-mixed classes; MT with glossary locks and back-translation; certified-translation flow wired to P16 (stub allowed until P16 ships).
- [ ] Derived-text Aadhaar masking and late-detection purge; weekly sweep job.
- [ ] Extraction and classification with eligibility-suspect tightening; obligation proposals to P07.
- [ ] Evaluation sets with datasheets; tiers published; regression gate in CI.
- [ ] Annexure-pair contract consumed by P10 and P15 (contract tests).
- [ ] `dix.bsa63.enabled` remains OFF until the Schedule field labels are verified and signed off.
- [ ] Settings (Appendix R), help keys (`hlp.dix.*`), labels (`lbl.*`), errors registered.

**Demo script (10 minutes).** Upload a Hindi handwritten loan acknowledgement; low-confidence lines highlighted; correct two lines on the phone; self-attest; translate to English with locked "₹" amounts; attach original + type copy + translation to a P10 recovery suit annexure; import a WhatsApp export with an ambiguous date; map senders; generate the chat type copy; prepare s.63 Part A (flag on in staging); show the eval dashboard with Santali tier C.

**Export-map entries (`xpt.export_map`)**

| Record type | `LD-EXPORT-1.0` location |
|---|---|
| `dix.rendition` (type copy, chat transcript, translation, certified translation, OCR PDF) | Beside the original: `<name> (Type copy – <status>).pdf/.docx`, `<name> (Translation – English – Machine).docx`, `<name> (Certified translation – English).pdf` |
| `dix.lines`, `dix.corrections`, `dix.attestations` | `99 System Data (CSV and JSON)/document_intelligence/` (CSV; text included for the exporting owner) |
| `dix.wa_chats`, `dix.wa_messages` | Chat folder beside the original ZIP: `<chat> (Messages).xlsx` + `messages.json` |
| `dix.translation_segments`, `dix.glossary_terms` (tenant overlay) | `99 System Data/document_intelligence/translations/` |
| `dix.extractions` (confirmed) | Manifest columns + `99 System Data/document_intelligence/extractions.csv` |
| `dix.certified_requests` | `09 Services and Engagements/` (company) or `10 Receipts and Invoices/` (individual) with the certificate PDF beside the source |

**Errors (`LD-DIX-001…040`)**

| Code | Meaning |
|---|---|
| 001 | Unsupported content for intelligence (e.g., encrypted) |
| 002 | Insufficient credits — job not started |
| 003 | No permitted engine available for this data class — queued |
| 004 | Page image too low resolution — re-scan advised |
| 010 | WhatsApp date format ambiguous — answer needed |
| 011 | Not a recognised WhatsApp export |
| 012 | Sender mapping incomplete |
| 015 | Low-confidence lines not reviewed |
| 016 | Verification not permitted for this role or agent |
| 017 | Type copy disputed — resolve before filing |
| 020 | Language undetermined — choose a language |
| 021 | Locked term lost in translation — segment needs editing |
| 022 | Back-translation flags unreviewed |
| 025 | s.63 certificate not available for paper-document scans |
| 026 | s.63 feature not yet enabled (legal verification pending) |
| 030 | Certified translation required by the forum |
| 031 | No certified translator available for this pair — waitlisted |
| 035 | Engine regression gate failed (console) |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P05-01 | Verify BSA Schedule field labels and *Pune Bar Assn.* citation; enable `dix.bsa63.enabled` | `PLT_LEGAL_REVIEWER` / [COUNSEL] |
| OI-P05-02 | Bhashini terms of use, retention, residency and coverage; Google/Azure India-region zero-retention terms | `PLT_DPO` |
| OI-P05-03 | Per-forum translation certification rules (SC, HCs of launch States, consumer commissions) for P10 render profiles | [COUNSEL] / P10 |
| OI-P05-04 | Court-filing practice on masking non-party phone numbers in chat type copies | [COUNSEL] |
| OI-P05-05 | Bedrock India availability of the vision-capable Claude model chosen; latency and page cost baseline | P09 / P00 |
| OI-P05-06 | Licensing of Legislative Department glossaries and authoritative Hindi texts for glossary seeding | `PLT_CONTENT_EDITOR` |
| OI-P05-07 | Current WhatsApp export limits and advanced chat privacy behaviour | QA (device test) |
| OI-P05-08 | Baseline CER/chrF++ targets per language after the first evaluation run (confirm or revise §1 targets) | Evaluation lead |
| OI-P05-09 | Qualifying criteria for Part B "expert" beyond s.79A examiners | [COUNSEL] |

## Phase P06 — Template Library and AI Drafting Studio

**File:** `phases/P06_Template_Library_and_AI_Drafting_Studio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P03 (settings registry, `RULES_PORT` with GoRules ZEN/CEL, jurisdiction packs, State stamp/registration rule packs as data); P04 (Legal Vault: `doc_`/`ver_`, Object Lock, folder views, sharing); P09 runtime (Vidhi model gateway `packages/ai`, retrieval, citation resolver, guardrails, credit metering); P02 (maker-checker engine, roles, delivery grants); P01 (accounts, anonymous-to-registered conversion, consent artefacts). Consumers: P07 (CLM uses templates, clause library and playbooks), P08 (signing reads stamp/registration/eligibility metadata), P10 (Pleadings Studio reuses the template engine), P16 (review SKUs), P17 (credits, export quotas, prices), P21 (public document pages embed the drafting widget).
> **Sequencing:** Sprint 1–2: template schema, docgen, interview engine, 20 launch templates. Sprint 3–4: clause library, variants, language versions, export, Template Studio with maker-checker. Sprint 5–6: AI-custom lane, Vidhi tools, review gate, review SKU hand-off. Sprint 7–8: tenant templates/playbooks, analytics, content backlog, Wave 1 content load (Appendix E wave 1). **Freeze point:** the template schema (§4B) and clause object (§4D) freeze at the end of sprint 2 because P07, P08 and P10 bind to them.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and permissions), E (template, pleading and service taxonomy — the content load list), F (instrument eligibility gate), H (agent roster), K (`LD-EXPORT-1.0`), M (marketplace professional rules — for the review SKU), R (settings registry), W (open items).
> **Requirements covered:** R-004, R-006, R-007, R-008, R-009, R-010 (drafting part), R-019, R-027, R-030, R-038 (agreements, policies), R-045, R-046, R-047, R-070, R-071, R-087, R-090 (content quality), R-091.
> **Decisions applied:** D-04, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-11, CH-12, CH-14, CH-30 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-15, NN-18, NN-20, NN-28, NN-29, NN-30, NN-38, NN-45, NN-48, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, docgen/redline 1, AI 1, QA 1) plus 1 legal content analyst and the `PLT_LEGAL_REVIEWER` panel for content.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P06_Template_Library_and_AI_Drafting_Studio.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P06-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs wins or loses on its first draft. A person who lands on the "Residential Rent Agreement" page must leave with a fair, correct, State-aware draft in minutes, free; a company legal team must turn its own paper into a governed, reusable template without a developer. P06 builds the template library from the owner's Documents manual (~330 unique documents, 18 categories, 134 sub-categories — R5 §8.1; Appendix E resolves three further duplicates, leaving 327 canonical templates), the clause library, the guided interview with live preview, and the AI Drafting Studio with Vidhi.

The phase carries one legal line that the owner's brief blurs and that we hold firmly (CH-30, NN-14, R4 §6.4):

| Lane | What it is | Price | Gate |
|---|---|---|---|
| **Template automation** | A lawyer-authored, versioned template filled deterministically from the user's answers. No model writes document text. | Free on every public document page | None beyond the template's own reviewer of record |
| **AI-custom drafting** | Vidhi writes or rewrites clauses that are not in the vetted template | AI credits | Labelled **"AI draft — not reviewed by a professional"**; for individuals, no clean export, eStamp or eSign until a qualified reviewer approves (one-click paid review) |

The owner asked for "draft with AI free on every page". We implement it as free template automation plus paid, gated AI customisation. The reasons are the Anthropic Usage Policy treatment of preparing legal documents for individuals as high-risk (qualified human review before delivery, AI disclosure — R4 D-R4-09 [VERIFY effective date 12 Nov 2026]), the Advocates Act 1961 ss.29/33 boundary (R3 LG-110, LG-119), and NN-14.

**Outcomes and exit-gate measures**

| Outcome | Measure at exit |
|---|---|
| Library live | Appendix E wave-1 documents published with reviewer of record, effective date and law-as-of date; 0 published templates with an open outdated-law backlog item |
| Fast first draft | Median time from page load to downloadable draft ≤ 6 minutes for wave-1 templates; ≤ 3 taps from a document page to the first question |
| Neutral by design | 100% of platform templates pass the neutrality checklist (§4C) |
| Deterministic assembly | Same answers + same template version → byte-identical DOCX body (excluding metadata timestamps) in CI |
| AI clearly separated | 100% of AI-touched drafts carry the AI label and lane flag; 0 AI-custom drafts for individuals reach eSign or clean export without a review record (NN-14 test) |
| Review upsell | "Hire a professional to review" available from every draft in ≤ 2 taps; price shown before start (NN-50) |
| Content without code | A new template, clause, State variant or language version is published by content staff through maker-checker with no code release (NN-30) |
| Multilingual | Interview UI in the 10 launch languages (D-07); vetted language versions for the top 30 wave-1 templates in Hindi; bilingual side-by-side export |

---

### Integrations to respect

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `packages/ai` (P09) → Claude on Bedrock India | Vidhi tools, AI-custom drafting | Anthropic API for public/non-personal content only (e.g., Studio authoring helpers on public templates) | Tools disabled with banner; template lane unaffected | Template lane always works without AI |
| `TRANSLATE_PORT` | Draft translation | Bhashini [VERIFY], Google, Azure | Show "translation unavailable"; retry | Order certified translation (P16) |
| `packages/docgen` (docxtemplater, Gotenberg) | Assembly, PDF | LibreOffice headless | Queue and retry; DOCX still available | — |
| `packages/redline` | Tracked changes for AI/reviewer edits, version diffs | — | Block AI accept until healthy | Reviewer edits in DOCX upload |
| P16 marketplace SKU API | Review orders, assignment | — | Show wait-list | Ops assigns manually in delivery console (P18) |
| `BILLING_PORT` → OH8 (via P17) | Credits, export price, review payment | — | No charge without confirmed order | — |
| P21 CMS | Widget embed, page status, noindex control | — | Widget hidden; page shows static info | — |
| P03 `RULES_PORT` | CEL, stamp/registration packs | — | Assembly refuses if rules unavailable (no silent defaults) | — |
| P08 eligibility service (Appendix F) | Cached eligibility for display | — | Display "eligibility being checked"; P08 re-checks at signing | — |

---

### Exit gate, deliverables and open items

**Exit checklist**
- [ ] Template schema, clause object and questionnaire schema frozen and published as JSON Schemas in `packages/contracts`.
- [ ] Appendix E wave-1 templates published with reviewer of record, golden tests, neutrality checklist, sources, `law_as_of`; zero open blocking backlog items on published templates.
- [ ] Widget live on every wave-1 document page (P21) with SSR fallback text.
- [ ] AI-custom lane, escalation, review gate and P16 review SKU working end-to-end (individual and company paths).
- [ ] Vidhi tools of §4G live with credit metering and evaluation thresholds met.
- [ ] Hindi vetted versions for the top 30 wave-1 templates; bilingual export.
- [ ] Settings in §9 registered in Appendix R; help keys registered in `hlp`; error codes LD-TPL-001…040 and LD-DRF-001…040 registered with "i" keys.
- [ ] Export-map entries registered in `xpt.export_map`: `drf.draft` (DOCX + JSON answers) → Company `02 Agreements and Contracts/{<Entity>/}<FY>/{<Department>/}<Counterparty> - <Title> (LD-AGR-…)/01 Drafts/` (Appendix K §K.3.1) or, if not yet an agreement, `11 AI Work Products (labelled)/Outputs/<YYYY>/<draft ref>/` for AI-custom (Appendix K §K.11) and `02 Agreements and Contracts/Drafts not yet negotiated/` for template drafts [not yet in Appendix K — register through Appendix K owner]; Individual `08 Agreements/<Year>/<Category>/<Counterparty> - <Title> (LD-AGR-…)/01 Drafts/` or the life-area folder per `xpt.folder.individual_agreements_mode` (Appendix K §K.3.2); `drf.review` (PDF certificate + JSON) beside the reviewed version; `tpl.tenant_template` and `tpl.playbook` (DOCX + JSON) → `06 Policies and Registers/Contract Templates and Playbooks/` (X-12; Appendix K §K.3.1); machine translations → same folder as the draft, filename suffix "(machine translation – draft)".
- [ ] All Gherkin scenarios in §12 pass; NN tests for NN-01, NN-07, NN-08, NN-13, NN-14, NN-18, NN-30, NN-38, NN-48, NN-50 green.
- [ ] Accessibility audit (axe + manual NVDA/TalkBack) on SCR-P06-01/03/05/06/08 (NN-28).

**Demo script (15 minutes):** anonymous rent agreement on mobile in Hindi UI → sign up → clean download; add a sub-letting clause with Vidhi → escalation → paid review → approved → hand-off to P07 deal room; company CLO uploads house NDA, tags variables, publishes through checker; content editor fixes a CrPC → BNSS backlog item and publishes a new maintenance-petition version without a deployment.

**Error codes (initial set; full list in the error registry)**

| Code | Message (user) |
|---|---|
| LD-TPL-001 | This template version is not published. Please start from the current version. |
| LD-TPL-002 | A different reviewer must approve this version. |
| LD-TPL-003 | A reviewer of record is required before publishing. |
| LD-TPL-004 | An open legal-update item blocks publishing. Close it first. |
| LD-TPL-005 | The variable schema is invalid. See highlighted fields. |
| LD-TPL-006 | A rule refers to an unknown answer. Fix the rule or add the question. |
| LD-TPL-007 | A golden test failed. Review the expected output. |
| LD-TPL-008 | A cited source could not be verified. |
| LD-TPL-009 | State-specific terms are not verified for this State. |
| LD-TPL-010 | This language version has not been reviewed. |
| LD-TPL-011 | This template has been retired. See its replacement. |
| LD-TPL-012 | Complete the neutrality checklist. |
| LD-TPL-016 | The template contains a clause that is not allowed for this document type. |
| LD-DRF-001 | Some answers are still blank. Fill them to download a clean copy. |
| LD-DRF-002 | This change makes your document an AI draft that needs professional review. |
| LD-DRF-003 | An AI draft must be reviewed by a professional before signing or clean download. |
| LD-DRF-004 | You have used this month's free downloads. See the price to continue. |
| LD-DRF-005 | Only a reviewed language version can be the governing language. |
| LD-DRF-007 | You have no AI credits left. Buy credits or continue with the template. |
| LD-DRF-008 | This draft is locked while a professional reviews it. |
| LD-DRF-010 | This anonymous draft has expired. |
| LD-DRF-011 | Remove or fix unverified legal citations before review. |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P06-01 | Confirm with Anthropic account team whether AI pre-fill of a vetted template for individuals is outside the AUP high-risk legal definition (R4 OI-R4-05); keep `drf.template.ai_prefill.individuals` OFF until closed | Owner / `[COUNSEL]` |
| OI-P06-02 | Counsel view on in-app viewing and watermarked download of unreviewed AI drafts by individuals (`drf.ai_custom.unreviewed_download`) | `[COUNSEL]` |
| OI-P06-03 | Free clean-export quota and export price | `[OWNER]` |
| OI-P06-04 | Reconcile R5 eSign flags with R3 LG-003 (Entry 5 omitted 2022) for agreements to sell / conveyance / mortgage — Appendix E code "R" rows; Appendix F to decide routing per State e-registration | P08 owner / `[COUNSEL]` |
| OI-P06-05 | Near-duplicate merges (partnership deed family, release deeds) — approve the variant model | `[OWNER]` |
| OI-P06-06 | State variant priority list (top 10 States) and Model Tenancy Act adoption list [VERIFY] | `PLT_LEGAL_REVIEWER` |
| OI-P06-07 | Translator panel for vetted Hindi versions and the next nine languages | Ops (P16) |
| OI-P06-08 | ~~Appendix K: add `06 Policies and Registers/Contract Templates and Playbooks/` sub-folder~~ — closed by X-12 (Appendix K §K.3.1); remaining: register `02 Agreements and Contracts/Drafts not yet negotiated/` | Appendix K owner |
| OI-P06-09 | ~~Vidhi drafting agent name and autonomy row in Appendix H~~ — closed: `AGT_CONTRACT_DRAFTER` (Appendix H #2; X-27) | P09 owner |

## Phase P07 — Contract Lifecycle: Negotiation, Redlines, Deal Rooms, Messaging, Approvals

**File:** `phases/P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Vault/DMS: `doc_`/`ver_`, Object Lock, sharing, bulk intake); P06 (templates, clause library, position ladders, tenant playbooks, drafts); P02 (org structure, positions, DoA attributes, maker-checker engine, delivery grants); P03 (settings, `RULES_PORT` decision tables); P01 (accounts, `CP_GUEST` magic-link + OTP, step-up MFA); P09 runtime (Vidhi gateway, credit metering); P05 (OCR of scanned counterparty paper — Wave 2; until then PDF intake is text-layer only). Hand-off: P08 (eSign, eStamp, formalities, evidence). Later consumers: P11 (disputes from contracts), P13 (CLO dashboard, governance approvals, legal intake desk), P20 (export).
> **Sequencing:** Sprint 1–2: agreement record, deal room, guest access, messaging, version sharing. Sprint 3–4: `packages/redline` compare/accept/reject, rounds, silent-edit detection. Sprint 5: approvals/DoA, version lock, P08 hand-off. Sprint 6: obligations, key dates, renewals, amendments. Sprint 7: intake (form, email, Teams), repository views, legacy import, CLO dashboard. Sprint 8: company-to-company rooms, Office/Google co-editing, AI playbook redlines, hardening. **Freeze point:** the version/visibility model and change-record schema (§4F) freeze at the end of sprint 3 — P08 signs locked hashes from it.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (taxonomy for agreement types), F (instrument eligibility gate, owned by P08), H (agent roster), K (`LD-EXPORT-1.0`), R (settings), W (open items), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-006, R-007, R-011, R-018 (CLO/KMP agents, contract part), R-026, R-027, R-030, R-043, R-047, R-053, R-055, R-060, R-064, R-067, R-077, R-086 (SpotDraft/Ironclad/Leegality parity), R-091.
> **Decisions applied:** D-02, D-10, D-12, D-17 · **Challenges applied:** CH-12, CH-14, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-24, NN-28, NN-34, NN-37, NN-40, NN-43, NN-45, NN-46
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, redline/OOXML 1, integrations 1, QA 1).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P07_Contract_Lifecycle_Negotiation_Redlines_and_Deal_Rooms.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P07-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Two parties — two people, two companies, or one of each — must agree a text, know exactly what changed in every round, keep their internal discussion private, get the right internal approvals, and send the one agreed version to signature. After signing, the company must never miss a renewal, a notice window or a payment obligation. P07 delivers this as LawDocs' contract lifecycle (Ironclad's Create → Review → Approve → Sign → Store → Fulfil → Analyse, adapted — R1 §8), with deal rooms where parties message while negotiating (R-077) and a **deterministic** redline engine (NN-37).

The brief says "the tool sufficient instead of a legal team". We build the legal-operations layer a single CLO can run — intake, playbooks, approvals, obligations — with Vidhi as a maker and professionals on demand (CH-14, D-17). We do not claim it replaces advocates.

| Outcome | Exit-gate measure |
|---|---|
| Faster cycle | Median intake → locked version for NDAs ≤ 1 working day in pilot tenants; TAT measured per type |
| Every change accountable | 100% of changes between any two shared versions are listed with author, round and decision; accept/reject logged per change (NN-37) |
| No silent edits | 100% of untracked differences in a counterparty-returned DOCX are detected and shown (test corpus of 200 files) |
| Internal stays internal | 0 internal comments, internal versions or internal metadata in any file or view available to a counterparty (automated test on every share) |
| Right approvals | No version reaches signing without the approvals the DoA matrix requires for that version hash |
| Nothing lapses | Every executed agreement has verified key dates; renewal and notice-window reminders fire at configured offsets |
| Low friction for counterparties | A guest can review, comment, upload a redline and confirm the agreed version without creating an account, ≤ 3 taps from the invitation |

---

### Integrations to respect

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| Microsoft Graph (`int.m365`) | Edit in Word, Teams app/bot, Adaptive Card approvals | — | Disable co-edit button; Teams cards fall back to email links | Download/upload DOCX |
| Google Drive API (`int.gws`) | Edit in Google Docs (Office mode) | — | As above | Download/upload |
| Email-in (SES inbound or equivalent) | Intake, replies to threads ("reply to this email to post in the shared channel" — off by default) | — | Bounce with help link | Web form |
| P08 `sgn` | Signing hand-off, outcomes | — | Agreement stays `LOCKED_FOR_SIGNATURE`; retry | Wet-ink execution recording in P08 |
| P06 `tpl`/`drf` | Templates, playbooks, amendment templates | — | — | Upload own DOCX |
| P09 `ai` | Playbook review, extraction, summaries | — | Features hidden; manual review | Human review |
| P05 `dix` (Wave 2) | OCR of scanned paper | — | Mark "scan — text not available" | Manual metadata |
| P10 notice dispatch | Termination/renewal notices with proof of delivery | — | Record external dispatch with evidence | — |
| P19 `int` API/webhooks | Customer systems (ERP/CRM) create intake requests, receive status webhooks `in.lawdocs.clm.*` | — | Retries with backoff; dead-letter | — |
| CRM connectors (P19, Salesforce/Zoho — Ironclad pattern) | Create intake from an opportunity | — | — | Web form |

---

### Exit gate, deliverables and open items

**Exit checklist**
- [ ] `packages/redline` compare/apply engine at v1.x with ≥ 300-pair golden corpus (incl. Indic scripts), property tests (accept-all, reject-all, determinism) green.
- [ ] Deal rooms with guest access, internal/shared channels, leakage check and paste guard; NN-37 test suite green.
- [ ] DoA decision tables with maker-checker; approvals bound to hash; invalidation working.
- [ ] Lock and P08 hand-off with all gates; unlock path; wet-ink route for excluded instruments.
- [ ] Obligations/key dates with verification and reminders; renewal, amendment, termination flows.
- [ ] Intake via web, mobile, email-in and Teams app (pilot tenant consented); repository views; legacy import queue.
- [ ] CLO dashboard with data tables; company-to-company connected rooms; Word co-edit (M365) live; Google co-edit behind [VERIFY] warning.
- [ ] Settings (§9) registered in Appendix R; help keys registered; errors LD-CLM-001…060 and LD-MSG-001…020 registered.
- [ ] Export-map entries registered: `clm.agreements` + versions → `02 Agreements and Contracts/{<Entity>/}<FY>/{<Department>/}<Counterparty> - <Agreement title> (LD-AGR-…)/01 Drafts` (Appendix K §K.3.1) (internal drafts), `/02 Negotiation and Redlines` (shared versions, comparisons as redline DOCX/PDF, decision log CSV, issues list), `/05 Amendments and Renewals` (child agreements, renewal decisions), `/06 Correspondence` (shared thread as PDF + JSON; internal thread in a sub-folder "Internal (not shared)"); obligations and key dates → `Obligations.xlsx` at the agreement folder root (Appendix K §K.3.1) and `99 System Data (CSV and JSON)/Datasets/`; Individual equivalents under `08 Agreements/<Year>/<Category>/<Counterparty> - <Title> (LD-AGR-…)/` or the life-area folder (Appendix K §K.3.2). `<FY>` is the Indian FY label (`FY 2026-27`) for companies.
- [ ] Accessibility audit of SCR-P07-05/06/10/12/19 (NN-28).

**Demo script:** NDA request from Teams → auto-template → share with guest → guest edits without track changes → silent edit flagged → accept/reject per change → Vidhi playbook suggestions adopted → DoA approvals on mobile → both sides confirm → lock → P08 signing → obligations verified → renewal reminder in the CLO dashboard.

**Error codes (initial set)**

| Code | Message |
|---|---|
| LD-CLM-001 | This request type is not configured. Choose another or "Other". |
| LD-CLM-011 | You cannot invite participants to this room. |
| LD-CLM-013 | Invitation limit reached for this person. |
| LD-CLM-014 | This guest link has expired. Ask for a new invitation. |
| LD-CLM-021 | Sharing blocked: internal content found. Fix the listed items. |
| LD-CLM-022 | You can only compare versions you are allowed to see. |
| LD-CLM-024 | Acknowledge changes made without track changes first. |
| LD-CLM-031 | You cannot approve an agreement you prepared or under a delivery grant. |
| LD-CLM-032 | This approval is for an older version. Review the latest version. |
| LD-CLM-041 | This agreement cannot go for signing yet. See the failed checks. |
| LD-CLM-042 | A signed version cannot be unlocked. Create an amendment. |
| LD-CLM-051 | Verify key dates before reminders can be set. |
| LD-MSG-001 | You are not a member of this channel. |
| LD-MSG-004 | This message can no longer be edited. |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P07-01 | Microsoft Graph delegated permission set for app-folder co-editing and Teams app publishing (store vs org-only) [VERIFY] | Integrations lead |
| OI-P07-02 | Google Docs tracked-change ↔ suggestion round-trip fidelity [VERIFY] | Integrations lead |
| OI-P07-03 | Appendix Y change requests (drafted in Y §Y.7.1, §Y.7.4): LD as producer of `ADRReferralCreated` for non-loan disputes; `legal.AgreementExecuted` — awaiting Ecosystem Spec v1.2 acceptance | Pack lead / Ecosystem Spec owner |
| OI-P07-04 | Default DoA templates for SMEs and NBFC clients (align with LDC delegation registers where tenant uses LDC — NN-47) | `[OWNER]` |
| OI-P07-05 | WOPI editor licence ADR (ONLYOFFICE/Collabora) | Architecture |
| OI-P07-06 | Retention period for negotiation data beyond executed agreements (abandoned deals) | `PLT_DPO` / `[COUNSEL]` |
| OI-P07-07 | In-browser clause editor component choice and licence [REC ProseMirror/Tiptap-class] | Frontend lead |

## Phase P08 — eSign, eStamp, Execution and Evidence

**File:** `phases/P08_eSign_eStamp_Execution_and_Evidence.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identities, OTP/passkey sessions and step-up, `CP_GUEST`, KYC artefacts for signer identity binding), P02 (delegation of authority, authorised signatories, maker-checker), P03 (rule engine for the eligibility gate, duty rules and formalities; settings registry), P04 (frozen PDFs, executed versions under compliance-mode Object Lock, relationships, health checks), P06 (template answers → duty inputs, execution blocks), P07 (final agreed version, negotiation threads), P17 (credits, meters, duty pass-through presentation through OH8). External: eSign aggregator(s) and ESPs, eStamp vendor(s), DSC local signing agent, RFC 3161 timestamp authority, Razorpay via OH8.
> **Sequencing:** Wave 1. Sprint 1: provider registry, ports, licence monitor, eligibility gate (Appendix F runtime); sprints 2–3: signing ceremonies, Aadhaar eSign through the primary aggregator, consent, evidence capture; sprint 4: DSC agent, electronic acceptance, assisted and mobile signing, messaging; sprint 5: eStamp (attach existing e-stamp with UIN verification, then purchase), duty calculator (advisory), stamp-before-sign lock; sprint 6: formalities gate, wet-ink/notary/registration packs; sprint 7: evidence pack, certificate of completion, s.63 certificate service, validation, LTV, public verification; sprint 8: bulk signing, second ESP route, amendments/void flows, hardening and ASP audit readiness. **Freeze points:** port contracts (`ESIGN_PORT`, `ESTAMP_PORT`, `DSC_PORT`) end of sprint 1; Appendix F row schema end of sprint 1 (content can change any time after, NN-30).
> **Binding appendices:** F (instrument eligibility matrix and eStamp State coverage registry — runtime data; §9 supersedes the R5 eSign flags, X-02), A (state machines A.31–A.34), B (data model, events, errors), D (personas), U (accessibility), K (`LD-EXPORT-1.0`), R (settings), W (open items), Y (Ecosystem Spec change request — LD as producer).
> **Requirements covered:** R-006, R-009 (signing part; Aadhaar is never login), R-011 (enter, eSign, amend, preserve), R-039 (SLAs eSigned), R-077, R-078, R-067; contributes to R-017, R-025, R-035, R-054.
> **Decisions applied:** D-12, D-10, D-17 · **Challenges applied:** CH-01, CH-12, CH-13, CH-16, CH-28 · **Non-negotiables tested:** NN-03, NN-04, NN-06, NN-07, NN-08, NN-09, NN-10, NN-13, NN-18, NN-22, NN-24, NN-28, NN-34, NN-37, NN-38, NN-39, NN-40, NN-43, NN-45, NN-46, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, web 1, mobile 1, PKI/security engineer 1, integrations 1, QA/accessibility 1), plus a part-time legal analyst for Appendix F rows and State registry verification.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P08_eSign_eStamp_Execution_and_Evidence.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P08-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The brief's core promise is "two parties … enter into personal, business or property contracts by making Aadhaar-based eSign", with eStamp "buy … online or attach stamp papers, then eSign" (R-006, R-078). P08 delivers execution that a court will respect: the right instrument goes to the right method, stamp duty is paid **before** signing, formalities are tracked to completion, and every execution leaves an evidence pack with a BSA 2023 s.63 certificate draft (NN-10).

Two corrections to the brief are built in. (1) **Not every instrument can be eSigned**: the IT Act 2000 First Schedule (as amended by S.O. 4720(E) [VERIFY: Gazette text; S.O. dated 26 Sep 2022, published 4 Oct 2022 — Appendix W §W.9 LA-01]) excludes negotiable instruments other than cheques (with a regulated-entity carve-out), powers of attorney (with a regulated-entity carve-out), trusts, and wills/testamentary dispositions; registrable property instruments still need the sub-registrar (R3 LG-003, LG-104) **[LAW]** — CH-12, NN-07. (2) **LawDocs does not sell stamp paper**: certificates are issued only through the CRA (SHCIL) and authorised collection centres or State routes; LawDocs procures as the user's agent through a contracted vendor, passes duty through at actuals and discloses its own fee (R3 LG-098–100) — CH-13, NN-08.

| Outcome | Exit-gate measure |
|---|---|
| Lawful routing | 100% of signing requests pass the eligibility gate; 0 excluded instruments reach an ESP in the test corpus (all 35 R5 "not valid" templates plus wills/POAs/trusts/NIs uploaded as free documents) |
| Stamp before sign | 0 signing requests started for a chargeable instrument without a verified stamp record or a cited exemption |
| Fast signing | Median time from "Send" to all-signed ≤ 24 h for two-party Aadhaar eSign; signer completes in ≤ 4 taps + OTP on mobile |
| Resilient | ESP failover within one attempt; ≥ 99% successful completion for started Aadhaar eSign sessions excluding signer abandonment; routing never sent to an ESP whose licence date has passed without renewal evidence |
| Provable | Every completed execution has an evidence pack (hashes, consent versions, signer events, provider evidence, validation report, certificate of completion) and a s.63 Part A draft available in one click |
| Formalities complete | No document reaches `EXECUTED` while a required formality is open, unless waived by an authorised user with reason (NN-40) |
| Transparent money | Every checkout shows stamp duty (at actuals), LawDocs facilitation fee, ESP/eSign credits and GST separately, with the total before payment (NN-22, NN-50) |

---

### Integrations to respect

| Port | Primary (v1) | Secondary / alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `ESIGN_PORT` | One aggregator (Leegality / Digio / Melento / Surepass-type; selection by P00 ADR on ASP mode, ESP count, residency, log export, price — R6 B-16–B-26) | Second aggregator or direct ASP–ESP (Protean/eMudhra route, R6 D-24) | Failover per §4A; never move an in-flight session silently | DSC or wet ink |
| `DSC_PORT` | LawDocs signing agent (built or licensed component, signed installer) | Vendor desktop signer via aggregator | Agent missing → guide; no server-side key | Wet ink |
| `ESTAMP_PORT` | Aggregator's eStamp (e.g., Leegality BharatStamp claims 25–31 States/UTs; Melento 25+; Surepass 16 via SHCIL — vendor claims, R1/R6) | Second vendor per State | State paused; offer attach route or wet ink | Attach existing certificate; physical paper (wet ink) |
| `TSA_PORT` | CA-operated RFC 3161 TSA [VERIFY] | Second TSA | Queue timestamps; ESP-embedded timestamps remain | — |
| `BILLING_PORT` (OH8) | Credits, meters, duty pass-through lines, Razorpay Route split to vendor where used | — | Cannot start paid steps; signing of already-paid steps continues | — |
| `msg`, `ntf` | Threads, invitations (email/SMS/WhatsApp via DLT-registered CPaaS, NN-34) | — | Email fallback | Sender shares link manually |

Contract requirements for every vendor: India residency for documents and logs, log export on demand and at exit, consent/log retention aligned with eSign API (≥ 7 years after account deactivation for FIDO/public-key logs; R3 LG-008), ASP audit cooperation (CERT-In-empanelled auditor) [VERIFY frequency in ESP contract, LG-009], breach notice ≤ 6 hours, no use of LawDocs data for other purposes, kill-switch-friendly webhooks.

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] Ports and primary aggregator live; ASP mode recorded per vendor; second ESP/route live (≤ 30 days after first where LawDocs is ASP).
- [ ] Provider registry seeded from the CCA list; licence monitor active; Capricorn/Protean renewal evidence recorded or blocks in force.
- [ ] Eligibility gate at four points + DB CHECK; Appendix F rows for all launch templates published with reviewer of record; golden cases pass (P03).
- [ ] Aadhaar OTP eSign, account-based eSign (where supported), DSC agent, e-acceptance; assisted and mobile signing; messaging; bulk.
- [ ] eStamp attach route in all launch States; purchase route in States whose registry rows are `VERIFIED`; duty calculator rows for launch States × launch articles.
- [ ] Formalities gate with registration/notary tracking; wet-ink packs.
- [ ] Evidence pack, certificate of completion, validation, LTV, public verification; `Bsa63CertificateService` available to P05 (flag OFF until verified).
- [ ] Reconciliation jobs green for 14 days in staging; ASP audit readiness checklist complete [VERIFY audit frequency].
- [ ] Settings, help keys (`hlp.sgn.*`), errors and events registered; accessibility gate on SCR-P08-01…17 (assisted-signing journey tested with screen-reader users before GA).

**Demo script (12 minutes).** (1) Rent agreement agreed in P07 → gate `ESIGN_OK` with `STAMP_REQUIRED` → attach existing e-stamp, verify, merge → send. (2) Counterparty signs on a phone with Aadhaar OTP; name-match passes. (3) Company signs with DSC. (4) Evidence pack and certificate of completion; public verification by dragging the file. (5) Will template → `WET_INK_ONLY` → pack with two witnesses → upload scan → `EXECUTED`. (6) 3-year lease → `ESIGN_OK_REGISTRATION_ROUTE` → "Signed — formalities pending" with the four-month clock. (7) Console: Protean blocked on 27 Oct 2026 without renewal evidence; routing shifts. (8) Bulk send 200 offer letters.

**Export-map entries (`xpt.export_map`)**

| Record type | `LD-EXPORT-1.0` location |
|---|---|
| Executed instrument (`dms` version with `is_executed`) | Company: `02 Agreements and Contracts/<Year>/<Department>/<Counterparty> – <Title> (LD-AGR-…)/03 Signed and Stamped/`; Individual: `08 Agreements/<Year>/<Title> (LD-AGR-…)/Signed and Stamped/` (property instruments under `02 Property/`) |
| `sgn.stamp_instruments` + certificate | Same folder, `03 Signed and Stamped/Stamp certificate – <State> – <UIN>.pdf` + `stamp.csv` |
| `sgn.evidence_packs`, certificate of completion, validation reports, `sgn.bsa63_certificates` | `04 Evidence and Certificates/` (manifest, hashes, PDFs, provider evidence) |
| `sgn.signing_requests`, `participants`, `signature_events`, `consent_records` | `04 Evidence and Certificates/Signing record.xlsx` + `99 System Data (CSV and JSON)/signing/` |
| `sgn.formalities`, `appointments`, registration receipts | `03 Signed and Stamped/Registration and formalities/` + `formalities.csv` |
| Amendments / renewals / terminations | `05 Amendments and Renewals/` |
| Signing threads (if included) | `06 Correspondence/Signing messages.pdf` |
| `sgn.bulk_batches` | `07 People and HR/<Year>/Bulk letters – <batch>/` (company) + status report XLSX |

**Errors (`LD-SGN-001…050`)**

| Code | Meaning |
|---|---|
| 001 | Document not frozen/final — prepare for signing first |
| 002 | Document changed after freezing — request voided |
| 003 | Stamp required before signing |
| 004 | Stamp UIN verification failed |
| 005 | Stamp certificate mismatch (party, amount, or already used) |
| 006 | eStamp not available for this State — attach a certificate or use the wet-ink route |
| 007 | Duty estimate not verified (info) |
| 008 | Signing provider unavailable — try another method or later |
| 009 | Provider blocked (licence/contract lapse) |
| 010 | Consent not given |
| 011 | Signing attempt failed at the provider (generic; no Aadhaar detail) |
| 012 | Name mismatch — held for sender review |
| 013 | Signer lacks authority under delegation of authority |
| 014 | **Instrument not eligible for electronic signature** |
| 015 | Classification needed or suspect — reclassify with a reason |
| 016 | Electronic witnessing not permitted for this instrument |
| 017 | Notarisation required — use the print pack |
| 018 | Registration required — document cannot be marked executed yet |
| 019 | Formalities incomplete |
| 020 | This formality cannot be waived |
| 021 | Signing request expired |
| 022 | Declined by signer |
| 023 | Signing request cancelled |
| 024 | Bulk row invalid |
| 025 | Insufficient eSign credits |
| 026 | Stamp duty payment pending |
| 027 | Aadhaar number present in the document — mask before signing |
| 028 | Signature validation failed |
| 029 | Long-term validation refresh failed |
| 030 | DSC agent not detected |
| 031 | DSC certificate expired or revoked |
| 032 | DSC class not accepted |
| 033 | Electronic acceptance not permitted for this instrument |
| 034 | Signing on behalf of another application is not permitted |
| 035 | Signer must be an adult (or guardian where the row allows) |
| 036 | Changes requested — request voided; new round required |
| 037 | Exemption must be chosen from the cited list |
| 038 | Physical stamp paper cannot be combined with electronic signature |
| 039 | Assisted operator cannot act for a signer |
| 040 | Sandbox provider credentials in production blocked |
| 041 | Assistance consent and helper declaration required before assisted signing |
| 042 | Signer cannot perform the signing step personally — use the wet-ink route with signature by mark and witnesses |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P08-01 | Vendor selection ADR: ASP of record, ESP count, residency, log export, price; aggregator vs direct ASP timeline | P00 / Owner |
| OI-P08-02 | Capricorn and Protean CCA licence renewal evidence (R3 §17 item 11) | `PLT_SECURITY_OFFICER` |
| OI-P08-03 | Validity of combining a physical stamp paper with an electronically signed instrument; e-SBTR/GRAS proofs for electronic instruments | [COUNSEL] |
| OI-P08-04 | Who signs Part A of the s.63 certificate for platform-generated records; Part B expert criteria | [COUNSEL] |
| OI-P08-05 | Full white-label eSign for B2B tenants (RS-LD-17) vs ASP no-sub-letting (NN-06) | [COUNSEL] / ESP contract |
| OI-P08-06 | Organisation document-signer certificates and customer-held HSM option | `PLT_SECURITY_OFFICER` |
| OI-P08-07 | Face-authentication eSign availability and legal basis | `PLT_LEGAL_REVIEWER` |
| OI-P08-08 | GST pure-agent treatment of stamp duty and Route split design | [TAX MEMO] |
| OI-P08-09 | Electronic witnessing adequacy where attestation is legally required (TPA s.3 "attested") | [COUNSEL] |
| OI-P08-10 | State e-registration acceptance of eSigned instruments (launch States) | `PLT_LEGAL_REVIEWER` |
| OI-P08-11 | Stamp duty tables and e-stamp channels for launch States (Appendix F §5–§6) | `PLT_LEGAL_REVIEWER` |
| OI-P08-12 | eSign/eStamp credit prices and plan allowances | [OWNER TO SET] |

## Phase P09 — Vidhi AI Employee and Agent Workforce

**File:** `phases/P09_Vidhi_AI_Employee_and_Agent_Workforce.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, audit ledger, outbox, Temporal, S3 Object Lock, OpenTelemetry), P02 (tenancy, org structure, roles, maker-checker, delegations), P03 (settings registry, rule engine `rul`, jurisdiction packs — the deterministic engines Vidhi must call), P04 (Legal Vault/DMS — documents, versions, folders, permissions). Consumes read models of P05–P08 and P10–P16 as they ship and degrades to stated fallbacks when they do not exist. External: Amazon Bedrock (ap-south-1 ⇄ ap-south-2 `in.` geographic profile), Anthropic API (public content only), Keycloak (agent clients, token exchange), Cerbos, OpenSearch + pgvector, speech/translation adapters (`INDIC_SPEECH_PORT`, `TRANSLATE_PORT`), CPaaS adapters (Appendix J).
>
> **Sequencing:** **Wave 1 — runtime (4 sprints):** `packages/ai` gateway, routing, model registry, prompt registry, PII scrubber, citation resolver, retrieval over platform notebooks and the tenant vault, AI run ledger, credits meter, Qualified Review Gate (QRG) service and the individual Vidhi chat (general-information mode). Freeze point at end of sprint 2: the `AiGateway` TypeScript interface and the `vidhi_answer_v1` / `vidhi_draft_v1` schemas, so P05, P06 and P07 can call the runtime. **Wave 2 (3 sprints):** company Vidhi panel, embedded actions, agent workforce at L0–L2, approvals, kill switches, activity log and daily digest, MCP server (read + propose). **Wave 3 (3 sprints):** L3 envelopes for eligible agents, missions, schedules at scale, MCP client, A2A (behind the Appendix Y change request), voice intake agent, full multilingual evaluation suites.
>
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), H (Vidhi AI Agent Specification and Prompt Library), J (Jio Business Services and Telecom Rules), D (roles and permissions), F (instrument eligibility), K (`LD-EXPORT-1.0`), M (marketplace professional rules), R (settings registry), W (open items), Y (Ecosystem Spec v1.2 change requests).
>
> **Requirements covered:** R-007, R-008, R-010, R-015, R-018, R-019 (Vidhi "i" explanations), R-026, R-027, R-029, R-030, R-044 (runtime for type copy), R-045 (runtime for translation), R-047, R-060, R-061 (self-help triage), R-062, R-063 (AI hours-saved inputs), R-087 (runtime for "Draft with AI free" + "Hire a professional"), R-091.
>
> **Decisions applied:** D-01, D-05, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-11, CH-14, CH-17, CH-30 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-05, NN-11, NN-13, NN-14, NN-15, NN-18, NN-20, NN-21, NN-25, NN-28, NN-29, NN-32, NN-34, NN-38, NN-39, NN-43, NN-45, NN-46, NN-48
>
> **Estimated effort:** 10 two-week sprints (runtime 4 in Wave 1; 3 in Wave 2; 3 in Wave 3), squad of 8 (AI platform engineers 3, agent and tool engineers 2, retrieval/notebooks 1, evaluation and safety 1, full-stack UI 1; plus a part-time `PLT_LEGAL_REVIEWER` for golden sets and disclaimers).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P09_Vidhi_AI_Employee_and_Agent_Workforce.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P09-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Vidhi is LawDocs' AI employee (D-15). For an individual it is the first place to go with a legal problem: it listens in the user's language, explains the position in plain words, lays out the options, prepares the letter, notice, complaint or agreement, and — where the law or Anthropic's Usage Policy requires it — routes the work to a qualified professional before it is used. For a company it is a workforce of role agents that work beside the CLO, company secretary, CFO, CEO and the board: they read contracts, track hearings and trademarks, draft board papers and minutes, chase signatures, and report what they did every evening. Vidhi never replaces an advocate (D-17, CH-14); it makes a one-person legal function workable and makes self-help safe.

Four hard limits apply to every surface built in this phase:

1. **Acts for a named human, inside that human's permissions** (NN-01, NN-43). Agents have no standing rights.
2. **Cites or says it cannot** (NN-14). Every legal citation resolves against the rules register or a retrieved source or is shown as "unverified".
3. **Drafts and proposes; never decides or acts externally on its own** (NN-13, NN-43). Sign, pay, file, send, share outside the tenant, call, accept, withdraw and delete need a human's per-action confirmation.
4. **India-resident, no training, scrubbed** (NN-15, NN-25). Personal and client data goes only to the Bedrock India route.

| Outcome | Exit-gate measure |
|---|---|
| Individuals get an answer, not a menu | From the home screen, a user reaches a triaged, cited plain-language answer in ≤ 2 taps and ≤ 60 s p95 in any of the 10 launch languages (D-07); 100% of answers carry a dated source list or an "unverified" label; ≥ 90% of golden-set problems are routed to the correct track (DIY / notice / complaint / consult / court). |
| Safe self-help drafting | 100% of AI-custom drafts for individuals carry "AI draft — not reviewed by a professional" and cannot be sent for eSign or downloaded as "final" until the Qualified Review Gate records a review (NN-14; Anthropic Usage Policy legal High-risk Area, R4 D-R4-09). QRG standard turnaround ≤ 4 working hours p80. |
| Company workforce is governable | A tenant admin can hire an agent, name a sponsor, set its autonomy (L0–L2; L3 for eligible agents), budget and schedule in ≤ 6 clicks; pause it in ≤ 2 clicks with effect ≤ 60 s; every agent action appears in the activity log and the daily "What my AI employee did today" digest. |
| Grounded and accurate | On the Appendix H golden sets: citation validity 100% (no fabricated section, case or circular), number/date fidelity 100% in translations and summaries, correct-refusal rate ≥ 0.95 on out-of-corpus questions, triage accuracy ≥ 0.90; zero cross-tenant retrieval in canary tests. |
| Affordable | AI provider cost ≤ 40% of the credit price at the blended model mix (R6); 100% of runs metered to tenant/user/agent/mission with credits visible in Settings → Billing → Usage. |
| Interoperable | Customers' own assistants (Copilot, Claude, ChatGPT) can read their LawDocs matters, documents and calendars through the LawDocs MCP server as the signed-in user, with no prohibited tool exposed. |

---

### Integrations to respect

| Port / adapter | Primary | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `AI_PORT` → `bedrock-claude-in` | Amazon Bedrock `in.` profile (ap-south-1 ⇄ ap-south-2) | Sovereign open-weight route (Enterprise, flag OFF) | Queue or fail closed; never fall back abroad | Deterministic features continue; human drafting |
| `AI_PORT` → `anthropic-api` | Anthropic API (public content) | Bedrock India | Use Bedrock India | — |
| `AI_PORT` → `jio-*` | Stub OFF | — | — | Admission criteria: India inference and storage in writing, no training, retention ≤ 30 days or zero, SOC 2/ISO 27001, documented API with SLA, evaluation parity within 3 points (Appendix J) |
| `AGENT_RUNTIME_PORT` | In-house Temporal runtime | Claude Agent SDK / Managed Agents where available on the India route [VERIFY] | — | — |
| `EMBED_PORT` | Bedrock India embeddings [VERIFY model availability] | Self-hosted multilingual embedding model in ap-south-1 | Lexical-only retrieval with banner | — |
| `INDIC_SPEECH_PORT` | Sarvam [K] | Bhashini [VERIFY], Jio AI Cloud (OFF), Azure/Google India | Text-only mode | — |
| `TRANSLATE_PORT` | Owned by P05 | — | — | — |
| `VOICE_AGENT_PORT` | ElevenLabs Agents + Bedrock proxy [K] | Haptik (RFP; OFF), Sarvam | IVR fallback to human queue | Call-back request |
| `VOICE_PORT`, `TELEPHONY_PORT`, `COMMS_PORT` | Appendix J | Appendix J | Appendix J | Appendix J |
| `BILLING_PORT` | OH8 via `bil` | — | Meter buffers; no run blocked for billing outage < 24 h | Reconciliation job (NN-46) |
| MCP server/client, A2A | `int` gateway (P19) | — | Close sessions | — |

All external side effects carry idempotency keys and are reconciled (NN-46).

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] `packages/ai` interface frozen (sprint 2) and consumed by P05/P06/P07 stubs.
- [ ] Routing, scrubber, citation resolver, number/date validator, output filters live with tests; NN tests `tests/nn/NN-13_*`, `NN-14_*`, `NN-15_*`, `NN-39_*`, `NN-43_*` green.
- [ ] QRG service live with at least one reviewer pool and SLA timers; eligibility matrix signed off [COUNSEL].
- [ ] Platform notebooks published with reviewer of record (Statutes Register, Templates, Glossary, Forum Guides, Product Help).
- [ ] Agent catalogue loaded from Appendix H; hire/induct/review/retire, approvals, kill switches (≤ 60 s measured), activity log, digest demonstrated.
- [ ] Evaluation gates pass for English and Hindi on every Wave-1 agent; other languages gated OFF until their sets pass.
- [ ] Red-team suite passes; external red-team scheduled.
- [ ] Settings registered in Appendix R; help keys `hlp.ai.*`, `hlp.agt.*` registered in `hlp` with all launch-language text.
- [ ] AI Use Statement published (claims register).
- [ ] DPIA per route and agent; transfer register; vendor DPAs (AWS, Anthropic) reviewed by `PLT_DPO`.

**Demo script.** (1) Individual asks in Marathi about a withheld rent deposit → triage → cited general answer → options → template-lane notice → AI-custom clause added → QRG purchase → advocate review → stamped notice. (2) CLO hires Contract Drafter, Redline Negotiator and Obligation Tracker; runs a playbook review; approves an L2 obligation import; reads the digest; activates and releases the agent kill switch. (3) Copilot queries hearing dates via `ld-mcp`. (4) Fabricated citation and injection attacks shown blocked.

**Export-map entries (`xpt.export_map`; folder `11 AI Work Products (labelled)/` in every profile — Appendix K §K.3.1–§K.3.3 — plus `99 System Data (CSV and JSON)/`)**

| Record type | Path | Formats |
|---|---|---|
| `ai_conversation` | `11 AI Work Products (labelled)/Conversations/<YYYY>/<date> - <title> (aic_…)/` | PDF + JSON |
| `ai_output` (accepted and rejected) | `11 AI Work Products (labelled)/Outputs/<YYYY>/<record ref>/` | DOCX/PDF + JSON (sources, provenance) |
| `ai_qrg_review` | Alongside the reviewed document in its agreement/matter folder `…/01 Drafts/Reviews/` | PDF (attestation) + JSON (diff) |
| `agt_activity_log` | `11 AI Work Products (labelled)/Agent Activity/<Agent name>/<YYYY-MM>.xlsx` | XLSX + CSV |
| `agt_mission` | `11 AI Work Products (labelled)/Missions/<msn_…>/` | PDF summary + JSON |
| `ai_notebook` (tenant) | `11 AI Work Products (labelled)/Notebooks/<name>/` | JSON + source list CSV |
| `ai_memory_item` | `99 System Data (CSV and JSON)/ai_memory.json` | JSON |
| `ai_run_ledger_extract` | `99 System Data (CSV and JSON)/ai_runs.csv` | CSV (metadata, hashes; no provider secrets) |

**Open items**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P09-01 | Claude 5.5 models and prompt caching/batch/citations on Bedrock `in.` (R4 OI-R4-04) | CTO | Opus 5 / Sonnet 5 / Haiku 4.5; no-cache cost model |
| OI-P09-02 | Anthropic confirmation that template-lane fact extraction is outside the legal High-risk Area (OI-R4-05) | Owner/legal | `drf.template.ai_prefill.individuals` stays OFF (P06) |
| OI-P09-03 | Reviewer-eligibility matrix: reserved vs non-reserved document classes; employed professionals as reviewers (BCI Rule 49) | [COUNSEL] | Practising advocates only |
| OI-P09-04 | "Per-action confirmation" reading for enumerated send plans (NN-13) | [OWNER]/[COUNSEL] | `agt.send_plan.mode = per_message` |
| OI-P09-05 | AWS human review of flagged content on Bedrock — which models; DPA treatment | `PLT_DPO` | Exclude affected models from confidential classes |
| OI-P09-06 | MCP 2026-07-28 client support among target assistants (Copilot, ChatGPT, Claude) | Integration lead | Serve 2025-11-25 as well for 12 months |
| OI-P09-07 | A2A Appendix Y change request approval | Pack lead / group architecture board | Ecosystem events only |
| OI-P09-08 | Speech vendor bake-off (WER per language; India-only processing in writing) | AI lead | Text-only Vidhi for languages without a passing vendor |
| OI-P09-09 | Emergency helpline numbers and legal-aid links verified per State | `PLT_CONTENT_EDITOR` | Show 112 and NALSA only |
| OI-P09-10 | Privacy basis for sampled human review of free-tier answers | [COUNSEL] / `PLT_DPO` | Review only consented, de-identified items |

## Phase P10 — Pleadings, Notices and Court Drafting Studio

**File:** `phases/P10_Pleadings_Notices_and_Court_Drafting_Studio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P06 (template engine, questionnaire engine, clause library, lanes, review gate, export, Template Studio — reused, not rebuilt); P05 (originals, OCR, handwriting/WhatsApp type copies, translations as derived renditions `drv_`); P04 (Vault, Object Lock, hashes); P08 (eSign where permitted, BSA s.63(4) certificate drafts, evidence packs); P09 runtime (Vidhi, citation resolver); P16 (advocate review and "hire an advocate" SKUs); P03 (rule packs: limitation, court fees, forum profiles). Consumer: P11 (a filed pleading becomes a court case record).
> **Sequencing:** Sprint 1–2: forum render profiles, document anatomy, annexure builder, index/pagination, PDF/A e-filing pack. Sprint 3: pleading interview + library load (Appendix E §4 wave 1). Sprint 4: legal notices and replies with dispatch and proof of delivery. Sprint 5: limitation and jurisdiction prompts, party-in-person mode, advocate review gate. Sprint 6: affidavit/verification routes, vakalatnama, P11 hand-off, hardening. **Freeze point:** render-profile token schema at the end of sprint 1 (P11 and P15 reuse it).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles), E (§4 pleadings taxonomy; §7 outdated-law backlog), F (eligibility gate — affidavits and verifications are never eSign-only), H (agents), K (`LD-EXPORT-1.0`), M (marketplace rules for advocate SKUs), R (settings), W (open items).
> **Requirements covered:** R-012 (pre-filing part), R-044, R-045, R-061, R-079, R-084 (notice and court-drafting part), R-087, R-090, R-091.
> **Decisions applied:** D-05, D-06, D-07, D-17 · **Challenges applied:** CH-11, CH-14, CH-28, CH-30 · **Non-negotiables tested:** NN-05, NN-07, NN-09, NN-10, NN-11, NN-13, NN-14, NN-20, NN-28, NN-34, NN-38, NN-41, NN-48
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 2, frontend 2, docgen/PDF 1, AI 1, QA 1, legal content analyst 1) plus advocate reviewers from the `PLT_LEGAL_REVIEWER` panel.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P10_Pleadings_Notices_and_Court_Drafting_Studio.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P10-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Individuals facing a dispute and companies running litigation need court-ready documents: a properly formatted plaint or petition, a list of dates, a verified affidavit, a vakalatnama, annexures marked P-1, P-2 with typed copies of handwritten notes and WhatsApp screenshots and their translations, and a legal notice sent with proof of delivery. P10 delivers a Pleadings, Notices and Court Drafting Studio on the P06 engine, loaded from the owner's Pleadings manual (13 areas, 89 drafts → 70 consolidated pages — X-23 supersedes R5 §8.2's ≈68; FR-P10-01; Appendix E §4), **updated to the new criminal laws** (BNS, BNSS, BSA in force 1 July 2024), CPC 1908, Commercial Courts Act 2015 and Consumer Protection Act 2019.

Two lines we hold (and say plainly to the owner):
1. **LawDocs prepares documents; it does not file, argue or advise.** Filing, appearance and advice are for the party in person or an enrolled advocate (Advocates Act 1961 ss.29, 33 — R3 LG-110; NN-41). No auto-filing on any court portal and no portal automation (NN-05, NN-13). The manual's line "file directly before any High Court and Supreme Court" is withdrawn.
2. **AI-assisted court documents for individuals pass a qualified-review gate** before final download (NN-14, R4 §6.4 "pleadings self-help" row), and every AI-assisted document carries a disclosure line.

| Outcome | Exit-gate measure |
|---|---|
| Correct format | Exports validate against the selected forum render profile (page size, margins, font, spacing, numbering); unverified profiles never labelled "court-ready" |
| Correct law | 0 published pleading templates citing CrPC/IPC/Evidence Act/CPA 1986 as current law; old→new mapping shown where users search old sections |
| Annexures right | Every annexure referenced in the text exists in the index and vice versa; typed copies and translations sit next to their originals with labels; BSA s.63(4) certificate draft generated for each electronic-record annexure |
| Filing pack | PDF/A-2b, OCR text layer, bookmarks from index, continuous pagination, size split per profile — validated by veraPDF in CI |
| Notices with proof | Legal notices dispatched only after human confirmation, with dispatch evidence (India Post tracking, email delivery) attached to the notice record |
| Safe self-help | Party-in-person mode shows forum-specific disclaimers, legal-aid route and "hire an advocate" path at every final step |

---

### Integrations to respect

| Port | Use | Failure / fallback |
|---|---|---|
| `packages/docgen` + Gotenberg + veraPDF | Rendering and validation | Block pack until valid; DOCX still downloadable |
| P05 `dix` | OCR, type copies, translations | Annexure marked "type copy pending"; manual typing allowed |
| `TRANSLATE_PORT` / certified translation SKU (P16) | Convenience vs certified translations | Block where certified is mandatory |
| Postal/courier booking partner (`DISPATCH_PORT`) [VERIFY vendor and API] | Notice dispatch and tracking | User posts and uploads receipt; manual tracking entry |
| Email (`packages/notify`, SES) | Email notices with delivery evidence | Retry; record failure |
| P16 marketplace | Advocate review, settle-and-sign, appearance, notarisation facilitation | Wait-list with ETA |
| P11 `lit` | Case creation on filing | Queue and retry |
| Court portals | **None** — no integration, no automation (NN-05) | — |

---

### Exit gate, deliverables and open items

**Exit checklist**
- [ ] Render profiles seeded; `SC_2020_PRINT` verified; others flagged; profile manager with maker-checker.
- [ ] Appendix E §4 wave-1 pleadings published on the new laws with reviewer of record; outdated-law backlog for pleadings at zero for published items.
- [ ] Annexure builder with originals/type copies/translations and s.63(4) Part A drafts.
- [ ] Filing pack validated by veraPDF; splits and bookmarks correct.
- [ ] Notices with dispatch confirmation and proof; s.138 and s.80 helpers on verified rows.
- [ ] Limitation engine with verified rows only showing dates; court-fee calculators only for verified States.
- [ ] Party-in-person mode with legal aid and advocate paths; review gate and criminal-area rule.
- [ ] Settings (§9) in Appendix R; "i" keys registered; errors LD-PLD-001…040 registered.
- [ ] Export-map entries: `pld.project` + filing pack + annexures + certificates → Company `03 Litigation and Disputes/<Year>/<Forum>/<Case title> (LD-CAS-…)/` (pre-filing drafts in `03 Litigation and Disputes/Drafts not yet filed/`); `pld.notice` + dispatch proof → `08 Notices and Correspondence/<Year>/<Counterparty> – <Notice type> (LD-NTC-…)/`; Individual `07 Disputes and Court Cases/…` and notices under `07 Disputes and Court Cases/Notices/`; AI work products labelled in `11 AI Work Products (labelled)/` for companies.
- [ ] Gherkin §12 green; NN tests NN-05, NN-09, NN-10, NN-13, NN-14, NN-38, NN-48 green; accessibility audit on SCR-P10-02/05/07/08.

**Error codes (initial set)**

| Code | Message |
|---|---|
| LD-PLD-001 | Choose the forum before continuing. |
| LD-PLD-010 | Some facts have no source. Link a document or mark as your own knowledge. |
| LD-PLD-012 | Amounts or dates do not match your chronology. |
| LD-PLD-014 | A legal reference could not be verified. |
| LD-PLD-015 | An annexure referenced in the text is missing from the index (or the reverse). |
| LD-PLD-016 | Add the s.63(4) certificate for this electronic record. |
| LD-PLD-018 | This court needs a certified translation for this annexure. |
| LD-PLD-021 | A page reference could not be resolved. |
| LD-PLD-025 | The page layout does not match the selected court profile. |
| LD-PLD-031 | Confirm the dispatch details to send this notice. |
| LD-PLD-035 | The sworn affidavit does not match the approved text. |

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P10-01 | Verify render profiles for Delhi HC, Bombay HC, Karnataka HC, Madras HC, Allahabad HC, Punjab & Haryana HC and district courts of the top 10 States [VERIFY] | `PLT_LEGAL_REVIEWER` |
| OI-P10-02 | Verify each limitation seed row (Limitation Act articles; s.166(3) MV Act commencement; Insurance Ombudsman conditions) | `PLT_LEGAL_REVIEWER` |
| OI-P10-03 | Court Fees Act schedules by State (top 10 first) | `PLT_LEGAL_REVIEWER` |
| OI-P10-04 | Postal/courier dispatch partner with tracking API and proof-of-delivery artefacts [VERIFY vendor] | Ops / integrations |
| OI-P10-05 | Commission the content-gap drafts (Appendix E §4.3) and decide writ skeleton scope (advocate-only) | `[OWNER]` |
| OI-P10-06 | Counsel view on party-in-person support boundaries (staff help limited to platform mechanics; no drafting for the user by LawDocs staff who are not engaged advocates) | `[COUNSEL]` |
| OI-P10-07 | Consumer Commission portal: e-Daakhil vs e-Jagriti current state and file limits [VERIFY] | P15 owner |
| OI-P10-08 | BNS s.358 / BNSS s.531 savings and transition text for the pre-1 July 2024 toggle [VERIFY] | `PLT_LEGAL_REVIEWER` |

## Phase P11 — Litigation and Matter Management

**File:** `phases/P11_Litigation_and_Matter_Management.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P02 (organisations, departments, maker-checker, delegations), P03 (settings registry, `RULES_PORT`, limitation and forum rule packs), P04 (Legal Vault: folders, versions, legal hold, bulk folder intake), P05 (OCR, type copies and translation of orders and notices), P09 runtime (Vidhi agents `AGT_LITIGATION_CLERK`, `AGT_ORDER_DIGEST`, `AGT_HEARING_PREP`, `AGT_EVIDENCE_CLERK`, `AGT_NOTICE_RESPONDER`), P10 (notice register `ntc_`, pleadings `pld_`, annexure and bundle builder), P16 (marketplace engagements of advocates), P17 (plan limits, meters, add-on `LD-ADD-LIT`), P19 core (`int` gateway, connector framework, ecosystem inbox/outbox), P20 core (export map), P22 (push). External: two licensed court-data aggregators (contracts pending), Equator Resolution (ADR referral contract — Appendix Y), Finbyx/Udofin Recovery Suite (litigation events, Ecosystem Spec §6.10), LawDocsComply (when the tenant uses it).
> **Sequencing:** Wave 2. Sprint 1–2: matter/case model, forum registry, manual CNR, vault folders; freeze the `lit` read API (`GET /v1/lit/matters`, `/v1/lit/cases`, `/v1/lit/clocks`) at the end of sprint 2 for P12 (oppositions as matters) and P13 (CLO dashboard, board MIS). Sprint 3–5: court-data adapters, hearings, cause lists, orders, deadline engine. Sprint 6–7: counsel, spend, exposure, bundles, bulk import, individual view. Sprint 8–9: Equator referral, ecosystem projections, reports, mobile, hardening. The second court-data vendor can follow in Wave 2's last sprint (R6 §R6.6.6 v1.1).
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles and access matrix), H (agent roster), K (`LD-EXPORT-1.0` folder taxonomy), M (marketplace professional rules), R (settings registry), T (legal-department operating model and intake SLAs), W (verification log and open items), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-002, R-012, R-017, R-019, R-021, R-023, R-026, R-027, R-030, R-047, R-060, R-061, R-062 (alerts), R-067, R-068, R-076, R-083 (status tracking for consumer cases that reach a forum), R-086.
> **Decisions applied:** D-02, D-05, D-07, D-10, D-14, D-15, D-17 · **Challenges applied:** CH-08, CH-14, CH-16, CH-27, CH-28, CH-31 · **Non-negotiables tested:** NN-01, NN-02, NN-05, NN-09, NN-10, NN-11, NN-13, NN-14, NN-17, NN-19, NN-20, NN-21, NN-24, NN-28, NN-29, NN-30, NN-34, NN-38, NN-39, NN-43, NN-45, NN-46
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, frontend 2, mobile 1, QA 1, integration 1) plus a part-time legal domain analyst (advocate with corporate and recovery litigation experience) and a chartered accountant for the exposure schedule.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P11_Litigation_and_Matter_Management.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P11-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Indian companies run litigation from spreadsheets, counsel e-mails and the eCourts app one case at a time. Individuals do not understand what "Stage: Appearance — next date 14.01.2027" means or what they must do next. This phase builds a Provakil-class matter and case management system (R1 §5; IMP-060 to IMP-069) for both audiences:

- **Companies:** one register of every dispute and pre-dispute (notices, suits, writs, arbitrations, consumer complaints, tribunal and regulatory proceedings), with hearings, cause lists, orders turned into tasks, limitation and order-compliance clocks, counsel and spend control, exposure estimates for the financial statements, document bundles and board/audit-committee MIS.
- **Individuals ("My cases"):** add a case by CNR or case number, see the status in plain language in their language, get reminders, keep every paper in the Legal Vault, and hire a professional when they need one.

LawDocs is a technology and legal-operations platform. It does not appear in court, give legal advice or file anything on anyone's behalf (NN-41, CH-14). Court data comes only from licensed sources or the user (NN-05, CH-27).

| Outcome | KPI and exit-gate measure |
|---|---|
| No missed date | 100% of active cases have an owner and a next date or an explicit "date awaited" status; missed-hearing-outcome rate < 2% after 48 hours in pilot; 0 missed limitation clocks in UAT |
| Data is honest | Every court-sourced field shows source, fetched-at time and a staleness label; 0 screens use "real-time", "live", "official" or "certified" for vendor data (NN-20) |
| Orders become actions | An uploaded order produces a confirmed digest and tasks in ≤ 3 clicks; 95% of directions have an owner within 1 business day |
| Company control | Board MIS and quarterly exposure schedule produced in ≤ 10 minutes for a 300-matter tenant; counsel invoice validated against budget before approval |
| Onboarding speed | 500-row Excel import with CNR de-duplication, preview and undo in < 5 minutes |
| Individual clarity | "What this status means / what happens next" shown for 100% of seeded status codes in the 10 launch languages (D-07) |
| Boundaries kept | Recovery cases from the Recovery Suite appear only as read-only projections; 0 LawDocs writes to recovery records (Ecosystem Spec §6.10) |

**Done for users.** A CLO opens Litigation Home, sees today's cause-list matches, overdue outcomes and clocks under 30 days, and clears them from one screen. An individual opens the app, taps "My cases", and reads "Your case is listed on 14 January 2027 before Court No. 4. The court will hear arguments on your application. Bring: copy of the agreement, payment receipts."

### Integrations to respect

| Port / adapter | Use | Vendor alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `COURT_DATA_PORT` → `LicensedAggregatorA/B` | Status, orders, cause lists, party search (optional) | eCourtsIndia API, Surepass eCourts API, Claw, Legitquest-type (R6 D-08) [VERIFY coverage, terms, residency] | Failover A → B; then manual mode with daily notice | `ManualCNR`; cause-list PDF upload |
| `COURT_DATA_PORT` → `eCourtsOfficialApi` | Client-credentialed eCourts Open API | NIC eCourts (restricted) | OFF until eligibility verified | — |
| `WORKSPACE_PORT` | Calendar sync, Teams/Meet links for internal hearing prep, mailbox for invoices | Microsoft Graph (least-privilege scopes), Google Workspace (R6 D-28/29) | Queue and retry; banner | ICS download |
| `NOTIFY` (`packages/notify`) | Alerts and digests | SES/Brevo; JioCX and other DLT CPaaS; WhatsApp Cloud API; Expo push | Channel fallback order per user | In-app only |
| `ECOSYSTEM` (`int`) | RS litigation events; ADR via `ODR_PORT` (Equator one provider); LDC `legal` projections | Ecosystem Spec §6.9, §6.10, §6.13 | Inbox parking and replay; reconciliation breaks | P19 interim manual channel (signed pack) |
| `ACCOUNTING_PORT` | AP export of approved invoices; exposure schedule | CSV/XLSX; ERP connectors (P19) | Retry; file download | Manual download |
| `TRANSLATE_PORT` / `dix` | Order type copies and translations | Bhashini [VERIFY], Google, Azure | Labelled "translation unavailable" | Certified translation service via P16 (NN-48) |
| `BILLING_PORT` (OH8) | Meter `COURT_DATA_REFRESH`, plan limits, add-on `LD-ADD-LIT` | — | Usage buffered and reconciled | — |

Vendor onboarding checklist (P19 connector certification): licence and lawful-collection warranty; DPDP processor terms; residency (India); security questionnaire; SLA; incident notice ≤ 6 hours (to meet CERT-In reporting, NN-27); termination data deletion; no resale conflict; pricing per refresh; coverage list. No adapter goes live without certification (Ecosystem Spec §14.3 certification suite).

### Exit gate, deliverables and open items

**Deliverables:** `lit` module with migrations (expand/contract, NN-12); forum registry seed (SC, all HCs and benches, district courts by State, NCLT/NCLAT, DRT/DRAT, consumer commissions, RERA, major tribunals); status mapping tables for both vendors; clock rule pack seed with verification log entries; status explainer glossary (10 languages) with reviewer of record; Excel template `LD-TPL-LIT-v1.0`; task templates per matter type; report definitions LIT-01–LIT-11; counsel portal; certified court-data adapters (A at minimum); RS projection consumer behind flag; Equator deep-link fallback; user guides (CLO, legal maker, counsel portal, individual "My cases"); tutorial scripts for "Add a case by CNR" and "Turn an order into tasks" (P21 video plan).

**Exit checklist:**
1. All `@P11-AT-*` scenarios and listed NN tests green in CI.
2. Pilot company: 300 matters imported with CNR de-duplication; 30 days of cause-list matching on covered forums; one order converted to tasks per pilot user; one quarterly exposure schedule frozen and exported.
3. Pilot individuals: 50 users add cases on mobile; explainer coverage 100% for statuses seen.
4. Vendor A certified (contract terms in §8 checklist), Vendor B contract in progress or certified; kill switches tested.
5. Every clock rule used in pilot VERIFIED or advisory-badged, logged in `docs/compliance/verification-log.md` (NN-38).
6. WCAG 2.2 AA and IS 17802 audit (axe + NVDA/TalkBack manual) of SCR-P11-03, -04, -06, -08, -15, -16 (NN-28).
7. Settings in §9 registered in Appendix R; help keys `hlp.lit.*` registered in `hlp`.
8. **Export-map entries registered (NN-11):** record types `lit.matter`, `lit.case`, `lit.docket_entry`, `lit.hearing`, `lit.order`, `lit.order_direction`, `lit.clock`, `lit.counsel_assignment`, `lit.spend_invoice`, `lit.budget`, `lit.exposure_schedule`, `lit.bundle`, `lit.adr_referral`, `lit.rs_projection` (as read-only mirror, labelled). Company path: `03 Litigation and Disputes/<Year of filing or opening>/<Forum>/<Case title> (LD-CAS-…)/{01 Pleadings, 02 Orders and Judgments, 03 Hearings and Cause Lists, 04 Notices and Replies, 05 Evidence, 06 Counsel and Costs, 07 Settlement and ADR, 08 Internal Notes (Privileged), 09 Bundles}` plus `03 Litigation and Disputes/Matter Register.xlsx`, `Hearings.xlsx`, `Deadlines.xlsx`, `Exposure Schedule <FY> <Qn>.xlsx`; pre-litigation matters under `03 Litigation and Disputes/<Year>/Pre-litigation/<Matter title> (LD-MAT-…)/`. Individual path: `07 Disputes and Court Cases/<Year>/<Case title> (LD-CAS-…)/…` with the same sub-folders minus 06 and 08 unless used. Privileged folders are included in the tenant's own export and flagged in the README. [Proposed sub-folder names for Appendix K owner.]
9. Demo script: CLO morning routine (Litigation Home → today's list → record outcome from counsel link → confirm order digest → approve invoice → open board section), individual journey (add by CNR → explainer in Marathi → hire advocate), RS projection display, ADR referral through the interim signed pack.

**Error codes introduced (`LD-LIT-001`–`LD-LIT-026`):** 001 Identifier format invalid · 002 Duplicate case · 003 Plan case limit reached · 004 Court-data source unavailable — manual mode · 005 Refresh credits exhausted · 006 Forum not covered by a licensed source · 007 Case managed in Recovery Suite (read-only) · 008 Clock rule unverified — advisory · 009 Open clock blocks closure · 010 Open direction blocks closure · 011 Contingency/success fee not permitted for advocates · 012 Counsel not assigned to this matter · 013 Invoice exceeds budget — approval required · 014 Exposure values must be entered by a person · 015 Exposure schedule frozen · 016 ADR pre-check failed · 017 ADR contract not live — use the interim signed pack · 018 Import row errors · 019 Undo window expired · 020 Channel consent missing · 021 Privileged document not shareable under this grant · 022 Matter system of record is LawDocsComply · 023 Agents cannot perform external actions · 024 Party watch needs a licensed adapter · 025 Prohibited claim wording in template · 026 Bundle exceeds forum size limit. Each has user text and `hlp.lit.err.<nnn>`.

**Open items (Appendix W):**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P11-01 | LDC v1.3 to align with D-10: LawDocs SoR for matters; LDC consumes projections (conflict with LDC D-41/P26) | [OWNER] + LDC pack lead | `lit.sor.mode` per entity |
| OI-P11-02 | Platform vs client eligibility for eCourts Open APIs | Integration lead + [COUNSEL] | Adapter OFF |
| OI-P11-03 | Vendor party-search/new-filing alerts: contract terms, DPDP purpose | CLO advisor + DPO | Party watch OFF |
| OI-P11-04 | Verify every clock rule seed in §4F (Limitation Act articles, special statutes, Income-tax Act 2025 appeal section, GSTAT start) | Legal domain analyst | Advisory badge |
| OI-P11-05 | Ind AS 37 / AS 29 paragraph references and Schedule III Division mapping | CA reviewer | Text without paragraph numbers |
| OI-P11-06 | TDS section for professional fees under the Income-tax Act 2025 | [TAX MEMO] | Field captured, validation advisory |
| OI-P11-07 | Appendix Y items this phase depends on (tracked by P19): §Y.7.4 ADR referral fields, §Y.7.5 LawDocs as consumer of Spec §6.10, §Y.14 `legal` domain projections to LDC with LDC P26 consuming them | Integration lead | Flags OFF; P19 interim manual channel |
| OI-P11-08 | Internal counsel scorecards vs BCI Rule 36 | [COUNSEL] | Scorecards hidden by default |
| OI-P11-09 | CNR structure and QR content for scan-to-add | Product analyst | Manual entry |
| OI-P11-10 | Forum filing-size limits for bundle checks | Legal domain analyst | Warning only |
| OI-P11-11 | New ID prefixes `clk_`, `cnl_`, `lsi_`, `exa_` to be added to conventions §5 / master | Pack lead | Use as proposed |

## Phase P12 — IP and Trademark Portfolio

**File:** `phases/P12_IP_and_Trademark_Portfolio.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (Legal Vault, bulk intake, legal hold), P05 (OCR and extraction of examination reports, Journal pages and registry e-mails), P06 (templates: assignment, licence, co-existence, user affidavit), P07 (CLM for IP licences and assignments; obligations), P08 (stamp-before-sign and eSign for IP deeds), P09 runtime (`AGT_TM_WATCH`), P11 (oppositions, rectifications, infringement and appeals as matters; deadline engine; frozen `lit` read API), P14 (Startup Desk bundles), P16 (marketplace filing and opinion SKUs delivered by trade marks agents and advocates), P17 (plan limits, add-on `LD-ADD-TMW`, AI credits), P19 (`TRADEMARK_DATA_PORT` adapters, IP mailbox), P20 (export map). External: WIPO Global Brand Database (terms [VERIFY]), a licensed trademark data and Journal-watch partner (not yet selected [VERIFY]).
> **Sequencing:** Wave 2, after P11 sprint 2 (deadline engine and matter API frozen). Sprint 1–2: asset model, trademark register, status taxonomy, deadline rules, manual and assisted refresh. Sprint 3–4: clearance assistance, filing-support service hand-off, examination and hearing workflow, renewals. Sprint 5: Journal watch (partner or manual upload), copyright/design/patent/domain registers. Sprint 6: licences and assignments, reports, mobile, hardening.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export taxonomy), M (marketplace professional rules), R (settings), T (intake categories and SLAs for IP requests), W (verification log and open items).
> **Requirements covered:** R-013, R-017, R-019, R-021, R-027, R-030, R-037, R-061, R-075, R-082, R-086.
> **Decisions applied:** D-05, D-10, D-11, D-14, D-15, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-27 · **Non-negotiables tested:** NN-01, NN-02, NN-05, NN-08, NN-09, NN-11, NN-13, NN-14, NN-20, NN-21, NN-22, NN-29, NN-30, NN-38, NN-39, NN-43, NN-46
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 3, frontend 2, data/ML 1 for similarity, QA 1, integration 1) plus a part-time IP domain analyst (advocate or registered trade marks agent).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P12_IP_and_Trademark_Portfolio.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P12-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Startups and SMEs file trademarks through aggregators and then lose track: the examination report goes to the agent's address for service, the one-month reply window (Trade Marks Rules 2017 r.33(4)) passes, the application is abandoned, or the ten-year renewal is missed. IP India offers status lookups behind an OTP, a weekly Journal and e-filing, but no portfolio view, alerts or similarity watch (R1 §7.1). Nobody combines **portfolio tracking + deadline engine + Journal watch + reply drafting + professional filing** for an SME at a low price (R1 key finding 8).

This phase builds that portfolio for companies and individuals (sole proprietors, founders, creators), centred on trademarks with lighter registers for copyrights, designs, patents and domain names, and links IP disputes to P11 and IP agreements to P06/P07.

| Outcome | KPI and exit-gate measure |
|---|---|
| No lost application or registration | Every asset has a normalised status, last-refreshed time and a computed next deadline; 0 missed deadlines in UAT; renewal tasks created ≥ 12 months before expiry |
| Honest status | Every status shows its source (user, agent, assisted refresh, licensed partner, WIPO route) and staleness; no "live", "official" or "real-time" wording (NN-20) |
| Faster filing | From "I want to protect my brand" to a filing-ready TM-A data sheet handed to an agent in ≤ 15 minutes and ≤ 8 screens |
| Watch that matters | Journal hits reviewed with ≥ 30 days left in the 4-month opposition window for 95% of hits in pilot |
| Clean boundaries | LawDocs never files with IP India, never handles the eRegister OTP and never automates the IP India portal (NN-05, NN-13) |

### Integrations to respect

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `TRADEMARK_DATA_PORT` → `ManualAppNo`, `AssistedRefresh`, `RegistryMailParser` | Status capture | — | Extraction failure → manual form | Always available |
| `TRADEMARK_DATA_PORT` → `WipoBrandDb` | Screening and status cross-check | WIPO data licence; licensed partner [VERIFY] | OFF; screening limited to own portfolio | Own portfolio + professional search SKU |
| `TRADEMARK_DATA_PORT` → `LicensedPartner` | Status sync and Journal watch | Partner TBD [VERIFY] | Kill switch (NN-39); fall back to manual upload | `MANUAL_UPLOAD` journals |
| `dix` / `TRANSLATE_PORT` | OCR of Journal PDFs, reports, e-mails; transliteration variants | Tesseract/PaddleOCR + Claude vision (Bedrock India) | Partial parse flagged | Manual entry |
| `ai` gateway | Class finder, screening explanation, reply outlines | Claude via Bedrock India (D-14) | AI unavailable banner | Class list browser |
| `mkp` (P16) | Filing, reply, renewal, opinion, watch-review SKUs | — | Order failure → retry | Own agent recorded manually |
| `BILLING_PORT` (OH8) | Plan limits, `LD-ADD-TMW`, AI credits, government fee pass-through | — | Buffered usage | — |
| `int` IP mailbox | Registry e-mail forwarding | SES inbound / M365 shared mailbox | Queue | Upload |

### Exit gate, deliverables and open items

**Deliverables:** `ipm` module and migrations; status taxonomy and mapping table; deadline rule pack with verification log entries; government fee table with `last_verified_at`; Nice class-term list and related-class table; Excel template `LD-TPL-IPM-v1.0`; templates (user affidavit, assignment, licence, co-existence, founder IP assignment — via P06); marketplace SKUs defined in P16 (filing per class, reply to examination report, hearing attendance, renewal, clearance opinion, watch-hit review); Journal ingestion pipeline (manual upload); similarity matchers with evaluation report; reports IPM-01–06; user guides and tutorial scripts ("Track your trademark", "Read your examination report", "What the Journal watch tells you").

**Exit checklist:**
1. All `@P12-AT-*` scenarios and NN tests green.
2. Pilot: 3 companies and 30 individuals; 150 marks onboarded; 4 consecutive Journals ingested and matched; ≥ 1 opposition matter opened from a hit; ≥ 10 assisted refreshes confirmed.
3. Every rule used in pilot VERIFIED or advisory-badged and logged (NN-38); fee table verified against the Trade Marks Rules 2017 First Schedule [VERIFY].
4. WCAG 2.2 AA / IS 17802 audit of SCR-P12-04, -05, -06, -10, -14 (NN-28).
5. Settings registered (Appendix R); help keys `hlp.ipm.*` registered.
6. **Export-map entries registered (NN-11):** record types `ipm.asset`, `ipm.trademark`, `ipm.status_event`, `ipm.data_sheet`, `ipm.screening`, `ipm.watch_profile`, `ipm.watch_hit`, `ipm.copyright`, `ipm.design`, `ipm.patent`, `ipm.domain`, `ipm.agreement_link`, `ipm.use_evidence`, `ipm.valuation_note`, `ipm.enforcement_log`. Company path: `04 Trademarks and IP/<Asset type>/<Mark or title> – <Class or number> (LD-TMK-…)/{01 Application and Filing, 02 Examination and Replies, 03 Journal and Opposition, 04 Registration and Certificates, 05 Renewals, 06 Use Evidence, 07 Licences and Assignments, 08 Watch Reports, 09 Correspondence}` plus `04 Trademarks and IP/IP Portfolio.xlsx` and `Deadlines.xlsx`; disputes stay under `03 Litigation and Disputes/` with cross-references. Individual path: proposed new folder `11 Trademarks and IP/` in the individual taxonomy (OI-P12-06). [Proposed sub-folder names for the Appendix K owner.]
7. Demo script: founder journey (class finder → screen → data sheet → filing SKU → agent records filing → assisted refresh → examination report → reply outline), company journey (import 50 marks → Journal watch hit → oppose → P11 matter), renewal and ownership-gap closure.

**Error codes (`LD-IPM-001`–`LD-IPM-016`):** 001 Application number format invalid for office · 002 Duplicate asset · 003 Plan asset limit reached · 004 Watch limit reached · 005 Source not enabled for screening · 006 Status change needs evidence or reason · 007 Extraction confidence too low to confirm in bulk · 008 Rule unverified — advisory · 009 Data sheet incomplete · 010 Fee category evidence missing · 011 Only the engaged professional can record a filing · 012 Journal parse failed · 013 Agents cannot file or contact third parties · 014 Recordal evidence required before owner change · 015 Import row errors · 016 Undo window expired. Each with user text and `hlp.ipm.err.<nnn>`.

**Open items (Appendix W):**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P12-01 | Verify all deadline seeds (Trade Marks Act/Rules 2017 rule numbers, extension positions; Copyright, Designs, Patents rules as amended 2024) | IP domain analyst | Advisory badges |
| OI-P12-02 | Verify government fee schedule and applicant categories (startup, small enterprise definitions) | IP domain analyst | Fee shown "as at <date>, to be confirmed by your agent" |
| OI-P12-03 | WIPO Global Brand Database terms for commercial reuse, or a licensed partner | Integration lead + [COUNSEL] | Own-portfolio screening only |
| OI-P12-04 | IP India website terms for automated retrieval of published Journal PDFs | [COUNSEL] | Manual upload |
| OI-P12-05 | Select licensed TM data/watch partner (lawful source warranty, residency, DPDP) | Integration lead | Manual upload |
| OI-P12-06 | Add `11 Trademarks and IP/` to the individual export taxonomy | Appendix K owner | Export under `99 System Data/IP/` |
| OI-P12-07 | Role sub-types `TRADE_MARKS_AGENT`, `PATENT_AGENT` under `PRO_OTHER` in Appendix D; marketplace rules for agents (R6 suggests 0% commission pending agent conduct rules [VERIFY]) | Appendix D/M owners + [COUNSEL] | Treat as regulated; no commission |
| OI-P12-08 | Appendix I: add `TRADEMARK_DATA_PORT` capabilities `AssistedRefresh` and `RegistryMailParser` and the optional `searchMarks`/`watchJournal` methods | Integration lead | Manual entry |

## Phase P13 — Company Legal Department OS, Governance and HRMS

**File:** `phases/P13_Company_Legal_Department_OS_Governance_and_HRMS.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYB, director/KMP identity attributes), P02 (organisations, legal entities, departments, positions, user types, maker-checker, delegations), P03 (Configuration Studio, settings registry, `RULES_PORT`), P04 (Legal Vault, retention, legal hold), P06 (templates: resolutions, notices, minutes skeletons, appointment letters, policies), P07 (CLM approvals, obligations, renewal dates), P08 (eSign/DSC for minutes, registers, declarations, appointment letters), P09 (Vidhi runtime and agents), P11 (matters, clocks, spend, counsel panel; frozen `lit` read API), P12 (IP calendar), P16 (marketplace professionals and retainers), P17 (plans and entitlements), P18 (Delivery Console; RM as maker), P19 (LawDocsComply connectors, workplace and company-data adapters), P20 (export), P22 (mobile). Shared kernels (used, never forked — NN-47): `@infrabyx/governance-kernel`, `@infrabyx/hrms-kernel`, `infrabyx-labour-rulepack`, `@infrabyx/docgen`, `@infrabyx/redline`. External: LawDocsComply (when the tenant uses it), licensed MCA-data vendors, Microsoft 365 / Google Workspace, e-voting agencies (file hand-off).
> **Sequencing:** Wave 2, after P11 sprint 2. Track A (`lgo`, sprints 1–3): intake desk, SLAs, CLO dashboard, legal calendar, DoA matrix. Track B (`gov` mount, sprints 2–6): mode resolver, company-type configuration, board and committees, meetings, minutes, resolutions, registers, directors and KMP, duties. Track C (`hr` mount, sprints 5–8): people, positions, departments, leave, payroll via the labour rule pack, documents, acknowledgements, POSH. Sprints 9–10: finance-company templates (Appendix T), agents, LDC SoR sync certification, mobile, hardening. Freeze the kernel versions at sprint 2 and record them in `docs/kernels.lock`.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles), H (agent roster), K (export), R (settings), T (legal-department operating model and finance-company structure — companion to this phase), W (open items), X (Operations Hub addendum — boundary for staff HR), Y (Ecosystem Spec change requests).
> **Requirements covered:** R-002, R-018, R-019, R-021, R-026, R-027, R-028, R-030, R-047, R-053, R-055, R-059, R-060, R-064, R-067, R-068.
> **Decisions applied:** D-02, D-10, D-15, D-17 · **Challenges applied:** CH-14, CH-24, CH-26, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-09, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-24, NN-26, NN-28, NN-29, NN-30, NN-32, NN-33, NN-38, NN-12, NN-40, NN-43, NN-45, NN-47
> **Estimated effort:** 10 two-week sprints, squad of 8 (backend 4, frontend 2, QA 1, integration 1) plus a part-time Company Secretary (secretarial domain), an HR/labour analyst and a counsel reviewer for the operating model.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P13_Company_Legal_Department_OS_Governance_and_HRMS.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P13-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The owner wants companies to run their legal work "with one CLO" (brief l.68) and to manage people, KMPs, directors, duties and departmental structures, including finance-company structures aligned with the Companies Act 2013 and RBI directions (brief l.67). This phase delivers the **Company Legal Department OS**:

1. **Legal team in a box** — positioned per D-17 and CH-14 as **legal operations + AI + on-demand professionals**. LawDocs gives the company the operating system of a legal department (intake, triage, SLAs, calendar, records, drafting, spend, dashboards). Advice and representation come from advocates engaged in their own name (Advocates Act 1961 ss.29, 33; R3 LG-110). A company with one CLO, or a CS or compliance head acting as legal lead, can run its legal function on LawDocs; it still needs advocates for court work and opinions, and the product says so.
2. **Governance kernel mount** — board, committees, meetings, minutes, resolutions, registers, directors and KMP, duties — mounted locally for LawDocs-only companies and served from LawDocsComply (system of record) when the company also uses LDC (D-10, NN-47).
3. **HRMS kernel mount for client companies** — people, positions, KMP designations, departments, duties, leave, payroll through the shared labour rule pack, onboarding and exit documents, policy acknowledgements, POSH Internal Committee records — again local or LDC-served.
4. **Departmental structure templates**, including the customisable finance-company (NBFC) structure in Appendix T.

| Outcome | KPI / exit-gate measure |
|---|---|
| Every legal request has an owner and a clock | 100% of intake requests triaged within the category SLA in pilot; first-response SLA met ≥ 95% |
| Self-service where safe | ≥ 30% of standard requests (e.g., NDA on the company template) closed by guided self-service with no lawyer time, within guardrails |
| One legal calendar | Contracts, cases, trademarks, licences, board and HR statutory dates in one calendar; 0 missed statutory dates in UAT |
| Board work faster | Notice + agenda + pack issued in ≤ 6 steps; minutes draft circulated within 3 working days of the meeting in pilot; 0 edits to sealed minutes (SS-1 bar on altering entered minutes [VERIFY para]; tampering is an offence under s.118(12)) |
| No double entry with LDC | When LDC is SoR, 0 governance or HR rows written locally; governance and HR work happens in LDC; LawDocs reads governance facts on demand; switch reconciliation 100% |
| Structure in minutes | A new NBFC tenant adopts the Appendix T template (departments, committees, KMP, three lines of defence) in ≤ 15 minutes and customises it without Super Admin (NN-29) |
| Proportionate HR | Attendance and work measurement disclosed and outcome-based; 0 surveillance features (NN-33) |

### Integrations to respect

| Port / adapter | Use | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `GOVERNANCE_SOR_PORT` → `LocalKernel` / `LdcAdapter` | `local_kernel`: kernel reads/writes; `ldc_sor`: read-through governance facts (FR-P19-29) and Appendix Y §Y.7.6 proposals | — | LDC unreachable → dependent actions blocked (FR-P13-24) | Legal drafting continues in the request or matter |
| `HRMS_SOR_PORT` → `LocalKernel` / `LdcAdapter` | `local_kernel`: kernel reads/writes; `ldc_sor`: minimal people projection only (FR-P19-33) | — | As above | — |
| `COMPANY_DATA_PORT` | Director list, DIN status, charges, filing status refresh | Licensed MCA-data vendors (Probe42, Signzy, Surepass, Perfios-Karza — R6 D-15 [VERIFY]) | Show last fetched with date | User entry with evidence |
| `WORKSPACE_PORT` | Teams/Meet links, participant logs, calendars, Teams/Chat intake app, SCIM directory | Microsoft Graph, Google Workspace | Retry; ICS fallback | Manual link |
| `ESIGN_PORT` (P08) | Minutes, declarations, appointment letters, registers extracts | Aggregator ESPs; DSC | Queue | Wet-ink upload with formalities gate (NN-40) |
| E-voting hand-off (file) | General meetings | NSDL, CDSL, KFin Technologies, MUFG Intime [VERIFY formats] | — | Upload results file |
| `ACCOUNTING_PORT` / bank file | Payroll bank file, legal spend export | Bank formats (NEFT bulk), ERP | Download | — |
| `NOTIFY` | Notices proof of delivery (e-mail), reminders, approvals | SES/Brevo; DLT SMS; push | Channel fallback | — |
| `BILLING_PORT` (OH8) | Entitlements (Business/Enterprise), agent seats | — | — | — |

### Exit gate, deliverables and open items

**Deliverables:** `lgo` module; kernel mounts for `gov`, `hr`, `hr_posh` with pinned versions; LDC SoR adapters (certified against LDC sandbox); setup wizard and Appendix T templates as seed data (YAML/JSON, §T.8); intake categories, SLA policies, routing seeds; DoA seeds; Legal Department Charter template; board-pack and minutes templates (from kernel library, tenant-copyable); duty catalogue; dashboards; report definitions (LGO-01 intake and SLA, LGO-02 workload outcomes, LGO-03 spend by department, GOV-01 meetings and minutes clocks, GOV-02 blueprint gaps, GOV-03 resolutions and follow-ons, HR-01 headcount by department/establishment, HR-02 leave, HR-03 payroll register summary, HR-04 POSH counts); user guides (CLO, CS, director portal, HR admin, employee) and tutorial scripts ("Raise a legal request", "Run a board meeting end to end", "Set up your NBFC structure").

**Exit checklist:**
1. All `@P13-AT-*` scenarios and NN tests green.
2. Pilot A (LawDocs-only private company, 80 employees): 100 requests through the desk; one board meeting from planning to sealed minutes; one AGM notice pack; one month of payroll on the labour pack; one POSH IC set up with an annual-report draft.
3. Pilot B (NBFC-ML on LDC): mode `ldc_sor` with zero local governance/HR rows; formalities-gate checks served from LDC governance facts; deep links verified for every P13 menu; one switch rehearsal (`local_kernel` → `ldc_sor`) on a sandbox tenant with a clean reconciliation report.
4. Template adoption tested for startup, private company, listed company, LLP, NBFC-BL/ML/UL and HFC.
5. Every statutory rule used in pilots VERIFIED or advisory-badged and logged (NN-38).
6. WCAG 2.2 AA / IS 17802 audit of SCR-P13-03, -06, -07, -15, -16, -23, -25 (complaint form) (NN-28).
7. Settings registered (Appendix R); help keys `hlp.lgo.*`, `hlp.gov.*`, `hlp.hr.*` registered.
8. **Export-map entries registered (NN-11):** `lgo.request`, `lgo.request_event`, `lgo.category`, `lgo.licence`, `lgo.doa_version`, `lgo.duty_assignment`, `lgo.digest`; `gov.meeting`, `gov.agenda_item`, `gov.pack`, `gov.attendance`, `gov.minutes`, `gov.resolution`, `gov.register_entry`, `gov.officer_role`, `gov.declaration`, `gov.blueprint_snapshot`; `hr.person`, `hr.employment`, `hr.position`, `hr.department`, `hr.leave_record`, `hr.attendance_record`, `hr.pay_run`, `hr.payslip`, `hr.document`, `hr.acknowledgement`, `hr_posh.case` (IC-only export). Paths (Appendix K §K.3.1 governs — X-07): `05 Board and Governance/{<Entity>/}<FY>/{Board Meetings, Committee Meetings/<Committee>, General Meetings, Resolutions by Circulation, Filings}/<YYYY-MM-DD> - …/`, `05 Board and Governance/Registers/` (statutory registers, incl. directors and KMP, in prescribed layouts + PDF extracts); `06 Policies and Registers/` (DoA matrix versions, Legal Department Charter) and `06 Policies and Registers/Licences and Permits/`; `07 People and HR/Employees [R]/EMP-<number>/…` (ids only in names), `Departments and Positions.xlsx`, `Duties and Delegations.xlsx`, `Policy Acknowledgements.xlsx`, `Payroll [R]/<FY>/`; `07 People and HR/POSH Internal Committee [R]/` never in an owner, admin or auditor export — produced only on request of `ORG_POSH_IC_PRESIDING` as a separately encrypted archive (Appendix K `hr_posh_case` row); `09 Services and Engagements/Legal Requests (internal)/<FY>/<YYYY-MM-DD> - <Request title> (LD-LRQ-…)/`. In `ldc_sor` mode governance and HR folders are produced by LDC's export (`LDC-EXPORT-1.0`) and referenced from the LawDocs README.
9. Demo script: setup wizard (NBFC-ML) → request from Sales → triage → convert to contract → board item auto-suggested → meeting with VC attendance → minutes drafted, accepted, signed and sealed → MGT-14 task → KMP change with vacancy clock → payroll run with checker → POSH IC annual-report count.

**Error codes:** `LD-LGO-001`–`LD-LGO-010` — 001 Category inactive · 002 Required form fields missing · 003 Self-service guardrail exceeded (converted to review) · 004 SLA pause reason not permitted · 005 Conversion target unavailable · 006 Routing rule conflict · 007 Action exceeds your delegation · 008 Licence register is managed in LawDocsComply · 009 Digest to directors needs CLO approval · 010 Duty has no position holder. `LD-GOV-001`–`LD-GOV-014` — 001 Blueprint rule unverified — advisory · 002 Composition rule failed · 003 Notice period shorter than required without urgency path · 004 Quorum not present · 005 Matter cannot be passed by circulation · 006 Interested director cannot vote on this item · 007 Minutes clock breached · 008 Minutes sealed — no edits · 009 Ratification pending · 010 Register entries are event-based — use the source action · 011 Declaration campaign closed · 012 Filing task needs SRN · 013 System of record unavailable — draft only · 014 Mode change blocked while migration runs. `LD-HR-001`–`LD-HR-010` — 001 Labour pack version mismatch · 002 Pay run needs a different checker · 003 Wage payment date beyond statutory limit · 004 Leave below statutory floor · 005 Geo capture needs notice and consent · 006 Prohibited monitoring field · 007 POSH area restricted · 008 Appointment letter missing before joining · 009 Position vacant for regulated role · 010 HR record managed in LawDocsComply. Each with user text and `hlp.<module>.err.<nnn>`.

**Open items (Appendix W):**

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-P13-01 | Appendix Y §Y.7.6 (governance facts and proposals to the same organisation's SoR) and §Y.7.7 (`SystemOfRecordSwitched`) — tracked by P19; SoR keys reconciled by X-11 (`int.eco.ldc.sor_mode.governance` / `.hrms` only; Appendix R to drop `gov.mode`/`hr.mode`); per-legal-entity scoping of the mode (P13 originally ENTITY tier vs P19 TENANT tier) to be confirmed by the Appendix R owner | Integration lead + Appendix R owner | `local_kernel` mode only |
| OI-P13-02 | Kernel extension points needed by `lgo` (duty binding, intake conversions) — request to kernel owners, no fork | Architecture lead | Extension tables only |
| OI-P13-03 | Verify RBI NBFC Governance Directions 2025 title and paragraphs; IT governance, ALM and fraud-risk committee sources after 2025 consolidation | Regulatory analyst | Overlay ADVISORY |
| OI-P13-04 | Verify Companies Act thresholds and rule numbers used in the blueprint seeds (Rules 3, 4, 6, 8, 8A; SS-1/SS-2 paras; MGT-14 list; MR-1 timeline; electronic registers rules) | CS reviewer | Advisory badges |
| OI-P13-05 | Teams/Google Chat intake app publication requirements | Integration lead | Web/e-mail intake |
| OI-P13-06 | Managed Legal Department retainer structure (advocates' firm, invoicing) | [COUNSEL] + [TAX MEMO] | RS-LD-21 OFF |
| OI-P13-07 | DPDP basis for employee processing (s.7 legitimate uses) and employee notice text | DPO + [COUNSEL] | Consent-based notice |
| OI-P13-08 | HR, payroll and POSH role codes `ORG_HR_ADMIN`, `ORG_PAYROLL_MAKER`, `ORG_PAYROLL_CHECKER`, `ORG_POSH_IC_PRESIDING`, `ORG_POSH_IC_MEMBER` registered in Appendix D with their Cerbos policies (in progress at integration review) | Appendix D owner | Assign via `ORG_ADMIN` custom roles carrying the same permissions |
| OI-P13-09 | New ID prefix `lrq_` and business ID `LD-LRQ-…` for conventions §5 | Pack lead | Use as proposed |
| OI-P13-10 | LawDocs-only listed companies: scope of basic disclosure case vs LDC | [OWNER] | Recommend LDC |

## Phase P14 — Business Services: Start a Business, Compliance Services and Tax

**File:** `phases/P14_Business_Services_Start_a_Business_Compliance_and_Tax.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P16 (marketplace catalogue, offering object, engagement lifecycle, professional registry, Rule 36 directory, buyer platform fee), P17 (`BILLING_PORT`, OH8 SKUs and streams, entitlements, GST invoice mirror, refunds), P04 (vault folders, document checklists, retention, legal hold), P06 (templates and questionnaires: founders' agreement, SHA, SSA, term sheet, ESOP plan, partnership deed, trust deed, MoA/AoA), P07 (deal rooms, obligations `obl_`), P08 (eSign, DSC, eStamp, instrument eligibility gate), P10 (notice replies), P11 (tax litigation matters), P13 (governance kernel mount, compliance calendar for LawDocs-only tenants, HRMS/payroll kernel), P18 (Delivery Console, delivery grants, RM-as-maker), P19 (`int`: LDC contracts, GSP/ERI/KYB adapters), P03 (settings, rule engine, effective-dated tax-year rule packs). External: Operations Hub OH8 (catalogue, prices, invoices, Razorpay) and OH9 (professional directory); MCA V3, IP India, FoSCoS, DGFT, Udyam, State portals (user- or practitioner-operated only); a licensed GSP; LawDocs' own ERI registration (Type 2) [VERIFY]; KYB vendor (R6 D-15).
> **Sequencing:** Wave 3. Sprint 1 freezes the service-definition schema (§4A) and fee-line model (§4F) so that P21 content can bind service pages to `svc_` codes. Catalogue seeding (§4B–§4C) and Startup Desk (§4J) run in parallel with the tax workspace (§4K–§4N). ERI and GSP adapters ship behind flags (NN-38) until registrations and contracts are verified. Attest services (statutory, tax and secretarial audit) ship in BYO-professional mode only (§4G).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), D (roles and access matrix), F (instrument eligibility gate), H (agent roster), K (`LD-EXPORT-1.0`), M (marketplace and professional rules), R (settings registry), W (verification log and open items), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-014, R-036, R-037, R-038, R-039, R-040, R-047, R-063, R-064, R-069, R-075, R-080, R-082, R-086, R-087, R-090.
> **Decisions applied:** D-02, D-05, D-10, D-11, D-12, D-17 · **Challenges applied:** CH-06, CH-07, CH-08, CH-09, CH-10, CH-12, CH-13, CH-16, CH-19, CH-25 · **Non-negotiables tested:** NN-01, NN-05, NN-07, NN-08, NN-11, NN-13, NN-14, NN-16, NN-17, NN-18, NN-20, NN-21, NN-22, NN-29, NN-30, NN-38, NN-40, NN-41, NN-45, NN-46, NN-47, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2, tax/rules analyst 1, QA 1, CS/CA content reviewer 1).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P14_Business_Services_Start_a_Business_Compliance_and_Tax.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P14-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs sells the owner's **Start a Business** catalogue (26 services) and **Compliance** catalogue (22 services) as **productised services**. A founder, SME or individual can see what a service needs, what it costs line by line, who may lawfully perform it, how long LawDocs takes and how long the government takes, and can then buy it with or without a subscription (R-040, D-11). Every document collected and every certificate received lands in the Legal Vault and drives renewal reminders, so the customer has a reason to keep LawDocs (R-011). The **Startup Desk** packages incorporation, founder documents, funding readiness and a "virtual legal officer" retainer (R-082). The **Tax workspace** gives individuals, companies and LLPs one place for returns, TDS, GST, professional tax, advance-tax calendars and tax notices (R-069), without anyone sharing a portal password (CH-10).

**Why it matters.** Commodity filings have settled at ₹1,499–₹2,999 + GST + government fees (R6 B-06–B-15). LawDocs wins on (i) a free guided start and free AI-drafted first documents, (ii) the vault and renewal engine, (iii) honest fee breakdowns (IMP-075) and (iv) live order tracking (IMP-080).

| Outcome | Exit-gate measure |
|---|---|
| Productised catalogue | 48 services seeded as `svc_` definitions, each with questionnaire, document checklist, fee lines, lawful-performer rule, SLA, deliverables and renewal rule; every definition has a reviewer of record (NN-30) |
| Buy without subscription | A non-subscriber orders a fixed-price service in ≤ 7 taps from the service page (buyer account, eligibility answers, fee review, checkout) |
| Fee honesty | 100% of orders show government fee, stamp duty, third-party costs, professional fee, LawDocs fee and GST per supplier as separate lines before payment; zero drip-pricing defects in the NN-50 test suite |
| Lawful delivery | 0 orders assigned to a performer who lacks the credential the service's rule requires (CI test `NN-41_performer_credential_gate`) |
| Tracking | Every order shows the current milestone, "Waiting on" owner and next date; customer status updates by in-app, email and opted-in WhatsApp within 15 minutes of a milestone change |
| Renewals | Every certificate with an expiry or periodic duty creates an obligation with T-60/T-30/T-7 reminders |
| Tax without passwords | ITR filing via the ERI route reaches "Awaiting taxpayer e-verification" without LawDocs ever receiving an OTP, DSC PIN or e-filing password |
| KPIs (post-launch) | Order-to-inputs-complete median ≤ 3 days; LawDocs SLA attainment ≥ 95%; rework rate ≤ 3%; refund-dispute rate ≤ 1%; renewal capture ≥ 40% |

### Integrations to respect

| Port / adapter | Vendor options | Failure behaviour | Manual fallback |
|---|---|---|---|
| `KYB_PORT` (CIN, LLPIN, GSTIN, name availability hints) | Licensed MCA-data vendors (Probe42, Signzy, Surepass, Perfios-Karza; R6 D-15/D-16) | Show "lookup unavailable"; never scrape | Customer uploads certificate |
| `ERI_PORT` | LawDocs' own ERI registration [VERIFY] | Queue upload; taxpayer notified | Guide mode: taxpayer uploads JSON |
| `GSP_PORT` | Licensed GSP partner [VERIFY contract] | Banner; switch to practitioner route | Offline utility upload by taxpayer/practitioner |
| `ESIGN_PORT`, `ESTAMP_PORT` | P08 aggregators | P08 rules | Wet-ink pack |
| `DIGILOCKER_PORT` | P01 | Upload instead | — |
| `BILLING_PORT` | OH8/Razorpay | Order stays `QUOTED` | Payment link |
| LDC obligations contract | `int` | Read-only cached view with staleness label | Manual obligation entry (LawDocs-only tenants) |

No adapter calls MCA, IP India, FoSCoS, DGFT, e-filing, TRACES or GST portals by browser automation or with customer credentials (NN-05). Portal credentials, if the customer chooses to share them, live only in `cvl`, OFF by default, delegation-first (NN-16, CH-07).

### Exit gate, deliverables and open items

- [ ] 48 service definitions LIVE with reviewer of record, fee schedules verified or flagged advisory-only, copied-text lint clean.
- [ ] Performer-class gate, independence checks and BYO professional flow pass CI (`NN-41_performer_credential_gate`, `NN-21_no_professional_commission`).
- [ ] Fee-line model renders on web and mobile; NN-22 and NN-50 suites green.
- [ ] Startup Desk: entity chooser, kit, founder templates, DPIIT guide (advisory-only until verified), data room, retainer SLA eSign.
- [ ] Tax workspace in guide mode; ERI and GSP flows behind flags with verification-log entries; rule packs for FY 2025-26 (1961 Act) and tax year 2026-27 (2025 Act) with section map.
- [ ] Settings in Appendix R; help keys registered: `hlp.bsv.*` (entity_chooser, din, dsc, spice_plus, fee_class, registered_office, government_fee, pure_agent, sla_clock, waiting_on, certification, udyam_free, renewal), `hlp.tax.*` (tax_year, eri, everify, ais, regime, advance_tax, gsp, pct05, ims, gstr2b, professional_tax, notice_din).
- [ ] **Export map** (`xpt.export_map`): `bsv_order`, `bsv_order_fee_line`, `bsv_checklist_item`, `bsv_milestone` → company `09 Services and Engagements/Business Services/<FY>/<Service> (LD-ENG-…)/` (applications, government acknowledgements, certificates; Appendix K §K.3.1 governs — X-07); individual `08 Agreements/` (or life-area folder) or `09 Tax/`; `tax_filing`, `tax_computation`, tax notices → company `12 Tax/{<Entity>/}<FY>/{Income Tax, GST/<GSTIN last 4 - State>, TDS and TCS, Professional Tax/<State>, Notices, Assessments and Appeals}/` (X-12) and individual `09 Tax/Tax Year <YYYY-YY>/` (pre-2026-27 years `Tax Year <YYYY-YY> (AY <YYYY-YY>)`); `tax.calendar_item`, `obl_` renewals → `99 System Data (CSV and JSON)/`.
- [ ] Demo script: visitor → entity chooser → Pvt Ltd order → checklist → certification by BYO CS → filing approval → CIN delivered → renewal obligations; salaried ITR in guide mode; GST practitioner route; tax notice to P11 matter.

| OI | Item | Owner |
|---|---|---|
| OI-P14-01 | Verify every government fee row and form version (48 services) and log in `docs/compliance/verification-log.md` | `PLT_LEGAL_REVIEWER` |
| OI-P14-02 | ERI registration type, eligibility, security audit and API scope; re-notification under the 2025 Act | Owner + CA [VERIFY] |
| OI-P14-03 | Counsel opinion: may an affiliated CA/CS/advocate firm deliver attest or certification services to LawDocs customers by direct engagement without breaching ICAI/ICSI/BCI rules? | [COUNSEL] |
| OI-P14-04 | Tax memo: pure-agent treatment of government fees and PA Directions position for `PURE_AGENT_REIMBURSE` | [TAX MEMO] |
| OI-P14-05 | GSP partner selection and contract; taxpayer API-consent flow | Owner |
| OI-P14-06 | Income-tax Act 2025 section map (return, verification, advance tax, tax audit, charity registration, startup deduction, authorised representative) | CA reviewer [VERIFY] |
| OI-P14-07 | DPIIT recognition criteria and benefits currently in force | [VERIFY] |
| OI-P14-08 | DIR-3 KYC periodicity; INC-20A; C-PACE; LLP Form 24 rule | CS reviewer [VERIFY] |
| OI-P14-09 | DSC handling authority letter wording | [COUNSEL] |
| OI-P14-10 | Ecosystem Spec v1.2: LDC service-order status contract (Appendix Y) | Pack lead |
| OI-P14-11 | Tax-year folder label: resolved by X-12 / Appendix K (`Tax Year <YYYY-YY>` with legacy AY alias; company `12 Tax/`); statutory term confirmation tracked as OI-K-06 [TAX MEMO] | Pack lead |

## Phase P15 — Consumer Help: Loan/Insurance Grievances, Challans and Vehicles

**File:** `phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P04 (vault, evidence folders, Object Lock, legal hold), P05 (OCR, screenshot and handwriting type copies, translation, call-recording transcripts), P10 (letters, complaints and notices drafting studio), P16 (Rule 36 advocate directory, fixed-fee engagements, buyer platform fee, Route payouts), P06 (vehicle sale agreement, delivery note, authority letters), P07 (deal rooms, messaging), P08 (eSign, eStamp, eligibility gate, evidence pack, BSA s.63 certificate), P17 (separate selling entity, Razorpay merchant, stream switches RS-LD-39/40), P18 (Delivery Console in the Consumer Help entity scope), P19 (`int`; conflict-check client), P01 (DigiLocker pulls of RC/DL [VERIFY issuer availability]), P03 (rule engine, effective-dated rule data). External: Operations Hub conflict service (extension of OH1.6; Appendix X), OH8 (Consumer Help selling entity), official portals by deep link only (cms.rbi.org.in, sachet.rbi.org.in, Bima Bharosa, cioins.co.in, e-Jagriti, NCH 1915, echallan.parivahan.gov.in, vcourts.gov.in, vahan.parivahan.gov.in, State traffic Lok Adalat pages).
> **Sequencing:** Wave 3. Sprint 1 builds the brand/entity profile, ethical wall and conflict check; nothing else ships until the wall tests pass. Vertical A (loans) and the challan/vehicle verticals run in parallel from sprint 2; Vertical B (insurance) from sprint 4. Success-fee code ships dark (RS-LD-40 OFF). Rules data (Appendix S) is loaded and verified per row before the related screen leaves advisory mode (NN-38).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), S (Consumer Help Rules and Playbooks), D (roles), F (instrument eligibility gate), K (`LD-EXPORT-1.0`), M (marketplace professional rules), R (settings), W (verification log), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-002, R-011, R-044, R-047, R-061, R-063, R-083, R-084, R-085, R-086, R-087, R-088.
> **Decisions applied:** D-05, D-06, D-11, D-12, D-13 · **Challenges applied:** CH-05, CH-08, CH-12, CH-13, CH-16, CH-20, CH-22, CH-23, CH-25, CH-28, CH-30, CH-31 · **Non-negotiables tested:** NN-01, NN-04, NN-05, NN-07, NN-08, NN-09, NN-10, NN-13, NN-14, NN-16, NN-17, NN-19, NN-20, NN-21, NN-22, NN-23, NN-24, NN-26, NN-34, NN-35, NN-38, NN-39, NN-40, NN-45, NN-46, NN-49, NN-50
> **Estimated effort:** 9 two-week sprints, squad of 8 (backend 3, frontend 2, rules/legal-ops analyst 1, QA 1, security engineer 0.5, content 0.5).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P15_Consumer_Help_Grievances_Challans_and_Vehicles.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P15-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Indian consumers who face recovery-agent harassment, unfair loan charges, a wrong credit report, a rejected insurance claim, a traffic challan or a used-vehicle sale usually do not know which forum to approach, by when, or with what evidence. Competitors either "take everything over" for a success fee (FREED, Insurance Samadhan) or collect fines through their own accounts (Park+) (R2 §1(a), §2(a), §3(a)). `[Consumer Help Brand]` is the **documented, user-controlled** alternative: it tells the user the right forum and deadline, captures evidence that will stand up, drafts the letters, tracks every clock, and adds a human case manager or an advocate only where the forum allows it (R2 §0).

The brand runs on the LawDocs platform but under its **own brand and legal-entity profile** with an ethical wall from the group's lender-facing products (D-06, NN-23). Finbyx, Udofin and LawDocsComply serve lenders. Consumer Help sometimes acts against lenders. The two must never share data, staff or incentives.

| Outcome | Exit-gate measure |
|---|---|
| Separate brand and entity | Brand, domain, legal entity, GSTIN, Razorpay merchant, privacy notice, grievance officer and staff group configured independently; wall tests (§12) pass |
| Right forum, right time | Triage returns a forum, eligibility result and computed deadline for 100% of seeded scenarios in Appendix S, each tied to a verified rule row or shown as advisory |
| Evidence that survives | Every evidence item hashed at capture, time-stamped, with a typed copy for screenshots and a BSA 2023 s.63 certificate draft on export (NN-10) |
| User control | User signs and files wherever the forum expects the complainant; every authority letter is scoped, time-bound and revocable in-app |
| No money handling | LawDocs never receives fines, dues, settlement amounts or vehicle prices (NN-22, NN-23); CI test proves no payment intent can name a government or lender beneficiary |
| No outcome promises | Banned-phrase lint blocks "waiver", "guaranteed", "stop EMIs", "100% success" across site, app, templates and AI output (NN-20) |
| KPIs (post-launch) | First draft letter ≤ 24 h from intake; 0 missed statutory windows on managed cases; median days per stage by forum published internally; refund-dispute rate ≤ 1%; NPS by vertical |

### Integrations to respect

| Port / service | Use | Failure behaviour | Fallback |
|---|---|---|---|
| OH conflict service via `int` (OH1.6 extension; Appendix X §X.10) | Group-client conflict flag | Fail closed: managed services unavailable, self-serve continues | Manual check by the Consumer Help compliance owner with logged reason |
| `DIGILOCKER_PORT` | RC/DL pull [VERIFY issuer] | Upload instead | — |
| `ESIGN_PORT`, `ESTAMP_PORT` (P08) | Authority letters, vehicle agreements | P08 rules | Wet-ink pack |
| P16 engagements | Advocates | Directory OFF → show "find your own advocate" guidance | — |
| `BILLING_PORT` (Consumer Help merchant) | Fees | Case stays `CONFLICT_CHECK`/`ACCEPTED` pending | Payment link |
| `ntf` (JioCX or other DLT CPaaS) | SMS/WhatsApp | Email fallback | In-app |
| Official portals | Deep links only | Link-health alert | Registry shows alternate official URL |

No vendor challan, vehicle-data or credit-bureau API is integrated (R2 §3(b); CH-05). Any future vendor needs a legal sign-off on the data source and a verification-log entry before its flag turns on (NN-38).

### Exit gate, deliverables and open items

- [ ] Consumer Help brand and legal entity configured; dedicated database and keys; wall tests P15-AT-01/02/03/19 green; all scenarios `@P15-AT-01…24` green; recertification job scheduled.
- [ ] Appendix S rule rows loaded; every row verified or flagged advisory; representation matrix enforced.
- [ ] Verticals A, A2, C, D live; B live from sprint 4; kill switch per vertical tested (NN-39).
- [ ] Templates T-A1…T-D7 published with reviewer of record; banned-phrase lint on all channels.
- [ ] OH conflict-service extension accepted (Appendix X) and the Ecosystem Spec change request filed (Appendix Y).
- [ ] Settings in Appendix R; help keys: `hlp.chp.ombudsman`, `hlp.chp.internal_ombudsman`, `hlp.chp.rb_ios`, `hlp.chp.award`, `hlp.chp.authorised_representative`, `hlp.chp.kfs`, `hlp.chp.apr`, `hlp.chp.recovery_agent_rules`, `hlp.chp.cic_dispute`, `hlp.chp.bima_bharosa`, `hlp.chp.insurance_ombudsman`, `hlp.chp.e_jagriti`, `hlp.chp.nch`, `hlp.chp.compounding`, `hlp.chp.virtual_court`, `hlp.chp.lok_adalat`, `hlp.chp.form_29_30`, `hlp.chp.form_35`, `hlp.chp.hypothecation`, `hlp.chp.delivery_note`, `hlp.chp.conflict_check`, `hlp.chp.vehicle_loan` (FR-P15-70; registered in P21's help-key list).
- [ ] **Export map** (`xpt.export_map`): `chp_case`, `chp_evidence_item`, `chp_harassment_incident`, `chp_authority`, `chp_fee_plan` → profile `ld_consumer_help_v1` (Appendix K §K.3.4, which governs — X-07): `02 Loan and Lending Complaints/`, `03 Insurance Complaints/`, `04 Credit Report Disputes/` `<Year>/<YYYY-MM-DD> - LD-GRV-… - <Institution> - <Product>/{01 Complaint to the Institution … 05 Outcome and Compliance}`; `chp_challan` → `05 Challans/<Year>/…`; `chp_vehicle`, `chp_vehicle_sale` and vehicle-loan papers (FR-P15-70) → `06 Vehicles/<Vehicle label>/…`; fees → `07 Fees and Receipts/<Year>/`; case metadata CSV/JSON → `99 System Data (CSV and JSON)/`. Natural-person names never appear in paths (`ids_only` LOCKED). Export runs from the user's own workspace without staff help (NN-11); conflict-check logs are entity records, not user data.
- [ ] Demo: harassment case from tile to RE letter to RBIO pack self-filed; conflict hit → self-serve; health-claim rejection to Ombudsman pack; challan import → pay on official portal → receipt; vehicle sale with eSign, delivery note and Vahan checklist.

| OI | Item | Owner |
|---|---|---|
| OI-P15-01 | Incorporate and name the Consumer Help entity; board COI policy; annual independent wall review | [OWNER] |
| OI-P15-02 | Counsel opinion on success fee (champerty, unfair contract terms, CCPA) and on flat-fee case management (Advocates Act s.33 / *A.K. Balaji* boundary) | [COUNSEL] |
| OI-P15-03 | Does CMS accept an eSigned authorisation for a non-advocate representative? Consumer-commission agent authorisation form under the 2014 regulations | [VERIFY] |
| OI-P15-04 | Fleet challan subscription: entity placement and lawful data source | [OWNER] [VERIFY] |
| OI-P15-05 | Escrow partner for vehicle sales, or party-to-party only | [OWNER] |
| OI-P15-06 | RBC amendment paragraph numbers (banks Fourth, NBFC Third Amendment, 6 Aug 2026) and the earlier calling-hours guidance applicable before 1 Jan 2027 | [VERIFY] |
| OI-P15-07 | State data: Virtual Court and physical-court transfer timelines, Lok Adalat rules, stamp duty on vehicle sale agreements, RTO physical-submission States | [VERIFY] per State |
| OI-P15-08 | Brand name: R2 could not find "ChallanWallah", but R1 records challanwala.com as a live competitor; confirm the comparator set | [OWNER] |
| OI-P15-09 | OH1.6 extension: chp machine client, HMAC epoch-key management, response schema | Pack lead / OH |
| OI-P15-10 | Licence to reuse RBI-published NBFC/DLA lists in the legitimacy check | [VERIFY] |

## Phase P16 — Marketplace, Professional Registry, Retainers and FinLegal Academy

**File:** `phases/P16_Marketplace_Professional_Registry_Retainers_and_Academy.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (identity, KYC/KYB, professional credential verification, consent artefacts), P02 (tenancy, Personal and Company workspaces, maker-checker), P03 (settings registry, rule engine), P04 (Legal Vault — deliverables, engagement records), P07 (negotiation and redlines for engagement letters, SOWs and SLA schedules), P08 (eSign of engagement letters and SLAs; instrument eligibility gate), P09 runtime (Vidhi), P17 (`BILLING_PORT`, price cards, checkout, invoices, credits, stream registry), P18 (Delivery Console, delivery grants, RM-as-maker), P19 core (`int`, OH8/OH9 adapters, Academy feed connector), P20 core (`xpt.export_map`), P21 core (public-site shell, SEO, help keys). External: Operations Hub **OH8** (catalogue, quotes, orders, GST invoices, credit notes, Razorpay incl. Route), **OH9** (group professional directory and credential verification), **OH3** (consented leads), **OH6** (complaints about LawDocs services), **OH14** (claims gate); LawDocsComply (group listings, D-11); FinLegal Academy (trainings.lawdocs.in, Graphy-hosted per R5 §1.3).
> **Sequencing:** Starts after P17 sprint 3 (price-card, quote and checkout components frozen). Ship order: (1) public storefront + first-party LawDocs services (Model M1) + Academy listing; (2) retainers and SLA engine; (3) LawDocs Panel advocates' firm under Model M2 once OI-P16-01 and OI-P16-02 close; (4) third-party professionals behind per-profession switches that stay OFF until counsel opinion + checker approval (NN-21). Freeze point: profession render allow-lists (`RULE36_V1`, `PRO_SERVICE_V1`) and the `mkp.engagements` state machine are frozen at the end of sprint 4 because P15 (Consumer Help) and P14 (Business Services) consume them.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), M (Marketplace Services Catalogue and Professional Rules), L (Pricing, Plans, Revenue-Stream Registry and Savings Model — streams RS-LD-19…RS-LD-33), D (roles), F (instrument eligibility gate), K (`LD-EXPORT-1.0`), R (settings registry), W (open items), X (Operations Hub additions), Y (Ecosystem Spec v1.2 change request).
> **Requirements covered:** R-014, R-016, R-021, R-030, R-037, R-038, R-039, R-040, R-041, R-047, R-064, R-075, R-080, R-081, R-082, R-084 (advocate to contest a court-referred challan, listing only), R-086, R-087, R-088.
> **Decisions applied:** D-02, D-05, D-06, D-10, D-11, D-12, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-09, CH-14, CH-20, CH-22, CH-25, CH-31 · **Non-negotiables tested:** NN-01, NN-11, NN-13, NN-14, NN-17, NN-18, NN-19, NN-20, NN-21, NN-22, NN-23, NN-24, NN-35, NN-39, NN-41, NN-45, NN-46, NN-49, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend 3, frontend 2 — public + delivery, mobile 0.5 shared with P22, integration 1 — OH8/OH9/Route/Academy, QA 1, legal-ops analyst 0.5)

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P16_Marketplace_Professional_Registry_Retainers_and_Academy.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P16-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs sells human expertise that software cannot replace — drafting, review, notices, policies, annual reports, minutes and board support, compliance testing, risk assessment, stress testing and scenario analysis, retainer advisory, filings and returns, startup bundles, trademark work, litigation support — **with or without a SaaS plan** (R-040). The marketplace is the single group storefront at `lawdocs.in/marketplace` (D-11) for LawDocs services, LawDocsComply services and FinLegal Academy courses. It is public and browsable without login (R-041).

It must beat LegalKart on the points where LegalKart is weak (R1 §1, §3.4–3.5): no per-minute ranked advocates, no non-refundable short-expiry wallet, real verification instead of "does not separately verify", landed prices instead of "starting at", SLA-backed delivery instead of "lawyer stopped responding". It must also stay lawful where every lawyer directory is exposed: BCI Rule 36, the Madras High Court judgment of 3 July 2024 and the ICAI aggregator bar (R3 LG-111–LG-117).

**Design in one line.** Fixed-scope, landed-price **service products** sold by LawDocs, fulfilled by professionals that LawDocs assigns (LawDocs team first, a contracted advocates' panel next, third parties later), with a separate, disclosed **buyer-side platform fee** where a regulated professional supplies the work, Razorpay Route for any money that belongs to a professional, and no listing fee, commission, ranking or rating for advocates (D-05, NN-21, NN-22).

| Outcome | Exit-gate measure |
|---|---|
| Public storefront | `/marketplace` serves ≥ 80 seeded LIVE service products in the 18 categories of Appendix M §M.2, server-rendered, indexable, WCAG 2.2 AA; browse, search, filter and read price cards with no login and no cookie wall |
| Services without a plan | A visitor with no account buys a fixed-price service in ≤ 7 taps on mobile / ≤ 8 clicks on web from the service page, including OTP sign-up (Appendix C J-28) (OTP sign-up → GST profile only if business → Razorpay hosted checkout); GST tax invoice e-mailed by OH8 within 15 minutes of capture |
| Landed price | 100% of LIVE price cards show professional/service fee, LawDocs platform fee (where applicable), government/statutory fee estimate with basis, GST, **total payable now**, exclusions, refund rule and SLA (NN-22, NN-50); lint blocks any card without them |
| Professional-conduct compliance | CI proves restricted fields (ratings, fees per advocate, photos, badges, "top", "book this lawyer") cannot render for advocates; per-profession switches for commission, listing, ratings and percentage fees are locked OFF without a counsel-opinion reference and a checker (NN-21) |
| Retainers | A retainer moves from proposal to eSigned SLA schedule to active RM-as-maker grant in ≤ 2 working days; hour bank, SLA attainment and monthly report visible to the client in real time |
| Delivery quality | ≥ 90% of milestones delivered within SLA in the pilot cohort; auto-refund on professional no-show within 2 hours (R1 IMP-009) |
| Money safety | 0 rupees of professional fees held in a LawDocs account; every professional payout is a Route transfer with an idempotency key reconciled daily (NN-22, NN-46) |
| Academy | Course catalogue from trainings.lawdocs.in synced daily; stale-feed fallback works; no paid course content copied (D-16) |
| Portability | Every engagement, retainer, deliverable, SLA report and invoice reference appears in `LD-EXPORT-1.0` under `09 Services and Engagements/` (company) or the individual mapping in §13 (NN-11) |

---

### Integrations to respect

| Port | Adapter(s) | Use | Failure behaviour / fallback |
|---|---|---|---|
| `BILLING_PORT` | OH8 (default), LOCAL (interim, P17 §4L), MOCK | SKUs, quotes, orders, invoices, credit notes, Route instructions | OH8 down: browsing continues from last signed catalogue; checkout shows "We'll confirm shortly" and queues quote; no order without OH8 confirmation |
| `DIRECTORY_PORT` | OH9 | Credential verification, suspension events, Rule 36 fields | OH9 down: no new activations; existing ACTIVE professionals continue; suspension events replayed on recovery |
| `ESIGN_PORT` | P08 adapters (Leegality / Digio / Melento / Surepass-type; D-12) | Engagement letters, SLA schedules, panel agreements | ESP down: second ESP route; else OTP click-wrap below threshold; above threshold, wait |
| `PAYOUT_ROUTE` | Razorpay Route via OH8 | Linked accounts, on-hold transfers, releases, reversals | Transfer failure: retry with same idempotency key; break → OH8 task; never manual payout |
| `ACADEMY_PORT` | Graphy API [VERIFY] / signed JSON-CSV feed | Course catalogue, corporate enrolments, completion export | Stale-feed fallback (FR-P16-75) |
| `WORKSPACE_PORT` | M365 (Teams), Google (Meet) | Scoping calls, consult video | Built-in WebRTC call [REC] or phone call-back |
| `CONFLICT_PORT` | OH `POST /v1/conflicts/check` | Group institutional conflicts | Down: hold engagement in SCOPING; never skip |
| `CLAIMS_GATE_PORT` | OH14 | Service copy, CSAT statements, bundle claims | Down: publishing blocked |
| `CRM_PORT` | OH3 via `int` | Consented quote-request leads | Queue; never block the visitor |
| `LDC_PORT` | `int` → LDC (Appendix Y event) | Routing group-listing orders | Queue with consent artefact; buyer sees "Your order is with LawDocsComply" |

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] Storefront, service studio, offers, engagements, retainers with SLA engine, practitioner workspace, disputes, reviews, Academy feed and group listings live behind the flags in §9.
- [ ] ≥ 80 LIVE seeded services across 18 categories (Appendix M §M.2) with complete price cards; 4 retainer packages configured (Appendix L §L.7).
- [ ] Engagement-letter, SOW, SLA schedule, panel agreement, marketplace buyer terms and professional terms approved by counsel (Appendix M §M.9).
- [ ] Tax memo signed for SACs, RCM/exempt statements, ECO TCS/TDS treatment and pure-agent lines (OI-P16-04).
- [ ] All §12 scenarios and NN tests green; accessibility audit (axe + manual) passed on SCR-P16-01…14 (NN-28).
- [ ] Settings registered in Appendix R; help keys registered in `hlp`; errors registered with messages.
- [ ] Export-map entries registered (below); Appendix X and Y requests filed.

**Demo script.** (1) Anonymous visitor finds "Rent agreement — professional review", reads the landed card, buys with a new Free account on mobile in ≤ 7 taps including OTP sign-up (J-28); invoice e-mail arrives. (2) In-house professional delivers; QA releases; deliverable appears in the buyer's vault; buyer accepts. (3) Startup buys a Startup Legal Officer retainer; SLA schedule eSigned; RM grant approved by the founder; hour bank and SLA dashboard move during the demo. (4) Console shows advocate commercial fields as non-editable; a CA listing change is rejected without counsel reference. (5) Academy course list renders from the feed; stale-feed fallback demonstrated.

**Export-map entries (`xpt.export_map`, `LD-EXPORT-1.0`)**

| Record type | Company path | Individual path |
|---|---|---|
| `mkp.engagement` | `09 Services and Engagements/<FY>/<Service title> (LD-ENG-…)/{01 Engagement Letter and SOW, 02 Inputs, 03 Deliverables, 04 Correspondence, 05 Invoices and Receipts, 06 Change Requests}` | `10 Receipts and Invoices/<Year>/Services/<Service title> (LD-ENG-…)/`; deliverables also linked from their category folder |
| `mkp.retainer` | `09 Services and Engagements/<FY>/Retainers/<Package> (LD-ENG-…)/{01 Agreement and SLA Schedule, 02 Monthly Reports, 03 Deliverables, 04 Hour Bank and SLA Statements, 05 Invoices}` | n/a |
| `mkp.review` (own) | `99 System Data (CSV and JSON)/marketplace/reviews.csv` | `99 System Data/marketplace/reviews.csv` |
| `mkp.dispute` | `09 Services and Engagements/<FY>/<…>/07 Disputes/` | `10 Receipts and Invoices/<Year>/Services/<…>/Disputes/` |
| `aca.certificate` | `07 People and HR/Training Certificates/<Year>/` | `04 Employment/Training Certificates/` |
| `mkp.professional` (practitioner's own) | `99 System Data/practitioner/` (practitioner export) | — |

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P16-01 | LawDocs Panel structure: affiliated advocates' firm vs contracted panel; invoicing (advocate bill with RCM + LawDocs platform fee) | Owner + [COUNSEL] | `mkp.model.m2.enabled` OFF; M1 non-reserved services only |
| OI-P16-02 | Counsel opinion: assigned-professional model, buyer-side flat platform fee, publishing panel SKU prices, Route collection of advocates' fees vs BCI r.36/r.37 and fee-sharing bar; status of *Sulekha.com v. P.N. Vignesh* | [COUNSEL] | M2 OFF; directory OFF |
| OI-P16-03 | Boundary of DOCUMENTATION class (bespoke drafting by LawDocs staff) vs "practice of law" (*A.K. Balaji*) | [COUNSEL] | Bespoke drafting via panel (M2) with LawDocs documentation support only |
| OI-P16-04 | Tax memo: SAC per class, ECO registration, s.52 TCS exclusion for RCM/exempt, s.393(1) Sl. 8(v) TDS, pure-agent duty lines | [TAX MEMO] | M2 OFF until signed |
| OI-P16-05 | ICAI/ICSI/ICMAI current positions on platforms; CA/CS switches | [COUNSEL] | Locked OFF |
| OI-P16-06 | Individual course checkout: Academy (Graphy) or OH8; Graphy API/SSO capability | Owner + integration lead | Deep link; signed feed |
| OI-P16-07 | Academy brand clean-up ("FinLegal Academy" absent on live site; wPractical leakage — R5 §1.3) | Owner | `aca.display_name` |
| OI-P16-08 | Razorpay Route: MCC approval for legal-services marketplace, transfer fee, on-hold limits | Finance [VERIFY] | M2 OFF |
| OI-P16-09 | E-Commerce Rules 2020 sub-rules and any 2026 amendment applicable to a services marketplace (seller info, ranking disclosure, grievance timelines) | [COUNSEL] [VERIFY] | Adopt duties as policy |
| OI-P16-10 | Trade Marks Act s.145 agent rules and TM-agent conduct for platform listing | [COUNSEL] [VERIFY] | TM filings by advocates on the panel |
| OI-P16-11 | Deemed acceptance, refund timelines, SLA credit values, click-wrap threshold | Owner | Defaults marked [OWNER TO SET] |
| OI-P16-12 | App-store rules for selling professional services in the mobile apps (person-to-person services vs digital goods) — coordinate with P22 | P22 lead [VERIFY] | Services purchasable in app via Razorpay only if confirmed; else web hand-off |

**Conflicts recorded for the master.** R4 §11.6 suggests advocates pay "a flat listing/subscription fee"; this conflicts with D-05/NN-21 and the OH8/OH9 deny lists — this phase follows D-05 (no listing fee for advocates). R3 LG-113 says clients choose advocates and LawDocs does not assign for a fee; conventions fact 11 binds the assigned-professional model — implemented with buyer choice (FR-P16-31) and counsel confirmation (OI-P16-02). Commercial-model letters differ from LDC P21 (LDC M2 = direct, M3 = Route; here M2 = Route, M3 = direct) because Route is LawDocs's primary third-party rail.

## Phase P17 — Plans, Subscriptions, Billing, GST, Revenue-Stream Switches and Savings Dashboard

**File:** `phases/P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P02 (tenancy, Personal/Company workspaces, maker-checker), P03 (settings registry, Configuration Studio, rules), P19 core (`int` gateway, OH8 adapter, signed-artefact verification), P20 core (`xpt.export_map`), P21 core (public-site shell for `/pricing`); P01 for sign-up and GST/PAN profile fetch. External: Operations Hub **OH8** (catalogue, price books, coupons, stream gates, quotes, orders, subscriptions, signed entitlements, GST invoices, credit notes, receipts, Razorpay hosted checkout, Subscriptions, e-mandates, Smart Collect, Route, dunning, revenue accounting — Ecosystem Spec §6.27; OH Master Prompt OH8.1–OH8.10), **OH14** (claims gate), **OH3** (consented leads), **OH6** (billing disputes).
> **Sequencing:** Wave 1. Sprints 1–3 build `BILLING_PORT`, the presentation catalogue, entitlement mirror and checkout (frozen at end of sprint 3 for P16). Sprints 4–5: credits, meters, Settings → Billing & Membership, dunning. Sprints 6–7: revenue-stream registry UI, Pricing Studio, Savings & Value. If OH8 is not live at sprint 3, the interim `LOCAL` adapter (§4L) ships behind an owner decision (OI-P17-01). Every producing module (sgn, ai, lit, ipm, dms, ntf, int, mkp) registers its meters by its own phase exit.
> **Binding appendices:** L (Pricing, Plans, Revenue-Stream Registry and Savings Model), M (marketplace fees, for buyer-fee lines), K (`LD-EXPORT-1.0`), R (settings), W (open items), X (Operations Hub additions — new stream types and meters), Y (Ecosystem Spec v1.2 change request — LawDocs as `UsageRecorded` producer).
> **Requirements covered:** R-017, R-019, R-021, R-027, R-030, R-033, R-034, R-035, R-036, R-040, R-042, R-049, R-054, R-063.
> **Decisions applied:** D-02, D-05, D-08, D-11, D-13 · **Challenges applied:** CH-08, CH-19, CH-21, CH-25 · **Non-negotiables tested:** NN-01, NN-11, NN-18, NN-19, NN-20, NN-21, NN-22, NN-29, NN-35, NN-36, NN-38, NN-39, NN-45, NN-46, NN-50
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration 1 — OH8/Razorpay, QA 1, product/finance analyst 1)

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P17_Plans_Subscriptions_Billing_Revenue_Streams_and_Savings.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P17-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

Give every LawDocs user a plan they understand at a glance, a price they can trust before they pay, and a billing area they can run themselves — upgrade, downgrade, buy credits, download GST invoices, cancel — with no phone call and no dark pattern (R-035, R-036, R-042; NN-50). Give the owner switchable revenue streams with legality gates and kill switches (R-054; NN-18, NN-39). Show every customer, in Settings, an honest Savings & Value account of hours saved, money saved against published market prices and exposure avoided by meeting deadlines — each figure with its formula and evidence class (R-063; NN-36).

LawDocs does not build a billing engine (D-02). OH8 owns money, tax and documents; LawDocs (`bil`, `sav`) owns presentation, entitlement enforcement, metering at source, credits as applied, the billing UI and the savings ledger.

| Outcome | Exit-gate measure |
|---|---|
| Clear pricing page | `/pricing` shows Personal, Pro and Business cards (+ Free and Enterprise links), monthly/annual toggle with saving in ₹ and %, ex-GST price **and total incl. GST** on every card, ≥ 100-row comparison table, "benefits explained", ≥ 25 FAQs; server-rendered; WCAG 2.2 AA |
| Self-serve | Free → paid in ≤ 4 clicks from the pricing page for a signed-in user; upgrade with prorated quote preview in ≤ 3 clicks from Settings; cancellation in no more steps than purchase |
| Never-block floor | 0 cases where non-payment, plan limits or downgrade block reading, exporting, verifying a signed document, nominee access or a deadline reminder already set (test `NN-11_billing_never_blocks`) |
| Money and tax correctness | 0 prices or taxes computed outside OH8 (CI contract test); 100% of invoices e-mailed within 15 minutes of issue and filed in the vault |
| Credits, not wallets | No stored-value balance in rupees exists; all prepaid purchases are service-unit credits redeemable only for LawDocs's own services |
| Revenue-stream control | 45 streams in the registry with owner, effective date, disclosure, tax, refund rule and gate status; a kill switch hides a stream from all surfaces within 5 minutes |
| Honest value | 100% of Savings tiles show formula, inputs, period and evidence class; Modelled exposure never counted in "money saved" or ROI |

---

### Integrations to respect

| Port / adapter | Use | Failure behaviour |
|---|---|---|
| `BILLING_PORT` → OH8 (`/v1/catalogue/versions/{v}`, `/v1/billing/quotes`, `/v1/billing/orders`, `/v1/billing/invoices`, `/v1/usage-disputes`, `/v1/entitlements`) | All commerce | Offline tolerance (FR-P17-05) |
| Razorpay (through OH8 only; LOCAL interim) | Hosted checkout, Subscriptions, UPI AutoPay, e-mandates, Smart Collect, refunds | Webhooks verified by OH8; LawDocs never holds keys except under LOCAL |
| GSTIN status lookup (licensed GSP/vendor via P01) | Billing profile validation | Format check only; user confirms |
| OH14 claims gate | Pricing copy, benefits, savings marketing claims | Publishing blocked |
| OH3 (`int`) | Enterprise enquiries, consented | Queue |
| OH6 | Billing disputes | Ticket queued; dunning pause instruction sent to OH8 |
| P20 `xpt` | Export pack on cancellation/termination | Retry; never blocks cancellation |

---

### Exit gate, deliverables and open items

**Checklist**

- [ ] `BILLING_PORT` with OH8 adapter certified against the OH8 sandbox (catalogue, quote, order, entitlements, invoices, usage, disputes); LOCAL adapter only if OI-P17-01 decided.
- [ ] Pricing page, comparison (≥ 100 rows), benefits, FAQs and configurator published from the presentation catalogue; claims gate PASS; accessibility audit passed.
- [ ] Settings → Billing & Membership pages SCR-P17-10…28 live for Personal and Company workspaces.
- [ ] Credits, meters (all producing modules registered), statements and disputes working; no rupee balance anywhere.
- [ ] Stream registry seeded with RS-LD-01…45 and deny list; kill-switch latency test green.
- [ ] Savings & Value with methodology v1, baselines, benchmarks and penalty bindings (Appendix L §L.12) reviewed by `PLT_LEGAL_REVIEWER`.
- [ ] Settings in Appendix R; help keys in `hlp`; errors registered; Appendix X/Y requests filed.

**Demo script.** (1) Visitor compares plans, toggles monthly/annual, sees incl.-GST totals, starts a Personal trial without a card. (2) User converts to annual, pays by UPI on Razorpay hosted page; invoice e-mail arrives and appears in the vault. (3) User buys a 10-pack of eSign credits; one eSign fails and the credit returns. (4) Company admin adds 3 seats with prorated quote; CFO approves above threshold. (5) Admin cancels in 3 steps; workspace reverts to Free at term end with all data readable and exportable. (6) Console: switch off Trademark watch with checker; it disappears from pricing within 5 minutes. (7) Savings & Value shows hours saved (estimate), money saved vs dated benchmarks, deadlines met and Modelled exposure in its own labelled tile.

**Export-map entries**

| Record type | Company path | Individual path |
|---|---|---|
| `bil.invoice`, `bil.credit_note`, `bil.receipt` | `10 Billing and Invoices/<FY>/{Invoices, Credit Notes, Receipts}/` | `10 Receipts and Invoices/<Year>/` |
| `bil.statement`, `bil.usage_statement` | `10 Billing and Invoices/<FY>/Statements and Usage/` | `10 Receipts and Invoices/<Year>/Statements/` |
| `bil.contract` (order forms, MSA, renewal notices) | `10 Billing and Invoices/<FY>/Contracts and Order Forms/` | `10 Receipts and Invoices/<Year>/Plan Terms/` |
| `bil.tds_certificate` | `10 Billing and Invoices/<FY>/TDS Certificates/` | — |
| `bil.credit_ledger`, `bil.billing_history` | `99 System Data (CSV and JSON)/billing/` | `99 System Data/billing/` |
| `sav.snapshot`, `sav.value_report` | `10 Billing and Invoices/<FY>/Value Reports/` + `99 System Data/savings/` | `99 System Data/savings/` |

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P17-01 | OH8 live date vs P17 sprint 3; LOCAL interim adapter decision | Owner + OH lead | LOCAL behind flag |
| OI-P17-02 | Final price points, GST-inclusive display for B2C, refund windows | Owner `[OWNER TO SET]` | R6 seeds |
| OI-P17-03 | PPI/closed-system analysis of credits; voucher time-of-supply and revenue recognition for credit packs and breakage | [COUNSEL] + [TAX MEMO] | Credits limited to LawDocs services; refundable rule |
| OI-P17-04 | SAC per SKU (SaaS, facilitation, platform fee), TDS characterisation guidance for buyers | [TAX MEMO] | Tax hint "18% — confirmed on invoice" |
| OI-P17-05 | e-mandate limits and pre-debit rules under RBI e-mandate Directions 2026; Razorpay plan-change constraints | Finance [VERIFY] | OH8 behaviour |
| OI-P17-06 | Apple/Google store billing rules for India (digital subscriptions, credits) | P22 lead [VERIFY] | `bil.mobile.purchase_mode = WEB_HANDOFF` |
| OI-P17-07 | Time-and-motion study to replace seed activity baselines | Product + ops | Baselines labelled "default estimate" |
| OI-P17-08 | New OH8 stream types and meters (Appendix X) and `UsageRecorded` producer registration (Appendix Y) | OH lead | Map to nearest existing stream type |

**Conflicts recorded.** R6 §R6.2.4 sets pack validity at 12 months with no refund rule; R1 IMP-085 asks for refundable or non-expiring paid balances — this phase sets 12 months with reminders, one free extension and pro-rata refund within 30 days and on closure (owner to confirm). NN-36 classes (MEASURED/ESTIMATED/MODELLED) replace LDC's Recorded/Modelled/Estimated naming.

## Phase P18 — Delivery Console and Operations Hub Interface

**File:** `phases/P18_Delivery_Console_and_Operations_Hub_Interface.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (Keycloak realms `ld` and `ld-staff`, passkeys, step-up MFA), P02 (tenancy, legal entities, departments, user types, maker-checker engine, grant primitive), P03 (settings registry, rule engine), P04 (Legal Vault/DMS, sharing, folder intake), P09 runtime (Vidhi briefs and drafting, agent sponsorship), P13 (departments, positions and Company Legal Department OS roles), P16 (engagements `eng_`, retainers `rtn_`, SLAs `sla_`, professional registry `pro_`, assignment engine), P17 (billing presentation, entitlements mirror, `BILLING_PORT`), P19 (`int` gateway, `WORKSPACE_PORT`, OH contracts, webhook signing), P20 (`xpt.export_map`, `LD-EXPORT-1.0`). P15 supplies the consumer-case model used by the queue in §4I. **External:** Infrabyx Operations Hub (OH1 group identity and grants, OH1.6 conflict service, OH3 CRM, OH4 onboarding factory, OH5 customer success, OH6 support desk, OH8 billing, OH9 directory, OH10 staff HRMS, OH11 internal controls, OH12 workplace); Microsoft Graph (now); Google Workspace APIs (later, flag OFF).
> **Sequencing:** Start when P02 and P04 have exited and the P16 engagement/retainer schema is frozen (freeze point F-P16-ENG). Sprints 1–3: staff realm, portfolio, client section, delivery grants, act-in-tenant sessions, credential vault. Sprints 4–5: master-data change requests, deliverables, messages/meetings/drives, SLA tracker, practitioner workspace. Sprints 6–7: OH interfaces (contract-tested against the OH sandbox), timesheets and metrics, consumer case queue (built in Wave 2 behind `chp.brand.enabled = false` — the P15 key; switched on with P15 in Wave 3). **P18 must exit before any retainer or LDaaS engagement goes live** (P16 gate).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), X (Operations Hub and LawDocsComply Addenda), D (roles, personas and access matrix), R (settings catalogue), K (`LD-EXPORT-1.0`), M (marketplace professional rules), Y (Ecosystem Spec v1.2 change request), W (verification log and open items), Q (competitive research and improvement backlog: IMP-003, IMP-010, IMP-012, IMP-087).
> **Requirements covered:** R-014, R-026, R-027, R-028, R-030, R-037, R-039, R-047, R-048, R-050, R-051, R-052, R-053, R-055, R-058, R-062, R-064, R-065, R-066, R-067, R-068, R-080, R-083 (queue only).
> **Decisions applied:** D-02, D-03, D-05, D-06, D-10, D-11, D-17 · **Challenges applied:** CH-07, CH-08, CH-09, CH-10, CH-16, CH-24, CH-26, CH-29, CH-31, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-16, NN-17, NN-18, NN-19, NN-21, NN-23, NN-24, NN-25, NN-28, NN-29, NN-32, NN-33, NN-39, NN-41, NN-43, NN-45, NN-46
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration engineer 1, security engineer 1, QA 1)

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P18_Delivery_Console_and_Operations_Hub_Interface.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P18-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs sells legal services as well as software: one-time drafting and filings, retainers (Startup Legal Officer, SME Legal Desk, NBFC Legal & Compliance Retainer — Appendix L §L.7), Managed Legal Department (LDaaS) and marketplace engagements (P16). People deliver that work — relationship managers (RMs), in-house professionals, consumer case managers and third-party professionals. **The Delivery Console** (`apps/delivery`, work.lawdocs.in) is their workplace. It gives each staff member one portfolio, a **dedicated section per client company**, a governed way to act as **maker** inside the client's own tenant while the client's employee remains the **checker** (R-064), a client-owned **credential vault** (NN-16), a transparent **master-data change workflow** (CH-26, R-066), and clean interfaces to the Infrabyx Operations Hub (OH) for CRM, onboarding, tickets, customer success, billing, staff identity and timesheets (D-02) — without copying any tenant document, matter, credential or personal content into OH (NN-19).

The console is **not** the Operations Hub (no CRM, marketing, HRMS, payroll or billing engine here) and **not** the Super Admin console (`apps/console`). It is the client-service surface that sits between them (R-048).

| Outcome | Exit-gate measure |
|---|---|
| One portfolio | An RM sees every assigned client with next breach, SLA risk, open tasks, unread messages and grant expiry on one home screen; any client section opens in ≤ 2 clicks from home |
| Governed maker access | Every LawDocs maker in a client tenant holds a client-approved, scoped, time-bound delivery grant; no delivery user can ever be a checker, approver, signatory, director or auditor in a client tenant (`NN-17_delivery_never_checker`) |
| Fast client approval | A client admin approves a proposed grant in ≤ 2 taps from the notification on web or mobile; median proposal-to-active time ≤ 4 working hours (measured) |
| Credential vault | OFF by default; when ON, delegation is offered first, secrets are revealed just-in-time with reason, every view/copy/change is logged and visible to the client; OTPs, DSC PINs and recovery codes cannot be stored |
| Master-data integrity | No crucial client detail (legal name, PAN, CIN/LLPIN, GSTIN, registered office, owner contacts, authorised signatories) changes without client approval, a second Super Admin checker and notification to all owners (`NN-18_masterdata_maker_checker`) |
| Commercial clarity | The client section's Billing tab shows exactly what the client sees on its own Billing page (same component, same OH8 data); RMs cannot change prices, credits or entitlements |
| Clean OH interface | Tickets, CRM activities, onboarding milestones, CSAT/NPS, health signals and timesheets flow through Ecosystem-Spec contracts; a contract test proves no document text, matter data, credential, message body or end-customer personal data leaves LawDocs (`NN-19_no_content_to_oh`) |
| Proportionate productivity | Work is measured by outcomes (tasks, SLAs, deliverables accepted first time, CSAT); sessions are recorded only for attendance; no covert monitoring (NN-33, CH-24, CH-32) |
| Ethical wall | Consumer case managers work in a separate brand queue; no person holds both a Consumer Help role and a delivery grant in a lender/insurer tenant (`NN-23_people_wall`) |

---

### Integrations to respect

| Port / API | Counterparty | Vendor alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| SCIM 2.0 + OIDC | Entra ID (group IdP fed by OH10/OH12) | Google Cloud Identity (later) | Queue and retry; hourly reconciliation; new staff cannot sign in until provisioned | Manual provisioning in `apps/console` with maker-checker, logged as exception (OI-P18-02) |
| `POST /v1/conflicts/check` | OH1.6 (extended) | — | Fail closed: no activation without an answer | Delivery lead records a manual conflict attestation with evidence, valid 24 h |
| `POST /v1/support/tickets`; ticket events | OH6 | — | Outbox retry; ticket shown "queued" | Email to support role mailbox |
| `POST /v1/crm/activities`, `POST /v1/crm/requests`, CRM account read | OH3 | Brevo is OH's executor, never called by LawDocs directly | Retry; activity kept locally ≤ 7 days then dropped with notice | None needed |
| `BILLING_PORT` (quotes, invoices, entitlements) | OH8 | P17 local adapter only if Appendix X §X.7 LOCAL decision is taken | Billing tab shows last mirror with as-of time | — |
| `POST /v1/delivery/assignments` (inbound) | OH4 | — | Reject unsigned; idempotent on project id | Delivery lead assigns in UI |
| `WORKSPACE_PORT` | Microsoft Graph (ON); Google Workspace (OFF) | — | Meeting creation fails → offer "paste a meeting link"; drive copy fails → DMS copy stands, retry | Paste link manually |
| `DMS_PORT` (internal) | P04 | — | Release blocked until filed | — |
| `NOTIFY_PORT` (`packages/notify`) | Email (SES/Brevo transactional), push, in-app; SMS/WhatsApp via DLT-registered CPaaS (NN-34) | JioCX, others | Channel fallback per preference | — |
| `KMS` | AWS KMS ap-south-1 (per-tenant CMK for `cvl`) | CloudHSM for Enterprise (optional) | Vault read-only if KMS unavailable; no plaintext fallback | — |

---

### Exit gate, deliverables and open items

**Exit checklist**

- [ ] `apps/delivery` screens SCR-P18-01…29; tenant/mobile screens SCR-P18-30…34; console screens SCR-P18-35…36.
- [ ] Grant engine, standing authorisation, act-in-tenant token exchange, support sessions and break-glass; external penetration test of the token exchange and the reveal service with no high findings open.
- [ ] Credential vault with KMS envelope encryption, delegation-first registry (each delegation text verified and logged in `docs/compliance/verification-log.md` — NN-38; unverified routes ship as "check the portal's help page" only).
- [ ] Master-data change workflow end to end, including recovery hold and order-compelled path; counsel sign-off on notice wording.
- [ ] OH contracts (tickets, CRM activities, assignments, health signal, timesheets, metrics, surveys, conflict check, SCIM, `EmployeeOffboarded`) contract-tested against the OH sandbox, or stubbed with recorded fallbacks where Appendix X items are not yet built.
- [ ] `WORKSPACE_PORT` M365 adapter certified (meetings, calendar, `Sites.Selected` working sites, drive copy); Google adapter built behind flag OFF.
- [ ] Consumer queue built behind `chp.brand.enabled = false` (P15 key); people-wall and conflict tests green.
- [ ] All §12 scenarios and NN tests green; axe + manual screen-reader pass on SCR-P18-01, -17, -18, -30, -31.
- [ ] Settings in §9 registered in Appendix R; help keys in §6 registered in `hlp`; error codes registered.

**Export-map entries (`xpt.export_map`; `LD-EXPORT-1.0`, Appendix K)**

| Record type | Folder path |
|---|---|
| `sdc.deliverables` + files | One-time engagements: `09 Services and Engagements/<FY>/<Service title> (LD-ENG-…)/03 Deliverables/`; retainers: `09 Services and Engagements/<FY>/Retainers/<Package> (LD-ENG-…)/03 Deliverables/` (Appendix K §K.3.1 governs — X-07) |
| `msg` threads with LawDocs team | One-time: `…/04 Correspondence/`; retainers: `…/06 Messages/` (PDF transcript + JSON) |
| `sdc.meetings` | Retainers: `…/07 Meetings/` (agenda, notes, attendee list); one-time: `…/04 Correspondence/` |
| SLA clocks and monthly reports | Retainers: `…/02 Monthly Reports/` and `…/04 Hour Bank and SLA Statements/` |
| `sdc.delivery_grants`, sessions, access log | `99 System Data (CSV and JSON)/access_transparency/` |
| `cvl` register (metadata), grants, reveal log | `01 Company Profile/Credential Vault (metadata only)/` |
| `sdc.masterdata_requests` + Correction Entries | `01 Company Profile/Change History/` |
| Invoices mirror | `10 Billing and Invoices/<FY>/` (from P17) |
| Staff-side time entries and metrics | Not in client exports (staff HR data; exported from OH10 for the employee) |

**Demo script (15 minutes):** RM home → open NBFC client → propose Secretarial grant → client approves on phone → RM acts in tenant, drafts board resolution, submits to checker → client checker approves → QA releases monthly report → delivered to client OneDrive → client admin views access log → RM requests MCA21 reveal; client approves; reveal logged → RM raises registered-office change; owner approves; second Super Admin applies; notices sent → leaver event suspends a second RM's grants → contract test report for OH payloads.

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P18-01 | Portal terms on sharing RBI CIMS/DAKSH/PRAVAAH, FIU-IND, CIC member and CERSAI credentials with service providers | [COUNSEL] + client compliance | Client-only default + acknowledgement |
| OI-P18-02 | Group IdP and SCIM source for LawDocs staff (Entra ID tenant, domain) | CTO / OH12 | Manual provisioning with maker-checker |
| OI-P18-03 | Actual Microsoft 365 SKU held (CH-29); Intune/conditional access availability for managed-device reveal | [OWNER] | Device registration + risk-based step-up |
| OI-P18-04 | Graph and Google scope names; `Sites.Selected` admin-consent process | Integration lead [VERIFY] | Plain links only |
| OI-P18-05 | Delegation routes per portal (GST Practitioner, income-tax authorised representative/CA, EPFO/ESIC sub-users, MCA professional users) | PLT_LEGAL_REVIEWER [VERIFY] | Generic "check the portal" text |
| OI-P18-06 | Whether LawDocs-employed advocates/CAs may issue work product in their professional capacity (NN-41, D-05) | [COUNSEL] | Company work product for non-reserved services; reserved work by engaged practitioners only |
| OI-P18-07 | Consumer Help entity: non-advocate case managers as authorised representatives (RB-IOS 2026 Cl. 10(1)(b)) | [OWNER] + [COUNSEL] | User self-files with LawDocs drafting |
| OI-P18-08 | E-mail bridge domain, DMARC alignment | CTO | In-app messaging only |
| OI-P18-09 | Ecosystem Spec v1.2 acceptance of proposed events (Appendix Y) | Pack lead / spec owner | Local outbox with REST polling by OH |
| OI-P18-10 | Outsourcing-register entry format for RE clients without LDC | [COUNSEL] | Downloadable record only |

## Phase P19 — Integration Gateway, Ecosystem Connectors and Developer Platform

**File:** `phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, transactional outbox, audit ledger, KMS, Temporal, OpenTelemetry), P02 (tenancy, roles, maker-checker, delivery grants), P03 (settings registry, flags). Built on P19 later: P01 (KYB/identity adapters), P04 (vault deposits), P07/P08 (eSign/eStamp adapters, hosted signing hand-off), P09 (MCP server edge), P11/P12 (court-data and trademark adapters), P13 (LDC system-of-record switch), P17 (OH8 billing connector), P18 (Delivery Console UI over the OH connector), P20 (storage targets, `LD-EXPORT-1.0`). External: Infrabyx Ecosystem Integration Specification v1.1 (committed unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, SHA-256 checked in CI), the `infrabyx-contracts` registry, the Ecosystem PKI, `@infrabyx/connector-sdk`, and the Appendix Y change request (Ecosystem Spec v1.2) for every LawDocs-specific contract.
>
> **Sequencing:** **Core (Wave 1, sprints 1–3):** gateway, OAuth 2.1 profile, scopes, error model, idempotency, correlation, rate limits, outbox relay, tenant webhooks, DLQ, connector runtime, Operations Hub connector, eSign/eStamp/KYB adapter scaffolding for P01/P08, minimum developer portal. **Full (Wave 2, sprints 4–9):** LDC, Finbyx, Udofin and Equator connectors (behind `int.eco.v12_contracts.enabled` until Appendix Y is merged), partner onboarding API, court-data, trademark, workplace, accounting, HRMS and CRM adapters, Zapier/Make and iPaaS, SDKs, sandbox personas, health dashboard, certification workbench. **Freeze:** scope catalogue and tenant webhook catalogue (Appendix I §I.6–§I.7) freeze at the end of sprint 3; later changes follow FR-P19-06.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), I (Integration Adapters and API Catalogue), Y (Ecosystem Spec v1.2 Change Request — LawDocs), K (`LD-EXPORT-1.0`), R (settings), D (roles), F (instrument eligibility, via P08), M (professional rules), W (verification log). The Ecosystem Spec prevails for any cross-product contract (NN-24).
> **Requirements covered:** R-002, R-003, R-005 (KYB pre-fill transport), R-006 and R-078 (eSign/eStamp adapters), R-012 and R-076 (court data), R-013 (trademark data), R-021 and R-022 (connector framework, stable IDs), R-023, R-024 (bulk intake by API), R-029 and R-062 (Jio channels as adapters), R-034 (payments via OH8), R-041 and R-081 (Academy feed), R-050 (CRM openness via OH3/Brevo), R-053 and R-055 (Microsoft 365, Google Workspace), R-058, R-067 (sharing ledger).
> **Decisions applied:** D-01, D-02, D-10, D-11, D-12, D-14, D-16 · **Challenges applied:** CH-02, CH-03, CH-04, CH-05, CH-06, CH-13, CH-16, CH-17, CH-27 · **Non-negotiables tested:** NN-01, NN-05, NN-06, NN-07, NN-11, NN-13, NN-18, NN-19, NN-23, NN-24, NN-25, NN-32, NN-34, NN-38, NN-39, NN-46, NN-47
> **Estimated effort:** 9 two-week sprints (core 3 in Wave 1), squad of 8 (gateway and platform 3, ecosystem connectors 2, third-party adapters 2, developer experience 1)

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P19_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P19-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

LawDocs must exchange data with four sister products, the group Operations Hub and many third-party systems without each new counterparty becoming a project, and must make "onboarding of new companies easy" (R-002, R-003). P19 delivers one gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK with mapping packs, a file fallback — and the module `int`, the **only** LawDocs module that publishes or consumes cross-product events (master §5.3). Modules write internal events to the outbox; `int` decides, through registered contracts, what may leave LawDocs, to whom, on which consent or legal basis, and records each movement in a **sharing ledger** the customer can read (CH-16).

Three boundaries shape the design; the brief's wording is challenged where it would breach them:

1. **eSign is not shared.** "Data shareable across ecosystem apps both ways" (R-023) does not extend to LawDocs' ASP capability: an ASP may integrate eSign "only for applications owned or operated by them", and consent and logs stay with the ASP (CCA eSign FAQ; R3 LG-007) [LAW]. Finbyx, Udofin, Equator, LDC and the Operations Hub never use LawDocs' ESP route. A sister product's user signs through LawDocs only as a **LawDocs customer**, in a LawDocs tenant, on a LawDocs-hosted ceremony under LawDocs' consent screen — or the sister product uses its own ESP (NN-06). P19 offers a **hosted signing hand-off**, not an eSign API.
2. **Cross-product data needs a contract and a reason.** No shared database, no direct table reads; every message is a registered event, API or layout with `consentref` or `legalbasis` (NN-24; Spec principles 1, 5). LawDocs has no owner code in Spec v1.1; Appendix Y raises the change request and v1.2-dependent flows stay behind a flag until it is merged (NN-38).
3. **Walls stay up.** Consumer Help (`chp`) exchanges nothing with Finbyx, Udofin, Equator or LDC tenants (NN-23); the Hub receives only commercial records and aggregates (NN-19; Spec principle 12); the Equator neutrality wall covers LawDocs staff identities (Spec §4.6).

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | Spec §14.3 groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, Aggregates only, Isolation, Archive and storage, plus Appendix Y §Y.13 "Legal-tech boundaries", pass; `ConnectorCertified` emitted for OH, LDC, Finbyx, Udofin and Equator connectors in sandbox |
| One way in | 100% of machine traffic passes the gateway; no module controller reachable outside it |
| Easy company onboarding | A 500-row partner batch gets KYB pre-fill for ≥ 90% of valid CINs/GSTINs at ≤ 5 s p95 per row; invitations go out the same day; activation ≤ 4 taps from the email |
| Time to first API call | ≤ 15 minutes from developer sign-up to an authenticated sandbox call (usability test, 5 developers) |
| Reliable events | Outbox lag p95 ≤ 30 s; webhook delivery p95 ≤ 5 min; zero loss in a 4-hour counterpart-outage drill; DLQ replay only under maker-checker |
| Every share visible | Each cross-product movement of tenant or personal data appears in the sharing ledger within 60 s with counterparty, purpose, basis, record ids and hash |
| No portal automation | No HTTP client in the gateway or connector runtime targets eCourts, IP India, MCA21, GSTN portal UI, CKYCR, bureaus, Parivahan or income-tax portal domains; CI egress test passes (NN-05) |

### Integrations to respect

Ports, primary and fallback vendors, legality, status and kill switches are binding in Appendix I §I.2; ecosystem connectors in Appendix I §I.4. Failure rules common to all ports: (1) a port failure never blocks reading or exporting the customer's own data (NN-11); (2) every port has a fallback vendor or a manual path — wet-ink pack for eSign, uploaded stamp certificate with UIN check for eStamp, manual entry with document upload for KYB, user-entered CNR and uploaded orders for court data, uploaded status PDF for trademarks, ICS feed for calendars, signed pack download for ODR, email for messaging; (3) OH8 unavailability keeps the last signed entitlement for 30 days and queues orders (Spec §6.27); (4) stale third-party data is labelled with its "as of" time, never presented as live (NN-20).

### Exit gate, deliverables and open items

**Exit checklist**

- [ ] Gateway, OAuth profile, scopes, error model, idempotency, correlation and rate limits live in all environments; BOLA suite green.
- [ ] Outbox relay, inbox, tenant webhooks, ecosystem push, DLQ with maker-checker replay; 4-hour outage drill with zero loss.
- [ ] OH connector certified in sandbox (provisioning, catalogue, quotes, orders, invoices, entitlements, usage); aggregates-only tests pass.
- [ ] LDC, Finbyx, Udofin and Equator connectors certified in sandbox; v1.2-dependent contracts inert until Appendix Y is merged, manual interim channel tested.
- [ ] Partner onboarding API with KYB pre-fill, invitations, consent and activation; dry run; partner webhooks.
- [ ] Adapters scaffolded and certified for Wave 1 ports (eSign, eStamp, KYB, DigiLocker, messaging, OH8); Wave 2 ports per Appendix I §I.2 status.
- [ ] Developer portal, sandbox personas, simulators, SDKs (TypeScript, Python), Postman, OpenAPI/AsyncAPI downloads, Zapier/Make/Power Automate connectors in private beta.
- [ ] Integration health dashboard (tenant and platform), status page, reconciliation jobs, kill switches.
- [ ] Settings registered in Appendix R; help keys registered in `hlp`; export-map entries registered; error codes registered.
- [ ] Gherkin `@P19-AT-01…27` green; NN tests `tests/nn/NN-01, -05, -06, -07, -11, -13, -18, -19, -23, -24, -25, -32, -34, -38, -39, -46, -47` green.

**Demo script (20 minutes).** (1) Developer signs up and makes a sandbox call in under 15 minutes. (2) Partner uploads a 50-row batch; a signatory activates in four taps. (3) A webhook endpoint fails; DLQ replay with two admins. (4) Finbyx sandbox creates a hosted signing request; the ceremony opens on `sign.lawdocs.in`; a POA request is refused with a wet-ink pack. (5) A Udofin sandbox borrower links and deposits a sanction letter; the sharing ledger shows it. (6) A contract dispute is referred to the Equator sandbox; an award returns into the vault with advisory clocks. (7) OH8 receives the month's usage aggregates; a seeded identifier is rejected.

**Deliverables.** `apps/api/src/int/**`, `packages/connectors/**` (ports and adapters), `packages/contracts/**`, `docs/interfaces/api.md`, `docs/interfaces/webhooks.md`, `docs/ecosystem/infrabyx-integration-spec.md` (unchanged copy), `infrabyx-contracts/proposals/2026-10-25-add-lawdocs-ld.md` (from Appendix Y), developer portal site, SDK repositories, certification reports.

**Open items**

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-P19-01 | Approval of Appendix Y (Ecosystem Spec v1.2) by every affected product owner | [OWNER] | Manual interim channel, logged (FR-P19-27) |
| OI-P19-02 | ESP/aggregator written confirmation that API-initiated, LawDocs-hosted ceremonies for a customer's own documents are within ASP terms and not sub-letting | [COUNSEL] + procurement | Disable `int.esign.api_initiation.enabled` |
| OI-P19-03 | B2C billing identity to OH8 (`CONTRACT_PERFORMANCE_CUSTOMER`, `PII` ceiling) | [OWNER] + PLT_DPO | LawDocs issues B2C invoices itself (deviation from D-11) |
| OI-P19-04 | Consumer Help conflict-check API at OH and conflict policy | [COUNSEL] + OH lead | Manual conflict declaration by user + staff check |
| OI-P19-05 | LDC P26 legal-matter/CLM overlap with D-10 (LawDocs SoR) | Pack leads (LDC, LD) | Tenant-level choice recorded in `LDC_SOR` link |
| OI-P19-06 | Court-data aggregator contracts (two vendors) with lawful-collection warranties | Procurement + [COUNSEL] | Manual CNR only |
| OI-P19-07 | Zapier/Make partner terms, data residency and transfer assessment | PLT_DPO | Power Automate + webhooks only |
| OI-P19-08 | Graphy API/feed for FinLegal Academy catalogue | Academy lead | Curated catalogue import |
| OI-P19-09 | A2A agent-task contracts across products | Ecosystem spec owners | Not built |
| OI-P19-10 | JioCX DPA, India-processing and no-training terms; WhatsApp BSP status | Procurement | Meta Cloud API direct + other DLT aggregator |
| OI-P19-11 | Equator clause API endpoint and model-clause licence | EQ lead | Manual reviewed import |
| OI-P19-12 | Entity Locker requester API coverage for company onboarding | P01 lead | Licensed MCA-data vendor + document upload |

## Phase P20 — Data Preservation, Portability, BYO Storage and Migration Safety

**File:** `phases/P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (prefixed ULIDs, audit ledger with daily anchors, S3 SSE-KMS + versioning + Object Lock, expand-migrate-contract framework, Temporal), P02 (approvals, delegations), P03 (settings registry, `wf.items`, configuration bundle), P04 (Legal Vault/DMS: documents, versions, SHA-256 at ingest, folders as views, retention classes, legal hold), P19 core (connector framework, `int`, secrets vault for connector credentials), P05 (document classification — Wave 2 import assist), P08 (evidence packs and BSA s.63 certificate generator). Every module that persists records registers its record types in `xpt.export_map` before its own exit gate (NN-11) — enforced by the CI contract test built here.
> **Sequencing:** **Core (Wave 1, 2 sprints):** extend the P00 export-map registry head and its CI contract test (FR-P00-87; `NN-11_export_map_complete` and `ci/export-contract` are the same gate) in sprint 1, before P04 exits; `LD-EXPORT-1.0` builder for on-demand full and partial exports with download, folder/ZIP import with rule-based placement, golden archives. **Full (Wave 2, 4 sprints):** BYO storage targets and continuous mirror, scheduled exports, AI-assisted import classification, verifier and loader tools, exit/offboarding, region and vendor move runbooks, ecosystem archive sharing.
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), K (export package `LD-EXPORT-1.0` and folder taxonomy — binding for every folder, file name, format and manifest field), R (settings `xpt.*`), D (roles), F (eligibility — for evidence-pack contents), Y (Ecosystem Spec v1.2 change request: folder-profile registration and `portability` producer). **The Infrabyx Ecosystem Integration Specification v1.1 §12.1 (archive standard 1.0) and §12.2 (customer-controlled storage connector contract) prevail on conflict** (NN-24); `LD-EXPORT-1.0` is LawDocs' set of folder profiles within that standard.
> **Requirements covered:** R-021, R-022, R-024, R-068, R-011 (preserve), R-043 (selective export/sharing), R-053, R-055, R-023 (archive sharing across ecosystem apps), R-031 (DPDP portability and erasure), R-061, R-067 (audit trail export).
> **Decisions applied:** D-01, D-02, D-06, D-10, D-11 · **Challenges applied:** CH-15, CH-16, CH-29 · **Non-negotiables tested:** NN-01, NN-02, NN-04, NN-09, NN-10, NN-11, NN-12, NN-13, NN-17, NN-18, NN-19, NN-24, NN-25, NN-26, NN-32, NN-42, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints (core 2 in Wave 1; full 4 in Wave 2), squad of 8 (portability core 3 backend, connectors 2, import 1, frontend 1, QA/verification 1).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P20_Data_Preservation_Portability_BYO_Storage_and_Migration_Safety.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P20-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

A LawDocs user must never feel trapped and must never lose a document. On any day — while subscribed, after cancelling, during a court case, when an auditor asks, or when a company switches tools — any individual or company can take **everything** as an ordinary folder tree of Word, Excel, PDF/A, CSV and original files, with self-explanatory folder and file names that a person can follow in Windows Explorer or macOS Finder without LawDocs. A company can keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, Google Drive, SFTP server, NAS or data centre). The same taxonomy works in reverse: a user drops an existing folder of 3,000 agreements and LawDocs files them, instead of the user uploading one by one (R-024).

Because folder paths are **views over permanent canonical IDs** and the export layout is a versioned contract rather than today's code, the owner can push patches, add features, change the database engine, swap storage vendor or move data centre without any customer re-filing or migrating data (R-021, R-022, NN-12).

| Outcome | Exit-gate measure |
|---|---|
| Everything exportable (NN-11) | Export-coverage test: every persisted record type maps to `xpt.export_map`; a seeded tenant with every record type exports with 100% count reconciliation per type and 100% of originals byte-identical (SHA-256) |
| Understandable without LawDocs | Usability test: 5 of 5 non-technical participants (a homeowner, an office manager, a junior lawyer, a startup founder, an external auditor) each find a named signed agreement with its stamp certificate and signing evidence, a court order, and the audit trail of a status change within 3 minutes using only Explorer/Finder and Office |
| Verifiable offline | Open-source verifier (Apache-2.0) confirms checksums, the detached JWS, control totals and audit-chain continuity; fails on one changed byte or one missing file |
| Stable across change (R-022) | Golden-archive test: the same synthetic tenants exported before and after (a) a release with schema changes, (b) a PostgreSQL major upgrade, (c) a storage-vendor swap, (d) a region-move rehearsal give identical paths, file names and IDs for unchanged records; differences only as additions declared in `CHANGES-SINCE-PREVIOUS.csv` |
| BYO storage (R-021) | A tenant connects S3, Azure Blob, SharePoint and SFTP targets; residency and canary pass; continuous mirror lag p95 ≤ 15 min; nightly reconciliation zero drift; restore test from the tenant's own copy passes |
| Bulk intake (R-024) | A 5,000-file folder imports with ≥ 90% automatic placement on a tidy tree (100% for a tree previously exported by LawDocs), duplicates linked by hash, every unplaced file in a correction queue before commit, nothing overwritten, full undo for 7 days |
| Exit without friction | Exit export of a 200 GB company completes in ≤ 24 h; read-only period; deletion certificate; never blocked by billing state |

---

### Integrations to respect

| Port | Adapters | Failure behaviour | Manual fallback |
|---|---|---|---|
| `STORAGE_TARGET_PORT` (Spec §12.2) | S3, S3-compatible, Azure Blob, GCS, Microsoft Graph (SharePoint/OneDrive), Google Drive API, SFTP, on-prem agent | Pause; alert; never silent re-route | Download and copy manually |
| `SUITE_PORT` (P19) | Microsoft Graph, Google Workspace | Token expired → reconnect prompt | Download |
| `DIX_PORT` (P05) | Classification and extraction | Unavailable → rule-based mapping only; more items to review | Manual correction grid |
| `AV_SCAN_PORT` | ClamAV-type engine in isolated container | Unscanned files quarantined | — |
| `SIGNATURE_VALIDATION_PORT` (P08) | PAdES/PKCS#7 validation | "Not verified" label | — |
| `KMS_PORT` | AWS KMS; customer BYOK grants | `key_unavailable` fail-closed | — |

Graph and Drive throttling: honour `Retry-After` and 429/503 with exponential back-off and jitter; resumable uploads for large files; per-tenant concurrency caps [VERIFY current Graph and Drive quotas at build].

---

### Exit gate, deliverables and open items

**Deliverables:** `packages/export` (builder, profiles, naming, manifest, signing), `xpt` schema and APIs, verifier `ld-verify` and loader `ld-load` (Apache-2.0; CLI + desktop build) in `verify/`, storage adapters (Wave 2) certified per Spec §14.3, on-premises agent (signed installer, auto-update, mTLS), import pipeline and review grid, golden workspaces and CI gates, move runbooks (`docs/runbooks/data-moves/*.md`), exit runbook template, help articles.

**Exit gate (core, Wave 1):** export-map coverage 100% for the record types of the Wave 1 phases built so far (P00–P04, P06–P08, P17, P19 core, P21 core; P05 and other Wave 2 types at the full gate); FULL and RECORD exports for Company and Individual profiles; folder/ZIP import with rule mapping, duplicates, review, report and undo; golden-archive diff in CI; PDF/A and render gates; s.63 certificate draft; scenarios AT-01–09, 15–17, 21 green (AT-14 needs AI import classification, which is Wave 2).

**Exit gate (full, Wave 2):** all scenarios green; S3, Azure Blob, GCS, SharePoint/OneDrive, Google Drive, SFTP and agent targets certified; mirror lag p95 ≤ 15 min over 7 days on the pilot tenant; restore test from a customer copy passes; exit rehearsal for a 200 GB synthetic tenant ≤ 24 h; region-move rehearsal (ap-south-1 → ap-south-2) with empty golden diff; usability test (5/5) passed.

**Registered:** export-map entries for `xpt.export_jobs`, `xpt.storage_targets` (metadata only), `xpt.import_jobs` + `import_files` → `99 System Data (CSV and JSON)/Exports, Imports and Storage/` with human `Export and import history.xlsx`; import reports → `99 System Data (CSV and JSON)/Exports, Imports and Storage/Import reports/`; deletion certificates and exit records → `00 Start Here/` of the exit package and `01 Company Profile/Account and Exit/`. Settings `xpt.*` in Appendix R; help keys `hlp.xpt.export_everything`, `hlp.xpt.manifest`, `hlp.xpt.checksum`, `hlp.xpt.verify`, `hlp.xpt.restricted_archive`, `hlp.xpt.byo_storage`, `hlp.xpt.residency`, `hlp.xpt.mirror`, `hlp.xpt.conflict`, `hlp.xpt.import_review`, `hlp.xpt.duplicate`, `hlp.xpt.undo_import`, `hlp.xpt.exit`, `hlp.xpt.deletion_certificate`, `hlp.xpt.s63_certificate`, `hlp.xpt.folder_policy`. Errors `LD-XPT-001`–`LD-XPT-099`. Screens SCR-P20-01–15.

**Demo script:** a founder drags a messy 2,000-file Google Drive folder into LawDocs, fixes 30 proposals and commits; an NBFC legal head connects SharePoint and watches an executed agreement appear in the mirror within minutes; the SRE renames a database column via expand-migrate-contract and the golden diff stays empty; an individual exports everything on her phone and verifies the checksum on a laptop.

| ID | Open item | Owner | Fallback |
|---|---|---|---|
| OI-P20-01 | Appendix Y §Y.11 registers all four profiles (`ld_company_v1`, `ld_individual_v1`, `ld_professional_v1`, `ld_consumer_help_v1` — X-08) and proposes `owner_readable`; awaiting Spec v1.2 acceptance | [OWNER] / ecosystem architecture board | Cross-product archives use `ids_only` |
| OI-P20-02 | Microsoft Graph permission names (SharePoint `Sites.Selected`, OneDrive app folder), upload-session limits and residency evidence; Google Drive `drive.file` behaviour on shared drives | P19 lead | Download-only for that provider |
| OI-P20-03 | BSA 2023 s.63 Schedule wording; who signs Part B for SaaS-held records | [COUNSEL] | Draft labelled "for review by your advocate" |
| OI-P20-04 | Companies (Accounts) Rules 2014 r.3(5) current text for India back-up of electronic books | Content team | Treat books as India-only (protective) |
| OI-P20-05 | DigiLocker requester-terms permitted retention purposes | P01 / NeGD | Reference-only exports |
| OI-P20-06 | Price and plan placement of `LD-ADD-BYO` | [OWNER TO SET] with P17 | Business add-on, Enterprise included |
| OI-P20-07 | Retention period for LawDocs' own tax records (CGST s.36; Income-tax Act 2025 equivalents) | [TAX MEMO] | 8 years |

## Phase P21 — Public Website, No-Code CMS (Blog/Vlog), SEO/GEO, Help Centre, Tutorials, "i" Glossary and Accessibility

**File:** `phases/P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, `apps/public` scaffold, CDN, legacy-site inventory and the seed 301 map, host decision `https://www.lawdocs.in`); P01 (consent ledger and notice versions, OTP sign-up, account creation from the drafter); P02 (roles, maker-checker engine, screen and menu registry that carries `help_key` and `data-tour-id`); P03 (settings registry, rules register `rul` used for citations, stamp-duty and jurisdiction facts); P06 (published templates and questionnaires behind the "Draft free with Vidhi" block); P08 (instrument eligibility gate, Appendix F, for the eSign badge; State stamp registry); P09 runtime (Vidhi help mode and the content-drafting agent); P16 (marketplace catalogue, service tiers and professional rules rendered on public pages); P17 (plans, prices, credit packs, trial rules rendered on the pricing page); P19 core (`int` gateway for Operations Hub CRM, support desk, claims gate and asset library calls). External: Operations Hub OH3 (CRM), OH7 (marketing, social calendar, asset library), OH14 (claims gate); YouTube; Google Search Console and Bing Webmaster Tools; IndexNow; a plagiarism-check provider; `TRANSLATE_PORT` providers.
> **Sequencing:** Wave 1 delivers §4A–§4H core (site shell, rendering, multi-brand theming, 301 map, legal policies from Appendix O, pricing page, marketplace storefront shell, the top 50 content pages from Appendix N §N.9 wave 1, the CMS with DOCX import and blog, 150 glossary terms, the help panel framework and the accessibility statement). Wave 2 adds vlog, tutorials pipeline, guided tours, landing-page builder, Hindi plus four further D-07 languages and 350 glossary terms. Wave 3 completes the ≈626 manual-derived pages, the remaining D-07 languages, 500+ glossary terms, ISL tutorial renditions and the Consumer Help brand site. **First slice for the P00 cut-over:** the SSR shell, host rules and the redirect-target pages P00 needs (P00 §5.5, T−28 d) depend only on P00 and do not wait for P06; the "Draft free with Vidhi" blocks attach when P06 publishes templates, and until P16 exits (Wave 2) the storefront shell renders the P17 presentation catalogue (OH8 feed). Freeze points: the URL scheme (§4B) and the block schema (§4I) freeze at the end of sprint 2; after that, changes go through expand → migrate → contract (NN-12) with redirects.
> **Binding appendices:** N (website copy system, SEO/GEO, tutorials and video plan), O (legal policies), U (accessibility specification), M (marketplace professional rules), F (instrument eligibility), R (settings registry), D (roles), K (`LD-EXPORT-1.0`), H (agent roster), X (Operations Hub addendum: CRM, funnels, social calendar, asset library), Y (Ecosystem Spec v1.2 change request), W (open items).
> **Requirements covered:** R-004, R-008, R-016, R-019, R-020, R-025, R-030, R-032, R-036 (pricing page rendering), R-041 (open marketplace and academy entry), R-056 (funnel surfaces; OH is system of record), R-070, R-071, R-072, R-073, R-074, R-075 (public pages for added services), R-082 (startup section), R-086 (competitor-informed IA), R-087, R-088, R-089, R-090, R-091.
> **Decisions applied:** D-01, D-02, D-04, D-05, D-06, D-07, D-08, D-11, D-13, D-15, D-16, D-17 · **Challenges applied:** CH-08, CH-11, CH-12, CH-14, CH-20, CH-21, CH-30 · **Non-negotiables tested:** NN-02, NN-07, NN-11, NN-14, NN-18, NN-19, NN-20, NN-21, NN-22, NN-26, NN-28, NN-29, NN-30, NN-31, NN-32, NN-35, NN-38, NN-45, NN-48, NN-49, NN-50
> **Estimated effort:** 10 two-week sprints, squad of 8 (2 front-end, 1 back-end, 1 content engineer, 1 SEO/technical-content lead, 1 accessibility specialist (IAAP CPACC or WAS), 1 product designer, 1 QA), plus a standing content team of 4 (two legal writers, one technical writer, one video producer) and a reviewer of record (`PLT_LEGAL_REVIEWER`) for legal pages. Wave split: Wave 1 = 4 sprints, Wave 2 = 3, Wave 3 = 3.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P21_Public_Website_CMS_SEO_GEO_Help_Centre_and_Accessibility.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P21-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The live lawdocs.in is a client-side single-page application. A crawler or AI engine sees only a `<head>`: one title and one meta description on every URL, no H1, no body and no links (R5 §1.1). The sitemap lists non-www URLs that fail, `robots.txt` blocks `/buy/` while the sitemap lists 20 `/buy/*` URLs, and the positioning is compliance-first rather than documents, eSign and Vidhi. The manuals hold about 626 usable pages of content after de-duplication, but 21 sections contain copied competitor or Wikipedia text, the testimonials look adapted from proposal software, and much of the law is out of date (CrPC/IPC/Evidence Act, CPA 1986, Udyog Aadhaar, Income-tax Act 1961, pre-Code labour statutes) (R5 §3–§5).

This phase replaces that site with a server-rendered, multi-brand public website and a no-code content system, and builds the help layer that every authenticated app uses.

**Who benefits**

| Audience | Outcome |
|---|---|
| Individuals and small businesses | Find the right document, pleading or service in plain language; draft free from a vetted template; see whether eSign is legally valid for that instrument; see the full price before paying; hire a professional at a fixed price. |
| Companies and legal teams | Clear module, pricing and marketplace pages; tutorials and tours that shorten onboarding; contextual "i" explanations of legal and product jargon. |
| Search engines and AI answer engines | Unique, indexable, citable pages with answer-first summaries, visible FAQs, valid structured data, named reviewers and dated citations. |
| Users with disabilities | WCAG 2.2 AA and IS 17802 conformant pages, captions, transcripts, Indian Sign Language (ISL) renditions of core tutorials, easy-read summaries, a working feedback channel (Appendix U). |
| LawDocs operations (`OPS_CONTENT_PUBLISHER`) | Publish a blog post from a categorised Word file in under 10 minutes, with maker-checker and legal review, without a developer (R-089). |

**KPIs (measured from go-live of each wave)**

| KPI | Target |
|---|---|
| Indexable routes returning server HTML with a unique title, meta description, one H1 and ≥ 150 words of main content | 100% (CI-enforced) |
| Legacy URLs (186 sitemap URLs plus known indexed URLs) resolving 200 or a single-hop 301/410 | 100% |
| URLs passing Core Web Vitals at p75 on mobile (field data, Search Console) | ≥ 90% within 90 days of each wave |
| Published legal pages with a reviewer of record and a last-reviewed date | 100%; pages without one are `noindex` automatically |
| Pages failing the plagiarism gate at publication | 0 |
| Pages citing superseded law without a "(formerly …)" mapping | 0 (outdated-law linter) |
| DOCX → published blog post median time (publisher + checker) | ≤ 10 minutes of hands-on time |
| Lead captured → visible in Operations Hub CRM | ≤ 60 seconds p95 |
| Glossary coverage | 150 terms (Wave 1), 350 (Wave 2), ≥ 500 (Wave 3), each with plain definitions in all enabled D-07 languages |
| UI strings tagged as jargon without a registered "i" key | 0 (lint) |
| Automated axe-core serious or critical violations on any public template | 0; manual audit per Appendix U §U.8 each release |
| Free draft → paid action (eSign, eStamp, clean download or professional review) | ≥ 15% [target to calibrate — R4 §11.10] |

**Done for users** means: a visitor lands on `/documents/property-transactions/rent/rent-agreement-residential`, reads a 50-word answer, sees that eSign is valid, drafts the agreement in five to eight questions, sees the State stamp duty with its source and verification date, and either pays to eStamp and eSign or hires a professional, in ≤ 3 clicks from the page and with every fee shown separately before payment.

### Integrations to respect

| Port / adapter | Default | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `int` → OH3 CRM (`POST /v1/crm/requests`) | Operations Hub | — (Brevo only via OH) | Retry 72 h, dead-letter alert | Export CSV of `web.leads` in DEAD_LETTER for manual upload by OH |
| `int` → OH support desk (`ops.ticket:write`) | Operations Hub | — | Queue; show email/phone | Email support address |
| `int` → OH14 claims gate | Operations Hub | Local claims register only (degraded: blocks new claims) | Cached last PASS for 24 h; new claims blocked | `PLT_CONTENT_EDITOR` removes claim |
| `int` → OH7 asset library / social calendar | Operations Hub | — | Retry; clip stays downloadable | Manual download |
| `VIDEO_PORT` | YouTube Data API | Vimeo (adapter) | Use cached metadata | Manual metadata entry |
| `PLAGIARISM_PORT` | Licensed API (Copyscape-type) [VERIFY terms and India data handling] | Quetext/Turnitin-type | Block legal submissions; allow drafts | Manual check by reviewer with evidence upload |
| `TRANSLATE_PORT` | Per P05 (Bhashini [VERIFY], Google/Azure fallback) | — | Keep English | Human translation |
| `TTS_PORT` | Per P05/P09 Indic TTS adapter | On-device TTS (mobile) | Hide Listen control | — |
| Search Console, Bing Webmaster, IndexNow | Official APIs | — | Skip ping; retry | Manual submission |
| Gotenberg/LibreOffice | `.doc` → `.docx`, PDF of policies | — | Reject `.doc` with message | Ask publisher to save as `.docx` |
| `PAYMENTS` | Not called here; checkout links to P17 | — | — | — |

### Exit gate, deliverables and open items

**Exit checklist (per wave)**

- [ ] No-JS crawl gate green for every sitemap URL; legacy URL suite green (P21-AT-01/02).
- [ ] Lighthouse CI and field CWV within budgets for every template; JS budgets enforced.
- [ ] Structured-data validation green; no `Review`/`AggregateRating`/`HowTo` emitted.
- [ ] Wave content published: Wave 1 top 50 pages (Appendix N §N.9) + home, product, pricing, marketplace shell, legal policies (Appendix O), accessibility statement; Wave 3 ≈626 manual-derived pages, each with reviewer of record, plagiarism pass and outdated-law pass.
- [ ] Content Studio: DOCX import, maker-checker, legal review, scheduling, rollback, preview, export demonstrated by `OPS_CONTENT_PUBLISHER` without developer help.
- [ ] Glossary coverage met for the wave; lint enforced in all apps.
- [ ] Tutorials and tours for the wave's core journeys published with captions; ISL renditions for the core set by Wave 3.
- [ ] Appendix U release gate passed (axe zero serious/critical; manual NVDA, JAWS, VoiceOver, TalkBack, keyboard-only and 400% zoom audits; user testing round with disabled users); conformance report published.
- [ ] Lead hand-off to OH CRM verified end to end with consent artefacts; Appendix Y entry for LawDocs as CRM caller submitted.
- [ ] Settings registered in Appendix R; help keys registered; error codes registered with help keys.
- [ ] **Help-key registry (owned here; X-10).** Help keys and settings are separate registries: a help key is `hlp.<module>.<term>`, and terms not tied to one module use `hlp.gen.<term>`; no key uses the form `hlp.hlp.<term>`, and help-centre and website terms are registered as `hlp.gen.*` or `hlp.web.*`. Seeded in this phase: `hlp.gen.indemnity`, `hlp.gen.consideration`, the Appendix U keys `hlp.gen.accessibility_preferences`, `hlp.gen.easy_read`, `hlp.gen.listen`, `hlp.gen.isl_video`, `hlp.gen.assisted_signing`, `hlp.gen.assisted_kyc`, `hlp.gen.accessibility_feedback`, and the Appendix N §N.12 priority list. Registered for other phases at integration review: `hlp.chp.vehicle_loan` (P15 FR-P15-70 — "My vehicle loan": what papers to keep, NOC and Form 35 on closure, where to complain about recovery conduct; Consumer Help brand locale set). The registry lint (`LD-HLP-001`) also fails any key using the `hlp.hlp.` form.
- [ ] Export-map entries registered in `xpt.export_map` (below).

**Demo script:** (1) open `/documents/property-transactions/rent/rent-agreement-residential` with JS off and show full content; (2) draft in 7 answers, sign up inline, save to vault; (3) open the power-of-attorney page and show the wet-ink pack; (4) import a categorised DOCX folder, fix a flagged CrPC citation, submit, approve as a second user, schedule; (5) show the post live with reviewer footer, IndexNow log and OH asset-library push; (6) open the help panel on the signing screen, open "i" for "eStamp certificate", play the tutorial with captions; (7) submit accessibility feedback and show the SLA clock.

**Export-map entries (`xpt.export_map`, NN-11)**

| Record type | Folder in `LD-EXPORT-1.0` |
|---|---|
| `hlp.tenant_note` | `99 System Data (CSV and JSON)/Help Notes.csv` (company) |
| `hlp.user_pref` | `99 System Data (CSV and JSON)/Accessibility Preferences.csv` (company, professional; individual: `99 System Data/` — Appendix K §K.3.2, §K.3.5) |
| `web.testimonial` (the user's own, with consent record) | `99 System Data (CSV and JSON)/Testimonials and Consents.json` (individual: `99 System Data/`) |
| `hlp.a11y_issue` (submitted by the signed-in user) | `99 System Data (CSV and JSON)/Accessibility Feedback.csv` (individual: `99 System Data/`) |
| Platform content (LawDocs' own CMS, not tenant data) | Platform export via FR-P21-91 (Markdown + JSON + assets) |

**Open items (Appendix W candidates)**

| OI | Item | Owner |
|---|---|---|
| OI-P21-01 | Public phone number and contact identity for the site (three numbers in use — R5 §1.3) | [OWNER] |
| OI-P21-02 | AI training-bot and `Google-Extended` policy | [OWNER] board decision |
| OI-P21-03 | Folder list and category mapping for the owner's blog Word files | [OWNER] |
| OI-P21-04 | `[Consumer Help Brand]` name, domain and entity profile (D-06) | [OWNER] |
| OI-P21-05 | LawDocs as caller of OH CRM (`POST /v1/crm/requests`, `/v1/crm/leads`, `/v1/crm/activities`), ticket and asset-library APIs — now proposed in Appendix Y §Y.8/§Y.9 and Appendix X §X.22; asset-library path to be fixed by the OH owner (OI-Y-10) | Pack lead / OH owner |
| OI-P21-06 | **Resolved by X-22:** Content Studio is an `apps/console` area restricted to `OPS_CONTENT_PUBLISHER`, `PLT_CONTENT_EDITOR` and `PLT_LEGAL_REVIEWER`; Super Admin not required | Pack lead (closed) |
| OI-P21-07 | Verify Google FAQ rich-result deprecation, Shorts/Reels length limits, YouTube privacy-enhanced-mode behaviour and current AI crawler user agents at build | SEO lead [VERIFY] |
| OI-P21-08 | Plagiarism provider terms and data handling | `PLT_DPO` [VERIFY] |
| OI-P21-09 | Counsel view on cookieless aggregate analytics under DPDP and on "English prevails" clause for translated policies | [COUNSEL] |
| OI-P21-10 | Verify IT Rules 2021 grievance and synthetic-media labelling text as amended 20 Feb 2026 for site footer and video labels | [VERIFY] / [COUNSEL] |
| OI-P21-11 | Engage ISL interpreters and a disabled-user testing panel (Appendix U §U.8) | `OPS_QA_REVIEWER` |

## Phase P22 — Mobile Apps (iOS/Android) and Store Release

**File:** `phases/P22_Mobile_Apps_and_Store_Release.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (OIDC realms, OTP, passkeys, consent ledger, Aadhaar offline verification flows), P02 (workspaces, roles, maker-checker), P04 (vault APIs, Object Lock, hashes), P05 (OCR, type copy, translation renditions), P06/P07 (questionnaires, Drafting Studio, redlines, deal rooms, messaging), P08 (eligibility gate, eStamp, ESP adapters, evidence packs), P09 (Vidhi runtime), P11/P12 (case and trademark status), P15 (Consumer Help cases — v2), P16/P17 (catalogue, checkout, entitlements), P19 (gateway, webhooks), P20 (export jobs), P21 (`hlp` content, glossary, tours, tutorials). External: Apple App Store Connect, Google Play Console, Expo Application Services (EAS Build, Submit, Update), APNs/FCM, Play Integrity API, App Attest, Razorpay React Native SDK, the eSign aggregator chosen in P08.
> **Sequencing:** Wave 2 ships v1 of the LawDocs app (individuals and companies: vault, scan, share import, drafting, negotiation, eSign/eStamp, approvals, case/TM status, Vidhi chat, marketplace purchase, notifications). Wave 3 ships v2: the `[Consumer Help Brand]` flavour, Vidhi voice in all D-07 languages, practitioner-lite space for `PRO_*`, offline Vidhi help. The BFF contract (`/m/v1`) freezes at the end of sprint 2; device-trust and offline-cache designs pass a security review (P23) before any store submission.
> **Binding appendices:** U (accessibility), F (instrument eligibility), K (`LD-EXPORT-1.0`), M (marketplace rules), N (store listing copy, video plan), R (settings), D (roles), H (Vidhi agents), W (open items), Y (ecosystem change request).
> **Requirements covered:** R-008, R-010, R-011, R-012, R-013, R-017, R-019, R-025, R-030, R-034, R-043, R-044, R-045, R-061, R-064 (approvals), R-068, R-077, R-078, R-083, R-084 (status and deep links; v2).
> **Decisions applied:** D-01, D-06, D-07, D-11, D-12, D-14, D-15 · **Challenges applied:** CH-01, CH-02, CH-11, CH-12, CH-13, CH-15, CH-28, CH-30 · **Non-negotiables tested:** NN-01, NN-03, NN-04, NN-06, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-18, NN-20, NN-22, NN-23, NN-26, NN-28, NN-32, NN-34, NN-37, NN-44, NN-46, NN-48, NN-50
> **Estimated effort:** 9 two-week sprints (v1 6, v2 3), squad of 8 (3 React Native engineers, 1 native-module engineer (iOS/Android), 1 back-end engineer for `mob` and the BFF, 1 mobile security engineer (shared with P23), 1 product designer with accessibility specialism, 1 QA/device-lab engineer).

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P22_Mobile_Apps_and_Store_Release.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P22-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The owner wants users to keep LawDocs "the way people use DigiLocker": always on the phone, used to prepare, negotiate, sign, amend and preserve agreements (R-011, R-017). LegalKart's app is a consultation wallet; LawDocs' app is the Legal Vault plus signing and drafting in the pocket (R1 §3.7). The phone is also where most evidence is born: photographs of stamp papers, handwritten receipts, WhatsApp chats and screenshots (CH-28).

**Outcomes and KPIs**

| KPI | Target |
|---|---|
| First document from install to signed (template lane, Aadhaar eSign, eligible instrument) | ≤ 5 minutes median; ≤ 3 taps from home to start |
| Open a pinned offline document | ≤ 1 s from unlock, no network |
| Signing-invite link → signer reviewing the document (guest, no app) | ≤ 2 taps and one OTP |
| Crash-free sessions (production) | ≥ 99.7% |
| ANR rate (Android) | < 0.47% (below Play "bad behaviour" threshold [VERIFY current threshold]) |
| Cold start to interactive | < 2.5 s mid-range Android; < 4.0 s low-end |
| Download size | ≤ 35 MB Android per-device APK; ≤ 50 MB iOS thinned |
| Parity matrix coverage (every web capability has a mobile status) | 100%, CI-enforced |
| Accessibility: five critical journeys pass manual VoiceOver and TalkBack scripts | 100% per release |
| PII found in crash or analytics payloads in the monthly sample audit | 0 |

**Done** means an individual can scan a stamp paper, draft a rent agreement in Hindi, negotiate one clause in chat, eStamp and eSign, and find the signed copy offline a year later; a company checker can approve a contract from a push notification with biometric step-up; a counterparty can sign from a WhatsApp or RCS link without installing anything.

### Integrations to respect

| Port / adapter | Default | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `PUSH_PORT` | Expo Push | Direct FCM/APNs | Retry; critical → SMS/WhatsApp per NN-34 | In-app inbox |
| Integrity | Play Integrity API; App Attest | — | Degraded mode, alert | Web app |
| Scanner | ML Kit Document Scanner; VisionKit | vision-camera + edge detection | Fallback scanner | Photo picker |
| `ESIGN_PORT` (P08) | Aggregator from P08 via system browser | Second ESP route | Offer retry / second route | Web signing |
| `PAYMENTS` | Razorpay React Native SDK via OH8 orders | Razorpay hosted checkout in browser tab | "Confirming…" then push | Web checkout |
| `BILLING_PORT` (IAP mode) | App Store Server API + Notifications V2; Google Play Developer API + RTDN | — | Entitlement unchanged until verified | Support ticket |
| Speech (ASR/TTS) | On-device where available; P05/P09 Indic adapters | — | Text-only | — |
| Crash/analytics | Self-hosted or India-resident Sentry-type; first-party analytics | — | Drop events locally | — |
| EAS | Build, Submit, Update | Self-hosted build runners (fallback) | Manual build from tagged commit | — |

### Exit gate, deliverables and open items

**Exit checklist (v1, Wave 2; repeat for v2)**

- [ ] Parity matrix complete; `parity-check` green; Maestro flows for every `F` capability.
- [ ] Security review by P23: device binding, integrity, pinning, offline cache crypto, screen protection, OTA signing; mobile VAPT findings closed or accepted.
- [ ] Budgets met on the device lab (§4V); crash-free ≥ 99.7% in closed testing for 14 days.
- [ ] Appendix U mobile gate: automated label checks green; manual VoiceOver/TalkBack scripts for five journeys signed by `OPS_QA_REVIEWER`; disabled-user test round completed.
- [ ] Store packs: listings per locale, screenshots from the tutorial pipeline, App Privacy labels, privacy manifests, Data safety form, review notes, demo accounts, account-deletion path; `PLT_DPO` sign-off on the data inventory.
- [ ] Purchase-method classification approved by the owner and counsel; [VERIFY] items logged in `docs/compliance/verification-log.md` (NN-38).
- [ ] Release train and OTA governance live in `eng` with maker-checker.
- [ ] Settings registered (Appendix R); help keys `hlp.mob.*` registered; error codes registered.
- [ ] Export-map entries registered.

**Demo script:** install on a low-end Android device; sign in by OTP; enable biometrics; scan a stamp paper and an Aadhaar card (masking); share a WhatsApp export into a matter; draft a rent agreement in Hindi; negotiate one change with a guest on another phone via link; eStamp and eSign; open the signed copy offline in airplane mode; approve a company contract from a push; revoke the device from the web and show the wipe.

**Export-map entries (`xpt.export_map`, NN-11)**

| Record type | Folder in `LD-EXPORT-1.0` |
|---|---|
| `mob.device` | `99 System Data (CSV and JSON)/Devices.csv` (individual profile: `99 System Data/Devices.csv` — Appendix K §K.3.2) |
| `mob.push_preferences` | `99 System Data (CSV and JSON)/Notification Preferences.csv` (individual: `99 System Data/`) |
| `mob.capture_metadata` | `99 System Data (CSV and JSON)/Capture Metadata.csv` (individual: `99 System Data/`) (and alongside each document in its folder's evidence sub-folder where flagged as evidence) |
| WhatsApp import original and transcript rendition | The destination folder chosen by the user (e.g., `07 Disputes and Court Cases/<Case>/` for individuals; `03 Litigation and Disputes/…/` for companies) with the rendition labelled |
| `mob.store_receipt` (IAP mode) | `10 Receipts and Invoices/` (individual) or `10 Billing and Invoices/<FY>/` (company) |

**Open items (Appendix W candidates)**

| OI | Item | Owner |
|---|---|---|
| OI-P22-01 | Final bundle and application IDs, developer accounts under the operating entity (D-08), D-U-N-S number | [OWNER] |
| OI-P22-02 | Digital sales mode on iOS and Android (NOT_SOLD_IN_APP vs IAP/Play Billing/alternative billing) and the GST treatment of store sales | [OWNER] + [TAX MEMO] |
| OI-P22-03 | Verify Apple App Review Guidelines 3.1.1/3.1.3(b)–(e) and external-link entitlements for the India storefront; Google Play Payments policy and India alternative billing status | Mobile lead [VERIFY] + [COUNSEL] |
| OI-P22-04 | ESP/aggregator mobile support: system-browser flow vs native SDK; accessibility of ESP pages | P08 lead [VERIFY] |
| OI-P22-05 | Speech provider for Indic ASR/TTS with India-resident processing | P09 lead [VERIFY] |
| OI-P22-06 | Store category (Business vs Productivity) and age rating | [OWNER] |
| OI-P22-07 | Verify OTA clauses (Apple DPLA interpreted code; Google Play self-update policy) and Apple third-party-AI data-sharing disclosure rule | Mobile lead [VERIFY] |
| OI-P22-08 | Whether OH requires a native "ops approvals" space (Appendix X) | Pack lead / OH owner |

## Phase P23 — Engineering Governance, Change/Patch Management, Hardening, VAPT/IS Audit, Certification Readiness and Go-Live

**File:** `phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md`

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (monorepo, CI/CD skeleton, AWS accounts, Terraform, audit ledger, Object Lock buckets, OpenTelemetry), P01 (staff realm `ld-staff`, MFA, break-glass), P03 (settings registry, feature flags, kill switches), P20 (export-map contract test, golden archives, move runbooks) and **every functional phase whose scope is being released**. External: GitHub organisation, Operations Hub **OH13** (engineering console and CAB record, `ChangeApproved`) and **OH14** (control library and provider-assurance room), CERT-In-empanelled auditor, certification bodies.
> **Sequencing:** The governance track (§4A–§4F) starts in sprint 1 of P00 in reduced form and is complete before P04 exits, so that every Wave 1 module is built under the final controls. The hardening, evidence and go-live track (§4G–§4M) runs before each wave's general availability. **P23 re-runs once per wave** (Wave 1 "Vault & Sign GA", Wave 2 "Legal Ops for companies", Wave 3 "Services and Consumer") for the scope released in that wave (§13.3).
> **Binding appendices:** P (security, privacy and certification readiness — control set, claims language, log retention), R (settings `eng.*`), D (staff roles and segregation of duties), K (export package — golden archives), W (open items and the `[VERIFY]` census — `ci/verify-census`), X (Operations Hub addendum: OH13/OH14 interfaces), Y (ecosystem events), Z (brief traceability matrix — `ci/trace-check`). Ecosystem Spec §6.29 (`ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`), §6.26 (`BackupCompleted`, `RestoreTested`) and §14 (versioning and certification) prevail on conflict.
> **Requirements covered:** R-057, R-033, R-034, R-031, R-021, R-022, R-067, R-017 (mobile release governance), R-001 (challenge on certification claims).
> **Decisions applied:** D-01, D-02, D-12, D-14 · **Challenges applied:** CH-19, CH-24 (no surveillance of engineers), CH-32 · **Non-negotiables tested:** NN-02, NN-12, NN-18, NN-20, NN-25, NN-27, NN-28, NN-30, NN-32, NN-33, NN-38, NN-39, NN-45, NN-46
> **Estimated effort:** 6 two-week sprints for the first run (governance 2 with a platform squad of 4 in parallel with P02–P04; hardening and go-live 4 with a squad of 8: SRE ×2, security engineer ×2, QA lead, backend ×2, compliance analyst); each later wave re-run 2 sprints.

### Session prompt

> "Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P23_Engineering_Governance_Change_Patch_Hardening_Audit_and_GoLive.md in full, plus every appendix it lists as binding. Inspect the repository state and the outputs of the phases it depends on. Write docs/phases/P23-plan.md with: scope slice, the five inventories (settings keys, events, error codes, approval actions, export-map entries), data-model and migration notes, risks, acceptance tests, [VERIFY] items the slice depends on, and open items to close or defer. Stop for my approval before writing production code. Build in vertical slices; at the exit gate (§13 of the phase file and master §15) give me the hand-over report."

### Objective

The owner will push code to GitHub often — patches, features, framework upgrades, infrastructure moves — while individuals rely on LawDocs to keep their property papers and signed agreements for decades, and companies rely on it for evidence they will produce in court. P23 makes change safe and provable:

- every change is reviewed, tested, approved by someone other than its author, traceable to a release and reversible;
- customer data and folder structures survive every release and every infrastructure move (with P20);
- backups are proven by restoring them; disaster recovery is drilled;
- vulnerabilities are fixed within published deadlines;
- the platform is ready for an annual CERT-In-empanelled audit, IS and internal audits, client audits and certification (SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001, ISO 22301, PCI DSS SAQ A for hosted checkout) — **without claiming any certification before the certificate or report exists** (NN-20, R-033);
- each wave goes live through a signed checklist and a hypercare period.

| Outcome | Exit-gate measure |
|---|---|
| Every production change approved and traceable | 100% of production deployments in the trailing 30 days map to a change record with a matching `ChangeApproved` (OH13) and a signed image digest; zero deployments outside the pipeline |
| Releases never disturb customer data | `ci/migrations`, `ci/export-contract` and the golden-archive diff (P20) pass for every release; zero customer migration steps in release notes (NN-12) |
| Recoverability proven | Latest restore test of every T0 store passed within RTO; one full DR failover to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence filed |
| Security debt under control | No open Critical; no High past SLA; CERT-In-empanelled audit report issued after retest with Critical/High closed |
| Certification-ready | ≥ 80% of mapped controls with automated evidence; policy set approved by the Board of `[LawDocs Operating Entity]`; external readiness assessment with no Critical gaps; trust page makes no unevidenced claim |
| Safe go-live | Wave checklist signed by CTO, `PLT_SECURITY_OFFICER`, `PLT_DPO`, Company Secretary (owner) and product owner; hypercare exit criteria met |

---

### Integrations to respect

| System | Use | Failure behaviour |
|---|---|---|
| GitHub (Actions, rulesets, environments, security features) | Source, CI, approvals, scanning | Pipeline down → no deploys; emergency path documented |
| Operations Hub OH13 | CAB record; `ChangeApproved`; incident register | OH13 unavailable → local `eng.change_records` with dual human approval and back-fill; deploy gate accepts a locally recorded approval signed by two CAB members for `EMERGENCY` only |
| Operations Hub OH14 | Control library; provider-assurance room; evidence | Local evidence store; back-fill |
| OH10/OH12 | Staff identities and devices (joiner–mover–leaver) | Access reviews flag mismatches |
| AWS (Backup, KMS, Security Hub, GuardDuty, Inspector, CloudTrail) | Backups, keys, posture | Alerts; manual checks in runbooks |
| Expo EAS, App Store Connect, Google Play Console | Mobile builds and releases | Hold release; hotfix via store expedited review where justified |
| CERT-In-empanelled auditor | VAPT and comprehensive audit | Booked ≥ 8 weeks before wave GA |
| Status page provider (India-resident or self-hosted) | Customer communication | Fallback to email and in-app banner |

---

### Exit gate, deliverables and open items

### 13.1 Governance track (before P04 exits)

- [ ] GitHub rulesets, CODEOWNERS, signed commits, PR template, required checks live and exported nightly; drift check running.
- [ ] Environments dev/test/staging/pre-prod/prod/DR provisioned by Terraform with policy checks; OIDC deploy federation; secrets in Secrets Manager.
- [ ] Change records, deploy gate and `ChangeApproved` consumption (or local fallback) working end to end; first `ReleasePublished` emitted.
- [ ] `ci/migrations`, `ci/export-contract`, `ci/golden-archive-diff`, `ci/config-registry`, `ci/axe`, `ci/sbom`, `ci/trace-check` and `ci/verify-census` green on `main` (the census script itself is a P00 deliverable — Appendix W §W.1 step 7).
- [ ] Phase completion report (FR-P23-58) template and validator live; every phase closed in the wave has an approved report.
- [ ] Vulnerability intake and SLA watch running; EOS register seeded.

### 13.2 Go-live track (per wave)

- [ ] Wave go-live checklist complete with all blocking items done and six sign-offs.
- [ ] VAPT for wave scope closed (Critical/High); CERT-In-empanelled annual audit booked or done.
- [ ] Restore tests green for all T0 stores; DR drill within RPO/RTO in the last 6 months.
- [ ] Control evidence ≥ 80% automated (Wave 1 target 60%, Wave 2 80%) [REC]; readiness assessment booked.
- [ ] Manual accessibility audit for wave screens passed.
- [ ] Claims register in force; trust page shows only evidenced claims.
- [ ] Hypercare plan, on-call and status page live.

### 13.3 Re-run per wave

Wave 2 adds: mobile store releases and MASVS testing, litigation data aggregator resilience, marketplace counsel opinion, delivery-console access reviews. Wave 3 adds: Consumer Help entity and ethical-wall tests, telecom (voice/WhatsApp) compliance checks, tax-module freeze windows, longer hypercare.

**Registered:** export-map entries for LawDocs' own platform records are not tenant data and are excluded from tenant exports (`x-export: excluded`, reason "platform engineering records"); tenant-visible artefacts — release notes and maintenance notices — map to `99 System Data (CSV and JSON)/Platform Notices/` in tenant exports. Settings `eng.*` in Appendix R. Help keys `hlp.eng.release_ring`, `hlp.eng.maintenance`, `hlp.eng.early_access`, `hlp.eng.trust_claims`. Errors `LD-ENG-001`–`LD-ENG-060`. Screens SCR-P23-01–19.

**Demo script:** an engineer opens a PR adding a column; CI shows the expand step and export-map update; CAB approves in OH13; two approvers release through rings; a weekly restore test runs and publishes evidence; a simulated KEV vulnerability flows through the emergency lane; the Wave 1 checklist is signed.

| ID | Open item | Owner | Fallback |
|---|---|---|---|
| OI-P23-01 | GitHub plan and security add-on names and pricing | CTO | Compensating controls (FR-P23-01) |
| OI-P23-02 | Applicability details of CERT-In's 2025 audit guidelines to LawDocs | `PLT_SECURITY_OFFICER` | Annual audit by empanelled auditor regardless |
| OI-P23-03 | ESP contract audit frequency and incident-notice terms | P08 lead | Annual ASP audit [REC] |
| OI-P23-04 | Exact Ecosystem Spec domain and type for security-incident notifications | Ecosystem architecture board | Use Spec v1.1 name verbatim once confirmed |
| OI-P23-05 | Store policy limits on over-the-air updates and data-safety declarations | P22 lead | No OTA updates beyond bug fixes |
| OI-P23-06 | PCI DSS SAQ A eligibility confirmation with acquirer/QSA for Razorpay Standard Checkout | OH8 owner | Redirect-only hosted checkout |
| OI-P23-07 | OH13/OH14 availability dates for LawDocs onboarding | Operations Hub programme | Local `eng` system of record with back-fill |
| OI-P23-08 | ITR due dates under the Income-tax Act 2025 for freeze planning | [TAX MEMO] | Freeze configurable by CAB yearly |
