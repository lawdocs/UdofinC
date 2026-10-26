# FINBYX — Phase-wise Claude Code Runbook

**Companion to the Finbyx Master Build Prompt v1.3** · 18 October 2026 · ready-to-paste instructions for every build phase

---

## 1. How to use this runbook

1. **Before Session 1:** commit the master prompt as `docs/00-master-prompt.md` and the RBI PDFs to `docs/regulations/rbi/`. You can also commit this runbook as `docs/01-phase-runbook.md`.
2. **One phase per session.** Start a fresh Claude Code session for each phase or sub-module, and paste only that phase's block.
3. **Each block is self-contained.** It already includes:
   - the Part 12 instruction;
   - the v1.3 regulatory additions from Part 8A.36.4;
   - the standard closing that makes Claude Code list the REQ-IDs, write the specification and stop for your approval before coding.
4. **Approve, then build.** Read the specification, reply "Approved" (or give changes), and let Claude Code build, test and open the pull request.
5. **Run the review gate** (the checklist under each phase) before merging. Use prompt U6 in Section 4 to have Claude Code run it for you.
6. **Large phases:** use the sub-module split shown for the phase. Paste the full block once, then use prompt U1 for each sub-module.
7. **Order:** 0 → 1 → 2 → 3 → 3b → 4 → 5 → 6 → 7 → 8 → 8b → 8c → 9 → 10 → 11 → 12 → 13 → 14 → 15 → P → 16 → 17 → 18 → 19 → 20. Do not start a phase until the phases it depends on are merged.

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
Read docs/00-master-prompt.md in full, then execute Part 13 (Phase 0 only).

In addition to the Phase 0 instruction in Part 12:
- seed docs/regulations/errata.md from Appendix F;
- store the RBI PDFs in docs/regulations/rbi/ and record each file's SHA-256 hash and "updated as on" date in docs/regulations/index.md (Part 8A.0.1).

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
- [ ] The PR shows the test output; the ledger balances (if money moved); the regulatory register and docs/status are updated.

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

Implement LSP contract v1 per Part 5:

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
- the effective-dated contact-policy engine from Phase 3b (current RBC paras 89–100; paras 100A–100AB from 1 Jan 2027 [VERIFY: Third Amendment text not supplied]);
- mandatory call recording and retention (para 100P);
- pre-visit intimation (para 100L) and visit conditions (para 100Y(5));
- borrower default/DPD alerts sent with each CIC submission (CIR para 34(1)(i)), and recovery-agent particulars sent before first contact on digital loans (CF para 9(6)).

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Contact engine for current RBC paras 89–100 (microfinance window under 91(2); para 100 excludes microfinance); Third Amendment rules behind [VERIFY: amendment text not supplied] [RBC / WD]

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

### Phase 12 — Recovery and legal (unsecured) + Equator

- **Outcome:** Sec 138 / Sec 25 PSS Act, arbitration and mediation via Equator, Lok Adalat, IBC/NeSL, OTS, write-off, wilful defaulters
- **Depends on:** 11
- **Branch:** `feat/recovery-legal`
- **Suggested sub-modules (one session each):** legal case management (Sec 138, arbitration, Lok Adalat); Equator ODR adapter; settlements and write-offs; wilful-defaulter workflow.

**Paste into Claude Code:**

