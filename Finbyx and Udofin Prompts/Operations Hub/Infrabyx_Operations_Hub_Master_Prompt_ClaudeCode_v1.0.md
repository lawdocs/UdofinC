# INFRABYX OPERATIONS HUB — Master Build Prompt for Claude Code

**Internal operations, CRM, revenue and billing, professional directory, staff HRMS, internal controls, workplace integration and engineering-assurance platform for the Infrabyx group**

Version 1.0 · 24 October 2026 · Companion to Finbyx v1.5, Udofin v1.2 and the Infrabyx Ecosystem Integration Specification v1.1

---

## HOW TO USE THIS PROMPT (for the project owner — do not paste this box)

1. **Before Session 1:** create a separate private repository, `infrabyx-ops-hub`. Each product keeps its own repository and super-admin console. Commit this entire file as `docs/00-master-prompt.md` (Parts 1–10, Appendices A–E and the Sources). Commit the Infrabyx Ecosystem Integration Specification v1.1 unchanged as `docs/ecosystem/infrabyx-integration-spec.md`, and reference copies of the Finbyx v1.5 and Udofin v1.2 master prompts as `docs/ecosystem/finbyx-master-prompt.md` and `docs/ecosystem/udofin-master-prompt.md`. The Hub implements the Hub side of Finbyx Parts 7K and 7L and Udofin Parts 7G and 7H; it does not build those Parts.
2. **Session 1:** open Claude Code on the repository and type: *"Read docs/00-master-prompt.md in full, then execute Part 10 (Phase O0 only)."* Claude Code will audit, propose and stop for your approval.
3. **After approval:** Claude Code commits `CLAUDE.md` (Appendix A), which points every later session to this prompt.
4. **Every later session:** copy one phase instruction from Part 9 at a time. Approve each specification before code is written. Phases O0 to O13 and OP follow the dependency table in Part 9.
5. **Items marked [VERIFY]** are legal, regulatory or vendor facts to re-check against the primary source before the related module is built. Claude Code records each check in the Hub's regulatory register (`docs/compliance/register.md`).
6. **Synthetic data only** until India-region hosting is in place (Part 7). No real staff identity, salary, bank or health data, no real client contact lists and no real advocate records may be loaded before then. In no environment does the Hub ever receive borrower, member or other client regulated data (Part 2.3).
7. **Your office-suite decision (needed before Phase O11; Appendix B decision 1):** you described your plan as "Microsoft 365 Business Starter". Microsoft 365's business plans are Business Basic, Business Standard and Business Premium; "Business Starter" is a Google Workspace edition. Check the admin console and record (a) which suite and plan each group company holds, (b) for Microsoft 365, whether the tenant's default geography is India and whether Advanced Data Residency is needed, and (c) whether any group company also runs Google Workspace. The Hub is built with adapters for both suites and enables only what you choose. Google Workspace offers no India data region, so it holds **non-regulated data only**: no personal data, books of account, returns, loan or HR data (Part 4.8).
8. **Shared artefacts:** the signed, versioned **Labour Code rule pack** `infrabyx-labour-rulepack` (Integration Specification Part 12.3) is maintained once and pinned by OH10 and Finbyx GV6; the **revenue catalogue** and the group's **Razorpay account** live only in the Hub (OH8); every export follows the shared **archive standard** of Integration Specification Part 12.1 (`00 Start Here` folder; each dataset as CSV, XLSX and JSON Schema; README as PDF, DOCX and TXT).
9. **Menus, screens and settings are build requirements.** Each module has `Menu and screens` and `Settings and options` subsections, consolidated in Appendix E (sidebar, role visibility, settings with defaults and floors, notifications). Every phase in Part 9 builds them; a module is not done until its screens, empty and error states and settings exist.
10. **Contract changes:** any Hub event, API, file layout or identity flow that crosses into another product is changed only through the Integration Specification change process (Specification Part 14.2), never by editing this prompt alone.

---

# PART 1 — ROLE AND WORKING AGREEMENT

Act as the Lead Software Architect, Senior Full-Stack Engineer, Business-Systems Architect (CRM, revenue operations, billing and HRMS), Indian Payroll and Labour-Law Systems Specialist, Database Architect, Security and Privacy Engineer, Internal-Controls and Assurance Specialist, QA Lead and Technical Product Partner for the development of the **Infrabyx Operations Hub** (product code `OH`).

I am the project owner. I set business objectives, approve product and policy decisions and give instructions phase by phase. You turn them into architecture, specifications, code, tests and documentation.

Do not behave merely as a code generator.

- Challenge incorrect assumptions, including mine about plan names, vendor capabilities, labour law, telecom rules and what "autopilot" can lawfully mean.
- Identify legal, privacy, financial-integrity, independence and security risks before building.
- Recommend better alternatives and explain material trade-offs before implementation.
- Do not agree with my proposals automatically. If a requested feature is impractical, insecure, legally questionable, commercially unviable or unnecessarily expensive, say why and propose a better approach.
- Ask as many questions as you need, but group them and ask only material ones. Where a sensible default exists, state it and proceed after approval.

Additional rules for the Hub:

- **The Hub runs the group, not the clients' businesses.** It never takes, records or influences a credit, KYC, classification, grievance-closure, ADR-referral, appointment-of-neutral or compliance decision of a client or of a group company's clients (Integration Specification Part 2 principle 3).
- **People decisions stay human.** No automated decision on hiring, discipline, pay, promotion or termination; AI may summarise or draft, a named manager decides (Part 4.7; OH10–OH11).
- **Controls reduce fraud; they do not eliminate it.** Never state otherwise in policy, sales or UI text.
- **No claim without evidence.** No certification, client name, regulatory endorsement or performance figure appears in any Hub-generated content without the evidence record behind it (Part 4.11; OH7).

---

# PART 2 — THE INFRABYX GROUP AND THE HUB'S PLACE IN IT

## 2.1 Group companies and products

Each group product has its own database, deployment, release cycle and super-admin console; products exchange data only through the Integration Specification, never through each other's tables.

| Group company or product | What it does | Relationship with the Hub |
|---|---|---|
| **Infrabyx** (group owner) — **Finbyx** | Staff-operated LOS, LMS, accounting, Recovery Suite, risk, returns and compliance; system of record for each client tenant; own console (Finbyx Part 3.2 workspace O) | Hub sells, onboards, supports, bills and assures; Finbyx enforces entitlements, meters usage and runs regulated functions (Finbyx Parts 7K, 7L) |
| **Infrabyx** — **Udofin** | Multi-lender LSP platform; never lends or holds funds; own platform administration | Hub runs RE partnership pipelines, implementation, vendor-side support, RE invoicing and engineering evidence; Udofin keeps borrower plans, borrower grievances and deal configuration (Udofin Parts 7B, 7C, 7G, 7H) |
| **Equator Resolution** | Independent ODR institution: conciliation, mediation, arbitration, Lok Adalat facilitation | Hub serves Equator's own back office inside an Equator-only legal-entity scope behind the Chinese wall (Part 4.4) |
| **LawDocsComply** | GRC platform for RBI, SEBI and IFSCA regulated entities; runs clients' risk and compliance logic | Hub serves its back office; client compliance content stays in LawDocsComply (Part 4.5) |
| **Future apps and group companies** (for example the field-investigation app, standalone Udolex) | New group businesses | Join the Hub as a legal entity (OH1) and the ecosystem through Integration Specification Part 11.3 |

## 2.2 What the Hub is, and what it is not

**The Hub is** the group's internal operations platform: one web application, used by staff of every group company within their legal-entity scope, for operations dashboards (OH2), an open-schema CRM (OH3), onboarding, implementation and migration (OH4), customer success (OH5), the vendor-side support desk and client complaints (OH6), marketing, brand, social media and PR (OH7), the central revenue catalogue and Razorpay billing for business customers (OH8), the group professional and advocate directory (OH9), group staff HRMS and payroll (OH10), internal controls and anti-fraud (OH11), workplace integration (OH12), the engineering-operations console (OH13) and the certification-readiness control library (OH14).

**The Hub is not:**

- **a product super-admin console.** Provisioning, feature flags, break-glass access, configuration and production operations stay inside each product. The Hub emits the signed provisioning request `TenantProvisioned` after maker-checker approval in OH4; the product creates the tenant itself and acknowledges through `PUT /v1/provisioning-requests/{id}` (Integration Specification Part 6.29). Staff are deep-linked into the product console under that product's own authentication and logging;
- **a client HRMS.** Client-company HRMS is Finbyx Part 7F GV6, running in the client's tenant;
- **a borrower-facing system.** Borrower plans, borrower billing, borrower grievances and wellness add-ons are Udofin's (Udofin Parts 7C, 7D, 7G);
- **a GRC system for clients.** Client obligations, controls and evidence belong in LawDocsComply, Finbyx M14 or the client's own GRC tool;
- **a data warehouse of group products.** It receives aggregates and metadata only (2.3).

## 2.3 What the Hub never holds

| Never in the Hub | Why | What the Hub holds instead |
|---|---|---|
| Borrower, guarantor, co-operative member, SHG or JLG member personal data | RE and LSP data-minimisation and residency duties (CF paras 13(4), 14(1), 14(4)); OUT paras 47(i), 74(vi) | Counts and amounts aggregated per tenant and period (`UsageRecorded`; Integration Specification Part 6.27) |
| Client regulated data: loans, ledgers, classifications, provisions, return contents, CIC files, KYC records, recovery and litigation files, ADR case files, compliance registers and evidence | Client confidentiality; OUT para 47(i); Equator neutrality; LawDocsComply client confidentiality | Tenant-level commercial and support metadata: organisation, contract, plan, entitlements, invoices, milestone status, ticket metadata, health-score inputs, control-total summaries signed by the client |
| Udofin wellness add-on data (credit reports, scores, expense entries) | Udofin Part 7D FW4 | Nothing; not even aggregates by user |
| Card data | CoFT circular (7 Sep 2021); PCI DSS scope | Razorpay tokens, last 4 digits and issuer name (OH8) |
| Product secrets, tenant keys, production database credentials | Separation of duties; Finbyx Part 10.6 items 18–19 | Links to product consoles; evidence records |

**Scoped support sessions are the only exception, and they copy nothing into the Hub.** With the client's authorisation, a support engineer opens a time-bound, purpose-bound session inside the product (Finbyx M19 break-glass) from a Hub ticket; the ticket stores only the session id, scope, approver and expiry, and what is viewed stays in the product. Ticket attachments holding borrower or member data are quarantined (OH6.6).

## 2.4 Data flows at a glance

- **Products → Hub:** `UsageRecorded` (aggregates; `meter_kind` USAGE or REVENUE_AGGREGATE), `ModuleAttached` and `ModuleDetached` (modules as applied), `ReleasePublished`, `ControlEvidenceCollected`, `BackupCompleted`, `RestoreTested`, `ConnectorCertified`, `AccessReviewCompleted` (`review_scope = PLATFORM` only: Infrabyx staff access to product production), `SecurityIncidentNotified` (copy), `ExportRequested` and `ExportCompleted` (status and counts), counts from external-access events, `MatterAllocated` (Finbyx R11 → OH9), and, only where the tenant opts in, status metadata of `ReturnDue`, `ReturnFiled` and `PeriodClosed` (Part 4.2). Products also call Hub APIs: provisioning acknowledgement, support tickets, CRM requests, quotes, orders, invoices, usage disputes and the catalogue (Part 6.5).
- **Hub → products:** `TenantProvisioned` (OH4 provisioning request), `ChangeApproved` (OH13 CAB record → product deployment gates), `PlanChanged`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`, `ImplementationMilestoneReached`, `SupportTicketOpened` and `SupportTicketResolved` (status for the client's in-product support page), `ProfessionalEmpanelled` and `ProfessionalSuspended` (directory), the signed revenue catalogue (Finbyx CM1.1), and conflict-check answers to Equator (OH1.6).
- **Hub internal only (`oh` scope):** `EmployeeOnboarded`, `EmployeeOffboarded`, `MailboxProvisioned` and `AccessReviewCompleted` (`review_scope = OH`) for the group's own staff. They never mix with the same-named events Finbyx GV6 and GV7 emit inside client tenants (`review_scope = TENANT`), which never reach the Hub (Integration Specification Part 6.23).

Every cross-product message follows the Integration Specification (CloudEvents envelope, signatures, idempotency, India residency). The Hub's CloudEvents `source` is `urn:infrabyx:oh:[legalentityid]`, where the tenant segment is the owning group company's `legal_entity_id` (Integration Specification Parts 3.2 and 4.6).

---

# PART 3 — USERS, WORKSPACES AND BOUNDARIES

## 3.1 User populations

- **Group staff** (employees, fixed-term staff, interns), each employed by one legal entity; **shared-service staff** employed by one company and serving several under intra-group agreements (Part 4.1); **contractors** with time-bound accounts and no restricted data.
- **Limited external users:** empanelled professionals (OH9 portal), auditors and assessors (OH14 read-only evidence rooms), client contacts (OH6 support portal, OH4 implementation portal). They never see internal CRM, HR or finance records.

## 3.2 Workspaces

Role-based workspaces show their queues, SLAs, alerts and next actions (as Finbyx Part 3.2); each is a view over shared modules, not a copy. A workspace decides which sidebar menus (Part 3.5) a role sees and what its Home shows; the full visibility matrix is Appendix E.2.

| # | Workspace | Primary users | Core jobs | Modules |
|---|---|---|---|---|
| A | Leadership | Directors, CEOs, group CFO | Dashboards, approvals above delegated limits, revenue-model review, incidents | OH2, OH8, OH11 |
| B | Delivery and implementation | Implementation managers, consultants, migration engineers | Projects, milestones, RAID, migration runs and sign-off, timesheets | OH4 |
| C | Onboarding | Onboarding coordinators, contract desk | Due diligence, contracts and DPAs, provisioning requests, kick-off, training | OH4, OH3 |
| D | Customer success | Customer success managers | Health, success plans, QBRs, renewals, expansion, NPS, exits | OH5 |
| E | Support desk | L1–L3 support, problem managers | Tickets, SLAs, escalations, problems, knowledge base, scoped sessions | OH6 |
| F | Marketing and brand | Marketing, design, content | Brand assets, calendar, campaigns, consent-gated sends, events, ads | OH7, OH3 |
| G | Social media | Social media managers | Publishing queue, social inbox, influencer register | OH7 |
| H | PR and collaborations | PR and partnerships staff | Media list, releases, coverage, collaborations, gifts register | OH7 |
| I | Sales and partnerships | Account executives, partner managers, presales | Leads, accounts, opportunities, quotes, partners | OH3, OH8 |
| J | Finance and billing | Group finance, billing operations | Catalogue, invoices, payments, dunning, revenue, vendor payments, expenses | OH8, OH11 |
| K | HR and people | HR, payroll, POSH Internal Committee (restricted) | Hire-to-retire, payroll, leave, appraisal, learning | OH10 |
| L | Security and engineering | CTO, CISO, SRE, CAB | Releases, changes, patches, VAPT, backups, incidents, access reviews, evidence | OH12, OH13, OH14 |
| M | Legal and directory administration | Group legal, directory administrators | Directory, empanelment, conflicts, contract repository | OH9, OH4 |
| N | Group-company users | Equator, LawDocsComply and future group-company staff | The same workspaces within their own legal entity and approved shared purposes | All |
| O | Internal audit and controls (read-only) | Internal auditor, Audit Committee or nominated director, assessors | Control testing, SoD and access-review evidence, whistle-blower oversight | OH11, OH14 |
| P | Hub administration | Hub administrators (no business-data rights by default) | Users, roles, entity scopes, configuration, integrations, retention | OH1 |

## 3.3 Cross-company roles

- **Grant model** (OH1; Integration Specification Part 4.6 `group_grant`): `(principal, role, entity_scope[], tenant_scope[], client_scope[], data_class_max, purpose, valid_from, valid_to, approvers[], evidence_ref)`.
- **Default deny across legal entities.** A user employed by company X sees only X's records. Any grant outside X needs a recorded purpose, the approval of the head of the principal's entity, the head of each target entity and the DPO (maker-checker; self-approval blocked), and lasts **at most 90 days**; renewal is a fresh approval, never an automatic extension (Integration Specification Part 4.6).
- **Shared services** (group finance, HR, IT, engineering) receive grants defined in the intra-group service agreement, limited to the data classes that service needs; they follow the same 90-day maximum and are reviewed in every access review. `HR` and `SPI`-class reach (Integration Specification Part 13.2) needs the DPO's specific approval.
- **Purpose binding.** Every grant carries one purpose from the Specification list: `SHARED_SERVICE_PAYROLL`, `SHARED_SERVICE_FINANCE`, `SHARED_SUPPORT`, `IMPLEMENTATION_DELIVERY`, `CUSTOMER_SUCCESS`, `GROUP_REPORTING_AGGREGATE`, `GROUP_INTERNAL_AUDIT`, `ENGINEERING_OPS`, `DIRECTORY_ADMIN`, `INCIDENT_RESPONSE`. Queries and exports are tagged with the purpose and refused if the record's purpose tags do not include it.
- **Group dashboards show aggregates only** across legal entities; record-level drill-down is limited to the user's own entity scope.
- **Access reviews:** cross-entity grants and privileged roles quarterly; all other roles half-yearly; a grant not attested within 14 days is revoked; each review emits `AccessReviewCompleted` (`review_scope = OH`) and becomes OH14 evidence.

## 3.4 Configuration boundaries

As in Finbyx Part 3.3, configuration is governed in layers: **standard core** (code: entity scoping, audit, consent gate, payroll statutory logic, claims gate), **Hub configuration** (maker-checker: pipelines, SLAs, templates, health-score weights, workflows), **regulated configuration** (needs legal or HR-compliance sign-off: Labour Code rule pack, consent texts, DLT templates, directory public fields, data-retention periods), and **feature flags**. **Configuration can never override a legal guard-rail**: for example no setting can enable keystroke monitoring, a paid directory placement, a borrower-data field in the CRM, or a promotional send without consent.

Every setting is registered once (`setting_definition`: key, module, level, default, floor or ceiling, nature, approver, effective date) and resolved in the order **platform floor → group → legal entity → team → user**; a lower level may only tighten a floor. Each module's `Settings and options` table uses four natures: **Floor** (regulatory or contractual minimum; can only be tightened), **Regulated** (changed with legal or HR-compliance sign-off), **Commercial** (owner or entity head choice) and **Personal** (the user's own preference). Every change is maker-checker, versioned and audited; Appendix E.3 is the consolidated catalogue.

## 3.5 Navigation, home and common screens

**Sidebar** (one order everywhere; a role sees only the menus its workspace grants; submenus in Appendix E.1, visibility in Appendix E.2): **Home** (OH2: role home, My Queue, notifications, saved views, dashboards) · **Clients** (OH3 accounts: client list and client 360, whose tabs appear only for modules the viewer holds) · **CRM** (OH3) · **Onboarding** (OH4) · **Success** (OH5) · **Support** (OH6) · **Marketing** (OH7) · **Revenue** (OH8) · **Directory** (OH9) · **People** (OH10) · **Controls** (OH11) · **Workplace** (OH12) · **Engineering** (OH13) · **Trust** (OH14) · **Admin** (OH1 and platform settings).

**Role home dashboards** (Home; tiles link to the governed metric and the underlying queue; each tile respects entity scope):

| Workspace | Home tiles (defaults; users may reorder, not add restricted tiles) |
|---|---|
| A Leadership | Group headlines by entity (aggregate), approvals above delegated limits, open Sev 1 incidents with clocks, MRR, collections and DSO, top churn risks |
| B Delivery | My projects by RAG, milestones due in 14 days, open RAID by severity, migration runs and sign-offs pending, utilisation (own team) |
| C Onboarding | Cases by state and age, provisioning orders awaiting gates or acknowledgement, contracts pending signature, days signature-to-tenant |
| D Customer success | Health heatmap, renewals in 120 days, detractors awaiting follow-up, QBRs due, churn-risk save plans |
| E Support | My Queue by time-to-breach, unassigned triage, Sev 1 and 2 open, SLA attainment (team), RE escalations with RE deadlines |
| F–H Marketing, social, PR | Items awaiting my review, scheduled posts, campaign send-gate refusals, inbox items by classification, coverage this month |
| I Sales | My pipeline by stage, stale opportunities (no activity in 30 days), quotes awaiting approval, due-diligence blockers, leads awaiting first touch |
| J Finance | Invoices due today, payment failures and dunning stages, usage disputes, settlement breaks, revenue-recognition run status |
| K HR | Joiners and leavers this week, payroll run status and variance, final settlements on the 2-working-day clock, leave approvals |
| L Security and engineering | Vulnerabilities past SLA, changes awaiting CAB, incidents with clocks, restore-test status, evidence freshness |
| M Legal and directory | Empanelment queue, credentials expiring in 60 days, conflict-check log, contracts awaiting legal review |
| O Internal audit | Control-test exceptions, SoD exceptions expiring, access-review completion, whistle-blower case ageing (counts only unless designated) |
| P Hub administration | Grants expiring in 14 days, pending grant approvals, integration health, failed jobs and DLQ, audit-chain verification |
| Employee self-service (all staff) | My tasks, leave balance, latest payslip, timesheet due, policy attestations due |

**Common screen rules (every module):**

- **Screen types:** list (filters, saved views, bulk actions, export), detail (header with state, owner, entity badge, clocks; tabs; timeline; audit trail), create or edit wizard (inline validation, explain-why messages naming the rule and citation), approval queue (maker, what changed, evidence, fresh MFA to approve, reject with reason), dashboard.
- **Global search** (`Ctrl+K` or `Cmd+K`): one box over clients, contacts, leads, opportunities, tickets, projects, invoices, professionals, employees and policies; results are filtered by the same RLS and grant policy as a direct read, show the entity badge, never show RESTRICTED field snippets, never return Equator records outside Equator scope, and are logged; exact matching on CIN, GSTIN, invoice and ticket numbers; queries containing PAN- or Aadhaar-like patterns are refused with a reason.
- **Notification centre:** bell with tabs Action needed, Clocks, Mentions and Updates; channels in-app, email and Teams or Google Chat (OH12); SMS only for Sev 1 on-call through a DLT service template. Approvals, regulatory clocks and security alerts are **mandatory** (cannot be muted; quiet hours do not apply); other items follow the user's preferences and a daily digest. Message bodies never carry RESTRICTED data; they link to the record. Catalogue: Appendix E.4.
- **Saved views:** any list's filters, columns and sort saved as personal, team or entity views and pinned to Home; a shared view stores the query, never the results, so each viewer sees only what their grants allow; exports from a view obey export permissions.
- **Productivity:** My Queue sorted by time to breach; keyboard shortcuts on heavy screens (`J` and `K` next and previous, `A` assign, `E` edit, `/` filter); bulk actions show a preview and count before running; undo for 10 seconds on non-financial edits.
- **Empty and error states:** every list explains what will appear and how to start ("No tickets yet: tickets raised in Finbyx appear here"); an integration outage shows a banner with the last successful sync and never blocks unrelated work.
- **Accessibility and locale:** WCAG 2.2 AA; English and Hindi for client and staff self-service; lakh and crore; DD-MM-YYYY; IST; the acting legal entity always visible.

---

# PART 4 — LEGAL, DATA AND INDEPENDENCE BOUNDARIES

## 4.1 DPDP roles between group companies

Every processing activity in the Hub has a recorded fiduciary, processor and purpose (Digital Personal Data Protection Act 2023 and Rules 2025; Rules notified 13 Nov 2025; core obligations from 13 May 2027 [VERIFY: whether MeitY compressed the timeline]; until then IT Act s.43A and the SPDI Rules 2011 apply). The table is the starting position; Phase O0 confirms it with counsel.

| Processing | Data fiduciary | Processor | Basis | Agreement |
|---|---|---|---|---|
| Hub platform operation | Each group company for its own records | The Hub operator company [owner to name it] | Per activity | Intra-group DPA: purpose, security, sub-processing, 24-hour breach notice, return and deletion, audit [REC] |
| Staff HR and payroll of each group company | The employing company | Shared HR and payroll function of the Hub operator | DPDP s.7(i) legitimate use for employment, plus consent where required (Part 4.7) | Intra-group DPA plus staff privacy notice |
| CRM and marketing of each company | The company whose prospects they are | Hub operator; Brevo and other marketing vendors as sub-processors | Consent for marketing (DPDP s.6); legitimate-use grounds do not cover marketing | DPA with each vendor; sub-processor register |
| Support tickets from client staff | The group company providing the service | Hub operator | Business relationship under the client contract; notice | Client MSA privacy clause |
| Client tenant data viewed in a scoped support session | The client (or the RE whose data it is) | The product company, with the Hub operator as sub-processor when its staff do the work | The client's instructions | Client MSA and DPA; sub-processor listed (4.3) |
| Professional directory | The Hub operator for the group directory | — | Consent of the professional; Rule 36 limits (4.9) | Empanelment terms |

Each intra-group DPA also states that no group company may use another's records for its own marketing without a fresh lawful basis, and that the receiving company deletes or returns data when the purpose ends (DPDP s.8(7)).

## 4.2 Intra-group outsourcing where a regulated entity is involved

- **If a group company is, or becomes, an RBI-regulated entity**, its use of the Hub or shared group services is intra-group outsourcing: Board-approved policy and SLAs covering shared premises and staff (OUT para 45); customers told which company provides each product (para 46); written terms on scope, charges, customer-data confidentiality, stand-alone risk management, RBI access and compliance with RBI directions (para 47); continuity if group services fail (para 48); no advertisement implying responsibility for group obligations (para 50); identical risk practices (paras 51, 92); objective selection and conflict management for IT services (paras 90–91).
- **For unrelated client REs that use several group companies** (for example Finbyx and LawDocsComply), each group company remains a separate service provider with its own contract, data segregation and incident duties. The Hub must never become an unapproved channel between them: no shared support desk view across two products' tenant data for one client unless both contracts list the Hub operator as a sub-processor, and the client's records in one product never inform another company's sales without the client's written authorisation.
- **Status-only regulatory calendar events.** Finbyx emits `ReturnDue`, `ReturnFiled` and `PeriodClosed` for a client (Finbyx Part 7B RR5; Integration Specification Parts 4.6, 6.18, 6.20). The Hub receives them only where the tenant opts in to Infrabyx filing-support monitoring (for example a group company that uses Finbyx as its own tenant, or a client that has contracted a managed-operations service and authorised the feed in writing). The Hub stores return code, period, due date and status only: never return contents, amounts or hashes, and never `InterestCertificateIssued` or any other borrower-level document event.

## 4.3 Sub-processor position for client contracts

When Hub-operator staff provide support, implementation or migration for Finbyx, Udofin, Equator or LawDocsComply clients, the Hub operator is a sub-processor of that product company. It appears in each product's sub-processor list with prior client consent before appointment or change (OUT paras 34(iv), 74(xi), 82; Finbyx Part 10.6 item 15), and its staff follow the client's information-security and acceptable-use policies (Finbyx Part 10.6 item 8).

## 4.4 Equator Resolution neutrality (Chinese wall)

Equator must be independent of the lenders whose disputes it hears and of the group companies that serve them (Integration Specification Parts 4.6 and 8.6; Arbitration and Conciliation Act 1996 s.12 with the Fifth Schedule grounds, the Sixth Schedule disclosure form and the Seventh Schedule ineligibility grounds; Mediation Act 2023 [VERIFY: mediator conflict-disclosure section and commencement]).

- **Separate legal-entity scope** for Equator with its own keys, administrator group and support queue.
- **Separation of duties at grant:** no grant combines an Equator case-level role (case manager, panel administrator, neutral) with any Finbyx, Udofin, LawDocsComply or RE-facing sales, collections or customer-success role (Integration Specification Part 4.6).
- **Equator staff never see** lender-side commercial data of any party to an Equator case (pipeline, contract values, revenue, health scores, tickets, notes); enforced by entity scope plus a **case-party block list** fed by Equator (OH1.6).
- **Finbyx, Udofin and LawDocsComply staff never see** Equator dockets, panels, appointments or outcomes; the Hub holds only Equator's own commercial records and case counts by status, and no dashboard joins Equator outcomes with lender commercial or collections data.
- **Conflict checks** before any appointment use `POST /v1/conflicts/check` (OH1.6), which returns only counts and a flag with its category, enough for Equator's Sixth and Seventh Schedule disclosure and per-lender caps; Finbyx R11 receives the identity-level `equator_neutral` flag so that an Equator neutral is never allocated as counsel in a matter that RE has referred to Equator [REC].
- **Commercial separation:** no bundle, discount or incentive linking Equator fees or referral volumes to any other group contract; Equator is never the default ODR provider in group material; no group sales commission on Equator referrals [REC].
- **Wall-breach log** of attempted and blocked cross-wall access, reviewed monthly by Equator's independent oversight.

## 4.5 LawDocsComply client confidentiality

LawDocsComply holds clients' obligation registers, compliance issues, incidents, risk data and evidence. That content stays in LawDocsComply. The Hub holds only LawDocsComply's commercial and support metadata for each client (organisation, plan, contract, invoices, ticket metadata, usage aggregates). LawDocsComply's knowledge of a client's compliance weaknesses must never be used to sell Finbyx, Udofin or any other group service to that client, or be visible to their sales teams, without the client's written authorisation [REC; OUT para 47(i) for RE clients].

## 4.6 Marketing communications law

- **TRAI TCCCPR 2018, as amended 12 Feb 2025:** commercial SMS only through DLT with registered principal-entity, header and template ids and the correct category; promotional messages carry an opt-out; after an opt-out, wait 90 days before seeking consent again; transactional consent lasts 7 days; ordinary 10-digit numbers are barred for telemarketing; promotional voice uses the **140-series** through a registered telemarketer; advance notice to the originating access provider before auto-diallers or robo-calls (reg 4); repeated breaches lead to disconnection and blacklisting (TRAI press release 11/2025, 12 Feb 2025) [REG].
- **1600-series** numbers are mandatory for service and transactional calls of RBI-regulated entities (TRAI Direction, 19 Nov 2025). The Infrabyx group companies are not REs; whether they may use 1600-series numbers for their own service calls is unconfirmed [VERIFY with DoT or TRAI]. Until confirmed, the Hub runs no automated or bulk voice service campaigns from group numbers; one-to-one calls by named staff about an existing contract or an inbound enquiry are allowed and logged (OH3, OH7).
- **DPDP consent for marketing:** explicit, purpose-specific, withdrawable consent after notice (DPDP ss.5–6), withdrawal as easy as giving it, evidence retained; business contact details of individuals are personal data. Self-published professional profiles may fall outside the Act [VERIFY: DPDP s.3(c)(ii)] but are never used for messaging without consent.
- **RE-facing and borrower-facing content:** any campaign that names a client RE or promotes a loan product needs that RE's written approval and follows the RE's obligations (RBC Second Amendment Directions 2026, Chapter IIIA, issued 15 Jun 2026 and effective 1 Jan 2027 [VERIFY: final NBFC text and paragraph numbers]; OUT paras 46, 49–50). The Hub never runs borrower marketing on behalf of an RE.
- **Advertising and endorsements:** ASCI Code; ASCI influencer guidelines; CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements 2022 and Dark Patterns Guidelines 2023; SEBI's restriction on regulated persons associating with unregistered persons who give securities advice or make return claims, where content touches investments [VERIFY: current texts] (OH7).

## 4.7 Staff data, monitoring and the Labour Codes

- **Labour Codes** in force from 21 Nov 2025; Central Rules notified 8 May 2026 (G.S.R. 342(E)–345(E); corrigendum G.S.R. 629(E) of 15 Jul 2026); State rules partly notified [VERIFY: Delhi, Uttar Pradesh and Rajasthan status]. Appointment letters, wage definition (50% rule), final wages within 2 working days, deduction cap, working hours, overtime caps and leave are implemented in OH10 through the shared rule pack `infrabyx-labour-rulepack` (Integration Specification Part 12.3; LC: Code on Wages s.2(y), s.17(2), s.18; OSHWC Code s.32).
- **DPDP s.7(i):** employment purposes and safeguarding the employer from loss or liability are legitimate uses without consent [VERIFY: final wording], but notice, minimisation, security safeguards, erasure when purposes end (s.8(7)) and processor contracts (s.8(2)) still apply.
- **Monitoring must be lawful, necessary and proportionate** (*K.S. Puttaswamy v Union of India* (2017) 10 SCC 1): login and logoff, self-entered timesheets, device-compliance status and security logs are allowed with notice; keystroke or mouse "activity" scoring, screenshots, webcam capture and off-duty location tracking are not built (OH10, OH11).
- **POSH Act 2013:** an Internal Committee at each office or administrative unit with 10 or more employees (s.4); complaint and inquiry contents may not be published or made known (s.16); the Committee's annual report goes to the employer and the District Officer (s.21) and the Board's report carries the disclosure (Companies (Accounts) Rules as amended 2025). Case records are a RESTRICTED class visible only to the Committee and, in aggregate, to the Board-report owner.
- **Books and payroll records:** wage registers kept electronically for 5 years after the last entry (Wages (Central) Rules 2026 r.51); books of account accessible in India with daily backup on servers in India (Companies (Accounts) Rules 2014 r.3(5)).

## 4.8 Workplace suites and data residency

- **Microsoft 365** tenants with default geography India keep Exchange, SharePoint, OneDrive and Teams data at rest in India; Advanced Data Residency covers further workloads [VEND: Microsoft 365 data-residency product terms].
- **Google Workspace** data regions offer only the United States or Europe, and Business Starter offers none [VEND: Google Workspace data-regions documentation; VERIFY: current region list]. Therefore **Google Workspace (Drive, Gmail, Chat, Calendar attachments) holds non-regulated data only: no files or records containing personal data, no books of account, returns, loan, borrower, member, client tenant or HR data**. Implementation and support staff may not download client data to Google Drive, Gmail or personal devices; the Hub's DLP rules block attachments from scoped support sessions, migration runs, payroll and HR from being shared to Workspace (OH12).
- Infrabyx internal documents without personal data (policies, proposals, marketing material, templates) may sit in either suite according to the owner's decision; HR, payroll and other personal-data documents sit only in the Hub's India store or in Microsoft 365 with India data location evidenced.

## 4.9 Professional and advocate directory (BCI Rule 36)

Advocates may not solicit work or advertise, directly or indirectly (Bar Council of India Rules, Part VI, Chapter II, Section IV, Rule 36; breach is professional misconduct under Advocates Act 1961 s.35). Website information is permitted only as in the BCI Schedule: name, address, contact details, enrolment number and date, State Bar Council, professional qualifications and areas of practice (BCI Resolution 50/2008). Ratings, "top" or "premium" labels, success rates, fees, testimonials and paid placement are prohibited, and a "mere directory" is no defence (*P.N. Vignesh v Bar Council of India*, Madras HC, 2024 [VERIFY: citation]). Internal panel scorecards used by a client RE to allocate matters stay internal to that RE (OH9; Finbyx R11).

## 4.10 Cyber incidents and logs

- **CERT-In Directions (28 Apr 2022, under IT Act s.70B(6))** bind every group company as a body corporate: report listed incidents within **6 hours** of noticing; nominate a point of contact; synchronise clocks to NIC or NPL NTP servers; keep logs for a rolling **180 days within India** [REG].
- **Client REs** must report to RBI within 6 hours of detection by the service provider, so group companies notify affected REs without undue delay, target **≤ 2 hours** from detection, through `SecurityIncidentNotified` (OUT para 61; Integration Specification Parts 3.8 and 6.15; Finbyx Part 10.6 item 6).
- **DPDP:** personal-data breaches notified to the Data Protection Board without delay and in detail within 72 hours, and to affected data principals, once the duty commences (13 May 2027 [VERIFY]); logs kept at least 1 year (DPDP Rules r.8(3)).
- The Hub is the group's incident register and clock-keeper (OH6, OH13); each product still runs its own detection and response.

## 4.11 No certification claims

PCI DSS, SOC 2 Type 1 and Type 2, ISO/IEC 27001, 27701, 22301 and 42001 are a **readiness programme** (OH14; Finbyx Part 7L EO5). Until a report or certificate is issued, group material says "aligned to" or "in progress". Razorpay's PCI DSS status is Razorpay's, never Infrabyx's. The claims gate (OH7.5) blocks any content that says otherwise.

## 4.12 Requirement codes used in this prompt

This prompt uses the Direction and requirement codes of Finbyx Part 8A and 8A.37: `OUT`, `CF`, `CYB`, `RBC`, `RBIOS26`, `IO26`, `EMD`, `PA`, `CA13`, `DPDP`, `TRAI`, `CERTIN`, `LC`, `ITA25`, `GST`, `ASCI`, `CCPA`, `CPA19`, `PCI`, `SOC2`, `ISO`, `BCI` (Bar Council of India Rules, Part VI) and `POSH` (Sexual Harassment of Women at Workplace Act 2013). It adds one Hub code, for proposal to Finbyx Part 8A.37 [REC]: `PCA88` (Prevention of Corruption Act 1988, s.9 as amended 2018). Hub requirement identifiers take the form `REQ-OH[n]-[seq]`, cross-referenced to the source code, for example `REQ-OH3-07 → TRAI TCCCPR reg 4`.

---

# PART 5 — FUNCTIONAL MODULE SPECIFICATION

Each module states its purpose, users, data model, workflows, rules and guard-rails with citations, integrations and events, configuration and acceptance tests. Modules OH1–OH7 are specified here; OH8–OH14 follow. Conventions for every module:

- **Scoping columns on every record:** `legal_entity_id`, `client_org_id` where relevant, `data_class` and `purpose_tags[]`; Postgres RLS enforces entity and class, the policy layer enforces purpose (Part 3.3). Hub classes are `PUBLIC`, `INTERNAL`, `CONFIDENTIAL` (commercial terms, business contacts) and `RESTRICTED` (HR, payroll, POSH, whistle-blower, investigations); on any cross-product message they map to Integration Specification Part 13.2 (`RESTRICTED` → `HR`, `SPI` or privileged `LEGAL`), and Hub subjects accept at most `INTERNAL` from product sources.
- **Hash-chained audit** of every create, update, approval, export and permission change (Finbyx M19 pattern); **maker-checker** on sensitive actions; nobody approves their own request.
- **Open data:** documented schema, internal API (OpenAPI 3.1) and full export in the Integration Specification Part 12.1 archive standard for every object (Hub folder profile `oh_entity_v1`, to be registered by proposal under Specification Part 14.2).
- **Menus, screens and settings:** each module ends with `Settings and options` (level, default, nature per Part 3.4) and `Menu and screens` (path, screens and actions, roles) tables; the common screen rules of Part 3.5 apply to every screen.
- **AI assistance** drafts, summarises, classifies and suggests; a named human confirms every consequential action (RBI FREE-AI Committee report, 13 Aug 2025, applied as good practice). Every AI output stores model, version, prompt version and the reviewer's decision.

---

## OH1. Group identity, legal entities and cross-company roles

**Purpose.** Give every person one identity across the group, scope everything they can see to the right legal entity and purpose, and provide the conflict service that protects Equator's independence. OH1 is the foundation that every other module relies on (Phase O1–O2).

**Users.** Hub administrators; HR (joiner, mover, leaver triggers); entity heads and the data-protection lead (approvals); internal audit (read-only); Equator's case system (conflict API, machine client).

### OH1.1 Data model

| Entity | Key fields |
|---|---|
| `legal_entity` | id, `org_id` (Integration Specification Part 4.1), legal name, constitution, CIN, PAN (masked plus token), GSTIN per State, LEI, registered office, `group_role` (OWNER, PRODUCT_COMPANY, ODR_INSTITUTION, GRC_PROVIDER, OTHER), email domains, status, effective dates |
| `office` | entity, address, State (drives Shops and Establishments Act, holidays, professional tax and LWF tables in OH10), headcount band, registrations |
| `department`, `cost_centre` | entity, parent, head, budget owner (customisable per entity) |
| `person`, `employment` | one person per human (`person_ref`; HR attributes live in OH10 as `RESTRICTED`); employments by entity, type (EMPLOYEE, FIXED_TERM, INTERN, CONTRACTOR, CONSULTANT), department, manager, dates |
| `user_account`, `role` | IdP subject, SCIM id, MFA and device-compliance status, last sign-in; roles with workspace, permissions, `data_class_max`, `sod_group` (OH11), privileged flag |
| `group_grant` | principal, role, `entity_scope[]`, `tenant_scope[]`, `client_scope[]`, `data_class_max`, purpose code, valid_from, valid_to (≤ 90 days), approvers, justification, `evidence_ref` (intra-group agreement or DPA clause), state, review due (Integration Specification Part 4.6) |
| `purpose_code` | code, description, lawful basis, permitted data classes, permitted entities, owner |
| `case_party_block` | `org_id`, source (Equator), as-of, expiry; identifiers only |
| `relationship` | person or legal entity ↔ client `org_id`, type (EMPLOYEE_ON_ACCOUNT, EMPANELLED_COUNSEL, CONSULTANT, DIRECTORSHIP, SHAREHOLDER, COMMERCIAL_CLIENT), from, to; used by the conflict service |
| `conflict_check_log` | request id, caller (Equator machine client), subject ref, counterparty `reid` or `org_id`, window, answer (count, flag, category), as_of; no case details |

### OH1.2 Identity and authentication

- OIDC sign-in against the group IdP chosen in Appendix B (Entra ID or Google), behind an OIDC abstraction (Finbyx Part 10.1); SCIM 2.0 provisioning; no Hub passwords; MFA for every account and phishing-resistant MFA (FIDO2) for privileged roles [REC].
- **Leavers:** accounts disabled within 4 hours of `EmployeeOffboarded`, privileged accounts within 1 hour (Integration Specification Part 4.2 [REC]); sessions revoked at the IdP.
- A Hub role never implies a product role; product access is requested through the OH12 joiner workflow and granted by the product's own administrators.

### OH1.3 Legal-entity onboarding

`DRAFT → VERIFIED (CIN, PAN, GSTIN checked) → AGREEMENTS_SIGNED (intra-group service agreement and DPA, Part 4.1) → CONFIGURED (offices, departments, calendars, domains) → ACTIVE → DORMANT → CLOSED`

No users, CRM records or payroll before `ACTIVE`; a failed verification returns the entity to `DRAFT` with the reason; `DORMANT` (no business for 12 months, by director decision) blocks new records but keeps read access; closing needs every open contract, payroll and ticket transferred or closed, then archives records under the retention policy and legal holds. The entity is registered in the ecosystem organisation registry with `is_group_operator = true` (Integration Specification Part 4.1).

### OH1.4 Grant lifecycle and authorisation

| State | Entry | Exit and timer | Owner and allowed actions |
|---|---|---|---|
| `REQUESTED` | Request wizard with purpose, scope, class, dates and evidence ref; SoD pre-check run | Approvals within 5 working days, else `LAPSED` | Requester may edit or withdraw |
| `APPROVING` | First approval recorded | All of: head of the principal's entity, head of each target entity, DPO (any cross-entity grant; specific approval for `HR` or `SPI` reach); any rejection → `REJECTED` with reason | Approvers approve with fresh MFA; nobody approves their own request |
| `ACTIVE` | Last approval; SCIM membership with `valid_to` pushed to each product | `valid_to` reached → `EXPIRED` automatically (enforced in each product, no Hub job needed); leaver, SoD breach or security event → `REVOKED` at once | Holder uses; owner or DPO may revoke |
| `EXPIRING` | T−14 days | Renewal is a new `REQUESTED` grant with fresh approvals, never an extension | Notifications to holder, manager and approvers |
| `EXPIRED`, `REVOKED`, `REJECTED`, `LAPSED` | As above | Terminal; kept for audit | Read-only |

- **Default deny** across legal entities; cross-entity grants last at most 90 days and products end sessions within 60 seconds of expiry or revocation (Part 3.3; Integration Specification Part 4.6).
- **SoD check at grant time** against the OH11 conflict matrix (for example vendor creation with payment release, employee creation with payroll approval, user administration with any finance role); a conflicting grant needs a director's exception with an expiry.
- **Authorisation engine:** RBAC plus ABAC (Cedar or OpenFGA, as Finbyx Part 10.1) with Postgres RLS as defence in depth; field-level masking by role (for example salary, bank account and personal contact fields).
- **Break-glass for Hub administrators:** two-person approval, 4-hour maximum, every action logged and reviewed within 2 working days.

### OH1.5 Access reviews

Cross-entity grants and privileged roles quarterly, all other roles half-yearly: each manager attests or revokes each grant; unattested grants are revoked after 14 days; dormant accounts (no sign-in for 45 days) are disabled [REC]. Campaigns run in `Controls › Access reviews` (OH11.4). Completion emits `AccessReviewCompleted` (`review_scope = OH`) with counts only, and the review pack becomes OH14 evidence.

### OH1.6 Equator conflict service

- **Inbound feed:** Equator's case system pushes `case_party_block` entries (party `org_id`s of open cases and cases closed within 3 years) through a machine client; no case details.
- **Wall enforcement:** for users in Equator's entity scope, every query adds `client_org_id NOT IN case_party_block` for records outside Equator's own scope; for users outside Equator, Equator's records are invisible (Part 4.4).
- **API** `POST /v1/conflicts/check` (Equator machine client only; Integration Specification Part 6.29): input `professional_id` (or `person_ref` for Infrabyx staff and consultants), counterparty `reid` or `org_id`, and `window` (ISO 8601 duration, default `P3Y`); output the **count of allocations** by that counterparty in the window (from OH9 `MatterAllocated`), a `conflict` flag with `category` (EMPLOYMENT, COUNSEL, CONSULTANCY, DIRECTORSHIP, GROUP_COMMERCIAL_RELATIONSHIP) and `as_of`. **Counts and flags only**: never matter, contract-value or pipeline data. Idempotency-Key required; p95 ≤ 800 ms; every call and answer is logged in `conflict_check_log`.
- **Look-back** default 3 years for employment, counsel and consultancy relationships; Equator may ask for a longer window, never a shorter one [REC; aligned with the 3-year periods in the A&C Act Fifth Schedule; Integration Specification Part 8.6].
- **Failure path:** if the service is unavailable, Equator's process treats the answer as unknown and pauses the appointment; the Hub never returns a cached "no conflict".

### OH1.7 Integrations and events

Consumes `EmployeeOnboarded`, `EmployeeOffboarded` (`oh` scope, from OH10) and `MailboxProvisioned` (from OH12); emits `AccessReviewCompleted` (`review_scope = OH`). The ecosystem organisation registry and tenant map (Integration Specification Part 4.1) are ecosystem services, not Hub tables: OH1 registers group companies there with `is_group_operator` and reads `org_id`s and tenant-map entries read-only.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Cross-entity grant maximum | Platform | 90 days | Floor (cap); entities may shorten |
| Grant approvers | Platform | Principal's entity head, each target entity head, DPO | Floor |
| Access-review cadence | Platform | Quarterly for cross-entity and privileged; half-yearly others | Floor; may be more frequent |
| Unattested-grant revocation | Platform | 14 days | Floor (maximum) |
| Dormant-account disable | Entity | 45 days without sign-in [REC] | Commercial; may shorten |
| Leaver disable | Platform | 4 hours; privileged 1 hour | Floor |
| Break-glass maximum | Platform | 4 hours, two-person approval | Floor |
| MFA | Platform | All accounts; FIDO2 for privileged roles | Floor |
| Idle session timeout | Entity | 30 minutes; privileged 15 minutes [REC] | Commercial; may shorten |
| Conflict look-back | Platform | `P3Y` | Floor (minimum) |
| Purpose codes and field data classes | Group | Integration Specification Part 4.6 list | Regulated (DPO) |
| Holiday calendars and working week | Office | State calendar | Commercial |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Admin › Legal entities` | List by state; entity wizard (OH1.3 states, verification evidence, agreements, offices, domains); detail with registry link and closure checklist | Hub administrators (maker), director (checker) |
| `Admin › Offices and calendars` | Offices by State with registrations; State holiday calendars; working-day calculator preview | Hub administrators, HR |
| `Admin › Org structure` | Departments and cost centres tree per entity; owners; bulk import with dry run | Hub administrators, finance |
| `Admin › Users` | Accounts with MFA, device and last sign-in; disable, revoke sessions; SCIM status per product; filters dormant, privileged, contractor | Hub administrators |
| `Admin › Roles` | Role catalogue with permissions, `data_class_max`, SoD group, privileged flag; diff before change | Hub administrators (maker), CISO (checker) |
| `Admin › Grants` | Request wizard with live SoD and wall check; approval queue; expiring in 14 days; revoke (single or bulk with reason); grant-use log | All staff (request); approvers; DPO; internal audit (read) |
| `Admin › Purpose codes` | Codes, lawful basis, permitted classes and entities; version history | DPO |
| `Admin › Equator wall` | Block-list feed status and counts; wall-breach log; conflict-check log (counts only) | Equator independent oversight; CISO (read) |
| `Admin › Break-glass` | Request, two-person approval, live sessions with timer, post-session review queue (2 working days) | Hub administrators, CISO |
| `Admin › Audit log` | Search by actor, entity, object and action; chain-verification status and anchors; export with second approver | Internal audit, CISO |

Empty and error states: a grant request that fails SoD or the wall explains which rule blocked it and who may grant an exception; an IdP or SCIM outage shows the queued changes and escalates leaver removals to the manual runbook (Part 6.5).

### Acceptance tests

- A LawDocsComply employee with no cross-entity grant receives no Finbyx CRM record through the UI, the API, search or an export.
- A cross-entity grant without the data-protection lead's approval cannot become `ACTIVE`; an `ACTIVE` grant stops working at `valid_to` without any job running late.
- Granting `vendor_create` to a user who holds `payment_release` is refused with `sod_conflict` unless a director's time-bound exception is attached.
- An Equator user cannot open the Finbyx opportunity for an RE listed in `case_party_block`, and the denied attempt appears in the wall-breach log.
- For a counsel empanelled for that RE two years ago, the conflict API returns only the allocation count, `conflict`, `category` and `as_of`, and `false` after the look-back has passed; a request with a window shorter than `P3Y` is refused.
- A grant combining an Equator panel-administrator role with a Finbyx customer-success role is refused at request time.
- An `EmployeeOffboarded` event disables the Hub account within 4 hours (1 hour for a privileged role), verified by a scheduled test with a synthetic leaver.

---

## OH2. Operations dashboards

**Purpose.** One governed set of operational dashboards for leadership and each workspace, built on defined metrics rather than ad hoc counts, separate from every product's super-admin monitoring (owner requirements 5 and 35).

**Users.** All workspaces, each seeing its own dashboards within its entity scope; leadership sees group aggregates.

### OH2.1 Governed metric layer

- **`metric_definition`:** formula, grain, source, owner, version, effective_from, `data_class`, scope rule, visibility (`TEAM`, `ENTITY`, `GROUP_AGGREGATE`, `INDIVIDUAL_RESTRICTED`), thresholds; every number shows its definition and version (as Finbyx Part 7E RK6).
- **Individual metrics** (for example tickets closed per agent, utilisation per consultant) are visible only to the person and their line manager, and never as a ranked league table [REC; Part 4.7]. Group views across entities are aggregates only.
- **Sources:** Hub modules only, including the aggregated product events they store (`UsageRecorded`, `ReleasePublished` and others in Part 2.4). No dashboard reads a product database.

### OH2.2 Dashboard catalogue

| Dashboard | Key measures | Owner |
|---|---|---|
| Delivery | Projects by phase; milestone on-time rate; schedule variance; budget burn; open RAID by severity; migration reconciliation status; team utilisation | Head of delivery |
| Onboarding | Signature to tenant provisioned (days); due-diligence items outstanding; time to first value (signature to first production transaction or approved return); training completion | Head of onboarding |
| After-sales and customer success | Health distribution and movement; renewals due in 30–120 days; renewal rate; expansion pipeline; QBR coverage; NPS and CSAT; churn-risk list | Head of customer success |
| Support (SLA) | Open tickets by severity and age; response and resolution SLA attainment; reopen rate; tickets per 100 active users; open problems; cost per ticket | Head of support |
| Grievance (vendor-side) | Client complaints by category and status against targets; RE escalations awaiting vendor input with RE deadlines; repeat themes | Grievance officer for business customers |
| Marketing and brand | Leads by source; funnel conversion (lead, MQL, SQL, opportunity, won); cost per lead and opportunity; consented audience and opt-out rate; claims-gate rejections | Head of marketing |
| Social media | Posts against plan; engagement rate (interactions ÷ impressions); follower growth; inbox response time | Social media manager |
| PR and collaborations | Releases; coverage and tone; share of voice [REC: licensed monitoring feed]; collaborations by stage; event leads and cost; gifts-register exceptions | PR lead |
| Sales pipeline | Pipeline by stage and product; weighted forecast; win rate; sales cycle; due-diligence blockers | Head of sales |
| Revenue | MRR, ARR, new, expansion, contraction and churned MRR; logo churn; NRR and GRR; billings, collections, DSO; revenue by stream; usage run-rate; recognised against billed (OH8) | Group CFO |
| HR | Headcount and FTE; joiners, leavers, attrition; time to hire; leave liability; payroll cost; final-settlement timeliness (2 working days); appraisal and training completion | Head of HR |
| Security and engineering | Vulnerabilities past SLA; incidents with clock compliance (2-hour RE notice, 6-hour CERT-In); emergency changes; change-failure rate; restore-test status; open VAPT findings; access-review completion; evidence freshness | CISO |
| Leadership (group) | Headlines from each dashboard, per entity and in aggregate | Group CEO |

### OH2.3 Revenue and customer-health definitions

```
MRR(month)          = Σ normalised monthly recurring charges active on the last day of the month
                      (subscriptions, monthly rental, committed minimums); excludes one-time,
                      implementation, professional services, pass-through and pay-as-you-go
usage_run_rate      = trailing-3-month average monthly pay-as-you-go and pass-through margin (shown separately)
ARR                 = MRR × 12
new_MRR             = MRR from accounts with no MRR in the prior month
expansion_MRR       = increase in MRR for existing accounts (upgrades, add-ons, seats, price rises)
contraction_MRR     = decrease in MRR for accounts still active
churned_MRR         = MRR of accounts whose recurring MRR fell to zero in the month
NRR(12m)            = (MRR_start + expansion − contraction − churned) ÷ MRR_start, same cohort
GRR(12m)            = (MRR_start − contraction − churned) ÷ MRR_start
logo_churn(period)  = accounts lost ÷ accounts at start of period
CAC_payback(months) = sales and marketing cost for the cohort ÷ (new_MRR × gross margin %)
DSO                 = trade receivables ÷ billings over the last 90 days × 90
```

- MRR and ARR come only from the OH8 subscription ledger, never from CRM opportunity values. Recognised revenue follows the framework chosen by the owner (AS 9 or Ind AS 115 [VERIFY: Infrabyx reporting framework]; Appendix B).
- **Customer health score** (0–100; weights configurable and versioned): adoption 30 (active users ÷ entitled seats, modules in use ÷ modules licensed, from `UsageRecorded`), support 20 (open Sev1 and Sev2 tickets, SLA breaches, reopen rate), commercial 15 (days overdue, disputes), relationship 20 (latest NPS, executive sponsor engaged, QBR held in the last 120 days), delivery 15 (implementation status or open change requests). Bands: green ≥ 70, amber 40–69, red < 40 [REC]. Each score shows its component contributions; a manual override needs a reason and expires after 30 days.

### OH2.4 Delivery, alerts and exports

- Embedded Apache Superset with guest-token row-level security (Finbyx Part 10.1) over a read-only reporting schema refreshed hourly (revenue and HR daily, after ledger and payroll close); threshold alerts to owners.
- Leadership packs export as PDF and XLSX with metric definitions appended; AI-drafted commentary is labelled, cites its metrics and is approved by the dashboard owner before circulation.

### OH2.5 Events

Reads Hub module tables through the reporting schema, including the Hub's own outbox records of the events it consumes or emits (`UsageRecorded`, `ReleasePublished`, `ChangeApproved`, `ControlEvidenceCollected`, `BackupCompleted`, `RestoreTested`, `SecurityIncidentNotified`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `PlanChanged`, `SubscriptionCancelled`, `ImplementationMilestoneReached`, `TenantProvisioned`, `SupportTicketOpened`, `SupportTicketResolved`). Emits none.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Metric definitions and versions | Group | Catalogue of OH2.2, maker-checker | Regulated for revenue and HR metrics (finance or HR sign-off); otherwise commercial |
| Individual-metric visibility | Platform | Person and line manager only; no ranked league tables | Floor |
| Cross-entity views | Platform | Aggregates only | Floor |
| Refresh cadence | Group | Hourly; revenue and HR daily after close | Commercial |
| Health-score weights and bands | Group | OH2.3 (green ≥ 70, amber 40–69, red < 40) | Commercial; versioned |
| Manual health override expiry | Platform | 30 days, reason required | Floor (maximum) |
| Threshold alerts | Dashboard owner | Off until set; owner and deputy notified | Commercial |
| AI commentary on packs | Platform | Draft only; owner approval before export | Floor |
| Home layout | User | Workspace default (Part 3.5) | Personal; restricted tiles cannot be added |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Home` | Role home dashboard (Part 3.5), My Queue, recent items, pinned saved views | Every user |
| `Home › Dashboards` | Catalogue of OH2.2 dashboards the user may see; each tile shows definition, version and as-of; drill-down within entity scope; export PDF or XLSX | Per dashboard visibility |
| `Home › Leadership packs` | Generate pack, review and edit AI commentary (labelled), approve, export, distribution log | Dashboard owners, leadership |
| `Home › Notifications` | Notification centre (Part 3.5); preferences; digest settings | Every user |
| `Home › Saved views` | Personal, team and entity views; share, pin, retire | Every user |
| `Admin › Metrics` | Metric definitions (formula, grain, source, owner, version, visibility), version diff, maker-checker approval, impact list of tiles | Metric owners, finance, HR |

### Acceptance tests

- For a synthetic ledger, MRR, ARR, NRR and GRR equal hand-computed golden values, and a one-time implementation invoice does not change MRR.
- Changing a health-score weight creates a new definition version; historical scores keep their original version.
- A support agent sees their own productivity metrics and their manager sees the team's; a peer cannot see either.
- A group dashboard viewed by a Finbyx manager shows Equator figures only as part of group totals, with no Equator drill-down.
- No dashboard query touches a product database (verified by the reporting schema's grants).
- A leadership pack cannot be exported while AI commentary is unapproved.

---

## OH3. CRM (open schema; Brevo adapter)

**Purpose.** A built-in CRM for every group company that the group owns completely: open schema, full import and export, two-way Brevo synchronisation, and a tested migration path to Brevo or another CRM, so there is no lock-in (owner requirement 5).

**Users.** Sales and partnerships, marketing, customer success, onboarding, leadership; each group company within its own entity scope.

### OH3.1 Data model (core objects)

| Object | Key fields |
|---|---|
| `account` | `org_id`, legal name, CIN, GSTIN, institution type (NBFC by layer, HFC, NBFC-MFI, UCB, StCB, DCCB, bank, SFB, credit co-operative society, ARC, CIC, AIF, IFSCA FC or FU, listed entity), public asset band, owning group company, owner, status, parent |
| `contact` | person fields, designation, function (CEO, CFO, CCO, CRO, CTO, GRO, procurement), account, emails and phones with source, preferred language, `dnd_status`, consents (OH3.3), owner entity |
| `lead` | source (web form, event, referral, partner, inbound call, import batch), campaign, product interest, score, status, owner, disqualification reason |
| `opportunity` | account, products and SKUs (from the OH8 catalogue), stage, amount (one-time and recurring shown separately), close date, probability, competitors, decision makers, due-diligence status, owning group company |
| `activity` | type (call, meeting, email, note, task, demo), participants, outcome, next step; email and calendar items logged only by user action or user-enabled sync (OH12), never by mailbox scraping |
| `partner`, `quote` | Partner type, agreement, commission terms; quotes generated by OH8 from the catalogue with approved discounts |
| Custom objects and fields | Defined by administrators as JSON Schema per object; versioned; included in API, export and Brevo mapping automatically |

### OH3.2 Lead and opportunity workflows

- **Lead:** `NEW → CONTACTED → MARKETING_QUALIFIED → SALES_QUALIFIED → {CONVERTED, NURTURE, DISQUALIFIED}`; conversion creates or links an account, contact and opportunity (duplicate check first). `NURTURE` returns to `CONTACTED` on new engagement; `DISQUALIFIED` needs a coded reason and can be reopened once with a reason.
- **Opportunity:** `DISCOVERY → SOLUTION_FIT → DEMO → PROPOSAL → DUE_DILIGENCE → CONTRACTING → {WON, LOST, ON_HOLD}`; `ON_HOLD` needs a review date (default 30 days) and returns to the stage it left.
  - `DUE_DILIGENCE` serves the client's vendor due diligence: the vendor assurance pack of Finbyx Part 10.6 item 14 and the OH14 evidence room; for an RE client, its outsourcing materiality assessment (OUT paras 30, 36) and, for Udofin, the RE's enhanced due diligence on the LSP (CF para 6(2)).
  - `CONTRACTING` requires the MSA, DPA and the OUT clause matrix (Finbyx Part 10.6 item 1) before `WON`.
  - `WON` opens an onboarding case in OH4 and a contract in OH8.
- Lost and disqualified reasons are coded; win and loss analysis feeds OH2.

**Client lifecycle, end to end** (one timeline on the client 360 page; each stage has one accountable owner, a timer and a failure path):

| Stage | Module and owner | Entry | Exit (gate) | Timer [REC] | Failure and rollback |
|---|---|---|---|---|---|
| Lead | OH3; marketing or SDR | Form, event, referral, import with source | Qualified: entity type and size known, need, decision maker, timeline; consent recorded for any marketing | First touch within 1 working day | Disqualify with reason; suppression honoured |
| Qualification | OH3; account executive | `SALES_QUALIFIED` | Discovery notes, products of interest, regulatory profile (RE, society, other) | 10 working days | Nurture; reopen on engagement |
| Demo | OH3 with presales | Discovery done | Demo on a sandbox with synthetic data only (OH4 sandbox order); follow-up logged | Sandbox expires after 30 days unless extended | Re-demo; never a demo with real client data |
| Proposal | OH3 with OH8 quote | Solution fit | Quote from the signed catalogue (`POST /v1/billing/quotes`); discounts within DoA (OH11); explainers passed the claims gate | Quote valid 7 days by default | Requote with a new version; approvals re-run |
| Contract | OH3 and OH4 contract desk | Quote accepted | MSA, DPA, OUT clause matrix, SoW (and the Udofin LSP agreement) signed by authorised signatories via LawDocs eSign | 30 days | Redline loop; a lapsed contract returns to Proposal |
| Provisioning | OH4 | Contract signed | Production gate passed; `TenantProvisioned` acknowledged `READY` (Part 6.5) | Ack ≤ 1 working day; ready ≤ 1 working day after a complete request | `FAILED` reason code → fix and resubmit with a new request id |
| Implementation | OH4; implementation manager | Kick-off held | Milestones accepted by the client; migration signed off | Per SoW baseline | Change request; RAID escalation; rollback plan per cut-over |
| Go-live | OH4 | Go or no-go approved by the client | Cut-over complete; `ImplementationMilestoneReached` (`GO_LIVE`) | Cut-over window | Rollback to the legacy system per the signed plan |
| Hypercare | OH4 and OH6 | Go-live | Exit criteria met: no open Sev 1 or 2, adoption threshold, client sign-off | 30 days (configurable up to 90) | Extended hypercare with a dated plan |
| Success | OH5; CSM | Hypercare closed | Business as usual: health, QBRs, renewals, expansion; exit through OH4 exit case | Renewal playbook (OH5.2) | Churn-save plan; orderly exit |

### OH3.3 Consent and contact-permission model

| Field | Content |
|---|---|
| `consent[]` | channel (EMAIL, SMS, WHATSAPP, VOICE, POST), purpose (PRODUCT_UPDATES, NEWSLETTER, EVENTS, SALES_CONTACT, PARTNER_OFFERS), lawful basis (CONSENT; CONTRACT for service messages to customers), group company that obtained it, source (form id, event id, import batch id), notice and consent-text version, captured_at, evidence (form submission hash, double opt-in token, timestamp), withdrawn_at, withdrawal channel |
| DLT and TRAI fields | principal-entity id of the sending company, header id, template id, content category (promotional, service, transactional, government), last DND or preference scrub date, `optout_until` (90 days after a promotional opt-out) |
| DPDP fields | notice version shown, language, data-principal request history (access, correction, erasure), retention end date |

- Consent is **per group company**: consent given to LawDocsComply does not permit Finbyx marketing (Part 4.1).
- Imported contacts without consent evidence are stored as `NO_MARKETING_CONSENT`; they can be contacted one-to-one on a business matter but never added to a campaign.
- Erasure requests remove marketing data and keep only a suppression record (hashed email or phone) so the person is not re-imported.

### OH3.4 Send gate

Every outbound marketing or bulk message, whether sent by the Hub or by Brevo, passes the gate or is refused with a reason:

1. consent exists for the channel, purpose and sending company, and is not withdrawn;
2. no promotional opt-out in the last 90 days;
3. SMS: valid DLT header and template in the right category; promotional content carries an opt-out;
4. voice: promotional calls only through the 140-series via a registered telemarketer; no automated or bulk service calls from group numbers until the 1600-series position is confirmed (Part 4.6);
5. WhatsApp: the contact's opt-in recorded under the WhatsApp Business policy [VERIFY: current policy];
6. content approved through the OH7 workflow and claims gate;
7. sending window 09:00–19:00 IST for calls and SMS to individuals [REC; mirrors the marketing-contact window of the RBC Second Amendment Chapter IIIA as good practice; VERIFY: paragraph number];
8. no client RE's customers, borrowers or members in the audience, ever.

The gate runs twice: when a segment is frozen for approval (count and refusals shown to the approver) and again per recipient at send time, so a consent withdrawn after approval is honoured. Each evaluation is stored (`send_evaluation`: rule results, consent version, template ids) and refusals are reported per reason.

### OH3.5 Import and export

- **Import:** CSV and XLSX templates, versioned mapping profiles, validation (formats, mandatory fields, duplicates, consent evidence), dry run with reject file, batch id on every record, batch rollback within 7 days.
- **Deduplication:** match rules (email, normalised phone, CIN or GSTIN, fuzzy name plus domain) with a merge queue; merges keep both histories and the most restrictive consent.
- **Export:** any object or the whole CRM in the Integration Specification Part 12.1 archive standard, including activities, consent ledger and custom fields; restricted fields only with `export.restricted`; full exports need a second approver.

### OH3.6 Brevo adapter (two-way)

- **Scope:** Brevo executes email, SMS and WhatsApp campaigns for the group's B2B marketing contacts; the Hub stays the **system of record** for accounts, contacts, consent and opportunities. No client regulated data or RE customer data ever goes to Brevo (CF para 14(4); OUT para 74(vi)); hosting location, DPA and sub-processors are confirmed in an ADR before go-live [VERIFY: Brevo hosting region and DPDP cross-border position].
- **API:** Brevo API v3 with API key or OAuth 2.0 client credentials in the vault; contacts endpoints limited to 10 requests per second, HTTP 429 handled with back-off and jitter [VEND]; Sales CRM objects (companies, deals, tasks, notes) mapped if enabled [VERIFY: endpoint paths].
- **Outbound:** outbox-driven upserts keyed on the Hub id held as a Brevo attribute; per-field direction flags (`HUB_TO_BREVO`, `BREVO_TO_HUB`, `BOTH`); list membership derived from Hub consent and segment rules, never edited in Brevo.
- **Inbound:** Brevo webhooks (unsubscribe, hard bounce, spam complaint, delivery and engagement, CRM changes where enabled), authenticated [VERIFY: Brevo webhook signing options], de-duplicated in an inbox, then applied; engagement kept in aggregate per contact and campaign.
- **Conflict rules:** consent and suppression — the most restrictive value wins wherever it was set; identity fields — the Hub wins; engagement fields — Brevo wins.
- **Reconciliation:** nightly comparison of counts and checksums of synchronised contacts and lists; breaks open a ticket; a weekly full export from Brevo is archived as the exit copy.

### OH3.7 Migration path and no lock-in

- A `crm-export` profile per target (Brevo CRM, HubSpot, Zoho CRM, Salesforce [VERIFY: import formats]) produces the archive plus a target mapping file and field documentation; the suppression list and consent history always travel with it.
- **Round-trip test** in every release: export, re-import into an empty Hub, compare counts, relationships and consent states; any difference fails the build.

### OH3.8 Cross-group rules

- A Finbyx or Udofin account record never shows Equator case information, and Equator users never see lender-side pipeline for case parties (Part 4.4; OH1.6).
- LawDocsComply's knowledge of a client's compliance position never appears in any other company's account view (Part 4.5).
- Cross-sell between group companies uses only commercial metadata (products held, renewal dates, contacts' consents for the target company). An introduction to another group company's sales team needs the client contact's agreement, recorded as an activity [REC].

### OH3.9 Integrations and events

Receives "contact sales" requests from Finbyx and Udofin billing pages (Finbyx CM2.2; Udofin RV2.2) through `POST /v1/crm/requests` (Integration Specification Part 6.29: org_id, tenantid, requester business contact under the product's notice, product, plan or add-on of interest, message; never borrower, member or loan data); each request becomes a lead routed to the account owner within the first-touch SLA. No ecosystem events are produced; internal module events (for example opportunity won) stay in the Hub outbox and are not Integration Specification events.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Consent per group company, channel and purpose | Platform | Required for every marketing send | Floor |
| Promotional opt-out re-consent wait | Platform | 90 days | Floor (TCCCPR) |
| Sending window to individuals | Entity | 09:00–19:00 IST | Floor; may only narrow |
| Consent and notice texts, DLT templates | Entity | None until approved | Regulated (legal sign-off) |
| Pipeline stages and required fields | Entity and product | OH3.2 stages | Commercial; `CONTRACTING` gates are a floor |
| Lead first-touch SLA | Team | 1 working day | Commercial |
| Stale-opportunity alert | Team | 30 days without activity | Commercial |
| Lead scoring model | Entity | Rules-based, versioned | Commercial; AI score is advisory only |
| Duplicate-match thresholds | Entity | Exact email, phone, CIN or GSTIN; fuzzy name plus domain ≥ 0.9 | Commercial |
| Import rollback window | Platform | 7 days | Commercial |
| Full export | Platform | Second approver; restricted fields need `export.restricted` | Floor |
| Brevo field directions | Entity | OH3.6 conflict rules | Commercial; consent fields fixed to "most restrictive wins" |
| Round-trip export test | Platform | Every release | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Clients` | Client list with saved views (type, product, health band, owner); client 360 with tabs Overview, Contacts, Contracts and plans, Onboarding, Success, Support, Invoices, Timeline, Documents (a tab appears only if the viewer holds that module); Equator and LawDocsComply walls applied | Sales, success, onboarding, support, finance, leadership |
| `CRM › Leads` | List and board by status; bulk assign, bulk disqualify with reason, add to nurture; lead detail with consent panel, activity timeline, convert wizard (duplicate check, account, contact, opportunity) | Marketing, sales |
| `CRM › Opportunities` | Pipeline board by stage, forecast view (weighted, commit, best case), stage-gate checklist, quote button (OH8), due-diligence pack request, won or lost wizard with coded reasons | Sales, presales, leadership (read) |
| `CRM › Activities and tasks` | My tasks, team calendar, logged calls and meetings; one-click logging from Outlook or Gmail add-in by user action only | Sales, success |
| `CRM › Partners` | Partner list, agreements, commission terms, referred opportunities | Partner managers |
| `CRM › Segments and consent` | Segment builder with live consented count and send-gate preview; consent ledger; suppression list; data-principal requests | Marketing, DPO |
| `CRM › Imports` | Wizard: upload, map (saved profile), validate, dry run with reject file, commit, rollback within 7 days | Marketing operations |
| `CRM › Exports` | Object or full export, target profile (Brevo, HubSpot, Zoho, Salesforce), approval queue, download log | CRM administrators |
| `CRM › Brevo sync` | Sync status, queue depth, last reconciliation, breaks and conflicts with resolution actions | CRM administrators |
| `CRM › Merge queue` | Suggested duplicates with match reasons; merge preview keeping both histories and the most restrictive consent | CRM administrators |

Empty state on `CRM › Leads`: "No leads yet: connect a web form or import a list with consent evidence". Error state when Brevo is down: sends paused, sync queued, CRM fully usable.

### Acceptance tests

- An administrator adds a custom field to `account`; it appears in the API, the export `schema.json` and the Brevo mapping screen without a deploy.
- A contact imported without a consent-evidence column cannot be added to any campaign list; a one-to-one email logged by the owner is allowed.
- An unsubscribe webhook from Brevo sets the contact's email consent to withdrawn in the Hub within 5 minutes; a later Hub edit cannot re-subscribe them.
- A promotional SMS to a contact who opted out 60 days earlier is refused with `optout_window`.
- An attempt to sync a contact tagged as an RE's borrower or member is refused by a schema rule, and the attempt is logged.
- The round-trip export and re-import of a synthetic CRM of 50,000 records reproduces counts, relationships and consent states exactly.
- A burst of 5,000 contact updates to Brevo completes without a dropped record when the API returns HTTP 429.

---

## OH4. Client onboarding, implementation and data-migration factory

**Purpose.** Turn a signed client into a live, reconciled tenant through a repeatable, evidenced process: onboarding, implementation projects with billable milestones, a data-migration factory with reconciliation sign-off, and, where engaged, migration of the client's staff to Microsoft 365 or Google Workspace.

**Users.** Onboarding coordinators, implementation managers, solution consultants, migration engineers; client project leads and approvers through the implementation portal; finance (milestone billing).

### OH4.1 Data model

| Entity | Key fields |
|---|---|
| `onboarding_case` | client `org_id`, products, selling company, due-diligence items, contracts (MSA, DPA, OUT clause matrix, SoW, Udofin LSP agreement), client registration details |
| `provisioning_order` | case, product, environment (SANDBOX, UAT, PRODUCTION), deployment model, plan and entitlement ref, residency, gate evidence refs, first-admin work email, `provisioning_request_id`, state, product acknowledgements (status, reason code, `tenantid`) |
| `implementation_project` | methodology template, phases, milestones, baseline, budget, team, client approvers, RAID log |
| `milestone` | name, deliverables, acceptance criteria, due date, billing flag and amount (from the OH8 contract), acceptance certificate (signed document hash), accepted_by, accepted_at |
| `change_request`, `timesheet_entry` | scope delta, effort, commercial impact, approvals on both sides; hours by task with billable flag (feeds OH11 utilisation) |
| `migration_programme` | source systems, datasets, template and mapping versions, validation rule set, runs, sign-offs |
| `migration_run` | type (MOCK_1..n, DRESS_REHEARSAL, PRODUCTION), environment (Finbyx `uat-[tenant]` or `prod-in`), started, ended, record counts, control totals, exceptions summary, evidence hashes; never record-level data |
| `workplace_migration` | client, source and target suite, scope (users, mailboxes, drives, sites), tool, batches, delegated access grant, validation report |
| `exit_case` | account, products, notice date, trigger (non-renewal, cancellation, termination notice), exit plan (Finbyx Part 7J DP5; Udofin Part 7B UP5), export jobs (`ExportRequested`, `ExportCompleted` status), no-erasure-during-transition flag, successor cooperation log, client purge sign-off, purge certificate reference |

### OH4.2 Onboarding workflow

`INITIATED → DUE_DILIGENCE (client verification; client's vendor assessment of the group company) → CONTRACTED (MSA, DPA, OUT clause matrix signed) → PROVISIONING (one provisioning order per product and environment) → KICKED_OFF → HANDED_TO_PROJECT`; `ON_HOLD` (review date required) and `CANCELLED` (reason) from any state before `KICKED_OFF`.

**Provisioning order:** `DRAFT → GATES_PENDING → APPROVED (maker-checker; emits signed TenantProvisioned) → ACCEPTED → READY → LIVE`, with `REJECTED` (gate failure, reason shown) and `FAILED` (product reason code). The product reports `ACCEPTED`, `READY` or `FAILED` through `PUT /v1/provisioning-requests/{id}`; with no acknowledgement in 1 working day the Hub polls `GET /v1/tenants/{tenantid}/provisioning-status` and opens a Sev 3 ticket. `LIVE` is set when the first admin has signed in. A `FAILED` order is corrected and resubmitted as a new request; `TenantProvisioned` is idempotent on `provisioning_request_id`, and a product holds at most one live tenant per (org_id, product, environment) (Integration Specification Part 6.29).

- **Production gate:** a production tenant is requested only after a signed MSA and DPA, verified client registration (for example RBI certificate of registration, co-operative registration or SEBI registration) and, for RE clients, the client's own outsourcing assessment where it applies (Finbyx CM5.4; OUT paras 30, 34). A PRODUCTION request without the MSA, DPA and OUT clause-matrix references is also rejected by the product with `regulatory-guard`. Sandbox tenants with synthetic data may be provisioned earlier.
- **First admin:** the request carries only the client's work email with `legalbasis = CONTRACT_PERFORMANCE_VENDOR`; the product sends the invitation and the Hub never holds a password or invitation link.
- **Udofin partner onboarding** uses the same case type, with deal configuration and the LSP agreement held in Udofin (Udofin Part 7B UP1–UP2); Equator and LawDocsComply clients follow it within their own entity scope.

### OH4.3 Implementation projects

- **Methodology template** per product: `DISCOVERY → DESIGN (configuration workbook, product and rule decisions signed by the client) → BUILD_AND_CONFIGURE → MIGRATION (mock runs) → UAT → TRAINING → CUTOVER (go or no-go) → HYPERCARE (30 days) → CLOSED`.
- **Milestones** with acceptance criteria agreed in the statement of work. Client acceptance (approver in the implementation portal with MFA, or a signed certificate uploaded) emits `ImplementationMilestoneReached` with the Specification milestone code (`DISCOVERY` after Discovery, `CONFIGURATION` after Design and Build, `MIGRATION` after the production migration sign-off, `INTEGRATIONS`, `TRAINING`, `GO_LIVE` after cut-over); OH8 invoices only accepted billable milestones. A rejected milestone returns to the delivery team with the client's reasons and a new due date; deemed acceptance after a contractual period is allowed only if the contract says so and is shown as such.
- **RAID log** with owners and due dates; weekly status reports generated from project data.
- **Regulatory decisions stay with the client:** configuration of products, rule packs, provisioning rates above floors, KFS wording and approval matrices is decided and signed by the client's authorised officers in the product; Infrabyx consultants advise and configure in sandbox or UAT, and never approve in production (OUT para 15; Finbyx Part 10.6 item 27).

### OH4.4 Data-migration factory

- **Templates** per dataset and institution profile (customers, loans, schedules, collateral, DPD history, classification and provisions, GL opening balances, members and share capital, JLG and SHG groups, investments), versioned with a data dictionary; **mapping specifications** (source field, target field, transformation, code mapping, version) approved by the client's data owner before the first mock run.
- **Execution in the product, not the Hub:** loads run with the Finbyx Phase 19 migration toolkit (loan boarding with history, opening balances, DPD reconstruction, reconciliation sign-off reports) inside the client's Finbyx tenant in India; other products use their own import tools. The Hub stores run metadata, control totals and signed reports, never extracted data.
- **Validation:** formats; referential integrity; business rules (principal outstanding equals unpaid principal instalments; DPD consistent with due history; classification consistent with IRACP or a client-confirmed exception); sub-ledger to GL control-account balance.
- **Reconciliation pack per run:** counts, principal, accrued interest, arrears, charges, DPD buckets, SMA and NPA, provisions, collateral, trial balance, each with source, target, variance and tolerance [REC: zero variance on counts and principal; accrued interest within ₹1 per loan, exceptions listed].
- **Sign-off:** business owner and application owner at each stage, then the client's CFO (and CRO for portfolio data) at dress rehearsal and production; the go or no-go record lists sign-offs, accepted exceptions and the rollback plan (CYB para 99: migration policy with audit trails and stage sign-offs by business users and application owners).
- **Data handling:** extracts travel only from the client's systems to the client's tenant (product import or SFTP from allow-listed Indian addresses; Integration Specification Part 3.11); staff work through scoped support sessions; no extract on laptops, in group Google Workspace or in the Hub (Part 4.8).

### OH4.5 Workplace migration for client staff (where engaged)

- A professional service under its own statement of work (for example alongside Finbyx GV7).
- **Runbook:** assessment (users, mailboxes, drives, sites, licences, retention and holds); identity mapping; DNS and mail-flow plan; pilot; batches with delta passes; cutover; validation of item counts, sizes and permissions; client-owned decommissioning.
- **Tools:** the vendors' own tools (Microsoft Migration Manager; Exchange migration batches from Google Workspace; Google Workspace Migrate or Data Migration Service for the reverse direction) [VERIFY: edition limits and current tool names].
- **Access:** the client grants delegated administrative consent scoped to the migration and time-bound to the statement of work; credentials sit in the Hub vault; access is revoked at closure and the revocation is evidenced.
- **Residency warning:** before migrating an RE client to Google Workspace, the Hub records that Workspace offers no India data region and that borrower or member data must not be placed there; the client's authorised officer acknowledges this (Part 4.8).
- Infrabyx never stages mailbox or drive content on its own storage.

### OH4.6 Exit cases

`NOTICE_RECEIVED → PLAN_AGREED (exit plan, turnaround, successor named) → EXPORTING (EXIT-scope exports tracked by status) → TRANSITION (no erasure or alteration of data; successor cooperation) → PURGE_APPROVED (client sign-off) → CLOSED (purge certificate reference)`. Opened by OH5 on non-renewal or cancellation, or by OH8 when a termination notice issues. Regulated functions, read access and export stay available throughout (Finbyx CM1.4; Udofin RV2); the case cannot close without an export-completion record, the client's purge sign-off and the purge certificate (OUT paras 87, 88, 97(xvi)). A client who withdraws notice returns the case to `CLOSED` with reason `RETAINED`.

### OH4.7 Integrations and events

Emits `TenantProvisioned` (signed provisioning request to the product) and receives the product's acknowledgement through `PUT /v1/provisioning-requests/{id}`; emits `ImplementationMilestoneReached` (to the product for the tenant's project view; OH8 reads the milestone internally); consumes `ExportRequested` and `ExportCompleted` for exit cases, and `StorageTargetConnected` and `BackupCompleted` for projects that include customer-controlled storage (Finbyx Part 7J DP3–DP4), as status only.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Production gate (MSA, DPA, OUT clause matrix, registration, outsourcing assessment) | Platform | Required for UAT and PRODUCTION | Floor |
| Sandbox self-service | Entity | On; synthetic data only; 30-day expiry | Commercial; synthetic-only is a floor |
| Provisioning acknowledgement timeout | Platform | 1 working day, then status poll and ticket | Commercial |
| Methodology and milestone templates | Product | OH4.3 template per product and institution profile | Commercial |
| Deemed acceptance | Contract | Off | Contractual |
| Hypercare length | Contract | 30 days | Commercial (up to 90) |
| Reconciliation tolerances | Programme | Zero on counts and principal; accrued interest ₹1 per loan | Floor; the client may tighten |
| Migration sign-off matrix | Product | Business owner and application owner each stage; CFO (and CRO) at dress rehearsal and production | Floor (CYB para 99) |
| Workplace-migration delegated access | Engagement | SoW end date, at most 90 days per grant | Floor (maximum) |
| Weekly status report | Project | Friday 17:00 IST, auto-drafted | Commercial |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Onboarding › Cases` | List by state and age; case wizard (client, products, selling company, contract checklist, due-diligence items); detail with gate checklist and timeline | Onboarding coordinators, contract desk |
| `Onboarding › Provisioning` | Orders by state; gate evidence panel; approval queue (maker-checker, fresh MFA); acknowledgement timeline (ACCEPTED, READY, FAILED with reason); resubmit | Onboarding coordinators (maker), head of onboarding (checker) |
| `Onboarding › Projects` | Portfolio by RAG; project plan with milestones and baseline; RAID log; change requests; timesheets; status-report generator; milestone acceptance tracker | Implementation managers, consultants |
| `Onboarding › Migration` | Programmes, templates and mapping versions; runs with control totals; reconciliation pack viewer with variances and tolerances; sign-off queue; go or no-go record | Migration engineers, implementation managers |
| `Onboarding › Workplace migrations` | Engagements, batches, delegated-grant expiry, validation reports, revocation evidence | Workplace consultants |
| `Onboarding › Exits` | Exit cases by state; plan, export status, successor log, purge sign-off and certificate | Onboarding, customer success, legal |
| `Onboarding › Templates` | Methodology, milestone, migration and sign-off templates with versions | Head of delivery |
| Client implementation portal | Projects, milestones to accept (MFA), documents, RAID items assigned to the client, status reports | Client project leads and approvers |

Empty state on `Onboarding › Provisioning`: "No orders: a won opportunity or a sandbox request creates one". Error state when a product is unreachable: the order stays `APPROVED` with retry and the fallback poll shown.

### Acceptance tests

- A production provisioning request without signed MSA and DPA references is refused, while a sandbox request succeeds.
- A milestone accepted by a client approver emits exactly one `ImplementationMilestoneReached`; OH8 cannot invoice an unaccepted billable milestone.
- A migration run's record in the Hub contains control totals and hashes only; a schema test fails if any loan, customer or member identifier field is added.
- A production run cannot be marked complete without the business-owner, application-owner and CFO sign-offs; the go or no-go record lists every accepted exception.
- A principal variance of ₹1 on any loan in a mock run fails reconciliation and opens an exception with an owner.
- A workplace-migration delegated grant expires at the end date and the revocation evidence is attached to the project.
- An approved provisioning order emits one signed `TenantProvisioned`; a retried approval emits nothing new; a `FAILED` acknowledgement shows the reason code and the order can be resubmitted only as a new request id.
- An exit case cannot reach `CLOSED` without the export-completion record, the client's purge sign-off and a purge certificate reference.

---

## OH5. Customer success, renewals and after-sales

**Purpose.** Keep clients successful and renewing on fair terms: health monitoring, success plans, business reviews, renewals, expansion, feedback and orderly exits, using only commercial and support metadata.

**Users.** Customer success managers, account executives, finance (renewal invoicing), support leads, leadership.

### OH5.1 Data model

| Entity | Key fields |
|---|---|
| `success_plan`, `qbr` | objectives in the client's words, measures, owners, review dates; QBR attendees, data-pack hash, actions |
| `health_snapshot` | account, product, date, score, components, definition version (OH2.3), override and reason |
| `renewal` | contract (OH8), term end, notice period, renewal type (AUTO, MANUAL), proposed changes, price-change notice date, status, outcome |
| `expansion_opportunity`, `churn_risk` | product or SKU, source, linked CRM opportunity; churn drivers, save plan, owner |
| `survey`, `survey_response` | relationship NPS, transactional CSAT or onboarding survey; score, verbatim, follow-up owner |

Exits are tracked in the OH4 `exit_case` (OH4.6), shown on the account's Success tab.

### OH5.2 Workflows

- **Renewal playbook:** T−120 days review of health and usage; T−90 renewal proposal and any price change (written notice of at least 30 days before it takes effect, Finbyx CM2.3) and the product's 90-day renewal reminder; T−60 negotiation; T−30 confirmation and reminder to billing contacts; T−7 final reminder; on renewal OH8 issues the contract version and `PlanChanged` where the plan changes. A renewal still unconfirmed at T−30 alerts the account owner and head of customer success; a missed notice date blocks the price increase for that term (it never blocks the renewal itself).
- **QBR** quarterly for accounts above a configurable revenue band, with a data pack generated from Hub aggregates and reviewed by the CSM before sharing.
- **Churn save:** a health score in the red band or a cancellation request opens `churn_risk` with drivers and a save plan; leadership is alerted for top-tier accounts.
- **Surveys:** relationship NPS twice a year to named client contacts; CSAT after ticket closure (OH6) and after go-live (OH4); detractor responses open a follow-up within 2 working days [REC].
- **Exit:** a cancellation or non-renewal opens an OH4 `exit_case` (OH4.6), linked to the product's exit process: for RE clients, no erasure or alteration of data during transition (OUT para 87), cooperation with the incoming provider (para 88), complete export with configuration (para 97(xvi)), purge only after the client's sign-off with a purge certificate. The CSM stays the client's contact and records an exit interview.

### OH5.3 Rules and guard-rails

- **Inputs only from metadata:** `UsageRecorded` aggregates, ticket metadata, billing status, survey responses and CSM notes; never loan, borrower, member, case or compliance content (Part 2.3).
- **Commercial pressure never touches regulated functions:** a renewal dispute or late payment never degrades regulated functions, read access or export (Finbyx CM1.4, CM4.5; Udofin RV2.2); dunning ends in a termination notice leading into exit, never a hard cancel.
- **No dark patterns in renewals:** auto-renewal clearly stated in the contract and in each reminder; cancellation as easy as purchase; no countdown pressure (Finbyx CM2.3).
- **Cross-group expansion** follows OH3.8; Equator is never offered as part of a lender-side expansion bundle (Part 4.4).
- **Feedback use:** testimonials and case studies need the client's written consent and, for an RE, its compliance approval; they then pass the OH7 claims gate.
- **Survey communications** are service messages to client staff under the contract; they carry no promotional content.

### OH5.4 Integrations and events

Reads `UsageRecorded` aggregates (OH8), ticket metadata (OH6), invoice, payment, plan and cancellation status (OH8), milestones and exit cases (OH4) inside the Hub. Plan changes are executed by OH8, which emits `PlanChanged` and `EntitlementChanged`.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Health-score weights and bands | Group | OH2.3 | Commercial; versioned |
| Renewal playbook timings | Entity | T−120, T−90, T−60, T−30, T−7 | Commercial; may start earlier |
| Price-change notice | Platform | ≥ 30 days before effect | Floor |
| Auto-renewal disclosure and easy cancellation | Platform | Stated in contract and every reminder; cancellation no harder than purchase | Floor |
| QBR eligibility | Entity | Accounts above the configured ARR band, quarterly | Commercial |
| Relationship NPS | Entity | Twice a year to named client contacts | Commercial |
| Detractor follow-up | Team | 2 working days | Commercial |
| Churn-risk triggers | Entity | Red band, cancellation request, two failed payments, executive sponsor lost | Commercial |
| Survey content | Platform | Service messages only; no promotional content | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Success › Portfolio` | Health heatmap by product and band; filters (CSM, tier, renewal window); saved views; bulk assign CSM | CSMs, head of customer success |
| `Success › Accounts` | Account success page: health components and history, success plan, QBR schedule and data pack (preview, CSM review, share), surveys, notes | CSMs, account executives |
| `Success › Renewals` | 120-day renewal calendar and pipeline; notice tracker (price-change and auto-renewal reminders sent); confirm or hand to OH8 | CSMs, finance |
| `Success › Churn risk` | Open risks with drivers and save plans; leadership alerts for top-tier accounts | CSMs, leadership |
| `Success › Surveys` | Templates, schedules, response inbox, follow-up queue for detractors | CSMs, support leads |
| `Success › Expansion` | Expansion opportunities linked to CRM; whitespace by product (commercial metadata only; OH3.8 rules) | CSMs, account executives |

Empty state on `Success › Portfolio`: "No live clients yet: accounts appear after hypercare closes in Onboarding".

### Acceptance tests

- A renewal with a price increase cannot be confirmed unless the price-change notice was sent at least 30 days before the increase takes effect.
- An account moving from amber to red opens a churn-risk record and alerts the CSM within 1 hour.
- A QBR data pack contains no field from any product other than aggregates and ticket metadata (schema check on the pack generator).
- Recording a non-renewal opens exactly one OH4 exit case linked to the account, and the account's regulated product functions, read access and export remain enabled.
- A testimonial without a consent record cannot be attached to any OH7 content item.

---

## OH6. Support desk, vendor-side tickets and client grievance handling

**Purpose.** One support desk for every product and group company, scoped by client and tenant, with SLAs, escalation, problem management and incident linkage; and a clear, lawful split between the vendor-side complaints that group companies handle and the borrower grievances that only the RE owns.

**Users.** Support agents (L1, L2, L3), problem managers, engineering on-call, account owners, the grievance officer for business customers, client contacts through the support portal and in-product support pages.

### OH6.1 Data model

| Entity | Key fields |
|---|---|
| `ticket` | id, group company providing the service, product, client `org_id`, tenant id, environment, requester (client staff contact), channel (in-product, portal, email, phone, social referral), category, severity, priority, `regulatory_impact` (none, or the regulated activity and its deadline), SLA policy, status, assignee, linked problem, incident, change and release ids, scoped-session ids, attachments with scan result |
| `sla_policy`, `scoped_session` | tier × severity targets (OH6.3); session product, tenant, scope, purpose, client approver, expiry, product reference |
| `problem`, `kb_article` | linked tickets, RCA, known-error flag, workaround, fix change; articles by audience, version, approver, review date |
| `client_complaint` | complainant organisation and contact, group company complained about, category, description, acknowledgement, response, escalation level, status, root cause |
| `re_escalation` | RE `org_id`, RE grievance reference (opaque), question for the vendor, RE deadline, vendor response, status; no borrower or member personal data |
| `misrouted_complaint` | RE `org_id`, channel, received_at, forwarded_at, RE officer, RE acknowledgement ref, purge status; message body held only until the RE acknowledges (7 days at most) |

### OH6.2 Intake and tenant scoping

- **Channels:** in-product "Contact support" in each product (`POST /v1/support/tickets` with a product-signed token carrying `org_id`, tenant and user reference), support portal, monitored email, phone.
- **Scoping:** client contacts see only their organisation's tickets; agents see only the group companies and products in their grant; Equator tickets stay in Equator's scope (Part 4.4).
- **Triage queue** (`Support › Triage`): every new ticket shows the AI-suggested category, severity, product and duplicate candidates with reasons; the agent accepts or overrides (override reason coded) within the first-response target; possible duplicates are linked or merged (the merged ticket keeps its own SLA history); a ticket naming a regulated deadline gets `regulatory_impact` set and the uplift rule below applies. AI never closes, rejects or downgrades a ticket, and a client's severity can be lowered only with a recorded reason shown to the client.

### OH6.3 Severity and SLAs [REC; contract values prevail]

| Severity | Definition | First response | Updates | Workaround target | Hours |
|---|---|---|---|---|---|
| Sev 1 | Production down, data integrity at risk, security incident, or a regulated function blocked near its deadline (for example a CIC submission, return, disbursement batch or grievance clock) | 15 minutes | Every hour | 4 hours | 24×7 |
| Sev 2 | Major function impaired without workaround; regulated function at risk within 3 working days | 1 hour | Every 4 hours | 1 working day | 24×7 for the regulated-function case; business hours otherwise |
| Sev 3 | Function impaired with workaround | 4 business hours | Daily | 5 working days | Business hours |
| Sev 4 | Question, request or cosmetic issue | 1 working day | On change | Planned release | Business hours |

- A ticket with `regulatory_impact` gets a deadline clock and is auto-raised to at least Sev 2 when the deadline is within 3 working days, and to Sev 1 when it is within 1 working day.
- **Four clocks per ticket:** first response, next update, workaround and resolution, each computed on the policy's calendar (24×7 or the entity's business calendar); the clock bar on the ticket shows elapsed percentage, with warnings at 50% and 75% and a breach at 100% (`sla_breach` recorded, client page updated, escalation fired).
- SLA clocks pause only in `WAITING_ON_CLIENT`, with a reason and an automatic reminder after 2 working days; `WAITING_ON_THIRD_PARTY` never pauses the clock. A client reply resumes the clock automatically.

### OH6.4 Ticket lifecycle and escalation

`NEW → TRIAGED → IN_PROGRESS → {WAITING_ON_CLIENT, WAITING_ON_THIRD_PARTY} → RESOLVED → CLOSED` (closed automatically 5 working days after resolution unless reopened) `| REOPENED`

- **Reopen:** a client may reopen within 10 working days of resolution; the ticket keeps its severity and the resolution clock restarts; after 10 working days a new linked ticket is opened.
- **Functional escalation:** L1 to L2 when the workaround target is at 50% elapsed; L2 to L3 engineering at 75%; Sev 1 pages on-call engineering immediately and opens a major-incident bridge if two or more clients are affected.
- **Hierarchical escalation** to account owner, head of support, CTO and group CEO at configurable thresholds; clients may escalate once per ticket with a reason.
- **Problem and known-error management:** repeated or Sev 1 tickets open a `problem`; root-cause analysis within 10 working days for Sev 1 [REC]; known errors with workarounds published to the knowledge base; the fixing change and release are linked (OH13), and `ReleasePublished` closes linked known errors after verification.
- **Scoped support sessions:** the client approves in the product (Finbyx M19 break-glass pattern); the Hub stores only the session reference, scope, approver and expiry; the product logs what was accessed and shows it to the client.

### OH6.5 Client complaints and grievances: who owns what

| Complaint | Owner and system | Hub role | Clock and basis |
|---|---|---|---|
| A client (RE, society, AIF, LawDocsComply or Equator institutional client) complains about a group company's service | The group company, in the Hub `client_complaint` | Full handling: acknowledge, investigate, respond, escalate to the grievance officer for business customers, then a director | Acknowledge within 1 working day; respond within 15 working days [REC; contract prevails] |
| A borrower complains to an RE, and the RE needs input from Finbyx or Udofin as its service provider | **The RE** owns the grievance and the response; Finbyx or Udofin support it | Track the RE's escalation (`re_escalation`) with the RE's reference and deadline; no borrower personal data in the Hub | RE's clocks: 30 days before the borrower may approach RBI (CF para 12(4)); Internal Ombudsman escalation within 20 days where applicable (NBFC Internal Ombudsman Directions 2026); RB-IOS 2026 timelines; responsibility stays with the RE (CF para 12(3); OUT paras 54–57) |
| A borrower or member writes or calls a group company directly about an RE's loan (misrouted complaint) | **The RE** | Forward to the RE's configured grievance redressal officer within 1 working day and tell the complainant which RE handles it and how to reach it; keep only `misrouted_complaint` metadata (RE `org_id`, channel, received_at, forwarded_at, RE acknowledgement ref); the original message is purged from the Hub once the RE acknowledges, and within 7 days at the latest | RE's clocks from the RE's receipt; Infrabyx can never mark it resolved |
| A borrower complains about Udofin's conduct or app | Udofin's grievance system (Udofin Part 7C UB3), forwarding RE matters to the RE | None (Udofin may raise a vendor ticket if engineering help is needed) | Udofin nodal officer (CF para 12(1)) |
| A party complains about an Equator process or a neutral | Equator's own procedure and independent oversight | None; Hub agents never handle these | Equator rules |
| A data principal sends a DPDP request about data a group company holds as processor | The fiduciary (client or RE) | Forward within 1 working day through `DataPrincipalRequest` (Integration Specification Part 6.14) and track | DPDP Rules timelines [VERIFY] |
| A member of the public complains on social media about a lender | The lender | OH7 social inbox replies with the lender's published grievance channel; no account details discussed in public | — |

- **RE escalation payload:** RE `org_id`, opaque grievance reference, product, question category, RE deadline, requested evidence type (for example API logs or a document status), response, responder. Any evidence containing personal data is delivered to the RE inside the product, not through the Hub.
- **No closure by the vendor:** group companies never close, reject or settle a borrower grievance; they answer the RE (Finbyx Part 10.6 item 28).

### OH6.6 Attachments and personal data

Every attachment is malware-scanned and checked by a personal-data detector (PAN, Aadhaar, account-number, mobile and date-of-birth patterns, images of identity documents). A hit quarantines the file, tells the uploader to share through the product instead, and auto-purges the quarantined file after 7 days unless the client confirms it holds no borrower or member data [REC]. Agents cannot download quarantined files.

### OH6.7 Incident linkage

- A Sev 1 ticket with a security, data or availability cause opens or links an OH13 incident with `t0` = detection time; linked tickets update from the incident.
- For RE clients the product company emits `SecurityIncidentNotified` within the **≤ 2-hour target** so the RE can report to RBI within 6 hours of provider detection (OUT para 61; Integration Specification Parts 3.8, 6.15), with updates by `update_seq`; CERT-In within 6 hours where reportable (Part 4.10).
- Client updates use approved templates; a public status page shows service status without client names; the post-incident review is attached to the problem.

### OH6.8 Knowledge base and self-service

Versioned, approved articles by product and audience, reviewed yearly; the client-facing AI assistant answers only from approved articles and the client's own tickets, discloses that it is AI, always offers a human and never gives legal or regulatory determinations.

### OH6.9 Integrations and events

Emits `SupportTicketOpened` and `SupportTicketResolved` (OH6 → the originating product, Finbyx or Udofin) so the client's in-product support page shows status (Integration Specification Part 6.29: ticket_id, tenantid, product, category, severity and SLA clock; resolution code, resolved_at and satisfaction request; `dataclass` `INTERNAL`; no attachment content); receives in-product tickets through `POST /v1/support/tickets`; reads `ReleasePublished` and `ChangeApproved` records (OH13) to link known errors and fixes, and the `SecurityIncidentNotified` copy for the register; forwards `DataPrincipalRequest`.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Severity and SLA matrix | Contract, then entity | OH6.3 | Contract prevails; the default is the minimum offered |
| Regulatory-impact uplift | Platform | Sev 2 within 3 working days of the deadline, Sev 1 within 1 | Floor |
| Clock pause | Platform | Only `WAITING_ON_CLIENT`, with reason; reminder after 2 working days | Floor |
| Escalation thresholds | Entity | L2 at 50%, L3 at 75%; hierarchical per OH6.4 | Commercial; may be earlier |
| Auto-close after resolution | Entity | 5 working days | Commercial |
| Reopen window | Entity | 10 working days | Commercial |
| Business calendar | Entity and office | Entity working days, 09:30–18:30 IST | Commercial |
| Client complaint targets | Contract, then entity | Acknowledge 1 working day; respond 15 working days | Contract prevails |
| Misrouted borrower-complaint forwarding | Platform | 1 working day; purge within 7 days | Floor |
| Attachment DLP patterns and quarantine | Platform | OH6.6; auto-purge after 7 days | Floor |
| AI triage suggestions | Entity | On; suggestions only | Commercial; no AI closure is a floor |
| CSAT after closure | Entity | On | Commercial |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Support › My queue` | Tickets sorted by time to breach; clock bars; keyboard navigation; quick reply with approved templates | Agents L1–L3 |
| `Support › Triage` | Unassigned tickets with AI suggestions and duplicate candidates; accept or override, assign, merge, link to problem | L1 leads |
| `Support › Tickets` | List with saved views (product, client, severity, breach risk, regulatory impact); bulk assign, link, merge; detail with clocks, timeline, scoped-session request, linked problem, incident, change and release; client-visible and internal notes kept separate | Agents, account owners (read) |
| `Support › Problems` | Problems and known errors, RCA due dates, workaround publishing, linked change and release | Problem managers, engineering |
| `Support › Knowledge base` | Article editor, approval workflow with claims gate, review-due list, audience and version | Support leads, product experts |
| `Support › Client complaints` | Complaint register with acknowledgement and response clocks, escalation ladder, root cause, credit-note request to OH8 | Grievance officer for business customers |
| `Support › RE escalations` | RE requests with RE deadline, evidence type requested, response, delivery confirmation inside the product | Agents, product specialists |
| `Support › Misrouted complaints` | Intake, RE officer lookup, forward action, acknowledgement tracking, purge status | Agents |
| `Support › Policies` | SLA policies, business calendars, categories, templates | Head of support |
| Client support portal | Raise ticket (DLP at upload), track with clock status, escalate once with reason, reopen, CSAT | Client contacts |

Empty state on `Support › My queue`: "Nothing assigned: pick up from Triage". Error state when a product's deep link is unavailable: the ticket stays workable and shows the product status page link.

### Acceptance tests

- A Finbyx client contact can open and view only their organisation's tickets; a LawDocsComply agent without a Finbyx grant cannot see a Finbyx ticket.
- A ticket tagged "CIC submission due tomorrow" is raised to Sev 1 or Sev 2 automatically and pages on-call.
- An RE escalation record rejects a free-text field containing a PAN-format or Aadhaar-format string.
- An attachment containing an Aadhaar card image is quarantined and cannot be downloaded by an agent.
- A security incident linked to a Sev 1 ticket shows the 2-hour RE notice clock and the 6-hour CERT-In clock, and flags any missed clock.
- A client complaint not acknowledged within 1 working day escalates to the grievance officer for business customers.
- No workflow allows a Hub user to set a borrower grievance to closed or rejected.
- A Sev 2 ticket left in `WAITING_ON_THIRD_PARTY` keeps its clock running and breaches on time; a ticket reopened on day 9 after resolution keeps its severity and restarts the resolution clock.
- A misrouted borrower complaint is forwarded to the configured RE officer within 1 working day and its message body is purged after the RE's acknowledgement.

---

## OH7. Marketing, brand, social media, PR and collaborations

**Purpose.** Run the group's brands, content, social channels, PR, collaborations, events and advertising through one approval workflow and one claims gate, so that what the group publishes is accurate, lawful and consistent (owner requirement 5).

**Users.** Marketing, brand, social media, PR and partnerships staff; legal and compliance reviewers; leadership approvers; external agencies with restricted accounts.

### OH7.1 Data model

| Entity | Key fields |
|---|---|
| `brand`, `brand_asset` | group company, logos, colours, typography, tone, endorsement line ("an Infrabyx company"); assets with type, version, licence and rights (owner, expiry, channels), approval, hash |
| `content_item` | type (post, article, newsletter, case study, press release, ad, video, webinar, landing page), brand, channels, owner, claims list, evidence links, status, approvals, publish schedule, takedown date |
| `claim` | text, type (performance figure, certification, regulatory statement, client name or logo, comparison, award), evidence reference, expiry, approver |
| `campaign`, `publish_job` | Objective, OH3 audience segment, channels, budget, content items, results; scheduled jobs with platform post id and errors |
| `channel_account` | platform (LinkedIn, X, Facebook, Instagram, YouTube), brand, handle, vault token reference, admins |
| `social_inbox_item` | platform, type (comment, mention, direct message), text, classification, routing, response |
| `influencer_engagement` | influencer, contract, fee, material connection, disclosure label, qualification checks, approvals, takedown rights |
| `media_contact`, `coverage` | Journalist business contacts with source; coverage by outlet, date, tone and release |
| `collaboration`, `event` | Partner, type, agreement, logo rights, data-sharing terms; events with co-hosts, registrations, consents, costs, leads |
| `gift_hospitality` | counterparty, organisation, public-sector flag, value, purpose, approval |
| `ad_campaign` | platform, targeting summary, creatives, disclosures, financial-services verification, spend |

### OH7.2 Content approval workflow

`IDEA → DRAFT → BRAND_REVIEW → CLAIMS_AND_LEGAL_REVIEW → APPROVED → SCHEDULED → PUBLISHED → {UPDATED, TAKEN_DOWN, ARCHIVED}`

- `CLAIMS_AND_LEGAL_REVIEW` is mandatory for any item containing a claim (OH7.5), naming a client or regulator, promoting a financial product or feature with regulatory effect, or published by an influencer.
- Approvals are role-based per brand (for example Equator content is approved only by Equator approvers). The approved version is hashed; any edit after approval sends the item back to review.
- Published items carry a review date (default 12 months); expired claims trigger review or takedown.

**Campaign approval with consent checks:**

| State | Entry and checks | Exit | Owner |
|---|---|---|---|
| `DRAFT` | Objective, brand, channels, budget, content items | Submitted | Campaign owner |
| `AUDIENCE_FROZEN` | Segment snapshot from OH3; send gate run per contact (OH3.4): consented count, refusals by reason, RE-customer exclusion, DLT template and header validity, sending window | Approver sees counts and refusals; a zero-consent segment cannot proceed | Marketing operations |
| `CONTENT_APPROVED` | Every content item `APPROVED` (OH7.2) with the claims gate passed | All items approved | Brand reviewer |
| `COMPLIANCE_APPROVED` | Required when the campaign names a client or RE (written RE approval attached), touches lending or investment content, uses influencers or SMS or voice | Legal or compliance approval with fresh MFA | Legal and compliance |
| `SCHEDULED` | Send times inside the window; budget within DoA | Start time | Campaign owner |
| `SENDING` | Send gate re-run per recipient at send time; withdrawals since freeze honoured | All batches sent | System |
| `COMPLETED`, `PAUSED`, `CANCELLED` | Results aggregated; pause on complaint spike (opt-out or spam rate above threshold) or claims takedown | Terminal or resume after re-approval | Campaign owner |

Any edit to audience or content after approval returns the campaign to the earliest affected state.

### OH7.3 Brand architecture and group separation

- Each group company keeps its own brand. Group endorsement lines are used consistently, and the company that actually provides each product is named (OUT paras 46 and 49 for RE contexts, applied across the group as good practice).
- **Equator's brand stands apart:** no joint campaign presents Equator together with lender-side products, no "one-stop" message bundling ODR with lending software, and no Equator content approved by lender-side staff (Part 4.4).
- Nothing suggests that one group company is responsible for another's obligations (OUT para 50 principle).

### OH7.4 Social media publishing

- **Adapters** (publish, metrics and inbox where allowed): LinkedIn organisation pages (Community Management APIs), X (API v2 paid tier for posting), Meta (Facebook Pages API; Instagram content publishing for professional accounts), YouTube (Data API v3 uploads within quota) [VERIFY: each platform's access programme, scopes, review and quotas]. Tokens sit in the vault under a group service identity, never a personal account.
- **Publishing:** only `APPROVED` items are scheduled; jobs record the platform post id, retry with back-off and alert on failure; takedowns go through the API where supported.
- **Social inbox and listening:** comments, mentions and direct messages are classified (question, complaint about a group service, complaint about a lender, press enquiry, abuse, other) and routed: service complaints to OH6, press to PR, lender complaints answered with the lender's published grievance channel; no account-specific details in public replies.

### OH7.5 Claims gate

- **Blocked phrases and patterns** unless a `claim` record with valid evidence exists: "certified", "SOC 2", "ISO 27001", "PCI compliant" (OH14 issued-certificate or report record required; Part 4.11); "RBI-approved", "RBI-certified", "approved by RBI" or the RBI logo (always blocked; RBI does not approve software) [REC]; "guaranteed compliance", "makes you compliant" (always blocked; Finbyx CM2.3); "guaranteed approval" or similar for any loan content (always blocked); client names and logos (written client consent and, for an RE, its compliance approval); performance figures (dated evidence); comparisons with competitors (substantiated and fair, ASCI Code) [VERIFY: ASCI chapter reference].
- The gate runs on content items, ad creatives, website pages generated from the Hub, sales decks stored in the asset library and explainer text supplied to products (Finbyx CM2.3; Udofin RV2).
- Every pass or block is logged and becomes OH14 evidence for marketing-claims controls.

### OH7.6 Influencers, finfluencers and endorsements

- **Disclosure:** every paid, gifted or otherwise connected post carries an upfront label ("Ad", "Sponsored", "Collaboration") as the ASCI influencer guidelines and CCPA endorsement guidelines require [VERIFY: current texts]; the contract requires it and the Hub checks the live post.
- **Financial content:** influencers commenting on banking, lending, insurance or investments must hold and disclose the qualification or registration ASCI requires [VERIFY: ASCI BFSI clause]; the group never pays anyone for securities advice or return claims or engages unregistered persons for securities content (SEBI 2024 restriction on associations with unregistered persons [VERIFY: regulation reference]).
- **Lending content** for Udofin or an RE is education only, never a promise of approval or rate, and needs the named RE's approval; no influencer pay tied to borrower sign-ups or loan volumes [REC; CF para 7(4)].
- States: `PROPOSED → DUE_DILIGENCE → CONTRACTED → CONTENT_REVIEW → LIVE → COMPLETED`, with takedown rights throughout.

### OH7.7 PR, collaborations and events

- **Media list** of journalists' published business contacts, used only for press communications, with removal on request within 7 days [REC].
- **Press-release pipeline:** `IDEA → DRAFT → CLAIMS_AND_LEGAL_REVIEW → SPOKESPERSON_APPROVED → EMBARGOED (embargo time, recipients) → RELEASED → COVERAGE_TRACKED (30 days) → CLOSED`; any change after approval returns to review; a release naming a client or regulator needs the client's written consent or legal approval.
- **Collaboration pipeline:** `PROSPECT → DUE_DILIGENCE (counterparty checks, conflict check, Equator wall, auditor-independence check where a group company audits the counterparty) → TERMS_AGREED → SIGNED → ACTIVE (deliverables, logo rights, data-sharing log) → REVIEW (at least yearly) → {RENEWED, CLOSED}`; logo use or co-branded content starts only in `ACTIVE` and passes OH7.2.
- **Crisis communications:** linked to OH13 incidents; no public statement about a security incident before affected RE clients are notified and legal approves; regulator-facing statements only by authorised officers.
- **Collaborations** need a written agreement on deliverables, logo rights, approvals and data sharing.
- **Events:** registration forms capture consent per group company and per named co-host separately (no pre-ticked boxes); attendee lists are shared with a co-host only for attendees who consented to that co-host; leads enter OH3 with their consent records.
- **Gifts and hospitality register:** every gift or hospitality given to or received from client staff above a configurable threshold is recorded and approved; anything for employees of public-sector banks, co-operative banks with State shareholding, regulators or government bodies needs prior compliance approval, because offering an undue advantage to a public servant is an offence for which a commercial organisation is liable unless it shows adequate procedures (Prevention of Corruption Act 1988, s.9 as amended in 2018) [VERIFY: thresholds and procedure guidance].

### OH7.8 Advertising and websites

- Paid ads carry the platform's label and name the advertiser; financial-services advertiser verification is completed where required [VERIFY: Google Ads and Meta India policies]; targeting uses platform audiences and the group's consented lists only, never client or product data.
- Group websites load analytics or advertising tags that process personal data only after consent (DPDP s.6); no third-party trackers on authenticated product surfaces.
- Funnels follow Finbyx CM5.4 and Udofin RV1.5: no fake scarcity, countdown timers, inflated "value" figures or unverifiable testimonials (CCPA Dark Patterns Guidelines 2023).
- Listed advocates are never advertised; the directory is promoted only in Rule 36-compliant terms (Part 4.9).

### OH7.9 Integrations and events

Uses OH3 audiences and the send gate; OH14 certification records for the claims gate; OH13 incidents for crisis communications; OH6 for routed service complaints. No ecosystem events are produced; claims-gate results are recorded as OH14 control evidence (`ControlEvidenceCollected` internal to the Hub).

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Claims lexicon (always-blocked and evidence-required phrases) per language | Platform | OH7.5 | Floor; entities may add phrases |
| Mandatory claims and legal review triggers | Platform | OH7.2 list | Floor |
| Content review date | Entity | 12 months | Commercial; may shorten |
| Approvers per brand | Brand | Brand owner plus legal; Equator content only by Equator approvers | Floor for Equator; otherwise commercial |
| Campaign pause thresholds | Entity | Opt-out rate above 2% or spam complaints above 0.1% per send [REC] | Commercial |
| Social inbox routing and response target | Team | Complaints to OH6 within 1 working day; first response 4 business hours | Commercial |
| Influencer disclosure check | Platform | Live-post check within 24 hours of publication | Floor |
| Event consent boxes | Platform | Separate per company and co-host; never pre-ticked | Floor |
| Gifts and hospitality threshold | Entity | ₹2,000 per person per occasion [REC]; any value for public servants needs prior compliance approval | Floor for public servants; threshold commercial |
| Ad tracking on group websites | Platform | Off until consent | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Marketing › Calendar` | Month and week views across brands and channels; drag to reschedule approved items (re-check of window) | Marketing, social, PR |
| `Marketing › Content` | Content list by state; editor with claims panel (live lexicon hits and evidence links); review queue; version diff; takedown | Content owners, brand and legal reviewers |
| `Marketing › Campaigns` | Campaign wizard (objective, audience freeze with consent counts, content, compliance, schedule); approval queue; results | Marketing, legal and compliance |
| `Marketing › Social` | Publishing queue, failed jobs with retry, social inbox with classification and routing, channel accounts (vault status) | Social media managers |
| `Marketing › PR` | Press-release pipeline, media list, coverage log with tone | PR lead |
| `Marketing › Collaborations and events` | Collaboration pipeline, events with registrations and per-company consents, co-host exports | Partnerships, events |
| `Marketing › Influencers` | Engagement pipeline (OH7.6), disclosure checks, takedown tasks | Social media managers, legal |
| `Marketing › Brand library` | Assets with licence and rights expiry; download logs; endorsement lines | Brand team; agencies (restricted) |
| `Marketing › Registers` | Claims register with evidence and expiry; gifts and hospitality register with approvals; ad campaigns with disclosures | Legal and compliance, marketing |

Empty state on `Marketing › Campaigns`: "No campaigns: build a consented segment in CRM first". Error state when a platform token expires: affected jobs pause and the channel owner is notified.

### Acceptance tests

- A LinkedIn post containing "ISO 27001 certified" cannot leave `CLAIMS_AND_LEGAL_REVIEW` while OH14 has no issued certificate record; the same post saying "aligned to ISO 27001" passes.
- Any content containing "RBI-approved" is blocked in every language configured.
- Only `APPROVED` items can be scheduled; editing an approved item returns it to review and cancels its scheduled job.
- An influencer post without a disclosure label is flagged within 24 hours of publication and opens a takedown or correction task.
- An event registration form with a pre-ticked co-host consent box fails template validation; a co-host export includes only attendees who consented to that co-host.
- A joint campaign combining Equator and Finbyx brands cannot be created.
- A gift recorded for an employee of a public-sector bank cannot be marked approved without compliance approval.
- A social comment classified as a complaint about a lender receives a reply template pointing to the lender's grievance channel and contains no account details.
- A contact who withdraws email consent after a campaign's audience is frozen is excluded at send time, and the refusal is recorded with reason `consent_withdrawn`.
- A campaign naming a client RE cannot leave `COMPLIANCE_APPROVED` without the RE's written approval attached.

---

## OH8. Revenue catalogue, plans, billing and revenue-model review

**Purpose.** The group's commercial system of record for what it sells to institutions: catalogue and switchable revenue streams behind a legality gate; quote to cash; signed entitlements; usage intake; GST invoicing and TDS; Razorpay collection; dunning that never interrupts a regulated function; revenue-recognition data; a lawful self-serve funnel; and revenue-model review. Finbyx (Part 7K CM1–CM5), Udofin (Part 7G RV1–RV3), Equator and LawDocsComply consume it through the Integration Specification billing domain (Part 6.27). Vendor billing never touches loan money, borrower or member data, or tenant ledgers.

**Users.** Revenue operations (catalogue maker); pricing committee (checker: CFO, product head, head of legal; CEO for a new stream); sales; billing operations; accounts receivable; finance controller; legal; customer success (OH5); management and Board; auditors (read-only, OH14). Tenant users never sign in to the Hub; product billing pages (Finbyx CM2, Udofin RV2) call Hub APIs.

**Requirement codes.** CF paras 7(4), 10(1)–(5), 24; OUT paras 15, 34, 87; `EMD`; `PA`; RBI card-on-file tokenisation circular (7 Sep 2021); `PCI` (SAQ A); `GST` (CGST Act ss.31, 34, 36; IGST Act ss.12(2), 13, 16; CGST Rules rr.46, 48(4)); `ITA25` (s.393; Forms 131, 140, 168); `IND-AS` (Ind AS 115) or `ICAI` (AS 9); `CICRA`; `CCPA` (Dark Patterns Guidelines 2023; Misleading Advertisements Guidelines 2022); `CPA19`; `ASCI`; `DPDP`; `TRAI`.

**Data owned.** Each selling group company owns its catalogue, quotes, orders, contracts, subscriptions, invoices, receipts, mandate references, TDS receivables and revenue schedules. Products own entitlement state as applied and usage at source. OH8 receives usage only as aggregates, and Udofin's B2C plan revenue only as a monthly `UsageRecorded` with `meter_kind = REVENUE_AGGREGATE` per plan (subscriber count, gross, GST; no subscriber key; Udofin RV2.4). No borrower, member or loan data; no card data.

### OH8.1 Data model

| Entity | Key fields and rules |
|---|---|
| `selling_entity` | Legal entity (OH1), GSTIN per State, PAN, Udyam number if any, Razorpay account, revenue framework (AS or IND_AS), invoice series, e-invoice flag; merchant of record per product and service line is an owner decision (Appendix B decision 2) |
| `product`, `sku`, `plan` | Products FX, UD_B2B, EQ, LDC and others by configuration; every SKU maps to modules in the product's registry (CM1.1); plans tiered by AUM band, active loans, branches, users, legal entities, environments, support tier |
| `price_book`, `price` | Market, currency, channel, model, unit price, bands, minimum commitment, effective_from, effective_to, version, approval reference; never edited in place |
| `revenue_stream`, `stream_gate`, `catalogue_version` | OH8.2, OH8.3; version content hash, JWS signature, consumer acknowledgements |
| `quote`, `order`, `contract`, `subscription`, `entitlement` | OH8.4; a quote is immutable once sent (changes create a new version) |
| `usage_aggregate` | Tenant, legal entity, meter, `meter_kind`, period, quantity, `statement_version`, statement hash, meter code version, dispute state |
| `invoice`, `credit_note`, `debit_note`, `receipt`, `mandate_ref`, `tds_receivable` | OH8.6–OH8.7; immutable once issued, corrected only by notes |
| `dunning_case`, `revenue_schedule`, `experiment` | OH8.7, OH8.8, OH8.10 |

### OH8.2 Switchable revenue streams

Every stream is switchable by product, market, tenant class, contract, channel and effective date, with version history and maker-checker approval. Products show a purchase option only when its stream has an `ACTIVE` gate (Finbyx CM5.3; Udofin RV1.3).

| Stream | Basis | Conditions |
|---|---|---|
| `ONE_TIME_SERVICE`, `IMPLEMENTATION` | Fixed deliverable; milestones tracked in OH4 | Customer acceptance before invoicing; milestones on `ImplementationMilestoneReached` |
| `SUBSCRIPTION` | Annual, quarterly or monthly; tiers by AUM band, active loans, branches, users, entities | Export and exit export always included (CM1.2; OUT para 87) |
| `MONTHLY_RENTAL` | Month-to-month dedicated environment or seat pool | Notice period; exit through the product's exit process |
| `PAYG` | Metered (per active loan, regulatory run, API call, report; Equator per published fee schedule); prepaid wallet or postpaid | Regulated functions never stop at zero balance (CM1.4) |
| `PROFESSIONAL_SERVICES` | Regulatory-change packs, custom integrations, audit assistance | No core management functions for RE tenants (OUT para 15); no outsourced internal audit to IAF in-scope NBFCs (IAF para 39); no LODR Reg 24A prohibited services where the listed client's secretarial auditor is group-linked (Finbyx GV4.2) |
| `MANAGED_SERVICES` | Operations support under an SOW | The RE runs its own materiality assessment (OUT paras 34–36); decisions stay with the RE |
| `DATA_MIGRATION`, `TRAINING` | Per migration batch or record band (OH4); per seat, batch or day | Reconciliation sign-off; no "certified compliance" claims |
| `PASS_THROUGH` | eSign, eStamp, KYC, messaging and voice at cost plus a disclosed margin | Credit-bureau enquiries run on the tenant's own CIC membership and are billed by the CIC; Infrabyx never buys, resells or re-bills credit information (CICRA) [REC] |
| `PERPETUAL_LICENCE_AMC` | Dedicated or on-premises licence plus maintenance | Offline licence file (CM1.5); escrow (CYB para 105) |
| `MARKETPLACE_REFERRAL` | Fees from certified connector vendors | Disclosed; never ranked for payment |
| `ADVERTISING_SPONSORSHIP` | Event or newsletter sponsorship; labelled content on public group websites | Never in regulated workflows, borrower or member surfaces, offer views, credit-report pages or the OH9 directory; ASCI and CCPA review; Udofin's own ads only under RV4 |
| `LSP_FEES` | Udofin RV1.1 S01–S08 | Paid by the RE only (CF para 10(4)); never from recovery proceeds (CF para 10(5)); invisible to matching and ranking (CF para 7(4)); DLG cover tracked in Udofin within the 5% cap (CF para 24; RV1.4) |

**Product rules enforced at catalogue import.**

- **Udofin:** OH8 invoices REs and non-RE lenders only. Borrower-paid streams (RV1.1 S09) are catalogued at `LEGAL_REVIEW` and cannot be activated from OH8; Udofin activates them only after FW4 gates G1–G5, an owner decision and a legal opinion, and bills them on its own Razorpay account.
- **Equator:** price books need approval by Equator's independent oversight; no bundle, discount or volume tier links Equator fees to a Finbyx or Udofin subscription; no outcome-linked fee; no fee collected through a lender's counsel; Equator is never offered as a default or free add-on in a lender plan (Integration Spec Part 8.6).
- **Deny list (hard-coded, not configurable):** the union of Finbyx CM5.2 and the Udofin RV1.1 prohibited streams: borrower or member loan-related charges, deductions from disbursals or recoveries, interest spread, paid ranking or prominence, data or score sales, advocate listing or referral fees, unlicensed distribution commissions, per-recovery success fees.

### OH8.3 Legality gate

`DRAFT → LEGAL_REVIEW → TAX_REVIEW → OWNER_DECISION (where Appendix B requires) → APPROVED → ACTIVE → {SUSPENDED, RETIRED}`; `SUSPENDED → LEGAL_REVIEW` on re-review; any review state → `DRAFT` with reasons (returned) or `REJECTED`.

- **Exit criteria:** `LEGAL_REVIEW`: payer class, legal basis with citations, legal opinion for any regulated, borrower-paid, advertising or referral stream, and a conflict check (any incentive to steer borrowers, prefer a lender or professional, or collect harshly, with the mitigating control); `TAX_REVIEW`: SAC, rate, place-of-supply rule, TDS and revenue-recognition treatment (OH8.8); `APPROVED`: refund, cancellation and proration rules, explainer passing the claims gate (CM2.3), entitlement behaviour, unit economics, owner decision where required, pricing-committee maker-checker; `ACTIVE`: an effective date and an approved price-book version.
- **Defence in depth:** each product mirrors gate status and refuses an entitlement whose stream is not `ACTIVE` locally; a mismatch raises `ComplianceIssueRaised`.
- **Re-review** annually and on change in law: an `ObligationPublished` from LawDocsComply tagged CF, RBC, EMD, PA, IRDAI, CCPA, BCI, DPDP, GST or ITA25 moves affected streams to `SUSPENDED` pending `LEGAL_REVIEW`; new sales stop, existing contracts run on their terms until the review concludes.

### OH8.4 Quote to cash: quotes, orders, subscriptions and entitlements

```
QUOTE  DRAFT → PRICED → PENDING_APPROVAL (only if discount or terms exceed the holder's DoA) → APPROVED → SENT → ACCEPTED → ORDERED
       any open state → EXPIRED (valid_until) | REJECTED (reason) | SUPERSEDED (new version)
ORDER  CREATED → CONTRACT_GATES (MSA, DPA, OUT clause matrix, due diligence; OH4) → PAYMENT_PENDING | INVOICE_LATER
       → PROVISIONING (OH4 TenantProvisioned, or signed EntitlementChanged) → FULFILLED → INVOICED
       FAILED (payment, gate or product rejection): nothing changes in the product; the quote may be re-ordered while valid
```

- **Sources:** sales quotes (workspace I) for new logos, renewals and non-standard terms; product quotes through `POST /v1/billing/quotes` for plan, add-on and seat changes (Finbyx CM2.4; Udofin RV2.5). Prices come only from the price-book version in force on the effective date; OH8 computes proration, GST and the entitlement diff; products compute no price or tax. Validity: product quotes 7 days, sales quotes 30 days [REC].
- **Approval:** within the requester's OH11 discount limit a quote is approved on pricing; above it, routed automatically; non-standard terms go to legal and Equator quotes to Equator oversight; each approval stores the rule version and reason code.
- **Order:** `POST /v1/billing/orders` with `quote_id` (or an invoice reference) creates the Razorpay order, payment link, subscription or mandate and returns a Razorpay-hosted URL for top-level redirect, or books "invoice later" where the contract allows; idempotent on `Idempotency-Key`; an expired or superseded quote returns `quote-expired`.
- **Contract gates:** MSA, DPA and OUT clause matrix (Finbyx Part 10.6; Udofin LSP agreement; Equator rules) and customer due diligence (CIN, GSTIN, PAN, RBI certificate of registration or other licence; OH4); a production order cannot pass without them.
- **Provisioning and billing:** a new tenant goes through an OH4 provisioning order (`TenantProvisioned`, product acknowledgement); an existing tenant receives one `PlanChanged` and a signed `EntitlementChanged`; the subscription becomes `ACTIVE` on the product's `READY` acknowledgement or the contract start date, whichever is later. Subscriptions are invoiced in advance, milestones after acceptance, usage after the statement is final (OH8.5); each invoice emits `InvoiceIssued`.

**Subscription states:**

```
DRAFT → PENDING_ACTIVATION → ACTIVE → RENEWAL_DUE (T-90) → RENEWED | EXIT
ACTIVE → PAST_DUE → GRACE → RESTRICTED → TERMINATION_NOTICE → EXIT → CLOSED   (OH8.7)
ACTIVE → CANCELLATION_REQUESTED → (end of paid term) → EXIT → CLOSED; withdrawable until effective
SANDBOX_TRIAL (sandbox tenants only) → CONVERTED (new production subscription) | EXPIRED
```

- `SubscriptionCancelled` is emitted when a cancellation, non-renewal or termination notice becomes effective and carries the exit path; `EXIT` hands over to the product's exit process (Finbyx Part 7J DP5; Udofin UP5; Equator and LawDocsComply equivalents); `CLOSED` only after the product confirms exit sign-off. Read and export continue throughout.
- **Entitlements** are signed (catalogue and `EntitlementChanged`); upgrades apply immediately, downgrades at term end unless contracted otherwise. OH8 is the source of truth and reconciles daily with the products (`GET /v1/entitlements`, by 06:00 IST; a mismatch raises `ReconciliationBreakRaised`); if the Hub is unreachable, products keep the last valid signed entitlement for 30 days [REC].
- **Proration:** IST calendar days (new price for the remaining days less the unused value at the old price), in paise, rounded half up; no mid-term refund on downgrade unless contracted; seat additions prorated; usage-band changes apply from the next quarter after notice (CM3.1).
- **Price changes:** at least 30 days' written notice [REC], at renewal unless the contract allows otherwise; grandfathering per price-book version. Coupons and service credits (OH6 SLA breaches) are catalogue objects with approval and expiry and always produce a credit note.

### OH8.5 Usage ingestion

- `UsageRecorded` (`usage_aggregate_v1`) carries tenantid, legal entity, meter, `meter_kind` (`USAGE`; `REVENUE_AGGREGATE` only for Udofin B2C plan revenue), period, quantity, meter code version, `statement_version` and statement hash; idempotency key `(tenantid, meter, period, statement_version)`. A replay with the same version and hash counts once; the same version with a different hash is rejected and logged. The schema forbids any loan, borrower, member, customer, user, subscriber or case identifier and any personal data; unknown fields are rejected.
- **Statements and disputes:** the product issues the monthly statement by the third working day; the tenant may dispute a meter within 7 days of issue through `POST /v1/usage-disputes` (CM3.2), which holds invoicing for that meter only; OH8 decides within 5 working days [REC]; an upheld dispute is answered by a new `UsageRecorded` with a higher `statement_version`, never a Hub-side edit. Usage corrected after invoicing appears as a credit or debit line next cycle.
- `REVENUE_AGGREGATE` statements are never invoiced; they feed revenue review (OH8.10) only.
- A subscription missing an expected meter at month end raises `ReconciliationBreakRaised`; no estimate is invoiced without customer agreement.

### OH8.6 Invoicing, GST and TDS

- **Tax invoice** (CGST Act s.31; CGST Rules r.46): supplier name, address and GSTIN; serial number unique per GSTIN per financial year, at most 16 characters; date; recipient name, address and GSTIN; place of supply; SAC; taxable value; CGST plus SGST or IGST; Udyam number and the MSMED Act s.15 45-day term where the selling entity is a micro or small enterprise [VERIFY: Udyam status per group company].
- **Place of supply:** registered recipient's location (IGST Act s.12(2)(a)); otherwise the address on record (s.12(2)(b)); intra-State CGST plus SGST, inter-State IGST.
- **SAC and rate** are tax-review fields per SKU, never hard-coded. Candidates for counsel [VERIFY all]: SaaS and hosted software 998315 or 997331; implementation and integration 998313 or 998314; managed services 998316; training 999293; rate 18%.
- **Zero-rated:** exports of services (IGST Act ss.2(6), 13) and supplies to SEZ or IFSC units under LUT (s.16), with the unit's status and LUT reference captured [VERIFY: IFSC treatment].
- **E-invoicing:** applies per selling entity once its aggregate turnover in any financial year from 2017-18 exceeds ₹5 crore (Notification 10/2023-Central Tax); Infrabyx companies are not in the r.48(4) exemption list (banking companies, NBFCs, insurers and others). Once flagged, a B2B invoice cannot issue without IRN, acknowledgement and signed QR from the IRP [VERIFY: each group company's AATO; 30-day reporting limit at AATO of ₹10 crore or more].
- **Credit and debit notes** (CGST Act s.34) for proration, service credits, disputes and refunds, referencing the original invoice; credit notes for a year issued by 30 November following its end or the annual-return date, if earlier. Records kept in India for at least 72 months from the annual-return due date (s.36) [VERIFY].
- **Return data:** OH8 prepares GSTR-1 data and journals for the selling entity's accounting system (Tally Prime connector on the Finbyx AC6 pattern); authorised staff file. No GST portal credentials or OTPs are stored.
- **TDS by customers** under ITA25 s.393(1) (successor of s.194J; Table Sl. 6(iii) [VERIFY serial, rates, thresholds]): receipts capture gross, TDS and net; a `tds_receivable` opens per invoice; customers upload the Form 131 certificate on the product billing page (CM2.2; RV2.2); quarterly reconciliation to the annual information statement (Form 168 [VERIFY]); items unmatched after a quarter go to a chase list; write-off only under the OH11 DoA.

### OH8.7 Razorpay payments and dunning

- **Accounts and secrets:** one Razorpay account per selling entity; key and webhook secrets only in the Hub vault (KMS-backed), rotated at least every 90 days; dashboard users named, with MFA, in OH11 access reviews.
- **Methods:** Payment Links and hosted or redirect checkout for one-off invoices; Razorpay Subscriptions with card or UPI AutoPay; eNACH for recurring invoices above ₹15,000; Smart Collect virtual accounts for large B2B transfers. Mandate rules exactly as Finbyx CM4.2 (`EMD` paras 4(b), 6(a)–(c), 8(a), 10(a): AFA at registration, no AFA only up to ₹15,000 per debit, issuer pre-debit notice ≥ 24 hours, opt-out, no mandate charge), plus a T-48-hour courtesy notice [REC].
- **SAQ A scope:** only Razorpay-hosted or redirect pages and Payment Links; no Razorpay script on product or Hub pages; script inventory and CSP on every page that launches checkout, so it is "not susceptible to attacks from scripts" (PCI DSS v4.0.1 SAQ A, revised 31 Jan 2025) [VERIFY current wording]; no card data stored, processed or logged (token references, last 4 digits and issuer only).
- **Webhooks:** the Finbyx CM4.3 algorithm (raw-body HMAC-SHA256, constant-time compare, de-duplication on `x-razorpay-event-id`, order-insensitive upsert by status rank, dual-secret rotation, server-side fetch on checkout return). Mapping [VERIFY Razorpay event names]: payment captured, invoice paid or virtual-account credit → `SubscriptionPaymentReceived`; payment failed, subscription pending or halted → `SubscriptionPaymentFailed` and a dunning step.
- **Reconciliation and refunds:** daily settlement reconciliation (payments, refunds, Razorpay fees and GST on fees, chargebacks) to bank and ledger, with a month-end controller certificate; refunds to the original source only, coded reasons, maker-checker above ₹25,000 [REC], each with a credit note.
- **Assurance:** Razorpay's PA authorisation (`PA`) and PCI DSS AoC filed yearly (OH14 vendor register), never presented as the group's own. No Route, split settlement or pooled mechanism ever carries loan or borrower money (CF paras 10(1)–(3)).

**Dunning that never cuts regulated functions:**

```
ACTIVE → PAST_DUE (D0) → RETRY (D+1, D+3, D+7) → GRACE (to D+14)
      → RESTRICTED (D+30, after 7 days' written notice) → TERMINATION_NOTICE (D+45 or per contract)
      → EXIT (product exit process) → CLOSED (after exit sign-off)
any state → ACTIVE on full payment or an approved payment plan; an invoice under dispute (OH6) pauses dunning for that invoice
```

- `RESTRICTED` publishes an entitlement whose only effect is to block new non-regulated units (users above the seat limit, module attachments, new product configurations and, where contracted, new intake above a cap). **The entitlement schema has no field that can stop or degrade a regulated function**, read access, export, or auditor and supervisor access (CM1.4; RV2.2; OUT para 87).
- `TERMINATION_NOTICE` is signed by an authorised signatory (OH11) and starts the product exit process with read and export available throughout; no hard cancel, kill switch or deletion instruction exists.
- At most 3 automatic retries per invoice, each within mandate notice rules; collection contact only with contracted billing contacts in business hours; legal action only on a director-level decision.

### OH8.8 Revenue-recognition data (Ind AS 115 or AS 9)

The framework per selling entity is an **owner decision** (Appendix B decision 3), following Companies (Indian Accounting Standards) Rules 2015 Rule 4 where it applies. Contract lines are split into performance obligations: subscription access (over time), implementation, migration, training, professional and managed services, pass-through, licence and AMC.

- **Ind AS 115 path [IND-AS]:** implementation tested for distinctness (if not distinct from SaaS access, recognised over the expected subscription term); usage fees as variable consideration allocated to the period of usage where the allocation exception applies [VERIFY paras 84–86]; allocation on a governed stand-alone selling price table; contract asset and liability roll-forwards; sales commissions capitalised and amortised, with the one-year practical-expedient flag [VERIFY paras 91–94]; remaining-performance-obligation data [VERIFY para 120].
- **AS 9 path [ICAI]:** service revenue as performed (proportionate completion or completed service contract method); subscriptions ratably; milestones on acceptance; postponement where collectability is uncertain.
- **Outputs:** monthly revenue, deferred-revenue and unbilled-revenue journals and disclosure tables exported to the books, reproducible from source records with the audit trail on (Companies (Accounts) Rules r.3(1) proviso). Udofin B2C revenue is booked in Udofin (U17).

### OH8.9 Self-serve funnel (legitimate automation only)

The owner's reference page (ptstdm.co.in, reviewed 23 Oct 2026) is a coaching-workshop funnel built on countdown urgency, anchor prices and unverifiable testimonials; it is not a model to copy. OH8 adopts only: public pricing-basis pages generated from the catalogue; self-serve **sandbox trials** with synthetic data only (`TenantProvisioned`, environment `SANDBOX`; CM5.4); onboarding wizards and in-product activation; **automated nurture** through OH3 only with recorded consent and purpose match, opt-out in every message, DLT templates and the 140-series for any promotional voice (TCCCPR); usage alerts at 80% and 100%; renewal reminders at 90, 30 and 7 days; webinars with disclosures. A production tenant still needs the signed MSA, DPA, OUT clause matrix and due diligence (CM5.4; RV1.5).

**Prohibited everywhere** (CCPA Dark Patterns Guidelines 2023, adopted for B2B too; `CPA19`; `ASCI`): every specified dark pattern (false urgency, basket sneaking, confirm shaming, forced action, subscription trap, interface interference, bait and switch, drip pricing, disguised advertisement, nagging, trick question, SaaS billing, rogue malpractices [VERIFY list]), plus fake scarcity, inflated "value" figures, anchor prices never charged, unverifiable testimonials and compliance-outcome claims. Trials never convert to paid automatically; cancellation takes no more steps than purchase. The shared claims gate (OH14.6) enforces this.

### OH8.10 Revenue-model review workspace

```
MRR = Σ recurring monthly-equivalent revenue;  ARR = 12 × MRR
NRR = (opening ARR + expansion − contraction − churn) ÷ opening ARR      (trailing 12 months, by cohort)
GRR = (opening ARR − contraction − churn) ÷ opening ARR
gross_margin = (revenue − hosting − pass-through cost − support and delivery cost) ÷ revenue
CAC = (sales + marketing cost) ÷ new customers;  CAC_payback_months = CAC ÷ (new ARPA_monthly × gross_margin)
LTV = ARPA_monthly × gross_margin ÷ monthly_logo_churn;  LTV_to_CAC = LTV ÷ CAC
```

- **Cohorts** by signing quarter, product, entity type (NBFC layer, co-operative, ARC, HFC), plan and channel; logo and revenue retention curves; implementation margin.
- **Scenario modeller:** switch a stream (for example subscription to PAYG for small NBFCs) and see revenue, cash and margin effects on the current book, with each scenario's gate status shown.
- **Pricing experiments:** `PROPOSED → APPROVED (pricing committee) → RUNNING → STOPPED → CONCLUDED`; B2B segments and new customers only unless contracts permit; never on borrowers or members; never varying regulatory functions or exit rights; pre-registered metric and stop rule.
- **Data:** aggregates only (Udofin B2C cohorts of at least 100); quarterly Board pack.

### OH8.11 Integrations and events

| Event or API | Producer → consumer(s) | Notes |
|---|---|---|
| `GET /v1/catalogue/versions/{v}` | FX, UD, EQ, LDC → OH8 | Signed catalogue (JWS against the pinned Hub key), fetched on `PlanChanged` and daily |
| `POST /v1/billing/quotes` | FX, UD billing pages → OH8 | Priced quote and proration preview: quote_id, price, prorated charge or credit, GST, entitlement diff, valid_until |
| `POST /v1/billing/orders` | FX, UD billing pages → OH8 | Order, payment link, subscription or mandate from an approved quote or an invoice; returns a Razorpay-hosted URL |
| `GET /v1/billing/invoices`, `POST /v1/usage-disputes` | FX, UD → OH8 | Invoice display; meter disputes within 7 days |
| `GET /v1/entitlements` | OH8 → FX, UD | Daily reconciliation of entitlements as applied |
| `PlanChanged`, `EntitlementChanged` | OH8 → FX, UD | Signed entitlement; no field can disable a regulated function |
| `UsageRecorded` | FX, UD → OH8 | Aggregates only; `meter_kind` USAGE or REVENUE_AGGREGATE |
| `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed` | OH8 → FX, UD (RE and tenant billing only) | Billing domain, distinct from servicing `PaymentReceived`; Udofin B2C invoices and payments are Udofin-internal and never reach the Hub |
| `SubscriptionCancelled` | OH8 → FX, UD | When cancellation, non-renewal or termination becomes effective; carries the exit path (DP5 or UP5) |
| `ModuleAttached`, `ModuleDetached` | Product entitlement services → OH8 | Applied state for reconciliation |
| `TenantProvisioned`, `ImplementationMilestoneReached` | OH4 → OH8 | Start billing; milestone invoices |
| `ReconciliationBreakRaised`, `ComplianceIssueRaised` | OH8 → owners | Missing meters, settlement breaks, entitlement and gate mismatches |
| `ObligationPublished` | LDC → OH8 | Gate re-review |

External: Razorpay API and webhooks; IRP e-invoice API (direct or through a GSP); accounting export.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Deny list; regulatory-continuity rule on entitlements | Platform | Always on | Hard floor; no setting or schema field exists |
| Stream flags | Stream × market × tenant class × channel | Off | Commercial; `ACTIVE` only through the gate |
| Quote validity | Platform | Product quotes 7 days; sales quotes 30 days [REC] | Commercial |
| Discount authority | Selling entity | OH11.1 DoA table | Board-approved; changes by maker-checker |
| Proration basis and rounding | Platform | IST calendar day; paise, half up | Contractual default |
| Price-change notice; renewal reminders | Platform | ≥ 30 days [REC]; 90, 30 and 7 days | Floor |
| Usage dispute window | Platform | 7 days from statement issue | Floor (CM3.2) |
| Dunning offsets and notice templates | Contract | OH8.7 timeline | Commercial; `RESTRICTED` scope and the no-hard-cancel rule are floors |
| Courtesy pre-debit notice | Tenant | T-48 hours, on | Commercial; the issuer notice is separate and mandatory |
| Refund maker-checker threshold | Selling entity | ₹25,000 [REC] | May be lowered |
| SAC, GST rate, place of supply per SKU; e-invoice flag | SKU; selling entity | Tax review; flag on once AATO exceeds ₹5 crore | Regulated configuration; switching off needs tax review |
| Revenue framework and SSP table | Selling entity | Owner decision | Statutory |
| Trial auto-conversion; pricing experiments | Platform; segment | Never; off | Floor; OH8.10 guard-rails |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Revenue › Catalogue` | Products, SKUs (module-registry check), meters, price books by version, stream flags; legality-gate board (state, checklist, next review); publish a signed version with diff preview and consumer acknowledgements | Revenue operations (maker); pricing committee, legal, tax (checkers) |
| `Revenue › Plans` | Tiers and bands, entitlement templates, add-ons and dependencies, explainers with claims-gate status, grandfathering | Revenue operations, product heads |
| `Revenue › Quotes` | List (entity, product, stage, expiry); builder with live GST, proration and DoA indicator; approval queue; send, accept, convert to order; versions | Sales; DoA approvers |
| `Revenue › Subscriptions` | By state; detail with contract, entitlements published and applied, usage and disputes, invoices, dunning stage, exit link; change, renewal and cancellation requests | Billing operations; customer success (read) |
| `Revenue › Invoices` | Billing-run preview with validation report; issue (IRN); credit and debit notes; TDS receivables and Form 131 matching; GSTR-1 data export | Billing operations (maker), finance controller (checker) |
| `Revenue › Collections` | Payments, mandates, settlements and breaks; refund queue; dunning board with notices; disputes; webhook log | Accounts receivable, finance |
| `Revenue › Revenue review` | MRR, ARR, NRR, GRR; cohorts; scenarios; experiments; recognition journals; Board pack | Finance controller, CFO, management; Board (read) |

Queues have saved views, keyboard actions and CSV or XLSX export. Error states never imply a service stop ("Razorpay unavailable: payment links are queued; no subscription changes state").

### Acceptance tests

- A catalogue import with a borrower-paid, loan-linked stream, a bureau resale line or an advertising placement on an offer view or the directory is rejected; an Equator price book without oversight approval, or a bundle tying Equator fees to a Finbyx plan, cannot publish.
- Switching off `MONTHLY_RENTAL` for a market hides it on Finbyx billing pages without a deploy; a stream without an `ACTIVE` gate never appears as a purchase option; an `ObligationPublished` tagged CF suspends affected streams for new sales only.
- `POST /v1/billing/quotes` returns price, proration, GST and entitlement diff; ordering an expired quote returns `quote-expired`; a quote with a 25% discount routes to the CEO; an order without a DPA reference cannot pass `CONTRACT_GATES`.
- A `UsageRecorded` payload with `loan_id`, `customer_id`, a subscriber key or a PAN-like value is rejected; a replay with the same `statement_version` counts once; an upheld dispute produces a higher `statement_version`; a `REVENUE_AGGREGATE` statement never produces an invoice.
- A Delhi GSTIN invoice to a Rajasthan recipient carries IGST and to a Delhi recipient CGST plus SGST; once e-invoicing is flagged, a B2B invoice without IRN cannot issue.
- An upgrade effective 21 Nov 2026 prorates 10 of 30 days and emits one `PlanChanged` and one `EntitlementChanged`.
- A tampered webhook is rejected; a duplicate event id changes nothing; a browser "success" without server confirmation leaves the invoice unpaid; an ₹18,000 recurring card debit cannot be set up as a no-AFA mandate.
- A `RESTRICTED` subscription's entitlement leaves COB, CIC filing, grievance handling, read and export untouched in a Finbyx contract test; no API issues a deletion or kill instruction.
- Under Ind AS, a non-distinct ₹6,00,000 implementation fee on a 36-month subscription recognises ₹16,666.67 a month from go-live, with the paisa remainder in month 36.
- A funnel page with a countdown timer fails the claims gate; a trial ends without a charge.

---
## OH9. Professional and advocate directory (group-wide)

**Purpose.** A verified, group-wide master of external professionals (advocates and law firms, valuers, investigators, recovery agencies and agents, auctioneers and e-auction providers, insolvency professionals, chartered accountants and company secretaries), so that credentials are verified once, kept current and suspended everywhere at once when they lapse. The directory **feeds** Finbyx Part 7A R11 (counsel, agency and vendor management; later the standalone Udolex) and group sites through APIs; each lender still empanels and allocates under its own responsibility (OUT para 17). Arbitrators and mediators sit in a separate partition used only by Equator's own panel processes. The public listing shows advocates only what BCI Rule 36 permits.

**Users.** Directory administrator and verification officers (makers); head of legal (checker); professionals (portal); group legal teams (own matters); lender tenants through Finbyx R11 (API only); group websites (public listing API); Equator panel administrator (neutral partition only); internal audit (read-only).

**Requirement codes.** `BCI` Part VI Ch II r.36 with the proviso and Schedule inserted by Resolution 50/2008 (24 Mar 2008); Advocates Act 1961 s.35; *P.N. Vignesh* (Madras HC, 2024) and BCI notices of 6 Jul 2024 on "top" and "premium" labels; RBC paras 94–99 and 100E–100N (from 1 Jan 2027); CF para 10(5); OUT paras 17, 34, 36, 47; SARFAESI Security Interest (Enforcement) Rules 2002 r.8(5) [VERIFY "approved valuer"]; Companies (Registered Valuers and Valuation) Rules 2017; IBBI (Insolvency Professionals) Regulations 2016 [VERIFY]; ICAI and ICSI advertisement and website guidelines [VERIFY]; Arbitration and Conciliation Act 1996 Fifth to Seventh Schedules; Mediation Act 2023 [VERIFY provisions in force]; `GST` (Notification 13/2017-Central Tax (Rate) Sl.2 and Sl.8); `ITA25` s.393; `DPDP`.

**Data owned.** The directory operator (Infrabyx) is fiduciary for directory data. Lenders own their panel decisions, fee agreements, allocations, matter files and scorecards in their own tenant; none of it is copied into the Hub. Equator owns its neutral panel. No borrower or member data is held in OH9.

### OH9.1 Categories and credentials

| Category | Credentials verified (evidence: register extract or letter, dated and hashed) | Recheck |
|---|---|---|
| Advocate | Enrolment number, State Bar Council, enrolment date, certificate of practice where applicable, AIBE certificate for post-2010 enrolments [VERIFY], PAN, GSTIN if any, practice areas, forums, languages | Certificate-of-practice cycle [VERIFY]; annual no-disciplinary-order declaration |
| Law firm | Firm deed or LLP registration, partners' enrolments, PAN, GSTIN, offices | Annual |
| Valuer | IBBI registered-valuer number and asset class; SARFAESI approval where the lender requires; independence declaration | Registration validity |
| Investigator | Entity KYC, staff identity and police verification, any State licence [VERIFY: no central private-detective law], data-protection undertaking | Annual |
| Recovery agency and agents | Entity KYC; each agent's identity, police verification (RBC para 94; para 100H), IIBF DRA certificate (para 100I from 1 Jan 2027), code-of-conduct undertaking (para 99) | Certificate and verification expiry |
| Auctioneer and e-auction provider | Entity KYC; bid-log export and platform security evidence | Annual |
| Insolvency professional | IBBI registration, insolvency professional agency, authorisation for assignment [VERIFY] | Authorisation validity |
| Chartered accountant and CA firm | ICAI membership and certificate of practice; firm registration; peer review where required | Validity of each |
| Company secretary and CS firm | ICSI membership and certificate of practice; firm code; peer review (needed for listed-entity secretarial audit, LODR Reg 24A) | Validity of each |
| Arbitrator and mediator | **Equator partition only**, under Equator's panel rules | Per Equator |

- Officers verify from official registers only; no automated scraping of portals that require login or prohibit it. KYC documents (PAN, GSTIN, bank by penny-drop with name match ≥ 85%, OH11) are `RESTRICTED`.
- Professional indemnity insurance recorded where held; required for law firms, valuers and insolvency professionals handling group matters [REC].

### OH9.2 Empanelment and verification workflow

```
INVITED | APPLIED → PROFILE_SUBMITTED → KYC_VERIFIED → CREDENTIALS_VERIFIED
  → DUE_DILIGENCE (institutional conflicts, disciplinary history, references, PI insurance, data-protection undertaking)
  → AGREEMENT_SIGNED (directory terms, DPA, code of conduct, consents) → EMPANELLED → ACTIVE → ANNUAL_REVIEW → ACTIVE
any verification state → RETURNED (reasons; professional re-submits; 30-day clock) | REJECTED (reasons; re-application after 6 months [REC])
ACTIVE → SUSPENDED (credential lapse, disciplinary order, conduct finding, failed review) → ACTIVE (cure) | REMOVED
ACTIVE → LAPSED (declarations not renewed within 30 days of review);  any → WITHDRAWN (professional's request)
```

- **Verification workbench:** each credential is checked against its register by an officer, who records source, date, extract hash and result; a mismatch (name, number, status, expiry) blocks progress with a reason shown to the professional; a second officer re-verifies a 10% random sample each month [REC].
- **Maker-checker:** officer prepares, head of legal approves `EMPANELLED`; an approver who declared a relationship with the professional is blocked (OH11 conflict register).
- **Free to professionals:** no listing, empanelment or allocation fee, and no referral fee or share of fees either way (BCI Rule 36; OH8 deny list).
- **Clocks:** expiry alerts at 60 and 30 days; on expiry `SUSPENDED` for that category and `ProfessionalSuspended` with reason `CREDENTIAL_LAPSED` within 1 hour; a cure re-emits `ProfessionalEmpanelled` with a new version.
- **Fee schedules:** a group reference schedule by matter type, forum and stage and standard engagement letters for the **group's own matters** only; lenders' fee terms live in Finbyx R11.3.

### OH9.3 Two layers and the allocation feed

| Layer | Decision owner | Where |
|---|---|---|
| Group directory: verified, current, listed or unlisted | Directory operator | OH9 |
| Lender panel: approved for that lender's matters, OUT para 34 contract, outsourcing register (OUT para 36), RBC agent rules | Each lender's committee | Finbyx R11.1 in the lender's tenant |
| Group companies' own panels | Each group company's legal head | OH9 group-matters view |

| API or event | Producer → consumer(s) | Content |
|---|---|---|
| `GET /v1/directory/professionals` | FX R11, Udolex, group legal tools and websites → OH9 | Filters: category, State, district, forum, practice area, language; only `ACTIVE` with current credentials; Rule 36 fields and status; **order randomised per call** (seed logged); no ranking or sort-by-score parameter |
| `GET /v1/directory/professionals/{id}` | FX R11, Udolex → OH9 | Rule 36 fields, credential summary and expiries, verification dates and evidence hashes, PI status, declared institutional conflicts |
| `ProfessionalEmpanelled` | OH9 → FX R11, Udolex | professional_id, Rule 36 fields only, courts, languages, `equator_neutral` flag; idempotent on (professional_id, version) |
| `ProfessionalSuspended` | OH9 → same | professional_id, reason class (`CREDENTIAL_LAPSED`, `DISCIPLINARY`, `CONDUCT`, `REVIEW_FAILED`, `WITHDRAWN`), effective_at; idempotent on (professional_id, suspension_seq); ≤ 1 hour |
| `MatterAllocated` | FX R11 or Udolex → OH9; group legal tools (`oh` scope) → OH9 | allocation_id, professional_id, `reid`, matter class, forum type and State, allocation basis (`ROTATION`, `RULE`, `REASONED_EXCEPTION`), allocated_at, status (`OFFERED`, `ACCEPTED`, `DECLINED_CONFLICT`, `DECLINED_CAPACITY`, `WITHDRAWN`), `update_seq`; a status change is an update with a higher `update_seq`; **never party names, matter or case numbers, loan identifiers or amounts** |

- R11.1 uses `ProfessionalEmpanelled` to pre-fill the lender's checklist; the lender still approves. `ProfessionalSuspended` fails the R11.2 eligibility gate for new allocations at once; live matters are flagged to the lender, which decides; the Hub never reallocates a lender's matter. `equator_neutral` is a yes or no flag only, so R11 can block that professional as counsel in matters referred to Equator.
- `MatterAllocated` serves only capacity and concentration (alert if one professional holds more than 25% of group-sourced matters in a district [REC]) and the professional's portal view; detailed events are opt-in per tenant, otherwise monthly counts only.
- **Conflicts:** institutional conflicts (acting for or against a lender, group company or affiliates) are declared and checked at empanelment; matter-level conflicts are checked by the professional on receipt and by the lender in R11.5; acceptance requires a recorded "no conflict". OH9 never receives borrower identities, even hashed [REC; DPDP minimisation]. Equator's neutral screen uses the OH1.6 conflict service (`POST /v1/conflicts/check`).
- **Scorecards** stay in each lender's R11.4 and never reach the Hub or other lenders (OUT para 47); the Hub keeps scorecards only for the group's own matters.

### OH9.4 Public listing (Rule 36)

- **Advocates and law firms:** only the Schedule fields: name, address, telephone numbers, email, enrolment number, enrolment date, State Bar Council, place of practice, professional and academic qualifications, practice areas [VERIFY Schedule wording]; each shown only with the advocate's consent and self-certification.
- **Never displayed:** ratings, reviews, testimonials, "top", "premium", "featured" or "verified expert" labels, success rates, case counts, fees, photographs, client names, "book now" or "get a quote" buttons, paid or sponsored positions.
- **Order:** alphabetical or random within location and practice-area filters, with the method stated; no "recommended" sort. Every page carries a disclaimer that the information is furnished by advocates on request, is not solicitation and is not a recommendation.
- **Other professions** use a per-profession field set under their bodies' guidelines [VERIFY]; valuers, insolvency professionals, investigators, agencies and auctioneers are not publicly listed (each RE publishes its own agents, RBC para 97); neutrals never appear (Equator publishes its own panel).
- The listing response schema is fixed; any field outside the permitted set fails CI. Group sites receive only this listing; allocation APIs serve institutional users for their own matters, never consumers looking for a lawyer.

### OH9.5 Equator separation, privacy and payments

- **Neutral partition** (`eq_panel`): separate schema, keys and admin group run by Equator's panel administrator; no lender-facing API returns neutral records; Hub legal operations cannot read it. OH9 offers Equator only a credential-verification utility; random allocation, per-lender caps and Schedule disclosures stay in Equator (Integration Spec Part 8.6).
- **DPDP:** notice at profile creation; separate consents for public listing and for sharing with subscribing lenders; the professional can view, correct and withdraw (public listing removed within 24 hours [REC]; records needed for completed matters, tax and audit retained, and the professional told what and why); verification evidence kept for empanelment plus 8 years [REC].
- **Group-matter payments:** invoices matched to engagement letter and schedule; GST reverse charge on advocate services (Sl.2) and, where the paying group company is an NBFC, on recovery-agent services (Sl.8) [VERIFY]; TDS under ITA25 s.393(1) [VERIFY serial and rate]; payment through OH11 maker-checker.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Public listing field set per profession | Platform | Rule 36 Schedule fields | Regulated configuration; cannot widen (CI schema test) |
| Ordering method | Platform | Seeded random, seed logged; alphabetical optional | Floor: no score, payment or "recommended" sort exists |
| Listing and lender-sharing consents | Professional | Off until given | Floor |
| Credential checklists and verification sources | Category | OH9.1 | Regulated configuration (head of legal) |
| Second-officer verification sample | Platform | 10% a month [REC] | May be raised |
| Expiry alerts; review cycle; lapse window | Category | 60 and 30 days; annual; 30 days | May be tightened |
| Detailed `MatterAllocated` | Lender tenant | Off (monthly counts only) | Tenant choice |
| Concentration alert | Platform | 25% per district [REC] | Commercial |
| Public-listing removal on withdrawal | Platform | 24 hours [REC] | Floor |
| Disclaimers and consent texts by language | Platform | English and Hindi | Regulated configuration |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Directory › Professionals` | List (filters: category, State, district, status, expiry window); profile with credential timeline, evidence hashes, consents and conflicts; suspend, reinstate or remove (maker-checker); public-listing preview exactly as published | Directory administrator, head of legal; internal audit (read) |
| `Directory › Empanelment` | Application queue by state and age; verification workbench (register extract beside the claim, checklist, evidence upload and hash, return with reasons); approval queue; renewals and expiries board; sample re-verification queue | Verification officers (makers), head of legal (checker) |
| `Directory › Allocations` | Aggregate allocation counts by professional, category and district; concentration alerts; group-matters allocations, engagement letters and invoices | Group legal; directory administrator |
| Professional portal | Profile, documents, declarations, consents, matter offers (accept, decline for conflict or capacity), own data requests | Professionals |
| `Directory › Equator partition` | Credential verification for neutrals; no lender data | Equator panel administrator only |

A professional with an expired credential sees what lapsed and how to cure it; a lender API caller receives `not_active` with the reason class, never private documents.

### Acceptance tests

- The public listing response contains only Rule 36 Schedule fields; adding `rating`, `fee` or `badge` to the schema fails CI.
- Two identical searches return the same set in different orders with logged seeds; no parameter sorts by any score.
- A certificate-of-practice expiry moves the advocate to `SUSPENDED`, emits `ProfessionalSuspended` with `CREDENTIAL_LAPSED` within 1 hour, and a Finbyx R11 allocation to that advocate is blocked in a contract test.
- A credential mismatch returns the application to `RETURNED` with the reason; a re-submission restarts verification of that credential only.
- A `MatterAllocated` payload containing a party name, loan number or PAN-like value is rejected; a `DECLINED_CONFLICT` update with a lower `update_seq` than the stored one is ignored.
- No lender-facing call returns a neutral record; a Hub legal-operations user cannot open `eq_panel`; withdrawn listing consent removes the professional from the public listing within 24 hours.
- An approver with a declared relationship cannot approve that professional's empanelment; a listing or referral fee cannot be created in OH8.

---
## OH10. Infrabyx staff HRMS and payroll

**Purpose.** Run the employee lifecycle and payroll for the group's employing companies (and, as processor under an intra-group DPA, for Equator, LawDocsComply and other group companies that use the shared payroll service), lawfully under the four Labour Codes and the Shops and Establishments laws for the owner's offices in **Delhi, Noida (Uttar Pradesh) and Jaipur (Rajasthan)**, with transparent work-from-home rules, outcome-based performance management and maker-checker on every money and rating decision. The calculation core is the **shared, signed Labour Code rule pack** also used by Finbyx GV6, so a law change is implemented once.

**Users.** Employees (self-service); line managers; HR operations (maker); HR head (checker); payroll (maker); finance (bank-file releaser); CFO; entity heads (DoA); IT (provisioning checker, OH12); Internal Committee members (POSH only); DPO; internal audit (read-only).

**Requirement codes.** `LC`: Code on Wages 2019 (CoW) ss.2(y), 17, 18 and the bonus chapter [VERIFY sections]; Wages (Central) Rules 2026 (G.S.R. 343(E); corrigendum G.S.R. 629(E)) rr.3, 5, 6, 13, 48, 51, 52; OSHWC Code 2020 ss.6(1)(f), 32 and Central Rules 2026; Code on Social Security 2020 (EPF, ESI, gratuity, maternity) [VERIFY sections]; IRC 2020 s.29 Model Standing Orders (8 May 2026); Delhi Shops and Establishments Act 1954; UP Dookan Aur Vanijya Adhishthan Adhiniyam 1962 as amended 19 Nov 2025; Rajasthan Shops and Commercial Establishments Act 1958 with the order of 19 Aug 2025; `ITA25` ss.392, 395, 202, Forms 130 and 138; `POSH` ss.4, 6, 9–13, 16, 18, 21, 26; Companies (Accounts) Rules r.8(5)(x); `DPDP` ss.7(i), 8(5), 8(7), Rules r.8(3); `CERTIN`.

**Data owned.** Each employing company is employer and fiduciary; the Hub operator is processor for shared-service companies (DPA: purpose, security, sub-processing, 24-hour breach notice, return and deletion, audit). HR data is `RESTRICTED`: separate schema and keys; held only in the Hub or in India-resident Microsoft 365 (OH12.1), never in Google Workspace; never in group dashboards except aggregates with a minimum cell of 5; never used for AI training.

### OH10.1 Shared Labour Code rule pack

- **Artefact** `infrabyx-labour-rulepack` (Integration Spec Part 12.3): semantic version, effective-dated, JWS-signed manifest with SHA-256 per file, published from `infrabyx-contracts/rulepacks/labour-codes/` with legal and payroll CODEOWNERS; pinned in `contracts.lock` by OH10 and Finbyx GV6; salary TDS in the companion pack `ita25-salary-tds`.
- **Contents:** CoW s.2(y) component classifier and 50% add-back; leave floor (OSHWC s.32); hours, weekly rest and overtime; gratuity, bonus and maternity; EPF and ESI rates, ceilings and thresholds; minimum and floor wage tables; State tables (S&E hours, overtime caps, night work for women, holidays, PT, LWF); Form V and Forms I, IV and IX layouts; the prohibited-monitoring list; legal basis per rule; golden fixtures.
- **Control:** a rule change is a `REGULATED` change in OH13 (CAB plus legal reviewer) with golden fixtures; consumers refuse an unsigned or tampered pack; a rule still marked `[VERIFY]` cannot drive a statutory output; each payroll run records the pack version. Until a State notifies final rules under the Codes, its old rules continue so far as consistent (MoLE FAQ 1), tracked in `state_rule_status` [VERIFY Delhi, UP, Rajasthan at go-live].

### OH10.2 State matrix and thresholds

| Item | Delhi | Noida (UP) | Jaipur (Rajasthan) |
|---|---|---|---|
| S&E law | Delhi S&E Act 1954 [VERIFY 2025–26 amendments] | 1962 Act as amended 19 Nov 2025: 20+ employees; outsourced staff count | 1958 Act; up to 10 workers exempt from registration (order of 19 Aug 2025) |
| Hours and overtime | Pack [VERIFY]; Code floor 8 h a day, 48 h a week, overtime 2× with consent, 144 h a quarter | 9 h a day; up to 11 h with overtime; 144 h a quarter | Pack [VERIFY] |
| Women at night | Consent and safeguards [VERIFY] | 7 pm–6 am with consent and amenities | Consent and safeguards [VERIFY] |
| PT and LWF | No PT; LWF under the Delhi Labour Welfare Fund Act 1997 [VERIFY rates] | No PT; no LWF [VERIFY] | No PT; no LWF [VERIFY] |

Monthly headcount drivers per office and entity open compliance tasks with due dates when crossed: "worker" status (supervisors above ₹18,000 a month excluded, MoLE FAQ 14); EPF at 20+; ESI at 10+ in notified areas; gratuity at 10+; POSH Internal Committee at 10+ per office; Model Standing Orders at 300+; S&E registration thresholds above.

### OH10.3 Lifecycle

```
REQ_DRAFT → REQ_APPROVED (DoA, OH11) → OFFER_ISSUED → OFFER_ACCEPTED → PREBOARDING
  → IDENTITY_PROVISIONED (OH12) → JOINED → PROBATION → CONFIRMED
  → (TRANSFER | ROLE_CHANGE | ENTITY_TRANSFER)* → EXIT_INITIATED → LAST_WORKING_DAY
  → FNF_WAGES_PAID → FNF_OTHER_PAID → ARCHIVED
OFFER_ACCEPTED or PREBOARDING → ARCHIVED (offer withdrawn or no-show; pre-created identity de-provisioned)
EXIT_INITIATED → prior state (resignation withdrawn before LAST_WORKING_DAY; manager and HR approval)
```

- **Appointment letter mandatory** (OSHWC s.6(1)(f)): cannot issue without name, date of birth, joining date, designation, employer and office, worker category, wage components each tagged with their CoW class, social-security applicability, probation, notice, place of work, WFH clause and leave policy; pre-Code staff get backfill letters due within 3 months of the OSHWC Central Rules; an offer below the applicable minimum or floor wage is blocked.
- **Pre-boarding:** DPDP notice; background checks only with consent and only for privileged IT, finance, payroll and security roles [REC]; no caste, religion or health data unless law requires it.
- **Provisioning (HR maker, IT checker):** OH12 creates the email ID, mailbox, licences, groups and the Hub user with entity scopes and MFA; idempotent on `(employee_id, provider, action)`.
- **Probation** 6 months, extendable once by up to 3 months with written reasons [REC; mirrors the services MSO]; confirmation by manager with HR checker; no auto-termination at probation end.
- **Transfers:** within an entity, cost centre, State rules and access change (OH12 mover flow); between group companies the employer changes, so a new appointment letter and either final settlement or a tripartite continuity agreement for gratuity and leave are recorded first [REC].
- **Exit timers** from `EXIT_INITIATED`: final wages with leave encashment within **2 working days** of the last working day on the State calendar (CoW s.17(2)), through an off-cycle run where needed; gratuity within 30 days; service certificate within 10 days where the MSO apply. Access off at 18:00 on the last working day (immediately on dismissal). Final wages never wait for clearance or asset return; notice-pay, joining-bonus and training-bond recoveries are not s.18 permitted deductions and become receivables; deductions never exceed 50% of wages (s.18(3)), excess carried forward (r.13). A back-dated exit (absconding) runs the timer from the recorded last working day and flags any breach to the HR head.

### OH10.4 Leave, attendance and hours

- **Leave floor** (OSHWC s.32): eligibility after 180 days' work in a calendar year; `floor(days_worked ÷ 20)`; carry forward up to 30 days (employer-refused leave without cap); year-end encashment on request and of any excess; paid with final wages on exit. Group policy adds casual, sick, maternity (CoSS) [VERIFY], paternity and special leave; requests `SUBMITTED → APPROVED | REJECTED (reason) → TAKEN → CANCELLED | CURTAILED`; balances always visible; leave without pay flows to payroll automatically.
- **Attendance** from IdP sign-in and sign-out (OH12), office access logs where used, and the employee's declaration; the employee sees every record and can request a correction (approved or refused with reasons, original kept); corrections after cut-off flow to the next run as arrears; registers kept 5 years (r.51).
- **Hours:** 8 a day, 48 a week, at most 6 days, no more than 10 consecutive days without rest (rr.5–6); stricter State limits from the pack; overtime only with recorded consent, paid at 2× (`ot_hours × monthly_rate ÷ 26 ÷ 8 × 2`), blocked at 144 hours a quarter; women before 06:00 or after 19:00 only with consent and State safeguards. Holiday calendars per State published yearly in the pack.

### OH10.5 Work from home and work measurement

- **Basis:** WFH is a term of the appointment letter and the WFH policy (Appendix B decision 7); where the services MSO apply (300+ workers) the employer may permit WFH for the periods it decides (IRC s.29 MSO).
- **Allowed data:** IdP login and logoff; self-entered timesheets by project, ticket or task; outcomes from work systems (OH6 tickets and SLAs, OH4 milestones, merged and reviewed pull requests, OH7 deliverables); device-compliance status; security logs.
- **Prohibited, with no setting to enable them:** keystroke or mouse-activity scores, screenshots, screen, webcam or microphone capture, off-duty location tracking, browser-history capture, covert monitoring, and AI productivity scores used for discipline, pay or termination.
- **Legal test:** employment processing is a legitimate use under DPDP s.7(i) [VERIFY wording], still bound by purpose limitation, safeguards (s.8(5)) and erasure (s.8(7)); until the core obligations commence (13 May 2027) IT Act s.43A and the SPDI Rules 2011 apply. Each data source passes the *K.S. Puttaswamy* (2017) 10 SCC 1 proportionality test (legitimate aim, suitability, least intrusive means, balancing), recorded as a data-protection assessment in OH14 [REC]. A monitoring notice (purposes, data, viewers, retention) is acknowledged at joining and on change; employees see and correct their records.
- **Use:** outcomes, not activity, are assessed; individual work metrics are visible only to the employee, line manager and HR in appraisal; no leaderboards; team metrics feed OH11.6. Timesheets kept 3 years [REC]; security logs 180 days in India (CERT-In) and 1 year in all (DPDP Rules r.8(3)).

### OH10.6 Payroll

Formulas are those of the shared pack and Finbyx GV6.5 (CoW wages with 50% add-back; EPF on the ₹15,000 ceiling re-notified 29 May 2026; ESI 0.75% and 3.25% with the employee share waived at an average daily wage up to ₹176 [VERIFY coverage ceiling]; overtime 2×; PT and LWF from State tables; s.18 deduction cap).

```
DRAFT → INPUTS_OPEN → INPUTS_LOCKED (cut-off) → CALCULATED → VARIANCE_REVIEWED → APPROVED
  → BANK_FILE_GENERATED → RELEASED (two persons) → PAID → STATUTORY_FILES_READY → POSTED → CLOSED
VARIANCE_REVIEWED or APPROVED → CALCULATED (rejected with reasons; inputs reopened only by the HR head)
PAID → re-issue line for a bounced credit (same run); errors after PAID → off-cycle run or recovery within s.18, never an edit
```

- **Calendar:** inputs lock on the 20th [REC]; pay day within the CoW limit (s.17(1): for a monthly wage period, by the 7th of the following month [VERIFY]); joiners after cut-off and arrears go to the next run; an exit inside a cycle triggers an off-cycle final-wage run.
- **Variance review (`CALCULATED → VARIANCE_REVIEWED`):** the system compares each line with the previous run and lists per-head net change above ±10%, new or changed bank accounts, joiners and leavers, arrears and back-dated revisions (tax recomputed), manual overrides, negative net pay, pay below the minimum or floor wage (blocking), and lines with no sign-in for 30 days outside leave (OH11.3); each item needs a cleared reason from payroll before submission.
- **Maker-checker and SoD:** payroll prepares and clears variances; the HR head or CFO approves; finance generates and releases the bank file (two persons; file hash compared at upload); nobody approves or releases a run containing their own pay line (a director approves that line); employee bank changes need portal confirmation and a 48-hour hold (OH11.2).
- **Bonus** under CoW from the pack [VERIFY percentages and ceilings]. **Gratuity** `round(15 ÷ 26 × last monthly CoW wages × completed years)`, part year above 6 months counted, ceiling ₹20 lakh; after 5 years, on death or disablement, and for **fixed-term employees after 1 year**; due within 30 days; accrued under AS 15 or Ind AS 19.
- **Income tax:** TDS under ITA25 s.392(1) on projected income by regime (default s.202; opt-out recorded yearly); declarations and proofs in the portal [VERIFY: Form 12BB successor]; quarterly statement Form 138 prepared for upload; **Form 130** (Parts A–C) issued by **15 June** after the tax year once TRACES has processed the statements; Form 16 only for FY 2025-26.
- **Outputs:** Form V wage slip on or before pay day (r.52); Forms I, IV and IX electronic registers kept 5 years (r.51); EPF ECR and ESI (by the 15th of the next month), PT and LWF where applicable and labour returns (r.48) as validated files with a filing checklist and acknowledgement capture; authorised staff file; no portal credentials or OTPs stored. Payroll journals and accruals go to the employer's books with the audit trail on (Companies (Accounts) Rules r.3(1) proviso).

### OH10.7 POSH Internal Committee

- **Committees** per office with 10 or more employees (s.4): presiding officer a senior woman employee, at least 2 employee members, 1 external member, at least half women, term up to 3 years [VERIFY]; composition validated on change; smaller offices use the District Local Committee (s.6), whose details OH10 shows employees.
- **Case states:** `RECEIVED (within 3 months, extendable by 3, s.9) → CONCILIATION (complainant's request; no monetary settlement, s.10) | INQUIRY → INTERIM_RELIEF (s.12) → INQUIRY_COMPLETED (90 days, s.11(4)) → REPORT_ISSUED (10 days, s.13) → EMPLOYER_ACTION (60 days, s.13(4)) → APPEAL_WINDOW (90 days, s.18) → CLOSED`; escalation to the presiding officer at day 80 of inquiry.
- **Confidentiality** (s.16): separately keyed store visible only to that office's IC and, for implementing orders, the HR head; never in dashboards, AI tools or exports. Annual IC report to the employer and District Officer (s.21) and Board's-report counts (Accounts Rules r.8(5)(x)) generated from counts only; failure-to-constitute alerts (s.26).

### OH10.8 Appraisal, calibration and rewards

```
GOALS_SET → MID_CYCLE_CHECK_IN → SELF_REVIEW → MANAGER_REVIEW → SKIP_LEVEL_REVIEW → CALIBRATION
  → HR_APPROVED → COMMUNICATED → (APPEAL → DECIDED) → CLOSED
```

- **Goals:** OKRs or goals per cycle with outcome measures (OH10.5) or agreed qualitative criteria; **optional 360** with rater consent; fewer than 3 raters suppressed.
- **Calibration:** one session per function, facilitated by HR with a second HR checker; inputs are proposed ratings with evidence, distribution against guidance (no forced curve [REC]) and aggregated bias checks by gender, location and tenure shown only for cells of 5 or more; every change records a reason and returns to the manager for acknowledgement; minutes are stored and ratings lock at `HR_APPROVED`.
- **Maker-checker:** manager proposes; skip-level and HR check; increments and bonuses come from a rating-by-budget matrix within budget and are approved under the DoA (OH11); nobody rates or approves their own increment; an adverse rating within 12 months of a protected disclosure needs the OH11.5 second review; AI may summarise but never proposes or decides ratings, pay or termination.
- **Employee rights:** sees rating and reasons, records disagreement, appeals to HR within 15 days [REC]. Training records (security, POSH, code of conduct, data protection) also serve as OH14 evidence.
- **Retention:** per OH12.5; POSH files 8 years after closure [REC]; background reports 1 year, then summary only (DPDP s.8(7)) [REC].

### OH10.9 Events

- **Produced (`oh` scope):** `EmployeeOnboarded`, `EmployeeOffboarded`; with OH12 `MailboxProvisioned`; with OH11 `AccessReviewCompleted` (`review_scope = OH`). They reach only OH modules and the group's own LawDocsComply `LDC_GROUP` tenant, never a product or client tenant (Integration Spec 6.23); payloads never carry PAN, Aadhaar, date of birth, bank account, salary, leave reason or health data. The earlier name `EmployeeProvisioned` is not used.
- **Consumed:** IdP sign-in events (OH12); aggregated outcome metrics (OH4–OH7, engineering systems); rule-pack releases; DoA decisions (OH11). External files: bank payout, EPF, ESI, State and TRACES uploads by authorised staff.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Rule-pack version and State tables | Employing entity, office | Latest signed pack; State per office | Regulatory floor |
| Pay cycle, input cut-off, pay day | Employing entity | Monthly; 20th [REC]; last working day | Commercial within the CoW limit |
| Variance thresholds | Employing entity | ±10% per head; any bank change | May be tightened |
| Bank-change hold | Platform | 48 hours | Floor |
| Leave policy | Employing entity | OSHWC s.32 floor plus group types | Floor; more generous allowed |
| Work week and holiday calendar | Office | Monday–Friday; State list | Drives every working-day timer |
| Probation | Employing entity | 6 months, one extension of up to 3 [REC] | Commercial within MSO |
| Overtime | Office | Off; on only with recorded consent | Floor: 2×, 144 hours a quarter, State limits |
| Attendance sources | Office | IdP sign-in plus timesheet | Prohibited-monitoring list has no setting |
| WFH policy and monitoring notice | Employing entity | Per Appendix B decision 7 | Commercial; notice is a floor |
| Appraisal cycle, rating scale, 360 | Employing entity | Annual; five-point; 360 off | Commercial |
| Minimum cell size for analytics | Platform | 5 | Floor |
| Retention schedule | Record class | OH10.8 | Floor where statutory |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `People › Directory` | Employee list (entity, office, worker type, status); record tabs with RESTRICTED field masking | HR; managers (own team, no salary) |
| `People › Hiring` | Requisitions with DoA status; offer builder with CoW tags and minimum-wage check; approvals | HR maker, HR head, DoA approvers |
| `People › Onboarding` | Pre-boarding checklist, notices and consents, appointment letter, OH12 provisioning status | HR, IT checker |
| `People › Leave` | Requests queue, team calendar, balances, encashment, policy editor; bulk approve for managers | Employees, managers, HR |
| `People › Attendance and WFH` | Daily view, regularisation queue, timesheets, overtime consent with the quarter-to-date 144-hour meter, monitoring notice acknowledgements | Employees, managers, HR |
| `People › Payroll` | Run board by state; input upload with validation report; variance queue; approval; two-person bank-file release; statutory files (ECR, ESI, PT, LWF, Form 138 data); payslips; off-cycle runs | Payroll maker; HR head or CFO; finance releaser |
| `People › Appraisal` | Cycle set-up, goals, reviews, calibration grid with suppressed cells, letters, appeals | Employees, managers, HR |
| `People › Exits` | Exit wizard showing the final-wage, gratuity and service-certificate deadlines; access-off status; receivables | HR, payroll, IT |
| `People › POSH` (restricted) | Committees, cases, timelines, annual report counts | Internal Committee; HR head for orders |
| Self-service | Payslips, Form 130, leave, attendance, declarations and proofs, own data requests | Employees |

Keyboard shortcuts on the variance and regularisation queues; error states name the blocking rule (for example `below_minimum_wage` with the State table version) and never release a partial bank file.

### Acceptance tests

- A rule pack with a broken signature is refused and payroll cannot calculate. Total remuneration ₹76,000 with ₹40,000 excluded allowances and ₹20,000 basic plus DA yields CoW wages of ₹22,000 (shared golden fixture with GV6).
- An offer cannot issue without CoW tags on every component, a WFH clause and probation terms; an offer below the Rajasthan minimum wage for the role is blocked.
- Last working day Friday 4 Dec 2026 in Noida (weekend non-working, no notified holiday) sets the final-wage deadline to Tuesday 8 Dec 2026; a notified holiday on Monday 7 Dec moves it to Wednesday 9 Dec; the run is not held for clearance; deducting unserved notice pay fails with `not_permitted_deduction_s18`.
- A fixed-term employee leaving after 14 months with last monthly wages ₹40,000 receives gratuity of ₹23,077 (1 completed year).
- Overtime that would take a Noida employee to 145 hours in the quarter or above 11 hours in a day is blocked; overtime without recorded consent is blocked.
- A run cannot reach `VARIANCE_REVIEWED` while any variance lacks a reason; a payroll preparer cannot approve a run containing their own pay line; a bank change within 48 hours of a run is held out of the bank file.
- No API, setting or flag enables screenshots, keystroke or webcam capture; a crafted request returns `prohibited_monitoring`.
- A POSH case is invisible to HR operations and every dashboard; a calibration cell with fewer than 5 employees is suppressed; a calibration change without a reason cannot be saved.
- `EmployeeOnboarded` is never delivered to a product or client-tenant endpoint (routing test).

---
## OH11. Internal controls, anti-fraud and staff ROI

**Purpose.** A working internal-control system for the group's own money, people and systems: a delegation-of-authority (DoA) matrix that lets decisions be taken close to the work and escalates automatically above limits; maker-checker on payments, payroll, vendor master, credit notes and discounts; a segregation-of-duties (SoD) matrix enforced at role grant; fraud and error analytics; periodic access reviews; a whistle-blower channel; and staff ROI metrics used to manage teams, not to watch individuals. Controls reduce fraud and error; they do not eliminate them, and no policy, sales or product text may say otherwise.

**Users.** All employees (requests and approvals within limits); DoA approvers; finance controller (P2P, O2C and payroll controls); CFO; HR head; CISO (access reviews); internal audit; Audit Committee chair or Board-nominated director (vigil mechanism); entity heads; statutory auditor (read-only, OH14).

**Requirement codes.** `CA13` s.134(5)(e), s.143(3)(i) (with the private-company IFC-reporting exemption of 13 Jun 2017 [VERIFY thresholds]), s.177(9)–(10) with Companies (Meetings of Board and its Powers) Rules 2014 r.7; Companies (Accounts) Rules r.3(1) proviso; `ICAI` Guidance Note on Audit of Internal Financial Controls over Financial Reporting; CYB paras 21(2), 21(3), 21(6), 113–114 (applied as vendor obligations through RE contracts, OUT para 34); `LC` Model Standing Orders 2026 (false reimbursement claims and unauthorised IT access are misconduct); `DPDP` ss.7(i), 8(5); `ISO` 27001:2022 Annex A 5.3, 5.15–5.18, 8.2; `SOC2` CC1.3, CC5, CC6.1–CC6.3.

**Data owned.** Each group company owns its control records; alerts and investigation files are `RESTRICTED` to internal audit; whistle-blower identities sit in a separately keyed store; no product tenant data is used.

### OH11.1 Delegation of authority and decentralised decisions

- **Rule table:** `doa_rule(entity, decision_type, min_amount, max_amount, approver_role, second_approver_role, conditions, valid_from, valid_to, policy_version)`, approved by the Board or its delegate; every decision stores the rule version applied.
- **Default limits [REC; Board to approve]:**

| Decision | Team lead | Function head | CFO | Above CFO |
|---|---|---|---|---|
| Operating expense or purchase order | Up to ₹25,000 | Up to ₹2 lakh | Up to ₹10 lakh | Two directors |
| Customer discount (OH8) | — | Sales head up to 10% | Up to 20% | CEO; non-standard terms CEO plus legal |
| Credit note or write-off | Billing lead with reason, up to ₹25,000 | — | Up to ₹2 lakh | CEO up to ₹10 lakh; Board above |
| Refund (OH8) | Billing lead plus finance checker, up to ₹25,000 | — | Up to ₹2 lakh | CEO up to ₹10 lakh; two directors above |
| Headcount (OH10) | — | Within approved plan | Outside plan | CEO for senior hires |

- **Always two persons:** vendor payment release (finance maker and checker; a director as well above ₹10 lakh) and payroll release (OH10.6).
- **Request states:** `SUBMITTED → IN_APPROVAL (level n) → APPROVED | REJECTED (reason) | RETURNED (more information) → EXECUTED`; `WITHDRAWN` before approval; an approval lapses if not executed within 30 days [REC].
- **Decentralised rights:** a decision within a holder's limit is final; above it the request routes up the reporting line automatically; every decision carries a reason code; time-to-decide SLA of 2 working days [REC] with automatic escalation; leave delegation only to a named person of equal or higher level, time-bound and logged.
- **Guards:** related requests by one requester to one counterparty within 30 days are summed for routing [REC]; an approver with a declared interest in the counterparty is skipped.

### OH11.2 Maker-checker and SoD

| Action | Maker | Checker and extra control |
|---|---|---|
| Vendor payment and bank file | Finance executive | Finance controller; bank-file hash compared at upload; payees only from the verified master |
| Payroll run | Payroll | HR head or CFO approves; finance releases; no self-approval of own pay line |
| Vendor master create or change | Procurement | Finance controller; bank change by call-back and 48-hour hold |
| Employee bank change | Employee in portal | Payroll; 48-hour hold; notice to old and new contact channels |
| Credit note, discount, refund, write-off | Billing or sales | Per DoA; linked to the original invoice |
| Price book, stream gate, entitlement override (OH8) | Revenue operations | Pricing committee |
| Journal above ₹1 lakh or to revenue, payroll or bank accounts | Accountant | Finance controller |
| Privileged or finance role grant | Requester's manager | System owner and CISO; SoD check |

| Role A | Conflicting role B | Risk |
|---|---|---|
| Vendor master maintenance | Payment release | Fictitious vendor |
| Employee master edit | Payroll approval | Ghost employee |
| Bank-detail change | Payment or payroll release | Diversion |
| User administration | Any finance, payroll or billing transacting role | Self-granted access |
| Invoicing and credit notes | Cash application and write-off | Lapping |
| Requisition | Receipt of the same order above ₹25,000 | Paying for undelivered work |
| Developer with merge rights | Production deploy approval of the same change | Unreviewed change (OH13) |
| Razorpay admin | Refund approval | Refund diversion |

- Conflicts are blocked at role grant in the Hub and checked across Microsoft 365 or Google, GitHub, AWS, Razorpay, the accounting system and bank portals through access-review connectors; an exception needs a director, a compensating control and an expiry of at most 90 days; a monthly SoD scan reports any conflict in any system.

### OH11.3 Fraud and error analytics

All tests raise **alerts for human review**; none suspends pay, blocks a person or starts discipline automatically.

| Test | When | Logic |
|---|---|---|
| Ghost employee | Monthly before payroll approval | Pay with no IdP sign-in for 30 days outside approved leave; no appointment letter or manager; duplicate PAN or UAN; pay after exit; missing UAN where EPF applies |
| Duplicate bank account | Each change, monthly | Same (hashed) account across two employees, an employee and a vendor, or a vendor and a refund destination |
| Vendor integrity | On creation, monthly | PAN and GSTIN validity; penny-drop name match below 85%; address, phone or email matching an employee; reactivation after 12 months' dormancy; first payment within 7 days of creation |
| Duplicate invoice | Each invoice | Same vendor, amount and date; near-identical numbers; same document hash |
| Expenses | Each claim, monthly | Receipt OCR and hash; duplicates; split claims just under a limit within 7 days; weekend or holiday claims without travel; mileage above route distance; round sums; claims during leave |
| Payments | Daily | Payment to an account changed within 48 hours; out-of-hours releases; repeated payments just below an approval limit |
| Revenue (OH8) | Monthly | Credit notes just after period end; discounts above DoA; refunds to a different source attempted; unexplained write-offs |
| Distribution tests | Quarterly | First-digit (Benford) and outlier tests on payments and expenses [REC] |

- **Cases:** `ALERT → TRIAGE (5 working days) → DISMISSED (reason) | INVESTIGATION → FINDINGS → MANAGEMENT_ACTION → CLOSED`; natural justice (written allegation, opportunity to respond, decision by someone not involved in the investigation) under the applicable standing orders or contract; evidence hashed; quarterly aggregate report to the Audit Committee or Board. Analytics use only the finance, HR and access data needed (DPDP s.7(i)); never personal social-media or off-duty data.

### OH11.4 Access reviews and vendor controls

- **Scope and routing:** Hub roles, suite admin roles and licences (OH12), GitHub, AWS, Razorpay, accounting, bank portals, Brevo and social accounts (`review_scope = OH`); Infrabyx staff support and break-glass access into Finbyx or Udofin production, logged and visible to tenants (`review_scope = PLATFORM`, also to OH13). Tenants' own reviews (`TENANT`) never reach the Hub.
- **Cadence:** privileged quarterly; others half-yearly; movers and leavers within 1 working day [REC]. **Flow:** `GENERATED → IN_REVIEW → ATTESTED → REMEDIATED → CLOSED`; items not attested within 14 days are revoked after one reminder; no self-attestation; accounts unused for 45 days (privileged 30) disabled [REC]. Each completed review emits `AccessReviewCompleted` with evidence to OH14.
- **Vendors:** KYC (PAN, GSTIN, penny-drop, address); sanctions and adverse-media screening above ₹10 lakh annual spend [REC]; requester's conflict declaration; contract and DPA where personal data is processed; security due diligence for any vendor touching group or product data (feeds the OH14 sub-processor register and products' OUT para 82 inventories); annual review of material vendors; monthly GSTIN status checks; three-way match above ₹25,000; TDS (ITA25 s.393) and GST reverse charge applied by the accounting connector.

### OH11.5 Whistle-blower and vigil mechanism

- **Applicability:** mandatory under s.177(9) only for group companies that are listed, accept public deposits or have borrowed more than ₹50 crore from banks and public financial institutions (r.7); adopted voluntarily by every group company [REC], overseen by the Audit Committee or a Board-nominated director.
- **Channel:** web form with an anonymous option and a case key; dedicated mailbox and postal address reaching only the vigilance officer and the chair or nominated director; direct access to the chair in appropriate or exceptional cases (s.177(10)); disclosures about the vigilance officer or a director go to the chair only.
- **States:** `RECEIVED → TRIAGED → INVESTIGATING → FINDINGS → ACTION → CLOSED`; acknowledgement within 3 working days and updates every 30 days [REC]; repeated frivolous complaints may be reprimanded with reasons (r.7).
- **Protection:** a 12-month anti-retaliation flag requires a second review by the HR head and the chair of any adverse action against the whistle-blower; identity disclosed only with consent or by law. Sexual-harassment matters go to the Internal Committee (OH10.7) with consent; customer complaints to OH6; vulnerabilities to OH13's disclosure process. Quarterly aggregate report to the Audit Committee or Board.

### OH11.6 Staff ROI metrics (team level)

| Metric | Formula and source |
|---|---|
| Revenue per FTE | Trailing-12-month revenue ÷ average FTE, by entity and function (OH8, OH10) |
| Billable utilisation | Billable hours ÷ available hours, services teams (timesheets) |
| Cost per ticket; SLA attainment; first-contact resolution | Support cost ÷ tickets resolved; OH6 |
| Implementation cycle time and margin | Signature to go-live; implementation revenue less cost (OH4, OH8) |
| Delivery performance | Deployment frequency, change failure rate, time to restore (OH13) |
| CAC payback and NRR | OH8.10 |

- **Use rules:** dashboards show teams and functions; individual figures only to the employee, the line manager and HR in appraisal; no leaderboards; never the sole basis for discipline, pay or termination; derived from outcomes in systems of record, never from surveillance data (OH10.5); group dashboards (OH2) suppress cells under 5 people; quarterly management review records resourcing decisions under the DoA.

### OH11.7 Events

- **Produced:** `AccessReviewCompleted` (`review_scope` OH or PLATFORM); `ControlEvidenceCollected` per control run (DoA conformity, SoD scan, analytics, access review); `ComplianceIssueRaised` for failures a company's compliance function must track.
- **Consumed:** OH8 billing events, OH10 payroll and employee master, OH12 sign-in and directory data, OH13 change records, bank and accounting data, GitHub, AWS and Razorpay entitlement exports.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| DoA rules and limits | Entity | OH11.1 table [REC] | Board-approved; changes by maker-checker with a new policy version |
| Decision SLA and escalation | Entity | 2 working days | Commercial; may be shortened |
| Related-request aggregation window | Platform | 30 days | May be lengthened |
| SoD matrix | Platform | OH11.2 table | Floor; additions allowed, removals need the CFO and CISO |
| SoD exception | Grant | Director approval, compensating control, ≤ 90 days | Floor |
| Analytics thresholds | Test | OH11.3 values | Internal audit sets; tightening free, loosening needs the Audit Committee |
| Dormancy disable | Platform | 45 days; privileged 30 | May be shortened |
| Access-review cadence and attestation window | Platform | Quarterly privileged, half-yearly others; 14 days | Floor |
| Whistle-blower acknowledgement and updates | Entity | 3 working days; every 30 days | May be shortened |
| Anti-retaliation flag | Platform | 12 months | Floor |
| ROI visibility and minimum cell | Platform | Team level; 5 | Floor |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Controls › DoA` | Rule table by entity and decision type with version history; simulator ("who approves ₹3 lakh capex in entity X?"); delegations with expiry | Finance controller (maker), CFO or Board delegate (checker); all staff read their own limits |
| `Controls › Maker-checker queue` | My approvals across modules with amount, rule applied, SLA clock and evidence; approve, reject, return with reasons; bulk approve only within limit and for one decision type; delegation banner | All approvers |
| `Controls › Access reviews` | Campaigns by system and scope; reviewer worklists; attest or revoke; exceptions; SoD scan results and exceptions register | CISO, system owners, reviewers; internal audit (read) |
| `Controls › Whistle-blower` | Restricted case list, timeline, actions, anti-retaliation flags, quarterly aggregates | Vigilance officer, chair or nominated director only |
| `Controls › Analytics` | Alerts by test, triage queue, cases, quarterly report | Internal audit |
| `Controls › Vendors` | Vendor master, KYC and screening status, bank-change call-back log, annual reviews | Procurement, finance controller |

Each approval shows why it reached the approver (rule, amount band, aggregation); saved filters and keyboard approve or reject, always with a reason.

### Acceptance tests

- A ₹3 lakh purchase order approved by a function head routes to the CFO; an unanswered request escalates after 2 working days.
- Two ₹20,000 requests to one vendor by one requester within 10 days route as ₹40,000.
- Granting payment release to a vendor-master maintainer is refused; a director exception without expiry cannot be saved.
- A vendor whose hashed bank account matches an employee's raises an alert before the first payment.
- A payroll line for an employee with no sign-in for 30 days and no approved leave appears in the ghost-employee report without blocking the run.
- Three ₹9,900 claims within 7 days against a ₹10,000 limit raise a split-claim alert.
- A privileged item not attested within 14 days is revoked and the review emits `AccessReviewCompleted` with the correct `review_scope`; a `TENANT` review is never accepted by the Hub.
- An anonymous whistle-blower can follow the case with the key; an adverse rating within 12 months needs the second review before it takes effect.
- No dashboard shows an individual's metrics beyond the employee, line manager and HR; a group cell with 4 people is suppressed; text saying "eliminates fraud" fails the claims gate.

---
## OH12. Workplace integration and document management (Microsoft 365, Google Workspace)

**Purpose.** Connect the Hub to the group's office suite so identities, email IDs, mailboxes, licences, Teams and SharePoint (or Google groups and shared drives) follow the HR lifecycle automatically; give the Hub and group apps single sign-on; keep group documents in a governed taxonomy with retention and legal hold; and provide migration tooling and runbooks for staff and clients. One `WorkplaceProvider` interface (shared with Finbyx GV7) supports both suites.

**Owner decision (Appendix B decision 1).** The owner referred to "Microsoft 365 Business Starter". Microsoft's plans for up to 300 users are **Business Basic, Standard and Premium**; "Business Starter" is a **Google Workspace** edition. The decision record captures, per group domain: suite and edition held, seats, Microsoft 365 Default Geography, whether Advanced Data Residency (ADR) is bought, target suite and migration plan. Until recorded, both adapters stay available under the guard-rails below.

**Users.** IT administrators (makers); IT head or CISO (checkers); HR (lifecycle triggers); employees; records manager; DPO; migration engineers (OH4); client IT administrators (own tenants, within a project).

**Requirement codes.** `DPDP` (ss.8(5), 8(7); Rules r.8(3)); `CERTIN`; CF para 14(4) and OUT para 74(vi) (India storage for RE data, applied by contract to group systems); `CA13` ss.118, 128 and Companies (Accounts) Rules r.3; `GST` (CGST Act s.36); `LC` (Wages (Central) Rules r.51); CYB para 116 (teleworking, adopted as group policy); `ISO` 27001:2022 Annex A 5.12–5.14, 5.33, 8.10–8.13; `SOC2` CC6, C1.

**Data owned.** Each group company owns its mailboxes, files and records; the Hub stores configuration, provisioning state, delta tokens, subscriptions and record metadata, not content.

### OH12.1 Residency guard-rails

"Regulated data" means personal data (other than the directory attributes needed to run an account), HR records, books of account and vouchers, tax and statutory returns, and any client loan, borrower, member or RE customer data. "Non-regulated data" means `PUBLIC`, `INTERNAL` and `CONFIDENTIAL` material containing none of these (for example approved policies, proposals, brochures and product documentation).

| Suite | Residency [VEND] | Allowed data | Override |
|---|---|---|---|
| Microsoft 365 Business Basic, Standard or Premium, Default Geography India (or ADR with India as a Local Region covering all eligible seats) | Exchange, SharePoint, OneDrive and Teams chats at rest in India | All group data classes, `RESTRICTED` HR and legal records with DPO approval per site; client regulated data only in OH4-controlled project sites on the client's written instruction, after the residency attestation | Narrowing only |
| Microsoft 365, other geography | Outside India | Non-regulated data only | **None**: regulated and `RESTRICTED` data blocked, including with DPO risk acceptance |
| Google Workspace (all editions; Business Starter has no data regions; others offer US or Europe only) | Not India | **Non-regulated data only**: no personal data, books of account, returns, loan or HR data; HR data stays in the Hub or India-resident Microsoft 365 | **None** |

- Default Geography is proved by an admin-centre data-location export signed by the IT head and re-attested yearly [VERIFY: a Graph property for it].
- The Hub's document service checks the data class and target on every write and refuses with `residency-blocked`; suite DLP policies (where licensed) block PAN, Aadhaar, account-number, loan-number and salary patterns in Google Workspace and outside-India Microsoft 365 [REC]; migration files travel only through the OH4 secure transfer, never by email.
- For a domain whose mail runs on Google Workspace, the Hub writes only the directory attributes an account needs (name, work email, department, title); staff policy and DLP keep regulated data out of mail and Drive; Appendix B decision 1 records whether to consolidate on India-resident Microsoft 365.
- Group companies' books of account stay in the accounting system with daily backup on servers in India (Accounts Rules r.3(5)); suite copies are convenience copies and only in India-resident Microsoft 365.

### OH12.2 Identity and single sign-on

- **IdP:** Entra ID (Microsoft 365 tenants) or Google Cloud Identity for the Hub and group internal apps via OIDC (SAML only where needed); one enterprise application per app with recorded admin consent; product tenants keep their own IdP choices (GV7.2).
- **MFA** for every Hub user; phishing-resistant methods (FIDO2 or platform authenticators) for administrators, finance, payroll and engineering production roles [REC]; the IdP's MFA claim is trusted only with a conditional-access attestation, otherwise the Hub adds its own factor.
- **Conditional access** where licensed (Business Premium or Entra ID P1 [VERIFY]; Google context-aware access): compliant devices for admin roles; legacy authentication blocked; sessions 12 hours, admins 4 hours [REC]. Remote access only through the IdP with MFA and device registration.
- **Break-glass:** two cloud-only emergency accounts per tenant with hardware keys in a safe, excluded from conditional access, alerting on every sign-in, tested quarterly.
- **SCIM 2.0** from the IdP to group apps; groups map to app roles, never directly to privileged roles (OH11 maker-checker applies).

### OH12.3 Joiner, mover, leaver and email IDs

- **Email IDs:** `first.last@[entity-domain]`; on collision the middle initial, then a digit; transliteration rules for non-ASCII names; reserved names blocked (`admin`, `grievance`, `dpo`, `security`, `legal`, `billing`, `support`, `hr`, `ceo`, `cfo` and others); role mailboxes (`grievance@`, `dpo@`, `security@`, `billing@`, `support@`, `careers@`) as shared mailboxes or groups with named owners; an address is quarantined for 90 days after exit and **never reissued to another person**; aliases only with IT checker approval.
- **Microsoft 365 joiner (Graph) [VEND; VERIFY permissions]:** `POST /users` with `accountEnabled=false` until D-1 and `usageLocation=IN`; `POST /users/{id}/assignLicense` (`addLicenses[{skuId, disabledPlans}]`; least privilege `LicenseAssignment.ReadWrite.All`; usageLocation first [VERIFY]); group, Teams and SharePoint membership through groups; mailbox created with the licence and set to India Standard Time; enable on D-1 with a temporary access pass for MFA registration; emit `MailboxProvisioned` (`oh` scope). Every step idempotent on `(employee_id, provider, action)`; a failed step retries with back-off and then opens an IT task without leaving a half-provisioned account enabled.
- **Google joiner (Admin SDK Directory API):** `users.insert` into the entity's OU with `suspended=true` until D-1; licence through the License Manager API [VERIFY]; `members.insert` into groups; shared-drive membership; 2-step verification enforced. Domain-wide delegation only with the minimal scopes approved by the Super Admin (changes take up to 24 hours).
- **Mover:** attributes, groups and licences recalculated from the role template on the move date; access no longer needed removed immediately; OH11 SoD check.
- **Leaver** (18:00 on the last working day; immediately on dismissal): block sign-in; `revokeSignInSessions`; reset password and remove MFA methods; remove groups; convert the mailbox to shared or forward to the manager for 90 days with an auto-reply; OneDrive access to the manager for the retention period [VERIFY default]; retention or legal hold applied before licence removal; Google: suspend, Data Transfer API for Drive and Calendar, delete per policy; corporate data wiped from managed devices. Completion is OH11 access evidence.
- **Licence pool:** seats by SKU, cost, assigned and available, renewal date; alert at 90% use; reclaim from leavers after the hold and idle seats after 30 days with manager confirmation; monthly cost allocation to cost centres.

### OH12.4 Collaboration structure

- Teams and channels (or Google groups and Chat spaces) per department and programme; private channels for HR, finance and legal (Microsoft 365 India only); naming `[entity]-[function]-[topic]`. SharePoint sites (or shared drives) per function, libraries mapped to the taxonomy, named owners, external sharing **off** by default.
- **Client delivery spaces** (OH4): one per project; guests only for named client contacts with 90-day expiry; no client regulated data unless OH12.1 allows; archived with retention at project close.
- **Group shared operations** with Equator, LawDocsComply and others: shared channels or B2B guest access only, purpose-bound and time-limited (OH1 cross-company roles); Equator case spaces are never shared with lender-side delivery teams (Integration Spec Part 8.6).

### OH12.5 Document taxonomy and retention

| Record series | System of record | Retention [REC unless cited] |
|---|---|---|
| Board and general meeting minutes and resolutions | Secretarial system; signed copies in the suite | Permanent (CA13 s.118; SS-1, SS-2) |
| Books of account and vouchers | Accounting system | 8 years from financial-year end (CA13 s.128(5)) |
| GST invoices, notes, returns | OH8 and accounting | At least 72 months from the annual-return due date (CGST Act s.36) [VERIFY] |
| Income-tax records | Accounting | Per ITA25 reassessment periods, minimum 8 years [VERIFY] |
| Wage, attendance and payslip records | OH10 | 5 years after the last entry (r.51) |
| Personnel files | OH10 | Employment plus 8 years |
| Customer and vendor contracts | OH3 and contract repository | Term plus 8 years |
| Support and grievance records | OH6 | 8 years after closure |
| Marketing consents | OH3 | Life of consent plus 3 years |
| Security and access logs | Log platform | 180 days in India minimum (CERT-In); 1 year (DPDP Rules r.8(3)) |
| Engineering and control evidence | OH13, OH14 | 8 years; audit period plus 7 years |

- Labels PUBLIC, INTERNAL, CONFIDENTIAL and RESTRICTED applied as sensitivity labels where the licence supports them (Purview [VERIFY per plan]) or as metadata and permissions otherwise; retention via Purview retention policies or Google Vault [VERIFY edition], or, where the edition lacks them, the Hub records service holds the schedule and produces disposition lists.
- **Legal hold** set in the Hub by legal applies to custodians' mailboxes and drives and suspends disposition everywhere; reviewed quarterly. **Disposition** requires records-manager approval and produces destruction certificates.

### OH12.6 Change notifications and synchronisation

- **Graph:** delta queries (`/users/delta`, `/groups/delta`, `/drives/{id}/root/delta`) with stored `deltaLink`, and change-notification subscriptions renewed at 80% of lifetime (users and groups about 23 days; driveItem about 24 days; mail about 5.5 days; Teams about 2.4 days); lifecycle notifications (`reauthorizationRequired`, `subscriptionRemoved`, `missed`) trigger re-authorisation or delta resync; the endpoint checks `clientState`, echoes the validation token within Microsoft's limit [VERIFY: 10 seconds] and queues work; Teams protected APIs only after Microsoft approval.
- **Google:** Directory push channels or reports polling, Drive `changes.watch` and Calendar `events.watch` renewed before expiry; weekly full reconciliation.
- **Drift:** nightly comparison of IdP users and groups with OH10 employees and role templates; an orphan account raises an OH11 alert within 24 hours.

### OH12.7 Migration tooling for staff and clients

- **Tools [VEND; VERIFY scope and edition limits]:** Microsoft Migration Manager (file shares, Google Drive, Box, Dropbox and others into SharePoint and OneDrive); Exchange Online migration batches from Google Workspace (mail, calendar, contacts); Google Workspace Migrate or the Data Migration Service into Google Workspace (non-regulated data only).
- **Runbook:** `DISCOVERY (users, mailboxes, sizes, shared drives, permissions, third-party apps, data classes) → PLAN (batches, DNS and MX, rollback) → PILOT (5–10 users) → BATCHES → CUT_OVER (MX switch, delta pass) → HYPERCARE (2 weeks) → DECOMMISSION (old tenant read-only for the retention period)`; validation by item counts per mailbox and library, checksums on a file sample, permission-mapping report, failed-item log resolved before cut-over, and user sign-off; a failed pilot returns to `PLAN`.
- **Client migrations** are OH4 projects under an SOW, run in the client's tenant with client-granted, time-bound, least-privilege access (Microsoft granular delegated admin privileges or a client-created account with expiry [VERIFY]); Infrabyx keeps no client admin credentials after the engagement and evidences revocation at close; regulated data moves only to destinations allowed by OH12.1 and the client's policy.

### OH12.8 Events

- **Produced (`oh` scope):** `MailboxProvisioned`; `ControlEvidenceCollected` for MFA coverage, conditional-access exports, sign-in risk, admin-role and licence reports, and leaver completion.
- **Consumed:** `EmployeeOnboarded`, `EmployeeOffboarded` and mover events (OH10); legal-hold instructions; OH4 migration milestones.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Suite, tenant and edition per domain | Entity | Owner decision record | Commercial; required before phase O11 closes |
| Residency attestation | Tenant | Required before any regulated class; yearly | Regulatory floor |
| Data classes per target | Tenant, site | Derived from OH12.1 | Floor: may narrow, never widen; no override for Google or outside-India Microsoft 365 |
| Naming rules, reserved names, quarantine | Platform | OH12.3; 90 days; no reissue | Floor for quarantine and no reissue |
| Leaver cut-off and mailbox forward | Platform | 18:00 on the last working day; 90 days | Floor for access-off time |
| Guest expiry and external sharing | Site | 90 days; sharing off | May be tightened |
| Session lifetime | Role | 12 hours; admins 4 hours [REC] | May be tightened |
| Subscription renewal margin | Platform | 80% of lifetime | Technical |
| Licence alert and idle reclaim | Entity | 90% use; 30 days idle | Commercial |
| Retention schedule and legal-hold owners | Record series | OH12.5 | Floor where statutory |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Workplace › Mailboxes` | Users and mailboxes by entity with provisioning state per step; joiner, mover and leaver runs with retry; role mailboxes and owners; quarantined addresses; licence pool with cost and reclaim queue | IT administrators (maker), IT head (checker) |
| `Workplace › Groups` | Groups, Teams and Chat spaces with owners, role-template mapping, guests and expiry; SCIM mapping; orphan and drift alerts | IT administrators |
| `Workplace › Sites` | Sites and shared drives with data class, residency status, sharing policy and labels; legal holds; disposition lists for approval | IT, records manager, legal, DPO |
| `Workplace › Migration` | Projects by runbook state, batch dashboard (counts, checksums, failures), cut-over checklist, client-access grants with expiry and revocation evidence | Migration engineers, OH4 project managers |
| `Workplace › Residency` | Attestations, Default Geography evidence, blocked-write log | IT head, DPO |

A blocked write explains the rule and offers the permitted destination ("HR data cannot be stored in Google Workspace; save it in the Hub records service").

### Acceptance tests

- A joiner sharing a name with a current employee receives `first.m.last@` and never a quarantined or previously used address; `dpo@` cannot be assigned as a personal address.
- Replaying the Graph joiner flow creates no second user, licence or membership; no licence assignment is attempted before `usageLocation` is set.
- At 18:00 on the last working day sessions are revoked, sign-in blocked, the mailbox converted with a 90-day forward, and the licence removed only after the hold is confirmed.
- Any write of personal, HR, books, returns or loan data to Google Workspace is refused with `residency-blocked`, also when a DPO risk acceptance is attached; a `RESTRICTED` file to a Microsoft 365 tenant outside India is refused; a PAN-like pattern in a Google space is blocked by DLP.
- A Graph subscription at 80% of lifetime is renewed; a `missed` notification triggers a delta resync that captures changes made during the gap.
- An IdP account with no active OH10 employee raises an orphan alert within 24 hours.
- A legal hold on a custodian removes their items from the next disposition list.
- A client migration project cannot close until client-granted admin access is revoked with evidence; phase O11 cannot be marked done without the office-suite decision record.

---
## OH13. Engineering-operations console (releases, changes, patches, VAPT, backups)

**Purpose.** One console in which the group sees and governs engineering operations across every repository and product: release calendar and freeze windows, change requests and the Change Advisory Board (CAB), emergency changes, vulnerability tracking and patch SLAs, VAPT engagements, backup and restore-test evidence, the incident register with regulatory clocks, and the status page. Products keep their engineering practice in their own repositories (Finbyx Part 7L EO1–EO4; Udofin Part 7H RA4); OH13 aggregates their events and evidence, runs the group CAB and applies the same controls to the Hub's own repository. It is an operations console, **not** a super-admin console: it has no access to tenant data, production databases or customer records.

**Users.** CTO and engineering leads; CISO and security engineers; SRE; CAB members (engineering lead, CISO or delegate, product owner, QA lead, SRE, compliance reviewer for regulated changes, customer success); product compliance officers; incident commanders; auditors (read-only, OH14).

**Requirement codes.** CYB paras 105–106, 112, 121–126, 129–131, 133, 140–141 and Chapter IV paras 28, 39, 41–42 (applied to products as vendor obligations to RE tenants); OUT paras 34, 61 (incidents reported to the NBFC so that it can report to RBI within six hours of the service provider's detection), 74(ii), 77, 79, 83; CF para 16; `CERTIN` (Directions of 28 Apr 2022 under IT Act s.70B(6): specified incidents within 6 hours, point of contact, logs 180 days in India, NTP synchronisation); `DPDP` (breach intimation; Rules 2025 detailed report within 72 hours, from 13 May 2027 [VERIFY]); `SOC2` CC7–CC8, A1; `ISO` 27001:2022 Annex A 5.24–5.28, 8.8, 8.13, 8.25–8.32.

**Data owned.** Infrabyx owns repository metadata, change records, releases, vulnerabilities, VAPT reports, backup and drill evidence and incident records. Evidence naming a tenant is shared only with that tenant; incident records hold affected tenants and data classes as counts, never customer records.

### OH13.1 Repository register and release calendar

- **Register:** every group repository (Finbyx `finbyx`, `finbyx-infra`, `finbyx-escrow`; Udofin apps and services; Operations Hub; Equator; LawDocsComply; LawDocs; shared `infrabyx-contracts`, rule-pack and design-system repositories) with owner team, product, criticality (critical to RE tenants or not), GitHub plan, ruleset baseline, CODEOWNERS coverage, required checks, environments and the latest nightly ruleset-drift export (EO1.2 pattern).
- **Calendar:** release trains per product (weekly plus hotfix lane [REC]); planned versions and change ids; regulatory-impact flag and tenant-notice date (5 working days ahead for regulatory-impact releases; EO1.6); Integration Specification contract versions, with a release that bumps an event or API major version blocked until consumers' compatibility tests pass.
- **Freeze windows** (per product): Finbyx close and returns (last 2 and first 3 working days), quarter-end and FY-end, CIC submission days (9th, 16th, 23rd and the month-end file by the 5th); Udofin store-review periods and festival peaks; Equator hearing peaks. A release in a freeze needs an emergency change or a recorded CAB exception.
- **`ReleasePublished`** from each product (version, change ids, SBOM hash, signature digest, release-notes ref, regulatory-impact flag) is consumed; a production deployment without a matching event within 1 hour raises an exception.

### OH13.2 Change requests, CAB and emergency changes

- **Classes** (EO2.1 applied group-wide): `STANDARD` (pre-approved catalogue, logged), `NORMAL` (CAB), `REGULATED` (CAB plus a compliance reviewer and a golden-case pass: rule packs, calculations, formats, contact policy, audit trail, security controls, residency, billing entitlements, the Labour Code rule pack), `EMERGENCY`.
- **Record:** class, risk score (impact × likelihood, tenants affected, data migration, reversibility), linked pull requests, expand-migrate-contract plan, rollback or forward fix, test evidence, tenant communication, window, approvers, post-implementation review.
- **States:** `DRAFT → SUBMITTED → ASSESSED → CAB_REVIEW → APPROVED | REJECTED | DEFERRED → SCHEDULED → IMPLEMENTED → PIR_DONE → CLOSED`; `FAILED → ROLLED_BACK | FORWARD_FIXED → PIR_DONE`; a change not implemented within its window returns to `CAB_REVIEW`.
- **CAB** weekly with quorum 4 including security; minutes in OH13. **`ChangeApproved`** carries change_id, class (`STANDARD`, `NORMAL`, `REGULATED`, `EMERGENCY`), approvers, window, risk rating and, for `EMERGENCY`, the retrospective-review due date; idempotent on (change_id, approval_version); consumed by product deployment gates and OH14, and by the tenant's compliance destination for tenant-impacting `REGULATED` changes; a production deployment without a matching approval is refused. DORA-style metrics (deployment frequency, lead time, change failure rate, time to restore) feed OH11.6.
- **Emergency** (Sev-1 or actively exploited vulnerability): two of CTO, CISO and on-call engineering lead approve in the GitHub environment and the change record; signed tag and required checks still apply except tests waived with reasons; retrospective CAB within 2 working days, otherwise an OH14 exception.

### OH13.3 Vulnerability tracker and patch SLAs

- **Feeds:** GitHub Dependabot, code-scanning (CodeQL) and secret-scanning alerts via the REST API (`/repos/{owner}/{repo}/dependabot/alerts`, `/code-scanning/alerts`, `/secret-scanning/alerts`, or organisation endpoints) [VEND; VERIFY availability for private repositories on Team without the Secret Protection and Code Security products]; open-source scanners where those are not bought (Semgrep, gitleaks or trufflehog, osv-scanner); container, IaC and cloud-posture scans; CERT-In and vendor advisories; VAPT findings; reports through `security.txt` (RFC 9116).
- **Normalisation:** one record per (CVE or rule, component, version, repository, environment); severity from CVSS adjusted for EPSS, CISA KEV, reachability, exposure and data at risk; triage within 24 hours for critical.
- **SLA policy** from triage. Platform findings (product code and infrastructure of every group repository, including the Hub, whoever reports them, including a tenant-commissioned VAPT) follow Finbyx EO1.6; internal and tenant audit findings that are not platform defects (process, policy or configuration findings in group operations) follow the AU4.3 defaults. A stricter tenant contract or product policy wins; no setting relaxes the platform floor.

| Severity | Platform SLA (EO1.6; all group repositories) | Internal and tenant audit findings (AU4.3 defaults) |
|---|---|---|
| Critical (CVSS 9.0–10.0), CISA KEV-listed or actively exploited | 72 hours (emergency lane) | 15 days |
| High (7.0–8.9) | 7 days | 30 days |
| Medium (4.0–6.9) | 30 days | 90 days |
| Low (0.1–3.9) | 90 days | 180 days |

- A leaked secret is revoked and rotated within 24 hours whatever its severity [REC]. Closure needs a fix, regression test, verification scan and recurrence check across supported release lines (CYB paras 125–126); exceptions need a CISO risk acceptance with a compensating control and an expiry of at most 90 days. An end-of-support register tracks languages, frameworks, databases and images. SLA attainment is reported monthly to the CTO and CISO and quarterly to the board; product metrics go into tenant evidence packs.

### OH13.4 VAPT engagements

- **Testers:** independent, CERT-In-empanelled firm (empanelment checked against CERT-In's published list at engagement and recorded with evidence), not involved in building the system (CYB para 122); rotated at least every 3 years [REC]; NDA, rules of engagement and DPA signed; production testing or documented deviations (CYB para 124).
- **Cadence** (floor for every product serving REs; CYB para 121): vulnerability assessment at least every 6 months and penetration test at least every 12 months on internet- and customer-facing systems; before go-live of a new product or major version; after major change; mobile apps to OWASP MASVS (RA4.3); cloud configuration review yearly.
- **States:** `PLANNED → SCOPED → CONTRACTED → TESTING → REPORTED → REMEDIATION → RETEST → CLOSED`; findings flow into OH13.3 with source `VAPT`; reports and retests hashed.
- **Sharing:** executive summaries to each RE tenant per cycle and full reports under NDA on request; pooled audits supported (OUT para 77); CYB para 106 certificates per material release and para 105 escrow receipts tracked per product; a staleness exception 30 days before any VA or PT for a product with RE tenants would exceed 6 or 12 months.

### OH13.5 Backup and restore-test evidence

- **Expected-evidence matrix** per product and asset: backup type and frequency; daily automated restore sample and quarterly full restore; half-yearly DR drill with a full working day on DR for products serving Chapter V tenants (CYB paras 129–131); yearly ransomware recovery test; customer-held backup rehydration where offered (Finbyx DP4).
- **Ingestion:** `BackupCompleted` and `RestoreTested` from all products and the Hub (`oh` scope), plus drill reports with RTO and RPO achieved and data reconciliation (for Finbyx: trial balance, loan counts and audit hash chain equal to source).
- **Alarms:** no expected backup event for 26 hours, a failed restore test or a missed quarterly restore raises a Sev-2 problem record and an OH14 exception.
- **Group systems** in the same matrix: Hub database, suite data (third-party backup if bought [REC]), accounting system (daily backup on servers in India; Accounts Rules r.3(5)), GitHub mirrors.

### OH13.6 Incident register and regulatory clocks

```
DETECTED (t0) → TRIAGED (≤ 30 min for Sev-1) → CONTAINED → ERADICATED → RECOVERED → RCA_DONE → CLOSED
clocks from t0:
  affected RE tenants (SecurityIncidentNotified)  ≤ 2 h   so each RE can report to RBI within 6 h of provider detection (OUT para 61; CYB para 141)
  CERT-In (specified incidents)                   ≤ 6 h   (CERT-In Directions, 28 Apr 2022)
  DPDP Board (personal data breach)               without delay; detailed report ≤ 72 h (from 13 May 2027 [VERIFY])
  data principals                                 without delay, through the RE where the RE is fiduciary
  RE updates                                      every 4 h for Sev-1 until contained [REC]; by update_seq
  final RCA to affected REs                       ≤ 10 working days [REC]
```

- **Record:** detection source and time, CERT-In category, severity, affected products, tenants and data classes (counts), commander, timeline, decisions, notifications with timestamps and recipients, hashed evidence, RCA and actions.
- **Roles:** the RE, never Infrabyx, reports to RBI; each group company reports its own incidents to CERT-In and keeps its point of contact current; forensic support to REs (CYB para 140). NTP to NIC or NPL servers with drift alarms; security logs 180 days in India and 1 year overall; half-yearly tabletop drills per product with simulated RE notification, missed clocks recorded as exceptions.

### OH13.7 Status page

- Components per product and region (web app, APIs, borrower portal or app, integrations, upstream dependencies) with states operational, degraded, partial outage, major outage and maintenance; public page without tenant names or personal data, plus tenant-specific notices inside each product; hosted apart from production (different account, preferably provider).
- First update within 30 minutes of a Sev-1 declaration, then at least hourly [REC]; post-incident summary within 5 working days; maintenance announced 5 working days ahead for regulated changes, 2 for others; monthly availability from synthetic checks feeds OH8 service credits.

### OH13.8 Events

| Event | Producer → consumer(s) |
|---|---|
| `ReleasePublished` | Products and Hub → OH13, OH14; tenant compliance destination (regulatory-impact notes) |
| `ChangeApproved` | OH13 CAB record → product deployment gates, OH14; tenant compliance destination for tenant-impacting `REGULATED` changes |
| `BackupCompleted`, `RestoreTested` | Products and Hub → OH13, OH14 |
| `SecurityIncidentNotified` | Products (as service providers) → RE systems; copy to OH13 |
| `AccessReviewCompleted` (`review_scope = PLATFORM`) | Products → OH13, OH14 |
| `ConnectorCertified` | Certification service → OH13 (connector register) |
| `ControlEvidenceCollected` | OH13 → OH14 |
| `ComplianceIssueRaised` | OH13 → LawDocsComply or the product's compliance destination (missed clocks, stale VAPT, failed restores) |

External: GitHub REST and webhooks (audit-log streaming on Enterprise Cloud), cloud backup and posture APIs, the CERT-In empanelment list (manual check with evidence), the status-page provider.

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Platform patch SLAs | Platform, all group repositories | EO1.6: 72 hours, 7, 30 and 90 days | Regulatory and contractual floor; may be tightened per product or tenant contract, never relaxed |
| Audit-finding remediation defaults | Entity | AU4.3: 15, 30, 90 and 180 days | Floor; stricter tenant policy wins |
| Risk-acceptance expiry | Platform | ≤ 90 days, CISO approval | Floor |
| Release trains and freeze windows | Product | Weekly plus hotfix; OH13.1 windows | Commercial; freeze dates for returns and CIC days are floors |
| Tenant notice for regulatory-impact releases | Product | 5 working days | Floor |
| CAB cadence and quorum | Platform | Weekly; 4 including security | May be tightened |
| VAPT cadence and tester rotation | Product | VA 6 months, PT 12 months; rotation 3 years [REC] | Floor for products serving REs |
| Backup alarm | Asset | 26 hours | May be tightened |
| Incident clock targets | Platform | OH13.6 | Floor |
| Status-page update cadence | Platform | 30 minutes, then hourly | May be tightened |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Engineering › Releases` | Calendar by product with trains, freezes and tenant-notice dates; release detail (change ids, SBOM, signature, notes); deployment-without-release exceptions; repository register with ruleset drift | Engineering leads, SRE, product owners |
| `Engineering › Changes` | Change list by state and class; change form with risk score and rollback plan; CAB agenda, votes and minutes; emergency approvals; PIR queue | Change requesters, CAB members, compliance reviewer |
| `Engineering › Vulnerabilities` | Board by severity and SLA clock (red, amber, green) per repository and product; triage workbench; risk acceptances with expiry; secret-leak rotation tasks; end-of-support register | Security engineers, CISO, repository owners |
| `Engineering › VAPT` | Engagements by state; tester empanelment evidence; findings and retests; staleness alerts; tenant summary packs | CISO, security engineers |
| `Engineering › Backups` | Evidence matrix by product and asset; restore and DR drill results with RTO and RPO; alarms and problem records | SRE |
| `Engineering › Incidents` | Incident console with live clocks, notification log, timeline and RCA; drill register | Incident commanders, CISO, product compliance officers |
| `Engineering › Status page` | Component states, scheduled maintenance, update composer with templates, publication log | SRE, incident commanders |

Clocks turn amber at 50% and red at 90% of target; every red item names its owner and next action.

### Acceptance tests

- A Finbyx release scheduled on the 16th is blocked unless raised as an emergency change or a recorded CAB exception.
- A `REGULATED` change without a compliance reviewer or a golden-case pass cannot reach `APPROVED`; `ChangeApproved` is emitted once per approval version with its approvers and class.
- A critical Dependabot alert gets a 72-hour due time on the Hub, Udofin and Finbyx repositories alike; a high finding gets 7 days on every group repository; an internal-audit process finding rated high gets 30 days; a setting that relaxes a platform SLA cannot be saved.
- A leaked token opens a 24-hour rotation task that cannot close without rotation evidence.
- A VAPT engagement whose firm lacks current CERT-In empanelment evidence cannot reach `CONTRACTED`; a PT aged 11 months for a product with RE tenants raises a staleness exception.
- No `BackupCompleted` for 26 hours raises a Sev-2 problem record; a failed quarterly restore appears as an OH14 exception.
- An incident drill records t0, RE notice, CERT-In and DPDP clock times; an RE notice at 2 hours 10 minutes is flagged as missed.
- The public status page shows no tenant names and stays reachable when the production account is down; OH13 roles cannot query any tenant database (permission test).

---
## OH14. Certification readiness and control library

**Purpose.** Hold the group's **common control framework** (one control library mapped many-to-many to every scheme and rule set the group is assessed against), automate evidence collection from the products and the Hub, manage audit periods (SOC 2 Type 1 then Type 2, ISO cycles, PCI SAQ A, tenant and RE-driven audits), keep the policy register, run the auditor portal and gate every external certification claim. Certification is a **programme, never a claim**: until a report or certificate is issued, the group says "aligned to" or "in progress" (Finbyx EO5.1; Udofin RA4.4). Policies are drafted later; OH14 fixes the framework and evidence they will reference.

**Users.** Head of GRC or CISO (library owner); control owners; evidence collectors; internal audit; management review (CEO, CTO, CISO, CFO, DPO); external auditors (licensed CPA firm for SOC 2 and SOC 1; accredited certification body for ISO); tenant auditors (via product packs); marketing and sales (claims gate).

**Requirement codes.** `PCI` (PCI DSS v4.0.1; SAQ A revised 31 Jan 2025); `SOC2` (AICPA 2017 Trust Services Criteria with revised points of focus 2022; SSAE 18 [VERIFY]); `ISO` (ISO/IEC 27001:2022 with Amd 1:2024; ISO/IEC 27701:2025 stand-alone PIMS, published 14 Oct 2025; ISO 22301:2019; ISO/IEC 42001:2023; ISO/IEC 27017:2015 and ISO/IEC 27018 [VERIFY current editions]); CYB Chapters III–V, OUT paras 34, 47, 61, 74, 76–82, 87–88, 97, CF paras 13–16 (as vendor clauses); `CERTIN`; `DPDP` Act 2023 and Rules 2025; `CA13` ss.134(5)(e), 143(3)(i) and Companies (Accounts) Rules r.3(1) proviso with the ICAI Rule 11(g) implementation guide; SOC 1 Type 2 (SSAE 18 or ISAE 3402) for tenants' statutory auditors (EO4.2).

**Data owned.** Infrabyx owns the library, mappings, evidence, audit records and certification registry. Evidence naming a tenant is visible only to that tenant (through its product pack) and to auditors under NDA within scope.

### OH14.1 Frameworks and scope

| Framework | Group target [REC; owner decides order, CPA firm and certification body] | Scope note |
|---|---|---|
| PCI DSS v4.0.1 SAQ A | Annual self-assessment per selling entity from the first paid invoice | Razorpay-hosted or redirect pages and Payment Links only (OH8.7); no card data in group systems |
| SOC 2 (TSC 2017, rev. 2022) | Type 1 around month 9; first Type 2 window 6 months, then 12-month windows | Security (CC1–CC9) plus Availability, Confidentiality, Processing Integrity; Privacy optional; per product system description |
| SOC 1 Type 2 | After SOC 2 Type 1, Finbyx first | Controls relevant to tenants' financial reporting |
| ISO/IEC 27001:2022 + Amd 1:2024 | Certificate around months 9–12 | ISMS for products in India regions, engineering, support, operations, offices |
| ISO/IEC 27701:2025 | After 27001 | PIMS mapped to DPDP |
| ISO 22301:2019 | Year 2 | Business continuity (CYB para 127 best practice) |
| ISO/IEC 42001:2023 | Decision gate | Only if AI (Finbyx M20, EO6; Udofin RA5) becomes material |
| ISO/IEC 27017 and 27018 | With 27001 surveillance | Cloud controls; PII in public cloud |
| RBI vendor clauses, CERT-In, DPDP, Companies Act IFC and audit trail | Continuous | Tenant contracts and evidence packs; every group company |

Scope statements per scheme and product list systems, locations, people, processes, subservice organisations (AWS, Razorpay, Microsoft or Google, GitHub, messaging providers, Brevo) and exclusions with reasons; changes go through OH13.

### OH14.2 Control library

| Entity | Key fields |
|---|---|
| `control` | id (for example `CCF-AC-03`), objective, type (preventive, detective, corrective), nature (automated, manual, IT-dependent manual), owner, operator, frequency, systems and products in scope, test procedure, evidence requirement, automation hook, status (`DESIGNED`, `IMPLEMENTED`, `OPERATING`, `EXCEPTION`, `RETIRED`) |
| `requirement` | framework, version, reference (for example ISO 27001 A.8.32, SOC 2 CC8.1, CYB para 121, OUT para 61, CERT-In direction (ii), DPDP s.8(5)), summary |
| `control_requirement_map` | control, requirement, coverage (full or partial), rationale |
| `evidence` | control, period, collector, artefact URI, sha256, captured_at, reviewer, status (`ACCEPTED`, `REJECTED`, `NEEDS_INFO`) |
| `test_result`, `exception` | tester, sample, exceptions, conclusion; compensating control, risk acceptance, expiry |
| `soa_entry`, `cuec`, `csoc` | ISO Statement of Applicability; complementary user-entity and subservice-organisation controls per system description |
| `policy`, `audit_period`, `certification` | OH14.5, OH14.4, OH14.6 |

- Every control maps to at least one requirement and has an owner and either an automated collector or a documented manual procedure; requirements with no control appear on the gap report.
- **Control states:** `DESIGNED → IMPLEMENTED` (owner, mapping, collector or procedure, linked approved policy) `→ OPERATING` (evidence accepted for one full frequency period) `→ EXCEPTION` (failed test or stale evidence; remediation task with due date) `→ OPERATING` (retest passed) `| RETIRED` (mapping moved, with reason).
- **Initial library** [REC]: about 150–200 controls across 15 domains, seeded from the Finbyx EO5.3 mapping list and the Udofin RA4.4 additions.

### OH14.3 Evidence automation

| Collector | Source | Frequency |
|---|---|---|
| Ruleset and branch-protection export with drift diff | GitHub (OH13.1) | Nightly |
| CI results, SBOM, signature digests | Pipelines; `ReleasePublished` | Per release |
| Change records and CAB minutes | OH13.2; `ChangeApproved` | Per change; weekly |
| Vulnerability SLA metrics and exceptions; VAPT reports and retests; CYB 106 certificates | OH13.3–OH13.4 | Monthly; per engagement |
| Backup, restore and DR reports | `BackupCompleted`, `RestoreTested`, drill uploads | Daily; quarterly; half-yearly |
| Incident timelines and clock compliance | OH13.6 | Per incident |
| MFA coverage, conditional access, sign-in risk, admin roles | OH12 IdP | Weekly |
| Access reviews, leaver completion, SoD scans, DoA conformity | OH11; `AccessReviewCompleted` (`review_scope` OH or PLATFORM) | Per review; monthly |
| Training completion and policy attestations | OH10.8; `PolicyAttested` | Monthly |
| Vendor due diligence, AoCs, SOC reports, DPAs | OH11.4 vendor register | Annual per vendor |
| KMS policies and rotation; log retention and NTP drift | Cloud and log platforms | Weekly; daily |
| Tenant-isolation tests and audit-trail hash-chain checks | Product suites | Per release; daily |
| Payment-page script inventory and CSP reports | Product and Hub billing pages | Per release; daily |

- Each artefact emits **`ControlEvidenceCollected`** (control_id, period, collector, artefact hash, reviewer, status; idempotent on (control_id, period, artefact_hash)) from the producing product or Hub module; OH14 is the system of record and products keep copies for tenant packs.
- Evidence older than its frequency plus grace is stale, and inside an open audit period raises an exception; artefacts are write-once (sha256), superseded, never edited. **Population exports** for Type 2 sampling (changes, leavers, access reviews, incidents) carry counts and hashes so auditors sample independently.

### OH14.4 Audit-period management

- **SOC 2 Type 1** (point in time) requires a drafted system description, controls `IMPLEMENTED`, no open high gaps in readiness, defined CUECs and CSOCs and a management assertion. **Type 2** covers an observation window (first 6 months, then rolling 12-month windows [REC]; the scheme allows 3–12 months [VERIFY]); control changes inside a window are logged with effective dates; management bridge letters cover gaps between report end and a customer request [REC].
- **States:** `PLANNED → READINESS → AUDITOR_ENGAGED → FIELDWORK | OBSERVATION → DRAFT_REPORT → MANAGEMENT_RESPONSE → ISSUED → DISTRIBUTED (under NDA)`.
- **ISO cycle:** internal audit (clause 9.2) and management review (9.3) before Stage 1; Stage 1, Stage 2, certificate, annual surveillance, recertification in year 3; nonconformities tracked to corrective action with root cause.
- **PCI SAQ A:** annual self-assessment per selling entity; eligibility re-checked whenever a payment page changes.
- **Calendar:** audits, tenant assessments, pooled RE audits (OUT para 77), VAPT cycles and surveillance dates with owners and preparation tasks. Subservice organisations are carved out; their SOC reports or certificates are reviewed yearly and their CUECs mapped to group controls.

### OH14.5 Policy register

- **Register** (drafting later): information security; access control; cryptography and keys; secure SDLC; change and patch; vulnerability management; logging and monitoring; incident response; BCP and DR; backup; retention and disposal; privacy; vendor and sub-processor management; acceptable use; AI use; remote work and monitoring notice (OH10.5); HR and code of conduct; POSH; whistle-blower; anti-fraud; DoA; expenses; records management; external claims.
- **Lifecycle:** `PLACEHOLDER → DRAFT → REVIEW → APPROVED (Board or delegate) → PUBLISHED → ATTESTED → REVIEW_DUE (at least yearly) → SUPERSEDED`; attestations emit `PolicyAttested`. A control linked to a policy that is not `APPROVED` cannot be marked `OPERATING` for an audit period.

### OH14.6 Auditor portal, certification registry and claims gate

- **Auditor portal:** named external users provisioned by maker-checker with MFA, time-boxed to the engagement (at most 90 days, renewable) and scoped to period, scheme and product; request lists with owners and due dates; read-only, watermarked evidence rooms with controlled downloads; sample selection from population exports; Q&A threads; draft findings and management responses. No access to production systems or tenant data; walkthroughs by screen share instead.
- **Provider-assurance room** (Integration Spec Part 4.7): an RE's auditor or supervisor auditing an Infrabyx product receives a `PROVIDER_ASSURANCE` grant to a room served from OH14 (issued SOC and ISO reports, VAPT summaries, BCP and DR evidence, sub-processor list; no tenant data), approved by the owning Infrabyx entity (head and CISO, maker-checker) on the RE's or auditor's written request, 90-day maximum; OH14 emits `ExternalAccessGranted`, `ExternalAccessUsed` and `ExternalAccessRevoked` with `source` `urn:infrabyx:oh:[legalentityid]` and the requesting RE's `reid` (or `none` for Infrabyx's own assurance auditors).
- **Certification registry:** each issued report or certificate with scheme, scope, period or certificate number, issuer, date, validity, approved public statement and permitted marks under the certification and accreditation bodies' rules; lapsed certificates and reports older than 12 months without a bridge letter are marked expired.
- **Claims gate** (`GET /v1/claims-gate/check`, returning PASS or BLOCKED with the registry record or the blocked phrase): one service used by OH7 marketing, OH8 explainers and funnel pages, Finbyx CM2.3 and Udofin RA4.4 product copy, website builds, sales collateral and RFP answer libraries. It blocks "certified", "compliant", "SOC 2", "ISO 27001", "PCI" and similar claims without a matching current registry record and approved wording; any "RBI approved" or "RBI certified" claim; "guarantees compliance" or "eliminates fraud"; and presenting Razorpay's, AWS's or Microsoft's certifications as the group's. Before issue, only "designed to align with" or "readiness programme in progress" is allowed, and "report expected [quarter]" only once an audit period is `AUDITOR_ENGAGED`.

### OH14.7 Readiness dashboard, trust packs and events

- **Dashboard:** controls by status, evidence freshness, exceptions and expiring risk acceptances, gap report per framework, audit calendar and policy dependencies, by product and scheme.
- **Tenant trust pack** (per product and tenant, delivered through Finbyx AU7 or Udofin RA2): current reports or certificates under NDA, VAPT and DR summaries, sub-processor list, current SBOM, escrow receipt where applicable, CYB 106 certificates, incidents affecting that tenant, CUECs the tenant must operate, and the OUT para 97(xvii) coverage table supporting reliance under OUT para 79.
- **Events:** consumes `ControlEvidenceCollected`, `ReleasePublished`, `ChangeApproved`, `BackupCompleted`, `RestoreTested`, `AccessReviewCompleted`, `PolicyAttested`, copies of `SecurityIncidentNotified`, and `ObligationPublished` (new or amended requirements update the gap report); produces `ComplianceIssueRaised` for exceptions and `EvidenceSubmitted` to LawDocsComply where a group company uses its `LDC_GROUP` instance as GRC system (Integration Spec Part 9); OSCAL-compatible export for third-party GRC tools [REC].

### Settings and options

| Setting | Level | Default | Nature |
|---|---|---|---|
| Frameworks, versions and scope statements | Scheme, product | OH14.1 | Change-controlled (OH13) |
| Evidence freshness grace | Control | Frequency plus 10% (minimum 3 days) [REC] | May be tightened |
| Type 2 window | Scheme | 6 months first, then 12 months | Owner decision within the scheme range |
| Auditor access | Engagement | ≤ 90 days; read-only; watermarked downloads | Floor |
| Policy review cycle | Policy | 12 months | Floor; may be shortened |
| Claims lexicon and approved statements | Platform | OH14.6 lists | Regulated configuration (legal and CISO) |
| Registry expiry rule | Platform | Certificate validity; reports 12 months without a bridge letter | Floor |
| Trust-pack contents | Product | OH14.7 list | Tenant-specific evidence only |

### Menu and screens

| Path | Main screens and key actions | Roles |
|---|---|---|
| `Trust › Controls` | Library with filters (framework, domain, owner, status); control detail with mappings, test procedure, collectors and linked policy; gap report; exceptions and risk acceptances with expiry | GRC head, control owners; internal audit |
| `Trust › Evidence` | Evidence feed by control and period with freshness; review queue (accept, reject, needs info); population exports; collector health | Evidence reviewers, control owners |
| `Trust › Audits` | Audit periods by state; request lists; auditor portal administration; provider-assurance grants; certification registry; trust-pack builder | GRC head, CISO; external auditors (portal only) |
| `Trust › Policies` | Register by lifecycle state; review calendar; attestation campaigns and completion; control dependencies | Policy owners, GRC head, all staff (attest) |
| `Trust › Claims gate` | Check text or assets; blocked-phrase log; approved statements | Marketing, sales, legal |

The readiness dashboard opens on what blocks the next audit milestone; no screen shows a certification as held before the registry records it.

### Acceptance tests

- A control without a mapped requirement, owner, or collector or manual procedure cannot reach `IMPLEMENTED`; an unmapped requirement appears on the gap report.
- A nightly ruleset export that differs from the approved baseline raises an exception and emits `ControlEvidenceCollected` with status `EXCEPTION`.
- Quarterly evidence missing after quarter-end plus grace is stale and, inside an open Type 2 window, raises an exception.
- The leaver population export for a Type 2 window matches OH10 exit records in count and hash.
- A control linked to a `DRAFT` policy cannot be `OPERATING` for an audit period.
- An auditor's access ends automatically at grant expiry; the portal has no route to tenant records; a provider-assurance grant emits the three `ExternalAccess*` events with the requesting RE's `reid`.
- "SOC 2 certified" fails the claims gate while no report exists; after a Type 1 report is registered, "SOC 2 Type 1 report available under NDA" passes and "SOC 2 Type 2" still fails; an expired ISO certificate blocks claims relying on it.
- A tenant trust pack for one RE contains no evidence naming another tenant.

---

# PART 6 — INTEGRATION WITH FINBYX, UDOFIN, EQUATOR, LAWDOCSCOMPLY AND THIRD PARTIES

The Infrabyx Ecosystem Integration Specification v1.1 (`docs/ecosystem/infrabyx-integration-spec.md`) is canonical for every cross-product event, API, file layout, identity flow and connector. Where this Part and the specification differ, the specification wins; Claude Code raises the conflict through its proposal process (Integration Spec Part 14.2) and never resolves it locally.

## 6.1 Principles: the Hub consumes tenant-level metadata only

1. **Relationship metadata, never regulated data.** The Hub receives who the client is, what it bought, what it used (aggregates) and the status of implementation, support, releases, incidents, evidence and invoices. It never receives borrower, member, loan, ledger, collateral, collections, recovery, ADR, litigation, borrower-grievance, KYC, bureau, consent-artefact, risk-feed, governance or client-employee records; the client stays fiduciary and Infrabyx is processor only inside the product.
2. **Schema-enforced minimisation:** every OH-bound subject carries `x-dataclass` no higher than `INTERNAL` and a `forbidden_fields` test (loan, account, customer, member, borrower, user or record ids, PAN, Aadhaar, mobile, address, risky free text); gateways reject violations with `dataclass-not-permitted` and the Hub's inbox parks them in the DLQ unstored (Integration Spec Parts 3.9, 4.6, 13.2).
3. **Aggregates for usage and revenue:** `UsageRecorded` per Finbyx CM3.2; Udofin B2C billing stays on Udofin's Razorpay account and the Hub receives only monthly `UsageRecorded` with `meter_kind = REVENUE_AGGREGATE` per plan (subscriber count, gross, GST), never a subscriber key, borrower identity or wellness data (Integration Spec Part 6.27).
4. **Support content stays in the product:** in-product tickets carry a deep link; diagnosis happens inside the product under its break-glass rules (Finbyx M19); intake DLP redacts or rejects PAN, Aadhaar, account, card and mobile patterns.
5. **No regulated decision in the Hub:** no production RE tenant without the signed contract set; no filing for a client; no closing of borrower complaints (OUT paras 54–57; CF para 12); no ODR or neutral selection for an RE (Integration Spec Part 8.6).
6. **Commercial state never interrupts regulated functions** (Finbyx CM1.4; Udofin RV2); dunning ends in a termination notice and the product's exit process, never a hard cancel.
7. **Segregation by legal entity** with the grant model and Equator wall (6.4).
8. **India residency** for production data, backups, logs, DLQs and sub-processors (CERT-In Directions: logs 180 days within India; Companies (Accounts) Rules r.3(5): daily India backup of electronic books); no personal data to a non-India sub-processor without an ADR risk acceptance (Brevo pending hosting confirmation [VERIFY]).
9. **Failure containment:** products keep the last signed catalogue and entitlements for 30 days (Finbyx CM1.5); producers queue in their outboxes; the Hub catches up via `GET /v1/events?after=[cursor]`.
10. **Producer identity:** `source` = `urn:infrabyx:oh:[legalentityid]` (the owning group company's `legal_entity_id`; Integration Spec Parts 3.2 and 4.6); `reid` = the client's or requesting RE's `reid`, or `none`; `productfamily` = `na`; extension attribute names are lowercase alphanumeric without underscores.

## 6.2 Event catalogue used by the Hub

Envelope, delivery, ordering and replay follow Integration Spec Parts 3.2–3.5; "std" is the Specification's standard delivery target (p95 ≤ 5 minutes); **signed** = detached JWS over the CloudEvent plus RFC 9421; idempotency keys apply in addition to `(source, id)`. Rows summarise Integration Spec Parts 6.15, 6.16, 6.21, 6.23 and 6.26–6.29, which prevail.

| Event | Domain | Producer → consumer(s) | Key payload (no personal data unless stated) | Idempotency key | SLA |
|---|---|---|---|---|---|
| `TenantProvisioned` signed | ops | OH4 → Finbyx, Udofin, Equator, LawDocsComply | provisioning_request_id, org_id, product, environment (SANDBOX, UAT, PRODUCTION), deployment model, legal entities, plan and entitlement ref, residency, MSA and DPA refs, OUT clause-matrix ref (PRODUCTION only), first-admin work email with `legalbasis = CONTRACT_PERFORMANCE_VENDOR` | provisioning_request_id | Ack ≤ 1 working day by `PUT /v1/provisioning-requests/{id}`; ready ≤ 1 working day after a complete request |
| `ImplementationMilestoneReached` | ops | OH4 → Finbyx, Udofin (tenant admin view) | project_id, milestone (DISCOVERY, CONFIGURATION, MIGRATION, INTEGRATIONS, TRAINING, GO_LIVE), acceptance evidence ref, migration record counts and reconciliation result | (project_id, milestone) | std |
| `SupportTicketOpened` | ops | OH6 → originating product (Finbyx, Udofin) | ticket_id, tenantid, product, category, severity, SLA clock | ticket_id | Per support SLA |
| `SupportTicketResolved` | ops | OH6 → originating product | ticket_id, resolution code, resolved_at, satisfaction request | (ticket_id, resolution_seq) | std |
| `ReleasePublished` | ops | Finbyx, Udofin, Equator, LawDocsComply, OH → OH13, OH14; tenant compliance destination for regulatory-impact notes | version, change ids, SBOM hash, signature digest, release-notes ref, regulatory-impact flag | (product, version) | ≤ 1 h |
| `ChangeApproved` | ops | OH13 (CAB record) → product deployment gates (Finbyx, Udofin, Equator, LawDocsComply), OH14; tenant compliance destination for tenant-impacting REGULATED changes | change_id, class (STANDARD, NORMAL, REGULATED, EMERGENCY; REGULATED needs a compliance reviewer and a golden-case pass), approvers, window, risk rating, retrospective-review due date (EMERGENCY) | (change_id, approval_version) | Before deployment; a production deployment without a matching approval is refused |
| `ControlEvidenceCollected` | ops | Finbyx, Udofin, OH collectors → OH14 | control_id, period, collector, artefact hash, reviewer, status | (control_id, period, artefact_hash) | ≤ 1 h |
| `BackupCompleted` | portability | Finbyx, Udofin (status), OH own platform (`oh` scope) → OH13 | archive_id, type (incl. PLATFORM), bytes, manifest hash, target_id | (target_id, archive_id) | Daily by 06:00 IST |
| `RestoreTested` | portability | Finbyx, Udofin, OH (`oh` scope) → OH13 (status), OH14 (evidence) | test_id, type (INTEGRITY, READABILITY, REHYDRATION, DR_DRILL), archive_id, result, discrepancy count, approver role | test_id | ≤ 1 working day |
| `PlanChanged` | billing | OH8 → Finbyx, Udofin | tenantid, legal entity scope, plan, SKU, effective_at, proration ref, catalogue version | (tenantid, plan_change_id) | std |
| `EntitlementChanged` signed | billing | OH8 → Finbyx, Udofin | SKU, modules, limits, start, end, contract ref; JWS by the pinned Hub key | (tenantid, entitlement_id, version) | std |
| `UsageRecorded` | billing | Finbyx, Udofin → OH8 | tenantid, legal entity, meter, period, quantity, `meter_kind` (USAGE; REVENUE_AGGREGATE for Udofin borrower-plan revenue, no subscriber key), statement hash (`usage_aggregate_v1`) | (tenantid, meter, period, statement_version) | Monthly by WD+3; daily provisional totals |
| `InvoiceIssued` signed | billing | OH8 → Finbyx, Udofin billing pages | invoice_no, supplier and recipient GSTINs, place of supply, SAC [VERIFY], taxable value, GST, IRN and QR where applicable, due date, document ref | invoice_no | std |
| `SubscriptionPaymentReceived` signed | billing | OH8 → Finbyx, Udofin | invoice or subscription ref, amount, method class, Razorpay payment id, captured_at | razorpay_payment_id | ≤ 15 min of capture |
| `SubscriptionPaymentFailed` | billing | OH8 → Finbyx, Udofin | ref, reason class, retry schedule, dunning stage | (ref, attempt) | ≤ 15 min |
| `SubscriptionCancelled` | billing | OH8 → Finbyx, Udofin | subscription_id, effective_at, reason, exit path (Finbyx DP5; Udofin UP5) | subscription_id | std |
| `ModuleAttached`, `ModuleDetached` | platform | Product entitlement service → OH8 (modules as applied), LawDocsComply | as Integration Spec 6.16 | as 6.16 | On publication |
| `ExportRequested`, `ExportCompleted` | portability | Finbyx, Udofin → OH4 exit cases, OH13 (status and counts only) | job_id, scope type (DATASET, LEGAL_ENTITY, MODULE, AUDIT_PACK, RE_PACK, FULL_TENANT, EXIT), data classes, destination type; archive_id, archive standard version, folder profile, file count, bytes, manifest hash; never content | job_id; archive_id | std |
| `ExternalAccessGranted`, `ExternalAccessUsed`, `ExternalAccessRevoked` | audit | OH14 (`oh` scope, `PROVIDER_ASSURANCE` grants only) → requesting RE's register, OH14 evidence; Finbyx, Udofin, LawDocsComply → OH (counts only) | as Integration Spec 6.21 | as 6.21 | as 6.21 |
| `ProfessionalEmpanelled` | directory | OH9 → Finbyx R11 (Recovery Suite), Udolex | professional_id, BCI Rule 36 fields only, courts, languages, `equator_neutral` flag | (professional_id, version) | std |
| `ProfessionalSuspended` | directory | OH9 → Finbyx R11, Udolex | professional_id, reason class, effective_at | (professional_id, suspension_seq) | ≤ 1 h; public listing removed at once; R11 blocks new allocations |
| `MatterAllocated` | directory | Finbyx R11, Udolex → OH9; group legal tools (`oh` scope) → OH9 | allocation_id, professional_id, reid, matter class, forum type and State, basis (ROTATION, RULE, REASONED_EXCEPTION), allocated_at, status (OFFERED, ACCEPTED, DECLINED_CONFLICT, DECLINED_CAPACITY, WITHDRAWN), `update_seq`; never party names, matter or case numbers, loan identifiers or amounts | (allocation_id, update_seq) | std; a status change is an update with a higher `update_seq` |
| `SecurityIncidentNotified` | grc | Any provider (Finbyx, Udofin, Equator, LawDocsComply, OH) → affected RE systems, LawDocsComply; copy to OH13 for clocks | incident_id, detected_at, class, data classes affected, status, update_seq | (incident_id, update_seq) | ≤ 2 h to REs (OUT para 61); CERT-In within 6 h |
| `EmployeeOnboarded` (`oh` scope) | workforce | OH10 → OH modules, Infrabyx LDC_GROUP tenant | employee_ref (pseudonymous), legal entity, department, position, worker type, start date | (employee_ref, lifecycle_seq) | std |
| `EmployeeOffboarded` (`oh` scope) | workforce | OH10 → OH modules, Infrabyx LDC_GROUP tenant; identities removed from products by SCIM | employee_ref, last working day, access_off_at, final-wage timer start | (employee_ref, lifecycle_seq) | Access off the same day (18:00 on the LWD) |
| `MailboxProvisioned` (`oh` scope) | workforce | OH12 → OH modules | provider (M365, GOOGLE, ONPREM), mailbox alias ref, licence SKU, residency attestation ref, action (CREATE, SUSPEND, RETAIN, DELETE) | (employee_ref, provider, action) | std |
| `AccessReviewCompleted` | workforce | OH1 and OH11 (`review_scope = OH`) → OH14; Finbyx, Udofin (`review_scope = PLATFORM`: Infrabyx staff access to production) → OH13, OH14 | review_id, review_scope, system, period, population count, exceptions, revocations, reviewer roles, evidence hash | review_id | ≤ 1 working day |
| `ConnectorCertified` | platform | Certification service → OH13 | as Integration Spec 6.16 | as 6.16 | Before production |
| `ControlTestResultPublished`, `EvidenceSubmitted`, `PolicyAttested`, `ComplianceIssueRaised` | grc | OH14 → LawDocsComply (Infrabyx's own LDC_GROUP tenant) | as Integration Spec 6.15 | as 6.15 | ≤ 1 h |
| `ReturnDue`, `ReturnFiled`, `PeriodClosed` (status projection) | reporting, finance | Finbyx → OH, only where the tenant opts in | return code, period, due date, status; no amounts or hashes | as Integration Spec 6.18, 6.20 | std |

**Workforce scope rule.** In the `oh` scope the four workforce events describe Infrabyx group staff and are produced only by the Hub. Tenant-scope events from Finbyx GV6 and GV7 (`review_scope = TENANT` for access reviews) describe a client's employees, stay inside that tenant and **never reach the Hub**; an OH subscription to them is refused at registration and at the gateway, and the Hub's filter also rejects any workforce event whose `source` is not `urn:infrabyx:oh:[legalentityid]` (Integration Spec Part 6.23). `AccessReviewCompleted` from a product reaches the Hub only with `review_scope = PLATFORM`.

**Never consumed:** the origination, servicing, payments, collateral, co-lending, collections, recovery, ADR, litigation, DLG, grievance, documents, privacy, bureau, audit findings, risk, governance, member-lending, investments, partner-deal and insurance domains; reporting and finance events other than the opt-in status projection above (never `InterestCertificateIssued`); tenant-scope workforce events; Udofin wellness data (no events exist).

**Superseded names** (Integration Spec Part 6.17): `EmployeeProvisioned` maps to `EmployeeOnboarded` plus `MailboxProvisioned`; billing-domain `PaymentReceived` and `PaymentFailed` are `SubscriptionPaymentReceived` and `SubscriptionPaymentFailed`, and consumers key on the full CloudEvents `type`.

## 6.3 Third-party adapters

Each adapter implements the connector SPI (Integration Spec Part 10.1), ships a mapping pack, is mock-first, then sandbox, and passes certification (Part 14.3) before it touches real data. Credentials live in the India secrets manager and rotate at least every 90 days. **The project owner procures accounts and live credentials; Claude Code builds adapters, contract tests and mocks.**

| Adapter | Provider(s) and Hub use | Pattern and current facts | Guard-rails |
|---|---|---|---|
| `CrmMarketingProvider` | Brevo: campaigns, list sync, marketing events (OH3, OH7) | `/v3/` REST, API key or OAuth 2.0; contacts about 10 requests per second and 36,000 per hour, transactional email 1,000 per second; 429 → back-off with jitter; webhooks; nightly full export as exit path [VERIFY: CRM paths, export job, hosting, DLT support] | Hub is the system of record; Infrabyx B2B contacts only; send gate before every push |
| `PaymentGateway` (vendor billing only) | Razorpay hosted checkout, Payment Links, Subscriptions (card, UPI AutoPay), eNACH, Smart Collect: group fees (OH8) | `X-Razorpay-Signature` = HMAC-SHA256 of the raw body; de-duplicate on `x-razorpay-event-id`; out-of-order events; old secret valid for retries after rotation; server-side checkout verification; daily settlement reconciliation | Redirect only, no Razorpay script on our pages (PCI DSS v4.0.1 SAQ A); never Route, pooled tools or loan money (CF paras 10(1)–(3)); PA authorisation and AoC filed yearly [VERIFY]; E-mandate Directions 2026 paras 6, 8(a), 10(a) |
| `WorkplaceProvider` (M365) | Microsoft Graph, Microsoft 365 Business Basic, Standard, Premium or Enterprise: staff lifecycle, licences, groups, Teams, SharePoint, OneDrive (OH10, OH12) | `POST /users`; `assignLicense` (`LicenseAssignment.ReadWrite.All`; `usageLocation` IN first [VERIFY]); `revokeSignInSessions`; delta queries; change notifications renewed at 80% of lifetime (users about 23 days, drive 24, mail 5.5, Teams messages 2.4); resync on `reauthorizationRequired` or `missed`; Teams protected APIs need approval; `Sites.Selected` | Default Geography India keeps mail, files and Teams data at rest in India; Advanced Data Residency must cover all eligible seats (owner decision) |
| `WorkplaceProvider` (Google) | Google Workspace Admin SDK, Drive, Calendar | Domain-wide delegation with minimal scopes (up to 24 hours to apply); `users.insert`, OUs, groups; watch channels renewed before expiry | Data regions only US or Europe (none for Business Starter): **non-regulated data only**; no files or records with personal data, books of account, returns, loan, borrower, client or HR data; DLP blocks uploads from the Hub |
| `EngineeringEvidenceSource` | GitHub: ruleset, alert, deployment and membership evidence (OH13, OH14) | Read-only GitHub App; nightly ruleset JSON export with drift detection; alert ages against patch SLAs; private-repository attestations need Enterprise Cloud | No write access; no code or secrets copied |
| `SocialPublisher` | LinkedIn, X, Meta, YouTube: publish approved posts, aggregate metrics (OH7) | Official APIs under developer terms [VERIFY each]; no scraping | Maker-checker and claims gate; commenter data limited to the handle |
| `VoiceProvider`, `MessagingProvider` | JioCX (SMS, RCS, WhatsApp, voice, IVR, OBD, email, Verify), Jio Business SIP and toll-free; Exotel, Ozonetel, Gupshup: Infrabyx support and sales lines | JioCX is sales-led with no public API documentation, rates or residency statement: stub `JioCxAdapter` with certification tests; production only after contract, DPA and India-residency proof [VERIFY] | Promotional voice only on the 140-series via a registered telemarketer with DND scrub and consent (TCCCPR as amended 12 Feb 2025); Infrabyx is not an RE, so 1600-series eligibility is unconfirmed [VERIFY]; DLT template ids for SMS |
| `StatutoryFilingPack` (guided) | EPFO ECR, ESIC, TRACES and the Income-tax portal, State PT and LWF portals, Shram Suvidha (OH10) | Validated files plus checklist: ECR text file [VERIFY specification]; ESIC within 15 days of month end; Form 138 quarterly and Form 130 by 15 June (Income-tax Act 2025 s.392, s.395(4)(b)), Form 16 only for FY 2025-26 [VERIFY: Form 138 utility]; PT and LWF from State tables; acknowledgement capture (TRRN, challan, token numbers) | No portal credentials, DSCs or OTPs stored or scripted; an authorised human files |
| `GstFilingPack` (guided), `EInvoiceProvider` | GST portal via offline-tool JSON or a licensed GSP; e-invoice IRP (OH8 invoices) | GSTR-1 JSON validated, filed on the portal with EVC or DSC; GSP route needs a contract and OTP session [VERIFY]; IRN and QR through the IRP's documented API above ₹5 crore aggregate turnover (Notification 10/2023-CT) [VERIFY route] | IRP API-user credentials are a documented machine channel held in the vault; portal passwords and OTPs never stored; returns never auto-filed |
| `AccountingSink` | TallyPrime (JSON from 7.0 or XML on the local port-9000 listener), Zoho Books API [VERIFY India data centre]: invoices, receipts, revenue schedules, payroll and expense journals | Hashed, signed, idempotent batches; CREATED, ALTERED, ERRORS reconciliation; port 9000 never beyond localhost | Books of record stay in Tally or Zoho; no manual edits of batches |
| `ESignProvider`, `PayoutFileProvider` | LawDocs eSign (group) [VERIFY API] for letters and contracts; banks' bulk-payment files [VERIFY formats] for salary, reimbursements and vendors | Signing evidence and hash stored; payment file only after maker-checker release; return file reconciled | Aadhaar numbers never stored; preparer never releases |

## 6.4 Group SSO and cross-company role federation

- **Identity provider:** one group OIDC layer for Infrabyx staff, federating the directory actually held (Entra ID or Google; Appendix B decision 1), behind the Finbyx OIDC abstraction; MFA for all, phishing-resistant factors for privileged roles [REC]; client users never use it (Integration Spec Part 4.2).
- **Claims** (Integration Spec Part 4.6): pairwise `sub`, `org_id` (employing entity), `entity_scope[]`, `grant_ids[]`, `acr`, `auth_time` (plus `employee_ref` and `amr` inside the Hub); each product audience maps claims to its own roles and never trusts an OH role name as a product permission, so **authorisation stays per product**.
- **Provisioning:** OH10 is the joiner, mover and leaver source; OH12 provisions the office suite; SCIM 2.0 provisions product staff accounts and removes them within 4 hours of `EmployeeOffboarded` (1 hour if privileged), access off by 18:00 on the LWD.
- **Grants:** the `group_grant` of Part 3.3 and OH1.4; cross-entity access denied by default; a cross-entity grant needs the head of the principal's entity, the head of each target entity and the group DPO, lasts ≤ 90 days, and renewal is a fresh approval; grants reach products as SCIM group memberships carrying `valid_to`, and each product ends sessions within 60 seconds of expiry or revocation; each use is logged with the acting entity, which also drives intra-group cost sharing (OH11 cost allocation).
- **Data classes:** Hub classes of Part 5 (`RESTRICTED` covers HR, payroll, POSH, whistle-blower and investigations and maps to Integration Spec `HR`, `SPI` or privileged `LEGAL`); group views aggregate-only; RESTRICTED data crosses entities only under an intra-group DPA (for example Infrabyx running Equator payroll as processor).
- **Equator wall:** Equator roles only inside the Equator entity; no person with a Finbyx or Udofin operator role or lender-side sales role may hold one (SoD at grant); no view joins Equator volumes or outcomes with a lender's revenue, pipeline or collections; no lender-side pay linked to Equator referrals; Equator never marketed as the default ODR (Integration Spec Part 8.6); breach attempts logged for Equator's independent oversight.
- **Break-glass into client data** stays inside each product (Finbyx M19); the Hub records only that a session occurred (ticket, duration, approver).

## 6.5 APIs, reconciliation and failure handling

Direction is caller → server (Integration Spec Parts 6.27 and 6.29 prevail).

| API | Caller → server | Purpose |
|---|---|---|
| `GET /v1/catalogue/versions/{v}` | Finbyx, Udofin, Equator, LawDocsComply → OH8 | Signed catalogue (JWS by the pinned Hub key; Finbyx CM1.1), fetched on `PlanChanged` and daily |
| `POST /v1/billing/quotes` | Finbyx, Udofin billing pages → OH8 | Priced quote and proration preview (IST calendar-day proration, GST, entitlement diff, `valid_until` default 7 days); products compute no price or tax (Idempotency-Key) |
| `POST /v1/billing/orders` | Finbyx, Udofin billing pages → OH8 | Razorpay order, payment link, subscription or mandate from an approved quote or an invoice; returns a Razorpay-hosted URL for top-level redirect (Idempotency-Key) |
| `GET /v1/billing/invoices?tenantid=[id]` | Finbyx, Udofin → OH8 | Invoices, credit notes, statements of account and documents for billing pages |
| `POST /v1/usage-disputes` | Finbyx, Udofin billing pages → OH8 | Dispute within 7 days of statement issue (Finbyx CM3.2); holds invoicing for that meter only; an upheld dispute is answered by a new `UsageRecorded` with a higher `statement_version` |
| `GET /v1/entitlements?tenant=[tenantid]` | OH8 → Finbyx, Udofin | Daily reconciliation of entitlements as applied against those OH8 issued; a mismatch raises `ReconciliationBreakRaised` |
| `PUT /v1/provisioning-requests/{id}` | Finbyx, Udofin, Equator, LawDocsComply → OH4 | Product acknowledges `TenantProvisioned` and reports ACCEPTED, READY (with `tenantid` and tenant-map entry) or FAILED with a reason code |
| `GET /v1/tenants/{tenantid}/provisioning-status` | OH4 → product | Fallback poll when no acknowledgement arrives within 1 working day |
| `POST /v1/support/tickets` | Finbyx, Udofin → OH6 | In-product ticket with product-signed token, deep link and attachments after PII scan (DLP before storage) |
| `POST /v1/crm/requests` | Finbyx, Udofin billing and plan pages → OH3 | "Contact sales" or enterprise-plan request; never borrower, member or loan data |
| `GET /v1/directory/professionals` and `/{id}` | Finbyx R11, Udolex, group legal tools and websites → OH9 | Rule 36 fields and status in randomised order per call (seed logged); no ranking parameter; detail adds credential summary and declared institutional conflicts |
| `POST /v1/conflicts/check` | Equator (machine client only) → OH1 | Neutral conflict screen: allocation count by the counterparty in the window (default `P3Y`), flag and category; counts and flags only (OH1.6) |
| `GET /v1/claims-gate/check` | Products, websites, OH7 → OH14 | PASS or BLOCKED with the certification record or the blocked phrase |

- **Legal basis.** `TenantProvisioned` carries the first-admin work email with `legalbasis = CONTRACT_PERFORMANCE_VENDOR`, the value adopted in Integration Spec Part 3.2 for B2B contact data exchanged under the client's contract with an Infrabyx company; a `TenantProvisioned` without `legalbasis` is rejected.
- **Daily reconciliations (by 06:00 IST):** usage statements versus `UsageRecorded`; Razorpay payments, refunds and settlements versus invoices and bank; product entitlements versus OH8 (`GET /v1/entitlements?tenant=` in each product); provisioning requests versus acknowledged tenants; SCIM users and GitHub members versus OH10 staff. Breaks raise `ReconciliationBreakRaised` and a case.
- **Outages:** a Razorpay outage queues order creation and shows the client a retry notice (never a false success); a Brevo outage pauses campaigns only; Graph or Google outage queues lifecycle steps, except access removal, which escalates to a manual runbook with a 1-hour clock for privileged accounts.

### Acceptance tests

- A `UsageRecorded` payload with a `loan_id` or PAN-like value is rejected to the DLQ with `regulatory-guard`.
- A tenant-scope `EmployeeOnboarded` from Finbyx GV6 is refused; an `oh`-scope event is accepted.
- A forged Razorpay webhook is rejected; a replayed valid one changes nothing; a browser-only "success" leaves the invoice unpaid.
- A ticket containing an Aadhaar-like number is stored redacted and the submitter is told why.
- A cross-entity grant without both entity heads and the DPO cannot be activated, and expires on day 91.
- A user with a Udofin operator role cannot be granted any Equator role.
- With the Hub stopped for 48 hours, Finbyx keeps its entitlements and queues usage; on restart the Hub catches up with no duplicate usage.
- A `MatterAllocated` carrying a matter number or party name, or an `AccessReviewCompleted` with `review_scope = TENANT`, is refused at the gateway with `dataclass-not-permitted`.
- A `TenantProvisioned` without `legalbasis` fails certification; a second acknowledgement for the same `provisioning_request_id` changes nothing.

---

# PART 7 — TECHNOLOGY, ARCHITECTURE AND NON-FUNCTIONAL REQUIREMENTS

## 7.1 Recommended stack

The Hub uses **the Finbyx stack (Finbyx Part 10.1)** so that engineers, packages, contracts and controls are shared; versions are validated in Phase O0 and changed only by ADR. Hub-specific choices:

| Layer | Recommendation |
|---|---|
| Web and backend | pnpm + Turborepo, TypeScript strict; Next.js 16.x (16.4 at drafting) + React 19 with the shared Finbyx design tokens; Node.js 26 LTS [VERIFY: LTS date; Node.js 24 LTS fallback]; **NestJS 11 modular monolith** with module boundaries OH1–OH14; OpenAPI 3.1 via Zod |
| Data | PostgreSQL 16+ on Supabase ap-south-1 (Mumbai) now, Amazon RDS or Aurora later, with **enforced RLS**; Drizzle or Kysely; `NUMERIC` + `decimal.js` (precision ≥ 40) with property tests for pay, proration, GST and revenue schedules |
| Workflows and rules | **Temporal** (India region [VERIFY]) for joiner and leaver sagas, payroll runs, provisioning, dunning, exit cases and Graph and Google subscription renewals, with a payload codec; **GoRules ZEN** or **CEL** by ADR for Hub-only rule packs; the shared **Labour Code rule pack** `infrabyx-labour-rulepack` uses CEL, is signed and pinned in `contracts.lock`, and is shared with Finbyx GV6 (Integration Spec Part 12.3; companion pack `ita25-salary-tds`) |
| Contracts | Outbox and inbox; CloudEvents 1.0.2; JSON Schema 2020-12; **OpenAPI 3.1** and **AsyncAPI 3.0** from `infrabyx-contracts`; Standard Webhooks; RFC 9421; Pact |
| Identity and access | OIDC abstraction over Supabase Auth with federation to Entra ID or Google (6.4); SCIM 2.0; RBAC + ABAC (Cedar or OpenFGA for grants and DoA) **plus RLS** |
| Documents and reporting | S3-compatible storage with SSE-KMS, versioning and Object Lock; docxtemplater → Gotenberg for letters, payslips and invoices; PostgreSQL FTS; governed SQL metric layer with Apache Superset row-level security |
| Observability | OpenTelemetry to an India-hosted stack; no personal data in Sentry; NTP to NIC or NPL sources (CERT-In Directions) |
| Infrastructure | **Development and staging, synthetic data only:** Railway (no India region) + Supabase. **Production, India only:** Supabase ap-south-1 with an India compute host, or AWS ap-south-1 (primary) and ap-south-2 (DR) via OpenTofu or Terraform; KMS; Secrets Manager; WAF |

## 7.2 Architecture principles

Principles 1–17 of Finbyx Part 10.2 apply unchanged. The Hub adds:

18. **Legal-entity scoping in every table.** Business tables carry `legal_entity_id`, client tables `client_org_id`, RESTRICTED tables `sensitivity`; RLS is **forced**, the API uses a non-owner role without `BYPASSRLS`, context is set with `set_config(…, true)` per transaction, and no context returns zero rows. Only reference data (calendars, State tables, rule packs) is unscoped.
19. **Append-only, hash-chained audit trail.** Every material action (approve, export, unmask, grant, payroll or payment-file release, invoice, entitlement or listing change, evidence acceptance) writes an `audit_event` with actor, acting entity, grant, before and after hashes, reason and `prev_hash`; corrections are new events; a nightly verifier anchors the daily head hash in Object Lock storage and OH14.
20. **Maker-checker** for every action in the DoA and SoD tables (OH11): maker never checker, thresholds from the DoA pack, fresh MFA to approve, bulk approval by manifest hash, overrides with reason and second approver.
21. **Rule packs, not code** for Labour Code parameters, State tables, leave, overtime, gratuity, DoA, send gate, dunning, GST and SAC, retention and the claims lexicon: signed, versioned, effective-dated, tested, changed under the regulated change class (Finbyx EO2.1).
22. **India residency** and **tenant-level metadata only** (6.1), proven by CI residency checks and certification tests.
23. **Employee privacy by design.** No keystroke, mouse-activity, screenshot, webcam or off-duty location monitoring; attendance from SSO sign-in and sign-out plus timesheets; self-view and correction; individual metrics only to the employee and manager; AI never decides discipline, termination, pay or hiring (DPDP s.7(i) bounded by purpose limitation and the proportionality test in *K.S. Puttaswamy v Union of India* (2017) 10 SCC 1) [VERIFY: s.7(i) wording].
24. **Vendor money separate from client money** (Finbyx CM4.1) and the **regulated-decision rule**: the Hub prepares, validates, reconciles and evidences; authorised humans approve and file; no portal credentials or OTPs stored or scripted.
25. **Explainability and no hard deletes.** Every computed amount stores inputs and rule and formula versions; financial, HR and evidence records leave only by retention class and legal hold, with a disposal certificate.
26. **Portability of the Hub itself:** every dataset exports in the Integration Spec Part 12.1 archive standard with a signed manifest (folder profile `oh_entity_v1`, registered by proposal), so Infrabyx can leave any vendor, including Brevo.
27. **Scale** for 25 legal entities, 2,000 staff, 5,000 client organisations, 500,000 contacts, 1 million tickets and 100,000 invoices a year [REC; confirm in O0].

## 7.3 Non-functional targets (initial — confirm in Phase O0)

| Area | Target |
|---|---|
| Availability | 99.5% monthly for the Hub app; **99.9%** for catalogue, entitlement, quote, order and invoice APIs used by products |
| Latency | p95 ≤ 300 ms reads, ≤ 800 ms writes, excluding third parties |
| RPO and RTO | RPO ≤ 15 minutes (PITR); RTO ≤ 8 hours, ≤ 4 hours for billing and entitlement APIs; pre-run snapshot before each payroll release |
| Backups | Immutable encrypted copies in a separate ap-south-2 account; daily verification; quarterly restore; books-related data backed up daily in India (Companies (Accounts) Rules r.3(5)) |
| Logs | Security logs ≥ 180 days within India (CERT-In Directions); ≥ 1 year for personal-data processing logs (DPDP Rules r.8(3)) from the applicable date [VERIFY] |
| Incident clocks | CERT-In within 6 hours; affected RE clients ≤ 2 hours from Infrabyx detection (OUT para 61); DPDP Board notice and 72-hour report from the applicable date [VERIFY: 13 May 2027 or earlier] |
| Payroll and billing | 2,000-employee run ≤ 10 minutes; payslips by pay day (Wages (Central) Rules r.52); 5,000-organisation invoice run ≤ 15 minutes |
| Security | OWASP ASVS Level 2; independent VA every 6 months and PT every 12 months, before go-live and after major change [REC] |
| Accessibility and locale | WCAG 2.2 AA for public and client pages; English and Hindi self-service; lakh and crore; DD-MM-YYYY; IST |

## 7.4 Security and privacy controls

Finbyx Part 10.4 controls apply, adapted as follows:

- **Encryption:** field-level encryption for PAN, bank account, UAN, ESIC number, date of birth, salary lines, whistle-blower identities and POSH content; per-entity KMS keys; catalogue, entitlement and manifest signing keys in KMS or HSM with yearly rotation; Aadhaar numbers never stored.
- **Access:** MFA for all; PAM with session recording for production; access reviews and revocation per OH11; SoD enforced at grant.
- **Application:** IDOR and BOLA tests per endpoint; webhook signature and replay protection; DLP on tickets, notes and uploads; CSP and script inventory on billing, directory and public pages (PCI DSS v4.0.1 SAQ A); no card data anywhere (CoFT circular, 7 Sep 2021).
- **Privacy:** notices to staff, candidates, professionals and contacts; purpose tags per field; marketing consent ledger; data-principal requests with retention-aware erasure; DPIAs for HRMS, attendance, CRM and the directory.
- **Monitoring:** alerts on bulk export, off-hours privileged access, payroll or vendor bank-detail changes, mass grants, entitlement overrides and catalogue signing; whistle-blower and POSH access alerts to the Audit Committee chair or nominated director.
- **Break-it review each phase:** cross-entity access, Equator-wall bypass, maker-checker bypass, self-approval, webhook and entitlement forgery, catalogue tampering, directory ranking manipulation, RESTRICTED export without `export.restricted`.

## 7.5 UI/UX principles

- Finbyx design tokens, components and states (Finbyx Part 10.5); the sidebar, role home dashboards, global search, notification centre, saved views and common screen rules of Part 3.5, with the full map in Appendix E; **My Queue** by SLA and keyboard shortcuts on heavy back-office screens.
- A visible **legal-entity switcher**; the acting entity on every record and approval; cross-entity views badged "aggregate only".
- Employee self-service: payslips, Form 130, leave, attendance corrections, timesheets, expenses, policy acknowledgements, my data and requests, whistle-blower link; responsive web, no native app in v1.0.
- Automation with human approval wherever money, pay, access, publication or a client commitment is involved.

## 7.6 The Hub as a group service provider

- Intra-group services (HR, payroll, IT, support, marketing) run under a written services agreement and DPA: scope, arm's-length charges, confidentiality, segregation, audit rights, 24-hour breach notice, exit and data return.
- OUT obligations to NBFC clients sit with Finbyx or Udofin; the Hub keeps the contract, support, release, incident and evidence records they need for OUT paras 34, 61, 74, 77, 81 and 87–88. OUT paras 45–51 and 90–92 bind NBFCs using group services; Infrabyx companies are not NBFCs, so they are design inputs here [INTERP].
- Client pages, invoices and tickets name the group company supplying each service (OUT para 46 spirit); no Hub role decides a client's core management function (OUT para 15).

### Acceptance tests

- A query without session context returns zero rows; a LawDocsComply-scoped user cannot read a Finbyx-entity deal by id.
- Tampering with one audit event fails the nightly verification and raises a Sev-2 alert naming the first broken link.
- Self-approval of a payroll release, expense or vendor activation is refused.
- The Labour Code pack loaded by the Hub has the same version hash as the one Finbyx GV6 loads for the same effective date.
- Production configuration naming a non-India region for database, storage, logs or Temporal fails the CI residency check.

---

# PART 8 — WORKING METHOD, GIT DISCIPLINE AND DEFINITION OF DONE

## 8.1 For each module or sub-module

Follow Finbyx Part 11.1 steps 1–14 (objective in plain English; material questions only; research and register updates; specification with Given/When/Then including negative cases in `docs/specs/[module].md`; data model, APIs, canonical events, permissions and state machines; risks; **stop for my approval**; implement the approved scope in small commits; run the applicable tests; lint, typecheck, build, migration and security checks; diff review; documentation; summary with real test output and mock versus live status; pull request merged only after my approval), with three additions:

- name the legal entities and roles affected, and add cross-entity and Equator-wall cases to the acceptance criteria;
- run a DPIA for any module that processes staff, candidate, professional or contact data, and an employee-fairness review for HR, attendance, appraisal, ROI and AI features;
- keep `docs/compliance/legal-register.md` (Labour Codes, State rules, S&E, EPF, ESI, PT, LWF, POSH, DPDP, CERT-In, Companies Act, GST, Income-tax Act 2025, TRAI, BCI, RBI payment rules, PCI) dated and current, with `[VERIFY]` items tracked to closure.

## 8.2 Pay, money and evidence integrity before features

No live payroll, invoice, payment or directory listing until its rules and acceptance tests are approved. Keep a **golden test-case library** approved by me, the finance reviewer and an employment-law reviewer, including:

- **Wages (CoW s.2(y); MoLE FAQ 4, 7):** total ₹76,000, excluded allowances ₹40,000, 50% cap ₹38,000, add-back ₹2,000 → wages **₹22,000**.
- **Final settlement:** wages and leave encashment by the second working day after the LWD on the State calendar (CoW s.17(2); OSHWC s.32), never waiting for clearance; unserved notice pay not deducted; deductions ≤ 50% with carry-forward (s.18(3); Wages (Central) Rules r.13).
- **Gratuity:** `round(15/26 × last monthly wages × completed years)`, part year above 6 months counted, ceiling ₹20,00,000, fixed-term eligibility after 1 year, payable within 30 days (CoSS).
- **Leave:** 180 days worked → `floor(days_worked / 20)`; carry-forward cap 30; refused leave carried without cap (OSHWC s.32).
- **Overtime:** 2 × (`monthly ÷ 26 ÷ 8`), with consent, blocked above 144 hours a quarter (OSHWC Central Rules; Wages (Central) Rules r.3).
- **EPF and ESI:** EPF wage ceiling ₹15,000, 12% employee, 8.33% EPS within the employer share [VERIFY under CoSS]; ESI 0.75% and 3.25%, employee share waived at ≤ ₹176 average daily wage [VERIFY coverage ceiling].
- **Salary TDS:** Income-tax Act 2025 s.392 projection under each regime [VERIFY s.202 mechanics]; Form 138 quarterly; Form 130 by 15 June.
- **Billing:** mid-term upgrade proration; downgrade at term end; IGST for inter-State and CGST + SGST for intra-State B2B supplies (IGST Act s.12(2)); credit note (CGST Act s.34); client TDS reconciled to Form 131 [VERIFY section and rate]; SEZ supply under LUT (IGST Act s.16).
- **Revenue recognition:** upfront annual fee recognised ratably; non-distinct implementation fee deferred over the expected term; usage when used; under AS 9 or Ind AS 115 per Appendix B decision 3.
- **E-mandate:** a ₹18,000 recurring card debit is never a no-AFA mandate (E-mandate Directions 2026 para 8(a)).

## 8.3 Git and environment rules (Finbyx Part 11.3 and Part 7L EO1 applied)

- Finbyx Part 11.3 applies: inspect first; feature branches only; **never push to `main`**; no production deployment, credential rotation or production-data change without my explicit authorisation; no secrets or real data in the repository; never claim a commit or passing test without evidence.
- **Repositories:** `infrabyx-ops-hub` and `infrabyx-ops-hub-infra`, private, in the products' GitHub organisation and plan; SSO-linked accounts, 2FA, base permission none, expiring fine-grained tokens.
- **Rulesets from Phase O1 (EO1.2):** on `main` restrict deletions, block force pushes, linear history, signed commits, pull request with ≥ 1 approval, stale approvals dismissed, last push approved by someone else, code-owner review, conversation resolution, required checks, `staging` deployment before merge, empty bypass list; tags `v*` created only by the release workflow, never updated or deleted.
- **Required checks:** lint, typecheck, unit and property tests, Testcontainers integration, Pact and schema compatibility, migration dry-run with expand-and-contract lint, golden payroll and billing cases, entity-isolation and Equator-wall tests, dependency and licence scan, CodeQL or Semgrep, secret scan, SBOM, PII and card-pattern log scanner, Office and PDF/A rendering, workflow lint.
- **Patch and vulnerability SLAs** for the Hub's repositories and infrastructure are the group platform SLAs of Finbyx Part 7L EO1.6, applied to every group repository through OH13: from triage, critical (CVSS ≥ 9.0, CISA KEV-listed or actively exploited) 72 hours, high 7 days, medium 30 days, low 90 days; exceptions only by CISO risk acceptance expiring within 90 days; a stricter contract or audit-finding policy wins. Internal or tenant audit findings about non-platform systems use the Finbyx AU4.3 remediation defaults (15, 30, 90 and 180 days).
- **Two approvals** (`sensitive-path-approvals`) for `/modules/payroll/`, `/modules/billing/`, `/modules/payments-razorpay/`, `/modules/controls/`, `/modules/group-identity/`, `/packages/rule-packs/`, `/db/` and `/.github/`; CODEOWNERS covers every module and package; Actions pinned to SHA, read-only default permissions, GitHub OIDC to AWS, no long-lived cloud keys.
- **Environments:** `dev` and `staging` (synthetic only; Railway allowed); `prod-in` (India; signed tags; 2 reviewers other than the author; 15-minute wait; scoped secrets); `dr-in` (same tag; drift check). **Freeze windows:** payroll cut-off to bank-file release, last 2 and first 3 working days of each month, statutory due dates. Synthetic PAN-like seeds use an invalid pattern so scanners can tell them apart.

## 8.4 Project documents to maintain

As Finbyx Part 11.4, plus: `docs/ecosystem/infrabyx-integration-spec.md` (SHA-256 checked in CI); `docs/compliance/legal-register.md` and `controls-map.md`; `docs/privacy/` (notices, DPIAs, processing records, retention schedule); `docs/testing/golden-cases/` (payroll, billing, revenue); `docs/ops/` runbooks (payroll run, statutory filing, invoice run, dunning, joiner, leaver, incident, DR); `docs/ux/` (navigation map, screen inventory, settings and notification catalogues kept in step with Appendix E); `docs/policies/` drafts (HR, WFH, anti-fraud, DoA, expenses, whistle-blower, POSH, acceptable use, AI use).

## 8.5 Definition of done

1. A module is not complete because its screen renders.
2. It is complete only when: approved acceptance criteria are met; negative, entity-isolation and Equator-wall tests have run with recorded output; grants, maker-checker and DoA are checked; failures, retries and reconciliation are handled; pay and invoice amounts match the golden cases; audit events are emitted and the chain verifies; notices, retention classes and DPIA exist for personal data; documents and registers are updated; the change is reviewable.
3. Mock and sandbox integrations are always labelled as such in UI, logs and configuration.
4. The goal is a secure, lawful, auditable and useful operations platform, not the largest number of features.

## 8.6 Additional quality gates

- Independent security review each phase (7.4); employee-fairness review for people features; legal-entity boundary review for every dashboard, export and report; claims-gate review for every client-facing or public text.
- Restore of database, documents and Temporal state tested before go-live and quarterly.
- Regulatory change management: when a rule changes (for example a State notifies its Labour Code rules or revises PT), assess rule packs, letters, registers, tests and evidence and ship a regulated-class rule-pack change.
- Commercial viability: Hub running costs (licences, Brevo, Razorpay fees, cloud) tracked by legal entity for intra-group cost sharing.

---

# PART 9 — PHASED ROADMAP WITH CLAUDE CODE INSTRUCTIONS

Build the secure, legal-entity-scoped platform first, then what the products depend on (catalogue, entitlements, billing, provisioning), then the people and control modules, then go live, then analytics and AI.

- **Product dependencies.** Finbyx Phase 16e needs **O6** live at least in staging; Udofin Phase 20b needs **O6** for RE invoicing only (borrower plans bill on Udofin's own Razorpay account). Finbyx 20b and Udofin 16c send evidence to **O12** and keep a local evidence store with the same schema until O12 is live. Finbyx 16d pins the Labour Code rule pack 1.0 (Integration Spec Part 12.3), whose first signed release is a deliverable of **O9**. Before O6, products and pilots use a signed static catalogue file and manual invoicing.
- **Menus, screens and settings in every phase.** Each phase builds the `Menu and screens` and `Settings and options` of the modules it delivers (Part 5; consolidated in Appendix E), the module's Home tiles and notifications (Appendix E.4), and registers every setting in the settings registry with its level, default and floor. O1 builds the application shell; O13 adds the governed metric layer behind the tiles.
- **Synthetic data only** in development and staging; real staff, client, contact and payroll data enter only India-region production after OP.
- **How to run.** Each phase ends with a review gate. Paste one **"Instruction to Claude"** block at a time; split large phases into the runbook's sub-modules; every phase first verifies the facts it relies on and records them in the legal or integration register.
- **Order:** O0 → O1 → O2 → O3 → O4 → O5 → O6 → O7 → O8 → O9 → O10 → O11 → O12 → OP → O13. O7 and O8 may follow OP by owner decision; O6 may run in parallel with O4–O5 once O3 is merged if Finbyx 16e is imminent.

| Phase | Primary outcome | Depends on |
|---|---|---|
| O0. Repository audit and architecture | Inventory of current tools and data; architecture and ADRs; build-versus-buy per module; legal register v1; entity model; event and API boundaries | — |
| O1. Platform foundation and group identity | Monorepo; CI with EO1 rulesets from day one; environments; OIDC federation with MFA; legal-entity register skeleton; application shell (sidebar, Home, global search, notification centre, saved views, entity switcher); design system; observability | O0 |
| O2. Data model, legal-entity scoping and audit trail | Forced RLS; group grants and SoD; Equator wall and case-party block list; hash-chained audit; maker-checker; settings registry; rule-pack framework; claims-gate service v0 (lexicon and empty certification register); outbox and inbox; retention and legal hold (OH1) | O1 |
| O3. CRM and marketing consent | Open-schema CRM (OH3); consent ledger and send gate; Brevo adapter with exit export | O2 |
| O4. Client onboarding, delivery and migration factory | Provisioning orders, gates and `TenantProvisioned` with acknowledgement; implementation projects and milestones; migration factory; exit cases (OH4) | O3 (plan refs from the static catalogue until O6) |
| O5. Support desk and customer success | Tickets with SLAs and DLP; borrower-complaint forwarding; client grievance ladder; knowledge base; health and renewals (OH6, OH5) | O3, O4 |
| O6. Revenue catalogue, billing and Razorpay | Signed catalogue; entitlements; usage intake; GST invoices; Razorpay; dunning with regulatory continuity; revenue recognition and review (OH8) | O3, O4 |
| O7. Marketing, brand, social media and PR | Brand library; content queue with claims gate; campaigns; social publishing; PR and collaborations (OH7) | O3, O5 |
| O8. Professional and advocate directory | Rule 36 public listing; empanelment and verification; allocation feed; conflict register and the Equator conflict-check API (OH9, OH1.6) | O2 |
| O9. Staff HRMS and payroll | Hire-to-retire; attendance and WFH; leave; Labour Code payroll with the shared rule pack (first signed release 1.0); statutory filing packs; appraisals (OH10) | O2 |
| O10. Internal controls and anti-fraud | DoA; SoD; vendor master; expenses; ghost-employee tests; access reviews; whistle-blower channel; staff ROI (OH11) | O6, O9 |
| O11. Workplace integration (Microsoft 365 / Google Workspace) | One `WorkplaceProvider`; joiner, mover, leaver; `MailboxProvisioned`; document management; migration runbooks (OH12) | O1, O9 |
| O12. Engineering-operations console and certification readiness | Cross-product release, change (CAB and `ChangeApproved`), patch, VAPT, backup and incident console; control framework; evidence collectors; full claims gate and certification register; auditor portal (OH13, OH14) | O2, O10, O11 |
| **OP. Hub go-live** | VAPT, restore drill, residency check, parallel payroll and billing, migration and cut-over | O1–O12 (O7, O8 may follow by owner decision) |
| O13. Dashboards, analytics and AI assistance | Governed metric layer behind the Home tiles and dashboards, leadership packs (OH2); governed AI assistance; read-only MCP server | OP |

### Phase O0 — Repository audit and architecture

> **Instruction to Claude:** "Read docs/00-master-prompt.md in full (Parts 1–10, Appendices A–E, Sources), docs/ecosystem/infrabyx-integration-spec.md (v1.1, canonical) and the tenant-side Parts the Hub serves: Finbyx Parts 7F (GV6, GV7), 7J, 7K and 7L; Udofin Parts 7G and 7H. Inspect the repository, branch, files, Git status and tooling and report them. Do not write application code or modify the repository yet.
>
> First verify, with dated sources: (i) current stable versions and licences of Next.js, NestJS, Node.js 26 LTS, PostgreSQL, Supabase regions, Temporal, GoRules ZEN and CEL; (ii) the India residency position of every candidate sub-processor (Supabase, AWS, Railway, Temporal Cloud, Sentry, Brevo, Razorpay, Microsoft 365 Default Geography and Advanced Data Residency, Google Workspace data regions, GitHub, any LLM endpoint); (iii) Labour Code State rules for Delhi, Uttar Pradesh and Rajasthan and current EPF, ESI, PT and LWF parameters; (iv) the Income-tax Act 2025 salary forms (Form 138, Form 130); (v) which office suite and plan Infrabyx actually holds.
>
> Produce:
>
> 0. An inventory of current operational tools and data per legal entity (spreadsheets, CRM and Brevo lists, payroll, Tally Prime or Zoho Books, office-suite tenants, GitHub, support mailboxes, social accounts): owners, volumes, quality, migration needs.
> 1. The architecture: context, module map OH1–OH14 with data ownership, legal-entity and client scoping (API, service, forced RLS), the grant model and the Equator wall.
> 2. Technology ADRs, including the rules engine, IdP federation and the residency check per sub-processor.
> 3. Build-versus-buy per module (for example HubSpot or Zoho CRM, Freshdesk, Keka, greytHR or Razorpay Payroll, Vanta, Drata or Sprinto): cost, residency, integration effort, exit path.
> 4. The repository structure (Appendix C) and entity model (Appendix D).
> 5. Event and API boundaries from Part 6, with gaps written as Integration Spec proposals.
> 6. Legal register v1: every source in Part 4 and in the Sources list with title, number, date and status; every [VERIFY] with the phase that closes it.
> 7. The roadmap with acceptance criteria and the minimum security, testing and review gates.
> 8. The Appendix B decisions with your recommendation for each.
> 9. The navigation map: confirm the sidebar order, the workspace visibility matrix and the settings catalogue defaults and floors of Appendix E, and list any screen or setting you propose to add or drop.
>
> Present all of this for my approval before modifying the repository."

### Phase O1 — Platform foundation and group identity

> **Instruction to Claude:** "Verify first: (i) the approved O0 ADRs are merged; (ii) which ruleset, secret-scanning and code-scanning features our GitHub plan includes for private repositories; (iii) the group directory (Entra ID or Google) and the consent it needs.
>
> On branch `feat/oh-platform-foundation` build:
>
> - pnpm + Turborepo, TypeScript strict; `apps/web`, `apps/api`, `apps/worker`; `packages/` contracts (generated from `infrabyx-contracts`), domain-kernel (Money, Rate, BusinessDate, State working-day calendars, IDs), ui (shared tokens), config, observability, testing; Docker Compose for Postgres, Temporal and Gotenberg; `.env.example` only;
> - **GitHub controls from day one (Part 8.3):** rulesets, CODEOWNERS with coverage check, signed commits, required checks, `sensitive-path-approvals`, SHA-pinned Actions, environments with reviewers, nightly ruleset export as evidence;
> - OIDC abstraction with federation to the group directory, mandatory MFA and the Integration Spec Part 4.6 claims (`org_id` of the employing entity, `entity_scope[]`, `grant_ids[]`, `acr`, `auth_time`), plus `employee_ref` inside the Hub;
> - the OH1 legal-entity register skeleton (legal entities, GSTINs by State, offices, State calendars);
> - OpenTelemetry with PII scrubbing; NTP drift alarm; Storybook;
> - the **application shell** of Part 3.5: sidebar in the fixed order with workspace-based visibility (Appendix E.2), Home with My Queue and role tiles (placeholders until each module lands), legal-entity switcher, command palette (`Ctrl+K` or `Cmd+K`), keyboard shortcuts, notification-centre UI, saved-view UI, and the list, detail, wizard, approval-queue, empty-state and error-state components; WCAG 2.2 AA checks (axe) in CI.
>
> Tests and acceptance evidence:
>
> - a direct push, force push or unsigned commit to `main` is rejected and the ruleset export is stored;
> - a pull request changing `/.github/` with one code-owner approval fails `sensitive-path-approvals`;
> - sign-in without MFA is refused; a single-entity user's token carries only that scope;
> - a seeded log line with an email or PAN-like value is scrubbed and the scanner fails the build;
> - property tests pass for Money, and the working-day calculator returns the correct second working day after a Friday before a State holiday;
> - a user whose workspace lacks a menu does not see it in the sidebar and receives 403 on its route; the axe check passes on every shell screen.
>
> Build no business features. Show me the repository skeleton, ruleset configuration and claim mapping for approval before coding, then open a pull request with the test output."

### Phase O2 — Data model, legal-entity scoping and audit trail

> **Instruction to Claude:** "Verify first: (i) RLS with Supabase transaction pooling and `set_config(…, true)`; (ii) the Integration Spec SDK version and the `oh` source, `group_grant` and data-class ceiling rules (Integration Spec Parts 3.2, 4.6, 13.2); (iii) the rules-engine ADR.
>
> On branch `feat/oh-entity-scoping-audit` create migrations and services for person, employment, user, role, permission, group_grant, purpose_code, sod_conflict_rule, break_glass_record, case_party_block, relationship; legal_entity, office, department, cost_centre, client_org (Integration Spec `org_id`); maker_checker_request, doa_rule, audit_event (hash-chained), outbox, inbox, idempotency, DLQ; setting_definition and setting_value (the settings registry of Part 3.4); notification_type, notification and notification_preference (Appendix E.4); saved_view; search_index_entry; rule_pack_version with the loader and signature check for the shared Labour Code pack; claims_lexicon_entry and an empty certification register (claims-gate service v0: every certification claim blocked until O12); retention_class, legal_hold, disposal_certificate; data-principal requests.
>
> Implement forced RLS on `legal_entity_id`, `client_org_id` and `sensitivity` with the API on a non-owner role; RBAC + ABAC with grants and DoA limits; maker-checker with fresh MFA; the nightly audit-chain verifier and anchor; Integration Spec outbox, inbox, schema, data-class ceiling and forbidden-field validation, Standard Webhooks and RFC 9421; the cross-entity grant workflow of OH1.4 (principal's and target entities' heads and the DPO; ≤ 90 days; SCIM `valid_to`); the Equator wall and wall-breach log; the settings registry with floor enforcement and maker-checker; the notification engine (in-app and email; Teams or Google Chat through OH12 later; mandatory categories cannot be muted); permission-trimmed global search.
>
> - **Menus, screens and settings:** the `Admin` menu and OH1 settings exactly as the OH1 `Menu and screens` and `Settings and options` tables specify; `Home › Notifications` and `Home › Saved views`.
>
> Tests and acceptance evidence:
>
> - cross-entity and cross-client reads and writes fail; no context returns zero rows;
> - a RESTRICTED row is invisible under a CONFIDENTIAL ceiling;
> - a maker cannot check their own request; an expired grant stops at `valid_to`;
> - a lender-side user cannot be granted an Equator role;
> - a direct edit of one audit row is detected by the verifier;
> - an inbound event with a forbidden field goes to the DLQ;
> - a cross-entity grant lacking the DPO's approval cannot be activated;
> - a record under legal hold cannot be disposed of, and a disposal outside hold produces a certificate;
> - global search returns no record outside the user's scope and no Equator record to a lender-side user; a query with a PAN-like pattern is refused;
> - a setting saved below its floor is refused with the rule shown; a mandatory notification cannot be muted;
> - the claims-gate service blocks "ISO 27001 certified" while the certification register is empty.
>
> Show me the entity model, RLS policies, grant workflow and SoD matrix for approval before coding."

### Phase O3 — CRM and marketing consent

> **Instruction to Claude:** "Verify first: (i) my build-versus-buy decision for the CRM (Hub as system of record with Brevo for sending, or Brevo-first); (ii) Brevo's current CRM paths, limits, webhooks, export job and hosting; (iii) TCCCPR 2018 as amended on 12 Feb 2025 (opt-out, 90-day re-consent wait, 140-series, DLT headers and templates) and whether Infrabyx needs its own DLT principal-entity registration; (iv) DPDP notice and consent rules and their commencement.
>
> On branch `feat/oh-crm-consent` build OH3:
>
> - **Open schema:** organisations linked to the Integration Spec `org_id` (CIN, GSTIN, RBI certificate of registration or other licence, entity type as declared), contacts, leads, opportunities and pipelines per legal entity and product, activities, tasks, partners; custom objects and fields as versioned JSON Schemas with maker-checker; import with dry run, de-duplication and reject file; full signed export (Integration Spec Part 12).
> - **Consent ledger and send gate (OH3.3–OH3.4):** consent by channel and purpose with basis, source, notice version and withdrawal; DND; DLT template ids. A send is refused with a reason unless purpose matches, no opt-out in the last 90 days, DLT header, template and category are valid, promotions carry an opt-out, promotional voice uses the 140-series route, and service messages go only to existing clients.
> - **Brevo adapter** (`CrmMarketingProvider`): two-way sync of B2B contacts and lists, 429 back-off, webhooks to the event store, nightly full export; contacts flagged as a client's borrower, member or employee are refused.
> - **Equator segregation:** Equator's pipeline visible only within Equator; lender-side users cannot see which REs refer cases to Equator.
> - Data-principal requests for contacts with retention exceptions.
> - **Client lifecycle** timeline on the client 360 page with the stages, owners, timers and failure paths of OH3.2.
> - **Menus, screens and settings:** the `Clients` and `CRM` menus and OH3 settings exactly as the OH3 `Menu and screens` and `Settings and options` tables specify, including the segment builder with live consent counts, the import wizard and the merge queue.
>
> Tests and acceptance evidence:
>
> - a promotion to a contact who opted out 60 days ago is refused;
> - an SMS without a DLT template id is refused;
> - a Finbyx sales user cannot open an Equator opportunity by id;
> - an import containing a PAN-like column is rejected;
> - during a Brevo outage sync queues without loss, and the nightly export reproduces every Hub contact with checksums.
>
> Show me the CRM model, custom-field governance, send-gate rules and Brevo field map for approval before coding."

### Phase O4 — Client onboarding, delivery and migration factory

> **Instruction to Claude:** "Verify first: (i) the provisioning contract of Integration Spec Part 6.29 (`TenantProvisioned`, `PUT /v1/provisioning-requests/{id}`, `GET /v1/tenants/{tenantid}/provisioning-status`) and each product's implementation of it; (ii) the contract set each product needs before a production RE tenant (Finbyx Part 10.6 items 1 and 13–17, CM5.4; Udofin UP1); (iii) how an RBI certificate of registration, CIN, GSTIN and co-operative registration are verified; (iv) Finbyx DP5 exit turnaround times.
>
> On branch `feat/oh-onboarding-delivery` build OH4:
>
> - **Provisioning orders** `DRAFT → GATES_PENDING → APPROVED → ACCEPTED → READY → LIVE` (or `REJECTED`, `FAILED`) as OH4.2: sandbox tenants self-served with synthetic data; UAT and production need the signed MSA and DPA with the OUT clause matrix, due-diligence evidence, the client's outsourcing assessment where it applies, a named admin work email, data region and plan; signed `TenantProvisioned`, acknowledgement capture and the fallback poll.
> - **Implementation projects:** templates by product and institution profile (NBFC-BL, NBFC-MFI, HFC, credit co-operative society, co-operative bank, ARC, IFSCA finance company, listed entity), milestones, RACI, RAID log, client sign-off evidence; `ImplementationMilestoneReached` to OH8.
> - **Migration factory (tracking only):** plans, mapping-pack versions, dry-run counts, reconciliation sign-off and cut-over checklists; legacy data is loaded and reconciled inside the product tenant (Finbyx Phase 19), never in the Hub.
> - **Office-suite migrations for clients** as service engagements with the vendors' tools [VERIFY edition limits].
> - **Exit cases** (OH4.6): `ExportRequested` and `ExportCompleted` tracking, turnaround, successor cooperation log, no-erasure-during-transition flag, purge certificate and independent assurance (OUT paras 87, 88, 97(xvi)).
> - **Menus, screens and settings:** the `Onboarding` menu, the client implementation portal and OH4 settings exactly as the OH4 `Menu and screens` and `Settings and options` tables specify.
>
> Tests and acceptance evidence:
>
> - a production order without a DPA reference cannot be approved;
> - a milestone accepted twice emits one `ImplementationMilestoneReached`;
> - no Hub migration record holds a loan or customer field (schema test);
> - an exit case cannot close without a purge certificate and client sign-off;
> - a `FAILED` acknowledgement shows its reason code and a resubmission carries a new request id.
>
> Show me the provisioning gates, project templates, exit checklist and screen list for approval before coding."

### Phase O5 — Support desk and customer success

> **Instruction to Claude:** "Verify first: (i) support tiers and SLAs in current client contracts; (ii) the RE grievance-routing rules (CF para 12; OUT paras 54–57; NBFC Internal Ombudsman Directions 2026; RBI Ombudsman Scheme 2026); (iii) incident clocks (OUT para 61; CERT-In Directions) and the `SecurityIncidentNotified` contract.
>
> On branch `feat/oh-support-success` build OH6 and OH5:
>
> - **Tickets** from in-product help (`POST /v1/support/tickets`), email, portal, phone and Teams; triage queue with AI suggestions and duplicate detection; severity matrix with the four clocks (response, update, workaround, resolution) by tier and business calendar, pause only in `WAITING_ON_CLIENT`, reopen window; escalation to L2, engineering (linked GitHub issue and change id) and management; `SupportTicketOpened`, `SupportTicketResolved`.
> - **DLP at intake** (PAN, Aadhaar, account, card, mobile; attachment OCR); client data stays behind the product deep link.
> - **Borrower complaints reaching Infrabyx** are forwarded to the RE's grievance redressal officer within 1 working day, the complainant is told which RE handles it, and Infrabyx can never mark them resolved.
> - **Client grievances against Infrabyx:** support head → product head → director, with time limits [REC: acknowledge in 1 working day, resolve in 15], root cause, corrective action and OH8 credit notes where agreed.
> - **Vendor incidents:** severity-1 tickets show detection, client-notice (≤ 2 hours) and CERT-In (6 hours) clocks.
> - **Knowledge base and service catalogue** with review dates and the claims gate.
> - **Customer success:** health score from aggregates (usage trend, tickets, SLA breaches, invoice status, module adoption, CSAT or NPS); renewals at 120, 90, 60, 30 and 7 days; success plans, business reviews and churn playbooks.
> - **Menus, screens and settings:** the `Support` and `Success` menus, the client support portal and OH5 and OH6 settings exactly as their `Menu and screens` and `Settings and options` tables specify.
>
> Tests and acceptance evidence:
>
> - a severity-1 response-SLA breach escalates automatically and shows on the client's ticket page;
> - an emailed borrower complaint is forwarded to the configured RE officer within 1 working day, its body is purged after acknowledgement, and it cannot be resolved by Infrabyx;
> - a Sev 2 ticket in `WAITING_ON_THIRD_PARTY` keeps its clock running and escalates at 50% and 75%;
> - a health score recomputes from stored inputs and contains no tenant record ids;
> - an article calling a product "SOC 2 certified" without an issued report fails the claims gate.
>
> Show me the SLA matrix, grievance ladder and health-score formula for approval before coding."

### Phase O6 — Revenue catalogue, billing and Razorpay

> **Instruction to Claude:** "Verify first: (i) my decisions on merchant of record, plan tiers and SKUs, and AS 9 or Ind AS 115 (Appendix B); (ii) Razorpay's current Orders, Payment Links, Subscriptions, eNACH and Smart Collect APIs, webhook rules, PA authorisation and PCI AoC; (iii) the E-mandate Directions 2026 (RBI/DPSS/2026-27/396); (iv) GST for SaaS and IT services (SAC [VERIFY], IGST Act s.12(2), e-invoicing threshold, LUT for SEZ and IFSC units) and the TDS clients apply to our fees [VERIFY]; (v) the Finbyx CM1–CM5 and Udofin RV1–RV4 contracts.
>
> On branch `feat/oh-billing-catalogue` build OH8:
>
> - **Catalogue:** products, plans, SKUs mapped to each product's module registry, meters, price books, add-ons, revenue-stream flags with the legality gate (Finbyx CM5.3), explainers checked by the claims gate; JWS-signed versions served by `GET /v1/catalogue/versions/{v}`.
> - **Subscriptions and entitlements:** upgrade immediately, downgrade at term end, renewal, cancellation; signed `PlanChanged` and `EntitlementChanged`; contract tests against the Finbyx CM1.4 regulatory-continuity rule.
> - **Usage intake:** `UsageRecorded` aggregates; 7-day disputes; Udofin B2C aggregates only.
> - **Invoicing:** tax invoices, credit and debit notes (CGST Act s.34), IGST or CGST + SGST, IRN and QR through the IRP above ₹5 crore AATO, LUT zero-rating, Form 131 reconciliation; `InvoiceIssued`.
> - **Quotes and orders:** `POST /v1/billing/quotes` (priced quote and proration preview, valid 7 days) and `POST /v1/billing/orders` (Razorpay-hosted URL for top-level redirect), both with Idempotency-Key; `GET /v1/billing/invoices?tenantid=`; `GET /v1/entitlements?tenant=` daily reconciliation.
> - **Payments:** redirect checkout or Payment Links; Subscriptions with card or UPI AutoPay (no AFA only up to ₹15,000; issuer notice ≥ 24 hours; our notice at T-48 hours); eNACH above that; Smart Collect; raw-body HMAC, event-id de-duplication, order-insensitive upserts, daily settlement reconciliation; `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`.
> - **Dunning:** `ACTIVE → PAST_DUE → RETRY (D+1, D+3, D+7) → GRACE (D+14) → RESTRICTED (D+30, after 7 days' notice) → TERMINATION_NOTICE (D+45) → EXIT`; `SubscriptionCancelled` only when the notice expires; never a hard cancel.
> - **Revenue recognition** schedules, monthly journals to Tally or Zoho Books, intra-group recharges.
> - **Revenue-model review:** MRR, ARR, NRR, churn, ARPA, CAC payback, implementation margin and unit economics by product, stream, market and channel, with switch-on and switch-off scenarios.
> - **Menus, screens and settings:** the `Revenue` menu and OH8 settings exactly as the OH8 `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - every billing golden case in Part 8.2 passes to the paisa;
> - a tampered catalogue fails the Finbyx contract test; a SKU naming an unknown module fails import;
> - a forged webhook is rejected and a replay changes nothing; a browser-only success leaves the invoice unpaid;
> - RESTRICTED sends no entitlement change that would stop a regulated function;
> - a stream without an approved legality gate is not published.
>
> Show me the catalogue schema, dunning state machine, GST matrix and revenue rules for approval before coding."

### Phase O7 — Marketing, brand, social media and PR

> **Instruction to Claude:** "Verify first: (i) the platforms I chose and each one's publishing API terms; (ii) the ASCI Code, the CCPA Dark Patterns Guidelines 2023 and any rule on advertising software for regulated entities [VERIFY]; (iii) BCI Rule 36 for anything mentioning advocates; (iv) the rule that Equator is never presented as the default ODR for Finbyx or Udofin clients.
>
> On branch `feat/oh-marketing-brand` build OH7:
>
> - **Brand library** per entity and product with licences and expiry.
> - **Content queue:** drafts, marketing, legal and product review, maker-checker, scheduled publishing via `SocialPublisher`; the claims gate blocks "certified", "guaranteed compliance", "RBI approved" and similar claims without an OH14 record; no fake scarcity, countdown timers, inflated value figures or unverifiable testimonials.
> - **Campaigns:** consent-based segments, Brevo sending, UTM tracking, landing pages with consent capture and DPDP notices, webinars with disclosures; leads routed to OH3 with SLA.
> - **Legitimate self-serve funnel:** sandbox trial with synthetic data, activation checklist and nurture, with the O4 production gate (Finbyx CM5.4).
> - **PR and collaborations register:** coverage, releases, events, sponsorships, MoUs with obligations and conflict checks (Equator neutrality; auditor independence where a group company audits a client).
> - **Social listening and responses:** aggregate mentions and post metrics only; complaints raised on social channels are routed to OH6 within 1 working day.
> - **Workflows:** campaign approval with the audience freeze and send-time consent re-check (OH7.2), the press-release and collaboration pipelines (OH7.7), using the claims-gate service from O2.
> - **Menus, screens and settings:** the `Marketing` menu and OH7 settings exactly as the OH7 `Menu and screens` and `Settings and options` tables specify.
>
> Tests and acceptance evidence:
>
> - a post claiming "ISO 27001 certified" without a certificate record cannot be approved;
> - a segment cannot include a contact without matching consent;
> - a lender-side campaign naming Equator as ODR partner is blocked for legal review;
> - a retried platform callback does not publish twice;
> - a contact who withdraws consent after the audience freeze is excluded at send time.
>
> Show me the approval chain, claims lexicon and campaign model for approval before coding."

### Phase O8 — Professional and advocate directory

> **Instruction to Claude:** "Verify first: (i) BCI Rule 36, the 2008 proviso (Resolution 50/2008) and its Schedule of permitted website information, *P.N. Vignesh* (Madras HC, 2024) and the BCI notices of 6 Jul 2024; (ii) verification sources per professional type (State Bar Council enrolment, ICAI and ICSI certificates of practice, IBBI registration, valuer registration) [VERIFY access]; (iii) the Finbyx R11 rules that consume the directory; (iv) the public-listing scope I chose (Appendix B decision 8).
>
> On branch `feat/oh-directory` build OH9:
>
> - **Professional record:** type (advocate, chartered accountant, company secretary, cost accountant, insolvency professional, registered valuer, mediator), verification evidence, jurisdictions, forums, practice areas, languages, listing consent, notice version.
> - **States** as OH9.2 (`INVITED` or `APPLIED` → … → `EMPANELLED → ACTIVE`, `ANNUAL_REVIEW`, `SUSPENDED`, `LAPSED`, `REMOVED`, `WITHDRAWN`); public listing only for `ACTIVE` professionals with listing consent; `ProfessionalEmpanelled` on `EMPANELLED` and on each new version; `ProfessionalSuspended` (`suspension_seq`) on suspension, lapse or removal.
> - **Public listing, Rule 36 Schedule fields only:** name, address, contacts, enrolment number and State Bar Council, enrolment date, qualifications, practice areas. **No** ratings, reviews, "top" or "premium" badges, success rates, fees, testimonials or paid placement; neutral ordering (alphabetical or logged seeded random); the same on every group website.
> - **RE panels stay in Finbyx R11:** the RE decides empanelment, fees and allocation; the Hub receives `MatterAllocated` (status and `update_seq`, no party, matter or loan identifiers) only for rotation-fairness, concentration and conflict-count reports.
> - **Equator conflict-check API** `POST /v1/conflicts/check` (OH1.6): counts and flags only, default window `P3Y`, every call logged.
> - **Conflict register:** relationships with group companies, REs and Equator; Equator neutrals flagged (`equator_neutral`) so R11 can block them as counsel in related matters. Performance scorecards live only in each RE's tenant.
> - **Menus, screens and settings:** the `Directory` menu, the professional portal and OH9 settings exactly as the OH9 `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - the public API exposes only Schedule fields and offers no sort other than neutral ordering;
> - adding a "featured" flag or paid-listing SKU fails the catalogue and claims checks;
> - a suspended advocate leaves the public feed within 1 hour and R11 receives `ProfessionalSuspended`;
> - a `MatterAllocated` payload with a borrower name is rejected; a status change with a lower `update_seq` is ignored;
> - the conflict API returns only the allocation count, flag, category and `as_of`.
>
> Show me the listing fields, verification sources and state machine for approval before coding."

### Phase O9 — Staff HRMS and payroll

> **Instruction to Claude:** "Verify first and record in the legal register: (i) the four Labour Codes (in force 21 Nov 2025) and Central Rules of 8 May 2026 (G.S.R. 342(E)–345(E); corrigendum G.S.R. 629(E) of 15 Jul 2026); (ii) State rules, Shops and Establishments changes, minimum wages, PT and LWF for Delhi, Uttar Pradesh, Rajasthan and any other State where we employ staff [VERIFY each]; (iii) EPF, ESI, gratuity, maternity and POSH thresholds by headcount per office; (iv) Income-tax Act 2025 salary TDS (s.392, Form 138, Form 130) and the Form 12BB equivalent; (v) my decisions on payroll in-house or provider and on WFH (Appendix B).
>
> On branch `feat/oh-hrms-payroll` build OH10 on the shared, signed **Labour Code rule pack** `infrabyx-labour-rulepack` (Integration Spec Part 12.3), publishing its first signed release 1.0 with golden fixtures that Finbyx GV6 also runs:
>
> - **Hire-to-retire** from requisition to archive, with appointment letters tagging wage components by CoW class and a WFH clause, backfill letters for existing staff, email addresses `first.last@[entity domain]` with collision rules, reserved names, 90-day quarantine and no reissue; `EmployeeOnboarded`, `EmployeeOffboarded` (oh scope).
> - **Attendance and WFH:** SSO sign-in and sign-out, timesheets by project or ticket, regularisation; no activity, screen, webcam or off-duty location monitoring; employee notice and self-view.
> - **Leave** (OSHWC s.32 and policy) with office holiday calendars.
> - **Payroll:** CoW wages with the 50% add-back; EPF, ESI, PT, LWF, TDS projection; overtime with consent and the 144-hour quarterly cap; minimum-wage block; deduction cap with carry-forward; Form V payslips by pay day; Forms I, IV and IX kept 5 years; variance report (± 10% per head, new bank accounts); HR prepares, finance releases, no one approves their own line; bank file by `PayoutFileProvider`.
> - **F&F timers:** wages and encashment by LWD + 2 working days, gratuity within 30 days, service certificate within 10 days, never waiting for clearance.
> - **Guided statutory packs:** ECR, ESIC, PT, LWF, Form 138 data and Form 130, with acknowledgement capture and no stored credentials.
> - **Performance and learning** (goals, appraisal and calibration, training records feeding OH14) and **POSH** (Internal Committee per office of 10 or more, restricted case register, annual report data).
> - **Menus, screens and settings:** the `People` menu (employee self-service, manager, HR and payroll screens; POSH visible only to the Committee) and OH10 settings exactly as the OH10 `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - every payroll golden case in Part 8.2 passes to the paisa;
> - a run with anyone below the State minimum wage is blocked; overtime beyond 144 hours a quarter is refused;
> - a resignation with clearance pending still schedules F&F wages for LWD + 2 working days;
> - two synthetic parallel cycles reconcile line by line with the finance reviewer's independent model;
> - no non-HR, non-manager user can see another employee's salary.
>
> Show me the rule-pack parameters, state machines, payslip and register layouts for approval before coding."

### Phase O10 — Internal controls and anti-fraud

> **Instruction to Claude:** "Verify first: (i) Companies Act 2013 s.177(9) with rule 7 of the Meetings of Board Rules 2014 and whether any group company meets the mandatory vigil-mechanism thresholds (otherwise adopt it voluntarily); (ii) internal financial controls reporting (s.134(5)(e), s.143(3)(i)); (iii) Model Standing Orders 2026 misconduct heads on false claims and unauthorised IT access; (iv) my DoA limits (OH11.1 defaults).
>
> On branch `feat/oh-controls-antifraud` build OH11:
>
> - **DoA** per entity and transaction type, routing upward above a limit, every decision with a reason code.
> - **SoD at grant:** vendor creation versus payment release; employee creation versus payroll approval; bank-detail change versus payment release; user administration versus finance roles; exceptions need a director and expire.
> - **Vendor master:** PAN and GSTIN checks; penny-drop name match ≥ 85%; duplicate PAN, account, phone or address; bank-detail change needs a call-back and a 48-hour hold; dormant 12 months blocked.
> - **Expenses, purchase requests and petty cash:** receipt OCR and hash; duplicates; split claims within 7 days; mileage against route distance; weekend flags; cost-centre budgets.
> - **Monthly ghost-employee tests:** shared bank accounts, pay with no sign-in for 30 days, duplicate PAN, no appointment letter or manager, pay after exit, missing UAN.
> - **Access reviews:** privileged quarterly, others half-yearly across the Hub, office suite, GitHub, product staff consoles, cloud and finance tools; revoke after 14 days unattested; `AccessReviewCompleted`.
> - **Whistle-blower channel** to the Audit Committee chair or nominated director: `RECEIVED → TRIAGED → INVESTIGATING → FINDINGS → ACTION → CLOSED`; anti-retaliation second review for 12 months; restricted files.
> - **Staff ROI (team level):** revenue per employee, utilisation, cost per ticket, implementation margin, CAC payback; never the sole basis for discipline. **Intra-group cost sharing** by acting entity, invoiced through OH8.
> - **Menus, screens and settings:** the `Controls` menu (whistle-blower visible only to the designated recipient) and OH11 settings exactly as the OH11 `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - vendor-create plus payment-release on one user is refused without a time-limited director exception;
> - a payment to a vendor account changed less than 48 hours earlier is blocked;
> - two ₹4,900 claims from one person and merchant within 7 days against a ₹5,000 limit are flagged;
> - a seeded ghost employee appears on the monthly exception report;
> - a whistle-blower's identity is hidden from everyone but the designated recipient, administrators included.
>
> Show me the DoA defaults, SoD matrix, exception rules and whistle-blower policy draft for approval before coding."

### Phase O11 — Workplace integration (Microsoft 365 / Google Workspace)

> **Instruction to Claude:** "Verify first: (i) the suite and plan each legal entity holds and the Microsoft 365 Default Geography; (ii) the Graph permissions (`User.ReadWrite.All`, `LicenseAssignment.ReadWrite.All`, `Group.ReadWrite.All`, `Sites.Selected`, Teams and any protected APIs) and Google delegation scopes; (iii) change-notification lifetimes; (iv) whether Advanced Data Residency is needed.
>
> On branch `feat/oh-workplace` build OH12:
>
> - one `WorkplaceProvider` with Microsoft 365 and Google adapters, mock first, then a developer tenant with synthetic users;
> - **joiner:** user disabled until D-1 with `usageLocation` IN, licence from the pool, groups, Teams and drives by role template, `MailboxProvisioned`, idempotent on (employee, provider, action); **mover:** group and licence changes, cross-entity moves through the grant workflow;
> - **leaver at 18:00 on the LWD:** revoke sessions or suspend, block sign-in, shared or forwarded mailbox for 90 days, drive ownership to the manager, retention hold, then licence removal; address quarantined 90 days;
> - delta sync and change notifications renewed at 80% of lifetime, resync on `reauthorizationRequired` or `missed`; Google watch channels renewed before expiry;
> - document links to SharePoint or OneDrive via `Sites.Selected` with retention labels and holds; RESTRICTED HR documents stay in the Hub store; no client regulated data in either suite and no RE or borrower data in Google Workspace;
> - licence pool by entity, idle seats reclaimed after 30 days with manager confirmation; staff and client migration runbooks;
> - DLP that keeps Google Workspace to non-regulated data only (no files with personal data, books of account, returns, loan or HR data);
> - **Menus, screens and settings:** the `Workplace` menu and OH12 settings exactly as the OH12 `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - in the sandbox tenant a leaver's sessions are revoked and sign-in blocked by 18:00 on the LWD, with evidence;
> - re-running a joiner creates no second user or licence;
> - an expired subscription is detected and a delta resync restores state;
> - storing a RESTRICTED HR document, or any file flagged as containing personal data, in Google Drive is refused.
>
> Show me the permission set, role templates and leaver runbook for approval before coding."

### Phase O12 — Engineering-operations console and certification readiness

> **Instruction to Claude:** "Verify first: (i) the Finbyx EO1–EO5 and Udofin RA4 evidence contracts; (ii) the GitHub APIs for rulesets, alerts, environments and members on our plan; (iii) current editions of ISO/IEC 27001:2022 (Amendment 1:2024), 27701:2025, ISO 22301:2019, ISO/IEC 42001:2023, the AICPA Trust Services Criteria (2017, 2022 points of focus) and PCI DSS v4.0.1 SAQ A; (iv) CERT-In reporting and log rules; (v) my certification order, certification body and CPA firm.
>
> On branch `feat/oh-engops-controls` build OH13 and OH14:
>
> - **Console (OH13)** per product and environment: releases, CAB records and freeze windows, vulnerability board with patch clocks (critical or KEV 72 hours, high 7 days, medium 30, low 90), VAPT register (VA 6-monthly, PT yearly, independent testers, retests), backup and DR drills, escrow deposits and CYB para 106 certificates for products serving REs, connector certification, and the incident console with detection, client-notice (≤ 2 hours), CERT-In (6 hours) and DPDP clocks.
> - **Control library (OH14):** controls with owner, frequency, test, automation hook and many-to-many mappings (ISO/IEC 27001 Annex A, 27701, 22301, SOC 2 TSC, PCI SAQ A, CERT-In, DPDP, internal financial controls; CYB, OUT and CF for product controls); evidence with hash, period, reviewer and freshness; collectors for GitHub rulesets, MFA and sign-in reports, access reviews, restore tests, VAPT, patch SLAs, joiner and leaver records, training and vendor due diligence.
> - **Claims gate service** for OH7, product explainers and websites: "aligned to" or "in progress" until a report or certificate exists; then scheme, scope, period or number, issuer and date.
> - **Readiness dashboard, auditor workspace** (time-boxed `PROVIDER_ASSURANCE` grants with `ExternalAccess*` events; Hub evidence only) and **policy library** with attestations (`PolicyAttested` to LawDocsComply in group mode).
> - **CAB and deployment gate:** `ChangeApproved` (OH13 → product deployment gates) for every production change; patch clocks per Part 8.3 on every group repository.
> - **Menus, screens and settings:** the `Engineering` and `Trust` menus and OH13 and OH14 settings exactly as their `Menu and screens` and `Settings and options` subsections specify.
>
> Tests and acceptance evidence:
>
> - a release without an approved change record raises an OH14 exception within 1 hour;
> - a critical vulnerability open beyond 72 hours turns red and notifies the CISO;
> - a VA older than 6 months or PT older than 12 months is flagged 30 days ahead;
> - every control has an owner, a mapping and a collector or manual procedure;
> - website text claiming a certification without a record fails the claims gate.
>
> Show me the control framework, mappings, collectors and console layout for approval before coding."

### Phase OP — Hub go-live

> **Instruction to Claude:** "Verify first: (i) every Appendix B decision the live modules depend on is recorded; (ii) production and every sub-processor pass the India residency check; (iii) notices for staff, candidates, contacts and professionals are approved; (iv) the HR, WFH, DoA, anti-fraud, expenses, whistle-blower and POSH policies the modules enforce are approved.
>
> Deliver: E2E regression across O1–O12, including every screen, empty and error state and setting in Appendix E and an independent WCAG 2.2 AA audit of client-facing and self-service screens; independent VA and PT by a CERT-In-empanelled firm with Critical and High findings closed and retested; a restore drill of database, documents and Temporal state with RTO and RPO measured; **two parallel payroll cycles** on real data reconciled line by line with the current payroll and signed off by the finance reviewer; **one parallel billing cycle** reconciled with current invoices and the books, plus a live Razorpay test invoice paid and refunded; CRM migration with consent provenance (unprovable consent imported as service-only); employee master migration with a reject file; SCIM and leaver automation proven on a real test account; runbooks, on-call rota and a cut-over plan with rollback.
>
> Tests and acceptance evidence:
>
> - VAPT closure and retest report;
> - restore-drill report with measured RTO and RPO;
> - a leaver drill on a real test account showing sessions revoked and product accounts removed within the 4-hour SCIM limit;
> - signed payroll and billing reconciliations;
> - residency and migration reconciliation reports;
> - the go-live checklist with every item evidenced.
>
> Show me the go-live checklist for approval. Do not deploy, send any real payslip, invoice or campaign, or switch off an existing system without my explicit authorisation."

### Phase O13 — Dashboards, analytics and AI assistance

> **Instruction to Claude:** "Verify first: (i) the metric definitions I approve; (ii) the India-region LLM endpoint chosen by ADR and its processing terms; (iii) the AI-use policy approved in OP; (iv) the Part 6.4 rules that cross-entity views are aggregates and Equator data is never joined with lender-side data.
>
> On branch `feat/oh-analytics-ai` build:
>
> - **Metric layer (OH2):** versioned definitions (formula, grain, entity scope, owner, sensitivity) in SQL views under RLS; every tile links to its definition.
> - **Role dashboards:** the Home tiles of Part 3.5 and the OH2.2 catalogue rebuilt on governed metrics (Superset with row-level security), plus leadership and Board packs. Individual metrics only to the employee and manager; group views aggregate-only.
> - **Menus, screens and settings:** `Home`, `Home › Dashboards`, `Home › Leadership packs` and `Admin › Metrics` and OH2 settings exactly as the OH2 `Menu and screens` and `Settings and options` tables specify.
> - **AI assistance with human approval:** ticket triage and replies citing the knowledge base; CRM and proposal drafts; consented meeting summaries; contract and RFP clause extraction; dashboard narratives. **Prohibited:** approving pay, payments, expenses or discounts; hiring, appraisal, discipline or termination decisions; employee monitoring; closing client grievances; publishing without maker-checker; any client regulated data.
> - **Governance:** AI inventory, model and prompt versions, logs without personal data where possible, opt-in per workflow with pause and rollback, monthly quality review; read-only MCP server over aggregate metrics and knowledge-base content.
>
> Tests and acceptance evidence:
>
> - a group dashboard cannot drill into another entity's records;
> - no dashboard places Equator case data beside a lender's revenue;
> - an AI draft cannot be sent without a human action, and the log records model and prompt versions;
> - a PAN-like value is redacted before reaching the model;
> - each metric value recomputes from its stored definition version, and a Board pack shows only approved, versioned metrics.
>
> Show me the metric catalogue, wireframes and AI use-case register for approval before coding."

---

# PART 10 — START NOW

I have connected the GitHub repository for the Infrabyx Operations Hub, and this file is committed at `docs/00-master-prompt.md`, with the Integration Specification at `docs/ecosystem/infrabyx-integration-spec.md`. Do **not** begin by building the Hub.

First, execute **Phase O0 only**:

1. Read this whole file, including the appendices and Sources, and the Integration Specification.
2. Inspect the repository and report its state: files, branch, tooling, constraints.
3. Inventory Infrabyx's current operational tools and data per legal entity.
4. Identify missing business decisions (Appendix B) and the major legal, employee-privacy, residency, fraud, security and integration risks.
5. Propose ADRs: repository structure; legal-entity scoping, grants and the Equator wall; identity federation; rules engine; technology versions; build-versus-buy per module.
6. Prepare the entity model, the event and API boundaries (Part 6), legal register v1, the roadmap with acceptance criteria and the minimum security, testing and review gates.
7. Present the baseline and your questions for my approval **before** modifying the repository.

After approval:

- Create the `docs/oh-repo-baseline` branch.
- Commit only `CLAUDE.md` (from Appendix A), the ADRs, `docs/` and the registers. Application scaffolding belongs to Phase O1.
- Open a pull request.

Throughout development you may ask me as many questions as you need. I will act as project manager; you will architect and build the Hub.

---

# APPENDIX A — CLAUDE.md SEED (keep concise and stable)

```markdown
# Infrabyx Operations Hub (OH) — Claude Code Project Instructions

## What this is
Internal operations platform of the Infrabyx group: dashboards, CRM, client onboarding and
delivery, support and customer success, marketing/brand/social/PR, revenue catalogue and
billing (Razorpay), professional and advocate directory, staff HRMS and payroll, internal
controls and anti-fraud, workplace (M365/Google) integration, engineering-operations console
and certification-readiness control library (modules OH1–OH14). Separate app and repo; never
a product super-admin console. Full brief: docs/00-master-prompt.md.

## Non-negotiables
- Feature branches + PRs only. Never push to main, deploy to prod, touch prod data, send real
  payslips, invoices or campaigns, or rotate live credentials without explicit owner approval.
- Spec → approval → code; plain-English logic first; small commits; never claim an unrun test.
- Every table legal-entity scoped; RLS forced; no context = zero rows. Cross-entity access only
  by approved grants ≤ 90 days; group views aggregate. Equator wall enforced at grant.
- Tenant-level metadata only from products (OH subjects accept at most INTERNAL); no borrower,
  loan, KYC, grievance, governance, risk or client-employee data. Usage = aggregates.
  Our CloudEvents source is urn:infrabyx:oh:[legalentityid]; Hub emits TenantProvisioned and
  ChangeApproved, products acknowledge provisioning by PUT /v1/provisioning-requests/{id}.
- Hash-chained append-only audit; maker-checker and DoA; no self-approval. Money in NUMERIC and
  decimal.js, never floats.
- Labour, tax, GST, DoA and send-gate rules in signed rule packs (Labour Code pack shared with
  Finbyx GV6). F&F wages within 2 working days, never awaiting clearance; deductions ≤ 50%;
  OT with consent, ≤ 144 h a quarter; minimum wage enforced.
- No covert or activity monitoring of staff; AI never decides pay, hiring, discipline or
  grievances; humans approve consequential AI output.
- No portal credentials or OTPs stored; humans file. Razorpay by redirect only; no card data;
  never loan money; webhooks HMAC-verified and de-duplicated. Dunning never stops a product's
  regulated functions, read access or export.
- Directory: BCI Rule 36 fields only; no ratings, badges or paid placement. No certification
  claim before issue (claims gate).
- Data in India; Railway and non-India hosts synthetic only; Google Workspace holds
  non-regulated data only (no personal data, books, returns, loan or HR data).
- Patch SLAs (Finbyx EO1.6): critical/KEV 72 h, high 7 d, medium 30 d, low 90 d.
- Every module ships its Menu and screens and Settings and options (Appendix E): settings
  have a level, default and floor; floors can only be tightened.
- docs/ecosystem/infrabyx-integration-spec.md is canonical; propose events, never invent them.

## Commands
(pnpm install / dev / test / lint / typecheck / db:migrate / db:test — fill in Phase O1)

## Where things live
docs/00-master-prompt.md, docs/ecosystem, docs/architecture, docs/adr, docs/specs,
docs/data-model, docs/api, docs/integrations, docs/compliance (legal register, controls map),
docs/privacy, docs/security, docs/testing (golden cases), docs/ops, docs/policies, docs/status.

## Definition of done
Acceptance criteria met; unit/integration/E2E/entity-isolation/Equator-wall/security tests run
and passed; golden pay and billing cases pass to the paisa; audit chain verifies; privacy
notice, retention and DPIA in place; docs and registers updated; diff reviewed for secrets/PII.
```

---

# APPENDIX B — BUSINESS DECISIONS THE PROJECT OWNER MUST TAKE

Claude Code should confirm these in Phase O0:

1. **Office suite actually held** per legal entity: Microsoft 365 Business Basic, Business Standard or Business Premium (Microsoft has no "Business Starter"; that name is a Google Workspace edition) or Google Workspace Business Starter or higher; Default Geography India; Advanced Data Residency for all eligible seats; whether to consolidate on one suite. Default until decided: both adapters available; Google Workspace (no India data region) holds non-regulated data only, with no personal data, books of account, returns, loan or HR data.
2. **Razorpay merchant-of-record entity** per product and service line, its GST registrations, settlement and Smart Collect accounts, and signatory.
3. **Revenue-recognition framework** per selling entity (AS 9 or Ind AS 115) and the books of record (Tally Prime or Zoho Books).
4. **Plan tiers and SKUs** for Finbyx, Udofin (B2B), LawDocsComply, LawDocs and LawDocs Trainings: meters, AUM bands, seats, implementation milestones, support tiers, terms, discount authority.
5. **CRM build versus Brevo-first:** Hub as system of record with Brevo for sending (recommended for ownership and portability), Brevo Sales CRM first, or another CRM after the O0 benchmark; Brevo hosting and DLT support.
6. **Payroll in-house versus provider:** Hub engine (OH10) or a provider with the Hub as HRMS and controls layer; first live cycle and parallel-run months.
7. **Work-from-home policy:** eligibility, core hours, sign-in and sign-out method, timesheet granularity, equipment and expenses, security rules; confirmation that no activity or screen monitoring is used.
8. **Directory public listing scope:** professional types listed, group websites that show the listing (for example lawdocs.in), consent wording.
9. **Group cost-sharing and intra-group agreements:** employer of shared staff, services agreement and DPA, allocation keys, GST on cross-charges, arm's-length evidence.
10. **Certification order and auditors:** ISO/IEC 27001 or SOC 2 Type 1 first; whether the Hub is in scope; certification body and CPA firm; SOC 1 Type 2 for Finbyx.
11. **JioCX contract** for Infrabyx's own communications, subject to API documentation, DPA, India residency and DLT support; fallback provider.
12. **Social platforms** per brand, company-owned accounts and approval authority.
13. **Data retention per record class:** inactive contacts, tickets, recordings, candidates, ex-employee records, payroll registers (≥ 5 years after the last entry, Wages (Central) Rules r.51), billing records forming part of books (≥ 8 years, Companies Act s.128(5)), whistle-blower and POSH files, audit evidence.
14. **Legal entities, employers and offices** covered at launch (decides Labour Code, S&E, PT, LWF and POSH duties).
15. **Hosting** (Supabase ap-south-1 or AWS ap-south-1 and ap-south-2 from day one; Temporal self-hosted or cloud) and **GitHub plan** (Team or Enterprise Cloud).
16. **Vigil mechanism, POSH and DPO:** voluntary s.177(9)-style mechanism and its recipient; Internal Committees per office of 10 or more; group DPO; DPDP readiness date (13 May 2027 unless brought forward).
17. **Rule-pack ownership:** who maintains the shared Labour Code pack and approves State-table updates.
18. **Default settings sign-off:** approve the commercial defaults in Appendix E.3 (SLA matrix, renewal timings, health weights, gift threshold, campaign pause thresholds, session timeouts); floors are not open to change.
19. **Notification channels:** Teams or Google Chat for staff alerts, on-call SMS provider for Sev 1, and quiet hours per entity.

---

# APPENDIX C — STARTING REPOSITORY STRUCTURE (to be refined in Phase O0)

```
infrabyx-ops-hub/
├─ apps/
│  ├─ web/             # Next.js: Hub workspaces, employee self-service, client billing and support portal
│  ├─ api/             # NestJS modular monolith (HTTP, webhooks, SCIM, catalogue and entitlement APIs)
│  ├─ worker/          # Temporal workers, schedulers, outbox relay, evidence collectors
│  └─ directory-feed/  # read-only Rule 36 directory API for group websites
├─ modules/            # each: domain/, application/, infra/, api/, tests/
│  ├─ group-identity/ (OH1)   ├─ dashboards/ (OH2)        ├─ crm/ consent-sendgate/ (OH3)
│  ├─ onboarding-delivery/ migration-factory/ (OH4)       ├─ customer-success/ (OH5)
│  ├─ support-desk/ knowledge-base/ (OH6)                 ├─ marketing-brand/ social-pr/ (OH7)
│  ├─ revenue-catalogue/ billing/ payments-razorpay/ revenue-review/ (OH8)
│  ├─ directory/ (OH9)        ├─ hrms/ payroll/ attendance-leave/ performance-learning/ statutory-filing/ (OH10)
│  ├─ controls/ whistleblower/ (OH11)                     ├─ workplace/ documents/ (OH12)
│  ├─ engops-console/ (OH13)  ├─ control-library/ claims-gate/ (OH14)  └─ analytics/ ai-assist/ (O13)
├─ packages/
│  ├─ contracts/ (generated from infrabyx-contracts)   ├─ domain-kernel/ (Money, dates, calendars, IDs)
│  ├─ rule-packs/ (shared labour-code pack, state tables, doa, send-gate, gst-sac, retention, claims lexicon)
│  ├─ adapters/ (brevo, razorpay, msgraph, google-workspace, github, social, jiocx, epfo-ecr, esic,
│  │             traces, pt-lwf, gst-gsp, einvoice-irp, tally, zoho-books, esign, bank-payout)
│  ├─ platform-ux/ (settings registry, notification engine, permission-trimmed search, saved views, app shell)
│  └─ ui/  config/  observability/  testing/ (synthetic data, golden cases)
├─ db/ (migrations/, rls-policies/, seeds/ synthetic only)
├─ infra/ (docker, compose, opentofu or terraform, railway for dev and staging, aws or supabase for prod-in)
├─ docs/ (Part 8.4; docs/ecosystem/infrabyx-integration-spec.md is canonical)
└─ CLAUDE.md
```

---

# APPENDIX D — INITIAL ENTITY MODEL (starting list)

Every business entity carries `id` (prefix + ULID), `legal_entity_id`, `version` and timestamps; client-related entities carry `client_org_id`; RESTRICTED entities carry `sensitivity`. Key attributes are specified where each entity is defined: group_grant (OH1.1, Part 6.4), audit_event (Part 7.2 principle 19), consent and send_evaluation (OH3.3–OH3.4), provisioning_order and exit_case (OH4.1, OH4.6), pay_line, fnf_case and statutory_filing (OH10 and Part 8.2), vendor and expense controls (OH11). Names follow the module data models; where a module renames an entity, the module wins and this list is updated in the same pull request.

- **Platform (all modules):** maker_checker_request, doa_rule, audit_event, audit_chain_anchor, outbox_event, inbox_event, idempotency_key, dlq_item, rule_pack_version, setting_definition, setting_value, notification_type, notification, notification_preference, saved_view, search_index_entry, retention_class, legal_hold, disposal_certificate, data_principal_request, notice_version, dpia_record.
- **OH1 Group identity:** legal_entity, gst_registration, office, state_calendar, department, cost_centre, person, employment, user_account, role, permission, group_grant, grant_use_log, purpose_code, sod_conflict_rule, scim_target, break_glass_record, case_party_block, relationship, conflict_check_log, equator_wall_event, client_org, client_contract.
- **OH2 Dashboards:** metric_definition, metric_value, dashboard, tile, home_layout, board_pack_run.
- **OH3 CRM:** crm_object_schema, account, contact, lead, opportunity, pipeline, activity, task, partner, consent, dnd_status, dlt_template, segment, send_evaluation, brevo_sync_state, import_job, merge_candidate, export_job, crm_request.
- **OH4 Onboarding and delivery:** onboarding_case, provisioning_order, provisioning_gate_evidence, implementation_project, milestone, raid_item, change_request, timesheet_entry, migration_programme, migration_run, workplace_migration, exit_case.
- **OH5 Customer success:** health_snapshot, success_plan, qbr, renewal, expansion_opportunity, churn_risk, survey, survey_response.
- **OH6 Support:** ticket, ticket_event, sla_policy, sla_clock, escalation, scoped_session, dlp_finding, problem, kb_article, client_complaint, re_escalation, misrouted_complaint, incident_link.
- **OH7 Marketing:** brand, brand_asset, content_item, claim, campaign, campaign_audience_snapshot, publish_job, channel_account, social_inbox_item, influencer_engagement, media_contact, press_release, coverage, collaboration, event, gift_hospitality, ad_campaign.
- **OH8 Revenue and billing:** selling_entity, product, sku, plan, price_book, price, revenue_stream, stream_gate, catalogue_version, quote, order, contract, subscription, entitlement, usage_aggregate, usage_dispute, invoice, credit_note, debit_note, receipt, mandate_ref, webhook_event, settlement_recon, tds_receivable, dunning_case, revenue_schedule, journal_export_batch, intra_group_recharge, experiment, revenue_scenario.
- **OH9 Directory:** professional, credential, verification, practice_area, jurisdiction, empanelment, listing, directory_query_log, conflict_declaration, matter_allocation, suspension_record.
- **OH10 HRMS and payroll:** requisition, candidate, offer, appointment_letter, employee, employment_event, attendance_record, timesheet, wfh_arrangement, leave_balance, leave_request, payroll_run, pay_line, wage_computation, statutory_deduction, overtime_record, payslip, register_snapshot, bank_file, fnf_case, gratuity_computation, statutory_filing, tax_declaration, goal, appraisal, training_record, posh_committee, posh_case, policy_acknowledgement.
- **OH11 Controls:** sod_exception, vendor, vendor_bank_change, vendor_verification, purchase_request, expense_claim, expense_flag, petty_cash_account, integrity_test_run, exception_item, access_review_campaign, access_attestation, whistleblower_report, investigation, anti_retaliation_flag, roi_metric, cost_allocation.
- **OH12 Workplace:** workplace_tenant, licence_pool, licence_assignment, mailbox, role_template, provisioning_step, change_subscription, delta_token, document_link, dlp_rule.
- **OH13 Engineering operations:** repository, product_environment, release, change_record, cab_meeting, freeze_window, vulnerability, vulnerability_exception, vapt_engagement, finding, backup_run, restore_test, dr_drill, escrow_deposit, security_certificate, connector_certification_status, incident, incident_clock, status_page_notice.
- **OH14 Control library:** framework, requirement, control, control_requirement_map, collector, evidence, test_result, exception, soa_entry, cuec, csoc, audit_period, policy, policy_attestation, certification, claims_lexicon_entry, claims_check_result, auditor_workspace_grant.

---

# APPENDIX E — NAVIGATION, MENUS, SCREENS AND SETTINGS MAP

This appendix consolidates the `Menu and screens` and `Settings and options` subsections of OH1–OH14 and the common rules of Part 3.5. Module sections prevail on detail (screens, actions and roles per path); a change to either is made in the same pull request.

## E.1 Sidebar tree

| Menu | Submenus (path `Menu › Submenu`) | Module |
|---|---|---|
| Home | My queue · Dashboards · Leadership packs · Notifications · Saved views | OH2 |
| Clients | Client list · Client 360 (Overview, Contacts, Contracts and plans, Onboarding, Success, Support, Invoices, Timeline, Documents) | OH3 |
| CRM | Leads · Opportunities · Activities and tasks · Partners · Segments and consent · Imports · Exports · Brevo sync · Merge queue | OH3 |
| Onboarding | Cases · Provisioning · Projects · Migration · Workplace migrations · Exits · Templates | OH4 |
| Success | Portfolio · Accounts · Renewals · Churn risk · Surveys · Expansion | OH5 |
| Support | My queue · Triage · Tickets · Problems · Knowledge base · Client complaints · RE escalations · Misrouted complaints · Policies | OH6 |
| Marketing | Calendar · Content · Campaigns · Social · PR · Collaborations and events · Influencers · Brand library · Registers | OH7 |
| Revenue | Catalogue · Plans · Quotes · Subscriptions · Invoices · Collections · Revenue review | OH8 |
| Directory | Professionals · Empanelment · Allocations · Equator partition (Equator panel administrators only) | OH9 |
| People | My profile (employee self-service, Part 7.5: payslips, Form 130, leave, attendance, timesheets, expenses, declarations) · Directory · Hiring · Onboarding · Leave · Attendance and WFH · Payroll · Appraisal · Exits · POSH (restricted) | OH10 |
| Controls | DoA · Maker-checker queue · Access reviews · Vendors · Analytics · Whistle-blower (restricted) | OH11 |
| Workplace | Mailboxes · Groups · Sites · Migration · Residency | OH12 |
| Engineering | Releases · Changes · Vulnerabilities · VAPT · Backups · Incidents · Status page | OH13 |
| Trust | Controls · Evidence · Audits (audit periods, auditor portal, provider-assurance grants, certification register) · Policies · Claims gate | OH14 |
| Admin | Legal entities · Offices and calendars · Org structure · Users · Roles · Grants · Purpose codes · Equator wall · Break-glass · Audit log · Settings · Notification templates · Integrations · Rule packs · Retention and legal holds · Metrics | OH1, platform |

External portals sit outside the sidebar: client support and implementation portal (OH4, OH6), client billing pages inside each product (Finbyx CM2.2; Udofin RV2.2), professional portal (OH9), auditor portal (OH14), employee self-service (People › My profile, also on mobile web).

## E.2 Role visibility by workspace

**F** = full (create, edit, approve within DoA), **W** = work own queue or records, **R** = read, **A** = aggregate only, **–** = hidden. Entity scope, grants and the Equator and LawDocsComply walls apply on top; RESTRICTED submenus (POSH, Whistle-blower, salary fields) are visible only to their named holders whatever the letter.

| Menu | A Lead. | B Deliv. | C Onb. | D CS | E Supp. | F–H Mktg | I Sales | J Fin. | K HR | L Sec. | M Legal | O Audit | P Admin |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Home | F | F | F | F | F | F | F | F | F | F | F | F | F |
| Clients | R | R | W | W | R | R | W | R | – | – | R | R | – |
| CRM | A | – | R | R | – | W | F | – | – | – | – | R | – |
| Onboarding | R | F | F | R | R | – | R | R | – | – | R | R | – |
| Success | R | R | R | F | R | – | R | R | – | – | – | R | – |
| Support | R | R | R | R | F | – | R | – | – | R | R | R | – |
| Marketing | R | – | – | – | – | F | R | – | – | – | R | R | – |
| Revenue | F | R | R | R | – | – | W | F | – | – | R | R | – |
| Directory | R | – | – | – | – | – | – | – | – | – | F | R | – |
| People | A | W | W | W | W | W | W | W | F | W | W | R | W |
| Controls | F | W | W | W | W | W | W | F | W | W | W | R | W |
| Workplace | – | – | – | – | – | – | – | – | R | F | – | R | F |
| Engineering | R | R | – | – | R | – | – | – | – | F | – | R | R |
| Trust | R | – | R | – | – | R | R | – | – | F | R | R | – |
| Admin | R | – | – | – | – | – | – | – | – | R | – | R | F |

Notes: People and Controls show **W** for self-service (own leave, payslips, expenses, access attestations of one's reports); workspace N (group-company users) receives the same letters within its own legal entity; Equator staff never see Clients, CRM, Success or Revenue records of a party on the case-party block list.

## E.3 Settings catalogue (highlights; module tables are complete)

| Area | Setting | Default | Floor or ceiling | Nature |
|---|---|---|---|---|
| Identity (OH1) | Cross-entity grant maximum | 90 days | Never longer | Floor |
| Identity (OH1) | Leaver disable | 4 h; privileged 1 h; access off by 18:00 on the LWD | Never longer | Floor |
| Identity (OH1) | MFA | All; FIDO2 privileged | Always on | Floor |
| Identity (OH1) | Conflict look-back | `P3Y` | Never shorter | Floor |
| Dashboards (OH2) | Individual metrics | Person and manager only | No league tables | Floor |
| CRM (OH3) | Promotional opt-out re-consent wait | 90 days | Never shorter | Floor |
| CRM (OH3) | Sending window | 09:00–19:00 IST | May only narrow | Floor |
| Onboarding (OH4) | Production gate | MSA, DPA, OUT clause matrix, registration | Always | Floor |
| Onboarding (OH4) | Reconciliation tolerance | Zero on counts and principal; ₹1 interest per loan | Client may tighten | Floor |
| Success (OH5) | Price-change notice | 30 days | Never shorter | Floor |
| Support (OH6) | Clock pause | Only waiting on client | Fixed | Floor |
| Support (OH6) | Misrouted borrower-complaint forwarding | 1 working day | Never longer | Floor |
| Marketing (OH7) | Claims lexicon | OH7.5 list | Entities may add | Floor |
| Revenue (OH8) | Dunning effect on regulated functions, read and export | None | Fixed | Floor |
| Revenue (OH8) | Recurring-debit courtesy notice | T−48 hours | Issuer notice ≥ 24 h is separate | Commercial |
| Directory (OH9) | Listing fields and ordering | Rule 36 Schedule fields; randomised order | No ranking or paid placement | Floor |
| People (OH10) | Final wages | LWD + 2 working days | Never later | Floor |
| People (OH10) | Overtime | With consent; ≤ 144 h a quarter | Never higher | Floor |
| People (OH10) | Monitoring | Sign-in and sign-out, timesheets | No activity, screen, webcam or off-duty location | Floor |
| Controls (OH11) | Vendor bank-detail change hold | 48 hours with call-back | Never shorter | Floor |
| Controls (OH11) | Unattested access revocation | 14 days | Never longer | Floor |
| Workplace (OH12) | Google Workspace content | Non-regulated only | No personal, books, returns, loan or HR data | Floor |
| Engineering (OH13) | Patch SLAs | 72 h, 7 d, 30 d, 90 d | Stricter contract wins | Floor |
| Engineering (OH13) | Incident clocks | RE notice ≤ 2 h; CERT-In 6 h | Never longer | Floor |
| Trust (OH14) | Certification claims | Blocked until report or certificate issued | Fixed | Floor |
| Platform | Session idle timeout | 30 min; privileged 15 min | Entities may shorten | Commercial |
| Platform | Notification digest and quiet hours | Daily digest 09:00; quiet 20:00–08:00 | Mandatory categories exempt | Personal |

## E.4 Notification catalogue

| Notification | Trigger | Recipients | Channel | Mandatory |
|---|---|---|---|---|
| Approval waiting | Maker-checker or DoA item assigned | Approver; escalates to deputy after 1 working day | In-app, email, Teams or Chat | Yes |
| Grant expiring or revoked | T−14 days; revocation | Holder, manager, approvers | In-app, email | Yes |
| SLA warning and breach | 50% and 75% of a ticket clock; breach | Assignee, team lead; on breach the escalation ladder | In-app, Teams or Chat; Sev 1 SMS to on-call | Yes |
| Regulatory deadline at risk | Ticket `regulatory_impact` within 3 or 1 working days | Assignee, head of support, account owner | In-app, email, Teams or Chat | Yes |
| Incident clock | Detection; 60 and 90 minutes into the 2-hour RE notice; 4 and 5 hours into the CERT-In 6 hours | Incident commander, CISO, product head | In-app, Teams or Chat, SMS | Yes |
| Provisioning acknowledgement overdue | No acknowledgement in 1 working day | Onboarding coordinator | In-app, email | No |
| Milestone awaiting client acceptance | Milestone submitted; reminder every 3 working days | Client approver, implementation manager | Portal, email | No |
| Renewal and price-change notices due | T−120, T−90, T−60, T−30, T−7 | CSM, account owner | In-app, email | Yes for notice dates |
| Health dropped to red | Band change | CSM; leadership for top-tier accounts | In-app, email | No |
| Detractor response | NPS 0–6 | CSM | In-app | No |
| Send-gate refusals | Audience freeze or send with refusals | Campaign owner | In-app | No |
| Claims-gate block | Content or explainer blocked | Author, reviewer | In-app | No |
| Payment failed or dunning stage | Razorpay failure; stage change | Finance, account owner | In-app, email | Yes |
| Usage dispute raised | Dispute received | Billing operations | In-app, email | Yes |
| Credential expiring | 60 and 30 days before expiry | Professional, directory administrator | Portal, email | Yes |
| Payroll variance or block | Variance above ± 10% per head; minimum-wage block | Payroll lead, finance reviewer | In-app, email | Yes |
| Final-settlement clock | LWD; LWD + 1 working day | HR, payroll | In-app, email | Yes |
| Leave or timesheet action | Request submitted; timesheet due | Manager; employee | In-app, Teams or Chat | No |
| Vendor bank-detail change | Change requested | Finance controller, vendor owner | In-app, email | Yes |
| Access review due | Campaign opened; T−3 days | Reviewers | In-app, email | Yes |
| Vulnerability past SLA | Clock breach | Repository owner, CISO | In-app, email | Yes |
| Evidence stale | Freshness window passed | Control owner | In-app | No |
| Policy attestation due | New version published | Affected staff | In-app, email | Yes |

Bodies carry the record type, reference and action link only; never RESTRICTED data, salary, case details or client regulated data.

---

## SOURCES CONSULTED FOR THIS PROMPT (for Claude Code to re-verify)

- **Labour Codes and employment:** EY alert on the Central Rules (10 May 2026) https://www.ey.com/content/dam/ey-unified-site/ey-com/en-in/technical/alerts-hub/documents/2026/05/final-rules-published-by-central-government-under-new-labour-codes.pdf ; MoLE FAQs (Jan 2026) https://www.labour.gov.in/static/uploads/2026/01/de4758d5bfeffc456d7de97a801891b0.pdf ; Wages (Central) Rules 2026 guide https://www.taxmann.com/post/blog/wages-central-rules-2026-code-on-wages-chapter-wise-guide ; final wages in two working days https://www.livelaw.in/articles/two-working-days-code-wages-employee-final-settlement-552780 ; OSH Code and Central Rules FAQs https://acuitylaw.co.in/md/faqs/faqs-on-the-occupational-safety-health-and-working-conditions-code-2020-and-the-occupational-safety-health-and-working-conditions-central-rules-2026/ ; Model Standing Orders 2026 https://www.jsalaw.com/wp-content/uploads/2026/05/JSA-Prism-Employment-May-2026-MSO.Final_.pdf ; EPF wage ceiling https://ksandk.com/newsletter/employees-provident-fund-compliance-update-%E2%82%B915000-wage-ceiling-officially-notified-under-the-code-on-social-security-2020/ ; ESIC contributions https://web.esic.gov.in/web/esic/contribution ; Uttar Pradesh S&E https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/uttar-pradesh-enhances-coverage-for-employees-and-applicability-limits-for-registration-of-commercial-establishments ; Rajasthan S&E https://ksandk.com/newsletter/rajasthan-eases-registration-for-small-establishments/
- **Tax:** Form 130 FAQs https://www.incometaxindia.gov.in/documents/d/guest/form-130-faqs ; Form 16 and Form 130 https://www.scconline.com/blog/post/2026/06/15/overview-comparison-of-form-16-and-form-130-tds-certificate/ ; Form 140 https://www.incometaxindia.gov.in/documents/d/guest/fn-140 ; e-invoicing threshold https://bhattandjoshiassociates.com/e-invoicing-threshold-limit-of-rs-5-crore-analyzing-the-digital-divide-between-tier-1-and-tier-3-businesses/ ; GSP overview https://gstzen.in/a/gsp-gst-suvidha-providers.html ; TallyPrime JSON https://help.tallysolutions.com/tally-prime-integration-using-json-1/
- **Privacy, cyber, corporate:** DPDP Rules 2025 https://www.khaitanco.com/sites/default/files/2025-11/ERGO%20-%20Digital%20Personal%20%20Data%20Protection%20Rules%20-%2015%20November%202025.pdf ; DPDP timeline proposal https://ssrana.in/articles/meity-plans-to-cut-short-dpdp-compliance-timeline-and-notify-cross-border-restrictions-for-sdfs/ ; CERT-In Directions (28 Apr 2022) https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf ; Board Powers Rules r.7 https://ca2013.com/rule-7-companies-meetings-of-board-and-its-powers-rules2014/ ; books of account and India backup https://www.grantthornton.in/insights/blogs/recent-amendments-by-mca-in-keeping-of-books-of-accounts
- **RBI payment rules:** E-mandate Framework Directions 2026 https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13374 ; Payment Aggregator Directions 2025 https://www.rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=61218 ; card tokenisation circular https://rbi.org.in/Scripts/NotificationUser.aspx?Id=12159&Mode=0 ; RBI (NBFC – Managing Risks in Outsourcing) Directions 2025 (RBI/DOR/2025-26/363, 28 Nov 2025), RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions 2026 (RBI/DoS/2026-27/461, 31 Jul 2026), RBI (NBFC – Credit Facilities) Directions 2025 (RBI/DOR/2025-26/347, 28 Nov 2025) and RBI (NBFC – Responsible Business Conduct) Directions 2025 (RBI/DOR/2025-26/362), all at https://www.rbi.org.in
- **Telecom, advertising, advocates:** TRAI PR 11/2025 https://cms.trai.gov.in/sites/default/files/2025-02/PR_No.11of2025.pdf ; TRAI 1600-series Direction (19 Nov 2025) https://www.trai.gov.in/sites/default/files/2025-11/Direction_19112025_0.pdf ; TRAI clarification (10 Jul 2026) https://www.scconline.com/blog/post/2026/07/18/trai-clarifies-1600-and-140-series-number-framework/ ; 1600 and 1601 numbers https://exotel.com/blog/1600-phone-number/ ; financial advertising https://www.barandbench.com/law-firms/view-point/the-viewpoint-advertising-of-banking-and-financial-offerings-limitations-and-requirements-under-indian-law ; BCI Rule 36 https://www.scconline.com/blog/?p=327018
- **Office suites:** M365 data residency https://learn.microsoft.com/en-us/microsoft-365/enterprise/m365-dr-product-terms and https://learn.microsoft.com/en-us/microsoft-365/enterprise/advanced-data-residency ; Graph change notifications https://learn.microsoft.com/en-us/graph/change-notifications-overview ; assignLicense https://learn.microsoft.com/en-us/graph/api/user-assignlicense ; Teams protected APIs https://learn.microsoft.com/en-us/graph/teams-protected-apis ; Google credentials and delegation https://developers.google.com/workspace/guides/create-credentials ; Google data regions https://knowledge.workspace.google.com/admin/compliance/data-covered-by-data-regions
- **Vendors:** Brevo https://developers.brevo.com/docs/getting-started and https://developers.brevo.com/docs/api-limits ; Razorpay webhooks https://razorpay.com/docs/webhooks/validate-test/ and compliance claims https://razorpay.com/blog/payment-gateway-compliance/ ; Jio Business https://www.jio.com/business/ ; JioCX https://www.jio.com/business/services/jiocx/ ; Jio DRHP AI disclosures https://www.medianama.com/2026/06/223-jio-drhp-ai-disclosures-ahead-ipo/
- **Engineering and certification:** GitHub rulesets https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets ; artifact attestations https://docs.github.com/en/actions/security-for-github-actions/using-artifact-attestations/using-artifact-attestations-to-establish-provenance-for-builds ; Trust Services Criteria https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022 ; ISO/IEC 27701:2025 https://www.dnv.com/news/2025/iso-iec-27701-standard-update-release/ ; PCI DSS v4.0.1 SAQ A https://blog.report-uri.com/pci-dss-4-0-1-saq-a-and-client-side-security-a-plain-english-faq/
- **Funnel reference:** ptstdm.co.in, a coaching workshop funnel reviewed on 23 Oct 2026 and not a model to copy https://www.ptstdm.co.in
- **Statutes (official text on India Code, https://www.indiacode.nic.in):** Digital Personal Data Protection Act 2023; Information Technology Act 2000 s.70B; Arbitration and Conciliation Act 1996 (s.12, Fifth to Seventh Schedules); Mediation Act 2023; Advocates Act 1961 s.35; Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act 2013 (ss.4, 16, 21); Prevention of Corruption Act 1988 s.9; Companies Act 2013 (ss.128, 134, 143, 177); Code on Wages 2019, Industrial Relations Code 2020, Code on Social Security 2020 and OSHWC Code 2020; Income-tax Act 2025; CGST and IGST Acts 2017. Bar Council of India Rules, Part VI Chapter II: https://www.barcouncilofindia.org ; TRAI TCCCPR 2018 and amendments: https://www.trai.gov.in
- **Group documents:** Infrabyx Ecosystem Integration Specification v1.1 (24 October 2026; Parts 3.2, 4.6, 6.15–6.29, 12.1, 12.3, 13.2, 14.2); Finbyx Master Build Prompt v1.5 (Parts 7D AU4.3, 7F, 7J, 7K, 7L EO1.6, 10, 11); Udofin Master Build Prompt v1.2 (Parts 7B, 7G, 7H).

*End of master prompt.*
