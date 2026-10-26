# Phase P18 — Delivery Console and Operations Hub Interface

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (Keycloak realms `ld` and `ld-staff`, passkeys, step-up MFA), P02 (tenancy, legal entities, departments, user types, maker-checker engine, grant primitive), P03 (settings registry, rule engine), P04 (Legal Vault/DMS, sharing, folder intake), P09 runtime (Vidhi briefs and drafting, agent sponsorship), P13 (departments, positions and Company Legal Department OS roles), P16 (engagements `eng_`, retainers `rtn_`, SLAs `sla_`, professional registry `pro_`, assignment engine), P17 (billing presentation, entitlements mirror, `BILLING_PORT`), P19 (`int` gateway, `WORKSPACE_PORT`, OH contracts, webhook signing), P20 (`xpt.export_map`, `LD-EXPORT-1.0`). P15 supplies the consumer-case model used by the queue in §4I. **External:** Infrabyx Operations Hub (OH1 group identity and grants, OH1.6 conflict service, OH3 CRM, OH4 onboarding factory, OH5 customer success, OH6 support desk, OH8 billing, OH9 directory, OH10 staff HRMS, OH11 internal controls, OH12 workplace); Microsoft Graph (now); Google Workspace APIs (later, flag OFF).
> **Sequencing:** Start when P02 and P04 have exited and the P16 engagement/retainer schema is frozen (freeze point F-P16-ENG). Sprints 1–3: staff realm, portfolio, client section, delivery grants, act-in-tenant sessions, credential vault. Sprints 4–5: master-data change requests, deliverables, messages/meetings/drives, SLA tracker, practitioner workspace. Sprints 6–7: OH interfaces (contract-tested against the OH sandbox), timesheets and metrics, consumer case queue (built in Wave 2 behind `chp.brand.enabled = false` — the P15 key; switched on with P15 in Wave 3). **P18 must exit before any retainer or LDaaS engagement goes live** (P16 gate).
> **Binding appendices:** A (workflows and state machines — governs where a §5 pointer says so), X (Operations Hub and LawDocsComply Addenda), D (roles, personas and access matrix), R (settings catalogue), K (`LD-EXPORT-1.0`), M (marketplace professional rules), Y (Ecosystem Spec v1.2 change request), W (verification log and open items), Q (competitive research and improvement backlog: IMP-003, IMP-010, IMP-012, IMP-087).
> **Requirements covered:** R-014, R-026, R-027, R-028, R-030, R-037, R-039, R-047, R-048, R-050, R-051, R-052, R-053, R-055, R-058, R-062, R-064, R-065, R-066, R-067, R-068, R-080, R-083 (queue only).
> **Decisions applied:** D-02, D-03, D-05, D-06, D-10, D-11, D-17 · **Challenges applied:** CH-07, CH-08, CH-09, CH-10, CH-16, CH-24, CH-26, CH-29, CH-31, CH-32 · **Non-negotiables tested:** NN-01, NN-02, NN-11, NN-13, NN-16, NN-17, NN-18, NN-19, NN-21, NN-23, NN-24, NN-25, NN-28, NN-29, NN-32, NN-33, NN-39, NN-41, NN-43, NN-45, NN-46
> **Estimated effort:** 7 two-week sprints, squad of 8 (backend 3, frontend 2, integration engineer 1, security engineer 1, QA 1)

---

## 1. Objective and business outcome

LawDocs sells legal services as well as software: one-time drafting and filings, retainers (Startup Legal Officer, SME Legal Desk, NBFC Legal & Compliance Retainer — Appendix L §L.7), Managed Legal Department (LDaaS) and marketplace engagements (P16). People deliver that work — relationship managers (RMs), in-house professionals, consumer case managers and third-party professionals. **The Delivery Console** (`apps/delivery`, work.lawdocs.in) is their workplace. It gives each staff member one portfolio, a **dedicated section per client company**, a governed way to act as **maker** inside the client's own tenant while the client's employee remains the **checker** (R-064), a client-owned **credential vault** (NN-16), a transparent **master-data change workflow** (CH-26, R-066), and clean interfaces to the Infrabyx Operations Hub (OH) for CRM, onboarding, tickets, customer success, billing, staff identity and timesheets (D-02) — without copying any tenant document, matter, credential or personal content into OH (NN-19).

The console is **not** the Operations Hub (no CRM, marketing, HRMS, payroll or billing engine here) and **not** the Super Admin console (`apps/console`). It is the client-service surface that sits between them (R-048).

| Outcome | Exit-gate measure |
|---|---|
| One portfolio | An RM sees every assigned client with next breach, SLA risk, open tasks, unread messages and grant expiry on one home screen; any client section opens in ≤ 2 clicks from home |
| Governed maker access | Every LawDocs maker in a client tenant holds a client-approved, scoped, time-bound delivery grant; no delivery user can ever be a checker, approver, signatory, director or auditor in a client tenant (`NN-17_delivery_never_checker`) |
| Fast client approval | A client admin approves a proposed grant in ≤ 2 taps from the notification on web or mobile; median proposal-to-active time ≤ 4 working hours (measured) |
| Credential vault | OFF by default; when ON, delegation is offered first, secrets are revealed just-in-time with reason, every view/copy/change is logged and visible to the client; OTPs, DSC PINs and recovery codes cannot be stored |
| Master-data integrity | No crucial client detail (legal name, PAN, CIN/LLPIN, GSTIN, registered office, owner contacts, authorised signatories) changes without client approval, a second Super Admin checker and notification to all owners (`NN-18_masterdata_maker_checker`) |
| Commercial clarity | The client section's Billing tab shows exactly what the client sees on its own Billing page (same component, same OH8 data); RMs cannot change prices, credits or entitlements |
| Clean OH interface | Tickets, CRM activities, onboarding milestones, CSAT/NPS, health signals and timesheets flow through Ecosystem-Spec contracts; a contract test proves no document text, matter data, credential, message body or end-customer personal data leaves LawDocs (`NN-19_no_content_to_oh`) |
| Proportionate productivity | Work is measured by outcomes (tasks, SLAs, deliverables accepted first time, CSAT); sessions are recorded only for attendance; no covert monitoring (NN-33, CH-24, CH-32) |
| Ethical wall | Consumer case managers work in a separate brand queue; no person holds both a Consumer Help role and a delivery grant in a lender/insurer tenant (`NN-23_people_wall`) |

---

## 2. Scope (in / out)

**In scope**

1. `apps/delivery` (Next.js 16) on realm `ld-staff` for LawDocs staff and realm `ld` for third-party professionals (practitioner workspace), phishing-resistant MFA (passkeys/FIDO2) for every delivery user.
2. Staff projection from the group identity provider (OH1/OH10 → Entra ID → SCIM 2.0 → Keycloak `ld-staff`).
3. Portfolio, assignments (RM, backup RM, professionals, reviewer), reassignment and leaver handling.
4. Per-client section: Overview, Contacts, Plan & entitlements, Engagements & retainers, Tasks, Deliverables, Messages, Meetings, Shared drive, Billing & invoices, SLA & reports, Access log, Notes.
5. Delivery grants (propose / approve / standing authorisation / renew / suspend / revoke / expire), multiple delegated makers, departmental role assignment, client checker binding, act-in-tenant sessions.
6. Credential vault (`cvl`) UI and service (client side in `apps/web`, delivery side in `apps/delivery`).
7. Master-data change requests with client approval and Super Admin maker-checker (`apps/console` screens built here).
8. Deliverables register and release gate; messages (`msg`), meetings (Teams now, Google Meet later), shared drive links (SharePoint/OneDrive now, Google Drive later) via `WORKSPACE_PORT`.
9. SLA tracker and monthly service reports.
10. Consumer case manager queue for the `[Consumer Help Brand]` (UI, assignment, walls; case logic is P15).
11. Practitioner workspace for third-party professionals and firms (PRO_* roles).
12. Time entries, utilisation aggregates to OH11, monthly outcome metrics to OH10/OH11, anti-fraud controls in delivery.
13. OH interfaces: CRM (OH3), onboarding (OH4), customer success, CSAT/NPS (OH5), tickets (OH6), billing (OH8), directory (OH9), staff identity (OH10/OH12), cross-company roles (OH1, Ecosystem Spec §4.6), conflict service (OH1.6).
14. Client-side surfaces in `apps/web` and `apps/mobile`: Settings › LawDocs team, approvals, vault, access log, master-data change tracker.

**Out of scope (owner phase)**

| Item | Owner |
|---|---|
| CRM, marketing, social calendar, PR, onboarding factory engine, CS playbooks, support desk engine, staff HRMS, payroll, leave, appraisal, internal-controls engine, billing engine and GST invoices | Operations Hub (Appendix X lists what OH must add) |
| Platform provisioning, global settings, feature flags, break-glass framework | P00, P02, P03, P23 (`apps/console`) |
| Engagement/retainer catalogue, offers, SLAs definition, professional verification and assignment engine | P16 |
| Plans, entitlements, presentation catalogue, Razorpay checkout UI | P17 |
| Consumer case workflows, forum rules, authority letters | P15 |
| Client-tenant legal features (CLM, litigation, IP, governance) — the delegated maker uses the normal tenant UI | P04–P13 |
| Mobile app shell and store release | P22 |

---

## 3. Personas and permissions touched

Full matrix in Appendix D. "Grant" means a client-approved delivery grant (NN-17).

| Role code | Where | Can | Cannot |
|---|---|---|---|
| `OPS_DELIVERY_LEAD` | apps/delivery | Assign portfolios and reviewers; propose and renew grants; activate makers under a client's standing authorisation; run grant and vault access reviews; approve trial extensions within DoA (P17); view all clients of the practice; portfolio reports | Approve own proposals; act as checker in any tenant; reveal a credential without a credential grant; approve own discounts |
| `OPS_RM` | apps/delivery + tenant (grant) | Own portfolio; client sections; propose grants and delegated makers; act as maker within grant; request credential access; raise master-data change requests; messages, meetings, drive links; draft quotes; log time; raise tickets for clients | Check, approve or sign in a tenant; change billing, prices or entitlements; see clients outside portfolio; edit master data |
| `OPS_PROFESSIONAL` | apps/delivery + tenant (grant) | Work assigned engagements as maker; upload deliverables; log time; request credential access | Release own deliverable; act outside grant scope |
| `OPS_QA_REVIEWER` | apps/delivery | Review and release deliverables (quality gate) | Review own work |
| `OPS_ONBOARDING` | apps/delivery | View onboarding projects (OH4 mirror); propose implementation grants (≤ 3 months); record milestone readiness | Act after go-live without a retainer grant |
| `OPS_CSM` | apps/delivery | Health, QBR packs, renewal risk flags, survey triggers; read-only client section | Act in tenant |
| `OPS_SUPPORT_AGENT` | apps/delivery | Ticket context (OH6 mirror); request time-boxed support sessions | Read tenant content without a client-approved support session |
| `OPS_CONSUMER_CASE_MANAGER` | apps/delivery (Consumer Help brand context only) | Work the `chp` queue; prepare complaints the user files or files as a non-advocate authorised representative where the forum allows (NN-23) | Hold any grant in a company tenant flagged lender/insurer/group-client; see any non-`chp` client; promise outcomes; collect dues |
| `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER` | apps/delivery (practitioner workspace) | Work engagements assigned by P16; act as maker in a client tenant under a client-approved grant; deliverables; time; own Rule 36 profile; payout status | See other professionals' engagements; see leads, rankings or ratings; solicit; be checker in a client tenant |
| `PRO_FIRM_ADMIN` / `PRO_FIRM_MEMBER` | practitioner workspace | Firm admin assigns firm members to the firm's engagements and client links | Add members to a client tenant without client approval |
| `ORG_OWNER`, `ORG_ADMIN` | apps/web, apps/mobile | Approve/deny/revoke grants; set standing authorisation; create delegated makers; bind checkers; enable/disable vault; own vault entries; approve master-data changes; read access log; configure what LawDocs sees | — |
| `ORG_CHECKER`, `ORG_APPROVER`, `ORG_DEPT_HEAD`, `ORG_CLO` | apps/web | Check work submitted by delegated makers in their scope; nominate checkers (dept head, CLO) | — |
| `ORG_DELEGATED_MAKER` | tenant | Role assumed by a grantee inside the tenant during an act-in-tenant session | Any checker/approver/admin permission |
| `PLT_SUPER_ADMIN` | apps/console | Make or check master-data changes (never both on one request); emergency revocation of any grant | Approve a grant on the client's behalf; decrypt vault secrets; act in tenants through the delivery console |
| `PLT_SECURITY_OFFICER` | apps/console | Vault anomaly review; break-glass co-approval; access-review evidence | Reveal secrets |
| `PLT_GRIEVANCE_OFFICER` | apps/console | Sees delivery-related grievances routed from OH6/P21 | — |
| OH services (machine) | `int` | Send provisioning, tickets status, invoices, entitlements, staff lifecycle; receive aggregates | Read tenant data |

---

## 4. Functional requirements

### 4A. Staff identity, portfolio and assignments

