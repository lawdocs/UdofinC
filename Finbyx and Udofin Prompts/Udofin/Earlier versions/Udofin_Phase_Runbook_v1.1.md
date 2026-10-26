# UDOFIN — Phase-wise Claude Code Runbook

**Companion to the Udofin Master Build Prompt v1.1** · 19 October 2026 · ready-to-paste instructions for every build phase

---

## 1. How to use this runbook

1. **Before Session 1:** commit the master prompt as `docs/00-master-prompt.md`, the RBI PDFs to `docs/regulations/rbi/`, a copy of the Finbyx master prompt to `docs/ecosystem/finbyx-master-prompt.md` and the Infrabyx Ecosystem Integration Specification to `docs/ecosystem/infrabyx-integration-spec.md` (canonical contract). You can also commit this runbook as `docs/01-phase-runbook.md`.
2. **One phase per session.** Start a fresh Claude Code session for each phase or sub-module, and paste only that phase's block.
3. **Each block is self-contained.** From Phase 1 onward it already includes (Phase 0 instead ends with the approval presentation of Part 13):
   - the Part 12 instruction;
   - the regulatory additions for that phase from Part 8A.16.2;
   - the standard closing that makes Claude Code list the REQ-IDs, write the specification and stop for your approval before coding.
4. **Approve, then build.** Read the specification, reply "Approved" (or give changes), and let Claude Code build, test and open the pull request.
5. **Run the review gate** (the checklist under each phase) before merging. Use prompt R6 in Section 4 to have Claude Code run it for you.
6. **Large phases:** use the sub-module split shown for the phase. Paste the full block in the first session, which writes and gets approval for the whole-phase specification; in each later sub-module session paste prompt R1, which re-reads that approved specification.
7. **Order:** 0 → 1 → 2 → 3 → 3b → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 12 → 12b → 13 → 14 → 15 → 16 → 16b → 17 → P → 18 → 18b → 19 → 20 → 21. Phase 12b (recovery support) is attachable per RE; if it is skipped, treat it as satisfied for Phase 16b, which then covers the recovery, ADR and litigation views only as contract-conformance tests, and build 12b before any RE attaches Part 7A. Phases 16b and 18 (LAS) also wait for the Finbyx phases named in their Depends on line. Do not start a phase until the phases it depends on are merged.

---

## 2. Standard closing (already included in every block)

```text
Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-<n>-<name>.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch <branch> in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

---

## 3. Phase instructions

### Phase 0 — Repository audit and architecture

- **Outcome:** Verified repo facts; architecture and ADRs (mobile/web, loan mirror, data residency, RE-scoped vault); regulatory register v1 with REQ-IDs; DLA register design; permission policy; app-store policy check
- **Depends on:** nothing (first phase)
- **Branch:** `feat/repo-baseline`

**Paste into Claude Code:**

```text
Read docs/00-master-prompt.md and docs/ecosystem/infrabyx-integration-spec.md in full, then execute Part 13 (Phase 0 only).

In addition to the Phase 0 instruction in Part 12:
- prepare docs/regulations/errata.md from Appendix F for the baseline PR after approval;
- confirm that the RBI PDFs are in docs/regulations/rbi/, the Finbyx master prompt (v1.4) is in docs/ecosystem/finbyx-master-prompt.md and the Infrabyx Ecosystem Integration Specification v1.0 is committed unchanged at docs/ecosystem/infrabyx-integration-spec.md (I committed them before this session);
- prepare docs/regulations/index.md with each file's SHA-256 hash and "updated as on" date (Part 8A.0.1) for the baseline PR after approval.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- ADR on Udofin's regulatory position: LSP under CF para 4(1)(xix), DLA per channel, not CI or SU, not FIU, not KYC decision-maker. Add the KYC "paragraph 62" CKYCR cross-reference slip to errata.md [Part 8A.1–8A.5, 8A.11]
- Record the OUT Chapter III and Chapter IV design decision and the RE-type rule-pack approach (NBFC, HFC, bank) in an ADR [Part 8A.6–8A.10, 8A.12–8A.15]

Present everything for my approval before modifying the repository.
```

**Review gate (check before merging):**

- [ ] Every Part 8A requirement is in regulatory register v1 with its REQ-ID (same IDs as Finbyx) and an [RE], [UDOFIN] or [RE→UDOFIN contract] tag; every [VERIFY] item is mapped to the phase that resolves it.
- [ ] Fund-flow diagrams show no Udofin account in any disbursement or repayment flow (CF para 10), and the loan-mirror ADR records that Fineract is not needed.
- [ ] The data-residency check covers every host and SaaS sub-processor (including Expo/EAS, push, analytics, LLM endpoints); nothing outside India holds real data (CF para 14(4)).
- [ ] The DLA register design has one line per DLA per platform per RE with the CF Annex-I fields and CF para 18(4) evidence; the permission policy and the app-store policy check (Play personal-loan rules, Apple 3.2.2(ix)) are written.
- [ ] You have answered the Appendix B decisions (including the Product 2 store-policy choice), or recorded a date for each.
- [ ] The baseline PR contains only CLAUDE.md, the ADRs, docs/, the registers and errata.md (Part 13); no application scaffolding.

### Phase 1 — Platform foundation

- **Outcome:** Monorepo with mobile, borrower web, portal, API and worker skeletons; CI with permission audit; design tokens; observability
- **Depends on:** 0
- **Branch:** `feat/platform-foundation`

**Paste into Claude Code:**

```text
Phase 1 — Platform foundation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 1; Part 8A prevails on regulatory points).

On branch `feat/platform-foundation`, initialise the approved monorepo. Set up:

- pnpm + Turborepo, TypeScript strict, ESLint/Prettier;
- `apps/mobile` (Expo, New Architecture, Expo Router, EAS profiles `development`, `preview`, `production`), `apps/borrower-web` (Next.js 16), `apps/portal` (Next.js 16 with operations, lender and admin workspaces), `apps/api` (NestJS) and `apps/worker` skeletons;
- `packages/` for contracts (OpenAPI, AsyncAPI, Zod), domain-kernel (Money, Rate, Percentage, IDs, BusinessDate), journey (shared step definitions and validation), ui-tokens, ui-web, ui-native, config, observability and testing;
- Docker Compose for local Postgres, Temporal and Gotenberg;
- GitHub Actions CI: lint, typecheck, test, build, secret scan, dependency scan, SBOM, EAS preview build, and a permission audit that fails if the built Android manifest or iOS Info.plist contains any permission not in `docs/compliance/permission-policy.md`;
- `.env.example` files; a check that no secret appears in client bundles;
- OpenTelemetry with PII redaction, and India-resident error tracking per the Phase 0 ADR; mobile crash reporting with on-device scrubbing;
- Storybook for web components and a component catalogue for native.

Implement Money, Rate and Percentage on decimal.js (precision ≥ 40) with property-based tests. Build no business features. Open a PR with the test output and the permission-audit output.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- SDK inventory of every third party that can collect personal data through the DLA, with processing location, checked in CI and feeding the privacy policy (CF paras 14(4), 15(2)); the permission allow-list check is already in the Phase 1 instruction [Part 8A.1–8A.5, 8A.11]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-1-platform-foundation.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/platform-foundation in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] CI is green on the PR, including secret scan, dependency scan, SBOM and an EAS preview build.
- [ ] The permission audit fails a test build that adds READ_CONTACTS or ACCESS_FINE_LOCATION and passes the approved manifest and Info.plist.
- [ ] Money, Rate and Percentage property-based tests pass; no float arithmetic anywhere.
- [ ] No secret or service key appears in the mobile bundle or the web client bundle; no business features were built.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 2 — Database, tenancy and security

- **Outcome:** RE-tenant and borrower model, RBAC/ABAC, enforced RLS, audit events, maker-checker, isolation tests
- **Depends on:** 1
- **Branch:** `feat/db-tenancy-security`
- **Suggested sub-modules (one session each):** migrations and enforced RLS; auth abstraction (borrower OTP, staff SSO/MFA); maker-checker, break-glass and isolation tests.

**Paste into Claude Code:**

```text
Phase 2 — Database, tenancy and security. Governing brief: docs/00-master-prompt.md (Part 12, Phase 2; Part 8A prevails on regulatory points).

On branch `feat/db-tenancy-security`, design and create the migrations for:

- lender_tenant with re_regulatory_profile (entity type, layer, asset size, s.11A status, CYB chapter, deposit-taking, card issuer), lender_legal_entity, udofin_org;
- staff_user (Udofin staff and RE users), borrower_account, device_binding, role, permission, role_permission, user_scope (RE, product, workspace);
- maker_checker_request; audit_event (hash-chained); idempotency_key; outbox_event;
- the RE-scoped vault tables and storage buckets keyed by RE, with per-RE KMS key references.

Implement:

- server-side authorisation (RBAC + ABAC);
- Postgres RLS on every RE-scoped and borrower-scoped table, enforced: the API connects as a non-owner role without BYPASSRLS; `FORCE ROW LEVEL SECURITY` on every tenant table; RE and borrower context set with `set_config(…, true)` inside each transaction;
- the auth abstraction over Supabase Auth: borrower OTP sessions with device-bound refresh, staff and RE SSO with mandatory MFA;
- the maker-checker framework;
- break-glass access for Udofin staff to RE data, logged and visible to the RE (OUT paras 24, 70);
- Supabase Data API (PostgREST, GraphQL) disabled, or application schemas unexposed with all privileges revoked from `anon` and `authenticated`; Storage RE-vault buckets private with no client policies; clients reach data only through the NestJS API.

Write isolation tests that try to read and write across REs, across borrowers and from a lender user into another RE's data, and prove they fail. Include a test proving that a query without context returns zero rows, and that a borrower JWT calling the Supabase Data API or Storage directly gets no data. Report results.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- India-only data residency for all stores; sub-processor register; data-classification register with per-RE minimal data set (CF para 14) [Part 8A.1–8A.5, 8A.11]
- RLS isolation tests per RE (OUT 26–27, 70); tamper-evident audit log (CYB 21(8)); MFA on privileged roles (CYB 115) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-2-db-tenancy-security.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/db-tenancy-security in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Cross-RE, cross-borrower and lender-to-other-RE read/write tests all fail as intended.
- [ ] A query without context returns zero rows; the API role has no BYPASSRLS and every tenant table has FORCE ROW LEVEL SECURITY.
- [ ] The audit-event hash chain verifies end to end.
- [ ] Udofin staff break-glass access to RE data is logged and visible in that RE's audit view (OUT paras 24, 70).
- [ ] The Supabase Data API and Storage are disabled or locked down for application schemas and RE-vault buckets: a borrower JWT calling them directly gets no data.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 3 — Lender onboarding, product catalogue and configuration

- **Outcome:** U1 RE onboarding and LSP agreement registry; U2 product catalogue with rule packs and guard-rails; U23 admin
- **Depends on:** 2
- **Branch:** `feat/lender-onboarding-catalogue`
- **Suggested sub-modules (one session each):** U1 RE onboarding and LSP agreement registry; U2 product catalogue and rule packs; U23 admin, feature flags and credentials.

**Paste into Claude Code:**

```text
Phase 3 — Lender onboarding, product catalogue and configuration. Governing brief: docs/00-master-prompt.md (Part 12, Phase 3; Part 8A prevails on regulatory points).

