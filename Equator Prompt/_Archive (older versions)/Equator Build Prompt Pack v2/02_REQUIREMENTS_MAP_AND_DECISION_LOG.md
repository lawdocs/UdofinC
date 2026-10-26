# 02 — Requirements Map, Decision Log and Assumptions (v2.0, 21 October 2026)

> Binding companion to `01_MASTER_PROMPT.md`. It maps every requirement given by Equator management (briefs of 19, 20 and 21 October 2026) to the file that specifies it, records decisions and the reasons for them, lists assumptions, and names questions that need qualified counsel. The coding agent reads this file at the start of every phase. Where this file and a phase prompt conflict, this file and the master prevail (master §15).

Research base for v2 (all under the build team's research archive): S1 Family & succession across communities · S2 Commercial, IBC/NCLT & company law · S3 Financial, insurance & competitors (ClaimBuddy, Insurance Samadhan, Jupitice, Presolv360, Sama, CORD) · S4 Workplace & pre-litigation mediation · S5 International institutions (SIAC, SIMC, ICC, LCIA, HKIAC, AAA-ICDR, MCIA, IIAC) · S6 Training, IMI QAP & neutral grading · S7 Reliance Jio AI, onboarding APIs & document AI · S8 Court formats, case status, publication, privacy & certifications · S9 Revenue, UX, SEO/GEO & corpus re-read. v1 research (R1–R5, C1–C5) and the verification of 514 flags (Appendix J) remain valid unless superseded below.

---

## 1. File map (v2)

| File | Purpose |
|---|---|
| `00_README.md` | How to run the pack; decisions needed; completion checklist |
| `01_MASTER_PROMPT.md` | Constitution: product, NN rules (NN-01–NN-32), architecture, phases |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | This file |
| `phases/P00–P14` | Build phases; each ends with a **v2 addendum** listing new requirements |
| `verticals/V1_FIN … V6_INT` | One specification per dispute type: subtypes, law by subtype, suitability rules, Dispute Explorer question trees, intake forms per mechanism with dropdown values, documents, modus operandi, practical difficulties, integrations, calculators, outputs, KPIs, tests |
| `appendices/A–J` | v1 binding specifications (workflows, fees, screens, integrations, AI, data model, legal register, GTM & website corrections, tests, verification log) |
| `appendices/K` | Dispute Explorer v2 and the dispute-type plug-in framework (adding new dispute types later, Jupitice-style catalogue) |
| `appendices/L` | Document management system, court-format templates (A4), type copies of handwritten/screenshot material, translation |
| `appendices/M` | AI Pleadings Studio — statement of claim / defence / affidavit drafting from party documents; model-provider abstraction |
| `appendices/N` | Neutral governance: grades A/B/C, Qualifying Assessment Programme, code of conduct, complaints, ratings, allocation, directory, training pathways, Private ADR Chambers |
| `appendices/O` | Revenue architecture, plans and benefits, one-time products, billing and settings pages |
| `appendices/P` | Website copy deck, taglines, microcopy, SEO/GEO/AI-search content system |
| `appendices/Q` | Privacy (GDPR, CCPA/CPRA, DPDP, IT Act), security and certification readiness (PCI DSS, SOC 2, ISO family) |
| `appendices/R` | Case-status portal, publication of awards and settlements, execution and registration support |
| `appendices/S` | Identity: separate login portals, onboarding integrations (Aadhaar, PAN, DigiLocker, MCA, credit reports), representatives, dashboards, RBAC |
| `appendices/T` | Benchmarks: competitors, international institutions, training providers, Reliance Jio AI evaluation |

---

## 2. Requirements map

Status key: **S** = specified; **S+L** = specified, needs legal sign-off before launch; **S+V** = specified, depends on vendor access or contract; **C** = configurable by design.

| ID | Requirement (management brief) | Where specified | Status |
|---|---|---|---|
| R-01 | Six dispute types: financial & loan, commercial & business, family & property, insurance, workplace, international commercial | Master §1.2; V1–V6 | S |
| R-02 | Each type has its own rules, law, modus operandi, intake forms, practical difficulties, integrations and APIs | V1–V6 §2–§12 | S+L |
| R-03 | Subtypes per type (e.g., family: inheritance, property division across all religions and communities; international: ICA and international mediation; commercial: IBC/NCLT, liquidation) | V1–V6 §2; App. K taxonomy | S+L |
| R-04 | Different intake/submission forms, dropdowns and process for negotiation, mediation, arbitration — by dispute type | V1–V6 §6; App. K §4 form-resolution rule | C |
| R-05 | Add further dispute types later (as Jupitice offers) without rebuilding | App. K §6 plug-in framework and expansion catalogue | C |
| R-06 | Research competitors ClaimBuddy, Insurance Samadhan (and others) | App. T §1; V4 §13 | S |
| R-07 | Separate login forms for disputing parties, case managers, mediators, arbitrators | App. S §2; P01 addendum | S |
| R-08 | Research Reliance Jio AI offerings (agent calling, automated calling, marketing tools, AI research, document drafting) | App. T §4; P07/P11 addenda | S+V |
| R-09 | Dispute Explorer tells pre-litigation users whether ADR suits their dispute; criminal matters not taken | App. K §1–§3; V1–V6 §5 | S+L |
| R-10 | AI drafts statement of claim/defence with index, list of dates, synopsis, affidavit from documents, screenshots, WhatsApp chats, PDFs, letters, emails; user reviews, edits, approves, e-signs, submits; Claude API or other AI pluggable | App. M; P11 addendum | S+L |
| R-11 | Detailed, customisable content and features incl. UI/UX; fewer clicks; mostly automated process | App. C, K, P, S; master §6 | C |
| R-12 | Aadhaar, PAN, DigiLocker, company registration, CIBIL APIs for quick secure onboarding | App. S §3 | S+L+V |
| R-13 | Pre-litigation mediation researched and built | App. K §5; V1–V6 §8; A (pre-suit machine) | S+L |
| R-14 | Web and mobile; different dashboards per user type; RBAC | App. S §5–§6; App. C; P12 | S |
| R-15 | Built in consonance with GDPR, CCPA, DPDP, IT Act and privacy/data-protection laws | App. Q §1–§3 | S+L |
| R-16 | Parties may appoint representatives (as advocates are appointed in litigation) | App. S §4 | S+L |
| R-17 | Copywriting: page content, internal content, catch lines, one-liners; SEO, GEO and AI-searchable | App. P | S |
| R-18 | Clean, minimal, modern UI/UX | App. C §design system; App. P §5 | S |
| R-19 | SaaS built for PCI DSS, SOC 2 Type I/II and ISO certifications; payment-gateway security; Razorpay-type integrations | App. Q §4–§6; P05 | S |
| R-20 | Multiple revenue streams incl. recurring; explain benefits of subscriptions and one-time products; detailed settings pages for billing and membership | App. O | S+L |
| R-21 | Advanced DMS: sharing, e-signing, search, filter; party chooses what to share | App. L §1–§4 | S |
| R-22 | Formal A4 documents with proper margins, formatted as the Supreme Court requires | App. L §5 (Supreme Court circular of 12 Mar 2020 parameters) | S |
| R-23 | Type copies of handwritten documents and WhatsApp screenshots via AI; user may correct | App. L §6; App. M §3 | S |
| R-24 | Translation into English; read UN official languages and main Indian languages | App. L §7 (6 UN languages + 22 Eighth Schedule languages) | S+V |
| R-25 | Publish awards and settlements on the website (like Supreme Court judgments) with party consent | App. R §3 (consent, redaction, s.42A A&C Act) | S+L |
| R-26 | Execute/implement awards and settlements; registration with district courts | App. R §4 | S+L |
| R-27 | Case status like the Supreme Court website: papers filed, dates, interim and final orders, parties | App. R §1–§2 | S |
| R-28 | Re-read the attached corpus for further requirements | S9 §8 corpus sweep → reflected across O, P, R, S, N | S |
| R-29 | Revise everything, find and fix errors | Appendix J (v1), §8 of this file (v2 review log) | S |
| R-30 | Private ADR courts: independent arbitrators/mediators use Equator as SaaS on subscription; separate page; run proceedings on their own terms | App. N §8; P10 addendum; App. O plans | S |
| R-31 | Smooth onboarding of empanelled neutrals; directory; transparency in working, onboarding and allotment | App. N §2–§6; P03 addendum | S |
| R-32 | Equator Code of Conduct; complaint mechanism; rating/feedback; assign more cases to best performers | App. N §5–§7 | S+L |
| R-33 | Research SIAC, Singapore mediation institutions and other world-class institutions | App. T §2; App. N, R adopt practices | S |
| R-34 | Research training providers; Equator ADR Institute (separate entity, equatoradr.com); 40-hour course; specialisations; country add-ons; Qualifying Assessment Programme (IMI) | App. N §9–§10; App. T §3 | S+L |
| R-35 | Neutral grades: C freshers (must train), B > 15 years, A retired judges / > 30 years (tech training; international and high-value matters); QAP linked | App. N §3–§4 | S |
| R-36 | Settlement/award drafting by neutrals; execution support | P06; App. R | S |
| R-37 | Rate cards customisable and approval-gated (19 Oct) | Master §7; App. B, O | C |
| R-38 | International commercial disputes; pricing in INR with foreign currency for international (19 Oct) | V6; App. B | S |
| R-39 | SEBI optional (19 Oct) | Master §1.2 | S |
| R-40 | Equator places its own calls; pre-suit mediation (20 Oct) | Master NN-12, §16 | S+L |

---

## 3. Decision log (v2)

| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| D2-01 | The six dispute types keep their names and codes (FIN, COM, FAM, INS, WRK, INT); subtypes are a two-level taxonomy inside each (`L1` category → `L2` subtype) held as configuration | Management brief; extensibility | V1–V6 §2; App. K |
| D2-02 | IBC/NCLT, liquidation and company-law disputes sit in COM. Equator never decides insolvency or other in-rem matters (*Vidya Drolia* (2021) 2 SCC 1; *Indus Biotech v Kotak* (2021)); it offers pre-admission settlement mediation, s.12A IBC withdrawal settlement support (as substituted by the IBC Amendment Act 2026: only after CoC constitution and before the first invitation for resolution plans, 90% CoC, NCLT decides within 30 days), out-of-court workouts, pre-pack documentation, and Companies Act s.442 panel mediation by individually empanelled neutrals | S2 §2, §8 | V2 |
| D2-03 | FAM covers all communities through a `regime_resolver` (personal law / statute by community, marriage law, place and date), never by asking the user's religion as a bare question; the answer is derived from the marriage law, the deceased's personal law and the user's selection with an explanation | S1 §1; privacy (sensitive data minimisation) | V3 |
| D2-04 | **Criminal matters are not undertaken.** Equator does not conduct criminal proceedings or mediate an offence. Where the law allows compounding or settlement of the civil dimension (NI Act s.138/s.147; civil terms in matrimonial matters with parallel FIRs), Equator mediates the civil/money dispute only and prepares the settlement and the compounding/consent papers for the court, which alone decides. Non-compoundable offences, triple talaq (Muslim Women (Protection of Rights on Marriage) Act 2019), POCSO, sexual offences, dowry offences and threats of violence are hard exclusions with signposting | Management brief; S1 §2.1; S3 FIN s.138 | App. K §3 exclusion list; V1, V3 |
| D2-05 | Separate login portals per persona on one identity backbone: Parties, Representatives (advocates/authorised persons), Mediators, Arbitrators (neutral portal with role-specific entry), Case Managers & staff, Enterprise, Private Chambers, Partners. Each portal has its own route, copy, authentication policy and post-login dashboard | Management brief; security (staff need stronger auth) | App. S §2 |
| D2-06 | Aadhaar: Equator registers as an **Offline Verification Seeking Entity** and uses Aadhaar QR/secure XML/Aadhaar app face verification; no online authentication or e-KYC unless and until a good-governance approval is obtained (G.S.R. 88(E), 31 Jan 2025, SWIK portal). DigiLocker via partner first, direct requester later. PAN, MCA, GSTIN, Udyam via licensed aggregators. **No credit-bureau pulls**: a party uploads its own credit report, or a lender tenant supplies it; Account Aggregator only through the lender as FIU | S7 §2 | App. S §3 |
| D2-07 | AI Pleadings Studio is a **self-help drafting tool available on identical terms to both sides**, grounded only in the user's documents and a verified legal corpus; Equator staff never draft or edit a party's pleading; the user is the author and approves every page; affidavits are sworn before an oath commissioner/notary (e-sign is not a substitute for the oath) | Advocates Act 1961 / unauthorised-practice risk (S7 §3, S9); *Pooja Ramesh Singh v J&K Bank Ltd*, 2026 INSC 668 (2 Jul 2026) on fabricated citations **[VERIFY — open: confirm text on the Supreme Court website; secondary source only]** | App. M |
| D2-08 | Court-format templates default to the Supreme Court circular of 12 Mar 2020 (A4, ≥ 75 GSM, both sides, Times New Roman 14, line spacing 1.5, quotations 12 single-spaced, margins 4 cm left/right and 2 cm top/bottom) and are configurable per forum; e-filing output PDF/A, OCR-searchable, bookmarked, within per-forum size limits | S8 §1 | App. L §5 |
| D2-09 | Languages: language identification and OCR/translation for the 6 UN official languages (Arabic, Chinese, English, French, Russian, Spanish) and the 22 Eighth Schedule languages; machine translations are labelled "for convenience" and a certified-translation workflow is offered for court use | Management brief; S7 §3 | App. L §7 |
| D2-10 | Publication of awards and settlements is **opt-in by all parties** in every track, including foreign-seated INT (master X-35); for India-seated matters A&C Act s.42A confidentiality binds arbitrators, institutions and parties; redacted (pseudonymised) by profile; FAM, POSH, health and minors' matters are never published in full; anonymised "digests of reasoning" allowed with consent; challenge decisions published redacted under the Equator Rules | S5 C5; S8 §3 | App. R §3 |
| D2-11 | Execution support = an execution pack prepared for filing (never labelled "court-ready" unless its court-format profile is verified — X-34) and guidance (A&C s.36 with CPC Order XXI; execution may be filed where assets are — *Sundaram Finance v Abdul Samad* (2018) 3 SCC 622; commercial-court jurisdiction for commercial awards; s.74 settlements; foreign awards ss.47–49), plus a registration workflow for documents that need it (Sub-Registrar under the Registration Act 1908). Equator does not represent parties in court | S8 §4 | App. R §4 |
| D2-12 | Neutral grades follow management's definition with competence gates (S6 §5): **Grade C — Associate Neutral** (entrants, including professionals with up to 15 years' experience; must complete recognised training and the Equator Qualifying Assessment); **Grade B — Senior Neutral** (> 15 years' verified professional experience + competence gate); **Grade A — Distinguished Neutral** (retired judges of the Supreme Court/High Courts or equivalent tribunals, or > 30 years' experience; subject training waived, Equator Tech Readiness mandatory). International and high-value matters go to A (and B within value caps) with an international endorsement. Retired judges acting as **mediators** still complete 40 hours of mediation training (MCPC standard) | Management brief; S6 §5.2 | App. N §3 |
| D2-13 | "Assign more cases to the best performing neutrals" is implemented as a **published, rules-based allocation**: hard eligibility filters (grade, endorsements, conflicts, language, availability) → rotation with concentration caps → a capped Quality Index soft score (process metrics only: timeliness, audit scores, moderated party feedback on conduct, CPD, complaint record). Settlement rates, outcomes, who won and client preference are never used (NN-03, NN-16). The allocation log is in every Independence Evidence Pack | NN-03 appointment defensibility; S5 C2; S6 §5.4 | App. N §6 |
| D2-14 | Neutral directory shows verified credentials, grade, endorsements, languages, availability and process statistics; **no paid or featured listings** and no outcome statistics | Neutrality; S9 | App. N §2; App. O |
| D2-15 | Institutional governance: an **Equator Institutional Committee** (majority external members) with Appointments, Challenge, Scrutiny, Ethics & Complaints, Rules, AI Oversight and Transparency sub-committees, supported by the Registrar; the company board takes no case decisions. The word "Court" is not used for any Equator body (NN-17) | S5 C1 (benchmark: SIAC/ICC/LCIA separate case bodies) | App. N §1 |
| D2-16 | Private ADR Courts (management's term) are built as the **Private ADR Chambers** SaaS (`chambers` module). The public product name is configurable; using "Court" in a tenant's name requires a counsel review under NN-17 and the Emblems and Names Act check (P10 FR-P10-01) | Master §1.4 (L2) and NN-17; P10 | App. N §8 |
| D2-17 | Equator ADR Institute is treated as a separate legal entity per management. Research found equatoradr.com presented as "Equa Trainings / Equa.Law", a brand of Infrabyx Consultancy (OPC) Private Limited, and claims ("IMI Accredited and Certified", "QAP" heading, "ISO 27001:2018") that overstate the IMI recognition (a Recognised Mediator Training Programme, June 2024) — to be corrected by the Institute. Equator refers learners to the Institute with a disclosed relationship, shows at least three recognised training options, never requires Institute training for empanelment, and runs its own competence assessment (Equator Qualifying Assessment Programme designed to IMI QAP standards; apply for IMI QAP approval) | S6 §1, §6 | App. N §9–§10; App. T §3 |
| D2-18 | Revenue: recurring streams (enterprise ODR contracts, GRM SaaS, POSH SaaS, Private Chambers plans incl. a low-cost practice tier, counsel tier with no procedural advantage, institutional memberships, API/white-label) and one-time products (filing/administration fees, neutral fees, certified copies, type copies, translations, transcripts, execution packs, e-stamp procurement, Explorer human review). Not sold: one-sided legal advice, merit opinions, paid visibility for neutrals; retail insurance uses flat fees only (no percentage-of-claim success fees) and shows free statutory routes first | S3 D3; S9 §1, §9; Advocates Act; IRDAI intermediary rules | App. O |
| D2-19 | Pricing and billing comply with the Consumer Protection (E-Commerce) Rules 2020, the CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023 (13 patterns linted), GST-inclusive display for consumers, and the RBI e-mandate framework (pre-debit notice, AFA above ₹15,000) | S9 §1 | App. O §6 |
| D2-20 | Primary tagline: **"Resolve disputes, not relationships."** Descriptor: "Online mediation, conciliation and arbitration — fair, fast and on the record." No court framing, no guaranteed outcomes | S9 §7 | App. P |
| D2-21 | Privacy: one control set satisfying DPDP Act 2023 + Rules 2025, IT Act s.43A/SPDI Rules 2011 and CERT-In Directions 2022, GDPR/UK GDPR (EU/UK parties in INT; Art. 27 representative when targeted), CCPA/CPRA (design-ready; thresholds assessed annually), Singapore PDPA and UAE PDPL for INT; the EU AI Act treats AI used in ADR as high-risk (Annex III from 2 Dec 2027) — Equator's AI stays assistive with human decision | S8 §5 | App. Q |
| D2-22 | Certification readiness: PCI DSS v4.0.1 scope minimised to **SAQ A** via Razorpay hosted/Standard Checkout (no card data touches Equator); SOC 2 Type I → Type II (6–12-month observation); ISO/IEC 27001:2022, 27701, 27017, 27018, 42001:2023, 22301, 9001; evidence automation (Vanta/Drata/Sprinto-class) | S8 §6 | App. Q §4–§6 |
| D2-23 | Reliance Jio: use Jio as a carrier (SIP trunk, DLT, JioCX SMS/RCS, branded caller ID) and evaluate Jio Haptik for voice/WhatsApp agents through an RFP; JioBrain / Reliance Enterprise Intelligence stay on a watch-list until public APIs, pricing and a data-processing agreement exist; conflict firewall because Reliance group companies may be parties | S7 §1 | App. T §4; P07 addendum |
| D2-24 | Representatives: party-granted, scoped, revocable **Letter of Authority / Vakalatnama** captured by e-sign; advocates verified against Bar Council enrolment; non-advocate representatives (family member, HR officer, company officer) allowed where the mechanism's rules permit; foreign lawyers limited per the BCI amendment of 13 May 2025 | S7; RES_A1b | App. S §4 |
| D2-25 | Probate copy: s.213 Indian Succession Act was omitted by the Repealing and Amending Act 2025 (assent 20 Dec 2025) — copy must not say probate is mandatory in Mumbai/Kolkata/Chennai; banks and buyers may still ask for it **[VERIFY — open: Act number and Gazette reference]** | S1 FR-S1-03 | V3 |
| D2-26 | MSMED Amendment Act 2026 (new s.18 referral by Facilitation Councils to a mediation service provider) is a major channel: build an MSEFC-readiness dossier and a feature-flagged referral track; activate only on commencement of the relevant section **[VERIFY — open: section and S.O. for commencement]** | S2 §8 | V2 |
| D2-27 | Uttarakhand Uniform Civil Code module (registration, divorce, succession) built behind a flag until counsel verifies the official text and the 2026 Ordinance | S1 FR-S1-06 | V3 |

---

## 4. Assumptions (to be confirmed by management)

| # | Assumption | If wrong |
|---|---|---|
| A-01 | Grade C also covers professionals with experience up to 15 years (management's definition named "freshers"; there was no grade for 1–15 years) | Add an intermediate band in `grading_policy` (configuration only) |
| A-02 | Grade B/A "years of experience" are counted from Bar enrolment, professional membership, judicial service or equivalent verified start date | Change the `experience_start_date` source list |
| A-03 | Equator ADR Institute will correct its website claims and confirm its operating entity before Equator links to it | Hide the referral card (flag `academy.institute_referral`) |
| A-04 | Equator will not employ advocates to represent parties; it may host an independent advocate directory without fee-sharing | Re-assess under Advocates Act and BCI Rules |
| A-05 | Launch geography is India first, with international parties in INT; the platform is not marketed to EU/US consumers at launch | Run full GDPR Art. 27 / CPRA programme before targeting |
| A-06 | Pricing figures in Appendices B and O are defaults pending Board approval | Edit in the fee editor (M-01) |

---

## 5. Open questions for qualified counsel (v2 additions; v1 items are in Appendix J)

1. Whether parties can waive A&C s.42A confidentiality to permit publication of India-seated awards, and the form of consent (App. R).
2. Whether AI-assisted self-help drafting of pleadings by a party on Equator's platform raises any issue under the Advocates Act 1961 or BCI Rules, and the disclosures needed (App. M).
3. Whether the Supreme Court direction of 19 Nov 2025 on pre-litigation mediation in HSA s.15 disputes is satisfied by private mediation (V3) **[VERIFY — open: order text]**.
4. Whether Equator's neutrals may conduct Companies Act s.442 panel mediations on the Equator platform and whether Equator may charge an administration fee (V2).
5. Aadhaar OVSE registration terms and retention limits for the Aadhaar verification certificate (App. S).
6. Use of "Court" in any Private Chambers tenant name (D2-16).
7. Uttarakhand UCC official text and the 2026 Ordinance (V3).
8. MSMED 2026 commencement and who designates mediation service providers (V2).
9. Equator Institutional Committee charter: independence from the company board and its legal effect on appointment defensibility (App. N).
10. Insurance consultants under Insurance Act s.2(10B)/s.42D — confirm that Equator's flat-fee mediation service is not an intermediary activity (V4).

---

## 6. Dependencies (critical path)

1. Legal entity particulars (CIN, registered office, GSTIN, DPO) → website, invoices, privacy notices.
2. Equator Rules (arbitration, mediation, conciliation, vertical rules), Code of Conduct and Institutional Committee charter → P03, P04, App. N.
3. Board approval of fee schedules → P05 go-live.
4. Vendor contracts (telecom/DLT, eSign/eStamp, KYC aggregator, Razorpay, LLM provider in India, OCR/translation) → P01, P05–P07, P11.
5. UIDAI OVSE registration; DigiLocker partner → P01.
6. Counsel opinions in §5 → feature flags.

---

## 7. Phase mapping of v2 additions

| Phase | v2 additions (see addendum at the end of each phase file) |
|---|---|
| P00 | Compliance-as-code scaffolding, `ops` tables, PII tagging, card-data guard, security baseline SC-01–SC-22, privacy-jurisdiction columns (App. Q); Ruleset Studio editors for taxonomy, explorer trees and pack manifests (App. K) |
| P01 | Separate login portals; onboarding integrations; representatives; dashboards and RBAC matrix (App. S) |
| P02 | Dispute Explorer v2; dispute-type plug-in framework; form resolution by type × subtype × mechanism (App. K); DMS core (App. L) |
| P03 | Grades A/B/C, Equator Qualifying Assessment, code of conduct, complaints, ratings, Quality Index allocation, directory transparency (App. N) |
| P04 | Mechanism-specific procedures per vertical (V1–V6 §7) |
| P05 | Revenue architecture, plans, billing and settings pages (App. O); PCI SAQ A boundary (App. Q) |
| P06 | Court-format templates, type copies, translation (App. L); publication and execution (App. R) |
| P07 | Pre-litigation cadence and templates (App. K); billing journeys (App. O); notification templates (App. P §4.5); Jio carrier/Haptik evaluation and vendor firewall (App. T §4) |
| P08 | Vertical specifications V1–V6 (the phase builds them in sub-iterations P08a–P08f) |
| P09 | MSEFC referral track; s.442 track; GRM variants (V2, V5) |
| P10 | Private ADR Chambers subscription page; training pathways and Institute referral (App. N §8–§10) |
| P11 | AI Pleadings Studio; provider abstraction; OCR router; evaluation per language (App. M) |
| P12 | Persona dashboards and logins on mobile (App. S) |
| P13 | Copy deck, SEO/GEO content system (App. P); Explorer entry pages (App. K); pricing routes (App. O); CMP and GPC (App. Q); Decisions Library and tracker pages (App. R); partner-portal boundary (App. S) |
| P14 | Privacy and certification readiness, evidence automation (App. Q) |

---

## 8. v2 review log

Six independent reviewers checked every v2 file end to end against the master, this file, Appendix F (names and codes), Appendix G (law) and Appendix B (fees). They looked for legal or factual errors, contradictions, broken references and ID collisions, error-code drift, internal inconsistencies, arithmetic, prohibited claims and formatting. A final cross-file pass then fixed the residual issues each reviewer reported outside its own files. All fixes were made in place.

| Pass | Files | Fixes | Most significant |
|---|---|---|---|
| RV1 | V1 FIN, V4 INS, P08 v2 addendum | 23 | V1's UPI-chargeback row renumbered (finally LR-PAY-008) to clear a collision; FIN concentration cap aligned to X-27; INT gates G1–G6 so the internationality test runs (NN-19); senior concession at age ≥ 60 per App. B; non-existent `FORM_FIELD_*` codes replaced by `VALIDATION_FAILED`; `intl.heap_lane` seed corrected; about 60 golden vectors recomputed, all correct |
| RV2 | V2 COM, V5 WRK | 22 | Mediation Act not-in-force list corrected (ss.2 and 55 added; s.26 in force); unamended MSMED s.18 statement now carries an open VERIFY marker; DPDP s.7 limb corrected; rule numbers remapped; clock names normalised to `clock_kind`; COM-02/COM-14 status 409 → 422; X-28 n ≥ 10 for public KPIs; about 40 vectors recomputed, all correct |
| RV3 | V3 FAM, V6 INT | 23 | MWPSC s.2(d): parents may claim whether or not senior citizens; publication aligned to Appendix R (consent after the outcome; arbitral and consensual flags OFF); `INT_SEAT_NOT_NOTIFIED` 409 → 422; co-mediation "× 2" now carries an open VERIFY marker; below-SIAC/ICC pricing line now needs a Claims Register record; all vectors correct |
| RV4 | K, L, M, R; P02, P04, P06, P11 addenda | 57 | K rule IDs remapped to V2; s.73(3) → s.73(4); mediation time box aligned to `med_contract_timebox`; outcome retention 13 years (X-36); one shared disclosures purpose list; `sign_instruments_on_behalf` locked until a power of attorney is verified (X-21); OCR routing per X-33; P11 provider fallback and Sarvam routing corrected (X-32); duplicate affidavit, WhatsApp-parser and status-sentence engines merged |
| RV5 | N, O, S; P01, P03, P05, P09, P10, P12 addenda | ~45 | Public statistics require n ≥ 10 (X-28); Grade B fast-track "≥ 10 settled" gate removed (NN-28); one EQAP fee for every candidate; P10 FR-ID clash resolved (FR-P10-V2-O1…O7); related-party approvals restated for a private company; "English and 11 Indian languages"; Appendix O arithmetic (Business Assure, dunning date, GRM overage) corrected |
| RV6 | P, Q, T; P00, P07, P13, P14 addenda; master and this file | ~43 | Publication opt-in in every track (X-35; D2-10); Anthropic direct API OFF and never used for case content (X-32); Appendix Q LR-PAY renumbering; stale P13 route and flag removed; Appendix P copy-lint table repaired; "court-ready" removed from D2-11; NN-14 aligned to Aadhaar offline verification; IRDAI arbitration copy limited to retail general insurance |
| Final | G, F, H, P08, P, T, V1, V5, master, P/Q/R/S/V5 formatting | ~75 | G LR-MED-021 time box aligned to Appendix A / X-40; G LR-LAB-002 and P08 clock renamed `wrk_wages_2wd`; G LR-FAM-019 parent correction; G LR-RBI-002 "CICs" ambiguity; G `fam_property_arbitration` and P08 seed set OFF (fail-safe); G §G.6 gains LR-PAY-007 (SAQ A) and LR-PAY-008 (UPI chargebacks); F `establishment_size` gains the 20-worker band; F §F.10.3 registers 162 v2 codes with dispositions; P08 FR-P08-23/56 statuses aligned to canonical codes (422 for non-arbitrability, waiver, fraud and retail arbitration), `MECH_NOT_PERMITTED_FOR_VERTICAL` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`, `WRK_WORKMAN_ARBITRATION_BLOCKED`, `fam.s15_prelit`; H WC-33 "court-ready" removed (EN and HI); Appendix T addendum mirrors P11 T01/T03; Appendix P §4.4 bound to the Appendix R sentence engine and `DD-R-WHO-DECIDES`; master X-29 restated (s.188 / s.177 where applicable / s.184, CS to confirm); 22 G §G.6 rows that only said "referenced without a defining row" now state the rule and its source; 30 horizontal rules that made 85 tables render as raw text in the Word copy fixed |

**Residual items not changed (decisions or counsel needed):**
- **V4 "one month" display margin.** V4 shows a conservative date beside the legal calendar-month date (X-40); management or counsel to confirm it, or switch both to the calendar month.
- **Appendix N deemed-consent publication of challenge decisions** stays behind an OFF flag (conflicts with NN-26 and X-35 unless counsel approves).
- **WRK flag naming.** WRK flags keep underscore names because Appendix G and P08 reference them.
- ***Sanjabij Tari* date.** The date differs between sources (25 v 26 Sep 2025); 25 Sep is kept.
- **V1 legacy gold flag.** `pledge_date` v `sanction_date` keying awaits Q-06.
- **Open markers.** Every open VERIFY marker is listed in Appendix J §J.6.
