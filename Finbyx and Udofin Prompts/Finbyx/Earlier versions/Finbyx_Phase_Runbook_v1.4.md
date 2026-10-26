# FINBYX — Phase-wise Claude Code Runbook

**Companion to the Finbyx Master Build Prompt v1.4** · 19 October 2026 · ready-to-paste instructions for every build phase

---

## 1. How to use this runbook

1. **Before Session 1:** commit the master prompt as `docs/00-master-prompt.md`, the RBI PDFs to `docs/regulations/rbi/` and the Infrabyx Ecosystem Integration Specification to `docs/ecosystem/infrabyx-integration-spec.md`. You can also commit this runbook as `docs/01-phase-runbook.md`.
2. **One phase per session.** Start a fresh Claude Code session for each phase or sub-module, and paste only that phase's block.
3. **Each block is self-contained.** From Phase 1 onward it already includes (Phase 0 instead ends with the approval presentation of Part 13):
   - the Part 12 instruction;
   - the v1.3 regulatory additions from Part 8A.36.4;
   - the standard closing that makes Claude Code list the REQ-IDs, write the specification and stop for your approval before coding.
4. **Approve, then build.** Read the specification, reply "Approved" (or give changes), and let Claude Code build, test and open the pull request.
5. **Run the review gate** (the checklist under each phase) before merging. Use prompt U6 in Section 4 to have Claude Code run it for you.
6. **Large phases:** use the sub-module split shown for the phase. Paste the full block in the first session, which writes and gets approval for the whole-phase specification; in each later sub-module session paste prompt U1, which re-reads that approved specification.
7. **Order:** 0 → 1 → 2 → 3 → 3b → 4 → 5 → 6 → 7 → 8 → 8b → 8c → 9 → 10 → 11 → 12 → 12b → 13 → 14 → 15 → P → 16 → 16b → 17 → 17b → 18 → 19 → 20. Phases 12, 12b and 17b build the Recovery Suite and 16b the ecosystem integration hub. Build them all: whether a tenant uses the suite is decided at runtime by licence and feature flag (Part 7A.0). Do not start a phase until the phases it depends on are merged.

---

## 2. Standard closing (already included in every block)

```text
Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-<n>-<name>.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch <branch> in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

---

## 3. Phase instructions

### Phase 0 — Repository audit and architecture

- **Outcome:** Verified repo facts; audit of the current Finbyx product; competitor benchmark; architecture proposal; ADRs; Fineract adoption decision; regulatory register v1
- **Depends on:** nothing (first phase)
- **Branch:** `feat/repo-baseline`

**Paste into Claude Code:**

```text
Read docs/00-master-prompt.md and docs/ecosystem/infrabyx-integration-spec.md in full, then execute Part 13 (Phase 0 only).

In addition to the Phase 0 instruction in Part 12:
- confirm that the RBI PDFs are in docs/regulations/rbi/ and the Infrabyx Ecosystem Integration Specification is in docs/ecosystem/infrabyx-integration-spec.md (I committed them before this session);
- prepare docs/regulations/errata.md (from Appendix F) and docs/regulations/index.md (SHA-256 hash and "updated as on" date of each RBI file, Part 8A.0.1) for the baseline PR after approval.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- ADR on V-CIP hosting: tenant-exclusive owned/leased storage (cloud allowed), immediate transfer of recordings, vendor retains no data (KYC 27(1)(i)). Add the tenant's s.11A PML Act notification status (Aadhaar e-KYC authentication) to the Appendix B item 4 decision [KYC]
- ADR classifying Finbyx under OUT for each deployment model and each tenant layer (BL → CYB Ch III/IV; CYB 117 residual) (OUT 3(2), 5, 58). Standard MSA/DPA clause matrix against OUT 34, 74, 87–88 and 97(xvi). Add GOV, OUT and ORM to regulatory register v1, with ORM marked "guidance" [GOV / OUT / ORM]

Present everything for my approval before modifying the repository.
```

**Review gate (check before merging):**

- [ ] Every Part 8A requirement is in regulatory register v1 with its REQ-ID; the count per code matches Part 8A (8A.1–8A.35).
- [ ] Every [VERIFY] item is mapped to the phase that will verify it.
- [ ] The data-residency check covers every host and SaaS sub-processor; nothing outside India holds real data.
- [ ] ADRs exist for Fineract adoption, V-CIP hosting (KYC 27(1)(i)) and the outsourcing classification of Finbyx (OUT).
- [ ] You have answered the Appendix B decisions, or recorded a date for each.
- [ ] The Udofin/LSP contract outline uses the canonical names in docs/ecosystem/infrabyx-integration-spec.md, and any event not in it is logged as a proposal, not invented (Integration Spec Part 14.2).
- [ ] The baseline PR contains only CLAUDE.md, the ADRs, docs/, the registers and errata.md (Part 13); no application scaffolding.

### Phase 1 — Platform foundation

- **Outcome:** Monorepo, CI/CD, environments, auth abstraction, design system, observability
- **Depends on:** 0
- **Branch:** `feat/platform-foundation`

**Paste into Claude Code:**

```text
Phase 1 — Platform foundation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 1; Part 8A prevails on regulatory points).

On branch `feat/platform-foundation`, initialise the approved monorepo. Set up:

- pnpm + Turborepo, TypeScript strict, ESLint/Prettier;
- the `apps/web` (Next.js), `apps/api` (NestJS) and `apps/worker` skeletons;
- the `packages/` for contracts, domain-kernel (money, dates, IDs), ui (design tokens + shadcn), config and testing;
- Docker Compose for local Postgres, Temporal and Gotenberg;
- GitHub Actions CI (lint, typecheck, test, build, secret scan, dependency scan);
- `.env.example` files;
- an OpenTelemetry baseline, with PII scrubbing and India-resident error tracking per the ADR;
- Storybook.

Implement the domain-kernel `Money` and `Rate` types on decimal.js (precision ≥ 40, explicit rounding policies), with property-based tests. Build no business features yet. Open a PR with the test output.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-1-platform-foundation.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/platform-foundation in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] CI is green on the PR, including the secret scan and dependency scan.
- [ ] Money and Rate property-based tests pass; no float arithmetic anywhere.
- [ ] No business features were built.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 2 — Database, tenancy and security

- **Outcome:** Tenant/entity/branch model, RBAC/ABAC, enforced RLS, audit events, maker-checker framework, isolation tests
- **Depends on:** 1
- **Branch:** `feat/db-tenancy-security`

**Paste into Claude Code:**

```text
Phase 2 — Database, tenancy and security. Governing brief: docs/00-master-prompt.md (Part 12, Phase 2; Part 8A prevails on regulatory points).

Design and create the migrations for:

- tenants, legal_entities, branches (hierarchy), users, roles, permissions, role_permissions, user_scopes (entity/branch/product/amount limits);
- maker_checker_requests;
- audit_events (hash-chained);
- consent_records;
- idempotency_keys;
- outbox_events.

Implement:

- server-side authorisation (RBAC + ABAC);
- Postgres RLS on every tenant-scoped table, enforced:
  - the API connects as a non-owner role without BYPASSRLS;
  - every tenant table uses `ALTER TABLE … FORCE ROW LEVEL SECURITY`;
  - tenant, entity and branch context is set with `SET LOCAL` / `set_config(…, true)` inside every transaction, so it works with transaction pooling;
- the auth abstraction over Supabase Auth, with MFA for staff;
- the generic maker-checker framework.

Write tenant-isolation and privilege-escalation tests that try to read and write across tenants, entities and branches, and prove they fail. Include a test proving that a query run without tenant context returns zero rows. Report results.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Extended entity_regulatory_profile and group tables (Part 8A.25) [CAP / SBR / DIV / MISC]
- Tenant-controlled keys (BYOK/HYOK, KMS/HSM) (OUT 97(vii)(b)). Break-glass access workflow with tenant-visible logs (OUT 24, 70). Tenant-isolation test suite (OUT 70, 97(vii)(c)). MFA and role-conflict matrix (OUT 97(viii)) [GOV / OUT / ORM]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-2-db-tenancy-security.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/db-tenancy-security in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Cross-tenant, cross-entity and cross-branch read/write tests all fail as intended.
- [ ] A query without tenant context returns zero rows; the API role has no BYPASSRLS.
- [ ] The audit-event hash chain verifies end to end.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 3 — Masters, configuration and product factory

- **Outcome:** Org hierarchy, calendars, masters, product factory, charges, rule packs, workflow designer v1
- **Depends on:** 2
- **Branch:** `feat/masters-product-factory`

**Paste into Claude Code:**

```text
Phase 3 — Masters, configuration and product factory. Governing brief: docs/00-master-prompt.md (Part 12, Phase 3; Part 8A prevails on regulatory points).

Build:

