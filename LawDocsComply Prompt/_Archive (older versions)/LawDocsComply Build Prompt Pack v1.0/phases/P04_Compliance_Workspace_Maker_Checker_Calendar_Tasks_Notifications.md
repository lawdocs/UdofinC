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
> **Estimated effort:** 8 two-week sprints for a squad of 9 (scheduling engine 2; maker-checker and evidence 2; calendar and sync 2; notifications and inbox 2; reports 1).

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

---

## 2. Scope (in / out)

**In scope:** compliance-instance generation; due-date and frequency engine with business-day conventions and holiday calendars; event-based triggers; maker/checker/auditor workflow mirroring template columns T–AD; evidence capture and reuse; rework, reallocation, delegation and backup owners; not-applicable claims, waivers, extensions; escalation ladders; exception register; attestations and compliance certificates (department → CCO → MD/CEO → Board); compliance score; reports and scheduled reports; Excel and PDF exports; unified calendar with external sync; task management (hierarchical assignment, sub-tasks, dependencies, checklists, recurring and scheduled tasks, tasks to Vidhi AI); Work Inbox; Notifications service with channels, digests, quiet hours and mandatory floors; WORKSPACE import application.

**Out of scope:** regulatory Updates and change impact (P05); meeting/committee scheduling (P06 — uses this calendar); policy reviews (P07 — uses this scheduler); return preparation (P11 — publishes due dates here); Vidhi's agent runtime (P17 — receives tasks from here); HR leave data (P13 — consumed for delegation); billing (P20).

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

---

## 4. Functional requirements

### 4A. From checkpoints to compliance instances

**FR-P04-01 Applicability scope.** For each adopted instrument (P03 §4F) and each tenant legal entity, the engine evaluates each effective checkpoint (base ⊕ overlays) through the applicability interface (P03 §4H). For APPLICABLE results a **compliance obligation assignment** (`cmp.obligation_assignments`) is created per legal entity and, where the checkpoint's `scope_level` requires it, per **establishment/branch/location** (labour registers per establishment, shops-and-establishments per state, branch-level KYC checks), per **product** (digital lending products), or per **committee** (meeting-related checkpoints). NEEDS_INPUT results create a one-time "Answer to confirm applicability" task for the CCO.

**FR-P04-02 Instances.** Each assignment generates **compliance instances** (`cmp.instances`) according to its frequency and due rule, for a rolling horizon (`cmp.schedule.horizon_months`, default 15 — current FY plus the next quarter, so the January full-year calendar view that competitors offer is available). Each instance pins `checkpoint_version_no` and `overlay_version_no` at creation (NN-03/NN-07); a later content release regenerates only **future, not-started** instances and records the change.

**FR-P04-03 Instance identity.** `instance_ref = <comp_id>/<legal-entity code>/<scope code>/<period code>` (e.g., `RBI-NBFC.GOV25.0012/LE01/HO/FY2026-27-Q3`; CompID format per Appendix E §E.8), shown to users and used in exports (column E carries CompID; the period travels in the `_LDC_System` sheet of the register export, see §4K).

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

### 4C. Instance lifecycle (mirrors template columns T–AD)

**FR-P04-20 Column mapping.** The owner's user columns map one-to-one to instance fields, so the Excel register and the screen always agree:

| Col | Header | Instance field | Set by |
|---|---|---|---|
| I | Date of Compliance | `date_of_compliance` | Maker (defaults to submission date; editable within rules) |
| J | Status | `overall_status` (system) | System (derived from state, §5.1) |
| T | Maker User/Email ID | `maker_user_id` (+ email) | Routing / reassignment |
| U | Upload Document or Evidence | `evidence_items[]` (link to DMS) | Maker |
| W | Status Update by Maker User | `maker_status` | Maker: COMPLIED, PARTIALLY_COMPLIED, NOT_COMPLIED, NOT_APPLICABLE_CLAIMED, IN_PROGRESS, COMPLIED_LATE |
| X | Comments, if any, by Maker User | `maker_comments` | Maker |
| Y | Checker User/Email ID | `checker_user_id` | Routing |
| Z | Filing/Compliance Date | `filing_or_compliance_date` | Checker confirms (e.g., portal acknowledgement date) |
| AA | Review- Approve, Reject, Reallocate | `checker_decision` | Checker: APPROVE, REJECT, REALLOCATE |
| AB | Comments, if any, by Checker User | `checker_comments` | Checker |
| AC | Assigned Auditor/Email ID | `auditor_user_id` | Audit sampling (§4H) or CCO |
| AD | Comments, if any, by Auditor | `auditor_comments` + `auditor_conclusion` | Auditor |

