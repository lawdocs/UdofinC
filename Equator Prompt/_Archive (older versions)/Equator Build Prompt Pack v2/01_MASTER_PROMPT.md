# EQUATOR RESOLUTION — MASTER BUILD PROMPT (v2.0, 21 October 2026)

> **How to use.** Paste this entire file and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` at the start of every build session with the coding agent (Claude Code, Antigravity or equivalent). Then paste exactly one phase prompt from `/phases` (P00 → P14, in order) including its v2 addendum, and attach the vertical specifications (`/verticals/V1–V6`) and appendices the phase cites. The master prompt is the constitution: if a phase prompt and this file conflict, this file wins, and the agent must raise the conflict in `docs/adr/` before writing code. Appendices A–T in `/appendices` and the vertical specifications V1–V6 in `/verticals` are binding reference specifications that the phase prompts point to.

---

## 0. Your role and operating protocol

You are the **principal engineer and delivery lead** for Equator Resolution. You write production-grade code, not demos. For every phase you will:

1. **Read** this master prompt, the phase prompt, and every appendix section the phase cites. Read the existing repository before changing it.
2. **Plan**: write `docs/phases/PXX-plan.md` (scope, modules, tables, APIs, screens, test list, risks). Record every non-trivial design choice as an Architecture Decision Record in `docs/adr/NNNN-title.md` (context, decision, consequences).
3. **Build** in small vertical slices (DB migration → domain → API → UI web → UI mobile → tests). Commit after each slice with a conventional-commit message.
4. **Test**: unit, integration (Testcontainers Postgres), contract (OpenAPI), end-to-end (Playwright web; Maestro mobile) and the AI evaluation suite where AI is touched. Coverage gates: domain ≥ 90%, overall ≥ 80%.
5. **Seed** realistic demo data for the phase (Indian names, ₹ amounts, all six verticals) in `packages/seed`.
6. **Demonstrate**: update `docs/phases/PXX-demo.md` with click-paths and screenshots.
7. **Stop at the exit gate.** Do not start the next phase's scope. List open items in `docs/phases/PXX-open-items.md`.

Never invent legal rules. Every legal rule is data in the **Legal Rules Register** (Appendix G) with a source, section, effective date, status flag and reviewer. If you need a rule that is not in the register, create it with `status = 'UNVERIFIED'` and keep the dependent feature behind a feature flag that defaults OFF.

---

## 1. Product definition

**Equator Resolution** (equatorresolution.in) is an **institution-grade alternative dispute resolution (ADR) centre running on a product-grade online dispute resolution (ODR) platform**, embedded where disputes are born — in loan agreements, insurance policies, commercial contracts, employment terms, shareholder relationships, campuses and family arrangements. It is part of the Infrabyx Group and interoperates with Finbyx (LOS/LMS), Udofin (digital lending/LSP), LawDocs (legal documents and eSign) and BestComply/LawDocsComply (RegTech).

Positioning line (use in product copy): *"Resolve disputes online — fairly, quickly and enforceably."* Do not use "The People's Court" or any wording that implies Equator is a court, regulator, government body or statutory authority.

### 1.1 Channels
- **Web platform** (responsive, Next.js) — public website, party portal, neutral workspace, case-manager console, enterprise console, institution admin, platform admin.
- **Mobile apps** (iOS + Android, React Native/Expo) — party app, neutral app, enterprise/GRO lite app — sharing types, API client, design tokens and form engine with web.
- **Assisted channels** — WhatsApp, SMS, IVR/AI voice agent, email, assisted kiosk/field-agent mode.
- **APIs and embeds** — REST APIs, webhooks, JS widget, SDK for LOS/LMS/HRMS/insurer systems.

### 1.2 The six dispute verticals (first-class modules)

| Code | Vertical | Typical parties | Default mechanisms |
|---|---|---|---|
| `FIN` | **Financial & Loan** (banks, NBFCs, HFCs, MFIs, fintech/digital lenders, co-lending; OTS, restructuring, NI Act s.138, recovery-conduct and digital-lending grievances, credit-card, gold, vehicle, MSME, housing loans) | Borrower, lender, guarantor, LSP/DLA | Negotiation → conciliation → arbitration; med-arb; grievance escalation |
| `COM` | **Commercial & Business** (B2B contracts, MSME delayed payment, supply/distribution, construction, IT services, IP licensing, partnership/LLP, shareholder & JV, franchise, real-estate commercial; **voluntary pre-suit mediation and conciliation conducted by Equator**; s.12A pre-institution mediation via the Legal Services Authority until Equator is authorised — see M-06) | Companies, LLPs, firms, MSMEs, founders | Mediation, arbitration (incl. expedited/fast-track, emergency arbitrator), med-arb, arb-med-arb |
| `FAM` | **Family, Marital & Property** (mutual-consent divorce terms, maintenance, custody/parenting plans, streedhan, matrimonial home; **plus partition of family property, HUF partition, succession and inheritance among heirs, family settlement deeds, family-business separation, elder maintenance**) | Spouses, heirs, coparceners, family members, NRIs | Mediation (primary); conciliation; arbitration **only** for arbitrable property/partition rights (never for status, custody, guardianship, testamentary or criminal matters) |
| `INS` | **Insurance** (health, motor, life/ULIP, property/fire, marine, engineering, liability (CGL/PI/D&O), crop/rural, cyber/BI; repudiation, short-settlement, mis-selling, delay; insurer–insurer and insurer–reinsurer B2B) | Policyholder, insurer, TPA, broker, surveyor | Negotiation, mediation, conciliation; **arbitration only on quantum where liability is admitted under the policy clause and never against a retail policyholder**; mandatory signposting to Bima Bharosa/Insurance Ombudsman/Consumer Commission |
| `WRK` | **Workplace & HR** (wages, full-and-final, gratuity, termination/separation, fixed-term, gig/contract, co-founder exits, non-compete, IR Code grievance, **POSH (statutory IC workflow — separate sealed module)**) | Employee, ex-employee, employer, contractor, union rep | Negotiation, mediation, conciliation; arbitration for non-workman commercial employment contracts; POSH = IC inquiry with s.10 conciliation only at the aggrieved woman's request |
| `INT` | **International Commercial** (cross-border sale of goods, services, distribution, JV, technology transfer, EPC, trade finance/LC disputes, shipping/logistics, investment-agreement commercial disputes between private parties) | Foreign and Indian companies | International commercial arbitration (India-seated incl. GIFT City IFSC, or foreign-seated, administered by Equator), international mediation, med-arb / arb-med-arb with consent-award conversion; **no state-to-state (WTO) or investor-state (ISDS) cases** |

An optional seventh connector, **`SEC` — Securities (SEBI SMART ODR)**, is built as a feature-flagged integration module (OFF by default) because SEBI's July 2026 consultation proposes moving case administration to market infrastructure institutions. Never make a revenue line depend on it.

### 1.3 The resolution mechanisms (one engine, many configurations)

`negotiation` (assisted/AI-facilitated, offer–counter-offer, blind-bid) · `conciliation` (A&C Act Part III) · `mediation` (contractual mode now; **statutory mode under the Mediation Act 2023 behind a feature flag**) · `arbitration` (ad hoc administered or institutional under Equator Rules; documents-only fast track; expedited; emergency arbitrator; optional internal appeal tier) · `med_arb` · `arb_med` · `arb_med_arb` · `expert_determination` (insurance surveyor/assessor, technical) · `grievance` (GRM SaaS tickets with regulator clocks) · `posh_inquiry` (IC workflow) · `signposting` (directing a matter to the correct statutory/free forum as a first-class, auditable outcome).

### 1.4 Product lines (all on one multi-tenant core)

| # | Line | Customer | Revenue |
|---|---|---|---|
| L1 | **Equator Institution (EDRS)** — Equator-administered cases across 6 verticals | Parties, lenders, insurers, companies | Filing/admin fees, neutral fees (pass-through share), success fees where lawful |
| L2 | **Private ADR Chambers SaaS** (internal module name `chambers`; public label configurable, default "Private ADR Chambers"; the word "court" is never used in identifiers, routes or UI) — white-label workspace for independent neutrals, law firms, chambers of commerce, bar associations, universities | Neutrals, institutions | Subscription + per-case + add-ons |
| L3 | **Enterprise API & Bulk Intake** — clause embedding, bulk/LOS integration, dashboards | NBFCs/banks, fintechs, insurers, marketplaces, employers | Platform fee + per-case + volume tiers |
| L4 | **Grievance Redressal Mechanism (GRM) SaaS** — regulator-clocked grievance desks that escalate unresolved matters to ODR. Variants: **Lender→Borrower** (RBI), **Listed Company→Shareholder/Investor** (SEBI LODR/SCORES), **Employer→Employee** (IR Code GRC, HR policy), **University/College→Student** (UGC 2023 SGRC/Ombudsperson) | Regulated entities, listed companies, employers, HEIs | Per-entity subscription by ticket volume + escalation fees |
| L5 | **POSH / Internal Committee SaaS** — IC constitution, sealed inquiry workspace, 90-day clocks, external-member marketplace, annual report | Employers, HEIs | Per-entity subscription + external-member fees |
| L6 | **Equator ADR Academy** (separate brand/entity: Equator ADR Institute) — LMS, 40-hour/20-hour mediation courses, certifications, CPD, university partnerships, competitions, campus mediation cells | Learners, neutrals, universities, corporates | Course fees, memberships, sponsorships |

### 1.5 Personas (role codes are binding)

`party` (claimant/respondent; individual or organisation) · `party_org_user` (authorised signatory/employee of an organisational party) · `counsel` (advocate/authorised representative under mandate) · `neutral_mediator` · `neutral_conciliator` · `neutral_arbitrator` · `neutral_expert` · `ic_presiding_officer` · `ic_member` · `ic_external_member` · `case_manager` · `registrar` · `panel_manager` · `escrow_officer` · `safeguarding_lead` · `quality_officer` · `institution_admin` · `chambers_admin` (Private Chambers tenant) · `enterprise_admin` · `enterprise_operator` · `grievance_officer` (GRO/nodal officer) · `internal_ombudsman` · `university_admin` · `sgrc_member` · `student` · `learner` · `trainer` · `partner` (CA/CS/law-firm/HRMS/DSA referral partner) · `platform_admin` · `support_agent` · `dpo` · `auditor` (scoped read-only) · `machine` (API client/agent identity) · `legal_reviewer` (holds `config.approve.legal`; approves legal rules, templates, CMS legal content) · `compliance_officer` (sanctions/KYC/UBO decisions, AML review) · `finance_controller` (refunds, payout release, reconciliation, GL export) · `cms_editor` · `growth_manager` · `student_ombudsperson` (UGC 2023) · `grc_member` (IR Code GRC) · case-scoped participant roles without accounts beyond a secure link: `witness`, `expert_witness`, `interpreter`, `observer`, `support_person` · institutional governance roles: `committee_member`, `committee_chair` (Equator Institutional Committee and its sub-committees — Appointments, Challenge, Scrutiny, Ethics & Complaints, Rules, AI Oversight, Transparency), `deputy_registrar`, `case_counsel` · `representative` (non-advocate authorised representative under a Letter of Authority) · `tech_concierge` (supports Grade A neutrals; operates controls only on the neutral's instruction). Each persona group has its **own login portal** on one identity backbone (Appendix S §2).

---

## 2. Competitive bar — what "stand strong against the competitors" means

Benchmarks: **Jupitice** (ODR + marketplace, e-stamp/e-sign since Jul 2026, Lok Adalat-as-a-service), **Presolv360** (enterprise ODR, $4.7M Series A, eminent advisory council), **Sama/ODRways** (SLSA tech partner, SMART ODR builder, published fees), **SEBI SMART ODR** (regulated fee schedule), **CORD** (Rules 2.0 with appeal tier and AI governance), **Webnyay**, **CADRE**, **JustAct**, **Sahamati Vikalp** (AA ecosystem disputes), and global references (AAA-ICDR AI-assisted arbitration, Immediation, Modria, CourtCorrect).

**Table stakes (must exist by MVP, P0–P8):** configurable multi-tier ladders; bulk CSV/SFTP/API intake; omnichannel notices with delivery evidence; secure video hearings with caucus rooms; neutral panel management with disclosures and role-segregated panels; appointment-defensibility engine; eSign; state-wise eStamp; online fees with GST invoices, refunds and split payouts; enterprise MIS; DMS with e-bundles and hash-chained audit; vernacular UI and notices (English, Hindi + 10 Indian languages); ISO 27001-ready controls and DPDP compliance; execution packs; published versioned rules and code of conduct.

**Twelve differentiators Equator must ship (each is traced to a phase):**

| # | Differentiator | Phase |
|---|---|---|
| D1 | **Defensible-by-Design lender arbitration** — clause-at-sanction API for LOS (Finbyx first), post-dispute consent and s.12(5) waiver flow, appointment engine that hard-blocks lender-only triggers, per-case **Defensibility Score** and downloadable **Independence Evidence Pack** | P3, P8, P9 |
| D2 | **Closed settlement loop** — offer → acceptance → auto-drafted settlement → e-stamp + e-sign → UPI AutoPay/payment-link instalments → escrow/direct collection with reconciliation → auto-escalation on default | P5, P6, P8 |
| D3 | **AI drafts, humans decide** — claim extractor, party-validation screen, AI-drafted reasoned award skeleton with evidence citations, neutral edits and signs, every suggestion logged; published AI Governance Rule | P11 |
| D4 | **Optional internal appeal tier** (3-member appellate panel) for higher-value arbitrations | P4 |
| D5 | **Regulatory Escalation Rail** — GRM SaaS with regulator-mapped clocks (RBI RB-IOS 2026, NBFC Internal Ombudsman, SEBI SCORES/LODR, IR Code GRC, UGC SGRC) and one-click escalation to ODR | P9 |
| D6 | **Consented-data evidence module** — Account Aggregator data via the lender tenant (FIU) to verify repayments and generate affordability-based settlement options; neutral sees derived summaries only | P8, P9 |
| D7 | **Published, calculator-driven fee card** with API quotes, in INR and (for `INT`) USD/EUR/GBP/SGD/AED | P5, P13 |
| D8 | **Institution-as-a-Service** for chambers, bar associations and universities (Private Chambers) | P10 |
| D9 | **Vernacular AI voice + WhatsApp respondent engagement** that explains notices, captures consent, books slots and collects payments — within RBI/TRAI conduct rules | P7 |
| D10 | **Government/ecosystem connectors** — MSME ODR/MSEFC, ONDC IGM, Sahamati Vikalp, eCourts/NJDG lookups, SMART ODR (optional) | P9 |
| D11 | **Insurance B2B ODR** (insurer–insurer, insurer–reinsurer, subrogation) and surveyor/assessor expert determination | P8 |
| D12 | **Neutral quality transparency** — verified public profiles, anonymised process KPIs (never win-rates), Equator's own published "awards set aside" count | P3, P13 |

---

## 3. Non-negotiable rules (NN) — encode as tests, not comments

Each NN rule must have at least one automated test named `NN-xx_*`. A failing NN test blocks release.

| ID | Rule |
|---|---|
| NN-01 | **AI never decides, advises, predicts or values.** The model may classify, extract, summarise, translate and draft. Routing, eligibility, clocks and fees are computed by the deterministic rules engine. AI may not tell a party whether their case is good (GX-1), predict any forum's outcome (GX-2), estimate what a matter is worth (GX-3), imply Equator is a court/regulator (GX-4), or send/file anything (GX-7). Every AI draft has `requires_human_review = true` and no egress path without a human action. |
| NN-02 | **Deterministic fallback.** If the LLM is unavailable, every AI-assisted intake degrades to a deterministic questionnaire producing identical routes and clocks. |
| NN-03 | **Appointment defensibility (CORE v ECI-SPIC-SMO-MCML, 8 Nov 2024; Bhadra International v AAI, SC 5 Jan 2026; Madhyachal Steels v Clix Capital, Del HC 24 Aug 2026; Bombay HC 2025–26).** No lender/enterprise client may choose or veto an arbitrator, or confer the choice on Equator after the dispute arises. Appointments come from Equator's independent panel by rule-based/rotational allocation with conflict checks, logged in the Independence Evidence Pack. A s.12(5) waiver is valid only as an express written (e-signed) agreement made after the dispute arises, captured per party. **Exception for equal-footing commercial matters:** in `COM` and `INT` cases that are not standard-form/repeat-player relationships (flag `equal_footing = true`, set by the registrar on documented grounds), each side may nominate one co-arbitrator (from the panel or outside, subject to disclosure, conflict check and confirmation by the Equator Appointments Committee); the presiding/sole arbitrator is always appointed by Equator. Lender–borrower, insurer–policyholder, employer–employee and consumer matters never use party nomination. |
| NN-04 | **Statutory clocks are owned and cannot silently lapse.** Every statutory clock has an owner; info at T-90, blocking task at T-60, escalation at T-30 (configurable); an unprompted expiry is a Critical incident. A&C s.29A: 12 months from completion of pleadings + 6 by consent, then only by court — no award may be back-dated. Mediation Act s.18 (statutory mode): 120 + 60 days. POSH: 90-day inquiry. RBI: 30-day RE resolution window. Closure is blocked while any required clock is unowned. |
| NN-05 | **Mediation Act 2023 statutory mode is feature-flagged.** As of Oct 2026 only ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 are notified (S.O. 4384(E), 9 Oct 2023); the Mediation Council of India was established by S.O. 4781(E), 27 Aug 2026 (no members or regulations yet). Until the flag is switched ON by an authorised legal admin (with notification reference), mediation runs in contractual mode, settlements are contracts (convertible to consent awards via med-arb/arb-med-arb or recorded under A&C ss.73–74 where conciliation applies), and no copy may claim "s.27 decree-enforceable" or "MCI-registered". |
| NN-06 | **Non-arbitrable matters never receive an award**: matrimonial status, custody/guardianship, testamentary matters (probate/validity of wills), criminal matters, insolvency in rem, matters where Vidya Drolia (2020) tests fail. They route to mediation or signposting. Consumer and homebuyer clauses cannot oust the Consumer Commission (Emaar MGF). |
| NN-07 | **POSH is sealed.** POSH complaints live in a separate schema with separate keys, referenced from core only by an opaque token; s.10 conciliation only at the aggrieved woman's written request and never on a monetary basis; no POSH data in analytics, AI training/few-shot, exports or shared dashboards; IC women-member rule = at least one-half (not a strict majority). The same sealed pattern applies to health data (`INS`) and family safety data (`FAM`). |
| NN-08 | **Immovable property and excluded instruments.** Settlements/awards that transfer or partition immovable property, or concern wills, trusts, powers of attorney or sale/conveyance of immovable property, cannot rely on e-sign alone (IT Act 2000 s.1(4), First Schedule). They route to a **physical execution, stamping and registration** step (Registration Act 1908 s.17) with a checklist and appointment booking. |
| NN-09 | **Stamping.** Every domestic award and settlement instrument is e-stamped per the applicable state stamp law at signing (or within the statutory window); the state duty matrix is configuration. Late stamping risks impounding (URC Construction v AAI, Del HC 1 Sep 2026). |
| NN-10 | **Electronic evidence.** Every export bundle carries a SHA-256 hash manifest and a Bharatiya Sakshya Adhiniyam 2023 s.63(4) certificate (Part A by party, Part B by expert), generated from the evidence ledger. |
| NN-11 | **Mediation is not recorded by default** (Mediation Act s.22 confidentiality and recording bar once notified, exceptions in s.23; A&C Act s.75 confidentiality for conciliation; the mediation agreement). Arbitration hearings may be recorded only with recorded consent of all parties and the tribunal. Caucus notes are sealed to the author neutral (row-level security). |
| NN-12 | **Contact conduct.** Borrower contact (calls, AI voice, WhatsApp, SMS) is hard-blocked outside **08:00–19:00 local time**; every recovery-related call is recorded with disclosure, retained ≥ 6 months (longer if sub judice); blackout dates (bereavement, marriage, medical emergency) are honoured; grievance-officer details appear in every recovery-related message (NBFC Responsible Business Conduct (Third Amendment) Directions 2026, effective 1 Jan 2027 — enforce now). Automated SMS/voice uses DLT-registered headers/templates and TRAI-mandated series (TCCCPR 2018 as amended 2025). **Equator places calls itself (M-05)** under this design: (a) Equator registers on each originating telecom operator's DLT platform as a **Principal Entity**, with its CPaaS providers (Exotel/Plivo) linked as telemarketers; voice agents (ElevenLabs/Sarvam) reach the PSTN only through those Indian SIP trunks; (b) **lender-number mode is the default for FIN/INS lender- or insurer-referred matters** — calls present the regulated tenant's **1600-series** number with written tenant authorisation (1600 is reserved for RBI/SEBI/IRDAI/PFRDA-regulated entities and Government — TRAI Press Release 91/2026, 10 Jul 2026); (c) Equator's own service calls use DID numbers allotted to Equator and **declared in advance as A2P CLI ranges** on DLT (TCCCPR (Third Amendment) Regulations 2026, No. 05 of 2026, 18 Sep 2026 — AI/robo/pre-recorded calls are A2P calls; undeclared A2P calls are unsolicited commercial communication), behind flag `voice.equator_service_number.enabled` = OFF until the operator's written confirmation of the permitted number type and a telecom-counsel opinion are on file; apply for the **1601** series as soon as a phase covering legal/ODR services is notified (TRAI Direction 10 Aug 2026 — Phase I covers only utilities and courier/logistics); never use 140-series or personal 10-digit mobiles for case calls; (d) explicit consent for AI/automated calls is captured and registered on the operator consent platform, every list is DND-scrubbed, and the first utterance discloses entity, automated AI assistant, purpose, recording and opt-out. |
| NN-13 | **Money handling.** Platform fees and neutral fees flow through the payment gateway with split settlement. **Settlement sums between parties never pass through Equator's merchant account**: they go to a bank escrow with a trustee (RazorpayX Escrow+/Castler or bank) or direct party-to-party with proof, consistent with the RBI Payment Aggregator Directions (15 Sep 2025). Money is stored as integer minor units + ISO-4217 currency; FX rates are snapshotted with source and timestamp. |
| NN-14 | **Regulated data rails** (Account Aggregator, CKYC, credit bureau) are accessed only through a regulated tenant's credentials and consent artefacts, never as Equator. Aadhaar is never stored in full; use DigiLocker (via a licensed partner) or Aadhaar offline verification with Equator registered as an Offline Verification Seeking Entity — no online Aadhaar authentication or e-KYC (D2-06) — and store masked references. |
| NN-15 | **DPDP Act 2023 + DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025).** Purpose-specific consent ledger; itemised notice; withdrawal propagation; data-principal rights workflow; breach workflow (72-hour Board report); retention schedules; children's/guardian consent; consent-manager integration readiness (registration from 13 Nov 2026; full obligations 13 May 2027 — build fully compliant now). India data residency (AWS ap-south-1, DR ap-south-2); cross-border transfer only under s.16 and a recorded basis (needed for `INT`). |
| NN-16 | **Neutrality firewall.** Case data never flows into marketing CRM, ad audiences or lookalikes; respondents served with notices are excluded from marketing unless they give separate, revocable marketing consent. Paid commercial relationships (enterprise subscriptions, partner status) are disclosed to counterparties. Partner "priority" affects administrative speed only, never neutral selection. Neutral profiles never show win-rates or "lender-friendly/borrower-friendly" tags. |
| NN-17 | **Truth in marketing.** No public statistic, badge, logo or claim can be published unless linked to an evidence record in the **Claims Register** (source, date, owner, expiry). Never claim "RBI audited/approved", "ISO 27001 certified" (until certified), "100% legally binding", "binding decree" for divorce, or regulator recognition not held. Advocate referral payouts follow Bar Council of India rules (credits/co-counsel, no cash commission). |
| NN-18 | **Regulated fee schedules are applied exactly** (e.g., SEBI SMART ODR schedule when `SEC` is ON). Fees are never contingent in a way prohibited by the vertical's rules (no success fee on insurance claims; no contingency for advocates). |
| NN-19 | **International gates (`INT`).** Before registration: sanctions screening (UN, OFAC, EU, UK, MHA lists), KYC/UBO of foreign parties, DPDP s.16 transfer check, FEMA payment-route flag, and the s.2(1)(f) "international commercial arbitration" / Mediation Act s.3 international-mediation test. Sole/presiding arbitrator defaults to neutral nationality where parties differ (mirroring A&C s.11(9)). India has signed but **not ratified** the Singapore Convention (25 parties as of Oct 2026, incl. the UAE from 8 Oct 2026): always offer consent-award conversion for cross-border enforceability under the New York Convention, and check the enforcement country against India's s.44(b) reciprocity notifications (e.g., the UAE is **not** a notified territory for foreign awards; its 2020 notification was under CPC s.44A for decrees only). |
| NN-20 | **Signposting is honest.** Where a free or statutory forum is more appropriate (RBI Ombudsman, Insurance Ombudsman/Bima Bharosa, Consumer Commission/e-Jagriti, Lok Adalat, MSEFC/MSME ODR, DRT, Labour authorities, police), the platform says so, names the forum and its last date to act, and records a signposting event. Closure is blocked until signposting is recorded where the vertical's closure policy requires it. |
| NN-21 | **Every configurable thing is versioned and pinned.** A case is pinned at filing to the ruleset version, form-schema version, rules-of-procedure version and fee-schedule version in force; later changes never retroactively alter it. All configuration changes go through maker–checker approval with audit. |
| NN-22 | **Immutable audit.** Every material action writes an append-only, hash-chained audit event (prev_hash, row_hash, actor, tenant, case, action, before/after digest). Evidence objects are stored in S3 with Object Lock (compliance mode) and hashed into an `evidence_ledger`. |
| NN-23 | **Accessibility and language.** WCAG 2.2 AA; English and Hindi at launch with Marathi, Tamil, Telugu, Kannada, Bengali, Gujarati, Punjabi, Malayalam, Odia and Urdu enabled by configuration; legal templates in any language require human legal review before activation; bilingual parity tests for AI routes and clocks. |
| NN-24 | **Criminal matters are not undertaken.** Equator never conducts criminal proceedings or mediates an offence. Where the law permits compounding or settlement of the civil dimension (NI Act s.138/s.147; civil terms in matrimonial disputes with parallel criminal cases), only the civil/money dispute is mediated and the court alone decides on compounding, withdrawal or quashing. Hard exclusions with signposting: non-compoundable offences, sexual offences and POCSO, triple talaq (Muslim Women (Protection of Rights on Marriage) Act 2019), dowry offences, threats or violence, matters needing urgent police or court protection (Appendix K §3). |
| NN-25 | **AI drafting is party self-help, grounded and attributable.** The AI Pleadings Studio drafts only from the user's own uploaded material and a verified legal corpus; every factual sentence carries a source anchor (document, page, message time); no case law, statute or quotation may appear unless retrieved from the verified corpus and checked; unsupported statements are shown as gaps, never filled; the user approves each section and is the author; the same tool is available on identical terms to both sides; Equator staff never draft or edit a party's pleading; affidavits are sworn before an oath commissioner or notary (Appendix M). |
| NN-26 | **Publication only with consent.** No award, settlement or order is published unless every party has given informed, recorded, revocable consent (and the tribunal for awards), redaction to the applicable profile is complete and legal review is signed off; India-seated arbitral matters observe A&C Act s.42A; family, POSH, health, minors' and safety-flagged matters are never published in full (Appendix R §3). |
| NN-27 | **Representatives act only within their authority.** A representative (advocate or authorised person) acts under an e-signed Letter of Authority / Vakalatnama with defined scope (file, respond, attend, settle up to a limit, receive notices, sign); the party can view, narrow or revoke it at any time; settlement above the authority limit requires the party's own e-sign (Appendix S §4). |
| NN-28 | **Neutral grading, allocation and directory are merit- and process-based and published.** Grades A/B/C follow the published grading policy; allocation uses published eligibility filters, rotation, concentration caps and a capped Quality Index built from process metrics only; settlement rates, outcomes, who won, enterprise-client preference and training purchases never influence grade or allocation; there are no paid or featured listings (Appendix N). |
| NN-29 | **Honest pricing.** Total price including GST is shown before payment for consumers; no drip pricing, false urgency, forced continuity, basket sneaking, confirm-shaming or any other pattern listed in the CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023; cancellation takes no more steps than sign-up; recurring debits follow the RBI e-mandate framework (pre-debit notification; additional factor of authentication above ₹15,000) (Appendix O). |
| NN-30 | **One privacy control set for all applicable laws.** DPDP Act 2023 + Rules 2025, IT Act s.43A and SPDI Rules 2011, CERT-In Directions 2022, GDPR/UK GDPR, CCPA/CPRA, Singapore PDPA and UAE PDPL are met through a single configurable control set (lawful basis/consent per purpose, notices per jurisdiction, data-subject rights, cross-border transfer records, processor contracts, DPIAs, breach workflows) (Appendix Q). |
| NN-31 | **Card data never touches Equator.** All card and UPI collection uses the payment provider's hosted or standard checkout and tokenisation; no PAN, CVV or full card data is entered, stored, logged or transmitted by Equator systems (PCI DSS v4.0.1 SAQ A boundary) (Appendix Q §4). |
| NN-32 | **Originals are preserved; derived texts are labelled.** Every type copy (handwritten or screenshot transcription), OCR text and translation is stored as a derived version linked to the untouched original, shows confidence and uncertain passages, records the engine and the human verifier, and is marked "Type copy" / "Translation — for convenience" or "Certified translation" as applicable (Appendix L). |

---

## 4. Architecture (locked decisions)

### 4.1 Stack
- **Monorepo:** pnpm + Turborepo. TypeScript strict everywhere. Node.js LTS.
- **Web:** Next.js (latest stable, App Router, React Server Components), Tailwind CSS + Radix UI primitives + design tokens, TanStack Query, React Hook Form + Zod, next-intl. Every public marketing route is server-rendered or statically generated (a build check fails if an indexable route returns a client-only shell).
- **API:** NestJS (latest stable) as a **modular monolith** with strict module boundaries (one Nest module per bounded context, no cross-module DB access except via published service interfaces or events), extractable to services later. REST/JSON, OpenAPI 3.1 generated from code, versioned `/v1`.
- **Workflows:** **Temporal** (TypeScript SDK) for every long-running process (case lifecycle, clocks, notice campaigns, settlement instalments, award drafting with human signals, bulk intake). LLM calls run as Temporal activities with retries and timeouts; human-in-the-loop via Signals.
- **Data:** PostgreSQL 16+ (Amazon Aurora PostgreSQL) with **Row-Level Security for tenant isolation**, `pgvector` for retrieval, partitioning for high-volume tables; Redis (cache, rate limits, BullMQ for short jobs); OpenSearch (full-text search across cases/documents/directory, tenant-scoped indices); S3 (documents) with Object Lock buckets for evidence; KMS with per-tenant data keys (BYOK option for enterprise).
- **ORM/migrations:** Prisma or Drizzle (choose in ADR-0002; prefer Drizzle for SQL-first control and RLS-friendly raw SQL). Migrations are forward-only, reviewed, and include RLS policies and constraints.
- **Mobile:** React Native with **Expo** (latest SDK), Expo Router, EAS Build/Update, SecureStore, biometric unlock, push via Expo Push (FCM/APNs), offline queue with SQLite for drafts and uploads.
- **Auth:** OIDC-compliant identity built on a proven library/provider (Keycloak self-hosted in AWS Mumbai, or an equivalent with India residency — decide in ADR-0003). Mobile OTP (DLT SMS + WhatsApp OTP), email magic link, password + TOTP/WebAuthn passkeys for professionals, SSO (SAML/OIDC) for enterprise tenants, DigiLocker login for parties (via licensed provider). Short-lived JWT access tokens + rotating refresh tokens; step-up MFA for signing, payouts, configuration changes and sealed-data access.
- **Authorisation:** RBAC + ABAC policy engine (Cerbos or OPA — ADR-0004) evaluated server-side on every request: tenant match, case membership, role-in-case, confidentiality tier, purpose, time-bound grants, break-glass with justification and DPO notification.
- **Infra:** AWS ap-south-1 (Mumbai) primary, ap-south-2 (Hyderabad) DR; ECS Fargate (or EKS — ADR) behind ALB + CloudFront + AWS WAF; Terraform IaC; GitHub Actions CI/CD with environments (dev, staging, uat, prod); secrets in AWS Secrets Manager; OpenTelemetry traces/metrics/logs to Grafana stack; Sentry for errors; feature flags via OpenFeature + Unleash (self-hosted, India).
- **Video:** LiveKit (India region; self-host fallback) with separate rooms for joint session, each caucus, breakout and waiting room.
- **AI:** Claude models via **Amazon Bedrock India in-country inference** (primary) through an internal **AI Gateway** module (prompt registry, policy filters, PII redaction, eval hooks, cost metering, kill switch per feature/tenant); Sarvam for Indic STT/TTS/translation/OCR; provider-agnostic `LlmPort`.

### 4.2 Repository layout
```
equator/
  apps/
    web/            # Next.js: (public) site, (app) portals, (admin) consoles, (embed) widgets
    api/            # NestJS modular monolith
    worker/         # Temporal workers + BullMQ processors
    mobile/         # Expo app (party / neutral / enterprise-lite via role-based navigation)
    docs-portal/    # Developer portal (OpenAPI, sandbox keys) — Phase 9
  packages/
    domain/         # Shared types, enums, Zod schemas, state machines (pure TS)
    rules/          # Rules engine evaluators (routing, eligibility, clocks, fees) — pure, deterministic
    forms/          # Schema-driven form engine (renderer for web + mobile, validator for API)
    ui/             # Web component library (tokens, Radix-based)
    ui-native/      # Mobile component library (same tokens)
    design-tokens/  # JSON tokens → CSS vars / RN theme
    api-client/     # Generated typed client from OpenAPI
    i18n/           # Message catalogues, legal-term glossary, locale utilities
    ai/             # Prompt registry, guardrail policies, eval datasets (no case data)
    templates/      # Document templates (notices, MSA, awards, orders) with versioning
    seed/           # Demo/test data
    config/         # eslint, tsconfig, prettier, commitlint
  infra/terraform/  # AWS IaC
  docs/             # adr/, phases/, runbooks/, legal-register/, api/