- org hierarchy, holiday calendars and business-date management;
- masters (pincode, IFSC, purpose and sector codes, reason codes, NACH return codes as configurable data);
- the product factory implementing every Fineract-equivalent parameter in Part 4.2A, with validation guard-rails from the regulatory rule packs (Part 10.2 #24);
- the charges engine with GST profiles, including the penal-charge GST flag;
- effective-dated versioning and maker-checker for all configuration.

Produce the product specification template `docs/products/_template.md` and the first two product specs (Personal Loan, MSME Term Loan) for my approval.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- CRO vetting step in the product factory (GOV 23). ORM 47 heads in product approval. Service-provider and MFI declarations in templates (OUT 55–56) [GOV / OUT / ORM]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-3-masters-product-factory.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/masters-product-factory in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The product factory rejects any parameter that breaches a rule-pack guard-rail.
- [ ] Every configuration change is effective-dated and passes maker-checker.
- [ ] The Personal Loan and MSME Term Loan product specs are approved.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 3b — Communications foundation

- **Outcome:** M18 templates, DLT/WhatsApp/email channels, consent and preference store, contact-policy engine skeleton
- **Depends on:** 2
- **Branch:** `feat/communications`

**Paste into Claude Code:**

```text
Phase 3b — Communications foundation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 3b; Part 8A prevails on regulatory points).

Build the M18 foundation:

- multilingual, versioned template management with approval workflow and DLT template IDs;
- SMS (DLT), WhatsApp Business Cloud API and email adapters (mock + sandbox);
- consent, preference and DND store;
- the effective-dated contact-policy engine, with separate recovery and sales/marketing windows (Part 7, M8 and M18).

Later phases (KFS delivery, reminders, default intimation, collections) must use this module, not their own messaging code.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Language preference store; block dispatch when no approved vernacular template exists (RBC 10) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-3b-communications.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/communications in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] No other module sends messages directly; everything goes through M18.
- [ ] The contact-policy engine blocks a recovery contact outside the permitted window.
- [ ] SMS cannot be sent without a DLT template ID.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 4 — Ledger and accounting core

- **Outcome:** CoA, journal engine, posting rules (including Ind AS deferred-fee postings), period close, trial balance — before any loan money moves
- **Depends on:** 2
- **Branch:** `feat/ledger-core`
- **Suggested sub-modules (one session each):** chart of accounts and journal engine; posting rules (including Ind AS deferred fees); period close and trial balance.

**Paste into Claude Code:**

```text
Phase 4 — Ledger and accounting core. Governing brief: docs/00-master-prompt.md (Part 12, Phase 4; Part 8A prevails on regulatory points).

Before any loan money moves, build the double-entry ledger:

- chart of accounts with the NBFC Ind AS template;
- append-only journals with database-enforced balance;
- reversal-only corrections;
- value, business and system dates;
- period locks;
- materialised balances;
- trial balance;
- accounting rule mapping (Fineract mapping keys + India extensions);
- sub-ledger framework;
- reconciliation checks.

For Ind AS entities, the posting matrix must defer processing fees and directly attributable costs at disbursement (deferred-fee/cost accounts), so nothing has to be re-posted when EIR amortisation arrives. Write golden test cases for every posting rule, and property tests proving the ledger always balances. Show me the posting matrix for approval.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Capital-component tags in the chart of accounts (CAP 7–16) [CAP / SBR / DIV / MISC]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-4-ledger-core.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/ledger-core in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The trial balance balances after a randomised posting test.
- [ ] Corrections happen only by reversal; posted journals are immutable.
- [ ] A closed period rejects new postings.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 5 — Schedule and allocation engine

- **Outcome:** Fineract-equivalent schedules and allocation strategies, replay, Fineract oracle fixtures, golden cases
- **Depends on:** 3, 4
- **Branch:** `feat/schedule-engine`
- **Suggested sub-modules (one session each):** schedule generation (all interest methods); allocation strategies; replay and the Fineract oracle harness.

**Paste into Claude Code:**

```text
Phase 5 — Schedule and allocation engine. Governing brief: docs/00-master-prompt.md (Part 12, Phase 5; Part 8A prevails on regulatory points).

Implement the loan calculation engine as pure functions over an immutable loan event log. Cover:

- EMI and equal-principal;
- declining and flat;
- daily and period interest;
- day-count conventions;
- broken period;
- grace and moratorium;
- tranches;
- step-up/down and balloon;
- interest recalculation and all four prepayment outcomes;
- all allocation strategies, including the RBI-order rule set (Part 4.2B);
- back-dated replay with snapshots.

Run Fineract 1.15.0 (PostgreSQL 18, large runner) as a nightly or on-demand oracle job, not on every PR. Generate versioned golden fixtures (JSON) across a scenario matrix that uses the correct Fineract engine (CUMULATIVE or PROGRESSIVE) for each scenario. PR CI compares Finbyx output against these fixtures. Report paisa-level differences and classify each as a bug or an approved deviation.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Rupee-rounding policy at billing/posting (MISC 27) [CAP / SBR / DIV / MISC]
- Golden cases for each MSD para 7(1)–(5) scenario: cheque handover later than cheque date, EMI on a partially disbursed tranche, mid-month disbursal and repayment, advance EMI [MFI / IAF / SA / SR / MSD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-5-schedule-engine.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/schedule-engine in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Schedules and allocations match the Fineract 1.15.0 oracle on the golden cases.
- [ ] Your CA reviewer has signed off the golden accounting cases.
- [ ] Rupee rounding happens at billing/posting only (MISC 27; RBC 103).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 6 — Customer, KYC and consent

- **Outcome:** CIF, de-dupe, KYC adapters (mock → Surepass sandbox), consent ledger, AML screening
- **Depends on:** 2
- **Branch:** `feat/customer-kyc-consent`
- **Suggested sub-modules (one session each):** CIF and de-duplication; KYC adapters and CKYC; consent ledger; AML/sanctions screening and risk categorisation.

**Paste into Claude Code:**

```text
Phase 6 — Customer, KYC and consent. Governing brief: docs/00-master-prompt.md (Part 12, Phase 6; Part 8A prevails on regulatory points).

Build:

- the CIF with relationships;
- de-dupe;
- risk categorisation;
- the consent ledger with exact notice versions;
- KYC flows per Part 8A.21 (CKYC search/download/upload with 10/7-day clocks, Aadhaar mode selection by s.11A status, OKYC/DigiLocker, PAN/Form 60, V-CIP, OVD and deemed-OVD capture, BO thresholds, NFTF EDD, para 25 limits);
- sanctions and PEP screening;
- the periodic-updation scheduler.

Adapters: mock first, then a Surepass sandbox adapter behind `KycProvider`. Never store the full Aadhaar number unless the vault design approved in Phase 0 meets UIDAI Circular No. 14 of 2025. Prefer OKYC/DigiLocker flows that avoid storage. Load the KYC REQ-IDs from Part 8A.21 into the register.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-6-customer-kyc-consent.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/customer-kyc-consent in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] CKYC search/download/upload clocks work (10 days / 7 days) and UCIC is unique per individual.
- [ ] No full Aadhaar number is stored outside the vault design approved in Phase 0.
- [ ] Sanctions and PEP screening run at onboarding and on list updates.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 7 — Origination (LOS)

- **Outcome:** Leads, applications, bureau/AA, BRE, verifications, deviations/DoA, CAM, sanction, KFS
- **Depends on:** 3b, 5, 6
- **Branch:** `feat/origination`
- **Suggested sub-modules (one session each):** leads and applications; bureau/AA data pulls; BRE and deviations/DoA; CAM, sanction and KFS.

**Paste into Claude Code:**

```text
Phase 7 — Origination (LOS). Governing brief: docs/00-master-prompt.md (Part 12, Phase 7; Part 8A prevails on regulatory points).

Implement:

- leads, and DSA/connector management with payouts;
- dynamic application forms from product templates;
- bureau and AA adapters (mock + sandbox);
- the GoRules-based BRE with simulation;
- verification management (FI/PD/technical/legal/RCU) with vendor allocation;
- the deviation matrix and DoA routing;
- the CAM generator (template + AI-drafted narrative with citations, edited by a human, locked at sanction);
- sanction;
- the KFS/APR engine per RBC para 29 and Annex I, with the KFS validity period (≥ 3 working days, or ≥ 1 for tenor < 7 days). This is not a waiting period. Include the unique proposal number, the Part 2 disclosures and the APR golden test (₹20,000 / 24 months / 15% / ₹400 fees → 17.07%; RBC para 29(3)).

Model the application state machine explicitly. Include a full E2E test from lead to sanction for the two MVP products.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- KFS unique proposal number, acknowledgement, Annex I Part 2 disclosures and the APR golden test (₹20,000 / 24 months / 15% / ₹400 fees → 17.07%) (RBC 29); vernacular sanction letter (RBC 13); LWD/large-defaulter gate (WD 7, 19) [RBC / WD]
- rw_class, guarantee cover, cancellability flag and HQ-infrastructure data captured at sanction (CAP 18) [CAP / SBR / DIV / MISC]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-7-origination.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/origination in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The KFS APR golden test returns 17.07% (₹20,000 / 24 months / 15% / ₹400 fees; RBC 29(3)).
- [ ] New-to-credit applicants are never auto-rejected for lack of history (CIR 38(5)).
- [ ] Related-party, exposure-limit, LEI, fraud-debarment and wilful-defaulter gates block sanction where required.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 8 — Documentation, execution, DMS and disbursement

- **Outcome:** Templates, signing evidence, physical-execution path, OTC/PDD, mandate registration, payout, loan booking
- **Depends on:** 7
- **Branch:** `feat/docs-esign-disbursement`

**Paste into Claude Code:**

```text
Phase 8 — Documentation, execution, DMS and disbursement. Governing brief: docs/00-master-prompt.md (Part 12, Phase 8; Part 8A prevails on regulatory points).

Build:

- document templates and generation (Gotenberg);
- eSign, eStamp and NeSL DDE adapters that store verifiable signing evidence;
- the physical-execution path for instruments the IT Act First Schedule excludes (DP notes and other negotiable instruments except cheques, powers of attorney, immovable-property conveyances);
- the DMS with hashes, versions, retention and access logs;
- OTC/PDD tracking;
- mandate registration (eNACH/UPI AutoPay);
- the disbursement memo with pre-disbursement checks;
- penny-drop and payout adapters with duplicate-payment prevention;
- atomic loan booking with opening entries, including Ind AS deferred fees.

Interest starts from the actual disbursement date. Include cooling-off handling for digital loans.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-8-docs-esign-disbursement.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/docs-esign-disbursement in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Signing evidence is stored and linked to the sanctioned KFS version.
- [ ] Digital-loan disbursement goes directly to the borrower's bank account, with no pass-through or LSP pool account, except where CF para 10 permits.
- [ ] Loan booking posts to the ledger and the trial balance still balances.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 8b — Field app foundation

- **Outcome:** Expo app shell, offline sync, device binding, assisted KYC/document capture
- **Depends on:** 2, 6
- **Branch:** `feat/field-app`

**Paste into Claude Code:**

