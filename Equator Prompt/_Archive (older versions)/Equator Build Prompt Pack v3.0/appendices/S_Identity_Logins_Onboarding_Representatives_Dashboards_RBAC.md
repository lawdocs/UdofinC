# Appendix S — Identity, Separate Login Portals, Onboarding Integrations, Representatives, Dashboards and RBAC

> **Binding reference** for P01 (identity, login, onboarding, consent) and P12 (mobile), and consumed by P02 (representatives, service on representatives), P03 (neutral portal), P09 (enterprise/GRO portal), P10 (Private Chambers portal) and P13 (partner portal). Read with the master prompt (NN-01–NN-32, §1.5 role codes, §4.1 auth stack, X-01), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-07, R-12, R-14, R-16; D2-05, D2-06, D2-24), P01, P12, Appendix C (screens, dashboards §D), Appendix F (DDL, events, errors — F prevails on names), Appendix G (legal rules), Appendix N (neutral grades), Appendix O (billing and membership settings), Appendix Q (privacy and security controls). Version 2.0, 21 October 2026.

**Tags used in this appendix.** **[K]** settled law or well-known fact; **[V-s]** verified from a secondary source in research stream S7 (re-confirm against the primary before it gates code); **[VERIFY — open: …]** must be closed by counsel or the vendor before the dependent feature flag is turned ON.

---

## 0. Scope, precedence and reconciliations made in this appendix

This appendix extends P01; it does not replace it. Where P01 already specifies a mechanism (OTP, magic link, passkeys, SSO, DPoP, recovery, consent ledger), this appendix cites the P01 requirement and adds only the v2 delta. Order of precedence follows master §15: master → Appendix G (law) → Appendix F (names, types, events, errors) → Appendix A → phase file → this appendix.

Conflicts found while writing this appendix and the resolution applied (record each in `docs/adr/` when implemented):

| # | Conflict | Resolution |
|---|---|---|
| S-R1 | P01 §7.3 uses `EQ-AUTH-0xx` / `EQ-KYC-0xx` error codes; Appendix F §F.10 uses canonical upper-snake codes and says phase codes are sub-codes carried in `rule`. | P01 codes become **sub-codes** under canonical codes (mapping in §8.4). New canonical codes needed by this appendix are listed in §8.4 and must be added to F.10.1 / `packages/domain/errors.ts` in the P01 v2 slice. |
| S-R2 | `core.party_representatives`: P01 DDL (case_id nullable, `scope jsonb`, `representative_type`, statuses `requested…completed`) differs from Appendix F (case_id NOT NULL, `scope text[]` limited to 7 values, statuses `pending_verification/active/revoked/expired`). | Appendix F prevails on the table name and existing columns. §8.1 adds **additive** columns and replaces F's `scope` CHECK with the v2 scope catalogue (§4.3) through a reviewed migration (ADR required — this is a CHECK change, not additive). `organisation_standing` mandates move to a new table `core.standing_authorities` so F's `case_id NOT NULL` holds. |
| S-R3 | Gender enum: P01 `Female/Male/Transgender/Prefer not to say`; F `female, male, non_binary, undisclosed`. | F prevails on stored values; UI labels: Female → `female`; Male → `male`; Transgender / non-binary → `non_binary`; Prefer not to say → `undisclosed`. P01 open item 9 closed. |
| S-R4 | Aadhaar column: P01 `aadhaar_last4`; F `aadhaar_ref_masked` (`^X{8}[0-9]{4}$`). | F prevails (`aadhaar_ref_masked`). |
| S-R5 | `kyc_method` enum (F.3) lacks the OVSE modalities required by D2-06. | Add `aadhaar_app_avc`, `aadhaar_offline_ekyc`, `aadhaar_face_offline`, `epassport_nfc`, `liveness`, `face_match` (additive; §8.1). F's existing `aadhaar_offline_xml` is kept as an alias of `aadhaar_offline_ekyc` for historical rows. |
| S-R6 | Face-match thresholds: P01 FR-P01-14 default ≥ 0.80; S7 §2.7 recommends ≥ 0.85 auto-pass, 0.60–0.85 manual review, < 0.60 fail. | S7 bands adopted as defaults in `assurance_policy` (configurable), pending vendor FAR/FRR calibration **[VERIFY — open (vendor): provider-specific calibration on an Indian demographic test set; FMR/FNMR per ISO/IEC 19795-1; Equator policy: '< 0.60' blocks automatic K2 only and routes to manual review/video KYC — never an automated rejection]**. |
| S-R7 | Mobile refresh lifetime for professionals: P01 FR-P01-09 = 14 days; P12 FR-P12-03 = 7 days (neutral, enterprise). | P12 governs mobile (master X-03 principle): 7 days for neutral and enterprise spaces; P01 value applies to web only. |
| S-R8 | Master §1.5 has two representation roles: `counsel` (advocate/authorised representative under mandate) and `representative` (non-advocate authorised representative). P01 treats both as `counsel` with `representative_type`. | Keep both role codes: `counsel` = enrolled advocate or foreign counsel; `representative` = non-advocate. Both sign in at `/counsel/login` (one Representatives portal). `representative_type` stays on the authority record. |
| S-R9 | NN-27 lists "sign" as a representative scope; IT Act 2000 s.1(4) read with the First Schedule excludes a "power-of-attorney as defined in section 1A of the Powers-of-Attorney Act, 1882" from electronic signature, and s.1A defines a power-of-attorney as "any instrument empowering a specified person to act for and in the name of the person executing it" [K]. An e-signed authority to **sign instruments in the party's name** is therefore at risk of being a power-of-attorney that cannot be validly e-signed. | **Decision S-D1:** the e-signed Letter of Authority (LoA) may grant every scope except `sign_instruments_on_behalf`. That scope is enabled only on upload and verification of a **physically executed, stamped (state stamp law) and notarised power-of-attorney** (NN-08, NN-09), or for an organisation, a board resolution/authority under FR-P01-19 (corporate authority, not a PoA). Individual parties otherwise sign settlements themselves. **[VERIFY — open: counsel to confirm whether a platform LoA limited to procedural acts (file, attend, receive notices, negotiate) is outside Powers-of-Attorney Act 1882 s.1A, and the stamp treatment of such an LoA under state Stamp Acts (Indian Stamp Act 1899 Sch. I Art. 48 and state equivalents)]**. |
| S-R10 | D2-05 names "Committee members" but master §1.5 has no committee portal route. | New portal `/committee/login` (§2.10) for `committee_member` and `committee_chair`. |

---

## 1. Identity backbone recap

### 1.1 Components (P01 FR-P01-01 to FR-P01-11 — unchanged)

| Component | Specification (source) |
|---|---|
| Identity provider | Keycloak ≥ 26.4, one realm `equator`, Keycloakify themes on `auth.equatorresolution.in`; custom authenticators (OTP, magic link, DigiLocker/Aadhaar App linking, risk) call the `identity` module over mTLS (FR-P01-01). |
| Web session | Next.js BFF, Authorization Code + PKCE server-side, `__Host-eq_sess` cookie, CSRF token on mutations (FR-P01-01). |
| Mobile session | `expo-auth-session` in the system browser, DPoP-bound tokens, hardware key binding (FR-P01-10; P12 FR-P12-03 to -06). |
| Request context | Gateway-signed `Equator-Context: tenant=…; role=…[; case=…]` validated against `core.memberships` (FR-P01-02; master X-01). |
| Authentication assurance | `eq:aal1`, `eq:aal2`, `eq:aal3` (FR-P01-03), plus v2 qualifier `eq:aal2-pr` = aal2 achieved with a **phishing-resistant** authenticator (WebAuthn passkey with user verification, or federated SSO whose `amr` asserts `hwk`/`swk` with `mfa` and the IdP is on the phishing-resistant allow-list). Required for staff, committee, platform admin and every arbitrator signing action (§2). Reference: NIST SP 800-63B-4 (2025) definition of phishing resistance **[K]**. |
| Identity assurance | K0–K3 (FR-P01-14), with the v2 method set and action table in §3.1–§3.2. |
| Authorisation | Cerbos (ADR-0004) evaluating RBAC + ABAC on every request; Postgres RLS as a second line (F.2). Matrix in §6. |
| Audit | Every login, step-up, context switch, KYC decision, representation change and break-glass event writes a hash-chained audit event (NN-22); `audit.access_log` for every sealed/high-tier read (F.5). Login logs retained ≥ 1 year (DPDP Rules 2025 r.6(1)(e)) and ≥ 180 days within India (CERT-In Directions No. 20(3)/2022-CERT-In, 28 Apr 2022, para (iv)) **[K]**; clocks synchronised to NIC/NPL NTP (same Directions, para (i)). |

### 1.2 The identity graph

```
core.persons (natural person, global) ──1:1── core.users (login identity; kind human|machine)
      │                                           │
      │                                           ├── core.memberships (tenant × role_code; long-lived)
      │                                           └── core.role_grants (case/proceeding/time-bound; counsel, auditor, break-glass, delegation)
      ├── core.kyc_checks / identity level K0–K3
      ├── core.professional_credentials (Bar, foreign bar, ICAI, ICSI, IBBI, …)
      └── core.party_representatives (authority as representative) ─── core.case_parties (the party represented)
core.organisations ── core.org_signatories (authority matrix FR-P01-19) ── core.kyb_checks
core.law_firms (v2) ── core.firm_memberships (v2)
```

One natural person has **one** person record and **one** consumer login identity, regardless of how many portals they use. A retired judge who is a Grade A arbitrator, a mediator on the FAM panel, a committee member and also a party in a family property matter signs in once; the portal they enter decides the **default role space** and the authentication policy; the role switcher (SCR-P01-38) moves between spaces, applying step-up where the target space requires stronger assurance.

### 1.3 Workforce identities are separate (decision S-D2)

Equator employees and contracted staff (`case_manager`, `registrar`, `deputy_registrar`, `case_counsel`, `panel_manager`, `escrow_officer`, `safeguarding_lead`, `quality_officer`, `finance_controller`, `legal_reviewer`, `compliance_officer`, `support_agent`, `tech_concierge`, `dpo`, `cms_editor`, `growth_manager`, `platform_admin`) hold a **workforce account** federated from the Equator workforce IdP (Microsoft Entra ID or Google Workspace — ADR-0003a) and brokered by Keycloak. `core.users.kind = 'human'` with v2 column `is_workforce = true`. Rules:

1. A workforce account can never hold a party, counsel, representative or neutral role; a staff member who is personally a party uses a separate consumer account.
2. If both accounts belong to the same natural person, the DPO links them (`core.person_links`, §8.1). The link creates an automatic **access conflict**: the workforce account is denied every case in which the linked person (or a close relative declared in the staff conflict declaration, FR-P01-27) is a party, counsel or neutral, and cannot be assigned to it (`CONFLICT_DETECTED`).
3. Leaving Equator: SCIM `active=false` or IdP disablement revokes memberships and sessions within 60 s (FR-P01-07).

### 1.4 Portal registry (configuration, not code)

Each login portal is a row in `core.login_portals` (§8.1) and a Keycloak OIDC client with its own **authentication-flow override** (Keycloak per-client "Authentication flow overrides" for browser flow) and Keycloakify theme variant. Changing a portal's methods, minimum assurance or copy is a Ruleset Studio change (config kind `login_portal`, risk class `elevated`, maker–checker, NN-21). Platform guardrails (cannot be lowered by any tenant): staff, committee and platform-admin portals require `eq:aal2-pr`; neutral portals require `eq:aal2`; SMS OTP is never accepted as a second factor in those portals.

### 1.5 Post-login portal gate (algorithm)

```
on OIDC callback for portal P:
  memberships = active memberships of user (tenant-filtered by host for tenant domains)
  eligible = memberships where role_code ∈ P.allowed_roles
  if eligible is empty:
      if user has pending neutral application and P ∈ {mediator, arbitrator}: route to application tracker
      elif user has any membership: show "Wrong door" page listing the portals the user CAN use (no role names of others)
      else: party portal only → create K0 party context (P = parties) ; other portals → PORTAL_ROLE_MISMATCH
  if session acr < P.min_acr or auth_age > P.max_auth_age: step-up (STEP_UP_REQUIRED, required_acr)
  if P.network_policy or P.device_policy fails: deny (NETWORK_POLICY_DENIED / DEVICE_POLICY_DENIED)
  select default context = P.default_role preference ∩ eligible (last used per device wins)
  write audit identity.portal.signed_in (portal_code, acr, amr, role chosen); redirect to P.dashboard_route
```

The gate runs after authentication, so the "Wrong door" page may name the user's own portals without leaking anything to an unauthenticated visitor. Before authentication, every portal returns identical responses for unknown and known identifiers (P01 §10 anti-enumeration).

---

## 2. Separate login portals (D2-05, R-07)

### 2.0 Portal registry (seed rows of `core.login_portals`)

| Code | Route (vanity, on `equatorresolution.in`) | OIDC client | Allowed roles | Login methods (order shown) | Min ACR at login | Web idle / absolute | Mobile | Lands on |
|---|---|---|---|---|---|---|---|---|
| `parties` | `/login` | `eq-portal-parties` | `party`, `party_org_user` (+ K0 auto-context) | Mobile OTP · email link · DigiLocker · Aadhaar App (flag) · passkey (optional) · org SSO (org users) | aal1 | 30 min / 12 h | Party space | `/app` (SCR-S-D01) |
| `counsel` | `/counsel/login` | `eq-portal-counsel` | `counsel`, `representative` | Passkey · password + TOTP · mobile OTP + device-bound key (aal2) · firm SSO | aal2 | 15 min / 12 h | Party space (representative mode) | `/app/counsel` (SCR-S-D02) |
| `mediator` | `/mediator/login` | `eq-portal-neutral` (`kc_variant=mediator`) | `neutral_mediator`, `neutral_conciliator`, `neutral_facilitator` (assisted negotiation, v2.1), `neutral_expert` (+ applicants) | Passkey · password + TOTP | aal2 | 15 min / 12 h | Neutral space | `/app/neutral?space=mediation` (SCR-S-D03) |
| `arbitrator` | `/arbitrator/login` | `eq-portal-neutral` (`kc_variant=arbitrator`) | `neutral_arbitrator`, `neutral_expert` (+ applicants) | Passkey · password + TOTP | aal2 (aal2-pr for signing) | 15 min / 12 h | Neutral space | `/app/neutral?space=arbitration` (SCR-S-D04) |
| `staff` | `/staff/login` (redirects to `console.equatorresolution.in`) | `eq-portal-staff` | Workforce roles (§1.3) except `platform_admin` | Equator workforce SSO only (phishing-resistant MFA asserted) | aal2-pr | 15 min / 10 h | Staff tab in neutral space (case_manager only, P12) | `/console` (SCR-S-D05/06) |
| `enterprise` | `/enterprise/login` | `eq-portal-enterprise` | `enterprise_admin`, `enterprise_operator`, `grievance_officer`, `internal_ombudsman`, `university_admin`, `sgrc_member`, `grc_member`, `student_ombudsperson`, IC roles (sealed entry) | Org SSO (enforced on verified domains) · password + TOTP/passkey (non-SSO tenants) | aal2 | 15 min / 12 h (IC 10 min / 8 h) | Enterprise-lite space | `/app/enterprise` or `/app/grm` (SCR-S-D08/09) |
| `chambers` | `/chambers/login` and `{tenant}.chambers.equatorresolution.in/login` or custom domain | `eq-portal-chambers-{slug}` | `chambers_admin` + tenant-scoped neutral/staff roles of that chambers tenant | Passkey · password + TOTP · chambers SSO | aal2 | 15 min / 12 h | Neutral space (tenant-branded variant) | `/app/chambers` (SCR-S-D10) |
| `partners` | `/partners/login` | `eq-portal-partners` | `partner` | Mobile OTP + device key / password + TOTP · passkey | aal2 | 15 min / 12 h | Not in v1 (web/PWA) | `/partners` (SCR-S-D11) |
| `committee` | `/committee/login` | `eq-portal-committee` | `committee_member`, `committee_chair` | Passkey (hardware or platform, attested) · password + TOTP only during first-week enrolment | aal2-pr | 10 min / 8 h | Content-free push only | `/committee` (SCR-S-D07) |

Other entries (built in their own phases, listed here so the registry is complete): respondent notice link `/r/{code}` (P01 FR-P01-13 — not a login portal; possession check only) · Academy `/academy/login` and Campus `/campus/login` (P10; learner/student/trainer) · GRM white-label complainant portal `{slug}.grievance.equatorresolution.in` (P09; reference + OTP) · Platform admin `admin.equatorresolution.in/login` (`eq-portal-admin`; `platform_admin`, `dpo`, `auditor`, `legal_reviewer` for platform scope; aal3 for elevation, FR-P01-34) · Developer portal `developers.equatorresolution.in` (P09; machine credentials are never issued through a human portal).

**Why separate portals and not one form with a role picker.** (a) Different minimum assurance is enforced before any role data loads (staff and committee never fall back to OTP); (b) each audience gets copy in its own vocabulary at ≤ class-8 reading level for parties; (c) phishing campaigns that imitate one portal cannot harvest professional credentials through the party form, because professional portals have no OTP-only path; (d) analytics and abuse controls are tuned per audience (OTP pumping protection only where OTP exists).

