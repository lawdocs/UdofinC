# Phase P22 — Service Delivery Console and Operations Hub Interface

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

---

## 1. Objective and business outcome

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

## 2. Scope (in / out)

**In scope**

- `apps/delivery` web application (Next.js), realm `ldc-staff` (Keycloak), phishing-resistant MFA (FIDO2/passkeys) for all delivery users.
- Staff directory projection from OH (identities, employing legal entity, job role, manager, status) via SCIM/OIDC from the group identity provider (OH1/OH10).
- Portfolio and assignment management (RM, backup RM, professionals, reviewer per client).
- Per-client section with tabs: Overview, Engagements & retainers, Work, Calendar, Act in tenant, Credentials, Messages, Files & drive, Deliverables, Billing, SLA & reports, Health, Notes, Activity.
- Tenant delivery grants (propose/approve/renew/revoke/expire) and **Act-in-tenant** session mode with visible banner and scoped permissions.
- Client-side creation of maker users for professional services, and LawDocs-side requests to create maker users (R-072).
- Credential Vault (stored in the client tenant; delivery console is a client of it).
- Messaging (client ↔ delivery team), e-mail bridge, meeting links.
- Shared drive links and deliverables register; file delivery into the client DMS.
- Read-only billing view and retainer usage; upsell proposals (quotes) for client acceptance.
- SLA tracker and monthly service report (from P21) in delivery context.
- Interfaces to OH: tickets (OH6), CRM activities and requests (OH3), CS health signals (OH5), timesheets/utilisation (OH4/OH11), onboarding milestones (OH4), billing events (OH8), staff lifecycle (OH10) — all through Ecosystem-Spec contracts.
- Cross-company work: one staff identity, product-specific roles; Finbyx/Udofin/Equator work happens in their own products (deep links), never through LDC.

**Out of scope**

- CRM, marketing, customer-success playbooks, support desk, staff HRMS/payroll/appraisal, internal-controls engine (OH).
- Platform super-admin functions (provisioning, master-data correction, global settings — `apps/console`, P00/P01/P02); the delivery console never edits client master data — it can only request a change, which a super admin applies via Correction Entry (R-074).
- Client tenant features themselves (compliance, governance, policies…) — the delivery maker uses the normal tenant UI under a delivery session.

---

## 3. Personas and permissions touched

| Role | Where | Can | Cannot |
|---|---|---|---|
| `dlv_lead` (delivery head / practice lead) | Console | Assign portfolios, approve proposals within DoA, propose/renew grants, approve trial extensions ≤ 14 d (P20), see all clients of the practice, run access reviews for delivery grants | Approve own proposals; act as checker in any tenant; reveal credentials without a grant |
| `dlv_rm` (relationship manager) | Console + tenant (grant) | Own client portfolio, messages, files, deliverables, propose grants and maker users, act as maker in tenant within grant, request credential access, log time, raise tickets for clients | Check/approve in tenant; change billing; see clients outside portfolio |
| `dlv_professional` (CS/CA/analyst/legal) | Console + tenant (grant) | Work assigned engagements, act as maker within grant, upload deliverables | As above |
| `dlv_reviewer` | Console | Review deliverables before release (quality gate) | Release own work |
| `ten_admin` (client) | Tenant | Approve/deny/revoke grants, create maker users for professional services, own credential entries and grants, see all delivery activity, configure what the delivery team sees | — |
| `ten_checker` (client employee) | Tenant | Check/approve work submitted by delivery makers (R-072) | — |
| `ten_cco` / `ten_dept_head` | Tenant | View delivery activity in their scope; nominate checkers | — |
| `plt_super_admin` | Console (`apps/console`) | Apply master-data change requests from RMs via Correction Entry; emergency revocation of any delivery grant | Use delivery console to act in tenants (separate identity) |
| `plt_security_officer` | Console | Monitor reveal logs, anomalies, quarterly access review evidence | — |
| OH services (machine) | Integration | Receive aggregates and metadata events; send tickets status, milestone acceptances, staff lifecycle | Read tenant data |

---

## 4. Functional requirements

### 4A. Staff identity and portfolio

- **FR-P22-01 — Identity source.** Delivery users are provisioned from the group identity provider (OH1/OH10 via SCIM 2.0 into Keycloak realm `ldc-staff`) with: staff id, employing legal entity, job role (RM, professional, reviewer, lead), practice, manager, location, status, professional credentials (membership numbers from OH9 if the staff member is also an empanelled professional — informational only). Leavers (`EmployeeOffboarded` in OH) are disabled in LDC within 15 minutes and all their tenant grants are suspended and reassigned (FR-P22-12).
- **FR-P22-02 — Assignments.** `sdc.assignments`: client tenant (or buyer org), role (RM, backup RM, professional, reviewer), engagement/retainer refs, start/end, capacity points; maximum active clients per RM (`sdc.rm.max_clients`, G, default 25); backup RM mandatory for retainer clients; reassignment wizard with hand-over note and automatic grant transfer request to the client admin.
- **FR-P22-03 — Portfolio home** (SCR-SDC-01): client cards sorted by "next breach" (earliest of: SLA due, statutory due date of an item assigned to the delivery maker, unanswered client message > 1 BD, grant expiring in ≤ 14 days, renewal ≤ 60 days); filters (practice, entity type, regulator, retainer type, health band); unified **Work Inbox** listing tasks assigned to the staff member across all tenants where they hold grants (read from each tenant through the delivery session API — federated query by tenant, no cross-tenant join, NN-01).

### 4B. Client section (one per client)