```text
Phase 8b — Field app foundation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 8b; Part 8A prevails on regulatory points).

Scaffold `apps/field` (Expo React Native + TypeScript). Build:

- offline-first storage and sync with conflict resolution;
- device binding and remote wipe;
- just-in-time permissions (camera and location only when needed; never contacts, SMS or call logs);
- assisted KYC and document capture, including the KYC para 24 digital-KYC flow (live photo with watermark, officer-mobile block, dual OTP; Part 8A.21);
- FI/PD report capture.

Plan distribution through managed Play Store/App Store or MDM, with a forced-update policy for incompatible versions.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-8b-field-app.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/field-app in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Offline sync resolves conflicts without data loss.
- [ ] Device binding works and a lost device can be revoked.
- [ ] The digital-KYC flow meets KYC para 24 (live photo with watermark, dual OTP, officer-mobile block).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 8c — Udofin / LSP inbound connector (minimal)

- **Outcome:** LSP contract v1, application intake, status callbacks, signing-evidence intake, disbursement and repayment events
- **Depends on:** 7, 8
- **Branch:** `feat/lsp-connector-v1`

**Paste into Claude Code:**

```text
Phase 8c — Udofin / LSP inbound connector (minimal). Governing brief: docs/00-master-prompt.md (Part 12, Phase 8c; Part 8A prevails on regulatory points).

Implement LSP contract v1 per Part 5 and the Ecosystem Integration Specification (Part 3 core and Parts 6.2–6.4, as sequenced in Integration Spec Part 15), using its canonical event names:

- OpenAPI/AsyncAPI;
- signed webhooks;
- idempotency;
- application intake with consent artefacts;
- status and decision callbacks;
- KFS and sanction publication;
- intake of signing evidence;
- disbursement and repayment events;
- daily reconciliation file.

Add Pact contract tests with Udofin. Prove that Finbyx keeps operating when Udofin is unavailable.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-8c-lsp-connector-v1.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/lsp-connector-v1 in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The LSP contract is versioned and every inbound event is idempotent.
- [ ] The LSP never receives or holds loan funds.
- [ ] Status callbacks and repayment events reconcile with Finbyx records.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 9 — Servicing (LMS) and COB

- **Outcome:** Accruals, EIR amortisation stub, repayments, prepayment/foreclosure, resets, restructuring, service requests, COB with classification
- **Depends on:** 5, 8
- **Branch:** `feat/servicing-cob`
- **Suggested sub-modules (one session each):** accruals and repayments; prepayment, foreclosure and resets; restructuring; service requests, closure and NOC; COB orchestrator and classification.

**Paste into Claude Code:**

```text
Phase 9 — Servicing (LMS) and COB. Governing brief: docs/00-master-prompt.md (Part 12, Phase 9; Part 8A prevails on regulatory points).

Build:

- the loan 360 view;
- daily accrual;
- an EIR amortisation stub driven by the Phase 4 rules;
- penal charges as charges;
- repayments with allocation;
- part-prepayment and foreclosure quotes with the prepayment-charge engine (RBC paras 33–34, 81);
- floating-rate resets with borrower options;
- restructuring and rescheduling with classification impact;
- top-up and balance transfer;
- service requests and certificates;
- closure, NOC, and the document-release SLA with compensation;
- write-off.

Build the COB orchestrator using the two-pass design in Part 4.2E:

- per-loan pass A;
- a cross-loan barrier for borrower-level SMA/NPA classification and upgrade;
- per-loan pass B for income recognition and derecognition, EIR and provisioning.

Add catch-up, inline COB, partitioned workers and the EOD exceptions dashboard. Load-test COB at 1 million loans.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Illustration I golden test and +1 DPD convention (IRACP 19); Part A/B restructuring workbench and monitoring/specified-period tests (RSA 53–62, 159, 189–194) [IRACP / RSA]
- Prepayment engine incl. RBC 34(3)–(9) and 81; penal rules RBC 30; reset elections and quarterly statement (RBC 31); account-transfer request (RBC 19); rounding (RBC 103); release clocks 30/60 days (RBC 35–40) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-9-servicing-cob.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/servicing-cob in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The IRACP Illustration I golden test passes (DPD = COB date − oldest unpaid due date + 1).
- [ ] Classification is borrower-wise across all the borrower's accounts; no income accrues on an account turning NPA.
- [ ] COB completes the 1 million-loan load test within the agreed window.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 10 — Payments and reconciliation

- **Outcome:** eNACH/UPI AutoPay presentation, bounces, virtual accounts, BBPS, payment-gateway links, three-way reconciliation
- **Depends on:** 9
- **Branch:** `feat/payments-recon`

**Paste into Claude Code:**

```text
Phase 10 — Payments and reconciliation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 10; Part 8A prevails on regulatory points).

Build:

- the mandate lifecycle;
- the presentation engine per sponsor bank, with cut-offs;
- re-presentation, and bounce processing with charges;
- UPI intent, QR and payment links;
- virtual accounts;
- the BBPS biller adapter;
- branch cash and cheque deposit tracking;
- three-way reconciliation with exception queues and suspense ageing.

A provider success response never finalises a payment without settlement confirmation. Add Stripe/PayPal adapters only for cross-border or SaaS billing, with an ADR.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- PDC capture block where NACH is available (MISC 23) [CAP / SBR / DIV / MISC]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-10-payments-recon.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/payments-recon in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Three-way reconciliation (bank, gateway/NACH, ledger) runs daily with aged breaks.
- [ ] Bounce charges follow the penal-charge rules and GST flag.
- [ ] Every receipt is allocated and posted the same day.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 11 — Collections

- **Outcome:** Strategies, allocation, telecalling, field collections, agencies, contact-policy engine, call recording
- **Depends on:** 3b, 8b, 9, 10
- **Branch:** `feat/collections`
- **Suggested sub-modules (one session each):** strategies and allocation; telecalling and contact engine; field collections and agencies.

**Paste into Claude Code:**

```text
Phase 11 — Collections. Governing brief: docs/00-master-prompt.md (Part 12, Phase 11; Part 8A prevails on regulatory points).

Verify the RBC Third Amendment Directions, 2026 text first. Then build:

- segmentation and bucket strategies triggered by COB DPD changes;
- rule-based allocation;
- the telecalling workspace with dispositions and PTP;
- field collections in the field app (offline, geo-tag, digital receipts, cash limits, same-day deposit);
- agency management with the IIBF certification register;
- the effective-dated contact-policy engine from Phase 3b (current RBC paras 89–100; paras 100A–100AB from 1 Jan 2027 under RBI/2026-27/230 of 6 Aug 2026 (confirmed; the official text is not in the supplied set, so re-check paragraph numbers when it is));
- mandatory call recording and retention (para 100P);
- pre-visit intimation (para 100L) and visit conditions (para 100Y(5));
- borrower default/DPD alerts sent with each CIC submission (CIR para 34(1)(i)), and recovery-agent particulars sent before first contact on digital loans (CF para 9(6)).

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Contact engine for current RBC paras 89–100 (microfinance window under 91(2); para 100 excludes microfinance); Third Amendment rules (RBI/2026-27/230, effective 1 Jan 2027; official text not in the supplied set) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-11-collections.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/collections in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Recovery-agent particulars reach the borrower before the first contact on digital loans (CF 9(6)).
- [ ] Contact windows and frequency limits are enforced by the engine, not by users.
- [ ] Calls are recorded and linked to the contact attempt.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 12 — Recovery Suite core (attachable)

- **Outcome:** Part 7A.0 attach/detach framework; R1 case and strategy engine with mechanism-selection and limitation engines; R2 pre-legal; R3 notices with dispatch and proof of service; R7 s.138 and s.25 PSS; R9 litigation tracker; R11 counsel and agencies; R12 recovery accounting; R14 registers and exports; R15 conduct controls; wilful defaulters; write-off
- **Depends on:** 4, 11
- **Branch:** `feat/recovery-suite-core`
- **Suggested sub-modules (one session each):** 7A.0 attach/detach framework and module registry; R1 case, mechanism-selection and limitation engines; R2 pre-legal and R3 notices with dispatch and proof of service; R7 cheque and mandate dishonour; R9 litigation tracker and R11 counsel and agencies; R12 recovery accounting, R14 registers and exports, R15 conduct controls and the wilful-defaulter workflow.

**Paste into Claude Code:**

```text
Phase 12 — Recovery Suite core (attachable). Governing brief: docs/00-master-prompt.md (Part 12, Phase 12; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026, effective 1 Jan 2027) against the contact-policy rule pack built in Phases 3b and 11, recording that the official text is not yet in docs/regulations/rbi/; (ii) the current version of docs/ecosystem/infrabyx-integration-spec.md; (iii) the Part 7A module boundaries. Then build the Recovery Suite core as an attachable module pack, in the `packages/recovery-*` domain packages behind the stable contract of 7A.0:

- 7A.0 attach and detach: a `module.yaml` manifest per module (id, version, requires, capabilities, events produced and consumed, APIs, permissions, data categories, regulatory refs, retention class, licence SKU, UI slots, migrations); the lifecycle AVAILABLE → LICENSED → INSTALLED → CONFIGURED (maker-checker) → CERTIFIED → ENABLED → READ_ONLY → DETACHED (7A.0.3); entitlement and flag checks on the server for every call (flag keys `mod.[module].[capability]`); `ModuleAttached` and `ModuleDetached` events (Integration Spec Part 6.16, Platform). Detaching turns off writes and UI, produces a hashed export pack and keeps every record read-only under legal hold until closure plus the retention period. Nothing is deleted on detach.
- R1 case management and strategy engine: case opening from M8 hand-off rules; strategy per product playbook key (Part 6.3); the mechanism-selection engine, which evaluates every mechanism on every material event and logs the permitted set with blocking reasons (for example SARFAESI blocked below the NBFC threshold or without CERSAI registration, s.26D; DRT blocked for an NBFC not notified under RDB s.2(h)(ii); arbitration blocked without a pre-named institution or post-dispute consent); the limitation engine (Limitation Act Arts. 19, 21, 55, 62, 136 and 137; rebase only on a written signed acknowledgment, s.18, or a documented part-payment, s.19; no reset on death, s.9; alerts at T−180, T−90 and T−30 days).
- R2 pre-legal recovery, field investigation and skip tracing: lawful sources only, no disclosure of the debt to third parties, purpose LOCATE logged (DPDP Act s.17(1)(f) basis [VERIFY: wording and commencement]).
- R3 legal notices, letters and document automation: clause library with statute citations; vernacular templates with human check (RBC 10); PDF/A with QR hash; DSC or eSign; outward register; dispatch adapters for India Post Speed Post with proof of delivery (Registered Post merged into Speed Post on 1 Sep 2025), couriers, email, DLT SMS and print-to-post; no WhatsApp channel for recovery or statutory notices (WhatsApp Business Messaging Policy prohibits debt-collection use; guard-rail 7A.0.6); a proof-of-service register per party per mode; no deemed-served state without evidence (*Sedhram Nilkanth Muglikar v M.R. Makhare*, Bom HC, 2026).
- R7 cheque and mandate dishonour: NI Act s.138 and PSS Act s.25 — notice within 30 days of receiving information of dishonour, 15 days for payment, complaint within one month of the cause of action with a condonation flag (s.142(1)(b)), filed where the payee's bank branch is (s.142(2)); summons by electronic modes and payment link, early s.143A, compounding-cost tiers (*Sanjabij Tari v Kishore S. Borcar*, 2025 INSC 1158, 25 Sep 2025); if the drawer company is under moratorium, proceed against its officers.
- R9 litigation and proceedings tracker: offensive and defensive matters in every forum (magistrate, civil and commercial courts, DRT and DRAT, NCLT and NCLAT, High Courts, Supreme Court, consumer commissions, arbitral tribunals, Lok Adalat and Permanent Lok Adalat, RB-IOS); CNR sync through the court-data adapter and daily cause-list matching; hearings, orders, directions as tasks, stays as holds on R1 actions; borrower-initiated matters (s.17 SARFAESI, Permanent Lok Adalat, writs) as a separate stream. SARFAESI, DRT and IBC matters are tracked manually here until Phase 17b.
- R11 counsel, agency and vendor management: empanelment with outsourcing due diligence (OUT 30, 34) and conflict checks; agent police verification and IIBF certificate register (RBC 100I from 1 Jan 2027); agency list on the website updated within 7 days (RBC 100K); counsel portal limited to assigned matters; bills with RCM GST and TDS.
- R12 recovery accounting and finance: versioned appropriation policy objects (contract first, else Indian Contract Act ss.59–61); legal-cost memo ledger, never a receivable on an NPA; post-write-off and technical write-off sub-ledgers (RSA 10(18), 91–94); RCM GST on advocate and recovery-agent fees (Notification 13/2017-CT(Rate)); TDS on professional fees [VERIFY: Income-tax Act 2025 s.393 table entry]; postings through M10 and exports to Tally Prime and SAP.
- R14 analytics, registers, reporting and exports: NPA, notice, litigation, agent, settlement, write-off and possessed-asset registers; CSV, XLSX, JSON (schema-versioned), XML, PDF/A, Tally Prime XML, SAP and API exports.
- R15 conduct, compliance and evidence controls: the contact-policy pre-check on every outbound recovery action (08:00–19:00, microfinance 09:00–18:00 until 31 Dec 2026, Third Amendment rule pack from 1 Jan 2027); call recording retention of at least 6 months, longer while sub judice (RBC 100P); grievance-officer block on every recovery communication (RBC 100AA); control results and evidence published as `ControlTestResultPublished` and `EvidenceSubmitted` through the outbox; delivery to the embedded M14 or the LawDocsComply bridge is wired in Phase 14, and to third-party GRC tools in Phase 16b.
- Carried over from v1.3: the wilful-defaulter workflow (R15.6; WD paras 5–7, 10, 13–15; ML and above) with monthly Annex I/II CIC files and the pre-transfer gate (WD 14); write-off and post-write-off recovery (R12).

Publish, with JSON Schemas in the registry and Pact tests, the events of Integration Spec Parts 6.7 (Collections: `RecoveryAgentNoticeSent`), 6.8 (Recovery) and 6.10 (Litigation) that these modules own: `RecoveryCaseOpened`, `RecoveryStrategyChanged`, `LegalNoticeIssued`, `NoticeServiceUpdated`, `RecoveryReceiptPosted`, `RecoveryCaseClosed`, `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled`, `OrderRecorded`, `LitigationCaseClosed`; and `LegalHoldChanged` (Integration Spec Part 6.14), which the detach and retention controls of 7A.0 produce. Udofin receives only status events scoped to its recovery-agent appointment.

Settlement and ADR (R8) follow in Phase 12b. SARFAESI, civil and tribunal remedies, IBC, repossession and auction, shared-exposure recovery and the product playbooks (R4–R6, R10, R13, R16) follow in Phase 17b.

Tests and acceptance evidence:

- detach test on a tenant with open cases: writes and UI off, reads intact, export pack hashed, row counts identical before and after;
- mechanism-selection golden cases (NBFC below ₹100 crore of assets; secured debt below ₹20 lakh; pledge collateral, s.31(b); un-notified NBFC at DRT; IBC moratorium holding all actions), each returning the expected blocking reason;
- limitation golden cases (demand loan from the loan date, Art. 21; a signed acknowledgment rebases; a death does not);
- s.138 clock cases computed on calendar months and the General Clauses Act s.9 first-day exclusion;
- no notice reaches SERVED without an evidence record; every borrower and guarantor gets a separate service row;
- a recovery contact attempted at 19:01 is denied and logged;
- recovery postings balance, and an NPA receipt follows the configured appropriation;
- a Tally Prime XML export imports into a test company; PDF/A files pass validation.

Show me the module manifests, the mechanism-selection table and the posting matrix for approval before coding.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Wilful-defaulter workflow per WD paras 5–7, 10, 13–15, gated to ML+ tenants; pre-transfer gate (WD 14) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-12-recovery-suite-core.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/recovery-suite-core in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Detaching the Recovery Suite on a tenant with open cases turns off writes and UI, produces a hashed export pack and leaves every row count unchanged (Part 7A.0; Part 10.2 principle 35).
- [ ] The mechanism-selection engine blocks SARFAESI for an NBFC below ₹100 crore of assets or a secured debt below ₹20 lakh (S.O. 652(E), 12 Feb 2021), for a charge not on CERSAI (SARFAESI s.26D) and for pledged collateral (s.31(b)), and blocks DRT for an NBFC not notified under RDB s.2(h)(ii).
- [ ] No notice reaches SERVED without an evidence record, and every borrower and guarantor has a separate service row (SARFAESI Rules, Rule 3(4); R3).
- [ ] The s.138 and s.25 PSS golden cases compute the 30-day notice, 15-day payment and one-month complaint deadlines correctly (NI Act ss.138, 142(1)(b)).
- [ ] A recovery contact outside 08:00–19:00 (09:00–18:00 for microfinance until 31 Dec 2026) is denied and logged, and wilful-defaulter Annex I/II files are produced monthly (RBC paras 91(2), 100; RBI/2026-27/230 para 100Y(4) from 1 Jan 2027; WD paras 11–12).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 12b — Settlement and ADR with Equator

- **Outcome:** R8: compromise settlement, conciliation (s.73/74), mediation, arbitration via Equator or other providers, Lok Adalat; ADR and settlement events
- **Depends on:** 12
- **Branch:** `feat/settlement-adr-equator`
- **Suggested sub-modules (one session each):** settlement policy engine (RSA paras 16, 86–100); forum selection, conciliation and mediation; arbitration controls and the Equator connector; Lok Adalat bulk referrals; OdrProvider multi-provider adapter and the Udofin settlement relay.

**Paste into Claude Code:**