- **FR-P18-01 — Staff provisioning.** Provision delivery staff from the group IdP (Entra ID, fed by OH10 joiner/mover/leaver and OH12.3) via SCIM 2.0 into Keycloak realm `ld-staff`. Projection fields: `usr_` id, OH employee id, employing legal entity (`ent_`), brand scope (`LAWDOCS` | `CHP` | both prohibited — see FR-P18-73), job role → role code mapping (Appendix X §X.8), practice, manager, work State, status, professional credential refs (from OH9 where the staff member is enrolled; informational). Passkey enrolment is mandatory before first client access.
- **FR-P18-02 — Leaver and mover.** On `EmployeeOffboarded` (OH, `oh` scope) or a role change: suspend all grants of that person within 15 minutes, end live sessions within 60 seconds, generate vault rotation prompts for every credential the person revealed in the last 180 days, reassign open tasks and deliverables to the backup RM, notify each affected client admin. Hourly SCIM reconciliation catches missed events.
- **FR-P18-03 — Assignments.** `sdc.assignments`: client (`ten_` + `ent_`) or buyer org without tenant, staff, role (RM, BACKUP_RM, PROFESSIONAL, REVIEWER, CSM, ONBOARDING), engagement/retainer refs, start/end, capacity points. Rules: a retainer or LDaaS client must have an RM and a backup RM; `sdc.rm.max_clients` caps load; assignment of a PRO_* or OPS_* to a client runs the conflict check (FR-P18-73, OH1.6).
- **FR-P18-04 — Portfolio home** (SCR-P18-01). Client cards sorted by **next breach** = earliest of: SLA clock ≥ 75%, statutory or contractual due date of a task held by the user, unanswered client message > 1 working day, grant expiring ≤ 14 days, master-data request awaiting the user, renewal ≤ 60 days. Filters: practice, segment (Individual, Startup, SME, Enterprise, NBFC/FI), plan, retainer type, health band, State. Click budget: client section ≤ 2 clicks.
- **FR-P18-05 — Unified work inbox** (SCR-P18-02). Tasks (`tsk_`) assigned to the user across all tenants where they hold grants, fetched through a per-tenant federated query under each grant (no cross-tenant join; NN-01). Keyboard: `J/K` move, `O` open, `R` remind client, `T` log time.
- **FR-P18-06 — Reassignment wizard.** Outgoing RM writes a hand-over note → system proposes new grants for the incoming RM to the client admin → on approval, old grants revoked, tasks reassigned with history, client notified with the new RM's name and contact.

### 4B. Client section (one per client company)

One section per client legal entity (`ent_`); a group with several entities shows an entity switcher. Every tab reads through the client's grant or through commercial metadata only; nothing is copied into `apps/delivery` storage except projections listed in §7.2.

| Tab | Content (source) | Notes |
|---|---|---|
| **Overview** | Legal name, constitution, CIN/LLPIN, GSTIN(s), registered office (read-only, `org`); segment; plan; active engagements/retainers; RM/backup RM; next meeting; open tickets count (OH6 status); renewal date; health band (§4K) | Edit is never possible here; "Request a change" opens §4F |
| **Contacts** | Client-designated contacts and roles: owner, admins, CLO, department heads, checkers, billing contact, grievance contact | Read from tenant `org`; RM may propose a contact role change, applied by client admin |
| **Plan & entitlements** | Plan, add-ons, meters (eSign credits, eStamp, AI credits, matters, TM marks, seats) with usage — P17 mirror of OH8 `EntitlementChanged` | Read-only |
| **Engagements & retainers** | P16 records: scope, SLA, hour bank, deliverables, monthly reports, change requests, renewal | Change requests raised here route to P16 |
| **Tasks** | Tasks in scope of the user's grants: held by LawDocs, awaiting client input, returned by checker | "Remind client" uses a polite template, rate-limited (`sdc.reminders.max_per_day`) |
| **Deliverables** | §4G register | — |
| **Messages** | `msg` threads: General, per engagement, per topic | §4G |
| **Meetings** | Scheduled/past meetings with Teams/Meet links, agenda, notes | §4G |
| **Shared drive** | Registered locations (LawDocs DMS "Shared with LawDocs" folder default; client SharePoint/OneDrive/Google Drive link; LawDocs working site) | Opens in browser |
| **Billing & invoices** | Mirror of the client's own Billing page (§4H) | Read-only + quote drafting |
| **SLA & reports** | §4J | — |
| **Access log** | Every access by LawDocs staff, professionals, support, agents and break-glass (§4D) | Same data as the client's Access transparency page |
| **Notes** | Internal delivery notes | DLP blocks credentials, Aadhaar and full PAN; visible to the client on request and always in a DPDP access request |

- **FR-P18-07 — Overview headline metrics.** Show only metrics the client allowed under `sdc.client_visibility.metrics` (default: open tasks with LawDocs, overdue tasks, contracts expiring in 30 days, hearings in 7 days, TM deadlines in 30 days — counts only). Each metric has an "i" key (`hlp.sdc.<metric>`).
- **FR-P18-08 — Entity scope.** A grant names one or more legal entities of the client; tabs filter by entity; a user without a grant for an entity sees only its commercial metadata.
- **FR-P18-09 — Empty states.** "You do not have maker access to this client yet — propose a grant" with a one-click proposal pre-filled from the retainer scope.
- **FR-P18-10 — Client section for buyers without a tenant.** Marketplace buyers who bought services without a subscription (D-11, R-040) get a lightweight section: orders, deliverables (delivered to the buyer's free Personal or Company vault created at checkout), messages, invoices. No act-in-tenant.

### 4C. Delivery grants, RM as maker, client checkers (R-064; NN-17)

- **FR-P18-11 — Grant object** (`sdc.delivery_grants`, `grt_`, tenant RLS; the 1:1 delivery extension of the P02 supertype row in `iam.grants` — one `grt_` id, one state machine, Appendix A §A.9, R-A-05). Fields: grantee (`usr_` staff or professional), grantee kind (`LAWDOCS_STAFF`, `PRACTITIONER`, `PRACTITIONER_FIRM_MEMBER`), tenant role assumed (`ORG_DELEGATED_MAKER` only), scope = {legal entities, departments (`dep_`), functions (CLM, LITIGATION, IP, NOTICES, PLEADINGS, GOVERNANCE_DRAFTING, POLICIES, HR_DOCS, TAX_PREP, BUSINESS_SERVICES), record classes, folders}, allowed actions (create/edit drafts, submit for check, upload, message users, create tasks for client users, run permitted Vidhi missions), data-class ceiling, purpose (`RETAINER_DELIVERY`, `ENGAGEMENT_DELIVERY`, `IMPLEMENTATION`, `SUPPORT_SESSION`), basis ref (`rtn_`/`eng_`/OH4 project id), checker binding (users or positions per department), valid_from, valid_to, approver, state, version.
- **FR-P18-12 — Duration caps.** Retainer ≤ 12 months; engagement ≤ engagement end + 30 days; implementation ≤ 3 months; support session ≤ 8 hours. Renewals create a new version; there is no silent extension.
- **FR-P18-13 — Two-way initiation, client approval.** (a) **Client-initiated:** Settings › LawDocs team › Add maker → pick from the assigned delivery team, an engaged professional, or "any RM LawDocs assigns under our standing authorisation" → set departments, functions, checkers → confirm with step-up → `ACTIVE`. (b) **LawDocs-initiated:** OPS_RM/OPS_DELIVERY_LEAD proposes (pre-filled from retainer scope) → client admin receives a mandatory notification (in-app, email, push) → approve / edit / deny → `ACTIVE`. Click budget for the client: ≤ 2 taps from notification. A Super Admin can never approve on the client's behalf (`LD-SDC-008`).
- **FR-P18-14 — Standing authorisation (fast path, OFF by default).** The client may record, in the eSigned retainer or in Settings, a **standing authorisation**: LawDocs may activate named-role makers (e.g., "up to 3 RMs/professionals from the LawDocs NBFC practice") within a fixed scope and end date without per-person approval. Each activation notifies the client admin within 1 hour, appears in the access log, and is revocable in one tap. This meets the brief's wish that the operations team can "create a maker user" for the client while keeping the client in control [REC]. Setting `sdc.grants.standing_authorisation` (TENANT, default OFF, maker-checker Y).
- **FR-P18-15 — Multiple makers and departmental roles.** A tenant may hold any number of active grants; each grant may cover several departments; the same department may have several makers. Departments come from `org` (P02/P13), including finance-company structures (Compliance, Legal, Credit, Operations, HR, Secretarial). Assigning a maker to a department maps a permission bundle (Appendix D) for the chosen functions.
- **FR-P18-16 — Client-created makers for outside professionals.** The client may also create an `ORG_DELEGATED_MAKER` for its own consultant (not LawDocs staff, not a marketplace engagement) through Settings › Users with mandatory contract end date, scope and checker; LawDocs staff are always grants, never ordinary tenant users, so leaver handling and SoD work automatically.
- **FR-P18-17 — Checker binding and SoD.** Every submission by a delegated maker routes only to the bound checkers. No checker bound → submission blocked (`LD-SDC-005`). A delegated maker's work can never be checked or approved by another delivery user, professional or agent (`LD-SDC-007`); attempts to add a grantee as checker/approver/signatory/director/auditor are refused (`LD-SDC-006`).
- **FR-P18-18 — Lifecycle.** `PROPOSED → ACTIVE → RENEWAL_PENDING` (UI label "Expiring"; T−14 notice both sides) `→ ACTIVE` (renewed by fresh client approval) `| EXPIRED`; `ACTIVE → SUSPENDED` (leaver, security alert, retainer suspended, conflict hit, client action) → `ACTIVE | REVOKED`; `REVOKED` is immediate. One machine with P02's grants (Appendix A §A.9; R-A-05). See §5.1.
- **FR-P18-19 — Conflict gate.** Activation calls `POST /v1/conflicts/check` (OH1.6, extended to LawDocs — Appendix X §X.10) with grantee and client `org_id`; a conflict flag blocks activation with `LD-SDC-011` and routes to OPS_DELIVERY_LEAD for reassignment. Professionals also confirm their own conflict declaration per engagement (P16).
- **FR-P18-20 — Outsourcing notice for regulated clients.** Where the client is an RBI/SEBI/IFSCA-regulated entity, the grant screen shows the client's outsourcing notice (text from P16 retainer terms) and offers an entry in the client's outsourcing register (LDC if connected; otherwise a downloadable record) [INTERP; VERIFY current outsourcing directions per client category].

### 4D. Act-in-tenant sessions, support sessions, break-glass

- **FR-P18-21 — Act-in-tenant.** "Work in <Client> as maker" opens `apps/web` in a delivery session: tenant-scoped token with claims `act=delivery`, `grt`, `dls` (session id), scope; persistent, non-dismissable banner ("You are working in <Client> as a LawDocs maker — grant <id>, scope <…>, expires <date>") using text and icon, not colour alone. Idle timeout `sdc.session.idle_timeout_min`; re-authentication for submissions with legal effect (submit for check, send to counterparty).
- **FR-P18-22 — Ledger attribution.** Every action in a session writes `actor_type = DELIVERY | PRACTITIONER`, `usr_`, `grt_`, `dls_` in the same transaction (NN-45, NN-02).
- **FR-P18-23 — Support sessions.** OPS_SUPPORT_AGENT requests a session from an OH6 ticket: reason code, ≤ 8 hours, read-only by default, client approval required; only the session id travels to OH6.
- **FR-P18-24 — Break-glass.** Dual approval (`PLT_SECURITY_OFFICER` + `PLT_SUPER_ADMIN`, different persons), reason, ≤ 4 hours, real-time alert to the client admin and a written report within 24 hours (NN-17); vault secrets are never reachable by break-glass.
- **FR-P18-25 — Access log.** Client section tab and client-side Settings › Security › Access transparency list every access: who, role, kind (grant session, support, break-glass, agent run, MCP client), when, why (grant/ticket/reason), scope, duration, records touched (counts and record ids, no content). Export CSV/XLSX; included in the tenant export (§13).

### 4E. Credential vault (`cvl`; NN-16, CH-07, CH-10, D-03)

- **FR-P18-26 — OFF by default.** `cvl.enabled` (TENANT, default false). Enabling needs `ORG_OWNER` or `ORG_ADMIN` as maker and a second admin/owner as checker (NN-18), plus acknowledgement of the vault terms. Personal workspaces have no vault (`cvl.personal_workspace_enabled`, PLATFORM, false) [REC: individuals should not share portal passwords].
- **FR-P18-27 — Delegation first.** The entry-type registry (`cvl.entry_types`, PLATFORM content, versioned, reviewer of record) records for each portal whether a native delegation route exists and how to use it (for example engaging a GST Practitioner on the GST portal, adding a CA/authorised representative on the income-tax e-filing portal, creating a sub-user on EPFO/ESIC, professional business user with own DSC on MCA21 — each **[VERIFY]** before the text is published). The "Add credential" flow shows the delegation route first; storing a password requires ticking "Delegation is not available or not suitable" with a reason. Filing returns with a client's password is not the default for tax: CH-10 routes (ERI/GSP, taxpayer EVC/DSC) apply.
- **FR-P18-28 — Entry types (seed).** MCA21 V3 business user; GST portal; Income-tax e-filing; TRACES; EPFO employer; ESIC employer; Shram Suvidha/State labour portals; Udyam; DGFT; IP India e-filing (client's own account, not an attorney's); NeSL; CERSAI; SEBI intermediary portal; stock-exchange listing centres; State e-stamp/e-registration portals; RBI CIMS, DAKSH, PRAVAAH; FIU-IND FINnet; CIC member portals (CIBIL, Experian, CRIF High Mark, Equifax); custom (label + allow-listed URL). **Client-only by default** (`cvl.client_only_types`): RBI CIMS, DAKSH, PRAVAAH, FIU-IND, CIC member portals, CERSAI — grantable to LawDocs only after the client admin ticks an unticked acknowledgement that the portal IDs are issued to named officers and that the client's policy permits sharing [INTERP; VERIFY each portal's terms]. **Blocked types** (cannot be created): net banking, UPI/PIN, e-mail mailbox passwords, DSC token PINs, OTP seeds and authenticator secrets, recovery codes, UIDAI/Aadhaar, DigiLocker, personal credit-bureau consumer logins.
- **FR-P18-29 — Fields.** Portal type, URL (allow-listed per type), username, secret (portal password only), 2FA note (who receives OTP — never the OTP), owner person, custodian(s), purpose, linked obligations/tasks, rotation period, last rotated, expiry, `staff_may_rotate` flag, grantees.
- **FR-P18-30 — Per-credential grants.** Client admin or custodian grants a named user `REVEAL` for ≤ `cvl.grant.max_days` and ≤ the delivery grant; grants show in the delivery client section as "available to you" (no secret).
- **FR-P18-31 — Just-in-time reveal.** Request → link a task or purpose (mandatory) → passkey step-up → client approval if `per_reveal_approval` (default ON for client-only types; tenant-configurable for others) → secret shown for `cvl.reveal_seconds`; copy clears the clipboard after the same period; logged as `CredentialRevealed` with user, purpose, time, IP, device hash → client admin and custodian notified (immediate for client-only types; immediate or daily digest otherwise).
- **FR-P18-32 — Change and rotation.** The client (or a grantee where `staff_may_rotate` = true) records a new secret; delivery staff who change a portal password on the client's behalf must record it in the same session (an auto-task tracks it); after any grant ends the vault lists credentials that person revealed and prompts rotation with a "Rotate now" deep link.
- **FR-P18-33 — No bulk, no export of secrets, no AI.** No bulk reveal; exports carry metadata only (portal, masked username, owner, rotation dates, reveal log); secrets are excluded from search, Vidhi context, MCP tools, logs, traces and support tickets (NN-15, NN-32).
- **FR-P18-34 — Anomalies.** Alert client admin and `PLT_SECURITY_OFFICER` on: > `cvl.anomaly.reveals_per_hour`; reveal outside `cvl.allowed_hours` (if set); new device; reveal without an open linked task; repeated denied attempts. High-severity anomaly suspends the user's vault access pending review.
- **FR-P18-35 — Visibility to the client.** Settings › Credential vault shows entries, grants, the full reveal/change log and pending rotation prompts; the same log appears in the Access log tab.

