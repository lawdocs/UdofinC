# R3 — Legal and Regulatory Baseline for LawDocs (lawdocs.in)

> **Stream:** R3, LawDocs Build Prompt Pack. **Prepared:** 25 October 2026. **Feeds:** the LawDocs rules register and the phase files for identity/onboarding, eSign/eStamp, vault/DMS, Vidhi AI, marketplace, billing, tax services, litigation, HRMS, accessibility and website.
> **Precedence:** on *what the law says*, this file governs a phase file until counsel signs off. A `[VERIFY]` row never drives a hard block; it drives a HIGH advisory with the feature flag OFF.
> **Style reference:** LDC Appendix G (`LR-*`) and Appendix Q. Rows imported from LDC and not re-fetched today are **V-REG**.

---

## 0. How to read this register

| Field | Meaning |
|---|---|
| **Rule ID** | `LG-NNN`; never reused; superseded rows keep their ID |
| **Instrument / Exact provision** | Statute, rules, regulations, directions, specification or judgment, with section/rule/para and the substance that drives product logic |
| **Effective** | Commencement or effective date |
| **Design implication** | What LawDocs must build, block, disclose, log or route |
| **Confidence** | **V-WEB** checked today on the authority's own site (URL in §18). **V-SEC** checked today against a reputable secondary source. **V-REG** carried from the LDC register/appendices. **[VERIFY]** analyst knowledge or unresolved — verify before the feature leaves its flag. A trailing "[VERIFY x]" on a verified row means only point *x* is open. |

**Session limitations.** `shcilestamp.com` returned a client error; one `rbidocs.rbi.org.in` PDF returned a human-verification page; the shared web-search budget ran out part-way through Topic 9, so rows on BCI's 2025 circulars, the ICAI Code edition, ICSI guidance, ERI types, GSP onboarding, the accessibility judgments, E-Commerce sub-rules and RBI PA paragraphs are `[VERIFY]` or `V-REG`. No domain was bypassed with curl or scripts.

**Headline conclusions.**
1. **LawDocs cannot be an Aadhaar requesting entity.** Its lawful Aadhaar routes are (a) **Aadhaar eSign via a licensed ESP** and (b) **offline verification as a registered OVSE** (Aadhaar App verifiable credential, secure QR, e-Aadhaar, offline XML) under the December 2025 amendment regulations. The 2025 "good governance" rules are a slow, discretionary path, not a login basis.
2. **CKYC, credit-bureau pulls and direct PAN verification are closed to a non-regulated platform.** DigiLocker (Requester ToU, June 2025) is the lawful substitute — but its ToU forbids storing pulled documents beyond the permitted purpose, which collides with a "keep forever" vault.
3. **No percentage commission, ratings or paid ranking for advocates; no listing of practising CAs on an aggregator.** Madras HC (2024) ruled against Sulekha/Justdial-type legal listings (SC notice Nov 2024, no stay reported); ICAI's 23 Oct 2019 announcement bars CA aggregator listings.

---

## 1. Electronic signatures and eSign

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-001 | **IT Act 2000 s.3A** — electronic signature/authentication technique that is reliable and **specified in the Second Schedule**. | 27 Oct 2009 (S.O. 2689) | Only **ESP eSign** and **CA-issued DSC** are s.3A signatures. Click-to-accept or drawn signatures are "e-acceptance" (s.10A) — never labelled "eSign". | V-WEB (commencement S.O.); [VERIFY s.3A wording] |
| LG-002 | **IT Act s.4** (electronic records), **s.5** (electronic signatures satisfy signature requirements), **s.10A** (e-contracts not unenforceable for that reason alone). | 17 Oct 2000; s.10A 27 Oct 2009 | Contract engine logs offer/acceptance events (s.10A) separately from signature events (s.5); execution clause cites ss.4, 5, 10A. | [VERIFY wording] |
| LG-003 | **IT Act First Schedule** as amended by **S.O. 4720(E), 26 Sep 2022** (Gazette No. 4510, 4 Oct 2022). **Entry 1:** negotiable instruments *other than* a cheque, or a demand promissory note/bill of exchange issued in favour of or endorsed by an RBI/NHB/SEBI/IRDAI/PFRDA-regulated entity. **Entry 2:** powers-of-attorney, *except* those empowering such a regulated entity to act for the executant. **Entry 3:** trusts (s.3 Indian Trusts Act). **Entry 4:** wills and other testamentary dispositions (s.2(h) Indian Succession Act). **Entry 5** (contracts for sale/conveyance of immovable property): **omitted**. | 4 Oct 2022 | **Locked document-type gate:** no eSign/DSC execution of wills/codicils, trust deeds, ordinary POAs, or promissory notes/bills not in favour of a listed regulated entity → wet-ink pack (witness/notary/registration checklist). Agreements to sell immovable property may be eSigned; registration and stamp duty still apply (LG-104, LG-096). | **V-WEB** |
| LG-004 | **IT Act Second Schedule** — eSign using Aadhaar e-KYC (G.S.R. 61(E), 27 Jan 2015); other e-KYC services (S.O. 1119(E), 1 Mar 2019); trusted third-party key creation and remote key storage (S.O. 3472(E), 29 Sep 2020). | as stated | eSign is not Aadhaar-only: support account-based eSign (API 3.x) for users without Aadhaar-linked mobile, NRIs and foreign nationals. | V-WEB (titles); [VERIFY Schedule text] |
| LG-005 | **CCA ESP list:** eMudhra (licence to 6 Nov 2028), C-DAC (28 Jun 2030), Capricorn (shown to **15 May 2026**), Protean (shown to **26 Oct 2026**), Verasys (22 Jul 2028), CSC e-Gov (15 May 2029), CDSL Ventures (6 Jan 2030). | as listed | ESP registry is data: nightly job blocks routing to an ESP whose CA licence date has passed until renewal evidence is recorded; Capricorn and Protean flagged `RENEWAL_UNCONFIRMED`; multi-ESP failover by default. | **V-WEB** |
| LG-006 | **eSign API v2.1** (4 May 2018; upd. 10 Aug 2020): `authMode` 1 OTP ("OTP class"), 2 fingerprint, 3 iris ("biometric class"); consent `sc="Y"` mandatory — ASP must obtain explicit informed consent (e-KYC retrieval, DSC application, key generation, CSR, one-time hash signing, key deletion) and must not call the API without it; ASP XML-signs requests; **one SHA-256 hash per request**; no combining documents; timestamp within 30 min; unique txn ID; ASP stores response code in its audit log; `PKCS7pdf` embeds chain, CRL/OCSP and timestamp; certificate is one-time, key deleted. | 10 Aug 2020 | Versioned consent screen per signer per document; hash the **final** locked PDF after stamping; one ceremony per document; use PKCS7pdf for long-term validation; evidence record = consent version, request XML, signed response, code, txn ID, hash, device/IP, timestamps. | **V-WEB** |
| LG-007 | **CCA eSign FAQ:** only CAs operate as ESPs; an external agency can be an ASP; "ASP can avail service from ESP for integrating eSign service **only for applications owned or operated by them**"; "obtaining consent from the signer and its logs should be with ASP only". | current | **No sub-letting.** LawDocs cannot resell its ASP access to tenants, third parties or Finbyx/Udofin/Equator/LDC. Ecosystem apps either redirect signers into a **LawDocs-hosted ceremony** or sign their own ASP agreements. The gateway "eSign API" only creates LawDocs-hosted sessions; consent and logs never leave LawDocs. | **V-WEB** |
| LG-008 | **eSign API v3.3** (9 Dec 2020): account-based eSign with Aadhaar offline XML, bank, organisational, PAN and foreign-national e-KYC; PIN + SMS-OTP/TOTP/MAT/FIDO2/PUBSIGN; `checkStatus` kept ≥ 30 days; **ASP must integrate with other ESPs within one month of onboarding with the first**; FIDO/public-key logs archived **7 years after account deactivation**. | 9 Dec 2020 | Adapter supports 2.1 and 3.x; second ESP live within 30 days of the first; eSign evidence retained ≥ 7 years after the later of signing and account closure (longer if limitation requires, LG-092). | **V-WEB** |
| LG-009 | **CCA eSign FAQ (PDF)** Q11–Q12, Q16, Q19, Q21, Q29: ASP may be "a legal entity registered in India"; onboarding per ESP criteria and CCA audit; application logon recommended before e-KYC OTP; classes "e-KYC – OTP" / "e-KYC – Biometric"; security logs retained and audited; ASP and ESP archive their own logs. | current | Budget an ASP audit pre-launch [VERIFY frequency in ESP contract]; MFA login before the eSign step; show certificate class on the signature panel. | **V-WEB** |
| LG-010 | **CCA eSign Empanelment Guidelines** (1 May 2017): ESPs are licensed CAs with e-KYC access and a CCA-empanelled audit; pricing and disputes are bilateral ASP–ESP matters. | 1 May 2017 | Negotiate SLA, log export and exit terms in each ESP contract. | **V-WEB** |
| LG-011 | **DSC Class 3** — Class 2 discontinued by CCA. | 1 Jan 2021 [VERIFY] | Company signatories use USB-token Class 3 DSC through a local PKCS#11 signing agent; key never leaves token; validate chain and revocation. | [VERIFY] |
| LG-012 | "DocSigner"-type local signing utilities — no CCA instrument located. | — | Treat as a vendor component (signed installer, hash-only transfer); don't name it in user copy until chosen. | [VERIFY] |
| LG-013 | OTP eSign needs the Aadhaar-registered mobile; biometric eSign needs a capture device (UIDAI registered device) [VERIFY RD requirement]. | current | OTP default; biometric only at assisted counters; fallback to 3.x account eSign or DSC. | V-WEB (classes) |
| LG-014 | **Bharatiya Sakshya Adhiniyam 2023 s.86** — court presumes a *secure* electronic record unaltered and a *secure* electronic signature affixed with intent to sign; s.85 (electronic agreements) and s.87 (electronic signature certificates) [VERIFY wording]. | 1 Jul 2024 | Prefer eSign/DSC with full chain and timestamp for anything a user may need to prove; explain the presumption via the "i" button. | V-SEC (s.86) |