### 2.1 Common layout, components and rules (all portals)

| Element | Specification |
|---|---|
| Desktop layout (≥ 1024 px) | Two columns. Left 40%: brand panel with portal headline (H1), one-liner, three trust bullets, illustration (decorative, `alt=""`), legal-entity footer line "Equator Resolution Service Private Limited · CIN {tenant.legal_entity.cin}". Right 60%: form card max-width 440 px, vertically centred. |
| Tablet / mobile web (< 1024 px) | Single column: compact header (logo, language switcher), H1, form card, then the trust bullets collapsed under "Why sign in here?". |
| Header | Logo (links to public home) · LanguageSwitcher (12 locales, native script) · "Not the right sign-in?" link opening the portal chooser (lists all portals by audience in plain words). |
| Form card | Method buttons stacked in the portal's configured order; primary method expanded by default; one primary action per step ("Continue"); "Back" link on every step after the first. |
| Footer | Help link (portal-specific help article), Privacy notice, Terms, Grievance Officer contact, Status page, "Equator is not a court" line on party and representative portals (GX-4). |
| Accessibility | WCAG 2.2 AA (NN-23); labels as visible text; `autocomplete` tokens (`username`, `current-password`, `one-time-code`, `webauthn`); errors in an ErrorSummary that receives focus; no CAPTCHA on first attempt — risk-based challenge (hCaptcha with audio alternative) only after throttling thresholds; accessible authentication without cognitive tests (WCAG 3.3.8): passkeys and copy-paste of codes always allowed. |
| Performance | ≤ 150 KB first load (P01 §6); works on 3G; no third-party scripts except the IdP and the risk-challenge provider. |
| Anti-enumeration | Identical response and timing (±50 ms) for known and unknown identifiers on every step (P01 §10). |
| Brand | Tenant domain shows tenant branding (P00 `core.tenant_branding`); professional portals never show party marketing; no "court", "judge", "decree" wording (GX-4, NN-17). |

**Common recovery entry.** Every portal shows "Can't sign in?" → `/account/recover?portal={code}` (SCR-P01-43), which applies the persona-class rule in P01 FR-P01-11 for that portal's audience.

### 2.2 Parties and litigants — `/login`

| Item | Specification |
|---|---|
| Audience | Individuals and organisational party users who filed, were served a notice, or were invited by a co-party or enterprise. |
| Layout | §2.1. Above the method buttons, a prominent card: **"Got a notice from us?"** → `/r/enter` (enter the 8-character code printed on the notice or open the link) — routes into FR-P01-13. |
| Fields and methods | (1) **Mobile number** (country code default +91; `^\+91[6-9]\d{9}$` for India; E.164 for others) → channel choice WhatsApp / SMS → OTP (6 digits; P01 FR-P01-04). (2) **Email** → magic link (FR-P01-05). (3) **Continue with DigiLocker** (flag `release.auth.digilocker_login`; FR-P01-08). (4) **Continue with the Aadhaar App** (flag `kyc.aadhaar_ovse.enabled`; login only after the Aadhaar App identity has been linked to an account through an OTP-verified contact point; §3.3). (5) **Use a passkey** (shown if a passkey exists on the device — WebAuthn conditional mediation). (6) **Organisation login (SSO)** link for `party_org_user` on SSO tenants. |
| Step-up rules | aal1 suffices to view notices, drafts, case status and documents of the user's own case. aal2 (`auth_time` ≤ 5 min) to: e-sign anything; pay ≥ ₹10,000 (configurable); change bank account (+ 24-hour cooling-off); withdraw a sealed-purpose consent; grant, narrow or revoke a representative's authority; download a DSR export. aal2 on a party account = OTP + device-bound key (mobile) or OTP + passkey/TOTP (web). |
| Identity level gates | §3.1 (K0 view; K1 file/respond; K2 sign/receive money). |
| Recovery | P01 FR-P01-11 party row (other verified contact + DigiLocker or Aadhaar App re-verification; assisted video recovery; 72-hour hold on contact change). |
| Copy | Headline: **"Sign in to your case"**. One-liner: "Use your mobile number or email. No password needed." Trust bullets: "Your Aadhaar number is never stored." · "Only people in your case can see it." · "Available in English and 11 Indian languages." Help text under mobile field: "We will send a 6-digit code. It is valid for 5 minutes." Help under email: "We will email you a sign-in link. It works once, for 15 minutes." |
| Errors (en; i18n keys `login.parties.*`) | Invalid number: "Enter a 10-digit Indian mobile number, or choose another country." · Too many codes: "You have asked for too many codes. Try again after {time}." (`RATE_LIMITED`) · Wrong code: "That code is not right. You have {n} tries left." · Code expired: "That code has expired. Send a new one." · Locked: "Too many wrong codes. Try again in 30 minutes or use your email instead." (`OTP_LOCKED`) · DigiLocker cancelled: "You did not finish in DigiLocker. You can try again or use your mobile number." · Provider down: "We cannot reach DigiLocker right now. Use your mobile number instead." (`PROVIDER_UNAVAILABLE`). |
| Mobile variant | App welcome (SCR-P01-M02) shows four large tiles: "I have a notice" · "I want to resolve a dispute" · "I represent someone" (→ counsel portal client) · "I am a mediator or arbitrator" (→ neutral client). OTP autofill via Android SMS Retriever and iOS one-time-code; biometric unlock after first login (P12 FR-P12-04). |

### 2.3 Representatives and advocates — `/counsel/login`

| Item | Specification |
|---|---|
| Audience | Advocates (`counsel`), foreign counsel (`counsel`, `representative_type = foreign_counsel`), non-advocate authorised representatives (`representative`): family member, company officer, HR officer, union representative, CA/CS acting in mediation or GRM where the rules permit (§4.1). |
| Fields and methods | **Passkey** (primary, "Sign in with a passkey"); **Email + password** then second factor (passkey, TOTP, recovery code); **Mobile OTP + device-bound key** (mobile app only; counts as aal2); **Firm SSO** for firm tenants with a verified domain (§4.6). No email-link-only or OTP-only login (representatives act for others; aal1 is not enough). |
| Step-up rules | aal2 at login. Re-authentication (`auth_time` ≤ 5 min) to: file a pleading or response on behalf of a client; accept or make an offer under authority; sign anything (only where scope permits — S-D1); accept a new mandate; add/remove firm members. |
| Gate after login | Role `counsel` or `representative` required. A person with a pending Bar verification may sign in and act under active authorities with the badge "Enrolment not verified" (FR-P01-22). First sign-in without any role routes to SCR-P01-24 (enrolment / representative profile). |
| Recovery | Professional row of FR-P01-11 (recovery code or second factor; else firm admin-initiated reset + liveness against KYC photo). |
| Copy | Headline: **"Sign in to represent your clients"**. One-liner: "For advocates and authorised representatives acting under a Letter of Authority." Trust bullets: "Every action is within the authority your client signed." · "Clients can see and change your authority at any time." · "Verified enrolment badge on every case." Help: "First time? Ask your client to invite you from their case, or request authority from the case page." |
| Errors | No role: "This sign-in is for representatives. If you are a party to a case, use Parties sign-in." (`PORTAL_ROLE_MISMATCH`) · Second factor required: "Use your passkey or authenticator code to continue." · Authority expired (after login, on a case): "Your authority for this case ended on {date}. Ask your client to renew it." (`MANDATE_EXPIRED`). |
| Mobile variant | Party space in "representative mode": tab bar Home · Matters · Messages · Profile; client switcher at the top of Matters; every action button shows the scope chip ("Your authority allows: attend, receive notices"). |

### 2.4 Mediators — `/mediator/login`

