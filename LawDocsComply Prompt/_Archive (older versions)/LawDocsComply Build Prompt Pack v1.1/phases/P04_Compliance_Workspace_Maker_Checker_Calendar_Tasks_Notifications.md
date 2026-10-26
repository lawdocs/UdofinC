# Phase P04 — Compliance Workspace: Maker-Checker, Calendar, Tasks and Notifications

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
> **Requirements added in v1.1:** R-103 (placeholder items for pre-seeded RBI directions), owner's v1.1 instruction to improve logic, speed and customisation (Appendix Z backlog IMP-015–IMP-058, IMP-070–IMP-075), G5 gaps (compliance testing, licences and alert fatigue).
>
> **Estimated effort:** 11 two-week sprints for a squad of 9 *(v1.1: +3 sprints for automated checkpoints, compliance testing, request lists, notification budget and grid bulk edit)* (scheduling engine 2; maker-checker, evidence and automated checks 3; calendar and sync 2; notifications and inbox 2; testing and issues 2).
>
> **v1.1 changes (25 October 2026)**
> - **Three dates per instance (NN-48):** act date, evidence date, approval date; timeliness judged on the act date (FR-P04-25 rewritten; IMP-031).
> - **Placeholder instances** for adopted RBI directions whose sheets are not yet published, converted automatically on publication (D-39; FR-P04-05).
> - **Grouped work for multi-licence entities** and **control executions** from P03's common control layer: one submission, many linked instances (FR-P04-06; IMP-013, IMP-014).
> - **Automated checkpoints** with versioned machine tests, `NO_DATA`/`INVALID` states and human attestation where required (§4P; IMP-015–018).
> - **Event trigger catalogue** expanded into event bundles that spawn every linked checkpoint across instruments and modules (FR-P04-33; IMP-028).
> - Evidence rules, evidence reuse with validity windows, request lists (PBC-style, incl. external parties), e-mail-in classification, AI sufficiency note (IMP-032–036).
> - **Compliance testing programme** (second line): cycles, sampling, test steps, remediation SLAs, retest (§4H; G5 gap).
> - Issues: AI-drafted action plans, remediation library, repeat-issue detection, validated closure (IMP-055–058).
> - **Notification budget**, batching, subscriptions/mute, risk-adaptive ladders, channel matrix, holiday-aware quiet hours and alert-health metric (§4N; IMP-040–046; G5 E-19).
> - **In-grid bulk edit with 24-hour undo** (NN-49), shared saved views, My Day, offline mobile maker flow, status explainers (IMP-038, IMP-039, IMP-047–054).
> - Score terminology fixed (Compliance Score vs Health Check Score vs Compliance Health Index; G5 E-06); report builder and board-pack studio moved to P28, which owns `rpt` (D-47; G5 E-02) — P04 registers its report definitions there.
> - Multi-timezone, per-jurisdiction fiscal years and holiday calendars for foreign entities (P25); calendar producers from licences (P26), contracts and litigation (P26) and ESG milestones (P27).
> - Compliance Coordinator agent (D-34) under bounded autonomy (NN-50); AI never sets a status (NN-47); MCP tools for "my due items" (NN-52).
> - Errors fixed: Work Inbox screen ID is SCR-WF-00 (Appendix C §C.9); register-export scenario no longer writes beyond column AD (NN-35); CompID example aligned with Appendix E.

---

## 1. Objective and business outcome

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
| Fair timeliness *(v1.1)* | An instance performed on time but approved after the due date is reported `complied`, not `complied_late`, under the default rule (NN-48) |
| Evidence that collects itself *(v1.1)* | At least 10 NBFC checkpoints run as automated checks on connected data (e.g., grievance officer details on the website, KFS published, monthly DLG disclosure) and refresh without maker effort; a disconnected source shows `NO_DATA`, never "failed" |
| Event-based items not missed *(v1.1)* | Logging "director appointed" creates in one step the DIR-12 filing, MBP-1 disclosure index entry, fit-and-proper declaration and RBI intimation instances with due dates (IMP-028) |
| Alert fatigue controlled *(v1.1)* | Default budget of 10 immediate notifications per user per day enforced; overflow folded into the digest; Critical never folded; 20 assignments produce one e-mail (IMP-040, IMP-041) |
| Bulk changes safe *(v1.1)* | 200 rows of owners, internal dates and tags edited in-grid in ≤ 2 minutes, with preview and a 24-hour undo (NN-49) |

---

## 2. Scope (in / out)

**In scope:** compliance-instance generation; due-date and frequency engine with business-day conventions and holiday calendars; event-based triggers; maker/checker/auditor workflow mirroring template columns T–AD; evidence capture and reuse; rework, reallocation, delegation and backup owners; not-applicable claims, waivers, extensions; escalation ladders; exception register; attestations and compliance certificates (department → CCO → MD/CEO → Board); compliance score; reports and scheduled reports; Excel and PDF exports; unified calendar with external sync; task management (hierarchical assignment, sub-tasks, dependencies, checklists, recurring and scheduled tasks, tasks to Vidhi AI); Work Inbox; Notifications service with channels, digests, quiet hours and mandatory floors; WORKSPACE import application. *(v1.1)* Placeholder instances; grouped multi-licence work items and control executions; automated checkpoints; event bundles; evidence rules, reuse and request lists; compliance testing programme; issue action plans and remediation library; notification budget and alert-health; in-grid bulk edit with undo; Compliance Coordinator agent; foreign-entity timezones, fiscal years and calendars.

**Out of scope:** regulatory Updates and change impact (P05); meeting/committee scheduling (P06 — uses this calendar); policy reviews (P07 — uses this scheduler); return preparation (P11 — publishes due dates here); Vidhi's agent runtime (P17 — receives tasks from here); HR leave data (P13 — consumed for delegation); billing (P20). *(v1.1)* Report builder, MIS catalogue and board-pack studio (P28 owns `rpt`; P04 contributes report definitions); licences and registrations register, contracts and litigation (P26 — P04 only schedules their dated obligations); ESG/BRSR (P27).

---

## 3. Personas and permissions touched

| Role | Responsibilities in P04 |
|---|---|
| `ten_maker` (incl. `dlv_rm` / `dlv_professional` acting as maker for retainer clients, R-072) | Performs the control activity, uploads evidence, sets maker status (W), date of compliance (I), comments (X) |
| `ten_checker` | Reviews evidence, sets filing/compliance date (Z), decides Approve/Reject/Reallocate (AA), comments (AB); cannot check own work |
| `ten_dept_head` | Sees all department instances, reassigns, approves extensions/N-A claims within delegated limits, signs department certificate |
| `ten_cco` | Owns the compliance programme: routing rules, escalations, exceptions, waivers above limits, CCO certificate, Board report |
| `ten_kmp` (MD/CEO, CFO, CRO, CS, CISO, DPO …) | Personal dashboard of items they own or attest; MD/CEO certificate |
| `ten_board_member`, `ten_committee_member` | Read Board/Committee compliance reports and drill-down (read-only) |
| `ten_internal_auditor` | Samples closed instances, records auditor comments (AC/AD), raises observations |
| `ten_external_auditor`, `ten_supervisor_view` | Read-only within time-boxed grant (D-12) |
| `ten_admin` | Calendar connections policy, notification floors, register exports, workspace import |
| `svc_vidhi` | Receives tasks, drafts evidence summaries, prepares reports — draft-only (NN-14) |
| Compliance Coordinator agent *(v1.1, D-34)* | Role agent under `svc_vidhi`, sponsored by the CCO: drafts reminders and evidence requests, proposes reassignments and events, prepares weekly status — autonomy L1–L2 per tenant setting; never sets a status or approves (NN-47, NN-50) |
| External requestee *(v1.1)* | Person outside the tenant (statutory auditor, vendor, group company, consultant) answering a request list through a one-time secure link: upload only, no account, link expires (FR-P04-26) |

---

## 4. Functional requirements

### 4A. From checkpoints to compliance instances

**FR-P04-01 Applicability scope.** For each adopted instrument (P03 §4F) and each tenant legal entity, the engine evaluates each effective checkpoint (base ⊕ overlays) through the applicability interface (P03 §4H). For APPLICABLE results a **compliance obligation assignment** (`cmp.obligation_assignments`) is created per legal entity and, where the checkpoint's `scope_level` requires it, per **establishment/branch/location** (labour registers per establishment, shops-and-establishments per state, branch-level KYC checks), per **product** (digital lending products), or per **committee** (meeting-related checkpoints). NEEDS_INPUT results create a one-time "Answer to confirm applicability" task for the CCO.

**FR-P04-02 Instances.** Each assignment generates **compliance instances** (`cmp.instances`) according to its frequency and due rule, for a rolling horizon (`cmp.schedule.horizon_months`, default 15 — current FY plus the next quarter, so the January full-year calendar view that competitors offer is available). Each instance pins `checkpoint_version_no` and `overlay_version_no` at creation (NN-03/NN-07); a later content release regenerates only **future, not-started** instances and records the change.

**FR-P04-03 Instance identity.** `instance_ref = <comp_id>/<legal-entity code>/<scope code>/<period code>` (e.g., `RBI-NBFC.GOV.0012/LE01/HO/FY2026-27-Q3`; CompID format per Appendix E §E.8), shown to users and used in exports (column E carries CompID; the period travels in the `_LDC_System` sheet of the register export, see §4K).

**FR-P04-05 Placeholder instances (D-39; Appendix AB §AB.6.2) *(v1.1)*.** When a tenant adopts a catalogued instrument whose coverage state is `PLANNED` or `IN_PREPARATION` (P03 FR-P03-56), the engine creates one **placeholder instance** per legal entity: checkpoint text "Maintain compliance with <direction title> — detailed checkpoints in preparation (expected <month>)", frequency CONTINUOUS with a quarterly attestation, owner `ten_cco`, risk inherited from the catalogue priority, evidence optional. Placeholders appear in the register, the CCO dashboard and the Board report with a "Detailed checkpoints pending" badge, so no adopted direction is invisible. On `CoverageStateChanged → AVAILABLE`, `PlaceholderConversionWorkflow` creates the detailed assignments and instances from the publication date, closes the placeholder as `withdrawn` with reason "Replaced by detailed checkpoints" (its attestations and comments stay in history), and moves any tenant checkpoints the client authored for the direction according to the choice made in P03 (keep / replace / keep as overlay).

