# Appendix O — Legal Policies: Review-Ready Drafts

**Status:** Binding for structure, placeholders, integration points and the non-negotiable positions each policy encodes; **Reference** for wording until qualified counsel signs each policy off. Every policy in this appendix is a **review-ready draft for qualified counsel. It is not final legal advice and must not be published as final** until the reviewer of record (`PLT_LEGAL_REVIEWER`) and the DPO (`PLT_DPO`, for privacy-related policies) approve it in the CMS legal-page workflow (P21).

**Used by:** P01 (consent purposes, Terms acceptance, Aadhaar and DigiLocker notices), P04 (retention, legal hold, nominee access), P06 and P09 (AI labels, AI Use Policy), P08 (eSign, eStamp and Electronic Records Terms), P15 (Consumer Help brand terms and the Fee and Authority Letter), P16 (Marketplace Buyer Terms, Professional Partner Terms), P17 (Refund, Cancellation and Subscription Policy), P20 (Retention and Deletion Schedule, export rights), P21 (legal pages, cookie banner, accessibility statement, trust page), P22 (in-app legal screens, store listings), P23 (security page, responsible disclosure, certification language).

**How to use.** Section O.0 sets the conventions every policy shares: the policy register (`POL-LD-nn`), placeholders, the publication and acceptance workflow, where each policy surfaces in the product, the settings keys proposed for Appendix R, and acceptance tests. Sections O.1 to O.14 are full drafts. Section O.15 gives outlines for the enterprise contract set (DPA, retainer SLA, MSA). Section O.16 lists verification items and open items. Each policy opens with a status box and closes with **build notes** for the coding agent. Text in plain paragraphs is the draft policy wording. Text in *italics prefixed "Drafting note"* is guidance for counsel and the owner and is never published. Tags: **[LAW]** statute or regulator text; **[INTERP]** our reading; **[REC]** recommendation; **[VERIFY: …]** unverified fact (the dependent clause ships only after verification, NN-38); **[COUNSEL]** needs a lawyer's decision; **[TAX MEMO]**; **[OWNER]**. Strip all tags and drafting notes before publication; the CMS pre-publish check (P21) blocks a legal page that still contains `[VERIFY`, `[COUNSEL`, `[OWNER` or "Drafting note".

---

## O.0 Common conventions for all policies

### O.0.1 Policy register

| Policy ID | Policy | Public URL (apps/public) | In-product surface | Acceptance model | Owner |
|---|---|---|---|---|---|
| POL-LD-01 | Privacy Notice | `/legal/privacy` | Sign-up, Privacy Centre (apps/web, mobile), every consent prompt links to its section | Notice acknowledged; consents captured per purpose (P01 consent ledger) | DPO |
| POL-LD-02 | Terms of Use | `/legal/terms` | Sign-up, plan purchase, quarterly reminder | Click-wrap acceptance, version logged | Reviewer of record |
| POL-LD-03 | eSign, eStamp and Electronic Records Terms | `/legal/esign-estamp-terms` | Signing ceremony, eStamp order | Accepted per ceremony by each signer (with the ESP consent screen) | Reviewer of record + `sgn` product owner |
| POL-LD-04 | AI Use Policy and Disclosures | `/legal/ai-use` | Vidhi chat, Drafting Studio, voice, avatars | Session-start disclosure; labels on every output | Reviewer of record + AI lead |
| POL-LD-05 | Refund, Cancellation and Subscription Policy | `/legal/refunds` | Checkout, plan page, cancellation flow | Shown before payment; accepted with order | Billing lead + reviewer |
| POL-LD-06 | Marketplace Terms for Buyers | `/legal/marketplace-buyers` | Service booking, engagement workspace | Accepted per booking | Marketplace lead + reviewer |
| POL-LD-07 | Professional Partner Terms | `/legal/professional-partners` (public summary); full text in partner onboarding | Partner onboarding (apps/delivery) | Signed (eSign) partner agreement | Reviewer + marketplace lead |
| POL-LD-08 | Cookie Policy | `/legal/cookies` | Consent banner, preferences centre | Per-category consent, versioned | DPO |
| POL-LD-09 | Grievance Redressal Policy | `/legal/grievance` | Footer, Help Centre, every app's "Report a problem" | Informational | Grievance Officer |
| POL-LD-10 | Acceptable Use and Content Policy | `/legal/acceptable-use` | Upload, share, message, listing flows | Incorporated in POL-LD-02 | Trust and Safety lead |
| POL-LD-11 | Data Retention and Deletion Schedule (public) | `/legal/retention` | Privacy Centre, account closure, export | Informational | DPO |
| POL-LD-12 | Accessibility Statement | `/accessibility` | Footer, app settings | Informational | Accessibility lead |
| POL-LD-13 | Security and Trust page; Responsible Disclosure Policy | `/trust`, `/trust/responsible-disclosure`, `/.well-known/security.txt` | Footer; enterprise sales packs | Informational | `PLT_SECURITY_OFFICER` |
| POL-LD-14 | Consumer Help Terms of Service + Fee and Authority Letter | `[Consumer Help Brand]` site `/terms`, `/fees` | Consumer Help case intake (`chp`) | Click-wrap + eSigned Fee and Authority Letter per case | Consumer Help reviewer + DPO |
| POL-LD-15 | Data Processing Addendum (outline) | `/legal/dpa` (request form) | Company workspace → Settings → Legal | Signed with the MSA or order form | DPO |
| POL-LD-16 | Retainer SLA template (outline) | Not public | Retainer workflow (P16) | eSigned per retainer | Delivery lead |
| POL-LD-17 | Enterprise MSA (outline) | Not public | Enterprise order flow | eSigned | Reviewer |

Review cycle: privacy, AI and Consumer Help policies every 6 months; others annually; all on any material legal change.

### O.0.2 Placeholders (filled from Super Admin → Legal entities, D-08)

| Placeholder | Meaning | Source field |
|---|---|---|
| `[LawDocs Operating Entity]` | Legal name of the company that operates lawdocs.in | `org.legal_entity.legal_name` |
| `[CIN]` | Corporate Identity Number | `org.legal_entity.cin` |
| `[GSTIN]` | GST registration | `org.legal_entity.gstin` |
| `[Registered Office]` | Registered office address | `org.legal_entity.registered_office` |
| `[Grievance Officer name/email]` | Grievance Officer under the IT Rules 2021 and the E-Commerce Rules 2020 | `org.legal_entity.grievance_officer` |
| `[DPO]` | Data Protection Officer (or the person answering privacy questions under DPDP s.8(9)) — name, email, postal address | `org.legal_entity.dpo` |
| `[Nodal Contact]` | 24×7 contact for orders of courts and government agencies | `org.legal_entity.nodal_contact` |
| `[Consumer Help Brand]` | Brand of the separate consumer-help business (D-06) | `chp.brand.name` |
| `[Consumer Help Entity]` | Legal entity that runs `[Consumer Help Brand]` (separate CIN, GSTIN, Grievance Officer, DPO) | `chp.brand.legal_entity_ref` |
| `[Effective Date]` | Date this version takes effect | CMS version record |
| `[Version]` | Semantic version of the policy (major = material change) | CMS version record |
| `[Seat City]` | Seat of arbitration and exclusive court jurisdiction for business customers | `web.legal.dispute_seat_city` [OWNER] |
| `[Support Email]` / `[Support Phone]` | Public support channels (one public number — R5) | Brand profile |

A placeholder left empty blocks publication (P21 pre-publish check).

### O.0.3 Status box format

Every policy starts with this table. The values shown in each policy are the draft defaults.

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-nn / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Role accountable for content |
| Counsel review required | Yes — scope of review |
| Applicable law | Principal instruments |
| Related codes | NN-xx, D-xx, CH-xx, LG-xxx |

### O.0.4 Publication, versioning and acceptance (binding)

1. **Legal pages are CMS content** (NN-30): versioned, effective-dated, maker-checker published (maker `PLT_CONTENT_EDITOR` or `OPS_CONTENT_PUBLISHER`; checker `PLT_LEGAL_REVIEWER`; privacy-related pages also need `PLT_DPO`). Publishing never needs a code release.
2. **Material change** (a major version) triggers: (a) a notice to all affected users at least `web.legal.material_change_notice_days` (default 30) days before the effective date, except where a law or a security need requires a shorter period; (b) re-acceptance at next sign-in for POL-LD-02, -03, -05, -06, -07 and -14; (c) fresh consent for any **new purpose** in POL-LD-01 — a new purpose is never covered by an old consent (DPDP s.6(1) [LAW]).
3. **Acceptance record:** `iam.policy_acceptance` (user, policy ID, version, language, channel, timestamp, IP, device, page hash). Acceptance is audit-ledgered (NN-45) and exported in `99 System Data/policy_acceptances.csv` (NN-11).
4. **Change log:** every public legal page shows "Last updated", a version history and a plain-language summary of changes.
5. **Languages:** English is the master text. Hindi and the D-07 launch languages are published as reviewed translations, labelled "Translation. If there is a conflict, the English text prevails, except where the law requires otherwise." The privacy notice must be available in English or any Eighth-Schedule language at the user's choice (DPDP s.5(3) [LAW] [VERIFY: sub-section]); untranslated languages show the English text with a request link.
6. **Quarterly reminder:** users are reminded of the Terms, Privacy Notice and Acceptable Use Policy at the interval the IT Rules require (R3 LG-077 reports three months from 20 Feb 2026 [VERIFY]); setting `web.legal.terms_reminder_interval_months`.
7. **Accessibility and fairness:** WCAG 2.2 AA pages with a table of contents and tagged PDF/A download; no pre-ticked consents and no consent bundled with Terms acceptance (NN-50).

### O.0.5 Proposed settings (register in Appendix R)

| Key | Tier | Type | Default | Changed by | Maker-checker |
|---|---|---|---|---|---|
| `web.legal.entity_profile_ref` | BRAND | ref | LawDocs entity | `PLT_SUPER_ADMIN` | Y |
| `web.legal.material_change_notice_days` | PLATFORM | int | 30 | `PLT_LEGAL_REVIEWER` | Y |
| `web.legal.reaccept_on_major_version` | PLATFORM | bool | true (Locked) | — | — |
| `web.legal.terms_reminder_interval_months` | PLATFORM | int | 3 [VERIFY] | `PLT_LEGAL_REVIEWER` | Y |
| `web.legal.policy_languages` | BRAND | list | `en`, `hi` | `PLT_CONTENT_EDITOR` | Y |
| `web.legal.supplement.gdpr.enabled` | BRAND | bool | false | `PLT_DPO` | Y |
| `web.legal.supplement.ccpa.enabled` | BRAND | bool | false | `PLT_DPO` | Y |
| `web.legal.dispute_seat_city` | BRAND | string | `[Seat City]` [OWNER] | `PLT_LEGAL_REVIEWER` | Y |
| `web.legal.odr.enabled` | BRAND | bool | true | `PLT_LEGAL_REVIEWER` | Y |
| `web.legal.odr.institution_list` | BRAND | list | institutions not affiliated with Infrabyx Group + any affiliated institution flagged "Group affiliate" | `PLT_LEGAL_REVIEWER` | Y |
| `bil.refunds.new_subscription_window_days` | PLAN | int | 7 [OWNER] | Billing lead | Y |
| `bil.credits.validity_months` | PLAN | int | 12 | Billing lead | Y |
| `bil.credits.expiry_reminder_days` | PLATFORM | list | 30, 7 | Billing lead | Y |
| `chp.fees.success_fee.enabled` | BRAND | bool | false (Locked until counsel opinion attached) | `PLT_LEGAL_REVIEWER` + checker | Y |
| `chp.fees.success_fee.cap_pct` | BRAND | decimal | 10 | `PLT_LEGAL_REVIEWER` | Y |
| `web.cookies.analytics.enabled` | BRAND | bool | true (loads only after consent) | `PLT_DPO` | Y |
| `web.cookies.marketing.enabled` | BRAND | bool | false | `PLT_DPO` | Y |
| `eng.disclosure.rewards.enabled` | PLATFORM | bool | false | `PLT_SECURITY_OFFICER` | Y |

### O.0.6 Events, errors, help keys and export-map entries

- **Events (internal):** `in.lawdocs.web.LegalPolicyVersionPublished.v1`, `in.lawdocs.web.LegalPolicyMaterialChangeScheduled.v1`, `in.lawdocs.iam.PolicyVersionAccepted.v1`. Consent events stay with P01 (`kyc`/`iam` consent ledger); this appendix does not create them.
- **Errors (proposed range `LD-WEB-090`–`LD-WEB-099`):** `LD-WEB-090` "Please review and accept the updated Terms to continue" · `LD-WEB-091` "This legal page cannot be published: placeholders or review tags remain" · `LD-WEB-092` "This policy version needs reviewer and DPO approval" · `LD-WEB-093` "Translation not yet reviewed; showing English".
- **Help keys:** `hlp.web.data_fiduciary`, `hlp.web.data_processor`, `hlp.web.consent_manager`, `hlp.web.data_protection_board`, `hlp.web.grievance_officer`, `hlp.web.legitimate_use`, `hlp.sgn.esp`, `hlp.sgn.asp`, `hlp.sgn.stamp_before_sign`, `hlp.sgn.s63_certificate`, `hlp.ai.ai_draft_label`, `hlp.ai.qualified_review`, `hlp.mkp.platform_fee`, `hlp.mkp.reserved_service`, `hlp.chp.authorised_representative`, `hlp.bil.credit_expiry`.
- **Export map:** `xpt.export_map` record types `policy_acceptance` and `consent_artefact` → `99 System Data (CSV and JSON)/Legal and Consent/` (company) and `99 System Data/Legal and Consent/` (individual); the accepted policy PDFs for each version are included once per export.

### O.0.7 Acceptance tests (`tests/acceptance/p21/legal_policies.feature`)

```gherkin
@APPO-AT-01 @NN-50
Scenario: Consent is never bundled with Terms acceptance
  Given a new visitor on the sign-up screen
  When the sign-up form renders
  Then the Terms acceptance control and each optional consent are separate unticked controls
  And sign-up succeeds with all optional consents declined

@APPO-AT-03
Scenario: Major version forces re-acceptance
  Given Terms of Use version 2.0.0 is effective today and the user accepted 1.4.0
  When the user signs in
  Then the user sees the change summary and must accept 2.0.0 before continuing
  And an audit entry records the acceptance with version and page hash

@APPO-AT-04 @NN-04
Scenario: Aadhaar section of the Privacy Notice matches system behaviour
  Given the Privacy Notice states that full Aadhaar numbers are never stored
  When a document containing a 12-digit Aadhaar number is uploaded
  Then the derived OCR text stores only the masked form "XXXX XXXX 1234"

@APPO-AT-05 @NN-21
Scenario: Professional Partner Terms offered to an advocate contain no fee-share clause
  Given a partner applicant with profession "ADVOCATE"
  When the partner agreement is generated
  Then the agreement contains clause set "PPT-ADV" and excludes commission, listing-fee and referral clauses

@APPO-AT-06 @NN-23
Scenario: Consumer Help terms render under the Consumer Help entity
  Given a user on the [Consumer Help Brand] site
  When the user opens Terms of Service
  Then the operator, CIN, Grievance Officer and DPO shown are those of the Consumer Help entity

@APPO-AT-07 @NN-14
Scenario: AI disclosure at session start
  When a user opens a new Vidhi chat or voice session
  Then the first message discloses that the user is interacting with an AI system and links to POL-LD-04

@APPO-AT-08 @NN-50
Scenario: Renewal terms shown before payment
  Given a user buying the Pro plan with auto-renewal
  When the checkout summary renders
  Then it shows renewal date, renewal price incl. GST, how to cancel and a link to POL-LD-05 before the Pay button
```

---

## O.1 Privacy Notice (POL-LD-01)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-01 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | `[DPO]` |
| Counsel review required | Yes — DPDP Act 2023 and Rules 2025 alignment; SPDI Rules 2011 interim compliance; roles analysis (fiduciary/processor) per product; legitimate-use reliance; GDPR/CCPA supplements |
| Applicable law | Digital Personal Data Protection Act 2023 (ss.4–17, 33); DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025); IT Act 2000 s.43A and SPDI Rules 2011 (until 13 May 2027); Aadhaar Act 2016 ss.8A, 29; DigiLocker Requester Terms (2 Jun 2025); IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 as amended; CERT-In Directions 28 Apr 2022; GDPR and CCPA (supplements, by jurisdiction) |
| Related codes | NN-04, NN-11, NN-15, NN-19, NN-23, NN-24, NN-25, NN-26, NN-27, NN-32, NN-42; D-06, D-08, D-14; CH-02, CH-15, CH-16, CH-18; LG-021–031, LG-036–038, LG-061–072, LG-075, LG-077, LG-079, LG-084–086 |

