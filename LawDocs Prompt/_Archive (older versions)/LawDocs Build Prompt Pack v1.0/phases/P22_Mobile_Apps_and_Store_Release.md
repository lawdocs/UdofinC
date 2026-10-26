# Phase P22 — Mobile Apps (iOS/Android) and Store Release

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P01 (OIDC realms, OTP, passkeys, consent ledger, Aadhaar offline verification flows), P02 (workspaces, roles, maker-checker), P04 (vault APIs, Object Lock, hashes), P05 (OCR, type copy, translation renditions), P06/P07 (questionnaires, Drafting Studio, redlines, deal rooms, messaging), P08 (eligibility gate, eStamp, ESP adapters, evidence packs), P09 (Vidhi runtime), P11/P12 (case and trademark status), P15 (Consumer Help cases — v2), P16/P17 (catalogue, checkout, entitlements), P19 (gateway, webhooks), P20 (export jobs), P21 (`hlp` content, glossary, tours, tutorials). External: Apple App Store Connect, Google Play Console, Expo Application Services (EAS Build, Submit, Update), APNs/FCM, Play Integrity API, App Attest, Razorpay React Native SDK, the eSign aggregator chosen in P08.
> **Sequencing:** Wave 2 ships v1 of the LawDocs app (individuals and companies: vault, scan, share import, drafting, negotiation, eSign/eStamp, approvals, case/TM status, Vidhi chat, marketplace purchase, notifications). Wave 3 ships v2: the `[Consumer Help Brand]` flavour, Vidhi voice in all D-07 languages, practitioner-lite space for `PRO_*`, offline Vidhi help. The BFF contract (`/m/v1`) freezes at the end of sprint 2; device-trust and offline-cache designs pass a security review (P23) before any store submission.
> **Binding appendices:** U (accessibility), F (instrument eligibility), K (`LD-EXPORT-1.0`), M (marketplace rules), N (store listing copy, video plan), R (settings), D (roles), H (Vidhi agents), W (open items), Y (ecosystem change request).
> **Requirements covered:** R-008, R-010, R-011, R-012, R-013, R-017, R-019, R-025, R-030, R-034, R-043, R-044, R-045, R-061, R-064 (approvals), R-068, R-077, R-078, R-083, R-084 (status and deep links; v2).
> **Decisions applied:** D-01, D-06, D-07, D-11, D-12, D-14, D-15 · **Challenges applied:** CH-01, CH-02, CH-11, CH-12, CH-13, CH-15, CH-28, CH-30 · **Non-negotiables tested:** NN-01, NN-03, NN-04, NN-06, NN-07, NN-08, NN-09, NN-11, NN-13, NN-14, NN-18, NN-20, NN-22, NN-23, NN-26, NN-28, NN-32, NN-34, NN-37, NN-44, NN-46, NN-48, NN-50
> **Estimated effort:** 9 two-week sprints (v1 6, v2 3), squad of 8 (3 React Native engineers, 1 native-module engineer (iOS/Android), 1 back-end engineer for `mob` and the BFF, 1 mobile security engineer (shared with P23), 1 product designer with accessibility specialism, 1 QA/device-lab engineer).

---

## 1. Objective and business outcome

The owner wants users to keep LawDocs "the way people use DigiLocker": always on the phone, used to prepare, negotiate, sign, amend and preserve agreements (R-011, R-017). LegalKart's app is a consultation wallet; LawDocs' app is the Legal Vault plus signing and drafting in the pocket (R1 §3.7). The phone is also where most evidence is born: photographs of stamp papers, handwritten receipts, WhatsApp chats and screenshots (CH-28).

**Outcomes and KPIs**

| KPI | Target |
|---|---|
| First document from install to signed (template lane, Aadhaar eSign, eligible instrument) | ≤ 5 minutes median; ≤ 3 taps from home to start |
| Open a pinned offline document | ≤ 1 s from unlock, no network |
| Signing-invite link → signer reviewing the document (guest, no app) | ≤ 2 taps and one OTP |
| Crash-free sessions (production) | ≥ 99.7% |
| ANR rate (Android) | < 0.47% (below Play "bad behaviour" threshold [VERIFY current threshold]) |
| Cold start to interactive | < 2.5 s mid-range Android; < 4.0 s low-end |
| Download size | ≤ 35 MB Android per-device APK; ≤ 50 MB iOS thinned |
| Parity matrix coverage (every web capability has a mobile status) | 100%, CI-enforced |
| Accessibility: five critical journeys pass manual VoiceOver and TalkBack scripts | 100% per release |
| PII found in crash or analytics payloads in the monthly sample audit | 0 |

**Done** means an individual can scan a stamp paper, draft a rent agreement in Hindi, negotiate one clause in chat, eStamp and eSign, and find the signed copy offline a year later; a company checker can approve a contract from a push notification with biometric step-up; a counterparty can sign from a WhatsApp or RCS link without installing anything.

## 2. Scope (in / out)

**In scope**

1. `apps/mobile` (Expo React Native, New Architecture, Hermes, Expo Router, TypeScript strict), one codebase, two brand flavours: **LawDocs** and **`[Consumer Help Brand]`** (v2).
2. Mobile BFF `/m/v1` in the `mob` module; device registry, push tokens, deep-link tokens, app-version policy, OTA release records.
3. Features per the parity matrix (§6.1): vault with encrypted offline cache; camera scan with edge detection and OCR; share-sheet import including WhatsApp chat exports; drafting (template lane and Vidhi lane); negotiation chat and change review; eSign and eStamp flows; maker-checker approvals; case, hearing and trademark status with alerts; Vidhi chat and voice in D-07 languages; marketplace browse and purchase; notifications; help panel, "i" popovers, tours; accessibility preferences; account and data export requests.
4. Device trust, biometric unlock, integrity attestation, certificate pinning, screen protection (NN-44).
5. Store compliance: purchase-method classification for Apple and Google, listings and ASO, App Privacy labels, privacy manifest, Google Play Data safety form, account deletion, review notes and demo accounts.
6. Release trains with EAS, OTA update policy, crash and analytics with PII scrubbing.

**Out of scope (owner)**

| Item | Owner / channel |
|---|---|
| Content Studio, console administration, rule and template authoring | Web (`apps/console`), P03/P06/P21 |
| Delivery Console for `OPS_*` roles | Responsive web (`apps/delivery`) in v1; native "ops approvals" only if Appendix X requests it |
| Bulk folder import (R-024) and BYO storage set-up | Web (P04, P20); mobile can trigger and download exports |
| DSC (USB token) signing | Web/desktop (P08); mobile shows DSC tasks as "Sign on computer" |
| Client credential vault reveal (`cvl`) | Web only in v1 (NN-16 controls); mobile shows that a request exists |
| Redline authoring of whole documents | Web; mobile reviews changes, accepts/rejects per change and comments |
| FinLegal Academy course consumption | `trainings.lawdocs.in` (D-16); not sold or played in the app |
| Consumer Help case management (`OPS_CONSUMER_CASE_MANAGER`) | Web (P15) |

## 3. Personas and permissions touched

| Role | Mobile v1 capabilities (Appendix D governs) |
|---|---|
| `IND_OWNER` | Full personal workspace: vault, scan, import, drafting, negotiation, sign, stamp, cases, TM, Vidhi, marketplace, export request. |
| `IND_FAMILY_MEMBER`, `IND_DELEGATE` | Scoped folders and tasks as granted; no sharing outside grant. |
| `IND_GUARDIAN` | Acts for the ward's workspace with the guardian banner. |
| `IND_NOMINEE` | Time-locked access screen only (claim flow per P04); no content until unlocked. |
| `ORG_LEGAL_MAKER`, `ORG_MEMBER` | Raise requests, draft from templates, upload, negotiate, track matters. |
| `ORG_CHECKER`, `ORG_APPROVER`, `ORG_CLO`, `ORG_DEPT_HEAD` | Approval inbox with biometric step-up; legal calendar; dashboards (read). |
| `ORG_DIRECTOR`, `ORG_KMP`, `ORG_BOARD_OBSERVER` | Board and resolution read; sign resolutions where eligible; Vidhi briefings. |
| `ORG_ADMIN` | Read-only admin summary; user invites; device revocation for company users; settings remain on web. |
| `CP_GUEST` | Universal-link signing and negotiation without an app account; optional upgrade to account. |
| `PRO_*` | v1: responsive web; v2: practitioner-lite space (engagement inbox, deliverable upload, messages). |
| `AGT_*` | No direct mobile surface; their outputs appear as labelled drafts and tasks. |

## 4. Functional requirements

### 4A. App architecture, workspaces and brand flavours

- **FR-P22-01** One Expo app with flavours set in `app.config.ts` from `BRAND`: bundle and application IDs (`in.lawdocs.app` [VERIFY final IDs; OWNER]), name, icon, splash, tokens from `packages/tokens/brands/<brand>.json`, associated domains, push credentials, store listing locale set, legal-entity profile. Builds are reproducible from EAS profiles `development`, `preview`, `production` × flavour.
- **FR-P22-02** The Consumer Help flavour compiles only the route groups `(chp)`, `(vault)` (Consumer Help tenant only), `(messages)`, `(marketplace)` (Consumer Help services), `(help)`, `(account)`; a build-time allow-list fails the build if any LawDocs company, LDC, Finbyx, Udofin or Equator route or API client is bundled (NN-23). It uses its own API audience and brand header; it cannot log in to a LawDocs tenant.
- **FR-P22-03** After login the app reads `GET /m/v1/me` and renders the **workspace switcher** (Personal and each Company workspace the user belongs to, P02). Each workspace has its own tab bar defined in Expo Router groups. Defaults — Personal: Home · Vault · Create · Activity · Me; Company: Home · Inbox · Contracts · Matters · More; Consumer Help flavour (FR-P22-02, v2): Home · My cases · Evidence · Vehicles · Me; guests (`CP_GUEST`) get no tab bar (single task). Home, Inbox (Company) and the last tab are fixed positions; the two Company middle slots take the tenant default `mob.bottom_bar.items` (role-appropriate rail items available on mobile, e.g., Sign and Board for checkers, approvers and directors; Appendix C §C.16 R-3) and otherwise follow this default. Tab order is user-customisable within the group (USER setting `mob.nav.tab_order`). These are the only tab sets; Appendix C §C.4.18 mirrors them. Switching workspace clears in-memory caches; the SQLite cache is partitioned by `(tenant_id, legal_entity_id, workspace)` (NN-01).
- **FR-P22-04** Navigation and click budgets: scan to vault ≤ 3 taps; start a document ≤ 3 taps; approve a pending item from push ≤ 2 taps plus biometric; find a document by search ≤ 2 taps plus query; open Vidhi from anywhere ≤ 1 tap (floating action on Home and in the document viewer).
- **FR-P22-05** Shared logic: forms, validation, money formatting (`decimal.js`), eligibility labels and help keys come from shared packages (`packages/contracts`, `packages/i18n`, `packages/a11y`, `packages/ui` native primitives); no business rule is re-implemented on the device — the server decides eligibility, fees, entitlements and permissions.

