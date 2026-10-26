# P01 — Identity, Login, Onboarding & Consent
> Paste after 01_MASTER_PROMPT.md. Prerequisites: P00. Estimated effort: 5 sprints (2-week) for a squad of 9 (1 tech lead, 3 backend, 2 web, 2 mobile, 1 SDET), with part-time security engineer, designer, DPO and legal reviewer.

## 1. Objective and business outcome

Give every persona in master §1.5 a safe, fast, low-friction way to sign in, prove who they are to the level the action requires, accept or decline each processing purpose separately, and reach their workspace in their language — on web and on the Expo mobile shell.

Business outcomes:
- A respondent who receives a notice can open it, prove possession of the notified contact and see the notice in under 2 minutes on a low-end Android phone over 3G (drives respondent participation, D9).
- Enterprises (lenders, insurers, employers, universities) onboard with KYB, authorised signatories with authority limits and SSO, which is a procurement gate for L3/L4/L5 deals.
- The consent ledger and itemised privacy notices meet the DPDP Act 2023 + DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025) before the 13 May 2027 hard date and are consent-manager ready from 13 Nov 2026 (NN-15).
- Aadhaar is never stored in full (NN-14); POSH IC access is sealed and step-up protected (NN-07); respondents are never fed into marketing (NN-16).

## 2. Scope (in / out)

**In scope**
1. Universal login (Keycloak, themed with Keycloakify using P00 tokens) with: mobile OTP (SMS via DLT, WhatsApp authentication template, voice fallback), email magic link, password + TOTP, WebAuthn passkeys, enterprise SSO (SAML 2.0 / OIDC), DigiLocker login via a licensed provider.
2. Assurance model: authentication levels (`eq:aal1`–`eq:aal3`) and identity levels (K0–K3); step-up.
3. Sessions, refresh-token rotation, device binding (DPoP), biometric unlock, session management UI.
4. Account recovery for every persona class.
5. Invitations (generic) and respondent invitation via notice link with a secure token.
6. KYC (DigiLocker, PAN, liveness/face match, video KYC, passport/OCI for NRIs, bank penny-drop) and KYB (CIN/LLPIN, GSTIN, PAN, Udyam, LEI, foreign company + UBO + sanctions for `INT`).
7. Organisations, authorised signatories and authority limits; counsel enrolment verification and mandates.
8. Onboarding flows for all personas (party individual, organisational party, counsel, neutral application start, staff, enterprise admin + SSO, GRO/internal ombudsman, IC members, university admin/SGRC member/student, learner/trainer, partner, platform admin/support/DPO/auditor, machine identity basics).
9. Privacy notices (versioned, itemised, multilingual), purposes catalogue, consent ledger, withdrawal propagation, guardian consent, data-principal rights centre (DSR).
10. Role and tenant switching; profile and preferences (language, channels, quiet hours, blackout dates, accessibility).
11. Expo mobile shell with auth, onboarding, device binding, biometric lock, push registration, deep links, role-based navigation skeleton.

**Out of scope**
Case filing and notice generation (P02; P01 provides the invitation primitive the notice engine uses) · neutral verification, interview, empanelment, bank/payout set-up (P03) · payments (P05) · journeys and channel orchestration beyond OTP/magic link/invites (P07) · GRM/POSH case workflows (P09) · partner portal features beyond onboarding (P13) · Academy LMS beyond learner registration (P10).

## 3. Personas and permissions touched

| Persona (role code) | Entry path | Allowed login methods | MFA baseline | Identity level needed to activate |
|---|---|---|---|---|
| Party individual (`party`) | Self sign-up (website / Dispute Explorer), notice link, enterprise bulk link | Mobile OTP, email link, DigiLocker, passkey (optional) | Risk-based; aal2 for signing/payments | K0 to view; K1 to file/respond; K2 to sign |
| Organisational party user (`party_org_user`) | Self sign-up as organisation; invite by org admin; notice link | OTP, email link, password+MFA, org SSO | aal2 for signatories | K1 + KYB verified + authority verified for signatories |
| Counsel (`counsel`) | Self sign-up; invited by party; mandate request | Password + TOTP/passkey, OTP | aal2 always | K1 + enrolment check (verified or flagged) |
| Neutrals (`neutral_mediator`, `neutral_conciliator`, `neutral_arbitrator`, `neutral_expert`) | Apply on website | Password + TOTP/passkey | aal2 always | K2 (application); empanelment in P03 |
| IC (`ic_presiding_officer`, `ic_member`, `ic_external_member`) | Invited by employer admin | Password + passkey/TOTP, org SSO for employees | aal2 + step-up per sealed session | K1 (internal), K2 (external) |
| Staff (`case_manager`, `registrar`, `panel_manager`, `escrow_officer`, `safeguarding_lead`, `quality_officer`, `support_agent`, `dpo`, `auditor`) | Invited by `institution_admin` | Staff SSO or password + passkey | aal2 always | K1 + undertakings |
| `institution_admin`, `chambers_admin` | Created at tenant provisioning | Staff/tenant SSO or password + passkey | aal2 always | K1 |
| `enterprise_admin`, `enterprise_operator` | Tenant provisioning invite; JIT via SSO | Org SSO (enforced on verified domains) or password + MFA | aal2 always | K1 + KYB of tenant |
| `grievance_officer`, `internal_ombudsman` | Invited by enterprise admin | Org SSO or password + MFA | aal2 always | K1 + appointment evidence |
| `university_admin`, `sgrc_member` | Tenant invite | University SSO or password + MFA | aal2 always | K1 + institution KYB |
| `student` | University SSO or verified email domain | SSO, email link, OTP | Risk-based | K0 + enrolment; guardian if < 18 |
| `learner`, `trainer` | Academy sign-up / trainer invite | OTP, email link, password | Risk-based (trainer aal2) | K0 learner; K1 trainer |
| `partner` | Partner application | OTP, password + MFA | aal2 | K1/KYB + bank (non-advocates) |
| `platform_admin` | Equator staff only | Staff SSO + hardware-bound passkey | aal3 + JIT elevation | K2 |
| `machine` | Created by tenant admin (basic in P01; full in P09) | Client credentials (+ optional mTLS) | n/a | Tenant KYB |

New permissions: `membership:invite|grant|revoke|suspend`, `sso:configure`, `kyc:review`, `kyb:review`, `credential:verify`, `mandate:create|accept|revoke`, `signatory:authorise|revoke`, `privacy_notice:propose|approve` (DPO), `dsr:fulfil` (DPO), `break_glass:invoke`.

## 4. Functional requirements

### 4.1 Authentication architecture

**FR-P01-01 — Identity architecture.** Keycloak (ADR-0003) is the OIDC provider; one realm `equator`; Keycloak Organizations map verified email domains to tenant IdPs. The app database is authoritative for persons, memberships, roles, assurance levels and consents; tokens carry identity and authentication context only (`sub`, `acr`, `amr`, `auth_time`, `sid`, `cnf` for DPoP). Web portals use a Next.js BFF: Authorization Code + PKCE server-side, tokens kept server-side, browser holds only an encrypted `__Host-eq_sess` cookie (HttpOnly, Secure, SameSite=Lax) plus a CSRF token for mutations. Mobile uses Authorization Code + PKCE (`expo-auth-session`) with DPoP-bound tokens in SecureStore. Login UI pages are a Keycloakify theme on `auth.equatorresolution.in` sharing `packages/design-tokens` and `packages/i18n`; custom Keycloak authenticators (Java SPI) call the `identity` module over mTLS internal endpoints for OTP, magic links, DigiLocker linking and risk scoring. Keycloak DPoP is officially supported from Keycloak 26.4 (preview since 23.0); pin ≥ 26.4 and enable "Require DPoP bound tokens" per client. For public mobile clients Keycloak may bind refresh tokens only; the fallback is refresh-token-only binding with short-lived bearer access tokens, plus binding to the device key via a signed `device_assertion` parameter checked by the API.

**FR-P01-02 — Request context.** Each API call carries `Equator-Context: tenant=<uuid>; role=<role_code>[; case=<uuid>]` (acting tenant, acting role and, where applicable, acting case — master X-01); the BFF/API gateway signs the header (HMAC over the header value, request id and a 60-second timestamp) and the API rejects unsigned or stale values; the API validates it against active `core.memberships` (Redis cache 60 s, busted on membership change), sets `app.tenant_id`, and Cerbos evaluates role + attributes. A missing or invalid context returns `400 EQ-TEN-001` / `403 EQ-TEN-003`.

**FR-P01-03 — Authentication assurance levels.**

| ACR | Achieved by | Used for |
|---|---|---|
| `eq:aal1` | One factor: mobile OTP, email magic link, DigiLocker login, password | Viewing own data, Explorer, drafts |
| `eq:aal2` | Two distinct factors: password + TOTP; passkey (user-verifying); OTP + device-bound key with biometric/PIN; SSO with IdP-asserted MFA (`amr` contains `mfa`) | All professional roles; signing; payments; consent withdrawal of sealed purposes; config approval |
| `eq:aal3` | Hardware-bound, attested passkey (allow-listed AAGUIDs) with user verification, auth age ≤ 5 min | Platform admin elevation, break-glass, key/BYOK operations |

Step-up: the API returns `401 EQ-AUTH-010` with `required_acr` and `max_age`; the client restarts OIDC with `acr_values` and `max_age`. Defaults: signing settlement/award → aal2, `auth_time` ≤ 5 min; sealed workspace entry → aal2, ≤ 10 min; payout/refund bank change → aal2 + 24-hour cooling-off before first use; config approval → aal2, ≤ 10 min; DSR export download → aal2.

**FR-P01-04 — Mobile OTP.** 6-digit numeric, CSPRNG, stored only as HMAC-SHA256 with a server pepper in Redis; TTL 300 s; 3 verification attempts per code; resend after 30 s; max 5 sends per number per 30 min and 10 per 24 h; max 20 sends per IP per hour; per-number lockout 30 min after 3 failed codes. Channel order is configurable per tenant (default: WhatsApp authentication template if the user previously opted in or chose WhatsApp, else SMS; voice OTP offered after 2 failed SMS deliveries — an Equator-placed automated call, so it uses only a DLT-declared A2P CLI and stays hidden while flag `voice.equator_service_number.enabled` is OFF (master NN-12/M-05)). SMS uses the DLT-registered template and header of the principal entity (TCCCPR 2018, as amended): `{#var#} is your Equator Resolution verification code. Valid for 5 minutes. Do not share it with anyone. -Equator` (template id stored in `core.message_templates.dlt_template_id`); the message never contains case details, party names or amounts. WhatsApp uses an authentication-category template with copy-code button and no URLs. Android SMS Retriever hash appended in the mobile flow. Delivery receipts update challenge status. Numbers must be E.164; India numbers `^\+91[6-9]\d{9}$`; foreign numbers allowed for `INT` and NRI users (SMS via international route; WhatsApp preferred).

**FR-P01-05 — Email magic link.** 256-bit random token, stored as SHA-256 hash, TTL 15 min, single use, bound to the initiating browser through the OIDC `state`; if opened on a different device, the page shows a 6-digit code to type on the original device instead of logging in the second device. Sent via SES with SPF/DKIM/DMARC alignment; link domain `auth.equatorresolution.in` only.

**FR-P01-06 — Password, TOTP and passkeys.** Passwords: min 12 characters, max 128, no composition rules, checked against an offline breached-password list (top 10 million) and contextual words (name, email, "equator"); Argon2id hashing in Keycloak. TOTP: RFC 6238, SHA-1, 6 digits, 30 s, ±1 step. WebAuthn passkeys: platform and roaming, `userVerification = required`, resident keys preferred; up to 10 passkeys per user. Recovery codes: 10 single-use, 10-character base32, shown once, regenerable with aal2. Professional roles (table §3) cannot complete onboarding without enrolling a second factor.

**FR-P01-07 — Enterprise SSO.** Per tenant: SAML 2.0 (SP metadata per tenant, signed assertions required, SHA-256, IdP-initiated disabled by default, clock skew 120 s, NameID = email) or OIDC (discovery URL, client secret in Secrets Manager, PKCE, `email_verified` required). Domain verification by DNS TXT `equator-verification=<token>`; once verified and "Enforce SSO" is ON, password/OTP login is refused for that domain except for 2 named break-glass admins. JIT provisioning creates `core.users` + `core.memberships` using group→role mappings (`core.sso_connections.role_mappings`); unmapped users get no membership and see "Ask your administrator". Optional SCIM 2.0 (RFC 7643/7644) at `/scim/v2/Users` and `/scim/v2/Groups` with a tenant-scoped bearer token; `active=false` revokes memberships and sessions within 60 s. Without SCIM, users inactive 90 days are suspended. Staff of Equator use the Equator staff IdP via the same mechanism.

**FR-P01-08 — DigiLocker login and data (NN-14).** Through a licensed DigiLocker partner (`KYC_PORT`, default Surepass; R3 §3.3), the user authorises DigiLocker; Equator receives name, DOB, gender, photo, address and the Aadhaar number in masked form only. Persist: `id_reference` (provider request id), `aadhaar_last4`, name, DOB, issuer, document type, fetched-at, and the photo (encrypted, used only for face match, deleted 30 days after verification unless consented otherwise). The full Aadhaar number, XML and QR payload are never persisted or logged; a DB CHECK rejects any 12-digit value in Aadhaar-labelled columns. Aadhaar OTP e-KYC is not performed by Equator (Aadhaar Act 2016 ss.4(4), 8 restrict authentication to requesting entities; R3 §3.3). "Sign in with DigiLocker" links the DigiLocker identity to the account on first use (after OTP verification of a contact point) and later serves as an aal1 login method.

