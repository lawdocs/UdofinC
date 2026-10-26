# Phase P28 — Reports, MIS and Board-Pack Studio

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **New in v1.1 (25 October 2026; D-47).** Module `rpt` was declared in master §5.3 and consumed by about ten phases, but no phase owned it (G5 error E-02). This phase is now the owner of the reporting semantic layer, the dashboard and widget framework, the report catalogue and builder, the scheduler and subscriptions, the MIS framework and catalogue, the report- and board-pack studio, report exports, embedding and analytics feeds. All content in this file is *(v1.1)*.
>
> **Dependencies:**
> - **P00** (tenancy, RLS, audit ledger, Correction Entries, outbox, Temporal, object storage with Object Lock);
> - **P01** (identity, roles, ABAC attributes — legal entity, department, sensitivity; step-up MFA);
> - **P02** (settings registry, rule packs, terminology, tenant branding; every `rpt.*` key is registered before use, NN-28);
> - **P04** (compliance instances, the Compliance Score, Work Inbox, notification service and budgets, calendar);
> - **P06** (board and committee meetings, board portal and meeting book — P28 packs are delivered into P06 meetings);
> - **P07** (`packages/docgen`, DMS, PDF/UA and DOCX rendering, retention, legal hold);
> - **P09** (governed metric definitions, values and certification — P28 never computes a regulatory metric).
>
> **Consumes (stated fallbacks if not yet built):** datasets published by P03, P05, P08, P10–P14, P16, P20, P26, P27 (each module registers its datasets; until a module exists its catalogue entries are hidden); P17 (Vidhi narration and natural-language report drafting — without it, the report builder works manually); P18 (embed tokens, OData/REST feeds, webhooks — without it, embedding is off); P19 (export mapping of report definitions, runs and packs); P25 (`FX_RATE_PORT`, regional cells — without it, single-currency INR views only).
>
> **Sequencing:** two tracks. **Core track (Wave 1, sprints aligned with P04's interface freeze):** semantic layer, KPI dictionary, dashboard runtime (`packages/dashboards`), role home dashboards (SCR-RPT-01/02), basic report catalogue, run-and-export, scheduler — because P04, P06 and P08 dashboards and the Wave-1 board compliance report depend on them. **Studio track (Wave 2):** ad-hoc builder, MIS catalogue and tiers, pack studio, inspection MIS file, embedding and feeds, natural-language reports, due-diligence snapshot.
>
> **Binding appendices:** C (widget catalogue §C.6.1, default layouts §C.6.2, personalisation §C.6.3, next-best action §C.6.4, design tokens §C.8), H (§H.0A metric ownership; §H.6.3 aggregation and currency rules), B (data model and event naming), D (roles and permissions), U (settings), M (export folders), K and AA (Vidhi skills, autonomy levels, MCP tools).
>
> **Requirements covered:** R-012 (CRO dashboard), R-013 (reports, exports), R-021 and R-076 (exports in open formats), R-024 and R-028 (customisation, fewer clicks), R-030 (dashboards per user type), R-059 (KMP dashboards, customisable), R-061 (CFO ratio dashboard), R-067 (savings and value reports with P20), R-075 and R-088 (audit-trail reports), R-092 and R-099 (committee and board packs), R-023 (faster cross-team workflows), R-031 (privacy by design), R-022 (accessibility).
>
> **Estimated effort:** 9 two-week sprints, squad of 8 (semantic layer and KPI dictionary 2; dashboard runtime and widgets 2; reports, builder and scheduler 2; pack studio and renderers 1.5; QA and accessibility 0.5), plus a part-time MIS/board-reporting analyst (company secretary or CA) for the MIS catalogue and pack templates. Core track: sprints 1–4; studio track: sprints 5–9.

---

## 1. Objective and business outcome

Every module of LawDocsComply produces information that someone must read, decide on, or send to the Board, a committee, an auditor or a supervisor. Today most Indian regulated entities assemble this information in Excel and PowerPoint, re-keying numbers from several systems, with no proof of where a figure came from and no way to reproduce last quarter's pack. Users of incumbent GRC tools report the same pain: reports that need the vendor to change, dashboards rebuilt user by user, board packs built outside the tool, and large reports that time out (Appendix Z §Z.9; IMP-071 to IMP-075, IMP-141).

P28 gives one governed reporting layer for the whole product: every module publishes its data once as a **governed dataset**; every number shown anywhere comes from that layer (and, for financial and risk metrics, from P09's certified values); every report and pack can be re-run "as at" its original date and produce the same result; and business users — not the vendor — build their own dashboards, reports and packs.

| Outcome | Exit-gate measure |
|---|---|
| One source of numbers | Every widget, report cell and pack figure resolves to a dataset field or a P09 metric version with provenance and as-of date; a CI check fails any widget bound to an ungoverned query |
| Role dashboards on day one | Each of the 22 role layouts in Appendix C §C.6.2 renders from seed data with mandatory widgets, drill-down to records in ≤ 3 clicks and "View as table" on every chart |
| Users build their own | A CCO builds a custom "overdue High checkpoints by department and regulator" report with a chart and formula column, saves it as a template and schedules it monthly to the MD in ≤ 10 minutes without support |
| Reproducible reports | "Re-run as at" of any approved report reproduces the original output byte-for-byte (same snapshot hash, template version and parameters) |
| Board packs inside the product | The pilot NBFC-ML composes its quarterly Board compliance and risk pack from saved sections, freezes it (hash), and the CS attaches it to the Board meeting in P06 — no Excel or PowerPoint outside LDC |
| MIS catalogue | The seed MIS catalogue (§4G) is installed for the pilot family with owners, frequencies, recipients and approval paths; the RBI inspection "Management and Systems" MIS file (§4H) is produced in one run |
| Performance | Dashboard p95 < 2 s at 50,000 compliance instances per tenant; a 50,000-row report completes asynchronously in < 2 minutes with notification; a 200-page pack renders in ≤ 60 s |
| Safe AI assistance | Vidhi drafts report definitions and variance commentary from bound values only; a narrative containing an unbound figure cannot be published (NN-37) |

---

## 2. Scope (in / out)

**In scope**
- `rpt` schema and services: dataset registry, field catalogue, data classes and row policies; KPI dictionary; metric bindings to P09; point-in-time snapshots.
- `packages/dashboards` (widget runtime used by every app shell), widget catalogue management, role layouts, personal and shared dashboards, dashboard library, next-best-action card host.
- Reports tab: catalogue, run, my reports, ad-hoc builder (no code), templates with inheritance, scheduler, subscriptions, approvals, distribution, retention.
- MIS framework: four MIS tiers, fourteen MIS categories, MIS metadata schema, seed MIS catalogue, inspection MIS file mapping, standard administrative and management reports.
- Report- and board-pack studio: compose, version, review, approve, freeze/hash, watermark, render (DOCX, PDF and PDF/UA, PPTX, XLSX), distribute to P06 meetings and to subscribers, addenda.
- Natural-language report drafting and narrative commentary with Vidhi (bound figures only).
- Embedding (signed embed tokens) and analytics feeds (OData/REST with RLS) for Power BI, Excel and other BI tools.
- Group, multi-entity and multi-currency views; localisation of labels and formats.
- Due-diligence snapshot (§4N); anonymised cross-tenant benchmarking (flag OFF).
- Export mapping of report definitions, runs, packs and snapshots (NN-10).

**Out of scope**
- Computing regulatory, financial or risk metrics (P09 owns definitions, computation and certification — Appendix H §H.0A).
- Meeting logistics, notices, attendance, minutes and the board portal itself (P06). P28 supplies packs and report papers to P06 meetings.
- Preparing or filing regulatory returns (P11; NN-08). Regulator-format MIS in P28 is for internal and inspection use, not filing.
- Replacing an enterprise BI tool: P28 provides governed feeds to external BI tools rather than a general-purpose analytics workbench.
- Marketing and platform-operations analytics (Operations Hub OH2 and P24 engineering metrics).

---

## 3. Personas and permissions touched

| Role code | What they do in P28 | Notes |
|---|---|---|
| `ten_admin` | Publishes tenant dashboard defaults, manages report catalogue entitlements, branding, embedding and feeds | Cannot see sealed-class datasets (NN-13) |
| `ten_cco`, `ten_kmp` (CEO, MD, CFO, CRO, CCrO, CS, CISO, DPO, GRO, IA head, CHRO, GC, CSO, AIO) | Own role dashboards; author, approve and distribute reports in their domains; compose packs for their committees | Permissions are per dataset domain and legal entity (ABAC) |
| `ten_dept_head` | Department dashboards and reports; copies dashboards to the department (IMP-075) | Scoped to own department tree |
| `ten_maker`, `ten_checker` | Personal dashboards; run catalogue reports within their scope | — |
| `ten_board_member`, `ten_committee_member` | View published packs and board dashboards; private annotations in P06 portal | Read-only; UPSI rules apply (P06) |
| `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor` | Run audit-trail, evidence and control reports within grant scope; receive packs shared with them | Assurance shell; time-boxed grants |
| `ten_supervisor_view` | Views packs and reports explicitly included in the D-12 grant | Watermarked "Shared with [regulator] under grant [id]" |
| `dlv_rm`, `dlv_professional` | Prepare reports and draft packs as makers under a delivery grant | Never approve or freeze (NN-43) |
| `plt_content_*` | Maintain master report and pack templates, seed MIS catalogue and KPI dictionary entries | Platform templates are Governed; tenants inherit and override |
| `svc_vidhi` | Drafts report definitions, narrative commentary, director question prompts — on behalf of a named user | Autonomy ceiling L2 (drafts only); never approves, freezes, distributes (NN-04, NN-14, NN-50) |

New permission set (registered in Appendix D *(v1.1)*): `rpt.reports.view`, `rpt.reports.run`, `rpt.reports.build`, `rpt.reports.publish`, `rpt.reports.approve`, `rpt.dashboards.publish_template`, `rpt.packs.compose`, `rpt.packs.approve`, `rpt.packs.freeze`, `rpt.feeds.manage`, `rpt.embed.manage`, `rpt.mis.manage`. Separation of duties: the author of a report or pack cannot be its approver (NN-05); freezing a Board-tier pack requires the approver and, where configured, the committee chair or CS.

---

## 4. Functional requirements

### 4A. Semantic layer and governed datasets

**FR-P28-01 — Dataset registry.** Every module registers its reportable data as **governed datasets** in `rpt.datasets` through a registration contract (`packages/dashboards/register-dataset`): dataset id (`<module>.<name>`, e.g., `cmp.instances`, `erm.kri_observations`, `ral.metric_values`, `aud.findings`, `grv.tickets`), owner module and owner role, grain, fields (name, type, unit, description, "i" help key, data class, sensitivity), allowed joins (declared keys only), row-policy expression (CEL over tenant, legal entity, department, assignment and sensitivity attributes), freshness SLA, retention class and export mapping. A module's phase is not done until its datasets are registered (master §15 Definition of Done, extended *(v1.1)*).

**FR-P28-02 — Read-only metric bindings.** Financial and risk metrics are not datasets that P28 computes; they are **bindings** to P09 metric versions (`ral.metric_values`) with value, version, as-of, provenance badge (`FX`, `UD`, `LDC`, `XLS`, `MAN`) and certification state (COMPUTED → … → CERTIFIED). A widget or report cell that shows a regulatory metric must display its certification state; indicative values are labelled "Indicative" with the reason (P09 FR-P09-18).

**FR-P28-03 — Data classes and sealed data.** Fields carry data classes (Appendix Q). Sealed classes (POSH cases, whistle-blower reports, complainant identity, health and disability, disciplinary, payroll, board-confidential, regulator-confidential, credentials) are never exposed to general datasets; where aggregate counts are needed (for example POSH case counts for the IC presiding officer, W-HR-06) a dedicated aggregate dataset with k ≥ 5 suppression is published by the owning module (X-36; NN-13). Report builders never see sealed fields in the field picker.

**FR-P28-04 — KPI dictionary.** One registry (`rpt.kpis`) holds every KPI shown on any dashboard: KPI id, name, plain-language definition, formula reference (P09 metric id, dataset aggregate expression or P04 score), unit, polarity, owner role, refresh frequency, thresholds (with source: regulatory floor from P09/P08, Board appetite, management target), "i" text and accessibility description. P04 compliance KPIs, P08 KRIs (linked, not duplicated), P09 ratios, P14 grievance KPIs, P20 savings figures and P23 health-check scores are all entries. Widgets refer to KPI ids, never to raw queries (CI check).

**FR-P28-05 — Four distinct scores (G5 error E-06; Appendix B §B.1.1) *(v1.1, X1 aligned)*.** The dictionary defines four different scores that must never be shown on one tile without their label: **Compliance Score** (P04; live, instance-based, weighted by risk), **Health Check Score** (P23; free 50-question self-assessment at a point in time), **Set-up Readiness Score** (P01 FR-P01-44; completeness of configuration after onboarding) and **Compliance Health Index** (optional five-component method defined in P04 FR-P04-82 — components and weights as stated there — selectable by `cmp.score.method`; P28 publishes it as KPI `cmp.compliance_health_index`). Each tile shows the score name, method version and as-of date.

**FR-P28-06 — Point-in-time snapshots.** Reports and packs run against a **snapshot**: a consistent read of the datasets used (transaction-time cut-off), stored as a manifest of dataset versions, row counts and content hashes, with large result sets materialised in object storage. Snapshots are immutable and referenced by every run; "Re-run as at" re-reads the bitemporal sources at the snapshot's cut-off (NN-07) and must reproduce the original output (NN-22).

**FR-P28-07 — Performance architecture.** Hot aggregates are materialised per tenant (`rpt.mv_*`, refreshed on events and on schedule); widget queries have a 500 ms budget; reports above the synchronous threshold (default 10,000 rows or 5 seconds estimated) run asynchronously on Temporal with progress and a notification on completion (IMP-141). Query cost limits per tenant and per user prevent noisy-neighbour effects; heavy users are told which filter will make a report faster.

### 4B. Dashboard framework

**FR-P28-08 — Widget runtime (`packages/dashboards`).** One runtime renders every dashboard in every shell (tenant, board, assurance, self-service, console, delivery). Widget types: single value with sparkline and RAG text, gauge/ring, bar/column/line/area, stacked and 100% charts, heat map (with table alternative), matrix (e.g., department × regulator), top-N list, movement table, kanban mini, funnel, calendar strip, map by state/district/branch, table with conditional formatting, text/markdown note, next-best-action card, embedded report. Every widget shows title with "i" help, as-of and refresh interval, provenance and certification badges where relevant, drill-down to the filtered record list, export (PNG, CSV, XLSX) and "View as table" (NN-21).

**FR-P28-09 — Widget catalogue.** The catalogue is Appendix C §C.6.1 (`cfg.widget_catalogue`), extended *(v1.1)* with: W-RSK-07 Early-warning signals (P08 FR-P08-61), W-RAL-10 Stress result cards (P09 FR-P09-62), W-RET-05 Prepare-due status (P11 FR-P11-85), W-RET-06 Data-quality scorecard (P11 FR-P11-87), W-RPT-01 Reports awaiting my approval, W-RPT-02 Scheduled reports failed or late, W-RPT-03 Packs in preparation (by meeting date), W-RPT-04 MIS catalogue compliance (MIS items produced on time by tier), W-RPT-05 Alert health (notifications per user per day, open rate; IMP-046), W-RPT-06 AI activity summary (drafts, acceptances, rejections, guardrail events; IMP-140), W-LIT-01 Litigation and notices summary (P26), W-ESG-01 ESG/BRSR readiness (P27), W-GRP-01 Group entity status (one row per legal entity). Modules add widgets by registering them against KPIs and datasets.

**FR-P28-10 — Role dashboards.** The default layouts of Appendix C §C.6.2 are seeded as **role templates** (versioned): maker, checker, department head, CCO, CEO, MD/WTD, CFO, CRO, CCrO, CS, CISO/CTO/CIO, DPO, GRO/PNO, Internal Ombudsman, HR admin, internal auditor, external auditor, Board member, supervisor view, `ten_admin`, `plt_super_admin`, content team, RM, employee, co-operative office bearer. *(v1.1)* additions: General Counsel (P26 matters, notices, regulator observations), Chief Sustainability Officer (P27), CHRO (P13 people metrics), AI Officer (`OV_AI` model inventory and AI incidents; Appendix AA), Audit Committee, RMC, ALCO and ITSC committee views (from P08/P09 FR-P09-52 content). Entity-family packs swap widgets (Appendix C §C.6.2 note).

**FR-P28-11 — Personalisation and sharing.** Per Appendix C §C.6.3: add, remove (except mandatory), resize, reorder, filter, pin a saved view, up to 5 personal dashboards, "Reset to role default". *(v1.1)* additions: **copy dashboard** to a role or department as a tenant template (requires `rpt.dashboards.publish_template`; IMP-075); **tenant dashboard library** with descriptions, owners and usage counts; **"view as"** (delegation, logged) for executive assistants; personal alert thresholds tighter-only for KRIs (P08 FR-P08-30). Changing a Board or committee template needs the chair's or CS's approval.

**FR-P28-12 — Context bar and filters.** Every dashboard inherits the context bar (tenant → group → legal entity → period → currency) and supports saved filter sets. Filters are applied server-side through row policies; a user never sees a count they could not drill into (no "phantom" counts).

**FR-P28-13 — Next-best-action host.** The runtime hosts the deterministic next-best-action card (Appendix C §C.6.4). P28 renders and records clicks; rules stay in `cfg.nba_rules` (P02).

### 4C. Reports tab

**FR-P28-14 — Navigation.** Left-rail item **Reports** (permission `rpt.reports.view`) with sub-menus: **Catalogue** (entitled reports by source module and audience tier, search and favourites) · **My reports** (status Draft / Awaiting approval / Approved / Distributed / Archived; re-run; duplicate) · **Run a report** (parameters: legal entity, period, scope, comparison period, currency, language; formats; preview) · **Builder** (ad-hoc) · **Scheduled** (cadence, next/last run, recipients, failures) · **Packs** (pack studio, §4I) · **MIS catalogue** (§4G) · **Regulatory filings** (link to P11 Return Studio; filing is P11) · **Approvals** (maker-checker on reports and packs).

**FR-P28-15 — Audience tiers.** Each report and pack has a tier that sets defaults for approval, distribution, retention and confidentiality:

| Tier | Typical recipients | Default approval | Default distribution | Default retention | Default confidentiality |
|---|---|---|---|---|---|
| Operational | Makers, checkers, team leads | None (self-service) | In-app, e-mail | 2 years | Internal |
| Management | Department heads, KMPs, executive committees | Maker → domain owner (e.g., CCO) | In-app, e-mail, Teams/Google Chat link | 8 years | Restricted |
| Board / Committee | Board, Audit Committee, RMC, NRC, ALCO, ITSC | Maker → KMP owner → CS (freeze) | P06 board portal only (no e-mail attachments) | Permanent (with minutes) | Highly Restricted |
| Regulator / Supervisor | Supervisor view grantees, inspection teams | Maker → CCO → MD/CEO (or delegate) | D-12 grant or secure link with expiry; never e-mail attachments by default | 10 years | Highly Restricted |

All defaults are Tenant-configurable within floors (Board/Regulator tiers cannot drop approval or move to e-mail attachments without a G-tier change).

**FR-P28-16 — Seed report catalogue.** Each module contributes catalogue entries; the seed set at P28 exit includes at least: compliance status by regulator/department/entity; overdue and due-soon registers; checker turnaround and rework; exceptions, waivers and extensions; regulatory change impact and acknowledgement; policy review and attestation coverage; meeting and minutes compliance; filings calendar status (MCA, LODR); risk register and movements; KRI breaches and episodes; loss events; RCSA completion; capital, liquidity and asset-quality summaries (bound to P09); stress-test results summaries; audit plan progress and findings ageing; returns status and acknowledgements; CIC cycle quality; grievances by category and TAT; DPDP requests and incidents; vendor risk and outsourcing register; HR headcount and labour compliance; litigation and notices (P26); ESG/BRSR readiness (P27); user activity; penalty exposure (indicative); savings and value (P20); AI activity; audit-trail extract.

### 4D. Ad-hoc report builder

**FR-P28-17 — No-code builder (IMP-074).** Steps on one screen: choose dataset(s) (only permitted ones; joins limited to declared keys) → pick fields (search by business name; "i" help shows definition) → filters (relative dates such as "this quarter", "last 3 periods"; parameters exposed to the runner) → groupings and sorting → measures (count, sum, average, min/max, distinct count, percentage of total, period-over-period change) → **formula columns** in CEL with unit and type checks (e.g., `overdue_days * risk_weight`) → visual (table, pivot, chart types of §4B) → conditional formatting → preview on live data with row count and cost estimate → save as personal, shared or tenant template. Formula columns can never redefine a P09 metric; they compute only on non-metric fields or display P09 values as they are.

**FR-P28-18 — Templates with inheritance.** Report and pack templates exist at three levels — **platform master** (content team; Governed), **tenant** (inherits master; may add sections, columns, branding, commentary blocks; cannot remove mandatory regulatory sections), **legal entity** (inherits tenant). When a regulation changes a master template (for example a new mandatory Board report item), the change cascades to tenant and entity templates as a proposed update with a diff; the tenant accepts or the change auto-applies on its effective date for mandatory items (NN-34). Each run records the template version used.

**FR-P28-19 — Reusable report sections.** Any saved report or widget can be saved as a **section** for packs (§4I) with its parameters bound to the pack context (entity, period).

### 4E. Report lifecycle, approvals and reproducibility

**FR-P28-20 — Seven stages.** (1) **Select** report and parameters → (2) **Resolve** data from the semantic layer into a point-in-time snapshot → (3) **Compute and validate** (data-quality checks: completeness of required datasets, freshness against SLA, reconciliation checks declared by the template; failures shown before rendering) → (4) **Render** (PDF, PDF/UA, XLSX, CSV, DOCX, HTML, PPTX, JSON) → (5) **Approve** (maker-checker per tier) → (6) **Distribute** (in-app, e-mail link, Teams/Google Chat link, P06 portal, secure link with expiry, supervisor grant) → (7) **Archive** (signed output + snapshot manifest + template version + parameter set + event log in WORM storage; NN-09).

**FR-P28-21 — Reproducibility (IMP-072).** Every approved run stores parameters, snapshot hash, template version, renderer version and output hash. **Re-run as at** reproduces the run; a differing output hash raises a Critical incident and the original remains authoritative. A **Re-run with current data** creates a new run linked to the original with a change summary ("47 instances changed status since the original run").

**FR-P28-22 — Corrections to issued reports.** An approved and distributed report is never edited. A correction is a new version marked "Supersedes version n" with the reason; recipients of the original are notified; Board-tier corrections become addenda (§4I) delivered into the P06 meeting. Changes to underlying records after issue are handled by Correction Entries in the source modules (NN-02).

### 4F. Scheduler and subscriptions

**FR-P28-23 — Cadences.** Daily, weekly (day), fortnightly, monthly (day or "nth working day"), quarterly, half-yearly, annual, financial-year anchored, **regulator-defined dates** (e.g., "within 21 days of quarter end", "30 days after AGM", "before the Board meeting") using the P02 calendar engine with holiday calendars, and **meeting-anchored** schedules (T−n working days before a P06 meeting).

**FR-P28-24 — Lead-time generation.** For statutory or Board-tier reports the scheduler generates a draft at T−n (default 10 working days) so that makers can review data quality before the approval deadline; missing data creates tasks for dataset owners (P04).

**FR-P28-25 — Subscriptions and digests.** Users subscribe to reports and dashboards (in-app, e-mail link, Teams/Google Chat); subscriptions respect the user's notification budget and quiet hours (P04 fatigue settings, G5 E-19) and bundle into the daily work digest (08:30) unless the user selects immediate delivery. Board-tier content is never attached to e-mail; subscribers receive a link that requires login.

**FR-P28-26 — Failure handling.** A failed scheduled run retries (3 times with back-off), then notifies the owner with the failing step and a suggested fix; repeated failures surface on W-RPT-02.

### 4G. MIS framework

**FR-P28-27 — Design principles.** The MIS framework (seeded from the owner's baseline, Architecture Part 1 §30, and Part 3 "Reports") follows: single source of truth (governed datasets only); design right-to-left from the recipient's decision; automate production; audit-ready (snapshot, approvals, archive); tiered by audience; frequency fitted to the decision; configurable taxonomy; aligned to regulator expectations; privacy by design (sealed classes excluded; minimum necessary detail per tier).

**FR-P28-28 — Four MIS tiers.** L1 Operational (daily; makers, team leads), L2 Tactical (weekly/monthly; department heads), L3 Management (monthly/quarterly; KMPs, executive committees), L4 Governance (quarterly and event-driven; Board and Board committees). Each MIS item declares its tier, which sets defaults from FR-P28-15.

**FR-P28-29 — Fourteen MIS categories with second-line owners.** (1) MIS catalogue and governance (CCO); (2) Board and governance (CS); (3) Compliance and regulatory (CCO); (4) Risk (CRO); (5) Finance and treasury (CFO); (6) Credit and operations (CCrO / COO); (7) Audit and internal control (Head of IA); (8) HR and people (CHRO); (9) IT, cyber and data protection (CISO / DPO); (10) Sector-specific — RBI, SEBI, IRDAI, IFSCA, co-operative registrar (CCO); (11) Customer service and grievance (GRO / PNO); (12) Fraud and AML (MLRO / Principal Officer); (13) ESG and sustainability (CSO); (14) Litigation, notices and recovery (General Counsel). Category owners approve additions to their category.

**FR-P28-30 — MIS metadata schema.** Every MIS item in the catalogue (`rpt.mis_items`) carries: MIS ID (`MIS-<CAT>-<nn>`), title (≤ 8 words), category and sub-category, tier, frequency, source datasets, data owner, generator role, approver role, recipients (roles or named bodies), distribution mode, regulator and citation (where the MIS is required by law or regulator), KPI/KRI links, retention class, confidentiality (Public / Internal / Restricted / Highly Restricted), formats, sample output and "last produced" status. The catalogue is itself a report (W-RPT-04 shows on-time production by tier).

**FR-P28-31 — Seed MIS catalogue.** Seed items per category (platform content; titles normalised from the owner's baseline tables; families switch items on or off via P15 applicability):

| Category | Seed items (examples; ≥ 60 items at exit) |
|---|---|
| Governance (GOV) | MIS-GOV-01 Board governance dashboard and compliance health; -02 Directors and KMP register summary; -03 Committee composition and meeting compliance; -04 Minutes and decision log with action-taken status (IMP-081); -05 Statutory filings status (MCA, LODR); -06 Group holding and related-party summary; -07 Corporate governance attestations; -08 Fit-and-proper and director KYC status |
| Compliance (COMP) | MIS-COMP-01 Compliance calendar tracker; -02 Non-compliance and breach register; -03 Policy register and review status; -04 Outsourcing register summary; -05 Litigation and notices register (P26); -06 Regulator correspondence log; -07 Penalty, fine and stricture register; -08 Regulatory change impact tracker; -09 Inspection/RBS observations and closure status (P26); -10 Compliance testing results; -11 Exceptions, waivers and extensions; -12 Quarterly compliance report to the Board; -13 CCO annual compliance plan progress |
| Risk (RM) | MIS-RM-01 RAS scorecard; -02 Top risks and movements; -03 KRI breaches and episodes; -04 Loss events and near misses; -05 Stress-test summary (P09 result cards); -06 Capital and liquidity summary (P09); -07 Early-warning signals (P08) |
| Audit (AUD) | MIS-AUD-01 Audit plan progress; -02 Open findings and ageing with repeat flags (IMP-057); -03 Cross-engagement executive summary for the Audit Committee (IMP-088) |
| Control (CTRL) | MIS-CTRL-01 Control coverage and automated test results (P08 FR-P08-60) |
| Finance (FIN) | MIS-FIN-01 Financial ratio pack (P09); -02 Returns calendar and acknowledgements (P11); -03 GST and TDS status |
| Credit (CR) and Operations (OPS) | MIS-CR-01 Asset quality and SMA summary (from Finbyx/LMS); -02 Concentration versus limits; MIS-OPS-01 Branch and process compliance status |
| Treasury (TRY) | MIS-TRY-01 ALM and liquidity summary (P09) |
| HR (HR) | MIS-HR-01 Headcount, attrition and key-person vacancies (aggregated, X-36); -02 Labour compliance calendar status |
| IT, cyber, DPDP (IT/DPDP) | MIS-IT-01 Cyber incidents and clocks; -02 VAPT and IS audit open items; MIS-DPDP-01 Data-principal requests and breaches |
| Customer (CUS) | MIS-CUS-01 Grievances by category, TAT and escalation; complaint-disclosure tables (P14) |
| Fraud and AML (FRD) | MIS-FRD-01 Frauds reported and FMR status; -02 STR/CTR filing tracker (counts only; tipping-off protection — no customer detail outside AML roles) |
| ESG (ESG) | MIS-ESG-01 BRSR readiness and ESG KPIs (P27) |
| Litigation (LIT) | MIS-LIT-01 Matters by forum and stage; -02 Hearings this month; -03 Contingent liabilities by matter; -04 Notices received and response status; -05 Regulator orders and directions; -06 Recovery-related matters (consumed from Finbyx Recovery Suite, D-41) |

**FR-P28-32 — Standard administrative and management reports (G5 gaps).** User activity (tasks assigned vs completed per user, submissions, logins — for administration and coaching, not covert monitoring, NN-25); **penalty exposure** (non-complied and late items × penalty rule packs = indicative exposure by Act, entity and location, labelled "indicative, not legal advice", NN-19); state-wise and location-wise compliance; third-party compliance; audit-trail report (record history, Correction Entries, access log extracts, NN-02); access transparency (every platform support or break-glass access to the tenant, NN-30; IMP-112); AI activity (IMP-140); alert health (IMP-046); quarterly value report to the tenant admin with the P20 savings method per figure (IMP-109).

### 4H. RBI inspection "Management and Systems" MIS file

**FR-P28-33 — Inspection file builder.** RBI supervisory inspections and RBS assessments begin with data and document requests covering organisation, governance, compliance, risk, audit, IT, customer service and business data. P28 ships a mapping template (`rpt.inspection_maps`) from a configurable list of inspection request topics (for example staff list and organogram → MIS-HR-01 and the HRMS org chart; KMP details → MIS-GOV-02; committee meetings → MIS-GOV-03; compliance testing → MIS-COMP-10; frauds → MIS-FRD-01; complaints → MIS-CUS-01; IT incidents → MIS-IT-01) to catalogue reports and DMS document sets. One run produces a numbered folder of outputs and an index workbook, ready for the CCO's review. The topic list is content, not code, and is marked [VERIFY] against the current RBI request formats; the inspection response itself is managed in P26 (regulator inspections and observations).

### 4I. Report- and board-pack studio

**FR-P28-34 — What a pack is.** A **pack** is an ordered set of sections — cover and index, executive summary, report sections (§4D), dashboard snapshots, P08/P09 result cards, P04 compliance status tables, P10 audit summaries, P12 cyber and vendor summaries, P14 grievance tables, P26 litigation and observation summaries, P27 ESG tables, documents from the DMS (policies for approval, auditor reports), and free-text notes — bound to a context (legal entity, period, meeting). Packs are used for: Board and committee papers (the P06 meeting book includes the frozen pack as one or more item papers), monthly management MIS packs, regulator/inspection packs, investor and lender packs, and due-diligence snapshots (§4N).

**FR-P28-35 — Composition.** Start from a pack template (platform → tenant → entity inheritance, FR-P28-18) or "copy last pack"; sections refresh to the new period automatically; each section shows data-quality and freshness status; the composer assigns section owners with due dates (tasks in P04) and sees a progress board. Mandatory items per family and body come from the template (e.g., RMC standing items from P08 FR-P08-43; quarterly compliance report items).

**FR-P28-36 — Narrative and figures (NN-37).** Narrative blocks may be written by humans or drafted by Vidhi; every figure in narrative text is a **bound placeholder** to a section value, KPI or metric version. A pre-freeze check fails if narrative text contains a numeral that is not bound (dates, paragraph numbers and section references are excluded by rule). Result cards from P09 carry their own bound summaries.

**FR-P28-37 — Review, approval and freeze.** Pack states: `DRAFT → COMPOSED → IN_REVIEW → APPROVED → FROZEN → DISTRIBUTED → (ADDENDUM)* → ARCHIVED`. Freeze computes a SHA-256 over every rendered page, bound value, metric version, template version and narrative; frozen packs are WORM-stored (NN-09) and cannot change. Late changes create an **addendum** (a new small pack referencing the original) rather than editing the frozen pack (P08 FR-P08-42 pattern).

**FR-P28-38 — Rendering.** DOCX (styles, headings, table of contents, bookmarks; editable for the CS before freeze), PDF and PDF/UA (tagged, accessible, bookmarked, page-numbered, per-recipient watermark with name and timestamp), PPTX (one slide per section with speaker notes; charts as native or high-resolution images with alt text), XLSX (data appendix with lineage sheet). Render time budget ≤ 60 s for 200 pages; larger packs render asynchronously with notification.

**FR-P28-39 — Distribution to P06 and others.** Board-tier packs are published only into the P06 meeting (board portal), inheriting the meeting's access list, UPSI handling and Structured Digital Database entries for listed entities (P06). Management packs distribute by in-app link and subscription; regulator packs by supervisor grant or secure link with expiry and access log.

**FR-P28-40 — Director question prompts (IMP-079).** Optionally, Vidhi drafts "questions a director may ask" for a Board-tier pack — each question cites the source records (overdue High checkpoints, repeat findings, KRI breaches, audit observations, regulator observations). The CS reviews and releases them; they are visible only to members of the body and labelled AI-drafted (NN-04, NN-14).

**FR-P28-41 — Board pack generator (IMP-071).** One click "Generate board pack" assembles the standard Board pack for the next meeting from the tenant's template: compliance status, regulatory changes and impact, risk and capital summaries, audit summaries, grievances, litigation, policy approvals due, action-taken report — leaving narrative blocks as drafts for owners. Target: a quarterly pack draft in under 15 minutes of user time once datasets are populated.

### 4J. Natural-language report building with Vidhi

**FR-P28-42 — "Ask for a report."** A user types a request ("overdue High compliances by department for Q2, compared with Q1, as a bar chart"). Vidhi (on behalf of the user, autonomy ceiling L2) proposes a **report definition** — datasets, fields, filters, groupings, chart — rendered in the builder for the user to review; Vidhi never returns numbers in its own text; the report engine computes them. The user runs, edits or saves the definition. Permission checks use the user's own row policies; Vidhi cannot request datasets the user cannot see (NN-41).

**FR-P28-43 — Narrative commentary.** For dashboards, reports and packs, Vidhi drafts commentary on movements and variances using bound placeholders only (FR-P28-36); the draft lists the values it used; a human approves before the commentary appears in any Management, Board or Regulator tier output (NN-04).

**FR-P28-44 — MCP and tools.** The P17 MCP server exposes `rpt.list_reports`, `rpt.run_report` (returns a link and bound figures under the calling user's permissions) and `T-rpt-get_figures` to the tenant's own AI assistants; sealed data is never returned (NN-52); runs requested through MCP are logged as AI-originated.

### 4K. Embedding and analytics feeds

**FR-P28-45 — Embedding.** Dashboards and individual widgets can be embedded in the tenant's intranet, SharePoint pages or Teams tabs using signed, short-lived embed tokens (P18), scoped to a named viewer identity (SSO) — never anonymous; embeds inherit row policies; Board-tier and Regulator-tier content cannot be embedded.

**FR-P28-46 — Analytics feeds.** Governed OData v4 / REST feeds of permitted datasets for Power BI, Excel and other BI tools, authenticated per user (OAuth) or per service account with dataset scopes; row policies and data-class filters apply; sealed classes excluded; feed usage logged. Feeds are read-only and carry dataset version and freshness metadata.

### 4L. Group, multi-entity and global views

**FR-P28-47 — Entity switcher and group dashboards.** Users with group roles switch between legal entities or see the group; group KPIs follow Appendix H §H.6.3 (recompute ratios, translate currencies at snapshot rates from `FX_RATE_PORT`, never net regulatory floors across entities).

**FR-P28-48 — Regional cells (NN-24 amended).** Entities homed in other regional cells (P25) contribute aggregate datasets only; group dashboards show which entities contributed aggregates; drill-down into a foreign entity requires a role in that entity's home cell.

**FR-P28-49 — Localisation.** Labels and report headings use the tenant's terminology (P02) and language (English default; Hindi second locale, D-30; others with P25 packs); dates, numbers (lakh/crore or international grouping per user), currencies and time zones follow user and entity settings; right-to-left layout supported in the runtime for Arabic locales (P25).

### 4M. Customisation without a super admin

**FR-P28-50 — Tenant controls.** Tenants configure without a super admin: role and department dashboard templates; tenant report and pack templates (inheriting platform masters); branding on outputs (logo, colours checked for contrast, cover page, footer, confidentiality labels); MIS catalogue additions and owners; approval paths per tier within SoD floors; distribution lists; retention above floors; subscription defaults; internal KPIs (counts and percentages over datasets) — financial and risk internal metrics go through P09 FR-P09-60; number-format and language defaults.

### 4N. Due-diligence snapshot and benchmarking

**FR-P28-51 — Due-diligence snapshot.** One click produces a point-in-time, evidence-backed compliance pack for lenders, investors, acquirers or auditors: scope selector (entities, regulators, period, sections), frozen and hashed snapshot, watermarked PDF and XLSX index, optional evidence extracts selected by the tenant, and a time-limited read-only link with access log and revocation. Sensitive classes are excluded unless the tenant admin explicitly includes them with a reason.

**FR-P28-52 — Anonymised benchmarking (flag `rpt.benchmarking.enabled` = OFF).** Consented, revocable participation; only segment aggregates with minimum cohort size (default 10 tenants) and noise where required; no tenant can be identified; methodology approved and published before activation (NN-19). Example benchmarks: on-time compliance %, median checker turnaround, grievance TAT by family.

### 4O. Accessibility and quality

**FR-P28-53 — Accessible outputs.** Every chart has a table alternative and alt text generated from bound values; colours never carry meaning alone (text RAG labels); PDFs are PDF/UA tagged; DOCX uses heading styles; PPTX slides have reading order and alt text; keyboard operation of the builder and dashboards; no drag-only interactions — every drag has a menu alternative (WCAG 2.2 SC 2.5.7; NN-21).

**FR-P28-54 — Data-quality gates.** Required datasets below freshness SLA or failing declared checks block Board-tier and Regulator-tier approval and show a reason; Operational and Management tiers render with a visible "data incomplete" banner.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P28-X01 — Report definitions contributed by other phases.** The P28 catalogue seeds definitions from: P04 (one-page compliance summary using SCR-CMP-17 data; Compliance Score; Compliance Health Index per P04 FR-P04-82); P26 (LIT_01–06, REG_01, CLM_01, LIC_01, ETH_01); P27 (ESG dashboards, BRSR progress, CSR spend, board sustainability section); P12 (Board AI report); P14 (regulator grievance MIS, Customer Service Committee pack); P13 (labour penalty exposure); P16 (society AGM pack); P10 (MIS-AUD-02/03); P20 (quarterly value report). The board-pack rendering engine is shared with P06 FR-P06-70 (one pack generator).

---

## 5. Workflows and state machines

### 5.1 Report run

`REQUESTED → SNAPSHOTTING → VALIDATING → RENDERING → READY → (SUBMITTED_FOR_APPROVAL → APPROVED | RETURNED) → DISTRIBUTED → ARCHIVED`; `FAILED` (with step and reason; retry). Guards: tier approval rules (FR-P28-15); author ≠ approver (NN-05); data-quality gate (FR-P28-54). Timers: approval SLA per tier (default Management 2 working days, Board 3, Regulator 1), escalation to the domain KMP.

### 5.2 Pack

`DRAFT → COMPOSED (all mandatory sections present) → IN_REVIEW (section owners done) → APPROVED → FROZEN (hash) → DISTRIBUTED → ADDENDUM* → ARCHIVED`. Return path from IN_REVIEW and APPROVED to COMPOSED with comments. Freeze only by a user with `rpt.packs.freeze` who is not the composer; Board-tier freeze additionally requires the CS (or committee secretary). Addenda follow the same states and reference the original hash.

### 5.3 Template change

Platform master change → `PROPOSED` → impact list (tenant templates and scheduled runs affected) → `APPROVED` (content checker) → cascades as `PENDING_TENANT_ACCEPTANCE` for optional changes or `SCHEDULED` for mandatory ones on their effective date → `APPLIED`. Tenant template changes to Board/committee tiers require the chair or CS approval.

### 5.4 Scheduled run

Cron/regulator rule → lead-time draft (T−n) → data-quality check → tasks for gaps → final run at due time → approval routing → distribution → archive. Missed due time raises an overdue flag on the MIS item (W-RPT-04).

### 5.5 Natural-language request (pseudo-code)

```
on ask_for_report(user, text):
  scopes = intersect(user.permissions, skill("report_drafting").scopes)      # NN-41
  draft = vidhi.propose_definition(text, catalog=datasets_visible_to(user))   # no numbers in output
  assert draft.contains_no_numeric_literals_outside_filters()
  show_in_builder(draft, badge="AI-drafted definition")
  if user.runs(draft): run = report_engine.run(draft, snapshot=new_snapshot())  # numbers from engine only
  log_ai_action(user, draft, run.id if run else None)
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Key content and actions | Fewer-click design |
|---|---|---|---|---|
| SCR-RPT-01 | Role home dashboard | Home | Role template widgets, next-best action, context bar | Opens on last-used view; mandatory widgets first |
| SCR-RPT-02 | Personal dashboards | Home › My dashboards | Up to 5 personal dashboards; add widget from catalogue | Drag or "Add" menu (no drag-only) |
| SCR-RPT-03 | Dashboard editor and library | Reports › Dashboards | Edit layout, publish as role/department template, library with owners and usage | Copy to role in one action |
| SCR-RPT-04 | Report catalogue | Reports › Catalogue | Search, favourites, tier badges, module filter | Recently run at top |
| SCR-RPT-05 | Run a report | Reports › Run | Parameters, preview, formats, comparison period, currency, language | Remembers last parameters |
| SCR-RPT-06 | Report builder | Reports › Builder | Dataset → fields → filters → groupings → measures → formula columns → visual → preview | Single page; keyboard navigation |
| SCR-RPT-07 | My reports | Reports › My reports | Status, re-run as at, re-run with current data, duplicate, supersede | Bulk archive (IMP-050) |
| SCR-RPT-08 | Scheduled reports | Reports › Scheduled | Cadence, next/last run, failures, recipients | Pause/resume inline |
| SCR-RPT-09 | Report and pack approvals | Reports › Approvals | Queue with data-quality status; approve/return | "Review next" sequence (NN-46) |
| SCR-RPT-10 | Pack studio | Reports › Packs | Compose from template or last pack, sections, owners, progress, narrative with bound values | Copy last pack; auto-refresh period |
| SCR-RPT-11 | Pack viewer and freeze | Reports › Packs › [pack] | Review, approve, freeze (hash), addendum, distribute to P06 meeting | Freeze preflight checklist |
| SCR-RPT-12 | MIS catalogue | Reports › MIS catalogue | Items by category and tier, owners, last produced, compliance | Enable seed items by family |
| SCR-RPT-13 | KPI dictionary | Reports › KPI dictionary | Definitions, formulas, thresholds, owners, "i" text | Linked from every widget's "i" |
| SCR-RPT-14 | Snapshots and re-runs | Reports › Snapshots | Snapshot manifests, re-run as at, output hash comparison | One-click verification |
| SCR-RPT-15 | Subscriptions | Profile › Subscriptions | My subscriptions, delivery channel, digest/immediate | Unsubscribe in one click |
| SCR-RPT-16 | Embedding and feeds | Settings › Reporting › Embedding and feeds | Embed tokens, allowed hosts, OData feeds, service accounts, usage | — |
| SCR-RPT-17 | Group view | Reports › Group | Entity × KPI matrix, aggregates from other cells, FX note | Entity switcher retains filters |
| SCR-RPT-18 | Ask for a report | Reports › Ask Vidhi | Natural-language request → draft definition in builder | Suggestions from catalogue |
| SCR-RPT-19 | Due-diligence snapshot | Reports › Due-diligence | Scope selector, preview, freeze, secure link, access log | Template per audience (lender, investor) |
| SCR-RPT-20 | Inspection MIS file | Reports › Inspection file | Topic → report/document mapping, run, index | Copy last inspection's mapping |
| SCR-RPT-21 | Reporting settings | Settings › Reporting | Tiers, approval paths, branding, retention, budgets | Preview of branded cover |

Empty states explain the next step ("No packs yet — start from the 'Quarterly Board pack – NBFC' template or copy a past pack"). Error states name the gate and the fix ("Board-tier approval blocked: dataset `cmp.instances` is 3 days stale; last successful refresh 22 Oct 18:00 — Refresh now").

---

## 7. Backend design

### 7.1 Modules

`rpt` (owner). Uses `core` (audit ledger, Correction Entries, outbox), `iam` (row-policy attributes), `cfg` (settings, terminology, calendars, NBA rules, widget catalogue), `wf` (tasks, approvals, notifications, digests), `dms` (renditions, WORM archive), `gov` (meetings and board portal delivery), `ral` (metric values and certification — read-only), `ai` (Vidhi skills), `int` (embed tokens, OData feeds, webhooks), `xpt` (export mapping). Packages: `packages/dashboards` (runtime and registration SDK), `packages/docgen` (P07 renderers), `packages/workflow`, `packages/notify`, `packages/calendar` (P04).

### 7.2 Tables (schema `rpt`; all with `tenant_id`, `legal_entity_id` where applicable, `created_*`, `updated_*`, RLS)

| Table | Key columns |
|---|---|
| `rpt.datasets` | dataset_id, owner_module, grain, version, fields jsonb (name, type, unit, data_class, sensitivity, help_key), joins jsonb, row_policy_cel, freshness_sla, retention_class, export_map_ref, status |
| `rpt.kpis` | kpi_id, name, definition, formula_ref (METRIC/DATASET_AGG/SCORE), unit, polarity, owner_role, refresh, thresholds jsonb (source, value, version), help_key, a11y_description |
| `rpt.widget_catalogue` (mirror of `cfg.widget_catalogue`) | widget_code, type, kpi_ids[], dataset_ids[], default_size, mandatory_for_roles[], module |
| `rpt.dashboard_templates` / `rpt.dashboards` | template_id, scope (PLATFORM/TENANT/ROLE/DEPARTMENT), version, layout jsonb, approver / dashboard_id, owner_user_id, based_on_template, layout jsonb, filters jsonb, shared_with |
| `rpt.report_templates` | template_id, level (MASTER/TENANT/ENTITY), parent_id, tier, sections jsonb, mandatory_items[], version, effective_from, status |
| `rpt.report_definitions` | definition_id, template_id?, datasets[], fields jsonb, filters jsonb, measures jsonb, formula_columns jsonb (CEL), visual jsonb, parameters jsonb, created_by, ai_drafted boolean |
| `rpt.snapshots` | snapshot_id, cut_off_at, dataset_versions jsonb, row_counts jsonb, content_hashes jsonb, object_key |
| `rpt.runs` | run_id, definition_id, parameters jsonb, snapshot_id, template_version, renderer_version, state, outputs jsonb (format, object_key, sha256), dq_result jsonb, approvals jsonb, supersedes_run_id, origin (USER/SCHEDULE/MCP/AGENT) |
| `rpt.schedules` | schedule_id, definition_id, rule (CRON/REGULATOR_RULE/MEETING_ANCHOR), lead_time_wd, recipients jsonb, channel, state |
| `rpt.subscriptions` | subscription_id, user_id, object_type, object_id, channel, mode (DIGEST/IMMEDIATE) |
| `rpt.mis_items` | mis_id, title, category, sub_category, tier, frequency, datasets[], data_owner_role, generator_role, approver_role, recipients jsonb, distribution, regulator, citation, kpi_links[], retention_class, confidentiality, formats[], definition_id, last_produced_at |
| `rpt.packs` / `rpt.pack_sections` | pack_id, template_id, context jsonb (entity, period, meeting_id), state, freeze_hash, frozen_at, frozen_by, addendum_of / section_id, pack_id, kind, source_ref, owner_id, due_at, status, bound_values jsonb, narrative, narrative_check |
| `rpt.inspection_maps` | map_id, topic_code, topic_text, report_ids[], document_queries jsonb, verify_status |
| `rpt.embed_grants` / `rpt.feeds` | grant_id, object_ref, allowed_hosts[], viewer_scope, expires_at / feed_id, datasets[], auth_mode, service_account_id, usage counters |
| `rpt.mv_*` | tenant-partitioned materialised aggregates for hot widgets |

### 7.3 APIs (REST, versioned `/v1/rpt/...`; OpenAPI 3.1)

`POST /v1/rpt/datasets` (module registration, platform-internal) · `GET /v1/rpt/kpis` · `GET /v1/rpt/widgets/{code}/data?filters=` · `GET/POST/PATCH /v1/rpt/dashboards` · `POST /v1/rpt/dashboards/{id}:publish-template` · `GET /v1/rpt/catalogue` · `POST /v1/rpt/definitions` · `POST /v1/rpt/runs` · `GET /v1/rpt/runs/{id}` · `POST /v1/rpt/runs/{id}:approve|return|distribute|supersede` · `POST /v1/rpt/runs/{id}:rerun-as-at` · `POST /v1/rpt/schedules` · `POST /v1/rpt/subscriptions` · `GET/POST /v1/rpt/mis-items` · `POST /v1/rpt/packs` · `POST /v1/rpt/packs/{id}/sections` · `POST /v1/rpt/packs/{id}:freeze|distribute|addendum` · `POST /v1/rpt/inspection-files` · `POST /v1/rpt/due-diligence` · `POST /v1/rpt/embed-grants` · `GET /v1/rpt/feeds/{id}/odata/...` · `POST /v1/rpt/ask` (Vidhi draft definition). The v1.0 route `GET /rpt/compliance/score` referenced in P04 §7.3 is served here as `GET /v1/rpt/kpis/cmp.compliance_score/value` (P04 keeps the score computation).

### 7.4 Domain events

Internal (`in.lawdocscomply.rpt.<Name>.v1`): `DatasetRegistered`, `RunCompleted`, `RunFailed`, `RunApproved`, `RunDistributed`, `RunSuperseded`, `RerunMismatchDetected` (Critical), `PackFrozen`, `PackDistributed`, `PackAddendumCreated`, `ScheduleMissed`, `TemplateChangeProposed`, `TemplateChangeApplied`, `EmbedGrantIssued`, `FeedAccessed`. Consumed: P06 `MeetingScheduled` (meeting-anchored schedules), P09 `MetricValueCertified` and `MetricDefinitionChanged` (refresh and "definition changed" banners), every module's dataset-change events for materialised views. No new cross-product events in v1.1; an aggregated `ClientHealthSignal` to the Operations Hub remains owned by P22.

### 7.5 Jobs and Temporal workflows

`snapshot-builder`, `report-run` (async above threshold), `pack-render`, `pack-freeze`, `schedule-dispatcher` (calendar-aware, lead-time drafts), `mv-refresh` (event-driven + nightly), `rerun-verifier` (weekly sample of archived runs re-run as at; mismatches raise Critical incidents), `mis-compliance` (daily: MIS items overdue → W-RPT-04 and tasks).

---

## 8. Integrations (ports and adapters)

| Port | Use in P28 |
|---|---|
| `WORKSPACE_PORT` (P18) | Teams/Google Chat links for subscriptions; SharePoint/Teams embedding of dashboards |
| `STORAGE_PORT` (P19) | Optional delivery of scheduled outputs to the tenant's own storage (e.g., monthly MIS folder in SharePoint) |
| `FX_RATE_PORT` (P25) | Snapshot FX rates for group views |
| `AI_PORT` (P17) | Vidhi report drafting, narration, director question prompts (India route for regulated data, NN-41) |
| OData/REST feeds (P18 gateway) | Power BI, Excel, other BI tools |
| P06 meeting book API | Delivery of frozen packs as item papers |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `rpt.async.row_threshold` | G | 10,000 | 1,000–100,000 | Platform |
| `rpt.async.seconds_threshold` | G | 5 | 2–30 | Platform |
| `rpt.tier.management.approval` | T | maker → domain owner | within SoD | `ten_admin` |
| `rpt.tier.board.approval` | T | maker → KMP → CS freeze | may add steps; cannot remove CS freeze | `ten_admin` with CS |
| `rpt.tier.regulator.approval` | T | maker → CCO → MD/CEO | may add steps | `ten_admin` with CCO |
| `rpt.tier.board.email_attachments` | L | OFF | — | — |
| `rpt.approval_sla_wd` | T | Mgmt 2 / Board 3 / Regulator 1 | 1–10 | `ten_admin` |
| `rpt.schedule.lead_time_wd` | T | 10 | 1–30 | Report owner |
| `rpt.subscriptions.default_mode` | T | DIGEST | DIGEST/IMMEDIATE | User |
| `rpt.dashboards.personal_max` | T | 5 | 1–10 | `ten_admin` |
| `rpt.retention.operational_years` | T | 2 | ≥ 1 | `ten_admin` |
| `rpt.retention.management_years` | T | 8 | ≥ 8 | `ten_admin` |
| `rpt.pack.render_timeout_s` | G | 60 | 30–600 | Platform |
| `rpt.narrative.bound_check` | L | ON | — | — |
| `rpt.ai.autonomy_ceiling` | G | L2 | L0–L2 | `ten_admin` |
| `rpt.embed.enabled` | T | OFF | ON/OFF | `ten_admin` |
| `rpt.feeds.enabled` | T | OFF | ON/OFF | `ten_admin` with CISO |
| `rpt.benchmarking.enabled` | G | OFF | ON/OFF (methodology approval required) | Platform |
| `rpt.number_format` | T | Indian (lakh/crore) | Indian / International | User |
| `rpt.due_diligence.link_expiry_days` | T | 14 | 1–90 | `ten_admin` |
| `cmp.score.method` | T | COMPLIANCE_SCORE | COMPLIANCE_SCORE / HEALTH_INDEX_5C | CCO |

---

## 10. Security, privacy and audit

- Row policies evaluated server-side for every widget, report, feed and embed; cross-tenant tests (NN-01) include feeds and embeds.
- Sealed classes excluded from datasets except owner-published aggregates with k ≥ 5 (NN-13, X-36).
- Board and Regulator tiers: no e-mail attachments, per-recipient watermark, access log, link expiry; UPSI handling and SDD entries through P06 for listed entities.
- Every run, approval, freeze, distribution, embed grant and feed access is written to the audit ledger in the same transaction (NN-45).
- Archived outputs WORM-stored with hashes (NN-09); exports carry the BSA 2023 s.63 certificate through P19.
- Supervisor access only through D-12 grants (NN-18); due-diligence links are time-limited and revocable.
- Feeds use OAuth per user or scoped service accounts; tokens rotate; feed definitions reviewed quarterly by the CISO.
- Vidhi-originated definitions and narratives are labelled and logged (NN-14, NN-15).

---

## 11. AI touchpoints and guardrails

| Touchpoint | What Vidhi does | Guardrails |
|---|---|---|
| Ask for a report | Drafts a report definition from natural language | No numbers in Vidhi text; datasets limited to the user's permissions; user runs it (NN-41, NN-50) |
| Narrative commentary | Drafts variance and trend commentary | Bound placeholders only; unbound numerals fail the check (NN-37); human approval before Management/Board/Regulator tiers (NN-04) |
| Director question prompts | Drafts cited questions for Board packs | CS releases; members-only; labelled AI (NN-14) |
| Pack assembly assistant | Suggests missing mandatory sections and owners | Suggestion only; composer decides |
| Alt text | Generates alt text from bound values | Deterministic template fallback |

Autonomy ceiling for reporting skills: L2 (draft records); P28 never grants L3 or above. Kill switches (NN-51) disable all reporting skills within 60 seconds while leaving manual reporting fully functional.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p28/*.feature`)

```gherkin
Feature: One source of numbers
  Scenario: Widget bound to an ungoverned query fails CI
    Given a widget definition that queries table "cmp.instances" directly
    When CI runs the dashboard contract tests
    Then the build fails with "Widget must reference KPI or dataset ids"

  Scenario: Regulatory metric shows certification state
    Given CRAR for Q2 is COMPUTED but not CERTIFIED in P09
    When the CFO opens the CFO dashboard
    Then the CRAR tile shows "Indicative — awaiting certification"

Feature: Reproducible reports (IMP-072)
  Scenario: Re-run as at
    Given approved run RUN-2026-Q2-017 with snapshot hash S1 and template version 3
    When "Re-run as at" is executed
    Then the output hash equals the original output hash

  Scenario: Mismatch raises an incident
    Given an archived run whose re-run output differs
    When the weekly rerun-verifier samples it
    Then a Critical incident "RerunMismatchDetected" is raised and the original remains authoritative

Feature: No-code builder (IMP-074)
  Scenario: CCO builds and schedules a report
    Given a CCO with access to dataset "cmp.instances"
    When she selects fields, filters "risk = High and overdue", groups by department and regulator, adds formula column "overdue_days * 1" and a bar chart
    And saves it as a tenant template and schedules it monthly to the MD
    Then the schedule exists with lead time 10 working days and recipients "MD"

  Scenario: Formula cannot redefine a regulatory metric
    When a user creates a formula column named "R1" that divides two fields
    Then the save is rejected with "LDC-RPT-012: regulatory metrics come from P09"

Feature: Pack freeze and addendum
  Scenario: Frozen pack is immutable
    Given a Board pack in FROZEN state with hash H1
    When a section owner edits a narrative
    Then the edit is rejected and an "Create addendum" action is offered

  Scenario: Unbound figure blocks freeze (NN-37)
    Given a narrative block containing "GNPA fell to 2.1%" where 2.1 is not bound
    When the composer requests freeze
    Then the preflight fails with "Unbound figure in section 4: 2.1%"

  Scenario: Board pack delivered to P06 meeting
    Given a frozen Board-tier pack for meeting M-2026-11
    When the CS distributes it
    Then it appears as item papers in the P06 meeting book and no e-mail attachment is sent

Feature: Tiers and SoD
  Scenario: Author cannot approve own report (NN-05)
    Given report run R authored by user A
    When user A tries to approve R
    Then the action fails with "LDC-CORE-005"

Feature: Sealed data never reachable
  Scenario: POSH fields absent from builder
    Given a tenant HR admin opens the report builder
    Then no dataset field with data class "SEALED" is listed

Feature: Group views across regional cells (NN-24 amended)
  Scenario: Aggregates only from GCC cell
    Given a group with an entity homed in the GCC cell
    When the group CFO runs the group compliance report
    Then the GCC entity appears as aggregate rows labelled "aggregate from GCC cell"

Feature: Performance (IMP-141)
  Scenario: Large report runs asynchronously
    Given a report estimated at 50,000 rows
    When the user runs it
    Then it runs asynchronously and completes within 2 minutes with a notification

Feature: Ask for a report (NN-41, NN-50)
  Scenario: Vidhi drafts but does not compute
    When a user asks "overdue High compliances by department for Q2"
    Then a draft definition opens in the builder labelled "AI-drafted definition"
    And Vidhi's response contains no figures
```

NN tests touched: NN-01, NN-04, NN-05, NN-09, NN-10, NN-13, NN-14, NN-21, NN-22, NN-24, NN-37, NN-41, NN-45, NN-46, NN-50, NN-51, NN-52.

---

## 13. Deliverables and exit gate

- `rpt` module, migrations (expand–contract, NN-11), OpenAPI/AsyncAPI specs, `packages/dashboards` with registration SDK and contract tests.
- Seeded KPI dictionary, widget catalogue (Appendix C §C.6.1 + v1.1 additions), 25+ role templates, seed report catalogue (FR-P28-16), seed MIS catalogue (≥ 60 items), pack templates (quarterly Board pack per family, RMC, Audit Committee, ALCO, monthly management MIS), inspection MIS mapping (marked [VERIFY]).
- Renderers for DOCX, PDF/UA, PPTX, XLSX with accessibility checks; WORM archive of runs and packs; export mapping registered (NN-10).
- Screens SCR-RPT-01 to SCR-RPT-21 with empty and error states, "i" help keys and keyboard operation.
- Documentation: `docs/phases/P28-plan.md` (five inventories), user guides and tutorial outlines (P23): build a report, schedule MIS, compose and freeze a Board pack.
- **Exit gate:** all §12 scenarios and NN tests green; core track live for Wave 1 (role dashboards and catalogue reports used by P04/P06/P08); pilot NBFC-ML produces its quarterly Board pack inside LDC and the inspection MIS file in one run; performance budgets met on a 50,000-instance tenant; WCAG 2.2 AA audit of SCR-RPT-01, -06, -10 and a rendered PDF/UA pack passed.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P28-01 | RBI inspection data-request topic list for the "Management and Systems" file | Current request formats not fetched | Platform content (RBI) | Mapping template ships editable; topics marked [VERIFY] |
| OI-P28-02 | Quarterly compliance report to the Board — mandatory items per NBFC Compliance Function Directions 2026 (RBI/DoS/2026-27/460) | Paragraphs not re-fetched | Platform content (RBI) | Template items labelled [VERIFY]; tenants may add items |
| OI-P28-03 | Benchmarking methodology (cohort size, noise) and consent text | Requires approval and counsel review | Product + counsel | `rpt.benchmarking.enabled` OFF |
| OI-P28-04 | OData feed licensing/performance for large tenants | Load testing needed | Platform engineering | Feeds OFF by default |
| OI-P28-05 | PPTX native chart rendering library choice | Licence ADR | CTO | High-resolution images with alt text |
| OI-P28-06 | Ownership of SCR-RPT-01/02 moves from P04 (X-26) to P28 | Master X-26 update needed | Pack lead | P28 provides runtime; P04 hosts home until updated |
| OI-P28-07 | Seed MIS titles derived from the owner's baseline tables | Normalised titles; owner confirmation | Owner / CS | Titles editable by tenant |

---

## 15. Sources (accessed 25 October 2026)

1. Owner's LawDocs Comply Architecture Part 1 §30 (MIS framework, tiers, categories, metadata schema, seed tables) and Part 3 "Reports" chapter (report lifecycle, tiers, templates, scheduler) — internal baseline.
2. Appendix Z — Customer Feedback, Reverse Engineering and Improvement Backlog (IMP-046, IMP-050, IMP-057, IMP-071, IMP-072, IMP-074, IMP-075, IMP-079, IMP-081, IMP-088, IMP-109, IMP-112, IMP-140, IMP-141).
3. Appendix AC and `_contrib/v11/G5_gaps_by_file.md` §C; `_contrib/v11/G5_errors_found.md` E-02, E-06, E-19.
4. Appendix C §C.6 (widget catalogue, layouts, personalisation, next-best action) and §C.8 (design tokens).
5. Appendix H §H.0A and §H.6.3 *(v1.1)* (metric ownership; aggregation and currency rules).
6. W3C, Web Content Accessibility Guidelines (WCAG) 2.2 — https://www.w3.org/TR/WCAG22/ ; ISO 14289-1 (PDF/UA).
7. OASIS, OData Version 4.01 — https://www.oasis-open.org/standards#odatav4.01
8. RBI (Non-Banking Financial Companies – Compliance Function) Directions, 2026, RBI/DoS/2026-27/460 (catalogue S.No 15) [VERIFY paragraphs].


---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**Added in v1.1:** NN-37, NN-47; X-43, X-46, X-49.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