- **FR-P22-04 — Overview tab.** Organisation profile (read-only from tenant master data: legal name, CIN/LLPIN, entity type, regulator registrations, group), plan and components (P20 mirror), active engagements/retainers (P21), key contacts (client-designated: admin, CCO, CFO, CS, billing), compliance health headline (only the metrics the client allowed under `sdc.client_visibility.*` — default: on-time %, overdue count, high-risk overdue count, upcoming 30-day deadlines count), open tickets (OH6 status), renewal date, last QBR, next meeting.
- **FR-P22-05 — Work tab.** Tasks assigned to delivery users in this tenant (within grant), items awaiting the client (checker queue length, client inputs pending), items returned by the checker with comments; bulk "remind client" (polite template, rate-limited); new task request to the client (creates a tenant task assigned to a client user, if the grant allows `task.create`).
- **FR-P22-06 — Calendar tab.** Combined view of statutory due dates in scope, SLA due dates, meetings, board/committee dates the RM supports; sync to the staff member's M365/Google calendar via WORKSPACE_PORT with **titles only** (no compliance content beyond the obligation short title; setting `sdc.calendar.sync_detail_level`, G: `TITLE_ONLY` default, `NONE`, `TITLE_AND_LINK`).
- **FR-P22-07 — Engagements & retainers tab.** From P21: scope, SLA attainment, hours used, deliverables, monthly reports; change requests; renewal.
- **FR-P22-08 — Notes tab.** Internal delivery notes (visible to the delivery team; **also visible to the client admin on request** — DPDP access right and transparency; default setting `sdc.notes.client_visible = false`, but notes are never hidden from a DPDP access request or an audit); notes must not contain credentials (DLP check blocks patterns) or sealed-class content.
- **FR-P22-09 — Activity tab.** Every delivery action in this client (grants, sessions, reveals, messages, files, deliverables, tasks) from the audit ledger; exportable; the same log is visible to the client admin in the tenant (Settings › Delivery team › Activity).

### 4C. Tenant delivery grants and Act-in-tenant (R-072)

- **FR-P22-10 — Grant object** (`iam.delivery_grants` in the tenant): grantee staff id, grantee role in tenant (`dlv_maker` mapped to tenant `ten_maker` permissions — never `ten_checker`, `ten_admin`, approver, board, auditor or supervisor roles), scope (departments, functions, compliance packs/instruments, modules, record classes; excludes sealed classes by default — NN-13), allowed actions (create/edit/submit compliance instances, upload evidence, draft policies, prepare return packages, draft minutes, create tasks, message users), data class ceiling, purpose (`RETAINER_DELIVERY`, `ENGAGEMENT_DELIVERY`, `IMPLEMENTATION`, `SUPPORT_SESSION`), basis reference (engagement/retainer id), valid_from, valid_to (≤ 12 months; implementation ≤ 3 months; support session ≤ 8 hours), approver (tenant admin), state.
- **FR-P22-11 — Two-way initiation, one approver.** (a) **Client-initiated**: tenant admin goes to Settings › Delivery team › Add maker from LawDocs, picks staff from the assigned delivery team list (or "any RM assigned by LawDocs"), sets scope and checker(s); grant becomes `ACTIVE` immediately upon admin's step-up MFA confirmation. (b) **LawDocs-initiated**: `dlv_rm`/`dlv_lead` proposes a grant (pre-filled from the retainer's SLA scope) → tenant admin receives an approval request (Notification, mandatory) → approves/edits/denies → `ACTIVE`. Either way the client admin is the only approver (NN-30). A super admin cannot approve on the client's behalf; in an emergency (client admin unavailable for a statutory deadline ≤ 2 days) the client CCO or a second client admin may approve if the tenant configured `sdc.grants.alternate_approvers`.
- **FR-P22-12 — Lifecycle.** `PROPOSED → ACTIVE → EXPIRING (T-14 notice to both sides) → RENEWED | EXPIRED`; `ACTIVE → SUSPENDED` (staff leaver, security alert, retainer suspended, client admin action) → `ACTIVE | REVOKED`; `REVOKED` is immediate and ends any open session within 60 seconds; reassignment produces a new grant for the replacement staff member (old grant revoked) — work items owned by the old staff member are reassigned in the tenant with history kept.
- **FR-P22-13 — Checker binding.** Each grant names the client checker(s) for the scope (user or role); every submission by a delivery maker routes only to those checkers; if no checker is set, submissions are blocked (`LDC-SDC-005`). Rule: a delivery maker's work can never be approved by another delivery user (SoD across organisations, test `NN-05_delivery_never_checker`).
- **FR-P22-14 — Act-in-tenant session.** From the client section, "Work in <Client> as maker" opens the tenant app in a delivery session: persistent banner "You are working in <Client> as a LawDocs maker (grant #, scope, expires …)"; tenant UI shows only scoped items; actions carry `actor_type = DELIVERY`, staff id, grant id and session id in the audit ledger; session timeout 30 min idle; re-auth for submissions with legal effect (e.g., submitting a return package for checking).
- **FR-P22-15 — Client-created maker users for professional services.** Tenant admin can also create a regular tenant maker user for an outside professional (not LawDocs staff) — e.g., the client's own consultant — through Settings › Users with user type `EXTERNAL_PROFESSIONAL` (contract end date mandatory, scope limited like a grant, no admin rights). LawDocs delivery users are always grants, never ordinary tenant users, so that leaver handling and SoD work automatically.
- **FR-P22-16 — Support sessions.** For product-support troubleshooting the console uses the P00 break-glass pattern (time-boxed ≤ 8 h, reason-coded, client-approved, read-only by default, visible to the tenant), linked to an OH6 ticket id (only the session id travels to OH; OH2.3).

### 4D. Credential Vault (D-04; R-073)