**FR-P04-21 Routing.** Maker and checker resolve per P03 FR-P03-63 (instance → function → department → legal entity → CCO), with **checker rules**: department head by default; for High-risk instances optionally the CCO or a second-level checker (`cmp.review.high_risk_two_level`). A rule engine (P02) allows routing by legal entity, location, product, amount or tag (e.g., all `board_reporting` items to the CS as checker). For retainer clients (R-072), the tenant can set "LawDocs as maker" for a department, function or instrument: the assigned `dlv_rm`/`dlv_professional` is maker and a client employee is checker; multiple makers per instance are supported (primary + contributors), and both the client admin and the delivery lead can create maker users (P22).

**FR-P04-22 Evidence.** Maker attaches evidence by drag-and-drop, from the DMS (P07), from a connected drive (OneDrive/SharePoint/Google Drive via P18), from an email forward address (`evidence+<instance-token>@in.lawdocscomply.com`, sender must be a tenant user; attachments scanned), or from an ecosystem event (e.g., Finbyx `ReturnStatusUpdated` with acknowledgement → auto-attached as evidence with source label). Each evidence item records hash, uploader, time, source, and the expected-evidence requirement it satisfies (P03 FR-P03-06). One document can satisfy several instances (linked, not copied). Vidhi may check sufficiency (§11) — advisory only.

**FR-P04-23 Submission rules.** Submit requires: maker status set; date of compliance not in the future (unless status IN_PROGRESS); for COMPLIED/COMPLIED_LATE at least one evidence item per mandatory requirement (configurable floor per risk: `cmp.evidence.required_for` default HIGH and MEDIUM); for NOT_APPLICABLE_CLAIMED a reason and supporting note; for NOT_COMPLIED or PARTIALLY_COMPLIED a remediation proposal (date, action, owner) that creates an exception on approval (§4F).

**FR-P04-24 Review.** The checker sees the checkpoint text (effective), clause and source link, control activity, expected evidence vs uploaded evidence (tick list), maker comments, history, and Vidhi's sufficiency note. Decisions: **Approve** (closes; status per maker status and timeliness), **Reject** (returns to maker with mandatory comment; rework counter increments; repeated rejections ≥ `cmp.review.rework_alert_count` notify the department head), **Reallocate** (to another maker or checker with reason; the original maker is notified). There is no bulk approval of compliance instances (NN-46): the checker moves through the queue with **Review next**, which opens the next item with its evidence preloaded. The only bulk exception is for checkpoints flagged `bulk_approvable` in content (Low risk and compliance type Suggestive or Internal Compliance); it opens a confirmation listing every item and records each approval individually.

**FR-P04-25 Timeliness.** `closed_on_time` = approval and date of compliance ≤ statutory due date; `closed_late` otherwise; late closure requires the maker to state the reason and whether any late fee/penalty was paid (feeds penalty ledger and the P20 savings model; paid amounts recorded with challan evidence).

### 4D. Event-based compliance