On branch `feat/lender-onboarding-catalogue`, build:

- U1: RE onboarding with the regulatory profile; the LSP agreement registry with effective dates, scope (sourcing, servicing, recovery agent yes/no, DLG yes/no), clause matrix against OUT paras 34 and 74 and CF para 6(1), the due-diligence pack (CF para 6(2)), ownership and conflict declaration (OUT paras 18(vi), 59), and the RE's grievance contacts, website link and data-storage policy (CF paras 9(4)–(5), 12(2), 14(2));
- U2: the product catalogue per RE, either received from the RE's LMS (`ProductCatalogPublished`, through the U21 connector port with a contract-faithful mock until Phase 9) or configured in the lender portal for REs without an LMS connector: amount and tenor ranges, pricing grids, charges, cooling-off days (≥ 1, CF para 11(1)), KFS template version, eligibility pre-filter rules (GoRules), required documents, mandate and payment providers;
- platform guard-rails that an RE cannot loosen: no fund flow through Udofin (CF para 10), cooling-off ≥ 1 day, KFS validity ≥ 3 working days or 1 for tenor < 7 days (RBC para 29(2)), contact windows (RBC para 100), store-policy channel filters (tenor ≤ 60 days blocked on store apps; APR > 36% blocked on iOS), microfinance flag for household income ≤ ₹3 lakh (CF para 51);
- classification of every configuration item into the five layers of Part 3.4 (standard core, tenant-safe, platform-approved, legal-review, controlled extensions), with maker-checker and effective dating;
- U23 admin for feature flags, roles and integration credentials (stored per RE, encrypted under the RE's key).

Produce `docs/products/_template.md` and the Personal Loan and Payday product specs for my approval. Tests: guard-rail rejection tests for every rule above; maker-checker tests; isolation tests for the lender workspace.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- U1 LSP agreement registry, initial DLA register lines (U18 table) with Annex-I export, recovery-agent and DLG flags; U2 beneficiary and fee rules (CF paras 6, 10, 18) [Part 8A.1–8A.5, 8A.11]
- RE regulatory profile, clause matrix, conflict declaration, compliance go-live gate and suspension switches (U1, U2, U18) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-3-lender-onboarding-catalogue.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/lender-onboarding-catalogue in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No configuration can name a Udofin account in a disbursement or repayment flow (CF para 10 guard-rail test).
- [ ] Guard-rails reject cooling-off below 1 day (CF para 11(1)) and KFS validity below 3 working days, or 1 for tenor under 7 days (RBC para 29(2)).
- [ ] Store-policy channel filters block tenor of 60 days or less on store apps and APR above 36% on iOS.
- [ ] The LSP agreement registry shows the clause matrix against OUT paras 34 and 74 and CF para 6(1) for each RE; every configuration change is effective-dated and passes maker-checker.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 3b — Communications and consent foundation

- **Outcome:** U4 consent ledger and notice versions; U16 templates, DLT/WhatsApp/email/push adapters; contact-policy engine
- **Depends on:** 2
- **Branch:** `feat/communications-consent`
- **Suggested sub-modules (one session each):** U4 consent ledger and privacy centre; U16 templates and channel adapters; contact-policy engine.

**Paste into Claude Code:**

```text
Phase 3b — Communications and consent foundation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 3b; Part 8A prevails on regulatory points).

On branch `feat/communications-consent`, build:

- U4 consent ledger: consent records with purpose, data categories, recipient RE(s), notice version and language, channel, timestamp, device, withdrawal and expiry; notice versioning with legal approval; purpose disclosure at each stage (CF para 13(1)–(4)); a privacy centre API for the app and web (view, withdraw, restrict sharing, request deletion, CF para 13(2)); retention rules engine with legal-basis exceptions (PMLA, RBI, CIC); DPDP rights workflow with a 90-day clock (DPDP Rule 14(3) from 13 May 2027) and a consent-manager integration point (Rule 4 from 13 Nov 2026) [VERIFY: Gazette text];
- U16 communications: versioned, multilingual templates with approval; SMS adapter with DLT entity, header and template IDs (sending on the RE's header where the message is the RE's); WhatsApp Business adapter restricted to categories the WhatsApp Business Messaging Policy allows (no payday-loan promotion, no debt collection); email; push via FCM/APNs with no personal data in payloads; voice/IVR adapter on 1600-series numbers for service calls [VERIFY: TRAI direction];
- contact-policy engine: effective-dated windows and frequency limits, separate service, marketing and recovery categories; recovery calls only 08:00–19:00 (RBC para 100), and only 09:00–18:00 with no persistent calling for microfinance loans, to which para 100 does not apply (RBC para 91(2)); a second effective-dated pack for the RBC Third Amendment from 1 Jan 2027 (para 100Y(4): borrower-requested times honoured; sensitive occasions avoided) [VERIFY: official text not supplied]; TCCCPR consent categories and opt-out cooling periods; DND checks.

Every later phase must send messages only through U16 and record consent only through U4. Tests: consent replay and withdrawal; template without DLT ID rejected; recovery message outside window blocked; push payload PII scan.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Consent centre with purpose-bound artefacts, revocation and erasure; storage and privacy policy publication (CF paras 13–15) [Part 8A.1–8A.5, 8A.11]
- Language template registry, quiet-hours and frequency engine, telemarketing number registry and consent checks (U16) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-3b-communications-consent.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/communications-consent in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every data collection and share in later phases can be traced to a U4 consent record with purpose, RE and notice version (CF para 13).
- [ ] Consent withdrawal stops further processing and sharing; the retention engine records the legal basis for any retained data.
- [ ] SMS cannot be sent without a DLT template ID; WhatsApp cannot carry collection or payday-loan content.
- [ ] The contact-policy engine blocks a recovery message outside 08:00–19:00 (RBC para 100) and, for microfinance loans, outside 09:00–18:00 (RBC para 91(2)); push payloads contain no personal data.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 4 — Borrower identity and onboarding (app and web)

- **Outcome:** U3 registration, OTP, device binding, app unlock, resumable journey shell on Android and web
- **Depends on:** 2, 3, 3b
- **Branch:** `feat/borrower-identity`
- **Suggested sub-modules (one session each):** Android app identity and device binding; borrower web app identity and handoff; resumable journey shell (Temporal).

**Paste into Claude Code:**

```text
Phase 4 — Borrower identity and onboarding (app and web). Governing brief: docs/00-master-prompt.md (Part 12, Phase 4; Part 8A prevails on regulatory points).

On branch `feat/borrower-identity`, build U3 on Android (Expo) and the borrower web app:

- registration and login by mobile OTP (SMS Retriever / WebOTP autofill; no SMS permission), sent through the U16 DLT-registered SMS adapter (Supabase Auth Send SMS hook or the auth abstraction), never Supabase's built-in SMS providers; rate limits and lockout;
- device binding with a hardware-backed key, Play Integrity standard request and App Attest verification on the server; device list and revocation; new-device notification;
- app unlock with biometric or app PIN after inactivity and at launch;
- the resumable journey shell: server-side Temporal workflow per application; the same step definitions on app and web; resume on another device after re-authentication;
- consent screens from U4 at the first step; purpose screens before each OS permission prompt;
- FLAG_SECURE and app-switcher blur on sensitive screens; version check against the minimum supported version with a forced-upgrade screen;
- web: WebAuthn passkey binding where available, CAPTCHA with server validation under attack, inactivity logout; QR/deep-link handoff to the app;
- accessibility (screen reader, dynamic type, contrast) and English/Hindi copy.

Target: an application starts in 3–4 interactions (mobile number, OTP, consent, product). Tests: E2E on a real low-end Android device and on Chromium mobile emulation; replayed OTP and session-fixation tests; deep-link hijack test; permission audit showing no new permission; cold-start measurement against Part 10.5.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Borrower identity across app and web; UCIC mapping per RE; registered-mobile lock; one-time camera, microphone and location in onboarding only (CF para 13(1); KYC paras 17(6), 44(2)) [Part 8A.1–8A.5, 8A.11]
- Preferred language capture; accessible journey and assisted fallback (RBC 10, 28) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-4-borrower-identity.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/borrower-identity in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] An application starts in 3–4 interactions on Android and on the web, measured in the E2E test.
- [ ] Device binding uses a hardware-backed key with server-verified Play Integrity or App Attest; a revoked device cannot obtain a session.
- [ ] Replayed OTP, session fixation and deep-link hijack tests fail as intended.
- [ ] The permission audit shows no new permission; OTP autofill uses SMS Retriever (app hash from the Play App Signing certificate in the DLT template) or WebOTP without SMS permission, and OTPs are sent only through the U16 DLT adapter.
- [ ] A journey interrupted on the app resumes on the web after re-authentication without duplicate applications or consents.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 5 — KYC and verification adapters

- **Outcome:** U5 PAN, OKYC/DigiLocker, CKYC via RE, V-CIP handoff, face match, bank verification
- **Depends on:** 4
- **Branch:** `feat/kyc-verification`
- **Suggested sub-modules (one session each):** PAN, OKYC and DigiLocker; CKYC via RE and V-CIP handoff; face match, liveness and bank verification.

**Paste into Claude Code:**

