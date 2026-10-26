# INFRABYX OPERATIONS HUB — Phase-wise Claude Code Runbook

**Companion to the Infrabyx Operations Hub Master Build Prompt v1.0** · 24 October 2026 · ready-to-paste instructions for every build phase

---

## 1. How to use this runbook

1. **Before Session 1:** create the separate `infrabyx-ops-hub` repository; commit the master prompt as `docs/00-master-prompt.md` and the Infrabyx Ecosystem Integration Specification v1.1 as `docs/ecosystem/infrabyx-integration-spec.md`. You can also commit this runbook as `docs/01-phase-runbook.md`.
2. **One phase per session.** Start a fresh Claude Code session for each phase or sub-module and paste only that phase's block.
3. **Approve, then build.** Read the specification, reply "Approved" (or give changes), and let Claude Code build, test and open the pull request.
4. **Run the review gate** under each phase before merging (utility prompt H6).
5. **Large phases:** use the sub-module split. The first session writes and gets approval for the whole-phase specification; later sessions use prompt H1.
6. **Order:** O0 → O1 → O2 → O3 → O4 → O5 → O6 → O7 → O8 → O9 → O10 → O11 → O12 → OP → O13. Finbyx Phase 16e needs O6 at least in staging; Udofin Phase 20b needs O6 for RE invoicing only; Finbyx 20b and Udofin 16c send evidence to O12; Finbyx 16d pins the Labour Code rule pack that O9 releases.
7. **Menus, screens and settings:** every phase builds the menu items, screens and settings in Appendix E; regulatory and legal floors cannot be relaxed.

---

## 2. Standard closing (already included in every block)

```text
Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-<n>-<name>.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch <branch> in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

---

## 3. Phase instructions

### Phase O0 — Repository audit and architecture

- **Outcome:** Inventory of current tools and data; architecture and ADRs; build-versus-buy per module; legal register v1; entity model; event and API boundaries
- **Depends on:** nothing (first phase)
- **Branch:** `docs/oh-repo-baseline`
- **Suggested sub-modules (one session each):** O0a Current-state inventory and data audit; O0b Architecture, ADRs and residency check; O0c Legal register v1 and [VERIFY] map; O0d Build-versus-buy benchmark and Appendix B recommendations.

**Paste into Claude Code:**

```text
Read docs/00-master-prompt.md and docs/ecosystem/infrabyx-integration-spec.md in full, then execute Part 10 (Phase O0 only).

Read docs/00-master-prompt.md in full (Parts 1–10, Appendices A–E, Sources), docs/ecosystem/infrabyx-integration-spec.md (v1.1, canonical) and the tenant-side Parts the Hub serves: Finbyx Parts 7F (GV6, GV7), 7J, 7K and 7L; Udofin Parts 7G and 7H. Inspect the repository, branch, files, Git status and tooling and report them. Do not write application code or modify the repository yet.

First verify, with dated sources: (i) current stable versions and licences of Next.js, NestJS, Node.js 26 LTS, PostgreSQL, Supabase regions, Temporal, GoRules ZEN and CEL; (ii) the India residency position of every candidate sub-processor (Supabase, AWS, Railway, Temporal Cloud, Sentry, Brevo, Razorpay, Microsoft 365 Default Geography and Advanced Data Residency, Google Workspace data regions, GitHub, any LLM endpoint); (iii) Labour Code State rules for Delhi, Uttar Pradesh and Rajasthan and current EPF, ESI, PT and LWF parameters; (iv) the Income-tax Act 2025 salary forms (Form 138, Form 130); (v) which office suite and plan Infrabyx actually holds.

Produce:

0. An inventory of current operational tools and data per legal entity (spreadsheets, CRM and Brevo lists, payroll, Tally Prime or Zoho Books, office-suite tenants, GitHub, support mailboxes, social accounts): owners, volumes, quality, migration needs.
1. The architecture: context, module map OH1–OH14 with data ownership, legal-entity and client scoping (API, service, forced RLS), the grant model and the Equator wall.
2. Technology ADRs, including the rules engine, IdP federation and the residency check per sub-processor.
3. Build-versus-buy per module (for example HubSpot or Zoho CRM, Freshdesk, Keka, greytHR or Razorpay Payroll, Vanta, Drata or Sprinto): cost, residency, integration effort, exit path.
4. The repository structure (Appendix C) and entity model (Appendix D).
5. Event and API boundaries from Part 6, with gaps written as Integration Spec proposals.
6. Legal register v1: every source in Part 4 and in the Sources list with title, number, date and status; every [VERIFY] with the phase that closes it.
7. The roadmap with acceptance criteria and the minimum security, testing and review gates.
8. The Appendix B decisions with your recommendation for each.
9. The navigation map: confirm the sidebar order, the workspace visibility matrix and the settings catalogue defaults and floors of Appendix E, and list any screen or setting you propose to add or drop.

Present all of this for my approval before modifying the repository.

Present everything for my approval before modifying the repository.
```

**Review gate (check before merging):**

- [ ] The inventory lists every current operational tool and dataset per legal entity (CRM and Brevo lists, payroll, Tally Prime or Zoho Books, office-suite tenants, GitHub, support mailboxes, social accounts) with owner, volume and migration need.
- [ ] Every sub-processor has a dated India-residency finding in an ADR; Google Workspace is recorded as having no India data region and Railway as synthetic-data only.
- [ ] Legal register v1 lists every source in Part 4 and the Sources list with title, number, date and status, and maps every [VERIFY] item to the phase that closes it.
- [ ] The architecture shows modules OH1–OH14 with data owners, forced-RLS legal-entity scoping, the grant model and the Equator wall; build-versus-buy is recommended per module.
- [ ] The event and API boundary list uses only canonical Integration Spec v1.1 names; every gap (for example the `oh` source and `CONTRACT_PERFORMANCE_VENDOR` basis) is a written proposal.
- [ ] Every Appendix B decision has a recommendation, and no application code or repository change has been made before approval.
- [ ] The menu map (workspace › module › screen) and the settings catalogue for OH1–OH14 list every setting with level, default and nature (regulatory floor or commercial choice) and are approved before Phase O1.
- [ ] The baseline PR contains only CLAUDE.md, the ADRs and docs/; no application scaffolding.

### Phase O1 — Platform foundation and group identity

- **Outcome:** Monorepo; CI with EO1 rulesets from day one; environments; OIDC federation with MFA; legal-entity register skeleton; application shell (sidebar, Home, global search, notification centre, saved views, entity switcher); design system; observability
- **Depends on:** O0
- **Branch:** `feat/oh-platform-foundation`
- **Suggested sub-modules (one session each):** O1a Monorepo, CI and GitHub rulesets; O1b OIDC federation and MFA; O1c Legal-entity register skeleton and State calendars; O1d Design system, observability and NTP.

**Paste into Claude Code:**

```text
Phase O1 — Platform foundation and group identity. Governing brief: docs/00-master-prompt.md (Part 9, Phase O1; Part 4 legal boundaries prevail).

Verify first: (i) the approved O0 ADRs are merged; (ii) which ruleset, secret-scanning and code-scanning features our GitHub plan includes for private repositories; (iii) the group directory (Entra ID or Google) and the consent it needs.

On branch `feat/oh-platform-foundation` build:

- pnpm + Turborepo, TypeScript strict; `apps/web`, `apps/api`, `apps/worker`; `packages/` contracts (generated from `infrabyx-contracts`), domain-kernel (Money, Rate, BusinessDate, State working-day calendars, IDs), ui (shared tokens), config, observability, testing; Docker Compose for Postgres, Temporal and Gotenberg; `.env.example` only;
- GitHub controls from day one (Part 8.3): rulesets, CODEOWNERS with coverage check, signed commits, required checks, `sensitive-path-approvals`, SHA-pinned Actions, environments with reviewers, nightly ruleset export as evidence;
- OIDC abstraction with federation to the group directory, mandatory MFA and the Integration Spec Part 4.6 claims (`org_id` of the employing entity, `entity_scope[]`, `grant_ids[]`, `acr`, `auth_time`), plus `employee_ref` inside the Hub;
- the OH1 legal-entity register skeleton (legal entities, GSTINs by State, offices, State calendars);
- OpenTelemetry with PII scrubbing; NTP drift alarm; Storybook;
- the application shell of Part 3.5: sidebar in the fixed order with workspace-based visibility (Appendix E.2), Home with My Queue and role tiles (placeholders until each module lands), legal-entity switcher, command palette (`Ctrl+K` or `Cmd+K`), keyboard shortcuts, notification-centre UI, saved-view UI, and the list, detail, wizard, approval-queue, empty-state and error-state components; WCAG 2.2 AA checks (axe) in CI.

