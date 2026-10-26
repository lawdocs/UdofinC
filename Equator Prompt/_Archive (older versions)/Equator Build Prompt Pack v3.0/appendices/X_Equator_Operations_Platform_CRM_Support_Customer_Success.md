# Appendix X — Equator Operations Platform: CRM, Onboarding, Customer Success, Support and Grievance (v3.0, 23 October 2026)

## X.0 Purpose, sources, precedence

**What this appendix does.** It specifies the **Equator Operations Platform (EOP)**: the separate application (`apps/ops`) and login portal (Keycloak client `eq-portal-ops`) in which Equator's own staff run the business — leadership oversight, case-services delivery tracking, onboarding and implementation, customer success, after-sales service, support tickets, Equator's own grievance redressal, finance-operations views, training and marketplace operations, the knowledge base, cross-functional task queues and the **CRM**. It also specifies the **automation engine** ("autopilot") that every EOP department uses and that Appendix Y uses for marketing-specific automations, the openness rules (NN-40) for Brevo and other CRMs, and the Microsoft 365 hooks for operations staff. Phase **P16** implements it.

**What EOP is not.**

| Not this | Why | Where it lives |
|---|---|---|
| The technical super-admin console | Platform administration (tenants, flags, provider circuits, elevations) needs JIT elevation and aal3; business staff must never hold it (D3-02) | `admin.equatorresolution.in` (Appendix S §2, SCR-S-D12) |
| The case-management console | Case administration (scrutiny, notices, clocks, hearings) is governed by the institutional rules and the neutrality firewall | `/console` (Appendix S SCR-S-D05/D06) |
| Tenant consoles | Lenders, insurers, employers, Chambers and GRM/POSH buyers administer their own organisations | P09, P10 |
| The marketing studio | Campaigns, social calendar, PR, brand assets and partnerships content | Appendix Y (`mkt` schema); EOP supplies the CRM, consent, segments and the automation engine Y runs on |
| The HRMS and payroll | Employee files, attendance, leave, payroll, appraisal | v3 workforce specification (`hr`, `pay` schemas); EOP reads only the staff directory projection it needs for assignment |
| A ledger | No journal entry, invoice, credit note, refund or payout is created or edited in EOP (NN-36) | P05 `billing`/`payments`; EOP shows read models and hands off |

**Sources.** Research: [RB] business models, revenue streams and the automation catalogue AU-01…AU-26 (§5, design implication F); [RD] Microsoft 365 (F1, DI-A), Brevo API v3 (F3.1, DI-B), portable exports (DI-C), governed/configurable/OFF summary (DI-H); [RE] marketplace law (F3), group data sharing (F4.4, F5) and design implication E. Pack: master §3 (NN-01–NN-40), §4 (architecture), §15 (X-01–X-42); `02` decision log; Appendix S (identity, portals, RBAC, §1.3 workforce identities, §2.6 staff portal, §6 RBAC/ABAC); Appendix O (revenue streams §1.2, entitlements §4, dunning §7); Appendix Q (privacy control set, DSR SLAs §2.4, retention §2.8, compliance-as-code §7); Appendix U §U.6.4 (Grievance Redressal Policy EGP-2026.1) and §U.4 (staff code ESC-2026.1); Appendix H §3 (GTM-implied features G-13, G-36, G-38); P09 (enterprise consoles, GRM engine); P13 (mini-CRM FR-P13-19, consent hooks FR-P13-22, neutrality firewall FR-P13-26); Appendix D §D.9 (`CRM_PORT`). v3 companions: the configuration framework (NN-33 tiers; P15), Appendix Y (marketing), Appendix AB (revenue stream registry, `rev`), Appendix AC (workspace port, `WORKSPACE_PORT`), Appendix AD (group companies, cross-company grants, GDSA; `grp`).

**Precedence.** Master and `02` → Appendix G (law) → Appendix B (fees) → Appendix F (names, types, events, codes; this appendix registers new `OPS_*` codes for F §F.10.4) → Appendix A (states and clocks) → the phase being executed (P16) → this appendix → other appendices. Where this appendix and Appendix Y overlap, **X governs the automation engine, CRM objects, consent and preference storage, segments and the Brevo CRM/contact connector; Y governs marketing automations, campaign objects, the social calendar, PR and partnership content and the Brevo campaign (`MARKETING_PORT`) connector** (D3-23).

### X.0.1 New requirements (add to `02` §2)

| # | Requirement (management brief, 23 Oct 2026) | Where | Type |
|---|---|---|---|
| R-51 | A separate Operations Platform (not the super-admin console) for operations, service delivery, after-sales, onboarding, customer success, support tickets and grievance redressal, with department workspaces and dashboards (brief item 3, 10) | App. X §X.1–§X.9; P16 | S |
| R-52 | A CRM that is open to Brevo and other tools, with integration and migration in both directions (brief item 3; NN-40) | App. X §X.4, §X.10; P16 | S |
| R-53 | "Autopilot" automation for operations with human approval for sensitive actions (brief item 7; Expanded Prompt) | App. X §X.12; P16 | S |
| R-54 | Group-ready operations: staff working cross-functionally for Finbyx and Udofin, dashboards and content shareable under controls; Microsoft 365 for ops staff (brief items 5, 11) | App. X §X.2.4, §X.11; P16; App. AD | S |

### X.0.2 New decisions (add to `02` §3)

| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| D3-20 | **EOP data plane.** All EOP business data lives in schema `ops` in the isolated **business database** (the P13 growth database, extended; `growth`, `ops` and `mkt` co-located; no grants on case, sealed, `hr` or `pay` schemas). EOP reads core data only through allow-listed read models (§X.2.3) | NN-16, NN-38; P13 FR-P13-26 | §X.2.2; X-50 |
| D3-21 | **Equator's own user grievances run on the P09 GRM engine** as variant `EQ_SERVICE` inside the Equator institution tenant, surfaced in the EOP Support and Grievance workspace; support tickets are a separate object (`ops.tickets`) that converts to a grievance on defined triggers | Reuse of a clock-safe engine; EGP-2026.1 | §X.8; X-52 |
| D3-22 | **Declared systems of record.** The Equator CRM (`ops`) is the system of record for accounts, contacts, leads, opportunities, consent preferences (mirrored to `core.consent_records`), tickets and implementations; Brevo is system of record only for raw email-engagement events it generates; `billing` remains system of record for plans, subscriptions, invoices and receivables. No external tool is ever system of record for consent | NN-40; RD DI-B | §X.10.1 |
| D3-23 | **Automation engine ownership.** Appendix X owns the no-code automation engine (`ops.automations`), its trigger/condition/action catalogue, permissions, preview, rate limits, exception paths, audit, pause/rollback and the **locked human-approval list**; Appendix Y owns marketing automations built on it | Management brief item 7; RB §F | §X.12 |
| D3-24 | **Commercial-to-case firewall.** Case-administration roles (`case_manager`, `registrar`, `deputy_registrar`, `case_counsel`, `quality_officer`, panel and committee roles) and neutrals never see an account's revenue, health score, renewal date, churn risk, discounts or pipeline; EOP sees case services only as a **metadata projection** (no evidence, pleadings, party names, offers, outcomes) | NN-03, NN-16, NN-28; RB AU-12 "aggregate only" | §X.3.3, §X.14 |

### X.0.3 Cross-file resolutions (add to master §15)

| # | Topic | Resolution |
|---|---|---|
| X-50 | `ops` schema meaning | From v3.0 schema `ops` means the **business Operations Platform** only (D3-20), hosted in the isolated business database. The v2.1 platform-assurance tables that Appendix Q §2/§7.2 and P14 placed in `ops` move to `eng` in the core database with unchanged names, as Appendix AE X-65 specifies (incl. `ops.security_findings` → `eng.vulnerabilities` with alias, `ops.processed_events` → `core.processed_events`); RD's `ops.jml_events` is `hr.jml_events` (Appendix Z Z-R2) and `ops.export_runs` is `xpt.export_runs` (Appendix AC). AE X-65 governs those tables; this resolution only fixes that no assurance, HR or export table may be created in `ops`. EOP tables carry module prefixes (`crm_`, `ob_`, `cs_`, `tkt_`, `kb_`, `wf_`, `svc_`, `fin_`, `ws_`, `con_`, `rpt_`) plus the unprefixed `ops.tickets`. AE X-65's read-only compatibility views `ops.<v2.1 name>` exist only in the **core** database and only for v3.0; they are never created in the business database, and the FR-P14-V3-X01 check ignores them until v3.1, when they are dropped. |
| X-51 | P13 mini-CRM vs EOP CRM | From P16, `ops.crm_*` is the CRM system of record. `growth.leads` remains the **capture inbox** for public forms, tools and the partner portal (write path unchanged, consent captured at source); `LeadIngestWorkflow` promotes each captured lead into `ops.crm_leads` within 60 s, running dedupe and suppression. `growth.accounts` and `growth.opportunities` are migrated once into `ops` (row map in `ops.crm_migration_map`) and kept as read-only views for 2 releases. SCR-P13-18 (`/admin/growth/crm`) is superseded by EOP screens; P13 routing bands, SLA timers and scoring defaults (FR-P13-19) become the seed of `ops.crm_routing_rules` and `ops.crm_scoring_models`. The HubSpot/Zoho sync of D.9 moves to the EOP CRM and keeps its rules (CRM data only, suppression and consent checks). Appendix Y X-53 adopts this resolution for marketing; Appendix AC §AC.11.1, §AC.11.2 and §AC.12.1 read `ops` where they name `growth` for leads, accounts and opportunities. |
| X-52 | Grievance owner and escalation (EGP-2026.1) | Appendix U §U.6.4 names escalation to the Company Secretary; the management brief names the Grievance Officer. Resolution: the **Grievance Officer** (`grievance_officer` in the Equator institution tenant; name and contact rendered from `tenant.legal_entity`, X-15) owns every grievance from acknowledgement to final reply; a complainant dissatisfied with the final reply may appeal to the **Company Secretary** (level-2 review; new permission bundle `escalation_reviewer`, held by the Company Secretary, to be registered in Appendix S §6) within 30 days; complaints about a neutral's conduct go to Appendix N §7.7 and are only tracked (metadata) in EOP; challenges to a case decision are not grievances and are signposted to the remedy the law provides. Clocks follow the strictest applicable rule pack (§X.8.3). |

---

## X.1 Product definition and boundaries

### X.1.1 One sentence

EOP is a **group-ready work operating system** — the "Infrabyx Work OS" engine (D3-02) — configured first for Equator Resolution Service Private Limited, in which every department works from its own workspace, every customer relationship is one CRM record across sales, onboarding, success and support, and every repeatable action can run on autopilot while legal, money, neutrality and people decisions stay with named humans.

### X.1.2 Locked boundaries (tier L; NN tests in §X.21)

| # | Boundary | Enforcement |
|---|---|---|
| EOP-L01 | EOP never stores or displays case evidence, pleadings, caucus notes, offers, settlement terms, awards, orders, party names or contact details obtained from a case, POSH data, health data or safety data (NN-07, NN-11, NN-16) | Separate database; schema validator on the core→ops projection rejects any non-allow-listed field (`OPS_CASE_FIELD_FORBIDDEN`); DB role `eq_ops` has no `USAGE` on case or sealed schemas |
| EOP-L02 | No marketing use of any data from a case, grievance, POSH, HR or support-ticket record (RB X-20; NN-16) | `mkt` and Brevo sync read only `ops.crm_contacts` rows with `marketing_eligible = true`; grievance/ticket bodies are never in segment predicates (`OPS_SEGMENT_SOURCE_FORBIDDEN`) |
| EOP-L03 | Served respondents are suppressed from every marketing list, CRM import and external sync unless they gave separate, revocable marketing consent outside the case flow (NN-16; P13 FR-P13-26(c)) | Suppression hash check on import, sync, segment build and send (`OPS_SUPPRESSED_CONTACT`) |
| EOP-L04 | Commercial data never reaches case administration or neutrals (D3-24) | Cerbos DENY; no read model of `ops.cs_health_scores`, `ops.crm_opportunities` or `ops.fin_receivables_view` is exposed to case or neutral roles |
| EOP-L05 | EOP never edits a ledger, invoice, payment, refund, payout or subscription; it proposes, routes and records hand-offs (NN-36) | No write grants on `billing`/`payments`; refund and write-off requests are created through P05 APIs where maker-checker applies |
| EOP-L06 | EOP never selects, ranks, recommends or vetoes a neutral, and never influences allocation, grading or the Quality Index (NN-03, NN-28, NN-34) | No API path from `ops` to `neutrals.allocation*`; CI test `NO_PAID_PLACEMENT` extended to `ops` |
| EOP-L07 | Automations never take an action on the human-approval list (§X.12.6) without a recorded human approval | Engine refuses to publish an automation whose action graph reaches a listed action without an `approval` step (`OPS_AUTOMATION_APPROVAL_REQUIRED`) |
| EOP-L08 | AI in EOP classifies, extracts, summarises and drafts only; a human sends every reply on fees, refunds, complaints, case procedure or legal matters (NN-01; RB AU-15) | AI drafts carry `requires_human_review = true`; the send button is disabled for AI-originated drafts until a human edits or approves |
| EOP-L09 | Group membership grants no data access (NN-38) | Every `ops` row carries `company_id`; RLS by company; cross-company access only through an active `grp` grant (Appendix AD) |
| EOP-L10 | No covert monitoring of staff through EOP (NN-35): activity metrics are task- and outcome-based (tickets handled, SLA attainment, quality reviews); no keystroke, screen or webcam capture | No such collectors exist; agent productivity reports show only work-item metrics and are visible to the employee |
| EOP-L11 | Every external tool sits behind a port with a declared system of record, field mapping, import/export and a migration rehearsal (NN-40) | Connector cannot be activated without a `cfg.system_of_record` row (`CFG_SOR_UNDECLARED`), an approved mapping set (`CFG_MAPPING_MISSING`) and a passed rehearsal in `cfg.migration_rehearsals` (`OPS_CONNECTOR_REHEARSAL_MISSING`) — Appendix AC IP-02–IP-04 |
| EOP-L12 | Statutory grievance clocks and DPDP request clocks are never paused, lengthened or disabled by configuration; tenants may only set stricter internal targets | Rule packs `rulepack.IN.grievance.*` are tier G with locked floors |

### X.1.3 Users

Internal staff of Equator (and, later, of group companies onboarded under Appendix AD) in the default departments of D3-06. Customers and parties never log in to EOP: they reach support through the web help centre, the portal "Help" panel, email, WhatsApp or phone, and see their tickets in the portal (`/app/help`). Contractors (implementation partners, freelance trainers) may receive time-bound **guest** memberships restricted to named implementation projects (`ops_guest` bundle; no CRM list views, no exports).

---

## X.2 Architecture

### X.2.1 Application, portal and modules

| Item | Specification |
|---|---|
| App | `apps/ops` — Next.js (App Router, RSC), same design tokens and `packages/ui` as `apps/web`; command palette (`Ctrl/Cmd+K`); keyboard-first lists; responsive to 360 px (support agents and CSMs on mobile browsers). Native mobile is out of scope for P16. |
| Host | `ops.equatorresolution.in` (X-14 domain); CloudFront + WAF; mTLS client-certificate option for managed devices (Appendix S §2.6 device policy) |
| Identity | Keycloak client `eq-portal-ops`; workforce SSO only (Entra ID via Keycloak brokering; Google Workspace adapter when enabled); **phishing-resistant MFA mandatory** (`acr = eq:aal2-pr`); session idle 15 min, absolute 10 h; network and device policy per Appendix S §2.6; group-company staff authenticate through their own company's IdP federated under Appendix AD |
| API | NestJS bounded context **`ops`** in `apps/api` (modular monolith), sub-modules: `ops-core` (workspaces, departments, tasks, dashboards, saved views), `crm`, `onboarding`, `success`, `support`, `grievance-bridge` (to `grm`), `kb`, `automation` (engine), `ops-finance-views`, `ops-service-views`, `ops-connectors` (Brevo/CRM/workspace adapters via `integrations`), `ops-reporting`. Strict module boundary: no import of `cases`, `documents`, `posh`, `hr`, `pay` internals; only published read-model clients |
| Workers | Temporal task queue `ops` (long-running: imports, migrations, onboarding projects, SLA timers, automation runs, sync); BullMQ for short jobs (dedupe scoring, notifications) |
| Search | OpenSearch index aliases `ops-{company}-crm`, `ops-{company}-tickets`, `ops-{company}-kb` (company-scoped; ticket bodies flagged `case_linked` are indexed only for support roles) |
| Files | S3 bucket `eq-{env}-ops` (SSE-KMS, company data key); attachments virus-scanned; no Object Lock (business records) except grievance records (governance mode, retention class `grievance`) |
| Observability | OpenTelemetry; per-automation run metrics; SLO: ticket intake API p95 ≤ 300 ms; CRM list p95 ≤ 800 ms for 100k records |

### X.2.2 Data plane and isolation (D3-20)

```
                 ┌──────────────────────── core database (case plane) ───────────────────────┐
                 │ core, cases, documents, billing, payments, grm, posh_sealed, …, eng       │
                 └──────┬──────────────────────────────┬─────────────────────────────────────┘
       allow-listed outbox events                 read-model APIs (aggregates / metadata only)
                        ▼                              ▼
   ┌──────────────── business database (isolated cluster; P13 boundary extended) ───────────┐
   │ growth (capture, CMS, claims, suppression)   ops (EOP)   mkt (Appendix Y)              │
   │ roles: eq_growth → growth   eq_ops → ops (+ SELECT on growth.suppression_hashes,        │
   │        growth.leads capture view)   eq_mkt → mkt (+ SELECT on ops.crm_marketing_view)  │
   └─────────────────────────────────────────────────────────────────────────────────────────┘
```