- **FR-P22-17 — Location and ownership.** The vault lives in the client tenant (`cred` sub-schema of `sdc` inside the tenant's encryption boundary; tenant-specific data key wrapped by KMS key `ldc/tenant/<id>/cred`; NN-13 sealed class). Each entry is owned by the client admin (or a delegated client "vault custodian").
- **FR-P22-18 — Entry types** (seed): MCA21 (V3) business user, DSC holder reference (never the DSC private key or PIN — DSC tokens stay with holders), GST portal, Income-tax e-filing, TRACES, EPFO employer, ESIC employer, Shram Suvidha / State labour portals, CERSAI, CKYCR, FIU-IND FINnet, CIC member portals (CIBIL, CRIF High Mark, Experian, Equifax), RBI CIMS, RBI DAKSH, RBI PRAVAAH, SEBI SI portal / SCORES, Stock exchange listing centre (BSE Listing Centre, NEAPS/NSE), IFSCA SWIT / portals, IRDAI portals (BAP, IIB), NeSL, DGFT, Udyam, State co-operative registrar portals, bank net-banking (**blocked type** — never stored; [REC]), e-mail accounts (**blocked**), other (custom label). Fields: portal, URL (allow-listed domains for the type), username, secret (password/PIN for the portal account — not OTP seeds), 2FA method note (OTP to whom — the device stays with the client), owner person, purpose, rotation period, last rotated, expiry, linked obligations/returns, grantees.
- **FR-P22-19 — RBI portal default.** Entries of type RBI CIMS/DAKSH/PRAVAAH are `CLIENT_ONLY` by default: they can be stored for the client's own users but cannot be granted to delivery staff unless the client admin ticks an unticked acknowledgement: "RBI portal user IDs are issued to our named officers; sharing them with a service provider may breach the portal terms and our IT/outsourcing obligations. We confirm our policy permits this and we accept responsibility." The acknowledgement is stored with the grant and highlighted in the reveal log [INTERP; VERIFY portal terms]. Same default for CIC member portals and FIU-IND.
- **FR-P22-20 — Per-credential grants.** Client admin grants a named delivery user (or client user) `REVEAL` or `USE_VIA_HELPER` for a period ≤ grant validity; grants are listed in the delivery console Credentials tab as "available to you" without showing the secret.
- **FR-P22-21 — Reveal flow.** Request → step-up MFA (FIDO2) → purpose selection (linked task/obligation/return) → secret shown for 30 seconds (copy-to-clipboard clears after 30 s; no screenshot prevention claims) → reveal logged (`CredentialRevealed` with staff, purpose, time, IP, device) → client admin and vault custodian notified (immediate or daily digest per tenant setting; RBI/CIC types always immediate). Optional dual control per entry: a second client user must approve each reveal (`require_client_approval_per_reveal`).
- **FR-P22-22 — Rotation.** Rotation reminders per entry; after any delivery staff member's grant ends, the vault prompts the client to rotate credentials they had revealed (list generated automatically) — "Rotate now" opens the portal URL; the client (or a granted RM, if allowed) records the new secret; rotation events logged. Delivery users who rotate a password on the client's behalf (R-073 "our team will also change passwords") must record it in the vault within the same session (task auto-created and tracked).
- **FR-P22-23 — No export, no bulk.** No bulk reveal, no export of secrets (P19 exports include only metadata: portal, username masked, owner, rotation dates); secrets excluded from search, AI context (NN-14) and logs (NN-32); clipboard events not logged in plain text.
- **FR-P22-24 — Anomaly detection.** Alerts to `plt_security_officer` and the client admin for: > 5 reveals per staff per hour, reveals outside 08:00–21:00 IST, reveal from new device/country, reveal without a linked active task; automatic suspension of the staff member's vault access on high-severity anomaly pending review.

### 4E. Messages, meetings and e-mail

- **FR-P22-25 — Secure messaging.** Per client: channels "General", per engagement/retainer, and per-topic threads; participants = assigned delivery team + client users invited by the client admin; mentions, attachments (DMS-backed, scanned), read receipts, message search; retention per tenant setting; messages are tenant data stored in the tenant (India region); the delivery console reads them through the tenant API.
- **FR-P22-26 — E-mail bridge.** Optional: each client channel gets an inbound address (`<client-code>.<channel>@deliver.lawdocscomply.com`); e-mails from allow-listed client domains are posted to the thread (attachments to DMS); outbound replies are sent from the delivery user's M365 mailbox via Graph (WORKSPACE_PORT) or from the platform mailer with "on behalf of" — choice `sdc.email.outbound_mode` (G). No mailbox scraping (OH3.1).
- **FR-P22-27 — Meetings.** "Schedule meeting" creates a Teams (or Google Meet) meeting through the delivery user's workspace account, invites client contacts, attaches agenda from the thread; minutes/notes saved to the client DMS (if the meeting is a board/committee meeting supported by the RM, P06 owns minutes workflow).
- **FR-P22-28 — Client portal parity.** Client users see the same threads in the tenant app (Messages › LawDocs team) and get notifications per their preferences (Notifications, NN-27).

### 4F. Files, shared drives and deliverables

- **FR-P22-29 — Shared drive link.** Per client, the RM can register a shared location: (a) LDC DMS folder "Shared with LawDocs" (default; inside the tenant), (b) client's SharePoint/OneDrive folder or Google Drive folder (via WORKSPACE_PORT with the **client's** consent and delegated access, or as a simple link if the client prefers), (c) LawDocs' SharePoint site for the client (owned by LawDocs' M365 tenant — for working drafts only). The registered location appears on both sides; opening external links happens in the browser (M365/Google authentication applies).
- **FR-P22-30 — Single source of truth for deliverables.** Final deliverables are always filed in the client's LDC DMS (with version, hash, deliverable id and engagement reference) even when drafted in SharePoint/Drive; the file is opened in Office for the web / desktop (DOCX/XLSX/PPTX native, PDF) — no proprietary formats (R-043); export follows Appendix M (`Services & Engagements/...`).
- **FR-P22-31 — Deliverables register.** Type (policy draft, minutes draft, return package, agenda, annual report draft, ICAAP draft, register update, filing acknowledgement, training material, report), status (`DRAFT → IN_REVIEW (dlv_reviewer) → RELEASED → ACCEPTED_BY_CLIENT | RETURNED`), due date, SLA link, client owner, linked tenant record (e.g., the policy version in P07, the return package in P11). Release requires reviewer approval (quality gate; reviewer ≠ author).
- **FR-P22-32 — Bulk delivery.** Upload a folder (e.g., 12 policies) with mapping preview to tenant targets (policy register entries, obligation evidence) — uses P19 folder intake rules; nothing overwrites an approved client record; each item becomes a draft for the client checker.