Tests and acceptance evidence:

- a direct push, force push or unsigned commit to `main` is rejected and the ruleset export is stored;
- a pull request changing `/.github/` with one code-owner approval fails `sensitive-path-approvals`;
- sign-in without MFA is refused; a single-entity user's token carries only that scope;
- a seeded log line with an email or PAN-like value is scrubbed and the scanner fails the build;
- property tests pass for Money, and the working-day calculator returns the correct second working day after a Friday before a State holiday;
- a user whose workspace lacks a menu does not see it in the sidebar and receives 403 on its route; the axe check passes on every shell screen.

Build no business features. Show me the repository skeleton, ruleset configuration and claim mapping for approval before coding, then open a pull request with the test output.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o1-oh-platform-foundation.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-platform-foundation in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A direct push, force push or unsigned commit to `main` is rejected, and the nightly ruleset JSON export is stored as evidence.
- [ ] A pull request changing `/.github/` with one code-owner approval fails `sensitive-path-approvals`; CODEOWNERS coverage check fails on any unowned module or package file.
- [ ] Sign-in without MFA is refused; a token for a single-entity user carries only that `le_scopes` value.
- [ ] A seeded log line with an email address or PAN-like value is scrubbed, and the PII scanner fails the build on the fixture.
- [ ] Money property tests pass and the working-day calculator returns the correct second working day after a Friday before a State holiday.
- [ ] The navigation shell renders the approved workspace menus by role, passes WCAG 2.2 AA automated checks, and every list screen has an empty and an error state.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O2 — Data model, legal-entity scoping and audit trail

- **Outcome:** Forced RLS; group grants and SoD; Equator wall and case-party block list; hash-chained audit; maker-checker; settings registry; rule-pack framework; claims-gate service v0 (lexicon and empty certification register); outbox and inbox; retention and legal hold (OH1)
- **Depends on:** O1
- **Branch:** `feat/oh-entity-scoping-audit`
- **Suggested sub-modules (one session each):** O2a Identity, grants and SoD model; O2b Forced RLS and isolation tests; O2c Hash-chained audit and maker-checker; O2d Rule-pack framework and shared Labour Code pack loader; O2e Outbox, inbox, schema registry and retention or legal hold.

**Paste into Claude Code:**

```text
Phase O2 — Data model, legal-entity scoping and audit trail. Governing brief: docs/00-master-prompt.md (Part 9, Phase O2; Part 4 legal boundaries prevail).

Verify first: (i) RLS with Supabase transaction pooling and `set_config(…, true)`; (ii) the Integration Spec SDK version and the `oh` source, `group_grant` and data-class ceiling rules (Integration Spec Parts 3.2, 4.6, 13.2); (iii) the rules-engine ADR.

On branch `feat/oh-entity-scoping-audit` create migrations and services for person, employment, user, role, permission, group_grant, purpose_code, sod_conflict_rule, break_glass_record, case_party_block, relationship; legal_entity, office, department, cost_centre, client_org (Integration Spec `org_id`); maker_checker_request, doa_rule, audit_event (hash-chained), outbox, inbox, idempotency, DLQ; setting_definition and setting_value (the settings registry of Part 3.4); notification_type, notification and notification_preference (Appendix E.4); saved_view; search_index_entry; rule_pack_version with the loader and signature check for the shared Labour Code pack; claims_lexicon_entry and an empty certification register (claims-gate service v0: every certification claim blocked until O12); retention_class, legal_hold, disposal_certificate; data-principal requests.

Implement forced RLS on `legal_entity_id`, `client_org_id` and `sensitivity` with the API on a non-owner role; RBAC + ABAC with grants and DoA limits; maker-checker with fresh MFA; the nightly audit-chain verifier and anchor; Integration Spec outbox, inbox, schema, data-class ceiling and forbidden-field validation, Standard Webhooks and RFC 9421; the cross-entity grant workflow of OH1.4 (principal's and target entities' heads and the DPO; ≤ 90 days; SCIM `valid_to`); the Equator wall and wall-breach log; the settings registry with floor enforcement and maker-checker; the notification engine (in-app and email; Teams or Google Chat through OH12 later; mandatory categories cannot be muted); permission-trimmed global search.

- Menus, screens and settings: the `Admin` menu and OH1 settings exactly as the OH1 `Menu and screens` and `Settings and options` tables specify; `Home › Notifications` and `Home › Saved views`.

Tests and acceptance evidence:

- cross-entity and cross-client reads and writes fail; no context returns zero rows;
- a RESTRICTED row is invisible under a CONFIDENTIAL ceiling;
- a maker cannot check their own request; an expired grant stops at `valid_to`;
- a lender-side user cannot be granted an Equator role;
- a direct edit of one audit row is detected by the verifier;
- an inbound event with a forbidden field goes to the DLQ;
- a cross-entity grant lacking the DPO's approval cannot be activated;
- a record under legal hold cannot be disposed of, and a disposal outside hold produces a certificate;
- global search returns no record outside the user's scope and no Equator record to a lender-side user; a query with a PAN-like pattern is refused;
- a setting saved below its floor is refused with the rule shown; a mandatory notification cannot be muted;
- the claims-gate service blocks "ISO 27001 certified" while the certification register is empty.

Show me the entity model, RLS policies, grant workflow and SoD matrix for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o2-oh-entity-scoping-audit.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-entity-scoping-audit in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Cross-entity and cross-client reads and writes fail, and a query without session context returns zero rows on every business table.
- [ ] A RESTRICTED row is invisible under a CONFIDENTIAL grant ceiling; an expired grant stops working at `valid_to`; a cross-entity grant without DPO approval cannot activate.
- [ ] A maker cannot check their own request, and approval without fresh MFA is refused.
- [ ] A user holding a Finbyx or Udofin operator role cannot be granted any Equator role.
- [ ] A direct database edit of one audit row is detected by the nightly hash-chain verifier.
- [ ] An inbound event carrying a forbidden field (loan id, PAN-like value) is rejected to the DLQ with `regulatory-guard`.
- [ ] The settings service stores every setting with level, default, nature and version; a change that relaxes a regulatory floor is refused, and a regulated-configuration change needs maker-checker.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O3 — CRM and marketing consent

- **Outcome:** Open-schema CRM (OH3); consent ledger and send gate; Brevo adapter with exit export
- **Depends on:** O2
- **Branch:** `feat/oh-crm-consent`
- **Suggested sub-modules (one session each):** O3a Open-schema CRM core and custom objects; O3b Consent ledger and send gate; O3c Brevo adapter and exit export; O3d Contact data-principal requests.

**Paste into Claude Code:**

```text
Phase O3 — CRM and marketing consent. Governing brief: docs/00-master-prompt.md (Part 9, Phase O3; Part 4 legal boundaries prevail).

Verify first: (i) my build-versus-buy decision for the CRM (Hub as system of record with Brevo for sending, or Brevo-first); (ii) Brevo's current CRM paths, limits, webhooks, export job and hosting; (iii) TCCCPR 2018 as amended on 12 Feb 2025 (opt-out, 90-day re-consent wait, 140-series, DLT headers and templates) and whether Infrabyx needs its own DLT principal-entity registration; (iv) DPDP notice and consent rules and their commencement.

On branch `feat/oh-crm-consent` build OH3:

- Open schema: organisations linked to the Integration Spec `org_id` (CIN, GSTIN, RBI certificate of registration or other licence, entity type as declared), contacts, leads, opportunities and pipelines per legal entity and product, activities, tasks, partners; custom objects and fields as versioned JSON Schemas with maker-checker; import with dry run, de-duplication and reject file; full signed export (Integration Spec Part 12).
- Consent ledger and send gate (OH3.3–OH3.4): consent by channel and purpose with basis, source, notice version and withdrawal; DND; DLT template ids. A send is refused with a reason unless purpose matches, no opt-out in the last 90 days, DLT header, template and category are valid, promotions carry an opt-out, promotional voice uses the 140-series route, and service messages go only to existing clients.
- Brevo adapter (`CrmMarketingProvider`): two-way sync of B2B contacts and lists, 429 back-off, webhooks to the event store, nightly full export; contacts flagged as a client's borrower, member or employee are refused.
- Equator segregation: Equator's pipeline visible only within Equator; lender-side users cannot see which REs refer cases to Equator.
- Data-principal requests for contacts with retention exceptions.
- Client lifecycle timeline on the client 360 page with the stages, owners, timers and failure paths of OH3.2.
- Menus, screens and settings: the `Clients` and `CRM` menus and OH3 settings exactly as the OH3 `Menu and screens` and `Settings and options` tables specify, including the segment builder with live consent counts, the import wizard and the merge queue.

Tests and acceptance evidence:

- a promotion to a contact who opted out 60 days ago is refused;
- an SMS without a DLT template id is refused;
- a Finbyx sales user cannot open an Equator opportunity by id;
- an import containing a PAN-like column is rejected;
- during a Brevo outage sync queues without loss, and the nightly export reproduces every Hub contact with checksums.

Show me the CRM model, custom-field governance, send-gate rules and Brevo field map for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o3-oh-crm-consent.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-crm-consent in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A promotion to a contact who opted out 60 days earlier is refused with the send-gate reason recorded.
- [ ] An SMS without a DLT template id, or a promotional call not on the 140-series route, is refused.
- [ ] A Finbyx-entity sales user cannot open an Equator opportunity by id.
- [ ] An import file containing a PAN-like column or contacts flagged as a client's borrowers is rejected with a reject file.
- [ ] During a simulated Brevo outage sync queues without loss, and the nightly export reproduces every Hub contact with checksums.
- [ ] The OH3 menus and settings match the approved menu map; a role without CRM rights sees no CRM menu, and a send-gate setting cannot be relaxed below its floor.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O4 — Client onboarding, delivery and migration factory

- **Outcome:** Provisioning orders, gates and `TenantProvisioned` with acknowledgement; implementation projects and milestones; migration factory; exit cases (OH4)
- **Depends on:** O3 (plan refs from the static catalogue until O6)
- **Branch:** `feat/oh-onboarding-delivery`
- **Suggested sub-modules (one session each):** O4a Provisioning orders and contract gates; O4b Implementation projects and milestones; O4c Migration-factory tracking; O4d Exit projects and suite-migration engagements.

**Paste into Claude Code:**

```text
Phase O4 — Client onboarding, delivery and migration factory. Governing brief: docs/00-master-prompt.md (Part 9, Phase O4; Part 4 legal boundaries prevail).

Verify first: (i) the provisioning contract of Integration Spec Part 6.29 (`TenantProvisioned`, `PUT /v1/provisioning-requests/{id}`, `GET /v1/tenants/{tenantid}/provisioning-status`) and each product's implementation of it; (ii) the contract set each product needs before a production RE tenant (Finbyx Part 10.6 items 1 and 13–17, CM5.4; Udofin UP1); (iii) how an RBI certificate of registration, CIN, GSTIN and co-operative registration are verified; (iv) Finbyx DP5 exit turnaround times.

On branch `feat/oh-onboarding-delivery` build OH4:

- Provisioning orders `DRAFT → GATES_PENDING → APPROVED → ACCEPTED → READY → LIVE` (or `REJECTED`, `FAILED`) as OH4.2: sandbox tenants self-served with synthetic data; UAT and production need the signed MSA and DPA with the OUT clause matrix, due-diligence evidence, the client's outsourcing assessment where it applies, a named admin work email, data region and plan; signed `TenantProvisioned`, acknowledgement capture and the fallback poll.
- Implementation projects: templates by product and institution profile (NBFC-BL, NBFC-MFI, HFC, credit co-operative society, co-operative bank, ARC, IFSCA finance company, listed entity), milestones, RACI, RAID log, client sign-off evidence; `ImplementationMilestoneReached` to OH8.
- Migration factory (tracking only): plans, mapping-pack versions, dry-run counts, reconciliation sign-off and cut-over checklists; legacy data is loaded and reconciled inside the product tenant (Finbyx Phase 19), never in the Hub.
- Office-suite migrations for clients as service engagements with the vendors' tools [VERIFY edition limits].
- Exit cases (OH4.6): `ExportRequested` and `ExportCompleted` tracking, turnaround, successor cooperation log, no-erasure-during-transition flag, purge certificate and independent assurance (OUT paras 87, 88, 97(xvi)).
- Menus, screens and settings: the `Onboarding` menu, the client implementation portal and OH4 settings exactly as the OH4 `Menu and screens` and `Settings and options` tables specify.

Tests and acceptance evidence:

- a production order without a DPA reference cannot be approved;
- a milestone accepted twice emits one `ImplementationMilestoneReached`;
- no Hub migration record holds a loan or customer field (schema test);
- an exit case cannot close without a purge certificate and client sign-off;
- a `FAILED` acknowledgement shows its reason code and a resubmission carries a new request id.

Show me the provisioning gates, project templates, exit checklist and screen list for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o4-oh-onboarding-delivery.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-onboarding-delivery in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A production provisioning order without an MSA, DPA or OUT clause-matrix reference cannot be approved; a sandbox order provisions with synthetic data only.
- [ ] `TenantProvisioned` is emitted once per approved order and the product acknowledgement is recorded.
- [ ] A milestone accepted twice emits one `ImplementationMilestoneReached`, which OH8 can bill.
- [ ] No migration record in the Hub contains a loan, customer or member field (schema test).
- [ ] An exit project cannot be closed without `ExportCompleted`, a purge certificate and the client's sign-off.
- [ ] The OH4 provisioning, project and exit screens show the gate checklist with blockers, and the approval queue refuses self-approval.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O5 — Support desk and customer success

- **Outcome:** Tickets with SLAs and DLP; borrower-complaint forwarding; client grievance ladder; knowledge base; health and renewals (OH6, OH5)
- **Depends on:** O3, O4
- **Branch:** `feat/oh-support-success`
- **Suggested sub-modules (one session each):** O5a Ticketing, SLAs and DLP; O5b Borrower-complaint forwarding and client grievance ladder; O5c Knowledge base and service catalogue; O5d Customer success, health scores and renewals.

**Paste into Claude Code:**

```text
Phase O5 — Support desk and customer success. Governing brief: docs/00-master-prompt.md (Part 9, Phase O5; Part 4 legal boundaries prevail).

Verify first: (i) support tiers and SLAs in current client contracts; (ii) the RE grievance-routing rules (CF para 12; OUT paras 54–57; NBFC Internal Ombudsman Directions 2026; RBI Ombudsman Scheme 2026); (iii) incident clocks (OUT para 61; CERT-In Directions) and the `SecurityIncidentNotified` contract.

On branch `feat/oh-support-success` build OH6 and OH5:

- Tickets from in-product help (`POST /v1/support/tickets`), email, portal, phone and Teams; triage queue with AI suggestions and duplicate detection; severity matrix with the four clocks (response, update, workaround, resolution) by tier and business calendar, pause only in `WAITING_ON_CLIENT`, reopen window; escalation to L2, engineering (linked GitHub issue and change id) and management; `SupportTicketOpened`, `SupportTicketResolved`.
- DLP at intake (PAN, Aadhaar, account, card, mobile; attachment OCR); client data stays behind the product deep link.
- Borrower complaints reaching Infrabyx are forwarded to the RE's grievance redressal officer within 1 working day, the complainant is told which RE handles it, and Infrabyx can never mark them resolved.
- Client grievances against Infrabyx: support head → product head → director, with time limits [REC: acknowledge in 1 working day, resolve in 15], root cause, corrective action and OH8 credit notes where agreed.
- Vendor incidents: severity-1 tickets show detection, client-notice (≤ 2 hours) and CERT-In (6 hours) clocks.
- Knowledge base and service catalogue with review dates and the claims gate.
- Customer success: health score from aggregates (usage trend, tickets, SLA breaches, invoice status, module adoption, CSAT or NPS); renewals at 120, 90, 60, 30 and 7 days; success plans, business reviews and churn playbooks.
- Menus, screens and settings: the `Support` and `Success` menus, the client support portal and OH5 and OH6 settings exactly as their `Menu and screens` and `Settings and options` tables specify.

Tests and acceptance evidence:

- a severity-1 response-SLA breach escalates automatically and shows on the client's ticket page;
- an emailed borrower complaint is forwarded to the configured RE officer within 1 working day, its body is purged after acknowledgement, and it cannot be resolved by Infrabyx;
- a Sev 2 ticket in `WAITING_ON_THIRD_PARTY` keeps its clock running and escalates at 50% and 75%;
- a health score recomputes from stored inputs and contains no tenant record ids;
- an article calling a product "SOC 2 certified" without an issued report fails the claims gate.

Show me the SLA matrix, grievance ladder and health-score formula for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o5-oh-support-success.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-support-success in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A severity-1 ticket breaching its response SLA escalates automatically and the breach is visible on the client's ticket page.
- [ ] A ticket containing an Aadhaar-like or PAN-like value is stored redacted and the submitter is told why.
- [ ] An emailed borrower complaint is forwarded to the configured RE grievance officer within 1 working day and cannot be marked resolved by Infrabyx.
- [ ] A client grievance follows the support head, product head, director ladder with time limits and root-cause capture.
- [ ] A health score recomputes exactly from stored inputs and formula version and contains no tenant record ids.
- [ ] The OH6 and OH5 menus match the approved map; the SLA and severity settings are versioned, and a borrower-complaint ticket has no "resolve" action for Infrabyx users.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O6 — Revenue catalogue, billing and Razorpay

- **Outcome:** Signed catalogue; entitlements; usage intake; GST invoices; Razorpay; dunning with regulatory continuity; revenue recognition and review (OH8)
- **Depends on:** O3, O4
- **Branch:** `feat/oh-billing-catalogue`
- **Suggested sub-modules (one session each):** O6a Catalogue, SKUs and legality gate; O6b Subscriptions, entitlements and usage intake; O6c GST invoicing and e-invoice; O6d Razorpay payments, webhooks and reconciliation; O6e Dunning with regulatory continuity; O6f Revenue recognition, books export and revenue-model review.

**Paste into Claude Code:**

```text
Phase O6 — Revenue catalogue, billing and Razorpay. Governing brief: docs/00-master-prompt.md (Part 9, Phase O6; Part 4 legal boundaries prevail).

Verify first: (i) my decisions on merchant of record, plan tiers and SKUs, and AS 9 or Ind AS 115 (Appendix B); (ii) Razorpay's current Orders, Payment Links, Subscriptions, eNACH and Smart Collect APIs, webhook rules, PA authorisation and PCI AoC; (iii) the E-mandate Directions 2026 (RBI/DPSS/2026-27/396); (iv) GST for SaaS and IT services (SAC [VERIFY], IGST Act s.12(2), e-invoicing threshold, LUT for SEZ and IFSC units) and the TDS clients apply to our fees [VERIFY]; (v) the Finbyx CM1–CM5 and Udofin RV1–RV4 contracts.

On branch `feat/oh-billing-catalogue` build OH8:

- Catalogue: products, plans, SKUs mapped to each product's module registry, meters, price books, add-ons, revenue-stream flags with the legality gate (Finbyx CM5.3), explainers checked by the claims gate; JWS-signed versions served by `GET /v1/catalogue/versions/{v}`.
- Subscriptions and entitlements: upgrade immediately, downgrade at term end, renewal, cancellation; signed `PlanChanged` and `EntitlementChanged`; contract tests against the Finbyx CM1.4 regulatory-continuity rule.
- Usage intake: `UsageRecorded` aggregates; 7-day disputes; Udofin B2C aggregates only.
- Invoicing: tax invoices, credit and debit notes (CGST Act s.34), IGST or CGST + SGST, IRN and QR through the IRP above ₹5 crore AATO, LUT zero-rating, Form 131 reconciliation; `InvoiceIssued`.
- Quotes and orders: `POST /v1/billing/quotes` (priced quote and proration preview, valid 7 days) and `POST /v1/billing/orders` (Razorpay-hosted URL for top-level redirect), both with Idempotency-Key; `GET /v1/billing/invoices?tenantid=`; `GET /v1/entitlements?tenant=` daily reconciliation.
- Payments: redirect checkout or Payment Links; Subscriptions with card or UPI AutoPay (no AFA only up to ₹15,000; issuer notice ≥ 24 hours; our notice at T-48 hours); eNACH above that; Smart Collect; raw-body HMAC, event-id de-duplication, order-insensitive upserts, daily settlement reconciliation; `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`.
- Dunning: `ACTIVE → PAST_DUE → RETRY (D+1, D+3, D+7) → GRACE (D+14) → RESTRICTED (D+30, after 7 days' notice) → TERMINATION_NOTICE (D+45) → EXIT`; `SubscriptionCancelled` only when the notice expires; never a hard cancel.
- Revenue recognition schedules, monthly journals to Tally or Zoho Books, intra-group recharges.
- Revenue-model review: MRR, ARR, NRR, churn, ARPA, CAC payback, implementation margin and unit economics by product, stream, market and channel, with switch-on and switch-off scenarios.
- Menus, screens and settings: the `Revenue` menu and OH8 settings exactly as the OH8 `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- every billing golden case in Part 8.2 passes to the paisa;
- a tampered catalogue fails the Finbyx contract test; a SKU naming an unknown module fails import;
- a forged webhook is rejected and a replay changes nothing; a browser-only success leaves the invoice unpaid;
- RESTRICTED sends no entitlement change that would stop a regulated function;
- a stream without an approved legality gate is not published.

Show me the catalogue schema, dunning state machine, GST matrix and revenue rules for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o6-oh-billing-catalogue.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-billing-catalogue in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every billing and revenue-recognition golden case in Part 8.2 passes to the paisa, including IGST versus CGST + SGST and a credit note.
- [ ] A tampered or unsigned catalogue fails the Finbyx CM1.1 contract test; a SKU naming an unknown module fails import.
- [ ] A forged Razorpay webhook is rejected, a replayed one changes nothing, and a browser-only success leaves the invoice unpaid.
- [ ] A ₹18,000 recurring card debit is not set up as a no-AFA mandate, and the T-48-hour courtesy notice is scheduled for every recurring debit.
- [ ] A client at RESTRICTED receives no entitlement change that stops a regulated function (contract test against Finbyx CM1.4), and cancellation occurs only through TERMINATION_NOTICE.
- [ ] A revenue stream without an `ACTIVE` legality gate is not published in the catalogue, and an `ObligationPublished` tagged CF suspends affected streams for new sales only.
- [ ] `POST /v1/billing/quotes` returns price, proration, GST and entitlement diff; ordering an expired quote through `POST /v1/billing/orders` returns `quote-expired`; a quote above the requester's discount limit routes for approval.
- [ ] A `UsageRecorded` replay with the same `statement_version` counts once; a payload carrying a subscriber key or loan id is rejected; a `REVENUE_AGGREGATE` statement never produces an invoice.
- [ ] The `Revenue › Catalogue`, `Plans`, `Quotes`, `Subscriptions`, `Invoices`, `Collections` and `Revenue review` screens and the OH8 settings exist with role visibility tests; the deny list and the regulatory-continuity rule have no setting.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O7 — Marketing, brand, social media and PR

- **Outcome:** Brand library; content queue with claims gate; campaigns; social publishing; PR and collaborations (OH7)
- **Depends on:** O3, O5
- **Branch:** `feat/oh-marketing-brand`
- **Suggested sub-modules (one session each):** O7a Brand library and content queue with claims gate; O7b Campaigns, landing pages and self-serve funnel; O7c Social publishing and listening; O7d PR and collaborations register.

**Paste into Claude Code:**

```text
Phase O7 — Marketing, brand, social media and PR. Governing brief: docs/00-master-prompt.md (Part 9, Phase O7; Part 4 legal boundaries prevail).

Verify first: (i) the platforms I chose and each one's publishing API terms; (ii) the ASCI Code, the CCPA Dark Patterns Guidelines 2023 and any rule on advertising software for regulated entities [VERIFY]; (iii) BCI Rule 36 for anything mentioning advocates; (iv) the rule that Equator is never presented as the default ODR for Finbyx or Udofin clients.

On branch `feat/oh-marketing-brand` build OH7:

- Brand library per entity and product with licences and expiry.
- Content queue: drafts, marketing, legal and product review, maker-checker, scheduled publishing via `SocialPublisher`; the claims gate blocks "certified", "guaranteed compliance", "RBI approved" and similar claims without an OH14 record; no fake scarcity, countdown timers, inflated value figures or unverifiable testimonials.
- Campaigns: consent-based segments, Brevo sending, UTM tracking, landing pages with consent capture and DPDP notices, webinars with disclosures; leads routed to OH3 with SLA.
- Legitimate self-serve funnel: sandbox trial with synthetic data, activation checklist and nurture, with the O4 production gate (Finbyx CM5.4).
- PR and collaborations register: coverage, releases, events, sponsorships, MoUs with obligations and conflict checks (Equator neutrality; auditor independence where a group company audits a client).
- Social listening and responses: aggregate mentions and post metrics only; complaints raised on social channels are routed to OH6 within 1 working day.
- Workflows: campaign approval with the audience freeze and send-time consent re-check (OH7.2), the press-release and collaboration pipelines (OH7.7), using the claims-gate service from O2.
- Menus, screens and settings: the `Marketing` menu and OH7 settings exactly as the OH7 `Menu and screens` and `Settings and options` tables specify.

Tests and acceptance evidence:

- a post claiming "ISO 27001 certified" without a certificate record cannot be approved;
- a segment cannot include a contact without matching consent;
- a lender-side campaign naming Equator as ODR partner is blocked for legal review;
- a retried platform callback does not publish twice;
- a contact who withdraws consent after the audience freeze is excluded at send time.

Show me the approval chain, claims lexicon and campaign model for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o7-oh-marketing-brand.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-marketing-brand in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A post or page claiming "ISO 27001 certified" or "SOC 2 certified" without an OH14 certificate record cannot be approved.
- [ ] A campaign segment cannot include a contact without a matching marketing consent.
- [ ] Countdown timers, scarcity banners or unverifiable testimonials are rejected by the content checks.
- [ ] A lender-side campaign naming Equator as the ODR partner is blocked for legal review.
- [ ] A retried platform callback does not publish a scheduled post twice.
- [ ] The OH7 menus and settings match the approved map, and every publish action calls the claims gate before scheduling.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O8 — Professional and advocate directory

- **Outcome:** Rule 36 public listing; empanelment and verification; allocation feed; conflict register and the Equator conflict-check API (OH9, OH1.6)
- **Depends on:** O2
- **Branch:** `feat/oh-directory`
- **Suggested sub-modules (one session each):** O8a Professional records and verification; O8b Public Rule 36 listing and feeds; O8c Conflict register and allocation-count reporting.

**Paste into Claude Code:**

```text
Phase O8 — Professional and advocate directory. Governing brief: docs/00-master-prompt.md (Part 9, Phase O8; Part 4 legal boundaries prevail).

Verify first: (i) BCI Rule 36, the 2008 proviso (Resolution 50/2008) and its Schedule of permitted website information, *P.N. Vignesh* (Madras HC, 2024) and the BCI notices of 6 Jul 2024; (ii) verification sources per professional type (State Bar Council enrolment, ICAI and ICSI certificates of practice, IBBI registration, valuer registration) [VERIFY access]; (iii) the Finbyx R11 rules that consume the directory; (iv) the public-listing scope I chose (Appendix B decision 8).

On branch `feat/oh-directory` build OH9:

- Professional record: type (advocate, chartered accountant, company secretary, cost accountant, insolvency professional, registered valuer, mediator), verification evidence, jurisdictions, forums, practice areas, languages, listing consent, notice version.
- States as OH9.2 (`INVITED` or `APPLIED` → … → `EMPANELLED → ACTIVE`, `ANNUAL_REVIEW`, `SUSPENDED`, `LAPSED`, `REMOVED`, `WITHDRAWN`); public listing only for `ACTIVE` professionals with listing consent; `ProfessionalEmpanelled` on `EMPANELLED` and on each new version; `ProfessionalSuspended` (`suspension_seq`) on suspension, lapse or removal.
- Public listing, Rule 36 Schedule fields only: name, address, contacts, enrolment number and State Bar Council, enrolment date, qualifications, practice areas. No ratings, reviews, "top" or "premium" badges, success rates, fees, testimonials or paid placement; neutral ordering (alphabetical or logged seeded random); the same on every group website.
- RE panels stay in Finbyx R11: the RE decides empanelment, fees and allocation; the Hub receives `MatterAllocated` (status and `update_seq`, no party, matter or loan identifiers) only for rotation-fairness, concentration and conflict-count reports.
- Equator conflict-check API `POST /v1/conflicts/check` (OH1.6): counts and flags only, default window `P3Y`, every call logged.
- Conflict register: relationships with group companies, REs and Equator; Equator neutrals flagged (`equator_neutral`) so R11 can block them as counsel in related matters. Performance scorecards live only in each RE's tenant.
- Menus, screens and settings: the `Directory` menu, the professional portal and OH9 settings exactly as the OH9 `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- the public API exposes only Schedule fields and offers no sort other than neutral ordering;
- adding a "featured" flag or paid-listing SKU fails the catalogue and claims checks;
- a suspended advocate leaves the public feed within 1 hour and R11 receives `ProfessionalSuspended`;
- a `MatterAllocated` payload with a borrower name is rejected; a status change with a lower `update_seq` is ignored;
- the conflict API returns only the allocation count, flag, category and `as_of`.

Show me the listing fields, verification sources and state machine for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o8-oh-directory.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-directory in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] The public directory API exposes only BCI Rule 36 Schedule fields and offers no ordering other than alphabetical or logged seeded random.
- [ ] Adding a "featured" flag, rating, fee or paid-listing SKU fails the catalogue and claims checks.
- [ ] A suspended professional leaves the public feed within 1 hour and Finbyx R11 receives `ProfessionalSuspended`.
- [ ] A `MatterAllocated` payload containing a borrower or party name, a matter number or a loan identifier is rejected; a status update with a lower `update_seq` is ignored.
- [ ] Annual review is scheduled for every `ACTIVE` professional, a lapsed credential moves the professional to `SUSPENDED`, and a credential mismatch returns the application to `RETURNED` with reasons.
- [ ] The `Directory › Professionals`, `Empanelment` and `Allocations` screens and the OH9 settings exist; no setting can add a public field, a ranking sort or a fee.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O9 — Staff HRMS and payroll

