# UDOFIN — Phase-wise Claude Code Runbook

**Companion to the Udofin Master Build Prompt v1.2** · 24 October 2026 · ready-to-paste instructions for every build phase

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
7. **Order:** 0 → 1 → 2 → 3 → 3b → 3c → 4 → 5 → 6 → 7 → 8 → 9 → 10 → 11 → 11b → 12 → 12b → 13 → 14 → 14b → 15 → 16 → 16b → 16c → 17 → P → 18 → 18b → 18c → 19 → 20 → 20b → 20c → 20d → 21. Phase 12b (recovery support) is attachable per RE; if it is skipped, treat it as satisfied for Phase 16b, which then covers the recovery, ADR and litigation views only as contract-conformance tests, and build 12b before any RE attaches Part 7A. Phases 16b and 18 (LAS) also wait for the Finbyx phases named in their Depends on line. Phases 18c, 20b, 20c and 20d are gated by owner decisions and licences recorded in docs/decisions/ (Part 7D FW4 gates G1–G5; IRDAI licence model) — if a gate is not met, the phase stops after its verification step. Do not start a phase until the phases it depends on are merged.
8. **Menus, screens and settings:** every phase builds the menu items, screens and settings its Part specifies, following Appendix G (Navigation, menus, screens and settings map); the borrower app keeps exactly five bottom tabs (Home, Loans, Pay, Help, Account).
9. **Companion prompts:** Phase 20b needs Operations Hub phase O6 for RE invoicing only (borrower plans are billed by Udofin itself); Phase 16c sends evidence to Operations Hub O12.

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
- repository controls from the first commit, equivalent to Finbyx Part 7L EO1 (Part 7H RA4.1): GitHub rulesets on `main` and `release/*` (pull request required; CODEOWNERS review, two reviewers for sensitive paths such as consent, KYC, payments and fund-flow validators, permission policy, CI workflows and `infra/`; required status checks; linear history; no force-push or deletion; no bypass for administrators), signed commits, secret scanning with push protection, Dependabot alerts and updates, protected release tags, and `staging` and `production` GitHub environments with required reviewers;
- `.env.example` files; a check that no secret appears in client bundles;
- OpenTelemetry with PII redaction, and India-resident error tracking per the Phase 0 ADR; mobile crash reporting with on-device scrubbing;
- Storybook for web components and a component catalogue for native.