**FR-P04-06 Grouped work for equivalent obligations and controls (IMP-013, IMP-014) *(v1.1)*.** Two mechanisms reduce duplicate effort without merging legal accountability: (a) **Equivalence groups** — instances whose checkpoints are linked as SAME_OBLIGATION or STRICTER_OF (P03 FR-P03-16) and fall in the same period for the same legal entity appear as **one work item** in My Day and the Work Inbox, listing every instrument it satisfies; the maker submits once, evidence links to each instance, and the due date shown is the earliest (or the stricter rule's); the checker reviews the group in one screen but records a decision per instance where the instances belong to different authorities or `requires_independent_review` is set. (b) **Control executions** — for a common control (P03 FR-P03-15) the engine creates one `cmp.control_executions` row per period; completing it (manually or via an automated test, §4P) links its evidence to every mapped instance and moves them to `submitted_for_review` together. Reports count each instance separately (regulator-wise accuracy); executive dashboards may collapse groups (`cmp.dashboard.collapse_equivalents`).

### 4B. Frequency and period engine (owner's "Due date & Frequency" lists)

**FR-P04-10 Frequencies.** The canonical frequency codes and their default period definitions:

| Rough-list value | Code | Default period | Notes |
|---|---|---|---|
| Annually | ANNUAL | Indian FY 1-Apr → 31-Mar | Per-checkpoint override to calendar year (e.g., some IFSC or global obligations) or to the entity's own FY |
| Half Yearly | HALF_YEARLY | Apr–Sep, Oct–Mar | Calendar-half option |
| Quarterly | QUARTERLY | Apr–Jun, Jul–Sep, Oct–Dec, Jan–Mar | |
| Monthly | MONTHLY | Calendar month | |
| Fortnightly | FORTNIGHTLY | Calendar half-month (1–15, 16–end) | Option ROLLING_14 anchored to a reference date; reporting-fortnight definitions for RBI returns come from P11 return definitions, not from here |
| Weekly | WEEKLY | Monday–Sunday (setting for week start) | |
| Daily | DAILY | Business day per tenant calendar | Treasury limits, cash positions |
| Event Based | EVENT | No period; instance created when the trigger event is recorded (§4D) | |
| Immediately | IMMEDIATE | Event-based with due = event time + `cmp.immediate.default_hours` (default 24 h) unless the due rule says otherwise | Urgent styling and priority escalation |
| Ongoing/Continuous | CONTINUOUS | No due date for performance; an **attestation instance** recurs at `cmp.ongoing.attestation_frequency` (default QUARTERLY) asking the owner to confirm continued compliance with evidence where specified | |
| One-time | ONE_TIME | Single instance on adoption (or on effective date); once approved, remains satisfied; re-opens only if the checkpoint changes materially or a linked event occurs | |

Families may add frequencies (EVERY_2Y, EVERY_3Y, EVERY_5Y in v1.0); Appendix E §E.13.1 lists them and the engine supports `RRULE` (RFC 5545) for any custom pattern.

**FR-P04-11 Due rule.** Each checkpoint version carries a structured `due_rule` (P03 FR-P03-05):

```json
{ "anchor": "PERIOD_END | PERIOD_START | EVENT | FIXED_DATE | FY_END | FY_START | AGM_DATE | BOARD_MEETING | FILING_OF:<checkpoint> | CUSTOM_RRULE",
  "offset": { "value": 21, "unit": "CALENDAR_DAYS | BUSINESS_DAYS | MONTHS" },
  "fixed": { "month": 9, "day": 30 },
  "business_day_convention": "NONE | PRECEDING | FOLLOWING | MODIFIED_FOLLOWING",
  "calendar": "IN-RBI-<state> | IN-NSE | IN-IFSC | IN-CENTRAL | TENANT:<code>",
  "window_opens": { "value": 30, "unit": "CALENDAR_DAYS" },
  "internal_buffer_days": 5 }
```
Examples: "within 7 days of appointment" → EVENT + 7 calendar days; "by 30 September every year" → FIXED_DATE 30-Sep; "within 21 days from the end of the quarter" → PERIOD_END + 21 days; "before the AGM" → AGM_DATE − 0 with dependency on the AGM date captured in P06. The **statutory due date** is computed by rule; an **internal due date** (statutory − buffer) drives reminders and escalation; both are shown. Business-day conventions default to NONE (regulators often do not extend for holidays) and must be set deliberately per checkpoint by the content team; P11 return definitions override with the portal's rule where RBI/SEBI publish one.

**FR-P04-12 Holiday calendars.** Calendars from P03 (§4I) plus tenant calendars (office holidays per location). Each instance records the calendar and convention used, so a reviewer can see why a date moved.

**FR-P04-13 Regulatory date changes.** When a regulator extends a due date (e.g., an MCA or GST extension circular), P05 publishes an **extension notice** that creates an effective-dated override (`cmp.due_overrides`) for the affected checkpoints and periods across tenants, recalculating open instances and notifying owners. The original statutory date stays on the record.

**FR-P04-14 Timezones, fiscal years and foreign calendars (P25) *(v1.1)*.** Each legal entity has a jurisdiction, timezone and fiscal-year convention (India 1 Apr–31 Mar; UK and Singapore by company year-end; UAE and US commonly calendar year — always from the entity profile, never assumed). Statutory due dates are computed and stored in the **entity's** timezone (`statutory_due_at` with zone), displayed in the viewer's timezone with the entity zone shown on hover; reminders fire in the assignee's local working hours. Period codes use the entity's fiscal year (`FY2026-27` for India, `FY2026` for calendar-year entities). Holiday calendars are chosen per entity and jurisdiction (P03 FR-P03-81); penalty and fee amounts carry currency.

### 4C. Instance lifecycle (mirrors template columns T–AD)

**FR-P04-20 Column mapping.** The owner's user columns map one-to-one to instance fields, so the Excel register and the screen always agree:

| Col | Header | Instance field | Set by |
|---|---|---|---|
| I | Date of Compliance | `act_date` (*v1.1*, NN-48: the date the obligation was actually performed, filed or complied with; formerly `date_of_compliance`) | Maker (defaults to the date read from the evidence where available, else today; editable within rules) |
| J | Status | `overall_status` (system) | System (derived from state, §5.1) |
| T | Maker User/Email ID | `maker_user_id` (+ email) | Routing / reassignment |
| U | Upload Document or Evidence | `evidence_items[]` (link to DMS) | Maker |
| W | Status Update by Maker User | `maker_status` | Maker: COMPLIED, PARTIALLY_COMPLIED, NOT_COMPLIED, NOT_APPLICABLE_CLAIMED, IN_PROGRESS, COMPLIED_LATE |
| X | Comments, if any, by Maker User | `maker_comments` | Maker |
| Y | Checker User/Email ID | `checker_user_id` | Routing |
| Z | Filing/Compliance Date | `confirmed_act_date` (*v1.1*) | Checker confirms or corrects the act date from the evidence (e.g., portal acknowledgement date); if blank, `act_date` stands |
| AA | Review- Approve, Reject, Reallocate | `checker_decision` | Checker: APPROVE, REJECT, REALLOCATE |
| AB | Comments, if any, by Checker User | `checker_comments` | Checker |
| AC | Assigned Auditor/Email ID | `auditor_user_id` | Audit sampling (§4H) or CCO |
| AD | Comments, if any, by Auditor | `auditor_comments` + `auditor_conclusion` | Auditor |

**FR-P04-21 Routing.** Maker and checker resolve per P03 FR-P03-63 (instance → function → department → legal entity → CCO), with **checker rules**: department head by default; for High-risk instances optionally the CCO or a second-level checker (`cmp.review.high_risk_two_level`). A rule engine (P02) allows routing by legal entity, location, product, amount or tag (e.g., all `board_reporting` items to the CS as checker). For retainer clients (R-072), the tenant can set "LawDocs as maker" for a department, function or instrument: the assigned `dlv_rm`/`dlv_professional` is maker and a client employee is checker; multiple makers per instance are supported (primary + contributors), and both the client admin and the delivery lead can propose maker users (P22); a delivery-lead proposal takes effect only after the client admin approves the delivery grant, and delivery staff never hold checker, approver or admin roles (NN-43) *(v1.1 clarification)*.

**FR-P04-22 Evidence.** Maker attaches evidence by drag-and-drop, from the DMS (P07), from a connected drive (OneDrive/SharePoint/Google Drive via P18), from an email forward address (`evidence+<instance-token>@in.lawdocscomply.com`, sender must be a tenant user; attachments scanned), or from an ecosystem event (e.g., Finbyx `ReturnStatusUpdated` with acknowledgement → auto-attached as evidence with source label). Each evidence item records hash, uploader, time, source, and the expected-evidence requirement it satisfies (P03 FR-P03-06). One document can satisfy several instances (linked, not copied). Vidhi may check sufficiency (§11) — advisory only.

**FR-P04-23 Submission rules.** Submit requires: maker status set; date of compliance not in the future (unless status IN_PROGRESS); for COMPLIED/COMPLIED_LATE at least one evidence item per mandatory requirement (configurable floor per risk: `cmp.evidence.required_for` default HIGH and MEDIUM); for NOT_APPLICABLE_CLAIMED a reason and supporting note; for NOT_COMPLIED or PARTIALLY_COMPLIED a remediation proposal (date, action, owner) that creates an exception on approval (§4F).

**FR-P04-24 Review.** The checker sees the checkpoint text (effective), clause and source link, control activity, expected evidence vs uploaded evidence (tick list), maker comments, history, and Vidhi's sufficiency note. Decisions: **Approve** (closes; status per maker status and timeliness), **Reject** (returns to maker with mandatory comment; rework counter increments; repeated rejections ≥ `cmp.review.rework_alert_count` notify the department head), **Reallocate** (to another maker or checker with reason; the original maker is notified). There is no bulk approval of compliance instances (NN-46): the checker moves through the queue with **Review next**, which opens the next item with its evidence preloaded. The only bulk exception is for checkpoints flagged `bulk_approvable` in content (Low risk and compliance type Suggestive or Internal Compliance); it opens a confirmation listing every item and records each approval individually.

**FR-P04-25 Timeliness — three dates (NN-48; IMP-031) *(v1.1, rewritten)*.** Every instance records three dates: **act date** (`confirmed_act_date`, else `act_date` — when the obligation was actually performed, filed or complied with), **evidence date** (`evidence_date` — the date on the proving document, extracted by the DMS or entered by the maker; for several documents the latest relevant one) and **approval date** (`approved_at` — system timestamp of the checker's approval). Default rule `cmp.timeliness.rule = ACT_DATE`: `closed_on_time` when the act date ≤ statutory due date **and** the evidence is accepted; approval after the due date does **not** make the item late (it raises a separate "review lag" metric for the checker). The tenant may choose the stricter `ACT_AND_APPROVAL` rule (G tier, maker-checker change, applies prospectively). Guards: act date cannot be after the evidence date for filing-type evidence (an acknowledgement dated 12 Jan cannot prove an act on 14 Jan) and cannot be in the future; a gap of more than `cmp.timeliness.max_evidence_gap_days` (default 30) between act date and evidence date requires a maker explanation. Late closure requires the maker to state the reason and whether any late fee or penalty was paid (feeds the penalty ledger and the P20 savings model; paid amounts recorded with challan evidence).

**FR-P04-26 Request lists (PBC-style; IMP-034) *(v1.1)*.** A maker, checker or auditor can raise a **request list** against one or many instances: items (document requested, description, due date, owner — internal user, group-company contact or external requestee), automatic reminders on the P04 ladder, and an upload portal. External requestees receive a one-time secure link (expiry `cmp.requests.external_link_days`, default 7; OTP to e-mail; upload-only; malware scan; no access to any other data); uploads land on the instance as evidence in `PENDING_ACCEPTANCE` until the requester accepts. Request lists are reusable templates (e.g., "Statutory auditor quarterly PBC — NBFC").

**FR-P04-27 Evidence rules and reuse (IMP-032, IMP-033) *(v1.1)*.** Each evidence requirement (P03 FR-P03-06) may carry deterministic **evidence rules** evaluated before the AI note and before submission: document class, issuer (e.g., "RBI CIMS acknowledgement"), date window relative to the period, entity name match, signature present, period match, minimum pages, file type. Failures are shown to the maker as fixable messages ("Document dated 02-Jan-2026 is outside the period Apr–Jun 2026"); the maker can override with a reason only where `cmp.evidence.rules_overridable` permits (never for High risk). **Reuse:** evidence with a validity window (e.g., a Board-approved policy valid until its next review date, a licence valid until expiry) can be linked to subsequent periods' instances in one click; the system blocks reuse beyond validity and records the source instance (`reused_from_instance_id`).

**FR-P04-28 E-mail-in per instance (IMP-036) *(v1.1)*.** Each instance has a unique address (`evidence+<token>@in.lawdocscomply.com`); a general address (`evidence@<tenant-slug>.in.lawdocscomply.com`) accepts forwarded mails and classifies attachments to instances by subject, CompID mention, sender's open items and document content (target ≥ 90 % correct; unclassified items wait in an "Evidence inbox" for one-click filing).

### 4D. Event-based compliance

**FR-P04-30 Event catalogue.** `cmp.event_types` (seeded, tenant-extendable): DIRECTOR_APPOINTED, DIRECTOR_RESIGNED, KMP_APPOINTED, KMP_CHANGED, AUDITOR_APPOINTED, AUDITOR_RESIGNED, BOARD_MEETING_HELD, GENERAL_MEETING_HELD, CHANGE_IN_REGISTERED_OFFICE, CHANGE_IN_SHAREHOLDING (with thresholds), CHANGE_IN_CONTROL, ALLOTMENT_OF_SECURITIES, CHARGE_CREATED/MODIFIED/SATISFIED, BRANCH_OPENED/CLOSED, NEW_PRODUCT_LAUNCHED, OUTSOURCING_ARRANGEMENT_ENTERED, MATERIAL_OUTSOURCING_TERMINATED, CYBER_INCIDENT_DETECTED, FRAUD_DETECTED, PERSONAL_DATA_BREACH, LARGE_EXPOSURE_BREACH, RBI_INSPECTION_REPORT_RECEIVED, SHOW_CAUSE_NOTICE_RECEIVED, PENALTY_IMPOSED, EMPLOYEE_HEADCOUNT_THRESHOLD_CROSSED, POSH_COMPLAINT_RECEIVED (sealed; NN-13), GRIEVANCE_ESCALATED, LISTING_OF_SECURITIES, PRICE_SENSITIVE_INFORMATION, RELATED_PARTY_TRANSACTION_PROPOSED, DIGITAL_LENDING_APP_ONBOARDED, LSP_ENGAGED.

**FR-P04-31 Triggers.** Events can be recorded (a) manually by authorised users (setting `cmp.events.<type>.who_can_trigger`, with optional approval before instances are created — the Lawrbit-style restriction), (b) automatically from LDC modules (P06 governance: director appointed; P13 HRMS: KMP changed; P12: incident logged; P14: grievance escalated), (c) from ecosystem events (Finbyx `LitigationCaseOpened`, `OrderRecorded`, `DLGDisclosurePublished`; Udofin LSP onboarding), or (d) proposed by Vidhi from a document it read (e.g., an RBI letter) — proposal requires a human confirmation. Each event carries `event_date`, attributes and evidence; all checkpoints whose due rule anchors to that event type (and whose applicability passes) generate instances with due dates computed from `event_date`.

**FR-P04-32 Chained obligations.** Due rules may anchor to another checkpoint's completion (`FILING_OF:<comp_id>`), e.g., file the intimation within 7 days after the Board approves; dependencies (pre/post) block or warn as configured.

**FR-P04-33 Event bundles and the "Log event" button (IMP-028) *(v1.1)*.** Every event type has a **bundle** — the list of checkpoints across all adopted instruments and modules anchored to it — so one recorded event spawns every linked obligation at once. Example bundle DIRECTOR_APPOINTED (company that is an NBFC): DIR-12 filing (MCA, 30 days), MBP-1 disclosure index entry and DIR-8 (P06), fit-and-proper declaration and Board/NRC assessment (RBI governance directions), RBI intimation of change in directors where applicable, updating the register of directors and KMP, LODR Reg 30 disclosure if listed, website update where required. A global **Log event** button (top bar and command palette) offers a form per event type with smart attribute capture (e.g., "Is the director independent?") that drives which bundle items apply. Bundles are content (platform-maintained, tenant-extendable); the bundle preview shows every instance to be created before confirmation. Sources wired: P06 (appointments, resignations, meetings, allotments, charges), P13 (KMP changes, headcount thresholds), P12 (incidents, breaches), P14 (grievance escalations), P26 (notices, litigation orders, licence events), Finbyx/Udofin (ecosystem events), and manual logging. Additional seeded types *(v1.1)*: NEW_BRANCH_OPENED (licence/intimation items), NEW_OUTSOURCING_ARRANGEMENT, LICENCE_RECEIVED/EXPIRING (P26), REGULATOR_INSPECTION_STARTED/REPORT_RECEIVED, DATA_BREACH_DETECTED (sealed handling), CHANGE_IN_AUDITOR, CHANGE_IN_FINANCIAL_YEAR, ENTITY_CROSSED_THRESHOLD (from P15), FOREIGN_SUBSIDIARY_INCORPORATED (P25).

### 4E. Not applicable, waivers, extensions, escalations

**FR-P04-40 Not-applicable claim on an instance** (distinct from instrument removal): maker claims with reason; checker approves; if the claim reveals a profile fact (e.g., "we do not accept public deposits"), the system asks whether to update the entity profile (P15), which then recomputes applicability.

**FR-P04-41 Internal extension.** The owner may request a new internal due date within the statutory date; approvals per delegation matrix (`cmp.extension.approver_by_risk`). Extensions beyond the statutory date are not "extensions" — the instance becomes overdue and, if the regulator grants an extension to this entity (a letter), the CCO records a **regulatory extension** with the letter as evidence.

**FR-P04-42 Waiver / dispensation.** For obligations that permit regulator dispensation or where the entity has a specific exemption, the CCO records a waiver with evidence and expiry; waivers above `cmp.waiver.board_threshold_risk` (default HIGH) require Board/Committee noting (P06 agenda item auto-proposed).

**FR-P04-43 Escalation ladder** (default; P02 setting, tenant may tighten, not loosen beyond floors):

| When | Action |
|---|---|
| Window opens (T − 30 d or per rule) | Instance becomes OPEN; maker notified (digest) |
| T − 15 d | Reminder |
| T − 7 d | Reminder; appears in "Due this week" |
| T − 3 d | Reminder to maker and checker; department head digest |
| T − 1 d | Reminder; High-risk: CCO notified |
| T (statutory) | Overdue; maker, checker, department head notified; High-risk: CCO and the KMP owner |
| T + 3 d | Escalation to CCO for all risks; High-risk: MD/CEO digest |
| T + 7 d | Exception auto-proposed (§4F); CCO must decide |
Internal-due-date reminders run in parallel. Reminders stop when submitted; escalation of an UNDER_REVIEW item targets the checker.

**FR-P04-44 Delegation and backup owners.** When an owner is on approved leave (P13 leave data or manual out-of-office), open and new instances route to the backup owner for the leave period and return afterwards (TeamLease-style auto-transfer); delegation never routes a checker task to the maker of the same instance (NN-05).

**FR-P04-45 "Waiting on" and workload (IMP-030, IMP-037) *(v1.1)*.** A maker can set an instance to **Waiting on** a named party (internal user, external requestee, regulator, vendor) with a follow-up date; the internal SLA and reminders pause, the statutory clock does not (NN-33), and the follow-up date creates a reminder for the maker. A **Workload view** for department heads shows open items per owner weighted by count × risk × days to due, with suggested reassignments (Vidhi L1); reassignment is one drag-and-drop with reason.

**FR-P04-46 Risk-adaptive ladders (IMP-043) *(v1.1)*.** The escalation ladder is a G-tier template per risk level (High: window opens earlier, reminders at T−21/−10/−5/−2/−1, department head copied from T−5, CCO from T−1; Low: T−7/−1 only) that tenants tune above floors (T tier). Ladders also adapt to behaviour: an owner with two late closures in the last four periods starts receiving the High ladder for that checkpoint (`cmp.ladder.adaptive`, T, default ON).

### 4F. Exception register

**FR-P04-50** *(v1.1: exceptions are the compliance-sourced type of the shared issue model used by P08, P10 and P12.)* An exception is a recorded non-compliance or partial compliance: instance link, description, root cause (vocabulary: PROCESS_GAP, RESOURCE, SYSTEM, THIRD_PARTY, INTERPRETATION, REGULATORY_CHANGE, OTHER), impact, penalty exposure estimate (from Appendix G penalty rules), regulatory reporting required? (yes/no with the relevant checkpoint, e.g., breach reporting), remediation plan (actions, owners, dates), risk acceptance (link to ERM P08 risk acceptance if remediation is not planned), status (OPEN, REMEDIATION_IN_PROGRESS, REMEDIATED, VALIDATED, ACCEPTED_RISK, CLOSED), validation by checker or internal audit. Exceptions emit `ComplianceIssueRaised` (Ecosystem Spec) and appear in CCO and Board reports.

**FR-P04-51 Action plans, remediation library and validated closure (IMP-055–058) *(v1.1)*.** (a) **AI-drafted action plan:** on an exception or issue, Vidhi drafts steps, suggested owners (from the org chart and the checkpoint's department), dates and evidence of remediation, labelled draft; the issue owner edits and approves (NN-47: AI never sets the issue's rating or status). (b) **Remediation library:** per checkpoint, typical fixes, templates and evidence examples curated by the content team (starting with the top 100 NBFC checkpoints) and tenant additions; offered when an exception opens. (c) **Repeat-issue detection:** an exception with the same checkpoint and root cause as one in the previous four periods or audits is flagged "Repeat" to the CCO, counted in the Board report and proposed for the Audit Committee agenda (P06). (d) **Validated closure:** closure requires validation evidence; High-risk exceptions need an independent validator (checker not involved in remediation, or internal audit) before CLOSED.

### 4G. Attestations and compliance certificates

**FR-P04-60 Certification chain.** Configurable chain (default): **Department head quarterly certificate** (list of department instances with status; signed in-app with step-up MFA, optional Aadhaar eSign/DSC) → **CCO certificate** to the Board/Audit Committee (consolidated; exceptions and remediation) → **MD/CEO certificate** where an RBI/SEBI requirement or the tenant's policy calls for it. Certificates are generated as DOCX + PDF from templates (P07 template engine), with the data snapshot hashed and frozen; edits to underlying data after signing produce a "post-certification changes" annex in the next certificate rather than altering the signed one.

**FR-P04-61 Ongoing attestations.** CONTINUOUS checkpoints produce periodic attestation instances (§4B) that can be answered in bulk per owner ("I confirm continued compliance with these 37 items; exceptions: 2"), with exceptions turned into exception records.

### 4H. Auditor columns, sampling and the compliance testing programme

**FR-P04-70** Internal audit (P10) can define sampling rules (e.g., 10 % of closed High-risk instances per quarter, all late closures, all N-A claims) that assign `auditor_user_id` (column AC) to selected instances; auditors record comments (AD) and a conclusion (SATISFACTORY, OBSERVATION, EXCEPTION); observations flow to the audit findings register in P10. External auditors and supervisors read within grant (D-12) and cannot change instance data.

**FR-P04-71 Compliance testing programme (second line; G5 gap) *(v1.1)*.** Distinct from internal audit (third line, P10), the compliance function tests whether controls and compliance actually operate. Elements: (1) **Annual testing plan** per legal entity built from risk (checkpoint risk × exception history × regulator focus × time since last test), approved by the CCO and noted by the Board/Audit Committee (P06); (2) **Test cycles** (quarterly by default) with scope (instruments, departments, branches); (3) **Test scripts** per checkpoint or control — objective, population definition, attributes to test, evidence to inspect, pass criteria — from a platform library (starting with NBFC KYC, Fair Practices Code/Responsible Business Conduct, grievance, digital lending, IRACP classification, outsourcing) and tenant additions; (4) **Sampling** — population pulled from LDC data or from Finbyx/Udofin/third-party systems via P18 (e.g., loans disbursed in the quarter), sample size by method (statistical attribute sampling at a chosen confidence and tolerable deviation rate, or judgemental with documented rationale; defaults: High-risk 95 %/5 %, Medium 90 %/10 %), reproducible random seed recorded; (5) **Execution** — testers record per-sample results (pass/fail/not testable) with evidence; (6) **Results** — deviation rate vs tolerance, conclusion EFFECTIVE / NEEDS_IMPROVEMENT / INEFFECTIVE, auto-raised exceptions for failures with **remediation SLAs by risk** (`cmp.testing.remediation_sla_days`, default High 30, Medium 60, Low 90) and **retest** scheduled after remediation; (7) **Reporting** — testing coverage, deviation rates and repeat findings in the CCO and Board reports; ecosystem event `ControlTestResultPublished` (Ecosystem Spec §9.2) for Finbyx/Udofin controls. Testers cannot test controls they operate (SoD; NN-05). Vidhi may propose samples' attribute checks from documents (L1) but never concludes a test (NN-47).

### 4I. Compliance score and dashboards

**FR-P04-80 Compliance Score.** *(v1.1 glossary: this is the **Compliance Score** — live, instance-based; distinct from the **Health Check Score** of the free pre-signup assessment, P23, and from the optional **Compliance Health Index**, FR-P04-82. No tile ever shows two of them without its label; G5 E-06.)* Default method (configurable, transparent, shown with an "i" explanation): for a scope and period, `score = Σ(weight × status_points) / Σ(weight × max_points)` with weights HIGH 3, MEDIUM 2, LOW 1 and status points: approved on time 1.0; approved late 0.6; partially complied 0.3; open not yet due excluded; overdue 0; exception with approved remediation 0.2; not applicable excluded. Displays score, trend, and the items that most reduce it.

**FR-P04-81 Dashboards (role-based, customisable widgets; Appendix C).**
- *My work* (maker/checker): due today/this week/overdue, returned for rework, awaiting my review, evidence requests.
- *Department head*: department heatmap (instrument × month), overdue by owner, rework rate, certificates due.
- *CCO*: entity-wide score, heatmap by regulator/department/legal entity, upcoming statutory deadlines (30 days), exceptions and ageing, N-A claims, waivers, regulatory filings tracker (with P11), recent Updates impact (P05), audit observations.
- *MD/CEO, Board*: one-page compliance health (score, trend, top risks, exceptions requiring Board attention, penalties paid/avoided), drill-down to evidence.
- *Auditor*: samples, evidence completeness, late closures, changes after closure (Correction Entries).

**FR-P04-82 Compliance Health Index (optional method; owner baseline) *(v1.1)*.** Setting `cmp.score.method` (T: `INSTANCE_SCORE` default, `HEALTH_INDEX`, or `BOTH`) enables the baseline's five-component index: overdue obligations severity-weighted 40 %, evidence completeness 20 %, upcoming readiness (next 30 days assigned with lead time) 15 %, open findings ageing 15 %, governance hygiene (policy review currency, training completion, register freshness) 10 %; grade bands A ≥ 90, B ≥ 75, C ≥ 60, D < 60. The formula is versioned; a formula change annotates trend charts so a jump caused by the method is never read as a change in compliance.

### 4J. Reports

**FR-P04-90 Report catalogue.** *(v1.1: P28 owns module `rpt` — the report builder, MIS catalogue, scheduling engine, board-pack studio and report snapshots; D-47, G5 E-02. P04 contributes the compliance report **definitions** below to the P28 catalogue through its registration contract, and each generated report stores its parameters and data-snapshot hash so it can be re-run "as at" (IMP-072). The **one-page compliance summary** per entity and period — score, overdue, high-risk open, upcoming 30 days, exceptions — is a P04 definition generated as PDF in ≤ 5 s (IMP-070).)* Compliance status report (filters: legal entity, department, regulator, instrument, risk, period, owner); Overdue and ageing report; Upcoming deadlines (7/30/90 days); Department-wise report; Instrument-wise report (per Master Direction — what the CCO presents when RBI asks "show your compliance with the X Directions"); Exception register; N-A and waiver register; Rework and quality report; Timeliness trend; Penalty and late-fee register; Evidence completeness report; Auditor sample report; Certification status; Changes-after-closure report; Workload report (instances per owner, for resource planning). The P28 **report builder** lets business users pick filters, up to 40 columns, groupings, charts and CEL formula columns, save and share templates, and schedule e-mail delivery (daily/weekly/monthly at a set time) — matching and exceeding the Lawrbit matrix-report pattern (IMP-074).

**FR-P04-91 Formats.** XLSX (including the owner's 30-column register format), CSV, PDF, DOCX (narrative reports via templates). Every export is logged (who, what scope, when, hash) and respects the user's ABAC scope.

**FR-P04-92 Board compliance report.** A templated DOCX/PDF with: executive summary (score, trend), compliance by regulator and instrument, overdue and exceptions with remediation, regulatory changes in the period and their implementation status (P05), filings made (P11), audit observations (P10), penalties, certifications, and an annex of instance-level status; generated as a draft, edited in Word (P07 round-trip) and approved by the CCO before it enters the Board pack (P06; assembled in the P28 board-pack studio). AI may draft the narrative (§11); every figure in it comes from report lineage, never from the model (NN-37).

### 4K. Owner's Excel format — register export and WORKSPACE import

**FR-P04-100 Register export.** "Export register (Excel)" produces the owner's template layout for the selected scope: rows = instances, content columns from the effective checkpoint, user columns I, J, T, W–AD populated, CompID in E; nothing is written beyond AD (NN-35). Each row's `Period` and `Instance Ref` are carried in the hidden `_LDC_System` sheet keyed by row (master X-28), the file is declared as export variant `REGISTER` in `_Template_Info`, and the content contract is unaffected (Appendix E §E.9). Dropdowns for W and AA are added in `Rough` for offline updating.

**FR-P04-101 WORKSPACE import application.** After P03 validates a WORKSPACE upload (V-16, V-17), P04 applies each row as the same action the user could take on screen (maker status + evidence references, checker decision), in the user's own name and permissions; rows the user cannot act on are rejected; each applied row emits the normal audit events. Evidence cannot be uploaded through Excel (files are attached in the app); a maker may reference an existing DMS document ID in column U.

### 4L. Calendar (R-094)

**FR-P04-110 Unified calendar.** One calendar service (`wf.calendar_items`) aggregates compliance instances (statutory and internal due dates), tasks, meetings (P06), policy reviews (P07), return deadlines and filing windows (P11), audit fieldwork (P10), training sessions (P21), POSH IC timelines (sealed — shown only to IC members, NN-13), and personal reminders; *(v1.1)* licence and registration renewals and licence-condition items (P26), contract milestones and renewals, litigation hearings and limitation dates (P26), ESG/BRSR and CSR milestones (P27), compliance-testing fieldwork (§4H) and request-list due dates (FR-P04-26). Every producer registers through `packages/calendar` (OP-1). Views: Month, Week, Agenda, Timeline (Gantt by department), Heatmap (density/criticality by day). Filters: regulator, department, legal entity, risk, status, owner, type. Drag-and-drop rescheduling of *internal* dates only (statutory dates are rule-computed), with audit entry.

**FR-P04-111 Visibility by role.** Users see their own items; department heads see all items of their departments; CCO and `ten_admin` see all; KMPs see their attestations and items they own; board members see meetings and Board-level deadlines; sealed items follow sealed-class permissions.

**FR-P04-112 External calendar sync.**

| User's calendar | Method | Direction and behaviour |
|---|---|---|
| Microsoft 365 (work account) | Microsoft Graph, delegated OAuth (`Calendars.ReadWrite`) or tenant-wide admin consent with application permission restricted by an Exchange application access policy to the users who opted in | LDC creates events in a dedicated calendar "LawDocsComply" in the user's mailbox; updates on change; deletes on cancellation; reminder minutes from the user's preference; deep link back to LDC. One-way (LDC → calendar) by default; optional two-way for meetings created in P06 (attendee responses read back) |
| Outlook.com / Hotmail / Live (personal Microsoft account) | Microsoft Graph with personal-account OAuth | Same as above |
| Google Workspace / Gmail | Google Calendar API OAuth (`calendar.events` scope on a secondary calendar created by LDC) | Same; push notifications via Calendar API watch channels for two-way meeting responses |
| Apple iCloud and any other client | ICS subscription feed — per-user secret, revocable URL (`webcal://…/ics/<token>.ics`), read-only, RFC 5545 with `VALARM` reminders; optional CalDAV for advanced users | Refresh interval controlled by the client (Apple configurable; Google may take several hours); the UI warns that ICS is not instant |
| Microsoft Teams | Meetings created via Graph `onlineMeeting` for P06 meetings | Join links in the event |
Privacy setting `cal.external.detail_level` (FULL, TITLE_ONLY, MINIMAL "Compliance item due – open LawDocsComply") — default TITLE_ONLY for external personal calendars and FULL for the tenant's own M365/Google domain; sealed items are always MINIMAL. Disconnect revokes tokens and deletes LDC-created events where the API allows. Two-way sync never changes LDC dates: statutory and assigned due dates are authoritative in LDC, and an edit or deletion of an LDC-created event in an external calendar is reverted on the next sync and logged (NN-07, master X-24); only meeting responses (accept/decline) flow back.

**FR-P04-113 Phone alerts.** Calendar alarms (Graph reminders, VALARM) give native phone notifications through the user's own calendar app (R-094); PWA web push is offered in addition (§4N).

### 4M. Tasks (R-095)

**FR-P04-120 Task model.** `wf.tasks` supports types COMPLIANCE (system-created from instances), AD_HOC, REVIEW, APPROVAL, EVIDENCE_REQUEST, MEETING_ACTION (P06), AUDIT_ACTION (P10), REMEDIATION (P04 exceptions), VIDHI (assigned to the AI employee), with title, description, rich checklist, sub-tasks, attachments, due date/time, priority, labels, links to any LDC record, watchers, dependencies (blocks/blocked-by), effort estimate and time spent (optional), and status (TODO, IN_PROGRESS, BLOCKED, IN_REVIEW, DONE, CANCELLED).

**FR-P04-121 Hierarchy rule.** A user may assign a task to anyone below them in the reporting hierarchy (org chart from P13/P06), to anyone in a department they head, or to themselves; peers and juniors may send a **task request** that the recipient accepts or declines; `ten_admin` and `ten_cco` may assign across the tenant. Delivery staff assign within their engagement scope. Every assignment records assigner, assignee and hierarchy basis.

**FR-P04-122 Tasks to Vidhi.** Any user may assign a task to Vidhi AI ("Draft the quarterly CCO certificate for Q2", "Collect the board resolutions approving the KYC policy and attach them to instance X", "Summarise this RBI letter and propose event-based compliances"). The task executes in P17 under the assigner's permissions and returns outputs as drafts for review; the task shows Vidhi's steps, sources and a **Review** button; nothing leaves the tenant or changes approved records without a human action (NN-14).

**FR-P04-123 Scheduled and recurring tasks.** Users create tasks that run on a schedule — RRULE recurrence (daily, weekly on Monday, first business day of each month, quarterly on the 5th business day…) or a one-off date-time — for humans or Vidhi. A Vidhi scheduled task (modelled on assistant "scheduled tasks") stores: instruction (prompt), scope (records/folders it may read), schedule, timezone, output destination (draft document, task comment, report, e-mail draft), approval requirement, stop condition (end date, count, or until cancelled), and a preview of the next three run times; each run creates a run record with outputs and logs; failures notify the owner; schedules pause automatically when the owner leaves the tenant.

**FR-P04-124 Work Inbox.** A single inbox collects every item needing the user's action — compliance instances, review requests, approvals (from any module), task assignments, mentions, rebase conflicts (P03), Updates requiring impact assessment (P05, shown as items but stored in the Updates model), certificate signatures, meeting actions — sortable by deadline and risk, with bulk actions, saved views, keyboard navigation and "snooze until" for non-mandatory items.

**FR-P04-125 Dependencies, comments and series (IMP-051–053) *(v1.1)*.** (a) **Dependencies** between instances and tasks ("blocked until checkpoint X complied", e.g., policy approval before attestation) with a visual chain on the instance and a "Blocked" filter; (b) **threaded comments** with @mentions on every instance, visible to auditors within scope; (c) the **recurrence engine owns each series**: ending or changing a series affects only future instances after confirmation, never history (NN-29); (d) **bulk archive** of completed reports, obsolete drafts and closed tasks (IMP-050).

### 4N. Notifications service (NN-27)

**FR-P04-130 Separation.** `wf.notifications` stores work notifications (assignment, reminder, overdue, escalation, approval request, decision, mention, comment, direct message, calendar event, task scheduled/completed, Vidhi run finished, export ready, system security alerts such as new-device login). Regulatory content lives in `chg.updates` (P05) and is never stored as a notification; the bell icon (Notifications) and the megaphone icon (Updates) are separate, each with its own unread count.

**FR-P04-131 Channels.** In-app (real-time via WebSocket), e-mail (transactional provider; DKIM/SPF/DMARC on `in.lawdocscomply.com`), PWA web push, Microsoft Teams chat card (optional, via Graph or incoming webhook per tenant), WhatsApp Business (opt-in, critical categories only, approved templates via a BSP), SMS (opt-in, critical only, DLT-registered templates and header — TCCCPR), mobile push (when the mobile app ships). Channel availability per category is governed by P02 settings with mandatory floors.

**FR-P04-132 Preferences.** Per user and category: channel, frequency (instant, hourly digest, daily digest at chosen time, weekly), quiet hours (timezone-aware; escalations for owned overdue High-risk items bypass quiet hours only for in-app and e-mail), and "follow"/"mute" per record. **Mandatory floors** (tenant cannot disable): assignment of a High-risk instance, overdue of an owned instance, escalation to the user, approval request older than SLA, security alerts. Digests group by due date and record, with one-click actions (approve Low-risk, open, snooze).

**FR-P04-133 Messaging.** Comments with @mentions on any record; direct messages between users in a tenant; threads per instance. Messages are tenant data, retained per retention settings, exportable (P19), and visible to auditors within grant. Delivery-team messaging with clients uses the same service in the delivery console (P22).

**FR-P04-134 Notification budget, batching and subscriptions (IMP-040–046; G5 E-19) *(v1.1)*.** (1) **Priority tiers** for every notification category: CRITICAL (statutory deadline today/overdue for High risk, security alerts, escalations to the user), HIGH, NORMAL, INFO. (2) **Budget:** at most `wf.notify.fatigue.max_immediate_per_day` (T, default 10, bounds 5–30) immediate notifications per user per day across channels; beyond that, NORMAL/INFO fold into the next digest; CRITICAL is never folded. (3) **Batching:** notifications of the same type and target within `wf.notify.batch_window_minutes` (default 10) are grouped ("You have been assigned 20 items" with a list), one e-mail not twenty. (4) **Subscriptions:** users follow or mute by instrument, entity, department or thread ("only what changed for me"); mutes are audited and cannot cover mandatory floors. (5) **Channel matrix** per category (in-app, e-mail, Teams, WhatsApp opt-in, SMS for CRITICAL only). (6) **Quiet hours** respect the user's timezone and the entity's holiday calendar (narrowing only; CRITICAL overrides). (7) **Alert health** metric per tenant and user — notifications per user per day, open rate, time to acknowledge, mute rate — with recommendations ("12 users receive > 25 notifications a day; switch Low-risk reminders to digest?") on SCR-WF-08.

### 4O. Fewer-click design patterns (R-023, R-028)

- **My Day**: the default landing page for makers and checkers — today's and overdue items with inline evidence drop zones and a single Submit.
- **Smart defaults**: date of compliance = today; maker status inferred from evidence type (e.g., acknowledgement PDF → COMPLIED) — suggestion only; checker defaulted by rule.
- **Evidence reuse**: "Use the same evidence as last period" for CONTINUOUS/attestation items, with a mandatory freshness check (document date within period).
- **Bulk**: multi-select submit, reassign (approval stays sequential except `bulk_approvable` items, NN-46), set internal dates, add watchers, export; long operations run in the background with a results summary ("287 succeeded, 3 failed — download error report").
- **Command palette** (`Ctrl/Cmd+K`): "submit", "assign to", "open instrument", "export overdue".
- **Comment templates** for frequent checker feedback.
- **Auto-close on ecosystem proof**: when a trusted integration event proves completion (e.g., a Finbyx return acknowledgement), the instance moves to UNDER_REVIEW with evidence attached; the checker still approves (no auto-approval for regulatory items).
- *(v1.1)* **In-grid bulk edit (IMP-047, NN-49):** in the register grid, select rows and edit owners, internal dates, tags, watchers and custom fields inline (spreadsheet-style fill-down), with a preview of changes and one Apply; every bulk edit is an undoable batch for `cmp.bulk.undo_window_hours` (T, default 24). Legal-effect actions (approval, N-A acceptance, waiver) are excluded from bulk (NN-46; IMP-049).
- *(v1.1)* **Shared saved views (IMP-048):** any filter/column/grouping set can be saved and shared to a role or department; a department head's "My team this week" view appears for all members.
- *(v1.1)* **My Day 2.0 (IMP-038):** sections Due today · Waiting on me · Blocked · Quick wins (items that need only an evidence drop) · Returned; one-key actions; progress ring for the day.
- *(v1.1)* **Mobile maker flow (IMP-039):** PWA with camera capture (multi-page scan to PDF with edge detection), offline queue that syncs when online, Hindi and regional-language labels; submission rules identical to the web.
- *(v1.1)* **Status explainers (IMP-054):** every status chip has an "i" explaining the canonical status and the tenant label.
- *(v1.1)* **Templates everywhere:** comment templates, request-list templates, test-script templates, event bundles and saved report definitions reduce typing to selection.

### 4P. Automated checkpoints (IMP-015–018) *(v1.1)*

**FR-P04-160 Automated test definition.** A checkpoint or common control may carry a **machine test**: `cmp.automated_tests (test_id, version_no, name, target checkpoint_ids[] / control_id, data_source {LDC module, ecosystem event/API (Finbyx, Udofin), P18 connector, public web check}, rule (CEL over the fetched dataset), schedule (cron or on-event), pass/fail semantics, evidence snapshot spec, requires_attestation bool, owner, status)`. Definitions are **versioned and immutable** — editing creates a new version ("copy to change"), and every result records the test version (IMP-016). Seed tests for the NBFC pack (≥ 10): Grievance Redressal Officer name and contact published on the website (public page check); Key Facts Statement template published for digital loans (Udofin/Finbyx); monthly DLG disclosure published (Udofin `DLGDisclosurePublished`); NPA classification run date not later than the day-end (Finbyx `ClassificationSync` T+1); CIC submission files transmitted for the cycle (Finbyx `bureau_cycle`); Fair Practices Code on website; interest-rate model policy published; KYC re-verification backlog below threshold; board-approved policies within review date (P07); RBI return acknowledgements received for due returns (P11/Finbyx `ReturnStatusUpdated`).

**FR-P04-161 Result states.** Each run produces `PASS`, `FAIL`, `NO_DATA` (source disconnected, empty or stale beyond freshness), or `INVALID` (rule error) — never collapsing data gaps into failures (IMP-017). `PASS` attaches an evidence snapshot (hashed JSON/PDF of the observed data, screenshot for web checks) to the period instance and moves it to `submitted_for_review` (or directly to the attestation step where `requires_attestation`); `FAIL` creates an exception proposal and notifies the owner; `NO_DATA`/`INVALID` create a data-gap task for `ten_integration_admin` and leave the instance with the maker.

**FR-P04-162 Human attestation and approval.** Automated results never close regulatory instances by themselves: the checker approves (or the owner attests, for checkpoints flagged `requires_attestation`; IMP-018); "auto-approve" is permitted only for INTERNAL or SUGGESTIVE checkpoints the tenant explicitly flags and never for High risk (NN-46, NN-47).

**FR-P04-163 Monitoring.** A **Continuous checks** dashboard (SCR-CMP-13) shows tests by state, last run, freshness and trend; consecutive FAILs escalate per the ladder; tests feed KRIs in P08 where mapped.

### 4Q. Compliance Coordinator agent and MCP tools *(v1.1)*

**FR-P04-170 Agent duties (D-34; P17, Appendix AA).** The Compliance Coordinator role agent, sponsored by the CCO, may at autonomy levels configured per tenant (NN-50): L1 — propose reminders, reassignments, events detected in documents, weekly status narrative, and request-list items; L2 — send pre-approved reminder templates to internal users and create draft request lists, within the notification budget. It may never: set or change a compliance status, approve, close, waive, extend, accept evidence, or contact external parties without a human action (NN-14, NN-47). Every agent action shows in the instance activity log as "Vidhi (Compliance Coordinator) on behalf of <sponsor>".

**FR-P04-171 MCP tools (NN-52).** *(v1.1, X1: names aligned with Appendix AA §AA.7.4.)* Read tools exposed through the LDC MCP server under the calling user's permissions: `list_due_items(range)`, `get_instance_status(instance_ref)` (status, dates, evidence list without sealed content), `query_register(filters)` (aggregates), `list_calendar(range)`. Draft tools (L1, create drafts only): `propose_tasks(...)`, `draft_request_list(...)`. No tool can submit, approve or change dates.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P04-X01 — Event catalogue entries from P26 and P15.** The event catalogue (IMP-028) includes `licence condition imposed`, `licence renewed or expired` (consumes `in.lawdocscomply.lit.LicenceRenewalDue` and `LicenceExpired`), `contract obligation confirmed` (`ContractObligationConfirmed` → linked checkpoint instances), `incoming notice received` (`NoticeReceived` → reply-deadline instance with the notice's statutory clock, NN-33) and `new branch or establishment opened` (spawns the licence and registration set for that location: Shops and Establishments, trade licence, GST additional place of business, labour registrations).

**FR-P04-X02 — Body review flag.** Each compliance instance carries `requires_body_review` (Board, committee or general body) derived from the checkpoint's compliance type and Column O/P; P06 agenda auto-suggest reads it so due items reach the right meeting without manual listing.

**FR-P04-X03 — Finding and observation links.** `POST /cmp/issues/{id}/links` links a compliance issue to a P10 audit finding or a P26 regulator observation (IMP-089) in either direction; closing one never closes the other automatically — each owner closes its own record, and the link shows both states.

**FR-P04-X04 — Three dates on all evidence sources.** Evidence arriving from the P13 contractor portal, P26 notices and P16 society records carries act date, evidence date and approval date (NN-48); timeliness is judged on the act date.

**FR-P04-X05 — Leave-aware routing.** Auto-approval of leave in P13 queries P04 for statutory-deadline items owned by the applicant within the leave window; if any exist, the leave request shows them and requires a named backup owner before approval (no statutory item is left unowned, NN-33).

**FR-P04-X06 — Reports through P28.** P04 registers its datasets (`cmp.*`), KPIs (Compliance Score, Compliance Health Index) and report definitions with P28; dashboards and subscriptions are rendered by P28 and honour the notification budget and fatigue settings of FR-P04 notifications (one budget across in-app, e-mail and report subscriptions).

---

## 5. Workflows and state machines

### 5.1 Compliance instance

```
SCHEDULED ──(window opens)──► OPEN ──(maker starts)──► IN_PROGRESS ──(submit)──► SUBMITTED ──► UNDER_REVIEW
UNDER_REVIEW ──APPROVE──► CLOSED (sub-status: COMPLIED_ON_TIME | COMPLIED_LATE | PARTIAL_WITH_EXCEPTION | NOT_COMPLIED_WITH_EXCEPTION | NOT_APPLICABLE)
UNDER_REVIEW ──REJECT──► REWORK ──(resubmit)──► SUBMITTED
UNDER_REVIEW ──REALLOCATE──► OPEN (new maker) | UNDER_REVIEW (new checker)
OPEN/IN_PROGRESS ──(N-A claim)──► SUBMITTED (maker_status = NOT_APPLICABLE_CLAIMED)
any non-closed ──(instrument removed / checkpoint retired before start)──► CANCELLED (reason; kept)
CLOSED ──(audit sample)──► CLOSED + auditor_conclusion
CLOSED ──(Correction Entry, D-02)──► CLOSED with correction annotation (never reopened silently)
CLOSED ──(reopen by CCO with reason, e.g. evidence found defective)──► REWORK (new cycle; original closure retained)
```
`overall_status` (column J) is derived: Not due · Open · Due soon (≤ 7 d) · Overdue · Submitted · Under review · Returned · Closed – on time · Closed – late · Closed – exception · Not applicable · Cancelled. Overdue is a flag computed against the statutory due date, independent of state, so an UNDER_REVIEW item past due is still shown as overdue (with responsibility on the checker).

**Mapping to the canonical compliance status (master §6.3, Appendix A §A.0.5; review R2).** Workflow states are positions in the process; reporting, exports, ecosystem events and column J use the Locked canonical status, derived as follows (tenant labels relabel the canonical values only):

| Workflow state / closure sub-status | Canonical status |
|---|---|
| SCHEDULED, OPEN | `not_started` |
| IN_PROGRESS (tenant interim sub-status) | `in_progress` (`in_progress_interim`) |
| IN_PROGRESS with a "waiting on others" reason | `waiting` (internal SLA paused; statutory clock runs, NN-33) |
| SUBMITTED, UNDER_REVIEW | `submitted_for_review` |
| REWORK | `returned` |
| CLOSED – COMPLIED_ON_TIME | `complied` |
| CLOSED – COMPLIED_LATE | `complied_late` |
| CLOSED – PARTIAL_WITH_EXCEPTION | `partially_complied` |
| CLOSED – NOT_COMPLIED_WITH_EXCEPTION | `not_complied` |
| CLOSED – NOT_APPLICABLE | `not_applicable` |
| CLOSED via approved exemption/waiver (§4E) | `exempted` |
| Open with a recorded regulator extension | `deferred_by_regulator` |
| CANCELLED | `withdrawn` |

The derived display labels above (Not due, Due soon, Overdue …) are views on these values; "Overdue" remains a computed flag.

Guards: maker ≠ checker ≠ (for two-level) second checker (NN-05); APPROVE requires the evidence floor; CLOSED instances are immutable except via Correction Entry; timers in §4E.

### 5.2 Event-based instance creation

```
EVENT_RECORDED (manual | module | ecosystem | Vidhi-proposed→confirmed)
  → [approval if cmp.events.<type>.requires_approval] → EVENT_CONFIRMED
  → for each adopted checkpoint with anchor EVENT:<type> and applicability = APPLICABLE
       create instance(due = event_date + offset, priority by risk, owner by routing)
  → notify owners; calendar items; link instances to the event record
EVENT_CORRECTED (date or attributes changed) → recompute due dates of not-closed instances; log
EVENT_VOIDED (recorded in error; reason; approval) → cancel not-started instances; keep history
```

### 5.3 Exception

```
PROPOSED (auto at T+7 or on NOT/PARTIAL approval) → OPEN (CCO accepts) → REMEDIATION_IN_PROGRESS → REMEDIATED → VALIDATED (checker or IA) → CLOSED
OPEN → ACCEPTED_RISK (CRO/Board per threshold; link to ERM) → CLOSED (on expiry review)
```

### 5.4 Certificate

```
DRAFT (generated snapshot) → IN_SIGNATURE (signatory chain) → SIGNED (hash frozen) → PRESENTED (Board/Committee meeting link, P06) → NOTED
SIGNED → SUPERSEDED (only by a new certificate referencing it)
```

### 5.5 Scheduled task (human or Vidhi)

```
DEFINED → ACTIVE ──(due run)──► RUN_PENDING → RUNNING → { RUN_SUCCEEDED (outputs as drafts) | RUN_FAILED (retry ≤ 3, then notify) }
ACTIVE → PAUSED (owner, or owner deactivated) → ACTIVE | ENDED (stop condition) | CANCELLED
```

### 5.5A Automated test run *(v1.1)*

```
SCHEDULED/ON_EVENT → RUNNING → { PASS (evidence snapshot → instance submitted_for_review | attestation) | FAIL (exception proposed) | NO_DATA (data-gap task) | INVALID (rule error → test owner) }
```

### 5.5B Request list item *(v1.1)*

```
REQUESTED → (reminders per ladder) → UPLOADED (PENDING_ACCEPTANCE) → { ACCEPTED (evidence linked) | RETURNED (comment; back to REQUESTED) } ; REQUESTED → EXPIRED (link expiry; re-issue)
```

### 5.5C Compliance test cycle *(v1.1)*

```
PLANNED → SCOPED (population defined) → SAMPLED (seed recorded) → IN_TESTING → RESULTS_REVIEW (CCO) → { EFFECTIVE → CLOSED | NEEDS_IMPROVEMENT/INEFFECTIVE → REMEDIATION (SLA by risk) → RETEST → CLOSED }
```

### 5.6 Calendar sync

```
DISCONNECTED → AUTHORISING (OAuth) → CONNECTED → (token expiry/revocation) → NEEDS_REAUTH → CONNECTED | DISCONNECTED
Outbound queue: item change → upsert job (idempotent on external_event_id) → success | retry with backoff (≤ 24 h) → failure surfaced in Settings › Calendar health
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Roles | Key elements |
|---|---|---|---|---|
| SCR-CMP-01 | My Day | Home (maker/checker default) | all working users | Due today, overdue, returned, awaiting review; inline drop zone; Submit |
| SCR-WF-00 | Work Inbox *(v1.1: ID aligned with Appendix C §C.9; formerly SCR-CMP-02)* | Inbox (top bar) | all | Unified actionable queue; filters; bulk actions (non-legal-effect only); snooze; keyboard |
| SCR-CMP-03 | Compliance register | Compliance › Register | tenant roles (scoped) | Instance grid with the 30 template columns + Period; saved views; group by regulator/instrument/department; export Excel/PDF; Workspace import |
| SCR-CMP-04 | Instance detail | Register › *instance* | scoped | Header (status, due statutory/internal, risk, maker, checker, regulator); tabs: Overview (effective checkpoint, "Why applicable", clause and source), Evidence (requirements checklist vs items), Workflow & approvals, Comments, Activity log; right panel: Vidhi suggestions, related circulars/updates, related policies; bottom action bar with context CTA |
| SCR-CMP-05 | Review queue | Compliance › Review | checkers | Evidence preview side-by-side with checklist; Approve/Reject/Reallocate; comment templates; "Review next" sequential flow (bulk only for `bulk_approvable` items, NN-46) |
| SCR-CMP-06 | Events | Compliance › Events | authorised triggerers, CCO | Record event (form per type), pending approvals, event history with generated instances |
| SCR-CMP-07 | Exceptions | Compliance › Exceptions | CCO, dept heads, IA, CRO | Register; remediation tracker; ageing; Board flag |
| SCR-CMP-08 | Certificates | Compliance › Certificates | dept heads, CCO, MD/CEO | Generate, review snapshot, sign (step-up, eSign/DSC), history |
| SCR-CMP-09 | Dashboards | Dashboard (role default) | role-based | Widgets per §4I; customise (add/remove/reorder widgets; saved layouts) |
| SCR-CMP-10 | Reports | Reports › Compliance | scoped | Catalogue, builder (filters, ≤ 40 columns), schedules, history of generated files |
| SCR-CMP-11 | Board compliance report | Reports › Board report | CCO, CS | Draft generation, Word round-trip, approve, send to Board pack |
| SCR-WF-01 | Calendar | Calendar | all | Month/Week/Agenda/Timeline/Heatmap; filters; subscribe/connect; drag internal dates |
| SCR-WF-02 | Tasks | Tasks | all | List/Kanban/Calendar views; My tasks, Assigned by me, Team; create; templates; dependencies |
| SCR-WF-03 | Scheduled tasks | Tasks › Scheduled | all | Definitions with next runs preview; run history; pause/resume |
| SCR-WF-04 | Notifications | Bell icon | all | Grouped list, mark read, preferences shortcut |
| SCR-WF-05 | Notification preferences | Profile › Notifications | all | Category × channel matrix, digests, quiet hours, mandatory floors shown locked |
| SCR-WF-06 | Calendar connections | Profile › Calendar; Settings › Calendar policy (admin) | all / `ten_admin` | Connect M365/Google, copy ICS link, detail level, sync health |
| SCR-WF-07 | Messages | Messages | all | Direct and record threads; search |
| SCR-CMP-12 *(v1.1)* | Request lists | Compliance › Requests | makers, checkers, auditors, CCO | Templates, items by owner, external link status, accept/return uploads |
| SCR-CMP-13 *(v1.1)* | Continuous checks | Compliance › Automated checks | CCO, dept heads, `ten_integration_admin` | Tests by state (PASS/FAIL/NO_DATA/INVALID), freshness, versions, run history, data-gap tasks |
| SCR-CMP-14 *(v1.1)* | Compliance testing | Compliance › Testing | CCO, testers | Annual plan, cycles, scripts, sampling calculator with seed, results, deviation rates, remediation and retest |
| SCR-CMP-15 *(v1.1)* | Workload | Compliance › Workload | dept heads, CCO | Owner × weighted load heatmap, suggested reassignments, drag to reassign |
| SCR-CMP-16 *(v1.1)* | Remediation library | Compliance › Exceptions › Library | CCO, owners | Fixes, templates and evidence examples per checkpoint; tenant additions |
| SCR-CMP-17 *(v1.1)* | One-page compliance summary | Dashboard › Summary (also PDF) | KMP, board, CCO | Score, overdue, high-risk open, next 30 days, exceptions — per entity/period |
| SCR-CMP-18 *(v1.1)* | Evidence inbox | Compliance › Evidence inbox | makers, CCO | Forwarded mails awaiting filing with classification suggestions |
| SCR-WF-08 *(v1.1)* | Alert health | Settings › Notifications › Alert health | `ten_admin`, CCO | Notifications/user/day, open and mute rates, budget breaches, recommendations |
| SCR-CMP-19 *(v1.1)* | Log event | Top bar › Log event; palette | authorised triggerers | Event type picker, smart attribute form, bundle preview of instances to be created |

UX: role-default landing pages; every status chip uses text + icon + colour (NN-21); "i" help keys `cmp.status.<code>`, `cmp.freq.<code>`, `cmp.col.<letter>`; empty states guide setup ("No makers mapped for 'Risk Management' — map now"); command palette; keyboard shortcuts (`A` approve, `R` reject with comment focus, `N` next); undo for bulk actions within the batch undo window (NN-49; *v1.1*, replacing the earlier 10-second undo); responsive layouts for tablet/phone (PWA) for review and approval on the go; *(v1.1)* every list remembers the user's last view; the command palette offers "Log event", "Request evidence", "Waiting on…" and "Group with equivalents".

---

## 7. Backend design

### 7.1 Modules
`cmp` (assignments, instances, evidence links, events, exceptions, certificates, score), `wf` (workflow engine, tasks, approvals, Work Inbox, notifications, messages, calendar items, external sync), with `cnt`, `cfg`, `dms`, `ai`, `hr` (leave, org chart), `int` (calendar connectors, ecosystem events), `rpt` (*v1.1*: owned by P28 — P04 registers report definitions and dashboard widgets through the P28 contract).

### 7.2 Tables (key columns)

| Table | Key columns |
|---|---|
| `cmp.obligation_assignments` | assignment_id, tenant_id, legal_entity_id, checkpoint_id, scope_level, scope_ref, applicability_result, rule_pack_version, active_from, active_to |
| `cmp.instances` | instance_id, tenant_id, assignment_id, checkpoint_version_no, overlay_version_no, period_code, period_start, period_end, statutory_due_at, internal_due_at, calendar_code, bdc, state, overall_status, maker_user_id, contributor_ids[], checker_user_id, second_checker_id, auditor_user_id, maker_status, date_of_compliance, filing_or_compliance_date, checker_decision, rework_count, closed_on_time, late_reason, penalty_paid_amount, event_id, recorded_at |
| `cmp.instance_comments` | instance_id, author_id, column_code (X/AB/AD/free), text, created_at |
| `cmp.evidence_links` | instance_id, document_id, requirement_id, source (UPLOAD, DMS, DRIVE, EMAIL, ECOSYSTEM), sha256, added_by |
| `cmp.event_types` / `cmp.events` | event_type, attributes schema, who_can_trigger, requires_approval / event_id, tenant_id, type, event_date, attributes, evidence, state |
| `cmp.due_overrides` | override_id, scope (PLATFORM/TENANT), checkpoint_ids[], period_codes[], new_due_at, source_update_id, reason |
| `cmp.exceptions` | exception_id, instance_id, root_cause, impact, penalty_exposure, remediation JSONB, state, risk_acceptance_ref |
| `cmp.certificates` | certificate_id, type, scope, period, snapshot_object_key, snapshot_sha256, signatories JSONB, state |
| `wf.tasks` / `wf.task_dependencies` / `wf.task_checklists` | task_id, tenant_id, type, assigner_id, assignee_id (user or `svc_vidhi`), basis, links JSONB, due_at, status, priority |
| `wf.schedules` / `wf.schedule_runs` | schedule_id, owner_id, target (TASK_TEMPLATE / VIDHI_INSTRUCTION), rrule, tz, scope JSONB, output_dest, approval_required, stop_condition, state / run_id, started_at, ended_at, outputs, status |
| `wf.approvals` | approval_id, object_ref, step, approver_id, decision, comment, decided_at |
| `wf.notifications` / `wf.notification_prefs` / `wf.deliveries` | category, recipient, channel, payload, read_at / per user×category / provider message IDs, status |
| `wf.messages` / `wf.threads` | thread on record or DM |
| `wf.calendar_items` / `wf.calendar_connections` / `wf.calendar_sync_map` | item_id, source_ref, start/end/all_day, visibility_class / provider, token ref (vault), detail_level, state / item_id ↔ external_event_id, etag |
| `cmp.instances` *(v1.1 columns)* | act_date, confirmed_act_date, evidence_date, approved_at, timeliness_rule, entity_timezone, placeholder bool, equivalence_group_id, control_execution_id, waiting_on JSONB, review_lag_days |
| `cmp.control_executions` *(v1.1)* | execution_id, tenant_id, control_id, period_code, legal_entity_id, state, evidence_ids[], automated_result_id |
| `cmp.equivalence_groups` *(v1.1)* | group_id, tenant_id, legal_entity_id, period_code, instance_ids[], governing_due_at |
| `cmp.automated_tests` / `cmp.automated_results` *(v1.1)* | test_id, version_no, targets, data_source, rule_cel, schedule, requires_attestation, owner / result_id, test_id, version_no, run_at, state, observed_snapshot_key, sha256, instance_id |
| `cmp.request_lists` / `cmp.request_items` *(v1.1)* | list_id, template_id, owner_id / item_id, list_id, assignee (user or external), due_at, state, link_token_hash, link_expires_at, uploaded_doc_id |
| `cmp.event_bundles` *(v1.1)* | event_type, family_code, checkpoint_ids[], attribute_conditions JSONB, version |
| `cmp.test_plans` / `cmp.test_cycles` / `cmp.test_scripts` / `cmp.test_samples` *(v1.1)* | plan_id, entity, year, approved_by / cycle_id, scope / script_id, attributes JSONB / sample_id, population_ref, seed, method, size, result |
| `cmp.remediation_library` *(v1.1)* | entry_id, checkpoint_id, scope, fix_text, templates[], evidence_examples[] |
| `cmp.bulk_batches` *(v1.1)* | batch_id, actor_id, change_count, undo_deadline, undone_at, compensation_ref |
| `wf.notification_budget_ledger` *(v1.1)* | user_id, date, immediate_count, folded_count |
| `wf.subscriptions` *(v1.1)* | user_id, target_type, target_id, mode FOLLOW/MUTE, created_at |

### 7.3 APIs

`GET /cmp/instances` (filters, views) · `GET /cmp/instances/{id}` · `POST /cmp/instances/{id}/evidence` · `POST /cmp/instances/{id}/submit` · `POST /cmp/instances/{id}/review` (`APPROVE|REJECT|REALLOCATE`) · `POST /cmp/instances/bulk` · `POST /cmp/events` · `POST /cmp/events/{id}/confirm|correct|void` · `GET/POST /cmp/exceptions` · `POST /cmp/certificates/generate` · `POST /cmp/certificates/{id}/sign` · `GET /cmp/register/export?format=xlsx|pdf` · `GET /wf/inbox` · `GET/POST /wf/tasks` · `POST /wf/tasks/{id}/assign` · `GET/POST /wf/schedules` · `GET /wf/notifications` · `PUT /wf/notification-prefs` · `GET /wf/calendar?from&to` · `POST /wf/calendar/connections/{provider}` · `GET /ics/{token}.ics` (public, token-authenticated, rate-limited) · `GET /v1/rpt/kpis/cmp.compliance_score/value` *(v1.1, X1: KPI read through the P28 semantic layer; P04 keeps the Compliance Score computation in `cmp` and registers the KPI and its datasets with P28)*. *(v1.1)* `POST /cmp/instances/bulk-edit` (preview + apply; returns batch id) · `POST /cmp/bulk-batches/{id}/undo` · `GET/POST /cmp/request-lists` · `POST /ext/requests/{token}/upload` (public, OTP) · `GET/POST /cmp/automated-tests` · `POST /cmp/automated-tests/{id}/versions` · `GET /cmp/automated-results` · `POST /cmp/events/log` (bundle preview + confirm) · `GET/POST /cmp/test-plans` · `/cmp/test-cycles/{id}/sample` · `/results` · `GET /cmp/workload` · `GET /cmp/summary/one-page?entity&period` · `PUT /wf/subscriptions` · `GET /wf/alert-health`.

### 7.4 Domain events
`in.lawdocscomply.cmp.InstanceCreated.v1`, `…InstanceSubmitted.v1`, `…InstanceReviewed.v1`, `…InstanceOverdue.v1`, `…InstanceEscalated.v1`, `…EvidenceSubmitted.v1` (Ecosystem name `EvidenceSubmitted`), `…ComplianceEventRecorded.v1`, `…ComplianceIssueRaised.v1` (Ecosystem name), `…ExceptionClosed.v1`, `…CertificateSigned.v1`, `…wf.TaskAssigned.v1`, `…wf.TaskCompleted.v1`, `…wf.ScheduleRunCompleted.v1`, `…wf.NotificationDelivered.v1` (internal), `…wf.CalendarSyncFailed.v1`; *(v1.1)* `…cmp.PlaceholderConverted.v1`, `…cmp.ControlExecutionCompleted.v1`, `…cmp.AutomatedTestResultRecorded.v1` (cross-product as `in.infrabyx.grc.ControlTestResultPublished.v1` via `int`, X-01), `…cmp.RequestItemUploaded.v1`, `…cmp.ComplianceTestCycleClosed.v1`, `…cmp.RepeatIssueDetected.v1`, `…cmp.BulkBatchUndone.v1`, `…wf.NotificationFolded.v1` (internal).
Consumed: `cnt.ObligationPublished`, `cnt.InstrumentAdopted/Removed`, `chg.DueDateExtensionPublished` (P05), `hr.LeaveApproved`, `hr.EmployeeExited`, `gov.DirectorAppointed`, `dpc.IncidentRecorded`, Ecosystem `ReturnStatusUpdated`, `ControlTestResultPublished`, `LitigationCaseOpened`, `OrderRecorded`; *(v1.1)* `cnt.CoverageStateChanged` (placeholder conversion), `cnt.ControlMapped`, `cnt.EquivalenceConfirmed`, `lit.LicenceExpiring` and `lit.NoticeReceived` (P26), `esg.MilestoneDue` (P27), `pack.EntityThresholdCrossed` (P15).

### 7.5 Jobs / Temporal
`ScheduleGenerator` (nightly + on change; idempotent per assignment/period), `ReminderLadder` (per instance timers), `OverdueSweep` (hourly), `DelegationResolver` (on leave events), `CertificateSnapshot`, `ReportScheduler`, `DigestBuilder` (per user schedule, timezone-aware), `CalendarOutbound` (queue with backoff), `IcsBuilder` (cached per user, invalidated on change), `VidhiTaskDispatcher` (to P17), `ScheduledTaskRunner`; *(v1.1)* `PlaceholderConversionWorkflow`, `AutomatedTestRunner` (per schedule/event; freshness watchdog), `EquivalenceGrouper` (on schedule generation), `RequestListReminder`, `ExternalLinkExpirer`, `TestCycleWorkflow`, `RepeatIssueDetector` (on exception creation), `BulkUndoWorkflow`, `NotificationBudgetGate` (inline in `packages/notify`), `AlertHealthAggregator` (daily).

---

## 8. Integrations

- **Calendars:** Microsoft Graph (work and personal accounts), Google Calendar API, ICS/CalDAV; Teams online meetings for P06. Tokens in the secrets vault (P00), least-privilege scopes, admin policy to allow/deny providers per tenant.
- **E-mail:** transactional provider (Amazon SES ap-south-1 or equivalent) with bounce/complaint handling; inbound evidence address via the same provider.
- **WhatsApp/SMS:** BSP and SMS aggregator adapters (opt-in, DLT templates; P18 catalogue); Jio Business messaging/calling adapters evaluated in P18 (D-14).
- **Ecosystem:** events listed in §7.4 per Integration Spec v1.1 (§6.15 `grc`, §6.18 `reporting`, §6.10 `litigation`).
- **HRMS:** org chart and leave from P13 (or a third-party HRMS via P18 connector).

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `cmp.schedule.horizon_months` | G | 15 | 12–24 | super admin |
| `cmp.window.default_open_days` | T | 30 | 7–90 | `ten_admin` |
| `cmp.internal_buffer_days.by_risk` | T | H 5, M 3, L 1 | 0–30 | `ten_cco` |
| `cmp.immediate.default_hours` | G | 24 | 1–72 | content lead |
| `cmp.ongoing.attestation_frequency` | T | QUARTERLY | MONTHLY–ANNUAL | `ten_cco` |
| `cmp.review.high_risk_two_level` | T | false | — | `ten_cco` |
| `cmp.review.bulk_approve_enabled` | T | OFF | ON only for content-flagged `bulk_approvable` checkpoints (L floor, NN-46) | `ten_cco` |
| `cmp.review.rework_alert_count` | T | 2 | 1–5 | `ten_cco` |
| `cmp.evidence.required_for` | T | HIGH, MEDIUM | must include HIGH (G floor) | `ten_cco` |
| `cmp.escalation.ladder` | T | per §4E | may add steps/tighten; cannot remove T, T+3 (floor) | `ten_cco` |
| `cmp.events.<type>.who_can_trigger` | T | dept head, CCO, admin | — | `ten_admin` |
| `cmp.events.<type>.requires_approval` | T | false (true for CHANGE_IN_CONTROL, PENALTY_IMPOSED) | — | `ten_admin` |
| `cmp.extension.approver_by_risk` | T | L dept head, M dept head, H CCO | — | `ten_cco` |
| `cmp.waiver.board_threshold_risk` | T | HIGH | — | `ten_cco` |
| `cmp.score.weights` | T | H3 M2 L1 | 1–10 | `ten_cco` |
| `cmp.score.status_points` | T | per §4I | 0–1 | `ten_cco` |
| `cmp.certificate.chain` | T | DEPT → CCO → MD | — | `ten_admin` |
| `cmp.fy_start_month` | T | 4 (April) | 1–12 | `ten_admin` |
| `cmp.week_start_day` | T | MONDAY | — | `ten_admin` |
| `cal.external.providers_allowed` | T | M365, GOOGLE, ICS | subset | `ten_admin` |
| `cal.external.detail_level` | T | own domain FULL; personal TITLE_ONLY | sealed always MINIMAL (L) | `ten_admin` / user (narrow only) |
| `notify.floors` | G | §4N list | cannot be disabled | — |
| `notify.channels.whatsapp.enabled` | T | OFF | requires BSP contract | `ten_admin` |
| `notify.channels.sms.enabled` | T | OFF | DLT templates | `ten_admin` |
| `notify.quiet_hours.default` | T | 20:00–08:00 local | — | user |
| `notify.digest.default` | T | daily 08:30 local (work digest, NN-27) | — | user |
| `wf.tasks.assignment_rule` | T | HIERARCHY | HIERARCHY, DEPARTMENT, OPEN | `ten_admin` |
| `wf.schedules.max_active_per_user` | T | 25 | 1–200 | `ten_admin` |
| `tpl.workspace.max_export_age_days` | T | 30 | 1–180 | `ten_admin` |
| `cmp.timeliness.rule` *(v1.1)* | G (tenant maker-checker) | ACT_DATE | ACT_DATE, ACT_AND_APPROVAL | `ten_cco` + approver |
| `cmp.timeliness.max_evidence_gap_days` *(v1.1)* | T | 30 | 0–180 | `ten_cco` |
| `cmp.requests.external_link_days` *(v1.1)* | T | 7 | 1–30 | `ten_admin` |
| `cmp.evidence.rules_overridable` *(v1.1)* | T | Medium and Low only | never High (L floor) | `ten_cco` |
| `cmp.ladder.adaptive` *(v1.1)* | T | ON | ON/OFF | `ten_cco` |
| `cmp.score.method` *(v1.1)* | T | INSTANCE_SCORE | INSTANCE_SCORE, HEALTH_INDEX, BOTH | `ten_cco` |
| `cmp.dashboard.collapse_equivalents` *(v1.1)* | T | ON for executive views | ON/OFF per view | `ten_admin` |
| `cmp.bulk.undo_window_hours` *(v1.1)* | T | 24 | 1–72 | `ten_admin` |
| `cmp.testing.remediation_sla_days` *(v1.1)* | T | H 30, M 60, L 90 | may tighten only below G defaults | `ten_cco` |
| `cmp.testing.sampling_defaults` *(v1.1)* | T | H 95 %/5 %, M 90 %/10 %, L judgemental | — | `ten_cco` |
| `cmp.automated_tests.auto_approve_internal` *(v1.1)* | T | OFF | ON only for INTERNAL/SUGGESTIVE, never High (L floor) | `ten_cco` |
| `wf.notify.fatigue.max_immediate_per_day` *(v1.1)* | T | 10 | 5–30 (CRITICAL exempt) | `ten_admin`; user may lower |
| `wf.notify.batch_window_minutes` *(v1.1)* | T | 10 | 1–60 | `ten_admin` |
| `ai.autonomy.agent.VA-02` *(v1.1; X1: key aligned with P17 `ai.autonomy.agent.<agent>`; was `wf.agent.coordinator.autonomy`)* | T | L1 | L0–L2 for P04 actions (NN-50; P17 platform ceiling applies) | `ten_cco` |

---

## 10. Security, privacy and audit

- ABAC: instance visibility by legal entity, department, assignment, sealed class; server-side enforcement on list, detail, export, calendar feed and search (NN-01).
- Every state transition, assignment, evidence add/remove (removal = unlink with reason; the file stays in WORM storage), decision, extension, waiver, event, certificate signature and export is an audit-ledger event (R-075, R-088); auditors can replay an instance's history.
- ICS tokens: 256-bit random, per user, revocable, rate-limited, contain no tenant name; feed content follows detail level; tokens rotate on password reset.
- Evidence e-mail ingestion: sender verification (tenant user + DMARC pass), malware scan, size limits, quarantine for unknown senders.
- External calendar data is minimised; no evidence content is ever written to an external calendar.
- Retainer delivery users act under tenant grants with "acting for LawDocs" badges in the audit trail (P22).
- Correction Entries only for closed instances (D-02).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Vidhi behaviour | Guardrail |
|---|---|---|
| Evidence sufficiency check (Komrisk "Kompare"-style) | Compares uploaded documents with expected evidence (type, period, entity name, signatures, dates) and flags gaps | Advisory note to maker and checker; never approves (NN-14) |
| Status suggestion | Suggests maker status and date from evidence (e.g., acknowledgement date) | Maker confirms |
| Event detection | Reads uploaded letters/notices and proposes events (e.g., SHOW_CAUSE_NOTICE_RECEIVED) | Human confirmation creates the event |
| Narrative drafting | Drafts CCO certificate commentary and Board report narrative from data | Draft; CCO edits/approves; sources (instance IDs) cited |
| Workload balancing | Suggests reassignment when an owner is overloaded or on leave | Department head decides |
| Tasks to Vidhi / scheduled Vidhi tasks | Executes instructions with read scope, produces drafts | Assigner's permissions; outputs as drafts; full run log (P17) |
| Natural-language queries | "Show overdue High-risk RBI items in Mumbai branch" → filtered view | Query translated to filters visible to the user; ABAC applies |
| Evidence date extraction *(v1.1)* | Reads the date, issuer, entity and period from evidence | Feeds evidence rules; maker confirms; never sets status (NN-47) |
| E-mail-in classification *(v1.1)* | Files forwarded attachments to instances | Unclassified items wait in the Evidence inbox |
| Action plans *(v1.1)* | Drafts remediation steps, owners and dates | Issue owner approves; rating unchanged by AI |
| Compliance Coordinator agent *(v1.1)* | Reminders, request drafts, weekly status (L1–L2) | Bounded autonomy, notification budget, sponsor accountable (NN-50) |
| Test support *(v1.1)* | Suggests attribute checks on sampled documents | Tester concludes; AI never concludes a test (NN-47) |

---

## 12. Acceptance criteria (`tests/acceptance/p04/*.feature`)

```gherkin
Feature: Instance generation
  Scenario: Quarterly checkpoint with period-end offset
    Given an adopted checkpoint with frequency QUARTERLY and due rule PERIOD_END + 21 calendar days
    When the schedule generator runs on 1-Oct-2026
    Then an instance for FY2026-27-Q3 exists with statutory due date 21-Jan-2027
    And the internal due date is 5 days earlier for a High-risk checkpoint

  Scenario: Event-based director appointment
    Given checkpoints anchored to DIRECTOR_APPOINTED with offsets of 30 days
    When the CS records a director appointment dated 10-Nov-2026
    Then instances are created due 10-Dec-2026 and assigned per routing

  Scenario: Content release does not change closed instances
    Given a closed instance of checkpoint X version 2
    When a release changes X to version 3
    Then the closed instance still displays version 2 text and future instances use version 3

Feature: Maker-checker
  Scenario: Maker cannot approve own submission
    Given user U is maker of instance I
    When U attempts to review I
    Then the API returns LDC-CMP-003 and the attempt is logged (NN-05)

  Scenario: High-risk evidence floor
    Given a High-risk instance with two mandatory evidence requirements
    When the maker submits with one document
    Then submission is blocked with LDC-CMP-010 naming the missing requirement

  Scenario: Retainer maker with client checker
    Given the tenant set "LawDocs as maker" for department Compliance
    Then new instances in Compliance have a dlv_rm maker and a client employee checker
    And the audit trail shows "acting for LawDocs" on the maker's actions

  Scenario: Delegation on leave
    Given maker M has approved leave from 1 to 10 Dec 2026 and backup B
    Then open instances of M route to B during the leave and return to M on 11 Dec

Feature: Calendar and notifications
  Scenario: Microsoft 365 sync
    Given a user connected Microsoft 365
    When an instance is assigned to the user
    Then an event appears in the user's "LawDocsComply" calendar within 15 minutes with a deep link

  Scenario: ICS privacy
    Given a POSH IC timeline item (sealed)
    Then the user's ICS feed shows it only as "Confidential item – open LawDocsComply" (NN-13)

  Scenario: Updates and notifications are separate
    When a regulatory update is published
    Then it appears in the Updates inbox and not in the Notifications list (NN-27)

  Scenario: Mandatory floor
    When a user tries to disable overdue alerts for owned High-risk items
    Then the preference toggle is locked with an explanation

Feature: Exports
  Scenario: Register export in owner's format
    When the CCO exports the register for the RBI NBFC Governance Directions
    Then the workbook has the owner's row-1 and row-2 headers and columns A–AD populated per mapping, nothing beyond AD (NN-35)
    And each row's Period and Instance Ref are in the hidden _LDC_System sheet
    And re-importing it in WORKSPACE mode with 5 maker status changes applies only rows the user may act on

Feature: Three dates and timeliness (v1.1)
  Scenario: Filed on time, approved late
    Given an instance due 15-Jan-2027 whose act date is 14-Jan-2027 with an acknowledgement dated 14-Jan-2027
    When the checker approves on 18-Jan-2027
    Then the canonical status is complied, not complied_late
    And the checker's review lag of 3 days is recorded

  Scenario: Act date after evidence date rejected
    Given evidence dated 12-Jan-2027 of class "Portal acknowledgement"
    When the maker enters act date 14-Jan-2027
    Then submission is blocked with a message naming the evidence date

Feature: Placeholders (v1.1)
  Scenario: Placeholder converts on publication
    Given a tenant adopted a PLANNED RBI direction and its placeholder has two quarterly attestations
    When the direction's sheet is published
    Then detailed instances are created from the publication date
    And the placeholder closes as withdrawn with its attestations kept in history

Feature: Automated checks (v1.1)
  Scenario: Disconnected source is not a failure
    Given an automated test reading Udofin DLG disclosures
    When the Udofin connector is disconnected
    Then the result is NO_DATA, a data-gap task goes to the integration admin, and the instance stays with the maker

Feature: Event bundles (v1.1)
  Scenario: Director appointed in a listed NBFC
    When the CS logs DIRECTOR_APPOINTED with "independent = yes"
    Then the bundle preview lists DIR-12, the MBP-1 index entry, DIR-8, fit-and-proper, the RBI intimation and the LODR Reg 30 disclosure
    And confirming creates all of them with due dates from the appointment date

Feature: Notification budget (v1.1)
  Scenario: Budget and batching
    Given a user with the default budget of 10 immediate notifications
    When 20 NORMAL assignments and 1 CRITICAL overdue alert arrive in 5 minutes
    Then the user receives one batched assignment e-mail, the CRITICAL alert immediately, and the overflow in the next digest

Feature: Bulk edit with undo (v1.1)
  Scenario: Undo a bulk reassignment
    Given a department head reassigned 200 instances in the grid
    When she clicks Undo within 24 hours
    Then all 200 assignments revert through a compensating batch and the ledger shows both batches (NN-49)

Feature: Compliance testing (v1.1)
  Scenario: Statistical sample is reproducible
    Given a KYC test script on 4,212 loans disbursed in Q3 with High-risk defaults
    When the tester draws the sample
    Then the sample size and random seed are recorded and re-drawing with the seed returns the same loans
    And a failed sample raises an exception with a 30-day remediation SLA and a scheduled retest
```
NN tests: `NN-01_instance_list_scoped`, `NN-03_release_spares_closed_instances`, `NN-05_maker_checker_distinct`, `NN-13_sealed_items_minimal_in_calendar`, `NN-14_vidhi_cannot_approve_instance`, `NN-21_status_chips_accessible`, `NN-27_updates_not_in_notifications`, `NN-29_cancelled_instances_retained`; *(v1.1)* `NN-33_waiting_does_not_move_statutory_date`, `NN-46_no_bulk_approval_legal_effect`, `NN-47_agent_cannot_set_status`, `NN-48_three_dates_recorded`, `NN-49_bulk_edit_undo`, `NN-50_coordinator_autonomy_bounded`, `NN-52_mcp_instance_tools_scoped`.

---

## 13. Deliverables and exit gate

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
13. *(v1.1)* Three-date model and timeliness rule; placeholder instances and conversion; equivalence groups and control executions.
14. *(v1.1)* Automated checkpoints with ≥ 10 NBFC seed tests and the Continuous checks screen.
15. *(v1.1)* Event bundles with Log event; request lists with external links; evidence rules, reuse, e-mail-in classification.
16. *(v1.1)* Compliance testing programme (plans, cycles, scripts, sampling, results, remediation, retest); issue action plans, remediation library, repeat detection, validated closure.
17. *(v1.1)* Notification budget, batching, subscriptions, alert health; in-grid bulk edit with undo; shared views; My Day 2.0; offline mobile maker flow.
18. *(v1.1)* Compliance report definitions registered in P28; one-page summary; Compliance Coordinator agent at L1; MCP tools.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P04-01 | Holiday-shift conventions per regulator | Regulators differ; many deadlines are not extended for holidays | Content lead | Default NONE; per-checkpoint setting; P11 return definitions override [VERIFY per authority] |
| OI-P04-02 | M365 application access policy vs delegated consent | Tenant IT preference | Customer IT | Delegated per-user OAuth default |
| OI-P04-03 | WhatsApp BSP and SMS aggregator selection | Contracts; DLT registration | Product owner | Channels OFF |
| OI-P04-04 | MD/CEO certificate requirement by entity type | Varies by sector and tenant policy | Content lead (Appendix G) | Chain configurable; default DEPT → CCO → MD |
| OI-P04-05 | Compliance score method | Owner may prefer a different weighting for sales/benchmarking | Product owner | Transparent default (§4I) |
| OI-P04-06 | Apple calendar push | Apple has no public push API for third-party calendars | — | ICS/CalDAV; native reminders via VALARM |
| OI-P04-07 | Statutory due-date data for every checkpoint | Due rules must be authored for all migrated rows | Content team | Instances without a due rule use frequency defaults and are flagged "due rule not verified" |
| OI-P04-08 *(v1.1)* | Data sources for the seed automated tests | Depends on Udofin/Finbyx events and tenant website URLs | Product owner / integrations | Tests ship OFF per tenant until the source is connected (NO_DATA) |
| OI-P04-09 *(v1.1)* | Default sampling parameters for compliance testing | Owner/industry practice | CCO advisory panel | Defaults per §4H; tenant-tunable |
| OI-P04-10 *(v1.1)* | Whether any regulator expects approval-date timeliness | Some tenants' policies may | Content lead | `cmp.timeliness.rule` lets the tenant choose the stricter rule |

---

## 15. Sources (accessed 25 October 2026)

1. Owner's sample workbooks and Part-2 commands (column definitions for I, J, T, U, V, W–AD), supplied 25-Oct-2026.
2. Owner's architecture document Part 1 — Compliance Calendar, Compliance Task Detail, Notifications, Bulk Operations, Accessibility sections.
3. Lawrbit GCMS solution overview (5 layers of defence; reallocate; FY calendar; heat maps; matrix report builder; scheduled reports; compliance certificates): https://www.lawrbit.com/wp-content/uploads/2024/07/solution-overview-gcms-india.pdf
4. TeamLease RegTech (performer/reviewer/approver/backup owner; auto-transfer on leave; tiered reminders T-7 → T+3; read-only time-bound auditor access; calendar sync): https://teamleaseregtech.com/product-services/statutory-regulatory-compliance-management-software/
5. Lexplosion Komrisk (escalation to senior management; Kompare evidence checking; KAI assistant): https://lexplosion.in/compliance-management-software/
6. Microsoft Graph calendar API documentation (events, calendars, reminders, onlineMeeting) — https://learn.microsoft.com/graph/api/resources/calendar [VERIFY scopes at build]
7. Google Calendar API (events, secondary calendars, push notifications) — https://developers.google.com/calendar/api [VERIFY]
8. IETF RFC 5545 (iCalendar, RRULE, VALARM) and RFC 4791 (CalDAV).
9. Infrabyx Ecosystem Integration Specification v1.1 §6.15, §6.18, §9.2 (event names `EvidenceSubmitted`, `ComplianceIssueRaised`, `ReturnStatusUpdated`, `ControlTestResultPublished`).
10. TRAI Telecom Commercial Communications Customer Preference Regulations 2018 (as amended) — DLT templates for SMS [VERIFY current amendments].
11. *(v1.1)* Appendix Z (customer feedback and improvement backlog IMP-015–IMP-058, IMP-070–IMP-075) — vendor review and help-centre sources listed there; Appendix AB §AB.6 (placeholder items); Appendix AC / G5 gap list (compliance testing, alert fatigue, licences); Appendix AA (agent workforce, autonomy levels).

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-33, NN-46; X-11, X-24 (LDC dates authoritative over synced calendars), X-26 (this phase owns `packages/workflow`, `notify`, `calendar`, SCR-RPT-01, SCR-WF-00 Work Inbox, SCR-CORE-21 global search; SCR-WF-01 remains the Calendar).

**Added in v1.1:** NN-47, NN-48, NN-49; X-43, X-46, X-60.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