*Drafting note — commencement.* The DPDP Act's core duties (ss.3–17) and Rules 3, 5–16, 22–23 apply from 13 May 2027; Rule 4 (consent managers) from 13 Nov 2026 (LG-061, LG-062) [VERIFY: whether MeitY has accelerated these dates]. Until 13 May 2027 IT Act s.43A and the SPDI Rules 2011 apply (LG-075). This notice is written to satisfy both regimes now (NN-26). Section 20 is the SPDI statement. Do not tell users that DPDP rights are "legally available" before commencement; say "we give you these rights now".

### 1. Who we are and what this notice covers

`[LawDocs Operating Entity]` (CIN `[CIN]`, registered office `[Registered Office]`) ("**LawDocs**", "**we**", "**us**") operates the website lawdocs.in, the web application at my.lawdocs.in, the LawDocs mobile apps and related services (together, the "**Platform**").

This notice explains how we process your personal data, why, who we share it with, how long we keep it, and how you can exercise your rights. It applies to visitors, account holders, people invited to negotiate or sign a document ("counterparties"), professionals who join our marketplace, and people who contact us.

**Our role depends on the service.**

| Situation | Who decides why and how your data is processed | Our role |
|---|---|---|
| You use LawDocs for yourself (Personal workspace) | LawDocs | **Data Fiduciary** |
| You visit our website, contact us, or buy a service from us | LawDocs | Data Fiduciary |
| Your employer or another organisation gives you access to its Company workspace | That organisation | **Data Processor** for the organisation's content; Data Fiduciary for your login and security data |
| Someone invites you to review or sign a document | The person or organisation that invited you, for the document's content | Processor for the document's content; **Data Fiduciary for the signing evidence** we must keep as the eSign application service provider |
| You engage a professional through our marketplace | You and the professional, for the advice and work product | See section 9 and POL-LD-07 [COUNSEL] |
| You use `[Consumer Help Brand]` | `[Consumer Help Entity]`, a separate business | Not covered by this notice — see that brand's own privacy notice |

*Drafting note.* DPDP s.2(i) defines a Data Fiduciary as a person who, alone or with others, determines the purpose and means of processing; s.8(2) lets a fiduciary engage a processor only under a valid contract [LAW]. The roles above are our reading (LG-072) [INTERP] [COUNSEL]. When we act as processor, the organisation's privacy notice governs; we help it answer your requests (O.15 DPA).

### 2. This notice at a glance

| Question | Short answer |
|---|---|
| Do you sell my data? | No. We never sell or rent personal data, and we do not share it for third-party advertising. |
| Do you use my documents to train AI? | No. Your data is never used to train AI models — ours or anyone else's (section 8). |
| Where is my data stored? | In India (AWS Mumbai, with disaster recovery in Hyderabad). Exceptions are listed in section 10. |
| Do you store my Aadhaar number? | No. We never store your full Aadhaar number, biometrics, OTPs or e-KYC files. We mask Aadhaar numbers in documents you upload (section 5). |
| Can I download or delete my data? | Yes, any time, from Settings → Privacy Centre, subject to legal retention duties (sections 11 and 13). |
| Who sees my documents? | Only people you or your organisation give access to, and our staff only under a time-bound access grant you approve, or where the law requires (section 9). |
| How do I complain? | Contact `[DPO]` or the Grievance Officer `[Grievance Officer name/email]`. If you are not satisfied, you may approach the Data Protection Board of India (section 17). |

### 3. Personal data we process

| Category | Examples | Source |
|---|---|---|
| Identity and contact | Name, email, mobile number, postal address, preferred language | You |
| Account and security | Login identifiers, passkey public keys, MFA settings, session records, device identifiers, IP address, sign-in history | You; your device |
| Identity verification (optional) | Result of Aadhaar offline verification (name, age-over-18 flag or year of birth, photograph only where a signing identity must be matched, last 4 digits of Aadhaar); PAN (displayed masked); DigiLocker document references (URI, issuer, document type, verification result) | You, the Aadhaar App or QR you present, DigiLocker with your consent |
| Business verification | Company name, CIN/LLPIN, GSTIN, registered office, director names and DINs, authorised-signatory details | You; Entity Locker with consent; licensed data vendors that warrant lawful sourcing |
| Documents and content | Drafts, agreements, uploaded files, OCR text, translations, notes, messages, comments, matter and case details, trademark data, vault folders | You; people you collaborate with |
| Third-party data inside your content | Names, addresses and other details of counterparties, witnesses, family members, employees, opposing parties | You (you must have a lawful basis to share it — section 15) |
| eSign evidence | Consent text version you accepted, signer name and certificate details returned by the eSign Service Provider (ESP), transaction ID, document hash, timestamps, IP address, device details, response codes | You; the ESP |
| eStamp details | Stamp certificate number (UIN), State, article, amount, first party, second party, purchaser, verification and lock status | You; the authorised stamp channel |
| Payments and invoices | Billing name, GSTIN, billing address, payment status, transaction reference, refund records. **We never receive or store card numbers or CVV** | You; Razorpay |
| Marketplace engagements | Service ordered, professional engaged, milestones, deliverables, messages, fees | You; the professional |
| AI interactions | Prompts, files you give Vidhi, outputs, citations, feedback, review status | You; Vidhi |
| Support and grievances | Tickets, call recordings (with notice), correspondence, complaint outcomes | You |
| Usage and cookies | Pages viewed, features used, errors, approximate location from IP, cookie identifiers (only with consent for non-essential cookies — POL-LD-08) | Your device |
| Marketing preferences | Channels you opted into, opt-outs | You |
| Professionals | Enrolment or membership numbers, certificate of practice, State Bar Council or Institute, qualifications, practice areas, languages, payout account (via Razorpay), tax details | The professional; regulators' public registers |

We do not ask for biometric, health, caste, religion, sexual-orientation or political data. If documents you store contain such data (for example, an insurance claim or a will), we protect them under our highest internal sensitivity class.

### 4. Why we process your data and our legal basis

DPDP s.4 permits processing only for a lawful purpose, either with your **consent** (s.6) or for a **legitimate use** listed in s.7 [LAW]. "Contract" is not a separate ground under DPDP; where a service needs data, we ask for your consent to that purpose and tell you what happens if you refuse.

| ID | Purpose | Data used | Basis | Optional? | If you withdraw |
|---|---|---|---|---|---|
| PUR-01 | Create and secure your account; sign-in, MFA, passkeys | Identity, contact, account and security | Consent | Required to use the Platform | Account is closed (section 13) |
| PUR-02 | Verify your identity (Aadhaar offline verification, DigiLocker, PAN) when a feature needs it | Verification data | Consent, per verification | Optional unless the feature needs a verified identity; alternatives always offered | Verified badge removed; verification-dependent features stop |
| PUR-03 | Draft, store, organise, search, share and export your documents (Legal Vault, Drafting Studio, contract tools) | Documents and content | Consent | Core service | Stored content is deleted after the export window (section 13) |
| PUR-04 | Run signing ceremonies through an ESP and keep the legally required evidence | eSign evidence | Consent per ceremony; legal obligation for evidence retention (s.7 [VERIFY: clause]) | Optional per document | Future ceremonies stop; past evidence is kept for the retention period (section 11) |
| PUR-05 | Procure stamp duty through authorised channels as your agent | eStamp details, party details | Consent per order | Optional | Order cancelled subject to POL-LD-05 |
| PUR-06 | Take payments, issue GST invoices, process refunds | Payments and invoices | Consent; legal obligation for tax records | Required for paid services | Paid services stop; tax records kept |
| PUR-07 | Vidhi AI assistance (drafting, review, summaries, OCR, translation) | Prompts, files you select | Consent (separate AI consent) | Optional; you can turn AI off | AI features stop; your content is not affected |
| PUR-08 | Connect you with a professional you choose and share the case file you select | Marketplace data, selected documents | Consent per engagement | Optional | Sharing for new engagements stops; the professional's own records remain theirs (section 9) |
| PUR-09 | Share specific data with an Infrabyx Group product you choose to use (for example, sending a signed agreement to your LawDocsComply workspace) | Only the items you pick | Separate consent per destination and purpose | Optional; never a condition of service | Sharing stops; data already shared is governed by the receiving product's notice |
| PUR-10 | Security, fraud and abuse prevention, audit trails, incident response | Account, security, usage, logs | Legitimate use where law requires security safeguards [INTERP]; consent | Not optional while you use the Platform | — |
| PUR-11 | Comply with law: CERT-In log retention, tax and accounting records, court and government orders, IT Rules | As the law requires | Legal obligation (s.7 [VERIFY: clause]) | Not optional | — |
| PUR-12 | Support, grievances and service messages (renewals, security alerts, policy changes) | Contact, support data | Consent; legal obligation for grievance handling | Service messages cannot be switched off while you hold an account | — |
| PUR-13 | Marketing by email, SMS, WhatsApp or calls about our products | Contact, marketing preferences | Separate opt-in consent per channel | Optional | We stop within 48 hours [REC]; your number goes on our suppression list |
| PUR-14 | Analytics and product improvement using aggregated or de-identified data | Usage data | Consent (cookies — POL-LD-08) | Optional | Analytics cookies stop |
| PUR-15 | Nominee and legacy access to your vault (if you set it up) | Nominee details, release evidence | Consent; your nomination right (s.14) | Optional | Nomination removed |

*Drafting note.* Counsel to confirm (a) whether PUR-03/PUR-04 may rely on s.7(a) "voluntarily provided for a specified purpose" [VERIFY: clause letter]; (b) the legal-obligation basis for eSign evidence (LG-008). P01 stores one consent artefact (`cns_`) per purpose with notice version and language.

### 5. Aadhaar: what we do and never do

1. **We never use Aadhaar to log you in.** You sign in with a mobile or email OTP, a passkey, a password with MFA, or your organisation's single sign-on (NN-03).
2. **Identity verification is offline and optional.** If a feature needs a verified identity, you may verify through the Aadhaar App, a secure QR code or e-Aadhaar under Aadhaar Act s.8A (offline verification) [LAW], or use an alternative (DigiLocker, PAN with name match, assisted video verification, or a Class 3 DSC). We tell you, before you share, what data will be shared, why, and the alternatives (s.8A(3)) [LAW].
3. **What we keep:** only the attributes the feature needs (for example, name, whether you are over 18, and — only where a signer must be matched — your photograph) and the **last four digits** of your Aadhaar number. We do not collect, use or store your full Aadhaar number or biometrics (s.8A(4)) [LAW]; keeping only a masked last-four reference is our reading of that bar [INTERP; COUNSEL — W.9 LA-29].
4. **Masking in your documents:** when you upload a document that shows an Aadhaar number, we mask the first eight digits in every text version we create (OCR, search index, previews, AI inputs) before storing it, and we never display an unmasked Aadhaar number publicly (s.29(4)) [LAW]. Your original file is stored as you uploaded it, encrypted, and is visible only to people you allow; you can choose to replace it with a masked copy.
5. **Aadhaar eSign** is performed by a licensed ESP, not by LawDocs. The ESP authenticates you with UIDAI; we receive only the signed document, the certificate and the response codes (section 7).
6. **Revoke Aadhaar data:** Privacy Centre → Identity → "Revoke Aadhaar data" deletes stored Aadhaar-derived attributes and gives you an acknowledgement, except where they form part of a signing record we must keep (LG-028).

### 6. DigiLocker and Entity Locker

When you choose to fetch a document from DigiLocker (or, for organisations, Entity Locker), we ask for your consent each time and tell you the reason. We store the **document reference (URI), its metadata and the verification result**, not a duplicate copy, unless you choose to save a copy in your vault for a purpose you record — and only as DigiLocker's terms allow (NN-42) [VERIFY: NeGD position on user-directed saving]. Documents fetched by URI show a "verified with issuer" badge; we re-check the reference when you display or export it. We do not share our DigiLocker integration with any other company, including Infrabyx Group companies (DigiLocker Requester Terms cl.17, LG-038) [LAW].

### 7. eSign and electronic records

Electronic signatures on LawDocs are created by an **eSign Service Provider** (a Certifying Authority licensed by the Controller of Certifying Authorities) under IT Act s.3A and the Second Schedule [LAW], or with your own Class 3 Digital Signature Certificate. LawDocs acts as the **Application Service Provider (ASP)**: we obtain your consent, prepare the document hash and receive the signature. We keep the consent record, the request and response, the transaction ID, the document hash, timestamps, IP address and device details as an **evidence pack**. The eSign rules require the ASP to keep consent and logs (LG-007, LG-008) [LAW], and the evidence pack lets you prove the signature in court (Bharatiya Sakshya Adhiniyam 2023 s.63 certificate support — POL-LD-03). We retain eSign evidence for at least **seven years** after the later of signing and account closure, or longer where a limitation period or legal hold requires (section 11).

### 8. Artificial intelligence (Vidhi)

1. Vidhi uses Anthropic's Claude models. **Content that contains personal or confidential data is processed only through an approved in-region endpoint in India** (Amazon Bedrock India; inference stays in India) with zero data retention by the model provider where available. Public, non-personal content (for example, our help articles) may be processed through Anthropic's own API (NN-15, D-14) [VERIFY: Bedrock India retention terms and the AWS human-review exception for flagged content — R4].
2. **No training on your data.** We do not use your content, prompts or outputs to train or fine-tune any AI model, and our contracts prohibit our AI providers from doing so.
3. Before data goes to a model, our gateway removes or masks secrets, OTPs and Aadhaar numbers (NN-32). Vidhi retrieves only documents you are permitted to see.
4. AI outputs are labelled. Documents Vidhi drafts for you as an individual are marked **"AI draft — not reviewed by a professional"** until a qualified reviewer approves them (POL-LD-04).
5. Vidhi does not make decisions about you that produce legal effects. It assists; people decide.
6. You can switch AI features off (Settings → AI and privacy). Your organisation's administrator may also switch them off for a Company workspace.

### 9. Who we share your data with

We share personal data only for the purposes in section 4, only as much as needed, and under contracts that bind the recipient to protect it.

| Recipient | Why | What | Safeguards |
|---|---|---|---|
| People you invite (counterparties, witnesses, collaborators, your family members or delegates) | To negotiate, sign or manage documents with them | What you choose to share | You control sharing; they see only shared versions (NN-37) |
| eSign Service Providers (licensed CAs) and eSign aggregators | To create electronic signatures | Signer name, mobile/email, document hash, consent | CCA-licensed; contract; India processing |
| Authorised stamp channels (SHCIL as Central Record-keeping Agency, Authorised Collection Centres, State e-stamp or franking routes) | To buy stamp duty on your behalf | Party names, State, article, consideration, amount | Authorised channels only (NN-08) |
| Professionals you engage (advocates, CAs, CSs, tax practitioners) | To deliver the service you booked | The case file and documents you select | Engagement terms; professional confidentiality; scoped, time-bound access (NN-17) |
| Infrabyx Group companies (LawDocsComply, Finbyx, Udofin, Equator Resolution, the group Operations Hub) | Only when you ask us to send specific data to a group product you use, or — for the Operations Hub — commercial records (orders, invoices) and aggregated metrics | Only the items you pick; the Operations Hub receives no documents, matters, cases or credentials | Separate consent per destination and purpose; every transfer logged in a sharing ledger you can see; regulated feeds never flow by default (CH-16, NN-19, NN-24) |
| Service providers (processors) — hosting, storage, email, SMS/WhatsApp, payments, AI, OCR, customer support tools, security | To run the Platform | As needed for their task | Contract under DPDP s.8(2); sub-processor list on `/trust`; changes announced 30 days ahead for business customers |
| Razorpay (payment aggregator) | Payments, subscriptions, refunds, marketplace payouts | Billing contact, payment status | RBI-authorised PA; we never see card data |
| Courts, regulators, law-enforcement and government agencies | When the law requires, or under a valid order | What the order requires | We check legal validity; we notify you unless prohibited |
| A successor business | If we merge, are acquired or transfer the business | Data needed to continue the service | Same protections; notice to you |

**`[Consumer Help Brand]` is separate.** Data you give `[Consumer Help Brand]` is held by `[Consumer Help Entity]` in a separate system and is never shared with LawDocsComply, Finbyx, Udofin or Equator Resolution, or with any lender or insurer client of the Infrabyx Group (NN-23).

We do not sell personal data. We do not share it with advertisers. Our public pages may show contextual sponsored content only if that feature is switched on; it never uses your personal data (NN-35).

### 10. Where we store your data and cross-border transfers