### 4G. Billing and commercial view

- **FR-P22-33 — Read-only billing.** Plan, components, renewal date, auto-renew state, invoices list with status (paid/overdue/disputed), dunning stage, retainer hours/deliverables vs plan, service credits — from P20 mirror/OH8 APIs; the same data the client sees in Settings › Billing, filtered to non-sensitive fields (no payment-method details).
- **FR-P22-34 — Upsell and renewal proposals.** RM can draft a quote (OH8 product quote via BILLING_PORT) for components, seats or services and send it to the client admin, who accepts in Settings › Billing (P20 flow). RM never applies changes; discounts beyond the RM's DoA route to OH8 approval. The quote shows the RM's name; no pressure tactics (renewal guard-rails, OH5.3).
- **FR-P22-35 — Trial extensions** within the delivery lead's limit (P20 FR-P20-26), reason-coded.
- **FR-P22-36 — Master-data change requests (R-074).** RM can raise "Request change to client details" (legal name, address, constitution, regulator registration, group structure, GSTIN) with evidence; it goes to `plt_super_admin` in `apps/console`, who applies it through a Correction Entry (maker-checker; D-02) with the client admin notified; the console never edits directly.

### 4H. SLA tracker, health and reports

- **FR-P22-37 — SLA tracker.** Per client: SLA metrics from the retainer (P21), live clocks, breaches, credits; per RM: SLA attainment across portfolio; alerts at 50% and 75% of clock.
- **FR-P22-38 — Delivery health score (LDC-internal view).** Distinct from the OH2.3 customer health score, which remains OH's system-of-record metric for customer success. Components (configurable weights, G): product adoption (active users/seats, modules used — aggregates), compliance hygiene (on-time %, overdue high-risk count — **only if the client allows**, and never sent to OH), service experience (SLA attainment, ticket CSAT, unresolved complaints), commercial (invoice status, renewal proximity), relationship (last meeting, last client login, survey NPS). LDC sends OH5 only the inputs OH2.3 uses — adoption aggregates (active users ÷ entitled seats, modules in use ÷ licensed) and delivery status (open change requests, SLA breaches) — as `ClientHealthSignal` (Appendix X §X.5); compliance-hygiene components stay inside LDC (OH Part 4.5).
- **FR-P22-39 — Reports.** Monthly service report (from P21), QBR pack (adoption, value from Savings Dashboard if the client allows `bil.savings.share_with_rm`, SLA, upcoming regulatory changes affecting the client — Updates titles only), portfolio report for `dlv_lead` (utilisation from OH11, SLA, health distribution, renewals pipeline).

### 4I. Operations Hub interfaces (D-03)

- **FR-P22-40 — Tickets.** "Raise ticket for client" in the console and "Contact support" in the tenant create OH6 tickets via `POST /v1/support/tickets` with product-signed token, category, severity, `regulatory_impact` (if a statutory deadline is at risk, with date), deep link; attachments only after PII scan/redaction (Ecosystem Spec §6.29); ticket status (`SupportTicketOpened/Resolved`) shown in the client section and the tenant's Help › My tickets.
- **FR-P22-41 — CRM.** Meeting notes flagged "commercial" (not compliance content) and client contact role changes sync to OH3 as activities/contacts through `POST /v1/crm/requests` or the CRM activity API (Appendix X §X.2 new endpoint); compliance discussions never go to CRM (OH Part 4.5).
- **FR-P22-42 — Customer success.** `ClientHealthSignal` (daily aggregate), renewal-risk flags raised by RM, QBR completion, survey triggers — to OH5.
- **FR-P22-43 — Timesheets and utilisation.** Time entries (P21 `mkp.time_entries` and non-engagement delivery time) aggregated per staff per day per client per category → OH4 `timesheet_entry` / OH11 utilisation (Appendix X §X.10); staff see their own entries; no keystroke or screen monitoring (NN-25).
- **FR-P22-44 — Onboarding.** For sales-led tenants, OH4 provisioning → LDC tenant → RM assignment from OH4 project team; implementation milestones accepted in LDC by the client (`ImplementationMilestoneReached` back to OH4) where the client acceptance happens in-product.
- **FR-P22-45 — Billing events.** Consumed from OH8 for display (FR-P22-33).
- **FR-P22-46 — No content egress.** A contract test (`NN-23_no_compliance_content_to_oh`) asserts that no event/API payload from LDC to OH contains obligation text, evidence, documents, credentials, messages bodies, risk data or personal data of client customers; only ids, counts, states and commercial metadata.

### 4J. Cross-company and group work (R-047)

- **FR-P22-47 — One identity, many products.** A staff member who serves Finbyx or Udofin clients as well holds separate product roles; the delivery console shows a product switcher with deep links to Finbyx/Udofin/Equator consoles (each with its own authentication and logging); no Finbyx/Udofin/Equator data is displayed inside the LDC console.
- **FR-P22-48 — Equator separation.** Staff holding any Equator case-level role (case manager, panel administrator, neutral) cannot hold a delivery grant in an LDC tenant of a lender that has matters with Equator, and vice versa, per OH1.6 separation rule (check via `POST /v1/conflicts/check` with counterparty org) [Integration Spec §8.6].
- **FR-P22-49 — Client authorisation for group cross-sell.** The delivery console never shows "sell Finbyx/Udofin" prompts based on compliance weaknesses; cross-group introductions require the client's written authorisation recorded in OH3 (OH Part 4.5).

### 4K. Productivity and anti-fraud controls