```

### 4.3 Bounded contexts (NestJS modules)
`identity` · `tenancy` · `consent` · `kyc` · `directory` (people, organisations) · `neutrals` (empanelment, panels, availability, scorecards) · `cases` (case, parties, claims) · `intake` (filing, scrutiny, triage) · `forms` · `rules` (Ruleset Studio, legal rules register) · `routing` · `clocks` · `notices` (service of process) · `documents` (DMS, e-bundles, evidence ledger) · `proceedings` (negotiation, conciliation, mediation, arbitration, med-arb, expert determination) · `hearings` (scheduling, video, transcripts) · `outcomes` (settlements, awards, orders, maker–checker) · `esign` · `estamp` · `execution` (enforcement bundles, compliance tracking) · `billing` (tariffs, quotes, invoices, GST/TDS, refunds) · `payments` (gateway, splits, payouts) · `escrow` · `comms` (email/SMS/WhatsApp/push/voice orchestration, templates, consent-aware) · `voice` (AI voice agents) · `ai` (gateway, agents, evals) · `grm` (grievance SaaS) · `posh` (sealed) · `enterprise` (API keys, bulk, webhooks, SLAs, MIS) · `chambers` (Private ADR Chambers) · `academy` (LMS, certification) · `campus` · `cms` (website content, claims register) · `growth` (CRM, referrals, partners, analytics events) · `reporting` (dashboards, regulatory MIS) · `audit` · `notifications` (in-app) · `admin` (platform ops) · `integrations` (ports/adapters, webhooks inbox, provider routing).

### 4.4 Cross-cutting engineering patterns
- **Ports and adapters** for every vendor (`VOICE_PORT`, `TELEPHONY_PORT`, `MESSAGING_PORT`, `EMAIL_PORT`, `PUSH_PORT`, `ESIGN_PORT`, `ESTAMP_PORT`, `KYC_PORT`, `PAYMENTS_PORT`, `PAYOUT_PORT`, `ESCROW_PORT`, `TAX_INVOICE_PORT`, `VIDEO_PORT`, `TRANSCRIPTION_PORT`, `TRANSLATION_PORT`, `LLM_PORT`, `DOC_AI_PORT`, `FX_PORT`, `SANCTIONS_PORT`, `AA_PORT`, `POSTAL_PORT` (speed post booking/tracking/proof of delivery), `CRM_PORT`, `ANALYTICS_PORT`, `CONNECTOR_PORT` (government/ecosystem connectors: SMART ODR, ONDC IGM, MSME ODR, Sahamati, SCORES, LSA export), `CONSENT_MANAGER_PORT` (DPDP registered Consent Managers)). Provider chosen per tenant via a `provider_routing` table with circuit-breaker failover. Full interfaces: Appendix D.
- **Transactional outbox** for every external side effect; **idempotent webhook inbox** (`/webhooks/:provider`, signature verification, unique `(provider, event_id)`, async processing).
- **Idempotency keys** on all POST endpoints that create money, notices or cases.
- **Domain events** in CloudEvents format (`equator.case.filed.v1`, …) published from the outbox; consumers are idempotent. Catalogue in Appendix F.
- **Errors**: RFC 9457 problem+json with stable `code` values (catalogue in Appendix F).
- **Pagination**: cursor-based. **Filtering**: allow-listed fields. **Rate limits**: per tenant and per API key.
- **IDs**: UUIDv7 internally; human-readable case numbers `EQ/{VERT}/{CITY}/{YYYY}/{NNNNN}` (e.g., `EQ/FIN/JAI/2027/00042`) with QR verification URL; per-tenant prefixes for Private Chambers.
- **Time**: store UTC (`timestamptz`); display in user's timezone (default Asia/Kolkata); clocks computed with the Indian holiday calendar (configurable per state) where rules use working days.
- **Money**: `amount_minor BIGINT`, `currency CHAR(3)`; GST stored per line (CGST/SGST/IGST); TDS separately; FX snapshot table.
- **PII**: field-level encryption for Tier-High/Sealed fields; logs never contain PII (structured logging with redaction middleware); masked display by default (PAN `ABCDE****F`, phone `98****3210`).
- **Search**: OpenSearch per-tenant index aliases; sealed data never indexed.

---

## 5. Canonical domain model (summary; full DDL in Appendix F)

- **Tenant** (`kind`: `institution` | `chambers` | `enterprise` | `grm_client` | `university` | `academy`), branding, domains, locales, enabled verticals/mechanisms, provider routing, fee schedule set, rules-of-procedure set, data-region, BYOK key.
- **Person / Organisation / User / Membership** — a person may hold many roles across tenants; organisations carry KYB (CIN/LLPIN/GSTIN/PAN/Udyam/LEI) and authorised signatories with authority limits.
- **Case** — the dispute container: tenant, vertical, dispute_type (configurable taxonomy), sub_type, claim value (minor units + currency), confidentiality tier (`standard` | `high` | `sealed`), language(s), seat/venue (for arbitration), governing law, pinned versions (ruleset, forms, rules of procedure, fees), source (`self_filed` | `bulk` | `api` | `court_referral` | `grm_escalation` | `clause_auto` | `private_chambers` | `marketplace`), status (case-level machine), linked matters.
- **CaseParty** — role (`claimant`, `respondent`, `co_claimant`, `co_respondent`, `intervenor`, `guarantor`, `insurer`, `third_party_beneficiary`), representation (counsel mandates with scope), vulnerability flags (never shown to the other side), screening outcomes (sealed).
- **Claim / Counterclaim / Relief** — structured heads with amounts, interest basis, currency.
- **Proceeding** — an instance of a mechanism on a case (a case may have many in sequence: e.g., mediation → arbitration); own state machine per mechanism; panel/tribunal; rules version; clocks.
- **Session / Hearing** — joint, caucus, shuttle, async (text), documents-only determination; attendance; recording consent; minutes; transcripts (where lawful).
- **Order / Direction / Procedural Order**; **Offer** (negotiation, blind-bid, settlement proposals); **Settlement** (MSA, OTS, consent terms, F&F); **Award** (interim, partial, final, consent, additional, corrected); **Appeal** (internal appellate tier, when opted).
- **Notice / ServiceAttempt** — channel, address, provider receipts, hashes, deemed-service rules.
- **Document / Evidence / Bundle** — versioned files, OCR text, classification, exhibits numbering, privilege flags, hash, evidence-ledger entry.
- **Clock** — kind, trigger event, period, extension rules, owner, expiry (generated), alerts, breach state.
- **Neutral / Empanelment / Panel / Accreditation / Availability / Disclosure / Challenge / Appointment / Scorecard / Payout**.
- **FeeSchedule / TariffItem / Quote / Invoice / Payment / Refund / Payout / EscrowAccount / EscrowMilestone / FxRate**.
- **Communication / Template / ConsentRecord / Preference / CallRecord / Transcript**.
- **GrievanceTicket** (GRM) and **PoshComplaint** (sealed schema).
- **Ruleset / LegalRule / FormSchema / DocumentTemplate / ProcedureRules** (versioned, maker–checker).
- **AuditEvent / EvidenceLedger / AccessLog / BreakGlassEvent**.
- **Course / Cohort / Enrolment / Assessment / Certificate / CpdRecord** (academy), **Competition** (campus).
- **Lead / Account / Opportunity / Partner / Referral / ClaimsRegisterEntry / Page** (growth & CMS — physically separate from case data per NN-16).

### 5.1 Case-level state machine (canonical)
`draft → filed → under_scrutiny ⇄ deficient → accepted | signposted | rejected → awaiting_respondent → neutral_appointment → in_proceedings → outcome_drafted → outcome_executed (signed + stamped) → in_compliance (instalments/escrow milestones) → closed`, with side states `on_hold` (court stay, sensitivity pause with reason and clock policy), `withdrawn`, `lapsed` (mandate terminated, e.g., s.29A), `challenged` (s.34 / s.28 / appeal), `in_execution`. Each **proceeding** has its own machine (Appendix A) and the case state is derived from proceedings + compliance. Every transition has a guard, emits an event, writes audit, and may start/stop clocks.

### 5.2 Mechanism × vertical permission matrix (defaults; configurable within legal limits)

| Mechanism | FIN | COM | FAM | INS | WRK | INT |
|---|---|---|---|---|---|---|
| Negotiation (assisted/blind-bid) | ✔ | ✔ | ✔ (no blind-bid on maintenance for vulnerable party) | ✔ | ✔ | ✔ |
| Conciliation | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Mediation | ✔ | ✔ (incl. s.12A PIMS info) | ✔ primary | ✔ | ✔ | ✔ |
| Arbitration | ✔ (NN-03) | ✔ | Property/partition rights only (NN-06) | Quantum-only, commercial/B2B; never retail policyholder | Non-workman contracts only | ✔ |
| Med-arb / Arb-med / Arb-med-arb | ✔ | ✔ | Property only | B2B only | Non-workman only | ✔ |
| Expert determination | — | ✔ | — | ✔ (surveyor/assessor) | — | ✔ |
| Grievance (GRM) | ✔ | — | — | ✔ (insurer desk) | ✔ | — |
| POSH inquiry | — | — | — | — | ✔ (sealed) | — |
| Signposting | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

### 5.3 Med-arb / arb-med rules (binding)
- **Med-arb**: different neutral for the arbitration phase by default. In **statutory mode** the same neutral can never continue (Mediation Act s.17 bars a mediator from acting as arbitrator, with no party carve-out). In contractual mode, and for A&C Part III conciliation (s.80: "unless otherwise agreed by the parties"), the same neutral may continue as arbitrator **only** with fresh, informed, written (e-signed) consent of all parties executed **after** the mediation ends, plus a renewed s.12 disclosure. Caucus information from mediation is firewalled (sealed; never placed in the arbitral record).
- **Arb-med**: the tribunal finalises and **seals** the award (hash recorded, not disclosed) before mediation begins; if mediation settles, a consent award on agreed terms (A&C s.30) replaces it; if not, the sealed award is released.
- **Arb-med-arb / consent-award conversion**: a mediated settlement can be recorded as a consent award by an arbitral tribunal constituted for that purpose (primary enforcement route for `INT` while India has not ratified the Singapore Convention).

---

## 6. Customisability ("fully customizable" requirement)

Everything below is **data, not code**, editable in the **Ruleset Studio** (no-code admin) by authorised roles with maker–checker, preview, versioning, effective dating, tenant scoping and pinning:

dispute taxonomy (verticals → dispute types → sub-types) · intake forms (JSON-schema, conditional logic, multilingual labels) · routing/triage rule packs and signposting directory · mechanisms enabled per vertical and the ladder order/time-boxes · clocks (kind, period, working-day calendars, extension rules, alert thresholds) · rules of procedure (versioned rulebooks rendered publicly) · fee schedules (slabs, flat items, per-session, success fees where lawful, waivers, concessions, refunds, GST/TDS treatment, currencies) · neutral panels, accreditation types, grading rubrics, allocation policies (rotation, concentration caps, language/city/sector matching) · document templates (notices, letters, MSA, awards, orders; Handlebars-style with clause library) · notification journeys (channel order, timing, quiet hours, languages) · voice-agent scripts and policies · branding/white-label (logos, colours, domains, email sender, legal entity details) · roles and permission bundles per tenant (within platform guardrails) · SLA targets and enterprise MIS packs · dashboards (configurable widgets) · data retention schedules · feature flags.

Guardrails on customisation: tenants cannot disable NN rules, reduce statutory clocks, enable prohibited mechanism × vertical combinations, or remove mandatory disclosures. The rules engine validates every configuration change against the Legal Rules Register before activation.

---

## 7. Fees and currency (principles; full schedules in Appendix B)

- **Default currency INR** for all domestic matters. Every fee schedule is currency-aware; **`INT` matters and international enterprise contracts may be priced and invoiced in USD, EUR, GBP, SGD or AED** (configurable list), with an INR equivalent shown and an FX snapshot recorded.
- Fee components: registration/filing fee, administrative fee (slab or marginal ad valorem), neutral fee (per case, per session, per hour/day, or slab), hearing/session fees, adjournment fees, emergency-arbitrator fee, expedited surcharge, appeal-tier fee, execution pack, notice add-ons (speed post at actuals), stamp duty at actuals + procurement fee, interpretation/translation, escrow fee (bank tariff), subscription plans (Chambers, GRM, POSH, Enterprise API), academy fees.
- Who pays is a rule (claimant, respondent, equal split, enterprise-pays, deferred/cost-follows-event in award).
- Concessions: fee waivers for vulnerable parties, pro bono band, promo codes, partner discounts — rule-based with approval.
- Taxes: GST on services (18% default; IGST/CGST+SGST by place of supply; export of services under LUT for foreign parties where eligible; reverse charge for imported neutral services); TDS on neutral payouts under the Income-tax Act 2025 (in force 1 Apr 2026): professional fees s.393(1) Table Sl. 6(iii) (old s.194J; 10%, threshold ₹50,000), foreign neutral payouts s.393(2) Sl. 17 (old s.195) at rates in force or DTAA rate with Form 41 and TRC, remittance forms 145/146 (old 15CA/15CB). SAC 998215 (arbitration and conciliation services); arbitral-tribunal services to business entities are under reverse charge (Notification 13/2017-CT(Rate) Sl. 3) unless exempt under Notification 12/2017-CT(Rate) Sl. 45. Assess e-commerce-operator exposure (TDS s.393(1) Sl. 8(v) at 0.1%; GST-TCS under CGST s.52 at 0.5%) in the tax memo before go-live.
- Quotes are generated by the deterministic fee engine and shown before payment; every invoice is GST-compliant (e-invoice IRN where applicable).
- **Rate cards are fully customisable and approval-gated.** Every fee schedule (platform, vertical, enterprise contract, Private Chambers tenant, academy) is created and edited in the Ruleset Studio fee editor without code; it moves `draft → in_review → approved → published → superseded` through maker–checker, with the approver role and approval evidence (e.g., Board resolution reference) recorded. Nothing is quoted or invoiced from an unapproved schedule. Tenants may customise their own schedules within NN-18 limits.
- **Benchmarks** used for defaults: SEBI SMART ODR schedule (conciliation ₹5,400; arbitration ₹5,400–₹1,55,000+), A&C Act Fourth Schedule model fees (₹45,000 up to ₹5 lakh … ceiling ₹30 lakh per arbitrator), s.12A PIMS fees, competitor published fees (Sama), and ICC/SIAC/LCIA/HKIAC/MCIA scales for `INT`. **All default figures are marked "Subject to Board approval"** and are editable.

---

## 8. Integrations (defaults; ports in Appendix D)

| Need | Primary | Fallback |
|---|---|---|
| AI voice agents | ElevenLabs Agents (India data residency, Enterprise) over Exotel SIP | Sarvam voice agents; LiveKit Agents + Sarvam STT/TTS |
| Telephony | Exotel | Plivo |
| WhatsApp | Meta Cloud API via Gupshup (BSP) | Interakt/AiSensy/MSG91 |
| SMS/OTP | MSG91 (DLT) | Gupshup/Kaleyra |
| Email | AWS SES (ap-south-1) | Resend |
| Push | Expo Push (FCM/APNs) | Direct FCM/APNs |
| eSign | Leegality (Aadhaar eSign, DSC, virtual sign) | Digio / Setu (multi-ESP) / SignDesk |
| eStamp | Leegality BharatStamp | Digio / SignDesk–NeSL / SHCIL partner |
| KYC/KYB | Surepass (DigiLocker, PAN, bank a/c, GSTIN, MCA, Udyam, eCourts CNR) | IDfy / Signzy / HyperVerge |
| Payments | Razorpay (Orders, Payment Links, Route splits, Smart Collect, UPI AutoPay, Subscriptions) | Cashfree (Easy Split, Payouts) |
| International payments | Razorpay International / PayPal / Stripe (where available) | Bank wire with virtual account reference |
| Escrow | RazorpayX Escrow+ / Castler (bank escrow + trustee) | Direct payment with proof upload |
| Video | LiveKit Cloud (India region) | Self-hosted LiveKit / 100ms |
| STT/Translation | Sarvam (Saaras STT, Translate), Bhashini | AI4Bharat IndicTrans2 self-hosted |
| OCR/Doc AI | Sarvam Vision | Google Document AI / Azure Document Intelligence |
| LLM | Claude via Amazon Bedrock (India in-country inference) | Anthropic API direct |
| Sanctions screening (INT) | Commercial list provider (e.g., via Surepass/ComplyAdvantage-class API) | Manual list upload + fuzzy match |
| Account Aggregator | Lender tenant's FIU/TSP credentials | Manual statement upload + OCR |
| Government | MSME ODR/MSEFC, ONDC IGM, eCourts/NJDG lookups, Sahamati Vikalp, SMART ODR (flag) | Manual export packs |
| Group systems | Finbyx (LOS/LMS), Udofin (LSP), LawDocs (documents/eSign), BestComply (compliance) | Generic REST/SFTP |

---

## 9. AI layer (principles; specification in Appendix E)

Agents (all human-in-the-loop, all tenant-scoped, all logged with prompt/model/policy versions and retrieved source IDs):
`intake_assistant` (Dispute Explorer — classifies, collects facts, explains process and free forums, computes deterministic route/clock/fee via tools) · `document_extractor` (loan file, policy, claim, contract, salary slips → structured fields with confidence) · `case_summariser` (neutral brief, chronology, issues list with citations to bundle pages) · `drafting_assistant` (notices, procedural orders, settlement terms from agreed heads, award skeleton with evidence citations — neutral edits and signs) · `negotiation_facilitator` (neutral-toned messaging, option generation from party-provided parameters; never values) · `translation_agent` (with legal glossary; human review for templates) · `case_manager_copilot` (next-best-action, clock risks, missing documents, scheduling) · `voice_agent` (outbound/inbound calls: notice explanation, consent capture, slot booking, payment link, reminders; strict scripts and RBI/TRAI policies) · `grievance_responder` (GRM: draft response with regulatory checklist) · `qa_auditor` (checks drafts for prohibited terms, missing mandatory clauses, citation integrity) · `analytics_narrator` (enterprise MIS narratives without case-identifying data).

Release gates: routing 100%, clocks 100%, zero-tolerance guardrails 100% (one failure blocks the platform release), other suites ≥ 97%, bilingual parity, sensitive-data scan, red-team before every release.

---

## 10. Phase plan

| Phase | Title | Depends on | Core outputs |
|---|---|---|---|
| **P00** | Foundations & Platform Core | — | Monorepo, CI/CD, IaC, tenancy + RLS, audit chain, design system, Ruleset Studio skeleton, feature flags, observability |
| **P01** | Identity, Login, Onboarding & Consent | P00 | Login screens (all personas), OTP/passkeys/SSO/DigiLocker, onboarding wizards, KYC/KYB, consent ledger, profile & roles, mobile shell |
| **P02** | Case Core: Intake, Form Engine, Routing, Notices, DMS | P01 | Dispute Explorer v1, filing/response, scrutiny, routing & signposting, clocks service, notice engine, DMS/e-bundles, case-status tracker |
| **P03** | Neutrals: Directory, Marketplace, Empanelment & Allocation | P02 | Public directory, neutral onboarding/empanelment, disclosures/challenges, allocation engine, Defensibility evidence, scorecards |
| **P04** | Resolution Engines & Virtual Hearings | P03 | Negotiation, conciliation, mediation, arbitration, med-arb/arb-med, expert determination, appeal tier, LiveKit hearing rooms, orders |
| **P05** | Fees, Payments, Escrow & Multi-Currency | P02 | Fee engine & rate cards, quotes, Razorpay, splits, payouts, GST/TDS, refunds, escrow, FX, subscriptions |
| **P06** | Outcomes: Drafting, eSign, eStamp, Awards & Enforcement | P04, P05 | Settlement/award builders, maker–checker, eSign, eStamp, registration route, certified copies, BSA s.63 certificate, execution packs, compliance tracker |
| **P07** | Omnichannel Communications & AI Voice Agents | P02 | Journey orchestrator, WhatsApp/SMS/email/push, ElevenLabs/Sarvam voice agents, consent-aware quiet hours, call records |
| **P08** | Six Vertical Packs | P04–P07 | Builds `verticals/V1–V6` in sub-iterations P08a FIN · P08b COM · P08c FAM · P08d INS · P08e WRK · P08f INT: subtype taxonomies, suitability rules, intake forms per mechanism, dropdowns, workflows, calculators, templates, integrations, dashboards |
| **P09** | Enterprise, GRM SaaS & POSH SaaS | P08 | APIs/webhooks/SDK/sandbox, bulk intake, clause API, lender/insurer/employer consoles, GRM (4 variants), POSH IC SaaS, SEC connector (flag), government connectors |
| **P10** | Private ADR Chambers SaaS, ADR Academy & Campus | P03, P05 | Chambers tenant self-serve, LMS & certification, university partner portal, campus mediation cell, competitions |
| **P11** | Agentic AI Layer | P02–P09 | AI gateway hardening, agents catalogue, eval harness, red-team, AI governance console |
| **P12** | Mobile Apps — Parity & Release | P01–P11 | Feature parity, offline, biometric, deep links, store release |
| **P13** | Public Website, CMS, SEO & Growth Engine | P01, P05 | New website (risky content removed), CMS with claims register, programmatic SEO, free tools, CRM, referral/partner portal, analytics |
| **P14** | Hardening, Compliance & Go-Live | All | Security (VAPT, ASVS L2), DPDP, performance, DR drills, UAT, runbooks, launch checklist |

Mobile work starts in P01 (shell, auth, design tokens) and each phase from P02 adds its mobile screens where marked; P12 closes parity and ships to stores. P13 may run in parallel with P08–P11 by a separate squad.

---

## 11. Quality, security and performance standards

- **Security**: OWASP ASVS Level 2 (Level 3 for auth, payments, sealed data); OWASP API Top 10 tests; SAST (Semgrep/CodeQL), dependency scanning, container scanning (Trivy), IaC scanning (Checkov); secrets scanning; signed builds; CSP/HSTS; anti-automation on public forms; virus scanning of uploads (ClamAV) and file-type allow-lists; deep-fake/forgery signals on KYC media (provider liveness); quarterly VAPT by CERT-In empanelled auditor; CERT-In 6-hour incident reporting runbook; ISO 27001 and SOC 2 control mapping maintained in `docs/compliance`.
- **SLOs**: availability 99.9% (core APIs), 99.95% target for hearing rooms during scheduled sessions; p95 API < 300 ms for reads, < 800 ms for writes; web LCP < 2.5 s on 4G, CLS < 0.1, INP < 200 ms; mobile cold start < 2.5 s mid-range Android; statutory clocks fire before breach 100%.
- **DR**: RPO ≤ 15 min, RTO ≤ 2 h (cross-region Aurora global database, S3 CRR); quarterly DR drill.
- **Data retention** (configurable defaults): case records 8 years after closure (longer under legal hold); caucus notes 12 months after closure; AI interaction logs 12 months; audit 10 years; POSH per statute/policy (7 years default); call recordings ≥ 6 months (recovery) / per consent otherwise.
- **Testing**: Gherkin acceptance tests per FR in `tests/acceptance`; synthetic data only (never production data in non-prod); seeded scenarios for all six verticals; load tests (k6) for bulk intake (100,000 cases/batch), notice campaigns (1M messages/day), concurrent hearings (500 rooms).
- **Accessibility**: automated axe checks in CI + manual screen-reader scripts for critical journeys (file, respond, pay, sign, join hearing).
- **Documentation**: OpenAPI published; runbooks for every operational process; user guides per persona generated from the CMS.

## 12. Definition of Done (every story)
Code + migration + RLS policy + API + web UI + mobile UI (if in scope) + i18n keys (en, hi) + audit events + domain events + permissions + tests (unit/integration/e2e) + accessibility check + OpenAPI updated + seed data + docs + feature flag (if risky) + NN tests green + no PII in logs + reviewed ADR where a decision was made.

---

## 13. Source materials in the user's folder (consult, do not copy blindly)

`Equator Resolution Architecture/` contains the prior architecture set (EQR-00 … EQR-43), the institution-wide platform pack (`Platform (institution-wide)/` — schema_core.sql, AI safety framework, shared services), five vertical frameworks (Financial & Loan, Insurance, Commercial & Business, Workplace & HR, Marital) each with forms packs, rules & tariffs, calculators, technical architecture, OpenAPI/SQL, AI eval harnesses and risk registers; `Forms available on Website/`; `University Partnerships/`; `Equator Strategy/`. Where those sources conflict, **this master prompt and its appendices prevail**. Known conflicts already resolved here: (a) the institution-wide platform pack prevails over EQR on legal/AI-safety rules; (b) EQR prevails on tenancy and platform structure; (c) US-derived website forms (FINRA/Nevada/Vermont) are replaced by Indian equivalents; (d) Mediation Agreement clause 21 (mediator as witness) is deleted; (e) one canonical schema replaces the competing per-vertical schemas; (f) "People's Court" and "Equa.Law" branding is retired.

## 14. Glossary (short)
ADR — alternative dispute resolution · ODR — online dispute resolution · MSA — mediated settlement agreement · OTS — one-time settlement · PIMS — Pre-Institution Mediation and Settlement (Commercial Courts Act s.12A) · MSEFC — Micro and Small Enterprise Facilitation Council · GRO — grievance redressal officer · IC — Internal Committee (POSH) · SGRC — Students' Grievance Redressal Committee · RB-IOS — RBI Integrated Ombudsman Scheme · RE — regulated entity · FIU — Financial Information User (AA) · ICA — international commercial arbitration · NYC — New York Convention 1958 · QES — qualified electronic signature · LUT — letter of undertaking (GST export) · RLS — row-level security · HITL — human in the loop.

---

## 15. Document precedence and cross-file resolutions (binding)

**Order of precedence** when two documents in this pack disagree: (1) this master prompt → (2) Appendix G (Legal Rules Register) on any legal rule → (3) Appendix B on fee figures, fee semantics, FX staleness and tax treatment → (4) Appendix F on table/column names, types, events and error codes → (5) Appendix A on states, transitions and clocks → (6) the phase file being executed → (7) other appendices. The agent records every reconciliation it performs in `docs/adr/`.

Resolutions already decided (apply them; do not reopen):

| # | Topic | Resolution |
|---|---|---|
| X-01 | Request-context header | Use `Equator-Context` (tenant ID + acting role + acting case, signed by the gateway) as defined in P01. P12 references to `X-Tenant-Id` are superseded. Tenant is otherwise resolved from the host name (custom domain / sub-domain). |
| X-02 | Speed post | Implemented behind `POSTAL_PORT` (India Post / aggregator API where available; manual booking + tracking-number entry fallback). |
| X-03 | Mobile tabs | P12 governs mobile navigation; P01 tab placeholders are superseded. |
| X-04 | Clock ownership | Every statutory clock in every vertical must have an owner before closure (NN-04). This supersedes the older per-vertical `closure_policy` defaults for the clock-ownership column only. |
| X-05 | Voice agent inside mediation | The voice agent never relays substantive offers inside a mediation proceeding; inside mediation it handles logistics only (reminders, slot booking, joining help). Offer relay is limited to the pre-proceeding negotiation rung (e.g., FIN OTS offers authorised by the lender) where NN-12 recording applies. This removes the NN-11/NN-12 conflict. |
| X-06 | Lender programme neutral share | Appendix B figures prevail over the general neutral fee bands in P03 for lender-programme cases. |
| X-07 | FIN success fees | Borrowers never pay a success fee. Any outcome-linked component is enterprise-paid only, behind a flag defaulting OFF, and the neutral's fee is identical whether or not the case settles. INS has no success fee at all. |
| X-08 | Fee schedule statuses, FX staleness, rate-column types | Appendix B semantics prevail; P05 implementation aligns Appendix F DDL accordingly in its first migration. |
| X-09 | Partitioned tables | Primary keys on partitioned tables include the partition key (Appendix F §4.10 pattern), including `core.communications` and `audit.audit_events`. |
| X-10 | UUID function | Use `uuidv7()` (Postgres extension or app-generated); aliases in Appendix F are for migration convenience only. |
| X-11 | `core.evidence_ledger` | Appendix F's merged definition prevails over P00/P02 drafts. |
| X-12 | Family credential code | ECFM (Equator Certified Family Mediator). |
| X-13 | RB-IOS 2026 | Reserve Bank – Integrated Ombudsman Scheme, 2026, effective 1 Jul 2026: complainant first approaches the RE; if no reply in 30 days or dissatisfied, may complain to the RBI Ombudsman within 90 days (RB-IOS 2021 continues for complaints received before 1 Jul 2026); caps ₹30 lakh consequential loss and ₹3 lakh for harassment/time/expenses. Store as configurable `LR-RBI-*` rules (verified 20 Oct 2026), not hard-coded. |
| X-14 | Domain | `equatorresolution.in` is the primary domain; `.com` (if held) redirects. All public contacts use domain email addresses. |
| X-15 | Legal entity | The operating entity is **Equator Resolution Service Private Limited** (management decision, 19 Oct 2026). CIN, registered office, GSTIN, DPO and Grievance Officer are configuration values (`tenant.legal_entity`), rendered site-wide, to be supplied by the Company Secretary before P13 go-live. Equator ADR Institute (Academy) remains a separate entity. |
| X-16 | Mediation Act ss.27–28 in copy | Public copy states that these sections are not yet notified (NN-05) and switches automatically when the statutory-mode flag is turned ON. |
| X-17 | Length of phase files | Phase files are intentionally detailed; the agent may split a phase into sub-iterations (PXXa, PXXb) but must not drop requirements. |
| X-18 | Mechanism matrix vs source frameworks | Master §5.2 prevails (e.g., WRK arbitration only for non-workman contracts; FAM arbitration only for property/partition rights), even where older vertical frameworks were mediation-only. |
| X-19 | Precedence for vertical-specific rules | A vertical specification (V1–V6) prevails over phase files for its vertical's taxonomy, forms, dropdowns, clocks and workflow defaults; Appendix A still governs clock *mechanics*, Appendix B fee *figures*, Appendix F names/types/error codes, Appendix G legal-rule status. Where a vertical spec re-codes P08 identifiers, the P08 codes remain as `legacy_ref` aliases. |
| X-20 | Error codes | Appendix F canonical codes prevail; phase/vertical codes become sub-codes or aliases (e.g., `INS_RETAIL_ARBITRATION_BLOCKED` 422, `WRK_WORKMAN_ARBITRATION_BLOCKED` 422). New codes proposed in V1–V6 and K–T are added to Appendix F §F.10 in P00/P08 migrations. |
| X-21 | Authority to sign for a party | A Letter of Authority / Vakalatnama e-signed in the platform authorises filing, attendance, receipt of notices and negotiation within limits. **Signing a settlement or other instrument on behalf of an individual** may amount to a power of attorney, which cannot be executed by e-signature (IT Act 2000 s.1(4) and First Schedule; Powers-of-Attorney Act 1882) — it is enabled only after a stamped, notarised (and, where required, registered) physical power of attorney is verified; otherwise the party signs personally (NN-27; Appendix S) **[VERIFY — open: counsel confirmation]**. |
| X-22 | Representative tables | `core.party_representatives` (Appendix F) is canonical with the added columns in Appendix S; organisation-wide mandates use `core.standing_authorities`. |
| X-23 | Face-match / liveness thresholds | Accept ≥ 0.85, manual review 0.60–0.85, reject < 0.60 (Appendix S), configurable; vendor must hold ISO/IEC 30107-3 presentation-attack-detection evidence. |
| X-24 | Workforce identity | Staff and committee members authenticate only through the workforce identity provider with phishing-resistant MFA (passkey/security key) and device/IP policy; a staff member's personal (party) account is linked by the DPO and blocks them from any case in which they are personally involved. |
| X-25 | Quick exit | Goes to a configurable external neutral page (default google.co.in) and clears the view; overrides P02 FR-P02-01. |
| X-26 | Neutral grades and scores | Grades A/B/C are eligibility tiers under `grading_policy.v2` (Appendix N); the 0–100 rubric is the Assessment Score (pass gate and Quality Index input), not the grade. Public labels: Distinguished / Senior / Associate Neutral **[VERIFY — open: confusion risk with "Senior Advocate"]**. |
| X-27 | Concentration caps | Absolute cap (LR-ARB-007) applies to non-bulk matters; relative cap (default 40% per counterparty per 24 months) applies to bulk programmes; legal reviewer confirms before FIN bulk go-live. |
| X-28 | Small-number privacy | Neutral feedback aggregates are computed and shown to the neutral at n ≥ 5 responses; public profile ratings and all public transparency statistics cells require n ≥ 10. POSH and safety data are excluded entirely. |
| X-29 | Training neutrality | No fast-track, fee advantage or ranking for graduates of any one provider, including Equator ADR Institute; the training picker shows at least three recognised providers; the Institute referral card is OFF (`academy.institute_referral`) until the Institute corrects its public claims and confirms its operating entity (D2-17); any referral fee between Equator and the Institute is treated as a related-party transaction: Board approval under Companies Act 2013 s.188 (and shareholder approval where the s.188 thresholds are crossed), Audit Committee approval under s.177 only if Equator is required to have an Audit Committee, and s.184 disclosure of interest by interested directors **[CS to confirm]**. |
| X-30 | Prepaid credits | Wallet / plan credits may pay only Equator's own fees, never neutral or tenant fees, to stay outside RBI prepaid-payment-instrument authorisation; neutral and tenant fees use direct checkout with split settlement. |
| X-31 | Chambers marketplace take | By plan (Lite/Solo 15%, Pro 12%, Institution 10%) per Appendix O, superseding Appendix B §B.7.7's flat rate — subject to Board approval. |
| X-32 | AI provider fallback for case content | No automatic fallback to a different model provider for case content; if the primary in-country provider is unavailable, drafting is queued and a guided form is offered (Appendix M). |
| X-33 | OCR and translation residency | Default engines run in India (Sarvam; Claude vision via Bedrock India; AWS Textract ap-south-1); non-Indian-region engines sit behind `ocr.regional_cloud.enabled` = OFF. Language set = 28 (22 Eighth Schedule + 6 UN official, English included in the UN set) plus romanised mixed-language classes (Appendix L). |
| X-34 | Court-format profiles | Only the Supreme Court print standard (circular of 12 Mar 2020) and profiles verified against primary sources are seeded as `verified`; others are `unverified` and output is never labelled "court-ready" until verified (Appendix L). |
| X-35 | Publication | Opt-in by every party (and the tribunal for awards) in all tracks, including foreign-seated INT (NN-26); India-seated arbitral publication stays behind a flag until counsel rules on s.42A waiver; citation format `EQR/<YYYY>/AWD/<NNNN>`; public statistics per X-28 (Appendix R). |
| X-36 | Retention of outcomes | Awards, settlements and certified copies are retained for at least 13 years after issue (execution limitation of 12 years plus buffer), overriding the 8-year case default (Appendix Q). |
| X-37 | SPDI Rules | IT Act s.43A and the SPDI Rules 2011 are treated as continuing until the DPDP Act provision omitting s.43A commences (expected 13 May 2027) — build to both; correct LR-DPDP-001 accordingly **[VERIFY — open: commencement split of DPDP s.44 under G.S.R. 843(E)]**. |
| X-38 | INT expedited thresholds and fees | Expedited procedure default threshold USD 4m (configurable) with an opt-in Highly Expedited lane; INT administration-fee cap to be re-benchmarked against IIAC (USD 15k) before Board approval of the INT fee card. |
| X-39 | Emergency arbitrator fee | Appendix B figures prevail over illustrative figures in P04. |
| X-40 | Vertical-specific clocks resolved | FIN negotiation time-box 21 days (s.138 and SARFAESI ladders 14); FAM property mediation 90 + 60 days and 7-day reflection window before signing; INS "one month" = calendar month (General Clauses Act s.3(35)); WRK clock `wrk_wages_2wd`; Appendix F workplace size bands gain a 20-worker break (IR Code GRC threshold). |
| X-41 | Expert determination in FIN | Not offered in FIN (master §5.2); accounts disputes use a tribunal-appointed expert under A&C s.26. |
| X-42 | Brand and copy | Brand line "Resolve disputes, not relationships." (D2-20); master positioning line remains the home-page H1; `LegalService` schema off by default; search crawlers allowed, AI-training crawlers blocked on neutral profiles and published outcomes (Board to confirm) (Appendix P). |

---

## 16. Management decisions recorded (19 October 2026)

| # | Decision | Effect in the pack |
|---|---|---|
| M-01 | Rate cards must be customisable and subject to approval | §7 approval-gated fee schedules; Appendix B defaults remain "Subject to Board approval" |
| M-02 | Operating entity: **Equator Resolution Service Private Limited**; remaining particulars to be provided by the Company Secretary | X-15 |
| M-03 | Lender-arbitration defensibility position approved | NN-03 confirmed |
| M-04 | Mediation Act 2023 (statutory mode behind flag) and Singapore Convention (not ratified → consent-award conversion) positions approved | NN-05, NN-19 confirmed |
| M-05 | Equator will place automated/AI calls itself, using third-party telephony/CPaaS subscriptions | Implemented through the NN-12 design: DLT Principal Entity registration, lender-number (1600) mode for regulated-tenant matters, Equator's own declared A2P DID numbers behind a flag pending operator confirmation and counsel opinion, 1601 application when ODR/legal services are notified (research of 20 Oct 2026). P07; Appendix D |
| M-06 | Equator will conduct pre-suit (pre-litigation) mediation | **Live now:** voluntary contractual pre-suit mediation and A&C Act Part III conciliation (s.73 settlement has award status under s.74) in all verticals. **Mandatory s.12A pre-institution mediation (Commercial Courts Act 2015):** as in force, only the Legal Services Authority can conduct it under the PIMS Rules 2018 (G.S.R. 606(E), 3 Jul 2018: Form-1 application, Form-3 non-starter report by the Authority, Form-5 failure report). Equator becomes eligible only after four gates: (1) notification of the Mediation Act's Ninth Schedule substituting s.12A; (2) MCI regulations and Equator's recognition as a mediation service provider; (3) a Central Government notification authorising Equator under the new s.12A(2)(ii); (4) new rules replacing the PIMS Rules. Until then the product prepares the Form-1 pack for the Authority, runs voluntary mediation in parallel only where lawful, and never represents its report as satisfying s.12A; flag `com.s12a_equator_authorised` = OFF. |

---

## 17. v2 reading order and scope additions (21 October 2026)

1. Read `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (requirements R-01–R-40, decisions D2-01–D2-27, assumptions, counsel questions).
2. For any vertical work, read the vertical specification `verticals/V<n>_<CODE>.md` end to end before the phase file.
3. New binding appendices: **K** Dispute Explorer v2 & dispute-type plug-in framework · **L** Document management, court-format templates, type copies & translation · **M** AI Pleadings Studio · **N** Neutral governance, grades, QAP, code of conduct, complaints, ratings, allocation, training & Private ADR Chambers · **O** Revenue, plans, billing & settings · **P** Website copy deck & SEO/GEO content system · **Q** Privacy, security & certification readiness · **R** Case-status portal, publication, execution & registration · **S** Identity, separate login portals, onboarding integrations, representatives, dashboards & RBAC · **T** Benchmarks (competitors, institutions, training providers, Reliance Jio AI).
4. Every phase file ends with a **v2 addendum**; the addendum's requirements are part of that phase's scope and exit gate.