**FR-P01-09 — Sessions and tokens.** Access token JWT 10 min, audience-scoped; refresh token opaque, rotating, reuse detection (a replayed refresh token revokes the whole token family and all sessions of that device, and alerts the user); DPoP-bound on mobile.

| Role class | Web idle timeout | Web absolute | Mobile refresh lifetime (sliding) | Concurrent sessions |
|---|---|---|---|---|
| Party, learner, student | 30 min | 12 h | 30 days | unlimited (listed) |
| Professionals (counsel, neutrals, staff, enterprise, GRO, university, partner, trainer) | 15 min | 12 h | 14 days | 5 |
| Sealed roles (IC) | 10 min | 8 h | 7 days; no offline cache | 2 |
| `platform_admin`, `dpo` | 15 min | 8 h | not allowed on mobile | 2 |

Sessions are revoked on: password change, factor removal, role/membership revocation, mandate revocation (case-scoped grants only), tenant suspension, de-empanelment (P03), SCIM deactivation, user "sign out everywhere", detected refresh reuse. All sessions are listed in SCR-P01-41 with device, approximate location (city from IP; IP itself stored as HMAC), last active.

**FR-P01-10 — Device binding and biometric unlock (mobile).** On first sign-in the app creates a P-256 key pair in the platform keystore (iOS Secure Enclave with `biometryCurrentSet` access control; Android Keystore, StrongBox where available, `setUserAuthenticationRequired`) via an Expo config plugin module (ADR-0031), registers the public key (`core.device_bindings`), and signs DPoP proofs with it. App attestation (Play Integrity standard request; Apple App Attest) is recorded; failure lowers the session to aal1 and raises the risk score but does not block parties; it blocks sealed roles and `platform_admin` on mobile. App lock after 5 min in background (configurable 1–15): unlock with biometric (Class 3 / Face ID / Touch ID) or a 6-digit app PIN; 5 wrong PINs → full re-login. A change in enrolled biometrics invalidates the key and forces re-login + re-binding. Rooted/jailbroken devices: warning for parties; blocked for sealed roles. Logout wipes SecureStore, SQLite offline cache and image cache ("remote wipe" on server-side device revocation at next app foreground).

**FR-P01-11 — Account recovery.**

| Persona class | Primary recovery | If primary fails | Safeguards |
|---|---|---|---|
| Party / learner / student | OTP to any other verified contact point + DigiLocker re-auth (name/DOB match ≥ 0.85) | Assisted recovery: support agent schedules video verification against the KYC photo | 72-hour hold before contact-point change takes effect; notices to all old contact points; payments/refund bank changes frozen 7 days |
| Professionals | Recovery code, or second registered passkey/TOTP | Tenant admin–initiated reset + liveness face match vs KYC photo | 24-hour cooling-off for payout bank changes; admin cannot reset another admin of the same tenant alone (2 admins) |
| SSO users | Handled by the organisation's IdP | — | Equator cannot bypass enforced SSO |
| IC members | Recovery code + employer admin confirmation | Video verification | All sealed sessions revoked; IC presiding officer notified |
| `platform_admin` | Second hardware key | Two other platform_admins + CTO approval | Break-glass procedure in `docs/runbooks/admin-recovery.md` |

Changing a mobile number or email requires OTP to both old and new contact, or (if the old is lost) the recovery path above.

### 4.2 Invitations

**FR-P01-12 — Generic invitations.** `core.invitations` supports kinds `tenant_member`, `org_member`, `counsel_mandate`, `ic_member`, `staff`, `trainer`, `respondent_notice`, `co_party`. Token: 128-bit+ random, URL-safe base62 22 characters; only its SHA-256 is stored; TTL default 14 days (members), configurable; single binding; revocable; resend generates a new token and invalidates the old. Invitee must verify the contact point the invitation was addressed to (possession) before binding. Acceptance creates the membership/role grant and records the inviter. Expired → status `expired`, audit, inviter notified.

**FR-P01-13 — Respondent invitation via notice link.** P02 notices embed `https://equatorresolution.in/r/{code}` (domain registered on the TRAI URL whitelist for SMS; R2 §12). Rules:
1. `GET /r/{code}` (no login) shows only: institution name, case number, claimant display name (organisation name or individual's first name + initial), notice date, response due date, languages available, and actions "This is me", "This is not me", "Read in another language". No allegations, amounts or documents.
2. "This is me" sends an OTP to the exact contact point the notice was sent to; success binds the invitation to an existing account with that verified contact or creates a K0 account.
3. The respondent privacy notice (SCR-P01-11, respondent variant) explains that dispute-administration processing relies on the DPDP s.17(1)(a) exemption (processing necessary for enforcing a legal right or claim) — and on s.7(e) where an award, judgment or order is being complied with — not on consent; optional purposes are presented separately and unticked; marketing consent is not offered in this flow (NN-16).
4. After binding, the notice and documents are visible (aal1). A formal response requires K1 (FR-P01-15).
5. "This is not me" records `misdirected_notice`, suppresses further messages to that contact for this case, creates a case-manager task, and shows the user how to report misuse; no account is created and the contact is retained only as long as needed to evidence the misdirection.
6. Link validity = response window + 90 days; after that `/r/{code}` shows "Link expired — request a new one" which re-sends a link only to the originally notified contact. Rate limit 10 lookups per IP per hour; invalid codes return the same neutral page (no enumeration).
7. Counsel may claim on behalf of the respondent only through a mandate (FR-P01-23) signed by the respondent.

### 4.3 KYC and KYB

**FR-P01-14 — Identity levels and assurance policy.** Identity levels: **K0** contact verified (mobile or email OTP); **K1** identity evidenced (DigiLocker document fetch, or PAN verification with name + DOB match, or passport verification for foreign nationals/NRIs); **K2** K1 + passive liveness + 1:1 face match against the DigiLocker/ID photo; **K3** K2 + video KYC with a trained Equator agent. Which level each action needs is the config kind `assurance_policy` (Ruleset Studio, risk class `elevated`); defaults in §9. Name matching: normalised (case, honorifics, initials expanded, transliteration via ICU) Jaro-Winkler ≥ 0.85 auto-pass, 0.70–0.85 manual review, < 0.70 fail. Face-match threshold and liveness pass criteria per provider are configuration (default face-match score ≥ 0.80) **[VERIFY — open (vendor): provider-specific calibration; obtain FMR/FNMR per ISO/IEC 19795-1 and PAD report (ISO/IEC 30107-3) before go-live; Equator policy: a low score never auto-rejects — it routes to retry, manual review or video KYC]**.

**FR-P01-15 — Individual KYC methods.**
- **DigiLocker** (preferred): FR-P01-08; documents fetched: Aadhaar (masked), PAN, driving licence as chosen by the user (consent screen lists each document).
- **PAN verification**: format `^[A-Z]{5}[0-9]{4}[A-Z]$`, 4th character must match holder type (`P` for individuals); verify name/DOB via provider; store `pan_enc`, `pan_bidx`, `pan_masked` (`ABCDE****F`).
- **Liveness + face match**: provider SDK (web and React Native) with passive liveness; selfie retained encrypted max 30 days, then only the score, decision and provider reference.
- **Video KYC** (K3): booked slot 09:00–18:00 IST; agent script with randomised questions; ID document shown on camera; geotag + IP captured; maker–checker (agent + reviewer); recording encrypted in the evidence bucket with retention per `retention_schedule` (default: 8 years where linked to a case, else 3 years after account closure). Equator is not an RBI-regulated entity; where a lender tenant needs RBI V-CIP, it runs through the lender's own regulated set-up (NN-14) (RBI (Non-Banking Financial Companies – Know Your Customer) Directions, 2025, 28 Nov 2025, paras 26–27; or the RE's own KYC Directions 2025, e.g. Commercial Banks – KYC Directions 2025).
- **Manual review**: uploaded ID (passport, voter ID, driving licence) with OCR by the KYC provider and human review in SCR-P01-45; Aadhaar uploads are refused unless the image is the masked e-Aadhaar (first 8 digits masked).

**FR-P01-16 — NRIs and foreign nationals.** Passport (Indian `^[A-Z][0-9]{7}$` or foreign, MRZ check-digit validation), OCI card (number and copy), visa/residence permit optional, overseas address with proof (≤ 3 months old), foreign mobile, timezone; K2 via liveness against passport photo; K3 video KYC when no DigiLocker, when risk score ≥ 70, or when the case is `INT` and the person is a signatory. Sanctions screening (`SANCTIONS_PORT`) on name + DOB + nationality for every `INT` participant (NN-19).

**FR-P01-17 — Bank account verification.** Penny-drop (₹1 IMPS with beneficiary name) or penniless name lookup via `KYC_PORT` (default Surepass; fallback Razorpay Fund Account Validation); IFSC `^[A-Z]{4}0[A-Z0-9]{6}$`; name match ≥ 0.80 to the KYC/KYB name; stored `account_enc`, `account_masked` (`XXXXXX4321`), IFSC, bank name, verified_at. Mandatory before any refund to a party, payout to a neutral/trainer/IC external member, or partner commission. A change triggers step-up + 24-hour cooling-off and notifications to all contact points.

**FR-P01-18 — Domestic KYB.** Organisation types: `private_ltd`, `public_ltd`, `opc`, `section8`, `llp`, `partnership`, `proprietorship`, `huf`, `trust`, `society`, `cooperative`, `bank`, `nbfc`, `hfc`, `mfi`, `insurer`, `tpa`, `broker`, `govt_body`, `university`, `foreign_company`, `other`. Checks (each a `core.kyb_checks` row): CIN `^[LU][0-9]{5}[A-Z]{2}[0-9]{4}[A-Z]{3}[0-9]{6}$` or LLPIN `^[A-Z]{3}-[0-9]{4}$` via MCA data (name, status, date of incorporation, registered office, directors/designated partners); GSTIN `^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z][1-9A-Z]Z[0-9A-Z]$` (legal/trade name, status, state code; PAN embedded in characters 3–12 must equal the organisation PAN); PAN (4th character must match entity type: C company, F firm/LLP, T trust, H HUF, A AOP, G government, L local authority, J artificial juridical person); Udyam `^UDYAM-[A-Z]{2}-[0-9]{2}-[0-9]{7}$` (MSME category — enables MSMED Act paths in P08); LEI (ISO 17442, 20 characters, mod-97 check) via the GLEIF public API. Regulator registration fields: RBI Certificate of Registration number (NBFC/HFC), IRDAI registration (insurer/TPA/broker), SEBI registration (SEC). MCA status handling: `Active` → proceed; `Strike Off`, `Under Liquidation`, `Amalgamated`, `Dissolved`, `Under CIRP` → organisation may still be a party but is flagged for case-manager review and cannot hold an enterprise subscription. KYB results are re-checked every 12 months for tenants and on each new case for parties older than 6 months.

**FR-P01-19 — Authorised signatories and authority limits.** Each organisation has ≥ 1 signatory before it can file, respond, settle or subscribe. Signatory record: person (K1 minimum), designation, authority evidence type (`board_resolution`, `power_of_attorney`, `authority_letter`, `partner_resolution`, `proprietor_self`, `trust_resolution`), document (certified true copy signed by a director/company secretary/designated partner), resolution date, validity from/to, and an **authority matrix**: allowed actions (`file`, `respond`, `negotiate`, `make_offer`, `accept_offer`, `sign_settlement`, `sign_s12_5_waiver`, `sign_arbitration_agreement`, `appoint_counsel`, `pay`, `manage_members`), mechanisms allowed, verticals allowed, monetary limit per instrument (₹ minor units and currency), dual-signature threshold (default ₹10,00,000 — above it two signatories must sign), and case scope (`all` or listed). `AuthorityService.check(orgId, personId, action, amountMinor, currency, mechanism)` is the single enforcement point used by P04–P06; denials return `403 EQ-AUTH-030` with the missing authority. For `sign_s12_5_waiver` (NN-03), the authority must be specific (generic "all actions" does not satisfy it) and is checked at signing time. Revocation is immediate, notifies the organisation's admins and any open counterparties' case managers, and is audited. Organisation admins (party org) manage members; adding a signatory requires KYB reviewer approval when the evidence is uploaded rather than verified from MCA director data.

**FR-P01-20 — Foreign company KYB, UBO and sanctions (`INT`, NN-19).** Fields: legal name (original script + Latin transliteration), jurisdiction of incorporation (ISO 3166), registration number, registry name, date of incorporation, registered address, LEI (mandatory if available), tax ID, certificate of incorporation, certificate of good standing/incumbency (≤ 6 months old), register of directors, shareholding chart; apostille/legalisation flag per document. Beneficial owners: every natural person holding > 10% ownership or control, or exercising control by other means, captured with name, DOB, nationality, residence, % and nature of control, PEP self-declaration; threshold per PML (Maintenance of Records) Rules 2005 r.9(3), as amended by the PML (Maintenance of Records) Amendment Rules 2023 (notified 7 Mar 2023): > 10% for companies and partnerships (adopted as Equator policy; Equator is not a PMLA reporting entity); where no natural person qualifies, the senior managing official is recorded. Sanctions screening of the entity, UBOs, directors and signatories against UN Security Council Consolidated List, OFAC SDN, EU Consolidated, UK HMT/OFSI and MHA (UAPA designated individuals/organisations) lists via `SANCTIONS_PORT`; potential matches (score ≥ 0.85) block activation and go to `kyb_review` with two-person decision; monthly re-screening while any `INT` matter is open. Also captured for `INT`: FEMA payment-route flag (current/capital account) and DPDP s.16 transfer basis record — the case-level gate runs in P02/P08 (NN-19).