- **Outcome:** Hire-to-retire; attendance and WFH; leave; Labour Code payroll with the shared rule pack (first signed release 1.0); statutory filing packs; appraisals (OH10)
- **Depends on:** O2
- **Branch:** `feat/oh-hrms-payroll`
- **Suggested sub-modules (one session each):** O9a Hire-to-retire, appointment letters and email identities; O9b Attendance, WFH and leave; O9c Payroll engine on the shared Labour Code rule pack; O9d F&F, gratuity and statutory filing packs; O9e Performance, learning and POSH registers.

**Paste into Claude Code:**

```text
Phase O9 — Staff HRMS and payroll. Governing brief: docs/00-master-prompt.md (Part 9, Phase O9; Part 4 legal boundaries prevail).

Verify first and record in the legal register: (i) the four Labour Codes (in force 21 Nov 2025) and Central Rules of 8 May 2026 (G.S.R. 342(E)–345(E); corrigendum G.S.R. 629(E) of 15 Jul 2026); (ii) State rules, Shops and Establishments changes, minimum wages, PT and LWF for Delhi, Uttar Pradesh, Rajasthan and any other State where we employ staff [VERIFY each]; (iii) EPF, ESI, gratuity, maternity and POSH thresholds by headcount per office; (iv) Income-tax Act 2025 salary TDS (s.392, Form 138, Form 130) and the Form 12BB equivalent; (v) my decisions on payroll in-house or provider and on WFH (Appendix B).

On branch `feat/oh-hrms-payroll` build OH10 on the shared, signed Labour Code rule pack `infrabyx-labour-rulepack` (Integration Spec Part 12.3), publishing its first signed release 1.0 with golden fixtures that Finbyx GV6 also runs:

- Hire-to-retire from requisition to archive, with appointment letters tagging wage components by CoW class and a WFH clause, backfill letters for existing staff, email addresses `first.last@[entity domain]` with collision rules, reserved names, 90-day quarantine and no reissue; `EmployeeOnboarded`, `EmployeeOffboarded` (oh scope).
- Attendance and WFH: SSO sign-in and sign-out, timesheets by project or ticket, regularisation; no activity, screen, webcam or off-duty location monitoring; employee notice and self-view.
- Leave (OSHWC s.32 and policy) with office holiday calendars.
- Payroll: CoW wages with the 50% add-back; EPF, ESI, PT, LWF, TDS projection; overtime with consent and the 144-hour quarterly cap; minimum-wage block; deduction cap with carry-forward; Form V payslips by pay day; Forms I, IV and IX kept 5 years; variance report (± 10% per head, new bank accounts); HR prepares, finance releases, no one approves their own line; bank file by `PayoutFileProvider`.
- F&F timers: wages and encashment by LWD + 2 working days, gratuity within 30 days, service certificate within 10 days, never waiting for clearance.
- Guided statutory packs: ECR, ESIC, PT, LWF, Form 138 data and Form 130, with acknowledgement capture and no stored credentials.
- Performance and learning (goals, appraisal and calibration, training records feeding OH14) and POSH (Internal Committee per office of 10 or more, restricted case register, annual report data).
- Menus, screens and settings: the `People` menu (employee self-service, manager, HR and payroll screens; POSH visible only to the Committee) and OH10 settings exactly as the OH10 `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- every payroll golden case in Part 8.2 passes to the paisa;
- a run with anyone below the State minimum wage is blocked; overtime beyond 144 hours a quarter is refused;
- a resignation with clearance pending still schedules F&F wages for LWD + 2 working days;
- two synthetic parallel cycles reconcile line by line with the finance reviewer's independent model;
- no non-HR, non-manager user can see another employee's salary.

