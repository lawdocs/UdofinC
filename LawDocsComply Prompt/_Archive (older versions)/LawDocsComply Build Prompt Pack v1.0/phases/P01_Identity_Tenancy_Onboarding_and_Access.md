# Phase P01 — Identity, Tenancy, Onboarding and Access

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (tenancy, RLS, session context, audit ledger, Correction Entries, break-glass schema, `cfg` heads, flags, evidence ingest, provisioning workflow).
>
> **Sequencing:** P01 follows P00. P02 (Configuration Studio) starts in P01 sprint 2 and consumes the settings P01 registers. P20 (pricing, subscriptions) and P23 (public site, health check) extend the onboarding funnel built here: P01 delivers the funnel's identity, KYB, tenant creation, trial and module-selection mechanics with a price-computation call to a stub of the P20 pricing service (`bil.quote`) that returns catalogue seed values until P20 is live. Migration wave 2 (tenants, users, compliance records) executes at the P01 exit (P00 FR-P00-57).
>
> **Binding appendices:** D (roles, personas and access-control matrix — owned by stream S12; this phase implements its enforcement), A (user, invitation, grant, delegation, break-glass, regulator-view state machines), B (identity tables), Q (authentication and session controls), U (settings), N (plans, trial rules — pricing data), L (KYB/KYC adapters — S8), C (dashboards per role — S12).
>
> **Requirements covered:** R-018, R-025, R-029, R-030, R-031, R-056 (user ↔ HRMS link foundation), R-057, R-069, R-072 (delivery users acting in a tenant), R-074, R-083, R-016 (health-check-to-trial hand-off), R-034 (trial).
>
> **Decisions applied:** D-02, D-03, D-04 (vault access step-up), D-10, D-12, D-14, D-15, D-21.
>
> **Estimated effort:** 5 two-week sprints, squad of 8 (identity engineer, 2 backend, 2 frontend, 1 integration engineer for KYB adapters, 1 QA, 1 UX writer/designer).

---

## 1. Objective and business outcome

LawDocsComply serves people with very different stakes: a platform super admin who can correct anything; a LawDocs relationship manager who works inside a client's tenant as a maker; a client company admin who configures the product; makers, checkers and department heads who do daily compliance work; KMPs and directors who need dashboards and approvals; internal, external, secretarial and IS auditors; an RBI or other supervisor who must see records read-only for a limited period; employees who only acknowledge policies; POSH Internal Committee members working on sealed matters; co-operative society office bearers and members; marketplace buyers who never subscribe; and anonymous visitors running the free health check.

P01 gives each of them the right door, the right proof of identity, the right permissions and nothing more — and makes a company's first hour with LawDocsComply fast: enter a PAN or CIN, confirm the auto-filled profile, pick the regulator and entity family, choose modules, see the price, invite the team and reach a first useful result.

| Outcome | Exit-gate measure |
|---|---|
| Fast self-onboarding | A new NBFC (synthetic) goes from health-check report → trial tenant → verified entity profile → modules selected → first five users invited → first compliance calendar visible in ≤ 30 minutes, with ≤ 12 fields typed manually (all others auto-filled or defaulted) |
| Strong authentication | 100% of privileged roles (platform, delivery, `ten_admin`, `ten_cco`, `ten_checker`, KMP, board, auditors, supervisor view, IC, payroll) enforce MFA at onboarding; passkeys available to all; step-up enforced on the actions in §4C |
| Least privilege, server-side | Every API, export, job and AI retrieval call is authorised by Cerbos with role + attributes; UI hiding is never the control; the Appendix D matrix is executable as policy tests (≥ 1 allow and ≥ 1 deny test per matrix row) |
| Delivery staff are visible guests | A LawDocs RM can act as maker in a client tenant only through a client-approved `delivery_grant`; every action shows "LawDocs (RM name)" in the tenant's audit and UI; revocation takes effect within 60 seconds |
| Regulator view is safe | A supervisor grant is created by the tenant (maker-checker), time-boxed ≤ 90 days, read-only at database, gateway and UI layers, watermarked, logged and revocable (D-12; NN-18) |
| No identity over-collection | No Aadhaar number, raw PAN image or bureau report is stored at onboarding; KYB facts carry source and fetched-at; DPDP notice and consent artefacts recorded (NN-12) |
| HRMS-linked users | A user can be created from an HRMS employee record (P13) or directly; either way, a person has one identity across tenants and products where they belong |

---

## 2. Scope (in / out)

**In scope**