**FR-P04-30 Event catalogue.** `cmp.event_types` (seeded, tenant-extendable): DIRECTOR_APPOINTED, DIRECTOR_RESIGNED, KMP_APPOINTED, KMP_CHANGED, AUDITOR_APPOINTED, AUDITOR_RESIGNED, BOARD_MEETING_HELD, GENERAL_MEETING_HELD, CHANGE_IN_REGISTERED_OFFICE, CHANGE_IN_SHAREHOLDING (with thresholds), CHANGE_IN_CONTROL, ALLOTMENT_OF_SECURITIES, CHARGE_CREATED/MODIFIED/SATISFIED, BRANCH_OPENED/CLOSED, NEW_PRODUCT_LAUNCHED, OUTSOURCING_ARRANGEMENT_ENTERED, MATERIAL_OUTSOURCING_TERMINATED, CYBER_INCIDENT_DETECTED, FRAUD_DETECTED, PERSONAL_DATA_BREACH, LARGE_EXPOSURE_BREACH, RBI_INSPECTION_REPORT_RECEIVED, SHOW_CAUSE_NOTICE_RECEIVED, PENALTY_IMPOSED, EMPLOYEE_HEADCOUNT_THRESHOLD_CROSSED, POSH_COMPLAINT_RECEIVED (sealed; NN-13), GRIEVANCE_ESCALATED, LISTING_OF_SECURITIES, PRICE_SENSITIVE_INFORMATION, RELATED_PARTY_TRANSACTION_PROPOSED, DIGITAL_LENDING_APP_ONBOARDED, LSP_ENGAGED.

**FR-P04-31 Triggers.** Events can be recorded (a) manually by authorised users (setting `cmp.events.<type>.who_can_trigger`, with optional approval before instances are created — the Lawrbit-style restriction), (b) automatically from LDC modules (P06 governance: director appointed; P13 HRMS: KMP changed; P12: incident logged; P14: grievance escalated), (c) from ecosystem events (Finbyx `LitigationCaseOpened`, `OrderRecorded`, `DLGDisclosurePublished`; Udofin LSP onboarding), or (d) proposed by Vidhi from a document it read (e.g., an RBI letter) — proposal requires a human confirmation. Each event carries `event_date`, attributes and evidence; all checkpoints whose due rule anchors to that event type (and whose applicability passes) generate instances with due dates computed from `event_date`.

**FR-P04-32 Chained obligations.** Due rules may anchor to another checkpoint's completion (`FILING_OF:<comp_id>`), e.g., file the intimation within 7 days after the Board approves; dependencies (pre/post) block or warn as configured.

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

### 4F. Exception register

**FR-P04-50** An exception is a recorded non-compliance or partial compliance: instance link, description, root cause (vocabulary: PROCESS_GAP, RESOURCE, SYSTEM, THIRD_PARTY, INTERPRETATION, REGULATORY_CHANGE, OTHER), impact, penalty exposure estimate (from Appendix G penalty rules), regulatory reporting required? (yes/no with the relevant checkpoint, e.g., breach reporting), remediation plan (actions, owners, dates), risk acceptance (link to ERM P08 risk acceptance if remediation is not planned), status (OPEN, REMEDIATION_IN_PROGRESS, REMEDIATED, VALIDATED, ACCEPTED_RISK, CLOSED), validation by checker or internal audit. Exceptions emit `ComplianceIssueRaised` (Ecosystem Spec) and appear in CCO and Board reports.

### 4G. Attestations and compliance certificates

**FR-P04-60 Certification chain.** Configurable chain (default): **Department head quarterly certificate** (list of department instances with status; signed in-app with step-up MFA, optional Aadhaar eSign/DSC) → **CCO certificate** to the Board/Audit Committee (consolidated; exceptions and remediation) → **MD/CEO certificate** where an RBI/SEBI requirement or the tenant's policy calls for it. Certificates are generated as DOCX + PDF from templates (P07 template engine), with the data snapshot hashed and frozen; edits to underlying data after signing produce a "post-certification changes" annex in the next certificate rather than altering the signed one.

**FR-P04-61 Ongoing attestations.** CONTINUOUS checkpoints produce periodic attestation instances (§4B) that can be answered in bulk per owner ("I confirm continued compliance with these 37 items; exceptions: 2"), with exceptions turned into exception records.

### 4H. Auditor columns and sampling

**FR-P04-70** Internal audit (P10) can define sampling rules (e.g., 10 % of closed High-risk instances per quarter, all late closures, all N-A claims) that assign `auditor_user_id` (column AC) to selected instances; auditors record comments (AD) and a conclusion (SATISFACTORY, OBSERVATION, EXCEPTION); observations flow to the audit findings register in P10. External auditors and supervisors read within grant (D-12) and cannot change instance data.