Show me the rule-pack parameters, state machines, payslip and register layouts for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o9-oh-hrms-payroll.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-hrms-payroll in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Every payroll golden case passes to the paisa, including the ₹76,000 → ₹22,000 wages example, gratuity and leave accrual.
- [ ] A payroll run with any employee below the State minimum wage is blocked, and overtime beyond 144 hours a quarter or without consent is refused.
- [ ] A resignation with clearance pending still schedules F&F wages for LWD + 2 working days, and no notice-pay recovery is deducted.
- [ ] The payroll preparer cannot release the bank file, and no one can approve their own pay line.
- [ ] Statutory packs (ECR, ESIC, Form 138 data, Form 130) validate and capture acknowledgements without storing any portal credential.
- [ ] No attendance feature records keystrokes, screenshots, webcam or off-duty location (privacy test), and no non-HR, non-manager user can see another employee's salary.
- [ ] A run cannot leave `CALCULATED` while any variance (±10% per head, bank change, override, negative pay) lacks a cleared reason, and a calibration change without a reason cannot be saved.
- [ ] The `People › Directory`, `Hiring`, `Onboarding`, `Leave`, `Attendance and WFH`, `Payroll`, `Appraisal` and `Exits` screens and the OH10 settings exist; no setting enables prohibited monitoring.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O10 — Internal controls and anti-fraud

- **Outcome:** DoA; SoD; vendor master; expenses; ghost-employee tests; access reviews; whistle-blower channel; staff ROI (OH11)
- **Depends on:** O6, O9
- **Branch:** `feat/oh-controls-antifraud`
- **Suggested sub-modules (one session each):** O10a DoA and SoD enforcement; O10b Vendor master and payments controls; O10c Expenses, purchase requests and petty cash; O10d Integrity tests and access reviews; O10e Whistle-blower channel, ROI metrics and cost allocation.

**Paste into Claude Code:**

```text
Phase O10 — Internal controls and anti-fraud. Governing brief: docs/00-master-prompt.md (Part 9, Phase O10; Part 4 legal boundaries prevail).

Verify first: (i) Companies Act 2013 s.177(9) with rule 7 of the Meetings of Board Rules 2014 and whether any group company meets the mandatory vigil-mechanism thresholds (otherwise adopt it voluntarily); (ii) internal financial controls reporting (s.134(5)(e), s.143(3)(i)); (iii) Model Standing Orders 2026 misconduct heads on false claims and unauthorised IT access; (iv) my DoA limits (OH11.1 defaults).

On branch `feat/oh-controls-antifraud` build OH11:

- DoA per entity and transaction type, routing upward above a limit, every decision with a reason code.
- SoD at grant: vendor creation versus payment release; employee creation versus payroll approval; bank-detail change versus payment release; user administration versus finance roles; exceptions need a director and expire.
- Vendor master: PAN and GSTIN checks; penny-drop name match ≥ 85%; duplicate PAN, account, phone or address; bank-detail change needs a call-back and a 48-hour hold; dormant 12 months blocked.
- Expenses, purchase requests and petty cash: receipt OCR and hash; duplicates; split claims within 7 days; mileage against route distance; weekend flags; cost-centre budgets.
- Monthly ghost-employee tests: shared bank accounts, pay with no sign-in for 30 days, duplicate PAN, no appointment letter or manager, pay after exit, missing UAN.
- Access reviews: privileged quarterly, others half-yearly across the Hub, office suite, GitHub, product staff consoles, cloud and finance tools; revoke after 14 days unattested; `AccessReviewCompleted`.
- Whistle-blower channel to the Audit Committee chair or nominated director: `RECEIVED → TRIAGED → INVESTIGATING → FINDINGS → ACTION → CLOSED`; anti-retaliation second review for 12 months; restricted files.
- Staff ROI (team level): revenue per employee, utilisation, cost per ticket, implementation margin, CAC payback; never the sole basis for discipline. Intra-group cost sharing by acting entity, invoiced through OH8.
- Menus, screens and settings: the `Controls` menu (whistle-blower visible only to the designated recipient) and OH11 settings exactly as the OH11 `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- vendor-create plus payment-release on one user is refused without a time-limited director exception;
- a payment to a vendor account changed less than 48 hours earlier is blocked;
- two ₹4,900 claims from one person and merchant within 7 days against a ₹5,000 limit are flagged;
- a seeded ghost employee appears on the monthly exception report;
- a whistle-blower's identity is hidden from everyone but the designated recipient, administrators included.

Show me the DoA defaults, SoD matrix, exception rules and whistle-blower policy draft for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o10-oh-controls-antifraud.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-controls-antifraud in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Granting one user both vendor creation and payment release is refused without a time-limited director exception.
- [ ] A payment to a vendor bank account changed less than 48 hours earlier, or without call-back evidence, is blocked.
- [ ] Two ₹4,900 claims by one person at one merchant within 7 days against a ₹5,000 limit are flagged as a split claim.
- [ ] A seeded ghost employee (shared bank account, no sign-in for 30 days) appears on the monthly exception report.
- [ ] Access unattested 14 days after a review campaign closes is revoked and `AccessReviewCompleted` is emitted.
- [ ] A whistle-blower's identity is hidden from everyone except the designated recipient, including system administrators.
- [ ] The `Controls › DoA`, `Maker-checker queue`, `Access reviews` and `Whistle-blower` screens and the OH11 settings exist; a setting that removes an SoD conflict needs the CFO and CISO.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O11 — Workplace integration (Microsoft 365 / Google Workspace)

- **Outcome:** One `WorkplaceProvider`; joiner, mover, leaver; `MailboxProvisioned`; document management; migration runbooks (OH12)
- **Depends on:** O1, O9
- **Branch:** `feat/oh-workplace`
- **Suggested sub-modules (one session each):** O11a WorkplaceProvider and Microsoft 365 adapter; O11b Google Workspace adapter; O11c Joiner, mover and leaver automation; O11d Document links, retention and licence pool.

**Paste into Claude Code:**