```text
Phase 5 — KYC and verification adapters. Governing brief: docs/00-master-prompt.md (Part 12, Phase 5; Part 8A prevails on regulatory points).

On branch `feat/kyc-verification`, build U5 with mock adapters first, then Surepass and other sandboxes behind `KycProvider`:

- PAN verification and PAN–Aadhaar link status;
- Aadhaar offline verification (OKYC XML or secure QR) and DigiLocker issued documents with digital-signature verification (KYC para 23 proviso (ii)–(iii)); Aadhaar number redaction (Explanation 1); no Aadhaar number or UID token stored by Udofin;
- Aadhaar OTP e-KYC only for REs whose profile shows s.11A notification, via the RE's KUA/sub-KUA, with specific OTP consent and the para 25 limits passed to the RE (term loans only, ₹60,000 a year, one-year validity unless full CDD) (KYC para 25);
- CKYC search and download with the borrower's explicit consent using the RE's credentials (KYC para 23(4));
- V-CIP handoff: launch the RE's V-CIP session (web) with a signed context; receive only the outcome and evidence reference (KYC paras 26–27);
- selfie liveness and face match with accessible alternatives (RBC para 105); scores only, no biometric storage (CF para 14(3));
- bank account verification (penny-drop/pennyless) with name match; the account must be the borrower's (CF para 10(1));
- KYC evidence packages written to the RE-scoped vault and sent to the RE as evidence; the KYC decision field is writable only by the RE (KYC para 13).

Load the KYC REQ-IDs from Part 8A.3 into the register. Tests: s.11A gate; para 25 limit propagation; no Aadhaar number in DB, logs or analytics (automated scan); RE-only KYC decision; provider time-out and retry without duplicate calls.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- KYC evidence pipeline with RE-actor decision; Aadhaar routes by s.11A status; OTP-e-KYC limits; V-CIP as RE application; CKYC Identifier first (KYC paras 13, 23, 25, 27, 44, 63) [Part 8A.1–8A.5, 8A.11]
- Accessible liveness alternatives (RBC 105); DIN/PAN capture for non-individual borrowers deferred to Phase 18 [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-5-kyc-verification.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/kyc-verification in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No Aadhaar number or UID token exists in the database, logs, analytics or fixtures (automated scan); OKYC/DigiLocker evidence is redacted (KYC para 23 Explanation 1).
- [ ] Aadhaar OTP e-KYC is available only for REs whose profile shows s.11A notification, and the KYC para 25 limits are passed to the RE.
- [ ] The KYC decision can be written only by an RE user or RE system (KYC para 13); V-CIP runs in the RE's session and Udofin receives only the outcome reference (KYC para 27).
- [ ] No biometric template is stored (CF para 14(3)); the liveness flow offers an accessible alternative (RBC para 105).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 6 — Credit data, affordability and eligibility

- **Outcome:** U6 bureau via RE, AA as RE's TSP, income and affordability, household-income test; U7 eligibility pre-filters
- **Depends on:** 3, 5
- **Branch:** `feat/credit-affordability-eligibility`
- **Suggested sub-modules (one session each):** bureau gateway and own-report path; AA as RE technology service provider; income, affordability and eligibility pre-filter.

**Paste into Claude Code:**

```text
Phase 6 — Credit data, affordability and eligibility. Governing brief: docs/00-master-prompt.md (Part 12, Phase 6; Part 8A prevails on regulatory points).

On branch `feat/credit-affordability-eligibility`, build U6 and the U7 eligibility pre-filter:

- bureau pulls through `BureauGateway` under the RE's CIC membership, with consent naming the RE and purpose; no Udofin-owned bureau account (CIR para 6) [VERIFY: CIC and Surepass contract terms];
- borrower-initiated own-report import as an alternative path, clearly labelled;
- Account Aggregator flows with the RE as FIU and Udofin as technology service provider; consent artefact per RE; data used only as the artefact allows (AA para 28);
- income, employment and bank-statement analysis adapters; economic profile capture of age, occupation and income for the RE's record (CF para 8(1));
- household income capture and the microfinance flag (≤ ₹3 lakh; CF para 51) with repayment obligations ≤ 50% of monthly household income for routing to microfinance products (CF para 55);
- the eligibility pre-filter: RE-approved GoRules versions only; first-time borrowers never excluded for lack of credit history (CIR para 38(5)); DLG cover never an input (CF para 20(2)); every pre-filter outcome stores inputs, rule version and RE attribution; the credit decision is always the RE's.

Tests: consent required before any pull; per-RE data isolation of bureau data; rule-version replay; new-to-credit test; microfinance-flag golden cases.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Per-RE bureau adapter; household-income questionnaire and microfinance flag; indicative 50% obligation ratio (CIR paras 6, 20; CF paras 51–58) [Part 8A.1–8A.5, 8A.11]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-6-credit-affordability-eligibility.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/credit-affordability-eligibility in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No bureau pull runs without consent naming the RE and purpose, and every pull uses the RE's CIC membership (CIR para 6).
- [ ] AA consent artefacts name the RE as FIU, and data is used only as the artefact allows (AA para 28).
- [ ] First-time borrowers are never excluded for lack of credit history (CIR para 38(5)); DLG cover is never a pre-filter input (CF para 20(2)).
- [ ] Household income at or below ₹3 lakh flags the application as microfinance (CF para 51), and the golden cases pass.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 7 — Lender routing, offers, KFS and cooling-off

- **Outcome:** U7 routing; U8 multi-lender offer view, KFS display and acknowledgement, cooling-off
- **Depends on:** 6
- **Branch:** `feat/routing-offers-kfs`
- **Suggested sub-modules (one session each):** routing and matching mechanism; multi-lender offer view; KFS display, acknowledgement and cooling-off.

**Paste into Claude Code:**

```text
Phase 7 — Lender routing, offers, KFS and cooling-off. Governing brief: docs/00-master-prompt.md (Part 12, Phase 7; Part 8A prevails on regulatory points).

On branch `feat/routing-offers-kfs`, build U7 routing and U8:

- routing to every RE whose pre-filter matches, using the documented matching mechanism, versioned and applied consistently to similarly placed borrowers (CF para 7(2));
- `EligibilityCheck` and `ApplicationSubmitted` to each RE (Finbyx Part 5.2), with only the data the borrower consented to share with that RE, through the U21 `LenderConnector` port against a contract-faithful mock until the Finbyx and generic connectors are built in Phase 9; handle `AdditionalInfoRequested`, `ApplicationStatusChanged`, `DecisionMade`, `KFSIssued` and `SanctionLetterIssued`, and send `BorrowerAccepted` within KFS validity;
- the multi-lender offer view: lender name, amount, tenor, APR, monthly repayment obligation, penal charges and KFS link per offer; unmatched lenders named; ranking only by a publicly pre-disclosed metric; no dark patterns (CF para 7(1)–(4); CCPA Dark Patterns Guidelines, 2023);
- channel filters from Phase 3 (store-policy limits) applied server-side and recorded;
- KFS display exactly as issued by the RE (`KFSIssued`): proposal number, validity period, APR computation sheet and repayment schedule (RBC para 29(1)–(3)); borrower acknowledgement captured; KFS in the borrower's language;
- the cooling-off period from the RE product and the exit request (`CoolingOffExitRequested`) with the RE-computed exit amount (CF para 11);
- no automatic credit-limit increase without an explicit borrower request (CF para 8(2)).

Tests: APR golden test 17.07% displayed (RBC para 29(3)); offer-neutrality test (same inputs, same order, no lender emphasis); unmatched-lender disclosure; KFS expiry blocks acceptance after the validity period; store-filter tests per channel; E2E from application to accepted offer on Android and web.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Multi-lender offer view with unmatched lenders, published ranking metric, dark-pattern review; KFS display; cooling-off display and exit (CF paras 7, 9, 11) [Part 8A.1–8A.5, 8A.11]
- KFS validity clock, APR recomputation golden test, acknowledgement capture, Annex I Part 2 validation (RBC 29) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-7-routing-offers-kfs.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/routing-offers-kfs in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The offer view shows lender name, amount, tenor, APR, monthly repayment obligation, penal charges and KFS link per offer, and names unmatched lenders (CF para 7(1), (3)).
- [ ] The offer-neutrality test passes: same inputs give the same order by the pre-disclosed metric, with no lender emphasis or pre-selection (CF para 7(4)).
- [ ] The KFS APR golden test displays 17.07% (RBC para 29(3)); acceptance after the KFS validity period is blocked (RBC para 29(2)).
- [ ] The cooling-off period and exit terms are shown before acceptance (CF para 11), and the exit request with the RE-computed exit amount works against a mocked disbursement event; the live clock start is tested in Phase 9.
- [ ] Lender events (EligibilityCheck, ApplicationSubmitted, DecisionMade, KFSIssued, SanctionLetterIssued, BorrowerAccepted) run through the U21 connector port against a contract-faithful mock, with the Part 5.2 names unchanged.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 8 — Documents, eSign, eStamp and DMS

- **Outcome:** U9 templates from RE, signing evidence, stamping, DMS and auto-flow of signed documents
- **Depends on:** 7
- **Branch:** `feat/documents-esign-dms`
- **Suggested sub-modules (one session each):** templates and document generation; eSign and eStamp adapters; DMS and automatic document flow (CF para 9(3)).

**Paste into Claude Code:**

```text
Phase 8 — Documents, eSign, eStamp and DMS. Governing brief: docs/00-master-prompt.md (Part 12, Phase 8; Part 8A prevails on regulatory points).

On branch `feat/documents-esign-dms`, build U9:

- document generation from RE-owned templates on the RE's letterhead (KFS, sanction letter, agreement, summary of product, privacy policies);
- eSign adapters storing provider transaction ID, certificate, signer details and document hash (`ESignCompleted`), never a bare flag; eStamp adapters with state, duty and certificate (`EStampCompleted`);
- the physical-execution path for instruments excluded by the IT Act First Schedule;
- the DMS with versions, hashes, retention per RE policy, access logs and signed short-lived URLs; the borrower sees every signed document in the app and web;
- automatic flow of the digitally signed KFS, product summary, sanction letter, terms and conditions and privacy policies to the borrower's verified email or SMS on execution (CF para 9(3)).

Tests: tampered document hash detected; signature evidence linked to the accepted KFS version; no document reachable without authorisation (IDOR tests on URLs); auto-flow sent once and only to the verified contact.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- RE signed-document pack delivery without re-rendering; microfinance loan card (CF para 9(3); RBC para 78) [Part 8A.1–8A.5, 8A.11]
- Agreement pack completeness and summary-box checks (RBC 14, 29(6)) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-8-documents-esign-dms.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/documents-esign-dms in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every signed document has provider transaction ID, certificate and hash linked to the accepted KFS version; no bare signed flag exists.
- [ ] Signed KFS, sanction letter, terms and privacy policies flow automatically to the verified email or SMS on execution (CF para 9(3)).
- [ ] Document URLs are short-lived and IDOR tests on the DMS fail as intended.
- [ ] Instruments excluded by the IT Act First Schedule follow the physical-execution path.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 9 — Lender connectors and disbursement orchestration

