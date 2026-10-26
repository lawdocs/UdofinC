# Phase P01 — Identity, Onboarding, KYC/KYB and Consent

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (core schema, tenancy, ledger, settings heads, flags, ingest, provider routing). External: Keycloak; a DLT-registered SMS route (JioCX or another CPaaS) and optional WhatsApp authentication templates; Google and Microsoft OIDC apps; DigiLocker Requester onboarding with NeGD; UIDAI Aadhaar secure-QR verification (Phase 1, no registration) and OVSE registration under Reg 13A (Phase 2); one licensed KYB vendor (MCA data), one GSP (GSTIN search), GLEIF (LEI); Operations Hub OH3 (consented leads), OH4 (provisioning), OH9 (professional directory).
> **Sequencing:** Starts in P00 sprint 4. Sprints 1–3: identity architecture, login methods, sessions, consent ledger, individual fast path. Sprints 4–6: verification ladder, DigiLocker, Aadhaar offline (QR), KYB, signatory authority, company wizard. Sprints 7–8: professionals, guests, guardians, nominees, partner onboarding API, accessibility pass. P02 starts in parallel from sprint 2 (it needs persons, users and memberships, which freeze at the end of sprint 2). Wave-2 migration activation (P00 users) runs at the P01 exit.
> **Binding appendices:** A (workflows and state machines), B (data model, events and error codes), D (roles, grant types, assurance requirements), K (export folders for profile, KYC and consent records), P (security and privacy controls; DPDP programme), R (settings), W (verification log and open items), Y (ecosystem change request: LawDocs as onboarding target and `TenantProvisioned` consumer).
> **Requirements covered:** R-002, R-003, R-005, R-009, R-017 (identity for web and mobile), R-023 (consented sharing foundations), R-025 (accessible authentication), R-028, R-030, R-031, R-061 (individual identity), R-064 (maker accounts), R-072 (notices and policies in-product).
> **Decisions applied:** D-01, D-02, D-06, D-08, D-10, D-12 (KYC via provider-neutral adapters) · **Challenges applied:** CH-01, CH-02, CH-03, CH-04, CH-05, CH-06, CH-08, CH-09, CH-15, CH-16, CH-17, CH-18, CH-30 · **Non-negotiables tested:** NN-03, NN-04, NN-05, NN-06, NN-11, NN-13, NN-19, NN-20, NN-21, NN-23, NN-24, NN-26, NN-28, NN-32, NN-34, NN-38, NN-42, NN-44, NN-50
> **Estimated effort:** 8 two-week sprints, squad of 8 (tech lead, 2 backend engineers, 2 frontend engineers (web + responsive/mobile flows), 1 identity and security engineer, 1 integrations engineer for KYC/KYB vendors, 1 QA and accessibility engineer).

---

## 1. Objective and business outcome

The owner asked for "Aadhaar login", automatic fetching of details from Aadhaar, PAN, CKYC, MCA and CIBIL APIs, and very fast onboarding for individuals and companies. Research shows that LawDocs is not, and does not plan to become, an Aadhaar requesting entity (Aadhaar Act s.4(4); s.57 omitted by the 2019 Amendment Act; the good-governance route under LG-027 is a long path, never a dependency; R3 LG-021–025), cannot search or download CKYC (PML Rules r.9; R3 LG-046), is unlikely to qualify for direct PAN verification (R3 LG-047), cannot pull credit-bureau data (CICRA ss.17(4), 22; R3 LG-057–058) and has no open MCA API (R3 LG-050). P01 delivers the lawful version of the same experience, and makes it faster than the owner's design:

- **Sign-in in one step** with mobile OTP, email OTP, passkey, password + MFA, Google or Microsoft sign-in, or enterprise SSO. No Aadhaar login (NN-03, CH-01).
- **Verification only when needed**, on a four-level ladder (L0 → L3), using DigiLocker issued documents, Aadhaar secure-QR / e-Aadhaar verification and later Aadhaar Verifiable Credentials as a registered OVSE, licensed KYB vendors, GSPs, GLEIF and Entity Locker — never storing an Aadhaar number (NN-04).
- **Companies discovered from one identifier** (CIN, LLPIN, GSTIN, PAN of the entity, LEI or Udyam) with provenance per field, then the authorised signatory verified with authority evidence.
- **Professionals onboarded with real credential checks**, advocates showing only BCI Rule 36 fields (NN-21).
- **Counterparties sign without an account**, guardians manage wards, nominees get time-locked access after verified events.
- **Consent per DPDP purpose** with versioned notices, one-tap withdrawal and a privacy centre.
- **Partners and sister products** start onboarding on the customer's behalf — group products through the Operations Hub (`TenantProvisioned`), third-party partners through the P19 partner API — but every workspace starts as an invitation; nothing activates until the customer confirms, and the requester gets no access.

| Outcome | Measure (exit gate; p75 in moderated usability tests with 10 participants per journey, then production analytics) |
|---|---|
| Individual: first draft fast | Landing on a document page → first draft preview ≤ **2 minutes** for documents with ≤ 10 required questions; account creation adds ≤ 3 taps + one OTP |
| Company: set-up fast | Sign-up → company workspace with discovered profile, departments and approval model → first agreement started ≤ **10 minutes** |
| No Aadhaar login exists | `NN-03_no_aadhaar_login`: no route, IdP, Keycloak authenticator or UI string offers Aadhaar as a login method |
| No Aadhaar number stored | `NN-04_*` suite: zero Aadhaar-number columns; QR payloads discarded after verification; logs clean |
| Discovery quality | Companies with a CIN: ≥ 85% of profile fields pre-filled with provenance; discovery p50 ≤ 20 s, p95 ≤ 40 s |
| Consent integrity | 100% of optional processing has a consent artefact referencing a notice version; withdrawal propagates internally ≤ 1 hour and to the Operations Hub ≤ 1 hour (Ecosystem Spec §6.14 [REC]) |
| Accessible authentication | WCAG 2.2 AA incl. SC 3.3.8; no image CAPTCHA; every verification path has a non-visual, non-liveness alternative (R3 LG-136 [VERIFY]) |

---

## 2. Scope (in / out)

**In scope:** Keycloak realms, clients and themes; BFF session handling; all login methods; MFA, passkeys, recovery; sessions and devices; step-up; the identity verification ladder and its providers; KYB for companies, LLPs, partnership firms, proprietorships, trusts, societies and HUFs; authorised-signatory verification and authority evidence; professional onboarding and credential verification; counterparty guest identity; minors, wards and guardians; nominees and legacy access; consent artefacts, notice versions, withdrawal and the privacy centre; the activation flow for partner invitations (API surface in P19 §4K) and Operations Hub provisioning consumption; the individual fast path and the company set-up wizard; Consumer Help brand identity separation; migration activation of P00 users.

**Out of scope**