- **FR-P22-50 — Output-based measurement.** Per staff: tasks completed, SLA attainment, deliverables released and accepted first time, client CSAT, rework rate, hours logged vs plan; visible to the staff member and their manager; feeds OH11/OH10 appraisal as metrics (no automated people decisions — OH Part 1).
- **FR-P22-51 — SoD.** Delivery author ≠ reviewer; RM cannot approve own quote discounts; a staff member cannot both reveal a credential and approve its rotation record (client approves); no delivery user can delete messages or files (retention; Correction Entries for errors).
- **FR-P22-52 — Access reviews.** Quarterly review of all delivery grants and credential grants by `dlv_lead` + client attestation request (client admin confirms or revokes); grants not attested within 14 days are suspended (OH3.3 pattern); evidence to Appendix Q control library.
- **FR-P22-53 — Leaver and mover.** On OH `EmployeeOffboarded` or role change: grants suspended within 15 min, vault rotation prompts generated for every credential the person revealed in the last 180 days, open tasks reassigned, client admins notified.

---

## 5. Workflows and state machines

### 5.1 Delivery grant

```
PROPOSED (by dlv_rm/dlv_lead, scope from retainer) ──(client admin, step-up MFA)──▶ ACTIVE
  │                └─(client admin)─▶ DENIED (reason)                                    │
  └─(client admin creates directly)──────────────────────────────────────────────────▶ ACTIVE
ACTIVE ─(T-14)─▶ EXPIRING ─(client admin)─▶ RENEWED(=ACTIVE, new version) | EXPIRED
ACTIVE ─(leaver | security alert | retainer suspended | client action)─▶ SUSPENDED ─▶ ACTIVE | REVOKED
ACTIVE ─(client admin | super admin emergency)─▶ REVOKED (sessions killed ≤ 60 s)
Guards: grantee role ∈ {dlv_maker}; checker(s) bound; sealed classes excluded unless client explicitly includes; valid_to ≤ policy max.
```

### 5.2 Credential reveal

```
REQUESTED (grantee; purpose + linked task) → STEP_UP (FIDO2) → [CLIENT_APPROVAL if per-reveal dual control] → REVEALED (30 s)
  → LOGGED (CredentialRevealed) → NOTIFIED (client admin/custodian) → [ROTATION_PROMPT after grant end]
Denied paths: no active grant | RBI/CIC type without acknowledgement | anomaly lock | outside allowed hours (if configured).
```

### 5.3 Deliverable

```
DRAFT (author) → IN_REVIEW (dlv_reviewer ≠ author) → RELEASED (filed in tenant DMS, client notified)
  → ACCEPTED_BY_CLIENT (checker/owner) | RETURNED (comments) → DRAFT (new version)
Linked tenant record (policy version / return package / minutes) follows its own module workflow (P07/P11/P06); the deliverable record mirrors its state.
```

### 5.4 Master-data change request (R-074)

```
RAISED (dlv_rm, evidence) → TRIAGED (plt_super_admin) → APPLIED as Correction Entry (maker ≠ checker, client admin notified) | REJECTED (reason)
```

### 5.5 Reassignment

```
INITIATED (dlv_lead) → HANDOVER_NOTE (outgoing RM) → NEW_GRANT_PROPOSED (client admin approves) → OLD_GRANT_REVOKED → TASKS_REASSIGNED → CLIENT_NOTIFIED
```

---

## 6. Screens and UX (`apps/delivery`)

| Screen ID | Name | Menu path | Roles |
|---|---|---|---|
| SCR-SDC-01 | Portfolio home | Home | all delivery |
| SCR-SDC-02 | Work Inbox (cross-tenant, federated) | Home › My work | all delivery |
| SCR-SDC-03 | Client list | Clients | all delivery (scoped) |
| SCR-SDC-04 | Client › Overview | Clients › {client} | assigned |
| SCR-SDC-05 | Client › Work | Clients › {client} › Work | assigned |
| SCR-SDC-06 | Client › Calendar | … › Calendar | assigned |
| SCR-SDC-07 | Client › Act in tenant (launcher + grant details) | … › Act in tenant | grantees |
| SCR-SDC-08 | Client › Credentials (available to me; request; reveal) | … › Credentials | grantees |
| SCR-SDC-09 | Client › Messages | … › Messages | assigned |
| SCR-SDC-10 | Client › Files & drive | … › Files | assigned |
| SCR-SDC-11 | Client › Deliverables | … › Deliverables | assigned |
| SCR-SDC-12 | Client › Billing (read-only) & proposals | … › Billing | assigned |
| SCR-SDC-13 | Client › SLA & reports | … › SLA | assigned |
| SCR-SDC-14 | Client › Health | … › Health | assigned, `dlv_lead` |
| SCR-SDC-15 | Client › Notes | … › Notes | assigned |
| SCR-SDC-16 | Client › Activity | … › Activity | assigned, `dlv_lead` |
| SCR-SDC-17 | Grants board (all grants, expiring, pending) | Access › Grants | `dlv_lead`, RM (own) |
| SCR-SDC-18 | Access review | Access › Reviews | `dlv_lead` |
| SCR-SDC-19 | Engagements pipeline (P21) | Marketplace › Engagements | delivery |
| SCR-SDC-20 | Offering studio (P21) | Marketplace › Offerings | `dlv_lead` |
| SCR-SDC-21 | Team & assignments | Team | `dlv_lead` |
| SCR-SDC-22 | My time | Me › Time | all delivery |
| SCR-SDC-23 | My metrics | Me › Performance | all delivery |
| SCR-SDC-24 | Portfolio reports | Reports | `dlv_lead` |
| SCR-SDC-25 | Product switcher (deep links to Finbyx/Udofin/Equator/OH) | top bar | per roles |

Tenant-side screens (built here, mounted in `apps/web`): SCR-SDC-30 Settings › Delivery team (assigned team, grants, approve/deny/revoke, checkers, visibility settings), SCR-SDC-31 Settings › Credential Vault (entries, grants, reveal log, rotation), SCR-SDC-32 Messages › LawDocs team, SCR-SDC-33 Delivery activity log, SCR-SDC-34 Approve delivery grant (mobile-friendly approval page with step-up).