```text
Phase 12b — Settlement and ADR with Equator. Governing brief: docs/00-master-prompt.md (Part 12, Phase 12b; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the Mediation Act 2023 commencement status (only ss.1, 3, 26, 31–38, 45–47, 50–54 and 56–57 in force by S.O. 4384(E) of 9 Oct 2023; Mediation Council of India established 27 Aug 2026; ss.4–25, 27–30 and 39–44 not yet notified); (ii) any RBI direction following *Shikha Ghosh v Axis Bank* (Del HC DB, 30 Sep 2026; next date 17 Nov 2026); (iii) the Equator API version, Integration Spec Part 6.9 (ADR) and Part 8 (Equator Resolution and other ODR/ADR providers). Then build R8, Settlement and ADR:

- Negotiation and compromise settlement: NPV calculator; the Board settlement policy as a versioned object; approver at least one level above the sanctioning authority with sanctioning officials excluded (RSA 16(5)(i)); Board approval for fraud and wilful-defaulter cases, without prejudice to criminal proceedings and penal measures (RSA 16(5)(ii), 97–98); payment over more than 3 months, or a part settlement, treated as restructuring until paid (RSA 89–90); consent decree where judicial proceedings are pending (RSA 100); cooling period of at least 12 months (RSA 95); quarterly reporting (RSA 93–94); applies to NBFCs below ₹500 crore too (RSA 157); CIC "settled" only where a waiver was given for financial inability (CIR 12(2), 12(4)); LWD removal only on full payment of the compromise amount (WD 13). AI or agent offers only inside the pre-approved band; anything else goes to a human approver.
- Forum-selection rules, logged with overrides: arbitration blocked for in-rem mortgage enforcement (*Booz Allen*, (2011) 5 SCC 532) and for claims within the RDB Act by banks and notified institutions (*Vidya Drolia*, 14 Dec 2020); all ADR on hold during an IBC moratorium; a pending consumer complaint cannot be forced into arbitration (*Emaar MGF v Aftab Singh*, (2019) 12 SCC 751); s.12A pre-institution mediation (3 + 2 months) before any commercial suit of ₹3 lakh or more without urgent relief (*Patil Automation*, 2022; *Dhanbad Fuels*, SC, 15 May 2025).
- Conciliation (default enforceable route today): invitation under A&C Act s.62 (no reply in 30 days is a rejection); online sessions; s.73 settlement signed by the parties and authenticated by the conciliator; s.74 status of an arbitral award, enforceable under s.36.
- Mediation: written consent to online mediation (Mediation Act s.30, once in force); recording hard-disabled (ss.22–23). Until s.27 is notified, a mediated settlement is only a contract, so the workflow converts it into a s.73 settlement or a consent decree.
- Arbitration: only where the loan agreement pre-names Equator or another independent institution, or the borrower gives written consent after the dispute arises; otherwise a s.11 petition. Never a lender-selected or lender-vetoed arbitrator, and never a forced choice from the lender's panel (*CORE v ECI-SPIC-SMO-MCML (JV)*, SC Constitution Bench, 8 Nov 2024; *Perkins Eastman v HSCC*, (2020) 20 SCC 760; *L&T Finance v Jai Paras Material Store*, Cal HC, 14 May 2026). s.21 notice to every known address with delivery evidence; Sixth Schedule disclosure before acceptance; per-neutral, per-lender counts against Fifth Schedule items 22 and 24 (*Shikha Ghosh*); clocks for s.23(4), s.29A, s.29B, s.33 and s.34(3); award stamped at signing (*URC Construction v AAI*, Del HC, 1 Sep 2026); execution in the civil court where assets lie (*Sundaram Finance v Abdul Samad*, (2018) 3 SCC 622).
- Lok Adalat: pre-litigation bulk referral under LSA Act ss.19–21 (next National Lok Adalat 12 Dec 2026), DLSA list export and award import, instalment awards over 3 months flagged as restructuring; Permanent Lok Adalat (ss.22A–22E) handled as borrower-initiated defensive matters in R9. The RBI ₹20 lakh Lok Adalat ceiling applies to banks and AIFIs only.
- Connectors: the Equator connector and the generic `OdrProvider` adapter for other providers (Presolv360, Sama, Jupitice, CADRE; CSV fallback where no API exists), both implementing Integration Spec Parts 6.9 and 8: `ADRReferralCreated`, `ADRConsentRecorded`, `ADRNeutralAppointed`, `ADRHearingScheduled`, `ADRCaseStatusChanged`, `ADROutcomeRecorded`, `ADROutcomeComplianceUpdated`; and the settlement events `SettlementRequested`, `SettlementOfferIssued`, `SettlementOfferAccepted`, `SettlementApproved`, `SettlementBreached` (Part 6.8). Outcomes create an R1 settlement record or an R9 execution matter.
- Udofin (LSP scope): relays `SettlementRequested`, shows RE-approved offers and Equator links (no separate app), and shows payment links to the RE's account only (CF 10(2)–(3)). Udofin never approves a settlement, never refers a dispute to arbitration and never holds funds.

Tests and acceptance evidence:

- a settlement proposed by the sanctioning officer cannot be approved by that officer or anyone below the next level;
- a fraud-tagged settlement routes to the Board;
- a 4-month instalment plan flags restructuring and blocks the closed-settled status until paid;
- a fresh-exposure request inside 12 months of settlement is blocked;
- referral without a pre-named institution or recorded post-dispute consent is rejected by the API;
- the lender role has no endpoint to choose, rank or veto a neutral;
- a mediation session cannot be recorded;
- Pact tests pass against the Equator stub, and Equator outage leaves Finbyx operating.

Show me the settlement policy object, the forum-selection table and the ADR state machine for approval before coding.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Settlement rules (RSA 16, 86–100), cooling-period gate (95), consent decree (100), fraud/WD Board approval (16(5)(ii)) [IRACP / RSA]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-12b-settlement-adr-equator.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/settlement-adr-equator in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A settlement cannot be approved by the sanctioning official or anyone below the next level, and fraud and wilful-defaulter settlements route to the Board (RSA para 16(5)).
- [ ] A settlement paid over more than 3 months is flagged as restructuring, and fresh exposure is blocked for 12 months after settlement (RSA paras 89, 95).
- [ ] An arbitration referral without a pre-named institution or recorded post-dispute consent is rejected, and the lender role has no endpoint to choose, rank or veto a neutral (CORE v ECI-SPIC-SMO-MCML (JV), SC, 8 Nov 2024; L&T Finance v Jai Paras Material Store, Cal HC, 14 May 2026).
- [ ] A conciliation settlement is produced as a s.73 instrument signed by the parties and authenticated by the conciliator, and mediation sessions cannot be recorded (A&C Act ss.73–74; Mediation Act ss.22–23).
- [ ] Pact tests pass against the Equator stub for every ADR event, and an Equator outage leaves Finbyx operating (Integration Spec Parts 6.9 and 8).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 13 — Finance, Ind AS 109 and accounting integrations

- **Outcome:** EIR, ECL, provisioning, tax, liabilities, accounting integrations, financial statements
- **Depends on:** 4, 9
- **Branch:** `feat/finance-indas-iracp`
- **Suggested sub-modules (one session each):** EIR and ECL; IRACP provisioning and Impairment Reserve; GST/TDS; borrowings and treasury; Tally/SAP integration and financial statements; capital adequacy (CAP).

**Paste into Claude Code:**

```text
Phase 13 — Finance, Ind AS 109 and accounting integrations. Governing brief: docs/00-master-prompt.md (Part 12, Phase 13; Part 8A prevails on regulatory points).

Implement:

- EIR (IRR-based) and amortisation;
- ECL staging with a pluggable model and a default provision matrix;
- parallel IRACP provisioning by layer, with Impairment Reserve logic;
- GST invoicing and extracts (NBFCs are exempt from e-invoicing), and TDS;
- bank reconciliation;
- the borrowings/liabilities module;
- month-end close;
- financial statements per Schedule III (Division III for Ind AS, Division I otherwise) and the FS Directions disclosure engine (Part 8A.8), including the Impairment Reserve, the IRACP-vs-Ind AS table, and the SICR-rebuttal and > 90 DPD-not-impaired registers;
- the investment portfolio module (Part 8A.5);
- TallyPrime (local connector, JSON), SAP and Zoho adapters, with reconciliation.

Our finance reviewer must approve the golden cases.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- IRACP rate tables (30, 32, 33, 48, 55, 58) and DLG ECL recompute (36A–36C); fair-value diminution, Sundry Liabilities account and RSA provisions (RSA 23, 48, 64, 118, 137, 198–211) [IRACP / RSA]
- Owned fund / NOF / EPt computation; dividend eligibility checker; PDI, sub-debt and NCD private-placement controls (CAP 9–13; DIV; MISC 9–11) [CAP / SBR / DIV / MISC]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-13-finance-indas-iracp.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/finance-indas-iracp in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] ECL and IRACP provisions reconcile to the GL; any shortfall goes to the Impairment Reserve (FS 12(2)).
- [ ] CRAR and leverage figures trace back to the GL with lineage (CAP).
- [ ] Your CA reviewer has signed off the golden ECL and provisioning cases.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 14 — Regulatory reporting, risk and compliance

- **Outcome:** CIC UCRF, CIMS returns (SR return catalogue), CRILC/DNBS09/FMR as applicable, FIU-IND, ALM, concentration, ICAAP mart, compliance module, LawDocsComply bridge
- **Depends on:** 9, 13
- **Branch:** `feat/regulatory-reporting`
- **Suggested sub-modules (one session each):** CIC submissions; SR return catalogue and CIMS returns; CRILC/DNBS09 and FMR; ALM and concentration; compliance module and LawDocsComply bridge.

**Paste into Claude Code:**

```text
Phase 14 — Regulatory reporting, risk and compliance. Governing brief: docs/00-master-prompt.md (Part 12, Phase 14; Part 8A prevails on regulatory points).

Build:

- CIC UCRF generation on the current reference dates, with rejection handling;
- the supervisory-return framework (online portal/CIMS formats per return spec), driven by the data-driven return catalogue in Part 8A.34, with reconciliation to GL, recorded aggregation rules, DQ metrics and ad-hoc subset queries (SR paras 13–19); start with the returns that apply to the pilot tenant's layer;
- CRILC monthly and the weekly Friday default report / DNBS09 (RSA 20–21, 106; SR 21–22; M13 row);
- the fraud module's per-case FMR/FUA, law-enforcement reporting, closure and RBR (Part 8A.14);
- FIU-IND reports, transaction-monitoring alerts and sanctions-match reporting (Part 8A.21);
- the ALM engine and daily LCR (Part 8A.7), with DNBS04A/04B and the public liquidity disclosure;
- the exposure engine, Large Exposure return and breach block (Part 8A.4);
- the Compliance Function suite (Part 8A.11);
- Auditor's Report evidence packs and DNBS10 (Part 8A.15);
- the AA consent-artefact store (Part 8A.10);
- the ICAAP data mart;
- the model inventory;
- the embedded compliance module (register, controls testing, calendar, product approval);
- the LawDocsComply bridge, with the compliance-mode and grievance-host switches.

Take return applicability, periodicity and due dates from Part 8A.34; take formats and validation rules from the RBI portal for each return.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Monthly Annex I and Annex II CIC files with 30-day removal logic (WD 11–13, 18) [RBC / WD]
- "the RWA/CRAR and leverage engine (Part 8A.24) with lineage and the para 48 golden test; SBR applicability and group/UL calendar (Part 8A.25); MISC intimation clocks (Part 8A.27)" [CAP / SBR / DIV / MISC]
- Governance register and its returns (8A.28). Third-party and outsourcing register with half-yearly Board/RMC packs and ACB vendor-reconciliation ageing (8A.29). ORM suite (8A.30) [GOV / OUT / ORM]
- Add bullets: the RBIA module (Part 8A.32); statutory-auditor register with Form A/B and branch-coverage report (Part 8A.33); PCA monitor and CFSS progress reporting (Part 8A.35); MFI qualifying-asset monitor and provision floor (Part 8A.31) [MFI / IAF / SA / SR / MSD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-14-regulatory-reporting.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/regulatory-reporting in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Return applicability for a test tenant matches the SR catalogue in Part 8A.34.
- [ ] CRILC, DNBS09, CIC and FMR test files pass format validation.
- [ ] The compliance module tracks every REQ-ID with an owner and a control test.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 15 — Grievance, borrower portal and feedback

- **Outcome:** Complaints, Internal Ombudsman, RB-IOS 2026, Equator referral (re-using the Phase 12b ODR adapter), borrower portal, feedback
- **Depends on:** 3b, 9, 12b
- **Branch:** `feat/grievance-portal`

**Paste into Claude Code:**

```text
Phase 15 — Grievance, borrower portal and feedback. Governing brief: docs/00-master-prompt.md (Part 12, Phase 15; Part 8A prevails on regulatory points).