| Item | Owner phase |
|---|---|
| Organisation structure, user types, roles builder, maker-checker engine, delivery grants | P02 |
| Settings Studio UI | P03 |
| eSign signer authentication (performed by the ESP), signing ceremony, signer consent screen | P08 (P01 supplies the signer's account/guest identity and verification level) |
| Drafting questionnaire engine and Vidhi drafting | P06 / P09 (P01 supplies the anonymous-draft session and save-to-account step) |
| Marketplace professional registry, listing switches, payouts | P16 (P01 captures and verifies credentials) |
| Billing, plan purchase | P17 / OH8 |
| Credential vault for portal passwords | P18 (`cvl`, NN-16) |
| DigiLocker document pull into the vault beyond identity verification | P04 |

---

## 3. Personas and permissions touched (Appendix D)

| Role code | What they can do in P01 |
|---|---|
| Visitor (no account) | Start an anonymous draft (template automation, CH-30); read notices; start sign-up |
| `IND_OWNER` | Create account; verify contacts; climb the ladder; manage consents, sessions, devices, passkeys; add wards (as guardian), nominees and delegates; request data rights |
| `IND_GUARDIAN` | Hold a ward profile with guardianship evidence; act for the ward inside the guardian's Personal workspace |
| `IND_NOMINEE` | Accept nomination; request release after a qualifying event; access released folders read-only |
| `IND_DELEGATE`, `IND_FAMILY_MEMBER` | Accept invitation; act within the scope granted (P02 defines scopes) |
| `ORG_OWNER` | Create the company workspace; run discovery; confirm profile; upload authority evidence; invite users; configure SSO/SCIM; sign the subscription and DPA as authorised signatory (or route to the signatory) |
| `ORG_ADMIN` | Invite users, configure SSO/SCIM and domain verification (cannot verify themselves as signatory) |
| `ORG_APPROVER` (authorised signatory) | Verify identity to L2; attach authority evidence; sign on behalf of the entity |
| `ORG_DIRECTOR`, `ORG_KMP` | Linked to MCA director/KMP data (name, DIN, designation) with the owner's confirmation |
| `CP_GUEST` | Open an invitation by magic link + OTP; view shared items; sign via ESP; upgrade to an account |
| `PRO_ADVOCATE`, `PRO_CA`, `PRO_CS`, `PRO_TAX_PRACTITIONER`, `PRO_OTHER`, `PRO_FIRM_ADMIN` | Apply; submit credentials and evidence; reach L2; get verified; manage Rule-36 profile fields |
| `OPS_ONBOARDING` | Assisted onboarding under a client-approved onboarding grant (P02); KYB review queue maker |
| `OPS_SUPPORT_AGENT` | Assisted account recovery steps (never sees OTPs or factors) |
| `PLT_DPO` | Notice versions, consent purposes, rights-request queue, Aadhaar-data revocation acknowledgements |
| `PLT_GRIEVANCE_OFFICER` | Grievance queue on identity, consent and privacy complaints |
| `PLT_SECURITY_OFFICER` | Identity-provider configuration approvals, staff realm policies, step-up policy floors |
| `PLT_SUPER_ADMIN` | Provider configuration (maker); tenant-level identity overrides only by Correction Entry |
| Operations Hub provisioning service; third-party partner clients (P19) | OH: `TenantProvisioned` for group-product and direct requests; partners: onboarding batches and invitations through P19 with an authority attestation; both read status only and get no access to the created tenant |

---

## 4. Functional requirements

### 4A. Identity architecture

**FR-P01-01 — Realms and clients (ADR-0003).** Two Keycloak realms:

- `ld` — every customer-side identity: individuals, company users, directors, auditors, external counsel, counterparties (guest accounts), professionals and partner-created users. Clients: `ld-web` (my.lawdocs.in), `ld-public` (www, for "save draft" and marketplace checkout), `ld-mobile` (Expo; PKCE, no client secret), `ld-delivery-pro` (professionals' practitioner workspace on work.lawdocs.in), `ld-api` (machine clients per tenant and per partner are created in P19). Keycloak Organizations map verified email domains to company IdPs.
- `ld-staff` — LawDocs and Infrabyx staff, federated to the group identity provider (Microsoft Entra ID while the group uses Microsoft 365 — CH-29 note: confirm the actual M365 plan [OWNER]), provisioned by SCIM from Operations Hub OH10, leavers disabled within 4 hours and privileged leavers within 1 hour (Ecosystem Spec §4.2, §4.6). Clients: `ld-console`, `ld-delivery`, `ld-staff-api`. No customer can authenticate in this realm; staff never use `ld` accounts for work.

The application database is authoritative for persons, users, memberships, roles, grants, verification and consents; tokens carry authentication context only (`sub`, `acr`, `amr`, `auth_time`, `sid`, `brand`). Web apps use a Next.js backend-for-frontend: Authorization Code + PKCE server-side; tokens never reach browser JavaScript; the browser holds an encrypted `__Host-ld_sess` cookie (HttpOnly, Secure, SameSite=Lax) and a CSRF token. Mobile uses the BFF `/m/v1` with refresh tokens in the secure enclave/keystore (NN-44). Login pages are a Keycloakify theme at `auth.lawdocs.in` (brand-themed for `[Consumer Help Brand]`).

**FR-P01-02 — Person, user, membership.** `iam.persons` (`prs_`): one real human, whether or not they have an account (a counterparty named in a contract is a person first); name, preferred name, contact points (each with `verified_at`, `verified_method`), preferred language, accessibility preferences (screen-reader mode, captions, reduced motion, high contrast, text size, extended time-outs), `is_minor` (for ward profiles only), `deceased_at` (set only by a nominee-release workflow). `iam.users` (`usr_`): an account (a Keycloak subject) linked to one person; one person may hold a customer account (`ld`) and a staff identity (`ld-staff`) — never merged, but linked by `person_link` for person-level segregation of duties (P02 SoD). `iam.memberships` (`mbr_`): person ↔ tenant with `kind` (`OWNER`, `MEMBER`, `GUEST`, `DELEGATE`, `GUARDIAN`, `NOMINEE`, `PROFESSIONAL`, `EXTERNAL_COUNSEL`, `AUDITOR`), status (`INVITED`, `ACTIVE`, `SUSPENDED`, `ENDED`), `valid_period`. Every new individual account gets a PERSONAL tenant (P00 FR-P00-25) with an `IND_OWNER` membership.

**FR-P01-03 — Request context.** Every API call carries a signed context `ld_ctx = {tenant_id, membership_id, legal_entity_scope[], act_as_role, grant_id?, on_behalf_of?, brand}` set by the BFF (HMAC over value, request ID and a 60-second timestamp). The API validates it against active memberships and grants (Redis cache ≤ 60 s, busted on change), sets the P00 session context and asks Cerbos (P02). Invalid context: `400 LD-IAM-001`; not a member: `403 LD-IAM-003`. The context switcher (P02 SCR-P02-01) changes `ld_ctx`; the header always shows the active workspace and capacity.

**FR-P01-04 — Authentication assurance levels (separate from identity levels, NN-03).**

| ACR | Achieved by | Required for (platform floors; tenants may tighten, never loosen) |
|---|---|---|
| `ld:aal1` | One factor: mobile OTP, email OTP or magic link, passkey without user verification, social sign-in without IdP MFA | Drafting, viewing own vault, reading shared items, guest viewing |
| `ld:aal2` | Two factors, or a user-verifying passkey, or SSO/social sign-in where the IdP asserts MFA (`amr` contains `mfa`/`hwk`/`otp`+`pwd`) | Sending documents outside the workspace, initiating signing requests, downloads of originals in bulk, consent and nominee changes, company admin and every role in NN-18 maker-checker actions, exports, settings changes, payment-method changes |
| `ld:aal3` | Phishing-resistant passkey with user verification, `auth_time` ≤ 5 minutes | Staff privileged actions (`PLT_*` approvals, Correction Entry approval, break-glass), nominee-release approval by staff, credential-vault reveal (P18) |

Step-up: the API returns `401 LD-AUTH-010` with `required_acr` and `max_age`; the client re-runs OIDC with `acr_values` and `max_age`. Defaults: checker approval AAL2 ≤ 30 min; tenant export AAL2 ≤ 10 min; nominee and guardian changes AAL2 ≤ 10 min; staff approvals AAL3.

### 4B. Login methods (NN-03; CH-01)

**FR-P01-05 — Mobile OTP.** 6 digits, CSPRNG, stored only as HMAC-SHA-256 with a pepper in Redis, TTL 300 s, 3 attempts per code, resend after 30 s, max 5 sends per number per 30 minutes and 10 per 24 hours, per-IP and per-device caps, 30-minute cool-off after repeated failures. SMS only through a DLT-registered principal entity, header and content template under the TRAI TCCCPR 2018 as amended (R3 LG-149; NN-34) [VERIFY: which entity holds the DLT registration — the operating entity per D-08]. WhatsApp authentication templates are an optional second channel the user chooses (`iam.otp.whatsapp.enabled` = OFF until the template is approved and the BSP contract signed). Voice OTP for users who cannot read SMS (accessibility) through the same DLT route, flag OFF until the route is verified. OTPs are never logged, never shown to support staff, never sent through email and SMS together. Android SMS Retriever / iOS one-time-code autofill supported.

**FR-P01-06 — Email OTP and magic link.** Email OTP (same rules as FR-P01-05) is the default for email; magic link (256-bit token, SHA-256 at rest, TTL 15 minutes, single use, bound to the initiating browser; cross-device opening shows a code to type instead) is offered for users who prefer it. Disposable email domains are blocked for COMPANY and PRO_FIRM owners.

**FR-P01-07 — Passkeys.** WebAuthn Level 2/3, platform and roaming authenticators, discoverable credentials preferred, `userVerification = preferred` for AAL1 and `required` for AAL2/AAL3, up to 10 per user. Offered after the first OTP sign-in ("Sign in next time with your fingerprint or face") and promoted as the default second factor. Staff realm: allow-listed AAGUIDs.

**FR-P01-08 — Password + MFA.** Optional for customers (OTP and passkeys are the defaults). Passwords 12–128 characters, no composition rules, checked against a breached-password list and contextual words (name, "lawdocs"), Argon2id. A password alone is AAL1; MFA (TOTP RFC 6238, passkey, or OTP) lifts to AAL2. SMS OTP is not accepted as the second factor for `ORG_OWNER`, `ORG_ADMIN`, `ORG_CLO`, `ORG_APPROVER`, professionals and all staff (SIM-swap risk) [REC]. Ten single-use recovery codes, shown once. Passwords are sensitive personal data under the SPDI Rules 2011 until 13 May 2027 (R3 LG-075) — stored only as hashes in Keycloak.

**FR-P01-09 — Google and Microsoft sign-in.** OIDC with `email_verified = true` required; account linking to an existing person only after OTP to the matching verified contact point (prevents account takeover through a newly created social account with the same email). Social sign-in gives AAL1 unless the IdP asserts MFA. Scopes: `openid email profile` only; no Drive, Gmail or Graph scopes at sign-in (workplace connectors in P19 ask for scopes separately).

**FR-P01-10 — Enterprise SSO.** Per COMPANY or PRO_FIRM tenant: SAML 2.0 (signed assertions, SHA-256, IdP-initiated off by default) or OIDC (discovery, PKCE). Domain verification by DNS TXT `lawdocs-verification=<token>`. "Enforce SSO" disables OTP/password for that domain except two named break-glass owners. JIT provisioning creates person and membership with the tenant's group→role mapping (P02); unmapped users get no membership. Directors, external counsel and auditors outside the domain keep local authentication with MFA.

**FR-P01-11 — SCIM 2.0.** `/scim/v2/Users` and `/scim/v2/Groups` (RFC 7643/7644) per tenant with a rotatable, hashed bearer token, for Entra ID and Google Workspace. `active=false` revokes memberships and sessions within 60 seconds. SCIM never grants `ORG_OWNER`, `ORG_ADMIN`, `ORG_APPROVER` or `ORG_CHECKER` roles marked "approval required" (those need an in-app grant with maker-checker, P02). SCIM endpoints are implemented in `iam` unless ADR-0003 records a production-grade Keycloak SCIM extension [VERIFY].

**FR-P01-12 — What is not a login method.** Aadhaar (any mode: OTP, biometric, face, QR, AVC, e-KYC) is never a login or account-recovery method (Aadhaar Act s.4(4), s.8A(4); R3 LG-022, LG-025, LG-034; NN-03). DigiLocker is a **verification source** used after sign-in (FR-P01-21), not a login method, because the NN-03 list is exhaustive and DigiLocker sign-in would make an Aadhaar-OTP-backed credential a de facto login [INTERP; OWNER may revisit only through an ADR and counsel opinion]. Account recovery never uses a government ID. `NN-03_no_aadhaar_login` checks Keycloak flows, routes and every i18n string for login-by-Aadhaar wording.

### 4C. Sessions, devices, recovery

**FR-P01-13 — Sessions.**

| Class | Idle | Absolute | Concurrent |
|---|---|---|---|
| Individuals, family members, delegates | 30 min web (90 days mobile with biometric unlock, device-local) | 30 days web refresh | Unlimited, listed |
| Company users (maker, checker, approver, CLO, admin, owner) | 15 min | 12 h | 5 |
| Directors, KMP, external counsel, auditors | 15 min | 8 h | 3 |
| Guests (`CP_GUEST`) | 15 min | Per invitation, ≤ 72 h per session | 2 |
| Professionals | 15 min | 12 h | 5 |
| Staff (`ld-staff`) | 15 min | 10 h | 3 |

Access tokens 10 minutes, audience-scoped; rotating refresh tokens with reuse detection (replay revokes the family and alerts the user). Revocation on factor removal, role/membership/grant revocation, tenant suspension, SCIM deactivation, staff offboarding, "sign out everywhere". Sessions listed with device, approximate city (from IP; IP stored as HMAC) and last active.

**FR-P01-14 — Devices (mobile).** `iam.devices` (`dev_`): platform, model class, app version, attestation result (Play Integrity / App Attest), push token reference, biometric unlock enabled (flag only; biometrics never leave the device — NN-44), last seen. Root/jailbreak or tamper detection blocks vault offline cache and signing on that device (P22).

**FR-P01-15 — Account recovery.** Individuals: recover through any second verified contact point or a recovery code; if only one contact point exists and it is lost, a 72-hour hold with notice to every known contact and a video-assisted check by `OPS_SUPPORT_AGENT` (identity re-verification at L3 with the user's consent; the call is not recorded by default). Company users: tenant-admin reset (two admins to reset an admin); SSO users through their IdP. Contact-point change requires OTP to old and new contact, or the recovery path; changing the email of an `ORG_OWNER` triggers a 72-hour hold with notice to all admins. Recovery never resets verification levels silently: an L2 attribute linked to a contact point stays but is flagged `REVERIFY_ON_NEXT_USE` [REC].

**FR-P01-16 — Bot and abuse controls without inaccessible CAPTCHAs.** Rate limits per IP, device, number and email; proof-of-work or invisible risk scoring; SMS-pumping defences (country allow-list +91 by default for OTP, number-range anomaly detection, per-tenant OTP budget); no image or audio puzzle CAPTCHA (WCAG 2.2 SC 3.3.8; R3 LG-136 [VERIFY]). Abuse blocks show `LD-AUTH-020` with a route to help.

### 4D. Identity verification ladder (authentication ≠ identity ≠ signing; NN-03)

**FR-P01-17 — Levels.** `kyc.identity_levels` per person:

| Level | Meaning | How reached | Typical unlock |
|---|---|---|---|
| **L0 Unverified** | Account exists; nothing verified | Sign-up started (or a guest before OTP) | Anonymous/own drafts; template automation; reading |
| **L1 Contact verified** | At least one contact point verified by OTP; name self-declared; 18+ self-declared | Mobile or email OTP | Save drafts, Legal Vault, sharing inside LawDocs, negotiation, sending signing requests (the ESP authenticates each signer anyway, P08), buying documents and marketplace services |
| **L2 Document verified** | Name (and where needed photo, 18+ flag) verified against an issuer-signed source; name match recorded | One of: DigiLocker issued document (PAN, driving licence, others) with name match; Aadhaar secure-QR / e-Aadhaar offline verification (Phase 1); Aadhaar Verifiable Credential via the Aadhaar App (Phase 2, after OVSE registration); DSC certificate subject match | Company owner/authorised signatory; guardian; nominee designation and release requests; professional application; "Verified" badge on own profile; higher sharing limits; Consumer Help case filing on the user's behalf where a forum requires identity |
| **L3 Assisted** | L2 plus a human-assisted check | Video-assisted verification by trained staff (document shown live, liveness by conversation, not by algorithm; or in-person at an assisted counter) — offered also as the accessible alternative for anyone who cannot use the digital paths | Account recovery without contact points; nominee release; high-risk changes on request; accessibility route for L2 |

Levels attach to the **person**, carry the method, source, date and expiry (`kyc.level_validity_months` default 24; PAN-based L2 does not expire, address-based attributes do), and are visible to the user with what each level unlocks. A tenant may require a higher level for its own roles (e.g., every `ORG_APPROVER` must be L2) — never lower than platform floors.

**FR-P01-18 — Verification is purpose-bound.** Each verification run (`kyc_` + ULID) records purpose (e.g., `SIGNATORY_VERIFICATION`, `GUARDIAN_PROOF`, `PROFESSIONAL_APPLICATION`, `PROFILE_BADGE`), the notice version shown, the consent artefact (`cns_`), the provider, the attributes requested and received, and the result. The user sees in plain words which attributes will be read and why, and an alternative route (Aadhaar Act s.8A(3); s.8 proviso; R3 LG-024–025).

**FR-P01-19 — Name matching.** Deterministic name-match service (normalisation of honorifics, initials, transliteration variants, token order; score 0–100) with thresholds per purpose (`kyc.name_match.threshold`, default 85 for signatory, 80 for profile badge); below threshold the user may attach a name-change document (gazette notification, marriage certificate) for manual review by `OPS_ONBOARDING` maker and checker.

### 4E. Aadhaar offline verification, DigiLocker and PAN (NN-04, NN-42; CH-02, CH-03, CH-04)

**FR-P01-20 — Aadhaar offline verification (OVSE).** LawDocs verifies Aadhaar **offline** only, never by authentication (Aadhaar Act s.8A; R3 LG-025, LG-029, LG-030):

- **Phase 1 (no UIDAI registration required per the OVSE Playbook, Jan 2026 — R3 LG-030):** verify the UIDAI digital signature on the **secure QR** (scanned from the user's printed Aadhaar or e-Aadhaar PDF) or on an e-Aadhaar PDF; read only the attributes needed for the purpose (name, year of birth or 18+ derivation, gender only if a purpose needs it, photo only for a signing-identity match when a tenant requires it); record last four digits only where a law requires display; discard the QR payload and the uploaded image immediately after verification (never written to the originals bucket). Flag `kyc.ovse.qr.enabled` = OFF until the verification-log row confirms the current QR format and signature verification method [VERIFY: UIDAI secure-QR specification version].
- **Phase 2 (after OVSE registration under Reg 13A of the 2025 amendment regulations — R3 LG-029 [VERIFY gazette date and fees]):** Aadhaar Verifiable Credential via the Aadhaar App (cross-device QR, app-to-app or web-to-app intent), selective disclosure of name, 18+ flag and, where justified, photo; offline face verification happens **inside the Aadhaar App**, never in LawDocs (R3 LG-029, LG-033; CH-17). Flag `kyc.ovse.avc.enabled` = OFF until registration is granted and recorded. Registration needs PAN, CIN, profile, self-declaration of lawful purpose, registered domain, callback URL, a Class 3 public certificate and SVG logo (R3 LG-030) — the owner's onboarding task [OWNER].
- **Paperless offline e-KYC XML** is treated as Phase 2 (registration needed per R3 LG-029) and is off by default.
- **Storage:** `ld_sealed.kyc_artefacts` holds only: verification result, attributes received (encrypted), last four digits where required, signature-verification evidence (certificate fingerprint, timestamp), purpose and consent reference. No Aadhaar number, no QR payload, no XML, no share code, no image, no biometric (NN-04; Aadhaar Act s.29(4); R3 LG-026). No Aadhaar Data Vault is needed because no number is held (UIDAI Circular 8 of 2025 applies ADV to requesting entities only — R3 LG-031 [VERIFY circular text]).
- **Revocation:** the privacy centre has "Revoke my Aadhaar verification data" — deletes the stored attributes, keeps only the fact and date of the verification and its revocation, sends an acknowledgement (Authentication and Offline Verification Regulations 2021 — holder may revoke consent to stored data; R3 LG-028 [VERIFY regulation number]); the identity level drops if no other L2 source remains.
- **Optionality:** every screen offering Aadhaar shows the alternatives (DigiLocker PAN, DSC, assisted L3) with equal prominence (Aadhaar Act s.4(3), s.8 proviso; R3 LG-021, LG-024).
- **Logo and wording:** the Aadhaar logo appears only if UIDAI permits (R3 LG-029 [VERIFY: regulation numbers — "Regs 251A–253" in the secondary source looks garbled]); copy says "Verify with Aadhaar (offline)", never "Aadhaar login" or "Aadhaar KYC".

**FR-P01-21 — DigiLocker (Requester).** LawDocs onboards as a DigiLocker Requester (senior authorised representative; NeGD verification; R3 LG-038). Uses in P01: pull issued **PAN** and **driving licence** (and other documents the purpose needs) with explicit, purpose-specific consent; verify issuer signature; store the **URI, document type, issuer, verification result, name-match score and fetched-at** — not the document copy — by default (NN-42; R3 LG-037–038). A copy is retained only if the user chooses "Save a copy to my Legal Vault" for a recorded purpose and only while flag `kyc.digilocker.retain_copy.enabled` = OFF → ON after NeGD's written confirmation [VERIFY with NeGD; OI-P01-03]. Data stays in India; DigiLocker-related incidents go to NeGD within 24 hours (P23 runbook; R3 LG-038 cl.4(e), 13). Sister products cannot use LawDocs' Requester integration without NeGD written approval (cl.17) — `int` refuses to proxy DigiLocker calls for any other product (CH-16). Copy says "LawDocs is not a DigiLocker" and the vault is called "Legal Vault" (R3 LG-036; CH-15).

**FR-P01-22 — PAN for individuals.** Primary: DigiLocker PAN (issuer-signed) with name match. Secondary: a licensed vendor PAN API only where the vendor gives a written warranty that its upstream access covers LawDocs' purpose (`kyc.pan.vendor.enabled` = OFF until the warranty is attached; R3 LG-047; R6 D-17; CH-04). LawDocs never calls Protean directly unless it becomes eligible. PAN stored as ciphertext + blind index + masked form; full PAN never in logs (NN-32).

**FR-P01-23 — What is never done.** No CKYC search or download (CH-03; R3 LG-046); no reuse of a sister regulated entity's CKYC result; no credit-bureau pull at onboarding or anywhere (CH-05; R3 LG-057–060) — users may upload their own credit report later as a document (P15); no direct PAN-database call; no scraping of the income-tax, MCA, GST or UIDAI portals (NN-05). `NN-05_no_closed_source_adapters` fails CI if a connector manifest declares a CKYCR, CIC, Protean-direct or portal-scraping endpoint.

**FR-P01-24 — DSC-based verification.** For professionals and signatories who hold a Class 3 DSC, the local signing agent (P08) signs a challenge; the certificate subject, issuer and validity are verified against the CA chain and revocation; the subject name is matched. This gives L2 without any Aadhaar route.

**FR-P01-25 — Re-verification and expiry.** Address-bearing attributes expire after `kyc.level_validity_months`; a professional's credential re-verification runs annually (FR-P01-40); a nominee designation requires the owner's L2 to be current at designation time only.

### 4F. KYB for companies, LLPs, firms and other organisations (CH-06)

**FR-P01-26 — Discovery input.** The discovery box accepts any one of: CIN, LLPIN, FCRN, GSTIN, entity PAN, LEI, Udyam Registration Number, or legal name + State. Local validation before any paid call: PAN `^[A-Z]{5}[0-9]{4}[A-Z]$` with the fourth character giving holder type (C company, F firm/LLP, T trust, A AOP, B BOI, H HUF, G government, L local authority, J artificial juridical person; P individual is rejected for entity onboarding with a clear message); CIN 21 characters (listing flag, industry code, State, year, ownership class, sequence); LLPIN `^[A-Z]{3}-[0-9]{4}$`; GSTIN 15 characters with State code, embedded PAN and check character verified locally; LEI 20 characters with ISO 17442 MOD 97-10 check digits; Udyam `UDYAM-XX-00-0000000` [VERIFY format]. One identifier is enough: GSTIN gives the PAN; the company-data provider gives PAN from CIN; PAN gives all GSTINs through the GSP.

**FR-P01-27 — Provider waterfall (`OnboardingDiscoveryWorkflow`).** Parallel calls, each with an 8-second timeout and a 25-second overall budget; partial results shown with "still checking" chips; circuit breaker switches to the secondary provider after three consecutive failures or p95 > 5 s:

| Port | Source (R6 §R6.6.3) | Facts | Rules |
|---|---|---|---|
| `COMPANY_DATA_PORT` | MCA21 master data through a licensed vendor (Probe42, Signzy, Surepass, Perfios-Karza — primary and secondary by contract [VERIFY each API, price and lawful-sourcing warranty]; R6 D-15) | Name, CIN/LLPIN, status, class, category, date of incorporation, registered office, capital, listing status, ROC, last AGM and balance-sheet dates, directors/designated partners (name, DIN/DPIN, designation, appointment date) | No MCA portal scraping (R3 LG-050; NN-05); never store directors' PAN or date of birth (R6 D-15); store source and fetch date per field |
| `GSTIN_PORT` | GSTN "Search Taxpayer" through a GSP (R3 LG-049; R6 D-16) | Legal and trade name, status, constitution, registration/cancellation dates, jurisdiction, principal and additional places of business, all GSTINs under the PAN | Public taxpayer data; cache 30 days (status 24 h) |
| `LEI_PORT` | GLEIF API (public) | LEI, legal name, address, status, renewal date, direct/ultimate parent | Free; cache 30 days |
| `ENTITY_LOCKER_PORT` | NeGD Entity Locker Requester API (R3 LG-039 [VERIFY coverage, eligibility and terms]) | Issued organisation documents (incorporation, GST, entity PAN) with the authorised signatory's consent | Flag `kyc.entity_locker.enabled` = OFF until verified; same storage rule as DigiLocker (URI + verification result) |
| `UDYAM_PORT` | Licensed vendor [VERIFY] | Udyam number, enterprise type, classification | OFF until vendor verified |
| Document-first fallback | User uploads certificate of incorporation, GST certificate, PAN card, partnership deed, trust deed, society registration, by-laws | Extracted by P05 document intelligence when available; until then manual entry with a reviewer | Low-confidence fields highlighted; reviewer maker-checker |

Every paid call is metered (`int.lookup_costs`: provider, unit cost, tenant or anonymous, purpose) and rate-limited: anonymous 3 discovery runs per IP per day with masked output, signed-in unverified 10, verified tenant 100 per month (`kyc.discovery.quota.*`). Results are cached per identifier (30 days; status fields 24 hours); a repeat within the cache window costs nothing.

**FR-P01-28 — Provenance per field.** Every pre-filled field carries `source` (vendor + upstream, GSTN, GLEIF, Entity Locker, user, document), `retrieved_at`, `confidence` (`EXACT` copied from an authoritative source; `DERIVED` computed, e.g., State from GSTIN; `INFERRED` rule-based guess) and a link to the stored response snapshot (hash). The profile card shows a badge per field; the user confirms the whole card or edits a field; editing an `EXACT` field needs a reason and keeps the source value; conflicting sources (MCA name differs from GST legal name) produce a conflict card with both values.

**FR-P01-29 — Constitution coverage.** Companies (private, public, OPC, Section 8, producer, Nidhi), LLPs, partnership firms (registered or unregistered; GSTIN + deed), proprietorships (proprietor's L2 + GSTIN/Udyam/shop licence), HUFs (karta's L2 + HUF PAN document), trusts and societies (registration certificate + trust deed/by-laws + PAN), co-operatives (registration + by-laws), government bodies (authorisation letter), foreign companies (FCRN + authorised representative). Each constitution has a required-evidence list in `kyc.kyb_requirements` (data, not code; NN-30).

**FR-P01-30 — Status checks.** MCA status Strike Off / Under process of striking off / Dissolved / Liquidated / Amalgamated, GST registration Cancelled: the wizard explains the status in plain words and blocks the "Verified organisation" badge and paid subscription (drafting for wind-up documents stays available); `PLT_SUPER_ADMIN` may override only by a Correction Entry citing the reason (e.g., a revival order).

**FR-P01-31 — Directors and KMP.** With the owner's confirmation, directors and designated partners from MCA data become person records (name, DIN/DPIN, designation, appointment date, `source = MCA_VIA_<vendor>`) in the company's people master; when the governance kernel is mounted (P13) they project into the director register; when the company also uses LawDocsComply, LDC is system of record and LawDocs reads through the contract (D-10, NN-47). No personal contact details are fetched; invitations go only to addresses the company enters.

**FR-P01-32 — Branches from GST.** Each GSTIN becomes a branch candidate (State, principal place, additional places) for P02's branch model; the user accepts which to create.

**FR-P01-33 — KYB result.** `kyc.kyb_cases` (`kyc_` prefix with `subject_kind = ORGANISATION`): states `DRAFT → DISCOVERED → CONFIRMED_BY_CUSTOMER → SIGNATORY_PENDING → UNDER_REVIEW (only when evidence needs a human) → VERIFIED | REJECTED | NEEDS_INFO`; result `VERIFIED_AUTO` (identifiers match authoritative sources and the signatory is a listed director/partner verified at L2), `VERIFIED_REVIEWED` (manual evidence approved by `OPS_ONBOARDING` maker + checker) or `UNVERIFIED`. Badge text: "Organisation details verified on <date> from <sources>" — never "government-approved" (NN-20).

### 4G. Authorised signatory and authority evidence

**FR-P01-34 — Who may act for the entity.** The person who signs the subscription, DPA, engagement letters or agreements **as the entity** must be an `ORG_APPROVER` (authorised signatory) at L2. Authority is established by one of:

| Basis | Evidence | Automatic match |
|---|---|---|
| Director / designated partner listed in MCA data | None beyond L2, if the L2 name matches the listed director (score ≥ threshold) | Yes (`VERIFIED_AUTO`) |
| Board resolution authorising the person (company) | Certified true copy of the resolution (upload; OCR extracts date, name, scope, limits when P05 is live) | No — reviewer checks name, date, scope, certification by a director or the company secretary |
| Authority letter on letterhead signed by a director | Letter + signer's director status | No |
| Partnership deed clause / partners' authority letter | Deed extract or letter signed by partners | No |
| LLP agreement clause / designated partners' resolution | Extract or resolution | No |
| Trust deed / society resolution / co-operative committee resolution | Extract or resolution | No |
| Power of attorney | Registered or notarised POA copy (as evidence only; a POA authorising a signatory is excluded from eSign by IT Act First Schedule entry 2 — only a POA empowering an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity is carved out, and Appendix F governs; NN-07; R3 LG-003) | No |

**FR-P01-35 — Authority scope and limits.** The authority record (`kyc.signatory_authorities`) stores the person, entity, basis, document reference, scope (all documents / named document types / value limit / until date), and validity. P02's delegation-of-authority matrix reads it: a signatory cannot sign above the recorded limit, and an expired authority blocks signing as the entity (`LD-KYC-040`) while still allowing personal signing.

**FR-P01-36 — Review queue.** Evidence-based authorities go to the KYB review queue (SCR-P01-14): `OPS_ONBOARDING` maker reviews, a different `OPS_ONBOARDING` or `OPS_DELIVERY_LEAD` checks (NN-18 class "master-data change of a client"); SLA 1 working day (`kyc.kyb.review_sla_hours` = 8 working hours); the customer can keep drafting while the case is pending, but cannot sign as the entity.

### 4H. Professional onboarding (NN-21; CH-08, CH-09)

**FR-P01-37 — Application.** A professional signs up (L1), opens "Join as a professional", reaches L2, and submits a profession-specific application to a PRO_FIRM tenant (individual practice = one-person firm):

| Profession | Credential fields | Evidence | Public profile fields (if listing is ever enabled) |
|---|---|---|---|
| Advocate (`PRO_ADVOCATE`) | Enrolment number, enrolment date, State Bar Council, Certificate of Practice number and date (BCI Certificate and Place of Practice (Verification) Rules 2015 [VERIFY]), bar association membership, qualifications, practice areas, courts, languages | Bar Council ID card, enrolment certificate, COP | **Rule 36 fields only:** name, address, telephone, email, enrolment number and date, State Bar Council, bar association membership, professional and academic qualifications, practice areas (BCI Rules Part VI Ch II r.36 as amended 2008; R3 LG-111). No photo, rating, review, fee, badge, success rate, testimonial or "book now" (NN-21) |
| Chartered accountant (`PRO_CA`) | ICAI membership number, ACA/FCA, COP status, firm name and FRN | Membership certificate, COP | Listing of practising CAs is **OFF** (ICAI 23 Oct 2019 announcement; R3 LG-115; CH-09) |
| Company secretary (`PRO_CS`) | ICSI membership (ACS/FCS), COP number | Membership certificate, COP | PCS listing **OFF** pending ICSI guidance (R3 LG-117) |
| Tax practitioner (`PRO_TAX_PRACTITIONER`) | GST practitioner enrolment number (CGST r.83 [VERIFY]), other registrations | Enrolment certificate | Per P16 rules |
| Other (`PRO_OTHER`: valuer, notary-facilitator, translator, forensic examiner) | Registration body and number | Registration certificate | Per P16 rules |

Bank and payout details are not collected here; P16/P17 create the Razorpay Route linked account through OH8, where the PA performs merchant due diligence (NN-22).

**FR-P01-38 — Verification desk.** The group professional directory is mastered by Operations Hub OH9 (`ProfessionalEmpanelled`, `ProfessionalSuspended`; Ecosystem Spec §6.29). P01 therefore: (a) captures the application and evidence in the professional's own PRO_FIRM tenant; (b) with the professional's consent, sends the application and evidence references to OH9 through `int` (`kyc.professional.verification_desk` = `OH9`; fallback `LOCAL` uses the same checklist in the LawDocs console until OH9 is live [OWNER]); (c) consumes `ProfessionalEmpanelled`/`ProfessionalSuspended` to set `pcr_` credential status. Checks: identity L2 name match with the credential; document authenticity review; registry check where an official online lookup exists and its terms allow manual use (State Bar Council rolls, ICAI/ICSI member directories) — performed by a person, never scraped (NN-05) [VERIFY each source]; COP validity date. Result statuses: `SUBMITTED`, `UNDER_REVIEW`, `VERIFIED`, `REJECTED`, `EXPIRED`, `SUSPENDED`.

**FR-P01-39 — Wording.** The badge says "Credentials checked by LawDocs on <date>: enrolment number and certificate of practice" — never "verified lawyer", "top lawyer" or any quality claim (NN-20; IMP-004).

**FR-P01-40 — Annual re-verification and suspension.** COP and membership re-checked every 12 months (`kyc.professional.reverify_months`); an expired COP or a disciplinary order (reported, or received as `ProfessionalSuspended`) suspends allocation within 1 hour; the professional and P16 are notified.

**FR-P01-41 — Employed professionals.** LawDocs-employed advocates do not practise while employed full-time (BCI Rule 49; R3 LG-112 [VERIFY]); their staff identity is in `ld-staff` (`OPS_PROFESSIONAL`) and they deliver non-reserved services (NN-41). The professional realm is for independent practitioners.

### 4I. Counterparty guest identity

**FR-P01-42 — Invitation.** When a user shares a document for negotiation, signing or witnessing (P07/P08), the invitee is a `prs_` person with the contact the initiator entered. The invitation (`ivt_`; ≥ 128-bit token, SHA-256 at rest, TTL `iam.guest.invite_ttl_days` default 14, revocable, re-send invalidates the previous token) is sent once by the initiator's chosen channel; reminders follow the initiator's schedule unless the guest opts out; no automated calls (NN-34). The initiator may instead "Share from my phone" (user-to-user deep link) (R4).

**FR-P01-43 — Guest session.** Opening the link asks for an OTP to the invited contact point; the session (`CP_GUEST`, AAL1) is bound to the invitation, the device and the shared items only. The guest sees only versions shared with them (NN-37), can comment, propose changes and message in the deal room, and signs through the ESP ceremony (P08) — ESP signer authentication is separate from LawDocs authentication (NN-03, NN-06). An initiator may require the guest to reach L2 before signing (`sgn.signer.min_identity_level`, P08 setting) — offered as DigiLocker PAN, Aadhaar offline QR or DSC, never mandatory Aadhaar.

**FR-P01-44 — Guest data and upgrade.** The guest's contact, OTP events, IP/device hashes and actions form the evidence trail for the transaction (P08 evidence pack). Notice shown before the OTP: who invited them, what LawDocs will record and why, retention, rights, and that they can create a free account. "Create my account" upgrades the guest to an `IND_OWNER` with a PERSONAL tenant and copies the executed documents they are party to into their vault (their own copy as a party). A guest never sees the initiator's other data.

**FR-P01-45 — Wrong recipient.** A guest can say "This is not me": the invitation is revoked, the initiator is told, and the shared content is not shown.

### 4J. Minors, wards and persons needing a guardian (NN-26)

**FR-P01-46 — Accounts are 18+.** Sign-up asks for a date of birth or an "I am 18 or older" declaration (`iam.age_assurance.mode`: `DECLARATION` default; `DIGILOCKER_TOKEN` when DPDP Rule 10 applies from 13 May 2027 — R3 LG-040, LG-066). A user who declares under 18 cannot create an account and is shown "Ask a parent or guardian to keep your documents in their LawDocs vault". No tracking, behavioural monitoring or targeted advertising of children anywhere (DPDP s.9(3); NN-26, NN-35).

**FR-P01-47 — Ward profiles.** An `IND_OWNER` at L2 may add a **ward profile** (a `prs_` person with `is_minor` or `needs_guardian`, no account) inside their Personal workspace, with guardianship evidence (birth certificate showing the parent, a court guardianship order, or a guardianship certificate for a person with disability) reviewed by `OPS_ONBOARDING` maker-checker [VERIFY acceptable proofs per Rule 10/11]. Two parents may both hold the ward (each L2). Documents about the ward (school, property inherited, maintenance orders) are filed under the ward. Signing on behalf of a minor follows the instrument rules in P06/P08 (a guardian signs in a representative capacity; some instruments need court permission [COUNSEL]).

**FR-P01-48 — Coming of age.** When the ward turns 18 (from the recorded date of birth), the guardian is prompted to hand over: the ward creates an account, verifies at L2 and accepts transfer; the ward's folder moves to the new PERSONAL tenant as a copy with history; the guardian keeps nothing unless the new owner shares back. If no handover happens within 12 months, the guardian is reminded quarterly; nothing is deleted automatically.

### 4K. Nominee and legacy access (DPDP s.14; R3 LG-068)

**FR-P01-49 — Designation.** An `IND_OWNER` at L2 with AAL2 may designate up to `iam.nominee.max` (default 3) nominees, each with: person, contact points, scope (whole vault / named folders / named documents), access type (read and download; never edit or delete), waiting period (`iam.nominee.release_waiting_days`, default 30, range 7–90), and an optional message. The nominee accepts by OTP (becoming `IND_NOMINEE`, no access yet). The owner can change or revoke at any time; every change notifies the nominee.

**FR-P01-50 — Release.** A nominee requests release with a qualifying event (`DEATH` with a death certificate; `INCAPACITY` with a medical certificate or court order; or the owner-chosen `INACTIVITY` trigger of P04 FR-P04-60, which needs no evidence review and goes from identity verification straight to the waiting period — Appendix A §A.8). Workflow (§5.7): the nominee must reach L2; `OPS_ONBOARDING` maker reviews the evidence, `PLT_DPO` or `OPS_DELIVERY_LEAD` checks at AAL3 (NN-18); the system sends notices to every contact point of the owner and starts the waiting period ("dead-man switch": any sign-in or "I am fine" response by the owner cancels the release and alerts them); at expiry the nominee receives read-only access to the scoped items for `iam.nominee.access_days` (default 180, renewable on request) with every access logged. Optional proof of presence of the nominee via the Aadhaar App (R3 LG-033) when Phase 2 is live [VERIFY].

**FR-P01-51 — Limits.** Release gives access, not ownership: copy explains that a nominee under DPDP s.14 exercises the principal's rights and that succession is governed by the law of succession and any will — LawDocs makes no determination of heirship [COUNSEL]. Wills stored in the vault are shown with a note that a will on LawDocs is a copy and that execution formalities apply (NN-07, NN-40). Death and incapacity evidence is held in `ld_sealed`.

### 4L. Consent artefacts, notices, withdrawal and the privacy centre (NN-26; CH-18)

**FR-P01-52 — Purpose catalogue.** `kyc.consent_purposes` (data, versioned, per operating entity and brand): each purpose has code, description in plain words, data items, lawful basis (consent, or legitimate use under DPDP s.7 [VERIFY clause letters; R3 LG-064], or contract), recipients, retention, whether it is required for the service, and the withdrawal effect. Seed purposes:

| Code | Basis | Default | Notes |
|---|---|---|---|
| `ACCOUNT_SERVICE` | Voluntarily provided / contract | Required | Account, vault, drafting, signing as the user requests |
| `IDENTITY_VERIFICATION` | Consent per run | Off until used | One artefact per verification run (FR-P01-18) |
| `AI_ASSISTANCE` | Consent | Off; asked at first Vidhi use | Vidhi on the user's content via Bedrock India (NN-15); no training |
| `DOCUMENT_INTELLIGENCE` | Consent | Asked at first OCR/translation | P05 |
| `PROFESSIONAL_SHARING` | Consent per engagement | Asked at booking | Share the matter summary/documents with the assigned professional (P16) |
| `ECOSYSTEM_SHARING:<product>:<datatype>` | Consent per product and data type | Off | Purpose-bound sharing with Finbyx, Udofin, Equator, LDC (CH-16; NN-24); ledgered |
| `MARKETING_EMAIL`, `MARKETING_SMS`, `MARKETING_WHATSAPP` | Consent | Off, unticked | Separate per channel (NN-50; E-Commerce Rules no pre-ticked consent — R3 LG-141) |
| `PRODUCT_ANALYTICS` | Consent | Off | Non-essential analytics; essential telemetry is service operation |
| `COOKIES_NON_ESSENTIAL` | Consent | Off | Banner with equal "Reject" and "Accept" |
| `TESTIMONIAL_PUBLICATION` | Consent per testimonial | Off | NN-49 |
| `CALL_RECORDING`, `AI_VOICE_CONTACT` | Consent | Off | NN-34; SGI labelling (R3 LG-078) |
| `DIRECTORY_LISTING` (professionals) | Consent | Off; only when a profession's listing switch is ON | NN-21 |

**FR-P01-53 — Consent artefact.** `kyc.consents` (`cns_`): principal (person), tenant context, operating entity, brand, purpose code, notice version (`ntv_`), language shown, data items, channel and method (checkbox, OTP-confirmed, signed), captured_at, captured_by (self, guardian, delegate with authority), status (`GIVEN`, `WITHDRAWN`, `EXPIRED`, `SUPERSEDED`), withdrawal time and channel, and `consentref` used in ecosystem events. Append-only history; a consent is never edited — a new artefact supersedes it.

**FR-P01-54 — Notices.** `kyc.notice_versions` (`ntv_`): itemised notice per purpose set (data, purposes, how to withdraw, how to exercise rights, how to complain to the Data Protection Board — DPDP s.5, Rule 3 from 13 May 2027 [VERIFY rule text]), content hash, effective date, languages (English and the D-07 UI languages; any Eighth Schedule language on request — DPDP s.5(3) [VERIFY]), reviewer of record (`PLT_DPO`), maker-checker publication (NN-30). A material change requires re-consent at next sign-in for consent-based purposes; legitimate-use purposes get a notice. Until 13 May 2027, the SPDI Rules 2011 privacy-policy and consent requirements apply in parallel (R3 LG-075).

**FR-P01-55 — Withdrawal.** One tap in the privacy centre or from any marketing message; as easy as giving (DPDP s.6(4); R3 LG-063). Effects: processing for that purpose stops; internal propagation ≤ 1 hour; ecosystem `ConsentWithdrawn` through `int` to every recipient (Ecosystem Spec §6.14; ≤ 1 hour [REC]); marketing suppression in OH3 CRM ≤ 1 hour; data collected under that purpose is erased per the retention schedule unless another basis or a legal hold applies. Withdrawal of `AI_ASSISTANCE` stops Vidhi on the user's content and deletes AI conversation memory (P09).

**FR-P01-56 — Consent manager adapter.** `CONSENT_MANAGER_PORT` accepts artefacts from a consent manager registered with the Board (DPDP s.6(7)–(9), Rule 4 from 13 Nov 2026; R3 LG-070); LawDocs does not become a consent manager. Flag `kyc.consent_manager.enabled` = OFF until a registered consent manager and its interface exist [VERIFY].

**FR-P01-57 — Privacy centre** (SCR-P01-18). Shows: notices accepted; every consent with on/off toggles; verification records (what was verified, from where, when; "Revoke my Aadhaar verification data"); devices and sessions; nominees and delegates; data-rights requests — access (summary of personal data and processing), correction, erasure, nomination, grievance (DPDP ss.11–14; Rule 14 response ≤ 90 days, internal SLA 30 days — R3 LG-068); download my data (P20 export, NN-11); contact of the DPO and the Grievance Officer of the brand's operating entity. Requests about data inside a company tenant (where LawDocs is processor — R3 LG-072) are forwarded to that tenant's privacy contact, and the requester is told so plainly.

**FR-P01-58 — Grievance clock.** Identity, consent and privacy grievances follow the IT Rules 2021 as amended (acknowledge ≤ 24 hours, resolve ≤ 7 days from 20 Feb 2026 — R3 LG-077 [VERIFY]) and the E-Commerce Rules for consumer purchases (acknowledge ≤ 48 hours, redress ≤ 1 month — R3 LG-141); the stricter clock wins (NN-26).

### 4M. Partner onboarding API and Operations Hub provisioning (R-003; NN-24)

**FR-P01-59 — Routes (API surface owned by P19 §4K; activation semantics owned here).** Three routes create workspaces on someone else's initiative, and all follow one rule — an **invitation, never a live tenant**, until the customer confirms:

| Route | Who | Mechanism |
|---|---|---|
| Group products | Finbyx, Udofin, LawDocsComply | Never create LawDocs tenants directly: they raise `POST /v1/crm/requests` (product `LAWDOCS`) to the Operations Hub or use OH4's provisioning flow; OH approves with maker-checker and emits `TenantProvisioned` (FR-P01-62; P19 FR-P19-58) |
| Third-party partners under a partner agreement | Resellers, CA/CS firms acting for their clients, chambers, bank SME desks | P19 `POST /v1/int/partner/onboarding-batches` (≤ `int.partner.onboarding.max_batch_rows`, default 500) and `POST /v1/int/partner/onboarding-invitations` (single); P01 supplies the KYB pre-fill (FR-P01-27) as an unconfirmed snapshot |
| Individuals referred by Finbyx or Udofin | Borrowers who want their own Legal Vault | No bulk onboarding of individuals from partner data (P19 FR-P19-63); the individual opts in through a `deposit_link` (Appendix Y) with a pairwise pseudonymous reference only (Ecosystem Spec §4.3), signs in by OTP and confirms; LawDocs receives no loan data unless the individual consents to `ECOSYSTEM_SHARING:<product>:<datatype>` |

**FR-P01-60 — Activation flow.** The invitation page shows the DPDP notice, the requester's identity, the pre-filled fields with source labels, plan and all-in price (NN-50) and the terms. The signatory verifies by OTP (plus optional DigiLocker or Entity Locker pull), confirms or corrects each pre-filled field (FR-P01-28), accepts terms and DPA, and becomes `ORG_OWNER`. LawDocs captures its own consent artefact (purpose code `PARTNER_ONBOARDING_PREFILL`, proposed in Appendix Y for the ecosystem consent table). Activation ≤ 4 taps from the email. Unconfirmed invitations expire after 30 days and their snapshots are deleted. On activation LawDocs reports the tenant to the Operations Hub with `TenantRegistered` (Appendix Y) for the commercial record.

**FR-P01-61 — No implicit access; same-organisation products.** The requester sees status only (`INVITED`, `OPENED`, `ACTIVATED`, `DECLINED`, `EXPIRED`); any later access needs a delivery grant the customer approves (P02, P18; NN-17). When the same organisation also uses LawDocsComply, a `legal_sor_link` (Appendix Y) records which product is system of record per kernel; LDC remains SoR for governance and HRMS (D-10, NN-47). Cross-product customer sign-in uses the customer's own enterprise IdP configured in both products; a token-exchange launch (RFC 8693) with OTP step-up, on the Ecosystem Spec §4.4 pattern, is not yet in Appendix Y and is raised as OI-P01-12. LawDocs eSign is **not** offered to partners as an API for their own documents (NN-06): under a `signing_handoff_link` (Appendix Y) a requesting product may only create LawDocs-hosted signing requests inside the organisation's own LawDocs tenant, and consent and logs stay with LawDocs as ASP (R3 LG-007).

**FR-P01-62 — Operations Hub provisioning.** When OH4 approves a provisioning request, `int` consumes `TenantProvisioned` (signed; Ecosystem Spec §6.29), creates the tenant through P00 `TenantProvisionWorkflow` with the first-admin work email (`legalbasis = CONTRACT_PERFORMANCE_VENDOR`, no password), and acknowledges with `PUT /v1/provisioning-requests/{id}` (`ACCEPTED`, `READY`, `FAILED` with reason). A PRODUCTION request without MSA and DPA references is rejected with `regulatory-guard`. At most one live tenant per `(org_id, product, environment)`. The tenant starts in `PENDING_CONFIRMATION` and the first admin activates it through FR-P01-60. LawDocs is not a listed `TenantProvisioned` product in Ecosystem Spec v1.1; Appendix Y adds `LAWDOCS` to the product enumeration — until it is accepted, OH4 uses the P19 single-invitation endpoint (`int.eco.v12_contracts.enabled` = OFF).

### 4N. Fast onboarding journeys

**FR-P01-63 — Individual fast path: "≤ 2 minutes to first draft".**

| Step | Screen | Taps / inputs | Notes |
|---|---|---|---|
| 1 | Document page (e.g., Rent agreement) on www | Tap "Draft free" | Template automation, not AI (NN-14, CH-30) |
| 2 | Questionnaire (P06) in a side panel; live preview | ≤ 10 answers | Anonymous draft session: server-side, keyed by an HttpOnly cookie, TTL 24 h (`iam.anonymous_draft.ttl_hours`); a one-line notice at the first field ("We keep this draft for 24 hours unless you save it — Privacy notice") |
| 3 | Preview complete | Tap "Save and download" | — |
| 4 | Sign-in sheet | Enter mobile (or "Use email" / Google / Microsoft / passkey) → 6-digit code | Notice + optional unticked marketing consents; "I am 18 or older" |
| 5 | Done | — | PERSONAL tenant provisioned; draft saved to Legal Vault › Drafts; download offered as DOCX and PDF; nudge to add a passkey |

Budget: ≤ 6 taps excluding questionnaire answers; account creation ≤ 3 taps + one code; p75 ≤ 2 minutes for a ≤ 10-question document. No verification, payment method or profile form is asked before first value.

**FR-P01-64 — Company set-up wizard: "≤ 10 minutes".**

| Step | Content | Time target |
|---|---|---|
| 1 Account | Work email OTP + mobile OTP; name; role in the company (drives home dashboard, P02) | 1 min |
| 2 Identify | One identifier → notice and consent for lookups (purpose, sources, retention; FR-P01-72 pattern) → discovery (≈ 20 s) | 1 min |
| 3 Confirm profile | Profile card with provenance and conflicts; directors; GSTIN branches | 2 min |
| 4 Workspace | Workspace name; departments from a template by constitution and size (P02; renameable); approval model default (single checker / two-level / department head) with SoD preview | 2 min |
| 5 People | Invite colleagues with role templates ("Legal team: 1 CLO, 2 makers, 1 checker"); import CSV or connect Microsoft 365 / Google directory (P19) — skippable | 2 min |
| 6 Signatory | "Are you an authorised signatory?" → L2 + authority basis now, or route to the signatory by invitation | 1 min (or deferred) |
| 7 First value | Choose: draft an NDA / upload existing agreements by folder (P04 bulk intake) / start a contract request; three-step progress ring on home | 1 min |

Every step auto-saves; resume within 30 days; reminders on day 1 and day 3 (transactional only; marketing only with consent). An unverified organisation can draft, negotiate and store immediately; signing **as the entity** waits for signatory verification (FR-P01-36). Assisted onboarding by `OPS_ONBOARDING` runs under a client-approved onboarding grant (P02 grant type `ONBOARDING`), every field shows who completed it.

**FR-P01-65 — Professional fast path.** Sign-up → profession → credential fields (pre-filled from the uploaded certificate when P05 is live) → L2 → submit; target ≤ 8 minutes; status visible with expected review time.

**FR-P01-66 — Guest to account.** One tap after signing ("Keep a copy in your own free Legal Vault") with the contact already verified.

**FR-P01-67 — Funnel analytics.** Per-step drop-off, time per step, verification success by method, discovery success by provider, assisted vs unassisted completion — aggregated, no personal content (NN-19 for anything sent to OH).

**FR-P01-68 — Migrated users (P00 wave activation).** A migrated person signs in by OTP to a migrated contact point; the flow marks the contact verified, links the migrated PERSONAL (or COMPANY) tenant, shows "What moved from old LawDocs" and resolves `DUP_CANDIDATE` merges with the user.

### 4O. Consumer Help brand identity separation (D-06; NN-23)

**FR-P01-69 — Separate fiduciary, separate account by default.** Consumer Help runs under its own brand and operating entity. Its customers sign up through the brand's client (`ld-web` brand flavour) and receive the brand's own notice and consents (`operating_entity_id` = Consumer Help entity). A person who already has a LawDocs account may choose "Use my LawDocs sign-in": authentication is shared (same Keycloak user), but **profile, verification results and documents are not shared** unless the person consents to a specific copy (e.g., copy my L2 verification result) — because the two entities are separate fiduciaries [INTERP; COUNSEL].

**FR-P01-70 — Ethical wall at identity level.** Consumer Help case managers (`OPS_CONSUMER_CASE_MANAGER`, staff realm) never receive any role in LDC/Finbyx/Udofin/Equator tenants or group grants combining those roles (P02 SoD); identity events of Consumer Help users never flow to lender-facing products (NN-23).

### 4P. Accessibility of authentication and verification (NN-28)

**FR-P01-71 — Accessible flows.** WCAG 2.2 AA including SC 3.3.8 (no cognitive function test; paste and password managers allowed; passkeys offered); OTP fields as one input with `autocomplete="one-time-code"`; time-outs extendable ("Need more time?"); voice OTP and email alternatives; screen-reader-tested QR flows with a document-upload alternative; L3 assisted verification by video or phone with sign-language interpretation on request (R3 LG-137 [VERIFY provider]); no liveness/blink checks anywhere in LawDocs (R3 LG-136 [VERIFY]); every step usable at 400% zoom and by keyboard; Hindi and launch languages for every identity screen.

**FR-P01-72 — Lookup notice pattern.** Before any third-party lookup (KYB, DigiLocker, Aadhaar offline, vendor PAN) the user sees one short notice: purpose, source, what will be stored, retention, alternative — with "Continue" and "Do it another way" of equal weight (NN-50).

---

## 5. Workflows and state machines

### 5.1 Account and membership

| State | Entry | Transitions | Guard / side effects |
|---|---|---|---|
| `PENDING_OTP` | Sign-up started | `ACTIVE` (OTP verified), `ABANDONED` (24 h) | Anonymous draft linked on activation |
| `ACTIVE` | OTP verified / SSO / migration activation | `LOCKED` (abuse), `SUSPENDED` (platform action with reason), `CLOSING` (user request) | PERSONAL tenant created; `in.lawdocs.iam.UserRegistered.v1` |
| `LOCKED` | Abuse thresholds | `ACTIVE` (cool-off or recovery) | User notified on every known contact |
| `CLOSING` | User requests closure | `CLOSED` after 30-day grace (export offered; legal holds respected) | Memberships ended; nominee designations end |
| `CLOSED` | Grace elapsed | — | Erasure per retention schedule; ledger retains pseudonymous events |

Membership: `INVITED → ACTIVE → SUSPENDED ⇄ ACTIVE → ENDED`; invitations expire per setting; ending a membership revokes sessions in that tenant within 60 seconds.

### 5.2 Identity verification run (`kyc_`)

`REQUESTED (purpose, notice, consent) → IN_PROGRESS (provider) → {SUCCEEDED (level updated; attributes stored per rules) | FAILED (reason; alternative offered) | NEEDS_REVIEW (name mismatch, manual document) → REVIEWED_OK | REVIEWED_REJECTED}`; `SUCCEEDED → REVOKED` (user revokes) or `EXPIRED` (validity). Each transition is a ledger event; provider responses are hashed, never logged.

### 5.3 KYB case

`DRAFT → DISCOVERED → CONFIRMED_BY_CUSTOMER → SIGNATORY_PENDING → (UNDER_REVIEW) → VERIFIED_AUTO | VERIFIED_REVIEWED | REJECTED | NEEDS_INFO`; `VERIFIED_* → REVERIFY_DUE` (monthly status refresh finds a change: struck off, GST cancelled, director ceased) → back to `UNDER_REVIEW` or `VERIFIED_*`. Reviewer maker ≠ checker; SLA timer 8 working hours.

### 5.4 Signatory authority

`PROPOSED → EVIDENCE_SUBMITTED → VERIFIED (auto or reviewed) → ACTIVE → {EXPIRED (until date) | REVOKED (company owner/admin, or board-resolution withdrawal) | SUPERSEDED}`. Only `ACTIVE` authorities let a person sign as the entity; P02 DoA reads limits.

### 5.5 Professional credential (`pcr_`)

State machine: Appendix A §A.5 governs (Resolution R-A-03: credential SUSPENDED/EXPIRED forces marketplace onboarding SUSPENDED).

`DRAFT → SUBMITTED → UNDER_REVIEW (OH9 or LOCAL desk) → VERIFIED → {REVERIFY_DUE (12 months) → UNDER_REVIEW | EXPIRED | SUSPENDED (disciplinary order, lapsed COP) → VERIFIED (reinstated) | WITHDRAWN}`; `REJECTED` with reasons and resubmission.

### 5.6 Guest invitation

`CREATED → SENT → OPENED → OTP_VERIFIED (session) → {COMPLETED (action done) | DECLINED ("not me" or decline) | EXPIRED | REVOKED (initiator)}`; `COMPLETED → UPGRADED` when the guest creates an account.

### 5.7 Nominee release

State machine: Appendix A §A.8 governs (Resolution R-A-04). One `nom_` record (`kyc.nominations`); P04 `dms.nominees` is its vault-scope projection and P04 §5.4 describes the same claim machine. Canonical state names are used below (`CLAIMED` was "release requested"; `EXPIRED` was "closed").

| State | Actor | Guard | Side effects |
|---|---|---|---|
| `DESIGNATED` | Owner | Owner L2, AAL2 | Nominee notified |
| `ACCEPTED` | Nominee | OTP | — |
| `CLAIMED` | Nominee | Nominee L2; event type (death, incapacity or inactivity trigger); evidence uploaded to `ld_sealed` | Review task; `dms.NomineeClaimRaised` |
| `IDENTITY_VERIFIED` | System | Identity matches the designation | — |
| `EVIDENCE_VERIFIED` | `OPS_ONBOARDING` maker → checker (`PLT_DPO` or `OPS_DELIVERY_LEAD`, AAL3); death/incapacity triggers only | Maker ≠ checker | Owner notified on every contact point |
| `WAITING` | System | `iam.nominee.release_waiting_days` | Any owner sign-in or "I am fine" → `CANCELLED_BY_OWNER` and alert (`LD-KYC-060`) |
| `OBJECTED` | Co-nominee or family member with standing | Reason and evidence | Human review; no release |
| `REJECTED` | Checker | Reason | Nominee informed |
| `RELEASED` | System | Timer elapsed without cancellation | Read-only grant (`grt_`, type `NOMINEE`) for scoped items; every access logged; `kyc.NomineeReleased` |
| `EXPIRED` | System or nominee | Access period ended or nominee closes | Grant revoked |

### 5.8 Consent

`GIVEN → {WITHDRAWN | EXPIRED | SUPERSEDED (new notice version accepted)}`; withdrawal emits `in.lawdocs.kyc.ConsentWithdrawn.v1` and, via `int`, `in.infrabyx.privacy.ConsentWithdrawn.v1` to every recipient of that `consentref`.

### 5.9 Onboarding invitation (`onb_`; created by P19 or OH provisioning, activated here)

State machine: Appendix A §A.2 governs (Resolution R-A-02): this is the short form; the canonical machine adds the intermediate states `IDENTITY_VERIFIED`, `KYB_CONFIRMED` and `TERMS_ACCEPTED` between `OPENED` and `ACTIVATED`. `iam.onboarding_invitations` is the single record; P19's partner-batch row references the `onb_` id.

`INVITED (pre-fill snapshot unconfirmed) → OPENED → IDENTITY_VERIFIED → KYB_CONFIRMED → TERMS_ACCEPTED → {ACTIVATED (signatory verified, fields confirmed, terms and DPA accepted; tenant READY; `TenantRegistered` to OH) | DECLINED | EXPIRED (30 days; snapshot deleted)}`; the requester sees status only.

---

## 6. Screens and UX

| ID | App | Purpose | Key components | Empty / error states | Mobile | Accessibility |
|---|---|---|---|---|---|---|
| SCR-P01-01 | auth.lawdocs.in | Sign-in / sign-up | Mobile field first; "Use email", Google, Microsoft, passkey, SSO ("Work account") | Wrong code: remaining attempts shown; lock message with help | Native OTP autofill | One field per step; errors announced; SC 3.3.8 |
| SCR-P01-02 | auth | OTP entry | Single input, resend timer, change number | Expired code → resend | SMS Retriever / one-time-code | `autocomplete="one-time-code"` |
| SCR-P01-03 | web/mobile | Passkey prompt after first sign-in | One-tap enrol; "Not now" equal weight | Unsupported device → hidden | Platform biometrics | Text explains passkeys plainly (`hlp.iam.passkey`) |
| SCR-P01-04 | www side panel | Anonymous draft save sheet | Sign-in inline; notice; 18+ declaration | — | Bottom sheet | Focus trapped in sheet, Escape closes |
| SCR-P01-05 | web | Security settings | Factors, passkeys, recovery codes, sessions, devices | — | Yes | — |
| SCR-P01-06 | web | Verification centre ("Verify your identity") | Current level, what it unlocks, methods with equal prominence (DigiLocker PAN, Aadhaar offline, DSC, assisted) | Failure → alternative method | Camera QR scan; upload fallback | Each method has a non-visual path |
| SCR-P01-07 | web | DigiLocker consent and result | Documents requested, purpose, storage statement (URI only) | DigiLocker down → retry later or other method | In-app browser | — |
| SCR-P01-08 | web | Aadhaar offline verification | Scan QR / upload e-Aadhaar; attributes to be read; "We never store your Aadhaar number" | Signature invalid → explain, alternatives | Camera | Upload alternative for users who cannot scan |
| SCR-P01-09 | web | Company discovery | One identifier field; lookup notice; progress chips per source | Not found → document-first fallback | Yes | Live region for "still checking" |
| SCR-P01-10 | web | Company profile card | Fields with provenance badges, conflict cards, directors, branches | Struck-off status banner | Stacked | Badges have text labels |
| SCR-P01-11 | web | Company set-up wizard (steps 4–7) | Departments template, approval model with SoD preview, invites, first value | — | Yes | Step headings; progress announced |
| SCR-P01-12 | web | Signatory authority | Basis picker, evidence upload, scope/limits | Expired authority banner | Yes | — |
| SCR-P01-13 | delivery (practitioner) | Professional application | Profession-specific fields, evidence, status timeline | Rejected → reasons, resubmit | Yes | — |
| SCR-P01-14 | console / delivery | KYB and credential review queue | Case, sources, evidence viewer, name-match score, maker/checker actions, SLA | — | — | Evidence viewer keyboard accessible |
| SCR-P01-15 | guest | Guest landing | Who invited you, what you are asked to do, notice, OTP | "This is not me" | Primary target | Plain language; Hindi toggle |
| SCR-P01-16 | web | Wards (guardian) | Ward profiles, evidence status, coming-of-age handover | — | Yes | — |
| SCR-P01-17 | web | Nominees | Designate, scope, waiting period, status; nominee view of release request | — | Yes | — |
| SCR-P01-18 | web | Privacy centre | Notices, consents (toggles), verification records and revocation, requests, download my data, DPO/Grievance contacts | — | Yes | Toggles state in text |
| SCR-P01-19 | console | Notice versions and consent purposes | Draft, diff, translations, reviewer, publish (maker-checker) | — | — | — |
| SCR-P01-20 | console | Identity providers and KYC/KYB vendors | Provider config, health, cost, kill switches, verification-gate status | Gated provider shows the open VERIFY row | — | — |
| SCR-P01-21 | console / OH4 | Partner onboarding requests | Requests, bulk uploads with row results, status | — | — | — |
| SCR-P01-22 | web | SSO and SCIM settings | Domain verification, IdP metadata, group mapping, enforce SSO, break-glass owners | Domain unverified → steps | — | — |

**Click budgets.** Sign-in for a returning user: ≤ 2 taps + code (or 1 tap with a passkey). From home to "Verify your identity": ≤ 2 taps. From home to withdraw a marketing consent: ≤ 3 taps (Profile → Privacy → toggle) or 1 tap from the message footer. Company owner from home to invite a colleague: ≤ 3 taps.

**Help keys:** `hlp.iam.passkey`, `hlp.iam.otp`, `hlp.iam.step_up`, `hlp.kyc.identity_level`, `hlp.kyc.ovse`, `hlp.kyc.digilocker_uri`, `hlp.kyc.name_match`, `hlp.kyc.kyb_provenance`, `hlp.kyc.authorised_signatory`, `hlp.kyc.board_resolution`, `hlp.kyc.rule36_profile`, `hlp.kyc.cop`, `hlp.kyc.guest`, `hlp.kyc.ward`, `hlp.kyc.nominee`, `hlp.kyc.consent`, `hlp.kyc.notice_version`, `hlp.kyc.withdraw_consent`, `hlp.kyc.data_rights`, `hlp.kyc.grievance_officer`.

---

## 7. Backend design

### 7.1 Modules

`iam` (persons, users, memberships, invitations, sessions/devices mirror, SSO/SCIM, step-up, guest sessions); `kyc` (verification runs and levels, Aadhaar offline, DigiLocker, PAN, KYB cases, signatory authorities, professional credentials, guardianship, nominee release, consent purposes, consents, notice versions, rights requests); `int` (partner onboarding API surface, OH provisioning consumer, ecosystem consent events); `core` (tenant provisioning).

### 7.2 Tables

| Table | Key columns | RLS / store | Retention class |
|---|---|---|---|
| `iam.persons` (`prs_`) | names, contact points (enc/bidx/masked), language, a11y prefs, is_minor, deceased_at | Tenant-scoped views; person master platform-scoped via `ld_platform` with logged access | Life of account + statutory |
| `iam.users` (`usr_`) | keycloak_sub, realm, person_id, status, brand | Platform | Life + 1 y |
| `iam.memberships` (`mbr_`) | person_id, tenant_id, kind, status, valid_period | Tenant | Life + 8 y (history) |
| `iam.invitations` (`ivt_`) | token_hash, kind, contact (enc), tenant_id, ttl, status | Tenant | 1 y |
| `iam.devices` (`dev_`) | user_id, platform, attestation, last_seen | Platform | Life + 1 y |
| `iam.sso_connections`, `iam.scim_tokens`, `iam.domain_verifications` | tenant_id, protocol, metadata, token_hash | Tenant | Life |
| `kyc.verifications` (`kyc_`) | person_id/org ref, purpose, method, provider, result, notice_id, consent_id | Tenant + `ld_sealed` artefact ref | 8 y (result); attributes per purpose |
| `ld_sealed.kyc_artefacts` | verification_id, attributes_enc, last4 (where required), signature evidence | Sealed | Purpose-bound; deleted on revocation |
| `kyc.identity_levels` | person_id, level, method, valid_until | Platform-scoped, logged | Life |
| `kyc.digilocker_records` | person_id, uri, doc_type, issuer, verified_at, name_match | Sealed ref | Until purpose ends or revocation |
| `kyc.kyb_cases`, `kyc.kyb_facts` | legal_entity_id, field, value_enc, source, retrieved_at, confidence, snapshot_hash | Tenant | Life + 8 y |
| `kyc.signatory_authorities` | person_id, legal_entity_id, basis, doc_id, scope, limit, valid_period, status | Tenant | Life + 8 y |
| `kyc.professional_credentials` (`pcr_`) | person_id, profession, numbers (enc), body, cop dates, status, desk | PRO_FIRM tenant | Life + 8 y |
| `kyc.guardianships` (`gdn_`) | guardian_person_id, ward_person_id, basis, evidence ref (sealed), status | Tenant | Until handover + 8 y |
| `kyc.nominations` | owner_person_id, nominee_person_id, scope, waiting_days, status, release refs | Tenant + sealed evidence | Life + 8 y |
| `kyc.consent_purposes`, `kyc.notice_versions` (`ntv_`) | code, basis, version, hash, languages, reviewer | Platform (per operating entity/brand) | Permanent |
| `kyc.consents` (`cns_`) | person_id, tenant_id, purpose, notice_id, status, captured_by | Tenant | Life + 8 y (proof of consent) |
| `kyc.rights_requests` | person_id, type, status, due_at, forwarded_to | Platform/brand | 8 y |
| `iam.onboarding_invitations` (`onb_`) | origin (OH provisioning / partner batch / single), requester ref, subject hash, snapshot ref, consentref/legalbasis, status | Platform | 3 y (snapshots deleted at expiry) |
| `int.lookup_costs` | provider, unit_cost, tenant_id, purpose | Platform | 8 y |

### 7.3 APIs (selected; full list in OpenAPI)

| Method and path | Purpose | Scope / role | Idempotent |
|---|---|---|---|
| `POST /v1/auth/otp:send`, `POST /v1/auth/otp:verify` | OTP (BFF-only; rate-limited) | public | Key per attempt |
| `GET /v1/me`, `PATCH /v1/me` | Profile | user | Yes |
| `GET/DELETE /v1/me/sessions/{id}`, `POST /v1/me/sessions:revoke-all` | Sessions | user | Yes |
| `POST /v1/me/passkeys`, `DELETE /v1/me/passkeys/{id}` | Passkeys (WebAuthn ceremonies) | user AAL2 for delete | Yes |
| `POST /v1/kyc/verifications` | Start verification (purpose, method) | user | Yes |
| `POST /v1/kyc/verifications/{id}:complete` | Provider callback / QR result | provider / user | Yes |
| `POST /v1/kyc/aadhaar-offline/revoke` | Revoke stored Aadhaar attributes | user AAL2 | Yes |
| `POST /v1/kyc/discovery` | Organisation discovery run | user (quota) | Yes (identifier hash) |
| `POST /v1/kyc/kyb-cases/{id}:confirm` | Customer confirms profile | `ORG_OWNER` | Yes |
| `POST /v1/kyc/signatory-authorities` / `:submit` / `:review` / `:revoke` | Authority lifecycle | owner/admin; reviewer | Yes |
| `POST /v1/kyc/professional-credentials` / `:submit` | Professional application | professional | Yes |
| `POST /v1/invitations`; `POST /v1/invitations/{token}:accept` / `:decline` | Invitations incl. guests | per kind | Yes |
| `POST /v1/kyc/wards`; `POST /v1/kyc/nominations`; `POST /v1/kyc/nominations/{id}:request-release` | Guardianship, nominees | owner AAL2; nominee L2 | Yes |
| `GET /v1/privacy/consents`; `POST /v1/privacy/consents`; `POST /v1/privacy/consents/{id}:withdraw` | Consents | user | Yes |
| `GET /v1/privacy/notices/{purposeSet}` | Current notice by language | public | — |
| `POST /v1/privacy/requests` | Data-rights request | user | Yes |
| `GET /v1/onboarding/invitations/{token}`, `POST /v1/onboarding/invitations/{token}:activate` / `:decline` | Activation flow for partner and OH-originated invitations (partner-facing endpoints are P19 §4K) | invitee (OTP session) | Yes |
| `PUT /v1/provisioning-requests/{id}` (outbound to OH) | Provisioning acknowledgement | `int` | Idempotency-Key |
| `/scim/v2/Users`, `/scim/v2/Groups` | SCIM | tenant SCIM token | — |

### 7.4 Domain events

`in.lawdocs.iam.UserRegistered.v1`, `…iam.ContactPointVerified.v1`, `…iam.MfaFactorChanged.v1`, `…iam.SessionsRevoked.v1`, `…iam.AccountRecovered.v1`, `…iam.MembershipChanged.v1`, `…iam.InvitationSent.v1`, `…iam.GuestUpgraded.v1`, `…iam.SsoConfigured.v1`, `…iam.ScimUserDeprovisioned.v1`, `…kyc.VerificationCompleted.v1`, `…kyc.VerificationRevoked.v1`, `…kyc.IdentityLevelChanged.v1`, `…kyc.KybCaseVerified.v1`, `…kyc.KybStatusChanged.v1`, `…kyc.SignatoryAuthorityChanged.v1`, `…kyc.ProfessionalCredentialChanged.v1`, `…kyc.GuardianshipChanged.v1`, `…kyc.NominationChanged.v1`, `…kyc.NomineeReleased.v1`, `…kyc.ConsentRecorded.v1`, `…kyc.ConsentWithdrawn.v1`, `…kyc.NoticeVersionPublished.v1`, `…kyc.RightsRequestChanged.v1`, `…iam.OnboardingInvitationActivated.v1` (P19 maps it to the partner webhook `in.lawdocs.int.OnboardingInvitationAccepted.v1` and to `TenantRegistered` for OH). Ecosystem mapping by `int`: `in.infrabyx.privacy.ConsentRecorded.v1` / `ConsentWithdrawn.v1` / `DataPrincipalRequest.v1` (Ecosystem Spec §6.14); `ProfessionalEmpanelled` consumed from OH9; `TenantProvisioned` consumed from OH (Appendix Y for LawDocs listing).

### 7.5 Jobs and workflows

`OnboardingDiscoveryWorkflow` (Temporal, 25-s budget); `KybMonthlyRefresh` (monthly; status, directors, GSTINs); `VerificationExpiry` (daily); `ProfessionalReverification` (daily scan; 12-month cycle); `NomineeReleaseWorkflow` (Temporal; waiting timer; cancellation signal on owner activity); `ComingOfAgeReminder` (daily); `ConsentPropagation` (on withdrawal; ≤ 1 h SLO with alert); `NoticeReconsentCampaign` (on material notice change; in-app at next sign-in); `AnonymousDraftPurge` (hourly; TTL 24 h); `InvitationExpiry` (hourly); `PartnerRequestExpiry` (daily); `MigratedUserReminder` (P00 FR-P00-68 schedule).

### 7.6 Error codes

`LD-IAM-001` invalid context · `LD-IAM-003` not a member · `LD-IAM-010` invitation expired · `LD-IAM-011` invitation addressed to another contact · `LD-IAM-020` SSO enforced for this domain · `LD-AUTH-001` code incorrect · `LD-AUTH-002` code expired · `LD-AUTH-003` too many attempts · `LD-AUTH-010` step-up required · `LD-AUTH-020` request blocked by abuse protection · `LD-KYC-001` verification method unavailable (flag off) · `LD-KYC-002` signature on QR/e-Aadhaar invalid · `LD-KYC-003` name match below threshold · `LD-KYC-004` provider unavailable — try another method · `LD-KYC-010` identifier format invalid · `LD-KYC-011` individual PAN used for organisation onboarding · `LD-KYC-012` organisation status blocks verification · `LD-KYC-020` discovery quota reached · `LD-KYC-030` age requirement not met · `LD-KYC-031` guardianship evidence required · `LD-KYC-040` signatory authority expired or exceeded · `LD-KYC-041` signatory not verified to L2 · `LD-KYC-050` professional credential not verified · `LD-KYC-060` nominee release cancelled by owner · `LD-KYC-070` consent required for this purpose · `LD-KYC-071` notice re-acceptance required · `LD-KYC-080` partner request lacks consentref or legal basis.

---

## 8. Integrations

| Port | Primary / alternatives | Failure behaviour and manual fallback |
|---|---|---|
| `SMS_PORT` | DLT-registered CPaaS (JioCX or other) primary + second CPaaS | Fail over; then email OTP; then voice OTP (when enabled) |
| `WHATSAPP_PORT` | Meta Cloud API direct; BSP alternate (R6 D-31) — authentication templates only | OFF by default; fall back to SMS |
| `EMAIL_PORT` | SES ap-south-1 / Brevo transactional | Retry; status shown |
| `SOCIAL_IDP_PORT` | Google, Microsoft OIDC | Offer OTP |
| `DIGILOCKER_PORT` | DigiLocker Requester direct (R6 D-18); aggregator fallback only with NeGD-compliant terms | Other L2 methods |
| `AADHAAR_OFFLINE_PORT` | Local verification of UIDAI signatures (Phase 1); Aadhaar App AVC integration (Phase 2) | Other L2 methods; flags OFF until verified (NN-38) |
| `COMPANY_DATA_PORT` | Licensed MCA-data vendor primary + secondary (R6 D-15) | Document-first fallback with reviewer |
| `GSTIN_PORT` | GSP (R6 D-16) | Manual GSTIN entry with certificate upload |
| `LEI_PORT` | GLEIF | Skip |
| `ENTITY_LOCKER_PORT` | NeGD Entity Locker (flag OFF) | Document upload |
| `PAN_PORT` | DigiLocker PAN; vendor with lawful-upstream warranty (flag OFF) | DSC or assisted L3 |
| `PRO_DIRECTORY_PORT` | OH9 via `int` | LOCAL desk |
| `CONSENT_MANAGER_PORT` | Registered consent managers (flag OFF) | Native consent |
| `BILLING_PORT` | OH8 (plan on wizard step if purchase chosen) | Continue on free/trial |

Each adapter carries a kill switch (NN-39), idempotency key and reconciliation record (NN-46), and non-prod routes to fakes (P00).

---

## 9. Settings and configuration (Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `iam.otp.ttl_seconds` | PLATFORM | int | 300 | `PLT_SECURITY_OFFICER` | Y |
| `iam.otp.max_sends_per_30min` | PLATFORM | int | 5 | `PLT_SECURITY_OFFICER` | Y |
| `iam.otp.whatsapp.enabled` | BRAND | flag | false | `PLT_SUPER_ADMIN` after template approval | Y |
| `iam.otp.voice.enabled` | BRAND | flag | false | `PLT_SUPER_ADMIN` | Y |
| `iam.login.methods` | BRAND / TENANT | set | OTP_MOBILE, OTP_EMAIL, PASSKEY, PASSWORD_MFA, GOOGLE, MICROSOFT, SSO | brand: `PLT_SUPER_ADMIN`; tenant may restrict | Y (brand) |
| `iam.sso.enforce_for_domain` | TENANT | bool | false | `ORG_OWNER`/`ORG_ADMIN` | Y |
| `iam.session.idle_timeout_minutes`, `iam.session.absolute_hours` (per role class) | PLATFORM (tenant may shorten) | int | per FR-P01-13 | `PLT_SECURITY_OFFICER`; tenant admin shorten | N (tenant shorten) |
| `iam.stepup.<action>` | PLATFORM (tenant may tighten) | acr + max_age | per FR-P01-04 | `PLT_SECURITY_OFFICER`; tenant admin tighten | Y |
| `iam.mfa.required_roles` | TENANT | set | ORG_OWNER, ORG_ADMIN, ORG_CLO, ORG_APPROVER, ORG_CHECKER | `ORG_OWNER` (add only) | Y |
| `iam.guest.invite_ttl_days` | TENANT | int (1–30) | 14 | `ORG_ADMIN`; individual per invite | N |
| `iam.anonymous_draft.ttl_hours` | PLATFORM | int (1–72) | 24 | `PLT_DPO` | Y |
| `iam.age_assurance.mode` | PLATFORM | enum | DECLARATION (DIGILOCKER_TOKEN from 13 May 2027 [VERIFY]) | `PLT_DPO` | Y |
| `iam.nominee.max` | PLATFORM | int | 3 | `PLT_SUPER_ADMIN` | Y |
| `iam.nominee.release_waiting_days` | USER (bounded 7–90) | int | 30 | owner | N |
| `iam.nominee.access_days` | PLATFORM | int | 180 | `PLT_DPO` | Y |
| `kyc.level_validity_months` | PLATFORM | int | 24 | `PLT_DPO` | Y |
| `kyc.min_level.<role>` | TENANT (≥ platform floor) | enum L0–L3 | ORG_APPROVER: L2; others L1 | `ORG_OWNER` | Y |
| `kyc.name_match.threshold.<purpose>` | PLATFORM | int | 85 signatory / 80 badge | `PLT_SECURITY_OFFICER` | Y |
| `kyc.ovse.qr.enabled` | PLATFORM | flag (verify-gated) | false | `PLT_SUPER_ADMIN` + `PLT_DPO` | Y |
| `kyc.ovse.avc.enabled` | PLATFORM | flag (verify-gated) | false | same | Y |
| `kyc.digilocker.enabled` | PLATFORM | flag | false until Requester onboarding complete | same | Y |
| `kyc.digilocker.retain_copy.enabled` | PLATFORM | flag (verify-gated, NeGD) | false | same | Y |
| `kyc.entity_locker.enabled` | PLATFORM | flag (verify-gated) | false | same | Y |
| `kyc.pan.vendor.enabled` | PLATFORM | flag (warranty-gated) | false | same | Y |
| `kyc.discovery.quota.<tier>` | PLATFORM / PLAN | int | 3 anon/day; 10 unverified; 100 verified/month | `PLT_SUPER_ADMIN` | Y |
| `kyc.kyb.review_sla_hours` | PLATFORM | int | 8 working hours | `OPS_DELIVERY_LEAD` | N |
| `kyc.kyb.refresh_cadence` | PLATFORM | enum | MONTHLY | `PLT_SUPER_ADMIN` | Y |
| `kyc.professional.verification_desk` | PLATFORM | enum OH9/LOCAL | OH9 (LOCAL until OH9 live) | `PLT_SUPER_ADMIN` | Y |
| `kyc.professional.reverify_months` | PLATFORM | int | 12 | `PLT_SUPER_ADMIN` | Y |
| `kyc.consent_manager.enabled` | PLATFORM | flag (verify-gated) | false | `PLT_DPO` | Y |
| `kyc.consent.withdrawal_propagation_minutes` | PLATFORM | int | 60 | locked | — |
| `kyc.rights.internal_sla_days` | PLATFORM | int (≤ 90) | 30 | `PLT_DPO` | Y |
| `kyc.grievance.resolve_days` | BRAND | int | 7 [VERIFY] | `PLT_GRIEVANCE_OFFICER` (shorten only) | Y |

---

## 10. Security, privacy and audit

- **Threats (Appendix P §P.2):** account takeover through OTP interception or SIM swap (mitigations: no SMS as second factor for privileged roles, passkeys, step-up, new-device alerts); OTP bombing and SMS pumping (rate limits, +91 allow-list, budgets); social-login account linking takeover (OTP on matching contact before link); guest-link forwarding (OTP to the invited contact; device binding); fake authority evidence (reviewer maker-checker, director match, re-verification, audit of reviewer decisions); professional impersonation (credential desk, annual re-checks, suspension within 1 hour); nominee fraud (L2 nominee, maker-checker evidence review at AAL3, waiting period with owner cancellation); KYB scraping abuse (quotas, masking for anonymous users).
- **Data classes:** Aadhaar attributes and DigiLocker results → `KYC_ARTEFACT` in `ld_sealed`; PAN → `SPI` (enc + bidx + masked); death/incapacity and guardianship evidence → sealed; consents → `PII` with proof retention.
- **NN tests:** NN-03 (no Aadhaar login), NN-04 (no Aadhaar number stored; QR payload discarded; masking), NN-05 (no closed-source adapters), NN-06 (no partner eSign API), NN-13 (no AI submits verifications or consents), NN-19 (OH receives only consented contacts and aggregates), NN-20 (no "verified lawyer"/"government-approved" copy), NN-21 (Rule-36 fields only), NN-23 (Consumer Help separation), NN-24 (`int` only), NN-26 (consent, notices, rights, minors), NN-28 (accessible authentication), NN-32 (no OTP/PAN/Aadhaar in logs), NN-34 (DLT, single invitation), NN-38 (verify-gated flags), NN-42 (DigiLocker URI default), NN-44 (mobile token storage), NN-50 (equal-weight choices, no pre-ticked consent), NN-11 (export map).
- **Retention:** verification results 8 years; attributes only for the purpose; Aadhaar attributes deleted on revocation; DigiLocker URIs until purpose ends; consents as proof for life + 8 years; OTP hashes 5 minutes; invitation tokens 1 year (hash only).
- **Audit:** every sign-in (success and failure), factor change, step-up, verification run, KYB fact confirmation and edit, authority decision, credential decision, consent change, notice publication, nominee step, partner request and provisioning acknowledgement.
- **Export map (NN-11):** `iam.persons` (own profile) → `01 My Profile and IDs (masked)/Profile.xlsx` or `01 Company Profile/People.xlsx`; `kyc.verifications` → `01 My Profile and IDs (masked)/Verification Records.xlsx` (results and sources; no Aadhaar number); `kyc.kyb_facts` → `01 Company Profile/Organisation Details and Sources.xlsx`; `kyc.signatory_authorities` → `01 Company Profile/Authorised Signatories/` (register + evidence documents); `kyc.consents` + notices → `99 System Data (CSV and JSON)/Consents and Notices/`; `kyc.nominations`, `kyc.guardianships` → `03 Family and Succession/Nominees and Wards.xlsx` (individuals); `kyc.professional_credentials` → PRO_FIRM `01 Company Profile/Professional Credentials/`.

---

## 11. AI touchpoints and guardrails

- **Document-first KYB and credential extraction** uses P05 document intelligence (Bedrock India) once live: extracted fields are suggestions with confidence; a person confirms; AI never sets a verification result (NN-13, NN-43).
- **Vidhi help in onboarding** (P09 runtime): answers "what is an authorised signatory?" from the glossary and help centre only, with sources; never asks for or accepts an Aadhaar number in chat (the chat input masks Aadhaar patterns before sending — NN-04).
- **No AI** in OTP, step-up, authority decisions, nominee release or consent capture. Consent to `AI_ASSISTANCE` is asked at first Vidhi use, not bundled with sign-up (NN-26).
- **Evaluation:** prompt-injection tests on uploaded authority letters (instructions inside a document never change the reviewer workflow).

---

## 12. Acceptance criteria (`tests/acceptance/p01/*.feature`)

```gherkin
@P01-AT-01 @NN-03
Scenario: Aadhaar is not offered as a way to sign in
  Given the sign-in page in every launch language
  When a visitor looks for sign-in options
  Then the options are mobile OTP, email OTP, passkey, password with MFA, Google, Microsoft and work SSO
  And no option, route or Keycloak flow authenticates with Aadhaar
  And account recovery never asks for an Aadhaar number

@P01-AT-02
Scenario: First draft in under two minutes
  Given a visitor on the Rent agreement page
  When they tap "Draft free", answer 9 questions and tap "Save and download"
  And enter their mobile number and the 6-digit code
  Then a PERSONAL workspace exists, the draft is in Legal Vault › Drafts
  And the elapsed time at p75 in the usability panel is at most 120 seconds
  And no identity verification or payment was requested

@P01-AT-03 @NN-04
Scenario: Aadhaar offline verification stores no Aadhaar number
  Given flag "kyc.ovse.qr.enabled" is ON after verification
  And user "Kavya" scans the secure QR of her e-Aadhaar for purpose SIGNATORY_VERIFICATION
  When the UIDAI signature validates
  Then her identity level becomes L2 with method AADHAAR_OFFLINE_QR
  And the stored record contains name, 18+ flag, signature evidence and, only where the purpose requires display, the last four digits
  And no table, object, log or trace contains the full number, the QR payload or the image

@P01-AT-04 @NN-38
Scenario: Aadhaar Verifiable Credential stays off until OVSE registration is recorded
  Given verification backlog item "V-012" (Appendix W) is OPEN
  When a user opens the verification centre
  Then the Aadhaar App option is not shown
  And an attempt to enable "kyc.ovse.avc.enabled" fails with "LD-CORE-016"

@P01-AT-05 @NN-42
Scenario: DigiLocker PAN is recorded by reference
  Given "Arjun" consents to fetch his PAN from DigiLocker for purpose PROFILE_BADGE
  When the issuer-signed PAN is received and the name matches at 92
  Then LawDocs stores the URI, issuer, verification result, name-match score and time
  And no copy of the PAN document is stored unless he chooses "Save a copy" and that flag is ON

@P01-AT-06 @NN-05
Scenario: Closed data sources cannot be configured
  Given a connector manifest declaring an endpoint of type "CKYC_SEARCH" or "CIC_REPORT_PULL"
  When CI runs
  Then the check "NN-05_no_closed_source_adapters" fails naming the manifest

@P01-AT-07
Scenario: Company discovered from one GSTIN with provenance
  Given "Neha" enters GSTIN "07AAACA1234A1ZM" (synthetic; company PAN with fourth character C and a valid check character, so it passes FR-P01-26 local validation) and accepts the lookup notice
  When discovery finishes
  Then the profile card shows legal name, constitution, State, CIN and directors with a source badge on each field
  And a conflict card appears where the MCA name differs from the GST legal name
  And p95 discovery time in staging is at most 40 seconds

@P01-AT-08
Scenario: Struck-off company cannot be badged as verified
  Given the company-data provider returns status "Strike Off" for the CIN
  When the owner confirms the profile
  Then the "Verified organisation" badge is not granted and the reason is shown in plain words
  And drafting remains available

@P01-AT-09
Scenario: A listed director becomes signatory automatically
  Given "Rahul" is listed as a director of "Alpha Pvt Ltd" in MCA data
  When Rahul reaches L2 through DigiLocker PAN with a name-match score above 85
  Then his signatory authority is VERIFIED_AUTO with basis "MCA_DIRECTOR"

@P01-AT-10 @NN-18
Scenario: Authority by board resolution needs two reviewers
  Given "Priya" is not a director and uploads a certified board resolution
  When OPS_ONBOARDING "Sam" approves the evidence
  Then the authority is not active until a different reviewer checks it
  And Sam cannot perform the check

@P01-AT-11
Scenario: Signing as the entity is blocked beyond the recorded limit
  Given Priya's authority allows agreements up to ₹10,00,000
  When she tries to sign an agreement worth ₹25,00,000 as the entity
  Then signing as the entity is refused with "LD-KYC-040" and the DoA route to a higher approver is offered

@P01-AT-12 @NN-21
Scenario: Advocate application captures Rule 36 fields only for any public profile
  Given an advocate application with enrolment number, State Bar Council and COP
  When the profile preview is generated
  Then only Rule 36 fields appear
  And there is no photo, rating, review, fee, badge or "book now" element

@P01-AT-13 @NN-20
Scenario: Credential badge wording makes no quality claim
  Given a professional credential VERIFIED on 2 Nov 2026
  Then the badge reads "Credentials checked by LawDocs on 2 Nov 2026: enrolment number and certificate of practice"
  And the strings "verified lawyer" and "top lawyer" do not appear anywhere in the product

@P01-AT-14 @NN-34
Scenario: Counterparty receives one invitation and can stop reminders
  Given "Meera" invites "Ravi" to sign by email
  Then Ravi receives exactly one invitation and reminders only per Meera's schedule
  When Ravi chooses "Stop reminders"
  Then no further reminders are sent and no automated call is ever placed

@P01-AT-15
Scenario: Guest says "This is not me"
  Given an invitation addressed to the wrong person
  When the recipient taps "This is not me" before entering an OTP
  Then the invitation is revoked, the initiator is notified, and no document content was displayed

@P01-AT-16 @NN-26
Scenario: A minor cannot create an account
  Given a visitor declares a date of birth showing age 16
  When they try to sign up
  Then account creation stops and they are told to ask a parent or guardian
  And no personal data beyond the declaration is retained

@P01-AT-17
Scenario: Nominee release is cancelled by the owner's sign-in
  Given nominee "Asha" has requested release with a death certificate and the evidence was verified by two reviewers
  And the waiting period of 30 days has started
  When the owner signs in on day 4
  Then the release moves to CANCELLED_BY_OWNER with "LD-KYC-060", the owner is alerted, and Asha receives no access

@P01-AT-18 @NN-26
Scenario: Consent withdrawal propagates within one hour
  Given "Karan" consented to MARKETING_WHATSAPP and the consent was shared with the Operations Hub CRM
  When he withdraws it in the privacy centre
  Then LawDocs stops WhatsApp marketing at once
  And "in.infrabyx.privacy.ConsentWithdrawn.v1" reaches every recipient within 60 minutes

@P01-AT-19 @NN-50
Scenario: No pre-ticked consents and equal choices
  Given the sign-up sheet and the cookie banner
  Then every optional consent is unticked
  And "Reject" and "Accept" have equal visual weight and the same number of taps

@P01-AT-20 @NN-24 @NN-17
Scenario: Onboarding on someone else's initiative gives the requester no tenant access
  Given a partner CA firm submits an onboarding batch row for "Gamma LLP" with an authority attestation
  And the Operations Hub emits TenantProvisioned for "Delta Pvt Ltd" requested through Finbyx
  When each signatory opens the invitation, verifies by OTP, confirms the pre-filled fields and accepts the terms
  Then each tenant becomes ACTIVE and the requester receives status ACTIVATED only
  And no partner, Finbyx or Operations Hub principal holds any membership or grant in either tenant

@P01-AT-21 @NN-06
Scenario: Partners cannot use LawDocs' eSign arrangement for their own documents
  Given a partner client with scope "onboarding.request:write"
  When it calls any signing endpoint for a document not owned by a LawDocs tenant
  Then the request is refused and the attempt is logged

@P01-AT-22 @NN-23
Scenario: Consumer Help account does not expose LawDocs profile data
  Given "Sunil" has a LawDocs account at L2
  When he signs up to [Consumer Help Brand] using "Use my LawDocs sign-in"
  Then the brand's notice is shown and its own consents are captured
  And his LawDocs verification result is not copied unless he consents to that copy

@P01-AT-23 @NN-28
Scenario: Verification has a non-visual alternative
  Given a screen-reader user on the verification centre
  When they choose "Assisted verification by phone or video"
  Then they can book a session without scanning a QR code or passing a liveness check

@P01-AT-24 @NN-32
Scenario: OTPs and identifiers never reach logs
  Given 1,000 OTP sends, verifications and discovery runs in staging
  When logs and traces are scanned
  Then no OTP value, full PAN, Aadhaar number or mobile number appears

@P01-AT-25
Scenario: Migrated user activates their old account
  Given a P00-migrated person with unverified email "old@example.com"
  When they sign in with an email OTP to that address
  Then the contact is marked verified, the migrated workspace is linked and "What moved from old LawDocs" is shown
```

---

## 13. Exit gate, deliverables and open items

**Checklist**

- [ ] Realms, clients, Keycloakify themes (LawDocs + Consumer Help brand); BFF sessions; mobile token handling.
- [ ] All login methods live; passkeys promoted; step-up working; SSO + SCIM tested with Entra ID and Google Workspace.
- [ ] Ladder L0–L3 with DigiLocker (Requester onboarding complete or flag OFF with OI), Aadhaar offline Phase 1 (flag gated), DSC, assisted L3.
- [ ] KYB discovery with one vendor + GSP + GLEIF; document-first fallback; review queue with maker-checker.
- [ ] Signatory authorities with limits read by P02 DoA.
- [ ] Professional applications with OH9 or LOCAL desk; Rule-36 preview.
- [ ] Guests, wards, nominees, consent ledger, notice versions, privacy centre, rights requests.
- [ ] Activation flow for P19 partner invitations and OH-provisioned tenants (behind the Appendix Y gate for `TenantProvisioned`).
- [ ] Individual ≤ 2 min and company ≤ 10 min journeys measured in moderated tests (10 participants each, including two screen-reader users and two Hindi-first users).
- [ ] NN tests in the header ACTIVE; acceptance scenarios pass; settings, help keys, error codes, events and export-map entries registered.
- [ ] P00 wave activation of migrated users done.

**Demo script.** Draft and save a rent agreement in under two minutes on a phone; add a passkey; verify by DigiLocker PAN; set up "Alpha Pvt Ltd" from a GSTIN, see provenance and a conflict card; Rahul becomes signatory automatically; Priya's board-resolution authority reviewed by two people; an advocate applies and sees the Rule-36-only preview; a guest opens an invitation and says "not me"; a nominee release cancelled by the owner's sign-in; marketing consent withdrawn and propagated; a partner-batch invitation activated in four taps with no partner access.

**Open items**

| ID | Item | Owner |
|---|---|---|
| OI-P01-01 | DLT principal-entity registration, headers and OTP templates for the operating entity | [OWNER] |
| OI-P01-02 | UIDAI secure-QR verification specification and OVSE Reg 13A registration (fees, documents, Class 3 certificate) | [OWNER] + [COUNSEL] |
| OI-P01-03 | NeGD written confirmation on user-directed saving of DigiLocker documents; Requester onboarding | [OWNER] with NeGD |
| OI-P01-04 | Entity Locker Requester API eligibility and terms | Tech lead |
| OI-P01-05 | KYB vendor contracts with lawful-sourcing warranties (primary + secondary) and prices | [OWNER] |
| OI-P01-06 | Vendor PAN API warranty (or decision to rely on DigiLocker PAN only) | [OWNER] + [COUNSEL] |
| OI-P01-07 | Professional verification sources (State Bar Council rolls, ICAI/ICSI directories) and their terms; COP rules citation | [COUNSEL] |
| OI-P01-08 | OH9 readiness for LawDocs professional applications; interim LOCAL desk | Integration Spec owner |
| OI-P01-09 | Acceptable guardianship and incapacity evidence under DPDP Rules 10–11 | [COUNSEL] |
| OI-P01-10 | Nominee release wording vis-à-vis succession law | [COUNSEL] |
| OI-P01-11 | Consumer Help: separate fiduciary account-sharing model | [COUNSEL] |
| OI-P01-12 | Cross-product customer sign-in by token exchange (not in Appendix Y rev. of 25 Oct 2026); confirm `PARTNER_ONBOARDING_PREFILL` purpose and `TenantRegistered` acceptance | Integration Spec owner / pack lead |
| OI-P01-13 | DigiLocker as a sign-in option: kept out (NN-03); revisit only by ADR + counsel | [OWNER] |
| OI-P01-14 | Current IT Rules grievance timelines and E-Commerce Rules sub-rules | [COUNSEL] |