UX: the tenant banner during a delivery session is non-dismissable and colour + text (not colour alone — WCAG); `Ctrl/Cmd+K` palette searches clients and deliverables within the user's scope; keyboard shortcuts on Work Inbox (`J/K`, `O` open, `R` remind client); empty states explain how grants work ("You do not have maker access to this client yet — propose a grant").

---

## 7. Backend design

### 7.1 Modules: `sdc` (owner), `iam` (grants, realm `ldc-staff`, step-up), `core` (audit, break-glass), `wf` (tasks, notifications, calendar), `dms` (files, deliverables), `mkp` (engagements, retainers, time), `bil` (billing view, quotes), `int` (OH events/APIs, WORKSPACE_PORT), `rpt` (health, reports).

### 7.2 Tables

| Table | Key columns |
|---|---|
| `sdc.staff` (projection) | staff_id, legal_entity_id, job_role, practice, manager_id, status, scim_id, updated_at |
| `sdc.assignments` | id, tenant_id/buyer_org_id, staff_id, role, refs[], start_at, end_at, capacity_points |
| `iam.delivery_grants` (tenant RLS) | id, tenant_id, staff_id, role, scope jsonb, actions[], data_class_max, purpose, basis_ref, checkers jsonb, valid_from, valid_to, state, proposed_by, approved_by, approved_at, version |
| `sdc.sessions` | id, tenant_id, staff_id, grant_id, started_at, ended_at, ip, device_hash, reason |
| `sdc.cred_entries` (tenant RLS, sealed) | id, tenant_id, type, portal_url, username_enc, secret_enc (envelope), owner_user_id, custodian_ids, client_only bool, ack_ref, rotation_days, last_rotated_at, expires_at, linked_refs[] |
| `sdc.cred_grants` | entry_id, grantee (staff_id or user_id), mode (REVEAL, USE_VIA_HELPER), valid_from, valid_to, granted_by, per_reveal_approval bool |
| `sdc.cred_reveals` (append-only) | entry_id, grantee, purpose_ref, approved_by, revealed_at, ip, device_hash, anomaly_flags |
| `sdc.threads`, `sdc.messages` (tenant RLS) | thread scope, participants; message body (encrypted), attachments→dms, read receipts |
| `sdc.drive_links` | tenant_id, kind (DMS, SHAREPOINT, ONEDRIVE, GDRIVE, LAWDOCS_SHAREPOINT), url, delegated_consent_ref, registered_by |
| `sdc.deliverables` | id, tenant_id, engagement_ref, type, title, version, dms_file_id, hash, status, author, reviewer, released_at, client_decision, linked_record_ref |
| `sdc.change_requests_masterdata` | tenant_id, field, current, proposed, evidence_file_id, state, applied_correction_id |
| `sdc.health_snapshots` | tenant_id, date, score, components jsonb, definition_version |
| `sdc.notes` | tenant_id, author, body (encrypted), visibility, created_at |

### 7.3 APIs (selected)

`GET /v1/delivery/portfolio`, `GET /v1/delivery/inbox` (federated), `GET /v1/delivery/clients/{tenant}/overview`, `POST /v1/delivery/clients/{tenant}/grants` (propose), `POST /v1/tenant/delivery-grants/{id}/approve|deny|revoke|renew` (tenant side), `POST /v1/delivery/sessions` (start act-in-tenant; returns tenant-scoped token with `act = delivery` claim), `GET /v1/delivery/clients/{tenant}/credentials` (metadata), `POST /v1/delivery/credentials/{id}/reveal` (step-up), `POST /v1/tenant/credentials` (client CRUD), `POST /v1/delivery/clients/{tenant}/messages`, `POST /v1/delivery/clients/{tenant}/deliverables`, `POST /v1/delivery/deliverables/{id}/review|release`, `POST /v1/delivery/clients/{tenant}/masterdata-requests`, `POST /v1/delivery/clients/{tenant}/quotes` (BILLING_PORT), `GET /v1/delivery/clients/{tenant}/billing`, `POST /v1/delivery/time-entries`.

### 7.4 Domain events

`DeliveryGrantProposed`, `DeliveryGrantActivated`, `DeliveryGrantRenewed`, `DeliveryGrantSuspended`, `DeliveryGrantRevoked`, `DeliverySessionStarted/Ended`, `CredentialEntryCreated`, `CredentialGrantChanged`, `CredentialRevealed` (sealed payload; tenant-only), `CredentialRotationPrompted`, `CredentialRotated`, `DeliverableReleased`, `DeliverableAccepted/Returned`, `MasterDataChangeRequested/Applied`, `ClientHealthSignal` (→ OH5, aggregate), `TimesheetAggregated` (→ OH4/OH11), `SupportTicketRequested` (→ OH6 API). Consumed: `EmployeeOnboarded/Offboarded`, role changes (OH10/OH1), `SupportTicketOpened/Resolved`, `InvoiceIssued`, `SubscriptionPaymentFailed`, `PlanChanged`, `RetainerActivated/Ended` (P21).

### 7.5 Jobs

`GrantExpiryWorkflow` (T-14 notices, expiry), `LeaverSweep` (≤ 15 min on event; hourly reconciliation with SCIM), `VaultRotationPromptJob`, `RevealAnomalyDetector` (streaming), `AccessReviewCampaign` (quarterly), `HealthSnapshotJob` (daily 04:00 IST), `TimesheetAggregationJob` (daily), `FederatedInboxIndexer` (per-tenant index of tasks assigned to delivery staff, tenant-partitioned).

---

## 8. Integrations