### 4B. Mobile BFF (`/m/v1`, `mob` module)

- **FR-P22-06** The BFF aggregates and shapes responses for mobile screens (home feed, vault folder page, document detail with renditions, approval inbox, case card), paginates with cursors, and strips fields not needed on mobile. It calls module APIs in-process (modular monolith); it never reads another module's tables directly.
- **FR-P22-07** Versioning: every request sends `LD-App-Version`, `LD-Platform`, `LD-Brand` and the OTA `runtimeVersion`. The BFF enforces `mob.version.min_supported` per platform: below it, `LD-MOB-001 Update required` with a store link; between min and recommended, a dismissible update banner. Feature flags and kill switches (NN-39) are delivered in `GET /m/v1/config` (signed payload, cached 15 min).
- **FR-P22-08** Delta sync: `GET /m/v1/sync/changes?cursor=` returns up to 500 changes per page for cached entity types; cursors older than 30 days force a full resync. Mutations from the outbox carry `Idempotency-Key` (UUIDv7) and `If-Match`; `412` → "needs review", `409/422` → rejected with the localised problem-detail and help key; network/`5xx`/`429` → backoff from 2 s to 5 min, abandoned after 20 attempts or 72 h with a user prompt (NN-46).
- **FR-P22-09** Real-time: WebSocket `/m/v1/realtime` for chat and signing status, authorised per subscription; push fallback when the socket is closed.

### 4C. Identity, device trust and biometric unlock (NN-03, NN-44)

- **FR-P22-10** Authentication: OIDC Authorization Code + PKCE through the system browser (`ASWebAuthenticationSession` / Custom Tabs); no embedded WebView login. Methods from P01: mobile OTP (DLT SMS, WhatsApp/RCS fallback — NN-34), email magic link, passkeys, password + MFA, enterprise SSO. **Aadhaar is never a login method** (NN-03, CH-01); Aadhaar offline verification and DigiLocker appear only inside KYC flows (P01).
- **FR-P22-11** Tokens: access token 10 min; refresh token opaque, rotating, sender-constrained with DPoP (RFC 9449) to a device-bound key (Keycloak DPoP support [VERIFY version]); stored only in `expo-secure-store` with `WHEN_UNLOCKED_THIS_DEVICE_ONLY` (iOS) and Keystore-backed encryption (Android); never in AsyncStorage, SQLite or logs.
- **FR-P22-12** Device binding: on first login the app generates a P-256 key pair in hardware (Secure Enclave; StrongBox or TEE Keystore) and registers the public key with an attestation (`POST /m/v1/devices`), creating `mob.devices`. Limits: 3 active devices for individuals, 2 for company users (TENANT setting within 1–5). A new device beyond the limit requires OTP and choosing a device to unbind. Every bind/unbind is audited and notified to the user's other devices and by email.
- **FR-P22-13** Integrity: Android Play Integrity (`MEETS_DEVICE_INTEGRITY` → pass; basic only → degraded; none → fail; `PLAY_RECOGNIZED` required for store builds); iOS App Attest on registration and every 24 h. Local signals (root/jailbreak paths, hooking frameworks, debugger, emulator) are reported but never decide alone; the server computes `device.integrity`. Effects: `fail` → restricted mode (read non-confidential metadata; cannot open documents, sign, pay, approve or export; banner explains and offers web); `degraded` → no offline cache, signing and approvals need OTP step-up. Attestation provider outages degrade, never fail, and alert `PLT_SRE`.
- **FR-P22-14** Biometric unlock (device-local only, NN-44): opt-in after first login via `expo-local-authentication`; strong biometrics only (Face ID/Touch ID; Android BiometricPrompt Class 3); the refresh-token wrapping key requires user authentication. LawDocs never receives or stores biometric data. App lock after `mob.lock.background_minutes` (individual 5, company 2; TENANT range 1–15). Five failed biometric attempts force OTP re-login. Enrolment change (new fingerprint/face) invalidates the wrapping key and forces OTP re-login. Device passcode is not accepted for step-up on approvals, signing or payments (OTP fallback).
- **FR-P22-15** Step-up: approvals (NN-18), signing launch, payments, export download, sharing outside the tenant and device unbinding require biometric or OTP step-up within the last 60 s (`mob.stepup.window_seconds`).
- **FR-P22-16** Sessions and remote revoke: "Devices" screen lists bound devices with last seen and integrity; the user (and `ORG_ADMIN` for company workspaces) can revoke; revoke invalidates tokens and triggers cache wipe on next contact (§4E).
- **FR-P22-17** Certificate pinning: SPKI SHA-256 pins for `api.lawdocs.in` with two backup pins; pin set updatable only through a signed config payload; pin failure blocks network calls and reports `PIN_VALIDATION_FAILED` without payload.

### 4D. Screen protection and device hygiene (NN-44, NN-32)

