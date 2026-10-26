# Phase O14 — Projects and Work OS (module OH15) *(v1.1)*

**Infrabyx Operations Hub — phase file v1.1 · 26 October 2026** · Companion to `Infrabyx_Operations_Hub_Master_Prompt_ClaudeCode_v1.1.md` (Part 9 Phase O14; module section reproduced below) and `Infrabyx_Operations_Hub_Phase_Runbook_v1.1.md` (paste block for Phase O14). Product code `OH`. Precedence: master prompt → IPB v1.0 → Ecosystem Specification v1.2 → this phase file → appendices. This file restates the module so one Claude Code session can work from a single document; where this file and the master prompt differ, the master prompt prevails and this file is corrected in the same pull request.

## 1. Phase card

| Item | Value |
|---|---|
| Phase | O14 |
| Module | OH15 |
| Depends on | O4, O5, O9 (timesheets); O6 for billable hours |
| Branch | `cc/o14-work-os` (Claude Code convention `cc/<phase>-<slug>`, IPB-09) |
| Binding IPB files | IPB-02 (IPB-02-11 product scope), IPB-07 (Work Inbox, settings tree, help keys), IPB-10 (API and events), IPB-03 §03.4.11 (OH skills referenced) |
| Binding master-prompt sections and appendices | Master prompt Parts 3.3A, 3.5, 4.7; OH4.3, OH6, OH8, OH10.12, OH11; Appendices B (decisions 20, 22), D, E; Ecosystem Spec v1.2 Part 6 (ImplementationMilestoneReached) |
| Owner decisions needed | See Appendix B rows named above; defaults apply where undecided and are listed in the specification |
| Session rule | Read `docs/ipb/00_README.md` first; write the specification; stop for approval; build in small commits; never claim an unrun test |
| Product scope | Every table in this phase carries `legal_entity_id` and `product_scope` with forced RLS and Cerbos policies (Part 3.3A); the acceptance test "an FBX-scoped RM cannot read an LD client ticket" is part of every review gate |

## 2. Module specification (verbatim from the master prompt) — OH15. Projects and Work OS (project management, tasks, boards, time, client status pages) *(v1.1)*

**Purpose.** Give every product team and shared service one place to plan and run work: projects, epics, tasks, boards, sprints, dependencies, time tracking, approvals and RAID, with templates per product scope, client-visible status pages, and tight links to support (OH6), CRM (OH3), onboarding and implementation (OH4), billing (OH8) and the office suite (OH12.9). v1.0 had only OH4.3 implementation projects; OH15 generalises them without moving them: an OH4 implementation project **is** an OH15 project of type `IMPLEMENTATION` with the OH4 gates, milestones and `ImplementationMilestoneReached` event unchanged. OH15 is a work-management system for Infrabyx; it never holds client regulated data (Part 2.3) and it never measures individuals for discipline (Part 4.7).

**Users.** Product heads and delivery leads (project owners), engineers, consultants, marketers, HR, finance and group functions (members), client contacts (status page and acceptance only, through the OH4 portal), leadership (portfolio aggregates), internal audit (read-only), Vidhi (`oh.task_draft`, `oh.project_brief`, L1–L2).

**Requirement codes.** `DPDP` (ss.7(i), 8(5), 8(7)); `LC` (timesheets are records of hours only, OSHWC rr.5–6 via OH10.12); `CA13` s.128 for billable-hour records forming part of books (via OH8); `ISO` 27001 Annex A 5.8 (project security), 8.25–8.32 where projects deliver software; `OUT` paras 34, 77 for client implementation projects (via OH4). Requirement identifiers `REQ-OH15-nn`.

**Data owned.** Project and task metadata per legal entity and product scope; time entries (hours and codes only); client-visible status items approved for publication. Timesheet hours feed OH8 billing and OH10 attendance as self-reported effort (OH10.12).

### OH15.1 Data model