| Item | Specification |
|---|---|
| Audience | Empanelled mediators and conciliators (Grades A/B/C, Appendix N), neutral experts, POSH external members who are also on Equator's panel, and applicants with an open application. |
| Shared identity | Same OIDC client as arbitrators (`eq-portal-neutral`) with theme variant `mediator`; one account per neutral; the variant sets `default_space=mediation` and the role preference `neutral_mediator` > `neutral_conciliator` > `neutral_expert`. |
| Fields and methods | Passkey (primary); email + password + TOTP/passkey. SMS OTP may be used **only** for recovery, never as a second factor. Grade A neutrals may request assisted enrolment of a hardware security key by a `tech_concierge` over video (the concierge never sees credentials; enrolment completes on the neutral's own device). |
| Step-up rules | aal2 at login. aal2 with `auth_time` ≤ 10 min to open caucus notes (NN-11) and sealed safeguarding summaries; aal2 ≤ 5 min to authenticate a settlement or sign a mediator's report; payout bank change web-only with 24-hour cooling-off (P12 §3). |
| Gate after login | If the person holds no mediation-type role but an arbitrator role: "You are on our arbitrator panel. Continue to your arbitration workspace?" If an application is open: route to the application tracker (P03). |
| Copy | Headline: **"Mediator workspace sign-in"**. One-liner: "Your sessions, agreements and notes — confidential by design." Trust bullets: "Caucus notes are visible only to you." · "Mediation sessions are never recorded." · "Join from web or the Equator app." |
| Errors | Second factor missing: "Mediators must use a passkey or authenticator app. Set one up to continue." · De-empanelled/suspended: "Your panel membership is not active. Contact the Panel Manager at {email}." (`FORBIDDEN`, sub-code `NEUTRAL_NOT_ACTIVE`). |
| Mobile variant | Neutral space: Today · Cases · Calendar · Messages · Profile (P12 FR-P12-21); Today opens on mediation sessions first. |

### 2.5 Arbitrators — `/arbitrator/login`

| Item | Specification |
|---|---|
| Audience | Empanelled arbitrators (sole, co-arbitrator, presiding, emergency, appellate tier), and party-nominated co-arbitrators from outside the panel in equal-footing `COM`/`INT` matters (NN-03 exception) who are given a **case-scoped** `neutral_arbitrator` role grant after confirmation by the Appointments Sub-Committee (Case Bench) (Appendix N §1.3). |
| Shared identity | `eq-portal-neutral`, variant `arbitrator`; `default_space=arbitration`. |
| Fields and methods | As §2.4; for outside nominees, first login completes K2 + passkey enrolment before the disclosure form (FR-P03 disclosure). |
| Step-up rules | **aal2-pr** (passkey) with `auth_time` ≤ 5 min to sign an award, an order terminating proceedings, a s.29A-related order or an arb-med sealed award (master §5.3); aal2 ≤ 10 min to open the sealed award vault; disclosure submissions at aal2. TOTP-only arbitrators can do everything except sign — signing prompts passkey enrolment. |
| Copy | Headline: **"Arbitrator workspace sign-in"**. One-liner: "Pleadings, hearings, orders and awards in one secure place." Trust bullets: "Statutory timelines tracked for you (s.29A)." · "Disclosures and appointments on record." · "You decide; drafting tools only assist." |
| Errors | As §2.4; plus "Your appointment in {case} has ended. You can still read the record for {n} days." (read-only grant). |
| Mobile variant | Neutral space; award signing on mobile only via Aadhaar eSign/virtual sign with biometric step-up (P12 FR-P12-16); DSC signing web-only. |

### 2.6 Case managers and staff — `/staff/login`

| Item | Specification |
|---|---|
| Audience | All workforce roles in §1.3 except `platform_admin` (who uses `admin.equatorresolution.in`). |
| Methods | Workforce SSO only (OIDC to Entra ID / Google Workspace via Keycloak identity brokering). Keycloak accepts the brokered login only if the IdP token's `amr` includes a phishing-resistant method (`hwk` or `swk` with `mfa`; FIDO2/WebAuthn) — configured as an IdP mapper that sets `acr = eq:aal2-pr`; otherwise login fails (`PHISHING_RESISTANT_MFA_REQUIRED`). Two named break-glass staff accounts with hardware keys held in a sealed envelope procedure (`docs/runbooks/staff-breakglass.md`). |
| Network policy | `core.network_policies`: allow-list of office egress IPs (Delhi, Noida, Jaipur) and the ZTNA/VPN egress range. Outside the allow-list: deny for `escrow_officer`, `finance_controller`, `safeguarding_lead`, `dpo`; for other staff, allow only with aal2-pr re-authentication ≤ 15 min and read-only on sealed/high tiers. |
| Device policy | Managed devices only for consoles that can open sealed or financial data: the IdP must assert device compliance (Entra `deviceid` + compliant claim, or Google endpoint verification), or the browser presents an MDM-issued client certificate (mTLS at the ALB for `console.equatorresolution.in`). Non-compliant device: read-only standard-tier access; no export, no download (`DEVICE_POLICY_DENIED` for blocked actions). |
| Step-up rules | aal2-pr ≤ 10 min for sealed entries, maker–checker approvals (NN-21), escrow release (dual control), payout approval, KYC/KYB decisions, export of any case data, break-glass requests (§6.6). |
| Session | Idle 15 min; absolute 10 h; concurrent sessions 2; session bound to device fingerprint and IP /24; IP change outside allow-list forces re-authentication. |
| Copy | Headline: **"Equator staff sign-in"**. One-liner: "Sign in with your Equator work account." Help: "Use your work security key or passkey. Personal accounts cannot be used here." No trust bullets; display the acceptable-use banner: "Access is logged. Use only for assigned work. Unauthorised access is an offence under the Information Technology Act 2000." |
| Errors | Non-workforce email: "Use your Equator work account." · No phishing-resistant MFA: "Your sign-in did not use a security key or passkey. Sign in again with one." · Network: "You are outside an approved network. Connect to the Equator VPN." · Device: "This device is not managed by Equator. You can view, but cannot change or download." |
| Mobile variant | Only `case_manager` gets the staff tab in the neutral space (P12 §3), via the same workforce SSO in the system browser; sealed tiers blocked on mobile. |

### 2.7 Enterprise (lenders, insurers, employers, listed companies, universities) — `/enterprise/login`

| Item | Specification |
|---|---|
| Audience | `enterprise_admin`, `enterprise_operator`, `grievance_officer`, `internal_ombudsman`, `university_admin`, `sgrc_member`, `grc_member`, `student_ombudsperson`; IC members enter the sealed workspace from here. |
| Methods | **"Continue with your organisation account"**: work email → home-realm discovery (Keycloak Organizations, verified domain) → tenant IdP (SAML 2.0 or OIDC; FR-P01-07). Tenants without SSO: email + password + passkey/TOTP. When "Enforce SSO" is ON, password login is refused for that domain except for 2 break-glass admins (FR-P01-07). |
| Step-up rules | aal2 at login (IdP must assert MFA — `amr` contains `mfa`, else Keycloak adds its own TOTP/passkey step). aal2 ≤ 10 min for: bulk-batch commit; offer approval within authority; API key and webhook changes; SSO configuration (FR-P01-07); IC sealed entry (passkey or TOTP only; SMS never; FR-P01-30). |
| Gate after login | Role decides landing: GRO/IO/SGRC/GRC → `/app/grm`; IC roles → sealed entry interstitial (SealedBanner + QuickExit + step-up) then `/app/posh`; others → `/app/enterprise`. **No enterprise landing page lists neutrals with select, rank or veto controls (NN-03).** |
| Copy | Headline: **"Organisation sign-in"**. One-liner: "For lenders, insurers, employers, universities and listed companies using Equator." Trust bullets: "Single sign-on with your company account." · "Grievance clocks and escalations in one desk." · "Neutrals are appointed independently — never by clients." Help: "Use your work email. If your company uses single sign-on, we will send you to its login page." |
| Errors | Unknown domain (generic, no tenant enumeration): "We could not find a sign-in for that email. Check it, or ask your administrator." · SSO enforced: "Your organisation requires its own login. Continue with your organisation account." (`STEP_UP_REQUIRED` sub-code `EQ-AUTH-011`) · Unmapped group: "You do not have a role yet. Ask your administrator." |
| Mobile variant | Enterprise-lite space: Queue · SLA · Escalations · Insights (P12 FR-P12-22); IC: content-free push only, web after step-up. |

### 2.8 Private ADR Chambers — `/chambers/login`

| Item | Specification |
|---|---|
| Audience | `chambers_admin` and the chambers tenant's own neutrals/staff (tenant-scoped roles). Each chambers tenant has its own OIDC client `eq-portal-chambers-{slug}` and branding; the vanity route `/chambers/login` first asks "Which chambers?" (search by name; only tenants that opted into public listing appear; others reach their portal only through their own domain). |
| Methods | Passkey; email + password + TOTP/passkey; chambers SSO (OIDC/SAML) on paid plans that include it (Appendix O plan matrix). |
| Step-up rules | As neutral portals for neutral actions; aal2 ≤ 10 min for fee schedule publication, member/role changes, branding publication, data export. |
| Copy | Headline: **"Sign in to {Chambers display name}"** (tenant label, default "Private ADR Chambers"; never "Court" unless the D2-16 counsel review is on record). One-liner: "Powered by Equator Resolution." Help: "Your chambers administrator manages your access." |
| Errors | Tenant suspended (billing or compliance): "This workspace is paused. Open cases and deadlines continue; contact your administrator." (Appendix O dunning rules: never block existing cases.) |
| Mobile variant | Neutral space with tenant-branded variant only if the tenant bought a white-label app (P12 FR-P12-01); otherwise the Equator app with tenant branding band. |

### 2.9 Partners — `/partners/login`

| Item | Specification |
|---|---|
| Audience | `partner` (CA, CS, CMA, law firm, advocate (BCI-compliant mode), HRMS vendor, DSA, university, association). Partner records live in the `growth` schema (FR-P01-33). |
| Methods | Passkey; email + password + TOTP; mobile OTP + passkey. aal2 at login. |
| Data boundary | Partner sessions carry a `growth` audience token only; the API rejects partner tokens on every case-context resource (`CASE_DATA_TO_GROWTH_FORBIDDEN`; NN-16). Referral status is the only case-derived signal and it is a coarse enum (`invited`, `registered`, `case_opened`, `closed`) with no party names. |
| Copy | Headline: **"Partner sign-in"**. One-liner: "Track referrals, clause adoption and statements." Trust bullet: "Partner status never affects who decides a case." Advocates see: "Advocate partners receive credits or co-counsel opportunities only — no cash commission (Bar Council of India rules)." |
| Errors | Application pending: "Your partner application is under review. We will email you within 5 working days." |
| Mobile variant | None in v1 (responsive web/PWA). |

### 2.10 Committee members — `/committee/login`

| Item | Specification |
|---|---|
| Audience | `committee_member`, `committee_chair` of the Equator Institutional Committee and its Appointments, Challenge, Scrutiny, Ethics & Complaints, Rules, AI Oversight and Transparency sub-committees (D2-15; Appendix N §1). Majority are external persons. |
| Methods | **Passkey only** after a one-week enrolment grace (during which password + TOTP is accepted); attested authenticators preferred (hardware key issued by the Registrar on appointment). aal2-pr at login. No SSO (external members have no common IdP). |
| Step-up rules | aal2-pr ≤ 5 min to vote, sign a decision, or record a recusal; aal2-pr ≤ 10 min to open a challenge file or ethics complaint file. |
| Gate and scoping | Membership is per sub-committee (`core.memberships.org_unit_id` = sub-committee); access to a matter requires a `role_grant` created by the Registrar's agenda for that meeting and is blocked automatically when the member has a declared or detected conflict (§6.5). |
| Copy | Headline: **"Institutional Committee sign-in"**. One-liner: "Agendas, papers and decisions for committee members." Banner: "Committee papers are confidential. Downloads are watermarked with your name." |
| Errors | Recused: "You have recused yourself from this matter. Papers are not available to you." (`CONFLICT_DETECTED`). |
| Mobile variant | Content-free push ("New papers for the {sub-committee} meeting on {date}") → web after step-up. |

### 2.11 Mobile portal mapping (P12)

The single binary (P12 FR-P12-01) maps portals to OIDC clients at sign-in: the welcome tiles (§2.2) select `eq-portal-parties`, `eq-portal-counsel` or `eq-portal-neutral`; "I work for an organisation" selects `eq-portal-enterprise`; staff (case managers) use "Equator staff" under "More sign-in options", which opens `eq-portal-staff`. Committee, partner, platform-admin and chambers-admin portals are not offered in the app in v1. A user signed in through one client who switches to a space whose portal has a stronger policy triggers step-up in the system browser (no embedded web views).

### 2.12 Login error catalogue (all portals)

| Situation | Canonical code (F.10) | Sub-code (`rule`) | HTTP | Message (en) — i18n key `errors.<code>` |
|---|---|---|---|---|
| Bad credentials (any method) | `UNAUTHENTICATED` | `EQ-AUTH-001` | 401 | "Those details did not work. Check and try again." |
| OTP expired | `UNAUTHENTICATED` | `EQ-AUTH-002` | 401 | "That code has expired. Send a new one." |
| OTP attempts exceeded | `OTP_LOCKED` | `EQ-AUTH-003` | 429 | "Too many attempts. Try again in 30 minutes." (P01 FR-P01-04 lockout is 30 min; F.10.1 text "15 minutes" is corrected to read the configured value `{minutes}`) |
| Send rate limit | `RATE_LIMITED` | `EQ-AUTH-004` | 429 | "Too many requests. Try again after {time}." |
| Step-up needed | `STEP_UP_REQUIRED` | `EQ-AUTH-010` | 401 | "Confirm it's you to continue." |
| SSO enforced for domain | `STEP_UP_REQUIRED` | `EQ-AUTH-011` | 401 | "Your organisation requires its own login." |
| Refresh token reuse | `UNAUTHENTICATED` | `EQ-AUTH-012` | 401 | "For your safety we signed you out. Sign in again." |
| Portal does not serve the user's roles | `PORTAL_ROLE_MISMATCH` (new) | — | 403 | "This sign-in is for {audience}. Use {portal link} instead." |
| Phishing-resistant MFA missing | `PHISHING_RESISTANT_MFA_REQUIRED` (new) | — | 401 | "Sign in again with your security key or passkey." |
| Network policy | `NETWORK_POLICY_DENIED` (new) | — | 403 | "You are outside an approved network." |
| Device policy | `DEVICE_POLICY_DENIED` (new) | — | 403 | "This device cannot be used for this action." |
| Account suspended | `FORBIDDEN` | `ACCOUNT_SUSPENDED` | 403 | "Your account is paused. Contact support at {email}." |
| Identity level too low | `KYC_REQUIRED` | `EQ-AUTH-020` | 409 | "Verify your identity to continue. It takes about 2 minutes." |
| Guardian consent pending | `GUARDIAN_CONSENT_REQUIRED` | `EQ-AUTH-040` | 409 | "A parent or guardian needs to approve your account first." |
| Provider outage | `PROVIDER_UNAVAILABLE` | `EQ-KYC-001` | 503 | "{Provider} is not responding. Try another way to sign in." |

---

## 3. Onboarding and verification integrations (R-12; D2-06; S7 §2)

### 3.1 Identity levels by action risk (config kind `assurance_policy`; defaults)

| Action (`assurance_policy.actions.*`) | Identity level | Auth level | Additional condition |
|---|---|---|---|
| Use Dispute Explorer, read public pages, start a draft | none | — | — |
| Open own notice, read own case documents, check status | K0 | aal1 | Possession of the notified contact (FR-P01-13) |
| File a claim; submit a response; upload evidence; pay a fee | K1 | aal1 (aal2 if payment ≥ ₹10,000) | — |
| Grant / narrow / revoke a representative's authority | K1 | aal2 ≤ 5 min | §4 |
| Make or accept an offer; agree to mediate; sign an arbitration agreement | K1 | aal2 ≤ 5 min | Org: signatory authority (FR-P01-19) |
| E-sign a settlement, consent award request, s.12(5) waiver, LoA | K2 | aal2 ≤ 5 min | NN-03 for waivers (party personally) |
| Receive a refund, settlement disbursal or payout | K1 + verified bank (§3.11) | aal2 | 24-hour cooling-off after bank change |
| Join an arbitration hearing | K1 | aal1 | Liveness at join where the tribunal directs (P04) |
| Representative acts on a case | K1 + credential status ≠ `rejected` | aal2 | Active authority with the scope (§4.3) |
| Neutral application; IC external member; committee member | K2 | aal2 / aal2-pr | — |
| `INT` signatory | K2 + sanctions clear | aal2 | K3 if risk score ≥ 70 (FR-P01-21) |
| FAM matter with safety flag; POSH complainant optional; tenant-required | K3 offered (voluntary unless tenant policy) | aal2 | Never a precondition for safety signposting |
| Any action when risk score ≥ 90 | — (restricted) | — | Manual review (FR-P01-21) |

Tenants may raise, never lower, these defaults (`RULESET_GUARDRAIL_VIOLATION`). A **respondent** who never verifies remains "unverified respondent" on the case; the proceeding continues on deemed-service rules (P02/P07), and the respondent's identity is never verified without the respondent's own action (S7 §7 Q3) **[VERIFY — open: DPDP s.17(1)(a) reach for respondent verification data]**.

### 3.2 Identity method chooser (SCR-P01-13, v2 order)

| Option key | Label (en) | Shown when | Level reached | Port / provider |
|---|---|---|---|---|
| `aadhaar_app_avc` | "Verify with the Aadhaar App (recommended)" | Indian resident; flag `kyc.aadhaar_ovse.enabled` ON (after OVSE registration) | K1; K2 with offline face verification | UIDAI Aadhaar App credential to Equator callback (direct) |
| `digilocker` | "Verify with DigiLocker" | Indian resident | K1 | `KYC_PORT` partner (Surepass; Digio fallback) → direct Requester later |
| `pan` | "Verify with PAN" | Indian resident or entity | K1 (name + DOB match) | `KYC_PORT` aggregator with OPV-channel warranty |
| `epassport_nfc` | "Scan your passport chip" | NRI/foreign; NFC-capable phone; mobile app | K1; K2 with liveness vs chip photo | On-device ICAO 9303 reader SDK |
| `passport_upload` | "Upload your passport for review" | Fallback | K1 after manual review | `KYC_PORT` OCR + SCR-P01-45 |
| `manual_id` | "Upload another ID for review" | Fallback (voter ID, driving licence, OCI) | K1 after manual review | Same; never an unmasked Aadhaar image |
| `video_verify` | "Video verification with our team" | Tenant/FAM/INT policy, risk ≥ 70, or user choice | K3 | `VIDEO_PORT` (LiveKit) + agent (FR-P01-15) |

Order logic: Indian resident on mobile → Aadhaar App, DigiLocker, PAN, others; Indian resident on desktop → DigiLocker, Aadhaar App (QR shown on screen), PAN; NRI/foreign → passport chip (if app), passport upload, video. Screen copy above the list: "To respond formally you need to verify who you are. This takes about 2 minutes. We do not see or store your Aadhaar number."

### 3.3 Aadhaar through Offline Verification (OVSE) — the only Aadhaar route in v2

**Legality [K / V-s].** After *K.S. Puttaswamy v Union of India (Aadhaar-5J)* (2019) 1 SCC 1 (SC, 26 Sep 2018) struck down Aadhaar Act s.57, private use rests on: **s.4(4)** (online authentication only for an entity permitted by a Parliamentary law or prescribed by the Central Government "in the interest of State"); the Aadhaar Authentication for Good Governance (Social Welfare, Innovation, Knowledge) Rules 2020 as amended by **G.S.R. 88(E), 31 Jan 2025** (new r.3(1)(aa) "promoting ease of living of residents and enabling better access to services"; application through a sponsoring Ministry via the SWIK portal launched 27 Feb 2025); **s.8A** (offline verification); and **s.29** (restrictions on sharing and display of the Aadhaar number). Equator is **not** an AUA/KUA and performs **no** CIDR authentication or e-KYC (D2-06). It registers as an **Offline Verification Seeking Entity (OVSE)** under the Aadhaar (Authentication and Offline Verification) Regulations 2021 as amended by the **Amendment Regulations of 9 Dec 2025** **[VERIFY — open (counsel): notification HQ-30011/5/2025-AU-HO, in force 9 Dec 2025 (secondary sources; reg.13A OVSE registration for AVC/offline e-KYC via Aadhaar App) — obtain Gazette copy; fee amounts not published; retention of the signed credential not addressed — keep hash only]** [G.S.R. 88(E) of 31 Jan 2025 verified on eGazette]. OVSE registration is needed for offline e-KYC and Aadhaar Verifiable Credential (AVC) sharing via the Aadhaar App (dedicated 28 Jan 2026); not for viewing a physical/e-copy or plain QR — but Equator never accepts copies (below). A SWIK good-governance proposal through the Ministry of Law & Justice is a post-launch stretch item (S7-07), never a Phase 1 dependency.

**Flows.**

| Flow | Steps | Result |
|---|---|---|
| A. Aadhaar App credential (web) | (1) User chooses `aadhaar_app_avc`. (2) Equator creates a request (`POST /v1/kyc/aadhaar-ovse/requests`) listing only needed attributes: name, DOB (or age-band ≥ 18 for guardian checks), photo, gender (only where the case form needs it), state/district (never full address unless the notice address must be proven). (3) Screen shows a signed QR + 120-s countdown; user scans in the Aadhaar App, reviews the attributes, consents with the App's own PIN/biometric. (4) UIDAI-signed credential posted to the registered callback `https://api.equatorresolution.in/v1/kyc/aadhaar-ovse/callback`. (5) Server verifies the UIDAI signature chain and nonce binding; extracts allow-listed attributes; computes `credential_sha256`; discards the payload. | K1; `core.kyc_checks.method = aadhaar_app_avc`, `aadhaar_ref_masked = XXXXXXXX1234` only if the credential carries the last four digits |
| B. Aadhaar App credential (mobile, same device) | As A, with an app-to-app intent/universal link instead of the QR; return to Equator via App Link. | Same |
| C. Offline face verification | After A/B, the user completes the Aadhaar App's offline face verification (live face vs the photo in the holder's App). Where unavailable, Equator's own liveness (§3.12) runs against the **credential photo** received in A/B — never against an Aadhaar photo obtained any other way. | K2 |
| D. Offline e-KYC XML (legacy) | Offered only if the Aadhaar App flow is unavailable for the user: user downloads the paperless offline e-KYC ZIP from the UIDAI site with a share code, uploads it; server validates the UIDAI signature, reads allow-listed fields, then deletes the ZIP and share code within the transaction. | K1 |

**Masking and minimisation (NN-14).** Persist only: verification result, method, timestamp, issuer-signature validation result, `credential_sha256`, name, DOB (or age-band), photo (encrypted, deleted 30 days after the K2 decision unless the user consents otherwise), `aadhaar_ref_masked`. Never persist or log the 12-digit number, VID, QR payload, XML or share code. DB trigger rejects any 12-digit Verhoeff-valid value in any column (P01 §10); log scrubbers redact the pattern. Upload validator: any image classified as Aadhaar is OCR-checked; if the first 8 digits are unmasked the file is rejected (`AADHAAR_UNMASKED_DETECTED`) and the user is offered Flow A or DigiLocker (mobile pre-masking per P12 FR-P12-12). Purpose copy (all locales): "We verify your identity to make sure only the real parties take part in your case. We do not see or store your Aadhaar number." Retention of the verification record: case record life (8 years after closure) **[VERIFY — open: S7 Q2 — retention of hash + minimal fields by an OVSE for the case-record life]**.

**Prohibited (CI tests):** Aadhaar OTP e-KYC; biometric capture against CIDR; storing Aadhaar copies; using Aadhaar as a login identifier; asking for Aadhaar where another ID suffices (an alternative method must always be shown).

### 3.4 DigiLocker