### 4F. Master-data change requests (CH-26, R-066; NN-18)

- **FR-P18-36 — Field classes.** **Class A (crucial):** legal name, constitution, CIN/LLPIN/registration number, PAN, GSTIN(s) and their States, registered office, owner identity and primary contacts, authorised signatories, billing entity and invoice GSTIN, brand/entity profile, storage/residency target. **Class B:** trade names, branch addresses, departments, logos, preferences — client self-service.
- **FR-P18-37 — Client self-service first.** `ORG_OWNER` may change Class A fields that can be re-verified (P01 KYB lookups through licensed vendors; NN-05) with step-up; the change is maker-checker inside the tenant if the tenant has a second admin.
- **FR-P18-38 — Super Admin path.** Used when a field is locked after verification, when the client asks LawDocs to make the change, for account recovery, or for registry-sourced corrections. Flow: request (raised by OPS_RM on behalf of the client, by the client via ticket, or by `PLT_SUPER_ADMIN`) with evidence → **client approval** by `ORG_OWNER` (or two `ORG_ADMIN`s) with step-up in web or mobile → **checker** `PLT_SUPER_ADMIN` ≠ maker → applied as a **Correction Entry** referencing the original (NN-02) → notification to every owner/admin and, for contact changes, to both old and new channels → 7-day "Report a problem" window with one-click revert request. Target SLA: 1 working day from client approval (`sdc.masterdata.sla_hours`).
- **FR-P18-39 — Exceptions.** (a) **Account recovery** (owner lost access): owner identity re-verification (OVSE/Aadhaar offline verification or DSC; NN-03/NN-04), authorised-signatory board resolution or partner letter upload, 72-hour hold with notices to all registered contacts, then maker-checker apply. (b) **Legal compulsion** (court or regulator order): counsel attachment + maker-checker; client notified unless the order forbids it. No other path exists.
- **FR-P18-40 — Transparency.** The client sees a tracker (SCR-P18-33): requested by, evidence, old → new values, approvals, applied time; RMs see status only. Every downstream system is updated by event (`MasterDataChangeApplied`); OH3/OH8 receive only the commercial fields they hold (legal name, GSTIN, billing address, billing contact) for invoices.

### 4G. Deliverables, messages, meetings and shared drives

- **FR-P18-41 — Deliverables register** (`dlv_`). Type (agreement draft, policy, notice, pleading draft, board/committee papers, minutes draft, annual report draft, return package, compliance report, legal opinion by an engaged advocate, filing acknowledgement, training material, other), status `DRAFT → IN_REVIEW → RELEASED → ACCEPTED | RETURNED`, due date, SLA link, engagement ref, client owner, linked tenant record (e.g., `agr_`, `drf_`, `pld_`). Release needs `OPS_QA_REVIEWER` ≠ author (`LD-SDC-015`). Advocate opinions are released by the advocate under their own name (NN-41).
- **FR-P18-42 — Single source of truth.** Released deliverables are filed in the client's LawDocs vault (`dms`) with version, SHA-256, deliverable id and engagement ref, in Office-openable formats (DOCX/XLSX/PPTX/PDF, PDF/A where required) — even when drafted in SharePoint or Google Drive.
- **FR-P18-43 — Bulk delivery.** Upload a folder (e.g., 12 policies) with mapping preview to tenant targets; uses P04 folder intake rules; nothing overwrites an approved record; each item arrives as a draft for the client checker.
- **FR-P18-44 — Messages.** `msg` threads per client: General, per engagement/retainer, per topic; participants = assigned team + client users invited by the client admin; attachments stored in the client DMS and malware-scanned; mentions, read receipts, search; retention per tenant setting. DLP warns or blocks credentials, Aadhaar numbers and full PAN in messages (NN-04, NN-32). Client users see the same threads in `apps/web` and `apps/mobile` (Messages › LawDocs team).
- **FR-P18-45 — E-mail bridge (optional).** Inbound address per client channel at a LawDocs delivery sub-domain [OWNER: domain]; only allow-listed client domains post into threads; outbound replies from the staff member's M365 mailbox via Graph or from the platform mailer "on behalf of" (`sdc.email.outbound_mode`). No mailbox scraping.
- **FR-P18-46 — Meetings.** "Schedule meeting" (≤ 3 clicks) creates a Teams meeting through the staff member's M365 account via `WORKSPACE_PORT` (Google Meet when `wks.google.enabled`), invites client contacts, attaches the agenda from the thread, and stores link, time and attendees in `sdc.meetings`. Notes are saved to the client DMS; board and committee minutes follow P13. Calendar sync to the staff calendar uses `sdc.calendar.sync_detail_level` (default `TITLE_ONLY`). Recording is OFF by default and needs all-party consent captured in the meeting record [REC].
- **FR-P18-47 — Shared drive link** (owner brief: "common drive link … openable in browser to deliver files like policies"). Per client, register one or more locations: (a) **default** — the LawDocs DMS folder "Shared with LawDocs" inside the tenant; (b) the client's SharePoint/OneDrive or Google Drive folder, as a plain link or via delegated access with the client's consent (P19); (c) a LawDocs working site for the client in LawDocs' M365 tenant (`LawDocs-Clients/<client-code>`), for working drafts only. Links open in the browser under the suite's own authentication. Registering (b) or (c) shows the residency note in §4N.
- **FR-P18-48 — Deliver to drive.** "Deliver" on a released deliverable files it in the DMS (always) and, if the client chose, also copies it to the client's registered drive folder through `WORKSPACE_PORT` with idempotency key and hash check (NN-46); the DMS copy remains canonical.

### 4H. Billing and invoices view (mirror of the client Billing page; R-065)

- **FR-P18-49 — Same component, same data.** The Billing tab renders the P17 Billing page component in read-only mode with the client's data from the P17 mirror of OH8: plan, add-ons, renewal date, auto-renew state, entitlements and meters, invoices and credit notes (PDF from the OH8 document reference), payment status, dunning stage, retainer hour bank, service credits. Payment-method details are never shown.
- **FR-P18-50 — Quotes and upsells.** RM drafts a quote through `BILLING_PORT` (`POST /v1/billing/quotes`) for add-ons, seats, services or retainer changes; the client accepts on its own Billing page (P17); discounts beyond the RM's DoA route to OH8 approval; no urgency or pressure copy (NN-50).
- **FR-P18-51 — Invoice questions and disputes.** "Question this invoice" raises an OH6 ticket of category `LD_BILLING_DISPUTE` with the invoice reference, which pauses dunning for that invoice (Appendix X §X.6).
- **FR-P18-52 — No money handling by staff.** RMs cannot create payment links outside OH8; the client section shows a fixed notice: "LawDocs never asks you to pay into a personal account. All payments go through LawDocs' checkout." (anti-fraud; NN-22).

### 4I. Consumer case manager queue (`[Consumer Help Brand]`; D-06, NN-23)

- **FR-P18-53 — Separate brand context.** OPS_CONSUMER_CASE_MANAGER signs in to `apps/delivery` in the Consumer Help brand context (brand theme, separate entity profile, separate menu). The queue lists `grv_` cases (LD-GRV-…) from the `chp` tenant partition only; no other client, tenant or brand data is reachable (separate encryption keys and search index).
- **FR-P18-54 — Intake triage.** New cases show category (loan/lending grievance, recovery-harassment evidence, insurance claim, credit-report dispute, challan, vehicle transaction), forum eligibility from P15 rules, clocks and a "Waiting on: Bank / Insurer / You / Ombudsman / Court" chip.
- **FR-P18-55 — Conflict check before acceptance.** Submit the keyed hash (`HMAC-SHA256` with the epoch key, P15 FR-P15-42) of the opposite party's legal name/CIN/RBI or IRDAI registration to the group conflict service; the answer is only "conflict / no conflict" (R2 §5.6). On conflict, the case continues as self-serve only or is declined, and the user is told in generic terms.
- **FR-P18-56 — Representation rules.** The queue enforces the P15 permission matrix: for RBI Ombudsman complaints, the user files or a **non-advocate** case manager files under a written authorisation; panel advocates are never shown as representatives there (RB-IOS 2026 Cl. 10(1)(b), R2) [VERIFY clause text at build]. Advocates are engaged only through a P16 fixed-fee SKU on a separate invoice.
- **FR-P18-57 — Conduct locks.** Outbound messages pass a lint that blocks outcome promises ("guaranteed", "waiver", "100% refund"); payment links for fines, challans or dues are impossible (the user pays on official portals — deep links only); success-fee features stay OFF (CH-31; RS-LD-40).
- **FR-P18-58 — People wall.** A person cannot hold `OPS_CONSUMER_CASE_MANAGER` (or any CHP brand scope) and any delivery grant in a company tenant flagged `counterparty_class ∈ {LENDER, INSURER, GROUP_CLIENT_LENDER_SIDE}`; the identity layer rejects the combination (`LD-SDC-020`); quarterly recertification.

### 4J. Practitioner workspace (third-party professionals; D-05, NN-21, NN-41)

