# UDOFIN — Master Build Prompt for Claude Code

**Borrower mobile app (Android and iOS) and web platform for a multi-lender Lending Service Provider (LSP): consent-based onboarding, KYC and credit-data orchestration, neutral offer comparison, KFS, eSign and eStamp, mandates and repayments, borrower servicing, grievance redressal with Equator, recovery support, notices and ADR access (attachable per lender), DLG management, and operations and partner-lender portals**

Version 1.1 · 19 October 2026 · regulatory baseline aligned with Finbyx Master Prompt v1.4 and the Infrabyx Ecosystem Integration Specification v1.0 (33 RBI Directions and 1 guidance note) · Derived from the original Udofin prompt

---

## HOW TO USE THIS PROMPT (for the project owner — do not paste this box)

1. **Before Session 1:** Commit this entire file to the Udofin repository as `docs/00-master-prompt.md`. That means Parts 1–13, Appendices A–F and the Sources — everything below this box. Do not commit only Parts 1–13, because Phase 0 depends on the appendices.
2. **RBI source texts:** Commit the official RBI Direction PDFs (the same set supplied for Finbyx v1.3) to `docs/regulations/rbi/`. Part 8A cites them paragraph by paragraph, using the same requirement IDs as Finbyx so that the ecosystem keeps one register.
3. **Session 1:** Open Claude Code on the repository and type: *"Read docs/00-master-prompt.md in full, then execute Part 13 (Phase 0 only)."* Claude Code will audit and propose, then stop for your approval.
4. **After approval:** Claude Code commits `CLAUDE.md` (Appendix A), which points every later session to the master prompt.
5. **Every later session:** Work one phase (or one sub-module) at a time. Copy the matching "Instruction to Claude" from Part 12 and follow the companion runbook `docs/01-phase-runbook.md`, which gives the session command, the checks to run and the exit criteria for each phase. Approve each specification before code is written.
6. **Items marked [VERIFY]** are regulatory, platform-policy or vendor facts that need re-checking against the primary source before the related module is built. Claude Code is instructed to do this check and record the result in the regulatory register.
7. **Data residency:** Railway has no India region. Use synthetic data only until India-region hosting is in place (Part 10). No real borrower, KYC or bureau data may touch a non-India environment.
8. **Your tasks, not Claude Code's:** opening the Google Play Console and Apple Developer Program accounts (as an organisation, with D-U-N-S details), the Google Play India personal-loan declaration, app-signing keys, and all live provider contracts and credentials (KYC, bureau, eSign, eStamp, depositories, payment gateways, mandates, messaging). Claude Code builds mock and sandbox adapters first and prepares store listings, privacy labels and data-safety forms for your review.
9. **Ecosystem contract:** the Infrabyx Ecosystem Integration Specification v1.0 is the single source for events, APIs, data ownership and connectors. Commit it unchanged to `docs/ecosystem/infrabyx-integration-spec.md`, and a copy of the Finbyx master prompt (v1.4) to `docs/ecosystem/finbyx-master-prompt.md`. Part 5 summarises the specification for Udofin. Change the contract only through a versioned change agreed in every affected repository.
10. **Version 1.1 additions (19 October 2026):** Part 7A (recovery support, notices and ADR access; attachable per lender), Part 6.4–6.5 (product-wise origination workflows and the Loan Against Securities journey), proposed Products 11–15, and Phases 12b, 16b and 18b. Appendix E.3 lists every change from v1.0.

---

# PART 1 — ROLE AND WORKING AGREEMENT

Act as the Lead Software Architect, Senior Full-Stack Engineer, Mobile Application Engineer (Android and iOS), Web and PWA Engineer, Digital-Lending Domain Architect, Database Architect, Security Engineer, QA Lead and Technical Product Partner for the development of **Udofin**.

I am the project owner and product manager. I will set business objectives, approve product decisions and give instructions module by module. You will turn those instructions into architecture, specifications, code, tests and implementation documentation.

Do not behave merely as a code generator.

- Challenge incorrect assumptions, including mine. The original Udofin prompt contained several (Appendix E); expect more.
- Identify regulatory, conduct, privacy, financial-integrity and security risks before they are built in.
- Recommend better alternatives and explain material trade-offs before implementation.
- Do not agree with my proposals automatically. If a requested feature is impractical, insecure, legally questionable, commercially unviable, blocked by app-store policy or unnecessarily expensive, say why and propose a better approach.
- Remember throughout that **Udofin is an LSP, not a lender** (Part 4). Never design a screen, message, data model or API that implies Udofin lends, decides credit, owns the loan or holds borrower money.
- Ask as many questions as you need, but group them and ask only material ones. Where a sensible default exists, state the default and proceed after approval.
- Explain the logic in plain English before you write code. Break every change into small, reviewable commits on a feature branch (Part 11). Never claim a test passed unless it was run and its result is available.

---

# PART 2 — THE INFRABYX PRODUCT ECOSYSTEM AND UDOFIN'S PLACE IN IT

We are building four related products in the finance-cum-legal domain. Each product has its own database, deployment and release cycle. They share approved services and data only through well-defined, versioned interfaces, never through access to each other's tables.

| Product | Role | Relationship with Udofin |
|---|---|---|
| **Udofin** (www.udofin.com) — *this build* | Borrower-facing digital lending platform operated by an LSP: Android and iOS apps, borrower web app, operations portal, partner-lender portal and optional field app. Serves several partner regulated entities (REs) at once. | System of record for the borrower's journey on Udofin, Udofin's consents and evidence, its LSP-side records, its own accounts and the DLG it provides. Never the system of record for a loan. |
| **Finbyx** (www.finbyx.com) | Web-based LOS + LMS + accounting + collections + risk + regulatory reporting for NBFCs, HFCs, UCBs and banks. Staff-operated. | First certified lender connector (Part 5). Where an RE uses Finbyx, Finbyx takes and records the RE's regulated decisions and feeds Udofin's loan mirror. Udofin must not depend on Finbyx: other REs connect their own LOS/LMS or use the Udofin lender portal. |
| **LawDocsComply** (www.lawdocscomply.com) | Governance, risk and compliance (GRC) platform for entities regulated by RBI, SEBI and IFSCA. | Receives Udofin's control evidence (consent logs, DLA register, permission manifests, DLG disclosures, incident reports, grievance statistics) for the RE and for Udofin's own compliance. |
| **Equator Resolution** (www.equator.in) | Online dispute resolution (ODR): mediation, conciliation and arbitration. | Receives grievances that remain unresolved after the RE's process, where legally, contractually and procedurally appropriate. Cases reach Equator only by the RE's referral, under a pre-named institution clause or the borrower's written post-dispute consent, never by Udofin. The borrower reaches Equator from inside the Udofin app or web, with no separate app (Part 7A UR2). |

**Core difference between Udofin and Finbyx (keep this in every design decision):**

- **Udofin is borrower-led.** The customer starts on a phone or browser, registers with a mobile number, gives purpose-specific consents, completes KYC steps through authorised channels, sees matching offers from several lenders side by side, accepts a KFS, eSigns and eStamps, sets up a mandate, and then services the loan in the same app.
- **Finbyx is lender-led.** Branch staff, relationship managers, field officers and DSAs capture applications for one lender.
- **The RE decides; Udofin facilitates.** KYC compliance decision, credit decision, pricing, sanction, KFS, disbursement, asset classification, CIC reporting, recovery policy and grievance-redressal ownership stay with the RE (Part 4.2). Udofin carries data and evidence to the RE and presents the RE's outputs to the borrower.

**Shared services only through interfaces.** Ecosystem single sign-on (one Infrabyx OIDC identity) is optional and only for staff who need several products; authorisation stays per product. Borrower identities are not shared across products without the borrower's consent.

**Switches carried over from the original prompt (configuration, not rebuilds):**

| Switch | Options | Default |
|---|---|---|
| Compliance mode | (a) the RE uses LawDocsComply and Udofin pushes evidence there; (b) the RE uses the compliance module embedded in Finbyx; (c) a group uses one LawDocsComply instance for all its companies; (d) the RE uses a third-party GRC tool (for example MetricStream, IBM OpenPages, ServiceNow IRM or Archer) through the generic GRC connector (U18); (e) evidence-pack export only | (e) until a connector is configured |
| Grievance host | (a) grievances are managed in Udofin's lender portal by the RE's GRO; (b) in Finbyx; (c) in LawDocsComply; in every case the borrower raises and tracks them in Udofin and unresolved cases can go to Equator | Per RE; (b) where the RE is on Finbyx |
| Lender system | (a) Finbyx connector; (b) generic LOS/LMS connector; (c) Udofin lender portal only | Per RE |

---

# PART 3 — WHAT UDOFIN MUST BE

## 3.1 Customers and commercial models

Udofin serves two customer groups: **borrowers**, who never pay Udofin, and **partner REs** (NBFCs including HFCs and NBFC-MFIs, banks and other eligible lenders), who pay Udofin under an LSP agreement. Support these RE operating models:

1. **RE on Finbyx.** Decisions and servicing in Finbyx; Udofin connects through the certified Finbyx connector.
2. **RE on another LOS/LMS.** Udofin connects through the generic connector framework (Part 5.3) with a per-RE mapping and certification.
3. **Portal-only RE.** The RE takes its decisions in the Udofin lender portal and books loans in its own LMS; servicing data returns to Udofin by API or file (Part 5.4).
4. **White-label DLA** [assess]. Udofin's code published under the RE's brand and, normally, the RE's developer accounts. Legally this is then the RE's own DLA with Udofin as technology service provider, which changes the CIMS "owner" field, the multi-lender rules and the contract (Part 4.6–4.7). Produce an ADR and a legal note before building it.

**Commercial models (record in the LSP agreement registry, U1):**

- sourcing fee per disbursed loan, platform or SaaS fee per RE, servicing or collection fee where Udofin is appointed for that activity, and DLG fee where Udofin provides DLG (CF para 20(1));
- every fee is paid by the RE directly and is never charged to or collected from the borrower (CF para 10(4)), never deducted from a disbursement and never taken from recovery proceeds (CF para 10(5));
- fee differences between REs must never influence matching or ranking (CF para 7(2), 7(4)). The ranking engine has no access to fee or DLG data.

Track unit economics from day one (original "important addition" 10): verification, bureau, eSign, eStamp, messaging and cloud cost per application; funnel conversion by RE and product; support cost; revenue per disbursed loan; DLG losses.

## 3.2 Channels and user groups

Build separate experiences, not one generic menu. Each staff workspace shows its queues, SLAs, alerts and next actions.

| # | Channel | Users | Core jobs |
|---|---|---|---|
| A | Borrower mobile app (Expo + React Native; Android first on Google Play, then iOS on the App Store) | Borrowers | Registration, consent, KYC steps, application, offer comparison, KFS, eSign, eStamp, mandates, repayments, documents, loan dashboard, grievances, feedback |
| B | Borrower web app (Next.js, responsive, installable PWA) | Borrowers | The same journey as A wherever the browser allows; hand-off to the app where a step needs a native capability |
| C | Udofin operations portal (web) | Udofin operations, support, reconciliation, compliance, risk and finance teams | Lender onboarding, application exceptions, integration failures, queues, support, reconciliation, configuration, reporting, DLG, incident handling |
| D | Partner lender (RE) portal (web) | Each RE's credit, operations, compliance, grievance, finance and audit staff | The RE's own applications, products, eligibility configuration, decision queues (portal-only REs), documents, complaints, DLG, reports. Strictly limited to that RE's data |
| E | Collection and field-agent app (Expo; optional, later phase) | Udofin or agency staff, only where an RE appoints Udofin as recovery agent; assisted-onboarding staff | Allocated cases, contact logging, PTP, digital receipts, assisted onboarding. Not a copy of the borrower app |
| F | Platform administration (web) | Infrabyx platform administrators | Tenant set-up, roles, permissions, integration credentials, feature flags, theming, security monitoring, break-glass access |

**Why both an app and a web platform.** The original prompt chose mobile only because borrowers must share location and OTPs. Browsers can do both, and Aadhaar eSign, DigiLocker, eNACH and V-CIP all work through web flows. The web reaches borrowers who will not install an app, suits document-heavy secured products, and is a fallback if a store listing is suspended. Both are DLAs (Part 4.7). The app stays primary because device binding, attestation and native capture are stronger there.

**Parity matrix (initial; confirm in Phase 0):**

| Capability | Android app | iOS app | Borrower web/PWA | Notes |
|---|---|---|---|---|
| Registration and OTP login | Yes, SMS Retriever or User Consent API (no SMS permission) | Yes, one-time-code autofill | Yes, WebOTP API on Chrome for Android; `autocomplete="one-time-code"` autofill on Safari (iOS and macOS); else manual entry | Never request SMS read permission (Part 4.5) |
| Device binding | Yes, hardware-backed key plus Play Integrity | Yes, Secure Enclave key plus App Attest | Partial: WebAuthn passkey plus step-up OTP. Passkeys are usually synced across the borrower's devices by the platform account (iCloud Keychain, Google Password Manager), so they authenticate the person, not a device; record whether the credential is device-bound or synced | Web sessions get lower transaction limits by policy |
| Document capture | Camera with edge detection, onboarding and KYC only | Same | Browser camera or file upload of a user-chosen file | After onboarding use the system document or photo picker, never storage permission |
| Selfie and liveness | Yes | Yes | Yes, browser camera | Only as the RE's KYC process requires; no biometric template retained (Part 4.5) |
| One-time location | Yes, "only this time", approximate only | Yes, "allow once", reduced accuracy | Yes, Geolocation API, called once; the browser returns precise coordinates and cannot be asked for approximate only, and the site permission may persist, so reduce precision before storage and never re-read it | Onboarding/KYC only (Part 4.5); precise V-CIP geo-tag only in the RE's browser session (Part 10.3) |
| V-CIP by the RE's official | Yes, the RE's web session opened from the app (Part 10.3) | Yes | Yes, browser WebRTC | RE's infrastructure and official; Udofin only launches the RE's V-CIP session and hosts no V-CIP component (KYC para 27) |
| DigiLocker, CKYC identifier capture, PAN check | Yes | Yes | Yes | Through RE-authorised channels |
| Bureau and AA consent | Yes | Yes | Yes | AA consent screens are the AA's own |
| Offer comparison and KFS | Yes | Yes | Yes | Identical content and ranking on every channel (CF para 7) |
| Aadhaar eSign and eStamp | Yes, provider web view or redirect | Yes | Yes, redirect | Evidence captured server-side |
| eNACH mandate | Yes, net banking or debit-card redirect | Yes | Yes | Mandate in favour of the RE |
| UPI AutoPay and UPI payment | Yes, UPI intent | Yes, UPI app switch [VERIFY iOS intent support per PSP] | UPI intent on Android mobile browsers, QR on desktop; collect request only as P2M where the RE's PSP supports it (NPCI ended P2P collect from 1 Oct 2025) | Settles to the RE's account |
| Push notifications | Yes, FCM | Yes, APNs | Web push in Chrome, Edge and Firefox without installation; on iPhone and iPad only from iOS/iPadOS 16.4 and only after the borrower adds the web app to the Home Screen; SMS or email fallback for service alerts | Service messages separate from marketing consent |
| Biometric unlock | Yes, OS biometric prompt | Yes, Face ID or Touch ID | Passkey | Local OS feature; no biometric data leaves the device |
| Root, jailbreak and remote-access detection | Yes | Yes | Not possible; use risk signals and step-up | DPS para 68 used as a baseline by policy |
| Loan dashboard, books-of-accounts view, documents | Yes | Yes | Yes | From the loan mirror (U12, U25) |
| Grievance, AI assistant, Equator access | Yes | Yes | Yes | No separate Equator app |
| Field app features | No | No | No | Channel E only |

**Deep links and hand-off rules:**

- Use verified Android App Links and iOS Universal Links on a Udofin-controlled domain; never custom URL schemes for anything sensitive.
- A web-to-app hand-off uses a QR code or link carrying a single-use, short-lived (for example 5 minutes), journey-bound token. It never carries PII, OTPs or document references.
- The receiving channel re-authenticates the borrower before resuming. The journey state lives on the server, so the borrower resumes at the same step on any channel.
- If a step needs a native capability that the browser lacks, hand off; never weaken the control to keep the borrower on the web.
- Every RE-specific link opens the RE's own website disclosures page where required (CF para 9(5)).

## 3.3 Borrower journey design

1. **Three to four interactions to begin an application** (original target), not to complete KYC, underwriting and execution. Default start: (1) enter mobile number and accept the platform notice; (2) verify OTP; (3) choose a product and enter amount and tenor; (4) give the purpose-specific consents needed for a first eligibility check. Everything else is progressive.
2. **Progressive disclosure.** Ask for each data item only at the step where it is needed, and say why it is needed and which lender will receive it (CF para 13(3)).
3. **Minimum mandatory data.** Age, occupation and income are captured for every application because the RE must assess creditworthiness on them (CF para 8(1)). Household income is captured for every collateral-free loan because of the microfinance test (CF para 51; Part 6).
4. **Resumable journeys.** Server-side journey state with explicit states and transitions; safe resumption after an app kill, network loss or channel switch; expiry rules for stale consents, offers and KFS validity.
5. **Permission at the point of use.** Request a device permission only at the step that needs it, after an explanation screen, and release it afterwards (Part 4.5).
6. **No shortcuts past controls.** Fewer clicks must never bypass verification, consent, disclosure, the KFS or the RE's underwriting.
7. **Transparency.** Show who the lender is, that Udofin is the RE's LSP, every charge, the APR, the cooling-off right and the grievance route at the moment they matter. After disbursal, give the borrower a "books of accounts" view of every amount disbursed, charged, paid and outstanding (U25).
8. **Accessibility.** WCAG 2.2 AA as the target on web and the equivalent platform accessibility APIs on mobile; dynamic type, screen-reader labels, sufficient contrast, no colour-only signals, and generous touch targets.
9. **Multilingual.** English and Hindi in the MVP; major regional languages next. The KFS must be in a language the borrower understands (RBC para 29(1)), so the language choice is stored and passed to the RE.
10. **Clear errors and recovery.** Every error says what happened, whether data was saved and what to do next. Never show raw provider errors.
11. **Feedback.** Lightweight feedback prompts after key events (application, disbursal, grievance closure) and a permanent feedback entry point (U16).

## 3.4 Customisation philosophy

Provide customisation for every product, journey, document, integration, communication, report and screen, through a governed model:

| Layer | Who can change it | Examples |
|---|---|---|
| **Standard core** (code, platform-controlled) | Infrabyx, by release | Consent engine, permission policy, offer-neutrality engine, money-flow guards, audit, security, tenant isolation |
| **Tenant-safe configuration** (UI, maker-checker inside the RE or Udofin) | RE administrator or Udofin operations | Branding within the theme tokens, document checklists, communication templates (non-regulatory parts), support hours, report schedules, journey copy within approved slots |
| **Platform-approved configuration** (Udofin approval and validation rule) | Udofin product and risk teams on an RE request | New product template, eligibility routing rules, connector mapping, new data pull, journey step order, feature flags per RE |
| **Legal-review configuration** (RE compliance sign-off plus Udofin legal review) | RE CCO and Udofin legal | Consent and notice wording, KFS template version, cooling-off period, privacy-policy text, DLG terms, recovery-contact policy, marketing consent wording, Equator referral wording |
| **Controlled extensions** | Infrabyx, or an RE developer through the connector SDK | Custom connector adapters, webhooks, custom report definitions |

**Regulatory guard-rails cannot be overridden by any configuration.** Examples:

- no access to files and media, contacts, call logs or telephony functions (CF para 13(1));
- data stored only in India (CF para 14(4));
- no disbursal to, or repayment through, an Udofin account (CF para 10(1)–(3));
- no fee charged to the borrower by Udofin (CF para 10(4));
- every matching offer shown, unmatched lenders named, and ranking only on a pre-disclosed metric (CF para 7);
- no execution before a KFS has been shown and acknowledged (RBC para 29(1));
- a cooling-off exit option of at least one day (CF para 11(1));
- grievance contacts and the CMS escalation route always visible (CF para 12);
- no exposure of one RE's data to another.

Every configuration change is validated against these guard-rails, versioned, effective-dated and audited.

## 3.5 MVP and expansion

**MVP (pilot):**

- Products 1 (Personal Loan) and 2 (Payday / short-tenure loan, subject to the app-store gate in Part 6).
- Android app + borrower web app + operations portal + lender portal.
- One or two pilot REs: one on Finbyx, one on a generic LMS connector.
- iOS follows after the pilot gate (Phase P; App Store release engineering is prepared in Phase 17), because App Store review needs a stable product and complete disclosures.

**Expansion, in order (Part 12):** secured products (LAS, Home, LAP, Vehicle; Phase 18); additional product templates (Gold, Business/MSME, Microfinance, Supply-chain/TReDS invoice finance, Education; proposed; Phase 18b); specialist products only after a feasibility note is approved (Phase 19); field app, analytics, broader AI and marketing (Phase 20); scale hardening and AWS migration (Phase 21).

**Scale.** Design for millions of borrowers and many REs from the start: stateless API instances, queue-based integrations, read replicas for the loan mirror, partitioned event and audit tables, CDN-served static assets, and load tests at ten times the pilot volume before each expansion (Part 10).

---

# PART 4 — UDOFIN'S REGULATORY POSITION AND OPERATING MODEL

This Part sets the operating model. The detailed, paragraph-level requirements are in Part 8A (8A.1 CF, 8A.2 CIR, 8A.3 KYC, 8A.4 AA, 8A.5 MFI, 8A.6 RBC, 8A.7 OUT, 8A.8 CYB, 8A.9 FRM, 8A.11 DPS). Distinguish law, interpretation and recommendation everywhere; label interpretations as such.

## 4.1 Udofin is an LSP, not a lender

- **Definition.** An LSP is "an agent of an NBFC (including another lender) who carries out one or more of NBFC's digital lending functions, or part thereof, in customer acquisition, services incidental to underwriting and pricing, servicing, monitoring, recovery of specific loan or loan portfolio on behalf of the NBFC in conformity with extant outsourcing guidelines" (CF para 4(1)(xix)). Udofin performs customer acquisition, services incidental to underwriting, servicing support, monitoring support and, only where separately appointed, recovery.
- **The RE stays fully responsible.** The NBFC "shall remain fully responsible and liable for all acts and omissions of the LSP" (CF para 6(7)); the LSP arrangement is a contract that defines roles, rights and obligations (para 6(1)), entered after enhanced due diligence (para 6(2)) and reviewed periodically (para 6(3)). Udofin must therefore be built to be audited by every RE (U18).
- **Outsourcing limits bind the design.** An NBFC may not outsource decision-making functions such as determining compliance with KYC norms or giving sanction for loans (OUT para 15; KYC para 13). Udofin's systems may compute, collect and present, but every regulated decision is recorded as taken by a named RE user or an RE-owned rule set (Part 4.2, 5.4).
- **Applicability by RE type.** CF applies to NBFCs and HFCs (CF para 3(1)). Bank REs follow the corresponding Commercial Banks directions, which were not supplied [VERIFY: bank digital-lending and KYC directions before onboarding a bank RE]. Keep the rule packs per RE type.
- **Payment aggregator boundary.** A PA that also performs LSP functions must comply with the Directions; the supplied text says "Chapter IV" in CF para 4(1)(xix), evidently meaning Chapter III (Digital Lending) [VERIFY; record in errata]. Udofin must not obtain a PA licence role in its loan flows (Part 4.3).
- **Never imply lending.** Copy, store listings, push messages and screens say "loans from [RE name], facilitated by Udofin, a lending service provider". No "Udofin loan", "Udofin credit limit" or "approved by Udofin". The CIMS listing is not an RBI endorsement and must not be presented as one (CF para 18(6)).

## 4.2 Responsibility matrix

Interpretation, to be confirmed in each LSP agreement. "Udofin acts" means as the RE's agent under the contract; the RE remains responsible (CF para 6(7)).

| Activity | RE (partner lender) | Udofin (LSP) | Contract / source |
|---|---|---|---|
| Sourcing and marketing | Approves products, eligibility and marketing content; owns the customer relationship once onboarded | Acquires and onboards borrowers; runs approved campaigns with consent; neutral offer display | LSP agreement; CF paras 6, 7; RBC paras 98–101 |
| KYC | Takes the KYC compliance decision; risk categorisation; CKYCR download and upload; V-CIP official; Aadhaar e-KYC only if notified under s.11A PML Act | Runs the technology: capture, OKYC or DigiLocker flows, PAN check, liveness, evidence packaging; never decides | KYC paras 13, 23, 25, 27; OUT para 15 |
| Credit bureau enquiry | Pulls bureau data under its own CIC membership and owns the enquiry | Captures borrower consent and the purpose; triggers the RE's pull through the RE's credentials or connector; displays only what the RE permits | CIR para 6; CICRA [VERIFY Udofin's access route] |
| Account Aggregator | Is the FIU; consent artefact names the RE | Technology service provider to the RE; launches the AA journey; never an FIU itself | AA paras 8(12), 27–28 [VERIFY Sahamati TSP rules] |
| Underwriting | Credit policy, BRE rules, decision, deviations | Collects and pre-validates inputs; runs the RE's rule set only as hosted for the RE (portal-only REs); no DLG input to any rule | CF paras 8, 20(2); OUT para 15 |
| Pricing | Sets rate, charges, penal charges, APR | Displays the RE's figures unchanged; independent APR recomputation check before display | RBC paras 29–30; CF para 7(3) |
| KFS | Issues the KFS with unique proposal number and validity; owns its content | Displays, explains, records acknowledgement and acceptance time, passes them to the RE | RBC para 29; CF para 9(1) |
| Sanction | Sanctions and issues the sanction letter | Displays and delivers | OUT para 15 |
| Loan agreement | Owns the template and contract; executes on its letterhead | Orchestrates borrower execution and evidence capture | CF para 9(3); IT Act |
| eSign and eStamp | Party to the document; may hold the ESP and stamp-vendor contracts | Orchestrates the borrower's eSign and the eStamp purchase on the RE's account; stores provider evidence; never marks "signed" without it | LSP agreement; IT Act s.3A; state Stamp Acts [VERIFY per state] |
| Disbursement | Disburses from its account to the borrower or permitted end-beneficiary | Shows status only; never touches funds | CF para 10(1) |
| Mandates | Mandate in its favour, with its sponsor bank and utility code | Orchestrates registration and shows status | CF para 10(2)–(3) |
| Repayment collection | Receives every payment in its own account | Generates payment instructions on the RE's merchant account; shows status and receipts | CF para 10(2)–(4) |
| Reminders | Sets content and policy; owns penal-charge disclosure | Sends approved reminders and alerts on the RE's behalf | RBC para 30; CIR para 34(1)(i) |
| Recovery | Owns recovery policy; appoints agents; sends agent particulars before contact | Only if appointed by an explicit recovery-agent contract; follows RBC conduct rules | CF paras 6(5), 9(6), 10(5); RBC paras 93–100; RBC Third Amendment paras 100A–100AB from 1 Jan 2027 (Part 7A) |
| Settlement, ADR and legal action | Approves every settlement one level above the sanctioning authority; refers disputes to ADR; issues legal notices and conducts litigation in its own name | Relays settlement requests and shows the RE's offers, notices and ADR status as the RE permits; never approves, refers or issues (Part 7A) | RSA paras 16(5), 87–100; OUT para 15; CF para 12 |
| DLG | Accepts DLG under its Board policy; invokes; classifies and provisions the loans | Provides DLG in a permitted form; auditor-certified declaration; monthly website disclosure | CF paras 19–29 |
| Grievance | Owns redressal; GRO and Internal Ombudsman; 30-day clock; refers disputes to ADR | Own nodal grievance officer for LSP-related complaints; lodging on the DLA; routing and tracking; ADR status and access for RE-referred cases (Part 7A UR2) | CF para 12 |
| CIC reporting | Reports all DLA lending, including household income for microfinance | Supplies captured data (for example household income) with evidence | CF paras 17, 54 |
| CIMS DLA reporting | Reports every DLA, certifies the para 18(4) points | Maintains the DLA register and supplies the data; keeps the DLA compliant | CF para 18 |
| Data storage | Responsible for borrower data privacy and security on an ongoing basis | Stores only basic minimal data within the agreement's scope; India-only storage | CF para 14(1), 14(4) |
| Security incidents | Reports to RBI within the regulatory timeline | Reports to the RE without undue delay (internal target 2 hours) so the RE can report to RBI within six hours of Udofin's detection | OUT para 61; CYB (Part 8A.8) |
| Audit | Audits Udofin; RBI may inspect | Gives access to books, records and systems; supports audits and inspections | OUT para 34(ii), (vii)–(ix) |

## 4.3 Fund flows

**Rules (CF para 10):**

- **Disbursal** always goes from the RE's account into the borrower's bank account. The only exceptions are disbursals exclusively under a statutory or regulatory mandate, flows between lenders in co-lending, and disbursals for a specific end use paid directly into the end-beneficiary's bank account (for example a hospital, dealer, builder or the existing lender being repaid). Never into a third-party account, including Udofin's (para 10(1)).
- **Salary advance proviso:** the employer may repay by salary deduction directly from the employer's bank account to the RE, with no LSP control over the funds (para 10(1) proviso). Not in the MVP.
- **Repayment** goes directly into the RE's bank account, with no pass-through or pool account of any third party, including Udofin (para 10(2)); no third party controls the flow (para 10(3)). In co-lending, only the co-lenders may control the escrow (para 10(1), Note).
- **LSP fees** are paid by the RE directly and never collected from the borrower (para 10(4)).
- **Cash recovery** on delinquent loans is allowed only where Udofin is the appointed recovery agent; it must be reflected in full in the borrower's account the same day, and no LSP fee may be taken from the proceeds (para 10(5)).

**Payment gateways.** Integrate Razorpay, Cashfree and PayU (and Juspay as optional orchestration) behind one `PaymentCollectionGateway` interface, always on **the RE's merchant account**: the RE is the merchant of record, settlement goes to the RE's bank account, and Udofin holds only API credentials scoped by the RE. Whether a PA's regulated escrow or nodal account counts as a third-party "pool account" under para 10(2) is an interpretation question [VERIFY: legal opinion per PA model].

**Stripe and PayPal.** The original prompt asked for them. Keep adapter interfaces, but do not use them for domestic loan repayments until verified: Stripe's India availability is restricted and PayPal has exited domestic Indian payments [VERIFY: current status]. They may suit Udofin's own cross-border SaaS billing to REs, not borrower EMIs. Record this in an ADR.

**Build guards:** the configuration validator rejects any beneficiary or settlement account that is not the borrower's, an approved end-beneficiary or the RE's; payment links and VPAs are generated per RE; a daily reconciliation (`DailyReconciliationFile`, Part 5) proves that no money touched Udofin.

## 4.4 DLG and collections are separate

The original prompt said that because Udofin gives 5% FLDG it must handle collections. That is wrong: a DLG arrangement does not by itself give Udofin any collection right or duty.

- **DLG (CF paras 19–29)** is a loss-sharing contract. Udofin must be a company under the Companies Act, 2013 (para 19) [VERIFY Udofin's legal entity], provide cover only in a permitted form (para 23), within 5% of the amount disbursed from a fixed DLG set (para 24), with an auditor-certified declaration (para 20(3)), accept invocation within 120 days overdue without reinstatement (paras 25(4), 27(1)), and publish a monthly disclosure (para 28). Detail in U14 and Part 8A.1.
- **Collections** come only from an explicit recovery-agent or outsourcing contract with the RE, recorded in U1 with effective dates, scope (reminders only, tele-calling, field), territories, controls and fees. Without it, Udofin sends only RE-approved reminders and payment links. With it, Udofin follows the RE's recovery policy and the RBC conduct rules (U13; Part 8A.6).
- **Conflict control:** Udofin's DLG exposure creates an incentive to steer borrowers and to collect aggressively. The matching and ranking engines must not read DLG data, and collection actions must pass the same contact-policy engine whether or not DLG covers the loan.

## 4.5 Data and device rules

**What the text says (CF para 13(1)):** the RE must ensure that collection of data by its DLA and its LSP's DLA "is need-based and with prior and explicit consent of the borrower having audit trail", and that the DLAs "desist from accessing mobile phone resources like file and media, contact list, call logs, telephony functions, etc. A one-time access can be taken for camera, microphone, location or any other facility necessary for the purpose of on-boarding / KYC requirements only, with the explicit consent of the borrower."

**Related rules:** give, deny, restrict, revoke and delete options (para 13(2)); purpose disclosed at each stage (para 13(3)); explicit consent before sharing with any third party unless law requires it (para 13(4)); the LSP stores only basic minimal data needed under the agreement (para 14(1)); a published storage, retention and destruction policy (para 14(2)); no biometric data stored or collected unless statute allows (para 14(3)); storage only in India, with anything processed abroad deleted and repatriated within 24 hours (para 14(4)); a comprehensive privacy policy listing third parties that collect data through the DLA (para 15).

**DPDP.** The Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 apply alongside the RBI rules [VERIFY: notification and phased commencement — Rules notified November 2025, Consent Manager provisions from November 2026, most obligations from May 2027, per Finbyx v1.3]. Determine in Phase 0, per processing purpose, whether Udofin acts as Data Fiduciary (its own platform account, marketing, fraud prevention) or as Data Processor for the RE (application data shared with that RE), and whether Udofin may be notified as a Significant Data Fiduciary [assess]. Where the RBI rule is stricter, the RBI rule wins.

**Interpretations adopted (record each in the regulatory register):**

- "One-time" means requested at the step that needs it, using the platform's one-time grant where available, and not used again. Udofin does not keep a standing permission for later use.
- After onboarding and KYC, document uploads (for example income proof for a top-up or evidence for a grievance) use the system document or photo picker, which gives access only to the file the borrower picks and needs no storage permission [VERIFY: legal view that this is not "accessing file and media"].
- A device's own biometric unlock (the OS keeps the template; Udofin receives only a yes or no) is not collection or storage of biometric data by Udofin [VERIFY]. Face-match templates created for KYC are discarded after the match; only the photo required as KYC evidence is kept for the RE [VERIFY: whether a face template is "biometric data" for para 14(3)].

**Permission policy (Android manifest and iOS entitlements are reviewed in CI against this table):**

| Permission | Allowed? | When | Why |
|---|---|---|---|
| Camera | Yes, one-time | Onboarding and KYC steps only (document capture, selfie, liveness, V-CIP) | Permitted for onboarding/KYC with explicit consent (CF para 13(1)) |
| Microphone | Yes, one-time | V-CIP session run by the RE's official only | Permitted for onboarding/KYC (CF para 13(1)); KYC para 27 |
| Location (approximate only, foreground) | Yes, one-time | Onboarding or KYC step only (address pre-fill, fraud signal or the RE's geo-tagging need); the precise V-CIP geo-tag is captured only in the RE's browser session (Part 10.3) | Permitted for onboarding/KYC (CF para 13(1)); ACCESS_FINE_LOCATION is prohibited for personal-loan apps on Google Play (Part 8.2) |
| Background location | No | Never | Not necessary for onboarding/KYC |
| Files, photos and media (storage, media read permissions) | No | Never; use the system picker | "File and media" access barred (CF para 13(1)) |
| Contacts | No | Never | Barred (CF para 13(1)); also no "references from phonebook" feature |
| Call logs | No | Never | Barred (CF para 13(1)) |
| SMS read, receive or send | No | Never; use the SMS Retriever or User Consent API and one-time-code autofill | Telephony functions barred; no SIM binding by outbound SMS |
| Phone state, phone number, IMEI, telephony | No | Never | Barred (CF para 13(1)); device binding uses an app-generated key |
| Notifications | Yes, opt-in | After registration, with separate service and marketing choices | Service alerts; marketing only with consent |
| Biometric prompt (local unlock) | Yes, optional | App unlock and step-up, if the borrower chooses | OS-held template; no data to Udofin |
| Installed-apps list (query all packages) | No | Never; declare only a narrow list of named remote-access apps to detect | Minimal data; remote-access detection per DPS para 68(2)(iv) as baseline |
| Accessibility service, overlay (draw over apps) | No | Never | Abuse risk; not needed |
| Advertising ID | No by default | Only if marketing attribution is approved and consented | Minimal data (DPS para 68(2)(vii) baseline) |
| Bluetooth, nearby devices, calendar | No | Never | Not needed |

Any change to this table is a legal-review configuration (Part 3.4), needs an ADR and must also pass the Google Play and App Store data-safety declarations (Part 8.2).

## 4.6 Multi-lender marketplace rules

Udofin has agreements with several lenders, so each RE must ensure that Udofin follows CF para 7:

- **All matching offers in one digital view,** and the **names of unmatched lenders disclosed** in the same view (para 7(1)).
- **Consistent, documented matching.** Udofin may choose its matching mechanism, but it must treat similarly placed borrowers and products alike, and the mechanism and every change to it must be documented (para 7(2)). Build: a versioned `matching_mechanism_version` with a plain-language description, stored with every offer set shown.
- **Comparable content.** Each offer shows lender name, amount, tenor, APR, monthly repayment obligation and penal charges (if any), so that the borrower can compare fairly, plus a link to that lender's KFS (para 7(3)).
- **Neutrality.** Content must be unbiased and objective, must not directly or indirectly push a lender, and must not use dark patterns as defined in section 2(e) of the CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 (para 7(4) and Note). Ranking on a publicly pre-disclosed metric is allowed. Build: default ranking by APR (ties by monthly repayment obligation), the metric published on the website and in the app before the offers appear, no pre-selected offer, no "recommended" or "best" badge, equal visual weight, no countdown timers or false scarcity, no paid placement inside the offer view.
- **Inputs to matching** come only from the borrower's request, the RE's published eligibility rules (`ProductCatalogPublished`) and each RE's `EligibilityCheck` response. Never from fees, DLG exposure or conversion targets.
- **No automatic limit increase** without an explicit, evaluated and recorded borrower request (CF para 8(2)); pre-approved top-up campaigns lead to a request, not an increase.
- **White-label and single-lender modes.** Whether para 7 applies to a DLA that shows only one RE, when Udofin has agreements with several lenders, is an interpretation question [VERIFY: legal opinion]. Default: apply para 7 to every Udofin-branded DLA.
- **Store-policy filtering versus para 7(1).** Channel filters (tenor of 60 days or less in both store apps; APR above 36% including fees in the iOS app; Part 10.2 principle 30) mean a store-app borrower may not see every matching offer. Name each filtered lender in the unmatched list with the reason "not available in this app; available on the web" and obtain a legal opinion that this satisfies para 7(1) [VERIFY].

## 4.7 DLA registration and disclosures

- **Every borrower-facing channel is a DLA** of each partner RE ("mobile and / or web-based applications"; CF para 4(1)(x)). Keep a **DLA register** with one line per DLA per platform per RE (Udofin Android, Udofin iOS, Udofin web, and each white-label DLA), carrying the CIMS Annex-I fields: name, owner (self or LSP), platform, link, GRO name, email, telephone and mobile, and the RE's website (CF para 18(1), Annex-I). Supply each RE with its extract and every change, so that the RE can update CIMS when a DLA is added or ceases (para 18(2)).
- **Certification support.** Give each RE the evidence for the four points its CCO certifies (para 18(4)): link from the DLA to the RE's website; Udofin's nodal grievance officer, shown prominently on the DLA; data collection and storage compliant with paras 13–14; and consistency with the RE's website disclosure under para 9(4).
- **Links and disclosures in the DLA:** a link to each partner RE's website disclosure page (para 9(5)); GRO details of the RE and of Udofin (para 12(2)); complaint lodging (para 12(3)); privacy policy listing third parties that collect data through the DLA (para 15); data storage and destruction policy (para 14(2)); the list of partner REs and the activities Udofin performs for each (supporting para 9(4)(ii)).
- **Website.** Udofin's website carries the same disclosures, the ranking metric (Part 4.6) and the monthly DLG disclosure (para 28).
- **App stores.** Google Play's Financial Services policy for personal-loan apps in India and Apple's App Review Guidelines for lending apps impose their own requirements: declarations, RE names, APR disclosure, no loans repayable in full in 60 days or less on either store, and a 36% maximum APR on the App Store. Re-check the current text before each submission (Part 8.2).
- **Never** describe the CIMS listing as an RBI registration, licence or approval (para 18(6)).

---

# PART 5 — UDOFIN ↔ LENDER AND ECOSYSTEM INTEGRATION (FINBYX, ANY LOS/LMS, EQUATOR, GRC AND THIRD PARTIES)

Udofin builds the **LSP side** of the ecosystem contract. **Canonical source (v1.1):** the Infrabyx Ecosystem Integration Specification v1.0 (`docs/ecosystem/infrabyx-integration-spec.md`, committed unchanged in every Infrabyx repository) is the single source for event names and schemas, APIs, data ownership, the security profile and connector certification. The tables in this Part summarise it for Udofin; where they differ, the specification wins and the difference is raised as a contract change, never coded silently. The event names below are identical to the specification and to Finbyx Part 5.2. Finbyx is the first certified connector; every other RE system connects through the same contract or through an adapter that translates to it.

## 5.1 Principles

1. **Ownership of records:**
   - **The RE's system (Finbyx or another LOS/LMS) is the system of record for:** the credit decision, sanction, KFS content, loan account, schedule, ledger, asset classification, CIC reporting and provisioning.
   - **Udofin is the system of record for:** the borrower's journey on Udofin, Udofin's consents and their evidence, KYC and signing evidence it captured, its DLA register, its grievance cases as the LSP, its DLG records and its own accounts.
   - Udofin's loan mirror (U12) is a read model. It is never authoritative; when it disagrees with the RE, the RE wins and the difference is a reconciliation break.
2. **Contracts:** per the Ecosystem Integration Specification: CloudEvents 1.0 envelope; OpenAPI 3.1 and AsyncAPI 3.0; a JSON Schema 2020-12 registry with backward-compatibility checks; mTLS plus RFC 9421 HTTP Message Signatures on every message (detached JWS for documents and regulated messages); OAuth 2.1 client credentials, and FAPI 2.0 where an API acts on the borrower's behalf; Standard Webhooks for external webhooks; `Idempotency-Key` on every POST; India-only data residency; every call idempotent, timestamped and replay-protected; schemas validated at both ends; contract tests (Pact) in both pipelines.
3. **Money flows:** Udofin never sends or receives loan money (Part 4.3). The contract carries instructions and status only. Udofin rejects any RE configuration that routes funds through it.
4. **Data minimisation and consent:** Udofin sends an RE only data the borrower consented to share with that RE, for that purpose, with the consent artefact reference (CF para 13(4)). Data goes to the RE that the borrower chose, not to every matching RE; eligibility checks before the choice use the minimum fields the RE needs.
5. **Failure containment:** if an RE system is unavailable, Udofin keeps working for every other RE and shows the borrower an honest status; the reverse is also true (Part 5.5).

## 5.2 Interface catalogue (minimum)

| Direction | Interface | What Udofin sends, or must do on receipt |
|---|---|---|
| RE → Udofin | `ProductCatalogPublished` | Store as an immutable product-offer version per RE; validate against guard-rails (cooling-off ≥ 1 day, KFS template present, grievance contacts, DLA disclosures); make live only after the RE's own go-live approval (for ML/UL REs, CCO evaluation of every new product: CMP paras 15(2), 31) and Udofin's platform checks; withdraw the old version from new journeys at its effective date |
| Udofin → RE | `EligibilityCheck` (sync API) | Send the minimum consented data for an indicative check by the RE's BRE; store the request, response, rule-version reference and timestamp; feed only the response into matching (Part 4.6); time out to "lender unavailable", never to a guessed result |
| Udofin → RE | `ApplicationSubmitted` | Send the application, KYC evidence references (evidence only; the KYC decision is the RE's: KYC para 13), the OTP-e-KYC declaration where used (KYC para 25(8)), bureau and AA references, documents and consent artefacts; idempotency key per application |
| RE → Udofin | `ApplicationStatusChanged`, `AdditionalInfoRequested`, `DecisionMade` | Update journey state only through allowed transitions; notify the borrower; open the information request as a task; show sanction or rejection with the RE's reason codes in plain language; never infer a decision |
| RE → Udofin | `KFSIssued`, `SanctionLetterIssued` | Store the documents with hashes; show the KFS with proposal number and validity expiry; run the independent APR check and raise an exception (not a silent fix) on a mismatch; record view, explanation acknowledgement and acceptance time |
| Udofin → RE | `BorrowerAccepted`, `ESignCompleted`, `EStampCompleted` | Send acceptance within KFS validity, and provider evidence (transaction IDs, certificate, signed-document hash, timestamps, stamp certificate number). **Never a bare "signed=true" flag** |
| Udofin → RE | `MandateRegistered` | Send UMRN, sponsor bank, mandate type, limits and validity, for a mandate in the RE's favour |
| RE → Udofin | `LoanDisbursed`, `DisbursementFailed` | Mark disbursed only on this event with UTR, amount and date; start the cooling-off clock display; create the loan mirror; on failure, show status and the RE's next step |
| Udofin → RE | `CoolingOffExitRequested` | Send the borrower's exit request within the period; show the RE's payable amount (principal plus proportionate APR, plus any processing fee disclosed in the KFS: CF para 11) and a payment instruction to the RE's account |
| RE → Udofin | `ScheduleIssued`, `ScheduleChanged`, `DueReminderTrigger`, `PaymentReceived`, `PaymentBounced`, `DPDChanged`, `AssetClassificationChanged`, `LoanClosed`, `NOCIssued` | Update the loan mirror; send RE-approved reminders and receipts; show the NOC; never show asset classification to the borrower unless the RE approves the wording |
| RE → Udofin | `CollectionAllocated`, `CollectionDeallocated` | Accept only if an active recovery-agent contract exists for that RE, scope and territory; apply the contact-policy rules carried in the allocation; confirm that the agent's particulars were sent to the borrower before first contact (CF para 9(6)) |
| Udofin → RE | `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued` | Send activity with timestamps, recordings references and geo-tags from agent devices; cash receipts reflected to the RE the same day (CF para 10(5)) |
| Both | `GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated` | Route to the RE's GRO under the grievance-host switch; keep one reference across systems; show the CMS escalation route after 30 days or on rejection (CF para 12(4)); record Equator referrals |
| Both | `DLGArrangementRegistered`, `DLGInvocationRaised`, `DLGInvocationSettled`, `DLGPortfolioCoverage` | Keep Udofin's own DLG records in U14 (Udofin is their system of record, Part 5.1) and reconcile them with the RE's DLG ledger; reconcile cover, invocations and recoveries; feed Udofin's accounts and monthly disclosure |
| Both | `DailyReconciliationFile` | Exchange applications, disbursals, payments, fees, collections and DLG positions; produce break reports in the ops portal |

**Events adopted in v1.1 (formerly contract gaps).** The v1.3 Finbyx catalogue had no event for consent withdrawal or data-erasure requests passed to the RE, for Udofin security incidents notified to the RE, or for Udofin's monthly DLG disclosure. v1.0 proposed `ConsentWithdrawn`, `DataPrincipalRequest`, `SecurityIncidentNotified`, `DLGDisclosurePublished`, `RiskSignalRaised` (fraud and early-warning signals to the RE; 8A.9) and `SettlementRequested` (a borrower's settlement request relayed to the RE; 8A.13) as a contract change; the Ecosystem Integration Specification v1.0 adopts all six. Implement each in the phase that needs it (Phase 3b consent events, Phase 13 DLG disclosure, Phase 16 incidents and risk signals, Phase 12b settlement). Never invent an event silently; raise any further gap as a versioned contract change.

**New canonical event domains (v1.1).** Udofin produces only the events marked as produced; it consumes the others only where Part 7A or Part 6.4 says so, filtered by the RE's visibility policy.

| Domain | Events | Udofin role |
|---|---|---|
| Collateral | `CollateralPledgeRequested`, `CollateralPledgeCreated`, `CollateralValuationUpdated`, `MarginCallRaised`, `MarginCallCured`, `CollateralInvoked`, `CollateralReleased` | Consumes all seven from the RE (`CollateralPledgeRequested` is RE → Udofin and starts the borrower's OTP and DP or RTA steps), plus `CollateralPledgeFailed`, `CollateralChargeRegistered` and `MarginCallLapsed`; produces only `CollateralHoldingsShared` (holdings with consent reference); calls the eligibility-quote, cure-intent, `DrawdownRequested` and facility-summary APIs (Integration Spec Parts 6.3, 6.5, 7.3; Part 6.5) |
| Co-lending and transfer | `CoLendingSplitConfirmed`, `ClassificationSynced`, `LoanTransferred`, `ServicerChanged` | Consumes `LoanTransferred` and `ServicerChanged` (updates the loan mirror, payment instructions and the single point of interface: TDCR paras 104–105, 117); `CoLendingSplitConfirmed` and `ClassificationSynced` pass only between the co-lenders (Integration Spec 6.6), so Udofin sees their effect through `AssetClassificationChanged` and the loan mirror |
| Recovery | `RecoveryCaseOpened`, `RecoveryStrategyChanged`, `LegalNoticeIssued`, `NoticeServiceUpdated`, `SettlementOfferIssued`, `SettlementApproved`, `SettlementBreached`, `AssetRepossessed`, `AuctionScheduled`, `AuctionConcluded`, `RecoveryReceiptPosted`, `RecoveryCaseClosed` | Consumes (Part 7A UR1, UR3); produces `NoticeServiceUpdated` only for delivery on Udofin's own channel and `SettlementOfferAccepted` (acceptance evidence); also consumes `SurplusRefunded` (Integration Spec 6.8) |
| ADR (Equator or another provider) | `ADRReferralCreated`, `ADRConsentRecorded`, `ADRNeutralAppointed`, `ADRHearingScheduled`, `ADRCaseStatusChanged`, `ADROutcomeRecorded`, `ADROutcomeComplianceUpdated` | Consumes only; never holds the referral scope (Part 7A UR2) |
| Litigation | `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled`, `OrderRecorded`, `LitigationCaseClosed` | Consumes only, as RE-permitted projections (Part 7A UR3); `OrderRecorded` is routed only to LawDocsComply (Integration Spec 6.10), so Udofin shows orders only through `LitigationCaseUpdated` |
| Compliance and GRC | `ObligationPublished`, `ControlTestResultPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `ReturnStatusUpdated`, `PolicyAttested` | Produces control results, evidence, issues and attestations for LawDocsComply or a third-party GRC tool (U18); consumes obligations |
| Platform | `ModuleAttached`, `ModuleDetached`, `ConnectorCertified` | Produces and consumes (Part 7A.0; U21) |

## 5.3 Lender connector framework

- **Connector SPI.** One TypeScript interface per contract capability (catalogue, eligibility, application, decision, documents, execution evidence, mandate, servicing events, collections, grievance, DLG, reconciliation). Each RE connector declares which capabilities it supports and how (sync API, webhook, polling, file).
- **Adapters:**
  - **Finbyx certified connector** — native contract, no mapping layer; first to be certified.
  - **Generic REST/webhook connector** — per-RE field and code mapping (status codes, reason codes, product codes, document types) held as versioned configuration, with a mapping test harness.
  - **File-based fallback** — SFTP or secure upload of CSV/JSON files on a schedule for REs without APIs, with schema validation, checksums and acknowledgement files.
- **Per-RE configuration:** endpoints, mTLS certificates, signing keys (rotated, stored in the secrets vault, never in the database in clear), timeouts, retry policy, rate limits, business hours, contacts for incidents.
- **Certification test-suite** run before any RE goes live and after every connector change: contract conformance, signature and replay rejection, duplicate and out-of-order events, missing fields, slow and failed responses, reconciliation of a synthetic month, and a tenant-isolation test proving no cross-RE leakage. Store the certification report as evidence (U18).
- **Sandbox per RE** with synthetic data, so that an RE can test without real borrowers.

## 5.4 Portal-only REs

Some REs will use only the Udofin lender portal:

- The RE's own staff review applications, documents, bureau and AA outputs, and take decisions in the portal. Decisions use maker-checker and record the user, authority, limit, rule version and reasons. Udofin staff cannot act in an RE's decision queue.
- An RE may configure its eligibility and credit rules in the hosted rule engine (GoRules), approved by its own authorised users. The rule set is the RE's; Udofin hosts it as an outsourced technology service and must not change it (OUT para 15).
- The RE still generates the KFS and sanction from its own approved templates in the portal, with its own document signer.
- The portal also generates the RE's credit appraisal memo (CAM) from the RE's CAM template and decision record, as the RE's document stored in the RE-scoped vault (original prompt asked for CAM generation).
- The RE books the loan in its own LMS. Udofin is not an LMS. Servicing data returns to the loan mirror by API or file; without it, Udofin shows only the KFS schedule labelled "as issued, not updated", and the RE is told that its borrowers' servicing view is incomplete.
- All portal-only obligations (DLA, grievance, CIC reporting, CIMS) remain the RE's.

## 5.5 Failure containment and reconciliation

- **Transactional outbox and inbox** with idempotency keys and per-aggregate sequence numbers; out-of-order events are parked until the gap is filled or timed out to an exception.
- **Retries** with exponential back-off and jitter; dead-letter queues with replay from the ops portal under maker-checker; circuit breakers per RE so that one RE's outage does not degrade others.
- **Durable workflows** (Temporal) for long journeys: application to decision, execution, disbursal wait, mandate registration, cooling-off.
- **Honest borrower states:** "submitted to [RE name]", "waiting for [RE name]", "lender system delayed — your application is saved". Never "approved" or "disbursed" without the RE's event.
- **Daily reconciliation** of every RE: applications sent vs acknowledged, decisions, KFS issued vs accepted, disbursals vs mirror, payments vs mirror, fees invoiced vs confirmed, DLG positions; break reports with ageing and ownership.
- **Incident handling:** connector failures above a threshold open an incident, notify the RE contact, and appear on the RE's dashboard.

---

# PART 6 — LOAN PRODUCTS: COMMON FINANCING ENGINE + PRODUCT TEMPLATES

## 6.1 Common financing engine

Build one common financing engine. Each product is a **product template** (journey, data requirements, consents, verification plan, document checklist, routing rules, disclosure set, execution steps, servicing views and analytics) that a partner RE switches on and configures within guard-rails. The engine provides a separate workflow for each use case covering (from the original prompt):

- purpose and beneficiary verification;
- document collection and consent;
- lender eligibility and affordability assessment (the RE's decision; Udofin collects and pre-validates);
- loan-offer comparison and disclosures;
- permitted disbursement routing (CF para 10(1));
- repayment tracking and reminders;
- evidence of end use, closure or settlement completion;
- product-level delinquency and profitability analytics (Udofin's funnel and unit economics; the RE's portfolio analytics stay in its LMS);
- regulatory compliance (rule packs by product and RE type);
- audit capability;
- data protection and cyber-security controls.

**Microfinance classifier (all products).** Every collateral-free loan to a household with annual income up to ₹3,00,000 (husband, wife and unmarried children) is a microfinance loan, whatever the product, end use or channel (CF para 51). Udofin must capture household composition and income for every collateral-free application, pass it to the RE, and apply the RE's microfinance rule pack: repayment obligations of all household loans plus the proposed loan capped at 50% of monthly household income, and no new loan while above it (CF paras 55–57); household income reported to CICs by the RE (para 54); no prepayment charge (RBC para 81). Detail in Part 8A.1 and 8A.5.

## 6.2 Products to template

| # | Product | Security | Key rules for Udofin (with cites) | MVP/phase |
|---|---|---|---|---|
| 1 | **Personal Loan** (salaried and self-employed) | Unsecured | Age, occupation and income captured (CF para 8(1)); microfinance classifier (CF para 51); OTP-based e-KYC in non-face-to-face mode allows only term loans up to ₹60,000 in aggregate a year and needs a "no other OTP-e-KYC account" declaration (KYC para 25(5), 25(8)), so larger loans route to V-CIP or other KYC by the RE; AA and bank-statement income through the RE as FIU; KFS with APR and validity (RBC para 29); cooling-off (CF para 11) | MVP |
| 2 | **Payday / short-tenure loan** | Unsecured | Heightened conduct risk; KFS validity of one working day for tenor under 7 days (RBC para 29(2)); APR display for very short tenors; repeat-borrowing and affordability limits set by the RE; for ML/UL REs, CCO evaluation before launch and 6 months of intensive monitoring (CMP paras 15(2), 31), applied to every RE by default; microfinance classifier. **App-store gate:** Google Play's Personal Loans policy does not allow apps that promote personal loans repayable in full in 60 days or less, and App Store Guideline 3.2.2(ix) bars the same and caps APR at 36% including fees; short tenors are offered only on the borrower web channel (subject to the RE's and legal sign-off) and are filtered out of the store apps server-side and never mentioned or linked from them, never by disguising the tenor (Part 8.2; Appendix B) | MVP, behind a launch gate |
| 3 | **Loan against securities** (listed shares, bonds, MF units) | Pledge or lien | Demat pledge initiated by the borrower through their DP or the depository's online pledge (NSDL or CDSL) with OTP authorisation and accepted by the RE as pledgee through the RE's own demat account; MF units by lien marked through the RTA (CAMS, KFintech) or MF Central in favour of the RE; invocation and release only by the RE [VERIFY API access route: RE, DP or RTA agreement]; holdings fetched only with consent; for listed-share collateral with NBFC REs of assets ≥ ₹100 crore, 50% LTV at all times with a 7-working-day cure (bond and MF-unit LTVs per the RE's policy), Group 1 securities above ₹5 lakh for capital-market purposes (CF para 106); no lending against the RE's own shares (para 105); IPO funding ≤ ₹1 crore per borrower (para 104); gold or silver-backed ETF and MF units blocked (para 35(2)); margin-call notices from the RE shown in the app | Phase 18 |
| 4 | **Home loan** | Mortgage | Housing-finance definition (plot loan needs a declaration to construct within 3 years; CF para 4(1)(xiv)); HFC REs follow the HFC Directions [VERIFY: not supplied]; disbursal to seller or builder as end-beneficiary (CF para 10(1)); property documents, legal and technical checks by the RE's vendors; mortgage deeds and sale agreements cannot be executed electronically (IT Act First Schedule), so the journey hands off to physical execution; document release within 30 days of closure (RBC para 35) shown in the app | Phase 18 |
| 5 | **Vehicle loan** (new and used cars, two-wheelers) | Hypothecation | Dealer as end-beneficiary (CF para 10(1)); Vahan RC check through an authorised channel; hypothecation endorsement on the RC at registration (Form 34) and removal with the RE's NOC (Form 35) under MV Act s.51 tracked from the RE's events, with the NOC delivered in the app [VERIFY Vahan e-service flow]; insurance status; top-ups against vehicles treated as unsecured by the RE (CON para 10) | Phase 18 |
| 6 | **Loan against property** | Mortgage | Not housing finance (CF para 4(1)(xiv)); title, valuation and legal checks by the RE; physical mortgage execution; document release within 30 days and ₹5,000 per day where the delay is attributable to the RE (RBC paras 35, 39; Section F covers personal loans only, RBC para 6(11), so business-purpose LAP follows the RE's policy) shown to the borrower | Phase 18 |
| 7 | **Resolution finance** (linked to Equator settlements) | Either | **Feasibility-gated.** Funds a borrower's settlement with an existing lender, paid directly to that lender (CF para 10(1) end use); settlement evidence from Equator; strict affordability test; where the new lender is the same RE, it is a compromise settlement or restructuring for that RE (RSA paras 89, 169), and settled borrowers face a cooling period of at least 12 months before fresh exposure from that RE (RSA para 95); measure how many borrowers qualify | Phase 19 |
| 8 | **Medical and insurance-premium finance** | Either | **Feasibility-gated.** Institutional partnerships with hospitals and insurers; payment direct to the provider as end-beneficiary (CF para 10(1)); health data is sensitive, so collect only the minimum and only with explicit purpose-specific consent; small number of clearly defined use cases first | Phase 19 |
| 9 | **Legal-expense and award-enforcement finance** | Either | **Feasibility-gated.** Ordinary repayable loans only, through the RE; non-recourse or litigation-funding cases are referred to specialist funders, not booked, and any referral fee needs a legal note (including professional-conduct rules for advocates) [VERIFY]; Equator awards as evidence only | Phase 19 |
| 10 | **Debt reset / consolidation** | Either | **Feasibility-gated.** A rigorous debt-closure and affordability model before refinancing stressed borrowers; payoff direct to existing lenders (CF para 10(1)); where the RE refinances its own stressed borrower it is restructuring and must pass the RE's viability assessment (RSA para 169); microfinance household cap applies (CF paras 55–57); no marketing that targets distress | Phase 19 |
| 11 | **Gold loan** (proposed) | Pledge of gold jewellery or coins with the RE | Leads, indicative estimate from the RE's published method and branch appointment only: collateral is handled and stored only in RE branches by RE employees (RBC paras 53–54); valuation and LTV per CF paras 40, 43–44; bullet loans ≤ 12 months (CF para 38); renewals and top-ups only on a formal request (CF para 34); auction rules are the RE's (RBC paras 60–66) | Phase 18b |
| 12 | **Business / MSME loan** (proposed) | Either | Entity KYC and beneficial owner; DIN or PAN of directors and guarantors (WD para 19(1)); GST, Udyam and AA data through the RE; CGTMSE-covered loans excluded from DLG (CF para 21(1)); collateral-free loans to low-income households are microfinance loans (CF para 51) | Phase 18b |
| 13 | **Microfinance loan** (proposed) | Unsecured | Household income test and 50% cap (CF paras 51–57); loan card and no prepayment charge (RBC paras 78–81); recovery at a designated place and 09:00–18:00 (RBC paras 90–91, to 31 Dec 2026; then Part 7A.0.4); group processes stay with the RE | Phase 18b |
| 14 | **Supply-chain / TReDS invoice finance** (proposed) | Assignment of receivables | Anchor programme with the supplier or dealer as end-beneficiary (CF para 10(1)); TReDS only as a referral to the platform with the RE as registered financier, without recourse to the MSME (RBI TReDS Directions, 23 Jun 2026) [VERIFY] | Phase 18b |
| 15 | **Education loan** (proposed) | Either | Institution as end-beneficiary (CF para 10(1)); co-borrower KYC and income; moratorium in the KFS; microfinance classifier applies to collateral-free loans (CF para 51) | Phase 18b |

**Feasibility gate for Products 7–10.** Before any workflow is built, produce a feasibility note covering legal permissibility (RBI Directions and other law), the commercial model, conduct and reputational risk, data sensitivity, partner REs willing to lend, and a pilot design with success measures. Do not assume viability.

**Revolving credit.** Build every product as a term loan. A draft CF amendment (August 2026) would confine NBFCs other than credit-card NBFCs to term loans [VERIFY final status]; keep any line-of-credit variant behind a feature flag.

## 6.3 Per-product definition checklist

Every product template has a versioned specification at `docs/products/[code].md` covering (from the original prompt):

1. borrower and beneficiary eligibility;
2. purpose and end-use verification;
3. loan amount, tenure and pricing rules (the RE's; Udofin displays);
4. security or collateral requirements, with collateral, valuation, ownership verification, lien or pledge creation, release and exception handling as explicit workflows for secured products;
5. documentation and verification, and the KYC route;
6. credit appraisal and lender decisioning (who decides, on what inputs, through which connector);
7. offer presentation and disclosures;
8. sanction and agreement workflows, including any physical-execution hand-off;
9. permitted disbursement routing;
10. repayment schedule and servicing;
11. delinquency and recovery workflows, and whether Udofin has any recovery role;
12. closure, settlement and release of security;
13. product-specific reporting and profitability metrics.

## 6.4 Product-wise origination workflows

Each product template (6.3) implements the workflow below. **6.4.0 is the common baseline**; each product table states only what is added or different. "RE" means the partner lender; every decision named is the RE's. Events use the canonical names of the Infrabyx Ecosystem Integration Specification. The **recovery playbook** row names the Finbyx Part 7A R16 playbook the RE runs and Udofin's role in Part 7A; playbook codes must match Finbyx R16 [VERIFY at contract review]. The CloudEvents `productfamily` attribute uses the specification's codes (PL, PDL, LAS or LAMF, HL, VL, LAP, GOLD, MSME, MFI, SCF, EDU; `CLN` for co-lent loans); `RF`, `MED`, `LEF` and `DR` (Products 7–10) are Finbyx and Udofin product codes not yet in the specification's `productfamily` list, so raise them as a versioned contract change before Phase 19. Products 11–15 are **proposed** templates built in Phase 18b, each only after an RE-approved product specification.

### 6.4.0 Common baseline (all products)

| Step | Baseline |
|---|---|
| Channel steps | Mobile number and OTP → platform notice and consents (U4) → product, amount, tenor → minimum eligibility data (age, occupation, income; household income for collateral-free loans: CF paras 8(1), 51) → `EligibilityCheck` to matching REs → offer view (CF para 7) → `ApplicationSubmitted` to the chosen RE → RE decision → KFS → execution → mandate → disbursal status → servicing |
| KYC route | Per RE (Part 8A.3): CKYC identifier with consent; Aadhaar offline or DigiLocker; Aadhaar OTP e-KYC only for s.11A-notified REs and only term loans up to ₹60,000 a year (KYC para 25(5)); V-CIP as the RE's session; PAN or Form 60. Evidence only; the RE decides (KYC para 13) |
| Credit data | Bureau under the RE's CIC membership with consent naming the RE (CIR para 6); AA with the RE as FIU (AA para 8(12)); bank-statement analysis by the RE-approved analyser |
| Documentation | RE's KFS with validity (RBC para 29); sanction letter; agreement with KFS summary box (RBC para 29(6)); eSign and eStamp evidence (`ESignCompleted`, `EStampCompleted`); physical execution for IT Act First Schedule instruments |
| Disbursement | RE account to the borrower's verified account, or to the end-beneficiary for a specific end use (CF para 10(1)); status only (`LoanDisbursed`) |
| Events to the RE | `ApplicationSubmitted`, `BorrowerAccepted`, `ESignCompleted`, `EStampCompleted`, `MandateRegistered`, `CoolingOffExitRequested`, `SettlementRequested`, `SettlementOfferAccepted`, `PTPCaptured`, `ConsentWithdrawn`, `GrievanceRaised`, `RiskSignalRaised` |
| Events from the RE | `ProductCatalogPublished`, `DecisionMade`, `KFSIssued`, `LoanDisbursed`, `ScheduleIssued`, `PaymentReceived`, `DPDChanged`, `LoanClosed`, `NOCIssued`; recovery, ADR and litigation events only as Part 7A permits; transferred, assigned or co-lent loans add `LoanTransferred` and `ServicerChanged` (`CoLendingSplitConfirmed` and `ClassificationSynced` pass only between co-lenders: Integration Spec 6.6) |
| Recovery | Udofin: UR1 for every RE that attaches it; UR2–UR3 per the RE's policy; UR4 only where appointed. The RE runs Finbyx R1–R16 or its own suite |

### 6.4.1 Product 1 — Personal loan (MVP)

| Step | Workflow |
|---|---|
| Channel | Baseline; app and web |
| KYC | Baseline; OTP e-KYC route capped at ₹60,000 a year, larger loans to V-CIP or other CDD |
| Credit data | Bureau and AA income; household income; microfinance flag where household income is ₹3 lakh or less (CF para 51) |
| Collateral | None |
| Documentation | Baseline; NACH mandate; no PDCs where NACH is available (MISC para 23) |
| Disbursement | Borrower's account |
| Events to the RE | Baseline |
| Recovery playbook | Finbyx R16 `PL`: reminders → NI Act s.138 or PSS Act s.25 where an instrument bounced → conciliation (s.74) or Lok Adalat → arbitration only via a pre-named institution or post-dispute consent → civil or commercial suit (s.12A mediation if ₹3 lakh or more). No SARFAESI (unsecured) |

### 6.4.2 Product 2 — Payday / short-tenure loan (MVP, launch-gated)

| Step | Workflow |
|---|---|
| Channel | Borrower web only where tenor is 60 days or less; store apps never show or link it (Part 6.2) |
| KYC | As Product 1 |
| Credit data | As Product 1; RE repeat-borrowing and affordability limits |
| Collateral | None |
| Documentation | KFS validity of one working day where tenor is under 7 days (RBC para 29(2)) |
| Disbursement | Borrower's account |
| Events to the RE | Baseline |
| Recovery playbook | Finbyx R16 `PDL`: early-bucket reminders → conciliation or Lok Adalat for small tickets → s.25 PSS Act where a NACH debit bounced. Heightened conduct monitoring (UR6) |

### 6.4.3 Product 3 — Loan against securities (Phase 18)

| Step | Workflow |
|---|---|
| Channel | Baseline plus holdings consent and pledge or lien authorisation; full journey in 6.5 |
| KYC | Baseline; demat and folio holder must match the borrower |
| Credit data | Holdings via CDSL LAS consent, NSDL CAS or MF Central and RTA (with consent); bureau per RE policy |
| Collateral | Pledge (NSDL, CDSL) or MF lien (CAMS, KFintech, MF Central) in favour of the RE; RE values daily; 50% LTV for listed shares, 7-working-day cure (CF para 106(1)); no RE own shares (para 105); no ETF or MF units backed by primary gold or silver (CF para 35(2)) |
| Documentation | Baseline; pledge form carrying the pledgee's reasonable-notice undertaking (SEBI circular of 5 Feb 2026) [VERIFY: circular number] |
| Disbursement | Borrower's account only after `CollateralPledgeCreated` |
| Events to the RE | Baseline plus `CollateralHoldingsShared`; OD drawdown through the `DrawdownRequested` API (FAPI 2.0; Integration Spec 6.3). From the RE: `CollateralPledgeRequested`, then `CollateralPledgeCreated` or `CollateralPledgeFailed` (6.5) |
| Recovery playbook | Finbyx R16 `LAS`: margin call → reasonable notice → pledge invocation (ICA s.176) → sale under Board policy → shortfall by civil suit or pre-agreed arbitration. SARFAESI excluded (s.31(b)); NBFCs generally cannot use DRT |

### 6.4.4 Product 4 — Home loan (Phase 18)

| Step | Workflow |
|---|---|
| Channel | Baseline plus property and builder details; hand-off to physical execution |
| KYC | Baseline for all co-applicants |
| Credit data | Bureau and AA; income of co-applicants |
| Collateral | Mortgage created by the RE; title, valuation and legal checks by the RE's vendors; CERSAI registration by the RE (SARFAESI s.26D bars enforcement without it) |
| Documentation | Mortgage deed and sale agreement cannot be executed electronically (IT Act First Schedule); RE checklist; plot loans need a declaration to construct within 3 years (CF para 4(1)(xiv)) |
| Disbursement | Seller or builder as end-beneficiary, in tranches by construction stage (CF para 10(1)); revised schedule per tranche (MSD para 7) |
| Events to the RE | Baseline plus property document references; `CollateralChargeRegistered` (CERSAI) and `CollateralReleased` from the RE (mortgage; `CollateralPledgeCreated` is only for pledges and liens) |
| Recovery playbook | Finbyx R16 `HL`: SARFAESI where the RE is eligible (NBFC: assets ₹100 crore or more and debt ₹20 lakh or more, S.O. 652(E) of 12 Feb 2021; HFCs are notified FIs without the NBFC floor) → s.13(2), s.13(4), Rules 8–9 auction; agricultural land excluded (s.31(i)); document release within 30 days of closure (RBC para 35) |

### 6.4.5 Product 5 — Vehicle loan (Phase 18)

| Step | Workflow |
|---|---|
| Channel | Baseline plus dealer quotation; dealer-assisted journey allowed with borrower OTP consent |
| KYC | Baseline |
| Credit data | Bureau; Vahan RC check through an authorised channel [VERIFY] |
| Collateral | Hypothecation endorsed on the RC; terminated with the RE's NOC (Form 35, MV Act s.51) |
| Documentation | Agreement with an enforceable repossession clause: notice period, waiver, procedure, final chance to pay, redelivery and sale (RBC para 26) |
| Disbursement | Dealer as end-beneficiary (CF para 10(1)) |
| Events to the RE | Baseline plus dealer invoice and RC references; `CollateralChargeRegistered` (VAHAN), `CollateralReleased` from the RE |
| Recovery playbook | Finbyx R16 `VL`: notice under the contract → final chance → daytime repossession by the RE's authorised agent with possession memo and inventory (*Hari Dutta Sharma v State of UP*, SC, 16 Sep 2026) → fresh RC in Form 36 (MV Act s.51(5)) → sale. Udofin never repossesses |

### 6.4.6 Product 6 — Loan against property (Phase 18)

| Step | Workflow |
|---|---|
| Channel | As Product 4 |
| KYC | Baseline; entity KYC where the owner is a firm or company |
| Credit data | Bureau, AA, GST and ITR for business purpose |
| Collateral | Mortgage by the RE with CERSAI registration; valuation by the RE's panel |
| Documentation | Physical mortgage execution; end-use undertaking |
| Disbursement | Borrower's account, or existing lender for a takeover |
| Events to the RE | As Product 4 |
| Recovery playbook | Finbyx R16 `LAP`: as `HL`; IBC s.7 against a corporate debtor with default of ₹1 crore or more; personal-guarantor insolvency at the NCLT |

### 6.4.7 Products 7–10 — Specialist products (Phase 19, feasibility-gated)

| Product | Origination differences | Disbursement | Recovery playbook |
|---|---|---|---|
| 7 Resolution finance | Settlement evidence from the existing lender or Equator; strict affordability; same-RE refinance is a settlement or restructuring (RSA paras 89, 169) | Existing lender as end-beneficiary | Finbyx R16 `RF`; settled borrowers face the RE's cooling period (RSA para 95) |
| 8 Medical and insurance-premium finance | Minimum health data with purpose-specific consent; institutional partner verification | Hospital or insurer as end-beneficiary | Finbyx R16 `MED`, as `PL` |
| 9 Legal-expense and award-enforcement finance | Ordinary repayable loans only; non-recourse cases referred out | Borrower or counsel as end-beneficiary [VERIFY: professional-conduct rules] | Finbyx R16 `LEF`, as `PL` |
| 10 Debt reset / consolidation | Debt-closure model; microfinance household cap (CF paras 55–57) | Existing lenders as end-beneficiaries | Finbyx R16 `DR`, as `PL` or secured playbook |

### 6.4.8 Product 11 — Gold loan (proposed, Phase 18b)

| Step | Workflow |
|---|---|
| Channel | Lead, indicative estimate from the RE's published gold price and LTV method (RBC para 45), and appointment at an RE branch. **Gold is handled and stored only in RE branches by RE employees** (RBC paras 53–54), so Udofin offers no doorstep pickup and never touches collateral |
| KYC | Completed by the RE in branch, or pre-filled digitally with the borrower's consent |
| Credit data | Detailed credit assessment above ₹2.5 lakh (CF para 33); bureau per RE policy |
| Collateral | Assay in the borrower's presence (RBC para 46); valuation at the lower of the 30-day average and previous-day close from IBJA or a SEBI-regulated exchange (CF para 40); LTV 85%, 80% or 75% by ticket, maintained throughout (CF paras 43–44); weight caps (CF para 39); assay certificate (RBC para 50) |
| Documentation | KFS and agreement covering auction procedure and notice period (RBC para 49); bullet loans capped at 12 months (CF para 38); no loan to buy gold (CF para 35(1)) |
| Disbursement | Borrower's account (CF paras 46–47) |
| Events to the RE | Baseline; renewals and top-ups only on a formal borrower request (CF para 34); release scheduling after closure |
| Recovery playbook | Finbyx R16 `GOLD`: adequate notice (public notice plus 1 month if untraceable: RBC para 60) → auction advertised in two newspapers (para 61) → reserve at least 90% of current value, 85% after two failures (para 63) → first auction physical in the district (para 64) → surplus within 7 working days (para 66); release within 7 working days of closure, ₹5,000 a day for delay (paras 58, 69). SARFAESI excluded (s.31(b)). Udofin shows RE notices (UR3) |

### 6.4.9 Product 12 — Business / MSME loan (proposed, Phase 18b)

| Step | Workflow |
|---|---|
| Channel | Baseline plus business profile; journey for proprietors, partnerships and companies |
| KYC | Individual KYC for proprietors; entity KYC and beneficial-owner identification for firms and companies; PAN of applicants and guarantors and DIN or PAN of directors (WD para 19(1)) |
| Credit data | Bureau (commercial and consumer), GST and bank data through AA where the RE is FIU, ITR, Udyam; LWD check (WD para 19(1)) and wilful-defaulter covenant (WD para 7(4)) |
| Collateral | Unsecured, or hypothecation or mortgage by the RE; CGTMSE cover flagged (blocks DLG: CF para 21(1)); collateral-free MSME loans to households with income of ₹3 lakh or less are microfinance loans (CF para 51) |
| Documentation | Baseline; guarantee agreements; end-use certificate (WD para 19(2)) |
| Disbursement | Borrower's business account or suppliers as end-beneficiaries |
| Events to the RE | Baseline plus GST, AA and Udyam references and guarantor KYC evidence |
| Recovery playbook | Finbyx R16 `MSME`: s.138 or s.25 → SARFAESI if secured and eligible → CGTMSE claim (first instalment after legal action; legal action waived up to ₹10 lakh) [VERIFY: current scheme terms] → IBC s.7 (corporate debtor, ₹1 crore) or PPIRP → personal-guarantor insolvency at the NCLT. Prepayment-charge limits for MSE floating loans (RBC para 34) |

### 6.4.10 Product 13 — Microfinance loan (proposed, Phase 18b)

| Step | Workflow |
|---|---|
| Channel | Digital application for individual loans; group (JLG or SHG) processes stay with the RE's field staff; assisted mode through U22 only with borrower OTP consent |
| KYC | Baseline; digital KYC only as the RE's authenticated application (KYC para 24) |
| Credit data | Household composition and income questionnaire (CF para 52); all household obligations from bureau and declaration; 50% cap (CF paras 55–57); the RE reports household income (CF para 54) |
| Collateral | None by definition (CF para 51) |
| Documentation | Standard microfinance agreement and loan card in the borrower's language (RBC paras 77–79); no prepayment charge (RBC para 81); pricing ceiling (CF paras 60–61) |
| Disbursement | Borrower's account; recovery-grievance mechanism in the disbursal notice (RBC para 92) |
| Events to the RE | Baseline plus household profile and obligation estimate |
| Recovery playbook | Finbyx R16 `MFI`: designated-place collection, home or work visit only after two missed appearances (RBC para 90); no calls before 09:00 or after 18:00 (para 91(2)) until 31 Dec 2026; paras 89–100 are replaced on 1 Jan 2027 by the Third Amendment (pack B), so keep the microfinance window and designated-place rule by RE policy until RBI confirms (7A.0.4) [VERIFY]; state overlays (7A.0.4); conciliation or Lok Adalat; no coercive steps. Udofin reminders only within the microfinance window |

### 6.4.11 Product 14 — Supply-chain and TReDS invoice finance (proposed, Phase 18b)

| Step | Workflow |
|---|---|
| Channel | Anchor-led dealer or vendor finance: the anchor nominates; the MSME applies in Udofin. TReDS: the RE bids as a registered financier on the TReDS platform; Udofin only refers the MSME to the platform and shows the RE's status (RBI TReDS Directions, RBI/DPSS/2026-27/406, 23 Jun 2026) [VERIFY] |
| KYC | Entity KYC as Product 12; anchor KYC by the RE |
| Credit data | Anchor programme limits, invoice and GST data, Udyam; bureau of the MSME and promoters |
| Collateral | Assignment of receivables; for TReDS, the accepted factoring unit is without recourse to the MSME and the platform registers the assignment with CERSAI |
| Documentation | Programme agreement with the anchor; invoice and acceptance evidence; no-other-financier undertaking for TReDS units |
| Disbursement | Seller's account, or the supplier as end-beneficiary for dealer finance (CF para 10(1)); TReDS settlement through the platform's mechanism [VERIFY: fit with CF para 10(1)] |
| Events to the RE | Baseline plus invoice and factoring-unit references |
| Recovery playbook | Finbyx R16 `SCF`: TReDS buyer default → claim against the buyer, no recourse to the MSME; dealer finance → recovery from the dealer per programme terms and anchor support |

### 6.4.12 Product 15 — Education loan (proposed, Phase 18b)

| Step | Workflow |
|---|---|
| Channel | Baseline plus admission letter, course, fee schedule and co-borrower (parent or guardian) |
| KYC | Baseline for the student and co-borrower |
| Credit data | Co-borrower bureau and income; collateral-free loans to households with income of ₹3 lakh or less are microfinance loans (CF para 51) |
| Collateral | Unsecured, or third-party mortgage or deposit lien above the RE's threshold |
| Documentation | Moratorium (course period plus grace) and repayment start stated in the KFS; institution verification |
| Disbursement | Institution as end-beneficiary per fee schedule (CF para 10(1)); overseas fees only through the RE's authorised dealer bank |
| Events to the RE | Baseline plus admission and institution references |
| Recovery playbook | Finbyx R16 `EDU`: reminders to student and co-borrower after the grace period → Lok Adalat or conciliation → civil suit; SARFAESI only where secured and eligible |

## 6.5 Loan Against Securities — end-to-end journey

This section corrects the Udofin × Finbyx LAS proposal (15 Oct 2026) and is binding for Product 3. Default build: **term loan**; the overdraft (OD) variant sits behind the RE's feature flag `mod.las.revolving` (Integration Spec 11.1; Finbyx Part 6.4), off by default, until the August 2026 draft CF amendment on revolving credit is final [VERIFY].

### 6.5.1 Who does what

| Function | Owner | Udofin role |
|---|---|---|
| Eligible-security list, haircuts, LTV, margin-call and invocation thresholds, cure periods | RE (published in `ProductCatalogPublished`) | Displays; computes only an indicative figure from the RE's published haircuts, labelled non-binding |
| Valuation, drawing power, freezes | RE (Finbyx or its LMS) | Displays `CollateralValuationUpdated` |
| Pledgee or lienholder; contracts with DP, CDSL LAS API, NSDL and RTA or MF Central | RE [VERIFY: direct or through an aggregator] | Runs the adapters as the RE's technology provider, on RE credentials (Part 9.1) |
| Sanction, disbursal, drawdown authorisation, invocation, release | RE | Orchestrates borrower steps and shows status |
| Ledger and OD balances | RE's core | None; no shadow ledger |

### 6.5.2 Rails

| Rail | Creation | Confirmation | Invocation | Release |
|---|---|---|---|---|
| CDSL demat pledge (LAS module) | Borrower's Aadhaar eSign consent to share holdings; holdings by PAN-BOID; OTP on CDSL; pledgor DP approves the same day, auto-approval allowed, rejection reasons required (CDSL/OPS/DP/POLICY/2026/468, 15 Jul 2026) | CDSL confirms to the pledgee | Pledgee instructs its DP | Pledge closure through the DPs |
| NSDL demat pledge | Pledgor's instruction through its DP with agreement number, closure date and pledgee | Pledgee accepts through its DP; pledgor cannot cancel after acceptance | Pledgee's DP; status "Closed, Invoked"; locked-in securities cannot be invoked | Pledgor initiates, pledgee accepts |
| MF units held in statement of account | Lien request through CAMS or KFintech or MF Central with borrower OTP; units cannot be redeemed or switched | RTA confirms the lien | RE invokes; units redeemed to the RE | RE revokes the lien |
| MF units in demat | As the depository pledge | As depository | As depository | As depository |

For every demat pledge the pledge form carries the pledgee's undertaking to give **reasonable notice** to the pledgor before invocation, and the depository notifies both parties on invocation (SEBI circular of 5 Feb 2026, implemented by 6 Apr 2026; ICA ss.176–177; SEBI (Depositories and Participants) Regulations, 2018, reg. 79(8)) [VERIFY: circular number]. The SEBI margin-pledge framework (25 Feb 2020) is for broker margin and is **not** an LAS rail.

### 6.5.3 Journey

1. **Indicative eligibility (Udofin).** From the RE's published list: Σ units × last price × (1 − haircut), capped at the product limit; excludes the RE's own shares (CF para 105), ETF and MF units backed by primary gold or silver (para 35(2)) and, for capital-market purposes above ₹5 lakh, non-Group 1 shares (para 106(2)(i)); IPO funding at most ₹1 crore (para 104). Labelled "indicative; [RE name] decides".
2. **Consent and holdings.** CDSL LAS eSign consent, NSDL CAS or MF Central or RTA OTP; holdings go to the RE as `CollateralHoldingsShared` with the consent reference (`ConsentRecorded`) and are referenced in `EligibilityCheck` and `ApplicationSubmitted`; Udofin keeps only a transient copy (CF para 14(1)).
3. **Application, KYC and bureau** per 6.4.0.
4. **Sanction (RE).** `DecisionMade` carries limit, eligible list, haircuts, LTV trigger, margin-call and invocation thresholds, cure period (7 working days for listed shares under CF para 106(1) where the RE has assets of ₹100 crore or more; RE policy for MF units and bonds) and facility type.
5. **KFS and execution.** `KFSIssued`; agreement and pledge form eSigned; evidence events.
6. **Pledge or lien.** On the RE's `CollateralPledgeRequested` (securities, quantities, pledgee DP or RTA, agreement number, deadline), Udofin orchestrates the borrower's OTP and DP or RTA steps under the scope `collateral.pledge:orchestrate` and returns the authorisation evidence to the RE. The provider confirms to the RE; the RE emits `CollateralPledgeCreated` (reference, quantity, evidence hash). Udofin never shows "pledged" without it; a partial confirmation is shown as partial and the RE recomputes; a rejection, OTP failure or expiry arrives as `CollateralPledgeFailed` and sets `PLEDGE_FAILED`.
7. **Disbursal.** Only after `CollateralPledgeCreated` and documentation; RE account to the borrower's own account (CF para 10(1)); `LoanDisbursed` with UTR.
8. **Daily valuation (RE).** T−1 exchange bhavcopy or AMFI NAV; data more than one business day old freezes drawdowns; corporate actions credited to pledged balances; `CollateralValuationUpdated` (eligible value, drawing power, LTV, price source, as-of, freeze flag).
9. **Drawdown (OD variant only).** The borrower asks in Udofin; Udofin shows the available amount returned by the RE's `GET /v1/facilities/{loan_id}/summary` (the RE computes min(limit, drawing power) − utilised − reserved − dues; Udofin never recomputes it); it sends the request through the `DrawdownRequested` API (Integration Spec 6.3; FAPI 2.0 with `acr` and `auth_time`) with an `Idempotency-Key`; the RE authorises and pays the borrower's account; `LoanDisbursed` (tranche). An uncertain bank status is never re-sent; Udofin shows "pending with [RE name]". In the term-loan variant a top-up is a new, explicit borrower request (CF para 8(2)).
10. **Margin call.** The RE emits `MarginCallRaised` (shortfall, options: pay down or pledge more, deadline). Udofin notifies through U16 in the borrower's language, shows a working-day countdown on the RE's holiday calendar, records the borrower's chosen cure through the RE's cure-intent API (`POST /v1/margin-calls/{id}/cure-intents`: top-up, part payment or sell-to-cure) and offers the RE's payment link or, on the RE's `CollateralPledgeRequested`, the top-up pledge flow. The RE emits `MarginCallCured`, or `MarginCallLapsed` at the deadline, after which Udofin shows "[RE name] will contact you" and waits for the RE's next event.
11. **Invocation (RE only).** The RE gives reasonable notice under the pledge undertaking (`LegalNoticeIssued`, instrument pledge invocation; shown in UR3), invokes through its DP or the RTA, and emits `CollateralInvoked` (quantity, proceeds, date). Sale follows the RE's Board policy; SEBI SAST and PIT disclosures are the RE's where thresholds are crossed [VERIFY]; surplus is refunded to the borrower; any shortfall follows Finbyx R16 `LAS`.
12. **Closure and release.** `LoanClosed` → the RE starts release (NSDL closure needs the pledgor's initiation, which Udofin orchestrates; lien revocation by the RE through the RTA) → `CollateralReleased` → `NOCIssued`. No release while a legal, settlement or set-off hold exists. Release timing follows the RE's policy; within 2 working days of closure [REC] (Finbyx Part 6.4.8; Integration Spec 7.3 step 10).
13. **Ongoing (RE).** Quarterly report of pledged shares to the stock exchanges (CF para 106(2)(ii)); daily reconciliation of pledge positions with the depository and RTA; Udofin reconciles its mirror.

**Mirror states (Udofin):** `ELIGIBILITY_SHOWN → APPLIED → SANCTIONED → PLEDGE_REQUESTED → {PLEDGE_CREATED | PLEDGE_PARTIAL | PLEDGE_FAILED} → DISBURSED → ACTIVE ⇄ MARGIN_CALL → {CURED | LAPSED → INVOKED} → CLOSURE_PENDING → RELEASED → CLOSED`; `FROZEN` is a flag on `ACTIVE`, set only from `CollateralValuationUpdated`.

### 6.5.4 Corrections to the LAS proposal

| Proposal said | v1.1 says | Basis |
|---|---|---|
| "LAS risk / DP engine" (BE-11) and drawable-amount computation in Udofin | Drawing power, LTV, margin calls and freezes are computed by the RE; Udofin shows indicative figures only | CF para 106; OUT para 15 |
| Margin-call deadline per agreement, T+1 to T+3 (Udolex) | 7 working days for listed shares at NBFCs with assets of ₹100 crore or more; RE policy otherwise | CF para 106(1) |
| OD facility as the product | Term loan by default; OD behind a flag pending the revolving-credit draft | Part 6.2 [VERIFY] |
| "RBI Digital Lending Directions, 2025" | CF Chapter III (paras 6–30), which consolidated them on 28 Nov 2025 | CF |
| Liquidation as a "separate legal workflow" | RE-only invocation after reasonable notice under the pledge undertaking | SEBI circular, 5 Feb 2026; ICA s.176 |
| Udolex: LODR disclosure on sale; DRT OA for the shortfall; CERSAI pledge satisfaction | SAST or PIT disclosures by the RE; NBFCs are generally not RDB financial institutions (*Tata Motors Finance v Naushad Khan*, Bom HC 2023; *Aditya Birla Finance v Anjali Nag*, Del HC 2024); pledges are outside SARFAESI (s.31(b)) | Research A [VERIFY: CERSAI registrability of pledges] |
| Event names `CollateralLienRequested`, `CollateralConfirmed`, `MarginShortfallRaised`, `DrawingPowerRecalculated`, `FacilityFrozen` | `CollateralPledgeRequested`, `CollateralPledgeCreated`, `MarginCallRaised`, `CollateralValuationUpdated` (with freeze flag) | Ecosystem Integration Specification |

**Tests:** pledge always names the RE as pledgee or lienholder; no disbursal or "pledged" status before `CollateralPledgeCreated`; RE own shares and gold-backed units excluded from indicative eligibility; stale valuation freezes drawdown display; duplicate drawdown request with the same `Idempotency-Key` creates one request; margin-call countdown uses working days; invocation status appears only after `CollateralInvoked`; release blocked while a hold exists; OD screens hidden while `mod.las.revolving` is off.

---

# PART 7 — FUNCTIONAL MODULE SPECIFICATION

Each module below is a domain module in the NestJS modular monolith. Each one owns its tables, exposes an internal API and publishes events. Build each one only after its specification is approved (Part 11). "Mobile" means channels A and E; "web" means channels B, C, D and F.

## U1. Tenancy, lender (RE) onboarding and LSP agreement registry

Purpose: onboard each partner RE as an isolated tenant and record exactly what Udofin is contracted to do for it.

- **Tenant model:** platform → RE tenant (`lender_tenant`) → legal entity → products. RE type (NBFC layer, HFC, NBFC-MFI, bank), CoR number, CIC memberships, AA FIU status, website disclosure URL, GRO and nodal-officer contacts, Internal Ombudsman applicability.
- **Enhanced due-diligence support:** Udofin's own evidence pack for each RE's LSP due diligence (technical capability, privacy and storage, conduct, past record, compliance; CF para 6(2)) and DLG provider declarations (U14).
- **LSP agreement registry (`lsp_agreement`):** versioned, effective-dated record of the activities Udofin performs (sourcing, KYC technology, servicing support, reminders, recovery agent, DLG), fees and who pays them, data shared, sub-contractors approved by the RE (OUT para 34(iv)), audit and RBI access rights (OUT para 34(vii)–(ix)), incident timelines, termination and exit.
- **Activity gate:** every runtime action that needs a contractual basis (for example accepting `CollectionAllocated`) checks the active agreement and scope.
- **Onboarding workflow:** maker-checker, connector certification (Part 5.3), DLA register lines (U18), product approval (U2), go-live checklist.
- **Isolation:** tenant ID on every RE-scoped row; server-side authorisation plus Postgres RLS; tests prove no cross-RE access.

## U2. Lender product catalogue and configuration

Purpose: hold each RE's approved products as published by the RE, and Udofin's journey configuration around them.

- **Product-offer versions (`product_offer_version`):** immutable copies of `ProductCatalogPublished` (eligibility parameters, pricing grids, charges, penal charges, KFS template version, cooling-off period, grievance contacts, DLA disclosures), with effective dates.
- **Udofin layer:** journey template, document checklist, verification plan, consent set, communications set, routing rules, product template link (Part 6).
- **Guard-rail validation** on publication: cooling-off at least one day, KFS template present, APR inputs complete, grievance contacts present, no borrower-paid LSP fee, microfinance flag logic, store-policy gate by channel (tenor of 60 days or less on both stores; APR above 36% including fees on the App Store).
- **Approval:** platform-approved and legal-review layers (Part 3.4); no product goes live without both the RE's publication and Udofin's approval.
- **Lender portal:** the RE sees and requests changes to its own products; portal-only REs maintain their products here.

## U3. Borrower identity, registration, authentication and device binding (app and web)

Purpose: give each borrower one secure Udofin account, separate from any RE's customer record.

- **Registration:** mobile number + OTP; no password by default; optional email verification; platform notice and consent (U4) before any data is processed; an age check (18 or over) before any further data is collected, because a minor cannot contract (Indian Contract Act s.11) and a child's data would need verifiable parental consent (DPDP s.9, from 13 May 2027).
- **Authentication:** Supabase Auth behind an OIDC abstraction; OTP rate limits and lockouts; step-up authentication (OTP or passkey) for KFS acceptance, eSign, mandate set-up, bank-account change, contact-detail change and data-rights requests.
- **Device binding (mobile):** hardware-backed key pair generated in the Android Keystore or iOS Secure Enclave; Play Integrity and App Attest checks; device register with the borrower's ability to see and remove devices; alerts on every new device on more than one channel; re-authentication at launch and after inactivity. DPS para 68 is used as the baseline by policy (DPS applies directly only to credit-card-issuing NBFCs, DPS para 3; Part 8A.11).
- **Web:** passkeys (WebAuthn; usually synced across the borrower's devices, so they are a strong authenticator but not a device binding); short sessions with inactivity timeout; strong CAPTCHA or equivalent against brute force (DPS para 67(1) baseline).
- **Version control:** server-side minimum-version check; one live version per platform with older versions retired within six months (DPS para 68(2)(iii) baseline); forced update for incompatible versions.
- **Account lifecycle:** mobile-number change with strong re-verification; account closure; dormant-account handling; deceased-borrower process routed to the RE.
- **No telephony binding:** no SIM binding by outbound SMS and no phone-state read (Part 4.5).

## U4. Consent, privacy and data lifecycle

Purpose: prove what the borrower agreed to, for which lender and purpose, and honour withdrawal, retention and deletion.

- **Consent artefact (`consent_artefact`):** purpose, data items, recipient (Udofin, a named RE, a named provider), legal basis, notice text version and language, channel, timestamp, device and IP, expiry, and the screen version shown. Separate artefacts for platform use, each RE eligibility check, each RE application, bureau, AA (reference to the AA's own artefact), CKYC download by the RE, DigiLocker, marketing, and Equator referral.
- **Purpose disclosed at each stage** (CF para 13(3)); explicit consent before sharing with any third party (para 13(4)).
- **Borrower controls:** view, give, deny, restrict, revoke, and request deletion (CF para 13(2)); a privacy dashboard in app and web; data-principal rights requests and grievances with clocks (DPDP Rules: response within 90 days, from 13 May 2027; a shorter RE or RBI clock wins).
- **Withdrawal effects:** stop future processing; tell affected REs (`ConsentWithdrawn`, `DataPrincipalRequest`; adopted in v1.1, Part 5.2); keep only what law requires.
- **Retention engine:** per data class, the longest legally required period wins (PMLA/KYC records are the RE's; Udofin keeps its evidence copies only as the agreement and law require); minimal data only (CF para 14(1)); secure destruction with certificates.
- **Data map:** every field tagged with owner, purpose, recipients, storage location (India only; CF para 14(4)), retention and sensitivity; generated privacy-policy annex of third parties (CF para 15(2)).
- **Breach handling** links to U24.
- **Consent Managers:** accept consent given, reviewed or withdrawn through a Consent Manager registered with the Data Protection Board (DPDP s.6(7)–(9); registration rules in force from 13 Nov 2026) [VERIFY interoperability standard].

## U5. KYC and verification

Purpose: run KYC technology for the RE and hand the RE complete, verifiable evidence; never take the KYC decision.

- **Routes, configured per RE (Part 8A.3):**
  - CKYC: capture the KYC Identifier and the borrower's explicit consent for the RE to download (KYC para 23(4)); the RE performs the CKYCR search and download [VERIFY Udofin access as the RE's agent].
  - Aadhaar: offline verification (XML or QR) or DigiLocker as proof of possession (KYC para 23(2) and proviso (ii)); Aadhaar OTP e-KYC authentication only where the RE is notified under the first proviso to s.11A(1) of the PML Act and through its own licence (KYC para 23 proviso (i)); never store a full Aadhaar number; mask it everywhere; no Aadhaar in logs.
  - OTP-based e-KYC in non-face-to-face mode: specific consent (KYC para 25(1)), declaration of no other such account (25(8)), and the ₹60,000 per year term-loan limit (25(5)) enforced in routing.
  - V-CIP: launched from app and web into the RE's own V-CIP web session (Udofin hosts no V-CIP component); the RE's infrastructure and authorised official; India-only IP, geo-tag, liveness (KYC para 27); Udofin as technology provider retains no V-CIP data (KYC para 27(1)(i)).
  - PAN or Form 60 (KYC para 23(5)), verified through an authorised provider; equivalent e-documents verified by digital signature with a live photo (KYC para 23 proviso (iii)).
- **Capture:** camera document scan with edge detection, glare and blur checks, compression and on-device redaction of the Aadhaar number; selfie and liveness; OCR with human-verifiable extraction.
- **Evidence (`kyc_evidence`):** provider, request and response hashes, timestamps, document hashes, liveness scores, the consent reference and the step version. Passed to the RE with `ApplicationSubmitted`.
- **Reuse across lenders:** a document held in one RE's vault is never copied to another RE (Part 10.2 principle 20); for a second RE the borrower re-fetches from DigiLocker, re-uploads, or authorises use of a copy Udofin is itself permitted to retain under its own agreement, each time with fresh consent naming that RE; each RE performs its own CDD.
- **Fraud signals** to U24: tampered document, face mismatch, velocity, device risk.

## U6. Credit data, income and affordability

Purpose: obtain credit and income data lawfully through the RE and present it for the RE's assessment.

- **Bureau:** Udofin is not a credit institution member of any CIC; CIR para 6 membership belongs to the RE. Bureau consent (`bureau_consent`) names the RE and purpose. Modes, selected per RE after legal review: (a) the RE pulls through its own membership via its connector; (b) Udofin calls the CIC or an aggregator with the RE's credentials as the RE's agent; (c) a borrower-consented own-report flow [VERIFY all three against CICRA s.2(l) "specified user", CIC Regulations reg. 3 and the provider's authorisations]. A fourth mode, Udofin becoming a specified user under reg. 3 (as amended 10 Nov 2021) on RBI's criteria, is not available at launch (Part 8.2). The original "Udofin soft-pulls CIBIL via Surepass" is not adopted until verified (Appendix E).
- **Multiple enquiries:** avoid one hard enquiry per matching RE; use the RE-approved pre-qualification mode and pull for the chosen RE only [VERIFY CIC enquiry classification].
- **New-to-credit:** routing must not exclude a borrower only for lack of credit history unless the RE's rule says so (CIR para 38(5)).
- **AA:** the RE is the FIU (AA para 8(12)); Udofin launches the AA consent journey as the RE's technology service provider and receives data only as the consent artefact allows (AA para 28); store `aa_consent_reference` only.
- **Income and affordability inputs:** declared income, employer, AA or bank-statement analysis output (RE-approved analyser), household composition and income for the microfinance test (CF paras 51, 55–57).
- **Display:** the borrower sees their own data where the RE allows and a plain explanation of what was used.

## U7. Application, eligibility and lender routing (multi-lender rules)

Purpose: turn a borrower request into eligibility checks with matching REs, consistently and neutrally.

- **Application (`application`):** product, amount, tenor, purpose, applicant data, state machine with allowed transitions, failure states, timeouts and human overrides (original "important addition" 4).
- **Pre-filter** using each RE's published eligibility parameters (U2) evaluated in GoRules ZEN; then `EligibilityCheck` to each matching RE in parallel with timeouts.
- **Matching mechanism** versioned and documented (CF para 7(2)); inputs restricted to the borrower's request, RE rules and RE responses (Part 4.6).
- **Unmatched lenders** recorded with a reason category for display (CF para 7(1)).
- **Mandatory captures:** age, occupation, income (CF para 8(1)); household income for collateral-free loans (CF para 51).
- **Submission** to the borrower's chosen RE only (`ApplicationSubmitted`), with consent references.
- **Information requests** from the RE become tasks with reminders; the borrower uploads through the system picker after onboarding (Part 4.5).
- **Ops portal:** exception queues (stuck states, connector failures, data mismatches); Udofin staff cannot change an RE decision.

## U8. Offers, KFS, disclosures and cooling-off

Purpose: present offers and RE disclosures exactly as issued, prove the borrower saw them, and support the cooling-off exit.

- **Offer view (`offer`):** built to Part 4.6 (CF para 7); identical on app and web; the offer set, matching-mechanism version and ranking metric are stored with each view.
- **Independent APR check:** recompute APR from the RE's cash flows; a mismatch blocks display and raises an RE exception.
- **KFS:** RE-issued, in the borrower's language, with unique proposal number and validity period (RBC para 29(1)–(2)); explanation screens and an acknowledgement that the contents were explained and understood (para 29(1)); `kfs_view_event` records each view, scroll completion and time. Validity is not a waiting period; acceptance within validity binds the RE to the KFS terms (para 29(2) Explanation).
- **Charges guard:** any charge not in the KFS is flagged if later seen in servicing data.
- **Disclosures:** LSP disclosure, RE website link, GRO details (CF para 12(2)), privacy policies, cooling-off terms.
- **Cooling-off:** period from the RE (≥ 1 day); exit button visible from disbursal until expiry; `cooling_off_exit` request, RE payable amount (principal and proportionate APR, plus any disclosed processing fee; CF para 11) and payment to the RE's account.

## U9. Documents, eSign, eStamp and DMS

Purpose: execute the RE's documents with verifiable evidence and give the borrower access to them for the retention period agreed with the RE, and thereafter a route to the RE's copy.

- **Document set:** application form, KFS, sanction letter, loan agreement, MITC, guarantee agreement, mandate form, KYC documents, end-use undertakings; the CAM is the RE's internal document and is shown to the borrower only if the RE chooses.
- **eSign:** Aadhaar OTP eSign through a licensed ESP (on the RE's or Udofin's contract per agreement); `esign_evidence` with ESP transaction ID, signer certificate, signed hash, timestamp, signer name match and IP. **A document is never marked signed because a workflow stage was reached.**
- **eStamp:** e-stamp certificate purchase through an authorised vendor for the state applicable to the agreement [VERIFY per state: Stamp Act, SHCIL or state portal, rates]; `estamp_certificate` with number, value, state, first and second party, and linkage to the document.
- **Physical-execution hand-off** for documents excluded from electronic execution (IT Act First Schedule: for example promissory notes, powers of attorney, sale or conveyance of immovable property).
- **Delivery:** digitally signed documents on the RE's letterhead flow automatically to the borrower's verified email or phone on execution (CF para 9(3)), sent by Udofin on the RE's behalf where the agreement says so.
- **DMS:** private, encrypted object storage in India; SHA-256 hashes; versions; verification status; short-lived signed URLs; watermarking; access logs; retention per U4; borrower "My documents" in app and web.

## U10. Disbursement orchestration (status only; no funds)

Purpose: show the borrower where their money is, without Udofin ever handling it.

- **Pre-disbursal checklist display:** execution complete, mandate status, any end-beneficiary details captured with the borrower's consent.
- **Beneficiary capture:** borrower's bank account with penny-drop name match through the RE's or an approved provider; end-beneficiary details for permitted end-use products (CF para 10(1)).
- **Status from the RE only:** `LoanDisbursed` (UTR, amount, date) or `DisbursementFailed`; no "disbursed" state otherwise.
- **Interest transparency:** show that interest runs from the actual disbursal date and EMIs on the disbursed amount, and any revised schedule after part-disbursement (MSD para 7).
- **Guard:** configuration validator blocks any Udofin-controlled account as beneficiary.

## U11. Repayments, mandates, payments and reconciliation

Purpose: let borrowers pay the RE easily and prove every payment reached the RE.

- **Mandates (`mandate`):** eNACH (net banking, debit card, Aadhaar) and UPI AutoPay in favour of the RE, on the RE's sponsor bank and utility code; lifecycle: registration, amendment, suspension, revocation, expiry; UMRN capture; `MandateRegistered`.
- **Payments (`payment_intent`):** UPI intent, QR, collect, payment links and cards through the RE's merchant account (Part 4.3); BBPS where the RE is a biller [VERIFY].
- **Status:** never treat a gateway "success" as final; await settlement confirmation or the RE's `PaymentReceived`; handle `PaymentBounced` with the RE's charges and messages.
- **Failed and duplicate payments:** duplicate-payment prevention by idempotency keys; refund requests routed to the RE.
- **Receipts:** the RE's receipt shown in the app; Udofin's acknowledgement is labelled "payment initiated", never "receipt".
- **Reconciliation:** gateway reports ↔ RE events ↔ mirror; break queue in the ops portal.
- **Payment security:** step-up authentication, fraud flags to U24, and an in-app "report as fraud" option (DPS para 66 baseline).

## U12. Loan mirror and borrower servicing

Purpose: give the borrower a clear servicing view built only from the RE's data.

- **Loan mirror (`loan_mirror`):** read model from RE events (schedule, dues, payments, DPD, charges, closure, NOC), versioned by event sequence; labelled with "as at" time and the RE's name.
- **Servicing requests** routed to the RE: statement of account, schedule, interest certificate, foreclosure quote, part-prepayment, NOC, document release, contact change, mandate change.
- **Prepayment:** show the RE's quote; no prepayment charge displayed where the RE's rules prohibit it (RBC paras 33–34, 81 via the RE's rule pack).
- **Reminders:** RE-approved reminders including the applicable penal charge (RBC para 30).
- **Closure:** NOC display; document-release tracking with the 30-day timeline (RBC para 35).
- **Quarterly statements** for floating-rate EMI loans where the RE provides them (RBC para 31).

## U13. Collections and recovery support

Purpose: support RE-approved reminders for every loan, and full recovery work only where Udofin is the appointed recovery agent.

- **Without a recovery contract:** pre-due and overdue reminders and payment links only, with RE-approved content.
- **With a recovery contract (gate in U1):** `collection_allocation` from `CollectionAllocated`; agent particulars sent to the borrower before first contact on every allocation or change (CF para 9(6)); notice and authorisation letter with the agent (RBC paras 95–96); agents trained and bound by the code of conduct (RBC paras 98–99); antecedent and police verification (RBC para 94). Paras 93–97 sit in the microfinance section of RBC; apply them to every product by policy (Part 8A.6).
- **Contact-policy engine:** effective-dated rule pack per RE; recovery contact only between 08:00 and 19:00 and no intimidation or harassment (RBC para 100); the RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026) replace paras 89–100 with Section J, paras 100A–100AB, from 1 Jan 2027, adding IIBF DRA certification of agents (para 100I), agency details at least 1 day before the first visit (100L), call logging and recording with disclosure kept at least 6 months or until disposal if sub judice (100P) and the grievance-officer block on every recovery communication (100AA); build both rule packs effective-dated (Part 7A.0.4) [VERIFY: official text not supplied in docs/regulations/rbi/]; separate microfinance windows per the RE's rule pack.
- **Recovery agents (`recovery_agent`):** identity, verification, certification, authorisation per RE, active status.
- **Cash:** digital receipts; cash only where the contract allows, reflected in full in the borrower's account the same day; no fee from proceeds (CF para 10(5)).
- **Logging:** `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued`; call recordings in India.
- **AI** may draft reminders within approved templates; it never threatens, never misrepresents and never agrees a settlement.
- **v1.1:** the overdue, settlement and payment centre, ADR access, notices and case visibility, recovery-agent operations, data feeds and conduct controls are specified in **Part 7A** (UR1–UR6), attachable per RE and product. Where Part 7A and this module differ, Part 7A prevails.

## U14. DLG management

Purpose: manage Udofin's obligations as a DLG provider, independent of collections.

- **Arrangement (`dlg_arrangement`):** RE, contract, form (cash with the RE, FD with a Scheduled Commercial Bank with lien, or bank guarantee; CF para 23), extent, invocation timeline, disclosure clause (para 22), term not shorter than the longest loan tenor in the set (para 27(2)).
- **DLG set (`dlg_set`):** fixed list of sanctioned loans; loans leave only by repayment or write-off; cover activates pro rata on disbursal; cap ≤ 5% of amount disbursed (para 24); headroom calculator; block loans under trust-fund credit-guarantee schemes (para 21(1)).
- **Provider declaration:** statutory-auditor-certified declaration of aggregate DLG outstanding, number of lenders, number of portfolios and past default rates on similar portfolios, on every entry or renewal (para 20(3)).
- **Invocation (`dlg_invocation`):** received from the RE within 120 days overdue (para 27(1)); validation against the set and cap; settlement; never reinstated (para 25(4)); recovery sharing per contract (para 25(3)).
- **Monthly disclosure (`dlg_disclosure`):** number of portfolios and amount of each, published on Udofin's website within 7 working days after month-end (para 28); workflow with maker-checker and evidence.
- **Accounting feed** to U17 (deposits, guarantees, invocations, recoveries, fees).
- **Isolation from decisions:** no DLG data in matching, ranking or underwriting inputs (para 20(2); Part 4.4).

## U15. Grievance redressal, AI support and Equator

Purpose: let borrowers raise and track complaints in the app or web, route them to the responsible party, and give access to Equator for disputes the RE has referred, without a separate app (Part 7A UR2).

- **Lodging** on the DLA and website (CF para 12(3)); unique reference; acknowledgement; category; attachments through the system picker; communication history.
- **Routing:** RE-related complaints to the RE's GRO under the grievance-host switch (Part 2); LSP-related complaints to Udofin's nodal grievance officer (para 12(1)); redressal responsibility stays with the RE (para 12(3)).
- **Clocks and escalation:** 30-day clock; after 30 days without reply, or on full or partial rejection, show the CMS (cms.rbi.org.in) and CRPC route (para 12(4)); Internal Ombudsman and RB-IOS 2026 information as the RE's framework requires [VERIFY: Internal Ombudsman Directions 2026 and RB-IOS 2026 texts not supplied].
- **Credit-information complaints** routed to the RE with its CIR clocks (Part 8A.2).
- **AI assistant:** answers only from approved knowledge sources and the borrower's own data; discloses that it is AI; never invents rights, never promises outcomes, never rejects or closes a complaint; always offers a human; classification and routing suggestions confirmed by staff.
- **ADR access (`equator_referral`, extended in v1.1 as `adr_case_view`; Part 7A UR2 prevails):** Udofin never refers a dispute to arbitration or any ADR process; the RE refers, and only where the loan agreement names Equator or another institution or the borrower gives written post-dispute consent (*CORE v ECI-SPIC-SMO-MCML (JV)*, SC, 8 Nov 2024; *L&T Finance v Jai Paras Material Store*, Cal HC, 14 May 2026). ADR is offered when a dispute remains unresolved after the RE's process and the parties consent, or where the agreement provides for ODR; never presented as a substitute for the RBI route; case created by the RE through its own API scope with a consented data set; secure deep link into Equator's web flow; outcome returned to the grievance record.

## U16. Communications, notifications and marketing

Purpose: send the right message on the right channel with the right consent.

- **Template management:** versioned, multilingual, approval workflow; regulatory templates owned by the RE; TRAI DLT template and header IDs for SMS.
- **Channels:** push (FCM, APNs, web push), SMS, WhatsApp Business, email, in-app inbox.
- **Service vs marketing:** service messages under the service relationship; marketing only with separate, explicit consent (`marketing_consent`) with "no" as the default; preference centre; frequency caps and quiet hours; the RBC Second Amendment marketing rules (Chapter IIIA) from their effective date [VERIFY: amendment text and date not supplied]; DoT/TRAI-registered telemarketers only (RBC para 101).
- **Neutrality:** no lender-sponsored promotion inside the offer journey (CF para 7(4)); any RE-specific campaign outside it needs legal review.
- **Feedback:** event-triggered CSAT/NPS, free-text feedback, app-store review prompts only after positive events, and feedback analytics.
- **No PII in push payloads**; deep links per Part 3.2.

## U17. Udofin finance and accounting

Purpose: keep Udofin's own books for its LSP business. The loan book belongs to the RE.

- **Double-entry ledger (`udofin_ledger` tables):** chart of accounts, journals, postings, periods, with NUMERIC money and decimal.js; immutable postings with reversal entries.
- **Revenue:** sourcing, platform and collection fees invoiced to REs; GST invoices and e-invoicing where applicable [VERIFY GST rate, place of supply, e-invoicing threshold]; TDS deducted by REs and reconciled with Form 26AS [VERIFY sections].
- **DLG accounting:** cash deposits and FD liens as assets; bank guarantees as contingent exposures; invocations as losses; recovery shares as income; treatment under the applicable accounting framework confirmed with Udofin's auditors [VERIFY: Ind AS 109 or AS applicability to Udofin].
- **Costs:** per-call vendor costs (KYC, bureau, eSign, eStamp, messaging, cloud) captured from provider logs for unit economics.
- **Reconciliation:** fees invoiced vs RE confirmations (`DailyReconciliationFile`); bank reconciliation of Udofin's own accounts.
- **Exports:** Tally Prime (XML/ODBC) and SAP (IDoc or API) export of Udofin's journals and masters; Tally and SAP are destinations, not the books.
- **Never:** record borrower loan principal or interest as Udofin's assets or income.

## U18. Compliance, regulatory register, audit access and LawDocsComply bridge

Purpose: prove to each RE, its auditors and RBI that Udofin meets its obligations.

- **Regulatory register:** dated requirements with REQ-IDs shared with Finbyx (Part 8A), applicability per RE type, owner, control, evidence, test and open questions; change impact workflow (original "important addition" 8).
- **DLA register (`dla_register`):** Part 4.7; certification evidence packs for each RE's CCO (CF para 18(4)).
- **Evidence:** permission manifests per build, consent statistics, data-map extracts, DLG disclosures, incident reports, connector certifications, VAPT reports, policy versions.
- **Audit and inspection access:** read-only, time-boxed roles for RE auditors and RBI-authorised persons, provisioned by maker-checker (OUT para 34(vii)–(ix)).
- **LawDocsComply and third-party GRC connectors** under the compliance-mode switch (Part 2): one generic GRC contract from the Ecosystem Integration Specification (resources `Obligation`, `Control`, `ControlTestResult`, `Issue`, `Incident`, `RegulatoryReturn`, `PolicyAttestation`, `OutsourcingArrangement`, `KRI`; events `ObligationPublished`, `ControlTestResultPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `PolicyAttested`), with LawDocsComply as the first certified adapter and versioned field and status maps for MetricStream (REST), IBM OpenPages (GRC REST), ServiceNow IRM (staging tables) and Archer (REST and Content API) [VERIFY: LawDocsComply public API and each vendor's current API]; periodic OSCAL 1.2.x export (component definition, assessment results, POA&M); evidence hash-chained and stored in India, with aggregate counts and masked sample IDs only, never raw PII.
- **Udofin's own compliance:** privacy policy, data storage policy, GRO appointment, website disclosures, DLG disclosures, DPDP obligations, app-store declarations.

## U19. Reports, MIS and lender dashboards

Purpose: give Udofin and each RE the operational and conduct reports they need, without duplicating the RE's LMS.

- **Udofin internal:** funnel by step, channel, RE and product; drop-off reasons; TAT; connector health; unit economics; grievance analytics; DLG positions; collections performance where appointed.
- **Lender dashboards:** the RE's own sourced applications, decisions, conversion, disbursals reported by the RE, complaints, DLG cover and invocations, reconciliation breaks; exports to Excel, CSV and PDF; scheduled reports.
- **Conduct reports:** offer-view neutrality checks (share of borrowers choosing each rank, by RE), dark-pattern audit results, permission audit.
- **The RE's financial, risk and regulatory reports** come from its LMS (Finbyx M17 for Finbyx REs); Udofin supplies data, not those reports.
- **Row-level security** by RE in every report.

## U20. AI layer (governed)

Purpose: use AI where it saves effort without taking decisions.

- **Use AI for:** borrower FAQ and status answers from approved sources; document classification and extraction with human verification; application completeness checks; complaint classification and routing suggestions; staff search and summaries; reminder drafting within templates; anomaly detection in reconciliation.
- **AI must never:** approve, reject or price a loan; rank offers; execute or alter a financial transaction; alter contract terms; bypass authorisation; reject or close a complaint; make legal determinations; send unapproved borrower messages.
- **Governance:** model inventory, prompt and output logs (PII-redacted), explainability records, AI disclosure to borrowers, India-region inference only [VERIFY per provider], aligned with the RBI FREE-AI framework (August 2025) as each RE requires.

## U21. Integration hub and lender connectors

Purpose: one place for every external integration, with consistent security and observability.

- **Lender connectors** per Part 5.3.
- **Provider adapters** behind interfaces (Part 9): KYC, DigiLocker, PAN, bureau, AA, bank-account verification, eSign, eStamp, depositories and RTAs, payment gateways, mandates, messaging, Equator and other ODR providers (Part 7A UR2), LawDocsComply and third-party GRC tools (U18), notice-dispatch vendors for RE-issued notices (Part 7A UR3), court-data and legal-tech views only as RE-permitted projections (Part 7A UR3), accounting exports.
- **Ecosystem integration v2 (Phase 16b):** every connector implements the Ecosystem Integration Specification (CloudEvents 1.0, AsyncAPI 3.0, OpenAPI 3.1, JSON Schema 2020-12 registry with 90-day dual publication of any breaking `vN`, Standard Webhooks, `Idempotency-Key`, mTLS with RFC 9421 signatures, OAuth 2.1 client credentials, FAPI 2.0 where borrower-delegated) and passes the connector certification suite, which emits `ConnectorCertified`; third-party LOS/LMS connectors are certified per RE under the same suite; attachable modules declare a `module.yaml` manifest (Part 7A.0.3).
- **Mock and sandbox first;** production adapters only with real credentials, clearly labelled.
- **Controls:** OAuth2 client credentials and mTLS; signed webhooks with replay protection; rate limits; timeouts; retries; credential vault with rotation; per-call cost and latency logging without PII.
- **Integration monitor** in the ops portal with health, error rates and alerts.

## U22. Field and assisted-onboarding app (optional)

Purpose: support assisted onboarding and, only where appointed, field collections.

- **Expo app** separate from the borrower app, distributed through managed channels.
- **Assisted onboarding:** the borrower still gives consent on their own device or by OTP; the agent never enters OTPs for the borrower.
- **Collections:** allocated cases only (U13); geo-tagged visits on the agent's device; digital receipts; offline sync with conflict resolution.
- **Device controls:** device binding, remote wipe, no access to contacts, SMS or call logs, minimum permissions.

## U23. Administration, white-labelling and theming

Purpose: let Udofin and each RE configure without code changes, inside guard-rails.

- **Users and roles:** RBAC plus attribute scopes (RE, product, function); maker-checker per permission; MFA mandatory for staff; break-glass access with audit.
- **Feature flags (`feature_flag`):** per platform, RE, product, channel and app version.
- **Theming (`theme_config`):** design tokens (colour, typography, spacing, radius, logo) shared by the mobile and web design systems; dark mode; accessibility contrast checks on every theme; RE co-branding within the offer view limited to the lender name and logo at equal size.
- **White-label build pipeline** [assess]: per-RE app identifiers, store listings and signing handled by the RE as account owner.
- **Configurable** forms, checklists, templates and journey copy within the layers of Part 3.4.
- **Audit trail:** immutable, hash-chained, who/what/when/where with before and after values.

## U24. Security operations, fraud and risk signals

Purpose: protect borrowers, REs and Udofin, and report incidents within the RE's regulatory timelines.

- **Fraud signals:** device integrity, emulator and remote-access detection, velocity, synthetic-identity indicators, document tampering, mule-account checks on beneficiary accounts; signals shared with the RE as evidence, never as a decision.
- **Security monitoring:** centralised logs without Aadhaar, PAN or OTP; SIEM alerts; WAF; DDoS protection; secrets scanning.
- **Incident management:** severity matrix; notification to each affected RE without undue delay, target 2 hours from Udofin's detection, so the RE can report to RBI within six hours of Udofin's detection (OUT para 61); Udofin's own CERT-In report within 6 hours (CERT-In Directions, 28 Apr 2022); where Udofin is Data Fiduciary, DPDP breach intimation to the Board and affected Data Principals without delay and a detailed report to the Board within 72 hours (DPDP Rules, from 13 May 2027); where it is the RE's processor, notice to the RE within the same 2-hour target; post-incident reviews.
- **Testing:** independent security review that tries to break the system: cross-RE access, IDOR, privilege escalation, insecure document links, replayed requests, webhook forgery, unauthorised admin actions (original "important addition" 1); VAPT before every major release.
- **App protection:** certificate pinning, obfuscation, secure storage, screenshot blocking on sensitive screens, no secrets in the app bundle; published app checksum or store link per DPS para 68(5) baseline.

## U25. Borrower financial dashboard and transparency

Purpose: give the borrower a trustworthy "books of accounts" view of their borrowing through Udofin.

- **Loan ledger per loan:** disbursed amount and date, every charge with its KFS reference, every payment with the RE's receipt, interest, penal charges, outstanding, next due, cooling-off status; data from the loan mirror with "as at" time.
- **Across loans:** total outstanding, monthly obligations, and a simple obligations-to-income view using the income the borrower declared.
- **Explainers:** APR, penal charges, prepayment rights, cooling-off, grievance route, how Udofin is paid (by the RE, never by the borrower).
- **Downloads:** statements, KFS, agreements and receipts from the DMS.
- **Personal expense tracking** beyond loans [assess]: only with separate explicit consent and borrower-entered data; Udofin is not an FIU and cannot pull bank data for this purpose (AA para 8(12)).
- **Feedback and trust signals:** RE disclosures, Udofin's GRO, data and permission summary ("what Udofin can access on this phone").

---

# PART 7A — RECOVERY SUPPORT, NOTICES AND ADR ACCESS (LSP SCOPE; ATTACHABLE)

This Part specifies the **LSP-scope subset** of the Infrabyx Recovery, Litigation and ADR Suite. The full lender-side suite is Finbyx Part 7A (R1–R16), which runs in the RE's system of record. Udofin builds six modules (UR1–UR6) as one attachable module pack, `modules/ur-recovery-support/`, that an RE switches on per product and per capability. Where Part 7A differs from U13 or U15, **Part 7A prevails**. Events, APIs and connector rules follow the Infrabyx Ecosystem Integration Specification (`docs/ecosystem/infrabyx-integration-spec.md`); event names below are the canonical names and must not be renamed.

Labels: **[LAW]** statute, regulation or Direction text; **[JUD]** judicial interpretation; **[INTERP]** our reading; **[REC]** recommendation. Anything unconfirmed carries `[VERIFY: …]`.

## 7A.0 Scope, attach and detach, and LSP limits

### 7A.0.1 What binds Udofin in recovery

| Rule | Source | Effect on Udofin |
|---|---|---|
| The RE guides an LSP acting as recovery agent to comply with RBC and stays fully liable; the RE answers for its recovery agents | [LAW] CF paras 6(5), 6(7); OUT para 17 | UR4 only under an explicit recovery-agent contract (U1); RE suspension switch |
| Agent particulars to the borrower by email or SMS before the agent's first contact, on every assignment or change | [LAW] CF para 9(6) | UR4 hard gate |
| Repayment directly to the RE; no pool or pass-through account; no third-party control; cash recovery reflected the same day, no LSP fee from proceeds | [LAW] CF para 10(2)–(5) | Payment instructions only on RE accounts; cash ledger (UR4) |
| LSP nodal grievance officer; redressal stays with the RE; CMS route after 30 days or rejection | [LAW] CF para 12 | ADR never replaces the CMS route |
| No contacts, call logs, files or telephony; consent before sharing; India-only storage | [LAW] CF paras 13(1), 13(4), 14(4) | No skip tracing, third-party contact or device data |
| Settlement is the RE's discretion, approved one level above the sanctioner (Board for fraud or wilful defaulter); over 3 months or part settlement is restructuring; cooling period at least 12 months; consent decree if a case is pending; decision-making cannot be outsourced | [LAW] RSA paras 16(5), 87, 89–90, 95, 100, 157; OUT para 15 | Udofin relays and displays; [INTERP] a settlement sanction is a credit decision Udofin never takes |
| Conduct until 31 Dec 2026: police verification, notice and authorisation letter, website list, training, no harassment, calls 08:00–19:00; microfinance designated place and 09:00–18:00 | [LAW] RBC paras 90–91, 94–100 | Rule pack A |
| RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026), **in force 1 Jan 2027**: paras 89–100 replaced by Section J, paras 100A–100AB | [LAW] RBI notification Id=13672 [VERIFY: official text not supplied in docs/regulations/rbi/] | Rule pack B: IIBF DRA certificate (100I; existing agents one more year); website agency list updated within 7 days (100K); agency details at least 1 day before the first visit (100L); notice of change (100M–N); minimum data to agents (100O); calls logged and recorded with disclosure, kept at least 6 months or until disposal if sub judice (100P); no harsh incentives (100Q); no device personal data (100U); contact 08:00–19:00 unless the borrower asks otherwise, avoiding bereavement, weddings and festivals (100Y(4)); pre-approved written communications naming the sender (100Y(8)); false statements are harsh (100Z); grievance officer's details on every recovery communication (100AA); TCCCPR (100AB). No numeric frequency cap |
| No unilateral appointment or forced choice from the lender's panel; referral to an institution not named in the agreement, with a silent borrower, is unilateral in substance | [JUD] *TRF v Energo* (2017) 8 SCC 377; *Perkins Eastman v HSCC* (2020) 20 SCC 760; *CORE v ECI-SPIC-SMO-MCML (JV)* (SC, 8 Nov 2024); *L&T Finance v Jai Paras Material Store* (Cal HC, 14 May 2026); *Shikha Ghosh v Axis Bank* (Del HC DB, 30 Sep 2026; next date 17 Nov 2026) | Udofin never refers, appoints or sees neutral selection (UR2) |
| Conciliation settlements have arbitral-award status; Mediation Act ss.4–25 and 27–30 not in force (s.26 in force) | [LAW] A&C Act ss.73–74; S.O. 4384(E), 9 Oct 2023 [VERIFY on egazette] | No mediated settlement is called a decree |
| DLG gives no collection right; RE invokes within 120 days overdue; never set off against the loan | [LAW] CF paras 25(2)–(4), 27(1) | DLG never shown in UR1 or used by UR4 |

### 7A.0.2 What Udofin may and may not do

| Activity | Udofin | Condition |
|---|---|---|
| RE-approved reminders, payment links, PTP capture, hardship request | May (all REs) | Servicing scope of the LSP agreement; contact policy; RE templates |
| Settlement request relay and display of the RE's offer; capture of the borrower's acceptance evidence | May (UR1 attached) | Offer is RE-issued and RE-approved; Udofin computes nothing |
| Display of RE-issued notices and case status | May (UR3 attached) | Only instruments and stages the RE's visibility policy permits |
| Borrower link into Equator or another ODR provider for a case the RE has referred | May (UR2 attached) | Referral basis recorded (pre-named institution or written post-dispute consent) |
| Tele-calling, field visits, cash receipts | Only where appointed (UR4) | Explicit recovery-agent contract; gates in UR4 |
| Approve, price or promise a settlement or waiver; negotiate within a band | **Never** | RSA para 16(5); OUT para 15 |
| Refer a dispute to arbitration, mediation, conciliation or Lok Adalat; nominate or veto a neutral | **Never** | The RE refers; Udofin credentials never hold the referral scope |
| Issue a legal notice or letter in Udofin's name (demand, LRN, SARFAESI s.13(2), NI Act s.138, A&C Act s.21, pledge invocation) | **Never** | Sender is always the RE (or its counsel or authorised officer) |
| Hold, pool or net money; take a fee from recovery proceeds | **Never** | CF para 10(2)–(5) |
| Repossess, invoke collateral, invoke DLG, start SARFAESI, litigation or IBC action | **Never** | RE-only acts (Finbyx R4–R10) |
| Skip tracing, asset search, contact with references or family, device lock | **Never** | CF para 13(1); RBC para 100; RBC Third Amendment paras 100S–100U |
| Hold the litigation record, call court-data APIs, see other REs' cases or the RE's settlement mandate | **Never** | Data ownership 7A.0.5 |

### 7A.0.3 Attach and detach

- **Unit of attachment:** RE tenant × product × capability (UR1–UR6). The entitlement is valid only when all three agree: the RE's licence SKU in U1, the LSP agreement scope (for UR4, the recovery-agent contract) and the feature flag `mod.udofin-recovery.[capability]`, evaluated server-side through an OpenFeature-compatible provider.
- **Manifest:** `modules/ur-recovery-support/module.yaml` declares id, version, `requires` (U1, U4, U11, U12, U15, U16, U21; U22 for field work), capabilities, events produced and consumed, APIs, permissions, data categories, `regulatory_refs`, `retention_class`, `licence_sku`, `ui_slots` and migrations.
- **Lifecycle:** `AVAILABLE → LICENSED → INSTALLED → CONFIGURED (maker-checker; RE approves templates, visibility policy and contact pack) → CERTIFIED (connector certification with the RE's suite; ConnectorCertified) → ENABLED (ModuleAttached) → READ_ONLY (ModuleDetached; RE detach or suspension switch, OUT para 17) → DETACHED (records retained)`.
- **On detach:** new allocations and requests are refused; all contact stops at once; open allocations are handed back (the RE issues `CollectionDeallocated` and notifies the borrower: RBC para 95; paras 100M–100N); in-flight settlement requests go to the RE with their evidence; the borrower keeps a read-only history and a "contact [RE name]" route; an export pack (JSON, CSV, PDF/A, SHA-256 manifest) goes to the RE (OUT paras 42–43, 87–88).
- **Read-only, never deleted:** detaching switches writes and UI off; it never shortens retention or lifts a legal hold.

| Record class | Minimum retention | Basis |
|---|---|---|
| Call recordings and call logs (UR4) | 6 months, and until final disposal where the matter is sub judice; Udofin default 12 months | [LAW] Third Amendment para 100P from 1 Jan 2027 [VERIFY]; [REC] before then |
| Agent particulars notices, authorisation letters, delivery proofs, contact evaluations | Later of 8 years after loan closure and final disposal of any linked proceeding | [REC], covering limitation periods of 3 to 12 years (Limitation Act arts. 55, 62, 136) |
| Settlement requests, offers as displayed, acceptance evidence | As above | [REC]; RSA paras 89–100 records are the RE's |
| Cash receipts and Udofin's cash-in-transit ledger | 8 years from the end of the financial year | [LAW] Companies Act s.128(5) for Udofin's books |
| Notice delivery and read evidence (Udofin channel) | As the notice it evidences | [REC] |
| ADR case view | Until the RE's case closure plus the RE's schedule; originals stay with the provider | [REC] |

DPDP erasure requests are passed to the RE (`DataPrincipalRequest`); records needed to establish or defend a legal claim are kept under the applicable exemption and the borrower is told why [VERIFY: DPDP Act s.17(1)(a) wording and Rules commencement].

### 7A.0.4 Rule packs

- **Pack A** (to 31 Dec 2026): RBC paras 90–100. **Pack B** (from 1 Jan 2027): Third Amendment paras 100A–100AB. The pack is chosen by the timestamp of each attempt; both are effective-dated rule-pack versions in U16 and UR4.
- **Microfinance window:** pack A uses 09:00–18:00 (RBC para 91(2)). Whether a microfinance-specific window survives the deletion of paras 89–97 is open [VERIFY]; until confirmed, keep 09:00–18:00 and the designated-place rule for microfinance loans by policy [REC].
- **State overlays:** Karnataka Act 15 of 2025 and the Tamil Nadu Money Lending Entities (Prevention of Coercive Actions) Act, 2025 (notified 9 Jun 2025; ss.20–26 reach NBFCs operating in Tamil Nadu; vires contested) as configurable overlays [VERIFY current text and status].

### 7A.0.5 Data ownership

The RE's system (Finbyx R1–R16 or the RE's suite) is the system of record for the loan, dues, classification, recovery case and strategy, notices, litigation, settlement decisions and ADR referral and mandate; Udofin holds only labelled projections. The ADR provider holds the docket, neutral selection, orders and original settlements and awards; Udofin holds status and links. Udofin is the system of record for borrower interactions in its channels, consents, settlement requests as received, acceptance evidence, its own delivery and read evidence, agent activity and recordings where appointed, cash receipts and LSP grievances.

## UR1. Borrower overdue, settlement and payment centre

**Purpose:** one place where the borrower sees what is overdue, pays the RE, promises payment, asks for help, and asks for or responds to a settlement, without Udofin taking any decision.

**Capabilities:**

- **Overdue view** from the U12 mirror: DPD, SMA status with the RE's examples (IRACP paras 15, 17; RSA para 18) and each penal charge with its reason (RBC para 30(7)).
- **Pay now:** link, UPI intent or QR on the RE's merchant account, or a mandate re-presentation request; Udofin's acknowledgement reads "payment initiated" until the RE's receipt arrives (CF para 10(2)–(3)). Co-lending loans pay into the escrow (TDCR para 117); after `LoanTransferred` or `ServicerChanged` only the new instruction is used and old links are disabled the same day.
- **Promise to pay:** date, amount and channel → `PTPCaptured`. The screen carries no acknowledgement-of-debt wording unless the RE's legal team approves the template, because a written, signed acknowledgement restarts limitation (Limitation Act s.18) [INTERP].
- **Hardship request** (all products by policy; RBC para 89 for microfinance) as a U12 service request to the RE.
- **Settlement request:** proposed amount, schedule, reason and documents (system picker) → `SettlementRequested`.
- **RE offer** (`SettlementOfferIssued`): shown verbatim with hash, validity, schedule and a mandatory RE **characterisation block** (display blocked without it): restructuring if over 3 months or partial (RSA paras 89–90); CIC status "settled" (CIR para 12(4)); cooling period of at least 12 months (RSA para 95); consent decree if a case is pending (RSA para 100); for fraud or wilful defaulters, criminal proceedings and penal measures continue (RSA paras 97–98).
- **Acceptance:** OTP or Aadhaar eSign within validity, bound to the offer hash; sent as `SettlementOfferAccepted` (Integration Spec 6.8) with `offer_ref` and evidence. `SettlementApproved`, `SettlementBreached` and `RecoveryReceiptPosted` update the view with the RE's text.
- **Counter-proposal:** a new `SettlementRequested` linked to the offer. Udofin staff and bots never counter-offer.

**Mobile and web:** same centre on app and web; push carries no amount or PII; desktop web shows UPI QR. The operations portal sees status only, with no approve or edit control. Portal-only REs issue and approve offers in the lender portal under maker-checker that checks the approver's level against the RE's delegation matrix and blocks anyone who sanctioned the loan (RSA para 16(5)(i)); fraud and wilful-defaulter cases need a Board approval reference (para 16(5)(ii)). The field app shows offers read-only.

**States:**

- `settlement_request`: `DRAFT → SUBMITTED → ACKNOWLEDGED_BY_RE → {OFFER_ISSUED → {ACCEPTED → APPROVED → IN_PAYMENT → {COMPLETED | BREACHED} | OFFER_EXPIRED | DECLINED_BY_BORROWER} | DECLINED_BY_RE} | WITHDRAWN`.
- `ptp`: `CAPTURED → DUE → {KEPT | PART_KEPT | BROKEN}`, set only from RE payment events.

**Data:** `settlement_request`, `settlement_offer_mirror` (RE reference, terms, validity, characterisation, hash), `settlement_acceptance_evidence` (method, transaction ID, offer hash, timestamp, device), `ptp`, `hardship_request`; `payment_intent` from U11.

**Controls:** no Udofin role can create or alter an offer, waiver or appropriation; no acceptance after validity; AI explains but never negotiates; no false urgency (para 100Z); borrower's language (RBC para 10) and grievance block (para 100AA); no cross-selling in recovery communications [REC]; DLG never shown as reducing dues (CF para 25(2)).

**Events:** consumes `DPDChanged`, `AssetClassificationChanged`, `PaymentReceived`, `PaymentBounced`, `SettlementOfferIssued`, `SettlementApproved`, `SettlementBreached`, `RecoveryReceiptPosted`, `LoanTransferred`, `ServicerChanged`; produces `SettlementRequested`, `SettlementOfferAccepted`, `PTPCaptured`.

**Tests:** offer without a characterisation block is not displayed; acceptance after validity is rejected; no Udofin role can write an offer (permission matrix test); a gateway "success" never marks a due as paid; old payment links are disabled after `ServicerChanged`; a co-lending payment never targets one RE's account; PTP screen contains no unapproved acknowledgement text; portal-only approval by the loan's sanctioner is blocked.

## UR2. Dispute and ADR access (Equator; no separate app)

**Purpose:** let the borrower take part in an ADR process that the RE has lawfully started, or ask the RE for one, from inside the Udofin app or web, while Udofin never refers.

**Routes the borrower may see (RE-approved neutral text):**

| Route | Status today | Udofin role |
|---|---|---|
| RE grievance, then RBI CMS | In force (CF para 12) | Always visible; never displaced by ADR |
| Conciliation (A&C Act Part III) | In force; s.74 award status; 30 days' silence rejects an invitation (s.62(4)) | Shows RE-referred sessions; relays borrower requests |
| Mediation (Mediation Act 2023) | Enforcement provisions not in force; a mediated settlement is a contract only | Never calls it a decree |
| Arbitration | Only where the loan agreement names Equator or another institution, or the borrower gives written post-dispute consent | Link into the provider's flow for RE-referred cases only |
| Lok Adalat (LSA Act ss.19–21) | Deemed decree, no appeal; next National Lok Adalat 12 Dec 2026 [VERIFY: nalsa.gov.in] | Shows the notice and sitting details |
| Consumer commission | An arbitration clause does not bar it (*Emaar MGF v Aftab Singh* (2019) 12 SCC 751) | Never discouraged |

**Capabilities:**

- **Case view** from ADR events sent by the RE, or by Equator under the RE's data-sharing terms: referral (track and basis), consent, neutral appointed (name and disclosure filed; no selection data), hearings, status, outcome and compliance.
- **Signed link** into the provider's web flow: single-use, short-lived, journey-bound token, no PII in the URL; in-app browser tab (Custom Tabs, SFSafariViewController) limited to the provider's allow-listed domain, no JavaScript bridge; a new tab on web. The provider authenticates by OTP and runs any eSign or DigiLocker step itself.
- **Post-dispute consent** is captured in the provider's flow with an explicit decline path (s.11 petition or ordinary courts); online mediation consent (Mediation Act s.30, when in force) and fast-track consent (A&C Act s.29B) are separate. Udofin never pre-ticks, never bundles consent with loan acceptance or a settlement, and never asks again after a decline unless the RE issues a new referral.
- **Borrower-initiated request:** a dispute form (category `adr_request`) goes to the RE as `GrievanceRaised`. The RE decides. The RE's reply, or day 31 without one, shows the CMS route.
- **Reminders** for hearings (at least 3 days before, [REC]) through U16; documents are uploaded in the provider's flow, not stored by Udofin.
- **Outcome:** settlement or award summary as sent; any payment link is the RE's; compliance status from `ADROutcomeComplianceUpdated`.
- **Disclosure:** the ADR page states that Equator and Udofin are Infrabyx products and that Equator is independent of the RE and of Udofin in appointing neutrals [REC; legal note required].

**Mobile and web:** same case view on app and web; the operations portal sees link health only, never case content; the lender portal shows the RE its own referrals.

**States (mirror):** `NOT_REFERRED → REFERRED → CONSENT_PENDING → {CONSENTED | DECLINED | DEEMED_DECLINED} → NEUTRAL_APPOINTED → HEARING_SCHEDULED ⇄ IN_PROGRESS → {SETTLED | AWARD_ISSUED | NON_SETTLEMENT | WITHDRAWN | STAYED} → COMPLIANCE → CLOSED`. For an arbitration referral, `CONSENTED` follows `REFERRED` only where the basis is `post_dispute_consent`, and a `clause_names_institution` referral goes straight to `NEUTRAL_APPOINTED`; conciliation and mediation referrals always pass through `CONSENT_PENDING` (A&C Act s.62; 30 days' silence is `DEEMED_DECLINED`, s.62(4)).

**Data:** `adr_case_view` (RE reference, provider, provider case ID, track, basis, status, last sequence), `adr_link_issue` (token hash, expiry, used_at), `adr_request`, `adr_info_view_event`.

**Controls:**

- The scope `adr.referral:create` is never issued to Udofin credentials (Ecosystem Integration Specification); a test proves Udofin cannot call it.
- A referral event without `basis` (pre-named institution with clause reference and version, or post-dispute consent reference) shows no call to action; Udofin raises `ComplianceIssueRaised` to the RE and its GRC tool.
- Udofin never sees neutral selection, the RE's settlement mandate or any other lender's case.
- When the RE sends an IBC moratorium, deceased-borrower or court-stay hold, ADR actions are hidden.
- Udofin records nothing in hearings; mediation and conciliation confidentiality (A&C Act s.75; Mediation Act ss.22–23 when in force) means no Udofin analytics on session content.

**Events:** consumes `ADRReferralCreated`, `ADRConsentRecorded`, `ADRNeutralAppointed`, `ADRHearingScheduled`, `ADRCaseStatusChanged`, `ADROutcomeRecorded`, `ADROutcomeComplianceUpdated`; produces `GrievanceRaised` (ADR request) and `ComplianceIssueRaised` (missing basis).

**Tests:** Udofin client credentials get 403 on referral creation; referral without basis shows no action and raises an issue; link token reuse and expiry rejected; in-app browser blocks non-allow-listed domains; consent screen is never shown inside the loan-acceptance journey; CMS route visible on every ADR screen; hold status hides actions.

## UR3. Notices and case visibility

**Purpose:** deliver the RE's notices and letters as an additional channel with evidence, and show recovery and case status only as the RE permits.

**Capabilities:**

- **Notice inbox** fed by `LegalNoticeIssued`: RE-signed PDF/A with hash, instrument (reminder, loan recall, agent intimation, settlement offer, SARFAESI s.13(2) or possession or sale notice copy, NI Act s.138 or PSS Act s.25 notice copy, A&C Act s.21 notice copy, gold auction notice, pledge invocation notice, Lok Adalat notice), statute reference, language and template version.
- **Udofin channel only:** in-app, SMS with a link to the authenticated inbox, and email, each producing `NoticeServiceUpdated` with Udofin's evidence (delivered, opened, fully scrolled). Udofin's delivery **never replaces** the statutory mode the RE must use (SARFAESI Rules, r.3; A&C Act s.3) and Udofin never marks a notice "served" or "deemed served" (*Sedhram Nilkanth Muglikar v M.R. Makhare*, Bom HC, 2026).
- **Visibility policy** per RE × product × instrument × stage, **off by default**, with RE-legal-approved wording for each status string (for example "Your lender has started proceedings under the SARFAESI Act; next step: …").
- **Case status** projection from `RecoveryCaseOpened`, `RecoveryStrategyChanged` (stage only), `LitigationCaseOpened`, `LitigationCaseUpdated`, `HearingScheduled` (date only), `LitigationCaseClosed`, `AssetRepossessed` (with the possession memo and inventory the RE sends; RBC para 26; *Hari Dutta Sharma v State of UP*, SC, 16 Sep 2026), `AuctionScheduled`, `AuctionConcluded`, `SurplusRefunded` (RBC para 66 for gold), `CollateralInvoked` and `RecoveryCaseClosed`. Udofin calls no court-data API and keeps no litigation record.
- **Borrower actions:** confirm receipt (never an admission of the debt), ask for another language (RBC para 10), dispute the notice with the RE's GRO, download. Addressees are only the borrower, co-borrower and guarantor of record (RBC para 100; para 100Y). No WhatsApp; push carries no content.

**Mobile and web:** inbox on app and web; delivery failures in the operations portal; visibility policy set in the lender portal with maker-checker and RE legal approval.

**States:** `notice_delivery`: `RECEIVED_FROM_RE → PUBLISHED → {DELIVERED → OPENED → READ_FULLY | NOT_DELIVERED → FALLBACK_SENT} → (WITHDRAWN_BY_RE)`.

**Data:** `notice_mirror` (RE reference, instrument, statute reference, language, SHA-256, template version, RE statutory mode, visibility policy version), `notice_delivery_event`, `case_status_projection`, `visibility_policy`.

**Controls:** hash check before display; no Udofin generation or editing of notice content; the sender is always the RE (or its counsel or authorised officer), Udofin appears only as "delivered by Udofin, LSP of [RE name]"; approved status strings only; no "served" state; grievance block on every recovery communication (para 100AA).

**Events:** consumes the events listed above and `NoticeServiceUpdated` from the RE where the policy permits showing statutory delivery status; produces `NoticeServiceUpdated` (Udofin channel) and `GrievanceRaised`.

**Tests:** tampered PDF is not displayed; an instrument outside the policy never appears; no API or UI path sets "served"; WhatsApp channel is not selectable for any recovery template; an unregistered addressee never receives a notice; a withdrawn notice shows the RE's withdrawal text.

## UR4. Recovery-agent operations (only where appointed)

**Purpose:** where an RE appoints Udofin (or an agency Udofin engages with the RE's prior consent, OUT para 34(iv)) as recovery agent, work allocated cases within the RE's policy, the RBC rules and full evidence.

**Hard gates (all must pass; fail closed):**

1. Active `recovery_agent_contract` covering the RE, product, DPD bucket, territory and channel (tele, field, cash) on the attempt date; otherwise `CollectionAllocated` is rejected with a reason.
2. Udofin's recovery role disclosed in the KFS (RBC Annex I Part 2 item 6(ii)) or notified under CF para 9(6).
3. Agent eligible: police and antecedent verification current (RBC para 94); training and code-of-conduct undertaking (paras 98–99); RE authorisation letter and ID (paras 95–96); from 1 Jan 2027, IIBF DRA certificate (para 100I; existing agents by 31 Dec 2027) [VERIFY].
4. Agent particulars delivered to the borrower by email or SMS before first contact (CF para 9(6)); from 1 Jan 2027, agency details at least 1 day before the first visit (para 100L) [VERIFY].
5. `canContact(account, party, channel, purpose, time)` permits the attempt; it runs before every attempt, logs denials and fails closed. Checks: party of record; window per pack, borrower preference and microfinance rules; sensitive-occasion blackout; the RE's Board frequency cap (RBI sets no number); stop on payment, PTP not yet due, open dispute, litigation, ADR or IBC hold, stay or deceased borrower; registered 1600-series caller ID [VERIFY: TRAI coverage of agency calls]; pre-approved template with sender and grievance block (paras 100Y(8), 100AA).

**Capabilities:**

- Allocation intake, worklists by bucket and territory, scripts in the borrower's language, outcome codes, PTP, field-visit check-in on the **agent's** device (never the borrower's location), digital receipts.
- Call recording with a disclosure prompt on every recovery call; call time and count logged (para 100P; [REC] before 1 Jan 2027); legal-hold flag extends retention.
- **Settlement during calls:** the agent or bot may only present an offer the RE has already issued for that account (`SettlementOfferIssued`); anything else is a `SettlementRequested` for the RE.
- **Cash:** only on overdue loans and where the contract allows; full-amount digital receipt; cash-in-transit ledger; RE posting confirmed the same day, otherwise escalation at end of day (CF para 10(5)); per-receipt and per-agent cash limits from the RE [VERIFY: Income-tax Act 2025 cash-receipt limit].
- **Hand-back, not escalation:** Udofin never decides on legal action; it returns the case with outcome codes and the RE issues `RecoveryStrategyChanged` or `CollectionDeallocated`.
- **Agency list feed** to the RE's website (RBC para 97; para 100K update within 7 days).
- **Voicebot or chat agent** [REC; RBI FREE-AI report, 13 Aug 2025, guidance only]: discloses it is automated and acting for the RE; offers a human at any turn; same `canContact` envelope; transcripts kept as recordings.

**Mobile and web:** field app (channel E, U22): minimum case data (para 100O), encrypted offline cache, remote wipe, recorded calls through the RE's trunk, digital ID and authorisation letter (RBC para 95), no contacts, SMS, call-log or storage permissions. Operations portal: tele-calling workspace with the `canContact` banner, QA and the agent register. Lender portal: allocations, conduct metrics, recording samples, suspension switch. Borrower app: agent particulars, "verify this agent" (QR on the agent's ID) and a recovery-grievance button (RBC para 92).

**States:**

- `collection_allocation`: `OFFERED → {ACCEPTED | REJECTED} → NOTICE_PENDING → NOTICE_DELIVERED → ACTIVE → {RESOLVED | RETURNED | DEALLOCATED | SUSPENDED} → CLOSED`.
- `contact_attempt`: `EVALUATED → {DENIED (reason) | PERMITTED → ATTEMPTED → {RIGHT_PARTY | NO_ANSWER | WRONG_PARTY | REFUSED}}`.

**Data:** `recovery_agent_contract`, `recovery_agent`, `agent_certification` (IIBF reference, expiry), `agent_authorisation`, `collection_allocation`, `agent_particulars_notice`, `contact_policy_pack`, `contact_evaluation` (inputs, pack version, decision), `contact_attempt`, `call_recording` (retention_until, legal_hold), `field_visit`, `ptp`, `cash_receipt`, `cash_in_transit_entry`, `agent_scorecard`.

**Controls:** incentives exclude raw call volume and include conduct metrics (para 100Q); DLG cover is invisible to agents and to the policy engine (Part 4.4); the RE audits a sample of cases where Udofin is both DLG provider and recovery agent [REC]; no photographs of people; no contact with references, family or employer; no device data (para 100U).

**Events:** consumes `CollectionAllocated`, `CollectionDeallocated`, `RecoveryAgentNoticeSent` (gate 4 evidence where the RE sends the particulars: CF para 9(6)), `LegalHoldChanged` (retention and contact holds), `RecoveryStrategyChanged`, `SettlementOfferIssued`, `PaymentReceived`, `RecoveryReceiptPosted`, `LitigationCaseUpdated` (hold flag), `ModuleDetached`; produces `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued`, `SettlementRequested`, `GrievanceRaised` (misconduct), `ComplianceIssueRaised` (gate breach).

**Tests:** allocation rejected without a contract, outside territory or for an ineligible agent; no attempt before a delivered particulars notice; attempts at 07:59 and 19:01 denied (08:59 and 18:01 for microfinance); pack B used from 1 Jan 2027; open dispute stops contact; unrecorded call flagged; unposted cash receipt escalates at end of day; bot cannot state a figure not in an RE offer; detach stops attempts at once.

## UR5. Data feeds to the RE's recovery suite

**Purpose:** give the RE's recovery suite (Finbyx Part 7A or a third-party system through the generic connector) complete, consented and reconcilable data from Udofin.

| Feed | Content | Timing | Event or transport |
|---|---|---|---|
| Promises to pay | Date, amount, channel, captured by | Real time | `PTPCaptured` |
| Settlement requests and acceptances | Proposal or offer reference, evidence | Real time | `SettlementRequested`; `SettlementOfferAccepted` |
| Disputes and complaints on the debt | Category, stop-contact flag | Real time | `GrievanceRaised`, `GrievanceUpdated` |
| Hardship and contact-detail changes | Borrower-verified changes | Real time | U12 service request |
| Contact attempts and outcomes (UR4) | Evaluation result, attempt, recording reference | Real time | `CollectionActivityLogged`, `FieldVisitLogged` |
| Cash receipts (UR4) | Full amount, receipt number, agent, time | Same day | `ReceiptIssued` |
| Notice delivery on Udofin's channel | Delivered, opened, read | Real time | `NoticeServiceUpdated` |
| Consent and rights requests | Withdrawal, erasure, access | Real time | `ConsentWithdrawn`, `DataPrincipalRequest` |
| Risk signals | Payment-failure patterns, suspected fraud | Real time | `RiskSignalRaised` |
| Engagement summary | Overdue-centre views, payment intents per loan | Daily | `DailyReconciliationFile` extension |

**Rules:**

- CloudEvents 1.0 envelope with `tenantid`, `reid`, `consentref` and `seq`; OpenAPI pull for backfill; SFTP file fallback for REs without APIs (Part 5.3); every payload cites a consent reference or a contractual or statutory basis flag (CF para 13(4)).
- Minimum data: no device data, no contact lists, no borrower location, no inferred hardship from device signals.
- **Routing:** co-lending feeds go to the servicer RE named as the single point of interface (TDCR paras 104–105); transferred loans follow `ServicerChanged`.
- **Daily reconciliation:** allocations vs activity, PTPs vs payments, cash receipts vs RE postings (same day), notices delivered, settlement requests acknowledged; breaks aged for the RE's audit committee (OUT paras 12(2), 39).

**States:** `feed_delivery`: `QUEUED → SENT → ACKED → {APPLIED | REJECTED (schema or consent)} → RECONCILED`, with dead-letter and maker-checker replay.

**Mobile and web:** back-end only; feed health and breaks in the operations and lender portals.

**Events:** produces the events in the table; consumes RE acknowledgements and `ConnectorCertified`.

**Tests:** payload without consent or basis is rejected before sending; schema registry rejects a breaking change without a new version; duplicate delivery is idempotent; a co-lending feed never reaches the partner RE directly; reconciliation flags a cash receipt without a same-day RE posting.

## UR6. Conduct, consent and evidence controls

**Purpose:** make every recovery conduct rule provable to the RE, its auditors, RBI and the RE's GRC tool.

| Control | Rule | Mechanism | Evidence |
|---|---|---|---|
| UR6-C01 | Contact window and frequency (RBC paras 91(2), 100; para 100Y(4)) | `canContact` before every attempt | Evaluation log incl. denials; zero out-of-window attempts |
| UR6-C02 | Notice before contact (CF para 9(6); para 100L) | UR4 gate | Delivered-notice reference per allocation |
| UR6-C03 | Agent eligibility (RBC paras 94, 98–99; para 100I) | Register gate | No allocation to an ineligible agent |
| UR6-C04 | Recording and logging (para 100P) | Recording service | Coverage % and retention dates |
| UR6-C05 | Pre-approved, vernacular communications with grievance block (RBC para 10; paras 100Y(8), 100AA) | Template registry | Template ID on every message |
| UR6-C06 | No threats, humiliation or false statements (RBC para 100; para 100Z) | Content lint on scripts and templates; QA sampling | Lint results; QA scores |
| UR6-C07 | No third-party contact or device data (CF para 13(1); para 100U) | Party-of-record check; permission audit | Denials; manifest scans |
| UR6-C08 | Money rules (CF para 10(2)–(5)) | Account validator; cash ledger | Zero Udofin accounts; same-day posting rate |
| UR6-C09 | Settlement authority (RSA para 16(5); OUT para 15) | Permission matrix | Quarterly access review |
| UR6-C10 | ADR referral basis (*CORE*, 8 Nov 2024; *L&T Finance*, 14 May 2026) | Scope denial; basis check | Denied calls; issues raised |
| UR6-C11 | Notices sent only by the RE | Sender check on templates | Template metadata |
| UR6-C12 | No WhatsApp in recovery (platform policy) | Channel configuration test | CI result |
| UR6-C13 | Grievance routing and CMS display (CF para 12; RBC para 92) | U15 routing | Forwarding receipts |
| UR6-C14 | India storage, retention and legal hold (CF para 14(4); para 100P) | Retention engine | Purge and hold logs |
| UR6-C15 | Bot disclosure and human hand-over [REC; FREE-AI report] | Bot policy | Transcript samples |
| UR6-C16 | DLG neutrality (Part 4.4) | No DLG fields in UR4 data | Schema test |

**Capabilities:** conduct dashboard per RE (complaints per 1,000 allocated accounts, out-of-window attempts, recording coverage, QA score, notice-before-contact rate, same-day cash posting rate) feeding the RE's FPC conduct pack (RBC para 8); breach workflow that suspends the agent, raises `ComplianceIssueRaised` within 24 hours [REC] and supports the RE's compensation process (para 100F) [VERIFY]; evidence to LawDocsComply or a third-party GRC tool as `ControlTestResultPublished` and `EvidenceSubmitted`, with periodic OSCAL assessment-results export; aggregate counts and masked sample IDs only, hash-chained, stored in India.

**Mobile and web:** operations and lender portals only; borrowers see the grievance route and agent verification (UR4).

**States:** `control_test_run`: `SCHEDULED → RUNNING → {PASSED | FAILED → ISSUE_RAISED → REMEDIATED → RETESTED}`.

**Events:** produces `ControlTestResultPublished`, `EvidenceSubmitted`, `ComplianceIssueRaised`, `PolicyAttested`; consumes `ObligationPublished`.

**Tests:** every UR6 control has an automated test and an owner; a synthetic out-of-window attempt fails C01 and raises an issue; evidence export contains no unmasked identifier; a detached module still publishes retention evidence; the OSCAL export validates against the OSCAL 1.2.x schema [VERIFY: version in use by each GRC tool].

---

# PART 8 — REGULATORY BASELINE (STARTING REGISTER — VERIFY BEFORE EACH MODULE)

## 8.1 Rules for handling regulation

Before implementing any regulated workflow:

1. Research the current authoritative source: rbi.org.in, the official gazette, MeitY, UIDAI, NPCI, TRAI, CERT-In, CERSAI, NeSL, DigiLocker, and the current Google Play and Apple App Store policy pages.
2. Record in `docs/compliance/requirements-to-controls.md`:
   - instrument;
   - paragraph;
   - date and "updated as on" version;
   - applicability conditions (RE type, layer, product, channel, Udofin role);
   - responsible party, tagged **[RE]**, **[UDOFIN]** or **[RE→UDOFIN contract]**;
   - system control;
   - evidence produced;
   - test case;
   - open questions.
3. Keep confirmed legal requirements separate from interpretations, recommendations and assumptions. Never claim regulatory compliance merely because a feature exists.
4. **Most RBI obligations bind the RE, not Udofin.** Udofin is an LSP: an agent of the RE that carries out part of the RE's digital lending functions under a contract (CF para 4(1)(xix)). An RBI Direction reaches Udofin through three routes only:
   - the RE must ensure that its LSP and DLAs comply (CF paras 6(6), 13–16);
   - the RE must put specific terms in the LSP and outsourcing contracts (CF para 22; OUT paras 33–34, 74);
   - the RE needs data, evidence or system behaviour from Udofin to discharge its own obligation (for example CIMS DLA reporting under CF para 18, or the 6-hour incident clock under OUT para 61).
   Record the route for every REQ-ID. Never design a control that makes Udofin the decision-maker for a function the RE cannot outsource (OUT para 15; KYC para 13).
5. Never assume one obligation applies identically to every RE. Applicability depends on:
   - entity type (NBFC / HFC / bank / UCB);
   - layer and asset size (CYB chapter; FRM; CMP; OUT Chapter IV scope);
   - deposit-taking status;
   - s.11A PML Act notification status (Aadhaar e-KYC authentication);
   - product (microfinance by household income, CF para 51; secured; short tenor);
   - channel (Android app, iOS app, borrower web app, lender portal).
   Store these as RE profile attributes in U1 and drive every rule pack from them.
6. On **28 November 2025** RBI repealed 9,445 circulars and issued 244 entity-wise Master Directions. On **31 July 2026** it issued **64 Department of Supervision Directions**, repealing a further 628 circulars. Older circular references (including the 2022 Digital Lending Guidelines and the Digital Lending Directions, 2025 of 8 May 2025) are legacy. Cite the new Directions; keep the legacy reference only for traceability.
7. The supplied texts are NBFC versions. For a bank, HFC or UCB partner, load the counterpart Direction for that RE type and re-verify each REQ-ID before go-live with that RE.
8. **App-store policies are binding release conditions, not law.** Google Play and Apple can remove the app. Record their requirements in the same register with strength flag "platform policy" and re-check them before every store submission (Phase 17).
9. **DPDP and RBI rules apply together.** Where both apply, implement the stricter control. Where RBI, PMLA or CIC rules require retention, record that legal basis against the erasure exception in the retention engine (U4).

## 8.2 Starting register

All items need confirmation against the primary text. The 8A section named in each row holds the verified paragraph-level requirements.

| Instrument | Relevance to Udofin | Status |
|---|---|---|
| CF — Credit Facilities Directions, 2025 (RBI/DOR/2025-26/347), Chapter III Digital Lending (paras 6–30) and Ch V microfinance (51–62) | Core LSP rulebook: LSP contract and due diligence (6); multi-lender offer view without dark patterns (7); KFS and auto-flow of signed documents (9); RE-to-borrower funds flow and no LSP fees from borrowers (10); cooling-off (11); nodal GRO on the DLA (12); need-based data with minimal permissions (13); minimal storage, no biometrics, India-only (14); privacy policy (15); CIMS DLA reporting (18); DLG (19–29); household-income test for microfinance (51) — Part 8A.1 | Verified (copy updated as on 1 Apr 2026) |
| CIR — Credit Information Reporting Directions, 2025 (349), as amended by RBI/DOR/2025-26/117 (4 Dec 2025, effective 1 Jul 2026) | Udofin is not a CIC member (CIR para 6 binds the RE); bureau pulls run under the RE's membership; Udofin supplies data for the RE's reporting, alerts and complaint handling; no auto-rejection of first-time borrowers in Udofin pre-screens (38(5)) — Part 8A.2 | Verified (original text); amendment not in supplied copy [VERIFY] |
| KYC — Know Your Customer Directions, 2025 (361) | RE owns the KYC decision (13); CDD modes and Aadhaar use (23); digital KYC (24); OTP e-KYC NFTF term-loan cap ₹60,000 a year (25(5)); V-CIP on RE premises or RE-owned cloud by RE officials (26–27); CKYCR (63) — Part 8A.3 | Verified (updated as on 29 Dec 2025) |
| AA — Account Aggregator Directions, 2025 (368) | Governs NBFC-AAs. The RE is the FIU; Udofin is a technology service provider; data used only as the consent artefact allows (28) — Part 8A.4 | Verified (derived FIU-side obligations) |
| MFI — Microfinance Institution Directions, 2025 (371) | Partner NBFC-MFIs; 25% cap on microfinance loans for non-MFI NBFCs (49) affects routing capacity — Part 8A.5 | Verified |
| RBC — Responsible Business Conduct Directions, 2025 (362) | Vernacular communication and FPC (9–21); KFS with proposal number, validity period and APR (29, Annex I); penal charges (30); prepayment (33–34); recovery agents, DSA/DMA and telemarketers (93–101); Supreme Court order on accessible digital KYC (105) — Part 8A.6 | Verified (updated as on 1 Apr 2026); Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026, in force 1 Jan 2027; paras 89–100 replaced by 100A–100AB) confirmed from the RBI notification, official text not supplied; Second Amendment not supplied [VERIFY] |
| Recovery and ADR law: A&C Act 1996 (ss.3, 7, 11, 12, 21, 29A, 29B, 34, 36, 62, 73–74); Mediation Act 2023 (ss.4–25 and 27–30 not in force; s.26 in force); LSA Act 1987 (ss.19–22E); NI Act s.138; PSS Act s.25; SARFAESI Act; RDB Act; IBC | The RE's remedies; Udofin never refers, issues notices or litigates and only shows status the RE permits — Part 7A | Status per Part 7A.0.1; Mediation Act commencement [VERIFY on egazette] |
| OUT — Managing Risks in Outsourcing Directions, 2025 (363) | Udofin is the RE's service provider: non-outsourceable functions (15); ownership bar (18(vi), 59); contract clauses (33–34, 74); isolation in multi-tenant platforms (26–27, 70); grievances stay with the RE (54–57); 6-hour cyber clock from Udofin's detection (61); cloud controls (97) — Part 8A.7 | Verified; existing IT agreements had to comply by renewal or 10 Apr 2026 (para 2) |
| CYB — Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions, 2026 (461) | RE obligations Udofin must support (paras 28, 33 and 62 are in Ch IV, BL ≥ ₹500 crore; paras 105–141 are in Ch V, ML and above): mobile financial services end-to-end encryption (33); DAKSH reporting within 6 hours (28, 141); vendor contract terms and admin audit logs (62); source code or escrow (105); vendor vulnerability certificate (106); VA/PT (121–126); DR (129–138) — Part 8A.8 | Verified (31 Jul 2026) |
| FRM — Fraud Risk Management Directions, 2026 (463) | RE fraud classification and EWS; Udofin supplies fraud signals and is a "third-party service provider" that may receive a show-cause notice (6(1)) and be held accountable by contract (31) — Part 8A.9 | Verified (UL, ML and BL ≥ ₹500 crore) |
| WD — Wilful and Large Defaulters Directions, 2025 (358) | The bar on further finance to listed wilful defaulters applies to all REs (para 2); routing must honour the RE's decline, never override it — Part 8A.10 | Verified |
| DPS — Digital Payment Security Controls Directions, 2026 (462) | Binds credit-card-issuing NBFCs only. Udofin adopts web (67) and mobile (68) controls as its voluntary baseline: device binding, version sunset within 6 months, root/jailbreak checks, no sensitive data on device — Part 8A.11 | Verified; voluntary baseline [interpretation] |
| CMP — Compliance Function Directions, 2026 (460) | ML/UL REs' product and process approval (9(7), 31) covers Udofin-sourced products and DLA changes — Part 8A.12 | Verified |
| GOV — Governance Directions, 2025 (344) | RE's CRO product vetting (19–24) and whistle-blower mechanism — Part 8A.12 | Verified |
| IAF — Internal Audit Function Directions, 2026 (464) | RE internal audit universe includes outsourced LSP activity; Udofin gives auditor access — Part 8A.12 | Verified |
| SA — Statutory Audit Directions, 2026 (465) | Statutory auditors of the RE may request Udofin evidence — Part 8A.12 | Verified |
| AUD — Auditor's Report Directions, 2026 (468) | RE auditor reporting; Udofin supplies evidence packs on request — Part 8A.12 | Verified |
| IRACP — Income Recognition, Asset Classification and Provisioning Directions, 2025 (356) | Classification stays with the RE; DLG in ECL (36A–36C) uses Udofin's DLG data; loan mirror shows RE classification only — Part 8A.13 | Verified (updated as on 13 Feb 2026) |
| RSA — Resolution of Stressed Assets Directions, 2025 (357) | Settlement and restructuring decisions are RE decisions; Udofin only relays offers and outcomes — Part 8A.13 | Verified |
| CAP — Capital Adequacy Directions, 2025 (345) | RE capital treatment of DLG-covered portfolios (CF para 26); Udofin supplies DLG positions — Part 8A.13 | Verified |
| TDCR — Transfer and Distribution of Credit Risk Directions, 2025 (352) | Co-lending (Part B): repayment into the co-lending escrow (CF 10(1) Note); originator DLG ≤ 5% (123); partner list on website (126) — Part 8A.13 | Verified |
| SR — Supervisory Returns Directions, 2026 (466) | RE returns; Udofin supplies DLA and sourcing data with lineage — Part 8A.14 | Verified |
| MISC — Miscellaneous Directions, 2025 (373) | No fresh PDCs or EMI cheques where NACH is available (23); nearest-rupee rounding (27) — Part 8A.14 | Verified (updated as on 26 Feb 2026) |
| SBR — Scale Based Regulation Directions, 2025 (339) | RE layer drives applicability of CYB, OUT, FRM and CMP to each partner — Part 8A.14 | Verified (original text); any 2026 amendment [VERIFY] |
| ORM — Guidance Note on Operational Risk Management and Operational Resilience (DOR.ORG.REC.301/14.10.001/2025-26) | Guidance, not a Direction: third-party due diligence (73), supply-chain responsibility (76), impact tolerances (31–33), lessons learned (99–101) — Part 8A.14 | Verified; strength flag "guidance" |
| CRM — Credit Risk Management Directions, 2025 (350) | No direct Udofin obligation; related-party, LEI and CERSAI gates run at the RE — Part 8A.15 | Verified |
| CON — Concentration Risk Management Directions, 2025 (351) | No direct obligation; RE exposure limits may cap routing capacity — Part 8A.15 | Verified |
| INV — Investment Portfolio Directions, 2025 (354) | No Udofin obligation — Part 8A.15 | Verified |
| BR — Branch Authorisation Directions, 2025 (342) | No Udofin obligation (Udofin offices are not RE branches) — Part 8A.15 | Verified |
| ALM — Asset Liability Management Directions, 2025 (355) | No Udofin obligation — Part 8A.15 | Verified |
| FS — Financial Statements Directions, 2025 (359) | No Udofin obligation; DLG data may feed RE disclosures — Part 8A.15 | Verified |
| CLM — Climate Finance Directions, 2025 (364) | No Udofin obligation (deposit-taking REs only) — Part 8A.15 | Verified |
| DIV — Declaration of Dividends Directions, 2025 (360) | No Udofin obligation — Part 8A.15 | Verified |
| SEC — Securitisation Transactions Directions, 2025 (353) | No Udofin obligation; pool data comes from the RE's LMS — Part 8A.15 | Verified |
| MSD — Miscellaneous Supervisory Directions, 2026 (467) | No direct obligation; interest from actual disbursement and revised schedules on part-disbursement (7) govern what the loan mirror displays — Part 8A.15 | Verified |
| Internal Ombudsman Directions, 2026 (14 Jan 2026) and Reserve Bank – Integrated Ombudsman Scheme, 2026 (RB-IOS 2026; effective 1 Jul 2026) | Complaint escalation path shown on the DLA; 30-day RE reply window before CMS escalation (CF para 12(4)) — U15 | Not supplied [VERIFY: texts not supplied] |
| Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E), notified 13 Nov 2025) | Udofin is a data fiduciary for its own processing and a processor for the RE where it acts on the RE's instructions [interpretation]. Board rules in force from 13 Nov 2025; consent-manager rule (Rule 4) from 13 Nov 2026; notice, consent, rights, security safeguards, breach intimation (72-hour detailed report), 1-year log retention (Rule 8(3)), 90-day rights response (Rule 14(3)), children's data (s.9) and penalties from 13 May 2027. Proposal to compress the SDF timeline not gazetted — U4 | In force in phases [VERIFY: Gazette texts and any compression] |
| Information Technology Act, 2000 s.43A and SPDI Rules, 2011 | Reasonable security practices for sensitive personal data until DPDP s.44(2) omits s.43A — U4, U24 | In force until the DPDP substantive date [VERIFY: commencement of s.44] |
| IT Act, 2000 s.3A, s.5 and Second Schedule (eSign); First Schedule exclusions; Indian Contract Act, 1872 s.10 | Aadhaar/other e-KYC eSign through licensed ESPs; physical execution path for excluded instruments (negotiable instruments other than cheques, powers of attorney, trusts, wills, immovable-property conveyances) — U9 | In force |
| Indian Stamp Act, 1899 and state stamp Acts; e-stamping through SHCIL (CRA) and state portals | Stamp duty by state of execution; eStamp evidence stored with the agreement — U9 | In force; state-wise rates [VERIFY] |
| Aadhaar Act, 2016 (ss.4, 8, 8A, 29), Aadhaar (Authentication and Offline Verification) Regulations, 2021, Aadhaar Good Governance Amendment Rules, 2025 (31 Jan 2025); PML Act s.11A; UIDAI Circular No. 14 of 2025 (Aadhaar Data Vault) | Aadhaar OTP e-KYC only by REs notified under s.11A acting as KUA or sub-KUA; offline verification (OKYC XML, QR) as OVSE; Udofin never stores the Aadhaar number; ADV duty sits with the requesting entity — U5 | In force; Circular 14 supersedes Circular 8 of 2025 [VERIFY] |
| IT (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules, 2016, Rule 9A (2017) | DigiLocker-issued documents are deemed at par with originals; the requester entity (preferably the RE) must be onboarded with DigiLocker and fetch each document with the borrower's consent — U5 | In force [VERIFY requester terms for an LSP acting for the RE] |
| PMLA 2002 and PML (Maintenance of Records) Rules, 2005 | RE is the reporting entity (CDD, STR/CTR, records 5 years); Udofin supplies evidence and flags, never files — U5, U18 | In force |
| Credit Information Companies (Regulation) Act, 2005, CIC Rules and Regulations, 2006 | Credit information is disclosed to members and specified users (CICRA s.2(l)); Udofin is neither today, so pulls run under the RE's membership with borrower consent, or as a borrower-initiated own-report. CIC Regulations reg. 3 (amended 10 Nov 2021) lets an entity processing information for credit institutions become a specified user if it meets RBI's criteria of 5 Jan 2022 (Indian-owned and controlled, net worth ≥ ₹2 crore, 3 years' experience, CISA certification); assess as a later option — U6 | In force [VERIFY: current criteria and CIC acceptance] |
| Payment and Settlement Systems Act, 2007 (incl. s.25); RBI (Regulation of Payment Aggregators) Directions, 2025 (15 Sep 2025); NPCI eNACH and UPI AutoPay rules | Gateways collect into the RE's merchant account only; PA-only entities are outside CF (para 4(1)(xix) proviso); UPI AutoPay and card e-mandate debits above ₹15,000 need an additional factor, except up to ₹1 lakh for mutual-fund subscriptions, insurance premiums and credit-card bill payments (RBI, 12 Dec 2023); some PSPs also apply ₹1 lakh to lending MCCs, which is not in the RBI circular [VERIFY NPCI circular before relying on it for EMIs above ₹15,000] — U11 | In force |
| Consumer Protection Act, 2019 and CCPA Guidelines for Prevention and Regulation of Dark Patterns, 2023 | Offer comparison and journey design free of dark patterns (CF para 7(4) Note) — U7, U8, U23 | In force |
| TRAI Telecom Commercial Communications Customer Preference Regulations, 2018 (TCCCPR) as amended 12 Feb 2025; TRAI direction of 19 Nov 2025 on 1600-series numbers for RBI-regulated entities | DLT-registered headers and templates; 140 series for promotional and 1600 series for service and transactional calls; consent and opt-out windows; the RE's 1600 obligation extends to calls made on its behalf [VERIFY: TRAI text] — U16, U13 | In force (direction of 19 Nov 2025: commercial banks from 1 Jan 2026; large NBFCs, payments banks and small finance banks from 1 Feb 2026; other NBFCs, co-operative banks and RRBs from 1 Mar 2026) [VERIFY: TRAI text] |
| CERT-In Directions under s.70B(6) IT Act (28 Apr 2022) | Udofin itself must report specified cyber incidents to CERT-In within 6 hours, keep ICT logs for 180 days within India and synchronise clocks to NTP (NIC/NPL) — U24 | In force |
| Rights of Persons with Disabilities Act, 2016; Supreme Court order of 30 Apr 2025 (Pragya Prasun; Amar Jain) referred to in RBC para 105 | Accessible digital KYC and app journeys (WCAG 2.2 AA, alternatives to blink-based liveness) — U3, U5 | In force [VERIFY: order text] |
| Google Play Developer Policy — Financial Services (Personal Loans) and India country requirements | App must be on RBI's "DLAs deployed by Regulated Entities" list before it is first published (new apps from 30 Oct 2025; existing apps by 28 Jan 2026), including facilitator apps, with the partner REs' licences submitted; facilitator declaration; names of all partner NBFCs and banks in the description; minimum/maximum repayment period, maximum APR and representative total cost in metadata; no apps promoting personal loans repayable in full in 60 days or less; prohibited permissions include READ_CONTACTS, READ_EXTERNAL_STORAGE, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, ACCESS_FINE_LOCATION, READ_PHONE_NUMBERS, QUERY_ALL_PACKAGES, WRITE_EXTERNAL_STORAGE — U23, Phase 17 | Platform policy; checked Oct 2026 |
| Apple App Store Review Guidelines 3.2.2(ix), 5.1.1(iii) and (ix), 2.5.2; Developer Program License Agreement 3.3 | Personal loan apps: disclose maximum equivalent APR and due date; maximum APR 36% including costs and fees; no loans repayable in full in 60 days or less; app submitted by a legal entity; data minimisation; interpreted-code updates only within the app's purpose — U23, Phase 17 | Platform policy; checked Oct 2026 |
| Companies Act, 2013 | A DLG provider must be incorporated as a company under it (CF para 19); Udofin's statutory auditor certifies the DLG declaration (CF para 20(3)) — U14, U17 | In force |
| Depositories Act, 1996 and NSDL/CDSL pledge procedures; SEBI requirements on pledge of securities | Loan against securities: pledge created in favour of the RE, never Udofin — Phase 18 | In force [VERIFY: current pledge APIs] |
| RBI FREE-AI Framework (Aug 2025); draft Guidance on Model Risk Management (Jun 2026) | Governance of U20 AI features used for RE processes — U20 | Framework / draft [VERIFY] |

---

# PART 8A — REQUIREMENTS FROM THE RBI DIRECTIONS SUPPLIED BY THE PROJECT OWNER (LSP lens; verified against the official texts)

## 8A.0 How to use this Part

The project owner supplied the official RBI texts of 33 Directions and 1 guidance note (the same set as Finbyx v1.3). Each was read in full. This Part restates them **from Udofin's side**: what the partner Regulated Entity (RE) must do, what it must flow down to Udofin by contract, and what Udofin must build or evidence.

### 8A.0.1 Rules for Claude Code

1. **Store the source texts** in `docs/regulations/rbi/` (file name = RBI number) and record each file's SHA-256 hash and "updated as on" date in `docs/regulations/index.md`.
2. **One ecosystem register.** Requirement IDs are identical to Finbyx (`REQ-<code>-<para>`, for example `REQ-CF-10(5)`), so a requirement implemented on both sides of the Finbyx ↔ Udofin contract has one ID. Load every requirement below into the U18 regulatory register.
3. **Actor tags.** Every requirement is tagged **[RE]** (the lender's own obligation; Udofin supplies data or a channel), **[UDOFIN]** (Udofin must build or do it) or **[RE→UDOFIN contract]** (the RE must impose it on Udofin through the LSP or outsourcing agreement). A requirement tagged [RE] is never implemented as a Udofin decision.
4. **Status of [VERIFY] items.** Paragraphs cited here were checked against the supplied copies. Anything marked [VERIFY] — amendments issued after a copy's "updated as on" date, non-RBI law, platform policies and interpretations — must be checked before the related module is built and the result recorded in the register.
5. **Law, interpretation, recommendation.** Record which one each control implements. Udofin-only design choices that go beyond the text (for example a 2-hour incident notice to the RE) are recommendations, not law.
6. **Drafting slips** in the official texts are listed in Appendix F. Implement the evident intent, record it in `docs/regulations/errata.md`, and never "fix" a slip silently in code.
7. **Still to be supplied:** the Internal Ombudsman Directions and RB-IOS 2026; the RBC Second and Third Amendment Directions, 2026; the HFC Directions; Directions for commercial-bank REs; the PPG.66 repeal circular; a later SBR copy.

### 8A.0.2 Directions and guidance covered

The "Applies to" column describes the REs the text binds. Udofin's relevance is in Part 8.2 and in each section below.

| Code | Direction (all "Reserve Bank of India (Non-Banking Financial Companies – …) Directions") | RBI number and reference | Date / version supplied | Applies to (summary) |
|---|---|---|---|---|
| CF | Credit Facilities, 2025 | RBI/DOR/2025-26/347; DOR.CRE.REC.No.266/07-01-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 | NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and **HFCs** (para 3(1)); partial for BL with customer interface but no public funds, CICs, P2P (para 3(2)) |
| CIR | Credit Information Reporting, 2025 | RBI/DOR/2025-26/349; DOR.FIN.REC.No.268/20.16.056/2025-26 | 28 Nov 2025 (original text). Amended by RBI/DOR/2025-26/117 (DOR.FIN.REC.No.324/20.16.056/2025-26, 4 Dec 2025, effective 1 Jul 2026), which substitutes paras 10(2) and 15, inserts para 12(10) and adds Annex VI; the amendment is not in the supplied copy | All lending NBFCs including HFC, P2P and CIC; not MGC, AA, SPD, NOFHC, or NBFCs without customer interface (para 3) |
| CRM | Credit Risk Management, 2025 | RBI/DOR/2025-26/350; DOR.CRE.REC.No.269/07-02-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendment of 5 Jan 2026) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC; paras 6–8 only for "Notified NBFCs" (NBFC-Factor, NBFC-D, non-deposit NBFCs ≥ ₹500 crore) |
| CON | Concentration Risk Management, 2025 | RBI/DOR/2025-26/351; DOR.CRE.REC.270/07-03-008/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendments of 1 Jan and 10 Mar 2026) | NBFC-D, ICC, Factor, MFI, IFC, IDF; HFCs except paras 7, 14, 16, 19, 22, 23 |
| INV | Classification, Valuation and Operation of Investment Portfolio, 2025 | RBI/DOR/2025-26/354; DOR.MRG.REC.No.273/00-00-014/2025-26 | 28 Nov 2025 | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, CIC |
| BR | Branch Authorisation, 2025 | RBI/DOR/2025-26/342; DOR.RAUG.REC.No.261/23-27-013/2025-26 | 28 Nov 2025, updated as on 15 Apr 2026 | NBFCs and HFCs (paras 6 and 12 deposit-taking only); CICs paras 10, 13–15 |
| ALM | Asset Liability Management, 2025 | RBI/DoR/2025-26/355; DoR.LRG.REC.No.274/13-10-004/2025-26 | 28 Nov 2025 | All layers incl. HFC; CICs except Ch III. Ch II only if assets ≥ ₹100 crore; Ch III (LCR) only for NBFC-D and NBFC-ND ≥ ₹5,000 crore |
| FS | Financial Statements: Presentation and Disclosures, 2025 | RBI/DOR/2025-26/359; DOR.ACC.REC.No.278/21.04.018/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (para 21(9A) inserted 5 Jan 2026) | All incl. HFC, CIC; C.1 all, C.2 ML/UL, C.3 UL |
| CLM | Climate Finance and Management of Climate Change Risks, 2025 | RBI/DOR/2025-26/364; DOR.SFG.REC.No.283/30.01.021/2025-26 | 28 Nov 2025 | **Only NBFC-D and deposit-taking HFCs.** In substance a green-deposit framework |
| AA | Account Aggregator, 2025 | RBI/DoR/2025-26/368; DoR.FIN.REC.No.287/03-10-123/2025-26 | 28 Nov 2025 | NBFC-AAs only; FIU-side obligations derived |
| CMP | Compliance Function, 2026 | RBI/DoS/2026-27/460; DoS.CO.PPG.54/11.01.005/2026-27 | 31 Jul 2026 | **Middle and Upper Layer only** |
| CYB | Cybersecurity, Technology: Risk, Resilience and Assurance Framework, 2026 | RBI/DoS/2026-27/461; DoS.CO.CSITEG.55/31.01.015/2026-27 | 31 Jul 2026, immediate effect | All NBFCs incl. HFC: Ch II all; Ch III BL < ₹500 crore and all CICs; Ch IV BL ≥ ₹500 crore; Ch V TL/UL/ML excluding CICs |
| DPS | Digital Payment Security Controls, 2026 | RBI/DoS/2026-27/462; DoS.CO.CSITEG.56/31.01.015/2026-27 | 31 Jul 2026 | **Credit-card-issuing NBFCs only** |
| FRM | Fraud Risk Management, 2026 | RBI/DoS/2026-27/463; DoS.CO.FMG.57/23.04.001/2026-27 | 31 Jul 2026 | UL, ML, and BL with assets ≥ ₹500 crore (audited 31 March balance sheet), incl. HFCs (HFC reporting to NHB) |
| AUD | Auditor's Report, 2026 | RBI/DoS/2026-27/468; DoS.CO.ARG.62/08.91.001/2026-27 | 31 Jul 2026; first applies to FY ending on or after that date | Every NBFC auditor (HFC auditors excluded) |
| IRACP | Income Recognition, Asset Classification and Provisioning, 2025 | RBI/DOR/2025-26/356; DOR.STR.REC.No.275/21.04.048/2025-26 | 28 Nov 2025, updated as on 13 Feb 2026 (paras 36A–36C inserted) | NBFC-D, ICC, Factor, IFC, IDF (para 3); HFC, MFI, MGC, CIC subject to their own Directions, which prevail (paras 4–7); not P2P, AA, SPD, NOFHC or the two no-public-funds categories (para 10) |
| RSA | Resolution of Stressed Assets, 2025 | RBI/DOR/2025-26/357; DOR.STR.REC.276/21.04.048/2025-26 | 28 Nov 2025 (original; no "updated as on" date) | NBFC-D, ICC, Factor, MFI, IFC, IDF (para 3). Part A: NBFC-D and ND ≥ ₹500 crore; Part B: ND < ₹500 crore (paras 7–8, 157–158). HFC paras 86–138 only; MGC 86–100; not CIC, P2P, AA, SPD, NOFHC or the no-public-funds categories (paras 4–6) |
| RBC | Responsible Business Conduct, 2025 | RBI/DOR/2025-26/362; DOR.MCS.REC.No.281/01-01-039/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (para 42 and Annex II deleted w.e.f. 1 Apr 2026). Second Amendment (15 Jun 2026, Ch IIIA) and Third Amendment (RBI/2026-27/230, 6 Aug 2026, in force 1 Jan 2027; paras 89–100 replaced by 100A–100AB) not in the supplied copy; the Third Amendment is confirmed from the RBI notification [VERIFY: official text not supplied] | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, all layers; P2P paras 98–100 only; not MGC, CIC, AA, SPD, NOFHC or NBFCs without customer interface (paras 3–5) |
| WD | Treatment of Wilful Defaulters and Large Defaulters, 2025 | RBI/DOR/2025-26/358; DOR.FIN.REC.No.277/20-16-003/2025-26 | 28 Nov 2025 (original text; immediate effect) | **ML and above:** NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, CIC; not MGC, P2P, AA, SPD, NOFHC, or NBFCs without public funds and customer interface. The bar on further finance and the large-defaulter provisions apply to all REs (para 2) |
| KYC | Know Your Customer, 2025 | RBI/DOR/2025-26/361; DOR.AML.REC.No.280/14.01.003/2025-26 | 28 Nov 2025, updated as on 29 Dec 2025 (Explanation to para 63(9), CKYCR reliance, inserted w.e.f. 29 Dec 2025) | All NBFC categories and layers; not NBFCs without customer interface (para 3); overseas branches and subsidiaries (para 4). Aadhaar e-KYC authentication only for NBFCs notified under PML Act s.11A |
| TDCR | Transfer and Distribution of Credit Risk, 2025 | RBI/DOR/2025-26/352; DOR.STR.REC.271/21.04.048/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, all layers. Not MGC, P2P, AA, CIC, SPD, NOFHC or non-public-fund NBFCs (para 3). Part B (co-lending) from 1 Jan 2026 or an earlier date set by internal policy (paras 2, 95) |
| SEC | Securitisation Transactions, 2025 | RBI/DOR/2025-26/353; DOR.STR.REC.272/21.04.177/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | As TDCR (para 3). NBFCs as originators, investors and facility providers |
| CAP | Prudential Norms on Capital Adequacy, 2025 | RBI/DOR/2025-26/345; DOR.CAP.REC.264/21-01-002/2025-26 | 28 Nov 2025, updated as on 1 Apr 2026 (Amendments of 1 Jan 2026, effective 1 Apr 2026, and 10 Mar 2026) | NBFC-D, ICC, Factor, IFC, IDF, MFI by layer; HFC, MGC, CIC and SPD for listed paras only; not P2P, AA, NOFHC or no-public-funds NBFCs (para 3) |
| SBR | Registration, Exemptions and Framework for Scale Based Regulation, 2025 | RBI/DOR/2025-26/339; DOR.FIN.REC.No.258/03.10.119/2025-26 | 28 Nov 2025 (original text; no "updated as on" date; any 2026 amendment not in the copy) | All registered NBFCs incl. Government companies; Ch IV exemptions for specified non-banking institutions |
| DIV | Prudential Norms on Declaration of Dividends, 2025 | RBI/DOR/2025-26/360; DOR.ACC.REC.279/21.02.067/2025-26 | 28 Nov 2025 | All layers incl. HFC, MGC, SPD, CIC, P2P, AA; not NOFHC |
| MISC | Miscellaneous, 2025 | RBI/DOR/2025-26/373; DOR.FIN.REC.No.292/03-10-119/2025-26 | 28 Nov 2025, updated as on 26 Feb 2026 | Ch II all layers; Ch III ML+; Ch IV Factors; Ch V IDF; HFC, MGC, SPD, P2P, AA and CIC per para 3(1); not NOFHC |
| GOV | Governance, 2025 | RBI/DOR/2025-26/344; DOR.GOV.REC.No.263/18-10-013/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | BL Ch III; ML Ch II–IV; UL Ch II–V, incl. HFC; CIC/MGC/SPD/AA/P2P partial (para 3); not NOFHC; paras 29–37 not for government-owned NBFCs |
| OUT | Managing Risks in Outsourcing, 2025 | RBI/DOR/2025-26/363; DOR.ORG.REC.No.282/21-04-158/2025-26 | 28 Nov 2025 (original text; no "updated as on" date); existing IT agreements compliant by renewal or 10 Apr 2026 (para 2) | NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, SPD, CIC, P2P, AA; BL excludes Ch IV and the IT parts of Ch II; MGC (ML+) Ch IV; not NOFHC |
| ORM | Guidance Note on Operational Risk Management and Operational Resilience, 2025 (**guidance, not a Direction**) | RBI/2025-26/[number blank in supplied copy]; DOR.ORG.REC.301/14.10.001/2025-26 | 28 Nov 2025 | Banks (incl. SFB, PB, LAB), RRBs, UCBs, RCBs, AIFIs (incl. NHB), NBFC-BL/ML/UL (para 8); HFCs by implication (9(14)(iii)); BL = "smaller RE" (12(2)) |
| MFI | Microfinance Institution, 2025 | RBI/DOR/2025-26/371; DOR.FIN.REC.290/03-10-038/2025-26 | 28 Nov 2025 (original text; no "updated as on" date) | Every NBFC-MFI (non-deposit-taking; ≥ 60% qualifying assets) (paras 3, 8(3)); para 49 (25% cap on microfinance loans) binds all NBFCs |
| IAF | Internal Audit Function, 2026 | RBI/DoS/2026-27/464; DoS.CO.PPG.58/11.01.005/2026-27 | 31 Jul 2026, immediate effect | All NBFC-D and HFC-D; NBFC-ND and HFC-ND with assets ≥ ₹5,000 crore (para 3) |
| SA | Statutory Audit, 2026 | RBI/DoS/2026-27/465; DoS.CO.ARG.59/08.91.001/2026-27 | 31 Jul 2026, immediate effect | All NBFCs incl. HFCs for SCA/SA appointment; NBFC-ND < ₹1,000 crore may continue extant procedure (para 3) |
| SR | Supervisory Returns, 2026 | RBI/DoS/2026-27/466; DoS.CO.DSG.60/33.01.001/2026-27 | 31 Jul 2026, immediate effect | All NBFCs, all layers, **HFCs excluded** (para 3); return-wise applicability in para 21 |
| MSD | Miscellaneous Supervisory, 2026 | RBI/DoS/2026-27/467; DoS.CO.PPG.61/11.01.005/2026-27 | 31 Jul 2026, immediate effect | NBFCs and HFCs (para 3); Ch II UL/ML with ≥ 10 fixed point service delivery units; Ch III incl. HFCs and MFIs; Ch IV NBFC-D excl. HFCs; Ch V NBFC-D and ML/UL/TL NBFC-ND excl. no-public-funds NBFCs, PDs, HFCs |

---

## 8A.1 CF — Credit Facilities Directions (347)

**Source:** RBI/DOR/2025-26/347; DOR.CRE.REC.No.266/07-01-008/2025-26; 28 Nov 2025, updated as on 1 Apr 2026. Chapter III (Digital Lending, paras 6–30) is the core of Udofin's regulatory position. Chapter V (Microfinance, paras 51–62) applies to any Udofin product reaching a low-income household. Annex-I (CIMS DLA data) was checked against the image in the official PDF.

### Applicability to Udofin

- **Through the RE's contract (primary route).** The Directions bind NBFCs and HFCs (para 3(1), which lists HFCs at (vii)), not LSPs. Udofin is bound because:
  - each RE must "ensure that the LSPs engaged by them and the DLAs (either of the NBFC or of the LSPs engaged by the NBFC) comply with these Directions" (para 6(6));
  - the RE "shall remain fully responsible and liable for all acts and omissions of the LSP" (para 6(7)).
- **Directly, in substance.** Several obligations are written in the LSP's own name. Udofin must treat them as its own obligations, even though RBI enforces them through the RE:
  - the multi-lender offer view (para 7);
  - the LSP nodal grievance officer (para 12(1));
  - the LSP's storage policy disclosure (para 14(2));
  - the LSP's privacy policy (para 15(1));
  - DLG portfolio publication (para 28).
- **Bank REs.** Where the partner RE is a bank, the corresponding commercial-bank Directions apply instead of 347. Their substance is expected to be the same, but they were not supplied [VERIFY: obtain the commercial bank Credit Facilities / Digital Lending Directions and map any differences].
- **Definitions that fix Udofin's position (para 4(1)):**
  - **LSP**, para 4(1)(xix): "an agent of an NBFC (including another lender) who carries out one or more of NBFC's digital lending functions, or part thereof, in customer acquisition, services incidental to underwriting and pricing, servicing, monitoring, recovery of specific loan or loan portfolio on behalf of the NBFC in conformity with extant outsourcing guidelines". Udofin is an LSP of every partner RE, and is also an outsourcing service provider under OUT (see 8A.7).
  - **DLA**, para 4(1)(x): "a mobile and / or web-based applications, on a standalone basis or as a part of suite of functions of an application with user interface that facilitate digital lending services". The Android app, the iOS app and the borrower web app/PWA are each a DLA of each partner RE.
  - **Digital lending**, para 4(1)(ix): "a remote and automated lending process … for customer acquisition, credit assessment, loan approval, disbursement, recovery, and associated customer service".
  - **DLG**, para 4(1)(viii): any contract under which another entity compensates the NBFC for default losses up to a percentage of the portfolio specified upfront. Any **implicit guarantee** of a similar nature linked to portfolio performance is also DLG.
  - **APR** has the RBC meaning (para 4(1)(ii); defined in RBC para 6(1); computation sheet in the KFS under RBC para 29(3)). The KFS itself is governed by RBC (para 9(1); see 8A.6).
  - The PA proviso in para 4(1)(xix) says that a PA acting as an LSP complies with "Chapter IV". The evident intent is Chapter III (drafting slip; see Appendix F).
- **Terminology.** The 2025 Directions use "cooling-off period" (para 11). The older term "look-up period" must not be used in the UI or in contracts.

### LSP engagement and RE due diligence (para 6)

- `REQ-CF-6(1)` **[RE→UDOFIN contract]** Digital lending through Udofin happens only under a contract that "clearly defines the respective roles, rights, and obligations of each party".
  - *Build:* U1 LSP agreement registry with versioned contract metadata (scope of LSP functions, DLAs covered, recovery-agent appointment yes/no, DLG yes/no, data scope, effective dates). A tenant cannot go live without an active agreement record.
- `REQ-CF-6(2)` **[RE]** Before contracting, the RE conducts enhanced due diligence on: the LSP's technical capabilities; the robustness of its data privacy policies and storage systems; fairness in its conduct with borrowers; its past record of conduct; its ability to comply with all applicable regulations and statutes.
  - *Build:* U18 "RE due-diligence pack" generator (security certifications, VAPT summaries, privacy and storage policies, grievance statistics, DLA register, sub-processor list) with a versioned evidence index.
- `REQ-CF-6(3)` **[RE]** The RE periodically reviews the LSP's conduct against the contract. `REQ-CF-6(4)` **[RE]** The RE sets policy-based monitoring of portfolios originated through LSPs.
  - *Build:* U19 lender dashboards (funnel, approval and rejection rates, complaint rates, DPD by vintage for Udofin-sourced loans) and a U18 audit-access role for RE reviewers.
- `REQ-CF-6(5)` **[RE→UDOFIN contract]** Where Udofin acts as recovery agent, the RE guides it to comply with RBC and related instructions.
  - *Build:* U13 is enabled per RE only when the U1 agreement records a recovery-agent appointment. RBC conduct rules are loaded as U13 policy (see 8A.6).
- `REQ-CF-6(6)` `REQ-CF-6(7)` **[RE→UDOFIN contract]** Udofin and its DLAs comply with these Directions and with OUT. Outsourcing never dilutes the RE's liability.
  - *Build:* U18 maps every REQ-CF item to a control and to evidence the RE can inspect.

### Multi-lender offer display (para 7)

Udofin has agreements with several lenders, so para 7 applies to every offer journey.

- `REQ-CF-7(1)` **[UDOFIN]** Show "a digital view of all the loan offers matching the borrower's request on the DLA". "The name of the unmatched lenders shall also be disclosed in the digital view."
  - *Build:* U7 routing returns matched and unmatched lender sets for each request. U8 renders both. Suppressing an unmatched lender's name is not configurable.
- `REQ-CF-7(2)` **[UDOFIN]** Any matching mechanism may be used, but it must follow "a consistent approach for similarly placed borrowers and products". The mechanism and every change to it are documented.
  - *Build:* U7 matching rules run in GoRules ZEN as versioned decision models. Every evaluation stores the model version, the inputs and the result. Changes go through maker-checker approval, and an RE-visible change log is kept in U18.
- `REQ-CF-7(3)` **[UDOFIN]** Each offer shows the lender name, the loan amount and tenor, the APR, the monthly repayment obligation and penal charges (if applicable), "in a way which enables the borrower to make a fair comparison", plus a link to each lender's KFS.
  - *Build:* U8 offer card schema with all fields mandatory. APR and KFS come from the RE (`EligibilityCheck`, `KFSIssued`) and are never computed or edited by Udofin.
- `REQ-CF-7(4)` **[UDOFIN]** Content is "unbiased, objective". It must not promote or push a lender's product, directly or indirectly, and must not use dark patterns (as defined in s.2(e) of the CCPA Dark Patterns Guidelines, 2023). Ranking is allowed only on "a publicly pre-disclosed metric".
  - *Build:*
    - U8 supports only ranking metrics published on Udofin's website, with the metric version shown on screen.
    - No "recommended", "best", sponsored badge or default pre-selection.
    - A U18 UI review checklist against the 13 CCPA dark patterns runs before every release [VERIFY: current CCPA dark-pattern list].
    - Commercial terms (fee rate) are never a ranking input.

### Creditworthiness, disclosures and recovery-agent notice (paras 8–9)

- `REQ-CF-8(1)` **[RE]** Before any loan, obtain the borrower's economic profile, at minimum **age, occupation and income**, and keep it for audit.
  - *Build:* U6 and U7 make age, occupation and income mandatory fields with source evidence, passed to the RE in `ApplicationSubmitted`.
- `REQ-CF-8(2)` **[RE]** No automatic increase in credit limit "unless an explicit request is received, evaluated and kept on record from the borrower".
  - *Build:* U12 offers limit increases only on a borrower-initiated, timestamped request event. There are no pre-ticked or auto-accept flows.
- `REQ-CF-9(1)` `REQ-CF-9(2)` **[RE]** The KFS and penal charges follow RBC (see 8A.6).
  - *Build:* U8 displays the RE-issued KFS unaltered, with its unique proposal number and validity period (at least 3 working days for tenor of 7 days or more; 1 working day for tenor under 7 days, RBC para 29(2)). Udofin captures the borrower's acknowledgement.
- `REQ-CF-9(3)` **[RE]** Digitally signed documents "on the letter head of the NBFC" automatically flow to the borrower's registered and verified email/SMS upon execution: KFS; summary of loan product; sanction letter; terms and conditions; account statements; privacy policies of the NBFC/LSP.
  - *Build:* U9 and U16 may deliver the RE's signed pack on the RE's behalf if the contract says so. Udofin never re-renders RE documents. Udofin supplies its current privacy-policy version to each RE through the U1 onboarding pack.
- `REQ-CF-9(4)` `REQ-CF-9(5)` **[RE]** The RE's website shows, at "a prominent single place", its LSPs, their DLAs and the activities they are engaged for. DLAs and LSPs link to that page.
  - *Build:* U23 shows a per-RE disclosure panel in every DLA, linking to the RE's page (the URL comes from `ProductCatalogPublished`). U1 holds the activity list each RE must publish.
- `REQ-CF-9(6)` **[RE→UDOFIN contract]** When a recovery agent is assigned or changed on a defaulted loan, its particulars are sent to the borrower by email/SMS **before** the agent contacts the borrower.
  - *Build:* U13 hard gate: no call, message or visit task can be created for an allocation until a delivered-notice record exists for that agent and loan. This applies whether the RE sends the notice or Udofin sends it on the RE's behalf (`CollectionAllocated`). RBC paras 95–97 (notice, authorisation letter, ID card) apply as well.

### Fund flows (para 10)

- `REQ-CF-10(1)` **[RE]** Disbursal always goes into the borrower's bank account. The only exceptions are:
  - a statutory or regulatory mandate;
  - co-lending flows between lenders;
  - a specific end use, paid directly to the end-beneficiary's bank account.
  - It never goes to a third-party or LSP account.
  - Salary advances may be repaid by the employer by salary deduction, directly from the employer's bank account, and "LSPs do not have any control over the flow of funds".
  - *Build:* U10 orchestrates status only. U2 product configuration rejects any beneficiary that is not the verified borrower account, except for an RE-flagged end-use product with a verified beneficiary.
- `REQ-CF-10(2)` `REQ-CF-10(3)` **[RE]** All servicing and repayment goes directly to the RE's bank account, with no pass-through or pool account of any third party, including the LSP. The flow of funds between borrower and RE is not controlled by a third party, directly or indirectly.
  - *Build:* U11 creates payment links, UPI intents and mandates only on the RE's merchant, collection or sponsor-bank accounts, with settlement to the RE. Udofin has no nodal, escrow or virtual account in the money path. A U21 configuration validator blocks any connector setup that names a Udofin account.
- `REQ-CF-10(4)` **[RE→UDOFIN contract]** LSP fees, charges and reimbursements are paid by the RE and "are not charged to or collected from the borrowers separately by LSP".
  - *Build:* U17 invoices the RE only. U2 and U8 cannot create any borrower-facing Udofin fee, including convenience, platform or report fees.
- `REQ-CF-10(5)` **[RE→UDOFIN contract]** For delinquent loans only, the RE may recover in cash through a physical interface. Cash recovered must be "duly reflected in full in the borrower's account on the same day", and the LSP's fees for that recovery are paid by the RE, never deducted from the proceeds.
  - *Build:*
    - U22 and U13 enable cash receipts only on loans with overdue status in the U12 mirror.
    - Each receipt is issued for the full amount and sent to the RE (`ReceiptIssued`) the same day.
    - Udofin's fee is never netted.
    - U17 runs a cash-in-transit ledger and daily reconciliation, and escalates any receipt not acknowledged by the RE's LMS by end of day.

### Cooling-off (para 11)

- `REQ-CF-11(1)` **[RE]** The borrower gets "an explicit option to exit a digital loan by paying the principal and the proportionate APR without any penalty" during a cooling-off period. The RE fixes the period in its credit policy, and it is **not less than one day**. After that, prepayment follows RBC.
- `REQ-CF-11(2)` **[RE]** A "reasonable one-time processing fee" may be retained on exit only if disclosed upfront in the KFS.
  - *Build:*
    - U8 shows the RE's period and exit terms before acceptance.
    - U12 shows a persistent "Exit this loan" action, with the RE-computed exit amount, for the whole period.
    - The exit request is sent as `CoolingOffExitRequested`, and payment goes to the RE account (U11).
    - The period starts on `LoanDisbursed` per the Finbyx contract. Para 11 does not state the start event [VERIFY: confirm the start trigger with each RE's credit policy].

### Grievance redressal (para 12)

- `REQ-CF-12(1)` **[UDOFIN]** Udofin, as an LSP with a borrower interface, designates a nodal grievance redressal officer for digital lending complaints. The RE designates its own.
- `REQ-CF-12(2)` **[UDOFIN]** The nodal officers' contact details are prominently displayed on the RE's website, Udofin's website and the DLA, and in the KFS.
  - *Build:* U15 holds the Udofin nodal officer record. U23 shows it on every DLA screen reachable from the help menu. U1 sends it to each RE for its website and KFS template [decision: carry it in the U1 onboarding pack, or add it to the Part 5 catalogue through a versioned contract change].
- `REQ-CF-12(3)` **[UDOFIN]** Complaints can be lodged on the DLA and the website. "Responsibility of grievance redressal shall continue to remain with the NBFC."
  - *Build:* U15 intake in the app and on the web, routed to the RE's GRO through `GrievanceRaised`. Udofin never closes a complaint that concerns the RE's decision or conduct.
- `REQ-CF-12(4)` **[RE]** The borrower may go to the CMS (https://cms.rbi.org.in) or the CRPC, RBI, Sector 17, Chandigarh 160017 if:
  - the RE rejects the complaint wholly or partly;
  - the borrower is not satisfied with the reply; or
  - there is no reply within **30 days of receipt by the NBFC**.
  - This must be conveyed to the borrower.
  - *Build:* U15 forwards complaints to the RE immediately (recommended: within one hour, with the delivery acknowledgement stored), because the RE's 30-day clock depends on it. Escalation text and links are shown on day 31 and on any rejection. Equator referral is an addition, never a substitute.

### Data collection, storage and privacy (paras 13–16)

- `REQ-CF-13(1)` **[UDOFIN]** Data collection by the DLA is "need-based and with prior and explicit consent of the borrower having audit trail". DLAs must "desist from accessing mobile phone resources like file and media, contact list, call logs, telephony functions, etc." "A one-time access can be taken for camera, microphone, location or any other facility necessary for the purpose of on-boarding / KYC requirements only, with the explicit consent of the borrower."
  - *Build:*
    - The U3 Android manifest and iOS plist allow-list is enforced in CI. The build fails if any of these is declared: `READ_CONTACTS`, `READ_CALL_LOG`, `READ_PHONE_STATE`, `READ_PHONE_NUMBERS`, `CALL_PHONE`, `READ_SMS`, `RECEIVE_SMS`, `SEND_SMS`, `READ_EXTERNAL_STORAGE`, `READ_MEDIA_*`, `MANAGE_EXTERNAL_STORAGE`, `ACCESS_FINE_LOCATION`, `ACCESS_BACKGROUND_LOCATION` or `QUERY_ALL_PACKAGES`.
    - Camera, microphone and foreground location are requested only inside U5 onboarding/KYC steps. Each request has a U4 consent record and is released after the step.
    - KYC documents are captured with the in-app camera, not from the gallery. Later uploads use the system document or photo picker, which is user-selected and needs no storage permission [interpretation].
    - OTP autofill uses the SMS Retriever or SMS User Consent API, which need no SMS permission [VERIFY: current Android API behaviour].
    - The web app requests browser camera and location only in the same steps.
    - Location is never collected for collections or marketing.
- `REQ-CF-13(2)` **[UDOFIN]** The borrower can: give or deny consent for specific data; restrict disclosure to third parties; choose data retention; revoke consent already granted.
  - "make the NBFC / LSP delete / forget the data".
  - *Build:* U4 consent centre with granular toggles, revocation and erasure requests. Erasure runs across Udofin stores and sends a deletion request to each RE. Statutory retention held by the RE (for example KYC records, KYC para 47) is explained, not overridden.
- `REQ-CF-13(3)` **[UDOFIN]** The purpose of each consent is disclosed "at each stage of interface". `REQ-CF-13(4)` **[UDOFIN]** Explicit consent is taken before personal information is shared with any third party, unless the sharing is statutory or regulatory.
  - *Build:* U4 purpose-bound consent artefacts (purpose, data items, recipient RE or vendor, expiry). U21 refuses any outbound call that has no matching live consent ID.
- `REQ-CF-14(1)` **[RE→UDOFIN contract]** The LSP does not store personal information "except some basic minimal data (viz., name, address, contact details of the customer, etc.)" needed for its operations within the scope of the NBFC–LSP agreement. Data privacy and security remain the RE's responsibility.
  - *Build:*
    - U4 data-classification register, with a per-RE "LSP minimal data set" defined in the U1 agreement.
    - KYC artefacts, bureau reports, AA data and bank statements are transient. They are delivered to the RE and then purged on the RE's acknowledgement, with a retention timer per contract.
    - The U12 loan mirror holds only what servicing needs.
    - [decision: the per-RE retention schedule, signed off by each RE.]
- `REQ-CF-14(2)` **[UDOFIN]** A storage policy (data types, retention period, use restrictions, destruction protocol, breach handling) is "disclosed by the NBFC and the LSP … prominently on their website and DLA at all times".
  - *Build:* U23 publishes the policy with a version and hash. U4 implements the destruction protocol and records evidence of each destruction.
- `REQ-CF-14(3)` **[UDOFIN]** "No biometric data is stored / collected by the NBFC and LSP, unless allowed under extant statutory guidelines."
  - *Build:*
    - No fingerprint or iris capture.
    - Face liveness and face match are run by the RE's KYC provider on the RE's account.
    - Udofin keeps no face templates or embeddings.
    - Live photographs required by KYC (KYC paras 24, 27) are held only as RE records [VERIFY: whether KYC photographs count as "biometric" under the Aadhaar Act s.2(g) definition, and the legal basis for any retention by Udofin].
- `REQ-CF-14(4)` **[UDOFIN]** All data is stored only on servers in India. If data is processed outside India, it is deleted there and "brought back to India within 24 hours of processing".
  - *Build:*
    - U18 sub-processor register with a processing-location field.
    - No borrower personal data goes to non-India AI, analytics, crash-reporting or push services. Push payloads carry no personal data.
    - U20 sends only redacted prompts to models hosted outside India, or uses India-hosted models.
    - Railway holds synthetic data only.
- `REQ-CF-15` **[UDOFIN]** Udofin publishes a comprehensive privacy policy on its website (para 15(1)). It discloses the third parties allowed to collect personal information through the DLA (para 15(2)).
  - *Build:* U18 SDK and third-party inventory generated from the dependency manifest, which feeds the privacy-policy annex. CI fails when a new SDK is not in the inventory.
- `REQ-CF-16` **[RE→UDOFIN contract]** Udofin complies with RBI and other cybersecurity standards for digital lending.
  - *Build:* see 8A.8 CYB and 8A.11 DPS (voluntary baseline).

### CIC reporting and the CIMS DLA register (paras 17–18)

- `REQ-CF-17` **[RE]** All lending through the RE's or LSPs' DLAs is reported to CICs "irrespective of its nature / tenor" (para 17(1)). This includes structured short-term or deferred-payment credit over merchant platforms (para 17(2)).
  - *Build:* Udofin never reports to CICs. U21 delivers complete, timely repayment events to the RE so that none goes unreported (CIR para 10(3)).
- `REQ-CF-18(1)` `REQ-CF-18(2)` **[RE]** The RE reports every DLA, own or LSP's, on CIMS in the Annex-I format and updates the list when a DLA is added or ceases.
  - Annex-I columns, verified on the PDF image:
    - S. No.;
    - Name of the DLA;
    - Name of the owner (self-owned, or the LSP's name);
    - Available on (website or app store name);
    - Link to DLA;
    - Name, email ID, telephone number and mobile number of the Grievance Redressal Officer;
    - Website of RE.
  - The footnotes say that each DLA is a separate line item and that each app store needs its own entry. A website DLA gives the website link; an app gives its store link.
  - *Build:* U18 DLA register (`dla_register`; lines created at U1 onboarding) with one row per DLA per platform (Google Play, App Store, web/PWA, and any white-label variant). Each row tracks its activation and cessation dates. An export per RE in Annex-I column order is regenerated, and the RE notified, on every launch, rename or withdrawal [VERIFY: whether the GRO columns take the RE's GRO or the LSP's nodal officer; para 18(4)(ii) suggests the LSP's for LSP-owned DLAs].
- `REQ-CF-18(3)` `REQ-CF-18(4)` **[RE]** The CCO or a Board-designated official certifies that:
  - each DLA links to the RE's website;
  - an LSP-owned DLA has a nodal grievance officer displayed on it;
  - data collection and storage comply with paras 13–14;
  - the DLA particulars appear on the RE's website under para 9(4).
  - *Build:* U18 produces a per-RE certification evidence pack covering all four points, with screenshots, manifest scans and policy versions.
- `REQ-CF-18(6)` **[UDOFIN]** Inclusion on CIMS must not be presented as RBI "registration, authorization, or endorsement" in any marketing material.
  - *Build:* a U16 content linter blocks phrases such as "RBI registered", "RBI approved" and "RBI authorised" in Udofin-originated copy.

### DLG — Udofin as provider (paras 19–30)

DLG is optional and per RE. **DLG creates no collection rights or duties.** Collections need a separate recovery-agent appointment (para 6(5); see U13).

- `REQ-CF-19` **[UDOFIN]** Only an LSP, or another lender engaged as an LSP, may give DLG. The LSP must be incorporated as a company under the Companies Act, 2013.
  - *Build:* U14 blocks DLG set-up until U1 holds Udofin's CIN and incorporation evidence [VERIFY: Udofin's incorporating statute].
- `REQ-CF-20(1)` **[RE]** Before any arrangement, the RE's policy sets: eligibility criteria for DLG providers; the nature and extent of cover; monitoring and review; fees payable to or received by the DLG provider.
- `REQ-CF-20(2)` **[RE]** DLG is no substitute for credit appraisal.
  - *Build:* U7 never passes DLG headroom to an RE's eligibility engine, and never routes by "DLG-covered" status [interpretation].
- `REQ-CF-20(3)` **[UDOFIN]** On **every entry or renewal**, Udofin gives a declaration, **certified by its statutory auditor**, covering: the aggregate DLG amount outstanding; the number of lenders; the respective number of portfolios against which DLG has been provided; past default rates on similar portfolios.
  - *Build:* U14 and U17 generate the declaration data from the DLG ledger. U18 tracks auditor sign-off and blocks renewal without it.
- `REQ-CF-21(1)` **[RE]** No DLG on loans covered by credit-guarantee schemes run by trust funds.
  - *Build:* U14 rejects any loan carrying a CGTMSE, CRGFTLIH or NCGTC flag from the RE.
- `REQ-CF-22` **[RE→UDOFIN contract]** An explicit, legally enforceable contract states: the extent of cover; the form of cover; the invocation timeline; the para 28 disclosure obligations.
- `REQ-CF-23` **[UDOFIN]** Only three forms of DLG are allowed: cash deposited with the NBFC; an FD with a Scheduled Commercial Bank with lien marked in favour of the NBFC; a bank guarantee in favour of the NBFC.
  - *Build:* U14 instrument register (form, bank, lien or BG reference, expiry) and U17 accounting for deposits, liens and contingent liabilities [VERIFY: Ind AS treatment with Udofin's auditors].
- `REQ-CF-24` **[RE→UDOFIN contract]** Total DLG cover on a portfolio "shall not exceed five per cent of the total amount disbursed out of that loan portfolio at any given time". For implicit guarantees, performance risk is capped at the equivalent of 5%.
  - The **DLG set** is identifiable sanctioned loans and is "fixed … not meant to be dynamic". Loans leave the set only by repayment or write-off.
  - Cover activates pro rata as loans are disbursed (para 24(3), Illustrations 1–2).
  - *Build:*
    - U14 keeps a set-level ledger: sanctioned set, cumulative disbursed, cap (5% of disbursed), invoked to date, and available headroom.
    - Adding loans to a closed set is blocked.
    - **Any fee clawback, reversal or first-loss term in the commercial contract is modelled as implicit DLG** and counted within the cap.
    - The original prompt's "5% FLDG" is a ceiling, not a fixed rate.
- `REQ-CF-25(2)` **[RE]** Invoked DLG is not set off against individual loans, so the borrower's liability is unaffected.
  - *Build:* U12 and U25 never show a loan as reduced or settled because DLG was invoked.
- `REQ-CF-25(3)` **[RE→UDOFIN contract]** Recoveries on loans where DLG was invoked may be shared with the provider as the contract says.
  - *Build:* a U14 recovery-sharing ledger.
- `REQ-CF-25(4)` **[RE→UDOFIN contract]** Invoked DLG is "not … reinstated, including through loan recovery".
  - *Build:* the U14 ledger has no reinstatement transaction type, and headroom never increases after invocation.
- `REQ-CF-26(2)` **[RE]** Capital deduction applies only where the DLG provider is an NBFC. Not applicable to Udofin.
- `REQ-CF-27(1)` **[RE]** The RE invokes DLG "within a maximum overdue period of 120 days, unless the loan dues are made good by the borrower before that". `REQ-CF-27(2)` **[RE→UDOFIN contract]** The DLG agreement runs for no less than the longest loan tenor in the portfolio.
  - *Build:* U14 consumes `DLGInvocationRaised`, validates the DPD (120 or less) against the U12 mirror, and records `DLGInvocationSettled`. Agreement end dates are checked against the maximum tenor in the set.
- `REQ-CF-28` **[UDOFIN]** Udofin publishes on its website "the total number of portfolios and the respective amount of each portfolio on which DLG has been offered". Lender names are optional. The disclosure is monthly, and "no later than seven (7) working days following the conclusion of that month".
  - *Build:* U14 auto-generates the disclosure and U23 publishes it. U18 holds the working-day calendar, the deadline alert and the published-version archive. `DLGDisclosurePublished` (contract event adopted in v1.1, Part 5.2) is sent to each RE as evidence.
- `REQ-CF-29` `REQ-CF-30(2)` **[RE]** Guarantees under CGTMSE, CRGFTLIH or NCGTC, and BIS, IMF or MDB guarantees, are not DLG. Compliant DLG is neither synthetic securitisation nor loan participation.

### Microfinance loans sourced through Udofin (Chapter V, paras 51–62)

- `REQ-CF-51` **[RE]** A microfinance loan is any **collateral-free** loan (no lien on a deposit account, no hypothecation) to a household with **annual household income up to ₹3,00,000**. Household means "husband, wife and their unmarried children". This applies "irrespective of end use and mode of application / processing / disbursal (either through physical or digital channels)".
  - *Build:* U6 captures household composition and household income for every collateral-free application. U7 sets an `is_microfinance` flag (unsecured, and annual household income of ₹3,00,000 or less) that travels with the application. Products 1–2 and every other unsecured product are in scope.
- `REQ-CF-52` **[RE]** The RE assesses household income under a Board-approved policy. The indicative parameters are:
  - the household profile (earning and non-earning members, accommodation, amenities, assets);
  - income by member and by source, including remittance, rent, pension, government transfers and scholarship, without double counting;
  - stability assessed over a minimum of one year;
  - household expenses (regular monthly and irregular over the last year);
  - corroboration, including from bank statements.
  - *Build:* U6 household-income questionnaire following para 52(1). Each RE configures the required fields in U2. Evidence links (AA statements, declarations) go to the RE.
- `REQ-CF-54` **[RE]** Household income is mandatorily reported to CICs. Reasons for any divergence from previously reported income are obtained from the borrower.
  - *Build:* U6 captures monthly family income for every microfinance application (UCRF MFI field 49, CIR Annex I) and a divergence-reason field.
- `REQ-CF-55` `REQ-CF-56` `REQ-CF-57` **[RE]** Monthly repayment outflows on **all** household loans (secured and unsecured, existing and proposed, principal plus interest) must not exceed **50% of monthly household income**. Future income from the financed activity is excluded. No new loan is given while the household is above 50%.
  - *Build:* U6 computes an indicative obligation ratio from RE-pulled bureau data and declarations, and shows it to the RE. U7 suppresses an RE's offer when the RE's engine reports a breach. The RE's decision is final [VERIFY: how each RE converts bullet or payday repayments into a monthly obligation for this test].
- `REQ-CF-58` **[RE]** The RE uses CIC data plus declarations, bank statements and local enquiries.
- `REQ-CF-59` **[RE]** The RE's policy offers flexible repayment periodicity on microfinance loans.
  - *Build:* U8 shows the periodicity options the RE allows.
- `REQ-CF-60` `REQ-CF-61` **[RE]** A Board pricing policy sets the interest-rate model, its components, spread ranges and a ceiling on interest and all charges. Pricing must not be usurious.
  - *Build:* U2 stores the RE's microfinance ceiling and U8 refuses to display an offer above it.
- `REQ-CF-62` **[RE]** Conduct follows RBC (see 8A.5 and 8A.6). Para 62(2) cites a non-existent "Management of Third-Party Dependencies" Directions; the evident intent is OUT (drafting slip; see Appendix F).

### Other CF chapters touching Udofin products

- `REQ-CF-105` **[RE]** No lending against the RE's own shares.
  - *Build:* the U2 LAS eligible-securities list excludes each RE's own ISINs.
- `REQ-CF-106` **[RE]** For loans against listed shares by an NBFC with assets of ₹100 crore and above:
  - LTV of 50% at all times, with any shortfall made good within 7 working days;
  - only Group 1 securities where the loan is for capital-market investment and exceeds ₹5 lakh.
  - *Build:* U12 and U16 margin-call notices using RE-supplied LTV status (Phase 18); full journey, rails and events in Part 6.5.
- `REQ-CF-4(1)(xiv)` **[RE]** Housing finance is defined in para 4(1)(xiv). LAP and furnishing loans are not housing finance.
  - *Build:* U2 product classification for products 4 and 6.
- Gold (Ch IV) is proposed Product 11 (Phase 18b) in a leads, branch-appointment and servicing role only (Part 6.4.8); project finance (Ch VI) and PCE (Ch VII) are outside Udofin's product set. Ch IV para 47 repeats the para 10(1)–(2) money-flow rule.

---

## 8A.2 CIR — Credit Information Reporting Directions (349, as amended by 117)

**Source:** RBI/DOR/2025-26/349; DOR.FIN.REC.No.268/20.16.056/2025-26; 28 Nov 2025, issued under s.11 of CICRA. Amendment RBI/DOR/2025-26/117 (effective 1 Jul 2026) is not in the supplied copy [VERIFY: obtain 117 and confirm paras 10(2), 12(10), 15 and Annex VI as summarised in Finbyx 8A.2].

### Applicability to Udofin

- **Not directly.** The Directions apply to Credit Institutions (CIs): the listed NBFCs, including HFCs and P2P (para 3(1)).
  - Udofin is not a CI.
  - Udofin cannot be a CIC member in its own right: para 6 obliges each CI to join all four CICs, and Udofin is not a CI [VERIFY: CICRA s.15 and the CIC Regulations on who else a CIC may admit as a member].
  - Udofin is not a "Specified User" (para 4(3), which refers to CICRA s.2(l) and the CIC Regulations reg 3) [VERIFY: CICRA s.2(l), CIC Regulations reg 3 and CIC Rules on who may obtain a credit information report; not in the supplied texts].
- **Through the RE's contract.** Udofin captures data, consents and complaints that the RE needs to meet its own CIR duties.

### Who may pull bureau data: the correct position

- **Who pulls.** Bureau pulls for a lending decision are made by the RE as CI, under its own CIC membership (para 6). The RE's credit policy must "include … suitable provisions for obtaining CIRs from one or more CICs" (para 20).
- **What Udofin may do.** Udofin may act as the RE's technology channel, calling the CIC with the RE's member credentials held in a per-RE credential vault, or the RE may pull in its own LOS. Either way the enquiry is the RE's and is logged as the RE's.
- **What changes in the original design.** "Udofin soft-pulls CIBIL via Surepass" must be restructured. A pull made by Udofin in its own name, or through an aggregator that is not the RE's contracted channel, has no basis in the supplied texts [VERIFY: CICRA s.2(l) and the CIC Regulations; whether the CICs permit a technology service provider of a member CI; whether any "borrower's own report" consent flow may be used for pre-qualification].
- **Soft and hard enquiries.** The CIR Directions do not define them, and their treatment is set by each CIC's product rules [VERIFY]. Udofin treats every enquiry as an RE enquiry and shows the borrower which lender will enquire before consent.

### Requirements

- `REQ-CIR-6` **[RE]** The RE is a member of all four CICs.
  - *Build:* U6 bureau adapter runs per RE, with RE credentials in the U21 vault. There is no Udofin-owned bureau account, and every enquiry record names the RE.
- `REQ-CIR-11` **[RE]** CICRA gives statutory backing to reporting, so no consent clause is needed **for reporting**. This says nothing about enquiry.
  - *Build:* U4 still takes explicit, lender-specific consent before any enquiry (CF para 13(1) and 13(4)).
- `REQ-CIR-20` **[RE]** CIRs are obtained from one or more CICs under the RE's policy.
  - *Build:* U2 stores each RE's CIC preference and fallback order. U6 never "shops" one borrower's enquiry across REs that did not request it.
- `REQ-CIR-10(3)` **[RE]** No repayment, including the last instalment, may go unreported.
  - *Build:* U11 sends every payment, failure and reversal to the RE through U21, with the reconciliation in Part 5 (`DailyReconciliationFile`).
- `REQ-CIR-12(4)` **[RE]** "Settled" is used only where principal or interest is waived because the borrower cannot pay. Wrong debits and contested charges are reported as "disputed".
  - *Build:* Part 7A UR1 (settlement) and UR2 (ADR) tell the borrower, before acceptance, that a settlement is reported to CICs as "settled".
- `REQ-CIR-12(10)` **[RE]** The CKYC number is reported where available or once issued (inserted by 117, from 1 Jul 2026) [VERIFY: 117 text].
  - *Build:* U5 passes the KYC Identifier to the RE when it is obtained.
- `REQ-CIR-34(1)` **[RE]** The RE sends SMS/email alerts **while submitting** default or DPD information to CICs, wherever contact details are available.
  - *Build:* U16 may send these on the RE's behalf, under the RE's sender ID and template, if the contract says so. They are worded as reporting alerts, not as threats.
- `REQ-CIR-35(1)` `REQ-CIR-35(2)` **[RE]** If a complaint is unresolved after 30 calendar days, ₹100 per calendar day is paid. The CI has 21 days to send corrected data and the CIC the rest.
- `REQ-CIR-35(8)` **[RE→UDOFIN contract]** Complaint forms capture contact details, email ID and bank account details or UPI ID for paying compensation.
  - *Build:* U15 credit-information complaint type with these mandatory fields, forwarded to the RE immediately so that its 21-day clock is not eroded.
- `REQ-CIR-38(3)` **[RE]** Credit-information grievances are integrated with the general grievance system. Para 38 lists best practices the CI takes into account in its Board-approved policies; 38(3) and 38(5) are best practice, not hard rules [interpretation].
  - *Build:* U15 category "credit report" routed to the RE's CIC nodal officer (para 34(2)).
- `REQ-CIR-38(5)` **[RE]** "First time borrowers' loan applications should not be rejected just because they have no credit history."
  - *Build:* U7 pre-qualification never filters out applicants with no bureau record (new to credit). They are routed to every RE whose rules accept them.

---

## 8A.3 KYC — Know Your Customer Directions (361)

**Source:** RBI/DOR/2025-26/361; DOR.AML.REC.No.280/14.01.003/2025-26; 28 Nov 2025, updated as on 29 Dec 2025.

### Applicability to Udofin

- **Not directly.** The Directions apply to NBFCs with a customer interface (para 3) as reporting entities under the PML Act. Udofin is not an RE [VERIFY: whether Udofin's activities make it a reporting entity under PML Act s.2(1)(wa)].
- **Through the RE's contract.** Udofin runs the onboarding technology. The RE keeps the KYC decision, the risk categorisation, the CKYCR upload, sanctions screening and FIU-IND reporting.
- **Two consequences fix the design:**
  - The RE "does not outsource the decision-making functions of determining compliance with KYC norms" (para 13). Udofin's results are evidence only.
  - The RE may rely on a third party's CDD only where that third party is regulated, supervised or monitored and has PML-compliant CDD measures (para 22(3)). Udofin does not meet this condition. It therefore acts as the RE's agent and technology, not as a third party whose CDD the RE relies on.

### Division of work

| Step | Udofin may (technology or agent) | RE must |
|---|---|---|
| Identity capture | Run OTP, DigiLocker, PAN and CKYC-consent screens; capture documents and photos | Set the mandatory fields (para 17(4)) and accept or reject them |
| Aadhaar e-KYC (number-based) | Host the UI only, through the RE's licensed channel | Be notified under PML Act s.11A first proviso and authenticate through UIDAI (para 23(1)(ii), proviso (i)) |
| Offline Aadhaar, e-documents | Fetch with consent and pass on with signature-check evidence | Verify and decide (para 23 provisos (ii)–(iii)) |
| CKYCR | Capture the KYC Identifier and explicit download consent | Download, rely on and upload records under its CERSAI access (paras 23(4), 63) |
| V-CIP | Provide the software, if the RE's conditions are met | Have its own trained official run each session; host or own the data (para 27) |
| KYC decision, risk category, sanctions, STR | Show status only | Decide, categorise, screen and report (paras 13, 20, 54–57, 49–53) |

### Requirements

- `REQ-KYC-13` **[RE]** KYC decision-making is never outsourced.
  - *Build:* U5 sends `ApplicationSubmitted` with evidence and vendor results. The "KYC complete" status is set only by an RE user in the lender portal, or by the RE's own system through U21, with the actor recorded. Udofin auto-rules may flag but never pass a case [VERIFY: whether an RE-approved rule executed on Udofin infrastructure is acceptable to each RE's compliance function].
- `REQ-KYC-17(5)` **[UDOFIN]** Information beyond the RE's KYC policy is collected only "with the explicit consent of the customer".
  - *Build:* U4 marks every optional field with a consent flag.
- `REQ-KYC-17(6)` `REQ-KYC-66` **[RE]** CDD is done at UCIC level, and every individual customer gets a UCIC.
  - *Build:* U3 maps one Udofin borrower ID to a separate UCIC in each RE. One RE's KYC status is never presented as another RE's.
- `REQ-KYC-17(10)` `REQ-KYC-17(11)` `REQ-KYC-17(12)` **[RE→UDOFIN contract]** PAN is verified with the issuing authority's facility, the digital signature on e-documents is verified, and GSTIN is verified where available.
  - *Build:* U5 adapters return raw verification evidence (request ID, timestamp, response hash) to the RE.
- `REQ-KYC-18` **[RE]** Onboarding is not rejected "without application of mind", and the officer records the reason.
  - *Build:* U5 cannot auto-reject KYC. Mismatches go to the RE's queue.
- `REQ-KYC-20(4)` **[RE]** The risk category and its reasons are never revealed to the customer.
  - *Build:* any risk category the RE shares is stored in a field hidden from all borrower channels, U20 AI support and U15 replies.
- `REQ-KYC-23` **[RE]** CDD for individuals is one of the following, **plus PAN or Form 60**:
  - the Aadhaar number, only for an Aadhaar s.7 benefit or when volunteered to an RE notified under PML Act s.11A, with UIDAI e-KYC authentication;
  - proof of possession of Aadhaar with offline verification;
  - an OVD e-document, with digital-signature verification and "a live photo as specified under paragraph 24" (proviso (iii)); or a physical OVD, or proof of possession of Aadhaar where offline verification cannot be done, verified through digital KYC under para 24 (proviso (iv));
  - the KYC Identifier, with explicit consent to download from CKYCR.
  - Further rules:
    - Aadhaar numbers are redacted where authentication is not required (Expl 1).
    - An NBFC official may perform biometric e-KYC authentication, including Aadhaar Face Authentication (Expl 2); this is not a borrower self-service route, and Udofin stores no biometric data (CF para 14(3)).
    - "Aadhaar number is not mandatory" (Expl 4).
  - *Build:*
    - U5 offers non-Aadhaar routes (DigiLocker e-documents, CKYC, V-CIP) on equal footing.
    - Aadhaar numbers are masked to the last 4 digits in every stored image and field.
    - Aadhaar number-based OTP e-KYC is offered only for REs flagged in U1 as notified under s.11A, through the RE's AUA/KUA channel [VERIFY: each RE's notification status and the UIDAI AUA/KUA or sub-AUA arrangement through any vendor such as Surepass; Aadhaar (Data Vault) obligations].
    - [VERIFY: whether a borrower-captured liveness selfie meets "live photo as specified under paragraph 24" for the e-document route, since para 24 describes officer capture.]
- `REQ-KYC-24` **[RE]** Digital KYC (assisted) runs only on "the NBFC's authenticated application", operated by the RE's authorised officer, who logs in with a login-id and password or a Live/Time OTP. The process requires:
  - a live photo of the customer against a white background, with no other person in frame;
  - a readable watermark showing the CAF number, GPS coordinates, the officer's name and RE-assigned employee code, the date (DD:MM:YYYY) and the time (HH:MM:SS);
  - an OVD photo taken from above with no tilt;
  - a customer OTP whose text reads exactly "Please verify the details filled in form before sharing OTP", never sent to the officer's own registered mobile;
  - the officer's OTP declaration with the officer's live photo;
  - a reference ID given to the customer;
  - the officer's digital signature on the CAF, then the customer's signature or thumb impression, scanned and uploaded;
  - the application captures only a live photograph and does not capture any printed or video-graphed photograph (para 24(5)).
  - *Build:* U22 white-labelled as each RE's application, with RE-assigned officer codes [VERIFY: whether Udofin field staff may be designated as the RE's "authorised officer"; otherwise U22 digital KYC is limited to RE staff].
- `REQ-KYC-25` **[RE]** Accounts opened by Aadhaar OTP e-KYC in non-face-to-face mode are subject to these conditions: specific consent to OTP authentication; alerts and OTPs only to the **Aadhaar-registered mobile**; **term loans only, with an aggregate of no more than ₹60,000 sanctioned in a year**; no operation **beyond one year** without full CDD under para 23 or V-CIP, failing which "no further debits"; a declaration that no other OTP e-KYC account exists with any RE; a CKYCR flag on the upload; violation alerts.
  - *Build:*
    - U5 tags the KYC level.
    - U7 caps offers for OTP-e-KYC customers at the RE's remaining ₹60,000 annual headroom and allows term loans only.
    - U16 sends reminders to upgrade (V-CIP or full CDD) from month 9.
    - U12 withholds drawdown and top-up requests in Udofin channels after 12 months unless the RE confirms full CDD; the debit bar itself is the RE's (para 25(7)).
    - The U3 alert channel is pinned to the Aadhaar-linked mobile for these accounts.
- `REQ-KYC-26` `REQ-KYC-27` **[RE]** V-CIP is run only by "officials of the NBFC specially trained for this purpose". Infrastructure and data rules:
  - Infrastructure is on the RE's premises, and the connection originates "from its own secured network domain".
  - On cloud, data ownership "rests with the NBFC only". All data and recordings move "immediately" to the RE's exclusively owned or leased servers, and the "third-party technology provider assisting the V-CIP shall retain no data".
  - End-to-end encryption.
  - Sessions from IP addresses outside India, or spoofed ones, are blocked.
  - Video carries a geo-tag and a timestamp.
  - Liveness and face match are used (gestures not mandatory).
  - VAPT and a security audit by CERT-In-empanelled auditors before go-live and periodically.
  - Session rules:
    - a dropped call means a fresh session;
    - the question sequence varies;
    - the session is rejected if the customer is being prompted;
    - Aadhaar XML/QR is no more than **3 working days** old, and the video is done within 3 working days of obtaining the ID data;
    - a PAN image is captured unless e-PAN is given;
    - printed e-documents are invalid;
    - the account is operational only after concurrent audit;
    - records are kept in India, with an activity log of the official's credentials.
  - Customer consent is recorded "in an auditable and alteration-proof manner" (para 27(1)(ii)). The V-CIP application and its APIs pass functional, performance and maintenance testing before live use, and periodically, with critical gaps closed first (para 27(1)(ix)). Any detected forged-identity case is reported by the RE as a cyber event (para 27(1)(vii)).
  - *Build:* U5 V-CIP is delivered as the RE's application. Recordings are streamed to RE-designated storage, with no Udofin copy and evidence of deletion. Geo-IP blocking and the 3-working-day validators run in U24 [decision: buy a V-CIP product contracted by the RE rather than build].
- `REQ-KYC-44` **[RE]** Non-face-to-face onboarding by CKYCR, DigiLocker or e-documents (outside para 25) requires: V-CIP offered **first** where the RE has it; no alternate mobile linked after CDD, with transactions only from the onboarding mobile; positive confirmation of the current address before the account operates; PAN verified; the first transaction to be a credit from the customer's own KYC-compliant bank account; high-risk categorisation until F2F or V-CIP verification.
  - *Build:* U5 journey ordering puts V-CIP first. U3 locks the registered mobile. U10 shows the RE's address-confirmation status as a pending step before the RE disburses [VERIFY: how each RE applies para 44(5) to a loan account, whose first transaction is a disbursement].
- `REQ-KYC-47` **[RE]** Transaction records are kept for at least 5 years from the transaction. Identification records are kept for at least 5 years after the relationship ends.
  - *Build:* the RE holds these records. U4 retention defers to the RE's instruction and to CF para 14(1).
- `REQ-KYC-54` `REQ-KYC-55` `REQ-KYC-56` `REQ-KYC-57` **[RE]** Sanctions screening against the UNSC, UAPA and DPRK lists, with daily verification (paras 54(2), 56), and against the WMD list at onboarding and periodically (para 55(3)).
  - *Build:* Udofin may run a pre-screen as a fraud signal (U24), but the binding screen and any freeze or report are the RE's.
- `REQ-KYC-61` **[RE→UDOFIN contract]** Account-opening information is not used "for the purpose of cross-selling, or for any other purpose without the express permission of the customer".
  - *Build:* U16 marketing audiences exclude KYC-derived attributes unless a separate express-permission consent exists in U4.
- `REQ-KYC-63` **[RE]** CKYCR rules:
  - upload within **10 days** of the relationship starting (para 63(1));
  - send updates within **7 days** (para 63(7));
  - communicate the KYC Identifier to the customer (para 63(6));
  - seek the Identifier first and do not ask for documents again except on the para 63(9) grounds;
  - per the 29 Dec 2025 Explanation, the RE that last uploaded the record is responsible for identity and address verification.
  - *Build:* U5 asks for the KYC Identifier first and stores download consent. U25 shows the Identifier when the RE returns it.
  - Paras 23 proviso (v) and 27(2)(vi)(c) cite "paragraph 62" for CKYCR retrieval, but CKYCR is para 63 (drafting slip; see Appendix F).
- `REQ-KYC-68` **[RE]** An ML/TF risk assessment is done before launching new products, delivery channels or technologies.
  - *Build:* U18 issues a "channel risk pack" to each RE before every new DLA, platform or KYC method goes live.
- `REQ-KYC-72` **[RE→UDOFIN contract]** Know-your-employee screening and KYC/AML training apply to staff deployed on KYC.
  - *Build:* U22 field-user onboarding records screening and training evidence for RE review.

---

## 8A.4 AA — Account Aggregator Directions (368)

**Source:** RBI/DoR/2025-26/368; DoR.FIN.REC.No.287/03-10-123/2025-26; 28 Nov 2025.

### Applicability to Udofin

- **Not directly.** The Directions regulate NBFC-AAs and set FIP/FIU duties.
- **Udofin cannot be an FIU.** A Financial Information User is "an entity registered with and regulated by any financial sector regulator" (para 8(12)), and Udofin is not.
- **Udofin cannot be an AA.** An AA needs a CoR, may do no other business (para 14(6)), and may not use third-party service providers for aggregation (para 14(8)).
- **Udofin's permitted role.** Udofin is a technology service provider to the RE as FIU. It embeds the AA consent journey in the DLA, and data flows to the RE under the RE's FIU identity [VERIFY: Sahamati/ReBIT technology-service-provider onboarding model; not in the supplied text].

### Requirements

- `REQ-AA-8(9)` **[RE]** Financial information covered: bank deposits and NBFC deposits; securities, MF, ETF and other market instruments; insurance and NPS; InvIT and REIT units.
  - GSTR-1 and GSTR-3B.
  - Loan accounts are not listed.
  - *Build:* U6 uses AA for bank-statement income and affordability, U2 and U6 for LAS holdings, and GST returns for self-employed borrowers where the RE asks for them. Existing loan obligations come from the RE's bureau pull, not AA.
- `REQ-AA-8(12)` `REQ-AA-17(4)` **[RE]** The RE is the FIU and the named recipient in the consent artefact.
  - *Build:* U21 AA connector configured per RE with the RE's FIU ID. There is no Udofin FIU registration.
- `REQ-AA-17` `REQ-AA-19` `REQ-AA-20` `REQ-AA-21` **[RE]** These are NBFC-AA obligations (the AA obtains and manages consent, para 16); the RE as FIU and Udofin as its technology provider rely on them and mirror them [interpretation]. The artefact carries: the customer's identity; the nature of information; the purpose; the recipients; the notification URL; creation and expiry dates; the AA's identity and signature.
  - The customer may revoke consent, including in part. The artefact can be logged, audited and verified.
  - *Build:* U4 mirrors the artefact ID, purpose, data range, fetch type and expiry, and the status notifications (active, paused, revoked, expired). On revocation or expiry, U4 stops fetches and purges data held by Udofin.
- `REQ-AA-27` **[RE]** The AA verifies the identity of the FIU and transfers the information only to the intended recipient named in the consent artefact (para 27).
  - *Build:* U21 receives AA data only at the RE's registered FIU endpoint and keys. Where Udofin hosts that FIU module, it runs as the RE's technology under the OUT contract, with RE-owned keys and no Udofin copy beyond CF para 14(1) [VERIFY: Sahamati/ReBIT technology-service-provider model].
- `REQ-AA-28` **[RE]** Information is not "used or disclosed by … the Financial Information User except as may be specified in the consent artefact".
  - *Build:* U4 tags the purpose on all AA-derived data. U16 and U20 cannot read AA data. AA data is delivered to the RE and not kept beyond CF para 14(1).
- `REQ-AA-14(11)` **[RE]** Where an AA statement and the FIP's books differ, the FIP's record prevails (an NBFC-AA duty that governs how the RE reads AA data). The disclaimer below is a Udofin recommendation, not a Udofin obligation.
  - *Build:* U6 and U25 show this disclaimer wherever AA-derived figures appear.
- `REQ-AA-29` **[RE]** An RE that joins as FIU must also join as FIP if it holds specified information. This is the RE's obligation and has no Udofin build.
- `REQ-AA-33` **[RE→UDOFIN contract]** The ReBIT technical specifications are adopted.
  - *Build:* U21 AA adapter conforms to the current ReBIT API version [VERIFY: version in force].
- **Credentials (interpretation).** Udofin never collects net-banking credentials or uses screen-scraping to fetch statements. This follows CF para 13(1) and the AA design principle in paras 14(9) and 30(2). Only AA or borrower-uploaded statements are allowed.
- **Correction.** The original prompt's "books of accounts" view of the borrower's finances cannot be built on AA data received by an RE for a lending purpose (para 28). U25 must use servicing data from the U12 mirror and borrower-entered data, or a separate consent route that does not exist in the supplied texts [VERIFY].

---

## 8A.5 MFI — Microfinance Institution Directions (371)

**Source:** RBI/DOR/2025-26/371; DOR.FIN.REC.290/03-10-038/2025-26; 28 Nov 2025 (original text; no "updated as on" date).

### Applicability to Udofin

- **Not directly.** The Directions apply to NBFC-MFIs (para 3).
- **Through the RE.** Two provisions shape Udofin's routing:
  - para 49 binds every NBFC that makes microfinance loans;
  - the NBFC-MFI definition depends on the RE's portfolio mix.
- The loan-level microfinance rules (household income, the 50% cap, pricing) sit in CF Ch V (8A.1). The conduct rules sit in RBC (8A.6).

### Requirements

- `REQ-MFI-8(2)` `REQ-MFI-8(3)` **[RE]** "Microfinance loan" has the CF meaning. An NBFC-MFI is a non-deposit-taking NBFC with at least 60% of total assets (net of intangibles) in microfinance loans on an ongoing basis.
  - *Build:* U1 records each RE's type (NBFC-MFI or other). U2 attaches MFI-specific product rules to that RE.
- `REQ-MFI-12` **[RE]** Qualifying assets are at least 60% on an ongoing basis. After four consecutive quarters below 60%, the NBFC-MFI approaches RBI with a remediation plan.
  - *Build:* none in Udofin beyond U19 sourcing MIS by microfinance flag.
- `REQ-MFI-49` **[RE]** Microfinance loans of all NBFCs follow CF, RBC and OUT. "An NBFC, which does not qualify as an NBFC-MFI shall extend microfinance loans, which in aggregate does not exceed 25 per cent of its total assets."
  - *Build:* U7 routes microfinance-flagged applications only to REs whose U2 configuration accepts microfinance loans. An RE can switch off microfinance intake when it nears its 25% limit, through `ProductCatalogPublished`.
- `REQ-MFI-46` **[RE]** Every NBFC-MFI is a member of at least one RBI-recognised SRO and follows its Code of Conduct.
  - *Build:* U1 stores the SRO, and U18 loads the SRO code as an obligation set where Udofin is the RE's agent [VERIFY: the current SRO code text].
- **RBC conduct rules on microfinance loans that Udofin executes as LSP or recovery agent** (verified in 362; full treatment in 8A.6):
  - `REQ-RBC-78` **[RE]** A loan card with:
    - borrower identification;
    - a simplified pricing factsheet;
    - all other terms;
    - acknowledgement of all repayments and the final discharge;
    - grievance details, including the nodal officer.
    - All entries are in a language the borrower understands (para 79).
    - *Build:* U9 and U25 render the RE-issued loan card.
  - `REQ-RBC-81` **[RE]** No prepayment charge. Delayed-payment charges apply to the overdue amount only.
    - *Build:* U8 blocks microfinance offers whose KFS shows a prepayment charge.
  - `REQ-RBC-90` **[RE→UDOFIN contract]** Recovery happens at a designated or central place agreed with the borrower. Field staff may recover at home or work only if the borrower fails to appear there "on two or more successive occasions".
    - *Build:* U13 and U22 visit rules.
  - `REQ-RBC-91` **[RE→UDOFIN contract]** No harsh methods. The list includes calling "before 9:00 a.m. and after 6:00 p.m.", persistent calling, harassing relatives or co-workers, and publishing names.
    - *Build:* the U13 contact-window engine uses 09:00–18:00 for microfinance-flagged loans, against 08:00–19:00 for other loans (RBC para 100).
- **No separate pricing cap.** The MFI Directions set no interest cap. Pricing stays under CF paras 60–61 and the RE's ceiling.

---

## 8A.6 RBC — Responsible Business Conduct Directions (362)

**Applicability to Udofin: through the RE's contract.** RBC binds NBFC-D, ICC, Factor, MFI, IFC, IDF-NBFC and HFC REs at all layers; NBFC-P2P only for paras 98–100 (paras 3–4). It reaches Udofin through CF para 6(5) (an LSP recovery agent must comply with RBC), OUT para 17 (the RE answers for its DSAs, DMAs and recovery agents) and the LSP agreement. Udofin is the borrower's interface for most conduct obligations, so it builds them as controls each RE configures and approves. Copy supplied: updated as on 1 Apr 2026. **Not in the supplied copy:** the Second Amendment (Chapter IIIA, sales and marketing) and the Third Amendment Directions, 2026 (RBI/2026-27/230, DOR.MCS.REC.No.199/01-01-039/2026-27, 6 Aug 2026, in force 1 Jan 2027), which delete paras 89–100 and insert Section J, paras 100A–100AB; the Third Amendment is confirmed from the RBI notification and secondary summaries and its key rules are in Part 7A.0.1 [VERIFY: official texts not supplied in docs/regulations/rbi/; confirm paragraph numbers before coding]. Build U13, U16 and Part 7A rules as effective-dated rule packs. **Bank REs:** the equivalent Commercial Bank conduct Directions apply instead [VERIFY: bank texts not supplied]; U1 holds the RE type and selects the rule pack.

**Board policies and review (paras 7–8):**

- **REQ-RBC-7** **[RE]** Board policies on FPC, grievance redressal (disputes heard at least at the next higher level), interest and charges, recovery agents, and the DSA/DMA/RA code of conduct (7(1)–(8)).
  - **[RE→UDOFIN contract]** Udofin receives each policy's version and applies it. *Build:* U2 stores policy references per RE product from `ProductCatalogPublished`; U23 links the RE's FPC (published on its website, para 21) on every product screen.
- **REQ-RBC-8** **[RE]** Periodic review of FPC compliance and the grievance machinery, with a consolidated Board report. *Build:* U19 "FPC conduct pack" per RE per period: complaints by category and TAT, communication-language exceptions, contact-policy breaches, KFS acknowledgement rates.

**Fair Practices Code (paras 10–21):**

- **REQ-RBC-10** **[RE→UDOFIN contract]** All communications to the borrower in the vernacular or a language the borrower understands. *Build:* U3 captures the preferred language at registration; U16 holds an RE-approved template per event per language; dispatch is blocked (and an exception raised) if no approved template exists in that language.
- **REQ-RBC-11** **[RE→UDOFIN contract]** The application form carries information enabling meaningful comparison with other lenders and lists the documents required. *Build:* U7 shows the product's key terms and the document checklist from U2 before submission; U8 provides the multi-lender comparison (CF para 7).
- **REQ-RBC-12** **[RE→UDOFIN contract]** Acknowledge every application, preferably with the disposal timeline. *Build:* U7 issues an in-app and SMS/email acknowledgement naming the RE as lender, the application number and the RE's disposal timeline from U2.
- **REQ-RBC-13** **[RE]** Sanction letter in the vernacular with the annualised rate and method of application; acceptance kept on record; late-payment penalties in bold in the loan agreement. *Build:* U8 shows `SanctionLetterIssued` unaltered and sends acceptance with evidence as `BorrowerAccepted`; U2 onboarding QA checks the bold penalty clause.
- **REQ-RBC-14** **[RE→UDOFIN contract]** Copy of the loan agreement and **every enclosure quoted in it** to every borrower at sanction or disbursement. *Build:* U9 delivers the executed pack to the borrower vault and by email, checked against the RE's enclosure list, with delivery evidence.
- **REQ-RBC-15** **[RE]** Notice of any change in terms (disbursement schedule, rates, service or prepayment charges) in the borrower's language; rate and charge changes **prospective only**. *Build:* U12 consumes `ScheduleChanged`; U16 notifies in the borrower's language; U12 raises an exception to the RE (never displays silently) when a change's effective date precedes its notice date.
- **REQ-RBC-19** **[RE]** Consent or objection to a borrower's request to transfer the borrowal account **within 21 days** of receipt. *Build:* U12 service request "account transfer" routed to the RE with a 21-day clock and escalation; Udofin never decides.
- **REQ-RBC-20** **[RE→UDOFIN contract]** No harassment (odd hours, muscle power); staff trained to deal with customers appropriately. *Build:* U16 quiet-hours engine applies to every outbound channel; U18 holds training records for every Udofin employee with borrower contact.
- **REQ-RBC-24** **[RE→UDOFIN contract]** The rate of interest is always an annualised rate. *Build:* U16 and U8 copy linter rejects any marketing or offer text that states a monthly or flat rate without the annualised rate and APR.
- **REQ-RBC-28** **[RE→UDOFIN contract]** No discrimination against physically or visually challenged applicants; PwD grievances handled through the GRM. *Build:* app and web accessible to WCAG 2.2 AA [recommendation]; assisted-journey fallback (U22 or call-back); U15 PwD tag on complaints.

**KFS (para 29; Annex I).** Scope: all retail and MSME term loans; credit-card receivables exempt.

- **REQ-RBC-29(1)** **[RE→UDOFIN contract]** KFS in the Annex I format, in a language the borrower understands, contents explained, **acknowledgement of understanding** obtained. *Build:* U8 renders `KFSIssued` unaltered with a plain-language explainer in the borrower's language and captures the acknowledgement with timestamp, device and KFS version hash.
- **REQ-RBC-29(2)** **[RE→UDOFIN contract]** Unique proposal number; validity **at least 3 working days for tenor of 7 days or more, 1 working day for tenor under 7 days**; the RE is bound if the borrower agrees within validity. *Build:* U8 shows a working-day countdown on the RE's holiday calendar; the accept action is disabled after expiry; the payday product (Product 2) uses the 1-working-day rule only where tenor is under 7 days.
- **REQ-RBC-29(3)–(4)** **[RE]** APR sheet and amortisation schedule; APR includes all RE charges and third-party charges at actuals. *Build:* U8 independently recomputes APR from the KFS cash flows (golden test: ₹20,000, 24 monthly instalments, 15% fixed, fees ₹400 → APR 17.07%) and blocks display on a mismatch above a configured tolerance, raising an exception to the RE.
- **REQ-RBC-29(5)** **[RE]** No fee or charge outside the KFS at any stage without explicit consent. *Build:* U12 flags any charge event not in the KFS; Udofin never collects any fee from the borrower (CF para 10(4)).
- **REQ-RBC-29(6)** **[RE]** KFS reproduced as a summary box in the loan agreement. *Build:* U9 pre-eSign check that the summary box is present.
- **REQ-RBC-29 Annex I Part 2** **[RE→UDOFIN contract]** Item 3: nodal GRO phone and email (a generic email only if responses come within 1 working day). Item 5: co-lending details (originating RE and share, partner RE and share, blended rate). Item 6: for digital loans, the cooling-off period and the LSP acting as recovery agent. *Build:* U8 validates these items are populated before display; U13 cannot start recovery contact by Udofin unless Udofin's role was disclosed in the KFS or notified under CF para 9(6).

**Penal charges (para 30):**

- **REQ-RBC-30** **[RE]** Penal charges only (never penal interest), not capitalised, only on the amount in default, disclosed in the agreement, KFS and website. **[RE→UDOFIN contract]** Every non-compliance reminder states the applicable penal charges, and each levy and its reason is communicated (30(7)). *Build:* U16 reminder templates carry a mandatory penal-charge field fed from U2; U12 shows each levy with its reason from the RE; Udofin never computes a penal charge.

**Floating reset, prepayment and release of documents:**

- **REQ-RBC-31** **[RE]** Floating-rate EMI personal loans: EMI/tenor impact at sanction, increases communicated immediately, **quarterly statement** (31(1), 31(6)). *Build:* U12 shows the statement; U16 relays notices.
- **REQ-RBC-34** **[RE]** For loans from 1 Jan 2026: no prepayment charge on floating-rate non-business loans to individuals; on business-purpose floating loans to individuals and MSEs none at UL, and none at ML up to ₹50 lakh; none where the RE initiates prepayment; undisclosed charges not leviable (34(1)–(2), (7)–(8)). *Build:* U12 shows the RE's quote and flags any charge absent from the KFS.
- **REQ-RBC-35–39** **[RE]** Personal loans only (Section F; para 6(11)): original movable or immovable property documents released and charges removed **within 30 days** of full repayment or settlement, at the branch or office the borrower chooses (35–36); lost documents: duplicates at the RE's cost and 30 more days (40); **₹5,000 per day** for RE-attributable delay. *Build (Phase 18):* U12 relays the borrower's choice and mirrors the RE's clock.
- Gold and silver collateral (paras 43–75): not applicable unless a gold-loan product is added.

**Microfinance conduct (paras 76–92).** Applies to any loan that is a microfinance loan (household income ≤ ₹3 lakh, collateral-free; CF para 51), whatever the product.

- **REQ-RBC-78–79, 81** **[RE→UDOFIN contract]** Loan card in the borrower's language (pricing, T&C, repayment acknowledgements, discharge, nodal officer); no prepayment charge. *Build:* U12 digital loan card from RE data.
- **REQ-RBC-89** **[RE→UDOFIN contract]** Identify borrowers facing repayment difficulty and guide them on recourse. *Build:* U12 hardship request type routed to the RE.
- **REQ-RBC-90–91** **[RE→UDOFIN contract]** Recovery at a mutually designated place; residence or workplace only after **two or more successive** failures to appear; harsh methods banned, including calls **before 09:00 or after 18:00**, persistent calls, harassing relatives or co-workers, publishing names. *Build:* U13 contact policy keyed on the microfinance flag (09:00–18:00 window, visit-location rule).
- **REQ-RBC-92** **[RE]** Dedicated recovery-grievance mechanism, details given at disbursal. *Build:* U15 recovery-grievance category; U10 disbursal notice carries the details.

**Recovery agents, DSAs, DMAs and telemarketers (paras 93–101).** Apply to Udofin only where an RE appoints Udofin (or its agency) as recovery agent, or uses Udofin for sourcing calls. Paras 93–97 sit in Section H (microfinance) but CF para 6(5) applies RBC to any LSP recovery agent [interpretation: apply 94–97 to all products].

- **REQ-RBC-94** **[RE→UDOFIN contract]** Due diligence covering individuals; antecedent **and police verification** of every recovery employee; re-verification at the RE-set periodicity. *Build:* U13 agent register with verification evidence and expiry; an agent without current verification cannot be allocated a case.
- **REQ-RBC-95–96** **[RE→UDOFIN contract]** Agent details given to the borrower when recovery starts; the agent carries the RE's notice, authorisation letter and ID card; on a change of agency the borrower is notified; notice and letter include the contact details of the agency and the RE. *Build:* U13 generates the notice and RE-signed authorisation letter per case; U16 sends agent particulars by email/SMS before first contact (CF para 9(6)); U22 shows the digital ID and letter to the borrower on request.
- **REQ-RBC-97** **[RE]** Up-to-date list of recovery agencies on the RE website. *Build:* U19 feed of Udofin's active agencies per RE.
- **REQ-RBC-98–99** **[RE→UDOFIN contract]** Training on soliciting, calling hours, privacy and correct T&C; code-of-conduct undertaking; adherence to the FPC and the RE's collection and repossession code; strict confidentiality. *Build:* U18 training and undertaking records per agent; U13 blocks allocation without both.
- **REQ-RBC-100** **[RE→UDOFIN contract]** No intimidation or harassment: public humiliation, intrusion on family, referees or friends, inappropriate mobile or social-media messages, threatening or anonymous calls, persistent calls, **recovery calls before 08:00 or after 19:00**, false representations. Not applicable to microfinance loans (paras 90–91 apply instead). *Build:* U13/U16 enforce the window in the borrower's local time on every channel, an RE-set frequency cap per day and week, registered caller IDs only, and no contact with any person other than the borrower and recorded co-obligants. Udofin cannot reach references or contacts in any case (CF para 13(1)). All recovery calls are recorded with a disclosure, retained per the RE contract; from 1 Jan 2027 call time and count are logged and calls recorded with disclosure, kept at least 6 months or until disposal if sub judice (Third Amendment para 100P) [VERIFY: official text not supplied]; before then recording is a recommendation.
- **REQ-RBC-101** **[RE→UDOFIN contract]** Only DoT/TRAI-registered telemarketers; the RE files the list and numbers with TRAI. *Build:* U16 places promotional and sourcing calls only from registered numbers and headers under the TRAI framework [VERIFY: current TRAI telecom commercial communications regulations], checks consent and preference before each call, and supplies its number list to each RE.

**Miscellaneous (paras 102–105):**

- **REQ-RBC-103** **[RE]** All transactions rounded to the nearest rupee (50 paise and above up; below 50 paise ignored). *Build:* U11 and U12 display and request only RE-posted rupee amounts; Udofin never re-rounds.
- **REQ-RBC-105** **[RE→UDOFIN contract]** Comply with the Supreme Court order of 30 Apr 2025 (Pragya Prasun; Amar Jain) [VERIFY: order text not reproduced; understood to concern accessible digital KYC for persons with disabilities]. *Build:* U5 offers non-blink liveness and assisted alternatives; no hard fail on a single biometric or gesture check.

---

## 8A.7 OUT — Managing Risks in Outsourcing Directions (363)

**Applicability to Udofin: through the RE's contract.** OUT binds NBFC and HFC REs (para 3(1)); BL REs apply all but Chapter IV and the IT-specific parts of Chapter II; ML and above apply all (3(2)). Udofin is a service provider. Its sourcing, application processing (loan origination), document processing, marketing, loan supervision, data processing and back-office work is **outsourcing of financial services under Chapter III** (para 4(1)); co-branded fintech applications fall under Chapter III (58(3)(iii)). The RE assesses materiality (para 14); a channel that originates and services a digital portfolio will usually be material [interpretation]. Where an ML-or-above RE also uses Udofin's hosted lender portal and data services, the RE may treat that as material IT outsourcing under Chapter IV (5(1)(iii)–(v), 58(2)) [interpretation; the RE decides]. **Design every arrangement to Chapter III and Chapter IV standards.** Existing IT agreements had to comply at renewal or by 10 Apr 2026, whichever was earlier (para 2); that deadline has passed. CF para 6(6)–(7) adds that the RE ensures its LSPs and DLAs comply with OUT and stays liable for all LSP acts and omissions. Bank REs: bank outsourcing Directions apply [VERIFY: not supplied].

**Functions Udofin must never perform (para 15):**

- **REQ-OUT-15** **[UDOFIN]** Udofin never performs or appears to perform the RE's compliance function, internal audit, **KYC-compliance decision** or **loan sanction** (OUT 15 names KYC compliance only for opening deposit accounts; KYC para 13 bars outsourcing the KYC-compliance decision generally). *Build:* U5 produces evidence and a recommendation, never a KYC decision; U7 routing and indicative eligibility are labelled as non-binding; no Udofin role can set a sanction, KYC-decision or classification state; a test proves these states arrive only by RE events (U21).

**Accountability and ownership (paras 9, 17–19, 59):**

- **REQ-OUT-17** **[RE]** The RE remains responsible for Udofin's actions, including DSA/DMA and recovery-agent activity, and keeps ultimate control. *Build:* U1 gives each RE a suspension switch per product, channel and activity (sourcing, servicing, recovery); U2 lets the RE withdraw any template or script immediately.
- **REQ-OUT-18(vi), 59** **[RE→UDOFIN contract]** A non-group provider may not be owned or controlled by an RE director or relative (18(vi), no exception); for IT outsourcing, also not by the RE's KMP, the arrangement approver or their relatives, unless the Board or a Board committee grants an exception with disclosure, oversight and monitoring (59 proviso; 13(iv)). *Build:* U1 conflict declaration at onboarding and annually, listing Infrabyx shareholders, directors and KMP for the RE to test.
- **REQ-OUT-19** **[RE]** CTR/STR remain the RE's. *Build:* U24 forwards suspicious-activity indicators to the RE; Udofin files nothing to FIU-IND on the RE's behalf.

**Confidentiality and security (paras 23–28, 68–70):**

- **REQ-OUT-24, 69(i)** **[UDOFIN]** Need-to-know access to customer information. *Build:* U23 role model scoped to RE and purpose; access reviews quarterly [recommendation].
- **REQ-OUT-26–27, 70** **[UDOFIN]** No commingling; each RE's customer data isolated and identifiable; in a multi-tenant system, clear separation so only RE-authorised personnel access its data. *Build:* PostgreSQL RLS by RE on every RE-scoped table (U1); borrower data shared with an RE only within the consent scope (U4); isolation tests in CI.
- **REQ-OUT-25, 28, 69(iii)** **[RE→UDOFIN contract]** Udofin discloses security breaches; the RE notifies RBI **immediately** of any breach or leakage of customer information and is liable to customers. *Build:* U24 breach workflow notifies every affected RE immediately on detection, within the 2-hour target (REQ-OUT-61), without waiting for confirmation.
- **REQ-OUT-61** **[RE→UDOFIN contract]** Cyber incidents reported to the RE without undue delay, so the RE can report to RBI **within 6 hours of detection by the service provider**. *Build:* U24 incident record with detection timestamp; notification to each affected RE within 2 hours of Udofin's detection [recommendation; internal target]; initial report fields aligned to DAKSH (8A.8).

**Due diligence and review (paras 29–32, 38, 71–72, 80):**

- **REQ-OUT-30, 71** **[RE→UDOFIN contract]** Udofin supports due diligence on financial, operational, legal and reputational factors, complaints and litigation, staff and subcontractor vetting, security and BCM, technology and DR, conflicts, data segregation, cyber risk and enforceability. *Build:* U18 vendor assurance pack, versioned, shared through the evidence room.
- **REQ-OUT-38, 80** **[RE]** Annual review (financial services) or risk-based review (IT) of the provider's condition. *Build:* U18 refreshes the pack at least annually and on material change.

**Agreement (paras 33–34, 73–74, 87–88).** The agreement is written, counsel-vetted and states the legal relationship (33, 73). Udofin's standard LSP agreement accepts every clause below; U1 stores a clause matrix per RE with pass/fail by clause ID.

| Clause | Udofin obligation and build |
|---|---|
| REQ-OUT-34(i) | Activity, service and performance standards; SLA schedule per RE (U19 SLA dashboard) |
| REQ-OUT-34(ii), 74(ii) | RE access to all books, records, data, logs, alerts and premises for the outsourced activity (U18 audit access) |
| REQ-OUT-34(iii) | Continuous monitoring by the RE (U19 live dashboards and monthly service report) |
| REQ-OUT-34(iv), 74(i) | **Prior RE consent for every subcontractor**; subcontractors bound to the same standards and audit (U18 sub-processor register with RE consent record) |
| REQ-OUT-34(v), 74(xix) | Confidentiality controls, NDA, Udofin liability for breach and leakage |
| REQ-OUT-34(vi), 74(x) | Contingency plans with testing (BCP schedule, joint tests) |
| REQ-OUT-34(vii) | RE audits by internal or external auditors or agents; copies of Udofin's audit reports |
| REQ-OUT-34(viii) | RBI access to records within reasonable time |
| REQ-OUT-34(ix), 74(xii) | RBI inspection of Udofin and its subcontractors, including infrastructure, applications and data |
| REQ-OUT-34(x), 74(xv) | Termination clause, minimum period, orderly transfer to another provider |
| REQ-OUT-34(xi)–(xii) | Confidentiality survives termination; documents and data preserved per the RE's legal obligations after termination |
| REQ-OUT-74(iii) | Listed material adverse events (data breach, denial of service, unavailability) reported to the RE |
| REQ-OUT-74(iv) | IT Act 2000 compliance and customer-data protection standards |
| REQ-OUT-74(vi) | **Data stored only in India** (also CF para 14(4)) |
| REQ-OUT-74(vii)–(viii) | Inventory of data captured, processed and stored per RE; data types Udofin may share with customers or others (U4 data map) |
| REQ-OUT-74(xi), 82 | Supply-chain disclosure for the RE's inventory and dependency map |
| REQ-OUT-74(xiii) | Udofin contractually liable for its subcontractors |
| REQ-OUT-74(xiv) | Compliance with RBI directions on the outsourced services |
| REQ-OUT-74(xvi)–(xviii) | Cooperation in the RE's insolvency or resolution; essential personnel on site in exigencies; back-to-back terms with OEMs and cloud providers |
| REQ-OUT-87–88 | Safe removal or destruction of data at exit; **no erasing or altering of data during transition** unless the RE or regulator advises; full cooperation with the incoming provider |
| REQ-OUT-74(v), 74(ix) | SLAs formalising performance criteria (U19); resolution process, events of default, indemnities, remedies and recourse for each party |

**Monitoring, audit and reconciliation (paras 12(2), 35–39, 75–81):**

- **REQ-OUT-36** **[RE]** Half-yearly Board or RMC review of material outsourcing. *Build:* U19 half-yearly report per RE.
- **REQ-OUT-12(2), 39** **[RE→UDOFIN contract]** Timely reconciliation; the RE's ACB reviews the ageing of entries pending reconciliation with vendors. *Build:* U11 `DailyReconciliationFile` with break ageing buckets; U17 reconciles Udofin's fee invoices with each RE.
- **REQ-OUT-77, 79, 81** **[UDOFIN]** Support pooled audits; offer globally recognised certifications (ISO/IEC 27001 and SOC 2 Type II targeted, not mandated) [recommendation]; grant unrestricted, effective access to the RE, its auditors, RBI and competent authorities. *Build:* U18 time-boxed read-only audit roles with access trail.

**BCP, exit and termination (paras 40–44, 83–89):**

- **REQ-OUT-40, 83** **[RE→UDOFIN contract]** Tested BCP and DR, joint tests on request.
- **REQ-OUT-42–43** **[UDOFIN]** Udofin can isolate, return or destroy each RE's information and records; the RE can intervene to continue operations. *Build:* U1 per-RE export (borrowers, consents, applications, documents, communications, recordings, audit logs) in a documented format; dry-run annually.
- **REQ-OUT-44, 89** **[RE]** On termination the RE publicises it so customers stop dealing with the provider. *Build:* U1 RE off-boarding state machine: new sourcing stops, servicing view continues per the transition plan, U16 notifies affected borrowers, and the RE updates its CIMS DLA lines (CF para 18(2)).

**Group arrangements (paras 45–51, 90–92).** Where the RE is an Infrabyx group company: **REQ-OUT-46, 50** **[RE→UDOFIN contract]** customers told which entity offers the product, with no implied group guarantee; **REQ-OUT-51, 92** **[RE]** arm's length and identical risk management. *Build:* U23 names the RE as lender on every offer, document and payment screen; group REs get the same clause matrix.

**Offshore (paras 52–53, 93–94):**

- **REQ-OUT-53** **[UDOFIN]** No offshore processing of RE customer data without the RE's prior consent; original records in India. *Build:* U20 AI features use India-hosted models or send no personal data offshore; any permitted offshore processing is deleted abroad and returned within 24 hours (CF para 14(4)).

**Cloud (para 97).** Udofin is a cloud SaaS (96(1)(i)(c)). *Build:* encryption keys and HSMs for RE data under the RE's control (97(vii)), offered as customer-managed keys per RE [recommendation; whether a pooled-key SaaS model is acceptable is the RE's decision], RBAC with SoD and MFA (97(viii)), logs exportable to the RE's SOC (97(xi)), exit with data return, portability and secure purge with independent assurance (97(xvi)).

**Grievances (paras 54–57, 98–99):**

- **REQ-OUT-55** **[RE→UDOFIN contract]** Product literature states that service providers may be used. *Build:* U23 LSP disclosure on every product page.
- **REQ-OUT-56, 98** **[RE]** Grievance responsibility rests with the RE; for microfinance, the agreement and FPC declare the RE accountable for service-provider staff behaviour. *Build:* U15 routes every complaint to the RE's GRO queue; Udofin's own nodal GRO handles DLA issues (CF para 12(1)) but never closes an RE complaint.
- **REQ-OUT-57** **[RE]** GRO name and contacts displayed where business is transacted, covering outsourced services; 30-day time limit; Ombudsman or CEPC route after rejection or no reply within 30 days. *Build:* U15 shows the RE GRO on the DLA and the RB-IOS route on day 31 or on rejection [VERIFY: the text cites the Integrated Ombudsman Scheme, 2021; confirm the current scheme name].

**Recovery agents:** OUT covers them only through para 17 (RE responsibility); conduct rules are in 8A.6.

---

## 8A.8 CYB — Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions (461)

**Applicability to Udofin: through the RE's contract.** CYB binds NBFC and HFC REs: Chapter III for BL below ₹500 crore and CICs, Chapter IV for BL of ₹500 crore and above, Chapter V for ML, UL and TL (para 3). It reaches Udofin through CF para 16 (LSPs comply with RBI cybersecurity standards), OUT Chapter IV clauses (8A.7), CYB paras 60–64 (outsourcing terms for BL REs of ₹500 crore and above), para 117 (vendor risk outside OUT) and paras 104–106 (software vendors). Udofin's app, web app and APIs are customer-facing systems in the RE's DMZ in substance; build them to the Chapter V standard so one platform satisfies every RE layer. Paras 21–64 cited below are Chapter IV (BL ≥ ₹500 crore; paras 31, 33 and 34 also bind Chapter III REs through para 8(5)); paras 97–146 are Chapter V (ML and above), which has no counterpart to paras 33–34 (para 110 mirrors 21(8)). CYB itself prescribes no data localisation, numeric RTO or log-retention period; those come from CF para 14(4), OUT 74(vi), the RE contract and CERT-In [VERIFY: CERT-In Directions of 28 Apr 2022 on 6-hour reporting and 180-day log retention apply to Udofin as a body corporate; not in the supplied texts].

**Incidents:**

- **REQ-CYB-28, 141** **[RE]** The RE reports cyber incidents on DAKSH **within 6 hours of detection** (para 28, Chapter IV; para 141, Chapter V, which adds proactive CERT-In notification and has HFCs report to NHB); CYB sets no reporting clock for Chapter III REs. **[RE→UDOFIN contract]** Udofin's notification feeds that clock (OUT para 61). *Build:* U24 incident taxonomy, severity, detection time, affected REs and borrowers, initial-report template; notification to RE within the 2-hour internal target.
- **REQ-CYB-142, 146** **[RE→UDOFIN contract]** Incident procedures name outsourced staff roles; crisis-communication drills with service providers. *Build:* Udofin runbook with named roles per RE; drill participation logged in U18.
- **REQ-CYB-145** **[RE]** Lessons learnt from incidents. *Build:* U24 RCA report shared with affected REs (see ORM para 101 questions, 8A.14).

**Customer application security:**

- **REQ-CYB-33** **[RE→UDOFIN contract]** Mobile financial services ensure confidentiality, integrity, authenticity and **end-to-end encryption** (Chapter IV; applied to Chapter III REs by para 8(5)). *Build (U3, Phase 17):* TLS 1.2 or higher with certificate pinning; app attestation (Play Integrity, App Attest); root, jailbreak, emulator and hooking detection; secrets only in the platform keystore; no personal data in logs, screenshots disabled on sensitive screens; web app with HSTS, CSP and secure cookies.
- **REQ-CYB-34** **[RE→UDOFIN contract]** Social-media risk, including account takeover and impersonation. *Build:* U24 brand monitoring for fake apps, fake handles and fake collection links, with a takedown workflow and borrower alerts.
- **REQ-CYB-21(8)** **[UDOFIN]** Audit trails sufficient for audit, forensics and dispute resolution (Chapter IV). *Build:* tamper-evident audit log for every borrower-affecting and privileged action (U18).
- **REQ-CYB-119–120** **[UDOFIN]** No manual intervention in data transferred between critical applications; STP with authentication and audit trail. *Build:* U21 signed, idempotent messages; replay only through an audited, maker-checker re-push; no manual file editing.
- **REQ-CYB-115** **[UDOFIN]** MFA for privileged users of critical systems and critical activities. *Build:* MFA on the ops portal, lender portal and admin; step-up for configuration and data export.

**Vendor obligations:**

- **REQ-CYB-62** **[RE→UDOFIN contract]** (BL ≥ ₹500 crore REs) contract terms: continuous monitoring; **admin audit trails and logs retained by Udofin and accessible to the RE on approved request**; audit rights and report copies; RBI access to paper and electronic records within reasonable time. *Build:* U18 log-access request workflow.
- **REQ-CYB-64, 138** **[RE→UDOFIN contract]** Proactive BCP assurance; collaborative resilience testing that meets the RE's RTO. *Build:* Udofin publishes RTO and RPO per service; joins RE drills.
- **REQ-CYB-97** **[RE→UDOFIN contract]** Service providers comply with the RE's information-security and acceptable-use policies. *Build:* U18 attestation per RE for Udofin staff with RE-portal or RE-data access.
- **REQ-CYB-104–106** **[RE→UDOFIN contract]** (Chapter V REs) maintenance and support by formal agreement (104); for applications the RE treats as critical, source code or **escrow including all updates and fixes** (105); written certificate that the application is **free of known vulnerabilities, malware and covert channels**, at onboarding and on each material change. *Build:* release pipeline produces SBOM, SAST, SCA and DAST results and a signed certificate per material release; escrow offered as an option.
- **REQ-CYB-117** **[RE]** Vendor risk assessment for concentration, conflicts, single points of failure, legal compliance, high availability and supply chain. *Build:* U18 sub-processor list, SPOF analysis and HA design note.

**Testing and resilience:**

- **REQ-CYB-121–126** **[RE→UDOFIN contract]** VA **at least every 6 months** and PT **at least every 12 months** for critical and customer-facing DMZ systems, plus pre-implementation, post-implementation (on production) and after change, by independent experts; time-bound fixes with no recurrence of known CVEs; CVSS-based approach covering cloud. *Build:* Udofin runs this cadence on app, web, APIs and portals and shares reports and remediation status with each RE (U18).
- **REQ-CYB-129, 131** **[RE]** DR drills at least half-yearly; DR run as primary for a full working day (Chapter V). *Build:* Udofin's own half-yearly DR drill, evidence shared.
- **REQ-CYB-102** **[RE]** DC and DR geographically separated. *Build:* both in India (Phase 21 AWS ap-south-1 and ap-south-2).

---

## 8A.9 FRM — Fraud Risk Management Directions (463)

**Applicability to Udofin: through the RE's contract.** FRM binds NBFCs and HFCs in UL, ML and BL with assets of ₹500 crore and above, on the audited balance sheet of the preceding 31 March (para 3). It does not bind BL REs below ₹500 crore. HFCs report frauds to NHB. Udofin is a third-party service provider: it can be served a show-cause notice (6(1)), held contractually accountable (31), and is the source of most digital-journey fraud signals (23).

- **REQ-FRM-6** **[RE]** (Udofin as respondent: **[UDOFIN]**) Persons examined for fraud include third-party service providers; a detailed SCN gives **not less than 21 days** to respond; a reasoned order follows (6(1)–(4)). *Build:* U18 legal-matter workflow for an SCN served on Udofin; U24 evidence export when an RE examines a borrower.
- **REQ-FRM-31** **[RE→UDOFIN contract]** Agreements may hold third parties accountable where their wilful negligence or malpractice causes fraud. *Build:* clause accepted in the standard LSP agreement (U1).
- **REQ-FRM-15, 19–23** **[RE]** ML and UL REs run an EWS integrated with their systems; every alert is examined; monitoring of transactions **through digital platforms and applications**, with vigilance on non-KYC and mule accounts. **[RE→UDOFIN contract]** Udofin supplies signals, not determinations. *Build:* U24 risk-signal service: device reuse across applicants, emulator or tampered app, SIM or device change before disbursal, location mismatch, document or selfie tampering scores, bank account reused by unrelated borrowers, identity velocity; delivered to the RE as a new event (`RiskSignalRaised`, to be added to Part 5 through Finbyx change control) with evidence references.
- **REQ-FRM-35** **[RE]** Persons classified as fraud are debarred from credit from RBI-regulated entities for 5 years from full repayment of the defrauded or settlement amount. *Build:* Udofin cannot see fraud lists; U7 routing honours the RE's decline without disclosing the reason beyond the RE's reason code.
- **REQ-FRM-40, 43** **[RE]** Immediate report to law enforcement; FMR **within 14 days** of classification, irrespective of amount. **[RE→UDOFIN contract]** Udofin's evidence pack (application trail, KYC evidence, device data, consents, communications and recordings) within the contractual SLA. *Build:* U24 one-click evidence pack per application or loan, hash-sealed.
- **REQ-FRM-42(10)** **[RE]** Digital-payment frauds are a reporting category. *Build:* U11 and U24 capture fake payment links, impersonated collection and UPI-handle misuse as incidents and notify the RE.
- **Fraud by Udofin staff or agents** **[UDOFIN]** Interpretation: the RE's staff-accountability rules (paras 32–34) do not reach Udofin staff, but the RE must still classify and report the fraud. *Build:* U24 notifies the RE immediately of any suspected fraud by Udofin employees or agents (fictitious applications, misappropriated cash recoveries); U13 reconciles every cash receipt to the RE ledger on the same day (CF para 10(5)).

---

## 8A.10 WD — Treatment of Wilful Defaulters and Large Defaulters Directions (358)

**Applicability to Udofin: through the RE's contract.** WD binds ML-and-above NBFCs, HFCs and CICs (para 2(1)); the bar on further finance to wilful defaulters and the large-defaulter provisions apply to **all RBI-regulated entities** (para 2(2) proviso). A wilful defaulter has outstanding of **₹25 lakh and above** (3(1)(xix)), so most Udofin unsecured loans will never generate a classification, but any borrower, guarantor or (for non-individual borrowers) director may already be on the list.

- **REQ-WD-7(3)** **[RE]** No additional credit to a wilful defaulter or associated entity; bar continues **1 year** after removal from the LWD; no finance for new ventures for **5 years** after removal. *Build:* U7 never routes or displays an offer from an RE that has declined on this ground; U6 sends the identifiers the RE needs.
- **REQ-WD-19(1)** **[RE]** At appraisal, the RE checks directors of a company, guarantors and persons in charge against the large-defaulter list and LWD by DIN/PAN, and resolves identical names through **independent sources, not a borrower declaration**. **[RE→UDOFIN contract]** Udofin supplies verified identifiers only; it never runs or decides the check. *Build:* U5 captures verified PAN for applicants, co-applicants and guarantors; for non-individual borrowers (Phase 18 secured products) U5 captures DIN and PAN of directors and persons in charge from verified sources [VERIFY: MCA21 data access route]; no self-declaration substitutes for these fields.
- **REQ-WD-19(2)** **[RE]** End-use monitoring and certificates from borrowers; legal action on false certification is the RE's. **[RE→UDOFIN contract]** Udofin collects certificates where the RE product requires it. *Build:* U12 end-use certificate request and capture where the RE product requires it, with the consequence notice.
- **REQ-WD-7(4)** **[RE]** Covenant in non-individual credit agreements barring LWD persons from the board or management. *Build:* U9 template check for business-purpose products.
- **REQ-WD-21** **[RE]** Third parties engaged by the lender that played a vital role in sanction or disbursement and were negligent or facilitated a wilful default are reported to IBA, after a hearing, for a caution list circulated to all REs (21(1)–(3)). *Build:* U18 legal-matter workflow for any hearing notice served on Udofin (as REQ-FRM-6); U24 evidence export.

---

## 8A.11 DPS — Digital Payment Security Controls Directions (462)

**Source:** RBI/DoS/2026-27/462; DoS.CO.CSITEG.56/31.01.015/2026-27; 31 Jul 2026, effective immediately (para 2).

### Applicability to Udofin

- **Not directly, and not through most REs.** The Directions apply only to "Credit-Card issuing Non-Banking Financial Companies" (para 3). Their scope is the digital payment products and services the card-issuing NBFC offers, including non-financial functions such as app registration, OTP generation, transaction status and raising disputes (para 4(1)).
- **Card-issuing partner REs.** If a partner RE issues credit cards, Udofin's repayment features are the LSP's DLA, not a product "offered directly by the NBFC". They are probably outside para 4(1) unless the RE's contract brings them in [VERIFY: each card-issuing RE's interpretation].
- **Voluntary baseline.** As in Finbyx, Udofin adopts the controls below as its voluntary security baseline for U3, U11 and U24. They also help meet CF para 16 and the RE's OUT and CYB flow-downs (see 8A.7, 8A.8). Each item is tagged **[UDOFIN]** (voluntary).

### Controls adopted

- `REQ-DPS-22` `REQ-DPS-23` **[UDOFIN]** No sensitive data in HTML hidden fields, cookies or client-side storage. WAF and DDoS mitigation on internet-facing services.
  - *Build:* U23 web, U24 edge.
- `REQ-DPS-30` `REQ-DPS-32` **[UDOFIN]** Threat modelling across the application lifecycle. Source review and VA/PT covering OWASP, with VA at least half-yearly, PT at least annually, and both on major change.
  - Where an RE does not own the code, it needs the developer's certificate that the application is "free of known vulnerabilities, malware, and any covert channels". Vendor contracts carry penal clauses.
  - *Build:* U24 security calendar. U18 issues the developer certificate to each RE, and Udofin accepts penal clauses in its RE contracts.
- `REQ-DPS-31` **[UDOFIN]** (voluntary; contractual only where a card-issuing RE brings Udofin's app within para 4(1)) For third-party-licensed payment applications, source-code escrow or equivalent continuity arrangements.
  - *Build:* U1 records the escrow agent and the release triggers [decision].
- `REQ-DPS-37` **[UDOFIN]** Monitoring for rogue or look-alike apps on app stores and the web, with takedown.
  - *Build:* U24 brand-monitoring job, run weekly.
- `REQ-DPS-40` **[UDOFIN]** Account numbers and other sensitive data are masked in SMS and email, including attachments.
  - *Build:* U16 template linter.
- `REQ-DPS-41` `REQ-DPS-46` `REQ-DPS-50` `REQ-DPS-51` **[UDOFIN]** Authentication and alerts: MFA with at least one dynamic or non-replicable factor for payment initiation; MFA and alerts for changes to bank account, mobile, email or mandate; a maximum number of failed attempts, then lock; secure reactivation; customer notification of failed attempts.
  - *Build:* U3 and U11.
- `REQ-DPS-57` **[UDOFIN]** Reconciliation with gateways, aggregators and other participants "not later than 24 hours from the time of receipt of settlement file(s)".
  - *Build:* U11 status reconciliation with the RE's PG/NACH data feeds. Udofin reconciles statuses, never funds.
- `REQ-DPS-58` `REQ-DPS-65` `REQ-DPS-66` **[UDOFIN]** Customer protection in the app: non-skippable secure-usage guidance in the customer's preferred language, at onboarding and after updates, with confirmation recorded; services provided only on a specific opt-in with acknowledgement of terms; an in-app "mark as fraudulent" action.
  - *Build:* U3 onboarding, U15 fraud-report type routed to the RE, U24.
- `REQ-DPS-67` **[UDOFIN]** Web application controls: adaptive authentication or a strong CAPTCHA with server-side validation; DNS-poisoning protection and secure cookies; a virtual keyboard option; inactivity timeout; forced change of system-issued passwords on first login.
  - *Build:* borrower web app (U3) and the portals (U23).
- `REQ-DPS-68` **[UDOFIN]** Mobile application controls: a server-side version check, and directing the user to reinstall on anomalies; device policy checks (vulnerable OS, malicious apps, insecure Wi-Fi); **one live version, with older versions deactivated within six months** of a newer release; remote-access app detection; minimal data collection and permissions; root and jailbreak checks; a published checksum, or a store link or QR code on the website; **device binding** "through a combination of hardware, software, and service information", with new-device alerts on multiple channels and a device register the user can disable; re-authentication at launch and after idle; unsecured-network detection; no credentials, keys or hashes on the device; an encrypted local database; TLS errors shown and blocked; obfuscation.
  - *Build:* U3 and U24 (Expo/React Native native modules).
  - **Conflict to resolve:** SIM-based "service information" usually needs telephony permissions that CF para 13(1) forbids a DLA. Udofin binds on hardware and software attestation (Play Integrity, App Attest) plus the OTP-verified registered mobile, without `READ_PHONE_STATE` or SMS permissions [VERIFY: RE and app-store acceptance of this binding design].

---

## 8A.12 Lender governance and audit touchpoints (CMP 460, GOV 344, IAF 464, SA 465, AUD 468)

**Applicability to Udofin: not directly; each shapes the evidence and approvals Udofin must hold before and after go-live.**

**CMP 460** binds ML and UL NBFCs registered under the RBI Act or the Factoring Regulation Act (para 3); HFCs registered under the NHB Act are outside its text [interpretation].

- **REQ-CMP-9(7)** **[RE]** The Compliance Department approves **every new process and product before introduction**. **[RE→UDOFIN contract]** *Build:* U2 and U18 go-live gate per RE: no new product, journey change, KFS or communication template, routing rule, collection script, DLA release or sub-processor goes live for an ML or UL RE without a recorded RE compliance approval (approver, date, scope, version hash). The materiality threshold for "new process" is agreed per RE in the LSP agreement.
- **REQ-CMP-15(2)** **[RE]** New products intensively monitored **for at least the first six months**. *Build:* U19 six-month monitoring pack per new product: volumes, rejections, complaints, cooling-off exits, early DPD, conduct exceptions.
- **REQ-CMP-31** **[RE]** The CCO sits on the new-product committee or evaluates every product. *Build:* the U18 approval record names the RE's approving officer.
- **BL REs** have no CMP, but the CCO or Board-designated official certifies each DLA on CIMS (CF para 18(3)–(4)). *Build:* U18 DLA certification evidence pack covering 18(4)(i)–(iv) for every RE.

**GOV 344:**

- **REQ-GOV-23** **[RE]** In NBFCs with assets above ₹5,000 crore (para 19), the CRO vets every credit product, retail or wholesale. *Build:* the U18 go-live record accepts a CRO-vetting reference.
- **REQ-GOV-17(2)** **[RE]** The Audit Committee ensures an IS audit; the cross-reference to OUT periodicity is a drafting slip (Appendix F). *Build:* Udofin supports the RE's IS audit through U18 access.

**IAF 464** binds deposit-taking NBFCs and HFCs, and non-deposit-taking ones with assets of ₹5,000 crore and above (para 3).

- **REQ-IAF-23** **[RE]** Internal audit is kept informed of new products and changes. *Build:* U18 release notes per RE delivered to the RE's IA contact.
- **REQ-IAF-39** **[RE]** Internal audit is not outsourced. Udofin never performs the RE's internal audit; it grants auditors read-only access (OUT 34(vii)).

**SA 465 and AUD 468:**

- **REQ-SA-3** **[RE]** SA governs only the RE's own statutory auditors. Udofin's auditor certifies Udofin's DLG declaration under CF para 20(3) (8A.1), not under SA.
- **REQ-AUD-11** **[RE]** (NBFC auditors; HFC auditors follow the HFC Directions, AUD 3) The RE's auditor reports non-compliance with applicable RBI Directions to the RBI SSM or Regional Office. Digital-lending compliance is therefore in audit scope. *Build:* U18 period-end evidence pack per RE: DLA register lines, consent and data-localisation attestations, fund-flow attestation (no pass-through accounts), DLG positions and disclosures, complaint MIS, recovery-agent register.

---

## 8A.13 Prudential touchpoints (IRACP 356, RSA 357, CAP 345, TDCR 352)

**Applicability to Udofin: not directly.** The RE owns classification, provisioning, restructuring, capital and co-lending accounting. Udofin must display the RE's positions correctly, relay borrower requests, and feed the RE what it needs.

**IRACP 356 (updated as on 13 Feb 2026):**

- **REQ-IRACP-15** **[RE]** For loans sanctioned on or after 31 Dec 2021, the agreement states exact due dates, frequency, principal/interest break-up and **examples of SMA/NPA dates**; the borrower is told at sanction and on every change. *Build:* U8 and U9 display the RE's examples; U12 redisplays them on every `ScheduleChanged`.
- **REQ-IRACP-17** **[RE→UDOFIN contract]** Consumer education on overdue, SMA, NPA and upgrade with reference to the day-end process. *Build:* U25 shows RE-approved education in the borrower's language; U16 reminders state the date each status would apply.
- **REQ-IRACP-18–19** **[RE]** Overdue flagged and SMA/NPA classified in the day-end process for the calendar date. *Build:* U12 mirror shows the RE's `DPDChanged` and `AssetClassificationChanged`; Udofin's shadow DPD computation only raises reconciliation exceptions.
- **REQ-IRACP-36A–36C** **[RE]** DLG under CF Chapter III or TDCR Part B may be reflected in ECL only where integral to the loan's contractual terms and not recognised separately; Ind AS 1 disclosures; **ECL recomputed after every invocation**. **[RE→UDOFIN contract]** *Build:* U14 sends invocation and settlement events the same day and a monthly DLG-set coverage file. Whether a DLG is "integral to the contractual terms of the loan" is the RE's accounting judgement [interpretation]; Udofin must not represent provisioning relief.

**RSA 357:**

- **REQ-RSA-18–19** **[RE]** SMA-0 up to 30 days, SMA-1 more than 30 up to 60, SMA-2 more than 60 up to 90; applies to all loans including retail. *Build:* U12 shows the RE's SMA status with plain-language consequences.
- **REQ-RSA-87** **[RE]** Compromise settlement is not a right; it is the RE's commercial discretion. **[UDOFIN]** Udofin only relays. *Build:* U12 settlement-request form sends the request and borrower proposal to the RE (`SettlementRequested`, adopted in v1.1; Part 7A UR1); no Udofin user can approve, promise or price a settlement; the app shows the RE's decision verbatim.
- **REQ-RSA-89–90** **[RE]** A settlement payable over **more than three months**, or any part settlement, is restructuring. *Build:* U12 shows the RE's characterisation and the credit-report consequence before the borrower accepts.
- **REQ-RSA-91** **[RE]** A technical write-off waives no claim. *Build:* U12 never shows "waived" for a technically written-off balance.
- **REQ-RSA-95** **[RE]** Cooling period before fresh exposure to a settled borrower: Board-set, **floor 12 months**. *Build:* U7 per-RE suppression list fed by the RE; the borrower can still see other REs' offers.
- **REQ-RSA-100** **[RE]** Settlement during pending judicial recovery needs a consent decree. *Build:* U12 shows the RE's status only.
- Products 7 (resolution finance) and 10 (debt reset) must be tested against these rules in their feasibility gate (Phase 19).

**CAP 345:**

- **REQ-CAP-15(3)** **[RE]** An NBFC that is a DLG provider deducts the full outstanding DLG from capital. For an RE that receives DLG from Udofin, capital and credit-risk mitigation on the loans continue under CAP (CF para 26(1)): **the RE gets no capital relief**. *Build:* U16 and sales material may not claim capital relief; where another RE acts as LSP and provides DLG, U14 flags the CAP deduction to that RE.

**TDCR 352, Part B co-lending (from 1 Jan 2026 or earlier by RE policy; para 95).** Digital co-lending follows both CF and Part B (para 98). Udofin may act as LSP to the originating RE, with the partner RE named in the KFS.

- **REQ-TDCR-104–105** **[RE]** The CLA agreement covers fees for lending services, segregation of responsibilities, the time-frame for exchanging critical information, customer interface and grievance redressal; the loan agreement names the **single point of customer interface**, changed only after prior intimation to the borrower. *Build:* U1 records the CLA and Udofin's role; U23 shows the interface entity.
- **REQ-TDCR-106, 108–109** **[RE]** CLA details in the KFS; **blended rate** weighted by funding shares; any partner rate change updates the blended rate and is communicated. *Build:* U8 checks KFS Part 2 item 5 is populated; U16 relays blended-rate changes.
- **REQ-TDCR-116–117** **[RE]** Separate borrower account per RE for its share; **all disbursements and repayments go through a bank escrow**. *Build:* U11 mandates and payment links point to the escrow, never to one RE's account or to Udofin; U12 mirror shows each RE's share.
- **REQ-TDCR-124** **[RE]** Borrower-level SMA/NPA classification across both REs, shared near-real time and **by end of the next working day**. *Build:* U12 shows one classification; a divergence between co-lenders raises an exception to both.
- **REQ-TDCR-111, 123** **[RE]** Lending-service fees must not include credit enhancement or DLG "unless permitted otherwise"; the originating RE may give DLG up to 5% of CLA loans outstanding. Whether Udofin may also give DLG on CLA loans is unresolved [VERIFY: TDCR 111 versus CF para 19]. *Build:* U14 blocks a DLG set that includes CLA loans until legal sign-off is recorded.

---

## 8A.14 Reporting, applicability and resilience (SR 466, MISC 373, SBR 339, ORM guidance note)

**SR 466** binds all NBFCs except HFCs (para 3). Udofin files no return. No return in the para 21 catalogue is filed from LSP data alone, but SR's data-governance rules cover outsourced data processes (para 6), so Udofin data used in the RE's returns must be reconcilable and traceable.

- **REQ-SR-6, 14–15, 17** **[RE→UDOFIN contract]** Data-quality standards for outsourced processes; returns reconciled with own sources; records of sources and aggregation rules; accuracy measured. *Build:* U19 feeds to each RE carry record-level lineage (source event, timestamp, version) and a daily control total reconciled to the RE's LMS.
- **REQ-SR-26** **[RE]** Returns under other Directions are unaffected. The Udofin-dependent ones are: the **CIMS DLA report**, one line per DLA per platform, updated when a DLA is added or ceases (CF para 18); Udofin's **monthly DLG portfolio disclosure on its website within 7 working days** of month-end (CF para 28); FMR evidence (8A.9); and the RE's financial-statement disclosures of complaints and co-lending (FS para 21(10), 21(4)). *Build:* U19 DLA register export per RE; U14 disclosure publisher; U15 complaint MIS in the FS ground-wise format.

**MISC 373:**

- **REQ-MISC-27** **[RE]** All transactions rounded to the nearest rupee; cheques with paise not rejected (also RBC para 103). *Build:* U11 payment requests use the RE's rounded amount.
- **REQ-MISC-22–23** **[RE→UDOFIN contract]** Move to electronic payments; **no fresh or additional PDCs or EMI cheques** alongside NACH mandates; CTS-2010 cheques only where NACH is unavailable. Para 23 does not apply to HFCs (para 3(1)(iii)). *Build:* U11 supports eNACH and UPI AutoPay only; no PDC capture flow.
- **REQ-MISC-24** **[RE]** Cash disbursal of loans only within Income-tax Act ss.269SS and 269T (MISC Section J); Udofin never disburses. *Build:* U13 cash-recovery limits configurable per RE [VERIFY: cash-receipt limits (s.269ST) and section numbering under the Income-tax Act, 2025; not in the supplied text].
- **REQ-MISC-14–15** **[RE]** AA participants follow the ReBIT specifications. *Build:* U6 AA flows to ReBIT (8A.4).

**SBR 339.** The RE's layer and type decide which Directions bind it, and so which Udofin controls switch on:

| RE profile | Effect on what Udofin supports |
|---|---|
| BL below ₹500 crore | OUT Chapter III only; CYB Chapter III; no FRM, WD (except the all-RE proviso), CMP or IAF |
| BL of ₹500 crore and above | CYB Chapter IV, including outsourcing contract terms (CYB 60–64); FRM applies; EWS not required (FRM 13 is ML/UL only) |
| ML (including all HFCs and NBFC-D; non-deposit NBFCs from the date assets reach ₹1,000 crore, SBR paras 11, 22) | OUT Chapter IV; CYB Chapter V; FRM with EWS; WD; CMP go-live gate (not HFCs); RBC 34(2) prepayment rule up to ₹50 lakh |
| UL | As ML; RBC 34(2) without the ₹50 lakh limit |
| Assets of ₹5,000 crore and above, and every deposit-taking NBFC or HFC for IAF | IAF (IAF 3); CRO vetting above ₹5,000 crore (GOV 19, 23) |

*Build:* U1 RE regulatory profile (RE type, NBFC category, layer and source, asset size and date, deposit-taking flag, effective dates); U18 resolves the obligation set and re-runs it when the profile changes, opening contract-amendment tasks where a new chapter applies.

**ORM guidance note (DOR.ORG.REC.301).** Guidance, not a Direction; applies to commercial banks, RRBs, UCBs, AIFIs and NBFC-BL, ML and UL (para 8). REQ-ORM IDs carry the register strength flag "guidance".

- **REQ-ORM-73** **[RE]** Due diligence verifying the third party has **at least equivalent operational resilience** for the RE's critical operations. *Build:* U18 resilience statement: critical services, impact tolerances, RTO/RPO, test history.
- **REQ-ORM-74–76** **[RE]** Board-approved third-party policy and register; exit plans and substitutability; provider **contractually liable for subcontractors including nth parties**. *Build:* clause accepted (also OUT 74(xiii)); U18 nth-party map.
- **REQ-ORM-69–72** **[RE]** Mapping of critical operations including third-party dependencies and single points of failure. *Build:* Udofin supplies a dependency map of the digital channel per RE.
- **REQ-ORM-87, 99, 101** **[RE]** Lessons from incidents, including at third parties; lessons-learned exercise with RCA. *Build:* U24 post-incident report answering the para 101 questions (cause, impact on critical operations, recovery speed, communication, tolerance breach, control adequacy) [VERIFY: the para 101 question list is not legible in the supplied text].

---

## 8A.15 Directions with no direct Udofin obligation

| Direction | Why no direct Udofin obligation | Data or support Udofin must give the RE |
|---|---|---|
| CRM 350 (Credit Risk Management) | Credit policy, appraisal and portfolio risk are the RE's | Application and bureau-consented data to the RE's underwriting; LSP-originated portfolio MIS for the RE's monitoring (CF para 6(4)) |
| CON 351 (Concentration Risk Management) | Exposure limits are measured on the RE's book | Group and related-party identifiers for business borrowers (Phase 18); routing caps if an RE configures them in U7 |
| INV 354 (Investment Portfolio) | Udofin holds no RE investments; LAS collateral is pledged security, not RE investment | None |
| BR 342 (Branch Authorisation) | Udofin offices are not RE branches | A deposit-taking NBFC with NOF up to ₹50 crore or rating below AA may appoint agents only within its home State (para 6) [VERIFY: whether LSP sourcing counts as appointing agents]; U7 can geo-restrict such REs |
| ALM 355 (Asset Liability Management) | Liquidity and rate risk are on the RE's balance sheet | Pipeline and expected-disbursement forecast on request (U19) |
| FS 359 (Financial Statements) | Disclosures are the RE's | Complaint MIS in the ground-wise format (para 21(10)); CLA and DLG data for notes to accounts (para 21(4)) |
| CLM 364 (Climate Change Risks) | Climate risk governance is the RE's | Collateral location data for secured products on request |
| DIV 360 (Dividends) | RE capital distribution only | None |
| SEC 353 (Securitisation) | Securitisation is between the RE and investors | KFS Part 2 item 4 disclosure display; lender-of-record and servicer changes reflected in the U12 mirror with borrower notice |
| MSD 467 (Miscellaneous Supervisory) | CFSS, nomination and PCA bind the RE | Ch III interest-charging fairness (para 7): U12 shadow checks that interest starts from the disbursement date, EMIs are on the disbursed amount, a revised schedule is issued on each part-disbursement, interest runs only for the days outstanding in the month of disbursal or repayment, and instalments collected in advance reduce the interest base (7(1)–(5)); Udofin assisted-onboarding points carrying RE signage may count as RE fixed-point units (para 5) [interpretation] |
| Credit Cards Issuance and Conduct Directions (referenced in OUT 4(1); not supplied) | No card product in scope | None |

---

## 8A.16 Cross-module build list from Part 8A

The module specifications in Part 7 and the phase instructions in Part 12 must include the items below. Where Part 7 or Part 12 and Part 8A differ, **Part 8A prevails**.

### 8A.16.1 Module additions (Part 7)

| Module | From | Additions |
|---|---|---|
| U1 Tenancy, lender onboarding and LSP agreement registry | 8A.1–8A.5, 8A.11 | Versioned LSP agreement record covering scope of LSP functions, DLAs covered, recovery-agent appointment, DLG yes/no, minimal data set and retention schedule; a tenant cannot go live without it (CF paras 6(1), 14(1)). DLA register lines created at onboarding in the U18 DLA register, with Annex-I export per RE (CF para 18(1)–(2), Annex-I). RE type (NBFC-MFI or other, HFC, bank) and s.11A PML notification flag (MFI para 8(3); KYC para 23). Udofin CIN and incorporation evidence before DLG (CF para 19). Escrow agent record (DPS para 31) |
| U1 Tenancy, lender onboarding and LSP agreement registry | 8A.6–8A.10, 8A.12–8A.15 | RE regulatory profile (RE type, NBFC category, layer and source, asset size and date, deposit-taking flag) driving the obligation set (SBR 10–12, 22); OUT clause matrix per RE with pass/fail by clause ID (OUT 34, 74, 87–88; CYB 62); conflict declaration at onboarding and annually (OUT 18(vi), 59); per-RE suspension switch by product, channel and activity (OUT 17); off-boarding state machine and full per-RE data export (OUT 42–44, 87–89; CF 18(2)) |
| U2 Lender product catalogue and configuration | 8A.1–8A.5, 8A.11 | Beneficiary rule: borrower account only, except RE-flagged end-use products (CF para 10(1)). No borrower-facing Udofin fee type (CF para 10(4)). Microfinance acceptance switch and pricing ceiling per RE (CF paras 60–61; MFI para 49). CIC preference order (CIR para 20). LAS eligible list excludes the RE's own shares (CF para 105). Housing-finance classification (CF para 4(1)(xiv)) |
| U2 Lender product catalogue and configuration | 8A.6–8A.10, 8A.12–8A.15 | Policy references per RE product (RBC 7); RE compliance go-live gate with approver, date, scope and version hash for every new product or process (CMP 9(7), 31; GOV 23); template QA for bold penal clause and KFS summary box (RBC 13, 29(6)); penal-charge schedule feed for reminders (RBC 30(7)) |
| U3 Borrower identity, authentication and device binding | 8A.1–8A.5, 8A.11 | CI manifest and plist allow-list forbidding contacts, call-log, telephony, SMS, storage, precise-location and background-location permissions (CF para 13(1)). One borrower ID mapped to a separate UCIC in each RE (KYC paras 17(6), 66). Registered-mobile lock for NFTF accounts and Aadhaar-mobile pinning for OTP-e-KYC accounts (KYC paras 25(2), 44(2)). Device binding without telephony permissions; MFA, lockout and secure reactivation (DPS paras 41, 46, 50–51, 68) |
| U3 Borrower identity, authentication and device binding | 8A.6–8A.10, 8A.12–8A.15 | Preferred language at registration (RBC 10); app security baseline: E2E encryption, pinning, attestation, root and jailbreak detection (CYB 33) |
| U4 Consent, privacy and data lifecycle | 8A.1–8A.5, 8A.11 | Purpose-bound consent artefacts with an audit trail; granular deny, restrict, revoke and erase (CF para 13(1)–(4)). Data-classification register and per-RE minimal data set; purge of KYC, bureau and AA artefacts on RE acknowledgement (CF para 14(1)). Published storage and destruction policy (CF para 14(2)). AA artefact mirror and purge on revocation or expiry (AA paras 17, 20, 28). Express-permission gate for cross-selling (KYC para 61) |
| U4 Consent, privacy and data lifecycle | 8A.6–8A.10, 8A.12–8A.15 | Data map per RE of data captured, processed and stored, and data Udofin may share (OUT 74(vii)–(viii)); RE-scoped consent boundary for multi-lender data (OUT 26–27, 70) |
| U5 KYC and verification | 8A.1–8A.5, 8A.11 | Evidence-only results; "KYC complete" set only by an RE actor (KYC para 13). Non-Aadhaar routes on equal footing; Aadhaar masking; number-based e-KYC only for s.11A-notified REs (KYC para 23, Expl 1 and 4). OTP-e-KYC tag and limits (KYC para 25). V-CIP as the RE's application with no Udofin retention (KYC para 27(1)(i)). V-CIP offered first for NFTF (KYC para 44(1)). KYC Identifier first (KYC para 63(9)) |
| U5 KYC and verification | 8A.6–8A.10, 8A.12–8A.15 | Evidence and recommendation only, never the KYC decision (OUT 15); verified PAN for applicants and guarantors and DIN/PAN of directors for non-individual borrowers, no self-declaration substitute (WD 19(1)); accessible liveness alternatives (RBC 105) |
| U6 Credit data, income and affordability | 8A.1–8A.5, 8A.11 | Per-RE bureau adapter using RE credentials; no Udofin bureau account (CIR paras 6, 20). Age, occupation and income mandatory (CF para 8(1)). Household composition and income questionnaire; monthly family income field; indicative 50% obligation ratio (CF paras 51–56; CIR Annex I MFI field 49). AA used only as the RE's FIU flow (AA para 8(12)) |
| U7 Application, eligibility and lender routing | 8A.1–8A.5, 8A.11 | Matched and unmatched lender sets; versioned, consistent matching models with a change log (CF para 7(1)–(2)). Microfinance flag (CF para 51). No DLG input to routing (CF para 20(2)). No new-to-credit hard filter (CIR para 38(5)). OTP-e-KYC ₹60,000 per-year cap (KYC para 25(5)). Microfinance routing only to accepting REs (MFI para 49) |
| U7 Application, eligibility and lender routing | 8A.6–8A.10, 8A.12–8A.15 | Application acknowledgement with RE disposal timeline (RBC 12); comparison information and document checklist (RBC 11); routing labelled non-binding (OUT 15); per-RE suppression list for settlement cooling periods (RSA 95); honour RE declines without exposing fraud or wilful-defaulter grounds (FRM 35; WD 7(3)); optional geo-restriction for NBFC-D REs (BR 6) |
| U8 Offers, KFS, disclosures and cooling-off | 8A.1–8A.5, 8A.11 | Offer card with lender, amount, tenor, APR, monthly obligation, penal charges and KFS link; ranking only by a published metric; dark-pattern checklist (CF para 7(3)–(4)). RE KFS shown unaltered with validity period (CF para 9(1); RBC para 29(2)). Cooling-off period and exit terms shown before acceptance (CF para 11). Block microfinance offers with prepayment charges or above the ceiling (RBC para 81; CF para 60) |
| U8 Offers, KFS, disclosures and cooling-off | 8A.6–8A.10, 8A.12–8A.15 | Working-day KFS validity clock, 3 or 1 working days by tenor (RBC 29(2)); independent APR recomputation with golden test 17.07% (RBC 29(3)); acknowledgement of understanding (RBC 29(1)); Annex I Part 2 items 3, 5, 6 validation (RBC Annex I); annualised-rate copy linter (RBC 24); CLA blended rate display (TDCR 106, 108) |
| U9 Documents, eSign, eStamp and DMS | 8A.1–8A.5, 8A.11 | Delivery of the RE's digitally signed pack on RE letterhead without re-rendering (CF para 9(3)). Microfinance loan card rendering (RBC para 78) |
| U9 Documents, eSign, eStamp and DMS | 8A.6–8A.10, 8A.12–8A.15 | Full agreement pack with every enclosure delivered and evidenced (RBC 14); KFS summary-box pre-eSign check (RBC 29(6)); LWD covenant check for business products (WD 7(4)) |
| U10 Disbursement orchestration | 8A.1–8A.5, 8A.11 | Status-only orchestration; verified borrower beneficiary (CF para 10(1)). Show the RE's address-confirmation status for NFTF customers before the RE disburses (KYC para 44(3)) |
| U10 Disbursement orchestration | 8A.6–8A.10, 8A.12–8A.15 | Disbursal notice carries the recovery-grievance mechanism for microfinance loans (RBC 92) |
| U11 Repayments, mandates, payments and reconciliation | 8A.1–8A.5, 8A.11 | Payment links, UPI and mandates only on RE merchant or sponsor accounts; connector validator blocks Udofin accounts (CF para 10(2)–(3)). Every payment event reaches the RE (CIR para 10(3)). Status reconciliation within 24 hours of settlement file (DPS para 57). Cooling-off exit payment to the RE account (CF para 11(1)) |
| U11 Repayments, mandates, payments and reconciliation | 8A.6–8A.10, 8A.12–8A.15 | Electronic mandates only, no PDC capture (MISC 22–23); RE-rounded amounts only (RBC 103; MISC 27); CLA payments to the bank escrow only (TDCR 117); reconciliation break ageing for the RE's ACB (OUT 12(2), 39); digital-payment fraud incident capture (FRM 42(10)) |
| U12 Loan mirror and borrower servicing | 8A.1–8A.5, 8A.11 | Persistent cooling-off exit action (CF para 11). Limit increase only on a borrower request event (CF para 8(2)). DLG invocation never shown as reducing dues (CF para 25(2)). Drawdown and top-up requests withheld in Udofin channels 12 months after OTP-e-KYC without upgrade; the debit bar is the RE's (KYC para 25(6)–(7)) |
| U12 Loan mirror and borrower servicing | 8A.6–8A.10, 8A.12–8A.15 | Prospective-only change check (RBC 15); account-transfer service request with 21-day clock (RBC 19); floating-rate quarterly statement display (RBC 31(6)); release-of-documents relay and clock (RBC 35–39); microfinance loan card (RBC 78–79); hardship request (RBC 89); SMA/NPA display and examples (IRACP 15, 18–19; RSA 18); settlement-request relay with RE characterisation (RSA 87, 89–91); end-use certificate capture (WD 19(2)); interest-charging shadow checks (MSD 7) |
| U13 Collections and recovery support | 8A.1–8A.5, 8A.11 | Enabled only with a recovery-agent appointment (CF para 6(5)). Hard gate: agent particulars delivered before first contact (CF para 9(6); RBC paras 95–97). Cash receipts only on overdue loans, full amount, same-day RE posting, no fee netting (CF para 10(5)). Contact windows: 09:00–18:00 microfinance, 08:00–19:00 others (RBC paras 91(2), 100). Visit rule after two successive non-appearances (RBC para 90) |
| U13 Collections and recovery support | 8A.6–8A.10, 8A.12–8A.15 | Active only under an RE recovery-agent contract; agent register with police verification, training and undertaking (RBC 94, 98–99); per-case notice and authorisation letter (RBC 95–96); 08:00–19:00 window, 09:00–18:00 and visit rule for microfinance (RBC 90–91, 100); frequency caps and registered caller IDs; same-day cash reflection (CF 10(5)) |
| U14 DLG management | 8A.1–8A.5, 8A.11 | Eligibility gate (CF para 19). Instrument register for the three forms (CF para 23). Fixed DLG set ledger with 5% of disbursed cap and implicit-guarantee modelling (CF para 24). No reinstatement transaction (CF para 25(4)). Recovery-sharing ledger (CF para 25(3)). Invocation within 120 DPD and term at least the longest tenor (CF para 27). Monthly portfolio disclosure within 7 working days (CF para 28). Auditor-certified declaration data (CF para 20(3)) |
| U14 DLG management | 8A.6–8A.10, 8A.12–8A.15 | Same-day invocation events and monthly coverage file for RE ECL recomputation (IRACP 36A–36C); no capital-relief claims (CAP 15(3); CF 26(1)); block CLA loans in a DLG set pending legal sign-off (TDCR 111, 123) |
| U15 Grievance redressal, AI support and Equator | 8A.1–8A.5, 8A.11 | Udofin nodal officer; in-app and web intake; immediate forwarding to the RE GRO; CMS and CRPC escalation text at day 31 or on rejection (CF para 12). Credit-report complaint type capturing email and bank account or UPI (CIR para 35(8)). Fraud-report type (DPS para 66) |
| U15 Grievance redressal, AI support and Equator | 8A.6–8A.10, 8A.12–8A.15 | Every complaint routed to the RE GRO; Udofin GRO never closes RE complaints (OUT 56, 98; CF 12); RB-IOS route on day 31 or rejection (OUT 57(4)); PwD and recovery-grievance categories (RBC 28, 92); complaint MIS in the FS ground-wise format (FS 21(10)) |
| U16 Communications, notifications and marketing | 8A.1–8A.5, 8A.11 | CIC default-reporting alerts on the RE's behalf when contracted (CIR para 34(1)(i)). Copy linter blocking "RBI registered/approved" claims (CF para 18(6)) and masking account numbers (DPS para 40). No KYC-derived marketing audiences without express permission (KYC para 61). OTP-e-KYC upgrade reminders (KYC para 25(6)) |
| U16 Communications, notifications and marketing | 8A.6–8A.10, 8A.12–8A.15 | RE-approved template per event per language, dispatch blocked otherwise (RBC 10); quiet-hours and frequency engine (RBC 20, 91, 100); penal charges in every reminder (RBC 30(7)); agent particulars before first contact (CF 9(6)); registered telemarketing numbers and consent checks (RBC 101); no claim of RBI endorsement from CIMS listing (CF 18(6)) |
| U17 Udofin finance and accounting | 8A.1–8A.5, 8A.11 | LSP fee invoicing to REs only (CF para 10(4)). DLG deposits, FD liens, BG contingent liabilities, invocations and recovery shares (CF paras 23, 25(3)). Cash-in-transit ledger for field recoveries (CF para 10(5)) |
| U17 Udofin finance and accounting | 8A.6–8A.10, 8A.12–8A.15 | Fee-invoice reconciliation with each RE (OUT 39) |
| U18 Compliance, regulatory register, audit access and LawDocsComply bridge | 8A.1–8A.5, 8A.11 | RE due-diligence pack (CF para 6(2)). Per-RE CIMS certification evidence pack (CF para 18(3)–(4)). Sub-processor and SDK register with processing location (CF paras 14(4), 15(2)). Channel risk pack before each new DLA or KYC method (KYC para 68). DLG disclosure calendar on working days (CF para 28). Developer security certificate (DPS para 32) |
| U18 Compliance, regulatory register, audit access and LawDocsComply bridge | 8A.6–8A.10, 8A.12–8A.15 | Vendor assurance pack refreshed annually (OUT 30, 38, 71, 80; ORM 73); sub-processor register with RE prior consent (OUT 34(iv), 74(xi)); audit and RBI access roles (OUT 34(vii)–(ix), 81; CYB 62); DLA certification evidence (CF 18(4)); period-end evidence pack for RE auditors (AUD 11); training and undertaking records; obligation resolver by RE profile (SBR) |
| U19 Reports, MIS and lender dashboards | 8A.1–8A.5, 8A.11 | RE portfolio-monitoring dashboards for Udofin-sourced loans (CF para 6(3)–(4)). Microfinance sourcing MIS (MFI paras 12, 49) |
| U19 Reports, MIS and lender dashboards | 8A.6–8A.10, 8A.12–8A.15 | FPC conduct pack (RBC 8); SLA and half-yearly outsourcing report (OUT 35–36); six-month new-product monitoring pack (CMP 15(2)); recovery-agency list feed (RBC 97); record-level lineage and control totals (SR 6, 14–15, 17); DLA register export (CF 18) |
| U20 AI layer (governed) | 8A.1–8A.5, 8A.11 | No personal data to processors outside India unless deleted and repatriated within 24 hours; redacted prompts by default (CF para 14(4)). No access to AA data or KYC risk category (AA para 28; KYC para 20(4)) |
| U20 AI layer | 8A.6–8A.10, 8A.12–8A.15 | No personal data to offshore model endpoints without RE consent (OUT 53; CF 14(4)) |
| U21 Integration hub and lender connectors | 8A.1–8A.5, 8A.11 | Outbound calls refused without a matching consent ID (CF para 13(4)). Per-RE credential vault for CIC and AA FIU identities (CIR para 6; AA para 8(12)). Escalate cash receipts not acknowledged same day (CF para 10(5)) |
| U21 Integration hub and lender connectors | 8A.6–8A.10, 8A.12–8A.15 | Signed STP, audited maker-checker replay, no manual file editing (CYB 119–120); new events `ConsentWithdrawn`, `DataPrincipalRequest`, `SecurityIncidentNotified`, `DLGDisclosurePublished`, `RiskSignalRaised` and `SettlementRequested` adopted in the Ecosystem Integration Specification v1.0 (Part 5.2) |
| U22 Field and assisted-onboarding app | 8A.1–8A.5, 8A.11 | Digital KYC only as the RE's authenticated application with RE officer codes, watermarking and OTP text rules (KYC para 24). Cash receipts per CF para 10(5). Screening and training evidence for field staff (KYC para 72) |
| U22 Field and assisted-onboarding app | 8A.6–8A.10, 8A.12–8A.15 | Digital agent ID and authorisation letter shown to borrower (RBC 95); assisted path for PwD (RBC 28) |
| U23 Administration, white-labelling and theming | 8A.1–8A.5, 8A.11 | Per-RE disclosure panel linking to the RE's single-place page (CF para 9(4)–(5)). Publication of the storage policy, privacy policy, nodal officer details and monthly DLG disclosure (CF paras 12(2), 14(2), 15(1), 28). Web controls (DPS para 67) |
| U23 Administration, white-labelling and theming | 8A.6–8A.10, 8A.12–8A.15 | RE named as lender and Udofin as LSP on every screen (OUT 46, 55); FPC and RE website links (RBC 21; CF 9(5)); WCAG 2.2 AA [recommendation] |
| U24 Security operations, fraud and risk signals | 8A.1–8A.5, 8A.11 | Mobile controls, one live app version, rogue-app monitoring (DPS paras 37, 68). Geo-IP blocking and 3-working-day validators for V-CIP (KYC para 27). Sanctions pre-screen as a fraud signal only (KYC paras 54–57) |
| U24 Security operations, fraud and risk signals | 8A.6–8A.10, 8A.12–8A.15 | Incident notification to RE within 2 hours of detection [recommendation; the rule is the RE's 6-hour clock] (OUT 61; CYB 28, 141); breach notification (OUT 28); VA 6-monthly and PT annual (CYB 121–126); brand-impersonation monitoring (CYB 34); fraud signals (FRM 15, 19–23); evidence packs (FRM 40, 43); RCA per ORM 101 |
| U25 Borrower financial dashboard and transparency | 8A.1–8A.5, 8A.11 | FIP-record-prevails disclaimer on AA figures (AA para 14(11)). No PFM built on lender-purpose AA data (AA para 28). Display of the KYC Identifier (KYC para 63(6)) and the RE loan card (RBC para 78) |
| U25 Borrower financial dashboard | 8A.6–8A.10, 8A.12–8A.15 | Overdue, SMA and NPA education with day-end examples (IRACP 17) |

### 8A.16.2 Phase additions (Part 12)

| Phase | From | Addition |
|---|---|---|
| 0 | 8A.1–8A.5, 8A.11 | ADR on Udofin's regulatory position: LSP under CF para 4(1)(xix), DLA per channel, not CI or SU, not FIU, not KYC decision-maker. Add the KYC "paragraph 62" CKYCR cross-reference slip to errata.md |
| 0 | 8A.6–8A.10, 8A.12–8A.15 | Record the OUT Chapter III and Chapter IV design decision and the RE-type rule-pack approach (NBFC, HFC, bank) in an ADR |
| 1 | 8A.1–8A.5, 8A.11 | SDK inventory of every third party that can collect personal data through the DLA, with processing location, checked in CI and feeding the privacy policy (CF paras 14(4), 15(2)); the permission allow-list check is already in the Phase 1 instruction |
| 2 | 8A.1–8A.5, 8A.11 | India-only data residency for all stores; sub-processor register; data-classification register with per-RE minimal data set (CF para 14) |
| 2 | 8A.6–8A.10, 8A.12–8A.15 | RLS isolation tests per RE (OUT 26–27, 70); tamper-evident audit log (CYB 21(8)); MFA on privileged roles (CYB 115) |
| 3 | 8A.1–8A.5, 8A.11 | U1 LSP agreement registry, initial DLA register lines (U18 table) with Annex-I export, recovery-agent and DLG flags; U2 beneficiary and fee rules (CF paras 6, 10, 18) |
| 3 | 8A.6–8A.10, 8A.12–8A.15 | RE regulatory profile, clause matrix, conflict declaration, compliance go-live gate and suspension switches (U1, U2, U18) |
| 3b | 8A.1–8A.5, 8A.11 | Consent centre with purpose-bound artefacts, revocation and erasure; storage and privacy policy publication (CF paras 13–15) |
| 3b | 8A.6–8A.10, 8A.12–8A.15 | Language template registry, quiet-hours and frequency engine, telemarketing number registry and consent checks (U16) |
| 4 | 8A.1–8A.5, 8A.11 | Borrower identity across app and web; UCIC mapping per RE; registered-mobile lock; one-time camera, microphone and location in onboarding only (CF para 13(1); KYC paras 17(6), 44(2)) |
| 4 | 8A.6–8A.10, 8A.12–8A.15 | Preferred language capture; accessible journey and assisted fallback (RBC 10, 28) |
| 5 | 8A.1–8A.5, 8A.11 | KYC evidence pipeline with RE-actor decision; Aadhaar routes by s.11A status; OTP-e-KYC limits; V-CIP as RE application; CKYC Identifier first (KYC paras 13, 23, 25, 27, 44, 63) |
| 5 | 8A.6–8A.10, 8A.12–8A.15 | Accessible liveness alternatives (RBC 105); DIN/PAN capture for non-individual borrowers deferred to Phase 18 |
| 6 | 8A.1–8A.5, 8A.11 | Per-RE bureau adapter; household-income questionnaire and microfinance flag; indicative 50% obligation ratio (CIR paras 6, 20; CF paras 51–58) |
| 7 | 8A.1–8A.5, 8A.11 | Multi-lender offer view with unmatched lenders, published ranking metric, dark-pattern review; KFS display; cooling-off display and exit (CF paras 7, 9, 11) |
| 7 | 8A.6–8A.10, 8A.12–8A.15 | KFS validity clock, APR recomputation golden test, acknowledgement capture, Annex I Part 2 validation (RBC 29) |
| 8 | 8A.1–8A.5, 8A.11 | RE signed-document pack delivery without re-rendering; microfinance loan card (CF para 9(3); RBC para 78) |
| 8 | 8A.6–8A.10, 8A.12–8A.15 | Agreement pack completeness and summary-box checks (RBC 14, 29(6)) |
| 9 | 8A.1–8A.5, 8A.11 | Disbursement status orchestration with verified-beneficiary checks; connector validator against Udofin accounts (CF para 10(1)–(3)) |
| 9 | 8A.6–8A.10, 8A.12–8A.15 | Disbursal notice carries the RE's recovery-grievance mechanism for microfinance loans (RBC 92) |
| 10 | 8A.1–8A.5, 8A.11 | Collections on RE merchant accounts only; 24-hour status reconciliation; no borrower fees (CF para 10(2)–(4); DPS para 57) |
| 10 | 8A.6–8A.10, 8A.12–8A.15 | Electronic mandates only; escrow routing for CLA loans; reconciliation ageing (MISC 23; TDCR 117; OUT 39) |
| 11 | 8A.1–8A.5, 8A.11 | Loan mirror with cooling-off exit, limit-increase request event and OTP-e-KYC drawdown block (CF paras 8(2), 11; KYC para 25(7)) |
| 11 | 8A.6–8A.10, 8A.12–8A.15 | Prospective-change check, 21-day transfer request, SMA/NPA display, settlement relay, end-use certificates, interest-charging shadow checks (RBC 15, 19; IRACP 15–19; RSA 87–95; WD 19(2); MSD 7) |
| 12 | 8A.1–8A.5, 8A.11 | Recovery-agent gating, notice-before-contact, contact windows, cash same-day posting (CF paras 6(5), 9(6), 10(5); RBC paras 90–100) |
| 12 | 8A.6–8A.10, 8A.12–8A.15 | Recovery-agent register, verification gates, notices, contact-window enforcement, call recording [recommendation], same-day cash reflection (RBC 90–100; CF 9(6), 10(5)) |
| 12b | 7A, 8A.6–8A.10, 8A.12–8A.15 | Rule pack B from 1 Jan 2027 (RBC Third Amendment paras 100A–100AB) [VERIFY: official text]; settlement relay with the RE's characterisation block and no Udofin approval (RSA paras 16(5), 87–100; CIR para 12(4); OUT para 15); ADR basis check and no referral scope (A&C Act s.7; *CORE*, SC, 8 Nov 2024); notice delivery evidence without a served state; same-day cash posting (CF para 10(5)) |
| 13 | 8A.1–8A.5, 8A.11 | DLG engine on the provider side, auditor declaration data, monthly website disclosure (CF paras 19–29) |
| 13 | 8A.6–8A.10, 8A.12–8A.15 | DLG event feed for ECL; CLA exclusion until legal sign-off (IRACP 36A–36C; TDCR 111, 123) |
| 14 | 8A.1–8A.5, 8A.11 | LSP nodal officer, intake, immediate RE routing, CMS and CRPC escalation; CIR complaint fields (CF para 12; CIR para 35(8)) |
| 14 | 8A.6–8A.10, 8A.12–8A.15 | RE GRO routing, RB-IOS day-31 prompt, FS-format complaint MIS (OUT 56–57; FS 21(10)) |
| 15 | 8A.1–8A.5, 8A.11 | LSP fee invoicing to REs; DLG instrument and cash-in-transit accounting (CF paras 10(4)–(5), 23) |
| 15 | 8A.6–8A.10, 8A.12–8A.15 | U19 FPC conduct pack, SLA and half-yearly outsourcing reports, six-month new-product monitoring pack, recovery-agency list feed, record-level lineage and control totals; U17 fee-invoice reconciliation with each RE (RBC 8, 97; OUT 35–36, 39; CMP 15(2); SR 6, 14–15, 17) |
| 16 | 8A.1–8A.5, 8A.11 | CIMS certification evidence pack; RE due-diligence pack; channel risk pack; DPS voluntary baseline controls (CF paras 6(2), 18(3)–(4); KYC para 68; DPS) |
| 16 | 8A.6–8A.10, 8A.12–8A.15 | Incident notification workflow, VAPT cadence, vendor assurance pack, audit access roles, fraud signals and evidence packs (OUT 61; CYB 121–126; FRM 15–23) |
| 17 | 8A.1–8A.5, 8A.11 | One line per DLA per store in the DLA register before each store or PWA launch; checksum or store link published; old app versions retired within 6 months (CF para 18; DPS para 68) |
| 17 | 8A.6–8A.10, 8A.12–8A.15 | Mobile and web security baseline and pre-release VA/PT; vulnerability-free certificate and SBOM per material release (CYB 33, 106, 121) |
| P | 8A.1–8A.5, 8A.11 | Pilot gate: each pilot RE confirms its Annex-I CIMS entries, cooling-off period, retention schedule, KYC route set and recovery-agent status in writing |
| P | 8A.6–8A.10, 8A.12–8A.15 | Pilot gate: RE compliance approval recorded for every pilot product (CMP 9(7)); RE confirms CIMS DLA lines; first joint BCP test; clause matrix fully passed |
| 18 | 8A.1–8A.5, 8A.11 | LAS own-share exclusion and LTV margin notices (CF paras 105–106); housing classification (CF para 4(1)(xiv)) |
| 18 | 8A.6–8A.10, 8A.12–8A.15 | DIN/PAN of directors and guarantors (WD 19(1)); release-of-documents relay (RBC 35–39); LWD covenant check |
| 18b | 6.4, 8A.1–8A.5, 8A.6–8A.10 | Gold: no Udofin handling of collateral (RBC paras 53–54), valuation and LTV only from RE data (CF paras 40, 43–44), auction and release notices shown as the RE's (RBC paras 58–69); microfinance household test and cap (CF paras 51–57) and loan card (RBC paras 78–81); MSME DIN or PAN of directors and guarantors (WD para 19(1)) and CGTMSE block on DLG (CF para 21(1)); end-beneficiary routing for education and supply chain (CF para 10(1)) |
| 19 | 8A.6–8A.10, 8A.12–8A.15 | Feasibility gate for resolution finance and debt reset tests RSA 87–100 restructuring characterisation |
| 20 | 8A.1–8A.5, 8A.11 | Field app digital KYC only after the authorised-officer question is resolved (KYC para 24) |
| 20 | 8A.6–8A.10, 8A.12–8A.15 | Field app shows the agent's digital ID and RE authorisation letter; assisted path for persons with disabilities (RBC 28, 95) |
| 21 | 8A.6–8A.10, 8A.12–8A.15 | DC and DR in separate India regions; exit and portability dry-run (CYB 102; OUT 87–88) |

### 8A.16.3 Open regulatory questions

Resolve each before the phase that depends on it, record the answer in the register, and mark whether it is law, interpretation or a decision of the RE.

- [VERIFY] Commercial-bank equivalents of CF Chapter III for bank REs (not supplied).
- [VERIFY] Current CCPA dark-pattern list referred to in CF para 7(4) Note.
- [VERIFY] Android SMS Retriever and SMS User Consent API behaviour (no SMS permission), and app-store policy on document pickers.
- [VERIFY] Whether KYC live photographs count as "biometric" under the Aadhaar Act s.2(g), and the basis for any retention by Udofin (CF para 14(3)).
- [VERIFY] Cooling-off start trigger in each RE's credit policy (CF para 11 is silent).
- [VERIFY] Which GRO each RE enters in the Annex-I CIMS columns for Udofin-owned DLAs.
- [VERIFY] Udofin's incorporating statute and CIN for CF para 19.
- [VERIFY] Ind AS treatment of DLG cash deposits, FD liens and BGs in Udofin's books.
- [VERIFY] How each RE converts bullet or payday repayments into a monthly obligation for the 50% test (CF paras 55–56).
- [VERIFY] CIR amendment RBI/DOR/2025-26/117 text (paras 10(2), 12(10), 15, Annex VI).
- [VERIFY] CICRA s.2(l), CIC Regulations reg 3 and CIC Rules on who may obtain a CIR; whether CICs allow a member CI's technology service provider; whether any "borrower's own report" flow may be used for pre-qualification.
- [VERIFY] Treatment of soft versus hard enquiries by each CIC.
- [VERIFY] Whether Udofin is a reporting entity under PML Act s.2(1)(wa).
- [VERIFY] Whether an RE-approved KYC rule executed on Udofin infrastructure satisfies KYC para 13 for each RE.
- [VERIFY] Each partner RE's s.11A notification status; the UIDAI AUA/KUA or sub-AUA arrangement for any vendor (for example Surepass); Aadhaar Data Vault obligations.
- [VERIFY] Whether a borrower-captured liveness selfie meets "live photo as specified under paragraph 24" for the e-document route (KYC para 23 proviso (iii)).
- [VERIFY] Whether Udofin field staff may be the RE's "authorised officer" for digital KYC (KYC para 24).
- [VERIFY] How each RE applies "first transaction shall be a credit" (KYC para 44(5)) to loan accounts.
- [VERIFY] Sahamati/ReBIT model for a technology service provider to an FIU; current ReBIT API version.
- [VERIFY] Any consent route under which borrower AA data could feed a personal-finance dashboard.
- [VERIFY] Current SRO Code of Conduct text for NBFC-MFI partners.
- [VERIFY] Card-issuing REs' view on whether Udofin repayment features fall within DPS para 4(1).
- [VERIFY] RE and app-store acceptance of device binding without SIM or telephony permissions (DPS para 68(6) against CF para 13(1)).
- Decision: carry the Udofin nodal officer and DLA particulars to REs in the U1 onboarding pack, or add LSP-to-RE events to the Part 5 catalogue through a versioned contract change.
- Decision: per-RE retention schedule for LSP-held data, signed off by each RE (CF para 14(1)).
- Decision: buy a V-CIP product contracted by the RE, or build it as the RE's application.
- Decision: source-code escrow agent and release triggers for REs that require them (DPS para 31).
- Decision: whether Udofin offers DLG at all, and to which REs; commercial terms must count any fee clawback as implicit DLG within the 5% cap.
- Decision: whether Udofin accepts recovery-agent appointments and cash collection (U13, U22) in the MVP.
- Does each RE classify Udofin under OUT Chapter III only, or also as material IT outsourcing under Chapter IV (OUT 58(3)(iii) versus 5(1))? This changes the clause set and audit scope per RE.
- Will Chapter V REs treat the DLA as a critical application needing source code or escrow (CYB 105), and who bears the escrow cost? (Escrow agent and release triggers: the DPS para 31 decision above.)
- Is Udofin owned or controlled by a director of any partner RE, or (for IT outsourcing) by its KMP, the arrangement approver or their relatives (OUT 18(vi), 59)? If so, Udofin must be a group company of that RE; only the IT bar admits a Board-approved, disclosed exception (59 proviso).
- Where an RE appoints Udofin as recovery agent: recording retention period and consent wording for recovery calls.
- Official texts of the RBC Second Amendment (Chapter IIIA) and Third Amendment (RBI/2026-27/230; paras 100A–100AB in force 1 Jan 2027) for docs/regulations/rbi/, and whether a microfinance-specific contact window survives the deletion of paras 89–97.
- Whether RBI's affidavit in *Shikha Ghosh v Axis Bank* (Del HC, due 16 Nov 2026; hearing 17 Nov 2026) leads to RBI instructions on lender arbitration that Part 7A UR2 must reflect.
- Which bank Directions (conduct, outsourcing, IT, fraud) apply to bank REs, and do any terms differ from the NBFC clause set?
- May Udofin give DLG on co-lending loans given TDCR 111 and 123?
- Persistent-calling cap: will each RE set a numeric daily and weekly cap, or will Udofin propose a default?
- TRAI registration path for Udofin's sourcing and reminder calls (telemarketer or principal entity) under the current regulations.
- Content and scope of the Supreme Court order of 30 Apr 2025 (RBC 105) for digital KYC design.
- For NBFC-D REs with NOF up to ₹50 crore or rating below AA, does LSP sourcing outside the home State count as appointing agents (BR 6)?
- Are offshore AI or analytics services acceptable to any RE, and on what data?
- Internal incident-notification target: confirm 2 hours from detection with each RE.

---

# PART 9 — INTEGRATIONS (PROVIDER ADAPTERS)

## 9.1 Design rules

- Keep provider-specific operations behind domain interfaces (U21), for example:
  - `KycProvider`, `DigiLockerRequester`, `CkycGateway`, `VcipLauncher`, `FaceMatchProvider`;
  - `BureauGateway` (RE-membership pulls) and `OwnReportProvider` (borrower-initiated);
  - `AccountAggregatorTsp`, `BankStatementAnalyser`, `BankAccountVerifier`;
  - `ESignProvider`, `EStampProvider`, `DepositoryPledgeProvider`, `MfLienProvider`;
  - `MandateProvider`, `PaymentCollectionGateway` (always on the RE's merchant account);
  - `LenderConnector` (Finbyx and generic LOS/LMS), `AccountingSink`;
  - `NotificationProvider` (SMS, WhatsApp, email, push, voice);
  - `OdrProvider` (Equator first; other ODR providers through the same contract), `GrcConnector` (LawDocsComply first; MetricStream, IBM OpenPages, ServiceNow IRM and Archer by field map);
  - `NoticeDispatchProvider` (delivery of RE-issued notices on add-on channels only), `CourtDataView` (read-only projection of RE-permitted case status; no direct court-data calls);
  - `GeoProvider`, `OcrProvider`, `StorageProvider`, `LlmProvider`, `IntegrityVerifier` (Play Integrity / App Attest).
- **Every adapter call carries an RE context.** The adapter resolves the credentials, contract and data scope of that RE. A call without an RE context fails, except for Udofin's own services (messaging for Udofin's own account, accounting, monitoring).
- **Contracting party decides the design.** Record for each integration whether the RE or Udofin is the contracting party (9.2). Where the law or the provider requires the RE to be the user (CIC membership, CKYCR, AA FIU, Aadhaar e-KYC, eNACH sponsor bank, payment-gateway merchant), Udofin builds the adapter and runs it as the RE's technology service provider, using credentials the RE owns and can revoke. Udofin never pools several REs' traffic under its own credentials.
- Do not try to make every infrastructure component interchangeable from day one.
- Build mock and sandbox adapters first. Label mock, sandbox and production in the UI, in logs, in config and in every evidence record. A mock result can never reach a production RE.
- For each adapter, document:
  - authentication and credential owner;
  - request validation;
  - response mapping and the evidence stored (provider transaction ID, timestamp, signed response or hash);
  - timeouts;
  - retries with idempotency;
  - duplicate handling;
  - error taxonomy and borrower-facing message;
  - reconciliation;
  - credential rotation;
  - data residency of the provider and its sub-processors;
  - what Udofin may retain after hand-off to the RE (CF para 14(1));
  - cost per call (feeds U17 unit economics).
- Do not assume every named provider offers an API or that access is automatically available. Verify current documentation, eligibility, commercial terms and authorisation requirements, and record them in `docs/integrations/register.md`.
- **I (the project owner) will procure and connect live credentials.** These include Surepass (already contacted), the eSign/eStamp providers, payment gateways, messaging vendors, Tally/SAP and the Apple and Google developer accounts. Where the RE must be the contracting party, I will arrange it with the RE. You build the adapters, contract tests and sandbox mocks.

**Correction to the original prompt.** The original prompt assumed that Udofin "soft-pulls CIBIL via Surepass". Udofin is not a member of any CIC and is not today a specified user under CICRA (it could apply later under CIC Regulations reg. 3 and RBI's January 2022 criteria; Part 8.2) [VERIFY], and the CIR Directions place membership on the credit institution (CIR para 6). A bureau pull for a lending decision must therefore run under the RE's CIC membership, with the borrower's consent naming the RE and the purpose; or the borrower obtains their own report through a CIC consumer channel and shares it. Surepass (or any aggregator) may act as a conduit only if the CIC contract permits it for that RE [VERIFY with each CIC]. The same applies to CKYCR and Aadhaar e-KYC.

## 9.2 Integration catalogue

| Capability | Candidate providers | Contracting party (RE or Udofin) | Notes |
|---|---|---|---|
| PAN verification | Surepass, Protean (formerly NSDL e-Gov), UTIITSL, Signzy, IDfy, HyperVerge, Decentro | Udofin for identity pre-checks; RE for the KYC record [interpretation] | PAN–name match and PAN–Aadhaar link status; store result and masked PAN only (CF para 14(1)) |
| Aadhaar OTP e-KYC | Through a KUA (or the RE as sub-KUA) | RE, only if notified under PML Act s.11A | KYC para 23 proviso (i); NFTF term-loan cap ₹60,000 a year (KYC para 25(5)); Udofin never stores the Aadhaar number (UIDAI Circular 14 of 2025) |
| Aadhaar offline verification (OKYC XML, secure QR) | Surepass, Digio, Decentro, IDfy | RE as OVSE; Udofin as technology provider | KYC para 23(2) and proviso (ii); redact Aadhaar number (Explanation 1) |
| DigiLocker | DigiLocker Requester APIs (direct or via Setu, Surepass, Decentro, Digio) | RE requester ID preferred; Udofin requester ID only if DigiLocker terms permit acting for the RE [VERIFY] | Issued documents as equivalent e-documents; verify digital signature (KYC para 23 proviso (iii)); consent per document |
| CKYC | CERSAI CKYCRR through the RE's reporting-entity credentials (direct or via Surepass, Decentro) | RE | Search and download only with explicit consent and KYC Identifier (KYC para 23(4)); upload is the RE's duty (KYC para 63) |
| V-CIP | Vendor platforms used by the RE (for example IDfy, HyperVerge, Signzy, Digio) | RE | Hosted on RE premises or RE-owned cloud; vendor retains no data; operated by RE officials; live GPS geo-tag; India-only IPs (KYC para 27) |
| Face match and liveness | HyperVerge, IDfy, Surepass | RE (8A.1, REQ-CF-14(3)); Udofin only as the RE's technology provider | No biometric storage (CF para 14(3)); keep score and decision only; accessible alternatives (RBC para 105) |
| Credit bureau | TransUnion CIBIL, Experian, Equifax, CRIF High Mark; Surepass as conduit if permitted | RE (membership, CIR para 6) | Pull under the RE's membership and purpose; store the report in the RE-scoped vault only for the agreed period; borrower own-report as alternative [VERIFY] |
| Account Aggregator | Licensed NBFC-AAs (for example Finvu, OneMoney, Anumati) via FIU gateways (Setu, FinBox, Perfios) | RE as FIU; Udofin as technology service provider | Consent artefact names the RE; use only as the artefact allows (AA para 28) |
| Bank statement and income analysis | Perfios, FinBox, ScoreMe, Karza | RE or Udofin per the LSP agreement | PDF upload uses the photo picker or document picker, never storage permission |
| Bank account verification | Penny-drop and pennyless (Surepass, Razorpay, Cashfree, Decentro) | Udofin or RE | Name match against KYC name; account must be the borrower's (CF para 10(1)) |
| GST, ITR, EPFO, Udyam, MCA | Surepass, Karza, Signzy | Udofin or RE | Income and employment verification with consent |
| eSign | Leegality, Digio, eMudhra, Protean eSign, Surepass | RE (signer is the borrower; document on the RE's letterhead) | Store provider transaction ID, certificate and document hash; never a bare "signed=true" (Finbyx Part 5.2) |
| eStamp | SHCIL e-stamping (via Leegality, Digio); state portals; NeSL DDE | RE | State-wise duty; stamp certificate stored with the agreement |
| Securities pledge (LAS) | NSDL and CDSL pledge APIs; CAMS, KFintech, MF Central lien | RE (pledgee) | Phase 18; pledge always in favour of the RE |
| Vehicle, property and collateral data | Vahan, CERSAI search, valuer and legal vendors, ULI where the RE is onboarded | RE | Phase 18 |
| Payment collection (UPI intent, cards, net banking, payment links) | Razorpay, Cashfree, PayU, Juspay, bank gateways | RE (merchant of record) | Funds settle to the RE's account; Udofin holds no merchant account for repayments (CF para 10(2)–(3)) |
| Mandates (eNACH, UPI AutoPay) | NPCI eNACH via the RE's sponsor bank or aggregators (Razorpay, Cashfree, Digio, Decentro); UPI AutoPay | RE (corporate utility code or merchant) | UMRN and limits sent to the LMS (`MandateRegistered`); UPI AutoPay lending categories up to ₹1 lakh without additional factor [VERIFY: NPCI circular] |
| Stripe and PayPal | Stripe (India accounts invite-only since 2024; primarily cross-border); PayPal (domestic India payments discontinued in 2021) | Udofin only | Not suitable for domestic repayment collection; use only for Udofin's cross-border SaaS billing if ever needed [VERIFY] |
| Finbyx | Finbyx LSP connector (Finbyx Part 5) | RE (Finbyx tenant) with Udofin | First certified connector; same event names as Finbyx Part 5.2 |
| Other LOS/LMS | Generic REST/webhook connector; file-based (SFTP) adapter; vendor-specific adapters as certified | RE | Connector certification suite in U21 |
| Accounting | TallyPrime (JSON/XML via local connector), SAP S/4HANA and Business One, Zoho Books, CSV | Udofin (its own books) | U17 exports Udofin's own ledger only; the loan book is the RE's |
| SMS | DLT-registered gateways (Gupshup, Kaleyra, Route Mobile, MSG91, Tanla) | RE header for lending messages sent on the RE's behalf; Udofin header for Udofin's own messages [interpretation] | DLT template IDs; TCCCPR consent categories |
| WhatsApp | WhatsApp Business Platform through a BSP | RE or Udofin | WhatsApp policy prohibits payday loans and debt collection on the platform; never use it for collections or short-tenor products |
| Email | Amazon SES (ap-south-1), Resend, SendGrid | Udofin | India-resident sending where personal data is in content [VERIFY residency] |
| Push | FCM, APNs (via Expo Push or direct) | Udofin | No personal or loan data in payloads; deep link to an authenticated screen |
| Voice and IVR | Exotel, Knowlarity, Ozonetel on 1600-series numbers | RE number series | Call recording where the RE's policy requires it |
| Equator | Equator Resolution ODR API and web flow (ADR domain of the Ecosystem Integration Specification) | RE for referral and mandate; Udofin only for the borrower link and status | The RE refers (RE-only scope) only under a pre-named institution clause or written post-dispute consent; Udofin never refers or appoints and sees no neutral selection; signed link into Equator's web flow, no separate app (Part 7A UR2) |
| Other ODR and ADR providers | Presolv360, Sama, Jupitice, Webnyay, CADRE; none publishes a lender API, so CSV or SFTP bulk exchange where needed [VERIFY under NDA] | RE | Same `OdrProvider` contract and ADR events; Udofin displays only status the RE forwards |
| Notice dispatch | DLT SMS gateways, email (SPF and DKIM), in-app inbox; print-to-post and the India Post bulk API (DoP contract and CEPT onboarding) only through the RE | RE for statutory notices; Udofin for add-on delivery of RE-issued notices | Udofin never issues a notice in its own name or marks one served; no WhatsApp for any recovery communication (Part 7A UR3) |
| Court-data and legal-tech | eCourts services (CNR), licensed aggregators (for example eCourtsIndia, Surepass CNR), Legitquest | RE | Udofin shows only RE-permitted, RE-worded status from `LitigationCaseUpdated`; it calls no court-data API and holds no litigation record (Part 7A UR3) |
| Third-party GRC tools | MetricStream (REST), IBM OpenPages (GRC REST), ServiceNow IRM (staging tables), Archer (REST, Content API); Indian tools such as Komrisk, Compfie, TeamLease RegTech [VERIFY APIs] | RE or Udofin | Generic GRC contract with OSCAL export (U18) |
| LawDocsComply | LawDocsComply GRC API | Udofin and each RE | Regulatory register, evidence and DLA register feed through the generic GRC contract; first certified GRC adapter [VERIFY: public API] |
| Maps and geolocation | Google Maps Platform, MapmyIndia (Mappls), OLA Maps | Udofin | Coarse location only in the store app; reverse geocoding for address pre-fill with consent |
| OCR and document AI | Self-hosted OCR in India, Surepass/IDfy OCR, LLM extraction via India-region endpoints | Udofin | Extraction is verified against source data; no autonomous decision (U20) |
| App integrity | Google Play Integrity API (standard requests), Apple App Attest and DeviceCheck | Udofin | Server-side verdict verification; failure triggers step-up, not silent block |
| Error tracking and analytics | Sentry (self-hosted in India), PostHog (self-hosted in India); Firebase Crashlytics only if the Phase 0 residency ADR accepts it (crash data and installation IDs are processed outside India) | Udofin | No PII; India residency ADR (CF para 14(4)) |

---

# PART 10 — TECHNOLOGY, ARCHITECTURE AND NON-FUNCTIONAL REQUIREMENTS

## 10.1 Recommended stack

Validate current versions in Phase 0 and propose changes through an ADR. Versions below were checked in October 2026.

| Layer | Recommendation | Reason |
|---|---|---|
| Monorepo | pnpm workspaces + Turborepo; TypeScript strict | Shared contracts, domain kernel and design tokens across app, web, portals and API |
| Borrower mobile app | **Expo SDK 57** (React Native 0.86, React 19.2; stable since 30 Jun 2026). SDK 58 (React Native 0.88) entered beta on 15 Sep 2026: adopt it after it is stable and Phase 0 has tested it. New Architecture (Fabric, TurboModules) only: it is mandatory from SDK 55. Hermes; Expo Router; EAS Build, Submit and Update | One TypeScript codebase for Android and iOS; managed native builds; controlled OTA for JavaScript-only fixes |
| Mobile libraries | expo-secure-store (Keystore/Keychain), expo-local-authentication (app unlock), expo-camera, the system photo and document pickers (no storage permission), @expo/app-integrity (alpha) or native Play Integrity / App Attest modules, react-native-mmkv with encryption for non-sensitive cache, TanStack Query, Zustand, Zod | Minimal permissions; secure storage; offline resume |
| Borrower web app | Next.js 16 (16.4 current, 6 Oct 2026) App Router + React 19; installable PWA (service worker for shell and static assets only) | Same journey on web; SEO for public pages; handoff to app where a native control is needed |
| Portals (operations, lender, admin) | Next.js 16 single portal app with role-based workspaces (recommended; see Appendix C); shadcn/ui + Tailwind with design tokens; TanStack Table v9 or AG Grid Community | Data-dense queues and configuration; one deployment, strict workspace isolation |
| Backend | Node.js 24 LTS (Maintenance LTS from 20 Oct 2026, end of life 30 Apr 2028; Node 26 becomes Active LTS on 28 Oct 2026 and is supported by Expo SDK 58, so decide 24 or 26 in the Phase 0 ADR; Node 20 reached end of life on 30 Apr 2026) + TypeScript; **NestJS (11 or 12, per the shared ecosystem ADR with Finbyx) modular monolith**. NestJS 12.0.0 was released in 2026 (ESM packages, Standard Schema validation; requires Node 20.19+ or 22.12+). Keep Finbyx and Udofin on the same NestJS major: decide 11 or 12 in one ecosystem ADR. OpenAPI 3.1 via Zod schemas; AsyncAPI for events | Business rules, integrations and controlled access on trusted servers |
| Database | PostgreSQL 16+ (Supabase ap-south-1 now; Amazon RDS/Aurora PostgreSQL ap-south-1 later); Drizzle ORM or Kysely; versioned SQL migrations; **enforced RLS** | Relational, transactional, portable |
| Money and maths | `NUMERIC` columns; decimal.js (precision ≥ 40); money as strings in APIs; property-based tests (fast-check) | Paisa-exact display of APR, EMI and DLG caps |
| Workflow orchestration | Temporal (TypeScript SDK; Temporal Cloud India regions or self-hosted) for application, KYC, signing, disbursement-status, mandate and grievance sagas; payload codec encryption so no PII sits in workflow history; pg-boss or Graphile Worker for simple jobs | Durable, resumable borrower journeys across app restarts and provider outages |
| Rules | GoRules ZEN engine (JDM decision tables) for RE eligibility pre-filters, routing and display rules; versioned per RE and effective-dated | Lender-specific configuration without code changes; replayable decisions |
| Events | Transactional outbox → Postgres queue or Redis Streams; Amazon MSK or Redpanda later | Reliable lender-connector events |
| Authentication | Borrowers: mobile OTP + device binding + app PIN/biometric unlock; Supabase Auth now, behind an OIDC abstraction (Keycloak or Cognito later). Staff and RE users: SSO/SAML/OIDC with mandatory MFA | Portability; strong staff authentication |
| Authorisation | Server-side policy layer (RBAC + ABAC; Cedar or OpenFGA) plus Postgres RLS by RE tenant, product and role | Supabase is never the only security boundary |
| Documents | S3-compatible private storage in India (Supabase Storage ap-south-1 → Amazon S3); per-RE keys by application-level envelope encryption under AWS KMS ap-south-1 (Supabase Storage offers no per-tenant customer-managed keys), then SSE-KMS per RE on S3; signed short-lived URLs; Gotenberg for PDF | KFS, agreements, signed documents |
| Search | PostgreSQL FTS + pg_trgm | Ops and lender queues |
| Reporting | Regulatory and lender reports in code; Apache Superset with row-level security for lender dashboards | Per-RE isolation |
| Observability | OpenTelemetry → Grafana stack self-hosted in India; Sentry self-hosted (or SaaS with no PII after ADR); mobile crash reporting with PII scrubbing | Production support; CERT-In 180-day log retention in India |
| Infrastructure | Docker. **Development and staging with synthetic data only:** Railway (no India region) + Supabase. **Any environment with real borrower data:** India-region only — Supabase ap-south-1 with India-region compute, or AWS ap-south-1 (primary) and ap-south-2 (DR) on ECS/EKS; OpenTofu/Terraform; KMS/CloudHSM; Secrets Manager; WAF and DDoS protection | Data localisation (CF para 14(4)); portability |
| Testing | Vitest/Jest; Testcontainers; Playwright (web E2E); Maestro or Detox (mobile E2E on real low-end Android devices); Pact (contract tests with Finbyx and LMS connectors); k6 (load); OWASP ZAP, Semgrep/CodeQL, MobSF (mobile static and dynamic) | Release gates |
| Mobile security baseline | OWASP MASVS v2.1.0 controls tested with MASTG v2.0.0 (30 Jun 2026) under the MAS-L2 and MAS-R testing profiles (MASVS v2 has no levels), with MASWE v1.0.0 weakness IDs | Recognised, testable mobile standard |
| Field app (later) | Same Expo codebase as a separate app target with its own bundle ID and MDM distribution | Assisted onboarding and collections, Phase 20 |

## 10.2 Architecture principles

These are mandatory. Principles 1–17 come from the original Udofin prompt; 18–35 are added for an LSP serving many REs.

1. Use a modular architecture with explicit domain boundaries (U1–U25). Start with a modular monolith, not microservices.
2. Define an owner for every important data entity, and record whether the RE or Udofin is the system of record (Finbyx Part 5.1).
3. Enforce RE-tenant isolation in the API, the service layer and the database (RLS), and test it. Borrowers see only their own data; lender users see only their RE's data.
4. Apply least-privilege access control.
5. Validate all sensitive operations on trusted backend services. The mobile app and the browser never hold privileged keys, never compute eligibility, routing, pricing or DLG, and never decide anything.
6. Use database transactions for operations that must be atomic.
7. Make every external side effect idempotent and safely retryable (idempotency keys stored and enforced).
8. Keep traceable state transitions for applications, offers, KFS versions, signing, disbursement status, mandates, payments, grievances and DLG. An application must not move to "disbursed" because the RE sanctioned it; only the RE's `LoanDisbursed` event with a UTR moves it.
9. Record critical operations as immutable, hash-chained audit events.
10. Keep configuration separate from code.
11. Keep secrets outside source control.
12. Keep migrations versioned and reviewed for locking, data loss, backward compatibility and rollback or forward recovery.
13. Use asynchronous processing for long-running tasks.
14. Implement structured logging, monitoring, error handling and alerting with **no Aadhaar number, PAN, OTP, account number, bureau data, document image or other sensitive personal data in logs, analytics events, crash reports or push payloads.**
15. Document API contracts, data models and material decisions (ADRs).
16. Avoid unnecessary duplication between app, web and backend: one journey definition, one validation schema, one copy deck.
17. Build reusable components only when their behaviour is clear.
18. **Udofin never lends and never touches money.** No Udofin bank account, wallet, virtual account or merchant account sits in any disbursement or repayment flow (CF para 10). Configuration that routes funds otherwise is rejected by a platform guard-rail that no RE or admin can switch off.
19. **The RE decides.** KYC compliance, credit decision, sanction, pricing, KFS, disbursement, classification, CIC reporting and grievance closure are RE decisions (OUT para 15; KYC para 13; CF para 12(3)). Udofin may pre-filter only on the RE's approved, versioned rules and must label every outcome with the RE rule version that produced it.
20. **Minimal LSP storage.** Udofin stores only the basic minimal data needed for its operations within the RE–LSP agreement (CF para 14(1)). Everything else (KYC documents, bureau reports, bank statements) lives in an **RE-scoped vault**: per-RE encryption keys (RE-controlled where the RE requires it, OUT para 97(vii)(b)), retention set by the RE's policy, purge after hand-off when the agreement says so, and every access logged and visible to the RE.
21. **Consent before data.** No data is collected or shared without a consent record naming the purpose, the RE(s) and the exact notice version (CF para 13; DPDP s.6). Purpose is disclosed at each stage (CF para 13(3)).
22. **Minimal device permissions.** Never request contacts, call logs, SMS, telephony, files or media, or installed-app lists (CF para 13(1); Play prohibited list). Camera and microphone only at the KYC step, one-time, with explicit consent. Location: coarse only, one-time, at onboarding; precise GPS only inside the RE's V-CIP session (10.3).
23. **Data in India.** All production data, backups, logs and sub-processors in India; data processed abroad deleted there and brought back within 24 hours (CF para 14(4)). No biometric data stored (CF para 14(3)).
24. **Lender neutrality.** The multi-lender offer view is driven by documented, versioned matching rules applied consistently to similarly placed borrowers; ranking only by a publicly pre-disclosed metric; unmatched lenders disclosed; no dark patterns (CF para 7).
25. **Regulation as configuration.** Cooling-off days, KFS validity, contact windows, DLG caps, microfinance thresholds, app-store APR and tenor limits live in versioned, effective-dated rule packs with platform guard-rails that an RE configuration can tighten but never loosen.
26. **Explainability.** Every pre-filter, routing decision and offer display stores inputs, rule version and output.
27. **Maker-checker** on every configurable sensitive action (RE onboarding, product publication, routing rules, DLG arrangements, credential changes, bulk exports).
28. **Loan mirror is read-only.** The RE's LMS is authoritative for schedules, balances, DPD and classification. The mirror is fed only by RE events and reconciled daily; it never computes a balance the borrower could rely on without showing the RE as source and the as-of time.
29. **Channel parity without weakening controls.** App and web run the same server-side journey. Where the web cannot meet a control (for example device binding or integrity attestation), the web journey applies a compensating control or hands off to the app by QR code or deep link.
30. **Store-policy gating.** Products and offers that a store policy prohibits (for example personal loans repayable in full in 60 days or less on Google Play and the App Store, or APR above 36% on the App Store) are filtered server-side by channel, with evidence of the filter in the decision record.
31. **Failure containment.** If an RE's connector is down, Udofin queues and shows the borrower an honest status; if Udofin is down, the RE's operations continue (Finbyx Part 5.1(5)).
32. **Straight-through data.** No manual edits to data passed to REs, LMSs, CICs or accounting systems; files are hashed and signed; exceptions use maker-checker with an audit trail (CYB paras 119–120).
33. **Regulator, RE and auditor access.** Time-boxed, read-only roles for each RE, its auditors and RBI over that RE's data, logs and evidence (OUT paras 34(viii)–(ix), 74(ii), 81; CYB para 62(2)).
34. **Scalability.** Design for 1 million+ borrowers in year one and 10 million+ registered users later, 100+ RE tenants, with partitioned tables (by RE and date) and horizontally scalable workers.
35. **Portability.** Containerised, environment-based config, storage and auth abstractions, IaC. Do not build an elaborate cloud-neutral platform before the product is validated.

## 10.3 Mobile engineering

**Framework and builds**

- Expo managed workflow with config plugins; `expo prebuild` only in CI (SDK 57 clears native folders by default). No hand-edited native folders in Git unless an ADR approves it.
- New Architecture only. Every native dependency must support it; record exceptions in the dependency register.
- EAS Build profiles: `development`, `preview` (internal testing, synthetic backend), `production`. Production builds run only from protected tags in CI. Signing keys: Play App Signing (Google holds the app signing key; Udofin holds the upload key in a hardware-backed secret store) and an Apple distribution certificate managed by EAS with two-person access.
- EAS Submit to Play internal testing → closed testing → production staged rollout; TestFlight → App Store phased release.
- One bundle per brand: the default Udofin app. A white-label app for an RE is a separate store listing, separate DLA line on CIMS and separate store declaration (Appendix B decision).

**Over-the-air (OTA) update policy**

- EAS Update may ship only JavaScript and asset changes that keep the app's reviewed purpose: bug fixes, copy, layout and content. Apple permits interpreted code that does not change the app's primary purpose (Developer Program License Agreement 3.3; Guideline 2.5.2). Google Play forbids self-updating by any route except Play, except for code run in an interpreter or virtual machine (Device and Network Abuse policy).
- **Never** ship by OTA: a new product, a new data collection or permission, a change to consent or disclosure screens, a change to payment flows, or any security control. Those require a store release with updated declarations.
- Updates are code-signed (EAS Update end-to-end code signing, available only on the EAS Production or Enterprise plan; the private key is held in KMS or the protected CI signing step, never in EAS or Git), tied to a `runtimeVersion`, rolled out by percentage, rolled back by the release pipeline when crash-free sessions regress, and logged in the release register.
- **Version sunset.** Keep only one supported app version per platform after a phased overlap of at most six months, and force an upgrade below the minimum supported version (DPS para 68(2)(iii) as voluntary baseline). The API rejects requests from unsupported versions with an upgrade screen.

**Permissions (just-in-time, with a purpose screen before each OS prompt)**

| Capability | Android | iOS | When | Rule |
|---|---|---|---|---|
| Camera | CAMERA | NSCameraUsageDescription | KYC selfie, document capture | One-time at KYC step, explicit consent (CF para 13(1)) |
| Microphone | None by default | None by default | V-CIP runs in the RE's web session in the system browser (Phase 0 ADR), so the browser asks for the microphone, not the app | Add RECORD_AUDIO and NSMicrophoneUsageDescription only if an ADR moves V-CIP in-app; then one-time, explicit consent |
| Location | ACCESS_COARSE_LOCATION only | When-in-use, reduced accuracy | One-time at onboarding for address pre-fill and fraud signal | ACCESS_FINE_LOCATION is prohibited for personal loan apps on Google Play; V-CIP geo-tagging (KYC para 27(1)(iv)) runs in the RE's V-CIP web session launched in the system browser or on the borrower web app [VERIFY: Google Play acceptance and RE V-CIP vendor support] |
| Photos and files | None: use the Android Photo Picker and Storage Access Framework document picker; iOS PHPicker and UIDocumentPicker | None | Uploading a salary slip or statement | READ_MEDIA_*, READ/WRITE_EXTERNAL_STORAGE are prohibited |
| Notifications | POST_NOTIFICATIONS | User notification authorisation | After first application | Service notifications only unless marketing consent exists |
| Biometrics | USE_BIOMETRIC | NSFaceIDUsageDescription | App unlock opt-in | Device-local only; no biometric data leaves the device or is stored by Udofin (CF para 14(3)) |
| OTP autofill | SMS Retriever / SMS User Consent API (no SMS permission) | One-time code autofill | Login | Never READ_SMS or RECEIVE_SMS; the DLT OTP template carries the 11-character SMS Retriever app hash computed from the Play App Signing certificate (not the upload key) and ends with the origin-bound line @[domain] #[code] for WebOTP and Safari autofill |

Never declare READ_CONTACTS, READ_CALL_LOG, READ_PHONE_STATE, READ_PHONE_NUMBERS, QUERY_ALL_PACKAGES or any accessibility service. CI fails if the merged AndroidManifest or Info.plist contains a permission not on the approved list (Phase 1 gate).

**Authentication, device binding and app unlock**

- Login by mobile OTP; device binding with a hardware-backed key generated in Keystore/Secure Enclave and registered with the server; Play Integrity (standard requests) and App Attest verdicts checked on the server at binding and on sensitive actions.
- Show the borrower every registered device and let them revoke one; notify on each new device through SMS and email (DPS para 68(6) as baseline).
- App unlock by biometric or app PIN after inactivity and at each launch (DPS para 68(8) as baseline). Biometric unlock gates a locally held key; it is not an identity proof for KYC or signing.
- Remote-access tools: detect known screen-sharing and remote-control apps through declared package-visibility queries for a maintained list, never QUERY_ALL_PACKAGES (DPS para 68(2)(iv) as baseline).
- Root, jailbreak, hooking and emulator detection: risk signal to U24 with step-up or block of high-risk actions; never a silent failure.

**Offline, interruption and resume**

- The journey state lives on the server (Temporal workflow). The app caches only the current step and non-sensitive form drafts, encrypted.
- Resume from any device after re-authentication; the web app and the mobile app share progress.
- Every step is idempotent; a retried submission never creates a second application, second consent or second mandate.
- Offline: read-only views of non-sensitive content (support articles, last-known status labelled with time). No KYC, signing, mandate or payment step works offline.

**Deep links**

- Android App Links and iOS Universal Links on a Udofin-controlled domain with `assetlinks.json` and `apple-app-site-association`. No custom URL scheme for sensitive actions.
- Every link lands on an authenticated screen; tokens in links are one-time, short-lived and bound to the user.
- Links from SMS and WhatsApp use the DLT-whitelisted domain [VERIFY: TRAI URL whitelisting rules].

**Sensitive screens**

- Prevent screenshots and screen recording on KYC, offer, KFS, signing, bank-account and payment screens (Android FLAG_SECURE; iOS secure overlay and blur in the app switcher).
- Mask PAN, account numbers and Aadhaar references in all UI.
- Clipboard: disable copy on sensitive fields; clear clipboard after OTP paste.

**Low-end Android and size**

- Reference device: 3 GB RAM, Android 10 or later on a mid-2020 chipset. Expo SDK 57 and 58 support Android 7+ (minSdk 24) and iOS 16.4+ and build with targetSdk 36; set the app's own minimum OS versions in the Phase 0 mobile ADR. Targets in 10.5.
- Android App Bundle with per-ABI splits; Hermes bytecode; image assets in WebP/AVIF; lazy-load non-critical screens; no heavy analytics SDK.
- Network-aware behaviour: compress uploads, resumable document uploads, retry with back-off, clear "slow network" messages.

**Accessibility and language**

- WCAG 2.2 AA equivalent on mobile: screen-reader labels, dynamic type, 44-point touch targets, colour contrast from tokens, no information by colour alone.
- Liveness checks must not depend on blinking or other gestures the borrower may be unable to make (KYC para 27 Explanation; RBC para 105). Provide an assisted or V-CIP alternative.
- English and Hindi at launch; framework for regional languages; KFS and key communications in the borrower's chosen language (RBC paras 10, 29(1)).

## 10.4 Web and PWA engineering

- **Borrower web app** (`apps/borrower-web`): the same journey, rules and copy as the mobile app, rendered by Next.js. It is a DLA in its own right: one CIMS line per RE (CF para 18).
- Browser capabilities: camera via `getUserMedia` at the KYC step with an explicit purpose screen; location via the Geolocation API one-time; WebOTP API for OTP autofill on Chrome for Android, and `autocomplete="one-time-code"` for Safari and other browsers (both need the origin-bound SMS line, 10.3).
- Compensating controls for the web: session binding to a device-bound key (WebAuthn passkey where the browser supports it), adaptive authentication and server-validated CAPTCHA under attack (DPS para 67(1) baseline), DNS and cookie hardening (67(2)), automatic logout after inactivity (67(4)).
- Handoff: steps the web cannot secure to the required level (for example if a partner RE requires app-attested devices for mandate registration) show a QR code or deep link to continue in the app, with progress preserved. Never weaken the control to keep the user on the web.
- **PWA:** installable shell; the service worker caches only static assets and public content. No API response containing personal data is cached by the service worker or stored in IndexedDB or localStorage. Push on the web only after consent; on iOS and iPadOS web push works only for a Home Screen-installed web app (iOS 16.4+) after a user gesture, so it is never the only channel for a regulatory or service notice.
- Public pages (`udofin.com`): product information, partner REs and their DLAs, each RE's website link (CF para 9(5)), grievance contacts (CF para 12(2)), privacy policy (CF para 15), data storage policy (CF para 14(2)), DLG disclosures (CF para 28), the ranking metric for offers (CF para 7(4)) and the checksum or official store links for the app (DPS para 68(5) baseline).
- Security headers: strict CSP with nonces, HSTS preload, frame-ancestors none, Referrer-Policy, Permissions-Policy denying everything not used.
- Portal app: one deployment with operations, lender and admin workspaces on workspace-scoped routes (a sub-domain per workspace is optional); SSO with MFA; no borrower PII in URLs; export controls by permission.

## 10.5 Non-functional targets (initial — confirm in Phase 0)

| Area | Target |
|---|---|
| Scale | 1 million+ registered borrowers in year one; design headroom to 10 million+; 100+ RE tenants; 50,000 concurrent app and web sessions; peaks of 200 application submissions per second during campaigns (validate in Phase 0) |
| Availability (production) | 99.9% monthly for borrower APIs and portals; graceful degradation when an RE connector or provider is down |
| API latency | p95 < 300 ms for reads and < 800 ms for standard writes, excluding third-party calls; provider calls shown with progress and time-outs |
| Journey speed | Start an application in 3–4 interactions (mobile number, OTP, consent, product choice); no step waits on a synchronous provider call longer than 10 seconds without a progress state |
| Mobile app | Cold start < 3 s on the reference low-end Android device; crash-free sessions ≥ 99.5%; ANR rate below Play's bad-behaviour threshold; download size < 30 MB per ABI split |
| Web | Core Web Vitals "good" at p75 on a mid-range Android phone on 4G (LCP < 2.5 s, INP < 200 ms, CLS < 0.1) |
| RPO / RTO | To be agreed per RE in the LSP agreement. Each ML+ RE's ITSC approves an RTO for its critical systems and needs near-zero RPO with a reconciliation method where RPO ≠ 0 (CYB paras 134–136); Udofin's default target is RPO ≤ 5 minutes and RTO ≤ 4 hours, with a tighter tier where an RE requires it (CYB para 138) |
| DR | Geographically separated sites (ap-south-1 / ap-south-2) for production (CYB para 102); Supabase has only one India region (ap-south-1), so while on Supabase the DR copy (PITR backups or a logical replica) runs on self-managed Postgres in AWS ap-south-2, decided in the Phase 0 hosting ADR; half-yearly DR drill for REs whose critical operations depend on Udofin (CYB para 129); quarterly restore tests |
| Backup | Encrypted, immutable backups in India; restore of database, documents and workflow state tested quarterly |
| Log retention | ICT logs 180 days in India (CERT-In Directions 2022); processing logs at least 1 year (DPDP Rule 8(3), from 13 May 2027); longer where an RE contract or law requires [VERIFY each] |
| Security testing | VA every 6 months and PT every 12 months by independent, appropriately trained experts (CYB para 122; CERT-In empanelment is Udofin policy) on production, plus pre- and post-go-live and after major change (CYB paras 121–124); MASVS L2 + R mobile assessment before each major release |
| Incident notice | Notify each affected RE within 2 hours of Udofin's detection (internal target) so it can meet its 6-hour DAKSH filing (OUT para 61; CYB paras 28, 141); Udofin's own CERT-In report within 6 hours |
| Accessibility | WCAG 2.2 AA for web and portals; mobile equivalent |
| Localisation | English + Hindi at launch; INR formatting (lakh/crore); DD-MM-YYYY; IST |

## 10.6 Security and cyber controls

Udofin must meet the controls its REs must ensure for their LSPs and DLAs (CF para 16) and for their IT service providers (OUT Ch IV; CYB). Map each control to a CYB paragraph, a MASVS v2.1.0 control group and a test.

| Area | Control | Mapping |
|---|---|---|
| Governance | Board-approved information security, cybersecurity and BCP policies for Udofin; annual IT risk assessment; ISO 27001 and SOC 2 Type II scoped to OUT para 97(xvii) heads | CYB paras 20–22, 32 (BL ≥ ₹500 crore) and 83–84, 95–96, 98 (ML and above); OUT para 79 |
| Identity and access (staff and RE users) | SSO with MFA for all staff and RE users; MFA for privileged users and critical actions (routing-rule publication, DLG arrangement, credential change, bulk export); PAM with session recording; quarterly access reviews; SoD matrix | CYB paras 113–115; OUT 97(viii) |
| Borrower authentication | OTP + device binding + app unlock; re-authentication on sensitive actions; device list and revocation; lockout after failed attempts with secure reactivation | MASVS-AUTH-1 to 3; DPS paras 49–51, 68(6), 68(8) (baseline) |
| Mobile data storage | No credentials, tokens in plain storage, keys, hashes or hard-coded secrets on the device; Keystore/Keychain only; encrypted local DB; wipe sensitive data on logout; no sensitive data in temp files, logs, backups or keyboard cache | MASVS-STORAGE-1, 2; DPS paras 68(10)–(11), 68(13)(iii) (baseline) |
| Cryptography | TLS 1.2+ (prefer 1.3); AES-256 at rest; field-level encryption for PAN, bank account, DOB; per-RE envelope keys in KMS; RE-controlled keys (BYOK/HYOK) for REs that require them; HSM for signing keys | MASVS-CRYPTO-1, 2; CYB para 118; OUT para 97(vii)(b) |
| Network | Certificate pinning to Udofin's own API domains with a backup pin and a remote kill switch for pin rotation (never pin third-party SDK domains); reject cleartext; stop loading content on TLS errors and show the error | MASVS-NETWORK-1, 2; DPS para 68(13)(iv)–(v) (baseline) |
| Platform interaction | Minimal permissions (10.3); FLAG_SECURE on sensitive screens; WebViews only for Udofin-controlled content with JavaScript bridges disabled; App Links/Universal Links only | MASVS-PLATFORM-1 to 3; DPS para 68(2)(vii) (baseline); CF para 13(1) |
| Code quality and supply chain | SAST, SCA, secret scanning, SBOM per release; signed builds; pinned dependencies; source-code escrow deposit per production release where an RE requires it; vendor certificate of no known vulnerabilities, malware or covert channels per material change | MASVS-CODE-1 to 4; CYB paras 105–106, 125–126 |
| Resilience | Play Integrity and App Attest verdicts verified server-side; root/jailbreak, hooking, emulator and repackaging detection as risk signals; code obfuscation; anti-tamper checks | MASVS-RESILIENCE-1 to 4; DPS para 68(2)(i), 68(2)(ix), 68(4) (baseline) |
| Privacy | Consent per purpose and RE; data minimisation; no third-party trackers that receive personal data; privacy dashboard in the app | MASVS-PRIVACY-1 to 4; CF paras 13–15; DPDP ss.5–6 |
| Aadhaar | Udofin never stores the Aadhaar number or UID token. Prefer OKYC/DigiLocker flows that return masked data; any Aadhaar Data Vault sits with the requesting entity (the RE as KUA or sub-KUA) per UIDAI Circular 14 of 2025, hosted on premises, on a MeitY-empanelled GCC or as ADV-as-a-service, with HSM and reference keys. Udofin tokenises with its own non-reversible reference IDs | Aadhaar Act s.29; UIDAI Circular 14 of 2025; KYC para 23 Explanation 3 |
| Biometrics | Face images used for match and liveness only, passed to the RE-scoped vault or discarded per the RE's instruction; no templates stored by Udofin | CF para 14(3) |
| Secrets | Secrets Manager / Vault; short-lived credentials; per-RE provider credentials stored encrypted under that RE's key; rotation runbook; no secrets in the app bundle, `app.json`, EAS env for client builds, or OTA bundles | OUT 97(viii); MASVS-STORAGE-1 |
| Logging without PII | Structured logs with an allow-list of fields; automatic redaction of PAN, Aadhaar patterns, account numbers, OTPs, tokens; correlation IDs instead of identifiers; mobile crash reports scrubbed on device | Principle 14; CYB paras 109–111 |
| Application security | Zod validation; output encoding; CSRF; rate limiting; IDOR/BOLA tests on every endpoint; webhook signature verification and replay protection; file-upload scanning; WAF and DDoS on every internet endpoint | OWASP ASVS L2; DPS paras 22–23 (baseline) |
| Monitoring and incidents | SIEM-ready audit stream with per-RE feeds to each RE's SOC; anomaly alerts (bulk export, off-hours privileged access, mass status change, credential stuffing); incident runbook with RE notification, DAKSH support and CERT-In templates; NTP-synchronised clocks | OUT paras 61, 97(xi); CYB paras 139–146; CERT-In 2022 |
| Fraud signals | Device, network, velocity, document-tamper and identity-mismatch signals to U24, shared with the RE as signals only | FRM paras 13–23 (RE EWS); FRM 31 |
| Independent security review | Each phase tries to break its own work: cross-RE access, borrower-to-borrower IDOR, privilege escalation, insecure document links, replayed OTP and webhooks, mandate and payment-link tampering, consent bypass, OTA bundle tampering, deep-link hijack, repackaged app | Part 11.6 |

## 10.7 UI/UX and theming

- **Non-cluttered by rule.** One primary action per screen in the borrower journey; progressive disclosure of detail; plain language at reading age 12; no marketing banners inside KYC, offer, KFS, signing or payment steps.
- **Explain why.** Every data request and permission shows the purpose, the RE(s) that will receive the data and the retention period before the OS prompt (CF para 13(3)).
- **Offer comparison.** A neutral, equal-weight card per matching lender with lender name, amount, tenor, APR, monthly repayment obligation, penal charges and KFS link (CF para 7(3)); unmatched lenders listed; the ranking metric shown with a link to its public description (CF para 7(4)). No pre-selected offer, countdown timers, confirm-shaming or visual emphasis on one lender (CCPA Dark Patterns Guidelines, 2023).
- **Transparency features (U25).** A borrower financial dashboard showing every loan sourced through Udofin with its RE as source and as-of time; all charges paid; upcoming dues; documents; consents given and withdrawn; data shared with whom; complaints and their status. An optional personal income and expense tracker based only on data the borrower enters or explicitly shares (no SMS reading).
- **Design tokens.** Colours, typography, spacing, radius, elevation, density, motion and iconography as tokens in `packages/ui-tokens`, compiled to React Native and Tailwind. The project owner can change the look without code changes.
- **Per-RE branding.** Within the Udofin app, RE branding appears only on RE-specific artefacts (offer card logo, KFS, sanction letter, agreements, RE grievance contacts); the shell stays Udofin-branded and neutral. A dedicated white-label app (Appendix B) takes a full theme from U23 and is a separate DLA.
- **Theme guard-rails.** Contrast checks on every theme; regulatory text sizes and placements cannot be changed by a theme; disclosures always render in the default reading style.
- **Portals.** Data-dense without noise: My Queue (SLA-sorted), global search with masked identifiers, application 360° view, saved filters, bulk actions with maker-checker, export by permission, timelines. Every screen has empty, loading, error and permission-denied states. Storybook for all components.
- **Maximum automation.** Pre-fill from consented data pulls; auto-classification of uploaded documents with human verification; automatic status updates from RE events; automatic reminders and escalations; straight-through processing where the RE's rules allow.

## 10.8 Vendor obligations Udofin must meet as a service provider to REs

Udofin is the RE's LSP and service provider. Build these obligations into the product, the LSP agreement and the evidence packs (U18).

**Udofin's status.** Udofin is an LSP (CF para 4(1)(xix)), so the RE's arrangement with Udofin is outsourcing of financial services under OUT Chapter III; OUT para 58(3)(iii) places partnership-based fintech firms providing co-branded applications, products and services under Chapter III. Where Udofin also hosts the lender portal, stores the RE's customer data or runs the RE's integrations, the arrangement also has the features of IT outsourcing (application service provider and cloud services, OUT para 5(1)(iii)–(v)); for ML/UL REs it is likely material (OUT para 58(2)) [interpretation; each RE decides]. **Design every arrangement to meet both Chapter III and Chapter IV.** BL REs apply CYB Ch III/IV instead of OUT Ch IV (OUT para 3(2)); for BL ≥ ₹500 crore, CYB paras 60–64 govern IT outsourcing (CYB para 117 is the ML-and-above vendor-risk rule).

1. **LSP agreement** defining roles, rights and obligations (CF para 6(1)), with the clauses of OUT paras 33–34 and 74(i)–(xix), the DLG terms where applicable (CF para 22), and for BL REs ≥ ₹500 crore the CYB para 62 terms. The standard Udofin LSP agreement and DPA carry all of them, with a clause matrix per RE:
   - activity and service standards (34(i));
   - RE access to books, records, data, logs and alerts (34(ii); 74(ii));
   - continuous monitoring by the RE (34(iii); CYB 62(1));
   - **prior RE consent to any subcontractor** (34(iv));
   - confidentiality and Udofin liability for breaches (34(v));
   - BCP (34(vi));
   - audit rights and copies of audit reports (34(vii));
   - RBI access and inspection of Udofin (34(viii)–(ix); 74(xii));
   - termination and minimum notice (34(x));
   - confidentiality after termination (34(xi)) and preservation of records (34(xii));
   - **retention of administrative audit trails and logs**, accessible on approved request (CYB 62(2)(i)).
2. **Enhanced due diligence pack** for the RE before signing and at renewal: technical capability, data privacy policies and storage systems, fairness in conduct with borrowers, past conduct, ability to comply (CF para 6(2); OUT paras 29–30). Refresh at least annually (OUT para 38).
3. **Periodic conduct review support:** monthly RE dashboard of Udofin's conduct against the agreement (complaints, SLA, data incidents, permission audit, offer-neutrality audit) (CF para 6(3)–(4)).
4. **No core management functions** (OUT para 15; KYC para 13): no Udofin role can sanction a loan, decide KYC compliance, close a complaint or set prices. Pre-filters run only on RE-approved rule versions and are labelled as the RE's.
5. **Ownership and conflicts:** Udofin is not owned or controlled by any director, KMP or approver of the arrangement at a partner RE, or their relatives, unless the RE's Board grants an exception with disclosure (OUT paras 18(vi), 59). Infrabyx group REs: objective selection, arm's length and Board policy (OUT paras 45–51, 90–92).
6. **Data:**
   - minimal storage and RE-scoped vault (CF para 14(1); principle 20);
   - India-only storage and 24-hour repatriation (CF para 14(4); OUT 74(vi));
   - data inventory of what is captured, processed and stored, per RE (OUT 74(vii));
   - permitted-sharing list (74(viii));
   - lifecycle to permanent erasure (97(xvi));
   - NDA with confidentiality surviving termination (74(xix)).
7. **Multi-tenant isolation:** each RE's customer information, documents and records are isolated and identifiable; only RE-authorised personnel access them; Udofin staff use break-glass, need-to-know access, logged and visible to the RE (OUT paras 24, 26–27, 70; 97(vii)(c)).
8. **Keys and access:** RE-controlled keys where required (OUT 97(vii)(b)); IAM with SoD and MFA (97(viii)).
9. **Incidents:** contractual list of material adverse events (OUT 74(iii)); notify the RE without undue delay, target ≤ 2 hours from Udofin's detection, so the RE can report to RBI within 6 hours of Udofin's detection (OUT para 61; CYB paras 28, 141); disclose security breaches (OUT para 25); support forensics and RCA; take part in crisis drills; supply lessons-learned input (CYB paras 140–146; ORM paras 99–101). Udofin also reports to CERT-In itself.
10. **Testing:** independent VA every 6 months and PT every 12 months, pre- and post-implementation and after change, with reports and remediation status shared (CYB paras 121–126).
11. **Source code and certificate:** source-code escrow with an independent agent, every release including fixes, for REs that require it (CYB para 105); a certificate that the application is free of known vulnerabilities, malware and covert channels at onboarding and on each material change, using the agreed materiality definition (CYB para 106).
12. **Maintenance and support** under a formal agreement and SLA (CYB para 104).
13. **SLAs and monitoring:** uptime, availability, performance and incident-response dashboard per RE (OUT paras 74(v), 75).
14. **SOC integration:** log and event export to each RE's SOC (OUT 97(xi)).
15. **BCP and DR:** documented, tested, joint tests with REs; essential personnel clause (OUT paras 40, 74(x), 74(xvii), 83; CYB paras 129–138).
16. **Sub-processors and supply chain:** full list to each RE; RE right to information about supply-chain parties (OUT 74(xi)); Udofin contractually liable for subcontractors (74(xiii); ORM para 76); back-to-back terms with OEMs and cloud providers (74(xviii)); inventory support (82).
17. **Access:** unrestricted and effective access for the RE, its auditors, RBI and competent authorities to data, logs, alerts and premises, including subcontractors (OUT paras 74(ii), 74(xii), 81). Support pooled audits (OUT para 77).
18. **Grievances:** Udofin designates a nodal grievance redressal officer for digital lending complaints (CF para 12(1)), shows contacts on its website and DLA (12(2)), accepts complaints on the DLA (12(3)), and routes every complaint to the RE, whose responsibility it remains; Udofin never closes an RE complaint (CF para 12(3); OUT paras 54–57).
19. **Recovery-agent role (only where appointed):** follow RE guidance and RBC paras 93–101 (CF para 6(5)); collections responsibility exists only under an explicit recovery-agent contract, never because of DLG.
20. **DLA reporting support:** for each RE, the data the RE files on CIMS (Annex-I fields), the CCO certification evidence for CF para 18(4)(i)–(iv), and change notices when a DLA is added, changed or withdrawn (CF para 18(2)). Udofin never markets CIMS inclusion as RBI registration or endorsement (CF para 18(6)).
21. **Exit:** orderly transfer (OUT 74(xv)); full cooperation with the incoming provider (88); no erasure or alteration of data during transition (87); complete export in documented formats (applications, consents, KYC evidence references, documents, audit trail, configuration); secure purge with an independent-assurance certificate (OUT para 42; 97(xvi)).
22. **Continuity:** cooperation in the RE's insolvency or resolution (OUT 74(xvi)); records stay available even if Udofin is wound up (escrow and export).
23. **RBI directions:** comply with RBI directions on the outsourced service through the contract (OUT 74(xiv)).
24. **Fraud accountability:** accept terms holding Udofin accountable where its wilful negligence or malpractice causes a fraud (FRM para 31); respond to a show-cause notice under the RE's fraud process (FRM para 6(1)).
25. **Certifications:** ISO 27001 and SOC 2 Type II with scope covering OUT 97(xvii); the RE may rely on them subject to its risk assessment (OUT para 79).
26. **ORM inputs:** RTO, RPO and service metrics for each RE critical operation that depends on Udofin (ORM para 33); Udofin RCSA; evidence of operational resilience at least equivalent to the RE's (ORM para 73).

---

# PART 11 — WORKING METHOD, GIT DISCIPLINE AND DEFINITION OF DONE

## 11.1 For each module or sub-module

Work through these steps in order (the original 13-step method, extended):

1. Explain the business objective in plain English.
2. Identify assumptions and ask only material unresolved questions.
3. Research the relevant legal, provider, app-store and technical requirements. Update the regulatory register (with REQ-IDs and the [RE] / [UDOFIN] / [RE→UDOFIN contract] tag) and the integration register.
4. Produce the functional specification and acceptance criteria (Given/When/Then), including negative cases, for **each channel** (Android, iOS, borrower web, portal). Save it to `docs/specs/[module].md`.
5. Describe the data model, data owner (RE or Udofin), APIs, events, permissions, state machine and workflows, and the screens with their copy.
6. Identify security, privacy, failure, performance, store-policy and migration risks.
7. **Stop for my approval.**
8. Explain the logic in plain English, then implement only the approved scope in small, reviewable commits.
9. Write and run the tests that apply:
   - unit and property-based (money, APR display, DLG caps);
   - integration and contract (Pact with Finbyx and LMS connectors; provider sandboxes);
   - E2E on web (Playwright) and on real Android and iOS devices (Maestro or Detox);
   - RE-tenant isolation and borrower-to-borrower isolation;
   - security (OWASP ASVS, MASVS);
   - accessibility (automated plus a manual screen-reader pass);
   - permission audit of the built app manifest.
10. Run linting, type checks, build checks (web and EAS preview build), migration validation and security scans.
11. Review the diff for unrelated changes, secrets, PII in logs or analytics, new permissions and security defects.
12. Update the docs: setup, configuration, migration, deployment, store declarations and runbooks.
13. Summarise:
    - what changed;
    - the actual test results;
    - known limitations;
    - mock vs sandbox vs live integrations;
    - next steps.
14. Commit with a meaningful message on the feature branch, open a pull request, and merge only after my approval.

Do not implement large unapproved features or silently expand the scope. Do not claim a test passed unless it was actually run and its result is available.

## 11.2 Financial and consent integrity before financial features

Udofin holds no loan ledger, but it displays money and moves money-related instructions. Do not implement live offer display, KFS display, mandate registration, payment links, loan-mirror balances, DLG calculations or fee accounting until their rules and acceptance tests are approved. Maintain a **golden test-case library** approved by me and our finance and compliance reviewers, including:

- APR display matching the RE's KFS to the paisa (RBC para 29(3) illustration: ₹20,000, 24 months, 15%, ₹400 fees → 17.07%);
- cooling-off exit amount shown as principal plus proportionate APR, from the RE, with any one-time processing fee retained only if disclosed upfront in the KFS (CF para 11(1)–(2));
- DLG cap of 5% of the amount disbursed in the DLG set, the CF para 24 illustrations (Initial, Further, Cases 1–3), invocation by day 120 overdue and no reinstatement (CF paras 24, 25(4), 27);
- household-income microfinance flag at ₹3,00,000 and repayment obligation ≤ 50% of monthly household income for routing to microfinance products (CF paras 51, 55);
- store-policy filters (tenor ≤ 60 days; APR > 36% on iOS);
- Udofin fee accrual and GST on LSP fees invoiced to the RE.

Every release must pass the library.

## 11.3 Git and environment rules

- First inspect the connected repository: current branch, existing files, Git status and available tooling.
- Do not overwrite existing work without understanding its purpose.
- Work on feature branches. **Never push directly to `main`.** Never deploy to production, submit to an app store, rotate live credentials or modify production data without my explicit authorisation.
  - The original Udofin prompt asked for the initial structure to be committed directly to `main`. That is withdrawn: create `feat/repo-baseline` and open a pull request. Enable branch protection on `main` (required reviews, required CI checks, no force-push).
- Never commit API keys, service-role secrets, signing keys, keystores, provisioning profiles, private certificates, production credentials or real borrower data. Use `.env.example` with placeholders. Keep local, test, staging and production configuration separate. Use synthetic test data only; synthetic PAN and Aadhaar-format values must be clearly invalid.
- Only `EXPO_PUBLIC_` and `NEXT_PUBLIC_` variables reach a client bundle, and they hold public configuration only; anything shipped in the app bundle or an OTA update is public. Build-time credentials (for example a source-map upload token) use EAS environment variables with secret visibility and are never read into `app.config` `extra`.
- If repository write access or commit capability is unavailable, provide the exact files and commands. Do not claim to have committed.
- Do not create placeholder business logic that pretends to work. Mark mocks clearly.

## 11.4 Project documents to maintain

- `README.md`
- `CLAUDE.md` (concise, stable; links to detail)
- `docs/00-master-prompt.md` and `docs/01-phase-runbook.md`
- `docs/architecture/` (system context, C4, module map, data ownership RE vs Udofin, fund-flow diagrams)
- `docs/adr/`
- `docs/specs/`
- `docs/products/`
- `docs/data-model/` (ERD, migrations log, RE-scoped vault design)
- `docs/api/` (OpenAPI, AsyncAPI, lender connector contract)
- `docs/integrations/register.md` (provider, contracting party, residency, cost)
- `docs/compliance/requirements-to-controls.md` and `docs/compliance/regulatory-register.md` (dated)
- `docs/compliance/dla-register.md` (one line per DLA per platform per RE)
- `docs/compliance/permission-policy.md` (approved permissions per platform and the purpose text)
- `docs/compliance/store-policy.md` (Google Play and Apple requirements with check dates)
- `docs/security/threat-model.md`, `docs/security/checklist.md`, `docs/security/masvs-matrix.md`
- `docs/testing/strategy.md` and `docs/testing/golden-cases/`
- `docs/ops/` (deployment, rollback, OTA release register, DR, incident runbooks, SLOs)
- `docs/legal/third-party-notices.md`
- `docs/status/modules.md` (module status and outstanding decisions)
- `docs/economics/unit-costs.md`

## 11.5 Definition of done

1. A module is not complete just because its screen renders.
2. It is complete only when all of the following are true:
   - its approved acceptance criteria are met on every channel in scope;
   - the relevant tests (including negative, RE-isolation and borrower-isolation tests) have passed and their output is recorded;
   - authorisation and maker-checker have been checked;
   - failures, retries, time-outs and reconciliation are handled, with honest borrower messages;
   - no new device permission, tracker or data field was added without an approved policy update;
   - consent and audit events are emitted;
   - documentation and registers are updated;
   - the change is reviewable.
3. A mock or sandbox integration is always clearly distinguished from a production integration.
4. Our goal is a secure, maintainable, configurable, regulator-ready and commercially viable LSP platform, not the largest number of features or files.

## 11.6 Additional quality gates

These are the ten "important additions" of the original prompt, extended:

1. **Independent security review** each phase: attempt to break the implementation (10.6 last row).
2. **A single authoritative financial record.** The RE's LMS owns loans, schedules, repayments and classification; Udofin's mirror is labelled and reconciled. Udofin's own ledger (U17) owns Udofin's fees, GST and DLG deposits. Prevent duplicate applications, mandates and payment links; reconcile provider records against internal records rather than trusting an API response.
3. **Borrower consent and data lifecycle:** record what was consented to, why, when, for which RE and purpose, and the exact wording; handle withdrawal, retention, deletion, correction and access logging with legally required exceptions (CF para 13(2); DPDP).
4. **Formal workflow and state rules** with failure states, retries and human overrides; no state is reached on an assumption.
5. **Independent testing and release gates:** a passing build is not evidence that the workflow is correct; tests must exercise the intended behaviour.
6. **Disaster recovery:** tested restore of database, documents, workflow state and queues, and reconciliation with REs after an outage.
7. **Change and migration safety:** no deployment may leave the mobile app (including older supported versions), web, API, workers and database on incompatible versions. Use expand-and-contract migrations and versioned APIs; the oldest supported app version is part of every compatibility test.
8. **Regulatory change management:** dated register; on each change, assess affected products, RE configurations, disclosures, store declarations, workflows, tests and evidence.
9. **Production monitoring:** SLOs for availability, latency, provider failure rates, RE connector lag, queue delays, mandate and payment-status reconciliation, crash-free rate; alerts carry no sensitive data.
10. **Commercial viability:** track per-application costs (KYC, bureau via RE, AA, eSign/eStamp, messaging, cloud, support) against LSP fee revenue per RE and per product. A technically working product may still be commercially unviable.

---

# PART 12 — PHASED ROADMAP WITH CLAUDE CODE INSTRUCTIONS

Build a common platform first, then launch a **narrow MVP pilot** before expanding:

- **MVP scope:** Products 1 (Personal Loan) and 2 (Payday / short-tenure loan); the Android app, the borrower web app, the operations portal and the lender portal; one or two pilot REs — one on Finbyx and one on a generic LMS connector.
  - Product 2 cannot be offered in the store apps where repayment in full falls due in 60 days or less (Google Play and App Store personal-loan rules). It is web-only in that form, or configured with tenor above 60 days for the apps. Decide in Phase 0 (Appendix B).
  - Development and staging use synthetic data only. The pilot goes live only on India-region hosting (Part 10.1).
- **iOS:** App Store submission after the Android pilot is stable (Phase P); release engineering is prepared in Phase 17.
- **Next:** secured products (LAS, Home, LAP, Vehicle), then the proposed templates for Products 11–15 (Phase 18b).
- **Last:** the specialist products, each after a feasibility approval.

How to run the phases:

- Each phase ends with a review gate (the runbook lists the checks).
- Copy one **"Instruction to Claude"** block into Claude Code when you start that phase. Do not paste several phases at once.
- Split large phases into sub-modules.
- Each phase also applies the Part 8A.16 items assigned to it: the module additions in 8A.16.1 and the phase additions in **8A.16.2**. Add them to the phase specification before approval.
- **Phase P (pilot go-live)** comes before the expansion phases (18–21).

| Phase | Primary outcome | Depends on |
|---|---|---|
| 0. Repository audit and architecture | Verified repo facts; architecture and ADRs (mobile/web, loan mirror, data residency, RE-scoped vault); regulatory register v1 with REQ-IDs; DLA register design; permission policy; app-store policy check | — |
| 1. Platform foundation | Monorepo with mobile, borrower web, portal, API and worker skeletons; CI with permission audit; design tokens; observability | 0 |
| 2. Database, tenancy and security | RE-tenant and borrower model, RBAC/ABAC, enforced RLS, audit events, maker-checker, isolation tests | 1 |
| 3. Lender onboarding, product catalogue and configuration | U1 RE onboarding and LSP agreement registry; U2 product catalogue with rule packs and guard-rails; U23 admin | 2 |
| 3b. Communications and consent foundation | U4 consent ledger and notice versions; U16 templates, DLT/WhatsApp/email/push adapters; contact-policy engine | 2 |
| 4. Borrower identity and onboarding (app and web) | U3 registration, OTP, device binding, app unlock, resumable journey shell on Android and web | 2, 3, 3b |
| 5. KYC and verification adapters | U5 PAN, OKYC/DigiLocker, CKYC via RE, V-CIP handoff, face match, bank verification | 4 |
| 6. Credit data, affordability and eligibility | U6 bureau via RE, AA as RE's TSP, income and affordability, household-income test; U7 eligibility pre-filters | 3, 5 |
| 7. Lender routing, offers, KFS and cooling-off | U7 routing; U8 multi-lender offer view, KFS display and acknowledgement, cooling-off | 6 |
| 8. Documents, eSign, eStamp and DMS | U9 templates from RE, signing evidence, stamping, DMS and auto-flow of signed documents | 7 |
| 9. Lender connectors and disbursement orchestration | U21 Finbyx connector and generic LMS connector; U10 disbursement status | 3, 8 |
| 10. Repayments, mandates and reconciliation | U11 eNACH/UPI AutoPay on RE accounts, payment links on RE merchant accounts, status reconciliation | 9 |
| 11. Loan mirror and borrower servicing | U12 loan mirror, statements, service requests; U25 borrower dashboard | 9, 10 |
| 12. Collections and recovery support | U13 reminders and, only where appointed, recovery-agent workflows | 3b, 11 |
| 12b. Recovery support, notices and ADR access | Part 7A (7A.0, UR1–UR6), attachable per RE: overdue, settlement and payment centre; ADR access through Equator without a separate app; RE notices and case visibility; recovery-agent operations only where appointed; data feeds to the RE's recovery suite; conduct and evidence controls | 3b, 9, 11, 12 (UR2 also 14; UR6 export to LawDocsComply or a GRC tool also 16, evidence packs before then; UR4 field-app features also 20) |
| 13. DLG management and lender disclosures | U14 DLG arrangements, caps, invocations, monthly website disclosure | 9, 11 |
| 14. Grievance, AI support and Equator | U15 complaints, nodal GRO, RE routing, AI support, Equator access for RE-referred cases | 3b, 11 |
| 15. Udofin finance, accounting and reporting | U17 Udofin ledger, fee invoicing, GST, DLG accounting, Tally/SAP; U19 reports and lender dashboards | 9, 13 |
| 16. Compliance, audit and security operations | U18 register, evidence, DLA register, RE audit access, LawDocsComply bridge; U24 SecOps and fraud signals | 2, 14 |
| 16b. Ecosystem integration v2 | Ecosystem Integration Specification conformance for every product lifecycle including LAS; new event domains; Equator and other ODR providers; LawDocsComply and third-party GRC connectors with OSCAL export; third-party LOS/LMS certification; module manifests | 9, 12b, 14, 16; Finbyx Phase 16b sandbox (Integration Spec Part 15) |
| 17. Mobile and web release engineering (Play Store, App Store, PWA) | Store declarations, listings, signing, staged rollout, OTA policy, PWA | 4–16 (MVP scope) |
| **P. MVP hardening and pilot go-live** | E2E, independent VAPT and MASVS assessment, DR and incident drills, RE onboarding sign-off, controlled Android and web go-live | 0–17 (12b and 16b only where a pilot RE attaches them) |
| 18. Secured products (LAS, Home, LAP, Vehicle) | Product specs, collateral workflows via the RE, NSDL/CDSL pledge; LAS journey per Part 6.5 | P; for LAS, Finbyx Phase 17 (Integration Spec Part 15) |
| 18b. Additional product templates | Products 11–15 (Gold, Business/MSME, Microfinance, Supply-chain/TReDS invoice finance, Education) per Part 6.4, each after an approved spec and a partner RE | 18, 16b |
| 19. Specialist products (feasibility-gated) | Feasibility notes and approved pilots for Products 7–10 | P, 14 |
| 20. Field app, analytics, AI and marketing expansion | U22 field app (if appointed), U20 governed AI, analytics, consented marketing | P |
| 21. Scale hardening and AWS migration | Scale tests, AWS ap-south-1 / ap-south-2, DR at scale | P, 16b, 18, 18b, 19, 20 |

### Phase 0 — Repository audit and architecture

> **Instruction to Claude:** "Read docs/00-master-prompt.md in full (Parts 1–13, Appendices A–F and Sources). Inspect the connected repository, branch, files, Git status and tooling, and report them. Do not write application code and do not modify the repository yet. Produce:
>
> 1. The architecture proposal: system context showing Udofin, each RE, Finbyx and other LMSs, Equator and LawDocsComply; the modular-monolith module map (U1–U25) with data ownership (RE or Udofin) for every entity; fund-flow diagrams proving no Udofin account sits in any money flow (CF para 10).
> 2. ADRs, after checking the current stable version and licence of each tool:
>    - mobile and web architecture: Expo SDK 57 vs SDK 58 (once stable), New Architecture, EAS Build/Submit/Update, OTA policy, the single portal app with operations, lender and admin workspaces (Appendix C), the borrower web app and PWA scope;
>    - backend: NestJS (11 or 12, per the shared ecosystem ADR with Finbyx), Node 24 LTS;
>    - **Apache Fineract is not needed**: Udofin is not an LMS. Record this and design the **loan mirror** instead: a read model fed by RE events (Finbyx Part 5.2), with source and as-of labels, daily reconciliation and no balance computation;
>    - the **RE-scoped vault** for KYC documents, bureau reports and statements, with per-RE keys and retention, meeting CF para 14(1);
>    - the Aadhaar approach: no Aadhaar number stored by Udofin; OKYC/DigiLocker first; OTP e-KYC only via REs notified under PML Act s.11A; any ADV with the RE (UIDAI Circular 14 of 2025);
>    - V-CIP: run by the RE's officials on the RE's infrastructure (KYC para 27(1)(i)); launched from the app as a web session so the store app never requests precise location.
> 3. A **data-residency check** for every hosting provider and SaaS sub-processor (Supabase, compute host, Temporal, Expo/EAS services, error tracking, analytics, push, email, SMS, WhatsApp, LLM endpoints, providers in Part 9.2). Record which ones may receive personal data; Expo push and EAS Update must carry none.
> 4. The proposed repository structure, using Appendix C.
> 5. The initial entity model, using Appendix D.
> 6. API boundaries and the lender connector contract, reusing the event names of the Infrabyx Ecosystem Integration Specification unchanged (Finbyx Part 5.2 and Udofin Part 5 summarise it).
> 7. **Regulatory register v1:**
>    - load every Part 8A requirement with its REQ-ID (same IDs as Finbyx) and its [RE] / [UDOFIN] / [RE→UDOFIN contract] tag;
>    - confirm every other instrument in Part 8.2 with title, number, date and status;
>    - list every [VERIFY] item with the phase that will resolve it; fully verify now only what Phases 1–5 depend on.
> 8. The **DLA register design**: one line per DLA per platform per RE (Android app, iOS app, borrower web app, any white-label app), with the CF Annex-I fields, GRO contacts, RE website link, store URL and package ID, and the evidence for the CF para 18(4) certification.
> 9. The **permission policy** (`docs/compliance/permission-policy.md`): approved Android permissions and iOS usage descriptions with purpose text, the prohibited list (CF para 13(1); Google Play personal-loan prohibited permissions), and the CI check that enforces it.
> 10. The **app-store policy check**: current Google Play Financial Services and India personal-loan requirements and Apple Guideline 3.2.2(ix), with their impact on Product 2 and on APR display, and the server-side channel filter design.
> 11. The phased roadmap with dependencies and acceptance criteria; the minimum security, testing and code-review gates.
> 12. The list of business decisions you need from me (Appendix B).
> 13. A competitor benchmark of Indian multi-lender LSP apps and DLAs (features, onboarding steps, permissions requested, disclosures, UX), with the gaps Udofin should close.
>
> Present all of this for my approval before modifying the repository."

### Phase 1 — Platform foundation

> **Instruction to Claude:** "On branch `feat/platform-foundation`, initialise the approved monorepo. Set up:
>
> - pnpm + Turborepo, TypeScript strict, ESLint/Prettier;
> - `apps/mobile` (Expo, New Architecture, Expo Router, EAS profiles `development`, `preview`, `production`), `apps/borrower-web` (Next.js 16), `apps/portal` (Next.js 16 with operations, lender and admin workspaces), `apps/api` (NestJS) and `apps/worker` skeletons;
> - `packages/` for contracts (OpenAPI, AsyncAPI, Zod), domain-kernel (Money, Rate, Percentage, IDs, BusinessDate), journey (shared step definitions and validation), ui-tokens, ui-web, ui-native, config, observability and testing;
> - Docker Compose for local Postgres, Temporal and Gotenberg;
> - GitHub Actions CI: lint, typecheck, test, build, secret scan, dependency scan, SBOM, EAS preview build, and a **permission audit** that fails if the built Android manifest or iOS Info.plist contains any permission not in `docs/compliance/permission-policy.md`;
> - `.env.example` files; a check that no secret appears in client bundles;
> - OpenTelemetry with PII redaction, and India-resident error tracking per the Phase 0 ADR; mobile crash reporting with on-device scrubbing;
> - Storybook for web components and a component catalogue for native.
>
> Implement Money, Rate and Percentage on decimal.js (precision ≥ 40) with property-based tests. Build no business features. Open a PR with the test output and the permission-audit output."

### Phase 2 — Database, tenancy and security

> **Instruction to Claude:** "On branch `feat/db-tenancy-security`, design and create the migrations for:
>
> - lender_tenant with re_regulatory_profile (entity type, layer, asset size, s.11A status, CYB chapter, deposit-taking, card issuer), lender_legal_entity, udofin_org;
> - staff_user (Udofin staff and RE users), borrower_account, device_binding, role, permission, role_permission, user_scope (RE, product, workspace);
> - maker_checker_request; audit_event (hash-chained); idempotency_key; outbox_event;
> - the RE-scoped vault tables and storage buckets keyed by RE, with per-RE KMS key references.
>
> Implement:
>
> - server-side authorisation (RBAC + ABAC);
> - Postgres RLS on every RE-scoped and borrower-scoped table, **enforced**: the API connects as a non-owner role without BYPASSRLS; `FORCE ROW LEVEL SECURITY` on every tenant table; RE and borrower context set with `set_config(…, true)` inside each transaction;
> - the auth abstraction over Supabase Auth: borrower OTP sessions with device-bound refresh, staff and RE SSO with mandatory MFA;
> - the maker-checker framework;
> - break-glass access for Udofin staff to RE data, logged and visible to the RE (OUT paras 24, 70);
> - Supabase Data API (PostgREST, GraphQL) disabled, or application schemas unexposed with all privileges revoked from `anon` and `authenticated`; Storage RE-vault buckets private with no client policies; clients reach data only through the NestJS API.
>
> Write isolation tests that try to read and write across REs, across borrowers and from a lender user into another RE's data, and prove they fail. Include a test proving that a query without context returns zero rows, and that a borrower JWT calling the Supabase Data API or Storage directly gets no data. Report results."

### Phase 3 — Lender onboarding, product catalogue and configuration

> **Instruction to Claude:** "On branch `feat/lender-onboarding-catalogue`, build:
>
> - **U1:** RE onboarding with the regulatory profile; the LSP agreement registry with effective dates, scope (sourcing, servicing, recovery agent yes/no, DLG yes/no), clause matrix against OUT paras 34 and 74 and CF para 6(1), the due-diligence pack (CF para 6(2)), ownership and conflict declaration (OUT paras 18(vi), 59), and the RE's grievance contacts, website link and data-storage policy (CF paras 9(4)–(5), 12(2), 14(2));
> - **U2:** the product catalogue per RE, either received from the RE's LMS (`ProductCatalogPublished`, through the U21 connector port with a contract-faithful mock until Phase 9) or configured in the lender portal for REs without an LMS connector: amount and tenor ranges, pricing grids, charges, cooling-off days (≥ 1, CF para 11(1)), KFS template version, eligibility pre-filter rules (GoRules), required documents, mandate and payment providers;
> - **platform guard-rails** that an RE cannot loosen: no fund flow through Udofin (CF para 10), cooling-off ≥ 1 day, KFS validity ≥ 3 working days or 1 for tenor < 7 days (RBC para 29(2)), contact windows (RBC para 100), store-policy channel filters (tenor ≤ 60 days blocked on store apps; APR > 36% blocked on iOS), microfinance flag for household income ≤ ₹3 lakh (CF para 51);
> - classification of every configuration item into the five layers of Part 3.4 (standard core, tenant-safe, platform-approved, legal-review, controlled extensions), with maker-checker and effective dating;
> - **U23** admin for feature flags, roles and integration credentials (stored per RE, encrypted under the RE's key).
>
> Produce `docs/products/_template.md` and the Personal Loan and Payday product specs for my approval. Tests: guard-rail rejection tests for every rule above; maker-checker tests; isolation tests for the lender workspace."

### Phase 3b — Communications and consent foundation

> **Instruction to Claude:** "On branch `feat/communications-consent`, build:
>
> - **U4 consent ledger:** consent records with purpose, data categories, recipient RE(s), notice version and language, channel, timestamp, device, withdrawal and expiry; notice versioning with legal approval; purpose disclosure at each stage (CF para 13(1)–(4)); a privacy centre API for the app and web (view, withdraw, restrict sharing, request deletion, CF para 13(2)); retention rules engine with legal-basis exceptions (PMLA, RBI, CIC); DPDP rights workflow with a 90-day clock (DPDP Rule 14(3) from 13 May 2027) and a consent-manager integration point (Rule 4 from 13 Nov 2026) [VERIFY: Gazette text];
> - **U16 communications:** versioned, multilingual templates with approval; SMS adapter with DLT entity, header and template IDs (sending on the RE's header where the message is the RE's); WhatsApp Business adapter restricted to categories the WhatsApp Business Messaging Policy allows (no payday-loan promotion, no debt collection); email; push via FCM/APNs with no personal data in payloads; voice/IVR adapter on 1600-series numbers for service calls [VERIFY: TRAI direction];
> - **contact-policy engine:** effective-dated windows and frequency limits, separate service, marketing and recovery categories; recovery calls only 08:00–19:00 (RBC para 100), and only 09:00–18:00 with no persistent calling for microfinance loans, to which para 100 does not apply (RBC para 91(2)); a second effective-dated pack for the RBC Third Amendment from 1 Jan 2027 (para 100Y(4): borrower-requested times honoured; sensitive occasions avoided) [VERIFY: official text not supplied]; TCCCPR consent categories and opt-out cooling periods; DND checks.
>
> Every later phase must send messages only through U16 and record consent only through U4. Tests: consent replay and withdrawal; template without DLT ID rejected; recovery message outside window blocked; push payload PII scan."

### Phase 4 — Borrower identity and onboarding (app and web)

> **Instruction to Claude:** "On branch `feat/borrower-identity`, build U3 on Android (Expo) and the borrower web app:
>
> - registration and login by mobile OTP (SMS Retriever / WebOTP autofill; no SMS permission), sent through the U16 DLT-registered SMS adapter (Supabase Auth Send SMS hook or the auth abstraction), never Supabase's built-in SMS providers; rate limits and lockout;
> - device binding with a hardware-backed key, Play Integrity standard request and App Attest verification on the server; device list and revocation; new-device notification;
> - app unlock with biometric or app PIN after inactivity and at launch;
> - the resumable journey shell: server-side Temporal workflow per application; the same step definitions on app and web; resume on another device after re-authentication;
> - consent screens from U4 at the first step; purpose screens before each OS permission prompt;
> - FLAG_SECURE and app-switcher blur on sensitive screens; version check against the minimum supported version with a forced-upgrade screen;
> - web: WebAuthn passkey binding where available, CAPTCHA with server validation under attack, inactivity logout; QR/deep-link handoff to the app;
> - accessibility (screen reader, dynamic type, contrast) and English/Hindi copy.
>
> Target: an application starts in 3–4 interactions (mobile number, OTP, consent, product). Tests: E2E on a real low-end Android device and on Chromium mobile emulation; replayed OTP and session-fixation tests; deep-link hijack test; permission audit showing no new permission; cold-start measurement against Part 10.5."

### Phase 5 — KYC and verification adapters

> **Instruction to Claude:** "On branch `feat/kyc-verification`, build U5 with mock adapters first, then Surepass and other sandboxes behind `KycProvider`:
>
> - PAN verification and PAN–Aadhaar link status;
> - Aadhaar offline verification (OKYC XML or secure QR) and DigiLocker issued documents with digital-signature verification (KYC para 23 proviso (ii)–(iii)); Aadhaar number redaction (Explanation 1); no Aadhaar number or UID token stored by Udofin;
> - Aadhaar OTP e-KYC only for REs whose profile shows s.11A notification, via the RE's KUA/sub-KUA, with specific OTP consent and the para 25 limits passed to the RE (term loans only, ₹60,000 a year, one-year validity unless full CDD) (KYC para 25);
> - CKYC search and download with the borrower's explicit consent using the RE's credentials (KYC para 23(4));
> - V-CIP handoff: launch the RE's V-CIP session (web) with a signed context; receive only the outcome and evidence reference (KYC paras 26–27);
> - selfie liveness and face match with accessible alternatives (RBC para 105); scores only, no biometric storage (CF para 14(3));
> - bank account verification (penny-drop/pennyless) with name match; the account must be the borrower's (CF para 10(1));
> - KYC evidence packages written to the RE-scoped vault and sent to the RE as evidence; the KYC decision field is writable only by the RE (KYC para 13).
>
> Load the KYC REQ-IDs from Part 8A.3 into the register. Tests: s.11A gate; para 25 limit propagation; no Aadhaar number in DB, logs or analytics (automated scan); RE-only KYC decision; provider time-out and retry without duplicate calls."

### Phase 6 — Credit data, affordability and eligibility

> **Instruction to Claude:** "On branch `feat/credit-affordability-eligibility`, build U6 and the U7 eligibility pre-filter:
>
> - bureau pulls through `BureauGateway` under the RE's CIC membership, with consent naming the RE and purpose; no Udofin-owned bureau account (CIR para 6) [VERIFY: CIC and Surepass contract terms];
> - borrower-initiated own-report import as an alternative path, clearly labelled;
> - Account Aggregator flows with the RE as FIU and Udofin as technology service provider; consent artefact per RE; data used only as the artefact allows (AA para 28);
> - income, employment and bank-statement analysis adapters; economic profile capture of age, occupation and income for the RE's record (CF para 8(1));
> - household income capture and the microfinance flag (≤ ₹3 lakh; CF para 51) with repayment obligations ≤ 50% of monthly household income for routing to microfinance products (CF para 55);
> - the eligibility pre-filter: RE-approved GoRules versions only; first-time borrowers never excluded for lack of credit history (CIR para 38(5)); DLG cover never an input (CF para 20(2)); every pre-filter outcome stores inputs, rule version and RE attribution; the credit decision is always the RE's.
>
> Tests: consent required before any pull; per-RE data isolation of bureau data; rule-version replay; new-to-credit test; microfinance-flag golden cases."

### Phase 7 — Lender routing, offers, KFS and cooling-off

> **Instruction to Claude:** "On branch `feat/routing-offers-kfs`, build U7 routing and U8:
>
> - routing to every RE whose pre-filter matches, using the documented matching mechanism, versioned and applied consistently to similarly placed borrowers (CF para 7(2));
> - `EligibilityCheck` and `ApplicationSubmitted` to each RE (Finbyx Part 5.2), with only the data the borrower consented to share with that RE, through the U21 `LenderConnector` port against a contract-faithful mock until the Finbyx and generic connectors are built in Phase 9; handle `AdditionalInfoRequested`, `ApplicationStatusChanged`, `DecisionMade`, `KFSIssued` and `SanctionLetterIssued`, and send `BorrowerAccepted` within KFS validity;
> - the multi-lender offer view: lender name, amount, tenor, APR, monthly repayment obligation, penal charges and KFS link per offer; unmatched lenders named; ranking only by a publicly pre-disclosed metric; no dark patterns (CF para 7(1)–(4); CCPA Dark Patterns Guidelines, 2023);
> - channel filters from Phase 3 (store-policy limits) applied server-side and recorded;
> - KFS display exactly as issued by the RE (`KFSIssued`): proposal number, validity period, APR computation sheet and repayment schedule (RBC para 29(1)–(3)); borrower acknowledgement captured; KFS in the borrower's language;
> - the cooling-off period from the RE product and the exit request (`CoolingOffExitRequested`) with the RE-computed exit amount (CF para 11);
> - no automatic credit-limit increase without an explicit borrower request (CF para 8(2)).
>
> Tests: APR golden test 17.07% displayed (RBC para 29(3)); offer-neutrality test (same inputs, same order, no lender emphasis); unmatched-lender disclosure; KFS expiry blocks acceptance after the validity period; store-filter tests per channel; E2E from application to accepted offer on Android and web."

### Phase 8 — Documents, eSign, eStamp and DMS

> **Instruction to Claude:** "On branch `feat/documents-esign-dms`, build U9:
>
> - document generation from RE-owned templates on the RE's letterhead (KFS, sanction letter, agreement, summary of product, privacy policies);
> - eSign adapters storing provider transaction ID, certificate, signer details and document hash (`ESignCompleted`), never a bare flag; eStamp adapters with state, duty and certificate (`EStampCompleted`);
> - the physical-execution path for instruments excluded by the IT Act First Schedule;
> - the DMS with versions, hashes, retention per RE policy, access logs and signed short-lived URLs; the borrower sees every signed document in the app and web;
> - **automatic flow** of the digitally signed KFS, product summary, sanction letter, terms and conditions and privacy policies to the borrower's verified email or SMS on execution (CF para 9(3)).
>
> Tests: tampered document hash detected; signature evidence linked to the accepted KFS version; no document reachable without authorisation (IDOR tests on URLs); auto-flow sent once and only to the verified contact."

### Phase 9 — Lender connectors and disbursement orchestration

> **Instruction to Claude:** "On branch `feat/lender-connectors-disbursement`, build U21 and U10:
>
> - the Finbyx connector implementing the Ecosystem Integration Specification exactly (same event names as Finbyx Part 5.2), with mTLS, JWS-signed messages, idempotency and replay protection; Pact contract tests against Finbyx;
> - the generic LMS connector framework (REST/webhook and SFTP file adapters), a mapping layer per RE, and a connector certification suite;
> - disbursement orchestration as **status only**: Udofin sends the accepted, signed package; the RE disburses directly to the borrower's verified account; Udofin moves the application to disbursed only on `LoanDisbursed` with UTR (CF para 10(1)); `DisbursementFailed` handling with borrower messaging;
> - start of the cooling-off clock on the trigger set in the RE's product (default the RE's `LoanDisbursed` event; CF para 11 leaves it to the RE's credit policy, 8A.16.3);
> - lender portal queues for REs without an LMS connector: decision capture by RE users only, with maker-checker.
>
> Tests: no configuration can name a Udofin account as payee (guard-rail test); duplicate event idempotency; connector outage queues and recovers; reconciliation report between Udofin application states and RE events."

### Phase 10 — Repayments, mandates and reconciliation

> **Instruction to Claude:** "On branch `feat/repayments-mandates-recon`, build U11:
>
> - eNACH and UPI AutoPay mandate registration on the RE's corporate utility code or merchant account, with limits and UMRN sent to the LMS (`MandateRegistered`); no fresh PDCs or EMI cheques where NACH is available (MISC para 23);
> - payment links and UPI intent on the RE's merchant account only; Udofin never holds a merchant account, escrow or virtual account for repayments (CF para 10(2)–(3));
> - payment status from the gateway reconciled against the RE's `PaymentReceived` and `PaymentBounced` events; a gateway success alone never marks a due as paid;
> - receipts issued by the RE shown in the app;
> - co-lending: repayment to the co-lending escrow controlled only by the co-lenders (CF para 10(1) Note);
> - Stripe and PayPal: no adapter for domestic repayments; record the ADR.
>
> Tests: payee-account guard-rail; duplicate payment-link prevention; three-way status reconciliation (gateway, RE event, mirror) with aged exceptions; mandate amount cannot exceed the RE-approved limit."

### Phase 11 — Loan mirror and borrower servicing

> **Instruction to Claude:** "On branch `feat/loan-mirror-servicing`, build U12 and U25:
>
> - the loan mirror fed by `ScheduleIssued`, `ScheduleChanged`, `PaymentReceived`, `PaymentBounced`, `DPDChanged`, `AssetClassificationChanged`, `LoanClosed` and `NOCIssued`; every figure labelled with the RE as source and the as-of time; daily reconciliation with the RE's `DailyReconciliationFile`; no balance computed by Udofin;
> - revised schedules shown on each part-disbursement as sent by the RE (MSD para 7(3));
> - service requests (statement, foreclosure quote, NOC, profile change) routed to the RE with SLA tracking;
> - U25 borrower dashboard: all loans, charges, dues, documents, consents and data-sharing history, complaints; optional personal expense tracker using only data the borrower enters.
>
> Tests: mirror never shows a value without source and as-of; reconciliation break raises an exception; service request reaches the right RE only; dashboard isolation between borrowers."

### Phase 12 — Collections and recovery support

> **Instruction to Claude:** "On branch `feat/collections-support`, build U13 in two separate capabilities:
>
> 1. **Reminders for all REs** (servicing under the LSP agreement): due-date reminders and payment links through U16 within the contact policy; no WhatsApp for debt collection.
> 2. **Recovery-agent workflows only for REs that appointed Udofin by an explicit recovery-agent contract** recorded in U1 (never inferred from DLG): `CollectionAllocated` and `CollectionDeallocated`; recovery-agent particulars sent to the borrower by email or SMS before first contact (CF para 9(6); RBC para 95); notice and authorisation letter (RBC paras 95–96); agent register with police verification and training (RBC paras 94, 98–99); calling window 08:00–19:00 and no harassment (RBC para 100), or 09:00–18:00, no persistent calling and recovery at the designated place unless the borrower fails to appear twice in succession for microfinance loans (RBC paras 90–91; para 100 excludes them); calls from the RE's 1600-series numbers [VERIFY]; `CollectionActivityLogged`, `PTPCaptured`, `FieldVisitLogged`, `ReceiptIssued`; cash recoveries reflected in the borrower's account the same day and no Udofin fee deducted from proceeds (CF para 10(5)).
>
> Build the RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026; paras 100A–100AB in force 1 Jan 2027) as a second effective-dated rule pack, as summarised in Part 7A.0.1 [VERIFY: official text not supplied; confirm paragraph numbers before release]. Phase 12b extends this phase with Part 7A. Tests: recovery workflow unavailable without an active contract; contact outside window blocked; particulars notice precedes first contact; DLG arrangement alone grants no collection rights."

### Phase 12b — Recovery support, notices and ADR access

> **Instruction to Claude:** "On branch `feat/recovery-support`, build Part 7A (7A.0, UR1–UR6) as the attachable module pack `modules/ur-recovery-support/` with its `module.yaml` manifest:
>
> - **7A.0:** entitlement check (the RE's licence SKU, the LSP agreement scope and the flag `mod.udofin-recovery.[capability]`, all server-side); lifecycle from `AVAILABLE` to `DETACHED` with `ModuleAttached` and `ModuleDetached`; read-only detach with an RE export pack; the retention schedule and legal holds; rule pack A (RBC paras 90–100, to 31 Dec 2026) and rule pack B (RBC Third Amendment Directions, 2026, RBI/2026-27/230, paras 100A–100AB, from 1 Jan 2027) as effective-dated versions, plus state overlays [VERIFY: official text not supplied; confirm paragraph numbers before release];
> - **UR1:** overdue view, RE payment options, PTP, hardship requests, settlement requests (`SettlementRequested`), RE offers shown verbatim with the characterisation block (RSA paras 89–90, 95, 97–98, 100; CIR para 12(4)) and acceptance evidence; no Udofin role can approve, price or promise a settlement (RSA para 16(5); OUT para 15);
> - **UR2 (after Phase 14):** ADR case view from the ADR events, signed link into Equator's web flow with no separate app, a basis check on every referral, and no referral scope for Udofin credentials (*CORE v ECI-SPIC-SMO-MCML (JV)*, SC, 8 Nov 2024; *L&T Finance v Jai Paras Material Store*, Cal HC, 14 May 2026);
> - **UR3:** RE notice inbox with hash checks, Udofin-channel delivery evidence (`NoticeServiceUpdated`), the RE's visibility policy (off by default), no "served" state and no WhatsApp;
> - **UR4:** recovery-agent operations only for REs with an explicit recovery-agent contract: contract, agent-eligibility, notice-before-contact (CF para 9(6)) and `canContact` gates; call recording; same-day cash posting (CF para 10(5)); agency list feed (RBC para 97);
> - **UR5:** data feeds to the RE's recovery suite with daily reconciliation;
> - **UR6:** controls UR6-C01 to C16 with evidence to LawDocsComply or the RE's GRC tool.
>
> Present the specification of each UR module for my approval before code. Tests: every test listed under UR1–UR6, plus: Udofin client credentials cannot create an ADR referral or a settlement approval; attaching UR4 for an RE without a recovery-agent contract fails; detach makes every UR screen read-only and produces a verified export; no recovery template can select WhatsApp."

### Phase 13 — DLG management and lender disclosures

> **Instruction to Claude:** "On branch `feat/dlg-management`, build U14 (Udofin as DLG provider):
>
> - eligibility check: Udofin incorporated under the Companies Act, 2013 (CF para 19); DLG policy inputs for the RE (CF para 20(1));
> - arrangements per RE with the explicit contract terms (extent, form, invocation timeline, disclosure; CF para 22), form as cash with the RE, FD with lien or bank guarantee (CF para 23), and the fixed DLG set (CF para 24(2));
> - cap engine: total cover ≤ 5% of the amount disbursed out of the DLG set, activated proportionately on disbursement (CF para 24(3), Illustration 1), with the CF para 24(3) illustrations as golden tests;
> - invocation register: invocation within 120 days overdue (CF para 27(1)); no set-off against borrower liability (25(2)); recovery sharing per contract (25(3)); **no reinstatement** (25(4)); DLG term ≥ longest loan tenor (27(2)); no DLG on loans under trust-fund guarantee schemes (CF para 21(1)) or for P2P;
> - the statutory-auditor-certified declaration (aggregate DLG outstanding, number of lenders, portfolios, past default rates) at each entry or renewal (CF para 20(3));
> - monthly website disclosure of the number of portfolios and amount of each on which DLG is offered, published within 7 working days of month-end (CF para 28);
> - `DLGArrangementRegistered`, `DLGInvocationRaised`, `DLGInvocationSettled`, `DLGPortfolioCoverage` with each RE; `DLGDisclosurePublished` to each RE and LawDocsComply (CF para 28); `DLGRecoveryShared` consumed into the recovery-share ledger (CF para 25(3)); data for the RE's ECL (IRACP paras 36A–36C) and capital treatment (CF para 26).
>
> DLG never feeds credit pre-filters (CF para 20(2)) and never creates collection rights. Tests: all CF para 24(3) cases; 121-day invocation rejected; reinstatement attempt rejected; disclosure job meets the 7-working-day deadline."

### Phase 14 — Grievance, AI support and Equator

> **Instruction to Claude:** "On branch `feat/grievance-ai-equator`, build U15:
>
> - complaint lodging in the app and on the web (CF para 12(3)); unique reference; acknowledgement; Udofin nodal GRO details displayed on the DLA and website and RE GRO details in the KFS (CF para 12(1)–(2));
> - routing every complaint to the responsible RE (`GrievanceRaised`, `GrievanceUpdated`, `GrievanceEscalated`); grievance redressal remains with the RE; Udofin never closes an RE complaint (CF para 12(3); OUT para 56);
> - the 30-day clock and escalation information to RBI CMS (https://cms.rbi.org.in) and the CRPC address when the RE rejects, partly rejects or does not reply within 30 days (CF para 12(4)); Internal Ombudsman and RB-IOS 2026 steps [VERIFY: texts not supplied];
> - AI support assistant answering only from approved sources (RE product documents, KFS, FAQs, case status), with citations, hand-off to a human and no invented rights or outcomes; it never rejects or closes a complaint; build now the minimum U20 controls it needs (model-inventory entry, approved-source retrieval, prompt redaction, India-region or RE-approved endpoint per CF para 14(4)), which Phase 20 extends;
> - Equator access only for cases the RE has referred (Udofin never refers), after the RE's process or under a pre-named institution clause or written post-dispute consent; a signed link into Equator's web flow from the app, no separate app; outcome status flows back (full specification in Part 7A UR2, built in Phase 12b);
> - feedback (CSAT/NPS) through U16.
>
> Tests: complaint cannot be closed by any Udofin role; 30-day escalation message triggers; AI refuses out-of-scope questions; Udofin credentials cannot create an ADR referral, and Equator access appears only for RE-referred cases with a recorded basis."

### Phase 15 — Udofin finance, accounting and reporting

> **Instruction to Claude:** "On branch `feat/udofin-finance`, build U17 and U19:
>
> - Udofin's own double-entry ledger (append-only, balanced, reversal-only corrections, period locks) for LSP fee income, GST on fees invoiced to REs, DLG deposits, FDs and bank guarantees, invocations and recoveries shared, collection-agent fees (where appointed) and vendor costs;
> - fee computation from RE agreements; invoices to REs only; a test proving no fee line can be charged to a borrower (CF para 10(4));
> - Tally Prime (JSON/XML connector), SAP and CSV exports with reconciliation;
> - U19 reports: per-RE funnel, conversion, TAT, complaints, DLG positions, sourcing data for the RE's returns (SR) with lineage, unit economics per application; lender dashboards with row-level security.
>
> Our CA reviewer approves the golden accounting cases. Tests: trial balance balances under randomised postings; RE dashboard isolation; export reconciles to the ledger."

### Phase 16 — Compliance, audit and security operations

> **Instruction to Claude:** "On branch `feat/compliance-secops`, build U18 and U24:
>
> - the regulatory register with REQ-IDs, owners, controls, control tests and evidence; dated change log;
> - the DLA register and CIMS data pack per RE (CF para 18, Annex-I) with change notices and CCO-certification evidence for CF para 18(4)(i)–(iv);
> - RE, auditor and RBI read-only, time-boxed access to that RE's data, logs and evidence (OUT paras 34, 74(ii), 81; CYB para 62(2));
> - vendor assurance pack generation (10.8);
> - the LawDocsComply bridge (register, evidence and DLA feed);
> - U24: SIEM feed per RE, anomaly rules, incident runbook with RE notification target ≤ 2 hours and CERT-In 6-hour reporting, fraud and device-risk signals to REs (FRM paras 13–23 as RE inputs), app-integrity verdict monitoring.
>
> Tests: an incident drill measuring Udofin detection → RE notification time; auditor role cannot see another RE; every REQ-ID has an owner and a control test."

### Phase 16b — Ecosystem integration v2

> **Instruction to Claude:** "On branch `feat/ecosystem-integration-v2`, bring every Udofin connector to the Infrabyx Ecosystem Integration Specification v1.0 (`docs/ecosystem/infrabyx-integration-spec.md`):
>
> - contracts: CloudEvents 1.0 envelope with the specification's type and source conventions and the extensions `tenantid`, `reid`, `productfamily`, `correlationid`, `causationid`, `consentref` or `legalbasis`, `dataclass`, `schemaver`, `seq` and `traceparent` (Integration Spec 3.2); AsyncAPI 3.0 and OpenAPI 3.1; JSON Schema 2020-12 registry with backward-compatibility checks and 90-day dual publication of any breaking `vN`; Pact tests in both pipelines;
> - security: mTLS everywhere; RFC 9421 HTTP Message Signatures, with a detached JWS for documents and regulated messages; OAuth 2.1 client credentials bound by mTLS; FAPI 2.0 where an API acts for the borrower; Standard Webhooks for external webhooks; `Idempotency-Key` on every POST; outbox, inbox and dead-letter queue;
> - every product lifecycle (Products 1–15, Part 6.4), including the LAS collateral events (Part 6.5), the co-lending and transfer events, the recovery, ADR and litigation views (Part 7A) and the six events adopted in v1.1 (Part 5.2);
> - Equator and other ODR providers through one `OdrProvider` contract, with CSV or SFTP where a provider has no API;
> - LawDocsComply and third-party GRC tools (MetricStream, IBM OpenPages, ServiceNow IRM, Archer) through the generic GRC contract with OSCAL export (U18);
> - third-party LOS/LMS connectors certified per RE with the same suite; notice-dispatch adapters for RE-issued notices; court-data views only as RE-permitted projections;
> - module manifests for every attachable module, and a connector certification suite that emits `ConnectorCertified` and stores the report as evidence.
>
> Never rename a canonical event; raise any gap as a versioned contract change in every affected repository. Tests: contract conformance for every event and API; signature, replay and idempotency rejection; payloads without a consent reference or statutory-basis flag rejected (CF para 13(4)); registry rejects a breaking change without a new version; tenant-isolation and India-residency checks; a certification report per connector."

### Phase 17 — Mobile and web release engineering (Play Store, App Store, PWA)

> **Instruction to Claude:** "On branch `feat/release-engineering`, prepare the releases in this order: **Google Play first, then the App Store, plus the PWA.**
>
> **Google Play:**
>
> - confirm that each pilot RE has reported the Udofin Android app on CIMS and that it appears on RBI's public list of DLAs deployed by REs before submission (CF para 18; Google Play India personal-loan requirement);
> - Financial features declaration as a platform that facilitates loans by registered NBFCs or banks; names of all partner NBFCs and banks prominently in the description;
> - listing metadata: minimum and maximum repayment period, maximum APR and a representative total-cost example; privacy policy URL; app category Finance;
> - Data safety form matching the actual data flows and the permission policy; no prohibited permission in the merged manifest;
> - Play App Signing; internal → closed → production staged rollout; Play Integrity configured;
> - target API level 36 (Android 16) or higher, required for every new app and update since 31 Aug 2026 (extension to 1 Nov 2026 only on request), and 16 KB memory-page-size support for every native library (required since 1 Nov 2025 for apps targeting Android 15+); CI fails a release build that misses either.
>
> **App Store:**
>
> - submission by Udofin as a legal entity (Guideline 5.1.1(ix));
> - maximum equivalent APR and payment due date disclosed; no offer above 36% APR and no loan repayable in full in 60 days or less in the iOS channel (Guideline 3.2.2(ix)); App Privacy labels matching flows; App Attest configured; separate CIMS line for the iOS app;
> - TestFlight → phased release.
>
> **OTA and versions:** EAS Update code signing, runtime-version policy, staged rollout with crash-rate rollback, release register; minimum supported version and six-month sunset (DPS para 68(2)(iii) baseline).
>
> **PWA:** manifest, service worker for static assets only, install prompts, Lighthouse and Core Web Vitals checks.
>
> Produce `docs/compliance/store-policy.md` with every requirement, its source URL, check date and evidence. Do not submit to any store without my explicit authorisation."

### Phase P — MVP hardening and pilot go-live

> **Instruction to Claude:** "On branch `release/pilot`, for Products 1–2, the Android app, the borrower web app, the operations and lender portals, and the pilot REs, deliver:
>
> - full E2E regression on real devices and browsers, including resume, outage and retry scenarios;
> - independent VA and PT on production by a CERT-In-empanelled firm (Udofin policy; CYB para 122 requires independent, trained experts), CVSS-scored, all Critical/High findings closed and re-tested (CYB paras 121–126), plus a MASVS L2 + R assessment of the release build;
> - source-code escrow deposit (where a pilot RE requires it) and the vendor security certificate for the release (CYB paras 105–106);
> - load test at the Part 10.5 targets;
> - DR switchover drill and restore of database, documents and workflow state, with post-drill reconciliation with each RE;
> - an incident drill proving RE notification fits a 6-hour DAKSH filing measured from Udofin's detection (OUT para 61; CYB paras 28, 141) and Udofin's CERT-In report;
> - a data-residency check of every environment and sub-processor;
> - each pilot RE's sign-off: LSP agreement clause matrix, due-diligence pack, DLA on CIMS and on RBI's public list, grievance contacts, website links, product approval;
> - an exit drill: full export for an RE, re-import test and purge certificate;
> - production runbook and a controlled go-live checklist for my approval.
>
> Do not deploy to production or publish to any store without my explicit authorisation."

### Phase 18 — Secured products (LAS, Home, LAP, Vehicle)

> **Instruction to Claude:** "On branch `feat/secured-products`, for each secured product:
>
> 1. produce the product spec and feasibility note with the RE's collateral policy;
> 2. build the collateral workflows as RE-owned steps orchestrated by Udofin: securities pledge via NSDL/CDSL and mutual-fund lien in favour of the RE; property and vehicle data, valuer and legal-vendor hand-offs; document collection; release-of-security status from the RE;
> 3. apply the product's RE rules received through the catalogue (for example LAS LTV and cure periods set by the RE under CF Ch VIII; the LAS journey follows Part 6.5) and never compute collateral decisions in Udofin.
>
> Tests: pledge always names the RE as pledgee; collateral status changes only on RE or depository events."

### Phase 18b — Additional product templates

> **Instruction to Claude:** "For Products 11–15 (Gold, Business/MSME, Microfinance, Supply-chain/TReDS invoice finance, Education; Parts 6.2 and 6.4), on branch `feat/product-templates-18b`, build each product only after I approve its specification and a partner RE confirms it:
>
> 1. write `docs/products/[code].md` from the 6.3 checklist and the 6.4 table, with the RE's policy references and the Finbyx R16 playbook code;
> 2. build the template on the common engine with its events, documents and disbursement routing;
> 3. apply each product's hard rules:
>    - gold: collateral handled and stored only in RE branches by RE employees, so leads and branch appointments only (RBC paras 53–54); valuation and LTV shown only from RE data (CF paras 40, 43–44);
>    - microfinance: household-income test and 50% cap (CF paras 51–57); loan card and no prepayment charge (RBC paras 78–81);
>    - business/MSME: entity KYC, DIN or PAN of directors and guarantors (WD para 19(1)) and the CGTMSE flag (CF para 21(1));
>    - supply chain: TReDS only as a referral with the RE as registered financier [VERIFY: TReDS Directions, 2026];
>    - education: institution as end-beneficiary (CF para 10(1)).
>
> Tests: golden journeys per product on app and web; the gold journey has no collateral-handling step in Udofin; the microfinance flag is set on every collateral-free MSME or education loan within the income threshold; the disbursement guard rejects any beneficiary not permitted by CF para 10(1)."

### Phase 19 — Specialist products (feasibility-gated)

> **Instruction to Claude:** "For Products 7–10 (resolution finance, medical and insurance-premium finance, legal-expense and award-enforcement finance, debt reset), do not build until I approve a feasibility note for each. On branch `feat/specialist-products`, for each approved product:
>
> - write the feasibility note: legal structure, RE partner, borrower protection, purpose and end-use verification, affordability model, Equator interaction (for resolution finance and debt reset), referral of non-recourse cases outside lending, and the risks;
> - build only the approved pilot workflow on the common engine, with product-level delinquency and profitability analytics."

### Phase 20 — Field app, analytics, AI and marketing expansion

> **Instruction to Claude:** "On branch `feat/field-analytics-ai`, build:
>
> - U22 field and assisted-onboarding app (separate Expo target, MDM distribution) only for REs that appoint Udofin for assisted onboarding or recovery; digital KYC under KYC para 24 by the RE's process;
> - U20 governed AI with a model inventory: document classification and extraction with human verification, application completeness checks, internal search, complaint categorisation, summaries; AI never decides credit, prices, moves money or rejects complaints;
> - analytics with consented, pseudonymised events only;
> - consented marketing campaigns through U16, using 140-series and promotional DLT categories, with opt-out honoured across channels."

### Phase 21 — Scale hardening and AWS migration

> **Instruction to Claude:** "On branch `feat/scale-aws`, run multi-tenant scale tests at 1 million+ borrowers and 100+ REs. Then:
>
> - write and rehearse the AWS ap-south-1 / ap-south-2 migration runbook;
> - run DR at scale;
> - tune performance and mobile app size and start-up;
> - repeat independent VAPT and the MASVS assessment.
>
> Present a controlled migration plan for my approval."

---

# PART 13 — START NOW

I have connected my GitHub repository for Udofin, and this file is committed at `docs/00-master-prompt.md`. Do **not** begin by implementing the complete lending application.

First, execute **Phase 0 only**:

1. Read this whole file, including the appendices.
2. Inspect the repository and report its current state: files, branch, tooling and constraints.
3. Identify missing business decisions and the major architecture, regulatory, app-store, data-residency and security risks.
4. Propose, as ADRs:
   - the repository structure;
   - the RE-tenancy and authorisation strategy;
   - the mobile and web architecture (Expo, EAS, OTA policy, PWA);
   - the loan-mirror design (no Fineract; Udofin is not an LMS);
   - the RE-scoped vault and Aadhaar approach;
   - the technology choices, with current versions.
5. Prepare the initial entity model and the API/integration boundaries, including the lender connector contract based on Finbyx Part 5.
6. Prepare regulatory register v1, the DLA register design, the permission policy and the app-store policy check, as described in the Phase 0 instruction.
7. Prepare:
   - the phased roadmap, with dependencies and acceptance criteria;
   - the minimum security, testing and review gates;
   - the competitor benchmark.
8. Present the proposed baseline and your questions for my approval **before** modifying the repository.

After approval:

- Create the `feat/repo-baseline` branch. (The original prompt asked for the initial structure to be committed directly to `main`; that is replaced by this branch and a pull request.)
- Commit only `CLAUDE.md` (from Appendix A), the ADRs, `docs/`, the registers and `docs/regulations/errata.md` (seeded from Appendix F). Application scaffolding (`package.json`, `tsconfig.json`, `app.json` and the app skeletons) belongs to Phase 1.
- Open a pull request.

Throughout development you may ask me as many questions as you need. I will act as project manager; you will architect and build Udofin.

---

# APPENDIX A — CLAUDE.md SEED (keep concise and stable)

```markdown
# Udofin — Claude Code Project Instructions

## What this is
Udofin: multi-lender Lending Service Provider (LSP) platform for Indian regulated lenders (REs:
NBFCs, HFCs, banks). Borrower Android/iOS app (Expo) + borrower web app/PWA (Next.js) + one
portal app (operations, lender, admin workspaces) + NestJS API + workers. Part of the Infrabyx
ecosystem (Finbyx LOS/LMS, LawDocsComply GRC, Equator ODR) — integrate only via versioned
contracts (canonical: docs/ecosystem/infrabyx-integration-spec.md). Full brief: docs/00-master-prompt.md.

## Non-negotiables
- Udofin is an LSP. It never lends, never sanctions, never holds or routes money. Disbursal
  RE → borrower account; repayment borrower → RE account (or co-lending escrow). No Udofin
  pool, escrow, wallet, virtual or merchant account in any loan money flow (CF para 10).
  LSP fees are paid by the RE, never charged to the borrower.
- The RE decides: KYC compliance, credit, sanction, pricing, KFS, disbursement, classification,
  CIC reporting, complaint closure. Udofin pre-filters only on RE-approved rule versions.
- Server decides: app and browser hold no secrets (public config only) and compute no eligibility,
  routing, pricing or DLG. Every external side effect is idempotent (stored idempotency keys).
- Minimal permissions: never contacts, call logs, SMS, telephony, files/media, installed-app
  lists, precise location. Camera/mic/coarse location one-time at onboarding/KYC with explicit
  consent. CI permission audit must pass (docs/compliance/permission-policy.md).
- Minimal storage: basic data only; KYC docs, bureau and bank data in the RE-scoped vault.
  No Aadhaar number, UID token or biometric template stored by Udofin.
- Data in India: prod data, backups, logs, sub-processors. Railway or any non-India host:
  synthetic data only.
- No Aadhaar/PAN/OTP/account numbers/bureau data/document images in logs, analytics, crash
  reports, push payloads, fixtures or code.
- Consent before data: purpose, RE(s), notice version recorded in U4 for every collection/share.
- Offer view is lender-neutral: documented matching, pre-disclosed ranking metric, unmatched
  lenders shown, no dark patterns (CF para 7).
- Each borrower channel is a DLA of each RE (one CIMS line per platform); never claim RBI
  registration or approval (CF para 18(6)).
- Collateral-free loan to a household with income ≤ ₹3 lakh = microfinance loan (CF para 51),
  whatever the product: 50% obligation cap (CF para 55), 09:00–18:00 contact window (RBC 91(2)).
- DLG ≠ collections. DLG never feeds pre-filters and never grants collection rights; recovery
  work only under an explicit recovery-agent contract recorded in U1.
- Recovery (Part 7A, attachable per RE): Udofin never approves, prices or promises a settlement,
  never refers a dispute to arbitration or any ADR (the RE refers), never issues a legal notice
  in its own name or marks one served, never holds or nets recovery money, never repossesses or
  invokes collateral or DLG, and shows legal, ADR and litigation status only as the RE permits.
  Agent work only where appointed: particulars to the borrower before contact (CF 9(6));
  RBC Third Amendment pack from 1 Jan 2027. No WhatsApp in recovery.
- Detach = read-only + export; no recovery record deleted before its retention date or under hold.
- Event names are canonical: never rename; raise gaps as versioned contract changes.
- AI never approves, rejects, prices or routes a loan, moves money, alters terms, or rejects
  or closes a complaint. Complaints are owned and closed by the RE.
- Store policy is enforced server-side per channel (Play/App Store personal-loan rules).
  OTA updates: JS/asset fixes only; never consent, disclosure, payment, permission or
  security changes.
- Money: NUMERIC in DB, decimal.js in TS, strings in APIs. Never floats.
- RE and borrower isolation in API, services AND Postgres RLS (forced) — and tested.
- Part 8A citations (verified against docs/regulations/rbi/) win over any other citation.
  ORM IDs are guidance. Before any regulated workflow: verify the current source and update
  docs/compliance/requirements-to-controls.md. Distinguish law, interpretation, recommendation.
- Feature branches + PRs only. Never push to main, deploy to prod, submit to a store, touch
  prod data or rotate live credentials without explicit owner approval.
- Spec → approval → code. Explain logic in plain English first. Small commits. Never claim a
  test passed unless run; paste results. Mark mock vs sandbox vs live clearly.

## Commands
(pnpm install / dev / test / lint / typecheck / db:migrate / db:test / eas build --profile
preview — fill in Phase 1)

## Where things live
docs/00-master-prompt.md, docs/architecture, docs/adr, docs/specs, docs/products,
docs/data-model, docs/api, docs/integrations, docs/compliance (register, DLA register,
permission policy, store policy), docs/security (threat model, MASVS matrix), docs/testing
(golden-cases), docs/ops (OTA release register, DR, incidents), docs/economics, docs/status.

## Definition of done
Acceptance criteria met on every channel in scope; unit/integration/contract/E2E (device and
web)/isolation/security tests run and passed; no new permission or tracker; consent and audit
events emitted; docs and registers updated; diff reviewed for secrets/PII/unrelated changes.
```

---

# APPENDIX B — BUSINESS DECISIONS THE PROJECT OWNER MUST TAKE

Claude Code should confirm these in Phase 0:

1. **Pilot REs:** names, entity type, layer and asset size (drives CYB chapter and OUT Chapter IV scope), s.11A PML Act notification status, LMS (Finbyx or other), products, states of operation, and confirmation that each RE reports the Udofin DLAs on CIMS before the store submission (Google Play publishes a new personal-loan app in India only if it is already on the RBI DLA list).
2. **Product 2 (payday / short-tenure) design:** Google Play and the App Store do not allow apps that promote personal loans repayable in full in 60 days or less, and the App Store caps APR at 36%. Choose: web-only short tenor; minimum tenor above 60 days in the apps; or drop the product from the MVP.
3. **App identity:** one Udofin-branded multi-lender app, or also RE-branded white-label apps (each a separate store listing, store declaration and CIMS line).
4. **Legal entity and accounts:** the company that publishes the apps (Apple requires a legal entity; Google requires the financial features declaration), owns the DLT entity and headers, and signs LSP agreements; D-U-N-S number and developer accounts.
5. **Udofin's roles per RE:** sourcing only; sourcing and servicing; recovery agent (explicit contract); DLG provider; and the fee model for each (paid by the RE).
6. **DLG appetite:** whether Udofin will offer DLG at launch; capital earmarked; form (cash, FD with lien, bank guarantee); statutory auditor engaged for the CF para 20(3) declaration; the website page for monthly disclosure.
7. **Data model with REs:** what Udofin may retain after hand-off (CF para 14(1)); RE-controlled keys for ML/UL REs; retention periods by data class from each RE's policy.
8. **KYC routes:** OKYC/DigiLocker as default; Aadhaar OTP e-KYC only via notified REs; V-CIP vendor and hosting of each RE; whether any RE requires app-attested devices for KYC or mandates.
9. **Bureau and AA access:** each RE's CIC memberships and consent to Udofin acting as its technology service provider; AA FIU registration of each RE and the FIU gateway; whether to offer a borrower own-report path.
10. **Payments:** each RE's payment gateway merchant account, eNACH sponsor bank or aggregator, UPI AutoPay merchant; confirmation that Stripe and PayPal are out of scope for domestic repayments.
11. **Hosting:** India-region host for real data (Supabase ap-south-1 with India compute, or AWS ap-south-1 / ap-south-2 from the pilot); AWS timeline; self-hosted vs SaaS observability.
12. **Messaging vendors:** SMS gateway and whether lending messages go on each RE's DLT header; WhatsApp BSP (no collections, no payday promotion on WhatsApp); 1600-series numbers for service calls through each RE.
13. **iOS timing:** App Store submission after how many weeks of stable Android pilot.
14. **Field app (U22):** needed at all, and only for REs that appoint Udofin for assisted onboarding or recovery.
15. **Specialist products (7–10):** owner of each feasibility note and the legal-review budget.
16. **Reviewers:** compliance reviewer for the regulatory register; CA for Udofin's ledger and DLG golden cases; CERT-In-empanelled VAPT firm; mobile security assessor (MASVS).
17. **Certifications:** ISO 27001 and SOC 2 Type II timeline (REs may rely on them, OUT para 79).
18. **Languages at launch:** English and Hindi, plus which regional languages for KFS and key communications.
19. **Recovery support (Part 7A):** which REs attach which capabilities (UR1–UR6), the licence SKU and fees (always paid by the RE), and each RE's visibility policy for notices and litigation status (off by default).
20. **Recovery-agent role:** whether Udofin accepts appointments at all; agent IIBF DRA certification plan (new agents from 1 Jan 2027, existing agents by 31 Dec 2027); call-recording vendor and retention; cash collection or digital only.
21. **Equator and ADR:** each RE's clause position (Equator or another institution pre-named, or none); the post-dispute consent journey hosted by Equator; the borrower-facing disclosure that Equator and Udofin are both Infrabyx products; other ODR providers to support.
22. **Products 11–15:** which to pursue, in what order, with which partner REs; Udofin's role in TReDS (referral only).
23. **LAS operating model:** term loan or OD (pending the revolving-credit draft); who contracts with CDSL, NSDL and the RTAs or MF Central; publication of each RE's eligible list and haircuts.
24. **GRC connectors:** which third-party GRC tools partner REs use; OSCAL export scope and frequency.
25. **Retention after detach:** per-RE schedule reconciling RBC para 100P, PMLA and KYC records, limitation periods and DPDP erasure.

---

# APPENDIX C — STARTING REPOSITORY STRUCTURE (to be refined in Phase 0)

Recommendation: **one portal app with three workspaces** (operations, lender, admin) rather than three separate Next.js apps. It shares authentication, design system, tables and audit tooling, and keeps one deployment to harden. Isolation is enforced by workspace-scoped routes, server-side authorisation and RLS, not by separate builds. Split a workspace into its own app later only if an RE contract requires a dedicated deployment or domain.

```
udofin/
├─ apps/
│  ├─ mobile/            # Expo React Native borrower app (Android first, then iOS); EAS profiles
│  ├─ borrower-web/      # Next.js borrower web app + PWA + public site pages
│  ├─ portal/            # Next.js: workspaces ops/, lender/, admin/ (recommended single app)
│  ├─ api/               # NestJS modular monolith (HTTP, webhooks, connector endpoints)
│  ├─ worker/            # Temporal workers, schedulers, outbox relay, report jobs
│  └─ field/             # (Phase 20, optional) Expo field and assisted-onboarding app
├─ modules/              # domain modules (each: domain/, application/, infra/, api/, tests/)
│  ├─ u01-tenancy-lender-onboarding/   ├─ u02-product-catalogue/
│  ├─ u03-borrower-identity/           ├─ u04-consent-privacy/
│  ├─ u05-kyc-verification/            ├─ u06-credit-affordability/
│  ├─ u07-eligibility-routing/         ├─ u08-offers-kfs-cooling-off/
│  ├─ u09-documents-esign-dms/         ├─ u10-disbursement-orchestration/
│  ├─ u11-repayments-mandates/         ├─ u12-loan-mirror-servicing/
│  ├─ u13-collections-support/         ├─ u14-dlg/
│  ├─ u15-grievance-equator/           ├─ u16-communications/
│  ├─ u17-udofin-finance/              ├─ u18-compliance-audit/
│  ├─ u19-reports-mis/                 ├─ u20-ai-governed/
│  ├─ u21-integration-hub/             ├─ u22-field/
│  ├─ u23-admin-white-label/           ├─ u24-secops-fraud/
│  ├─ u25-borrower-dashboard/
│  └─ ur-recovery-support/          # Part 7A UR1–UR6 (attachable; module.yaml)
├─ packages/
│  ├─ contracts/      # OpenAPI 3.1, AsyncAPI, Zod schemas, Finbyx Part 5 event catalogue
│  ├─ domain-kernel/  # Money, Rate, Percentage, BusinessDate, IDs, Result types
│  ├─ journey/        # shared step definitions, validation and copy keys (app + web)
│  ├─ adapters/       # kyc, digilocker, ckyc, vcip, bureau, aa, bank-verify, esign, estamp,
│  │                  # mandate, pg, depository, lms-finbyx, lms-generic, tally, sap, sms,
│  │                  # whatsapp, email, push, odr-equator, grc-lawdocscomply, ocr, llm, integrity
│  ├─ rule-packs/     # regulatory and store-policy guard-rails, versioned
│  ├─ ui-tokens/      # design tokens → React Native + Tailwind
│  ├─ ui-web/         # web components (shadcn), Storybook
│  ├─ ui-native/      # native components, catalogue
│  ├─ config/  ├─ observability/ (PII redaction)  └─ testing/ (synthetic data, device farm, Pact)
├─ db/
│  ├─ migrations/  ├─ rls-policies/  └─ seeds/ (synthetic only)
├─ infra/            # docker, compose, opentofu/terraform, railway (synthetic), aws (eas.json lives in apps/mobile/)
├─ docs/             # see Part 11.4 (incl. compliance/dla-register.md, permission-policy.md,
│                    # store-policy.md; security/masvs-matrix.md; regulations/rbi/, errata.md)
└─ CLAUDE.md
```

---

# APPENDIX D — INITIAL ENTITY MODEL (starting list)

Every RE-scoped table carries `lender_tenant_id` and is protected by server-side authorisation plus Postgres RLS. Money columns are `NUMERIC`. Event and audit tables are append-only. Refine in Phase 0 and record ownership (Udofin, RE mirror or provider evidence) for each entity.

- **Platform, tenancy and agreements (U1, U23):**
  - platform_setting, lender_tenant (RE type, layer, CoR, CIC memberships, FIU status, website disclosure URL, IO applicability), lender_legal_entity, lender_contact (GRO, nodal officer, incident, operations);
  - lsp_agreement (version, effective dates, activities, fees and payer, data shared, approved sub-contractors, audit and RBI access, incident timelines, exit), lsp_agreement_activity, recovery_agent_contract (scope, territory, effective dates), due_diligence_pack;
  - staff_user, role, permission, user_scope, maker_checker_request, break_glass_session, feature_flag, theme_config (design tokens per platform, RE and white-label), config_version, audit_event (hash-chained).
- **Products and catalogue (U2, Part 6):** product_template, product_offer_version (immutable copy of `ProductCatalogPublished`: eligibility parameters, pricing grid, charges, penal charges, KFS template version, cooling-off period, grievance contacts, DLA disclosures), journey_template, document_checklist, verification_plan, consent_set, routing_rule_version (GoRules JDM), store_policy_gate, product_approval, feasibility_note.
- **Borrower identity and devices (U3):** borrower_account, borrower_profile (minimal data), contact_point (mobile, email, verification status), auth_session, device_binding (public key, attestation result, platform, app version, status), device_event, passkey_credential, app_version_policy, mobile_number_change_request, account_closure_request.
- **Consent and privacy (U4):** notice_version, consent_artefact (purpose, data items, recipient, legal basis, notice version, language, channel, timestamp, device, IP, expiry, screen version), consent_event (give, deny, restrict, revoke), data_principal_request (access, correction, erasure, grievance) with clocks, data_map_entry (field, owner, purpose, recipients, location, retention, sensitivity), retention_rule, destruction_certificate, privacy_policy_version, third_party_disclosure.
- **KYC and verification (U5):** kyc_session (route, RE, step version), kyc_evidence (provider, request and response hashes, document hashes, liveness score, timestamps, consent reference), ckyc_identifier_capture, okyc_evidence (masked, no full Aadhaar), digilocker_fetch, pan_verification, otp_ekyc_declaration, vcip_session_reference (RE-held recording reference only), document_capture (quality metrics, redaction flag), face_match_result (score only; no template retained).
- **Credit data (U6):** bureau_consent (RE, purpose, mode), bureau_pull_reference (RE, CIC, enquiry type, response reference, cost), aa_consent_reference (AA handle, consent ID, FIU = RE, purpose, status), income_declaration, household_profile (composition, annual household income, source), affordability_snapshot (RE-approved inputs and outputs), microfinance_flag.
- **Application and routing (U7):** application (state machine), application_state_transition, applicant_data_version, eligibility_request, eligibility_response (RE rule-version reference, outcome, timestamps), matching_mechanism_version (description, rules, effective dates), offer_set, unmatched_lender_entry (reason category), information_request, borrower_task.
- **Offers, KFS and cooling-off (U8):** offer (lender, amount, tenor, APR, monthly repayment obligation, penal charges, KFS link, rank, ranking metric version), apr_check (recomputed APR, tolerance, result), kfs_document (proposal number, validity expiry, language, hash), kfs_view_event (view, scroll completion, duration, explanation acknowledgement), borrower_acceptance, sanction_document, cooling_off_window, cooling_off_exit (request time, RE payable amount, status).
- **Documents and execution (U9):** document (type, owner RE, version, SHA-256, storage key, retention class, verification status), document_access_log, esign_request, esign_evidence (ESP, transaction ID, certificate, signed hash, timestamp, signer name match, IP), estamp_certificate (number, state, value, parties, vendor, linked document), physical_execution_task, document_delivery (channel, recipient, timestamp, status).
- **Disbursement and payments (U10, U11):** beneficiary_account (borrower or end-beneficiary, penny-drop result), disbursement_status (from `LoanDisbursed`/`DisbursementFailed`; UTR), mandate (type, UMRN, sponsor bank, RE utility code, limits, validity, status), mandate_event, payment_intent (RE merchant account, channel, amount, idempotency key, status), payment_status_event, gateway_settlement_record, refund_request, rail_config_validation.
- **Loan mirror and servicing (U12, U25):** loan_mirror (RE loan reference, product, sanctioned and disbursed amounts, rate, tenor, status, as-at sequence), mirror_schedule_line, mirror_transaction (payment, charge, penal charge, reversal), mirror_dpd_snapshot, service_request (type, RE reference, SLA, status), noc_record, document_release_tracker, borrower_ledger_view (materialised per loan), expense_entry (optional, borrower-entered, separate consent).
- **Collections (U13):** collection_allocation (from `CollectionAllocated`; contract reference, scope, contact-policy pack), agent_particulars_notice (sent before first contact), recovery_agent (identity, verification, certification, authorisation per RE, status), contact_policy_pack (effective-dated), contact_attempt (channel, time, outcome, recording reference), ptp, field_visit (agent-device geo-tag), cash_receipt (same-day posting proof), collection_fee_claim.
- **DLG (U14):** dlg_arrangement (RE, contract, form, extent, invocation timeline, term, disclosure clause), dlg_instrument (cash deposit, FD with lien, bank guarantee; amounts, dates, bank), dlg_set (fixed loan list, sanctioned amount), dlg_set_loan, dlg_cover_snapshot (disbursed amount, cap, active cover, headroom), dlg_provider_declaration (auditor certificate, aggregate outstanding, number of lenders and portfolios, past default rates), dlg_invocation (loan, overdue days, amount, settlement), dlg_recovery_share, dlg_disclosure (month, portfolios, amounts, publication time, maker-checker).
- **Grievance and Equator (U15):** grievance (reference, category, against RE or LSP, channel, status, clocks), grievance_event, grievance_attachment, grievance_routing (host switch, GRO, nodal officer), escalation_info_shown (CMS/CRPC route, timestamp), ai_conversation (redacted), ai_answer_source, equator_referral (consent, data set, Equator case ID, status, outcome), feedback.
- **Communications and marketing (U16):** template_version (channel, language, owner, approval, DLT IDs), notification (channel, purpose class, template, status; no PII in push payload), marketing_consent (purpose, channel, default no, timestamps), preference_setting, campaign, campaign_audience_rule, suppression_entry, push_token.
- **Udofin finance (U17):** udofin_ledger tables: gl_account, journal, posting, accounting_period, cost_centre; fee_invoice (RE, type, GST), tds_receivable, vendor_cost_record (per provider call), dlg_accounting_entry, bank_reconciliation_run, tally_export_job, sap_export_job.
- **Compliance and audit (U18):** dla_register (one line per DLA per platform per RE, with Annex-I fields and change history), cims_extract, certification_evidence_pack, regulatory_requirement (REQ-ID shared with Finbyx), control, control_test, evidence, permission_manifest (per build and platform), store_declaration (Play data-safety, App Store privacy, India personal-loan declaration), policy_document_version, auditor_access_grant.
- **Reports (U19):** report_definition, report_run, dashboard, conduct_metric (offer-rank selection shares, dark-pattern audit results).
- **AI (U20):** ai_model_inventory, prompt_log (redacted), ai_output_review, knowledge_source_version.
- **Integration (U21, Part 5):** connector (RE, type, capabilities, version, certification status), connector_mapping_version, connector_certification_run, integration_credential (vault reference only), outbox_event, inbox_event, idempotency_key, webhook_delivery, provider_call_log (redacted, with cost and latency), dead_letter_item, reconciliation_run, reconciliation_break (`DailyReconciliationFile`).
- **Field app (U22):** field_agent, field_device, assisted_session (borrower consent channel), offline_sync_batch.
- **Security and fraud (U24):** risk_signal, fraud_case, security_incident (severity, detection time, RE notification times), incident_notification, vapt_report, app_integrity_event.

- **Added from the Part 8A review** (where a name below repeats or renames an entity above, for example `dla_register_entry` and `dla_register`, `offer_card` and `offer`, `dlg_monthly_disclosure` and `dlg_disclosure`, `aa_consent_mirror` and `aa_consent_reference`, merge them in Phase 0 under the name above and add the listed fields):
  - `lsp_agreement` (RE, version, scope of functions, recovery_agent_appointed, dlg_enabled, minimal_data_set, retention_schedule, effective dates)
  - `dla_register_entry` (RE, DLA name, owner, available_on, link, GRO name, email, telephone, mobile, RE website, activated_at, ceased_at)
  - `cims_certification_pack`
  - `lender_matching_model_version` and `lender_match_result` (matched and unmatched lenders per request)
  - `ranking_metric_publication`
  - `offer_card`
  - `consent_artefact` (purpose, data items, recipient, expiry, status) and `consent_event`
  - `data_classification_item`, `retention_rule` and `purge_evidence`
  - `subprocessor` (processing location) and `sdk_inventory_item`
  - `privacy_policy_version` and `storage_policy_version`
  - `borrower_re_link` (borrower to RE UCIC and KYC level)
  - `kyc_evidence` (vendor, request ID, response hash) and `kyc_decision_mirror` (RE actor)
  - `otp_ekyc_exposure` (RE, financial year, sanctioned total)
  - `vcip_session_reference` (RE storage pointer, deletion evidence)
  - `bureau_enquiry` (RE, CIC, consent ID)
  - `household_profile`, `household_member_income` and `household_obligation_estimate`
  - `aa_consent_mirror`
  - `cooling_off_window` and `cooling_off_exit_request`
  - `nodal_officer` and `grievance_forwarding_receipt`
  - `recovery_agent_notice` (agent, loan, channel, delivered_at)
  - `cash_receipt` and `cash_in_transit_entry`
  - `dlg_arrangement`, `dlg_instrument`, `dlg_set`, `dlg_set_loan`, `dlg_ledger_entry` (no reinstatement type), `dlg_invocation`, `dlg_recovery_share`, `dlg_monthly_disclosure` and `dlg_auditor_declaration`
  - `channel_risk_pack`
  - `app_version_registry` and `device_registration`
  - `re_regulatory_profile` (re_id, re_type, nbfc_category, layer, layer_source, asset_size, asset_size_date, deposit_taking, effective_from, effective_to)
  - `outsourcing_clause_check` (re_id, agreement_version, clause_id, status, evidence_ref, reviewed_at)
  - `conflict_declaration` (re_id, declared_at, persons, outcome, board_exception_ref)
  - `re_change_approval` (re_id, change_type, artefact_ref, version_hash, approver_name, approver_role, approved_at, scope)
  - `subprocessor` and `subprocessor_consent` (re_id, subprocessor_id, consent_ref, consented_at)
  - `communication_template` (re_id, event_code, language, version, approved_by_re_ref)
  - `contact_policy` (re_id, product_id, microfinance_flag, window_start, window_end, daily_cap, weekly_cap) and `contact_attempt` (case_id, channel, attempted_at, caller_id, recording_ref, outcome)
  - `recovery_agent` (agency_id, person_id, police_verification_ref, verified_at, reverify_due, training_ref, undertaking_ref, status) and `agent_authorisation` (case_id, agent_id, notice_ref, letter_ref, notified_at)
  - `telemarketer_registration` (number_or_header, registration_ref, valid_to)
  - `kfs_acknowledgement` (application_id, kfs_version_hash, validity_expires_at, acknowledged_at, device_ref)
  - `service_request` (type such as account_transfer, hardship, settlement, document_release; sla_due_at; re_status)
  - `security_incident` and `incident_re_notification` (incident_id, re_id, detected_at, notified_at, severity, report_ref)
  - `vapt_engagement` (scope, tester, type, performed_at, report_ref, open_findings)
  - `vendor_assurance_pack` (version, published_at, contents_index)
  - `risk_signal` (subject_ref, signal_type, score, evidence_ref, sent_to_re_at)
  - `fraud_evidence_request` and `scn_received` (re_id, received_at, response_due_at)
  - `party_identifier` (party_id, pan_verified_ref, din, source)
  - `end_use_certificate` (loan_ref, requested_at, submitted_at, document_ref)
  - `re_suppression` (re_id, borrower_id, reason_code, until)
  - `co_lending_arrangement` (originating_re_id, partner_re_id, shares, escrow_account_ref, interface_entity)
  - `audit_access_grant` (re_id, grantee_type, scope, valid_from, valid_to)
  - `re_exit_plan` and `data_export_job` (re_id, scope, started_at, completed_at, checksum)
- **Added in v1.1** (Part 7A recovery support, Parts 6.4–6.5 product workflows and LAS, Phase 16b ecosystem integration). Where a name repeats an entity above (for example `ptp`, `recovery_agent`, `contact_attempt`, `equator_referral`, `connector_certification_run`), merge it in Phase 0 under the earlier name and add the listed fields:
  - **Module attachment (7A.0):** `module_manifest` (module_id, version, requires, capabilities, events_produced, events_consumed, regulatory_refs, retention_class, licence_sku, ui_slots); `module_entitlement` (re_id, product_id, capability, licence_sku, flag_key, state, effective_from, effective_to); `module_lifecycle_event` (module_id, re_id, from_state, to_state, actor, maker_checker_ref, event_ref for `ModuleAttached` or `ModuleDetached`); `detach_export_job` (re_id, module_id, scope, manifest_sha256, delivered_at, acknowledged_at); `retention_class` (class, minimum_period, basis, trigger); `legal_hold` (record_ref, reason, placed_by, placed_at, released_at)
  - **Rule packs (7A.0.4):** `contact_policy_pack` (re_id, pack A or B, state overlay, microfinance_window, window_start, window_end, frequency caps from the RE's Board policy, blackout calendar, version, effective_from, effective_to); `borrower_contact_preference` (borrower_id, re_id, preferred times and places, captured_at)
  - **UR1 overdue and settlement centre:** `settlement_request` (re_id, loan_ref, proposal, schedule, reason, documents, status, offer_ref); `settlement_offer_mirror` (re_ref, terms, validity_until, characterisation block: restructuring flag, CIC status, cooling period, consent-decree flag, fraud or wilful-defaulter note; sha256); `settlement_acceptance_evidence` (offer_ref, method, provider transaction ID, offer_sha256, timestamp, device_ref); `hardship_request` (loan_ref, reason, submitted_at, re_status); `ptp` (adds promised_amount, channel, captured_by, outcome from RE events)
  - **UR2 ADR access:** `adr_case_view` (re_id, loan_ref, provider, provider_case_id, track, basis type and reference, status, last_seq, hold_flag); `adr_link_issue` (case_view_id, token_hash, expires_at, used_at); `adr_request` (borrower-initiated; grievance_ref, requested track, re_response, responded_at); `adr_info_view_event`
  - **UR3 notices and case visibility:** `notice_mirror` (re_ref, instrument, statute_ref, language, sha256, template_version, re_statutory_mode, visibility_policy_version, withdrawn_at); `notice_delivery_event` (notice_id, channel, delivered_at, opened_at, read_fully_at, failure_reason); `case_status_projection` (loan_ref, source event, approved_string_id, as_of); `visibility_policy` (re_id, product_id, instrument, stage, approved_string_id, approved_by_re_ref, version)
  - **UR4 recovery-agent operations:** `recovery_agent_contract` (adds buckets, territories, channels, cash_allowed, cash limits, effective dates); `agent_certification` (agent_id, IIBF DRA reference, issued_at, expires_at, grace_until); `contact_evaluation` (allocation_id, party_id, channel, purpose, attempted_for, pack_version, inputs_sha256, decision, denial_reason); `call_recording` (attempt_id, storage_ref, disclosure_played, retention_until, legal_hold_id); `agent_scorecard` (agent_id, period, outcome and conduct metrics); `agency_list_publication` (re_id, published_at, version, delivered_to_re_at)
  - **UR5 feeds:** `feed_delivery` (event_id, re_id, type, consentref or basis flag, status, acked_at, reconciliation_run_id)
  - **UR6 controls:** `control_definition` (control_id UR6-C01 to C16, rule refs, owner, frequency); `control_test_run` (control_id, period, result, population, sample_masked_ids, evidence_sha256); `grc_export_job` (target tool, contract version, OSCAL version, period, package_sha256, delivered_at)
  - **Products and LAS (Parts 6.4–6.5):** `product_playbook_link` (product_code, finbyx_r16_code, version); `las_eligible_security_list` (re_id, version, ISIN or scheme, haircut, group_1_flag, excluded_reason); `collateral_position_mirror` (loan_ref, rail, ISIN or scheme, quantity, pledge_or_lien_ref, pledgee, status, as_of); `pledge_request` (loan_ref, rail, quantity, provider_request_id, authorisation_evidence_ref, status); `valuation_snapshot_mirror` (loan_ref, eligible_value, drawing_power, ltv, price_source, as_of, frozen_flag); `margin_call_mirror` (loan_ref, shortfall, options, deadline, working_day_calendar_ref, status); `drawdown_request` (facility_ref, amount, idempotency_key, status, re_ref, utr); `gold_branch_appointment` (re_id, branch_ref, slot, status); `institution_beneficiary` (institution, account verification, fee schedule); `invoice_reference` (anchor, invoice number, factoring_unit_id, platform, due_date)
  - **Ecosystem integration v2 (Phase 16b):** `event_schema_version` (type, version, registry_url, compatibility, dual_publish_until); `signing_key` (kid, algorithm, purpose, rotated_at, retired_at); `webhook_endpoint` (counterparty, url, secret vault reference, tolerance); `odr_provider_connector` (provider, transport, mapping version, certification status); `grc_connector` (tool, field_map_version, OSCAL support, certification status); `co_lending_split_mirror` (loan_ref, originating_re, partner_re, shares, escrow_ref, interface_entity); `loan_transfer_mirror` (loan_ref, mode, transferee, servicer, effective_date, payment_instruction, notice_ref)

---

# APPENDIX E — CHANGES FROM THE ORIGINAL UDOFIN PROMPT

The original Udofin prompt is preserved in substance. The table lists where this prompt departs from it and why. Claude Code must follow this prompt where the two differ.

| # | Original prompt said | This prompt says | Reason (source) |
|---|---|---|---|
| 1 | Structure the repo and "commit these initial changes directly to my main branch" | Inspect first, work on a feature branch, open a pull request, merge only after approval | The same prompt also required feature branches and no direct push to main; protected main prevents unreviewed changes (Part 11) |
| 2 | Udofin is a mobile application because customers share location and OTPs; a web app may be suggested "if it is right" | Mobile app (Android, then iOS) plus a borrower web app/PWA, ops portal, lender portal and optional field app; each borrower channel is a separate DLA | Browsers support OTP, location, camera, eSign, DigiLocker, eNACH and V-CIP; DLAs are "mobile and / or web-based" (CF para 4(1)(x)); registration per platform (CF para 18) |
| 3 | Udofin soft-pulls CIBIL via Surepass | Bureau data is pulled under the RE's CIC membership or a verified borrower-consented route, for the chosen RE, with consent naming that RE | Membership of CICs is the RE's (CIR para 6); access is limited to specified users under CICRA [VERIFY CICRA s.2(l), CIC Regulations reg. 3 and Surepass's authorisations] |
| 4 | Udofin fetches Aadhaar through OTP | Offline verification or DigiLocker by default; Aadhaar OTP e-KYC only through an RE notified under s.11A PML Act and its licence; no full Aadhaar stored | KYC para 23 and provisos; OTP-e-KYC limits (KYC para 25); UIDAI vault rules (Part 8.2) |
| 5 | Udofin gives 5% FLDG, therefore it must take care of collections | DLG and collections are separate; collection rights only from an explicit recovery-agent contract | DLG is a loss-sharing contract (CF paras 19–29); recovery-agent role is separate (CF para 6(5)); the original prompt itself asked for this separation |
| 6 | FLDG terminology | Default Loss Guarantee (DLG), with eligibility, forms, 5% cap on a fixed set, auditor-certified declaration, 120-day invocation, no reinstatement and monthly disclosure | CF paras 4(1)(viii), 19–29 |
| 7 | Integrate Razorpay, Stripe and PayPal | Gateways only on the RE's merchant account with settlement to the RE; Stripe and PayPal kept as interfaces, not used for domestic EMIs until verified | Repayment directly to the RE with no pool or pass-through account (CF para 10(2)–(3)); Stripe and PayPal India limitations [VERIFY] |
| 8 | Supabase for database and auth; Railway for the backend | Supabase in an India region for real data; Railway for synthetic data only; Supabase Auth behind an OIDC abstraction; plan for AWS ap-south-1 and ap-south-2 | Data stored only in India (CF para 14(4)); Railway has no India region; portability |
| 9 | ExpressJS server on Railway, including "calculating interest rates" | NestJS modular monolith (major version per the shared ecosystem ADR with Finbyx) with workers and Temporal; Udofin never computes pricing, it displays the RE's figures and independently checks the APR | Modular boundaries and durable workflows; pricing is the RE's decision (RBC para 29; OUT para 15) |
| 10 | Supabase migrations for users, loan_applications, loans and repayments; users read and write their own data | Udofin owns applications, consents and evidence; loans are a read-only mirror of the RE's records; RLS for both borrower and RE tenant isolation; the mobile app never holds privileged keys | The RE's LMS is the system of record (Part 5.1); tenant isolation (Part 10.2, principle 3) |
| 11 | Udofin and Finbyx integrate with Tally Prime/SAP, Finbyx manages end-to-end accounting, and all tools make "make double-entry, subledgers, loan schedules, accruals, provisioning core capabilities" | Udofin keeps double-entry books for its own LSP business (fees, GST, DLG, vendor costs) plus a loan mirror for the borrower view; loan accounting stays in the RE's LMS | Udofin is not a lender; Tally Prime and SAP are export destinations (U17) |
| 12 | An automated grievance mechanism in which an AI agent answers the borrower's queries | AI gives informational support from approved sources and suggests routing; the RE's GRO decides; the CMS escalation route is always shown | Redressal responsibility remains with the RE (CF para 12(3)–(4)); the original prompt also barred AI from rejecting complaints |
| 13 | The app can ask for permissions to use phone data for better UX | Permission policy: one-time camera, microphone and location for onboarding/KYC only; no files and media, contacts, call logs, SMS or telephony; system pickers after onboarding | CF para 13(1); DPS para 68(2)(vii) as baseline; app-store data-safety rules |
| 14 | Users scan documents and share KYC with "the system administrator" | Documents go to the RE that the borrower chose, with consent; Udofin staff see them only on a need-to-know basis with logging | Explicit consent before sharing (CF para 13(4)); minimal LSP data (CF para 14(1)) |
| 15 | eSign and eStamp are used on Udofin only | Executed in the Udofin journey, but the documents are the RE's, on its letterhead, and evidence flows to the RE; physical execution where electronic execution is excluded | CF para 9(3); IT Act First Schedule |
| 16 | Lenders' dashboard to generate finance, risk-management and compliance reports; apply Basel/BCBS and Ind AS | Lender portal reports cover Udofin-sourced business, conduct and reconciliation; prudential, risk and financial reports come from the RE's LMS (Finbyx M17) | Udofin does not hold the loan book |
| 17 | Explore Apache Fineract | Not used in Udofin; Fineract is an LMS concern (Finbyx Part 4) | Udofin keeps only a loan mirror |
| 18 | Ten-phase build plan | 24-phase plan (Phases 0–21 plus 3b and P) with an MVP pilot gate before secured and specialist products | Separates regulated foundations (consent, KYC, money-flow guards) from features; narrow MVP (Part 12) |
| 19 | Nine products "should be there" (no personal loan), four of them flagged by the original for feasibility assessment | Ten product templates; Personal Loan and Payday in the MVP; secured products in Phase 18; Products 7–10 only after an approved feasibility note | The original prompt asked for feasibility assessments; Google Play Personal Loans policy and App Store Guideline 3.2.2(ix) (no loans repayable in full in 60 days or less; App Store APR cap of 36%) |
| 20 | Payday loans "work like personal loans" | Separate template with heightened conduct controls, one-working-day KFS validity for tenors under 7 days, CCO evaluation and 6-month monitoring, and an app-store launch gate | RBC para 29(2); CMP paras 15(2), 31; Google Play Personal Loans policy; App Store Guideline 3.2.2(ix) |
| 21 | Some NBFCs may use only Udofin's web portal | Portal-only mode: the RE decides in the lender portal with maker-checker; Udofin hosts but never changes the RE's rules; the RE books loans in its own LMS | Sanction cannot be outsourced (OUT para 15) |
| 22 | Grievance module may sit in LawDocsComply or Finbyx; unresolved cases go to Equator | Kept as the grievance-host switch; Equator is offered only where legally and contractually appropriate and never displaces the RBI CMS route | CF para 12(4) |
| 23 | Marketing capabilities such as push notifications | Separate marketing consent with "no" as default, service and marketing messages split, DLT templates, no lender promotion inside the offer journey | CF para 7(4); RBC para 101; RBC Second Amendment [VERIFY] |
| 24 | "Books of accounts" view of the borrower's finances | A per-loan and cross-loan ledger from the RE's data; personal expense tracking only with separate consent and borrower-entered data | Udofin is not an FIU and cannot pull bank data for its own purposes (AA para 8(12)) |
| 25 | RBI master directions issued on 28 November 2025 and 31 July 2026 | 33 RBI Directions and 1 guidance note supplied for Finbyx v1.3, cited paragraph by paragraph in Part 8A with the same REQ-IDs | One shared ecosystem register |
| 26 | Owner will integrate provider APIs manually later | Claude Code builds provider adapters with mocks and sandboxes now; the owner supplies contracts and credentials; production adapters are labelled separately | Original definition of done (clearly distinguish mock from production) |
| 27 | Inspect the current products through a logged-in browser session to find loopholes in the current versions | Claude Code works from the repository and does not rely on a live session; the owner supplies screenshots, exports or a test account for the current udofin.com flows, which Phase 0 reviews as a gap analysis alongside the competitor benchmark | Reproducible evidence; no production credentials in the coding session (Part 11) |

## Further corrections found in the Part 8A review

| # | Original assumption | Correct position (source) |
|---|---|---|
| 1 | Udofin soft-pulls the CIBIL score itself through Surepass | Bureau pulls are the RE's, as CIC member and CI, under its credit policy; Udofin may only be the RE's technology channel with RE credentials, and every enquiry is the RE's (CIR paras 4(3), 6, 20; CICRA s.2(l) [VERIFY]) |
| 2 | Udofin gives 5% FLDG, so collections are Udofin's responsibility | DLG gives no collection role. Collection needs a separate recovery-agent appointment, RE guidance and notice to the borrower before contact. 5% is a ceiling on the amount disbursed from a fixed DLG set, not a fixed rate, and fee clawbacks count as implicit DLG (CF paras 4(1)(viii), 6(5), 9(6), 24; RBC paras 93–99) |
| 3 | The app may ask for permissions to use phone data | DLAs must not access file and media, contacts, call logs or telephony functions. Camera, microphone and location are one-time, for onboarding or KYC only, with explicit consent (CF para 13(1)) |
| 4 | Udofin is mobile-only because customers share location and OTPs | The web app is equally a DLA, with its own CIMS line. Location is a one-time onboarding/KYC access, not a reason for a native app (CF paras 4(1)(x), 13(1), 18; Annex-I) |
| 5 | NBFCs will disburse the loan on the Udofin platform | Disbursal goes from the RE directly to the borrower's bank account and repayment directly to the RE's account; there is no LSP pool or pass-through account, and Udofin orchestrates status only (CF para 10(1)–(3)) |
| 6 | Aadhaar is fetched by OTP on the mobile number the borrower enters | Number-based e-KYC is only for REs notified under PML Act s.11A; the OTP goes to the Aadhaar-registered mobile; NFTF OTP-e-KYC loans are term loans of no more than ₹60,000 a year, upgraded within 1 year; Aadhaar is not mandatory, so offline, DigiLocker, CKYC and V-CIP routes must be offered (KYC paras 23, 25) |
| 7 | The borrower shares KYC with the Udofin system administrator, who completes it | The RE cannot outsource the KYC decision, and cannot rely on Udofin as a third party because Udofin is not regulated for CDD; Udofin supplies evidence only (KYC paras 13, 22(3)) |
| 8 | Udofin stores KYC files, CAMs and loan documents as its DMS of record | The LSP keeps only basic minimal data within the agreement; KYC, bureau and AA artefacts go to the RE and are purged; the CAM is the RE's; no biometric storage (CF para 14(1), 14(3)) |
| 9 | Razorpay, Stripe and PayPal integrations collect payments for Udofin | Gateways must run on the RE's merchant account with settlement to the RE; no third party controls the flow; LSP fees are paid by the RE and never charged to the borrower (CF para 10(2)–(4)); Stripe/PayPal suitability for domestic loan collections [VERIFY] |
| 10 | The borrower sees which NBFCs and banks offer loans (presentation left open) | All matching offers must be shown, with the names of unmatched lenders, on a consistent documented mechanism; ranking only on a publicly pre-disclosed metric; no dark patterns (CF para 7) |
| 11 | The borrower can view finances "like books of accounts" in Udofin, by implication from AA data | Udofin cannot be an FIU, and AA data received by the RE may be used only for the consent purpose (AA paras 8(12), 28) |
| 12 | Location and other device data may support collections | Location is limited to one-time onboarding/KYC access; collections use RBC contact rules and agent notice (CF para 13(1); RBC paras 91, 100) |
| 13 | CF rules apply to every partner lender | CF 347 binds NBFCs and HFCs; bank partners follow their own Directions (CF para 3(1)) [VERIFY bank text] |
| 14 | Udofin runs collections under its own policy | Collection rights arise only from an explicit recovery-agent appointment; the RE stays responsible and RBC conduct rules apply to Udofin as its agent (CF 6(5), 9(6); OUT 17; RBC 93–100) |
| 15 | A collection engine runs in Udofin for every loan | Udofin's recovery functions activate per RE contract only; pre-due reminders are servicing and still follow language and penal-charge disclosure rules (RBC 10, 30(7)) and, by policy, the RBC para 100 calling window (which itself covers recovery of overdue loans) |
| 16 | An AI agent answers queries, the borrower contacts the NBFC GRO, and unresolved grievances go to Equator | Grievance responsibility stays with the RE; Udofin also needs its own nodal GRO; the borrower must be told of the RBI Ombudsman route after rejection or 30 days without reply; Equator is optional and cannot replace or delay that route (CF 12; OUT 56–57, 98) |
| 17 | Resolution finance tests actual settlement cases through Equator | Compromise settlement is the RE's discretion; payment over more than 3 months or part settlement is restructuring; a cooling period of at least 12 months applies before fresh exposure by that RE; a consent decree is needed where court recovery is pending (RSA 87, 89–90, 95, 100) |
| 18 | Udofin handles closure, settlement and release of security | These are RE obligations with fixed clocks and compensation; Udofin relays requests and mirrors status (RBC 35–41; RSA 87) |
| 19 | The borrower sees which NBFCs and banks offer loans, implying Udofin decides eligibility | Loan sanction and KYC-compliance decisions cannot be outsourced; Udofin's routing and indicative eligibility are non-binding (OUT 15) |
| 20 | Data protection and cyber security as generic capabilities | Specific obligations: incident notice feeding the RE's 6-hour RBI clock, VA every 6 months and PT every 12 months, India-only storage, audit and RBI inspection rights, subcontractor consent (OUT 34, 61, 74; CYB 28, 121; CF 14(4)) |
| 21 | Disaster recovery as tested restoration only | Also half-yearly DR drills, collaborative resilience tests against each RE's RTO, and DC/DR geographic separation (CYB 102, 129, 138) |

## E.3 v1.0 → v1.1

| # | v1.0 said | v1.1 says | Reason (source) |
|---|---|---|---|
| 1 | Part 5 event names identical to Finbyx 5.2; six events proposed | The Infrabyx Ecosystem Integration Specification v1.0 is canonical; Part 5 summarises it; the six events are adopted; new collateral, co-lending and transfer, recovery, ADR, litigation, compliance and platform domains | One contract for every Infrabyx product |
| 2 | U13 and U15 covered collections and Equator referral | Part 7A (UR1–UR6), attachable per RE, prevails over U13 and U15 | Owner requirement; CF paras 6(5), 9(6), 10(5), 12 |
| 3 | Equator referral offered by Udofin | Only the RE refers, and only under a pre-named institution clause or written post-dispute consent; Udofin holds no referral scope | *CORE v ECI-SPIC-SMO-MCML (JV)* (SC, 8 Nov 2024); *L&T Finance v Jai Paras Material Store* (Cal HC, 14 May 2026); *Shikha Ghosh v Axis Bank* (Del HC DB, 30 Sep 2026) |
| 4 | RBC Third Amendment text not supplied, not coded | RBI/2026-27/230 (6 Aug 2026) confirmed from the RBI notification; rule pack B from 1 Jan 2027; official text still to be committed [VERIFY] | RBI notification Id=13672 |
| 5 | Recovery-call recording a recommendation | Mandatory from 1 Jan 2027, kept at least 6 months or until disposal if sub judice | RBC Third Amendment para 100P [VERIFY] |
| 6 | No agent certification rule | IIBF DRA certificate for agents from 1 Jan 2027; existing agents one more year | RBC Third Amendment para 100I [VERIFY] |
| 7 | Settlement relay in U12 only | UR1 with the RE's characterisation block and acceptance evidence; acceptance sent as `SettlementOfferAccepted` (Integration Spec 6.8) | RSA paras 16, 87–100; CIR para 12(4) |
| 8 | Ten product templates | Products 11–15 proposed (Phase 18b); product-wise workflows for all products (Part 6.4) | Owner requirement; research gap |
| 9 | LAS: pledge in favour of the RE; margin notices shown | Full journey (Part 6.5): RE computes drawing power; term loan by default, OD behind a flag; SEBI reasonable-notice undertaking before invocation | CF paras 104–106; SEBI circular, 5 Feb 2026 [VERIFY] |
| 10 | LawDocsComply bridge only | Generic GRC contract with OSCAL export; MetricStream, OpenPages, ServiceNow IRM and Archer adapters | Owner requirement |
| 11 | Phases 0–21 plus 3b and P | Adds Phases 12b, 16b and 18b | Part 12 |
| 12 | (Udolex) an LSP may execute settlements within DLG agreement limits without the RE | Not permitted: settlement is the RE's decision, one level above the sanctioning authority | RSA paras 16(5), 157; OUT para 15 |
| 13 | (Udolex) DLG capped at 5% of the outstanding pool; invocation 6–12 months after NPA; proceeds credited to the NPA account | 5% of the amount disbursed from a fixed set; invocation within 120 days overdue; never set off against the loan | CF paras 24, 25(2), 27(1) |
| 14 | (Udolex) at most 3 contact attempts a week and "one-click human transfer" as RBI rules | RBI sets no numeric cap (Board policy decides); human hand-over is a recommendation drawn from the FREE-AI report | RBC para 100; Third Amendment paras 100Y–100Z |
| 15 | (Udolex) Mediation Act mandates pre-litigation mediation; mediated settlements enforceable once registered | s.5 is voluntary and not in force; s.27 enforcement not in force; conciliation (A&C Act s.74) is the enforceable route today | Mediation Act 2023; S.O. 4384(E), 9 Oct 2023 |
| 16 | (LAS proposal) drawing-power engine in Udofin; event names of its own | Drawing power at the RE; canonical collateral events | Part 6.5.4 |

---

# APPENDIX F — DRAFTING SLIPS FOUND IN THE SUPPLIED RBI TEXTS

Seed `docs/regulations/errata.md` from this list (Part 8A.0.1 rule 6). For each slip, implement the evident intent, record the interpretation, and re-check it when RBI issues a corrected or amended text.

**IRACP / RSA**

- IRACP para 32(2)(i) says "NBFC-BL" in a Chapter II (all-NBFC) rule.
- IRACP para 5 repeats "with these Directions".
- RSA para 23 table: the last row repeats "secured portion" (evidently "unsecured portion").
- RSA para 66 cites para 63 for the additional specific provisions (evidently para 64).
- RSA para 72 cites para 70 for the freeze period, which is set in para 69.
- RSA para 84 contains the artefact "_bookmark20".
- RSA para 108 says CRILC instructions "as per paragraph 107", which covers consortium intimation.
- RSA para 138 is truncated in the official PDF (text reads only "A").
- RSA Part B uses "compromise settlement" without defining it (definition is Part A para 10(2), not applied by para 157).

**RBC / WD**

- RBC para 37: "sanction letters issued on or December 1, 2023" (word "after" missing).
- RBC para 31(3) Note: "where such an option is provided by the bank" (should read NBFC).
- RBC para 43: unclosed parenthesis "(and timeline for serving an auction notice…".
- RBC para 6(9): defines microfinance loan by reference to an "NBFC – Microfinance Institution Directions, 2025", whereas microfinance rules sit in CF Ch V [VERIFY].
- RBC paras 89–97 (recovery and agent rules) sit under Section H (microfinance), while para 100 excludes microfinance loans; the general agent rules are in paras 98–100 only.
- WD Annex I field 10: valid values list "01 - Suit filed" and "– Non-Suit Filed" without the code "02" (Annex II shows 02).
- WD Annex I: field 11 uses "SUBST" and field 12 uses "SUBSTD".
- WD Annex II: field numbering skips 17 (16 → 18).
- WD para 5(15) requires non-whole-time/independent/nominee directors to be flagged in Annex II, but Annex II has no such field, and the Annex I note excludes them.
- WD para 3(1)(xii)(e): cites the SBR "Guidelines, 2025" (the instrument is a Directions).
- WD para 21(1): cites the "Fraud Risk Management in NBFCs Directions, 2024" (now RBI/DoS/2026-27/463, 2026).

**KYC**

- KYC para 23 proviso (v) and para 27(2)(vi)(c) refer to "paragraph 62" for CKYCR. CKYCR is para 63; para 62 is FCRA.
- KYC para 63(7) refers to "clauses (5) and (6)" for the 1 Apr 2017 / 1 Apr 2021 cut-off dates; they are in clauses (4) and (5). It also cites a "clause (10)" that does not exist (para 63 has nine clauses).
- KYC para 28(vi)–(vii) say "Directions (4) and (5)" where they mean clauses (iv) and (v) of para 28.
- Annex I (MHA UAPA Order) numbering skips para 3.3; the Order also cites "Para 4(i)" and "Paragraph 5 (i)", which do not exist in that form. These are reproduced Government text; no software impact.

**TDCR / SEC**

- **TDCR para 2, second proviso vs para 96:** para 2 defines existing CLAs as those "executed before August 06, 2025"; para 96 says "executed before the date of issuance of these Directions" (28 Nov 2025). Implement: CLAs entered into before the effective date follow the earlier rules, and record both dates.
- **TDCR para 83 proviso:** cross-refers to "sub-clause (a)", but the items are numbered (i)–(iv). It is a legacy 2021 transition running to FY 2025-26.
- **TDCR:** paras 1–2 read "Reserve Bank of India of India"; para 95 refers to "a RE"; para 92(2) has "perspective buyers".
- **SEC para 84(3):** reads "rest" for "reset".
- **SEC para 114:** omits "2025" from the FS Directions title.
- **SEC para 4(10) vs TDCR para 12(4):** the SEC AIFI list omits NaBFID; TDCR includes it. Treat as intended; do not harmonise.

**CAP / SBR / DIV / MISC**

- CAP 12(8)(iii) refers to "paragraph 8(i)" (para 8 is CET1 deductions); the intended cross-reference is within 12(8).
- CAP 18(9)(iii) refers to "8(i) and 8(ii)"; it means 18(9)(i)–(ii).
- CAP 50 refers to "paragraph 44" for the thickness adjustment; the formula is in para 45.
- CAP 18(1) places the Sr (2)(e) infrastructure loans under the "Investments" heading.
- DIV para 3 numbers item (x) twice; para 11 numbers item (i) twice; para 7 says "this Master Direction".

**CF / GOV / OUT / ORM**

- CF para 62(2) cites a "Reserve Bank of India (NBFCs – Management of Third-Party Dependencies) Directions, 2025". No such Direction exists; the correct reference is OUT 363 ("Managing Risks in Outsourcing"; para 1), which CF para 6(6) cites correctly.
- GOV para 17(2) takes the IS audit periodicity from the Outsourcing Directions, which prescribe none. Use CYB para 56 for BL ≥ ₹500 crore (at least once a year, preferably before the statutory audit); ML and above set the periodicity in their IS Audit Policy (CYB para 150).
- OUT para 4(2)(i) and para 5(1) cross-refer to para 58(1)/(2) "above"; para 58 comes later.
- OUT para 6(2) defines "Group" by reference to the Reserve Bank of India (Commercial Banks – Concentration Risk Management) Directions, 2025, not the NBFC Directions. NBFC CON 351 contains no "group" definition [VERIFY the Commercial Banks text].
- OUT para 57(4) cites the RBI Integrated Ombudsman Scheme, 2021, which RB-IOS 2026 has superseded (effective 1 Jul 2026) [VERIFY: RB-IOS 2026 text not supplied].
- The ORM Guidance Note's RBI number is printed blank ("RBI/2025-26/") in the supplied copy.

**SA / IAF / ALM / CON / SR**

- SA para 23: "the outgoing SCAs / SAs **of the bank**" in NBFC Directions.
- IAF para 29 uses a 3-level risk scale (high, medium, low). Para 34 uses 5 levels (low, medium, high, very high, extremely high). Make the scale configurable.
- ALM para 58 cites the "Reserve Bank of India (Filing of Supervisory Returns) Directions, 2024". Use SR 2026 instead.
- CON Annex I is headed "Return for the Month" and para 48(4) says "10 largest exposures". SR para 21 item 12 lists the LE Framework return as quarterly, with the "20 largest exposures".
- SR para 21 table: DNBS09 shares CRILC's merged applicability cell, and FUA and FMR4/RBR share FMR's merged cell. Plain-text extraction loses this; confirmed from the PDF (pp. 8, 10–11).

**Found while drafting Udofin**

- CF para 4(1)(xix) says a payment aggregator acting as an LSP must comply with "Chapter IV" (gold and silver); it evidently means Chapter III (digital lending).

---

## SOURCES CONSULTED FOR THIS PROMPT (for Claude Code to re-verify)

- **RBI:**
  - Official texts of the 33 Directions and 1 guidance note in Part 8A, supplied by the project owner: docs/regulations/rbi/
  - Press release on the 244 consolidated Master Directions (28 Nov 2025): https://www.rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=61705
  - Master Directions index: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx
  - NBFC Credit Facilities Directions, 2025: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12957
  - NBFC Responsible Business Conduct Directions, 2025: https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=12942
  - NBFC Credit Information Reporting Amendment Directions (RBI/DOR/2025-26/117, 4 Dec 2025): https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13187
  - KYC amendment (29 Dec 2025): https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13236
  - NBFC Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions, 2026: https://rbi.org.in/scripts/NotificationUser.aspx?Mode=0&Id=13592
  - NBFC Fraud Risk Management Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13590
  - NBFC Supervisory Returns Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13587
  - NBFC Miscellaneous Supervisory Directions, 2026: https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13586
  - 31 Jul 2026 Supervision Directions press release: https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=63265
  - RBC Second Amendment Directions, 2026: https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=13493
  - Digital Lending Directions, 2025 (8 May 2025; legacy, now in CF Chapter III) and CIMS DLA reporting press release (CIMS open by 13 May 2025; data by 15 Jun 2025; public list "DLAs deployed by Regulated Entities" under Citizen's Corner by 1 Jul 2025): https://rbi.org.in/Scripts/BS_PressReleaseDisplay.aspx?prid=60403 and https://rbi.org.in/Scripts/NotificationUser.aspx?Id=12848&Mode=0 (exact URL of the public DLA list [VERIFY])
  - Regulation of Payment Aggregators Directions, 2025 (15 Sep 2025): https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=12896
  - RBI Complaint Management System: https://cms.rbi.org.in
  - FREE-AI report: https://www.rbi.org.in/scripts/PublicationReportDetails.aspx?ID=1306
- **Data protection, IT and telecom:**
  - DPDP Rules, 2025 (G.S.R. 846(E), 13 Nov 2025) summary and commencement dates: https://ssrana.in/articles/meity-notifies-final-digital-personal-data-protection-rules-2025/
  - DPDP notification status and proposed SDF compression (not gazetted as of Sep 2026): https://consentos.in/learn/dpdp-rules-notification-status/ (verify against the Gazette and meity.gov.in)
  - CERT-In Directions under s.70B(6) (28 Apr 2022): https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
  - TRAI TCCCPR amendments (12 Feb 2025): https://cms.trai.gov.in/sites/default/files/2025-02/PR_No.11of2025.pdf
  - TRAI 1600-series directions (IRDAI entities, 16 Dec 2025, referring to the earlier direction for RBI-regulated entities): https://www.trai.gov.in/sites/default/files/2025-12/PR_No.151of2025.pdf
  - Secondary summary of the 19 Nov 2025 TRAI direction for RBI-regulated entities (phased dates 1 Jan, 1 Feb, 1 Mar 2026): https://www.elisiontec.com/trai-1600-series-mandate-bfsi-phased-deadlines.md [VERIFY against TRAI]
- **Aadhaar, DigiLocker and CKYC:**
  - UIDAI Circular No. 14 of 2025 (Aadhaar Data Vault): https://www.uidai.gov.in/images/Circular-No.14_of-2025.pdf
  - UIDAI Aadhaar Data Vault FAQs (3 Nov 2025): https://www.uidai.gov.in/images/FAQs_Aadhaar_Data_Vault_03112025_v10.pdf
  - Khaitan & Co note on the revised ADV framework (Dec 2025): https://www.khaitanco.com/sites/default/files/2025-12/ERGO%20-%20Aadhaar%20Data%20Vault%20-%2010%20December%202025.pdf
  - Aadhaar Good Governance Amendment Rules, 2025 (private-entity authentication): https://ssrana.in/articles/aadhaar-authentication-by-private-entities-from-data-privacy-perspective/
  - DigiLocker requester onboarding FAQ: https://www.digilocker.gov.in/assets/FAQ%20DL%20EL_onboarding.pdf; API Setu partners SOP: https://cf-media.api-setu.in/resources/Partners-SOP.pdf
- **App stores:**
  - Google Play Financial Services policy (personal loans, prohibited permissions, 60-day rule, India requirements): https://support.google.com/googleplay/android-developer/answer/9876821
  - Google Play India personal-loan apps and the RBI DLA list (new apps from 30 Oct 2025; existing apps by 28 Jan 2026): https://support.google.com/googleplay/android-developer/answer/16604194
  - Apple App Store Review Guidelines (3.2.2(ix), 5.1.1, 2.5.2): https://developer.apple.com/app-store/review/guidelines/
  - OTA update policy summary (Apple DPLA 3.3; Google Device and Network Abuse): https://bitrise.io/blog/post/what-app-stores-allow-with-ota-updates-apple-and-google-policy-explained
  - WhatsApp Business Messaging Policy (payday loans and debt collection prohibited): https://whatsappbusiness.com/policy/
- **Payments:**
  - Razorpay UPI AutoPay limits (₹15,000 general; ₹1 lakh for lending and investment categories without additional factor): https://razorpay.com/docs/payments/payment-gateway/s2s-integration/recurring-payments/upi
  - Payment Aggregator Directions, 2025 analysis: https://indiacorplaw.in/2025/10/09/decoding-rbis-overhaul-of-the-payment-aggregator-directions/
  - Repayments through PAs with the RE as merchant (industry reading of RBI FAQs): https://www.cashfree.com/blog/rbi-faqs-on-digital-lending-guidelines/
  - Stripe invite-only in India (May 2024): https://www.axios.com/pro/fintech-deals/2024/05/31/stripe-goes-invite-only-in-india; Stripe cross-border services in India: https://support.stripe.com/questions/cross-border-payment-services-in-india
  - PayPal exit from domestic Indian payments (2021): https://www.finextra.com/newsarticle/37425/paypal-quits-competitive-indian-payments-market
- **Technology:**
  - Expo SDK 56 (React Native 0.85, 21 May 2026): https://expo.dev/sdk/56
  - Expo SDK 57 (React Native 0.86, 30 Jun 2026): https://expo.dev/changelog/sdk-57
  - Expo SDK 58 beta (React Native 0.88 RC, 15 Sep 2026; Node 22.13+/24.3+/26+): https://expo.dev/changelog/sdk-58-beta
  - Expo New Architecture guide (mandatory from SDK 55): https://docs.expo.dev/guides/new-architecture.md
  - Expo app integrity (Play Integrity and App Attest): https://docs.expo.dev/versions/v57.0.0/sdk/app-integrity.md
  - Play Integrity API: https://developer.android.com/google/play/integrity/overview
  - Next.js blog (16.2 Mar, 16.3 Aug, 16.4 6 Oct 2026): https://nextjs.org/blog
  - NestJS v12.0.0 release (Node 20.19+ or 22.12+): https://newreleases.io/project/github/nestjs/nest/release/v12.0.0
  - Node.js release status (Node 20 EOL 30 Apr 2026; Node 24 Maintenance LTS from 20 Oct 2026, EOL 30 Apr 2028; Node 26 Active LTS from 28 Oct 2026): https://github.com/nodejs/release#release-schedule and https://nodejs.org/en/about/previous-releases
  - OWASP MASTG releases (v2.0.0, 30 Jun 2026; MASVS v2.1.0): https://github.com/OWASP/mastg/releases
  - OWASP MASWE v1.0.0 (Aug 2026): https://mas.owasp.org/news/2026/08/17/maswe-v100-release/
  - Temporal regions: https://docs.temporal.io/cloud/regions
  - GoRules ZEN: https://docs.gorules.io/reference/nodejs
  - Railway deployment regions: https://docs.railway.com/reference/deployment-regions
  - Surepass API catalogue: https://surepass.io/surepass-id-verification-apis/
  - NSDL APIs: https://nsdl.co.in/API-BP/api_brief.html; CDSL APIs: https://www.cdslindia.com/DP/APIs.html
  - TallyPrime JSON integration: https://help.tallysolutions.com/tally-prime-integration-using-json-1/
  - ReBIT AA specifications: https://api.rebit.org.in/spec/aa
  - Expo SDK support table (Android 7+, iOS 16.4+, targetSdk 36): https://docs.expo.dev/versions/v58.0.0; EAS Update code signing: https://docs.expo.dev/eas-update/code-signing/; @expo/app-integrity (alpha): https://docs.expo.dev/versions/v57.0.0/sdk/app-integrity.md
  - Google Play target API level (API 36 from 31 Aug 2026): https://developer.android.com/google/play/requirements/target-sdk
  - Supabase regions (ap-south-1 is the only India region): https://supabase.com/docs/guides/platform/regions; Data API hardening: https://supabase.com/docs/guides/database/hardening-data-api
  - SMS Retriever app hash: https://developers.google.com/identity/sms-retriever/verify; WebOTP: https://developer.chrome.com/docs/identity/web-apis/web-otp; iOS web push: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
- **Recovery, ADR, collateral and integration (added in v1.1):**
  - RBC Third Amendment Directions, 2026 (RBI/2026-27/230, 6 Aug 2026; in force 1 Jan 2027): https://rbi.org.in/Scripts/NotificationUser.aspx?Id=13672 ; summary of the parallel bank directions: https://taxguru.in/rbi/rbi-issues-comprehensive-commercial-bank-recovery-agent-loan-recovery-conduct-directions-january-2027.html
  - *Shikha Ghosh v Axis Bank* (Del HC DB, 30 Sep 2026): https://www.scconline.com/blog/post/2026/10/16/repeated-appointment-same-arbitrator-4155-cases-delhi-hc-axis-rbi/
  - *L&T Finance v Jai Paras Material Store* (Cal HC, 14 May 2026): https://knallp.com/unilateral-odr-appointment-of-sole-arbitrator-invalid-lt-finance-v-jai-paras-material-store-calcutta-high-court/
  - *Sundaram Finance v Hanuman Prasad* (Raj HC, 2026): https://www.livelawbiz.com/amp/arbitration/high-court/rajasthan-high-court-arbitrator-appointment-agreed-independent-arbitral-institution-not-unilateral-536329
  - *CORE v ECI-SPIC-SMO-MCML (JV)* (SC, 8 Nov 2024): https://www.jsalaw.com/newsletters-and-updates/jsa-prism-dispute-resolution-november-2024/
  - *Sedhram Nilkanth Muglikar v M.R. Makhare* (Bom HC, 2026) on service of arbitration notices: https://www.livelawbiz.com/arbitration/high-court/deemed-service-cannot-cure-defect-in-service-of-arbitration-notices-bombay-high-court-540651
  - Mediation Act, 2023 (Gazette): https://egazette.gov.in/WriteReadData/2023/248775.pdf ; Mediation Council of India established (27 Aug 2026): https://www.scconline.com/blog/post/2026/08/31/new-mediation-council-of-india-established/
  - National Lok Adalat dates 2026 (secondary; verify at nalsa.gov.in): https://oga-prod.angelone.in/news/economy/national-lok-adalat-schedule-march-may-september-and-december-dates-2026-released
  - ODR providers: https://presolv360.com/fees ; https://www.sama.live/rules_and_procedures-2024 ; https://jupiticeodr.com/odr-procedural-rules ; https://www.webnyay.in
  - India Post bulk-customer API SOP (CEPT, v6.1): https://utilities.cept.gov.in/dop/pdfbind.ashx?id=5778 ; IIBF DRA rules: https://www.iibf.org.in/documents/RulesSyllabus/2024/DRA_Rev_030424.pdf
  - CDSL LAS: https://www.cdslindia.com/LAS/LAS.html ; CDSL LAS module communiqué summary (15 Jul 2026): https://teamleaseregtech.com/updates/article/57870/cdsl-introduced-loan-against-securities-las-module-in-easiest/ ; NSDL pledge: https://nsdl.com/services/pledge ; SEBI margin-pledge circular (25 Feb 2020, not an LAS rail): https://www.sebi.gov.in/legal/circulars/feb-2020/margin-obligations-to-be-given-by-way-of-pledge-re-pledge-in-the-depository-system_46082.html
  - MF lien marking (industry descriptions): https://voltmoney.in/blog/lien-marking-mutual-funds ; https://docs.finsire.com/docs/loan-against-mutualfunds-1
  - RBI TReDS Directions, 2026 (RBI/DPSS/2026-27/406, 23 Jun 2026): https://www.rbi.org.in/scripts/NotificationUser.aspx?Id=13526
  - Standards: OpenAPI release notes: https://www.speakeasy.com/openapi/release-notes ; OSCAL 1.2.3 reference: https://pages.nist.gov/OSCAL-Reference/models/v1.2.3/plan-of-action-and-milestones/json-reference/ ; FAPI 2.0: https://openid.net/fapi2-0-final-conformance-tests-available/ ; Idempotency-Key draft: https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-idempotency-key-header
  - GRC tools: https://www.metricstream.com/platform/apis.htm ; https://ibm.com/products/openpages/integrations ; https://pypi.org/project/rsa-archer/
- **Infrabyx ecosystem:**
  - Finbyx Master Build Prompt v1.4 (Part 5 summary; Part 7A Recovery, Litigation and ADR Suite R1–R16; Part 8A requirements and REQ-IDs): docs/ecosystem/finbyx-master-prompt.md
  - Infrabyx Ecosystem Integration Specification v1.0 (canonical events, APIs, data ownership and connectors): docs/ecosystem/infrabyx-integration-spec.md

*End of master prompt.*