We store and process your data in India (AWS ap-south-1 Mumbai, disaster recovery in ap-south-2 Hyderabad) (NN-25). We transfer personal data outside India only (a) where you direct it (for example, you share a document with someone abroad or engage a professional located abroad), (b) where a sub-processor listed on `/trust` with a recorded transfer assessment needs it, or (c) where you use an optional integration you connect (for example, your own Google Drive). We will not transfer data to any country the Central Government restricts under DPDP s.16(1) [LAW], and we follow stricter sector rules where they apply (s.16(2)) [LAW].

### 11. How long we keep your data

We keep personal data only as long as the purpose needs it or the law requires, then erase it (DPDP s.8(7)) [LAW]. Before erasing data because you have been inactive, we give you at least 48 hours' notice so you can sign in or export (we apply this voluntarily — DPDP Rules 2025 Rule 8 [LAW] [VERIFY: Third-Schedule classes]). The full schedule is POL-LD-11. Key periods:

| Data | Retention |
|---|---|
| Account profile | While the account is open; then 90 days for export, then deletion |
| Vault documents and drafts | Until you delete them or close your account (plus 90-day export window), unless a legal hold applies |
| eSign evidence packs and signing logs | At least 7 years after the later of signing and account closure (LG-008, LG-092) |
| Invoices and payment records | 8 years from the end of the financial year (Companies Act 2013 s.128(5); CGST Act s.36) [VERIFY] |
| Security and access logs | 400 days in India (≥ 180 days CERT-In; ≥ 1 year DPDP Rules) (LG-065, LG-079) |
| Aadhaar-derived attributes | Until the verification purpose ends or you revoke, except where part of a signing record |
| Marketing consent records | Until withdrawn, then a minimal suppression record |

### 12. How we protect your data

We use encryption in transit and at rest, per-tenant encryption keys, immutable storage for originals and signed files, role-based and attribute-based access control, multi-factor authentication for staff, maker-checker for sensitive actions, append-only audit trails, India-resident logging, vulnerability testing, and staff training. Our staff access a customer's workspace only through an access grant the customer approves; emergency access needs two approvals and is reported to the customer within 24 hours (NN-17). Details are on `/trust` (POL-LD-13).

If a personal data breach occurs, we inform affected users and the Data Protection Board without delay, and give the Board a detailed report within 72 hours (DPDP Rules 2025 Rule 7) [LAW]; we report cyber incidents to CERT-In within 6 hours (CERT-In Directions 2022) [LAW]; and where DigiLocker data is involved, we inform NeGD within 24 hours (LG-038) [LAW].

### 13. Your rights and how to exercise them

| Right | What it means | How |
|---|---|---|
| Information and access (DPDP s.11) | A summary of your personal data we process, the processing activities, and the identities of fiduciaries and processors we shared it with | Privacy Centre → "Download my data" or "Request a summary" |
| Correction, completion, updating (s.12) | Fix inaccurate or incomplete data | Edit in your profile, or request through the Privacy Centre |
| Erasure (s.12) | Delete data no longer needed for the purpose, unless the law requires us to keep it | Privacy Centre → "Delete data" or "Close account" |
| Withdraw consent (s.6(4)) | As easy as giving it; withdrawal does not affect processing already done | Privacy Centre → Consents, one tap per purpose |
| Grievance redressal (s.13) | Have your complaint handled by us first | Section 17 |
| Nominate (s.14) | Name a person to exercise your rights if you die or become incapable | Privacy Centre → Nominee |
| Portability [REC] | Export everything in standard formats (folders, DOCX, XLSX, PDF, CSV, JSON) | Settings → Export (no staff help needed — NN-11) |

**Timelines.** We acknowledge requests within 24 hours and aim to complete them within 30 days. The outer limit we commit to is 90 days (DPDP Rules 2025 Rule 14(3)) [LAW] [VERIFY]. **Verification.** We confirm your identity before acting, using your signed-in session or a one-time code; we do not ask for your Aadhaar number. **Limits.** We may refuse or limit erasure where we must keep data by law (eSign evidence, tax records, logs), where a legal hold applies, or where an exemption under DPDP s.17 applies (for example, processing necessary to enforce a legal right or claim) [LAW] [COUNSEL]. Deleting your copy of a shared or signed document does not delete the copies other parties hold.

**Company workspaces.** If your organisation controls the workspace, we pass your request to its administrator and help it respond.

### 14. Duties you have

DPDP s.15 requires you not to impersonate anyone, not to suppress material information when providing data for an identity document, not to register false or frivolous complaints, and to provide only verifiably authentic information when exercising correction or erasure [LAW]. When you upload documents containing other people's data, you confirm you have a lawful basis to do so.

### 15. Consent managers

From the date DPDP Rule 4 applies (13 November 2026 per the commencement notification [VERIFY]), you may give, manage, review and withdraw your consent to us through a **consent manager** registered with the Data Protection Board (DPDP s.6(7)–(9)) [LAW]. We will accept consent artefacts from registered consent managers once our integration is live and will publish the list on this page. LawDocs is not itself a consent manager.

### 16. Children and persons with disabilities

LawDocs accounts are for **adults (18 and over)**; a minor cannot enter into a binding contract (Indian Contract Act 1872 s.11) [LAW]. We do not knowingly process a child's personal data without **verifiable consent of a parent or lawful guardian** (DPDP s.9; Rule 10) [LAW]. A guardian may manage documents for a minor or ward through a guardian workspace after we verify guardianship (for example, through a DigiLocker age-and-identity token where available — LG-040). We do not track, behaviourally monitor or target advertising at children (s.9(3)) [LAW]. For a person with a disability who has a lawful guardian, we obtain the guardian's verifiable consent (Rule 11) [LAW].

### 17. Grievances and the Data Protection Board

**Data Protection Officer:** `[DPO]`. **Grievance Officer:** `[Grievance Officer name/email]`, `[Registered Office]`. We acknowledge your complaint within 24 hours and resolve it within the period in POL-LD-09 (currently 7 days for complaints under the IT Rules, and no later than 90 days for DPDP rights requests) [VERIFY]. If you are not satisfied, you may complain to the **Data Protection Board of India** after using our grievance process (DPDP s.13(3)) [LAW]; an appeal against the Board's decision lies to the Appellate Tribunal (TDSAT) (s.29) [LAW] [VERIFY: period].

### 18. Changes to this notice

We notify material changes at least 30 days ahead (unless law or security requires otherwise) and ask for fresh consent for any new purpose. Earlier versions are in the version history.

### 19. Languages

This notice is available in English and in the Indian languages listed on this page. You may ask for it in any language in the Eighth Schedule to the Constitution [LAW] [VERIFY: DPDP s.5(3)]; we will provide a reviewed translation.

### 20. Statement under the IT Act 2000 and SPDI Rules 2011 (applies until 13 May 2027)

Until IT Act s.43A is omitted (13 May 2027), passwords, financial information (such as bank details) and biometric information are "sensitive personal data or information" under the SPDI Rules 2011 r.3 [LAW] [VERIFY: rule numbers]. We collect them only with your consent, for the purposes above, protect them with reasonable security practices, and disclose them only as this notice describes. You may review and correct them, and withdraw consent, as set out in section 13.

### Supplement A — European Union and United Kingdom (shown only when `web.legal.supplement.gdpr.enabled` is on and the visitor is identified as EU/UK-resident)

1. **Controller:** `[LawDocs Operating Entity]`. **EU/UK representative:** `[name/address, if appointed under GDPR Art. 27]` [COUNSEL: needed once we offer services to people in the EU — LG-084].
2. **Legal bases (GDPR Art. 6(1)):** contract (account, documents, signing, payments); legal obligation (tax, eSign evidence); legitimate interests (security, fraud prevention, service improvement with de-identified data — you may object); consent (marketing, non-essential cookies, AI features, group sharing).
3. **Transfers:** your data is processed in India, which has no EU adequacy decision [VERIFY]. We use the European Commission's Standard Contractual Clauses (2021/914) with a transfer impact assessment, and the UK Addendum/IDTA for UK data.
4. **Rights (Arts. 15–22):** access, rectification, erasure, restriction, portability, objection, and not to be subject to solely automated decisions (we make none). Response within one month, extendable by two months.
5. **Complaints:** you may complain to your local supervisory authority.

### Supplement B — California (shown only when `web.legal.supplement.ccpa.enabled` is on)

1. Categories of personal information collected in the last 12 months: identifiers; customer records; commercial information; internet activity; professional information; sensitive personal information limited to account log-in credentials (used only to provide the service).
2. We do **not sell or share** personal information (as "sell" and "share" are defined in Cal. Civ. Code §1798.140) and have not done so in the last 12 months. We honour Global Privacy Control signals.
3. Rights: to know, delete, correct, opt out of sale/sharing, and limit use of sensitive personal information; to non-discrimination. Submit through the Privacy Centre or `[DPO]`; authorised agents accepted with written permission.
*Drafting note.* CCPA applies only above its thresholds (LG-086) [VERIFY: current CPI-adjusted figure]; keep the supplement OFF until counsel confirms a trigger (CH-18).

**Build notes (O.1).** (a) Each `PUR-nn` row is a consent purpose in the P01 ledger with the same ID; the notice section anchor (`#pur-07`) is stored on the artefact. (b) Privacy Centre (SCR in P01/P20) exposes every action in section 13 with ≤ 3 taps from Settings. (c) The "at a glance" table renders above the fold on mobile. (d) Section 9's sub-processor list is generated from the sub-processor register (P23) — never typed. (e) The group-sharing ledger (PUR-09) is visible in Privacy Centre → Sharing. (f) Supplements render only under their flags and jurisdiction detection plus a manual "I live in the EU/UK/California" link. (g) Help keys: `hlp.web.data_fiduciary`, `hlp.web.legitimate_use`, `hlp.web.consent_manager`, `hlp.web.data_protection_board`.

---
## O.2 Terms of Use (POL-LD-02)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-02 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Reviewer of record (`PLT_LEGAL_REVIEWER`) |
| Counsel review required | Yes — platform role and Advocates Act boundary; intermediary status and safe harbour; consumer-facing liability caps (unfair contract terms); dispute clause and ODR option; GST pure-agent wording [TAX MEMO] |
| Applicable law | Indian Contract Act 1872; IT Act 2000 ss.2(1)(w), 10A, 79; IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021 as amended (incl. Amendment Rules 2026); Consumer Protection Act 2019 and Consumer Protection (E-Commerce) Rules 2020; Advocates Act 1961 ss.29, 33; Arbitration and Conciliation Act 1996; Mediation Act 2023; Commercial Courts Act 2015 s.12A; Copyright Act 1957; Trade Marks Act 1999 |
| Related codes | NN-13, NN-14, NN-20, NN-21, NN-22, NN-41, NN-50; D-05, D-08, D-17; CH-08, CH-14, CH-30; LG-077, LG-081, LG-110, LG-119, LG-140–142 |

### 1. About these Terms

1.1 These Terms of Use ("**Terms**") are a contract between you and `[LawDocs Operating Entity]` (CIN `[CIN]`, GSTIN `[GSTIN]`, registered office `[Registered Office]`) ("**LawDocs**", "**we**", "**us**"). They govern your use of lawdocs.in, my.lawdocs.in, work.lawdocs.in, the LawDocs mobile apps, our APIs and related services (the "**Platform**").

1.2 These Terms incorporate: the Privacy Notice (POL-LD-01), the Acceptable Use and Content Policy (POL-LD-10), the AI Use Policy (POL-LD-04), the Refund, Cancellation and Subscription Policy (POL-LD-05), and — when you use those features — the eSign, eStamp and Electronic Records Terms (POL-LD-03) and the Marketplace Terms for Buyers (POL-LD-06). Business customers who sign an order form or Master Services Agreement are governed by that agreement, which prevails over these Terms where they conflict.

1.3 **Who may use the Platform.** You must be at least 18 years old and competent to contract (Indian Contract Act 1872 s.11) [LAW]. If you accept these Terms for an organisation, you confirm you are authorised to bind it; "you" then includes the organisation.

1.4 These Terms are an electronic record under the IT Act 2000, published under IT Rules 2021 r.3(1)(a) [LAW]. You accept them by clicking "I agree" or by using the Platform.

### 2. What LawDocs is — and what it is not

2.1 **LawDocs is a legal technology and legal operations platform.** We provide: (a) software (document templates, drafting tools, the Legal Vault, contract lifecycle, eSign and eStamp workflows, litigation and trademark trackers, the Vidhi AI assistant); (b) administration and coordination (scheduling, document handling, filings support that does not require a licensed professional); and (c) **non-reserved services** delivered by our employees, such as document preparation from your instructions, compliance calendars, secretarial support that does not require a practising certificate, and process management.

2.2 **LawDocs is not a law firm and does not practise law.** Only advocates enrolled under the Advocates Act 1961 may practise law, including giving legal advice and appearing in courts (ss.29, 33) [LAW]. LawDocs does not give legal advice or representation in its own name, does not perform attest or certification functions reserved for practising chartered accountants or company secretaries, and does not create an advocate–client relationship with you (NN-41) [LAW] [INTERP].

2.3 **Reserved services are delivered by independent practitioners.** When you need legal advice, representation, an audit, a certification or any other service that the law reserves to a licensed professional, that service is provided by an independent advocate, chartered accountant, company secretary or other professional whom you engage directly, under terms between you and that professional (POL-LD-06). That professional is solely responsible for their professional judgement and work. Our role is limited to providing the technology and administration around the engagement.

2.4 **Information is not advice.** Content on the Platform — articles, guides, glossary ("i") explanations, template notes, calculators, and Vidhi's general answers — is general legal information. It does not take account of your circumstances. Do not act on it without consulting a qualified professional where your matter needs advice.

2.5 **Template automation is not advice.** When the Platform assembles a document from a vetted template using your answers, it is applying your instructions to a standard form. You choose the template and the options; you are responsible for checking that the document suits your purpose.

*Drafting note.* Counsel to confirm the boundary of "non-reserved services" against *Bar Council of India v. A.K. Balaji* (SC 2018) (practice of law includes non-litigious advice) [VERIFY: citation] and LG-110; where a service line (e.g., startup "legal officer", LDaaS retainers — R6 §R6.2.7) involves advice, it must be supplied by an advocate or advocates' firm in its own name (CH-14, D-17).

### 3. Our role as an intermediary for user content

3.1 For documents, messages, profiles, listings and other content that users upload, store, share or transmit ("**User Content**"), LawDocs acts as an **intermediary** within the meaning of IT Act s.2(1)(w) and observes the due-diligence obligations in rule 3 of the IT Rules 2021 [LAW]. We do not initiate those transmissions, select their recipients, or select or modify their contents, except as you direct (for example, when you ask Vidhi to redline a draft) [INTERP].

3.2 You must not host, display, upload, modify, publish, transmit, store, update or share information that is prohibited by rule 3(1)(b) of the IT Rules 2021 or by POL-LD-10 [LAW].

3.3 We may remove or disable access to User Content, and suspend or terminate accounts, where: we receive a valid order of a court or an authorised government agency; we receive a complaint we find valid under POL-LD-09; or the content breaches these Terms or POL-LD-10. We act within the time limits that the IT Rules prescribe (POL-LD-09) [LAW] [VERIFY: 2026 amendment timelines]. Where we remove content, we may preserve it and associated records for the period the law requires for investigation (IT Rules r.3(1)(g)) [LAW] [VERIFY: 180 days].

3.4 We remind users of these Terms, the Privacy Notice and POL-LD-10 periodically, as the IT Rules require [LAW].

3.5 Our intermediary role does not extend to services we sell in our own name (software, non-reserved services). For those, we are the supplier and these Terms set our obligations.

### 4. Accounts and security

4.1 Provide accurate information and keep it updated. One login belongs to one person; do not share credentials.

4.2 Protect your account with multi-factor authentication or a passkey. Tell us immediately at `[Support Email]` if you suspect unauthorised access. You are responsible for activity under your account until you tell us, except where the activity results from our failure to keep reasonable security.

4.3 **Aadhaar is never a login method.** Identity verification is optional unless a feature needs it, and alternatives are always offered (POL-LD-01 section 5; NN-03).

4.4 **Organisation workspaces.** The organisation's administrators control users, roles, maker-checker rules, delivery grants and retention. Administrators may access, export or delete content in the organisation's workspace. If you leave the organisation, your access ends; the content stays with the organisation.

4.5 **Delegation and delivery grants.** If you allow a LawDocs relationship manager, an engaged professional or a delegate to act in your workspace, they act only within the scope and time you approve, and every action is logged and visible to you (NN-17). Actions with legal or financial effect (send, file, sign, pay, share externally, delete) always need your confirmation (NN-13).

4.6 **Credential vault.** If your organisation enables the credential vault, it holds credentials you choose to store under your organisation's control. We never store OTPs, DSC PINs or recovery codes. Using a portal through another person's credentials may breach that portal's terms; prefer the portal's own delegation features (CH-07, NN-16).