Rules: (a) no cross-database joins; (b) core never reads `ops` except the ticket-status read API used by `/app/help` and the GRM bridge (§X.8); (c) `eq_ops` has no grant on `hr`/`pay`; EOP obtains staff for assignment through the **staff directory projection** (`ops.ws_staff_directory`: person id, display name, work email, department, cost centre, company, skills, languages, working hours, out-of-office flag — no salary, appraisal, leave reason or personal data); (d) `eq_mkt` reads only the marketing view, which excludes ticket, grievance, service and finance tables; (e) per-company KMS data keys.

### X.2.3 Read models consumed from the core plane (allow-listed fields only)

| Read model | Source | Fields (exhaustive) | Consumers | Refresh |
|---|---|---|---|---|
| `ops.svc_account_service_stats` | `cases`, `clocks`, `notices`, `hearings` aggregates per tenant | tenant ref, period, matters filed/open/closed by vertical and stage, scrutiny-within-SLA %, notice delivered %, hearings held, median days filing→constitution, clock breaches (count), service failures (count) | Case services, CS (account level), leadership | hourly |
| `ops.svc_matter_status` | `cases`, `clocks` | case number, tenant ref, vertical, mechanism, stage, SLA state (`green/amber/red`), owning case-manager team, next milestone date, flags `service_failure`, `deemed_service_pending`, `unowned_clock` | `case_services_lead`, `ops_manager`, `ops_director` only | 5 min |
| `ops.fin_receivables_view` | `billing` | invoice no., account ref, amount_minor, currency, GST total, due date, ageing bucket, dunning state, mandate state, last payment date | `finance_ops`, `accounts_*`, CSM (own accounts, amounts only), leadership | 15 min |
| `ops.cs_usage_signals` | `billing` meters (App. O §4.3), `identity` | tenant ref, seats used/allowed, active users 7/30 d, meter consumption vs allowance by meter, features enabled, API calls, bulk batches | CS, onboarding | daily 02:00 IST |
| `ops.crm_subscription_view` | `core.subscriptions` (Appendix F), `core.enterprise_contracts` | plan code, status, term start/end, renewal date, auto-renew flag, MRR/ARR (minor units), committed-use attainment % | Sales, CS, finance ops | hourly |
| `ops.tkt_case_context` | `cases` | case number, stage, assigned case-manager team, next hearing date (date only), portal deep link for staff | Support agents on a ticket with a verified case link and an active support grant | on demand (API), never stored beyond the ticket's lifetime cache (24 h) |

Any new field needs an ADR and the schema-validator allow-list update; the validator runs in CI and at runtime (`OPS_CASE_FIELD_FORBIDDEN`, 422 at publish).

### X.2.4 Work OS engine and group readiness

- **Company dimension.** `grp.companies` (Appendix AD) seeds Equator as `company_code = 'EQR'`. Every `ops` row carries `company_id`; RLS policy `ops_company_isolation` compares it with the acting membership's company in `Equator-Context` (X-01).
- **Workspaces are configuration.** Departments, workspaces, queues, pipelines, SLA policies, dashboards, KB spaces and automations are rows, not code; a new company is onboarded by cloning a **workspace template pack** (`ops.ws_template_packs`: `equator_default_v1`, `lending_software_v1` for Finbyx, `lending_platform_v1` for Udofin) and then configuring it.
- **Cross-functional staff.** A person may hold memberships in several companies; each membership has its own roles. The UI shows a company switcher; actions are always recorded against one company. Shared queues across companies (e.g., a group support desk) require an Appendix AD grant naming the purpose, the data categories, the expiry (≤ 12 months, renewable) and the GDSA reference.
- **Ethical walls (RE E.26).** A user holding any Finbyx/Udofin role is denied Equator `ops.svc_matter_status` rows for tenants that are clients of those companies, and is never assigned Equator support tickets with a verified case link involving those clients (`OPS_ETHICAL_WALL`). The check runs at role grant and at policy time; annual attestation is collected in EOP (§X.20).
- **Shared dashboards.** Group leadership dashboards show **aggregates only** (revenue by company, ticket volumes, SLA attainment, CSAT) published by each company's `ops_director` to a group dashboard space; drill-down into another company's records needs a grant.
- **Group cross-sell (RB AU-26)** stays OFF (`group.ops.cross_sell.enabled`) until the group consent design and the GDSA are approved (Appendix AD; RE F4.4).

---

## X.3 Departments, workspaces and dashboards

### X.3.1 Default department model (D3-06; configurable)

Management said it would explain the departmental structure and has not yet done so. EOP therefore ships the **default model below as configuration** (`tenant.ops.departments`, tier T): departments can be renamed, merged, split or added, given cost centres and a legal entity, and mapped to workspaces. Two properties are **locked**: Internal Audit reports to the Board/Audit function and is independent of operations (no operations role can be its head or approve its access), and the Grievance Officer role cannot be held by the head of the department whose service is complained about for that grievance (conflict check at assignment).

| Department (default) | EOP workspace | Default roles | Primary queues | Head approves |
|---|---|---|---|---|
| Leadership | Leadership cockpit | `ops_director`, `department_head` (each head) | Escalations, approvals awaiting leadership | Authority-matrix items above department limits |
| Case Services (Registry and Case Management) | Service delivery (metadata) | `case_services_lead`, `ops_manager` | Service exceptions, SLA risk, customer service requests about matters | Service-credit proposals (to finance) |
| Neutral Relations and Panel | Panel operations (metadata) | `panel_manager` (existing), `ops_manager` | Empanelment pipeline tasks, training-provider liaison | — (panel decisions stay in P03/App. N) |
| Onboarding and Implementation | Onboarding | `onboarding_specialist`, `ops_manager` | Implementation projects, migration tasks, go-live sign-offs | Go-live readiness |
| Customer Success and After-Sales | Success | `customer_success_manager` | At-risk accounts, renewals, QBRs, expansion | Retention offers within bands |
| Support and Grievance | Support desk; Grievance desk | `support_agent`, `support_lead`, `grievance_officer` | Tickets by SLA; grievances by statutory clock | Ticket→grievance conversion disputes |
| Sales and Business Development | Sales | `sales_executive`, `bd_manager` | Leads, opportunities, quotes awaiting approval | Discounts within band |
| Marketing, Brand and Content | (Appendix Y studio) | `marketing_manager`, `content_writer`, `designer` | Campaign approvals (Y) | Sequence versions (Y) |
| Social Media and PR | (Appendix Y) | `social_media_executive`, `pr_manager` | Social calendar (Y) | — |
| Partnerships and Collaborations | Partnerships (CRM pipeline `partnership`) | `partnerships_manager` | Partner onboarding, MoU tracker | MoU (CEO per AU-24) |
| Training and Academy Liaison | Training operations | `ops_manager` (training bundle) | Client training sessions, EQAP sitting logistics | — |
| Finance and Accounts | Finance operations views | `finance_ops`, `accounts_maker`, `accounts_checker` | Receivables follow-ups, refund hand-offs, billing queries | Write-off proposals (P05) |
| HR and Administration | (HRMS) | `hr_manager`, `hr_executive` | — (HRMS) | — |
| Legal and Compliance | Legal review queue | `legal_reviewer`, `compliance_officer` | KB/public-article legal review, complaint legal review, contract redlines | Legal sign-offs |
| Technology and Information Security | IT requests | `it_admin` | Access requests, workspace provisioning exceptions | — |
| Internal Audit | Audit (read-only) | `internal_auditor` | Sampling, attestations | — |

### X.3.2 Workspace anatomy (every department)