## 2. Aadhaar

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-021 | **Aadhaar Act 2016 s.4(3)** (as amended 2019): holder may *voluntarily* use the number for authentication or offline verification; authentication requires informed consent. | 2019 Act published 24 Jul 2019 [VERIFY commencement] | Aadhaar always optional with a visible alternative. | V-SEC |
| LG-022 | **s.4(4):** an entity may perform authentication only if UIDAI is satisfied it (a) meets privacy/security standards and (b)(i) is permitted by a **law made by Parliament** or (b)(ii) seeks it for a purpose **prescribed by the Central Government** in the interest of the State. | 2019 | **LawDocs cannot be an AUA/KUA by contract**; online Aadhaar authentication/e-KYC is out of scope absent a good-governance approval (LG-027). | V-SEC; V-WEB (UIDAI ordinance text) |
| LG-023 | **s.57 omitted** ("Section 57 of the principal Act shall be omitted", cl.23 of the 2019 Ordinance, carried into the Act) after *K.S. Puttaswamy v. UoI* (Aadhaar, 26 Sep 2018) struck down contract-based private use. | 2019 | No "Aadhaar e-KYC login"; consent + contract is not a basis. | V-WEB; [VERIFY judgment citation] |
| LG-024 | **s.8:** authentication with consent; proviso — **alternative means of identification** where authentication fails (illness, injury, age, technical reasons). | 2019 | Every eSign journey has a non-Aadhaar path (3.x account eSign, DSC, wet-ink). | V-SEC |
| LG-025 | **s.8A** offline verification: consent (8A(2)); inform holder of data shared, uses and alternatives (8A(3)); OVSE must **not authenticate, nor collect, use or store the Aadhaar number or biometrics** (8A(4)). | 2019 | Identity proofing via Aadhaar App/QR/e-Aadhaar/XML; store only purpose-limited UIDAI-signed attributes and last 4 digits. | V-SEC |
| LG-026 | **s.29(3)** use/disclosure only for purposes informed in writing in clear language; **s.29(4)** Aadhaar number, demographic information or photograph not to be published/displayed publicly; **s.33A** civil penalty up to **₹1 crore per contravention** + **₹10 lakh/day** continuing (adjudication s.33B; TDSAT appeal s.33C). | 2019 | Purpose statement stored per verification; **OCR auto-masking** of Aadhaar numbers in every uploaded/shared document (last 4 only); public links never expose Aadhaar data. | **V-WEB** |
| LG-027 | **Aadhaar Authentication for Good Governance (Social Welfare, Innovation, Knowledge) Rules 2020** as amended **2025** (PIB 31 Jan 2025): private entities may seek authentication for good governance, ease of living, better access to services, preventing leakage, innovation/knowledge (examples: e-commerce, travel, hospitality, health); application on a portal to a Central/State ministry/department → UIDAI examines → MeitY approves → department notifies. | 31 Jan 2025 | Possible long-path (e.g., department-sponsored legal-aid use); flag `aadhaar.auth.good_governance` OFF; never a dependency. Rule numbers amended not confirmed. | V-WEB (UIDAI release); V-SEC (Khaitan) |
| LG-028 | **Aadhaar (Authentication and Offline Verification) Regulations 2021** (8 Nov 2021): yes/no and e-KYC facilities for REs; offline modes — QR, paperless offline e-KYC XML (last 4 digits + demographics/photo), e-Aadhaar, offline paper, others UIDAI adds; holder may **revoke consent** to stored e-KYC data → delete and acknowledge. | 8 Nov 2021 | Verify UIDAI signatures; "Revoke Aadhaar data" control in the privacy centre deletes attributes and issues an acknowledgement. | V-SEC; [VERIFY reg numbers] |
| LG-029 | **Authentication and Offline Verification Amendment Regulations 2025** (s.54): **Reg 13A** OVSE registration for paperless e-KYC and **Aadhaar Verifiable Credentials** (fees; reasons + 30-day reconsideration on rejection); **Reg 3A** modes incl. **Offline Face Verification** (local match in the Aadhaar application) and AVC selective disclosure; **Reg 2** "Aadhaar Application" (Aadhaar App, mAadhaar); **Reg 23A** surrender duties (logs, grievances, accounts); **Regs 251A–253** penalties and logo use. | Dec 2025 [VERIFY gazette date] | **Register as an OVSE**; face match happens in the Aadhaar App, never in LawDocs; Aadhaar logo only as UIDAI permits. | V-SEC (IndiaLaw) |
| LG-030 | **UIDAI OVSE Playbook** (Jan 2026): registration **required for AVC via Aadhaar App, not for secure QR or e-Aadhaar**; documents — PAN, CIN, profile, self-declaration of compliance and lawful purpose, registered domain, callback URL, **Class 3 public certificate (2-year)**, SVG logo; email submission until portal opens; integration by cross-device QR, app-to-app or web-to-app intent; consent, selective disclosure, **no transmission/storage of Aadhaar number**. | Jan 2026 | Phase 1: QR/e-Aadhaar verification (no registration); Phase 2: AVC after Reg 13A registration. "Verify with Aadhaar App" is the preferred individual KYC path, requesting only name, 18+ flag and (where signing identity must be matched) photo. | **V-WEB** |
| LG-031 | **UIDAI Circular No. 8 of 2025** (18 Jul 2025; FAQs 3 Nov 2025): **ADV applies only to requesting entities** (AUA/KUA, sub-AUA/sub-KUA), not OVSEs or entities holding Aadhaar copies internally. | 18 Jul 2025 | No ADV needed while LawDocs is an OVSE; `aadhaar.storage_mode = NONE` Locked. | V-SEC; [VERIFY circular text] |
| LG-032 | **s.3A:** children enrolled with guardian consent; cancellation option at 18. | 2019 | No Aadhaar flows for minors; accounts 18+ (LG-066). | V-SEC |
| LG-033 | **UIDAI Aadhaar App** release (19 Nov 2025): selective sharing; "proof of presence through offline face verification". | Nov 2025 | Optional proof-of-presence at witnessed signings and before releasing vault items to a nominee. | **V-WEB** |
| LG-034 | Online face authentication (FaceRD) is a requesting-entity facility. | [VERIFY] | No "Aadhaar face login" in LawDocs. | [VERIFY] |

## 3. DigiLocker

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-036 | **IT (Preservation and Retention of Information by Intermediaries Providing Digital Locker Facilities) Rules 2016**, G.S.R. 711(E), 21 Jul 2016: **r.2(1)(l)** DLSP = intermediary (body corporate or agency) authorised to provide locker/gateway/repository; **rr.3, 5(2), 10** Digital Locker Authority licenses/empanels DLSPs; **r.6** facilities in India; **r.12** grievance officer; **r.16** portability; **r.17** audit; **r.20(3)–(4)** offsite DR, no confidential data outside India; **r.21** reasonable security. | 21 Jul 2016 (amended 8 Feb 2017) | LawDocs' vault is **not a Digital Locker** under the Rules: call it "Legal Vault", never "DigiLocker"; adopt the good practices voluntarily (India residency, DR, portability, annual audit). | V-SEC (rule text) |
| LG-037 | **Rule 9A** (G.S.R. 111(E), w.e.f. 8 Feb 2017): issued documents shared from a Digital Locker account are **at par with physical documents**; a document accessed via **URI** is deemed shared by the issuer. | 8 Feb 2017 | Data model distinguishes `DIGILOCKER_URI (Rule 9A)` from `USER_UPLOAD`; only URI-fetched issuer-signed documents get the "verified with issuer" badge, re-validated on display/export. | V-SEC |
| LG-038 | **DigiLocker Requester Terms of Use** (2 Jun 2025): cl.2 onboarding by senior authorised representative, NeGD verification; cl.3 retrieval only, no rebranding, purpose limitation; cl.4(c)–(d), 6(b) explicit informed consent with reason; **cl.4(d), 6(b), 18 no caching/duplicating/storing beyond the permitted duration** unless law requires, nothing outside India; **cl.4(e), 13 incidents and breaches to NeGD within 24 hours**; cl.5 no scraping; **cl.14–15 annual audit by CERT-In-empanelled auditor**; cl.16 7-day rectification, suspension without notice possible; **cl.17 extension to affiliates needs NeGD written approval**; cl.9 no charges now. | 2 Jun 2025 | (a) DigiLocker is the **primary lawful source** for PAN, DL, RC, education and other issued documents; (b) vault stores **URI + metadata + verification result** by default and re-fetches with fresh consent; a retained copy only when the user saves it for a recorded purpose — obtain NeGD's written confirmation [VERIFY]; (c) add the 24-h NeGD clock to the incident runbook; (d) annual CERT-In audit; (e) sister apps cannot use LawDocs' requester integration without NeGD approval. | **V-WEB** |
| LG-039 | **Entity Locker** — Requester API specification (28 Nov 2024) for organisation documents. | 28 Nov 2024 | Company onboarding pulls incorporation, GST and entity-PAN documents with the authorised signatory's consent [VERIFY coverage/eligibility]. | V-SEC (title/date) |
| LG-040 | **DPDP Rules 2025 Rule 10:** verifiable parental consent may use a **virtual token from a Digital Locker service provider**. | 13 May 2027 | If guardian-managed vaults are allowed, use the DigiLocker age token. | V-SEC |
| LG-041 | DigiLocker **Issuer** onboarding. | — | Later option: issue LawDocs/FinLegal Academy certificates into DigiLocker [VERIFY eligibility]. | [VERIFY] |