| Port / API | Counterparty | Notes |
|---|---|---|
| SCIM 2.0 + OIDC | Group IdP (OH1/OH10) | Staff provisioning to `ldc-staff` realm |
| `POST /v1/support/tickets`; `SupportTicketOpened/Resolved` | OH6 | Ecosystem Spec §6.29 |
| `POST /v1/crm/requests`; CRM activity API (new, Appendix X §X.2) | OH3 | Commercial metadata only |
| `ClientHealthSignal` (new event, Appendix X §X.5) | OH5 | Aggregates |
| `TimesheetAggregated` (new event, Appendix X §X.10) | OH4/OH11 | Per staff/day/client/category hours |
| `ImplementationMilestoneReached` | OH4 | Milestone acceptance in-product |
| `BILLING_PORT` | OH8 | Quotes, invoices view |
| `POST /v1/conflicts/check` | OH1.6 | Equator separation |
| `WORKSPACE_PORT` (Graph / Google APIs) | M365 / Google Workspace | Calendar sync (title only), Teams/Meet, SharePoint/OneDrive/Drive links, outbound mail via user mailbox |
| `DMS_PORT` | P07 | Files, deliverables |
| `ESIGN_PORT` | ESPs | Engagement amendments where needed |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `sdc.rm.max_clients` | G | 25 | 5–60 | `dlv_lead` + checker |
| `sdc.grants.max_months.retainer` | G | 12 | 1–12 | `plt_super_admin` |
| `sdc.grants.max_months.implementation` | G | 3 | 1–6 | `plt_super_admin` |
| `sdc.grants.support_session_max_hours` | L | 8 | — | — |
| `sdc.grants.expiry_notice_days` | G | 14 | 7–30 | `plt_super_admin` |
| `sdc.grants.alternate_approvers` | T | none | client users with admin/CCO | `ten_admin` |
| `sdc.grants.include_sealed_classes` | T | false | — | `ten_admin` (step-up, per grant) |
| `sdc.session.idle_timeout_min` | G | 30 | 10–60 | `plt_security_officer` |
| `sdc.vault.reveal_seconds` | G | 30 | 10–60 | `plt_security_officer` |
| `sdc.vault.client_only_types` | G | RBI_CIMS, RBI_DAKSH, RBI_PRAVAAH, CIC_*, FIU_IND | add-only | `plt_security_officer` |
| `sdc.vault.blocked_types` | L | NET_BANKING, EMAIL, DSC_PIN, OTP_SEED | — | — |
| `sdc.vault.reveal_notify_mode` | T | IMMEDIATE | IMMEDIATE, DAILY_DIGEST (not for client-only types) | `ten_admin` |
| `sdc.vault.allowed_hours` | T | none | e.g., 08:00–21:00 | `ten_admin` |
| `sdc.vault.per_reveal_client_approval` | T | false | per entry | `ten_admin` |
| `sdc.vault.anomaly_threshold_per_hour` | G | 5 | 2–20 | `plt_security_officer` |
| `sdc.client_visibility.compliance_metrics` | T | [on_time_pct, overdue_count, high_risk_overdue, due_30d] | subset | `ten_admin` |
| `sdc.notes.client_visible` | T | false | — | `ten_admin` |
| `sdc.calendar.sync_detail_level` | G | TITLE_ONLY | NONE, TITLE_ONLY, TITLE_AND_LINK | `plt_security_officer` |
| `sdc.email.outbound_mode` | G | USER_MAILBOX | USER_MAILBOX, PLATFORM_ON_BEHALF | `plt_super_admin` |
| `sdc.health.weights` | G | adoption 25, hygiene 25, service 25, commercial 15, relationship 10 | sum 100 | `dlv_lead` + checker |
| `sdc.access_review.cadence_months` | G | 3 | 1–6 | `plt_security_officer` |

---

## 10. Security, privacy and audit

- **Phishing-resistant MFA** for all delivery staff; step-up for grants, reveals, releases, quotes; device posture check optional (managed device required for vault reveals — `sdc.vault.require_managed_device`, G, default true if Intune/MDM integration available [VERIFY OH12]).
- **Vault crypto**: envelope encryption with per-tenant DEKs wrapped by KMS CMKs (AWS KMS ap-south-1); secrets decrypted only in the reveal service, never cached, never logged; HSM-backed keys for Enterprise (CloudHSM) optional; memory zeroisation best-effort; secrets excluded from backups' logical exports (backups encrypted; restores re-wrap) — Appendix Q.
- **Audit**: all delivery actions with `actor_type = DELIVERY` and grant id (NN-02); client-visible logs; Correction Entries for errors (D-02); BSA 2023 s.63 certificate in exports of delivery logs where needed (NN-09).
- **DPDP**: LawDocs acts as processor for the client's data handled in delivery; staff confidentiality undertakings (OH10); client notices describe delivery access; messages and notes subject to access/correction requests via the tenant.
- **Data egress**: no compliance content to OH (FR-P22-46); calendar sync minimises detail; e-mail bridge allow-lists domains; DLP scans for credentials and Aadhaar/PAN patterns in messages and notes (warn or block per type).
- **RE outsourcing**: for RBI REs the delivery service is an outsourced activity supporting (not replacing) core management functions; the grant UI shows the RE notice (P21 FR-P21-13) and the tenant's outsourcing register (P12 TPRM) gets an auto-entry for LawDocs delivery with the grant scope.

---

## 11. AI touchpoints and guardrails

- **Client brief** (Vidhi): summarises a client's status for the RM before a meeting from data the RM may see (tasks, deadlines in scope, open items, recent messages) — tenant-scoped retrieval under the grant; no credentials, no sealed classes (NN-13/NN-14).
- **Message drafting**: drafts replies and reminders; RM sends.
- **Deliverable QA** (shared with P21): citation and template checks before reviewer step.
- **Health insight**: explains health-score changes from components; never predicts churn as a fact; never suggests cross-group sales (FR-P22-49).
- All AI runs within the tenant's AI credit budget only when acting inside the tenant session on the client's request; delivery-internal AI (portfolio summaries) is charged to LawDocs' internal budget.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p22/*.feature`)