| Entity | Key fields |
|---|---|
| `portfolio` | legal entity, product scope, name, owner, strategic goal refs, period |
| `project` | id, legal entity, `product_scope`, `client_org_id` (optional), type (IMPLEMENTATION, INTERNAL, PRODUCT_DELIVERY, MARKETING_CAMPAIGN, COMPLIANCE, HR_PROGRAMME, EVENT, RESEARCH), template ref, state, owner, sponsor, start, target end, budget hours and amount (optional), billing mode (NON_BILLABLE, FIXED, T_AND_M, RETAINER), rate card ref, RAG, status-page flag, visibility (TEAM, PRODUCT, GROUP), confidentiality class |
| `epic` | project, title, outcome, owner, order, state, target sprint or milestone |
| `task` | project, epic (optional), parent task (sub-task), title, description (rich text, DLP-scanned), type (TASK, BUG, STORY, CHANGE, APPROVAL, CHECKLIST_ITEM), state (from the project's workflow), assignee (one), reviewers[], priority, estimate (hours or points), due date, start date, labels[], linked records (ticket, lead, opportunity, onboarding case, milestone, incident, content item, notebook output), dependency links, watchers[], billable flag, time entries, attachments (hash, AV status), `product_scope` inherited from project |
| `workflow` | per project template: states, transitions, required fields per transition, WIP limits, done definition |
| `board_view` | kanban, list, Gantt (timeline), calendar; filters, swimlanes, saved per user or team |
| `sprint` | project or team, start, end, goal, capacity (hours per member from OH10 arrangements and leave), committed tasks, carry-over record |
| `dependency` | predecessor, successor, type (FINISH_TO_START, START_TO_START, FINISH_TO_FINISH), lag, hard or soft, cross-project allowed only within one product scope or via `GRP` |
| `milestone` | project, name, due, acceptance criteria, evidence ref, client acceptance (OH4 reuse), state |
| `raid_item` | project, class (RISK, ASSUMPTION, ISSUE, DEPENDENCY), description, owner, probability and impact (risks), mitigation, due, state (OH4.3 reuse) |
| `approval_request` | project or task, what is approved (scope change, budget change, go-live, publication, client deliverable), approver role, maker-checker record (OH11) |
| `time_entry` | person, date, task or project or internal code, hours (0.25 granularity), note, billable flag, rate card line, timesheet ref (OH10.12), state |
| `rate_card` | legal entity, product scope, role, hourly or daily rate, currency, validity; from the OH8 catalogue |
| `status_page` | project, public token (client portal), items published (milestones, RAG, next steps, open client actions), last published, publisher, checker |
| `project_template` | product scope, type, default workflow, epics, tasks, checklists, roles, RAID seeds, status-page layout, estimate defaults; versioned |
| `retrospective` | sprint or project, what went well, what to change, actions (tasks) |
| `capacity_snapshot` | team, period, available hours by person (from arrangements and approved leave), allocated hours |

Every entity carries `legal_entity_id`, `product_scope` and, where relevant, `client_org_id`; RLS applies on both scope dimensions (Part 3.3A). Task descriptions and comments pass the OH6.6 DLP patterns (PAN, Aadhaar, account, card, mobile) and are refused or redacted; attachments carrying client regulated data are quarantined as in OH6.6.

### OH15.2 Project lifecycle

```
PROPOSED → APPROVED (DoA: owner, sponsor, budget) → PLANNED (template applied; milestones; team) → ACTIVE
  → (ON_HOLD ↔ ACTIVE) → DELIVERED (all milestones accepted) → CLOSED (retrospective, time locked, status page archived)
PROPOSED → REJECTED (reason); ACTIVE → CANCELLED (reason; open tasks disposed; time locked)
```

- **REQ-OH15-01** `APPROVED` needs an owner, a sponsor from the product scope, and, where hours or amounts are budgeted, a DoA approval (OH11.1); client-facing projects also need the OH4 contract reference (SOW or MSA schedule) and inherit the OH4 gate states for provisioning.
- **REQ-OH15-02** `PLANNED` applies a template; the owner may add or remove items but mandatory checklist items from the template (security review, DPIA where personal data is processed, claims-gate review for client deliverables, residency check for client migrations) cannot be deleted, only marked not applicable with a reason and a checker.
- **REQ-OH15-03** `ON_HOLD` pauses SLA clocks on tasks and status-page countdowns and records the reason; a project on hold for 90 days alerts the sponsor.
- **REQ-OH15-04** `DELIVERED` requires every milestone `ACCEPTED` (client acceptance evidence for client projects, OH4.3) and every `APPROVAL` task done; `CLOSED` locks time entries (after the billing run picks them up), archives the status page with a final notice, triggers the retrospective and releases guest access in OH12.4.
- **REQ-OH15-05** Scope and budget changes are `approval_request`s under the DoA; a change above 10% of budgeted hours or amount escalates to the sponsor [REC].

### OH15.3 Tasks, workflows and boards

- **REQ-OH15-06 Workflows** are per template: default `BACKLOG → READY → IN_PROGRESS → IN_REVIEW → DONE` with `BLOCKED` as a flag, not a state; a template may add states (for example `CLIENT_REVIEW`, `LEGAL_REVIEW`, `QA`); transitions may require fields (estimate before `READY`, reviewer before `IN_REVIEW`, evidence before `DONE`); WIP limits per state are soft by default and hard where the template says so.
- **REQ-OH15-07 Boards** render the same task set as kanban (columns = states, swimlanes by epic, assignee or priority), list (sortable, bulk edit with preview), Gantt (timeline with dependencies, critical path, baseline versus actual, drag to reschedule with dependency propagation and a confirmation), and calendar; views save filters, columns and grouping as personal, team or product views (Part 3.5 saved views; the view stores the query, not results).
- **REQ-OH15-08 Sprints** (optional per project): capacity from OH10 arrangements and approved leave minus a focus factor (Commercial setting, default 70% [REC]); over-commitment shows a warning; sprint close carries over unfinished tasks with a record; burndown and velocity are **team** metrics visible to the team and their lead only, never per person outside the team view, and never used in appraisal (OH10.8, OH11.6 cell ≥ 5).
- **REQ-OH15-09 Dependencies** block a successor's transition to `IN_PROGRESS` when a hard predecessor is not done; cross-project dependencies are allowed within a product scope and, through `GRP`, across scopes with both owners' approval; a dependency on a record the user cannot see shows as "external dependency (restricted)" with no details.
- **REQ-OH15-10 Sub-tasks and checklists** roll up progress; a parent cannot be `DONE` with open children.
- **REQ-OH15-11 Comments and mentions** notify watchers (Appendix E.4 "Mentions"); comments are DLP-scanned; edits keep history; deletion is soft and logged.
- **REQ-OH15-12 Recurring tasks** use RFC 5545 `RRULE` (shared with Vidhi scheduled tasks, IPB-03-64) with time zone and `EXDATE`; a recurring task creates the next instance on completion or on schedule per template.
- **REQ-OH15-13 Approvals as tasks.** `APPROVAL` tasks bind to OH11 maker-checker: the approver sees the diff, evidence and consequences; fresh MFA to approve; the maker never approves; approval outcome writes the audit chain.
- **REQ-OH15-14 Keyboard and bulk.** `J`/`K`, `A` assign, `E` edit, `/` filter, `M` move state; bulk actions preview the count and allow 10-second undo for non-financial changes (Part 3.5).
- **REQ-OH15-15 Work Inbox.** OH15 tasks assigned to or awaiting the user appear in the Work Inbox and My Queue sorted by due date and SLA (IPB-07 Work Inbox model), with deterministic next-best-action text (for example "Estimate and move to Ready").

### OH15.4 Templates per product scope

| Scope | Seeded templates (v1.1) |
|---|---|
| `FBX` | NBFC implementation (OH4 profiles), data-migration programme, UAT cycle, regulatory-change rollout (ties to `ReleasePublished` with regulatory impact), quarterly client review |
| `UDF` | RE partner onboarding, lender integration, app release, compliance review (Digital Lending Directions checklist by reference, no content held) |
| `LD` | Template-library release, eSign provider integration, enterprise client onboarding, SEO and content sprint |
| `LDC` | Compliance-module release, regulatory-feed onboarding, client obligations onboarding, board-pack season |
| `EQ` | Panel onboarding, hearing-room operations improvement, institution rules update (never case work) |
| `TRN` | Course production, cohort delivery, certification run |
| `HSP` | Property onboarding, seasonal campaign, vendor renewal cycle, audit preparation |
| `GRP` | Policy drafting and approval (links OH16 notebooks and OH14.5 policy register), audit period preparation (OH14.4), payroll year-end, website release (OH18), group event, hiring drive, intern cohort (OH10.11) |

Templates are versioned data owned by the product head (maker) and the PMO or Hub administrator (checker); a template may not remove the mandatory checklist items of REQ-OH15-02.

### OH15.5 Client-visible status pages

- **REQ-OH15-16** A client project may publish a status page inside the OH4 client portal: milestones with dates and states, overall RAG with a one-line explanation, next steps, open client actions with owners and due dates, recent accepted deliverables, and a contact. The page shows **only items marked for publication** and reviewed by a second person (maker-checker; the claims gate runs on free text); internal notes, RAID detail, time, cost and staff names beyond the project lead never appear.
- **REQ-OH15-17** Publication is versioned; the client sees "last updated" and may subscribe to e-mail digests (consent-based, service category); access uses the OH4 portal identity with 90-day guest expiry (OH12.4) and the client's own scope only.
- **REQ-OH15-18** Client acceptance of a milestone on the status page is the OH4.3 acceptance evidence and emits `ImplementationMilestoneReached` for `IMPLEMENTATION` projects.

### OH15.6 RAID, risks and reporting

- **REQ-OH15-19** RAID per project with owner, due, probability and impact scoring (risks), mitigation tasks (linked), review cadence; overdue items surface on the owner's home and the sponsor's portfolio view.
- **REQ-OH15-20** Portfolio dashboards (OH2 metric layer): projects by state and RAG per product scope, milestones due in 14 days, budget consumed versus planned, billable utilisation by **team** (OH11.6), dependency hotspots; group leadership sees aggregates across scopes, record drill-down within scopes held (Part 3.3A).
- **REQ-OH15-21** Project health is a transparent formula (schedule variance, open high risks, blocked tasks share, acceptance backlog) with the inputs shown; no AI-derived health score drives escalation without a human reading it.

### OH15.7 Time tracking and billing integration

- **REQ-OH15-22** Time entries (0.25-hour granularity, per task or project or internal code) are self-reported; timers are optional and run only when the user starts them; the weekly timesheet of OH10.12 is the submission and approval vehicle; approved entries lock.
- **REQ-OH15-23** Billable entries carry a rate-card line from the OH8 catalogue; the monthly billing run aggregates approved billable hours per client, project and role into `UsageRecorded`-style internal usage for T&M invoices and into retainer consumption; the client invoice (OH8.6) shows hours by role and period, never individual names unless the contract requires them; disputes follow OH8 usage-dispute rules.
- **REQ-OH15-24** Fixed-price projects track hours for margin only; margin and utilisation are team-level OH11.6 metrics with cell ≥ 5 and never the sole basis for any people decision.
- **REQ-OH15-25** Timesheet reminders follow quiet hours (OH10.10); no automated escalation on unlogged time beyond the manager's queue.

### OH15.8 Integrations, Vidhi and events

- **Support (OH6):** a ticket converts to a task or links to one; task state changes post a note on the ticket; a `problem` record may own tasks across projects within a scope.
- **CRM (OH3):** an opportunity at `PROPOSAL` may spawn a presales project; a won opportunity spawns the onboarding case and implementation project from the product template (OH4.2).
- **Onboarding and implementation (OH4):** OH4.3 projects are OH15 projects of type `IMPLEMENTATION`; OH4 gate states, milestones and migration runs are unchanged and surfaced as OH15 milestones and tasks.
- **Billing (OH8):** rate cards, billable hours, retainer balances, project invoices.
- **Marketing (OH7, OH17):** campaign projects link content items and publication dates to tasks.
- **Knowledge (OH16):** a notebook output (briefing, checklist) can be attached to a task; policy-drafting projects link the policy version in OH14.5.
- **Workplace (OH12.9):** calendar events for ceremonies, To Do and Planner mirroring, Teams channel per project with the naming rule, SharePoint project site via `Sites.Selected`.
- **Engineering (OH13):** a `CHANGE`-type task links to an OH13 change record; a release project links `ReleasePublished`.
- **Vidhi skills (OH16, IPB-03):** `oh.task_draft` (L1: draft tasks, sub-tasks and acceptance criteria from a brief, ticket or meeting notes), `oh.project_brief` (L1: project brief and risk list from a template and linked records), `oh.status_update_draft` (L1: draft the client status text from accepted milestones; the claims gate and a human publish), `oh.sprint_summary` (L1: team-level sprint narrative). Vidhi never assigns work to a person, never changes estimates or states autonomously above L2, and never produces per-person productivity text.
- **Events (`oh` scope, internal):** `in.oh.pm.ProjectStateChanged.v1`, `in.oh.pm.MilestoneAccepted.v1` (also emits the ecosystem `ImplementationMilestoneReached` for implementation projects as today), `in.oh.pm.TaskStateChanged.v1`, `in.oh.pm.StatusPagePublished.v1`, `in.oh.pm.TimeApproved.v1` (hours, codes, rate-card line; no names outside OH8 and OH10). None carry client regulated data.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Project approval and budget-change thresholds | Entity, scope | DoA pack; 10% change escalates [REC] | Commercial within DoA (Floor: DoA applies) |
| Mandatory template checklist items | Platform | Security review, DPIA, claims-gate review, residency check (where applicable) | Floor (may add, not remove) |
| Workflow states and WIP limits | Template | OH15.3 default; soft WIP | Commercial |
| Sprint capacity focus factor | Team | 70% [REC] | Commercial |
| Time granularity and timer | Platform | 0.25 h; timers optional, user-started | Floor: no automatic timers |
| Billable-hours export and rate cards | Entity, scope | Monthly to OH8; OH8 catalogue | Commercial; rates from the signed catalogue (Floor) |
| Status-page publication | Project | Off; maker-checker; claims gate | Floor for maker-checker and claims gate |
| Client digest frequency | Project | Weekly, consent-based | Commercial |
| Individual velocity or utilisation visibility | Platform | Team only; cells ≥ 5 | Floor |
| Vidhi autonomy for `oh.task_draft` and `oh.status_update_draft` | Scope | L1 | Ceiling L2 (Floor) |
| DLP on descriptions, comments and attachments | Platform | OH6.6 patterns | Floor |
| Guest access to status pages | Project | 90 days, named contacts | Floor (maximum) |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Projects › Portfolio` | Projects by product scope, state and RAG; milestones due; budget versus actual; dependency hotspots; aggregate for group roles | Product heads, leadership (aggregate), PMO |
| `Projects › My work` | My tasks across projects by due and SLA (Work Inbox integration); timers; this week's timesheet | All staff |
| `Projects › Boards` | Kanban, list, Gantt, calendar per project or team; saved views; bulk actions; dependency editor | Members, owners |
| `Projects › Project detail` | Overview (RAG, formula inputs), epics, tasks, milestones, RAID, approvals, time and budget, status page preview and publish, documents (SharePoint links), Teams channel, retrospective | Members (own scope), owner, sponsor |
| `Projects › Sprints` | Planning with capacity, commitment, carry-over, team burndown and velocity (team only) | Team, lead |
| `Projects › Templates` | Template catalogue by scope and type; versioning; mandatory items; diff before publish | Product heads (maker), PMO (checker) |
| `Projects › Time` | Time entries by week; approvals; billable export status; retainer balances | Members, managers, finance |
| `Projects › Status pages` | Published pages, versions, subscribers, pending publications | Owners, checkers |
| Client portal (OH4) › Project status | Milestones, RAG, next steps, client actions, acceptance | Client contacts |

Empty and error states: a new project opens on the template picker with the mandatory items explained; a blocked transition names the unmet rule ("Successor cannot start: predecessor `Data mapping signed off` is not done"); a publication blocked by the claims gate shows the phrase.

### Acceptance tests

- An FBX-scoped consultant cannot open, list, search, mention or receive a digest about an LD project or task; the denied read is logged as `scope_denied`.
- A project cannot reach `APPROVED` without owner, sponsor and (where budgeted) a DoA approval; a 15% budget increase routes to the sponsor; a mandatory checklist item cannot be deleted and needs a checker to be marked not applicable.
- A task with a hard predecessor not done cannot move to `IN_PROGRESS`; a parent with open sub-tasks cannot be `DONE`; a comment containing a PAN-like pattern is refused.
- Sprint velocity is visible to the team and lead only; no per-person velocity metric exists in the metric catalogue (negative test); an appraisal screen has no link to OH15 metrics.
- Approved billable hours for a month aggregate to the OH8 T&M invoice by role; a change to an approved entry after lock is refused; a rate not in the signed catalogue is refused.
- A status page shows only items marked for publication and checked by a second person; an internal RAID note never renders; client acceptance on the page emits `ImplementationMilestoneReached` for an implementation project; guest access ends at 90 days.
- A Vidhi draft of tasks is created in `BACKLOG` with the AI label and run id and assigns nobody; a Vidhi attempt to change a task state at L1 is refused.
- A To Do completion proposes, and does not apply, task completion (OH12.9).
- Closing a project locks time entries after the billing run and archives the status page with a final notice; a retrospective is created.


## 3. Instruction to Claude (from master prompt Part 9)

> **Instruction to Claude:** "Read docs/ipb/00_README.md, then IPB-07 (Work Inbox, settings tree), IPB-02 (product_scope IPB-02-11) and IPB-10 before the plan. Verify first: (i) the OH4.3 implementation-project model and `ImplementationMilestoneReached` contract so OH15 wraps them without a breaking change; (ii) the OH8 rate-card and T&M invoicing rules and the OH10.12 timesheet model; (iii) the IPB-07 Work Inbox item model and keyboard map; (iv) RFC 5545 `RRULE` library choice shared with the Vidhi scheduler.
>
> On branch `cc/o14-work-os` build OH15 (master prompt OH15; phase file `v1.1 supplements/phases/Phase_O14_Projects_and_Work_OS.md`):
>
> - **Data model and RLS:** portfolio, project, epic, task, workflow, board_view, sprint, dependency, milestone (OH4 reuse), raid_item (OH4 reuse), approval_request (OH11 binding), time_entry, rate_card (OH8 read), status_page, project_template, retrospective, capacity_snapshot — every table with `legal_entity_id` and `product_scope`, forced RLS on both, Cerbos policies, DLP on descriptions and comments.
> - **Lifecycles:** project `PROPOSED → … → CLOSED` with DoA at `APPROVED`, mandatory template checklist items, hold rules; task workflows per template with required fields, soft and hard WIP, hard dependencies, sub-task roll-up, soft delete; recurring tasks by `RRULE`.
> - **Boards:** kanban, list, Gantt with dependency propagation and baseline, calendar; saved views (query, not results); bulk actions with preview and undo; keyboard shortcuts; Work Inbox and My Queue integration with next-best-action text.
> - **Templates per product scope** (OH15.4) as versioned data with maker-checker; migrate OH4.3 implementation templates into OH15 templates of type `IMPLEMENTATION` without changing OH4 gates or events.
> - **Sprints** with capacity from OH10 arrangements and leave; team-only velocity and burndown (cells ≥ 5; nothing per person outside the team view).
> - **Time and billing:** 0.25-hour entries, optional user-started timers, weekly timesheet submission through OH10.12, approved billable hours to OH8 by rate-card line, retainer consumption, lock after billing run.
> - **Client status pages** in the OH4 portal: publication-marked items only, maker-checker, claims gate, versions, consent-based digests, 90-day guest expiry, client acceptance emitting `ImplementationMilestoneReached`.
> - **Integrations:** OH6 ticket ↔ task, OH3 opportunity → presales or onboarding project, OH12.9 calendar and To Do or Planner mirroring (confirm-before-apply), Teams channel and SharePoint site per project, OH13 change links, OH16 skills `oh.task_draft`, `oh.project_brief`, `oh.status_update_draft`, `oh.sprint_summary` at L1.
> - **Menus, screens and settings:** the `Projects` menu and OH15 settings exactly as the OH15 `Menu and screens` and `Settings and options` tables specify; `hlp.oh.pm.*` keys for every field; Home tiles for workspace B and the new workspace Q.
>
> Tests and acceptance evidence: every OH15 acceptance test, in particular the FBX-versus-LD scope denial on open, list, search, mention, digest and export; DoA at approval; hard-dependency block; no per-person velocity metric; billable-hour aggregation to an OH8 invoice; status page shows only published items and guest access ends at 90 days; Vidhi drafts assign nobody and cannot change states.
>
> Show me the entity model, RLS and Cerbos policies, workflow and template schema, Gantt dependency rules and status-page publication flow for approval before coding."

**Exit gate:** OH15 acceptance tests green with recorded output; OH4 regression suite unchanged and green; scope-isolation tests in CI; settings and `hlp` keys registered; DPIA note for time entries; docs/status updated.

## 4. Build notes for Claude Code

### 4.1 Sub-module plan (one session each)

| Session | Scope | Depends on | Exit evidence |
|---|---|---|---|
| O14a | Schema `pm`: tables, RLS policies on `legal_entity_id` and `product_scope`, Cerbos resource policies (`pm:project`, `pm:task`, `pm:time_entry`, `pm:status_page`), project lifecycle service, DoA binding, template checklist enforcement | O2 | RLS tests; lifecycle tests; schema lint for `product_scope` |
| O14b | Task workflows, dependencies, sub-tasks, recurrence, comments with DLP, boards (kanban, list, Gantt, calendar), saved views, bulk actions, keyboard map, Work Inbox items | O14a | Board snapshot tests; dependency and WIP tests; axe zero critical |
| O14c | Templates per scope; migration of OH4.3 projects into `type = IMPLEMENTATION`; OH4 regression | O14a, O4 | OH4 suite green; template versioning tests |
| O14d | Sprints and capacity (OH10 arrangements and leave), RAID, retrospectives, portfolio metrics on the OH2 layer | O14b, O9 | Team-only metric tests; capacity tests |
| O14e | Time entries, timers, OH10.12 timesheet integration, rate cards, OH8 billable export, locks | O14a, O6, O9 | Billing aggregation golden case |
| O14f | Status pages (OH4 portal), integrations (OH6, OH3, OH12.9, OH13), Vidhi skills registration (manifests only; runtime arrives in O15) | O14b–O14e | Publication and guest-expiry tests; manifest validation |

### 4.2 API surface (`/v1/pm/...`, IPB-10 conventions)

| Method and path | Purpose | Scope and authorisation |
|---|---|---|
| `GET/POST /v1/pm/projects` | List (cursor pagination, filters by scope, state, RAG) and propose a project | `oh.pm.read`, `oh.pm.write`; RLS and Cerbos |
| `POST /v1/pm/projects/{id}:transition` | Lifecycle transition with reason; DoA check at `APPROVED` | Maker; checker for DoA |
| `GET/PATCH /v1/pm/projects/{id}` | Detail; edit with optimistic `version` | Members |
| `POST /v1/pm/projects/{id}/template:apply` | Apply a template version | Owner |
| `GET/POST /v1/pm/tasks`, `PATCH /v1/pm/tasks/{id}`, `POST /v1/pm/tasks/{id}:transition` | Tasks, state changes (required fields, dependency and WIP checks) | Members |
| `POST /v1/pm/tasks/{id}/dependencies` | Add dependency (cross-scope requires `GRP` and both owners) | Owner |
| `POST /v1/pm/tasks/{id}/comments` | Comment (DLP; mentions) | Members |
| `GET/POST /v1/pm/sprints`, `POST /v1/pm/sprints/{id}:close` | Sprint planning and close with carry-over | Lead |
| `GET/POST /v1/pm/time-entries`, `POST /v1/pm/time-entries:submit` | Time entries and weekly submission (OH10.12) | Self |
| `POST /v1/pm/time-entries:export-billable` | Monthly billable aggregation to OH8 (idempotent per period) | Finance |
| `GET/POST /v1/pm/status-pages/{projectId}/versions`, `POST …:publish` | Status-page versions; publish needs checker and claims gate | Owner, checker |
| `GET /v1/pm/status-pages/public/{token}` | Client portal read (OH4 identity) | Client contact (scope of their org) |
| `GET/POST /v1/pm/templates`, `POST /v1/pm/templates/{id}:publish` | Template catalogue, versioning, maker-checker | Product head, PMO |
| `GET /v1/pm/portfolio/metrics` | Governed metrics (aggregate for `GRP`) | Leadership, product heads |

Errors (RFC 9457 `type` slugs): `pm/scope_denied`, `pm/doa_required`, `pm/mandatory_item_locked`, `pm/dependency_blocked`, `pm/wip_limit`, `pm/required_field_missing`, `pm/children_open`, `pm/time_locked`, `pm/rate_not_in_catalogue`, `pm/claims_blocked`, `pm/checker_required`, `pm/guest_expired`, `pm/dlp_blocked`, `pm/version_conflict`.

### 4.3 Settings keys registered in this phase

`pm.approval.change_escalation_pct` (10), `pm.template.mandatory_items` (floor list), `pm.workflow.default_states`, `pm.sprint.focus_factor` (0.70), `pm.time.granularity_hours` (0.25), `pm.time.timers_enabled` (true; user-started only), `pm.billing.export_cadence` (monthly), `pm.status_page.require_checker` (true, floor), `pm.status_page.guest_days` (90, floor max), `pm.metrics.individual_visibility` (team_only, floor), `pm.dlp.patterns` (OH6.6 set, floor), `vidhi.skill.oh.task_draft.autonomy_level` (L1, ceiling L2).

### 4.4 Events

Internal: `in.oh.pm.ProjectStateChanged.v1`, `in.oh.pm.MilestoneAccepted.v1`, `in.oh.pm.TaskStateChanged.v1`, `in.oh.pm.StatusPagePublished.v1`, `in.oh.pm.TimeApproved.v1`. Ecosystem (registered, unchanged): `ImplementationMilestoneReached` for `IMPLEMENTATION` projects. Consumed: `SupportTicketOpened` (OH6, to offer "create task"), `in.oh.hr.TimesheetApproved.v1`, OH12.9 `ws.*` events.

### 4.5 Help keys (minimum set)

`hlp.oh.pm.project_scope`, `hlp.oh.pm.rag_formula`, `hlp.oh.pm.mandatory_checklist`, `hlp.oh.pm.hard_dependency`, `hlp.oh.pm.wip_limit`, `hlp.oh.pm.sprint_capacity`, `hlp.oh.pm.focus_factor`, `hlp.oh.pm.billable_flag`, `hlp.oh.pm.rate_card`, `hlp.oh.pm.status_page_publication`, `hlp.oh.pm.guest_expiry`, `hlp.oh.pm.team_velocity` (explains why no per-person velocity exists, citing Part 4.7 and OH10.5).

## 5. Acceptance tests (Gherkin)

```gherkin
Feature: Product-scope segregation in Projects and Work OS
  @REQ-OH15-01 @IPB-D-12
  Scenario: FBX-scoped consultant cannot reach an LD project
    Given user "test.employee@opshub.test" holds product scope FBX only
    And project "LD-2026-014" exists under product scope LD with task "LD-T-88"
    When the user requests GET /v1/pm/projects/LD-2026-014
    Then the response is 404 with type "pm/scope_denied"
    And a "scope_denied" audit event records actor, held scopes [FBX] and requested scope LD
    When the user searches "LD-T-88" in global search
    Then no result is returned
    When an LD colleague shares saved view "LD open tasks" with the user
    Then opening the view returns zero rows under scope FBX

Feature: Project lifecycle and DoA
  @REQ-OH15-01 @REQ-OH15-05
  Scenario: Approval requires owner, sponsor and DoA
    Given a PROPOSED project with budget 400 hours and no sponsor
    When the owner requests transition to APPROVED
    Then the response is 422 with type "pm/doa_required" listing "sponsor" and "doa_approval"
    Given a sponsor from scope FBX and a DoA approval by a different user
    When the owner requests transition to APPROVED
    Then the project is APPROVED and the audit chain has a maker and a checker entry
  Scenario: Budget change above threshold escalates
    Given an ACTIVE project with budget 400 hours
    When the owner proposes a change to 470 hours
    Then an approval_request routed to the sponsor is created and the budget is unchanged until approval

Feature: Task rules
  @REQ-OH15-09 @REQ-OH15-10 @REQ-OH15-11
  Scenario: Hard dependency blocks start
    Given task B has a FINISH_TO_START hard dependency on task A in state IN_PROGRESS
    When a member moves task B to IN_PROGRESS
    Then the response is 409 with type "pm/dependency_blocked" naming task A
  Scenario: DLP on comments
    When a member posts a comment containing "PAN ABCDE1234F"
    Then the comment is refused with type "pm/dlp_blocked" and nothing is stored

Feature: Team-only metrics
  @REQ-OH15-08 @REQ-OH15-24
  Scenario: No per-person velocity
    When the metric catalogue is listed
    Then no metric has grain "person" for velocity, utilisation or throughput
    And the appraisal screen contains no link to the pm module

Feature: Time to billing
  @REQ-OH15-22 @REQ-OH15-23
  Scenario: Approved billable hours reach the invoice
    Given 12.5 approved billable hours for client "Demo Co" at rate-card line "Consultant" in October 2026
    When the monthly export runs
    Then OH8 receives one aggregate line of 12.5 hours for "Consultant" with the project reference
    And re-running the export for October creates no second line
    When a member edits a locked entry
    Then the response is 423 with type "pm/time_locked"

Feature: Client status page
  @REQ-OH15-16 @REQ-OH15-17 @REQ-OH15-18
  Scenario: Only published items render and guest access expires
    Given milestone "Data mapping signed off" marked for publication and RAID item "Vendor delay risk" not marked
    When a checker publishes version 3
    Then the client page shows the milestone and not the RAID item
    And the client's acceptance of the milestone emits ImplementationMilestoneReached
    Given the client guest was created 91 days ago
    When the client opens the page
    Then the response is 403 with type "pm/guest_expired"

Feature: Vidhi task drafting
  @REQ-OH15-25 @IPB-03-71
  Scenario: Drafts assign nobody and cannot change states
    When skill oh.task_draft runs on a brief
    Then tasks are created in BACKLOG with assignee null and the AI label and run id
    When the agent attempts PATCH on a task state
    Then the response is 403 with type "IPB-VID-040"

Feature: Adversarial — IDOR, self-approval and locked time *(v1.1 review)*
  @REQ-OH15-16 @REQ-OH15-17 @IPB-02-11
  Scenario: Status-page token of another client is refused
    Given client contact C1 is signed in to the OH4 portal for client org A with a valid status-page token for project P-A
    When C1 requests GET /v1/pm/status-pages/public/{token of project P-B} belonging to client org B
    Then the response is 404 (no existence leak) and an audit event "status_page_denied" records actor, token hash and project
    And the same request with a guessed or expired token returns 404 with the same timing profile

  @REQ-OH15-13 @REQ-OH15-22
  Scenario: Maker cannot approve their own APPROVAL task or timesheet
    Given user U1 created an APPROVAL task and submitted their own weekly timesheet
    When U1 attempts to approve either record, directly or through a Vidhi-prepared approval
    Then the response is 403 with type "pm/checker_required" and the maker-checker audit chain records the refusal
    And an approver with the role but a stale (expired) product-scope assignment is refused with "pm/scope_denied"

  @REQ-OH15-22 @REQ-OH15-23
  Scenario: Locked time entry cannot be edited through any path
    Given a time entry locked after the monthly billing run
    When a PATCH, a bulk edit, a CSV re-import or an MCP write tool targets that entry
    Then every path returns 409 with type "pm/time_locked" and no row changes
```

## 6. Exit gate

- All Gherkin scenarios above and the OH15 acceptance list pass with recorded output; OH4 regression unchanged.
- `pnpm lint:schema` confirms `product_scope` on every `pm` table; Cerbos policy tests cover every resource and action.
- Settings and help keys registered; Storybook stories for boards, approval card and status page; axe zero critical.
- DPIA note for time entries and comments filed in `docs/privacy/`; `docs/status` updated; pull request merged after owner approval.

## 7. Data model sketch (schema `pm`)

```
pm.portfolio(pf_id pk, legal_entity_id, product_scope, name, owner_id, goal_refs text[], period daterange)
pm.project(prj_id pk, legal_entity_id, product_scope, client_org_id null, type, template_id, template_version, state, owner_id, sponsor_id, starts_on, target_end, budget_hours numeric(10,2), budget_amount numeric(18,2), billing_mode, rate_card_id, rag, status_page_enabled bool, visibility, data_class, version int)
pm.epic(epc_id pk, prj_id fk, title, outcome, owner_id, position, state, target_ref)
pm.task(tsk_id pk, prj_id fk, epc_id null, parent_id null, title, description_html, type, state, assignee_id null, reviewers uuid[], priority, estimate numeric(8,2), estimate_unit, starts_on, due_on, labels text[], billable bool, rrule text null, version int)
pm.task_link(from_id, to_id, kind check in ('TICKET','LEAD','OPPORTUNITY','ONBOARDING_CASE','MILESTONE','INCIDENT','CONTENT','NOTEBOOK_OUTPUT','CHANGE'))
pm.dependency(pred_id, succ_id, type, lag_days int, hard bool, cross_scope_approved_by uuid[] )
pm.workflow(wf_id pk, template_id, states jsonb, transitions jsonb, wip_limits jsonb, done_definition text)
pm.board_view(bv_id pk, owner_kind check in ('USER','TEAM','SCOPE'), owner_ref, kind, query jsonb, columns jsonb)
pm.sprint(spr_id pk, prj_id null, team_id, starts_on, ends_on, goal, capacity_hours numeric, focus_factor numeric, state)
pm.sprint_task(spr_id, tsk_id, committed bool, carried_over_from null)
pm.approval_request(apr_id pk, prj_id, tsk_id null, kind, payload_diff jsonb, approver_role, mc_request_id fk oh11.maker_checker_request)
pm.time_entry(te_id pk, person_ref, on_date, tsk_id null, prj_id null, internal_code null, hours numeric(5,2) check (hours % 0.25 = 0), note, billable bool, rate_line_id null, timesheet_id fk hr.timesheet, state)
pm.status_page(sp_id pk, prj_id fk unique, public_token, state)
pm.status_page_version(spv_id pk, sp_id fk, version int, payload jsonb, claims_check jsonb, published_by, checked_by, published_at)
pm.project_template(tpl_id pk, product_scope, type, version, workflow jsonb, epics jsonb, tasks jsonb, checklist jsonb, mandatory_items text[], raid_seeds jsonb, status_page_layout jsonb, state, maker_id, checker_id)
pm.retrospective(ret_id pk, spr_id null, prj_id null, went_well text, change text, action_task_ids uuid[])
pm.capacity_snapshot(team_id, period, person_ref, available_hours numeric, allocated_hours numeric)   -- team view only
```

RLS policy template for every table: `USING (legal_entity_id = ANY(current_setting('oh.entities')::uuid[]) AND product_scope = ANY(current_setting('oh.scopes')::text[]))`; `capacity_snapshot` adds a Cerbos rule that only team leads and HR may read rows for persons other than themselves. Milestones and RAID items stay in the OH4 schema and are referenced by `prj_id`.

## 8. Screen specifications (key screens; common rules of Part 3.5 apply)

**Projects › Portfolio.** Filters: scope (switcher-bound), state, RAG, owner, client. Columns: reference, name, scope badge, client, state, RAG with formula tooltip, milestones due (14 days), budget consumed bar, open high risks, blocked tasks share. Group roles see totals by scope and open a row only when the scope is held; otherwise the row shows "aggregate only". Primary action: Propose project (template picker first). Empty state: "No projects in this scope yet — propose one from a template or convert a won opportunity."

**Projects › Project detail.** Header: reference, name, state chip with allowed transitions, owner, sponsor, entity and scope badges, RAG, client (link to Client 360 if scope held), clocks (next milestone, hold duration). Tabs: Overview (formula inputs, checklist with mandatory items locked, next steps), Epics and tasks (board or list toggle), Milestones (OH4 states and acceptance evidence), RAID, Approvals (maker-checker cards), Time and budget (hours by role, burn, retainer balance), Status page (preview, publish with checker, versions, subscribers), Documents (SharePoint links), Team (capacity this sprint), Retrospective. Primary action depends on state (for example "Submit for approval", "Publish status page").

**Projects › Boards.** Kanban columns from the workflow with WIP counters (soft limit amber, hard limit red and blocked); cards show reference, title, assignee avatar, due, dependency and blocked icons, billable flag; drag or keyboard `M` to move with transition validation; swimlane selector. Gantt: rows by epic or task, bars with baseline shadow, dependency arrows, critical path toggle, drag to reschedule showing the propagation preview and a confirmation; keyboard: `Shift+→` moves a day. List: dense table with inline edit on estimate, due, state; bulk edit preview and undo.

**Projects › Sprints.** Planning pane (backlog with estimates; commitment bar against capacity after focus factor), active sprint board, close dialog with carry-over list; team burndown and velocity charts labelled "team metric — not used for appraisal" with a link to `hlp.oh.pm.team_velocity`.

**Projects › Time.** Weekly grid (days × tasks or codes) with 0.25-hour cells, optional timer control, billable toggle per row where the task allows, submit for approval (OH10.12), approval queue for managers, billable export status for finance (period, lines, OH8 reference, locked flag).

**Client portal › Project status.** Branded with the product's pack; shows last updated, RAG with the published explanation, milestone list with states and dates, next steps, "your actions" with due dates and an Accept control for milestones awaiting acceptance (OH4 evidence), recent accepted deliverables, contact; subscribe to digest (consent). No staff names beyond the project lead; no internal items.

**Error and empty states.** Blocked transition: banner naming the rule and the record ("Cannot start: `Data mapping signed off` is not done"); claims gate: the blocked phrase and the register link; expired guest: neutral message with the contact; scope denial: "Not available in your current scope" with the switcher when another scope is held.

## 9. Risks, open items and owner decisions for this phase

| # | Risk or open item | Mitigation or decision | Owner |
|---|---|---|---|
| 1 | Wrapping OH4.3 implementation projects could change OH4 gate semantics or the `ImplementationMilestoneReached` payload | OH4 regression suite is a required check; milestones and RAID stay in the OH4 schema; the event contract is unchanged (Part 6.2) | Engineering lead |
| 2 | Team metrics drifting into individual performance management | No person-grain metric exists in the catalogue; appraisal screens carry no OH15 link; `pm.metrics.individual_visibility` is a floor; the employee-fairness review (Part 8.1) runs before merge | HR head, CISO |
| 3 | Time entries used as a monitoring source | Entries are self-reported, timers are user-started, and the monitoring notice lists timesheets as the only effort source (OH10.5, OH10.10) | DPO |
| 4 | Client status pages leaking internal detail | Publication-marked items only, second-person check, claims gate, no staff names beyond the lead, 90-day guest expiry | Delivery leads |
| 5 | Cross-scope dependencies creating hidden data flows | Allowed only within a scope or through `GRP` with both owners' approval; restricted predecessors render as "external dependency (restricted)" | Product heads |
| 6 | Rate cards diverging from the signed OH8 catalogue | Rates are read from the catalogue; `pm/rate_not_in_catalogue` refuses others; monthly export is idempotent per period | Finance |
| 7 | Owner decisions pending: product-scope assignments (Appendix B decision 20), remote-work model inputs for capacity (decision 22) | Defaults: no assignments beyond seeds; focus factor 70% | Owner |