### 4I. Compliance score and dashboards

**FR-P04-80 Score.** Default method (configurable, transparent, shown with an "i" explanation): for a scope and period, `score = Σ(weight × status_points) / Σ(weight × max_points)` with weights HIGH 3, MEDIUM 2, LOW 1 and status points: approved on time 1.0; approved late 0.6; partially complied 0.3; open not yet due excluded; overdue 0; exception with approved remediation 0.2; not applicable excluded. Displays score, trend, and the items that most reduce it.

**FR-P04-81 Dashboards (role-based, customisable widgets; Appendix C).**
- *My work* (maker/checker): due today/this week/overdue, returned for rework, awaiting my review, evidence requests.
- *Department head*: department heatmap (instrument × month), overdue by owner, rework rate, certificates due.
- *CCO*: entity-wide score, heatmap by regulator/department/legal entity, upcoming statutory deadlines (30 days), exceptions and ageing, N-A claims, waivers, regulatory filings tracker (with P11), recent Updates impact (P05), audit observations.
- *MD/CEO, Board*: one-page compliance health (score, trend, top risks, exceptions requiring Board attention, penalties paid/avoided), drill-down to evidence.
- *Auditor*: samples, evidence completeness, late closures, changes after closure (Correction Entries).

### 4J. Reports

**FR-P04-90 Report catalogue.** Compliance status report (filters: legal entity, department, regulator, instrument, risk, period, owner); Overdue and ageing report; Upcoming deadlines (7/30/90 days); Department-wise report; Instrument-wise report (per Master Direction — what the CCO presents when RBI asks "show your compliance with the X Directions"); Exception register; N-A and waiver register; Rework and quality report; Timeliness trend; Penalty and late-fee register; Evidence completeness report; Auditor sample report; Certification status; Changes-after-closure report; Workload report (instances per owner, for resource planning). A **report builder** lets users pick filters and up to 40 columns, save templates, and schedule e-mail delivery (daily/weekly/monthly at a set time) — matching and exceeding the Lawrbit matrix-report pattern.