Build:

- the complaint management system, with automated Internal Ombudsman escalation where applicable, and RB-IOS 2026 support;
- Equator referral, re-using the Phase 12b ODR adapter (R8);
- the AI support assistant, restricted to approved sources;
- the optional borrower self-service portal;
- feedback (CSAT/NPS, plus sales feedback within 30 days under RBC para 101Y [VERIFY: amendment text not supplied]).

Use the Phase 3b communications module for all messages.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Next-higher-level grievance disposal (RBC 7(2)); Second Amendment para 101Y feedback behind [VERIFY: amendment text not supplied] [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-15-grievance-portal.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/grievance-portal in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] CIR complaint clocks (21/30 days) and ₹100/day compensation work (CIR 34–35).
- [ ] Complaint replies carry the RB-IOS 2026 escalation text and follow its escalation timelines [VERIFY: RB-IOS 2026 text not yet supplied].
- [ ] Every complaint is disposed at the next-higher level where RBC 7(2) requires it.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase P — MVP hardening and pilot go-live

- **Outcome:** E2E, independent VAPT, COB load test, DR restore drill, India-region production cut-over for the two MVP products
- **Depends on:** 0–15, including 3b, 8b, 8c and 12b (Phase 14 only for the returns that apply to the pilot's layer)
- **Branch:** `release/pilot`

**Paste into Claude Code:**

```text
Phase P — MVP hardening and pilot go-live. Governing brief: docs/00-master-prompt.md (Part 12, Phase P; Part 8A prevails on regulatory points).

For the two MVP products and the pilot tenant, deliver:

- a full E2E regression;
- independent VA and PT on production by a CERT-In-empanelled firm, CVSS-scored, with all Critical/High findings closed and re-tested (CYB paras 121–126);
- a source-code-escrow deposit and the vendor security certificate for the release (CYB paras 105–106);
- a COB load test;
- a DR switchover drill running production on the DR site for one full business day including COB, with post-drill reconciliation (CYB paras 129–137);
- an incident drill proving that tenant notification fits a 6-hour RBI/DAKSH filing measured from Finbyx's own detection timestamp (CYB paras 28, 141, 146; OUT para 61);
- a data-residency check of every environment and sub-processor;
- a production runbook;
- a migration and cut-over plan;
- a controlled go-live checklist for my approval.

Do not deploy to production without my explicit authorisation.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- an exit drill (full tenant export, re-import into a clean instance, purge certificate) (OUT 87–88, 97(xvi)); vendor assurance pack issued (OUT 30, 71; ORM 73); SOC log feed live (OUT 97(xi)) [GOV / OUT / ORM]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-p-pilot.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch release/pilot in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The independent VAPT has no open critical or high findings.
- [ ] The DR restore drill and the 6-hour incident-notification drill both pass.
- [ ] Production runs on India-region hosting only; the exit drill (export, re-import, purge certificate) passes.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 16 — Partner connectors, co-lending, loan transfers and securitisation

- **Outcome:** Full LSP framework, DLG ledger, co-lending/DA/securitisation engine, partner portals
- **Depends on:** 8c, 9, 10, 13, 14
- **Branch:** `feat/partners-colending-transfers`
- **Suggested sub-modules (one session each):** full LSP framework and DLG ledger; co-lending engine; loan-transfer engine (TDCR); securitisation engine and investor module (SEC); partner portals.

**Paste into Claude Code:**

```text
Phase 16 — Partner connectors, co-lending, loan transfers and securitisation. Governing brief: docs/00-master-prompt.md (Part 12, Phase 16; Part 8A prevails on regulatory points).

Extend the Phase 8c connector into the full LSP/channel-partner framework (Part 5). Add:

- the DLG ledger (≤ 5% of the amount disbursed out of the covered portfolio, invoked within 120 days overdue), emitting `DLGRecoveryShared` for post-invocation recoveries shared under the contract (CF 25(3); never credited to the loan, CF 25(2)) and consuming the LSP's `DLGDisclosurePublished` (CF 28);
- the collection-agent appointment model, kept separate from DLG;
- the CIMS DLA register;
- the co-lending engine (10% retention, 15-day booking, bank escrow, blended rate, next-working-day classification sync, each lender's own CIC reporting, originator-only DLG ≤ 5% of CLA outstanding (TDCR 123), website partner list (TDCR 126));
- the loan-transfer engine (TDCR Part A): MHP, one-third DD/10% retention, no re-acquisition, 30-day replacement, stressed-loan sale with valuation and Swiss challenge, ARC/SR accounting, trade-reporting database;
- the securitisation engine (SEC): eligibility, MRR, 20% cap, SPE checks, CE/liquidity/servicing facilities, STC checker, Annex I and quarterly RBI report;
- the investor-side securitisation module (SEC Ch V, paras 97–107);
- partner portals.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Securitisation SEC-ERBA capital; DLG and co-lending capital deductions (CAP 15, 19–51) [CAP / SBR / DIV / MISC]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-16-partners-colending-transfers.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/partners-colending-transfers in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The CF 24 DLG ledger and the TDCR 123 co-lending DLG ledger are separate.
- [ ] Loan transfers enforce MHP, retention and the no-re-acquisition rule (TDCR).
- [ ] Fraud accounts cannot be transferred until the FRM 54 and TDCR 28/78 gates are cleared.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 16b — Ecosystem integration hub v2

- **Outcome:** Ecosystem Integration Specification implemented: Udofin for all products, Equator, LawDocsComply and third-party GRC (OSCAL), court data, e-auction, notice dispatch, agencies and diallers, third-party LOS/LMS; module registry; connector certification
- **Depends on:** 12b, 14, 16
- **Branch:** `feat/ecosystem-hub-v2`
- **Suggested sub-modules (one session each):** platform standards (registry, webhooks, idempotency, signatures, consent references); Udofin all-product lifecycle, with the LAS/LAMF collateral contracts registered and stubbed (live with Phase 17); Equator certification and the LawDocsComply / third-party GRC connector with OSCAL; court data, e-auction, notice dispatch, agencies and diallers; third-party LOS/LMS, future-app onboarding and the daily reconciliation framework.

**Paste into Claude Code:**

```text
Phase 16b — Ecosystem integration hub v2. Governing brief: docs/00-master-prompt.md (Part 12, Phase 16b; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) the version of docs/ecosystem/infrabyx-integration-spec.md and that the same version is committed in the Udofin, Equator and LawDocsComply repositories; (ii) the standards it pins (CloudEvents 1.0.2, OpenAPI 3.1 with 3.2 for streaming, AsyncAPI 3.0, JSON Schema 2020-12, Standard Webhooks, RFC 9421, RFC 8705, FAPI 2.0; the Idempotency-Key header and OAuth 2.1 are still IETF drafts); (iii) the access position for each external connector listed below, recorded in docs/integrations/register.md. Then implement the Integration Spec in Finbyx (Parts 3–14, sequenced by Part 15):

- Platform (Integration Spec Part 3): schema registry with BACKWARD compatibility (a breaking change publishes a new `vN`, dual-published for at least 90 days); transactional outbox and inbox with idempotent writes and a dead-letter queue; Standard Webhooks with a 5-minute tolerance; `Idempotency-Key` (UUIDv7; stored response kept at least 24 hours, 7 days for money movements; Integration Spec Part 3.4); mTLS on every connection plus sender-constrained OAuth client credentials; RFC 9421 signatures or detached JWS on regulated messages; FAPI 2.0 for any API acting on a borrower's behalf; a consent reference on every PII payload, rejected without one unless a statutory basis is flagged (CF 13(4)); India-only residency; the module registry and entitlements built in Phase 12 (7A.0), extended to connectors, product templates and ecosystem apps (Integration Spec Part 11.1); and the connector certification suite, which emits `ConnectorCertified`.
- Udofin, all products: the product × lifecycle matrix (Part 6.3 of this prompt; Integration Spec Part 7.2), including the LAS and LAMF collateral events and APIs, registered and Pact-tested here against stubs and taken live with the Phase 17 margin engine (Part 6.4; Integration Spec Parts 6.5, 7.3 and 15: `CollateralHoldingsShared`, `CollateralPledgeRequested`, `CollateralPledgeCreated`, `CollateralPledgeFailed`, `CollateralChargeRegistered`, `CollateralValuationUpdated`, `MarginCallRaised`, `MarginCallCured`, `MarginCallLapsed`, `CollateralInvoked`, `CollateralReleased`); co-lending and transfer events (Part 6.6: `CoLendingSplitConfirmed`, `CoLendingReceiptAllocated`, `ClassificationSynced`, `LoanTransferred`, `ServicerChanged`); recovery and ADR status events scoped to Udofin's appointment and the borrower's consent; and the six events proposed by Udofin v1.0 (`ConsentWithdrawn`, `DataPrincipalRequest`, `SecurityIncidentNotified`, `DLGDisclosurePublished`, `RiskSignalRaised`, `SettlementRequested`).
- Equator: the full ADR contract from Phase 12b (Integration Spec Part 8), certified, with SLA monitors (screening, first notice, delivery status, appointment, webhook latency).
- LawDocsComply and third-party GRC: the generic GRC connector (Obligation, Control, ControlTestResult, Issue, Incident, RegulatoryReturn, PolicyAttestation, OutsourcingArrangement, KRI); REST pull with cursor pagination, CloudEvents push, and a periodic OSCAL package (catalog, component-definition, assessment-results, POA&M; OSCAL 1.2.x); adapters for MetricStream (REST), IBM OpenPages (GRC REST), ServiceNow IRM (staging tables) and Archer (REST and Content API); the Compliance/GRC events (Integration Spec Parts 6.15 and 9) `ObligationPublished`, `ControlTestResultPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `ReturnStatusUpdated`, `PolicyAttested`. Evidence is hash-chained and carries aggregate counts and masked sample IDs, never raw PII. [VERIFY: LawDocsComply public API]
- Court data and legal tech: official eCourts open APIs where the tenant obtains institutional-litigant credentials [VERIFY: NBFC eligibility], otherwise licensed aggregators (CNR, cause lists, orders); e-DRT is a filing portal with no API; e-Jagriti for consumer matters.
- E-auction: listing export and bid-log import for BAANKNET [VERIFY: NBFC listing and API], C1 India, auctiontiger, MSTC and Shriram Automall.
- Notice dispatch: India Post bulk booking and tracking (DoP contract and CEPT onboarding; XML manifests; tracking events), couriers and print-to-post vendors behind `NoticeDispatchProvider`.
- Collection agencies and diallers: allocation and recall, activity and recording ingestion, agent certificate sync, behind `CollectionAgencyConnector` and `DiallerProvider`; every attempt passes the R15 contact-policy check.
- Third-party LOS and LMS: inbound loan boarding for LMS-only tenants, outbound booking for LOS-only tenants, and legacy migration feeds, on the same contract.
- Future ecosystem apps: the onboarding checklist (legal role and materiality under OUT, group-outsourcing policy (OUT 45–51), DPIA and India residency, need-to-know data, OIDC and SCIM, contracts in the registry with Pact tests, VAPT and SBOM, manifest and SKU, BCP and exit plan, certification), demonstrated with a field-investigation app stub that consumes `VerificationRequested` and produces `VerificationCompleted` (Integration Spec Part 6); any further event goes to the specification's proposal process, never invented locally.
- Daily reconciliation framework (Integration Spec Part 7.4; breaks as `ReconciliationBreakRaised`): applications, KFS acceptance, disbursement UTRs, collections, collateral registers (depository, RTA, Vahan, CERSAI, gold vault), co-lending escrow (three-way), DLG, LSP fees, classification-sync timestamps, servicer remittances, and legal and ADR status versus Equator and court feeds.

Tests and acceptance evidence:

- schema-compatibility check blocks a breaking change without a new version;
- replayed webhooks and duplicate `Idempotency-Key` requests produce no second effect;
- a PII payload without a consent reference is rejected;
- each certified connector has a passing certification report (Integration Spec Part 14) and a `ConnectorCertified` event;
- an OSCAL export validates against the NIST schema;
- every product template live in Finbyx passes the Udofin Pact suite for its lifecycle events (secured templates join when Phase 17 delivers them);
- reconciliation breaks open cases by T+1;
- outage of any connector leaves Finbyx operating, with queued retries and dead-letter handling.

Show me the connector list with access status, the event matrix and the certification suite for approval before coding.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-16b-ecosystem-hub-v2.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/ecosystem-hub-v2 in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A breaking schema change is rejected unless it is published as a new major version that runs in parallel for at least 90 days (Integration Spec Parts 3.3 and 14.1).
- [ ] Replayed webhooks and duplicate Idempotency-Key requests cause no second effect, and a PII payload without a consent reference is rejected (CF para 13(4)).
- [ ] Every enabled connector has a passing certification report and a ConnectorCertified event, and Udofin passes the lifecycle Pact suite for every product template live in Finbyx at this phase; LAS/LAMF and the other secured templates are certified after Phase 17 (Integration Spec Parts 7.2, 14 and 15).
- [ ] The OSCAL export validates against the NIST schema and carries no raw PII (M14 GRC connector).
- [ ] Daily reconciliation raises ReconciliationBreakRaised by T+1 for each seeded break, including the co-lending escrow and classification-sync timestamps (TDCR paras 117, 124; Integration Spec Part 7.4).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 17 — Secured products expansion

- **Outcome:** LAP/Home, Vehicle, Gold, LAS/LAMF templates (Part 6.3); collateral flows; LAS/LAMF margin engine (Part 6.4); gold custody, release and compensation (enforcement in Phase 17b)
- **Depends on:** P, 12, 16b
- **Branch:** `feat/secured-products`
- **Suggested sub-modules (one session each):** LAP/Home; Vehicle; Gold; LAS/LAMF.

**Paste into Claude Code:**

```text
Phase 17 — Secured products expansion. Governing brief: docs/00-master-prompt.md (Part 12, Phase 17; Part 8A prevails on regulatory points).

For each secured product (LAP/Home, Vehicle, Gold, LAS/LAMF):

1. produce the product spec and feasibility notes;
2. implement the collateral workflows (M5), integrations and regulatory checks;
3. build the collateral-side rules these products need before enforcement: gold release, compensation and unclaimed-collateral rules (RBC paras 58, 69, 71–72), the vehicle repossession clause contents in the agreement template (RBC paras 26–27), and the LAS/LAMF margin engine (Part 6.4), publishing the collateral events through the Phase 16b hub (Integration Spec Parts 6.5 and 7.3). SARFAESI, repossession, auctions, pledge invocation and sale are built in Phase 17b.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Gold conduct module (RBC 43–59 and 67–75; the auction rules in paras 60–66 are built in Phase 17b); vehicle repossession clause in the agreement (RBC 26–27) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-17-secured-products.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/secured-products in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Gold-loan LTV, valuation, release, compensation and unclaimed-collateral rules match RBC 43–59 and 67–75 and CF 32–50 (gold auctions, RBC 60–66, are gated in Phase 17b).
- [ ] The LAS margin engine raises calls with a 7-working-day deadline (CF para 106(1)) and gold release follows RBC paras 58 and 69.
- [ ] Every charge type is filed with CERSAI (CRM 27–28).
- [ ] The collateral events (CollateralPledgeCreated, CollateralValuationUpdated, MarginCallRaised, MarginCallCured, MarginCallLapsed, CollateralReleased) pass the Udofin Pact suite through the Phase 16b hub (Integration Spec Parts 6.5, 7.3 and 15).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 17b — Secured enforcement and shared-exposure recovery

- **Outcome:** R4 SARFAESI, R5 civil and DRT where eligible, R6 IBC, R10 repossession and auction, R13 co-lending, transfer, securitisation, ARC and consortium recovery, R16 product playbooks
- **Depends on:** 16b, 17
- **Branch:** `feat/secured-enforcement`
- **Suggested sub-modules (one session each):** R4 SARFAESI; R5 civil and tribunal remedies; R6 IBC; R10 repossession, valuation, auction and sale; R13 shared-exposure recovery; R16 product playbooks.

**Paste into Claude Code:**

```text
Phase 17b — Secured enforcement and shared-exposure recovery. Governing brief: docs/00-master-prompt.md (Part 12, Phase 17b; Part 8A prevails on regulatory points).

Before writing the specification, verify: (i) each pilot tenant's SARFAESI eligibility evidence (last audited assets and the NBFC thresholds of ₹100 crore of assets and ₹20 lakh of debt under S.O. 652(E), 12 Feb 2021) and any RDB s.2(h)(ii) notification for the tenant; (ii) IBC commencement notices after S.O. 2625(E) of 22 May 2026 (CIIRP, group insolvency and cross-border provisions not in force as of 19 Oct 2026); (iii) access to BAANKNET and to the Vahan financier services. Then build:

- R4 SARFAESI enforcement: eligibility gate (NBFC thresholds; HFCs as notified financial institutions; s.31 exclusions including pledges, agricultural land and claims of ₹1 lakh or less or below 20% of principal plus interest); CERSAI registration gate (s.26D); limitation gate (s.36); state machine 13(2) notice → 13(3A) reply within 15 days → 60-day cure → possession notice and publication within 7 days (Rule 8(1)–(2)) → s.14 application → valuation and reserve → sale notice (Rule 8(6)) → auction no earlier than 30 days (15 for a re-sale; Rule 9(1)) → 25% deposit the same or next working day → balance within 15 days of confirmation, or up to 3 months by written extension (Rule 9(3)–(4); *M.R. Vasumathi v Authorized Officer*, SC, 9 Jun 2026) → sale certificate → s.13(7) appropriation → surplus or shortfall; redemption closing on publication of the sale notice (s.13(8); *Celir LLP v Bafna Motors*, SC, 21 Sep 2023; *M. Rajendran v KPK Oils*, 2025 INSC 1144); borrower's s.17 window of 45 days tracked in R9; possessed-asset website feed updated monthly (CIR 21).
- R5 civil and tribunal remedies: DRT original applications only for RDB-eligible lenders (₹20 lakh threshold, S.O. 4312(E) of 6 Sep 2018); an NBFC is not eligible unless notified under s.2(h)(ii) (*Tata Motors Finance v Naushad Khan*, Bom HC, 2023; *Aditya Birla Finance v Anjali Nag*, Del HC, 2024); e-DRT filing for all pleadings from 23 Jun 2025; Order XXXVII summary suits; commercial suits with the s.12A gate from R8; execution under Order XXI; the forum for an un-notified NBFC's s.13(10) shortfall application [VERIFY].
- R6 insolvency (IBC): NeSL information-utility record of default; s.7 applications for defaults of ₹1 crore or more within Art. 137 limitation, with admission tracked against s.7(5) as amended (14 days, from 26 May 2026); Form C claims by the public-announcement date and late-claim rules; CoC vote log; personal-guarantor applications at the NCLT (s.95; no interim moratorium against personal guarantors to corporate debtors, s.96(4) as amended); moratorium watcher that freezes R4, R7 and R10 actions against the corporate debtor; liquidation auctions on BAANKNET; CIIRP kept off in the rule pack until notified.
- R10 repossession, valuation, auction and sale: vehicles (contractual notice period elapsed, daytime repossession by an authorised agent with ID and authorisation, signed possession memo and inventory, no force; RBC 26; *Hari Dutta Sharma v State of UP*, SC, 16 Sep 2026; Form 36 re-registration under MV Act s.51(5)); gold (RBC 60–66; reserve from the IBJA or exchange feed; surplus within 7 working days); LAS and LAMF invocation and sale (Part 6.4.7); SARFAESI immovable and movable sales; valuer panel and reserve worksheet; e-auction listings through the Phase 16b connectors; `AssetRepossessed`, `AuctionScheduled`, `AuctionConcluded`, `CollateralInvoked`, `SurplusRefunded` (Integration Spec Parts 6.5 and 6.8).
- R13 shared-exposure recovery: co-lending decision matrix (servicer RE decides contact; each RE settles its own share under its own Board policy; joint SARFAESI needs secured creditors holding at least 60% by value, s.13(9)); classification sync by the end of the next working day (TDCR 124, `ClassificationSynced`); recoveries after DLG invocation kept off the loan account (CF 25(2)); transferred loans (each party resolves its own economic interest, TDCR 19(2); binding invocation mechanism for security held in trust, TDCR 21; servicer trust accounts and certified data, TDCR 29–30, 41–42); securitisation servicing (remit all cash flows, no commingling, SEC 95–96; servicer replacement, SEC 70); stressed-loan sale and ARC transfer (Board review, valuations, Swiss challenge, permitted transferees, s.29A check, cash only, cooling period; TDCR 56–94; substitution of the assignee in pending cases); consortium and ICA vote engine (75% by value and 60% by number; dissenters at least liquidation value; RSA 31–33, 45–48); `LoanTransferred` and `ServicerChanged` (Integration Spec Part 6.6).
- R16 product recovery playbooks: one playbook per product code in Part 6.3 (and the co-lending overlay), each binding the mechanism profile, notice templates, clocks, conduct overlay and accounting map; tenant-editable within guard-rails.

Tests and acceptance evidence:

- SARFAESI is blocked for a tenant below the threshold, for a debt below ₹20 lakh and for a charge not on CERSAI;
- a sale balance received on day 16 with no written extension blocks the sale certificate and opens the forfeiture workflow;
- a vehicle repossession task cannot start before the notice period ends or without an authorised agent;
- a gold auction reserve below 90% (85% after two failed auctions) is rejected;
- an IBC admission for a corporate debtor freezes SARFAESI and invocation actions against it;
- a 90:10 co-lent account cannot start SARFAESI on the 10% lender's vote alone;
- an ICA decision with 76% by value but 55% by number fails;
- every product code has an approved R16 playbook.

Show me the SARFAESI state machine, the R13 decision matrix and the playbook list for approval before coding.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Gold auction rules (RBC 60–66: notice, two newspapers, reserve ≥ 90% of current value or 85% after two failures, first auction in the district, no related-party bids, surplus within 7 working days); vehicle repossession conduct (RBC 26) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-17b-secured-enforcement.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/secured-enforcement in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] SARFAESI actions are blocked for an ineligible tenant, a debt below ₹20 lakh, a time-barred claim (SARFAESI s.36) or a charge not registered with CERSAI (s.26D).
- [ ] A sale balance received after 15 days without a written extension blocks the sale certificate and opens the forfeiture workflow (Security Interest (Enforcement) Rules, Rule 9(4); M.R. Vasumathi v Authorized Officer, SC, 9 Jun 2026).
- [ ] A vehicle repossession task cannot start before the contractual notice period ends or without an authorised agent and a signed possession memo (RBC para 26; Hari Dutta Sharma v State of UP, SC, 16 Sep 2026).
- [ ] An IBC admission freezes SARFAESI, pledge-invocation and repossession actions against the corporate debtor, and CIIRP stays switched off in the rule pack (IBC s.14; IBC (Amendment) Act 2026).
- [ ] Joint SARFAESI on a co-lent account needs secured creditors holding at least 60% by value, and an ICA decision needs 75% by value and 60% by number (SARFAESI s.13(9); RSA para 32).
- [ ] A gold auction without prior notice to the borrower, with a reserve below 90% of current value (85% after two failed auctions), outside the district for the first auction or with a related-party bidder is rejected, and any surplus is refunded within 7 working days (RBC paras 60, 63–66).
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 18 — Analytics, AI layer and MCP

- **Outcome:** MIS catalogue, BI embedding, governed AI copilots, read-only MCP server
- **Depends on:** P
- **Branch:** `feat/analytics-ai-mcp`

**Paste into Claude Code:**

```text
Phase 18 — Analytics, AI layer and MCP. Governing brief: docs/00-master-prompt.md (Part 12, Phase 18; Part 8A prevails on regulatory points).

Build:

- the MIS catalogue;
- embedded BI with row-level security;
- governed AI copilots (M20), with an AI model inventory;
- the read-only, tenant-scoped MCP server.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-18-analytics-ai-mcp.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/analytics-ai-mcp in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] AI never approves, rejects or prices a loan, moves money or rejects a complaint.
- [ ] The MCP server is read-only and tenant-scoped.
- [ ] Every model is in the model inventory with an owner and validation record.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 19 — Migration tooling

- **Outcome:** Legacy loan boarding and reconciliation sign-off
- **Depends on:** 9, 13
- **Branch:** `feat/migration-tooling`

**Paste into Claude Code:**

```text
Phase 19 — Migration tooling. Governing brief: docs/00-master-prompt.md (Part 12, Phase 19; Part 8A prevails on regulatory points).

Build the legacy loan-boarding toolkit, with history, opening balances, DPD reconstruction and reconciliation sign-off reports.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-19-migration-tooling.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/migration-tooling in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Migrated balances reconcile to the legacy trial balance, loan by loan.
- [ ] Classification history and DPD are preserved, not recomputed silently.
- [ ] The tenant signs off the reconciliation.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

### Phase 20 — Scale hardening and AWS migration

- **Outcome:** Multi-tenant scale tests, AWS ap-south-1 / ap-south-2 migration, DR at scale, performance tuning
- **Depends on:** P, 16–19
- **Branch:** `feat/scale-aws`

**Paste into Claude Code:**

```text
Phase 20 — Scale hardening and AWS migration. Governing brief: docs/00-master-prompt.md (Part 12, Phase 20; Part 8A prevails on regulatory points).

Run multi-tenant scale tests. Then:

- write and rehearse the AWS ap-south-1 / ap-south-2 migration runbook;
- run DR at scale;
- do performance tuning;
- repeat independent VAPT.

Present a controlled migration plan for my approval.

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-20-scale-aws.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/scale-aws in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Scale tests meet the agreed throughput and COB window.
- [ ] The AWS migration stays in ap-south-1 / ap-south-2.
- [ ] The DR drill passes at production scale.
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

---

## 4. Utility prompts

Replace the text in square brackets before pasting.

| No. | When to use | Prompt |
|---|---|---|
| U1 | Start a sub-module | Continue Phase [n]. This session covers only the sub-module: [name]. Re-read the approved spec docs/specs/[file].md and the related REQ-IDs, confirm the scope in five lines, then build it. Do not touch other sub-modules. |
| U2 | Resume after an interruption | Read CLAUDE.md, docs/status and the open PR for Phase [n]. Summarise what is done, what is pending and any failing tests, then continue from the next pending item. |
| U3 | Status check | Give me a status report for Phase [n]: items done, items pending, tests run and their results, open [VERIFY] items, and any decision you need from me. Do not write code. |
| U4 | Fix failing tests | The following tests fail: [paste output]. Find the root cause, explain it in plain English, propose the fix, and apply it only after I approve. Re-run the full test suite and paste the results. |
| U5 | New RBI circular or amendment | I have added [RBI number, date] to docs/regulations/rbi/. Read it in full. List every requirement with a new REQ-ID, every existing REQ-ID it amends or withdraws, and every module, rule pack, return and test affected. Propose the changes with effective dates. Do not change code until I approve. |
| U6 | Run the review gate | Run the review gate for Phase [n] from docs/01-phase-runbook.md. For each item, show the evidence (test name and output, query result, screenshot or file path). Mark any item you cannot evidence as NOT MET. |
| U7 | Change a specification | I want to change the approved spec for Phase [n]: [change]. Update docs/specs/[file].md, list the regulatory and ledger impact, update the tests, and wait for my approval before changing code. |
| U8 | Regulatory check before a regulated workflow | Before building [workflow], list the applicable REQ-IDs, the entity-profile flags that decide applicability (layer, asset size, deposit-taking, HFC and so on), and any [VERIFY] item. Confirm what is law and what is our interpretation. |

---

## 5. Progress tracker

| Phase | Spec approved (date) | PR | Review gate passed (date) | Notes |
|---|---|---|---|---|
| Phase 0 — Repository audit and architecture |  |  |  |  |
| Phase 1 — Platform foundation |  |  |  |  |
| Phase 2 — Database, tenancy and security |  |  |  |  |
| Phase 3 — Masters, configuration and product factory |  |  |  |  |
| Phase 3b — Communications foundation |  |  |  |  |
| Phase 4 — Ledger and accounting core |  |  |  |  |
| Phase 5 — Schedule and allocation engine |  |  |  |  |
| Phase 6 — Customer, KYC and consent |  |  |  |  |
| Phase 7 — Origination (LOS) |  |  |  |  |
| Phase 8 — Documentation, execution, DMS and disbursement |  |  |  |  |
| Phase 8b — Field app foundation |  |  |  |  |
| Phase 8c — Udofin / LSP inbound connector (minimal) |  |  |  |  |
| Phase 9 — Servicing (LMS) and COB |  |  |  |  |
| Phase 10 — Payments and reconciliation |  |  |  |  |
| Phase 11 — Collections |  |  |  |  |
| Phase 12 — Recovery Suite core (attachable) |  |  |  |  |
| Phase 12b — Settlement and ADR with Equator |  |  |  |  |
| Phase 13 — Finance, Ind AS 109 and accounting integrations |  |  |  |  |
| Phase 14 — Regulatory reporting, risk and compliance |  |  |  |  |
| Phase 15 — Grievance, borrower portal and feedback |  |  |  |  |
| Phase P — MVP hardening and pilot go-live |  |  |  |  |
| Phase 16 — Partner connectors, co-lending, loan transfers and securitisation |  |  |  |  |
| Phase 16b — Ecosystem integration hub v2 |  |  |  |  |
| Phase 17 — Secured products expansion |  |  |  |  |
| Phase 17b — Secured enforcement and shared-exposure recovery |  |  |  |  |
| Phase 18 — Analytics, AI layer and MCP |  |  |  |  |
| Phase 19 — Migration tooling |  |  |  |  |
| Phase 20 — Scale hardening and AWS migration |  |  |  |  |

*End of runbook.*