```text
Phase 12 — Recovery and legal (unsecured) + Equator. Governing brief: docs/00-master-prompt.md (Part 12, Phase 12; Part 8A prevails on regulatory points).

Build:

- legal case management;
- the Sec 138 NI Act and Sec 25 PSS Act workflows, with statutory timelines and templates;
- arbitration and mediation referral to Equator through the ODR adapter, with outcomes flowing back;
- Lok Adalat;
- the IBC/NeSL IU filing workflow;
- the OTS/settlement calculator with approval matrix;
- the wilful-defaulter workflow (WD paras 5–7, 10, 13–15; Part 8A.20), with monthly Annex I/II CIC files, penal-measure clocks and the pre-transfer wilful-default gate;
- write-off and post-write-off recovery accounting.

SARFAESI, repossession and auction are built in Phase 17, with the secured products.

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Settlement rules (RSA 16, 86–100), cooling-period gate (95), consent decree (100), fraud/WD Board approval (16(5)(ii)) [IRACP / RSA]
- Wilful-defaulter workflow per WD paras 5–7, 10, 13–15, gated to ML+ tenants; pre-transfer gate (WD 14) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-12-recovery-legal.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/recovery-legal in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Settlements with fraud or wilful-defaulter borrowers route to the Board (RSA 16(5)(ii)).
- [ ] The cooling-period gate blocks fresh exposure for at least 12 months after a settlement (RSA 95).
- [ ] The wilful-defaulter workflow produces the monthly Annex I/II CIC files (WD).
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

- **Outcome:** Complaints, Internal Ombudsman, RB-IOS 2026, Equator referral (re-using the Phase 12 ODR adapter), borrower portal, feedback
- **Depends on:** 3b, 9, 12
- **Branch:** `feat/grievance-portal`

**Paste into Claude Code:**

```text
Phase 15 — Grievance, borrower portal and feedback. Governing brief: docs/00-master-prompt.md (Part 12, Phase 15; Part 8A prevails on regulatory points).

Build:

- the complaint management system, with automated Internal Ombudsman escalation where applicable, and RB-IOS 2026 support;
- Equator referral, re-using the Phase 12 ODR adapter;
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
- **Depends on:** 0–15 (Phase 14 only for the returns that apply to the pilot's layer)
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

- the DLG ledger (≤ 5% of the amount disbursed out of the covered portfolio, invoked within 120 days overdue);
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

### Phase 17 — Secured products expansion

- **Outcome:** LAP/Home, Vehicle, Gold, LAS/LAMF templates; collateral flows; SARFAESI; repossession and auction
- **Depends on:** P, 12
- **Branch:** `feat/secured-products`
- **Suggested sub-modules (one session each):** LAP/Home; Vehicle; Gold; LAS/LAMF.

**Paste into Claude Code:**

```text
Phase 17 — Secured products expansion. Governing brief: docs/00-master-prompt.md (Part 12, Phase 17; Part 8A prevails on regulatory points).

For each secured product (LAP/Home, Vehicle, Gold, LAS/LAMF):

1. produce the product spec and feasibility notes;
2. implement the collateral workflows (M5), integrations and regulatory checks;
3. build SARFAESI (with the NBFC eligibility gate), repossession and auction, including the gold release, auction, compensation and unclaimed-collateral rules (RBC paras 58–72) and the vehicle repossession clause contents (RBC paras 26–27).

v1.3 regulatory additions for this phase (Part 8A.36.4) — include them:
- Gold conduct module (RBC 43–75), not only paras 60–66; vehicle repossession clause (RBC 26–27) [RBC / WD]

Before writing any code:
1. List the REQ-IDs (Part 8A) and module items (Parts 7, 8A.16 and 8A.36) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-17-secured-products.md: scope, data model changes, APIs and events, state machines, rule-pack parameters, acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/secured-products in small commits; run unit, integration, tenant-isolation and security tests; update the regulatory register, docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Gold-loan LTV, valuation, release, auction and compensation rules match RBC 58–72 and CF 32–50.
- [ ] SARFAESI actions are blocked for tenants that do not meet the eligibility gate.
- [ ] Every charge type is filed with CERSAI (CRM 27–28).
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
| Phase 12 — Recovery and legal (unsecured) + Equator |  |  |  |  |
| Phase 13 — Finance, Ind AS 109 and accounting integrations |  |  |  |  |
| Phase 14 — Regulatory reporting, risk and compliance |  |  |  |  |
| Phase 15 — Grievance, borrower portal and feedback |  |  |  |  |
| Phase P — MVP hardening and pilot go-live |  |  |  |  |
| Phase 16 — Partner connectors, co-lending, loan transfers and securitisation |  |  |  |  |
| Phase 17 — Secured products expansion |  |  |  |  |
| Phase 18 — Analytics, AI layer and MCP |  |  |  |  |
| Phase 19 — Migration tooling |  |  |  |  |
| Phase 20 — Scale hardening and AWS migration |  |  |  |  |

*End of runbook.*