```text
Phase O11 — Workplace integration (Microsoft 365 / Google Workspace). Governing brief: docs/00-master-prompt.md (Part 9, Phase O11; Part 4 legal boundaries prevail).

Verify first: (i) the suite and plan each legal entity holds and the Microsoft 365 Default Geography; (ii) the Graph permissions (`User.ReadWrite.All`, `LicenseAssignment.ReadWrite.All`, `Group.ReadWrite.All`, `Sites.Selected`, Teams and any protected APIs) and Google delegation scopes; (iii) change-notification lifetimes; (iv) whether Advanced Data Residency is needed.

On branch `feat/oh-workplace` build OH12:

- one `WorkplaceProvider` with Microsoft 365 and Google adapters, mock first, then a developer tenant with synthetic users;
- joiner: user disabled until D-1 with `usageLocation` IN, licence from the pool, groups, Teams and drives by role template, `MailboxProvisioned`, idempotent on (employee, provider, action); mover: group and licence changes, cross-entity moves through the grant workflow;
- leaver at 18:00 on the LWD: revoke sessions or suspend, block sign-in, shared or forwarded mailbox for 90 days, drive ownership to the manager, retention hold, then licence removal; address quarantined 90 days;
- delta sync and change notifications renewed at 80% of lifetime, resync on `reauthorizationRequired` or `missed`; Google watch channels renewed before expiry;
- document links to SharePoint or OneDrive via `Sites.Selected` with retention labels and holds; RESTRICTED HR documents stay in the Hub store; no client regulated data in either suite and no RE or borrower data in Google Workspace;
- licence pool by entity, idle seats reclaimed after 30 days with manager confirmation; staff and client migration runbooks;
- DLP that keeps Google Workspace to non-regulated data only (no files with personal data, books of account, returns, loan or HR data);
- Menus, screens and settings: the `Workplace` menu and OH12 settings exactly as the OH12 `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- in the sandbox tenant a leaver's sessions are revoked and sign-in blocked by 18:00 on the LWD, with evidence;
- re-running a joiner creates no second user or licence;
- an expired subscription is detected and a delta resync restores state;
- storing a RESTRICTED HR document, or any file flagged as containing personal data, in Google Drive is refused.

Show me the permission set, role templates and leaver runbook for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o11-oh-workplace.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-workplace in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] In the sandbox tenant a leaver's sessions are revoked and sign-in blocked by 18:00 on the LWD, with evidence captured.
- [ ] Re-running a joiner workflow creates no second user, mailbox or licence, and `MailboxProvisioned` is emitted once.
- [ ] An expired change-notification subscription is detected and a delta resync restores state.
- [ ] Any write of personal, HR, books, returns or loan data to Google Workspace, or of RESTRICTED data to Microsoft 365 outside India, is refused with `residency-blocked`, with no override even with a DPO risk acceptance.
- [ ] A released email address stays quarantined for 90 days and is never reissued to another person.
- [ ] The `Workplace › Mailboxes`, `Groups`, `Sites` and `Migration` screens and the OH12 settings exist; a data-class setting can narrow but never widen the OH12.1 matrix.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O12 — Engineering-operations console and certification readiness

- **Outcome:** Cross-product release, change (CAB and `ChangeApproved`), patch, VAPT, backup and incident console; control framework; evidence collectors; full claims gate and certification register; auditor portal (OH13, OH14)
- **Depends on:** O2, O10, O11
- **Branch:** `feat/oh-engops-controls`
- **Suggested sub-modules (one session each):** O12a Engineering-operations console; O12b Incident console and clocks; O12c Control library, mappings and evidence collectors; O12d Claims gate, readiness dashboard and auditor workspace.

**Paste into Claude Code:**

```text
Phase O12 — Engineering-operations console and certification readiness. Governing brief: docs/00-master-prompt.md (Part 9, Phase O12; Part 4 legal boundaries prevail).

Verify first: (i) the Finbyx EO1–EO5 and Udofin RA4 evidence contracts; (ii) the GitHub APIs for rulesets, alerts, environments and members on our plan; (iii) current editions of ISO/IEC 27001:2022 (Amendment 1:2024), 27701:2025, ISO 22301:2019, ISO/IEC 42001:2023, the AICPA Trust Services Criteria (2017, 2022 points of focus) and PCI DSS v4.0.1 SAQ A; (iv) CERT-In reporting and log rules; (v) my certification order, certification body and CPA firm.

On branch `feat/oh-engops-controls` build OH13 and OH14:

- Console (OH13) per product and environment: releases, CAB records and freeze windows, vulnerability board with patch clocks (critical or KEV 72 hours, high 7 days, medium 30, low 90), VAPT register (VA 6-monthly, PT yearly, independent testers, retests), backup and DR drills, escrow deposits and CYB para 106 certificates for products serving REs, connector certification, and the incident console with detection, client-notice (≤ 2 hours), CERT-In (6 hours) and DPDP clocks.
- Control library (OH14): controls with owner, frequency, test, automation hook and many-to-many mappings (ISO/IEC 27001 Annex A, 27701, 22301, SOC 2 TSC, PCI SAQ A, CERT-In, DPDP, internal financial controls; CYB, OUT and CF for product controls); evidence with hash, period, reviewer and freshness; collectors for GitHub rulesets, MFA and sign-in reports, access reviews, restore tests, VAPT, patch SLAs, joiner and leaver records, training and vendor due diligence.
- Claims gate service for OH7, product explainers and websites: "aligned to" or "in progress" until a report or certificate exists; then scheme, scope, period or number, issuer and date.
- Readiness dashboard, auditor workspace (time-boxed `PROVIDER_ASSURANCE` grants with `ExternalAccess*` events; Hub evidence only) and policy library with attestations (`PolicyAttested` to LawDocsComply in group mode).
- CAB and deployment gate: `ChangeApproved` (OH13 → product deployment gates) for every production change; patch clocks per Part 8.3 on every group repository.
- Menus, screens and settings: the `Engineering` and `Trust` menus and OH13 and OH14 settings exactly as their `Menu and screens` and `Settings and options` subsections specify.

Tests and acceptance evidence:

- a release without an approved change record raises an OH14 exception within 1 hour;
- a critical vulnerability open beyond 72 hours turns red and notifies the CISO;
- a VA older than 6 months or PT older than 12 months is flagged 30 days ahead;
- every control has an owner, a mapping and a collector or manual procedure;
- website text claiming a certification without a record fails the claims gate.

Show me the control framework, mappings, collectors and console layout for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o12-oh-engops-controls.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-engops-controls in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A production release in any product without an approved change record raises an OH14 exception within 1 hour.
- [ ] A critical or KEV-listed vulnerability on any group repository, the Hub included, turns red after 72 hours and notifies the CISO; high, medium and low findings carry 7, 30 and 90 days, and internal or tenant audit findings 15, 30, 90 and 180 days.
- [ ] A VA report older than 6 months or a PT report older than 12 months is flagged 30 days before expiry.
- [ ] Every control in the framework has an owner, at least one mapping and a collector or documented manual procedure.
- [ ] Website or product text claiming a certification without a certificate record fails the claims-gate API.
- [ ] An incident drill records detection, client-notice (≤ 2 hours) and CERT-In (6 hours) clocks and flags any missed clock.
- [ ] `ChangeApproved` carries class `STANDARD`, `NORMAL`, `REGULATED` or `EMERGENCY`, and a `REGULATED` change without a compliance reviewer and golden-case pass cannot be approved.
- [ ] The `Engineering › Releases`, `Changes`, `Vulnerabilities`, `VAPT`, `Backups`, `Incidents` and `Status page` and `Trust › Controls`, `Evidence`, `Audits` and `Policies` screens and the OH13 and OH14 settings exist; no setting relaxes a platform patch SLA.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase OP — Hub go-live

- **Outcome:** VAPT, restore drill, residency check, parallel payroll and billing, migration and cut-over
- **Depends on:** O1–O12 (O7, O8 may follow by owner decision)
- **Branch:** `release/oh-go-live`
- **Suggested sub-modules (one session each):** OP-a VAPT and remediation; OP-b Restore and DR drill; OP-c Parallel payroll and billing runs; OP-d Data migration and cut-over plan.

**Paste into Claude Code:**

```text
Phase OP — Hub go-live. Governing brief: docs/00-master-prompt.md (Part 9, Phase OP; Part 4 legal boundaries prevail).

Verify first: (i) every Appendix B decision the live modules depend on is recorded; (ii) production and every sub-processor pass the India residency check; (iii) notices for staff, candidates, contacts and professionals are approved; (iv) the HR, WFH, DoA, anti-fraud, expenses, whistle-blower and POSH policies the modules enforce are approved.

Deliver: E2E regression across O1–O12, including every screen, empty and error state and setting in Appendix E and an independent WCAG 2.2 AA audit of client-facing and self-service screens; independent VA and PT by a CERT-In-empanelled firm with Critical and High findings closed and retested; a restore drill of database, documents and Temporal state with RTO and RPO measured; two parallel payroll cycles on real data reconciled line by line with the current payroll and signed off by the finance reviewer; one parallel billing cycle reconciled with current invoices and the books, plus a live Razorpay test invoice paid and refunded; CRM migration with consent provenance (unprovable consent imported as service-only); employee master migration with a reject file; SCIM and leaver automation proven on a real test account; runbooks, on-call rota and a cut-over plan with rollback.