## 4. CKYC, PAN, GSTIN, MCA

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-046 | **PML (Maintenance of Records) Rules 2005 r.9** (incl. r.9(1A) CKYCR filing) and RBI NBFC KYC Directions 2025 (RBI/DOR/2025-26/361, para 63(9)): reporting entities file with CKYCR and **retrieve using the customer's KYC Identifier with explicit consent**; registration is for RBI/SEBI/IRDAI/PFRDA-regulated institutions. | in force (upd. 29 Dec 2025) | **LawDocs (not a PMLA reporting entity) cannot register with, search or download from CKYCR.** Remove CKYC from onboarding; use DigiLocker + Aadhaar offline. A sister RE's CKYC result is not reused for LawDocs. | V-SEC; V-REG (LR-RBI-039); [VERIFY r.9 sub-rules] |
| LG-047 | **Protean Online PAN Verification** — eligible entities only (~40 classes): banks, NBFCs, PSOs, insurers, MFs, depositories/DPs, KRAs, CICs and other regulated entities; government bodies (GSTN, ONDC etc.); **companies/government deductors with > 500 deductees per quarter**; SFT filers. Modes: screen, file (1,000 PANs), API; DSC required. | current | LawDocs is unlikely to qualify. Use the **DigiLocker PAN card** (issuer-signed) with name match; a vendor PAN API only with a written warranty that its upstream licence covers LawDocs' purpose. | **V-WEB** |
| LG-048 | Income-tax portal pre-login "Verify Your PAN"; TRACES PAN verification is for deductors. | [VERIFY] | User-initiated deep-link only; no automated third-party PAN submission. | [VERIFY] |
| LG-049 | GST public "Search Taxpayer"; programmatic access via GSTN-licensed **GSPs** (public and OTP-consented taxpayer APIs). | [VERIFY GSP onboarding] | Validate GSTIN through a licensed GSP; taxpayer data only with OTP consent. | [VERIFY] |
| LG-050 | **MCA21 V3** master data public view; **Companies Act s.399** inspection on fee; no open third-party API located. | [VERIFY] | Licensed data vendor (lawful-sourcing warranty) or user-initiated lookup; no scraping; store source and fetch date per field. | [VERIFY] |

## 5. Credit information (CICRA 2005)

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-056 | **CICRA s.2(d)** credit information; **s.2(f)** credit institution; **s.2(l)** specified user = credit institution, member CIC (s.15(3)) or persons RBI specifies by regulation. | in force | LawDocs is none of these. | **V-WEB** |
| LG-057 | **s.17(4):** a CIC shall not disclose credit information to any person other than its specified user; specified user shall not disclose further; only for lawful purposes. | in force | **No CIBIL/Experian/Equifax/CRIF pull at onboarding.** | **V-WEB** |
| LG-058 | **s.22:** no access to credit information unless authorised by the Act, other law or court; offence — fine up to **₹1 lakh** plus daily fine; information so obtained unusable. | in force | No "credit score widget" built by LawDocs. | **V-WEB** |
| LG-059 | **s.21:** applicant may obtain the lender's copy of credit information; **s.21(3)** corrections acted on within 30 days. | in force | Loan-grievance service: the **user** uploads their own report; LawDocs drafts s.21(3) dispute letters. | **V-WEB** |
| LG-060 | **CIC Regulations 2006 reg 3** (amended 29 Nov 2021) + RBI specified-user criteria (5 Jan 2022): Indian company, **net worth ≥ ₹2 crore**, resident Indian ownership/control, diversified ownership, **≥ 3 years** information processing, **CISA-certified** IT audit, CIC membership, purpose "support or benefit of credit institutions"; **reg 9** permitted uses include giving a person their own credit information. | 2021–22 | Not a legal-tech onboarding route. CIC consumer "report for self" programmes → redirect to the CIC's own portal; LawDocs receives the report only as a user upload [VERIFY partner terms]. | V-SEC |

## 6. Data protection, intermediary duties, cyber security

### 6A. DPDP Act 2023 and Rules 2025

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-061 | **DPDP Act commencement, G.S.R. 843(E)** (13 Nov 2025): immediately s.2, ss.18–26, 35, 38–43, s.44(1), (3); **after one year** s.6(9), s.27(1)(d); **after 18 months** ss.3–5, s.6(1)–(8), (10), ss.7–17, rest of s.27, ss.28–34, 36, 37 and **s.44(2)** (omission of IT Act s.43A). | 13 Nov 2025 / **13 Nov 2026** / **13 May 2027** | Build to the full regime now; effective-date DPDP obligations in the rules engine. | V-SEC |
| LG-062 | **DPDP Rules 2025, G.S.R. 846(E)** (13 Nov 2025; PIB 14 Nov): Rules 1, 2, 17–21 immediate; **Rule 4** from 13 Nov 2026; Rules 3, 5–16, 22, 23 from **13 May 2027**. MeitY consulted on 22 Jan 2026 on shortening timelines; **not notified** per the latest source reviewed (14 Aug 2026). | as stated | `dpdp.commencement_date` is a Governed parameter so an acceleration ships as a rule-pack release; re-check before launch. | V-SEC; [VERIFY acceleration] |
| LG-063 | **s.4–6; Rule 3:** lawful purpose with consent or legitimate use; standalone, clear, itemised notice with purposes and links to withdraw, exercise rights and complain to the Board; consent free, specific, informed, unconditional, unambiguous, affirmative, data-minimised; withdrawal as easy as giving (s.6(4)). | 13 May 2027 | Per-purpose consent ledger (account, KYC, AI drafting, marketplace referral, marketing, ecosystem sharing, analytics); no bundling; one-tap withdrawal; notice in English or an Eighth-Schedule language [VERIFY s.5(3)]. | V-SEC; V-REG |
| LG-064 | **s.7** legitimate uses incl. voluntarily provided data and **employment purposes** [VERIFY clause letters]. | 13 May 2027 | HRMS relies on employment use with proportionality (LG-167); counterparty data in a user's contract is processed as the user's processor — basis recorded in the ROPA. | [VERIFY] |
| LG-065 | **s.8; Rules 6–8:** reasonable safeguards; **Rule 6(e)** keep logs/data for detection **one year**; **Rule 7** breach — affected principals and the Board **without delay**, detailed Board report **within 72 hours** (extendable on request); **Rule 8** erase when purpose ends, **48-hour** pre-erasure notice for Third-Schedule classes; **Rule 8(3)** keep data, traffic data and logs **≥ one year** from processing. | 13 May 2027 | Log floors = max(1 yr DPDP, 180 days CERT-In, 7 yrs eSign evidence) per log class; incident runbook with CERT-In 6 h, NeGD 24 h, DPDP 72 h; retention engine with legal hold; 48-h notice applied voluntarily. | V-SEC |
| LG-066 | **s.9; Rules 10–11:** child < 18 — verifiable parental consent; no tracking/behavioural monitoring/targeted ads; Rule 11 lawful-guardian consent for persons with disability. | 13 May 2027 | Accounts **18+ only**; guardian flows require verified guardianship proof [VERIFY acceptable proofs]. | V-SEC; V-REG |
| LG-067 | **s.10; Rule 13** Significant Data Fiduciary — DPO in India, independent audit, DPIA [VERIFY Rule 13 content]. | on notification | Design as if SDF: DPO, annual DPIA and audit, algorithmic risk assessment of Vidhi AI. | V-REG |
| LG-068 | **ss.11–14; Rule 14:** access, correction, erasure, grievance, **nomination**; **Rule 14(3)** respond within a reasonable period **≤ 90 days**. | 13 May 2027 | Privacy-request tracker (internal SLA 30 days); vault **nominee** release only after verified death/incapacity documents. | V-SEC |
| LG-069 | **s.16; Rule 15:** transfers abroad allowed save to restricted countries, subject to Government orders; stricter sectoral laws prevail. | 13 May 2027 | India hosting by default; Claude API calls are cross-border transfers — minimise/pseudonymise, contract no-training and zero retention, log in transfer register [VERIFY regional processing options]. | V-SEC |
| LG-070 | **s.6(7)–(9); Rule 4** consent managers registered with the Board. | **13 Nov 2026** | Adapter to accept consent-manager artefacts; LawDocs does not become one. | V-SEC |
| LG-071 | **s.33 + Schedule:** up to ₹250 crore (security safeguards), ₹200 crore (breach notice; children), ₹50 crore residual [VERIFY rows]. | 13 May 2027 | Risk register and "penalties avoided" page (conservative). | V-REG |
| LG-072 | Roles: LawDocs is **fiduciary** for its users/leads/visitors and **processor** for company tenants' data (s.8(2) contract). | — | DPA template, sub-processor list (cloud, ESPs, Razorpay, Anthropic, messaging), processor-to-tenant breach notice (2 h, as LDC Q). | V-REG |

