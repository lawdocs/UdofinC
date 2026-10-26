# Appendix A — Workflows and State Machines (binding)

> LawDocsComply Build Prompt Pack v1.1 · 25 October 2026 (v1.0 of the same date) · Owner: P02 (definitions), P04 (engine). Every module that stores a lifecycle uses the canonical machine defined here; phase files may add sub-states and tenant-configurable labels (P02 §4G) but may not add transitions that the canonical graph forbids, remove a guard marked **(L)**, or pause a statutory clock.

> **v1.2 changes (25 October 2026)**
> - New machines A.46–A.51 *(v1.2)*: conversation thread with append-only message sub-machine (NN-59), explanation request, assignment acceptance and owner-of-record invariant with holding-state projection (NN-60), RAG computation as a derived value with pseudo-code (NN-58, D-54), compliance-list export job (extends A.19), star/watch/collection
> - Event index extended with the lifecycle events of A.46–A.51

> **v1.1 changes (25 October 2026)**
> - Universal guards G-BATCH (undo windows, NN-49) and G-REGION (cells, NN-24); G-AI extended for autonomy levels and NN-47
> - Three-date model (A.0.5A; NN-48): timeliness from act date
> - New machines A.26–A.35: change batch, jurisdiction pack (DRAFT→PILOT→PUBLISHED→DEPRECATED), incoming notice and legal matter, contract, ESG disclosure and CSR cycles, report run, agent mission and delegation, applicability challenge, tracker import, region migration

---

## A.0 Conventions

**A.0.1 Notation.** Each machine lists states, then a transition table: *From · Event · Guard · To · Side effects (events, timers, notifications)*. `*` = any non-terminal state. Terminal states are in **bold**. Event names are CloudEvents types without the `in.lawdocscomply.` prefix (Appendix B §B.5).

**A.0.2 Engine.** Machines are implemented as explicit transition tables in `packages/state` (TypeScript), persisted with `status`, `status_version` (optimistic lock) and a `state_history` row per transition (actor, on-behalf-of, reason, at, from, to, guard results). Long-running timers and multi-step processes run as Temporal workflows (named in each section). A transition is only accepted through the owning module's API, which re-runs guards server-side (UI hiding is not a control).

**A.0.3 Universal guards (L).**

| Guard | Rule |
|---|---|
| G-SOD | Actor of a check/approve transition ≠ actor of the make/submit transition on the same object version (NN-05). Delegates inherit the delegator's exclusion. |
| G-AUTH | Actor holds the permission for the transition in the object's scope (legal entity, department, function, assignment) — Appendix D. |
| G-STEPUP | Approve, sign, publish, override, export of sensitive scope and break-glass require AAL2 step-up within 10 minutes. |
| G-EVID | Transitions into `submitted_for_review`, `complied`, `remediation_submitted`, `approved` (policy) require the evidence set defined by the content or template, unless an exception is recorded. |
| G-AI | `svc_vidhi` and every Vidhi role agent may perform only `draft`, `suggest`, `extract`, `summarise`, `classify` transitions — and, at autonomy L3/L4, pre-approved internal actions listed for the skill (create reminder, assign within rule, compile pack) as a reversible change batch; never approve, sign, file, pay, publish, close, change access, or set a compliance status, risk rating, materiality or audit conclusion (NN-04, NN-14, NN-47, NN-50) *(v1.1)*. |
| G-SEAL | Sealed objects (POSH, whistle-blower, complainant identity) transition only by members of the sealed audience (NN-13). |
| G-CLOCK | Statutory and regulator clocks attached to an object never pause, never move later by a workflow transition, and are only changed by a G rule-pack change or a recorded regulator extension (with reference). |
| G-HIST | No transition deletes history; corrections use Correction Entries (A.5, NN-02). |
| G-BATCH *(v1.1)* | A transition performed in bulk or by import belongs to a change batch with an undo window (A.26, NN-49); the batch id is recorded on each `state_history` row. |
| G-REGION *(v1.1)* | A transition never moves data to another region cell; cross-cell effects are aggregates only (NN-24 amended). |

**A.0.4 Clocks.** A clock is `{clock_type, starts_at, due_at, basis (rule-pack version + citation), owner, warn_offsets[], escalation_ladder_id, status (running, met, breached, waived_by_regulator)}`. Clock state (`green`, `amber`, `red`, `breached`) is server-computed only. Owned statutory clocks: info at the first warn offset, task at the second, escalation at the third (defaults T-15, T-7, T-1 days; tenant `raise_only`). Unowned statutory clocks block closure of the parent object and raise an alert.

**A.0.5 Canonical status set for compliance-type objects (L, referenced by P02 FR-P02-40).** `not_started`, `in_progress`, `in_progress_interim`, `waiting`, `submitted_for_review`, `returned`, `complied`, `complied_late`, `partially_complied`, `not_complied`, `not_applicable`, `exempted`, `deferred_by_regulator`, `withdrawn`. `overdue` is a **derived flag** (`due_at < now ∧ status ∉ terminal`), never a stored state.

**A.0.5A Three dates (NN-48) *(v1.1)*.** Every compliance-type object records `act_date` (when the obligation was actually performed or filed — from the acknowledgement where one exists), `evidence_date` and `approval_date`. Timeliness (`complied` vs `complied_late`) is computed from `act_date` against the statutory `due_at` (+ regulator grace); internal SLA performance uses `approval_date` against the internal target. An `act_date` earlier than the submission date requires an evidence item showing it.