Each workspace has: **home dashboard** (widgets configurable within the department pack; mandatory widgets marked M cannot be hidden); **queues** (saved views over tasks, tickets, projects or CRM records with SLA timers); **records** (the department's object lists); **playbooks** (KB space with SOPs and scripts); **automations** (those owned by the department); **reports**; **settings** (department-level, tier T, within company bounds). Fewer-clicks rules of Appendix S §5 apply (next action ≤ 1 click; bulk actions; command palette).

### X.3.3 Department dashboards (defaults)

| Workspace | Widgets (M = mandatory) | KPIs | Quick actions (≤ 4) |
|---|---|---|---|
| Leadership cockpit | **M** company scorecard (ARR, net revenue retention, gross churn, pipeline coverage, CSAT, NPS, ticket SLA %, grievance clock breaches); **M** approvals awaiting me; revenue by stream (from `rev`, Appendix AB, with neutrality-exposure tile per RB A.7); department SLA heatmap; top at-risk accounts (CS); grievances older than 21 days; automation exceptions; staffing load (open work items per person, no personal data) | NRR, GRR, ARR growth, CAC payback (from Appendix Y attribution), grievance breaches (target 0) | Approve · Open escalation · Publish group dashboard · Export board pack |
| Service delivery (Case Services) | **M** red/amber matters by account (metadata, §X.2.3); **M** unowned-clock flags (must be 0; the fix happens in `/console`, link-out); service failures this week; customer service requests about matters (ticket category `case_procedure`); scrutiny-within-SLA trend; notice delivery % by channel; hearings logistics exceptions | Scrutiny ≤ 2 working days %; notices delivered %; service-request first response | Open in case console · Assign service request · Raise service-credit proposal · Notify CSM (metadata only) |
| Onboarding | **M** projects by stage with RAG; **M** go-live sign-offs due; migration tasks failing validation; training sessions this week (Teams links); configuration checklist completion by project; hypercare tickets | Time-to-first-value; time-to-go-live vs plan; migration error rate; checklist completion % | New project · Book training · Run migration dry-run · Request go-live sign-off |
| Success | **M** health distribution and movers; **M** renewals in 120/90/60/30 days; at-risk playbooks running; QBRs due; expansion signals (allowance > 80%); NPS/CSAT verbatims (process only) | GRR, NRR, logo churn, health ≥ 70 %, QBR coverage | Start playbook · Schedule QBR · Log risk · Create renewal opportunity |
| Support desk | **M** my queue by SLA timer; **M** breaching in ≤ 60 min; unassigned by category; awaiting customer; macros; KB suggestions; CSAT last 7 days | First response within SLA %; resolution within SLA %; backlog age; reopen rate; CSAT; deflection rate | Next ticket · New ticket · Merge · Escalate |
| Grievance desk | **M** grievances by clock state (T-7, T-3, breached); **M** acknowledgements due in ≤ 12 h; level-2 appeals; category heatmap; quarterly transparency-report counts | Acknowledged ≤ 48 h %; resolved ≤ 30 days %; appeals upheld | Open next · Acknowledge · Draft final reply · Prepare quarterly summary |
| Sales | **M** my pipeline by stage; **M** leads breaching speed-to-lead SLA; quotes awaiting approval; activities today; forecast (commit/best case) | Speed-to-lead; win rate; cycle time; average contract value; discount leakage | New lead · Log activity · Create quote · Book meeting |
| Finance operations views | **M** receivables ageing (0–30/31–60/61–90/90+); **M** dunning states and hand-offs; refund requests awaiting P05 maker-checker; billing-query tickets; collections tasks by CSM | DSO; overdue %; dunning recovery %; billing-query resolution time | Open invoice (read-only) · Create collections task · Route refund request to P05 · Export ageing |
| Training operations | client training calendar; attendance; certificates issued (client staff); EQAP sitting logistics (dates, rooms, invigilators — no candidate scores); training-provider list (≥ 3 providers, X-29) | Sessions delivered; attendance %; training CSAT | Schedule session · Send materials · Record attendance · Open KB |
| Marketplace operations | seller (Chambers/neutral) onboarding queue for the Private Practice Marketplace; listing moderation; complaint flags; ranking-parameter publication status; sponsored-slot audit (OFF until `marketplace.paid_placement`, NN-34) | Time to approve listing; complaint rate; moderation SLA | Review listing · Request correction · Suspend listing (maker) · Open audit |
| Partnerships | partner pipeline; MoUs awaiting signature; partner-sourced pipeline; partner statements (reward-eligible partners only; professionals are relationship partners with no reward, X-54) | Partners active; partner-sourced ARR | New partner · Send MoU · Log activity · Open statement |
| Internal Audit | sampling queue; attestation status; exceptions register (from `ctl`); access-review findings | Attestations complete %; exceptions closed ≤ 30 days | Sample records · Request evidence · Export (watermarked) |

### X.3.4 Internal task queues and cross-functional assignment

`ops.ws_tasks` is the universal work item: `type` (configurable: `onboarding_step`, `migration_task`, `collections_followup`, `service_request`, `legal_review`, `it_request`, `qbr_prep`, `generic`), `title`, `description` (rich text, no case content — a validator flags case-number + party-name patterns and asks the author to remove them), `owner_person_id`, `owner_queue_id`, `requested_by`, `department_id`, `company_id`, `related` (polymorphic link to CRM, project, ticket, grievance), `priority`, `due_at`, `sla_policy_id`, `status` (`open → in_progress → blocked → done | cancelled`), `blocked_reason`, `dependencies[]`, `watchers[]`, `checklist jsonb`, `visibility` (`department`, `named`, `company`). **Cross-functional assignment:** any user can request work from another department's queue; the receiving queue's routing rules (skills, language, load, round-robin, out-of-office skip) assign it; reassignment across departments records reason; tasks to another company require an Appendix AD grant. **Load view** shows work-item counts and SLA attainment per person (NN-35: work items only, visible to the person).

---

## X.4 CRM

### X.4.1 Object model

| Object | Table | Key fields | Notes |
|---|---|---|---|
| Account (organisation) | `ops.crm_accounts` | name, legal name, kind (`lender`, `insurer`, `employer`, `listed_company`, `hei`, `msme`, `chambers`, `law_firm`, `institution`, `government`, `partner`, `vendor`, `other`), CIN/LLPIN, GSTIN (validated format), PAN (masked display), LEI, website domain, industry, size band, volume band (P13), state/city, owner, territory, tier, lifecycle (`prospect`, `customer`, `former_customer`, `partner`), `core_tenant_ref` (when provisioned), `core_org_ref`, parent account (hierarchy), tags, custom fields | Enrichment from public company data only (RB AU-02; MCA/GSTIN via licensed aggregator, Appendix S §3.6–3.7) |
| Contact (person) | `ops.crm_contacts` | name, job title, seniority, department, emails (verified flag), phones (E.164), preferred language, account links (many-to-many with role), persona (party, enterprise, neutral, learner, partner, counsel, institution), consent summary (derived), `marketing_eligible` (derived), `suppressed` (derived), source, owner | Advocates flagged `is_advocate = true` (self-declared or verified) → advocate rules (§X.4.11) |
| Lead | `ops.crm_leads` | capture ref (`growth.leads.id`), source, UTM first/last, page, form, persona, vertical, dispute-type interest (product interest, never a dispute narrative), volume band, city, language, score + explanation, status (`new → working → nurturing → qualified → converted | disqualified`), disqualify reason, owner, SLA timer | Converted into account + contact + opportunity |
| Opportunity (deal) | `ops.crm_opportunities` | pipeline, stage, amount_minor + currency (expected first-year value excl. GST), probability (stage default, overridable with reason), close date, products (lines from `rev` registry), competitor, decision process, next step, owner, source, partner ref, quote refs, `requires_legal_review`, `requires_security_review` | Stage gates (§X.4.2) |
| Product / plan | `ops.crm_products` (read model of `rev.streams` (Appendix AB) + `core.plans`) | stream code (RS-xx), plan code, name, pricing unit, cadence, list price ref (App. B/O), `sellable` (stream status `live` in the quoting scope and kill switch not engaged — Appendix AB AB-R1), neutrality rating (N0–N4, Appendix AB) | Sales can quote only `sellable` products (`OPS_PRODUCT_NOT_SELLABLE`) |
| Quote | `ops.crm_quotes` | opportunity, quote number, version, lines (from fee engine `POST /v1/billing/quotes` — Appendix B precedence), discount % per line, total excl. GST, GST, total incl. GST, validity, terms template version, approval state, e-sign ref, PDF/DOCX renditions | Discount above band or non-standard terms → maker-checker (§X.4.5) |
| Subscription | `ops.crm_subscription_view` | (read model; §X.2.3) | Never edited in EOP |
| Implementation | `ops.ob_projects` | (§X.5) | Linked to account and opportunity |
| Activity | `ops.crm_activities` | kind (`call`, `meeting`, `email`, `note`, `whatsapp`, `task`), direction, subject, body (rich text), participants (contacts and staff), occurred_at, duration, outcome code, recording ref (if consented), meeting join URL, visibility (`team`, `private`, `restricted`), sensitivity (`normal`, `commercial_confidential`) | §X.4.6 |
| Consent and preferences | `ops.crm_comm_prefs` + refs to `core.consent_records` | per purpose (`marketing_email`, `marketing_whatsapp`, `marketing_sms`, `newsletter`, `event_updates`, `partner_communications`, `group_share:<company>`), status, captured_at, notice version, channel, source, withdrawn_at; quiet hours; language; frequency cap | §X.4.7 |
| Segment | `ops.crm_segments` | kind (`dynamic`, `static`), predicate (JSON DSL), owner, purpose, refresh cadence, member count, last built | §X.4.8 |
| Custom field | `ops.crm_custom_fields` | object, key, label (en/hi), type (`text`, `number`, `money`, `date`, `select`, `multiselect`, `boolean`, `url`, `lookup`), validation, sensitivity (`normal`, `confidential`, `prohibited`), required-at-stage, tier | §X.4.8 |
| Tag | `ops.crm_tags` | name, colour, object scope, owner | Free tags cannot encode prohibited attributes (validator) |
| Saved view | `ops.ws_saved_views` | object, filters, columns, sort, sharing (`me`, `team`, `department`, `company`) | Respect row/field permissions at render time |
| Duplicate candidate | `ops.crm_duplicate_candidates` | object, record A, record B, rule, score, status | §X.4.9 |
| Import job | `ops.crm_import_jobs` | file, mapping, preview, dry-run result, reconciliation | §X.4.10 |
| Routing rule | `ops.crm_routing_rules` | object, conditions, assignment method, SLA policy, priority | §X.4.11 |
| Scoring model | `ops.crm_scoring_models` | version, factors, weights, thresholds, status, approved_by | §X.4.12 |
| Partner / referral | `ops.crm_partners`, `ops.crm_referrals` | partner kind (`ca_firm`, `cs_firm`, `cma_firm`, `law_firm`, `advocate`, `bar_body`, `hrms_vendor`, `los_vendor`, `chamber_of_commerce`, `industry_association`, `reseller`, `university`, `other`), agreement ref, reward type (`cash_revenue_share`, `service_credit` (B2B customers only, Appendix Y RP-02), `none`), `reward_eligible` (locked `false` for `advocate`, `law_firm`, `bar_body`, `ca_firm`, `cs_firm`, `cma_firm`), status. `crm_referrals` links a referral (partner or customer; `mkt.referral_codes` code by value) to the lead or opportunity for attribution only | No referral reward of any kind to advocates, CAs, CSs, CMAs or their firms (NN-34; Appendix Y X-54; master X-62); cash revenue share only for other partners with a written agreement (RS-28). Programme rules, codes and rewards live in Appendix Y (`mkt.referral_programmes`, `mkt.referral_codes`, `mkt.referral_rewards`); the partner organisation record and the `partnership` pipeline live here |

### X.4.2 Pipelines and stages (configurable; tier T, gates tier G where legal)

Pipelines are configuration (`ops.crm_pipelines`, `ops.crm_stages`). Seeded pipelines:

| Pipeline | Stages (default probability) | Stage gates (cannot advance without) |
|---|---|---|
| `enterprise_odr` (lenders, insurers, employers) | Discovery (10) → Solution fit (25) → Pilot / proof (40) → Proposal (60) → Contract and security review (80) → Closed won (100) / Closed lost (0) | Proposal: quote approved; Contract: legal review of redlines done, DPA/DSA draft attached (P09 FR-P09-23), Appendix O §2.4.1 contract heads captured, NN-03/NN-16 disclosure text acknowledged by customer; Closed won: e-signed order form + DPA |
| `saas_grm_posh` | Discovery → Demo → Trial/sandbox → Proposal → Closed | Proposal: quote approved; Closed: order form e-signed |
| `chambers_counsel` (self-serve assisted) | Interested → Demo → Plan selected → Closed | Closed: plan purchase confirmed by `billing` event (no manual close) |
| `institutional` (universities, government, institutions) | Engagement → Requirement → Proposal / tender → Negotiation → Award → Closed | Tender documents uploaded; conflict register checked (RB RS-26) |
| `partnership` (shared with Appendix Y §Y.9.2; no separate marketing pipeline) | Identified → Researched → Contacted → Exploring → Proposal → Term sheet → Legal review → Approval → MoU signed → Active | Legal review: MoU mandatory clauses present (Appendix Y §Y.9.1; `MKT_MOU_LEGAL_REVIEW_REQUIRED`); Approval: authorised signatory through `ctl` (CEO for MoUs, RB AU-24); MoU signed: signed instrument recorded on `mkt.mous`; claims about partners only after signature. The post-signature lifecycle (renewal due → renewed / expired / terminated) is held on `mkt.mous` |
| `renewal` (auto-created by CS, §X.6.5) | Open (90) → In negotiation → Committed → Renewed / Churned | Renewed: `billing` renewal event |
| `expansion` | Signal → Qualified → Proposal → Closed | Proposal: quote approved |

Stage changes write `ops.crm_stage_history` (from, to, by, at, reason, time-in-stage). Closed-lost requires a reason code (configurable list; `price`, `no_decision`, `competitor`, `legal_constraint`, `timing`, `product_gap`, `other`).

### X.4.3 Products, prices and the revenue registry

The product list is **never typed in EOP**: it is a read model of the Appendix AB revenue stream registry and `core.plans`. A stream whose kill switch is engaged (`equator.rev.stream.killed.v1`), or whose status is not `live` in the quoting scope (`REV_STREAM_NOT_LIVE`, Appendix AB AB-R1), disappears from new quotes within 5 minutes (RB A.6; Appendix AB KS-3), and open quotes containing it are flagged for review. Streams rated **N2** in Appendix AB (commercial visibility or a take linked to neutrals' work, e.g., RS-18, RS-19 sponsored listing) are `non_administered` only and can be quoted only to non-advocate private-practice neutrals and chambers on the Private Practice Marketplace surface, RS-19 only when `marketplace.paid_placement` is ON (NN-34); **N3** streams are never quotable for administered work; **N4** streams (prohibited, e.g., RS-20, RS-29, RS-50, RS-51, RS-53, RS-54) are never quotable. Advocates, CAs, CSs and CMAs are never quoted placement, ratings, featured labels or referral rewards (NN-34).

### X.4.4 Quotes (from the fee engine)

1. The sales user selects products; EOP calls the fee engine (`POST /v1/billing/quotes`, P05) which returns line prices, GST (CGST/SGST or IGST by place of supply), validity and the fee-schedule version; EOP never computes a price itself.
2. Discounts: per-line discount within the **discount band** of the authority matrix (`ctl.authority_rules`, resolved through `ctl.resolve_authority`; approvals as `ctl.approval_requests` — workforce/internal-controls specification; NN-36): default bands — `sales_executive` ≤ 5 %, `bd_manager` ≤ 15 %, `ops_director` ≤ 25 %; above 25 % or any non-standard term (payment terms beyond net-30, liability caps, SLA credits above standard, exclusivity, most-favoured pricing) → maker-checker with `finance_ops` and, for terms, `legal_reviewer`.
3. Locked: no quote may offer a success fee that Appendix B or X-07 prohibits, a price contingent on outcomes, a lower take-rate as a neutral's billed fees rise (RB X-19), or any feature that gives a paying party a procedural advantage (RA-2, RA-3).
4. Renditions: DOCX (editable, MS Office compatible) and PDF; total including GST shown on every page for consumer-facing quotes (NN-29); e-sign through `ESIGN_PORT`; acceptance emits `equator.ops.quote.accepted.v1`, which starts provisioning (AU-10) only after the order form and DPA are both signed.

### X.4.5 Approvals in the commercial cycle

| Item | Maker | Checker | Extra |
|---|---|---|---|
| Discount within own band | Owner | — | Logged |
| Discount above band | Owner | Next band holder (≠ maker) | Reason ≥ 30 chars |
| Non-standard commercial term | Owner | `finance_ops` + `legal_reviewer` | Redline attached |
| Enterprise contract (every one) | `bd_manager` | `legal_reviewer`; `ops_director` for value above `tenant.ops.crm.contract_board_threshold_minor` | P09 FR-P09-23 DPA/DSA gate |
| Related-party contract (group company or director-interested entity) | `bd_manager` | Company Secretary | Companies Act 2013 s.188/s.184 flag; arm's-length note (RE F5.2) **[CS to confirm thresholds]** |
| Partner agreement with cash revenue share | `partnerships_manager` | `finance_ops` + `legal_reviewer` | Partner confirmed not an advocate (RB AU-21) |

### X.4.6 Activities: logging, consent and access

- **Calls.** Click-to-call from EOP uses `TELEPHONY_PORT` with an Equator DID; outbound sales calls are commercial communications: DND scrub and TCCCPR rules apply; calls to a contact who is a borrower in any FIN matter are blocked from EOP entirely (suppression list) and, if inbound support callbacks are needed, follow the NN-12 08:00–19:00 window. **Recording** only with a disclosure played at the start and the contact's consent captured (`ops.crm_activities.recording_consent`); otherwise no recording.
- **Meetings.** Calendar-backed Teams meetings via `WORKSPACE_PORT.createMeeting` (§X.11); join URL stored on the activity; transcripts retrieved only when the meeting organiser enabled transcription, all attendees were told, and the meeting was internal or with a B2B customer (never a party to a case; never a hearing).
- **Emails.** Logged by (a) the BCC drop-box address `log+{company}@crm.equatorresolution.in` (SES inbound), (b) the EOP composer (sends through `EMAIL_PORT` business class, never the case-notice class), or (c) the Outlook add-in (flag `tenant.ops.crm.outlook_addin.enabled`, OFF until the staff notice is updated, NN-35). Automatic mailbox scraping is not offered.
- **Access.** Default visibility `team`; `private` activities are visible only to the author and `ops_director`; `restricted` (e.g., notes on a sensitive commercial dispute with the customer) need the account's `restricted_viewers`. Activities never record health, caste, religion, political opinion, sexual orientation or any case narrative (validator prompts; free-text scanner flags case numbers and Aadhaar/PAN patterns and masks them).
- **Customer complaints inside activities.** If an activity records a complaint about Equator's service, the user must convert or link it to a ticket (§X.7) so the complaint enters a tracked process (`OPS_COMPLAINT_NOT_TRACKED` warning blocks closing the activity without a link).

### X.4.7 Consent and communication preferences

- The consent service (`core.consent_records`, P01) remains the legal ledger; `ops.crm_comm_prefs` is a synchronous mirror keyed by person and purpose, updated by `equator.consent.consent.given.v1` / `…withdrawn.v1` (P01) within 60 s, and EOP writes consent changes through the consent API (never directly).
- Marketing consent is **never inferred** from a case, grievance, support or purchase interaction (RB §5); a support ticket never sets `marketing_eligible`.
- `marketing_eligible = consent(purpose, channel) ∧ ¬suppressed ∧ ¬opted_out ∧ age ≥ 18 confirmed ∧ ¬respondent_hash_match`; computed, not editable.
- Preference centre (signed link, P13 FR-P13-22) shows purposes, channels, frequency and language; opt-out of one company's marketing never opts the person into another's; **90-day no-re-ask** after an opt-out (RB E.23).
- Withdrawal propagation: Brevo and any other external CRM within 15 minutes (D.9; RD DI-B.10); failure raises `OPS_CONSENT_PROPAGATION_LATE` and pages the DPO desk after 30 minutes.

### X.4.8 Segments, custom fields, tags and saved views

- **Segment DSL** (JSON; compiled to parameterised SQL over the marketing-safe view): fields from accounts, contacts, leads, opportunities, subscriptions view, product interests, lifecycle, engagement events (from Appendix Y touchpoints), consent; **forbidden sources** (validator): tickets, grievances, `svc_*`, `fin_*`, activities bodies, custom fields marked `prohibited`, any `case_linked` flag (`OPS_SEGMENT_SOURCE_FORBIDDEN`). Preview shows count and a 20-row sample (masked) before save. Segments used for marketing must name a purpose that matches a consent purpose.
- **Custom fields:** up to `tenant.ops.crm.custom_fields_max_per_object` (default 100); sensitivity `prohibited` is a guardrail category (e.g., religion, caste, health) that cannot be created — the creation API rejects labels matching the prohibited-attribute dictionary (`OPS_FIELD_PROHIBITED`).
- **Saved views** respect field-level permissions at render time; a shared view never reveals a column the viewer cannot read (column silently omitted with a "hidden by permission" chip).

### X.4.9 Duplicate detection and merge

| Rule | Object | Match keys | Action |
|---|---|---|---|
| D1 exact | Contact | normalised email (lower-case, trimmed; Gmail dot/plus normalisation only for `gmail.com`) | Block create; offer "open existing" |
| D2 exact | Contact | phone E.164 | Block create unless the existing contact is in another account and the user confirms a shared number |
| D3 exact | Account | GSTIN, CIN/LLPIN, LEI | Block create |
| D4 fuzzy | Account | legal-name similarity (Jaro–Winkler ≥ 0.92 after removing "Private Limited/Pvt Ltd/Limited/LLP") + same state, or same website domain | Candidate for review |
| D5 fuzzy | Contact | name similarity ≥ 0.9 + same account, or same name + same city + same employer domain | Candidate for review |
| D6 lead→contact | Lead | email/phone matches an existing contact | Attach lead to contact; do not create a duplicate |

**Merge:** a user with `crm.merge` chooses the surviving record; survivorship per field (default: most recently verified value; consent records are **unioned with the most restrictive status winning** — a withdrawal on either record survives); activities, tickets, opportunities and tasks re-parent; merged record becomes a tombstone (`merged_into_id`) for 30 days and can be **un-merged** within that window; every merge writes `ops.crm_merge_log` (before/after digests, rule, user) and the audit chain. Merges that would join records from two companies are impossible (`OPS_CROSS_COMPANY_MERGE`).

### X.4.10 Import tools

Steps (Temporal `CrmImportWorkflow`): **upload** (CSV RFC 4180 UTF-8 with or without BOM, XLSX, JSON; ≤ 200,000 rows or 100 MB) → **mapping** (auto-suggested by header similarity; user confirms each column; unmapped columns listed; saved mapping templates) → **preview** (first 50 rows rendered as they will be stored; validation per row: formats, required fields, picklist values, GSTIN checksum, E.164) → **dedupe plan** (per row: create / update existing / skip, with the rule that matched) → **consent plan** (each row must carry a lawful source: `consent_artefact_ref`, `existing_customer_contract`, or `none` → imported as non-marketing; imports without consent evidence can never become `marketing_eligible`) → **suppression check** (respondent hashes; DND for phones) → **dry-run** (writes nothing; produces the reconciliation report: counts created/updated/skipped/rejected by reason) → **approval** (imports > 1,000 rows or containing personal data of > 100 people need a checker ≠ maker) → **commit** (idempotent by `import_job_id` + row number) → **reconciliation** (post-commit counts must equal dry-run counts ± rows changed concurrently; mismatches listed) → **rollback** (within 7 days: deletes created records not since modified, restores updated fields from the before-image). Prohibited: bulk import of Bar Council rolls, institute member directories or scraped lists (NN-39); files whose source field says so are rejected (`OPS_IMPORT_SOURCE_PROHIBITED`).

### X.4.11 Territory, ownership and routing

Routing rules (ordered, first match wins; tier T, changes audited): conditions on account/lead fields (state, city, segment, volume band, persona, language, product interest, partner source), assignment method (`named_owner`, `round_robin` within a team, `load_balanced` (fewest open items), `territory_owner`, `queue`), SLA policy (speed-to-lead), fallback owner. Seed = P13 FR-P13-19 bands: > 2,000 monthly disputes → enterprise lead RM, first response 1 business hour; 500–2,000 → enterprise RM, 4 business hours; 100–500 → mid-market queue, 1 business day; < 100 → inside sales / nurture; individuals (parties) → **not sold to**: routed to the case-services help queue with a 4-business-hour response and no commercial follow-up. Out-of-office owners are skipped (staff directory flag). Territory changes re-assign open records only after a preview and checker approval when > 50 records move.

**Advocates and professionals (NN-34, NN-39; RE F1).** Contacts flagged `is_advocate` are never targeted with paid-visibility offers, ratings, featured labels or referral rewards; outreach to advocates is limited to informational communication about Equator products they may use (counsel workspace); **no referral reward of any kind** (cash or non-cash) to advocates, CAs, CSs, CMAs or their firms (NN-34; Appendix Y X-54, D3-27 — RS-29 registered as Prohibited (N4; never leaves draft — Appendix AB §AB.3)); no solicitation of their clients through Equator. Directory listings are not managed in the CRM — the professional registry (`dir`, group shared service, D3-05) is separate and consent-based.

### X.4.12 Lead scoring (explainable, deterministic)

- Model = versioned points table (`ops.crm_scoring_models`): factors and points, e.g. seed from P13 (organisation type 25, volume 20, engagement 20, seniority 15, geography 10, data quality 10; threshold ≥ 70 → senior owner). Engagement points come only from marketing-consented engagement events (Appendix Y). **Forbidden inputs (locked):** anything from cases, grievances, tickets, POSH, HR, payments of parties, or inferred sensitive attributes (RB X-20).
- Every score stores its **explanation** (`[{factor, value, points}]`), shown on the record ("Why this score?").
- Model changes: maker (`bd_manager`) → checker (head of sales / `ops_director`) (RB AU-03); a back-test on the last 90 days' leads (conversion by score band) is shown before approval; rollback to the previous version is one click and re-scores asynchronously.
- AI may suggest factor weights from historical conversions as a **draft** for the human owner; it never scores individual leads.

### X.4.13 Referral, partner sources and attribution hooks (Appendix Y)

- Source taxonomy (`ops.crm_sources`): `web_form`, `tool`, `explorer_handoff` (only with separate marketing consent), `webinar`, `event`, `partner_referral`, `customer_referral`, `inbound_email`, `inbound_whatsapp`, `outbound`, `import`, `social_engagement` (Appendix Y E1), `event_registration`, `lead_magnet` (Appendix Y MA-03), `group_referral` (OFF with AU-26).
- **Attribution hooks:** every lead and opportunity stores `first_touch` and `last_touch` (UTM source/medium/campaign/content/term, landing page, timestamp) from `growth`, plus `mkt_touchpoint_ids[]` (Appendix Y). EOP exposes `GET /v1/ops/crm/attribution/{opportunityId}` and emits `equator.ops.opportunity.closed.v1` with amount and touchpoint ids so Appendix Y computes multi-touch attribution; offline conversion export to ad platforms is Appendix Y's and applies only to consented filers, never respondents (P13 FR-P13-23).
- Referral rewards: computed by the Appendix Y partner programme rules for `reward_eligible` partners only (never advocates, CAs, CSs, CMAs or their firms — locked, X-54); payouts are requested in EOP and executed only through P05 with `accounts_maker`/`accounts_checker` (NN-36).

---

## X.5 Onboarding and implementation

### X.5.1 Two tracks

| Track | Who | Flow | Human gates |
|---|---|---|---|
| **Self-service** | Chambers Lite/Solo, counsel workspace, small GRM tenants, Business Assure | Plan purchase (P05) → tenant provisioned (P01/P10) → in-app **setup checklist** in the tenant's settings area only (never inside case views) → guided tours → help centre → optional booked onboarding call | None for provisioning; legal review of tenant branding where the name contains restricted words (D2-16) |
| **Assisted (implementation project)** | Enterprise ODR programmes, GRM/POSH for regulated entities, Chambers Pro/Institution, API/white-label, BYOK | Closed-won opportunity → `ob_project` from template → kickoff → configuration → data migration → integration → training → UAT → go-live sign-off → hypercare → handover to CS | Security review (API/BYOK tenants, RB AU-10); DPA/DSA executed (P09 FR-P09-23); go-live sign-off (CSM + customer sponsor); legal review of tenant clause/rule choices where they affect third parties (NN-33 G) |

### X.5.2 Implementation project model

`ops.ob_projects` (account, opportunity, template, product lines, sponsor contact, Equator owner, CSM, start, target go-live, actual go-live, RAG status, hypercare end, `blocked_reason`) → `ops.ob_milestones` (name, sequence, owner side `equator|customer|joint`, planned/actual dates, exit criteria, status) → `ops.ob_checklist_items` (configuration items with a **verification probe**: e.g., "SSO configured" verified by a successful test login event; "Clause version adopted" verified by `equator.enterprise.clause.adopted.v1`; "Statutory clocks reviewed" verified by legal-reviewer sign-off) → `ops.ob_migration_tasks` (§X.5.4) → `ops.ob_training_sessions` (§X.5.5) → `ops.ob_signoffs`.

Template packs (tier T, versioned): `enterprise_fin_lender_v1` (12 milestones incl. clause registry, bulk-intake template mapping, notice templates in languages used, NN-12 contact-window confirmation, 1600-series number authorisation where lender-number mode is used, GRM variant `FIN_RBI`), `insurer_v1`, `employer_v1` (incl. POSH compliance-status scope only), `grm_saas_v1`, `posh_saas_v1` (sealed workspace set-up done by the customer's IC with Equator support that never sees complaint data, NN-07), `chambers_institution_v1`, `api_whitelabel_v1` (sandbox keys, webhook test, security questionnaire, pen-test evidence exchange).

### X.5.3 Project state machine

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| `draft` | kickoff held | sponsor named; template chosen | `in_progress` | milestones instantiated; Teams kickoff recorded as activity |
| `in_progress` | milestone blocked | reason given | `at_risk` | CSM + `ops_manager` notified |
| `at_risk` | blocker cleared | — | `in_progress` | — |
| `in_progress` | all pre-go-live milestones done | checklist probes green; migration reconciled; UAT signed | `ready_for_golive` | sign-off request sent |
| `ready_for_golive` | sign-off complete | Equator CSM + customer sponsor e-sign; security review passed where required | `live_hypercare` | hypercare timer (default 30 days); tickets tagged `hypercare` get P2 minimum priority |
| `live_hypercare` | hypercare ends | no open P1/P2; adoption baseline captured | `handed_over` | account moves to CS steady state; project CSAT survey |
| any | cancelled | reason | `cancelled` | open tasks cancelled; finance notified if milestone billing (RS-27) |

### X.5.4 Data migration tasks

Migration of a customer's historical data into Equator (e.g., an employer's open grievances into GRM; a Chambers' matter list) uses the platform import service (`xpt`, EQ-EXPORT-1.0 conventions, Appendix AC §AC.13) — EOP only tracks it: task per dataset with source, mapping template, dry-run result link, error rate, reconciliation counts (source rows = imported + rejected), customer acceptance of the reconciliation, and rollback point. **Case content imported for a tenant never lands in `ops`**: EOP records counts and status only.

### X.5.5 Training sessions

Session (title, audience role, language, mode `teams|in_person|recorded`, trainer, date/time, capacity, materials from KB, attendance, feedback). Teams sessions are created through `WORKSPACE_PORT.createMeeting` with calendar invites to customer contacts; attendance is recorded from the meeting attendance report where the SKU and policy allow (**[VERIFY — open: Business Basic attendance-report API availability, RD Open point 2]**) or manually; certificates for client staff are issued by EOP as "Certificate of attendance — product training" (never a professional credential, never a QAP/EQAP certificate).

### X.5.6 Go-live sign-off and hypercare

Sign-off pack (generated DOCX + PDF): scope delivered, checklist with probe evidence, open items with owners and dates, migration reconciliation, training attendance, support model and SLAs, escalation contacts, Equator neutrality disclosures (NN-03, NN-16) acknowledged, data-protection roles (DPA reference). Signed by the customer sponsor (e-sign) and the Equator CSM; for API/BYOK tenants the Equator security lead co-signs. Hypercare: daily stand-up task for 10 working days, weekly afterwards; exit criteria configurable.

---

## X.6 Customer success and after-sales

### X.6.1 Health score (explainable, deterministic; RB AU-12)

`health = Σ wᵢ × componentᵢ` (0–100), recomputed daily; each component and its inputs are shown ("Why this score?"). Default weights (tier T, changes maker-checker by `ops_director`):

| Component | Weight | Inputs (from read models, aggregates only) | Scoring (default) |
|---|---|---|---|
| Adoption | 30 | active users 30 d ÷ seats; feature breadth (enabled ÷ entitled); logins trend | linear bands; < 30 % active → 0 |
| Usage vs allowance | 20 | meters ÷ allowance (App. O §4.3); committed-use attainment (App. O §2.4.2) | 60–100 % → full; < 30 % → 0; > 100 % sustained → full + expansion signal |
| Support experience | 15 | open P1/P2 tickets, ticket CSAT 90 d, reopen rate | P1 open → 0 |
| Commercial | 15 | dunning state, overdue days (`fin_receivables_view`) | `past_due` → 5; `suspended_soft` → 0 |
| Engagement | 10 | QBR held in last 120 d, success-plan milestones on track, sponsor still active | — |
| Sentiment | 10 | latest NPS (process questions only) from the account's admins | promoter 10, passive 5, detractor 0 |

**Excluded inputs (locked):** case outcomes, settlement or award rates, recoveries, neutral identity or performance, the account's results as a party, complaints by the account's counterparties. Rationale: health must never create an incentive to influence case handling (D3-24). Health bands: ≥ 70 healthy, 40–69 watch, < 40 at risk.

### X.6.2 Playbooks

Configurable playbooks (`ops.cs_playbooks`): trigger (health band change, renewal window, adoption drop > 20 % in 30 days, sponsor left, P1 ticket, NPS detractor), steps (tasks, templated outreach drafts, meeting booking, training offer), owner, exit condition. Outreach is drafted, never auto-sent, when the playbook trigger is a complaint, an NPS detractor or a commercial dispute (human-approval list).

### X.6.3 Success plans and QBRs

- **Success plan:** customer objectives (from the customer, in their words), measures (product metrics only — e.g., "GRM tickets acknowledged within 48 h ≥ 98 %"), milestones, owners, review dates.
- **QBR pack** (generated DOCX/PPTX + PDF; RB AU-12/13): usage and adoption, service metrics (`svc_account_service_stats` aggregates: volumes by stage, SLA attainment, notice delivery, clock breaches), support summary, roadmap items, success-plan progress, renewal timeline, data-protection items (DSRs handled for the tenant as processor, breaches nil/notified). **Never in a QBR:** settlement or award rates presented as performance, neutral names or scores, individual matter details, any "win" framing (NN-16, NN-28). `analytics_narrator` may draft the narrative from aggregates; a CSM approves.
- QBR meeting: Teams via `WORKSPACE_PORT`; minutes logged; follow-up tasks auto-created (OA-14).

### X.6.4 NPS and CSAT (process-only)

| Survey | Audience | Trigger | Questions (default) | Rules |
|---|---|---|---|---|
| Relationship NPS | Tenant admins and sponsors of B2B accounts | Every 6 months; not within 30 days of a P1 incident | "How likely are you to recommend Equator's platform and service to a colleague?" (0–10) + "What is the main reason?" | Never sent to parties, respondents, neutrals or GRM complainants; never asks about case outcomes |
| Ticket CSAT | Ticket requester | Ticket solved | "How satisfied are you with how we handled this request?" (1–5) + comment | Not sent for grievances (they get the grievance feedback form) or for tickets classified `case_procedure` from a respondent (to avoid any appearance of courting a party) unless the requester opted into service surveys |
| Onboarding CSAT | Project sponsor and key users | Hand-over | Process questions | — |
| Training CSAT | Attendees | Session end | Content and delivery questions | — |

Results are aggregated with n ≥ 5 before display outside the owning CSM (X-28 pattern); verbatims are moderated for personal data before entering reports; scores never feed neutral grading or allocation.

### X.6.5 Renewals, expansion and churn risk

- **Renewals:** `RenewalWatchWorkflow` creates a `renewal` opportunity at T-120 days (enterprise) or T-60 (SaaS), tasks at T-90/T-60/T-30; customer-facing reminders are Appendix O §6.6 messages sent by `billing` (T-30/T-7/T-1, auto-renew rules), not by EOP; EOP never changes auto-renew settings.
- **Retention offers:** only within pre-approved bands (`tenant.ops.cs.retention_offer_bands`; RB AU-20); outside the band → maker-checker with `finance_ops`.
- **Expansion:** signal when an allowance exceeds 80 % (RB AU-14) or seats are full; the CSM approves any offer; **no upsell banner, prompt or message appears inside a case view or a hearing**; in-product banners only in the tenant's settings/billing area.
- **Churn risk:** rule-based (`health < 40`, `sponsor_left`, `dunning ≥ D+7`, `NPS detractor`, `downgrade intent`) with a reason list; churn reason codes captured at cancellation; win-back (AU-20) is Appendix Y's marketing automation with at most 2 messages.

### X.6.6 After-sales service

Service requests that are not incidents (configuration changes, new users, new templates, additional training, report requests, data exports, contract amendments) are tickets of type `service_request` with catalogue items (`ops.tkt_service_catalogue`: item, fulfilment queue, SLA, approval needed, chargeable flag linked to RS-27 implementation services, RS-39 data migration, RS-40 onboarding packages or RS-41 premium support (Appendix AB)). Chargeable items create a draft order line for `finance_ops`; nothing is billed from EOP.

---

## X.7 Support desk

### X.7.1 Channels and intake

| Channel | Intake | Identity | Notes |
|---|---|---|---|
| Web help centre form | `/help/contact` (public) | email/mobile OTP for status tracking | Category picker first; KB deflection shown before submit (RB AU-16) |
| Portal "Help" panel | `/app/help` in every portal | authenticated user; tenant and role attached | Case link added only by the user choosing one of **their own** cases; stored as `case_ref` + `case_link_verified = true` |
| Email | `support@equatorresolution.in` (SES inbound → `ops`); optional M365 shared mailbox connector (`tenant.ops.support.m365_mailbox.enabled`, OFF) | sender email matched to contact | Threading by `Message-ID`/`In-Reply-To`; auto-reply with ticket number; attachments scanned |
| WhatsApp | Equator business number via `MESSAGING_PORT` (Gupshup/MSG91) | phone matched to contact | Replies inside the provider's customer-service window; outside it only approved utility templates **[VERIFY — open: current Meta window and template category rules with the BSP]**; no marketing |
| Phone | Equator support DID via `TELEPHONY_PORT`; IVR language menu | caller ID matched | Call recorded only after the disclosure prompt; recording retained per retention class `support_call` (default 180 days); callbacks to borrowers in FIN matters within 08:00–19:00 (NN-12) |
| Partner portal | `/partners` help | partner token | Partner tokens cannot attach case links (P13 FR-P13-V2-S1) |
| Internal | EOP "Raise on behalf" | staff | Records the original channel and time |

All channels create `ops.tickets` with the **original received time** (clock start), channel, requester, company, and a classification. Abuse/spam filter quarantines but never deletes (reviewed daily).

### X.7.2 Categories (seed; tier T within locked top level)

Top level is locked because it drives routing to legally distinct processes:

| Top level (locked) | Sub-categories (configurable) | Routes to |
|---|---|---|
| `account_access` | login, MFA reset (no factor bypass — Appendix S), SSO, invites | Support L1 |
| `billing` | invoice copy, GST details, failed payment, mandate, refund request, plan change | Support L1 → finance ops hand-off; refund requests always to P05 maker-checker |
| `product_how_to` | per product line | Support L1; KB |
| `technical_issue` | bug, outage, integration, API, webhook | Support L2 → engineering (incident if SEV) |
| `case_procedure` | how to respond, deadlines, hearing joining, document upload, fees for a case | Case Services queue; **answers are procedural only, from approved scripts; never merits or legal advice** (NN-01; ESC-2026.1) |
| `data_protection` | access, correction, erasure, consent withdrawal, privacy question | DPO desk (Q §2.4 DSR workflow; ticket becomes a linked DSR) |
| `complaint_service` | staff conduct, billing dispute, accessibility, delay, privacy (complaint) | Grievance conversion (§X.8.2) |
| `complaint_neutral` | conduct of a neutral | Appendix N §7.7 complaints process; EOP keeps metadata only |
| `safety_urgent` | threat, harassment, self-harm risk, urgent safety | `safeguarding_lead` immediately (break-glass rules, Appendix S §6.6); never auto-replied beyond a safety acknowledgement with emergency numbers |
| `posh_related` | anything indicating a POSH complaint | Customer's IC through the sealed channel signpost; EOP stores no narrative (NN-07) — the ticket body is purged after routing and replaced with "Routed to sealed channel" |
| `feedback_feature` | suggestions | Product board |
| `partnership_media` | press, partnership, vendor | PR/partnerships (Appendix Y) |

### X.7.3 Priority and SLA

Priority = impact × urgency matrix (P1 critical: platform unavailable, a live hearing cannot proceed, a statutory deadline at risk within 48 h; P2 high: a function blocked for many users or a deadline within 7 days; P3 normal; P4 low). **Deadline awareness:** a ticket with a verified case link whose case has a clock due within 7 days is raised to at least P2, and within 48 h to P1 (from `tkt_case_context`, dates only).

| Priority | First response (business hours) | Next response | Resolution target | Escalation |
|---|---|---|---|---|
| P1 | 30 min (24×7 for platform and live-hearing issues) | 60 min | 4 h workaround | auto to `support_lead` at 50 % elapsed; `ops_manager` at 100 % |
| P2 | 2 h | 4 h | 1 business day | lead at 75 % |
| P3 | 8 h | 1 business day | 3 business days | lead at 100 % |
| P4 | 2 business days | 3 business days | 10 business days | — |

Enterprise contracts may set stricter targets (`core.enterprise_sla_policies`, P09 FR-P09-20); SLA clocks use the company business calendar (Indian holidays by state) except P1 24×7 rows. Clocks pause only in `awaiting_customer` and only for SLA purposes; **statutory grievance clocks never pause** (§X.8).

### X.7.4 Ticket state machine

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| `new` | auto-classify / agent triage | category set | `open` | routing rule applied; SLA clock starts at received time |
| `open` | agent replies publicly | — | `pending_customer` or `open` | first-response SLA met |
| `open` | escalate | reason | `escalated` | owner changes to L2/lead/other department; watchers notified |
| `escalated` | handed back | — | `open` | — |
| `open` / `escalated` | internal dependency (engineering, finance, case services) | linked task | `on_hold_internal` | SLA continues |
| `pending_customer` | customer replies | — | `open` | SLA resumes |
| `pending_customer` | no reply 7 days (2 reminders) | not `complaint_*` | `solved` | auto-close notice |
| `open` | resolution recorded | resolution code set; public reply sent | `solved` | CSAT survey (§X.6.4) |
| `solved` | customer reopens ≤ 7 days | — | `open` | reopen counter |
| `solved` | 7 days elapse | — | `closed` | read-only |
| any | complaint trigger (§X.8.2) | — | `converted_to_grievance` | grievance created; ticket linked; requester told the grievance number and timelines |
| any | merge into another ticket | same requester or same incident | `merged` | messages moved |

### X.7.5 Routing, macros, notes, updates, resolution codes

- **Routing:** skills (product, language, channel, tier), load balancing with a per-agent cap, VIP/enterprise queues, language routing (en, hi + configured languages), follow-the-sun off.
- **Macros:** versioned reply templates with variables (`{{ticket.number}}`, `{{requester.first_name}}`, `{{kb.link}}`); macros touching fees, refunds, complaints or case procedure carry `legal_approved_version` and cannot be edited at send time beyond fields marked editable.
- **Internal notes** never visible to the requester; a note cannot be converted to a public reply without re-review; @mentions create tasks.
- **Customer updates:** public replies, status-change notices, incident broadcasts to all tickets linked to an incident (`tkt_incident_links`).
- **Resolution codes** (seed): `answered_kb`, `configuration_changed`, `bug_fixed`, `workaround`, `refund_routed`, `duplicate`, `no_response`, `out_of_scope_signposted`, `routed_case_services`, `routed_dpo`, `routed_grievance`, `routed_safeguarding`, `routed_neutral_complaints`.
- **Customer-visible status** in `/app/help` and by tracking link: received, in progress, waiting for you, solved — with the ticket number and expected next update.

### X.7.6 Case-linked tickets (neutrality and confidentiality)

A ticket linked to a case is `case_linked = true`: the body is classified `confidentiality_tier = high`; it is excluded from AI training, from segments, from CRM activity timelines visible to sales, and from QBRs; support agents see the case only through `tkt_case_context` and, where they need more, a time-bound **support grant** (Appendix S `support_agent` "R [ticketed support grant]", ≤ 24 h, read-only, logged) that opens the case record in the case console with documents at **metadata level only** (Appendix S RBAC: documents "R metadata"); no evidence, pleading, caucus or offer content is visible, and nothing from that view is copied into `ops`. Agents never relay messages between parties, never comment on merits, and hand any procedural decision (extension requests, adjournments, document admissions) to the case manager in `/console`.

---

## X.8 Grievance redressal (Equator's own users; EGP-2026.1)

### X.8.1 Scope

Complaints about **Equator's service**: staff conduct, billing, privacy handling, accessibility, delays, platform failures, marketplace transactions and listings (where Equator is the marketplace e-commerce entity — RE F3.1), and content on Equator's intermediary surfaces (RE F3.3). Out of scope (signposted, tracked as metadata): the decision in a case (only the remedy the law allows — e.g., A&C Act s.34), a neutral's conduct (Appendix N §7.7), POSH complaints (the employer's IC; NN-07), a tenant's own customers' grievances (the tenant's GRM desk, P09).

### X.8.2 Conversion triggers (ticket → grievance)

A ticket converts when any of: (a) the requester uses the words complaint/grievance/शिकायत or selects "This is a complaint" (explicit); (b) category is `complaint_service`; (c) the requester is dissatisfied with a solved ticket and reopens with a complaint; (d) an agent judges it a complaint (reason recorded). A conversion can be reversed only by the Grievance Officer with reasons sent to the complainant. The **original received time of the first message** starts the grievance clocks.

### X.8.3 Clock rule packs (tier G; strictest applies)

| Rule pack | Applies to | Acknowledge | Resolve | Source | Status |
|---|---|---|---|---|---|
| `rulepack.IN.grievance.equator_policy@2026.1` | All service complaints | 48 h | 30 days | EGP-2026.1 (App. U §U.6.4) | Board approval pending |
| `rulepack.IN.grievance.ecommerce@2026.1` (instrument: E-Commerce Rules 2020) | Marketplace transactions and Equator's own online services sold to consumers | 48 h | 1 month from receipt | Consumer Protection (E-Commerce) Rules 2020 r.4(5) [RE F3.1] | Treated as applicable by default (counsel to confirm characterisation, App. O §6.1) |
| `rulepack.IN.grievance.ecommerce@2026.2` (instrument: Amendment Rules 2026; `effective_from` = commencement) | Same, from commencement of the 2026 Amendment | as above + copy of complaint as recorded (r.4(5)); NCH convergence (r.4(7)) | as above | Consumer Protection (E-Commerce) (Amendment) Rules 2026 [RE F3.1] | **[VERIFY — open: commencement 1 Jan 2027 per secondary source; Gazette text not opened]** |
| `rulepack.IN.grievance.it_intermediary@2026.1` | Complaints about user-generated content on Equator's intermediary surfaces (neutral bios, chambers pages, reviews) | 24 h | 7 days (specified content takedown 3 h) | IT Rules 2021 r.3(2) as amended by G.S.R. 120(E), 10 Feb 2026 [RE F3.3] | **[VERIFY — open: amendment text; RE cites pack research, not the Gazette]** |
| `rulepack.IN.grievance.dpdp@2026.1` (instrument: DPDP Rules 2025) | Privacy grievances | 48 h (internal) | 30 days internal; ≤ 90 days statutory outer limit | DPDP Act 2023 s.13; DPDP Rules 2025 r.14(3) (App. Q §2.4) | Verified in App. Q |

Version suffixes follow Appendix V §V.2.1: `@YYYY.N` is the Nth approved version in the approval year (all seeds above are approved in 2026); the instrument and its year are pack metadata (citation), and the Amendment is a later version of the same pack whose `effective_from` is the commencement date. If the Amendment pack is approved in 2027 it becomes `@2027.1`.

`due_at = min(applicable resolve deadlines)`; T-7, T-3 and T-1 alerts; a breach is a Critical incident (NN-04 pattern) reported to `ops_director` and the Company Secretary.

### X.8.4 Implementation on the GRM engine (D3-21)

Variant `EQ_SERVICE` in `grm.sla_policies` for the Equator institution tenant; states as P09 §5.1 minus RBI-specific ones (`io_review` replaced by `level2_review` for the Company Secretary appeal). EOP's Grievance desk is a UI over the GRM APIs with the `grievance_officer` role scoped to `EQ_SERVICE`. Final reply must include: the decision with reasons, what Equator will do, how to appeal to the Company Secretary within 30 days, and external remedies where they exist (e.g., National Consumer Helpline / consumer commission for consumer complaints; the Data Protection Board after exhausting the fiduciary's process for privacy, DPDP s.13(3)) — wording from approved templates. The Grievance Officer's name and contact come from `tenant.legal_entity` (X-15). Quarterly summary to the Transparency Report (App. N §6.7) with counts by category, median resolution time and breaches (k ≥ 10 rule for any cell, X-28).

---

## X.9 Knowledge base and help centre

| Space | Audience | Content | Approval | Surface |
|---|---|---|---|---|
| `internal_sop` | Staff (department-scoped) | SOPs, runbooks for operations (not engineering runbooks, which stay in `docs/runbooks/`), escalation matrices | Department head; legal reviewer if it states law | EOP |
| `playbooks` | CS, sales, onboarding | Playbooks, objection handling (truthful; Claims Register for any number, NN-17) | Department head + legal for claims | EOP |
| `scripts` | Support, case-services help | Call/chat scripts, procedural answers | **Legal reviewer mandatory** for `case_procedure`, fees, refunds, complaints | EOP; macros |
| `templates` | All | Email/letter templates, proposal and QBR templates (DOCX/XLSX/PPTX) | Owner + legal for customer-facing legal text | EOP; generated documents |
| `public_help` | Public, customers, parties | How-to articles, FAQs, fee explainers (live fee blocks from the fee engine), accessibility help | P13 CMS legal workflow (FR-P13-09): legal reviewer ≠ author; prohibited-phrase linter; Claims Register | `/help` on `apps/web` (server-rendered, indexable, en + hi) |

Articles are versioned (`ops.kb_articles`, `ops.kb_versions`) with owner, review-due date (default 12 months; 6 months for fee/legal articles), "last reviewed" stamp, feedback ("Was this helpful?") and deflection analytics (search → view → no ticket within 24 h). Public help articles are authored in EOP but **published through the P13 CMS** so the legal workflow and linter apply once; the CMS is the system of record for public text.

---

## X.10 Openness (NN-40): systems of record, Brevo, migration, connectors, API and exports

### X.10.1 Declared systems of record (D3-22; rows in `cfg.system_of_record`, Appendix AC §AC.12.1, tier G — change needs ADR + DPO)

This table refines Appendix AC §AC.12.1 for EOP categories. AC §AC.12.1 (as integrated on 23 October 2026) already names `ops.crm_*` as the CRM system of record from P16 (X-51) and `mkt.touchpoints` (normalised raw events) and `mkt.metric_snapshots` (reported figures) for campaign send results and published-post metrics (X-53; Appendix Y §Y.1.3).

| Data category | System of record | Copies / sync | Direction |
|---|---|---|---|
| Accounts, contacts, leads, opportunities, quotes metadata, activities | Equator CRM (`ops`) | Brevo (contacts, companies, deals); HubSpot/Zoho/Salesforce (if enabled) | Equator → external; inbound field updates accepted only for allow-listed fields with last-writer rules (§X.10.2) |
| Consent and communication preferences | `core.consent_records` (mirrored in `ops.crm_comm_prefs`) | Brevo list membership / blacklist; external CRM opt-out flags | Both: opt-outs from any side apply everywhere ≤ 15 min; **opt-ins are never accepted from an external tool** without the consent artefact |
| Email engagement events (opens, clicks, bounces, spam) | Brevo for raw events | Normalised copy in `mkt.touchpoints` (Appendix Y) | Brevo → Equator |
| Campaigns, sequences, social calendar | Appendix Y (`mkt`) | Brevo campaigns | Equator → Brevo |
| Plans, subscriptions, invoices, receivables | `billing` (P05) | Read model in `ops` | Core → ops only |
| Tickets, grievances, KB | `ops` / `grm` / CMS (public help) | none by default | — |
| Staff directory | HRMS (`hr`) | `ops.ws_staff_directory` projection; M365 users | HRMS → ops; HRMS → M365 (Appendix AC) |
| Meeting records for ops meetings | M365 (collaboration surface only; RD F1.4: never system of record for retained records) | join URL + minutes in `ops.crm_activities` | M365 → ops (links) |

### X.10.2 Brevo connector (`CRM_PORT.brevo` contacts/companies/deals; `MARKETING_PORT.brevo` belongs to Appendix Y)

| Equator object | Brevo object | Mapping notes |
|---|---|---|
| `crm_contacts` (only `marketing_eligible` or `existing_customer` with transactional-business purpose) | Contact (`/v3/contacts`) | Email as key; attributes: `EQ_ID`, `PERSONA`, `LANGUAGE`, `COMPANY_CODE`, `SEGMENT_CODES`, consent flags per purpose; no case fields exist to map |
| `crm_segments` | Contact attribute `SEGMENT_CODES` only | `CRM_PORT` pushes no send lists: Appendix Y materialises approved audience snapshots (`mkt.audience_snapshots`, built from `ops.crm_segments` over `ops.crm_marketing_view`) as static Brevo lists through `MARKETING_PORT` (§Y.6.7); Brevo segments are never a source of truth |
| `crm_accounts` | Companies (CRM scope `crm`) | Name, domain, `EQ_ACCOUNT_ID`, kind, size band |
| `crm_opportunities` | Deals (`POST /v3/crm/deals`: `name`, `attributes.deal_owner`, `pipeline`, `deal_stage`; `linkedContactsIds`, `linkedCompaniesIds`) | Pipeline/stage IDs stored in provider config; one-way Equator → Brevo |
| `ws_tasks` (sales) | Tasks | One-way Equator → Brevo |
| Opt-out (`unsubscribed`, `contactDeleted`, `hardBounce`, `spam`) | Webhook events | Inbound → consent withdrawal / bounce flag after re-fetch (below) |

**Constraints from [RD F3.1] and compensating controls.**

| Constraint | Control |
|---|---|
| EU hosting (OVH France/Germany, Google Cloud Belgium); no India region | Transfer-register row `BREVO_EU` (data class `personal`, CRM/marketing data only); residency ADR; DPA and sub-processor list obtained before activation (CS-owned contract); one connector flag for both ports, `mkt.brevo.enabled` (G, **OFF**; owner Appendix AC §AC.17); CRM-object sync additionally needs `tenant.ops.connectors.brevo_crm_sync.enabled` (**OFF**), which cannot be turned ON while `mkt.brevo.enabled` is OFF or before the DPA record, the DPDP s.16 check and DPO approval exist |
| **No HMAC webhook signature** documented | Per-subscription bearer token (rotated ≤ 90 days) + Brevo IP allow-list + **re-fetch the contact from the API before applying** any consent-affecting event; unmatched events quarantined (`OPS_WEBHOOK_UNVERIFIED`) |
| Rate limits: contacts 10 rps / 36,000 per h (General); **all other endpoints 100 per h** on non-Enterprise plans (CRM/campaign endpoints likely in the catch-all — NC) | One shared budget for the Brevo account, `tenant.mkt.brevo.max_requests_per_hour` (default 80; Appendix AC §AC.5, §AC.17; RD's `brevo.crm.max_requests_per_hour` is an alias), split between `CRM_PORT` and `MARKETING_PORT` sync by one token bucket; bulk import above 50 records; queue-based incremental sync every 5 min; never synchronous per UI action; 429 → `RATE_LIMITED`, exponential backoff with jitter (no Retry-After documented) |
| India SMS/WhatsApp DLT support not confirmed | Brevo used for email marketing and CRM only; `mkt.brevo.sms_whatsapp.enabled` (alias of RD's `growth.brevo.sms_whatsapp.enabled`, Appendix Y X-55) OFF (RD DI-B.9) |
| Retry policy and CRM-webhook configuration not confirmed | Nightly reconciliation job compares counts and opt-out sets in both directions; drift > 0 for opt-outs is a P1 privacy ticket |

### X.10.3 Migration both ways

`CrmMigrationWorkflow` (Temporal; tier G for the approval, T for mappings) supports **Equator → Brevo / HubSpot / Zoho / Salesforce / CSV** and **those → Equator**:

1. **Inventory:** objects and counts on both sides; custom fields; pipelines/stages.
2. **Field mapping** (a mapping set in `cfg.field_mappings` / `cfg.mapping_sets`, Appendix AC §AC.12.2; consent and identity fields make it tier G): source field → target field, transform (trim, case, E.164, date format, picklist map), default, required; unmapped fields listed and either mapped to a custom field or exported to an archive file.
3. **Dry-run:** full read, transform and validation without writes; report of creates/updates/conflicts/rejections; sample of 50 transformed records for human review.
4. **Dedupe:** §X.4.9 rules applied across the combined set; conflict resolution policy chosen (source wins / target wins / most recent / manual queue).
5. **Consent preservation:** consent status, purpose, timestamp, notice version and source travel with each record; records arriving without consent evidence are imported as `non_marketing`; withdrawals and suppression always win; respondent-hash and DND checks run on inbound data.
6. **Approval:** maker (`ops_manager`) → checker (`ops_director`) + DPO for any migration of > 1,000 people or to a new external processor.
7. **Cut-over:** freeze window, delta sync, switch of system of record recorded in `cfg.system_of_record` (only for categories where an external SoR is permitted — never consent).
8. **Reconciliation:** counts per object and checksum of key fields on both sides; consent-set equality check (must be exact); report signed by checker.
9. **Rollback:** restore point (before-images) kept 30 days; outbound rollback deletes records created in the target by run id where the target API allows, otherwise produces a deletion list.
10. **Rehearsal:** at least one full rehearsal in staging per connector before production activation (EOP-L11).

### X.10.4 Generic CRM connector port

`CRM_PORT` (Appendix D §D.9) is extended:

```ts
export interface CrmPortV3 extends CrmPort {
  capabilities(): { objects: Array<'contact'|'company'|'deal'|'task'|'note'>; bulkImport: boolean; webhooks: 'hmac'|'bearer'|'none';
                    rateBudget: { perHour: number; perSecond?: number }; residency: string };
  upsertBatch(object: string, rows: MappedRecord[], opts: { idempotencyKey: string; dryRun?: boolean }): Promise<BatchResult>;
  exportAll(object: string, since?: Date): AsyncIterable<ExternalRecord>;            // migration inbound
  applyOptOut(email: string, purpose: string): Promise<void>;                        // ≤ 15 min SLA
  verifyWebhook(req: InboundRequest): Promise<{ ok: boolean; reason?: string }>;   // HMAC or bearer + IP + re-fetch
}
```

Adapters: `brevo` (P16), `hubspot` and `zoho` (moved from P13; webhook signing per D.9 — HubSpot `X-HubSpot-Signature-v3`, Zoho notification token, both to confirm at contracting), `salesforce` (candidate; flag OFF), `csv_file` (always available fallback). Each adapter: provider config row, rate budget, rehearsal record, residency record, failover `none` (native CRM continues).

### X.10.5 Webhooks, public REST API and exports

- **Outbound webhooks** (P09 webhook service, HMAC-SHA256 signing, retries, replay): `ops.lead.*`, `ops.opportunity.*`, `ops.ticket.*` (metadata only), `ops.project.*` for customers' own systems (e.g., an enterprise customer's ITSM receiving its ticket updates) — subscription by the tenant admin, scopes per object, never sealed or case-content fields.
- **Public REST API** (`/v1/ops/...`, OpenAPI 3.1 in the developer portal): OAuth2 client credentials with scopes `ops.crm.read`, `ops.crm.write`, `ops.tickets.read`, `ops.tickets.write`, `ops.kb.read`; per-key rate limits; company-scoped; idempotency keys on creates.
- **Exports** (EQ-EXPORT-1.0, D3-07, D3-41, NN-37; Appendix AC §AC.13): scope `OPS_DEPARTMENT` (department head, `ops_director` checker, aal2-pr) or the company-level scopes of AC; EOP content goes in `05_Operations/` (`CRM_Accounts.xlsx`, `CRM_Contacts.xlsx`, `CRM_Leads.xlsx`, `CRM_Opportunities.xlsx`, `CRM_Activities.xlsx`, `Onboarding_Projects/`, `Tickets.xlsx` + `Tickets/` threads as PDF/A, `Grievances.xlsx` + records as PDF/A, `Knowledge_Base/` as DOCX, `SLA_Report.xlsx`) with CSV + JSON data copies, `00_README.pdf`, `99_Manifest/` and checksums; every run writes `xpt.export_runs`; exports containing personal data of > 100 people are maker-checker (NN-36) and watermarked; free at exit; AC path budget applies.

---

## X.11 Microsoft 365 hooks for operations staff (via `WORKSPACE_PORT`, Appendix AC)

| Hook | Graph operation (RD F1.3) | Permission model | Basic SKU? | Rules |
|---|---|---|---|---|
| Teams meeting for onboarding, training, QBR, sales demo | `POST /users/{id}/events` with `isOnlineMeeting: true`, `onlineMeetingProvider: "teamsForBusiness"` (calendar-backed) | `eq-ops-collab` app; `Calendars.ReadWrite` scoped; `OnlineMeetings.ReadWrite.All` with an application access policy limited to the `eq-meeting-hosts` group | ✓ (300 attendees) | Join URL on the CRM activity; **never for hearings or any case session** (hearings stay on `VIDEO_PORT`); customer invitees receive the invite from the staff member's mailbox |
| Outlook calendar availability for booking pages | free/busy read for the host (delegated or application calendar read) | scoped as above | ✓ | Booking page shows slots only; no calendar content leaves M365 |
| Meeting follow-ups | transcripts `GET …/onlineMeetings/{id}/transcripts` (`.vtt`) where recording/transcription is licensed and enabled | `OnlineMeetingTranscript.Read.All` (same access policy) | **[VERIFY — open: transcription/recording on Basic]** | Only for internal or B2B meetings where every attendee was told; AI summary is a draft for the organiser (`meeting_followup` agent, §X.12.5 OA-15); transcripts are not stored in `ops` beyond 30 days unless attached by the organiser |
| SharePoint document links | `POST /drives/{id}/items/{id}/createLink` (organisation or specific people, with expiry) | `Sites.Selected` per site | ✓ | EOP stores the link and the file's SHA-256; **M365 is never the system of record** for retained records (RD F1.4); case documents never go to SharePoint except through a governed export |
| Shared support mailbox (optional) | mailbox read/send for `support@` if hosted in Exchange | Exchange application RBAC scoping (**[VERIFY — open: mechanism, RD Open point 2]**) | ✓ | Flag OFF by default (SES inbound is the default intake) |

Capability matrix per SKU (Appendix AC seed) hides actions the tenant's SKU cannot perform. Google Workspace equivalents (`google_workspace` adapter: Calendar `events.insert` with Meet link; Drive sharing) stay behind `ops.workspace.google.enabled` = OFF; Google Workspace offers no India data region (RD F2), so enabling it needs a residency ADR and Company Secretary + DPO approval (Appendix AC §AC.17).

---

## X.12 Automation engine ("autopilot")

### X.12.1 Model

An **automation** = `trigger` → optional `conditions` → ordered `actions` (with branches, waits and approval steps) → `exception path`. Definitions are versioned JSON (`ops.wf_automations`, `ops.wf_automation_versions`) executed by Temporal (`AutomationRunWorkflow`, one run per trigger event, idempotent by `(automation_version_id, trigger_event_id)`).

| Element | Catalogue (P16 seed) |
|---|---|
| Triggers | record created/updated/field changed (lead, contact, account, opportunity, ticket, project, task); stage changed; SLA timer at % elapsed; schedule (cron in IST); date-relative (renewal T-n, hypercare end); health band changed; segment entered/left; inbound message (email/WhatsApp) received; form submitted (`growth`); event from allow-listed core events (`billing.subscription.*`, `billing.invoice.overdue`, `enterprise.tenant.provisioned`, `identity.sso.configured`); webhook from a connected tool (verified) |
| Conditions | field comparisons; segment membership; business hours; company; owner availability; consent status; counts over a window; previous run outcome |
| Actions | assign owner / queue (routing rule); create task / checklist; create ticket; change field (allow-listed fields only); add/remove tag; add to static segment; send **templated** internal notification (in-app, email, Teams chat message to an internal channel **[VERIFY — open: Graph chat permission on Basic]**); draft an external message (always a draft unless the template is pre-approved for auto-send and the action is not on the approval list); schedule a Teams meeting (draft invite); generate a report or document (DOCX/XLSX/PDF) from a template; call an internal API from the allow-list; post an outbound webhook; wait (duration / until event); request approval (named role, deadline, fallback) |
| Exception paths | retry policy (max 5, exponential); on failure → fallback assignee task + `ops.wf_exceptions` row; dead-letter after max retries; notify automation owner; auto-pause after `tenant.ops.automation.auto_pause_failures` (default 20) failures in 1 h |

### X.12.2 Permissions

| Action | Who |
|---|---|
| Create/edit draft automation | Department roles with `automation.author` for their department's objects |
| Publish | `automation.publisher` in the same department (≠ author; maker-checker) — `ops_manager`, `support_lead`, `bd_manager`, `customer_success_manager` lead, `marketing_manager` (Y automations) |
| Publish an automation that touches money, consent, external messages to > 500 recipients, or another department's records | Checker from the affected function + `ops_director` |
| Pause | Author, publisher, department head, `ops_director`, DPO (any automation touching personal data), `compliance_officer` (any) |
| Global kill switch (`tenant.ops.automation.global_pause`) | `ops_director`, DPO, `it_admin` |

### X.12.3 Preview, simulation and rate limits

- **Preview:** shows the compiled graph, every field it can change, every recipient class, and the approval steps; a **simulation** runs the automation against the last 30 days of matching events in read-only mode and reports how many runs, actions and messages would have occurred.
- **Rate limits** per automation (default 1,000 runs/h; external drafts 200/h; outbound webhooks 600/h) and per company; per-recipient frequency cap for any external communication (default 1 message/24 h per automation, 3 per 7 days across automations); external-tool budgets (Brevo `tenant.mkt.brevo.max_requests_per_hour`, default 80 req/h for the whole account) are shared and enforced by the connector.
- **Loop guard:** an automation cannot trigger itself through its own field changes; chains deeper than 3 automations are cut and logged (`OPS_AUTOMATION_LOOP`).

### X.12.4 Audit, pause and rollback

Every publish, pause, resume and rollback writes the audit chain with the version diff; every run stores trigger, inputs (IDs only), decisions, actions and outcomes (`ops.wf_runs`, 13 months). **Rollback** re-publishes a previous version (maker-checker waived for rollback to the last approved version); **compensation** for runs already executed is listed (e.g., "unassign 34 leads") and executed only on explicit confirmation. Pause stops new runs within 60 s; in-flight runs finish their current action and stop at the next step.

### X.12.5 Operations automation catalogue (X-owned; Y-owned items listed for coordination)

| ID | Automation | RB ref | Trigger | Actions | Approval | Default |
|---|---|---|---|---|---|---|
| OA-01 | Lead ingest, dedupe and suppression | AU-01 | `growth.lead.created` | promote to `ops`, dedupe, suppression check | — | ON |
| OA-02 | Enrichment (public company data) | AU-02 | lead/account with GSTIN/CIN | fetch via licensed aggregator | — | ON |
| OA-03 | Lead routing and speed-to-lead SLA | AU-03/04 | lead qualified | route, SLA timer, acknowledgement (pre-approved template, opt-in channel only) | Scoring model changes: head of sales | ON |
| OA-04 | Quote approval routing | AU-08 | quote submitted | route to band holder / finance / legal | Maker-checker (locked) | ON |
| OA-05 | Provisioning hand-off | AU-10 | order form + DPA signed | create provisioning task for platform team; create onboarding project | Security review for API/BYOK | ON |
| OA-06 | Onboarding project creation and task generation | AU-11 | `equator.ops.opportunity.won.v1` | project from template, milestones, kickoff meeting draft | — | ON |
| OA-07 | Checklist probes and nudges | AU-11 | daily | evaluate probes; remind owners (settings-area only for customers) | — | ON |
| OA-08 | Go-live sign-off request | AU-11 | all pre-go-live milestones done | generate sign-off pack, send for e-sign | CSM go-live decision | ON |
| OA-09 | Health computation | AU-12 | daily 03:00 IST | compute, store explanation | — | ON |
| OA-10 | Health-based check-in | AU-13 | band → at risk | CSM task + outreach **draft** | CSM decides outreach | ON |
| OA-11 | Expansion signal | AU-14 | allowance > 80 % | CSM task; settings-area banner | CSM approves offer | ON |
| OA-12 | Renewal pipeline | AU-18 | T-120/T-60 | renewal opportunity, tasks | Retention offers within bands | ON |
| OA-13 | Ticket triage, assignment and AI draft | AU-15 | ticket created | classify, route, suggest KB, draft reply | **Human sends** fees/refunds/complaints/procedure | ON |
| OA-14 | SLA escalation | AU-15 | SLA % elapsed | escalate per matrix, notify | — | ON |
| OA-15 | Meeting follow-up | — | Teams meeting ended (ops) | draft minutes and tasks from transcript where available | Organiser approves | ON (where licensed) |
| OA-16 | Grievance clock alerts | AU-17 | grievance clock T-7/T-3/T-1 | alert GO, escalate to CS on breach risk | GO owns outcome | ON (always_on) |
| OA-17 | Collections hand-off | AU-19 | invoice overdue +7 (enterprise) | CSM + finance-ops task; no customer message from EOP (billing sends dunning) | Finance approves write-offs (P05) | ON |
| OA-18 | Scheduled report generation | — | cron | QBR data pack, weekly SLA report, monthly leadership pack (DOCX/XLSX/PDF) | Distribution list approval at publish | ON |
| OA-19 | Stale-record hygiene | — | weekly | flag leads inactive 24 months for deletion review (P13 retention) | DPO-approved retention rule | ON |
| OA-20 | Partner payout hand-off | AU-21 | `equator.mkt.referral.reward_approved.v1` (Appendix Y MA-17 attributes and `finance_ops` approves the reward) | create the P05 payout request (RP-01 cash) or service-credit request (RP-02) for `reward_eligible` partners only; attribution link on `crm_referrals` | P05 maker-checker (`accounts_maker`/`accounts_checker`) executes; any professional flag blocks (X-54, master X-62) | ON |
| Y-owned | Marketing captures to CRM (MA-03), nurture sequences, regulatory-deadline campaigns, webinars, win-back, review/case-study requests, social calendar, PR and MoU tracker, referral attribution and rewards (MA-17) | AU-05/06/07/20/21/22/23/24 | — | Built on this engine by Appendix Y (MA-01–MA-32) | Per Appendix Y | per Y |
| AA-owned | Sponsored-listing operations | AU-25 | — | Marketplace module (Appendix AA, `mkp`); not EOP or Appendix Y | `compliance_officer` signs the monthly self-audit | **OFF** (`marketplace.paid_placement`, NN-34) |
| — | Group cross-sell | AU-26 | — | — | — | **OFF** (`group.ops.cross_sell.enabled`) |

### X.12.6 Locked human-approval list (no automation may complete these without a recorded human approval)

1. Any **legal conclusion** or statement of a person's legal position, rights or deadlines beyond a pre-approved procedural template.
2. **Eligibility overrides** of any kind (product, plan, programme, SLA exceptions, policy exceptions).
3. **Neutral selection**, recommendation, ranking or any communication suggesting a neutral (and nothing in EOP may do it even with approval — EOP-L06).
4. **Refunds, credits, write-offs, discounts beyond band, payouts, price or fee changes** and any money movement (NN-36).
5. **Sensitive employee decisions**: assignment changes framed as performance action, disciplinary steps, access revocation for cause (HRMS owns; EOP never automates them).
6. **Public claims** and any publication (posts, articles, testimonials, statistics) (NN-17).
7. **Complaints and grievances**: acknowledgements may use pre-approved templates automatically; every substantive reply, rejection, closure or conversion reversal is human.
8. Messages to **parties, respondents or neutrals about a case**, other than pre-approved status notifications.
9. **Consent changes** other than applying a withdrawal (withdrawals apply automatically; grants never come from automation).
10. **Bulk external messages** to more than `tenant.ops.automation.bulk_external_threshold` (default 500) recipients.
11. **Exports** of personal data of more than 100 people and any cross-company data movement (NN-37, NN-38).
12. Deleting records (other than tombstoning duplicates under the merge rules).

---

## X.13 Operations settings catalogue (NN-33 tiers)

Keys follow `<scope>.<module>.<key>` and are registered in the P15 Configuration Studio (Appendix V; G values use V's G-standard / G-elevated / G-legal sub-levels); **L** = locked guardrail, **G** = governed (source, effective dates, maker ≠ checker, preview, rollback, review date), **T** = tenant/company routine setting (immediate, audited, rollback). "Who" = role that may change; "Appr." = approval needed.

| Key | Default | Tier | Who | Appr. |
|---|---|---|---|---|
| `platform.ops.case_projection.allowed_fields` | §X.2.3 list | L | ADR only | — |
| `platform.ops.marketing_sources.forbidden` | tickets, grievances, svc, fin, case_linked, HR | L | — | — |
| `platform.ops.health.excluded_inputs` | outcomes, settlement/award rates, neutral data | L | — | — |
| `platform.ops.automation.approval_list` | §X.12.6 | L | — | — |
| `platform.ops.consent.propagation_minutes_max` | 15 | L (tenant may only tighten) | — | — |
| `platform.ops.leaver.access_revoke_hours_max` | 4 (Q SC-01) | L | — | — |
| `platform.ops.export.personal_data_checker_threshold` | 100 persons | L | — | — |
| `tenant.ops.departments` | D3-06 list | T | `ops_director` | — |
| `tenant.ops.workspace.dashboard_packs` | §X.3.3 | T | department head | — |
| `tenant.ops.crm.pipelines` / `.stages` | §X.4.2 | T (gates: G) | `bd_manager` | gates: `legal_reviewer` |
| `tenant.ops.crm.stage_probabilities` | §X.4.2 | T | `bd_manager` | — |
| `tenant.ops.crm.custom_fields_max_per_object` | 100 | T | `ops_manager` | — |
| `tenant.ops.crm.dedupe.fuzzy_threshold_account` | 0.92 | T | `ops_manager` | — |
| `tenant.ops.crm.unmerge_window_days` | 30 | T (range 7–90) | `ops_manager` | — |
| `tenant.ops.crm.import.checker_threshold_rows` | 1,000 | T (max 1,000) | `ops_manager` | — |
| `tenant.ops.crm.routing_rules` | P13 bands | T | `bd_manager` | > 50 records moved: checker |
| `tenant.ops.crm.speed_to_lead_sla` | 1 h / 4 h / 1 bd | T | `bd_manager` | — |
| `tenant.ops.crm.scoring_model` | P13 seed | G | `bd_manager` | head of sales |
| `tenant.ops.crm.discount_bands` | 5 / 15 / 25 % | G (NN-36) | `finance_ops` | `ops_director` |
| `tenant.ops.crm.contract_board_threshold_minor` | **[Board to set]** | G | Company Secretary | Board resolution ref |
| `tenant.ops.crm.outlook_addin.enabled` | OFF | T | `it_admin` | staff notice updated (NN-35) |
| `tenant.ops.ob.templates` | §X.5.2 packs | T | `ops_manager` | — |
| `tenant.ops.ob.hypercare_days` | 30 | T (10–90) | `ops_manager` | — |
| `tenant.ops.cs.health_weights` | §X.6.1 | T | `ops_director` | maker-checker |
| `tenant.ops.cs.health_bands` | 70 / 40 | T | `ops_director` | — |
| `tenant.ops.cs.retention_offer_bands` | **[Finance to set]** | G | `finance_ops` | `ops_director` |
| `tenant.ops.cs.nps_frequency_months` | 6 | T | CS lead | — |
| `tenant.ops.cs.small_n_display` | 5 | T (min 5) | — | — |
| `tenant.ops.support.priority_matrix` | §X.7.3 | T | `support_lead` | — |
| `tenant.ops.ticket.sla_first_response_hours` | P1 0.5 / P2 2 / P3 8 / P4 16 | T (stricter only for contracted tenants) | `support_lead` | — |
| `tenant.ops.ticket.auto_close_days` | 7 | T (3–14) | `support_lead` | — |
| `tenant.ops.ticket.categories.sub` | §X.7.2 | T (top level L) | `support_lead` | — |
| `tenant.ops.support.call_recording_retention_days` | 180 | G | DPO | `compliance_officer` |
| `tenant.ops.support.m365_mailbox.enabled` | OFF | T | `it_admin` | — |
| `tenant.ops.support.business_calendar` | IN national + state holidays | T | `support_lead` | — |
| `rulepack.IN.grievance.*` (§X.8.3) | as listed | G-legal (floors L) | `grievance_officer` (maker) | Head of Legal (`legal_reviewer`), per Appendix V §V.2 |
| `tenant.ops.grievance.appeal_window_days` | 30 | G | Company Secretary | `legal_reviewer` |
| `tenant.ops.kb.review_months` | 12 (legal/fee 6) | T (max 12) | KB owner | — |
| `mkt.brevo.enabled` (connector flag, both ports; owner Appendix AC §AC.17) | OFF | G (flag) | `marketing_manager` | DPO + DPA record |
| `tenant.ops.connectors.brevo_crm_sync.enabled` | OFF | T (cannot be ON while `mkt.brevo.enabled` is OFF) | `ops_director` | DPO approval recorded |
| `tenant.mkt.brevo.max_requests_per_hour` (shared Brevo account budget; owner Appendix AC §AC.17) | 80 | T (≤ 95 % of plan limit) | `marketing_manager` | — |
| `tenant.ops.connectors.hubspot.enabled` / `.zoho.enabled` / `.salesforce.enabled` | OFF | G | DPO | `ops_director` |
| `ops.workspace.google.enabled` (flag; owner Appendix AC §AC.17) | OFF | G | `it_admin` (maker) | Company Secretary + DPO after residency ADR |
| `tenant.ops.automation.global_pause` | false | T | `ops_director`, DPO, `it_admin` | — |
| `tenant.ops.automation.auto_pause_failures` | 20 / h | T | `ops_manager` | — |
| `tenant.ops.automation.bulk_external_threshold` | 500 | T (max 500) | `ops_director` | — |
| `tenant.ops.automation.recipient_frequency_cap` | 1/24 h; 3/7 d | T (tighten only) | `ops_manager` | — |
| `group.ops.shared_dashboards` | none | G | `group_admin` | Appendix AD grant |
| `group.ops.cross_sell.enabled` | OFF | G | `group_admin` | GDSA + counsel |
| `tenant.ops.guest_access.max_days` | 90 | T (≤ 180) | `ops_manager` | — |

---

## X.14 RBAC matrix for operations roles (least privilege)

Actions: **C** create · **R** read · **U** update · **A** approve (checker) · **X** execute/export · **—** none. Conditions: [own] records owned/assigned; [dept] own department; [acct] accounts the user covers; [agg] aggregates only; [grant] Appendix AD or support grant; [k] masked PII. **No ops role sees case evidence, employee files or another company's data without a grant** (EOP-L01, EOP-L09).

**Table 1 — commercial and customer objects**

| Role | Accounts / contacts | Leads / opps | Quotes | Activities | Consent prefs | Import / merge | Health / renewals | Finance views |
|---|---|---|---|---|---|---|---|---|
| `ops_director` | C R U | C R U A | R A (≤ 25 %) | R | R | A | R U (weights) A | R |
| `ops_manager` | R U | R | R | R [dept] | R | C X A | R | R [agg] |
| `department_head` | R [dept] | R [dept] | R | R [dept] | R | A [dept] | R [agg] | R [agg] |
| `sales_executive` | C R U [own] | C R U [own] | C (≤ 5 %) | C R U [own] | R; change via consent API | C (≤ 1,000 rows) | — | — |
| `bd_manager` | C R U | C R U A | C A (≤ 15 %) | C R U | R | C X A | R [acct] | R [acct, amounts] |
| `partnerships_manager` | C R U [partners] | C R U [partnership] | — | C R U [own] | R | C | — | — |
| `customer_success_manager` | R U [acct] | C R U [renewal, expansion] | C (renewal) | C R U [acct] | R | — | C R U [acct] | R [acct, amounts] |
| `onboarding_specialist` | R [acct] | R [acct] | — | C R U [acct] | R | — | R [acct] | — |
| `support_agent` | R [k] | — | — | C R [ticket] | R; apply withdrawal | — | — | — |
| `support_lead` | R [k] | — | — | R | R | A (ticket merges) | R [agg] | — |
| `case_services_lead` | R [acct, k] | — | — | C R [service] | — | — | — | — |
| `grievance_officer` | R [complainant, k] | — | — | R [grievance] | R | — | — | — |
| `finance_ops` | R | R | R A (terms) | R | — | — | R | R X |
| `accounts_maker` / `accounts_checker` | R [k] | — | R | — | — | — | — | R (+ P05 maker/checker actions there) |
| `marketing_manager`, `content_writer`, `designer`, `social_media_executive`, `pr_manager` | R [marketing view] | R [agg] | — | — | R | C (marketing lists, consent evidence mandatory) | — | — |
| `legal_reviewer` | R (on review items) | R (on review items) | A (terms) | R (on review items) | — | — | — | — |
| `compliance_officer` | R | R | R | R | R | R | R | R |
| `internal_auditor` | R [grant, watermark] | R | R | R | R | R | R | R |
| `group_admin` | — (grants only) | — | — | — | — | — | R [agg] | R [agg] |
| `dpo` | R | R | — | R (privacy review) | R U (DSR) | A (> 100 persons) | — | — |
| `it_admin` | — | — | — | — | — | — | — | — |
| `employee` | — | — | — | — | — | — | — | — |

**Table 2 — service, knowledge and platform objects**

| Role | Projects | Tickets | Grievances | Service metadata | KB | Automations | Exports | Settings / connectors |
|---|---|---|---|---|---|---|---|---|
| `ops_director` | R A | R | R | R | R A | A; pause | A | U (T, G maker) |
| `ops_manager` | C R U | R | R [agg] | R | C R U | C A [dept] | C | U (T) |
| `case_services_lead` | R | R U [case_procedure] | R [agg] | R (matter status) | C R U [scripts] | C [dept] | — | — |
| `onboarding_specialist` | C R U [own] | C R [hypercare] | — | R [acct, agg] | R | C [dept] | — | — |
| `customer_success_manager` | R U [acct] | R [acct] | R [acct, status only] | R [acct, agg] | R | C [dept] | — | — |
| `support_agent` | — | C R U [queue] | C (conversion) | R `tkt_case_context` [grant] | R; suggest | — | — | — |
| `support_lead` | — | C R U A | C R | R [agg] | C R U A [support] | C A [dept] | C [tickets] | U (support T) |
| `grievance_officer` | — | R | C R U A (decide) | — | R | C [grievance alerts] | C [grievances] | — |
| `finance_ops` | R (milestone billing) | R U [billing] | R [billing] | — | R | C [finance] | C [ageing] | — |
| `legal_reviewer` | R | R (on referral) | R | — | A (legal) | A (legal-impacting) | — | A (G) |
| `compliance_officer` | R | R | R | R [agg] | R | pause | R | A (G) |
| `internal_auditor` | R | R | R | R [agg] | R | R | X [grant, watermark] | R |
| `dpo` | R | R [data_protection] | R [privacy] | — | R | pause | A | A (connectors) |
| `it_admin` | — | R [it_request] | — | — | R | global pause | — | U (workspace/M365) |
| `group_admin` | — | — | — | R [agg, grant] | — | — | — | U (group G maker) |
| `employee` | — | C (internal IT/HR requests) | C (as complainant) | — | R [internal] | — | X (own data) | — |
| `ops_guest` | R U [named project] | C R [project] | — | — | R [project space] | — | — | — |

**Hard denials (Cerbos DENY, override every allow):** any `ops` principal → case content, sealed schemas, `hr`/`pay` records (`OPS_ACCESS_DENIED_CASE_CONTENT`); case-administration and neutral roles → `ops.crm_*`, `ops.cs_*`, `ops.fin_*` (D3-24); principal in a Finbyx/Udofin role → Equator matter status for those companies' clients (`OPS_ETHICAL_WALL`); author approving own quote discount, import, automation publish, export or merge (SoD); `support_agent` → bypassing an authentication factor (Appendix S); any role → creating a consent grant on behalf of a person.

**SoD additions (Appendix S §6.7):** `accounts_maker` ∉ approvers of their own refund hand-offs; `grievance_officer` ≠ head of the department complained about (per grievance); `internal_auditor` holds no other ops role; `bd_manager` cannot be checker of a contract they own.

---

## X.15 Data model (`ops` schema; business database; RLS `company_id`)

All tables: `id uuid DEFAULT uuidv7()`, `company_id uuid NOT NULL` (FK `grp.companies` via replicated reference table `ops.ws_companies`), `created_at/updated_at timestamptz`, `created_by`, `version int` (optimistic locking); money as `amount_minor bigint` + `currency char(3)`; soft delete only where stated; audit via `audit.append_event` (cross-DB through the outbox).

```sql
CREATE TABLE ops.crm_accounts (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, name text NOT NULL, legal_name text,
  kind text NOT NULL CHECK (kind IN ('lender','insurer','employer','listed_company','hei','msme','chambers','law_firm',
        'institution','government','partner','vendor','other')),
  cin text, gstin text CHECK (gstin IS NULL OR gstin ~ '^[0-9]{2}[A-Z0-9]{10}[0-9A-Z]{3}$'), lei text, domain text,
  state_code text, city text, size_band text, volume_band text, tier text, lifecycle text NOT NULL DEFAULT 'prospect',
  owner_person_id uuid, territory_id uuid, parent_account_id uuid REFERENCES ops.crm_accounts(id),
  core_tenant_ref uuid, core_org_ref uuid, custom jsonb NOT NULL DEFAULT '{}', tags text[] NOT NULL DEFAULT '{}',
  merged_into_id uuid, created_at timestamptz NOT NULL DEFAULT now(), updated_at timestamptz NOT NULL DEFAULT now(),
  version int NOT NULL DEFAULT 1,
  UNIQUE (company_id, gstin), UNIQUE (company_id, cin));
CREATE TABLE ops.crm_contacts (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, full_name text NOT NULL, job_title text, seniority text,
  email_norm text, email_verified boolean NOT NULL DEFAULT false, phone_e164 text, language text DEFAULT 'en',
  persona text, is_advocate boolean NOT NULL DEFAULT false, source text NOT NULL, owner_person_id uuid,
  age_confirmed_18 boolean, suppressed boolean NOT NULL DEFAULT false,                -- respondent hash / DND / hard bounce
  -- marketing_eligible is never stored: it is computed in VIEW ops.crm_marketing_view from crm_comm_prefs, suppressed, age (§X.4.7)
  custom jsonb NOT NULL DEFAULT '{}', merged_into_id uuid, created_at timestamptz NOT NULL DEFAULT now(),
  UNIQUE (company_id, email_norm));
CREATE TABLE ops.crm_comm_prefs (
  contact_id uuid NOT NULL REFERENCES ops.crm_contacts(id), purpose text NOT NULL, channel text NOT NULL,
  status text NOT NULL CHECK (status IN ('granted','withdrawn','never')), consent_record_ref uuid,
  notice_version text, captured_at timestamptz, withdrawn_at timestamptz, no_reask_until date,
  PRIMARY KEY (contact_id, purpose, channel));
CREATE TABLE ops.crm_opportunities (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, account_id uuid NOT NULL REFERENCES ops.crm_accounts(id),
  pipeline_id uuid NOT NULL, stage_id uuid NOT NULL, name text NOT NULL, amount_minor bigint, currency char(3) DEFAULT 'INR',
  probability int CHECK (probability BETWEEN 0 AND 100), close_date date, owner_person_id uuid NOT NULL,
  source text, partner_id uuid, first_touch jsonb, last_touch jsonb, mkt_touchpoint_ids uuid[] DEFAULT '{}',
  lost_reason text, status text NOT NULL DEFAULT 'open' CHECK (status IN ('open','won','lost')));
CREATE TABLE ops.crm_quotes (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, opportunity_id uuid NOT NULL, quote_no text NOT NULL,
  version int NOT NULL, billing_quote_ref uuid NOT NULL,           -- fee engine quote (P05) is authoritative
  max_discount_bp int NOT NULL DEFAULT 0, nonstandard_terms boolean NOT NULL DEFAULT false,
  approval_state text NOT NULL DEFAULT 'draft' CHECK (approval_state IN ('draft','pending','approved','rejected','sent','accepted','expired')),
  maker_id uuid NOT NULL, checker_id uuid, CHECK (checker_id IS NULL OR checker_id <> maker_id), UNIQUE (company_id, quote_no, version));
CREATE TABLE ops.tickets (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, ticket_no text NOT NULL, channel text NOT NULL,
  received_at timestamptz NOT NULL, requester_contact_id uuid, requester_core_user_ref uuid, tenant_ref uuid,
  category text NOT NULL, subcategory text, priority text NOT NULL CHECK (priority IN ('P1','P2','P3','P4')),
  status text NOT NULL, queue_id uuid, assignee_person_id uuid, case_ref text, case_link_verified boolean NOT NULL DEFAULT false,
  case_linked boolean GENERATED ALWAYS AS (case_ref IS NOT NULL) STORED, confidentiality_tier text NOT NULL DEFAULT 'standard',
  sla_policy_id uuid, first_response_due_at timestamptz, resolution_due_at timestamptz, first_responded_at timestamptz,
  solved_at timestamptz, resolution_code text, csat smallint, grievance_ref uuid, reopen_count int NOT NULL DEFAULT 0,
  UNIQUE (company_id, ticket_no), CHECK (NOT case_linked OR confidentiality_tier = 'high'));
CREATE TABLE ops.ob_projects (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, account_id uuid NOT NULL, opportunity_id uuid,
  template_code text NOT NULL, status text NOT NULL, rag text NOT NULL DEFAULT 'green', owner_person_id uuid NOT NULL,
  csm_person_id uuid, target_golive date, actual_golive date, hypercare_end date, security_review_required boolean NOT NULL);
CREATE TABLE ops.cs_health_scores (
  account_id uuid NOT NULL, company_id uuid NOT NULL, as_of date NOT NULL, score int NOT NULL CHECK (score BETWEEN 0 AND 100),
  band text NOT NULL, components jsonb NOT NULL, model_version int NOT NULL, PRIMARY KEY (account_id, as_of));
CREATE TABLE ops.wf_automations (
  id uuid PRIMARY KEY DEFAULT uuidv7(), company_id uuid NOT NULL, owner_department_id uuid NOT NULL, code text NOT NULL,
  name text NOT NULL, owning_appendix text NOT NULL CHECK (owning_appendix IN ('X','Y')), status text NOT NULL
    CHECK (status IN ('draft','in_review','published','paused','retired')), current_version_id uuid, UNIQUE (company_id, code));
CREATE TABLE ops.wf_automation_versions (
  id uuid PRIMARY KEY DEFAULT uuidv7(), automation_id uuid NOT NULL REFERENCES ops.wf_automations(id), version int NOT NULL,
  definition jsonb NOT NULL, touches_approval_list boolean NOT NULL, approval_steps_present boolean NOT NULL,
  simulation_report jsonb, author_id uuid NOT NULL, publisher_id uuid, published_at timestamptz,
  CHECK (publisher_id IS NULL OR publisher_id <> author_id),
  CHECK (NOT touches_approval_list OR approval_steps_present), UNIQUE (automation_id, version));
-- System-of-record declarations live in cfg.system_of_record (Appendix AC §AC.12.1); a CHECK there forbids any external system for data_category 'consent'.
```

Other tables (key columns in P16 §7.2): `crm_leads`, `crm_pipelines`, `crm_stages`, `crm_stage_history`, `crm_products` (view), `crm_subscription_view`, `crm_activities`, `crm_segments`, `crm_segment_members`, `crm_custom_fields`, `crm_tags`, `crm_duplicate_candidates`, `crm_merge_log`, `crm_import_jobs`, `crm_import_rows`, `crm_routing_rules`, `crm_scoring_models`, `crm_partners`, `crm_referrals`, `crm_sources`, `crm_migration_runs`, `crm_migration_mappings`, `crm_migration_map`, `ob_milestones`, `ob_checklist_items`, `ob_migration_tasks`, `ob_training_sessions`, `ob_signoffs`, `cs_playbooks`, `cs_playbook_runs`, `cs_success_plans`, `cs_qbrs`, `cs_surveys`, `cs_survey_responses`, `tkt_messages`, `tkt_internal_notes`, `tkt_macros`, `tkt_sla_policies`, `tkt_queues`, `tkt_service_catalogue`, `tkt_incident_links`, `tkt_case_context` (cache, 24 h TTL), `kb_spaces`, `kb_articles`, `kb_versions`, `kb_feedback`, `wf_runs`, `wf_exceptions`, `ws_departments`, `ws_workspaces`, `ws_tasks`, `ws_saved_views`, `ws_dashboard_layouts`, `ws_staff_directory`, `ws_template_packs`, `ws_companies`, `rpt_kpi_definitions`, `svc_account_service_stats`, `svc_matter_status`, `fin_receivables_view`, `cs_usage_signals`, `con_providers` (connector config, rehearsal record, residency record), `con_sync_log`.

---

## X.16 APIs (`/v1/ops`, OpenAPI 3.1; Idempotency-Key on every creating POST; cursor pagination)

| Endpoint | Purpose | Roles |
|---|---|---|
| `GET/POST/PATCH /v1/ops/crm/{accounts|contacts|leads|opportunities}` | CRUD (field-level permissions) | per §X.14 |
| `POST /v1/ops/crm/leads/{id}/convert` | Lead → account/contact/opportunity | sales |
| `POST /v1/ops/crm/opportunities/{id}/stage` | Stage change with gate check | owner |
| `POST /v1/ops/crm/quotes` · `POST …/{id}/submit` · `POST …/{id}/approve` · `POST …/{id}/send` | Quote lifecycle (fee engine call inside) | sales; checker |
| `GET/POST /v1/ops/crm/activities` | Activities | per §X.14 |
| `GET /v1/ops/crm/contacts/{id}/preferences` · `POST …/withdraw` | Preferences; withdrawal (writes via consent API) | support, sales, DPO |
| `POST /v1/ops/crm/segments` · `POST …/{id}/preview` · `POST …/{id}/build` | Segments | marketing, sales |
| `GET /v1/ops/crm/duplicates` · `POST /v1/ops/crm/merge` · `POST /v1/ops/crm/merge/{id}/undo` | Dedupe and merge | `crm.merge` holders |
| `POST /v1/ops/crm/imports` · `…/{id}/mapping` · `…/{id}/dry-run` · `…/{id}/approve` · `…/{id}/commit` · `…/{id}/rollback` | Imports | ops_manager; checker |
| `POST /v1/ops/crm/scoring-models` · `…/{id}/backtest` · `…/{id}/approve` | Scoring | bd_manager; head of sales |
| `GET /v1/ops/crm/attribution/{opportunityId}` | Attribution hook (Appendix Y) | marketing, sales |
| `POST /v1/ops/connectors/{provider}/migrations` · `…/{run}/dry-run` · `…/{run}/approve` · `…/{run}/cutover` · `…/{run}/rollback` | Migration both ways | ops_manager; ops_director; DPO |
| `POST /webhooks/brevo` | Single Brevo ingress for both ports (bearer + IP + re-fetch): consent events → consent API; engagement events → Appendix Y `mkt.touchpoints` through the outbox (`ops.connector.engagement_received`) | machine |
| `GET/POST /v1/ops/projects` · `…/{id}/milestones` · `…/{id}/signoff` | Onboarding | onboarding, CSM |
| `GET /v1/ops/accounts/{id}/health` · `POST /v1/ops/qbrs` · `POST /v1/ops/qbrs/{id}/generate` | CS | CSM |
| `POST /v1/ops/tickets` (public intake: `/v1/help/tickets`, captcha + OTP) · `PATCH …/{id}` · `POST …/{id}/reply` · `…/note` · `…/escalate` · `…/merge` · `…/convert-to-grievance` | Support | support |
| `GET /v1/help/tickets/{no}` (requester, signed link or session) | Customer status view | requester |
| `GET/POST /v1/ops/grievances` (proxy to `grm` variant `EQ_SERVICE`) · `…/{id}/acknowledge` · `…/final-reply` · `…/appeal` | Grievance | grievance_officer; Company Secretary |
| `GET/POST /v1/ops/kb/articles` · `…/{id}/submit-review` · `…/{id}/publish` (→ CMS) | KB | KB authors; legal |
| `GET/POST /v1/ops/automations` · `…/{id}/versions` · `…/{v}/simulate` · `…/{v}/publish` · `…/{id}/pause` · `…/{id}/rollback` | Automation engine | per §X.12.2 |
| `GET/POST /v1/ops/tasks` | Task queues | all ops roles |
| `GET /v1/ops/service/accounts/{id}/stats` · `GET /v1/ops/service/matters` | Service metadata | case_services_lead etc. |
| `GET /v1/ops/finance/receivables` · `POST /v1/ops/finance/handoffs` | Finance views; hand-off to P05 | finance_ops |
| `POST /v1/ops/exports` (scope `OPS_DEPARTMENT`, Appendix AC §AC.13.3) | Export package | per §X.14 |
| `GET/PATCH /v1/ops/settings/{key}` | Settings (tier-aware) | per §X.13 |

---

## X.17 Events (`equator.ops.<entity>.<verb>.v1`; payload IDs and codes only, never PII or case content)

`lead.created` · `lead.routed` · `lead.sla_breached` · `lead.converted` · `contact.merged` · `contact.preferences_changed` · `opportunity.stage_changed` · `opportunity.won` · `opportunity.lost` · `opportunity.closed` · `quote.submitted` · `quote.approved` · `quote.accepted` · `import.committed` · `import.rolled_back` · `segment.built` · `project.created` · `project.status_changed` · `project.golive_signed` · `project.handed_over` · `health.band_changed` · `qbr.completed` · `renewal.opened` · `ticket.created` · `ticket.first_responded` · `ticket.sla_breached` · `ticket.escalated` · `ticket.solved` · `ticket.converted_to_grievance` · `kb.article_published` · `automation.published` · `automation.paused` · `automation.rolled_back` · `automation.run_failed` · `connector.sync_completed` · `connector.optout_applied` · `connector.engagement_received` (Brevo engagement events forwarded to Appendix Y; IDs and event types only) · `migration.cutover_completed` · `export.ready` · `ethical_wall.denied`. Consumed: `equator.growth.lead.created.v1`, `equator.consent.consent.{given,withdrawn}.v1` (P01 names), `equator.billing.subscription.*`, `equator.billing.invoice.overdue.v1`, `equator.enterprise.tenant.provisioned.v1`, `equator.grm.ticket.*` (variant `EQ_SERVICE`), `equator.notices.respondent.served.v1` (suppression hash only, via `growth`), `equator.hr.employee.{activated,role_changed,transferred,exit_effective}.v1` (staff directory projection only; Appendix Z).

---

## X.18 Error codes (register in Appendix F §F.10.4, v3)

| Code | HTTP | Meaning |
|---|---|---|
| `OPS_CASE_FIELD_FORBIDDEN` | 422 | A projection, import or field tried to carry non-allow-listed case data |
| `OPS_ACCESS_DENIED_CASE_CONTENT` | 403 | Ops principal requested case content or sealed/HR data |
| `OPS_ETHICAL_WALL` | 403 | Group ethical-wall denial |
| `OPS_COMMERCIAL_DATA_FORBIDDEN` | 403 | Case or neutral role requested commercial data (D3-24) |
| `OPS_SEGMENT_SOURCE_FORBIDDEN` | 422 | Segment predicate uses a forbidden source |
| `OPS_FIELD_PROHIBITED` | 422 | Custom field on a prohibited attribute |
| `OPS_SUPPRESSED_CONTACT` | 409 | Contact suppressed (respondent hash, DND, opt-out) |
| `OPS_CONSENT_EVIDENCE_REQUIRED` | 422 | Marketing eligibility or import without consent artefact |
| `OPS_CONSENT_PROPAGATION_LATE` | 500 (alert) | Withdrawal not propagated in time |
| `OPS_DUPLICATE_RECORD` | 409 | Exact-duplicate rule matched |
| `OPS_CROSS_COMPANY_MERGE` | 422 | Merge across companies |
| `OPS_UNMERGE_WINDOW_EXPIRED` | 409 | Un-merge after window |
| `OPS_IMPORT_SOURCE_PROHIBITED` | 422 | Bar roll / institute directory / scraped source |
| `OPS_IMPORT_RECONCILIATION_MISMATCH` | 409 | Commit counts differ from dry-run |
| `OPS_PRODUCT_NOT_SELLABLE` | 422 | Stream disabled, killed or neutrality-restricted |
| `OPS_DISCOUNT_APPROVAL_REQUIRED` | 409 | Discount above band |
| `OPS_STAGE_GATE_UNMET` | 422 | Opportunity stage gate unmet |
| `OPS_PAID_PLACEMENT_FORBIDDEN` | 422 | Placement quoted to an advocate/CA/CS/CMA or while flag OFF (NN-34) |
| `OPS_GOLIVE_SIGNOFF_INCOMPLETE` | 409 | Go-live without required signatures/probes |
| `OPS_QBR_CONTENT_BLOCKED` | 422 | QBR or leadership pack contains banned content (outcome rates as performance, neutral names, matter details) |
| `OPS_TICKET_CATEGORY_LOCKED` | 422 | Top-level category change not permitted |
| `OPS_CASE_LINK_UNVERIFIED` | 403 | Case link not chosen by the requester from their own cases |
| `OPS_AI_DRAFT_REQUIRES_REVIEW` | 409 | Attempt to send an unreviewed AI draft |
| `OPS_GRIEVANCE_CLOCK_LOCKED` | 422 | Attempt to pause/extend a statutory clock |
| `OPS_COMPLAINT_NOT_TRACKED` | 409 | Activity records a complaint without a ticket link |
| `OPS_AUTOMATION_APPROVAL_REQUIRED` | 422 | Automation reaches an approval-list action without an approval step |
| `OPS_AUTOMATION_LOOP` | 409 | Loop or chain depth exceeded |
| `OPS_AUTOMATION_RATE_LIMITED` | 429 | Automation rate limit |
| `OPS_CONNECTOR_REHEARSAL_MISSING` | 409 | Connector activation without a passed rehearsal in `cfg.migration_rehearsals` (with AC's `CFG_SOR_UNDECLARED` / `CFG_MAPPING_MISSING`) |
| `OPS_CONNECTOR_DISABLED` | 409 | Connector flag OFF |
| `OPS_WEBHOOK_UNVERIFIED` | 401 | Inbound webhook failed verification |
| `OPS_SOR_CHANGE_FORBIDDEN` | 422 | Attempt to make an external tool system of record for consent |
| `OPS_EXPORT_APPROVAL_REQUIRED` | 409 | Export above personal-data threshold without checker |
| `OPS_GRANT_REQUIRED` | 403 | Cross-company action without Appendix AD grant |

---

## X.19 KPIs and reports per department

| Department | KPIs (definition source in `ops.rpt_kpi_definitions`, shown in-app) | Standard reports (DOCX/XLSX/PDF; scheduled via OA-18) |
|---|---|---|
| Leadership | ARR; NRR; GRR; logo churn; pipeline coverage (pipeline ÷ target); CSAT; NPS; grievance breaches; automation exception rate | Monthly leadership pack; quarterly board pack (aggregates; revenue by stream with neutrality-exposure tile) |
| Case Services | scrutiny ≤ 2 working days %; notices delivered %; service-request first response; unowned-clock flags (target 0) | Weekly service report per enterprise account (metadata) |
| Onboarding | time-to-first-value; time-to-go-live vs plan; migration error rate; checklist completion; hypercare P1/P2 count | Project status report; go-live sign-off pack |
| Customer Success | health distribution; GRR/NRR by segment; QBR coverage; renewal forecast accuracy; save rate | QBR pack; renewal forecast; at-risk register |
| Support | first response within SLA %; resolution within SLA %; backlog age; reopen rate; CSAT; deflection rate; contacts per account | Weekly SLA report; monthly category trends; enterprise SLA report (contracted tenants) |
| Grievance | acknowledged ≤ 48 h %; resolved within clock %; median days; appeals; upheld %; breaches | Quarterly Transparency Report summary (k ≥ 10, X-28); grievance register (XLSX) |
| Sales / BD | speed-to-lead; MQL→SQL; win rate; cycle time; average contract value; discount leakage | Pipeline and forecast; win/loss analysis |
| Partnerships | active partners; partner-sourced pipeline and ARR | Partner statements (reward-eligible partners only) |
| Finance ops views | DSO; overdue %; dunning recovery; billing-query resolution time | Ageing report (read-only from `billing`) |
| Training / marketplace ops | sessions delivered; attendance; listing approval time; moderation SLA; complaint rate | Marketplace moderation log; monthly self-audit inputs (NN-34 when ON) |

Staff-level reports show work-item metrics only and are visible to the staff member (NN-35); no report ranks staff by personal attributes.

---

## X.20 Audit, privacy, retention and assurance

- **Audit:** every create/update/delete of CRM, ticket, grievance, project, automation, setting, connector and export writes the hash-chained audit event (NN-22) via the outbox with actor, company, before/after digests; reads of `case_linked` tickets, `svc_matter_status`, finance views and exports write `audit.access_log`.
- **Privacy notice:** the EPN-2026.1 notice (Appendix U §U.5) gains EOP purposes: B2B relationship management, support, grievance handling, service quality surveys, product training; the staff notice gains EOP work-item metrics (NN-35).
- **DSRs:** EOP data is in scope of the DSR portal (Appendix Q §2.4); the `DSR_PORTABILITY` export scope (Appendix AC §AC.13) includes CRM, ticket and grievance records about the person; erasure tombstones CRM records and keeps grievance records under legal retention.
- **Retention (`core.retention_classes` additions; tier G):** `crm_lead_inactive` 24 months of inactivity then delete (P13); `crm_customer` contract term + 8 years (commercial records; **[VERIFY — open: CS/tax adviser to confirm the books-of-account and GST record periods applicable to CRM attachments]**); `support_ticket` 3 years after closure; `support_call` 180 days; `grievance` 8 years after closure (aligned with the case default, App. Q §2.8); `automation_run` 13 months; `meeting_transcript_ops` 30 days unless attached.
- **Annual attestations:** ethical walls, acceptable use, confidentiality (staff in group roles) collected in EOP; evidence to `eng` control `PC-OPS-01` (new) via collector `ops_attestation_status`.
- **Assurance collectors (Q §7.3 additions):** `ops_consent_parity` (daily: consent sets Equator vs each connector — must be equal), `ops_projection_schema_check` (per release), `ops_automation_approval_lint` (per publish), `ops_export_register` (monthly).
- **Processor roles:** for tenants' customers' data Equator handles in support (e.g., a lender's GRO raising a ticket), Equator is processor under the tenant DPA; for its own B2B prospects and customers' contact data, Equator is fiduciary (Appendix Q §1.1 role matrix **[VERIFY — open: counsel sign-off of role matrix, as P09 FR-P09-23]**).

---

## X.21 Acceptance tests (Gherkin; `tests/acceptance/appendix-X.feature`; extended in P16 §12)

```gherkin
Feature: Appendix X operations platform guardrails

Scenario: NN-16_ops_projection_rejects_case_content
  Given the core→ops projection payload contains field "party_name"
  When the projection consumer validates the event
  Then it is rejected with OPS_CASE_FIELD_FORBIDDEN and no ops row is written

Scenario: NN-16_respondent_never_enters_brevo
  Given a person served as respondent with no separate marketing consent
  And the same email is in an approved CRM import
  When the Brevo contact sync runs
  Then the contact is not sent to Brevo and import shows "suppressed"

Scenario: D3-24_case_manager_cannot_see_health
  Given a user with role case_manager
  When they call GET /v1/ops/accounts/{id}/health
  Then the API returns 403 OPS_COMMERCIAL_DATA_FORBIDDEN

Scenario: NN-36_discount_above_band_needs_checker
  Given a sales_executive quote with a 12% line discount
  When they submit the quote
  Then the state is "pending" and the bd_manager queue holds an approval
  And the sales_executive cannot approve it

Scenario: EOP-L07_refund_automation_blocked
  Given an automation whose action creates a refund hand-off with no approval step
  When the author publishes it
  Then the API returns 422 OPS_AUTOMATION_APPROVAL_REQUIRED

Scenario: NN-40_brevo_optout_propagates
  Given a Brevo "unsubscribed" webhook with a valid bearer token from an allow-listed IP
  When the connector re-fetches the contact and confirms the unsubscribe
  Then a consent withdrawal is recorded in core.consent_records within 15 minutes
  And the contact leaves every marketing segment
```

---

## X.22 Open items and verification flags

| # | Item | Owner | Gate |
|---|---|---|---|
| X-OI-01 | Microsoft 365 SKU (management said "Business Starter"; RD: likely Business Basic) — confirm via admin centre or `subscribedSkus` (D3-04) | Company Secretary | P16 M365 hooks go-live |
| X-OI-02 | Basic SKU: Teams recording/transcription licensing; attendance-report API; Graph chat permission; Exchange application-RBAC scoping (RD Open point 2) | `it_admin` | OA-15; shared-mailbox flag |
| X-OI-03 | Brevo: INR prices; whether CRM/campaign endpoints fall under the 100/h catch-all; webhook retry policy; DPA and sub-processor list; DLT support (RD Open point 5) | CS / `ops_director` | `mkt.brevo.enabled`; `tenant.ops.connectors.brevo_crm_sync.enabled` |
| X-OI-04 | E-Commerce Amendment Rules 2026 commencement and text (Gazette CG-DL-E-10092026-276125) | `legal_reviewer` | `rulepack.IN.grievance.ecommerce@2026.2` (`effective_from` = commencement) |
| X-OI-05 | IT Rules 2021 amendment of 10 Feb 2026 (G.S.R. 120(E)) grievance timelines | `legal_reviewer` | `rulepack.IN.grievance.it_intermediary@2026.1` |
| X-OI-06 | Whether the E-Commerce Rules apply to Equator's own services and marketplace (counsel characterisation, App. O §6.1) | Counsel | Rule-pack applicability flags |
| X-OI-07 | Related-party thresholds and approvals for group contracts and shared services (s.188, r.15(3)) | Company Secretary | `tenant.ops.crm.contract_board_threshold_minor` |
| X-OI-08 | Fiduciary/processor role matrix for EOP data | Counsel / DPO | Production go-live |
| X-OI-09 | Retention periods for commercial CRM records and attachments | CS / tax adviser | Retention class activation |
| X-OI-10 | Department structure from management (D3-06 default shipped) | Management | None (configurable) |
| X-OI-11 | Group cross-sell consent design and GDSA (AU-26) | Group / counsel | `group.ops.cross_sell.enabled` |
| X-OI-12 | WhatsApp customer-service window and template categories for support replies | BSP / `support_lead` | WhatsApp channel go-live |

---

## X.23 Phase addenda

### For P09

**FR-P09-V3-X01 — GRM variant `EQ_SERVICE`.** Add the `EQ_SERVICE` variant to `grm.sla_policies` for the Equator institution tenant with the rule packs of §X.8.3, a `level2_review` state replacing `io_review`, and the final-reply template set of §X.8.4. *Acceptance:* a converted EOP ticket creates a GRM grievance whose clock starts at the ticket's original received time; the clock cannot be paused (`OPS_GRIEVANCE_CLOCK_LOCKED`).

**FR-P09-V3-X02 — Enterprise ticket webhooks.** Expose `ops.ticket.*` and `ops.project.*` metadata events through the P09 webhook service to the customer's own subscription. *Acceptance:* the payload contains IDs, status and timestamps only; a sealed or case-content field fails schema validation.

**FR-P09-V3-X03 — Console "Help" panel.** Every enterprise console page gets the `/app/help` panel creating EOP tickets with tenant and role attached and an optional link to one of the user's own cases. *Acceptance:* a case not visible to the user cannot be linked (`OPS_CASE_LINK_UNVERIFIED`).

**FR-P09-V3-X04 — Service-stats read model.** Publish the `svc_account_service_stats` aggregate read model per enterprise tenant (§X.2.3). *Acceptance:* the read model holds only the allow-listed fields; the CI schema check fails on any addition without an ADR.

### For P11

**FR-P11-V3-X01 — Agent `support_triage`.** Register an agent that classifies tickets (top-level category, sub-category, priority, language), detects complaint, safety and POSH indicators, suggests KB articles and drafts replies from approved macros and KB content only. *Acceptance:* `safety_urgent` and `posh_related` are routed with no AI reply; every draft carries `requires_human_review = true`; no case content is sent to the model beyond the requester's own ticket text; bilingual parity eval (en/hi) ≥ the P11 threshold.

**FR-P11-V3-X02 — Agent `meeting_followup`.** Drafts minutes and action items from an ops meeting transcript (internal or B2B only). *Acceptance:* the agent refuses a transcript tagged as a hearing or case session; output is a draft for the organiser.

**FR-P11-V3-X03 — `analytics_narrator` for QBRs and leadership packs.** Extend its allowed inputs to EOP aggregates (§X.19). *Acceptance:* it cannot read `svc_matter_status` rows or outcome metrics; output contains no settlement or award rates.

**FR-P11-V3-X04 — Scoring-weight suggestion.** A tool that proposes lead-scoring weights from historical conversions as a draft for the human owner. *Acceptance:* forbidden inputs (§X.4.12) are absent from the feature set; no individual lead is scored by AI.

### For P13

**FR-P13-V3-X01 — Capture inbox and promotion (X-51).** `growth.leads` remains the capture store; `LeadIngestWorkflow` promotes leads to `ops.crm_leads` within 60 s with dedupe and suppression. *Acceptance:* a form submission appears in EOP in ≤ 60 s; a respondent-hash match is created as suppressed.

**FR-P13-V3-X02 — Supersede SCR-P13-18.** Remove the growth mini-CRM screen after a one-time migration of `growth.accounts`/`growth.opportunities` into `ops` with a row map. *Acceptance:* migrated counts reconcile exactly; the old screen redirects to EOP.

**FR-P13-V3-X03 — Public help centre.** `/help` (server-rendered, en + hi) publishes `public_help` KB articles through the CMS legal workflow and hosts the contact form with KB deflection. *Acceptance:* an article with a fee figure renders the live fee block; an article with an unapproved claim cannot publish.

**FR-P13-V3-X04 — Preference centre parity.** The signed-link preference centre writes through the consent API and updates `ops.crm_comm_prefs` and connected tools within 15 minutes. *Acceptance:* `ops_consent_parity` collector shows equality after a withdrawal test.

### For P14

**FR-P14-V3-X01 — Schema hygiene (X-50, with AE X-65).** After the AE X-65 relocation migration, a CI check fails if any table outside the EOP prefixes (and `ops.tickets`) exists in `ops`, or if any EOP table exists in the core database. *Acceptance:* the check runs on every migration PR and on the production schema nightly.

**FR-P14-V3-X02 — EOP in go-live gates.** Add to the go-live checklist: EOP RBAC matrix tests (§X.14) green; Cerbos DENY tests for D3-24 and ethical walls; consent-parity collector green for every enabled connector; automation approval lint green; grievance rule packs approved by the legal reviewer. *Acceptance:* go-live is blocked when any item is red.

**FR-P14-V3-X03 — Access reviews.** Include EOP roles, guest memberships, connector credentials and the `eq-ops-collab` Graph app in quarterly access reviews (Q §7.3). *Acceptance:* the review campaign lists EOP principals; un-actioned items auto-revoke after 10 working days.

**FR-P14-V3-X04 — EOP VAPT scope.** Add `ops.equatorresolution.in`, `/v1/ops/*`, `/v1/help/*` and `/webhooks/brevo` to the VAPT scope, including tests for case-content leakage and cross-company access. *Acceptance:* no high or critical finding open at go-live.
