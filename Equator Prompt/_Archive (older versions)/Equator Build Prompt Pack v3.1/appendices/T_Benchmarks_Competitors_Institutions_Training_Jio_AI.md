# Appendix T — Benchmarks: Competitors, International Institutions, Training & Accreditation Providers, and Reliance Jio AI Evaluation

> **Binding reference** for P03, P07, P10, P11 and P13, and the source for §15 ("Competitor notes") of each vertical specification V1–V6. Read with master §2 (competitive bar, D1–D12), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md` (R-06, R-08, R-33, R-34; D2-12, D2-13, D2-15, D2-17, D2-23), **Appendix H** (v1 competitor matrix, threats, pricing positioning, equatorresolution.in website corrections WC-01…, safe-claims library — **not repeated here**), Appendix N (governance, grades, QAP, code, complaints, allocation, directory, training), Appendix R (case status, publication, execution) and V6 (INT procedure tiers, AMA, institution notes).
>
> Research base: S3 Part C (claim-assistance and ODR competitors, 21 Oct 2026), S5 (international institutions, 21 Oct 2026), S6 (training, IMI QAP, grading, Equator ADR Institute review, 21 Oct 2026), S7 §1 (Reliance Jio / Reliance Intelligence AI, 21 Oct 2026), v1 R1 (competitors, 19 Oct 2026), RES_A2 Q13 (SEBI SMART ODR fees), RES_A4 Q14/Q15/Q27/Q36 (Bedrock India, ElevenLabs, WhatsApp, Exotel/Plivo/Sarvam). Facts are **as of 21 October 2026**.

---

## 0. Scope, evidence rules and reconciliations

### 0.1 What this appendix does

| # | Purpose | Consumer in the build |
|---|---|---|
| 1 | Benchmarks every named Indian ODR provider, claim-assistance player and global ODR reference on offering, user journey, pricing, strengths, weaknesses, and what Equator **adopts** or **avoids** | P13 comparison content (through the Claims Register, NN-17); V1–V6 §15; product backlog |
| 2 | Benchmarks twelve arbitral/mediation institutions on governance, panels, transparency, platforms, fees and publication, and maps each adopted practice to the appendix that implements it | Appendix N, Appendix R, V6; P03, P04, P06 |
| 3 | Benchmarks eleven training and accreditation providers, positions the separate **Equator ADR Institute**, and lists the Institute's required website corrections (D2-17) | Appendix N §9–§10; P03, P10, P13 |
| 4 | Evaluates Reliance Jio / Reliance Intelligence AI offerings as an **integration evaluation, not a commitment** (D2-23), with an RFP checklist, go/no-go gates and a vendor comparison | P07, P11 (phase addenda at the end) |
| 5 | Summarises how Equator v2 beats each competitor, with traceability to features and appendices | P13 copy; Board pack |

**Not in scope:** fee figures (Appendix B is authoritative, master §15 precedence 3); website corrections for equatorresolution.in (Appendix H §5, rows WC-xx); legal rules (Appendix G). This appendix never sets a price, a legal rule or a public claim; it records benchmarks and design consequences.

### 0.2 Evidence tags

| Tag | Meaning | May it appear in public copy? |
|---|---|---|
| **[V]** | Verified on a fetched primary or near-primary source (regulator, institution rules, company page) in the research pass named | Only via a Claims Register entry (NN-17) with URL and `verified_on` |
| **[V2]** | Verified from a secondary source (press, law-firm note) | Only as attributed ("as reported by …") and via the Claims Register |
| **[C]** | Company self-claim (marketing page, advertorial, press release) | Never as fact; may be paraphrased as "X states that …" with link |
| **[3P]** | Third-party aggregator (FitGap, Techjockey, Tracxn, GetLatka) | Never |
| **[K]** | Well-documented rule or practice, not re-fetched | Internal only until re-verified |
| **[U]** | Unverified, absent, or inference | Never; tracked in §6 |

**Comparative-advertising rule (binding, NN-17).** No page may name a competitor or make a comparative statement ("lower fees than…", "only platform that…") unless every factual element links to a `growth.benchmark_entries` row (§0.4) whose `evidence_tag ∈ {V, V2}` and whose `verified_on` is ≤ 90 days old. The CCPA Guidelines for Prevention of Misleading Advertisements and Endorsements for Misleading Advertisements 2022 and Consumer Protection Act 2019 s.2(28) apply to comparative claims **[K]**. Disparagement is prohibited: copy states Equator facts and verifiable competitor facts only, never characterisations ("expensive", "biased", "unsafe").

### 0.3 Reconciliations recorded for `docs/adr/` (do not reopen)

| # | Source statement | Resolution in this pack | Authority |
|---|---|---|---|
| RT-01 | S5 C1 recommends an "Equator Court of Dispute Resolution" | The body is the **Equator Institutional Committee** with sub-committees; the word "Court" is never used for any Equator body | D2-15; NN-17; master §1 |
| RT-02 | S5 C2 proposes grades G4–G1 | Grades are **A / B / C** (Distinguished / Principal / Associate Neutral — master X-26; "Senior" never used, v3.1 correction) per D2-12; S5's international overlay becomes the `END-INT-ARB` / `END-INT-MED` endorsements | D2-12; S6 §4.1 |
| RT-03 | R1 §2.2 and §8.3: "Presolv360 pricing not public" | **Superseded.** Presolv360 publishes model fees at presolv360.com/fees [V S3 C2] | S3 C2 (later pass) |
| RT-04 | R1 §2.4 / §8.1: SMART ODR unsuccessful conciliator fee ₹3,200 | **₹3,240** (Master Circular SEBI/HO/OIAE/OIAE_IAD-3/P/CIR/2023/195, 31 Jul 2023, updated 28 Dec 2023); total ₹3,840 | RES_A2 Q13; GLOBAL_CORRECTIONS §6 |
| RT-05 | R5 / H refer to ICC 2021 Rules and USD 3m expedited threshold | **ICC Arbitration Rules 2026 in force 1 Jun 2026**; Expedited Procedure opt-out threshold USD 4m for agreements on/after 1 Jun 2026; Highly Expedited (opt-in) 3-month award | S5 A3, D-1 |
| RT-06 | R1 §8.5 recommends charging lenders "mainly on outcome" | Borrowers never pay a success fee; any outcome-linked component is enterprise-paid, flag `fin_outcome_fee` OFF, neutral fee identical whether or not the case settles; INS has no success fee | X-07; NN-18 |
| RT-07 | S7 §1.4 RFP Q5 asks vendors for "CLI type (140/160-series per TRAI)" | Equator **never** uses 140-series or personal mobiles for case calls; lender-number mode uses the regulated tenant's **1600-series** number with written authorisation; Equator's own service calls use declared A2P DID ranges behind `voice.equator_service_number.enabled` OFF; **1601** applied for when legal/ODR services are notified | NN-12; M-05; GLOBAL_CORRECTIONS (M-05) |
| RT-08 | S5 A1 recommends publishing redacted challenge decisions under deemed consent | Adopted for publication of **challenge decisions** only, subject to counsel's s.42A view (02 §5 Q1); awards and settlements remain opt-in (NN-26) | NN-26; D2-10; Appendix R §3 |
| RT-09 | S6 §5 calls Grade C "freshers"; management brief names no 1–15-year band | Grade C covers entrants including professionals up to 15 years (assumption A-01) | 02 §4 A-01 |
| RT-10 | S6 §1: the Institute's site states IMI "accredited and certified" training and shows a "Qualifying Assessment Program" heading | IMI recognition held is a **Recognized Mediator Training Program (RMTP, formerly CMTP), announced 1 Jun 2024** — not a QAP; corrections in §3.4 | D2-17; S6 §1.4 |
| RT-11 (v3.0, 23 Oct 2026) | Appendix AF §AF.7.1 findings AFC-T-01…T-14 and review RVD E22 | Applied in place where they correct a fact against a dated source or align with a binding v3 rule: T-01–T-06, T-08–T-10, T-12–T-14 and the [C] tag for institution-reported statistics (§2.2). T-07 applied by D3-38 (C1–C20 numbering and stricter gate). T-11 (additional fee rows) is held in Appendix AF §AF.2.1 and is not duplicated here | Appendix AF §AF.0.2, §AF.7.1; NN-34; D3-38 |

### 0.4 Benchmark register (data, not prose)

Competitor and institution facts used by the website, sales decks and vertical pages are stored as data so they can expire and be re-verified.

```sql
CREATE TABLE growth.benchmark_entries (
  id                uuid PRIMARY KEY DEFAULT uuidv7(),
  subject_code      text NOT NULL,          -- e.g. 'cmp.presolv360', 'inst.siac', 'trn.imi', 'vnd.jio_haptik'
  subject_kind      text NOT NULL CHECK (subject_kind IN ('odr_competitor','claim_assist','global_odr','institution','training_provider','vendor')),
  attribute_code    text NOT NULL,          -- e.g. 'fee.mediation.registration', 'rules.in_force', 'feature.appeal_tier'
  value_text        text,
  value_minor       bigint,                 -- money in minor units
  currency          char(3),
  evidence_tag      text NOT NULL CHECK (evidence_tag IN ('V','V2','C','3P','K','U')),
  source_url        text,
  verified_on       date NOT NULL,
  verified_by       uuid NOT NULL REFERENCES core.users(id),
  next_reverify_due date GENERATED ALWAYS AS (verified_on + 90) STORED,
  public_use_allowed boolean GENERATED ALWAYS AS (evidence_tag IN ('V','V2')) STORED,
  superseded_by     uuid NULL REFERENCES growth.benchmark_entries(id),
  source_published_on date NULL,           -- v3.0 (AFC-T-14; R-66): publication date of the source, where known
  source_ref        text,                   -- v3.0: Appendix AF source ID (AF-Sxx)
  notes             text
);
```

Rules: (a) `growth.claims_register` rows of `claim_type = 'comparative'` must reference ≥ 1 `benchmark_entries.id` with `public_use_allowed = true` and `next_reverify_due ≥ today`, else the CMS linter blocks publication (error `CLAIM_BENCHMARK_STALE`); (b) a nightly job `growth.benchmark.reverify_due` opens a `core.tasks` item for the `growth_manager` 14 days before expiry; (c) event `equator.growth.benchmark_entry.expired.v1` unpublishes dependent page blocks; (d) the table lives in the `growth` schema (NN-16 physical separation) and never references case data. Seed rows: every [V]/[V2] fact in §1–§3 of this appendix.

---

## 1. Competitor benchmark v2

### 1.1 Indian ODR institutions and platforms

All seven below are SEBI SMART ODR empanelled ODR Institutions [V R1 §2.4, investor.sebi.gov.in]. Equator does not hold that status (master §1.2: `SEC` connector OFF), and SEBI's 23 Jul 2026 consultation paper (comments closed 13 Aug 2026; no final circular as of Oct 2026) proposes moving administration to market infrastructure institutions [V RES_A2 Q14; R1 §1 item 1], so no Equator revenue line depends on it.

#### 1.1.1 Jupitice Justice Technologies (Chandigarh, founded 2019)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | "Justice technology" suite: ODR interface; Contract Lifecycle Management; Litigation Management; Compliance Management; **Legal Notice Management System (LNMS)**; Digital Law Office; "Trust Layer" for AI-output QA (8 Jul 2026); **e-Stamp + e-Sign platform** launched 23 Jul 2026 (Offline, Operational and Financial e-stamping workflows; Stamp Wallet and NeSL model; Aadhaar eSign, DSC, bulk signing; targets banks, NBFCs, HFCs, insurers); "Saya" AI chatbot (Mar 2023); MSME "digital court" (May 2021). *v3.0 (23 Oct 2026, Appendix AF §AF.1):* products also include SARFAESI Management, Smart Debt Collection ERP, Litigation ERP (government), Bharat ODR and no-code Builders/Modules; a sponsored article of 1 Aug 2026 describes Stamp Inventory, operational and financial modes and NeSL but not a Stamp Wallet, so "Stamp Wallet" stays attributed to the 23 Jul 2026 source | [C] Bar & Bench 8 Jul 2026; webindia123 23 Jul 2026; entrepreneur.com; AF-S16, AF-S19, AF-S30 |
| Dispute catalogue | BFSI portfolios (banks, NBFCs, fintech, insurance), MSME and cross-border MSME disputes; full category list **partly captured** (v3.0, 23 Oct 2026): the marketplace site is fetchable and shows 10 consumer tiles and 8 relationship formats; sub-types are in-app only; only `www.jupitice.com` and `app.jupitice.com` refuse automated fetch — OI-T-01 (= OI-S3-01) is **partially closed** (AF-S01, AF-S10, AF-S17). Equator's own expansion catalogue is Appendix K §7 | [V2]/[U] |
| Marketplace | Global ADR-professionals "Marketplace" (2021); third-party report of a tiered take-rate on practitioner fees (18% ≤ USD 20k; 15% USD 20,001–100k; 14% > USD 100k) plus 3% client processing fee; "free for resolution seekers". *v3.0 caveats (Appendix AF AFC-T-02):* AffairsCloud supports only the 2021 launch, not the rates; FitGap cites no source and its ₹/USD band edges do not match; a commission is confirmed to exist by the escrow terms; "free for resolution seekers" is not confirmed (buyer-side "delivery platform subscription"); never public | Rates [3P] FitGap only (unsourced); launch [V2] affairscloud 18 May 2021; AF-S10, AF-S26, AF-S29 |
| User journey | Enterprise-led (BFSI portfolio upload → automated notices via LNMS → hearings → award/agreement execution); individual entry via marketplace | [C] |
| Pricing | No public enterprise price list; take-rate model only from third-party source | [3P] |
| Scale claims | 1.16 lakh ODR cases resolved, 80,000+ hearings, 3,000+ neutrals, 22 clients (16 Sep 2026, advertorial); group-wide 180+ institutions. v3.0: the marketplace site also claims 4,000+ / 5,000+ providers, 10 Mn users and 83,000 hearings; "22 clients" conflicts with "180+ institutions" (Appendix AF §AF.1.5) | [C], conflicting |
| Strengths | Widest bundle in BFSI (ODR + notices + e-stamp/e-sign + CLM); API-first e-stamp; NeSL model; SEBI ODRI; Lok Adalat-as-a-service positioning | [C] |
| Weaknesses | Metrics largely from paid advertorials; no public reviews on Gartner; opaque take-rate pricing; "meta-platform" breadth dilutes ODR focus; earlier claims "awards valid in 166–171 countries" unverified; no confirmed settlement-money collection loop. v3.0 additions (Appendix AF §AF.1.7, W1, W3–W10, W12): login-gated directory; undisclosed paid status of featured profiles; contradictory reviews; freelance-style escrow; discretionary delisting and an income test; auto-assignment; legal-document defects; pre-DPDP privacy terms; site hygiene; desktop-only per company | [3P]/[U]; [C] |
| **Equator adopts** | Plug-in dispute catalogue model (Appendix K §6) so new dispute types ship as configuration; native e-stamp + e-sign inside the outcome flow (P06; NN-09); notice management with delivery evidence (P07) | — |
| **Equator avoids** | Opaque take-rate on neutral fees (Equator publishes fee cards, D7, NN-29); paid-advertorial metrics (NN-17 Claims Register); paid placement on the institutional directory or anything read by appointment — on the Private Practice Marketplace only labelled, capped sponsored slots behind `marketplace.paid_placement` OFF (NN-34; D3-01; v3.0 supersedes "paid or featured neutral listings in any marketplace") | — |

#### 1.1.2 Presolv360 (Edgecraft Solutions Pvt Ltd, Mumbai)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | Institutional arbitration, mediation, conciliation, negotiation; dispute types: money recovery, property, insurance, employment, other civil; small-value lending; execution support; "Presolv for All" free tier for eligible low-income parties; Indian Sign Language interpreter option | [V] presolv360.com |
| Published fees | **Domestic arbitration (model):** ₹5,000 (claim ≤ ₹50,000); ₹10,000 (≤ ₹1 lakh); ₹20,000 (≤ ₹5 lakh); ₹20,000 + 3% of excess over ₹5 lakh, rising by slab to ₹7.8 lakh + 0.5% of excess over ₹10 crore (to ₹20 crore); cap ₹30 lakh. **MSME arbitration** from ₹2,750 (≤ ₹5 lakh). **Cross-border** from USD 500. **Mediation:** registration ₹4,500 + administration ₹5,000 per session + mediator fee as agreed (MSME ₹2,000 + ₹2,500; international USD 125 + USD 175). Fees non-refundable; claimant pays arbitration fees | [V] presolv360.com/fees (S3 C2) |
| User journey | Login/register → business enquiry or case filing → notices → online sessions → settlement/award with e-signature | [V]/[3P] |
| Capital and credibility | Series A USD 4.7m led by Elevation Capital (2025); advisory council: former CJI U.U. Lalit, Justice B.N. Srikrishna, Justice K. Kannan; Smart Resolution Summit (Aug 2026, Attorney General keynote); open-source "AI Library for Arbitration" | [V] inc42; LiveLaw |
| Strengths | Published fee card (now one of few); judicial advisory council; capital; MSME and international bands; accessibility (ISL) | — |
| Weaknesses | **Named by the Bombay High Court** (*Radiance Galore v Yes Bank*, 17 Jul 2025) and asked to explain safeguards against lender-triggered unilateral appointment; non-refundable fees; no mobile app per directory listing; site counters render placeholders | [V] Bar & Bench; [3P] |
| **Equator adopts** | Published, slabbed fee card with MSME and international bands (Appendix B; D7); free tier for vulnerable parties (master §7 concessions); ISL/sign-language interpretation in hearing booking (NN-23) | — |
| **Equator avoids** | Blanket non-refundability (Appendix B refund policies; Consumer Protection Act 2019 s.2(46) unfair contract risk [K]); any appointment path a lender can trigger alone (NN-03, D1) | — |

#### 1.1.3 Sama (Odrways Solutions Pvt Ltd, Bengaluru)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | Mediation (family & matrimonial; property & real estate; payment & banking; insurance & employment; commercial & business; co-founder) and arbitration (loan recovery & banking; commercial & contractual; partnership & employment; property money claims; credit-card defaults); hybrid "Suljhao Space"; **builder of the SEBI SMART ODR portal** (Aug 2023) and of SLSA online Lok Adalats (Delhi, Rajasthan, Bihar, Maharashtra, Gujarat) | [V] sama.live |
| User journey | Optional consultation → registration → notices by call, email, SMS, WhatsApp, Speed Post → **15-day respondent consent window** (nothing beyond registration charged if no response) → mediation (~30 days) or sole-arbitrator arbitration (≤ 180 days) → execution packet | [V] sama.live/faqs |
| Published fees | Consultation ₹2,500 / 60 min (credited); mediation with no defined claim ₹10,000–₹1,00,000 per session (≤ 3 h); staged registration → consent → settlement fees; arbitration fee upfront + stamp duty + ₹40 per stamp procurement; extra physical notice ₹100 per address; execution packet ₹500; **unpaid settlement fee bars the user from future matters**; 3-year data retention | [V] |
| Scale claims | 2 crore+ cases handled; 34 lakh+ resolved; 45-day average (dominated by Lok Adalat traffic-challan volumes) | [C] |
| Strengths | Volume incumbency; government-platform credentials; multichannel notices incl. Speed Post; transparent partial price points; Indian Mediation Week community | — |
| Weaknesses | Headline volumes not comparable to contested matters; staged and settlement-linked fees; future-matter bar for unpaid fees; low equity funding relative to scale | Analysis |
| **Equator adopts** | Respondent window with no charge if the respondent does not engage (Appendix B stage refunds); execution pack as a one-time product (Appendix O; Appendix R §4); Speed Post via `POSTAL_PORT` | — |
| **Equator avoids** | Settlement-contingent fees borne by consumers (X-07, NN-18); barring users from future matters for unpaid fees (dark-pattern and access-to-justice risk; NN-29); 3-year retention below Equator's 8-year case retention (master §11) | — |

#### 1.1.4 CORD — Centre for Online Resolution of Disputes (resolveoncord.com)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | Arbitration, mediation, negotiation; clause drafting; **dispute system design** (grievance infrastructure for organisations); training and certification; sectors: banking/NBFC (bulk NBFC, co-lending), tenancy/housing society, workplace, insurance, e-commerce, MSME, consumer, healthcare, securities (SMART ODR for NSE, NCDEX) | [V] |
| **CORD Rules 2.0 (effective 4 Sep 2026)** | AI-governance framework embedded in the Rules; tiered fees; **opt-in in-built appellate mechanism**; **Appointments Council**; emergency arbitration; published stage timelines. Fee amounts not published | [V] |
| User journey | "Start a case" / "Generate clause" → free consultation → upload → notices → award/settlement → opt-in appeal | [V] |
| Claims | ₹500 crore+ dispute value administered; ~75-day average; 25 languages; "0 awards set aside" | [C] |
| Strengths | Closest to an institution-grade, rules-first model; AI governance in the rulebook; appeal tier; credible leadership (CEO Deepika Kinhal) | — |
| Weaknesses | Fee amounts not public despite "transparent" positioning; lender tooling (bulk notices, e-stamp, settlement collection) not shown; logo labels inconsistent on site | [V]/[C] |
| **Equator adopts** | Published stage timelines and Service Charter (Appendix N; S5 R15); AI Governance Rule in Equator Rules (D3; P13 FR-P13-07); optional internal appeal tier (D4); Appointments Committee (D2-15); own published "awards set aside" count (D12) | — |
| **Equator avoids** | "Transparent" claims without published figures (NN-17, NN-29) | — |

#### 1.1.5 Webnyay (webnyay.ai, New Delhi)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | ODR (online conciliation and arbitration); **Compliance & Grievance Redressal** (smart forms, omni-channel intake); Webnyay AI Suite; Docs by Webnyay; **Arbitral Institutions** secretariat offering; AIARB.IN; Draft-Your-Self pleadings; e-bundles; AI-powered neutral selection using "past performance" and "neutrality metrics" | [V] |
| Credentials | ISO 27001:2022; Bombay HC and Bombay Chamber mediation empanelment; RBIH Swanari TechSprint shortlist; IBA-recommended TSP; NLU Delhi and NALSAR partnerships; "sole IFSCA-authorised ODR provider in GIFT City" claim unverified | [C]/[U] |
| Pricing | Not public ("Book a demo") | [V] |
| Strengths | Grievance SaaS with BFSI logos (Bajaj Finance, Shriram, Muthoot, TVS Credit, Kotak); certified ISMS; institution-as-a-service | [C] |
| Weaknesses | Small team (~27 staff, 3P estimate) for broad scope; no regulator-clock-to-ODR bridge shown; AI neutral selection on "past performance" risks outcome-based selection; no price card | [3P]/Analysis |
| **Equator adopts** | Self-help drafting tool — but grounded, attributable and available to both sides on identical terms (Appendix M; NN-25); grievance SaaS (D5) with regulator clocks; ISO/IEC 27001:2022 certification path (Appendix Q) | — |
| **Equator avoids** | Any AI or score that uses outcomes or "performance" in neutral selection (NN-28, D2-13); ISO claims before certification (NN-17) | — |

#### 1.1.6 CADRE (Erdac Solutions Pvt Ltd, Bengaluru)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | "India's Simplest ODR platform": negotiation, mediation, arbitration; debt recovery and rental (historic NestAway); email/WhatsApp updates; optional video | [C]/[V dated] |
| Funding | ~USD 400K pre-seed; USD 200K strategic round led by Share Samadhan (Apr 2025); IIM-B NSRCEL | [3P]/[V] |
| Pricing | Not public | [U] |
| Strengths | Simplicity; WhatsApp-first updates; investor-dispute adjacency through Share Samadhan | — |
| Weaknesses | Thin public product evidence; site body not retrievable; no published rules or fees seen | [U] |
| **Equator adopts** | WhatsApp-first respondent engagement with consent (P07; D9) | — |
| **Equator avoids** | Opaque process and fee disclosure | — |

#### 1.1.7 JustAct (2019)

| Dimension | Benchmark | Tag |
|---|---|---|
| Offering | ODR operations partner; **"NPAC — powered by JustAct"** (Nani Palkhivala Arbitration Centre, 16 Apr 2026): hybrid/online hearings, AI transcription, electronic evidence management, AES-256 video, e-bundling, 2FA, "JustAct Première" case management | [V] LiveLaw |
| Pricing / metrics | Not public | [U] |
| Strengths | Proven **institution-as-a-service** model with a legacy arbitral centre | — |
| Weaknesses | Little public product depth beyond the NPAC tie-up | [U] |
| **Equator adopts** | Private ADR Chambers / institution-as-a-service for chambers, bar associations, universities (D8; Appendix N §8; P10) | — |
| **Equator avoids** | Recording mediation sessions by default (Equator: NN-11 — no mediation recording; arbitration recording only with all-party and tribunal consent) | — |

#### 1.1.8 Rails Equator integrates rather than competes with

SEBI SMART ODR (fee schedule applied exactly when `SEC` is ON, NN-18; conciliator ₹4,800 settled / ₹3,240 not settled + ODRI ₹600 — RT-04), Sahamati inter-member dispute framework (AA-network disputes; empanelment window closed), MSME ODR/MSEFC, ONDC IGM, NPCI UDIR. Treatment and connectors: Appendix H §1.1–§1.2, master D10, P09 `CONNECTOR_PORT`.

### 1.2 Claim-assistance players (INS front door)

These are not neutral institutions; they act for the policyholder or within a broker relationship. Equator competes with them only at the **front door** (who the policyholder turns to after a rejection) and must not copy their fee model (NN-18; X-07; D2-18).

| Dimension | **ClaimBuddy** (claimbuddy.in) | **Insurance Samadhan** (insurancesamadhan.in) | **Policybazaar** claim support | **InsuranceDekho** claim support |
|---|---|---|---|---|
| Legal form / licence | Private company, Delhi NCR, founded 2020; no IRDAI licence found [V Inc42; U] | Grievance-redressal company, founded 2018 [V2] | Policybazaar Insurance Brokers Pvt Ltd, IRDAI-registered broker [K] | IRDAI direct broker; footer licence No. 505 (D2C Insurance Broking Pvt Ltd); EDGE terms name Girnar Insurance Broker Pvt Ltd (entity inconsistency on page) [V] |
| Offering | B2C claim help for patients + B2B claims digitisation for hospitals (250+ partner hospitals, Apr 2024) [V] | Complaint drafting with "techno-legal" articulation, insurer liaison, escalation to Ombudsman/consumer forum; "Know Your Policy" tool [V/V2] | Claim Samadhaan Diwas in-person settlement days with insurers (since 2022); on-ground claim teams; **Claim Kavach** motor (Dec 2025): dedicated manager, 24×7 helpline, escalation team [V2] | "EDGE" motor claim assistance: insurer and garage liaison, cashless facilitation, free pickup, 6-month paint warranty; reporting 10:00–19:00 [V] |
| User journey | App/web or hospital desk → hospital-side claim file → claim settled [U on detail] | Web form + call-back → screening → company writes to insurer → escalation → insurer pays claimant → fee invoiced [V2] | Inside broker servicing → claims manager → escalation → settlement day [V2] | Helpline/email → garage/surveyor coordination [V] |
| Pricing | Not retrievable (site blocks fetch) [U] | **₹999 registration incl. GST + 20% + GST success fee** (22% + GST at legal level; withdrawal 10%/15% + GST) [V] (insurancesamadhan.com, read 22 Oct 2026; OI-T-02 closed for Insurance Samadhan) | Free to customer (broker remuneration) [K] | No fee stated [V] |
| Scale claims | 35,000+ patients assisted [V Inc42] | 20,000+ grievances / ₹220 crore+ since 2019 (Sep 2025) [V2] | 2,00,000+ customers assisted (Sep 2025) [V2] | 1,45,000+ claims served [C] |
| Strengths | Hospital desk integration (where cashless claims actually fail) | Proven recoveries in mis-selling; ~90% resolved at insurer level [V2 BT 2020] | Settlement days resolve stuck claims quickly | Garage network |
| Weaknesses / exposure | Unregistered-intermediary question under Insurance Act s.2(10B)/s.42D [U] | Same intermediary question; practice-of-law risk for drafting (*BCI v A.K. Balaji* (2018) [K]); 9% fee large against a free Ombudsman route | **IRDAI ₹5 crore penalty, order 4 Aug 2025** (unsupported "Top/Best" labels, outsourcing fees, record-keeping, premium remittance delays) [V2] | Disclaimers shift garage-delay risk to customer [V] |
| **Equator adopts** | Hospital/TPA read-only evidence request (V4; PI-INS-04; PI-CMP-04) | Representation-letter generator and policy-wording reader as **self-help** (V4; Appendix M) | White-label insurer "Settlement Days" with batch scheduling (V4; PI-INS-10) | Post-rejection motor disputes as the INS wedge, not first-notice handling |
| **Equator avoids** | Referral fees from hospitals or insurers for steering cases (NN-16) | Percentage-of-claim fees in retail INS (NN-18; X-07); acting as the policyholder's advocate while also offering a neutral (02 §5 Q10) | "Top/Best" labels without data (NN-17; PI-CMP-06) | Unilateral changeable terms (NN-29) |

**Free-route-first rule (binding for INS retail, from V4 and PI-INS-01).** Where the Insurance Ombudsman engine returns eligible, Equator shows "Free: Insurance Ombudsman" first, then Bima Bharosa, then Equator's flat-fee options. This is the single most important differentiator against claim-assistance success-fee models.

### 1.3 Global ODR references

| Dimension | **AAA-ICDR** (US) | **Immediation** (Australia) | **Modria / Tyler Technologies** (US) | **CourtCorrect** (UK) |
|---|---|---|---|---|
| Offering | Largest US institution; ICDR International Rules (2021); acquired ODR.com's parent (May 2024); **AI Arbitrator** announced 17 Sep 2025, live 3 Nov 2025, built with QuantumBlack (McKinsey), trained on 1,500+ construction awards, for **two-party, documents-only construction cases**; expansion planned 2026 [V] | Cloud ODR for commercial and insurance claims (subrogation, insurer–reinsurer, contribution); panel of former judges; fixed fees; decision within 30 days (2019 launch) [V dated] | Court-embedded ODR: **diagnosis → asynchronous negotiation → mediation → evaluative outcome** for landlord–tenant, family, debt, small civil; integrates with Tyler court CMS [V] | AI complaint handling for financial services: evidence analysis, similar-case retrieval, out-of-the-box regulator checks [V 2023] |
| User journey | Briefs → AI summary → **parties validate the summary** → AI draft with reasons → human arbitrator revises, issues, signs; mutual opt-in [V Mayer Brown; KJK May 2026] | Online filing → fixed-fee determination | Self-diagnosis → negotiate without a neutral → mediator if needed | Consumer complaint → AI analysis → firm response |
| Pricing | 2026 International Fee Schedule (flat filing fees by band) [U not fetched]; AI fee [U] | "Fixed fees" (amounts [U]) | Licence to courts [U] | SaaS [U] |
| Strengths | Governance model for AI with human control; published AI standards | Insurance B2B niche | > two-thirds of disputes resolved where both parties engaged (Denton County JP Court) [V] | Regulator-mapped checks |
| Weaknesses | AI lane limited to one case type; enforceability abroad untested | Current status unverified [U] | Court-only distribution | **Suggests outcomes** — not permissible for Equator |
| **Equator adopts** | Party-validation screen and AI-drafts-human-signs (D3; P11; Appendix E; AI lane flag `intl.ai_docs_only_lane` OFF pending counsel, V6) | Insurance B2B and surveyor expert determination (D11; V4) | Async negotiation before any neutral (P04 negotiation engine; Appendix K §5 pre-litigation) | GRM `grievance_responder` with regulator checklist (D5; P09) |
| **Equator avoids** | Autonomous AI determinations; AI as "arbitrator" (A&C Act s.31 — award made by the arbitral tribunal; NN-01) | — | Evaluative outcomes by software | AI outcome suggestion or valuation (NN-01 GX-2, GX-3) |

### 1.4 Published price points (benchmark only — Equator figures live in Appendix B)

| Service | Presolv360 [V] | Sama [V] | SEBI SMART ODR [V] | Insurance Samadhan [V2, 2020] | Jupitice [3P] | Equator |
|---|---|---|---|---|---|---|
| Consultation / pre-filing call | — | ₹2,500 / 60 min, credited | Free pre-conciliation | ₹500 registration per family member | — | Appendix B (live site: ₹1,000 / 30 min, credited — H §4) |
| Mediation / conciliation (low value) | ₹4,500 registration + ₹5,000 admin/session + mediator fee | ₹10,000–₹1,00,000 per session (no defined claim) | ₹4,800 + ₹600 if settled; ₹3,240 + ₹600 if not | 9% success fee | Take-rate 14–18% on practitioner fee + 3% ([3P], unsourced; internal only — AF-S29) | Appendix B cards (flat, slabbed, GST shown — NN-29) |
| Arbitration ≤ ₹1 lakh | ₹10,000 (₹5,000 ≤ ₹50k) | Upfront (amount not public) + stamp + ₹40/stamp | ₹4,800 + ₹600 | n/a | as above | Appendix B (FIN documents-only lane) |
| Arbitration ₹5 lakh | ₹20,000 | — | ₹8,000 + ₹1,000 | n/a | — | Appendix B |
| Cap | ₹30 lakh | — | max(1% of claim, ₹1,20,000) + ₹35,000 | — | — | Fourth Schedule ceiling ₹30 lakh per arbitrator as reference (*ONGC v Afcons*, SC 30 Aug 2022) |
| Execution pack | Execution support (price not seen) | ₹500 | MII deposit mechanism | — | — | Appendix O one-time product |
| Refunds | Non-refundable | Staged | Deposits returned per award | — | — | Stage-based refund policies (Appendix B) |

Reading: SMART ODR remains the regulated floor for low-value arbitration; Presolv360 is now the most complete private published card. Equator's D7 claim must be framed as "published, calculator-driven, GST-inclusive quotes with stage refunds" — **not** as "the only published fee card" (that would now be false; NN-17).

### 1.5 User journeys compared (entry → outcome)

| Step | Presolv360 | Sama | CORD | Jupitice | Insurance Samadhan | **Equator v2** (pointer) |
|---|---|---|---|---|---|---|
| Entry | Login / enquiry | Optional paid consultation | Start a case / generate clause | Enterprise portfolio or marketplace | Web form + call-back | **No-login Dispute Explorer v2**; criminal and non-arbitrable exclusions; free forums and last dates shown first (Appendix K §1–§3; NN-20, NN-24) |
| Screening | — | Consultant recommends | Free consultation | Enterprise rules | Selective | Deterministic eligibility and suitability engine (Appendix K §4; NN-01, NN-02) |
| Identity | Account | Account | Account | Enterprise | Form | Separate persona portals; DigiLocker, OVSE Aadhaar, PAN, MCA (Appendix S §2–§3; D2-05, D2-06) |
| Documents | Upload | Agreement upload | Upload | DMS | Policy, rejection letter | DMS with party-controlled sharing, type copies, translation, BSA s.63 certificate (Appendix L; NN-10, NN-32) |
| Pleadings | Party/counsel | Party/counsel | Party/counsel | — | Company drafts for client | **AI Pleadings Studio** — grounded self-help, same terms both sides (Appendix M; NN-25) |
| Respondent contact | Notices | Call, email, SMS, WhatsApp, Speed Post; 15-day window | Notices | LNMS automated | Company writes to insurer | DLT/TCCCPR-compliant omnichannel + AI voice with disclosure (P07; NN-12) |
| Representation | Counsel | Counsel | Counsel | — | The company | Scoped, revocable Letter of Authority / Vakalatnama (Appendix S §4; NN-27) |
| Neutral | Platform-matched | Platform | Appointments Council | Marketplace | n/a | Published allocation: hard filters → rotation → capped Quality Index; no outcome metrics (Appendix N §6; NN-03, NN-28) |
| Fee point | Registration + per session; non-refundable | Staged; settlement fee | Tiered | Take-rate | Success fee | Quote before payment, GST-inclusive, stage refunds (Appendix B, O; NN-29) |
| Outcome | Settlement / award | Award; execution packet | Award; opt-in appeal | Award; e-stamp | Insurer pays | Settlement / s.73–74 / consent award; e-stamp + e-sign; registration route (P06; Appendix R §4; NN-08, NN-09) |
| Status visibility | Dashboard | — | — | Dashboards | Calls | Supreme-Court-style case status: papers, dates, orders, parties (Appendix R §1–§2) |
| Publication | — | — | — | — | — | Consent-only publication with redaction (Appendix R §3; NN-26) |

### 1.6 Feature comparison matrix (v2)

Legend: **●** confirmed in source · **◐** claimed, partial or third-party · **○** not found in sources (≠ absent) · **✖** source says not offered · **n/a** not applicable. Equator column gives the owning appendix/phase; a feature counts for Equator only when its acceptance tests pass (no public claim before then — NN-17). Competitor marks carry forward Appendix H §1.1 (19 Oct 2026) and are updated from S3 (21 Oct 2026); re-verify before any public use (§0.2).

#### 1.6.1 Indian ODR providers (44 features)

| # | Feature | **Equator v2** | Jupitice | Presolv360 | Sama | CORD | Webnyay | CADRE | JustAct |
|---|---|---|---|---|---|---|---|---|---|
| F01 | No-login pre-filing suitability tool with free-forum signposting and last-date warnings | ● App. K §1–§4; P02 | ○ | ○ | ◐ (paid consultation) | ◐ (free consultation) | ○ | ○ | ○ |
| F02 | Criminal-matter hard exclusion with civil-dimension handling (s.138 compounding papers) | ● App. K §3; NN-24 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| F03 | Dispute-type plug-in catalogue (new types as configuration) | ● App. K §6–§7 | ◐ (broad catalogue) | ○ | ○ | ○ | ○ | ○ | ○ |
| F04 | Distinct intake forms by type × subtype × mechanism | ● V1–V6 §6; App. K §4 | ○ | ○ | ◐ (mediation vs arbitration) | ○ | ◐ (smart forms) | ○ | ○ |
| F05 | Separate login portals per persona (party, representative, mediator, arbitrator, case manager, enterprise, chambers) | ● App. S §2; D2-05 | ◐ (stakeholder dashboards) | ◐ | ○ | ○ | ○ | ○ | ◐ (role portals) |
| F06 | Aadhaar (OVSE) / DigiLocker / PAN / MCA onboarding | ● App. S §3; D2-06 | ◐ (Aadhaar eSign) | ○ | ○ | ○ | ○ | ○ | ○ |
| F07 | Scoped, revocable representative authority (LoA / Vakalatnama) | ● App. S §4; NN-27 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| F08 | Bulk CSV / SFTP / API intake for lenders and insurers | ● P09 (100k rows) | ◐ | ◐ | ◐ | ◐ ("bulk NBFC") | ○ | ○ | ○ |
| F09 | Clause-at-sanction API with verification seal | ● P09 (D1) | ○ | ○ | ○ | ◐ (clause drafting) | ○ | ○ | ○ |
| F10 | Appointment-defensibility controls (lender-trigger block, post-dispute s.12(5) waiver, Independence Evidence Pack) | ● P03/P09; NN-03 | ○ | ○ (under Bom HC query) | ○ | ◐ (Appointments Council) | ○ | ○ | ○ |
| F11 | Published, rules-based neutral allocation with no outcome metrics | ● App. N §6; NN-28 | ○ | ◐ (AI matching) | ○ | ◐ | ✖ (selection uses "past performance") | ○ | ○ |
| F12 | Neutral grades A/B/C with competence gate and Equator QAP | ● App. N §3–§4; D2-12 | ○ | ○ | ○ | ◐ (training/certification) | ○ | ○ | ○ |
| F13 | Public neutral directory without paid/featured listings | ● App. N §2; D2-14 | ◐ (login-gated; 19 featured cards public; paid status undisclosed — v3.0) | ◐ | ◐ | ◐ | ◐ | ○ | ○ |
| F14 | Published Code of Conduct + neutral-conduct complaints + party feedback | ● App. N §5–§7 | ◐ (Empanelment Rules and Undertaking published; securities complaint matrix; feedback confidential — v3.0) | ◐ (Rules, Code & Fees link) | ○ | ◐ | ○ | ○ | ○ |
| F15 | Institutional governance body separate from company board (Institutional Committee) | ● App. N §1; D2-15 | ○ | ◐ (advisory council) | ○ | ◐ (Appointments Council) | ○ | ○ | ○ |
| F16 | Pre-dispute negotiation (offer/counter-offer, blind bid) | ● P04 | ● | ● | ● | ● | ○ | ● | ○ |
| F17 | Conciliation / mediation with caucus rooms | ● P04 | ● | ● | ● | ● | ● | ● | ● |
| F18 | Arbitration with reasoned award and award scrutiny | ● P04/P06; App. N; V6 | ● (award) | ● (award) | ● (award) | ● (award) | ● (award) | ● (award) | ● (award) |
| F19 | Optional internal appeal tier | ● P04 (D4) | ○ | ○ | ○ | ● (Rules 2.0) | ○ | ○ | ○ |
| F20 | Emergency arbitrator and expedited / documents-only tiers | ● P04; V6 §7.2–§7.3 | ○ | ○ | ◐ (180-day sole) | ● (EA in Rules 2.0) | ○ | ○ | ○ |
| F21 | Video hearings | ● P04 (LiveKit) | ● | ● | ● | ● | ● | ◐ | ● (AES-256) |
| F22 | Mediation not recorded by default; arbitration recording only with consent | ● NN-11 | ○ | ○ | ○ | ○ | ○ | ○ | ✖ (transcription feature) |
| F23 | Omnichannel notices (WhatsApp/SMS/email/Speed Post) with delivery evidence | ● P07 | ● (LNMS) | ○ | ● (+ Speed Post) | ○ | ◐ (omni-channel intake) | ● (email/WhatsApp) | ○ |
| F24 | Vernacular AI voice agent with disclosure and calling-hour controls | ● P07 (D9); NN-12 | ◐ (chatbot) | ○ | ◐ (human calls) | ○ | ○ | ○ | ○ |
| F25 | DMS with party-controlled sharing, e-bundles, hash manifest | ● App. L; NN-10, NN-22 | ● (audit trail) | ● (encrypted exchange) | ○ | ○ | ● (e-bundles) | ○ | ● (e-bundling) |
| F26 | AI type copies of handwritten/screenshot material with originals preserved | ● App. L §6; NN-32 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| F27 | Translation (22 scheduled + 6 UN languages) labelled "for convenience" + certified-translation workflow | ● App. L §7; D2-09 | ● (translation) | ○ | ◐ (vernacular on request) | ◐ (25 languages) | ◐ (multilingual) | ○ | ○ |
| F28 | AI pleadings drafting grounded in party documents, verified citations only, identical for both sides | ● App. M; NN-25 | ◐ (AI drafting) | ◐ (AI library) | ○ | ○ | ◐ (Draft-Your-Self) | ◐ ("AI-driven") | ○ |
| F29 | AI award skeleton with party validation; human signs; published AI rule | ● P11 (D3) | ◐ (AI drafting, Trust Layer) | ○ | ○ | ● (AI governance in Rules) | ◐ (AI suite) | ○ | ○ |
| F30 | e-Sign (Aadhaar eSign / DSC) | ● P06 | ● | ● | ○ | ○ | ○ | ○ | ○ |
| F31 | State-wise e-Stamp at signing | ● P06; NN-09 | ● (NeSL + wallet) | ○ | ● (₹40 procurement) | ○ | ○ | ○ | ○ |
| F32 | Settlement-money loop (UPI AutoPay / escrow with trustee) without pass-through | ● P05/P06 (D2); NN-13 | ◐ | ○ | ○ | ○ | ○ | ○ | ○ |
| F33 | Immovable-property route to physical execution, stamping and registration | ● P06; App. R §4; NN-08 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| F34 | Execution pack (s.36 bundle, certified copies, BSA s.63 certificate) | ● P06; App. R §4 | ● | ◐ (execution support) | ● (₹500) | ● ("award upheld") | ○ | ○ | ○ |
| F35 | Case-status portal (papers filed, dates, interim/final orders, parties) | ● App. R §1–§2 | ◐ (dashboards) | ● (dashboard) | ○ | ○ | ○ | ○ | ◐ |
| F36 | Consent-only publication of awards/settlements with redaction | ● App. R §3; NN-26 | ○ | ○ | ○ | ○ | ○ | ○ | ○ |
| F37 | Grievance SaaS with regulator clocks → ODR escalation | ● P09 (D5) | ◐ (LNMS/CMS) | ○ | ○ | ◐ (dispute system design) | ◐ (grievance redressal) | ○ | ○ |
| F38 | POSH Internal Committee sealed SaaS | ● P09; NN-07 | ○ | ○ | ○ | ◐ (workplace) | ○ | ○ | ○ |
| F39 | Published fee card with calculator and API quotes, GST shown | ● P05/P13 (D7); NN-29 | ✖ (3P only) | ● (/fees) | ◐ (partial FAQ) | ◐ (tiered, amounts not seen) | ✖ | ✖ | ✖ |
| F40 | Private ADR Chambers / institution-as-a-service | ● P10 (D8) | ● | ○ | ● (SMART ODR, Lok Adalats) | ○ | ● (Arbitral Institutions) | ○ | ● (NPAC) |
| F41 | International (INT) multi-currency invoicing with compliance gates (sanctions, UBO, FEMA, DPDP s.16) | ● V6; NN-19 | ◐ (cross-border MSME) | ◐ (cross-border from USD 500) | ○ | ○ | ◐ (GIFT City claim [U]) | ○ | ○ |
| F42 | Mobile apps (iOS + Android) | ● P12 | ○ | ✖ (directory FAQ) | ○ | ○ | ◐ (device-agnostic web) | ○ | ○ |
| F43 | ISO/IEC 27001 certified | Target; claim only when certified (App. Q; P14) | ○ | ◐ | ◐ | ○ | ● (2022) | ○ | ◐ (2FA) |
| F44 | Annual Transparency Report (caseload, appointments by gender/method, challenges, service levels) | ● App. N; S5 C3; P13 | ○ | ○ | ○ | ◐ ("0 awards set aside") | ○ | ○ | ○ |

#### 1.6.2 Claim-assistance and global references (subset relevant to Equator design)

| # | Feature | **Equator v2** | ClaimBuddy | Insurance Samadhan | Policybazaar | InsuranceDekho | AAA-ICDR | Immediation | Modria | CourtCorrect |
|---|---|---|---|---|---|---|---|---|---|---|
| G01 | Neutral third party (not acting for one side) | ● | ✖ | ✖ | ✖ (broker) | ✖ (broker) | ● | ● | ● | ✖ (firm-side) |
| G02 | Free statutory route shown before any paid option | ● V4; NN-20 | ○ | ◐ (escalates to Ombudsman) | ○ | ○ | n/a | n/a | ◐ (court-embedded) | ◐ |
| G03 | No percentage-of-claim fee for retail policyholders | ● NN-18 | ○ [U] | ✖ (20% + GST success fee, site Oct 2026) | ● (free) | ● (free) | n/a | ● (fixed fee) | n/a | n/a |
| G04 | Hospital / TPA evidence request | ● V4 (PI-INS-04) | ● | ○ | ◐ | n/a | n/a | n/a | n/a | n/a |
| G05 | Insurer-convened settlement days (batch) | ● V4 (PI-INS-10) | ○ | ○ | ● | ○ | n/a | n/a | n/a | n/a |
| G06 | Insurer–insurer / subrogation B2B ODR | ● V4 (D11) | ○ | ○ | ○ | ○ | ◐ | ● | ○ | ○ |
| G07 | Asynchronous negotiation before a neutral | ● P04 | ○ | ○ | ○ | ○ | ○ | ○ | ● | ○ |
| G08 | AI summary validated by parties before any draft | ● P11 (D3) | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| G09 | Human neutral signs; AI never decides | ● NN-01 | n/a | n/a | n/a | n/a | ● | ● | ◐ (evaluative module) | ✖ (suggests outcomes) |
| G10 | Regulator-mapped checks on grievance responses | ● P09 (D5) | ○ | ○ | ○ | ○ | n/a | n/a | n/a | ● |
| G11 | Published AI standards / governance rule | ● P13 FR-P13-07 | ○ | ○ | ○ | ○ | ● | ○ | ○ | ○ |
| G12 | Regulatory sanction on record for marketing claims | — | ○ | ○ | ● (IRDAI ₹5 crore, 4 Aug 2025) | ○ | ○ | ○ | ○ | ○ |

### 1.7 Threat register — v2 deltas over Appendix H §1.2

Appendix H §1.2 ranks ten threats; the following are **new or changed** on 21 Oct 2026.

| # | Threat (new / changed) | Evidence | Equator response | Owner phase |
|---|---|---|---|---|
| TT-01 | Presolv360 now publishes a full model fee card — Equator's D7 "only published card" framing is no longer true | [V] presolv360.com/fees | Reframe D7 as calculator-driven, GST-inclusive quotes with stage refunds and API quotes; Claims Register blocks "only" wording (NN-17) | P13 |
| TT-02 | CORD Rules 2.0 (4 Sep 2026) ships AI governance + appeal + Appointments Council before Equator launches | [V] | Equator Rules must ship the same chapters at launch, plus published Service Charter metrics and transparency report CORD lacks | P04, P13; App. N |
| TT-03 | Jupitice e-stamp + e-sign (23 Jul 2026) closes part of Equator's D2 gap | [C] | D2 differentiation rests on the **settlement-money loop** (UPI AutoPay, escrow with trustee, reconciliation, default → escalation), not on e-stamp alone | P05, P06 |
| TT-04 | Claim-assistance players capture the INS front door with success fees and broker-funded "free" help | [V/V2] | Free-route-first INS Explorer; flat Claim Prep products; insurer-paid B2B mediation (V4; Appendix O) | P08d |
| TT-05 | Reliance group as both a potential vendor (Jio Haptik, JioCX) and a frequent party (Jio Financial Services, Jio Payments Bank, Reliance Retail, insurance JVs) | S7 §0 item 3 | Vendor conflict firewall and per-case vendor switch (§4.8; FR-P07-V2-T06) | P07, P11 |
| TT-06 | Institute (Equator ADR Institute / Equa Trainings) claims could be attributed to Equator by association | S6 §1.4 | Institute corrections (§3.4) as a pre-condition of any referral link (flag `academy.institute_referral` OFF; assumption A-03) | P10, P13 |

### 1.8 Operating protocols

| Protocol | Rule | Owner | Output |
|---|---|---|---|
| Re-verification | Every `growth.benchmark_entries` row re-verified every 90 days; fee rows every 30 days during launch quarter | `growth_manager`; `legal_reviewer` approves | Updated rows; expired rows unpublish dependent copy |
| Review mining (PI-CMP-05) | Quarterly: Google, Trustpilot, MouthShut, Play Store, consumer-forum, Reddit reviews for ClaimBuddy, Insurance Samadhan, Policybazaar, InsuranceDekho, Sama, Presolv360, CORD, Jupitice; themes tagged `fee_shock`, `delay`, `communication`, `outcome`, `trust`, `notice_harassment` | `growth_manager` | Internal theme report (never quotes reviewers publicly); FAQ and microcopy backlog for Appendix P |
| Mystery-shop | Twice a year, a staff member files a test enquiry (no case data, no deception of neutrals or parties — enquiry stage only) to capture journeys and current published fees | `growth_manager` | Journey screenshots stored in `growth` schema with date |
| Category capture | Manual capture of Jupitice and CORD category lists (OI-T-01) before Appendix K §7 roadmap is finalised | `growth_manager` | K §7 roadmap update via pack manifest |
| Comparative copy review | Any page naming a competitor: `legal_reviewer` sign-off + Claims Register link; no logos of competitors | `cms_editor` | Approved page version |

---

## 2. International institutions benchmark

Twelve institutions: SIAC, SIMC, ICC, LCIA, HKIAC, AAA-ICDR, JAMS, CIETAC, DIAC (Dubai), MCIA, IIAC, IAMC; v3.0 adds DIAC (Delhi) to the governance table (Appendix AF §AF.2.2). Fee rows for JAMS, AAA-ICDR, CEDR and SMC, LCIA hourly secretariat rates and the 5% overhead, and HKIAC banded administration and fixed appointment fees are in Appendix AF §AF.2.1 (AFC-T-11); SIAC figures there came through a secondary source on 23 Oct 2026. V6 §15 already records the INT fee and procedure positioning against SIAC, ICC, LCIA, HKIAC, AAA-ICDR, IIAC, MCIA and DIAC; this section covers the institution-wide practices that Appendices N and R implement across **all** verticals.

### 2.1 Governance and rules in force

| Institution | Rules in force (Oct 2026) | Case-decision body | Administration | Separation from commercial board | Tag |
|---|---|---|---|---|---|
| **SIAC** | Arbitration Rules 2025 (7th ed.), in force 1 Jan 2025 | Court of Arbitration (39 members, 11 women; President Lucy Reed) | Registrar + Secretariat (scrutiny, administration) | Board of Directors (strategy) separate from Court | [V] Clifford Chance; SIAC Annual Report 2025 |
| **SIMC** | SIMC Mediation Rules 2023; SIAC–SIMC Arb-Med-Arb Protocol | SIMC (appointment on default; objection-replacement) | SIMC case team | n/a (mediation centre) | [V] SIMC Rules PDF |
| **ICC** | **Arbitration Rules 2026, in force 1 Jun 2026** (Terms of Reference abolished → initial CMC; Art. 12 disclosure; Art. 30 early determination; App. VI Highly Expedited) | International Court of Arbitration (members from 100+ jurisdictions [U count]) | Secretariat (regional teams) | Court independent of ICC World Council [K] | [V] Crowell; CMS |
| **LCIA** | Arbitration Rules 2020; Mediation Rules 2020 | LCIA Court (divisions decide challenges) | Registrar/Secretariat | LCIA Board (company) separate [K] | [K]/[V] casework report |
| **HKIAC** | Administered Arbitration Rules 2024 (1 Jun 2024) + 1 Jan 2026 amendments | Council with Appointments Committee and Proceedings Committee | Secretariat | Council committees [K] | [V] HSF; MoFo |
| **AAA-ICDR** | ICDR International Arbitration Rules 2021; AAA Commercial Rules 2022 | ICDR administrators; AAA Board | ICDR case teams | Not separated as a "court" [K] | [K] |
| **JAMS** | International & Comprehensive Rules 2021; AI Disputes Rules 2024 | JAMS administration | Case managers | For-profit; exclusive panel [K] | [K] |
| **CIETAC** | Arbitration Rules 2024 (1 Jan 2024) | CIETAC Arbitration Court | Secretariat | Under CCPIT [K] | [V] Freshfields |
| **DIAC (Dubai)** — Dubai International Arbitration Centre, code `inst.diac_dubai` (renamed v3.0) | DIAC Arbitration Rules 2022 (21 Mar 2022); Dubai Decree No. 34 of 2021 abolished DIFC Arbitration Institute and EMAC, transferring cases to DIAC | Arbitration Court | Executive Office / Registrar | Board of Directors separate [K] | [K] (article numbers [U]) |
| **MCIA** | MCIA Rules 2016 and **MCIA Rules 2025** (content and in-force date [U]) | MCIA Council | Secretariat | Council chaired by eminent jurist [K] | [V] existence |
| **IIAC** | IIAC (Conduct of Arbitration) Regulations 2023; statutory body (NDIAC Act 2019, renamed 2022) | Chairperson with advisory panel (3–10 advisors; ≥ 2 advise on each appointment); Chamber of Arbitration | Registrar | Statutory | [V] IIAC Regulations 2023 |
| **IAMC** (Hyderabad) | IAMC Arbitration and Mediation Rules | Board of Trustees (former SC judges) | Secretariat | Trust | [K] |
| **DIAC (Delhi)** — Delhi International Arbitration Centre (Delhi High Court), code `inst.diac_delhi` (added v3.0) | DIAC (Administrative Costs & Arbitrators' Fees) Rules 2018; DIAC (Arbitration Proceedings) Rules 2023 — r.33.5 lets the Centre or tribunal terminate a claim or counter-claim if fees are not deposited within 30 days | Court-annexed centre | Centre secretariat [U] | Delhi High Court [U] | [V] *Samsung India Electronics v DIAC*, Del HC W.P.(C) 3440/2026, 18 Mar 2026 (AF-S46); 2018 schedule figures [U] |

**Pattern.** Every top-tier institution separates (i) a corporate board, (ii) a case-decision body and (iii) a registrar/secretariat. Equator implements this as the **Equator Institutional Committee** (majority external) with Appointments, Challenge, Scrutiny, Ethics & Complaints, Rules, AI Oversight and Transparency sub-committees, supported by the Registrar; the ERSPL board takes no case decisions (D2-15; RT-01; Appendix N §1).

### 2.2 Panels, appointments and challenges

| Institution | Panel model | Appointment practice | Challenge decision | Diversity practice | Tag |
|---|---|---|---|---|---|
| SIAC | Published Panel (application: CV, references, appointment record, award samples); off-panel appointments allowed | Joint nomination of sole arbitrator within 21 days; arbitrator signs Statement of Acceptance, Independence, Impartiality and Availability (r.20) | SIAC Court, reasoned (r.28.4), final; committee with ≥ 1 outsider where the challenged arbitrator sits on SIAC bodies (r.28.6); **redacted publication under deemed consent (r.28.7)** | 36% women among SIAC appointments (2025) | Rules and practice [V]; statistics [C] (institution-reported — v3.0, Appendix AF §AF.0.2); panel criteria [U] |
| SIMC | Panel of international mediators; partner-organisation panels | Joint nomination (need not be on panel); failing agreement in 10 days SIMC appoints (r.4.2); objection → replacement within 5 business days | n/a | — | [V] |
| ICC | No closed panel; National Committees propose; arbitrator self-registration in Case Connect | Parties must provide a **list of relevant persons/entities** (Art. 12(5)); doubts resolved in favour of disclosure (Art. 12(2)) | Court; reasons on request | Women 29.6% overall; 44.6% of Court appointments (2025) | Rules [V]; statistics [C] (institution-reported) |
| LCIA | Database; Court selects | Court reviews independence and availability before appointment | LCIA Court; **"unfitness" includes failure to conduct the arbitration with reasonable efficiency, diligence and industry (Art. 10.2)**; **Challenge Decision Database — 84 decisions public** | Women 38%; 49% of Court selections (2025) | Rules [V] Kennedys; Acerislaw; statistics [C] (institution-reported) |
| HKIAC | Panel (senior) and List (developing), periodic review | **Must consider diversity** when appointing (Art. 9A); may revoke an appointment in exceptional cases (Art. 13.10) | Committee; 4 challenges in 2025, all rejected | Women 36.4%; **first-time appointees 20.5%** (published metric) | Rules [V] MoFo; statistics [C] (institution-reported) |
| AAA-ICDR | Roster > 725 international neutrals; specialised panels | AAAi Panelist Search; AAA/ABA Code of Ethics (2004) | ICDR administrative decision | [K] | [V]/[K] |
| JAMS | Exclusive panel (largely retired judges) | List from exclusive roster | Administrative | [K] | [K] |
| CIETAC | Closed Panel, renewed periodically; off-panel subject to confirmation | CIETAC may appoint presiding arbitrator where agreed procedure is unfair (Arts. 26–27) | CIETAC Chairman | [K] | [V]/[K] |
| DIAC (Dubai) | Panel [U] | Arbitration Court | Arbitration Court | [U] | [K] |
| MCIA | "Call for Arbitrators"; YMCIA directory | Council | Council | [U] | [V] page |
| IIAC | Panel maintained by Centre; Chamber of Arbitration | Chairperson appoints with advisory panel; 28 days to agree sole arbitrator (Reg. 11–14) | Chairperson; **target 15 days** (Reg. 15–16) | — | [V] |
| IAMC | Panel | Trust secretariat | [U] | — | [K] |

### 2.3 Transparency and publication

| Practice | SIAC | ICC | LCIA | HKIAC | AAA-ICDR | CIETAC | IIAC | MCIA | **Equator** |
|---|---|---|---|---|---|---|---|---|---|
| Award publication | Only with written agreement of all parties, redacted (r.60) [V] | **Opt-out**: may publish ≥ 2 years after notification; any party may object or ask for anonymisation; opt-in where a confidentiality agreement exists (ICC Note) [V] | Only with prior written consent of all parties and tribunal (Art. 30.3) [K] | Redacted where no party objects [U wording] | Consumer/employment case data published (e.g., California CCP §1281.96) [K] | Selected case digests [K] | No publication provision [V] | None [U] | **Opt-in by all parties in every track, including foreign-seated INT** (X-35; A&C Act s.42A for India-seated matters); redaction profile; FAM/POSH/health/minors never in full (NN-26; Appendix R §3) |
| Challenge decisions | Redacted, deemed consent (r.28.7) [V] | Reasons on request [K] | Database, 84 decisions [V] | Digests [K] | — | — | — | — | Redacted after 12 months under Equator Rules deemed consent, behind `publication.challenge_decisions.enabled` = OFF until counsel's s.42A view (RT-08; Appendix N; Appendix R R-R9) |
| Tribunal composition register | — | Names, nationality, role, appointment method, sector, counsel [V] | — | — | — | — | — | — | INT/COM only, opt-out; never FAM/WRK/POSH/INS-health (Appendix R) |
| Annual statistics | Detailed annual report [V] | Annual statistics [V] | Casework report + **first publication of turnaround times** (2025) [V] | Annual statistics incl. interim-measures data [V] | Annual report [K] | Work report [K] | [U] | [U] | **Annual Transparency Report + quarterly dashboard** with suppression of any cell below n = 10 (X-28) and sealed-vertical exclusion (S5 C3; Appendix N; P13) |
| Award scrutiny | Registrar approves form; flags substance; estimate in 30 days, draft in 90 days of last submission (r.53) [V] | Court approves form; draws attention to substance [K]; quality of draft award considered in fees (App. III Art. 6(2)) [V] | None [K] | None (form check) [K] | None [K] | Draft-award scrutiny [K] | Registrar suggests form changes within 21 days (Reg. 33) [V] | [U] | Scrutiny S0–S5 gate; never affects the tribunal's freedom of decision (S5 C6; Appendix N; V6) |
| Confidentiality undertakings from non-counsel attendees | — | — | — | — | — | — | — | — | Adopted from **SIMC r.9.4** (≥ 2 business days before session) for mediation (V6 §7.4 M-4) |
| Information security directions | r.61 [V] | — | Art. 30A [K] | Arts. 13.1, 45A [V] | Cybersecurity in Rules [K] | — | — | — | Security tier at first CMC (V6 `security_tier`; S5 R18) |

### 2.4 Case-management platforms

| Platform | Vendor | Notable features [V unless marked] | Equator target (pointer) |
|---|---|---|---|
| SIAC Gateway (Aug 2024) | Opus 2 | E-filing, e-payment, secure storage, real-time case management, 24/7 access | Own build: filing, payments, DMS with hash ledger (P02, P05; App. L) |
| ICC Case Connect (next-gen, Apr 2025) | Opus 2 | Online Requests with e-payment; role-specific portals; task workflows; **Court decision workflows in-platform**; arbitrator expense management; arbitrator self-registration; > 8,000 arbitrators onboarded | Committee decisions in-platform as `InstitutionalDecision` records; neutral expense claims; empanelment self-application (App. N; P03) |
| HKIAC Case Connect (Nov 2021) | Thomson Reuters HighQ | Repository with upload notifications; activity log; **case calendar syncable to Outlook**; in-platform messaging | ICS calendar feed per user per case; upload notifications; messaging with ex parte guard (App. R §1–§2) |
| AAA WebFile / Panelist eCenter | AAA | Online filing, payments, neutral portal [K/U] | — |
| IIAC portal | IIAC | Portal or email filing; physical/virtual/hybrid hearings (Reg. 4–6, 20–21) | — |
| MCIA | MCIA | Online fee calculator | Public fee calculator (D7) |
| **Gap all share** | — | No integrated video hearing room in SIAC Gateway or ICC Case Connect | Integrated LiveKit hearings with caucus rooms (P04) |

### 2.5 Fees (benchmark summary)

| Institution | Model | Key figures | Tag |
|---|---|---|---|
| SIAC | Ad valorem, SGD | Registration SGD 3,000 (overseas); admin cap SGD 150,000; Streamlined capped at 50% of maxima | [V R5] |
| ICC | Ad valorem, USD; 2026 Schedule of Fees | Filing USD 5,000; admin cap USD 150,000 (pre-2026 scale; 2026 scale figures [U]) | [V]/[U] |
| LCIA | Hourly, GBP | Registration GBP 1,950; arbitrators GBP 250–650/h; 5% of tribunal fees | [V R5] |
| HKIAC | Dual (hourly or ad valorem), HKD | Registration HKD 10,000 (from 1 Jan 2026); hourly cap HKD 7,500 | [V R5] |
| IIAC | Ad valorem, INR and **USD** | International: filing USD 500; **admin cap USD 15,000**; arbitrator cap USD 200,000; EA USD 2,000 + USD 15,000 | [V S5 A12.1] |
| MCIA | Ad valorem, INR only | Filing ₹50,000; admin to ₹41.6 lakh; EA admin ₹80,000 | [V] |
| IAMC | INR admin; USD sole-arbitrator scale | Admin cap ₹30 lakh; USD scale cap ≈ USD 344,543 | [V R5] |
| SIMC / ICC Mediation | Filing + admin + mediator rate | ICC Mediation filing USD 3,000; admin up to USD 30,000 | [V R5] |

**Board item (re-benchmark).** Appendix B's INT admin cap (USD 50,000, per V6 §15) sits above IIAC's USD 15,000 and below SIAC's SGD 150,000; S5 D-3 recommends ~USD 25,000–35,000 for India-seated INT. This appendix does not change the figure (Appendix B precedence); it is listed as OI-T-14 for the Board's fee approval (M-01).

### 2.6 Practices adopted by Equator (with implementing pointers)

| # | Practice | Benchmark source | Equator implementation | Pointer | Phase |
|---|---|---|---|---|---|
| IP-01 | Separate case-decision body from corporate board; reasoned institutional decisions | SIAC Court; ICC Court; LCIA Court; IIAC advisory panel | Equator Institutional Committee + sub-committees; `InstitutionalDecision` objects with members, votes, reasons, publication flag | App. N §1; D2-15 | P03 |
| IP-02 | Recusal rule where a challenged neutral sits on institutional bodies | SIAC r.28.6 | External-majority committee for such challenges | App. N §1, §5 | P03 |
| IP-03 | Statement of Acceptance, Independence, Impartiality and Availability; "doubts → disclose"; parties' relevant-persons list | SIAC r.20; ICC 2026 Art. 12(2), 12(5) | Neutral statement on every appointment; relevant-persons list at filing drives conflict engine | App. N §5–§6; V6 `intl.relevant_persons` | P03, P08f |
| IP-04 | Diversity duty and first-time-appointee metric | HKIAC Art. 9A; HKIAC statistics | Diversity as a published allocation consideration within NN-28 (never overriding conflict or eligibility filters); first-time-appointee % in the Transparency Report | App. N §6; S5 C2 | P03, P13 |
| IP-05 | Unfitness for inefficiency; late-draft fee reduction | LCIA Art. 10.2; ICC App. III Art. 6(2) and Note | Code ground "fails to conduct proceedings with reasonable efficiency"; fee-reduction ladder for late drafts (subject to counsel, S5 F Q5) | App. N §5; App. B | P03, P05 |
| IP-06 | Award scrutiny as a hard gate with clocks | SIAC r.53; IIAC Reg. 33 | Scrutiny S0–S5; `award.status: draft_submitted → scrutiny → form_approved → issued`; s.29A buffer | App. N; V6; App. A | P04, P06 |
| IP-07 | Challenge decisions published redacted | SIAC r.28.7; LCIA database | Redacted publication after 12 months under Equator Rules (RT-08) | App. N; App. R §3 | P13 |
| IP-08 | Consent-only award publication | SIAC r.60; LCIA Art. 30.3 | Opt-in by every party in all tracks, including foreign-seated INT (X-35); ICC-style opt-out not adopted | App. R §3; NN-26 | P06, P13 |
| IP-09 | Annual statistics with service-level turnaround times | LCIA 2025; SIAC; ICC; HKIAC | Annual Transparency Report + Service Charter metrics live | App. N; App. R | P13 |
| IP-10 | Procedure tiers keyed to value with "circumstances warrant" override | SIAC r.13–14; ICC App. V–VI | Streamlined / Highly Expedited (opt-in) / Expedited / Standard | V6 §7.2 | P08f |
| IP-11 | Emergency arbitrator before notice of arbitration; protective preliminary order | SIAC Sch. 1; ICC App. IV; IIAC Reg. 18; HKIAC Sch. 4 | EA-1…EA-5 with 1-business-day appointment target and 14-day order | V6 §7.3 | P04, P08f |
| IP-12 | Third-party funding disclosure (existence + funder identity) | SIAC r.38; CIETAC Art. 48; HKIAC Art. 44 | `intl.tpf_disclosures`; conflict re-run on change | V6 §16 | P08f |
| IP-13 | Arb-Med-Arb with 8-week window and paused clocks | SIAC–SIMC AMA Protocol | AMA inside arbitration; consent award; different neutral by default (master §5.3) | V6 §7.4; App. A | P04 |
| IP-14 | Mediation confidentiality undertakings; no recording or transcript | SIMC r.9.4–9.5 | Pre-session gate; NN-11 | V6 §7.4; App. N | P04 |
| IP-15 | Joint mediator nomination window then institutional appointment; objection-replacement in 5 business days | SIMC r.4 | 10-day window; Appointments Committee | V6 §7.4 M-3 | P04 |
| IP-16 | Calendar sync, upload notifications, activity log | HKIAC Case Connect | ICS feed; notifications; activity log in case-status portal | App. R §1–§2 | P02, P12 |
| IP-17 | Certified copies and verification; letters confirming case registration for court applications | ICC; SIAC; IIAC Reg. 33(11); HKIAC letters | Registrar-certified copies (QES) with verification URL; registration letters; country enforcement cards | App. R §4; V6 §13 | P06 |
| IP-18 | Party validation of AI summaries; human signs | AAA-ICDR AI Arbitrator | D3 pipeline; AI lane flag OFF pending counsel | App. E; P11; V6 | P11 |
| IP-19 | Credentialing separate from administration | SIMI/IMI vs SIMC; IIAC Chamber vs Academy | Equator QAP (assessment) separate from Equator ADR Institute (training) | App. N §9–§10; §3 below | P03, P10 |
| IP-20 | Virtual-first default; environmental consideration in directions | HKIAC Arts. 13.1, 34.4 | Virtual-first hearings and e-bundles by default | P04 | P04 |

### 2.7 Practices deliberately not adopted

| Practice | Institution | Reason |
|---|---|---|
| Naming the case body a "Court" | SIAC, ICC, LCIA, DIAC | NN-17; master §1 — Equator never implies it is a court (D2-15) |
| Same-tribunal conciliation inside arbitration as default | CIETAC | Enforcement risk (*Gao Haiyan v Keeneye*, HKCA 2011 [K]); Mediation Act 2023 s.17 bar in statutory mode; master §5.3 requires a different neutral by default |
| Opt-out award publication for India-seated arbitrations | ICC Note | A&C Act s.42A confidentiality duty on the institution; counsel question 02 §5 Q1 |
| Deemed-consent publication of full FIN/INS awards | ICSID 2022 model | Consumer and DPDP risk; only anonymised reasoning digests with consent (D2-10) |
| Exclusive premium panel with employment of neutrals | JAMS | Conflicts with open, merit-based, rotation allocation (NN-28) and concentration caps |
| Unreasoned award as a default | ICC HEAP option | Permitted only on all-party opt-in in INT HEAP (V6 §7.2); A&C s.31(3) requires reasons unless agreed |
| AI as decision-maker | — | NN-01; A&C s.31 |

---

## 3. Training and accreditation providers benchmark

### 3.1 Provider benchmark

| Provider / regime | Type | Credential tiers | Entry / hours | Assessment | Maintenance | Price signal | Equator credential code (`accreditation_body`) | Tag |
|---|---|---|---|---|---|---|---|---|
| **IMI** (International Mediation Institute) | Global standards body | **Qualified Mediator** (via a Recognized Mediator Training Program, RMTP — formerly CMTP); **Certified Mediator** (via a Qualifying Assessment Program, QAP); specialisations: Intercultural (ICQAP), Online/ODR (ODR-QAP), Mediation Advocate/Advisor (MAQAP) | RMTP ≥ 40 h (≤ 10% asynchronous online); Certified requires **≥ 200 hours or ≥ 20 mediations** | RMTP: ≥ 1 role-play assessment ≥ 60 min, 100% supervised, assessor ≠ coach. QAP: experience verification + knowledge + skills; ≥ 1 assessor independent of the QAP | Certified: annual listing; Feedback Digest updated every 2 years; Code; biennial QAP audit | Qualified €75 sign-up + €75/yr; Certified €165/yr | `IMI_QUALIFIED`, `IMI_CERTIFIED`, `IMI_INTERCULTURAL`, `IMI_ODR`, `IMI_ADVOCATE` | [V] imimediation.org |
| **CIArb** (UK Royal Charter) | Professional body | ACIArb → MCIArb → FCIArb (≥ 5 years' ADR experience + Diploma + peer interview) → Chartered Arbitrator (≥ 10 years) | Course routes or experience route | Modules, award writing, peer interview | Membership; title regulation only | Not retrieved [U] | `CIArb_ACIArb`, `CIArb_MCIArb`, `CIArb_FCIArb`, `CIArb_CArb` | [V] ciarb.org |
| **CEDR** (UK) | Trainer / accreditor | CEDR-Accredited Mediator; Advanced; Workplace modules; International Accreditation Programme | 6–7 days intensive | Assessed skills course [U detail] | Refresher | London £5,800; International (virtual) £4,050; Workplace M1 £1,600, M2 £3,450 | `CEDR_ACCREDITED` | [V] cedr.com |
| **SIMI / SMC** (Singapore) | Credentialing scheme (sunsetting) | SIMI Accredited L1–L3; SIMI Certified | L1 after SCMP Modules 1–2 + Mediation Skills Assessment; Certified: 20 mediations / 200 h in 3 years | Certified: 90-min role-play, 30-min debrief, 60-min written test, reflection; Feedback Digest ≥ 10 mediations | — | Admin S$327; QAP S$1,090 (incl. 9% GST) | `SIMI_L1/L2/L3/CERTIFIED` — legacy, `superseded_by` IMI | [V] |
| **SIMI → IMI transition** | — | Applications closed 31 Aug 2026; **scheme ceases 31 Mar 2027**; SIMI Partner Scheme ends by 30 Oct 2026; SIMI Certified → IMI Certified via Cross-Recognition without reassessment; SIMI L1–L3 → IMI Qualified pathway opening Q4 2026 | — | — | — | — | Register must map `superseded_by` from 1 Apr 2027 | [V] IMI statement 23 Aug 2026 |
| **MCPC** (Supreme Court Mediation & Conciliation Project Committee) | De facto Indian court standard | "40-hour trained"; "trained mediator" (40 h + ≥ 20 mediations, ≥ 10 settled per NSLSA circular of 11 Dec 2015) | 40 h theory, role-play, demonstration + actual mediations under guidance; training needed "irrespective of background" | Trainer-observed | HC panel terms (e.g., 3 years) | Court/LSA programmes | `MCPC_40H`, `MCPC_TRAINED_MEDIATOR` (settlement counts recorded, **never scored** — NN-28) | [V] NALSA Manual; NSLSA circular |
| **IIAM** (Indian Institute of Arbitration & Mediation, Kochi) | Private institute | Training and panels | 40-hour-type | [U] | [U] | [U] | `OTHER` + provider record; reported early IMI QAP **[U — confirm before naming]** | [U] |
| **ICA** (Indian Council of Arbitration, FICCI) | Institution | Panel of arbitrators | Panel criteria [U] | [U] | [U] | [U] | `ICA_PANEL` | [U] |
| **MCIA** (Mumbai) | Institution | Panel; "Call for Arbitrators"; YMCIA; tribunal-secretary page | Criteria [U] | — | — | — | `MCIA_PANEL` | [V] page; criteria [U] |
| **AMDRAS** (Australia; MSB became AMDRAS Board 1 Jul 2024) | National accreditation system | Accredited, Advanced, Leading Mediator; Specialist Practitioner | Recognised Training Providers separate from Recognised Accreditation Providers | 1,200-word written + 2–2.5 h standardised simulation; assessors with 3 years + 100 h | Renewal: 20 h (Accredited) / 40 h (others) practice + 25 h CPD | — | `AMDRAS_ACCREDITED/ADVANCED/LEADING/SPECIALIST`; `NMAS` legacy | [V] msb.org.au (dates [U]) |
| **CMC** (UK Civil Mediation Council) | Registration body | Associate; Registered Mediator; Fellow | CMC Registered training course (post-1 Sep 2018 E&W) | Observation & experience points | **CPD ≥ 6 h/yr**; **PI ≥ £1,000,000**; complaints procedure; code no less rigorous than EU Model Code (2004) | — | `CMC_ASSOCIATE/REGISTERED/FELLOW` | [V] CMC Rules amended 1 Mar 2026 |
| **HKMAAL** (Hong Kong, incorporated 28 Aug 2012) | Accreditation body (Bar, Law Society, HKIAC, HKMC) | Accredited General Mediator; Family Mediator; supervisors, assessors, trainers | Stage 1 = 40-hour recognised course (100% attendance) | Stages 2–3 assessment | Law Society panels: CPD 20 points / 4 years | CityU course HK$16,000 | `HKMAAL_GENERAL`, `HKMAAL_FAMILY` | [V] LegCo paper; CityU |

### 3.2 Design rules Equator takes from the benchmark

| # | Rule | Benchmark basis | Implemented in |
|---|---|---|---|
| TR-01 | Grade C floor = **40 hours** of mediation training from any recognised provider | MCPC 40; IMI RMTP 40; HKMAAL 40; NMAS 38; Law Society of Singapore 40 | App. N §3–§4; D2-12 |
| TR-02 | Every grade route includes an **assessed simulation**; ≥ 2 assessors, ≥ 1 independent; a trainer never assesses own trainee | IMI QAP criterion 5; RMTP coach ≠ assessor; SIMI QAP | Equator QAP (App. N §9–§10) |
| TR-03 | Experience tier uses verified **activity** plus years; years-of-standing gates (15 years) mirror court and bar panels | IMI 200 h / 20; MCPC Model Rules 15 years; Law Society of Singapore Senior Mediator 15 years | Grade B (> 15 years) + competence gate (D2-12) |
| TR-04 | Retired judges acting as **mediators** still complete 40 hours (or documented court-annexed mediation experience); no training legally required for arbitrators in India [K] | MCPC Manual ("irrespective of his background") | Grade A rule (D2-12) |
| TR-05 | Biennial maintenance with CPD; Feedback Digest export compatible with IMI | IMI; NMAS/AMDRAS; CMC; HKMAAL | App. N §7 (S6-13, S6-18) |
| TR-06 | Credential register supports consolidation (`superseded_by`) and hidden statutory values (`MCI_REGISTERED`, `ACI_ACCREDITED`) behind flags `mci_regs_in_force`, `aci_operational` | SIMI → IMI; NMAS → AMDRAS; MCI established by S.O. 4781(E), 27 Aug 2026 with no regulations; ACI not operationalised | App. N; P03 |
| TR-07 | Training never buys a grade, empanelment or allocation priority | IIAC separates Chamber (empanelment) from Academy (training) by statute; NN-28 | App. N §6, §9–§10 |
| TR-08 | Settlement counts are recorded where a regime requires them (MCPC "trained mediator") but never scored | NN-28; D2-13 | `core.neutral_experience_log.outcome_recorded` excluded by CI lint (S6-05) |

### 3.3 Equator ADR Institute — facts and positioning

| Item | Fact as found (21 Oct 2026) | Tag | Consequence |
|---|---|---|---|
| Legal entity | Site equatoradr.com trades as "Equa Trainings" / "Equa.Law", footer: "A Brand owned by Infrabyx Consultancy (OPC) Private Limited", Jaipur; the name "Equator ADR Institute" does not appear on the pages fetched; no CIN or GSTIN displayed | [V] S6 §1.1 | Management treats the Institute as a separate legal entity (D2-17; master L6). The entity name, CIN, GSTIN and merchant account must be confirmed and displayed before any Equator link goes live (assumption A-03; OI-T-10) |
| IMI recognition held | 40-hour programme approved as an IMI **Certified Mediator Training Program (CMTP)**, announced 1 Jun 2024; IMI now calls this tier **Recognized Mediator Training Program (RMTP)**. Graduates may **apply** to be listed as **IMI Qualified Mediators** | [V] IMI announcement | Correct wording is fixed in §3.4 C1 |
| IMI QAP | **No IMI QAP approval found** for Equa/Equator; site shows a "Qualifying Assessment Program" heading | [V] site; absence [U] | QAP wording removed until approval; Equator's own assessment is "designed to IMI QAP standards", and Equator applies to IMI (OI-T-11) |
| Course names | "Grade B Mediators/Arbitrators", "Refresher for Grade A" | [V] | Could imply that buying a course confers an Equator grade — renamed (§3.4 C5) |
| Brand overlap | "Equa.Law" also presents itself as a virtual dispute-resolution centre offering "work for neutrals" | [V] | Master §13(f) and Appendix H WC-41 retire the Equa/Equa.Law brand for the institution; the trainer brand must be kept distinct from any ODR service |
| Platform | Graphy white-label LMS; refund page references equa.graphy.com | [V] | Institute keeps its own checkout and merchant; Equator collects no course fees (S6 §6.3) |
| v3.0 facts (23 Oct 2026; Appendix AF §AF.4.1) | About-page wording on the entity conflicts with the footer; a personal Gmail address sits behind a mailto link; comparison prices are inconsistent; prices displayed in USD only with an ex-GST pattern; a Graphy referral banner; the IMI page dated Jun 2024 was modified 14 Aug 2024; currency of the IMI recognition is open | [V]/[C]/[U] (AF-S31–AF-S34) | Corrections C1–C20 (§3.4) and OI-AF-06/OI-AF-08; referral card cannot show prices until INR prices incl. GST are confirmed |

**Positioning (binding for P10 and P13):**

1. Equator Resolution (ERSPL) **empanels, grades and allocates**; Equator ADR Institute **trains**. Equator's competence assessment (Equator QAP) is open to candidates trained by any provider (IMI QAP criterion 7).
2. At `training_required`, the provider picker shows **≥ 3 recognised providers** (e.g., an IMI RMTP, an MCPC/High Court/LSA programme, CIArb India, and the Institute) in randomised or alphabetical order, never Institute-first by default, with hours, price (INR incl. GST), mode and recognition pulled from the Claims Register.
3. Persistent disclosure on the picker: "{Confirmed legal entity name} is a separate company within the Infrabyx group. Training with it does not affect your grade, empanelment or allocation." *(v3.0: the name "Equator ADR Institute" does not appear on the site, whose operator is shown as Infrabyx Consultancy (OPC) Private Limited; the disclosure must name the confirmed legal entity and stays a placeholder until the Company Secretary confirms it — AF-S31; D3-38.)* If any referral fee exists, its basis is disclosed. Referral fee, if any, is flat per enrolment, never tied to empanelment or allocation; the default is **₹0** and any fee needs Board approval under Companies Act 2013 s.188 and the AB stream RS-22 record going `live` (D3-38) *(v3.1)*.
4. Data sharing: Equator → Institute nothing by default (optional itemised DPDP consent for name, email, mobile); Institute → Equator only a consented credential-verification payload `{certificate_no, holder_name, course_code, hours, completion_date, assessment_result, issuer_signature, status}` — never recordings, scores, attendance or payment data.
5. Institute trainers, coaches and assessors never sit on Equator's empanelment or complaint decisions about their trainees (`conflict_edges.relation = trainer_of`).
6. Related-party hygiene: arm's-length agreement approved by both boards; if directors are common, interest disclosure under Companies Act 2013 s.184 and related-party approval under s.188 as applicable **[K]** (CS action item, OI-T-12).

Full mechanics: Appendix N §9–§10 and S6 §6.3. This section adds no further requirements to avoid duplication.

### 3.4 Required corrections to the Institute's website (equatoradr.com)

These corrections are for the **Institute's** site and are a **pre-condition** for flag `academy.institute_referral` (OFF). Corrections to **equatorresolution.in** are in Appendix H §5 and are not repeated (see in particular WC-28 — no claim of alignment with MCI, ACI or IMI accreditation — and WC-41 — retire "Equa"/"Equa.Law" for the institution; training arm named only "Equator ADR Institute").

| # | As published | Problem | Action | Replacement copy (paste-ready) |
|---|---|---|---|---|
| C1 | "The IMI Accredited and Certified Mediation Training Program"; store category "IMI Certified Mediation Training" | IMI *recognises* training programmes and *certifies* mediators; the programme is an RMTP, leading to eligibility for **IMI Qualified**, not Certified | REPLACE | "40-hour mediation training recognised by the International Mediation Institute (IMI) as a Recognized Mediator Training Program. Graduates may apply to IMI to be listed as IMI Qualified Mediators. IMI Certified Mediator status requires separate assessment by an IMI Qualifying Assessment Program and at least 200 hours or 20 mediations of experience." |
| C2 | Heading "Qualifying Assessment Program" | No IMI QAP recognition found; "QAP" is IMI's term of art | REMOVE (or rename) | "Practice Assessment (not an IMI Qualifying Assessment Program)" |
| C3 | "Be a Certified Mediator"; "certified and accredited mediators through EQUA" | Implies statutory/professional status; no mediator certification body operates in India (MCI has no regulations) | REPLACE | "Certificate of Completion — 40-hour Mediation Training (Equator ADR Institute)." |
| C4 | "Various dispute resolution platforms have accredited this training, especially Equa.Law" | Self-accreditation; no third party named | REMOVE | — (name only verifiable recognitions, with link and date verified) |
| C5 | "Mediation Training for Grade B Mediators", "Refresher Training for Grade A Mediators/Arbitrators" | Implies a link to Equator panel grades; risk of "buying a grade" (NN-28) | REPLACE | "Advanced Practitioner Course" / "Senior Practitioner Refresher". Add: "Completion does not confer any panel grade or empanelment with any institution." |
| C6 | "ISO 9001:2015; ISO 27001:2018"; "meets GDPR, CCPA, HIPAA and SOC 2 Type 1" | No ISO/IEC 27001:2018 edition exists (2013, 2022); HIPAA is a US health law; SOC 2 is an attestation report, not a certification | REPLACE or REMOVE | Show certificate number, certification body and validity for each ISO certificate held; otherwise remove. For data protection: "We process personal data under the Digital Personal Data Protection Act, 2023. Privacy notice: [link]." |
| C7 | USD-only prices, no GST, blanket "non-refundable" | GST at 18% (SAC 999293) must appear for Indian learners; blanket no-refund for a live course risks an unfair contract term (Consumer Protection Act 2019 s.2(46)) | REPLACE | INR price incl. GST for Indian learners (USD for overseas, stated as such); "Full refund before the first live session; pro-rata refund before session 2; no refund after session 2." (Board to approve) |
| C8 | Lorem-ipsum "Mediation Training Centers"; empty Membership page | Unfinished content | REMOVE until live | — |
| C9 | Course page "industry-ready" section on contract review | Copy does not match course | REPLACE | Course-specific learning outcomes and published hours |
| C10 | Trainer bios referencing Supreme Court / Australian standards | Acceptable only as trainer facts, not course endorsements | KEEP with edit | "[Trainer] holds …" — never "this course is approved by …" |
| C19 (was C11; renumbered v3.0, Appendix AF §AF.4.3) | Specialisation and country add-on courses state no hours | Equator endorsements need minimum hours (S6 §4.1) | ADD | Published hours, assessment component and verifiable certificate per course |
| C20 (was C12; renumbered v3.0) | No public certificate verification | Equator onboarding needs issuer verification | ADD | `/verify/{certificate_no}` page or signed verifiable credential, with revocation list |

Verification of corrections: `legal_reviewer` re-fetches the site and records a `growth.benchmark_entries` row per correction (`subject_code = 'trn.equator_adr_institute'`, `attribute_code = 'correction.C1'…`). The referral flag may be switched ON only when **all corrections C1–C20** (Appendix AF §AF.4.3: C1–C10 above, Appendix N §9 C11, [RB] C12–C18, C19 and C20 above) are recorded as corrected **and** the operating entity, CIN and GSTIN are displayed on the site (D3-38; FR-P10-V3-AF01). *v3.0 (23 Oct 2026): the v2 numbering C11/C12 collided with Appendix N §9 C11 and the new C12–C18 and is replaced; the earlier gate "C1–C8 and C12" is withdrawn.*

### 3.5 Equator's own assessment route (summary; detail in Appendix N)

| Item | Position |
|---|---|
| Name | **Equator Qualifying Assessment** (internal code `EQ-QA`) — public copy: "designed to the International Mediation Institute's assessment-programme standards" |
| IMI status | Not yet an IMI QAP. Equator applies for **IMI QAP** and an **ODR-QAP** variant using the 10-point readiness checklist (S6 §6.2) |
| Copy before approval | "Equator is not yet an IMI Qualifying Assessment Program." |
| Copy after approval | "Equator's assessment is recognised by IMI as a Qualifying Assessment Program; successful candidates with at least 200 hours or 20 mediations may be submitted to IMI for Certified Mediator status." |
| Logo | IMI QAP logo only on the QAP programme page, never on panel or directory pages |
| Claims Register lint | Blocks "accredited by IMI", "IMI certified course", "MCI registered", "QAP" unless a verified claim exists (S6-16) |

---

## 4. Reliance Jio AI evaluation (integration evaluation, not a commitment — D2-23)

**Posture in one line.** Use Jio as a **carrier** (SIP trunk, DLT, JioCX SMS/RCS, branded caller ID); evaluate **Jio Haptik** through an RFP as a challenger for voice and WhatsApp agents; keep **JioBrain** and **Reliance Enterprise Intelligence (REIL)** on a watch-list until a public API, price list, India-residency commitment and a data-processing agreement exist. The primary stack in master §8 does not change.

### 4.1 Offering map (as of 21 Oct 2026)

| Offering | Owner | Capability | Availability | API / docs status | Data residency | Pricing status | Tag |
|---|---|---|---|---|---|---|---|
| **JioBrain** | Jio Platforms | "Suite of AI tools and platforms" for Reliance's own operations, to be offered to enterprises later (47th AGM, Aug 2024) | Internal-first; no enterprise contracting channel found | **None published.** A single secondary article (Startupory, 3 Jun 2026) claims public APIs, 8B/70B/175B models, ₹0.18 per 1K input tokens, SOC 2 Type II, "MeitY empanelment" — no primary source; not mentioned in 49th AGM coverage (19 Jun 2026) | Unknown | Unknown | [V2] announcement; claim **[U — do not rely]** |
| **Jio AI Cloud** | Jio Platforms | **Consumer** cloud storage (up to 100 GB free for Jio users from Diwali 2024) — not compute or an AI API | Live (consumer) | n/a | n/a | Free tier | [V2] |
| **Reliance Intelligence Ltd** | Wholly owned RIL subsidiary (48th AGM, 29 Aug 2025) | Umbrella AI company: data centres, cloud, enterprise software, consumer apps; priority sectors education, healthcare, agriculture | Corporate vehicle | n/a | n/a | n/a | [V2] |
| **REIL — Reliance Enterprise Intelligence Ltd** | JV: Reliance Intelligence 70% / Facebook Overseas Inc. (Meta) 30%; ~₹855 crore initial commitment; announced 25 Oct 2025 | Enterprise AI PaaS on **Meta Llama**; pre-configured solutions for sales, marketing, finance, IT operations, customer service; cloud, on-premise or hybrid | Announced; no public product | **None published** | Not stated | Not published | [V2] press; [V] Meta newsroom (scope) |
| **Google Cloud partnership** | RIL / Google | Dedicated AI cloud region at Jamnagar (announced 29 Aug 2025); Gemini (Google AI Pro) consumer bundle for Jio users (49th AGM) | Infrastructure 2026–27; consumer bundle live | No Equator-consumable "Reliance–Google" enterprise API; Equator would buy Vertex AI from Google directly | Region details [U] | Google list prices | [U]/[V2] |
| **Jamnagar AI compute** | RIL / Reliance Intelligence | First ~120 MW AI-ready capacity targeted end-2026; Nvidia GB300 fleet | 2026–27 | n/a | India | n/a | [V2] |
| **Jio Haptik** | Reliance Jio (acquired 2019, ~US$100M) | Agentic AI platform: **voice AI agents** (support, bookings, follow-up calls, lead qualification), **WhatsApp AI agents**, CRM/back-end integrations; **Interakt** WhatsApp-first CRM and marketing suite (50,000+ business users); "AI for All" for SMBs from ₹10,000 (3 Sep 2025); SOLO (8 Jul 2026); 22 Indian languages | **Live, sales-led** | No public docs found on BYO-LLM, residency, webhook signing, recording export, consent controls | **Not stated** | SMB entry ₹10,000; enterprise by quote | [V2] |
| **JioCX** | Jio Business CPaaS | SMS (high-volume), Email, Voice, **RCS**, WhatsApp Business, Alerts, EasyPhone (cloud virtual number), EasyListing, **Verify (branded caller ID)** | **Live, demo-led** (hello@jiocx.com) | No public API reference, DLT detail or price list on the product page; via an orchestrator: Org Name, Username, Password, Sender/Header, **DLT Entity ID**, Route (Transactional / Promotional / OTP); **delivery reports off by default — Jio must enable a callback URL** | Not stated (Indian TSP) | "Pay only for what you send"; no public rates | [V] jio.com; [V2] fyno.io |
| **Jio Business SIP trunk, IP Centrex, Toll-Free, JioMeet** | Jio Business | SIP Trunk 10–10,000 simultaneous sessions; IP Centrex; toll-free; JioMeet up to 1,000 participants | **Live** (CAF + enterprise KYC + MSA + service orders) | Provisioning and self-care portal; no voice-bot API; JioMeet has no published embed/recording-export API | India (TSP) | By order form | [V] jio.com/business |
| **Jio DLT** | Reliance Jio (TSP) | Principal Entity, header, template and consent registration under TCCCPR 2018 as amended | **Live** | Operator portal | India | Registration fees per operator | [K] (P07 FR on `core.dlt_registry`) |
| **Marketing / adtech** | Haptik Interakt; JioStar/JioHotstar ads; JioCX Email | WhatsApp marketing CRM; video ad inventory; email | Live | Interakt docs [U]; ads via media buying | Not stated | Commercial | [V2] |
| **AI research & drafting** | REIL "pre-configured solutions"; JioBrain | Not documented for legal research or drafting | Not available | None | Unknown | Unknown | [U] |
| **Jio AI Call Agent** (consumer) | Jio (49th AGM, 19 Jun 2026) | **In-network AI on ordinary calls for Jio subscribers**: transcribes, identifies up to 10 speakers, summarises, extracts actions | Rolling out to consumers | n/a — not an Equator product, but **affects Equator's calls** (§4.9) | Not stated | Consumer | [V2] |

### 4.2 Fit score per Equator need (pre-RFP, public evidence only)

Scale 0–5: **5** = contractable now with documented API, India processing in writing and NN-12/DPDP controls verified; **3** = live and contractable but key controls undocumented; **1** = announced, no product; **0** = not offered. Scores are product judgements, not facts, and are recomputed after the RFP (§4.6).

| Equator need (R-08) | Best Jio / Reliance option | Jio fit | Why | Best pack option (master §8) | Pack fit | Decision |
|---|---|---|---|---|---|---|
| **Agent calling** (inbound helpline, case status, intake triage; outbound notice explanation, consent capture, slot booking) | Jio Haptik voice AI agents | **2** | Capability and 22 languages exist; no published BYO-LLM, India-only processing, recording export or non-skippable AI disclosure | ElevenLabs Agents (India residency, Enterprise) with Claude on Bedrock India via OpenAI-compatible proxy; Sarvam voice agents fallback | 4 | **RFP challenger** (FR-P07-V2-T05/T08) |
| **Automated calling** (reminders, notice-served confirmations, payment-link calls — PSTN carriage and IVR) | Jio SIP trunk; JioCX Voice; Toll-Free | **4** (SIP) / 3 (JioCX Voice) | Jio is the largest TSP; SIP trunk live; DLT on Jio is mandatory anyway; adds carrier diversity and CLI resilience | Exotel India cluster (`api.in.exotel.com`, AgentStream) primary; Plivo fallback | 4 | **Adopt Jio SIP as second PSTN carrier** behind flag (FR-P07-V2-T01) |
| **SMS / RCS** (DLT notices, OTP, reminders) | JioCX SMS/RCS | **3** | On-net delivery to Jio subscribers; DLR callback must be enabled; no public API doc | MSG91 primary; Gupshup/Kaleyra fallback | 4 | **Secondary route** (FR-P07-V2-T03) |
| **Branded caller ID** | JioCX Verify | **3** | Reduces call rejection for Jio subscribers; coverage on other networks unconfirmed | TSP branded CLI / Truecaller for Business | 3 | **Pilot** (FR-P07-V2-T04) |
| **Marketing tools** | Interakt; JioStar ads; JioCX Email | **2** | Usable only for consented marketing leads in the `growth` schema; Interakt is a marketing CRM and must never receive respondents (NN-16) | P13 stack (CMS, CRM with DPDP purpose consent) | 4 | **Optional channel, no integration dependency** (FR-P07-V2-T09) |
| **AI research** (legal research over verified corpus) | REIL Llama PaaS; JioBrain | **0–1** | No documented product, residency or no-training terms | Claude on Bedrock India over Equator's verified-citation corpus (Appendix M; NN-25) | 4 | **Watch-list only** (FR-P11-V2-T02) |
| **Document drafting** (pleadings self-help, settlement terms, award skeletons) | REIL pre-configured solutions | **0–1** | Not documented; drafting must be grounded, attributable, verified-citation-only (NN-25) and human-signed (NN-01) | Claude on Bedrock India + LawDocs templates (Appendix M, P06) | 4 | **No** |
| Indic STT/TTS/translation | Haptik (inside its agent); JioBrain (claimed) | 1 | Not separable as an API | Sarvam (STT ₹30/h; Translate ₹20/10K chars; Bulbul v3 TTS ₹30/10K chars; Vision ₹0.5/page) [V]; Bhashini fallback | 4 | Sarvam primary |
| Video hearings | JioMeet | 1 | No embed, recording-export or watermark API | LiveKit (India region) | 4 | **No** |

### 4.3 Risk register

| # | Risk | Likelihood × impact | Control |
|---|---|---|---|
| JR-01 | **No DPA / no documented API** for JioBrain, REIL and (publicly) Haptik — processor obligations under DPDP Act 2023 s.8(2) and Rules 2025 cannot be evidenced | High × High | Go/no-go gates G1–G4 (§4.6); `provider_routing` cannot reference a vendor without `eng.vendor_evaluations.status = 'approved'` (FR-P07-V2-T05) |
| JR-02 | **Conflict: Reliance group entities as parties** (Jio Financial Services, Jio Payments Bank, Reliance Retail, Reliance general/health insurance JVs, Jio as telecom service provider in consumer matters) while a Reliance company processes case content | Medium–High × High (neutrality, NN-16, appearance of bias) | Vendor conflict register; per-case vendor exclusion when any party's `group_code` matches the vendor's; disclosure in sub-processor register; written firewall and audit right (G5; FR-P07-V2-T06) |
| JR-03 | **Residency not committed in writing** (Haptik, JioCX); Meta JV raises cross-border model and telemetry questions for REIL | Medium × High | India-only processing in writing including inference, support access and backups (G3); DPDP s.16 transfer record if any element leaves India (NN-15) |
| JR-04 | **Training on customer data** (Llama derivatives, agent tuning) | Medium × High | Contractual no-training clause; deletion within 30 days of termination (G4) |
| JR-05 | **Telecom non-compliance**: undeclared A2P CLI, 140-series use, missing DLT template binding, calls outside 08:00–19:00 for borrower contact (09:00–18:00 for microfinance loans, LR-RBI-005) *(v3.1)*, no consent registration | Medium × High (TCCCPR (Third Amendment) Regulations 2026, No. 05 of 2026, 18 Sep 2026; NBFC RBC (Third Amendment) Directions 2026) | Platform-level enforcement remains Equator's `comms` module (NN-12) regardless of vendor; vendor must evidence DLT binding and A2P declaration (G6); RT-07 |
| JR-06 | **Unverified marketing claims** about JioBrain (Startupory) entering Equator copy or procurement decisions | Medium × Medium | Claims Register blocks; benchmark entry tagged [U]; quarterly watch-list review (FR-P11-V2-T02) |
| JR-07 | **Consumer-side network AI transcription** (Jio AI Call Agent) captures confidential mediation calls on PSTN | Medium × High for FAM, POSH, INS-health | Confidentiality script; Rules clause; VoIP-first for sealed-tier sessions (§4.9; FR-P07-V2-T07) |
| JR-08 | **Delivery-report gaps** (JioCX DLRs off by default) weaken proof of service | Medium × Medium | Route not activatable until DLR callback with authentication is live and tested (FR-P07-V2-T03) |
| JR-09 | **Lock-in** on numbers and agent definitions | Low–Medium × Medium | Number portability for toll-free/virtual numbers; agent definitions held provider-neutral in `core.voice_agents` (P07 FR-P07-22) |
| JR-10 | **Market-power dependency** if Jio is both majority carrier and AI vendor | Low × Medium | Dual-carrier policy: no single TSP carries > 70% of Equator's outbound minutes in any month (config `telephony.max_carrier_share = 0.70`) |

### 4.4 Recommended posture per offering

| Offering | Posture | Condition to change posture |
|---|---|---|
| Jio Business SIP trunk | **Adopt** as second PSTN carrier (flag `telephony.jio_sip.enabled` OFF until contracted and tested) | Contract (CAF/MSA), DLT linkage, failover test |
| Jio DLT | **Mandatory** — Principal Entity registration (already P07) | — |
| JioCX SMS/RCS | **Adopt as secondary route** (flag `messaging.jiocx.enabled` OFF) | API docs + authenticated DLR callback + telemarketer status confirmed (OI-T-17) |
| JioCX Verify | **Pilot** (flag `voice.branded_cli.jiocx.enabled` OFF) | Pilot shows answer-rate uplift ≥ 10% with zero complaints of impersonation |
| Jio Haptik voice/WhatsApp agents | **RFP challenger** | Passes G1–G10 and the bake-off; BYO-LLM via Equator's Bedrock proxy |
| Haptik Interakt | **Marketing-only, optional**; never for respondents | NN-16 unchanged |
| JioBrain | **Watch-list** | Primary-source API docs, DPA, residency, no-training, firewall |
| REIL | **Watch-list** | As JioBrain, plus clarity on Meta's data access |
| Google Cloud (Jamnagar region) | **No change** (AWS ap-south-1/ap-south-2 per master §4.1) | Re-assess in 2027 for sovereign-cloud tenders |
| JioMeet | **Reject** for hearings | Published embed/recording-export/watermark API |

### 4.5 RFP checklist — 12 questions (send to Jio Haptik, JioCX and, when contractable, REIL)

Every answer must be written and incorporated into the DPA or order form. The checklist is stored as `eng.rfp_questions` (versioned) and responses as `eng.vendor_rfp_responses`.

| # | Area | Question | Pass criterion |
|---|---|---|---|
| Q1 | Residency | Where are audio, transcripts, prompts, embeddings, logs and backups stored **and processed**, including model inference and support access? Name regions and sub-processors. | India only; named regions; named sub-processors; no support access from outside India without Equator approval |
| Q2 | Training | Is any Equator data used to train, fine-tune or evaluate any model, including Meta Llama derivatives? | Contractual no-training; deletion within 30 days of termination with certificate |
| Q3 | BYO-LLM | Can the agent call Equator's OpenAI-compatible endpoint (Claude on Bedrock India) with function calling, so the vendor's own LLM never sees case content? | Supported and documented |
| Q4 | API maturity | Public or NDA API reference, sandbox, rate limits, idempotency keys, **HMAC-signed webhooks** with timestamp tolerance | Signed webhooks; sandbox; idempotency |
| Q5 | Telecom compliance | DLT header/template binding; consent registration on the operator consent platform; **A2P CLI declaration** under TCCCPR (Third Amendment) Regulations 2026; DND scrubbing; calling-hour windows enforced per contact; support for **lender-number (1600-series) mode** with tenant authorisation and for Equator's declared A2P DIDs; confirmation that **140-series is never used** | Platform enforces each item and exports logs (RT-07; NN-12) |
| Q6 | AI disclosure | Configurable, non-skippable first-utterance disclosure ("This is an automated assistant from Equator Resolution… this call is recorded… say 'stop' to opt out") in every enabled language | Yes; cannot be disabled by prompt or script |
| Q7 | Recording and evidence | Dual-channel recording export, SHA-256 per file, retention control, deletion API, export within 10 minutes of call end | Yes (to meet P07 S3 Object Lock copy) |
| Q8 | Conflict firewall | Can any Reliance group entity that is a party to an Equator case access case data, logs, analytics or model outputs? | Written firewall; named personnel controls; audit right; breach = termination right |
| Q9 | Security | ISO/IEC 27001, SOC 2 Type II, CERT-In empanelled audit, 6-hour CERT-In incident reporting (CERT-In Directions 28 Apr 2022), 180-day log retention | All evidenced with certificate numbers |
| Q10 | DPDP | Processor terms under DPDP Act 2023 s.8(2); breach notice to Equator within 24 hours so Equator can meet Rule 7 (DPDP Rules 2025, G.S.R. 846(E), 13 Nov 2025) | Yes |
| Q11 | Pricing | Unit prices: per minute (voice), per conversation (WhatsApp), per message (SMS/RCS), per verified call (Verify); minimum commitments; overage | Transparent unit pricing in INR |
| Q12 | Exit | Data export formats; agent-definition export; number portability for toll-free and virtual numbers; transition assistance | Yes, within 30 days |

### 4.6 Scoring model and go/no-go gates

**Weighted RFP score (/100):** residency 20 · telecom compliance 15 · API maturity 15 · Indic quality (WER/MOS on Equator's test set) 15 · cost 10 · BYO-LLM 10 · neutrality firewall 10 · exit 5. Pre-RFP public-evidence scores (product judgement): ElevenLabs ~80; Sarvam ~78; Exotel ~75; JioCX ~55; Jio Haptik ~45; REIL/JioBrain not scorable. A vendor is shortlisted at ≥ 70 **and** all blocking gates passed.

| Gate | Requirement | Evidence | Blocking for | Owner |
|---|---|---|---|---|
| G1 | Written API specification + sandbox | Docs, sandbox credentials | All AI and messaging uses | `platform_admin` |
| G2 | DPA with s.8(2) processor terms and 24-hour breach notice | Signed DPA | Any case data | `dpo` |
| G3 | India-only processing in writing (incl. inference, support, backups) | DPA schedule | Any case data; sealed tier never without it | `dpo` |
| G4 | No-training clause + deletion certificate | DPA | Any case data | `dpo` |
| G5 | Conflict firewall + audit right (Reliance-group vendors) | Firewall letter; audit clause | Any Reliance-group vendor | `legal_reviewer` |
| G6 | Telecom compliance evidence (DLT binding, A2P declaration, consent platform, DND, calling hours, no 140-series) | Operator confirmations; logs | Voice, SMS, RCS | `compliance_officer` |
| G7 | Security attestations (ISO 27001, SOC 2 Type II, CERT-In audit) | Certificates/reports | All | `platform_admin` |
| G8 | Bake-off: WER ≤ pack baseline + 2 points per language; MOS ≥ 4.0; p95 turn latency ≤ 1.5 s; disclosure compliance 100% | Eval run ID (P11 harness) | Voice agents | `quality_officer` |
| G9 | Transparent unit pricing | Order form | Commercial approval | `finance_controller` |
| G10 | Exit and portability | MSA clause | Commercial approval | `legal_reviewer` |
| G11 *(v3.1)* | Replaceability (NN-40): the vendor sits behind its port with a declared system of record per data category, a documented field mapping, a tested export/import and a named fallback adapter; a migration rehearsal has run in staging on synthetic data (X-66(c)) | Rehearsal report; port contract tests | Activation of any adapter | `tech_lead` |

Go = G1–G11 passed and score ≥ 70 → `eng.vendor_evaluations.status = 'approved'`, then maker–checker activation of the adapter in `core.provider_routing`. No-go on any blocking gate → `rejected` or `watch` with re-review date.

**Keeping approvals current *(v3.1)*.** Each approved evaluation stores the expiry of every attestation and contract it relied on (G2–G4 DPA, G6 operator confirmations, G7 certificates/reports, G10 MSA term). Thirty days before any expiry a re-review task goes to the gate owner; if the evidence is not renewed by the expiry date the evaluation moves to `watch`, new tenants cannot be routed to the adapter, and existing routing continues for 30 days while the fallback adapter (G11) is prepared — never an abrupt cut-off for live matters. A sub-processor change notice (Appendix Q PC-22, 30 days) is raised whenever an approved vendor adds a sub-processor or processing location. KPIs: approved vendors with all evidence current = 100%; days from expiry to renewal (watch).

### 4.7 Comparison with the pack's chosen vendors

| Criterion | Jio Haptik | JioCX | Jio SIP trunk | ElevenLabs Agents | Sarvam | Exotel / Plivo | Gupshup | Claude via Amazon Bedrock |
|---|---|---|---|---|---|---|---|---|
| Role in pack | RFP challenger (voice/WhatsApp agents) | Secondary SMS/RCS; branded CLI pilot | Second PSTN carrier | **Primary voice agent** | Indic STT/TTS/translation/OCR; voice-agent fallback | **Primary CPaaS** (Exotel); fallback (Plivo) | **WhatsApp BSP** (Meta Cloud API) | **Primary LLM** |
| India residency | Not stated | TSP (India) | India | India Data Residency (Enterprise, launched 30 Jul 2025; `api.in.residency.elevenlabs.io`); **custom LLM and post-call webhooks may process outside region** — Equator's LLM proxy keeps inference in India [V RES_A4 Q15] | India-hosted [V] | Exotel India cluster `api.in.exotel.com` [V]; Plivo region [U] | Meta Cloud API **Local Storage `IN`** for data at rest; data in use may be processed outside for up to 60 minutes [V RES_A4 Q27] | **In-country inference in India** (announced 5 Oct 2026; Opus 5, Sonnet 5, Haiku 4.5; Mumbai + Hyderabad); Titan Text Embeddings V2 in-Region ap-south-1/ap-south-2 [V RES_A4 Q14] |
| API maturity | Not public | Not public | Provisioning | Documented; HMAC-signed post-call webhooks (`ElevenLabs-Signature`) | Documented; auth `api-subscription-key`; callback auth open | Documented; AgentStream WebSocket (slin 8 kHz); callback signing open; Plivo `X-PH-` SIP headers [V] | Documented via Meta; Gupshup v1 vs v3 auth and callback signing open [U] | Documented (Bedrock) |
| BYO-LLM | Unknown | n/a | n/a | Yes (OpenAI-compatible custom LLM) | Own models (Sarvam 105B ₹15/₹60 per 1M tokens) | n/a | n/a | n/a (is the LLM) |
| Indic languages | 22 (claimed) | n/a | n/a | Multilingual; bake-off per language | 22 Indic + English (Vision); strong Indic STT/TTS | n/a | Templates any language | Multilingual; Indic quality per eval |
| Telecom compliance controls | Unknown | DLT Entity ID, routes; DLR off by default | DLT on Jio | Via Exotel SIP (Equator enforces NN-12) | Via SIP/CPaaS | Telemarketer on DLT linked to Equator PE | WhatsApp template approval | n/a |
| Neutrality concern | **Reliance group** | **Reliance group** | Reliance group (carrier only; no content access beyond carriage) | None known | None known | None known | None known | None known |
| Pricing transparency | Partial (SMB ₹10,000) | No public rates | Order form | Public tiers; Enterprise by quote | **Public** [V] | Public/quote | Public/quote | Public (Bedrock) |
| Decision | RFP | Secondary + pilot | Adopt (flagged) | Keep primary | Keep | Keep | Keep | Keep primary |

### 4.8 Vendor conflict firewall (design)

1. `eng.vendor_groups(vendor_code, group_code, group_name)` — e.g., `jio_haptik`, `jiocx`, `jio_sip` → `group_code = 'reliance'`.
2. `core.organisations.group_code` populated at KYB from MCA/LEI data or declared by the enterprise tenant; registrar can set it on documented grounds.
3. Routing rule `RR-VND-01`: when a case is created or a party is joined, if any party's `group_code` equals a content-processing vendor's `group_code`, the case gets `provider_overrides` excluding that vendor for **content-processing ports** (`VOICE_PORT`, `MESSAGING_PORT` for WhatsApp agents, `LLM_PORT`, `TRANSCRIPTION_PORT`, `TRANSLATION_PORT`, `DOC_AI_PORT`). Pure carriage (`TELEPHONY_PORT` PSTN trunk; DLT) is permitted but logged.
4. Event `equator.integrations.vendor_conflict.applied.v1` (case ID, vendor, port, rule version); audit entry; sub-processor register shows the group relationship.
5. Any party may request a vendor switch for its case (`POST /v1/cases/{caseId}/provider-overrides`, role `party`/`representative`, reason optional); granted automatically for content-processing ports where a fallback exists.

### 4.9 Consumer-side network AI (Jio AI Call Agent) — mitigations

| Measure | Text / rule |
|---|---|
| Session script (mediation, conciliation, caucus by phone) | "Please do not record or use call-transcription or AI assistants on this call. This includes features provided by your phone network." |
| Equator Mediation Rules confidentiality clause | Covers "recordings, transcripts or summaries generated by any device, application or network service" |
| Channel policy | Sealed-tier sessions (FAM safety, POSH, INS-health) default to in-app VoIP/WebRTC; PSTN bridge only on the party's request with the script read and acknowledged |
| Voice-agent calls | First-utterance disclosure unchanged (NN-12); no substantive offer relay inside mediation (X-05) |

---

## 5. Differentiation summary — how Equator v2 beats the field

Each row is a **build commitment**, not marketing copy; public wording comes only from Appendix H §6 (safe-claims library) and Appendix P, through the Claims Register. KPIs and targets: Appendix H §2.

| # | Gap in the field (evidence) | Who leaves the gap | Equator v2 feature | Implementing appendix / phase | Master ref |
|---|---|---|---|---|---|
| DX-01 | Lender-triggered appointments under High Court scrutiny (*Radiance Galore v Yes Bank*, Bom HC 17 Jul 2025; *CORE*, 8 Nov 2024; *Bhadra International*, SC 5 Jan 2026) | Presolv360, AdresNow; most ODRIs | Lender-trigger block, post-dispute s.12(5) waiver capture, rotation allocation, Defensibility Score, Independence Evidence Pack | P03, P09; App. N §6 | D1; NN-03 |
| DX-02 | No suitability tool that says "ADR is not right for you" and names the free forum and last date | All seven Indian ODRIs; claim-assistance players | Dispute Explorer v2 with exclusions (criminal, non-arbitrable), signposting and dated forum cards | App. K §1–§4; V1–V6 §5 | NN-06, NN-20, NN-24 |
| DX-03 | Success fees on retail insurance claims against a free Ombudsman route | Insurance Samadhan (20% + GST, site Oct 2026) | Free-route-first INS pathway; flat fees only; insurer-paid B2B mediation | V4; App. O | NN-18; X-07 |
| DX-04 | E-stamp/e-sign without a settlement-money loop | Jupitice | Offer → MSA → e-stamp + e-sign → UPI AutoPay/escrow with trustee → reconciliation → default escalation; no pass-through | P05, P06 | D2; NN-09, NN-13 |
| DX-05 | AI drafting without grounding or symmetry | Webnyay Draft-Your-Self; Jupitice AI | AI Pleadings Studio: source anchors, verified citations only, gaps shown, same tool for both sides, user is author | App. M; P11 | NN-25; D2-07 |
| DX-06 | AI-assisted outcomes without party validation | CourtCorrect (outcome suggestions) | Party-validated AI summaries; human neutral signs; AI never values or predicts | P11; App. E | D3; NN-01 |
| DX-07 | Opaque or partial pricing; non-refundable fees; future-matter bars | Jupitice, Webnyay, CADRE, JustAct, CORD (amounts); Presolv360 (non-refundable); Sama (bar) | Calculator-driven GST-inclusive quotes, API quotes, stage refunds, no dark patterns | App. B, O; P05, P13 | D7; NN-29 |
| DX-08 | Neutral selection by "past performance" or outcomes; paid visibility | Webnyay (AI selection); marketplaces | Published grades A/B/C, hard filters → rotation → capped process-only Quality Index; no paid listings in the institutional directory or allocation (any Marketplace sponsorship is separate and labelled, NN-34) *(v3.1)* | App. N §2–§6 | NN-28; D2-12–D2-14 |
| DX-09 | Institutional governance mixed with commercial management | Most private ODR platforms | Equator Institutional Committee (majority external) with sub-committees; reasoned, logged decisions | App. N §1 | D2-15 |
| DX-10 | No case-status transparency comparable to court websites | All Indian ODRIs | Case-status portal: papers filed, dates, interim/final orders, parties; ICS calendars; verification URLs | App. R §1–§2 | R-27 |
| DX-11 | No consent-based publication of awards or challenge decisions in India | Indian ODRIs and IIAC/MCIA | Consent-only publication with redaction; redacted challenge decisions; Annual Transparency Report with service-level times | App. R §3; App. N | NN-26; D2-10 |
| DX-12 | Weak handling of handwritten, screenshot and multilingual evidence | All | Type copies with originals preserved, OCR router, 22 + 6 language translation labelled, certified-translation workflow, BSA s.63 certificate | App. L | NN-10, NN-32 |
| DX-13 | Representatives without scoped authority | All | Letter of Authority / Vakalatnama with scope, settlement limit, revocation | App. S §4 | NN-27 |
| DX-14 | Separate persona logins and dashboards | Most | Distinct portals and dashboards per persona on one identity backbone; Aadhaar OVSE/DigiLocker/PAN/MCA onboarding | App. S §2–§6 | D2-05, D2-06 |
| DX-15 | Training seller and empaneller combined | Training-platform hybrids | Equator QAP separate from the Institute; ≥ 3 providers; no conditionality | §3 above; App. N §9–§10 | D2-17 |
| DX-16 | Regulator-clock grievance → ODR bridge missing | Webnyay (grievance only), helpdesks | GRM SaaS with RB-IOS 2026, IO, SCORES, IR Code GRC, UGC SGRC clocks and one-click escalation | P09 | D5 |
| DX-17 | International matters priced in one currency, no India-specific gates | MCIA (INR only); private ODRIs | Multi-currency invoicing with FX snapshot; sanctions/UBO/FEMA/DPDP s.16 gates; procedure tiers; AMA; enforcement cards | V6; App. B | D7; NN-19 |
| DX-18 | Voice outreach without telecom-grade compliance | Market practice in collections | DLT PE, A2P CLI declaration, 1600 lender-number mode, quiet hours, disclosure, recording retention; dual-carrier incl. Jio | P07; §4 | D9; NN-12; M-05 |

**Credibility gaps Equator must still close** (carried from Appendix H §1.1 read-across, updated): SEBI/MII status (not pursued while `SEC` is OFF), panel depth (competitors claim 3,000+ neutrals — company claims), ISO/IEC 27001 certification (Webnyay holds 2022), judicial advisory council (Presolv360), published rules at launch matching CORD Rules 2.0, and an IMI QAP approval (§3.5).

---

## 6. Open items

| ID | Item | Why it matters | Owner | Closes before |
|---|---|---|---|---|
| OI-T-01 | Manual capture of Jupitice (and CORD) dispute category lists (= OI-S3-01) | App. K §7 roadmap; comparative claims | `growth_manager` | P13 content freeze |
| OI-T-02 | Current ClaimBuddy and Insurance Samadhan fee pages (9% figure is from 2020) (= OI-S3-02) | INS comparison copy | `growth_manager` | P08d go-live |
| OI-T-03 | First quarterly review-mining run (PI-CMP-05) | FAQ and microcopy | `growth_manager` | P13 |
| OI-T-04 | CORD Rules 2.0 fee tiers (amounts) | Fee benchmark | `growth_manager` | Board fee approval |
| OI-T-05 | Webnyay IFSCA / GIFT City authorisation claim | INT positioning | `legal_reviewer` | P08f |
| OI-T-06 | ICC 2026: initial CMC deadline (20 vs 30 days); 2026 fee scale; TPF and scrutiny article numbers | V6 and App. N references | `legal_reviewer` | P08f |
| OI-T-07 | HKIAC Art. 45 publication wording; MCIA Rules 2025 content and in-force date; DIAC 2022 article numbers; SIAC, HKIAC and MCIA panel admission criteria | Institution benchmark accuracy | `legal_reviewer` | P13 publication of any comparison |
| OI-T-08 | Which Indian bodies hold an IMI QAP (IIAM reported [U]) | Provider picker accuracy | `panel_manager` | P03 |
| OI-T-09 | AMDRAS commencement/transition dates; IMI QAP application fees | Credential register | `panel_manager` | P03 |
| OI-T-10 | Equator ADR Institute legal entity, CIN, GSTIN, merchant account (Equa Trainings / Infrabyx Consultancy (OPC) Pvt Ltd vs "Equator ADR Institute") | D2-17; A-03; referral flag | Company Secretary | P10 |
| OI-T-11 | Equator IMI QAP and ODR-QAP application pack (S6 §6.2 checklist) | §3.5 copy switch | `quality_officer` | Post-P03 |
| OI-T-12 | Related-party review of any ERSPL–Institute referral agreement (Companies Act 2013 ss.184, 188 as applicable) | Governance | Company Secretary | Before referral flag ON |
| OI-T-13 | Institute website corrections C1–C20 verified (Appendix AF §AF.4.3) | Referral flag pre-condition | `legal_reviewer` | Before referral flag ON |
| OI-T-14 | INT admin cap re-benchmark (Appendix B USD 50,000 vs IIAC USD 15,000; S5 suggests USD 25,000–35,000) | Board fee approval (M-01) | `finance_controller` | Board approval of INT card |
| OI-T-15 | JioBrain / REIL primary-source documentation; confirm or refute the Startupory claim of 3 Jun 2026 | Watch-list | `platform_admin` | Quarterly |
| OI-T-16 | Jio Haptik documentation: BYO-LLM, residency, webhook signing, recording export (RFP Q1–Q12) | RFP | `platform_admin` | P07 RFP close |
| OI-T-17 | JioCX API reference, DLR/webhook security; whether JioCX is a registered Telemarketer on DLT | Secondary route activation | `compliance_officer` | Before `messaging.jiocx.enabled` ON |
| OI-T-18 | Counsel: whether using a vendor whose group company is a party requires disclosure to the other party or neutral, or consent (S7 Q13) | Firewall design (§4.8) | `legal_reviewer` | P07 |
| OI-T-19 | Counsel: s.42A A&C Act — validity of deemed-consent publication of redacted challenge decisions and of statistics (02 §5 Q1; S5 F Q1–Q2) | IP-07, IP-09 | `legal_reviewer` | P13 publication |
| OI-T-20 | Telecom counsel opinion and operator written confirmation of CLI type for Equator's own service calls (RES_A4 D3) | `voice.equator_service_number.enabled` | `compliance_officer` | Before flag ON |

---

## Phase addendum (paste into P07)

Vendor posture only. Requirements extend P07 FR-P07-01…; they do not change master §8 defaults.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P07-V2-T01 | **Jio SIP trunk as second PSTN carrier.** Add `TELEPHONY_PORT` adapter `jio_sip` behind flag `telephony.jio_sip.enabled` (default OFF). Activation requires: signed CAF/MSA, Equator PE linkage on Jio DLT in `core.dlt_registry` (operator `jio`), failover test from Exotel, and config `telephony.max_carrier_share` (default 0.70) enforced monthly. | With the flag OFF no call routes via `jio_sip`; with it ON a circuit-breaker trip on Exotel routes new calls to `jio_sip` within 60 s; a monthly report flags any carrier above 70% of outbound minutes; NN-12 tests pass unchanged on both carriers. |
| FR-P07-V2-T02 | **Telecom compliance is enforced by Equator, not the vendor.** Quiet hours (08:00–19:00 for borrower contact; 09:00–18:00 for microfinance loans, LR-RBI-005 *(v3.1)*), DND/consent checks, DLT template binding, A2P CLI declaration, 1600-series lender-number mode with written tenant authorisation, and the 140-series prohibition are evaluated in the `comms` module before any `TELEPHONY_PORT`, `VOICE_PORT` or `MESSAGING_PORT` call, for every provider including Jio. | Test `NN-12_vendor_agnostic_enforcement`: a call scheduled at 19:05 local time via any adapter is blocked with `CONTACT_OUTSIDE_WINDOW` (Appendix F canonical; alias `COMMS_QUIET_HOURS`); a CLI in a 140-series range is rejected with `COMMS_CLI_SERIES_FORBIDDEN`. |
| FR-P07-V2-T03 | **JioCX as secondary SMS/RCS route.** `MESSAGING_PORT` adapter `jiocx` behind `messaging.jiocx.enabled` (OFF). Route cannot be activated unless delivery-report callbacks are enabled by Jio, authenticated (signature or IP allow-list + mutual TLS) and pass a 100-message DLR test; route types mapped to DLT routes (Transactional / OTP only for case traffic; Promotional never for case traffic). | Activation attempt without a passing DLR test returns `PROVIDER_ACTIVATION_GATE_FAILED`; a case notice cannot be sent on the Promotional route (`COMMS_ROUTE_NOT_ALLOWED`); DLRs land in `core.service_attempts` with provider receipt hash. |
| FR-P07-V2-T04 | **Branded caller ID pilot (JioCX Verify).** Behind `voice.branded_cli.jiocx.enabled` (OFF); display name is "Equator Resolution" for Equator-number calls and the regulated tenant's registered name in lender-number mode; applies only to declared numbers. Pilot report: answer rate and complaint count vs control. | Pilot cannot start for undeclared numbers; report shows uplift and complaints; flag stays OFF if any impersonation complaint is upheld. |
| FR-P07-V2-T05 | **Vendor evaluation registry and gates.** Tables `eng.vendor_evaluations(id, vendor_code, ports[], status CHECK IN ('watch','rfp','shortlisted','approved','rejected'), score_total, gate_results jsonb, decided_by, decided_at, review_due)`, `eng.rfp_questions` (versioned; seeded with §4.5 Q1–Q12) and `eng.vendor_rfp_responses`. `core.provider_routing` rows may reference only vendors with `status = 'approved'` for the port concerned; maker–checker on status changes. | Inserting a `provider_routing` row for a vendor in `watch` or `rfp` fails with `PROVIDER_NOT_APPROVED`; approval without all ten gates recorded fails; status changes write `audit.audit_events` and emit `equator.integrations.vendor_evaluation.status_changed.v1`. |
| FR-P07-V2-T06 | **Vendor conflict firewall.** `eng.vendor_groups`; `core.organisations.group_code`; routing rule `RR-VND-01` excludes content-processing vendors of the same group as any case party for `VOICE_PORT`, WhatsApp-agent `MESSAGING_PORT`, `LLM_PORT`, `TRANSCRIPTION_PORT`, `TRANSLATION_PORT`, `DOC_AI_PORT` (§4.8); carriage-only ports logged. Party-requested vendor switch via `POST /v1/cases/{caseId}/provider-overrides`. | Seeded case with a Reliance-group respondent never routes a voice-agent call through `jio_haptik` (test `RR-VND-01_group_exclusion`); event `equator.integrations.vendor_conflict.applied.v1` emitted; override request by a party is applied within one request when a fallback exists. |
| FR-P07-V2-T07 | **Network-AI confidentiality controls.** Mediation phone-session script (§4.9) inserted before any PSTN mediation or caucus bridge; sealed-tier sessions default to in-app VoIP; PSTN only on party request with acknowledgement recorded. | A FAM safety-flagged session cannot be scheduled on PSTN without a recorded acknowledgement; script text present in EN and HI templates. |
| FR-P07-V2-T08 | **Voice-agent bake-off harness for challengers (incl. Jio Haptik).** Same Equator test set per language; metrics WER, MOS, p95 turn latency, disclosure compliance; Haptik agent must use Equator's OpenAI-compatible Bedrock proxy (BYO-LLM). | A challenger is routable only if gate G8 passes (`ai_eval_run_id` recorded); disclosure compliance must be 100%. |
| FR-P07-V2-T09 | **Marketing tools never touch respondents.** Interakt or any marketing CRM adapter (`CRM_PORT`) can read only `growth` schema contacts with a valid marketing consent; respondent and case contacts are unreachable from `CRM_PORT` by schema permission. | Attempt to sync a respondent contact fails with `NN16_MARKETING_SCOPE_DENIED` (test `NN-16_marketing_firewall_vendor`). |
| FR-P07-V2-T10 | **No JioMeet dependency.** `VIDEO_PORT` excludes JioMeet until an embed, recording-export and watermark API is published and passes G1–G7. | `VIDEO_PORT` provider list contains no JioMeet adapter; ADR records the decision. |

## Phase addendum (paste into P11)

Vendor posture only for AI providers. Extends P11 FR-P11-01… and Appendix E.

| ID | Requirement | Acceptance criteria |
|---|---|---|
| FR-P11-V2-T01 | **LLM provider allow-list.** `LLM_PORT` routable providers: Claude via Amazon Bedrock India in-country inference (primary), Anthropic API direct (public-data jobs only, OFF by default — FR-P11-07; never a fallback for case content — X-32, App. M §4.2), Sarvam (Indic models, `indic_low_risk` tier only — FR-P11-08). JioBrain and REIL are registered in `eng.vendor_evaluations` with `status = 'watch'` and are non-routable. | Configuring `LLM_PORT` to a `watch` provider fails with `PROVIDER_NOT_APPROVED`; sealed-tier prompts are refused by any provider without India inference (test `NN-15_llm_residency_route`). |
| FR-P11-V2-T02 | **Quarterly AI watch-list review.** Scheduled Temporal workflow `ai.vendor_watchlist.review` creates a task for `platform_admin` every quarter to re-check JioBrain/REIL (and other watch-listed AI vendors) for primary-source API docs, DPA, residency, no-training and firewall terms; result recorded in `growth.benchmark_entries` and `eng.vendor_evaluations.review_due`. | Task created on schedule; a watch-list vendor cannot move to `rfp` without a primary-source URL recorded (secondary sources such as press articles are rejected for this field). |
| FR-P11-V2-T03 | **Data-class routing.** `ai.route_policy` maps data class → allowed providers per App. M §4.3: `sealed` → Bedrock India only, and sealed sources never reach a model (App. M M-D-05); `high` and `standard` case content (D2/D3) → Bedrock India only (self-hosted engines for MT/embeddings; Sarvam only for the `indic_low_risk` tier and the App. L OCR/translation routes); account/contact (D1) → Bedrock India, Sarvam India; `public` (D0) → any approved provider. Enforced in the AI Gateway before egress. | Eval `routing_policy` 100%; a sealed-tier request with Bedrock unavailable degrades to the deterministic fallback (NN-02), never to another provider. |
| FR-P11-V2-T04 | **No third-party "pre-configured" drafting or research solutions.** AI research and drafting use only Equator's AI Gateway over the verified corpus (Appendix M); vendor-packaged drafting products (e.g., REIL pre-configured solutions) are not integrated. | Code search in CI finds no adapter for vendor drafting suites; App. M citation-integrity eval remains 100%. |
| FR-P11-V2-T05 | **Provider onboarding eval gate.** Any new LLM or voice-reasoning provider must pass the zero-tolerance guardrail suite (GX-1…GX-7), citation integrity, bilingual parity and the sensitive-data scan before `approved`. | `eng.vendor_evaluations` approval requires `ai_eval_run_id` with all zero-tolerance suites at 100%. |
| FR-P11-V2-T06 | **Sub-processor and group disclosure.** Every AI and communications vendor appears in the public sub-processor register (Trust Centre, Appendix Q) with corporate group, processing location and purpose; changes published ≥ 30 days before activation for enterprise tenants with DPAs. | Register page generated from `eng.vendor_evaluations` + `eng.vendor_groups`; activation before the notice period ends is blocked for affected tenants. |
| FR-P11-V2-T07 | **BYO-LLM for agent platforms.** If any agent platform (Jio Haptik, ElevenLabs, Sarvam) is used, the reasoning model for case content is Equator's OpenAI-compatible proxy to Bedrock India; the platform's native LLM is disabled for case-content agents. | Agent definition compile (`VOICE_PORT.upsertAgent`) fails with `AGENT_NATIVE_LLM_FORBIDDEN` if the native LLM is selected for a case-content agent. |

*(End of Appendix T.)*
