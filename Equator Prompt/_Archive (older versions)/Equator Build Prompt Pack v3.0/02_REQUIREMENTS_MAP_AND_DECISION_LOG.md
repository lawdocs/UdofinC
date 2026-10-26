# 02 — Requirements Map, Decision Log and Assumptions (v3.0, 23 October 2026)

> Binding companion to `01_MASTER_PROMPT.md`. It maps every requirement given by Equator management (briefs of 19, 20, 21, 22 and 23 October 2026) to the file that specifies it, records decisions and the reasons for them, lists assumptions, and names questions that need qualified counsel. The coding agent reads this file at the start of every phase. Where this file and a phase prompt conflict, this file and the master prevail (master §15).

Research base for v2 (all under the build team's research archive): S1 Family & succession across communities · S2 Commercial, IBC/NCLT & company law · S3 Financial, insurance & competitors (ClaimBuddy, Insurance Samadhan, Jupitice, Presolv360, Sama, CORD) · S4 Workplace & pre-litigation mediation · S5 International institutions (SIAC, SIMC, ICC, LCIA, HKIAC, AAA-ICDR, MCIA, IIAC) · S6 Training, IMI QAP & neutral grading · S7 Reliance Jio AI, onboarding APIs & document AI · S8 Court formats, case status, publication, privacy & certifications · S9 Revenue, UX, SEO/GEO & corpus re-read. v1 research (R1–R5, C1–C5) and the verification of 514 flags (Appendix J) remain valid unless superseded below.

Research base for v3.0 (23 October 2026): **RA** Jupitice and the Jupitice ADR Marketplace · **RB** business models, institutions' revenue lines and equatoradr.com · **RC** Indian labour and payroll law · **RD** Microsoft 365, Google Workspace, Brevo, Adobe Express, portability, DevOps and audit · **RE** directory, marketplace and group-data law. Files cite them as [RA]…[RE].

---

## 1. File map (v2 and v3.0)

| File | Purpose |
|---|---|
| `00_README.md` | How to run the pack; decisions needed; completion checklist |
| `01_MASTER_PROMPT.md` | Constitution: product, NN rules (NN-01–NN-40), architecture, phases (P00–P21), precedence and cross-file resolutions (X-01–X-66) |
| `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` | This file |
| `phases/P00–P14` | Build phases; each ends with a **v2 addendum** and a **v3 addendum** listing new requirements |
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
| `appendices/U` | Institutional rules, codes and policy baselines: Equator Resolution Rules plan, Code of Conduct additions, staff code, privacy and cookie notices, terms of service, refund policy, disclaimer, security and accessibility statements, model clauses, remediation of the old Equa site (v2.1) |
| `appendices/V` (v3.0) | Configuration framework (NN-33 tiers L/G/T), Governed rule engine, configurability of all 469 open items, settings catalogue for every persona, `cfg` data model |
| `appendices/W` (v3.0) | Private ADR Chambers workspace v3: practice pages and domains, chambers and neutral customisation, staff and case-manager management, practice HR-lite with salary records and disbursal (`chm`) |
| `appendices/X` (v3.0) | Equator Operations Platform (`apps/ops`): departments and workspaces, CRM, onboarding, customer success, support tickets and grievances, knowledge base, automation engine (`ops`) |
| `appendices/Y` (v3.0) | Marketing, brand, social media, PR, partnerships and growth automation; campaign and social calendar; Brevo and Adobe Express as executors (`mkt`) |
| `appendices/Z` (v3.0) | Workforce HRMS, payroll under Indian labour law and internal controls: lifecycle, attendance, leave, performance, payroll engine, authority matrix, maker-checker (`hr`, `pay`, `ctl`) |
| `appendices/AA` (v3.0) | Equator Marketplace (three isolated surfaces; Private Practice Marketplace; sponsored listings OFF) and Infrabyx Professional Registry (`mkp`, `dir`) |
| `appendices/AB` (v3.0) | Revenue architecture v3 and the Revenue Stream Registry RS-01–RS-57 with kill switches and Board gates (`rev`) |
| `appendices/AC` (v3.0) | Workspace suites (Microsoft 365 first, Google later), open integrations catalogue, system-of-record register, data portability (`EQ-EXPORT-1.0`, `xpt`) |
| `appendices/AD` (v3.0) | Group companies and cross-functional operations: legal entities, shared services, cross-company grants, GDSA, secondment (`grp`) |
| `appendices/AE` (v3.0) | Engineering change, release, patch, backup, VAPT and audit management (`eng`) |
| `appendices/AF` (v3.0) | Competitive research v3 (reference): Jupitice and its ADR Marketplace, institutions' operating and revenue models, equatoradr.com, corrections to T, H and B |
| `phases/P15` (v3.0) | Configuration Studio and Tenant Settings (Appendix V) |
| `phases/P16` (v3.0) | Equator Operations Platform: CRM, Support, Onboarding and Customer Success (Appendix X) |
| `phases/P17` (v3.0) | Marketing, Brand and Growth Automation (Appendix Y) |
| `phases/P18` (v3.0) | Workforce HRMS, Payroll and Internal Controls (Appendix Z) |
| `phases/P19` (v3.0) | Equator Marketplace, Infrabyx Professional Registry and Revenue Stream Registry (Appendices AA, AB, AF) |
| `phases/P20` (v3.0) | Chambers Workspace v3 and Practice HR (Appendix W) |
| `phases/P21` (v3.0) | Group Operations, Integrations and Portability (Appendices AC, AD) |

---

## 2. Requirements map

Status key: **S** = specified; **S+L** = specified, needs legal sign-off before launch; **S+V** = specified, depends on vendor access or contract; **C** = configurable by design. R-44–R-70 come from the management brief of 23 October 2026 (brief items numbered as in the `00_README.md` §5 coverage map) and are worded as in the defining appendix.

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
| R-41 | Use the earlier Equa website (sites.google.com/view/equalaw) as the basis for the privacy policy, code of conduct, institutional rules and other policies (22 Oct) | App. U; App. N §5 (ECC v2.1 additions) | S+L |
| R-42 | Close or disposition every open item in Appendix J with internet research, verifying the responses supplied by management (22 Oct) | App. J §J.5–§J.7 | S+L |
| R-43 | Negotiation participants or facilitators as a distinct role (management master prompt, 22 Oct) | App. S §6.2 (`neutral_facilitator`); App. U §U.2.2 | S |
| R-44 | Three-tier configuration (NN-33) with a Configuration Studio; routine tenant changes need no super admin; legal and safety values are governed (23 Oct brief item 1) | App. V §V.1–§V.2, §V.5; P15 | C |
| R-45 | Every Appendix J open item classified by configurability, with tier, key or rule pack, who may change it and its default or fallback (Expanded Prompt; brief item 1) | App. V §V.3 (469 rows); App. J §J.9 | S |
| R-46 | A complete settings catalogue for every user type and module, showing what each user can change unaided (brief item 2) | App. V §V.4; P15 | C |
| R-47 | A Governed rule engine with jurisdiction and domain rule packs, effective dating, sandbox testing, impact analysis, rollback, review alerts and a regulatory-watch feed ("regulators change rules") | App. V §V.2; P15 | S+L |
| R-48 | Extensive customisation for Private ADR Chambers and independent neutrals, including public practice pages on the Equator website and tenant domains (brief item 2) | App. W §W.3, §W.4, §W.8; P20 | C |
| R-49 | Staff and case-manager management for chambers with queues, SLAs and confidentiality separation (brief item 2) | App. W §W.5; P20 | S |
| R-50 | Small HR module with salary records, payroll and disbursal for chambers staff (brief item 2) | App. W §W.6; P20 | S+L |
| R-51 | A separate Operations Platform (not the super-admin console) for operations, service delivery, after-sales, onboarding, customer success, support tickets and grievance redressal, with department workspaces and dashboards (brief items 3, 10) | App. X §X.1–§X.9; P16 | S |
| R-52 | A CRM open to Brevo and other tools, with integration and migration in both directions (brief item 3; NN-40) | App. X §X.4, §X.10; P16 | S |
| R-53 | "Autopilot" automation for operations with human approval for sensitive actions (brief item 7; Expanded Prompt) | App. X §X.12; P16 | S |
| R-54 | Group-ready operations: staff working cross-functionally for Finbyx and Udofin, dashboards and content shareable under controls; Microsoft 365 for operations staff (brief items 5, 11) | App. X §X.2.4, §X.11; P16; App. AD | S |
| R-55 | A full marketing, brand, social media, PR and partnerships architecture inside Equator, with the campaign and social calendar kept in Equator even where Brevo, Adobe Express or social tools send or publish (brief items 3, 7) | App. Y §Y.1–§Y.9; P17 | S+V |
| R-56 | "Autopilot" growth — funnels, lead magnets, nurture, webinars, referral and partner programmes, events and re-engagement — with human approval of public claims, pricing, testimonials, sensitive targeting and mass sends (brief item 7) | App. Y §Y.7; P17 FR-P17-30–FR-P17-37 | S+L |
| R-57 | Open, replaceable marketing tools with Equator as system of record for segments, consent and campaign results; analytics, attribution, budget/ROI and outcome-based contribution metrics for marketing staff (brief items 3, 4, 7; NN-35, NN-40) | App. Y §Y.6, §Y.11; P17 | S+V |
| R-58 | Internal HRMS with the full employee lifecycle — requisition, recruitment, offer, appointment letter, onboarding, work e-mail and access, probation, movements, secondment, exit and full and final settlement — remote-first across India (brief item 4) | App. Z §Z.3–§Z.5, §Z.13; P18 | S+L |
| R-59 | Transparent attendance (login/logoff), work measurement, role scorecards, ROI dashboards and performance appraisal for remote staff, including case managers working from home (brief item 4; NN-35) | App. Z §Z.6, §Z.7, §Z.10; P18 | S+L |
| R-60 | Leave and salary calculation under Indian labour law with versioned State and Central rule packs, statutory outputs and accounting export (brief item 4) | App. Z §Z.2, §Z.8, §Z.9; P18 | S+L |
| R-61 | Decentralised decisions within delegated limits, maker-checker, separation of duties, anti-corruption and anti-embezzlement controls, internal-audit workspace (brief item 4; NN-36) | App. Z §Z.12; P18 | S |
| R-62 | Equator Marketplace: three isolated surfaces; Private Practice Marketplace journeys, provider onboarding, payments as e-commerce operator, reviews, complaints, enterprise procurement, governance (brief item 12) | App. AA §AA.2–§AA.9, §AA.13; P19 | S+L |
| R-63 | Infrabyx Professional Registry (`dir`) and Professional Panel Register; post-resolution services (execution, registration, recovery) with party choice (brief item 8) | App. AA §AA.11, §AA.12; P19 | S+L |
| R-64 | Paid placement (sponsored listings) and display advertising under NN-34; marketplace revenue hooks into the stream registry (brief items 6, 12) | App. AA §AA.10, §AA.14; P19 | S+L |
| R-65 | A Revenue Stream Registry: every stream a versioned, maker-checker-approved record with status, scope, a kill switch effective within 5 minutes, legal and ethical dependencies, neutrality rating, tax treatment, refund code, cost drivers, KPIs and review cadence; prices changed only within approved bounds (brief item 6) | App. AB §AB.2–§AB.8; P19, P05, P13 | S |
| R-66 | A dated competitive and institutional benchmark register seeded from Appendix AF (source, evidence tag, publication and access dates, re-verification ≤ 90 days), the only source for comparative statements and revenue benchmarks; training-site corrections C1–C20 tracked as evidence (brief item 12) | App. AF §AF.0.3, §AF.8; P13, P10, P19 | S |
| R-67 | Microsoft 365 today (SKU to be confirmed; design works on Business Basic, Standard or Premium) with Teams and SharePoint; Google Workspace possibly later; documents open in MS Office; downloads as self-explanatory folders of Word, Excel and PDF; open, replaceable integrations with migration in and out (brief items 3, 5) | App. AC; P21 §4A–4D | S+V |
| R-68 | Multi-company group operations: cross-functional staff for Equator, Finbyx, Udofin and other group companies; dashboards, content and data shareable under controls; separate data, exports and audit per legal entity; handoffs and referrals between group businesses and registry professionals (brief item 11) | App. AD; P21 §4E–4H | S+L |
| R-69 | Change and patch management on GitHub branches, with protected branches, reviews, release control and patch SLAs (brief item 9) | App. AE §AE.1–§AE.5; P00 v3 addenda | S |
| R-70 | Backups, VAPT, IS audit, internal and external audit readiness, including auditor access and the accounting audit trail (brief item 9) | App. AE §AE.6–§AE.9; P14 v3 addenda | S+L |

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
| D2-14 | Neutral directory shows verified credentials, grade, endorsements, languages, availability and process statistics; **no paid or featured listings** and no outcome statistics. **v3.0: retained for the institutional directory; see D3-01/NN-34** (paid placement exists only on the separate Private Practice Marketplace) | Neutrality; S9 | App. N §2; App. O |
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
| D2-26 | MSMED s.18 as substituted by Mediation Act 2023 s.62 + Seventh Schedule and amended by MSMED (Amendment) Act 2026 s.8 (Council referral to a mediation service provider) is a major channel: build an MSEFC-readiness dossier and a feature-flagged referral track; activate only on commencement of the relevant section [Corrected 22 Oct 2026: neither Mediation Act s.62 nor Amendment Act s.8 is in force; S.O. 5575(E), 12 Oct 2026 commences ss.2–7, 11, 13–17 (15 Oct 2026) and s.12 (15 Dec 2026) only] | S2 §8 | V2 |
| D2-27 | Uttarakhand Uniform Civil Code module (registration, divorce, succession) built behind a flag until counsel verifies the official text and the 2026 Ordinance | S1 FR-S1-06 | V3 |
| D2-28 | The Equa (2022) rules, code and policies are adopted as the **base** of Equator's policy set, corrected for current law and the NN rules: no "court" naming, no outcome or certification claims, no Equator-held escrow, no CVV or Aadhaar-number collection, 15-day arbitrator challenge, opt-in publication, non-participation record instead of a "Failure Report" | Management brief 22 Oct; App. U §U.12 | App. U |
| D2-29 | Every open item carries one of seven dispositions (verified, corrected, provisional, counsel sign-off, vendor confirmation, product decision, watch) with evidence, residual uncertainty, approver, production gate and recheck trigger; an item closes only on `verified` or `corrected`, or on written sign-off by its approver | Management response of 22 Oct; App. J §J.6 | App. J |

### 3A. Decision log (v3.0, 23 October 2026)

D3-01–D3-09 are binding decisions set for all v3 writers; D3-10–D3-44 are recorded in the appendix named in the last column, which states them in full.

| ID | Decision | Reason / source | Effect |
|---|---|---|---|
| D3-01 | **Paid placement scope** as NN-34: only on the Private Practice Marketplace, only for non-advocate private-practice neutrals and chambers, in a separate labelled slot, capped, equal rate card, flag `marketplace.paid_placement` OFF until Board approval and counsel sign-off; never touches the institutional directory, allocation, eligibility, Quality Index, grading or conflict checks; never sold to advocates, CAs, CSs or CMAs. D2-14 retained for the institutional directory | Brief item 6 (preference placement); BCI Rules Part VI Ch. II r.36, Ch. III r.2; [RE] | NN-34; App. AA §AA.10; App. AB RS-19 |
| D3-02 | **Operations Platform is a separate app and portal**, group-ready ("Infrabyx Work OS" engine, Equator as first company), not the super-admin console | Brief item 3 | `apps/ops`, `eq-portal-ops`; App. X; P16 |
| D3-03 | **Internal HRMS and payroll built in**, with exports to and from specialist payroll and accounting tools | Brief item 4 | App. Z; `PAYROLL_EXCHANGE_PORT`; App. AC §AC.11 |
| D3-04 | **Microsoft 365 SKU to be confirmed** by the Company Secretary; the design works on Business Basic ("Business Starter" is not a Microsoft plan name) | Brief item 5; [RD] F1.1 | Master §18 item 6; App. AC §AC.3 |
| D3-05 | **Professional registry is a group shared service** owned by an entity the Board designates, under a Group Data-Sharing Agreement | Brief item 8; NN-38, NN-39; [RE] | App. AA §AA.12; App. AD |
| D3-06 | **Default department model, fully configurable** (16 departments; Internal Audit independent of operations) — management's departmental explanation was not received | Brief item 10 | Master §18 item 5; App. X §X.3; FR-P18-02 |
| D3-07 | **Export package convention** for NN-37 portability | Brief item 5; Expanded Prompt | Implemented by D3-41; App. AC §AC.13 |
| D3-08 | **Revenue stream registry with kill switches** | Brief item 6 | App. AB; R-65 |
| D3-09 | **GitHub Enterprise Cloud recommended** for protected-environment approvals on private repositories; until licensed, `ReleaseApprovalWorkflow` is the compensating control | Brief item 9; [RD] F5.1 | P00 FR-P00-08 note; App. AE §AE.2.1; X-66(f) |
| D3-10 | **One configuration plane** in `cfg` (definitions, values, scopes, locks, packs, rule-pack metadata); rule-pack versions stay in `core.rulesets`/`core.ruleset_versions` so PinSets work unchanged; `core.config_change_requests` remains the configuration approval engine; T changes apply immediately through `cfg.setting_changes` with audit and one-click rollback | NN-21, NN-33 | App. V |
| D3-11 | **Registry before use** — no code reads a setting or flag not registered in `cfg.setting_definitions` with tier, scopes, type, bounds, default, fallback, owner role and audit class; CI fails on an unregistered read (`CFG_UNREGISTERED_KEY`) | NN-33 | App. V; P15 |
| D3-12 | **Tenant rule-pack adaptation** — adopt, adapt within overlay bounds, or author tenant contractual rules; never relax a statutory or platform floor; adaptations affecting third parties' rights need the tenant's named `legal_reviewer` and carry the tenant-rule disclosure | NN-33; brief item 1 | App. V §V.2.11 |
| D3-13 | **Configured fallback is mandatory** for every Governed definition; it applies automatically and visibly; there is never a "no rule" state | NN-33 | App. V §V.2.10 |
| D3-14 | **No super-admin dependency** — `platform_admin` cannot change a tenant's T or tenant-scope G values except in a tenant-granted support session (≤ 72 h, logged, visible); routine G changes are made by named functional roles | Brief item 1 | App. V; P15 |
| D3-15 | **Practice pages are a separate surface** (`/chambers/{slug}`, `/people/{person}`, tenant sub-domain, verified custom domain), never linked from, ranked with or rendered inside `/neutrals` or any allocation, eligibility or live-case screen; Equator hosts them as an intermediary (IT Rules 2021 r.3) | NN-28, NN-34; [RE] F3.3 | App. W |
| D3-16 | **Tenant-governed approvals** — G settings affecting third parties' rights inside a chambers are approved by the tenant's holder of `chm.config.approve.legal` after platform validators; Equator validates L guardrails but does not review, approve or endorse tenant legal content | App. N §8.5 | App. W |
| D3-17 | **Practice HR is the chambers' own employer tool** — the chambers is employer and fiduciary, Equator processor; calculations are tools, not advice; Equator never holds or routes salary money | NN-13, NN-36 | App. W §W.6 |
| D3-18 | **Single-person separation of duties** — where only one natural person can act, NN-36 is met by compensating controls (passkey step-up after a minimum gap, cooling and out-of-band confirmation, anomaly holds, optional external checker, `SINGLE_PERSON_SOD` reporting) | NN-36 | App. W §W.6.10 |
| D3-19 | **Confidentiality wall** — `chambers_hr` and `chambers_accounts` never read case content; case roles never read HR or salary records (Cerbos `DENY`, separate RLS, field-level encryption of salary data) | NN-11, NN-16 | App. W |
| D3-20 | **Operations Platform data plane** — all EOP business data in schema `ops` in the isolated business database (with `growth` and `mkt`); no grants on case, sealed, `hr` or `pay` schemas; core data only through allow-listed read models | NN-16, NN-38 | App. X §X.2.2; X-50 |
| D3-21 | **Equator's own user grievances run on the P09 GRM engine** as variant `EQ_SERVICE`; support tickets (`ops.tickets`) are a separate object that converts to a grievance on defined triggers | EGP-2026.1 | App. X §X.8; X-52 |
| D3-22 | **Declared systems of record** — the Equator CRM (`ops`) for accounts, contacts, leads, opportunities, consent preferences (mirrored to `core.consent_records`), tickets and implementations; Brevo only for raw email-engagement events; `billing` for plans, subscriptions, invoices and receivables; no external tool is ever system of record for consent | NN-40; [RD] DI-B | App. X §X.10.1 |
| D3-23 | **Automation engine ownership** — Appendix X owns the no-code engine, its catalogue, permissions, preview, rate limits, exception paths, audit, pause/rollback and the locked human-approval list; Appendix Y owns marketing automations built on it | Brief item 7 | App. X §X.12 |
| D3-24 | **Commercial-to-case firewall** — case-administration roles and neutrals never see an account's revenue, health score, renewal date, churn risk, discounts or pipeline; EOP sees case services only as a metadata projection | NN-03, NN-16, NN-28 | App. X §X.3.3, §X.14 |
| D3-25 | **Equator is system of record** for segments and send audiences, consent and suppression, content approvals, publication evidence and **reported** campaign results (frozen `mkt.metric_snapshots`); Brevo only for raw engagement events it generates; external tools are executors behind ports | NN-40; [RD] F3.1 | App. Y §Y.1.3, §Y.6 |
| D3-26 | **Adobe Express is an asset hand-off**, not a publishing integration (no public publishing API); Equator's own `SOCIAL_PORT` adapters publish only where platform access is granted, each behind a flag OFF; `manual_handoff` is the default | [RD] F3.2, F3.3 | App. Y §Y.4.6–§Y.4.8 |
| D3-27 | **No referral rewards of any kind to advocates, CAs, CSs or CMAs** (or their firms); professionals may be relationship partners without reward; cash referral fees only to non-professional partners under a written, disclosed agreement | NN-34; BCI r.36, Ch. III r.2; ICAI, ICSI, ICMAI guidelines ([RE] F1.2–F1.5) | App. Y §Y.7.5; X-54 |
| D3-28 | **Funnel technique register** — locked video players, resetting timers, unbound scarcity, fictitious reference prices, unverified testimonials, outcome or saving promises and "evergreen presented as live" webinars are prohibited; paid low-ticket webinars allowed for B2B education only with full price incl. GST, refund terms and operator identity | CCPA Misleading Advertisements Guidelines 2022; Dark Patterns Guidelines 2023; NN-17, NN-29 | App. Y §Y.7.1–§Y.7.3 |
| D3-29 | **Attribution and contribution** — a versioned attribution-model registry (default position-based 40/20/40, with first- and last-touch views), maker-checker changes that never silently restate history; marketing contribution metrics outcome- and quality-based, visible and disputable | NN-35 | App. Y §Y.11 |
| D3-30 | **Workforce systems of record** — `hr`, `pay`, `ctl` for people, organisation, attendance, leave, compensation, payroll and approvals; Microsoft 365/Google downstream for identity and mailbox only; Tally/Zoho Books for the general ledger; specialist payroll tools optional import/export partners | NN-40; [RD] F1.4 | App. Z |
| D3-31 | **Remote-employee jurisdiction default** — `establishment_state` and `work_location_state` per effective date; S&E Act, holidays and "appropriate Government" follow the establishment State; minimum wage the higher of the two; PT and LWF follow the establishment State until a written CA/counsel opinion is filed | [RC] F6.3 (recommendation) | App. Z §Z.2.4, §Z.8, §Z.9 |
| D3-32 | **Equator Standard leave policy** (earned 18, casual 8, sick 12, 10 paid holidays, carry-forward 45, refused leave never lapses) for every employee, validated against the statutory floor of every class and State and raised automatically where a State floor is higher (e.g., Rajasthan) | [RC] C.14, F6.2 | App. Z §Z.8.3 |
| D3-33 | **Output-based measurement only** — keystroke logging, webcam capture, covert screen recording, off-hours location tracking, personal-device monitoring and reading personal communications are Locked OFF; individual ROI views OFF until a DPIA is approved | NN-35; [RC] F12 | App. Z §Z.6, §Z.7 |
| D3-34 | **One transaction-approval engine** (`ctl`) for authority matrix, maker-checker, separation of duties and exceptions across HR, payroll, billing, procurement, expenses, payee changes, role grants and sensitive exports; default Delegation of Financial Powers values are proposals subject to Board approval | NN-36 | App. Z §Z.12; X-56 |
| D3-35 | **Operating model of the Private Practice Marketplace** — Equator acts as a marketplace e-commerce entity for every category; listing needs an active Chambers workspace (from CH-LITE) and a booking creates the matter in the provider's Chambers tenant; percentage take only on non-advocate providers, flat fee for advocate-neutrals; collection model G (`provider_merchant_of_record` default); paid bookings disabled until the tax memo records the e-commerce-operator position; settlement sums never pass through the marketplace | E-Commerce Rules 2020 ([RE] F3.1); NN-13, NN-34 | App. AA §AA.2.4 |
| D3-36 | **Registry topology and the Post-Resolution Advocate Panel** — Directory Owner (Board-designated) is data fiduciary; consumers are independent fiduciaries; GDSA is a provisioning gate (`DIR_GDSA_MISSING`); optional panel `EQ-POSTRES` behind `postres.advocate_panel` OFF — listing free, no fee-share, commission, referral fee or rating; shown only inside the party's own case | NN-38, NN-39; DPDP s.8(2) | App. AA §AA.11.4, §AA.12.1 |
| D3-37 | **Sponsored-listing and display-advertising commercial rules** — product name "Sponsored listing"; ≤ 2 slots per page and ≤ 20% of results; separate block above organic results with the NN-34 label; equal flat rate card per category × geography (Subject to Board approval); rotation with equal impression share; ad-reviewer maker, compliance-officer checker; targeting by category and geography only | NN-34; [RA], [RB] | App. AA §AA.10.3 |
| D3-38 | **Training through equatoradr.com is a related-party stream, ₹0 to Equator by default** — no revenue unless the Board approves an arm's-length arrangement under Companies Act 2013 s.188 (s.184 disclosure; s.177 only where an Audit Committee is mandatory) **[CS to confirm related-party status under s.2(76)]**; RS-22 OFF until corrections C1–C20 are evidenced and entity, CIN and GSTIN are displayed; training never affects empanelment, grade, allocation, EQAP fee or directory position | Master X-29; [RB] §1.1 | App. AB; App. AF §AF.4 |
| D3-39 | **Revenue sequencing and stop/go governance** — streams launch in waves; viability review monthly for two quarters then quarterly, annual Board review; Board thresholds held as Governed settings; any stream rated N2 or above or dependent on counsel, a vendor contract or an unconfirmed fact defaults OFF with its approver named | Brief item 6 | App. AB §AB.6.5, §AB.7.3 |
| D3-40 | **Workspace topology and meeting policy** — one suite-neutral `WORKSPACE_PORT`, adapter `m365_graph` default; every feature works on Business Basic; Business Premium (or Basic plus add-ons) recommended for console, Tier-High, sealed or finance access; Keycloak (`eq-portal-ops`) is the access control point regardless of SKU; Equator-administered proceedings never run on Teams or Google Meet (locked); Google Workspace adapter OFF (no India data region) | [RD] F1, F2 | App. AC §AC.2–§AC.8 |
| D3-41 | **Export package `EQ-EXPORT-1.0`** (implements D3-07) — one human-readable folder taxonomy (`Equator_Export_<Org>_<YYYY-MM-DD>/00_README.pdf`, `01_Organisation_Profile/` … `99_Manifest/`); Standard folder package and Archival bag (RFC 8493 BagIt); ZIP64 with UTF-8 names; ASCII names; path budget root folder ≤ 40 characters and path below root ≤ 140; DOCX/XLSX/PPTX working copies, PDF/A-2b record copies, byte-exact signed originals, CSV + JSON data, manifest CSV + JSON with SHA-256; `xpt` canonical; `POST /v1/me/exports` an alias of `POST /v1/exports` | NN-37; [RD] F4.2 | App. AC §AC.13–§AC.14 |
| D3-42 | **Group model** — `grp`: group → legal entities → brands, billing profiles, policies, administrators; `group_admin` (no data access by default) vs `entity_admin`; shared services as processor under an intra-group processing agreement, partitioned by `legal_entity_id`; cross-company access only by `grp.cross_company_grants` (purpose, data categories, default 90 days, per-role maximum ≤ 365, target-entity approver, auto-expiry, access log) under an active GDSA; one employer of record per employee with `hr.secondments`; s.188 flags; ethical walls; referrals only on the party's authorisation; Equator case, neutral and allocation data never leave Equator's partition | NN-38; [RE] F4, F5 | App. AD |
| D3-43 | **Change and release governance** — trunk-based development with ≤ 2-day branches; release branches only to hotfix a deployed release; umbrella `rel-*` tags; four change classes (`standard`, `normal`, `high`, `emergency`); deterministic risk score with "sensitive area ⇒ CAB" locked; small-company CAB; two-person production approval; freeze calendar; customer notice floors for breaking changes | [RD] F5.3, F5.4; Q §7.3 | App. AE §AE.2, §AE.4 |
| D3-44 | **Patch, backup and assurance defaults** — patch SLAs Critical ≤ 72 h, High ≤ 7 d, Medium ≤ 30 d, Low next release (≤ 90 d) with Q SC-11 values as locked ceilings; weekly base-image rebuild; weekly automated restore tests; `eq-backup` account with the air-gapped vault and source mirror; Vault Lock compliance mode; annual comprehensive CERT-In-aligned audit + quarterly VAPT + major-release VAPT; production VAPT window and bug bounty OFF pending CS/CTO and Board; auditor workspace with ≤ 90-day watermarked grants | [RD] F6, F7; Q SC-11, SC-17; master §11 | App. AE §AE.5–§AE.8 |

---

## 4. Assumptions (to be confirmed by management)

| # | Assumption | If wrong |
|---|---|---|
| A-01 | Grade C also covers professionals with experience up to 15 years (management's definition named "freshers"; there was no grade for 1–15 years) | Add an intermediate band in `grading_policy` (configuration only) |
| A-02 | Grade B/A "years of experience" are counted from Bar enrolment, professional membership, judicial service or equivalent verified start date | Change the `experience_start_date` source list |
| A-03 | Equator ADR Institute will correct its website claims and confirm its operating entity before Equator links to it | Hide the referral card (flag `academy.institute_referral`) |
| A-04 | Equator will not employ advocates to represent parties; it may host an independent advocate directory without fee-sharing. *v3.0:* the directory is the consent-based Infrabyx Professional Registry (NN-39); public advocate search stays OFF and advocates receive no referral reward of any kind (NN-34) | Re-assess under Advocates Act and BCI Rules |
| A-05 | Launch geography is India first, with international parties in INT; the platform is not marketed to EU/US consumers at launch | Run full GDPR Art. 27 / CPRA programme before targeting |
| A-06 | Pricing figures in Appendices B and O are defaults pending Board approval | Edit in the fee editor (M-01) |
| A-07 (v3.0) | The D3-06 default department model fits Equator until management explains its departmental structure (the brief said it would but did not) | Rename, merge or add departments in configuration (no code change) |
| A-08 (v3.0) | The Microsoft 365 plan held is Business Basic (management's "Business Starter" is not a Microsoft plan name) | Capability matrix and licence rules switch by detected SKU (App. AC §AC.3); nothing else changes |
| A-09 (v3.0) | Equator Resolution Service Private Limited is the first company on the Operations Platform; Finbyx and Udofin join later under Appendix AD | Group onboarding runs the P21 group go-live gate first |

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
11. Whether Equator becomes a "recovery agency" under RBI (NBFC – Responsible Business Conduct) Directions 2025 para 6(11A) if a lender pays it to run negotiation on defaulted accounts — **launch-blocking for lender-paid FIN programmes** (J.5, J-057/J-095/J-108).
12. The Data Fiduciary / processor role for each Equator workflow, and reliance on DPDP s.17(1)(a) for institutional case administration before 13 May 2027 (J-055, J-099).
13. Contractual appellate arbitration tier: s.34(3) trigger and s.29A for the appellate tribunal (J-003/J-034/J-148).
14. POSH Act s.11(4): start point of the 90-day inquiry period (J-047 and related).
15. BCI Rules Part VI Ch. II r.36 limits on advocate-neutral profiles (languages, courts, fee range, ratings) (J-083, J2 A4/A9 items).

**v3.0 additions (23 October 2026):**

16. **Paid placement on the Private Practice Marketplace** (NN-34, D3-01, D3-37): whether sponsored listings for non-advocate neutrals and chambers are lawful and compatible with the Mediation Council of India's future conduct standards, the E-Commerce Rules disclosure duties and the dark-patterns rules; Board approval of the stream and rate card is needed before `marketplace.paid_placement` is switched ON (App. AA §AA.10; RS-19).
17. **Advocate directory** (NN-39): whether any public advocate search or profile is permissible under BCI Rules Part VI Ch. II r.36 (verbatim proviso and 2008 Schedule) pending *Sulekha.com v P.N. Vignesh*, SLP (C) 25794/2024, and *Anil Pandey v BCI*, WP (C) 817/2026; whether r.36 reaches advocate-neutral marketplace profiles; the terms of the Post-Resolution Advocate Panel (`postres.advocate_panel` OFF) (App. AA AA-OI-01–03).
18. **ICAI, ICSI and ICMAI aggregator and referral bars**: CAs may not list on app-based aggregators, CMAs may not list on aggregator sites or join referral networks, CS websites are advertisements; confirm the ICSI aggregator position, the ICMAI Guidelines 2025 Gazette date and the ICAI fee-sharing clauses before `register.ca`, `register.cs`, `register.cma` change from OFF (App. AA AA-OI-07; X-62(e)).
19. **E-Commerce (Amendment) Rules 2026**: Gazette text, G.S.R. number, sub-rule numbers and commencement (reported 1 Jan 2027); the characterisation of ADR services after *D.K. Gandhi*; r.5(6) for group-affiliated sellers (App. AA AA-OI-04; App. AF OI-AF-05; App. AD).
20. **Payroll and tax parameters**: every Appendix Z §Z.2.4–§Z.2.5 parameter marked `NOT_CONFIRMED` or `SECONDARY_ONLY` (bonus ceilings, OSH Central Rules details, ESIC rates, the EPF wage-ceiling notification and the September 2026 split month, income-tax slabs) needs sign-off by the Payroll Compliance Officer with a CA or counsel before a live pay run; the remote-employee S&E Act, PT and LWF position (D3-31); night work by women working from home; marketplace e-commerce-operator tax (LR-TAX-007/008) (App. Z §Z.20; App. AA AA-OI-05).
21. **Employee monitoring notice** (NN-35): the employee notice for attendance, login/logoff and work measurement — quoting the enacted DPDP s.7(i) text — and the DPIA before individual ROI views are enabled (D3-33; App. Z §Z.6, §Z.20 item 10).
22. **Secondment**: GST on secondment (*CCE v Northern Operating Systems*; CBIC Instruction 05/2023-GST), the host entity's own DPDP basis where it directs a secondee's work, PF/ESI for part-time multiple appointments and OSH Code contract-labour thresholds for intra-group deputation (App. AD §AD.18).
23. **Related-party Group Data-Sharing Agreements and shared services**: related-party status under Companies Act 2013 s.2(76) of Infrabyx Consultancy (OPC) Pvt Ltd and the group companies, s.188 approvals (and r.15(3) thresholds) for GDSAs, intra-group service agreements and registry consideration, and the Infrabyx shareholding chain (D3-05, D3-38, D3-42; App. AD §AD.18; App. AA AA-OI-09).

---

## 6. Dependencies (critical path)

1. Legal entity particulars (CIN, registered office, GSTIN, DPO) → website, invoices, privacy notices.
2. Equator Rules (arbitration, mediation, conciliation, vertical rules), Code of Conduct and Institutional Committee charter → P03, P04, App. N.
3. Board approval of fee schedules → P05 go-live.
4. Vendor contracts (telecom/DLT, eSign/eStamp, KYC aggregator, Razorpay, LLM provider in India, OCR/translation) → P01, P05–P07, P11.
5. UIDAI OVSE registration; DigiLocker partner → P01.
6. Counsel opinions in §5 → feature flags.
7. (v3.0) Company Secretary confirms the Microsoft 365 SKU (D3-04) → P18 workspace provisioning, P21.
8. (v3.0) Board designates the registry owner entity and approves the GDSA; Board approves the revenue streams and the sponsored-listing rate card (D3-05, D3-37, D3-39) → P19.
9. (v3.0) Board approves the Delegation of Financial Powers (authority matrix) (D3-34) → P18 go-live.
10. (v3.0) Payroll parameters signed off and the employee monitoring notice issued (§5 items 20–21) → first live pay run and attendance capture (P18).
11. (v3.0) GitHub Enterprise Cloud licensed, or the `ReleaseApprovalWorkflow` compensating control recorded (D3-09) → P00 production deployments.
12. (v3.0) Management confirms or replaces the D3-06 department model → first position creation (P18) and EOP workspaces (P16).

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

### 7A. Phase mapping of v3.0 additions (23 October 2026)

The v3 addenda appended to P00–P14 come from the "Phase addenda" sections of the v3 appendices (requirements `FR-Pnn-V3-<Letter>nn`); P15–P21 are new phases.

| Phase | v3.0 additions (source appendices) |
|---|---|
| P00 | Rule-pack kind, alias registry for flags, Ruleset Studio → "Rules and legal", open-item linkage, `REGWATCH_PORT` (V); `hr`/`pay`/`ctl` schemas and entity RLS, `WORKSPACE_PORT` and `PAYROLL_EXCHANGE_PORT`, config kinds, edit-log guard (Z); `grp` schema, grant-aware entity scope, `GROUP_SHARE_SCOPE` CI test (AD); GitHub organisation, plan and rulesets, CODEOWNERS, required checks, environments and OIDC, `eng` schema, change records, fallback approval path, backup topology and restore tests, ledger audit-trail guard, JIT production access (AE) |
| P01 | Portability alias and SKU-sufficiency check at role grant (AC); cross-company grants in the policy engine and the `entity_admin` role (AD) |
| P02 | Case and intake settings from `cfg`; PinSet includes rule packs (V); case export from the DMS; file to Equator from mail (AC) |
| P03 | Institutional profile isolated from practice pages; no `chm` reads in allocation; consented chambers parties in the blind conflict index (W); "Request this panel neutral" rename, `NO_PAID_PLACEMENT` extended and `MKP_SURFACE_ISOLATION`, conflict edges from panels and private engagements, paid-visibility item in disclosures (AA); group relationships in conflict checks (AD) |
| P04 | Hearing platform lock — Equator-administered proceedings stay on LiveKit (AC) |
| P05 | Money settings G-elevated; tax-memo flags with shadow ledgers (V); chambers invoice profiles, `PAYOUT_PORT` disbursal, consultant fees with TDS, add-on entitlements (W); authority matrix, payroll journals, unified payee controls (Z); marketplace tax engine, payouts with SoD, transfer holds, stream codes on lines (AA); registry guard in billing, kill-switch run-off, new refund codes, packages and coupons, marketplace tax lines, revenue recognition (AB) |
| P06 | Post-Resolution Professional Chooser, authorised document transfer, retire `/advocates` (AA) |
| P07 | Contact and channel settings; telecom pack (V); workspace is not a notice channel (AC) |
| P08 | Vertical parameters and State packs as rule packs (V) |
| P09 | Enterprise settings catalogue and onboarding setting packs (V); GRM variant `EQ_SERVICE`, enterprise ticket webhooks, console Help panel, service-stats read model (X); enterprise procurement, lender Professional Panel Register, external-member flow unchanged (AA); Finbyx/Udofin connectors as the lender's processor channel, referral signposting (AD) |
| P10 | Role templates, onboarding wizard, branding and domain v3, run-off covering practice HR, practice dashboards (W); chambers add-on streams, plan-dependent take and advocate-neutral flat fee, advocate credits removed, tenant revenue settings (AB); chambers exits and mirrors (AC); Institute referral gate on C1–C20 (AF) |
| P11 | Agents `support_triage`, `meeting_followup`, QBR narratives, scoring-weight suggestion (X); marketing copy assistant, social triage, accessibility drafting, guardrail evals, synthetic-media rules (Y); HR agents and prohibitions, deterministic fallback (Z); AI artefacts as changes, evals as release gates, model-provider vendor review (AE) |
| P12 | Chambers staff self-service, work queues and owner approvals on mobile (W); mobile change records, staged rollout gates, signing-key custody, mobile VAPT (AE) |
| P13 | Website and legal-entity settings (V); practice page renderer, lint profile, structured data, "Report this page", `/private-adr-chambers` copy v3 (W); capture inbox and promotion (X-51), SCR-P13-18 superseded, public help centre, preference centre (X); landing-page blocks, channel lint profiles, partner-portal amendment (X-54), lead hand-off with UTM (X-53), operator footer (Y); marketplace public pages, display-ad slots, dark-pattern certificate (AA); generated pricing and "How Equator earns", ad and sponsored slots OFF (AB); benchmark register seed and competitor-claim linter (AF) |
| P14 | Configuration health and audit evidence (V); schema hygiene, Operations Platform go-live, access reviews, VAPT scope (X); marketing go-live, dark-pattern self-audit, crisis tabletop, social account security (Y); controls evidence, SoD access reviews, HR go-live (Z); portability and integration go-live (AC); group go-live gate (AD); change management, patch SLA engine, release notes, rollout rings, backup and DR evidence, VAPT programme, auditor workspace, evidence catalogue, internal audit support, log retention (AE) |
| P15 | Configuration Studio and tenant settings (V) |
| P16 | Operations Platform: CRM, support, onboarding, customer success (X); Brevo CRM adapter conformance (AC); grants in the Operations Platform (AD) |
| P17 | Marketing, brand and growth automation (Y); marketing and social adapter conformance (AC) |
| P18 | Workforce HRMS, payroll and internal controls (Z); group columns for secondments and the cross-entity employment guard (AD) |
| P19 | Marketplace and professional registry (AA); `rev` schema, registry console, kill-switch service, price governance, viability reviews, related-party register (AB); marketplace benchmark acceptance set and quarterly transparency report (AF) |
| P20 | Chambers workspace v3 and practice HR (W) |
| P21 | Group operations, integrations and portability (AC, AD) |

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
| v2.1 research | All 469 open items (J-001–J-170, J2-001–J2-299), eight research groups | 355 edits + ~25 cross-file fixes | Dispositions for every item (App. J §J.5); 19 launch gates; corrections incl. LR-RBI-005 (contact hours in force now; microfinance window), LR-DPDP-001 (s.44(2) from 13 May 2027), LR-TEL-010 (30/60/90-day tiers), MSMED referral (Mediation Act s.62 + Amendment Act s.8, not commenced), SEBI fee payer, CIC circular /73, CoFT /96, IT Rules G.S.R. 120(E), IR Code clause letters, NCLT/NCLAT format, Singapore Convention Art. 1(3)(b), *Snidha Mehra*, Sahamati naming; Appendix U added; ECC additions; `neutral_facilitator` role |

**Residual items not changed (decisions or counsel needed):**
- **V4 "one month" display margin.** V4 shows a conservative date beside the legal calendar-month date (X-40); management or counsel to confirm it, or switch both to the calendar month.
- **Appendix N deemed-consent publication of challenge decisions** stays behind an OFF flag (conflicts with NN-26 and X-35 unless counsel approves).
- **WRK flag naming.** WRK flags keep underscore names because Appendix G and P08 reference them.
- ***Sanjabij Tari* date.** The date differs between sources (25 v 26 Sep 2025); 25 Sep is kept.
- **V1 legacy gold flag.** `pledge_date` v `sanction_date` keying awaits Q-06.
- **Open markers.** Every open VERIFY marker is listed in Appendix J §J.6.

### 8A. v3.0 build and review log (23 October 2026)

**Scope.** The management brief of 23 October 2026 (configurable open items and settings; chambers and neutral customisation with practice HR; a separate Operations Platform with CRM, support, onboarding, customer success, marketing, PR and grievances; workforce HRMS, payroll and controls; Microsoft 365 and Google Workspace; switchable revenue streams and paid placement; autopilot; post-resolution professionals and a group directory; change, patch, backup and audit; a default department model; multi-company operations; Jupitice and an Equator Marketplace) and the ChatGPT "Expanded Prompt" where consistent with the binding decisions D3-01–D3-09.

| Pass | Files | Work | Most significant |
|---|---|---|---|
| Research RA–RE | Five research streams | Jupitice; business models and equatoradr.com; labour and payroll law; Microsoft 365, Google, Brevo, Adobe Express, portability, DevOps and audit; directory, marketplace and group-data law | "Business Starter" is not a Microsoft plan; EPF wage ceiling ₹25,000 from 17 Sep 2026; BCI r.36 and the SLP (C) 25794/2024 appeal; ICAI/ICMAI aggregator bars; GitHub Enterprise Cloud needed for protected environments on private repositories |
| W1 | Appendix V, P15 | Writer | 469 open items classified (L 65, G 346, T 7, N 51); Configuration Studio |
| W2 | Appendix W, P20 | Writer | Practice pages as a separate surface; practice HR-lite on the shared payroll engine |
| W3 | Appendix X, P16 | Writer | Operations Platform `apps/ops`; CRM system of record `ops`; automation engine |
| W4 | Appendix Y, P17 | Writer | Marketing architecture with Brevo and Adobe Express as executors; no referral rewards to professionals |
| W5 | Appendix Z, P18 | Writer | HRMS, payroll rule packs, authority matrix, output-based measurement |
| W6 | Appendices AA, AB, AF; P19 | Writer | Three-surface marketplace, registry, 57-stream registry, Jupitice research |
| W7 | Appendices AC, AD, AE; P21 | Writer | Workspace port, `EQ-EXPORT-1.0`, group model, engineering governance |
| RVA | V, P15 | ~35 fixes | Four keys carrying two tiers re-keyed; V §V.3.3 counts recomputed; `marketplace.paid_placement` made a G platform flag |
| RVB | W, Z, P18, P20 | ~37 fixes | No new `PAY_STATUTORY_WAIVER_FORBIDDEN`; Rajasthan leave floor above the Equator Standard; gratuity provision formula; shared `bank_file` adapter on `PAYOUT_PORT` |
| RVC | X, Y, P16, P17 | ~45 fixes | One consent mirror, one partnership pipeline, one Brevo ingress; `mkt.market_segments`; `MKT_APPROVAL_NODE_MISSING` replaced by `OPS_AUTOMATION_APPROVAL_REQUIRED` |
| RVD | AA, AB, AF, P19 | ~32 fixes | RS-57 registered; e-commerce TDS ₹5 lakh threshold; institution-reported statistics tagged [C]; flags `billing.eco_*` and `platform.rev.ads.enabled` |
| RVE | AC, AD, AE, P21 | ~42 fixes | Export path budget root ≤ 40 / below root ≤ 140; `core.consent_records`; audit register in `eng` |
| I1 | New v3 files | Integration of review requests targeting V–AF, P15–P21 and a consistency sweep | Export taxonomy per AC; one Brevo flag and budget; alias seed table in Appendix V |
| I2 | v2.1 files (master, this file, README, Appendices B, D, F, G, H, J, O, Q, S, T; P00, P01, P05, P10, P13) | Integration into the existing pack | NN-33–NN-40; X-43–X-66; R-44–R-70; D3-01–D3-44; F §F.10.4 v3 error register; S §6.9 v3 roles; AF corrections to T, H and B; e-commerce TDS threshold correction in G, B and P05; advocate credit rewards removed (X-54/X-62) |

**Residual items not changed (decisions or counsel needed):** the AF findings that need a Board decision (AFC-B-02 plan-dependent take and advocate-neutral flat fee; AFC-B-04 Card ACAD entity and prices; AFC-B-10 bundled day rates and staged billing) and AFC-T-11 (extra fee rows, held in Appendix AF §AF.2.1); the cluster placement of the workforce, chambers, marketplace, revenue, portability and group schemas (ADR in P15); the counsel questions in §5 items 16–23. Integration details: `INTEGRATION_I2.md` in the build archive.