- **FR-P18-59 — Workspace.** PRO_* users (realm `ld`) see: My engagements (assigned by the P16 engine — never bought leads), engagement workspace (messages, files, deliverables, hearing/deadline calendar), client links (grants), time, earnings and payouts (Route transfer status from OH8), own profile.
- **FR-P18-60 — Profile.** Advocates edit only BCI Rule 36-permitted fields (name, qualifications, enrolment number and State Bar Council, areas of practice, languages, contact details) [LAW: BCI Rules Part VI Ch. II r.36 as amended 2008]; no ratings, reviews, rankings, fees, badges or testimonials are displayed or editable (NN-21). CA/CS fields follow their institute switches (CH-09).
- **FR-P18-61 — Client links.** A professional acts in a client tenant only under a client-approved delivery grant (same model as §4C, grantee kind `PRACTITIONER`), maker only; firm admins assign firm members to the firm's engagements but cannot add them to a client tenant without client approval.
- **FR-P18-62 — Fees and invoices.** The professional's fee and LawDocs' platform fee appear as separate lines (NN-22); the professional's invoice is issued in the professional's name (RCM flag where the advocate's client is a business entity — R6 §R6.3, [TAX MEMO]); payouts through Razorpay Route only; TDS capture per the payer's obligation [TAX MEMO]. No commission on advocates' fees and no listing, lead or ranking fee (RS-LD-27/28/29 prohibited).
- **FR-P18-63 — Independence of judgement.** The workspace never lets LawDocs staff edit an advocate's opinion after release; LawDocs may return it with comments; the professional signs or eSigns their own work (NN-41).

### 4K. SLA tracker, health and reports

- **FR-P18-64 — SLA tracker.** SLA definitions from P16 (`sla_`): first response, turnaround per deliverable type, hour bank, availability windows. Clocks run on the client entity's business calendar (IST default, national and State holidays from P03); pause while "waiting on client"; alerts at 50%, 75% and 100% to RM and delivery lead; breach records feed service credits (`in.infrabyx.billing.ServiceCreditIssued.v1`, proposed — Appendix Y) issued by OH8.
- **FR-P18-65 — Delivery health (LawDocs-internal view).** Components with weights (`sdc.health.weights`): adoption aggregates, service (SLA attainment, CSAT, open complaints), commercial (invoice status, renewal proximity), relationship (last meeting, last login). Only the aggregates listed in Appendix X §X.5 go to OH5 as `ClientHealthSignal`.
- **FR-P18-66 — Reports.** Monthly service report per retainer (deliverables, SLA attainment, hours, upcoming deadlines — counts and titles the client allowed), generated as DOCX + PDF into the client DMS; QBR pack; portfolio report for the delivery lead.

### 4L. Time, utilisation, productivity and anti-fraud (NN-33, CH-24, CH-32)

- **FR-P18-67 — Time entries** (`tme_`). Per engagement/retainer/client/category (RETAINER, ENGAGEMENT, IMPLEMENTATION, PRESALES, INTERNAL, TRAINING), duration, billable flag, short non-content description (DLP checked). Log time in ≤ 2 clicks from any task. Staff see and correct their own entries within `sdc.time.edit_window_days`; later corrections are Correction Entries.
- **FR-P18-68 — Aggregation to OH.** Daily `in.infrabyx.ops.TimesheetAggregated.v1` (proposed — Appendix Y): staff id, date, client org id, tenant id, category, engagement id, hours, billable. No task titles or content.
- **FR-P18-69 — Outcome metrics.** Monthly per staff: tasks completed, SLA attainment, deliverables accepted first time, rework rate, CSAT, hours vs plan → `in.infrabyx.ops.DeliveryMetricsMonthly.v1` for OH10 appraisal and OH11 staff ROI; visible to the staff member and their manager; no leaderboards; no automated people decisions.
- **FR-P18-70 — Attendance is not productivity.** The console records sign-in/sign-out (from the IdP) for OH10 attendance only (CH-32). There is no keystroke logging, mouse-activity scoring, screenshot, webcam, microphone or browsing capture, and no setting can enable it (NN-33; `NN-33_no_covert_monitoring`).
- **FR-P18-71 — Anti-fraud controls.** (1) Author ≠ reviewer; (2) RM cannot approve own quote discount; (3) the user who reveals a credential cannot approve its rotation record; (4) no deletion of messages, files, time or deliverables — Correction Entries only; (5) no off-platform payment links (FR-P18-52); (6) anomaly rules: mass downloads (> `sdc.anomaly.downloads_per_hour`), exports outside working hours, grant proposals outside the user's portfolio, repeated reveal denials, time entries exceeding 14 h/day; alerts to delivery lead and `PLT_SECURITY_OFFICER`, with OH11 receiving counts only; (7) quarterly access review of all grants and credential grants with client attestation; unattested grants suspend after 14 days.
- **FR-P18-72 — Gifts and side deals.** Staff declare gifts or hospitality from clients in OH11's register (link from the console); the client section shows the published anti-bribery notice [REC].

### 4M. Operations Hub interfaces (D-02, NN-19, NN-24)

| FR | Interface | LawDocs behaviour |
|---|---|---|
| **FR-P18-73** | Conflict and wall service (OH1.6, extended) | Called on assignment, grant activation and consumer-case acceptance; counts and flags only |
| **FR-P18-74** | CRM — leads, accounts, contacts (OH3) | Delivery staff see the client's CRM account card (commercial fields, contacts with consent states) read-only via OH3 API; "Log activity" sends `POST /v1/crm/activities` (commercial-only summary ≤ 500 chars, classifier + block-list for matter/document terms; Appendix X §X.2); referrals from clients ("my friend needs a rent agreement") create a CRM request only with the referee's consent captured by the client-facing form |
| **FR-P18-75** | Onboarding projects (OH4) | Consume `TenantProvisioned` and self-serve `TenantSelfServeCreated` (proposed); OH4 calls `POST /v1/delivery/assignments` to set the RM team at kick-off; LawDocs proposes implementation grants; client acceptance of milestones in-product produces `ImplementationMilestoneReached` acknowledgement |
| **FR-P18-76** | Support tickets (OH6) | "Raise ticket for client" and the client's "Contact support" call `POST /v1/support/tickets` with category (Appendix X §X.6), severity, deep link, consented context bundle; attachments only after PII scan; ticket status from `SupportTicketOpened/Resolved` shows in the client section and the client's Help › My tickets |
| **FR-P18-77** | CSAT/NPS (OH5) | Ticket-close CSAT and quarterly relationship NPS surveys for retainer clients are triggered from LawDocs and answered in-product; OH5 receives scores and comment sentiment class, never document content; detractor (≤ 6) creates a CSM task |
| **FR-P18-78** | Customer success (OH5) | Daily `ClientHealthSignal` aggregates; RM-raised renewal-risk flags with fixed reason codes; QBR completion |
| **FR-P18-79** | Billing (OH8) | Read entitlements, invoices, credit notes, quotes and payment events through P17's mirror; quotes via `BILLING_PORT`; service credits via proposed `ServiceCreditIssued` |
| **FR-P18-80** | Staff identity (OH10/OH12) | SCIM joiner/mover/leaver into `ld-staff`; `EmployeeOffboarded` consumer; job architecture mapping (Appendix X §X.8) |
| **FR-P18-81** | Directory (OH9) | `ProfessionalEmpanelled`/`ProfessionalSuspended` update practitioner status; a suspended professional's grants suspend within 1 hour |
| **FR-P18-82** | Cross-company roles (OH1; Ecosystem Spec §4.6) | A staff member seconded from another group company holds an OH `group_grant` (purpose `IMPLEMENTATION_DELIVERY` or `CUSTOMER_SUCCESS`, ≤ 90 days, renewal = fresh approval); LawDocs reads it to allow assignment; client delivery grants are still required for tenant access |
| **FR-P18-83** | No content egress | Contract test `NN-19_no_content_to_oh` runs on every LawDocs → OH payload schema and sample corpus: no document text, matter/case numbers, party names, credentials, message bodies, consumer-case data or end-customer personal data |

### 4N. Workspace suites: Microsoft 365 now, Google Workspace later (R-053, R-055; CH-29)

- **FR-P18-84 — `WORKSPACE_PORT`.** All suite calls go through P19's `WORKSPACE_PORT` with adapters `WorkplaceProvider.M365` (Graph; ON) and `WorkplaceProvider.Google` (Drive, Calendar, Meet; flag `wks.google.enabled` OFF). Operations: create meeting, create/update calendar event, resolve and open drive link, copy file to folder, create per-client working site/folder, send mail as user. Least-privilege scopes: delegated `Calendars.ReadWrite`, `OnlineMeetings.ReadWrite`, `Sites.Selected` for working sites, `Mail.Send` (delegated) — scope names **[VERIFY at build against Microsoft Graph documentation]**; Google `drive.file` and Calendar scopes **[VERIFY]**.
- **FR-P18-85 — Residency guard.** LawDocs' own working copies that contain client personal data or legal-matter content may sit only in India-resident Microsoft 365 (Default Geography India) or in the LawDocs DMS; Google Workspace working copies are limited to non-regulated material until a suite with India data residency is confirmed (OH12.1; NN-25). The guard checks the data class on every write and refuses with `LD-SDC-025`.
- **FR-P18-86 — Suite-neutral data.** Drive links, meetings and working sites are records with `provider` and `kind`; canonical files live in the DMS; switching LawDocs from M365 to Google Workspace is a re-point of adapters and links plus an OH12.7 migration of working drafts — no client data migration is needed (NN-12).
- **FR-P18-87 — Client suites.** A client on M365 or Google Workspace may connect its suite in its own Settings (P19); delivery staff then use the client's links; LawDocs never holds the client's suite admin credentials.
- **FR-P18-88 — Office-openable outputs.** Every delivery output is DOCX/XLSX/PPTX/PDF with self-explanatory names: `<Client> – <Deliverable type> – <Title> – v<n> – <YYYY-MM-DD>.docx` (R-053).

### 4O. Client-side surfaces and agents

- **FR-P18-89 — Settings › LawDocs team** (`apps/web`, SCR-P18-30): assigned team with photos off by default, grants (active, pending, expiring), approve/deny/revoke, standing authorisation, checker bindings per department, what LawDocs can see (`sdc.client_visibility.*`), notification preferences.
- **FR-P18-90 — Mobile approvals** (`apps/mobile`, P22): push → deep link → approve grant / master-data change / reveal request / deliverable acceptance with biometric unlock and step-up; protected screens block screenshots (NN-44).
- **FR-P18-91 — Agents in delivery.** An RM may start a Vidhi mission in a client tenant only if the client enabled that agent, only up to the client's autonomy ceiling, and only within the grant scope; outputs are drafts for the bound checker; the agent and the RM appear as co-preparers; irreversible actions require human confirmation (NN-13, NN-43).
- **FR-P18-92 — Customisation hooks.** Client: visibility metrics, standing authorisation, per-reveal approval, allowed hours, reveal notification mode, message retention, email bridge on/off, report template choice. LawDocs (delivery lead, maker-checker): RM capacity, health weights, reminder caps, SLA alert thresholds. None needs a Super Admin or a code release (NN-29).

---

## 5. Workflows and state machines

### 5.1 Delivery grant

State machine: Appendix A §A.9 governs (Resolution R-A-05). P02 and this phase describe **one** grant machine: `iam.grants` (`grt_`, P02) is the supertype register; `sdc.delivery_grants` is the 1:1 delivery extension (scope, bound checker, standing-authorisation fields). Delivery grants emit `sdc.DeliveryGrant*` events only. Canonical state names below; the delivery UI may show the labels in brackets.

| State | Entry | Allowed transitions | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| `PROPOSED` | RM/lead proposes; engagement acceptance | → ACTIVE (or APPROVED until `valid_from`), DECLINED, WITHDRAWN | Client approver (`ORG_OWNER`/`ORG_ADMIN`); proposer (withdraw) | Grantee role = `ORG_DELEGATED_MAKER`; checker bound (`LD-SDC-005`); duration ≤ cap (`LD-SDC-004`); conflict check clear (`LD-SDC-011`); only the client may approve (`LD-SDC-008`) | Mandatory notification; `in.lawdocs.sdc.DeliveryGrantProposed.v1` |
| `APPROVED` (transient) | Client approved with a future `valid_from` | → ACTIVE at `valid_from`; → REVOKED | System; client | — | — |
| `ACTIVE` | Client approves with step-up; client creates directly; activation under a client-approved standing authorisation (X-20; `LD-SDC-009`) | → RENEWAL_PENDING, SUSPENDED, REVOKED | System; client; lead | Standing authorisation in force and within scope | `DeliveryGrantActivated`; access-log entry; activation notice ≤ 1 h if standing authorisation |
| `RENEWAL_PENDING` ["Expiring"] | T−14 days | → ACTIVE (renewed: new version, fresh client approval, never automatic), SUSPENDED, REVOKED, EXPIRED | Client admin; system | — | Notices to both sides; `DeliveryGrantRenewed` on renewal |
| `SUSPENDED` | Leaver, security alert, conflict hit, retainer suspended, unattested review, client action | → ACTIVE (cause cleared, client reinstates), REVOKED | Client admin; lead (security) | Cause cleared | Sessions end ≤ 60 s; `DeliveryGrantSuspended` |
| `REVOKED` | Client, lead, `PLT_SUPER_ADMIN` emergency | terminal | — | — | Sessions end ≤ 60 s; open items reassigned; rotation prompts (§5.2); `DeliveryGrantRevoked` |
| `EXPIRED` | `valid_to` reached in RENEWAL_PENDING | terminal | System | — | As revoke; `DeliveryGrantExpired` |
| `DECLINED` ["Denied"] / `WITHDRAWN` | Client declines / proposer withdraws | terminal | — | — | Ledger |

### 5.2 Credential entry and reveal

State machine: Appendix A §A.55 governs.

```
ENTRY: DRAFT (client) → ACTIVE → [ROTATION_DUE] → ACTIVE (rotated) | ARCHIVED (client)
REVEAL: REQUESTED (grantee; purpose + linked task) → STEP_UP (passkey)
  → [CLIENT_APPROVAL if per_reveal_approval] → REVEALED (cvl.reveal_seconds) → LOGGED → NOTIFIED
Denied: vault OFF | no credential grant | client-only type without acknowledgement | outside allowed hours
        | anomaly lock | grant suspended → LD-CVL-00x with "i" help
After any delivery grant ends → ROTATION_PROMPTED for each credential revealed by that grantee (180-day look-back)
```

### 5.3 Master-data change (Super Admin path)

State machine: Appendix A §A.56 governs (wraps the Correction Entry machine A.1; Resolutions R-A-01 and R-A-21 — P02's `POST /v1/org/master-data-changes` is the tenant-side entry point to this one machine).

| State | Actor | Guard | Next |
|---|---|---|---|
| `RAISED` | OPS_RM / client ticket / PLT_SUPER_ADMIN (maker) | Evidence attached; field class A | `AWAITING_CLIENT` |
| `AWAITING_CLIENT` | ORG_OWNER or two ORG_ADMINs | Step-up; not the maker | `CLIENT_APPROVED` / `CLIENT_REJECTED` |
| `CLIENT_APPROVED` | PLT_SUPER_ADMIN checker | Checker ≠ maker; evidence reviewed | `APPLIED` / `RETURNED` |
| `APPLIED` | System | Correction Entry written in same transaction | `IN_REVIEW_WINDOW` (7 days) → `CLOSED` or `REVERT_REQUESTED` |
| `RECOVERY_HOLD` (exception a) | System | Identity re-verified; signatory authority uploaded | 72 h hold → `CLIENT_APPROVED` path with recovered owner |
| `ORDER_COMPELLED` (exception b) | PLT_SUPER_ADMIN + counsel | Order attached | `CLIENT_APPROVED`-equivalent → checker → `APPLIED` |

Events: `MasterDataChangeRequested`, `MasterDataChangeClientDecided`, `MasterDataChangeApplied`, `MasterDataChangeRevertRequested`.

### 5.4 Deliverable

State machine: Appendix A §A.54 governs.

```
DRAFT (author) → IN_REVIEW (OPS_QA_REVIEWER ≠ author) → RELEASED (filed in client DMS; optional copy to client drive)
  → ACCEPTED (client owner/checker) | RETURNED (comments) → DRAFT (v+1)
Advocate opinion: DRAFT (advocate) → RELEASED by the advocate (LawDocs QA may comment, never edit)
```

### 5.5 Consumer case queue view (not a separate machine)

State machine: Appendix A §A.50 governs (Resolution R-A-19). The case and its states are **owned by P15** (`chp.cases`, `grv_`); this phase builds only a queue view for `OPS_CONSUMER_CASE_MANAGER` and the delivery lead, and writes no case state of its own. Queue columns map to the canonical case states:

| Queue column | Canonical P15 case state(s) |
|---|---|
| New | `INTAKE`, `TRIAGED` |
| Conflict check | `CONFLICT_CHECK` |
| Assigned | `ACCEPTED` (case manager assigned; `chp.CaseAssigned`) |
| Self-serve only (conflict) | `SELF_SERVE` with closure code `SELF_SERVE_ONLY_CONFLICT` if the user stops |
| Working | `EVIDENCE` … `FORUM_PROCEEDING` |
| Waiting on {User, Bank, Insurer, Ombudsman, Court} | Any active state with an open WAITING item (`wf.items`, A.15) whose party type is that party |
| Declined / Closed | `DECLINED` / `CLOSED` (outcome recorded from user evidence; exactly one primary closure code) |

Assignment, reassignment and declines are P15 transitions invoked from this queue; no `chp` event is ever published by `int` (X-26; NN-23).

### 5.6 Leaver sweep (Temporal `LeaverSweepWorkflow`)

State machine: Appendix A §A.57 governs.

```
EmployeeOffboarded → suspend grants (≤ 15 min) → end sessions (≤ 60 s) → list revealed credentials (180 d)
→ create rotation prompts per tenant → reassign tasks/deliverables to backup RM → propose replacement grants
→ notify clients → acknowledge to OH (sweep complete)
```

---

## 6. Screens and UX

| Screen ID | App | Purpose | Key components | Empty / error states | Mobile behaviour | Accessibility notes |
|---|---|---|---|---|---|---|
| SCR-P18-01 | delivery | Portfolio home | Client cards by next breach; filters; KPIs | "No clients assigned — ask your delivery lead" | Responsive; cards stack | Breach reason in text, not colour |
| SCR-P18-02 | delivery | Work inbox (federated) | Task list, keyboard shortcuts, bulk remind | "Nothing due"; tenant unreachable banner per tenant | List view | Shortcuts documented; focus order |
| SCR-P18-03 | delivery | Client list | Search, segment, plan, health | — | — | Table with headers, sortable via keyboard |
| SCR-P18-04 | delivery | Client › Overview | Profile card, metrics allowed by client, team | "Request a change" CTA | Two-column → one | "i" on each metric |
| SCR-P18-05 | delivery | Client › Contacts | Roles, consent state | — | — | — |
| SCR-P18-06 | delivery | Client › Plan & entitlements | Meters with usage bars | — | — | Bars with numeric labels |
| SCR-P18-07 | delivery | Client › Engagements & retainers | P16 cards, hour bank | — | — | — |
| SCR-P18-08 | delivery | Client › Tasks | In scope, awaiting client, returned | "No grant" empty state with propose CTA | — | — |
| SCR-P18-09 | delivery | Client › Deliverables | Register, review queue, deliver | Release blocked message (`LD-SDC-015`) | Read + accept only | — |
| SCR-P18-10 | delivery | Client › Messages | Threads, attachments, DLP warnings | DLP block explains pattern type | Full | Live region for new messages |
| SCR-P18-11 | delivery | Client › Meetings | Schedule (Teams/Meet), agenda, notes | Suite not connected → connect | Join link opens app | Captions reminder |
| SCR-P18-12 | delivery | Client › Shared drive | Registered locations, residency badge | Residency block `LD-SDC-025` | Opens browser | Link purpose text |
| SCR-P18-13 | delivery | Client › Billing & invoices | P17 Billing component (read-only), quotes | OH8 unreachable → cached as-of time | Read-only | Same as client page |
| SCR-P18-14 | delivery | Client › SLA & reports | Clocks, breaches, reports | — | — | Clock text "75% elapsed, 6 h left" |
| SCR-P18-15 | delivery | Client › Access log | Filterable log, export | — | — | — |
| SCR-P18-16 | delivery | Client › Notes | Notes, DLP | — | — | — |
| SCR-P18-17 | delivery | Client › Act in tenant | Grants held, launch session | Expired grant → renew CTA | — | Banner spec |
| SCR-P18-18 | delivery | Client › Credentials | Available to me, request, reveal | Vault OFF explanation | Reveal disabled on mobile web by default (`cvl.reveal_on_mobile`) | Countdown announced |
| SCR-P18-19 | delivery | Propose grant / delegated maker | Scope builder (entities, departments, functions), checker picker | Conflict block `LD-SDC-011` | — | — |
| SCR-P18-20 | delivery | Grants board | Pending, active, expiring, suspended | — | — | — |
| SCR-P18-21 | delivery | Access reviews | Campaign, attest, revoke | — | — | — |
| SCR-P18-22 | delivery | Team & assignments | Capacity, reassignment wizard | — | — | — |
| SCR-P18-23 | delivery | Me › Time | Timesheet, corrections | — | Quick log | — |
| SCR-P18-24 | delivery | Me › My metrics | Outcome metrics (own) | — | — | No ranks shown |
| SCR-P18-25 | delivery | Portfolio reports | SLA, utilisation, renewals | — | — | — |
| SCR-P18-26 | delivery | Consumer case queue (CHP brand) | Queue, clocks, waiting-on chips, conflict status | Conflict → self-serve banner | Responsive | Plain-language status |
| SCR-P18-27 | delivery | Practitioner home | Engagements, calendar, payouts | — | Responsive | — |
| SCR-P18-28 | delivery | Practitioner profile (Rule 36 fields) | Allowed fields only | Blocked field message | — | — |
| SCR-P18-29 | delivery | Product switcher | Deep links to OH, LDC, Finbyx, Udofin, Equator consoles per roles | — | — | — |
| SCR-P18-30 | web | Settings › LawDocs team | Team, grants, standing authorisation, checkers, visibility | — | Mobile parity | — |
| SCR-P18-31 | web/mobile | Approve request (grant, reveal, change, deliverable) | Summary, scope, step-up | Expired request | Primary on mobile | Large targets |
| SCR-P18-32 | web | Settings › Credential vault | Enable (maker-checker), entries, grants, log, rotation | Delegation-first panel | View only on mobile | — |
| SCR-P18-33 | web | Master-data change tracker | Old → new, approvals, timeline | — | Mobile | — |
| SCR-P18-34 | web | Settings › Security › Access transparency | Same as SCR-P18-15 | — | Mobile | — |
| SCR-P18-35 | console | Master-data change queue | Maker/checker, evidence viewer | — | — | — |
| SCR-P18-36 | console | Break-glass approvals | Dual approval | — | — | — |

UX rules: `Ctrl/Cmd+K` palette searches clients, tasks and deliverables in scope; every jargon term carries an "i" (`hlp.sdc.delivery_grant`, `hlp.sdc.delegated_maker`, `hlp.sdc.checker`, `hlp.sdc.standing_authorisation`, `hlp.sdc.access_log`, `hlp.sdc.master_data_change`, `hlp.sdc.sla_clock`, `hlp.sdc.hour_bank`, `hlp.cvl.credential_vault`, `hlp.cvl.delegation_first`, `hlp.cvl.just_in_time_reveal`, `hlp.cvl.client_only_portal`, `hlp.chp.ethical_wall`, `hlp.chp.waiting_on`, `hlp.mkp.rule36_profile`). All screens meet WCAG 2.2 AA and IS 17802 (NN-28); no colour-only status; timers announced to screen readers; 400% zoom without loss of function.

Click budgets: client section ≤ 2 clicks from home; propose grant ≤ 3 clicks from the client section; client approval ≤ 2 taps from notification; reveal ≤ 3 clicks + step-up; master-data request ≤ 3 clicks; schedule meeting ≤ 3 clicks; log time ≤ 2 clicks; deliver a released file to the client's drive ≤ 2 clicks.

---

## 7. Backend design

### 7.1 Modules

`sdc` (owner: portfolio, assignments, delivery grants, sessions, deliverables, drive links, meetings, master-data requests, SLA clocks, time, metrics, practitioner links, consumer queue view), `cvl` (owner: vault), `iam` (realms, step-up, token exchange for act-in-tenant), `org` (entities, departments, positions), `wf` (tasks, maker-checker, SLA calendars), `msg` (threads), `dms` (files, deliverable filing), `mkp` (engagements, retainers, SLAs, professionals), `bil` (billing presentation, quotes), `chp` (cases; read via queue), `int` (OH contracts, `WORKSPACE_PORT`, conflict service), `rpt` (reports), `core` (audit ledger, Correction Entries, break-glass).

### 7.2 Tables

All tenant rows carry `tenant_id` + `legal_entity_id` with enforced RLS (NN-01). Retention classes from Appendix R: `R-OPS-8Y` (8 years after relationship end), `R-SEC-1Y` (security logs: 180 days hot in India, 1 year total), `R-LEDGER` (permanent, append-only).

| Table | Key columns | Indexes | RLS | Retention |
|---|---|---|---|---|
| `sdc.staff_projection` | usr_id, oh_employee_id, legal_entity_id, brand_scope, role_codes[], practice, manager_id, work_state, status, scim_id, updated_at | (status), (practice) | staff-plane only | Life + 8y |
| `sdc.assignments` | id, tenant_id, legal_entity_id, usr_id, role, refs[], start_at, end_at, capacity_points | (usr_id, end_at), (tenant_id) | tenant + staff scope | R-OPS-8Y |
| `sdc.delivery_grants` (1:1 extension of `iam.grants`; `state` mirrors the supertype row, canonical names per §5.1) | grt_id, tenant_id, grantee_usr_id, grantee_kind, scope jsonb (entities, departments, functions, classes, folders), actions[], data_class_max, purpose, basis_ref, checker_binding jsonb, valid_from, valid_to, state, proposed_by, approved_by, approved_at, standing_auth_id, version | (tenant_id, state), (grantee_usr_id, state), (valid_to) | tenant RLS | R-OPS-8Y |
| `sdc.standing_authorisations` | id, tenant_id, scope jsonb, max_makers, role_filter, valid_to, approved_by, evidence_doc_id | (tenant_id) | tenant | R-OPS-8Y |
| `sdc.sessions` | dls_id, tenant_id, usr_id, grt_id, kind (DELIVERY, SUPPORT, BREAK_GLASS), started_at, ended_at, ip, device_hash, reason, ticket_ref | (tenant_id, started_at) | tenant | R-SEC-1Y + ledger |
| `sdc.deliverables` | dlv_id, tenant_id, engagement_ref, type, title, version, doc_id, sha256, status, author_id, reviewer_id, released_at, client_decision, linked_record_ref | (tenant_id, status), (engagement_ref) | tenant | R-OPS-8Y |
| `sdc.drive_links` | id, tenant_id, provider (LAWDOCS_DMS, M365_SHAREPOINT, M365_ONEDRIVE, GOOGLE_DRIVE), kind (CLIENT, LAWDOCS_WORKING), url, residency_class, delegated_consent_ref, registered_by | (tenant_id) | tenant | R-OPS-8Y |
| `sdc.meetings` | dmt_id (prefix `dmt_` delivery meeting; `mtg_` is governance meetings — Appendix B §B.1), tenant_id, provider, join_url, starts_at, attendees jsonb (business contacts), agenda_doc_id, notes_doc_id, recording_consent | (tenant_id, starts_at) | tenant | R-OPS-8Y |
| `sdc.notes` | id, tenant_id, author_id, body_enc, visibility, created_at | (tenant_id) | tenant | R-OPS-8Y |
| `sdc.masterdata_requests` | mdc_id (prefix `mdc_` master-data change; `chg_` is reserved for engineering change records — Appendix B §B.1), tenant_id, legal_entity_id, field_key, class, current_value_enc, proposed_value_enc, evidence_doc_ids[], raised_by, client_decision_by, checker_id, state, correction_entry_id, review_window_ends_at | (state), (tenant_id) | tenant + console | R-LEDGER |
| `sdc.sla_clocks` | id, tenant_id, sla_id, subject_ref, started_at, paused_intervals jsonb, due_at, state, breach_at | (due_at, state) | tenant | R-OPS-8Y |
| `sdc.time_entries` | tme_id, usr_id, tenant_id, engagement_ref, category, minutes, billable, note, entered_at, corrected_by_ref | (usr_id, entered_at) | staff + tenant | 8y (OH10 payroll evidence via OH) |
| `sdc.metrics_monthly` | usr_id, period, tasks_done, sla_attainment, first_time_right, rework_rate, csat, hours_planned, hours_logged | (usr_id, period) | staff-plane | 8y |
| `sdc.health_snapshots` | tenant_id, date, score, components jsonb, definition_version | (tenant_id, date) | tenant | 3y |
| `sdc.practitioner_links` | id, pro_org_id, tenant_id, grt_ids[], billing_mode | (pro_org_id) | tenant + practitioner org | R-OPS-8Y |
| `cvl.vault_settings` | tenant_id, enabled, enabled_by, checked_by, per_reveal_default, allowed_hours, notify_mode | — | tenant | R-OPS-8Y |
| `cvl.entry_types` (content) | code, label, url_allowlist[], delegation_route_md, client_only, blocked, reviewer, effective_from | (code) | public read | versioned |
| `cvl.entries` | cvl_id, tenant_id, type_code, url, username_enc, secret_enc (envelope, per-tenant DEK), twofa_note, owner_user_id, custodian_ids[], client_only_ack_ref, rotation_days, last_rotated_at, expires_at, staff_may_rotate, linked_refs[] | (tenant_id, type_code) | tenant, sealed class | Until archived + 1y; secrets crypto-shredded on archive |
| `cvl.grants` | id, cvl_id, grantee_usr_id, mode (REVEAL), valid_from, valid_to, granted_by, per_reveal_approval | (grantee_usr_id) | tenant | R-OPS-8Y |
| `cvl.reveal_events` (append-only) | id, cvl_id, grantee, purpose_ref, approved_by, outcome, revealed_at, ip, device_hash, anomaly_flags | (cvl_id, revealed_at) | tenant | R-LEDGER |
| `cvl.rotation_tasks` | id, cvl_id, reason (GRANT_ENDED, PERIODIC, ANOMALY), created_at, done_at | (cvl_id) | tenant | R-OPS-8Y |

Messages use `msg.channels` (`cnv_`) and `msg.messages` (`msg_`) from the `msg` module (P07 owns `msg`; Resolution R-B-02); the queue uses `chp.cases` (`grv_`) from P15.

### 7.3 APIs (OpenAPI 3.1; all mutating calls require `Idempotency-Key`; NN-46)

| Method | Path | Scope | Notes |
|---|---|---|---|
| GET | `/v1/delivery/portfolio` | `sdc:read` | Staff portfolio |
| GET | `/v1/delivery/inbox` | `sdc:read` | Federated per grant |
| GET | `/v1/delivery/clients/{ten}/overview` | `sdc:read` + assignment | Commercial metadata + allowed metrics |
| POST | `/v1/delivery/clients/{ten}/grants` | `sdc:grant.propose` | Propose grant |
| POST | `/v1/tenant/delivery-grants/{grt}/approve` · `/deny` · `/revoke` · `/renew` | tenant `ORG_OWNER/ORG_ADMIN`, step-up | Client side only |
| POST | `/v1/tenant/standing-authorisations` | tenant admin, maker-checker | — |
| POST | `/v1/delivery/grants/{grt}/activate-under-standing` | `OPS_DELIVERY_LEAD` | Within standing scope |
| POST | `/v1/delivery/sessions` | grantee | Token exchange → tenant token with `act=delivery` |
| POST | `/v1/delivery/sessions/{dls}/end` | grantee/system | — |
| POST | `/v1/console/break-glass` · `/{id}/approve` | `PLT_SECURITY_OFFICER`, `PLT_SUPER_ADMIN` | Dual approval |
| GET | `/v1/tenant/access-log` · `/v1/delivery/clients/{ten}/access-log` | tenant admin / assigned staff | CSV/XLSX export |
| POST | `/v1/tenant/vault/enable` · `/approve-enable` | tenant admin maker/checker | — |
| POST/PATCH | `/v1/tenant/vault/entries` | tenant admin/custodian | — |
| POST | `/v1/tenant/vault/entries/{cvl}/grants` | tenant admin/custodian | — |
| GET | `/v1/delivery/clients/{ten}/credentials` | grantee | Metadata only |
| POST | `/v1/delivery/credentials/{cvl}/reveal-requests` | grantee, step-up | Returns approval state or a one-time reveal token |
| POST | `/v1/delivery/credentials/reveal` | one-time token | Returns secret once; never cached |
| POST | `/v1/delivery/clients/{ten}/masterdata-requests` | `OPS_RM`, `PLT_SUPER_ADMIN` | Raise |
| POST | `/v1/tenant/masterdata-requests/{mdc}/decision` | `ORG_OWNER` | Approve/reject |
| POST | `/v1/console/masterdata-requests/{mdc}/apply` | `PLT_SUPER_ADMIN` ≠ maker | Correction Entry |
| POST | `/v1/delivery/clients/{ten}/deliverables` · `/{dlv}/review` · `/{dlv}/release` · `/{dlv}/deliver-to-drive` | per role | — |
| POST | `/v1/delivery/clients/{ten}/meetings` | assigned staff | `WORKSPACE_PORT` |
| POST | `/v1/delivery/clients/{ten}/drive-links` | assigned staff / tenant admin | Residency guard |
| POST | `/v1/delivery/clients/{ten}/quotes` | `OPS_RM` | `BILLING_PORT` |
| GET | `/v1/delivery/clients/{ten}/billing` | assigned staff | P17 mirror |
| POST | `/v1/delivery/time-entries` | staff | — |
| POST | `/v1/delivery/assignments` | OH4 machine client (signed) | Appendix X §X.4 |
| GET | `/v1/delivery/chp/queue` | `OPS_CONSUMER_CASE_MANAGER` (brand CHP) | — |
| GET | `/v1/practitioner/engagements` | PRO_* | — |

### 7.4 Domain events

Internal (`in.lawdocs.<module>.<EventName>.v1`, CloudEvents 1.0, outbox): `sdc.DeliveryGrantProposed`, `sdc.DeliveryGrantActivated`, `sdc.DeliveryGrantRenewed`, `sdc.DeliveryGrantSuspended`, `sdc.DeliveryGrantRevoked`, `sdc.DeliveryGrantExpired`, `sdc.StandingAuthorisationChanged`, `sdc.DelegatedMakerCreated`, `sdc.DeliverySessionStarted`, `sdc.DeliverySessionEnded`, `sdc.BreakGlassOpened`, `sdc.DeliverableReleased`, `sdc.DeliverableAccepted`, `sdc.DeliverableReturned`, `sdc.MasterDataChangeRequested`, `sdc.MasterDataChangeClientDecided`, `sdc.MasterDataChangeApplied`, `sdc.MasterDataChangeRevertRequested`, `sdc.SlaThresholdReached`, `sdc.SlaBreached`, `sdc.TimeEntryLogged`, `sdc.DeliveryAnomalyDetected`, `cvl.VaultEnabled`, `cvl.VaultDisabled`, `cvl.CredentialEntryCreated`, `cvl.CredentialGrantChanged`, `cvl.CredentialRevealRequested`, `cvl.CredentialRevealed` (sealed payload; tenant-only), `cvl.CredentialRotated`, `cvl.CredentialRotationPrompted`, `cvl.VaultAnomalyDetected`. Consumed from P15 (owned and emitted there, not here): `chp.CaseAssigned`, `chp.ConflictChecked` (the former name `chp.ConflictCheckCompleted` is an alias; R-A-19).

Cross-product (published only by `int`; `source = urn:infrabyx:lawdocs:<tenantid>`): **existing** — consume `in.infrabyx.ops.TenantProvisioned.v1`, `ImplementationMilestoneReached`, `SupportTicketOpened`, `SupportTicketResolved`, `in.infrabyx.billing.PlanChanged.v1`, `EntitlementChanged`, `InvoiceIssued`, `SubscriptionPaymentReceived`, `SubscriptionPaymentFailed`, `SubscriptionCancelled`, `in.infrabyx.directory.ProfessionalEmpanelled.v1`, `ProfessionalSuspended`; produce `ReleasePublished`, `ControlEvidenceCollected`. **Proposed in Appendix Y** (never improvised): `in.infrabyx.ops.TenantSelfServeCreated.v1`, `in.infrabyx.ops.ClientHealthSignal.v1`, `in.infrabyx.ops.TimesheetAggregated.v1`, `in.infrabyx.ops.DeliveryMetricsMonthly.v1`, `in.infrabyx.ops.SurveyResponseRecorded.v1`, `in.infrabyx.billing.ServiceCreditIssued.v1`, `in.infrabyx.ops.GrievanceStatusChanged.v1` (metadata mirror to OH6 of the grievance queues owned by P01, P16 and P21; Appendix X §X.6), consumer of `EmployeeOffboarded` (`oh` scope extended to LawDocs). Domains and payloads are fixed in Appendix Y §Y.7.10; mapping in Appendix I §I.8.

### 7.5 Jobs and workflows (Temporal unless noted)

| Job | Trigger | Behaviour |
|---|---|---|
| `GrantExpiryWorkflow` | Grant activation | T-14 notices; expire; rotation prompts |
| `LeaverSweepWorkflow` | `EmployeeOffboarded`; hourly SCIM reconciliation | §5.6 |
| `MasterDataChangeWorkflow` | Request raised | Client approval wait (reminders at 24/72 h), checker, apply, 7-day window |
| `VaultRotationPromptJob` (BullMQ, daily) | Rotation due; grant ended | Prompts and tasks |
| `RevealAnomalyDetector` (stream) | `CredentialRevealRequested/Revealed` | Rules in FR-P18-34 |
| `SlaClockWorker` (BullMQ, 1-min tick) | Clock events | Thresholds, breaches, credits proposal |
| `AccessReviewCampaign` | Quarterly | Staff attestation + client attestation; suspend unattested after 14 days |
| `TimesheetAggregationJob` | Daily 02:00 IST | `TimesheetAggregated` |
| `MetricsMonthlyJob` | WD+2 | `DeliveryMetricsMonthly` |
| `HealthSignalJob` | Daily 04:00 IST | `ClientHealthSignal` |
| `ServiceReportJob` | Monthly | DOCX/PDF report into client DMS |
| `FederatedInboxIndexer` | Task events | Per-tenant partitioned index of tasks held by delivery users |

---

## 8. Integrations

| Port / API | Counterparty | Vendor alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| SCIM 2.0 + OIDC | Entra ID (group IdP fed by OH10/OH12) | Google Cloud Identity (later) | Queue and retry; hourly reconciliation; new staff cannot sign in until provisioned | Manual provisioning in `apps/console` with maker-checker, logged as exception (OI-P18-02) |
| `POST /v1/conflicts/check` | OH1.6 (extended) | — | Fail closed: no activation without an answer | Delivery lead records a manual conflict attestation with evidence, valid 24 h |
| `POST /v1/support/tickets`; ticket events | OH6 | — | Outbox retry; ticket shown "queued" | Email to support role mailbox |
| `POST /v1/crm/activities`, `POST /v1/crm/requests`, CRM account read | OH3 | Brevo is OH's executor, never called by LawDocs directly | Retry; activity kept locally ≤ 7 days then dropped with notice | None needed |
| `BILLING_PORT` (quotes, invoices, entitlements) | OH8 | P17 local adapter only if Appendix X §X.7 LOCAL decision is taken | Billing tab shows last mirror with as-of time | — |
| `POST /v1/delivery/assignments` (inbound) | OH4 | — | Reject unsigned; idempotent on project id | Delivery lead assigns in UI |
| `WORKSPACE_PORT` | Microsoft Graph (ON); Google Workspace (OFF) | — | Meeting creation fails → offer "paste a meeting link"; drive copy fails → DMS copy stands, retry | Paste link manually |
| `DMS_PORT` (internal) | P04 | — | Release blocked until filed | — |
| `NOTIFY_PORT` (`packages/notify`) | Email (SES/Brevo transactional), push, in-app; SMS/WhatsApp via DLT-registered CPaaS (NN-34) | JioCX, others | Channel fallback per preference | — |
| `KMS` | AWS KMS ap-south-1 (per-tenant CMK for `cvl`) | CloudHSM for Enterprise (optional) | Vault read-only if KMS unavailable; no plaintext fallback | — |

---

## 9. Settings and configuration

All keys are registered in Appendix R before code reads them (NN-29). MC = maker-checker.

| Key | Tier | Type | Default | Changed by | MC |
|---|---|---|---|---|---|
| `sdc.rm.max_clients` | PLATFORM | int 5–60 | 25 | OPS_DELIVERY_LEAD + checker | Y |
| `sdc.rm.backup_required_for` | PLATFORM | enum[] | [RETAINER, LDAAS] | PLT_SUPER_ADMIN | Y |
| `sdc.grants.max_months.retainer` | PLATFORM | int 1–12 | 12 | PLT_SUPER_ADMIN | Y |
| `sdc.grants.max_months.implementation` | PLATFORM | int 1–6 | 3 | PLT_SUPER_ADMIN | Y |
| `sdc.grants.engagement_grace_days` | PLATFORM | int 0–60 | 30 | PLT_SUPER_ADMIN | Y |
| `sdc.grants.support_session_max_hours` | PLATFORM | int 1–8 | 8 | PLT_SECURITY_OFFICER | Y |
| `sdc.grants.expiry_notice_days` | PLATFORM | int 7–30 | 14 | PLT_SUPER_ADMIN | N |
| `sdc.grants.standing_authorisation` | TENANT | bool + scope | OFF | ORG_OWNER/ORG_ADMIN | Y |
| `sdc.grants.alternate_approvers` | TENANT | user[] | none | ORG_OWNER | Y |
| `sdc.grants.include_sealed_classes` | TENANT | bool (per grant) | false | ORG_ADMIN (step-up) | Y |
| `sdc.session.idle_timeout_min` | PLATFORM | int 10–60 | 30 | PLT_SECURITY_OFFICER | N |
| `sdc.breakglass.max_hours` | PLATFORM | int 1–4 | 4 | PLT_SECURITY_OFFICER | Y |
| `sdc.client_visibility.metrics` | TENANT | enum[] | [open_tasks, overdue_tasks, contracts_expiring_30d, hearings_7d, tm_deadlines_30d] | ORG_ADMIN | N |
| `sdc.notes.client_visible` | TENANT | bool | false | ORG_ADMIN | N |
| `sdc.reminders.max_per_day` | PLATFORM | int 1–5 | 2 | OPS_DELIVERY_LEAD | N |
| `sdc.calendar.sync_detail_level` | PLATFORM | enum NONE/TITLE_ONLY/TITLE_AND_LINK | TITLE_ONLY | PLT_SECURITY_OFFICER | Y |
| `sdc.email.bridge_enabled` | TENANT | bool | false | ORG_ADMIN | N |
| `sdc.email.outbound_mode` | PLATFORM | enum USER_MAILBOX/PLATFORM_ON_BEHALF | USER_MAILBOX | PLT_SUPER_ADMIN | Y |
| `sdc.meetings.recording_default` | TENANT | bool | false | ORG_ADMIN | N |
| `sdc.masterdata.sla_hours` | PLATFORM | int 4–48 | 8 (working hours) | PLT_SUPER_ADMIN | Y |
| `sdc.masterdata.review_window_days` | PLATFORM | int 3–30 | 7 | PLT_SUPER_ADMIN | Y |
| `sdc.masterdata.recovery_hold_hours` | PLATFORM | int 24–168 | 72 | PLT_SECURITY_OFFICER | Y |
| `sdc.health.weights` | PLATFORM | map, sum 100 | adoption 30, service 30, commercial 20, relationship 20 | OPS_DELIVERY_LEAD + checker | Y |
| `sdc.sla.alert_thresholds_pct` | PLATFORM | int[] | [50, 75, 100] | OPS_DELIVERY_LEAD | N |
| `sdc.time.edit_window_days` | PLATFORM | int 1–14 | 7 | OPS_DELIVERY_LEAD + checker | Y |
| `sdc.anomaly.downloads_per_hour` | PLATFORM | int | 50 | PLT_SECURITY_OFFICER | Y |
| `sdc.access_review.cadence_months` | PLATFORM | int 1–6 | 3 | PLT_SECURITY_OFFICER | Y |
| `sdc.delivery.agent_runs.enabled` | TENANT | bool | false | ORG_ADMIN | Y |
| `cvl.enabled` | TENANT | bool | **false** | ORG_OWNER/ORG_ADMIN (maker) + second admin (checker) | Y |
| `cvl.personal_workspace_enabled` | PLATFORM | bool | false | PLT_SUPER_ADMIN | Y |
| `cvl.client_only_types` | PLATFORM | code[] (add-only) | RBI_CIMS, RBI_DAKSH, RBI_PRAVAAH, FIU_IND, CIC_*, CERSAI | PLT_SECURITY_OFFICER + PLT_LEGAL_REVIEWER | Y |
| `cvl.blocked_types` | PLATFORM (locked) | code[] | NET_BANKING, UPI, EMAIL, DSC_PIN, OTP_SEED, RECOVERY_CODE, UIDAI, DIGILOCKER, CONSUMER_BUREAU | — (code) | — |
| `cvl.reveal_seconds` | PLATFORM | int 10–60 | 30 | PLT_SECURITY_OFFICER | Y |
| `cvl.grant.max_days` | TENANT | int 1–365 | 90 | ORG_ADMIN | Y |
| `cvl.per_reveal_approval.default` | TENANT | bool | true for client-only types; false otherwise | ORG_ADMIN | Y |
| `cvl.allowed_hours` | TENANT | time range | none | ORG_ADMIN | N |
| `cvl.notify_mode` | TENANT | enum IMMEDIATE/DAILY_DIGEST | IMMEDIATE (client-only types always IMMEDIATE) | ORG_ADMIN | N |
| `cvl.anomaly.reveals_per_hour` | PLATFORM | int 2–20 | 5 | PLT_SECURITY_OFFICER | Y |
| `cvl.reveal_on_mobile` | TENANT | bool | false | ORG_ADMIN | Y |
| (no P18 key) — read P15's `chp.brand.enabled` | PLATFORM | bool | false (until P15 exit) | PLT_SUPER_ADMIN (P15) | Y |
| (no P18 key) — conflict-hash epoch key rotation is P15's `chp.conflict.key_rotation_days` | PLATFORM | int | 90 | PLT_SECURITY_OFFICER (P15) | Y |
| `wks.m365.enabled` | PLATFORM | bool | true | PLT_SUPER_ADMIN | Y |
| `wks.google.enabled` | PLATFORM | bool | false | PLT_SUPER_ADMIN | Y |
| `wks.residency.allow_regulated_on_google` | PLATFORM (locked) | bool | false | — | — |

Kill switches (NN-39): `sdc.breakglass.enabled`, `cvl.reveal.enabled` (platform-wide emergency stop), `sdc.email.bridge.global_enabled`, `wks.<provider>.enabled`, `sdc.delivery.agent_runs.global_enabled`.

---

## 10. Security, privacy and audit

| Threat | Control |
|---|---|
| Staff misuse of client access | Client-approved grants only (NN-17); scope by entity/department/function; maker-only role; access log visible to client; quarterly attestation; anomaly rules |
| Credential theft or over-exposure | Vault OFF by default; delegation-first; envelope encryption with per-tenant DEKs under KMS CMK `ld/tenant/<id>/cvl`; no Super Admin key access; decrypt only in the isolated reveal service; never cached or logged; 30-second reveal; per-reveal approval option; blocked types; rotation after grant end (NN-16) |
| Account takeover via master-data change | Class A fields only through client approval + second Super Admin; dual-channel notices; recovery hold; Correction Entries (NN-18, NN-02) |
| Insider fraud (payments, discounts, kickbacks) | No staff payment links; OH8-only checkout; DoA on discounts; SoD; gifts register; OH11 analytics on counts (CH-24) |
| Cross-brand leakage (Consumer Help ↔ lender clients) | Separate brand partition, keys and index; people wall in identity layer; hashed conflict check (NN-23) |
| Data egress to OH or suites | Schema allow-lists and `NN-19_no_content_to_oh`; residency guard for suites (NN-25); calendar title-only |
| Session hijack | Passkeys; token exchange with short TTL; device binding; re-auth for legal-effect submissions |
| Surveillance creep | No monitoring features exist; attendance from IdP only; monitoring notice via OH10 (NN-33) |

- **Data classes:** vault secrets = SEALED; messages and notes = CONFIDENTIAL tenant content; time entries and metrics = staff HR data (processed for employment purposes; DPDP s.7 [VERIFY clause]); access log = SECURITY.
- **DPDP:** LawDocs acts as processor for client data handled in delivery and as fiduciary for staff data; client notices describe delivery access; data principals' requests reach the client via the tenant; delivery staff sign confidentiality undertakings in OH10.
- **CERT-In:** security logs (sessions, reveals, break-glass) retained 180 days in India; NTP-synced (NN-27).
- **Audit events:** every grant change, session start/end, reveal request/outcome, vault setting change, master-data step, deliverable release/acceptance, quote, break-glass, access review decision — in the hash-chained ledger in the same transaction (NN-02, NN-45).
- **Logs and tickets:** no secrets, Aadhaar, OTPs, full PAN or document content (NN-32); OpenTelemetry scrubbers tested with seeded patterns.

---

## 11. AI touchpoints and guardrails

| Feature | Agent / model route | Autonomy | Human confirmation | Guardrails |
|---|---|---|---|---|
| Client brief before a meeting | Vidhi summariser (Bedrock India) | L1 (draft for RM) | RM reads; nothing sent | Grant-scoped retrieval; no vault, no sealed classes; cites records |
| Message and reminder drafting | Vidhi writer | L1 | RM sends | Lint blocks outcome promises and pressure language (NN-50) |
| Deliverable pre-check | Vidhi QA (template conformance, citation resolver) | L1 | QA reviewer decides | Unresolved citations flagged "unverified" (NN-14) |
| Master-data evidence check | Vidhi extraction (registry document vs proposed value) | L0 (advisory) | Super Admin checker decides | Never auto-applies |
| Health explanation | Vidhi analyst | L0 | — | Never predicts churn as fact; never suggests cross-group sales |
| Consumer case drafting | P15 agents | L1 | Case manager + user approve | No outcome promises; AI-draft label (NN-14) |
| Missions in client tenant | Client-enabled role agents | ≤ client ceiling | Client checker approves outputs; irreversible actions need confirmation | Maker-only (NN-43, NN-13) |

Evaluation: golden sets for summaries (no leakage across grants), lint precision/recall on 500 seeded messages, citation-resolver accuracy ≥ 99% on the regression set. AI consumed inside a client session is charged to the client's AI credits only when the client requested it; internal delivery AI is charged to LawDocs' internal budget.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p18/*.feature`)

```gherkin
Feature: Delivery grants and RM as maker

  @P18-AT-01
  Scenario: LawDocs proposes, client approves, RM works as maker
    Given an active NBFC Legal & Compliance Retainer for tenant T with departments "Compliance" and "Secretarial"
    When RM R proposes a maker grant for "Secretarial" with checker C
    Then T's admin receives a mandatory approval notification
    And after the admin approves with step-up in at most 2 taps the grant is ACTIVE
    And R's submissions in "Secretarial" route only to C

  @P18-AT-02 @NN-17
  Scenario: A delivery user can never be a checker
    Given RM R holds an ACTIVE grant in tenant T
    When anyone tries to add R as checker, approver, signatory, director or auditor in T
    Then the change is refused with LD-SDC-006

  @P18-AT-03 @NN-17
  Scenario: Super Admin cannot approve a grant for the client
    When a PLT_SUPER_ADMIN calls the approve endpoint for a PROPOSED grant in tenant T
    Then the API returns 403 with LD-SDC-008 and the attempt is in T's access log

  @P18-AT-04
  Scenario: Standing authorisation activates a maker with notice
    Given tenant T recorded a standing authorisation for up to 3 makers in "Legal" until 31 Mar 2027
    When the delivery lead activates professional P under it
    Then P's grant is ACTIVE without per-person approval
    And T's admin is notified within 1 hour and can revoke in one tap

  @P18-AT-05
  Scenario: Multiple makers across departments
    Given tenant T has grants for RM R1 in "Legal" and RM R2 in "HR"
    Then R1 cannot open HR records and R2 cannot open Legal records

  @P18-AT-06 @NN-01
  Scenario: Federated inbox never crosses tenants
    Given RM R holds grants in tenants T1 and T2
    When R opens the work inbox
    Then each task is fetched under its own tenant grant and no query joins T1 and T2 data

  @P18-AT-07 @NN-02 @NN-45
  Scenario: Leaver sweep
    Given RM R holds grants in 3 tenants and revealed 2 credentials in the last 180 days
    When OH emits EmployeeOffboarded for R
    Then within 15 minutes all R's grants are SUSPENDED and live sessions end within 60 seconds
    And the vault of each tenant holding one of those 2 credentials shows a rotation prompt and the ledger records each step

Feature: Credential vault

  @P18-AT-08 @NN-16
  Scenario: Vault is OFF by default and needs maker-checker to enable
    Given a new company tenant T
    Then Settings shows the vault as OFF
    When admin A1 enables it
    Then it stays OFF until a second admin A2 approves

  @P18-AT-09 @NN-16
  Scenario: Delegation is offered first
    When a client admin adds a GST portal entry
    Then the delegation route panel is shown first
    And saving a password requires the "delegation not suitable" reason

  @P18-AT-10 @NN-16
  Scenario: OTP seeds and DSC PINs cannot be stored
    When a user tries to create an entry of type DSC_PIN or OTP_SEED
    Then the request fails with LD-CVL-003

  @P18-AT-11 @NN-16
  Scenario: RBI CIMS credential is client-only by default
    Given a vault entry of type RBI_CIMS
    When the admin grants it to RM R without ticking the acknowledgement
    Then the grant fails with LD-CVL-005

  @P18-AT-12 @NN-16 @NN-32
  Scenario: Just-in-time reveal is logged, notified and absent from logs
    Given RM R holds a REVEAL grant on the MCA21 entry with per-reveal approval
    When R requests a reveal linked to task "Annual filing FY 2025-26" and the client approves
    Then the secret is shown for 30 seconds once
    And CredentialRevealed is in the ledger and the client admin is notified immediately
    And no log, trace, search index or AI context contains the secret

  @P18-AT-13 @NN-11
  Scenario: Export carries vault metadata, never secrets
    When tenant T exports everything
    Then the export contains the vault register with masked usernames and the reveal log and no secret

Feature: Master-data change (CH-26)

  @P18-AT-14 @NN-18
  Scenario: Registered office change needs client approval and a second Super Admin
    Given RM R raises a registered-office change with evidence for tenant T
    When T's owner approves with step-up
    And Super Admin S2, who is not the maker, applies it
    Then a Correction Entry references the original value
    And all owners and admins are notified with old and new values
    And a 7-day "Report a problem" window opens

  @P18-AT-15 @NN-18
  Scenario: Maker cannot be checker
    Given Super Admin S1 raised a GSTIN change
    When S1 tries to apply it
    Then the API refuses with LD-SDC-017

  @P18-AT-16
  Scenario: Owner email change notifies both channels
    When an owner-email change is applied
    Then notices go to the old and the new email addresses

Feature: Deliverables, drives and meetings

  @P18-AT-17
  Scenario: Reviewer must differ from author
    Given professional P authored a policy deliverable
    When P tries to release it
    Then release fails with LD-SDC-015 until a different OPS_QA_REVIEWER approves

  @P18-AT-18 @NN-11 @NN-46
  Scenario: Final deliverable is filed in the DMS and optionally copied to the client's drive
    Given a released deliverable drafted in SharePoint
    Then a version with SHA-256 and engagement reference exists in T's vault
    And the copy to T's registered OneDrive folder carries an idempotency key and matching hash
    And the item appears in T's export under "09 Services and Engagements"

  @P18-AT-19 @NN-25
  Scenario: Residency guard blocks regulated working copies on Google Workspace
    Given wks.google.enabled is true and the working site provider is GOOGLE_DRIVE
    When staff copy a CONFIDENTIAL matter document there
    Then the write fails with LD-SDC-025

Feature: Billing mirror

  @P18-AT-20
  Scenario: Billing tab equals the client's billing page
    Given tenant T's billing page shows 3 invoices and 1 credit note from OH8
    Then the client section Billing tab shows the same documents and statuses
    And RM R has no control to change plan, price or credit

Feature: Consumer Help wall

  @P18-AT-21 @NN-23
  Scenario: People wall
    Given staff U has role OPS_CONSUMER_CASE_MANAGER
    When anyone proposes a delivery grant for U in a tenant flagged LENDER
    Then the proposal fails with LD-SDC-020

  @P18-AT-22 @NN-23
  Scenario: Conflict check returns only a flag
    Given a new loan-grievance case against lender L
    When the conflict check runs
    Then the case manager sees only "conflict" or "no conflict" and the case continues as self-serve if conflicted

  @P18-AT-23 @NN-23
  Scenario: No dues collection and no outcome promises
    When a case manager drafts "We guarantee a full waiver" or tries to create a payment link for a challan
    Then the message is blocked by the lint and the payment link control does not exist

Feature: Practitioner workspace

  @P18-AT-24 @NN-21
  Scenario: Advocate profile shows Rule 36 fields only
    When advocate A edits the profile
    Then fields for ratings, fees, testimonials, badges and rankings are not available

  @P18-AT-25 @NN-41
  Scenario: LawDocs cannot edit an advocate's released opinion
    Given advocate A released an opinion deliverable
    When an OPS user tries to edit it
    Then the edit is refused and only a comment can be added

Feature: OH interface and workforce

  @P18-AT-26 @NN-19 @NN-24
  Scenario: No content to the Hub
    Given the contract-test corpus of all LawDocs → OH payloads
    Then none contains document text, case numbers, party names, credentials, message bodies or consumer-case data

  @P18-AT-27 @NN-33
  Scenario: No monitoring settings exist
    When any administrator searches Settings for keystroke, screenshot, webcam or browsing monitoring
    Then no such setting exists and the settings API rejects any such key as unregistered (NN-29)

  @P18-AT-28 @NN-43 @NN-13
  Scenario: RM-started agent output needs the client's checker
    Given tenant T enabled the Contract Reviewer agent at L2
    When RM R starts a mission and the agent produces a redline
    Then the redline is a draft awaiting T's checker and nothing is sent to the counterparty without human confirmation

  @P18-AT-29 @NN-39
  Scenario: Emergency stop for reveals
    When PLT_SECURITY_OFFICER turns cvl.reveal.enabled off
    Then all pending and new reveal requests fail with LD-CVL-010 and the action is audited

  @P18-AT-30 @NN-28
  Scenario: Delivery banner is accessible
    Given an act-in-tenant session
    Then the banner is announced by screen readers, has text and icon, and passes axe with no serious violations
```

NN test files: `tests/nn/NN-01_delivery_federated_isolation.spec.ts`, `NN-02_delivery_ledger.spec.ts`, `NN-11_vault_export_metadata_only.spec.ts`, `NN-13_delivery_agent_confirmation.spec.ts`, `NN-16_credential_vault.spec.ts`, `NN-17_delivery_grants_only.spec.ts`, `NN-17_delivery_never_checker.spec.ts`, `NN-18_masterdata_maker_checker.spec.ts`, `NN-19_no_content_to_oh.spec.ts`, `NN-21_practitioner_rule36.spec.ts`, `NN-23_people_wall.spec.ts`, `NN-25_workspace_residency.spec.ts`, `NN-32_no_secrets_in_logs.spec.ts`, `NN-33_no_covert_monitoring.spec.ts`, `NN-39_delivery_kill_switches.spec.ts`.

### Error codes introduced

| Code | Message (user) | Help key |
|---|---|---|
| LD-SDC-001 | You are not assigned to this client. | `hlp.sdc.assignment` |
| LD-SDC-002 | This grant has expired. Ask the client to renew it. | `hlp.sdc.delivery_grant` |
| LD-SDC-003 | This action is outside your grant's scope. | `hlp.sdc.grant_scope` |
| LD-SDC-004 | Grant duration exceeds the allowed maximum. | `hlp.sdc.grant_duration` |
| LD-SDC-005 | Name a client checker for this department before submitting. | `hlp.sdc.checker` |
| LD-SDC-006 | LawDocs makers cannot hold checker, approver, signatory, director or auditor roles. | `hlp.sdc.delegated_maker` |
| LD-SDC-007 | Work by a delegated maker must be checked by the client. | `hlp.sdc.checker` |
| LD-SDC-008 | Only the client can approve access to its workspace. | `hlp.sdc.delivery_grant` |
| LD-SDC-009 | Standing authorisation does not cover this scope or has ended. | `hlp.sdc.standing_authorisation` |
| LD-SDC-010 | Session ended because the grant changed. | `hlp.sdc.session` |
| LD-SDC-011 | A conflict was found. The delivery lead will reassign this work. | `hlp.sdc.conflict_check` |
| LD-SDC-012 | Break-glass needs two different approvers. | `hlp.sdc.break_glass` |
| LD-SDC-015 | A different reviewer must approve this deliverable before release. | `hlp.sdc.quality_gate` |
| LD-SDC-016 | This field needs the client's approval before it can change. | `hlp.sdc.master_data_change` |
| LD-SDC-017 | The person who raised this change cannot apply it. | `hlp.sdc.master_data_change` |
| LD-SDC-018 | Evidence is required for this change. | `hlp.sdc.master_data_change` |
| LD-SDC-020 | Consumer Help staff cannot work for lender or insurer clients. | `hlp.chp.ethical_wall` |
| LD-SDC-021 | Payment links can only be created through LawDocs checkout. | `hlp.bil.checkout` |
| LD-SDC-025 | This storage location is not approved for this type of data. | `hlp.sdc.residency` |
| LD-SDC-026 | Message blocked: it appears to contain a password, Aadhaar number or full PAN. | `hlp.sdc.dlp` |
| LD-CVL-001 | The credential vault is switched off for this workspace. | `hlp.cvl.credential_vault` |
| LD-CVL-002 | Vault changes need a second administrator's approval. | `hlp.cvl.credential_vault` |
| LD-CVL-003 | This type of secret cannot be stored (OTP, PIN, recovery code, banking). | `hlp.cvl.blocked_types` |
| LD-CVL-004 | Link a task or purpose to request access. | `hlp.cvl.just_in_time_reveal` |
| LD-CVL-005 | This regulator portal is client-only unless your admin records the acknowledgement. | `hlp.cvl.client_only_portal` |
| LD-CVL-006 | You do not have access to this credential. | `hlp.cvl.grants` |
| LD-CVL-007 | Waiting for the client to approve this reveal. | `hlp.cvl.per_reveal_approval` |
| LD-CVL-008 | Reveals are not allowed at this time for this workspace. | `hlp.cvl.allowed_hours` |
| LD-CVL-009 | Vault access is paused pending a security review. | `hlp.cvl.anomaly` |
| LD-CVL-010 | Credential reveals are temporarily disabled. | `hlp.cvl.kill_switch` |
| LD-CVL-011 | This URL is not allowed for this portal type. | `hlp.cvl.url_allowlist` |

---

## 13. Exit gate, deliverables and open items

**Exit checklist**

- [ ] `apps/delivery` screens SCR-P18-01…29; tenant/mobile screens SCR-P18-30…34; console screens SCR-P18-35…36.
- [ ] Grant engine, standing authorisation, act-in-tenant token exchange, support sessions and break-glass; external penetration test of the token exchange and the reveal service with no high findings open.
- [ ] Credential vault with KMS envelope encryption, delegation-first registry (each delegation text verified and logged in `docs/compliance/verification-log.md` — NN-38; unverified routes ship as "check the portal's help page" only).
- [ ] Master-data change workflow end to end, including recovery hold and order-compelled path; counsel sign-off on notice wording.
- [ ] OH contracts (tickets, CRM activities, assignments, health signal, timesheets, metrics, surveys, conflict check, SCIM, `EmployeeOffboarded`) contract-tested against the OH sandbox, or stubbed with recorded fallbacks where Appendix X items are not yet built.
- [ ] `WORKSPACE_PORT` M365 adapter certified (meetings, calendar, `Sites.Selected` working sites, drive copy); Google adapter built behind flag OFF.
- [ ] Consumer queue built behind `chp.brand.enabled = false` (P15 key); people-wall and conflict tests green.
- [ ] All §12 scenarios and NN tests green; axe + manual screen-reader pass on SCR-P18-01, -17, -18, -30, -31.
- [ ] Settings in §9 registered in Appendix R; help keys in §6 registered in `hlp`; error codes registered.

**Export-map entries (`xpt.export_map`; `LD-EXPORT-1.0`, Appendix K)**

| Record type | Folder path |
|---|---|
| `sdc.deliverables` + files | One-time engagements: `09 Services and Engagements/<FY>/<Service title> (LD-ENG-…)/03 Deliverables/`; retainers: `09 Services and Engagements/<FY>/Retainers/<Package> (LD-ENG-…)/03 Deliverables/` (Appendix K §K.3.1 governs — X-07) |
| `msg` threads with LawDocs team | One-time: `…/04 Correspondence/`; retainers: `…/06 Messages/` (PDF transcript + JSON) |
| `sdc.meetings` | Retainers: `…/07 Meetings/` (agenda, notes, attendee list); one-time: `…/04 Correspondence/` |
| SLA clocks and monthly reports | Retainers: `…/02 Monthly Reports/` and `…/04 Hour Bank and SLA Statements/` |
| `sdc.delivery_grants`, sessions, access log | `99 System Data (CSV and JSON)/access_transparency/` |
| `cvl` register (metadata), grants, reveal log | `01 Company Profile/Credential Vault (metadata only)/` |
| `sdc.masterdata_requests` + Correction Entries | `01 Company Profile/Change History/` |
| Invoices mirror | `10 Billing and Invoices/<FY>/` (from P17) |
| Staff-side time entries and metrics | Not in client exports (staff HR data; exported from OH10 for the employee) |

**Demo script (15 minutes):** RM home → open NBFC client → propose Secretarial grant → client approves on phone → RM acts in tenant, drafts board resolution, submits to checker → client checker approves → QA releases monthly report → delivered to client OneDrive → client admin views access log → RM requests MCA21 reveal; client approves; reveal logged → RM raises registered-office change; owner approves; second Super Admin applies; notices sent → leaver event suspends a second RM's grants → contract test report for OH payloads.

**Open items**

| ID | Item | Owner | Fallback / flag |
|---|---|---|---|
| OI-P18-01 | Portal terms on sharing RBI CIMS/DAKSH/PRAVAAH, FIU-IND, CIC member and CERSAI credentials with service providers | [COUNSEL] + client compliance | Client-only default + acknowledgement |
| OI-P18-02 | Group IdP and SCIM source for LawDocs staff (Entra ID tenant, domain) | CTO / OH12 | Manual provisioning with maker-checker |
| OI-P18-03 | Actual Microsoft 365 SKU held (CH-29); Intune/conditional access availability for managed-device reveal | [OWNER] | Device registration + risk-based step-up |
| OI-P18-04 | Graph and Google scope names; `Sites.Selected` admin-consent process | Integration lead [VERIFY] | Plain links only |
| OI-P18-05 | Delegation routes per portal (GST Practitioner, income-tax authorised representative/CA, EPFO/ESIC sub-users, MCA professional users) | PLT_LEGAL_REVIEWER [VERIFY] | Generic "check the portal" text |
| OI-P18-06 | Whether LawDocs-employed advocates/CAs may issue work product in their professional capacity (NN-41, D-05) | [COUNSEL] | Company work product for non-reserved services; reserved work by engaged practitioners only |
| OI-P18-07 | Consumer Help entity: non-advocate case managers as authorised representatives (RB-IOS 2026 Cl. 10(1)(b)) | [OWNER] + [COUNSEL] | User self-files with LawDocs drafting |
| OI-P18-08 | E-mail bridge domain, DMARC alignment | CTO | In-app messaging only |
| OI-P18-09 | Ecosystem Spec v1.2 acceptance of proposed events (Appendix Y) | Pack lead / spec owner | Local outbox with REST polling by OH |
| OI-P18-10 | Outsourcing-register entry format for RE clients without LDC | [COUNSEL] | Downloadable record only |