- **Outcome:** U21 Finbyx connector and generic LMS connector; U10 disbursement status
- **Depends on:** 3, 8
- **Branch:** `feat/lender-connectors-disbursement`
- **Suggested sub-modules (one session each):** Finbyx connector; generic LMS connector framework and certification suite; disbursement status orchestration and lender queues.

**Paste into Claude Code:**

```text
Phase 9 — Lender connectors and disbursement orchestration. Governing brief: docs/00-master-prompt.md (Part 12, Phase 9; Part 8A prevails on regulatory points).

On branch `feat/lender-connectors-disbursement`, build U21 and U10:

- the Finbyx connector implementing the Ecosystem Integration Specification exactly (same event names as Finbyx Part 5.2), with mTLS, JWS-signed messages, idempotency and replay protection; Pact contract tests against Finbyx;
- the generic LMS connector framework (REST/webhook and SFTP file adapters), a mapping layer per RE, and a connector certification suite;
- disbursement orchestration as status only: Udofin sends the accepted, signed package; the RE disburses directly to the borrower's verified account; Udofin moves the application to disbursed only on `LoanDisbursed` with UTR (CF para 10(1)); `DisbursementFailed` handling with borrower messaging;
- start of the cooling-off clock on the trigger set in the RE's product (default the RE's `LoanDisbursed` event; CF para 11 leaves it to the RE's credit policy, 8A.16.3);
- lender portal queues for REs without an LMS connector: decision capture by RE users only, with maker-checker.

Tests: no configuration can name a Udofin account as payee (guard-rail test); duplicate event idempotency; connector outage queues and recovers; reconciliation report between Udofin application states and RE events.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Disbursement status orchestration with verified-beneficiary checks; connector validator against Udofin accounts (CF para 10(1)–(3)) [Part 8A.1–8A.5, 8A.11]
- Disbursal notice carries the RE's recovery-grievance mechanism for microfinance loans (RBC 92) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-9-lender-connectors-disbursement.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/lender-connectors-disbursement in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Pact contract tests pass against Finbyx using the Finbyx Part 5.2 event names unchanged.
- [ ] An application moves to disbursed only on the RE's LoanDisbursed event with UTR; sanction alone never changes it.
- [ ] Duplicate and replayed connector events are idempotent; a connector outage queues and recovers without loss.
- [ ] The daily reconciliation between Udofin application states and RE events shows no unexplained breaks.
- [ ] The cooling-off clock starts on the trigger configured in each RE's product (default LoanDisbursed), and the Phase 3 and Phase 7 connector mocks are replaced by the certified connectors with the same tests passing.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 10 — Repayments, mandates and reconciliation

- **Outcome:** U11 eNACH/UPI AutoPay on RE accounts, payment links on RE merchant accounts, status reconciliation
- **Depends on:** 9
- **Branch:** `feat/repayments-mandates-recon`
- **Suggested sub-modules (one session each):** eNACH and UPI AutoPay mandates; payment links on RE merchant accounts; status reconciliation.

**Paste into Claude Code:**

```text
Phase 10 — Repayments, mandates and reconciliation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 10; Part 8A prevails on regulatory points).

On branch `feat/repayments-mandates-recon`, build U11:

- eNACH and UPI AutoPay mandate registration on the RE's corporate utility code or merchant account, with limits and UMRN sent to the LMS (`MandateRegistered`); no fresh PDCs or EMI cheques where NACH is available (MISC para 23);
- payment links and UPI intent on the RE's merchant account only; Udofin never holds a merchant account, escrow or virtual account for repayments (CF para 10(2)–(3));
- payment status from the gateway reconciled against the RE's `PaymentReceived` and `PaymentBounced` events; a gateway success alone never marks a due as paid;
- receipts issued by the RE shown in the app;
- co-lending: repayment to the co-lending escrow controlled only by the co-lenders (CF para 10(1) Note);
- Stripe and PayPal: no adapter for domestic repayments; record the ADR.

Tests: payee-account guard-rail; duplicate payment-link prevention; three-way status reconciliation (gateway, RE event, mirror) with aged exceptions; mandate amount cannot exceed the RE-approved limit.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Collections on RE merchant accounts only; 24-hour status reconciliation; no borrower fees (CF para 10(2)–(4); DPS para 57) [Part 8A.1–8A.5, 8A.11]
- Electronic mandates only; escrow routing for CLA loans; reconciliation ageing (MISC 23; TDCR 117; OUT 39) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-10-repayments-mandates-recon.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/repayments-mandates-recon in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Mandates and payment links settle only to the RE's account or co-lending escrow; no Udofin merchant, escrow or virtual account exists (CF para 10(2)–(3)).
- [ ] A gateway success alone never marks a due as paid; three-way status reconciliation (gateway, RE event, mirror) runs daily with aged exceptions.
- [ ] Duplicate payment links and duplicate mandates are prevented; no PDCs are collected where NACH is available (MISC para 23).
- [ ] No Stripe or PayPal adapter is used for domestic repayments, and the ADR records why.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 11 — Loan mirror and borrower servicing

- **Outcome:** U12 loan mirror, statements, service requests; U25 borrower dashboard
- **Depends on:** 9, 10
- **Branch:** `feat/loan-mirror-servicing`
- **Suggested sub-modules (one session each):** loan mirror and reconciliation; service requests; U25 borrower dashboard.

**Paste into Claude Code:**

```text
Phase 11 — Loan mirror and borrower servicing. Governing brief: docs/00-master-prompt.md (Part 12, Phase 11; Part 8A prevails on regulatory points).

On branch `feat/loan-mirror-servicing`, build U12 and U25:

- the loan mirror fed by `ScheduleIssued`, `ScheduleChanged`, `PaymentReceived`, `PaymentBounced`, `DPDChanged`, `AssetClassificationChanged`, `LoanClosed` and `NOCIssued`; every figure labelled with the RE as source and the as-of time; daily reconciliation with the RE's `DailyReconciliationFile`; no balance computed by Udofin;
- revised schedules shown on each part-disbursement as sent by the RE (MSD para 7(3));
- service requests (statement, foreclosure quote, NOC, profile change) routed to the RE with SLA tracking;
- U25 borrower dashboard: all loans, charges, dues, documents, consents and data-sharing history, complaints; optional personal expense tracker using only data the borrower enters.

Tests: mirror never shows a value without source and as-of; reconciliation break raises an exception; service request reaches the right RE only; dashboard isolation between borrowers.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Loan mirror with cooling-off exit, limit-increase request event and OTP-e-KYC drawdown block (CF paras 8(2), 11; KYC para 25(7)) [Part 8A.1–8A.5, 8A.11]
- Prospective-change check, 21-day transfer request, SMA/NPA display, settlement relay, end-use certificates, interest-charging shadow checks (RBC 15, 19; IRACP 15–19; RSA 87–95; WD 19(2); MSD 7) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-11-loan-mirror-servicing.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/loan-mirror-servicing in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every figure in the loan mirror shows the RE as source and the as-of time; Udofin computes no balance.
- [ ] The mirror reconciles to the RE's DailyReconciliationFile and breaks raise exceptions.
- [ ] Revised schedules on part-disbursement are shown as sent by the RE (MSD para 7(3)).
- [ ] Service requests reach only the responsible RE, and the borrower dashboard passes borrower-isolation tests.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 12 — Collections and recovery support

- **Outcome:** U13 reminders and, only where appointed, recovery-agent workflows
- **Depends on:** 3b, 11
- **Branch:** `feat/collections-support`
- **Suggested sub-modules (one session each):** reminders for all REs; recovery-agent workflows (appointed REs only).

**Paste into Claude Code:**

```text
Phase 12 — Collections and recovery support. Governing brief: docs/00-master-prompt.md (Part 12, Phase 12; Part 8A prevails on regulatory points).

On branch `feat/collections-support`, build U13 in two separate capabilities:

1. Reminders for all REs (servicing under the LSP agreement): due-date reminders and payment links through U16 within the contact policy; no WhatsApp for debt collection.
2. Recovery-agent workflows only for REs that appointed Udofin by an explicit recovery-agent contract recorded in U1 (never inferred from DLG): `CollectionAllocated` and `CollectionDeallocated`; recovery-agent particulars sent to the borrower by email or SMS before first contact (CF para 9(6); RBC para 95); notice and authorisation letter (RBC paras 95–96); agent register with police verification and training (RBC paras 94, 98–99); calling window 08:00–19:00 and no harassment (RBC para 100), or 09:00–18:00, no persistent calling and recovery at the designated place unless the borrower fails to appear twice in succession for microfinance loans (RBC paras 90–91; para 100 excludes them); calls from the RE's 1600-series numbers [VERIFY]; `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued`; cash recoveries reflected in the borrower's account the same day and no Udofin fee deducted from proceeds (CF para 10(5)).

Build the RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026; paras 100A–100AB in force 1 Jan 2027) as a second effective-dated rule pack, as summarised in Part 7A.0.1 [VERIFY: official text not supplied; confirm paragraph numbers before release]. Phase 12b extends this phase with Part 7A. Tests: recovery workflow unavailable without an active contract; contact outside window blocked; particulars notice precedes first contact; DLG arrangement alone grants no collection rights.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Recovery-agent gating, notice-before-contact, contact windows, cash same-day posting (CF paras 6(5), 9(6), 10(5); RBC paras 90–100) [Part 8A.1–8A.5, 8A.11]
- Recovery-agent register, verification gates, notices, contact-window enforcement, call recording [recommendation], same-day cash reflection (RBC 90–100; CF 9(6), 10(5)) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-12-collections-support.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/collections-support in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Recovery-agent workflows are unavailable for an RE without an active recovery-agent contract in U1; a DLG arrangement alone grants no collection rights.
- [ ] Recovery-agent particulars reach the borrower by email or SMS before the first contact (CF para 9(6); RBC para 95).
- [ ] Contact outside 08:00–19:00 (RBC para 100), or outside 09:00–18:00 for microfinance loans (RBC para 91(2)), or above frequency limits is blocked by the engine; the microfinance visit rule applies (RBC para 90); no collection message goes on WhatsApp.
- [ ] Cash recoveries are reflected in the borrower's account the same day and no Udofin fee is deducted from proceeds (CF para 10(5)).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 12b — Recovery support, notices and ADR access