### 6B. IT Act legacy privacy, intermediary rules, CERT-In

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-075 | **IT Act s.43A + SPDI Rules 2011:** SPDI includes **passwords**, financial and biometric data (r.3); privacy policy (r.4); written consent (r.5); disclosure with consent (r.6); ISO 27001 as reasonable security (r.8). s.43A omitted only from **13 May 2027**. | 11 Apr 2011 → 13 May 2027 | SPDI-compliant privacy policy and consent until May 2027 — directly relevant to the "password tracker" (Challenge 7). | V-REG; [VERIFY rule numbers] |
| LG-076 | **IT Act s.66C** (fraudulent/dishonest use of another's password or unique identification feature); **s.72A** (disclosure in breach of lawful contract). | 27 Oct 2009 | Any credential access is named, logged and attributable. | [VERIFY wording] |
| LG-077 | **IT (Intermediary Guidelines and Digital Media Ethics Code) Rules 2021**, amended by **Amendment Rules 2026** (notified 10 Feb 2026): **r.3(1)(c)** user reminders **every three months**; **r.3(1)(d)** takedown on court/government order within **3 h** (was 36 h); **r.3(2)(a)(i)** grievance resolution within **7 days** (was 15); prohibited-content complaints **36 h** (was 72 h); **r.3(2)(b)** intimate imagery **2 h** (was 24 h); acknowledgement 24 h [VERIFY post-2026 text]. | **20 Feb 2026** | LawDocs hosts user content and listings → intermediary. Grievance workflow: ack ≤ 24 h, resolve ≤ 7 days (Locked), 36 h prohibited content, 3 h order-based takedown with 24×7 on-call; quarterly terms reminder; grievance officer published. | V-SEC |
| LG-078 | **2026 Amendment r.2(1)(wa), r.3(3)** synthetically generated information (SGI): audio/visual content made to look real; **excludes text-only, routine editing and document preparation**; enablers must warn users, prevent unlawful SGI (incl. **false documents**), and label SGI (visible label, audio prefix, permanent metadata). | 20 Feb 2026 | Vidhi text drafting is outside SGI; **AI voice calls, avatars and generated images are SGI** → label + provenance metadata. Guard-rail: AI refuses to fabricate official-looking records (stamp certificates, court orders, IDs). | V-SEC |
| LG-079 | **CERT-In Directions** under s.70B(6), 28 Apr 2022: (i) NTP sync to **NIC/NPL**; (ii) report listed incidents **within 6 h**; (iii) point of contact; (iv) ICT logs **180 days in India**; (v) cloud/VPS/VPN subscriber data 5 years; (vi) VASP KYC 5 years. | 60 days after issue [VERIFY exact date] | NTP config, CERT-In POC, 6-h clock, India log store (400 days default). | V-SEC; V-REG |
| LG-080 | **CERT-In Comprehensive Cyber Security Audit Policy Guidelines** (25 Jul 2025) [VERIFY applicability]. | 25 Jul 2025 | Annual CERT-In-empanelled audit (also needed under DigiLocker ToU). | V-REG |
| LG-081 | **IT Act s.79** safe harbour conditional on due diligence; Madras HC (2024) denied it to legal-service listing platforms (LG-113). | in force | LawDocs is neutral for advocate particulars; any active selling of legal services by LawDocs loses the intermediary defence for that feature. | V-SEC |

### 6C. Foreign privacy triggers

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-084 | **GDPR Art. 3(2)** — offering goods/services to, or monitoring, people in the EU; Art. 27 representative; Art. 33 72-h breach notice; Ch. V transfers (no India adequacy). | 25 May 2018 | No EU targeting at launch; `EU_RESIDENT` flag routes NRIs in the EU to a GDPR notice, SCCs and (at volume) an Art. 27 representative. | V-REG |
| LG-085 | **UK GDPR / DPA 2018** (as amended by the Data (Use and Access) Act 2025): same territorial test; IDTA/UK Addendum. | in force | Same gating. | V-REG; [VERIFY DUAA changes] |
| LG-086 | **CCPA/CPRA** (Cal. Civ. Code §1798.140(d)): revenue above the CPI-adjusted threshold (US$25 m base), or PI of ≥ 100,000 consumers/households, or ≥ 50% revenue from selling/sharing PI. | in force | Thresholds unlikely at launch; never "sell/share" PI (no ad-tech pixels on vault/drafting pages). | [VERIFY current figure] |

## 7. Electronic evidence, translations and court filing

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-090 | **BSA 2023 s.2(1)(d)** document includes electronic/digital records; **s.57** primary evidence explanations for electronic records; **s.61** electronic record not inadmissible for being electronic, same effect subject to s.63; **s.62** contents proved per s.63. | **1 Jul 2024** | Preserve native files and metadata, never only a rendered copy. | V-SEC; [VERIFY s.57 explanations] |
| LG-091 | **BSA s.63(4) + Schedule:** certificate with **Part A** (party) and **Part B** (expert), identifying the record, device and **hash value**. ***Pune Bar Assn. v. UoI*, 2026 SCC OnLine SC 1297 (22 May 2026, 3 judges)** upheld s.63(4) and the Schedule; hash is "an electronic fingerprint"; Part B may be signed by a s.79A IT Act examiner and possibly other proven experts — scope left open; Madras HC's examiner-only view not binding. | SC 22 May 2026 | **Court-ready evidence pack**: native file, SHA-256/512 computed **at upload** and at export, chain-of-custody log, source metadata, pre-filled Part A for the user, Part B request to LawDocs' forensic expert or an empanelled s.79A examiner. | V-SEC |
| LG-092 | **Limitation Act 1963** (Schedule; ss.3–24): e.g., most contract suits 3 years. | in force | Contract/evidence retention ≥ term + limitation + buffer, never < 7 years; limitation tracker advisory until counsel review. | V-REG |
| LG-093 | **Constitution Art. 348(1)** — SC and HC proceedings in English (Art. 348(2) Hindi/State language in an HC with Presidential consent); **CPC s.137** — subordinate-court language set by the State. | in force | Pleadings module picks court language per forum. | [VERIFY wording] |
| LG-094 | HC rules / Supreme Court Rules 2013 on translations: non-court-language documents need a **certified** translation [VERIFY rule numbers]. | in force | Claude translations labelled "machine translation — draft"; certified-translation service produces the filing copy; originals + typed copies + s.63 certificate filed together. | [VERIFY] |
| LG-095 | **BNSS 2023 s.530** proceedings in electronic mode; HC e-filing rules; eCourts e-filing portal. | 1 Jul 2024 | Export e-filing-ready PDFs (OCR text, bookmarks, pagination, size limits); no automated submission using advocates' credentials. | [VERIFY] |
| LG-096A | eCourts/NJDG case status public; no open commercial API located. | — | Track by user-entered CNR/case number with user-initiated refresh or a licensed partner; no CAPTCHA bypass. | [VERIFY] |

## 8. Stamp duty, e-stamping, registration, notarisation

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-096 | **Indian Stamp Act 1899:** s.3 chargeability; **s.17** stamp **before or at execution**; s.29 who pays; s.33 impounding; **s.35** unstamped instrument inadmissible unless duty + penalty paid; s.2(14) "instrument" covers electronic records (Finance Act 2019, from 1 Jul 2020) [VERIFY]. | 1899; 1 Jul 2020 [VERIFY] | **Locked stamp-before-sign:** signing cannot start until a stamp certificate/franking/GRAS proof is attached and its UIN verified. | [VERIFY text] |
| LG-097 | **State Stamp Acts** (Maharashtra 1958, Karnataka 1957, Rajasthan 1998; Indian Stamp Act as applied in UP/Delhi etc.): rates, articles and modes differ by State [VERIFY inter-State rules]. | in force | Duty calculator = Governed rule pack per State × article with citations; v1 only in counsel-verified States. | [VERIFY] |
| LG-098 | **SHCIL** is the CRA; e-stamping in **23 States/UTs** (Gujarat 2007 first; Meghalaya Nov 2021 latest, per StockHolding 2022); online purchase (self-print, pick-up, courier) or **ACCs** (banks, FIs, licensed vendors, CSCs, co-operatives); public verification; sub-registrars verify and **lock** certificates. | in force | UIN verification on every attached certificate; procurement via an ACC/vendor or SHCIL corporate channel; store PDF, UIN, State, article, amount, purchaser and lock status. | V-WEB; [VERIFY current list] |
| LG-099 | State channels: **Kerala** treasury e-stamp portal; **Maharashtra** SHCIL + **GRAS** + franking; **Haryana** SHCIL + Haryana Stamp (Payment of Duties by Means of Online E-Stamping) Rules 2017; **Karnataka** SHCIL integrated with Kaveri; physical paper persists in some north-eastern States. | as noted | State adapter registry `SHCIL / STATE_PORTAL / GRAS / FRANKING / PHYSICAL`; physical-paper fallback. | V-SEC; [VERIFY] |
| LG-100 | Platform procurement: certificates issue only through the CRA and ACCs/licensed vendors under State rules; a platform may buy **as the user's agent** through them, not sell stamps itself unless licensed (market practice: Leegality BharatStamp, Melento, NeSL). | in force | Duty is a **pass-through** (via PA split settlement, LG-145) plus a disclosed service fee; certificate in the first party's name with real consideration; no "sign first, stamp later". | V-SEC; [VERIFY State vendor rules] |
| LG-101 | NeSL digital document execution (MoF notification of 30 Jun 2020) [VERIFY]. | [VERIFY] | Optional adapter for financial documents in Finbyx/Udofin flows. | [VERIFY] |
| LG-102 | Electronic execution does not remove stamp duty. | in force | Never claim "no stamp paper needed" for chargeable instruments. | V-SEC |
| LG-104 | **Registration Act 1908 s.17(1)(a)–(e)** compulsory registration (gifts; non-testamentary instruments on immovable property ≥ ₹100; **leases year-to-year or > 1 year**; etc.); **s.17(1A)** agreements for s.53A TPA (from 24 Sep 2001); **s.23** presentation within 4 months; **ss.32–33** presentation in person/agent; **s.49** effect of non-registration. | in force | Classifier flags "registration required"; sale deeds and leases > 1 year go to the sub-registrar or State e-registration (e.g., Maharashtra leave-and-licence); no advice to evade registration. | [VERIFY wording] |
| LG-105 | **Registration Bill 2025** (DoLR draft): electronic presentation, Aadhaar or consent-based e-document verification (traditional methods retained), standard templates; adds agreements to sell, developer agreements, POAs for transfer, sale certificates, mortgage-by-deposit terms, merger instruments, decree/award instruments as compulsorily registrable. | draft [VERIFY status] | Governed future rule; classifier ready to add categories if enacted. | V-SEC |
| LG-106 | **Notaries Act 1952; Oaths Act 1969** — affidavits/notarial acts need a notary/oath commissioner; no operational e-notarisation [VERIFY]. | in force | Affidavits produce a print pack + notary appointment service; never present an eSigned affidavit as sworn. | [VERIFY] |
| LG-107 | **Motor Vehicles Act 1988 s.50** — ownership transfer via the registering authority (Vahan Forms 29/30) [VERIFY]. | in force | Vehicle sale agreement + Vahan transfer checklist; no claim of transfer by agreement. | [VERIFY] |

## 9. Professional-conduct rules

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-110 | **Advocates Act 1961 s.29** (only advocates practise law), **s.33** (only advocates practise in courts), **s.35** misconduct, **s.45** illegal practice; *BCI v. A.K. Balaji* (SC 2018) — practice of law includes non-litigation advice [VERIFY citation]. | in force | LawDocs (a company) does not practise law; advisory is by advocates **in their own name**; Vidhi output is legal information/drafting assistance with a human route; full-time employed advocates do not practise (BCI r.49). | [VERIFY] |
| LG-111 | **BCI Rules Part VI Ch II Section IV Rule 36** (amended 2008 after *V.B. Joshi v. UoI*): no solicitation or advertising, direct or indirect; website may show **only** name, address, phone, email, enrolment no./date, State Bar Council, bar-association membership, qualifications, practice areas. | 2008 | Advocate directory renders only `RULE36_V1` fields in neutral order with a disclaimer; **no ratings, reviews, testimonials, fees, photos, badges, paid ranking or "book now"**. | V-SEC; V-REG |
| LG-112 | **BCI Rule 20** (no contingent fee or share of proceeds); **Rule 37** (no permitting one's services/name to aid unauthorised practice by a lay agency); **Rule 49** (no full-time salaried employment while practising); fee-sharing with non-advocates prohibited [VERIFY rule number]. | in force | No success fees; **no percentage, referral or lead fee from advocates**; fees agreed and paid client↔advocate (LawDocs collection rails only if counsel confirms no fee-sharing). | [VERIFY numbers] |
| LG-113 | **Madras HC (DB), P.N. Vignesh petition, 3 Jul 2024:** platforms (Quikr, Sulekha, Justdial) offering "online lawyer services" contravene Rule 36, no s.79 shelter; BCI directed to frame guidelines. ***Sulekha.com v. P.N. Vignesh*, SLP (C) 25794/2024** — SC notice to BCI (reported 13 Nov 2024), tagged with SLP (C) 17844/2024; **no stay reported**. LDC notes BCI advertising directives (Mar 2025) [VERIFY]. | 2024; SC pending | Directory **OFF at launch** pending counsel opinion and SC outcome; clients choose advocates — LawDocs does not match/assign for a fee. | V-SEC |
| LG-114 | **Chartered Accountants Act 1949 First Schedule Part I** cl.(2) fee/profit sharing with non-members, cl.(3) accepting non-member profit share, cl.(6) solicitation, cl.(7) advertising. | in force | No commission from practising CAs; no paid listing. | V-REG; V-SEC |
| LG-115 | **ICAI Ethical Standards Board announcement, 23 Oct 2019:** members in practice may **not list on online application-based service aggregators**; misconduct under cl.(6)/(7) even if no service is delivered through the platform. | 23 Oct 2019 | **Practising-CA listing OFF**; LawDocs-employed CAs deliver non-attest services as employees. | V-SEC |
| LG-116 | ICAI Code of Ethics current edition (brief: 13th edition from 1 Apr 2026). | [VERIFY] | Re-check online-presence guidance before CA-facing features. | [VERIFY] |
| LG-117 | **Company Secretaries Act 1980 First Schedule Part I** (analogous clauses) and ICSI advertisement guidance [VERIFY]. | in force | PCS listing OFF pending opinion; certification only by an independent PCS engaged directly. | V-REG |
| LG-118 | BCI Foreign Lawyers and Foreign Law Firms Rules 2022 (notified Mar 2023) [VERIFY]. | Mar 2023 | Not applicable to v1; no foreign professionals for Indian-law advice. | [VERIFY] |
| LG-119 | AI legal assistance — no specific statute; risk framed by Advocates Act ss.29/33 and BCI Rule 37. | — | Vidhi disclaims advice, never claims to be a lawyer, escalates strategy/opinions/representation to a named advocate. | [INTERP] |

## 10. Tax-filing intermediaries

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-123 | **Income-tax Act 2025 / Income-tax Rules 2026** from tax year 2026-27; 1961 Act for earlier years. | 1 Apr 2026 | Tax module keyed by year and regime [VERIFY form serials]. | V-REG |
| LG-124 | **e-Return Intermediary (ERI) scheme** — Type 1 (portal/utility), Type 2 (own software via API), Type 3 (software/API for other ERIs); eligibility and security audit [VERIFY scheme text]. | [VERIFY] | Lawful route for "the team files returns": register as an **API ERI**, add clients via the portal's OTP consent; the **taxpayer verifies** (Aadhaar-OTP/bank/demat EVC, DSC or ITR-V). | [VERIFY] |
| LG-125 | **Income-tax Act 1961 s.140** (2025 Act equivalent): return verified by the assessee or prescribed person; representatives only in specified cases. | in force | Staff never verify returns, never receive OTPs, never use client DSCs. | [VERIFY] |
| LG-126 | Portal terms (e-filing, GST, MCA, TRACES, CERSAI, RBI CIMS/DAKSH/PRAVAAH, CICs) issue credentials to named users [VERIFY each]. | — | Use delegation mechanisms (Challenge 7). | [VERIFY] |
| LG-127 | **CGST Act s.48; CGST Rules r.83** GST practitioners; **Form PCT-05** authorisation; taxpayer confirms returns. | in force | GST filing by enrolled practitioners under PCT-05 using their own logins; GSP API data with OTP consent. | [VERIFY wording] |
| LG-128 | **CGST Act s.36** — accounts retained 72 months from the annual-return due date [VERIFY]. | in force | Tax-document retention ≥ 8 years. | [VERIFY] |
| LG-129 | TDS statements via RPU/FVU uploaded by the deductor (or ERI); TRACES for certificates. | [VERIFY] | LawDocs prepares; deductor uploads/verifies. | [VERIFY] |
| LG-130 | GST on LawDocs' services (CGST r.46 invoices; **e-invoicing** above ₹5 crore AATO, r.48(4)); advocate services to business entities under **reverse charge** (Notification 13/2017-CT(Rate)) [VERIFY]. | in force | GST-compliant invoices; RCM flag on advocate-to-business invoices raised in the advocate's name. | V-REG; [VERIFY RCM] |

## 11. Accessibility

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-133 | **RPwD Act 2016 s.40** accessibility standards incl. ICT; **s.42** accessible electronic content, audio description, sign-language interpretation, captions; **s.44** mandatory observance; **s.46** service providers to comply within two years of the rules [VERIFY]; **s.89** fines ₹10,000 then ₹50,000–₹5 lakh. | 19 Apr 2017 | Accessibility is a legal floor; publish an accessibility statement and grievance route. | [VERIFY text] |
| LG-134 | **RPwD Rules 2017 Rule 15** (as amended 2023): websites per **GIGW** (3.0, 2023); ICT products/services per **IS 17802 Parts 1–2** [VERIFY amendment]. | [VERIFY] | Target **WCAG 2.2 AA** (W3C Rec, 5 Oct 2023) + IS 17802 + GIGW 3.0; native mobile accessibility APIs; tagged PDFs. | [VERIFY] |
| LG-135 | ***Rajive Raturi v. UoI*** (SC, 8 Nov 2024): Rule 15's guideline-only approach inconsistent with the Act; mandatory rules to be framed [VERIFY citation/directions]. | [VERIFY] | Governed parameter `a11y.standard_set` updates when rules change. | [VERIFY] |
| LG-136 | ***Pragya Prasun v. UoI*** (SC, 30 Apr 2025): digital access part of Art. 21; directions for **accessible digital KYC** (alternatives to blink/liveness, accessible formats), KYC directions revision, accessibility audits [VERIFY]. | [VERIFY] | KYC/eSign offer non-visual, non-liveness options (Aadhaar App, DSC, human-assisted video), labelled OTP fields, extended time-outs, no image-only CAPTCHA, ops-hub assisted route. | [VERIFY] |
| LG-137 | **Indian Sign Language** (ISLRTC); s.42 captions/interpretation. | in force | Captions + transcripts on all videos; ISL versions of core tutorials; chat/captions in advocate video calls. | [VERIFY] |

## 12. Consumer protection, e-commerce, payments, telecom

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-140 | **Consumer Protection Act 2019** s.2(16) e-commerce, s.2(47) unfair trade practice, s.18 CCPA guidelines, s.94 e-commerce measures. | 20 Jul 2020 | Consumer duties apply to individual buyers of documents/services. | [VERIFY] |
| LG-141 | **Consumer Protection (E-Commerce) Rules 2020** (23 Jul 2020): Rule 4 — entity details, **grievance officer**, **ack within 48 h, redress within one month** (r.4(5)), no price manipulation, **no pre-ticked consent**, no posing as consumers to post reviews; Rule 5 marketplace — provider identity/GSTIN, **ranking parameters**, refund terms [VERIFY sub-rules; any 2026 amendment]. | 23 Jul 2020 | Consumer grievance ack ≤ 48 h / resolve ≤ 1 month, but the stricter IT-Rules 7-day clock governs content grievances; provider cards show identity and GSTIN; ranking-parameters page; no pre-ticked add-ons. | [VERIFY] |
| LG-142 | **CCPA Dark Patterns Guidelines 2023** (30 Nov 2023): false urgency, basket sneaking, confirm shaming, forced action, subscription trap, interface interference, bait and switch, drip pricing, disguised ads, nagging, trick question, SaaS billing, rogue malware. | 30 Nov 2023 | No fake timers (VSL funnel only without false urgency); all-in price (duty, GST, fees) before payment; cancel as easy as subscribe; renewal notices. | V-REG; [VERIFY wording] |
| LG-143 | **CCPA Misleading Ads/Endorsements Guidelines 2022**; **IS 19000:2022** online reviews (BIS, voluntary). | 9 Jun 2022 / Nov 2022 | Testimonials genuine, consented, dated; **none for advocates**; non-regulated provider reviews follow IS 19000 (verified purchase, no suppression, labelled incentives). | [VERIFY] |
| LG-145 | **RBI Payment Aggregator Directions 2025** (15 Sep 2025): authorised PAs handle merchant due diligence, escrow and settlement; marketplace collection for third parties is payment aggregation unless through a PA's settlement structure [VERIFY paras]. | 15 Sep 2025 | Razorpay split settlement/route for provider payouts and duty pass-through; LawDocs never pools third-party funds. | V-REG |
| LG-146 | RBI card-on-file tokenisation — merchants may not store card data after 30 Sep 2022 [VERIFY]. | 1 Oct 2022 | Network tokens via the PA only. | [VERIFY] |
| LG-147 | RBI e-mandate Directions 2026 (RBI/DPSS/2026-27/396): AFA at registration and above the limit; pre-debit notice; no customer charge [VERIFY limits]. | 21 Apr 2026 | Subscriptions via PA e-mandates with renewal reminders. | V-REG |
| LG-148 | **PCI DSS v4.0.1 SAQ A** (Jan 2025 revision): fully outsourced payment pages; 6.4.3 and 11.6.1 removed from SAQ A; new eligibility confirmation that the site is not susceptible to script attacks. | 2025 | Hosted checkout, CSP/SRI, script inventory, signed webhooks, annual SAQ A. A merchant *attests*; it is not "certified". | V-REG ([VERIFY] with PCI SSC) |
| LG-149 | **TRAI TCCCPR 2018** as amended: DLT-registered headers/templates; promotions from 140-series to consenting/non-DND users; 1600-series for regulated-entity service calls [VERIFY non-RE scope]. | in force | AI/automated calling only via DLT-registered telemarketer, consented, DND-checked, time-limited, with an audio AI disclosure (LG-078). | V-REG |
| LG-150 | Government dues (stamp duty, fees, traffic challans) are paid on official channels [VERIFY authorised third-party collection]. | — | Challans: lookup + deep-link to the official payment page; contest via a user-chosen advocate or Virtual Court. | [VERIFY] |

## 13. Companies Act 2013 and governance anchors

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-155 | **s.117** — specified resolutions filed in **MGT-14 within 30 days**. | 1 Apr 2014 | Resolution register auto-creates MGT-14 tasks. | V-REG; [VERIFY wording] |
| LG-156 | **s.118** minutes within **30 days**; **SS-1/SS-2** mandatory (s.118(10); revised SS effective 1 Apr 2024). | 1 Apr 2024 | Minutes: Vidhi draft → maker-checker → chair signature (eSign/DSC where SS-1 permits [VERIFY para]) → locked PDF; 30-day clock. | V-REG |
| LG-157 | **s.173** — first meeting within 30 days; ≥ 4 a year, gap ≤ 120 days; **7 days' notice**; VC participation (s.173(2); Meetings of Board Rules r.3). | in force | Meeting clocks; VC attendance capture per r.3 [VERIFY]. | V-REG |
| LG-158 | **s.175** circular resolutions; **s.179(3)** matters only at a meeting. | in force | Circular workflow blocks s.179(3) items. | [VERIFY list] |
| LG-159 | **s.184** MBP-1 at first meeting each FY and on change; **s.188** RPTs. | in force | Annual MBP-1 eSign task; conflict check in agenda builder. | V-REG |
| LG-160 | **s.149** composition; **s.177** audit committee; **s.178** NRC/SRC; **s.203** KMP (Managerial Personnel Rules r.8/8A); **s.134** authentication and board's report (POSH/maternity statements, Accounts Rules r.8 as amended 30 May 2025). | in force | Governance OS seeds board, committees and KMP by company class; board's-report checklist. | V-REG |
| LG-161 | **RBI NBFC Governance Directions 2025** (RBI/DOR/2025-26/344, 28 Nov 2025) and Compliance Function Directions (31 Jul 2026). | 28 Nov 2025 | NBFC tenants import LDC rule packs; LawDocs does not duplicate them. | V-REG |

## 14. Labour (HRMS)

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-162 | **Four Labour Codes** in force — Code on Wages (S.O. 5322(E)), IR Code (S.O. 5320(E)), Social Security Code (S.O. 5319(E)), OSH Code (S.O. 5321(E)); Central Rules 8 May 2026 (G.S.R. 342(E)–345(E)); State rules vary. | **21 Nov 2025** | Use the shared State-aware `infrabyx-labour-rulepack`; do not fork. | V-REG |
| LG-163 | **Code on Wages s.2(y)** (50% exclusion cap), **s.17** (monthly wages by the 7th; full and final within 2 working days), s.18 (deductions ≤ 50%). | 21 Nov 2025 | Payroll parameters from the pack. | V-REG |
| LG-164 | **OSH Code s.32** annual leave (1 day per 20 days after 180 days; carry-forward 30); **s.6(1)(f)** appointment letter. | 21 Nov 2025 | Leave engine applies the higher of Code and State S&E Act; appointment letters eSigned. | V-REG |
| LG-165 | **SS Code** — gratuity 5 years (1 year FTE), EPF ≥ 20, ESI ≥ 10, maternity 26 weeks, crèche ≥ 50. | 21 Nov 2025 | Obligations by headcount. | V-REG |
| LG-166 | **POSH Act 2013 ss.4, 11(4), 13, 21** — IC for ≥ 10 employees; inquiry 90 days; report 10 days; annual report. | in force | IC module with sealed case data and clocks. | V-REG |
| LG-167 | Employee monitoring — DPDP s.7 employment use; *Puttaswamy* proportionality. | 13 May 2027 | Integrity via maker-checker, segregation of duties, immutable logs and outcome KPIs — no keystroke logging, covert screenshots or webcam surveillance; attendance capture disclosed. | [INTERP] |

## 15. Other rows used by the challenges

| Rule ID | Instrument / exact provision | Effective | Design implication | Confidence |
|---|---|---|---|---|
| LG-170 | **Trade Marks Act 1999 s.21** (opposition within 4 months of advertisement), **s.25** (10-year term, renewable); Trade Marks Rules 2017 response periods [VERIFY]. | in force | Tracker by application number with user-initiated refresh or licensed data; opposition and renewal clocks. | [VERIFY] |
| LG-171 | **RBI Integrated Ombudsman Scheme 2026:** complain to the RE first; RE reply 30 days; representation rules (advocate only if the complainant is one, under the 2021 Scheme) [VERIFY 2026 clause]. | 1 Jul 2026 | Financial-grievance service drafts and tracks; the user files (or LawDocs acts as authorised representative only if the Scheme allows); no "guaranteed resolution". | V-REG |
| LG-172 | **Insurance Ombudsman Rules 2017** and Bima Bharosa [VERIFY representation]. | in force | As LG-171. | V-REG |

---

## 16. Challenges to the owner's brief

Items 1–14 are hard conflicts; 15–28 are material risks needing a design change.

| # | Brief's wish (line) | Conflict | Lawful alternative |
|---|---|---|---|
| 1 | Individuals "**login through Aadhaar**" (l.22) | s.4(4) bars authentication by entities not permitted by Parliamentary law/prescribed purpose; s.57 omitted; Aadhaar use voluntary with alternatives (LG-021–025). | Login = mobile/email OTP + passkey + MFA. Aadhaar only for **OVSE offline verification** (LG-029/030) and **ESP eSign** (LG-006); DigiLocker or manual documents as alternatives. |
| 2 | "**Aadhaar APIs** … automatically fetch the details" (l.21, l.43) | Not an AUA/KUA; OVSE may not store the Aadhaar number (s.8A(4)). | Aadhaar App credential/QR; store purpose-limited signed attributes + last 4 digits; OCR auto-masking (s.29(4)). |
| 3 | "**CKYC** based APIs" (l.21) | CKYCR is for PMLA reporting entities using the KYC Identifier with consent (LG-046). | Drop CKYC; DigiLocker (PAN/DL/RC; Entity Locker for companies); no reuse of a sister RE's CKYC result. |
| 4 | "APIs of … **PAN**" (l.43) | Direct PAN verification limited to enumerated entities (LG-047). | DigiLocker PAN + name match; vendor API only with lawful-upstream warranty. |
| 5 | "APIs of … **CIBIL**" for registration (l.43) | CICRA s.17(4), s.22 (offence); specified-user criteria (LG-057–060). | No bureau pull; users upload their own reports; s.21(3) dispute drafting. |
| 6 | "APIs of … **company registration**" (l.43) | No open MCA API; scraping breaches terms. | Licensed vendor or user-initiated lookup; Entity Locker with consent (LG-039, LG-050). |
| 7 | Ops-hub **password tracker** (CERSAI, MCA, CIBIL, Experian, GST, RBI CIMS, DAKSH, PRAVAAH) — both sides "view/provide/change passwords" (l.73) | Credentials/DSCs are issued to named officers; passwords are SPDI until May 2027 and personal data after; s.66C/s.72A exposure; destroys attribution required by the RE's RBI cyber and outsourcing directions (LR-RBI-017, LR-RBI-044) and by SOC 2/ISO 27001; staff acting inside a regulator portal as a client officer is impersonation. | (a) **Delegation first:** GST practitioner (PCT-05), ERI client authorisation, MCA professional roles with own DSC, separate named users created by the RE on RBI/CERSAI/CIC portals where permitted. (b) If a client insists, a **client-owned zero-knowledge vault** (client-held keys, never plaintext, MFA reveal with reason, time-boxed, tamper-evident log); OTPs never forwarded; DSC tokens stay with officers. (c) Feature OFF by default. |
| 8 | Advocates on "**subscription or percentage basis**"; ratings/testimonials (l.49, l.93) | BCI r.36, r.37, r.20 and fee-sharing bar; Madras HC 2024 (SC pending, no stay) (LG-111–113). | Rule-36-only directory, OFF until counsel opinion; no percentage/referral/lead fee; revenue from users (SaaS, documents, convenience fees) and from non-regulated providers; flat-priced practice SaaS for advocates (counsel to confirm). |
| 9 | Empanel **CAs/CSs** on subscription/percentage (l.26, l.49) | CA Act Sch. I Pt I cl.(2), (3), (6), (7); ICAI 23 Oct 2019 aggregator ban; CS Act analogues (LG-114–117). | Practising CA/CS listing OFF; LawDocs-employed CAs/CSs deliver non-attest services; attest work by independent practitioners engaged directly, no fee to LawDocs. |
| 10 | "Team can **file returns**" with client passwords (l.49, l.76) | Returns verified by the taxpayer; credential sharing defeats verification (LG-125/126). | **API ERI** with client consent; taxpayer EVC/DSC; GST practitioners under PCT-05; TDS uploaded by deductor or ERI. |
| 11 | "**UN-approved languages**" + Indian languages; AI translations attached to petitions (l.53) | UN has six official languages — not a legal category; courts need court-language filings and **certified** translations (LG-093/094). | English + Hindi + demand-ranked Eighth-Schedule languages; six UN languages for reading only; AI output labelled draft; certified translation service; originals + typed copies + s.63 certificate. |
| 12 | **eSign** for all personal, business and property contracts (l.13, l.22) | First Schedule excludes wills, trusts, ordinary POAs, most NIs; sale deeds/long leases need registration; affidavits need a notary (LG-003, LG-104, LG-106). | Document-type gate, wet-ink pack, notary/registration appointment services. |
| 13 | "**eStamp API**: buy stamp papers online" (l.84) | Only CRA/ACCs/licensed vendors issue; coverage differs by State (LG-098–100). | Agent procurement via contracted ACC; duty pass-through via PA; disclosed fee; State registry; stamp-before-sign; UIN checks. |
| 14 | "**Tool sufficient instead of a legal team**"; individuals "handle everything"; startups' "legal officer" (l.68–69, l.88) | Only advocates practise law/appear in courts; a company cannot (LG-110). | Legal-operations platform run by a CLO/retained advocates; party-in-person tools permitted; representation by advocates in their own name. |
| 15 | Vault "like **DigiLocker**", kept forever (l.23, l.69) | Requester ToU bars storage beyond purpose; LawDocs is not a DLSP; Rule 9A only for issuer URIs (LG-036–038). | "Legal Vault"; URI + verification for pulled documents; retained copy only for a recorded user purpose (confirm with NeGD); uploads stored normally with hashes. |
| 16 | Data "**shareable across ecosystem apps**" (l.34, l.66, l.72) | DPDP purpose/consent (s.5–6); DigiLocker cl.17; eSign no sub-letting; CICRA s.17(4)(b). | Intra-group data-sharing contracts, per-purpose consent, sharing ledger; regulated feeds never flow to sister apps by default. |
| 17 | **Aadhaar face auth**; Jio **automated/AI calling** (l.41, l.70) | Face auth is an RE facility; AI voice is SGI; DLT/consent rules (LG-034, LG-078, LG-149). | Face match only inside the Aadhaar App; AI calls via DLT telemarketer with consent, audio disclosure and human hand-off. |
| 18 | "In consonance with **GDPR, CCPA**" (l.44) | Apply only on triggers (LG-084–086). | DPDP-first with GDPR-grade controls; jurisdiction flags switch on extra notices/representatives. |
| 19 | "**PCI-DSS** … certifications" (l.46) | Hosted-checkout merchants self-assess (SAQ A) (LG-148). | SAQ A attestation; copy says "LawDocs never stores card data". |
| 20 | **Testimonials** on pages (l.93) | Rule 36 for advocates; fake reviews (LG-141, LG-143). | Genuine, consented testimonials for LawDocs' own services only. |
| 21 | **Advertisements** revenue (l.62) | Advocate ads barred; no targeted ads to children; ad-tech "sharing". | Contextual non-legal partner ads on public content pages only. |
| 22 | **Challan** pay/contest; FREED-like **loan/insurance grievances** (l.89) | Collecting dues for others is payment collection; ombudsman representation rules; no guaranteed outcomes (LG-150, LG-171/172). | Deep-link payment; user-chosen advocate or Virtual Court; drafting and tracking while the user files. |
| 23 | **Vehicle sale** (l.90) | Transfer via Vahan (LG-107). | Agreement + Vahan checklist. |
| 24 | "**Employees cannot cheat**"; login/logoff tracking (l.59–60) | DPDP proportionality (LG-167). | Maker-checker, segregation, immutable logs, outcome KPIs; transparent attendance. |
| 25 | Marketplace and duty payments through LawDocs; saved cards (l.47, l.49) | PA Directions, CoFT, e-mandate (LG-145–147). | Split settlement; tokens; e-mandates with pre-debit notices. |
| 26 | "**Super admin changes crucial client details**" (l.74) | DPDP accuracy (s.8(3)); evidence integrity; processor role. | Maker-checker with client approval, reason codes, tamper-evident audit, client notification. |
| 27 | **Trademark** and **Provakil-like** case tracking (l.25, l.83) | No open registry APIs; scraping breaches terms (LG-096A, LG-170). | User-entered numbers with user-initiated refresh; licensed partners; statutory clocks flagged until counsel review. |
| 28 | AI reads **WhatsApp screenshots**/handwriting and attaches to petitions (l.53) | Screenshots are secondary evidence; s.63(4) certificate with hash needed (LG-091). | Ingest native chat exports where possible, hash at upload, keep images as originals, label transcriptions, run the Part A/Part B workflow. |

---

## 17. Verification summary

| Topic | Rows | V-WEB | V-SEC | V-REG | [VERIFY]/[INTERP] |
|---|---|---|---|---|---|
| 1 eSign | 14 | 9 | 1 | 0 | 4 |
| 2 Aadhaar | 14 | 4 | 9 | 0 | 1 |
| 3 DigiLocker | 6 | 1 | 4 | 0 | 1 |
| 4 CKYC/PAN/GST/MCA | 5 | 1 | 1 | 0 | 3 |
| 5 CICRA | 5 | 4 | 1 | 0 | 0 |
| 6 Privacy/cyber | 21 | 0 | 11 | 7 | 3 |
| 7 Evidence/courts | 8 | 0 | 2 | 1 | 5 |
| 8 Stamp/registration | 11 | 1 | 4 | 0 | 6 |
| 9 Professional rules | 10 | 0 | 3 | 2 | 5 |
| 10 Tax | 8 | 0 | 0 | 2 | 6 |
| 11 Accessibility | 5 | 0 | 0 | 0 | 5 |
| 12 Consumer/payments/telecom | 10 | 0 | 0 | 5 | 5 |
| 13 Companies/RBI governance | 7 | 0 | 0 | 6 | 1 |
| 14 Labour | 6 | 0 | 0 | 5 | 1 |
| 15 Other | 3 | 0 | 0 | 2 | 1 |
| **Total** | **133** | **20** | **36** | **30** | **47** |

(Counts by primary status; many verified rows carry a narrow trailing `[VERIFY x]`.)

**Engineering rule (mirrors LDC NN-38).** `[VERIFY]` rows seed content, help and tasks but cannot drive a hard block. Locked despite partial verification, because the conservative choice is also the safe one: LG-003 (First Schedule gate), LG-007 (no sub-letting), LG-022/LG-025 (no Aadhaar authentication or number storage), LG-057/LG-058 (no bureau pull), LG-096 (stamp-before-sign), LG-111 (Rule-36 directory).

**Next verification pass (priority).** (1) BCI 2025 circulars and SC status of *Sulekha*; (2) BCI fee-sharing rule number; (3) ERI scheme document; (4) DPDP acceleration status and Third-Schedule thresholds; (5) gazette text and OVSE fees of the 2025 Aadhaar amendment; (6) NeGD position on user-directed saving of DigiLocker documents; (7) RPwD Rule 15 and the *Raturi*/*Prasun* directions; (8) E-Commerce Rules sub-rules and any 2026 amendment; (9) RBI PA Directions marketplace paras; (10) State stamp-vendor rules in launch States; (11) Protean and Capricorn CA licence renewals; (12) ICAI Code edition and ICSI platform guidance.

---

## 18. Sources (accessed 25 October 2026)

**Official / first-party**
1. CCA, S.O. 4720(E) — https://www.cca.gov.in/sites/files/pdf/ACT/SO4720.pdf
2. CCA, gazette notifications — https://cca.gov.in/eSign_gazette_notification.html
3. CCA, empanelled ESPs — https://cca.gov.in/service-providers.html
4. CCA, eSign API v2.1 — https://www.cca.gov.in/sites/files/pdf/ACT/eSign-APIv2.1.pdf
5. CCA, eSign API v3.3 — https://www.cca.gov.in/sites/files/pdf/esign/eSign-APIv3.3.pdf
6. CCA, eSign Empanelment Guidelines — https://www.cca.gov.in/sites/files/pdf/esign/CCA-ESP.pdf
7. CCA, eSign FAQ (web) — https://cca.gov.in/eSign_service_faq.html
8. CCA, eSign FAQ (PDF) — https://www.cca.gov.in/sites/files/pdf/esign/ESIGNFAQ.pdf
9. UIDAI, Aadhaar amendment Ordinance 2019 — https://uidai.gov.in/images/Ordinance__Aadhaar_amendment_07032019.pdf
10. UIDAI, good-governance amendment press release — https://uidai.gov.in/images/Press_Release-Aadhaar_Authentication_Good_Governace.pdf
11. UIDAI, OVSE Playbook — https://www.uidai.gov.in/images/OVSE_Playbook.pdf
12. UIDAI, Aadhaar App offline verification webinar — https://uidai.gov.in/images/Webinar_on_Offline_Verification_of_Aadhaar_App.pdf
13. NeGD, DigiLocker Requester Terms of Use (Jun 2025) — https://cf-media.api-setu.in/resources/DigiLocker-Terms-of-User-Requester-june-2025.pdf
14. DigiLocker, Entity Locker requester API spec (title only) — https://entity.digilocker.gov.in/assets/img/Requester%20-%20Entity%20Locker%20API%20Specification_28_11_24.pdf
15. Protean, Online PAN Verification — https://tinpan.proteantech.in/services/online-pan-verification/pan-verification-overview.html
16. CICRA 2005 (official text, IFSCA) — https://www.ifsca.gov.in/Document/Legal/71-the-credit-information-companies-regulation-act-2005-12092020034712.pdf
17. StockHolding, e-Stamping services — https://blog.stockholding.com/e-stamping-services-by-stockholding.html
18. shcilestamp.com (fetch failed) — https://www.shcilestamp.com/
19. RBI CKYCR PDF (verification wall) — https://rbidocs.rbi.org.in/rdocs/notification/PDFs/CKYCRLEB3990A3432AC4BAB95D7A77854CE011F.PDF

**Secondary**
20. Leegality, First Schedule explainer — https://leegality.com/blog/first-schedule
21. Bar & Bench, S.O. 4720(E) analysis — https://www.barandbench.com/law-firms/view-point/will-documentation-finally-go-paperless-an-analysis-into-the-recent-amendments-to-the-information-technology-act-2000
22. Vinod Kothari, IT Act First Schedule — https://vinodkothari.com/tag/power-of-attorney/
23. Taxguru, Aadhaar (Amendment) Act 2019 — https://taxguru.in/corporate-law/aadhaar-laws-amendment-act-2019.html
24. iPleaders, Aadhaar amendment and fintech — https://blog.ipleaders.in/new-aadhar-amendment-bill-affects-fintech-space/
25. Khaitan, Aadhaar authentication for private entities — https://khaitanco.com/thought-leadership/Aadhaar-authentication-for-private-entities
26. SCC Online, Authentication and Offline Verification Regulations 2021 — https://www.scconline.com/blog/post/2021/11/11/aadhaar-authentication-and-offline-verification-regulations-2021-notified-offline-verification-allowed-along-with-power-to-revoke-e-kyc-consent/
27. IndiaLaw, 2025 offline verification amendments — https://www.indialaw.in/blog/regulatory/aadhar-offline-verification-amendments/
28. Mondaq, Aadhaar Data Vault clarifications — https://webiis10.mondaq.com/india/privacy-protection/1719124/vaulting-to-safety-uidai-issues-clarifications-on-applicability-of-aadhaar-data-vault-requirements
29. SCC Online, Digital Locker Rule 9A — https://www.scconline.com/blog/post/2017/04/27/issuing-certificates-or-documents-in-digital-locker-system-at-par-with-physical-documents
30. Legitquest, Digital Locker Rules 2016 — https://www.legitquest.com/act/information-technology-preservation-and-retention-of-information-by-intermediaries-providing-digital-locker-facilities-rules-2016/9707
31. Vinod Kothari, CKYCR — https://vinodkothari.com/2020/12/ckycr-becomes-fully-operational/
32. APRB, CKYC FAQ — https://aprb.bank.in/ckyc-faq.php
33. Vinod Kothari, specified users — https://vinodkothari.com/2022/01/specified-users/
34. SCC Online, DPDP Rules notified — https://www.scconline.com/blog/post/2025/11/14/meity-notified-digital-personal-data-protection-rules-2025/
35. dpdpa.com, enforcement timeline — https://dpdpa.com/dpdpa_enforcement_timeline.html
36. dpdpa.com, Rules 6, 7, 8, 14 — https://dpdpa.com/dpdparules/rule6.html ; https://dpdpa.com/dpdparules/rule7.html ; https://dpdpa.com/dpdparules/rule8.html ; https://dpdpa.com/dpdparules/rule14.html
37. Grant Thornton, DPDPA one-pager — https://www.grantthornton.in/globalassets/1.-member-firms/india/assets/pdfs/flyers/dpdpa___one_pager_final__25th_november_2025__3.pdf
38. Legal500, DPDP 2026 milestones — https://www.legal500.com/intelligence/india/privacy/dpdp-act-and-rules-2025-the-2026-compliance-milestones-businesses-cant-afford-to-miss
39. Takshashila, DPDP timeline consultation — https://takshashila.org.in/content/blogs/20260126-meity-considers-reducing-dpdpa-compliance-timelines.html
40. Wikipedia, DPDP Rules 2025 (cross-check) — https://en.wikipedia.org/wiki/Digital_Personal_Data_Protection_Rules,_2025
41. Khaitan, IT Amendment Rules 2026 — https://www.khaitanco.com/thought-leadership/MeitY-notifies-the-IT-Amendment-Rules-2026
42. Mondaq, IT Amendment Rules 2026 overview — https://www.mondaq.com/india/it-and-internet/1749836/update-overview-of-the-it-intermediary-amendment-rules-2026
43. PSA Legal, CERT-In Directions — https://psalegal.com/new-cert-in-directions-overview-and-implications/
44. SCC Online, *Pune Bar Assn.* on s.63(4) BSA — https://www.scconline.com/blog/post/2026/07/08/sc-upholds-admissibility-of-electronic-evidence-under-section-63-4-bsa/
45. TaxManagementIndia, BSA s.86 — https://www.taxmanagementindia.com/visitor/detail_act.asp?ID=42101
46. Leegality, digital stamping legality — https://www.leegality.com/blog/digital-stamping-legal-india
47. Melento, digital stamping validity — https://melento.ai/en-in/blog/is-digital-stamping-legally-valid-in-india
48. IndiaPost.org, e-stamping by State — https://indiapost.org/e-stamping-by-state
49. Wikipedia, E-stamping (cross-check) — https://en.wikipedia.org/wiki/E-stamping
50. Mondaq, Registration Bill 2025 — https://www.mondaq.com/india/real-estate/1662976/registration-bill-2025-breaking-colonial-legacy-embracing-digital-governance
51. iPleaders, Rule 36 — https://blog.ipleaders.in/bar-against-legal-advertising-and-solicitation/
52. Verdictum, *Sulekha v. P.N. Vignesh* — https://www.verdictum.in/court-updates/supreme-court/sulekhacom-new-media-private-limited-v-pn-vignesh-ors-special-leave-to-appeal-c-nos-257942024-1557830
53. Taxguru, ICAI aggregator announcement — https://taxguru.in/chartered-accountant/cas-cannot-list-with-application-based-service-provider-aggregators-icai.html

**Internal (V-REG)**
54. LDC Appendix G — `/home/claude/ldpack/ref/LDC/appendices/G_Legal_and_Regulatory_Rules_Register.md`
55. LDC Appendix Q — `/home/claude/ldpack/ref/LDC/appendices/Q_Security_Privacy_and_Certification_Readiness.md`
56. LDC Appendix O §O.5 — `/home/claude/ldpack/ref/LDC/appendices/O_Marketplace_Services_Catalogue_and_Professional_Rules.md`
57. LDC Appendix T — `/home/claude/ldpack/ref/LDC/appendices/T_HRMS_Labour_Codes_Registers_and_Payroll_Parameters.md`
58. Owner brief — `/home/claude/ldpack/src/Owner_Brief_25Oct2026.md`