**A.0.6 Events.** Every transition emits `<Module><Object>StatusChanged.v1` with `{object_id, tenant_id, from, to, actor_ref, at, reason_code}` plus specific events listed below. Ecosystem-facing events reuse Ecosystem Spec v1.1 names (`ObligationPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `ControlTestResultPublished`, `PolicyAttested`, `ReturnStatusUpdated`, `GrievanceRaised`).

---

## A.1 Compliance instance (`cmp.compliance_instances`)

A compliance instance is one occurrence of an obligation for one legal entity and period (e.g., "NBFC-ML Quarterly return X for Q2 FY26-27", "Board meeting gap check", "Policy annual review"). Generated by `ComplianceScheduleWorkflow` from the tenant's applicable obligations (P03 content + tenant overlay + P02 due-date rule pack pinned at generation, NN-03, NN-07).

**States:** `scheduled` (future period; not yet open), `not_started`, `in_progress`, `in_progress_interim`, `waiting`, `submitted_for_review`, `returned`, `checked` (checker accepted; transient when no auditor step), `auditor_review` (optional sample), **`complied`**, **`complied_late`**, **`partially_complied`**, **`not_complied`**, `na_requested`, **`not_applicable`**, **`exempted`**, **`deferred_by_regulator`**, **`withdrawn`**. Terminal states can be reopened only by A.5 Correction Entry (platform) or by `reopen` with checker approval (tenant) within the period's reporting window; reopening is recorded, never overwrites.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| scheduled | window_opens (timer: `due_at − open_lead_days`) | — | not_started | Task to maker; calendar entry; `ComplianceInstanceOpened` |
| not_started | start | G-AUTH (maker or assignee) | in_progress | — |
| not_started / in_progress | set_waiting | reason, party, expected_by (P02 §4G) | waiting | Chase workflow; internal SLA may pause; statutory clock runs (G-CLOCK) |
| waiting | resume / response_received | — | in_progress | Chase stopped |
| in_progress | record_interim | interim evidence type present | in_progress_interim | Next-check date; not counted as complied |
| in_progress_interim | resume | — | in_progress | — |
| in_progress / in_progress_interim | submit | G-EVID; mandatory fields; maker attestation tick ("I confirm the evidence is complete and true") | submitted_for_review | Approval item to checker pool; `EvidenceSubmitted` |
| submitted_for_review | return | G-SOD; reason code + comment | returned | Notification to maker; rework SLA |
| returned | resubmit | G-EVID | submitted_for_review | Return count +1 (analytics) |
| submitted_for_review | check_accept | G-SOD, G-AUTH, G-STEPUP for High risk | checked | `ControlTestResultPublished` (result = pass) |
| checked | auto (auditor step not configured or not sampled) | — | complied or complied_late | Status by comparing `act_date` with `due_at` (+ regulator grace if any) — NN-48 *(v1.1)* |
| checked | sampled_for_audit | sampling rule (P10) | auditor_review | Auditor task |
| auditor_review | audit_ok | auditor ≠ maker/checker | complied / complied_late | — |
| auditor_review | audit_exception | reason | in_progress | `ComplianceIssueRaised` (source AUDIT) |
| submitted_for_review | check_partial | checker records which sub-items remain | partially_complied | Follow-up instance auto-created for remainder |
| * (non-terminal) | due_passed (timer at `due_at + grace`) with no submission | — | stays; `overdue` flag set | Escalation L1→L3 per ladder; Notification to dept head and CCO; savings ledger records "risk exposure" (P20) |
| * (non-terminal) | period_closed (timer: end of reporting window) | not submitted | not_complied | `ComplianceIssueRaised` (source TEST); board-report flag |
| not_started / in_progress | request_na | reason code from NA list (P02 FR-P02-48) | na_requested | Approval item to checker |
| na_requested | approve_na | G-SOD; for instruments marked "NA requires CCO" → `ten_cco` | not_applicable | Applicability exception logged; future instances suppressed only if "NA for all periods" selected (then tenant overlay change, A.7) |
| na_requested | reject_na | reason | prior state | — |
| * | regulator_exemption_recorded | exemption reference + document | exempted | — |
| * | regulator_extension_recorded | circular/letter reference | same state with new due_at | Clock `due_at` changed by recorded regulator extension only (G-CLOCK) |
| * | regulator_deferral_recorded | reference | deferred_by_regulator | — |
| * (non-terminal) | instrument_repealed (from P05 content release) | publisher approved repeal; propagation mode | withdrawn | History preserved (NN-29) |
| complied / complied_late / not_complied / partially_complied | reopen | checker approval; within window; reason | in_progress | Original completion retained in history |

**Timers (Temporal `ComplianceInstanceWorkflow`):** open window, reminder offsets (T-n), due, grace end, period close, auditor sampling cut-off. **Derived metrics:** on-time %, late %, rework rate, average days to check, waiting time by party.

---

## A.2 Evidence item (`dms.evidence_items`)

**States:** `uploading`, `scanning`, **`quarantined`**, `available`, `processing` (OCR / type copy / translation / classification), `linked`, `under_review`, `accepted`, `rejected`, **`superseded`**, `on_legal_hold` (overlay flag).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| uploading | upload_complete | checksum matches; size ≤ limit; type allowed | scanning | SHA-256 recorded |
| scanning | clean | AV + file-type sniff pass | available | — |
| scanning | infected / disallowed | — | quarantined | Security alert; uploader notified |
| available | process (auto) | OCR/translation enabled | processing | AI extraction marked machine-generated |
| processing | done | — | available | Type copy stored as separate version (original untouched) |
| available | link(object) | G-AUTH on target | linked | Evidence chain entry |
| linked | parent_submitted | — | under_review | — |
| under_review | accept | via parent check (A.1) | accepted | Object Lock WORM retention applied (NN-09) |
| under_review | reject | reason | rejected | Maker task to replace |
| accepted / rejected | new_version_uploaded | — | superseded (old) | New item starts at `uploading`; version chain kept |
| * | legal_hold_on/off | `ten_cco` or platform legal | flag | Deletion blocked while on hold |

Accepted evidence is immutable: corrections attach a new version and, if needed, a Correction Entry on the parent; the original stays retrievable (NN-02, NN-09).

---

## A.3 Task (`wf.tasks`)

Generic task for any module, including tasks assigned to Vidhi AI and scheduled/recurring tasks (R-095).

**States:** `scheduled` (future start or recurrence placeholder), `open`, `in_progress`, `waiting`, `ai_queued`, `ai_running`, `ai_draft_ready`, `human_review`, **`done`**, **`cancelled`**, **`expired`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| scheduled | start_time_reached | — | open | Notification; calendar |
| open | accept / start | assignee or pool member | in_progress | Atomic claim for pool tasks (`SKIP LOCKED`) |
| open / in_progress | set_waiting | reason, party | waiting | Chase policy |
| waiting | resume | — | in_progress | — |
| open | assign_to_vidhi | creator holds the permissions the task needs; task kind is AI-eligible (draft, summarise, extract, prepare report, compile data) | ai_queued | `svc_vidhi` acts on behalf of creator (D-14) |
| ai_queued | run | budget and rate limits OK | ai_running | AI log entry |
| ai_running | draft_produced | — | ai_draft_ready | Output stored as draft, labelled AI-generated |
| ai_running | failed | — | open (assigned back to creator) | Error explained |
| ai_draft_ready | review | human reviewer (creator or named) | human_review | — |
| human_review | accept | G-AI (human performs completion) | done | Draft promoted to owning object's draft state (never published) |
| human_review | request_rework_ai | instruction text | ai_queued | — |
| in_progress | complete | completion fields; evidence if required | done | `TaskCompleted`; recurring → next instance `scheduled` |
| * | cancel | creator, assigner or dept head; reason | cancelled | — |
| open / in_progress | due_passed | — | same + overdue flag | Escalation ladder |
| scheduled (one-off) | expiry_without_start (optional) | `expires_at` set | expired | — |

**Hierarchy rule (R-095):** a user may assign tasks to users at or below their position in the tenant's reporting line (HRMS) or within a department where they are head/deputy; peers may "request" (creates a task in `open` that the assignee may decline with reason). Tenant may relax to "anyone can assign anyone" (T, `wf.tasks.assignment_policy`).

**Recurrence:** RRULE (RFC 5545) with time zone; skip/shift on holidays per business calendar; stop condition (`until`, `count`, or "until instrument withdrawn"). Scheduled AI tasks (e.g., "Every Monday 09:00 prepare a compliance status summary for the CCO") run as `ai_queued` instances with preview of first 3 occurrences before activation.

---

## A.4 Approval request (generic; `wf.approval_requests` and `core.config_change_requests`)

**States:** `draft`, `submitted`, `in_review`, **`approved`**, **`rejected`**, `changes_requested`, **`withdrawn`**, **`expired`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| draft | submit | validators; summary; attachments | submitted | Inbox items to eligible approvers (serial/parallel/quorum per workflow definition) |
| submitted | open | eligible approver | in_review | — |
| in_review | approve (step) | G-SOD, G-AUTH, G-STEPUP if configured | in_review (next step) or approved | Step record |
| in_review | reject | reason ≥ 20 chars | rejected | Maker notified |
| in_review | request_changes | comment | changes_requested | — |
| changes_requested | resubmit | — | submitted | Prior approvals reset if payload digest changed |
| draft / submitted / in_review | withdraw | maker | withdrawn | — |
| submitted / in_review | timeout (`expiry_days`) | — | expired | Maker notified |
| in_review | sla_breach | — | in_review | Escalation; delegate suggestion |

**WYSIWYS:** the approver sees the exact payload digest; any payload change after an approval step invalidates the step. **Bulk approval:** not allowed for G-legal changes, money, privileges, sensitive exports, High-risk compliance checks; allowed for sources flagged `bulk_approvable` (leave, attendance regularisation, Low-risk T content), each item still evaluated individually (Appendix C §C.5.2).

---

## A.5 Correction Entry (`core.correction_entries`; D-02, R-068, R-071, R-074)

**States:** `requested`, `in_review`, `approved`, `applied`, **`rejected`**, `applied_emergency`, **`ratified`**, **`auto_reverted`**, `tenant_notified` (flag), **`closed`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | request | `plt_super_admin` (or tenant `ten_admin` for tenant-scope corrections of own data); target object, fields, new value, `effective_at`, reason code, reason ≥ 20 chars, evidence ref | requested | Inbox to approvers |
| requested | open | approver ≠ requester; role `plt_super_admin` or `plt_security_officer` (platform) / `ten_cco` (tenant) | in_review | — |
| in_review | approve | G-STEPUP both | approved | — |
| approved | apply (auto) | target not on legal hold (or hold owner consents) | applied | Ledger `CorrectionEntryApplied` (old value sealed, new value, effective_at, recorded_at); read models updated; "Corrected" chip |
| applied | notify (auto) | — | closed + tenant_notified | Notification to `ten_admin` (and `ten_cco` for compliance records); entry visible on SCR-CFG-28 |
| in_review | reject | reason | rejected | — |
| — | emergency_apply | `plt_super_admin` + incident ID; reversible change only | applied_emergency | P1 alert to `plt_security_officer` |
| applied_emergency | ratify (≤ 24 h) | second approver | ratified → closed | Tenant notified |
| applied_emergency | 24 h elapse | — | auto_reverted | Reverse Correction Entry generated automatically |

Correctable targets: tenant master data, compliance instance dates/status/evidence links, document version pointers, settings, entitlements, trial dates, invoices (via OH8 credit note only — P20, X-02), audit-trail **annotations** (a note attached to a ledger event; the event itself is immutable). Never correctable: ledger events' content or order, sealed content, NN tests.

---

## A.6 Platform content release (instrument version and base question bank; P03/P05)

**States:** `ingested`, `extracted`, `drafting` (AI question drafting or Excel import), `maker_review`, `checker_review`, `approved`, `scheduled`, **`published`**, `superseded`, **`repealed`**, **`rejected`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | ingest | source file, URL, retrieval date, SHA-256 | ingested | — |
| ingested | extract | OCR confidence recorded per page | extracted | Clause tree built |
| extracted | draft_questions (AI) / import_excel | template family matches (Appendix E) | drafting | AI output flagged; Excel validation report |
| drafting | submit | every row has clause ref, frequency, department code, evidence, control activity; no blank system columns violated | maker_review | — |
| maker_review | send_to_checker | maker attests | checker_review | — |
| checker_review | approve | G-SOD (checker ≠ maker), G-STEPUP | approved | — |
| checker_review | return | comments per row | maker_review | — |
| approved | schedule | effective date; propagation mode; "what changed" summary (if amendment) | scheduled | Impact analysis (affected tenants, overlays, open instances) |
| scheduled | publish (timer or immediate with `plt_content_publisher`) | publisher ≠ maker | published | `ObligationPublished`; Regulatory Update item (P05) |
| published | newer_version_published | — | superseded | Pinned instances unaffected; tenants offered upgrade diff |
| published | repeal_published | repeal instrument cited | repealed | Open instances → `withdrawn` per propagation mode; history kept |
| * pre-publish | reject | reason | rejected | — |

AI-drafted questions can never skip `maker_review` and `checker_review` (NN-04). Excel uploads by super admin follow the same path; tenant-admin AI/Excel authoring follows A.7.

---

## A.7 Tenant overlay (tenant changes to base content; R-017, R-085, R-087)

Covers: edited question/actionable text, added questions, changed department/frequency/evidence, tenant-only instruments (tenant-uploaded master direction → AI-drafted questions), applicability decisions (instrument added/removed).

**States:** `draft`, `submitted`, **`active`**, `conflict` (base content changed under an active overlay), **`retired`**, **`rejected`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | create (edit row / add row / upload instrument / select or deselect instrument) | `ten_admin` or delegated `ten_cco` | draft | Base version reference stored |
| draft | submit | validation per Appendix E; reason | submitted | Approval item to tenant checker (`ten_cco` or delegate) |
| submitted | approve | G-SOD | active | Future instances use overlay; audit "Tenant change" (who, what, why, old vs new text) |
| submitted | reject | reason | rejected | — |
| active | base_updated (P05 publishes a new base version touching the same obligation) | — | conflict | Side-by-side diff (base old → base new vs overlay); task to `ten_cco`; overlay **remains in force** until resolved (NN-03) |
| conflict | keep_overlay / adopt_base / merge | decision + reason | active (new overlay version) or retired | — |
| active | retire | reason | retired | Base content resumes for future instances |

Deselecting an instrument (removing from the tenant's applicable list) requires confirmation that lists open instances; open instances move to `withdrawn` only if the admin selects that; completed history is preserved (NN-29).

---

## A.8 Rule-pack version (P02)

States `draft → review → approved → scheduled → active → superseded → retired`, side exits `rejected`, `withdrawn`. Guards: validators, citations, golden suite, fallback, impact report, maker ≠ checker (≠ publisher for permissive). Detailed table: P02 §5.2–5.3. Events: `RulePackVersionSubmitted`, `RulePackVersionActivated`, `RulePackRetired`, `RulePackReviewDue`, `FallbackActivated`.

---

## A.9 Regulatory update (P05; `chg.regulatory_updates`)

**States:** `detected`, `duplicate` (terminal), `triage`, `non_actionable` (terminal after publication as FYI), `analysis` (AI summary, diff, candidate obligations), `content_review`, `checker_review`, `published_update`, `content_change_in_progress` (links to A.6), **`closed`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | source_item_found (20:00 IST scan or intraday feed) | hash not seen | detected | Archived copy, SHA-256 |
| detected | dedupe_match | — | duplicate | Linked to original |
| detected | classify | content maker | triage | Class: new instrument, amendment, corrigendum, repeal, FAQ/clarification, consultation, enforcement/penalty order, press release, news |
| triage | mark_non_actionable | reason | non_actionable → (publish FYI optional) | — |
| triage | analyse | — | analysis | AI summary, clause diff, affected entity families, effective dates — all marked machine-generated |
| analysis | submit | maker reviewed and edited | content_review → checker_review | — |
| checker_review | approve_update | G-SOD | published_update | Updates feed item to affected tenants: "what changed / why it matters / what to do"; push/email/calendar per preference; `RegulatoryUpdatePublished` |
| published_update | content_change_needed | — | content_change_in_progress | Creates A.6 release (new questions/actionables) |
| content_change_in_progress | release_published | — | closed | Tenants see "Previous actionable → New actionable" diff on affected obligations |
| published_update | no_content_change | — | closed | — |

**Tenant side (per tenant `chg.tenant_update_reviews`):** `new → acknowledged → impact_assessed (applicable / not applicable with reason) → actions_created (tasks, policy reviews, committee agenda items) → closed`. Unacknowledged critical updates escalate to `ten_cco` after 2 working days (T).

---

## A.10 Policy version (P07; `pol.policy_versions`)

**States:** `draft`, `owner_review`, `compliance_review`, `committee_review`, `board_approval_pending`, `approved`, `published`, `acknowledgement_open`, `in_force`, `review_due`, **`superseded`**, **`retired`**, `returned`.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | create (from model template, from previous version, or Vidhi draft with track changes) | owner assigned | draft | DOCX with tracked changes vs base (P07) |
| draft | submit | owner attests | owner_review → compliance_review | — |
| compliance_review | clear | `ten_cco` ≠ drafter | committee_review (if policy requires a committee) or board_approval_pending | Agenda item proposed in P06 meeting |
| committee_review | recommend | committee meeting minutes reference | board_approval_pending | — |
| board_approval_pending | board_approved | board meeting ID + resolution number + **approved signed PDF uploaded** | approved | Approval date recorded |
| any review | return | comments | returned → draft | — |
| approved | publish | effective date | published | Previous version → superseded |
| published | open_acknowledgements (if required) | audience | acknowledgement_open | Attestation tasks; `PolicyAttested` per user |
| acknowledgement_open | threshold_met / window_end | — | in_force | Non-acknowledgers escalated |
| in_force / published | next_review_date − N days | — | review_due | Owner task; calendar |
| review_due | reviewed_no_change | approver per policy (board/committee/CCO as configured) | in_force (new next_review_date) | — |
| review_due | revise | — | (new version) draft | — |
| * | retire | approver; reason | retired | — |

Guard (L): a policy marked "Board-approved required" (regulatory policies — e.g., RBI-mandated policies for NBFCs) cannot reach `approved` without a board meeting reference and the uploaded approved copy.

---

## A.11 Meeting (P06; board, committee, general meeting, co-operative general body)

**States:** `planned`, `notice_drafting`, `notice_issued`, `agenda_circulated`, `convened`, `adjourned`, **`concluded`**, **`cancelled`**, **`invalid_no_quorum`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | plan | meeting type, body, date/time, mode (physical, VC, hybrid) | planned | Calendar holds for members (CALENDAR_PORT); statutory checks (gap ≤ 120 days for board, s.173(1)) |
| planned | draft_notice | — | notice_drafting | Vidhi drafts notice and agenda from template + open agenda queue |
| notice_drafting | issue_notice | approver (CS/Chair); notice period rule satisfied (board ≥ 7 days, s.173(3); shorter notice only with conditions recorded); recipients = all members entitled | notice_issued | Delivery evidence (email, portal) per member |
| notice_issued | circulate_agenda_papers | SS-1 timelines (agenda and notes at least 7 days before, unless shorter-notice items) [VERIFY para] | agenda_circulated | Board pack (secure, watermarked) |
| agenda_circulated | convene | quorum present (rule pack by body: board — one-third or two directors, s.174; committees per charter; co-op per by-laws) | convened | Attendance register; VC compliance record |
| agenda_circulated | quorum_failed | — | adjourned (rule: same day next week or as articles) or invalid_no_quorum | Adjournment notice |
| convened | conclude | — | concluded | Minutes workflow (A.12) starts |
| planned / notice_issued / agenda_circulated | cancel | reason | cancelled | Members notified |

---

## A.12 Minutes (P06; SS-1/SS-2 aligned)

**States:** `drafting`, `internal_review`, `draft_circulated`, `comments_window`, `finalised`, `signed`, **`entered_in_minute_book`**, `correction_pending` (via A.5 only).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | meeting_concluded | — | drafting | Vidhi drafts from agenda, attendance, decisions captured live, transcript (if recording consented) |
| drafting | submit_for_review | CS/secretary | internal_review | — |
| internal_review | circulate_draft | within draft-circulation clock (default 15 days of meeting; G rule pack `IN.icsi.ss1`) | draft_circulated | Clock: comments window |
| draft_circulated | comments_window_end (default 7 days) | — | comments_window → finalised (after Chair incorporates comments) | Comment log retained |
| finalised | sign | Chair of that meeting or next meeting (DSC / eSign / wet-ink scan) | signed | Signed PDF hash |
| signed | enter_in_book | within entry clock (default 30 days of conclusion) | entered_in_minute_book | Page numbering, locked PDF, WORM (NN-09) |
| entered | correction | A.5 only (alteration after signing not permitted except by a subsequent resolution noted in later minutes) | correction_pending → entered | — |

Statutory clocks (circulation, entry) are owned by the CS; breach is a compliance issue in A.1.

---

## A.13 Audit finding (P10; internal, RBIA, IS, secretarial, concurrent, statutory-auditor observations)

**States:** `draft`, `discussed_with_auditee`, `management_response`, `agreed_action`, `in_remediation`, `remediation_submitted`, `validation`, **`closed`**, `risk_accepted`, `reopened`, **`withdrawn`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | raise | auditor; severity (Critical/High/Medium/Low); criteria, condition, cause, effect | draft | — |
| draft | share_with_auditee | audit lead review | discussed_with_auditee | Auditee task with response clock (default 15 days, T) |
| discussed_with_auditee | respond | auditee head | management_response | — |
| management_response | agree_action | owner, target date | agreed_action → in_remediation | `ComplianceIssueRaised` (source AUDIT) |
| in_remediation | submit_remediation | evidence | remediation_submitted | — |
| remediation_submitted | validate_ok | auditor ≠ remediator | closed | — |
| remediation_submitted | validate_fail | reason | in_remediation | — |
| management_response / in_remediation | accept_risk | approver above owner (Audit Committee for High/Critical); expiry ≤ 12 months | risk_accepted | Expiry timer → reopened |
| closed | recurrence_found | — | reopened → in_remediation | Repeat-finding flag |
| draft | withdraw | audit lead | withdrawn | — |

Overdue remediation escalates to the Audit Committee agenda (P06) per ladder.

---

## A.14 Risk issue and action (P08)

Risk register entries are versioned assessments (`erm.risk_assessments`: `draft → submitted → approved → superseded`); issues and actions follow:

**Issue states:** `identified`, `assessed`, `action_planned`, `in_progress`, **`resolved`**, `accepted` (risk acceptance with expiry), `escalated`, **`closed`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | identify (manual, KRI breach, incident, loss event, audit finding, control failure) | — | identified | Link to risk; `RiskIssueRaised` |
| identified | assess | risk owner; inherent/residual rating | assessed | — |
| assessed | plan_action | owner, target date | action_planned → in_progress | — |
| in_progress | complete | evidence | resolved → (validation by risk function) closed | — |
| assessed / in_progress | accept | approver per appetite matrix (CRO / Risk Management Committee for above-appetite) | accepted | Expiry timer |
| * | breach_of_appetite | KRI red or rating above appetite | escalated | Agenda item for RMC; CRO dashboard alert |

---

## A.15 Return run (P11; Return Studio; D-05)

**States:** `scheduled`, `data_requested`, `data_received`, `prepared`, `validation_failed`, `validated`, `reviewed`, `approved`, `exported`, `submitted` (human upload recorded), `acknowledged`, **`closed`**, `rejected_by_portal`, `revision_required`, **`superseded`** (by revised run).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| scheduled | period_end (+ data lead) | — | data_requested | Requests to Finbyx/Udofin (events per Ecosystem Spec §6.18), Tally/Excel upload tasks |
| data_requested | data_complete | all sources present or marked N/A with reason | data_received | Data lineage snapshot hash |
| data_received | prepare | returns-kernel version pinned | prepared | Cell map applied |
| prepared | validate | kernel validations + cross-return reconciliations | validated / validation_failed | Error list per cell |
| validation_failed | fix_and_revalidate | — | prepared | — |
| validated | review | preparer ≠ reviewer | reviewed | — |
| reviewed | approve | authorised signatory per return (G-STEPUP) | approved | — |
| approved | export | — | exported | Upload-ready file(s) (XBRL/XML/CSV/XLSX per portal) with hash |
| exported | record_submission | human uploads to portal; uploader, timestamp, portal reference (D-13) | submitted | `ReturnStatusUpdated` |
| submitted | record_ack | acknowledgement file/screenshot | acknowledged → closed | Compliance instance (A.1) moves to complied/complied_late |
| submitted | portal_rejection | rejection file | rejected_by_portal → prepared | — |
| closed | revision_needed | reason (RBI query, error) | revision_required → new run (old → superseded) | Revision reason recorded |

For Finbyx clients the run consumes Finbyx `return_run` packages: states `data_requested → data_received` are replaced by `package_received` (hash verified) and preparation is skipped.

---

## A.16 Grievance and support ticket (P14)

Two linked machines: support ticket (L1) and grievance (regulated complaint).

**Support ticket:** `new → triaged → in_progress → waiting_customer → resolved → closed`; `reopened`; `converted_to_grievance`. A ticket is converted to a grievance when the customer expresses dissatisfaction with a product/service of the regulated entity per the tenant's configured definition (regulator-aligned), or on customer request.

**Grievance states:** `received`, `acknowledged`, `assigned`, `under_investigation`, `resolution_proposed`, `final_reply_sent`, `escalated_level2` (GRO / Nodal), `io_review` (Internal Ombudsman, where the RE is required to have one and the complaint is proposed to be rejected wholly or partly), **`closed_resolved`**, **`closed_rejected`**, `customer_appealed`, `external_forum` (RBI Ombudsman / SEBI SCORES / IRDAI Bima Bharosa / IFSCA / Registrar), **`closed_external_outcome`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | receive (web form on client site, email, phone log, branch, Finbyx/Udofin `GrievanceRaised`) | — | received | Grievance ID; clock starts (G rule pack per regulator) |
| received | acknowledge | within ack clock (default same/next working day) | acknowledged | Ack to complainant with ID and escalation path (GRO details) |
| acknowledged | assign | routing rules | assigned → under_investigation | — |
| under_investigation | propose_resolution | — | resolution_proposed | — |
| resolution_proposed | approve_reply | reviewer (GRO for level 2) | final_reply_sent | Reply includes external-forum rights text (NN-31) |
| resolution_proposed | propose_reject (full/part) | RE subject to Internal Ombudsman requirement | io_review | IO decision clock |
| io_review | io_decision | IO ≠ handler | final_reply_sent | IO's view recorded |
| final_reply_sent | customer_satisfied / silence period | — | closed_resolved / closed_rejected | Rating request |
| final_reply_sent / any open after reply window | customer_escalates | — | escalated_level2 | — |
| * | external_complaint_recorded | external reference | external_forum | Tasks to respond to forum within its timelines |
| external_forum | outcome_recorded | — | closed_external_outcome | Compliance with award tracked as A.1 instance |

Clocks (G, L floors): acknowledgement, final reply (30 days floor under RB-IOS 2026 for RBI REs before complainant may approach the Ombudsman [VERIFY clause]), IO turnaround, regulator response windows. Complainant identity sealed (NN-13).

---

## A.17 Subscription and trial (P20)

**States:** `lead` (health check / account created), `trial_active`, `trial_extended`, `trial_expired`, `active`, `pending_change` (scheduled downgrade at period end), `past_due`, `grace`, `suspended`, `cancellation_scheduled`, `cancelled`, `read_only_exit_window`, **`archived`**, **`erased`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| lead | start_trial | identity verified (P01); one trial per legal entity PAN (G) | trial_active | Trial timer 7 days (G: `bil.trial.default_days`) |
| trial_active | extend | `plt_super_admin` via `ENTITLEMENT` Correction Entry (second approver) or approved promo rule | trial_extended | Tenant notified |
| trial_active / trial_extended | checkout_paid (OH8 payment confirmation via `BILLING_PORT`; Razorpay webhook verified by OH8) | — | active | Entitlements granted; GST invoice issued by OH8 (NN-16, X-02) |
| trial_active / trial_extended | timer_end | — | trial_expired | Data retained read-only for `bil.trial.retention_days` (G, default 30; P20), then deleted unless converted or exported (X-15) |
| trial_expired | checkout_paid | — | active | — |
| active | upgrade | — | active | Immediate proration charge; entitlements now |
| active | downgrade | — | pending_change | Applies at period end; data of removed modules kept read-only + exportable (NN-29) |
| active | renewal_payment_failed | — | past_due | Dunning schedule |
| past_due | payment_succeeded | — | active | — |
| past_due | dunning_exhausted | — | grace → suspended | Read-only; exports always available |
| active | cancel | admin; reason | cancellation_scheduled → cancelled at period end | Exit pack offered |
| cancelled / suspended | exit_window_start | — | read_only_exit_window (`bil.exit.read_only_days`, G: default 30, floor 30, max 180; P20) | Full LDC-EXPORT-1.0 free (P19) |
| read_only_exit_window | window_end | — | archived | Retention per law (legal hold respected) |
| archived | erasure_due | no legal hold; statutory retention passed | erased | Erasure certificate |

---

## A.18 Marketplace engagement and retainer (P21)

**States:** `enquiry`, `scoping`, `quoted`, `quote_accepted`, `agreement_sent` (engagement letter / SLA), `agreement_signed`, `advance_due`, `in_progress`, `deliverable_submitted`, `client_review`, `changes_requested`, `accepted`, `invoiced`, `paid`, **`closed`**, `on_hold`, `disputed`, **`cancelled`**, **`refunded`**. Retainers add `active_period` (monthly cycle) and `renewal_due`.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | enquire (public, no login needed) | consent to contact | enquiry | Lead to Ops Hub CRM (D-03) |
| enquiry | scope | provider accepts; conflict check done | scoping → quoted | Quote with GST breakdown (priced and taxed by OH8, X-02) |
| quoted | accept | buyer identity verified | quote_accepted → agreement_sent | Engagement letter / SLA via eSign (D-20) |
| agreement_sent | all_signed | — | agreement_signed → advance_due (if advance) or in_progress | — |
| advance_due | paid | payment confirmed by OH8 | in_progress | Invoice/receipt issued by OH8 |
| in_progress | submit_deliverable | — | deliverable_submitted → client_review | Delivered via DMS share (P07) |
| client_review | accept | buyer | accepted → invoiced | — |
| client_review | request_changes | within revision allowance | changes_requested → in_progress | — |
| invoiced | paid | payment confirmed by OH8 | paid → closed | Provider payout instruction to OH8 per D-06 settings |
| * | dispute | reason | disputed | Resolution workflow; payouts held |
| * | cancel | per terms | cancelled / refunded | Credit note issued by OH8 |
| retainer: active_period | cycle_end | — | invoiced (monthly) and new active_period | Delivery report (hours, deliverables) |

Retainer activation also provisions delivery access: `dlv_rm` as maker in the tenant (A.20-style grant, time-bound to the retainer term; D-03).

---

## A.19 Export job (P19; LDC-EXPORT-1.0)

**States:** `requested`, `approval_pending` (sensitive scope), `approved`, `building`, `ready`, `delivering` (to BYO storage), `delivered`, `downloaded`, **`expired`**, **`failed`**, **`rejected`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | request | scope within requester's permissions | requested | — |
| requested | auto (non-sensitive) / submit (sensitive: sealed, HR, credentials metadata, full tenant) | — | approved / approval_pending | Checker for sensitive scope (NN-05) |
| approval_pending | approve / reject | G-SOD | approved / rejected | — |
| approved | build | — | building | Temporal `ExportBuildWorkflow`; manifest, checksums, BSA s.63 certificate |
| building | complete | export-coverage test passes for scope | ready | Notification |
| ready | push_to_byo | destination verified | delivering → delivered | — |
| ready | download | link valid (default 7 days) | downloaded | Access log |
| ready | ttl_end | — | expired | Files purged |
| building | error | — | failed | Retry (idempotent) |

---

## A.20 Break-glass and support access (NN-30)

**States:** `requested`, `tenant_approval_pending` (support session) or `two_person_approval_pending` (break-glass), `active`, **`ended`**, **`expired`**, **`denied`**, `under_review`, **`reviewed`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | request_support_session | ticket ref; scope; duration ≤ 24 h | tenant_approval_pending | `ten_admin` approval item |
| tenant_approval_pending | approve / deny | `ten_admin` | active / denied | Banner in tenant UI while active |
| — | request_break_glass | incident ID; reason (tenant unreachable or security emergency) | two_person_approval_pending | — |
| two_person_approval_pending | approve | `plt_security_officer` + second platform approver | active | Tenant notified immediately (or post-incident if legally barred, with reference) |
| active | end / ttl | — | ended / expired | Session recording/log sealed |
| ended / expired | review (break-glass) | security officer ≠ user | under_review → reviewed | Report to tenant within 5 working days |

---

## A.21 External access grant (auditor, regulator supervisor view; D-12, Ecosystem Spec §4.7)

**States:** `draft`, `approval_pending`, `active`, `suspended`, **`revoked`**, **`expired`**.

Guards: grantee type (`ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view`), basis code (statutory audit, RBI inspection, SEBI inspection, IFSCA, IRDAI, registrar audit), scope (modules, legal entities, periods), PII level, export level (none, watermarked PDF only), `valid_to` ≤ 90 days; approval by `ten_admin` + `ten_cco`. Every access emits `ExternalAccessUsed`; revoke propagates to federated products (`DELETE /v1/external-access/grants/{id}`).

---

## A.22 Clock and escalation engine (shared)

**Clock states:** `running`, `paused` (internal SLA only, never statutory), `met`, `breached`, `waived_by_regulator` (reference required), `cancelled` (parent withdrawn).

**Escalation ladder (PAT-13):** `L0` owner → `L1` department head (at first breach or at warn offset 2) → `L2` CCO / function head → `L3` CEO / committee chair (statutory clocks: L3 mandatory). Each level: notification, inbox alert, dashboard flag; de-escalates on action. Temporal `ClockWorkflow` per clock; nightly reconciliation job recomputes due dates when a rule-pack version changes and propagation mode requires (P02 FR-P02-22).

---

## A.23 Updates vs Notifications (NN-27)

| Aspect | Regulatory Update (`chg`) | Notification (`wf`) |
|---|---|---|
| Origin | Regulator/government source item reviewed and published by the LDC content team (A.9), or a super-admin broadcast | Work events: assignment, mention, message, approval, due date, calendar event, overdue, task from a senior, system alert |
| States (per user) | `unread → read → acknowledged` (ack required for critical) | `unread → read → done/dismissed`; actionable items live in Work Inbox |
| Model | `chg.regulatory_updates`, `chg.tenant_update_reviews` | `wf.notifications`, `wf.inbox_items` |
| UI | **Updates** menu (feed with filters by regulator, entity family, impact) | Bell + Work Inbox |
| Digest | Daily regulatory digest (20:30 IST default, after the 20:00 scan) | Daily work digest (08:30 default) |
| Can user turn off? | Non-critical channels yes; critical updates always in-app | Per category within tenant policy |

---

## A.26 Change batch and undo window *(v1.1; NN-49; P00 FR-P00-64)*

**States:** `open` (undo available until `undo_until`), **`undone`**, **`partial_undo`**, **`final`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| open | undo | actor = batch actor, tenant admin or CCO; G-STEPUP if > 100 items | undone | Compensating actions in reverse order; `ChangeBatchUndone` |
| open | undo (some items changed later) | as above | partial_undo | Changed items listed for manual decision; task to actor |
| open | timer `undo_until` | — | final | Further changes only by normal edits or Correction Entry (A.5) |

Not undoable (L): sealed-class records, filed returns with acknowledgement, signed documents, messages or files already sent outside the tenant, payments.

## A.27 Jurisdiction pack lifecycle *(v1.1; D-45, NN-53; P25)*

Extends A.6 for country packs. **States:** `draft` → `pilot` → `published` → `deprecated` (with `withdrawn` for packs abandoned before publication).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| draft | submit_for_pilot | source register complete; reviewer of record named; coverage statement drafted | pilot | Available only to tenants opted into the pilot, every screen labelled "Pilot content" |
| pilot | publish | maker ≠ checker; reviewer of record sign-off; pilot feedback closed or deferred with reason; official-language text retained for every clause (NN-54) | published | `JurisdictionPackPublished`; catalogue entry; freshness SLA clock starts |
| published | new_version | as A.6 | published (vN+1) | Tenant impact per A.9 |
| published | deprecate | replacement named or market exit approved; 90-day notice | deprecated | No new adoptions; history kept (NN-29) |
| published | freshness_breach (timer) | source not reviewed within SLA | published (flag `stale`) | Banner to tenants; partner escalation (P25) |

## A.28 Incoming notice and legal matter *(v1.1; D-41; P26)*

**Notice states:** `received` → `classified` → `triaged` → `acknowledged` → `under_investigation` → `reply_drafted` → `reply_approved` → `despatched` → **`closed`** | `converted_to_matter`. Guards: classification by AI is a proposal until a human confirms type, statute and reply deadline (NN-47); `reply_approved` per authority matrix (value, type, severity; G-SOD); `despatched` requires proof of service; the reply-deadline clock follows G-CLOCK (statutory windows never pause).

**Matter states (litigation):** `onboarding` → `counsel_engaged` (conflict check passed; fee letter) → `filed_or_served` → `pre_trial` → `hearings` ⇄ `interim_order` → `evidence` → `arguments` (guard: evidence closed) → `judgment` → `appeal_evaluation` (limitation clock) → `execution_compliance` | `appeal_filed` (new linked matter) → **`closed`** (lessons learnt recorded). Side states: `stayed`, `settled` (settlement record), `withdrawn`. The matter docket is append-only (NN-36 pattern). Provision class changes (probable / possible / remote) are separate transitions with CFO approval each quarter.

## A.29 Contract (CLM-lite) *(v1.1; P26)*

`intake` → `drafting` → `negotiation` (versioned redlines) → `approval` (value/risk-tiered; G-SOD) → `execution` (eSign or wet-ink per IT Act First Schedule) → `active` → `renewal_due` (timer: notice period) → `renewed` | `expired` | `terminated`. Extracted obligations become tenant checkpoints only after approval (NN-04).

## A.30 ESG disclosure cycle *(v1.1; P27)*

`scoping` (materiality approved by Board) → `data_collection` (per KPI: `draft → submitted → checked`, G-SOD) → `computed` (method and emission-factor version stamped; NN-22) → `internal_review` (CSO and CFO sign-off) → `assurance` (assurer seat; `assured` | `qualified` | `not_assured`) → `approved_for_publication` (Board) → `filed_published` (human filing — NN-08) → **`archived`**; `restated` creates a new version with a restatement log.

**CSR cycle (s.135):** `applicability_tested` → `budget_computed` → `action_plan_approved` (Board) → `spending` → `year_end_review` → (`unspent_transfer_pending` with statutory clock) → `reported` (Board's report annexure, CSR-2 prepared) → **`closed`**.

## A.31 Report run *(v1.1; P28)*

`requested` → `snapshot_taken` (point-in-time, hashed) → `validated` (data-quality checks) → `rendered` → `awaiting_approval` (maker-checker per audience tier) → `approved` → `distributed` | `filed` (human) → **`archived`** (WORM). Re-generation from the snapshot reproduces the same output (NN-22).

## A.32 Agent mission and delegation *(v1.1; P17; NN-50, NN-51)*

**Delegation grant:** `requested` → `approved` (sponsor) → `active` → **`ended`** (expiry, revocation, kill switch, sponsor leaves). The autonomy level on a grant may be lowered without approval; raising it needs a new approval.

**Mission run:** `scheduled` → `running` (effective autonomy = minimum of platform, tenant, agent, skill, mission, user and sealed-context levels) → `awaiting_human` (any action at or above the gate) → `running` → **`completed`** | **`failed`** | **`killed`** (kill switch ≤ 60 s). Every tool call is logged; outputs at L2 are drafts; AI never sets a compliance status, risk rating, materiality or audit conclusion (NN-47).

## A.33 Applicability challenge *(v1.1; P01 FR-P01-38)*

`raised` → `under_review` (CCO; LawDocs RM may prepare a note as maker) → **`upheld`** (tenant overlay "not applicable" with reason and citation; reversible) | **`rejected`** (reason). Mandatory family-core items need CCO + second approver to be upheld.

## A.34 Tracker import *(v1.1; P01 FR-P01-43)*

`uploaded` → `parsed` → `mapping_proposed` → `under_review` → `approved` (full or partial) → `importing` → `imported` → (change batch A.26) `undone` | `final`. Create-only (L): no update of base content or existing instances.

## A.35 Region migration *(v1.1; P24 FR-P24-45)*

`requested` → `approved` (owner) → `consented` (tenant) → `transfer_basis_recorded` → `frozen_export` → `replicating` → `read_only` → `verified` → `switched` → `source_retained` → **`source_deleted`** (deletion certificate).

## A.36 Catalogued instrument coverage *(v1.1, X1; P03 §5.7; D-39)*

**States:** `PLANNED` → `IN_PREPARATION` → `AVAILABLE`; any state → **`SUPERSEDED`**.

| From | Event | Guard | To | Side effects / timers |
|---|---|---|---|---|
| PLANNED | Part-2 import job targets the instrument | import batch exists for the catalogue row | IN_PREPARATION | Tenant badge "In preparation" with expected month |
| IN_PREPARATION | content release published | `reference_basis = CONFIRMED`; maker ≠ checker (NN-05); no `[VERIFY]` rows (NN-38) | AVAILABLE | `cnt.CoverageStateChanged`; P04 `PlaceholderConversionWorkflow` per adopting tenant (idempotent; never half-converted) |
| any | P05 records supersession or withdrawal | analyst confirmation (A.40) | SUPERSEDED | Concordance target offered; NN-55 blocks new citations; history kept (NN-29) |

## A.37 Import batch with undo window *(v1.1, X1; P03 §5.8; NN-49)*

Specialises A.26 for content imports. **States:** `APPLIED` (with `undo_deadline`) → `UNDO_CHECK` → **`UNDONE`** | **`PARTIALLY_UNDONE`**; `APPLIED` → **`FINAL`** at the deadline. Blockers are rows already acted on in P04 (instances submitted or reviewed); they are listed and left in place. Undo writes a compensating Correction Entry batch (NN-02).

## A.38 Automated control test run *(v1.1, X1; P04 §5.5A; AA §AA.11)*

`SCHEDULED` | `ON_EVENT` → `RUNNING` → one of **`PASS`** (evidence snapshot attached; instance moves to `submitted_for_review` or attestation — never to `complied` directly, NN-47), **`FAIL`** (exception proposed to the control owner; VA-14 may open a Low/Medium internal issue at L3 only where enabled), **`NO_DATA`** (data-gap task to the data owner), **`INVALID`** (rule error routed to the test owner). Timer: a test stuck in `RUNNING` beyond the timeout on its test definition (`ccm.tests`, AA §AA.11.2) fails closed as `INVALID`. Events: `ControlTestRunCompleted`.

## A.39 Request list item and compliance test cycle *(v1.1, X1; P04 §5.5B–§5.5C)*

**Request item:** `REQUESTED` → (reminders per ladder) → `UPLOADED` (`PENDING_ACCEPTANCE`) → **`ACCEPTED`** (evidence linked; three dates recorded, NN-48) | `RETURNED` (comment; back to `REQUESTED`); `REQUESTED` → `EXPIRED` (link expiry; re-issue creates a new item).

**Test cycle (second-line compliance testing):** `PLANNED` → `SCOPED` (population defined) → `SAMPLED` (seed and method recorded for reproducibility, NN-22) → `IN_TESTING` → `RESULTS_REVIEW` (CCO) → **`CLOSED`** when `EFFECTIVE`; `NEEDS_IMPROVEMENT` or `INEFFECTIVE` → `REMEDIATION` (SLA by risk per `cmp.testing.remediation_sla_days`: High 30 days, Medium 60, Low 90 — tenants may only tighten) → `RETEST` → `CLOSED`. Guard: tester ≠ control performer (SoD).

## A.40 RBI category-page row and content incident *(v1.1, X1; P05 §5.4A–§5.4B)*

**Category-page row:** `ROW_SEEN` (first time) → new-instrument change item → catalogue row `PLANNED` (A.36); `ROW_UPDATED_AS_ON` (changed "Updated as on" date) → consolidation-update change item → clause diff v(n)→v(n+1) → sibling proposals for parallel directions (D-40) → release (NN-34); `ROW_MISSING` (previously listed) → `POSSIBLY_SUPERSEDED` flag → analyst confirms → `SUPERSEDED` | false alarm (parser fix).

**Content incident:** `DECLARED` → `BLAST_RADIUS_COMPUTED` → `CONTAINED` (rollback for future instances; corrective release drafted) → `TENANTS_NOTIFIED` → `CORRECTED` (release published) → `REVIEWED` (post-incident review) → **`CLOSED`**. Timers: S1 containment ≤ 4 hours; S2 ≤ 1 business day; review ≤ 5 business days. Completed tenant instances are never altered (NN-03).

## A.41 Governance sub-machines *(v1.1, X1; P06 §5.8–§5.10)*

**Paper replacement:** `PUBLISHED_PAPER` → `REVISION_PENDING_CS` → `REPLACED` (old version retained; members notified; annotation re-anchor job) → `RE_ANCHOR_DONE`; CS rejection returns to `PUBLISHED_PAPER`; a revision after the notes cut-off is a "late paper" needing the chair's consent recorded in the minutes.

**Securities transfer / transmission request:** `RECEIVED` → `DOCS_CHECK` (→ `AWAITING_DOCS` with reminders; statutory clock keeps running, NN-33) → `RTA_VERIFIED` → `APPROVAL_PENDING` → `APPROVED` → `REGISTERED` (MGT-1 entry by maker, approved by checker) → **`CLOSED`**; or **`REFUSED`** (refusal notice within the statutory period; reason mandatory).

**Annual-report project:** `PLANNED` → `ASSEMBLING` → `CHECKLIST_CLEAR` (no missing lines; cross-figure mismatches resolved; figures only from lineage, NN-37) → `BOARD_APPROVED` (freeze, snapshot hash) → `PUBLISHED` → **`FILED`** (AOC-4/MGT-7 SRNs). A post-freeze change reopens only through a Correction Entry with Board re-approval.

## A.42 Policy drift item and attestation campaign *(v1.1, X1; P07 §5.10–§5.11)*

**Drift item:** `DETECTED` → `UNDER_REVIEW` (policy owner) → `PRACTICE_CORRECTED` (task closed with evidence) | `POLICY_AMENDMENT_STARTED` (linked draft version) → **`RESOLVED`** when the new version is effective | **`ACCEPTED_WITH_REASON`** (CCO approval mandatory for High-risk policies). Re-detection of the same mismatch within 90 days reopens the item.

**Attestation campaign:** `DRAFT` → `SCHEDULED` → `RUNNING` (reminders, escalations, quiz attempts) → **`CLOSED`** (completion snapshot, certificates) | **`CANCELLED`**. A material policy change during `RUNNING` offers close-and-relaunch.

## A.43 AI system (OV_AI) *(v1.1, X1; P12 §5.8; D-36)*

`REGISTERED` → `CLASSIFIED` (risk class approved by the AI Officer; AI proposals only, NN-47) → `ASSESSED` (impact assessment approved; DPIA linked where personal data) → `VALIDATED` (independent validation by `ten_model_validator`, SoD-17) → `APPROVED_FOR_USE` (approval authority by tier; High = RMC/Board resolution link) → `IN_PRODUCTION` → `UNDER_REVIEW` (material change, threshold breach, incident) → `SUSPENDED` (kill switch or override) → **`RETIRED`**. Guards: `IN_PRODUCTION` needs a current validation and a kill-switch test within interval (NN-51); `SUSPENDED` may be entered by the kill-switch owner alone, exit needs a checker. Events: `AISystemRegistered`, `AISystemClassified`, `AISystemApproved`, `AISystemSuspended`, `AISystemRetired`.

## A.44 Legal sub-machines *(v1.1, X1; P26 §5.3, §5.5, §5.6; D-41)*

**Regulator engagement (inspection):** `ANNOUNCED` → `DATA_REQUESTED` → `ON_SITE` → `EXIT_MEETING_HELD` → `DRAFT_OBSERVATIONS_RECEIVED` → `RESPONSE_SUBMITTED` → `FINAL_REPORT_RECEIVED` → `COMPLIANCE_IN_PROGRESS` → `COMPLIANCE_SUBMITTED` → **`CLOSED_BY_REGULATOR`**. **Observation:** `OPEN` → `ACTION_IN_PROGRESS` → `COMPLIED_PENDING_VERIFICATION` → `VERIFIED` (P10 closure test PASS) → `REPORTED_CLOSED` → **`CLOSED_BY_REGULATOR`**; a FAIL returns to `ACTION_IN_PROGRESS`. Records are REGULATOR_CONFIDENTIAL; P10 holds projections only (P26 is owner).

**Licence / registration:** `ACTIVE` → (lead-time timer) `RENEWAL_DUE` → `RENEWAL_FILED` → `ACTIVE` (new validity) | `EXPIRED` (Critical issue; Updates to CCO) ; **`SURRENDERED`** and **`CANCELLED`** are terminal with evidence.

**Ethics declaration:** `REQUESTED` → `SUBMITTED` → `UNDER_REVIEW` → `NO_CONFLICT` | `MITIGATION_DECIDED` (recusal, reassignment, disclosure or prohibition) → **`CLOSED`**. **Gift:** `DECLARED` → `AUTO_APPROVED` (below threshold) | `PENDING_PRECLEARANCE` → `APPROVED` | `DECLINED` (returned or donated, with evidence). Declarant never approves own declaration (SoD-26).

## A.45 ESG sub-machines *(v1.1, X1; P27 §5.1, §5.3, §5.4)*

**Metric value:** `DRAFT` (maker) → `SUBMITTED` → `APPROVED` (checker; SoD-19) | `RETURNED`; approved values roll up; `FROZEN` at disclosure freeze or assurer sign-off; a change after freeze creates `RESTATED` (new version with reason and restatement record).

**CSR project:** `PROPOSED` → `COMMITTEE_RECOMMENDED` → `BOARD_APPROVED` (in the annual action plan) → `ONGOING` → `COMPLETED` → `IMPACT_ASSESSED` (where required) → **`CLOSED`**; at financial-year end an unspent ongoing amount goes to `UNSPENT_TRANSFER_DUE` (30-day statutory clock, NN-33) → `TRANSFERRED`; amounts not spent within three years go to `FUND_TRANSFER_DUE` → `TRANSFERRED`.

**Assurance engagement:** `PLANNED` → `READINESS_REVIEW` → `FIELDWORK` (time-boxed `ext_assurer` grant active) → `ADJUSTMENTS_AGREED` → `REPORT_ISSUED` → **`CLOSED`** (grant expired). Unresolved adjustments block `approved_for_publication` in the disclosure cycle (A.30).

## A.46 Conversation thread *(v1.2; P04 FR-P04-240–246; NN-59; `wf.threads`, `wf.messages`)*

Applies to threads on a compliance instance or on a CompID (all periods). **Types:** `QUERY`, `EXPLANATION_REQUEST` (sub-machine A.47), `GUIDANCE_REQUEST`, `NOTE`, `DECISION`. **States:** `open`, `awaiting_response`, `responded`, `extension_requested`, **`closed`**, **`auto_closed`**. `NOTE` and `DECISION` are created directly in `closed` after the first message (record only).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | open_thread | G-AUTH (view access); type rules of FR-P04-241; addressee required for QUERY, EXPLANATION_REQUEST, GUIDANCE_REQUEST; G-SEAL for sealed instances | awaiting_response (typed) / closed (NOTE, DECISION) | `ThreadOpened`; `ThreadSlaWorkflow` starts with `sla_due_at` = now + `cmp.thread.sla_days[type]` business days; addressee notified; ledger entry on the CompID (NN-57) |
| awaiting_response | post_message (by addressee) | sender verified (in-app session, or signed reply-to token + DMARC for e-mail, or Teams identity) | responded | `ThreadMessagePosted`; timer stopped |
| awaiting_response | timer 50 % / 100 % of SLA | — | same | Reminder to addressee |
| awaiting_response | timer 150 % of SLA (`cmp.thread.escalate_at_pct`) | — | same; `sla_breached` flag | `ThreadSlaBreached`; escalation to addressee's manager (P13 reporting line, A.22 ladder L1); shown in Accountability tab |
| awaiting_response | request_more_time | reason + new date | extension_requested | Requester notified |
| extension_requested | accept_extension / reject_extension | actor = requester | awaiting_response (new `sla_due_at` / original) | Logged |
| responded | post_message (by requester) | — | awaiting_response | SLA restarts at the type default |
| * (non-terminal) | post_message (by others) | G-AUTH; mentions resolved at send time | same | `ThreadMessagePosted`; mentioned users without access get an "ask for access" prompt (no access granted) |
| responded / awaiting_response | close | actor = requester (or `ten_cco`); outcome ∈ Answered, Explanation accepted, Explanation not accepted (comment required), Superseded | closed | `ThreadClosed`; for EXPLANATION_REQUEST → A.47 |
| * (non-terminal) | instance_approved | — | auto_closed | Final summary line; outcome `Superseded` unless the requester reopens within 5 business days |
| closed / auto_closed | reopen | actor = requester; within the instance's reporting window | awaiting_response | Logged |

**Message sub-machine (L, NN-59):** `draft` → `posted` → (author, within `wf.message.edit_window_minutes` = 5) `edited` (original kept as revision) | `withdrawn` (placeholder "withdrawn by author" remains) → after 5 minutes **`locked`**. A locked message can only be followed by a new message; deletion only by retention expiry respecting legal hold (G-HIST). Error `LDC-WF-200` on edit after lock.

## A.47 Explanation request *(v1.2; P04 FR-P04-241, 245, 254; D-53)*

**States:** `requested`, `acknowledged`, `explained`, **`accepted`**, **`not_accepted`**, **`withdrawn`**, **`lapsed`** (no response by 150 % SLA and the instance closed).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | request | requester ∈ {reporting-line superior of addressee (P13), Accountable owner, `ten_cco`, internal auditor, Board/committee secretary}; reason: delay / rejection / non-compliance | requested | `ExplanationRequested`; thread (A.46) of type EXPLANATION_REQUEST |
| requested | open_by_addressee | — | acknowledged | Read receipt in Accountability tab |
| requested / acknowledged | respond | text ≥ 20 characters; optional delay reason code (FR-P04-253) and attachments | explained | `DelayReasonRecorded` if a code is chosen; a named other party gets a right of reply |
| explained | accept | actor = requester | accepted | `ExplanationRecorded` (outcome accepted); explanation record with ledger hash |
| explained | not_accept | actor = requester; comment required | not_accepted | `ExplanationRecorded` (outcome not accepted); accountability flag visible to Accountable owner and CCO |
| explained | ask_further | comment | requested | SLA restarts |
| requested / acknowledged | withdraw | actor = requester; reason | withdrawn | — |
| requested / acknowledged | instance closed and SLA breached | — | lapsed | Recorded as "no explanation given" in the accountability report |

Guards: the respondent can never close their own request; AI may draft a response for the respondent and a summary for the requester (G-AI), but never chooses the outcome (NN-47).

## A.48 Assignment acceptance and owner of record *(v1.2; P04 FR-P04-250–252; D-53, NN-60)*

**Acceptance states:** `offered`, **`accepted`**, **`declined`**, **`lapsed`**, **`withdrawn`** (superseded by another offer).

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | offer (new assignment, reassignment, delegation) | G-AUTH (assigner); offered_to ≠ checker of same instance (G-SOD) | offered | `AssignmentOffered`; `AssignmentAcceptanceWorkflow` timer = `cmp.assign.accept_sla_days`; list shows "Unaccepted" |
| offered | accept | actor = offered_to | accepted | `AssignmentAccepted`; maker holding interval starts at this time |
| offered | decline | reason code (wrong person, no access, conflict, on leave, other + text) | declined | `AssignmentDeclined`; task to assigner to re-offer; holding interval UNASSIGNED starts |
| offered | timer SLA expiry | — | lapsed | `AssignmentAcceptanceLapsed`; escalation to assigner; **maker holding interval starts at the lapse** (non-acceptance cannot avoid responsibility) |
| offered | reoffer to another user | — | withdrawn | New offer created |

**Owner-of-record invariant (L):** `accountable_owner` of every active CompID assignment is never null. On `hr.EmployeeExited`, `hr.LeaveApproved` (covering a due date) or role removal, `OwnerOfRecordGuard` sets the owner to the delegate → department head → `ten_cco` (first available), emits `OwnerOfRecordChanged` with the reason, and offers the assignment (above) to the new owner. A manual change that would leave the owner blank is refused (`LDC-CMP-211`).

**Holding-state projection (NN-60):** `HoldingIntervalProjector` derives `cmp.holding_intervals` from ledger events only: MAKER (accepted/lapsed → submit), CHECKER (submit → decision), RETURNED (return → resubmit), WAITING_INTERNAL / WAITING_EXTERNAL / WAITING_REGULATOR (A.1 `set_waiting` reason party → resume), UNASSIGNED (decline/exit → next acceptance), PLATFORM_INCIDENT (`core.PlatformIncidentDeclared` overlapping the interval, tenant-wide). Intervals never overlap for one instance; the projection can be rebuilt from the ledger and a nightly check compares it with a rebuild. Delay reasons and explanations annotate intervals; they never change them.

## A.49 RAG computation *(v1.2; P04 FR-P04-230–233; D-54, NN-58)*

RAG is a **derived value**, never a stored state of the instance (like `overdue`, A.0.5); `cmp.rag_state` caches it with the rule-set version for lists, exports and history. Evaluated by `RagEvaluator` on every instance event and by `RagSweep` (hourly and at local midnight per entity time zone); deterministic for a given input and rule-set version.

```
function rag(i, rules, today):                         # rules = cmp.rag.rules (G floor ⊕ T widening), versioned
  if i.status in {not_applicable, exempted, withdrawn}:          return GREY,  "Not applicable / exempt / withdrawn"
  if i.frequency == EVENT_BASED and i.trigger_event is null:      return BLUE,  "Awaiting trigger event"
  if i.status in {complied, complied_late}:                       return GREEN, i.status == complied_late ? "Complied late" : "Complied"
  due   = i.status == deferred_by_regulator ? i.regulator_extension_date : i.statutory_due_at   # NN-33
  basis = rules.internal_basis == INTERNAL and context == INTERNAL_REPORTING ? i.internal_due_at : due
  d     = business_or_calendar_days(today, basis, i.entity_calendar)    # negative when past
  if days(today, due) < 0:                                        return RED,   "Overdue by " + |days(today, due)| + " days"
  (red_w, amber_w) = rules.window(i.frequency_class, i.department)      # event-based: % of statutory period remaining
  if i.risk == HIGH: red_w = ceil(red_w * (1 + rules.high_risk_widen_pct/100)); amber_w = ceil(amber_w * (1 + rules.high_risk_widen_pct/100))
  if i.status == returned and d <= amber_w:                       return RED,   "Returned — due in " + d + " days"
  if d <= red_w:                                                  return RED,   (i.risk == HIGH ? "High risk — " : "") + "Due within " + red_w + " days"
  if d <= amber_w:
    if i.evidence_required and not i.evidence_complete:           return AMBER, "Evidence missing — due in " + d + " days"
    if i.status == waiting:                                       return AMBER, "Waiting on " + i.waiting.party + " — due in " + d + " days"
    return AMBER, "Due within " + amber_w + " days"
  return GREEN, "On track"
```

Rules: (1) statutory dates always decide Red-overdue (G-CLOCK); (2) tenant rule sets may only widen windows above the platform floor (`LDC-CMP-205`); (3) a rule-set change runs `RagRuleChangeRecompute` after an impact preview and is itself a config change request (A.4); (4) every colour change writes `cmp.rag_history` and emits `RagChanged` {instance_id, comp_id, from, to, reason_code, rule_set_version, trigger}; (5) severity order for sorting: RED > AMBER > BLUE > GREEN > GREY.

**Prediction (separate, NN-58):** `SlipPredictor` sets `slip_risk` = {probability, model_version, features} and the flag "At risk of slipping" when probability ≥ `cmp.predict.threshold` for GREEN or AMBER instances; emits `SlipRiskFlagged`. It has no transition into the RAG function above and no write access to status, dates or owners (G-AI).

## A.50 List export job *(v1.2; P04 FR-P04-260–265; extends A.19)*

Compliance-list exports reuse A.19 with these additions. **States:** `requested`, `approval_pending` (sensitive scope: sealed items, HR fields, > `cmp.export.max_rows`/2 rows of another department), `approved`, `building`, `ready`, `delivering`, `delivered`, `downloaded`, **`expired`**, **`failed`**, **`rejected`**, **`cancelled`**.

| From | Event | Guard | To | Side effects |
|---|---|---|---|---|
| — | request (definition = view filter AST + sort + group_by ≤ 3 + columns + format + layout) | rows ≤ `cmp.export.max_rows` (`LDC-CMP-202`); group levels ≤ 3 (`LDC-CMP-212`); scope within ABAC | requested | `ListExportRequested`; definition frozen with data as-of time |
| requested | auto / submit | sensitive scope → approval (G-SOD) | approved / approval_pending | — |
| approved | build | rows ≤ `cmp.export.background_threshold_rows` → synchronous; else Temporal `ListExportWorkflow` with progress | building | — |
| building | complete | row count equals the query count at as-of time; hash computed | ready | `ListExportGenerated`; ledger entry on each included CompID (NN-57); watermark |
| building | cancel | actor = requester | cancelled | Partial files purged |
| ready | download / push (e-mail, SharePoint/OneDrive, Google Drive, P28 subscription) | recipient permission re-checked now (`LDC-CMP-214` drops recipient) | downloaded / delivering → delivered | `ListExportDelivered` |
| ready / delivered | ttl (`cmp.export.retention_days`) | — | expired | Files purged; ledger entry kept; `ListExportExpired` |
| building | error | — | failed | Idempotent retry ×3 |

**Schedules:** `cmp.export_schedules` fire `request` with the stored definition at each RRULE occurrence; a schedule whose owner loses access is paused and the owner's manager notified.

## A.51 Star and watch *(v1.2; P04 FR-P04-220–222)*

**Star (personal, private):** `unstarred` ⇄ `starred` (toggle; label and reminder optional). A reminder date creates a personal task (A.3) — never a statutory clock. Stars survive period roll-over when set at CompID level; an instance-level star ends when the instance closes (kept in "Recently starred" 30 days). Emits `StarChanged` to the user's own surfaces only.

**Watch:** `not_watching` → `watching` (self, or added by department head as team watcher — visible to the watched user) → `muted` (user mute within notification budget, §4N) → `not_watching`. Responsible and Accountable users are **implicit watchers** and cannot move to `not_watching` while they hold the role (`LDC-CMP-218`); they may only mute non-floor categories. Emits `WatchChanged`.

**Collection:** `draft` → `shared` → `archived`; items added/removed with actor and time; archived collections remain readable for audit.

## A.24 Event index (lifecycle events introduced in this appendix)

`ComplianceInstanceOpened`, `ComplianceInstanceStatusChanged`, `EvidenceSubmitted`, `EvidenceAccepted`, `EvidenceQuarantined`, `TaskAssigned`, `TaskCompleted`, `AiTaskDraftReady`, `ApprovalRequested`, `ApprovalDecided`, `CorrectionEntryRequested`, `CorrectionEntryApplied`, `EmergencyOverrideApplied`, `ContentReleasePublished`, `ObligationPublished`, `InstrumentRepealed`, `TenantOverlayActivated`, `TenantOverlayConflict`, `RegulatoryUpdatePublished`, `TenantUpdateAcknowledged`, `PolicyVersionApproved`, `PolicyAttested`, `MeetingNoticeIssued`, `MeetingConcluded`, `MinutesSigned`, `AuditFindingRaised`, `AuditFindingClosed`, `RiskIssueRaised`, `RiskAccepted`, `ReturnRunApproved`, `ReturnStatusUpdated`, `GrievanceRaised`, `GrievanceFinalReplySent`, `GrievanceEscalated`, `SubscriptionStatusChanged`, `EngagementStatusChanged`, `ExportReady`, `BreakGlassActivated`, `ExternalAccessGranted`, `ExternalAccessUsed`, `ExternalAccessRevoked`, `ClockBreached`, `EscalationRaised`. Full payloads: Appendix B §B.5.

*(v1.1)* Added: `ChangeBatchCreated`, `ChangeBatchUndone`, `ChangeBatchFinalised`, `JurisdictionPackPiloted`, `JurisdictionPackPublished`, `JurisdictionPackDeprecated`, `NoticeReceived`, `NoticeClassified`, `NoticeReplyDespatched`, `MatterStageChanged`, `MatterProvisionReclassified`, `ContractExecuted`, `ContractRenewalDue`, `EsgKpiChecked`, `EsgDisclosureApproved`, `CsrUnspentTransferDue`, `ReportRunApproved`, `ReportRunArchived`, `DelegationGrantChanged`, `MissionStarted`, `MissionAwaitingHuman`, `MissionCompleted`, `MissionKilled`, `ApplicabilityChallenged`, `ApplicabilityChallengeDecided`, `TrackerImportApproved`, `TrackerImportUndone`, `RegionMigrationStateChanged` (internal family `in.lawdocscomply.<module>.*`; ecosystem mappings per X-01 in P18).

*(v1.2)* Added: `ThreadOpened`, `ThreadMessagePosted`, `ThreadSlaBreached`, `ThreadClosed`, `ExplanationRequested`, `ExplanationRecorded`, `DelayReasonRecorded`, `AssignmentOffered`, `AssignmentAccepted`, `AssignmentDeclined`, `AssignmentAcceptanceLapsed`, `OwnerOfRecordChanged`, `RagChanged`, `SlipRiskFlagged`, `ListExportRequested`, `ListExportGenerated`, `ListExportDelivered`, `ListExportExpired`, `StarChanged` (private), `WatchChanged`, `CollectionChanged` (modules `cmp` and `wf`; P04 §7.4).

## A.25 Sources (accessed 25 October 2026)

*(v1.2)* A.46–A.51 follow P04 §4R and lead spec `_contrib/v12/LEAD_v12_spec.md` (D-50–D-54, NN-56–NN-60); WCAG 2.2 SC 1.4.1 (https://www.w3.org/TR/WCAG22/) for RAG presentation.

*(v1.1)* Additional machines A.26–A.35 follow P00, P01, P17, P24, P25, P26, P27 and P28 of v1.1; Companies Act 2013 s.135 and CSR Rules (CSR cycle); SEBI LODR Reg 34(2)(f) (BRSR); Limitation Act 1963 (appeal clocks) [VERIFY windows per forum in P26].

Companies Act 2013 ss.118, 173, 174 (MCA); ICSI SS-1 and SS-2 (icsi.edu; para numbers [VERIFY]); RBI Integrated Ombudsman Scheme 2026 (effective 1 Jul 2026; RE salient-features copies, e.g. https://www.bandhan.bank.in/sites/default/files/2026-07/Annexure-Salient_features_of_the_Integrated_Ombudsman_Scheme_2026.pdf); RBI Internal Ombudsman directions for NBFCs and banks [VERIFY current consolidated instrument]; CERT-In Directions 28 Apr 2022; RFC 5545 (iCalendar RRULE); Infrabyx Ecosystem Integration Specification v1.1 §§4.7, 6.18, 9.2; Equator Pack v3.1 Appendix AG §AG.7 (pattern library).