Route: Phase 1 via licensed partner (`KYC_PORT` Surepass; Digio fallback); Phase 2 direct Requester onboarding under the DigiLocker Partner SOP (NeGD, 5 Jun 2024) to remove the aggregator as processor (S7-08). Documents offered (user picks each on the DigiLocker consent screen): masked Aadhaar, PAN, driving licence, education certificates (neutral applicants), e-EPIC where issued. DigiLocker-issued documents are treated as on par with originals under r.9A of the IT (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules 2016 **[K]**. Obligations carried into Equator controls from the Requester Terms of Use (2 Jun 2025): explicit consent before each fetch (cl.4(c), 6(b)); no caching or storage beyond the transaction unless law requires (cl.6(b)) — Equator keeps **verification attributes only** (name, DOB, masked ID, issuer, document URI, signature result, timestamp, hash), never the document image; India-only storage (cl.18); security incidents to NeGD within 24 hours (cl.4(e), 13) — wired into the breach workflow (Appendix Q); annual CERT-In-empanelled audit (cl.15); courts at New Delhi (cl.8). Where a party needs the document itself as evidence (e.g., driving licence in a motor `INS` claim), the party uploads it as evidence under a separate basis. **[VERIFY — open: S7 Q4 — whether retaining verification attributes for the case record is "required by law" under cl.6(b)]**.

### 3.5 PAN

Format `^[A-Z]{5}[0-9]{4}[A-Z]$`; 4th character: `P` individual; `C` company; `F` firm/LLP; `H` HUF; `T` trust; `A` AOP; `G` government; `L` local authority; `J` artificial juridical person (FR-P01-18). Verification through an aggregator that holds a Protean Online PAN Verification channel under its own eligible category, with the contract warranty in S7 §2.4 (ERSPL does not fall in a listed OPV category) **[V]**. Response used: PAN status (valid / deleted / deactivated / fake / not found), name match Y/N, DOB/incorporation match Y/N, PAN–Aadhaar link status (operative / inoperative). Stored: `pan_masked` (`ABCDE****F`), `pan_hmac`, encrypted PAN only where tax law needs it (neutral, trainer, partner payees; party GSTIN invoicing). Inoperative PAN on a payee raises the TDS higher-rate flag for P05 **[VERIFY — open: Income-tax Act 2025 section replacing s.206AA]**. Fallback: user-assisted "Verify your PAN" on the Income-tax e-filing portal with screenshot upload to manual review.

### 3.6 MCA21 company/LLP and DIN (KYB)

| Check | Source | Decision rule |
|---|---|---|
| CIN `^[LU][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$` / LLPIN `^[A-Z]{3}-[0-9]{4}$` | Aggregator MCA master-data API (Surepass "MCA Data APIs (V3)"; IDfy fallback); public master data under Companies Act 2013 s.399 | Name, status, incorporation date, registered office, ROC, directors/designated partners with DIN/DPIN |
| Status `Active` | — | Proceed |
| `Strike Off`, `Under process of striking off`, `Dormant`, `Amalgamated`, `Dissolved` | — | May be a party; flagged for case-manager review; cannot hold an enterprise subscription; claimant against a struck-off company sees revival-order guidance (Companies Act s.252) |
| `Under CIRP` | — | **Block filing a claim against it** and signpost: "This company is under insolvency proceedings. Claims against it generally go to the Resolution Professional. [Find out how]" (IBC 2016 s.14 moratorium) |
| `Under liquidation` | — | Block claim filing without NCLT leave (IBC s.33(5)); signpost to the liquidator |
| Signatory authority | DIN list + board resolution | Auto-pass if the signatory's DIN is a current director; else board resolution / PoA upload → KYB reviewer |
| DIN status "Deactivated due to non-filing of DIR-3 KYC" | DIN master | Warn; signatory may act only on a fresh board resolution signed by an active director |
| Foreign company in India | FCRN | Route to foreign KYB (§3.10, FR-P01-20) |
| Charges (FIN secured debt) | MCA index of charges | Prefill security details in the FIN claim form |

No official public commercial MCA API was found **[V-s/U]**; mitigations: manual "Fetch from MCA" fallback (user uploads the MCA master-data PDF; reviewer checks), 30-day cached snapshot with hash, and an aggregator contract warranty that access is lawful.

### 3.7 GSTIN

Format `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$`; state code (chars 1–2) and embedded PAN (chars 3–12) must match the organisation PAN. Source: GST public search via a GST Suvidha Provider/aggregator (registration under CGST Act 2017 s.25). Stored: legal name, trade name, status (Active / Cancelled / Suspended), constitution, principal place, registration date, return-filing status (last 6 periods). Cancelled GSTIN: proceed as party; B2B invoice falls back to unregistered-recipient treatment (Appendix B place-of-supply rule). Multi-state organisations add several GSTINs.

### 3.8 Udyam (MSME)

Format `^UDYAM-[A-Z]{2}-[0-9]{2}-[0-9]{7}$`; registration under MSMED Act 2006 s.8 read with Notification S.O. 2119(E), 26 Jun 2020 **[K]**. Verification: aggregator or Udyam portal public verify (number + OTP/captcha) with screenshot to manual review. Stored: Udyam number, enterprise name, category (micro/small/medium), NIC codes, date of registration. Effect: a micro or small supplier with a delayed-payment claim is shown the MSEFC route first (MSMED s.18; NN-20) and the feature-flagged MSEFC referral track (D2-26).

### 3.9 LEI (GLEIF)

ISO 17442, 20 characters, mod-97 check; GLEIF public API (`api.gleif.org`, CC0 data, free) for name, jurisdiction, registration status (`ISSUED`, `LAPSED`, `RETIRED`…), legal address and Level 2 direct/ultimate parent (used as a UBO hint and in neutral conflict checks, never as proof of UBO). Mandatory for `INT` organisations where an LEI exists (FR-P01-20); a `LAPSED` LEI is a warning, not a block.

### 3.10 Passport NFC/MRZ (NRIs and foreign parties)

| Step | Specification |
|---|---|
| MRZ | Camera OCR of the TD3 MRZ; validate check digits (document number, DOB, expiry, composite) per ICAO Doc 9303 Part 3 **[K]**; Indian passport number `^[A-Z][0-9]{7}$`. |
| NFC chip (mobile only) | Access with BAC/PACE keys derived from the MRZ; read DG1 (MRZ data) and DG2 (face image); **Passive Authentication**: verify the Document Security Object signature against the issuing country's Document Signer certificate and CSCA (from the ICAO PKD or national masterlists) per ICAO Doc 9303 Part 11 **[K]**; Chip/Active Authentication where supported (anti-cloning). Indian e-passports are read where issued **[VERIFY — open: coverage of Indian e-passports issued under Passport Seva Programme 2.0 and availability of the Indian CSCA certificate in the ICAO PKD]**. |
| Liveness | Equator liveness (§3.12) vs the DG2 chip photo → K2. |
| Fallbacks | No NFC / chip fails: passport upload + manual review (K1) and video verification (K3) where policy requires; for court-facing use, a notarised and apostilled copy (India a party to the Hague Apostille Convention since 14 Jul 2005 **[K]**; consular legalisation for non-Convention states). |
| Stored | MRZ fields, chip-photo hash, passive-authentication result, issuing state, expiry; passport number encrypted + masked (`P****567`). |
| OCI | OCI card number and copy (manual review); overseas address with proof ≤ 3 months (FR-P01-16). |
| Sanctions | Every `INT` participant screened on name + DOB + nationality (NN-19; FR-P01-20). |

### 3.11 Bank account verification (penny-drop / penniless)

Required before any refund, settlement disbursal through escrow, neutral/trainer/IC external payout or partner commission (FR-P01-17). Methods: ₹1 IMPS penny-drop with beneficiary name, or penniless name lookup (RBI beneficiary account name look-up for RTGS/NEFT, circular of 30 Dec 2024 effective 1 Apr 2025 **[K]**). Providers: RazorpayX Fund Account Validation (primary for payouts), Cashfree verification, Surepass. IFSC `^[A-Z]{4}0[A-Z0-9]{6}$`; name match (normalised Jaro-Winkler) ≥ 0.80 to the KYC/KYB name; stored `account_enc`, `account_masked` (`XXXXXX4321`), IFSC, bank, name-at-bank, score, verified_at. Change → aal2 + 24-hour cooling-off + notice to all contact points. Card details are never collected (NN-31).

### 3.12 Liveness, face match and deepfake defences

| Control | Specification |
|---|---|
| Presentation attack detection | Vendor SDK with ISO/IEC 30107-3 PAD test evidence (iBeta Level 1 minimum, Level 2 for K2 used in signing) **[K]**; passive liveness default, active challenge (random head turn / blink sequence) on retry. |
| Injection attacks | Device attestation (Play Integrity / App Attest — P12 FR-P12-06), virtual-camera and emulator detection on web, SDK-signed frames, server nonce bound into the challenge; vendor evidence against CEN/TS 18099 **[K/U]**. |
| Face match | 1:1 against the credential photo (Aadhaar App AVC, DigiLocker, passport chip) only; never against an Aadhaar photo obtained outside the sanctioned flow (S7 §2.7). Bands: ≥ 0.85 pass; 0.60–0.85 manual review; < 0.60 fail; max 3 attempts per 24 h, then assisted video verification (S-R6). |
| Data | Images retained ≤ 30 days encrypted; templates transient (never stored); biometric data is sensitive personal data under the SPDI Rules 2011 r.3 (IT Act s.43A) and personal data under the DPDP Act 2023 **[K]**. |
| Hearing integrity | Random liveness challenge at arbitration hearing join when the tribunal directs; neutral attests identity in the attendance register (P04). |
| Voice | Never authenticate by voice; instructions on AI calls are confirmed by OTP or in-app confirmation (S7 §2.7). |

### 3.13 Credit reports and financial data — no bureau pulls

**Rule (CI-tested, `NN-14_no_bureau_pull`):** Equator never requests credit information from a credit information company, directly or through a reseller, in its own name. Equator is not a credit institution or a "specified user" (Credit Information Companies (Regulation) Act 2005 s.2(l); CIC Regulations 2006 reg 3 as amended 29 Nov 2021, with RBI's eligibility criteria of 5 Jan 2022 including ≥ 3 years' information-processing experience; dispute resolution is not a reg 9 purpose) **[V-s]**. The `KYC_PORT` has no bureau method; any attempt returns `REGULATED_RAIL_TENANT_ONLY`.

| Route | When | Controls |
|---|---|---|
| Party self-upload | FIN disputes about reporting, write-off, settled-but-shown-unpaid, identity theft | Upload as evidence (`credit_report_self`); check report date, control number and name against K1; PDF tamper checks (incremental-save, metadata); label "party-supplied". Copy: "We cannot fetch your credit report for you. You can download your free credit report from the credit bureau's website and upload it here." |
| Lender tenant production | Lender (a credit institution) is a party | Lender uploads its own pull or tradeline extract as evidence (DPDP s.17(1)(a)) **[VERIFY — open: S7 Q5 — CICRA s.22 / reg 9 for lender upload without a tribunal direction]** |
| Tribunal direction | Contested arbitration | Procedural order directing production (A&C Act s.19; court assistance s.27) |
| Correction workflow | Remedy sought is correction | Letters to CI and CIC; 21-day (CI) and 9-day (CIC) clocks and ₹100/day compensation calculator (RBI circular of 26 Oct 2023; V1 FIN) |
| Account Aggregator | Bank statements, deposits, GST, insurance data | Only through the **lender tenant acting as FIU** with its own credentials and consent artefacts (RBI NBFC-AA Directions 2025; NN-14); Equator is never an FIU; the neutral sees derived summaries only (D6). Without lender FIU set-up → `AA_FIU_NOT_CONFIGURED`; party may upload statements instead (OCR). |

### 3.14 Minimum data matrix (what Equator keeps)

| Source | Kept | Never kept | Retention |
|---|---|---|---|
| Aadhaar App / offline e-KYC | Result, method, `credential_sha256`, name, DOB/age-band, `aadhaar_ref_masked`, photo (≤ 30 days) | Full number, VID, QR, XML, share code | Record: case life; photo ≤ 30 days |
| DigiLocker | Attributes, document URI, issuer, signature result, hash | Document image | Case life |
| PAN | Masked, HMAC, status, match flags; encrypted PAN for payees only | Bulk PAN lists | Case life / tax law (8 years) |
| MCA / GSTIN / Udyam / LEI | Registry fields, snapshot hash | Unrelated directors' personal data | KYB review cycle (12 months) + case life |
| Passport | MRZ fields, PA result, masked number, chip-photo hash | Full chip dump | Case life |
| Bank | Masked account, IFSC, name-at-bank, score; encrypted number for payouts | Card data (NN-31) | Financial records 8 years |
| Liveness / face | Scores, decision, provider ref | Templates; images > 30 days | Scores: case life |
| Credit report | Uploaded PDF as evidence (hash) | Any bureau pull | Case life |

### 3.15 Fallback ladder (never a dead end)

1. Preferred digital method fails or provider down (`PROVIDER_UNAVAILABLE`) → next method in the chooser; KYC check moves to `review_required`, never auto-pass (P01 §5.2).
2. All digital methods unavailable → upload ID for manual review (SLA 1 working day; reviewer SCR-P01-45).
3. Manual review inconclusive or risk ≥ 70 → video verification (K3) slot within 2 working days.
4. Person cannot use any digital channel → assisted mode with a `support_agent` (P12 FR-P12-25; party OTP per action) or an in-person check at an Equator office or partner help desk (DLSA camp, university cell) with document sighting recorded by two staff.
5. Respondent who will not verify → case continues as "unverified respondent"; actions needing K1+ remain unavailable to that respondent only.

### 3.16 Vendor list (indicative; each subject to RFP, DPA and the conflict firewall S7-04)

| Need | Primary | Fallback | Mandatory contract terms |
|---|---|---|---|
| Aadhaar OVSE | Direct UIDAI integration (Aadhaar App credential) | Licensed partner offering OVSE tooling | — (Equator is the OVSE) |
| DigiLocker | Surepass (partner) → direct Requester | Digio | Lawful-channel warranty; India residency; no caching of documents; 24-h breach notice |
| PAN / GSTIN / MCA / Udyam | Surepass | IDfy, Signzy | OPV category disclosure and indemnity; scraping prohibited unless portal terms permit |
| Liveness / face match | HyperVerge | IDfy | ISO/IEC 30107-3 evidence; injection detection; India processing; no template retention; no training on Equator data |
| e-passport NFC | On-device SDK (e.g., Regula / Inverid ReadID-class) | MRZ-only + manual | On-device processing; no image egress |
| Bank verification | RazorpayX FAV | Cashfree, Surepass | — |
| LEI | GLEIF API | Certificate upload | — |
| Foreign registries | UK Companies House API; licensed aggregator (OpenCorporates/Kyckr-class) | Apostilled extract | Licence for commercial use |
| Sanctions | Commercial list API (ComplyAdvantage / LSEG World-Check-class) | Manual list upload + fuzzy match | Daily list refresh; audit trail |
| Video verification | LiveKit (India) | Self-hosted LiveKit | — |

Every vendor DPA: India data residency (or a recorded s.16 basis for `INT`), sub-processor list, CERT-In 6-hour incident reporting support, deletion on termination, no model training, audit rights, group-affiliation disclosure (Reliance-group and other group vendors that may be parties — S7-04).

---

## 4. Representatives (R-16; D2-24; NN-27)

### 4.1 Who may represent, by mechanism (rule pack `representation_policy`, legal risk class)

| Representative type (`representative_type`) | Role code | Negotiation / GRM | Mediation / conciliation | Arbitration | Expert determination | POSH inquiry | Notes |
|---|---|---|---|---|---|---|---|
| `advocate` (enrolled, Indian) | `counsel` | ✔ | ✔ | ✔ | ✔ | ✘ (POSH Rules 2013 r.7(6): no legal practitioner) | Advocates Act 1961 ss.29, 30, 33 **[K]** |
| `law_firm` (firm account; acts through its advocates) | `counsel` (per advocate) | ✔ | ✔ | ✔ | ✔ | ✘ | Authority names the firm; each acting advocate is listed (§4.6) |
| `foreign_counsel` | `counsel` | `INT` only | `INT` only | `INT` only, limits in §4.8 | `INT` only | ✘ | BCI Foreign Lawyers Rules 2022 as amended 13 May 2025 |
| `family_member` (adult relative of an individual party) | `representative` | ✔ | ✔ (FAM: never for a party alleging abuse by that relative — safeguarding screen) | Only with tribunal leave recorded in PO1 | ✔ | ✘ | Relationship declared; no fee |
| `company_officer` (director, employee, in-house counsel of an org party) | `representative` (or `party_org_user` if signatory) | ✔ | ✔ | ✔ as the party's authorised officer | ✔ | ✘ | Authority via board resolution/authority letter (FR-P01-19) |
| `hr_officer` / `union_representative` (WRK) | `representative` | ✔ | ✔ | Only with tribunal leave | — | ✘ | Union rep only for a workman who signs the LoA |
| `professional_agent` (CA, CS, CMA, insurance surveyor acting for a party) | `representative` | ✔ | ✔ | Only with tribunal leave | ✔ | ✘ | No conduct of legal argument; no fee-sharing with Equator |
| `guardian` / `next_friend` (minor or person with disability) | `representative` | ✔ | ✔ | ✔ | ✔ | — | Guardian link (FR-P01-39); court-appointed guardian order uploaded |
| `support_person` (non-representing companion) | case-scoped participant | — | ✔ (with all-party consent) | With tribunal leave | — | Per IC | Not a representative; cannot speak for the party |

Non-advocate representation in arbitration is allowed only as the party's own officer (organisations) or with the tribunal's recorded leave **[VERIFY — open: whether Advocates Act s.33 ("…before any authority or person…") restricts non-advocate representation before an arbitral tribunal; and the Mediation Act 2023 provision on party representatives and advisers once notified]**. Senior Citizens Maintenance Tribunal matters are signposted (no legal practitioner — Senior Citizens Act 2007 s.17). Equator employees never act as representatives (S7-27; A-04).

### 4.2 Letter of Authority / Vakalatnama (Equator proceedings) — e-sign flow

Instrument names: **"Letter of Authority"** (all types) and, where the representative is an advocate, the same instrument is titled **"Vakalatnama (Equator proceedings)"**. It is not a court vakalatnama (CPC Order III r.4; the Advocates' Welfare Fund Act 2001 s.23 stamp applies only to court filings **[K]**); for any court step (s.34 challenge, execution) the platform generates a draft court vakalatnama for the party and advocate to execute offline.

Template `eqr.tpl.loa.v2` fields: party (name, K1 reference, role in case), case number(s) or scope `standing` (organisations only — `core.standing_authorities`), representative (name, type, enrolment no. + State Bar Council or credential, firm), scopes (§4.3, each with plain-language line), monetary limit and currency for offer scopes, mechanisms covered, validity (from / to; default to case closure), service address election (§4.10), sub-delegation allowed (Y/N; advocates within the same firm only), fee arrangement declaration ("non-contingent", NN-18), conflict declaration by representative (§4.9), party acknowledgement ("I can view, narrow or revoke this authority at any time"), date, signatures.

| Step | Actor | Action | Guard / SLA | Output |
|---|---|---|---|---|
| 1 | Party ("Add a representative") or representative ("Request authority") | Starts from case page (SCR-S-R01) | Party K1; representative account exists or invite sent (`core.invitations.kind = counsel_mandate`) | Draft authority, status `offered` / `requested` |
| 2 | Party | Selects type, scopes, limits, validity; preview PDF | Scope/mechanism compatibility (§4.1) else `REPRESENTATIVE_NOT_PERMITTED_FOR_MECHANISM` | Draft PDF (hash) |
| 3 | Representative | Accepts; completes conflict declaration; confirms credential | Credential status ≠ `rejected`; conflict engine run (§4.9) | `accepted` |
| 4 | Party | E-signs at aal2 ≤ 5 min: Aadhaar eSign (default for individuals) or DSC / virtual sign with OTP (organisations; procedure rules may require Aadhaar eSign) via `ESIGN_PORT` | K1 (K2 if scopes include `accept_offers` above ₹10,00,000 or `sign_instruments_on_behalf`) | Signed LoA in evidence ledger (NN-22) |
| 5 | Representative | Counter-signs (acceptance) | aal2 | `active`; case-scoped `core.role_grants` created; event `equator.directory.mandate.activated.v1` |
| 6 | System | Notifies all parties, the neutral(s) and case manager; neutral disclosure re-trigger (LR-ARB-005) | Within 5 min | Representative appears on the case with badge |
| 7 (if `sign_instruments_on_behalf`) | Party | Uploads physically executed, stamped, notarised PoA; reviewer verifies (S-D1) | KYB/KYC reviewer, 1 working day | Scope enabled only after verification |

Stamp duty on the LoA itself: none charged by default; flagged in the NN-09 duty matrix as a per-state check **[VERIFY — open: S-R9]**.

### 4.3 Scope catalogue and limits (`core.party_representatives.scope_v2`)

| Scope key | Plain-language line shown to the party | Default | Limit fields |
|---|---|---|---|
| `view_documents` | "See the case documents shared with me." | ON | — |
| `file_documents` | "File claims, responses and documents for me." | ON | — |
| `attend_sessions` | "Attend meetings and hearings with or for me." | ON | — |
| `receive_notices` | "Receive formal notices for me. Notices sent to them count as sent to me." | OFF | — |
| `negotiate` | "Discuss settlement options for me." | ON | — |
| `make_offers` | "Make settlement offers for me up to the limit." | OFF | `offer_limit_minor`, currency |
| `accept_offers` | "Accept offers for me up to the limit. I still sign the final settlement unless I give a separate power of attorney." | OFF | `accept_limit_minor`, currency |
| `sign_procedural` | "Sign procedural documents for me (for example, a request for time)." | OFF | — |
| `sign_instruments_on_behalf` | "Sign the final settlement or agreements in my name." | OFF; locked until PoA verified (S-D1) | `sign_limit_minor` |
| `pay_and_receive` | "Pay fees for me." (receipt of money to the representative is **not** offered — settlement sums go to the party or escrow, NN-13) | OFF | — |
| `sub_delegate` | "Let another advocate in their firm act for me." | OFF | firm only |
| — `sign_s12_5_waiver` | Never delegable (NN-03) — shown greyed: "Always signed by you personally." | — | DB CHECK |

Enforcement: `AuthorityService.checkRepresentative(caseId, personId, action, amountMinor, currency, mechanism)` — the single enforcement point (mirrors FR-P01-19). Above-limit acceptance creates a party approval task (aal2 e-sign by the party) and returns `MANDATE_LIMIT_EXCEEDED`; missing scope returns `MANDATE_SCOPE_INSUFFICIENT`. Every representative action shows the scope chip and is labelled "by {representative} for {party}" in the case timeline.

### 4.4 Narrowing, revocation, withdrawal, expiry

| Event | Who | Effect | Timing |
|---|---|---|---|
| Narrow scope / lower limit | Party (aal2) | New version of the authority (versioned, hashed); old version superseded | Immediate; representative notified |
| Revoke | Party (aal2), one tap from SCR-S-R01 or Settings → Representatives | Role grants end; sessions lose case access ≤ 60 s; offers already accepted stand; pending representative offers lapse | Immediate as to the platform; as to third parties, from notification (Indian Contract Act 1872 s.208 **[K]**) — all parties and the neutral are notified in the same transaction |
| Withdraw (representative renounces) | Representative | Party notified with 7-day reminder to appoint another or act in person; clocks continue (NN-04) — the notice states the next deadline | Effective on notification (Contract Act s.201) |
| Expiry | System | `expired` at `valid_to`; T-7 reminder to both | Scheduled |
| Death / incapacity of party; credential `rejected` or suspended | System / reviewer | Authority suspended; case manager task (substitution of legal representatives per the procedure rules) | Immediate |
| Party substitution of representative | Party | New authority; old revoked in the same transaction | Immediate |

### 4.5 Advocate verification (Bar Council)

As FR-P01-22 with v2 additions: (a) inputs — State Bar Council (dropdown of 25 councils + BCI), enrolment number (per-state regex), enrolment date, Certificate of Practice number and date, Bar ID card, enrolment certificate; (b) channels — official State Bar Council online roll adapter where one exists (`KYC_PORT.lookupBarRoll`, OFF per state until an official portal is confirmed), else two-person human verification (support agent + registrar) including name match to K1; (c) Certificate of Practice validity under the BCI Certificate and Place of Practice (Verification) Rules 2015 [Verified 22 Oct 2026: CoP valid 5 years, verified every 5 years — BCI CoP Rules 2015 r.9.1; annual re-verification is Equator policy]; (d) badge text "Advocate — enrolment verified on {date}" or "Representative — enrolment not verified"; (e) annual re-verification (`CredentialReverificationWorkflow`); (f) BCI Rules Part VI Ch. II r.36 respected — public representative profiles (if any directory is later enabled) show only factual details, no ratings, no solicitation **[K]**.

### 4.6 Firm accounts

`core.law_firms` (name, registration — partnership deed / LLPIN, address, Bar-registered address, GSTIN, verified domain(s)) and `core.firm_memberships` (advocate, role `firm_admin` | `partner` | `associate` | `clerk`). Firm admin: invites members, sets up firm SSO, sees the firm's matter list (only matters where an authority names the firm), assigns which advocates act (each acting advocate must be listed on the LoA or added by the party's approval). Clerks (`representative`, non-advocate) get `view_documents` and `file_documents` only, never `attend_sessions` in arbitration or any offer scope. Billing for counsel plans: Appendix O (Counsel-Pro; no procedural advantage — D2-18).

### 4.7 Non-advocate representatives

Captured fields: relationship/designation, authority evidence (relationship declaration; board resolution/authority letter for officers; union authorisation), K1 identity, declaration "I am not receiving a fee contingent on the outcome" and "I will not act as a legal practitioner". Platform copy on their badge: "Authorised representative (not an advocate)". Safeguards: FAM safety screen asks each party privately whether they want this person present; a vulnerability flag can block a family-member representative (safeguarding lead decision, sealed). Disallowed: collection agents, DSA/LSP staff or anyone from the lender/recovery side representing a borrower (structural conflict — `REPRESENTATIVE_CONFLICT`, NN-03/NN-12).

### 4.8 Foreign counsel limits (BCI amendment of 13 May 2025)

Foreign counsel may act only in `INT` matters seated in India where (a) they are registered with BCI or within fly-in/fly-out limits (≤ 60 days in any 12 months, Form C declaration, no office in India), (b) the client's principal office is outside India, and (c) the issues on which they act are confined to foreign law and/or international law; Indian-law issues need an Indian advocate on record (BCI Rules for Registration and Regulation of Foreign Lawyers and Foreign Law Firms in India 2022, notified Mar 2023, amended 13 May 2025; *Bar Council of India v A.K. Balaji* (2018) 5 SCC 379, SC, 13 Mar 2018) (Appendix G LR rule; RES_A1b Q02). Product controls: registration status field (`bci_registered` with registration no. / `fifo` with Form C upload and day counter across Equator matters); client principal-office attestation; issue-of-law attestation on each pleading/appearance; blocked for non-`INT` cases and foreign-seated matters need no BCI check but record home-bar good standing (≤ 6 months). Breach → `FOREIGN_COUNSEL_SCOPE_RESTRICTED`.

### 4.9 Conflict checks

Run at authority acceptance, at any party/neutral change and nightly for open cases (`RepresentativeConflictWorkflow`):

| Check | Source | Outcome |
|---|---|---|
| Representative previously acted/advised for the opposite party in the same matter | Platform history; representative declaration | Block (`REPRESENTATIVE_CONFLICT`) — BCI Rules Part VI Ch. II r.33 **[K]** |
| Representative (or firm) acts for both sides | Firm membership graph | Block |
| Relationship with a neutral on the case (same firm, family, professional association listed in Fifth Schedule) | Neutral disclosures; firm graph | Neutral disclosure re-triggered (A&C s.12; LR-ARB-005); registrar review; may lead to challenge |
| Representative is an Equator employee, committee member or empanelled neutral in the same tenant matter | Workforce/neutral rosters | Block; empanelled neutrals may represent parties only in matters where they are not on the panel list for that case and after disclosure under Appendix N |
| Lender/insurer/employer staff representing the counterparty | Org membership | Block |
| Repeat-player concentration (same representative on > N matters for one enterprise) | Analytics | Information to registrar only (feeds neutral disclosure, never allocation) |

### 4.10 Notices to representatives

Service on a representative counts as service on the party only if (a) the authority has `receive_notices` ON, (b) the case's pinned rules of procedure allow service on authorised representatives, and (c) the representative's service address/channel is verified. Otherwise notices go to the party, with a courtesy copy to the representative. Deemed-service computation (P02/P07) records which address satisfied A&C Act s.3 or the rules. Recovery-related communications to borrowers still follow NN-12 windows even if a representative is copied. When authority ends, the notice engine reverts to party addresses within the same transaction and re-sends any notice issued in the preceding 72 hours to the party.

### 4.11 Representative dashboard

See §5 (SCR-S-D02).

---

## 5. Dashboards per user type (R-14; extends Appendix C §D and S9 §5.3)

Screen IDs `SCR-S-Dnn` are allocated here; the implementing phase renames them into its series in the same PR (Appendix C §A rule). Widgets are configurable through the `dashboard_pack` config kind within these defaults; users may reorder or hide non-mandatory widgets (`core.dashboard_layouts`); sealed data never appears outside the sealed workspace (NN-07); no widget ranks neutrals by outcome (NN-16, NN-28).

| Persona | Screen | Widgets (top to bottom; **M** = mandatory, cannot be hidden) | KPIs shown | Quick actions (max 4) |
|---|---|---|---|---|
| Party (individual / org user) | SCR-S-D01 `/app` | **M** Next action card (what, why, due date, days left, "who decides at this step"); **M** My cases (status chip + ClockPill + "what happens next" sentence); upcoming sessions (join button 15 min before); what this costs so far / what's next (paid, due, refundable — S9); documents requested; messages; my representatives (scope summary, revoke); **M** free-forum reminder where signposting applies (forum + last date, NN-20); help & assisted-mode request | Days to next deadline; actions pending | Respond / continue filing · Join session · Pay · Add a representative |
| Representative (counsel / representative / firm) | SCR-S-D02 `/app/counsel` | Client switcher; **M** matters by client with authority scope chips and expiry; filings due 7/14/30 days; hearings this week; offers awaiting client decision; authorities pending acceptance; verification status banner; firm workload (firm admin) | Filings due count; authorities expiring ≤ 14 days | File for client · Request authority · Join hearing · Message client's case manager |
| Mediator / conciliator | SCR-S-D03 `/app/neutral?space=mediation` | **M** Today's sessions with join and safeguards status; appointment offers with countdown (disclosure first); agreements to mediate pending signature; settlement drafts awaiting authentication; mediation clocks amber/red (contractual 120+60 default); feedback summary (conduct only); earnings & payouts; CPD hours vs requirement (Appendix N) | Sessions today; offers expiring ≤ 48 h; CPD hours | Join next session · Accept/decline offer · Open caucus notes · Mark availability |
| Arbitrator | SCR-S-D04 `/app/neutral?space=arbitration` | **M** s.29A clocks per case (days to 12-month mark; extension status; never back-dating — NN-04); hearings; drafting queue (orders, awards) with AI-assist status "draft — requires your review" (NN-01); disclosure renewals due; challenge notices; fee deposits status; sealed-award vault (arb-med) | Cases within 60 days of s.29A limit; awards in drafting > 30 days after final hearing | Open award builder · Issue procedural order · Join hearing · Submit disclosure |
| Case manager | SCR-S-D05 `/console` | **M** Queue by stage with SLA timers; **M** clocks owned by me (amber/red; unowned clocks block closure — NN-04); scrutiny SLA; service failures and deemed-service decisions due; hearings needing logistics; representative changes today (re-send check §4.10); handoffs; deficiency expiries | Scrutiny within 2 working days %; notices delivered %; my red clocks | Next in queue · Assign clock owner · Compose notice · Schedule session |
| Registrar / deputy registrar / case counsel | SCR-S-D06 `/console/registrar` | Appointments pending (allocation runs — counts only); challenges with timeliness; committee agenda builder; certified-copy requests; s.34/s.28 challenge windows; **M** unowned statutory clocks; publication requests awaiting consent/redaction; break-glass approvals pending (§6.6) | Appointment time (filing → constituted); challenges decided within rules time | Run allocation · Build agenda · Issue certified copy · Approve break-glass |
| Committee member / chair | SCR-S-D07 `/committee` | **M** Next meeting with papers (watermarked); matters awaiting my vote; recusals I declared; decisions issued (my sub-committees); circulation-resolution requests with deadline | Matters pending > 7 days | Open papers · Vote · Declare conflict · Sign decision |
| Enterprise admin / operator (lender, insurer, employer, listed co.) | SCR-S-D08 `/app/enterprise` | Volumes this FY by vertical/stage; settled pre-arbitration %; notice funnel (sent → delivered → engaged); SLA heatmap; compliance (instalments on track/overdue); last bulk batch; clause coverage; Defensibility distribution (FIN); contract meter committed vs used (Appendix O); **M** disclosure banner "Neutrals are appointed independently by Equator" (NN-03, NN-16) | Settled pre-arbitration %; median days to outcome; instalment compliance % | New bulk batch · File a case · Approve offer (within authority) · Download MIS |
| GRO / internal ombudsman / SGRC / GRC | SCR-S-D09 `/app/grm` | **M** Tickets by regulator clock state (T-7, T-3, breached; RB-IOS 2026 30-day RE window, UGC SGRC 15 working days, etc.); escalations offered/accepted; ageing buckets; IO referrals; category heatmap | % resolved within regulator clock; breaches this month | Open next ticket · Respond from template · Offer ODR · Export regulator MIS |
| Chambers admin | SCR-S-D10 `/app/chambers` | Caseload by stage; clock risk; revenue (₹) month/FY; subscription status and usage meters (Appendix O); referral inflow (if listed); members and pending invites; branding/legal-review status | Active matters; on-time hearings %; MRR | New matter · Invite member · Publish fee schedule · View invoices |
| Partner | SCR-S-D11 `/partners` | Referrals by status (coarse enum only); clause adoptions; statements (no referral reward of any kind to advocates, CAs, CSs or CMAs — NN-34; master X-62); approved collateral | Referrals this quarter; conversions | Copy referral link · New co-branded page · Download statement |
| Platform admin | SCR-S-D12 `admin…/` | Availability/SLOs; outbox lag; audit chain verification; incidents; provider circuits; tenants provisioning; flags pending approval; active elevations with countdown | Error budget burn; chain status | Request elevation · Provision tenant · Flip release flag (maker) · Open incident |
| DPO | SCR-S-D13 `admin…/privacy` | **M** DSR queue with SLA clocks; withdrawal-propagation breaches; **M** break-glass events awaiting review; breach incidents (72-hour Board timer; 6-hour CERT-In); notices pending legal approval; DigiLocker/UIDAI partner obligations calendar (audits, reports) | DSRs within SLA %; open breaches | Assign DSR · Review break-glass · Start breach workflow · Approve notice |
| Auditor (time-bound, read-only) | SCR-S-D14 `admin…/audit` | Grant scope and expiry countdown; scoped audit search; chain verification reports; evidence-ledger sampler; access-log sampler | Days left on grant | Search events · Verify chain · Export (watermarked, logged) |

**Fewer-clicks rules (testable; `ux.click_budget` lint in Playwright):**

1. The next action for any persona is reachable in **≤ 1 click** from the dashboard; the five critical journeys (respond, pay, sign, join hearing, upload document) complete in **≤ 5 screens** from a notification deep link.
2. Deep links land on the action, not the dashboard (P12 FR-P12-14), after the minimum step-up.
3. Pre-fill everything already known (identity from K1, organisation from KYB, case from context; WCAG 3.3.7 redundant entry); never ask for an ID before the user knows the route and fee (S9 §5.2).
4. One primary button per screen; destructive actions need a confirmation screen, not a modal checkbox.
5. Bulk actions on staff and enterprise lists (assign owner, send reminder, export); keyboard command palette (`Ctrl/Cmd+K`) on staff, neutral and enterprise consoles.
6. Mobile: thumb-reach primary actions; offline-prepared drafts (P12 FR-P12-09).
7. Empty states tell the user what to do next in one sentence and one button.

---

## 6. RBAC / ABAC matrix

### 6.1 Policy model

Cerbos (ADR-0004) evaluates `principal × resource × action` on every API call; Postgres RLS (F.2) is the second line; Appendix C UI hides what policy denies but never substitutes for it.

- **Principal attributes:** `roles` (from the acting membership in `Equator-Context`), `tenant_id`, `person_id`, `acr`, `auth_age_s`, `kyc_level`, `is_workforce`, `device.bound`, `device.integrity`, `network_zone` (`office` | `ztna` | `public`), `grants[]` (case/proceeding role grants incl. representative scopes and limits), `conflicts[]` (case IDs blocked by §6.5), `sealed_refs[]`.
- **Resource attributes:** `tenant_id`, `case_id`, `vertical`, `mechanism`, `confidentiality_tier` (`standard` | `high` | `sealed`), `owner_party_id`, `visibility` (document sharing set — Appendix L), `state`, `amount_minor`, `currency`, `is_caucus`, `requires_consent_of[]`.
- **Decision logging:** every deny and every allow on `high`/`sealed` resources writes `audit.access_log` with `policy_version` (F.5).

### 6.2 Matrix (roles × resources × actions)

Actions: **C** create · **R** read · **U** update · **S** sign / approve / decide · **X** execute (serve, send, release, publish, pay) · **—** none. Conditions in brackets (§6.3). Case = case record and parties; Document = DMS objects; Hearing = sessions/rooms; Order = procedural orders and directions; Award = arbitral awards (incl. consent awards); Settlement = settlement terms/MSA/OTS; Payment = invoices, payments, refunds, payouts, escrow; Publication = published awards/settlements/digests (App. R); Config = Ruleset Studio objects (rules, forms, fees, templates, flags); User admin = memberships, roles, SSO, invites.

| Role | Case | Document | Hearing | Order | Award | Settlement | Payment | Publication | Config | User admin |
|---|---|---|---|---|---|---|---|---|---|---|
| `party` | C, R, U [own] | C, R [own, vis] | R, join [own] | R [own] | R [own, issued] | R, U (propose terms), S [own, K2] | C (pay), R [own] | S consent / revoke [own] | — | own representatives only |
| `party_org_user` | as party [org] | as party [org] | as party | R | R | S [auth] | C, R [org]; S approve within [auth] | S consent [auth] | — | org members (org admin) |
| `counsel`, `representative` | R, U, C file [scope] | C, R [scope, vis] | join [scope: attend] | R [scope] | R [scope] | U propose; S only [scope: sign_instruments_on_behalf + PoA] | C pay [scope: pay_and_receive] | — (party consents personally) | — | firm members (firm admin) |
| `neutral_mediator` / `neutral_conciliator` | R [appt] | R [appt, vis]; C caucus note [author] | C, U, X host [appt] | C, S [appt] | — | U draft, S authenticate [appt] | R own fee notes | — | — | — |
| `neutral_arbitrator` | R [appt] | R [appt, vis] | C, U, X host; recording [cons] | C, S [appt, aal2-pr] | C, U, S [appt, aal2-pr]; seal (arb-med) | R; S consent-award conversion [appt, cons] | R own fees; C deposit directions | S tribunal consent [appt] | — | — |
| `neutral_expert` | R [appt] | R [appt, vis] | C, X host site visit [appt] | — | — | — | R own fees | — | — | — |
| `neutral_facilitator` (v2.1) | R [appt] | R [appt, vis] | C, U, X host negotiation rounds [appt] | — | — | R; U draft negotiated terms for parties to adopt [appt] | R own fees | — | — | — |
| `tech_concierge` | R metadata [assigned to neutral] | — | X operate controls [on neutral's instruction] | — | — | — | — | — | — | — |
| `case_manager` | R, U [assigned]; C (assisted filing) | R, U metadata; C bundles [assigned] | C schedule, U, X logistics | X serve [assigned] | X serve after issue | C envelope, X send for signing | R [assigned] | C publication request | — | — |
| `registrar` / `deputy_registrar` | R, U, S scrutiny decision [tenant] | R [tenant, not caucus] | R | C, S institutional orders (appointments, extensions under rules) | R; X certified copy, sealed-vault release [dual] | R | R | X publish [after legal S + consents] | C (maker) rules-of-procedure items | — |
| `case_counsel` | R, U [assigned] | R [assigned] | R | C drafts for registrar | R | R | — | U redaction | — | — |
| `committee_member` / `committee_chair` | R [grant: agenda, ¬conflict] | R [grant, watermark] | — | S committee decisions [grant, aal2-pr] | — | — | — | S Transparency sub-committee policy | S (Rules sub-committee: procedure rules checker) | — |
| `panel_manager` | — | R neutral files | — | — | — | — | — | — | C panels, allocation policies (maker) | neutral memberships |
| `quality_officer` | R [tenant] | R | R (QA samples) | R | R; U return to tribunal (scrutiny) | R | — | U redaction, prepare | — | — |
| `safeguarding_lead` | R, U safety flags [tenant, sealed-safety] | R [sealed-safety] | U (shuttle-only directions) | — | — | R | — | — | — | — |
| `escrow_officer` | R [tenant] | R evidence of milestones | — | — | — | R | X release [dual, aal2-pr, office/ztna] | — | — | — |
| `finance_controller` | R [tenant] | R invoices | — | — | — | — | S refunds, payouts; X GL export [aal2-pr] | — | S fee schedules (finance checker) | — |
| `legal_reviewer` | — | R templates | — | — | — | — | — | S legal sign-off | S (checker) legal rules, templates, notices | — |
| `institution_admin` | R [tenant, agg] | — | — | — | — | — | R reports | — | C, U (maker) | C, U, revoke [tenant, SoD] |
| `chambers_admin` | R [chambers tenant] | R [tenant, not caucus] | R | R | R | R | R; C invoices | S tenant publication policy | C, U (maker) within guardrails | C, U [tenant] |
| `enterprise_admin` | C, R [org's cases, as party]; R MIS [agg] | C, R [org, vis] | join as party | R [org] | R [org] | S [auth] | C, R [org] | S consent [auth] | C, U tenant SLA / clause choices (maker) | C, U [tenant]; SSO |
| `enterprise_operator` | C (single/bulk), R [org, org_unit] | C, R [org_unit] | join as party rep [auth] | R | R | U propose, S [auth limit] | C pay | — | — | — |
| `grievance_officer` / `internal_ombudsman` | GRM tickets: C, R, U, S respond [desk]; ODR offer X [consent] | C, R [ticket] | — | — | — | — | — | — | — | — |
| `partner` | — (coarse referral status only) | — | — | — | — | — | R own statements | — | — | — |
| `support_agent` | R [ticketed support grant] | R metadata | R | — | — | — | R status | — | — | U reset assist (no factor bypass) |
| `dpo` | R [DSR / breach purpose grant] | R [grant] | — | — | — | — | — | S privacy review | S privacy notices | R; S break-glass review |
| `auditor` | R [grant ≤ 90 days, scoped] | R [grant, watermark] | R | R | R | R | R | R | R | R |
| `platform_admin` | — by default; R/U only with JIT elevation [aal3, approved] | — | — | — | — | — | — | — | C, U platform (maker); flags | C, U [elevation] |
| `machine` (API client) | C (bulk/API intake), R [api scopes, tenant] | C upload, R [scopes] | — | — | — | — | C pay intents [scope] | — | — | — (never `allocation:run`, F.4.1 CHECK) |

*v2.1 addition (22 Oct 2026, from the management brief):* `neutral_facilitator` is a panel neutral who assists a negotiation (structured offers, blind-bid rounds, issue lists) without any power to decide or to recommend terms. Facilitators sign in through the neutral portal (`kc_variant=mediator`, negotiation space), follow the Code of Conduct (Appendix U §U.3) and the conflict and disclosure rules for mediators, may not hold caucus recordings, and may not authenticate a settlement; negotiated terms are adopted and signed by the parties through P06.

Hard denials encoded as Cerbos `DENY` rules (override every allow): enterprise roles never select, rank or veto neutrals (`APPOINTMENT_LENDER_TRIGGER_BLOCKED`, NN-03); caucus notes readable only by the author neutral (`CAUCUS_SEALED`, NN-11); POSH resources only through the sealed service (NN-07); nobody signs a `sign_s12_5_waiver` for another person (NN-03); no role publishes without all-party consent and legal sign-off (NN-26); no workforce principal accesses a case in its `conflicts[]`; no AI principal (`machine` with `ai_agent` subject) sends, files or signs (NN-01).

### 6.3 ABAC condition dictionary

| Tag | Predicate |
|---|---|
| `own` | `resource.case_id ∈ principal.case_ids` via `core.case_parties` for the principal's person/org |
| `org` / `org_unit` | Resource belongs to a case where the principal's organisation (or org unit) is a party |
| `auth` | `AuthorityService.check(org, person, action, amount, currency, mechanism)` passes (FR-P01-19) |
| `scope` | Active `core.party_representatives` row with the scope key, within limits and validity (§4.3) |
| `vis` | Document shared with the principal's side under Appendix L sharing controls |
| `appt` | Confirmed appointment (`core.appointments.status = confirmed`) on that proceeding |
| `assigned` | Case assigned to the staff member or their team; or `app.staff_scope = tenant` for registrar-level roles |
| `grant` | Unexpired, unrevoked `core.role_grants` row for that scope/case |
| `cons` | Required consents recorded (recording, publication, same-neutral med-arb) |
| `dual` | Second distinct approver with the same or higher role completes within 24 h |
| `agg` | Aggregated/anonymised read model only (k ≥ 5 suppression) |
| `aal2-pr`, `K2` | Principal `acr` / `kyc_level` meet the stated level with the stated auth age |

### 6.4 Delegation

| Delegation | Allowed | Limits |
|---|---|---|
| Org signatory → operator | Yes (`core.delegations`) | ≤ delegator's limit; ≤ 90 days; named actions; never `sign_s12_5_waiver` or `sign_arbitration_agreement` |
| Party → representative | Yes (§4) | Scope catalogue; PoA for signing on behalf |
| Representative → firm associate | Only if `sub_delegate` scope | Same firm; one level; party notified |
| Neutral → tech_concierge | Yes, per session | Operate controls only (admit, mute, move rooms, share bundle page); no content edits, no notes, no signing; concierge actions logged as "on instruction of {neutral}" |
| Case manager → cover case manager | Yes (leave cover) | ≤ 30 days; same tenant; SoD rules re-checked |
| Registrar → deputy registrar | Yes | By standing order recorded in the audit log |
| Any delegation chain | Max depth 1 | Delegate cannot re-delegate; delegations end with the delegator's own authority |

### 6.5 Conflict checks at access level

`ConflictIndex` (rebuilt on party, representative, neutral, staff or committee changes): links persons and organisations through case participation, firm membership, employment and declared relationships (staff and committee declarations, neutral disclosures). A principal whose node is within the configured conflict distance of a party in a case gets that case in `conflicts[]`: workforce users lose access and cannot be assigned; committee members are auto-recused (with a notice to the chair); neutrals are excluded from allocation (P03) and must disclose. Overrides: none for workforce and committee; a neutral conflict may proceed only on all-party informed written waiver where the law allows (A&C s.12(5) proviso for Seventh Schedule matters — post-dispute, express, per party; NN-03).

### 6.6 Break-glass

| Element | Rule |
|---|---|
| Who may request | `registrar`, `safeguarding_lead`, `platform_admin` (with elevation), `dpo` |
| When | Imminent risk to a person's safety; legal deadline about to lapse with the owner unreachable; court or regulator order requiring immediate production; security incident containment |
| How | `POST /v1/break-glass` with case/resource scope, reason code (`safety`, `deadline`, `legal_order`, `security`) and justification ≥ 30 characters (F.5 CHECK); aal2-pr ≤ 5 min (aal3 for `platform_admin`); approved by a second eligible person (F.4.1 CHECK `approved_by <> granted_by`) within 15 minutes (on-call roster) |
| Grant | `core.role_grants.break_glass = true`, single case or resource set, read-only unless the reason is `deadline` (then the minimum write action), ≤ 4 hours, never sealed POSH content (POSH break-glass exists only inside the sealed service, presiding officer + DPO) |
| After | DPO notified immediately (`equator.identity.break_glass.opened.v1`); every read in `audit.access_log`; post-incident review by DPO within 2 working days (`audit.break_glass_events.review_outcome`); affected party notified unless the reason is a legal order that forbids it |

### 6.7 Segregation of duties (extends FR-P01-27)

Maker ≠ checker on every config change (NN-21); `escrow_officer` ∉ {`case_manager`, `quality_officer`, `finance_controller`} in a tenant; `quality_officer` ≠ `case_manager`; `legal_reviewer` cannot approve a template they drafted; `committee_member` cannot be `registrar` in the same tenant; `panel_manager` cannot be an empanelled neutral in the same panel; `platform_admin` cannot approve their own elevation. SoD conflicts are checked at membership grant (DB trigger) and at policy time.

### 6.8 Example policy (Cerbos, abbreviated)

```yaml
apiVersion: api.cerbos.dev/v1
resourcePolicy:
  resource: settlement
  version: "v2"
  rules:
    - actions: ["sign"]
      effect: EFFECT_ALLOW
      roles: ["party"]
      condition: { match: { all: { of: [
        { expr: "R.attr.case_id in P.attr.own_case_ids" },
        { expr: "P.attr.kyc_level >= 2 && P.attr.acr in ['eq:aal2','eq:aal2-pr'] && P.attr.auth_age_s <= 300" } ] } } }
    - actions: ["sign"]
      effect: EFFECT_ALLOW
      roles: ["counsel", "representative"]
      condition: { match: { expr: >
        has(P.attr.grants[R.attr.case_id]) &&
        'sign_instruments_on_behalf' in P.attr.grants[R.attr.case_id].scopes &&
        P.attr.grants[R.attr.case_id].poa_verified == true &&
        R.attr.amount_minor <= P.attr.grants[R.attr.case_id].sign_limit_minor } }
    - actions: ["*"]
      effect: EFFECT_DENY
      roles: ["*"]
      condition: { match: { expr: "R.attr.case_id in P.attr.conflicts" } }
```

### 6.9 v3.0 role catalogue additions (23 October 2026)

v3.0 adds the roles below. This appendix registers the **codes**; the owning appendix holds each role's full permission matrix and Cerbos policies, and prevails on its detail. Every workforce role signs in through Keycloak client `eq-portal-ops` (Operations Platform, `apps/ops`) with phishing-resistant MFA (`acr = eq:aal2-pr`; master X-24); chambers roles sign in through `eq-portal-chambers` / `eq-portal-chambers-{slug}` (§2.8). Roles already in §6.2 (`support_agent`, `grievance_officer`, `finance_controller`, `legal_reviewer`, `compliance_officer`, `dpo`, `auditor`, `chambers_admin`, `platform_admin`) keep their rows and gain only the v3 permissions stated by the owning appendix. No v3 role can be combined with a case-administration role in a way that breaks NN-36 separation of duties or the commercial-to-case firewall (D3-24).

| Role code(s) | Scope / portal | Purpose (summary) | RBAC owner |
|---|---|---|---|
| `legal_ops` | Platform; `eq-portal-ops` | Authors platform rule-pack versions; triages the regulatory-watch feed; cannot approve (Appendix G §G.4.1) | Appendix V §V.6.5; P15 §3 |
| `ops_director`, `ops_manager`, `case_services_lead`, `onboarding_specialist`, `customer_success_manager`, `support_lead`, `sales_executive`, `bd_manager`, `finance_ops`, `department_head`, `employee` | Equator (and later group-company) workforce; `eq-portal-ops` | Operations Platform departments: operations, case-services metadata only, onboarding, customer success, support, sales and BD, finance operations, department heads, employee self-service | Appendix X §X.1.3, §X.3, §X.14; P16 §3 |
| `ops_guest` | Time-bound guest (≤ 90 days), named implementation projects only | Contractors such as implementation partners; no CRM list views | Appendix X §X.1.3, §X.14 |
| `escalation_reviewer` (permission bundle) | Equator institution tenant; held by the Company Secretary | Level-2 review of a grievance after the Grievance Officer's final reply (appeal within 30 days) | Appendix X X-52, §X.8 |
| `marketing_manager`, `content_writer`, `designer`, `social_media_executive`, `pr_manager`, `partnerships_manager` | Workforce; `eq-portal-ops` | Marketing, brand, content, social, PR and partnerships (bundles `mkt.*`) | Appendix Y §Y.13; P17 §3 |
| `hr_manager`, `hr_executive`, `payroll_maker`, `payroll_checker`, `accounts_maker`, `accounts_checker`, `group_hr` | Workforce (per legal entity); `eq-portal-ops` | HRMS, payroll and accounts under maker-checker (NN-36); payroll maker ≠ checker | Appendix Z §Z.12.4, §Z.14.1; P18 §3 |
| `internal_auditor` | Entity or group, per engagement; read-only, time-boxed | Internal audit (independent of operations; reports to the Board/Audit function) | Appendix Z §Z.14.1; Appendix AE §AE.1.1, §AE.11 |
| `it_admin` | One entity's workspace connection | Joiner-mover-leaver provisioning, groups and licences in Microsoft 365 (or Google Workspace when enabled); never grants platform roles | Appendix AC; Appendix AD §AD.3 |
| `group_admin`, `entity_admin` | Group (no data access by default) / one legal entity | Group registers, shared services, GDSA and grant templates / the entity's settings, users and grants into its own partition | Appendix AD §AD.3; FR-P01-V3-AD02 |
| `revenue_manager` | Platform; `eq-portal-ops` | Maker for revenue-stream records in the stream registry (`rev`); checker is `finance_controller` (CFO designation) or the Board per the authority matrix | Appendix AB §AB.13 |
| `marketplace_manager`, `marketplace_moderator`, `provider_verifier`, `ad_reviewer` | Workforce; `eq-portal-ops` | Private Practice Marketplace operations, moderation, two-person provider verification, sponsored-creative review (maker; `compliance_officer` checks) | Appendix AA §AA.16 |
| `mkp_provider_owner`, `mkp_provider_staff` | Marketplace providers (Chambers tenants, service providers) | Own listing, engagements, statements and sponsorship orders; `mkp_provider_owner` may request the export scope `MARKETPLACE_PROVIDER` (Appendix AC §AC.13.3) | Appendix AA §AA.16 |
| `registry_steward`, `registry_verifier`, `panel_register_admin`, `panel_register_user` | Registry owner entity / consumer tenants | Infrabyx Professional Registry status, DSRs and two-person verification; tenant professional panel registers | Appendix AA §AA.12, §AA.16 |
| `engineer`, `tech_lead`, `release_manager`, `sre`, `security_engineer`, `security_lead`, `cab_chair` | Engineering workforce; `eq-portal-ops` | Change, release, patch and backup governance; no production data access for `engineer`; two-person production approval | Appendix AE §AE.1.1 |
| `chambers_owner`, `chambers_case_manager`, `chambers_staff`, `chambers_hr`, `chambers_accounts` (`chambers_admin` exists; `employee` at tenant scope) | Chambers tenant; `eq-portal-chambers` | Practice ownership, case management (replaces the P10 `case_manager` seat), staff, practice HR (maker) and accounts (checker); HR and accounts roles never read case content (D3-19) | Appendix W §W.2.1; P20 §3 |

**Designations, not roles.** `cfo` is a designation held on `finance_controller`, and `company_secretary` a designation held on `compliance_officer` (Appendix Z §Z.2.3, §Z.12.2; Appendix AB §AB.13); the Payroll Compliance Officer is `compliance_officer` with responsibility `payroll_compliance` (Appendix Z §Z.2.4, §Z.2.6).

**New permissions (Appendix V §V.6.5; P15 §3).** Cerbos resources `cfg_setting`, `rule_pack`, `cfg_pack`, `support_session`, `access_review`: `cfg:read`, `cfg:read:history`, `cfg:write:t`, `cfg:lock`, `cfg:export`, `cfg:import`, `cfg:pack:apply`, `cfg:regwatch:triage`, `cfg:rulepack:adopt`, `cfg:rulepack:adapt`, `cfg:rulepack:author`, `access:jit:request`, `access:jit:approve`, `access:review`, `support_session:grant`. The §6.2 "Config" column reads as follows for G-tier changes: existing `config:propose`, `config:approve` and `config.approve.legal` (P00) are reused; tier-L values are not editable by any role (NN-33). `platform_admin` changes a tenant's T or tenant-scope G values only inside a tenant-granted support session of ≤ 72 hours (D3-14).

**Separation of duties added by v3 (extends §6.7).** Payroll maker ≠ payroll checker; accounts maker ≠ accounts checker; no single user can create a payee or employee, change bank details, approve and execute a payment, and reconcile it (NN-36; Appendix Z §Z.12.4); the requester or author of a change cannot approve its production deployment (Appendix AE §AE.1.1); sales and ad-operations users cannot sit on the Marketplace Review or Appeals Panels (Appendix AA §AA.8.3).

---

## 7. Common settings pages (`/settings`, one shell with left rail; sections by role)

Billing, plans, payment methods, mandates, invoices, tax details, renewal and cancellation are specified in **Appendix O** (Settings → Billing / Payments and receipts) and are not repeated here.

| Section (route) | Fields / controls | Rules |
|---|---|---|
| Profile `/settings/profile` (SCR-P01-39) | Display name; legal name (read-only once K1, "Request correction" → re-verification); photo (optional); contact points (add/verify/set primary); addresses (PIN lookup; foreign schema); professional credentials (counsel/neutral; status chips); organisation memberships | Changing primary mobile/email: OTP to old and new (FR-P01-11) |
| Security `/settings/security` (SCR-P01-41) | Passkeys (add, rename, remove; attested badge), authenticator app, recovery codes (regenerate at aal2), password (professionals), "Sign-in methods allowed for my account" (party may opt into passkey-only) | Removing the last second factor blocked for professional roles |
| Sessions and devices `/settings/devices` | Active sessions (device, city, portal, last active, revoke); bound mobile devices (platform, attestation, bound date, revoke → remote wipe P12 FR-P12-24); "Sign out everywhere"; login history 30 days (portal, method, result) | Revocation effective ≤ 60 s |
| Notifications `/settings/notifications` (SCR-P01-40) | Channel order (WhatsApp, SMS, email, push, voice) with per-channel opt-in; categories (hearing, deadline, payment, signing, messages, case updates; marketing separately consented); quiet hours (narrow only; NN-12 window shown locked); blackout dates; digest (daily/weekly) for professionals | Legal notices cannot be switched off; the page explains which ones and why |
| Language and accessibility `/settings/accessibility` | UI language; notice language; second language for bilingual documents; font scale 100–200%; high contrast; reduced motion; captions default; screen-reader layout; sign-language interpreter request; assisted-mode request | Language change re-renders without reload; accessibility prefs synced to mobile |
| Privacy and consents `/settings/privacy` (SCR-P01-42) | Consents by purpose (status, date, notice version; give/withdraw in one action); notices (current and history); data requests (access, correction, erasure, nomination, grievance) with SLA; guardian links; download my data; delete account (explains legal-hold retention) | Withdrawal propagation per FR-P01-38; sealed purposes need aal2 |
| Connected accounts `/settings/connections` | DigiLocker (linked / unlink); Aadhaar App credential (last verified date; "verify again"); organisation SSO (read-only, managed by admin); calendar feed for neutrals and representatives (private ICS URL, regenerate; titles carry case number only — no party names); firm (counsel); LEI (organisations) | Unlinking DigiLocker does not lower an already-achieved K-level; the K-level expiry policy applies |
| Representatives `/settings/representatives` (parties) · Clients and authorities (representatives) | Party: list of authorities across cases (scope, limits, validity; narrow, revoke). Representative: authorities held, pending requests, expiries, renounce | §4.4 |
| Organisation `/settings/organisation` (org admins) | KYB status, signatories and authority matrix (SCR-P01-20), members (SCR-P01-21), SSO (SCR-P01-30), delegations (§6.4) | Edits after verification need review |

---

## 8. Data model, APIs, events, errors and configuration

### 8.1 Tables (new or additive; Appendix F conventions; tenant RLS unless stated)

| Table | Key columns | Constraints / notes |
|---|---|---|
| `core.login_portals` (platform config) | code PK, route, oidc_client_id, allowed_roles text[], methods jsonb (ordered), min_acr, max_auth_age_s, idle_timeout_s, absolute_timeout_s, network_policy_id, device_policy, dashboard_route, mobile_space, copy_keys jsonb, version, status | Guardrail trigger: `staff`, `committee`, `admin` rows require `min_acr = 'eq:aal2-pr'` |
| `core.network_policies` | id, tenant_id (NULL = platform), name, cidrs cidr[], zone (`office`,`ztna`), applies_to_roles text[] | — |
| `core.person_links` (identity-owned) | id, consumer_person_id, workforce_person_id, linked_by (dpo), linked_at, reason | Drives automatic conflicts (§1.3) |
| `core.users` (additive) | `is_workforce boolean NOT NULL DEFAULT false` | CHECK via trigger: workforce users cannot hold party/counsel/representative/neutral memberships |
| `core.kyc_checks` (additive) | `credential_sha256 char(64)`, `pa_result text` (passport passive auth), `attributes_minimised jsonb` | `method` enum extended per S-R5 |
| `core.party_representatives` (additive to F) | `representative_type text CHECK IN ('advocate','law_firm','foreign_counsel','family_member','company_officer','hr_officer','union_representative','professional_agent','guardian')`, `firm_id uuid`, `scope_v2 jsonb NOT NULL`, `offer_limit_minor bigint`, `accept_limit_minor bigint`, `sign_limit_minor bigint`, `currency core.currency_code`, `mechanisms text[]`, `valid_to timestamptz`, `poa_document_id uuid`, `poa_verified_at timestamptz`, `receive_notices boolean`, `service_contact_point_id uuid`, `sub_delegate boolean`, `version int`, `supersedes_id uuid`, `revocation_reason text`, `renounced_at timestamptz` | CHECK `NOT (scope_v2 ? 'sign_s12_5_waiver')`; CHECK `NOT (scope_v2 @> '{"sign_instruments_on_behalf":true}') OR poa_verified_at IS NOT NULL OR party is organisation`; status enum extended to F values + `offered`, `requested`, `accepted`, `suspended`, `renounced` (ADR — S-R2) |
| `core.standing_authorities` | id, tenant_id, organisation_id, counsel_person_id, firm_id, scope_v2, limits, valid_from/to, document_id, status | For panel counsel of an enterprise (replaces P01 `organisation_standing`) |
| `core.law_firms` | id, tenant_id NULL (shared), legal_name, constitution (`partnership`,`llp`,`proprietorship`), llpin, gstin, pan_masked, address_id, verified_domains citext[], kyb_status | UNIQUE (llpin) |
| `core.firm_memberships` | id, firm_id, person_id, firm_role (`firm_admin`,`partner`,`associate`,`clerk`), status, valid_from/to | — |
| `core.foreign_counsel_registrations` | id, person_id, mode (`bci_registered`,`fifo`), bci_registration_no, form_c_document_id, fifo_days_used int, window_start date, home_bar, good_standing_document_id, good_standing_date | CHECK `mode <> 'fifo' OR fifo_days_used <= 60` |
| `core.representative_conflict_checks` | id, tenant_id, case_id, representative_id, check_code, result (`clear`,`disclose`,`block`), detail_code, run_at | Append-only |
| `core.delegations` | id, tenant_id, delegator_user_id, delegate_user_id, kind, actions text[], limit_minor, currency, case_scope, starts_at, ends_at, revoked_at | CHECK `ends_at <= starts_at + interval '90 days'`; no `sign_s12_5_waiver` |
| `core.dashboard_layouts` | user_id, tenant_id, dashboard_code, layout jsonb, version | Mandatory widgets enforced server-side |
| `core.aadhaar_ovse_requests` | id, tenant_id, person_id, nonce_hash, attributes_requested text[], status, expires_at, callback_received_at, credential_sha256 | TTL 120 s; no payload column exists |

### 8.2 APIs (`/v1`; Idempotency-Key on every POST that creates)

| Method and path | Purpose | Auth |
|---|---|---|
| GET `/v1/meta/login-portals` · GET `/v1/meta/login-portals/{code}` | Public portal descriptors (methods, copy keys) for vanity routes | public |
| GET `/v1/auth/portal-gate?portal={code}` | Post-login gate result (§1.5) | session |
| POST `/v1/kyc/aadhaar-ovse/requests` · GET `/v1/kyc/aadhaar-ovse/requests/{id}` | Create credential request; poll status | self aal1 |
| POST `/v1/kyc/aadhaar-ovse/callback` | UIDAI credential callback (signature-verified) | UIDAI-signed |
| POST `/v1/kyc/aadhaar-offline-ekyc` | Offline e-KYC ZIP upload (transactional; no storage) | self |
| POST `/v1/kyc/epassport-verifications` | Submit chip DG1/DG2 + SOD for passive authentication | self (mobile) |
| POST `/v1/kyc/liveness-sessions` · POST `…/{id}/result` | Liveness (vendor SDK) | self |
| POST `/v1/cases/{caseId}/representatives` (offer/request) · GET | Start an authority | party K1 / representative |
| POST `/v1/representatives/{id}:accept` · `:sign` · `:countersign` · `:narrow` · `:revoke` · `:renounce` | Lifecycle (§4.2–4.4) | party aal2 / representative aal2 |
| POST `/v1/representatives/{id}/poa` | Upload PoA for `sign_instruments_on_behalf` | party aal2 |
| GET `/v1/representatives/{id}/authority-check?action=&amountMinor=&currency=&mechanism=` | Service check | internal |
| POST `/v1/organisations/{orgId}/standing-authorities` | Enterprise panel counsel | org signatory |
| POST `/v1/law-firms` · POST `/v1/law-firms/{id}/members` · GET `/v1/law-firms/{id}/matters` | Firm accounts | firm admin |
| POST `/v1/me/foreign-counsel-registration` | BCI/FIFO record | counsel |
| POST `/v1/delegations` · POST `/v1/delegations/{id}:revoke` | Delegations | delegator aal2 |
| POST `/v1/break-glass` · POST `/v1/break-glass/{id}:approve` · POST `/v1/break-glass/{id}/review` | Break-glass (§6.6) | eligible roles |
| GET/PUT `/v1/me/dashboard-layouts/{dashboardCode}` | Widget layout | self |
| GET `/v1/me/dashboard/{dashboardCode}` | Server-composed widget data (role-filtered) | self |
| POST `/v1/admin/person-links` | Consumer–workforce link | dpo aal2-pr |

### 8.3 Events (`equator.<ctx>.<entity>.<verb>.v1`; payloads IDs/codes only)

`equator.identity.portal.signed_in.v1` (portal_code, acr, amr[], role_code) · `equator.identity.portal.denied.v1` (portal_code, reason_code) · `equator.identity.break_glass.opened.v1` (F #9) · `equator.identity.break_glass.approved.v1` · `equator.identity.break_glass.reviewed.v1` · `equator.identity.delegation.created.v1` / `.revoked.v1` · `equator.identity.person_link.created.v1` · `equator.kyc.aadhaar_ovse.verified.v1` (check_id, level) · `equator.kyc.epassport.verified.v1` · `equator.kyc.liveness.completed.v1` (score band only) · `equator.directory.representative.offered.v1` · `.accepted.v1` · `.activated.v1` (= F/P01 `mandate.activated`) · `.narrowed.v1` · `.revoked.v1` · `.renounced.v1` · `.expired.v1` · `.poa_verified.v1` · `equator.directory.representative_conflict.detected.v1` · `equator.directory.law_firm.verified.v1`. Representative events are webhook-deliverable (W) to the enterprise tenant only where the enterprise is the represented party.

### 8.4 Errors

New canonical codes (add to F.10.1): `PORTAL_ROLE_MISMATCH` 403 · `PHISHING_RESISTANT_MFA_REQUIRED` 401 · `NETWORK_POLICY_DENIED` 403 · `DEVICE_POLICY_DENIED` 403 · `MANDATE_SCOPE_INSUFFICIENT` 403 "Your authority does not cover this action." · `MANDATE_LIMIT_EXCEEDED` 403 "This is above the limit your client set. They must approve it." · `MANDATE_EXPIRED` 409 · `POA_REQUIRED` 409 "Signing for someone else needs a verified power of attorney." · `REPRESENTATIVE_NOT_PERMITTED_FOR_MECHANISM` 422 · `REPRESENTATIVE_CONFLICT` 409 · `FOREIGN_COUNSEL_SCOPE_RESTRICTED` 422 · `DELEGATION_NOT_PERMITTED` 422 · `OVSE_NOT_ENABLED` 409 · `CREDENTIAL_SIGNATURE_INVALID` 422 "We could not confirm this credential. Try again or use another method." Sub-code mapping of P01 codes (add to F.10.2): `EQ-AUTH-001/-002/-012` → `UNAUTHENTICATED`; `EQ-AUTH-003` → `OTP_LOCKED`; `EQ-AUTH-004` → `RATE_LIMITED`; `EQ-AUTH-010/-011` → `STEP_UP_REQUIRED`; `EQ-AUTH-020` → `KYC_REQUIRED`; `EQ-AUTH-030` → `FORBIDDEN`; `EQ-AUTH-031` → `MANDATE_SCOPE_INSUFFICIENT`; `EQ-AUTH-040` → `GUARDIAN_CONSENT_REQUIRED`; `EQ-KYC-001` → `PROVIDER_UNAVAILABLE`; `EQ-KYC-002` → `VALIDATION_FAILED`; `EQ-KYC-003` → `SANCTIONS_HIT_REVIEW`; `EQ-CON-001` → `CONSENT_REQUIRED`; `EQ-CON-002` → `CONSENT_REQUIRED`; `EQ-PREF-001` → `CONTACT_OUTSIDE_WINDOW`; `NEUTRAL_NOT_ACTIVE`, `ACCOUNT_SUSPENDED` → `FORBIDDEN`. Correct F.10.1 `OTP_LOCKED` text to the configured lockout (default 30 minutes, FR-P01-04).

### 8.5 Feature flags and config keys

Flags (legal flags default OFF): `kyc.aadhaar_ovse.enabled` (ON only after UIDAI OVSE approval reference is recorded), `kyc.aadhaar_offline_ekyc.enabled`, `kyc.epassport_nfc.enabled`, `kyc.digilocker_direct_requester.enabled`, `release.auth.digilocker_login`, `kyc.bar_roll_lookup.{state}`, `representation.non_advocate_arbitration` (tribunal-leave flow), `representation.poa_signing.enabled` (S-D1), `portal.committee.enabled`, `portal.partners.enabled`. Config kinds: `login_portal` (elevated), `assurance_policy` (elevated), `representation_policy` (legal), `dashboard_pack` (standard), `network_policy` (elevated), `role_bundle` (elevated).

---

## 9. Acceptance tests (Gherkin; file `tests/acceptance/appendix-S.feature`)

```gherkin
Feature: Appendix S — portals, verification, representatives, dashboards, RBAC

  Scenario: S-01 Staff portal refuses non-phishing-resistant sign-in
    Given a case manager whose workforce IdP login used password plus SMS OTP
    When the brokered login returns to "eq-portal-staff"
    Then sign-in fails with "PHISHING_RESISTANT_MFA_REQUIRED"
    And the same user signing in with a FIDO2 security key reaches "/console" with acr "eq:aal2-pr"

  Scenario: S-02 Staff network policy for escrow officer
    Given an escrow officer signs in from a public IP outside office and ZTNA ranges
    When the officer opens the escrow console
    Then access is denied with "NETWORK_POLICY_DENIED" and an audit event is written

  Scenario: S-03 Wrong portal after authentication
    Given a person who holds only the "party" role
    When they authenticate at "/arbitrator/login"
    Then they see the "Wrong door" page offering "Parties sign-in"
    And no arbitration resource is requested

  Scenario: S-04 Anti-enumeration on professional portals
    When an unknown email and a registered counsel email are submitted at "/counsel/login"
    Then both responses are identical in body and status and differ in time by less than 50 ms

  Scenario: S-05 One identity, two neutral entries
    Given a neutral empanelled as mediator and arbitrator
    When she signs in at "/mediator/login"
    Then her default space is "mediation"
    And switching to the arbitration space needs no new login
    But signing an award prompts a passkey step-up with max_age 300

  Scenario: S-06 NN-14 Aadhaar App verification stores no Aadhaar number
    Given flag "kyc.aadhaar_ovse.enabled" is ON
    When a party completes the Aadhaar App credential flow
    Then core.kyc_checks has method "aadhaar_app_avc", result "verified" and a credential_sha256
    And no column, log line or object in the evidence bucket matches a Verhoeff-valid 12-digit number

  Scenario: S-07 Unmasked Aadhaar upload is rejected
    When a user uploads an image of an Aadhaar card with all 12 digits visible
    Then the upload fails with "AADHAAR_UNMASKED_DETECTED"
    And the user is offered "Verify with the Aadhaar App" and "Verify with DigiLocker"

  Scenario: S-08 No credit bureau pulls
    When any service calls KYC_PORT with a credit-report method
    Then the call fails with "REGULATED_RAIL_TENANT_ONLY" and test "NN-14_no_bureau_pull" passes
    And the borrower sees "We cannot fetch your credit report for you"

  Scenario: S-09 Company under CIRP blocks claim filing
    Given MCA status "Under CIRP" for respondent CIN "U65999DL2015PTC123456"
    When a claimant tries to file a money claim against it
    Then filing is blocked with signposting to the Resolution Professional (IBC s.14)

  Scenario: S-10 Passport chip passive authentication
    Given an NRI party scans an e-passport whose Document Security Object signature fails CSCA validation
    Then the check result is "failed", K1 is not granted, and passport upload for manual review is offered

  Scenario: S-11 NN-27 representative limit
    Given an advocate holds "accept_offers" with accept_limit ₹5,00,000 for the respondent
    When the advocate accepts an offer of ₹7,50,000
    Then the API returns "MANDATE_LIMIT_EXCEEDED"
    And the respondent receives an approval task requiring aal2 e-sign

  Scenario: S-12 Signing on behalf needs a verified power of attorney (S-D1)
    Given an individual party's LoA grants "sign_instruments_on_behalf" without a verified PoA
    When the representative tries to sign the settlement
    Then the API returns "POA_REQUIRED" and the party is asked to sign personally

  Scenario: S-13 NN-03 waiver never delegable
    When a party tries to add "sign_s12_5_waiver" to an authority
    Then the database CHECK rejects the row and the UI shows "Always signed by you personally"

  Scenario: S-14 Revocation takes effect within 60 seconds and reroutes notices
    Given an active authority with "receive_notices" ON
    When the party revokes it at aal2
    Then the representative's open sessions lose case access within 60 seconds
    And all parties and the neutral are notified in the same transaction
    And notices issued in the previous 72 hours are re-sent to the party

  Scenario: S-15 Foreign counsel limited to foreign/international-law issues
    Given foreign counsel in fly-in/fly-out mode with 58 days used in the window
    When they record appearances on 3 more days in an India-seated INT arbitration
    Then the third appearance is blocked with "FOREIGN_COUNSEL_SCOPE_RESTRICTED"
    And appearance in a domestic COM matter is always blocked

  Scenario: S-16 Representative conflict
    Given advocate A acted for the claimant in case EQ/COM/DEL/2027/00011
    When the respondent in the same case offers authority to advocate A
    Then acceptance is blocked with "REPRESENTATIVE_CONFLICT"

  Scenario: S-17 Non-advocate barred from POSH inquiry
    When a complainant tries to appoint any representative in a POSH inquiry
    Then the option is unavailable and the help text cites POSH Rules 2013 r.7(6)

  Scenario: S-18 Enterprise dashboard has no neutral selection controls (NN-03)
    When an enterprise admin loads every enterprise and enterprise-lite screen
    Then no element exposes select, rank, prefer or veto of a neutral
    And any request carrying a neutral identifier from an enterprise principal returns "APPOINTMENT_LENDER_TRIGGER_BLOCKED"

  Scenario: S-19 Break-glass needs a second approver and DPO review
    Given a registrar requests break-glass with a 20-character justification
    Then the request fails "BREAK_GLASS_JUSTIFICATION_REQUIRED"
    When the registrar resubmits with 60 characters and the same registrar tries to approve
    Then approval fails "MAKER_CHECKER_SAME_USER"
    When the deputy registrar approves
    Then a 4-hour read-only grant is created and the DPO is notified

  Scenario: S-20 Workforce–consumer link blocks own case
    Given the DPO links case manager C's workforce account to consumer person P
    And P is a respondent in case X
    Then C cannot open or be assigned case X ("CONFLICT_DETECTED")

  Scenario: S-21 Committee member auto-recusal
    Given committee member M declared a directorship in the claimant company
    When the Challenge sub-committee agenda includes that case
    Then M has no grant to the papers and the chair is told M is recused

  Scenario: S-22 Party dashboard click budget
    Given a respondent opens a deep link for a payment due
    Then payment completes in at most 5 screens including step-up
    And the dashboard shows the free-forum reminder with its last date where signposting applies
```

---

## 10. Open items and counsel questions

1. S-R9 / S-D1 — whether an e-signed procedural LoA is a "power-of-attorney" under Powers-of-Attorney Act 1882 s.1A (and so excluded from e-signature by IT Act s.1(4) First Schedule); stamp duty on the LoA by state.
2. Non-advocate representation before arbitral tribunals under Advocates Act s.33; Mediation Act 2023 representation provision once notified.
3. UIDAI OVSE: notification number of the 9 Dec 2025 amendment regulations; fee; retention of credential hash and minimal fields for the case-record life (S7 Q2).
4. DigiLocker ToU cl.6(b) and retention of verification attributes (S7 Q4).
5. DPDP s.17(1)(a) for respondent verification data (S7 Q3).
6. Lender upload of a borrower's credit report without a tribunal direction (CICRA s.22; S7 Q5).
7. BCI Certificate and Place of Practice (Verification) Rules 2015 renewal cycle; official online State Bar rolls (P01 open item 2).
8. Indian e-passport coverage and CSCA availability in the ICAO PKD.
9. Workforce IdP choice (Entra ID vs Google Workspace) and device-compliance claim format (ADR-0003a).
10. Face-match calibration and vendor FAR/FRR evidence (S-R6).

---

## Phase addendum (paste into P01)

**FR-P01-V2-01 — Portal registry.** Implement `core.login_portals`, nine portals on eight OIDC clients (`eq-portal-parties`, `-counsel`, `-neutral` with `mediator`/`arbitrator` variants, `-staff`, `-enterprise`, `-chambers-{slug}`, `-partners`, `-committee`) with Keycloak per-client browser-flow overrides and Keycloakify variants, and the vanity routes in §2.0. *Acceptance:* each route renders its own headline, one-liner and method order from §2.2–§2.10 in en-IN and hi-IN; changing a portal's method order is a maker–checker config change; S-03 and S-04 pass.

**FR-P01-V2-02 — Post-login portal gate.** Implement §1.5 including the "Wrong door" page, application-tracker routing and default-space selection. *Acceptance:* S-03 and S-05 pass; gate decisions write `equator.identity.portal.signed_in.v1` / `.denied.v1`.

**FR-P01-V2-03 — Phishing-resistant assurance.** Add `eq:aal2-pr`; IdP mappers derive it from brokered `amr`; enforce for staff, committee and admin portals and for arbitrator signing. *Acceptance:* S-01 and S-05 pass; tenants cannot lower `min_acr` on these portals (`RULESET_GUARDRAIL_VIOLATION`).

**FR-P01-V2-04 — Workforce identities.** `core.users.is_workforce`, workforce-only brokering for `/staff/login`, membership trigger blocking party/counsel/neutral roles on workforce users, `core.person_links` with automatic conflicts. *Acceptance:* S-20 passes.

**FR-P01-V2-05 — Staff network and device policy.** `core.network_policies`, ALB mTLS for MDM certificates or IdP device-compliance claims, per-role deny/read-only behaviour (§2.6). *Acceptance:* S-02 passes; non-compliant device can read standard tier but cannot export or download.

**FR-P01-V2-06 — Committee portal.** `/committee/login` with passkey-only after a 7-day enrolment grace, sub-committee memberships via `org_unit_id`, agenda-based grants and auto-recusal. *Acceptance:* S-21 passes; committee papers are watermarked with the member's name.

**FR-P01-V2-07 — Aadhaar OVSE flows.** Flows A–D of §3.3 behind `kyc.aadhaar_ovse.enabled` / `kyc.aadhaar_offline_ekyc.enabled`; `core.aadhaar_ovse_requests`; signature verification; attribute allow-list; payload discard. *Acceptance:* S-06 and S-07 pass; flags cannot be turned ON without a recorded UIDAI OVSE approval reference.

**FR-P01-V2-08 — Method chooser v2.** SCR-P01-13 options and ordering per §3.2; K-level table §3.1 seeded in `assurance_policy`. *Acceptance:* Indian resident on mobile sees Aadhaar App first; NRI sees passport chip first; an alternative to Aadhaar is always visible.

**FR-P01-V2-09 — KYB decision rules.** MCA status rules incl. IBC s.14 / s.33(5) blocks and DIN-KYC warnings, GSTIN–PAN cross-check, Udyam MSEFC signposting hook, LEI status handling (§3.6–§3.9). *Acceptance:* S-09 passes; a GSTIN whose embedded PAN differs from the organisation PAN fails `VALIDATION_FAILED`.

**FR-P01-V2-10 — No bureau pulls.** Remove any bureau method from `KYC_PORT`; `credit_report_self` upload type; copy per §3.13. *Acceptance:* S-08 passes.

**FR-P01-V2-11 — Liveness bands and anti-injection.** Thresholds 0.85 / 0.60, attempt limits, vendor PAD evidence recorded in the vendor register, image retention ≤ 30 days. *Acceptance:* a 0.72 score routes to manual review; images older than 30 days are purged by a nightly job (test with clock skew).

**FR-P01-V2-12 — Representative types and policy.** `representation_policy` rule pack per §4.1; `representative` role code alongside `counsel`. *Acceptance:* S-17 passes; a family member cannot be added in arbitration without a recorded tribunal-leave order.

**FR-P01-V2-13 — Letter of Authority / Vakalatnama e-sign flow.** Template `eqr.tpl.loa.v2`, steps 1–7 of §4.2, scope catalogue §4.3 in `scope_v2`, limits, PoA gating (S-D1). *Acceptance:* S-11, S-12 and S-13 pass; the signed LoA hash is in the evidence ledger.

**FR-P01-V2-14 — Authority lifecycle.** Narrow, revoke, renounce, expire, suspend per §4.4 with notifications and notice rerouting. *Acceptance:* S-14 passes.

**FR-P01-V2-15 — Firm accounts and foreign counsel.** `core.law_firms`, `core.firm_memberships`, `core.foreign_counsel_registrations` with FIFO day counter and issue-of-law attestation. *Acceptance:* S-15 passes; a firm clerk cannot be given an offer scope.

**FR-P01-V2-16 — Representative conflict engine.** `RepresentativeConflictWorkflow` and `core.representative_conflict_checks` (§4.9). *Acceptance:* S-16 passes; neutral disclosure is re-triggered when a representative joins.

**FR-P01-V2-17 — Dashboards.** SCR-S-D01…D14 composed by `GET /v1/me/dashboard/{code}` with mandatory widgets, layouts per user, and the click-budget lint. *Acceptance:* S-18 and S-22 pass; no dashboard widget shows sealed data or neutral outcome statistics.

**FR-P01-V2-18 — RBAC/ABAC policies.** Cerbos policies for the ten resources in §6.2 with the condition dictionary §6.3 and hard DENY rules; policy tests generated from the matrix (one allow and one deny per non-empty cell). *Acceptance:* matrix-driven policy test suite green; every deny on high/sealed writes `audit.access_log`.

**FR-P01-V2-19 — Delegation and break-glass.** `core.delegations` (§6.4) and break-glass (§6.6) with two-person approval and DPO review. *Acceptance:* S-19 passes; delegations longer than 90 days are rejected.

**FR-P01-V2-20 — Settings shell.** Sections of §7 (billing links to Appendix O). *Acceptance:* every section works at 200% font scale; "Sign out everywhere" revokes all sessions within 60 s; legal notices cannot be switched off and the page explains why.

**FR-P01-V2-21 — Reconciliations.** Apply S-R1 to S-R8: error sub-code mapping (§8.4), F-aligned column names (`aadhaar_ref_masked`, gender values), extended `kyc_method`, `party_representatives` migration with ADR. *Acceptance:* `errors.ts` CI check passes against the updated F.10; migration reversible on a staging copy without data loss.

## Phase addendum (paste into P12)

**FR-P12-V2-01 — Portal-aware sign-in.** Welcome tiles map to `eq-portal-parties`, `-counsel`, `-neutral`, `-enterprise`; "More sign-in options" exposes `-staff` for case managers only (§2.11). *Acceptance:* selecting "I represent someone" opens the counsel client in the system browser; no embedded web view is used.

**FR-P12-V2-02 — Representative mode.** Party space shows client switcher, scope chips on every action and authority expiry banners; offer acceptance above limit shows "Your client must approve" and creates the party task. *Acceptance:* S-11 passes on Android and iOS via Maestro flows tagged `NN-27`.

**FR-P12-V2-03 — Aadhaar App same-device flow.** App-to-app credential request and App Link return (§3.3 Flow B). *Acceptance:* the credential payload is never written to SQLite, logs or crash reports (automated scan).

**FR-P12-V2-04 — e-passport NFC.** On-device MRZ + NFC read with passive authentication, liveness against the chip photo, graceful fallback when NFC is absent. *Acceptance:* S-10 passes on one Android and one iOS device; no chip image leaves the device except the DG2 hash and the liveness comparison input sent to the vendor.

**FR-P12-V2-05 — Mobile dashboards.** Party, representative, neutral (mediation/arbitration), case-manager staff tab and enterprise-lite home screens render the mandatory widgets of §5 within the P12 performance budget (≤ 4 API calls on open). *Acceptance:* cold start to interactive dashboard < 2.5 s mid-range; mandatory widgets cannot be hidden.

**FR-P12-V2-06 — Step-up on space switch.** Switching into a space whose portal policy is stronger (e.g., party → arbitrator signing) triggers step-up in the system browser with the required ACR and max_age. *Acceptance:* award signing on mobile requires a fresh passkey assertion or Aadhaar eSign with biometric step-up.

**FR-P12-V2-07 — Committee and staff push.** Committee members receive content-free push only; case managers' staff tab blocks sealed tiers. *Acceptance:* push payloads for committee and sealed events contain no names, case facts or amounts (lint).

## Phase addendum (paste into P02)

**FR-P02-V2-S1 — Service on representatives.** Notice engine applies §4.10 (scope `receive_notices`, rules-of-procedure permission, verified channel) and reverts to party addresses on authority end with the 72-hour re-send. *Acceptance:* S-14 notice assertions pass; the deemed-service record names the address that satisfied A&C Act s.3 or the rules.

## Phase addendum (paste into P03)

**FR-P03-V2-S1 — Neutral portal entries.** `/mediator/login` and `/arbitrator/login` route applicants to the application tracker and empanelled neutrals to their default space; outside party-nominated co-arbitrators receive case-scoped grants only after Appointments Sub-Committee (Case Bench) confirmation (Appendix N §1.3). *Acceptance:* an outside nominee cannot see any other case or the panel directory admin views.

## Phase addendum (paste into P13)

**FR-P13-V2-S1 — Partner portal boundary.** `/partners/login` issues `growth`-audience tokens rejected by every case-context API (`CASE_DATA_TO_GROWTH_FORBIDDEN`); advocate partners see the BCI credit-only notice. *Acceptance:* a partner token calling `/v1/cases` returns 403; nightly test confirms no case attribute in `growth` beyond the coarse referral status.

---

*End of Appendix S.*