- Keycloak realms, clients, themes and custom authenticators; BFF session pattern for all Next.js apps.
- Authentication methods: email + password, email magic link, mobile OTP (SMS/WhatsApp), TOTP, passkeys (WebAuthn), enterprise SSO (Microsoft Entra ID, Google Workspace, any SAML 2.0/OIDC IdP), recovery codes.
- Authentication assurance levels and step-up.
- Persons, users, memberships, role grants, ABAC attributes, delegations, act-as and on-behalf-of (Vidhi).
- Invitations; bulk user import (CSV/XLSX); SCIM 2.0 provisioning; HRMS-driven provisioning hooks (P13 completes).
- Cerbos policy service and the enforcement library (`packages/authz`), plus query-plan filters for list endpoints.
- Delivery grants (LawDocs staff acting in tenants), regulator/supervisor grants, auditor grants, break-glass UI.
- Self-onboarding funnel: entry from health check, pricing or marketplace; account creation; KYB auto-fill; entity profile; regulatory profile and family; module selection with live price; trial start; team invitation; first value.
- Trial lifecycle (7 days default, extendable by super admin per tenant — R-070) and conversion hand-off to P20.
- Multi-entity and group setup (holding, subsidiaries, member societies).
- Account experience: profile, security, sessions, devices, notification-channel preferences (data captured here; P04 notification engine uses it), privacy centre (DPDP rights for the user's own data).
- Platform, delivery and tenant administration screens for users and access.

**Out of scope**

- Configuration Studio and setting packs (P02) — P01 registers its settings and calls the P02 resolver once available (fallback to registry defaults).
- Detailed dashboards (P04 onward; information architecture in Appendix C).
- HRMS employee master and org chart (P13) — P01 provides the `iam.persons` ↔ `hr.employees` link.
- Billing, payment, invoices, plan changes (P20) — P01 calls `bil.quote` and `bil.start_trial` and receives entitlements.
- Credential vault content (P22) — P01 provides the step-up and access-grant primitives it uses.
- Co-operative member self-service portal details (P16) — P01 provides member identity and login.

---

## 3. Personas and permissions touched

| Persona | Role codes (Appendix D) | App | Minimum assurance | Notes |
|---|---|---|---|---|
| Platform super admin | `plt_super_admin` | console | AAL3 for elevation | Overrides only through Correction Entries (D-02) |
| Platform content team | `plt_content_maker`, `plt_content_checker`, `plt_content_publisher` | console | AAL2 | Maker ≠ checker ≠ publisher for base content |
| Platform support, security, finance, auditor | `plt_support`, `plt_security_officer`, `plt_finance`, `plt_auditor` | console | AAL2 (security AAL3) | Support has no standing tenant access (NN-30) |
| LawDocs delivery staff | `dlv_lead`, `dlv_rm`, `dlv_professional`, `dlv_reviewer` | delivery; web (when granted) | AAL2 | Act in tenants only via `delivery_grant` |
| Client company admin | `ten_admin` | web | AAL2 | At least two admins recommended; the last admin cannot be removed |
| Compliance and risk leadership | `ten_cco`, `ten_kmp` (CRO, CCO, CFO, CS, CISO, DPO, GRO…) | web | AAL2 | |
| Makers, checkers, department heads | `ten_maker`, `ten_checker`, `ten_dept_head` | web | AAL1 for viewing; AAL2 for approval and submission (default; tenant may lower makers to AAL1) | |
| Board and committee members | `ten_board_member`, `ten_committee_member` | web (board portal view) | AAL2 | Often external to the company's email domain |
| Auditors | `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor` | web (auditor workspace) | AAL2 | External auditors via time-boxed `audit_grant` |
| Supervisor (regulator) view | `ten_supervisor_view` | web (supervisor workspace) | AAL2, named accounts only | D-12 grant; read-only |
| HR and payroll | `ten_hr_admin`, `ten_payroll_maker`, `ten_payroll_checker` | web | AAL2 | |
| Employees | `ten_employee` | web | AAL1 | Policy acknowledgements, own HR records, POSH complaint channel |
| POSH IC members | `ten_ic_member` | web (sealed workspace) | AAL2, session ≤ 8 h, idle 10 min | Sealed (NN-13) |
| Support agents and GRO | `ten_support_agent`, `ten_kmp:GRO` | web | AAL2 | |
| Co-operative | `coop_office_bearer`, `coop_member`, `coop_returning_officer` | web (society portal) | Office bearers AAL2; members AAL1 | P16 |
| Marketplace | `mkp_provider_admin`, `mkp_professional`, `mkp_buyer` | public/web | Buyers AAL1 (AAL2 for payment-method changes); providers AAL2 | P21 |
| Public | `anon`, `lead` | public | none / email verified | Health check, marketplace browsing |
| Vidhi AI | `svc_vidhi` | — | inherits the human's session | Acts on behalf of a named user only |

---

## 4. Functional requirements

### 4A. Identity architecture

**FR-P01-01 — Keycloak realms and clients (ADR-0003).** Two realms:

- `ldc-staff` — platform and delivery staff (LawDocs/Infrabyx employees). Federated to the group's Microsoft Entra ID (D-10: Microsoft 365 first) as the primary IdP, with Keycloak-local passkeys as the second factor if Entra does not assert phishing-resistant MFA. Clients: `ldc-console`, `ldc-delivery`, `ldc-staff-api`. Staff accounts are provisioned from the Operations Hub staff directory (OH10) via SCIM or an event, and disabled within 60 seconds of offboarding there. No customer can authenticate in this realm.
- `ldc` — every customer-side identity (tenant users, board members, auditors, supervisors, co-operative members, marketplace buyers and providers, health-check leads). Clients: `ldc-web`, `ldc-public`, `ldc-api` (machine clients are created per tenant in P18). Keycloak Organizations (or equivalent) map verified email domains to tenant IdPs.

The application database is authoritative for persons, memberships, roles, attributes, grants and consents; tokens carry identity and authentication context only (`sub`, `acr`, `amr`, `auth_time`, `sid`, `org`, `cnf` where DPoP is used). Web apps use a Next.js backend-for-frontend: Authorization Code + PKCE server-side; tokens kept server-side; the browser holds only an encrypted `__Host-ldc_sess` cookie (HttpOnly, Secure, SameSite=Lax) and a CSRF token for mutations. Login pages are a Keycloakify theme on `auth.lawdocscomply.com` using `packages/ui` tokens and `packages/i18n`, meeting WCAG 2.2 AA including success criterion 3.3.8 (Accessible Authentication — no cognitive function test; paste and password managers allowed; passkeys offered).

**FR-P01-02 — Request context.** Each API call carries a signed context: `ldc_ctx = {tenant_id, membership_id, legal_entity_scope[], act_as_role, delivery_grant_id?, supervisor_grant_id?, audit_grant_id?, on_behalf_of?}` set by the BFF (HMAC over value, request id and a 60-second timestamp). The API validates it against active memberships/grants (Redis cache 60 s, busted on change), sets the P00 session context and asks Cerbos. Missing or invalid context returns `400 LDC-IAM-001` or `403 LDC-IAM-003`. A user with memberships in several tenants (a group CFO, an external auditor of three clients, a LawDocs RM serving twelve clients) switches tenant with the tenant switcher; the switch is audited and the UI shows the active tenant and capacity in the header at all times ("Acting as Maker for Alpha Finance Ltd — via LawDocs retainer").

**FR-P01-03 — Assurance levels.**

| ACR | Achieved by | Used for |
|---|---|---|
| `ldc:aal1` | One factor: password, email magic link, mobile OTP | Viewing own tasks and data; policy acknowledgement; health-check report access |
| `ldc:aal2` | Two factors: password + TOTP; user-verifying passkey; password + OTP (fallback only for non-privileged roles); SSO with IdP-asserted MFA (`amr` contains `mfa`, or `acr` mapped by the tenant's SSO configuration) | All privileged tenant roles; checker approval; submission of returns packages; Board and committee approvals; exports above thresholds; settings changes; payment-method changes |
| `ldc:aal3` | Hardware-bound or synced passkey with user verification from an allow-listed authenticator (AAGUID policy for staff), `auth_time` ≤ 5 minutes | Platform elevation (`plt_super_admin` actions), Correction Entry approval, break-glass, key/BYOK operations, credential-vault reveal of RBI portal entries |

Step-up: the API returns `401 LDC-AUTH-010` with `required_acr` and `max_age`; the client re-runs OIDC with `acr_values` and `max_age`. Step-up defaults (registry; tenant may tighten, never loosen below platform floors): checker approve/reject → AAL2, `auth_time` ≤ 30 min; export of > 1,000 rows or any SPI/HR/SEALED export → AAL2 ≤ 10 min; credential-vault reveal → AAL2 ≤ 5 min (AAL3 for RBI portal entries, D-04); supervisor-grant approval → AAL2 ≤ 10 min; Correction Entry approval → AAL3; bank-detail change (payroll, refunds) → AAL2 + 24-hour cooling-off before first use.

**FR-P01-04 — Passwords, TOTP, passkeys, recovery codes.** Passwords: 12–128 characters, no composition rules, checked against a breached-password list and contextual words (name, company, "lawdocs"); Argon2id in Keycloak. TOTP: RFC 6238, 6 digits, 30 s, ±1 step. Passkeys (WebAuthn Level 2/3): platform and roaming, `userVerification = required`, discoverable credentials preferred, up to 10 per user; promoted as the default second factor ("Sign in with your fingerprint or face"). Recovery codes: 10 single-use, shown once, regenerable at AAL2. SMS OTP is not accepted as the second factor for platform, delivery, `ten_admin`, `ten_cco`, auditors, supervisor view or IC roles (SIM-swap risk) [REC; aligns with NIST SP 800-63B restrictions on PSTN authenticators].

**FR-P01-05 — Mobile OTP and email magic link.** OTP: 6 digits, CSPRNG, stored only as HMAC-SHA-256 with a pepper in Redis, TTL 300 s, 3 attempts per code, resend after 30 s, max 5 sends per number per 30 minutes and 10 per 24 hours, per-IP caps, 30-minute lockout after 3 failures. SMS uses a DLT-registered header and template under TRAI TCCCPR 2018 (as amended) with LawDocsComply's principal-entity registration [VERIFY: entity holding DLT registration]; WhatsApp uses an approved authentication template. Magic link: 256-bit token stored as SHA-256 hash, TTL 15 minutes, single use, bound to the initiating browser (cross-device opening shows a code to type instead).

**FR-P01-06 — Enterprise SSO.** Per tenant, SAML 2.0 (signed assertions, SHA-256, IdP-initiated disabled by default) or OIDC (discovery, PKCE, `email_verified` required). Domain verification by DNS TXT `lawdocscomply-verification=<token>`. "Enforce SSO" makes password/OTP login unavailable for that domain except for two named break-glass admins. JIT provisioning creates a person and membership using the tenant's group→role mapping; unmapped users get no membership. Board members and external auditors usually sit outside the corporate domain and keep local authentication with MFA.

**FR-P01-07 — SCIM 2.0.** `/scim/v2/Users` and `/scim/v2/Groups` (RFC 7643/7644) per tenant with a tenant-scoped bearer token (rotatable, hashed at rest), for Microsoft Entra ID and Google Workspace provisioning (D-10). `active=false` revokes memberships and sessions within 60 seconds. Group membership maps to role grants through the tenant's mapping; SCIM never grants `ten_admin` or sealed roles (those need an in-app grant with maker-checker). Keycloak's SCIM capability is implemented in the application (the `iam` module owns the SCIM endpoints) unless ADR-0003 records a production-grade Keycloak SCIM server extension [VERIFY].

**FR-P01-08 — Sessions.**

| Role class | Idle timeout | Absolute | Concurrent sessions |
|---|---|---|---|
| Employees, co-op members, marketplace buyers, leads | 30 min | 12 h | unlimited (listed) |
| Tenant professionals (maker, checker, dept head, KMP, admin, HR, GRO) | 15 min | 12 h | 5 |
| Board, committee, auditors, supervisor view | 15 min | 8 h | 3 |
| IC members (sealed) | 10 min | 8 h | 2 |
| Platform and delivery staff | 15 min | 10 h | 3 |

Access tokens 10 minutes, audience-scoped; refresh tokens rotating with reuse detection (a replayed refresh token revokes the family and alerts the user). Revocation on password change, factor removal, role/membership/grant revocation, tenant suspension, SCIM deactivation, staff offboarding in OH, "sign out everywhere". Sessions listed in SCR-IAM-22 with device, city-level location (from IP; IP stored as HMAC) and last active.

**FR-P01-09 — Account recovery.** Tenant users: recovery code or second factor; else tenant-admin-initiated reset (two admins required to reset an admin); SSO users follow their IdP. Board members and auditors: recovery via the tenant admin with identity re-verification (video call recorded as an event, not stored by default). Staff: per OH10 and the staff realm runbook. Contact-point changes need OTP to old and new contact or the recovery path; a 72-hour hold applies to the email of `ten_admin` accounts with notice to all admins.

### 4B. People, memberships, roles and attributes

**FR-P01-10 — Person and user model.** `iam.persons` (one real person; `id` `per_`; name, preferred name, contact points with verification state, preferred language, accessibility preferences — screen-reader mode, reduced motion, captions, high contrast, text size — used across apps per NN-21) and `iam.users` (a Keycloak subject linked to a person; one person may have a staff identity and a customer identity, never merged across realms). `iam.memberships` link a person to a tenant with status (`invited`, `active`, `suspended`, `ended`), `kind` (`employee`, `director`, `external_professional`, `auditor`, `supervisor`, `delivery`, `coop_member`, `marketplace`), `hr_employee_ref` (P13), `designation`, `org_unit_ids[]`, `legal_entity_ids[]`, `valid_period`.

**FR-P01-11 — Role grants.** `iam.role_grants`: membership × role code × scope (`tenant`, `legal_entity`, `org_unit`, `instrument_pack`, `committee`, `audit_engagement`, `matter`) × valid period × granted_by × approved_by (for roles marked "approval required" in Appendix D: `ten_admin`, `ten_cco`, `ten_checker` for regulated packs, `ten_ic_member`, `ten_payroll_checker`, `ten_supervisor_view`, delivery maker grants). A person may hold several roles; **SoD rules** (Appendix D §D.4) block combinations on the same scope (for example maker and checker of the same compliance pack; payroll maker and payroll checker; internal auditor and process owner of the audited area; IC member and respondent in the same POSH matter — the latter enforced in P13). KMP sub-types (CEO, MD, WTD, CFO, CRO, CCrO, CCO, CS, CISO, CTO, CIO, DPO, GRO, PNO, IO) are attributes of `ten_kmp`, driving default dashboards and the governance registers in P06.

**FR-P01-12 — ABAC attributes.** Cerbos principal attributes: tenant, memberships, roles with scopes, legal entities, org units (including descendants via materialised path), KMP sub-types, committee memberships, audit engagements, delivery grant scopes, supervisor grant scopes, sealed clearances, assurance level and auth age, device posture (staff), working-hours window (optional, tenant-configured for exports). Resource attributes: tenant, legal entity, org unit, owner, assignees, data class, sealed flag, state, confidentiality label (`NORMAL`, `RESTRICTED`, `BOARD_ONLY`, `SEALED`), regulator-view eligible flag, export class. Policies live in `policies/cerbos/` versioned with the code, tested with Cerbos policy tests generated from Appendix D; changes to policies are code changes with CODEOWNERS = security + domain owner.

**FR-P01-13 — Enforcement library.** `packages/authz` provides `@Authorize(action, resourceResolver)` for NestJS handlers, `authz.planQuery(principal, resourceKind, action)` that converts Cerbos query plans into Drizzle `WHERE` fragments for list endpoints (so lists never return rows the user cannot open), and helpers for exports, background jobs (jobs carry the initiating principal or a named service principal with documented scope), AI retrieval filters (P17 uses the same plan to filter the retrieval index — a user's Vidhi never sees a document the user cannot open) and object-storage presigning. A Semgrep rule fails any controller method without `@Authorize` or `@Public(reason)`.

**FR-P01-14 — Delegation.** A user may delegate approval authority (for leave periods) to another user holding the same role on the same scope, never to the maker of the items concerned (NN-05), for a fixed period ≤ 30 days (tenant-configurable), with reason; delegated actions show "approved by B for A (delegation D-123)". Delegation of `ten_admin`, IC, supervisor or payroll checker roles is not allowed. Delegations are listed in the tenant's access review.

**FR-P01-15 — On-behalf-of (Vidhi).** Vidhi AI (P17) acts only with a token exchange (RFC 8693) producing a token whose `act` claim names `svc_vidhi` and whose `sub` is the requesting user; permissions are the intersection of the user's permissions and the Vidhi tool scope (Appendix K). Actions listed in NN-14 as human-only are refused for Vidhi tokens by policy, not by prompt.

### 4C. Special grants: delivery, auditors, supervisors, break-glass

**FR-P01-16 — Delivery grants (LawDocs staff in a client tenant; D-03, R-072).** `iam.delivery_grants`: tenant, engagement reference (retainer or marketplace order from P21/P22), staff person, roles granted inside the tenant (typically `ten_maker` for named compliance packs or departments; sometimes `ten_dept_head` for a managed function; never `ten_admin`, `ten_checker` of the same scope, sealed roles or `ten_supervisor_view`), scopes, valid period (engagement term), created by (`ten_admin`) **or** proposed by `dlv_lead` and approved by `ten_admin`, approval state, revoke reason. Rules:

1. The client remains in control: a delivery grant becomes active only on the tenant admin's approval (maker-checker inside the tenant if the tenant enables it).
2. Delivery staff act under their staff identity (`ldc-staff` realm) via token exchange into the tenant context; the UI marks them "LawDocs" everywhere; audit events record `actor_type = delivery` and the engagement.
3. Multiple makers per tenant are supported (R-072): the tenant may combine its own makers and LawDocs makers on the same pack; the checker is always a tenant employee unless the tenant explicitly appoints a LawDocs reviewer as an *additional* reviewer (never the sole checker of LawDocs-made items).
4. Revocation (by the tenant or at engagement end) removes access within 60 seconds and reassigns open tasks according to the tenant's rule (back to the pack owner by default).
5. Delivery staff cannot export bulk tenant data except through deliverable workflows (P22), and cannot reveal vault credentials without a per-credential grant (D-04).

**FR-P01-17 — Auditor grants.** Internal auditors are tenant members. External statutory, secretarial, IS, tax, concurrent and co-operative auditors receive `iam.audit_grants` (scope: legal entities, periods, modules, datasets, PII level, export level, valid ≤ engagement window, maximum 90 days per grant renewable), aligned with Ecosystem Spec §4.7 grantee types `RE_STATUTORY_AUDITOR`, `RE_INTERNAL_AUDITOR`, `RE_CONCURRENT_AUDITOR`, `RE_IS_AUDITOR`, `RE_SECRETARIAL_AUDITOR`, `RE_TAX_AUDITOR`, `COOP_AUDITOR`, with basis codes (`CA13_S143_1`, `CA13_S204`, `STATE_COOP_ACT`, `MSCS`, `CONTRACT`…). The auditor workspace (P10) uses these grants.

**FR-P01-18 — Supervisor view grants (D-12, NN-18, R-057).** `iam.supervisor_grants` implement the Ecosystem Spec §4.7 grant record and lifecycle `REQUESTED → BASIS_RECORDED → SCOPE_DEFINED → RE_APPROVED → PROVISIONED → ACTIVE ⇄ EXTENDED → EXPIRED | REVOKED → ARCHIVED`, with grantee types `RBI_SUPERVISOR`, `RBI_INSPECTION_TEAM`, `NHB`, `NABARD`, `IFSCA`, `REGISTRAR_INSPECTOR`, and LDC additions `SEBI_INSPECTION`, `IRDAI_INSPECTION`, `RCS_INSPECTOR`, `CRCS_INSPECTOR` [VERIFY: add to Ecosystem code table via the change process], basis codes (`RBI_S45N`, `BR_S35`, `STATE_COOP_ACT`, `MSCS`, `SEBI_INSPECTION`, `IRDAI_INSPECTION`, `IFSCA`, `CONTRACT`), named grantee identities with verified email domains (`rbi.org.in`, `sebi.gov.in`, `ifsca.gov.in`, `irdai.gov.in` or the authority's domain recorded by the tenant), PII, export and query levels (defaults MASKED / AGGREGATE / DASHBOARDS), valid ≤ 90 days. Tenant maker = CCO (or nominee), checker = MD/CEO or CISO (configurable, never the same person). Controls: read-only database role `ldc_supervisor_ro` on supervisor read models; no write route reachable; confidentiality banner citing the basis; watermarked exports; idle 15 minutes, absolute 8 hours; anomaly alerts (volume > 10× the grant's daily median, out-of-window access, repeated unmask attempts) to CCO and CISO; daily activity report to the CCO. The product never states or implies that it is connected to the regulator; the supervisor workspace header reads "Read-only access granted by <Tenant> under <basis> until <date>". If the Ecosystem Spec federation is active (the tenant's master register is in Finbyx AU7), LDC provisions on `POST /v1/external-access/grants` and emits `ExternalAccessGranted/Used/Revoked` (P18).

**FR-P01-19 — Break-glass (NN-30).** Platform support or security may access tenant data only through break-glass: request with scope (tenant, modules, read or read-write), ticket or incident reference, justification ≥ 30 characters; two-person approval for SEALED, CREDENTIAL, HR or write scopes; AAL3; maximum 4 hours (setting); tenant admins notified immediately (email + in-app + Updates feed entry "LawDocs support accessed your workspace") with scope and reason; every read is logged in `core.access_log`; session recorded (screens visited, records opened); post-session report auto-generated and shown to the tenant within 24 hours. Without break-glass, staff see only tenant metadata needed for support (plan, status, user counts, error codes). The tenant may set `iam.break_glass.tenant_prior_consent` = true, requiring the tenant admin's in-app approval before access (except for a declared Sev-1 security incident, which notifies instead).

### 4D. Invitations, bulk import and HRMS-linked provisioning

**FR-P01-20 — Invitations.** Kinds: `tenant_member`, `board_member`, `committee_member`, `auditor`, `supervisor` (sent only after an approved grant), `delivery_staff` (internal), `coop_member`, `marketplace_buyer_team`. Token: ≥ 128-bit random, URL-safe, SHA-256 stored, TTL 14 days (configurable 1–30), single binding, revocable, resend invalidates the previous token. The invitee verifies the addressed contact point before binding. Acceptance creates the membership and pending role grants (grants needing approval stay pending until approved). Invitation emails name the inviter and the company and never include sensitive content.

**FR-P01-21 — Bulk import.** CSV/XLSX template (`LDC-USERS-v1`): name, email, mobile, designation, department/function, legal entity, roles, KMP sub-type, manager email, HRMS employee code, start date. Preview with row-level validation (duplicate emails, unknown departments — offer to create, SoD conflicts, role needing approval), dry-run, commit, and a result file. Same template for export (users and roles report, which the tenant uses for quarterly access reviews — P24 provides the review workflow).

**FR-P01-22 — HRMS-linked provisioning (R-018, R-056).** When the HRMS module (P13) is enabled, `hr.EmployeeJoined`, `hr.EmployeeTransferred`, `hr.EmployeeExited`, `hr.DesignationChanged` events drive membership creation, org-unit and legal-entity scope changes and deactivation, using the tenant's role-mapping rules (designation/department → default roles, e.g. "Compliance Officer" → `ten_maker` on compliance packs; "Head – Risk" → `ten_kmp:CRO` + `ten_dept_head` on Risk). Mapped grants that need approval are queued to `ten_admin`. Exit deactivates access at the exit date/time (or immediately if the HR action is "terminate access now"), reassigns open tasks per rule, and records the handover. When an external HRMS (Microsoft Entra ID, Google Workspace, Keka, Zoho People, Darwinbox, greytHR via P18 connectors) is the source, the same mapping applies through SCIM or connector events.

### 4E. Self-onboarding funnel (R-069, R-016, R-034)

**FR-P01-23 — Entry points.** (a) Free Compliance Health Check report (P23) — "Start 7-day free trial with these results"; (b) pricing page configurator (P20/P23) — "Start trial" or "Buy now"; (c) marketplace checkout (P21) for services-only buyers (no tenant workspace is created; a buyer account and an organisation record are); (d) invitation by a sales or delivery person from the Operations Hub (lead record → `bil` quote → tenant created with the agreed plan; the OH never creates tenant data directly, it calls the provisioning API with business contact data only, Ecosystem Spec §4.6); (e) group onboarding (holding company adds subsidiaries).

**FR-P01-24 — Step 1: Account.** Name, work email (verified by magic link or code), mobile (verified by OTP, optional for the trial, required before payment), role in the company (drives the default dashboard), preferred language, MFA enrolment (passkey offered first; TOTP; MFA mandatory before Step 4 for the first admin). DPDP privacy notice (itemised: data, purposes, retention, rights, grievance contact, Data Protection Board complaint route — DPDP Rules 2025 Rule 3 notice content [VERIFY: rule numbering]) and consent artefact for optional purposes (product emails, marketing — separate, unticked). The baseline copy "We're ISO 27001 certified" is **not** used (NN-19); the copy says "Your data is stored in India" (true by NN-24) and links the trust page.

**FR-P01-25 — Step 2: Identify the organisation (KYB auto-fill).** The user enters **any one** of: PAN (entity), CIN, LLPIN, GSTIN, LEI, RBI CoR number, SEBI/IRDAI/IFSCA registration number, co-operative registration number, or the organisation name (type-ahead). The `KYB_PORT` (P18 adapters; Appendix L) queries in order of reliability and records each fact with `source`, `fetched_at`, `confidence`:

| Source | Facts | Notes |
|---|---|---|
| MCA master data (via a licensed data provider such as Probe42, Signzy, Surepass, Perfios/Karza — selection in Appendix L) | Name, CIN/LLPIN, date of incorporation, class (private/public/OPC), category, sub-category, status (active/strike-off), registered office, authorised and paid-up capital, directors/designated partners (name and DIN only), last AGM and balance-sheet dates, charges summary, listing status | MCA does not offer a public API for this; providers aggregate public records. Consent not required for public company data; DIN-level director data is personal data — store name, DIN and designation only, as needed for governance (purpose recorded) |
| GSTN taxpayer search (via a GST Suvidha Provider/ASP) | Legal and trade name, GSTIN status, constitution, state, principal place of business, registration date, return-filing status | One PAN may have several GSTINs (all states); user selects which to add |
| PAN verification (Protean e-Gov or provider) | PAN status, name match, entity type from the fourth character (C company, F firm/LLP, T trust, A AOP, B BOI, etc.) | Verification of name ↔ PAN only; no PAN card image is collected; PAN stored encrypted + masked + blind index |
| GLEIF LEI API (public) | LEI, legal name, address, status, parent relationships | Useful for banks, large NBFCs, listed and IFSC entities |
| Regulator public registers (RBI list of NBFCs/ARCs/UCBs; SEBI intermediary registers; IRDAI lists; IFSCA registered entities; CRCS MSCS list; state RCS portals where published) | Registration type, number, date, category | Fetched from published lists refreshed weekly by a P05 job; matching by name/registration number; shown as "found in RBI's published list as NBFC-ICC, registration B-14.xxxxx" [VERIFY per register availability and terms] |
| DigiLocker (organisation documents are rarely available; individual documents only with the individual's consent) | Not used for entity KYB by default | Used in P13 for employee onboarding documents with consent |

The user sees an auto-filled profile card ("We found Alpha Finance Private Limited — CIN U65xxx…, incorporated 12-Mar-2014, registered office Noida, 3 directors, RBI-registered NBFC") and confirms or corrects each field (a correction keeps the fetched value as "source value" and records the user's value with reason — useful when registers are stale). Failure of a source never blocks onboarding: the field becomes manual with a "We couldn't fetch this" note. **No credit bureau report (CIBIL, CRIF, Experian, Equifax) is pulled at onboarding**: LawDocsComply is not a specified user for that purpose under the Credit Information Companies (Regulation) Act 2005 and has no lawful basis to pull a client's bureau data; a client may later upload its own Company Credit Report if a module needs it [LAW: CICRA 2005 ss.17–19, 22 (access by specified users) [VERIFY]; REC]. Mentions of "CIBIL" in the brief are served by P11 (preparing the client's own CIC submission files), not by onboarding pulls.

**FR-P01-26 — Step 3: Entity profile.** Constitution (pre-selected from PAN fourth character and MCA class), legal entity details, financial year, size indicators used by applicability rules (asset size bands, deposit size, AUM, turnover, net worth, employee count bands, listed/unlisted, listing segment, number of members for co-operatives), group structure (add holding/subsidiaries/associates now or later; bulk lookup by CINs), and locations (states — they drive state labour and co-operative packs). Values used for regulatory classification (e.g., NBFC layer, UCB tier) are captured with the source and "as of" date and are re-confirmed annually by a P15 task.

**FR-P01-27 — Step 4: Regulatory profile and entity family.** The user selects the regulator(s) and entity type(s); suggestions are pre-ticked from Step 2 facts. The selection maps to the P15 `pack` taxonomy (entity families aligned with the Excel template families of Appendix E — e.g., RBI-NBFC with layer and type, RBI-SCB, RBI-UCB with tier, RBI-ARC, COOP-CCS state/multi-state, IFSCA-FCFU, SEBI-LISTED, SEBI-AIF category, IRDAI-INT broker type, MCA-CO, MCA-LLP), and cross-cutting packs (data protection, cyber, labour and POSH, GST/tax, Companies Act/LLP Act always on for companies/LLPs). An entity can belong to several families (a listed NBFC; a UCB that is also a co-operative society; an AIF whose manager is a company). The wizard shows the resulting applicability preview ("312 obligations across 18 instruments will be loaded; 41 need your confirmation of thresholds") from P03/P15 rules; P01 provides the step and the call, P15 the logic.

**FR-P01-28 — Step 5: Modules and live price.** Module cards (Compliance core, Governance & Secretarial, Policies & DMS, Risk Management, Risk Assessment Lab/ICAAP, Audit, Return Studio, Data Protection & Cyber, HRMS & Labour, Grievance Desk, Co-operative Suite, Vidhi AI tiers, Integrations), each with a one-line benefit, an "i" explanation, what it includes, and whether it is included in the selected plan or an add-on. The price panel (Apple-style running total — R-070) calls `bil.quote(plan, add-ons, entities, users, billing period, promo code)` — which returns OH8 catalogue prices and tax; LDC computes no price or tax itself (X-02) — and shows base price, each add-on, discounts, GST (18% [VERIFY rate and SAC]), total, and what happens after the trial. Modules selected here become trial entitlements (`core.tenant_modules`); during the trial all selected modules are fully usable with trial limits (Appendix N).

**FR-P01-29 — Step 6: Trial start and tenant provisioning.** "Start my 7-day free trial" creates the tenant via `TenantProvisionWorkflow` (P00 §5.3) with `status = trial`, `trial_ends_at = now + trial_days` (default 7; super admin may extend per tenant through an `ENTITLEMENT` Correction Entry with reason and second approver, or an approved promo rule; tenant-visible (NN-02, master §6.6)), loads the setting pack for the entity family (P02), loads applicable content (P03/P15) in the background with a progress indicator, and assigns the first admin `ten_admin` + the KMP sub-type chosen in Step 1. No payment method is required to start the trial (configurable `bil.trial.card_required` = false). The trial is limited to one trial per organisation identifier (PAN/CIN/GSTIN blind index) per 12 months, enforceable by super-admin exception.

**FR-P01-30 — Step 7: Team and workflows.** Invite colleagues with role templates ("Compliance team: 1 CCO, 2 makers, 1 checker"; "Board: 5 directors"); set up departments from the family default (customisable names — R-086); choose the approval model (single checker, two-level, department head sign-off); optional SSO connection. Import from Excel or from Microsoft 365/Google directory (P18) if connected. Skippable.

**FR-P01-31 — Step 8: First value.** The wizard ends on a page with three concrete results generated from the tenant's data: (1) "Your next 30 days" — calendar of due obligations; (2) "Top 5 gaps from your health check" converted into tasks with owners; (3) a draft board note "Compliance status as on <date>" (Vidhi-generated draft if AI is enabled for the trial, otherwise a deterministic template). A 3-minute guided tour (P23) starts on first dashboard visit. Save-and-resume: every step auto-saves; the user can return within 30 days; reminders on day 1 and day 3 if incomplete (transactional emails; marketing emails only with consent).

**FR-P01-32 — Trial lifecycle.** States: `trial → (converted) active | (day N) grace | expired`. Day 5: in-app and email reminder with plan summary and value delivered ("38 obligations tracked, 12 evidence files uploaded"); day 7: trial ends — if no plan purchased, `grace` for 7 days (configurable): read-only access, export available, no new content; after grace, `expired`: data retained 30 days (configurable) for return, then deletion per the retention schedule with a final export offer (P19). Conversion is handled by P20; P01 handles state, access level and messages. Super admin can extend or re-open a trial for a company (R-070) through the console with reason.

**FR-P01-33 — Services-only buyers (R-035).** A marketplace buyer creates an account (email + mobile verified), an organisation record (PAN/GSTIN auto-fill for GST invoices — GSTIN needed for input-tax credit), and pays for services without a tenant workspace. If the buyer later starts a SaaS trial, the organisation record becomes the tenant's legal entity without re-entry.

**FR-P01-34 — Assisted onboarding.** A LawDocs onboarding specialist (delivery role `dlv_lead` with an onboarding grant approved by the client) may complete steps on the client's behalf during an implementation engagement; every step shows who completed it. Enterprise variations (several entities, SSO first, data migration from another GRC tool) follow the implementation checklist in P22.

### 4F. Account experience and privacy centre

**FR-P01-35 — My account.** Profile, contact points, language, timezone, accessibility preferences (FR-P01-10), notification channels and quiet hours (consumed by P04), calendar connections (P04/P18), security (factors, passkeys, recovery codes, sessions, devices), delegations, memberships (tenants the person belongs to, with capacity), API tokens for personal integrations (P18, if enabled by the tenant).

**FR-P01-36 — Privacy centre (DPDP, GDPR, CCPA as applicable to LawDocsComply as fiduciary/controller for user account data).** View the notice and consents; withdraw optional consents (propagation to marketing systems in the Operations Hub through the consent event within 24 hours); request access/correction/erasure/nomination (DPDP s.11–14) for the user's own account data, routed to the LawDocsComply DPO workflow; note that compliance records the user created inside a client tenant belong to the client (LawDocsComply is processor there), so erasure requests about those are forwarded to the client's DPO (P12) — the user is told this plainly.

---

## 5. Workflows and state machines

### 5.1 User and membership

`invited → active → suspended → active | ended`; `ended` is terminal (re-join creates a new membership). Suspension reasons: admin action, SCIM `active=false`, HR exit pending date, tenant suspension, security lock. Ending a membership revokes grants and sessions, reassigns open tasks (rule: to the pack owner, else the department head, else `ten_cco`), keeps all authored records attributed to the person.

### 5.2 Role grant needing approval

`requested → approved → active → expired | revoked`; `requested → rejected`. Approver ≠ requester; for `ten_admin` grants, approver is another `ten_admin`; first admin of a new tenant is auto-approved by onboarding and must be confirmed by a second admin within 30 days or a reminder escalates (configurable).

### 5.3 Delivery grant

`proposed (by dlv_lead) → tenant_approved (ten_admin) → active → suspended (tenant) → active | ended (engagement end, revoke)`; or `created (by ten_admin) → active`. Ending triggers task reassignment and a handover note generated by the delivery console.

### 5.4 Supervisor grant

As FR-P01-18; timers: `ACTIVE` grant 7 days before `valid_to` notifies the CCO ("extend or let expire"); on expiry, sessions revoked within 60 seconds; logs retained inspection cycle + 8 years.

### 5.5 Break-glass

`requested → approved (1 or 2 approvers) → active (≤ max minutes) → ended (manual or timeout) → reported (post-session report to tenant)`; `requested → denied`. A tenant with prior-consent mode adds `awaiting_tenant_consent` before `approved`.

### 5.6 Onboarding journey

`started → account_verified → organisation_identified → profile_confirmed → regulatory_profile_set → modules_selected → trial_started → team_invited (optional) → first_value_seen`; any state may become `abandoned` after 30 days of inactivity (data deleted except the lead record with consent). Funnel metrics per step (P23 dashboards; OH CRM receives only business contact and stage, with consent).

### 5.7 KYB fetch

`requested → fetching (parallel sources, 8-second budget per source) → partial | complete | failed`; results cached per identifier for 24 hours (public data only); a "refresh from source" action re-fetches. Each fact retains its source record for audit ("as fetched from MCA via <provider> on 25-Oct-2026 11:02 IST").

---

## 6. Screens and UX

| Screen ID | Name | App / path | Roles |
|---|---|---|---|
| SCR-IAM-01 | Sign in (email, passkey, SSO discovery by domain) | auth | all |
| SCR-IAM-02 | MFA challenge and step-up | auth | all |
| SCR-IAM-03 | Enrol second factor / passkey | auth | all |
| SCR-IAM-04 | Account recovery | auth | all |
| SCR-IAM-05 | Accept invitation | auth/web | invitees |
| SCR-IAM-06 | Tenant and capacity switcher (header) | web, delivery | multi-membership users |
| SCR-IAM-10 | Onboarding — Account | public→web | new admin |
| SCR-IAM-11 | Onboarding — Find your organisation (KYB) | web | new admin |
| SCR-IAM-12 | Onboarding — Entity profile and group | web | new admin |
| SCR-IAM-13 | Onboarding — Regulatory profile and families (applicability preview) | web | new admin |
| SCR-IAM-14 | Onboarding — Modules and price | web | new admin |
| SCR-IAM-15 | Onboarding — Team and workflows | web | new admin |
| SCR-IAM-16 | Onboarding — First value | web | new admin |
| SCR-IAM-20 | My account (profile, language, accessibility) | web, delivery, console | all |
| SCR-IAM-21 | Security (factors, passkeys, recovery codes) | same | all |
| SCR-IAM-22 | Sessions and devices | same | all |
| SCR-IAM-23 | Privacy centre | web, public | all customers |
| SCR-IAM-30 | Users (list, filters, bulk actions) | web › Settings › Users & access | ten_admin |
| SCR-IAM-31 | User detail (memberships, roles, scopes, SoD warnings, activity) | same | ten_admin |
| SCR-IAM-32 | Roles and role templates (view; custom role names in P02) | same | ten_admin |
| SCR-IAM-33 | Pending approvals (role grants, delivery grants) | same | ten_admin |
| SCR-IAM-34 | Bulk import users | same | ten_admin |
| SCR-IAM-35 | SSO and SCIM | same | ten_admin |
| SCR-IAM-36 | Delivery access (LawDocs staff in your workspace) | same | ten_admin, ten_cco |
| SCR-IAM-37 | Auditor access grants | same | ten_admin, ten_cco |
| SCR-IAM-38 | Supervisor (regulator) access | same | ten_cco (maker), MD/CEO/CISO (checker) |
| SCR-IAM-39 | Support access and break-glass history | same | ten_admin |
| SCR-IAM-40 | Access review (quarterly attestation; P24 workflow) | same | ten_admin, dept heads |
| SCR-IAM-50 | Staff directory and delivery assignments | delivery › Team | dlv_lead |
| SCR-IAM-51 | Request delivery grant | delivery › Clients › <client> › Access | dlv_lead |
| SCR-IAM-60 | Platform users and roles | console › Access | plt_super_admin |
| SCR-IAM-61 | Break-glass console | console › Access › Break-glass | plt_support, plt_security_officer |
| SCR-IAM-62 | Trials and extensions | console › Tenants › Trials | plt_super_admin, plt_finance |

UX rules: the onboarding wizard shows a persistent progress bar with step names and time estimate; every auto-filled field shows its source on hover/focus and an "i" explanation (e.g., "NBFC Layer — RBI's Scale Based Regulation classifies NBFCs into Base, Middle, Upper and Top layers by size and risk; it decides which rules apply to you"); one primary action per screen; "Ask Vidhi" side panel available (P17; deterministic help text when AI is off); keyboard-only completion possible; fields announce errors with text, not colour alone; mobile-responsive. Users list: saved views (by department, role, last login, MFA status), bulk actions (assign role with preview of SoD conflicts, suspend, resend invitation, export) with an impact preview and 10-second undo for reversible actions. The header shows the active tenant, legal-entity scope and capacity badge at all times.

---

## 7. Backend design

### 7.1 Modules touched

`iam` (owner), `core` (tenants, provisioning), `bil` (quote and trial stubs), `pack` (applicability preview call), `cfg` (settings registration), `int` (KYB adapters via ports), `hr` (event contracts, consumer stubs).

### 7.2 Tables (key columns; DDL in Appendix B)

`iam.persons`, `iam.contact_points` (type, value encrypted + blind index + masked, verified_at), `iam.users` (realm, subject, person_id), `iam.memberships`, `iam.role_grants`, `iam.role_grant_approvals`, `iam.sod_rules` (seeded from Appendix D), `iam.delegations`, `iam.delivery_grants`, `iam.audit_grants`, `iam.supervisor_grants`, `iam.grant_usage_daily`, `iam.invitations`, `iam.bulk_imports`, `iam.sso_connections`, `iam.scim_tokens`, `iam.role_mappings` (group/designation → role), `iam.sessions_index` (session metadata mirror for UI), `iam.consents` (DPDP artefacts for LawDocsComply's own processing: purpose, notice version, given_at, withdrawn_at, channel), `iam.privacy_requests`, `iam.onboarding_journeys`, `iam.kyb_facts` (identifier, field, value (encrypted if personal), source, fetched_at, confidence, user_override), `core.tenant_trials` (ends_at, extended_by, reason).

### 7.3 APIs (selected; full list in OpenAPI)

| Method and path | Purpose |
|---|---|
| `POST /v1/onboarding/journeys` / `PATCH …/{id}` | Create and advance a journey (step payloads) |
| `POST /v1/onboarding/kyb:lookup` | KYB fetch by identifier or name (rate-limited; anonymous only with verified email) |
| `POST /v1/onboarding/journeys/{id}:start-trial` | Provision tenant and trial |
| `GET /v1/me` / `PATCH /v1/me` | Profile, preferences |
| `GET /v1/me/memberships` / `POST /v1/me/context` | Memberships and context switch |
| `GET/POST /v1/users`, `PATCH /v1/users/{id}`, `POST /v1/users:bulk-import` | Tenant user admin |
| `POST /v1/role-grants`, `POST /v1/role-grants/{id}:approve` | Grants |
| `POST /v1/delegations` | Delegation |
| `POST /v1/delivery-grants`, `:approve`, `:revoke` | Delivery access |
| `POST /v1/audit-grants`, `:approve`, `:revoke` | Auditor access |
| `POST /v1/supervisor-grants`, `:record-basis`, `:define-scope`, `:approve`, `:revoke`, `:extend` | Supervisor access |
| `POST /v1/external-access/grants`, `DELETE …/{id}` | Ecosystem federation endpoint (Ecosystem Spec §4.7) |
| `POST /v1/break-glass`, `:approve`, `:end`, `GET /v1/break-glass/{id}/report` | Break-glass |
| `POST /v1/invitations`, `:resend`, `:revoke`, `POST /v1/invitations/{token}:accept` | Invitations |
| `/scim/v2/Users`, `/scim/v2/Groups` | SCIM |
| `POST /v1/sso-connections`, `:verify-domain`, `:enforce` | SSO |
| `POST /v1/privacy/requests` | Privacy centre |
| `POST /v1/authz/check` (internal) | Batch permission checks for UI rendering hints (never a substitute for server enforcement) |

### 7.4 Domain events

Internal: `in.lawdocscomply.iam.UserInvited.v1`, `…UserActivated.v1`, `…MembershipEnded.v1`, `…RoleGranted.v1`, `…RoleRevoked.v1`, `…DelegationCreated.v1`, `…DeliveryGrantActivated.v1`, `…DeliveryGrantEnded.v1`, `…AuditGrantActivated.v1`, `…SupervisorGrantActivated.v1`, `…SupervisorGrantUsed.v1` (daily roll-up), `…SupervisorGrantRevoked.v1`, `…BreakGlassApproved.v1`, `…OnboardingStepCompleted.v1`, `…TrialStarted.v1`, `…TrialExtended.v1`, `…TrialExpired.v1`, `…ConsentWithdrawn.v1`, `…PrivacyRequestReceived.v1`. Ecosystem (mapped by `int`): `in.infrabyx.audit.ExternalAccessGranted.v1`, `…ExternalAccessUsed.v1`, `…ExternalAccessRevoked.v1`; Operations Hub lead/stage events with business contact data only and consent reference.

### 7.5 Jobs and workflows

`OnboardingJourneyWorkflow` (reminders, abandonment); `KybFetchWorkflow`; `TrialLifecycleWorkflow` (day-5 reminder, end, grace, expiry); `GrantExpiryWorkflow` (delivery, audit, supervisor, delegations); `SupervisorAnomalyMonitor` (hourly); `BreakGlassTimer`; `ScimReconcile` (nightly diff with IdP where API allows); `DormantAccountSweep` (users inactive 90 days → suspend, configurable); `RegisterListRefresh` (weekly regulator public lists, owned jointly with P05).

---

## 8. Integrations (ports and adapters)

| Port | Adapters (candidates; selection in Appendix L) | Failure behaviour |
|---|---|---|
| `IDP_PORT` | Keycloak; Microsoft Entra ID (staff and tenant SSO); Google Workspace; generic SAML/OIDC | Local login for break-glass admins |
| `SCIM_PORT` | Entra ID, Google Workspace, Okta | Manual user admin |
| `KYB_PORT` | MCA data providers (Probe42, Signzy, Surepass, Perfios/Karza), GSP/ASP for GSTIN search, Protean/provider for PAN verification, GLEIF LEI, regulator public lists | Field becomes manual; no blocking |
| `KYC_PORT` (persons; used later in P13/P16) | DigiLocker via licensed partner; Aadhaar offline verification only if LawDocsComply or the client registers as an OVSE under the Aadhaar (Authentication and Offline Verification) Amendment Regulations 2025 [VERIFY] | Document upload with manual verification |
| `OTP_PORT` | SMS gateway with DLT templates (MSG91, Gupshup, Kaleyra…), WhatsApp Business (Gupshup, Meta Cloud API), Amazon SES for email | Fallback channel order |
| `PRICING_PORT` | `bil.quote` (P20); stub with seed catalogue until then | Show "price shown at checkout" |
| `OH_PORT` | Operations Hub provisioning acknowledgement and lead-stage events (Ecosystem Spec §4.6, 6.29) | Queue and retry |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `iam.mfa.required_roles` | G (tenant may add roles) | all privileged roles (§3) | cannot remove platform floor | ten_admin (add only) |
| `iam.mfa.maker_aal` | T | aal2 | aal1–aal2 | ten_admin |
| `iam.stepup.export_rows_threshold` | T | 1000 | 100–100000 | ten_admin |
| `iam.session.idle_minutes.professional` | T | 15 | 5–30 | ten_admin |
| `iam.session.absolute_hours.professional` | T | 12 | 4–12 | ten_admin |
| `iam.sso.enforce` | T | false | — | ten_admin |
| `iam.invitation.ttl_days` | T | 14 | 1–30 | ten_admin |
| `iam.delegation.max_days` | T | 30 | 1–90 | ten_admin |
| `iam.delivery_grant.tenant_maker_checker` | T | false | — | ten_admin |
| `iam.delivery_grant.lawdocs_sole_checker_allowed` | L | false | — | — |
| `iam.supervisor_grant.max_days` | L | 90 | — | — |
| `iam.supervisor_grant.default_pii_level` | T | MASKED | MASKED \| UNMASK_ON_REQUEST | ten_cco |
| `iam.supervisor_grant.anomaly_multiplier` | T | 10 | 3–50 | ten_kmp:CISO or ten_admin |
| `iam.break_glass.tenant_prior_consent` | T | false | — | ten_admin |
| `iam.dormant.suspend_after_days` | T | 90 | 30–365 | ten_admin |
| `iam.onboarding.resume_days` | G | 30 | 7–90 | plt_super_admin |
| `bil.trial.default_days` (owned by P20; per-tenant extension by `ENTITLEMENT` Correction Entry) | G | 7 | 1–60 | `plt_super_admin` + checker |
| `bil.trial.grace_days` | G | 7 | 0–30 | plt_super_admin |
| `bil.trial.card_required` | G | false | — | plt_super_admin |
| `bil.trial.one_per_org_months` | G | 12 | 0–36 | plt_super_admin |
| `iam.kyb.sources_order` | G | as §4E table | — | plt_super_admin |
| `iam.kyb.cache_hours` | G | 24 | 1–168 | plt_super_admin |

---

## 10. Security, privacy and audit

- Every grant, delegation, SoD override (if a tenant explicitly accepts a conflict, it needs CCO approval and an expiry ≤ 90 days, shown in access reviews), break-glass, supervisor and auditor action is a material action in the audit ledger.
- KYB facts are public business data; director names and DINs are personal data processed for governance purposes (DPDP s.7 legitimate uses do not obviously cover this; LawDocsComply relies on the client's instruction as processor for governance records, and on notice for its own onboarding [INTERP; VERIFY with counsel]). No Aadhaar, no bureau data, no PAN images.
- Rate limits and bot protection on onboarding and KYB endpoints (abuse could turn the KYB lookup into a free data-scraping service): verified email required, 20 lookups per hour per account, CAPTCHA-free challenge (Cloudflare Turnstile or AWS WAF challenge) for anonymous health-check lookups, results limited to fields needed for onboarding.
- Authentication events (success, failure, MFA, step-up, recovery) are logged; failed-login monitoring with alerting on credential-stuffing patterns; impossible-travel heuristic for staff.
- Supervisor and auditor accesses produce daily reports to the CCO and are exportable with a s.63 certificate.
- Threat model: account takeover of a `ten_admin`; malicious LawDocs RM; insider super admin (mitigated by D-02 corrections, break-glass, tenant visibility); supervisor credential misuse; SCIM token leak; KYB scraping. Recorded in `docs/security/threat-model-iam.md`.

---

## 11. AI touchpoints and guardrails

- "Ask Vidhi" help during onboarding explains terms using platform content only (no tenant data before the tenant exists); deterministic help when AI is off.
- Optional AI matching of an organisation name to registry results (fuzzy name matching is deterministic first; AI only to explain ambiguity) — no AI decision on identity.
- The "first value" draft board note is labelled "Draft generated by Vidhi AI — review before use" (NN-04).
- Vidhi's on-behalf-of tokens (FR-P01-15) are built here; Vidhi can never approve grants, create users, change roles, start break-glass or approve supervisor access (NN-14 policy tests).

---

## 12. Acceptance criteria (`tests/acceptance/p01/*.feature`)

```gherkin
Feature: Self-onboarding with KYB auto-fill
  Scenario: New NBFC onboards from a health-check report in under 30 minutes
    Given a lead has completed the free health check as "NBFC – Middle Layer"
    When she clicks "Start 7-day free trial" and verifies her work email
    And enters CIN "U65999DL2014PTC000000" (synthetic)
    Then the entity profile is auto-filled with name, incorporation date, registered office and directors from the MCA data adapter
    And each auto-filled field shows its source and fetch time
    When she confirms the profile, selects "RBI – NBFC – Middle Layer – NBFC-ICC" and the Compliance, Governance and Risk modules
    Then the price panel shows base price, add-ons, GST and total from the pricing catalogue
    When she enrols a passkey and starts the trial
    Then a tenant in status "trial" is created with trial_ends_at 7 days ahead
    And the first-value page shows the next 30 days of obligations

  Scenario: Source failure does not block onboarding
    Given the GSTN adapter is unavailable
    When the user enters a PAN
    Then MCA and PAN facts are filled and GSTIN fields become manual with a "We couldn't fetch this" note

  Scenario: No credit bureau pull at onboarding
    When any onboarding flow completes
    Then no call is made to any credit information company adapter

Feature: Least privilege
  Scenario: Maker cannot approve own submission
    Given user M holds ten_maker and ten_checker on different packs
    When M submits evidence on pack P1 where M is maker
    Then M is not offered and cannot call approve on that item (403 LDC-IAM-020)

  Scenario: List endpoints never leak unauthorised rows
    Given a department head of "Treasury" in legal entity E1
    When she lists compliance instances
    Then only instances of org units under "Treasury" in E1 are returned

Feature: Delivery staff act as visible guests
  Scenario: Client approves a LawDocs RM as maker
    Given dlv_lead proposes RM R as ten_maker on "RBI – NBFC Master Directions" for tenant Alpha
    When Alpha's ten_admin approves
    Then R can switch into Alpha as "Maker – via LawDocs retainer"
    And every action by R in Alpha shows "LawDocs (R)" and records actor_type delivery
    When Alpha's ten_admin revokes the grant
    Then R's access ends within 60 seconds and R's open tasks move to the pack owner

  Scenario: LawDocs reviewer cannot be the sole checker of LawDocs-made items
    Given an item made by RM R
    When the tenant tries to set LawDocs reviewer L as the only checker
    Then the configuration is refused with LDC-IAM-031

Feature: Supervisor view
  Scenario: RBI inspection team receives time-boxed read-only access
    Given Alpha's CCO creates a supervisor grant for two named "rbi.org.in" accounts under basis RBI_S45N valid 30 days
    And Alpha's MD approves it with step-up
    When an inspector signs in
    Then the header shows "Read-only access granted by Alpha under RBI s.45N until <date>"
    And any write API returns 403 and no write control is rendered
    And exports are watermarked and logged
    When the grant expires
    Then sessions are revoked within 60 seconds

Feature: Break-glass
  Scenario: Support access is visible to the tenant
    Given a support engineer requests read access to tenant Alpha for ticket T-991
    When a security officer approves
    Then Alpha's admins receive an immediate notification with scope and reason
    And a post-session report appears in SCR-IAM-39 within 24 hours

Feature: HRMS-linked deactivation
  Scenario: Employee exit removes access
    Given employee E with ten_maker is marked exited effective today 18:00 in HRMS
    When the time passes
    Then E's sessions are revoked and open tasks are reassigned per rule

Feature: Strong authentication
  Scenario: SMS OTP is refused as second factor for ten_admin
    When a ten_admin tries to enrol SMS OTP as the only second factor
    Then enrolment is refused and passkey or TOTP is required
```

NN tests: `NN-05_maker_checker_*`, `NN-14_vidhi_cannot_grant`, `NN-18_supervisor_readonly_*`, `NN-12_no_bureau_pull_onboarding`, `NN-30_breakglass_tenant_visible`, `NN-21_onboarding_axe` (zero serious/critical; keyboard-only completion), `NN-19_no_cert_claim_onboarding_copy`.

---

## 13. Deliverables and exit gate

- [ ] Keycloak realms, clients, theme (WCAG 2.2 AA), authenticators; staff realm federated to Entra ID; SCIM endpoints.
- [ ] Cerbos policies generated from Appendix D with ≥ 1 allow and ≥ 1 deny test per matrix row; `packages/authz` with query-plan filters; Semgrep rule for unauthorised handlers.
- [ ] Delivery, auditor and supervisor grants; break-glass UI and tenant reports; delegations; SoD enforcement.
- [ ] Onboarding funnel steps 1–8 with KYB adapters (at least MCA data provider, GSTN search, PAN verification, GLEIF) in sandbox; trial lifecycle; services-only buyer path.
- [ ] Users admin, bulk import, invitations, HRMS-event consumer contract (P13 will produce).
- [ ] Privacy centre for LawDocsComply's own account data; consent ledger.
- [ ] Migration wave 2 executed with reconciliation; all migrated users enrolled in MFA on first login.
- [ ] Settings registered; screens SCR-IAM-01 to 62; acceptance and NN tests green.
- [ ] `docs/phases/P01-plan.md` with the five inventories.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P01-01 | Choice and contract of MCA data provider; terms on reuse and storage of director data | Vendor and legal | CTO / CS | Manual entry; `iam.kyb.mca.enabled` = OFF until contract |
| OI-P01-02 | GSP/ASP for GSTIN taxpayer search | Vendor | CTO | Manual GSTIN entry with checksum validation |
| OI-P01-03 | PAN verification route (Protean eligibility vs provider) | Eligibility | CTO / CA | Format + fourth-character validation only |
| OI-P01-04 | Availability and terms of regulator public registers for automated matching (RBI, SEBI, IRDAI, IFSCA, CRCS, state RCS) | Terms of use differ | Compliance | User-entered registration with "unverified" badge |
| OI-P01-05 | DLT principal-entity registration for SMS (which group company) | Telecom | CS | Email-only OTP; WhatsApp after template approval |
| OI-P01-06 | Supervisor grantee types and basis codes for SEBI/IRDAI/RCS to add to the Ecosystem code table | Change process | Integration Spec owner | LDC-local codes mapped to `CONTRACT` |
| OI-P01-07 | Whether director DIN/name processing for governance needs notice to directors from the client | DPDP reading | Counsel | Client instruction recorded; notice template offered to client |
| OI-P01-08 | Keycloak SCIM server capability maturity | Product roadmap | Tech lead | SCIM implemented in `iam` |
| OI-P01-09 | DPDP Rules 2025 notice-content rule number and Consent Manager interoperability (registrations from 13 Nov 2026) | Phased commencement | DPO | Notice per s.5 content; consent manager integration flag OFF |
| OI-P01-10 | GST rate/SAC for SaaS subscriptions shown in the price panel | Tax | CA | Show "GST as applicable" until confirmed |
| OI-P01-11 | Aadhaar OVSE registration if offline verification is ever needed (employees, co-op members) | UIDAI process | CS | DigiLocker or document upload only |

---

## 15. Sources (checked 25 October 2026 unless stated)

1. Infrabyx Ecosystem Integration Specification v1.1 — §3.6 (tokens), §4.1, §4.5, §4.6 (group identity and Operations Hub), §4.7 (external auditor and supervisor access: grantee types, basis codes, lifecycle, ≤ 90 days, common controls).
2. Equator Build Prompt Pack v3.1 — P01 (authentication architecture, assurance levels, OTP, SSO, sessions, recovery — pattern reference).
3. Owner's LawDocs Comply Architecture Part 1 — "Onboarding the Company" (nine-step wizard, entity taxonomy, branching logic, field validation).
4. UIDAI — Offline Verification Seeking Entities, OVSE Playbook; Aadhaar (Authentication and Offline Verification) Amendment Regulations 2025 (summary: https://www.indialaw.in/blog/regulatory/aadhar-offline-verification-amendments/) [VERIFY against gazette text]; https://uidai.gov.in/ovse
5. DigiLocker — Terms of Use for Requesters (June 2025): https://cf-media.api-setu.in/resources/DigiLocker-Terms-of-User-Requester-june-2025.pdf
6. Digital Personal Data Protection Act 2023 and DPDP Rules 2025 (notified 13 Nov 2025; phased commencement) — https://www.meity.gov.in/
7. Credit Information Companies (Regulation) Act 2005 — access by specified users [VERIFY sections].
8. TRAI Telecom Commercial Communications Customer Preference Regulations 2018 (as amended).
9. W3C WCAG 2.2 (SC 3.3.8 Accessible Authentication); W3C WebAuthn Level 3; NIST SP 800-63B (authenticator assurance) — reference.
10. RFC 7643/7644 (SCIM 2.0), RFC 8693 (Token Exchange), RFC 9700 (OAuth 2.0 Security BCP).
11. Keycloak release history (26.8.x, Oct 2026) — https://versionlog.com/keycloak/ [VERIFY on keycloak.org].

---

## 16. Master integration notes (pack lead, 25 October 2026)

This phase is bound by the following master-prompt rules and cross-file resolutions added at integration: **NN-43; X-07 (no credit-bureau pulls at onboarding), X-13 (shells), X-15 (trial tenants, pending D-26), X-17, X-19 (added roles)**. Where any text above conflicts with them, master §4 and §18 prevail. Proposed rules in this phase's stream notes were consolidated into NN-33–NN-46 (`02` §3.3). Events listed above that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01).