### 5. Plans, credits, fees and payments

5.1 Plans, prices, inclusions and credit rates are shown on our pricing page and at checkout. The total amount — including GST, any government fee, stamp duty, professional fee and LawDocs fee — is shown, line by line, **before** you pay (NN-22, NN-50).

5.2 **Government fees and stamp duty** are collected from you and paid to the government or authorised channel on your behalf at actuals, as your agent; they are shown as separate lines and are not LawDocs' income [TAX MEMO: pure-agent treatment, CGST Rules r.33].

5.3 **Auto-renewal.** Subscriptions renew automatically only if you choose auto-renewal at checkout. We remind you before each renewal, and you can cancel in two taps from Settings → Billing. Details, cancellations, credit validity and refunds are in POL-LD-05.

5.4 Payments are processed by Razorpay, an RBI-authorised payment aggregator. We do not receive or store your card details (NN-22). Tax invoices are issued by the supplier of each service; for LawDocs' own services, by `[LawDocs Operating Entity]`.

5.5 You are responsible for any tax deduction at source that applies to your payment and for providing the certificate; see Settings → Billing → Tax documents [TAX MEMO].

### 6. Your content

6.1 **You own your content.** We claim no ownership of your documents, data or outputs generated for you.

6.2 **Licence to us.** You grant us a non-exclusive, worldwide, royalty-free licence to host, store, copy, process, transmit, display and adapt your content **only** to provide, secure and support the Platform for you and the people you authorise, and as the law requires. This licence ends when your content is deleted, except for backups (which expire on their normal cycle) and records we must keep by law.

6.3 **No training.** We do not use your content to train AI models and do not allow our providers to do so (NN-15).

6.4 **Your responsibilities.** You confirm that you have the right to upload your content, including any personal data of others in it (for example, a counterparty's address or an employee's details), and that your use complies with law. You remain responsible for decisions you take based on your content.

6.5 **Originals are preserved.** Original uploads and signed files are stored unchanged; OCR text, typed copies, translations and summaries are separate, labelled versions that you can correct (NN-09).

6.6 **Export.** You may export all your content at any time in standard formats without our staff's help (NN-11).

### 7. AI features and outputs

7.1 Vidhi is an AI system. It can make mistakes, including in law, dates and citations. Outputs are labelled; unverified citations are flagged "unverified" (NN-14).

7.2 Documents Vidhi drafts for an individual beyond template assembly carry the label **"AI draft — not reviewed by a professional"** until a qualified reviewer approves them. You may buy a professional review in one click.

7.3 Vidhi does not give legal advice and does not act for you. It will not send, file, sign, pay or share anything without your confirmation (NN-13).

7.4 You are responsible for reviewing outputs before relying on them. POL-LD-04 sets out the full AI terms.

### 8. eSign, eStamp and execution

Electronic signing and stamp procurement are governed by POL-LD-03. In short: some documents cannot be signed electronically under Indian law; stamp duty must be paid before or at signing; and registration, notarisation and attestation, where required, are not completed by electronic signing.

### 9. Marketplace