- **Outcome:** Part 7A (7A.0, UR1–UR6), attachable per RE: overdue, settlement and payment centre; ADR access through Equator without a separate app; RE notices and case visibility; recovery-agent operations only where appointed; data feeds to the RE's recovery suite; conduct and evidence controls
- **Depends on:** 3b, 9, 11, 12 (UR2 also 14; UR6 export to LawDocsComply or a GRC tool also 16, evidence packs before then; UR4 field-app features also 20)
- **Branch:** `feat/recovery-support`
- **Suggested sub-modules (one session each):** 7A.0 attach and detach, rule packs and retention; UR1 overdue, settlement and payment centre; UR2 ADR access (after Phase 14); UR3 notices and case visibility; UR4 recovery-agent operations (appointed REs only); UR5 data feeds and UR6 conduct controls (GRC connector export after Phase 16; evidence packs before then).

**Paste into Claude Code:**

```text
Phase 12b — Recovery support, notices and ADR access. Governing brief: docs/00-master-prompt.md (Part 12, Phase 12b; Part 8A prevails on regulatory points).

On branch `feat/recovery-support`, build Part 7A (7A.0, UR1–UR6) as the attachable module pack `modules/ur-recovery-support/` with its `module.yaml` manifest:

- 7A.0: entitlement check (the RE's licence SKU, the LSP agreement scope and the flag `mod.udofin-recovery.[capability]`, all server-side); lifecycle from `AVAILABLE` to `DETACHED` with `ModuleAttached` and `ModuleDetached`; read-only detach with an RE export pack; the retention schedule and legal holds; rule pack A (RBC paras 90–100, to 31 Dec 2026) and rule pack B (RBC Third Amendment Directions, 2026, RBI/2026-27/230, paras 100A–100AB, from 1 Jan 2027) as effective-dated versions, plus state overlays [VERIFY: official text not supplied; confirm paragraph numbers before release];
- UR1: overdue view, RE payment options, PTP, hardship requests, settlement requests (`SettlementRequested`), RE offers shown verbatim with the characterisation block (RSA paras 89–90, 95, 97–98, 100; CIR para 12(4)) and acceptance evidence; no Udofin role can approve, price or promise a settlement (RSA para 16(5); OUT para 15);
- UR2 (after Phase 14): ADR case view from the ADR events, signed link into Equator's web flow with no separate app, a basis check on every referral, and no referral scope for Udofin credentials (*CORE v ECI-SPIC-SMO-MCML (JV)*, SC, 8 Nov 2024; *L&T Finance v Jai Paras Material Store*, Cal HC, 14 May 2026);
- UR3: RE notice inbox with hash checks, Udofin-channel delivery evidence (`NoticeServiceUpdated`), the RE's visibility policy (off by default), no "served" state and no WhatsApp;
- UR4: recovery-agent operations only for REs with an explicit recovery-agent contract: contract, agent-eligibility, notice-before-contact (CF para 9(6)) and `canContact` gates; call recording; same-day cash posting (CF para 10(5)); agency list feed (RBC para 97);
- UR5: data feeds to the RE's recovery suite with daily reconciliation;
- UR6: controls UR6-C01 to C16 with evidence to LawDocsComply or the RE's GRC tool.

Present the specification of each UR module for my approval before code. Tests: every test listed under UR1–UR6, plus: Udofin client credentials cannot create an ADR referral or a settlement approval; attaching UR4 for an RE without a recovery-agent contract fails; detach makes every UR screen read-only and produces a verified export; no recovery template can select WhatsApp.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Rule pack B from 1 Jan 2027 (RBC Third Amendment paras 100A–100AB) [VERIFY: official text]; settlement relay with the RE's characterisation block and no Udofin approval (RSA paras 16(5), 87–100; CIR para 12(4); OUT para 15); ADR basis check and no referral scope (A&C Act s.7; *CORE*, SC, 8 Nov 2024); notice delivery evidence without a served state; same-day cash posting (CF para 10(5)) [Part 7A, 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-12b-recovery-support.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/recovery-support in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Part 7A capabilities attach only when the RE's licence SKU, the LSP agreement scope and the feature flag agree; detach makes every UR screen read-only, stops all contact at once and produces a verified export pack, and no record is deleted before its retention date or while on legal hold (OUT paras 42–43, 87–88).
- [ ] No Udofin role or credential can approve, price or promise a settlement or create an ADR referral; RE offers are shown verbatim with the characterisation block, and a referral without a recorded basis shows no call to action (RSA paras 16(5), 89–90, 95, 100; OUT para 15; CORE v ECI-SPIC-SMO-MCML (JV), SC, 8 Nov 2024; L&T Finance v Jai Paras Material Store, Cal HC, 14 May 2026).
- [ ] UR4 rejects allocations without a recovery-agent contract or an eligible agent, blocks every attempt before the agent-particulars notice is delivered (CF para 9(6)) and outside the window of the applicable pack (RBC paras 91(2), 100; RBC Third Amendment para 100Y(4) from 1 Jan 2027) [VERIFY: Third Amendment official text].
- [ ] Udofin never issues a notice in its own name or marks one served, no recovery template can select WhatsApp, and a cash receipt not posted by the RE the same day escalates (CF para 10(5); WhatsApp Business Messaging Policy).
- [ ] Every UR6 control (C01–C16) has an owner and an automated test; its evidence is produced as masked, hash-chained evidence packs with aggregate counts and masked sample IDs only, and reaches LawDocsComply or the RE's GRC tool once the Phase 16 connector is merged (CF para 14(4); OUT para 34(ii)).
- [ ] Udofin consumes but never produces CollateralPledgeRequested, settlement acceptance is sent as SettlementOfferAccepted, and UR1 to UR4 consume only the events the Integration Specification routes to Udofin (no CoLendingSplitConfirmed, ClassificationSynced or OrderRecorded); RecoveryAgentNoticeSent or Udofin's own delivery evidence satisfies the notice-before-contact gate (CF para 9(6)).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 13 — DLG management and lender disclosures

- **Outcome:** U14 DLG arrangements, caps, invocations, monthly website disclosure
- **Depends on:** 9, 11
- **Branch:** `feat/dlg-management`
- **Suggested sub-modules (one session each):** DLG arrangements, instruments and cap engine; invocations, declaration and monthly disclosure.

**Paste into Claude Code:**

```text
Phase 13 — DLG management and lender disclosures. Governing brief: docs/00-master-prompt.md (Part 12, Phase 13; Part 8A prevails on regulatory points).

On branch `feat/dlg-management`, build U14 (Udofin as DLG provider):

- eligibility check: Udofin incorporated under the Companies Act, 2013 (CF para 19); DLG policy inputs for the RE (CF para 20(1));
- arrangements per RE with the explicit contract terms (extent, form, invocation timeline, disclosure; CF para 22), form as cash with the RE, FD with lien or bank guarantee (CF para 23), and the fixed DLG set (CF para 24(2));
- cap engine: total cover ≤ 5% of the amount disbursed out of the DLG set, activated proportionately on disbursement (CF para 24(3), Illustration 1), with the CF para 24(3) illustrations as golden tests;
- invocation register: invocation within 120 days overdue (CF para 27(1)); no set-off against borrower liability (25(2)); recovery sharing per contract (25(3)); no reinstatement (25(4)); DLG term ≥ longest loan tenor (27(2)); no DLG on loans under trust-fund guarantee schemes (CF para 21(1)) or for P2P;
- the statutory-auditor-certified declaration (aggregate DLG outstanding, number of lenders, portfolios, past default rates) at each entry or renewal (CF para 20(3));
- monthly website disclosure of the number of portfolios and amount of each on which DLG is offered, published within 7 working days of month-end (CF para 28);
- `DLGArrangementRegistered`, `DLGInvocationRaised`, `DLGInvocationSettled`, `DLGPortfolioCoverage` with each RE; `DLGDisclosurePublished` to each RE and LawDocsComply (CF para 28); `DLGRecoveryShared` consumed into the recovery-share ledger (CF para 25(3)); data for the RE's ECL (IRACP paras 36A–36C) and capital treatment (CF para 26).

DLG never feeds credit pre-filters (CF para 20(2)) and never creates collection rights. Tests: all CF para 24(3) cases; 121-day invocation rejected; reinstatement attempt rejected; disclosure job meets the 7-working-day deadline.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- DLG engine on the provider side, auditor declaration data, monthly website disclosure (CF paras 19–29) [Part 8A.1–8A.5, 8A.11]
- DLG event feed for ECL; CLA exclusion until legal sign-off (IRACP 36A–36C; TDCR 111, 123) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-13-dlg-management.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/dlg-management in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] All CF para 24(3) illustrations pass, with cover capped at 5% of the amount disbursed out of the fixed DLG set.
- [ ] Invocation after 120 days overdue is rejected (CF para 27(1)) and any reinstatement attempt is rejected (CF para 25(4)).
- [ ] Each arrangement holds the statutory-auditor-certified declaration (CF para 20(3)) and a permitted form (CF para 23); loans under trust-fund guarantee schemes are excluded (CF para 21(1)).
- [ ] The monthly website disclosure is published within 7 working days of month-end (CF para 28).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 14 — Grievance, AI support and Equator

