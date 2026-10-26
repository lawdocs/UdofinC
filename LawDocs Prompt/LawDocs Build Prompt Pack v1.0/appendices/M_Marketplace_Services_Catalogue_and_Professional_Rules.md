# Appendix M — Marketplace Services Catalogue and Professional Rules

**Status:** Binding for codes, service classes, who-may-deliver rules, profession switch defaults, render allow-lists, onboarding evidence and template outlines; **Reference** for prices (`[OWNER TO SET]`, ex-GST, government fees at actuals). Every professional-conduct position is [INTERP] unless tagged [LAW] and must be confirmed by counsel before the related switch is turned ON (NN-21, NN-38).
**Used by:** P16 (primary), P14 (business-service orders), P15 (Consumer Help listings), P18 (retainer delivery), P21 (service pages and "Hire a professional" blocks), P17 (price lines and streams).

**How to use.** P16 loads §M.2 as seed service products (status `DRAFT` → lint → review → `LIVE`), §M.5 as `mkp.profession_rules` version 1, §M.6 as fixed response schemas with CI tests, §M.7 as the onboarding checklist, and §M.9–§M.10 as template outlines for counsel to complete. Prices map to OH8 SKUs and RS-LD streams in Appendix L. Do not publish any service whose "Who may deliver" column names a supplier whose switch is OFF; it stays `DRAFT` with the reason shown.

---

## M.0 Precedence

Conventions §7 (NN) and §8 (D) prevail; then the `rul` legal rules register (R3 LG rows); then OH8 on price, tax and stream gates; then OH9 on credentials and Rule 36 fields; then this appendix.

## M.1 Marketplace principles

| # | Principle |
|---|---|
| MP-LD-01 | Open to all: browse, search, compare and read landed prices without login or a plan (D-11, R-041) |
| MP-LD-02 | LawDocs first: launch with LawDocs-supplied non-reserved services; panel advocates next; third parties only after per-profession clearance |
| MP-LD-03 | Sell services, not people: fixed-scope products fulfilled by assigned professionals whose enrolment or registration has been checked (M.7); no ranked directory of advocates; never described as "verified" professionals (NN-20; R1 IMP-001) |
| MP-LD-04 | Conduct by design: the render layer and schema constraints, not staff discipline, prevent forbidden listings, ratings, fees and calls to action (NN-21) |
| MP-LD-05 | Landed price: fee + platform fee (if any) + government fee estimate + GST = total, before payment (NN-22, NN-50) |
| MP-LD-06 | Scope clarity: every service states inclusions, exclusions, deliverables, inputs, timeline, revisions and SLA |
| MP-LD-07 | No money custody: professional fees move only through Razorpay Route; LawDocs never pools third-party funds (NN-22) |
| MP-LD-08 | Professional judgement stays with the professional; LawDocs never supplies reserved services in its own name (NN-41) |
| MP-LD-09 | Reviews are about LawDocs's service only; never about an advocate; no photos by default (NN-49) |
| MP-LD-10 | One record: every engagement, deliverable and invoice lives in the client's vault and export (NN-11) |
| MP-LD-11 | Ethical wall for Consumer Help; no outcome promises; official-portal payments only (NN-23) |
| MP-LD-12 | Neutral group: LawDocsComply listings carry their seller of record; Equator only as an optional neutral link (D-11, NN-24) |

## M.2 Category tree and seeded catalogue

**Legend.** Class: DOC = `DOCUMENTATION`, ADV = `ADVISORY_COMPLIANCE`, TEC = `TECHNICAL`, TRN = `TRAINING`, FAC = `FACILITATION`, RA = `RESERVED_ADVOCACY`, RG = `RESERVED_AGENT`, RT = `RESERVED_ATTEST`. Who may deliver: **LT** LawDocs team (M1; employees and contractors; non-reserved only) · **LP** LawDocs Panel advocate/firm (M2; locked until OI-P16-01/02) · **TMA** registered trademark agent or advocate (M2) · **GSTP** enrolled GST practitioner (M2; or LT where LawDocs staff are enrolled and act as employees [VERIFY]) · **ERI** LawDocs as registered e-Return Intermediary with taxpayer verification (P14; [VERIFY registration]) · **PCS/PCA** practising CS/CA (locked OFF) · **TPN** non-regulated third party (translator, courier, typist) · **CHB** Consumer Help brand case manager · **LDC** LawDocsComply · **ACA** FinLegal Academy. SLA = business days from complete inputs. Price models per P16 FR-P16-09.