**FR-P01-21 — Risk score.** Deterministic score 0–100 (rules in config `assurance_policy.risk_rules`): +40 sanctions potential match, +25 PEP declaration, +20 name mismatch in review band, +15 foreign national without DigiLocker, +15 more than 3 devices in 24 h, +10 attestation failure, +10 claim/authority value ≥ ₹1,00,00,000, +10 recent recovery. ≥ 70 → K3 required before signing or receiving funds; ≥ 90 → account restricted pending review. No AI is used for scoring (NN-01).

**FR-P01-22 — Counsel enrolment verification.** Counsel enter State Bar Council, enrolment number (validated against per-state patterns in config, e.g., `D/1234/2015`, `MAH/1234/2010`, `R/123/2012`), enrolment date, and upload the enrolment certificate, Bar Council identity card and Certificate of Practice under the BCI Certificate and Place of Practice (Verification) Rules, 2015 [Verified 22 Oct 2026: CoP valid 5 years and verified every 5 years, application up to 6 months before expiry — BCI CoP Rules 2015 r.9.1]. Verification channels in order: (1) adapter lookup where a State Bar Council publishes an official online roll (`KYC_PORT.lookupBarRoll`, enabled per state in config; no scraping of unofficial sources) **[VERIFY — open (State Bar Council): official portals exist in some States (e.g., Bar Council of Delhi enrolment status) but no API/terms; enable `lookupBarRoll` per State only with the Council's written permission — else staff-assisted check on the official portal]**; (2) human verification by `support_agent` with second-person check by `registrar` (SCR-P01-45), including name match to K1 identity. Statuses: `unverified`, `pending_review`, `verified`, `rejected`, `expired` (annual re-verification). Until verified, counsel may still act under a mandate but every case participant sees the badge "Authorised representative — enrolment not verified"; verified counsel show "Advocate — enrolment verified on DD MMM YYYY". Non-advocate representatives (`representative_type = authorised_representative`) are supported for mediation/conciliation with an authority letter and no Bar check. Foreign counsel in `INT` matters record home-bar admission and certificate of good standing; participation follows the BCI Rules for Registration and Regulation of Foreign Lawyers and Foreign Law Firms in India, 2022 (notified Mar 2023; amended by Gazette notification of 13 May 2025). Under these, foreign counsel may act in international arbitrations in India only for a client whose principal office is abroad and only on issues of foreign law and/or international law. Unregistered fly-in/fly-out practice is capped at 60 days in any 12-month period and requires a Form C declaration. See also *Bar Council of India v A.K. Balaji* (2018) 5 SCC 379 (SC, 13 Mar 2018). Referral payouts to advocates are disabled (NN-17).

**FR-P01-23 — Counsel mandates.** Created by a party ("Invite my lawyer") or requested by counsel ("Request mandate" — the party must accept). Fields (per F-19): party, organisation (if any) and signatory, counsel, case (nullable in P01; bound in P02) or `organisation_standing` scope (panel counsel for an enterprise), scope flags `view_documents`, `file_documents`, `attend_sessions`, `negotiate`, `receive_notices` (service on counsel counts as service only if this flag is set and the procedure rules allow), `make_offers`, `accept_offers`, `sign_settlement_on_behalf` (default false; when false the party signs personally), validity dates, fee arrangement note (non-contingent; NN-18). `sign_s12_5_waiver` can never be delegated to counsel (NN-03: the waiver is captured per party by its own express written agreement). The mandate PDF is generated, signed by the party (platform OTP signature at aal2; Aadhaar eSign where the procedure rules require), hashed into the evidence ledger, and accepted by counsel. Revocation by party or counsel is immediate: case-scoped `core.role_grants` end, cached permissions bust within 60 s, open sessions lose access to that case, all parties and the neutral are notified.

### 4.4 Persona onboarding flows

**FR-P01-24 — Party individual.** Sign-up → contact verification (K0) → itemised privacy notice and purpose choices (SCR-P01-11) → profile (SCR-P01-12: fields from F1/F-L01/F-I01/F-W01/F-01 common core) → optional KYC now or deferred until required by `assurance_policy` → dashboard. Vertical-specific profile extensions are captured at case intake in P02 (e.g., loan account reference, policy number, employee ID, marriage details), not at sign-up, to minimise data (DPDP s.6(1) purpose limitation). Vulnerability self-declaration (optional; never shown to the other side; master §5 CaseParty) is offered at intake (P02), not here.

**FR-P01-25 — Organisational party.** Sign-up as "an organisation" → user K1 → organisation KYB (SCR-P01-19) → signatory authority (SCR-P01-20) → members (SCR-P01-21) → bank verification optional (needed for refunds) → for `INT`, SCR-P01-22. If the organisation already exists (matched by CIN/LLPIN/GSTIN/LEI), the user requests to join; an existing org admin approves; if none exists, a KYB reviewer verifies the requester's authority.

**FR-P01-26 — Neutral application (start).** Public "Apply as a neutral" → account with password + mandatory TOTP/passkey (aal2) → K2 → PAN verification → application wizard `eqr.form.neutral_application.v2` (C4 §C.12/C.13; C1 F3) with autosave: (1) Personal — name as per ID, DOB, gender (optional; used only for anonymised panel-diversity statistics with consent), nationality(ies), languages with proficiency (speak/read/write), cities and seats, time zone, photo; (2) Roles and categories — `mediator`, `conciliator`, `arbitrator`, `expert`, `posh_external_member`; verticals FIN/COM/FAM/INS/WRK/INT; specialisations; (3) Credentials — Bar enrolment (reuses FR-P01-22), retired judicial office (court, rank, retirement date), professional body (ICAI, ICSI, ICMAI, IBBI IP registration, IRDAI surveyor licence, actuarial, engineering), accreditations with training hours (court-annexed/MCPC 40-hour, IIAM, CIArb, IMI, others) and certificates, matters handled by type/role/value band, CV (PDF ≤ 5 MB); (4) Integrity — conflict declarations (employment, directorships, retainers, lender/insurer/enterprise relationships in the last 3 years with names), disciplinary history, pending criminal proceedings declaration; (5) References — 3 referees (name, designation, email, relationship); (6) Practice — availability pattern, preferred fee grade, `INT` rate card currency (USD/EUR/GBP/SGD/AED); (7) Declarations — truth, versioned Code of Conduct acknowledgement, privacy notice, granular public-profile display consent (photo, bio, languages, city — each separate). Submit → status `submitted`, event `equator.neutrals.application.submitted.v1`; verification, interview, Academy, empanelment, bank/GST and payouts are P03. The applicant sees a status tracker (submitted → under verification → interview → decision) fed by P03.

**FR-P01-27 — Staff onboarding.** `institution_admin` invites with role(s); invitee signs in with Equator staff SSO (or password + passkey) → K1 → acknowledgements stored as consent-ledger records of kind `undertaking`: confidentiality undertaking, Code of Conduct, information-security policy, DPDP training attestation (date, module version) → conflict declaration (relationships with enterprises, lenders, insurers, employers, law firms in the last 3 years) → role activation. Segregation-of-duties rules (`role_bundle` guardrails, C1 §L.2): `escrow_officer` cannot hold `case_manager` or `quality_officer` in the same tenant; `quality_officer` cannot hold `case_manager`; nobody can be maker and checker on the same change. `auditor` grants are time-bound (max 90 days), scoped (tenant, modules, date range) and read-only.

**FR-P01-28 — Enterprise tenant and admin.** Platform admin provisions the tenant (P00) and invites the first `enterprise_admin`. The admin: K1 → enterprise KYB (FR-P01-18, regulator registration fields) → authorised signatory for the platform agreement → e-acceptance of the Master Services Agreement, Data Processing Agreement and Equator rules (each a versioned undertaking record) → SSO set-up (SCR-P01-30) → invite operators, GROs and IC admins → organisation units (branches/business lines) for scoping operators. The tenant record stores `commercial_relationship = true` so P02 discloses the paid relationship to counterparties (NN-16).

**FR-P01-29 — GRO and Internal Ombudsman.** Invited by `enterprise_admin` in a `grm_client` tenant; fields: designation, employee ID, official email (verified domain), official phone, office address, appointment letter (upload), role flags `principal_nodal_officer`, `grievance_officer` level (1/2), `internal_ombudsman` (requires independence declaration and appointment evidence under the RE-specific RBI Internal Ombudsman Directions, 2026 of 14 Jan 2026 (e.g. Reserve Bank of India (Non-Banking Financial Companies – Internal Ombudsman) Directions, 2026, RBI/CEPD/2025-26/384; Commercial Banks – RBI/CEPD/2025-26/381), which repealed the IO Directions for Regulated Entities, 2023 (29 Dec 2023)); public-display consent for the name, designation and contact details that regulated entities must publish (C1 §L.3; R2 §6.1) — displayed in recovery-related messages per NN-12. MFA mandatory.

**FR-P01-30 — IC members (sealed, NN-07).** Invited by the employer's POSH admin. Onboarding happens inside the sealed workspace: K1 for employees (K2 for `ic_external_member`) → aal2 factor enrolment (passkey or TOTP; SMS OTP not permitted as second factor for sealed roles) → confidentiality undertaking referencing POSH Act 2013 s.16 (prohibition of publication) and s.17 (penalty) → conflict declaration. External member additionally: affiliation (NGO/association committed to the cause of women, or person familiar with issues relating to sexual harassment — POSH Act s.4(2)(c)), CV, bank verification for per-sitting fees (POSH Act s.4(4); POSH Rules 2013 r.3 — statutory floor ₹200/day plus travel, payable by employer; eligibility criteria for external members are r.4), PAN. Gender declaration is stored only in `posh_sealed.ic_members` and used solely to validate composition (presiding officer a woman employed at a senior level, s.4(2)(a); at least one-half women, s.4(2) proviso). Each sealed session requires step-up (aal2, auth age ≤ 10 min); screens are screenshot-protected; no mobile offline cache; every read is written to `audit.access_log`. The core `identity` module stores only the membership with role code and an opaque `sealed_ref`.

**FR-P01-31 — University, SGRC and students.** `university_admin`: K1 → institution KYB (name, AISHE code, UGC/AICTE recognition reference, PAN, GSTIN optional, address) → SSO (Google Workspace for Education / Microsoft Entra) or verified email domains → invite `sgrc_member`s (role only; SGRC constitution and clocks under the University Grants Commission (Redressal of Grievances of Students) Regulations, 2023 are P09). Students sign in via university SSO, or email magic link restricted to verified domains, plus enrolment number, programme and year; DOB triggers the child flow if under 18 (FR-P01-39). Student data for Academy/Campus is segregated from live case data (C5 §B.8); grievance filings (P09) live in the GRM tenant scope.

**FR-P01-32 — Learner and trainer.** Learner registration (academy tenant) implements Academy form F-01 (C5 §A.3): full name, institution + enrolment number (optional), programme + year, email, mobile, DOB, optional dietary/accessibility needs, emergency contact; one mandatory processing consent plus optional, unbundled marketing and results-publication consents (never pre-ticked); notice version + timestamp stored; under-18 → guardian consent (F-03: guardian identity, document sighted, reference, verified by). Trainer: invitation → K1 → PAN → bank verification → trainer agreement undertaking.

**FR-P01-33 — Partner.** Application: partner type (`ca`, `cs`, `cma`, `law_firm`, `advocate`, `hrms_vendor`, `dsa`, `university`, `association`, `other`), individual or organisation (KYC/KYB), professional membership number (ICAI 6-digit; ICSI `ACS`/`FCS` + number; Bar enrolment for advocates), GSTIN, PAN, bank verification (not collected for advocates — BCI-compliant mode: credits/co-counsel only, no cash commission; NN-17), referral programme terms (versioned undertaking), neutrality disclosure acknowledgement (NN-16: partner status is disclosed to counterparties; "priority" affects administrative speed only). Approval by Equator growth team (maker–checker). Partner records are written to the `growth` schema; no case data is visible to partners beyond referral status.

**FR-P01-34 — Platform staff and machine identities.** `platform_admin`: Equator staff SSO + attested hardware passkey (aal3); base login grants read-only operations; privileged actions require JIT elevation (`POST /v1/admin/elevations`) approved by another platform_admin, maximum 4 hours, reason mandatory, audited, DPO notified for elevations that include cross-tenant data scope. `support_agent`, `dpo`, `auditor` as FR-P01-27. `machine`: tenant admin creates an OAuth client (client credentials, secret shown once, or private-key JWT; optional mTLS) with scopes; full API-key product in P09.

### 4.5 Consent, notices and rights (NN-15, NN-16)

**FR-P01-35 — Privacy notices.** Config kind `privacy_notice` (Ruleset Studio, risk class `legal`, DPO approval mandatory). Each notice version per tenant and locale contains, itemised: personal data categories collected; the specified purpose for each category; the goods/services or uses enabled; retention period per category; lawful basis; recipients/processors (by category); cross-border transfer (only `INT`, with s.16 basis); how to withdraw consent (link, as easy as giving it — DPDP s.6(4)); how to exercise rights (ss.11–14); how to complain to the Data Protection Board (s.5(1)(iii)); contact of the grievance officer/DPO (s.8(9)–(10)); date and version. Notices are standalone (not inside terms), plain language, and available in English, Hindi and the 10 configured Indian languages, with any other Eighth Schedule language provided on request (DPDP s.5(3)); DPDP Rules 2025 r.3 (in force 13 May 2027) requires a stand-alone notice, understandable independently, with an itemised description of personal data and specified purposes and the means to withdraw consent, exercise rights and complain to the Board. Every translated notice requires `legal_approved` status (NN-23). `content_sha256` is stored and referenced by each consent record.

**FR-P01-36 — Purposes catalogue.** Platform purposes (`core.consent_purposes`, tenants may add tenant-specific purposes; codes are stable):

| Code | Purpose | Basis | Default |
|---|---|---|---|
| `account_login` | Create and secure your account | consent | required for account |
| `identity_verification` | Verify identity/organisation (KYC/KYB), sanctions screening | consent; legal obligation for `INT` screening | required when an action needs K1+ |
| `dispute_administration` | Administer disputes you file or respond to | consent (filer); s.17(1)(a) (respondent and third-party data before engagement); s.7(e) for compliance with awards/orders | required to file |
| `service_communications` | Notices, reminders, OTPs by SMS/email/push | consent / s.17(1)(a) | required |
| `whatsapp_channel` | Receive service messages on WhatsApp | consent (explicit opt-in) | off |
| `voice_ai_calls` | Automated voice calls (P07; `legal.voice.ai_outbound`) | consent | off |
| `session_recording` | Recording of arbitration hearings (case-level, P04) | consent | off |
| `health_data` | Health information in insurance disputes (sealed) | explicit separate consent (F-I01) | off |
| `family_safety_data` | Safety information in family matters (sealed) | explicit separate consent | off |
| `ai_assisted_processing` | AI classification/extraction/drafting on your submissions (NN-01; deterministic path if declined, NN-02) | consent | off |
| `neutral_public_profile_*` | Display of photo/bio/languages/city (one purpose each) | consent | off |
| `academy_registration`, `academy_results_publication`, `media_release` | Academy | consent | first required; others off |
| `marketing_communications` | News, offers, events | consent, unbundled | off; never offered to respondents in notice flows |
| `research_anonymised` | Use of anonymised data for research | consent, never bundled | off |
| `payments_tax` | Invoices, GST, TDS records | legal obligation | required when paying |
| `cross_border_transfer` | Transfer outside India for `INT` | s.16 recorded basis + notice | case-level |

**FR-P01-37 — Consent ledger.** Every give/withdraw writes an immutable `core.consent_records` row: principal (person), tenant (data fiduciary context), purpose code, basis, status (`given`, `withdrawn`, `expired`, `superseded`), notice id/version/locale/content hash, capture surface (screen id + UI copy hash), channel (`web`, `mobile`, `whatsapp`, `ivr`, `assisted`, `api`), actor (self, guardian, assisted operator with principal confirmation), evidence (timestamp, IP HMAC, user-agent hash, OTP challenge id for assisted/remote capture), guardian link id, consent-manager artefact id (nullable, for DPDP s.6(7)–(9) integration behind `legal.consent.consent_manager_integration`), expiry (marketing: 12 months then re-consent). Records are retained ≥ 7 years (C1 §L.3) and hash-anchored through the audit chain. No pre-ticked boxes; required and optional purposes are visually separate; declining an optional purpose never blocks the service.

**FR-P01-38 — Withdrawal propagation.** Withdrawal is one tap from SCR-P01-42 (aal1; aal2 for sealed purposes). Event `equator.consent.consent.withdrawn.v1` drives `ConsentWithdrawalPropagationWorkflow`: comms suppression ≤ 5 min; WhatsApp opt-out sync ≤ 5 min; neutral public profile element unpublished ≤ 1 h; marketing CRM/audience deletion in `growth` ≤ 24 h; academy publication removal ≤ 24 h; processors notified ≤ 72 h; research exclusion from the next extract. The UI explains what continues and why (e.g., processing needed to administer a pending case under s.17(1)(a), tax records under law). Completion is recorded per consumer; any consumer not confirming in its SLA raises a DPO task.

**FR-P01-39 — Children and persons with disability (DPDP s.9).** DOB is mandatory where an account holder may be a minor (students, learners, family-matter parties). If age < 18, the account stays `pending_guardian` until a guardian completes verifiable consent: the guardian is an adult with K1 identity whose age is confirmed (DigiLocker DOB or PAN DOB), declares the relationship, optionally uploads proof, and gives consent per purpose; the record links child and guardian. Child accounts: no marketing, no behavioural tracking or analytics profiling, no targeted content (s.9(3)); product analytics events are dropped for them. For a person with disability who has a lawful guardian, the guardian uploads the appointment order (court order or limited guardianship under the RPwD Act 2016 s.14 / National Trust Act 1999) and a reviewer verifies it (DPDP Rules 2025 r.10 — children: verifiable parental consent; adult = 18+, verified via existing reliable details, voluntarily provided details or a virtual token incl. DigiLocker; r.11 — persons with disability: lawful guardian appointed by a court, RPwD Act designated authority or National Trust Act local-level committee; exemptions r.12 + Fourth Schedule; in force 13 May 2027).

**FR-P01-40 — Data-principal rights centre.** Requests: access (summary of personal data and processing, s.11), correction/completion/updating (s.12), erasure (s.12, subject to legal hold and s.17(1)(a)), nomination of a person to exercise rights on death or incapacity (s.14), grievance (s.13). Identity re-verification (aal2) before fulfilment; internal SLA 30 days; DPDP Rules 2025 r.14(3) sets a grievance-redressal outer limit of 90 days (no separate fixed period for rights requests; in force 13 May 2027); access exports are JSON + PDF in the exports bucket (7-day link). Partial refusals cite the reason (pending dispute, legal obligation, legal hold). The DPO queue (SCR-P01-46) tracks SLA clocks.

**FR-P01-41 — Neutrality firewall at identity level (NN-16).** Persons whose first contact is a notice (`origin = respondent_notice`) carry `marketing_eligible = false` permanently unless they later give `marketing_communications` consent from the privacy centre on their own initiative; no identity, contact or case attribute is ever written to `growth` for them; growth sync jobs filter on this flag and a nightly test asserts zero overlap between respondent persons and `growth.leads`.

### 4.6 Account experience

**FR-P01-42 — Role and tenant switching.** A person may hold many memberships (tenant × role). The switcher (SCR-P01-38) lists them grouped by tenant with brand colour band and role chip; switching calls `POST /v1/me/context`, which validates the membership, requires step-up when entering sealed or admin roles, rotates the CSRF token, writes an audit event and reloads navigation. Deep links carry tenant context (`/t/{tenantSlug}/…`); a link to a context the user lacks shows "You do not have access in this organisation" without revealing resource existence. Last-used context is remembered per device.

**FR-P01-43 — Profile and preferences.** Profile: display name, legal name (from KYC, read-only once verified; change requires re-verification), photo (optional), contact points (multiple, each verified; one primary per type), addresses (structured; PIN code `^[1-9][0-9]{5}$` with district/state lookup; foreign address schema for NRIs), date format, time zone (default Asia/Kolkata). Preferences (`core.contact_preferences`): UI language; notice language (may differ; any of 12 locales); second language for bilingual documents; channel order (WhatsApp, SMS, email, push, voice) with per-channel opt-in; quiet hours — a user may narrow but cannot widen the platform contact window, and for any recovery-related communication the hard window is 08:00–19:00 local time (NN-12; `core.quiet_hours_policies`); blackout dates with reason category (`bereavement`, `marriage`, `medical_emergency`, `other`) honoured by P07; accessibility — font scale (100–200%), high-contrast theme, reduced motion, screen-reader optimised layout, captions on by default, sign-language interpreter request, "assisted mode" request (a case manager or field agent helps, with consent recorded per action).

**FR-P01-44 — Mobile app shell (Expo).** One app (`apps/mobile`) with role-based navigation (party / neutral / enterprise-lite) per master §4.1: Expo Router groups `(auth)`, `(onboarding)`, `(app)/(party)/(tabs)`, `(app)/(neutral)/(tabs)`, `(app)/(enterprise)/(tabs)`; screens SCR-P01-M01…M08; shared `packages/api-client`, `packages/forms`, `packages/ui-native`, `packages/i18n`; universal links `https://equatorresolution.in/app/*` and `https://equatorresolution.in/r/*` (opens the app if installed, else web) plus `equator://` scheme; push registration only after an in-app primer and OS permission (Expo Push tokens stored per device binding); offline queue scaffold (SQLite) for drafts; screenshot protection (`expo-screen-capture`) on sealed and Tier-High screens; app-switcher blur; forced-update gate (P00 endpoint); low-bandwidth mode (images off, text-only lists) auto-enabled on 2G/slow-3G detection. Bottom tabs are placeholders in P01 (Home, Cases/My work, Messages, Profile) and are filled from P02; P12 governs final mobile navigation (master X-03).

## 5. Workflows and state machines

### 5.1 User account

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| — | register / claim_invite | contact verified (OTP/link) | active_k0 | person + user created; consent records; audit |
| active_k0 | verify_identity | K1 method passed | active_k1 | `assurance_level.changed` event |
| active_k1 | verify_liveness | liveness + face match pass | active_k2 | event |
| active_k2 | complete_video_kyc | agent + reviewer approve | active_k3 | event |
| any active | dob_under_18 | — | pending_guardian | block sign-in to case features; guardian invite |
| pending_guardian | guardian_consent_verified | guardian K1 adult | previous level | consent records (guardian actor) |
| any active | suspend | admin/risk ≥ 90/SCIM | suspended | revoke sessions |
| suspended | reinstate | admin (2-person for admins) | prior | audit |
| any | close_account | no open case/obligation, or legal hold applies → `closed_retained` | closed / closed_retained | retention schedule applies |

### 5.2 KYC/KYB check

`initiated → provider_pending → (passed | failed | review_required) → (passed | failed) [review] → expired [re-check due]`. Provider timeout 30 s → retry ×3 (stateless) with failover per P00; all failures → `review_required` (never silently passed).

### 5.3 Invitation (incl. respondent notice link)

| State | Event | Guard | Next | Side effects |
|---|---|---|---|---|
| created | deliver | channel available | sent | message via `MESSAGING_PORT`/`EMAIL_PORT` (P07 orchestrates notices) |
| sent | open_link | code valid, not expired | opened | audit (no PII) |
| opened | verify_possession | OTP to addressed contact passes | verified | — |
| verified | bind | invitee accepts; respondent: privacy notice shown | accepted | membership / role grant / case participation (P02) |
| opened | not_me | — | declined_not_me | suppress contact for case; task to case manager |
| sent/opened | expire | now > expires_at | expired | inviter notified |
| any non-terminal | revoke | inviter/admin | revoked | — |

### 5.4 Counsel mandate

`requested (by counsel) | offered (by party) → accepted (counterpart) → signed (party, aal2) → active → (revoked | expired | completed)`. Guard on `active`: counsel credential status ≠ `rejected`; for `organisation_standing` scope, signatory authority includes `appoint_counsel`.

### 5.5 Respondent first contact

```mermaid
sequenceDiagram
  participant R as Respondent (phone)
  participant W as Web /r/{code}
  participant ID as identity module
  participant M as MESSAGING_PORT
  participant C as consent module
  R->>W: open link from SMS/WhatsApp
  W->>ID: preview(code)
  ID-->>W: institution, case no., claimant display name, due date (no allegations)
  R->>W: "This is me"
  W->>ID: start possession check
  ID->>M: OTP to the notified contact only
  R->>W: enter OTP
  W->>ID: verify → bind invitation, create/link K0 account
  W->>C: show respondent notice (s.17(1)(a) basis; optional purposes unticked; no marketing)
  C-->>W: consent records written
  W-->>R: notice + documents; "Respond" (requires K1)
```

### 5.6 SSO activation

`draft → metadata_uploaded → test_passed (admin completes test login, attributes mapped) → domain_verified (DNS TXT) → active → enforced (optional)`; deactivation requires a replacement login path for at least 2 admins.

## 6. Screens and UX (web + mobile)

Common rules for every P01 screen: plain language at reading level ≤ class 8 in en/hi; all text from i18n catalogues (en-IN, hi-IN mandatory); language switcher on every unauthenticated screen; states — empty, loading (Skeleton), error (InlineAlert with `code`), success (Toast or confirmation page); keyboard-complete; focus moves to the first error with an ErrorSummary; touch targets ≥ 44 px on mobile; pages ≤ 150 KB first load on auth routes; works without JavaScript for `/r/{code}` preview. Mobile variants use the same IDs with `M` suffix where the layout differs materially.

### 6.1 Sign-in and authentication

| ID | Route | Persona | Purpose | Key fields / components | Notes |
|---|---|---|---|---|---|
| SCR-P01-01 | `auth…/login` | all | Universal sign-in hub | Buttons: "Continue with mobile number", "Continue with email", "Continue with DigiLocker" (flag), "Sign in with password", "Use your organisation login (SSO)"; link "I received a notice"; language switcher; tenant brand header when reached from a tenant domain | Order adapts: professional tenants show SSO/password first |
| SCR-P01-02 | `…/login/mobile` | all | Request OTP | Country code (default +91), mobile number, channel choice (WhatsApp / SMS), consent line for service messages | Inline validation of E.164; rate-limit message with time left |
| SCR-P01-03 | `…/login/otp` | all | Verify OTP | OTPInput (6), countdown 30 s, resend, "Try SMS instead", "Get a voice call" (after 2 failures), change number | `autocomplete="one-time-code"`; SMS Retriever on Android |
| SCR-P01-04 | `…/login/email` | all | Magic link | Email; "Check your email" state with cross-device code entry | Explains link expiry (15 min) |
| SCR-P01-05 | `…/login/password` | professionals | Password sign-in | Email/username, password (show/hide), "Use a passkey" (conditional UI autofill), forgot password | Breached-password notice on change |
| SCR-P01-06 | `…/login/mfa` | professionals | Second factor | Passkey prompt, TOTP code, recovery code, "Trust this browser for 30 days" (not for sealed/admin) | aal shown in plain words ("extra check") |
| SCR-P01-07 | `…/login/sso` | enterprise, staff, university | SSO discovery | Work email → domain lookup → redirect to IdP; error if domain unknown | No tenant enumeration: generic message |
| SCR-P01-08 | `…/login/digilocker` | parties | DigiLocker | Explainer (what will be fetched, Aadhaar stays masked), Continue → provider; return page with result | Flag `release.auth.digilocker_login` |
| SCR-P01-09 | `/r/{code}` | respondent | Notice-link landing | Institution, case number (mono font), claimant display name, notice date, respond-by date, language selector, "This is me", "This is not me", help line | No JS required; ≤ 50 KB; QuickExit not shown (not sensitive) unless vertical FAM/WRK-POSH |
| SCR-P01-10 | `/signup` | party, org, learner, partner, neutral | Sign-up | "I am: an individual / an organisation / a neutral applying to the panel / a learner / a partner"; contact (mobile or email); name | Routes to persona wizard |
| SCR-P01-11 | `/onboarding/privacy` | all | Itemised notice + purposes | Notice accordion per purpose (data items, purpose, retention, basis); required purposes (no toggle, explained); optional purposes (unticked toggles); links: withdraw, rights, Board complaint, DPO contact; "Read in another language"; Continue | Respondent variant shows legal basis text; child variant routes to guardian |
| SCR-P01-43 | `/account/recover` | all | Recovery | Choose path (other contact / recovery code / DigiLocker / assisted); status of 72-hour hold | Never reveals which contacts exist (masked hints only) |

### 6.2 Identity and organisation onboarding

| ID | Route | Persona | Purpose | Key fields / components | Notes |
|---|---|---|---|---|---|
| SCR-P01-12 | `/onboarding/profile` | party | Personal profile | Full name (as per ID), father's/spouse's name (optional; FAM), gender (Female/Male/Transgender/Prefer not to say), DOB, primary language, notice language, mobile (verified), alternate mobile, email, address (line 1–2, city, district, state, PIN; or foreign), NRI/OCI toggle (country of residence), representative (none / counsel / family member) | Data minimised: vertical fields come at intake (P02) |
| SCR-P01-13 | `/onboarding/identity` | party, org user, counsel, neutral | KYC method chooser | Cards: DigiLocker (recommended), PAN, Passport (NRI/foreign), Upload ID for review; shows level needed and why ("To respond formally you need identity verification") | Progress indicator K0→K1→K2 |
| SCR-P01-14 | `/onboarding/identity/pan` | same | PAN verification | PAN, name as on PAN, DOB; result with match status | Masks after entry |
| SCR-P01-15 | `/onboarding/identity/liveness` | K2 roles | Liveness + face match | Camera permission primer, provider SDK, retry (max 3/day), fallback "Book video verification" | Low-light tips; accessible alternative = video KYC |
| SCR-P01-16 | `/onboarding/identity/video-kyc` | high-risk, NRI | Video KYC | Slot picker (IST and local time), documents checklist, join button, status | Recording notice before start |
| SCR-P01-17 | `/onboarding/identity/passport` | NRI, foreign | Passport/OCI | Passport number, country, expiry, MRZ scan (camera) or upload, OCI number + copy, overseas address + proof, foreign mobile | Sanctions screening runs silently; result only to reviewers |
| SCR-P01-18 | `/onboarding/guardian` | minors, PwD | Guardian consent | Child: guardian's mobile/email to invite. Guardian: own K1, relationship (parent/legal guardian/court-appointed), proof upload (optional for parent; mandatory for court-appointed), per-purpose consent | Child sees "Waiting for your guardian" |
| SCR-P01-19 | `/onboarding/organisation` | org user, enterprise/university admin | KYB | Organisation type, legal name, CIN/LLPIN, PAN, GSTIN(s) (multi-state), Udyam, LEI, regulator registration (RBI CoR / IRDAI / SEBI), registered address (auto from MCA), website, industry; each identifier shows verification chip | Prefills from MCA/GST; edits after verification need review |
| SCR-P01-20 | `/organisations/{id}/signatories` | org admin | Signatories & authority | Person (invite or self), designation, evidence type + upload, resolution date, validity, authority matrix (actions × mechanisms × verticals), monetary limit (MoneyInput ₹), dual-signature threshold, case scope | Matrix uses checkbox grid with row/column headers for screen readers |
| SCR-P01-21 | `/organisations/{id}/members` | org admin | Members | Table (name, role, signatory?, status, last active), invite (email/mobile, role), join requests | — |
| SCR-P01-22 | `/organisations/{id}/international` | `INT` org | Foreign KYB + UBO | Jurisdiction, registry, registration no., incorporation date, documents (incorporation, good standing ≤ 6 months, directors register, shareholding chart) with apostille flags, UBO repeater (name, DOB, nationality, residence, %, control type, PEP), senior managing official fallback, FEMA route, tax ID | Screening status hidden from applicant beyond "under review" |
| SCR-P01-23 | `/account/bank` | party, neutral, partner, trainer, IC external | Bank verification | Account holder name, account number (twice), IFSC (bank/branch lookup), account type; result and name-match | Step-up for changes; 24-hour cooling-off banner |

### 6.3 Professional onboarding

| ID | Route | Persona | Purpose | Key fields / components | Notes |
|---|---|---|---|---|---|
| SCR-P01-24 | `/onboarding/counsel` | counsel | Enrolment verification | Representative type (advocate / authorised representative / foreign counsel), State Bar Council, enrolment no., enrolment date, CoP number, uploads (enrolment certificate, Bar ID card, CoP), chambers address, firm (optional); foreign: home bar, admission no., good-standing certificate | Status chip and expected review time (2 working days) |
| SCR-P01-25 | `/mandates/{id}` | party, counsel | Mandate | Parties, counsel (with verification badge), scope checkboxes (with plain-language explanation each), validity, fee arrangement note, preview PDF, sign (party), accept (counsel), revoke | `sign_s12_5_waiver` shown as "Always signed by the party personally" |
| SCR-P01-26 | `/apply/neutral` | neutral applicant | Start application | Account creation, MFA enrolment, KYC (K2), PAN | Explains P03 steps and timeline |
| SCR-P01-27 | `/apply/neutral/{appId}/{step}` | neutral applicant | Application wizard | Steps 1–7 per FR-P01-26 with Stepper, autosave, review page, submit; status tracker after submit | Mobile supported; CV upload from Files |
| SCR-P01-28 | `/invite/{code}` → `/onboarding/staff` | staff | Staff onboarding | Accept invite, SSO/password+passkey, K1, undertakings (each a ConsentCheckbox with document link and version), DPDP training date, conflict declaration repeater | SoD conflict shown to inviter, not invitee |
| SCR-P01-29 | `/onboarding/enterprise` | enterprise_admin | Enterprise onboarding | Checklist: KYB → signatory → agreements (MSA, DPA, Rules — e-accept) → SSO → invite team → org units; progress meter | Commercial-relationship disclosure note |
| SCR-P01-30 | `/settings/sso` | enterprise/university/chambers/institution admin | SSO set-up | Protocol (SAML/OIDC), SP metadata download / ACS & entity ID, IdP metadata upload or discovery URL, attribute mapping, group→role mapping table, test login, domain verification (TXT record + check), enforce SSO toggle, break-glass admins, SCIM token generation | Test result shows received attributes (redacted) |
| SCR-P01-31 | `/onboarding/grievance-officer` | GRO, internal ombudsman | GRO profile | Designation, employee ID, official email/phone, office address, level, principal nodal officer flag, appointment letter, independence declaration (IO), public-display consent | Preview of public contact card |
| SCR-P01-32 | `/sealed/onboarding` | IC roles | IC onboarding (sealed) | Factor enrolment (passkey/TOTP only), confidentiality undertaking (s.16/s.17), conflict declaration; external member: affiliation type, CV, PAN, bank; gender (sealed, explained purpose) | Screenshot-blocked; QuickExit; step-up on entry |
| SCR-P01-33 | `/onboarding/university` | university_admin | Institution onboarding | Institution name, type, AISHE code, UGC/AICTE reference, PAN, address, nodal officer, SSO or email domains, invite SGRC members | — |
| SCR-P01-34 | `/onboarding/student` | student | Student onboarding | Institution (pre-filled from SSO/domain), enrolment number, programme, year, DOB, contact; guardian branch | — |
| SCR-P01-35 | `/academy/register` | learner | Learner registration (F-01) | Fields per FR-P01-32; three separate consent controls (processing required; marketing optional; publication optional) | Under-18 → SCR-P01-18 |
| SCR-P01-36 | `/partners/apply` | partner | Partner application | Fields per FR-P01-33; advocate selection switches to BCI-compliant mode (bank fields hidden, credit explanation) | Status page after submit |
| SCR-P01-37 | `/admin/elevate` | platform_admin | JIT elevation | Requested scope (tenants/modules), duration (≤ 4 h), reason, approver selection; active elevation banner with countdown | aal3 required |

### 6.4 Account, privacy and admin

| ID | Route | Persona | Purpose | Key fields / components | Notes |
|---|---|---|---|---|---|
| SCR-P01-38 | header menu / `/switch` | multi-role users | Role & tenant switcher | Grouped list: tenant logo/name, role chip, last used; search; step-up indicator for sealed/admin roles | Announces context change to screen readers |
| SCR-P01-39 | `/account/profile` | all | Profile | Per FR-P01-43; verified badges; "Request correction" for KYC-locked fields | — |
| SCR-P01-40 | `/account/preferences` | all | Preferences | Languages (UI, notices, second), channel order (drag + keyboard reorder), per-channel opt-in, quiet hours (time range limited to permitted window), blackout dates, accessibility settings, assisted-mode request | Shows the non-editable legal window with explanation (NN-12) |
| SCR-P01-41 | `/account/security` | all | Security | Factors list (add/remove passkey, TOTP, recovery codes), devices (bound devices, attestation status, revoke), sessions (device, city, last active, revoke, sign out everywhere), login history (30 days) | Remove last factor blocked for professional roles |
| SCR-P01-42 | `/account/privacy` | all | Privacy centre | Consents by purpose (status, date, notice version, withdraw/give), notices (current + history), data requests (new: access/correction/erasure/nomination/grievance; status with SLA), guardian links, download my data | Withdraw = one action + confirmation explaining consequences |
| SCR-P01-44 | `/admin/people` | institution/enterprise/chambers/university admin | Users & memberships | Table (person, roles, status, KYC level, last active, MFA), invite, change role (SoD check), suspend, reset factors (2-admin rule for admins), export (audited) | Tenant-scoped via identity module API |
| SCR-P01-45 | `/admin/verification-queue` | support_agent, registrar, kyb reviewer | KYC/KYB/credential reviews | Queue (type, risk score, age, SLA), detail with provider results, documents viewer (watermarked with reviewer id), name-match breakdown, decision (approve/reject/request info) with reason; second-person confirm for sanctions and counsel | Documents never downloadable; all views logged |
| SCR-P01-46 | `/admin/privacy` | dpo | Notices & DSR desk | Notice versions per tenant/locale (status, legal approval), purposes catalogue, DSR queue with SLA clocks, withdrawal propagation status per consumer, guardian verification queue | Notice changes via Ruleset Studio CR |

### 6.5 Mobile shell

| ID | Screen | Purpose | Key components | Notes |
|---|---|---|---|---|
| SCR-P01-M01 | Splash & update gate | Version check, attestation | Logo, progress, forced-update screen | Offline-tolerant |
| SCR-P01-M02 | Welcome & language | First-run language and purpose | 12 language tiles (native script), "I received a notice", Sign in | Large tap targets |
| SCR-P01-M03 | Sign-in | Native wrapper of SCR-P01-01…08 | System browser (ASWebAuthenticationSession / Custom Tabs) | No embedded web views for credentials |
| SCR-P01-M04 | Device binding | Bind device key, explain | Explainer, biometric prompt, success | Skipped for SSO-only users if policy says so |
| SCR-P01-M05 | Lock screen | Biometric/PIN unlock | Biometric prompt, PIN pad, "Sign out" | 5 attempts then re-login |
| SCR-P01-M06 | Notifications primer | Push permission | Plain explanation of what we send; Allow / Not now | Respect OS denial; no re-prompt within 30 days |
| SCR-P01-M07 | Role home (placeholder tabs) | Navigation shell | Party: Home, Cases, Messages, Profile; Neutral: Today, Cases, Calendar, Profile; Enterprise-lite: Alerts, Escalations, Reports, Profile | Filled from P02 onward |
| SCR-P01-M08 | Low-bandwidth notice view | `/r/{code}` deep link in app | Text-first notice card, language toggle, "This is me" | Works on 2G |

## 7. Backend design

### 7.1 Modules touched
`identity`, `consent`, `kyc`, `directory` (persons, organisations, signatories, mandates), `tenancy` (SSO connections), `notifications` (in-app), `comms` (OTP/invite sends via ports; full orchestration P07), `audit`, `admin`, `rules` (config kinds `assurance_policy`, `privacy_notice`, `role_bundle`), `neutrals` (application intake only), `growth` (partner applications, neutrality filter), `academy` (learner registration).

Global identity tables (`core.users`, `core.persons`, `core.contact_points`, `core.mfa_factors`, `core.sessions_auth`, `core.device_bindings`) are not tenant-scoped; they are accessed only by the `identity` module through a dedicated DB role `eq_identity` whose policies allow full access, while `eq_app` sees only the caller's own rows (`id = app.person_id`). Listed in `db/rls-exemptions.yaml` with this justification (ADR-0032).

### 7.2 Tables

| Table | Key columns | Constraints / RLS |
|---|---|---|
| `core.persons` | id, legal_name, display_name, father_or_spouse_name, gender, dob, nationality[], kyc_level (K0–K3), risk_score, origin (`self_signup`,`respondent_notice`,`invite`,`sso_jit`,`bulk`), marketing_eligible, is_minor (generated from dob), pan_enc/bidx/masked, aadhaar_last4, created_at | CHECK aadhaar_last4 ~ '^[0-9]{4}$'; no column may hold 12 digits (trigger); `eq_identity` only |
| `core.users` | id, person_id, keycloak_sub UNIQUE, status (`active_k0`…`closed_retained`), primary_locale, last_login_at | — |
| `core.contact_points` | id, person_id, kind (`mobile`,`email`,`whatsapp`), value_enc, value_bidx, value_masked, verified_at, is_primary, source | UNIQUE (kind, value_bidx) where verified |
| `core.addresses` | id, owner_type, owner_id, line1, line2, city, district, state_code, pin, country, proof_document_id | PIN regex when country = IN |
| `core.organisations` | id, tenant_id (tenant-of-record), org_type, legal_name, cin, llpin, gstins[], pan_enc/bidx/masked, udyam, lei, regulator_regs jsonb, jurisdiction, mca_status, kyb_status, commercial_relationship, created_by | RLS tenant template; UNIQUE (tenant_id, cin), (tenant_id, lei) |
| `core.org_signatories` | id, tenant_id, organisation_id, person_id, designation, evidence_type, evidence_document_id, resolution_date, valid_from, valid_to, authority jsonb, dual_sign_threshold_minor, currency, status, verified_by | RLS; CHECK valid_to > valid_from |
| `core.memberships` | id, tenant_id, user_id, role_code, status, org_unit_id, granted_by, sealed_ref, valid_from, valid_to | RLS; UNIQUE active (tenant_id, user_id, role_code); SoD trigger |
| `core.role_grants` | id, tenant_id, user_id, role_code, scope_type (`case`,`organisation`,`proceeding`), scope_id, source (`mandate`,`appointment`,`assignment`,`audit_grant`), source_id, valid_from, valid_to, revoked_at | RLS; used by Cerbos attribute fetch |
| `core.mfa_factors` | id, user_id, kind (`totp`,`passkey`,`recovery_codes`), label, aaguid, attested, created_at, last_used_at | metadata mirror of Keycloak; no secrets |
| `core.sessions_auth` | id (= Keycloak sid), user_id, device_binding_id, acr, created_at, last_seen_at, ip_hmac, city, revoked_at, revoke_reason | — |
| `core.device_bindings` | id, user_id, platform, public_key_jwk, attestation (`passed`,`failed`,`unavailable`), biometric_bound, push_token_enc, created_at, revoked_at | — |
| `core.invitations` | id, tenant_id, kind, token_sha256 UNIQUE, short_code_sha256 UNIQUE, addressed_contact_bidx, addressed_masked, case_id (nullable; FK in P02), role_code, payload jsonb, status, expires_at, invited_by, bound_user_id | RLS (+ public lookup via SECURITY DEFINER function returning preview fields only) |
| `core.kyc_checks` | id, tenant_id, person_id, check_type (`digilocker`,`pan`,`liveness`,`face_match`,`video_kyc`,`passport`,`oci`,`bank_account`,`sanctions`,`bar_enrolment`,`manual_id`), provider, provider_ref, status, score, result jsonb (minimised), reviewer_id, decided_at, expires_at | RLS; result never contains full Aadhaar |
| `core.kyb_checks` | id, tenant_id, organisation_id, check_type (`cin`,`llpin`,`gstin`,`pan`,`udyam`,`lei`,`foreign_registry`,`sanctions`,`ubo`), provider, status, result jsonb, reviewer_id, decided_at, next_check_at | RLS |
| `core.org_beneficial_owners` | id, tenant_id, organisation_id, person_id, ownership_pct numeric(5,2), control_type, is_pep, is_smo | RLS; CHECK ownership_pct BETWEEN 0 AND 100 |
| `core.professional_credentials` | id, person_id, kind (`bar_enrolment`,`certificate_of_practice`,`foreign_bar`,`icai`,`icsi`,`icmai`,`ibbi`,`irdai_surveyor`,`other`), issuer, number, issued_on, status, verified_by, verified_at, next_verification_at, document_ids[] | identity-owned |
| `core.party_representatives` | id, tenant_id, party_person_id, party_org_id, counsel_person_id, representative_type, case_id (nullable until P02), scope_kind (`case`,`organisation_standing`), scope jsonb, status, signed_document_id, valid_from, valid_to, revoked_at, revoked_by | RLS; CHECK NOT (scope ? 'sign_s12_5_waiver') |
| `core.consent_purposes` | code, tenant_id (NULL platform), basis_default, sealed, required_for jsonb, version | platform rows readable by all |
| `core.notices_privacy` | id, tenant_id, notice_code, version, locale, ruleset_version_id, items jsonb, body_md, content_sha256, status, legal_approved_by, effective_from | RLS + platform rows |
| `core.consent_records` | id, tenant_id, person_id, purpose_code, basis, status, notice_id, notice_sha256, surface_id, copy_sha256, channel, actor_type (`self`,`guardian`,`assisted`), actor_person_id, guardian_link_id, evidence jsonb, consent_manager_ref, given_at, withdrawn_at, expires_at | append-only (status changes = new row); RLS |
| `core.guardian_links` | id, child_person_id, guardian_person_id, relationship, proof_document_id, verified_by, verified_at, status | identity-owned |
| `core.dsr_requests` | id, tenant_id, person_id, kind (`access`,`correction`,`erasure`,`nomination`,`grievance`), status, due_at, decision, reason, fulfilled_at | RLS |
| `core.contact_preferences` | person_id, tenant_id, ui_locale, notice_locale, second_locale, channel_order[], channel_optins jsonb, quiet_start, quiet_end, accessibility jsonb, assisted_mode | — |
| `core.quiet_hours_policies` | id, tenant_id, scope (`recovery_related`,`general`), earliest_local, latest_local, locked | platform row `recovery_related` 08:00–19:00 locked (NN-12) |
| `core.sso_connections` | id, tenant_id, protocol, status, idp_metadata_ref, client_secret_ref, domains[], enforce_sso, role_mappings jsonb, scim_enabled, breakglass_user_ids[] | RLS |

Critical DDL:
```sql
CREATE TABLE core.memberships (
  id          uuid PRIMARY KEY DEFAULT core.uuid_v7(),
  tenant_id   uuid NOT NULL REFERENCES core.tenants(id),
  user_id     uuid NOT NULL REFERENCES core.users(id),
  role_code   text NOT NULL REFERENCES core.role_codes(code),   -- master §1.5 list, seeded
  status      text NOT NULL DEFAULT 'active' CHECK (status IN ('invited','active','suspended','revoked','expired')),
  org_unit_id uuid,
  sealed_ref  text CHECK (sealed_ref IS NULL OR sealed_ref ~ '^sr_[a-z2-7]{26}$'),
  valid_from  timestamptz NOT NULL DEFAULT now(),
  valid_to    timestamptz,
  granted_by  uuid,
  CHECK (role_code NOT IN ('ic_presiding_officer','ic_member','ic_external_member') OR sealed_ref IS NOT NULL)
);
CREATE UNIQUE INDEX memberships_one_active ON core.memberships (tenant_id, user_id, role_code) WHERE status = 'active';
SELECT rls.enable_tenant_rls('core','memberships');

CREATE TABLE core.consent_records (
  id             uuid PRIMARY KEY DEFAULT core.uuid_v7(),
  tenant_id      uuid NOT NULL REFERENCES core.tenants(id),
  person_id      uuid NOT NULL REFERENCES core.persons(id),
  purpose_code   text NOT NULL,
  basis          text NOT NULL CHECK (basis IN ('consent','legitimate_use_s7','legal_claim_s17_1_a','legal_obligation','s16_transfer')),
  status         text NOT NULL CHECK (status IN ('given','withdrawn','expired','superseded')),
  notice_id      uuid NOT NULL REFERENCES core.notices_privacy(id),
  notice_sha256  char(64) NOT NULL,
  surface_id     text NOT NULL,                 -- e.g. 'SCR-P01-11'
  copy_sha256    char(64) NOT NULL,             -- hash of the exact UI text shown
  channel        text NOT NULL CHECK (channel IN ('web','mobile','whatsapp','ivr','assisted','api')),
  actor_type     text NOT NULL CHECK (actor_type IN ('self','guardian','assisted')),
  actor_person_id uuid,
  guardian_link_id uuid,
  evidence       jsonb NOT NULL,                -- {ts, ip_hmac, ua_sha256, otp_challenge_id?}
  consent_manager_ref text,
  given_at       timestamptz,
  withdrawn_at   timestamptz,
  expires_at     timestamptz,
  CHECK (actor_type <> 'guardian' OR guardian_link_id IS NOT NULL),
  CHECK (status <> 'withdrawn' OR withdrawn_at IS NOT NULL)
);
REVOKE UPDATE, DELETE ON core.consent_records FROM eq_app;   -- append-only; current state via view core.v_consent_current
SELECT rls.enable_tenant_rls('core','consent_records');

CREATE TABLE core.party_representatives (
  id                 uuid PRIMARY KEY DEFAULT core.uuid_v7(),
  tenant_id          uuid NOT NULL REFERENCES core.tenants(id),
  party_person_id    uuid,
  party_org_id       uuid REFERENCES core.organisations(id),
  counsel_person_id  uuid NOT NULL REFERENCES core.persons(id),
  representative_type text NOT NULL CHECK (representative_type IN ('advocate','authorised_representative','foreign_counsel')),
  case_id            uuid,                       -- FK added in P02
  scope_kind         text NOT NULL CHECK (scope_kind IN ('case','organisation_standing')),
  scope              jsonb NOT NULL,             -- {"view_documents":true,...}
  status             text NOT NULL CHECK (status IN ('requested','offered','accepted','signed','active','revoked','expired','completed')),
  signed_document_id uuid,
  valid_from         timestamptz, valid_to timestamptz,
  revoked_at         timestamptz, revoked_by uuid,
  CHECK (party_person_id IS NOT NULL OR party_org_id IS NOT NULL),
  CHECK (NOT (scope ? 'sign_s12_5_waiver')),     -- NN-03: never delegable
  CHECK (scope_kind = 'organisation_standing' OR case_id IS NOT NULL OR status IN ('requested','offered'))
);
SELECT rls.enable_tenant_rls('core','party_representatives');
```

### 7.3 APIs

| Method & path | Purpose | Auth / role | Idempotency |
|---|---|---|---|
| POST /internal/v1/otp/challenges | Create OTP challenge (Keycloak SPI) | mTLS (Keycloak) | challenge id |
| POST /internal/v1/otp/challenges/{id}/verify | Verify OTP | mTLS | — |
| POST /internal/v1/magic-links, …/redeem | Magic link issue/redeem | mTLS | — |
| GET /v1/auth/session | Current session, acr, context | session | — |
| POST /v1/auth/step-up | Start step-up (returns authorize URL with acr/max_age) | session | — |
| POST /v1/auth/logout, /v1/auth/logout-all | Sign out | session | — |
| GET /v1/r/{code} | Notice-link preview (minimal) | public, rate-limited | — |
| POST /v1/r/{code}/possession-checks, …/{id}/verify | OTP to addressed contact; bind | public → session | required |
| POST /v1/r/{code}/not-me | Misdirected notice | public | required |
| POST /v1/invitations · GET · POST /{id}/resend · POST /{id}/revoke | Generic invitations | membership:invite | required |
| GET /v1/invitations/{code}/preview · POST /v1/invitations/{code}/accept | Invitee flow | public → session | required |
| GET /v1/me · PATCH /v1/me/profile | Profile | self | `If-Match` |
| GET /v1/me/memberships · POST /v1/me/context | List / switch context | self (step-up for sealed/admin) | — |
| GET/PUT /v1/me/preferences | Preferences (NN-12 validation) | self | `If-Match` |
| GET/POST/DELETE /v1/me/contact-points · POST …/{id}/verify | Contact points | self (aal2 to remove primary) | required |
| GET /v1/me/security · DELETE /v1/me/security/factors/{id} · POST /v1/me/security/recovery-codes | Factors | self aal2 | required |
| GET /v1/me/sessions · DELETE /v1/me/sessions/{id} | Sessions | self | — |
| POST /v1/me/devices · DELETE /v1/me/devices/{id} | Device binding | self | required |
| POST /v1/account-recovery/requests · POST …/{id}/verify | Recovery | public → verified | required |
| POST /v1/kyc/digilocker/sessions · GET /v1/kyc/digilocker/callback | DigiLocker | self | required |
| POST /v1/kyc/pan-verifications · /liveness-sessions · /passport-verifications · /bank-account-verifications · /video-kyc/bookings | KYC checks | self | required |
| GET /v1/kyc/status | Levels, pending checks | self | — |
| POST /v1/organisations · GET/PATCH /v1/organisations/{id} | Organisation | org user / admin | required |
| POST /v1/organisations/{id}/kyb-checks · /beneficial-owners · /join-requests | KYB | org admin | required |
| POST /v1/organisations/{id}/signatories · PATCH …/{sid} · POST …/{sid}/revoke | Signatories | signatory:authorise | required |
| GET /v1/organisations/{id}/authority-check?personId=&action=&amountMinor=&currency=&mechanism= | Authority check (service API) | internal / case modules | — |
| POST /v1/me/professional-credentials · GET | Counsel/neutral credentials | self | required |
| POST /v1/mandates · POST /{id}/accept · /sign · /revoke · GET /v1/mandates | Mandates | party / counsel | required |
| POST /v1/neutral-applications · PATCH /{id} · POST /{id}/submit · GET /{id} | Neutral application | applicant | required |
| POST /v1/partner-applications · GET /{id} | Partner application | applicant | required |
| POST /v1/academy/registrations | Learner registration | self | required |
| POST/GET/PATCH /v1/tenant-admin/sso-connections · POST /{id}/test · /activate · /domains/{domain}/verify | SSO | sso:configure (aal2) | required |
| GET/POST /v1/tenant-admin/members · PATCH /v1/tenant-admin/memberships/{id} · POST …/suspend | Members | membership:* | required |
| /scim/v2/Users, /scim/v2/Groups (RFC 7644) | Provisioning | SCIM bearer (machine) | SCIM semantics |
| POST /v1/tenant-admin/oauth-clients | Machine identity (basic) | tenant admin aal2 | required |
| GET /v1/privacy/notices/{noticeCode}?locale= | Public notice | public | — |
| GET /v1/me/consents · POST /v1/me/consents · POST /v1/me/consents/{id}/withdraw | Consent ledger | self (aal2 for sealed) | required |
| POST /v1/me/guardian-links · POST /v1/guardian-links/{id}/consent | Guardian flow | child / guardian | required |
| POST /v1/me/data-requests · GET | DSR | self aal2 | required |
| GET /v1/admin/verification-queue · POST …/{id}/decision | Reviews | kyc:review / kyb:review / credential:verify | required |
| GET /v1/admin/data-requests · POST …/{id}/fulfil | DPO desk | dsr:fulfil | required |
| POST /v1/admin/elevations · POST …/{id}/approve | JIT elevation | platform_admin aal3 | required |
| GET /v1/meta/assurance-policy | Current requirements per action | public | — |

Errors added: `EQ-AUTH-001` invalid credentials (generic), `EQ-AUTH-002` OTP expired, `EQ-AUTH-003` OTP attempts exceeded, `EQ-AUTH-004` send rate limit, `EQ-AUTH-010` step-up required, `EQ-AUTH-011` SSO enforced for domain, `EQ-AUTH-012` refresh token reuse detected, `EQ-AUTH-020` identity level insufficient (`required_level`), `EQ-AUTH-030` authority insufficient, `EQ-AUTH-031` mandate scope insufficient, `EQ-AUTH-040` guardian consent pending, `EQ-KYC-001` provider unavailable (queued for review), `EQ-KYC-002` name mismatch, `EQ-KYC-003` sanctions review pending, `EQ-CON-001` required purpose missing, `EQ-CON-002` notice version outdated (re-present), `EQ-PREF-001` quiet hours outside permitted window.

### 7.4 Domain events

`equator.identity.user.registered.v1`, `equator.identity.user.suspended.v1`, `equator.identity.user.reinstated.v1`, `equator.identity.mfa_factor.enrolled.v1`, `equator.identity.mfa_factor.removed.v1`, `equator.identity.session.revoked.v1`, `equator.identity.refresh_reuse.detected.v1`, `equator.identity.device.bound.v1`, `equator.identity.device.revoked.v1`, `equator.identity.account.recovered.v1`, `equator.identity.membership.granted.v1`, `equator.identity.membership.revoked.v1`, `equator.identity.context.switched.v1` (audit-only, not webhook-deliverable), `equator.identity.invitation.sent.v1`, `equator.identity.invitation.accepted.v1`, `equator.identity.invitation.expired.v1`, `equator.identity.invitation.not_me.v1`, `equator.identity.sso_connection.activated.v1`, `equator.kyc.check.completed.v1`, `equator.kyc.assurance_level.changed.v1`, `equator.kyc.kyb_check.completed.v1`, `equator.kyc.sanctions.potential_match.v1`, `equator.directory.organisation.verified.v1`, `equator.directory.signatory.authorised.v1`, `equator.directory.signatory.revoked.v1`, `equator.directory.mandate.activated.v1`, `equator.directory.mandate.revoked.v1`, `equator.directory.credential.verified.v1`, `equator.consent.consent.given.v1`, `equator.consent.consent.withdrawn.v1`, `equator.consent.notice.published.v1`, `equator.consent.dsr.requested.v1`, `equator.consent.dsr.fulfilled.v1`, `equator.neutrals.application.submitted.v1`, `equator.growth.partner_application.submitted.v1`, `equator.academy.learner.registered.v1`. Payloads carry ids, enums and levels; never names, contacts or document content.

### 7.5 Temporal workflows / jobs

| Workflow | Trigger | Behaviour |
|---|---|---|
| `KycCheckWorkflow` | Check initiated | Provider call with 30 s timeout, 3 retries (stateless), failover; ambiguous → review task; emits completion |
| `VideoKycWorkflow` | Booking | Reminders T-24 h and T-15 min, agent assignment, recording ingest to evidence bucket, maker–checker decision |
| `KybVerificationWorkflow` | Organisation created/identifier added | Parallel CIN/GSTIN/PAN/Udyam/LEI checks; MCA status rules; signatory cross-check with directors |
| `SanctionsRescreenWorkflow` | Monthly 1st, 03:00 IST, for persons/orgs in open `INT` matters | Re-screen; new potential match → review + block new signing |
| `CredentialReverificationWorkflow` | Daily | Bar/CoP re-verification 30 days before `next_verification_at`; expiry → status `expired`, badge change |
| `InvitationExpiryWorkflow` | Timer per invitation | Expire; notify inviter |
| `ConsentWithdrawalPropagationWorkflow` | Withdrawal event | Fan-out to consumers; await confirmations within SLAs; DPO task on breach |
| `MarketingConsentExpiryJob` | Daily | Expire marketing consents at 12 months; request re-consent only through owned channels for eligible persons |
| `DsrFulfilmentWorkflow` | DSR created | SLA timers (T-7 days alert); export generation; legal-hold check |
| `AccountRecoveryWorkflow` | Recovery request | 72-hour hold, notifications to old contacts, cancel link, apply |
| `DormantAccessJob` | Daily | Suspend enterprise/SSO users inactive 90 days (no SCIM); end expired auditor grants and elevations |

## 8. Integrations (ports and adapters used, with provider defaults and failure behaviour)

| Port | Use | Primary | Fallback | Failure behaviour |
|---|---|---|---|---|
| `MESSAGING_PORT` (SMS/WhatsApp) | OTP, invites | MSG91 (DLT) for SMS; Gupshup (Meta Cloud API) for WhatsApp | Gupshup SMS / Kaleyra; MSG91 WhatsApp | Stateless failover; after both fail, offer email link or voice OTP |
| `TELEPHONY_PORT` | Voice OTP | Exotel | Plivo | Voice OTP disabled if both unavailable |
| `EMAIL_PORT` | Magic links, invites | AWS SES ap-south-1 | — (Resend after residency check) | Queue + retry 3×; user told to try mobile |
| `PUSH_PORT` | Security alerts | Expo Push | Direct FCM/APNs | Best effort; security alerts also by SMS/email |
| `KYC_PORT` | DigiLocker, PAN, bank, GSTIN, MCA, Udyam, face/liveness, passport OCR, bar roll (where official) | Surepass | HyperVerge (liveness), IDfy | Stateless failover for lookups; liveness sessions restart on the fallback; never auto-pass |
| `SANCTIONS_PORT` | `INT` screening | Commercial list API (contract pending) | Manual list upload + fuzzy match (Jaro-Winkler ≥ 0.85) | Unavailable → `review_required`, activation blocked (NN-19) |
| GLEIF API (via `KYC_PORT` adapter) | LEI | GLEIF public API | Manual certificate | Manual review |
| `VIDEO_PORT` | Video KYC sessions | LiveKit Cloud India | Self-hosted LiveKit | Reschedule |

All KYC/KYB provider responses are minimised before persistence (allow-listed fields), stored encrypted where Tier-High, and never sent to analytics or AI.

## 9. Configuration surface (Ruleset Studio; defaults)

| Config kind | Key settings | Defaults |
|---|---|---|
| `assurance_policy` (elevated) | Level per action; risk rules; name-match thresholds; face-match threshold | View notice K0; file/respond K1; join arbitration hearing K1 (+ liveness at join, P04); sign settlement/award K2 + aal2; receive refund/payout K1 + bank; neutral application K2; counsel K1 + credential; signatory K1 + authority; IC external K2; `INT` signatory K2 + sanctions clear, K3 if risk ≥ 70; platform_admin K2 + aal3 |
| `privacy_notice` (legal; DPO approval) | Notice items per purpose per locale | Platform notices `account`, `party`, `respondent`, `neutral_applicant`, `staff`, `enterprise_user`, `ic_member`, `student`, `learner`, `partner` in en-IN and hi-IN |
| `consent_purposes` (legal) | Tenant-specific purposes | Platform catalogue FR-P01-36 |
| `role_bundle` (elevated) | Permissions per role; SoD rules | Master §1.5 roles; SoD per FR-P01-27 |
| Auth settings (elevated, per tenant) | Enabled login methods, OTP channel order, session timeouts within platform maxima, enforce SSO, MFA for parties (optional upgrade) | Table FR-P01-09; WhatsApp OTP OFF until template approved |
| Invitation settings | TTLs per kind; respondent link validity extension | Members 14 days; respondent = response window + 90 days |
| Bar roll adapters | Enabled states, number patterns | Patterns for DL, UP, RJ, MH, KA, TN, TG, WB, GJ, HR; adapters OFF until verified |
| Quiet hours | Tenant general window (inside platform window) | Recovery-related 08:00–19:00 locked |

Guardrails: tenants cannot lower assurance below platform minima for signing, payouts, sealed access or admin; cannot enable SMS OTP as a second factor for sealed roles; cannot remove required notice items; cannot widen the NN-12 window.

## 10. Security, privacy and audit

- OWASP ASVS Level 3 for authentication, session management and sealed access; Level 2 elsewhere. Credential stuffing defences: WAF bot control, per-IP and per-identifier throttles, generic error messages, no user enumeration on login/recovery/invite endpoints (identical responses and timing ±50 ms).
- Audit events for every login, failed login (aggregated per 5 min), step-up, factor change, session revocation, context switch, KYC/KYB decision, document view in review queue, consent give/withdraw, mandate change, signatory change, invitation lifecycle, elevation, SCIM change.
- PII: contacts, PAN, bank account, passport numbers are field-encrypted with blind indexes; display masked; KYC images retained ≤ 30 days; reviewer document viewer watermarks reviewer id and blocks download/print; Aadhaar full number never persisted (NN-14) with a DB trigger test.
- Sealed: IC onboarding and gender data live in `posh_sealed`; core knows only `sealed_ref` (NN-07).
- Consent: notice and copy hashes make each consent reproducible; records ≥ 7 years; withdrawal propagation tracked to completion (NN-15).
- Neutrality: respondent-origin persons excluded from growth (NN-16); partner neutrality disclosure acknowledged.
- Mobile: certificate pinning to Equator API and auth hosts (with backup pins), DPoP, attestation, screenshot protection on sealed/High screens, wipe on logout.
- Threat model update `docs/security/threat-model-P01.md`: SIM swap (mitigated by device binding + risk score + 72-hour hold on contact changes), OTP phishing (WhatsApp copy-code template, no links in OTP), notice-link forwarding (possession OTP to addressed contact), malicious IdP (signed assertions, domain verification), insider misuse of review queue (watermarking, logging, second-person checks).

## 11. AI touchpoints and guardrails

None in this phase. KYC document OCR, MRZ reading and liveness are performed by the KYC provider's deterministic/biometric services under `KYC_PORT`, not by the AI gateway; `kill.ai.gateway` remains ON (AI disabled). The `ai_assisted_processing` consent purpose is registered now so that P02/P11 can honour a principal's choice from the first case (NN-01, NN-02).

## 12. Acceptance criteria (Gherkin)

```gherkin
Feature: Identity, login, onboarding and consent

  Scenario: OTP send limits per number
    Given mobile "+919812345678" has received 5 OTPs in the last 30 minutes
    When a 6th OTP is requested for that number
    Then the response is 429 with code "EQ-AUTH-004" and a retry time
    And no message is sent

  Scenario: OTP message contains no case data and uses a DLT template
    Given a respondent with a pending case "EQ/FIN/JAI/2027/00042"
    When an SMS OTP is sent
    Then the message text matches the registered DLT template id
    And the text contains neither the case number nor any party name or amount

  Scenario: WhatsApp OTP falls back to SMS
    Given WhatsApp is the preferred OTP channel and the WhatsApp provider returns a failure
    When the user taps "Try SMS instead" after 30 seconds
    Then an SMS OTP is sent via MSG91 and the WhatsApp code is invalidated

  Scenario: Magic link opened on a different device shows a code
    Given Priya Sharma requested a magic link on her laptop
    When she opens the link on her phone
    Then the phone shows a 6-digit code and is not signed in
    And entering the code on the laptop signs the laptop in

  Scenario: NN-14_aadhaar_never_stored_in_full
    Given Ramesh Kumar completes DigiLocker verification
    When the persons, kyc_checks and audit tables and application logs are scanned
    Then only "aadhaar_last4" and the provider reference are present
    And no 12-digit Aadhaar-like value exists anywhere

  Scenario: Respondent must prove possession before seeing documents
    Given a notice was sent by SMS to "+919876543210" with link code "Xq3…"
    When anyone opens "/r/Xq3…" without verification
    Then only the institution, case number, claimant display name and dates are shown
    And documents are visible only after an OTP sent to "+919876543210" is verified

  Scenario: "This is not me" suppresses further contact
    Given a respondent link for case C1 addressed to "+919811111111"
    When the recipient selects "This is not me"
    Then no further messages for C1 are sent to that number
    And a case-manager task "Misdirected notice" is created for C1
    And no account is created

  Scenario: NN-16_respondent_excluded_from_marketing
    Given a person created through a respondent notice link
    When the nightly growth sync runs
    Then no record for that person exists in growth.leads or any audience export
    And the respondent privacy screen did not offer marketing consent

  Scenario: Counsel acting without verified enrolment is visibly flagged
    Given Adv. Sanjay Mehta entered enrolment "D/1234/2015" with status "pending_review"
    And party Anita Rao signed his mandate for case C2
    When the neutral views C2 participants
    Then Sanjay Mehta shows "Authorised representative — enrolment not verified"

  Scenario: Mandate revocation removes access within 60 seconds
    Given counsel has an active mandate for case C2 and an open session
    When Anita Rao revokes the mandate at 10:00:00
    Then by 10:01:00 any request by the counsel to C2 resources returns 403 "EQ-AUTH-031"
    And all parties and the neutral are notified

  Scenario: NN-03 waiver authority cannot be delegated to counsel
    When a mandate is created with scope "sign_s12_5_waiver"
    Then the request fails validation and no mandate is stored

  Scenario: Signatory monetary limit enforced
    Given signatory Vikram Singh of "Acme Finance Ltd" has a limit of ₹5,00,000 for "accept_offer"
    When the authority check is called for "accept_offer" with ₹7,50,000
    Then the result is denied with code "EQ-AUTH-030" and missing authority "amount_limit"

  Scenario: Struck-off company is flagged
    Given CIN "U65990DL2015PTC123456" returns MCA status "Strike Off"
    When KYB completes
    Then the organisation kyb_status is "review_required"
    And it cannot be attached to an enterprise subscription

  Scenario: NN-19 sanctions potential match blocks INT activation
    Given foreign company "Gulf Trading FZE" with a UBO whose screening score is 0.91 against a listed name
    When KYB completes
    Then the organisation is "review_required" with code "EQ-KYC-003"
    And activation requires two reviewers' decisions

  Scenario: NN-15 consent withdrawal propagates within SLA
    Given Meena Joshi has given "whatsapp_channel" and "marketing_communications" consent
    When she withdraws both at 14:00
    Then no WhatsApp message is sent to her after 14:05
    And her growth marketing record is deleted by 14:00 next day
    And the privacy centre explains that case notices continue by SMS and email under s.17(1)(a)

  Scenario: NN-15 minor requires verifiable guardian consent
    Given a student registers with a date of birth making her 17 years old
    Then the account status is "pending_guardian"
    And case and academy features return 403 "EQ-AUTH-040" until a K1-verified adult guardian consents

  Scenario: NN-07 IC external member onboarding is sealed
    Given Dr. Kavita Nair is invited as "ic_external_member"
    When she completes onboarding
    Then her gender declaration is stored only in posh_sealed.ic_members
    And core.memberships holds only role_code and a sealed_ref
    And entering the IC workspace 11 minutes after login requires step-up

  Scenario: Enforced SSO refuses password login
    Given "acmefinance.in" is verified and SSO is enforced for tenant "acme-nbfc"
    When "ops@acmefinance.in" attempts password sign-in
    Then sign-in is refused with code "EQ-AUTH-011" and the user is offered SSO

  Scenario: SCIM deactivation revokes sessions
    Given an enterprise operator with 2 active sessions
    When the IdP sends a SCIM PATCH setting active=false
    Then within 60 seconds both sessions are revoked and the membership is "suspended"

  Scenario: Refresh token reuse revokes the family
    Given a refresh token RT1 was rotated to RT2
    When RT1 is presented again
    Then all tokens in the family are revoked with code "EQ-AUTH-012"
    And the user receives a security alert on all verified channels

  Scenario: Platform admin requires a hardware-bound passkey
    Given a platform_admin signed in with password and TOTP only
    When they request JIT elevation
    Then the API returns 401 "EQ-AUTH-010" with required_acr "eq:aal3"

  Scenario: NN-12 quiet hours cannot be widened
    When a party sets quiet hours to allow contact from 07:00 to 21:00
    Then the request fails with "EQ-PREF-001"
    And setting 09:00 to 18:00 succeeds

  Scenario: NN-23 Hindi privacy notice parity
    Given the "respondent" notice v3 is legal_approved in en-IN only
    When activation of v3 is requested
    Then it is refused until the hi-IN version is legal_approved

  Scenario: Biometric change invalidates device key
    Given a party app bound with biometric key K on an Android phone
    When a new fingerprint is enrolled on the phone and the app is unlocked
    Then the key K is unusable, the session ends and device re-binding is required
```

## 13. Deliverables and exit gate (checklist)

- [ ] Keycloak realm, Keycloakify theme (en/hi + 10 locales), custom authenticators (OTP SMS/WhatsApp/voice, magic link, DigiLocker linking, risk), SSO brokering with Organizations; DPoP or device-assertion binding verified.
- [ ] BFF session handling with CSRF; context header validation; step-up flow end-to-end.
- [ ] All screens SCR-P01-01…46 and SCR-P01-M01…M08 implemented with axe pass and screen-reader scripts for sign-in, respondent link, KYC, privacy centre.
- [ ] KYC (DigiLocker, PAN, liveness, video KYC, passport/OCI, bank) and KYB (CIN/LLPIN, GSTIN, PAN, Udyam, LEI, foreign + UBO + sanctions) against provider sandboxes with fakes in CI.
- [ ] Signatory authority service and mandate engine with NN-03 constraint.
- [ ] Persona onboarding flows for every role in §3, seeded demo users for each in `packages/seed` (`scenarios/P01`).
- [ ] Privacy notices (10 notice codes × en/hi) legal-approved; purposes catalogue; consent ledger; withdrawal propagation with consumer confirmations; guardian flow; DSR desk.
- [ ] Respondent notice-link primitive ready for P02 (API + SCR-P01-09 + M08).
- [ ] Expo app builds (iOS/Android) on EAS dev and staging channels with sign-in, binding, lock, push registration, deep links.
- [ ] NN tests green: NN-03 (mandate), NN-07 (IC onboarding), NN-12 (quiet hours), NN-14, NN-15, NN-16, NN-19 (KYB gate), NN-23 (notices).
- [ ] Load test: 200 OTP sends/s sustained for 10 min with p95 verify < 300 ms; login p95 < 800 ms.
- [ ] Pen-test of auth flows by security engineer (internal) with zero high findings; ADR-0031 (mobile key storage module), ADR-0032 (global identity tables and `eq_identity` role), ADR-0033 (Keycloakify theming), ADR-0034 (assurance model K0–K3/aal1–3) merged.
- [ ] `docs/phases/P01-plan.md`, `P01-demo.md` (click-paths per persona), `P01-open-items.md`.

## 14. Open items and legal verification flags

1. DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025; corr. G.S.R. 892(E)) confirmed: r.3 notice itemisation, r.10 children, r.11 guardian of PwD, r.14(3) ≤ 90 days. Respondent processing basis = DPDP s.17(1)(a) (enforcing legal right/claim), not s.7 (resolved).
2. BCI Certificate and Place of Practice (Verification) Rules, 2015 — name confirmed. [Verified 22 Oct 2026: 5-year CoP validity/verification — BCI CoP Rules 2015 r.9.1] **[VERIFY — open (State Bar Council): official online roll and the Council's written permission for automated lookup before enabling any `lookupBarRoll` adapter; meanwhile staff-assisted check on the official portal]**
3. RESOLVED (Oct 2026): BCI Foreign Lawyers Rules 2022 (notified Mar 2023), amended 13 May 2025. ICA participation is limited to foreign/international-law issues for clients with a principal office abroad; fly-in/fly-out ≤ 60 days in 12 months. Re-check for further amendments quarterly.
4. PML (Maintenance of Records) Rules 2005 r.9(3) beneficial-ownership threshold (10%); Equator is not a PMLA reporting entity, so this is adopted as policy, not obligation — confirm with counsel. [Checked 22 Oct 2026: r.9(3)(a) 'more than ten per cent' — FIU-IND consolidated Rules] **[VERIFY — open: G.S.R. number/date of the 2023 amending notification; do not cite until confirmed]**
5. Resolved: the IO Directions 2023 (29 Dec 2023) were repealed by six RE-specific IO Directions, 2026 (14 Jan 2026; NBFC: RBI/CEPD/2025-26/384, cl.7(2), 14(2), 14(4) from 30 Jun 2026). KYC: RBI (NBFC – KYC) Directions 2025, RBI/DOR/2025-26/361, 28 Nov 2025; V-CIP at paras 26–27 (Commercial Banks – KYC Directions 2025 for banks/PSOs).
6. POSH Rules 2013 r.3 (external-member allowance ₹200/day + travel, employer pays) and r.4 (persons familiar with sexual-harassment issues: social worker ≥ 5 years or person familiar with labour/service/civil/criminal law). No amendment to the 2013 Rules found to Oct 2026 (resolved).
7. Keycloak DPoP: supported from 26.4 (pin ≥ 26.4) [resolved]. TRAI URL whitelisting in force since 1 Oct 2024 — whitelist the `equatorresolution.in` short domain on DLT before launch [action, not a legal unknown]. Meta authentication templates: fixed preset text, optional security line and 1–90 min expiry, one-tap/copy-code/zero-tap buttons; verify `primary_business_location` = India so domestic (not authentication-international) rates apply [Checked 22 Oct 2026: Meta developer docs] **[VERIFY — open (vendor): BSP onboarding at WABA set-up]**
8. **Data-fiduciary mapping:** for Chambers, enterprise, GRM and university tenants, confirm with the DPO whether the tenant or Equator is the Data Fiduciary for each purpose; notices and consent records are tenant-scoped on the assumption that the tenant is fiduciary for its own processes and Equator is processor.
9. **Gender enum:** master does not fix the gender values; P01 uses Female / Male / Transgender / Prefer not to say (aligned to the Transgender Persons (Protection of Rights) Act 2019 terminology). Confirm for Appendix F.
10. **Eighth Schedule languages:** 12 locales are live; the remaining Eighth Schedule languages are served "on request" by human translation — confirm SLA (proposed 15 working days) with the DPO.

---

## v2 Addendum (21 October 2026)

> The requirements below are part of this phase's scope and exit gate (master §17). They come from the v2 appendices named in each heading; where they conflict with earlier sections of this phase, the addendum prevails (precedence: master §15, 02 decision log). Bare § references inside each block point to the appendix named in its heading.

### From Appendix Q — Privacy, Security & Certification Readiness

**FR-P01-V2-Q1 — Notices by jurisdiction.** `core.notices_privacy.jurisdiction` and the six variants of §2.3a; capture surfaces select by resolver output. *Acceptance:* Q-02 passes.

**FR-P01-V2-Q2 — Rights centre v2.** New DSR kinds (restriction, portability, objection, adm_review, opt_out_sale_share, limit_spi, know), requester kinds (guardian, nominee, authorised agent), export `POST /v1/me/exports`. *Acceptance:* Q-03 and Q-04 pass.

### From Appendix S — Identity, Logins, Onboarding, Representatives, Dashboards & RBAC

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

### From Appendix U — Institutional Rules, Codes & Policy Baselines (v2.1, 22 October 2026)

**FR-P01-V2-U02 — Acceptance records.** Sign-up records the ETS and EPN versions accepted. Case filing records ERR and any case-specific terms. Re-acceptance is prompted only for material changes.
