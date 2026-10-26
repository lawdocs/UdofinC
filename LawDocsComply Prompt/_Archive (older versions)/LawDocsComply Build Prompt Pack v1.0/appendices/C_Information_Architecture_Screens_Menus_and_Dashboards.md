# Appendix C — Information Architecture, Screens, Menus and Dashboards (binding)

> LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Owner: S12 (P02); consumed by every phase. Menus are **data** (`cfg.nav_items`, P02 FR-P02-60); each leaf maps to a screen ID owned by a phase. Precedence: this appendix governs shells, menus, navigation, Work Inbox, search, palette, dashboards and widget catalogue; phase files govern the content of their own screens.

---

## C.0 Design principles (R-023, R-028, R-030, R-032, NN-21)

1. **Role-first home.** Every user lands on a dashboard built for their role (C.5) with their next actions on top — no user starts from a blank module list.
2. **Three-click rule.** Any routine action (submit evidence, approve, assign, open a due item, upload a document, ask Vidhi) is reachable in ≤ 3 interactions from home, the Work Inbox or the command palette; statutory deadlines are visible on home without a click.
3. **One inbox.** All actionable work (tasks, approvals, mentions, messages, deadlines, requests, alerts) is in the **Work Inbox**; regulatory content is in **Updates** (NN-27). No module keeps a private "to-do" list.
4. **Automation before forms.** Pre-fill from APIs (PAN/CIN/GSTIN, P01), from Finbyx/Udofin/Tally data (P18, P11), from previous periods (copy last period's evidence description), from HRMS (people), and from documents (Vidhi extraction, P07). Users confirm rather than type.
5. **Explain everything.** Every module title, menu label, column heading, status and regulatory term has an "i" button (`hlp.<key>`, P23) giving plain-language meaning, an example and a link to the tutorial; the glossary is searchable from the palette.
6. **Minimal, calm UI.** Clean white surfaces, navy primary, generous spacing (4-pt grid), one primary action per view, no decorative motion; dense tables available as a "Compact" density toggle for power users.
7. **Accessible by default.** WCAG 2.2 AA is a release gate (NN-21): keyboard paths for every action, visible focus, ≥ 24×24 px targets (SC 2.5.8), drag alternatives (SC 2.5.7), no information by colour alone, captions/transcripts for every video, screen-reader-tested charts with table alternatives, accessible authentication (SC 3.3.8; passkeys/OTP paste allowed), redundant entry avoided (SC 3.3.7).
8. **Same patterns everywhere.** Lists, detail pages, drawers, approvals, imports and exports use the pattern library (C.7) so a user who learns one module knows all.
9. **Multi-entity awareness.** The context bar always shows tenant → legal entity (and period where relevant); switching context never loses unsaved work; actions confirm the entity in the confirmation text ("Submit for **ABC Finance Ltd** · Q2 FY26-27").
10. **Indian-first conventions.** INR with Indian digit grouping (₹ 12,34,567.00), dd-MMM-yyyy dates, financial year notation FY26-27 (April–March), IST with the viewer's zone shown when different (IFSCA and foreign users), Hindi and other Indian-language UI packs (P23).

---

## C.1 Shell catalogue

| Shell | App | Host | Users | Purpose |
|---|---|---|---|---|
| `tenant` | `apps/web` | `app.lawdocscomply.com` (or `<tenant>.lawdocscomply.com` / custom domain) | All tenant roles, delivery staff acting in a tenant under grant, external auditors and supervisor view (restricted shell variant `assurance`) | The client workspace |
| `assurance` | `apps/web` (restricted) | same host, `/assurance` | `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor`, `ten_supervisor_view` | Read-only scoped workspace with evidence request portal and watermarked exports (D-12) |
| `board` | `apps/web` (simplified) | same host, `/board` | `ten_board_member`, `ten_committee_member` | Board portal: meetings, packs, resolutions, disclosures, personal compliance (DIN KYC, MBP-1, DIR-8), voting on circular resolutions |
| `selfservice` | `apps/web` | `/me` | `ten_employee` (HRMS-only users), `coop_member` | Payslips, leave, attendance, declarations, policy acknowledgements, POSH complaint entry (sealed), member services for co-operatives |
| `console` | `apps/console` | `console.lawdocscomply.com` (IP-restricted, phishing-resistant MFA) | `plt_*` roles | Platform super-admin, content operations, regulatory monitor, pricing, tenants, corrections, security |
| `delivery` | `apps/delivery` | `delivery.lawdocscomply.com` | `dlv_*` roles | Service Delivery Console for LawDocs RMs and professionals (D-03) |
| `public` | `apps/public` | `www.lawdocscomply.com` | `anon`, `lead`, `mkp_buyer` | Marketing site, pricing configurator, free health check, public marketplace, academy listings, help centre, blog |
| `provider` | `apps/public` (authenticated area) | `www…/provider` | `mkp_provider_admin`, `mkp_professional` | Marketplace provider workspace (listings, engagements, payouts) |

CRM, marketing, staff HRMS, payroll and group billing are in the **Infrabyx Operations Hub** (separate app; Appendix X); LDC shells link to it for staff with OH accounts but never embed OH data in tenant shells.

## C.2 Shell anatomy (web)

| Region | Content |
|---|---|
| Top bar (56 px) | Logo (tenant brand), **context switcher** (tenant → legal entity; period selector on period-scoped pages), global search (`Ctrl/Cmd+K`), **Ask Vidhi** (`Ctrl/Cmd+J`), Updates bell (regulatory, with count of unacknowledged critical), Notifications/Work Inbox badge, Help ("?" and tutorials), profile (preferences, accessibility, sign out) |
| Left rail (240 px → 72 px collapsed; remembers state) | Primary navigation (C.3) with icons + text labels (icons never alone), entitlement-aware, terminology-aware; "Explore" section shows unlicensed modules when the tenant enables upsell display |
| Main area | Page header (title + "i", breadcrumb, primary action, secondary actions menu), filters bar, content; max readable width 1,440 px for forms, full width for tables |
| Right context panel (400 px, optional, dockable) | Vidhi chat with sources; activity/timeline; related items (circulars, policies, previous period); details drawer |
| Footer (32 px) | Version, environment badge (sandbox in amber), status page link, accessibility statement, support |
| Banners | Sandbox mode, support session active (NN-30), trial days left, payment past due, maintenance, "Changes made by LawDocs" (unseen corrections) |

Responsive: ≥ 1,280 px full layout; 768–1,279 px rail collapses and right panel becomes overlay; < 768 px approvals-first mobile layout (Work Inbox, calendar, evidence upload from camera, Vidhi chat, document preview). Native apps are deferred (D-01); the web app is an installable PWA with push notifications.

---

## C.3 Complete menu trees

Legend: **[E]** shown only if the module is entitled (P20); **[F:x]** shown only for entity families x; **(L)** cannot be hidden; leaf → screen ID (owning phase).

### C.3.1 Tenant shell (`apps/web`) — full tree for `ten_admin`

```
Home (role dashboard) ............................................. SCR-RPT-01 (P04/C.5) (L)
Work Inbox ........................................................ SCR-WF-00 (P04) (L)
Updates (regulatory) .............................................. SCR-CHG-01 (P05) (L)
  ├ All updates · Critical · By regulator · By entity family · Acknowledgements due
Calendar .......................................................... SCR-WF-10 (P04)
  ├ My calendar · Department calendar · Compliance calendar · Meetings · Returns · Subscriptions (ICS / M365 / Google)
Compliance [E]
  ├ My compliances ................................................ SCR-CMP-01
  ├ Compliance register (all obligations; list / timeline / month) SCR-CMP-02
  ├ By regulator · By department · By legal entity ............... SCR-CMP-03
  ├ Instrument catalogue (add / remove directions, regulations) ... SCR-CNT-10 (P03)
  ├ Question bank & our changes (tenant overlays, audit) ......... SCR-CNT-12 (P03)
  ├ Upload a direction (AI-drafted questions, tenant only) ....... SCR-CHG-20 (P05)
  ├ Excel import / export ........................................ SCR-TPL-01 (P03)
  ├ Attestations & certifications ................................ SCR-CMP-08
  ├ Exceptions, waivers & not-applicable decisions ............... SCR-CMP-09
  ├ Compliance health score ....................................... SCR-CMP-10
  └ Compliance reports ............................................ SCR-CMP-11
Governance [E]
  ├ Company & legal entities (profile, CIN, registrations, licences) SCR-GOV-01 (P06)
  ├ Board & directors · KMP · Shareholding / members ............. SCR-GOV-02..04
  ├ Committees .................................................... SCR-GOV-05
  ├ Meetings (board, committee, general, circular resolutions) ... SCR-GOV-06
  ├ Minutes & minute books ......................................... SCR-GOV-07
  ├ Resolutions library ............................................ SCR-GOV-08
  ├ Statutory registers ............................................ SCR-GOV-09
  ├ MCA / ROC filings ............................................... SCR-GOV-10
  ├ Listed company (LODR, PIT, SAST, disclosures) [F:SEBI-LISTED, SEBI-REIT-INVIT] SCR-GOV-20
  ├ Fit & proper, declarations, related parties ................... SCR-GOV-12
  ├ Board portal settings .......................................... SCR-GOV-15
  └ Co-operative affairs [F:COOP-*] (members, general body, elections, office bearers) → P16 SCR-COOP-*
Policies [E] ...................................................... SCR-POL-01 (P07)
  ├ Policy register · Reviews due · Model templates · Acknowledgements · Drafting with Vidhi
Documents (DMS) ................................................... SCR-DMS-01 (P07)
  ├ All documents · Evidence vault · Shared with me / by me · Folder intake · Signatures · Translations & type copies · Retention & legal hold
Risk [E]
  ├ Risk register · RCSA · KRIs · Incidents & loss events · Issues & actions · Risk appetite · Controls library · Risk reports  (P08)
Risk Lab [E]
  ├ Capital & ratios · ICAAP · Stress tests · Scenario library · Liquidity & ALM · Investment limits [F:RBI-NBFC-ICC, …] · Model inventory  (P09)
Audit [E]
  ├ Audit universe · Annual plan · Engagements · Workpapers · Findings · Audit reports · Auditor access  (P10)
Returns & Filings [E]
  ├ Return calendar · Return Studio runs · Data sources & imports (Tally, Excel, Finbyx, Udofin, other LMS) · CIC submissions · GST & TDS · Filing evidence & acknowledgements  (P11)
Data Protection & Cyber [E]
  ├ Data inventory (RoPA) · Notices & consents · Data-principal requests · DPIA · Breaches & cyber incidents · Security controls (ISMS) · Vendors & outsourcing (TPRM) · Cyber returns  (P12)
People & Labour [E] (also sold standalone; R-014)
  ├ Employees · Org chart & departments · Attendance · Leave · Payroll · Labour registers · Labour returns · Committees (IC under POSH, works committee, grievance redressal committee, safety) · Employment agreements · Self-service settings  (P13)
Grievance & Support [E]
  ├ Support tickets · Grievances · GRO desk · Internal Ombudsman [F:where required] · External forum cases · Website & app widget · Grievance analytics  (P14)
Vidhi AI
  ├ Ask Vidhi · Knowledge notebooks · Agents & scheduled tasks · Drafts awaiting review · AI usage  (P17)
Reports & MIS
  ├ Report library · Board pack builder · Dashboards · Scheduled reports · Savings & value (P20) · Exports  (P04/P06/P20)
Services & Academy
  ├ My engagements & retainers · Buy services (marketplace) · Courses (FinLegal Academy)  (P21)
Integrations [admin]
  ├ Connected systems · API keys & webhooks · Data sharing (ecosystem consents) · Storage destinations (BYO)  (P18/P19)
Settings (L for admin) ............................................. SCR-CFG-01 (P02)
  ├ Organisation · Users & roles · Workflow · Data & forms · Notifications · Dashboards · Navigation · Branding · Rules & packs · Billing & plan (P20) · Security · Data export & exit (P19) · Account (Changes made by LawDocs, support access)
Help & Learning (L) ............................................... SCR-HLP-01 (P23)
  ├ Getting started · Tutorials & videos · Glossary · What's new · Contact support
```

### C.3.2 Role trimming (tenant shell)

| Role | Sees | Notes |
|---|---|---|
| `ten_maker` | Home, Work Inbox, Updates, Calendar, Compliance (My compliances, register read), Documents, modules where assigned, Vidhi, Help, personal Settings | Department scope by default |
| `ten_checker` | Maker set + review queues, exceptions (read), reports for own departments | — |
| `ten_dept_head` | Checker set + department dashboards, department settings (delegated), assignment, risk/audit items of department | — |
| `ten_cco` | All compliance, Updates acknowledgements, policies, governance (read), risk (read), audit findings (read), reports, configuration of compliance workflows | Default tenant legal reviewer |
| `ten_kmp` (CEO/MD) | Executive dashboard, all modules read, approvals routed to them, board pack | — |
| `ten_kmp` CFO | Risk Lab capital & ratios, Returns & Filings, GST & TDS, investment limits, Finance department compliance | — |
| `ten_kmp` CRO | Risk, Risk Lab (full), KRIs, incidents, outsourcing risk, ICAAP | — |
| `ten_kmp` CCrO (Chief Credit Officer) | Credit-related compliance, credit risk dashboards, concentration, NPA trends (from Finbyx), CIC submissions status | — |
| `ten_kmp` CS | Governance (full), meetings, minutes, registers, MCA filings, LODR | — |
| `ten_kmp` CISO / CTO / CIO | Data Protection & Cyber, IT compliance, IS audit findings, incidents | — |
| `ten_kmp` DPO | Data protection (full), DSR queue, breaches, DPIA | — |
| `ten_kmp` GRO / PNO / IO | Grievance & Support (full or IO-scoped) | IO sees only escalated items |
| `ten_hr_admin` | People & Labour (full), POSH IC only if also `ten_ic_member` | Payroll split: `ten_payroll_maker` / `ten_payroll_checker` |
| `ten_ic_member` | POSH IC sealed workspace only (+ own self-service) | NN-13 |
| `ten_internal_auditor` | Audit (full), read of all audited modules, evidence | Independent of audited functions |
| `ten_board_member` / `ten_committee_member` | `board` shell | — |
| external auditors, `ten_supervisor_view` | `assurance` shell | D-12 |
| `ten_viewer` | Home (viewer), reports shared with them | — |

### C.3.3 Board shell (`/board`)

```
Board home (next meeting, packs to read, items to sign/vote, personal compliance) · Meetings (upcoming, past, minutes to approve) · Board packs (secure viewer, annotations private to the director) · Circular resolutions (vote with eSign) · Disclosures (MBP-1, DIR-8, interests, related parties; annual declarations) · My compliance (DIN KYC due date, trainings, independence declarations for IDs) · Committee spaces · Resolutions library (read) · Dissent log · Regulator correspondence (read, where shared) · Help
```

### C.3.4 Assurance shell (`/assurance`)

```
Engagement home (scope, validity, contacts) · Evidence requests (PBC list; request, receive, comment) · Read-only registers within scope (compliance register, policies, minutes, registers, risk, audit, returns, grievance stats) · Sampling workspace (P10) · Exception reports · Downloads (watermarked PDF only; export level per grant) · Access log (own)
```

### C.3.5 Self-service shell (`/me`)

```
My home · Payslips & tax documents · Leave · Attendance & regularisation · Declarations (investment, nomination) · Policies to acknowledge · Trainings · My documents · Raise a concern (POSH complaint → sealed IC workspace; whistle-blower → sealed vigil mechanism) · Co-operative member services [F:COOP] (my shares, my loans view from Finbyx/Udofin link, general-body notices, elections, complaints)
```

### C.3.6 Settings menu (tenant; detailed sections)

```
Organisation: Company profile · Legal entities · Departments & functions · Terminology · Business calendars & holidays · Financial year
Users & access: Users · Roles & permissions · Delegations · Groups & pools · External access grants · Support access · SSO / SCIM
Workflow: Workflow designer · Status sets · Waiting-on parties & chase policies · Reason codes · SLA & escalation ladders · Assignment rules
Data & forms: Custom fields · Forms · Saved views (official) · Import mappings
Notifications: Templates · Channel policy & quiet hours · Digests · Updates preferences (separate block)
Dashboards: Role defaults · Department defaults · Widgets
Navigation: Menu & landing pages · Shortcuts
Branding: Logo & colours · Letterhead & PDF · Domains & email sender
Rules & packs: Setting packs · Rule packs (adopted, pinned, adapted) · Golden cases & sandbox · Configuration health
Billing & plan (P20): Plan & components · Seats & usage · Invoices & payments · Payment methods · Promo codes applied · Savings & value
Security: Password & MFA policy · Sessions · IP allow-list · Data residency · Encryption keys (BYOK where entitled) · Audit log viewer
Data export & exit (P19): Exports · Storage destinations (BYO) · Retention & legal holds · Exit plan
Integrations (P18): Connected systems · API keys · Webhooks · Ecosystem data sharing
Account: Changes made by LawDocs · Support access · Close account
My preferences: Language · Accessibility · Notifications · Quiet hours · Digest time · Calendar sync · Delegation / away
```

### C.3.7 Console shell (`apps/console`)

```
Home (platform health, content pipeline, scan freshness, tenants at risk, open corrections, security alerts)
Tenants: Directory · Tenant 360 (profile, entitlements, settings override → Correction Entry, users count, usage, health score, billing) · Trials · Onboarding pipeline
Content: Sources & authorities · Instruments & versions · Question banks · Excel templates registry (Appendix E) · AI question drafting · Releases (maker/checker/publisher) · Tenant overlay analytics (anonymised counts) · Glossary & help content
Regulatory monitor (P05): Source health & freshness · Today's scan (20:00 IST) · Triage queue · Published updates · Broadcasts
Rules & config: Platform settings & bounds · Rule packs · Setting packs · Feature flags · Emergency blocks
Commercial (P20): Pricing catalogue · Components & add-ons · Plans & comparison table · Discounts & promo codes · Trials policy · Revenue streams (switches) · Tax settings
Marketplace (P21): Providers & verification · Services catalogue · Categories · Commercial switches by profession (D-06) · Disputes · Payout batches · Academy links
Corrections: Requests · Emergency overrides · Log
Security: Break-glass · Support sessions · Access reviews · Key management · Vulnerabilities & VAPT findings (P24)
Engineering (P24): Releases & change records · Backups & restore tests · Incidents · Status page
Assurance: Certification evidence (SOC 2 / ISO / PCI readiness) · Platform audit log · Claims register (NN-19)
Analytics: Product usage · Funnel (health check → trial → paid) · Content coverage
```

### C.3.8 Delivery shell (`apps/delivery`)

```
Home (my clients' risk heat: overdue, due this week, waiting on client, SLA of retainer deliverables)
My clients (portfolio list with health, plan, retainer status)
Client workspace (per client; opens the tenant in delivery mode under grant)
  ├ Overview · Compliance work (as maker) · Returns & filings work · Deliverables · Meetings & minutes support · Messages (secure thread with client) · Shared drive link (OneDrive / SharePoint / Google Drive) · Credential vault (D-04) · Billing & invoices (synced) · Tickets · Engagement terms & SLA
Queues (team work by type and SLA) · Calendar (all assigned clients) · Effort log (time per client/engagement) · Templates & precedents · Knowledge (Vidhi notebooks for staff) · Link to Operations Hub (CRM, HR)
```

### C.3.9 Public shell (`apps/public`)

```
Mega-menu:
Product: Compliance management · Regulatory change & updates · Governance & company secretarial · Risk management & Risk Lab (ICAAP, stress testing) · Audit management · Returns & filings · Data protection & cyber · People & labour compliance (HRMS) · Grievance redressal · Vidhi AI · Integrations & API
Solutions (by entity): NBFCs (by layer & type) · Banks & SFBs · Urban co-operative banks · Credit co-operative societies & other co-operatives · ARCs · IFSCA entities · Listed companies · Mutual funds & AIFs · REITs & InvITs · Insurers & insurance intermediaries · Private & public companies · LLPs · Fintechs & LSPs
Pricing (configurator) · Free compliance health check · Marketplace (services, professionals) · Academy (FinLegal Academy courses) · Resources: Regulatory updates digest · Blog · Glossary · Tutorials & videos · Help centre · Webinars · Templates (gated)
Company: About · Security & trust · Accessibility statement · Careers · Contact · Partners
CTA: Start free health check · Start 7-day trial · Log in
```
Detailed public page specifications: P23 and Appendix P.

---

## C.4 Global search, command palette and keyboard

### C.4.1 Indexed objects (permission-trimmed; OpenSearch per-tenant aliases; sealed classes never indexed, NN-13)

| Shell | Objects | Fields |
|---|---|---|
| tenant | Compliance instances, obligations/questions (base + overlay), instruments, Updates, tasks, documents (title, tags, OCR text where allowed), policies, meetings, minutes, resolutions, registers entries, risks, KRIs, incidents, audit findings, return runs, grievances (ID and category only for non-GRO roles), employees (name, code, department; for HR roles), vendors, users, settings, help articles, glossary | Title, ID, clause ref, regulator, department, status, owner, dates, tags |
| console | Tenants, instruments, releases, rule packs, settings, corrections, providers, services | — |
| delivery | Assigned clients and their permitted objects | — |
| public | Pages, blog, glossary, help, marketplace listings, courses | — |

Query features: typo tolerance, Indian legal abbreviations synonym list (MD = Master Direction, SBR = Scale Based Regulation, LODR, PIT, KMP, DPDP, RBIA, ICAAP), filters chips, "search within this module", results grouped by type with keyboard navigation; natural-language queries can be sent to Vidhi ("/vidhi which returns are due this week?").

### C.4.2 Command palette (`Ctrl/Cmd+K`)

Commands are registered by modules (`cfg.palette_commands`) with permission checks. Seed commands:

| Command | Action |
|---|---|
| Go to … (any menu leaf) | Navigation |
| New task · Assign task to Vidhi · Schedule a recurring task | P04 / P17 |
| Upload evidence for … (search instance) | P04 |
| Submit / approve next item | Opens next item in inbox order |
| Add a direction to my compliance list | P03 catalogue |
| Upload a new direction (draft questions) | P05 |
| Start a board meeting · Draft minutes for … · Create circular resolution | P06 |
| Draft a policy with Vidhi · Start policy review | P07 |
| Log an incident · Log a loss event · Record KRI value | P08 |
| Run a stress test · Open ICAAP | P09 |
| Raise audit finding · Request evidence (PBC) | P10 |
| Start return run · Import Tally data | P11 |
| Report a data breach · New DSR request | P12 |
| Apply leave · Run payroll (payroll makers) | P13 |
| New grievance · Find grievance by ID | P14 |
| Rename department · Add custom field · Change reminder cadence · Apply setting pack | P02 |
| Export … (scope) | P19 |
| Open help for this page · Search glossary | P23 |
| Switch legal entity · Switch period | Context |

### C.4.3 Keyboard shortcuts (documented on `?`; all remappable; none single-key without a modifier unless the user enables "single-key shortcuts", SC 2.1.4)

`Ctrl/Cmd+K` palette · `Ctrl/Cmd+J` Vidhi · `g h` home · `g i` inbox · `g u` updates · `g c` calendar · `g s` settings · `j/k` next/previous row · `Enter` open · `e` edit · `a` approve (opens confirmation, never approves silently) · `r` return/reject (requires reason) · `u` upload · `/` search in page · `?` shortcut help · `Esc` close drawer.

---

## C.5 Work Inbox

### C.5.1 Item kinds

| Kind | Examples in LDC | Actionable |
|---|---|---|
| `task` | Upload evidence for an instance; prepare return; draft minutes; review policy; respond to PBC request; remediate finding | Yes |
| `approval` | Check a compliance submission; approve NA request; approve tenant overlay; approve G config change; approve policy for committee; approve return; approve payroll; approve export of sensitive scope; Correction Entry (console) | Yes |
| `mention` | "@CFO please confirm the CRAR figure" in a comment | Yes |
| `message` | Client ↔ RM thread; auditor query; committee member comment | Yes |
| `deadline` | Statutory clock at warn offsets; licence/registration renewal; DIN KYC; policy review due | Open |
| `alert` | KRI breach; overdue escalation; integration feed failure (Finbyx data missing); quarantined evidence; trial ending | Yes |
| `request` | Access request; external auditor evidence request; delegation request; "request change" on a locked setting | Yes |

Updates (regulatory) are **not** inbox items; critical Updates that need acknowledgement create a `task` ("Acknowledge and assess RBI update …") linked to the Update (NN-27).

### C.5.2 Ordering, priority, actions

- Priority P1 (statutory deadline ≤ 24 h or breached; security alert), P2 (SLA amber/red, approval blocking others, due ≤ 3 working days), P3 (normal), P4 (FYI).
- Default order: `(legal_blocking DESC, sla_state DESC, due_at ASC NULLS LAST, priority ASC, created_at ASC)`; user can sort by newest/source; default returns each visit.
- Opening an item loads the owning module's decision panel in a drawer (no page change); actions call the owning engine with `If-Match`; stale items reload ("This changed since you opened it").
- **Bulk:** mark read, snooze, reassign, mark tasks done. **Bulk approve only for `bulk_approvable` sources** (Low-risk T content reviews, leave, attendance regularisations); never for compliance checks of High/Medium risk, G changes, money, privileges, sensitive exports (supersedes the owner's baseline "bulk approve available" for checkers). A **"Review next"** button gives checkers fast sequential review instead.
- Snooze: not for P1; P2 not past `due_at − 24 h`; max 3 snoozes.
- Away & delegation: per P02 FR-P02-52; delegated items show "On behalf of {delegator} until {date}".
- Unassigned approvals escalate to the next authority level.

### C.5.3 Notification centre and digests

Bell shows Notifications (work) and links to Inbox; Updates have their own icon. Channels by priority (P1 immediate in-app/push/email; P2 immediate in-app/push, email digest; P3 in-app, daily digest; P4 in-app only). Daily work digest 08:30 (user time); daily regulatory digest 20:30 IST after the 20:00 scan; weekly management digest Monday 08:30 for KMPs. Quiet hours narrow-only (default 21:00–08:00). De-duplication per object per 15 minutes.

---

## C.6 Dashboards, widget catalogue and next-best action (R-012, R-059, R-030)

### C.6.1 Widget catalogue (`cfg.widget_catalogue`; seed)

Every widget: title + "i" help; server-computed values only; drill-down to the filtered list; export PNG/CSV/XLSX; accessible table alternative ("View as table"); period and legal-entity filters inherit from the context bar; refresh interval shown ("Updated 10:42"). Widgets reading Finbyx/Udofin data show source and as-of date ("Source: Finbyx, as of 24-Oct-2026 23:00") and a stale badge if older than the feed SLA.

| Code | Widget | Module | Typical roles |
|---|---|---|---|
| W-CMP-01 | Compliance score ring (0–100; canonical statuses, weighted by risk) with per-regulator segments | cmp | CCO, CEO, MD, Board, dept head |
| W-CMP-02 | **Overdue statutory items** (count + list, P1 first) | cmp | CCO, dept head, Board, CEO (mandatory) |
| W-CMP-03 | Due in next 7 / 30 days | cmp | maker, checker, dept head, CCO |
| W-CMP-04 | My compliances by status (kanban mini) | cmp | maker |
| W-CMP-05 | Awaiting my check (count, oldest age, SLA) | cmp/wf | checker |
| W-CMP-06 | Department compliance heatmap (dept × regulator) | cmp | CCO, CEO, Board |
| W-CMP-07 | Trend: on-time % (30/60/90 days, FY) | cmp | CCO, CEO, Board |
| W-CMP-08 | Waiting on others (by party type, age) | cmp | dept head, CCO, RM |
| W-CMP-09 | Exceptions & NA decisions pending | cmp | CCO |
| W-CMP-10 | Rework rate & returns by checker | cmp | dept head, CCO |
| W-CMP-11 | Penalty exposure (indicative; from penalty rule packs; "not legal advice") | cmp/bil | CCO, CFO, CEO, Board |
| W-CHG-01 | **Critical regulatory updates to acknowledge** | chg | CCO (mandatory), dept head |
| W-CHG-02 | Updates by regulator this week | chg | CCO, CS, CEO |
| W-CHG-03 | "What changed" — obligations changed vs previous direction | chg | CCO, dept head |
| W-WF-01 | My tasks (today / week / overdue) | wf | all |
| W-WF-02 | My calendar (next 7 days) | wf | all |
| W-WF-03 | Team workload (open items per person, ageing) | wf | dept head |
| W-WF-04 | Approvals awaiting me | wf | all approvers |
| W-WF-05 | Escalations raised (L1–L3) | wf | dept head, CCO, CEO |
| W-GOV-01 | Next board / committee meetings (notice, papers, quorum status) | gov | CS, Board, CEO |
| W-GOV-02 | Minutes clocks (draft circulation, entry) | gov | CS |
| W-GOV-03 | MCA / ROC filings due & filed | gov | CS, CFO |
| W-GOV-04 | Director compliance (DIN KYC, DIR-8, MBP-1, independence declarations) | gov | CS, Board |
| W-GOV-05 | LODR disclosure clock (events awaiting disclosure; 24 h / 30 min clocks per regulation) [F:listed] | gov | CS, CFO |
| W-GOV-06 | Board action-taken report (open decisions) | gov | Board, CEO, MD |
| W-GOV-07 | Related-party transactions awaiting approval | gov | CS, CFO, Audit Committee |
| W-POL-01 | Policies due for review / overdue | pol | CCO, policy owners, Board |
| W-POL-02 | Acknowledgement coverage % | pol | HR, CCO |
| W-RSK-01 | Enterprise risk heatmap (inherent vs residual; 5×5 default) | erm | CRO, CEO, Board, RMC |
| W-RSK-02 | **KRIs in breach** (red/amber vs appetite) | erm | CRO (mandatory), CEO |
| W-RSK-03 | Top 10 risks with trend arrows | erm | CRO, Board |
| W-RSK-04 | RCSA progress by department | erm | CRO, dept head |
| W-RSK-05 | Incidents & loss events (count, amount, by Basel event type) | erm | CRO, CISO |
| W-RSK-06 | Risk acceptances expiring | erm | CRO |
| W-RAL-01 | Capital adequacy (CRAR, Tier 1, vs regulatory minimum and internal buffer) | ral | CFO, CRO, CEO, Board |
| W-RAL-02 | Liquidity (LCR where applicable; structural liquidity buckets; cumulative mismatch limits) | ral | CFO, CRO, ALCO |
| W-RAL-03 | Asset quality (GNPA, NNPA, PCR, SMA buckets — sourced from Finbyx/LMS) | ral | CCrO, CRO, CFO, Board |
| W-RAL-04 | Concentration (single/group borrower, sector, top 20) vs limits | ral | CCrO, CRO |
| W-RAL-05 | Stress test results (latest; baseline/adverse/severe; capital after stress) | ral | CRO, CFO, Board |
| W-RAL-06 | ICAAP status and capital planning headroom | ral | CRO, CFO |
| W-RAL-07 | Investment limits (exposure to capital market, AIF investments, single-entity caps) [F:ICC, investment entities] | ral | CFO, CIO |
| W-RAL-08 | Financial ratio panel (configurable: ROA, ROE, NIM, cost-to-income, leverage, NOF, debt-equity) | ral/acc | CFO, CEO, Board |
| W-RAL-09 | ALM gap chart | ral | CFO, ALCO |
| W-AUD-01 | Audit plan progress | aud | IA, Audit Committee |
| W-AUD-02 | **Open findings by severity and age** | aud | IA (mandatory), CEO, Audit Committee |
| W-AUD-03 | Overdue remediation (repeat findings flagged) | aud | IA, dept head |
| W-AUD-04 | Evidence requests (PBC) status | aud | IA, external auditor, CCO |
| W-RET-01 | Returns due / prepared / submitted / acknowledged (this period) | ret | CFO, CCO, returns team |
| W-RET-02 | Data feed health (Finbyx, Udofin, Tally, Excel) | ret/int | CFO, returns team, CTO |
| W-RET-03 | CIC submission cycles (accepted/rejected records, DQ index) | ret | CCrO, CFO |
| W-RET-04 | GST & TDS due dates and status | ret | CFO |
| W-DPC-01 | Data-principal requests (open, SLA) | dpc | DPO |
| W-DPC-02 | **Incident clocks** (CERT-In 6 h; DPDP Board report; regulator cyber reporting) | dpc | CISO (mandatory), DPO |
| W-DPC-03 | Control effectiveness (ISMS controls tested, failing) | dpc | CISO |
| W-DPC-04 | Vendor risk (critical vendors, overdue assessments, outsourcing register gaps) | tpr | CISO, CRO, CCO |
| W-DPC-05 | VAPT / IS audit open items | dpc/aud | CISO, CTO |
| W-HR-01 | Headcount and attrition (by department, location) | hr | HR, CEO |
| W-HR-02 | Labour compliance calendar (registers, returns, contributions) | lab | HR, CCO |
| W-HR-03 | Payroll run status (maker/checker/disbursal file) | hr | HR, payroll roles, CFO |
| W-HR-04 | Leave & attendance exceptions | hr | HR, dept head |
| W-HR-05 | People-risk indicators (key-person dependency, vacancies in KMP roles, training overdue) | hr/erm | HR, CRO |
| W-HR-06 | POSH IC: count of open cases and clock status only (no details; sealed) | lab | IC presiding officer only |
| W-GRV-01 | **Grievances breaching / near breach** | grv | GRO (mandatory), PNO, CCO |
| W-GRV-02 | Grievance volume by category / channel / product | grv | GRO, CEO, Board |
| W-GRV-03 | External forum cases (Ombudsman, SCORES, Bima Bharosa) | grv | GRO, CCO |
| W-GRV-04 | Support tickets (open, first response SLA) | grv | support agents |
| W-AI-01 | Vidhi drafts awaiting review | ai | all |
| W-AI-02 | Scheduled agent runs & results | ai | admins, CCO |
| W-BIL-01 | Plan, usage, seats, next invoice | bil | `ten_admin` |
| W-BIL-02 | Savings & value (hours saved, penalties avoided — indicative, with method) | bil | `ten_admin`, CEO, CFO |
| W-ADM-01 | Users & roles changes (last 30 days); pending invites | iam | `ten_admin` |
| W-ADM-02 | Integration health | int | `ten_admin`, CTO |
| W-ADM-03 | Configuration health | cfg | `ten_admin` |
| W-ADM-04 | Security alerts (failed logins, new devices, MFA gaps) | iam | `ten_admin`, CISO |
| W-SUP-01 | Supervisor view: scope summary & what's included (read-only banner) | core | `ten_supervisor_view` (mandatory) |
| W-DLV-01 | Client portfolio health (per client: overdue, due this week, waiting on client) | sdc | `dlv_rm`, `dlv_lead` |
| W-DLV-02 | Retainer SLA tracker (deliverables due, hours used vs allowance) | sdc | `dlv_rm`, `dlv_lead` |
| W-PLT-01 | Scan freshness & failed sources | chg | content team, `plt_super_admin` |
| W-PLT-02 | Content pipeline (drafting, maker, checker, scheduled) | cnt | content team |
| W-PLT-03 | Tenants: trials, conversions, at-risk | bil | `plt_super_admin` |
| W-PLT-04 | Open corrections & emergency overrides | core | `plt_super_admin`, security |
| W-PLT-05 | Platform SLOs, incidents, backup status | eng | `plt_super_admin`, security |

### C.6.2 Default layouts per role (row 1 → row 3; **bold** = mandatory, cannot be hidden)

| Role | Row 1 | Row 2 | Row 3 | Quick actions (header) |
|---|---|---|---|---|
| Maker (`ten_maker`) | **W-WF-01 My tasks**, W-CMP-03 Due 7 days | W-CMP-04 My compliances by status, W-WF-02 Calendar | W-AI-01 Vidhi drafts, W-CHG-03 What changed (my departments) | + Upload evidence · + New task · Ask Vidhi |
| Checker (`ten_checker`) | **W-CMP-05 Awaiting my check**, W-WF-04 Approvals | W-CMP-10 Rework & returns, W-CMP-03 Due 7 days | W-WF-02 Calendar | Review next · Ask Vidhi |
| Department head / VP | **W-CMP-02 Overdue (dept)**, W-WF-03 Team workload | W-CMP-08 Waiting on others, W-WF-05 Escalations | W-RSK-04 RCSA progress, W-AUD-03 Overdue remediation | Assign · Reassign · Dept report |
| CCO | **W-CMP-02 Overdue**, **W-CHG-01 Critical updates**, W-CMP-01 Score | W-CMP-06 Dept heatmap, W-CMP-07 Trend, W-CMP-11 Penalty exposure | W-CMP-09 Exceptions, W-POL-01 Policies due, W-GRV-01 Grievance breaches | Board compliance report · Acknowledge updates · Ask Vidhi |
| CEO | W-CMP-01 Score, **W-CMP-02 Overdue**, W-RSK-02 KRIs | W-RAL-01 Capital, W-RAL-03 Asset quality, W-RSK-01 Heatmap | W-GOV-06 Board action-taken, W-AUD-02 Findings, W-GRV-02 Grievance volumes | Executive summary PDF · Ask Vidhi |
| MD / WTD | As CEO + W-GOV-01 Next meetings | W-RAL-08 Ratio panel | W-HR-05 People risk | — |
| CFO | **W-RAL-01 Capital**, W-RET-01 Returns, W-RET-04 GST & TDS | W-RAL-08 Ratio panel, W-RAL-02 Liquidity, W-RAL-09 ALM gap | W-RAL-07 Investment limits [F], W-GOV-03 MCA filings, W-HR-03 Payroll | Start return run · Import Tally · Ratio report |
| CRO | **W-RSK-02 KRIs in breach**, W-RSK-01 Heatmap | W-RAL-05 Stress tests, W-RAL-06 ICAAP, W-RSK-05 Incidents & losses | W-RSK-06 Acceptances expiring, W-DPC-04 Vendor risk, W-HR-05 People risk | Run stress test · Log incident · RMC report |
| CCrO (Chief Credit Officer) | W-RAL-03 Asset quality, W-RAL-04 Concentration | W-RET-03 CIC submissions, W-CMP-02 Overdue (credit) | W-GRV-02 Grievances (credit products) | Credit risk report |
| CS | **W-GOV-01 Next meetings**, W-GOV-02 Minutes clocks | W-GOV-03 MCA filings, W-GOV-04 Director compliance | W-GOV-05 LODR clock [F:listed], W-GOV-07 RPTs | Create meeting · Draft minutes · New circular resolution |
| CISO / CTO / CIO | **W-DPC-02 Incident clocks**, W-DPC-03 Controls | W-DPC-05 VAPT/IS audit, W-DPC-04 Vendor risk | W-RET-02 Data feed health, W-ADM-04 Security alerts | Log incident · Control test |
| DPO | **W-DPC-01 DSR queue**, **W-DPC-02 Incident clocks** | W-DPC-04 Vendors (processors) | W-POL-02 Acknowledgements (privacy policies) | New DSR · Report breach · DPIA |
| GRO / PNO | **W-GRV-01 Breaching**, W-GRV-03 External forum | W-GRV-02 Volumes, W-GRV-04 Tickets | W-WF-01 Tasks | New grievance · Find by ID |
| Internal Ombudsman | **W-GRV-01 (IO-escalated only)** | — | — | Review next |
| HR admin | W-HR-02 Labour calendar, W-HR-03 Payroll | W-HR-01 Headcount, W-HR-04 Exceptions | W-POL-02 Acknowledgements, W-HR-05 People risk | Run payroll · Add employee · Labour register |
| Internal auditor | **W-AUD-02 Open findings**, W-AUD-01 Plan progress | W-AUD-03 Overdue remediation, W-AUD-04 PBC status | W-CMP-07 Compliance trend | Raise finding · Request evidence |
| External / secretarial / IS auditor (assurance) | W-AUD-04 PBC status (own) | Scope summary | Downloads | Request evidence |
| Board member | **W-CMP-02 Overdue statutory**, W-GOV-01 Next meeting & pack | W-CMP-01 Score, W-RSK-01 Heatmap, W-RAL-01 Capital | W-GOV-04 My director compliance, W-GOV-06 Action-taken | Open board pack · Vote on circular resolution |
| Supervisor view | **W-SUP-01 Scope summary** | Read-only registers within scope | Access log | — |
| `ten_admin` | W-ADM-01 Users, W-BIL-01 Plan & usage | W-ADM-03 Config health, W-ADM-02 Integrations | W-BIL-02 Savings, W-ADM-04 Security | Invite user · Apply setting pack · Settings |
| `plt_super_admin` | W-PLT-03 Tenants, W-PLT-04 Corrections | W-PLT-05 Platform health, W-PLT-01 Scan freshness | W-PLT-02 Content pipeline | Tenant 360 · New correction |
| Content team (`plt_content_*`) | **W-PLT-01 Scan freshness**, W-PLT-02 Pipeline | Triage queue | Releases scheduled | Triage next · Draft questions |
| RM (`dlv_rm`) | **W-DLV-01 Portfolio health**, W-DLV-02 Retainer SLA | W-CMP-08 Waiting on client (all clients) | W-WF-02 Calendar (all clients) | Open client · Message client |
| Employee (self-service) | Payslip, leave balance | Policies to acknowledge, trainings | Holiday calendar | Apply leave · Raise concern |
| Co-operative office bearer | General body / committee meetings, election calendar | Compliance due (registrar returns, audit) | Member complaints | Notice to members |

Entity-family packs (P02 §4N) swap widgets: e.g., UCB packs replace W-RAL-02 with UCB liquidity widgets; co-operative packs hide W-RAL-01 if not applicable and show registrar-return widgets; listed packs show W-GOV-05.

### C.6.3 Personalisation rules

Users may add, remove (except mandatory), resize (S/M/L/XL grid), reorder, set filters, pin a saved view as a widget, and create up to 5 personal dashboards; tenant admins publish role and department defaults and lock widgets; "Reset to role default" always available. KMPs can choose "Board view" (simplified, larger type) for presenting. Dashboards export to PDF/PPTX-ready images for board packs (P06) with source and as-of footers.

### C.6.4 Next-best action (deterministic; `cfg.nba_rules`)

Rules (never AI-decided) surface one primary suggestion card on home, e.g.: "3 items due tomorrow are not started — Open"; "RBI update needs your acknowledgement — Review"; "Return X data from Finbyx not received — Chase"; "Board meeting in 9 days: notice not issued (7-day rule) — Issue notice"; "Policy Y review overdue by 12 days — Start review"; "KRI 'GNPA %' breached appetite — Raise issue". Vidhi may phrase the explanation, but the trigger and target are rule-based and logged.

---

## C.7 Workflow pattern library (`packages/patterns`)

Every phase cites a pattern ID in its screen table; deviations need an ADR.

| ID | Pattern | Key rules |
|---|---|---|
| PAT-01 | Wizard with save-and-resume | ≤ 7 steps, each a URL; autosave ≤ 10 s; "Check your answers"; pre-fill (SC 3.3.7); drafts kept 90 days |
| PAT-02 | Maker-checker approval | Diff, evidence, citations, preview; maker ≠ checker; reason on reject; step-up where configured; WYSIWYS digest |
| PAT-03 | Bulk action with preview and undo | Dry run with counts and sample; per-row results CSV; undo window 10 min for reversible actions; irreversible actions use PAT-16 |
| PAT-04 | SLA queue with "Next" | Deadline-aware ordering; atomic claim; pauses only internal SLA with fixed reasons |
| PAT-05 | Kanban | Keyboard "Move to…" alternative (SC 2.5.7); stage gates explain what is missing |
| PAT-06 | Timeline / audit history | Filter by actor, kind, date; corrections shown with "Corrected" chip and both values for authorised viewers |
| PAT-07 | Calendar and scheduling | Store UTC, show viewer zone + IST; holiday overlays; ICS and M365/Google sync; recurring rules preview |
| PAT-08 | Document review and annotate | Comments as separate records; approval binds to version hash; redline compare |
| PAT-09 | eSign ceremony | Pre-sign summary; signer order; reminders; IT Act First Schedule exclusions blocked; signed PDF verification |
| PAT-10 | Payment and checkout | Price breakdown incl. GST before personal data; hosted checkout; "Paid" only after verified webhook |
| PAT-11 | Import with mapping preview | Template download → upload → mapping → dry-run → (approval) → commit → reconciliation counts; rollback until dependants exist |
| PAT-12 | Export request | Scope → layout → destination → redaction profile → preview of folders/counts → approval for sensitive → certificate |
| PAT-13 | Escalation ladder | L0–L3; level times above floors; L3 mandatory for statutory clocks |
| PAT-14 | Exception handling | Open → acknowledged → resolved / risk-accepted (expiry ≤ 12 months) → reopened |
| PAT-15 | Empty, error, loading states | One sentence + one action; skeletons; error code + trace ID; data preserved on error |
| PAT-16 | Confirmation for irreversible actions | Full confirmation screen stating effect and entity; typed reference for destructive deletes and mass sends; irreversible list (L): sign, pay, publish policy, issue meeting notice, send final grievance reply, approve payroll, record portal submission, erase data, apply Correction Entry |
| PAT-17 | Evidence capture from anywhere | Upload from device, camera (mobile), email-in address per instance, drag from DMS, pull from connected drive, or "request from colleague/external party" with secure link |
| PAT-18 | Inline AI assist | "Draft with Vidhi" button next to rich-text fields; draft appears as suggestion with "Accept / Edit / Discard"; label "AI-generated draft — review required"; sources panel |
| PAT-19 | Period roll-forward | "Copy from last period" for evidence descriptions, control notes and assignees (never copies evidence files or status) |
| PAT-20 | Saved views and filters | URL-encoded filters; share; official views by admins |

---

## C.8 Design tokens and visual identity (from owner's baseline, corrected for WCAG 2.2 AA)

### C.8.1 Colour

| Token | Hex | Use | Contrast on white | Rule |
|---|---|---|---|---|
| `color.primary` (Navy) | #0A2540 | Primary text accents, primary buttons, header | 15.5:1 | — |
| `color.primary.dark` | #050F1F | Hover/pressed | — | — |
| `color.primary.wash` | #E8EDF2 | Section backgrounds, hover rows | — | Background only |
| `color.accent` (Gold) | #C9A961 | Premium badges, decorative accents, focus ring on navy | **2.25:1** | **Never for text or meaningful icons on light backgrounds**; allowed on navy (6.9:1) |
| `color.accent.text` | #8A6D2B | Gold-toned text on light surfaces | 4.9:1 | Use instead of #C9A961 for text |
| `color.success` | #2D6A4F | Complied, approved | 6.4:1 | Always with icon + label |
| `color.success.bg` | #D1E7DD | Success background | — | — |
| `color.warning` (Amber) | #D97706 | Due-soon fills, icons ≥ 3:1 UI | **3.2:1** | **Not for body text**; text variant below |
| `color.warning.text` | #B45309 | Due-soon text | 5.0:1 | — |
| `color.warning.bg` | #FEF3C7 | Warning background | — | — |
| `color.danger` | #C44536 | Overdue, breach | 4.9:1 | With icon + label |
| `color.danger.bg` | #FEE2E2 | Error background | — | — |
| `color.info` | #1D4ED8 | Links, info | 6.7:1 | Links underlined in body text |
| `color.text` | #0F172A | Body text | 17.9:1 | — |
| `color.text.secondary` | #475569 | Secondary text | 7.6:1 | — |
| `color.text.placeholder` | #64748B | Placeholders, helper text | ≈ 4.8:1 | Replaces #94A3B8 for any informative text |
| `color.disabled` | #94A3B8 | Disabled controls only | 2.6:1 | Disabled state exempt; never for active information |
| `color.border` | #E2E8F0 | Dividers | — | Input borders use #64748B (≥ 3:1, SC 1.4.11) |
| `color.bg` | #F8FAFC | App background | — | — |
| `color.surface` | #FFFFFF | Cards, modals | — | — |

Status is never conveyed by colour alone: every status chip has an icon (check-circle, clock, alert-triangle, x-circle, info, pause for waiting) and a text label. Dark and high-contrast themes are generated from the same tokens and validated in CI.

### C.8.2 Typography, spacing, shape

Headings Space Grotesk (500/600/700; H1 32/40, H2 24/32, H3 20/28, H4 16/24); UI Inter (400/500/600/700; 14/20 default, 16/24 emphasis, 12/16 small — minimum 12 px, never for essential information below 14 px); monospace JetBrains Mono 13/18 for IDs and clause references; long-form legal text IBM Plex Serif 16/26; Indic scripts Noto Sans family per script. Spacing scale 4, 8, 12, 16, 24, 32, 48, 64, 96. Radius: inputs/buttons 8, cards/modals 12, chips pill. Elevation: card shadow-sm, popover shadow-md, modal shadow-lg. Icons: Lucide, 24 px default, 1.5 px stroke; regulator marks only where trademark use is permitted [VERIFY permission; default: text chips "RBI", "SEBI" without logos]. Motion 150–250 ms, respects `prefers-reduced-motion`; celebratory animations off by default (T).

### C.8.3 Machine-readable tokens

```json
{
  "color": {"primary":"#0A2540","primaryDark":"#050F1F","primaryWash":"#E8EDF2","accent":"#C9A961","accentText":"#8A6D2B",
            "success":"#2D6A4F","successBg":"#D1E7DD","warning":"#D97706","warningText":"#B45309","warningBg":"#FEF3C7",
            "danger":"#C44536","dangerBg":"#FEE2E2","info":"#1D4ED8","text":"#0F172A","textSecondary":"#475569",
            "placeholder":"#64748B","disabled":"#94A3B8","border":"#E2E8F0","inputBorder":"#64748B","bg":"#F8FAFC","surface":"#FFFFFF"},
  "spacing":[0,4,8,12,16,24,32,48,64,96],
  "radius":{"sm":4,"md":8,"lg":12,"full":9999},
  "font":{"heading":"Space Grotesk","body":"Inter","mono":"JetBrains Mono","legal":"IBM Plex Serif"},
  "size":{"xs":12,"sm":14,"md":16,"lg":18,"xl":20,"2xl":24,"3xl":32},
  "weight":{"regular":400,"medium":500,"semibold":600,"bold":700},
  "focus":{"ring":"2px solid #0A2540 + 2px offset #C9A961 (on light); 2px solid #C9A961 (on navy)"},
  "breakpoints":{"sm":640,"md":768,"lg":1024,"xl":1280,"2xl":1536}
}
```

### C.8.4 Copy conventions

Plain English (grade ≈ 8 where possible), active voice, Indian conventions (INR, dd-MMM-yyyy, FY26-27); regulatory terms keep their official names with "i" explanations; errors say what happened, why and what to do, with code and trace ID; never "Oops"; AI content always labelled; no claims of certification, regulator approval or guaranteed compliance (NN-19).

---

## C.9 Compiled screen inventory

*(Compiled by the pack lead from all streams' `_contrib/*_screens.md`.)*

Screen IDs below are binding. Duplicates found at review (25 Oct 2026) were resolved as follows: P00's console screens keep SCR-CORE-01–09; the shell-level screens are renumbered **SCR-CORE-20** (command palette), **SCR-CORE-21** (global search) and **SCR-CORE-22** (context switcher); P04's Calendar keeps **SCR-WF-01** and the Work Inbox is **SCR-WF-00**. SCR-TPL-01–04 appear twice because P03 (S1) and Appendix E (S2) described the same template screens; they are one screen each — Appendix E §E's descriptions are the content specification, P03's names are the menu labels. Shell-level screens SCR-RPT-01 (role home dashboards), SCR-WF-00 (Work Inbox) and SCR-CORE-21 (global search) are owned by P04 (X-26).

### Screens — stream S11 (P00, P01, P24, App B, Q)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-CORE-01 | Platform home (health) | console › Home | plt_* | P00 |
| SCR-CORE-02 | Tenants list and detail | console › Tenants | plt_super_admin, plt_support (masked) | P00 |
| SCR-CORE-03 | Feature flags | console › Platform › Flags | plt_super_admin, approver roles | P00 |
| SCR-CORE-04 | Audit explorer (platform chain) | console › Audit › Platform chain | plt_auditor, plt_security_officer | P00 |
| SCR-CORE-05 | Correction Entries (create, approve, apply) | console › Audit › Corrections | plt_super_admin (maker), plt_security_officer/checker | P00 |
| SCR-CORE-06 | Migration console | console › Platform › Migration | plt_super_admin, plt_content_maker/checker | P00 |
| SCR-CORE-07 | Outbox and integrations health | console › Platform › Events | plt_super_admin, plt_support | P00 |
| SCR-CORE-08 | Platform corrections register (tenant) | app › Settings › Audit & history › Platform corrections | ten_admin, ten_cco, auditors | P00 |
| SCR-CORE-09 | Chain verification (tenant) | app › Settings › Audit & history › Integrity | ten_admin, auditors | P00 |
| SCR-IAM-01 | Sign in | auth | all | P01 |
| SCR-IAM-02 | MFA challenge and step-up | auth | all | P01 |
| SCR-IAM-03 | Enrol second factor / passkey | auth | all | P01 |
| SCR-IAM-04 | Account recovery | auth | all | P01 |
| SCR-IAM-05 | Accept invitation | auth/web | invitees | P01 |
| SCR-IAM-06 | Tenant and capacity switcher | header (web, delivery) | multi-membership users | P01 |
| SCR-IAM-10 | Onboarding — Account | public→web | new admin | P01 |
| SCR-IAM-11 | Onboarding — Find your organisation (KYB) | web | new admin | P01 |
| SCR-IAM-12 | Onboarding — Entity profile and group | web | new admin | P01 |
| SCR-IAM-13 | Onboarding — Regulatory profile and families | web | new admin | P01 |
| SCR-IAM-14 | Onboarding — Modules and price | web | new admin | P01 |
| SCR-IAM-15 | Onboarding — Team and workflows | web | new admin | P01 |
| SCR-IAM-16 | Onboarding — First value | web | new admin | P01 |
| SCR-IAM-20 | My account | all apps › Avatar › My account | all | P01 |
| SCR-IAM-21 | Security (factors, passkeys, recovery codes) | My account › Security | all | P01 |
| SCR-IAM-22 | Sessions and devices | My account › Sessions | all | P01 |
| SCR-IAM-23 | Privacy centre | My account › Privacy | all customers | P01 |
| SCR-IAM-30 | Users | app › Settings › Users & access › Users | ten_admin | P01 |
| SCR-IAM-31 | User detail | same › <user> | ten_admin | P01 |
| SCR-IAM-32 | Roles and role templates | Settings › Users & access › Roles | ten_admin | P01 |
| SCR-IAM-33 | Pending access approvals | Settings › Users & access › Approvals | ten_admin | P01 |
| SCR-IAM-34 | Bulk import users | Settings › Users & access › Import | ten_admin | P01 |
| SCR-IAM-35 | SSO and SCIM | Settings › Users & access › Single sign-on | ten_admin | P01 |
| SCR-IAM-36 | Delivery access (LawDocs staff) | Settings › Users & access › LawDocs access | ten_admin, ten_cco | P01 |
| SCR-IAM-37 | Auditor access grants | Settings › Users & access › Auditors | ten_admin, ten_cco | P01 |
| SCR-IAM-38 | Supervisor (regulator) access | Settings › Users & access › Regulator access | ten_cco (maker), MD/CEO/CISO (checker) | P01 |
| SCR-IAM-39 | Support access and break-glass history | Settings › Users & access › Support access | ten_admin | P01 |
| SCR-IAM-40 | Access review | Settings › Users & access › Access reviews | ten_admin, dept heads | P01/P24 |
| SCR-IAM-50 | Staff directory and assignments | delivery › Team | dlv_lead | P01 |
| SCR-IAM-51 | Request delivery grant | delivery › Clients › <client> › Access | dlv_lead | P01 |
| SCR-IAM-60 | Platform users and roles | console › Access | plt_super_admin | P01 |
| SCR-IAM-61 | Break-glass console | console › Access › Break-glass | plt_support, plt_security_officer | P01 |
| SCR-IAM-62 | Trials and extensions | console › Tenants › Trials | plt_super_admin, plt_finance | P01 |
| SCR-ENG-01 | Release calendar and rings | console › Engineering › Releases | release manager, CTO, product owner | P24 |
| SCR-ENG-02 | Release detail | console › Engineering › Releases › <rel> | same | P24 |
| SCR-ENG-03 | Change records | console › Engineering › Changes | engineering | P24 |
| SCR-ENG-04 | Migration monitor | console › Engineering › Migrations | SRE, tech lead | P24 |
| SCR-ENG-05 | Golden export diff viewer | console › Engineering › Export goldens | tech lead, data owner | P24 |
| SCR-ENG-06 | Backups and restore tests | console › Engineering › Resilience | SRE, security | P24 |
| SCR-ENG-07 | DR drills | console › Engineering › Resilience › Drills | SRE, CTO | P24 |
| SCR-ENG-08 | Vulnerabilities | console › Security › Vulnerabilities | security, engineering | P24 |
| SCR-ENG-09 | VAPT engagements | console › Security › VAPT | security | P24 |
| SCR-ENG-10 | Control evidence status | console › Assurance › Evidence | security, plt_auditor | P24 |
| SCR-ENG-11 | Incidents and clocks | console › Security › Incidents | incident commander, security | P24 |
| SCR-ENG-12 | Go-live checklist | console › Assurance › Go-live | CTO, CISO, CS, product owner | P24 |
| SCR-ENG-20 | What's new | app › Help › What's new | all tenant users | P24 |
| SCR-ENG-21 | Release preferences | app › Settings › Platform & releases | ten_admin | P24 |
| SCR-ENG-22 | Security and trust | app › Settings › Security & trust | ten_admin, ten_kmp:CISO | P24 |

### Screens — stream S12 (P02, App A, C, D, U)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-CFG-01 | Settings home | Settings | all (trimmed) | P02 |
| SCR-CFG-02 | Settings section page | Settings → {section} | per section | P02 |
| SCR-CFG-03 | Setting detail & history (drawer) | any setting row | per key | P02 |
| SCR-CFG-04 | Change request composer | Settings → Requests → New | ten_admin, platform roles | P02 |
| SCR-CFG-05 | Change request review (inbox decision panel) | Work Inbox | checkers | P02 |
| SCR-CFG-06 | Rule packs catalogue | Settings → Rules & packs → Rule packs; Console → Rules & config | ten_admin, content roles | P02 |
| SCR-CFG-07 | Rule-pack editor (ZEN decision tables) | Console → Rules & config → Rule packs → Edit | plt_content_* | P02 |
| SCR-CFG-08 | Golden cases & sandbox runner | Console / Settings → Rules & packs → Sandbox | content roles, ten_admin | P02 |
| SCR-CFG-09 | Impact analysis report | linked from change request | approvers | P02 |
| SCR-CFG-10 | Setting packs | Settings → Rules & packs → Setting packs | ten_admin | P02 |
| SCR-CFG-11 | Department & function tree (merge/split wizard) | Settings → Organisation → Departments & functions | ten_admin, ten_dept_head | P02 |
| SCR-CFG-12 | Terminology | Settings → Organisation → Terminology | ten_admin | P02 |
| SCR-CFG-13 | Status sets | Settings → Workflow → Status sets | ten_admin | P02 |
| SCR-CFG-14 | Waiting-on parties & chase policies | Settings → Workflow → Waiting-on | ten_admin, ten_cco | P02 |
| SCR-CFG-15 | Reason-code lists | Settings → Workflow → Reason codes | ten_admin | P02 |
| SCR-CFG-16 | Custom fields | Settings → Data & forms → Custom fields | ten_admin | P02 |
| SCR-CFG-17 | Form builder | Settings → Data & forms → Forms | ten_admin | P02 |
| SCR-CFG-18 | Workflow designer | Settings → Workflow → Workflow designer | ten_admin, ten_cco | P02 |
| SCR-CFG-19 | SLA policies & escalation ladders | Settings → Workflow → SLA & escalation | ten_admin, ten_cco | P02 |
| SCR-CFG-20 | Delegations | Settings → My preferences → Delegation / Users & access → Delegations | all / admins | P02 |
| SCR-CFG-21 | Notification templates & channel policy | Settings → Notifications | ten_admin | P02 |
| SCR-CFG-22 | Dashboard defaults & builder | Settings → Dashboards; Home → Customise | ten_admin, users | P02 |
| SCR-CFG-23 | Menu & landing pages | Settings → Navigation | ten_admin | P02 |
| SCR-CFG-24 | Configuration Health | Settings → Rules & packs → Configuration health | ten_admin, ten_cco, platform | P02 |
| SCR-CFG-25 | Branding & domains | Settings → Branding | ten_admin | P02 |
| SCR-CFG-26 | Configuration export / import / compare | Settings → Data export & exit → Configuration | ten_admin | P02 |
| SCR-CFG-27 | Personal preferences | Settings → My preferences | all | P02 |
| SCR-CFG-28 | Changes made by LawDocs | Settings → Account → Changes made by LawDocs | ten_admin, ten_cco, auditors | P02 |
| SCR-CFG-29 | Tenant override console | Console → Tenants → Tenant 360 → Configuration | plt_super_admin | P02 |
| SCR-CFG-30 | Correction Entry review | Console → Corrections | plt_super_admin, plt_security_officer | P02 |
| SCR-CFG-31 | Platform settings & bounds | Console → Rules & config → Platform settings | platform roles | P02 |
| SCR-CFG-32 | Support access sessions | Settings → Account → Support access | ten_admin | P02 |
| SCR-CORE-20 | Command palette (Ctrl/Cmd+K) | global | all | P02 (framework) / P04 |
| SCR-CORE-21 | Global search results | global | all | P04 (proposed owner) |
| SCR-CORE-22 | Context switcher (tenant → legal entity → period) | top bar | all | P01 |
| SCR-RPT-01 | Role home dashboard | Home | all | P04 (proposed owner) |
| SCR-RPT-02 | Personal dashboards (up to 5) | Home → My dashboards | all | P04 |
| SCR-WF-00 | Work Inbox (all kinds) | Work Inbox | all | P04 |
| SCR-BRD-01 | Board shell home | /board | ten_board_member, ten_committee_member | P06 |
| SCR-ASR-01 | Assurance shell home | /assurance | external auditors, supervisor view | P01/P10 |
| SCR-ME-01 | Self-service home | /me | ten_employee, coop_member | P13/P16 |

### Screens — stream S1 (P03–P05, App F)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-CNT-01 | Content Library | Console › Content › Library | plt_content_*, plt_super_admin | P03 |
| SCR-CNT-02 | Instrument workspace | Console › Content › Library › instrument | plt_content_* | P03 |
| SCR-CNT-03 | Content Studio grid | Instrument › Checkpoints › Edit | plt_content_maker | P03 |
| SCR-CNT-04 | Release manager | Console › Content › Releases | plt_content_checker, plt_content_publisher | P03 |
| SCR-TPL-01 | Template Registry | Console › Content › Templates | plt_super_admin, plt_content_maker | P03 |
| SCR-TPL-02 | Import wizard | Console › Content › Import; Tenant › Compliance › Regulations › Import | importers | P03 |
| SCR-TPL-03 | Import job detail | Import › Jobs › job | importer, checker | P03 |
| SCR-TPL-04 | Checker diff review | Work Inbox › Content review | plt_content_checker, ten_cco | P03 |
| SCR-CNT-10 | Regulation Catalogue | Tenant › Compliance › Regulations | ten_admin, ten_cco (+read) | P03 |
| SCR-CNT-11 | Instrument (tenant view) | Regulations › instrument | tenant roles | P03 |
| SCR-CNT-12 | My Questions & Overlays | Regulations › My changes | ten_cco, ten_admin, ten_dept_head | P03 |
| SCR-CNT-13 | Overlay conflicts | Work Inbox › Rebase conflicts | ten_cco | P03 |
| SCR-CNT-14 | Departments & functions mapping | Settings › Organisation › Compliance mapping | ten_admin | P03 |
| SCR-CNT-15 | Checkpoint lineage | Checkpoint › History | read roles | P03 |
| SCR-CMP-01 | My Day | Home | working users | P04 |
| SCR-CMP-02 | Work Inbox | Inbox | all | P04 |
| SCR-CMP-03 | Compliance register | Compliance › Register | tenant roles | P04 |
| SCR-CMP-04 | Instance detail | Register › instance | scoped | P04 |
| SCR-CMP-05 | Review queue | Compliance › Review | checkers | P04 |
| SCR-CMP-06 | Events | Compliance › Events | triggerers, CCO | P04 |
| SCR-CMP-07 | Exceptions | Compliance › Exceptions | CCO, dept heads, IA, CRO | P04 |
| SCR-CMP-08 | Certificates | Compliance › Certificates | dept heads, CCO, MD/CEO | P04 |
| SCR-CMP-09 | Dashboards | Dashboard | role-based | P04 |
| SCR-CMP-10 | Reports | Reports › Compliance | scoped | P04 |
| SCR-CMP-11 | Board compliance report | Reports › Board report | CCO, CS | P04 |
| SCR-WF-01 | Calendar | Calendar | all | P04 |
| SCR-WF-02 | Tasks | Tasks | all | P04 |
| SCR-WF-03 | Scheduled tasks | Tasks › Scheduled | all | P04 |
| SCR-WF-04 | Notifications | Bell icon | all | P04 |
| SCR-WF-05 | Notification preferences | Profile › Notifications | all | P04 |
| SCR-WF-06 | Calendar connections | Profile › Calendar; Settings › Calendar policy | all / ten_admin | P04 |
| SCR-WF-07 | Messages | Messages | all | P04 |
| SCR-CHG-01 | Change dashboard | Console › Regulatory change › Dashboard | content team | P05 |
| SCR-CHG-02 | Triage queue | Console › Regulatory change › Triage | plt_content_maker | P05 |
| SCR-CHG-03 | Change item workspace | Triage › item | content team | P05 |
| SCR-CHG-04 | Sources | Console › Regulatory change › Sources | plt_super_admin, content lead | P05 |
| SCR-CHG-05 | Horizon | Console › Regulatory change › Horizon | content team | P05 |
| SCR-CHG-10 | Updates inbox | Megaphone; Compliance › Updates | tenant users | P05 |
| SCR-CHG-11 | Update detail | Updates › item | tenant users | P05 |
| SCR-CHG-12 | Impact assessment | Update › Assess impact | ten_cco, dlv_rm | P05 |
| SCR-CHG-13 | Change implementation tracker | Compliance › Regulatory changes | ten_cco, dept heads, IA, Board | P05 |
| SCR-CHG-14 | Change history | Checkpoint/instrument › Change history | tenant roles | P05 |
| SCR-CHG-15 | Update preferences | Profile › Updates; Settings › Updates | users / ten_admin | P05 |
| SCR-AIS-01 | AI Question Authoring Studio | Console › Content › AI Studio; Tenant › Regulations › Create questions with Vidhi | plt_content_maker; ten_admin, ten_cco, dlv_rm | P05 |
| SCR-AIS-02 | Draft review grid | AI Studio › run | same | P05 |
| SCR-AIS-03 | Methodology & prompts | Console › Content › AI Studio › Methodology | plt_super_admin, content lead | P05 |
| SCR-AIS-04 | Evaluation | Console › Content › AI Studio › Evaluation | content lead | P05 |

### Screens — stream S2 (App E, templates)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-TPL-01 | Template catalogue (download family templates, version, status, changelog) | Console → Content Studio → Templates; Tenant → Compliance Library → Templates | plt_content_maker, plt_content_checker, ten_admin, ten_cco | P03 |
| SCR-TPL-02 | Import wizard (choose scope, family, instrument version; upload) | Content Studio → Import Question Sheet; Compliance Library → My Instruments → Import | plt_content_maker, ten_admin | P03 |
| SCR-TPL-03 | Import preview and issues (row grid, issue filters, diff view, download issues workbook) | (from SCR-TPL-02) | plt_content_maker, plt_content_checker, ten_admin, ten_cco | P03 |
| SCR-TPL-04 | Re-upload diff and change classification (Editorial / Substantive / Correction) | Content Studio → Instrument → Change set | plt_content_maker, plt_content_checker | P05 |
| SCR-TPL-05 | Family and vocabulary editor (C/D axes, values, aliases, canonical codes, taxonomy mapping, build & validate) | Console → Content Studio → Families | plt_content_maker, plt_content_checker | P03 |
| SCR-TPL-06 | Tenant vocabulary extensions (department names, internal compliance types) | Tenant → Settings → Compliance vocabulary | ten_admin | P02/P03 |
| SCR-TPL-07 | AI authoring run (para map approval, batch progress, download draft workbook) | Content Studio / My Instruments → Draft with Vidhi | plt_content_maker, ten_admin | P05 |

### Screens — stream S3 (P06–P07)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-GOV-01 | CS Dashboard | Governance › Home | see phase §3 | P06 |
| SCR-GOV-02 | Governance Blueprint | Governance › Blueprint | see phase §3 | P06 |
| SCR-GOV-03 | Entity Master | Governance › Entities › {entity} | see phase §3 | P06 |
| SCR-GOV-04 | Group Structure | Governance › Entities › Group tree | see phase §3 | P06 |
| SCR-GOV-05 | People — Directors & KMP | Governance › People | see phase §3 | P06 |
| SCR-GOV-06 | Person Governance Profile | Governance › People › {person} | see phase §3 | P06 |
| SCR-GOV-07 | Committees | Governance › Committees | see phase §3 | P06 |
| SCR-GOV-08 | Committee Page | Governance › Committees › {committee} | see phase §3 | P06 |
| SCR-GOV-09 | Annual Planner | Governance › Meetings › Planner | see phase §3 | P06 |
| SCR-GOV-10 | Meeting Workspace | Governance › Meetings › {meeting} | see phase §3 | P06 |
| SCR-GOV-11 | Agenda Builder | inside SCR-GOV-10 | see phase §3 | P06 |
| SCR-GOV-12 | Board Pack Builder | inside SCR-GOV-10 | see phase §3 | P06 |
| SCR-GOV-13 | Director Portal Home | Board Portal (separate shell for directors) | see phase §3 | P06 |
| SCR-GOV-14 | Board Book Reader | Board Portal › Meeting › Book | see phase §3 | P06 |
| SCR-GOV-15 | Meeting Conduct Console | Meeting › Conduct | see phase §3 | P06 |
| SCR-GOV-16 | Minutes Editor | Meeting › Minutes | see phase §3 | P06 |
| SCR-GOV-17 | Circular Resolution | Governance › Circular resolutions | see phase §3 | P06 |
| SCR-GOV-18 | General Meeting Builder | Governance › General meetings | see phase §3 | P06 |
| SCR-GOV-19 | Resolutions Library | Governance › Library | see phase §3 | P06 |
| SCR-GOV-20 | Decisions & Actions | Governance › Decisions | see phase §3 | P06 |
| SCR-GOV-21 | Statutory Registers | Governance › Registers | see phase §3 | P06 |
| SCR-GOV-22 | Register Entry Review | Registers › Pending | see phase §3 | P06 |
| SCR-GOV-23 | ROC Filings | Governance › Filings | see phase §3 | P06 |
| SCR-GOV-24 | Declarations & Fit-and-Proper | Governance › Declarations | see phase §3 | P06 |
| SCR-GOV-25 | Regulator Approvals | Governance › Approvals | see phase §3 | P06 |
| SCR-GOV-26 | LODR Calendar | Governance › Listed › Calendar | see phase §3 | P06 |
| SCR-GOV-27 | Disclosure Cases (Reg 30) | Governance › Listed › Disclosures | see phase §3 | P06 |
| SCR-GOV-28 | RPT Monitor | Governance › Listed › RPT | see phase §3 | P06 |
| SCR-GOV-29 | Insider Trading | Governance › Listed › PIT | see phase §3 | P06 |
| SCR-GOV-30 | Annual Report Builder | Governance › Annual report | see phase §3 | P06 |
| SCR-GOV-31 | Secretarial Audit Workspace | Auditor shell | see phase §3 | P06 |
| SCR-GOV-32 | LLP Governance | Governance › LLP | see phase §3 | P06 |
| SCR-POL-01 | Policy Register | Policies › Register | see phase §3 | P07 |
| SCR-POL-02 | Required Policies | Policies › Required | see phase §3 | P07 |
| SCR-POL-03 | Policy Page | Policies › {policy} | see phase §3 | P07 |
| SCR-POL-04 | Draft with Vidhi | inside SCR-POL-03 | see phase §3 | P07 |
| SCR-POL-05 | Review Workspace | Policies › Reviews (my queue) | see phase §3 | P07 |
| SCR-POL-06 | Approval Evidence | inside SCR-POL-03 | see phase §3 | P07 |
| SCR-POL-07 | Attestation Campaigns | Policies › Attestations | see phase §3 | P07 |
| SCR-POL-08 | My Policies | Personal › My policies | see phase §3 | P07 |
| SCR-POL-09 | Review Calendar | Policies › Calendar | see phase §3 | P07 |
| SCR-POL-10 | Model Template Studio (platform) | Console › Content › Model templates | see phase §3 | P07 |
| SCR-POL-11 | Tenant Templates | Policies › Templates | see phase §3 | P07 |
| SCR-DMS-01 | Documents Home | Documents | see phase §3 | P07 |
| SCR-DMS-02 | Browser | Documents › Browse | see phase §3 | P07 |
| SCR-DMS-03 | Document Page | Documents › {doc} | see phase §3 | P07 |
| SCR-DMS-04 | Type Copy Workbench | inside SCR-DMS-03 | see phase §3 | P07 |
| SCR-DMS-05 | Translation View | inside SCR-DMS-03 | see phase §3 | P07 |
| SCR-DMS-06 | Search | global search bar + Documents › Search | see phase §3 | P07 |
| SCR-DMS-07 | Share Pack Builder | Documents › Share › New | see phase §3 | P07 |
| SCR-DMS-08 | Shares & Access Log | Documents › Shares | see phase §3 | P07 |
| SCR-DMS-09 | eSign Envelope Builder | Sign › New envelope | see phase §3 | P07 |
| SCR-DMS-10 | My Signatures | Sign › Inbox | see phase §3 | P07 |
| SCR-DMS-11 | Folder Intake | Documents › Import | see phase §3 | P07 |
| SCR-DMS-12 | Retention & Holds | Documents › Retention | see phase §3 | P07 |
| SCR-DMS-13 | E-mail-in Addresses | Documents › Settings › E-mail-in | see phase §3 | P07 |
| SCR-DMS-14 | External Viewer | external shell (no app chrome) | see phase §3 | P07 |
| SCR-DMS-15 | Redaction Tool | inside SCR-DMS-03 | see phase §3 | P07 |

### Screens — stream S4 (P08–P09, App H)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-ERM-01 | CRO Home | Risk › Home | ten_kmp(CRO), ten_maker(risk officer) | P08 |
| SCR-ERM-02 | Framework & applicability | Risk › Framework | CRO, ten_admin (read), ten_internal_auditor (read) | P08 |
| SCR-ERM-03 | Risk appetite (RAS) | Risk › Appetite | CRO (edit), CFO/CCO (concur), RMC, Board (approve) | P08 |
| SCR-ERM-04 | Risk register | Risk › Register | CRO office, risk owners (own scope), IA (read) | P08 |
| SCR-ERM-05 | Risk detail | Risk › Register › [risk] | as above | P08 |
| SCR-ERM-06 | Controls | Risk › Controls | CRO office, control owners, IA | P08 |
| SCR-ERM-07 | RCSA campaigns | Risk › RCSA | CRO office | P08 |
| SCR-ERM-08 | RCSA response | Risk › RCSA › My assessments | ten_dept_head, ten_maker (respondents) | P08 |
| SCR-ERM-09 | RCSA challenge queue | Risk › RCSA › Review | ten_checker (second line), CRO | P08 |
| SCR-ERM-10 | KRI library | Risk › KRIs | CRO office | P08 |
| SCR-ERM-11 | KRI monitor | Risk › KRIs › Monitor | CRO, KRI owners, RMC (read) | P08 |
| SCR-ERM-12 | Breach episode | Risk › KRIs › [episode] | KRI owner, CRO, CCO | P08 |
| SCR-ERM-13 | Loss events | Risk › Loss events | ORM team; any employee (quick form) | P08 |
| SCR-ERM-14 | Issues & actions | Risk › Issues | owners, second line | P08 |
| SCR-ERM-15 | Risk acceptances | Risk › Acceptances | CRO, RMC, Board | P08 |
| SCR-ERM-16 | Emerging risks | Risk › Emerging | CRO office | P08 |
| SCR-ERM-17 | Committees & packs | Risk › Committees | CRO, CS, committee members | P08 |
| SCR-ERM-18 | Risk disclosures | Risk › Disclosures | CRO, CFO, CS | P08 |
| SCR-ERM-19 | Risk governance | Risk › Governance | CRO, CS, CCO | P08 |
| SCR-ERM-20 | Model inventory | Risk › Models | CRO, model owners, IA | P08 |
| SCR-ERM-21 | Data feeds | Risk › Data feeds | CRO office, integration admin | P08 |
| SCR-ERM-22 | Quick RCSA | Risk › Quick assessment | ten_admin / risk owner (small tenants) | P08 |
| SCR-ERM-23 | Risk owner home | Home | ten_dept_head | P08 |
| SCR-ERM-24 | Board risk view | Board › Risk | ten_board_member | P08 |
| SCR-RAL-01 | Lab home | Risk Lab › Home | CRO, CFO, analysts | P09 |
| SCR-RAL-02 | Data & snapshots | Risk Lab › Data | analysts, data stewards | P09 |
| SCR-RAL-03 | Data quality | Risk Lab › Data › Quality | data stewards | P09 |
| SCR-RAL-04 | Capital runs | Risk Lab › Capital | CFO office, CRO | P09 |
| SCR-RAL-05 | Capital drill-down | Risk Lab › Capital › Drill-down | CFO, CRO, IA | P09 |
| SCR-RAL-06 | What-if & capital plan | Risk Lab › Capital › Planning | CFO, CRO | P09 |
| SCR-RAL-07 | Ratio library | Risk Lab › Metrics | data stewards, metric owners | P09 |
| SCR-RAL-08 | ALM & liquidity | Risk Lab › Liquidity | Treasury, CFO, CRO, ALCO | P09 |
| SCR-RAL-09 | Interest-rate risk | Risk Lab › IRRBB | Treasury, CRO | P09 |
| SCR-RAL-10 | Concentration | Risk Lab › Concentration | CRO, CCrO | P09 |
| SCR-RAL-11 | Investments | Risk Lab › Investments | CFO, investment committee | P09 |
| SCR-RAL-12 | Scenario library | Risk Lab › Stress › Scenarios | CRO office | P09 |
| SCR-RAL-13 | Stress run builder | Risk Lab › Stress › New run | analysts | P09 |
| SCR-RAL-14 | Stress results | Risk Lab › Stress › Results | CRO, RMC, ALCO | P09 |
| SCR-RAL-15 | ICAAP cycles | Risk Lab › ICAAP | risk function, CRO, CS, RMC, Board | P09 |
| SCR-RAL-16 | PCA monitor | Risk Lab › PCA | CS, CRO, CFO, MD/CEO, Board | P09 |
| SCR-RAL-17 | KMP dashboards | Dashboards › My dashboard | all KMP roles | P09 |
| SCR-RAL-18 | Certification queue | Dashboards › Sign-off | data stewards, checkers, metric owners, CS | P09 |
| SCR-RAL-19 | Lab model registry | Risk Lab › Models | CRO, validators | P09 |
| SCR-RAL-20 | Schedule III ratios | Risk Lab › Financial ratios | CFO (company/LLP/listed) | P09 |
| SCR-RAL-21 | Co-operative indicators | Risk Lab › Society indicators | coop_office_bearer (Secretary/Treasurer) | P09 |
| SCR-RAL-22 | Insurer solvency | Risk Lab › Solvency | Insurer CFO, Appointed Actuary (read) | P09 |

### Screens — stream S5 (P10–P11, App I–J)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-AUD-01 | Audit home | Audit › Home | All audit roles | P10 |
| SCR-AUD-02 | Universe | Audit › Universe | HIA, IA (edit); ACB (read) | P10 |
| SCR-AUD-03 | Risk assessment | Audit › Risk assessment | IA, HIA | P10 |
| SCR-AUD-04 | Plan builder | Audit › Plan | HIA (edit), ACB (approve) | P10 |
| SCR-AUD-05 | Methodology | Audit › Methodology | HIA, ACB | P10 |
| SCR-AUD-06 | Engagements | Audit › Engagements | IA team; HIA | P10 |
| SCR-AUD-07 | Engagement detail | Audit › Engagements › {id} | Team, HIA | P10 |
| SCR-AUD-08 | Workpaper editor | … › Workpapers › {ref} | Preparer, reviewer | P10 |
| SCR-AUD-09 | Sampling | … › Samples | IA | P10 |
| SCR-AUD-10 | Analytics (CAAT) library | Audit › Analytics | IA, IS auditors | P10 |
| SCR-AUD-11 | Evidence vault | Audit › Evidence | IA; external via room | P10 |
| SCR-AUD-12 | Findings | Audit › Findings | IA, owners (own items), ACB (read) | P10 |
| SCR-AUD-13 | Retest queue | Audit › Findings › Retest | Retesters | P10 |
| SCR-AUD-14 | ATR | Audit › ATR | HIA, CS; ACB read | P10 |
| SCR-AUD-15 | ACB pack builder | Audit › Committee packs | HIA, CS | P10 |
| SCR-AUD-16 | HIA and QAIP | Audit › Function | HIA, CS, ACB chair | P10 |
| SCR-AUD-17 | Statutory auditors | Audit › Statutory › Auditors | CFO office, CS, ACB | P10 |
| SCR-AUD-18 | PBC tracker | Audit › Statutory › PBC | CFO office; auditors (room) | P10 |
| SCR-AUD-19 | Auditor's Report Directions & CARO | Audit › Statutory › Checklists | Auditors, CFO, CCO | P10 |
| SCR-AUD-20 | Branch coverage | Audit › Statutory › Branch coverage | CFO, auditors | P10 |
| SCR-AUD-21 | Secretarial audit | Audit › Secretarial | CS, secretarial auditor | P10 |
| SCR-AUD-22 | IS audit & ITGC | Audit › IS & IT | IS auditors, CISO (read) | P10 |
| SCR-AUD-23 | VAPT | Audit › VAPT | CISO office, IA | P10 |
| SCR-AUD-24 | Concurrent audit | Audit › Concurrent | Concurrent auditors | P10 |
| SCR-AUD-25 | Inspections | Audit › Inspections | CCO, HIA | P10 |
| SCR-AUD-26 | Stock audit | Audit › Stock audit | Credit/risk, auditors | P10 |
| SCR-AUD-27 | External access (audit) | Audit › External access | CCO, CISO, CFO | P10 |
| SCR-AUD-28 | Auditor room | `apps/web` external landing | External auditors | P10 |
| SCR-AUD-29 | Inspection room | `apps/web` external landing | `ten_supervisor_view` | P10 |
| SCR-AUD-30 | Report studio | … › Report | Lead, HIA | P10 |
| SCR-RET-01 | Reporting home | Returns › Home | Makers, checkers, CFO, CCO | P11 |
| SCR-RET-02 | Return calendar | Returns › Calendar | All reporting roles | P11 |
| SCR-RET-03 | Applicability matrix | Returns › Applicability | CCO, auditors | P11 |
| SCR-RET-04 | Return instance | Returns › {code} › {period} | Per matrix | P11 |
| SCR-RET-05 | Lineage explorer | … › Lineage | Makers, checkers, auditors | P11 |
| SCR-RET-06 | Guided upload | … › File | Filer | P11 |
| SCR-RET-07 | Data Room | Returns › Data Room | Makers, data owners | P11 |
| SCR-RET-08 | Batch detail | … › Batch {id} | Makers | P11 |
| SCR-RET-09 | Mapping studio | Returns › Mapping | Makers, checkers | P11 |
| SCR-RET-10 | Reconciliations | Returns › Reconciliations | Makers, checkers, CFO | P11 |
| SCR-RET-11 | Revisions & queries | Returns › Revisions | CCO, makers | P11 |
| SCR-RET-12 | Credit bureau | Returns › Credit bureau | Bureau ops, nodal officer | P11 |
| SCR-RET-13 | GST | Returns › GST | Finance, tax | P11 |
| SCR-RET-14 | TDS/TCS | Returns › Income-tax | Finance, tax | P11 |
| SCR-RET-15 | MCA filings data | Returns › MCA | CS, CFO | P11 |
| SCR-RET-16 | Accounting bridge | Finance › Statements | CFO office | P11 |
| SCR-RET-17 | Ratio data | Finance › Data for ratios | CFO, CRO | P11 |
| SCR-RET-18 | Vidhi data-prep | Side panel on SCR-RET-07/09/10/04 | Makers | P11 |
| SCR-RET-19 | Registry (platform) | Console › Returns registry | plt_content_* | P11 |

### Screens — stream S6 (P12–P14, App T)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-DPC-01 | Privacy home (DPO dashboard) | Data & Cyber › Privacy | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-02 | Processing activities | › Privacy › Activities | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-03 | Activity detail | (drill) | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-04 | ROPA export | › Privacy › ROPA | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-05 | Notice designer | › Privacy › Notices | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-06 | Consent ledger | › Privacy › Consent | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-07 | Rights desk | › Privacy › Requests | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-08 | Request detail | (drill) | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-09 | Assessments | › Privacy › Assessments | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-10 | Incident register | › Data & Cyber › Incidents | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-11 | Incident war-room | (drill) | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-12 | CISO dashboard | › Cyber & IT | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-13 | Asset register | › Cyber & IT › Assets | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-14 | Control library | › Cyber & IT › Controls | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-15 | Statement of Applicability | › Cyber & IT › SoA | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-16 | VAPT & vulnerabilities | › Cyber & IT › VAPT | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-17 | BCP / DR | › Cyber & IT › Resilience | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-01 | Third-party home | › Third Parties | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-02 | Vendor profile | (drill) | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-03 | Outsourcing registers | › Third Parties › Registers | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-04 | DDQ builder & reviews | › Third Parties › Due diligence | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-05 | Contract checklist | (drill) | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-TPR-06 | Vendor portal | `/vendor` | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-18 | AI systems | › AI Governance | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-DPC-19 | Data & cyber reports | › Reports | DPO, CISO, CRO, CCO, makers/checkers, auditors, vendor (portal) | P12 |
| SCR-HR-01 | People home | People | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-02 | Employee directory | People › Employees | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-03 | Employee profile | (drill) | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-04 | Organisation designer | People › Organisation | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-05 | Default structure picker | Onboarding / Organisation | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-06 | Positions & regulated roles | People › Organisation › Positions | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-07 | Lifecycle board | People › Lifecycle | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-08 | Offer & agreement composer | (drill) | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-09 | Attendance | People › Time | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-10 | Leave console | People › Leave | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-11 | Payroll cockpit | People › Payroll | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-12 | Variance review | (drill) | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-13 | Statutory outputs | People › Payroll › Statutory | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-14 | Labour compliance home | People › Labour Compliance | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-15 | Register viewer | (drill) | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-16 | Committees (HR) | People › Committees | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-POSH-01 | IC workspace | People › POSH | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-POSH-02 | Case file | (drill, sealed) | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-17 | Policies & training | People › Policies & Training | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-HR-18 | People-risk KRIs | People › Reports › People risk | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-SS-01..08 | Self-service screens | My Work › … | HR admin, payroll maker/checker, CFO, dept heads, employees (self-service), IC members (POSH) | P13 |
| SCR-GRV-01 | Agent inbox | › Inbox | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-02 | Ticket workspace | (drill) | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-03 | GRO desk | › GRO Desk | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-04 | IO desk | › IO Desk | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-05 | Ladder designer | › Settings › Ladders | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-06 | Categories & mapping | › Settings › Categories | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-07 | Widget & portal builder | › Settings › Channels | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-08 | Knowledge base | › Knowledge Base | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-09 | MIS dashboard | › Reports & MIS | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-10 | Regulatory reports | › Reports & MIS › Regulatory | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-11 | Board/CSC pack | › Reports & MIS › Packs | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-PUB-01 | Public complaint form | `/grievance` | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |
| SCR-GRV-PUB-02 | Status tracker | `/grievance/track` | Support agents, GRO, PNO, IO, CCO, complainants (public) | P14 |

### Screens — stream S7 (P15–P16, App G, S)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-PACK-01 | Entity profile | Settings › Organisation › Entity profile | ten_admin, ten_cco, ten_kmp (CFO, CS); read: auditors, ten_supervisor_view | P15 |
| SCR-PACK-02 | Profile activation wizard | Onboarding › Step 3 Regulatory profile | ten_admin, ten_cco | P15 |
| SCR-PACK-03 | Applicability explorer | Compliance › Applicability | ten_cco, ten_dept_head, ten_admin; read: auditors | P15 |
| SCR-PACK-04 | What-if simulator | Compliance › Applicability › Simulate | ten_cco, ten_admin, ten_kmp | P15 |
| SCR-PACK-05 | Profile change queue | Compliance › Profile changes | ten_cco, ten_kmp (CFO/CS) | P15 |
| SCR-PACK-06 | Exemptions register | Compliance › Exemptions | ten_cco, ten_checker; read: auditors | P15 |
| SCR-PACK-07 | Sector pack overview | Settings › Sector pack | ten_admin, ten_cco | P15 |
| SCR-PACK-08 | Investment compliance | Risk › Investments | ten_kmp (CFO, CRO), ten_cco | P15 |
| SCR-PACK-09 | ARC trusts and clocks | Compliance › ARC › Trusts | ten_cco, ten_kmp | P15 |
| SCR-PACK-10 | Listed-company event register | Governance › Listed company › Events | ten_kmp (CS), ten_cco | P15 |
| SCR-PACK-11 | Group structure | Settings › Organisation › Group | ten_admin, ten_kmp (CS, CFO) | P15 |
| SCR-CNT-PK-01 | Taxonomy studio | Console › Content › Taxonomy | plt_content_maker/checker/publisher | P15 |
| SCR-CNT-PK-02 | Applicability rule editor | Console › Content › Applicability rules | plt_content_maker/checker | P15 |
| SCR-CNT-PK-03 | Jurisdiction packs | Console › Content › Jurisdictions | plt_content_publisher | P15 |
| SCR-COOP-01 | Society home | Home | coop_office_bearer, ten_kmp, ten_admin | P16 |
| SCR-COOP-02 | Society master and legal profile | Settings › Society | ten_admin | P16 |
| SCR-COOP-03 | Bye-laws | Governance › Bye-laws | secretary (maker), chairperson (checker) | P16 |
| SCR-COOP-04 | Members register | Members › Register | ten_maker, ten_checker, coop_office_bearer | P16 |
| SCR-COOP-05 | Member 360 | Members › Register › Member | ten_maker, ten_checker | P16 |
| SCR-COOP-06 | Shares register | Members › Shares | ten_maker, ten_checker | P16 |
| SCR-COOP-07 | Board and office bearers | Governance › Board | coop_office_bearer, ten_admin | P16 |
| SCR-COOP-08 | General body meetings | Governance › General Body | secretary, chairperson | P16 |
| SCR-COOP-09 | Elections | Governance › Elections | secretary, chairperson | P16 |
| SCR-COOP-10 | Statutory registers | Records › Registers | ten_maker; read: auditors, Registrar view | P16 |
| SCR-COOP-11 | Appropriation | Finance › Appropriation | treasurer, board | P16 |
| SCR-COOP-12 | Audit and rectification | Audit › Statutory audit | secretary; ten_external_auditor | P16 |
| SCR-COOP-13 | Registrar returns | Returns › Registrar / CRCS | CEO, secretary | P16 |
| SCR-COOP-14 | Inspections and inquiries | Compliance › Registrar matters | secretary, chairperson | P16 |
| SCR-COOP-15 | Credit-society monitors | Risk › Prudential | board, CEO, auditors | P16 |
| SCR-COOP-16 | Member portal | Member › My membership | coop_member | P16 |
| SCR-COOP-17 | Returning-officer view | Elections › Officer | coop_returning_officer (time-boxed) | P16 |

### Screens — stream S8 (P17–P19, App K–M)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-AI-01 | Vidhi panel (dock) | Global — `Ctrl/Cmd+J`; top bar "Ask Vidhi" | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-02 | Vidhi full page | Vidhi → Chat | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-03 | Output Card / review | Work Inbox → item | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-04 | Plan approval | Work Inbox → item | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-05 | Action approval | Work Inbox → item | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-06 | Vidhi tasks board | Vidhi → My Vidhi work | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-07 | Schedules | Vidhi → Schedules | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-08 | Notebooks home | Vidhi → Notebooks | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-09 | Notebook workspace | Vidhi → Notebooks → [notebook] | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-10 | Type Copy editor | DMS → document → Type copy | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-11 | Translation view | DMS → document → Translate | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-12 | WhatsApp/email importer | DMS → Import → Chat or email | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-13 | Drafting Studio | Opened from P06/P07/P09/P10 actions | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-14 | What Vidhi remembers | Settings → Vidhi AI → Memory | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-15 | Tenant AI settings | Settings → Vidhi AI | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-16 | AI usage and budgets | Settings → Billing → AI usage | all tenant users; admin for settings; platform for console | P17 |
| SCR-AI-17 | AI run ledger | Settings → Vidhi AI → Activity log (admin, auditor) | all tenant users; admin for settings; platform for console | P17 |
| SCR-CON-AI-01 | Model registry | Console → AI → Models | all tenant users; admin for settings; platform for console | P17 |
| SCR-CON-AI-02 | Skill and prompt registry | Console → AI → Skills | all tenant users; admin for settings; platform for console | P17 |
| SCR-CON-AI-03 | Evaluation dashboard | Console → AI → Evaluations | all tenant users; admin for settings; platform for console | P17 |
| SCR-CON-AI-04 | Platform notebook curation | Console → Content → Notebooks | all tenant users; admin for settings; platform for console | P17 |
| SCR-CON-AI-05 | AI kill switches | Console → AI → Controls | all tenant users; admin for settings; platform for console | P17 |
| SCR-INT-01 | Integrations home (catalogue) | Settings → Integrations | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-02 | Connector setup wizard | Settings → Integrations → [connector] → Connect | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-03 | Connector detail and health | Settings → Integrations → [instance] | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-04 | Ecosystem links | Settings → Integrations → Infrabyx ecosystem | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-05 | API clients | Settings → Integrations → API clients | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-06 | Webhooks | Settings → Integrations → Webhooks | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-07 | Mapping packs | Settings → Integrations → Mappings | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-08 | On-premises agents | Settings → Integrations → Agents | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-09 | Workplace and SSO | Settings → Security → Single sign-on & provisioning | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-10 | My calendar connection | User menu → Calendar sync | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-11 | Channels | Settings → Communications | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-12 | Website and app embeds | Settings → Grievance & help → Embeds | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-13 | eSign providers | Settings → Documents → eSign | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-INT-14 | Integration monitor (tenant) | Settings → Integrations → Monitor | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-CON-INT-01 | Platform connector catalogue | Console → Integrations → Catalogue | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-CON-INT-02 | Platform integration monitor | Console → Integrations → Monitor | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-CON-INT-03 | Certification workbench | Console → Integrations → Certification | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-DEV-01…08 | Developer portal | developers.lawdocscomply.com | ten_admin / ten_integration_admin; users (own calendar); platform for console | P18 |
| SCR-XPT-01 | Data & exports home | Settings → Data & exports | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-02 | New export wizard | Settings → Data & exports → New export | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-03 | Export job detail | Settings → Data & exports → History → [job] | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-04 | Storage targets | Settings → Data & exports → Storage targets | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-05 | Scheduled copies | Settings → Data & exports → Scheduled copies | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-06 | Folder policy | Settings → Data & exports → Folder naming | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-07 | Import folders | DMS → Import → Folder / Settings → Data & exports → Import | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-08 | Intake review queue | DMS → Import → Review queue | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-09 | Exit & deletion | Settings → Data & exports → Exit | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-10 | Download as folder (contextual) | Any list/record → ⋯ → Download as folder | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-XPT-11 | Package viewer (offline, inside export) | `00 Start Here/Open me - Viewer.html` | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-CON-XPT-01 | Platform export operations | Console → Data → Exports | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |
| SCR-CON-XPT-02 | Folder profile registry | Console → Data → Folder profiles | ten_admin; scoped roles for scoped exports; DPO for restricted | P19 |

### Screens — stream S9 (P20–P22, App N, O, X)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-BIL-01 | Pricing page | `/pricing` | anon, lead, ten_admin | P20 |
| SCR-BIL-02 | Configurator | `/pricing/build` (also embedded) | anon, lead, ten_admin | P20 |
| SCR-BIL-03 | Saved configuration | `/pricing/c/{token}` | anon, lead, ten_admin | P20 |
| SCR-BIL-04 | Compare packages (full) | `/pricing/compare` | anon, lead, ten_admin | P20 |
| SCR-BIL-05 | Add-on detail | `/pricing/add-ons/{slug}` | anon, lead, ten_admin | P20 |
| SCR-BIL-06 | Start trial | `/start` | anon, lead, ten_admin | P20 |
| SCR-BIL-07 | Organisation fetch | `/start/organisation` | anon, lead, ten_admin | P20 |
| SCR-BIL-08 | Choose sections | `/start/sections` | anon, lead, ten_admin | P20 |
| SCR-BIL-09 | Terms acceptance | `/start/terms` | anon, lead, ten_admin | P20 |
| SCR-BIL-10 | Checkout return | `/billing/checkout/return` | anon, lead, ten_admin | P20 |
| SCR-BIL-11 | Overview | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-12 | Plan & components | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-13 | Usage & limits | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-14 | Users & seats | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-15 | Legal entities | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-16 | Vidhi AI credits | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-17 | Invoices & documents | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-18 | Payments & mandates | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-19 | Billing profile | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-20 | Tax documents | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-21 | Promotions & credits | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-22 | Renewals & notices | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-23 | Purchase approvals | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-24 | Marketplace orders & retainers | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-25 | Cancel & exit | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-26 | Billing history (audit) | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-27 | Savings & Value | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-28 | Notification preferences (billing) | Settings › Billing & Membership | ten_admin (read: ten_cco, CFO) | P20 |
| SCR-BIL-40 | Pricing Studio home | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-41 | Package & component editor | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-42 | Feature rows & comparison editor | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-43 | Configurator rules editor | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-44 | Promotions | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-45 | Trial policies | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-46 | Preview & publish | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-47 | Tenant commercial panel | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-48 | Stream switches | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-49 | Reconciliation | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-BIL-50 | Savings methodology registry | apps/console | plt_super_admin, plt_finance | P20 |
| SCR-MKP-01 | Marketplace home | `/marketplace` | anon+ — category tiles, "Popular for NBFCs/UCBs/listed companies/co-operatives…" (segment presets, not popularity claims unless evidenced), search bar, "Buy services without a subscription" explainer | P21 |
| SCR-MKP-02 | Category page | `/marketplace/{category}` | anon+ — filters, ranking-parameters disclosure link | P21 |
| SCR-MKP-03 | Offering page | `/marketplace/s/{slug}` | anon+ | P21 |
| SCR-MKP-04 | Compare offerings | `/marketplace/compare` | anon+ | P21 |
| SCR-MKP-05 | Provider page (permitted modes only) | `/marketplace/p/{slug}` | anon+ | P21 |
| SCR-MKP-06 | Legal professionals directory (Rule 36 mode) | `/marketplace/directory/advocates` | anon+ — disclaimer, random/alphabetical order, Schedule fields only (only if enabled) | P21 |
| SCR-MKP-07 | Trainings (Academy) | `/marketplace/trainings` | anon+ | P21 |
| SCR-MKP-08 | Request / quote form | modal | anon → buyer | P21 |
| SCR-MKP-09 | Buyer sign-up & organisation | `/marketplace/account` | buyer | P21 |
| SCR-MKP-10 | Checkout (first-party fixed price) | P20 components | buyer, tenant | P21 |
| SCR-MKP-11 | My engagements | `/services` (in-app) and `/marketplace/my` | buyer, tenant | P21 |
| SCR-MKP-12 | Engagement Room | `/services/{engagement}` | buyer, provider | P21 |
| SCR-MKP-13 | Retainer dashboard | `/services/retainers/{id}` | buyer/tenant | P21 |
| SCR-MKP-14 | Monthly service reports archive | tab in SCR-MKP-13 | buyer/tenant | P21 |
| SCR-MKP-15 | Disputes & complaints | `/services/{engagement}/dispute` | buyer | P21 |
| SCR-MKP-20 | Offering studio (first-party) | `apps/delivery` › Marketplace › Offerings | `dlv_lead` | P21 |
| SCR-MKP-21 | Proposal builder | `apps/delivery` › Engagements › Proposal | `dlv_professional`, `dlv_lead` | P21 |
| SCR-MKP-22 | Engagement pipeline (kanban by state) | `apps/delivery` › Engagements | delivery roles | P21 |
| SCR-MKP-23 | Delivery workbench | `apps/delivery` › Engagement › Work | delivery roles | P21 |
| SCR-MKP-24 | Provider portal (external) | `providers.lawdocscomply.com` (flagged) | `mkp_provider_admin` | P21 |
| SCR-MKP-30 | Marketplace administration | `apps/console` › Marketplace (categories, profession modes, guard-rails, streams, moderation queue, provider review, grievance queue) | `plt_super_admin`, `plt_content_checker`, grievance officer | P21 |
| SCR-MKP-31 | Academy feed monitor | `apps/console` › Marketplace › Academy | `plt_super_admin` | P21 |
| SCR-SDC-01 | Portfolio home | Home | all delivery | P22 |
| SCR-SDC-02 | Work Inbox (cross-tenant, federated) | Home › My work | all delivery | P22 |
| SCR-SDC-03 | Client list | Clients | all delivery (scoped) | P22 |
| SCR-SDC-04 | Client › Overview | Clients › {client} | assigned | P22 |
| SCR-SDC-05 | Client › Work | Clients › {client} › Work | assigned | P22 |
| SCR-SDC-06 | Client › Calendar | … › Calendar | assigned | P22 |
| SCR-SDC-07 | Client › Act in tenant (launcher + grant details) | … › Act in tenant | grantees | P22 |
| SCR-SDC-08 | Client › Credentials (available to me; request; reveal) | … › Credentials | grantees | P22 |
| SCR-SDC-09 | Client › Messages | … › Messages | assigned | P22 |
| SCR-SDC-10 | Client › Files & drive | … › Files | assigned | P22 |
| SCR-SDC-11 | Client › Deliverables | … › Deliverables | assigned | P22 |
| SCR-SDC-12 | Client › Billing (read-only) & proposals | … › Billing | assigned | P22 |
| SCR-SDC-13 | Client › SLA & reports | … › SLA | assigned | P22 |
| SCR-SDC-14 | Client › Health | … › Health | assigned, `dlv_lead` | P22 |
| SCR-SDC-15 | Client › Notes | … › Notes | assigned | P22 |
| SCR-SDC-16 | Client › Activity | … › Activity | assigned, `dlv_lead` | P22 |
| SCR-SDC-17 | Grants board (all grants, expiring, pending) | Access › Grants | `dlv_lead`, RM (own) | P22 |
| SCR-SDC-18 | Access review | Access › Reviews | `dlv_lead` | P22 |
| SCR-SDC-19 | Engagements pipeline (P21) | Marketplace › Engagements | delivery | P22 |
| SCR-SDC-20 | Offering studio (P21) | Marketplace › Offerings | `dlv_lead` | P22 |
| SCR-SDC-21 | Team & assignments | Team | `dlv_lead` | P22 |
| SCR-SDC-22 | My time | Me › Time | all delivery | P22 |
| SCR-SDC-23 | My metrics | Me › Performance | all delivery | P22 |
| SCR-SDC-24 | Portfolio reports | Reports | `dlv_lead` | P22 |
| SCR-SDC-25 | Product switcher (deep links to Finbyx/Udofin/Equator/OH) | top bar | per roles | P22 |
| SCR-SDC-30 | Settings › Delivery team | apps/web › Settings › Delivery team | ten_admin (33: ten_admin, ten_cco) | P22 |
| SCR-SDC-31 | Settings › Credential Vault | apps/web › Settings › Credential Vault | ten_admin (33: ten_admin, ten_cco) | P22 |
| SCR-SDC-32 | Messages › LawDocs team | apps/web › Messages › LawDocs team | ten_admin (33: ten_admin, ten_cco) | P22 |
| SCR-SDC-33 | Delivery activity log | apps/web › Delivery activity log | ten_admin (33: ten_admin, ten_cco) | P22 |
| SCR-SDC-34 | Approve delivery grant | apps/web › Approve delivery grant | ten_admin (33: ten_admin, ten_cco) | P22 |

### Screens — stream S10 (P23, App P, R)

| Screen ID | Name | Menu path | Roles | Phase |
|---|---|---|---|---|
| SCR-WEB-01 | Home | `/` | anon, lead | P23 |
| SCR-WEB-02 | Solution (family) | `/solutions/<family>` | anon, lead | P23 |
| SCR-WEB-03 | Module | `/platform/<module>` | anon, lead | P23 |
| SCR-WEB-04 | Pricing | `/pricing` | anon, lead | P23 |
| SCR-WEB-05 | Marketplace entry | `/marketplace`, `/marketplace/<category>`, `/marketplace/<service>` | anon, lead | P23 |
| SCR-WEB-06 | Academy | `/academy` | anon, lead | P23 |
| SCR-WEB-07 | Regulatory updates index | `/regulatory-updates` | anon, lead | P23 |
| SCR-WEB-08 | Regulatory update item | `/regulatory-updates/<regulator>/<yyyy>/<slug>` | anon, lead | P23 |
| SCR-WEB-09 | Glossary index | `/glossary` | anon, lead | P23 |
| SCR-WEB-10 | Glossary term | `/glossary/<slug>` | anon, lead | P23 |
| SCR-WEB-11 | Insights / blog | `/insights`, `/insights/<slug>` | anon, lead | P23 |
| SCR-WEB-12 | Guides & checklists | `/guides/<slug>` | anon, lead | P23 |
| SCR-WEB-13 | Webinars | `/webinars`, `/webinars/<slug>` | anon, lead | P23 |
| SCR-WEB-14 | Case studies | `/customers/<slug>` | anon, lead | P23 |
| SCR-WEB-15 | Trust Centre | `/trust` | anon, lead | P23 |
| SCR-WEB-16 | Accessibility statement & ACR | `/accessibility`, `/accessibility/acr` | anon, lead | P23 |
| SCR-WEB-17 | About / Company | `/about` | anon, lead | P23 |
| SCR-WEB-18 | Contact & book demo | `/contact`, `/book-demo` | anon, lead | P23 |
| SCR-WEB-19 | Legal pages | `/privacy`, `/terms`, `/cookies`, `/refund-policy`, `/grievance-officer`, `/dpa` | anon, lead | P23 |
| SCR-WEB-20 | Campaign landing | `/lp/<slug>` | anon, lead | P23 |
| SCR-WEB-21 | Health check — start | `/health-check` | anon, lead | P23 |
| SCR-WEB-22 | Health check — organisation lookup | `/health-check/organisation` | anon, lead | P23 |
| SCR-WEB-23 | Health check — profile | `/health-check/profile` | anon, lead | P23 |
| SCR-WEB-24 | Health check — segment | `/health-check/s/<n>` | anon, lead | P23 |
| SCR-WEB-25 | Health check — review & consent | `/health-check/review` | anon, lead | P23 |
| SCR-WEB-26 | Health check — result | `/health-check/result/<id>` | anon, lead | P23 |
| SCR-WEB-27 | Health check — shared report | `/hc/r/<token>` | anon, lead | P23 |
| SCR-WEB-28 | Lead portal | `/my/reports` (magic link) | anon, lead | P23 |
| SCR-WEB-29 | Status page | `status.lawdocscomply.com` | anon, lead | P23 |
| SCR-WEB-30 | Console — CMS pages | `apps/console` → Website → Pages | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-WEB-31 | Console — page editor | Website → Pages → Edit | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-WEB-32 | Console — Claims Register | Website → Claims | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-WEB-33 | Console — Health-check studio | Website → Health check | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-WEB-34 | Console — Redirects & SEO | Website → SEO | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-WEB-35 | Console — Experiments | Website → Experiments | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-01 | Help panel (in-app) | `?` from any screen | all ten_*, anon (public help) | P23 |
| SCR-HLP-02 | Help centre home | `help.lawdocscomply.com` | all ten_*, anon (public help) | P23 |
| SCR-HLP-03 | Article | `/articles/<slug>` | all ten_*, anon (public help) | P23 |
| SCR-HLP-04 | Tutorials library | `/tutorials` | all ten_*, anon (public help) | P23 |
| SCR-HLP-05 | Tutorial player | `/tutorials/<slug>` | all ten_*, anon (public help) | P23 |
| SCR-HLP-06 | Learning paths | `/learn/<path>` | all ten_*, anon (public help) | P23 |
| SCR-HLP-07 | Release notes | `/releases` | all ten_*, anon (public help) | P23 |
| SCR-HLP-08 | Accessibility & display preferences | Profile → Accessibility and display | all users | P23 |
| SCR-HLP-09 | Report an accessibility problem | Footer / Help panel | all ten_*, anon (public help) | P23 |
| SCR-HLP-10 | Console — Glossary studio | Console → Help → Glossary | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-11 | Console — Help articles | Console → Help → Articles | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-12 | Console — Tutorials | Console → Help → Tutorials | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-13 | Console — Tours | Console → Help → Tours | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-14 | Console — Accessibility | Console → Quality → Accessibility | plt_content_maker, plt_content_checker, plt_content_publisher | P23 |
| SCR-HLP-15 | Tenant — help notes | Settings → Help & guidance | ten_admin | P23 |


## C.10 Sources (accessed 25 October 2026)

Owner's LawDocs Comply Architecture Part 1 (Visual Identity, Component Library, Layout & Navigation, Key Screens, Interaction Patterns, Design Tokens); W3C WCAG 2.2 (SC 1.4.3, 1.4.11, 2.1.4, 2.4.11, 2.5.7, 2.5.8, 3.3.7, 3.3.8) — https://dequeuniversity.com/resources/wcag-2.2 ; contrast ratios computed with the WCAG relative-luminance formula; Equator Pack v3.1 Appendix AG (navigation, Work Inbox, palette, pattern library) as internal pattern reference; ServiceNow IRM and MetricStream public product documentation (benchmarks) — https://www.metricstream.com/blog/grc-low-code-no-code.html.