```gherkin
Feature: Delivery grants
  Scenario: LawDocs proposes, client approves
    Given an active retainer for tenant T with scope "Returns & Reporting"
    When RM R proposes a maker grant for that scope
    Then the tenant admin receives a mandatory approval notification
    And after the admin approves with step-up MFA the grant is ACTIVE with the named checker
    And R can submit return packages only to the named checker

  Scenario: Delivery user can never be a checker
    Given a delivery grant for RM R
    When anyone tries to add R as a checker or approver in tenant T
    Then the change is refused with LDC-SDC-007

  Scenario: Super admin cannot approve on the client's behalf
    When a super admin attempts to approve a proposed delivery grant for tenant T
    Then the API returns 403 LDC-SDC-008

  Scenario: Leaver handling
    Given RM R holds grants in 3 tenants and revealed 2 credentials last month
    When OH emits EmployeeOffboarded for R
    Then within 15 minutes all R's grants are SUSPENDED and active sessions end
    And the 2 tenants' vaults show rotation prompts for the revealed credentials

Feature: Credential vault
  Scenario: RBI CIMS credential is client-only by default
    Given a vault entry of type RBI_CIMS
    When the client admin tries to grant it to RM R without ticking the acknowledgement
    Then the grant is refused with LDC-SDC-012

  Scenario: Reveal is logged and notified
    Given RM R has a REVEAL grant on the GST portal entry
    When R reveals it with step-up MFA linked to task "GSTR-3B Oct 2026"
    Then the secret is visible for 30 seconds
    And CredentialRevealed is written to the ledger and the client admin is notified immediately

  Scenario: No bulk export of secrets
    When any user requests a full tenant export
    Then the export contains vault metadata with masked usernames and no secrets

Feature: OH interface hygiene
  Scenario: No compliance content to the Hub
    Given the contract test corpus of all LDC→OH payloads
    Then none contains obligation text, evidence, document content, message bodies, credentials or customer personal data

Feature: Deliverables
  Scenario: Reviewer must differ from author
    Given professional P authored a policy draft deliverable
    When P tries to release it
    Then release is refused until a different dlv_reviewer approves

  Scenario: Final deliverable lands in the client DMS
    Given a released deliverable drafted in SharePoint
    Then a version with hash and engagement reference exists in tenant T's DMS
    And it is included in tenant T's LDC-EXPORT-1.0 under Services & Engagements

Feature: Master data change
  Scenario: RM requests a registered-address change
    When RM R raises a master-data change request with evidence
    Then it appears in the super admin queue and is applied only as a Correction Entry approved by a second super admin
    And the client admin is notified with old and new values
```

NN tests: `NN-01_delivery_federated_inbox_isolation`, `NN-02_delivery_actions_ledger`, `NN-05_delivery_never_checker`, `NN-13_vault_sealed`, `NN-14_vault_excluded_from_ai`, `NN-17_credential_vault_rules`, `NN-23_no_compliance_content_to_oh`, `NN-25_no_covert_monitoring`, `NN-30_delivery_access_only_by_grant`, `NN-32_no_secrets_in_logs`.

---

## 13. Deliverables and exit gate

- `apps/delivery` with SCR-SDC-01…25, tenant-side SCR-SDC-30…34, grant engine extension, act-in-tenant sessions, credential vault (with security review and pen-test of the reveal service), messaging and e-mail bridge, drive links, deliverables register, SLA/health/report views, OH integrations (tickets, CRM, CS signals, timesheets, milestones) contract-tested against OH sandbox, runbooks (leaver sweep, vault anomaly response, emergency revocation).
- **Exit gate:** §12 scenarios and NN tests green; external penetration test of vault and session token exchange with no high findings open; legal sign-off on delivery terms, RE notice and RBI-portal acknowledgement wording; OH addendum (Appendix X) items X.2, X.5, X.10 implemented in OH or stubbed with fallbacks recorded.

---

## 14. Open items and verification flags

| ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P22-01 | RBI CIMS/DAKSH/PRAVAAH, CIC and FIU-IND portal terms on credential sharing with service providers | Not verified | Counsel / client compliance | Client-only default + acknowledgement |
| OI-P22-02 | Group IdP and SCIM source (OH1 or Entra ID/M365) | Depends on OH build and M365 SKU (D-10) | CTO | Manual staff provisioning with maker-checker until SCIM |
| OI-P22-03 | Managed-device enforcement (Intune) availability under the M365 plan held | Business Basic lacks Intune [VERIFY] | CTO | Device registration + risk-based step-up |
| OI-P22-04 | E-mail bridge domain and DMARC alignment for `deliver.lawdocscomply.com` | Infra | CTO | In-app messaging only |
| OI-P22-05 | Whether LawDocs staff who are advocates/CAs may sign deliverables in their professional capacity while employed by a company | Professional rules | Counsel | Deliverables issued by LawDocs as company work product; no professional seal |
| OI-P22-06 | Outsourcing-register auto-entry content for RE tenants | Align with P12 TPRM | S6 | Manual entry prompt |

---

## 15. Sources (accessed 25 October 2026)

1. Infrabyx Operations Hub Master Prompt v1.0 — Part 2.2–2.4 (Hub scope, never-holds), Part 3.2–3.5 (workspaces, grants, navigation), Part 4.5 (LawDocsComply client confidentiality), OH1.6 (Equator conflict service), OH3–OH6, OH10–OH12.
2. Infrabyx Ecosystem Integration Specification v1.1 — §4.6 (group identity, grants ≤ 90 days), §4.7 (external access), §6.27, §6.29, §8.6 (Equator separation).
3. RBI (Rural Co-operative Banks – Managing Risks in Outsourcing) Directions 2025, RBI/DOR/2025-26/318, para 11 (core management functions) — https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12986 ; NBFC/bank equivalents [VERIFY].
4. Digital Personal Data Protection Act 2023 and DPDP Rules 2025 (processor duties, notices) — MeitY [VERIFY phased dates via S6].
5. NIST SP 800-63B (authenticator assurance; phishing-resistant MFA) and OWASP ASVS 5.0 (V6 authentication, V8 data protection) — design references.

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-17, NN-43; X-02, X-17**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

