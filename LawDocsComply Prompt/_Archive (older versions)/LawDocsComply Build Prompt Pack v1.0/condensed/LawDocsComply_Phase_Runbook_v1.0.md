# LAWDOCSCOMPLY — PHASE RUNBOOK FOR CLAUDE CODE (v1.0, 25 October 2026)

Companion to `LawDocsComply_Master_Prompt_ClaudeCode_v1.0` and the full Build Prompt Pack v1.0. One section per phase: what to type, dependencies, objective, the exit gate and the integration notes that bind the phase. The full functional specification of each phase is in `phases/PXX_*.md` of the pack.

## How to run each session (project owner)

1. Open Claude Code in the LawDocsComply repository.
2. Session 1 only: commit `01_MASTER_PROMPT.md` as `docs/00-master-prompt.md`, `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` as `docs/01-decision-log.md`, all phase files under `docs/phases/`, all appendices under `docs/appendices/`, and the Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`.
3. Every session, type the session prompt given for the phase below. Claude Code reads the master, the decision log and the phase file, writes `docs/phases/PXX-plan.md` and stops for your approval.
4. Approve the plan (or correct it). Claude Code then builds in vertical slices and stops at the exit gate with the hand-over pack (master §0).
5. Before a wave goes live, run P24 for that wave's scope.

## Phase order and waves

Wave 1 (Compliance Core GA, about S1–S25): P00 → P01 → P02 → P03 → P04 → P05, with P15 (RBI-NBFC, MCA-CO, DATA-PRIV, IFSCA-GEN), P17 runtime, P18 core, P19 core, P06, P07, P20 and P23 in parallel squads → P24. Wave 2 (about S18–S38): P08, P09, P10, P11, P12, P14, rest of P15, P17, P18, P19 → P24. Wave 3 (about S28–S46): P13, P16, P21, P22 → P24. See master §13.


---

## Phase P00 — Foundations, Repository Discovery and Migration

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P00_Foundations_Repository_Discovery_and_Migration.md in full, plus the appendices it names as binding. Then write docs/phases/P00-plan.md with the five inventories of master §0 and stop for my approval."*

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
> **Estimated effort:** 4 two-week sprints, squad of 7 (tech lead, 2 backend, 1 frontend, 1 platform/DevOps, 1 data-migration engineer, 1 QA/security engineer) plus a part-time product owner and the Company Secretary as content owner for wave 1.

### Objective and business outcome

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

### Exit gate

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

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-34, NN-45; X-01, X-05, X-06 (licence ADR for an optional WOPI editor), X-21, X-22 (remove live-site claims), X-25 (kernel ADRs), X-26; raise the Ecosystem Spec v1.2 change requests of master §19 in sprint 1**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P01 — Identity, Tenancy, Onboarding and Access

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P01_Identity_Tenancy_Onboarding_and_Access.md in full, plus the appendices it names as binding. Then write docs/phases/P01-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, session context, audit ledger, Correction Entries, break-glass schema, `cfg` heads, flags, evidence ingest, provisioning workflow).
>
> **Sequencing:** P01 follows P00. P02 (Configuration Studio) starts in P01 sprint 2 and consumes the settings P01 registers. P20 (pricing, subscriptions) and P23 (public site, health check) extend the onboarding funnel built here: P01 delivers the funnel's identity, KYB, tenant creation, trial and module-selection mechanics with a price-computation call to a stub of the P20 pricing service (`bil.quote`) that returns catalogue seed values until P20 is live. Migration wave 2 (tenants, users, compliance records) executes at the P01 exit (P00 FR-P00-57).
>
> **Binding appendices:** D (roles, personas and access-control matrix — owned by stream S12; this phase implements its enforcement), A (user, invitation, grant, delegation, break-glass, regulator-view state machines), B (identity tables), Q (authentication and session controls), U (settings), N (plans, trial rules — pricing data), L (KYB/KYC adapters — S8), C (dashboards per role — S12).
>
> **Requirements covered:** R-018, R-025, R-029, R-030, R-031, R-056 (user ↔ HRMS link foundation), R-057, R-069, R-072 (delivery users acting in a tenant), R-074, R-083, R-016 (health-check-to-trial hand-off), R-034 (trial).
>
> **Decisions applied:** D-02, D-03, D-04 (vault access step-up), D-10, D-12, D-14, D-15, D-21.
>
> **Estimated effort:** 5 two-week sprints, squad of 8 (identity engineer, 2 backend, 2 frontend, 1 integration engineer for KYB adapters, 1 QA, 1 UX writer/designer).

### Objective and business outcome

LawDocsComply serves people with very different stakes: a platform super admin who can correct anything; a LawDocs relationship manager who works inside a client's tenant as a maker; a client company admin who configures the product; makers, checkers and department heads who do daily compliance work; KMPs and directors who need dashboards and approvals; internal, external, secretarial and IS auditors; an RBI or other supervisor who must see records read-only for a limited period; employees who only acknowledge policies; POSH Internal Committee members working on sealed matters; co-operative society office bearers and members; marketplace buyers who never subscribe; and anonymous visitors running the free health check.

P01 gives each of them the right door, the right proof of identity, the right permissions and nothing more — and makes a company's first hour with LawDocsComply fast: enter a PAN or CIN, confirm the auto-filled profile, pick the regulator and entity family, choose modules, see the price, invite the team and reach a first useful result.

| Outcome | Exit-gate measure |
|---|---|
| Fast self-onboarding | A new NBFC (synthetic) goes from health-check report → trial tenant → verified entity profile → modules selected → first five users invited → first compliance calendar visible in ≤ 30 minutes, with ≤ 12 fields typed manually (all others auto-filled or defaulted) |
| Strong authentication | 100% of privileged roles (platform, delivery, `ten_admin`, `ten_cco`, `ten_checker`, KMP, board, auditors, supervisor view, IC, payroll) enforce MFA at onboarding; passkeys available to all; step-up enforced on the actions in §4C |
| Least privilege, server-side | Every API, export, job and AI retrieval call is authorised by Cerbos with role + attributes; UI hiding is never the control; the Appendix D matrix is executable as policy tests (≥ 1 allow and ≥ 1 deny test per matrix row) |
| Delivery staff are visible guests | A LawDocs RM can act as maker in a client tenant only through a client-approved `delivery_grant`; every action shows "LawDocs (RM name)" in the tenant's audit and UI; revocation takes effect within 60 seconds |
| Regulator view is safe | A supervisor grant is created by the tenant (maker-checker), time-boxed ≤ 90 days, read-only at database, gateway and UI layers, watermarked, logged and revocable (D-12; NN-18) |
| No identity over-collection | No Aadhaar number, raw PAN image or bureau report is stored at onboarding; KYB facts carry source and fetched-at; DPDP notice and consent artefacts recorded (NN-12) |
| HRMS-linked users | A user can be created from an HRMS employee record (P13) or directly; either way, a person has one identity across tenants and products where they belong |

---

### Exit gate

- [ ] Keycloak realms, clients, theme (WCAG 2.2 AA), authenticators; staff realm federated to Entra ID; SCIM endpoints.
- [ ] Cerbos policies generated from Appendix D with ≥ 1 allow and ≥ 1 deny test per matrix row; `packages/authz` with query-plan filters; Semgrep rule for unauthorised handlers.
- [ ] Delivery, auditor and supervisor grants; break-glass UI and tenant reports; delegations; SoD enforcement.
- [ ] Onboarding funnel steps 1–8 with KYB adapters (at least MCA data provider, GSTN search, PAN verification, GLEIF) in sandbox; trial lifecycle; services-only buyer path.
- [ ] Users admin, bulk import, invitations, HRMS-event consumer contract (P13 will produce).
- [ ] Privacy centre for LawDocsComply's own account data; consent ledger.
- [ ] Migration wave 2 executed with reconciliation; all migrated users enrolled in MFA on first login.
- [ ] Settings registered; screens SCR-IAM-01 to 62; acceptance and NN tests green.
- [ ] `docs/phases/P01-plan.md` with the five inventories.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-43; X-07 (no credit-bureau pulls at onboarding), X-13 (shells), X-15 (trial tenants, pending D-26), X-17, X-19 (added roles)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P02 — Configuration Studio, Rule Engine and Settings

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P02_Configuration_Studio_Rule_Engine_and_Settings.md in full, plus the appendices it names as binding. Then write docs/phases/P02-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, hash-chained audit ledger, `core.correction_entries`, feature flags, outbox, Temporal), P01 (identity, step-up authentication, role catalogue, delegations, legal-entity and department masters).
>
> **Sequencing:** P02 starts immediately after P01 and runs **in parallel with P03 onwards**. Sprint 1 freezes the settings SDK (`packages/config`), key-naming rules, the scope tree and the tier badge component; every later phase registers its settings in the P02 registry **before** reading them (NN-28, "registry before use"). P02 must be complete before P04 exits and before P20–P22 start, because pricing, marketplace and delivery settings depend on G-tier pipelines.
>
> **Binding appendices:** U (configuration framework and settings catalogue), A (workflow and state-machine conventions), C (menus, widget catalogue, settings menu), D (roles, SoD, delegation), B (DDL conventions, events, error codes). Precedence on conflict: master → 02 → Appendix G (law) → Appendix U (tiers and keys) → this phase → other appendices.
>
> **Requirements covered:** R-023, R-024, R-028, R-039, R-068, R-071, R-074, R-086, R-007 (per-entity logic as configuration), R-013 (maker-checker configuration), R-012 and R-059 (customisable dashboards), R-090 (notification templates, not Updates content).
>
> **Estimated effort:** 6 two-week sprints for a squad of 8 (configuration core 3; rule engine 2; Studio UX, designers and catalogue 3).

### Objective and business outcome

LawDocsComply is sold to hundreds of organisation types — an NBFC-Middle Layer lender in Delhi, a Tier-2 urban co-operative bank, a Rajasthan credit co-operative society, an IFSCA Finance Unit, a listed company, an LLP, an insurance broker. Each has different laws, structures, names for things and appetite for process. Regulators change rules often. This phase delivers the **Configuration Studio**: one governed place where every user type changes what it is allowed to change **without a super admin or a code release**, while legal floors, security baselines and evidence integrity stay protected.

| Outcome | Exit-gate measure |
|---|---|
| Routine changes without LawDocs staff (R-024, R-039) | A newly onboarded tenant admin can, in ≤ 30 minutes and with no LawDocs action: rename departments and functions; add a function; create two custom fields on compliance instances; change the default checker routing for one department; set an internal reminder cadence; change dashboard defaults for the CCO; brand the workspace (contrast-validated); set quiet hours — all audited and one-click reversible |
| Entity-specific logic as data (R-007) | Applying the setting pack "NBFC-ML — RBI" or "Credit co-operative society — Rajasthan" at onboarding pre-configures departments, committees, workflows, terminology, calendars, dashboards and statutory-clock rule packs in ≤ 15 minutes; switching packs shows a diff and preserves history (NN-29) |
| Legal values governed (NN-05, NN-28) | Every Governed (G) change passes maker ≠ checker, preview, citation and effective date; no Locked (L) value can be changed through any API or UI (tests `NN-28_*`) |
| Regulatory change as data | A changed statutory deadline (e.g., a revised filing due date), a new State Professional Tax slab or a new RBI return frequency can be drafted, previewed against golden cases, impact-analysed, scheduled for a future date and activated without deployment; compliance instances already generated keep their pinned version unless the propagation mode says otherwise (NN-03, NN-07) |
| Open, interim and waiting items configurable (R-039) | Tenants define their own work statuses, "waiting on" parties, reason codes, chase cadences and escalation ladders, mapped to a locked canonical status set so reports, board packs and benchmarks stay comparable; statutory clocks cannot be paused or weakened |
| Super-admin overrides are safe (D-02, R-068, R-071, R-074) | `plt_super_admin` can change any tenant T or G value, enable or hide any component or settings section, and correct tenant master data — only through a dual-approved, reason-coded Correction Entry visible to the tenant in "Changes made by LawDocs" |
| Configuration is portable | A tenant exports its configuration as a signed JSON bundle (and a human-readable XLSX) and imports it into a sandbox or a sister legal entity with a diff; L and out-of-bounds values are rejected |
| Faster administration (R-023, R-028) | Every settings page shows tier badge, current value, source scope, "who can change this", last change and "Request change"; bulk change across departments has an impact preview and a 10-minute undo window |

---

### Exit gate

1. `packages/config` SDK with codegen, React hook, NestJS decorator, test helpers; CI lint `config-registry-lint`.
2. `cfg` schema migrations (expand-contract), seed definitions (Appendix U), seed setting packs (≥ 12 families at exit: NBFC-BL/ML/UL, NBFC-ICC, UCB-T2, COOP-CCS-RJ, IFSCA-FCFU, SEBI-LISTED-MAIN, IRDAI-BROKER, MCA-PVT, MCA-LLP, STANDALONE-HRMS-LABOUR), seed department catalogue, terminology packs, canonical status sets, seed workflow templates (≥ 8).
3. Rule engine (`RULES_PORT` + ZEN + CEL) with ADR, golden-case harness, impact workflow, review-due scanning, fallback.
4. Studio screens SCR-CFG-01 to SCR-CFG-32, accessible (axe-core clean, keyboard paths tested).
5. Correction Entry console path and tenant "Changes made by LawDocs" page.
6. Configuration export/import/compare.
7. Documentation: `docs/config/` (how to add a setting, tier decision test, rule-pack authoring guide, setting-pack authoring guide), runbook for emergency blocks and overrides.

**Exit gate:** all §12 scenarios and NN tests green; zero unregistered keys in CI; p95 resolve ≤ 2 ms warm; a pilot tenant completes the §1 30-minute admin script unaided; Configuration Health shows zero High-risk workflows without a checker; ADR for the rule engine merged; P03–P05 teams have consumed the SDK.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33 (waiting pauses internal targets only), NN-46; X-10 (department alias map, Appendix U §U.9.0), X-11 (canonical statuses), X-14 (Correction Entry scope), X-16 (register the host switches as Governed settings)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P03 — Regulatory Content Library, Template Registry and Excel Import

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P03_Regulatory_Content_Library_Template_Registry_and_Excel_Import.md in full, plus the appendices it names as binding. Then write docs/phases/P03-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, audit ledger and Correction Entries, object storage with Object Lock, outbox), P01 (identity, roles `plt_content_*`, `ten_admin`, step-up MFA), P02 (settings registry, rule-pack engine, terminology overrides, Governed change pipeline).
>
> **Sequencing:** P03 starts after P01 exits and runs alongside P02 sprint 2 onwards. P04 cannot start its compliance-instance work until P03 §13 items 1–6 are green. P05 consumes the content model, the release pipeline and the importer built here. P15 (sector packs) plugs its applicability rules into the interface defined in §4H.
>
> **Binding appendices:** E (Excel template contract, entity-family vocabularies, importer rules — owned by S2; this phase implements it), F (source register), G (legal rules register), B (data model, events, errors), U (settings catalogue), D (access matrix).
>
> **Requirements covered:** R-003, R-004, R-005, R-007, R-013, R-017, R-039, R-084, R-086, R-087, R-088, R-102 (ingestion side), R-005/D-19 (jurisdiction packs).
>
> **Estimated effort:** 6 two-week sprints for a squad of 8 (content model and release pipeline 3; importer and template registry 3; tenant catalogue and overlay UX 2).

### Objective and business outcome

LawDocsComply sells one product to many kinds of regulated entity — an NBFC in the Middle Layer, an Urban Co-operative Bank in Tier 2, an IFSCA Finance Unit, an AIF, a listed company, an LLP, a credit co-operative society. The legal content each of them must comply with is different, it changes every month, and every client wants to adjust the wording to its own operating structure. This phase builds the **content backbone** that makes that possible without code changes:

1. a versioned, clause-linked **Regulatory Content Library** owned by the LawDocs content team;
2. a **Template Registry** that treats the owner's Excel question format as a versioned ingestion contract, one template per entity family (D-08; Appendix E);
3. an **Excel Importer** that validates, previews, diffs and publishes question sheets prepared in Part 2 of the programme (R-004, R-084);
4. a **tenant overlay** model so that a client can edit, add or retire questions for itself only, with a full audit trail, while still receiving platform updates (R-017, R-086, NN-03);
5. a **Regulation Catalogue** in which the client admin sees every available instrument with its date, update date and applicability, and adds or removes it with a checkbox (R-087).

| Outcome | Exit-gate measure |
|---|---|
| Owner can load Part-2 question sheets without developer help | The 13 IFSCA sheets already in the `IFSCA Documents` folder and the two samples supplied on 25-Oct-2026 import with zero blocking errors after correction; median time from upload to "ready for checker" ≤ 5 minutes for a 300-row sheet |
| Every checkpoint is traceable to law | 100 % of published checkpoints carry authority, instrument, version, clause reference, source URL and source-file hash (NN-06); a citation lint rejects any row without them |
| Tenants customise without losing updates | A tenant overlay on 20 checkpoints survives a platform release that amends 5 of them; the 15 untouched overlays rebase automatically; the 5 conflicting overlays raise one consolidated review task; no completed compliance record changes (NN-03, NN-29) |
| Client admin decides applicability in one screen | A new NBFC-ML tenant sees its recommended instruments pre-ticked, can accept all in one click, or untick one with a reason; time to a complete applicable set ≤ 10 minutes |
| Customisation hierarchy works | A tenant renames "Compliance" to "Secretarial & Compliance" and splits "Risk Management" into "Credit Risk" and "Operational Risk"; all existing checkpoints remap via a mapping table, without editing any question |
| Round-trip Excel | Export of any adopted instrument in the owner's format, edit offline, re-import: unchanged rows are recognised by CompID, changed rows show a cell-level diff, and nothing is applied before checker approval |
| Global-ready | A non-Indian jurisdiction pack (EU GDPR, flag OFF) can be created as data — authority, instruments, holiday calendar, vocabulary — without schema change (D-19) |

---

### Exit gate

1. `cnt` and `tpl` schemas, migrations (expand-contract), RLS policies and seed authorities/jurisdictions/calendars.
2. Template Registry loaded with every family in Appendix E (S2's 24 templates) and their vocabularies; blank templates downloadable.
3. Importer with all four modes, V-rules, preview, error workbook, diff, review and idempotency; performance targets in FR-P03-37 met.
4. Content Studio grid with source pane, lint (L-rules) and coverage report.
5. Release pipeline with scheduling, events and fan-out rebase.
6. Tenant overlays, tenant checkpoints, conflict review, lineage view.
7. Regulation Catalogue with recommended set, adoption preview, removal with second approver.
8. Department/function mapping and terminology.
9. Applicability interface wired to a stub evaluator (real rules from P15).
10. Migration of legacy MongoDB banks and the 9 RBI NBFC MD sheets (460–468) plus the IFSCA sheets into DRAFT, with a migration quality report.
11. All §12 scenarios and NN tests green; accessibility audit of SCR-CNT-10/03 and SCR-TPL-02 passes WCAG 2.2 AA.
12. Contribution to Appendix B (DDL), C (screens), U (settings) and F (events) registered.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-34, NN-35; X-08 (delimiter "; "), X-09 (template and data-template codes), X-10, X-12 (cite the 31 Jul 2026 DoS directions), X-28 (`_LDC_System` export sheet, owner to confirm), X-29, X-38 (canonical IFSCA vocabulary)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P04 — Compliance Workspace: Maker-Checker, Calendar, Tasks and Notifications

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P04_Compliance_Workspace_Maker_Checker_Calendar_Tasks_Notifications.md in full, plus the appendices it names as binding. Then write docs/phases/P04-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, audit ledger, outbox, Temporal), P01 (users, roles, ABAC, delegations, step-up), P02 (settings registry, rule packs, terminology), P03 (content model, adoption, overlays, department map, holiday calendars, WORKSPACE import validation).
>
> **Sequencing:** Starts when P03 §13 items 1–6 are green. P05 (Updates) and P06–P14 build on the workflow engine, Work Inbox, calendar and notification service delivered here; those services ship in sprint 2 of P04 as shared packages (`packages/workflow`, `packages/notify`, `packages/calendar`) and later phases must use them rather than building their own.
>
> **Binding appendices:** A (canonical state machines), C (screens and menus), D (access matrix), U (settings), B (events and errors), G (penalty rules used for exposure), E (column contract).
>
> **Requirements covered:** R-013, R-018, R-023, R-028, R-030, R-057, R-067 (exposure inputs), R-072, R-075, R-088, R-090, R-094, R-095, R-004 (display of imported questions), R-086 (routing).
>
> **Estimated effort:** 8 two-week sprints for a squad of 9 (scheduling engine 2; maker-checker and evidence 2; calendar and sync 2; notifications and inbox 2; reports 1).

### Objective and business outcome

Turn every adopted checkpoint into **work that gets done, proven and reviewed on time** — by the right person, with the fewest clicks, with evidence a checker and an auditor can rely on, and with reports a Chief Compliance Officer can put before the Board.

| Outcome | Exit-gate measure |
|---|---|
| No compliance left unattended | 100 % of applicable checkpoints of adopted instruments generate instances for the current and next period with an owner and due date; unowned instances = 0 (an unowned instance raises a setup alert to the CCO within 1 hour) |
| Maker-checker discipline | No instance can close without a checker other than the maker (NN-05); High-risk instances require evidence matching the checkpoint's expected-evidence list |
| Fewer clicks | A maker can submit a routine monthly compliance with evidence in ≤ 3 interactions from the Work Inbox (open → drop file → submit); a checker can review and approve in ≤ 2 interactions after opening the evidence |
| Deadlines visible where people already look | Due dates and assigned tasks appear in the user's Microsoft 365, Google, Outlook.com, Gmail or Apple calendar within 15 minutes of assignment (Graph/Google API) or at the next ICS refresh |
| Work vs regulatory news separated | Notifications inbox (work) and Updates inbox (regulatory, P05) are separate data models and UIs (NN-27); users can tune digests without muting mandatory escalations |
| Board-ready reporting | CCO generates the quarterly compliance report for the Board/Audit Committee as an editable DOCX and a signed PDF in ≤ 5 minutes, from live data, with drill-down evidence links |
| Owner's Excel format round-trips | The tenant's register exports in the owner's 30-column format with user columns populated; bulk status updates re-import through WORKSPACE mode under the same permissions |

---

### Exit gate

1. `cmp` and `wf` schemas with RLS; shared packages `packages/workflow`, `packages/notify`, `packages/calendar` adopted by later phases.
2. Schedule generator, due-rule evaluator with holiday calendars and business-day conventions, event engine, extension overrides.
3. Instance lifecycle with maker/checker/auditor mapping to columns I, J, T, U, W–AD; evidence capture (upload, DMS, drive, e-mail, ecosystem).
4. Exceptions, waivers, extensions, escalation ladder with floors, delegation and backup owners.
5. Certificates chain with snapshot hashing and eSign/DSC hooks.
6. Dashboards (maker, department head, CCO, MD/Board, auditor), score, report catalogue and builder, scheduled reports, Board compliance report draft.
7. Register export in owner's format and WORKSPACE import application.
8. Calendar with M365, Google, personal accounts and ICS; Teams meetings hook for P06.
9. Tasks with hierarchy rule, dependencies, scheduled/recurring tasks, Vidhi task dispatch stub (real agent in P17), Work Inbox.
10. Notifications with channels, digests, quiet hours, floors; messaging.
11. All §12 scenarios and NN tests green; performance: register grid 50,000 instances scroll at 60 fps (virtualised), filter ≤ 1 s P95; schedule generator 1 million instances/night per region.
12. Contributions to Appendices A, B, C, U registered.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33, NN-46; X-11, X-24 (LDC dates authoritative over synced calendars), X-26 (this phase owns `packages/workflow`, `notify`, `calendar`, SCR-RPT-01, SCR-WF-00 Work Inbox, SCR-CORE-21 global search; SCR-WF-01 remains the Calendar)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P05 — Regulatory Change Management and AI Question Authoring

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P05_Regulatory_Change_Management_and_AI_Question_Authoring.md in full, plus the appendices it names as binding. Then write docs/phases/P05-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (Temporal, object storage with Object Lock, outbox, egress proxy), P01, P02 (settings, rule packs, flags), P03 (content model, clause index, importer, release pipeline, overlays, Regulation Catalogue), P04 (Work Inbox, tasks, calendar, notification service, due-date overrides). AI runtime basics from P17 sprint 1 (provider adapter, prompt registry, logging) — P05 may ship with a minimal adapter and adopt P17's when ready.
>
> **Sequencing:** Starts when P03 exits; may overlap P04 sprints 3–8. The source monitor (§4A–4B) ships first so that the content team accumulates history before go-live.
>
> **Binding appendices:** F (source register — every monitored URL, method and SLA), E (template contract and vocabularies used by the AI Studio), K (Vidhi AI agent specification), G (legal rules), B, U, C.
>
> **Requirements covered:** R-006, R-085, R-088, R-089, R-090, R-004, R-005, R-017, R-039, R-102 (generation of data-compliance sheets uses the same studio), R-097 (Vidhi as authoring assistant).
>
> **Estimated effort:** 7 two-week sprints for a squad of 8 (monitor and ingestion 2; diff and impact 2; Updates UX and tenant change management 2; AI Question Authoring Studio and evaluation 2).

### Objective and business outcome

Regulators change their rules constantly — RBI alone replaced more than 9,000 circulars with 238 function-wise Master Directions on 28 November 2025 and has since issued amendment directions and "updated as on" consolidations almost every month. A compliance tool whose content is static becomes wrong within weeks. This phase makes LawDocsComply a **living** system:

1. **Detect** every relevant publication from RBI, SEBI, IFSCA, IRDAI, MCA, MeitY, CERT-In, the Ministry of Labour, the Central and state co-operative registrars, GST/CBDT and other sources, every evening at 20:00 IST and intraday where feeds allow (D-18, R-089).
2. **Understand** it: classify, summarise, diff against the previous text, and map it to the checkpoints and tenants it affects.
3. **Publish** reviewed changes through the P03 release pipeline with maker-checker (NN-04, NN-05), preserving the previous direction and the previous actionable side by side (R-006, R-088).
4. **Tell** each affected client exactly *what changed, why it matters and what to do*, in the Updates inbox (separate from Notifications, NN-27), by e-mail and push, with calendar entries for effective dates (R-090).
5. **Manage** the client's implementation of the change: impact assessment, tasks, policy updates, board approvals and closure, all audit-trailed.
6. **Author** new compliance question sheets with AI: upload a Master Direction or regulation, let Claude apply the family template and the owner's question-writing method, export the draft Excel, verify, re-upload, and publish after confirmation (R-085) — for the platform (super admin) and for an individual client (client admin, tenant-only).

| Outcome | Exit-gate measure |
|---|---|
| Nothing missed silently | Every source in Appendix F has a last-success timestamp; a source not successfully scanned within its SLA raises a P2 alert to the content lead; the 20:00 IST reconciliation report lists counts per source and failures |
| Fast, reviewed publication | Triage ≤ 1 business day for all detected items (≤ 4 hours for items marked "effective immediately"); High-urgency actionable changes published to tenants ≤ 3 business days; others ≤ 10 business days (P95), measured on the change dashboard |
| Client knows what to do | Every published change produces an Updates item with the three-part note, old vs new actionable side by side, effective date in the calendar, and one-click actions (acknowledge, assign impact assessment, adopt, open conflicts) |
| History preserved | For any checkpoint, a user can see every regulatory change that affected it — previous instrument and paragraph, previous actionable, new actionable, change reason, release, reviewer, and the tenant's own response — exportable as a PDF/Excel change history |
| AI authoring accelerates Part 2 | On the evaluation set (owner-approved IFSCA sheets and the RBI NBFC 460–468 sheets), the AI Studio's draft reaches: clause-coverage recall ≥ 95 % of obligation clauses, citation accuracy ≥ 98 %, zero rows citing non-existent paragraphs, 100 % vocabulary validity, and median reviewer edits ≤ 20 % of rows |
| No auto-publish | No AI output reaches a tenant without human approval (NN-04); tests prove it |

---

### Exit gate

1. `chg` schema, source registry loaded from Appendix F, fetchers (RSS, HTML listing, PDF, e-Gazette, e-mail alert), schedules incl. 20:00 IST reconciliation, health monitoring and alerts.
2. Ingestion, extraction, metadata and classification; triage UI; change-item workflow with SLAs.
3. Clause diff, amendment-instruction parser, working consolidation, concordance editor and re-citation drafting.
4. Publication fan-out integrated with P03 releases and P04 recalculation; due-date extensions.
5. Updates inbox with categories, three-part notes, old-vs-new tables, delivery channels, preferences, acknowledgement and escalation; calendar entries.
6. Tenant impact assessment, implementation tracker, change history exports, Board report section.
7. AI Question Authoring Studio (platform and tenant), methodology profiles for every Appendix E family, evaluation harness with the golden set, cost estimates and metering hooks (P20).
8. Change dashboard with lead-time metrics; Radar report.
9. §12 scenarios and NN tests green; one-month shadow run before go-live comparing the monitor's detections with a manual check of RBI, SEBI, IFSCA and IRDAI pages (target: zero missed P1 items).

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33, NN-34; X-01 (event names), X-12; the RBI 28 Nov 2025 concordance (master §7) is a Wave-1 deliverable**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P06 — Governance, Board, Committees and Company Secretarial

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P06_Governance_Board_Committees_and_Company_Secretarial.md in full, plus the appendices it names as binding. Then write docs/phases/P06-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, hash-chained audit ledger, Correction Entries — D-02, NN-02; feature flags; outbox);
> - **P01** (identity, MFA/step-up, roles `ten_*`, legal-entity scoping, ABAC attributes `legal_entity_id`, `committee_id`, `confidentiality_class`);
> - **P02** (settings registry, rule packs for thresholds and due-date rules, terminology overrides — committee and department names are tenant terms);
> - **P04** (task engine, maker-checker, calendar, Notifications inbox; compliance instances that require Board noting);
> - **P07** (DMS, evidence vault, Word generation, eSign envelopes, DSC signing hand-off) — P06 and P07 are built by the same squad in alternating sprints;
> - **P13** (HRMS person master for directors, KMP and employees). Until P13 exits, P06 ships `gov.persons` as a minimal person master and migrates it to the HRMS projection with expand-contract (NN-11).
>
> **Sequencing:** starts after P04 sprint 2; P15 supplies regulator overlays (RBI, SEBI, IRDAI, IFSCA governance rule packs) — P06 builds the overlay engine and seeds the Companies Act, SEBI LODR, RBI NBFC/UCB/commercial bank and IRDAI governance packs as reference data. P10 (secretarial audit) and P16 (co-operative governance) reuse the P06 meeting, register and declaration engines.
>
> **Binding appendices:** A (state machines), B (data model, events, errors), C (screens, menus), D (access matrix), G (legal rules `LR-MCA-*`, `LR-ICSI-*`, `LR-SEBI-*`, `LR-RBI-*`, `LR-IRDAI-*`), J (ICSI Secretarial Standards map), M (export folder taxonomy `05 Governance - Board, Committees and Meetings/…` and `06 Company Secretarial - Registers, Filings and Resolutions/…`), U (settings).
>
> **Requirements covered:** R-009, R-018, R-053, R-054, R-056, R-057, R-066, R-071, R-086, R-092, R-093, R-094 (governance events), R-095, R-099; contributes to R-013, R-021, R-075.
>
> **Estimated effort:** 9 two-week sprints, squad of 8 (governance core 3, meetings and board portal 3, listed-company and filings 2), plus one company-secretary domain analyst (part-time ICSI member) for content and UAT.

### Objective and business outcome

Every client of LawDocsComply — a private company, a listed NBFC, an urban co-operative bank, an insurer in GIFT City, an LLP or a society — must run its internal governance the way its constitution, the Companies Act 2013 (or the LLP Act 2008, the Societies Registration Act 1860 or the co-operative law), the ICSI Secretarial Standards and its sector regulator require. Today this lives in Word files, Excel trackers and the company secretary's memory. P06 turns it into a **Governance Operating System**: it composes the entity's governance blueprint from law and regulation, keeps the board, committee and KMP structure compliant as people change, runs every meeting from calendar to sealed minutes, maintains statutory registers from events, prepares ROC and stock-exchange filings, and drafts the annual report from source data — with the company secretary in control and every step evidenced.

| Outcome | Exit-gate measure |
|---|---|
| Governance blueprint generated, not hand-built | For each of the eight seeded entity profiles (private company; unlisted public company above thresholds; listed equity company; NBFC-ML; NBFC-UL; UCB > ₹5,000 crore assets; life insurer; LLP) the blueprint lists required directors, independent directors, woman director, committees, KMP, policies, meeting cadence, registers and filings, each with an `LR-*` citation, and matches the domain analyst's golden blueprint with zero missing mandatory items |
| Composition breaches caught at source | A change in a person's attributes (independence lapses, tenure ends, directorship count exceeds limit, DIN deactivated, fit-and-proper declaration overdue) raises a composition issue on every affected committee within 1 minute, with the rule cited and a remediation task assigned to the CS |
| Meetings with fewer clicks | A quarterly board meeting is scheduled, noticed, packed and published in ≤ 25 clicks by the CS using the standard agenda template and auto-pulled items; the notice goes out at least 7 clear days ahead (s.173(3)) or the system forces the shorter-notice path with the ID-presence rule |
| SS-1 minutes discipline | Draft minutes circulate within 15 days, comments close in 7 days, minutes are entered and signed within 30 days (SS-1; s.118 read with Rule 25) — timers visible, escalated at T-3 days; signed minutes are sealed and cannot be edited (NN-02) |
| Registers maintained by events | Allotment, transfer, charge creation, loan/investment approval, RPT approval, SBO declaration and director appointment events update the corresponding register automatically; a register snapshot reconciles to its event log with zero differences |
| Filings prepared, not missed | Every ROC, LODR and sector governance filing in the catalogue has a computed due date, an owner, a data sheet and attachments ready before T-5 working days; after filing, the SRN or acknowledgement is captured; overdue filings show accruing additional fee |
| Listed-company controls | Material events detected in the platform (board outcome, credit rating change, auditor resignation) open a Reg 30 disclosure case with the correct clock (30 minutes for board-meeting outcomes; 24 hours otherwise); UPSI shared through board packs creates Structured Digital Database entries automatically |
| Annual report drafted from data | The Board's report (s.134) and, for listed entities, MD&A and the Corporate Governance Report are produced as a DOCX draft with every figure traceable to its source (accounts, Finbyx/Udofin portfolio, registers, HRMS) and every narrative paragraph marked as AI draft until approved |
| Portability | `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` export (Appendix M §M.3, X-27) holds minutes as signed PDF and DOCX, registers as XLSX and PDF, resolutions, notices, packs and filings, readable without LawDocsComply |

---

### Exit gate

**Deliverables:** `gov` module with migrations; seeded rule packs (Companies Act thresholds, SS-1/SS-2 timelines, LODR, PIT, RBI NBFC/UCB/commercial bank governance, IRDAI CG 2024, LLP, Societies Registration Act base); committee templates; register definitions; filing catalogue; resolution and document templates (DOCX); board portal shell; Temporal workflows; dashboards; Vidhi prompt templates for agenda notes, minutes and annual report; export mapping to `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` (Appendix M); acceptance and NN tests; `docs/phases/P06-plan.md` and `docs/phases/P06-handover.md`.

**Exit gate:**

1. All Gherkin scenarios and NN tests green; domain analyst signs golden blueprints for the eight seeded profiles.
2. One full board-meeting cycle run end to end with a pilot tenant (notice → sealed minutes → MGT-14 data sheet → SRN recorded) with timers verified.
3. Register reconciliation produces zero unexplained differences on the pilot's data.
4. Listed-company module demonstrated on a synthetic listed NBFC: LODR calendar, Reg 30 case, RPT monitor, SDD auto-entries.
5. Accessibility (WCAG 2.2 AA) audit of the board portal and minutes editor passed (NN-21).
6. Export of `05 Governance - Board, Committees and Meetings/` and `06 Company Secretarial - Registers, Filings and Resolutions/` validated: signed minutes open in a PDF reader, registers open in Excel, folder names self-explanatory.
7. All **[VERIFY]** items for features enabled at go-live closed or behind OFF flags.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-36, NN-37; X-26, X-30 (LODR Reg 24A conflict check), X-37 (MBP-1/MBP-4/deposit register corrections); committee and KMP seeds come from P15 §4F and are not redefined here**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P07 — Policy Lifecycle and Document Management System

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P07_Policy_Lifecycle_and_Document_Management_System.md in full, plus the appendices it names as binding. Then write docs/phases/P07-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, object storage with SSE-KMS, versioning and Object Lock, outbox);
> - **P01** (identity, step-up MFA, external-party identities for signers and share recipients, ABAC attributes `confidentiality_class`, `department_id`);
> - **P02** (settings registry, retention-class rule packs, terminology, custom metadata);
> - **P04** (tasks, approvals, calendar, Notifications; evidence linkage to compliance instances);
> - **P06** (Board/committee approval of policies through agenda items and decisions; SDD writes for UPSI sharing).
>
> **Sequencing:** the DMS core (§4H–§4M, §4S, §4W) is a platform service and is built **first, in P07 sprint 1–3, before P06 needs it**; the policy lifecycle follows. P17 (Vidhi) provides the model adapters for drafting, OCR of handwriting and translation; P07 owns the document pipeline, UX and storage. P18 delivers the storage and eSign adapters; P19 consumes the folder taxonomy for export and bring-your-own storage.
>
> **Binding appendices:** A (state machines), B (data model), C (screens), K (Vidhi — drafting, vision, translation guardrails), L (eSign, storage, Microsoft 365/Google adapters), M (LDC-EXPORT-1.0 folder taxonomy — the DMS folder tree mirrors it), Q (security), U (settings).
>
> **Requirements covered:** R-091, R-038, R-021 (folder intake, preserved structure), R-027 (reads documents, screenshots, WhatsApp chats, PDFs, letters, e-mail; eSign where required), R-043, R-076, R-081, R-082; contributes to R-013 (evidence), R-017, R-053.
>
> **Estimated effort:** 8 two-week sprints, squad of 8 (DMS core 3, policy lifecycle 2, document intelligence 2, eSign and sharing 1), plus a part-time legal-drafting analyst for model templates and UAT.

### Objective and business outcome

Regulated entities run on documents: board-approved policies that must be reviewed on time, evidence that proves each compliance, signed agreements, scanned letters from regulators, WhatsApp screenshots of customer complaints, handwritten registers in a branch. P07 gives LawDocsComply one governed document layer and one policy lifecycle, so that (a) every policy is drafted from the right model, redlined against its last approved version in real Word tracked changes, approved by the right body and evidenced by the signed copy; and (b) every document in the platform is stored once, found in seconds, shared selectively, signed lawfully, read by OCR and translated where needed, retained for as long as the law requires and exported in a folder structure a beginner can understand.

| Outcome | Exit-gate measure |
|---|---|
| Policies never silently lapse | Every policy has an owner, approver body, effective date and next-review date; an overdue review opens a compliance issue on day +1; dashboard shows 100% of policies with a computed status |
| Real tracked changes | A Vidhi-assisted revision of a 40-page KYC policy opens in Microsoft Word with every change as a native tracked insertion/deletion attributed to "Vidhi AI (draft)" and a comment citing the regulatory clause or model clause behind it; accepting all changes in Word yields exactly the approved text |
| Approval evidenced | A policy cannot move to `EFFECTIVE` without a P06 decision reference and an uploaded signed or certified copy (PDF); the system compares the scanned copy with the approved text and flags material differences |
| Attestations measured | Acknowledgement campaigns reach the HRMS-derived audience with reminders; completion rate and defaulters are reportable per department |
| Find anything fast | Permission-trimmed full-text and metadata search returns results in ≤ 1.5 s at p95 on 1 million documents per tenant, including OCR text of scans |
| Selective, controlled sharing | A user can assemble a share pack choosing exactly which documents to include, with view-only, watermark, expiry and OTP; every open is logged; revocation takes effect within 60 s |
| Lawful e-signature | Aadhaar eSign (through CCA-empanelled ESPs) and DSC flows complete with a certificate of completion; documents excluded by the IT Act First Schedule are blocked from e-signature with an explanation |
| Handwriting and screenshots usable | Handwritten letters, WhatsApp screenshots and photographed registers produce an editable type copy side by side with the original, with low-confidence words highlighted; the verified type copy and the original are attached together to the record |
| Translation | Documents in any of the six UN official languages or the 22 Eighth Schedule languages are detected and translated into English with segment alignment and confidence, labelled machine translation until reviewed |
| Folder intake | A 5,000-file folder tree is uploaded in one action with a mapping preview, duplicate detection and a commit report; nothing is overwritten |
| Structure survives releases | Canonical document paths are derived from metadata and the LDC-EXPORT-1.0 taxonomy (Appendix M), not from code; a schema release changes no customer-visible path (NN-10, NN-11) |

---

### Exit gate

**Deliverables:** `pol` and `dms` modules with migrations; `packages/redline` (with CI round-trip validation); ingestion, OCR, type-copy and translation pipelines; eSign envelope service with at least one ASP adapter in sandbox; share service and external viewer; folder intake with mapping rules; retention rule pack seed; model templates for the first 20 required policies of NBFC-ML and listed entities (legal analyst signed); tenant template merge; Microsoft 365 co-authoring adapter (sandbox tenant); Appendix M mapping implemented; acceptance and NN tests; `docs/phases/P07-plan.md`, `docs/phases/P07-handover.md`.

**Exit gate:**

1. All Gherkin and NN tests green; redline round-trip suite passes on 50 real-world policy documents (tables, numbering, headers, footnotes).
2. Pilot tenant runs one policy end to end: model → Vidhi draft → reviews → P06 Board approval → signed copy → effective → attestation campaign with ≥ 90% completion.
3. Search p95 ≤ 1.5 s on a 1-million-document synthetic tenant; permission-trimming penetration test passed.
4. eSign: Aadhaar eSign and DSC flows completed in sandbox with certificate of completion; excluded-document block verified.
5. OCR/translation evaluation report from P17 attached, with per-language quality tiers published; tier A enabled only where evaluation passes.
6. Folder intake of 5,000 files with mapping preview and zero overwrites; re-import of an LDC export maps 100%.
7. WCAG 2.2 AA audit of viewer, type-copy workbench and share builder passed (NN-21); screen-reader reading order verified for type copies.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37 (deterministic redline engine), X-04 (ESP/ASP terms), X-06 (Graph co-authoring default)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P08 — Enterprise Risk Management and CRO Workspace

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P08_Enterprise_Risk_Management_and_CRO_Workspace.md in full, plus the appendices it names as binding. Then write docs/phases/P08-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger and Correction Entries, outbox, feature flags);
> - **P01** (identity, roles, ABAC attributes, step-up MFA);
> - **P02** (settings registry, rule packs, terminology, entity-family resolver — every `erm.*` key is registered before use, NN-28);
> - **P03** (content library — obligations and control library that risks link to);
> - **P04** (workflow engine, tasks, approvals, Notifications inbox, calendar);
> - **P06** (committees and meetings — Risk Management Committee packs and minutes);
> - **P07** (DMS — evidence, policies such as the Risk Management Policy and Risk Appetite Statement).
>
> **Consumes (stated fallbacks if not yet built):** P12 (IT/cyber incidents, TPRM register, DPDP breaches → risk events), P13 (people metrics), P14 (complaint metrics), P15 (entity-family profile and applicability), P18 (inbound Finbyx/Udofin `risk` events), P17 (Vidhi drafting). Until P18 ships, KRI values arrive by Excel upload or manual attested entry (§4E.6).
>
> **Sequencing:** starts after P04 exit; runs in parallel with P06–P07; must exit before P09 (Risk Assessment Lab), which reuses the taxonomy, appetite framework, KRI engine and dashboard shell built here.
>
> **Binding appendices:** H (risk taxonomy, Basel mapping, applicability, KRI library, ratio library IDs), A (canonical approval and breach state machines), C (menus and dashboards), D (role matrix), U (settings catalogue), L (integration contracts; Ecosystem Spec v1.1 §6.22 and §9).
>
> **Requirements covered:** R-010, R-012, R-013 (risk-linked controls), R-015 (people-risk data intake), R-023, R-024, R-028, R-030, R-039, R-056, R-058, R-059 (dashboards; ratios in P09), R-075, R-086, R-088.
>
> **Estimated effort:** 6 two-week sprints, squad of 7 (backend 3, frontend 2, risk domain analyst 1, QA 1).

### Objective and business outcome

LawDocsComply is sold to banks, small finance banks, UCBs, NBFCs of every layer and category, ARCs, credit co-operative societies, IFSCA entities, SEBI-regulated entities (mutual funds, AIFs, listed companies, REIT/InvIT managers, intermediaries), IRDAI-regulated insurers and intermediaries, and ordinary companies and LLPs. Each has a different risk-management obligation: a commercial bank must run Pillar 2 ICAAP and publish Pillar 3 disclosures; an NBFC-ML must have a Risk Management Committee and a Board-approved risk policy; a top-1,000 listed company must have an RMC under LODR Reg 21; an LLP has no statutory risk function at all but still benefits from a register. This phase delivers **one configurable enterprise risk engine** — taxonomy, appetite, register, RCSA, controls, KRIs, loss events, issues, acceptance, committee packs and the CRO workspace — that switches on exactly what each entity family needs and nothing more.

| Outcome | Exit-gate measure |
|---|---|
| One engine, many entity families | Onboarding a tenant as "NBFC-ICC, Middle Layer, non-deposit, assets ₹2,400 crore" auto-enables the NBFC-ML taxonomy pack, RMC committee template, appetite metric set and 31 seed KRIs; onboarding "Private limited company, unlisted" enables only the corporate taxonomy (strategic, operational, compliance, financial, cyber, people, legal, reputational, ESG) with no prudential categories. Both explainable with the resolver's citation list (§4A.4) |
| Risk appetite that bites | The Board-approved RAS has appetite, tolerance and limit levels per metric; a limit can never be looser than the regulatory floor (test `NN-22_ras_floor`); a red observation opens a breach episode with escalation in ≤ 15 minutes of the value arriving |
| Live register linked to compliance | Every risk links to objectives, processes, controls and obligations (P03/P04). A failed compliance instance, audit finding (P10) or incident (P12) raises or re-rates the linked risk without re-keying |
| RCSA completed in days, not weeks | A 40-unit RCSA campaign is launched in ≤ 10 clicks from a template; units answer on one screen per risk; second-line challenge queue; completion ≥ 90% within the due date on the seeded pilot |
| KRIs fed automatically | For a Finbyx tenant, `RiskSnapshotPublished`, `KriBreached`, `LimitBreached` and `LossEventRecorded` update the CRO dashboard within the Ecosystem Spec SLA (≤ 15 min for breaches); for a non-Finbyx tenant, the same KRIs update from Excel/Tally templates (P11) or manual attested entries with evidence |
| CRO and RMC can run their meeting from LDC | The RMC pack (risk profile, appetite utilisation, top risks, breaches, loss events, RCSA status, emerging risks, cyber and third-party summary, ICAAP and stress summary from P09) is generated, frozen with a hash and distributed through the P06 board portal in ≤ 30 minutes of preparation |
| Fully customisable without a super admin | Tenant admins and CROs rename categories (levels 2–3), change scales, add KRIs, add widgets and edit templates within the Locked/Governed/Tenant tiers (NN-28); every change is audited (NN-02) |

---

### Exit gate

- `erm` module, schema migrations (expand-contract, NN-11), OpenAPI and AsyncAPI specs, seed taxonomy packs (14) and KRI library (172), RAS templates per family, RCSA templates (enterprise, process, quick), RMC/ALCO/ITSC/ORC pack templates, Excel KRI-value template `LDC-DT-KRI-v1.0`.
- Screens SCR-ERM-01 to SCR-ERM-24 with empty/error states, "i" help keys and keyboard shortcuts; role templates for CRO, risk officer, risk owner, RMC member, Board member.
- Inbound Finbyx/Udofin risk-feed consumer certified against the Ecosystem Spec sandbox (P18), with reconciliation job.
- Documentation: `docs/phases/P08-plan.md` (five inventories: settings, events, error codes, approval actions, export mapping), user guide and video script outlines for P23 (RAS setup, RCSA, KRI breach handling, RMC pack).
- **Exit gate:** all §12 scenarios and NN tests green; pilot tenants (one NBFC-ML on Finbyx feed, one listed company without Finbyx, one credit co-operative society in quick mode) complete RAS setup, one RCSA campaign and one RMC pack end to end; WCAG 2.2 AA audit of SCR-ERM-01/04/08/11 passed; export of `08 Risk Management` opens in Excel/Word/PDF readers without LDC.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-38, NN-39; X-16 (`ral.icaap.host`, `ral.stress.fx_mode`), X-25 (risk kernel, D-22), X-36 (people-risk aggregates k ≥ 5)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P09 — Risk Assessment Lab: ICAAP, Stress Testing, Capital and Ratios

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P09_Risk_Assessment_Lab_ICAAP_Stress_Testing_Capital_and_Ratios.md in full, plus the appendices it names as binding. Then write docs/phases/P09-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P08** (taxonomy, RAS, KRI engine, breach episodes, committee packs, dashboard/widget shell — mandatory);
> - **P11** (accounting bridge: trial balance, Tally Prime/Excel import, Ind AS/AS mapping, financial statements; returns kernel client) — the Lab's non-Finbyx data path;
> - **P02** (rule packs: capital, ALM, PCA, ratio thresholds as effective-dated Governed packs);
> - **P07** (DMS and Word generation with tracked changes for the ICAAP document);
> - **P06** (Board/RMC/ALCO meetings, approvals and minute references);
> - **P18** (Finbyx/Udofin `risk` events and the proposed stress-run API).
>
> **Sequencing:** starts when P08 exits and P11's trial-balance import is available (P11 sprint 2). Capital and ratio engines first (sprints 1–3), ALM and liquidity (3–4), stress studio (4–6), ICAAP (6–7), KMP dashboards and exports (7–8). Banks' 1 April 2027 rule packs run in parallel mode from go-live (§4C.4).
>
> **Binding appendices:** H (ratio library, scenario library, ICAAP outline, KRI library, Basel mapping), A (ICAAP, stress-run and certification state machines), I (return elements that share metrics, e.g., DNBS03/DNBS04A/B), J (Ind AS/AS and Schedule III mapping), U, L.
>
> **Requirements covered:** R-010, R-011, R-012, R-052, R-058, R-059, R-060, R-061, R-064 (investment-entity ratios), R-065 (ARC capital), R-077, R-078, R-021 (exports), R-024, R-028, R-086.
>
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend/quant engineers 3, frontend 2, risk/treasury domain analyst 1, chartered accountant/actuarial reviewer 0.5, QA 1.5).

### Objective and business outcome

Risk managers at Indian regulated entities run capital, liquidity and stress tests in spreadsheets that break every quarter, are hard to audit and cannot show where a number came from. Finbyx solves this for lenders whose books are on Finbyx (Finbyx Part 7E). LawDocsComply must solve it for **every** tenant: Finbyx lenders (by consuming certified Finbyx runs), lenders on other LMSs, banks and UCBs, ARCs, CICs, insurers (as reported), investment companies, listed corporates and co-operatives — from their trial balance, loan-book extracts and portfolio files. The Lab delivers transparent, reproducible engines and a Board-ready ICAAP, with every figure traceable to its input and rule version (NN-22).

| Outcome | Exit-gate measure |
|---|---|
| Right engine for each entity | The capital profile resolver selects the correct engine and minimums for 12 seeded profiles (NBFC-BL leverage only; NBFC-ML CRAR 15%/T1 10%; NBFC-UL + CET1 9%; gold-primary T1 12%; HFC; CIC ANW/RWA 30%; commercial bank CET1 5.5%/T1 7%/total 9% + CCB 2.5%; UCB Tier 1 9% / Tiers 2–4 12%; ARC CRAR 15%; insurer solvency 150% as reported; corporate Schedule III ratios; credit co-operative management indicators) with citations |
| One number, one lineage | Any certified ratio drills to source rows (TB line, loan-book segment, Finbyx event) in ≤ 3 clicks; recomputing a frozen snapshot reproduces identical results bit-for-bit |
| Finbyx clients never re-key | For a Finbyx tenant in `LDC_EXTERNAL` mode, `CapitalRatioComputed`, `RiskSnapshotPublished` and `StressTestCompleted` populate the Lab within the Ecosystem Spec SLA, with provenance `FX` and no LDC recomputation of certified values |
| Non-Finbyx clients self-serve | An NBFC on a third-party LMS uploads the TB (Tally Prime XML/Excel), the loan-book segment template and the borrowings template and gets CRAR, Tier 1, leverage, SLS, IRS, LCR (where applicable), concentration and 40+ ratios within 30 minutes of upload, with data-quality results |
| Stress tests a Board can trust | Scenario library (46 seeded scenarios) covering credit, collateral, interest-rate, liquidity, concentration, operational, cyber, macro and reverse stress; a multi-period run (up to 12 quarters) completes in < 2 minutes for a 50-segment book; approved scenarios are immutable |
| ICAAP in weeks, not months | ICAAP cycle from data freeze to Board-ready Word/PDF in ≤ 15 working days on the pilot NBFC-ML, with tracked changes against last year's document (P07), every table bound to the frozen snapshot |
| KMP dashboards | 15 role templates (CEO, MD, CFO, CRO, CCrO, CCO, CS, IA head, Board, Audit Committee, RMC, ALCO, ITSC, Treasurer/co-op Secretary, Insurer CFO/Appointed Actuary view) render with only governed metrics; users customise without a super admin |
| Exports that stand alone | ICAAP, stress results, capital and ratio packs export as Word, Excel (values plus an assumptions sheet and lineage sheet) and PDF/A into LDC-EXPORT-1.0 `09 Risk Assessments - ICAAP, Stress Tests and Ratios/<FY>/…` and open without LDC |

---

### Exit gate

- `ral` module; kernel integration (`infrabyx-risk-kernel` pinned) with golden fixtures shared with Finbyx CI; rule packs: NBFC CAP 2025, UCB CAP 2025, Bank CAP 2025 (+ 2027 parallel pack), NBFC ALM 2025, NBFC CON 2025, NBFC MSD 2026 PCA, CIC, HFC, ARC, insurer solvency; Lab templates (11) with `_Template_Info`; ratio library of 125 metrics; scenario library of 46; ICAAP templates (NBFC nine-part, bank, light); 15 KMP role templates.
- Screens SCR-RAL-01 to SCR-RAL-22; user guides and P23 tutorial scripts ("Your first capital run", "Running a stress test", "ICAAP in 15 days", "Reading the ALM statement").
- `docs/phases/P09-plan.md` with inventories; model-validation file for each Lab model; reproducibility report.
- **Exit gate:** §12 scenarios and NN tests green; three pilots end to end — (1) NBFC-ML on a third-party LMS: upload → certified CRAR, SLS, IRS, concentration, 40 ratios, stress (5 scenarios + reverse), ICAAP Board-approved DOCX/PDF; (2) Finbyx NBFC in `LDC_EXTERNAL`: values flow from events, ICAAP hosted in LDC, no recomputation; (3) listed corporate: Schedule III ratios and scenario analysis; ICAAP export opens in Word/Excel without LDC; reviewer (CA/actuarial) sign-off on engines.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37, NN-38, NN-39; X-16, X-25; MFI qualifying-asset value per OI-H-01 (master §7)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P10 — Audit Management: Internal Audit, RBIA, Concurrent, IS/IT, Secretarial, Statutory-Audit Support and Specialised Audits

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P10_Audit_Management_Internal_RBIA_IS_Secretarial_Statutory.md in full, plus the appendices it names as binding. Then write docs/phases/P10-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, hash-chained audit ledger and Correction Entries, object storage with Object Lock, outbox);
> - **P01** (identity, step-up MFA, roles `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view`, external-access grants);
> - **P02** (settings registry, rule packs, terminology, Locked/Governed/Tenant tiers);
> - **P04** (obligations, control tests, evidence, tasks, calendar, notifications — audit consumes and writes these);
> - **P07** (DMS evidence vault, OCR, eSign envelopes, Word/PDF rendering);
> - **P08** (risk register, RCSA, KRIs, loss events, risk appetite — the second line that audit reads);
> - **P06** (Audit Committee, Board, meetings, minutes, resolutions — where audit reports are tabled; directors and KMP register).
>
> **Sequencing:** P10 starts after P04 and P08 reach their sprint-2 freeze (obligation, control and risk read models). It runs in parallel with P11 (shared evidence and data-snapshot services) and P12 (IS audit consumes the P12 control library and VAPT register). P17 (Vidhi AI) adds the audit drafting agents; P10 ships the deterministic engine and the AI hooks behind flags.
>
> **Binding appendices:** A (state machines), B (data model, events, error codes), C (screens), D (access matrix), G (legal rules register — LR-RBI-IAF, LR-RBI-SA, LR-RBI-AUD, LR-RBI-CYB, LR-MCA-138, LR-MCA-143, LR-MCA-204, LR-SEBI-24A, LR-ICAI, LR-ICSI), J (accounting, auditing and secretarial standards map), L (integration adapters: Finbyx Part 7D, Udofin RA2/RA4), M (export package), Q (security). Ecosystem: Infrabyx Ecosystem Integration Specification v1.1 §4.7 (external access) and §6.21 (`audit` events).
>
> **Requirements covered:** R-055 (audit module), R-013 (complete compliance tool incl. reports and maker-checker), R-018 (auditor, external auditor, board, supervisor roles), R-057 (regulator read-only), R-052/R-053 (data from Finbyx and Udofin), R-075 (event audit trail), R-076/R-081 (download), R-097 (AI employee for audit drafting), R-054 (secretarial standards checks), R-012/R-059 (Internal Auditor and Audit Committee dashboards), R-021 (export folders).
>
> **Estimated effort:** 8 two-week sprints for a squad of 8 (audit core 3; programmes and type packs 2; workpapers, sampling and evidence 2; reports and dashboards 1), plus one domain analyst (CA with bank/NBFC audit experience) and one CS for the secretarial pack.

### Objective and business outcome

LawDocsComply is sold to NBFCs, banks, UCBs, co-operative societies, ARCs, IFSCA entities, SEBI- and IRDAI-regulated entities, listed and unlisted companies and LLPs. Each of them must plan and evidence audits that a regulator, a statute or a professional standard requires, and most of them run those audits today in spreadsheets, e-mail and shared drives. This phase delivers **one assurance workspace** for every audit type a tenant runs or supports, built on the same obligation, control, risk and evidence base as the compliance and risk modules, so that audit work is not re-keyed and every finding drives remediation.

LawDocsComply is the **tool**. The tenant's auditors own every opinion, rating, finding and report. Neither LawDocs nor any Infrabyx company performs a tenant's internal audit through the tool (RBI (NBFC – Internal Audit Function) Directions, 2026, RBI/DoS/2026-27/464 ("IAF"), para 39: internal audit cannot be outsourced; contract experts only where the Board/ACB is assured the expertise is unavailable internally, and report ownership stays with regular IA staff) — the Marketplace (P21) may sell co-sourced specialist support only within those limits, and the product enforces the limits (§4C.3).

| Outcome | Exit-gate measure |
|---|---|
| One audit universe and risk-based plan for every tenant type | An ML NBFC, a scheduled UCB, a listed company and a credit co-operative society can each be onboarded with an auto-seeded universe (from the entity profile, departments, products, branches, IT systems, outsourcing register, obligations) and an ACB-approved annual plan in ≤ 2 working days of data being available; ten IAF para 31 parameters are locked for RBIA tenants |
| Every audit type has a governed pack | Programmes, checklists, report templates and timelines exist for: internal audit (Companies Act s.138), RBIA (IAF; RBI (Commercial Banks – Internal Audit Function) Directions 2026, RBI/DoS/2026-27/413; UCB RBIA instructions [VERIFY]), concurrent audit (RBI (Commercial Banks – Concurrent Audit) Directions 2026, RBI/DoS/2026-27/409), IS audit (RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026, RBI/DoS/2026-27/461 ("CYB"); SEBI CSCRF; IRDAI cyber guidelines), IT general controls, VAPT tracking, secretarial audit (s.204, Rule 9, LODR Reg 24A), statutory-audit support (PBC, CARO 2020, Rule 11(g), NBFC Auditor's Report Directions 2026, LFAR for banks), stock and receivables audit, branch audit, data-protection audit (DPDP Rules 2025 r.13 for SDFs), regulatory inspection management, tax-audit support, special investigation, outsourcing/vendor audit, co-operative statutory audit support |
| Evidence without re-keying | ≥ 80% of evidence items in a seeded RBIA engagement are system evidence links (LDC compliance records, policies, minutes, risk data, Finbyx/Udofin records by reference and hash) rather than uploads; every link is hash-pinned and drift-detected |
| Reproducible sampling and analytics | Re-running any sample with the stored snapshot and seed returns identical items; full-population tests run on imported or connected data |
| Findings drive remediation | Every issued finding creates action items in the P04 task engine, a risk-register link (P08) and, where a regulatory breach is flagged, a `ComplianceIssueRaised` event; overdue High findings escalate to the ACB pack automatically |
| Reports in the legally required shape | Report engine produces RBIA, internal-audit, concurrent, IS-audit, MR-3, Secretarial Compliance Report (Reg 24A), CARO clause pack, NBFC Auditor's Report Directions checklist, LFAR question bank (banks), and inspection-response packs as DOCX and PDF/A, with locked mandatory sections; AI may draft narrative, a named human signs |
| Audit Committee ready | One-click ACB pack (plan status, findings by rating and ageing, repeat findings, ATR, HIA in-camera tracker, QAIP, VAPT status, concurrent-audit summary) frozen with hash and tabled through P06 |
| External auditors and supervisors work inside the tool | Time-boxed, read-only, purpose-bound grants (D-12; Ecosystem Spec §4.7) for statutory, IS, secretarial, concurrent and co-operative auditors and supervisors; watermarked capped exports; daily activity report |
| Portability | Every engagement exports to `LDC-EXPORT-1.0` under `10 Audits and Inspections/<Audit type>/<FY>/<Engagement name> - <Period>/` with planning, workpapers, evidence, findings register (XLSX), report and manifest (Appendix M §M.3, X-27) |

---

### Exit gate

1. `aud` schema migrations (expand-contract), seed programme libraries (NBFC RBIA, bank RBIA/concurrent, UCB, co-operative, ARC, companies s.138, IS/ITGC, data protection, secretarial, statutory support), report base templates, CAAT library v1 (≥ 30 tests), methodology v1.
2. All screens in §6 with empty/error states and `help.aud.*` content.
3. Applicability resolver with citations for all §4B types; decision log visible to CCO and HIA.
4. Engagement, finding, plan, methodology, grant, VAPT state machines with Temporal timers.
5. ACB pack builder integrated with P06 agenda and minutes write-back.
6. Ecosystem mirror and publish for `audit` events; evidence-request client.
7. Export to `LDC-EXPORT-1.0` (§4Q) with contract test.
8. Gherkin suites (§12) green; NN tests green; WCAG 2.2 AA audit of audit screens.
9. Documentation: `docs/modules/aud.md` (domain model, events, settings), auditor user guide, ACB user guide, external-auditor onboarding guide.

Exit gate: a demo tenant (ML NBFC) completes universe seeding, risk assessment, ACB-approved plan, one RBIA engagement with sampled workpapers and three findings through retest, an ACB pack frozen and tabled, a statutory-audit PBC cycle with AUD checklist and DNBS10 timer, one secretarial audit with SS checks, and a VAPT import with an SLA breach — all exported and re-imported into a sandbox with matching hashes.

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37, NN-39; X-16 (`aud.host.mode`), X-19 (`ia_contributor`), X-30 (co-sourced IA only for RBIA-bound REs)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P11 — Return Studio, Data Preparation and Accounting Bridge

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P11_Return_Studio_Data_Preparation_and_Accounting_Bridge.md in full, plus the appendices it names as binding. Then write docs/phases/P11-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, ledger, object storage with Object Lock, outbox, Temporal);
> - **P01** (roles, step-up MFA, external-access grants);
> - **P02** (settings, rule packs, holiday calendars, delegation matrix);
> - **P03** (instrument catalogue — every return definition cites an instrument version);
> - **P04** (obligations, calendar, tasks, notifications, evidence — every return due instance is also a compliance obligation instance);
> - **P07** (DMS: evidence vault, OCR, PDF extraction);
> - **P18** (integration gateway: Finbyx and Udofin connectors, Tally agent channel, SFTP drop, API keys).
>
> **Sequencing:** P11 starts with the **shared returns kernel** contract (D-05) agreed with the Finbyx team in sprint 1 (interface ADR, package `@infrabyx/returns-kernel` and data packs `infrabyx-returns-packs`). P11 then runs in parallel with P10 (shared snapshot and evidence services) and feeds P09 (ratios, capital, ALM), P06 (annual report and board-pack financials), P10 (PBC items, CARO, AUD checklists, tax-audit packs) and P19 (export).
>
> **Binding appendices:** I (returns, CIC and tax return catalogue), J (accounting, auditing and secretarial standards map), B (data model, events, errors), L (adapters and APIs incl. Tally, Finbyx, Udofin), M (export package — `11 Returns and Regulatory Reporting`, `11 Returns and Regulatory Reporting/Credit Information Companies`, `11 Returns and Regulatory Reporting/Accounts and Tax`), G (rules register — LR-RBI-SR, LR-RBI-CIR, LR-GST, LR-IT, LR-MCA). Ecosystem: Infrabyx Ecosystem Integration Specification v1.1 §§5.2 (entities 30–32), 6.18–6.20, 10.2, 12.1–12.3.
>
> **Requirements covered:** R-048 (RBI returns, CIMS/DAKSH/PRAVAAH, data definitions, supervisory-return directions), R-049 (CIC submissions), R-050 (Tally/Excel import and transformation), R-051 (Ind AS/AS applicability; exports follow standards), R-052 (draw from Finbyx/Udofin/other LMS; export return-ready data), R-053 (data for annual reports and minutes), R-061 (CFO ratios from accounts and loan data), R-077 (return-ready data for RBI, SEBI, IFSCA, GST and tax portals with agentic AI), R-078 (import balance sheets, prior annual reports, books, data dumps, Tally), R-079 (GST/tax exports), R-081 (download), R-013 (maker-checker).
>
> **Estimated effort:** 10 two-week sprints for a squad of 9 (kernel client and registry 2; ingestion and mapping 3; validation, reconciliation and packaging 2; accounting bridge 1; CIC and tax packs 1), plus a regulatory-reporting analyst (ex-bank/NBFC MIS) and a CA for accounting and tax packs.

### Objective and business outcome

Indian regulated entities file dozens of periodic, event-based and ad hoc returns to RBI, NABARD, NHB, SEBI, IFSCA, IRDAI, FIU-IND, CERSAI, the GST Network, the income-tax department, the MCA and the four credit information companies (CICs). Compliance teams rarely own the source data; finance, credit and treasury do, often in Tally Prime, Excel and a loan system that may not be Finbyx. This phase gives every tenant a **Return Studio** that turns raw data — wherever it lives — into validated, reconciled, approved, upload-ready files, with the human filer in control and a complete evidence trail.

The design honours three fixed decisions:
1. **Shared kernel (D-05).** Return definitions, cell maps, validation rules and CIC layouts are maintained once, in the Infrabyx returns kernel, and used by both Finbyx and LawDocsComply. LawDocsComply never forks a definition.
2. **Prepare, never file (D-13, NN-08).** LDC generates, validates, reconciles, packages and evidences. An authorised user of the regulated entity uploads on the portal and records the acknowledgement. No portal credential, OTP, DSC PIN, cookie or token is stored, proxied or scripted; no RPA.
3. **Finbyx stays the book of record (NN-23).** For Finbyx tenants, LDC consumes Finbyx `return_run` packages, bureau-cycle records, `PeriodClosed` and `FinancialStatementsApproved` events and never recomputes those returns. LDC computes only for data that is not in Finbyx (non-Finbyx lenders, non-lending entities, group companies, co-operative societies, SEBI/IRDAI/IFSCA entities).

| Outcome | Exit-gate measure |
|---|---|
| A return calendar for every entity type | For an ML NBFC, a scheduled UCB, an ARC, a credit co-operative society, a listed company and an AIF manager, the registry resolves the applicable returns with citations, generates due instances 13 months ahead and shows them in the P04 calendar within 1 minute of profile approval |
| Any source, one pipeline | A non-Finbyx NBFC can load a loan tape (Excel/CSV), a TallyPrime trial balance and GL (via the local agent or XML/JSON export file), a borrowings and investments schedule, and produce DNBS02, DNBS04B and DNBS13 packages reconciled to the trial balance within the template rounding tolerance |
| Finbyx tenants get no duplication | For a Finbyx tenant, every RBI return and CIC cycle appears in LDC from Finbyx events with status, hashes and acknowledgement; "Generate in LDC" is disabled with the reason |
| Deterministic outputs | The same snapshot hash, cell-map version and template hash give a byte-identical file; validation errors cite rule ID and instrument paragraph |
| CIC files for non-Finbyx lenders | Consumer UCRF v3.74, Commercial UCRF v3.10 and MFI UCRF v3.3.1 files built from the loan tape pass the golden-file tests; four bureau outputs from one dataset; incremental W1–W3 and month-end cadence (CIR para 10(2) as substituted from 1 Jul 2026) |
| GST and TDS ready | GSTR-1, GSTR-1A, GSTR-3B, GSTR-9/9C data packages and Form 140/138/144/143 data files (Income-tax Act 2025; 1961-Act forms for earlier periods) are produced with reconciliations and human-filing workflows |
| Accounting bridge | A trial balance mapped once to Schedule III (Division I, II or III), BR Act Third Schedule or the co-operative format produces draft financial statements, notes skeletons and the ratio feed to P09; framework resolved per entity-year with citations (Appendix J) |
| AI that helps but never invents numbers | Vidhi suggests column and ledger mappings, extracts tables from PDF balance sheets and annual reports, explains variances and drafts commentary; every number in a return cell comes from a deterministic computation with lineage (NN-14, NN-22) |
| Evidence and export | Every filing has a sealed evidence pack exported under `11 Returns and Regulatory Reporting/<regulator>/<portal>/<return code>/<period>/` with manifest and acknowledgement (Appendix M) |

---

### Exit gate

1. Kernel interface ADR signed by Finbyx and LDC leads; kernel and packs consumed with pinned versions; golden-fixture CI.
2. `ret`, `ret_stg`, `acc` migrations; CFDM; LDC data templates (17 templates with `_Template_Info`); starter mapping profiles (Tally group names → Schedule III; three generic LMS exports).
3. Data Room with all §4C adapters (Tally agent read path behind flag); malware and PII scanning.
4. Return engine path for NBFC families (DNBS01–14, LEF, FMR family, Form A) on LDC-native data; mirror path for Finbyx; UCB, ARC, bank, SFB rows loaded `ACTIVE_UNVERIFIED` with calendar and evidence.
5. CIC builder (consumer, commercial, MFI) with golden files; GST and TDS packs; MCA AOC-4 payload; accounting bridge (framework resolver, statements, Schedule III datasets, ratio feed).
6. Vidhi data-prep tools and guardrails; agentic run-book behind flag.
7. Screens §6 with empty and error states and help content; dashboards §4O.
8. Exports per §4P with contract tests.
9. Documentation: `docs/modules/ret.md`, `docs/modules/acc.md`, data-template guide for clients, Tally agent installation guide, CIC onboarding checklist, filer's guide (guided upload).

Exit gate: (a) a non-Finbyx BL NBFC demo tenant produces reconciled, signed packages for DNBS02, DNBS04B and DNBS13 (NIL) for one quarter from Tally + Excel, records acknowledgements, and exports the evidence; (b) a Finbyx-linked demo tenant shows mirrored returns with no generate action; (c) a CIC month-end and one W-cycle build passes golden tests; (d) GSTR-1/3B and one Form 140 package pass schema/utility validation; (e) draft Division III statements tie to DNBS02 and the P09 CRAR; (f) all NN tests green.

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37, NN-39; X-09 (`LDC-DT-*` data templates), X-12, X-25, X-31, X-32 (return generation scope in v1), X-41 (Tally read-only)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P12 — Data Protection, Cyber Security, IT Governance and Third-Party Risk (TPRM)

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P12_Data_Protection_Cyber_Security_IT_Governance_and_TPRM.md in full, plus the appendices it names as binding. Then write docs/phases/P12-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, audit ledger, Object Lock evidence store), P01 (identity, step-up MFA, grants), P02 (settings registry, rule packs, Locked/Governed/Tenant tiers), P03 (instrument and obligation library — the DPDP, GDPR, CCPA, CERT-In, RBI/SEBI/IRDAI/IFSCA cyber instruments are content packs), P04 (compliance instances, maker-checker, evidence, calendar, tasks), P07 (DMS, policy lifecycle — privacy notice, ISMS policies), P08 (risk register, KRIs, loss events).
>
> **Sequencing:** starts after P04 exit. P12 sub-iterations: P12a Privacy Programme (§4A–§4F), P12b Cyber and IT Governance (§4G–§4K), P12c TPRM and Outsourcing (§4L–§4N), P12d AI Governance hooks (§4O). P12b can run in parallel with P12a using a second squad. P13 (HRMS) and P14 (grievance) consume the consent ledger, rights-request desk and breach workflow built here.
>
> **Binding appendices:** A (state machines), B (data model, events, errors), D (roles and SoD), F (source register — DPDP, MeitY, CERT-In, sector cyber sources), G (legal rules `LR-MEITY-*`, `LR-CERTIN-*`, `LR-EU-*`, `LR-US-*`, `LR-RBI-*` cyber/outsourcing), M (export package), Q (security and certification readiness of LDC itself — this phase is the *client's* programme), U (settings).
>
> **Requirements covered:** R-005, R-010, R-013, R-021, R-031, R-033, R-038, R-039, R-046 (client side), R-058, R-086, R-088, R-102.
>
> **Estimated effort:** 8 two-week sprints for a squad of 8 (privacy 3, cyber/ISMS 3, TPRM 2); +2 sprints for the multi-law overlay content load with the content team.

### Objective and business outcome

Every client of LawDocsComply processes personal data of borrowers, depositors, investors, policyholders, members and employees, runs regulated technology and depends on vendors. P12 gives the client one place to run its **privacy programme**, its **cyber and IT governance programme** and its **third-party/outsourcing programme**, each driven by versioned law packs and linked to the same obligations, controls, evidence, risks, incidents and Board reporting as the rest of the platform. LawDocsComply is the client's tool; the client remains the Data Fiduciary / controller / regulated entity (NN-14 accountability stays human).

| Outcome | Exit-gate measure |
|---|---|
| A data-protection programme a DPO can run end to end | A seeded NBFC-ML tenant completes: data inventory of 40 processing activities, ROPA export (DPDP + GDPR Art. 30 view), 3 DPIAs, consent-ledger configuration for two purposes, a rights request closed within SLA, and a simulated breach with DPB 72-hour report, CERT-In 6-hour report and RBI DAKSH 6-hour report drafts — all evidenced, in ≤ 1 working day of user effort |
| Multi-law overlay without duplication | One processing activity shows DPDP, GDPR and CCPA obligations side by side, de-duplicated into common controls with law-specific deltas; switching a law pack on/off changes only applicability, never history (NN-29) |
| Sector cyber frameworks as one control library | RBI NBFC Cyber Directions 2026, RBI IT Governance MD 2023 (banks), SEBI CSCRF, IRDAI ICS Guidelines 2023, IFSCA Cyber Guidelines 2025, CERT-In Directions 2022 and ISO/IEC 27001:2022 Annex A load as packs mapped to ≤ 220 common controls; a control test once evidenced satisfies every mapped requirement, with the mapping visible |
| Incident clocks never silently lapse | Every incident with a reportable classification starts each applicable clock (CERT-In 6 h, RBI DAKSH 6 h, IFSCA 6 h, SEBI per CSCRF, DPB "without delay" + 72 h, GDPR 72 h, sector-specific) at the right start event, owned, escalated at 50 %, 75 % and 90 % of the window; a lapse is a Critical exception (NN-31 pattern) |
| VAPT, BCP and DR testing tracked to closure | VA/PT schedule auto-generated from the asset criticality register per the applicable directions (e.g., RBI NBFC 2026 paras 121–126: VA half-yearly, PT annually for critical/DMZ systems); findings tracked to closure with re-test evidence; DR drill records show "DR as primary ≥ 1 working day" where required (para 131) |
| Outsourcing register an RBI inspector would accept | Material-outsourcing classification (paras 14, 58(2) of the NBFC Outsourcing Directions 2025), due diligence, contract-clause checklist (paras 34, 74), half-yearly Board/RMC review (paras 12(1)(vii), 36), exit plan (paras 84–88) — each evidenced and exportable |
| AI governance hooks | Client's AI systems inventory with ISO/IEC 42001-aligned risk assessment and CCPA ADMT / DPDP Rule 13 algorithmic-due-diligence flags |

---

### Exit gate

Deliverables: `dpc` and `tpr` modules with migrations; seeded packs (DPDP + Rules + Schedules, IT Act/SPDI, CERT-In, GDPR, CCPA, RBI NBFC Cyber 2026, NBFC Outsourcing 2025, SEBI CSCRF, IRDAI ICS 2023, IFSCA Cyber 2025, ISO 27001:2022, ISO 22301, NIST CSF 2.0 mapping) with mapping to the common control library; 22 model policies (with P07); vendor portal; exports (ROPA, SoA, registers, breach reports, Board packs); Temporal workflows; dashboards; settings registered; acceptance and NN tests green; documentation `docs/modules/dpc.md`, `docs/modules/tpr.md`, runbook "Running a breach in LawDocsComply" for clients (P23 tutorial source).

Exit gate: all §12 scenarios pass; demo of the §1 outcome script on seeded NBFC-ML, SEBI AIF manager (CSCRF small-size) and IRDAI broker tenants; content reviewer sign-off on each pack's clause mapping with [VERIFY] items listed in Appendix W; accessibility audit of SCR-DPC-07, -10, -11 (WCAG 2.2 AA, NN-21).

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33 (incident clocks from earliest detection incl. service provider), X-33 (no Consent Manager registration)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P13 — HRMS, People and Labour Compliance Suite

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P13_HRMS_People_and_Labour_Compliance_Suite.md in full, plus the appendices it names as binding. Then write docs/phases/P13-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, ledger, Object Lock), P01 (identity, SCIM, step-up), P02 (settings registry and rule-pack engine — payroll and labour parameters are rule packs, NN-26), P03/P04 (labour-law obligations as content packs and compliance instances), P06 (directors, KMP, committees — the people records are shared), P07 (DMS, eSign envelopes, policy acknowledgements).
>
> **Sequencing:** P13 starts after P06 sprint 2 (shared people model). Sub-iterations: **P13a** People core (org, employees, KMP/director link, lifecycle, documents, user provisioning) → **P13b** Time, attendance and leave → **P13c** Payroll on rule packs and statutory outputs → **P13d** Labour compliance (registers, returns, committees, POSH sealed module, employment agreements) → **P13e** People-risk metrics and ecosystem sharing. P13a must precede P04's role-assignment UX finishing (roles are assigned to employees). The suite is sold as a **standalone SKU** ("LawDocsComply People & Labour") and as an add-on inside the GRC subscription (P20 entitlements).
>
> **Binding appendices:** T (Labour Codes, registers, payroll parameters — the parameter seed), D (roles, SoD), A (state machines), B (data model), G (`LR-MOLE-*` rules), M (export), U (settings).
>
> **Requirements covered:** R-014, R-015, R-018, R-024, R-025, R-030, R-043, R-056, R-082, R-086, R-094, R-095, R-102 (labour questionnaires as Part 2 content), and the client-side parts of R-041/R-042 (staff HRMS for LawDocs staff itself is in the Infrabyx Operations Hub OH10, D-03).
>
> **Estimated effort:** 12 two-week sprints, squad of 9 (people core 3, time & leave 2, payroll 3, labour compliance 1 + content analyst). Payroll go-live for any tenant is gated on Appendix T parameter verification for that tenant's States.

### Objective and business outcome

Regulated finance companies, co-operatives and ordinary companies must run their people function under Companies Act governance (KMP, directors, committees), regulator expectations (fit and proper, CISO independence, Chief Compliance Officer tenure, Internal Ombudsman tenure), the four Labour Codes in force from 21 November 2025, State Shops and Establishments laws, the POSH Act and the Income-tax Act 2025. P13 delivers an HRMS that is (a) **the single people master for every other module** (users and roles are employees; committees and KMP come from here), (b) a **labour-compliance engine** producing registers, returns, wage slips and statutory clocks from signed rule packs, and (c) a **payroll engine** that computes and approves pay while disbursal goes out by bank file or a licensed payout partner (D-11).

| Outcome | Exit-gate measure |
|---|---|
| One people master | A new employee created in P13 can be given a platform role, appointed to a committee (P06) and assigned compliance tasks (P04) without re-entering data; leaver revocation removes all LDC access within 15 minutes and pushes M365/Google suspension where connected |
| Finance-company org out of the box | The onboarding wizard proposes a default department structure for the tenant's entity family (NBFC, bank, UCB, credit co-op, ARC, insurance intermediary, AIF manager, listed company, private company, LLP) which the admin can rename, merge or extend; departments map to the compliance "Department" vocabulary of the tenant's Excel templates (Appendix E column M) |
| Labour compliance generated, not typed | For a 150-employee NBFC in Delhi and Uttar Pradesh: unified registers, wage slips, appointment letters, leave records, overtime records, POSH annual report, EPF ECR data file, ESI contribution data, PT/LWF (where applicable) and the Labour Codes obligations calendar are produced from transactions; every output cites its rule-pack version |
| Payroll that an auditor can reproduce | A finalised pay run re-computes bit-for-bit from its stored inputs and parameter versions (NN-22); maker, checker and approver are three different people; bank file hash matches the approved register |
| POSH handled with sealing | POSH complaints are in a sealed store with separate keys; only IC members see case content; 90-day inquiry clock owned and escalated; annual report and Board-report disclosure generated without exposing identities (NN-13) |
| Employment agreements signed in-tool | Offer, appointment letter and employment agreement assembled from templates, signed by Aadhaar eSign/DSC through the P07 eSign port, stored with audit trail |
| People-risk to the risk function | Aggregated people-risk KRIs (attrition, key-person vacancy, training completion, concentration of approvals, overdue mandatory leave for sensitive roles) flow to P08 and, by tenant consent, to Finbyx/Udofin as aggregates only |

---

### Exit gate

Deliverables: `hr`, `lab`, `lab_posh` modules; default structures for 8 entity families; rule-pack adapters pinned to `infrabyx-labour-rulepack` and `ita25-salary-tds`; registers and statutory files for Central sphere + 5 launch States (DL, UP, RJ, MH, KA) with verification status; POSH module; employment-agreement templates and clause library; self-service PWA; workspace provisioning (M365 first); KRI feed; standalone SKU entitlements (P20); documentation and tutorials (P23 sources).

Exit gate: §12 scenarios green; payroll golden fixtures from the shared rule pack identical to OH10/Finbyx GV6 outputs; a pilot tenant's two parallel-run months reconcile to the tenant's existing payroll within ₹1 per employee per component (differences explained); every parameter used in pilot runs is `VERIFIED` or acknowledged `SECONDARY_ONLY`; accessibility audit of self-service.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-25, NN-26 (as before), X-10 (department codes), X-36 (aggregated people metrics); D-11 (no salary money held)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P14 — Grievance Redressal and Customer Support Desk

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P14_Grievance_Redressal_and_Customer_Support_Desk.md in full, plus the appendices it names as binding. Then write docs/phases/P14-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00, P01 (identity, public intake realm, OTP), P02 (settings, rule packs for SLA clocks), P04 (tasks, notifications, calendar, maker-checker), P07 (DMS, OCR/translation for complaint attachments and letters), P12 (rights-request desk shares the intake widget; breach linkage), P13 (GRO/PNO/IO positions and support-team rosters), P18 (website/app/LMS integration, Ecosystem events).
>
> **Sequencing:** after P04 exit; can run in parallel with P12. Sub-iterations: **P14a** Support desk (omnichannel ticketing, knowledge base, embeddable widget) → **P14b** Grievance redressal ladder (GRO → PNO/Internal Ombudsman → external signposting) with regulator clock packs → **P14c** MIS, regulatory reports and Board/Customer Service Committee packs → **P14d** Ecosystem (Finbyx/Udofin/Equator) and investor/member/policyholder variants.
>
> **Binding appendices:** A (state machines), B (events `grievance` scope reuse), D (roles), G (`LR-RBI-*` grievance and IO rules, `LR-SEBI-*` SCORES/LODR, `LR-IRDAI-*` PPHI, `LR-IFSCA-*`, `LR-COOP-*`), L (website/app widget SDK, Ecosystem adapters), U (settings).
>
> **Requirements covered:** R-080, R-098, R-013, R-023, R-031, R-062, R-066, R-086, R-090 (grievance work items are Notifications; regulatory changes to grievance rules arrive as Updates), R-075.
>
> **Estimated effort:** 6 two-week sprints, squad of 7 (desk 3, ladder & clocks 2, MIS & reports 1, integrations 1).

### Objective and business outcome

A borrower, depositor, member, investor, policyholder or customer first contacts the client's help and support channels (website, app, branch, phone, e-mail, WhatsApp, LSP app such as Udofin, LMS borrower portal such as Finbyx). If unresolved, the complaint escalates to the client's Grievance Redressal Officer (GRO), then — where the regulator requires — to the Principal Nodal Officer (PNO) and/or the **Internal Ombudsman (IO)**, and finally the complainant is told how to approach the external forum (RBI Integrated Ombudsman via CMS, SEBI SCORES, IRDAI Bima Bharosa / Insurance Ombudsman, IFSCA, Co-operative Ombudsman or Registrar, Consumer Commission). LawDocsComply hosts the **whole ladder** for the client: the support team closes tickets inside LDC, the GRO has a dedicated workspace, regulator clocks are owned and escalated, and complaint MIS and regulatory reports are generated. The client's website shows the grievance link; the system runs on LDC.

| Outcome | Exit-gate measure |
|---|---|
| One desk from first contact to final reply | A complaint raised on the client's website widget, by e-mail and by Udofin event lands as one ticket per issue (dedup), is acknowledged within the configured time with a reference number, and is resolved, escalated or signposted with every step time-stamped |
| Regulator clocks never silently lapse | For an NBFC tenant covered by the NBFC IO Directions 2026: a partially-resolved complaint is auto-escalated to the IO so that the IO has ≥ 10 days before any RBI/NPCI/card-network TAT, otherwise within 20 days of receipt (cl.14(1)); the final reply issues within 30 days of receipt (cl.14(9)); the RB-IOS 2026 route (30-day wait, then 90-day window) is stated in the final reply |
| Correct ladder per entity type | Ladder templates for bank, NBFC (with and without IO), UCB, credit co-operative/MSCS, ARC, listed company (investors), AMC/AIF/intermediary (SCORES), insurer/intermediary (IRDAI), IFSCA RE, ordinary company/LLP (customers, MCA/IEPF investor grievances), employer (IR Code GRC lives in P13) — selected automatically from the P15 entity profile |
| GRO workspace that saves hours | GRO resolves a complaint in ≤ 5 clicks from inbox with templates, knowledge base suggestions and Vidhi draft reply; bulk acknowledge; SLA-sorted queues |
| Regulatory reports generated | Quarterly IO report to RBI (cl.16(2), due by the 15th after quarter end), Board/Customer Service Committee complaint review with top-5 categories (cl.13(5)), annual report disclosures (complaints received/resolved/pending, maintainability per RBI format [VERIFY current disclosure circular]), SEBI LODR Reg 13(3) quarterly investor-complaint statement, IRDAI grievance returns [VERIFY form] — each export-ready |
| Ecosystem-ready | Finbyx/Udofin `GrievanceRaised` events open tickets in LDC when LDC is the grievance host; `GrievanceUpdated/Escalated` flow back; Equator referral only on the complainant's or RE's explicit choice (never automatic) |

---

### Exit gate

Deliverables: `grv` module; ladder packs for 14 entity families (table §4B) with citations and verification status; widget, hosted portal, SDK wrappers; channel adapters (e-mail, WhatsApp BSP, CTI logging); GRO and IO desks; MIS and 10 regulatory/governance reports; KB; model Grievance Redressal Policies per entity type (P07); tutorials (P23); documentation.

Exit gate: §12 scenarios green; pilot NBFC tenant runs 30 days of live complaints in parallel with existing process with no clock miss; accessibility audit of public form and tracker; content checker sign-off on each ladder pack (or pack remains DRAFT behind flag).

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33, NN-40; X-01, X-23 (no WhatsApp for recovery or legal notices)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P15 — Sector Packs and Entity Logic

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P15_Sector_Packs_and_Entity_Logic.md in full, plus the appendices it names as binding. Then write docs/phases/P15-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, feature flags, bitemporal conventions);
> - **P01** (onboarding wizard, PAN/CIN/GSTIN auto-fetch, legal-entity and group model, users and roles);
> - **P02** (settings registry, three-tier configurability L/G/T, rule-pack engine, terminology/vocabulary packs, menus);
> - **P03** (regulatory content library `cnt`, template registry `tpl`, Excel importer — columns C, D and S feed this phase);
> - **P04** (compliance instances and calendar consume applicability results).
>
> **Sequencing:** P15 sprint 1 freezes the entity taxonomy, the `pack.entity_profile` schema and the applicability-rule DSL, because P04–P14 and P16 read them. P15 runs in parallel with P05–P10; per-family default packs (§4F) are completed family by family as the corresponding content (Part 2 Excel sheets) arrives. P16 (co-operative suite) starts after P15 sprint 2.
>
> **Binding appendices:** E (Excel template contract and entity-family vocabularies — the dropdown values for columns C/D are the taxonomy codes defined here), G (legal and regulatory rules register — every threshold below is an `LR-*` row), H (risk taxonomy and ratio library), I (returns catalogue), S (co-operative law), U (settings catalogue).
>
> **Requirements covered:** R-005, R-007, R-009, R-010, R-012, R-024, R-039, R-056, R-058, R-059, R-060, R-062 (with P16), R-064, R-065, R-066, R-084 (taxonomy side), R-086, R-087, R-093.
>
> **Estimated effort:** 7 two-week sprints for a squad of 8 (taxonomy and rule engine 3; family packs and defaults 3; investment/ARC/listed extensions and UX 2) plus a regulatory content analyst pair (CS + CA) for the family packs.

### Objective and business outcome

LawDocsComply is sold to very different organisations: a ₹200 crore NBFC-ICC in the Base Layer, a Tier 3 UCB, a listed HFC, an AIF manager, a GIFT City finance unit, a composite insurance broker, a private limited company with 40 employees, an LLP, or a Maharashtra credit co-operative society with 12 branches. Each has a different regulator (often several), vocabulary, governance organs, mandatory committees, KMP set, returns, calendars and risk profile. This phase delivers the **entity logic layer**: a single, versioned taxonomy and profile, an explainable applicability engine, and **sector packs** that pre-configure each tenant so that a new client sees only what applies to it, with reasons, from the first login — and so that the profile moves automatically and audibly when the entity crosses a threshold or changes category.

| Outcome | Exit-gate measure |
|---|---|
| Right obligations, explained | For the 12 golden entity profiles (§12), the applicability engine selects exactly the expected obligations from the seeded content (precision and recall = 100% against the golden set); every selected or excluded obligation shows a human-readable "why" (rule, attribute, threshold, citation) |
| Separate logic per entity type (R-007) | Departments, committees, KMP roles, vocabulary, dashboards, return calendars, risk taxonomy and Excel template family are seeded from the sector pack in ≤ 60 seconds after profile activation; no NBFC term appears in a co-operative or insurance tenant |
| Thresholds and transitions handled as data | A simulated crossing of ₹1,000 crore assets moves an NBFC-ICC from Base to Middle Layer with an impact report (added/removed obligations, new committees, new returns) and an effective date equal to the date of crossing (SBR para 22), without a code release |
| Multi-regulator entities | A listed NBFC, a UCB (RBI + State Registrar), an IFSC banking unit of an Indian bank, and an NBFC that is also an IRDAI corporate agent each resolve the union of applicable packs with conflicts resolved by the strictest-wins rule |
| Investment, ARC and listed-company extensions | NBFC-ICC/CIC investment-limit monitors, the ARC pack and the listed-company pack (LODR, PIT, SAST, ICDR events) are active for their families and consume Finbyx aggregates where connected |
| Global readiness (D-19) | The jurisdiction-pack framework accepts a non-India pack (EU GDPR overlay used as the pilot) without schema change; no non-India pack is enabled for a tenant unless it is in state `PUBLISHED` with a named reviewer |
| Customisable without super admin (R-024, R-039, R-086) | A client admin can rename departments and committees, add a voluntary obligation ("Suggestive Compliance"), narrow scope with a reason, and adjust KMP sets within the floors; Locked legal floors cannot be loosened by any tenant role (test `NN-28_*`) |

---

### Exit gate

1. `pack` schema, migrations (expand-contract), RLS policies and seed taxonomy (all families, types, schemes, attribute dictionary, parameters with `LR-*` citations).
2. Applicability DSL, engine, explanation renderer, simulator; golden-profile test suite G1–G12 green with 100% precision/recall on seeded content.
3. Profile-change detector and workflows; exemption and overlay workflows.
4. Sector packs v1.0 for BANK, UCB, RCB, NBFC, ARC, CCS, COOP, IFSC (GEN, FCFU, FME), MF, AIF, LISTED, REIT_INVIT, SEBI_INT, INSURER, INS_INT, COMPANY, LLP, plus overlays (DATA, CYBER, LABOUR, TAX, AML, FEMA, ESG); stubs for AIFI, PAY, CIC_INFO, SOCIETY, PFRDA.
5. Investment, ARC and listed-company extensions with Finbyx event consumers and the investment-register importer.
6. Jurisdiction-pack framework with EU GDPR overlay as a pilot in `IN_COUNTRY_REVIEW` (not enabled).
7. Screens SCR-PACK-01–11 and console screens; "i" help keys registered (P23); settings registered (P02).
8. Applicability statement export (DOCX/PDF/XLSX) included in LDC-EXPORT-1.0 (P19).
9. Documentation: `docs/packs/taxonomy.md`, `docs/packs/rule-dsl.md`, `docs/packs/<family>.md` per family, `docs/regulations/errata.md` entries.

**Exit gate:** §12 scenarios and NN tests pass; content team signs the seeded parameters against Appendix G; three pilot tenants (one NBFC, one credit society, one private company) activated end-to-end in staging within 60 minutes each.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-38; X-09 (family → template code map, master §1.2), X-10, X-12; D-19 jurisdiction packs**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P16 — Co-operative Society Operations Suite

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P16_Cooperative_Society_Operations_Suite.md in full, plus the appendices it names as binding. Then write docs/phases/P16-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P15** (families `CCS` and `COOP`, entity profile, applicability engine, vocabulary pack `COOP`, State rule-pack framework);
> - **P04** (compliance instances, calendar, tasks, maker-checker);
> - **P06** (meetings, minutes, resolutions, statutory-register engine — reused with co-operative templates);
> - **P07** (bye-laws and policy versioning, DMS, eSign);
> - **P13** (staff HRMS for society employees), **P14** (complaints and grievance desk), **P18** (Finbyx/Udofin connectors), **P11** (Registrar/CRCS return preparation).
>
> **Sequencing:** starts after P15 sprint 2 (taxonomy frozen). MSCS and Maharashtra packs ship complete; other States ship as STUB packs completed with counsel at each client's onboarding (P15 FR-P15-49).
>
> **Binding appendices:** S (co-operative law and operations — the legal source for every rule here), G (rules register `LR-COOP-*`), E (template family `LDC-TPL-COOP-CCS` and `LDC-TPL-COOP-GEN`), I (Registrar/CRCS returns), M (export folder taxonomy — co-operative profile).
>
> **Requirements covered:** R-062, R-093, R-096, R-009, R-056 (co-operative variant), R-080 (member grievance), R-081, R-007, R-086.
>
> **Estimated effort:** 6 two-week sprints for a squad of 7 (registers and members 2; general body, elections and governance 2; audit, returns and credit-society monitors 2; UX/vernacular 1) plus a co-operative law analyst.

### Objective and business outcome

India has about 8.4 lakh co-operatives with about 32 crore members across 30 sectors (National Cooperative Database, as reported by PIB, February 2026), and thousands of credit co-operative societies that hold members' savings without RBI supervision, DICGC cover or a modern governance system. Many still keep registers in paper books, hold AGMs late, miss Registrar returns, carry unrectified audit paras for years, and lose their boards to disqualification under the Act. Failures such as the Adarsh Credit Co-operative Society case (Central Registrar notices and liquidation) show what weak member-eligibility, related-party and audit controls cost depositors.

This phase delivers an **end-to-end operating system for a co-operative society** — registration facts and bye-laws, members and shares, managing committee and office bearers, general body meetings, elections support, statutory registers, funds and appropriation, audit and rectification, Registrar/CRCS returns, inspections, complaints and member communications — with the society's GRC (compliance, risk, audit) on the same platform. For **credit co-operative societies**, loans, deposits, interest and share accounting stay in Finbyx (D-16) and members borrow and repay through Udofin; LDC runs governance, compliance and the prudential monitors.

| Outcome | Exit-gate measure |
|---|---|
| Society runs its affairs in LDC | Pilot Maharashtra credit society and a pilot MSCS can, without LawDocs staff help: admit a member, hold a managing-committee meeting with minutes, convene and record an AGM, file the annual return package, record audit paras and file the rectification report — all within statutory clocks |
| No statutory clock lapses unnoticed | AGM, annual return, audit, rectification, election-notice and director-disqualification clocks each have an owner, alerts at T-60/T-30/T-7 days and escalation; an expired clock without action is a Critical issue (NN-31 pattern) |
| Correct law per society | The engine selects the MSCS Act or the correct State Act pack, and the society's bye-laws as a versioned tighten-only layer; a State with a STUB pack shows "limited coverage" and blocks no operations |
| Credit-society safety | Deposit-eligibility exceptions (deposits only from active voting members), director/relative loan reporting, prudential monitors (CRCS order of 22 Jan 2024 for MSCS; State Act for others) and the "no bank in name" guard are live and visible to the board and auditors |
| Ecosystem coherence | For a society on Finbyx, the member register and share ledger are read from Finbyx (single system of record); for a society not on Finbyx, LDC is the system of record and can export the same contracts to any LOS |
| Vernacular and accessible | Hindi and Marathi labels shipped; notices generated bilingual; WCAG 2.2 AA (NN-21) |

---

### Exit gate

1. `coop` schema with RLS, registers engine, clocks, workflows and events above.
2. MSCS and Maharashtra packs complete (variables, templates, notices, forms) and STUB packs for nine States.
3. Member projection sync with Finbyx and membership APIs per Integration Spec §6.24 (contract tests).
4. Screens SCR-COOP-01–17 with EN/HI/MR; member portal behind flag.
5. Export profile for co-operatives in LDC-EXPORT-1.0 (top-level folder `15 Co-operative Society Records/` with sub-folders `Bye-laws`, `Members register and share capital`, `Managing Committee`, `General Body Meetings`, `Elections`, `Statutory audit by co-operative auditor`, `Returns to Registrar`, `Complaints and disputes`; registers, compliance and other records sit in the standard top-level folders 03–24 — Appendix M §M.3 names are authoritative, X-27) (P19, Appendix M).
6. Docs: `docs/coop/state-pack-<code>.md`, `docs/coop/sor-switch.md`.

**Exit gate:** §12 scenarios and NN tests green; pilot MSCS and pilot Maharashtra credit society run one full annual cycle in staging (AGM, return, audit, rectification) with synthetic data; counsel sign-off on MSCS and MH packs.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-38; X-16 (`coop.sor.members`, D-23), X-34 (elections conducted by the authority)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P17 — Vidhi AI Employee, Agents and Knowledge Notebooks

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P17_Vidhi_AI_Employee_Agents_and_Knowledge_Notebooks.md in full, plus the appendices it names as binding. Then write docs/phases/P17-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, audit ledger, outbox, Temporal, object storage), P01 (identity, roles, delegation, step-up), P02 (settings registry, rule packs), P03 (regulatory content library `cnt` — the source corpus for platform notebooks), P04 (tasks, approvals, notifications, calendar — Vidhi's work queue), P07 (DMS, evidence vault, OCR pipeline, Word rendering). Consumes read models of P05, P06, P08–P11, P13, P14 when those exist; ships stated fallbacks when they do not.
>
> **Sequencing:** A thin "Ask Vidhi" (regulatory Q&A over platform notebooks, document summarise/translate) ships in sprint 1–3 so that P05, P06, P07, P09 and P10 can call the shared AI runtime (`packages/ai-runtime`) as they are built. The agent layer (tasks, schedules, tools, approvals) ships in sprints 4–7. Notebook Studio outputs and the evaluation harness complete the phase.
>
> **Binding appendices:** K (Vidhi AI Agent Specification — skills, tool registry, guardrails, evaluation, model cards), L (provider adapters, API catalogue), M (export of AI artefacts), Q (security and certification readiness), U (settings), D (roles), C (screens).
>
> **Requirements covered:** R-019, R-026, R-027, R-038 (AI parts), R-053, R-063 (AI parts), R-077 (AI data preparation assist), R-085 (shared runtime for AI question authoring, built in P05), R-091 (policy drafting), R-092 (agenda and minutes), R-095 (tasks to Vidhi, scheduled tasks), R-097.
>
> **Estimated effort:** 8 two-week sprints, squad of 9 (AI platform 3, agents and tools 3, notebooks and document intelligence 2, evaluation and safety 1).

### Objective and business outcome

LawDocsComply sells time back to compliance teams, company secretaries, risk officers, auditors and boards. Vidhi is the product's **AI employee**: a governed, always-available colleague that can be given work like a junior team member — "draft the minutes from this recording", "check every evidence upload for the ICAAP pack", "every Monday 9 am, send me the overdue RBI items for the Credit department", "read these WhatsApp screenshots and prepare a type copy", "what does the RBI Master Direction say about our grievance redressal timeline, with paragraph references?" — while staying inside four hard limits: it acts only for a named user and inside that user's permissions; it cites or says it cannot; it drafts and proposes but never approves, signs, files, pays, publishes or sends externally on its own (NN-14); and it never trains on, or leaks across, tenant content (NN-15, NN-01).

| Outcome | Exit-gate measure |
|---|---|
| Vidhi is assignable like an employee | A user can assign any task type in P04 to "Vidhi" from the task form, the command palette (`Ctrl/Cmd+K → "Ask Vidhi to…"`), an `@Vidhi` mention in a comment, or the Vidhi panel. Vidhi acknowledges in ≤ 5 s, shows a plan, executes, and returns the output to the assignee's Work Inbox with a "Review and accept" action. 100% of runs carry the delegating user, the permission snapshot, the tools used and the cost. |
| Scheduled and recurring AI work | A user can schedule a Vidhi job (one-off, RRULE recurrence, or event trigger such as "when an RBI update is published that maps to my department") with a preview of the next five runs, an owner, a stop date and a budget cap. Missed runs (outage) are run once on recovery and labelled. |
| Grounded regulatory answers | On the 400-question golden set (Appendix K §K.7) for RBI-NBFC, SEBI-LODR, IFSCA-FCFU, MCA and DPDP notebooks: citation precision ≥ 0.95, answer faithfulness ≥ 0.92, correct-refusal rate ≥ 0.95 on out-of-corpus questions, zero answers that cite a superseded version as current. |
| Document intelligence | Typed copy of printed scans ≥ 98% character accuracy; handwriting and screenshots show per-line confidence; every low-confidence line (< 0.85) is highlighted for human correction; corrected type copy is versioned beside the original (NN-09). Translation into English from the six UN official languages and the 22 Eighth-Schedule Indian languages, with a "machine translation — not certified" watermark. |
| Drafting in Word | Policy, agreement, agenda, minutes and report drafts are produced as `.docx` with **tracked changes** against the chosen base (model template, tenant template or previous approved version) and Word comments carrying citations; drafts open cleanly in Microsoft Word, LibreOffice and Word for the web (headless render test). |
| Notebooks like NotebookLM | Platform notebooks for every enabled regulator pack and tenant notebooks over the tenant's own documents, with chat, citations to passage level, Studio outputs (summary, FAQ, briefing note, study guide, timeline, comparison table, mind map, flashcards/quiz, slide outline; audio overview behind a flag), sharing within the tenant, and staleness banners when a source is superseded. |
| Safe, auditable, affordable | 100% of AI runs written to the AI run ledger (prompt template version, model, provider, region, sources, tool calls, approvals, output hash, tokens, cost). Prompt-injection red-team suite passes (Appendix K §K.8). Tenant AI budgets enforced; per-plan AI credits metered and visible in Settings → Billing → Usage. |
| India-resident inference | Personal, confidential, financial, HR or legal data is processed only by providers whose inference and storage stay in India (default: Claude via Amazon Bedrock India geographic cross-Region inference, ap-south-1 ⇄ ap-south-2) unless the tenant records a cross-border basis (NN-24). |

---

### Exit gate

**Deliverables**: `packages/ai-runtime` (router, adapters, retrieval, validators, redaction, ledger client, cost meter); `apps/api` `ai` module; Vidhi panel and screens SCR-AI-01…17 and console SCR-CON-AI-01…05; skills V-SK-01…25 with prompt templates, schemas and evaluation sets; tool registry with action classes; Temporal workflows (§7.5); platform notebooks for every pack enabled at launch with golden questions; type-copy, translation, WhatsApp/email importers; redline builder with Word comment citations; evaluation dashboard; red-team suite; model cards (`docs/ai/model-cards/`); AI Use Statement (claims-registered); DPIA for AI processing (with P12); sub-processor entries; runbooks (`docs/runbooks/ai-provider-outage.md`, `ai-kill-switch.md`, `ai-incident.md`); seeded schedule templates; tutorial scripts handed to P23.

**Exit gate**: all §12 scenarios green; NN tests green; evaluation thresholds met for every skill enabled at launch (Appendix K §K.7); red-team suite passed with no open critical/high findings; India routing evidence captured for each regulated class; headless render of all golden drafts; load test: 200 concurrent interactive runs per region with p95 first-token ≤ 4 s and p95 Q&A completion ≤ 20 s (excluding provider queueing); cost per median Q&A run within the Pricing Catalogue assumption (Appendix N); accessibility audit of Vidhi screens (NN-21); documentation and hand-off per master §10.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-37, NN-41; X-03 (Bedrock India default route), X-18 (Vidhi name)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P18 — Integration Gateway, Ecosystem Connectors and Developer Platform

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P18_Integration_Gateway_Ecosystem_Connectors_and_Developer_Platform.md in full, plus the appendices it names as binding. Then write docs/phases/P18-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (outbox, audit ledger, tenancy, KMS, Temporal), P01 (identity, SSO, SCIM, service accounts, step-up), P02 (settings registry, mapping-pack overrides), P04 (tasks, calendar, notifications — consumers of calendar and messaging connectors), P07 (DMS — consumer of storage and eSign connectors). Commit the **Infrabyx Ecosystem Integration Specification v1.1** unchanged as `docs/ecosystem/infrabyx-integration-spec.md` (SHA-256 checked in CI; Spec §0 instruction 1) and the `infrabyx-contracts` registry client.
>
> **Sequencing:** Gateway, auth, error model, idempotency and outbox/webhook delivery ship in sprints 1–3 (every later phase publishes and consumes through them). Ecosystem connectors (Finbyx, Udofin, Ops Hub) in sprints 3–6; identity/KYB onboarding adapters in sprint 2 (needed by P01 self-onboarding and P23 health check); workplace/calendar connectors in sprints 4–6; communications and embeds in sprints 6–8; developer portal and certification in sprints 8–10. P19 (portability and storage targets) builds on the storage connector framework delivered here.
>
> **Binding appendices:** L (adapter specifications and REST/API catalogue), B (data model, event and error registers), Q (security), U (settings), M (export formats where connectors exchange files). Ecosystem Spec v1.1 prevails over this file for any cross-product contract (NN-23).
>
> **Requirements covered:** R-002, R-029, R-043 (integration parts), R-047 (group grants), R-049 and R-052 (data intake from Finbyx/Udofin/LMS), R-050 (Tally/Excel intake transport; transformation in P11), R-053, R-057 (federated external access), R-058, R-063 (Jio channels), R-082, R-094, R-098.
>
> **Estimated effort:** 10 two-week sprints, squad of 8 (gateway and platform 3, ecosystem connectors 2, third-party adapters 2, developer experience 1).

### Objective and business outcome

LawDocsComply must connect to the rest of the Infrabyx ecosystem (Finbyx, Udofin, Equator, LawDocs, the Infrabyx Operations Hub, FinLegal Academy) and to the systems its customers already run (third-party LOS/LMS/LSP and recovery systems, Tally and other accounting packages, Microsoft 365 or Google Workspace, their websites and apps, eSign providers, messaging and calling providers) **without redesign** each time a new counterparty appears. The answer is one integration gateway with a small set of stable contracts — versioned REST, CloudEvents over signed webhooks, a connector SDK, mapping packs and a file fallback — and an onboarding path that lets a new company, a group company or a channel partner connect in days, not projects.

| Outcome | Exit-gate measure |
|---|---|
| Ecosystem contracts implemented exactly | LDC passes the Ecosystem Spec §14.3 certification suite groups Contract, Security, Idempotency and ordering, Resilience, Reconciliation and privacy, Operations, External and group access, Risk feed, Archive and storage — and emits `ConnectorCertified` for the Finbyx↔LDC, Udofin↔LDC and Ops Hub↔LDC connectors in sandbox |
| Compliance-mode switch works both ways | A Finbyx tenant can move from `EMBEDDED` to `LDC_EXTERNAL` (and back) with obligations, controls, open issues and the evidence index carried over (hash-chain heads reconciled), dual-publishing for one compliance period, zero lost records (Ecosystem Spec §9.1) |
| New counterparty without code in the core | A certified third-party LMS connector (Apache Fineract reference adapter) and a generic CSV/SFTP layout are onboarded by mapping pack only; a fictitious "Lender X LOS" is connected in ≤ 5 working days in the sandbox with no change to `cmp`, `erm`, `ral` or `ret` code |
| Self-service onboarding data | A prospect entering a PAN or CIN in the health check (P23) or onboarding wizard (P01) gets name, constitution, registration date, registered address, status, directors (for companies/LLPs), GSTINs and LEI pre-filled from licensed sources in ≤ 5 s p95, with consent captured and source attribution shown |
| Calendars everywhere | Tasks and deadlines appear in Microsoft 365, Google Calendar, Outlook.com, Gmail and Apple Calendar (through native sync or ICS/CalDAV), role-scoped, within 5 minutes of a change, with reminders reaching the user's phone through their own calendar app |
| Website and app embeds | A client NBFC puts a "Grievance Redressal" button on its website or app (script tag, hosted page or API) in ≤ 1 hour; complaints land in its P14 grievance desk with acknowledgement in seconds |
| Developer platform | Public developer portal with OpenAPI 3.1 and AsyncAPI 3.0 references, sandbox tenants with synthetic data, client self-registration with tenant-admin approval, SDKs (TypeScript, Python, Java), Postman collection, status page and changelog |
| Safe by default | Every inbound and outbound call authenticated, scoped, rate-limited and logged; personal data never leaves India through a connector unless a recorded basis exists; regulator portals handled as `PORTAL_MANUAL` only (no credentials, OTPs, cookies, RPA or scraping) |

---

### Exit gate

**Deliverables**: gateway configuration as code; `int` module; `packages/contracts` (OpenAPI 3.1, AsyncAPI 3.0, JSON Schemas); generated SDKs (TypeScript, Python, Java); connector host and SDK integration; Finbyx, Udofin, Ops Hub, Equator, LawDocs and Academy connectors; Fineract reference connector; generic CSV/SFTP layouts; `ldc-agent` (Windows/Linux, signed) with Tally XML/JSON extractors; onboarding lookup adapters (at least one licensed company-data provider, GSTIN, GLEIF, PAN channel); Microsoft 365 adapter (SSO, SCIM, calendar, Teams meetings/transcripts, SharePoint `Sites.Selected`); ICS and CalDAV services; eSign adapters (at least two ESPs + DSC desktop signer); email/SMS/WhatsApp/voice adapters (at least JioCX for SMS and one alternate); embeds (script, hosted page, API) with accessibility audit; Razorpay adapter; developer portal and sandbox; certification workbench; integration monitor; runbooks (`docs/runbooks/integration-incident.md`, `dlq-replay.md`, `key-rotation.md`, `compliance-mode-switch.md`, `agent-install.md`).

**Exit gate**: §12 scenarios and NN tests green; Ecosystem Spec §14.3 suite groups relevant to LDC green in sandbox with `ConnectorCertified` emitted for Finbyx↔LDC, Udofin↔LDC, OH↔LDC; Pact tests green with `contracts.lock` pinned; penetration test of gateway, embeds and agent with no open critical/high; load: 500 req/s sustained per region on read APIs with p95 ≤ 800 ms excluding third parties; webhook fan-out 50,000 deliveries/hour with outbox lag p95 ≤ 30 s; documentation complete in the developer portal.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **X-01, X-03, X-04, X-07, X-23, X-24, X-41; implement the Ecosystem Spec v1.2 change requests of master §19 only after approval**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P19 — Data Preservation, Portability and Bring-Your-Own Storage

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P19_Data_Preservation_Portability_and_BYO_Storage.md in full, plus the appendices it names as binding. Then write docs/phases/P19-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (stable identifiers, audit ledger with daily anchors, object storage with Object Lock, migration framework), P01 (roles, step-up), P02 (settings, folder policy, terminology registry — department and function names), P07 (DMS: documents, versions, renditions, evidence vault), P18 (connector framework, `StorageTarget` base, on-premises agent, Microsoft Graph and Google adapters). Every module that stores records (P03–P16, P17, P20–P22) must register its record types in the **export map** (§4E) before its exit gate — this is a cross-phase obligation enforced by CI (NN-10).
>
> **Sequencing:** The export map registry, the export-mapping contract test and the storage key scheme ship in sprint 1 so that every module built after P00 is portable by construction. Full/partial exports and the verifier ship in sprints 2–4; BYO storage targets and scheduled backups in sprints 4–6; folder-tree intake in sprints 5–7; exit plan, rehydration tool and infrastructure-move runbooks in sprints 7–8.
>
> **Binding appendices:** M (export package `LDC-EXPORT-1.0` and folder taxonomy — binding for every path and file name), L (`StorageTarget` adapters), Q (security), U (settings), B (data model conventions). The **Infrabyx Ecosystem Integration Specification v1.1 §12.1 archive standard 1.0** and **§12.2 storage connector contract** prevail on any conflict (NN-23); `LDC-EXPORT-1.0` is LDC's registered **folder profile** `ldc_tenant_v1` within that standard.
>
> **Requirements covered:** R-021, R-043 (folder export, Office formats), R-076, R-081, R-082 (storage parts), R-046 (backups, restore tests — engineering parts in P24), R-047 (cross-product sharing of packages), R-055 (audit-readable exports), R-051 (exports follow accounting/audit/corporate practice — format rules), R-088 (audit trail export).
>
> **Estimated effort:** 8 two-week sprints, squad of 7 (portability core 3, storage connectors 2, intake 1, verification and tooling 1).

### Objective and business outcome

A company that uses LawDocsComply must never feel trapped. On any day — while subscribed, during a regulator's inspection, at the auditor's request, or when it leaves — it can take **all of its data** as an ordinary folder tree of Word, Excel, PDF and CSV files whose folder and file names explain themselves to a beginner, verify that nothing was altered, open everything with Microsoft Office or LibreOffice, and load it into another system. It can also keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, SFTP server, NAS or hard disk in its own data centre). And because the structure is defined by a versioned contract rather than by today's code, the folders do not move when LDC ships new features, changes its database, moves data centre or changes cloud: **no customer ever has to migrate their own data because LDC changed**.

The same folder taxonomy works in reverse: instead of uploading hundreds of compliance documents one by one, a company can drop a structured folder (or its existing SharePoint library) and LDC files each document against the right entity, year, department, obligation, committee or policy.

| Outcome | Exit-gate measure |
|---|---|
| Everything is exportable | The export-coverage test passes: every persisted record type in every module has an export mapping; a seeded tenant with every record type produces an `LDC-EXPORT-1.0` package in which 100% of records are present (count reconciliation per type) and 100% of documents are byte-identical to the stored originals (SHA-256) |
| Understandable without LDC | Usability test: 5 of 5 non-technical participants (a junior accountant, an office manager, a new compliance executive, a director, an external auditor) find a named Board resolution, a policy's approved version, the evidence for a specific compliance and the audit trail of a status change within 3 minutes each using only Windows Explorer/macOS Finder and Office |
| Verifiable offline | The open-source verifier (Apache-2.0) confirms hashes, the detached JWS signature, control totals and audit-chain continuity offline; it fails on a single changed byte or missing file |
| Stable across releases and infrastructure moves | Golden-tenant test: the same synthetic tenant exported before and after (a) a release with schema changes, (b) a database engine major upgrade, (c) a storage-provider swap, (d) a region move rehearsal produces **identical folder paths and file names** for unchanged records and identical record IDs; differences appear only as additive files declared in the package's `CHANGES-SINCE-PREVIOUS.csv` |
| Bring-your-own storage | A tenant connects at least one target (S3, Azure Blob, GCS, SharePoint/OneDrive, SFTP, on-premises agent to NAS/disk); residency verified; canary passes; daily incremental and monthly full copies arrive by 06:00 IST; restore test from the tenant's own copy passes |
| Folder intake | A 5,000-file structured folder is imported with ≥ 95% automatic placement on a well-structured tree (100% on a tree previously exported by LDC), duplicates detected by hash, every unplaced file listed in a review queue, nothing overwritten |
| Exit without friction | Exit export (scope EXIT) completes for a 500 GB tenant within 48 hours, followed by a read-only period, a deletion workflow that respects retention and legal hold, and a signed deletion certificate |

---

### Exit gate

**Deliverables**: `xpt` module; export map registry and registrations for all modules built so far (later phases add theirs before their exit gate); package builder; restricted-archive builder; BSA s.63 pre-fill generator and platform statement; offline viewer; `ldc-verify` and `ldc-load` (Apache-2.0, signed releases, Windows/macOS/Linux); storage adapters (S3, S3-compatible, Azure Blob, GCS, SharePoint/OneDrive, Google Drive, SFTP, on-prem agent jobs); scheduled copies and restore tests; folder intake with mapping wizard and review queue; exit and deletion workflows with certificate; CI gates (coverage, golden diff, render/PDF-A); runbooks (`docs/runbooks/export-failure.md`, `storage-target-incident.md`, `infra-move-database.md`, `infra-move-object-storage.md`, `region-move.md`, `tenant-exit.md`, `court-order-export.md`); usability test report (§1 measure).

**Exit gate**: §12 scenarios and NN tests green; Ecosystem Spec §14.3 "Archive and storage" group green; usability test passed; 500 GB synthetic tenant exit export ≤ 48 h; 50,000-document intake completes with rollback verified; infrastructure-move rehearsal (database provider and object-store move in staging) with empty golden diff and evidence pack.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-42, NN-45; X-27 (Appendix M folder names authoritative)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P20 — Pricing, Plans, Subscriptions, Billing, Savings and Revenue Streams

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P20_Pricing_Plans_Subscriptions_Billing_Savings_and_Revenue_Streams.md in full, plus the appendices it names as binding. Then write docs/phases/P20-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, feature flags, outbox/inbox);
> - **P01** (identity, onboarding wizard, PAN/CIN/GSTIN fetch, trial tenant creation, step-up MFA);
> - **P02** (settings registry and Configuration Studio — every key in §9 is registered there before use, NN-28);
> - **P18** (integration gateway: signed-event inbox, JWS verification of OH catalogue and entitlements, webhook framework);
> - **P23** (public website shell, Free Compliance Health Check that seeds the configurator) — P20 ships the pricing page and configurator components that P23 mounts.
> - **External:** Infrabyx Operations Hub **OH8** (catalogue, quotes, orders, invoices, Razorpay, dunning) and **OH4** (provisioning) per Infrabyx Ecosystem Integration Specification v1.1 §6.27 and §6.29, and Appendix X of this pack.
>
> **Sequencing:** Sprint 1 freezes `BILLING_PORT`, the presentation-catalogue schema and the entitlement SDK (`packages/entitlements`) that every module from P04 onwards calls. P20 may start after P01 exits; its exit gate requires the OH8 adapter to pass contract tests against the OH8 sandbox **or** the interim `LOCAL` adapter to be approved by the owner (D-21; OI-P20-01).
>
> **Binding appendices:** N (Pricing, Plans, Add-ons, Revenue Streams and Savings Model), X (Operations Hub Addendum), U (settings catalogue), B (data model, events, errors), Q (PCI DSS SAQ A scope), P (pricing-page copy and SEO).
>
> **Requirements covered:** R-016 (handoff from health check), R-024, R-034, R-037, R-044, R-067, R-069, R-070, R-071, R-074, R-076 (billing documents download), R-033 (payment security).
>
> **Estimated effort:** 6 two-week sprints, squad of 8 (commerce backend 3, frontend/configurator 3, QA 1, finance-domain analyst 1).

### Objective and business outcome

LawDocsComply must sell itself: a visitor runs the free health check, sees exactly what the product costs for an organisation like theirs, starts a 7-day trial without talking to anyone, and converts by paying online — while a large bank or NBFC can still negotiate an enterprise contract. Every price, component, discount, promotion and trial rule is data, so the owner can change strategy without a release (R-070). Revenue streams that do not work can be switched off (R-044). Clients see, in money and hours, what the product saves them — but only on a transparent, evidenced method (R-067, NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Transparent public pricing | `/pricing` renders three packages (Essentials, Professional, Enterprise), a comparison table of ≥ 60 feature rows and every add-on with its price delta, entirely from the published presentation catalogue; Lighthouse accessibility ≥ 95, WCAG 2.2 AA manual pass (NN-21); prices shown "excl. GST" with the GST-inclusive total shown before payment |
| Apple-style configurator | A visitor configures package + components + scale + billing cycle and sees the itemised running total update in ≤ 150 ms per change; dependencies and exclusions explained inline; configuration can be saved, shared as a link and converted to a quote |
| Self-serve trial → paid | From the end of the health-check report to an active trial tenant in ≤ 5 minutes and ≤ 12 clicks (PAN/CIN fetch pre-fills the organisation); from trial to paid subscription in ≤ 6 clicks via Razorpay-hosted checkout; no auto-conversion (OH8.9) |
| Owner controls commerce without code | Super admin can change a price, add a component, publish a promo code, extend one company's trial, re-order the feature list or retire a package; each change goes through maker-checker with a preview of the public page and of affected tenants, and takes effect on its `effective_from` without a deployment |
| Entitlements enforced server-side | Every module checks `entitlements.check()` on the API; UI hiding is never the control; a lapsed or restricted subscription never blocks reading, exporting, auditor or supervisor access, or any statutory deadline workflow already in progress (OH8.7; NN-29) |
| Billing and membership settings | Tenant admin can see plan, components, usage, seats, AI-credit wallet, invoices, payments, mandates, billing profile, tax documents, renewals and exit — 15 settings pages (§6) — and do every routine billing task without raising a ticket |
| Revenue-stream switches | Each LDC stream (Appendix N §N.6, RS-LDC-01…RS-LDC-30) can be turned on/off by market, segment and channel, with a kill switch that withdraws the purchase option within 5 minutes while honouring existing contracts |
| Honest savings | The Savings Dashboard shows hours saved, cost avoided and penalty exposure managed, each labelled *Recorded*, *Modelled* or *Estimated*, with the formula, inputs and evidence links one click away; no savings figure leaves the tenant (marketing, case studies) without the client's written consent and a claims-gate PASS (NN-19) |

---

### Exit gate

- Presentation catalogue schema, Pricing Studio, public pricing page, configurator (public + embedded), self-serve trial flow, Billing & Membership settings (SCR-BIL-11…28), entitlement SDK adopted by all modules built so far, usage meters, Savings Dashboard and Value Report, stream switches, `BILLING_PORT` with OH8 adapter contract-tested (or LOCAL adapter approved, OI-P20-01).
- Seed data: Appendix N catalogue, feature rows, FAQs, savings methodology registry (baselines marked `[OWNER TO SET]` until the time-and-motion study is done).
- Evidence: SAQ A scope note, dark-pattern self-audit v1, claims-gate PASS for all public copy, accessibility report, load test (pricing page p95 TTFB ≤ 300 ms at 200 rps), reconciliation dry run with OH8 sandbox.
- **Exit gate:** all §12 scenarios and NN tests green; owner sign-off on seeded prices (Appendix N `[OWNER TO SET]` resolved) and refund policy; legal sign-off on ToS, DPA, RE Addendum and click-wrap design (OI-P20-03); tax sign-off on SAC per SKU (OH8 tax review).

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-42, NN-44; X-02 (OH8 is the billing system of record; `bil` scope per master §5.3), X-15, X-18; open owner decisions D-26, D-27, D-28**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P21 — Marketplace, Retainers and FinLegal Academy

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P21_Marketplace_Retainers_and_FinLegal_Academy.md in full, plus the appendices it names as binding. Then write docs/phases/P21-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00, P01** (tenancy, identity — including light-weight **buyer accounts** for organisations without a subscription), **P02** (settings), **P07** (DMS, eSign envelopes, engagement letters), **P04** (tasks, notifications, calendar), **P18** (integration gateway, Academy feed connector), **P20** (shared quote/order/invoice components, `BILLING_PORT`, entitlements, presentation catalogue patterns), **P23** (public site shell, SEO).
> - **External:** Operations Hub **OH8** (first-party service SKUs, quotes, orders, invoices, Razorpay), **OH9** (group professional directory: verification, `ProfessionalEmpanelled`, `ProfessionalSuspended`), **OH3** (leads), **OH6** (complaints about LawDocs services), **OH14** claims gate; LawDocs Trainings LMS (trainings.lawdocs.in).
>
> **Sequencing:** Starts after P20 sprint 2 (shared commerce components frozen). Third-party provider commerce (Model M2/M3, §4C) ships behind flags that stay OFF until counsel clears each profession (D-06; OI-P21-02…05). First-party LawDocs services and the Academy listing ship first.
>
> **Binding appendices:** O (Marketplace Services Catalogue and Professional Rules), N (streams RS-LDC-12…RS-LDC-22), X (OH addendum §X.8–§X.9), G (legal rules LR-BCI-*, LR-ICAI-*, LR-RBI outsourcing), M (export of engagement records).
>
> **Requirements covered:** R-035, R-036, R-037, R-072 (retainer contract basis), R-100, R-020 (service explainers), R-038 (deliverable sharing), R-021 (engagement records in export).
>
> **Estimated effort:** 7 two-week sprints, squad of 9 (marketplace backend 3, frontend 3, Academy/integration 1, QA 1, legal-ops analyst 1).

### Objective and business outcome

The LawDocsComply Marketplace is the place where an organisation buys the human expertise that the software alone cannot provide — compliance retainers, virtual CXO support, drafting of policies, agreements, annual reports and ICAAP documents, stress testing and risk assessments, return-filing support, audit-readiness, certification readiness (SOC 2, ISO, PCI DSS), VAPT and trainings — **with or without a software subscription**. It is open to anyone without logging in (R-036), starts with LawDocs' own professionals and opens to outside providers later (R-035), and is designed so that LawDocs never breaches the professional-conduct rules that bind advocates, chartered accountants, company secretaries and cost accountants (D-06).

| Outcome | Exit-gate measure |
|---|---|
| Public, browsable catalogue | `/marketplace` lists ≥ 60 seeded first-party offerings in ≥ 12 categories (Appendix O §O.2), each with scope, deliverables, exclusions, timeline, price basis and "who this is for"; browse and search need no login; WCAG 2.2 AA |
| Services without SaaS | A non-subscriber can buy a fixed-price service in ≤ 8 clicks (buyer account + GST profile + Razorpay checkout) and receive deliverables in an Engagement Room; later conversion to a full tenant carries the engagement record across |
| Custom offerings and pricing | LawDocs delivery leads (and, when enabled, outside providers) publish offerings with their own scope, price model (fixed, milestone, retainer, hourly band, quote-only) and SLA; every offering passes legal-category and claims checks before going live |
| Retainers with SLA eSign | A retainer goes from proposal to eSigned SLA to active RM assignment (P22) in ≤ 2 working days; monthly invoices, service-hour or deliverable tracking and SLA credits run automatically |
| Professional-conduct compliance | Per-profession switches enforce listing mode, commission, ratings and call-to-action rules; advocates and CAs in practice are never listed with commerce features unless counsel clears it; CI tests prove forbidden fields cannot be rendered |
| FinLegal Academy | Courses from trainings.lawdocs.in appear in the marketplace with live price, next batch and enrolment link; corporate seat bundles can be quoted and invoiced; completion certificates flow back as compliance evidence where the learner consents |
| Billing | First-party services invoiced by the LawDocs selling entity through OH8 with GST; direct-model provider invoices captured; invoices e-mailed to buyers; refunds and disputes handled with credit notes |

---

### Exit gate

- Marketplace public and in-app surfaces, buyer accounts, Engagement Room, first-party offering studio, proposal builder, delivery pipeline, retainers with SLA engine, Academy feed, disputes, moderation, profession rules engine with seeded rules, 60+ seeded offerings (Appendix O §O.2), engagement-letter and SLA templates (Appendix O §O.6) approved by counsel.
- **Exit gate:** §12 scenarios and NN tests green; counsel sign-off on engagement letter and marketplace terms; tax sign-off on SAC per service class and RCM statements; owner sign-off on retainer plans and prices; external provider flags remain OFF unless OI-P21-02…05 are closed with opinions recorded.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-20 (render allow-lists), NN-43; X-02, X-18 (Academy name), X-30; D-32 (no reserved advocacy/attest services in LawDocs' own name)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P22 — Service Delivery Console and Operations Hub Interface

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P22_Service_Delivery_Console_and_Operations_Hub_Interface.md in full, plus the appendices it names as binding. Then write docs/phases/P22-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (tenancy, audit ledger, break-glass framework), **P01** (Keycloak realms, staff identities, step-up MFA, grants), **P02** (settings), **P04** (tasks, maker-checker, calendar, notifications), **P07** (DMS, deliverables, sharing, eSign), **P18** (integration gateway, `WORKSPACE_PORT`, OH events), **P20** (billing views, entitlements), **P21** (engagements and retainers that create delivery work).
> - **External:** Infrabyx Operations Hub (OH1 group identity and grants, OH3 CRM, OH4 onboarding, OH5 customer success, OH6 support desk, OH8 billing, OH10 staff HRMS, OH11 internal controls/timesheets/utilisation, OH12 workplace suites) — Appendix X lists what OH must add.
>
> **Sequencing:** Can start after P04 and P07 exit; the tenant-grant mechanics (§4C) must be built with P01's grant engine. P22 must exit before any retainer goes live (P21 FR-P21-30).
>
> **Binding appendices:** X (Operations Hub Addendum), D (roles and access matrix), Q (credential vault controls), L (WORKSPACE_PORT adapters), A (maker-checker and grant state machines), M (export of delivery records).
>
> **Requirements covered:** R-025, R-040 (via OH, interface here), R-043, R-047, R-072, R-073, R-074, R-083, R-030 (role dashboards for delivery staff), R-075.
>
> **Decisions applied:** D-03 (group Hub + LDC delivery console), D-04 (encrypted credential vault in the client tenant), D-02 (correction entries), D-10 (suite-neutral workspace).
>
> **Estimated effort:** 6 two-week sprints, squad of 8 (backend 3, frontend 3, security engineer 1, QA 1).

### Objective and business outcome

LawDocs serves its clients through people — relationship managers (RMs), company secretaries, chartered accountants, compliance analysts and legal professionals — who do real work *inside* each client's LawDocsComply tenant. The **Service Delivery Console** (`apps/delivery`) is their workplace: one portfolio across all clients, one section per client, and a governed way to act as a **maker** inside the client's tenant while the client's own employee remains the **checker** (R-072). It holds the client's portal credentials safely (D-04), keeps messages and shared files in one place (R-073), shows billing and SLA status, and talks to the Infrabyx Operations Hub for CRM, tickets, customer success, timesheets and billing (D-03) — without copying client compliance content into the Hub (OH Part 4.5).

| Outcome | Exit-gate measure |
|---|---|
| One portfolio | An RM sees all assigned clients with health, SLA risk, due items and unread messages on one home screen; time to open any client section ≤ 2 clicks |
| Governed maker access | A delivery maker grant is proposed by either side and approved only by the client's tenant admin; scope by department/function/obligation set; max 12 months per grant (renewable); delivery users can never act as checker, approver, board member or auditor in a client tenant (test `NN-05_delivery_never_checker`) |
| Credential vault | Credentials are owned by the client admin, revealed only to named grantees with step-up MFA, every reveal logged and visible to the client; RBI portal credentials default to client-only; no bulk export exists |
| Client communication | Secure messages, shared drive links (SharePoint/OneDrive/Google Drive) and deliverables are reachable from the client section; every file shared lands in the client's DMS with a hash |
| Commercial visibility | RM sees plan, components, renewal, invoices status and retainer usage (read-only from P20/OH8); cannot change prices or entitlements |
| OH integration | Tickets, CRM activities, CS health inputs, timesheets and milestone acceptances flow to OH through Ecosystem-Spec events/APIs, carrying no compliance content; a contract test proves no obligation text, evidence or credential ever leaves LDC |
| Anti-fraud and productivity | Every action is attributable to a named staff member; work is measured by outputs (tasks, SLAs, deliverables), not covert monitoring (NN-25); SoD and access reviews quarterly |

---

### Exit gate

- `apps/delivery` with SCR-SDC-01…25, tenant-side SCR-SDC-30…34, grant engine extension, act-in-tenant sessions, credential vault (with security review and pen-test of the reveal service), messaging and e-mail bridge, drive links, deliverables register, SLA/health/report views, OH integrations (tickets, CRM, CS signals, timesheets, milestones) contract-tested against OH sandbox, runbooks (leaver sweep, vault anomaly response, emergency revocation).
- **Exit gate:** §12 scenarios and NN tests green; external penetration test of vault and session token exchange with no high findings open; legal sign-off on delivery terms, RE notice and RBI-portal acknowledgement wording; OH addendum (Appendix X) items X.2, X.5, X.10 implemented in OH or stubbed with fallbacks recorded.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-17, NN-43; X-02, X-17**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P23 — Public Website, Free Compliance Health Check, Help Centre, Tutorials and Accessibility

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P23_Public_Website_Health_Check_Help_Centre_Tutorials_and_Accessibility.md in full, plus the appendices it names as binding. Then write docs/phases/P23-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P00** (monorepo, `apps/public` scaffold, audit ledger, object storage, observability);
> - **P01** (identity, consent ledger, company lookup through PAN/CIN adapters, trial tenant provisioning);
> - **P02** (settings registry, terminology overrides, menu registry — the "i" keys and help keys are registered there);
> - **P03/P05** (regulatory content library and Updates feed — the public Regulatory Updates hub reads a published, human-summarised subset);
> - **P15** (entity families and applicability — the health check selects its question set per family);
> - **P18** (integration gateway: MCA/PAN lookup adapters, Operations Hub CRM events, Brevo through the Hub);
> - **P20** (pricing catalogue and configurator — this phase renders the public pricing page; P20 owns its data and checkout);
> - **P21** (public marketplace and FinLegal Academy listings — this phase renders the public entry points and SEO for them).
>
> **Sequencing:** the marketing site shell, CMS, claims register and accessibility foundation (§4A–4D, §4L) start as soon as P00/P01 exit and can run in parallel with P03–P10 on a growth squad. The health check (§4E) needs P15's entity taxonomy and P01's lookup adapters. Tutorials (§4K) start once the first tenant modules (P03–P04) are stable and are refreshed every release thereafter. The accessibility release gate (NN-21) applies to **every** phase from P01 onwards; this phase owns the standard, the tooling and the conformance report.
>
> **Binding appendices:** Appendix P (copy deck, health-check question bank, tutorial and video catalogue, SEO/GEO clusters and schema), Appendix R (competitive research), Appendix C (information architecture of the authenticated apps), Appendix N (pricing data), Appendix O (marketplace catalogue), Appendix Q (security and privacy), Appendix U (settings catalogue).
>
> **Requirements covered:** R-016, R-020, R-022, R-028, R-030 (public surfaces), R-032, R-034 (pricing presentation), R-036 (public marketplace and academy entry), R-037 (benefit explanation), R-045 (marketing funnel surfaces, with the Hub as system of record), R-069 (health check → trial entry), R-070 (pricing page rendering), R-100 (memorable client experience), R-101 (verification of published claims).
>
> **Estimated effort:** 7 two-week sprints for a growth squad of 7 (2 front-end, 1 back-end, 1 content engineer, 1 accessibility specialist (IAAP CPACC/WAS), 1 designer, 1 QA), plus a content team of 3 (regulatory writer, technical writer, video producer) that continues after the phase as a standing function.

### Objective and business outcome

LawDocsComply is sold self-serve to thousands of NBFCs, co-operative societies, intermediaries and companies that will not take a sales call before they trust the product. The public website, the free Compliance Health Check and the learning surfaces are therefore the first product most buyers use. This phase delivers a fast, accessible, search- and AI-discoverable public site; a free health check that gives a genuinely useful, indicative result and converts into a 7-day trial; a help centre, "i" glossary and tutorial library that let users understand regulatory terms and features without calling support; and an accessibility programme that makes every LawDocsComply surface usable by people who are blind, low-vision, deaf, hard of hearing, motor-impaired or neurodivergent — which is also a regulatory obligation that many LawDocsComply customers themselves now carry (SEBI digital-accessibility circular of 31 July 2025; draft RPwD (Amendment) Rules 2026).

| Outcome | Exit-gate measure |
|---|---|
| Content visible to crawlers and AI retrieval | Every public page returns its full primary content in the initial HTML response (no client-side-only rendering); `curl` of `/`, `/pricing`, `/solutions/nbfc`, `/health-check`, `/glossary/crar` shows headline, body and structured data. `/llms.txt` is served as `text/plain`. (Fixes the 25 Oct 2026 finding that the live site returns an empty SPA shell — Appendix R §R.9.) |
| Fast and stable | Core Web Vitals at the 75th percentile on mobile (CrUX or RUM): LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1; Lighthouse performance ≥ 90 on the five template types |
| Free health check works end to end | An anonymous visitor completes the check for any of the 12 launch families (Appendix P §P.3) in ≤ 12 minutes median; receives an on-screen result immediately, a PDF and a share link; the lead reaches the Operations Hub CRM within 60 seconds with consent flags; the visitor can start a 7-day trial with the entity profile pre-filled in ≤ 2 clicks |
| Honest results | Every report carries the D-15 disclaimer; every score is reproducible from the stored answers, question-bank version and scoring-model version (NN-22); no report says "compliant", "certified" or "audit-ready" (NN-19) |
| Claims governed | 100% of numeric claims, logos, testimonials, certifications and regulatory-recognition statements on published pages link to an approved, unexpired Claims Register entry; the build fails otherwise |
| Self-help reduces support | Every menu item, column header and form label in the tenant app that names a regulatory or product term has an "i" key resolving to a published glossary entry (coverage report = 100% of registered keys); help panel opens contextually from every screen; ≥ 40 tutorial videos with captions and transcripts published (Appendix P §P.5) |
| Accessible | WCAG 2.2 Level AA conformance of the public site and of every authenticated screen shipped to date, evidenced by automated checks in CI (zero serious/critical axe violations), a manual assistive-technology test cycle and an independent IAAP-certified audit; an Accessibility Conformance Report (ACR) published in human- and machine-readable form; an accessibility grievance channel live (NN-21) |
| Measurable discoverability | Search Console and Bing Webmaster verified; IndexNow pings on publish; a monthly "AI answer panel" of 30 fixed buyer prompts runs and reports named/cited presence separately (§4M.12) |

---

### Exit gate

1. `apps/public` with all page types, server-rendered, on the CDN, with the legacy redirect map applied.
2. `web` and `hlp` modules with console screens (SCR-WEB-30…35, SCR-HLP-10…15), APIs, events and jobs.
3. Health check live for 12 families with published banks and scoring model v1.0 (Appendix P §P.3), PDF and share links, Hub hand-off, trial pre-fill.
4. Claims Register populated for every live claim; prohibited-phrase lint.
5. Glossary ≥ 400 published terms (first 152 per Appendix P §P.4 reviewed by a regulatory reviewer), coverage check = 100%.
6. Help centre with ≥ 120 articles mapped to help keys; help panel on every shipped screen.
7. ≥ 40 tutorial videos with corrected captions, transcripts and quick cards; ISL renditions for the 12 getting-started videos; social derivatives handed to the Hub.
8. Accessibility: token corrections merged; component contract; preferences page; CI gates; manual AT matrix signed; independent IAAP audit report; ACR (VPAT 2.5 INT + IS 17802 map) and Accessibility Statement published; grievance channel live.
9. SEO/GEO: structured data per page type, sitemaps, robots/AI-crawler policy approved by the owner, llms.txt, Search Console/Bing verified, AI answer panel baseline recorded.
10. Trust Centre and security.txt.
11. Documentation: `docs/phases/P23-plan.md`, content style guide, accessibility playbook, tutorial production guide, health-check methodology note (public).

**Exit gate:** all §12 scenarios and NN tests green; Core Web Vitals and Lighthouse budgets met; no serious/critical accessibility defects open; owner sign-off on health-check methodology, band texts and disclaimer; DPO sign-off on the health-check notice and retention; claims reviewed by the Company Secretary.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-44; X-07 (no bureau pulls in the health check), X-18, X-20 (corrected tokens), X-21, X-22, X-39 (Hindi), X-40 (AI-crawler default)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).


---

## Phase P24 — Engineering Governance, Hardening, Certification Readiness and Go-Live

**Session prompt (type in Claude Code):** *"Read docs/00-master-prompt.md, docs/01-decision-log.md and docs/phases/P24_Engineering_Governance_Hardening_Certification_Readiness_and_GoLive.md in full, plus the appendices it names as binding. Then write docs/phases/P24-plan.md with the five inventories of master §0 and stop for my approval."*

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (CI/CD skeleton, audit ledger, buckets, infrastructure), P01 (identity, grants, break-glass), P02 (settings registry), and every functional phase whose scope is being released. The **first P24 run** (general-availability go-live) needs P00–P07, P15 (at least the RBI-NBFC, MCA-CO and DATA-PRIV families), P18 (integration gateway core), P19 (export package) and P20 (billing). Later phases released after go-live each **re-run the P24 checklist for their scope** (§13.3).
>
> **Sequencing:** the engineering-governance part (§4A–§4E) starts in parallel with P02 (sprint 3 of the programme) so that every later phase is built under the final controls; hardening, certification evidence and go-live (§4F–§4K) run before general availability.
>
> **Binding appendices:** Q (security, privacy and certification readiness — control set and evidence catalogue), B (eng tables, error codes), A (change, release, incident, vulnerability state machines), U (settings), V (acceptance catalogue — the go-live regression suite), X (Operations Hub addendum — OH13/OH14 interfaces).
>
> **Requirements covered:** R-033, R-046, R-047 (engineering staff across group repositories), R-031, R-021 (preservation across releases and infrastructure moves), R-075, R-081 (backups and BYO storage evidence), R-101 (final review discipline).
>
> **Decisions applied:** D-01, D-02, D-03 (OH13/OH14 own the group console and provider-assurance room), D-13, D-14, D-21.
>
> **Estimated effort:** governance track 3 sprints (platform squad of 4) running alongside P02–P05; hardening and go-live track 4 sprints (squad of 7: SRE, 2 security engineers, QA lead, 2 backend, compliance analyst) before GA; each later re-run 1 sprint.

### Objective and business outcome

The owner will push code to GitHub regularly — patches, new features, framework upgrades, infrastructure moves — while banks, NBFCs, listed companies and co-operative societies rely on LawDocsComply for records that regulators, auditors and boards will inspect. P24 makes change safe and provable: every change is reviewed, tested, approved, traceable to a release and reversible; data and the client's folder structure survive every release and every infrastructure move; backups are tested by restoring them; vulnerabilities are found and fixed within published SLAs; and the platform is ready for independent assurance — SOC 2 Type 1 then Type 2, ISO/IEC 27001:2022, ISO/IEC 27701, ISO/IEC 42001 (AI), ISO 22301 (continuity) and PCI DSS self-assessment for the payment flow — without making any certification claim before a certificate or report exists (NN-19).

| Outcome | Exit-gate measure |
|---|---|
| Every production change is approved and traceable | 100% of production deployments in the last 30 days map to a change record with `ChangeApproved` (OH13) and a signed image digest; 0 deployments outside the pipeline |
| Releases never break client data or folder structure | Expand-contract checker, export-mapping contract (NN-10) and golden export comparison pass for every release; zero manual customer migration steps in release notes (NN-11) |
| Recoverability proven | Latest restore test of every T0 store succeeded within RTO; a full DR drill to ap-south-2 met RPO ≤ 15 min and RTO ≤ 4 h; evidence stored |
| Security debt under control | No open Critical; no High older than its SLA; VAPT (CERT-In empanelled auditor) final report issued after retest with all Critical/High closed |
| Certification-ready | Appendix Q control set implemented with automated evidence for ≥ 80% of controls; policy set approved by the Board; readiness assessment by an external firm with no Critical gaps; SOC 2 Type 1 audit window can start |
| Go-live safe | Go-live checklist (§4J) signed by CTO, CISO, Company Secretary and product owner; first paid RE tenants live on the AWS production estate (P00 ADR-0006) |

---

### Exit gate

### 13.1 Governance track (before P05 ends)
- [ ] GitHub plan decision recorded; rulesets, CODEOWNERS, required checks, merge queue, signed commits live on all repositories; drift export running.
- [ ] Change classes, change record, OH13 integration (`ChangeApproved` gate, `ReleasePublished`), freeze windows, release trains and rings in operation.
- [ ] Expand-contract checker, golden export test, content-untouched test as required checks.
- [ ] Vulnerability intake and SLA monitoring live; EOS register populated.

### 13.2 Go-live track (before GA)
- [ ] Production on AWS ap-south-1 with DR in ap-south-2; RPO/RTO verified by drill.
- [ ] Restore tests green for 4 consecutive weeks.
- [ ] Hardening checklist 100% with evidence.
- [ ] CERT-In empanelled VAPT closed (Critical/High = 0) with retest; DAST/API fuzzing clean of High.
- [ ] Performance suites within budgets; chaos tests passed with documented fallbacks.
- [ ] Incident process rehearsed (tabletop) including CERT-In 6-hour and client 2-hour clocks.
- [ ] Evidence collectors running for ≥ 80% of Appendix Q controls; policy set approved by the Board; readiness assessment completed; SOC 2 Type 1 engagement scheduled.
- [ ] Trust centre content approved through the claims register.
- [ ] Go-live checklist signed (CTO, CISO, Company Secretary, product owner); hypercare roster.

### 13.3 Re-run for later phases
Each phase released after GA runs: threat model update, VAPT scope delta (major-release VAPT if applicable), performance test of its heavy paths, export-mapping and golden export update, evidence collector additions, release notes and tenant notice, and the §13.2 items relevant to its scope. Deferred items are recorded in `docs/phases/P24-deferred.md` and close at the exit of the phase that builds them.

---

### Integration notes

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-34, NN-45; X-05, X-22; track the master §19 change requests and companion addenda to closure**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).