- **Outcome:** U15 complaints, nodal GRO, RE routing, AI support, Equator access for RE-referred cases
- **Depends on:** 3b, 11
- **Branch:** `feat/grievance-ai-equator`
- **Suggested sub-modules (one session each):** complaint management and RE routing; AI support assistant; Equator access for RE-referred cases (signed link into Equator's web flow, no separate app; Udofin never refers).

**Paste into Claude Code:**

```text
Phase 14 — Grievance, AI support and Equator. Governing brief: docs/00-master-prompt.md (Part 12, Phase 14; Part 8A prevails on regulatory points).

On branch `feat/grievance-ai-equator`, build U15:

- complaint lodging in the app and on the web (CF para 12(3)); unique reference; acknowledgement; Udofin nodal GRO details displayed on the DLA and website and RE GRO details in the KFS (CF para 12(1)–(2));
- routing every complaint to the responsible RE (`GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated`); grievance redressal remains with the RE; Udofin never closes an RE complaint (CF para 12(3); OUT para 56);
- the 30-day clock and escalation information to RBI CMS (https://cms.rbi.org.in) and the CRPC address when the RE rejects, partly rejects or does not reply within 30 days (CF para 12(4)); Internal Ombudsman and RB-IOS 2026 steps [VERIFY: texts not supplied];
- AI support assistant answering only from approved sources (RE product documents, KFS, FAQs, case status), with citations, hand-off to a human and no invented rights or outcomes; it never rejects or closes a complaint; build now the minimum U20 controls it needs (model-inventory entry, approved-source retrieval, prompt redaction, India-region or RE-approved endpoint per CF para 14(4)), which Phase 20 extends;
- Equator access only for cases the RE has referred (Udofin never refers), after the RE's process or under a pre-named institution clause or written post-dispute consent; a signed link into Equator's web flow from the app, no separate app; outcome status flows back (full specification in Part 7A UR2, built in Phase 12b);
- feedback (CSAT/NPS) through U16.

Tests: complaint cannot be closed by any Udofin role; 30-day escalation message triggers; AI refuses out-of-scope questions; Udofin credentials cannot create an ADR referral, and Equator access appears only for RE-referred cases with a recorded basis.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- LSP nodal officer, intake, immediate RE routing, CMS and CRPC escalation; CIR complaint fields (CF para 12; CIR para 35(8)) [Part 8A.1–8A.5, 8A.11]
- RE GRO routing, RB-IOS day-31 prompt, FS-format complaint MIS (OUT 56–57; FS 21(10)) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-14-grievance-ai-equator.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/grievance-ai-equator in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No Udofin role or AI agent can close or reject an RE complaint (CF para 12(3); OUT para 56).
- [ ] Nodal GRO details appear on the DLA and website, and complaints can be lodged in the app and on the web (CF para 12(1)–(3)).
- [ ] The CMS escalation message triggers when the RE rejects or does not reply within 30 days (CF para 12(4)); Internal Ombudsman and RB-IOS 2026 steps are marked [VERIFY] until the texts are supplied.
- [ ] The AI assistant answers only from approved sources with citations and refuses out-of-scope questions; Udofin credentials cannot create an ADR referral (scope adr.referral:create is denied) and Equator access appears only for RE-referred cases with a recorded basis (pre-named institution or written post-dispute consent).
- [ ] The AI assistant has a model-inventory entry, uses only approved sources, redacts prompts and runs on an India-region or RE-approved endpoint (CF para 14(4)).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 15 — Udofin finance, accounting and reporting

- **Outcome:** U17 Udofin ledger, fee invoicing, GST, DLG accounting, Tally/SAP; U19 reports and lender dashboards
- **Depends on:** 9, 13
- **Branch:** `feat/udofin-finance`
- **Suggested sub-modules (one session each):** Udofin ledger, fees and GST; DLG accounting; Tally/SAP exports and U19 reports.

**Paste into Claude Code:**

```text
Phase 15 — Udofin finance, accounting and reporting. Governing brief: docs/00-master-prompt.md (Part 12, Phase 15; Part 8A prevails on regulatory points).

On branch `feat/udofin-finance`, build U17 and U19:

- Udofin's own double-entry ledger (append-only, balanced, reversal-only corrections, period locks) for LSP fee income, GST on fees invoiced to REs, DLG deposits, FDs and bank guarantees, invocations and recoveries shared, collection-agent fees (where appointed) and vendor costs;
- fee computation from RE agreements; invoices to REs only; a test proving no fee line can be charged to a borrower (CF para 10(4));
- Tally Prime (JSON/XML connector), SAP and CSV exports with reconciliation;
- U19 reports: per-RE funnel, conversion, TAT, complaints, DLG positions, sourcing data for the RE's returns (SR) with lineage, unit economics per application; lender dashboards with row-level security.

Our CA reviewer approves the golden accounting cases. Tests: trial balance balances under randomised postings; RE dashboard isolation; export reconciles to the ledger.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- LSP fee invoicing to REs; DLG instrument and cash-in-transit accounting (CF paras 10(4)–(5), 23) [Part 8A.1–8A.5, 8A.11]
- U19 FPC conduct pack, SLA and half-yearly outsourcing reports, six-month new-product monitoring pack, recovery-agency list feed, record-level lineage and control totals; U17 fee-invoice reconciliation with each RE (RBC 8, 97; OUT 35–36, 39; CMP 15(2); SR 6, 14–15, 17) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-15-udofin-finance.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/udofin-finance in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The Udofin trial balance balances after a randomised posting test; corrections happen only by reversal.
- [ ] No fee line can be charged to a borrower; LSP fees are invoiced only to REs (CF para 10(4)).
- [ ] Tally Prime and SAP exports reconcile to the ledger, and your CA reviewer has signed off the golden cases.
- [ ] Lender dashboards pass RE-isolation tests.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 16 — Compliance, audit and security operations

- **Outcome:** U18 register, evidence, DLA register, RE audit access, LawDocsComply bridge; U24 SecOps and fraud signals
- **Depends on:** 2, 14
- **Branch:** `feat/compliance-secops`
- **Suggested sub-modules (one session each):** U18 register, evidence and DLA register; RE, auditor and RBI access; U24 SIEM, incidents and fraud signals.

**Paste into Claude Code:**

```text
Phase 16 — Compliance, audit and security operations. Governing brief: docs/00-master-prompt.md (Part 12, Phase 16; Part 8A prevails on regulatory points).

On branch `feat/compliance-secops`, build U18 and U24:

- the regulatory register with REQ-IDs, owners, controls, control tests and evidence; dated change log;
- the DLA register and CIMS data pack per RE (CF para 18, Annex-I) with change notices and CCO-certification evidence for CF para 18(4)(i)–(iv);
- RE, auditor and RBI read-only, time-boxed access to that RE's data, logs and evidence (OUT paras 34, 74(ii), 81; CYB para 62(2));
- vendor assurance pack generation (10.8);
- the LawDocsComply bridge (register, evidence and DLA feed);
- U24: SIEM feed per RE, anomaly rules, incident runbook with RE notification target ≤ 2 hours and CERT-In 6-hour reporting, fraud and device-risk signals to REs (FRM paras 13–23 as RE inputs), app-integrity verdict monitoring.

Tests: an incident drill measuring Udofin detection → RE notification time; auditor role cannot see another RE; every REQ-ID has an owner and a control test.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- CIMS certification evidence pack; RE due-diligence pack; channel risk pack; DPS voluntary baseline controls (CF paras 6(2), 18(3)–(4); KYC para 68; DPS) [Part 8A.1–8A.5, 8A.11]
- Incident notification workflow, VAPT cadence, vendor assurance pack, audit access roles, fraud signals and evidence packs (OUT 61; CYB 121–126; FRM 15–23) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-16-compliance-secops.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/compliance-secops in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every REQ-ID has an owner, a control and a control test in the register.
- [ ] The CIMS data pack per RE reproduces the CF Annex-I fields for every DLA, with CF para 18(4) certification evidence.
- [ ] The incident drill shows RE notification within 2 hours of Udofin detection, supporting the RE's 6-hour DAKSH filing (OUT para 61; CYB paras 28, 141), and a CERT-In report within 6 hours.
- [ ] Auditor and RBI roles are read-only, time-boxed and cannot see another RE's data.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 16b — Ecosystem integration v2

- **Outcome:** Ecosystem Integration Specification conformance for every product lifecycle including LAS; new event domains; Equator and other ODR providers; LawDocsComply and third-party GRC connectors with OSCAL export; third-party LOS/LMS certification; module manifests
- **Depends on:** 9, 12b, 14, 16; Finbyx Phase 16b sandbox (Integration Spec Part 15)
- **Branch:** `feat/ecosystem-integration-v2`
- **Suggested sub-modules (one session each):** contract and registry conformance; security profile; product lifecycles including LAS; ODR and GRC connectors; third-party LOS/LMS certification.

**Paste into Claude Code:**

```text
Phase 16b — Ecosystem integration v2. Governing brief: docs/00-master-prompt.md (Part 12, Phase 16b; Part 8A prevails on regulatory points).

On branch `feat/ecosystem-integration-v2`, bring every Udofin connector to the Infrabyx Ecosystem Integration Specification v1.0 (`docs/ecosystem/infrabyx-integration-spec.md`):

- contracts: CloudEvents 1.0 envelope with the specification's type and source conventions and the extensions `tenantid`, `reid`, `productfamily`, `correlationid`, `causationid`, `consentref` or `legalbasis`, `dataclass`, `schemaver`, `seq` and `traceparent` (Integration Spec 3.2); AsyncAPI 3.0 and OpenAPI 3.1; JSON Schema 2020-12 registry with backward-compatibility checks and 90-day dual publication of any breaking `vN`; Pact tests in both pipelines;
- security: mTLS everywhere; RFC 9421 HTTP Message Signatures, with a detached JWS for documents and regulated messages; OAuth 2.1 client credentials bound by mTLS; FAPI 2.0 where an API acts for the borrower; Standard Webhooks for external webhooks; `Idempotency-Key` on every POST; outbox, inbox and dead-letter queue;
- every product lifecycle (Products 1–15, Part 6.4), including the LAS collateral events (Part 6.5), the co-lending and transfer events, the recovery, ADR and litigation views (Part 7A) and the six events adopted in v1.1 (Part 5.2);
- Equator and other ODR providers through one `OdrProvider` contract, with CSV or SFTP where a provider has no API;
- LawDocsComply and third-party GRC tools (MetricStream, IBM OpenPages, ServiceNow IRM, Archer) through the generic GRC contract with OSCAL export (U18);
- third-party LOS/LMS connectors certified per RE with the same suite; notice-dispatch adapters for RE-issued notices; court-data views only as RE-permitted projections;
- module manifests for every attachable module, and a connector certification suite that emits `ConnectorCertified` and stores the report as evidence.

Never rename a canonical event; raise any gap as a versioned contract change in every affected repository. Tests: contract conformance for every event and API; signature, replay and idempotency rejection; payloads without a consent reference or statutory-basis flag rejected (CF para 13(4)); registry rejects a breaking change without a new version; tenant-isolation and India-residency checks; a certification report per connector.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-16b-ecosystem-integration-v2.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/ecosystem-integration-v2 in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every Udofin event and API validates against the Ecosystem Integration Specification schema registry with canonical names unchanged; a breaking change without a new vN is rejected, and Pact tests pass in both pipelines.
- [ ] Signature (RFC 9421 or detached JWS), mTLS, replay and Idempotency-Key tests pass, and any payload without a consent reference or statutory-basis flag is rejected (CF para 13(4)).
- [ ] Each connector (Finbyx, third-party LOS/LMS, Equator and other ODR providers, LawDocsComply and third-party GRC tools) passes the certification suite, emits ConnectorCertified and stores its report as evidence (U18; OUT para 34).
- [ ] Collateral, co-lending, transfer, recovery, ADR and litigation events update the loan mirror and the Part 7A views for every product lifecycle including LAS, with daily reconciliation breaks aged (TDCR paras 117, 124; OUT para 39).
- [ ] The GRC export produces a schema-valid OSCAL assessment-results package with no unmasked identifier, and every endpoint and store involved is in India (CF para 14(4)).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 17 — Mobile and web release engineering (Play Store, App Store, PWA)

- **Outcome:** Store declarations, listings, signing, staged rollout, OTA policy, PWA
- **Depends on:** 4–16 (MVP scope)
- **Branch:** `feat/release-engineering`
- **Suggested sub-modules (one session each):** Google Play release; App Store release; PWA and OTA policy.

**Paste into Claude Code:**

```text
Phase 17 — Mobile and web release engineering (Play Store, App Store, PWA). Governing brief: docs/00-master-prompt.md (Part 12, Phase 17; Part 8A prevails on regulatory points).

On branch `feat/release-engineering`, prepare the releases in this order: Google Play first, then the App Store, plus the PWA.

Google Play:

- confirm that each pilot RE has reported the Udofin Android app on CIMS and that it appears on RBI's public list of DLAs deployed by REs before submission (CF para 18; Google Play India personal-loan requirement);
- Financial features declaration as a platform that facilitates loans by registered NBFCs or banks; names of all partner NBFCs and banks prominently in the description;
- listing metadata: minimum and maximum repayment period, maximum APR and a representative total-cost example; privacy policy URL; app category Finance;
- Data safety form matching the actual data flows and the permission policy; no prohibited permission in the merged manifest;
- Play App Signing; internal → closed → production staged rollout; Play Integrity configured;
- target API level 36 (Android 16) or higher, required for every new app and update since 31 Aug 2026 (extension to 1 Nov 2026 only on request), and 16 KB memory-page-size support for every native library (required since 1 Nov 2025 for apps targeting Android 15+); CI fails a release build that misses either.

App Store:

- submission by Udofin as a legal entity (Guideline 5.1.1(ix));
- maximum equivalent APR and payment due date disclosed; no offer above 36% APR and no loan repayable in full in 60 days or less in the iOS channel (Guideline 3.2.2(ix)); App Privacy labels matching flows; App Attest configured; separate CIMS line for the iOS app;
- TestFlight → phased release.

OTA and versions: EAS Update code signing, runtime-version policy, staged rollout with crash-rate rollback, release register; minimum supported version and six-month sunset (DPS para 68(2)(iii) baseline).

PWA: manifest, service worker for static assets only, install prompts, Lighthouse and Core Web Vitals checks.

Produce `docs/compliance/store-policy.md` with every requirement, its source URL, check date and evidence. Do not submit to any store without my explicit authorisation.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- One line per DLA per store in the DLA register before each store or PWA launch; checksum or store link published; old app versions retired within 6 months (CF para 18; DPS para 68) [Part 8A.1–8A.5, 8A.11]
- Mobile and web security baseline and pre-release VA/PT; vulnerability-free certificate and SBOM per material release (CYB 33, 106, 121) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-17-release-engineering.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/release-engineering in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Each pilot RE has reported the Udofin Android app on CIMS and the app appears on RBI's public list of DLAs before Play submission.
- [ ] The Play listing names all partner NBFCs and banks and shows minimum and maximum repayment period, maximum APR and a representative total-cost example; the Data safety form matches actual flows.
- [ ] The release build contains no Google Play prohibited permission and the iOS channel filters out offers above 36% APR or repayable in full within 60 days (Apple 3.2.2(ix)).
- [ ] EAS Update is code-signed with staged rollout and rollback; the minimum supported version and six-month sunset are enforced by the API.
- [ ] The Android release build targets API level 36 or higher and all native libraries support 16 KB memory pages (Google Play requirements).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase P — MVP hardening and pilot go-live

- **Outcome:** E2E, independent VAPT and MASVS assessment, DR and incident drills, RE onboarding sign-off, controlled Android and web go-live
- **Depends on:** 0–17 (12b and 16b only where a pilot RE attaches them)
- **Branch:** `release/pilot`

**Paste into Claude Code:**

```text
Phase P — MVP hardening and pilot go-live. Governing brief: docs/00-master-prompt.md (Part 12, Phase P; Part 8A prevails on regulatory points).

On branch `release/pilot`, for Products 1–2, the Android app, the borrower web app, the operations and lender portals, and the pilot REs, deliver:

- full E2E regression on real devices and browsers, including resume, outage and retry scenarios;
- independent VA and PT on production by a CERT-In-empanelled firm (Udofin policy; CYB para 122 requires independent, trained experts), CVSS-scored, all Critical/High findings closed and re-tested (CYB paras 121–126), plus a MASVS L2 + R assessment of the release build;
- source-code escrow deposit (where a pilot RE requires it) and the vendor security certificate for the release (CYB paras 105–106);
- load test at the Part 10.5 targets;
- DR switchover drill and restore of database, documents and workflow state, with post-drill reconciliation with each RE;
- an incident drill proving RE notification fits a 6-hour DAKSH filing measured from Udofin's detection (OUT para 61; CYB paras 28, 141) and Udofin's CERT-In report;
- a data-residency check of every environment and sub-processor;
- each pilot RE's sign-off: LSP agreement clause matrix, due-diligence pack, DLA on CIMS and on RBI's public list, grievance contacts, website links, product approval;
- an exit drill: full export for an RE, re-import test and purge certificate;
- production runbook and a controlled go-live checklist for my approval.

Do not deploy to production or publish to any store without my explicit authorisation.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Pilot gate: each pilot RE confirms its Annex-I CIMS entries, cooling-off period, retention schedule, KYC route set and recovery-agent status in writing [Part 8A.1–8A.5, 8A.11]
- Pilot gate: RE compliance approval recorded for every pilot product (CMP 9(7)); RE confirms CIMS DLA lines; first joint BCP test; clause matrix fully passed [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-p-pilot.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch release/pilot in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The independent VAPT (CERT-In-empanelled) and the MASVS L2 + R assessment have no open critical or high findings (CYB paras 121–126).
- [ ] The DR restore drill passes, and the incident drill shows RE notification within 2 hours of Udofin's detection so the RE can file within 6 hours (OUT para 61; CYB paras 28, 141).
- [ ] Production runs on India-region hosting only; the exit drill (export, re-import, purge certificate) passes.
- [ ] Each pilot RE has signed off the LSP agreement clause matrix, due-diligence pack, CIMS DLA entries, grievance contacts and product approval.
- [ ] The source-code escrow deposit and vendor security certificate for the release are delivered (CYB paras 105–106).
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 18 — Secured products (LAS, Home, LAP, Vehicle)

- **Outcome:** Product specs, collateral workflows via the RE, NSDL/CDSL pledge; LAS journey per Part 6.5
- **Depends on:** P; for LAS, Finbyx Phase 17 (Integration Spec Part 15)
- **Branch:** `feat/secured-products`
- **Suggested sub-modules (one session each):** Loan against securities (NSDL/CDSL, MF lien); Home loan; Loan against property; Vehicle loan.

**Paste into Claude Code:**

```text
Phase 18 — Secured products (LAS, Home, LAP, Vehicle). Governing brief: docs/00-master-prompt.md (Part 12, Phase 18; Part 8A prevails on regulatory points).

On branch `feat/secured-products`, for each secured product:

1. produce the product spec and feasibility note with the RE's collateral policy;
2. build the collateral workflows as RE-owned steps orchestrated by Udofin: securities pledge via NSDL/CDSL and mutual-fund lien in favour of the RE; property and vehicle data, valuer and legal-vendor hand-offs; document collection; release-of-security status from the RE;
3. apply the product's RE rules received through the catalogue (for example LAS LTV and cure periods set by the RE under CF Ch VIII; the LAS journey follows Part 6.5) and never compute collateral decisions in Udofin.

Tests: pledge always names the RE as pledgee; collateral status changes only on RE or depository events.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- LAS own-share exclusion and LTV margin notices (CF paras 105–106); housing classification (CF para 4(1)(xiv)) [Part 8A.1–8A.5, 8A.11]
- DIN/PAN of directors and guarantors (WD 19(1)); release-of-documents relay (RBC 35–39); LWD covenant check [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-18-secured-products.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/secured-products in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every securities pledge and MF lien names the RE as pledgee; Udofin is never a party to the security.
- [ ] Collateral status changes only on RE or depository events.
- [ ] Each secured product spec is approved by the RE, and collateral decisions are recorded as RE decisions.
- [ ] The LAS journey follows Part 6.5: no disbursal or 'pledged' status before the RE's CollateralPledgeCreated; drawing power, available amount, margin calls (including MarginCallLapsed), invocation and release come only from RE events or the facility-summary API; drawdowns use the DrawdownRequested API with an Idempotency-Key; OD screens stay hidden while mod.las.revolving is off; the pledge form carries the SEBI reasonable-notice undertaking (CF para 106; SEBI circular, 5 Feb 2026) [VERIFY: circular number].
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 18b — Additional product templates

- **Outcome:** Products 11–15 (Gold, Business/MSME, Microfinance, Supply-chain/TReDS invoice finance, Education) per Part 6.4, each after an approved spec and a partner RE
- **Depends on:** 18, 16b
- **Branch:** `feat/product-templates-18b`
- **Suggested sub-modules (one session each):** Gold loan (leads and branch appointment); Business / MSME loan; Microfinance loan; Supply-chain / TReDS invoice finance; Education loan.

**Paste into Claude Code:**

```text
Phase 18b — Additional product templates. Governing brief: docs/00-master-prompt.md (Part 12, Phase 18b; Part 8A prevails on regulatory points).

For Products 11–15 (Gold, Business/MSME, Microfinance, Supply-chain/TReDS invoice finance, Education; Parts 6.2 and 6.4), on branch `feat/product-templates-18b`, build each product only after I approve its specification and a partner RE confirms it:

1. write `docs/products/[code].md` from the 6.3 checklist and the 6.4 table, with the RE's policy references and the Finbyx R16 playbook code;
2. build the template on the common engine with its events, documents and disbursement routing;
3. apply each product's hard rules:
   - gold: collateral handled and stored only in RE branches by RE employees, so leads and branch appointments only (RBC paras 53–54); valuation and LTV shown only from RE data (CF paras 40, 43–44);
   - microfinance: household-income test and 50% cap (CF paras 51–57); loan card and no prepayment charge (RBC paras 78–81);
   - business/MSME: entity KYC, DIN or PAN of directors and guarantors (WD para 19(1)) and the CGTMSE flag (CF para 21(1));
   - supply chain: TReDS only as a referral with the RE as registered financier [VERIFY: TReDS Directions, 2026];
   - education: institution as end-beneficiary (CF para 10(1)).

Tests: golden journeys per product on app and web; the gold journey has no collateral-handling step in Udofin; the microfinance flag is set on every collateral-free MSME or education loan within the income threshold; the disbursement guard rejects any beneficiary not permitted by CF para 10(1).

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Gold: no Udofin handling of collateral (RBC paras 53–54), valuation and LTV only from RE data (CF paras 40, 43–44), auction and release notices shown as the RE's (RBC paras 58–69); microfinance household test and cap (CF paras 51–57) and loan card (RBC paras 78–81); MSME DIN or PAN of directors and guarantors (WD para 19(1)) and CGTMSE block on DLG (CF para 21(1)); end-beneficiary routing for education and supply chain (CF para 10(1)) [Part 6.4, 8A.1–8A.5, 8A.6–8A.10]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-18b-product-templates-18b.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/product-templates-18b in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Each of Products 11–15 has an owner-approved specification, a confirming partner RE and its Finbyx R16 playbook code before any code is merged.
- [ ] The gold journey contains no collateral-handling step in Udofin and shows valuation and LTV only from RE data (RBC paras 53–54; CF paras 40, 43–44).
- [ ] The microfinance flag and the 50% household obligation cap apply to every collateral-free loan within the income threshold, including MSME and education loans (CF paras 51, 55–57).
- [ ] The disbursement guard accepts only the borrower or a permitted end-beneficiary such as an institution, supplier or dealer (CF para 10(1)), and TReDS appears only as a referral with the RE as financier [VERIFY: TReDS Directions, 2026].
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 19 — Specialist products (feasibility-gated)

- **Outcome:** Feasibility notes and approved pilots for Products 7–10
- **Depends on:** P, 14
- **Branch:** `feat/specialist-products`
- **Suggested sub-modules (one session each):** resolution finance; medical and insurance-premium finance; legal-expense and award-enforcement finance; debt reset.

**Paste into Claude Code:**

```text
Phase 19 — Specialist products (feasibility-gated). Governing brief: docs/00-master-prompt.md (Part 12, Phase 19; Part 8A prevails on regulatory points).

For Products 7–10 (resolution finance, medical and insurance-premium finance, legal-expense and award-enforcement finance, debt reset), do not build until I approve a feasibility note for each. On branch `feat/specialist-products`, for each approved product:

- write the feasibility note: legal structure, RE partner, borrower protection, purpose and end-use verification, affordability model, Equator interaction (for resolution finance and debt reset), referral of non-recourse cases outside lending, and the risks;
- build only the approved pilot workflow on the common engine, with product-level delinquency and profitability analytics.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Feasibility gate for resolution finance and debt reset tests RSA 87–100 restructuring characterisation [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-19-specialist-products.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/specialist-products in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No specialist product is built without an approved feasibility note naming the RE partner and legal structure.
- [ ] Non-recourse legal-funding cases are referred outside the lending workflow and never presented as loans.
- [ ] Debt-reset and resolution-finance pilots include the affordability model and borrower-protection checks approved in the feasibility note.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 20 — Field app, analytics, AI and marketing expansion

- **Outcome:** U22 field app (if appointed), U20 governed AI, analytics, consented marketing
- **Depends on:** P
- **Branch:** `feat/field-analytics-ai`
- **Suggested sub-modules (one session each):** U22 field app; U20 governed AI; analytics and consented marketing.

**Paste into Claude Code:**

```text
Phase 20 — Field app, analytics, AI and marketing expansion. Governing brief: docs/00-master-prompt.md (Part 12, Phase 20; Part 8A prevails on regulatory points).

On branch `feat/field-analytics-ai`, build:

- U22 field and assisted-onboarding app (separate Expo target, MDM distribution) only for REs that appoint Udofin for assisted onboarding or recovery; digital KYC under KYC para 24 by the RE's process;
- U20 governed AI with a model inventory: document classification and extraction with human verification, application completeness checks, internal search, complaint categorisation, summaries; AI never decides credit, prices, moves money or rejects complaints;
- analytics with consented, pseudonymised events only;
- consented marketing campaigns through U16, using 140-series and promotional DLT categories, with opt-out honoured across channels.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- Field app digital KYC only after the authorised-officer question is resolved (KYC para 24) [Part 8A.1–8A.5, 8A.11]
- Field app shows the agent's digital ID and RE authorisation letter; assisted path for persons with disabilities (RBC 28, 95) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-20-field-analytics-ai.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/field-analytics-ai in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The field app is distributed only through MDM or managed store tracks and is enabled only for REs that appointed Udofin.
- [ ] AI never approves, rejects, prices or routes a loan, moves money or rejects a complaint; every model is in the model inventory with an owner and validation record.
- [ ] Marketing messages go only to borrowers with marketing consent, use promotional DLT categories and honour opt-out across channels.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 21 — Scale hardening and AWS migration

- **Outcome:** Scale tests, AWS ap-south-1 / ap-south-2, DR at scale
- **Depends on:** P, 16b, 18, 18b, 19, 20
- **Branch:** `feat/scale-aws`

**Paste into Claude Code:**

```text
Phase 21 — Scale hardening and AWS migration. Governing brief: docs/00-master-prompt.md (Part 12, Phase 21; Part 8A prevails on regulatory points).

On branch `feat/scale-aws`, run multi-tenant scale tests at 1 million+ borrowers and 100+ REs. Then:

- write and rehearse the AWS ap-south-1 / ap-south-2 migration runbook;
- run DR at scale;
- tune performance and mobile app size and start-up;
- repeat independent VAPT and the MASVS assessment.

Present a controlled migration plan for my approval.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- DC and DR in separate India regions; exit and portability dry-run (CYB 102; OUT 87–88) [Part 8A.6–8A.10, 8A.12–8A.15]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-21-scale-aws.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/scale-aws in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Scale tests meet the Part 10.5 targets at 1 million+ borrowers and 100+ REs.
- [ ] The AWS migration stays in ap-south-1 / ap-south-2 and passes a rehearsal with reconciliation.
- [ ] The DR drill passes at production scale and the repeated VAPT has no open critical or high findings.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

---

## 4. Utility prompts

Replace the text in square brackets before pasting.

| No. | When to use | Prompt |
|---|---|---|
| R1 | Start a sub-module | Continue Phase [n]. This session covers only the sub-module: [name]. Re-read the approved spec docs/specs/[file].md and the related REQ-IDs, confirm the scope in five lines, then build it. Do not touch other sub-modules. |
| R2 | Resume after an interruption | Read CLAUDE.md, docs/status and the open PR for Phase [n]. Summarise what is done, what is pending and any failing tests, then continue from the next pending item. |
| R3 | Status check | Give me a status report for Phase [n]: items done, items pending, tests run and their results, open [VERIFY] items, and any decision you need from me. Do not write code. |
| R4 | Fix failing tests | The following tests fail: [paste output]. Find the root cause, explain it in plain English, propose the fix, and apply it only after I approve. Re-run the full test suite and paste the results. |
| R5 | New RBI circular or amendment | I have added [RBI number, date] to docs/regulations/rbi/. Read it in full. List every requirement with a new REQ-ID, every existing REQ-ID it amends or withdraws, and every module, rule pack, RE data feed, store declaration and test affected. Propose the changes with effective dates. Do not change code until I approve. |
| R6 | Run the review gate | Run the review gate for Phase [n] from docs/01-phase-runbook.md. For each item, show the evidence (test name and output, query result, screenshot or file path). Mark any item you cannot evidence as NOT MET. |
| R7 | Change a specification | I want to change the approved spec for Phase [n]: [change]. Update docs/specs/[file].md, list the regulatory, consent, RE-contract and store-declaration impact, update the tests, and wait for my approval before changing code. |
| R8 | Regulatory check before a regulated workflow | Before building [workflow], list the applicable REQ-IDs, the RE-profile flags that decide applicability (RE type, layer, asset size, s.11A status, CYB chapter, microfinance acceptance), the [RE] or [UDOFIN] tag of each, and any [VERIFY] item. Confirm what is law and what is our interpretation. |

---

## 5. Progress tracker

| Phase | Spec approved (date) | PR | Review gate passed (date) | Notes |
|---|---|---|---|---|
| Phase 0 — Repository audit and architecture |  |  |  |  |
| Phase 1 — Platform foundation |  |  |  |  |
| Phase 2 — Database, tenancy and security |  |  |  |  |
| Phase 3 — Lender onboarding, product catalogue and configuration |  |  |  |  |
| Phase 3b — Communications and consent foundation |  |  |  |  |
| Phase 4 — Borrower identity and onboarding (app and web) |  |  |  |  |
| Phase 5 — KYC and verification adapters |  |  |  |  |
| Phase 6 — Credit data, affordability and eligibility |  |  |  |  |
| Phase 7 — Lender routing, offers, KFS and cooling-off |  |  |  |  |
| Phase 8 — Documents, eSign, eStamp and DMS |  |  |  |  |
| Phase 9 — Lender connectors and disbursement orchestration |  |  |  |  |
| Phase 10 — Repayments, mandates and reconciliation |  |  |  |  |
| Phase 11 — Loan mirror and borrower servicing |  |  |  |  |
| Phase 12 — Collections and recovery support |  |  |  |  |
| Phase 12b — Recovery support, notices and ADR access |  |  |  |  |
| Phase 13 — DLG management and lender disclosures |  |  |  |  |
| Phase 14 — Grievance, AI support and Equator |  |  |  |  |
| Phase 15 — Udofin finance, accounting and reporting |  |  |  |  |
| Phase 16 — Compliance, audit and security operations |  |  |  |  |
| Phase 16b — Ecosystem integration v2 |  |  |  |  |
| Phase 17 — Mobile and web release engineering (Play Store, App Store, PWA) |  |  |  |  |
| Phase P — MVP hardening and pilot go-live |  |  |  |  |
| Phase 18 — Secured products (LAS, Home, LAP, Vehicle) |  |  |  |  |
| Phase 18b — Additional product templates |  |  |  |  |
| Phase 19 — Specialist products (feasibility-gated) |  |  |  |  |
| Phase 20 — Field app, analytics, AI and marketing expansion |  |  |  |  |
| Phase 21 — Scale hardening and AWS migration |  |  |  |  |

*End of runbook.*