**FR-P04-91 Formats.** XLSX (including the owner's 30-column register format), CSV, PDF, DOCX (narrative reports via templates). Every export is logged (who, what scope, when, hash) and respects the user's ABAC scope.

**FR-P04-92 Board compliance report.** A templated DOCX/PDF with: executive summary (score, trend), compliance by regulator and instrument, overdue and exceptions with remediation, regulatory changes in the period and their implementation status (P05), filings made (P11), audit observations (P10), penalties, certifications, and an annex of instance-level status; generated as a draft, edited in Word (P07 round-trip) and approved by the CCO before it enters the Board pack (P06). AI may draft the narrative (§11).

### 4K. Owner's Excel format — register export and WORKSPACE import

**FR-P04-100 Register export.** "Export register (Excel)" produces the owner's template layout for the selected scope: rows = instances, content columns from the effective checkpoint, user columns I, J, T, W–AD populated, CompID in E; nothing is written beyond AD (NN-35). Each row's `Period` and `Instance Ref` are carried in the hidden `_LDC_System` sheet keyed by row (master X-28), the file is declared as export variant `REGISTER` in `_Template_Info`, and the content contract is unaffected (Appendix E §E.9). Dropdowns for W and AA are added in `Rough` for offline updating.

**FR-P04-101 WORKSPACE import application.** After P03 validates a WORKSPACE upload (V-16, V-17), P04 applies each row as the same action the user could take on screen (maker status + evidence references, checker decision), in the user's own name and permissions; rows the user cannot act on are rejected; each applied row emits the normal audit events. Evidence cannot be uploaded through Excel (files are attached in the app); a maker may reference an existing DMS document ID in column U.

### 4L. Calendar (R-094)

**FR-P04-110 Unified calendar.** One calendar service (`wf.calendar_items`) aggregates compliance instances (statutory and internal due dates), tasks, meetings (P06), policy reviews (P07), return deadlines and filing windows (P11), audit fieldwork (P10), training sessions (P21), POSH IC timelines (sealed — shown only to IC members, NN-13), and personal reminders. Views: Month, Week, Agenda, Timeline (Gantt by department), Heatmap (density/criticality by day). Filters: regulator, department, legal entity, risk, status, owner, type. Drag-and-drop rescheduling of *internal* dates only (statutory dates are rule-computed), with audit entry.

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

### 4N. Notifications service (NN-27)

**FR-P04-130 Separation.** `wf.notifications` stores work notifications (assignment, reminder, overdue, escalation, approval request, decision, mention, comment, direct message, calendar event, task scheduled/completed, Vidhi run finished, export ready, system security alerts such as new-device login). Regulatory content lives in `chg.updates` (P05) and is never stored as a notification; the bell icon (Notifications) and the megaphone icon (Updates) are separate, each with its own unread count.

**FR-P04-131 Channels.** In-app (real-time via WebSocket), e-mail (transactional provider; DKIM/SPF/DMARC on `in.lawdocscomply.com`), PWA web push, Microsoft Teams chat card (optional, via Graph or incoming webhook per tenant), WhatsApp Business (opt-in, critical categories only, approved templates via a BSP), SMS (opt-in, critical only, DLT-registered templates and header — TCCCPR), mobile push (when the mobile app ships). Channel availability per category is governed by P02 settings with mandatory floors.

**FR-P04-132 Preferences.** Per user and category: channel, frequency (instant, hourly digest, daily digest at chosen time, weekly), quiet hours (timezone-aware; escalations for owned overdue High-risk items bypass quiet hours only for in-app and e-mail), and "follow"/"mute" per record. **Mandatory floors** (tenant cannot disable): assignment of a High-risk instance, overdue of an owned instance, escalation to the user, approval request older than SLA, security alerts. Digests group by due date and record, with one-click actions (approve Low-risk, open, snooze).

**FR-P04-133 Messaging.** Comments with @mentions on any record; direct messages between users in a tenant; threads per instance. Messages are tenant data, retained per retention settings, exportable (P19), and visible to auditors within grant. Delivery-team messaging with clients uses the same service in the delivery console (P22).

### 4O. Fewer-click design patterns (R-023, R-028)

- **My Day**: the default landing page for makers and checkers — today's and overdue items with inline evidence drop zones and a single Submit.
- **Smart defaults**: date of compliance = today; maker status inferred from evidence type (e.g., acknowledgement PDF → COMPLIED) — suggestion only; checker defaulted by rule.
- **Evidence reuse**: "Use the same evidence as last period" for CONTINUOUS/attestation items, with a mandatory freshness check (document date within period).
- **Bulk**: multi-select submit, reassign (approval stays sequential except `bulk_approvable` items, NN-46), set internal dates, add watchers, export; long operations run in the background with a results summary ("287 succeeded, 3 failed — download error report").
- **Command palette** (`Ctrl/Cmd+K`): "submit", "assign to", "open instrument", "export overdue".
- **Comment templates** for frequent checker feedback.
- **Auto-close on ecosystem proof**: when a trusted integration event proves completion (e.g., a Finbyx return acknowledgement), the instance moves to UNDER_REVIEW with evidence attached; the checker still approves (no auto-approval for regulatory items).

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
| SCR-CMP-02 | Work Inbox | Inbox (top bar) | all | Unified actionable queue; filters; bulk actions; snooze; keyboard |
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

UX: role-default landing pages; every status chip uses text + icon + colour (NN-21); "i" help keys `cmp.status.<code>`, `cmp.freq.<code>`, `cmp.col.<letter>`; empty states guide setup ("No makers mapped for 'Risk Management' — map now"); command palette; keyboard shortcuts (`A` approve, `R` reject with comment focus, `N` next); undo for 10 s on bulk actions where reversible; responsive layouts for tablet/phone (PWA) for review and approval on the go.

---

## 7. Backend design

### 7.1 Modules
`cmp` (assignments, instances, evidence links, events, exceptions, certificates, score), `wf` (workflow engine, tasks, approvals, Work Inbox, notifications, messages, calendar items, external sync), with `cnt`, `cfg`, `dms`, `ai`, `hr` (leave, org chart), `int` (calendar connectors, ecosystem events), `rpt` (dashboards, report builder).

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

### 7.3 APIs

`GET /cmp/instances` (filters, views) · `GET /cmp/instances/{id}` · `POST /cmp/instances/{id}/evidence` · `POST /cmp/instances/{id}/submit` · `POST /cmp/instances/{id}/review` (`APPROVE|REJECT|REALLOCATE`) · `POST /cmp/instances/bulk` · `POST /cmp/events` · `POST /cmp/events/{id}/confirm|correct|void` · `GET/POST /cmp/exceptions` · `POST /cmp/certificates/generate` · `POST /cmp/certificates/{id}/sign` · `GET /cmp/register/export?format=xlsx|pdf` · `GET /wf/inbox` · `GET/POST /wf/tasks` · `POST /wf/tasks/{id}/assign` · `GET/POST /wf/schedules` · `GET /wf/notifications` · `PUT /wf/notification-prefs` · `GET /wf/calendar?from&to` · `POST /wf/calendar/connections/{provider}` · `GET /ics/{token}.ics` (public, token-authenticated, rate-limited) · `GET /rpt/compliance/score`.

### 7.4 Domain events
`in.lawdocscomply.cmp.InstanceCreated.v1`, `…InstanceSubmitted.v1`, `…InstanceReviewed.v1`, `…InstanceOverdue.v1`, `…InstanceEscalated.v1`, `…EvidenceSubmitted.v1` (Ecosystem name `EvidenceSubmitted`), `…ComplianceEventRecorded.v1`, `…ComplianceIssueRaised.v1` (Ecosystem name), `…ExceptionClosed.v1`, `…CertificateSigned.v1`, `…wf.TaskAssigned.v1`, `…wf.TaskCompleted.v1`, `…wf.ScheduleRunCompleted.v1`, `…wf.NotificationDelivered.v1` (internal), `…wf.CalendarSyncFailed.v1`.
Consumed: `cnt.ObligationPublished`, `cnt.InstrumentAdopted/Removed`, `chg.DueDateExtensionPublished` (P05), `hr.LeaveApproved`, `hr.EmployeeExited`, `gov.DirectorAppointed`, `dpc.IncidentRecorded`, Ecosystem `ReturnStatusUpdated`, `ControlTestResultPublished`, `LitigationCaseOpened`, `OrderRecorded`.

### 7.5 Jobs / Temporal
`ScheduleGenerator` (nightly + on change; idempotent per assignment/period), `ReminderLadder` (per instance timers), `OverdueSweep` (hourly), `DelegationResolver` (on leave events), `CertificateSnapshot`, `ReportScheduler`, `DigestBuilder` (per user schedule, timezone-aware), `CalendarOutbound` (queue with backoff), `IcsBuilder` (cached per user, invalidated on change), `VidhiTaskDispatcher` (to P17), `ScheduledTaskRunner`.

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
    Then the workbook has the owner's row-1 and row-2 headers, columns A–AD populated per mapping, plus Period and Instance Ref after AD
    And re-importing it in WORKSPACE mode with 5 maker status changes applies only rows the user may act on
```
NN tests: `NN-01_instance_list_scoped`, `NN-03_release_spares_closed_instances`, `NN-05_maker_checker_distinct`, `NN-13_sealed_items_minimal_in_calendar`, `NN-14_vidhi_cannot_approve_instance`, `NN-21_status_chips_accessible`, `NN-27_updates_not_in_notifications`, `NN-29_cancelled_instances_retained`.

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

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-33, NN-46; X-11, X-24 (LDC dates authoritative over synced calendars), X-26 (this phase owns `packages/workflow`, `notify`, `calendar`, SCR-RPT-01, SCR-WF-00 Work Inbox, SCR-CORE-21 global search; SCR-WF-01 remains the Calendar)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