Tests and acceptance evidence:

- VAPT closure and retest report;
- restore-drill report with measured RTO and RPO;
- a leaver drill on a real test account showing sessions revoked and product accounts removed within the 4-hour SCIM limit;
- signed payroll and billing reconciliations;
- residency and migration reconciliation reports;
- the go-live checklist with every item evidenced.

Show me the go-live checklist for approval. Do not deploy, send any real payslip, invoice or campaign, or switch off an existing system without my explicit authorisation.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-op-oh-go-live.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch release/oh-go-live in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] Independent VA and PT by a CERT-In-empanelled firm have all Critical and High findings closed and retested.
- [ ] A restore drill of database, documents and Temporal state into an isolated India-region environment meets the RTO and RPO targets.
- [ ] Two parallel payroll cycles reconcile line by line with the existing payroll, signed off by the finance reviewer.
- [ ] One parallel billing cycle reconciles with existing invoices and the books, and a live Razorpay test invoice is paid and refunded.
- [ ] The residency report confirms production and every sub-processor holding personal data are in India.
- [ ] The go-live checklist is fully evidenced and approved before any real payslip, invoice or campaign is sent.
- [ ] User acceptance on every module's menus and settings is signed off by its business owner, with the settings export reviewed against the approved catalogue.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

### Phase O13 — Dashboards, analytics and AI assistance

- **Outcome:** Governed metric layer behind the Home tiles and dashboards, leadership packs (OH2); governed AI assistance; read-only MCP server
- **Depends on:** OP
- **Branch:** `feat/oh-analytics-ai`
- **Suggested sub-modules (one session each):** O13a Metric layer and role dashboards; O13b Group and Board packs; O13c Governed AI assistance; O13d Read-only MCP server.

**Paste into Claude Code:**

```text
Phase O13 — Dashboards, analytics and AI assistance. Governing brief: docs/00-master-prompt.md (Part 9, Phase O13; Part 4 legal boundaries prevail).

Verify first: (i) the metric definitions I approve; (ii) the India-region LLM endpoint chosen by ADR and its processing terms; (iii) the AI-use policy approved in OP; (iv) the Part 6.4 rules that cross-entity views are aggregates and Equator data is never joined with lender-side data.

On branch `feat/oh-analytics-ai` build:

- Metric layer (OH2): versioned definitions (formula, grain, entity scope, owner, sensitivity) in SQL views under RLS; every tile links to its definition.
- Role dashboards: the Home tiles of Part 3.5 and the OH2.2 catalogue rebuilt on governed metrics (Superset with row-level security), plus leadership and Board packs. Individual metrics only to the employee and manager; group views aggregate-only.
- Menus, screens and settings: `Home`, `Home › Dashboards`, `Home › Leadership packs` and `Admin › Metrics` and OH2 settings exactly as the OH2 `Menu and screens` and `Settings and options` tables specify.
- AI assistance with human approval: ticket triage and replies citing the knowledge base; CRM and proposal drafts; consented meeting summaries; contract and RFP clause extraction; dashboard narratives. Prohibited: approving pay, payments, expenses or discounts; hiring, appraisal, discipline or termination decisions; employee monitoring; closing client grievances; publishing without maker-checker; any client regulated data.
- Governance: AI inventory, model and prompt versions, logs without personal data where possible, opt-in per workflow with pause and rollback, monthly quality review; read-only MCP server over aggregate metrics and knowledge-base content.

Tests and acceptance evidence:

- a group dashboard cannot drill into another entity's records;
- no dashboard places Equator case data beside a lender's revenue;
- an AI draft cannot be sent without a human action, and the log records model and prompt versions;
- a PAN-like value is redacted before reaching the model;
- each metric value recomputes from its stored definition version, and a Board pack shows only approved, versioned metrics.

Show me the metric catalogue, wireframes and AI use-case register for approval before coding.

Before writing any code:
1. List the module items (Parts 5 and 6), legal boundaries (Part 4) and integration contracts (Integration Spec) this phase implements, and any [VERIFY] items it must resolve.
2. Write the specification to docs/specs/phase-o13-oh-analytics-ai.md: scope, data model changes, APIs and events, state machines, menus, screens and settings (Appendix E), acceptance criteria and test plan (including golden cases).
3. Stop and wait for my approval.
After approval: build on branch feat/oh-analytics-ai in small commits; run unit, integration, legal-entity isolation and security tests; update docs/status and the ADRs; open a PR with the test output pasted. Never claim a test passed unless you ran it.
```

**Review gate (check before merging):**

- [ ] A group dashboard cannot drill into another legal entity's records, and no view places Equator case data beside a lender's revenue.
- [ ] Every dashboard tile links to a versioned metric definition, and each value recomputes from it.
- [ ] An AI-drafted reply cannot be sent without a human action, and the log records model and prompt versions.
- [ ] A PAN-like value in an AI request is redacted before reaching the model, and the endpoint is India-hosted per the ADR.
- [ ] No AI workflow can approve pay, payments, expenses or discounts, or decide hiring, appraisal or discipline (negative tests).
- [ ] Each role dashboard appears only in its workspace menu, and each AI-assisted workflow has an on or off setting per workflow, default off.
- [ ] The PR shows the test output; legal-entity isolation tests pass; docs/status and the ADRs are updated.

---

## 4. Utility prompts

Replace the text in square brackets before pasting.

| No. | When to use | Prompt |
|---|---|---|
| H1 | Start a sub-module | Continue Phase [n]. This session covers only the sub-module: [name]. Re-read the approved spec docs/specs/[file].md, confirm the scope in five lines, then build it. Do not touch other sub-modules. |
| H2 | Resume after an interruption | Read CLAUDE.md, docs/status and the open PR for Phase [n]. Summarise what is done, what is pending and any failing tests, then continue from the next pending item. |
| H3 | Status check | Give me a status report for Phase [n]: items done, items pending, tests run and results, open [VERIFY] items and decisions you need from me. Do not write code. |
| H4 | Fix failing tests | The following tests fail: [paste output]. Find the root cause, explain it in plain English, propose the fix and apply it only after I approve. Re-run the full suite and paste the results. |
| H5 | Law or vendor change | I have added [instrument or vendor notice, date] to docs/regulations/. Read it in full, list every affected module, rule pack, setting and test, and propose changes with effective dates. Do not change code until I approve. |
| H6 | Run the review gate | Run the review gate for Phase [n] from docs/01-phase-runbook.md. For each item show the evidence (test name and output, query result, screenshot or file path). Mark any item you cannot evidence as NOT MET. |
| H7 | Change a specification | I want to change the approved spec for Phase [n]: [change]. Update docs/specs/[file].md, list the legal, data and billing impact, update the tests, and wait for my approval before changing code. |

---

## 5. Progress tracker

| Phase | Spec approved (date) | PR | Review gate passed (date) | Notes |
|---|---|---|---|---|
| Phase O0 — Repository audit and architecture |  |  |  |  |
| Phase O1 — Platform foundation and group identity |  |  |  |  |
| Phase O2 — Data model, legal-entity scoping and audit trail |  |  |  |  |
| Phase O3 — CRM and marketing consent |  |  |  |  |
| Phase O4 — Client onboarding, delivery and migration factory |  |  |  |  |
| Phase O5 — Support desk and customer success |  |  |  |  |
| Phase O6 — Revenue catalogue, billing and Razorpay |  |  |  |  |
| Phase O7 — Marketing, brand, social media and PR |  |  |  |  |
| Phase O8 — Professional and advocate directory |  |  |  |  |
| Phase O9 — Staff HRMS and payroll |  |  |  |  |
| Phase O10 — Internal controls and anti-fraud |  |  |  |  |
| Phase O11 — Workplace integration (Microsoft 365 / Google Workspace) |  |  |  |  |
| Phase O12 — Engineering-operations console and certification readiness |  |  |  |  |
| Phase OP — Hub go-live |  |  |  |  |
| Phase O13 — Dashboards, analytics and AI assistance |  |  |  |  |

*End of runbook.*