| Code | Service | Class | Key deliverables | SLA | Who may deliver | Price model | Indicative price |
|---|---|---|---|---|---|---|---|
| **01 Agreements and contract drafting (AGR)** ||||||||
| SVC-AGR-01 | Draft from a vetted template with Vidhi (self-serve) | DOC (software) | DOCX/PDF draft; eSign eligibility result; stamp-duty estimate | Instant | Vidhi | FIXED | Free; ₹99 premium export |
| SVC-AGR-02 | Rent / leave-and-licence agreement — prepared and checked | DOC | Agreement; stamp-duty estimate; registration checklist (if > 11 months or State rule) | 1 | LT | FIXED | ₹799 |
| SVC-AGR-03 | Vehicle sale agreement + Vahan transfer checklist | DOC | Agreement; delivery note; RTO transfer checklist (transfer stays on Vahan — CH-23) | 1 | LT | FIXED | ₹499 |
| SVC-AGR-04 | NDA (mutual or one-way) | DOC | NDA DOCX/PDF | 1 | LT | FIXED | ₹999 |
| SVC-AGR-05 | Employment agreement + offer letter set | DOC | Agreement; offer letter; confidentiality and IP clauses | 2 | LT | FIXED | ₹1,999 |
| SVC-AGR-06 | Service / consultancy agreement | DOC | Agreement with SOW schedule | 2 | LT | FIXED | ₹2,499 |
| SVC-AGR-07 | Vendor / supply agreement | DOC | Agreement; schedules | 3 | LT | FIXED | ₹2,999 |
| SVC-AGR-08 | Loan between individuals + promissory note pack | DOC | Agreement; wet-ink pack for the note (IT Act First Schedule — NN-07) | 1 | LT | FIXED | ₹999 |
| SVC-AGR-09 | Shareholders' / founders' agreement (bespoke) | RA | Draft SHA with advice note; negotiation-ready redline | 7 | LP | FIXED / QUOTE | ₹9,999+ |
| SVC-AGR-10 | Bespoke drafting by a professional | RA | Draft + explanatory note | 3–10 | LP | FIXED by complexity | ₹1,999–₹9,999 |
| SVC-AGR-11 | Agreement translation (labelled machine + human review; certified route for courts — NN-48) | DOC | Translated DOCX; translator note | 2 | LT / TPN | PER_UNIT | ₹399 / page |
| SVC-AGR-12 | Bulk agreement set-up (template + data mapping, 50+ agreements) | TEC | Configured template; sample batch | 5 | LT | FIXED | ₹14,999 |
| **02 Consultations, contract review and negotiation support (CON, REV)** ||||||||
| SVC-CON-01 | 15-minute consultation by practice area (flat slot) | RA (legal) / ADV (tax, compliance) | Call + optional written summary; 48-hour follow-up chat | Slot | LP (legal); LT in-house professional (non-reserved compliance/tax information) | CONSULT_SLOT | ₹299–₹599 |
| SVC-CON-02 | 30-minute consultation | as above | as above | Slot | as above | CONSULT_SLOT | ₹599–₹1,499 |
| SVC-CON-03 | 60-minute consultation | as above | as above | Slot | as above | CONSULT_SLOT | ₹999–₹2,999 |
| SVC-REV-01 | Professional review of a self-drafted agreement | RA (opinion) / DOC (documentation check) | Review memo; tracked changes | 2 | LP (with opinion) or LT (documentation check, no opinion) | PER_UNIT (page bands) | ₹499 (≤ 5 pp) / ₹999 (≤ 15) / ₹1,999 (≤ 40) |
| SVC-REV-02 | Contract negotiation support (one round) | RA | Redline; negotiation note; call | 3 | LP | FIXED | ₹4,999 |
| SVC-REV-03 | Incoming-contract risk summary (AI report + human documentation check) | DOC | Labelled risk summary; clause table | 1 | LT | FIXED | ₹699 |
| SVC-REV-04 | Written legal opinion | RA | Opinion on advocate's letterhead | 5 | LP | QUOTE | On quote |
| **03 Legal notices and replies (NTC)** ||||||||
| SVC-NTC-01 | Legal notice drafting and dispatch | RA | Notice on advocate's letterhead; dispatch proof | 2 | LP | FIXED | ₹1,499–₹2,999 + postage at actuals |
| SVC-NTC-02 | Cheque-bounce demand notice | RA | Notice within the statutory window (NI Act 1881 s.138 proviso (b) [VERIFY]); dispatch proof; limitation tracker entry | 1 | LP | FIXED | ₹1,999 |
| SVC-NTC-03 | Reply to a legal notice | RA | Reply; dispatch proof | 3 | LP | FIXED | ₹2,499 |
| SVC-NTC-04 | Payment reminder letter on the client's letterhead (non-legal) | DOC | Letter | 1 | LT | FIXED | ₹499 |
| SVC-NTC-05 | Bulk advocate notices for a business (e.g., dues) | RA | Notices; dispatch report | Quote | LP | QUOTE | On quote (no recovery-agent activity; lender clients follow RBI recovery conduct rules [VERIFY]) |
| **04 Policies and documentation (POL)** ||||||||
| SVC-POL-01 | HR policy pack (handbook, leave, conduct, WFH) | ADV | Policy set; acknowledgement workflow in HRMS-lite | 10 | LT | FIXED | ₹14,999 |
| SVC-POL-02 | POSH policy + Internal Committee kit | ADV | Policy; IC order; notice; annual report template | 5 | LT | FIXED | ₹4,999 |
| SVC-POL-03 | Privacy notice and DPDP consent notices | ADV | Notice set; consent text; data map starter | 7 | LT | FIXED | ₹9,999 |
| SVC-POL-04 | Website terms, refund and cookie policy set | ADV | Policy set | 5 | LT | FIXED | ₹7,999 |
| SVC-POL-05 | NBFC / regulated-entity policy (e.g., Fair Practices Code, KYC/AML, grievance redressal) | ADV | Draft policy for board approval (board approves — no outsourcing of policy formulation) | 10 | LT (or LDC listing) | PER_UNIT | ₹14,999–₹49,999 |
| SVC-POL-06 | Information-security / IT policy set | ADV | Policy set; control mapping | 10 | LT | FIXED | ₹24,999 |
| SVC-POL-07 | Annual policy review | ADV | Tracked-changes revisions; change log | 15 | LT | PER_UNIT | ₹2,999 per policy |
| **05 Annual reports, board reports and minutes (ARM)** ||||||||
| SVC-ARM-01 | Board's report drafting (Companies Act 2013 s.134 [LAW]) | ADV | Draft board's report with annexure checklist | 10 | LT (CS team) | FIXED | ₹24,999+ |
| SVC-ARM-02 | Annual report compilation (unlisted company) | ADV | Compiled report (financial statements supplied by the auditor/client) | 15 | LT | QUOTE | ₹49,999–₹1,49,999 |
| SVC-ARM-03 | Minutes of a board or committee meeting (SS-1 aligned [VERIFY]) | ADV | Draft minutes; resolution extracts | 3 after meeting | LT | PER_UNIT | ₹2,499 per meeting |
| SVC-ARM-04 | Minutes of a general meeting (SS-2 aligned [VERIFY]) | ADV | Draft minutes; scrutiniser-report placeholders | 5 | LT | PER_UNIT | ₹3,999 |
| SVC-ARM-05 | Minutes from a recording (AI draft + CS review) | ADV | Labelled AI draft reviewed by a CS-qualified employee | 2 | LT | PER_UNIT | ₹1,999 |
| **06 Board, secretarial and governance support (GOV)** ||||||||
| SVC-GOV-01 | Board meeting kit (notice, agenda, notes, draft resolutions) | ADV | Kit in the governance module | 3 | LT | FIXED | ₹4,999 |
| SVC-GOV-02 | AGM kit | ADV | Notice, explanatory statement, proxy form, attendance slip | 5 | LT | FIXED | ₹9,999 |
| SVC-GOV-03 | Statutory registers set-up | ADV | Registers in the governance kernel | 7 | LT | FIXED | ₹7,999 |
| SVC-GOV-04 | Director appointment / resignation pack | ADV | Resolutions, consents, forms prepared; filed with the client's DSC | 2 | LT | FIXED | ₹2,999 + government fee |
| SVC-GOV-05 | Annual ROC compliance (small company) | ADV (+ RT certification where the form requires a practising professional, engaged directly) | Forms prepared; calendar; filing tracker | Annual | LT (+ PCS/PCA where certification is required — locked) | RETAINER_ANNUAL | ₹14,999 / year |
| SVC-GOV-06 | Secretarial compliance health check (non-attest) | ADV | Gap report | 10 | LT | FIXED | ₹19,999 |
| SVC-GOV-07 | Secretarial audit (Companies Act s.204) | RT | — | — | PCS (locked OFF) | QUOTE | OFF |
| **07 Compliance testing and audit readiness (CMP)** ||||||||
| SVC-CMP-01 | Legal compliance health check (SME) | ADV | Scored report; remediation plan | 10 | LT | FIXED | ₹24,999 |
| SVC-CMP-02 | Compliance testing of a regulatory area (sample-based) | ADV | Test plan; results; exceptions log | 15 | LT | QUOTE | ₹50,000+ |
| SVC-CMP-03 | DPDP readiness assessment | ADV | Gap report; ROPA starter; notice review | 15 | LT | FIXED | ₹49,999 |
| SVC-CMP-04 | Contract compliance review (obligations met, renewals, breaches) | ADV | Obligation register; exceptions | 10 | LT | FIXED | ₹29,999 |
| SVC-CMP-05 | Audit-readiness pack (document index for auditors) | ADV | Indexed evidence set; auditor read-only grant | 7 | LT | FIXED | ₹19,999 |
| **08 Risk assessment, stress testing and scenario analysis (RSK)** ||||||||
| SVC-RSK-01 | Legal risk assessment (contracts + litigation) | ADV | Risk register; heat map; board summary | 15 | LT (+ LP for merits) | FIXED | ₹49,999+ |
| SVC-RSK-02 | Stress testing and scenario analysis (NBFCs, fintechs) | ADV | Scenario design; results; management report (RE's own officers decide) | 20 | LT GRC team (or LDC listing) | QUOTE | ₹1,00,000–₹5,00,000 |
| SVC-RSK-03 | Contingent-liability and litigation exposure review | ADV | Exposure table; provisioning inputs for the auditor | 10 | LT (+ LP for merits) | FIXED | ₹49,999 |
| SVC-RSK-04 | Vendor-contract risk review | ADV | Clause scorecard per contract | 10 | LT | PER_UNIT | ₹1,999 per contract |
| **09 Retainer advisory and managed legal department (RTN)** — definitions in Appendix L §L.7 ||||||||
| SVC-RTN-01 | Startup Legal Officer | ADV + RA (split) | Monthly basket; hour bank 6 h; SLA schedule | Monthly | LT + LP | RETAINER_MONTHLY | ₹14,999–₹24,999 |
| SVC-RTN-02 | SME Legal Desk | ADV + RA | Hour bank 10 h | Monthly | LT + LP | RETAINER_MONTHLY | ₹24,999–₹49,999 |
| SVC-RTN-03 | NBFC Legal & Compliance Retainer | ADV + RA | Hour bank 20 h; RM as maker | Monthly | LT + LP | RETAINER_MONTHLY | ₹50,000–₹2,50,000 |
| SVC-RTN-04 | Managed Legal Department (OFF until memo) | RA + ADV | Named legal manager; 40 h | Monthly | LP + LT | RETAINER_MONTHLY | ₹75,000–₹3,00,000 |
| SVC-RTN-05 | Custom retainer | as scoped | as scoped | — | as scoped | QUOTE | On quote |
| **10 Filings, registrations and returns (FIL)** ||||||||
| SVC-FIL-01 | Private limited company incorporation | ADV (+ RT certification where required [VERIFY SPICe+ certification]) | Name, MoA/AoA, SPICe+ forms prepared, PAN/TAN; filed with directors' DSCs | 10 | LT (+ certifying professional) | FIXED | ₹2,999 + government fees + DSC |
| SVC-FIL-02 | LLP incorporation | ADV | LLP agreement; forms | 10 | LT | FIXED | ₹3,999 + fees |
| SVC-FIL-03 | Partnership firm deed + registration | DOC + FAC | Deed; registration application (State) | 7 | LT | FIXED | ₹2,499 + stamp duty + fees |
| SVC-FIL-04 | Proprietorship set-up (GST / Udyam) | FAC | Registrations | 5 | LT | FIXED | ₹2,499 |
| SVC-FIL-05 | DSC procurement facilitation | FAC | DSC via a licensed certifying authority partner [VERIFY] | 1 | LT | FIXED | ₹1,499 |
| SVC-FIL-10 | GST registration | RG / FAC | Application prepared; taxpayer submits with OTP/EVC | 3 | GSTP / LT | FIXED | ₹1,499 |
| SVC-FIL-11 | GST monthly returns | RG | Returns prepared; taxpayer confirms (PCT-05 authorisation — R3 LG-127) | Monthly | GSTP | SUBSCRIPTION_SERVICE | ₹999 / month |
| SVC-FIL-12 | Udyam / MSME registration | FAC | Certificate | 1 | LT | FIXED | ₹499 |
| SVC-FIL-13 | Shops and establishment / trade licence | FAC | Application per State rules | per State | LT | FIXED | ₹1,999 + fees |
| SVC-FIL-20 | ITR — CA-assisted (salaried) | RG | Return prepared via ERI; taxpayer verifies (R3 LG-124–LG-125; CH-10) | 3 | ERI (P14) | FIXED | ₹999 |
| SVC-FIL-21 | ITR — capital gains | RG | as above | 5 | ERI | FIXED | ₹2,499 |
| SVC-FIL-22 | ITR — business / profession | RG | as above | 7 | ERI | FIXED | ₹4,999 |
| SVC-FIL-23 | TDS return preparation | ADV | Statement prepared; deductor uploads (R3 LG-129) | Quarterly | LT | PER_UNIT | ₹1,999 / quarter |
| SVC-FIL-25 | Income-tax / GST notice reply | RA / RG | Reply draft; representation only by eligible representative [VERIFY authorised-representative rules] | 5 | LP / GSTP; LT drafting support | QUOTE | ₹2,999–₹14,999 |
| **11 Startup bundles (STB)** — each line keeps its own supplier, invoice and refund rule (P16 FR-P16-84) ||||||||
| SVC-STB-01 | Founder Kit (founders' agreement, NDAs, IP assignment, advisor agreement) | DOC + RA review | Kit + panel review note | 7 | LT + LP | BUNDLE | ₹9,999 |
| SVC-STB-02 | Incorporation + Compliance Year 1 | ADV | SVC-FIL-01 + SVC-GOV-05 + board kits | 10 + annual | LT | BUNDLE | ₹19,999 + fees |
| SVC-STB-03 | Fundraise Docs (term-sheet review, SHA/SSA support, data room) | RA + TEC | Redlines; data room set-up | Quote | LP + LT | QUOTE | ₹29,999+ |
| SVC-STB-04 | Brand Protection (TM search + filing in 2 classes + 1-year watch) | RG | Filings; watch | 5 | TMA / LP | BUNDLE | ₹7,999 + government fees |
| SVC-STB-05 | ESOP scheme + grant letters | ADV + RA review | Scheme; board/shareholder resolutions; grant letters | 10 | LT + LP | FIXED | ₹14,999 |
| **12 Trademarks and IP (TMK)** ||||||||
| SVC-TMK-01 | Trademark search + filing (per class) | RG | Search report; TM-A filing; acknowledgement in IP tracker | 3 | TMA / LP | PER_UNIT | ₹1,999 + government fee (₹4,500 individual/startup/small enterprise; ₹9,000 others — B-13 [VERIFY]) |
| SVC-TMK-02 | Knock-out search report (advisory) | DOC | Labelled similarity report | 1 | LT | FIXED | ₹499 |
| SVC-TMK-03 | Examination report reply | RG | Reply filed before the deadline | 7 (deadline-driven) | TMA / LP | FIXED | ₹3,999 |
| SVC-TMK-04 | Opposition (notice or counter-statement) | RG / RA | Filing; evidence plan | Quote | TMA / LP | QUOTE | ₹9,999+ |
| SVC-TMK-05 | Trademark renewal | RG | Renewal filing | 3 | TMA / LP | PER_UNIT | ₹1,499 + government fee |
| SVC-TMK-06 | Copyright registration support | DOC / RG | Application prepared | 7 | LT / LP | FIXED | ₹2,999 + fee |
| SVC-TMK-07 | IP assignment / licence agreement | DOC (template) / RA (bespoke) | Agreement | 3 | LT / LP | FIXED | ₹3,999 |
| **13 Litigation support (LIT)** ||||||||
| SVC-LIT-01 | Case file organisation and paperbook compilation | DOC | Indexed, paginated compilation | 3 | LT | PER_UNIT | ₹1,999 per 100 pages |
| SVC-LIT-02 | Typed copies and translations of annexures (labelled; certified route for filing) | DOC | Typed copies with page anchors; translations | 2 | LT / TPN | PER_UNIT | ₹199 per page |
| SVC-LIT-03 | BSA 2023 s.63(4) certificate preparation support | DOC | Part A draft for the party; Part B handed to an eligible expert [VERIFY expert eligibility] | 1 | LT | FIXED | ₹999 |
| SVC-LIT-04 | Bulk matter onboarding into the litigation tracker | TEC | Matters set up from CNR list | 3 | LT | PER_UNIT | ₹4,999 per 50 matters |
| SVC-LIT-05 | Representation / appearance | RA | Per engagement letter | — | LP (M2) or client's own advocate (M3) | QUOTE | On quote |
| SVC-LIT-06 | Drafting pleadings for filing | RA | Pleading on advocate's responsibility | Quote | LP | QUOTE | On quote |
| SVC-LIT-07 | Certified-copy retrieval (RS-LD-43 OFF) | FAC | Certified copy | per court | LT / LP where rules require | PER_UNIT | ₹99 + court fee |
| **14 Property and family documentation (PFD)** ||||||||
| SVC-PFD-01 | Will drafting with wet-ink execution pack (witnesses; optional registration) | RA | Will; execution instructions (no eSign — NN-07) | 3 | LP | FIXED | ₹2,999 |
| SVC-PFD-02 | Gift or relinquishment deed + registration checklist | RA | Deed; stamp-duty estimate; registration checklist | 3 | LP | FIXED | ₹2,999 + duty + fees |
| SVC-PFD-03 | Property title document review | RA | Title review note | 7 | LP | FIXED | ₹4,999+ |
| SVC-PFD-04 | Agreement to sell (property) + registration appointment | DOC + FAC | Agreement (eSign permitted; registration/stamp still apply — R3 LG-003) | 3 | LT (+ LP review option) | FIXED | ₹2,999 |
| SVC-PFD-05 | Affidavit drafting + notary appointment (RS-LD-44 OFF) | DOC + FAC | Affidavit print pack (never eSigned as sworn — R3 LG-106) | 1 | LT | FIXED | ₹499 + notary fee |
| SVC-PFD-06 | Mutual-consent divorce documentation | RA | Petition and settlement drafts | Quote | LP | QUOTE | On quote |
| **15 Execution services (EXE)** ||||||||
| SVC-EXE-01 | eStamp facilitation (authorised channel; stamp before sign — NN-08) | FAC | Stamp certificate (UIN verified, hash-linked) | Same day | LT | PER_UNIT | ₹49 + duty at actuals |
| SVC-EXE-02 | Physical stamp paper / franking with courier | FAC | Stamped paper delivered | per State | LT | PER_UNIT | ₹199 + duty + courier |
| SVC-EXE-03 | Assisted signing ceremony (video-assisted, multi-party) | FAC | Completed ceremony; evidence pack | Scheduled | LT | FIXED | ₹499 |
| SVC-EXE-04 | Registration appointment facilitation (OFF) | FAC | Appointment; document checklist | per State | LT | FIXED | On activation |
| **16 Consumer Help — `[Consumer Help Brand]` (CHP; delivered in P15)** ||||||||
| SVC-CHP-01 | Loan / lending grievance — drafting and escalation pack (RE first, then RBI CMS) | DOC | Complaint to RE; escalation draft; status tracker | 3 | CHB | FIXED (RS-LD-39 OFF until memo) | ₹999 |
| SVC-CHP-02 | Insurance claim grievance — drafting and escalation pack | DOC | Complaint to insurer; Bima Bharosa / Ombudsman drafts [VERIFY routes] | 3 | CHB | FIXED | ₹1,499 |
| SVC-CHP-03 | Credit-report dispute letter (user uploads own report — CH-05) | DOC | Dispute letter to the CIC | 1 | CHB | FIXED | ₹499 |
| SVC-CHP-04 | Recovery-harassment complaint drafting | DOC | Complaint to RE / regulator / police drafts | 2 | CHB | FIXED | ₹999 |
| SVC-CHP-10 | Challan status check with official-payment deep links | Tool | Status; official link | Instant | Software | FIXED | Free |
| SVC-CHP-20 | Challan contest (court-referred) by an advocate | RA | Appearance/representation per Virtual Court or court rules | Per hearing | LP | FIXED | ₹999–₹2,999 + fine paid by the user officially |
| SVC-CHP-21 | Vehicle sale agreement (brand listing of SVC-AGR-03) | DOC | as SVC-AGR-03 | 1 | LT / CHB | FIXED | ₹499 |
| **17 LawDocsComply services (LDC; seller = LDC entity; delivered in LDC)** ||||||||
| SVC-LDC-01 | Compliance retainers (RBI/SEBI/IFSCA) | ADV | Per LDC Appendix O | Monthly | LDC | per LDC | per LDC catalogue |
| SVC-LDC-02 | Regulatory policy packs | ADV | per LDC | per LDC | LDC | per LDC | per LDC |
| SVC-LDC-03 | ICAAP document preparation | ADV | per LDC | per LDC | LDC | per LDC | per LDC |
| SVC-LDC-04 | Regulatory return preparation support | ADV | per LDC | per LDC | LDC | per LDC | per LDC |
| SVC-LDC-05 | Certification readiness (SOC 2, ISO 27001, PCI DSS) | ADV | per LDC (readiness only; no certification) | per LDC | LDC | per LDC | per LDC |
| **18 Trainings — FinLegal Academy (ACA)** ||||||||
| (feed) | Individual courses from trainings.lawdocs.in | TRN | Course access on the Academy | — | ACA | Academy price | Per feed (R5: ₹5,999–₹21,999 observed) |
| SVC-ACA-01 | Corporate seat bundle (compliance, DSA/DMA, KYC/AML, POSH, CISO, DPDP, board/KMP) | TRN | Seats; completion report | — | ACA / LT | PER_UNIT | Seat price − 20–40% |
| SVC-ACA-02 | In-house batch (live, online or on-site) | TRN | Sessions; materials; certificates | Scheduled | ACA / LT | QUOTE | On quote |

Seed count: 115 rows — 114 service codes plus the Academy feed (≥ 80 LIVE at P16 exit; RT rows, OFF streams and LP rows stay `DRAFT` until their switches open).

## M.3 Service classes

| Class | Definition | Who may supply | LawDocs (company) may supply? | Basis |
|---|---|---|---|---|
| RESERVED_ADVOCACY | Legal advice/opinion, representation, appearance, pleadings for filing, notices on an advocate's letterhead, bespoke legal drafting involving advice | Enrolled advocate or firm of advocates in own name | No | Advocates Act 1961 ss.29, 33 [LAW]; *Bar Council of India v. A.K. Balaji* [VERIFY citation] (R3 LG-110); NN-41 |
| RESERVED_ATTEST | Audits and certifications reserved to practising CAs/CSs/CMAs | Eligible practitioner in own name, engaged directly | No | CA Act 1949; CS Act 1980; Companies Act 2013 s.204 [LAW] |
| RESERVED_AGENT | Trademark Registry filings; GST practitioner work; ERI-route tax returns verified by taxpayer | Registered TM agent or advocate; enrolled GST practitioner; registered ERI | Only as ERI (if registered) or through enrolled employees acting within their authorisation [VERIFY] | Trade Marks Act 1999 s.145 [VERIFY]; CGST Rules r.83 (R3 LG-127); ERI scheme (R3 LG-124) |
| DOCUMENTATION | Template-based preparation, documentation support, typing, translation (labelled), compilation | LawDocs team; non-regulated third parties | Yes | [INTERP; COUNSEL boundary — OI-P16-03] |
| ADVISORY_COMPLIANCE | Compliance management, testing, risk assessment, stress testing, policy drafting support, secretarial and board support, minutes, annual-report drafting support | LawDocs team; LDC; third parties | Yes | [INTERP] |
| TECHNICAL | Implementation, migration, integration and data-room set-up | LawDocs team | Yes | — |
| TRAINING | Courses and corporate training | Academy; LawDocs team | Yes | — |
| FACILITATION | eStamp facilitation, appointments, courier, certified-copy retrieval | LawDocs team | Yes (pass-through at actuals) | NN-08; Notaries Act 1952; State rules |

## M.4 Commercial models

| Item | M1 — LawDocs supplies | M2 — Professional supplies; Route-collected | M3 — Direct engagement |
|---|---|---|---|
| Supplier | `[LawDocs Operating Entity]` | Professional or firm | Professional or firm |
| Contracts | Buyer ↔ LawDocs (engagement letter) | Buyer ↔ professional (engagement letter); buyer ↔ LawDocs (marketplace terms, platform service) | Buyer ↔ professional; buyer ↔ LawDocs (platform service) |
| Invoice | OH8 tax invoice by LawDocs | Professional's invoice / bill of supply in own name; LawDocs invoice for platform fee only | Professional's own; LawDocs invoice for platform fee |
| Collection | Razorpay (LawDocs account via OH8) | Razorpay hosted checkout; Route transfer of 100% of professional fee to linked account (on hold → release) | Professional's own means |
| LawDocs revenue | Service fee | Buyer platform fee (flat) — never a share of the professional's fee | Buyer platform fee |
| GST | FC 18% (SAC per tax memo) | Advocate → business entity: RCM (exempt if the business entity's turnover is below the registration threshold); → non-business individual: exempt [TAX MEMO]; other professionals: their own GST; LawDocs fee FC 18% | As M2 |
| ECO duties | — (LawDocs is the seller) | ECO registration; TCS 0.5% on taxable supplies (excl. RCM/exempt) [TAX MEMO]; TDS 0.1% on payouts [VERIFY]; seller details; grievance officer | Facilitation duties (seller details, grievance officer) [VERIFY whether ECO TCS/TDS apply] |
| Default | **ON** | OFF until OI-P16-01, -02, -04, -08 close | OFF |

## M.5 Professional rules by profession (engine values `mkp.profession_rules` v1)

| Profession | Source rules | Allowed | Locked / prohibited | Display allow-list | Default switches |
|---|---|---|---|---|---|
| **Advocates and law firms** | Advocates Act 1961 ss.29, 33, 35 [LAW]; BCI Rules Part VI Ch II Section IV **r.36** (no solicitation or advertising; website particulars per proviso) [LAW]; r.20 (no contingent fee), r.37 (not aid unauthorised practice), r.49 (no full-time employment while practising) [VERIFY numbering] (R3 LG-111–LG-112); Madras HC, *P.N. Vignesh*, 3 Jul 2024 (W.P. 31281 & 31428 of 2019); SC SLP (C) 25794/2024 pending, no stay reported (R3 LG-113); BCI notice 17 Mar 2025 (R1 §3.8) | Deliver reserved services in own name when assigned; accept/decline assignments; set panel fee schedule with LawDocs (no share to LawDocs); buy software plans on ordinary terms | **No** listing fee, commission, fee share, lead fee, paid ranking, badge, referral reward (hard, not configurable); no ratings, reviews, testimonials, photos, per-person fees, success rates, case counts, "top/premium/featured/verified expert" labels, "book this lawyer" CTA; no success fee; no marketing of named advocates (R4-MKT-01–03) | `RULE36_V1` (directory, if ON) / `PRO_SERVICE_V1` (inside an engagement) | listing_mode ASSIGNED_ONLY; directory OFF; buyer fee FLAT; models M2/M3 (both OFF at launch) |
| **Chartered accountants in practice** | CA Act 1949 First Schedule Part I cl.(2), (3), (6), (7) [LAW]; ICAI Ethical Standards Board announcement 23 Oct 2019 — no listing on application-based aggregators (R3 LG-115); ICAI Code of Ethics current edition [VERIFY] (R3 LG-116) | Buy software; LawDocs-employed CAs deliver non-attest services as employees (M1) | Practising-CA listing OFF; commission/fee share OFF; attest work only by direct engagement | `PRO_SERVICE_V1` only if switched on | listing_mode OFF; all commercial OFF; locked pending counsel |
| **Company secretaries in practice** | CS Act 1980 First Schedule (analogous clauses) [VERIFY]; ICSI guidance on advertisement/online platforms [VERIFY] (R3 LG-117) | As CAs | PCS listing OFF; certification only by an independent PCS engaged directly | as CAs | OFF; locked |
| **Cost accountants** | Cost and Works Accountants Act 1959 Schedules [VERIFY]; ICMAI 2025 referral-network bar (R6 P-04) | Buy software | Listing and commission OFF | — | OFF; locked |
| **Tax practitioners — GST practitioners, tax return preparers (non-CA)** | CGST Act s.48; CGST Rules r.83; Form PCT-05 (R3 LG-127) | Deliver RG services under PCT-05; ERI route for returns | Never file using client credentials (CH-10); `commission_pct_allowed` OFF until legal review (RS-LD-26) | `PRO_SERVICE_V1`; aggregate service rating only if allowed | ASSIGNED_ONLY; buyer fee FLAT; M2 |
| **Trademark agents (non-advocate)** | Trade Marks Act 1999 s.145; agent conduct rules [VERIFY] | Deliver RG services | Listing fees and commission OFF (treated as regulated) | `PRO_SERVICE_V1` | ASSIGNED_ONLY; M2; locked pending counsel |
| **Notaries** | Notaries Act 1952; Oaths Act 1969; no operational e-notarisation [VERIFY] (R3 LG-106) | Facilitation of appointments only | No listing, no commission; notary fee pass-through | — | OFF (RS-LD-44 OFF) |
| **Insolvency professionals, registered valuers** | IBBI codes of conduct [VERIFY] | — | Not listed in v1 | — | OFF |
| **Mediators and arbitrators** | Equator governs (Ecosystem Spec §8.6) | Neutral link only if enabled | Never listed in LawDocs | — | OFF |
| **Non-regulated providers** (translators, typists, couriers, process servers, document retrieval) | Consumer Protection Act 2019; E-Commerce Rules 2020 r.5 seller duties [VERIFY]; CCPA Dark Patterns Guidelines 2023 | Full listing with seller details; ratings with IS 19000 moderation | No paid placement (`mkp.sponsored.enabled` OFF) | `PROVIDER_FULL_V1` | FULL; take rate 10–20% (RS-LD-25, ON with third parties) |
| **LawDocs employees** (`OPS_PROFESSIONAL`) | Company law; BCI r.49 for advocates employed full-time [VERIFY] | DOC, ADV, TEC, TRN, FAC services as employees | No reserved services in LawDocs's name; no professional seals or "advocate" titles implying the company practises law (NN-41) | "Prepared by LawDocs (reviewer: name, role)" | n/a |

Every switch change: maker `PLT_SUPER_ADMIN` → checker `PLT_LEGAL_REVIEWER` (≠ maker) → mandatory `counsel_opinion_ref` for regulated professions → effective-dated → audit-ledgered → kill switch (NN-18, NN-39).

## M.6 Render allow-lists (fixed response schemas; CI-enforced)

| Schema | Fields (only these) | Where used |
|---|---|---|
| `RULE36_V1` | name, address, telephone, email, enrolment_number, enrolment_date, state_bar_council, place_of_practice, qualifications (professional, academic), practice_areas, disclaimer | Optional advocates directory page (OFF); BCI r.36 proviso and Schedule [VERIFY Schedule wording]; consent and self-certification required (OH9.4) |
| `PRO_SERVICE_V1` | display_name, profession, role_level (e.g., "Advocate, 8–12 years"), languages, State of practice, verification_status ("credentials checked on DD-MM-YYYY"), disclaimer | Assignment confirmation inside an engagement only; never public, never sortable |
| `PROVIDER_FULL_V1` | legal_name, seller details (GSTIN, address, customer-care contact), services, prices, languages, response time, ratings_aggregate (count, period, method), certifications (claims-gated) | Non-regulated providers |
| `LAWDOCS_SERVICE_V1` | service fields per P16 FR-P16-03; aggregate CSAT of LawDocs services with method | All service pages |

Forbidden for any advocate response under every schema: rating, review, testimonial, photo, fee per person, success rate, case count, client names, "top", "premium", "featured", "verified expert", "best", "book this professional". CI test `NN-21_profession_render_allowlist` serialises every endpoint that can return a professional and fails on any extra key.

## M.7 Onboarding evidence (P16 FR-P16-24/25; verification via P01 and OH9)

| Applicant | Mandatory evidence | Verified against | Recheck |
|---|---|---|---|
| Advocate | Enrolment number, State Bar Council, enrolment date, certificate of practice where applicable [VERIFY], ID (masked; NN-04), PAN, no-disciplinary-order declaration, practice areas, forums, languages, conflict declaration, panel agreement (eSigned), PI cover (firm), bank via Route KYC (penny test; name match ≥ 85%) | State Bar Council roll / OH9 officer verification; no scraping (NN-05) | Annual + certificate-of-practice cycle |
| Law firm | Firm deed / LLP registration, partners' enrolments, PAN, GSTIN (if any), offices, PI cover, DPA, information-security questionnaire | Registers; OH9 | Annual |
| CA / CS / CMA (if ever enabled) | Membership, certificate of practice, firm registration, peer review where relevant | ICAI / ICSI / ICMAI registers [VERIFY access] | Annual |
| Trademark agent | Agent registration [VERIFY register]; ID; PAN | IP India register (manual) | Annual |
| GST practitioner | Enrolment; ID; PAN | GST portal (manual) | Annual |
| LawDocs employee | OH10 employment record; professional credentials if any; role mapping | OH10 / OH9 | On role change |
| Non-regulated provider | Entity KYC (PAN, GSTIN, CIN/LLPIN/deed), bank, seller-details declaration, sample work, DPA, code of conduct | P01 KYB | Annual |

States: `INVITED|APPLIED → PROFILE_SUBMITTED → KYC_VERIFIED → CREDENTIALS_VERIFIED → DUE_DILIGENCE → AGREEMENT_SIGNED → ROUTE_LINKED (M2) → ACTIVE → SUSPENDED/REMOVED`; `RETURNED` with reasons and a 30-day resubmission window.

## M.8 Conduct and quality controls

| Control | Rule |
|---|---|
| Code of conduct (eSigned at onboarding) | Confidentiality; conflicts declared before acceptance; no off-platform solicitation of buyers met through LawDocs (for M2, only where lawful [COUNSEL]); no misrepresentation of credentials; respond within SLA; no outcome guarantees; data handling per DPA; no use of buyer data outside the engagement; AI use disclosed and reviewed (NN-14) |
| Prohibited claim words (lint) | "best", "top", "No. 1", "guaranteed", "100% success", "assured result", "government-approved", "verified expert", "instant approval", "win your case", "waiver guaranteed" (Consumer Help) — claims gate OH14 for any other claim (NN-20) |
| Conflict checks | Automated party-name and PAN/CIN hash check + group institutional check + professional declaration before acceptance (P16 FR-P16-32) |
| Independence | Buyer-declared auditors cannot deliver overlapping compliance testing/secretarial services (P16 FR-P16-33) |
| QA | M1: release review by `OPS_QA_REVIEWER`; monthly 10% sample; M2: 5% process sample (timeliness, scope fit, documentation) — legal merits stay with the advocate (NN-41) |
| Operational reliability (internal only) | On-time milestone %, acceptance at first release %, response time, dispute rate — used for assignment fit and panel review; never displayed publicly for advocates |
| Suspension triggers | Credential lapse (OH9 `ProfessionalSuspended`), upheld conduct complaint, repeated SLA breach (3 in 90 days), confidentiality breach, conflict non-disclosure |
| Anti-leakage | Masked contacts; warning nudges when phone numbers/e-mails are typed in threads; no keystroke or screen surveillance (NN-33) |
| Grievance | Marketplace grievance officer: acknowledge ≤ 48 h, resolve ≤ 1 month (E-Commerce Rules 2020 r.4(5) [VERIFY]) |

## M.9 Template outlines (full texts by counsel; versioned in `tpl`, reviewer of record — NN-30)

**M.9.1 Engagement letter / SOW (M1; and template for M2 between buyer and professional).** 1 Parties and authority · 2 Scope by reference to service code, version and scope snapshot · 3 Exclusions (mandatory: no representation unless named; no attest services unless by an eligible practitioner named; no filing with client credentials; decisions reserved to the client) · 4 Deliverables, revisions and acceptance (deemed acceptance only if stated) · 5 Inputs and dependencies; clock starts when inputs complete · 6 Timeline and SLA · 7 Fees by supplier, GST/RCM/exempt statement, pass-through lines, payment and TDS · 8 Change requests · 9 Confidentiality · 10 Data protection roles (M.12) and India residency · 11 IP (client owns final deliverables on payment; supplier keeps pre-existing know-how) · 12 Professional-conduct statements (who is responsible for professional judgement) · 13 Conflicts and independence representations · 14 Limitation of liability (cap = fees paid in the prior 12 months [OWNER TO SET]) · 15 Termination · 16 Governing law and disputes (courts at `[OWNER TO SET]`; consumer remedies preserved) · 17 Electronic execution (IT Act 2000; eSign/DSC/click-wrap thresholds).

**M.9.2 SLA schedule (retainers).** Metrics, targets, measurement, clock rules (IST business calendar of the client's State), exclusions, service-credit formula and cap, escalation matrix, reporting, amendment by eSigned new version (Appendix L §L.7.1).

**M.9.3 Panel agreement (LawDocs ↔ advocates' firm).** Independence of professional judgement; supply in own name; panel fee schedule; **no fee sharing, no referral reward, no listing or lead fee**; assignment by objective fit and rotation; SLAs and QA (process only); confidentiality and DPA; Route linked account and on-hold release rules; conflicts; insurance; suspension and exit; compliance with BCI Rules.

**M.9.4 Marketplace buyer terms.** LawDocs's role per model; seller information; ranking parameters; platform fee explanation; reviews policy (LawDocs service only); refunds and cancellations (M.10); grievance officer; prohibited uses; data protection.

**M.9.5 Professional terms (third parties, when enabled).** Verification; profession rules; service accuracy; SLAs; fees (platform fee charged to buyers; take rate only for non-regulated providers); suspension; DPA; information security; audit rights.

**M.9.6 Consultation terms.** Flat slot; mode; masked numbers; recording only with consent; 48-hour follow-up; no-show refund; not an emergency service.

## M.10 Cancellation and refund policy (service side; consistent with Appendix L §L.13.2)

| Situation | Outcome |
|---|---|
| Buyer cancels before scoping or work starts | 100% refund, platform fee included |
| After scoping call, before work | Refund less the scoping fee shown on the price card (if any) |
| After inputs received | Delivered milestones payable; undelivered milestones refunded |
| Professional no-show (consult) | Automatic full refund within 2 hours; rebook offered |
| Buyer cancels a consult ≥ 4 hours before | Full refund; < 4 hours: 50%; one free reschedule |
| No professional available within 1 business day | Full refund or new date at the buyer's choice |
| Dispute upheld | Re-work, partial or full refund via credit note and Route reversal |
| Retainers | Per notice period; prepaid months beyond notice refunded; hour bank non-refundable unless LawDocs terminates |
| Pass-through amounts | Refunded only if not yet paid to the authority or vendor |
| Refund method | Original payment method within 7 working days of approval `[OWNER TO SET]`; credit note issued; no stored balance created |

## M.11 FinLegal Academy course feed (P16 FR-P16-72)

| Field | Type | Rule |
|---|---|---|
| `course_id` | string | Stable Academy id |
| `title` | string | Plain text; no claims beyond claims gate |
| `category` | enum | Compliance foundations · NBFC compliance officer · DSA/DMA and collection-agent conduct · KYC/AML · CISO and IT security · Data protection and DPO · POSH · Board and KMP · Company secretarial practice · Drafting and paralegal · Litigation practice (AoR, arbitration) · Exam preparation · Legal-tech and AI governance |
| `audience[]` | enum list | Individuals, students, lawyers, compliance officers, DSAs, CISOs, DPOs, HR, directors/KMP, entrepreneurs |
| `level` | enum | Foundation, practitioner, advanced |
| `format` | enum | Live, recorded, blended |
| `duration_hours` | decimal | — |
| `language[]` | enum | Per D-07 |
| `price_minor`, `mrp_minor`, `currency` | integer, integer, ISO | MRP shown only if it was actually charged in the last 30 days (NN-50) |
| `next_batches[]` | {start, end, mode} | Hidden if feed stale > 7 days |
| `certificate_type` | enum | Completion, assessment-based; verification URL pattern |
| `trainer_display` | string | Only with trainer consent |
| `url` | URL | Allow-listed host trainings.lawdocs.in |
| `updated_at`, `feed_hash` | timestamp, sha256 | Signature over the feed |

Reviews from the Academy are not imported (R5 found identical reviews on every course). Paid course content is never copied (D-16).

## M.12 Data-protection roles (DPDP Act 2023)

| Model | Account and contact data | Engagement content and deliverables | Professional records |
|---|---|---|---|
| M1 | LawDocs — fiduciary | LawDocs — fiduciary for its engagement records; processor where it processes a business buyer's documents on instructions (DPA) | — |
| M2 | LawDocs — fiduciary (platform data) | Professional — fiduciary for professional records; LawDocs — processor for hosting the engagement room | Professional — fiduciary |
| M3 | As M2 | As M2 | As M2 |
| Consumer Help | Brand entity — fiduciary; ethical wall (NN-23) | Brand entity | — |
| LDC listings | LDC — fiduciary after consented routing (NN-24) | LDC | — |

Retention seed: engagement records 8 years after closure [REC; VERIFY]; quote-intake quarantine 30 days; engagement messages 3 years after closure unless legal hold; export available throughout (NN-11).

## M.13 Consumer Help listing rules (P15 owns delivery)

1. Listed under `[Consumer Help Brand]` with its own entity profile, grievance officer and terms (D-06).
2. Mandatory card statements: "We do not promise any outcome, waiver or settlement." · "Pay fines, challans and dues only on the official portal." · "You can file this yourself for free on the official portal; we help you draft and track." · Where RB-IOS 2026 applies: "An advocate cannot act as your authorised representative before the RBI Ombudsman" [VERIFY clause — conventions fact 13].
3. Flat fees only; success fee RS-LD-40 OFF and never where an advocate acts (CH-31); no lead fees from lenders or insurers (LD-X06).
4. Conflict check against the group's lender/insurer clients before acceptance (NN-23).
5. Sensitive intents excluded from retargeting (R4-MKT-10).

## M.14 Parity backlog from competitor research (R1)

| R1 ref | Idea | Placement | Gate |
|---|---|---|---|
| IMP-005 | Consult modes: async chat with response SLA, scheduled call/video, call-back; masked numbers | SVC-CON-01…03 | M2 ON |
| IMP-008 | 48-hour free follow-up after each consult | SVC-CON-* | — |
| IMP-009 | Auto-refund on no-show; partial refunds; grievance SLA displayed | M.10 | — |
| IMP-012 | QA layer and SLA breach auto-escalation | M.8 | — |
| IMP-013 | Off-platform leakage nudges | M.8 | Warning only |
| IMP-030 | Expert review priced per page band with written report | SVC-REV-01 | — |
| IMP-075 | TM price card with government fee by applicant type | SVC-TMK-01 | Fee [VERIFY] |
| IMP-079 | Landed price card | All services | — |
| IMP-082 | Membership quotas for consults and reviews | Appendix L F-131 | — |

## M.15 Standard inputs, exclusions and price-card pattern

### M.15.1 Inputs checklist patterns (attach per service; each item has an "i" key)

| Pattern | Items | Used by |
|---|---|---|
| IN-PARTY | Party names, addresses, PAN/CIN (optional), authorised signatory, contact for the other side (counterparty is never treated as a lead — R4-MKT-12) | AGR, REV, NTC, PFD |
| IN-PROPERTY | Address, State, nature of right (sale, lease, licence, gift), consideration, term, prior title documents (uploads), encumbrance information if available | AGR-02, PFD-* |
| IN-VEHICLE | Registration number, chassis/engine numbers, RC copy, insurance, loan/hypothecation status, buyer/seller IDs (masked — NN-04) | AGR-03, CHP-21 |
| IN-NOTICE | Facts timeline, amount, documents (invoices, cheque, dishonour memo, correspondence), relief sought, previous notices | NTC-* |
| IN-COMPANY | CIN, registered office, directors/KMP, board composition, financial year, auditor details (for independence checks) | ARM, GOV, CMP, FIL |
| IN-POLICY | Entity type and regulator, existing policies (uploads), board approval cycle, applicable directions list from LDC if connected | POL-* |
| IN-RISK | Portfolio and liquidity data extracts (aggregated), risk appetite statement, prior stress results | RSK-* |
| IN-TM | Mark (word/logo files), applicant type (individual, startup, small enterprise, other), classes, goods/services description, first-use date, prior searches | TMK-* |
| IN-MATTER | CNR/case numbers, forum, parties, next date, orders received, documents | LIT-* |
| IN-GRIEVANCE | Product, RE/insurer name, complaint already made to the RE (date, reference), reply received, amount, documents | CHP-* |

### M.15.2 Standard exclusions (lint requires at least one; these are the defaults)

- "Representation before any court, tribunal or authority unless this service says it includes it."
- "Statutory certification or audit, unless an eligible practitioner named in your engagement letter provides it."
- "Filing on government or regulator portals using your login or OTP; you or your authorised professional submit."
- "Government fees, stamp duty, court fees and registration charges, which you pay at actuals."
- "Decisions reserved to your board, officers or you; we prepare drafts and analysis."
- "Translation certified for court filing, unless you order the certified-translation service."
- Consumer Help only: "Any promise of an outcome, waiver, settlement or refund."

### M.15.3 Price-card pattern (P16 FR-P16-10; lint-checked)

```
<Service title> — <package>
Service fee (LawDocs) ............................ ₹ x          | or: Professional fee (paid to the delivering advocate's firm) ₹ x
LawDocs platform fee ............................. ₹ y          (only where a professional supplies the work)
Government / statutory fees (estimate) ........... ₹ z          basis: <rule, date>; paid at actuals
GST .............................................. ₹ g          18% on LawDocs fees; advocate's fee: exempt for non-business buyers and for business entities below the registration threshold (Notification 12/2017-CT(R), entry 45) / reverse charge for other business entities, registered or not (Notification 13/2017-CT(R), Sl. 2) [TAX MEMO]
Total payable now ................................ ₹ T          (amounts at actuals collected when the filing or instrument is ready)
Not included: <top exclusions>   ·   Delivery: <n> business days after inputs   ·   Refund: <one line>   ·   SLA: <one line>
```

## M.16 Regulated-entity buyer guard-rails (NBFCs, HFCs, co-operative credit societies, IFSCA units)

| Service | Limitation [INTERP; VERIFY current RBI outsourcing and internal-audit directions] | Product behaviour |
|---|---|---|
| NBFC Legal & Compliance Retainer; compliance testing | The compliance function and policy formulation are core management functions the RE cannot outsource | Offered as support to the RE's own officers; unticked acknowledgement at order; RM is maker, RE officer is checker (R-064) |
| Policy drafting (SVC-POL-05) | Board approves policies | Deliverables are drafts; approval tracked in governance module or LDC |
| Stress testing (SVC-RSK-02) | Decisions and submissions stay with the RE | Analysis and drafts only |
| Recovery notices (SVC-NTC-05) | RE's recovery conduct rules apply; LawDocs is not a recovery agent | Advocate notices only; no field or call recovery; no harassment templates |
| Any service involving borrower data | Outsourcing due diligence, contract clauses and register entry by the RE | Auto-generated outsourcing schedule; DPA; residency statement |
| Group LDC services | LDC is SoR for compliance and governance (D-10, NN-47) | Route to LDC listing when the tenant uses LDC |

## M.17 "Hire a professional" mapping for document pages (R-087)

| Document page family (R5 inventory) | Free lane | Paid lane (first offer) | Second offer |
|---|---|---|---|
| Rent / leave-and-licence | SVC-AGR-01 | SVC-AGR-02 | SVC-EXE-01 eStamp |
| Sale agreements (movable / vehicle) | SVC-AGR-01 | SVC-AGR-03 | SVC-REV-01 |
| Property (agreement to sell, gift, relinquishment) | SVC-AGR-01 (agreement to sell only) | SVC-PFD-04 / SVC-PFD-02 | SVC-PFD-03 title review |
| Wills and succession | Information + wet-ink checklist (no AI-custom will without review — NN-14) | SVC-PFD-01 | — |
| Employment and HR | SVC-AGR-01 | SVC-AGR-05 | SVC-POL-01 |
| Business contracts (NDA, service, vendor) | SVC-AGR-01 | SVC-AGR-04 / -06 / -07 | SVC-REV-02 |
| Startup documents | SVC-AGR-01 | SVC-STB-01 | SVC-RTN-01 |
| Notices | SVC-AGR-01 (letter templates) | SVC-NTC-01 / -02 / -03 | SVC-CON-02 |
| Pleadings and court drafts | Pleadings studio templates (P10) labelled | SVC-LIT-06 | SVC-LIT-02 typed copies |
| Compliance and governance documents | Templates | SVC-ARM-03 / SVC-GOV-01 | SVC-RTN-02 / -03 |
| Trademark pages | SVC-TMK-02 knock-out search | SVC-TMK-01 | SVC-STB-04 |
| Consumer grievance pages (brand) | Templates + official-portal links | SVC-CHP-01 / -02 | SVC-CON-01 |

Every block shows the landed price and "no plan needed"; the free lane is template automation, while AI-customised drafts for individuals carry the review label and the one-click paid review (NN-14; CH-30).

## M.18 Category price guard-rail bands (`mkp.price_guardrail.<category>`; anomaly detection only)

| Category | Min | Max (above → QUOTE_ONLY) |
|---|---|---|
| 01 Agreements | ₹299 | ₹49,999 |
| 02 Consultations and review | ₹199 | ₹49,999 |
| 03 Notices | ₹499 | ₹24,999 |
| 04 Policies | ₹1,999 | ₹2,00,000 |
| 05 Annual reports and minutes | ₹999 | ₹2,50,000 |
| 06 Board and secretarial | ₹999 | ₹1,00,000 |
| 07 Compliance testing | ₹9,999 | ₹10,00,000 |
| 08 Risk and stress testing | ₹9,999 | ₹10,00,000 |
| 09 Retainers (monthly) | ₹9,999 | ₹5,00,000 |
| 10 Filings and returns | ₹299 | ₹99,999 |
| 11 Startup bundles | ₹4,999 | ₹2,00,000 |
| 12 Trademarks and IP | ₹299 | ₹99,999 |
| 13 Litigation support | ₹199 | Quote |
| 14 Property and family | ₹499 | ₹99,999 |
| 15 Execution services | ₹49 | ₹4,999 |
| 16 Consumer Help | ₹0 | ₹4,999 (flat fees only) |

Bands block obvious errors; they never fix a third party's price and never apply to the panel fee schedule except as an outer limit.

## M.19 Service-page copy pattern (P21 owns the CMS; claims gate applies)

1. **H1** = outcome in plain words ("Get your rent agreement checked and ready to sign").
2. **Who it is for / not for** (two short lists).
3. **Landed price card** (M.15.3) and **timeline**.
4. **What you get** (deliverables), **what you give us** (inputs), **what is not included** (exclusions).
5. **Who does the work** — "LawDocs documentation team" or "An advocate enrolled with a State Bar Council, from the LawDocs Panel, assigned by practice area and language (enrolment checked on [date])" — never "verified advocate", a named advocate, rating or photo (NN-20, NN-21; W.9 LA-19).
6. **How it works** in 4 steps (order → upload → we deliver → you approve), each with an "i" key.
7. **Free alternative** ("Draft it yourself free with Vidhi — template lane").
8. **FAQs** (≥ 3, visible HTML), grievance officer link, seller-of-record panel, last-reviewed date and reviewer role (NN-30).

## M.20 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-M-01 | Counsel completion of M.9 templates and the panel agreement | [COUNSEL] | M1-only services live |
| OI-M-02 | Confirm DOCUMENTATION vs RESERVED_ADVOCACY split for rows SVC-AGR-02…08, SVC-REV-03, SVC-TMK-07, SVC-PFD-04 | [COUNSEL] (OI-P16-03) | Move to LP if counsel says reserved |
| OI-M-03 | RESERVED_AGENT supply by LawDocs employees (GST practitioners, ERI registration) | [COUNSEL] + P14 | GSTP/ERI rows OFF |
| OI-M-04 | RBI Ombudsman representation clause and IRDAI routes for Consumer Help copy | [VERIFY] P15 | Generic "check the scheme" copy |
| OI-M-05 | Professional registers accessible for verification (State Bar Councils, ICAI/ICSI, IP India agents) | OH9 lead [VERIFY] | Manual officer verification with evidence hash |
| OI-M-06 | Final prices for all rows | Owner `[OWNER TO SET]` | Seeds |