- **FR-P22-18** Protected screens: document viewer, signed-file viewer, evidence packs, matters marked confidential, KYC screens, payment confirmation with identifiers, approval detail. Android: `FLAG_SECURE` per screen (blocks screenshots, recording, casting; blanks Recents). iOS: blur/brand overlay on `sceneWillResignActive`; content hidden when `UIScreen.isCaptured`; screenshot notification → audit event `in.lawdocs.mob.ScreenCaptureDetected.v1` and a gentle notice. Tenants may allow screenshots for non-confidential classes (`mob.screen.allow_capture_classes`, TENANT, default none).
- **FR-P22-19** Watermark on protected document views: user name, masked mobile, timestamp, document reference (`LD-AGR-…`).
- **FR-P22-20** No sensitive data in device logs (`console` stripped in production builds; native logs filtered), notifications (FR-P22-70), app switcher snapshots, crash reports (§4U) or the clipboard (copy of document text from protected screens disabled; copied OTPs never auto-read beyond the platform's SMS retriever/one-time-code autofill).
- **FR-P22-21** Keyboard: secure text entry on secret fields; personalised-learning disabled for sensitive inputs (`autoCorrect=false`, `importantForAutofill` set appropriately).

### 4E. Vault and encrypted offline cache

- **FR-P22-22** Vault browsing mirrors P04: folders as views over canonical IDs (NN-12), search (server, with offline search over cached metadata), filters (type, party, date, status, tag), sort, document detail with versions, renditions (OCR text, type copy, translation — each labelled with confidence, NN-09 rule), sharing (selective, time-bound links per P04), and legal-hold badges.
- **FR-P22-23** Offline cache: SQLCipher-encrypted `expo-sqlite` for metadata (key in SecureStore); files encrypted at rest with per-file AES-256-GCM keys wrapped by a device-bound Keystore/Secure Enclave key (NN-44). The user pins documents or folders "Available offline"; recent documents are cached automatically only if `mob.offline.auto_cache_recent` (TENANT, default ON for individuals, OFF for companies). Size cap `mob.offline.max_mb` (default 500, LRU).
- **FR-P22-24** Never cached: credential-vault entries (`cvl`), unapproved AI drafts of another user, documents under a tenant policy "online only", sealed matters, KYC artefacts, payment instruments. Company tenants may disable offline cache entirely (`mob.offline.enabled`, TENANT).
- **FR-P22-25** Originals are immutable (NN-09): the device never edits a cached original; edits create new versions server-side. Conflict rules: metadata server-wins with a notice; drafts never auto-merge (user chooses); uploads queued offline keep their capture-time hash.
- **FR-P22-26** Remote wipe: on revoke, integrity `fail`, or 30 days without contact (`mob.offline.max_days_without_contact`), the app deletes the wrapped keys first (crypto-shred), then files and the database, and logs the wipe on next contact.
- **FR-P22-27** Downloads: "Save a copy" to the device or Files app is a share outside the tenant: step-up, audit, tenant policy (`mob.export.device_save_allowed`, TENANT, default ON for individuals, OFF for companies); exported files carry the original hash in the filename suffix of the evidence copy.
- **FR-P22-28** Data portability (NN-11): the Me tab offers "Export everything" which starts the P20 `LD-EXPORT-1.0` job; the ZIP is downloaded over Wi-Fi by default or sent to a connected BYO storage target; mobile-originated records (devices, push preferences, capture metadata) are included (§13).

### 4F. Camera scan, OCR and Aadhaar masking

- **FR-P22-29** Capture through the platform document scanners (Android ML Kit Document Scanner; iOS VisionKit `VNDocumentCameraViewController`) via an Expo config-plugin module, with a `react-native-vision-camera` + on-device edge-detection fallback for devices without Google Play services. Features: auto edge detection with manual corner adjustment, perspective correction, auto-capture when stable, up to 50 pages, reorder/delete/rotate, filters (original, greyscale, high contrast), page-count and quality hints spoken for screen-reader users ("Document edges found. Hold still.").
- **FR-P22-30** Output: each page JPEG (quality 0.75, long edge ≤ 2,400 px) assembled into one PDF on device; SHA-256 of each page and of the assembled PDF computed at capture and sent in the upload manifest so the evidence trail shows capture → PDF (NN-09). EXIF GPS stripped by default; capture time and device model kept only if the user marks the scan as evidence.
- **FR-P22-31** On-device OCR preview (ML Kit text recognition for Latin and Devanagari scripts; other Indic scripts server-side only [VERIFY on-device script coverage]) gives instant search hints and the Aadhaar check; the authoritative OCR, handwriting type copy and translation are server renditions from P05 (`drv_`), labelled, versioned and editable (NN-09, CH-28).
- **FR-P22-32** Aadhaar masking (NN-04): on every capture or pick, an on-device detector checks for 12-digit patterns with Verhoeff validation and Aadhaar card cues ("आधार", "Aadhaar", "Unique Identification Authority", "VID"). On a hit: "This looks like an Aadhaar number. LawDocs does not need it in full. Mask the first 8 digits?" with **Mask automatically** (default; also masks the QR code) or **Mask manually**. No "upload unmasked" option exists. The server re-runs detection (P05); an unmasked number found server-side is masked in the stored derivative and the user is notified. PAN is displayed masked; bank account numbers prompt only.
- **FR-P22-33** Resumable uploads: multipart S3 presigned parts (5 MB cellular, 8 MB Wi-Fi), background transfer (iOS background URLSession; Android WorkManager), resume of missing parts, malware scan and MIME allow-list server-side, queue screen with progress, paused, failed (reason + help key) and done; jobs survive app kill and restart; "Wi-Fi only for files over 20 MB" setting (USER).

### 4G. Share-sheet import, including WhatsApp exports

- **FR-P22-34** iOS Share Extension and Android intent filters (`ACTION_SEND`, `ACTION_SEND_MULTIPLE`) accept PDF, DOCX, XLSX, images (JPEG, PNG, HEIC converted to JPEG), audio (M4A, OPUS, MP3) and ZIP. The extension authenticates with the shared keychain group/app group (iOS) or the main app process (Android), shows a destination picker (workspace → folder, or "Attach to matter / agreement / consumer case"), applies the Aadhaar check (FR-P22-32) and queues the upload; it never holds a full session token beyond the platform's shared secure storage.
- **FR-P22-35** WhatsApp chat exports ("Export chat" `.txt` with or without media, delivered as a `.zip` or multiple files): the app stores the original export immutably (hash at receipt) and asks P05 to build a **chat transcript rendition**: parsed messages with timestamp, sender label as in the export, message text, media references linked to the extracted media files, and system notices; output as a readable PDF and CSV, labelled "Generated from a WhatsApp export — check against the original". Locale-specific date formats in exports are detected; ambiguous dates are flagged for the user to confirm. The user can select a message range to attach to a pleading or notice; P10 can then generate the BSA 2023 s.63(4) certificate draft for the export (NN-10).
- **FR-P22-36** Screenshots of chats or documents go through the same P05 type-copy pipeline; the screenshot stays the original; the typed copy is a derived rendition the user can correct (CH-28).
- **FR-P22-37** Third-party personal data notice: on the first chat import the app explains that chats contain other people's personal data, that the user should import only what they need for their matter, and how to delete it (DPDP purpose limitation [INTERP]). Imports are private to the importing user unless shared.

### 4H. Drafting on mobile

- **FR-P22-38** Template lane: the P06 questionnaire renders natively from the same JSON Schema + UI schema (pinned version), one question per screen with progress, "i" explanations per question, voice input on text answers (§4M), autosave every 5 s and on blur, resume on web. Preview renders server-side as paginated images with a text layer for screen readers and zoom to 400%.
- **FR-P22-39** Vidhi lane: "Ask Vidhi to adapt this" opens a chat bound to the draft; Vidhi proposes clause changes as tracked suggestions; output labelled **"AI draft — not reviewed by a professional"** with one-tap paid review (NN-14, CH-30).
- **FR-P22-40** Editing: a structured editor for fields, parties, schedules and clause selection; free-text editing of clauses in a simplified editor; whole-document formatting and complex redlining stay on web ("Continue on computer" hand-off sends a secure link to the user's own email or opens the web app on a signed-in desktop session via QR).
- **FR-P22-41** Language: the user can draft in any enabled D-07 language where the template has a reviewed translation; otherwise the template is English with a labelled machine translation preview (NN-48).

### 4I. Negotiation chat and change review (NN-37)

- **FR-P22-42** Deal-room threads (P07) per agreement: external thread (all parties), internal thread (own side only, visibly labelled "Internal — not visible to {counterparty}"), and per-change comments. The composer shows the audience above the input and changes colour and text when switching; sending to the external thread from the internal composer is impossible (separate composers).
- **FR-P22-43** Change review: list of tracked changes for the round with author, before/after text and clause reference; accept, reject or comment per change; bulk accept is confirmation-gated; every decision logged per change (NN-37). New round creation follows P07 rules.
- **FR-P22-44** Voice notes in threads (≤ 2 min) with optional labelled machine transcript; attachments through FR-P22-33; read receipts (user can disable); message retraction within 10 min hides but retains with `retracted_at`.
- **FR-P22-45** Counterparty contact rules: LawDocs sends a counterparty at most one invitation plus reminders they did not opt out of; no automated calls (NN-34). Push to a counterparty happens only if they installed the app and opted in.

### 4J. eSign, eStamp and execution (NN-06, NN-07, NN-08, NN-40)

- **FR-P22-46** Before any signing request, the app calls the P08 eligibility API; an excluded instrument (IT Act First Schedule) shows the wet-ink/notary/registration pack with booking options instead of the eSign button (`LD-SGN-014` from P08; NN-07, CH-12). "Check" instruments show the condition and require the user's confirmation per P08.
- **FR-P22-47** Stamp before sign (NN-08): where the State requires duty before execution, the flow is: State and article confirmation → duty computed by P08 from the State registry (duty at actuals, LawDocs facilitation fee separate, GST on the fee only) → payment → stamp procured through the authorised channel → certificate UIN verified and linked to the document hash → signing unlocked. "Attach my own stamp paper" uses the scanner with UIN entry and verification status.
- **FR-P22-48** Aadhaar eSign launch: biometric step-up; a native pre-sign summary (title, `LD-AGR-…`, pages, document hash prefix, signer name, "You are signing electronically under the Information Technology Act 2000, s.3A, through {ESP}") and the signer consent text required by the ESP flow; then the ESP/aggregator page opens in the system browser tab (`openAuthSessionAsync`), never an embedded WebView, unless P08 contracts a native SDK [VERIFY at contracting]. Return via the `/s/{id}/return` universal link; the app shows only the **server** status, which changes when the signature-verified provider webhook is processed (redirect parameters are never trusted). LawDocs' ASP capability is never exposed to any other app (NN-06).
- **FR-P22-49** Signing status: per signer (invited, viewed, signed, declined, expired), reminders (as allowed by NN-34), evidence pack and BSA s.63(4) certificate draft available after completion (NN-10); "Executed" only after the formalities gate (NN-40).
- **FR-P22-50** DSC signing tasks appear as "Sign on computer" with a QR hand-off; witness and notary steps per P08 tracking.

### 4K. Deep links and signing invites

- **FR-P22-51** iOS Universal Links (`apple-app-site-association`) and Android App Links (`assetlinks.json`, `autoVerify=true`) on the guest and app hosts `sign.lawdocs.in` (signing invites `/s/…`) and `my.lawdocs.in` (all other paths) — guest surfaces are `apps/web` routes, not `apps/public` (master §1.3; Appendix C §C.1) — and on the Consumer Help host. Paths: `/s/{token}` (signing invite), `/n/{token}` (negotiation invite), `/d/{docRef}`, `/a/{approvalId}`, `/m/{matterRef}`, `/pay/{orderId}`, `/x/{exportId}`. Custom scheme `lawdocs://` only for OAuth returns.
- **FR-P22-52** A link is a pointer, never a credential: `GET /m/v1/deep-links/resolve` re-authorises; a non-member gets the same "not available" response as a non-existent item (no existence leak). Invite tokens (`mob.deep_link_tokens`): 128-bit random, hashed at rest, expiry 14 days (TENANT range 1–30), ≤ 10 resolutions, bound to the invited contact; OTP to that contact is required before any document content is shown.
- **FR-P22-53** Not installed: the same URL opens the web signing experience (SSR, accessible) with optional store badges; guests are never forced to install. After install, `POST /m/v1/deep-links/claim` with attestation and OTP restores the pending path; no third-party attribution SDK, no clipboard hand-off, no device fingerprinting.
- **FR-P22-54** Invites are delivered through `packages/notify` (email, SMS, WhatsApp, RCS verified sender — R4 J-03) with DLT-registered templates; the message names LawDocs, the inviting party and the document title only as permitted by the template; anti-phishing guidance ("LawDocs will never ask for your Aadhaar OTP by call") is in every invite.

### 4L. Case, hearing, trademark and consumer-case status

- **FR-P22-55** Litigation (P11): matter and case cards with CNR or case number, forum, next hearing, last order, tasks; hearing calendar with device-calendar export (ICS) on user action; alerts T-7/T-3/T-1 days and T-2 h. Every status shows "Last refreshed {time} from {source}" and a user-initiated "Refresh" that calls the licensed partner within rate limits; never "real-time" or "live" wording (NN-20; master §11 `COURT_DATA_PORT`).
- **FR-P22-56** Trademarks (P12): application number, class, status from the deadline engine, next deadline (opposition window, response due, renewal), same staleness labelling and manual refresh; reminder schedule.
- **FR-P22-57** Consumer Help (v2, flavour only): case status timeline (complaint to RE → wait period → ombudsman eligibility → filed → resolved), documents checklist, and "Pay on official portal" deep links for challans (never collecting fines — NN-23, CH-22).

### 4M. Vidhi chat and voice in D-07 languages

- **FR-P22-58** Vidhi chat (P09) with workspace-scoped retrieval, citations, "unverified" labels, AI disclosure at session start ("You are talking to Vidhi, an AI assistant. Not a lawyer." in the user's language), and actions only as suggestions that need the user's confirmation (NN-13).
- **FR-P22-59** Voice input: push-to-talk (no always-listening); on-device speech recognition where the platform supports the language, else server ASR through the P05/P09 speech adapter in India-resident processing [VERIFY provider and Indic coverage]; the transcript appears for confirmation before sending; raw audio is discarded after transcription unless the user saves it as a voice note (`mob.vidhi.retain_audio`, default false).
- **FR-P22-60** Voice output: "Listen" on Vidhi answers and on document summaries using server TTS from the approved text or on-device `expo-speech` when the locale voice exists; machine-translated content carries a spoken disclaimer (NN-48); confidential classes use on-device TTS only.
- **FR-P22-61** Languages at v1: English and Hindi chat and voice; v2: all ten D-07 languages when P09 evaluation for the language passes and UI catalogue completeness ≥ 99%.
- **FR-P22-62** Vidhi help mode inside the help panel (P21 FR-P21-112) works offline for cached help articles; full Vidhi requires network ("Vidhi needs a connection" with the cached help fallback).

### 4N. Marketplace, purchase and payments

- **FR-P22-63** Marketplace browse (P16): categories, fixed-scope services, full fee breakdown (professional fee, LawDocs platform fee, government fee or stamp duty at actuals, GST, total) before payment (NN-22); no advocate ratings, photos, rankings or "book this advocate" (NN-21; Appendix M); neutral ordering.
- **FR-P22-64** Payment with the Razorpay React Native SDK for SKUs classified `EXTERNAL_ALLOWED` (§4O): order created server-side with an idempotency key; UPI intent first (installed UPI apps), then UPI collect/QR, cards (tokenised by Razorpay), netbanking; after the SDK callback the app shows "Confirming…" and polls `GET /m/v1/payments/{id}` until the webhook-confirmed state; the SDK callback alone never marks an order paid (NN-46). No card data touches the app (NN-22).
- **FR-P22-65** Renewal and cancellation terms are shown before any subscription purchase; cancellation is available in the same number of steps as purchase, or, for store subscriptions, through a direct link to the platform's subscription management page (NN-50).

### 4O. Store purchase-method policy (Apple and Google) [VERIFY current policies for the India storefronts before each submission]

Each P17/P16 SKU carries `store_class`. The table states the default classification and the reasoning; App Review is the final arbiter, so the review notes (FR-P22-82) explain each class.

| SKU family | Example | Apple (App Review Guidelines) | Google Play (Payments policy) | Default in app |
|---|---|---|---|---|
| Government fees and stamp duty | Duty at actuals, registration fee pass-through | Real-world payment, not digital content (3.1.3(e) goods/services outside the app; 3.1.5-type real-world) [INTERP] | Outside Play Billing scope (payments for physical goods/real-world services) [INTERP] | `EXTERNAL_ALLOWED` (Razorpay) |
| eStamp facilitation | ₹49 procurement fee through an ACC/SHCIL route | Service performed outside the app by a third party [INTERP; VERIFY] | Real-world service [INTERP] | `EXTERNAL_ALLOWED` |
| Professional services delivered by people | Document review by an advocate, company registration by a CS, retainer | Human professional services consumed outside the app; one-to-one real-time consultations fall under 3.1.3(d) person-to-person services [VERIFY whether App Review treats document-review deliverables as 3.1.3(e)] | Services performed outside the app [INTERP] | `EXTERNAL_ALLOWED`; fallback `WEB_ONLY` if Review objects |
| SaaS plans (individuals) | Personal, Pro | Digital subscription unlocking in-app features → IAP (3.1.1); or sell only on web and let the app access existing purchases as a multiplatform service (3.1.3(b)) with no in-app purchase call-to-action | Digital subscription → Play Billing, or user-choice/alternative billing where available in India [VERIFY current India programme] | `NOT_SOLD_IN_APP` (v1) [OWNER] |
| SaaS plans (companies) | Business, Enterprise | 3.1.3(c) Enterprise Services may use other methods when sold directly to organisations for employees [INTERP] | B2B purchase outside the app | `NOT_SOLD_IN_APP` (managed on web) |
| eSign credits, AI credits | Credit packs | Digital consumables used in the app → IAP (3.1.1) unless not sold in app | Digital goods → Play Billing or alternative billing [VERIFY] | `NOT_SOLD_IN_APP` (v1) [OWNER] |
| Template unlock (clean DOCX/PDF) | One-time unlock | Digital content → IAP | Digital goods → Play Billing | `NOT_SOLD_IN_APP` (v1) [OWNER] |
| FinLegal Academy courses | Paid course | Digital content → IAP; not offered in app | Digital content | `NOT_SHOWN` (catalogue card without price or link on iOS) |

- **FR-P22-66** `NOT_SOLD_IN_APP` items show the user's current entitlement and usage; on iOS there is **no** purchase button, price, or link or call-to-action to buy elsewhere, unless an Apple entitlement for external purchase links applies to the India storefront [VERIFY]; on Android the same default applies until the owner chooses Play Billing or alternative billing. Neutral text ("Your plan: Personal") is allowed.
- **FR-P22-67** If the owner enables in-app purchase (`mob.store.<platform>.digital_sales_mode = IAP`): StoreKit 2 and Google Play Billing Library [VERIFY current major version]; server-side receipt verification through App Store Server API / Server Notifications V2 and Google Real-time Developer Notifications into P17 via `BILLING_PORT`, which issues entitlements (OH8 remains the billing engine of record); store prices set per tier with GST handling confirmed [TAX MEMO: GST on app-store sales, whether the store acts as an e-commerce operator, and invoice issuance]; price parity or disclosed differences per NN-50; restore purchases; refunds via the store reflected in entitlements.
- **FR-P22-68** Payment-method decisions are settings (§9), maker-checker (`PLT_RELEASE_MANAGER` + `PLT_SUPER_ADMIN`), take effect only with a new store build (never by OTA — FR-P22-90).

### 4P. Notifications

- **FR-P22-69** `PUSH_PORT`: Expo Push primary, direct FCM/APNs fallback; tokens bound to `device_id`; invalid tokens pruned. Categories: `signing`, `approval`, `deadline` (hearings, TM deadlines, renewals, obligations), `payment`, `messages`, `documents` (OCR or type copy ready, share received), `account_security` (new device, export ready), `product_news` (OFF by default; separate consent).
- **FR-P22-70** Payload rule: only safe fields (document reference, generic event label, date/time) — never document text, counterparty names, amounts, case facts, health or family details; confidential matters send "You have an update" with a deep link only (NN-32). Lock-screen previews follow the same rule.
- **FR-P22-71** Quiet hours (USER default 21:00–08:00) for non-critical categories; `signing`, `approval` (configurable), `deadline` and `account_security` are never batched; others batch into a digest when more than 3 arrive within 6 hours. Undelivered critical pushes (no receipt in 10 min) fall back to SMS/WhatsApp only for the user's own account and only through consented, DLT-registered templates (NN-34).
- **FR-P22-72** Actionable notifications: "Review" opens the item; no approve/sign action from the notification itself (step-up and full context are required).

### 4Q. Accessibility (NN-28; Appendix U binding)

- **FR-P22-73** Every touchable has `accessibilityRole`, a localised `accessibilityLabel`, `accessibilityHint` where the action is not obvious and `accessibilityState`; grouped elements are announced as one where that reads better (document card: "Rent agreement, signed, 12 March 2026, button").
- **FR-P22-74** Targets ≥ 44 × 44 pt (iOS) and ≥ 48 × 48 dp (Android); Dynamic Type and Android font scale up to the largest accessibility sizes without truncation of legal text (scroll containers, no fixed-height text boxes); layout reflows at 200% (WCAG 1.4.4/1.4.10 equivalents).
- **FR-P22-75** Contrast tokens ≥ 4.5:1 text and ≥ 3:1 for UI components; high-contrast and dark themes; status never by colour alone ("Signed", "Waiting for Asha"); reduce-motion respected; no flashing.
- **FR-P22-76** Gestures: every swipe action (archive, accept/reject change) has a visible button and an accessibility action (`accessibilityActions`); no path-based or multi-finger gestures required (WCAG 2.5.1, 2.5.7); Switch Access, Voice Control and external keyboards supported with logical focus order.
- **FR-P22-77** Signing for screen-reader users: the pre-sign summary is a linear, headed screen; the document is available as accessible text (rendition from the DOCX source, not OCR) with clause navigation by heading; OTP fields are labelled single fields with platform one-time-code autofill; time-outs warn at least 60 s ahead with "Extend" (WCAG 2.2.1); ESP pages are in the system browser where the platform screen reader works [VERIFY ESP page accessibility at contracting — Appendix U §U.5].
- **FR-P22-78** Media: captions on all in-app videos by default (USER setting), transcripts, ISL renditions for core tutorials; "Listen" (TTS) on documents, summaries and help; voice input on all free-text fields.
- **FR-P22-79** Manual VoiceOver and TalkBack scripts for the five critical journeys (scan → vault; draft → sign; approve; negotiate a change; pay) and automated checks (accessibility linting, Maestro/Detox assertions on labels) are part of the exit gate; the accessibility preferences screen mirrors web (P21 FR-P21-144).

### 4R. Store listing, ASO, privacy declarations and account deletion

- **FR-P22-80** Listing content per flavour and locale from Appendix N §N.13: name, subtitle/short description, full description, keywords (Apple), category (Business or Productivity for LawDocs [OWNER]; Finance not used), screenshots and preview videos generated by the P21 tutorial pipeline on the synthetic demo tenant (captioned, with accessible descriptions in the listing text), "What's new" notes. Every claim passes the claims gate (NN-20); no "best lawyer", "government-approved", "real-time court status" or invented download counts; no advocate names or photos.
- **FR-P22-81** Privacy declarations generated from a single data-inventory file (`apps/mobile/privacy/data-inventory.yaml`) reviewed by `PLT_DPO`: Apple App Privacy labels; the iOS privacy manifest (`PrivacyInfo.xcprivacy`) with required-reason API declarations for the app and every SDK (CI fails if an SDK lacks a manifest) [VERIFY current Apple list]; Google Play Data safety form; consistency test that the declared data types match analytics and crash SDK configuration. No tracking as Apple defines it (no ATT prompt needed) unless marketing measurement is added, which would require ATT and a fresh review [OWNER].
- **FR-P22-82** App Review readiness: review notes explaining the purchase classification (§4O), eSign through a licensed ESP, the eligibility gate, KYC choices, and AI disclosures; demo accounts on a synthetic tenant (Personal and Company) with seeded documents; a signing invite the reviewer can complete with a test ESP route; contact for review.
- **FR-P22-83** Account deletion: in-app "Delete my account" (Apple 5.1.1(v); Google Play account-deletion requirement with a web deletion link) [VERIFY current wording]: explains what is deleted and what is retained under law or legal hold (signed instruments with counterparties, evidence logs, tax invoices, CERT-In logs) with retention periods, offers export first (NN-11), requires step-up, and runs the P01/P04 erasure workflow; company users are directed to their admin for workspace data.
- **FR-P22-84** AI-feature store items: disclosure that Vidhi uses a third-party AI model provider and what data is sent, with consent before first use where store rules require it (Apple guideline on sharing personal data with third-party AI [VERIFY 2025 update]); in-app "Report a problem with this answer" on every Vidhi response (Google Play generative-AI app policy [VERIFY]).
- **FR-P22-85** Age rating and audience: 18+ for account holders (contracts need capacity); guardians act for minors through `IND_GUARDIAN` (NN-26 children's data rules).
- **FR-P22-86** Export compliance: the app uses standard encryption only; set the platform encryption declarations accordingly [VERIFY].

### 4S. Release trains (EAS)

- **FR-P22-87** Trains: production store release every 4 weeks (`mob.release.train_weeks`), hotfix trains as needed; each train has a release record in `eng` (P23) with change list, risk class, test evidence, accessibility audit, privacy-declaration diff and approver (`PLT_RELEASE_MANAGER` maker, second approver checker — NN-18).
- **FR-P22-88** Pipeline: EAS Build per flavour and profile from a tagged commit; credentials managed in EAS with a KMS-held backup of signing keys and Play app-signing upload key; automated tests (unit, Maestro flows tagged by capability, accessibility lint, size and performance budgets, SDK privacy-manifest check); EAS Submit to TestFlight (internal then external testers) and Play internal → closed → production tracks.
- **FR-P22-89** Rollout: Apple phased release (7-day) and Play staged rollout 1% → 5% → 20% → 50% → 100%, each step gated by crash-free sessions ≥ 99.7%, ANR below threshold, no S1 accessibility regression and no spike in `LD-MOB-*` errors; automatic halt on breach.

### 4T. OTA update policy (EAS Update)

- **FR-P22-90** OTA updates are allowed only for JavaScript and asset changes that fix bugs, copy, translations, help content or layout and that do not change the app's primary purpose, add features requiring review, change permissions, payment or purchase flows, privacy practices, data collection, or native code (Apple Developer Program License Agreement interpreted-code clause and App Review 2.5.2; Google Play device-and-network-abuse policy on self-updating [VERIFY clause numbers]). Anything else ships through a store build.
- **FR-P22-91** Mechanics: EAS Update with **code signing** enforced (app rejects unsigned updates); `runtimeVersion` policy `fingerprint` so an update reaches only binaries with a matching native layer; channels map to build profiles; staged OTA rollout 10% → 50% → 100% with automatic rollback (republish previous update) when crash-free sessions drop by > 0.3 percentage points against baseline; emergency rollback in one action.
- **FR-P22-92** Governance: every OTA publish is maker-checker (`PLT_RELEASE_MANAGER` + checker), linked to a change record, audited (`in.lawdocs.mob.OtaReleasePublished.v1`, `in.lawdocs.mob.OtaRolledBack.v1`); an OTA cannot flip `store_class`, purchase modes or privacy settings (server-enforced: those flags are read only from the signed build config).

### 4U. Crash reporting and analytics with PII scrubbing (NN-32)

- **FR-P22-93** Crash and error tracking: Sentry-type service, self-hosted or India-resident (D-01 observability); `beforeSend` scrubber removes request bodies, headers, query strings except allow-listed keys, user-entered text, file names (replaced by type and size), and any pattern matching Aadhaar, PAN, mobile, email, OTP or bank account; breadcrumbs limited to navigation route names and HTTP status codes; no screenshots, view hierarchy captures or session replay; user identifier is a salted hash.
- **FR-P22-94** Product analytics: opt-in (consent artefact, NN-26); first-party, India-resident; event taxonomy of screen and action names with no content properties (e.g., `scan_completed{pages: 3}`), never document titles, party names, matter facts or search queries; analytics SDKs that cannot be configured this way are not allowed.
- **FR-P22-95** Monthly sample audit of crash and analytics payloads (P23) checks for PII; any finding is an S1 incident with a CERT-In triage per NN-27 where applicable.

### 4V. Performance and size budgets

- **FR-P22-96** Budgets enforced in CI and on the device lab: Android per-device download ≤ 35 MB (arm64-v8a) and ≤ 32 MB (armeabi-v7a); iOS thinned ≤ 50 MB; Hermes bundle ≤ 7 MB; cold start < 2.5 s mid-range, < 4.0 s low-end (2–3 GB RAM); warm start < 1.0 s; vault list of 500 items ≥ 55 fps median; scan of 10 pages to PDF ≤ 6 s mid-range; memory < 300 MB low-end during scanning. Indic fonts beyond Latin and Devanagari download on demand.
- **FR-P22-97** Device-lab matrix: at least 12 devices including low-end Android Go-class, mid-range Samsung/Xiaomi/Realme-class, current and n-2 iPhones, one iPad, with OS versions covering ≥ 95% of the active base (minimum iOS and Android versions set at P22 start [VERIFY Expo SDK support matrix]).

## 5. Workflows and state machines

### 5.1 Device lifecycle (`mob.devices.state`)

| State | Entry | Transitions | Actor | Guard | Side effects / events |
|---|---|---|---|---|---|
| PENDING | Key generated, attestation sent | → BOUND, → REJECTED | System | Attestation verified; device limit respected | — |
| BOUND | Registration OK | → DEGRADED, → RESTRICTED, → REVOKED | System / user / `ORG_ADMIN` | — | `in.lawdocs.mob.DeviceBound.v1`; notify other devices |
| DEGRADED | Basic integrity only or provider outage | → BOUND, → RESTRICTED, → REVOKED | System | Re-attestation | Offline cache disabled; step-up OTP |
| RESTRICTED | Integrity fail | → BOUND (re-attest pass), → REVOKED | System | — | `in.lawdocs.mob.IntegrityFailed.v1`; wipe offline cache |
| REVOKED | User/admin revoke, inactivity, new binding over limit | terminal | User / admin / system | Step-up for user revoke | Tokens invalidated; wipe on next contact; `in.lawdocs.mob.DeviceRevoked.v1` |

### 5.2 Signing from an invite link

`LINK_OPENED → RESOLVED (token valid) → OTP_VERIFIED → DOCUMENT_REVIEWED → (STAMP_CHECK: requires duty? → STAMPED) → CONSENT_SHOWN → ESP_LAUNCHED → RETURNED → SERVER_CONFIRMED (webhook) → SIGNED | DECLINED | FAILED`. Expired or over-used token → `NOT_AVAILABLE` (same response as non-existent). Excluded instrument → no signing state; wet-ink pack shown (NN-07).

### 5.3 Capture and upload job (`mob.upload_jobs.status`, client and server)

`CAPTURED (hashes computed) → AADHAAR_CHECKED (masked if hit) → QUEUED → UPLOADING ⇄ PAUSED → COMPLETING → SERVER_VERIFIED (hash, malware, MIME) → STORED (original immutable) → RENDITIONS_REQUESTED (P05) → DONE`, or `FAILED` (reason + help key, retry offered), or `QUARANTINED` (server found an issue; user notified).

### 5.4 Store purchase (only when `digital_sales_mode = IAP`)

`STOREFRONT_SHOWN → PURCHASE_STARTED (store sheet) → STORE_CONFIRMED (client) → SERVER_VERIFIED (App Store Server API / Play Developer API) → ENTITLEMENT_ISSUED (P17 via BILLING_PORT; OH8 notified) → ACTIVE → RENEWED | CANCELLED | REFUNDED | EXPIRED` driven by server notifications; entitlement changes only on server verification. Emits `in.lawdocs.mob.StorePurchaseVerified.v1`.

### 5.5 OTA release (`mob.ota_releases.state`)

`DRAFT → APPROVED (maker-checker) → ROLLING_10 → ROLLING_50 → LIVE`, any rolling state → `ROLLED_BACK` (auto on crash regression or manual). Only allowed when the change classification check (FR-P22-90) passes.

## 6. Screens and UX

### 6.1 Feature-parity matrix (`apps/mobile/parity.json`; `F` full, `R` read-only, `W` hand-off to web, `—` excluded with reason)

| Capability (phase) | Individual | Company maker/member | Checker/approver/CLO | Director/KMP | Guest | Reason code if not F |
|---|---|---|---|---|---|---|
| Vault browse, search, share, versions (P04) | F | F | F | R | R (shared items) | — |
| Offline encrypted cache (P04/P22) | F | F (tenant policy) | F (tenant policy) | F (tenant policy) | — | `GUEST_NO_CACHE` |
| Bulk folder import (P04) | W | W | W | — | — | `BULK_ONLY` |
| Camera scan + OCR + type copy (P05) | F | F | F | F | — | — |
| Share-sheet and WhatsApp import (P05) | F | F | F | — | — | — |
| Template-lane drafting (P06) | F | F | R | — | — | — |
| Vidhi drafting lane (P06/P09) | F | F | R | R | — | — |
| Full-document redline authoring (P07) | W | W | W | — | W | `COMPLEX_EDITING` |
| Change review accept/reject/comment (P07) | F | F | F | R | F | — |
| Deal-room chat internal/external (P07) | F | F | F | R | F (external only) | — |
| eSign Aadhaar via ESP (P08) | F | F | F | F | F | — |
| DSC signing (P08) | W | W | W | W | W | `DSC_HARDWARE` |
| eStamp purchase / attach stamp paper (P08) | F | F | R | — | — | — |
| Evidence pack and s.63 certificate draft (P08/P10) | F | F | F | R | R (own signature) | — |
| Maker-checker approvals (P02/P13) | — | — | F | F (board items) | — | — |
| Pleadings and notices drafting (P10) | F (template lane) | F | R | — | — | — |
| Litigation tracker and hearings (P11) | F | F | F | R | — | — |
| Trademark tracker (P12) | F | F | F | R | — | — |
| Board and resolutions (P13) | — | R | R | F (sign where eligible) | — | — |
| Marketplace browse and buy (P16) | F | F | F | — | — | — |
| Plan purchase and upgrade (P17) | W (store policy) | W | W | — | — | `STORE_POLICY` |
| Savings dashboard (P17) | R | R | R | R | — | — |
| Credential vault reveal (P18/`cvl`) | — | — | — | — | — | `ADMIN_ONLY` (web, NN-16) |
| Export everything (P20) | F | W (admin) | W | — | — | `ADMIN_ONLY` |
| Help panel, "i", tours, tutorials (P21) | F | F | F | F | F (signing help) | — |
| Consumer Help cases (P15, v2 flavour) | F | — | — | — | — | `BRAND_FLAVOUR` |

CI job `parity-check` fails if a capability from any phase lacks an entry, if an `F` entry lacks a Maestro flow tagged with its ID, or if an exclusion lacks an approved reason code (`BULK_ONLY`, `COMPLEX_EDITING`, `DSC_HARDWARE`, `STORE_POLICY`, `ADMIN_ONLY`, `GUEST_NO_CACHE`, `BRAND_FLAVOUR`).

### 6.2 Screen catalogue

| ID | Purpose | Key components | Empty / error states | Accessibility notes |
|---|---|---|---|---|
| SCR-P22-01 | Welcome and sign-in | OTP, passkey, SSO, language picker | OTP failure with resend timer and voice-call option | Language picker first; OTP single field with autofill |
| SCR-P22-02 | Biometric set-up and app lock | Opt-in, explanation | Not enrolled → OTP only | Explains device-local biometrics |
| SCR-P22-03 | Workspace switcher | Personal + companies | — | Announces current workspace |
| SCR-P22-04 | Home (personal) | Tasks, recent, quick actions (Scan, Create, Ask Vidhi), deadlines | New user → checklist | Headings per section |
| SCR-P22-05 | Home (company) / Inbox | Approvals, tasks, hearings, renewals | Nothing pending → "All clear" | Counts in text |
| SCR-P22-06 | Vault folders and search | Folder views, filters, offline badges | Offline → cached only notice | Filters as dialog with fieldsets |
| SCR-P22-07 | Document detail and viewer | Versions, renditions, share, sign, Vidhi | Rendition pending | Accessible text view, clause headings |
| SCR-P22-08 | Scanner | Edge detection, page strip, filters | Camera denied → explain + settings link | Spoken capture hints |
| SCR-P22-09 | Aadhaar masking prompt | Preview with mask boxes | — | Mask regions described |
| SCR-P22-10 | Share-extension destination picker | Workspace, folder, attach-to | Not signed in → open app | — |
| SCR-P22-11 | WhatsApp import review | Message list, range select, media | Ambiguous date format → confirm | Messages as list items with sender and time |
| SCR-P22-12 | Upload queue | Progress, paused, failed | — | Progress values announced |
| SCR-P22-13 | Questionnaire (template lane) | One question per screen, "i", voice input | Validation summary | Error text linked to field |
| SCR-P22-14 | Draft preview and Vidhi adapt | Paginated preview, AI label | Template withdrawn | Label read first |
| SCR-P22-15 | Deal room | External and internal threads, composers | — | Audience announced before send |
| SCR-P22-16 | Change review | Change list, accept/reject/comment | No changes | Before/after as text, not colour |
| SCR-P22-17 | Eligibility and stamp step | Badge, State, duty breakdown, attach stamp | Not eligible → wet-ink pack | Fee table readable |
| SCR-P22-18 | Pre-sign summary and consent | Hash prefix, signer, legal text | ESP unavailable → retry/second ESP | Linear headed screen |
| SCR-P22-19 | Signing status and evidence | Signers, reminders, evidence, s.63 draft | Declined → reason | Status in text |
| SCR-P22-20 | Approval detail | Summary, diff, approve/return with step-up | Already actioned | Step-up dialog accessible |
| SCR-P22-21 | Matters and hearing calendar | Cards, calendar, refresh | Source stale → label | Calendar list alternative (Appendix U §U.5) |
| SCR-P22-22 | Trademark portfolio | Status, deadlines | — | — |
| SCR-P22-23 | Vidhi chat and voice | Disclosure, push-to-talk, transcript confirm, Listen | Offline → help-only mode | Voice and text parity |
| SCR-P22-24 | Marketplace and checkout | Services, fee breakdown, Razorpay | Payment pending → "Confirming…" | — |
| SCR-P22-25 | Plan and entitlements (store-policy aware) | Current plan, usage | — | — |
| SCR-P22-26 | Notifications centre and settings | Categories, quiet hours, digest | — | — |
| SCR-P22-27 | Devices and security | Bound devices, revoke | — | — |
| SCR-P22-28 | Accessibility preferences | Theme, text size, motion, captions, inline "i", easy-read | — | Mirrors web |
| SCR-P22-29 | Help panel and tours | Articles, video, terms, contact support | Offline cached | Non-modal sheet |
| SCR-P22-30 | Export and account deletion | Export everything, delete account with retention explanation | Legal hold → explain | — |
| SCR-P22-31 | Restricted mode banner/screen | Reason, web link, support | — | — |
| SCR-P22-32 | Update required | Store link | — | — |
| SCR-P22-33 | Consumer Help home and case timeline (v2 flavour) | Case stages, documents, official-portal links | — | — |

## 7. Backend design

### 7.1 Modules

`mob` (BFF, devices, push, deep links, versions, OTA records, store receipts) in `apps/api`; it composes `dms`, `dix`, `tpl`, `drf`, `clm`, `msg`, `sgn`, `lit`, `ipm`, `mkp`, `bil`, `ai`, `hlp`, `ntf`, `iam`, `xpt` through their public module interfaces.

### 7.2 Tables (tenant rows carry `tenant_id` + `legal_entity_id` with RLS where the row is tenant-scoped; device rows are user-scoped)

| Table | Key columns | Indexes | RLS | Retention class |
|---|---|---|---|---|
| `mob.devices` | id, user_id, platform, model, os_version, app_version, public_key, attestation_verdict, integrity, state, bound_at, last_seen_at | (user_id, state) | user | 1 year after revoke |
| `mob.push_tokens` | id, device_id, provider, token (encrypted), categories_jsonb, quiet_hours | device_id | user | until pruned |
| `mob.deep_link_tokens` | id, token_hash, purpose, target_ref, contact_ref, expires_at, max_uses, uses, tenant_id | token_hash unique | tenant | 90 days after expiry |
| `mob.upload_jobs` | id, user_id, tenant_id, manifest_jsonb (hashes, sizes), status, error_code | (user_id, status) | tenant | 30 days after DONE |
| `mob.app_versions` | platform, brand, version, min_supported, recommended, released_at | (platform, brand) | platform | permanent |
| `mob.ota_releases` | id, channel, runtime_version, update_group_id, change_ref, state, rollout_pct, approved_by | channel | platform | permanent |
| `mob.store_receipts` | id, user_id, platform, product_id, original_transaction_id, state, verified_at, entitlement_ref | original_transaction_id unique | user | 8 years [TAX MEMO] |
| `mob.capture_metadata` | id, document_id, page_hashes[], pdf_hash, captured_at, device_model (optional), evidence_flag | document_id | tenant | with the document |

### 7.3 APIs (BFF `/m/v1`)

| Method | Path | Scope | Idempotency |
|---|---|---|---|
| GET | `/m/v1/me`, `/m/v1/config` | authenticated | — |
| POST | `/m/v1/devices` · DELETE `/m/v1/devices/{id}` | authenticated (+ step-up for delete) | Idempotency-Key |
| POST | `/m/v1/devices/{id}/attest` | authenticated | Idempotency-Key |
| POST | `/m/v1/push-tokens` | authenticated | Idempotency-Key |
| GET | `/m/v1/home`, `/m/v1/inbox`, `/m/v1/vault/folders/{id}`, `/m/v1/documents/{id}` | authenticated, RLS | — |
| GET | `/m/v1/sync/changes?cursor=` | authenticated | — |
| POST | `/m/v1/uploads` · `/m/v1/uploads/{id}/complete` · GET `/m/v1/uploads/{id}` | authenticated | Idempotency-Key |
| POST | `/m/v1/imports/whatsapp` | authenticated | Idempotency-Key |
| POST | `/m/v1/approvals/{id}/decision` | checker roles + step-up | Idempotency-Key |
| POST | `/m/v1/signing-requests/{id}/mobile-launch` | signer + step-up | Idempotency-Key |
| GET | `/m/v1/deep-links/resolve?path=` · POST `/m/v1/deep-links/claim` | public + OTP / authenticated | Idempotency-Key (claim) |
| POST | `/m/v1/orders/{id}/payment-intents` · GET `/m/v1/payments/{id}` | authenticated + step-up | Idempotency-Key |
| POST | `/m/v1/store/receipts` | authenticated (IAP mode only) | Idempotency-Key |
| POST | `/m/v1/exports` | owner/admin + step-up | Idempotency-Key |
| POST | `/m/v1/account/deletion-requests` | owner + step-up | Idempotency-Key |
| WS | `/m/v1/realtime` | authenticated, per-subscription authorisation | — |

Errors (range **`LD-MOB-001`–`LD-MOB-030`**, each with a help key `hlp.mob.*`): `001` Update required · `002` Device limit reached · `003` Device integrity check failed (restricted mode) · `004` Attestation unavailable (degraded) · `005` Step-up required · `006` Biometric enrolment changed — sign in again · `007` Certificate validation failed · `008` Offline copy not permitted by your organisation · `009` Saving to device not permitted · `010` Upload incomplete — resume available · `011` File type not accepted · `012` WhatsApp export could not be parsed · `013` Link not available · `014` Link expired · `015` Payment confirmation pending · `016` Purchase not available in the app · `017` Store receipt could not be verified · `018` Feature needs a computer (DSC, bulk import) · `019` Vidhi needs a connection · `020` Voice language not yet supported · `021` OTA update signature invalid · `022` Account deletion blocked by legal hold (explains retention) · `023` Screen capture blocked on this screen.

### 7.4 Domain events

`in.lawdocs.mob.DeviceBound.v1`, `in.lawdocs.mob.DeviceRevoked.v1`, `in.lawdocs.mob.IntegrityFailed.v1`, `in.lawdocs.mob.ScreenCaptureDetected.v1`, `in.lawdocs.mob.OfflineCacheWiped.v1`, `in.lawdocs.mob.DeepLinkClaimed.v1`, `in.lawdocs.mob.StorePurchaseVerified.v1`, `in.lawdocs.mob.OtaReleasePublished.v1`, `in.lawdocs.mob.OtaRolledBack.v1`, `in.lawdocs.mob.AppVersionPolicyChanged.v1`. No cross-product events.

### 7.5 Jobs and workflows

Temporal: `DeviceAttestationWorkflow` (24-hour re-attestation), `WhatsAppImportWorkflow` (store original → parse → rendition → notify), `StoreEntitlementWorkflow` (server notifications → verify → P17), `OtaRolloutWorkflow` (staged percentages with health gates). BullMQ: push fan-out with receipts, token pruning, inactive-device revoke sweep (daily), deep-link token expiry sweep, crash-free-session monitor feeding rollout gates.

## 8. Integrations

| Port / adapter | Default | Alternatives | Failure behaviour | Manual fallback |
|---|---|---|---|---|
| `PUSH_PORT` | Expo Push | Direct FCM/APNs | Retry; critical → SMS/WhatsApp per NN-34 | In-app inbox |
| Integrity | Play Integrity API; App Attest | — | Degraded mode, alert | Web app |
| Scanner | ML Kit Document Scanner; VisionKit | vision-camera + edge detection | Fallback scanner | Photo picker |
| `ESIGN_PORT` (P08) | Aggregator from P08 via system browser | Second ESP route | Offer retry / second route | Web signing |
| `PAYMENTS` | Razorpay React Native SDK via OH8 orders | Razorpay hosted checkout in browser tab | "Confirming…" then push | Web checkout |
| `BILLING_PORT` (IAP mode) | App Store Server API + Notifications V2; Google Play Developer API + RTDN | — | Entitlement unchanged until verified | Support ticket |
| Speech (ASR/TTS) | On-device where available; P05/P09 Indic adapters | — | Text-only | — |
| Crash/analytics | Self-hosted or India-resident Sentry-type; first-party analytics | — | Drop events locally | — |
| EAS | Build, Submit, Update | Self-hosted build runners (fallback) | Manual build from tagged commit | — |

## 9. Settings and configuration (register in Appendix R — NN-29)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `mob.version.min_supported` | PLATFORM (per platform, brand) | semver | set per release | `PLT_RELEASE_MANAGER` | Y |
| `mob.version.recommended` | PLATFORM | semver | latest | `PLT_RELEASE_MANAGER` | N |
| `mob.devices.max_active` | TENANT | int | individual 3, company 2 (range 1–5) | `ORG_ADMIN` | N |
| `mob.lock.background_minutes` | TENANT, USER | int | individual 5, company 2 (range 1–15) | `ORG_ADMIN`, user (stricter only) | N |
| `mob.stepup.window_seconds` | PLATFORM | int | 60 | `PLT_SECURITY_OFFICER` | Y |
| `mob.integrity.policy` | PLATFORM | object | per FR-P22-13 | `PLT_SECURITY_OFFICER` | Y |
| `mob.screen.allow_capture_classes` | TENANT | list | none | `ORG_ADMIN` | Y |
| `mob.offline.enabled` | TENANT | bool | true | `ORG_ADMIN` | N |
| `mob.offline.auto_cache_recent` | TENANT, USER | bool | individuals true, companies false | `ORG_ADMIN`, user | N |
| `mob.offline.max_mb` | USER | int | 500 | user | N |
| `mob.offline.max_days_without_contact` | TENANT | int | 30 | `ORG_ADMIN` | Y |
| `mob.export.device_save_allowed` | TENANT | bool | individuals true, companies false | `ORG_ADMIN` | Y |
| `mob.upload.wifi_only_over_mb` | USER | int | 20 | user | N |
| `mob.deeplink.invite_expiry_days` | TENANT | int | 14 (1–30) | `ORG_ADMIN` | N |
| `mob.push.quiet_hours` | USER | object | 21:00–08:00 | user | N |
| `mob.push.digest_threshold` | PLATFORM | int | 3 per 6 h | `PLT_SUPER_ADMIN` | N |
| `mob.vidhi.retain_audio` | USER | bool | false | user | N |
| `mob.vidhi.voice_locales` | PLATFORM | list | en, hi (v1) | `PLT_SUPER_ADMIN` | Y |
| `mob.store.ios.digital_sales_mode` | BRAND | enum NOT_SOLD_IN_APP/IAP | NOT_SOLD_IN_APP [OWNER] | `PLT_SUPER_ADMIN` | Y (build-time) |
| `mob.store.android.digital_sales_mode` | BRAND | enum NOT_SOLD_IN_APP/PLAY_BILLING/ALT_BILLING | NOT_SOLD_IN_APP [OWNER] | `PLT_SUPER_ADMIN` | Y (build-time) |
| `mob.release.train_weeks` | PLATFORM | int | 4 | `PLT_RELEASE_MANAGER` | N |
| `mob.ota.enabled` | PLATFORM | bool | true | `PLT_RELEASE_MANAGER` | Y |
| `mob.ota.auto_rollback_crash_delta_pp` | PLATFORM | decimal | 0.3 | `PLT_RELEASE_MANAGER` | Y |
| `mob.analytics.enabled` | PLATFORM | bool | true (consent-gated per user) | `PLT_DPO` | Y |
| `mob.nav.tab_order` | USER | list | per FR-P22-03 | user | N |
| `mob.bottom_bar.items` | TENANT | list (exactly 2; Company middle slots) | `[Contracts, Matters]` | ORG_ADMIN | N |
| `mob.kill.<feature>` (scan, whatsapp_import, vidhi_voice, payments, ota) | PLATFORM | bool | false | `PLT_SUPER_ADMIN`, `PLT_SRE` | N (audited) |

## 10. Security, privacy and audit

| Threat | Control |
|---|---|
| Stolen or cloned device | Hardware-bound keys, DPoP, biometric-wrapped refresh token, remote revoke, crypto-shred wipe, device limits |
| Rooted/jailbroken or tampered app | Play Integrity / App Attest server verdicts, restricted mode, code obfuscation of native modules, OTA code signing |
| Man-in-the-middle | TLS 1.3, certificate pinning with backup pins, no cleartext (`NSAppTransportSecurity` strict; Android network security config) |
| Shoulder-surfing, screenshots, app switcher | FLAG_SECURE, iOS overlays, watermark, capture detection |
| Phishing via fake signing links | Verified domains, App Links/Universal Links, OTP bound to invited contact, RCS verified sender, anti-phishing copy |
| PII in logs and telemetry (NN-32) | Scrubbers, allow-listed breadcrumbs, no replay, monthly audit |
| Aadhaar exposure (NN-04) | On-device and server masking; no unmasked upload path; never store full numbers |
| Over-collection from chat imports | Range selection, purpose notice, private by default, deletion controls |
| Store-policy breach | `store_class` classification, build-time payment modes, OTA restrictions, review notes |

Audit events: device bind/revoke, step-ups, approvals, signing launches, payment intents, exports, account deletion requests, capture-detection events, OTA publishes and rollbacks — all in the ledger in-transaction (NN-45). DPDP: consent for analytics and product news; notice for chat imports; deletion and export flows; children through guardians only.

## 11. AI touchpoints and guardrails

| Feature | Runtime | Autonomy | Human confirmation | Guardrails |
|---|---|---|---|---|
| Vidhi chat and voice | P09 | L0–L1 | Any action (send, share, sign, pay, file) needs a per-action confirmation (NN-13) | AI disclosure at start, citations or "unverified" (NN-14), workspace-scoped retrieval, Bedrock India for confidential classes (NN-15), audio not retained by default |
| Vidhi drafting lane | P06/P09 | L1 | User reviews; paid professional review offered | "AI draft — not reviewed by a professional" |
| Type copy, OCR, translation, chat transcript | P05 | L1 | User corrects; renditions labelled with confidence | Originals immutable (NN-09); MT labelled (NN-48) |
| Alt text for captured images (accessibility) | `packages/ai` vision | L1 | User may edit | Labelled as generated |

Evaluation: P09 language evaluations gate each voice locale (FR-P22-61); a mobile-specific evaluation set checks that voice transcripts in noisy conditions are confirmed before sending in 100% of cases.

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p22/*.feature`)

```gherkin
@P22-AT-01 @NN-03
Scenario: Aadhaar is never offered as a login method
  Given a new user opens the LawDocs app
  When the sign-in screen renders
  Then the options are mobile OTP, email link, passkey and SSO
  And no option uses Aadhaar authentication

@P22-AT-02 @NN-44
Scenario: Biometric enrolment change forces re-login
  Given a user with biometric unlock enabled
  When a new fingerprint is added to the device
  Then the next unlock fails with LD-MOB-006 and requires OTP sign-in

@P22-AT-03 @NN-44
Scenario: Offline cache is encrypted and wiped on revoke
  Given a user pinned a signed agreement for offline use
  Then the file on disk is unreadable without the device-bound key
  When the user revokes the device from the web
  And the device next contacts the server
  Then the wrapped keys, files and database are deleted
  And event in.lawdocs.mob.OfflineCacheWiped.v1 is recorded

@P22-AT-04 @NN-44
Scenario: Integrity failure restricts the app
  Given Play Integrity returns no device integrity
  When the user opens a document
  Then the app is in restricted mode with LD-MOB-003 and offers the web app

@P22-AT-05 @NN-04
Scenario: Aadhaar number is masked before upload
  Given a user scans an Aadhaar card
  When the on-device detector finds a valid 12-digit Aadhaar number
  Then the user is offered automatic or manual masking only
  And the stored derivative shows only the last 4 digits

@P22-AT-06 @NN-09
Scenario: Capture hashes are preserved
  Given a 3-page scan
  When the upload completes
  Then the server verifies the PDF hash from the manifest
  And the original is stored under Object Lock and OCR text is a labelled rendition

@P22-AT-07
Scenario: WhatsApp export becomes a transcript rendition
  Given a user shares a WhatsApp "Export chat" zip with media to LawDocs
  When the import completes
  Then the original zip is stored unchanged with its hash
  And a transcript PDF and CSV labelled "Generated from a WhatsApp export" are available
  And the user can select a message range to attach to a notice

@P22-AT-08 @NN-07
Scenario: Excluded instrument cannot be routed to eSign on mobile
  Given a user drafted a will
  When they tap the signing action
  Then the wet-ink and registration pack is shown
  And the API returns LD-SGN-014 if eSign is forced

@P22-AT-09 @NN-08
Scenario: Stamp before sign
  Given a rent agreement for Maharashtra that requires duty before execution
  When the user starts signing
  Then the duty, facilitation fee and GST on the fee are shown separately
  And signing stays locked until a verified stamp certificate UIN is linked to the document hash

@P22-AT-10 @NN-06
Scenario: Signing status comes only from the server
  Given the ESP redirects back with status "success" in the URL
  And the provider webhook has not been processed
  Then the app shows "Confirming your signature" and not "Signed"

@P22-AT-11
Scenario: Guest signs from a link without installing the app
  Given a counterparty without the app opens https://sign.lawdocs.in/s/{token}
  When they verify the OTP sent to the invited mobile
  Then they can review and sign in the web flow
  And an expired token returns the same response as a non-existent one

@P22-AT-12 @NN-37
Scenario: Internal comment cannot reach the counterparty
  Given a maker is in the internal thread of a deal room
  When they send a message
  Then it is stored with audience INTERNAL and is not visible to the counterparty session

@P22-AT-13 @NN-18
Scenario: Approval from push requires step-up and maker is not checker
  Given a checker receives an approval push
  When they open it and approve
  Then biometric or OTP step-up is required
  And an approval on an item they created fails with "LD-WF-010" (P02 maker cannot approve own request)

@P22-AT-14 @NN-20
Scenario: Court status is labelled with freshness
  Given a tracked case refreshed from a licensed partner 3 hours ago
  Then the card shows "Last refreshed 3 hours ago from {source}"
  And no screen contains the words "real-time" or "live" for court data

@P22-AT-15 @NN-14
Scenario: Vidhi voice session discloses AI and confirms transcript
  Given a user starts Vidhi voice in Hindi
  Then the first message discloses that Vidhi is an AI assistant, not a lawyer
  And the transcript is shown for confirmation before it is sent

@P22-AT-16 @NN-22
Scenario: Marketplace payment shows full breakdown and confirms by webhook
  Given a user buys "Rent agreement review"
  Then professional fee, platform fee and GST are shown with the total before payment
  And the order is marked paid only after the verified Razorpay webhook

@P22-AT-17
Scenario: Digital items are not sold in the iOS app by default
  Given digital_sales_mode for iOS is NOT_SOLD_IN_APP
  When an individual opens Plan and entitlements on iOS
  Then the current plan and usage are shown
  And no purchase button, price or external purchase link is present

@P22-AT-18 @NN-32
Scenario: Crash report contains no personal data
  Given a crash occurs while a user types a party name in a questionnaire
  When the crash report is sent
  Then it contains no input text, file names, Aadhaar, PAN, mobile or email patterns

@P22-AT-19
Scenario: OTA cannot change purchase behaviour
  Given an OTA update that changes the payment screen
  When the release manager submits it
  Then the classification check rejects it and requires a store build

@P22-AT-20
Scenario: Staged OTA rolls back on crash regression
  Given an OTA at 10% rollout
  When crash-free sessions drop 0.4 percentage points below baseline
  Then the previous update is republished automatically and in.lawdocs.mob.OtaRolledBack.v1 is emitted

@P22-AT-21 @NN-28
Scenario: Critical journeys pass screen-reader scripts
  Given VoiceOver on iOS and TalkBack on Android
  When the tester runs the scan, sign, approve, negotiate and pay scripts
  Then every control is reachable, labelled and operable without gestures
  And text scales to the largest accessibility size without truncation

@P22-AT-22 @NN-11
Scenario: Export everything from mobile
  Given an individual starts "Export everything" on mobile
  When the LD-EXPORT-1.0 job completes
  Then the package includes "99 System Data/Devices.csv" and "99 System Data/Capture Metadata.csv"

@P22-AT-23 @NN-23
Scenario: Consumer Help flavour excludes lender-facing modules
  Given the Consumer Help flavour build
  Then the build allow-list check passes only if no LawDocs company, LDC, Finbyx, Udofin or Equator route is bundled
  And signing in with a LawDocs company account is refused

@P22-AT-24
Scenario: Account deletion explains retention and offers export
  Given an individual with signed agreements requests account deletion
  Then the app lists data that will be deleted and data retained by law with periods
  And offers "Export everything" before confirming with step-up

@P22-AT-25 @NN-01
Scenario: Workspace switch never shows another tenant's cached data
  Given a user belongs to Company A and Company B and has cached documents in Company A
  When they switch to Company B while offline
  Then no Company A document, title or count is visible
  And cache rows are read only for the (tenant, legal entity, workspace) partition of Company B

@P22-AT-26 @NN-13
Scenario: Vidhi cannot share a document without confirmation
  Given Vidhi suggests "Share the signed agreement with your landlord"
  Then the suggestion opens a share screen with recipient, scope and expiry
  And nothing is shared until the user confirms with step-up

@P22-AT-27 @NN-34
Scenario: Counterparty receives one invitation and no automated calls
  Given a maker sends a signing request to a counterparty without the app
  Then exactly one invitation is sent through a DLT-registered template
  And reminders follow the schedule unless the counterparty opts out
  And no automated voice call is placed

@P22-AT-28 @NN-46
Scenario: Retried approval from the outbox is applied once
  Given a checker approves offline and the outbox retries the request three times after reconnecting
  Then the server records one approval for the Idempotency-Key
  And the app shows the approval once

@P22-AT-29 @NN-26
Scenario: Analytics wait for consent
  Given a new user declines product analytics during onboarding
  Then no analytics event leaves the device
  And crash reports are sent scrubbed under the operational-necessity basis stated in the privacy notice

@P22-AT-30 @NN-48
Scenario: Listening to a machine translation carries a spoken disclaimer
  Given a Tamil machine translation of a notice without human review
  When the user taps Listen
  Then the audio begins with the statement that it is an unofficial machine translation and the original is authoritative

@P22-AT-31 @NN-50
Scenario: Store subscription shows renewal terms and an equally easy cancellation
  Given digital_sales_mode for Android is PLAY_BILLING
  When the user starts a Personal plan purchase
  Then the price, renewal period, renewal price and cancellation path are shown before payment
  And "Cancel subscription" is reachable in no more taps than purchase
```

## 13. Exit gate, deliverables and open items

**Exit checklist (v1, Wave 2; repeat for v2)**

- [ ] Parity matrix complete; `parity-check` green; Maestro flows for every `F` capability.
- [ ] Security review by P23: device binding, integrity, pinning, offline cache crypto, screen protection, OTA signing; mobile VAPT findings closed or accepted.
- [ ] Budgets met on the device lab (§4V); crash-free ≥ 99.7% in closed testing for 14 days.
- [ ] Appendix U mobile gate: automated label checks green; manual VoiceOver/TalkBack scripts for five journeys signed by `OPS_QA_REVIEWER`; disabled-user test round completed.
- [ ] Store packs: listings per locale, screenshots from the tutorial pipeline, App Privacy labels, privacy manifests, Data safety form, review notes, demo accounts, account-deletion path; `PLT_DPO` sign-off on the data inventory.
- [ ] Purchase-method classification approved by the owner and counsel; [VERIFY] items logged in `docs/compliance/verification-log.md` (NN-38).
- [ ] Release train and OTA governance live in `eng` with maker-checker.
- [ ] Settings registered (Appendix R); help keys `hlp.mob.*` registered; error codes registered.
- [ ] Export-map entries registered.

**Demo script:** install on a low-end Android device; sign in by OTP; enable biometrics; scan a stamp paper and an Aadhaar card (masking); share a WhatsApp export into a matter; draft a rent agreement in Hindi; negotiate one change with a guest on another phone via link; eStamp and eSign; open the signed copy offline in airplane mode; approve a company contract from a push; revoke the device from the web and show the wipe.

**Export-map entries (`xpt.export_map`, NN-11)**

| Record type | Folder in `LD-EXPORT-1.0` |
|---|---|
| `mob.device` | `99 System Data (CSV and JSON)/Devices.csv` (individual profile: `99 System Data/Devices.csv` — Appendix K §K.3.2) |
| `mob.push_preferences` | `99 System Data (CSV and JSON)/Notification Preferences.csv` (individual: `99 System Data/`) |
| `mob.capture_metadata` | `99 System Data (CSV and JSON)/Capture Metadata.csv` (individual: `99 System Data/`) (and alongside each document in its folder's evidence sub-folder where flagged as evidence) |
| WhatsApp import original and transcript rendition | The destination folder chosen by the user (e.g., `07 Disputes and Court Cases/<Case>/` for individuals; `03 Litigation and Disputes/…/` for companies) with the rendition labelled |
| `mob.store_receipt` (IAP mode) | `10 Receipts and Invoices/` (individual) or `10 Billing and Invoices/<FY>/` (company) |

**Open items (Appendix W candidates)**

| OI | Item | Owner |
|---|---|---|
| OI-P22-01 | Final bundle and application IDs, developer accounts under the operating entity (D-08), D-U-N-S number | [OWNER] |
| OI-P22-02 | Digital sales mode on iOS and Android (NOT_SOLD_IN_APP vs IAP/Play Billing/alternative billing) and the GST treatment of store sales | [OWNER] + [TAX MEMO] |
| OI-P22-03 | Verify Apple App Review Guidelines 3.1.1/3.1.3(b)–(e) and external-link entitlements for the India storefront; Google Play Payments policy and India alternative billing status | Mobile lead [VERIFY] + [COUNSEL] |
| OI-P22-04 | ESP/aggregator mobile support: system-browser flow vs native SDK; accessibility of ESP pages | P08 lead [VERIFY] |
| OI-P22-05 | Speech provider for Indic ASR/TTS with India-resident processing | P09 lead [VERIFY] |
| OI-P22-06 | Store category (Business vs Productivity) and age rating | [OWNER] |
| OI-P22-07 | Verify OTA clauses (Apple DPLA interpreted code; Google Play self-update policy) and Apple third-party-AI data-sharing disclosure rule | Mobile lead [VERIFY] |
| OI-P22-08 | Whether OH requires a native "ops approvals" space (Appendix X) | Pack lead / OH owner |