When you book a service from a professional through the Platform, your contract for that service is with the professional (or, for LawDocs' own non-reserved services, with us), as POL-LD-06 explains. We charge a separately disclosed platform fee. We do not rank professionals for payment, and we do not take any share of an advocate's fee (NN-21).

### 10. Integrations, ecosystem products and third-party services

10.1 You may connect third-party services (for example, Microsoft 365, Google Workspace, cloud storage, accounting tools) and Infrabyx Group products (LawDocsComply, Finbyx, Udofin, Equator Resolution). Those services are governed by their own terms. We send data to them only when you ask (POL-LD-01 PUR-09).

10.2 Our eSign capability is for use on LawDocs only and cannot be resold or used by another application, including group products (NN-06).

10.3 We link to government portals (courts, registries, tax, Vahan, e-challan). We do not control them, do not scrape them, and do not guarantee their availability or accuracy (NN-05).

### 11. Acceptable use

You must comply with POL-LD-10. Serious breaches — forged documents, fake stamp certificates, impersonation, harassment — lead to immediate suspension and may be reported to authorities.

### 12. Intellectual property

12.1 The Platform, its software, design, templates, clause library, glossary and content are owned by LawDocs or its licensors and are protected by the Copyright Act 1957 and the Trade Marks Act 1999 [LAW].

12.2 **Template licence.** We grant you a non-exclusive, non-transferable licence to use templates and generated documents for your own (and, for organisations, your organisation's) legal and business needs, including sharing the final document with your counterparties. You may not extract, republish or resell our templates or clause library as a collection, or use them to build a competing service.

12.3 "LawDocs", "Vidhi" and related logos are our trade marks. Do not use them without written permission.

### 13. Availability and changes to the service

13.1 We do not guarantee uninterrupted service, except under a written service-level agreement for business customers.

13.2 We may change features. If we remove a material paid feature during your subscription term, we will offer a pro-rata refund or an equivalent alternative (POL-LD-05).

### 14. Disclaimers

14.1 We do not guarantee any legal outcome, approval by any authority, or result in any dispute.

14.2 Court-case, trademark and registry data come from users, licensed partners or public sources. They may be delayed or incomplete; each item shows its source and when it was last updated. **We do not provide "real-time" official data** (NN-20).

14.3 Stamp duty calculators and checklists are estimates based on published State schedules and are labelled with their source and date; confirm with a professional or the authority for high-value instruments.

### 15. Limitation of liability

*Drafting note.* Caps against consumers must survive Consumer Protection Act 2019 scrutiny: s.2(46) "unfair contract" and s.49(2)/s.59(2) powers of State and National Commissions to declare unfair terms null [LAW] [VERIFY: sub-sections]; and s.2(47) unfair trade practice. Keep consumer caps generous and exclude only what is fair. Figures are [OWNER]/[COUNSEL].

15.1 **Nothing in these Terms limits liability** for fraud, wilful misconduct or gross negligence, for our breach of our data-protection security obligations caused by our failure to maintain reasonable security safeguards [COUNSEL: whether to cap with a super-cap], or for anything else the law does not allow to be limited.

15.2 **Individuals (consumers).** Subject to 15.1, our total liability for any claim relating to a service is limited to the higher of (a) the amount you paid us for that service in the 12 months before the claim, and (b) ₹`[amount]` [OWNER]. This does not restrict any remedy a Consumer Commission may award under the Consumer Protection Act 2019 [LAW].

15.3 **Business customers.** Subject to 15.1, our total liability in any 12-month period is limited to the fees paid or payable by you for the Platform in that period; for claims arising from a personal data breach caused by our failure to keep reasonable security, the limit is `[2]` times that amount [OWNER]. Neither party is liable for loss of profit, revenue, goodwill or indirect or consequential loss.

15.4 **Professionals' work.** We are not liable for the advice, work product, acts or omissions of independent professionals engaged through the marketplace (POL-LD-06), but we remain responsible for our own platform services and fees.

15.5 **Third parties.** We are not liable for failures of ESPs, stamp channels, government portals, payment networks or telecom operators beyond our reasonable control, but we will help you complete or reverse the affected transaction and refund our own fees where the service was not delivered (POL-LD-05).

### 16. Indemnity

16.1 You will indemnify LawDocs against third-party claims, penalties and reasonable costs arising from: User Content you upload without the right to do so; your breach of POL-LD-10 or the law; forged, false or misleading documents you create or submit; or your misuse of another person's personal data.

16.2 For business customers, LawDocs will defend and indemnify you against third-party claims that the Platform (excluding your content and third-party services) infringes Indian intellectual-property rights, subject to prompt notice and control of the defence.

### 17. Suspension, termination and exit

17.1 You may close your account any time from Settings.

17.2 We may suspend or terminate access for material breach, unlawful activity, non-payment (business customers, after notice), a court or government order, or a security risk. Except in urgent cases, we give notice and a chance to remedy.

17.3 **Exit and data.** After closure or termination you have **90 days** to export your data (NN-11). After that we delete it within 30 days, except records we must keep by law (POL-LD-11). Legal holds suspend deletion.

17.4 Sections 6, 12, 15, 16, 17, 18 and 19 survive termination.

### 18. Disputes and governing law

18.1 **Governing law.** These Terms are governed by the laws of India.

18.2 **Step 1 — tell us.** Most problems are solved quickly through our grievance process (POL-LD-09).

18.3 **Step 2 — mediation or online dispute resolution (optional).** If the grievance process does not resolve the matter, either party may propose mediation, including online mediation, under the Mediation Act 2023 [LAW] [VERIFY: provisions for online mediation in force]. You may choose an **independent ODR institution** from the list on our dispute-resolution page. The list includes institutions that have no connection with the Infrabyx Group; any institution affiliated with the Infrabyx Group (for example, Equator Resolution) is clearly marked "Group affiliate", is never the default and is never mandatory.

18.4 **Individuals (consumers).** Nothing in these Terms takes away your right to approach the appropriate Consumer Disputes Redressal Commission under the Consumer Protection Act 2019 (including through the e-Jagriti portal) or a civil court [LAW]. You are not required to arbitrate.

18.5 **Business customers.** Disputes not resolved within 60 days of a written notice are finally resolved by arbitration under the Arbitration and Conciliation Act 1996 by a sole arbitrator, seated at `[Seat City]`, in English, under the rules of an arbitral institution chosen jointly from the list referred to in 18.3 (excluding any Group affiliate unless both parties agree in writing after the dispute arises), with hearings by video conference where possible. Where the Commercial Courts Act 2015 applies, the parties will complete pre-institution mediation under s.12A before filing a suit that does not contemplate urgent interim relief [LAW]. Courts at `[Seat City]` have exclusive jurisdiction for interim relief and enforcement.

*Drafting note.* Equator Resolution is a group company; naming it as the mandatory forum would raise a conflict-of-interest and independence objection (Arbitration Act s.12 and Seventh Schedule) [LAW] [COUNSEL]. Consumer disputes are generally not compellable to arbitration (*Emaar MGF Land Ltd v. Aftab Singh*, SC 2018) [VERIFY: citation]; hence 18.4.

### 19. General

19.1 **Changes.** We may update these Terms. For material changes we give at least 30 days' notice (except where a law or security need requires otherwise) and ask you to accept the new version. If you do not accept, you may close your account and receive a pro-rata refund of prepaid fees for the unused term (POL-LD-05).

19.2 **Notices.** We send notices to your registered email or in-app. You send notices to `[Support Email]` and, for legal notices, to `[Registered Office]`.

19.3 **Assignment.** You may not transfer your account without our consent. We may assign these Terms to a group company or successor with notice, without reducing your rights.

19.4 **Force majeure.** Neither party is liable for delay caused by events beyond reasonable control; payment obligations for services already delivered continue.

19.5 **Severability; no waiver.** If a provision is unenforceable, the rest continues. A delay in enforcing a right is not a waiver.

19.6 **Contact.** `[LawDocs Operating Entity]`, `[Registered Office]`; `[Support Email]`; Grievance Officer `[Grievance Officer name/email]`; Nodal contact for authorities `[Nodal Contact]`.

**Build notes (O.2).** (a) Terms acceptance is a separate control from consents (APPO-AT-01). (b) Clause 2 "What LawDocs is not" also renders as a 3-line notice on every service, booking and Vidhi screen (`hlp.mkp.reserved_service`). (c) Clause 18.3 list is driven by `web.legal.odr.institution_list`; the UI never preselects a Group affiliate. (d) Re-acceptance gating returns `LD-WEB-090`.

---

## O.3 eSign, eStamp and Electronic Records Terms (POL-LD-03)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-03 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Reviewer of record + `sgn` product owner |
| Counsel review required | Yes — First Schedule exclusions as amended; account-based eSign availability; State stamp rules in launch States; agency wording for stamp procurement; s.63 certificate Part B signatory |
| Applicable law | IT Act 2000 ss.3A, 4, 5, 10A, First and Second Schedules (as amended by S.O. 4720(E), 26 Sep 2022); CCA eSign API specifications (v2.1, v3.3) and eSign FAQs; Indian Stamp Act 1899 and State Stamp Acts/rules; Registration Act 1908; Notaries Act 1952; Bharatiya Sakshya Adhiniyam 2023 ss.61–63, 85–87 and Schedule |
| Related codes | NN-06, NN-07, NN-08, NN-09, NN-10, NN-13, NN-34, NN-40, NN-46; D-12; CH-12, CH-13, CH-28; LG-001–014, LG-091, LG-096–107 |

### 1. Scope

These terms apply whenever you prepare a document for execution, invite signers, sign electronically, buy or attach stamp duty, or rely on LawDocs' evidence records. They add to the Terms of Use (POL-LD-02). Each signer accepts them at the start of each signing ceremony.

### 2. Definitions

| Term | Meaning |
|---|---|
| **eSign** | An electronic signature created through an **eSign Service Provider** using Aadhaar e-KYC or another e-KYC method listed in the Second Schedule to the IT Act [LAW] |
| **ESP** | eSign Service Provider — a Certifying Authority licensed by the Controller of Certifying Authorities (CCA) and empanelled to offer eSign |
| **ASP** | Application Service Provider — the entity whose application integrates eSign. On LawDocs, `[LawDocs Operating Entity]` is the ASP, directly or through a contracted aggregator [VERIFY: final vendor structure — D-12] |
| **DSC** | Digital Signature Certificate (Class 3) issued by a licensed Certifying Authority, usually on a USB token |
| **Electronic acceptance** | Accepting a contract by clicking, typing a name, or drawing a mark. It can form a valid contract (IT Act s.10A) but is **not** an "electronic signature" under s.3A [LAW] |
| **Stamp certificate** | An e-stamp certificate, e-SBTR, franking impression, State-portal receipt or physical stamp paper evidencing payment of stamp duty |
| **UIN** | The unique identification number on a stamp certificate |
| **Evidence pack** | The record LawDocs creates for each executed document (clause 9) |

### 3. Signature methods and their legal effect

| Method | How it works | Legal status | When we offer it |
|---|---|---|---|
| Aadhaar eSign (OTP) | The ESP authenticates you with UIDAI by OTP to your Aadhaar-linked mobile, issues a one-time certificate and signs the document hash; your key is then deleted | Electronic signature under s.3A and the Second Schedule [LAW] | Default for individuals with an Aadhaar-linked mobile |
| Aadhaar eSign (biometric) | As above, using a UIDAI-registered biometric device | As above | Assisted counters only |
| Account-based eSign | eSign with an ESP account verified by another permitted e-KYC (for users without an Aadhaar-linked mobile, NRIs, foreign nationals) | As above [VERIFY: ESP availability — LG-008] | Where our ESP supports it |
| DSC (Class 3) | You sign with your own token through a local signing agent; your key never leaves the token | Electronic signature under s.3A [LAW] | Companies, professionals, statutory filings |
| Electronic acceptance | Click, typed name or drawn mark with OTP-verified identity | Valid e-contract formation (s.10A) [LAW]; weaker evidence; never labelled "eSign" | Low-risk documents where all parties choose it |

Aadhaar use is voluntary. If you do not wish to use Aadhaar, or Aadhaar authentication fails, choose another method (Aadhaar Act s.8 proviso) [LAW].

### 4. Your consent to eSign

4.1 Before each eSign, you see a consent screen that explains — in plain language and in your chosen language — that the ESP will, with your authorisation: retrieve your e-KYC data from UIDAI or other permitted source; generate a key pair and a one-time signature certificate in your name; sign the hash of the specific document shown; and delete the key after signing. You consent separately for each document (eSign API specifications) [LAW].

4.2 LawDocs never sees or stores your Aadhaar number, OTP or biometric data. We receive the signed document, the certificate and the ESP's response codes.

4.3 The ESP's own terms and privacy notice also apply to its part of the process. We show a link to them on the consent screen.

### 5. Role of the ESP and of LawDocs

5.1 The ESP is responsible for authenticating you and issuing the certificate. LawDocs is responsible for obtaining your consent, presenting the correct document, computing and sending its hash, receiving the signature, and keeping the consent and transaction logs that the eSign rules require the ASP to keep (LG-007) [LAW].

5.2 LawDocs uses its eSign arrangement **only for documents executed on LawDocs**. We do not resell or sub-let eSign to other applications, including Infrabyx Group products (NN-06) [LAW].

5.3 We route to more than one ESP and stop routing to an ESP whose licence has lapsed until renewal evidence is recorded. If every ESP is unavailable, your ceremony waits or you may choose DSC or wet-ink execution; we do not substitute a different signature method without your choice.

### 6. Documents that cannot be eSigned, and other formalities

6.1 **Excluded by law.** Under the First Schedule to the IT Act, as amended in 2022 by notification S.O. 4720(E) [LAW] [VERIFY: Gazette date and text — W.9 LA-01] (LG-003), the following **cannot** be executed by electronic signature, and the Platform blocks them before signing (NN-07):

| Entry | Excluded instrument | Exception |
|---|---|---|
| 1 | Negotiable instruments (promissory notes, bills of exchange) | A cheque; a demand promissory note or bill of exchange issued in favour of, or endorsed by, an entity regulated by RBI, NHB, SEBI, IRDAI or PFRDA |
| 2 | Powers of attorney | A power of attorney empowering such a regulated entity to act for the executant |
| 3 | Trusts (Indian Trusts Act 1882 s.3) | — |
| 4 | Wills and other testamentary dispositions (Indian Succession Act 1925 s.2(h)), including codicils | — |

For these, we produce a **wet-ink execution pack**: a print-ready document, witness and notary checklist, and — where relevant — the registration checklist.

6.2 **Registration not provided.** Some documents must be registered with a Sub-Registrar — for example, sale deeds and gift deeds of immovable property, leases from year to year, for more than one year or reserving a yearly rent, and agreements to sell under which the buyer takes possession in part performance (Registration Act 1908 s.17(1) and s.17(1A); Transfer of Property Act 1882 s.53A) [LAW] [VERIFY: State amendments]. A document that must be registered but is not does not affect the immovable property it covers and cannot be received as evidence of the transaction, except for the limited purposes the law allows (Registration Act s.49) [LAW] (W.9 LA-12). Electronic signing on LawDocs does **not** register a document. We provide checklists, document preparation and, where offered, appointment facilitation. A document needing registration is not marked "Executed/Complete" until you record registration or an authorised user waives the step with a reason (NN-40).

6.3 **Notarisation and oaths.** Affidavits and notarial acts need a notary or oath commissioner (Notaries Act 1952; Oaths Act 1969) [LAW]. An eSigned affidavit is not a sworn affidavit [VERIFY: any State e-notarisation scheme]. We provide a print pack and, where offered, notary appointment facilitation.

6.4 **Attestation.** Where the law requires attestation by witnesses (for example, mortgages and gifts of immovable property under the Transfer of Property Act 1882 ss.59 and 123, and wills under the Indian Succession Act 1925 s.63) [LAW] [VERIFY: wording], the Platform prompts for witnesses and records their attestation; electronic attestation is offered only where counsel has confirmed it is acceptable for that instrument [COUNSEL].

6.5 **Our gate is conservative.** The Platform's eligibility table is reviewed by a qualified reviewer and versioned. If we are unsure whether an instrument may be eSigned, we treat it as excluded. You remain responsible for confirming the formalities your document needs.

### 7. Stamp duty: stamp before sign

7.1 **Duty first.** Under the Indian Stamp Act 1899 s.17 and corresponding State laws, instruments chargeable with duty must be stamped before or at the time of execution [LAW]. On LawDocs, **signing cannot start on a chargeable instrument until a stamp certificate is attached and its UIN verified**, or you confirm that the instrument is not chargeable (NN-08).

7.2 **Your responsibility.** The parties are responsible for paying the correct duty. Our duty calculator gives an estimate from the State schedule (State × article), shows its source and date, and asks you to confirm the State, the article and the consideration. An instrument that is not duly stamped may be impounded and is not admissible in evidence until duty and penalty are paid (Indian Stamp Act ss.33, 35, and State equivalents) [LAW].

7.3 **How we buy stamps.** Where you ask, we procure stamp duty **as your agent** only through authorised channels — the Stock Holding Corporation of India Ltd (as Central Record-keeping Agency), its Authorised Collection Centres, State e-stamp or e-SBTR portals, GRAS or franking routes — as each State permits (LG-098–100) [LAW]. We do not sell stamp paper ourselves. The certificate is issued in the name of the party you specify, with the real consideration.

7.4 **Charges.** Stamp duty and any government fee are charged at actuals and paid to the authorised channel. Our facilitation fee (and any courier charge for physical paper) is shown separately with GST (NN-22).

7.5 **Physical stamp paper.** You may attach stamp paper or a franked document you already hold. We verify the UIN where the State's verification service allows and record the verification result; where it does not, we record that the certificate is "not verified" and show this in the evidence pack.

7.6 **Binding the stamp to the document.** We link the stamp certificate to the hash of the final document. If the document changes after stamping in a way that changes the consideration, parties or article, we warn you that fresh stamping may be needed.

7.7 **Refunds of duty** follow POL-LD-05 and State rules; government refunds are not within our control.

7.8 **Instruments executed outside India.** Instruments executed outside India and received in India may need to be stamped within a statutory period after receipt (Indian Stamp Act s.18) [LAW] [VERIFY: State equivalents]. We show a reminder.

### 8. Your obligations as a signer

You confirm that:
1. You are the person named as signer, and you are signing voluntarily — not under coercion, undue influence or fraud (Indian Contract Act 1872 ss.14–18) [LAW].
2. You have read the document, including all pages and annexures shown before the consent screen.
3. If you sign for an organisation, you hold the authority to do so (board resolution, delegation of authority or power of attorney), and you will provide proof if asked.
4. You will not share your OTP, DSC PIN or token with anyone, including LawDocs staff.
5. The mobile number linked to your Aadhaar or ESP account is yours and under your control.
6. If you are a witness, you saw the signer sign or received the signer's acknowledgement as the law requires for that instrument.
7. You will not use the Platform to sign a document you know is false, forged or intended to defraud (POL-LD-10).

### 9. Evidence, integrity and retention

9.1 For every executed document we create an **evidence pack** containing: the final document's SHA-256 hash (computed when the document was locked for signing and again on export); the stamp certificate and its verification result; each signer's consent version, method, certificate details, ESP transaction ID and response codes; timestamps; IP address and device information; the order of events; and an extract of the audit trail (NN-10).

9.2 Original uploads and signed files are stored in write-once storage and are never altered (NN-09).

9.3 We keep evidence packs for at least **seven years** after the later of execution and account closure, or longer where a limitation period, legal hold or regulator requires (LG-008, LG-092). If you close your account, you can export your evidence packs first; deleting your copy does not delete records we must keep or copies other parties hold.

9.4 Any party can verify a document's integrity on LawDocs' verification page by uploading the file or entering its reference, without an account.

### 10. Using your records in court — BSA s.63 certificate support

10.1 Electronic records are admissible as documents, subject to Bharatiya Sakshya Adhiniyam 2023 (BSA) s.63 [LAW]. Section 63(4) requires a certificate in the form in the Schedule, with **Part A** completed by the party and **Part B** by an expert, identifying the record, the device and the hash value [LAW] (LG-091).

10.2 For any document in your vault, the Platform generates a pre-filled **Part A** for you to complete and sign, and lets you request **Part B** from LawDocs' designated officer or an examiner you choose (including an Examiner of Electronic Evidence notified under IT Act s.79A) [LAW] [VERIFY: who may sign Part B after *Pune Bar Association v. Union of India*, SC, 22 May 2026 — R3 LG-091; COUNSEL].

10.3 We do not guarantee that a court will admit or rely on any record; admissibility and weight are for the court.

### 11. Inviting counterparties

When you invite someone to review or sign, we send at most one invitation and reminders they have not opted out of; we do not make automated calls to them unless they opt in (NN-34). Counterparties see only the versions you share; your internal comments are never visible to them (NN-37).

### 12. Limits of our responsibility

We are not responsible for: the legal validity, enforceability or content of your document; the choice of stamp article or the duty amount you confirm; ESP, UIDAI or State-portal outages beyond our control; or the absence of formalities (registration, notarisation, attestation) we have flagged. Where a ceremony or stamp order fails because of our error, we refund our fees and help you complete or reverse the transaction (POL-LD-05).

**Build notes (O.3).** (a) Clause 4 consent text is versioned in `tpl` and stored per signer (`sig_` record). (b) The clause 6.1 table is rendered from the eligibility register (Appendix F), never hard-coded. (c) Clause 7.1 gate raises `LD-SGN-0xx` errors defined in P08 (e.g., "Instrument not eligible for electronic signature"); this appendix does not define them. (d) Help keys `hlp.sgn.esp`, `hlp.sgn.asp`, `hlp.sgn.stamp_before_sign`, `hlp.sgn.s63_certificate`.

---
## O.4 AI Use Policy and Disclosures (POL-LD-04)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-04 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Reviewer of record + AI lead |
| Counsel review required | Yes — "information vs advice" boundary; Anthropic Usage Policy high-risk legal requirements; synthetic-media labelling under the IT Rules 2026 amendment |
| Applicable law | Advocates Act 1961 ss.29, 33; IT Rules 2021 as amended by the Amendment Rules 2026 (r.2(1)(wa), r.3(3)) [VERIFY: final text]; DPDP Act 2023; Consumer Protection Act 2019 s.2(47); provider policy: Anthropic Usage Policy (effective 12 Nov 2026) [VERIFY] |
| Related codes | NN-13, NN-14, NN-15, NN-20, NN-34, NN-43, NN-48; D-14, D-15; CH-17, CH-30; LG-078, LG-119; R4 §6.4 |

**1. What Vidhi is.** Vidhi is the AI assistant built into LawDocs, powered by Anthropic's Claude models through our AI gateway. **You are interacting with an AI system, not a person and not a lawyer.** Every chat and voice session begins with this disclosure.

**2. What Vidhi does.**

| Vidhi can | Vidhi does not |
|---|---|
| Explain legal concepts and procedures in general terms, with the provisions it relied on | Give legal advice on what you should do in your specific matter |
| Fill an approved template from your answers (template automation) | Represent you, appear for you, or act as your advocate |
| Draft bespoke clauses or documents (AI-custom drafts), labelled for review | Guarantee accuracy, completeness or any outcome |
| Review and redline contracts; extract obligations and dates | Send, file, sign, pay, share outside your workspace, accept, withdraw or delete without your confirmation (NN-13) |
| Read handwriting and screenshots into editable typed copies; translate | Replace certified translations required by courts (NN-48) |
| Summarise orders, notices and documents | Invent case law, sections or citations — unresolved citations are shown as "unverified" (NN-14) |

**3. Two drafting lanes and human review.**

| Lane | What happens | Label | Can it be sent for eSign? |
|---|---|---|---|
| Template lane | The document text comes from a template written and reviewed by a qualified professional; Vidhi helps you answer the questions | "Prepared from a reviewed template" | Yes |
| AI-custom lane (individuals) | Vidhi writes or changes legal text for your situation | **"AI draft — not reviewed by a professional"** | Not until a qualified reviewer approves it (one-click paid review) |
| AI-custom lane (company workspaces) | As above | "AI draft — review required" | After review by a user your organisation designates as qualified (for example, CLO, CS or advocate) |

After review the label reads: "Prepared with AI assistance; reviewed by `[name, qualification/enrolment no.]` on `[date]`". *Drafting note:* this implements the Usage Policy requirement that a qualified person meaningfully review high-risk legal outputs before delivery and that the individual is told AI was used (R4 §6.4) [VERIFY: whether template-lane fact extraction falls outside the high-risk definition — OI-R4-05].

**4. Accuracy limits.** AI can be wrong, out of date or incomplete, particularly on recent amendments, State-specific rules and court practice. Each answer shows the date of the sources it used. Check important points with a professional.

**5. Your data and AI.** Personal and confidential content is processed only through an approved in-region endpoint in India; Anthropic's own API is used only for public, non-personal content. **We never use your data to train AI models** (NN-15). Vidhi only sees documents you can see. You can turn AI features off in Settings → AI and privacy. See POL-LD-01 section 8.

**6. AI agents.** In company workspaces, AI agents may prepare work as **makers only**. They never approve, check or sign, act within limits your administrator sets, and can be stopped at once by a kill switch (NN-43).

**7. AI voice, avatars and generated media.** Where we use AI-generated voice, video avatars or images (for example, tutorial narration, an AI voice agent for reminders), they are **synthetically generated information** under the IT Rules as amended in 2026 [LAW] [VERIFY: r.2(1)(wa), r.3(3)]. We label them visibly, prefix audio with a spoken disclosure ("This is an automated AI voice from LawDocs"), embed provenance metadata, and offer a human hand-off. AI calls are made only with your consent, from declared numbers, within permitted hours and after DND checks (NN-34). Text-only drafting is not synthetic media under that definition, but we label it anyway.

**8. Things Vidhi will refuse.** Creating or altering official-looking records (stamp certificates, court orders, identity documents, government letters); imitating a real person's voice or likeness without consent; drafting harassment or threatening notices; helping evade law or a court order (POL-LD-10).

**9. Report a problem.** Use "Report this answer" on any output or write to `[Support Email]`. Serious issues (fabricated citation, unsafe advice, privacy leak) are triaged within one business day [REC].

**Build notes (O.4).** Disclosure text and labels are CMS content keyed `ai.disclosure.*` and rendered by `packages/ai`; label states map to the draft lifecycle in P06; help keys `hlp.ai.ai_draft_label`, `hlp.ai.qualified_review`.

---

## O.5 Refund, Cancellation and Subscription Policy (POL-LD-05)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-05 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Billing lead + reviewer of record |
| Counsel review required | Yes — fairness of credit expiry; E-Commerce Rules cancellation-charge parity; stamp-duty refund rules per launch State; GST credit-note mechanics [TAX MEMO] |
| Applicable law | Consumer Protection Act 2019 ss.2(46), 2(47); Consumer Protection (E-Commerce) Rules 2020 r.4 [VERIFY: sub-rules]; CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023; RBI e-mandate directions [VERIFY: current instrument — LG-147]; CGST Act s.34 (credit notes); Indian Stamp Act 1899 ss.49–54 and State rules |
| Related codes | NN-22, NN-50; D-11; CH-25; LG-141, LG-142, LG-145, LG-147 |

**1. Principles.** All prices are shown with GST, government fees and stamp duty as separate lines before you pay. Renewal date and price are shown at checkout and in Settings → Billing. **Cancelling is as easy as subscribing** — two taps, no call, no retention maze (NN-50). We charge no cancellation fee on consumer orders unless we would bear a matching charge for cancelling on our side (E-Commerce Rules r.4(10)) [LAW] [VERIFY: sub-rule].

**2. Plans and renewals.**
1. Plans are billed monthly or annually. Auto-renewal is your choice at checkout.
2. We send renewal reminders **7 days** before monthly renewals and **30 and 7 days** before annual renewals, with the amount and a cancel link. Mandate debits follow RBI's e-mandate rules, including pre-debit notification [LAW] [VERIFY].
3. Price increases apply only from your next renewal and are notified at least 30 days ahead.

**3. Cancelling a subscription.**

| When you cancel | What happens |
|---|---|
| Within `[7]` days of first purchase of a plan (`bil.refunds.new_subscription_window_days`) [OWNER] | Full refund of the plan fee, less the value of paid credits or third-party costs (eSign, eStamp) you consumed |
| Monthly plan, later | Plan continues to the end of the paid month; no further charge |
| Annual plan, later | Plan continues to the end of the term; no further renewal. If we materially reduce a paid feature or you reject a material change in terms, we refund the unused months pro rata |
| Downgrade | Takes effect at the next renewal; your data stays and becomes read-only only where the lower plan lacks the feature |

**4. Credits.**
1. Credits (eSign, AI, court-data refresh) are shown with their expiry date before purchase. Purchased credit packs are valid for **12 months** from purchase (`bil.credits.validity_months`); plan-included credits are valid for the plan period.
2. We remind you **30 and 7 days** before credits expire. Credits are used oldest-first.
3. Unused purchased credits are refundable pro rata within the first-purchase window; afterwards they are not refundable, but if we discontinue the credit type we refund the unused balance. *Drafting note:* counsel to confirm that 12-month expiry with reminders is a fair term (CPA 2019 s.2(46)) [COUNSEL].
4. Credits have no cash value, cannot be transferred outside your account or workspace, and are not a deposit.

**5. One-time services by LawDocs.**

| Stage | Refund |
|---|---|
| Cancelled before work starts | 100% of LawDocs' fee |
| Work started, no deliverable shared | Fee less work done, by the published stage scale for that service |
| Deliverable shared | No refund for that stage; one revision round included as stated in the service card |
| We cannot deliver as promised | 100% of the undelivered portion |

**6. Marketplace services from professionals.** The professional's fee is held by Razorpay Route and released to the professional on milestone acceptance (POL-LD-06). If a milestone is not delivered, the held amount is refunded by reversal. Disputes over professional work follow POL-LD-06 section 6. LawDocs' platform fee is refunded if the engagement is cancelled before the professional accepts it, or if the professional fails to start.

**7. Government fees, stamp duty and third-party charges.**
1. **Government fees** (court fees, registration fees, ROC/MCA fees, trademark fees and similar) are **non-refundable by LawDocs once paid** to the authority. If the authority refunds a fee, we pass it to you.
2. **Stamp duty:** once a stamp certificate is issued, any refund is governed by the Indian Stamp Act (allowances for spoiled or unused stamps, ss.49–54) or the State's law and e-stamp rules, usually through an application to the Collector within a time limit and subject to a deduction [LAW] [VERIFY: each launch State's period, deduction and e-stamp cancellation procedure]. We help you prepare the application; the refund decision and timing are the authority's. Our facilitation fee is refunded only if the certificate was not issued.
3. **eSign transactions** consumed are not refundable unless the failure was our fault.

**8. How refunds are paid.** To the original payment method within **7 business days** of approval [REC]; Razorpay and your bank may take further time. For GST-invoiced services we issue a credit note (CGST Act s.34) [LAW].

**9. Questions and complaints.** `[Support Email]`; Grievance Officer `[Grievance Officer name/email]` (POL-LD-09).

**Build notes (O.5).** Checkout summary renders clauses 1–2 dynamically (APPO-AT-08). Stage scales are catalogue data in `mkp`/`bil`; refunds require maker-checker (NN-18); help key `hlp.bil.credit_expiry`.

---

## O.6 Marketplace Terms for Buyers (POL-LD-06)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-06 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Marketplace lead + reviewer of record |
| Counsel review required | Yes — BCI Rule 36 directory constraints and Madras HC 2024; buyer platform fee structure; E-Commerce Rules marketplace duties; Route on-hold mechanics |
| Applicable law | Advocates Act 1961; BCI Rules Part VI Ch. II (Rules 20, 36, 37) [VERIFY: numbering]; CA Act 1949 and CS Act 1980 First Schedules; Consumer Protection (E-Commerce) Rules 2020 r.4–6; RBI Payment Aggregator Directions 2025; CGST Act s.52 and Notification 13/2017-CT(R) [TAX MEMO]; IS 19000:2022 |
| Related codes | NN-17, NN-21, NN-22, NN-41, NN-49; D-05, D-11; CH-08, CH-09, CH-20, CH-25; LG-111–117, LG-141, LG-143, LG-145 |

**1. Who you contract with.** Each service card shows the **supplier**: either `[LawDocs Operating Entity]` (for LawDocs' own non-reserved services) or a named independent professional or firm, with their registration details and GSTIN where applicable (E-Commerce Rules r.5) [LAW]. **For reserved services — legal advice, representation, audit, certification — your engagement is directly with the professional**, who is solely responsible for the work. LawDocs is not a party to that professional relationship (NN-41).

**2. How professionals are shown.** Advocates are shown only with the details BCI Rule 36 permits (name, address, contact, enrolment number and date, State Bar Council, bar association, qualifications, practice areas), in neutral order, with **no ratings, reviews, testimonials, fees-based ranking, badges or photographs** [LAW] (NN-21). Our ordering parameters (for example, relevance to your service, language, availability) are published on the "How ordering works" page; no professional can pay to rank higher (E-Commerce Rules r.5) [LAW] [VERIFY: sub-rule]. Verification shown means only what it says (for example, "enrolment number matched with `[source]` on `[date]`"), not a quality endorsement (NN-20).

**3. Fees.** Before you pay you see: the professional's fee (set by the professional); **LawDocs' platform fee** as a separate line (our charge to you for the booking, secure workspace, payment handling and records); government fees at actuals; and GST per supplier. LawDocs takes **no share of an advocate's fee** and charges advocates nothing for listing or leads (NN-21). Advocates' services to business entities may be under GST reverse charge, which the invoice will show [TAX MEMO].

**4. Payment and milestones.** You pay once through Razorpay. The professional's fee goes to the professional's own linked account through Razorpay Route and is held until you accept the milestone (or until it is deemed accepted `[5]` business days after delivery if you do not respond, after two reminders) [OWNER]; LawDocs never pools professionals' money (NN-22).

**5. Engagement workspace.** Each engagement gets a secure workspace. The professional sees only the documents you share and only for the engagement's duration (delivery grant, NN-17). Communications with an advocate in the course of the engagement are confidential and may be privileged (BSA 2023 s.132) [LAW] [VERIFY].

**6. Problems and disputes.**
1. Raise a concern in the workspace; the professional responds within 2 business days.
2. If unresolved, ask LawDocs to review the **service-delivery** aspects (missed milestone, non-delivery, scope as stated on the card). We may pause release of held funds and decide refunds of the held amount under POL-LD-05. We do not judge the professional's legal opinion; complaints about professional conduct go to the relevant regulator (State Bar Council, ICAI, ICSI), whose details we provide.
3. Your rights under consumer law and POL-LD-09 are unaffected.

**7. Reviews.** You may review **LawDocs' own services** and non-regulated providers (for example, translators) after a verified purchase. Reviews must be genuine, your own experience and free of personal data; we do not pay for, edit or selectively suppress reviews, we label any incentive, and we moderate under IS 19000:2022 [REC]. **You cannot review or rate advocates** on LawDocs (NN-49).

**8. Off-platform dealings.** Payments made to a professional outside LawDocs are outside our protections and refund process.

**Build notes (O.6).** Booking page renders clauses 1, 3 and 4 above the Pay button; directory cards use the `RULE36_V1` field set; help keys `hlp.mkp.platform_fee`, `hlp.mkp.reserved_service`.

---

## O.7 Professional Partner Terms (POL-LD-07)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-07 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Reviewer of record + marketplace lead |
| Counsel review required | Yes — per-profession clause sets; Rule 36 directory scope pending *Sulekha.com v. P.N. Vignesh*; ICAI 23 Oct 2019 announcement; ICSI guidance; data-protection roles; Route linked-account terms; TDS/TCS mechanics [TAX MEMO] |
| Applicable law | Advocates Act 1961 ss.29, 33, 35; BCI Rules Part VI Ch. II (Rules 20, 36, 37, 49) [VERIFY]; BCI Certificate and Place of Practice (Verification) Rules 2015 [VERIFY]; CA Act 1949 First Schedule Part I; CS Act 1980 First Schedule; DPDP Act 2023 ss.2(i), 8(2); BSA 2023 ss.132–134; RBI PA Directions 2025; CGST Act s.52; Income-tax Act 2025 s.393 [VERIFY: table entries] |
| Related codes | NN-17, NN-21, NN-22, NN-41, NN-49; D-05; CH-08, CH-09; LG-110–117, LG-130; R6 §R6.3, T-05, T-07 |

*Drafting note.* Generate the agreement from clause sets by profession: `PPT-COMMON` + `PPT-ADV` (advocates and law firms), `PPT-CA`, `PPT-CS`, `PPT-TAX` (non-CA tax/GST practitioners), `PPT-OTHER` (translators, valuers, process servers). Practising-CA and practising-CS listing remains **OFF** until counsel confirms a compliant structure (D-05, CH-09); `PPT-CA`/`PPT-CS` therefore apply initially to LawDocs-engaged non-attest work or directly engaged independent work without listing [COUNSEL].

**1. Parties and nature.** These terms are between `[LawDocs Operating Entity]` and you, a professional or firm ("**Partner**"). You are an independent professional. Nothing creates employment, partnership, agency or a fee-sharing arrangement. You contract with buyers directly for your professional services and are solely responsible for them.

**2. Verification.** Before activation we verify, and periodically re-verify: identity (KYC); for advocates, enrolment with a State Bar Council and certificate of practice where applicable [VERIFY]; for CAs/CSs, membership and certificate-of-practice status; GSTIN and PAN; professional indemnity insurance if you hold it; no current suspension. You must tell us within 7 days of any suspension, disciplinary order or change of status.

**3. Conduct rules by profession (`PPT-ADV`).** LawDocs charges advocates **no listing fee, commission, referral or lead fee, or fee for ranking**, and pays advocates no referral reward (BCI Rules; NN-21) [LAW]. Your directory profile contains only Rule 36-permitted particulars, which you provide and keep accurate; no testimonials, ratings, photographs or claims of success. You set your own fees; you will not charge a fee contingent on results or take a share of the proceeds of a claim (Rule 20) [LAW]. You will not allow your name or services to be used by any lay agency to practise law (Rule 37) [LAW]. You may subscribe to LawDocs software on the same terms as any customer; your subscription never affects visibility or allocation. *Drafting note:* the directory itself stays **OFF at launch** pending counsel opinion (LG-113); until then advocates are engaged on buyer request through fixed-price service cards [COUNSEL].

**4. Conduct rules (`PPT-CA`, `PPT-CS`, `PPT-TAX`).** You will comply with your Institute's Code of Ethics, including the prohibitions on sharing fees with non-members, solicitation and advertising [LAW] [VERIFY: current ICAI and ICSI guidance]. No percentage of your fee is paid to LawDocs. Non-institute tax practitioners are subject to the commercial terms in Schedule 1, enabled only after legal review [COUNSEL].

**5. Confidentiality and privilege.** You keep buyers' information confidential, use it only for the engagement, and access it only through the engagement workspace and its delivery grant (NN-17). You will not download buyer data beyond what the engagement needs. Professional communications retain whatever privilege the law gives them (BSA 2023 ss.132–134) [LAW]; LawDocs staff do not access engagement content except under the buyer's grant or a legal requirement.

**6. Conflicts.** Before accepting, you run your own conflict check; the Platform also checks the counterparty names you provide against your declared conflict list. You must decline matters where you have a conflict.

**7. Data protection roles.**

| Data | Role of Partner | Role of LawDocs | Basis |
|---|---|---|---|
| Buyer's matter content and your advice | Independent Data Fiduciary (you decide how to use it to advise) [INTERP] | Processor hosting the workspace on your and the buyer's instructions [INTERP] | Engagement terms; DPDP s.8(2) contract (this clause) |
| Buyer's account, booking and payment data | Recipient for the engagement only | Data Fiduciary | POL-LD-01 |
| Your own profile and payout data | Data Principal | Data Fiduciary | POL-LD-01 |

*Drafting note.* DPDP s.2(i) permits a fiduciary to determine purposes "alone or in conjunction with other persons" [LAW]; counsel to decide whether the workspace is better characterised as joint determination, and adjust the DPA-style clauses (security, breach notice within 24 hours to LawDocs, deletion at engagement end) accordingly [COUNSEL].

**8. Payouts.** You must hold a KYC-verified Razorpay Route linked account. Buyer payments for your fee are transferred to your account on milestone acceptance; refunds are by reversal of held amounts only. LawDocs collects tax at source as an e-commerce operator where applicable (CGST Act s.52; Notification 15/2024-CT for the 0.5% rate) and deducts TDS where the Income-tax Act 2025 requires (for example, s.393 table entry for e-commerce operators) [LAW] [TAX MEMO: exclusion of RCM/exempt supplies; current entries]. You issue your own invoice or bill of supply to the buyer.

**9. Service standards.** Accept or decline bookings within 1 business day; meet the milestones on the service card; respond to buyer queries within 2 business days; use the workspace for engagement communications.

**10. Suspension and exit.** We may suspend for loss of eligibility, credible misconduct complaints, data misuse or breach of these terms. On exit, you complete or hand over live engagements as the buyer directs and return or delete buyer data, keeping only what your professional rules require.

**Build notes (O.7).** Clause sets are `tpl` templates keyed by `pro.profession`; any commercial switch beyond Schedule 1 is locked per NN-21 (APPO-AT-05). Partner agreement is eSigned during onboarding in apps/delivery.

---
## O.8 Cookie Policy and consent banner (POL-LD-08)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-08 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | `[DPO]` |
| Counsel review required | Yes — whether any cookieless aggregate analytics may run before consent under DPDP; GDPR/ePrivacy and CCPA variants |
| Applicable law | DPDP Act 2023 ss.5–6; SPDI Rules 2011 (interim); CCPA Dark Patterns Guidelines 2023; GDPR and ePrivacy (supplement); CCPA/CPRA (GPC) |
| Related codes | NN-26, NN-31, NN-35, NN-50; CH-18, CH-21 |

**1. What cookies are.** Cookies and similar technologies (local storage, SDK identifiers in our apps, pixels) store or read small pieces of information on your device.

**2. Categories.**

| Category | Purpose | Examples | Default | Can you refuse? |
|---|---|---|---|---|
| Strictly necessary | Sign-in, security, load balancing, fraud prevention, remembering your cookie choice | Session cookie, CSRF token, consent record | On | No (the service cannot work without them) |
| Preferences | Language, accessibility and display settings | Language, text size, theme | Off until you choose | Yes |
| Analytics | Understand page use and errors to improve the service; first-party, hosted in India | Self-hosted analytics identifier | Off until you consent | Yes |
| Marketing | Measure campaigns and show our ads on other sites | Advertising pixels (loaded only if switched on and consented) | Off; feature itself OFF by default | Yes |

We never place marketing or analytics technologies on vault, drafting, signing, matter, consumer-case or Vidhi pages (NN-35). We do not sell or share cookie data for third-party advertising.

**3. The banner.** On first visit you see three equal buttons — **Accept all**, **Reject all**, **Choose** — with no pre-ticked boxes and no repeated nagging after you choose (NN-50). Your choice is stored with the policy version and timestamp; if you are signed in, it is linked to your consent record. We honour Global Privacy Control signals as "Reject marketing" [REC].

**4. Changing your choice.** Footer → "Cookie settings" or app Settings → Privacy; effective immediately.

**5. Retention.** Session cookies end when you close the browser; consent records are kept for the life of the choice plus 12 months; analytics identifiers expire within 13 months [REC].

**6. Current list.** The table of every cookie (name, provider, purpose, category, duration) is generated from our tag inventory and shown below this policy; nothing loads that is not in the inventory.

**Build notes (O.8).** Banner categories map to P21's consent manager; marketing tags additionally gated by `web.cookies.marketing.enabled`; mobile SDKs follow the same categories (P22).

---

## O.9 Grievance Redressal Policy (POL-LD-09)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-09 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | `[Grievance Officer name/email]` (`PLT_GRIEVANCE_OFFICER`) |
| Counsel review required | Yes — current IT Rules timelines after the 2026 amendment; E-Commerce Rules timelines; how the stricter clock applies per complaint type |
| Applicable law | IT Rules 2021 r.3(2) as amended by the Amendment Rules 2026 (notified 10 Feb 2026, in force 20 Feb 2026 per R3) [VERIFY: final text]; Consumer Protection (E-Commerce) Rules 2020 r.4; DPDP Act 2023 ss.8(10), 13; RPwD Act 2016 |
| Related codes | NN-23, NN-26; D-06; LG-077, LG-141 |

**1. Grievance Officer.** `[Grievance Officer name/email]`, `[LawDocs Operating Entity]`, `[Registered Office]`. Phone `[Support Phone]` (business hours). Data Protection Officer: `[DPO]`. Contact for orders of courts and authorities: `[Nodal Contact]` (24×7).

**2. How to complain.** Online form at `/legal/grievance` (no sign-in needed), in-app "Report a problem", email, or post. You receive a reference number at once.

**3. Timelines.** Where more than one rule applies, **we follow the shortest**.

| Complaint type | Acknowledge | Resolve | Source |
|---|---|---|---|
| Content you believe is unlawful under IT Rules r.3(1)(b), or a request to remove it | 24 hours | **36 hours** for prohibited-content removal requests; otherwise 7 days | IT Rules r.3(2) as amended 2026 (R3 LG-077) [LAW] [VERIFY] |
| Content exposing a person's private area, nudity, sexual act or impersonation in morphed images | Immediately | **2 hours** to remove or disable access | IT Rules r.3(2)(b) as amended 2026 [LAW] [VERIFY] |
| Any other grievance about the Platform (account, content, service) | 24 hours | **7 days** | IT Rules r.3(2)(a)(i) as amended 2026 [LAW] [VERIFY] |
| Consumer complaint about a purchase (refund, delivery, deficiency) | 48 hours | Within 7 days (our standard), never later than one month | E-Commerce Rules r.4(5) (48 h / 1 month) [LAW]; 7 days [REC] |
| Privacy rights request (access, correction, erasure, nomination) | 24 hours | 30 days target; no later than 90 days | DPDP Rules 2025 Rule 14(3) [LAW] [VERIFY] |
| Accessibility barrier | 24 hours | Workaround within 2 business days; fix scheduled and reported | RPwD Act 2016 [REC] |
| Court or government order | — | Within the time stated in the order or the IT Rules (3 hours for takedown orders per the 2026 amendment) | IT Rules r.3(1)(d) [LAW] [VERIFY] |

**4. Escalation.**
1. Level 1 — Support team (most issues within 2 business days).
2. Level 2 — Grievance Officer (all complaints in the table above go directly here if you choose).
3. Level 3 — External: the **Grievance Appellate Committee** under IT Rules r.3A for intermediary decisions (appeal within 30 days of our decision) [LAW] [VERIFY]; the **Data Protection Board of India** for privacy complaints after our process (DPDP s.13(3)); the **National Consumer Helpline** (1915) or a **Consumer Commission** (e-Jagriti) for consumer disputes; the relevant **State Bar Council, ICAI or ICSI** for professional-conduct complaints about a professional; the **Chief Commissioner** or State Commissioner for Persons with Disabilities for accessibility [VERIFY].

**5. What we record.** Every grievance, its clock and outcome is logged; we publish annual counts by type and the share resolved in time [REC].

**6. `[Consumer Help Brand]` variant.** `[Consumer Help Brand]` publishes this same policy under `[Consumer Help Entity]` with its own Grievance Officer and DPO. Complaints about a financial-services provider you are pursuing through `[Consumer Help Brand]` are not grievances against `[Consumer Help Brand]`; they follow your case's escalation ladder (the provider's grievance officer, its Internal Ombudsman where applicable, then the RBI Ombudsman, Insurance Ombudsman or Consumer Commission). Complaints **about** our case handling come to our Grievance Officer and are answered within the timelines above.

**Build notes (O.9).** The clock table is rule data in `rul` (effective-dated) driving the OH support-desk SLA; the 2026 timelines are Locked as the stricter default even while `[VERIFY]` (conservative choice).

---

## O.10 Acceptable Use and Content Policy (POL-LD-10)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-10 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Trust and Safety lead |
| Counsel review required | Yes — alignment with IT Rules r.3(1)(b) list; reporting duties to authorities |
| Applicable law | IT Act 2000 ss.66C, 66D, 67, 72A; IT Rules 2021 r.3(1)(b); Bharatiya Nyaya Sanhita 2023 (forgery and related offences) [VERIFY: sections]; Indian Stamp Act 1899; Aadhaar Act 2016 s.29; Copyright Act 1957; Trade Marks Act 1999 |
| Related codes | NN-04, NN-05, NN-13, NN-34; CH-13; LG-076, LG-078 |

**1. You must not use LawDocs to:**

| # | Prohibited use |
|---|---|
| 1 | Create, alter or present a **forged or false document**, or backdate a document to mislead |
| 2 | Create or present **fake stamp papers or stamp certificates**, reuse a certificate for another instrument, or misstate consideration to underpay duty |
| 3 | **Impersonate** any person, sign for someone without authority, or use another person's OTP, DSC, password or identity (IT Act ss.66C, 66D) [LAW] |
| 4 | Send **harassing, threatening or extortionate notices** — including debt-recovery notices that breach recovery-conduct rules, or notices threatening arrest or public shaming |
| 5 | Upload or share content that is obscene, sexually explicit, harmful to children, invasive of another's privacy, defamatory, hateful, or that infringes intellectual property; or any other category in IT Rules r.3(1)(b) [LAW] |
| 6 | Publish another person's **Aadhaar number**, bank details, health data or other personal data without a lawful basis (Aadhaar Act s.29(4)) [LAW] |
| 7 | Misrepresent yourself as an advocate, CA, CS, notary or government official, or use LawDocs to practise a profession you are not licensed for |
| 8 | Use AI to generate realistic audio, images or video of a real person without consent, or official-looking records (orders, IDs, certificates) |
| 9 | Scrape, crawl or automate access to LawDocs, or use LawDocs to scrape or bypass CAPTCHAs of any court, registry, government or bureau portal (NN-05) |
| 10 | Upload malware, probe or attack our systems (except under POL-LD-13's disclosure policy), or overload the service |
| 11 | Send spam, unsolicited bulk invitations or automated calls (NN-34) |
| 12 | Facilitate money laundering, fraud, unregistered deposit schemes or evasion of tax or a court order |

**2. What happens.** Depending on severity: warning; removal of content; suspension of sharing, signing or messaging; account termination; preservation of records and reporting to law-enforcement or the authority concerned where the law requires or the harm is serious. Forgery, fake stamps and impersonation lead to immediate suspension.

**3. Reporting.** Report misuse through "Report" on any shared item or the grievance form (POL-LD-09). Counterparties who receive an abusive notice through LawDocs can report it without an account.

**4. Our checks.** We run proportionate checks (stamp UIN verification, duplicate-certificate detection, Aadhaar masking, malware scanning). We do not read private documents except to act on a report, a legal order or a security alert.

---

## O.11 Data Retention and Deletion Schedule — public summary (POL-LD-11)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-11 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | `[DPO]` |
| Counsel review required | Yes — each period against limitation, tax, eSign and sector rules; legal-hold triggers |
| Applicable law | DPDP Act 2023 s.8(7), Rules 2025 Rule 6, Rule 8; CERT-In Directions 2022; eSign API v3.3; Limitation Act 1963; Companies Act 2013 s.128(5); CGST Act s.36; DigiLocker Requester Terms |
| Related codes | NN-02, NN-09, NN-11, NN-12, NN-26, NN-27, NN-42; LG-008, LG-065, LG-079, LG-092, LG-128 |

Periods run from the event shown. A **legal hold** (litigation, investigation, regulator request) suspends deletion until released. Backups expire on a 35-day cycle [REC] after the live record is deleted. Company workspaces may set longer periods for their own content.

| Record | Retention | Then |
|---|---|---|
| Account profile and settings | Account life + 90-day export window | Deleted within 30 days |
| Vault documents, drafts, versions, derived renditions | Until you delete, or account closure + 90 days | Deleted; signed originals subject to the eSign row |
| eSign evidence packs, consent records, ESP responses | ≥ 7 years after the later of signing and account closure (LG-008); longer if limitation or hold requires | Deleted |
| eStamp records (certificate, UIN, verification) | As the executed document; minimum 8 years for the transaction record [REC] | Deleted |
| Aadhaar-derived attributes (last 4 digits, flags) | Until verification purpose ends or you revoke; kept inside signing records only | Deleted |
| DigiLocker references | URI and verification result while the linked document is in your vault; no copy unless you save one for a recorded purpose (NN-42) | Deleted |
| Invoices, payments, refunds | 8 years from the end of the financial year (Companies Act s.128(5); CGST Act s.36) [VERIFY] | Deleted |
| Security, access and audit logs | 400 days in India (≥ 180 days CERT-In; ≥ 1 year DPDP Rules) | Deleted; the hash-chained audit ledger keeps event metadata for 8 years [REC] |
| AI prompts and outputs | Kept with the document or conversation they belong to; standalone chats 2 years [REC] | Deleted |
| Support tickets and grievances | 3 years after closure [REC] | Deleted |
| Call recordings (with notice) | Sales 90 days; support 180 days; longer only for an open dispute (R4) | Deleted |
| Marketing consents and opt-outs | Until withdrawn; opt-out suppression record kept as long as needed to honour it | — |
| Inactive free accounts | After 3 years of inactivity, 48 hours' notice, then closure (voluntary application of Rule 8) [REC] | Export window, then deletion |
| Marketplace engagement records | 8 years after engagement end [REC] | Deleted |

**Build notes (O.11).** This table is rendered from the retention-class registry (P04/P20); classes, not copied numbers, drive deletion jobs, so a change here is a rule-pack release, not a code change (NN-12, NN-30).

---

## O.12 Accessibility Statement (POL-LD-12)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-12 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Accessibility lead |
| Counsel review required | Light — statutory references; complaint route |
| Applicable law | Rights of Persons with Disabilities Act 2016 ss.40, 42, 46, 89; RPwD Rules 2017 Rule 15 (as amended) [VERIFY]; IS 17802 (Parts 1–2); GIGW 3.0; WCAG 2.2 |
| Related codes | NN-28; LG-133–137 |

**1. Our commitment.** LawDocs aims to be usable by everyone, including people who are blind or have low vision, are deaf or hard of hearing, or have motor, cognitive or speech disabilities. We design and test to **WCAG 2.2 Level AA** and **IS 17802 (Parts 1 and 2)**, with GIGW 3.0 as a reference, across the website, web app and mobile apps [REC]. We do not use accessibility overlay widgets; accessibility is built into the product (NN-28).

**2. What you can do.** Navigate fully by keyboard; use screen readers (NVDA, JAWS, VoiceOver, TalkBack); zoom to 400% without loss of content; choose text size, spacing, high-contrast and dark themes, reduced motion; read captions and transcripts on all videos; use Indian Sign Language versions of core tutorials (rolling out); choose identity-verification and signing options that do not depend on sight, hearing or face liveness (for example, DSC or assisted verification); ask for extra time on time-limited steps; and request any document in an accessible format.

**3. Conformance status.** Partially conformant [update at each wave]. We test every release with automated checks and manual screen-reader and keyboard testing.

**4. Known limitations** (updated each release).

| Area | Limitation | Workaround | Target fix |
|---|---|---|---|
| Uploaded third-party PDFs | Documents you or others upload may not be tagged | Use the OCR typed copy or request an accessible version | Ongoing (we cannot fix third-party files) |
| ESP signing pages | The ESP's OTP page is outside our control | Use DSC or assisted signing; tell us and we will raise it with the ESP | Per ESP |
| Government portals we link to | Outside our control | Assisted route via support | — |
| `[populate from audit]` | | | |

**5. Feedback and complaints.** Contact `[Support Email]` (subject "Accessibility") or the grievance form; we acknowledge within 24 hours and provide a workaround within 2 business days (POL-LD-09). If you are not satisfied, you may approach the Chief Commissioner or your State Commissioner for Persons with Disabilities [LAW] [VERIFY].

**6. Assessment.** Last assessed `[date]` by `[assessor]`.

---

## O.13 Security and Trust page; Responsible Disclosure Policy (POL-LD-13)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-13 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | `PLT_SECURITY_OFFICER` |
| Counsel review required | Yes — claim wording (NN-20); researcher safe-harbour language given IT Act ss.43, 66 |
| Applicable law | IT Act 2000 ss.43, 66, 70B; CERT-In Directions 2022; DPDP Rules 2025 Rules 6–7; PCI DSS v4.0.1 (SAQ A); RFC 9116 (security.txt) |
| Related codes | NN-02, NN-09, NN-17, NN-20, NN-22, NN-25, NN-27; CH-19; LG-079, LG-148 |

### Claim discipline (binding for this page and all marketing)

| Never say (until evidenced) | Say instead | Evidence needed to upgrade wording |
|---|---|---|
| "ISO 27001 certified" | "Our information security management system is designed to align with ISO/IEC 27001:2022" | Certificate from an accredited certification body, with scope and certificate number |
| "SOC 2 compliant/certified" | "We are preparing for a SOC 2 Type I examination" | Issued SOC 2 report (Type I or II), available under NDA; never "certified" |
| "PCI DSS certified" | "Card payments are handled on Razorpay's hosted checkout. LawDocs never sees or stores your card number" | Annual SAQ A attestation on file: then "We complete an annual PCI DSS SAQ A self-assessment" (LG-148) |
| "Bank-grade", "unhackable", "military-grade" | Describe the control (e.g., "AES-256 encryption at rest") | — |
| "Government-approved" | Name the specific licence or empanelment, with number | Licence document |

The page shows each claim with an "as of" date; the CMS blocks the left-column phrases (NN-20).

### Trust page copy (draft)

**Your data stays in India.** Production systems run in AWS Mumbai with disaster recovery in Hyderabad. [Publish only after hosting evidence is recorded — content deck §2.4; NN-20; W.9 LA-34]

**Encryption.** TLS 1.2+ in transit; AES-256 at rest with keys managed in AWS KMS, separated per customer.

**Originals that cannot be altered.** Original uploads and signed files are stored in write-once (Object Lock) storage with a SHA-256 fingerprint taken on upload.

**An audit trail no one can rewrite.** Every change is recorded in an append-only, hash-chained ledger. Corrections are new entries that reference the original — even our administrators cannot edit history.

**You control our access.** LawDocs staff and professionals can enter your workspace only through a time-limited access grant you approve. You see every access in your access-transparency log. Emergency access needs two approvals and is reported to you within 24 hours.

**AI with boundaries.** Vidhi processes personal data only through in-country AI endpoints and never trains on your data.

**Payments.** Hosted checkout through Razorpay; no card data on our systems.

**Incidents.** We report the cyber incidents listed in the CERT-In Directions 2022 to CERT-In within 6 hours of noticing them, and notify affected users and the Data Protection Board as the DPDP Rules require; business customers receive notice within the period in their agreement.

**Testing.** VAPT by a CERT-In-empanelled auditor `[frequency]`; summary for business customers under NDA.

**Sub-processors.** `[Generated list: name, purpose, data, region]`.

### Responsible Disclosure Policy (draft)

1. **Scope.** `*.lawdocs.in`, the LawDocs mobile apps and public APIs. Out of scope: third-party services (ESPs, Razorpay, government portals), physical or social-engineering attacks, denial-of-service, and spam or volumetric testing.
2. **How to report.** `security@lawdocs.in` [VERIFY: mailbox] or the form at `/trust/responsible-disclosure`; PGP key and contact in `/.well-known/security.txt` (RFC 9116). Include steps to reproduce and impact.
3. **Rules.** Test only with accounts you own; do not access, change or keep other users' data — stop and report as soon as you see any; do not degrade the service; give us reasonable time (90 days by default) to fix before public disclosure.
4. **Our commitments.** Acknowledge within 2 business days; triage within 7 days; keep you informed; credit you in our hall of fame if you wish.
5. **Good-faith research.** If you follow this policy, we will not initiate legal action or a complaint against you for your research, and we will say so to any authority that asks. *Drafting note:* Indian law offers no statutory researcher safe harbour; unauthorised access remains within IT Act ss.43/66 exposure, and we cannot bind the State. Keep this wording as a contractual undertaking only [COUNSEL].
6. **Rewards.** Rewards are discretionary and currently `[not offered]` (`eng.disclosure.rewards.enabled` = false); we will announce a bounty programme here if we start one.

---
## O.14 `[Consumer Help Brand]` — Terms of Service and Fee and Authority Letter (POL-LD-14)

| Field | Value |
|---|---|
| Policy ID / version | POL-LD-14 / `[Version]` |
| Effective date | `[Effective Date]` |
| Owner | Consumer Help reviewer of record + `[Consumer Help Entity]` DPO |
| Counsel review required | Yes — Advocates Act boundary for non-advocate case management; RB-IOS 2026 representation clauses; Insurance Ombudsman Rules 2017 r.14; Consumer Commission agent rules; success-fee legality (champerty, Contract Act s.23); authority-letter stamp duty per State |
| Applicable law | Advocates Act 1961 ss.29, 33, 45; BCI Rules Part VI Ch. II Rules 20–21; Reserve Bank – Integrated Ombudsman Scheme 2026 (Cl. 3(1)(c), 10(1)(b), 10(1)(g), 15) [VERIFY: clause numbers against RBI text]; Insurance Ombudsman Rules 2017 r.14, r.17; Consumer Protection Act 2019; Indian Contract Act 1872 ss.23, 182–238 (agency); CICRA 2005 s.21; DPDP Act 2023 s.17(1)(a) |
| Related codes | NN-05, NN-13, NN-20, NN-22, NN-23, NN-41, NN-50; D-06; CH-22, CH-31; LG-059, LG-150, LG-171, LG-172; R2 §0, §5; R6 §R6.4 |

*Drafting note — structure.* `[Consumer Help Brand]` is operated by `[Consumer Help Entity]`, a separate company with its own GSTIN, bank account, Razorpay merchant account, privacy notice, Grievance Officer and DPO (R2 §5.6). It employs **non-advocate case managers** (`OPS_CONSUMER_CASE_MANAGER`). Panel advocates, where needed, are engaged directly by the user for **fixed fees** under POL-LD-06 and never share in any case-management fee (BCI Rules 20–21; R2 §5.1) [LAW]. Success fee stays **OFF** (`chp.fees.success_fee.enabled` Locked) until a written counsel opinion is attached and a checker approves (CH-31) [COUNSEL].

### Part A — Terms of Service

**1. Who we are.** `[Consumer Help Brand]` is a service of `[Consumer Help Entity]` (CIN `[CIN of Consumer Help Entity]`, `[Registered Office of Consumer Help Entity]`). We help individuals organise and pursue grievances about loans, lending, recovery conduct, credit reports, insurance claims, traffic challans and vehicle transactions. We use LawDocs technology under contract; we are a separate business.

**2. What we do.**
1. Understand your problem and tell you, in general terms, which grievance routes exist and their time limits.
2. Collect and organise your evidence (with hashes and timestamps) and prepare letters, complaints and forms for you to review.
3. Track deadlines and replies, and remind you.
4. Where a forum allows a non-advocate representative and you sign an Authority Letter, a named case manager may submit and correspond for you within the scope you approve.
5. Refer you, at your choice, to an independent advocate for legal advice or court representation, at a fixed fee you agree with the advocate.

**3. What we do not do.**
1. **We are not a law firm and our case managers are not advocates.** We do not give legal advice or appear in courts (Advocates Act ss.29, 33) [LAW].
2. **We do not promise any outcome** — no "guaranteed waiver", "settlement guaranteed", "100% success" or "loan closure certificate". Lenders, insurers, ombudsmen and courts decide (NN-20, NN-23).
3. **We never collect, hold or pay your loan dues, settlement amounts, premiums, fines or challans.** You pay the lender, insurer or official portal directly; we charge only our own fee (NN-22).
4. We do not pull your credit report; you upload it or obtain it from the credit information company (CICRA s.21) [LAW] (CH-05).
5. We do not represent you where the forum's rules do not allow it. For example, before the RBI Ombudsman an advocate cannot act as your authorised representative (RB-IOS 2026 Cl. 10(1)(b)) [LAW] [VERIFY], so a non-advocate case manager or you file; before the Insurance Ombudsman you file yourself or through a legal heir, nominee or assignee (Rule 14(1)) [LAW] [VERIFY: practice of the Council for Insurance Ombudsmen].
6. We do not act for lenders or insurers in any matter we handle for you.

**4. Independence and ethical wall.** `[Consumer Help Entity]` is part of the Infrabyx Group, which also serves lenders and insurers through other companies. To protect you: your data is held in a separate system and is never shared with those companies; our staff and panel advocates do not work on lender-side matters; and before accepting your case we run a conflict check that reveals no client names. If a conflict is found, we tell you in general terms and offer self-help tools only, or decline (NN-23).

**5. Your responsibilities.** Give true and complete information and documents; tell us about any case already pending in a court, tribunal, consumer commission or arbitration (it may bar an ombudsman complaint — RB-IOS 2026 Cl. 10(1)) [LAW]; keep paying dues you owe unless a forum orders otherwise; confirm every settlement yourself in the app — we cannot bind you to a settlement (R2 §5.4).

**6. Fees.** Fees are flat per stage and shown before you pay (Part B, Schedule). No hidden charges; government and forum fees, if any, are paid by you directly. Refunds on withdrawal follow the scale in Part B clause 5.

**7. Your data.** Our privacy notice explains how we use your data. We process your case data to pursue your claim; where the law permits, processing necessary to enforce a legal right or claim may be exempt from parts of the DPDP Act (s.17(1)(a)) [LAW] [VERIFY: scope], but we still apply notice, consent, security and retention controls and never use case data for marketing.

**8. Ending the service.** You may withdraw at any time in the app; we stop work, revoke the Authority Letter and refund per the scale. We may stop acting if you give false information, act unlawfully, or abuse our staff, with written reasons.

**9. Complaints.** Grievance Officer `[Consumer Help Grievance Officer name/email]` (POL-LD-09 variant). Disputes: Indian law; you may approach a Consumer Commission; optional mediation through an independent institution (never a Group affiliate by default).

### Part B — Fee and Authority Letter (template; eSigned per case)

> **FEE AND AUTHORITY LETTER**
> Case reference: `LD-GRV-[YYYY]-[NNNNNN]` · Date: `[date]`
>
> **Between** `[Client full name]`, `[address]`, mobile ending `[last 4 digits]` ("**Client**")
> **and** `[Consumer Help Entity]`, CIN `[ ]`, `[Registered Office]`, operating as `[Consumer Help Brand]` ("**Company**").
>
> **1. Matter.** Grievance against `[Opposite party name]` (`[bank / NBFC / insurer / authority]`, `[RBI registration no. / IRDAI reg. no. / other]`) concerning `[loan account / policy / challan / vehicle no.]` — `[one-line description]`.
>
> **2. Case manager.** `[Name]`, employee of the Company, **who is not an advocate**. Replacement only with notice to the Client in the app.
>
> **3. Authority granted (tick only what applies; nothing else is authorised).**
> ☐ (a) Correspond with the opposite party's grievance/nodal officer on the Client's behalf.
> ☐ (b) Obtain information and documents about the account or policy from the opposite party.
> ☐ (c) File and pursue a complaint before `[RBI Ombudsman under RB-IOS 2026 / other forum]` as the Client's authorised representative **other than an advocate**, where that forum permits.
> ☐ (d) Receive copies of communications on the Client's behalf (the Client also receives them).
> ☐ (e) Negotiate proposals — **without authority to accept any settlement, waiver or payment plan**. Every offer is placed before the Client, who alone accepts or rejects it in the app.
>
> **4. Limits.** This letter is not a power of attorney. It does not authorise the Company to: sign any settlement or admission; receive or pay any money for the Client; appear before a court; or engage an advocate in the Client's name without the Client's separate engagement. It covers only the matter in clause 1.
>
> **5. Fees.**
>
> | Stage | Fee (₹, excl. GST) | Payable when |
> |---|---|---|
> | Case assessment and evidence pack | `[ ]` | On signing |
> | Complaint to opposite party (drafting + follow-up for 30 days) | `[ ]` | When filed |
> | Ombudsman / regulator complaint and follow-up | `[ ]` | When filed |
> | Appeal / review stage (if instructed) | `[ ]` | When filed |
> | **Success fee** | **Not applicable** `[COUNSEL: clause appears only if chp.fees.success_fee.enabled; then: "[x]% of amounts actually received by the Client as compensation or refund attributable to the complaint, capped at ₹[ ] and at [10]% (chp.fees.success_fee.cap_pct); not charged on amounts the opposite party had already agreed to pay before this letter, or on statutory automatic compensation; payable by the Client after receipt"]` | — |
>
> GST at the applicable rate is added. **Withdrawal:** stages not started are refunded in full; the current stage is refunded `[50]%` if no document has been filed `[OWNER]`. Panel advocates' fees, if any, are agreed and invoiced separately by the advocate and do not depend on the result.
>
> **6. No guarantee.** The Company has not promised any outcome. The decision rests with the opposite party, the forum or the court.
>
> **7. Ethical wall and data.** The Company confirms the conflict check for this matter returned "no conflict" on `[date]`. Client data is used only for this matter and is not shared with any lender, insurer or other Infrabyx Group company.
>
> **8. Duration and revocation.** Valid from the date above until `[date — max 12 months]` or closure of the matter, whichever is earlier. The Client may revoke it at any time in the app or in writing; revocation is notified to the forum and opposite party where they were informed of this authority.
>
> **9. Stamp duty.** `[State-specific: COUNSEL to confirm whether an authority letter of this kind attracts duty in the Client's State and at what rate]` [VERIFY].
>
> Signed electronically by the Client (`[method]`, `[timestamp]`) and by `[authorised signatory]` for the Company.

**Build notes (O.14).** The letter is a `tpl` template under the `chp` brand; checkbox 3(c) is enabled only when the forum's representation rule (rule data in `rul`) allows a non-advocate; the success-fee row is hidden unless the Locked switch is released by maker-checker with an opinion attached; revocation emits a case event in P15; help key `hlp.chp.authorised_representative`.

---

## O.15 Outlines: DPA, retainer SLA and Enterprise MSA (POL-LD-15 to POL-LD-17)

### O.15.1 Data Processing Addendum for companies (POL-LD-15) — outline

| Clause | Key content |
|---|---|
| 1. Roles | Customer = Data Fiduciary; LawDocs = Data Processor for Customer Data (DPDP s.8(2)); LawDocs = fiduciary for account/billing data and eSign evidence it must keep as ASP [COUNSEL] |
| 2. Instructions | Process only on documented instructions (the customer's configuration and use are instructions); notify if an instruction appears unlawful |
| 3. Personnel | Confidentiality undertakings; access only via delivery grants (NN-17); background checks |
| 4. Security | Annex of measures (Appendix on security, POL-LD-13); India residency (NN-25); encryption; Object Lock; audit ledger |
| 5. Sub-processors | Published list; ≥ 30 days' prior notice of additions; objection right with termination and pro-rata refund as remedy |
| 6. Assistance | Data-principal requests (forward within 2 business days; tooling in Privacy Centre); DPIAs; Board enquiries |
| 7. Breach | Notify customer without undue delay and in any case within `[2]` hours of confirmation [REC, LDC parity]; information to support the customer's DPDP Rule 7 and CERT-In reports |
| 8. AI | No training on Customer Data; in-region endpoints for personal data; AI features configurable by the customer (NN-15) |
| 9. Transfers | No transfer outside India without the customer's written approval and a transfer assessment; s.16 restrictions |
| 10. Return and deletion | Export in `LD-EXPORT-1.0` at any time; deletion within 30 days after the export window with a deletion certificate; legal hold exceptions |
| 11. Audit | Assurance pack, questionnaires, reports under NDA; on-site or remote audit once a year with notice; regulator access where the customer is a regulated entity (RBI/SEBI/IRDAI outsourcing requirements) [VERIFY: paragraph references] |
| 12. Ecosystem | Cross-product sharing only through the customer's configured, consented connectors (NN-24) |
| 13. Liability | As the MSA, with the data-protection super-cap |
| Annexes | A. Processing description (subject matter, duration, purposes, data principals, categories) · B. Security measures · C. Sub-processors · D. GDPR SCC module 2/3 and UK Addendum (only where applicable) |

### O.15.2 Retainer SLA template (POL-LD-16) — outline

| Clause | Key content |
|---|---|
| 1. Parties and structure | Client; `[LawDocs Operating Entity]` for technology, administration and non-reserved services; **named advocate or advocates' firm, by separate engagement, for legal advice** (NN-41; R6 §R6.2.7) |
| 2. Scope | Service catalogue lines; hour bank; exclusions; reserved services carved out to the professional's engagement |
| 3. People | Dedicated RM as delegated maker (`ORG_DELEGATED_MAKER`); client checker; backups; replacement notice |
| 4. Access | Delivery grant scope, duration, renewal; access-transparency log; break-glass rules (NN-17) |
| 5. Service levels | Response and turnaround by request class (e.g., P1 regulatory deadline same day; standard contract review `[3]` business days); measurement from the `wf` clock; exclusions (client delays, third-party portals) |
| 6. Reporting | Monthly MIS: requests, SLA attainment, hours used, open/interim/waiting items, evidence class for any savings figure (NN-36) |
| 7. Service credits | `[x]%` of monthly fee per missed SLA class, capped at `[y]%`; sole financial remedy for SLA misses, without prejudice to termination for persistent failure |
| 8. Fees | Monthly fee; hour-bank top-ups; government fees at actuals; separate invoices for advocate fees (RCM where applicable) [TAX MEMO] |
| 9. Term, renewal, exit | Minimum term; renewal notice; exit assistance and export (NN-11) |
| 10. Execution | eSigned in LawDocs; changes by signed change order |

### O.15.3 Enterprise Master Services Agreement (POL-LD-17) — outline

| Clause | Key content |
|---|---|
| 1. Structure | MSA + order forms + DPA + SLA + security annex; order of precedence |
| 2. Services | Subscription, credits, implementation, delivery services; reserved services excluded and supplied by professionals under their own engagements |
| 3. Customer obligations | Lawful use; admin control; user conduct (POL-LD-10); accuracy of master data |
| 4. Fees and taxes | Annual invoicing; price protection for the initial term; TDS certificates; GST |
| 5. Confidentiality | Mutual; 5 years post-term; trade secrets indefinitely |
| 6. Data protection and security | DPA incorporated; India residency; incident notice; assurance rights |
| 7. IP | LawDocs owns the platform and templates; customer owns its data and outputs; template licence; feedback |
| 8. Warranties | Material conformance with documentation; no malicious code; professional services with reasonable skill and care |
| 9. Indemnities | IP infringement (LawDocs); unlawful content or data (customer) |
| 10. Liability | 12 months' fees cap; super-cap for data protection and confidentiality `[2–3×]` [OWNER]; uncapped for fraud, wilful misconduct |
| 11. Term and termination | For convenience after the initial term; for cause with cure period; effect; exit assistance and export |
| 12. Ecosystem and third parties | Connectors at customer's choice; no ASP sub-letting (NN-06) |
| 13. Regulated customers | Outsourcing and IT-vendor clauses for RBI/SEBI/IRDAI/IFSCA entities (audit, regulator access, business continuity, sub-contracting) [VERIFY: current directions] |
| 14. Disputes | Escalation; mediation (Commercial Courts Act s.12A where applicable); arbitration seated at `[Seat City]` under an independent institution; no Group affiliate unless agreed after the dispute arises |
| 15. General | Assignment; force majeure; notices; anti-bribery; non-solicitation (mutual, 12 months) [OWNER]; electronic execution |

---

## O.16 Verification items and open items

### O.16.1 Verification before publication (NN-38)

| # | Item | Affects | Where to verify |
|---|---|---|---|
| V-O-01 | DPDP commencement dates and any acceleration of Rule 4 / core duties | POL-LD-01 §§13, 15, 20 | e-Gazette; MeitY |
| V-O-02 | DPDP s.5(3) language option; s.7 clause letters; Rule 14(3) 90-day outer limit | POL-LD-01 | Act and Rules text |
| V-O-03 | IT Rules 2021 as amended 2026: grievance 7 days, 36 h / 2 h / 3 h clocks, three-monthly reminders, SGI labelling r.2(1)(wa) and r.3(3) | POL-LD-02, -04, -09 | e-Gazette (G.S.R. of 10 Feb 2026) |
| V-O-04 | E-Commerce Rules 2020 r.4 and r.5 sub-rule numbers (grievance 48 h/1 month, cancellation-charge parity, ranking disclosure) and any later amendment | POL-LD-05, -06, -09 | Department of Consumer Affairs |
| V-O-05 | Bedrock India retention and human-review terms; Anthropic Usage Policy text effective 12 Nov 2026 | POL-LD-01 §8, POL-LD-04 | AWS service terms; anthropic.com/legal/aup |
| V-O-06 | State stamp-duty refund periods, deductions and e-stamp cancellation procedures for launch States | POL-LD-05 §7 | State Stamp Acts/rules; SHCIL |
| V-O-07 | Authority-letter stamp duty per State | POL-LD-14 Part B §9 | State schedules |
| V-O-08 | RB-IOS 2026 clause numbers (representation, limitation, award acceptance) | POL-LD-14 | RBI notification of 16 Jan 2026 |
| V-O-09 | Who may sign BSA s.63(4) Part B after *Pune Bar Association* (SC, 22 May 2026) | POL-LD-03 §10 | Judgment text |
| V-O-10 | Registration Act s.17 State amendments; TPA attestation requirements; any State e-notarisation | POL-LD-03 §6 | Bare Acts; State notifications |
| V-O-11 | Companies Act s.128(5) and CGST s.36 retention basis; Income-tax Act 2025 s.393 table entries for TDS | POL-LD-01 §11, -07, -11 | Statute; CBDT/CBIC |
| V-O-12 | NeGD position on user-directed saving of DigiLocker documents | POL-LD-01 §6, -11 | NeGD written confirmation |
| V-O-13 | RPwD complaint route and Rule 15 status after *Rajive Raturi* | POL-LD-12 | DEPwD |
| V-O-14 | *Emaar MGF v. Aftab Singh* citation; Mediation Act 2023 online-mediation provisions in force | POL-LD-02 §18 | SC reports; e-Gazette |

### O.16.2 Open items (candidates for Appendix W)

| ID | Item | Owner | Default until closed |
|---|---|---|---|
| OI-O-01 | Fiduciary/processor characterisation of the marketplace engagement workspace | Counsel + DPO | LawDocs as processor; Partner as independent fiduciary (POL-LD-07 §7) |
| OI-O-02 | Consumer liability cap amount and data-breach super-cap | Owner + counsel | Higher of 12 months' fees and ₹`[amount]`; 2× for business |
| OI-O-03 | First-purchase refund window (`bil.refunds.new_subscription_window_days`) | Owner | 7 days |
| OI-O-04 | Milestone deemed-acceptance period | Owner | 5 business days after two reminders |
| OI-O-05 | Success-fee switch for `[Consumer Help Brand]` | Counsel + owner | OFF, Locked |
| OI-O-06 | Consumer Help withdrawal refund scale | Owner | 50% of current stage if nothing filed |
| OI-O-07 | Seat city for business arbitration and court jurisdiction | Owner | `[Seat City]` placeholder blocks publication |
| OI-O-08 | Researcher safe-harbour wording | Counsel | Contractual undertaking only |
| OI-O-09 | Whether to appoint a GDPR Art. 27 representative | DPO | Not appointed; EU supplement OFF |
| OI-O-10 | Error range `LD-WEB-090`–`099` and `web.legal.*` keys — confirm with P21/Appendix R authors | Pack lead | As proposed in O.0 |