Implement Money, Rate and Percentage on decimal.js (precision ≥ 40) with property-based tests. Build no business features. Open a PR with the test output, the permission-audit output and an export of the ruleset, CODEOWNERS and environment-protection settings as the first engineering-operations evidence (Part 7H RA4; filed to the Operations Hub console once phase O12 is live).

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
- maker_checker_request; audit_event (hash-chained per RE partition: each row stores the SHA-256 of its canonical content and of the previous row's hash, with a daily anchor hash written to write-once storage and a verifier job; this is the audit trail exported in RE archive folder 17, Part 7H RA3); idempotency_key; outbox_event;
- the external-access skeleton: `external_access_grant`, `external_access_session` and `external_access_query_log` tables (Appendix D) and the external-access role family (RE auditors, RBI supervisors, co-operative auditors) with SELECT-only, one-RE, time-boxed grants and no write path; the grant workflow is built in Phase 16c (Part 7H RA2);
- the RE-scoped vault tables and storage buckets keyed by RE, with per-RE KMS key references.

Implement:

- server-side authorisation (RBAC + ABAC);
- Postgres RLS on every RE-scoped and borrower-scoped table, enforced: the API connects as a non-owner role without BYPASSRLS; `FORCE ROW LEVEL SECURITY` on every tenant table; RE and borrower context set with `set_config(…, true)` inside each transaction;
- the auth abstraction over Supabase Auth: borrower OTP sessions with device-bound refresh, staff and RE SSO with mandatory MFA;
- the maker-checker framework;
- break-glass access for Udofin staff to RE data, logged and visible to the RE (OUT paras 24, 70);
- Supabase Data API (PostgREST, GraphQL) disabled, or application schemas unexposed with all privileges revoked from `anon` and `authenticated`; Storage RE-vault buckets private with no client policies; clients reach data only through the NestJS API.

Write isolation tests that try to read and write across REs, across borrowers and from a lender user into another RE's data, and prove they fail. Include a test proving that a query without context returns zero rows, and that a borrower JWT calling the Supabase Data API or Storage directly gets no data. Also prove that altering or deleting any `audit_event` row makes the chain verifier fail, and that an external-access role cannot write any table or read another RE's rows. Report results.

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

Phase 3c extends U1 with the full lender deal state machine, two-way due diligence, the per-deal configurator, RE export packs and exit (Part 7B UP1–UP3, UP5); design the U1 tables (`lender_tenant`, LSP agreement registry, activity gate) so that 3c adds the deal layer without breaking migrations, and keep commercials out of every table the ranking or routing services can read.

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

### Phase 3c — Lender partnership onboarding and deal configurator

- **Outcome:** Part 7B UP1–UP3, UP5: deal state machine with fail-closed gates and `LenderDeal*` events; two-way due diligence and LSP declarations; per-deal configurator with the neutrality firewall; RE export packs P1–P10; suspension, exit, freeze and data return
- **Depends on:** 2, 3, 3b (packs P3–P10 completed as their source modules land: P3 after 7, P5 after 13, P4 after 14b, P9 after 20; full exit archive after 16c)
- **Branch:** `feat/lender-deals`
- **Suggested sub-modules (one session each):** UP1 deal state machine, gates and pilot; Two-way due diligence and LSP declarations; UP2 configurator and neutrality firewall; UP3 export-pack framework (P1–P2 now; others as sources land); UP5 suspension, exit, freeze and data return; LenderDeal events and Finbyx contract tests; Menus, screens and settings (Part 7B (UP1–UP3, UP5)).

**Paste into Claude Code:**

```text
Phase 3c — Lender partnership onboarding and deal configurator. Governing brief: docs/00-master-prompt.md (Part 12, Phase 3c; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the partner-deal domain of `docs/ecosystem/infrabyx-integration-spec.md` v1.1 (`LenderDealProposed`, `LenderDealApproved`, `LenderDealActivated` with `mode` PILOT or GENERAL and `resumed`, `LenderDealSuspended`, `LenderDealTerminated`, `ExportRequested`, `ExportCompleted`) and raise any gap as a versioned contract change; (ii) the current Google Play India personal-loan policy text on naming partner lenders in the listing [VERIFY]; (iii) that the bank, SFB and co-operative-bank rule packs are still `unmapped`, so those REs cannot pass due diligence (UP-C03) [VERIFY: bank texts]; (iv) the OUT paras 34 and 74 clause list in the U1 clause matrix against docs/regulations/rbi/. Then, on branch `feat/lender-deals`, build Part 7B UP1–UP3 and UP5 on top of U1 and U2 (UP4, the non-RE society track, is Phase 18c):

- UP1 deal state machine: `lender_deal` from PROPOSED through DUE_DILIGENCE, LEGAL, TECHNICAL_CERTIFICATION, PILOT and ACTIVE to TERMINATED, with WITHDRAWN and the UNDER_REVIEW overlay that never stops service; every transition through the gate engine, fail-closed, maker-checker inside Udofin and the RE approver's name, role and authority reference (`re_change_approval`). The PILOT gate requires the RE's CIMS acknowledgement for each Udofin DLA per platform (CF para 18(1)–(2)), the RE website disclosure snapshot (CF para 9(4)), the store-listing snapshot, live GRO and nodal-officer contacts (CF para 12(2)), the redress-profile hook (UB-C09; the profile itself is built in Phase 14b) and `ConnectorCertified`. The U1 activity gate reads the deal state: nothing borrower-facing exists before PILOT. Pilot plan with caps and the system-measured exit criteria;
- two-way due diligence: Udofin's versioned DD pack with an expiry per item (CF para 6(2); OUT paras 29–32, 38); counter-party diligence on the RE, including `re_board_policy_evidence` (OUT para 20; RBC para 7; CF paras 6(4), 20(1); CIR para 20); the signed `lsp_declaration` at LEGAL and annually (OUT paras 18(vi), 59; CF paras 10(1)–(4), 13(1), 14(3)–(4), 18(6)); certification shown only as programme status, never as a certificate;
- UP2 per-deal configurator: the twelve sections of the immutable, diffed, effective-dated `deal_config_version` with approval on both sides and Udofin legal sign-off for sections 4, 7, 8, 9 and 10; the in-flight rule (an application keeps its submission version; an accepted KFS binds the RE within validity, RBC para 29(2) Explanation); commercials in the separately keyed `deal_commercials` schema;
- neutrality firewall (CF para 7(4)): the schema validator rejects any priority, boost, featured, sponsored, default_selected, rank_weight or badge key; the ranking, matching, routing, offer, AI and marketing database roles have no grant on `deal_commercials`, `dlg_*` or `deal_config.commercials`; any borrower-facing Udofin fee line fails validation (CF para 10(4)); clawback terms count inside the 5% DLG cap (CF para 24); wellness add-ons can never be a deal item;
- UP3 export packs P1–P10: the pack framework (README, `manifest.json` with SHA-256 per file and per pack, detached JWS, CSV and XLSX, PDF/A, JSON Lines, `reconciliation.xlsx`), snapshot generation on a read replica, masking levels, maker-checker for P8 and for unmasked P3, P4 and P6, and the hash-verification tool. P1 and P2 now; the others are wired as their source modules land (P3 after Phase 7, P5 after 13, P4 after 14b, P9 after 20);
- UP5 suspension and exit: the four suspension types; the borrower-continuity table enforced per borrower position; a per-RE freeze flag checked by every purge job (OUT para 87); `deal_exit` states; data return, RE acknowledgement by hash and destruction certificate (OUT paras 42, 88, 97(xvi)); DLG cover and disclosure survive exit (CF paras 27(2), 28); an annual exit dry-run per active RE;
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7B (UP1–UP3, UP5) on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed;

Publish the `LenderDeal*` events with JSON Schemas and Pact tests; Finbyx consumes them into the RE's LSP register and the OUT para 36 central record.

Tests and acceptance evidence:

- every UP1, UP2, UP3 and UP5 acceptance test in Part 7B;
- PILOT is refused while any gate item is missing, and the error names each missing item;
- a `deal_config` with a `featured` key fails validation; the ranking role gets 'permission denied' on `deal_commercials` in CI; raising RE A's sourcing fee from 1% to 3% leaves the offer order unchanged for an identical synthetic borrower;
- an application submitted under version 4 still uses version 4 after version 5 takes effect;
- every pack verifies against its manifest, one altered byte fails, regeneration from the same snapshot gives identical hashes, and a cross-RE row aborts generation;
- with a freeze active a scheduled purge is blocked and logged; after TERMINATED the monthly DLG disclosure still runs for open sets;
- each transition emits exactly one event with the correct `mode`; replay is idempotent;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the deal state machine with its gate table, the `deal_config` JSON Schema with the guard-rail validator rules, the pack catalogue with masking levels, and the lender-portal and operations-portal menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-3c-lender-deals.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/lender-deals in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No borrower-facing journey, offer or message exists for a lender before its deal reaches PILOT, and PILOT is refused while the RE's CIMS acknowledgement for each Udofin DLA per platform, the RE website disclosure snapshot, the store-listing snapshot, live GRO and nodal-officer contacts or the connector certification is missing, with each missing item named (CF paras 9(4), 12(2), 18(1)–(2); Part 7B UP1).
- [ ] The `deal_config` schema rejects any priority, boost, featured, sponsored, default_selected, rank_weight or badge key; the ranking, matching, routing, offer, AI and marketing roles get 'permission denied' on `deal_commercials` and `dlg_*` in CI; a sourcing-fee change from 1% to 3% leaves the offer order unchanged for an identical synthetic borrower (CF para 7(2), 7(4)).
- [ ] Any borrower-facing Udofin fee line, any netting from disbursal or recovery proceeds and any DLG or clawback term above the 5% cap fails validation (CF paras 10(4)–(5), 24).
- [ ] Every UP3 pack covers one RE only, verifies file by file against its signed manifest, reproduces identical hashes from the same snapshot, and P8 or any unmasked P3, P4 or P6 pack needs an RE maker-checker approval (OUT paras 34, 36, 81).
- [ ] With an exit freeze active no purge, erasure or alteration of the RE's data runs; the exit plan cannot be approved without a treatment for every borrower position; DLG disclosure continues after TERMINATED (OUT paras 42, 87–88, 97(xvi); CF paras 27(2), 28).
- [ ] Each deal transition emits exactly one `LenderDeal*` event with the correct `mode` and `resumed` values, validated against Integration Spec v1.1 and Pact-tested with Finbyx; replay is idempotent.
- [ ] Every screen in the `Menu and screens` subsections of Part 7B (UP1–UP3, UP5) exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
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
- U25 borrower dashboard: all loans, charges, dues, documents, consents and data-sharing history, complaints; no expense tracker here: the expense tracker and budget planner are Part 7D FW3, built in Phase 20b behind the FW4 gate in a separate store; the dashboard's document downloads are Part 7C UB1, built in Phase 11b.

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

### Phase 11b — Borrower downloads and tax documents

- **Outcome:** Part 7C UB1–UB2: My documents and data, DPDP requests and borrower export; RE-issued tax certificates under the Income-tax Act 2025 with the regime notice; Form 131 relay and GSTIN profile
- **Depends on:** 3b, 8, 11; `InterestCertificateIssued` from Finbyx Phase 13b (mock until then)
- **Branch:** `feat/borrower-downloads-tax`
- **Suggested sub-modules (one session each):** UB1 document catalogue and RE-served documents; My data: DPDP requests and borrower export; UB2 certificate mirror, Act variants and regime notice; Business borrowers: Form 131 relay and GSTIN profile; Menus, screens and settings (Part 7C (UB1–UB2)).

**Paste into Claude Code:**

```text
Phase 11b — Borrower downloads and tax documents. Governing brief: docs/00-master-prompt.md (Part 12, Phase 11b; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the Income-tax Act, 2025 provisions used by UB2 against the official text and the CBDT concordance: s.22(1)(b)–(c), 22(2)(a)–(b), 22(4) and 22(5) (house-property interest and the lender's certificate), s.123 with Schedule XV (home-loan principal), s.129 (education-loan interest), ss.130–132 (legacy windows), s.202 (default new regime), the s.393 table entry replacing old s.194A, Form 131 and Form 168 [VERIFY]; keep s.131 disabled until the successor of old s.80EEA is confirmed [VERIFY]; confirm that FY 2025-26 documents keep 1961-Act references [VERIFY: CBDT transition guidance]; (ii) the `InterestCertificateIssued` and `DocumentShared` schemas and `GET /v1/documents/{id}` in Integration Spec v1.1, with a contract-faithful mock until Finbyx Phase 13b publishes the certificate; (iii) DPDP Rules r.14(3) (90-day period for grievances; whether it bounds s.11–12 access, correction and erasure requests [VERIFY]) and the commencement of DPDP ss.11–14 on 13 May 2027 [VERIFY]; (iv) the GST positions in UB2 (Notification 12/2017-CT(Rate) entry 27(a); CBIC Circular 245/02/2025-GST; CGST Rule 48(4)) [VERIFY]. Then, on branch `feat/borrower-downloads-tax`, build Part 7C UB1–UB2:

- UB1 My documents and data: the `document_catalogue_entry` model with issuer, owner, source, availability state and rule; RE documents served only as the RE-signed version after hash and JWS verification, never re-rendered (CF para 9(3)); 'Not yet issued by [RE name]' with a one-tap U12 service request on the deal SLA (UP2); co-borrower, guarantor and authorised-signatory scoping; legal-heir requests routed to the RE (RBC para 38); release-of-documents tracker with the 30-day and 60-day clocks (RBC paras 35–41); post-exit access period (UP5); society labels for UP4 lenders;
- my data: DPDP ss.11–14 as practice now (summary, correction, erasure with plain-language retention reasons, nomination); loan-data requests forwarded to the RE as `DataPrincipalRequest` within 1 working day; a 30-day Udofin target, inside the 90-day grievance period of DPDP Rules r.14(3) (whether that period bounds s.11–12 requests is [VERIFY]), with a shorter RE or RBI clock winning;
- 'Download my data': scope selection; folder archive with README in the borrower's language, `manifest.json`, CSV, JSON, PDF/A and XLSX; step-up authentication within 5 minutes; passphrase-encrypted package; signed URL valid at most 15 minutes; alert to every registered channel; purge after 7 days; at most 3 full exports per 30 days; wellness data is a separate package from its own store and never merged (UB-C03);
- UB2 tax documents: the certificate mirror state machine; certificates displayed only when received from the RE and verified, because the deduction depends on the certificate of the person to whom interest is payable (ITA25 s.22(2)(a)); 1961-Act or 2025-Act variant by period; the fixed regime notice (ITA25 s.202) on every view and download; caps and eligibility never computed; the optional summary card labelled 'not a tax certificate'; s.129 hidden without the RE's eligibility reference; provisional and final requests; 8-year retention; no income-tax portal credentials, OTPs or AIS downloads ever requested;
- business borrowers: Form 131 upload through the system picker (no storage permission; CF para 13(1)), fields confirmed by the borrower, relayed as `DocumentShared`, RE reconciliation status shown; Udofin never computes TDS and never files Form 140; `business_tax_profile` with GSTIN validation (format, check digit, PAN segment, State code, status); RE invoices mirrored; no Udofin GST invoice for an RE fee (CF para 10(4));
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7C (UB1–UB2) on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed;

Tests and acceptance evidence:

- every UB1 and UB2 acceptance test in Part 7C;
- a KFS or certificate with a tampered byte is not displayed and raises an RE exception;
- an FY 2025-26 certificate shows 1961-Act references and a tax year 2026-27 certificate shows ITA25 references, each with the regime notice;
- a repository test proves no tax-certificate template exists in Udofin's document generator (UB-C05);
- a full export contains README, manifest and every selected scope, recomputed hashes match, the package will not open without the passphrase, and a fourth full export in 30 days is refused;
- wellness data never appears in a loan export, even with 'select all';
- an erasure request covering loan data reaches the RE within 1 working day with the retention reasons shown to the borrower;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the document catalogue, the borrower export package layout with its README and manifest, the certificate validation rules with the regime-notice text, and the borrower menu and settings map for My documents and tax documents for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-11b-borrower-downloads-tax.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/borrower-downloads-tax in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Udofin displays only RE-signed documents and certificates whose hash and JWS verify; a tampered file is never shown and raises an RE exception, and no tax-certificate template exists in Udofin's generator (CF para 9(3); ITA25 s.22(2)(a); UB-C01, UB-C05).
- [ ] Every certificate view and download carries the fixed regime notice (ITA25 s.202); FY 2025-26 documents show 1961-Act references and tax year 2026-27 onwards show ITA25 references (s.22, s.123 with Schedule XV, s.129); s.131 stays disabled until the old s.80EEA successor is confirmed [VERIFY]; no deduction or cap is computed.
- [ ] Loan-data DPDP requests reach the RE as `DataPrincipalRequest` within 1 working day, and the clock shows the 30-day Udofin target inside the 90-day grievance period of DPDP Rules r.14(3) [VERIFY: whether it bounds s.11–12 requests; commencement 13 May 2027].
- [ ] The borrower export requires step-up within 5 minutes, is passphrase-encrypted, downloadable only through a signed URL valid at most 15 minutes, limited to 3 full exports per 30 days, purged after 7 days, and never contains wellness data (UB-C02, UB-C03).
- [ ] Form 131 uploads use only the system picker with no storage permission in the manifest (CF para 13(1)); an RE PAN that does not match the loan's RE is rejected; a GSTIN whose PAN segment or check digit is wrong fails; no Udofin GST invoice is produced for any RE fee (CF para 10(4)).
- [ ] Every screen in the `Menu and screens` subsections of Part 7C (UB1–UB2) exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
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
- the 30-day clock and escalation information to RBI CMS (https://cms.rbi.org.in) and the CRPC address when the RE rejects, partly rejects or does not reply within 30 days (CF para 12(4)); the full chain (lender redress profile, the RE's Internal Ombudsman under the Internal Ombudsman Directions 2026, the RBI Ombudsman under the Integrated Ombudsman Scheme 2026 with its 90-day window, parallel routes, reopen, rating and case packs) is Phase 14b (Part 7C UB3–UB4), which supersedes U15 where they differ, so build the `grievance` aggregate here for 14b to extend;
- AI support assistant answering only from approved sources (RE product documents, KFS, FAQs, case status), with citations, hand-off to a human and no invented rights or outcomes; it never rejects or closes a complaint; build now the minimum U20 controls it needs (model-inventory entry, approved-source retrieval, prompt redaction, India-region or RE-approved endpoint per CF para 14(4)), which Phase 20 extends;
- Equator access only for cases the RE has referred (Udofin never refers), after the RE's process or under a pre-named institution clause or written post-dispute consent; a signed link into Equator's web flow from the app, no separate app; outcome status flows back (full specification in Part 7A UR2, built in Phase 12b);
- feedback (CSAT/NPS) through U16.

Tests: complaint cannot be closed by any Udofin role; 30-day escalation message triggers; AI refuses out-of-scope questions; Udofin credentials cannot create an ADR referral, and Equator access appears only for RE-referred cases with a recorded basis.

Regulatory additions for this phase (Part 8A.16.2) — include them:
- LSP nodal officer, intake, immediate RE routing, CMS and CRPC escalation; CIR complaint fields (CF para 12; CIR para 35(8)) [Part 8A.1–8A.5, 8A.11]
- RE GRO routing, RBI Ombudsman prompt (rejection, dissatisfaction or 30 days; 90-day RB-IOS 2026 window; full chain in Phase 14b), FS-format complaint MIS (OUT 56–57; FS 21(10)) [Part 8A.6–8A.10, 8A.12–8A.15]

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

### Phase 14b — Grievance escalation chain v2

- **Outcome:** Part 7C UB3–UB4: lender redress profile; tiers to the RE Internal Ombudsman and the RBI Ombudsman with the 90-day window; parallel routes; twelve borrower capabilities, case packs and help-centre content model
- **Depends on:** 3c, 11b, 14
- **Branch:** `feat/grievance-chain-v2`
- **Suggested sub-modules (one session each):** Lender redress profile; Tier engine, clocks and automatic escalations; Parallel routes and display rules; UB4 borrower capabilities and case pack; Help-centre content model, languages and MIS; Menus, screens and settings (Part 7C (UB3–UB4)).

**Paste into Claude Code:**

```text
Phase 14b — Grievance escalation chain v2. Governing brief: docs/00-master-prompt.md (Part 12, Phase 14b; Part 8A prevails on regulatory points).

Before writing the specification, verify against the official texts and record the paragraph numbers in the regulatory register: (i) the Reserve Bank – Integrated Ombudsman Scheme, 2026 (notified 16 Jan 2026, effective 1 Jul 2026): coverage and exclusions (cl.1(3)), complaint first to the RE (cl.10(1)(e)), the RE's 30-day period (cl.10(1)(f)), the 90-day window to file after that period or the RE's last reply (cl.10(1)(g)), representatives other than advocates (cl.10(1)(b)), the Principal Nodal Officer and display duties (cl.18), and the transition rule for complaints received before 1 Jul 2026 (cl.20) [VERIFY: clause numbering]; (ii) the RBI (NBFCs – Internal Ombudsman) Directions, 2026 (14 Jan 2026): applicability thresholds, auto-escalation of partial or full rejections within 20 days and the final reply within 30 days [VERIFY: paragraph numbers]; (iii) the current NHB route for HFCs and the post-2026 CEPC route for NBFCs outside RB-IOS [VERIFY]; (iv) CMS upload limits, the Insurance Ombudsman Rules, 2017 limits and the Data Protection Board commencement [VERIFY]; (v) `GrievanceReopened`, `GrievanceRated` and `OmbudsmanReferralRecorded` in Integration Spec v1.1. Then, on branch `feat/grievance-chain-v2`, build Part 7C UB3–UB4 on the U15 `grievance` aggregate (UB3 and UB4 supersede U15 where they differ):

- lender redress profile: the versioned `re_redress_profile` per RE (`rbios_covered`, `io_applicable`, `top_tier` of RBI Ombudsman, CEPC regional office, NHB, bank RB-IOS or co-operative route, and the contacts), recomputed on every asset-size update and required before an RE deal reaches PILOT (UB-C09);
- tiers T0–T5 and the co-operative route: help centre; Udofin nodal grievance officer (CF para 12(1)) with forwarding of every RE-related complaint targeted within 1 hour and the RE's receipt acknowledgement stored; the RE GRO with day-20 and day-25 reminders; the RE's Internal Ombudsman (IO 2026); the T4 panel that opens at the earliest of a whole or partial rejection, a borrower 'not satisfied' or 30 days without reply (CF para 12(4)), and closes 90 days after the later of the end of the RE's 30-day period and the RE's last communication (RB-IOS cl.10(1)(g)); the 2021 Scheme applies only to Ombudsman filings made before 1 Jul 2026 [INTERP; VERIFY: cl.20]; chains that start at the help section of the RE's website or a Finbyx-hosted page appear in the borrower's case list through `GrievanceUpdated`;
- clock rules: legal clock from the RE's receipt; if unacknowledged after 1 business day, Udofin's forwarding time is shown as the receipt date with the basis disclosed in the case pack; calendar days; a reopen gets a new RE receipt and recomputes the window; Udofin never pauses an RE clock;
- parallel routes by subject (credit information with the CIR para 35 clocks and mandatory bank or UPI details; insurance; personal data; subscription to consumer routes; recovery conduct; fraud; Sachet; ODR only through RE referral or borrower consent; courts), never in place of the RBI route for an RE complaint;
- display, states and automatic actions: contacts on every help screen (CF para 12(2)); neutral wording with a linter for discouraging phrases (UB-C12); the full `grievance` state machine; internal escalations only; Udofin never files externally or represents the borrower; AI drafts for staff review and never rejects, closes or advises against escalation (U20);
- UB4: the twelve borrower capabilities (raise, attach through the picker, acknowledgement, track, reply, escalate, case pack, reopen within 30 days, rate, withdraw, nominate a non-advocate representative, callback and accessible format); the PDF/A and JSON case pack signed by Udofin; the help-centre content model with owner, approver, sources and review dates; English and Hindi at launch with RB-IOS salient features in the regional language; WCAG 2.2 AA; MIS feeding UP3 pack P4 and the RE's FPC review (RBC para 8);
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7C (UB3–UB4) on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed;

Tests and acceptance evidence:

- every UB3 and UB4 acceptance test in Part 7C;
- golden date cases: a complaint received by the RE on 1 Aug 2026 with no reply opens the external route on 1 Sep 2026 and closes it on 29 Nov 2026 [VERIFY: day-count convention]; one received by the RE on 20 Jun 2026 and taken to the Ombudsman after 1 Jul 2026 gets the 90-day window under RB-IOS 2026 [INTERP; VERIFY: cl.20];
- an RE with ₹80 crore of assets and no deposits shows the CEPC regional office; an HFC never shows RB-IOS; a society loan never shows any RBI route;
- no Udofin role can set `RE_FINAL_REPLY` or close an RE-owned complaint (CF para 12(3); OUT para 56);
- a partial rejection by an `io_applicable` RE without IO status by day 20 pages Udofin compliance and the RE nodal officer;
- a nominated representative can view but not reply, withdraw or reopen; a one-star rating shows escalation options and no promotion;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the redress-profile decision table, the tier and clock specification with the golden date cases, the grievance state machine, the case-pack layout, and the help-centre, complaint and staff-queue menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-14b-grievance-chain-v2.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/grievance-chain-v2 in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The `re_redress_profile` exists and is current for every RE before its deal reaches PILOT, and routes an RE with ₹80 crore of assets and no deposits to the CEPC regional office, an HFC to the NHB route and a society loan to the co-operative route, never RBI (RB-IOS 2026 cl.1(3); OUT para 57(4)) [VERIFY: clause numbering].
- [ ] The T4 panel opens at the earliest of a whole or partial rejection, a borrower 'not satisfied' or 30 days without an RE reply, and closes 90 days later (CF para 12(4); RB-IOS 2026 cl.10(1)(f)–(g)); golden cases pass for 1 Aug 2026 (opens 1 Sep, closes 29 Nov 2026) and for a pre-1 Jul 2026 complaint under the 2021 Scheme window [VERIFY: day-count convention].
- [ ] For an `io_applicable` RE, a partial or full rejection without Internal Ombudsman status by day 20 raises an internal escalation to Udofin compliance and the RE nodal officer (IO 2026) [VERIFY: paragraph numbers].
- [ ] No Udofin role or AI action can set `RE_FINAL_REPLY`, close, reject or settle an RE-owned complaint, and Udofin never files externally on the borrower's behalf (CF para 12(3); OUT para 56; U20).
- [ ] All twelve UB4 capabilities work identically on Android, iOS and web; a reopen keeps the case ID with a new RE receipt time; the case pack validates as PDF/A with the clock basis and hashes and excludes RE internal notes; a credit-information complaint cannot be submitted without bank or UPI details (CIR para 35).
- [ ] `GrievanceReopened`, `GrievanceRated` and `OmbudsmanReferralRecorded` validate against Integration Spec v1.1, and P4 complaint counts equal the register for the same RE and period.
- [ ] Every screen in the `Menu and screens` subsections of Part 7C (UB3–UB4) exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
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
- RE, auditor and RBI read-only, time-boxed access to that RE's data, logs and evidence (OUT paras 34, 74(ii), 81; CYB para 62(2)), as the minimum on the Phase 2 skeleton; the full grant workflow, scope catalogue, masking and access logs are Phase 16c (Part 7H RA2);
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

On branch `feat/ecosystem-integration-v2`, bring every Udofin connector to the Infrabyx Ecosystem Integration Specification v1.1 (`docs/ecosystem/infrabyx-integration-spec.md`):

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

### Phase 16c — Risk function, supervisory access, data portability and engineering assurance

- **Outcome:** Part 7H RA1–RA4: LSP risk register, KRIs, DLG cap monitor and LawDocsComply feed; RE auditor and RBI read-only access; RE archives and India-only RE-controlled storage; engineering operations, app-store release gates, MASVS and certification readiness
- **Depends on:** 2, 3c, 13, 14b, 16, 16b; Operations Hub O12 for the evidence console (local evidence store until then)
- **Branch:** `feat/risk-access-portability-assurance`
- **Suggested sub-modules (one session each):** RA1 risk register, KRIs and DLG cap monitor; RA1 quarterly packs and LawDocsComply feed; RA2 external-access workflow and controls; RA3 archive folders, export jobs and storage targets; RA3 backups to RE storage and restore tests; RA4 engineering-operations parity, release gates and MASVS; Menus, screens and settings (Part 7H (RA1–RA4)).

**Paste into Claude Code:**

```text
Phase 16c — Risk function, supervisory access, data portability and engineering assurance. Governing brief: docs/00-master-prompt.md (Part 12, Phase 16c; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) OUT paras 30, 34(ii), (iv), (vii)–(ix), (xii), 38, 61, 74(ii), (vi), (xii), 77, 81, 87 and 97(xvi), CYB paras 46, 57, 105–106 and 121–126, CF paras 20(3), 21(1), 23–28, and the ORM guidance note paras 31–33, 42 and 73 (guidance, not a Direction); (ii) counsel's opinion on notifying the RE of a direct RBI request and whether RBI Act s.45NAA could ever apply [VERIFY]; (iii) Integration Spec v1.1 risk, audit and portability events (`KriBreached`, `LossEventRecorded`, `LimitBreached` with `limit_type` and `status` OPEN or CURED, `RiskSnapshotPublished`, `ExternalAccessGranted`, `ExternalAccessUsed`, `ExternalAccessRevoked`, `StorageTargetConnected`, `BackupCompleted`, `RestoreTested`, `ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`) and the export-archive standard; (iv) Finbyx Part 7L EO1–EO5 and the Operations Hub OH13 and OH14 contracts (until Hub phase O12 is live, keep evidence in a local store with the same schema); (v) Microsoft 365 data residency for any SharePoint or OneDrive target [VERIFY]. Then, on branch `feat/risk-access-portability-assurance`, build Part 7H RA1–RA4:

- RA1 risk function: register R01–R15 with owner, 5 × 5 ratings, controls with test references, appetite and KRIs; the KRI library with the formulas and Board thresholds of RA1.3, tightened per deal; the DLG cap monitor run daily, on every `LoanDisbursed` and on every cover change (cover ≤ 5% of the total amount disbursed out of each fixed set, CF para 24(1)–(2); repayments never reduce the denominator and invoked cover is never reinstated, para 25(4); permitted forms only, CF para 23; current auditor declaration, CF para 20(3)), refusing any cover that would exceed the cap and sending `LimitBreached` (`DLG_CAP`, OPEN then CURED); loss events (ORM para 42), semi-annual RCSA and impact tolerances (ORM para 33); the quarterly pack per RE within 15 days of quarter-end; the LawDocsComply feed with aggregates and HMAC pseudonyms keyed in the tenant's KMS, no PII; Udofin never computes or displays any RE's CRAR, NPA or ALM metrics as its own;
- RA2 RE auditor and supervisor access: the Integration Spec 4.7 lifecycle (REQUESTED → BASIS_RECORDED → SCOPE_DEFINED → RE_APPROVED → PROVIDER_APPROVED → PROVISIONED → ACTIVE ⇄ EXTENDED → EXPIRED or REVOKED → ARCHIVED) on the Phase 2 role skeleton, including grants federated from the RE's register through `POST /v1/external-access/grants`; one RE per scope; grantee types and basis codes from the Spec code tables (OUT paras 34(ii), (vii)–(ix), 74(ii), 81; CYB paras 46, 57); RE maker-checker approval, which cannot narrow an RBI request; RE notice of a direct RBI request within 1 hour unless legally barred; named users, MFA, `rbi.org.in` domain check; default 30 days and a hard maximum of 90 days per grant including extensions; read-only snapshot, SELECT-only grants and `read:*` scopes; masking with logged per-record unmask; watermarked, hashed, capped exports; daily activity report to the RE's CCO; revocation within 60 seconds;
- RA3 export and RE-controlled storage: the data-class rules (wellness and insurance data never in an RE archive); folders 00–17 in the Integration Spec 12.1 archive standard (profile `udofin_re_v1`: `00 Start Here` with README as PDF, DOCX and TXT, `[dataset].csv`, `.xlsx` and `.schema.json`, `manifest.json` with a detached JWS, control totals reconciled before signing, folder 12 as a separately encrypted restricted archive) with the open-source verifier; export jobs with second RE approver for full or exit exports; storage targets under the Integration Spec 12.2 `StorageTarget` contract with residency checks at registration, weekly and before every full or exit export (S3 ap-south-1 or ap-south-2, Azure India regions, GCS asia-south1 or asia-south2, SharePoint or OneDrive only with attested India residency, RE data centre in India; Google Drive only for non-regulated data and never borrower data; CF para 14(4); OUT para 74(vi)); optional daily backups to RE storage and quarterly restore tests;
- RA4 engineering operations: parity with Finbyx EO1–EO5 (rulesets, CODEOWNERS, signed commits, the EO1.6 platform patch SLAs of 72 hours for critical, 7 days for high, 30 days for medium and 90 days for low, SBOM, VA every 6 months and PT every 12 months, CYB paras 105–106 escrow and certificates where an RE requires them); the app-store release controls of RA4.2 as pipeline gates that Phase 17 applies; the MASVS v2.1.0 programme tested under the MAS-L2 and MAS-R profiles (RA4.3); certification readiness with the claims linter (RA4.4): never claim a certification before the certificate or report is issued;
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7H RA1–RA4 on the channel and workspace named there (navigation map in Appendix G), including the lender-portal `Risk`, `Audit access` and `Exports` menus, the auditor and supervisor workspace (channel G) and the operations-portal `Risk`, `Compliance › External access`, `Portability` and `Engineering` menus: list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed.

Tests and acceptance evidence:

- every RA1–RA4 acceptance test in Part 7H;
- a KFS execution without acknowledgement raises `KriBreached` within 5 minutes; a cover top-up that would take a DLG set above 5% of its total amount disbursed is refused, and a computed ratio above 5% raises `LimitBreached`;
- a quarterly pack for RE A contains nothing about RE B, and no risk payload contains a name, phone, PAN, account number or Aadhaar reference;
- a grant without basis, RE approval or expiry cannot be provisioned; an extension beyond 90 days from `valid_from` is refused; a grantee cannot write or read another RE (penetration cases);
- a Google Drive target is refused for any borrower data class and a non-India S3, Azure or GCS target is refused; the verifier detects one altered byte; LibreOffice and veraPDF pass every generated XLSX, DOCX and PDF/A file in CI;
- a release with a changed Data safety answer cannot be submitted; the copy linter fails 'ISO 27001 certified' without an issued-certificate record;
- every screen in the RA1–RA4 `Menu and screens` lists renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the risk register with KRI formulas and thresholds, the access-grant state machine and scope catalogue, the RE archive folder map, the release-gate list, and the RA1–RA4 menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-16c-risk-access-portability-assurance.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/risk-access-portability-assurance in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every R01–R15 risk has an owner, a tested control and a KRI; a KFS execution without acknowledgement raises `KriBreached` within 5 minutes; no risk payload carries PII and the LawDocsComply feed uses HMAC pseudonyms only; no RE prudential ratio appears as a Udofin metric (CF para 6(2)–(4); OUT paras 30, 38, 61; ORM paras 33, 42).
- [ ] A cover deposit or top-up that would take a DLG set above 5% of its total amount disbursed is refused; repayments never reduce the denominator and invoked cover is never reinstated; a computed ratio above 5% raises `LimitBreached` (`DLG_CAP`, OPEN, then CURED with a higher `update_seq`); a non-permitted DLG form or an arrangement without a current auditor declaration cannot be saved (CF paras 20(3), 23, 24, 25(4)).
- [ ] External-access grants follow the Integration Spec 4.7 lifecycle (REQUESTED to ARCHIVED, with PROVIDER_APPROVED and ACTIVE ⇄ EXTENDED); none is provisioned without a recorded basis, RE approval and expiry; the default is 30 days and no grant, with extensions, runs beyond 90 days from `valid_from`; grantees are read-only, one-RE, masked by default with logged unmask, and are revoked within 60 seconds; a direct RBI request notifies the RE within 1 hour unless legally barred (OUT paras 34(ii), (vii)–(ix), 74(ii), 81; CYB paras 46, 57).
- [ ] RE archives follow the Integration Spec 12.1 standard (profile `udofin_re_v1`: `00 Start Here`, README as PDF, DOCX and TXT, `[dataset].csv`, `.xlsx` and `.schema.json`, signed manifest, control totals, restricted folder 12 as a separate encrypted archive) that the verifier checks byte for byte; they never contain wellness, insurance or another RE's data and are written only to India-region targets re-verified before every full or exit export; Google Drive never receives borrower data (CF para 14(4); OUT paras 74(vi), 87).
- [ ] The app-store release gates block a changed permission manifest, Data safety answer or partner list without approval; the latest MAS-L2 and MAS-R assessment is under 12 months old with no critical or high finding past its EO1.6 SLA (72 hours, 7, 30 and 90 days); the copy linter fails any certification claim without an issued certificate (CYB paras 121–126; RA4).
- [ ] Every screen in the `Menu and screens` subsections of Part 7H (RA1–RA4) exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
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

Release controls (Part 7H RA4.2–RA4.4; gates built in Phase 16c, applied here): production builds only from protected tags with build number, commit, SBOM and permission manifest in the release record; the store-declaration gate comparing the merged manifest, Info.plist, privacy manifest, Data safety form, Financial features declaration and privacy labels with the approved versions; the partner-list check against the DLA register and each RE's CIMS confirmation; staged rollout with automatic halt below 99.5% crash-free sessions, on Play's ANR threshold or on a P1 incident; OTA rejection of any change to permissions, data collection, consent, disclosures, payments or security controls; hardware-key MFA, least privilege and a two-person rule on Play Console, App Store Connect and signing keys; an independent assessment of the release candidate against OWASP MASVS v2.1.0 under the MAS-L2 and MAS-R testing profiles using MASTG test cases, with findings tracked under the Finbyx EO1.6 platform SLAs (critical 72 hours, high 7 days, medium 30 days, low 90 days); no certification claim in any listing (RA4.4 copy linter).

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

- **Outcome:** E2E, independent VAPT and MASVS assessment, DR and incident drills, RE onboarding sign-off through the Phase 3c deal gates, controlled Android and web go-live
- **Depends on:** 0–17, including 3c, 11b, 14b and 16c (12b and 16b only where a pilot RE attaches them)
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
   - microfinance: household-income test and 50% cap (CF paras 51–57); loan card and no prepayment charge (RBC paras 78–81); this is the individual-loan template, and its KFS, loan-card and household-income components are reused by the JLG and SHG journeys, CGT and GRT, centre meetings, group collection records and MFIN Guardrails 2.0 display of Phase 18c (Part 7E MG2–MG4);
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

### Phase 18c — Member and group lending: co-operative societies and microfinance

- **Outcome:** Part 7B UP4 and Part 7E MG1–MG4: non-RE society track; member journeys with no deposit features; JLG and SHG journeys; field app with assisted mode, offline capture and group collection records
- **Depends on:** P, 3c, 12b (UR4 cash on delinquent loans only), 14b, 18b; Finbyx Phase 17c or the lender's system for member and group events; society member APIs in Integration Spec v1.1
- **Branch:** `feat/member-group-lending`
- **Suggested sub-modules (one session each):** UP4 non-RE society track and eligibility gate; MG1 member verification, admission, sureties and member loans; MG2 JLG journeys, guardrails, CGT and GRT, centre meetings; MG3 SHG linkage and book-keeping view; MG4 field app, assisted mode, offline sync and receipts; State rule packs (MSCS and Maharashtra first); Menus, screens and settings (Parts 7B (UP4) and 7E).

**Paste into Claude Code:**

```text
Phase 18c — Member and group lending: co-operative societies and microfinance. Governing brief: docs/00-master-prompt.md (Part 12, Phase 18c; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) MSCS Act ss.25(4), 26, 39(3), 66(1), 67, 84 and 85A and the CRCS norms of 22 Jan 2024; Maharashtra MCS Act ss.24, 48, 49, 91, 101 and 144-5A; Tamil Nadu Act 40 of 2025 s.20 commencement; Karnataka Act 15 of 2025 s.1(3) and its platform limb [VERIFY all]; (ii) whether a credit society can be a CIC member (CICRA) [VERIFY]; (iii) the app-store position for non-RE lenders [VERIFY]: until confirmed, society loans run on web, PWA and assisted channels only; (iv) MFIN Guardrails 2.0 (Directive 14, 25 Nov 2024) still current, DAY-NRLM SHG and grading norms, and NABARD JLG norms [VERIFY]; (v) Integration Spec v1.1: `GET /v1/societies/{id}/members/{ref}`, `POST /v1/societies/{id}/membership-applications`, `lender_type` (RE or NON_RE_SOCIETY) on `ApplicationSubmitted`, and the member and group events produced by the lender's system (Finbyx Phase 17c or another LOS/LMS); (vi) for each pilot RE, whether its legal opinion permits its own staff to collect regular instalments in cash on DLA-sourced loans (CF para 10(2), 10(5)); default is a per-member UPI QR. Then, on branch `feat/member-group-lending`, build Part 7B UP4 and Part 7E MG1–MG4:

- non-negotiables: no deposit journey, listing, rate, solicitation or display for any lender or member class (MSCS s.67; MH MCS Act s.144-5A; BUDS Act First Schedule items 4(i) and 8); Udofin never holds cash or funds; no borrower-paid Udofin fee (CF para 10(4), mirrored by contract for societies); joint liability as voluntary peer support only; no co-lending, direct assignment or split loans between a society or co-operative bank and an NBFC (TDCR paras 12(4), 97); the lender decides membership, sureties, group recognition, GRT, sanction and posting (OUT para 15; KYC para 13);
- UP4: the ten-point eligibility gate including the name check against 'bank', 'banker', 'banking' and transliterations (BR Act s.7) and the no-deposits-from-non-voting-members confirmation; tenant class NON_RE_COOP with its own RLS; the PILOT gate with registration verification and counsel's opinion in place of CIMS; packs for the society, its auditor and the Registrar;
- MG1: the separate 'Your co-operative society' space outside the CF para 7 offer view, with the fixed lender card ('not regulated by the Reserve Bank of India'; 'not insured by DICGC'); member verification by API, never a bulk register download; the admission journey with the MSCS 4-month-plus-15-day deemed-refusal timer; share money and repayments only to the society's account; surety consent on the surety's own device; the society loan fact sheet with APR; State rule packs (MSCS and Maharashtra first); statutory dispute forums with the Equator gate (conciliation only, never private arbitration); the co-operative grievance route, never RBI;
- MG2 and MG3: group states with `GroupFormed` as the recognition trigger; household questionnaire and the indicative 50% ratio labelled '[RE name] decides' (CF paras 51–57); MFIN guardrails surfaced from the RE's bureau result; CGT and GRT scheduling with GRT by RE staff only; one KFS and loan card per member (RBC paras 29, 78–81); centre meetings as the designated place (RBC para 90); no group-dues button; contact window 09:00–18:00 until 31 Dec 2026, then the RBC Third Amendment rule pack (RBI/2026-27/230) from 1 Jan 2027 [VERIFY]; SHG linkage, CIR para 13 member tables and the SHG book-keeping view with two-office-bearer maker-checker;
- MG4: the field app target (`apps/field`) for group lending, extended for other assisted journeys in Phase 20: managed devices, the assisted-mode limits (the assistant never sees an OTP, consents, accepts a KFS or signs), offline-first capture with an encrypted 72-hour store and signed, hash-chained sync, low-literacy consent with no biometric template (CF para 14(3)), hash-chained receipts naming the lender, the cash reconciliation view and the field-event checklist; Udofin staff collect cash only as appointed recovery agent on delinquent loans (CF para 10(5); Part 7A UR4);
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Parts 7B (UP4) and 7E (MG1–MG4), including the separate 'Your society' space and the field-app menus on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed;

Tests and acceptance evidence:

- every UP4 and MG1–MG4 acceptance test in Parts 7B and 7E;
- no deposit API, screen or template exists for a NON_RE_COOP tenant (route test) and the template linter rejects 'FD', 'RD' and 'deposit';
- a society–NBFC co-lending configuration fails with the TDCR reference;
- a non-member, a non-borrowing nominal member and a defaulter reach no loan screen;
- a member above ₹3,00,000 household income never sees a microfinance KFS; a GRT outcome cannot be recorded by a Udofin role;
- contact at 08:59 or 18:01 on a microfinance loan is denied; a Tamil Nadu field visit without the s.20 checklist cannot be saved;
- receipts are gap-free per device and sync exactly once; a meeting cannot close with an unsynced receipt;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the UP4 eligibility checklist, the member and group state machines, the society and microfinance rule-pack fields, the field-app offline and receipt design, and the member-space, field-app and lender-portal menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-18c-member-group-lending.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/member-group-lending in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No deposit API, screen, template, rate or message exists for any society tenant or member class, and the template linter rejects deposit vocabulary (MSCS s.67; MH MCS Act s.144-5A; BUDS Act First Schedule items 4(i), 8).
- [ ] A society onboarding fails on any name containing 'bank', 'banker' or 'banking' (BR Act s.7), and any co-lending, direct-assignment, participation or split-loan configuration between a society or co-operative bank and an NBFC fails with the TDCR reference (TDCR paras 12(4), 97).
- [ ] Society products appear only in the separate member space with the fixed lender card, never in the CF para 7 offer view, never on the store apps while the non-RE store position is unconfirmed, and the RBI Ombudsman route never shows for a society loan [VERIFY: store policy].
- [ ] Each microfinance member gets an individual RE KFS and loan card; household income above ₹3,00,000 routes to a non-microfinance product; a GRT outcome cannot be recorded by a Udofin role; there is no group-dues button (CF paras 51–57; RBC paras 29, 78–81, 88, 90).
- [ ] Microfinance and low-income member contact is denied outside 09:00–18:00 until 31 Dec 2026 and follows the Third Amendment pack (RBI/2026-27/230) from 1 Jan 2027; a Tamil Nadu field event without the s.20 checklist cannot be saved (RBC para 91(2); TN Act 40 of 2025) [VERIFY].
- [ ] Udofin holds no cash or funds in any table; Udofin staff can issue a cash receipt only on a delinquent loan under a UR4 appointment; with no RE cash opinion recorded the field app offers only UPI QR; receipts are gap-free, hash-chained and sync exactly once (CF para 10(2), 10(5)).
- [ ] Every screen in the `Menu and screens` subsections of Parts 7B (UP4) and 7E exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
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

- U22 field and assisted-onboarding app (separate Expo target, MDM distribution) only for REs that appoint Udofin for assisted onboarding or recovery; digital KYC under KYC para 24 by the RE's process; extend the `apps/field` target created in Phase 18c and apply the Part 7E MG4 assisted-mode rules to every assisted journey: the assistant never sees or enters an OTP, gives consent, accepts a KFS, signs, chooses a lender or changes the borrower's bank or contact details; consent, KFS acceptance and eSign complete on the borrower's own device; offline-first capture with an encrypted local store purged within 72 hours and signed, hash-chained sync; hash-chained receipts that name the lender, never Udofin; no cash collected by Udofin staff except as appointed recovery agent on delinquent loans (CF para 10(5); Part 7A UR4); `assisted_session` evidence on every session;
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

### Phase 20b — Financial wellness add-ons and plans and billing

- **Outcome:** Part 7D FW1–FW4 behind the G1–G5 gate; Part 7G RV1–RV4: revenue catalogue mirror and legality gate, lender and borrower billing pages, Razorpay for Udofin revenue, advertising rules
- **Depends on:** P, 3c, 11b, 14b, 16c; owner decision and legal opinion (FW4 G1–G2) before any wellness or borrower-plan code; Operations Hub O6 for RE invoicing only (borrower plans run on Udofin's own billing)
- **Branch:** `feat/wellness-plans-billing`
- **Suggested sub-modules (one session each):** FW4 gate check, separate store, grants and usage bans; FW1 credit report tracking and FW2 simulator; FW3 expense tracker and budget planner; RV1 catalogue mirror, deny list and legality gate; usage meters; RV2 lender and borrower billing pages; RV3 Razorpay, webhooks, GST invoices and dunning; RV4 advertising policy engine (S10 in DRAFT); Menus, screens and settings (Parts 7D and 7G).

**Paste into Claude Code:**

```text
Phase 20b — Financial wellness add-ons and plans and billing. Governing brief: docs/00-master-prompt.md (Part 12, Phase 20b; Part 8A prevails on regulatory points).

Gate first. Read `docs/decisions/` and the Part 7D FW4 `addon_legality_decision` records: G1 the owner decision to offer the money tools and through which entity or brand; G2 the written legal opinion on CF paras 10(4) and 14(1), CIC partner terms, DPDP, consumer-protection and e-commerce rules; G3 the signed CIC consumer-partner agreement; G4 the separate owner decision to charge, with the G2 pricing addendum; G5 a review date that has not lapsed. If G1 or G2 is absent, stop and tell me: build no Part 7D tool, no borrower plan page and no B2C checkout. I may then authorise the RE-side scope only (RV1 catalogue mirror and legality gate, RV2.2 lender billing pages, usage meters, RV4 policy engine with S10 in DRAFT). If G3 is absent, FW1 and FW2 run only against a CIC sandbox mock; if G4 is absent, S09 stays LEGAL_REVIEW and no paid plan exists. Also verify: the CIC Regulations reg 9 text and each CIC's partner terms [VERIFY]; the E-mandate Directions 2026 (RBI/DPSS/2026-27/396) paras 4(b), 6(a)–(c), 8(a) and 10(a); PCI DSS v4.0.1 SAQ A eligibility [VERIFY]; the CCPA Dark Patterns Guidelines 2023 Annexure 1 list [VERIFY]; the Integration Spec v1.1 billing domain (6.27): Udofin produces only `UsageRecorded` (`meter_kind` USAGE for RE meters, REVENUE_AGGREGATE for B2C plan revenue, no subscriber key) and consumes `PlanChanged`, the signed `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed` and `SubscriptionCancelled` for RE fees, while B2C billing events stay Udofin-internal; and Operations Hub phase O6 for RE invoicing only. Then, on branch `feat/wellness-plans-billing`, build behind `addons.wellness` (off in production until FW-C13 passes):

- FW4 separation: the `wellness` store in its own cluster or schema with its own KMS key, service accounts, backups and retention jobs; stand-alone DPDP notices and consents, every choice default No; the six usage bans hard-coded; no event with a wellness data class (FW-C15); a CI test enumerating database grants for U6, U7, U8, U13, U16, U19, U20, U21, U24 and every RE-facing API (FW-C14); the UI slot allow-list (FW-C17); the quarterly separation audit;
- FW1–FW3: credit report and score tracking as the consumer's agent under a CIC partner programme (never an RE report; CIR para 6), per-CIC display with free annual report links on every screen; the educational simulator with direction and band only and the locked label; the expense tracker fed by manual entry, statement upload through the system picker and CSV only, with SMS, notification-listener, accessibility-service and storage permissions blocked (CF para 13(1)) and no Account Aggregator access in Udofin's name (AA para 8(12));
- RV1: the catalogue mirror of OH8 with S01–S13, the hard-coded deny list and the legality gate; Udofin refuses any entitlement whose stream is not ACTIVE in its own mirror; meters as monthly aggregated `UsageRecorded` statements only, never loan, borrower, member or user IDs; deal switches sent to OH8 and applied only on a verified `EntitlementChanged`;
- RV2 and RV3: lender billing pages with the fixed CF para 10(4) statement; borrower plan pages only while S09 is ACTIVE, using 'plan' (never 'membership'), both fixed statements, one-tap cancel, no auto-converting trial; Udofin's own Razorpay account with hosted checkout (SAQ A), credential purpose tags, HMAC webhook verification, event-ID deduplication and status precedence, mandate cap equal to plan price, GST invoices and credit notes, and B2C dunning that never creates a debt; plan changes with the RV2.5 proration preview, consent or maker-checker, mandate replacement before an upgrade above the cap, and roll-back on failure; RE non-payment never cuts read access or export and ends only in a termination notice leading into the UP5 exit;
- RV4: the surface matrix (never in any loan, offer, KFS, payment, overdue, grievance or credit-report screen), labels, contextual targeting by default, no third-party ad SDK, advertiser verification; S10 stays DRAFT until my advertising-policy decision;
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Parts 7D (FW1–FW4) and 7G (RV1–RV4), including `Account › Plans and billing`, the lender-portal `Billing and plan` menu and the operations-portal `Finance` and `Marketing › Advertising` menus on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed.

Tests and acceptance evidence:

- with G2 missing, enabling `addons.wellness` in production fails and logs the reason;
- every FW1–FW4 and RV1–RV4 acceptance test in Parts 7D and 7G;
- a subscriber and a non-subscriber with identical requests receive identical offer sets and order;
- a subscription payment cannot use an RE credential and a repayment cannot use the `UDOFIN_REVENUE` credential;
- no card number appears in any log, database or crash report (CI PAN-pattern scan);
- no plan, money-tools or ad element renders on any loan route (route scan);
- a consumer upgrade previews and charges the prorated amount once, and a failed mandate authorisation leaves the old plan in force;
- the Operations Hub sandbox receives only `UsageRecorded` statements from Udofin, and a seeded subscriber or borrower identifier is rejected;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the gate status table, the wellness store and grant design, the revenue-stream catalogue with gate states, the billing, proration and webhook design, and the `Account › Money tools`, `Account › Plans and billing`, lender billing and operations-portal menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-20b-wellness-plans-billing.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/wellness-plans-billing in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] With FW4 G1 (owner decision) or G2 (legal opinion on CF paras 10(4) and 14(1)) missing, no Part 7D tool, borrower plan page or B2C checkout exists, and enabling `addons.wellness` in production fails and logs the reason; a lapsed G5 review switches the flag off; no paid plan exists without G4 (FW-C13).
- [ ] No non-wellness database role (U6, U7, U8, U13, U16, U19, U20, U21, U24 or any RE-facing API) has a grant on the wellness store, no event carries a wellness data class, and a subscriber and a non-subscriber receive identical offer sets and order (CF para 7(4); FW-C14, FW-C15).
- [ ] FW1 pulls only with Udofin's consumer-partner credentials and a live consent, never an RE's bureau access; FW3 adds no SMS, notification-listener, accessibility-service or storage permission and has no Account Aggregator access in Udofin's name (CIR para 6; CF para 13(1); AA para 8(12)).
- [ ] The deny list rejects every loan-linked borrower charge in OH and in Udofin; S09 cannot become ACTIVE without owner-decision and legal-opinion references; 'membership' is never used for a paid plan; RE non-payment never cuts read access or export and ends only in a termination notice leading into the UP5 exit (CF para 10(4)).
- [ ] Subscription money uses only the `UDOFIN_REVENUE` Razorpay credential with hosted checkout (PCI DSS v4.0.1 SAQ A), verified HMAC webhooks applied once with status precedence, a mandate cap equal to the plan price, no mandate charge (EMD para 10(a)), a GST invoice per charge and a credit note per refund; plan changes follow the RV2.5 proration and roll back on failure; B2C billing events stay Udofin-internal and the Hub receives only monthly `UsageRecorded` statements (`meter_kind` USAGE or REVENUE_AGGREGATE, no subscriber key).
- [ ] A route scan finds no plan, money-tools or ad element on any loan, offer, KFS, payment, overdue, grievance or credit-report screen, and S10 advertising stays DRAFT until the owner's advertising-policy decision (CF para 7(4); RV4.1).
- [ ] Every screen in the `Menu and screens` subsections of Parts 7D and 7G exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 20c — Extensible products and insurance distribution

- **Outcome:** Part 7F XP1–XP4: product plug-in registry with licence gating and kill-switch; insurance quote, buy, pay, claim support and complaints; feasibility-gated future products; cross-sell consent and sales-practice controls
- **Depends on:** P, 14b, 16c, 20b; IRDAI licence model decided and registration or legal note recorded before any insurance code
- **Branch:** `feat/product-framework-insurance`
- **Suggested sub-modules (one session each):** Licence-model gate check; XP1 product registry, licence lifecycle and kill-switch; XP1 partner adapters and certification suite; XP2 insurance journey, documents and claim support; XP2 complaints route and seller tagging; XP3 feasibility registry and XP4 sales-practice controls and UI audit; Menus, screens and settings (Part 7F).

**Paste into Claude Code:**

```text
Phase 20c — Extensible products and insurance distribution. Governing brief: docs/00-master-prompt.md (Part 12, Phase 20c; Part 8A prevails on regulatory points).

Gate first. Read `docs/decisions/` for the IRDAI licence-model decision (Part 7F XP2.1, Appendix B): model A (Udofin composite Corporate Agent) or B (Insurance Web Aggregator) needs Udofin's own IRDAI registration certificate recorded with number, permitted lines, validity, principal officer and tie-up list; model C (unpaid technology provider to an RE that is a Corporate Agent) needs the RE's registration and counsel's note confirming no solicitation or remuneration by Udofin [VERIFY: Insurance Act ss.40 and 42D(8) after the 2025 amendment]; model D is display in the RE's KFS only. If no model is recorded, or the required registration or note is missing, stop and tell me: build no insurance screen, route, adapter or API, and keep every `xp.insurance.*` module LICENCE_PENDING. I may then authorise the XP1 framework and the XP3 registry records only. Also verify: the IRDAI intermediary amendment of 30 Jul 2026, including the fresh-certificate deadline of 31 Jan 2027 and seller tagging from 1 Jan 2027 [VERIFY: notification text]; the RBC Second Amendment Directions (15 Jun 2026, effective 1 Jan 2027) paras 101G, 101I, 101M, 101Q, 101V, 101W, 101X and 101Y–Z for NBFCs [VERIFY: final numbering]; the IRDAI policyholder-protection regulations 2024 free-look periods, the Insurance Ombudsman Rules, 2017 and the E-mandate Directions 2026 paras 6 and 8(b) [VERIFY]; and that the insurance events (`InsuranceQuoteRequested`, `PolicyIssued`, `ClaimAssistanceRequested`) flow Udofin ↔ insurer only under separate consent. Then, on branch `feat/product-framework-insurance`, build Part 7F:

- XP1: the product-type registry as `module.yaml` with the `product` block; the regulator map; the lifecycle from PROPOSED to RETIRED; ENABLED only with a valid licence held by the named holder for that line, an active partner agreement within the tie-up limit (at most 9 insurers per line for a Corporate Agent), compliance and legal sign-off, complete disclosures and summary sheet in every active language, an ACTIVE RV1 stream and a passed UI audit; the nightly licence job; a 60-second kill-switch; new modules only by store release, never OTA; the separate `product_vault`; partner adapters with a certification suite and India processing by contract;
- XP2: insurance in its own area under Account (`Account › Protect › Quotes`, `My policies`, `Claims help`, `Complaints`; never a bottom tab: the app keeps Home, Loans, Pay, Help and Account) with the XP2.3 journey state table (needs check with explain-why lines, separate consent before the insurer's proposal, payment only on the insurer's gateway, the 48-hour issuance watch, free-look clock from the policy document), never in the loan chooser, offer view, KFS, signing, mandate, payment, loan dashboard, recovery or grievance screens (CF para 7(4)); no bundling: no loan conditional on, priced against or faster because of insurance (RBC Second Amendment para 101V); no premium financed from a loan (101W); no prompt in any cooling-off period or within 30 days of a microfinance disbursal (MFIN Guardrails 2.0; RBC para 80); quotes with equal weight and no default; the insurer's proposal form; premium paid directly to the insurer; seller tagging checked on issue; free-look reminders; the 30-day feedback contact; claim-support intake and tracking where the insurer decides; the insurance complaint route (insurer GRO, Bima Bharosa, Insurance Ombudsman), never the RBI route unless a model D loan complaint;
- XP3: candidate products only as PROPOSED records with no route, adapter or screen until a feasibility note is approved; co-operative society deposits and digital gold are never valid;
- XP4: product-specific consents, default No and kept at least one year after the contract (101G, 101I, 101Q); one-tap withdrawal (101M); promotional contact only with consent, 140-series numbers and within the window, enforced by the Phase 3b contact-policy engine until the Phase 20d routing engine is live (no outbound voice for non-loan products before then); the mis-selling review workflow; no cross-sell to overdue, hardship, grievance or bereavement cases; the dark-pattern UI audit before ENABLED; mis-selling reviews with refunds through the insurer;
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7F (XP1–XP4), including `Account › Protect` and the operations-portal `Products`, `Insurance` and `Compliance › Sales practice` menus on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed.

Tests and acceptance evidence:

- with no approved licence model, no insurance screen, route or API is reachable;
- every XP1–XP4 acceptance test in Part 7F;
- a module with an expired licence, a 10th insurer on one line or no RV1 stream cannot reach ENABLED; the kill-switch disables it on app and web within 60 seconds;
- an automated UI scan finds no insurance component on any loan route;
- a premium can be initiated only to the insurer's gateway; a claim ticket cannot be set approved or rejected by any Udofin role;
- from 1 Jan 2027 an issued policy without the seller's name and functional ID raises a compliance issue within one hour;
- an expired quote cannot be submitted, and a paid journey without `PolicyIssued` after 48 hours opens an insurer task;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the licence-model record, the registry manifest schema, the insurance journey state table, the UI-audit checklist, and the `Account › Protect` and operations-portal menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-20c-product-framework-insurance.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/product-framework-insurance in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] With no IRDAI licence model recorded, or without Udofin's own registration (models A or B) or the RE registration and no-solicitation legal note (model C), no insurance screen, route, adapter or API is reachable and every `xp.insurance.*` module stays LICENCE_PENDING [VERIFY: Insurance Act ss.40, 42D(8)].
- [ ] A module cannot reach ENABLED with an expired or soon-expiring licence, a 10th insurer on one line under a Corporate Agent licence, no active partner agreement, no compliance and legal sign-off, no RV1 stream or no UI audit; the kill-switch disables it on app and web within 60 seconds.
- [ ] An automated UI scan finds no insurance component on any loan chooser, offer, KFS, signing, mandate, payment, loan dashboard, recovery or grievance route; no loan is conditional on or priced against insurance and no premium is loan-funded (CF para 7(4); RBC Second Amendment paras 101V, 101W, effective 1 Jan 2027) [VERIFY: final numbering].
- [ ] Every non-loan consent is product-specific, separate and default No with one-tap withdrawal; no cross-sell appears within 30 days of a microfinance disbursal, during a cooling-off period or to overdue, hardship or bereavement cases; promotional contact passes the Phase 3b contact-policy engine (no outbound voice for non-loan products until Phase 20d) (RBC Second Amendment paras 101G, 101I, 101M, 101Q; RBC para 80; MFIN Guardrails 2.0).
- [ ] The insurance journey follows the XP2.3 state table: an expired quote cannot be submitted, proposal data is shared only after the separate insurer consent, and a paid journey without `PolicyIssued` after 48 hours opens an insurer task.
- [ ] Premiums go only to the insurer's gateway; no Udofin role can set a claim approved or rejected; from 1 Jan 2027 an issued policy without the seller's name and functional ID raises a compliance issue within one hour; insurance complaints show the insurer, Bima Bharosa and Insurance Ombudsman route, never the RBI route except for a model D loan complaint [VERIFY: IRDAI amendment of 30 Jul 2026].
- [ ] Every screen in the `Menu and screens` subsections of Part 7F exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 20d — Voice, AI contact-centre and Jio adapters

- **Outcome:** Part 7H RA5: provider-neutral messaging, voice, speech, LLM and conversation ports; TRAI number-series and calling-window routing; AI disclosure, handover and recording rules; Indian-language acceptance; Jio adapter after contract
- **Depends on:** P, 3b, 12b, 14b, 16c, 20
- **Branch:** `feat/voice-ai-contact-centre`
- **Suggested sub-modules (one session each):** Provider-neutral ports, mocks and provider evaluation (Jio and alternatives); Routing engine: purpose, number series, consent, window and frequency; AI contact-centre rules and conversation test suite; Recording, retention and legal hold; Indian-language speech acceptance; Menus, screens and settings (Part 7H (RA5)).

**Paste into Claude Code:**

```text
Phase 20d — Voice, AI contact-centre and Jio adapters. Governing brief: docs/00-master-prompt.md (Part 12, Phase 20d; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the TRAI series: the Direction of 19 Nov 2025 on 1600-series numbers for RBI-regulated entities (NBFCs above ₹5,000 crore from 1 Feb 2026; other NBFCs and co-operative banks from 1 Mar 2026), the clarification of 10 Jul 2026, the 1601 sub-series, and whether an LSP may hold 1600-series numbers or originate calls on an RE's number [VERIFY]; the TCCCPR 2018 as amended on 12 Feb 2025 (140-series for promotional calls, consent categories, 90 days before re-seeking consent after an opt-out, advance notice of robo-calls and auto-diallers under reg 4) [VERIFY]; (ii) the RBC calling rules: para 100 (08:00–19:00), para 91(2) (microfinance 09:00–18:00 until 31 Dec 2026), the Third Amendment pack from 1 Jan 2027 (paras 100P, 100Y(4)) and the RBC Second Amendment draft paras 101L and 101O [VERIFY: official texts]; (iii) the JioCX (Jio Things Ltd) API documentation, DPA, India residency, DLT and 1600 or 140 support, AI voice roadmap and rates, and the owner's contract decision (Appendix B) [VERIFY]; (iv) Bhashini and Sarvam AI terms and residency [VERIFY]. Udofin's own outbound service calls stay disabled until 1600-series eligibility is confirmed. Then, on branch `feat/voice-ai-contact-centre`, build Part 7H RA5 on U16, U20 and Part 7A UR4:

- adapters: `NotificationProvider` and `LlmProvider` (existing, Part 9.1), `VoiceProvider`, `SpeechProvider` and `ConversationAgent` as provider-neutral ports with a mock and one certified implementation; a provider is enabled only with an India-residency attestation for recordings, transcripts and inference, a DPA and sub-processor list, DLT and series support, and zero retention and no training on Udofin data (CF para 14(4)); Jio is one implementation behind the ports, built only after the contract and documents above; Exotel, Ozonetel, Knowlarity and Gupshup are evaluated behind the same ports [VERIFY];
- routing engine: every outbound communication computes `purpose`, `principal_entity`, `number_series`, `consent_check`, `time_window`, `frequency_cap`, `language` and `auto_dialler`; RE service, transactional and recovery calls only from the RE's 1600-series numbers through the RE's trunk or an RE-authorised provider; Udofin promotional calls only from 140-series numbers through a registered telemarketer with promotional consent and DND scrubbing; never an ordinary 10-digit number for telemarketing or RE service calls; denials logged with the rule; a call from an unregistered number is an incident;
- AI contact-centre rules: disclosure first in the borrower's language, not configurable off; human handover at any turn under the RA5.5 workflow (triggers, warm transfer with a context summary, service level, callback ticket inside the permitted window when no agent is free, never a silent end); no threats, misstatement or third-party contact (RBC paras 91, 100); no settlement, waiver, credit, claim or complaint decision and figures only from RE-issued offers; scripts and prompts approved by the RE's compliance team or Udofin compliance, with versions logged; model, prompt version, transcript and outcome stored in India; QA sampling feeding KRI R15;
- recording: announcement and DPDP notice link, repeated by the human after a transfer; for a service-call objection, unrecorded mode or a written channel; recovery calls always recorded, with a written channel offered to an objecting borrower; recovery recordings kept at least 6 months and until disposal if sub judice (pack B para 100P from 1 Jan 2027) with a Udofin default of 12 months; an unrecorded written or callback channel for objecting borrowers where the RE's policy allows; restricted RE-archive folder only;
- Indian languages: per-language acceptance tests by native reviewers before go-live; regulatory text only as text-to-speech of the RE-approved translation, never generated by an LLM;
- lifecycles: provider, number and script lifecycles of RA5.7;
- menus, screens and settings: build every entry of the `Menu and screens` and `Settings and options` subsections of Part 7H RA5, including the operations-portal `Communications` menu, the lender-portal `Settings › Communications` and the borrower's `Account › Settings › Contact preferences` on the channel and workspace named there (navigation map in Appendix G): list, detail, wizard, approval-queue and dashboard screens with their key and bulk actions, filters, exports, empty and error states and role visibility; each setting as a versioned, effective-dated `module_setting` record with its default, where a regulatory floor is enforced server-side and can never be relaxed.

Tests and acceptance evidence:

- every RA5 acceptance test in Part 7H;
- an RE service call without a configured RE 1600-series number is blocked; a Udofin promotional call without consent, from a non-140 number or outside 09:00–18:00 is blocked;
- recovery calls at 07:59 and 19:01 and microfinance calls at 08:59 and 18:01 are denied and logged; after 1 Jan 2027 the Third Amendment pack applies;
- a bot call without the opening disclosure fails the conversation suite; a request for a settlement figure not in an RE offer is declined with a human handover;
- a provider without India residency cannot be enabled for recordings, transcripts or inference; a language cannot go live without its acceptance record;
- 'talk to a person' with no agent free creates a callback inside the permitted window; a recovery-call recording objection never stops recording;
- every screen in the module's `Menu and screens` list renders only for the roles named there, and a setting change below its regulatory floor is refused server-side and logged.

Show me the port interfaces, the routing decision table with the number-series rules, the provider evaluation matrix including Jio, the handover workflow, the conversation test suite, and the communications menu and settings map for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Part 7 and Part 8A.16) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-20d-voice-ai-contact-centre.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/voice-ai-contact-centre in small commits; run unit, integration, tenant-isolation, security and (for app or web screens) device and accessibility tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every outbound communication passes the routing engine: RE service, transactional and recovery calls only from the RE's 1600-series numbers; Udofin promotional calls only from 140-series numbers with promotional consent and DND scrubbing; Udofin's own outbound service voice stays disabled until 1600-series eligibility is confirmed; denials are logged with the rule (TRAI Direction 19 Nov 2025; TCCCPR 2018 as amended 12 Feb 2025) [VERIFY].
- [ ] Until 31 Dec 2026 recovery calls are denied at 07:59 and 19:01 and microfinance and low-income member calls at 08:59 and 18:01; from 1 Jan 2027 the RBC Third Amendment rule-pack version (RBI/2026-27/230) decides without a code change; no persistent calling beyond the frequency cap (RBC paras 91(2), 100; pack B para 100Y(4)) [VERIFY].
- [ ] Every bot call or chat opens with a non-configurable AI disclosure in the borrower's language, hands over to a human on request or on an RA5.5 trigger with a context summary within the service level (or books a callback inside the permitted window, never ending silently), and never gives a settlement, waiver, credit, claim or complaint decision or any figure not in an RE-issued offer (RBC paras 91, 100; FREE-AI report).
- [ ] No voice, speech or LLM provider, including Jio, is enabled without an India-residency attestation for recordings, transcripts and inference, a DPA, zero retention and no training on Udofin data; Jio is integrated only after the owner's contract decision and API documentation (CF para 14(4)) [VERIFY: JioCX terms].
- [ ] Recordings are announced, encrypted, stored in India, kept at least 6 months for recovery calls (pack B para 100P from 1 Jan 2027) or the Udofin default of 12 months, purged at expiry unless on legal hold; no language goes live without its native-reviewer acceptance record, and regulatory text is only text-to-speech of RE-approved translations.
- [ ] Every screen in the `Menu and screens` subsections of Part 7H (RA5) exists on the named channel with its role visibility, empty and error states, and matches the Appendix G navigation map; every setting in `Settings and options` is a versioned, effective-dated record with its default, and a change below a regulatory floor is refused server-side and logged.
- [ ] The PR shows the test output; no borrower PII appears in logs or fixtures; the regulatory register and docs/status are updated.

### Phase 21 — Scale hardening and AWS migration

- **Outcome:** Scale tests, AWS ap-south-1 / ap-south-2, DR at scale
- **Depends on:** P, 16b, 18, 18b, 18c, 19, 20; 20b, 20c and 20d where built
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
| Phase 3c — Lender partnership onboarding and deal configurator |  |  |  |  |
| Phase 4 — Borrower identity and onboarding (app and web) |  |  |  |  |
| Phase 5 — KYC and verification adapters |  |  |  |  |
| Phase 6 — Credit data, affordability and eligibility |  |  |  |  |
| Phase 7 — Lender routing, offers, KFS and cooling-off |  |  |  |  |
| Phase 8 — Documents, eSign, eStamp and DMS |  |  |  |  |
| Phase 9 — Lender connectors and disbursement orchestration |  |  |  |  |
| Phase 10 — Repayments, mandates and reconciliation |  |  |  |  |
| Phase 11 — Loan mirror and borrower servicing |  |  |  |  |
| Phase 11b — Borrower downloads and tax documents |  |  |  |  |
| Phase 12 — Collections and recovery support |  |  |  |  |
| Phase 12b — Recovery support, notices and ADR access |  |  |  |  |
| Phase 13 — DLG management and lender disclosures |  |  |  |  |
| Phase 14 — Grievance, AI support and Equator |  |  |  |  |
| Phase 14b — Grievance escalation chain v2 |  |  |  |  |
| Phase 15 — Udofin finance, accounting and reporting |  |  |  |  |
| Phase 16 — Compliance, audit and security operations |  |  |  |  |
| Phase 16b — Ecosystem integration v2 |  |  |  |  |
| Phase 16c — Risk function, supervisory access, data portability and engineering assurance |  |  |  |  |
| Phase 17 — Mobile and web release engineering (Play Store, App Store, PWA) |  |  |  |  |
| Phase P — MVP hardening and pilot go-live |  |  |  |  |
| Phase 18 — Secured products (LAS, Home, LAP, Vehicle) |  |  |  |  |
| Phase 18b — Additional product templates |  |  |  |  |
| Phase 18c — Member and group lending: co-operative societies and microfinance |  |  |  |  |
| Phase 19 — Specialist products (feasibility-gated) |  |  |  |  |
| Phase 20 — Field app, analytics, AI and marketing expansion |  |  |  |  |
| Phase 20b — Financial wellness add-ons and plans and billing |  |  |  |  |
| Phase 20c — Extensible products and insurance distribution |  |  |  |  |
| Phase 20d — Voice, AI contact-centre and Jio adapters |  |  |  |  |
| Phase 21 — Scale hardening and AWS migration |  |  |  |  |

*End of runbook.*
