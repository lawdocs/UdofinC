# V6 — International Commercial (INT) — Vertical Specification

> Binding for P08f. Read with master (`01_MASTER_PROMPT.md` v2.0), `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`, Appendices A, B, F, G, K, L, M (and N, Q, R, S where cited). This file extends P08 §4.6 (FR-P08-68 – FR-P08-83); it does not repeat what P08 already specifies unless a change or a field-level detail is needed. Where this file and P08 differ, §0.3 says which one wins and why.
>
> Version 2.0 · 21 October 2026 · Operator: Equator Resolution Service Private Limited · Owner: Registrar (INT) · Legal reviewer sign-off required before activation (FR-P08-01).

---

## 0. Scope and how to use

### 0.1 What this vertical covers

Business-to-business disputes with a cross-border element, administered by Equator under the **Equator International Arbitration Rules**, the **Equator International Mediation Rules**, or — on the parties' election — the **UNCITRAL Arbitration Rules (2010/2021)** or **UNCITRAL Mediation Rules (2021)** with Equator as administering institution and appointing authority. Two first-level (L1) families:

| L1 | Family | Mechanisms (master §5.2, INT column) |
|---|---|---|
| `int.ica` | International commercial arbitration — India-seated (New Delhi, Mumbai, other Indian city, GIFT City IFSC) or foreign-seated, administered by Equator | `arbitration` (Standard, Expedited, Highly Expedited, Streamlined documents-only), emergency arbitrator, `arb_med_arb` (Equator AMA Protocol), `arb_med`, `expert_determination` (technical/valuation issues, by agreement), optional internal appeal tier (D4) |
| `int.imed` | International mediation (and Part III conciliation where the place of conciliation is India) | `negotiation`, `mediation` (contractual mode; statutory mode only behind the NN-05 flag), `conciliation`, `med_arb`, consent-award conversion (master §5.3) |

A third, signpost-only L1, `int.out_of_scope`, holds requests Equator never administers: WTO/state-to-state trade disputes, investor-state (treaty) claims, cross-border consumer disputes, and criminal matters (NN-24). These produce an auditable signposting event (NN-20) and nothing else.

### 0.2 How the coding agent uses this file

1. Seed taxonomy (§2) into `core.dispute_types` with `l1_code`, `l2_code` (Appendix K plug-in format).
2. Load suitability rules (§4) as a decision table into `packages/rules/verticals/int/` — deterministic; the AI intake assistant may classify but never routes (NN-01, NN-02).
3. Build the Dispute Explorer trees (§5) and the form schemas (§6) through the P02 form engine; every dropdown in §6.9 is a versioned option list (`core.form_schema_versions`), bilingual EN + HI labels, with the target-language label slot for INT (FR-P08-09).
4. Implement step tables (§7, §8) as Temporal workflows on top of Appendix A machines (§3.3 mediation, §3.5–3.8 arbitration, §3.10 AMA, §3.11 expert determination, §3.12 appeal).
5. Implement calculators (§12) with the golden vectors as unit tests.
6. Apply data-model extensions (§16) in the `intl` schema; error codes and events in §16.6–16.7 are added to Appendix F catalogues by the P08f migration.
7. Ship the ≥ 15 Gherkin scenarios in §17 as `tests/acceptance/int/*.feature`; NN-tagged tests use the `NN-xx_*` naming rule.

### 0.3 Reconciliation with existing pack files (recorded for `docs/adr/`)

| # | Topic | Existing text | This file | Winner and reason |
|---|---|---|---|---|
| R-V6-01 | Taxonomy codes | P08 FR-P08-68 uses sector codes (`int.sale_of_goods` …) as dispute types | L1 = mechanism family (`int.ica` / `int.imed` / `int.out_of_scope`); L2 = the same P08 sector codes, unchanged; new L2 `int.energy` and `int.services` retained | Both: P08 codes become the L2 key; no migration of codes needed. D2-01 two-level taxonomy |
| R-V6-02 | Expedited threshold | P08 FR-P08-72 and §9 config: ≤ USD 3,000,000; Appendix B Card INT-USD "Track" column marks only USD 250,001–1,000,000 as "Expedited eligible" | Rules parameter `int.tier.expedited_max_usd` default **USD 4,000,000** (benchmark: ICC Arbitration Rules 2026, Appendix VI threshold for agreements on/after 1 Jun 2026; SIAC Rules 2025 r.14 SGD 10m) | This file sets the procedural threshold (a rules parameter, not a fee figure); Appendix B's "Track" column is descriptive only and Appendix B fee figures are untouched. Board approval required (M-01). Raise ADR. *v3.1:* conflict resolved — Appendix B and P08 now state USD 4,000,000 (OI-INT-10) |
| R-V6-03 | Error codes | P08 FR-P08-83 uses `INT_SANCTIONS_HOLD` (423), `INT_TRANSFER_BASIS_MISSING` | Appendix F codes `SANCTIONS_HIT_REVIEW` (409), `DPDP_TRANSFER_BASIS_MISSING` (409), `INT_KYC_UBO_INCOMPLETE`, `INT_TEST_NOT_MET` | Appendix F (master §15 precedence 4 over phase file 6). P08 names kept as aliases in the error map |
| R-V6-04 | Publication of INT awards | S5 research recommends ICC-style opt-out publication after 24 months for foreign-seated awards | Opt-in only, all parties + tribunal, revocable until publication (NN-26) | Master NN-26 |
| R-V6-05 | Governance names and grades | S5 research proposes an "Equator Court" and grades G1–G4 | Equator Institutional Committee and sub-committees (D2-15); grades A/B/C with an **INT endorsement** (`END-INT`) (D2-12; Appendix N) | Master/02 decision log |
| R-V6-06 | Mediation Act definition | R5 cited s.3(e) and A&C-style wording | **Mediation Act 2023 s.3(g)** ("place of business outside India" test) — LR-MED-016 | Appendix G / GLOBAL_CORRECTIONS §1 |
| R-V6-07 | ICC benchmark | R5 §3 cites ICC 2021 Rules (EPP ≤ USD 3m) | ICC Arbitration Rules 2026, in force 1 Jun 2026 (Terms of Reference no longer mandatory; EPP USD 4m; opt-in Highly Expedited provisions; early determination Art. 30; disclosure Art. 12) | S5 Part D-1 (verified) |

### 0.4 Status legend used in this file

`IN_FORCE` / `NOT_IN_FORCE` / `DRAFT` follow Appendix G. **[K]** = established law or institutional text not re-fetched for this file. A bold VERIFY-open marker with a reason = must be confirmed before the dependent rule is activated; the dependent feature ships behind a flag defaulting OFF (master §0).

---

## 1. Vertical overview

### 1.1 Who uses INT

| Segment | Typical claimant | Typical respondent | Why they come to Equator |
|---|---|---|---|
| Indian exporters and importers | Indian MSME or mid-cap exporter (textiles, engineering goods, pharma APIs, agri) | Foreign buyer (UAE, US, EU, UK, Africa, ASEAN) | Unpaid invoices, quality rejection, documentary-credit discrepancies; cost of SIAC/ICC/LCIA is disproportionate below USD 1m |
| Foreign suppliers to India | Foreign OEM, technology licensor, commodity trader | Indian distributor, licensee, EPC contractor | Need an India-competent forum with English proceedings, USD/EUR pricing and New York Convention (NYC) output |
| Cross-border JV and investment parties | PE/VC investor, foreign JV partner, promoter | Counterparty shareholder; target company | Put/call options, earn-outs, warranty claims (SPA), deadlock — private-party disputes only |
| EPC and project parties | Contractor, sub-contractor, employer | Employer, EPC contractor | FIDIC-based claims after DAAB; delay, variation, liquidated damages, bond calls |
| Shipping and logistics | Cargo owner, carrier, charterer, owner, freight forwarder | Counterparty | Cargo loss/damage (Hague-Visby one-year bar), demurrage, freight |
| Law firms, chambers of commerce, trade bodies | Referral partners (P09/P10) | — | Clause builder, appointing-authority service, fundholding |

### 1.2 Value proposition (copy-safe, NN-17)

- One platform from negotiation to an **enforcement-ready award pack**: NYC Art. IV documents, apostille/legalisation route, certified translations, procedural-fairness log.
- **Published USD fee schedule** (Appendix B Cards INT-USD, INT-MED) priced below SIAC/ICC for sub-USD-5m matters (public comparison only with a Claims Register record — NN-17; Appendix B benchmarks are approximate), invoiced in USD/EUR/GBP/SGD/AED with INR equivalent shown (D7).
- **Independent appointments**: Equator Appointments Committee; neutral-nationality default for sole/presiding arbitrators (A&C s.11(9) mirror; LR-INT-005); no unilateral appointment (*CORE* 2024; NN-03).
- **Time-zone-fair virtual hearings** (Seoul Protocol 2020 based), interpretation channels, e-bundles.
- **Compliance gates** (sanctions, KYC/UBO, data transfer, FEMA) so that awards are payable through banks.
- Copy must never say: "Singapore Convention enforceable in India", "Equator court", "decree", "guaranteed enforcement", "fastest in Asia" (no evidence record), "IFSC arbitration centre" (none exists — LR-INT-021).

### 1.3 Mechanisms allowed (master §5.2, INT column) and INT limits

| Mechanism | Allowed | INT-specific limits |
|---|---|---|
| Negotiation | ✔ | Assisted or blind-bid; multi-currency offers with FX snapshot (NN-13) |
| Conciliation (A&C Part III) | ✔ | Offered where the place of conciliation is India; s.73/s.74 settlement has award status in India, but its recognition abroad under the NYC is uncertain (no arbitral tribunal), and it may also fall outside the Singapore Convention as a settlement 'enforceable as an arbitral award' (Art. 1(3)(b)) **[VERIFY — open (counsel): foreign recognition of s.74 settlements]** → consent-award conversion is the default cross-border route |
| Mediation | ✔ | Contractual mode; statutory mode only when the NN-05 flag is ON |
| Arbitration | ✔ | Four procedure tiers (§7.2); NN-03 equal-footing nomination allowed only where `equal_footing = true` |
| Med-arb / Arb-med / Arb-med-arb | ✔ | Master §5.3; different neutral by default; same-neutral switch only on fresh post-mediation e-signed consent + renewed s.12 disclosure; never in statutory mode (Mediation Act s.17) |
| Expert determination | ✔ | Technical (EPC, energy), valuation (JV exit), quality (sale of goods); outcome is contractual, not an award (Appendix A §3.11) |
| Grievance / POSH | — | Not applicable |
| Signposting | ✔ | WTO, ISDS, courts (vessel arrest, anti-suit, insolvency), CCI, NCLT, IP offices, consumer forums |

### 1.4 Status of key laws and instruments (as of 21 Oct 2026)

| Instrument | Status | Effect on product | Rule |
|---|---|---|---|
| Arbitration and Conciliation Act 1996 (A&C) Part I (India seat) and Part II (foreign awards) | IN_FORCE (as amended 2015, 2019, 2021) | ICA definition s.2(1)(f); Part I only for India seat s.2(2) and proviso; s.29A advisory for ICA; s.34(2A) patent illegality **does not apply** to ICA [K] | LR-INT-001/002, LR-ARB-010 |
| Draft A&C (Amendment) Bill 2024 (statutory EA s.9A; appellate arbitral tribunal s.34A) | DRAFT — not introduced as of 20 Oct 2026 | Nothing statutory; contractual EA and optional appeal tier only | LR-ARB-026 |
| Mediation Act 2023 (Act 32 of 2023) | PARTIALLY_IN_FORCE: ss.1, 3, 26, 31–38, 45–47, 50–54, 56–57 (S.O. 4384(E), 9 Oct 2023; corr. S.O. 4506(E), 13 Oct 2023); MCI established S.O. 4781(E), 27 Aug 2026 | International mediation definition s.3(g) is in force; ss.17, 22, 23, 27, 28, 30 are not — applied as Equator policy; contractual mode | NN-05; LR-MED-001, -016 |
| Singapore Convention on Mediation (2018) | 25 parties, 22 in force (UNCITRAL status 20 Oct 2026); UAE acceded 8 Oct 2026 (in force for UAE 8 Apr 2027); Mauritius in force 17 Feb 2027; Uzbekistan 28 Feb 2027; **India signed 7 Aug 2019, not ratified** | Never claim enforceability in India; offer consent-award conversion on every iMSA; Art. 4 attestation for use in Convention states | NN-19; LR-INT-010/011 |
| New York Convention 1958 + A&C s.44(b) notifications | IN_FORCE; India applies reciprocity and commercial reservations [K]; ~50 territories notified | Seat badge "India-notified" per Gazette S.O.; **UAE not notified** (2020 notification is CPC s.44A, decrees only); Mauritius S.O. 1881(E), 13 Jul 2015; Netherlands S.O. 732(E), 24 Nov 1972; China/HK/Macao S.O. 580(E), 19 Mar 2012; Cyprus and Saudi Arabia — notification unconfirmed; treated as not notified until a Gazette S.O. is recorded **[VERIFY — open: Gazette check]** | LR-INT-006, LR-INT-025 |
| UNCITRAL Arbitration Rules (2021 text incl. Expedited Rules appendix), Mediation Rules 2021, Model Law on International Commercial Mediation 2018, Technical Notes on ODR 2016 | Current [K] | Optional rules tracks; Equator as appointing authority | §7 |
| ICC Arbitration Rules 2026 (in force 1 Jun 2026); SIAC Rules 2025 (1 Jan 2025); HKIAC Rules 2024 (+1 Jan 2026 amendments); LCIA Rules 2020; ICDR Rules 2021; IIAC (Conduct of Arbitration) Regulations 2023 | Current (benchmarks) | Tier design, EA, TPF disclosure, scrutiny, relevant-persons list | §7, §15 |
| IBA Rules on the Taking of Evidence 2020; IBA Guidelines on Conflicts of Interest 2024; IBA Guidelines on Party Representation 2013; Seoul Protocol on Video Conferencing 2020; ICCA–NYC Bar–CPR Cybersecurity Protocol (2022 ed.); ICCA–IBA Data Protection Roadmap 2022; CIArb Guideline on AI in Arbitration 2025 | Soft law [K] | PO-1 options; disclosure engine; hearing protocol; security tier; AI protocol | §7, §13 |
| CISG (Vienna 1980) | India **not a party** | CISG exclusion toggle; applies only by choice or via PIL leading to a Contracting State's law | LR-INT-018 |
| Carriage of Goods by Sea Act 2025 (Act 19 of 2025; in force 10 Sep 2025) replacing the 1925 Act; Schedule = Hague-Visby based rules | IN_FORCE | One-year time-bar clock for cargo claims (Schedule Art. III para 6(c); extension by agreement; 3-month proviso) [Verified 22 Oct 2026: Act 19 of 2025, India Code; in force 10 Sep 2025, S.O. 4082(E)] | LR-INT-023 |
| DPDP Act 2023 + DPDP Rules 2025 (G.S.R. 846(E), 13 Nov 2025) | Core obligations from 13 May 2027 — comply now | s.16 transfer basis; s.17(1)(a) legal-claims; s.17(1)(d) non-resident data under foreign contract | LR-DPDP-010/011; NN-15 |
| EU AI Act (Reg. 2024/1689) Annex III(8)(a), as amended by Reg. (EU) 2026/1744 | High-risk obligations apply from 2 Dec 2027 | INT matters with EU parties: AI clerical/translation/summary only | LR-INT-020 |
| BCI Foreign Lawyers Rules 2022 (notified Mar 2023; amended 13 May 2025) | IN_FORCE | Foreign counsel only in ICA, client's principal office abroad, foreign/international-law issues only; fly-in/fly-out ≤ 60 days in any 12 months (Form C) | LR-INT-019 |
| Income-tax Act 2025 (from 1 Apr 2026) | IN_FORCE | Non-resident neutral payouts s.393(2) Table Sl. 17; Form 41; Forms 145/146; TRC s.159(8) | LR-TAX-005 |
| GIFT City IFSC arbitration centre | **Not established** (further IFSCA expert committee, reported 24 Jul 2026) | IFSC seat = Indian seat (Part I; Gujarat High Court supervisory); `intl_ifsc_schedule` OFF | LR-INT-021 |

---

## 2. Subtype taxonomy

### 2.1 L1 families

| L1 code | Name | Case number segment | Default confidentiality tier | Notes |
|---|---|---|---|---|
| `int.ica` | International commercial arbitration | `EQ/INT/<CITY>/<YYYY>/<NNNNN>` with suffix `-A` | `high` | Requires gate G5 (`ica_flag = true`) for India seat; for foreign seat Equator still records the s.2(1)(f) result for Part II analysis |
| `int.imed` | International mediation / conciliation | suffix `-M` | `high` | Requires `intl_mediation_flag = true` (Mediation Act s.3(g)) or `ica_flag = true` |
| `int.out_of_scope` | Signpost only (WTO, ISDS, consumer, criminal) | no case number; `signposting_events` row only | — | `signpost_only = true` (FR-P08-02) |

If neither international test is met (all parties Indian, places of business in India, no foreign government), G5 re-routes the matter to `COM` with its form answers carried over (`INT_TEST_NOT_MET`, 422; outcome `OUT-INT-REROUTE-COM`). Exception: two Indian parties who **choose a foreign seat** stay in INT under `int.ica` (*PASL Wind Solutions v GE Power Conversion India* (2021) 7 SCC 1; LR-INT-003) with `ica_flag = false` and `foreign_seat_indian_parties = true`.

### 2.2 L2 subtypes (apply under both `int.ica` and `int.imed`)

Value bands (USD equivalent at filing snapshot): **B1** ≤ 250,000 · **B2** 250,001–1,000,000 · **B3** 1,000,001–5,000,000 · **B4** 5,000,001–25,000,000 · **B5** > 25,000,000.

| L1 code | L2 code | Name | Typical parties | Value band | Default ladder | Negotiable | Mediable | Arbitrable | Signpost forum | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| ica / imed | `int.sale_of_goods` | Cross-border sale of goods (CISG-aware; Incoterms 2020) | Exporter, importer, trader | B1–B4 | `int.ama.v1` (negotiation 30 d → mediation 60 d → arbitration) | ✔ | ✔ | ✔ | Customs/DGTR for duty issues; ECGC for export-credit cover claims (not a forum for the buyer dispute) | Streamlined tier common; quality disputes → expert determination option |
| ica / imed | `int.services` | Cross-border services / IT / BPO / outsourcing | Service provider, customer | B1–B4 | `int.ama.v1` | ✔ | ✔ | ✔ | — | SLA credits, acceptance, change requests |
| ica / imed | `int.distribution_agency` | Distribution, agency, franchise | Principal, distributor, agent, franchisee | B1–B3 | `int.ama.v1` | ✔ | ✔ | ✔ (contract claims) | CCI (competition law effects, Competition Act 2002 s.3(4)) | EU commercial-agent indemnity/compensation if EU law governs (Directive 86/653/EEC Arts. 17–18) [K] |
| ica / imed | `int.jv_shareholder` | JV / shareholder (cross-border) | JV partners, investor, promoter | B2–B5 | `int.ama.v1` + expert determination for valuation | ✔ | ✔ | ✔ inter-se contract claims; ✖ oppression/mismanagement reliefs | NCLT (Companies Act 2013 ss.241–242) | Put/call options → FEMA NDI pricing advisory (LR-INT-014) |
| ica / imed | `int.technology_licensing` | Technology transfer / IP licensing | Licensor, licensee | B1–B4 | `int.ama.v1` | ✔ | ✔ | ✔ royalty, scope, breach; ✖ validity/grant/registration of IP | Patent Office / Trade Marks Registry / High Court (validity); WIPO AMC (alternative ADR) | IP validity is in rem — never awarded (NN-06; *Vidya Drolia* (2021) 2 SCC 1) |
| ica / imed | `int.epc_construction` | Construction / EPC / FIDIC | Employer, contractor, sub-contractor | B2–B5 | DAAB (contractual, outside Equator unless appointed) → amicable settlement (mediation) → arbitration | ✔ | ✔ | ✔ | — | FIDIC 2017 cl. 20.2.1 28-day notice; cl. 21 DAAB; Notice of Dissatisfaction 28 days [K — confirm clause numbers against licensed text] |
| ica / imed | `int.shipping_logistics` | Shipping, charterparty, carriage of goods (COGSA 2025), freight forwarding | Cargo interests, carrier, owner, charterer, forwarder | B1–B4 | arbitration (maritime list) or mediation | ✔ | ✔ | ✔ | High Court admiralty jurisdiction for vessel arrest (Admiralty (Jurisdiction and Settlement of Maritime Claims) Act 2017) [K] | Hague-Visby one-year time bar clock (LR-INT-023); LMAA/SCMA-style terms are benchmarks only [K] |
| ica / imed | `int.trade_finance` | Trade finance, LC, standby LC, demand guarantee, factoring | Beneficiary, applicant, issuing/confirming bank, factor | B1–B4 | mediation → arbitration (bank consent required) | ✔ | ✔ | ✔ between consenting parties | High Court for injunctions restraining encashment (fraud / irretrievable injustice only) | Autonomy notice (LR-INT-022); ICC DOCDEX is a benchmark expert service [K]; RBI-regulated bank parties may need internal approvals |
| ica / imed | `int.energy` | Energy (cross-border power, LNG/gas supply, renewables EPC, equipment, O&M) | Generator, offtaker, supplier, EPC contractor | B2–B5 | `int.ama.v1`; price-review clauses → expert determination | ✔ | ✔ | ✔ contract claims; ✖ matters within CERC/SERC exclusive adjudication | CERC/SERC (Electricity Act 2003 ss.79(1)(f), 86(1)(f)); PNGRB (Mediation Act First Schedule excludes PNGRB matters) [K] | Licensee–generator disputes go to the Commission, which may refer to arbitration (*Gujarat Urja Vikas Nigam v Essar Power* (2008) 4 SCC 755) [K] |
| ica / imed | `int.investment_private` | Investment-agreement commercial disputes between private parties (SPA, SHA, earn-out, W&I) | Buyer, seller, investor, warrantor | B2–B5 | `int.ama.v1` + expert determination for completion accounts | ✔ | ✔ | ✔ | — | **Never** a claim against a State under a BIT (→ `int.out_of_scope`) |
| ica / imed | `int.other` | Other cross-border commercial | per agreement | any | per agreement | ✔ | ✔ | ✔ subject to arbitrability screen | — | Registrar classifies within 2 working days |
| out_of_scope | `int.state_treaty` | Investor-state / treaty claim | Investor v State | — | none | — | — | — | ICSID (India not a Contracting State) [K], PCA, UNCITRAL ad hoc; India Model BIT 2016 | Declined + signposted (LR-INT-016) |
| out_of_scope | `int.wto_trade_measure` | WTO / state-to-state trade dispute | Government v Government | — | none | — | — | — | Department of Commerce (Trade Policy Division); DGTR; DGFT | Private parties have no standing (WTO DSU Arts. 1, 3, 4, 6) |
| out_of_scope | `int.consumer_crossborder` | Cross-border consumer dispute | Consumer v foreign trader | — | none | — | — | — | e-Jagriti (https://e-jagriti.gov.in/); National Consumer Helpline | Consumer clauses cannot oust the Consumer Commission (*Emaar MGF v Aftab Singh* (2019) 12 SCC 751); INT is B2B only |
| out_of_scope | `int.criminal` | Fraud/offence-led matter (e.g., cargo theft FIR, cheating) | — | — | none | — | — | — | Police / Magistrate; ED for FEMA contraventions | NN-24: civil money dimension may proceed only if separable and not under compounding (§4.2) |

### 2.3 Trade-measure impact (cross-cutting field, not a subtype)

Every L2 carries `trade_measure_impact` (§6.9 list DL-INT-27): `none · ad_cvd · safeguard · tariff_change · qco_tbt · sps · export_control · sanctions · cbam · fta_origin_denial`, with `measure_reference` and `effective_date`. It never makes a matter state-to-state; it informs hardship / force-majeure briefing cards for the tribunal (UNIDROIT Principles 2016 Arts. 6.2.1–6.2.3, 7.1.7; Indian Contract Act s.56 — *Energy Watchdog v CERC* (2017) 14 SCC 80: a price rise is not frustration) and analytics clustering (§14).

---

## 3. Legal framework by subtype

### 3.1 Common framework (all L2)

| Topic | Rule | Source | Status | Product effect |
|---|---|---|---|---|
| ICA definition | At least one party: foreign national/habitual resident; body corporate incorporated outside India; association/body whose central management and control is outside India; foreign Government. An Indian-incorporated company controlled from abroad is not foreign | A&C s.2(1)(f); *TDM Infrastructure v UE Development* (2008) 14 SCC 271 | IN_FORCE | G5 auto-computation (§4.4) |
| International mediation definition | At least one party: individual national of/habitually resident in another country; body corporate (incl. LLP) **with its place of business outside India**; association/body with place of business outside India; foreign Government; commercial dispute | Mediation Act 2023 s.3(g) | IN_FORCE (s.3) | `intl_mediation_flag` |
| Seat and Part I | Part I applies only to an Indian seat; ss.9, 27, 37(1)(b), 37(3) available to foreign seats unless excluded; pre-6 Sep 2012 agreements follow *Bhatia International* | A&C s.2(2); *BALCO v Kaiser Aluminium* (2012) 9 SCC 552 | IN_FORCE | LR-INT-002; legacy notice |
| Foreign seat for Indian parties | Permitted; award is a Part II foreign award; s.9 relief available in India | *PASL Wind Solutions* (2021) 7 SCC 1 | IN_FORCE | LR-INT-003 |
| Three laws | Substantive law, law of the arbitration agreement, seat/lex arbitri captured separately; governing-law ≠ seat → warning | *Disortho S.A.S. v Meril Life Sciences* 2025 SCC OnLine SC 570; UK Arbitration Act 2025 s.6A (law of the seat default for the arbitration agreement) [K — in force 1 Aug 2025; confirm] | IN_FORCE | LR-INT-004; London seat → law-of-agreement field mandatory |
| Rules of law in ICA | Parties may choose rules of law (e.g., UNIDROIT Principles); absent choice the tribunal applies rules it considers appropriate; ex aequo et bono only if expressly authorised | A&C s.28(1)(b), s.28(2) | IN_FORCE | `rules_of_law`, `ex_aequo_authorised` fields |
| Formation by conduct | An arbitration agreement may be found in correspondence/conduct even if the main contract is unsigned | *Glencore International AG v Shree Ganesh Metals* 2025 (SC); A&C s.7(4)(b) | IN_FORCE | LR-ARB-027; email-chain evidence upload |
| Non-signatories | Joinder on evidence of consent/conduct (group of companies) by reasoned tribunal order | *Cox & Kings v SAP India* (2024) 4 SCC 1; *ASF Buildtech v Shapoorji Pallonji* (SC 2025) | IN_FORCE | LR-ARB-029; F-INT-17 |
| Appointment | Unilateral appointment of sole/presiding invalid; ICA appointments by the Supreme Court under s.11(12)(a) where court assistance is needed; s.11(9) neutral nationality | *CORE v ECI-SPIC-SMO-MCML (JV)* 2024 INSC 857 (8 Nov 2024); A&C s.11(9), (12) | IN_FORCE | NN-03, LR-INT-005 |
| Independence | Sixth Schedule disclosure; Seventh Schedule ineligibility waivable only by express written post-dispute agreement | A&C s.12, Fifth–Seventh Schedules; *Bhadra International v AAI* (SC, 5 Jan 2026) | IN_FORCE | LR-ARB-002; IBA 2024 list mapping |
| Time limit | s.29A 12-month limit is advisory for ICA ("endeavour") | A&C s.29A(1) proviso | IN_FORCE | LR-ARB-010; owned service clock |
| Interim relief | India-seated EA order enforceable as s.17 order; foreign-seated EA order needs s.9 in India | *Amazon.com NV Investment Holdings v Future Retail* (2022) 1 SCC 209 | IN_FORCE | LR-ARB-025 |
| Award form | In writing, signed, reasons (unless agreed or s.30), date and seat; post-award interest under s.31(7)(b) cannot be contracted out; severable heads | A&C s.31; *ONGC v G&T Beckfield* 2025 INSC 1066; *Gayatri Balasamy v ISG Novasoft* 2025 INSC 605 | IN_FORCE | LR-ARB-013/015/021 |
| Delay | Inordinate unexplained delay can vitiate the award | *Lancor Holdings v Prem Kumar Menon* 2025 INSC 1277 | IN_FORCE | Award target ≤ 3 months after final hearing/submission |
| Setting aside (India seat, ICA) | s.34 grounds; patent illegality (s.34(2A)) unavailable for ICA [K] | A&C s.34 | IN_FORCE | Scrutiny checklist |
| Enforcement of foreign awards in India | s.44 definition; s.47 evidence; s.48 narrow grounds; s.49 deemed decree only after court is satisfied; s.50 appeals; limitation Art. 137, 3 years | A&C ss.44–50; *Vijay Karia v Prysmian* (2020) 11 SCC 1; *Avitel Post Studioz v HSBC PI* (2024) 7 SCC 197; *Kalyani Transco v Bhushan Power & Steel* 2025 INSC 1165; *Government of India v Vedanta Ltd* (2020) 10 SCC 1; *Gokul Patnaik v Nine Rivers Capital*, SLP(C) 21109/2025 dismissed 22 Apr 2026 | IN_FORCE | LR-INT-007/008/009 |
| Stamp duty | India-seated award stamped in the state of execution (last signature); foreign award not stamped for enforcement | *Shriram EPC v Rioglass Solar* (2018) 18 SCC 313; *URC Construction v AAI* (Del HC, 1 Sep 2026) | IN_FORCE | LR-STAMP-001/003 |
| Confidentiality | Arbitrator, institution and parties keep proceedings confidential, save the award where needed for enforcement | A&C s.42A | IN_FORCE | LR-ARB-024; publication opt-in (NN-26) |
| Notices abroad | Receipt under A&C s.3 with delivery evidence; Hague Service Convention (in force for India 1 Aug 2007) not a mandatory channel for ADR notices; Central Authority only for court process | A&C s.3; NYC Art. V(1)(b) | IN_FORCE | Notice engine evidence (P02) |
| Limitation (India seat) | Limitation Act 1963 applies to arbitrations (A&C s.43); arbitration commences on receipt of the request (s.21) | A&C ss.21, 43 | IN_FORCE | Limitation pre-check (§4.6) |
| Foreign counsel | ICA only; client principal office abroad; foreign/international law issues only; Indian-law issues need Indian counsel | BCI Rules 2022 as amended 13 May 2025; *BCI v A.K. Balaji* (2018) 5 SCC 379 | IN_FORCE | LR-INT-019; F-INT-19 |
| FEMA | Award/settlement damages are current-account; capital-account-linked payments need NDI pricing advisory; curable FEMA breach is not a public-policy bar | FEMA 1999 s.5; FEM (Non-Debt Instruments) Rules 2019; *Vijay Karia* | IN_FORCE | LR-INT-014; G4 |
| LRS | Resident individuals capped at USD 250,000 per financial year; TCS under Income-tax Act 2025 s.394 | RBI Master Direction – LRS | IN_FORCE | LR-INT-015 |

### 3.2 Subtype-specific framework

| L2 | Statute / instrument | Forum (non-ADR) | Limitation / time bars (India-law default; foreign law per governing law) | Recent case law / status |
|---|---|---|---|---|
| `int.sale_of_goods` | Sale of Goods Act 1930 (if Indian law governs) [K]; CISG only by choice or PIL (India not a party); Incoterms 2020 (ICC Pub. 723) [K]; UNIDROIT Principles 2016 as rules of law | Commercial Court (Commercial Courts Act 2015) | Price of goods sold and delivered: Limitation Act Sch., Art. 14 (3 years from delivery, no fixed credit) [K]; breach of contract: Art. 55 (3 years) [K]; CISG Art. 39 notice of non-conformity within reasonable time, outer limit two years [K] | *Glencore v Shree Ganesh Metals* (2025): arbitration agreement by conduct in commodity contracts |
| `int.services` | Indian Contract Act 1872; IT Act 2000 (e-contracts s.10A) | Commercial Court | Art. 55 (3 years) [K] | — |
| `int.distribution_agency` | Indian Contract Act ss.182–238 (agency; s.205 compensation for revocation without reasonable notice) [K]; Competition Act 2002 s.3(4); EU Directive 86/653/EEC [K] | CCI (competition effects — not arbitrable as such) | Art. 55 [K] | — |
| `int.jv_shareholder` | Companies Act 2013 (SHA enforceability vs articles); FEMA NDI Rules 2019 (pricing of transfers between residents and non-residents) [K]; Specific Relief Act 1963 | NCLT for ss.241–242 reliefs; High Court | Art. 55 / Art. 113 [K] | *NTT Docomo v Tata Sons* (Del HC 2017) and *Vijay Karia* (2020): put-option awards enforceable, FEMA curable; *Gokul Patnaik v Nine Rivers Capital* (SLP dismissed 22 Apr 2026): SIAC put-option award enforcement upheld |
| `int.technology_licensing` | Patents Act 1970 ss.68–69 (licences in writing; registration) [K]; Copyright Act 1957; Trade Marks Act 1999; FEMA current-account royalties [K] | IP offices / High Court for validity, infringement against third parties | Art. 55 [K] | *Vidya Drolia* (2021) 2 SCC 1: grant/registration of IP non-arbitrable; licence disputes in personam arbitrable |
| `int.epc_construction` | Indian Contract Act s.73–74 (liquidated damages; reasonable compensation) [K]; FIDIC 2017 conditions (contractual) [K] | Commercial Court | Art. 55 [K]; FIDIC 28-day contractual notices (contractual time bars — enforceability is for the tribunal) | — |
| `int.shipping_logistics` | Carriage of Goods by Sea Act 2025 (Act 19 of 2025) Schedule (Hague-Visby based); Admiralty (Jurisdiction and Settlement of Maritime Claims) Act 2017 [K]; Multimodal Transportation of Goods Act 1993 [K] | High Court (admiralty) for arrest; Equator never arrests vessels | **One year** from delivery or due delivery (Art. III(6)) — owned clock `int_hv_time_bar` | Act in force 10 Sep 2025 per India Code |
| `int.trade_finance` | UCP 600 (Art. 4 autonomy; Art. 5 documents not goods; Art. 14(b) maximum five banking days to examine; Art. 16 refusal notice) [K]; ISP98; URDG 758 (Art. 5 independence; Art. 15 demand requirements) [K] | High Court (injunction against encashment only for egregious fraud/irretrievable injustice) | Art. 55 [K] | *U.P. Coop. Federation v Singh Consultants* (1988) 1 SCC 174 (LR-INT-022) |
| `int.energy` | Electricity Act 2003 ss.79(1)(f), 86(1)(f) [K]; PNGRB Act 2006 (PNGRB matters excluded from mediation, Mediation Act First Schedule) | CERC/SERC; APTEL; PNGRB | Art. 55 [K] | *GUVNL v Essar Power* (2008) 4 SCC 755 [K] |
| `int.investment_private` | Indian Contract Act; FEMA NDI Rules 2019; SEBI takeover rules where a listed target is involved (signpost only) [K] | High Court; NCLT (schemes) | Art. 55 [K] | *Gokul Patnaik* (2026) |

**AI rule for §3 content:** the Dispute Explorer may display these rows as facts with their citation; it may not say whether a claim is in time or strong (NN-01 GX-1/GX-2). Limitation outputs are "indicative date per inputs; confirm with counsel" (§12.4).

---

## 4. Suitability and eligibility rules

All rules below are deterministic rows in `packages/rules/verticals/int/suitability.v1.json`, evaluated in order; the first `reject` or `signpost` short-circuits; `accept_with_conditions` accumulates conditions. Each row cites its Appendix G rule. Output object: `{outcome, outcome_code, conditions[], signposts[], clocks_to_open[], disclosures[], rule_ids[]}`.

### 4.1 Decision table

| # | Inputs (form fields) | Condition | Outcome | Outcome code | Conditions / signposts | Rule |
|---|---|---|---|---|---|---|
| S-01 | `respondent_type`, `claim_basis` | respondent is a State/State organ **and** claim is under a bilateral investment treaty, FTA investment chapter or ICSID | signpost | `OUT-INT-SIGNPOST-ISDS` | ICSID/PCA/UNCITRAL ad hoc; India Model BIT 2016 note | LR-INT-016 |
| S-02 | `forum_requested`, `parties_all_states` | WTO dispute, trade-remedy challenge against a Government measure, or all parties are States | signpost | `OUT-INT-SIGNPOST-WTO` | Department of Commerce (Trade Policy Division); DGTR (trade remedies); DGFT (origin/SCOMET) | LR-INT-016 |
| S-03 | `claimant_capacity` | claimant acts as consumer (personal, non-business purchase) | signpost | `OUT-INT-SIGNPOST-CONSUMER` | e-Jagriti; National Consumer Helpline | NN-06 (*Emaar*) |
| S-04 | `criminal_flags[]` | any of: offence alleged as the primary relief, cheating/forgery complaint pending and relief sought is prosecution/withdrawal, threats or violence, matter needs police protection, sanctions evasion or terrorism financing allegation | reject + signpost | `OUT-INT-REJECT-CRIMINAL` | Police/Magistrate; ED (FEMA contravention); FIU-IND (bank-side reporting) | NN-24; App. K §3 |
| S-05 | `criminal_flags[]`, `civil_relief_separable` | parallel criminal complaint exists **and** a separable civil money/contract dispute is sought to be resolved | accept_with_conditions | `OUT-INT-ACCEPT-CIVIL-ONLY` | Civil dimension only; settlement may not provide for withdrawal of a non-compoundable complaint; compounding is for the court | NN-24 |
| S-06 | `sanctions_status` (G1 pre-screen) | potential or confirmed match on UN/MHA/OFAC/EU/UK lists | hold | `OUT-INT-HOLD-SANCTIONS` | Compliance review; parties see "under compliance review" only (VG-INT-03) | LR-INT-012 |
| S-07 | `ica_flag`, `intl_mediation_flag`, `seat_country` | both flags false **and** seat in India | reroute | `OUT-INT-REROUTE-COM` | Carry answers to COM intake | LR-INT-001; LR-MED-016 |
| S-08 | `relief_types[]` | relief is in rem or reserved to a statutory forum: IP validity/grant/registration, oppression/mismanagement (NCLT), winding up/insolvency, competition infringement finding, CERC/SERC exclusive matters, vessel arrest | signpost (for that relief) + accept remaining in-personam claims if any | `OUT-INT-PARTIAL-SIGNPOST` | Named forum per §2.2; arbitration blocked for the excluded relief (NN-06) | LR-ARB-019 |
| S-09 | `urgent_relief_needed`, `relief_target` | urgent relief needed against a non-party (bank, carrier, vessel) or anti-suit injunction | accept_with_conditions | `OUT-INT-ACCEPT-COURT-INTERIM` | Court route for the interim measure (A&C s.9 India seat; s.9 for foreign seat unless excluded; local court abroad); EA offered only against parties to the agreement | LR-ARB-025 |
| S-10 | `urgent_relief_needed`, `relief_target = party` | urgent relief against a party to the arbitration agreement | accept_with_conditions | `OUT-INT-ACCEPT-EA` | EA application F-INT-07; seat-enforceability notice | LR-ARB-025 |
| S-11 | `agreement_exists`, `agreement_evidence[]` | no written agreement and no exchange evidencing one | accept_with_conditions (mediation only) | `OUT-INT-ACCEPT-IMED-ONLY` | Arbitration needs a post-dispute submission agreement (e-signed by all) | LR-ARB-027 |
| S-12 | `agreement_names_other_institution` | clause names SIAC/ICC/LCIA/HKIAC/other institution | signpost (arbitration) + accept mediation | `OUT-INT-SIGNPOST-OTHER-INSTITUTION` | Name the institution; arbitration at Equator only on a new all-party submission agreement | LR-ARB-027 |
| S-13 | `seat_country` | seat in a non-NYC state or an NYC state not notified under s.44(b) (incl. UAE/DIFC/ADGM) | accept_with_conditions | `OUT-INT-ACCEPT-SEAT-ACK` | Explicit acknowledgement F-INT-04 `ack_non_notified_seat`; enforcement-in-India card | LR-INT-006, LR-INT-025 |
| S-14 | `agreement_date` | before 6 Sep 2012 and seat outside India | accept_with_conditions | `OUT-INT-ACCEPT-LEGACY` | *Bhatia International* legacy notice | LR-INT-002 |
| S-15 | `limitation_precheck` | indicative limitation date (§12.4) passed and no acknowledgement/extension evidence | accept_with_conditions | `OUT-INT-ACCEPT-LIMITATION-NOTICE` | Show computed date and "the tribunal decides limitation"; never refuse on this ground (NN-01) | LR-ARB (A&C s.43) |
| S-16 | `l2_code = int.shipping_logistics`, `cargo_claim`, `delivery_date` | cargo claim and less than 60 days to the one-year bar | accept_with_conditions | `OUT-INT-ACCEPT-TIMEBAR-URGENT` | Open owned clock `int_hv_time_bar` with T-30/T-7/T-1; advise commencing arbitration (s.21 request) or obtaining a written time extension from the carrier | LR-INT-023; NN-04 |
| S-17 | `respondent_type = state_entity_commercial` | a State-owned enterprise or foreign Government acting in a commercial capacity under a contract | accept_with_conditions | `OUT-INT-ACCEPT-STATE-ENTITY` | Registrar review: sovereign-immunity waiver clause, authority to arbitrate, enforcement-against-State-assets notice | A&C s.2(1)(f)(iv) |
| S-18 | `counsel_foreign`, `issues_of_law[]` | foreign counsel on record and Indian law is among issues | accept_with_conditions | `OUT-INT-ACCEPT-INDIAN-COUNSEL` | Indian counsel must be added for Indian-law issues | LR-INT-019 |
| S-19 | `eu_party` | any party established in the EU/EEA | accept_with_conditions | `OUT-INT-ACCEPT-EU-AI-CLERICAL` | AI limited to clerical/translation/summary; GDPR notice; Art. 27 representative check | LR-INT-020; NN-30 |
| S-20 | default | none of the above | accept | `OUT-INT-ACCEPT-ICA` or `OUT-INT-ACCEPT-IMED` | Ladder per §2.2 | — |

### 4.2 Hard exclusions (non-configurable; tenants cannot unblock — FR-P08-02)

| Code | Exclusion | Basis | Signpost |
|---|---|---|---|
| HX-INT-01 | Investor-state / treaty claims | Master §1.2 INT; LR-INT-016 | ICSID, PCA, UNCITRAL ad hoc |
| HX-INT-02 | WTO/state-to-state trade disputes | WTO DSU Arts. 1, 3, 4, 6 | Department of Commerce; DGTR; DGFT |
| HX-INT-03 | Criminal proceedings or mediation of an offence; non-compoundable offences; terrorism financing; sanctions evasion | NN-24; UAPA 1967 ss.35, 51A | Police; Magistrate; ED |
| HX-INT-04 | Awards on in-rem or statutory-forum matters (IP validity, insolvency, oppression, winding up, competition findings, CERC/SERC exclusive, admiralty arrest) | NN-06; *Vidya Drolia* | §2.2 forum column |
| HX-INT-05 | Any party, UBO (≥ 10%), counsel, funder or neutral with an unresolved confirmed sanctions hit | LR-INT-012 | Compliance closure letter (no details) |
| HX-INT-06 | Cross-border consumer disputes | NN-06; master INT scope (B2B) | e-Jagriti |
| HX-INT-07 | Unilateral appointment by one party of the sole/presiding arbitrator; enterprise/repeat-player nomination | NN-03; *CORE* (2024) | — (blocked control) |

### 4.3 Urgent and safety triggers

| Trigger | Detection | Action | SLA |
|---|---|---|---|
| Asset dissipation / imminent bond or LC encashment | F-INT-02 `urgent_relief_needed = true` + `relief_target` | EA lane (party) or court route card (non-party bank) within the same session | EA appointment ≤ 1 business day (cap 2) |
| Cargo time bar ≤ 60 days | S-16 | Owned clock + Registrar task | Task created at intake |
| Vessel about to leave port | `vessel_departure_at` within 7 days | Court route card (admiralty arrest is a court remedy) | Immediate |
| Threats, coercion, extortion | free-text classifier (AI may flag; rule decides) + checkbox | NN-24 reject + signpost; case manager review | Same day |
| Party designated mid-case | `IntlSanctionsRescreenWorkflow` hit | Freeze fee collection, payouts and award release; Registrar + compliance officer | ≤ 1 business day |

### 4.4 Jurisdiction and internationality computation (gate G5)

```text
ica_flag = any(party in parties where
   party.nationality != 'IN' (individuals) or party.habitual_residence != 'IN'
   or party.incorporation_country != 'IN' (bodies corporate)
   or party.central_management_country != 'IN' (associations/bodies of individuals; also companies for evidence only)
   or party.kind == 'foreign_government')
   and legal_relationship_commercial == true
   -- TDM Infrastructure: an India-incorporated company is NOT foreign even if controlled abroad
intl_mediation_flag = any(party where
   party.nationality != 'IN' or party.habitual_residence != 'IN' (individuals)
   or party.place_of_business_country != 'IN' (bodies corporate incl. LLP; associations)
   or party.kind == 'foreign_government')
   and dispute_commercial == true
foreign_seat_indian_parties = (not ica_flag) and seat_country != 'IN'
```

Evidence required per party (G5 cannot clear without it): certificate of incorporation (bodies corporate), registered/place-of-business proof, passport or residence permit (individuals), board-seat/management evidence where central management is claimed. Each evidence item is stored with hash (NN-22). A party may contest G5 by uploading counter-evidence; the Registrar decides with reasons (`InstitutionalDecision`, Appendix N).

### 4.5 Seat-dependent jurisdiction matrix

| Seat | Lex arbitri | Supervisory court | Challenge route | Enforcement in India | Equator default label |
|---|---|---|---|---|---|
| New Delhi / Mumbai / other Indian city | A&C Part I | High Court (for ICA, "Court" means the High Court — A&C s.2(1)(e)(ii)) [K] | s.34 (no s.34(2A) for ICA) | s.36 as decree | "India seat (Part I)" |
| GIFT City IFSC | A&C Part I | Gujarat High Court [K] | s.34 | s.36 | "India seat — GIFT IFSC (Part I). No IFSC arbitration centre exists; Equator administers under its own Rules." |
| Singapore | International Arbitration Act 1994 (Singapore) [K] | Singapore High Court / SICC [K] | Singapore court | Part II (notified) | "Foreign seat" |
| London | Arbitration Act 1996 as amended by Arbitration Act 2025 (UK) [K] | English High Court | English court | Part II (notified) | "Foreign seat — law of arbitration agreement required" |
| Dubai (DIFC / onshore), Abu Dhabi (ADGM) | DIFC Arbitration Law / UAE Federal Arbitration Law No. 6 of 2018 / ADGM Arbitration Regulations 2015 [K] | DIFC Courts / Dubai courts / ADGM Courts [K] | Local court | **Not Part II** (UAE not s.44(b) notified) → suit on the award or on the claim in India | "Foreign seat — not India-notified" (`INT_SEAT_NOT_NOTIFIED` ack) |
| Hong Kong | Arbitration Ordinance (Cap. 609) [K] | HK Court of First Instance | HK court | Part II (notified 2012, S.O. 580(E)) | "Foreign seat" |
| Paris | French Code of Civil Procedure (arbitration book) [K] | Paris Court of Appeal [K] | French court | Part II (France notified) [K] | "Foreign seat" |
| Other | configured in `intl.country_profiles` | — | — | per profile | per profile |

### 4.6 Limitation pre-checks (indicative only)

| Check | Input | Output | Owner |
|---|---|---|---|
| India-law claim limitation | `cause_of_action_date`, `claim_category` (DL-INT-31), `acknowledgement_dates[]` (Limitation Act s.18 [K]) | indicative last date; "confirm with counsel" | rules engine; display only |
| Commencement date | Request for Arbitration received by respondent (A&C s.21) — from notice engine delivery evidence | `commenced_on` | notices |
| Hague-Visby time bar | `delivery_date` or `due_delivery_date`; carrier extension letters | owned clock `int_hv_time_bar` (NN-04) | Registrar |
| Contractual time bars (FIDIC notices, DAAB NOD) | event date; configured period (28 days default) | service clock; tribunal decides effect | case_manager |
| Foreign-award enforcement in India | award receipt date | indicative 3 years (Art. 137; *Vedanta* (2020)) — accrual point is legal question | display only |
| s.11 petition (ad hoc failure) | date of s.21 notice and refusal | 3 years (Art. 137; *Arif Azim v Aptech* 2024 INSC 155) | display only |

---

## 5. Dispute Explorer question tree

Common rules (Appendix K): plain English, reading level ≤ class 8, one question per screen, ≤ 12 questions to an outcome, every answer saved to `core.form_submissions` (draft), "Not sure" always available and routed to the deterministic default, language switch at any point. Free-forum disclosures appear **before** any fee screen (NN-20, NN-29). AI may rephrase questions and classify free text into an L2 with a confidence score; any classification below 0.80 is shown to the user to confirm; routes and clocks come only from §4 (NN-01, NN-02). Bilingual parity tests cover every node (NN-23).

### 5.1 Entry tree (shared)

| QID | Question (plain English) | Answer options | Branching |
|---|---|---|---|
| INT-Q00 | Is this a dispute between businesses (or a business and a government company) in different countries? | Yes · No, I am buying for personal use · No, both are in India · Not sure | Yes → Q01 · personal use → `OUT-INT-SIGNPOST-CONSUMER` · both in India → Q00a · Not sure → Q01 |
| INT-Q00a | Has your contract chosen a place of arbitration outside India? | Yes · No · No contract · Not sure | Yes → Q01 (PASL path) · No/No contract → `OUT-INT-REROUTE-COM` · Not sure → upload contract → AI extracts clause → Registrar confirms; Not sure and no upload → `OUT-INT-REROUTE-COM` with a note that the case returns to INT if a foreign seat is later shown (answers carried) *(v3.1: the no-upload path had no route)* |
| INT-Q01 | Who is the other side? | A private company · A government-owned company · A government or ministry · A person in business | Government/ministry → Q01a · others → Q02 |
| INT-Q01a | Is your claim based on an investment treaty or a WTO rule? | Investment treaty · WTO / trade rule · A normal contract · Not sure | Treaty → `OUT-INT-SIGNPOST-ISDS` · WTO → `OUT-INT-SIGNPOST-WTO` · Contract → Q02 (flag S-17) · Not sure → Q02 (registrar review) |
| INT-Q02 | Has anyone made threats, used force, or committed a crime that you want punished? | Yes · There is a police complaint but I only want my money · No | Yes → `OUT-INT-REJECT-CRIMINAL` · police complaint → Q02a · No → Q03 |
| INT-Q02a | Can the money or contract part be settled without asking for the complaint to be dropped? | Yes · No · Not sure | Yes → Q03 (S-05) · No → `OUT-INT-REJECT-CRIMINAL` · Not sure → Q03 (S-05, case manager review) |
| INT-Q03 | What is the dispute mainly about? | Goods sold/bought · Services or software · Distributor, agent or franchise · Joint venture or shares · Licence of technology, brand or patent · Construction or project work · Shipping, cargo or freight · Letter of credit, bank guarantee or trade finance · Power, oil, gas or energy · Buying or selling a business · Something else | sets `l2_code`; → Q04 |
| INT-Q04 | Does your contract have a clause on how to settle disputes? | Yes — it names Equator · Yes — it names another centre (SIAC, ICC, LCIA, HKIAC, other) · Yes — arbitration without a named centre · Yes — mediation only · No clause · Not sure | names other → `OUT-INT-SIGNPOST-OTHER-INSTITUTION` (mediation still offered) · No clause → Q05 with `agreement_exists = false` · others → Q05 |
| INT-Q05 | What would you like to do first? | Talk and settle with help (mediation) · Get a binding decision (arbitration) · First mediate, then arbitrate if needed · Only negotiate online · Not sure | sets `l1_code` and ladder; Not sure → shows ladder comparison card (facts only) → user picks |
| INT-Q06 | Do you need urgent protection in the next few days (for example, to stop a bank guarantee being cashed or assets being moved)? | Yes — against the other party · Yes — against a bank, ship or someone else · No | party → S-10 card · non-party → S-09 court card · No → Q07 |
| INT-Q07 | Roughly how much is the dispute worth, and in which currency? | amount + currency (USD, EUR, GBP, SGD, AED, INR, other) · Not sure | computes value band (B1–B5) via FX snapshot |
| INT-Q08 | In which countries might you need to collect money or enforce the result? | multi-select countries · Not sure | populates enforcement targets; shows NYC / India-notified / Singapore Convention / apostille facts table |
| INT-Q09 | When did the problem start (or when was the payment due / goods delivered)? | date · Not sure | limitation pre-check (§4.6); shipping → S-16 |
| INT-Q10 | Is anyone paying your legal costs in return for a share of what you recover? | Yes · No · Not sure | Yes → TPF disclosure (F-INT-06) required |

### 5.2 `int.ica` sub-tree (arbitration)

| QID | Question | Answer options | Branching / effect |
|---|---|---|---|
| ICA-Q01 | Where is the arbitration to take place (the "seat")? | New Delhi · Mumbai · Other Indian city · GIFT City (IFSC) · Singapore · London · Dubai (DIFC) · Dubai (onshore) · Abu Dhabi (ADGM) · Hong Kong · Paris · Other · Not decided | Non-notified seat → acknowledgement card (S-13); Not decided → seat comparison facts table (no recommendation, VG-INT-01) |
| ICA-Q02 | Which law governs the contract? | Indian law · English law · Singapore law · UAE law · New York law · Other · Not stated | ≠ seat law → Disortho warning |
| ICA-Q03 | Does the contract say which law governs the arbitration clause itself? | Yes (law) · No · Not sure | London seat + No → mandatory field later in F-INT-04 |
| ICA-Q04 | How many arbitrators does the contract say? | One · Three · Not stated | Not stated → Equator Rules default (one; three if value band ≥ B4 and any party requests within 15 days) |
| ICA-Q05 | Is this a dispute between equals (not a standard-form contract where one side is a repeat player)? | Yes · No · Not sure | sets `equal_footing_requested`; Registrar decides (NN-03) |
| ICA-Q06 | Would a decision on documents only, without a hearing, be acceptable? | Yes · No · Only if the amount is small | value ≤ USD 250,000 + Yes → Streamlined offered |
| ICA-Q07 | Would you like a very fast award (about 3 months after the first meeting), with fewer steps? | Yes · No · Explain more | Yes → Highly Expedited opt-in card (all parties must agree; no joinder/consolidation) |
| ICA-Q08 | Are other companies in your group or the other side's group involved, or are there related contracts? | Yes · No | Yes → joinder/consolidation notice (F-INT-17) |
| ICA-Q09 | Will you need interpretation or translation? | No · Yes (languages) | Yes → F-INT-08 |
| ICA-Q10 | Will a foreign lawyer represent you? | No · Yes | Yes → F-INT-19 issue-of-law attestation |

**Outcomes:** `OUT-INT-ACCEPT-ICA` (+ tier suggestion facts: Streamlined/Expedited/Highly Expedited/Standard eligibility), with conditions from §4.1.

### 5.3 `int.imed` sub-tree (mediation)

| QID | Question | Answer options | Branching / effect |
|---|---|---|---|
| IMED-Q01 | Has the other side agreed to mediate, or should Equator invite them? | Already agreed (clause or email) · Please invite them · Not sure | invite → invitation journey (§8) |
| IMED-Q02 | Which rules would you like to use? | Equator International Mediation Rules · UNCITRAL Mediation Rules 2021 (Equator administers) · Not sure | Not sure → facts card |
| IMED-Q03 | Where will you need to rely on the settlement? | India · A country that has joined the Singapore Convention · Another country · Not sure | India or another country → consent-award conversion card; Convention country → Art. 4 attestation card + note that a consent award and a Convention settlement are alternative routes (§13.3) |
| IMED-Q04 | Should the mediation be online, in person or both? | Online · In person (city) · Hybrid | online → LR-MED-008 consent at F-INT-10 |
| IMED-Q05 | Do you want the mediator to come from a different country than the parties? | Yes · No preference | sets `mediator_nationality_preference` |
| IMED-Q06 | Which language(s)? | multi-select | interpretation flag |
| IMED-Q07 | If mediation does not settle, should the matter go to arbitration? | Yes — Equator arbitration · Yes — as the contract says · No | sets AMA / med-arb ladder |

**Outcomes:** `OUT-INT-ACCEPT-IMED`, `OUT-INT-ACCEPT-IMED-ONLY` (no arbitration agreement), with conditions.

### 5.4 Free-forum and cost disclosures (shown before any fee screen)

| Disclosure ID | Shown when | Text (EN source; translated with legal review) |
|---|---|---|
| DISC-INT-01 | Every INT journey | "Equator is a private dispute resolution institution, not a court or government body. Fees are listed before you pay." |
| DISC-INT-02 | Q01a = treaty/WTO | "Claims under investment treaties go to bodies such as ICSID or the PCA. WTO disputes are between governments only; businesses can raise concerns with the Department of Commerce." |
| DISC-INT-03 | IMED-Q03 = India | "India has signed but not ratified the Singapore Convention on Mediation. To make a settlement enforceable across borders, the parties can ask an arbitral tribunal to record it as a consent award." |
| DISC-INT-04 | Seat = UAE (any) | "India has not notified the UAE for enforcing foreign arbitral awards. An award made in the UAE may not be enforceable in India as a 'foreign award'; you may need to sue on it." |
| DISC-INT-05 | S-09 | "Urgent orders against banks, ships or other non-parties come from courts, not from Equator." |
| DISC-INT-06 | Every INT fee screen | "Prices are set in US dollars. Other currencies are shown at today's exchange-rate snapshot and fixed when you accept the quote. GST/withholding treatment is shown per payer." |

---

## 6. Intake and submission forms per mechanism

### 6.0 Form register (resolution rule: Appendix K §4 — form = f(vertical, L1, L2, mechanism, stage))

| Form ID | Title | Disposition (FR-P08-07) | L1 | Mechanism / stage | Status vs P08 |
|---|---|---|---|---|---|
| F-INT-01 | International onboarding & KYB | CORE+EXT | both | onboarding | P08 — fields detailed in §6.7 |
| F-INT-02 | Request for Arbitration (International) | VERTICAL | ica | arbitration / commencement | P08 — fields detailed in §6.3 |
| F-INT-03 | Answer to Request & Counterclaim | VERTICAL | ica | arbitration / response | P08 — §6.4 |
| F-INT-04 | Seat / Law / Language Election | VERTICAL | ica | pre-constitution | P08 — §6.3.3 |
| F-INT-05 | Sanctions & KYC/UBO Declaration | VERTICAL | both | gate G1/G2 | P08 — §6.7 |
| F-INT-06 | Third-Party Funding Disclosure | VERTICAL | both | filing + on change | P08 — §6.7 |
| F-INT-07 | Emergency Arbitrator Application | VERTICAL | ica | EA | P08 — §6.6 |
| F-INT-08 | Interpretation & Translation Request | VERTICAL | both | any | P08 — §6.7 |
| F-INT-09 | Enforcement Target Countries | VERTICAL | both | filing; award | P08 — §6.7 |
| F-INT-10 | Request for International Mediation | VERTICAL | imed | mediation / commencement | P08 — §6.2 |
| F-INT-11 | Data Transfer & Region Election | VERTICAL | both | gate G3 | P08 — §6.7 |
| F-INT-12 | Payment Route & Tax Treatment Declaration | VERTICAL | both | gate G4 | P08 — §6.7 |
| F-INT-13 | Trade Particulars (sector blocks) | VERTICAL | both | filing | P08 — §6.8 (L2 blocks) |
| F-INT-14 | Consent-Award Conversion Request | VERTICAL | both | post-settlement | P08 — §6.6 |
| F-INT-15 | Negotiation Request (International) | VERTICAL | imed | negotiation | **new** |
| F-INT-16 | Relevant Persons & Entities List | VERTICAL | both | filing + on change | **new** (ICC 2026 Art. 12(5) model) |
| F-INT-17 | Consolidation / Joinder / Coordinated Proceedings Application | VERTICAL | ica | proceedings | **new** |
| F-INT-18 | Early or Preliminary Determination Application | VERTICAL | ica | proceedings | **new** |
| F-INT-19 | Foreign Counsel Registration & Issue-of-Law Attestation | CORE+EXT (App. S §4) | both | representation | **new** |
| F-INT-20 | Procedure-Tier Election | VERTICAL | ica | pre-constitution | **new** |
| F-INT-21 | Security for Costs / Security for Claim Application | VERTICAL | ica | proceedings | **new** |
| F-INT-22 | Interpreter / Translator Declaration | TEMPLATE + e-sign | both | hearing | **new** |
| F-INT-23 | Publication Consent (INT) | CORE+EXT (App. R §3) | both | filing + award | **new** |
| F-INT-24 | Response to Mediation / Negotiation Invitation | VERTICAL | imed | response | **new** |
| F-INT-25 | Statement of Claim (International) | VERTICAL (AI Pleadings Studio compatible, App. M) | ica | pleadings | **new** |
| F-INT-26 | Statement of Defence & Counterclaim (International) | VERTICAL (App. M) | ica | pleadings | **new** |
| F-INT-27 | Same-Neutral Role-Switch Consent (med-arb) | VERTICAL + e-sign | both | med→arb | **new** (master §5.3) |
| F-INT-28 | Document Production Request (Redfern schedule) | BUILDER | ica | proceedings | **new** (IBA Rules 2020 Art. 3) |

All forms: schema ID `form.int.<slug>@<semver>`; pinned to the case at filing (NN-21); every free-text field ≤ 4,000 characters unless stated; uploads go to the DMS with hash (NN-22) and originals preserved (NN-32); every amount field = `{amount_minor: bigint, currency: DL-INT-01}`; dates ISO-8601 with time zone where time matters.

### 6.1 Common header block `HB-INT` (prefixes every INT form)

| field_id | label | type | required | options / dropdown | validation | help text |
|---|---|---|---|---|---|---|
| hb_case_ref | Equator case reference | text (read-only) | auto | — | `EQ/INT/...` pattern | Assigned on filing |
| hb_l1 | Dispute family | enum (read-only) | auto | DL-INT-02 | — | From Dispute Explorer |
| hb_l2 | Dispute type | enum | ✔ | DL-INT-03 | must be in §2.2 | You can change this before filing |
| hb_filer_party | Filing party | ref `core.case_parties` | ✔ | — | must be party or authorised representative (NN-27) | — |
| hb_filer_role | You are filing as | enum | ✔ | DL-INT-04 | representative needs active LoA (App. S §4) | — |
| hb_language_ui | Form language | enum | ✔ | DL-INT-24 | — | Legal text in other languages is "for convenience" unless certified (NN-32) |
| hb_timezone | Your time zone | IANA tz | ✔ | tzdb list | valid IANA id | Used for deadlines and hearing times |
| hb_consent_notice | Privacy notice acknowledged | checkbox + notice version | ✔ | — | current INT notice version (NN-15/NN-30) | Explains transfers, retention and your rights |

**Pre-fill (v3.1; FR-P08-86).** An LEI entered in `pb_lei` (or found by name search) fills legal name, jurisdiction of incorporation, registered address and direct/ultimate parent from GLEIF, shown for confirmation and used as G5 evidence (V2) without re-typing; Indian parties use the MCA/GSTN lookup instead. An uploaded contract pre-fills the clause, seat, governing law and law of the arbitration agreement fields of F-INT-04 with page anchors for confirmation. Explorer answers (INT-Q00–Q10, ICA/IMED sub-trees) are not asked again; the party sees them in a "We filled these — please check" summary.

### 6.2 `int.imed` — Negotiation request (F-INT-15), Mediation request (F-INT-10), Response (F-INT-24)

#### 6.2.1 F-INT-15 Negotiation Request (International)

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| neg_counterparty | Other party | party block (§6.7.1 subset: name, country, email, authorised contact) | ✔ | — | email + country mandatory | We will invite them |
| neg_issue_summary | What needs to be resolved | textarea | ✔ | — | 50–2,000 chars | Facts only; no offers here |
| neg_amount | Amount in issue | money | ✔ | DL-INT-01 | > 0 | — |
| neg_mode | Negotiation mode | enum | ✔ | DL-INT-35 (`assisted`, `blind_bid`, `structured_offers`) | blind bid only if both parties opt in | Blind bid: each side enters a figure; settles automatically if within the agreed gap |
| neg_blind_bid_gap_pct | Settlement gap for blind bid | integer % | when blind_bid | 1–25 | default 10 | Applied to the higher figure |
| neg_rounds_max | Maximum rounds | integer | ✔ | 1–5 | default 3 | — |
| neg_window_days | Negotiation window | integer days | ✔ | 7–30 | default 30 (ladder rung 1) | After this the next step in your clause starts |
| neg_offer_currency | Offer currency | enum | ✔ | DL-INT-01 | one currency per negotiation | FX shown for information only (VG-INT-07) |
| neg_next_step | If no settlement | enum | ✔ | DL-INT-36 | must be permitted by clause or new consent | — |
| neg_docs | Key documents | upload[] | ✖ | DL-INT-39 | ≤ 25 files, ≤ 50 MB each | — |

#### 6.2.2 F-INT-10 Request for International Mediation (extends P08 field list)

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| med_basis | Basis for mediation | enum | ✔ | DL-INT-05 (`clause`, `post_dispute_agreement`, `invitation`, `tribunal_referral_ama`, `court_referral_foreign`) | clause/agreement → upload | — |
| med_agreement_upload | Mediation clause or agreement | upload | when basis ∈ clause, agreement | PDF/DOCX/EML/MSG | hash stored | An email exchange is acceptable |
| med_rules | Rules | enum | ✔ | DL-INT-06 (`equator_intl_mediation_2026`, `uncitral_mediation_2021`) | UNCITRAL → Equator as administering institution and appointing authority | — |
| med_mode_legal | Legal mode | enum (system) | auto | `contractual` / `statutory` | `statutory` only if NN-05 flag ON and venue India | — |
| med_venue | Venue | enum | ✔ | DL-INT-07 (`online`, `hybrid`, physical city list) | online → `med_online_consent` | — |
| med_online_consent | I consent to the mediation being conducted online | checkbox + e-sign | when venue ∈ online, hybrid | — | per party (LR-MED-008) | — |
| med_parties | Parties | party blocks[] | ✔ | — | ≥ 2; each with country and place of business | Used for the international test (s.3(g)) |
| med_dispute_summary | Short description of the dispute | textarea | ✔ | — | 100–3,000 chars | — |
| med_issues | Issues for mediation | list (text) | ✔ | — | 1–15 items | — |
| med_amount | Amount(s) in issue | money[] | ✔ | DL-INT-01 | per head | — |
| med_mediator_count | Number of mediators | enum | ✔ | `1`, `2_co_mediation` | co-mediation fee per Card INT-MED using modifier `COMED_160` (1.6×; 0.8× each) — recommended extension of the Appendix B rule **[VERIFY — open (product): add INT-MED to `COMED_160` scope; Registrar quote until added]** | — |
| med_mediator_nomination | Joint nomination | ref neutral or external person | ✖ | — | off-panel nominee must accept Equator Neutral Code + disclosure; joint nomination window 10 days, then Equator appoints | SIMC r.4 benchmark |
| med_mediator_nationality_pref | Mediator nationality preference | enum | ✔ | DL-INT-08 (`neutral_nationality`, `no_preference`, `specified`) | — | — |
| med_language | Language(s) of mediation | enum[] | ✔ | DL-INT-24 | ≥ 1 | Interpretation via F-INT-08 |
| med_sector_expertise | Sector expertise wanted | enum[] | ✖ | DL-INT-03 | — | Used as allocation filter |
| med_confidentiality_undertaking | All non-counsel attendees will sign confidentiality undertakings 2 business days before sessions | checkbox | ✔ | — | must be true | SIMC r.9.4 benchmark |
| med_recording_ack | I understand mediation sessions are not recorded or transcribed | checkbox | ✔ | — | must be true (NN-11; LR-MED-006) | — |
| med_settlement_use_countries | Where may the settlement need to be relied on | country[] | ✔ | ISO-3166 | — | Drives Singapore Convention / consent-award card |
| med_ama_consent | If settled, record the settlement as a consent award | enum | ✔ | `yes`, `no`, `decide_later` | `yes` needs an arbitration agreement or F-INT-14 | §13.3 trade-off shown |
| med_sgconv_attestation_requested | Request Equator attestation for Singapore Convention use | checkbox | ✖ | — | available only if `med_ama_consent ≠ yes` | Art. 4(1)(b) |
| med_time_box_days | Mediation period | integer | ✔ | 30–120 | default 60; extension by consent ≤ 60 | ladder rung 2 |
| med_cost_split | Cost sharing | enum | ✔ | DL-INT-09 | default `equal_split` | Card INT-MED |
| med_invoice_currency | Invoice currency (your share) | enum | ✔ | DL-INT-01 (excl. INR for foreign payers) | fixed for the case (FX-6) | — |

#### 6.2.3 F-INT-24 Response to Mediation / Negotiation Invitation

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| resp_decision | Your response | enum | ✔ | `accept`, `accept_with_changes`, `decline`, `need_more_time` | `need_more_time` once, ≤ 14 days | Declining has no penalty unless your contract says otherwise |
| resp_changes | Changes requested | multi | when accept_with_changes | `rules`, `venue`, `mediator`, `language`, `timetable`, `cost_split` | — | — |
| resp_mediator_counter | Mediator nominee | ref | ✖ | — | same checks as nomination | — |
| resp_issues_added | Additional issues | list | ✖ | — | ≤ 15 | — |
| resp_representative | Representative | ref LoA | ✖ | — | NN-27 scope | — |
| resp_online_consent | Online consent | checkbox + e-sign | when online | — | LR-MED-008 | — |
| resp_decline_reason | Reason (optional) | enum | ✖ | `prefer_court`, `prefer_other_institution`, `no_dispute`, `other` | — | Helps us improve; not shared as a judgement |

Invitation treated as rejected (at the inviting party's election) if no acceptance within 30 days of delivery — Equator rule, configurable `int.imed.invitation_response_days`; benchmark UNCITRAL Model Law on International Commercial Mediation 2018 Art. 5(2) (30 days from the day the invitation was **sent**) [Verified 22 Oct 2026: UNCITRAL 2018 text]; Mediation Rules 2021 article **[VERIFY — open]**.

### 6.3 `int.ica` — Request for Arbitration (F-INT-02) and Seat/Law election (F-INT-04)

#### 6.3.1 F-INT-02 Request for Arbitration (International)

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| rfa_claimants | Claimant(s) | party blocks[] | ✔ | §6.7.1 | ≥ 1 | — |
| rfa_respondents | Respondent(s) | party blocks[] | ✔ | §6.7.1 | ≥ 1; address for service + email | Notices go here (A&C s.3) |
| rfa_non_signatories | Non-signatory parties proposed | party blocks[] | ✖ | — | each needs `consent_evidence[]` | Tribunal decides joinder (LR-ARB-029) |
| rfa_agreement_text | Arbitration agreement (exact text) | textarea | ✔ | — | 20–5,000 chars | Copy the clause word for word |
| rfa_agreement_source | Where the clause is found | enum | ✔ | DL-INT-10 | — | — |
| rfa_agreement_upload | Contract / correspondence containing the clause | upload[] | ✔ | DL-INT-39 | hash; date extracted | Email chains accepted (LR-ARB-027) |
| rfa_agreement_date | Date of the arbitration agreement | date | ✔ | — | < today; < 6 Sep 2012 → legacy notice | — |
| rfa_contracts_related | Other related contracts | list {title, date, parties, clause} | ✖ | — | — | Multi-contract claims (§7.6) |
| rfa_rules | Arbitration rules | enum | ✔ | DL-INT-11 | UNCITRAL → Equator appointing authority fee (Card INT-USD) | — |
| rfa_seat | Seat (proposed or agreed) | enum | ✔ | DL-INT-12 | non-notified → ack | — |
| rfa_tier_requested | Procedure tier requested | enum | ✔ | DL-INT-13 | eligibility check §7.2 | — |
| rfa_arbitrator_count | Number of arbitrators | enum | ✔ | `1`, `3`, `as_per_rules` | — | — |
| rfa_equal_footing_request | Request party nomination of co-arbitrators | checkbox | ✖ | — | only if `3` and not repeat-player; Registrar decides (NN-03) | — |
| rfa_nominee | Claimant's nominee (co-arbitrator) | ref neutral or external | when equal_footing approved | — | disclosure + conflict check + Appointments Committee confirmation | Never for sole/presiding |
| rfa_nationality_pref | Presiding/sole arbitrator nationality | enum | ✔ | DL-INT-08 | default `neutral_nationality` (LR-INT-005) | Parties may jointly agree otherwise in writing |
| rfa_language | Language of arbitration | enum[] | ✔ | DL-INT-24 | ≥ 1 | A&C s.22 |
| rfa_claims | Claims | claim heads[] {head_type DL-INT-14, description, amount, currency, interest_basis DL-INT-15, interest_rate_text, from_date} | ✔ | — | ≥ 1; currency per head | Calculators are indicative (§12) |
| rfa_reliefs_nonmoney | Non-money relief | list {type DL-INT-16, description} | ✖ | — | in-rem relief types blocked (HX-INT-04) | — |
| rfa_facts_summary | Summary of facts | textarea | ✔ | — | 200–8,000 chars | Full Statement of Claim follows (F-INT-25) unless Highly Expedited |
| rfa_combined_soc | Request includes full Statement of Claim | checkbox | ✔ if tier = highly_expedited | — | forces F-INT-25 fields inline | ICC 2026 App. VI model |
| rfa_ea_requested | Emergency relief needed | checkbox | ✖ | — | → F-INT-07 | — |
| rfa_ama_optin | Mediate first under the AMA Protocol | enum | ✔ | `yes`, `no`, `as_per_clause` | — | 8-week stay; consent award if settled |
| rfa_pre_steps | Pre-arbitration steps completed | enum[] | ✔ | DL-INT-17 | if clause requires steps not done → Registrar notice (not a bar) | — |
| rfa_tpf | Third-party funding | enum | ✔ | `none`, `yes` | `yes` → F-INT-06 mandatory | LR-INT-024 |
| rfa_relevant_persons | Relevant persons & entities | → F-INT-16 | ✔ | — | ≥ 1 row per party (self) | Drives conflict checks |
| rfa_counsel | Representatives | LoA refs[] | ✖ | — | foreign counsel → F-INT-19 | NN-27 |
| rfa_enforcement_targets | Enforcement countries | → F-INT-09 | ✔ | — | ≥ 1 or `unknown` | — |
| rfa_publication_pref | Publication preference | → F-INT-23 | ✖ | — | default `none` | Opt-in only (NN-26); a preference only — consent is taken after the award (App. R §3) |
| rfa_ai_protocol | AI-use protocol | enum | ✔ | DL-INT-18 | EU party → `clerical_only` forced (LR-INT-020) | — |
| rfa_fee_payer_currency | Invoice currency | enum | ✔ | DL-INT-01 | fixed per FX-6 | — |
| rfa_statement_of_truth | I confirm the facts stated are true to the best of my knowledge | checkbox + e-sign | ✔ | — | signatory authority checked (F-INT-01) | — |

#### 6.3.2 F-INT-20 Procedure-Tier Election

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| tier_choice | Procedure tier | enum | ✔ | DL-INT-13 | §7.2 eligibility matrix | — |
| tier_basis | Basis | enum | ✔ | `rules_default_by_value`, `party_agreement`, `registrar_decision_circumstances` | agreement → all-party e-sign | "Circumstances warrant" override (SIAC r.14 model) |
| tier_heap_waivers | I accept for Highly Expedited: no joinder or consolidation; no extension without all-party agreement; hearing may be dispensed with | checkbox[] | ✔ if HEAP | — | all three | ICC 2026 App. VI model |
| tier_unreasoned_award | Parties agree the award need not state reasons | checkbox (all parties) | ✖ | — | only HEAP/Streamlined; India seat → A&C s.31(3)(a); warn: some enforcement courts expect reasons **[VERIFY — open: per target country]** | — |
| tier_documents_only | Documents only (no oral hearing) | checkbox | ✔ if Streamlined | — | any party may request a hearing; tribunal decides | — |
| tier_opt_out_expedited | Opt out of Expedited (where value ≤ threshold) | checkbox (all parties) | ✖ | — | all-party e-sign | ICC 2026 opt-out model |

#### 6.3.3 F-INT-04 Seat / Law / Language Election (field detail)

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| sl_seat_country | Seat country | enum | ✔ | DL-INT-12 | — | — |
| sl_seat_city | Seat city | text/enum | ✔ | city list per country | IN → New Delhi/Mumbai/Bengaluru/Chennai/Kolkata/Hyderabad/Gandhinagar (GIFT IFSC)/other | — |
| sl_seat_is_ifsc | GIFT City IFSC seat | boolean (derived) | auto | — | true iff city = GIFT IFSC | Indian seat (LR-INT-021) |
| sl_venue | Hearing venue (if different) | enum | ✖ | `virtual`, `hybrid`, city list | venue ≠ seat note | Venue does not change the seat |
| sl_governing_law | Law governing the contract | enum + text | ✔ | DL-INT-19 | — | — |
| sl_law_of_agreement | Law governing the arbitration agreement | enum + text | ✔ if seat = GB; else ✖ | DL-INT-19 | — | UK Arbitration Act 2025 s.6A default = seat law [K] |
| sl_rules_of_law | Rules of law (optional) | enum | ✖ | DL-INT-20 | ICA only (A&C s.28(1)(b)) | — |
| sl_cisg | Does the CISG apply? | enum | ✔ for sale_of_goods | `excluded`, `applies_by_choice`, `applies_by_pil`, `not_sure` | Indian seller default `excluded` (LR-INT-018) | — |
| sl_ex_aequo | Tribunal may decide ex aequo et bono | checkbox (all parties) | ✖ | — | express authority (s.28(2)) | — |
| sl_languages | Language(s) | enum[] | ✔ | DL-INT-24 | — | — |
| sl_ack_foreign_seat | I understand Indian courts will not hear a challenge to a foreign-seated award and enforcement in India is under Part II | checkbox | ✔ if seat ≠ IN | — | — | TPL-INT-N02 |
| sl_ack_non_notified_seat | I understand this seat is not notified by India for enforcing foreign awards | checkbox | ✔ if non-notified | — | `INT_SEAT_NOT_NOTIFIED` until true | DISC-INT-04 |
| sl_exclude_s9_s27 | Exclude Indian court support under ss.9/27 (foreign seat) | enum | ✔ if seat ≠ IN | `no` (default), `yes` | — | s.2(2) proviso |
| sl_agreement_pre_2012 | Agreement dated before 6 Sep 2012 | boolean (derived) | auto | — | → legacy notice | *BALCO* |

### 6.4 `int.ica` — Response: Answer (F-INT-03) and Statement of Defence & Counterclaim (F-INT-26)

#### 6.4.1 F-INT-03 Answer to Request & Counterclaim

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| ans_due | Answer due | date (read-only) | auto | — | 30 days from delivery of Request (Standard/Expedited); 30 days (HEAP); 21 days (Streamlined) | Extension once, ≤ 14 days, Registrar |
| ans_jurisdiction_objection | Objection to jurisdiction | enum[] | ✖ | DL-INT-21 | must be raised no later than the Statement of Defence (A&C s.16(2)) | Tribunal decides (s.16) |
| ans_objection_grounds | Grounds | textarea | when objection | — | ≤ 5,000 chars | — |
| ans_position_seat | Position on seat / law / language | enum per item | ✔ | `agree`, `disagree_propose` | proposal fields as F-INT-04 | — |
| ans_position_tier | Position on procedure tier | enum | ✔ | `agree`, `disagree` | HEAP needs all-party agreement | — |
| ans_arbitrator_count | Position on number of arbitrators | enum | ✔ | `1`, `3`, `agree_with_claimant` | — | — |
| ans_nominee | Respondent's nominee | ref | when equal_footing approved | — | as rfa_nominee | — |
| ans_nationality_pref | Presiding nationality | enum | ✔ | DL-INT-08 | — | — |
| ans_summary_defence | Summary of defence | textarea | ✔ | — | 100–8,000 chars | — |
| ans_counterclaims | Counterclaims | claim heads[] | ✖ | DL-INT-14/15 | currency per head | Counterclaim fees per Card INT-USD on aggregate value |
| ans_setoff | Set-off pleaded | money[] + basis | ✖ | — | — | Counts toward sum in dispute |
| ans_tpf | Third-party funding | enum | ✔ | `none`, `yes` | → F-INT-06 | — |
| ans_relevant_persons | Relevant persons & entities | → F-INT-16 | ✔ | — | — | — |
| ans_ama_position | AMA mediation | enum | ✔ | `agree`, `decline` | — | — |
| ans_enforcement_targets | Respondent's own enforcement concerns (counterclaim) | → F-INT-09 | ✖ | — | — | — |
| ans_statement_of_truth | Statement of truth | checkbox + e-sign | ✔ | — | — | — |

Non-participation: if no Answer by `ans_due`, the case proceeds (A&C s.25(b) for India seat — failure to communicate defence is not an admission) [K]; the platform logs every delivery attempt for the Art. V(1)(b) shield (LR-INT-008).

#### 6.4.2 F-INT-25 Statement of Claim and F-INT-26 Statement of Defence & Counterclaim

Built in the AI Pleadings Studio (Appendix M; NN-25): sections `parties`, `jurisdiction_and_agreement`, `facts` (each sentence source-anchored), `issues`, `legal_basis` (only verified-corpus citations), `relief` (structured heads re-used from F-INT-02/03), `quantum_annex` (calculator outputs labelled indicative), `witness_list`, `expert_list`, `exhibits` (auto-numbered C-1…/R-1…), `document_production_requests` (→ F-INT-28), `statement_of_truth`. Additional INT fields:

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| soc_governing_law_submissions | Submissions on applicable law | textarea | ✖ | — | citations must resolve in verified corpus | — |
| soc_currency_of_award | Currency in which the award is sought | enum per head | ✔ | DL-INT-01 | — | Tribunal decides; FX conversion date stated |
| soc_conversion_date_basis | FX conversion date sought | enum | ✖ | `date_of_breach`, `date_of_award`, `date_of_payment`, `contract_specified` | — | — |
| soc_interest_post_award | Post-award interest sought | enum | ✔ | DL-INT-15 | India seat: s.31(7)(b) cannot be contracted out (LR-ARB-015) | — |
| soc_translations | Exhibits needing translation | list | ✖ | — | NN-32 labels | — |
| sod_jurisdiction | Jurisdiction objections maintained | enum[] | ✖ | DL-INT-21 | s.16(2) timing | — |
| sod_counterclaim_heads | Counterclaim heads | claim heads[] | ✖ | — | — | — |

Clocks: SoC due 30 days after constitution (Standard), 21 (Expedited), with Request (HEAP); SoD due 45/30/30 days; India seat: pleadings complete within 6 months of arbitrators' notice of appointment (A&C s.23(4); LR-ARB-011) — owned clock even for ICA.

### 6.5 L2 differences in core forms

The forms above are identical across L2 except: (a) F-INT-13 sector block (§6.8) is mandatory for the L2; (b) `int.trade_finance` adds `bank_consent_to_arbitrate` (bank parties must sign a submission agreement unless the instrument incorporates one); (c) `int.shipping_logistics` adds `time_bar_extension_upload`; (d) `int.jv_shareholder` and `int.technology_licensing` add the in-rem relief blocker list; (e) `int.energy` adds `regulator_jurisdiction_check` (CERC/SERC/PNGRB).

### 6.6 Vertical-specific procedural forms

#### 6.6.1 F-INT-07 Emergency Arbitrator Application

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| ea_filed_before_rfa | Filed before the Request for Arbitration | boolean | ✔ | — | true → `ea_rfa_due` = +7 days (SIAC Sch. 1 model) | Request must follow within 7 days or the EA application lapses |
| ea_relief | Relief sought | enum[] + text | ✔ | DL-INT-22 | relief against non-parties blocked (S-09) | — |
| ea_urgency | Why it cannot wait for the tribunal | textarea | ✔ | — | ≥ 200 chars | — |
| ea_prima_facie | Prima facie case | textarea | ✔ | — | — | — |
| ea_balance | Balance of convenience / irreparable harm | textarea | ✔ | — | — | — |
| ea_ppo_requested | Protective preliminary order without notice requested | checkbox | ✖ | — | foreign seat only by default; India seat → Registrar legal review; ex parte urgency routes to court under s.9 (A&C ss.18, 24; no Model Law Art. 17B equivalent) **[VERIFY — open (counsel): ex parte EA orders and natural justice for India seat]** | — |
| ea_undertaking | Undertaking in damages / security offered | enum + money | ✔ | `undertaking`, `security`, `none_with_reasons` | — | — |
| ea_seat_ack | I understand: India-seat EA orders are enforceable as s.17 orders; foreign-seat EA orders need a s.9 application in India | checkbox | ✔ | — | LR-ARB-025 | — |
| ea_fee_ack | EA fees (Card INT-USD: admin USD 3,000 + EA fee USD 12,500 default) | checkbox | ✔ | — | payment before appointment | — |

#### 6.6.2 F-INT-14 Consent-Award Conversion Request

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| cac_settlement_ref | Settlement document | ref `core.settlements` | ✔ | — | signed by all parties | — |
| cac_route | Conversion route | enum | ✔ | `ama_existing_tribunal`, `tribunal_constituted_for_purpose`, `s74_conciliation_india` | `tribunal_constituted_for_purpose` needs arbitration agreement + legal-review flag (App. A B05 **[VERIFY — open]**) | — |
| cac_arbitration_agreement | Arbitration agreement covering the dispute | ref/upload | ✔ unless s74 | — | — | — |
| cac_seat | Seat for the consent award | enum | ✔ | DL-INT-12 | non-notified seat → ack | — |
| cac_genuine_dispute_attest | Each party attests a genuine dispute existed and the settlement is not a means to move funds | checkbox + e-sign per party | ✔ | — | LR-INT-013 | — |
| cac_aml_review | AML red-flag review result | enum (system) | auto | `clear`, `enhanced_review`, `blocked` | rules §7.4 | — |
| cac_sgconv_tradeoff_ack | I understand a consent award is enforced under the New York Convention and is outside the Singapore Convention (Art. 1(3)) | checkbox | ✔ | — | [K] | §13.3 |
| cac_fee_ack | Conversion fee (Card INT-USD: USD 1,500 admin + USD 2,500 sole tribunal) | checkbox | ✔ | — | — | — |

#### 6.6.3 F-INT-17 Consolidation / Joinder / Coordinated Proceedings

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| cj_type | Application type | enum | ✔ | `consolidation`, `joinder_additional_party`, `coordinated_proceedings`, `single_arbitration_multiple_contracts` | HEAP → blocked (`INT_HEAP_JOINDER_BLOCKED`) | — |
| cj_cases | Other Equator case(s) | ref[] | when consolidation/coordination | — | same tenant | — |
| cj_party_to_join | Party to be joined | party block | when joinder | — | `consent_evidence[]` required for non-signatory | LR-ARB-029 |
| cj_common_questions | Common questions of law or fact | textarea | ✔ | — | — | — |
| cj_compatible_agreements | Arbitration agreements compatible (seat, rules, language) | enum | ✔ | `yes`, `no`, `partly` | `no` → consolidation refused unless all parties agree | — |
| cj_stage | Stage of each proceeding | enum | ✔ | `pre_constitution`, `constituted`, `post_pleadings` | post-constitution → tribunal decides; pre-constitution → Institutional Committee prima facie | — |
| cj_waiver_of_nomination | Parties waive party-nomination rights for a consolidated tribunal | checkbox (all parties) | ✖ | — | — | HKIAC Art. 29 model |

#### 6.6.4 F-INT-18 Early or Preliminary Determination

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| ed_type | Type | enum | ✔ | `early_determination_manifestly_without_merit`, `early_determination_manifestly_outside_jurisdiction`, `preliminary_issue` | — | ICC 2026 Art. 30; SIAC r.46 models |
| ed_target | Claim/defence targeted | ref claim heads[] | ✔ | — | — | — |
| ed_grounds | Grounds | textarea | ✔ | — | ≤ 5,000 chars | — |
| ed_efficiency | How this saves time and cost | textarea | ✔ | — | — | Tribunal may refuse without reasons on admissibility of the application |

Clocks: tribunal decides whether to admit within 14 days; decision on merits of the application within 60 days of admission (Equator default; configurable).

#### 6.6.5 F-INT-21 Security for Costs / Security for Claim

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| sec_type | Type | enum | ✔ | `security_for_costs`, `security_for_claim` | — | SIAC rr.48–49 models |
| sec_amount | Amount | money | ✔ | DL-INT-01 | — | — |
| sec_grounds | Grounds | enum[] + text | ✔ | `impecuniosity`, `asset_flight`, `tpf_without_adverse_costs_cover`, `non_enforcement_jurisdiction`, `other` | — | — |
| sec_form | Form of security | enum | ✔ | `bank_guarantee`, `escrow_deposit`, `parent_guarantee`, `atl_insurance` | escrow via ESCROW_PORT only (NN-13) | — |

#### 6.6.6 F-INT-27 Same-Neutral Role-Switch Consent

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| rs_mediation_ended_at | Mediation ended at | datetime (system) | auto | — | consent must be dated after this (master §5.3) | — |
| rs_statutory_mode | Statutory mode | boolean (system) | auto | — | true → form blocked (Mediation Act s.17; LR-MED-011) | — |
| rs_informed | I have read the explanation of risks (caucus information, impartiality, enforcement abroad — *Gao Haiyan v Keeneye* (HKCA 2011) [K]) | checkbox | ✔ | — | — | — |
| rs_consent | I consent to the mediator acting as arbitrator | e-sign per party | ✔ | — | all parties | — |
| rs_renewed_disclosure | Neutral's renewed s.12 disclosure | ref | ✔ | — | dated after consent | — |

#### 6.6.7 F-INT-28 Document Production Request (Redfern schedule)

Columns: `req_no`, `documents_requested`, `relevance_and_materiality` (IBA Rules 2020 Art. 3(3)), `objections` (DL-INT-23: `not_relevant`, `privilege`, `burden`, `confidentiality`, `not_in_possession`, `illegally_obtained`), `reply_to_objections`, `tribunal_decision` (`granted`, `granted_in_part`, `denied`, `withdrawn`). Export as XLSX/PDF; hash-stamped versions.

### 6.7 Compliance and party forms (field detail for P08 forms)

#### 6.7.1 F-INT-01 International onboarding & KYB (party block)

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| pb_kind | Party type | enum | ✔ | DL-INT-25 | — | — |
| pb_legal_name | Legal name (as registered) | text | ✔ | — | non-Latin script → also transliteration | — |
| pb_incorporation_country | Country of incorporation / registration | ISO-3166 | ✔ (bodies) | — | — | Used for s.2(1)(f) |
| pb_place_of_business | Principal place of business (country, address) | address | ✔ | — | — | Used for s.3(g) |
| pb_central_management_country | Country where central management and control is exercised | ISO-3166 | ✔ (associations; optional for companies) | — | evidence upload | — |
| pb_nationality | Nationality(ies) | ISO-3166[] | ✔ (individuals) | — | dual allowed | Neutral-nationality check |
| pb_habitual_residence | Habitual residence | ISO-3166 | ✔ (individuals) | — | — | — |
| pb_registry_number | Company / registry number | text | ✔ (bodies) | — | format per country profile | — |
| pb_lei | LEI | text (20) | ✖ | — | ISO 17442 checksum; GLEIF lookup | Speeds up verification |
| pb_tax_id | Tax identifier (GSTIN/PAN for Indian; foreign TIN) | text | ✔ | — | GSTIN/PAN format for IN | Tax treatment |
| pb_directors | Directors / managers | list {name, nationality, role} | ✔ (bodies) | — | ≥ 1 | Sanctions screening |
| pb_signatory | Authorised signatory | person + authority doc | ✔ | DL-INT-26 | board resolution / power of attorney; apostille or legalisation if foreign (LR-INT-017) | — |
| pb_signatory_limit | Signatory authority limit | money | ✖ | — | settlement above limit needs further authority (NN-27) | — |
| pb_contact_email | Email for notices | email | ✔ | — | verified by link | — |
| pb_contact_phone | Phone | E.164 | ✔ | — | — | International calls follow NN-12 consent rules where applicable |
| pb_address_service | Address for service | address | ✔ | — | — | A&C s.3 |
| pb_timezone | Time zone | IANA tz | ✔ | — | — | — |
| pb_state_entity | State-owned / Government entity | enum | ✔ | `no`, `soe_commercial`, `government` | `government` + treaty → S-01 | — |

#### 6.7.2 F-INT-05 Sanctions & KYC/UBO Declaration

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| ubo_rows | Beneficial owners (≥ 10% shares, capital, profits or control) | list {name, dob, nationality, residence, pct, control_type DL-INT-28} | ✔ | — | sum ≤ 100%; none above threshold → senior managing official row | Equator policy threshold ≥ 10% (LR-INT-012; `int.ubo_threshold_pct`), slightly stricter than PML Rules r.9(3)(a) (> 10%) |
| ubo_pep | Any UBO, director or signatory a politically exposed person | enum | ✔ | `no`, `yes` | yes → enhanced review | — |
| ubo_sanctioned_country_nexus | Business with comprehensively sanctioned countries/regions | enum + text | ✔ | `no`, `yes` | yes → G1 enhanced | — |
| ubo_source_of_funds | Source of funds for deposits | enum | ✔ | DL-INT-29 | third-party payer → identity + reason | — |
| ubo_documents | Supporting documents | upload[] | ✔ | DL-INT-39 | apostille/legalisation for foreign | — |
| ubo_declaration | Declaration of accuracy and duty to update within 7 days of change | checkbox + e-sign | ✔ | — | — | — |

#### 6.7.3 F-INT-06 Third-Party Funding Disclosure

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| tpf_exists | Funding arrangement exists | enum | ✔ | `none`, `litigation_funder`, `law_firm_contingency_abroad`, `insurer_ate`, `portfolio_funding`, `other` | — | Advocates enrolled in India may not take contingency fees (BCI Rules) — never accepted for Indian counsel |
| tpf_funder_name | Funder legal name | text | when exists | — | screened under G1 | Identity is disclosed to the tribunal and parties |
| tpf_funder_country | Funder country | ISO-3166 | when exists | — | — | — |
| tpf_control_rights | Funder has control or veto over settlement | enum | when exists | `none`, `consultation`, `veto` | — | Shown to tribunal only |
| tpf_adverse_costs_cover | Adverse-costs cover in place | enum | when exists | `yes`, `no`, `partial` | — | Relevant to security for costs |
| tpf_confidentiality_undertaking | Funder signs Equator confidentiality undertaking | e-sign (funder) | when exists | — | before any document access | Funder has no platform access by default |
| tpf_update_ack | I will update this disclosure within 7 days of any change | checkbox | ✔ | — | — | — |

#### 6.7.4 F-INT-16 Relevant Persons & Entities List

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| rp_rows | Persons/entities | list {name, relationship DL-INT-30, country, identifier} | ✔ | — | ≥ parent + ultimate parent + counsel firm | Equator runs conflicts against neutrals using this list |
| rp_update_ack | Update on any change | checkbox | ✔ | — | — | — |

#### 6.7.5 F-INT-08 Interpretation & Translation Request; F-INT-22 Interpreter Declaration

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| it_languages | Languages needed | pair[] {from, to} | ✔ | DL-INT-24 | — | — |
| it_mode | Interpretation mode | enum | ✔ | `simultaneous`, `consecutive`, `whispered`, `none` | simultaneous → separate audio channel | — |
| it_sessions | Sessions | ref sessions[] | ✔ if interpretation | — | — | — |
| it_docs_certified | Documents needing certified translation | ref documents[] | ✖ | — | each with target country standard | NN-32 labels |
| it_cert_standard | Certification standard | enum | when certified | DL-INT-32 | — | e.g., UAE: MOJ-licensed legal translator [K] |
| it_cost_payer | Who pays | enum | ✔ | `requesting_party`, `shared`, `as_tribunal_directs` | — | Actuals + 10% (Card INT-USD) |
| F-INT-22 decl_* | Interpreter declares impartiality, accuracy, confidentiality, no relationship with parties; lists languages and accreditation | e-sign | ✔ | — | before first session | — |

#### 6.7.6 F-INT-09 Enforcement Target Countries

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| et_country | Country | ISO-3166 | ✔ | — | — | — |
| et_asset_types | Asset types believed there | enum[] | ✖ | DL-INT-33 | — | Information only |
| et_facts | Facts table (auto) | read-only | auto | — | from `intl.country_profiles`: NYC party, India-notified (s.44(b)) with S.O. reference, Singapore Convention status + EIF, apostille member, translation language, notes | Facts only — no prospects (VG-INT-01) |

#### 6.7.7 F-INT-11 Data Transfer & Region Election; F-INT-12 Payment Route & Tax

| field_id | label | type | required | options | validation | help |
|---|---|---|---|---|---|---|
| dt_region | Primary storage region | enum | ✔ | `in_mumbai` (default), `sg` (flag), `eu` (flag) | non-IN needs DPO approval + DPA | NN-15 |
| dt_transfer_basis | Basis for transfers outside India | enum | ✔ | DL-INT-34 | negative-list check (none notified as of Oct 2026) | DPDP s.16 |
| dt_gdpr_basis | GDPR/UK GDPR basis (EU/UK parties) | enum | when EU/UK party | `art6_1_b_contract`, `art6_1_c_legal_obligation`, `art6_1_f_legitimate_interests`; special data `art9_2_f_legal_claims`; transfers `sccs_2021_914`, `uk_idta`, `art49_1_e_legal_claims` | — | — |
| dt_dpo_signoff | DPO sign-off | approval | ✔ for non-IN region | — | maker–checker | — |
| pr_payer_country | Payer country | ISO-3166 | ✔ | — | — | — |
| pr_account_type | FEMA account nature of the underlying payment | enum | ✔ | `current_account`, `capital_account`, `not_applicable` | capital → NDI advisory | LR-INT-014 |
| pr_lrs_individual | Resident individual remitting under LRS | boolean | ✔ | — | true → USD 250,000/FY + TCS s.394 notice | LR-INT-015 |
| pr_tax_treatment | GST treatment of Equator invoice | enum (system-proposed) | ✔ | DL-INT-37 | `T05` needs foreign recipient + convertible FX | LR-TAX-003 |
| pr_lut_on_file | Equator LUT reference | text (system) | auto | — | valid for FY | — |
| pr_withholding_gross_up | Foreign payer withholding — gross-up acknowledgement | checkbox | ✔ foreign payer | — | INT terms require gross-up (App. B) | — |

### 6.8 F-INT-13 Trade Particulars — L2 sector blocks

| L2 | Block fields (field_id: type; options) |
|---|---|
| `int.sale_of_goods` | `incoterm_code`: enum DL-INT-38; `incoterm_named_place`: text; `incoterm_version`: enum (`2020`, `2010`, `other`); `goods_hs_code`: text (6–8 digits); `quantity` + `unit`; `contract_price`: money; `delivery_date`: date; `inspection_certificate`: upload; `nonconformity_notice_date`: date; `cisg_status`: enum (from F-INT-04); `quality_expert_requested`: boolean |
| `int.services` | `sow_reference`: text; `acceptance_criteria_met`: enum (`yes`, `no`, `disputed`); `sla_credits_claimed`: money; `change_requests`: list; `ip_in_deliverables`: enum |
| `int.distribution_agency` | `relationship_type`: enum (`distributor`, `commercial_agent`, `franchisee`, `reseller`); `territory`: country[]; `exclusive`: boolean; `term_start`/`term_end`: date; `termination_notice_date`: date; `notice_period_days`: integer; `indemnity_or_compensation_claimed`: money; `eu_agent_law_applies`: enum (`yes`, `no`, `not_sure`); `competition_issue_flag`: boolean (→ CCI signpost) |
| `int.jv_shareholder` | `instrument`: enum (`sha`, `jva`, `spa`, `articles`); `company_name` + `cin`; `shareholding_pct` per party; `option_type`: enum (`put`, `call`, `drag`, `tag`, `rofr`, `deadlock`, `none`); `exit_price_formula`: text; `fema_ndi_pricing_relevant`: boolean (→ G4 capital account); `oppression_relief_sought`: boolean (→ NCLT signpost; HX-INT-04); `valuation_expert_requested`: boolean |
| `int.technology_licensing` | `ip_type`: enum[] (`patent`, `copyright`, `trademark`, `design`, `trade_secret`, `software`, `know_how`); `registration_numbers`: list; `licence_scope`: text; `royalty_basis`: enum (`running`, `lump_sum`, `minimum_guarantee`, `milestone`); `royalty_claimed`: money; `audit_rights_invoked`: boolean; `validity_challenge`: boolean (→ IP office signpost; arbitration blocked for validity); `source_code_escrow`: boolean |
| `int.epc_construction` | `contract_form`: enum (`fidic_red_2017`, `fidic_yellow_2017`, `fidic_silver_2017`, `fidic_1999`, `nec4`, `bespoke`, `other`); `daab_status`: enum (`no_daab`, `daab_decision_issued`, `nod_served`, `daab_not_constituted`); `daab_decision_date`, `nod_date`: date; `claim_types`: enum[] (`eot`, `variation`, `ld`, `disruption`, `payment`, `defects`, `bond_call`); `bond_type`: enum (`performance`, `advance_payment`, `retention`, `none`); `programme_upload`: upload |
| `int.shipping_logistics` | `transport_document`: enum (`bill_of_lading`, `sea_waybill`, `charterparty`, `multimodal`, `air_waybill`, `cmr`); `vessel_name` + `imo_number` (7 digits, checksum); `port_loading`/`port_discharge`: UN/LOCODE; `delivery_date` or `due_delivery_date`: date; `claim_type`: enum (`cargo_loss`, `cargo_damage`, `delay`, `demurrage`, `detention`, `freight`, `general_average`, `charter_hire`); `time_bar_extension_upload`: upload; `vessel_departure_at`: datetime (→ urgent card) |
| `int.trade_finance` | `instrument_type`: enum DL-INT-40; `instrument_number`; `issuing_bank` + country + SWIFT BIC; `confirming_bank`; `presentation_date`; `refusal_notice_date`; `discrepancies`: list {text, ucp_article}; `amount`: money; `expiry_date`; `fraud_alleged`: boolean (→ court card); `bank_consent_to_arbitrate`: enum (`yes`, `no`, `in_instrument`) |
| `int.energy` | `asset_type`: enum (`power_plant`, `transmission`, `lng`, `pipeline_gas`, `solar`, `wind`, `storage`, `equipment`, `om_services`); `contract_type`: enum (`ppa`, `gsa`, `spa_lng`, `epc`, `o_and_m`, `supply`); `price_review_clause`: boolean (→ expert determination option); `regulator_jurisdiction_check`: enum (`cerc`, `serc`, `pngrb`, `none`, `not_sure`) |
| `int.investment_private` | `transaction_type`: enum (`share_purchase`, `asset_purchase`, `subscription`, `merger`); `closing_date`; `claim_type`: enum (`warranty`, `indemnity`, `earn_out`, `completion_accounts`, `mac`, `non_compete`); `wi_insurance`: boolean; `notice_of_claim_date`; `de_minimis_and_cap`: text; `listed_target`: boolean (→ SEBI signpost note) |
| all | `trade_measure_impact` {type DL-INT-27, measure_reference, effective_date}; `fta_relevance` {agreement DL-INT-41, chapter} |

### 6.9 Dropdown master list (option values are stored codes; labels in `packages/i18n`)

| List | Name | Values (code — label) |
|---|---|---|
| DL-INT-01 | Currency | `USD` US dollar · `EUR` Euro · `GBP` Pound sterling · `SGD` Singapore dollar · `AED` UAE dirham · `INR` Indian rupee · `JPY` Japanese yen (claims only) · `CHF` Swiss franc (claims only) · `OTHER` (claims only; ISO-4217 code entry). Invoicing limited to `currencies.enabled` (App. B FX-1) |
| DL-INT-02 | L1 family | `int.ica` · `int.imed` · `int.out_of_scope` |
| DL-INT-03 | L2 type | `int.sale_of_goods` · `int.services` · `int.distribution_agency` · `int.jv_shareholder` · `int.technology_licensing` · `int.epc_construction` · `int.shipping_logistics` · `int.trade_finance` · `int.energy` · `int.investment_private` · `int.other` · (signpost) `int.state_treaty` · `int.wto_trade_measure` · `int.consumer_crossborder` · `int.criminal` |
| DL-INT-04 | Filing role | `party_self` · `party_org_user` · `counsel_indian` · `counsel_foreign` · `representative` |
| DL-INT-05 | Mediation basis | `clause` · `post_dispute_agreement` · `invitation` · `tribunal_referral_ama` · `court_referral_foreign` |
| DL-INT-06 | Mediation rules | `equator_intl_mediation_2026` · `uncitral_mediation_2021` |
| DL-INT-07 | Venue | `online` · `hybrid` · `new_delhi` · `mumbai` · `bengaluru` · `gift_ifsc` · `singapore` · `london` · `dubai` · `other_city` |
| DL-INT-08 | Neutral nationality preference | `neutral_nationality` (default) · `no_preference` · `specified` (country list) |
| DL-INT-09 | Cost split | `equal_split` · `claimant_pays` · `respondent_pays` · `as_agreed` (percentage) |
| DL-INT-10 | Clause source | `main_contract` · `separate_arbitration_agreement` · `terms_and_conditions_incorporated` · `purchase_order_acceptance` · `email_exchange` · `submission_agreement_post_dispute` |
| DL-INT-11 | Arbitration rules | `equator_intl_arbitration_2026` · `uncitral_2021_administered` · `uncitral_2021_appointing_authority_only` · `ad_hoc_equator_fundholding` |
| DL-INT-12 | Seat | `IN-DEL` New Delhi · `IN-BOM` Mumbai · `IN-BLR` Bengaluru · `IN-MAA` Chennai · `IN-CCU` Kolkata · `IN-HYD` Hyderabad · `IN-GIFT` GIFT City IFSC · `IN-OTH` other Indian city · `SG-SIN` Singapore · `GB-LON` London · `AE-DIFC` Dubai (DIFC) · `AE-DXB` Dubai (onshore) · `AE-ADGM` Abu Dhabi (ADGM) · `HK-HKG` Hong Kong · `FR-PAR` Paris · `CH-GVA` Geneva · `CH-ZRH` Zurich · `SE-STO` Stockholm · `NL-AMS` Amsterdam · `MU-MRU` Mauritius · `US-NYC` New York · `OTHER` |
| DL-INT-13 | Procedure tier | `streamlined_documents_only` · `highly_expedited` · `expedited` · `standard` |
| DL-INT-14 | Claim head type | `price_or_invoice` · `damages_breach` · `liquidated_damages` · `refund_restitution` · `royalty` · `commission` · `indemnity` · `demurrage_detention` · `freight_hire` · `lc_or_guarantee_amount` · `earn_out` · `warranty` · `interest_pre_award` · `costs` · `other` |
| DL-INT-15 | Interest basis | `contractual_rate` · `statutory_rate_governing_law` · `tribunal_discretion` · `reference_rate_plus_margin` (SOFR/€STR/SONIA/SORA/EIBOR/MIBOR + margin text) · `none_claimed` |
| DL-INT-16 | Non-money relief | `declaration_in_personam` · `specific_performance` · `injunction_inter_partes` · `delivery_of_goods_or_documents` · `account_and_audit` · `share_transfer_inter_partes` · (blocked) `ip_validity` · `winding_up` · `oppression_relief` · `vessel_arrest` |
| DL-INT-17 | Pre-arbitration steps | `negotiation_done` · `mediation_done` · `daab_decision_and_nod` · `expert_determination_done` · `cooling_off_period_elapsed` · `none_required` · `not_done` |
| DL-INT-18 | AI-use protocol | `ciarb_2025` · `svamc_2024` · `clerical_only` (forced for EU parties) · `none` |
| DL-INT-19 | Governing law | `IN` · `GB-ENG` · `SG` · `AE-ONSHORE` · `AE-DIFC` · `AE-ADGM` · `HK` · `US-NY` · `US-DE` · `CH` · `FR` · `DE` · `NL` · `other` (text) |
| DL-INT-20 | Rules of law | `unidroit_principles_2016` · `cisg_as_rules_of_law` · `lex_mercatoria` · `none` |
| DL-INT-21 | Jurisdiction objection | `no_arbitration_agreement` · `agreement_invalid` · `claim_outside_scope` · `non_arbitrable_subject` · `pre_conditions_not_met` · `wrong_institution` · `time_barred_claim_tribunal_to_decide` · `non_signatory_not_bound` |
| DL-INT-22 | EA relief | `preserve_status_quo` · `restrain_encashment_by_party` · `restrain_asset_disposal` · `preserve_evidence` · `deliver_documents_or_goods` · `restrain_share_transfer` · `security_for_claim` |
| DL-INT-23 | Document-production objection | `not_relevant` · `privilege` · `unreasonable_burden` · `commercial_confidentiality` · `not_in_possession` · `illegally_obtained` · `political_or_institutional_sensitivity` |
| DL-INT-24 | Languages | UN six: `ar` `zh` `en` `fr` `ru` `es`; Eighth Schedule 22: `as` `bn` `brx` `doi` `gu` `hi` `kn` `ks` `kok` `mai` `ml` `mni` `mr` `ne` `or` `pa` `sa` `sat` `sd` `ta` `te` `ur`; plus `de` `ja` `ko` `pt` `it` `nl` `tr` `id` `vi` `th` (interpretation only) — D2-09 |
| DL-INT-25 | Party kind | `company` · `llp` · `partnership` · `sole_proprietor` · `individual_in_business` · `trust` · `association` · `state_owned_enterprise` · `foreign_government` · `bank` · `insurer` |
| DL-INT-26 | Signatory authority document | `board_resolution` · `power_of_attorney` · `articles_authority` · `certificate_of_incumbency` · `secretary_certificate` |
| DL-INT-27 | Trade-measure impact | `none` · `ad_cvd` · `safeguard` · `tariff_change` · `qco_tbt` · `sps` · `export_control` · `sanctions` · `cbam` · `fta_origin_denial` |
| DL-INT-28 | UBO control type | `shares` · `capital` · `profits` · `voting_rights` · `board_appointment` · `other_control` · `senior_managing_official` |
| DL-INT-29 | Source of funds | `operating_revenue` · `group_funding` · `third_party_funder` · `insurer` · `bank_facility` · `other` |
| DL-INT-30 | Relevant-person relationship | `parent` · `ultimate_parent` · `subsidiary` · `affiliate` · `shareholder_10pct_plus` · `director` · `counsel_firm` · `funder` · `insurer` · `expert` · `witness` |
| DL-INT-31 | India-law claim category (limitation) | `price_goods_delivered` (Art. 14) · `breach_of_contract` (Art. 55) · `money_lent` (Art. 19) · `residual` (Art. 113) · `foreign_law_governs` (no computation) [K] |
| DL-INT-32 | Translation certification | `sworn_translator_target_country` · `consular_certified` (A&C s.47(2)) · `notarised_translator_india` · `moj_licensed_uae` · `machine_for_convenience` |
| DL-INT-33 | Asset type | `bank_accounts` · `receivables` · `real_estate` · `vessels` · `shares` · `inventory` · `ip` · `unknown` |
| DL-INT-34 | Transfer basis (DPDP) | `s16_permitted_not_restricted` · `s17_1_a_legal_claims` · `s17_1_d_non_resident_contract` · `consent` |
| DL-INT-35 | Negotiation mode | `assisted` · `blind_bid` · `structured_offers` |
| DL-INT-36 | Next step | `mediation_equator` · `arbitration_equator` · `as_per_clause` · `stop` |
| DL-INT-37 | GST treatment | `T01_B2B_INTRA` · `T02_B2B_INTER` · `T05_EXPORT_LUT` · `T08_IFSC` (flag `tax.ifsc_zero_rating`, App. B) · `T13_IMPORT_RCM` (Equator's own liability) |
| DL-INT-38 | Incoterms 2020 | `EXW` · `FCA` · `CPT` · `CIP` · `DAP` · `DPU` · `DDP` · `FAS` · `FOB` · `CFR` · `CIF` |
| DL-INT-39 | Accepted upload formats | PDF, PDF/A, DOCX, XLSX, CSV, EML, MSG, TXT, JPG, PNG, HEIC, TIFF, MP3, MP4, ZIP (scanned; ≤ 50 MB each) |
| DL-INT-40 | Trade-finance instrument | `lc_ucp600` · `standby_isp98` · `standby_ucp600` · `demand_guarantee_urdg758` · `bank_guarantee_indian_law` · `documentary_collection_urc522` · `factoring` · `supply_chain_finance` |
| DL-INT-41 | FTA | `india_uae_cepa` · `india_australia_ecta` · `india_efta_tepa` · `india_uk_ceta` · `india_mauritius_cecpa` · `india_asean_aitiga` · `india_japan_cepa` · `india_korea_cepa` · `other` |

---

## 7. Modus operandi per subtype

### 7.1 Core ICA step table (Equator International Arbitration Rules; applies to all L2 unless §7.5 overrides)

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| 1 | Claimant | Files F-INT-02 (+ F-INT-16, F-INT-06 if funded, F-INT-19 if foreign counsel), pays registration fee | — | agreement, contract, claim docs | `TPL-INT-N01` to respondent on registration | — |
| 2 | Case manager | Acknowledges filing; starts gates G0–G6 (FR-P08-69) | acknowledge ≤ 1 business day (Service Charter) | — | acknowledgement | — |
| 3 | Compliance officer / DPO / Registrar | Gates G1 sanctions, G2 KYC/UBO, G3 transfer, G4 FEMA, G5 internationality, G6 seat/law | median ≤ 5 working days (FR-P08-81) | F-INT-01, 05, 11, 12 | "under compliance review" only | clear / clear-with-conditions / hold |
| 4 | Equator | Serves Request (A&C s.3 evidence); commencement date recorded (s.21) | serve ≤ 2 business days after gates | Request + annexes | delivery receipts | — |
| 5 | Respondent | Files F-INT-03 Answer + counterclaim | 30 d (21 d Streamlined) | — | — | jurisdiction objection noted |
| 6 | Registrar | Tier decision (§7.2); number of arbitrators; `equal_footing` decision | ≤ 5 working days after Answer | F-INT-20 | tier notice | NN-03 decision with reasons |
| 7 | Appointments Committee / parties | Constitution: nominations (equal-footing only, 15 d), allocation of sole/presiding from Grade A/B + `END-INT` roster with conflict check against F-INT-16, nationality rule | sole: ≤ 21 d after Answer; three-member ≤ 30 d | Statement of Acceptance, Independence, Impartiality and Availability; Sixth Schedule disclosure; IBA 2024 list mapping | constitution notice | challenge window opens |
| 8 | Tribunal | Initial case management conference (CMC) and **Procedural Order No. 1** (`TPL-INT-P01`): timetable, IBA Rules 2020 as guidelines, Seoul Protocol hearing protocol, cybersecurity tier, data-protection annex, AI-use protocol, language/interpretation | CMC ≤ 21 d after constitution (Standard), 10 d (Expedited), 7 d (HEAP), 14 d (Streamlined) | PO-1 | PO-1 to parties | — |
| 9 | Parties | Statement of Claim / Defence & Counterclaim / Reply (F-INT-25/26) | per PO-1; India seat: s.23(4) six months owned clock | pleadings, exhibits | upload notifications | early determination (F-INT-18) |
| 10 | Parties / tribunal | Document production (Redfern F-INT-28), witness statements, expert reports | per PO-1 | — | — | tribunal orders |
| 11 | Tribunal / case manager | Hearing (virtual-first, §7.7) or documents-only determination | scheduler fairness rule | e-bundle with hash manifest (NN-10) | hearing notice T-21 d; test call T-7 d | recording only with all-party + tribunal consent (NN-11) |
| 12 | Tribunal | Closes proceedings; estimate of draft-award date | estimate ≤ 15 d after closure | — | closure order | — |
| 13 | Tribunal → Registrar | Draft award to scrutiny (form review; substance points flagged; no interference with decision) | draft ≤ 60 d after closure (INT); scrutiny ≤ 10 working days (5 Streamlined/HEAP) | draft award, computation annex | — | `form_approved` gate (App. N Scrutiny sub-committee for > USD 5m) |
| 14 | Tribunal | Signs award (DSC / eIDAS QES / wet-ink counterparts); India seat → e-stamp at execution state (LR-STAMP-001) | award target ≤ 3 months after final hearing/submission; s.29A advisory (LR-ARB-010) | award + AI non-delegation attestation | delivery to each party with receipt (LR-ARB-014) | release after costs settled |
| 15 | Equator | Issues enforcement pack (§13), certified copies, verification URL | ≤ 5 working days after release | pack | — | — |
| 16 | Parties | Post-award: correction/interpretation/additional award (s.33, 30 d); challenge at seat; enforcement | s.34: 3 months + 30 d (India seat) | — | — | status `award_issued → recognition_filed → enforceable_decree → executed` (LR-INT-009) |

### 7.2 Procedure tiers

| Tier | Eligibility | Tribunal | Written phase | Hearing | Award time limit | Fees (App. B) | Joinder / consolidation | Benchmark |
|---|---|---|---|---|---|---|---|---|
| Streamlined (documents-only) | sum ≤ `int.tier.streamlined_max_usd` (USD 250,000) by Rules default, or by agreement | sole | Request+SoC, Answer+SoD, one reply each | none unless tribunal decides | 90 days from constitution | Card INT-USD band ≤ 250,000 fixed fees | allowed only before constitution | SIAC r.13 / Sch. 2 (≤ SGD 1m; 3 months) |
| Highly Expedited | **opt-in by all parties only**; any value ≤ `int.tier.heap_max_usd` (default USD 4,000,000) | sole (Appointments Committee if no joint nomination in 20 days) | combined Request + SoC; Answer + SoD in 30 days; no further rounds without leave | may be dispensed with; max 1 day | **3 months from initial CMC**; no extension without all-party agreement | Card INT-USD with expedited −20% on tribunal fees | **not permitted** (`INT_HEAP_JOINDER_BLOCKED`) | ICC 2026 Appendix VI |
| Expedited | sum ≤ `int.tier.expedited_max_usd` (default USD 4,000,000; R-V6-02) unless all parties opt out; or by agreement; or Registrar decides circumstances warrant | sole, unless the agreement requires three and parties do not agree to one | SoC, SoD, one reply | 1 hearing, ≤ 3 days | 6 months from constitution, extendable once to 9 months by Registrar | expedited −20% on tribunal fees | allowed before constitution | ICC 2026 App. VI (EPP USD 4m); UNCITRAL Expedited Rules 2021 (6 months, max 9); SIAC r.14 |
| Standard | all other | 1 or 3 | per PO-1 | per PO-1 | Equator target 12 months from completion of pleadings (s.29A advisory for ICA) | Card INT-USD | allowed | — |

Tier transitions: Registrar may move a case from Expedited to Standard on application (counterclaim pushes value above threshold, complexity), reasons recorded; HEAP cannot be converted except by all-party agreement.

### 7.3 Emergency arbitrator (EA) procedure

| Step | Actor | Action | Clock |
|---|---|---|---|
| EA-1 | Applicant | F-INT-07 + EA fees; may file before Request | if before Request: Request due ≤ 7 days, else EA application lapses (`INT_EA_NOA_OVERDUE`) |
| EA-2 | Appointments Committee | Appoints EA from Grade A `END-INT` EA list (conflict check against F-INT-16) | target ≤ 1 business day; cap 2 business days |
| EA-3 | EA | Schedule (notice to respondent unless protective preliminary order sought — foreign seat default; India seat after legal review) | schedule ≤ 2 business days of appointment |
| EA-4 | EA | Order/award on emergency relief | ≤ 14 days from appointment |
| EA-5 | Tribunal (on constitution) | May confirm, vary or discharge; EA cannot sit on the tribunal without all-party consent | EA powers end on constitution |

Disclosure on every EA order: India seat → enforceable as an order under s.17 (*Amazon v Future Retail* (2022) 1 SCC 209); foreign seat → apply under s.9 in India (LR-ARB-025).

### 7.4 International mediation, AMA Protocol and consent awards

| Step | Actor | Action | SLA / clock | Documents | Decision point |
|---|---|---|---|---|---|
| M-1 | Requesting party | F-INT-10 (or AMA election inside arbitration, App. A B01–B02) | — | clause / invitation | — |
| M-2 | Equator | Invitation journey (§8) | response 30 days (`int.imed.invitation_response_days`) | `TPL-INT-N03` invitation | accept / decline |
| M-3 | Parties / Equator | Joint nomination 10 days → otherwise Appointments Committee appoints (language, expertise, nationality preference); objection → replacement ≤ 5 business days | 10 d + 5 bd | Code acceptance + disclosure | — |
| M-4 | Mediator | Pre-mediation call; mediation agreement e-signed; online consent (LR-MED-008); confidentiality undertakings for non-counsel attendees ≥ 2 business days before session | — | agreement to mediate | — |
| M-5 | Mediator | Joint and caucus sessions (no recording; caucus notes sealed to author — NN-11) | `med_contract_timebox` INT 60 d (+60 by consent) | position papers | — |
| M-6 | Parties | Settlement drafted from agreed heads (P06 builder); signed by parties; mediator authentication signature (LR-MED-004 as policy) | — | iMSA (`TPL-INT-S02`) | conversion choice (§13.3) |
| M-7a | Tribunal (AMA) | Consent award on agreed terms (A&C s.30 for India seat; seat law otherwise) after AML review (LR-INT-013) | ≤ 15 days of settlement | `TPL-INT-S01` | NYC route |
| M-7b | Equator | Singapore Convention attestation certificate (QR + hash) where conversion not chosen | ≤ 5 working days | attestation | Convention route |
| M-7c | Conciliator (India place) | s.73 settlement authenticated → s.74 status (India) | — | settlement | domestic award status |
| M-8 | Equator | Compliance tracking (escrow milestones, NN-13) | per terms | — | default → arbitration rung or enforcement |

AMA inside arbitration: tribunal constituted → stay order → 8-week mediation window (`ama_window`, extendable by consent) with arbitration clocks paused → consent award or resumption (Appendix A §3.10; SIAC–SIMC AMA Protocol benchmark). Different neutral by default; same neutral only via F-INT-27.

AML/TBML red-flag rules for any consent award (enhanced review by `compliance_officer`, `INT_AML_REVIEW_REQUIRED`): settlement within 14 days of filing with no response on record; parties related (F-INT-16 overlap or common UBO); amount disproportionate to stated business turnover (> 3× last-year turnover declared in F-INT-01); payer is a third party with no stated reason; payment to a country on FATF increased-monitoring list or a sanctioned-nexus route; settlement amount equals claim to the cent with no negotiation trail.

### 7.5 L2 overlays (only differences from §7.1/§7.4)

| L2 | Overlay steps |
|---|---|
| `int.sale_of_goods` | Optional quality expert determination before arbitration (App. A §3.11; ToR within 7 days; determination 21 days); Incoterm risk-transfer card for tribunal; CISG Art. 39 notice date shown on chronology |
| `int.services` | Acceptance/SLA chronology auto-built from uploaded tickets; optional technical expert |
| `int.distribution_agency` | Competition-law flag → CCI signpost card; termination-notice calculator (notice period vs actual) displayed as facts |
| `int.jv_shareholder` | Valuation expert determination (completion of ToR with agreed valuation standard); FEMA NDI pricing advisory issued with any share-transfer award/settlement (G4 capital account); oppression reliefs signposted to NCLT |
| `int.technology_licensing` | Confidentiality ring (counsel-only tier) for source code/trade secrets; source-code inspection protocol in PO-1 (JAMS AI-disputes rules as benchmark [K]); validity issues excluded from the award |
| `int.epc_construction` | DAAB status check at filing (NOD served within 28 days of DAAB decision?) — displayed, tribunal decides admissibility; programme/delay expert; site-visit evidence via geotagged uploads; bond-call urgent card |
| `int.shipping_logistics` | Owned clock `int_hv_time_bar`; maritime specialist list; documents-only default for demurrage ≤ USD 250,000; vessel-arrest court card |
| `int.trade_finance` | Bank submission agreement check; autonomy notice (LR-INT-022); documents-only default for discrepancy disputes; optional DOCDEX-style expert opinion on UCP compliance (non-binding expert determination) |
| `int.energy` | Regulator-jurisdiction check (CERC/SERC/PNGRB) before acceptance; price-review clauses → expert determination track |
| `int.investment_private` | Completion-accounts expert determination; W&I insurer joined as observer only with consent; claim-notice deadline (contractual) service clock |

### 7.6 Multi-party, multi-contract and coordination

Consolidation (pre-constitution) decided prima facie by the Institutional Committee within 14 days; post-constitution by the tribunal. Coordinated proceedings (same tribunal, separate awards — SIAC r.17 model) need common questions of law/fact. Joinder of a non-signatory only by reasoned tribunal order on consent evidence (LR-ARB-029). Where parties waive nomination for a consolidated tribunal, Equator appoints all members (HKIAC Art. 29 model). HEAP excludes all of these.

### 7.7 Hearings, time zones and interpretation

- **Scheduler fairness rule** (FR-P08-73, parameters `int.tz.window_start = 08:00`, `int.tz.window_end = 19:00`, bounds 07:00–21:00): find slots inside every participant's local window; if none of the required length exists, choose the slot minimising the maximum per-party out-of-window minutes, then rotate the burden across sessions so cumulative out-of-window minutes per party differ by ≤ 60; record `fairness_score` per session (§12.5).
- **Holiday/weekend calendars** per country from `intl.country_profiles` (e.g., UAE Saturday–Sunday weekend since 1 Jan 2022; Gulf Ramadan reduced hours as an advisory overlay).
- **Seoul Protocol 2020 checklist** in `TPL-INT-P02`: test call T-7 days; witness room 360° camera scan; no unauthorised persons or communication; document camera; contingency (dial-in; adjournment rule after 30 minutes of failure); interpreter booth/channel.
- **Interpretation:** interpreter role (case-scoped, App. S) with separate LiveKit audio track; F-INT-22 declaration; machine translation labelled "Translation — for convenience" (NN-32); certified translation for evidence on request.
- **Recording:** arbitration hearings only with recorded consent of all parties and tribunal; mediation never (NN-11).
- **Information security tier** at the CMC (ICCA–NYC Bar–CPR Protocol): `standard` (MFA, TLS, at-rest encryption), `enhanced` (+ watermarking, download limits, IP allow-list), `high` (+ view-only bundles, hardware key MFA, separate KMS key) — the tribunal may direct measures and act on breaches (SIAC r.61 / HKIAC Art. 45A models).

---

## 8. Pre-litigation journey (INT)

| Stage | What happens | Actor | Clock | Output | Legal character |
|---|---|---|---|---|---|
| 1 Invite | Claimant uses F-INT-15 or F-INT-10 without a clause; Equator sends `TPL-INT-N03` invitation by email + courier/registered post to the address for service (A&C s.3 evidence pattern) in English + respondent's language (labelled translation) | case_manager | response 30 d; reminders at day 7, 14, 25 (business hours of recipient's time zone) | delivery evidence | Not a legal notice of arbitration unless stated |
| 2 Consent | Respondent accepts via F-INT-24; both e-sign the agreement to mediate (and online consent); post-dispute arbitration agreement offered (optional) so a consent award can later be issued | parties | — | agreement to mediate (+ submission agreement) | Contract |
| 3 Gates | G1–G4 run before any fee collection from foreign payers (FX-10) | compliance_officer, dpo | ≤ 5 working days | gate decisions | — |
| 4 Session(s) | Online/hybrid mediation; interpreter channels; no recording | mediator | 60 d (+60) | — | Confidential (A&C s.75 for conciliation; policy mirror of Mediation Act ss.22–23) |
| 5 Settlement | Settlement built from agreed heads; e-signed (eIDAS QES for EU parties on request) | parties, mediator | — | iMSA | Contract (contractual mode) |
| 6a Conversion | Consent award by a tribunal constituted under the submission agreement (AMA route) | tribunal | ≤ 15 d | consent award | Arbitral award (NYC) |
| 6b Attestation | Singapore Convention Art. 4(1)(b) attestation (if conversion not chosen and enforcement state is a Convention party in force) | Registrar | ≤ 5 working days | attestation certificate | iMSA usable in Convention states (subject to reservations) |
| 6c Conciliation | If conducted as Part III conciliation with place in India: s.73 settlement → s.74 status | conciliator | — | s.74 settlement | Award status in India only; cross-border: NYC doubtful and possibly excluded from the Singapore Convention (Art. 1(3)(b)) — use 6a/6b for foreign enforcement **[VERIFY — open (counsel)]** |
| 7 Compliance | Payment via escrow or direct with proof (NN-13); FX snapshot on each instalment; payer pack (Form 145/146 guidance for Indian payers; AD bank documents) | escrow_officer, parties | per terms | compliance ledger | — |
| 8 Default | Auto-escalation to arbitration rung (consent captured at stage 2) or enforcement pack | case_manager | 7 d cure notice | — | — |

No pre-litigation step is represented as satisfying Commercial Courts Act s.12A (LR-MED-014, -020); for an Indian respondent and an Indian court suit, the s.12A PIMS pack is offered separately (M-06).

---

## 9. Document checklists per subtype

Formats per DL-INT-39. Verification codes: **V1** hash + upload only · **V2** registry/API check (GLEIF, foreign registry, MCA) · **V3** apostille/legalisation check (LR-INT-017) · **V4** case-manager review · **V5** compliance-officer review · **V6** certified translation required for use.

| Code | Document | L2 | M/O | Verification |
|---|---|---|---|---|
| DOC-INT-01 | Contract / clause / correspondence evidencing the arbitration or mediation agreement | all | M | V1, V4 |
| DOC-INT-02 | Certificate of incorporation / registry extract (each body corporate) | all | M | V2 or V3 |
| DOC-INT-03 | Board resolution / PoA for signatory (apostilled or legalised if foreign) | all | M | V3, V4 |
| DOC-INT-04 | UBO declaration (F-INT-05) + register of members/shareholders | all | M | V5 |
| DOC-INT-05 | Passport / residence proof (individual parties, UBOs) | all | M (individuals) | V5; masked display |
| DOC-INT-06 | TPF agreement summary (not the agreement itself) | funded | M if funded | V4 |
| DOC-INT-07 | Translations of key documents | non-English | O (M for enforcement) | V6; NN-32 labels |
| DOC-INT-08 | Sales contract / PO / proforma invoice; commercial invoice; packing list; bill of lading/AWB; inspection/quality certificate; certificate of origin; non-conformity notice | sale_of_goods | M (contract, invoice, transport doc) | V1, V4 |
| DOC-INT-09 | MSA/SOW, change requests, acceptance certificates, SLA reports, tickets | services | M (MSA/SOW) | V1 |
| DOC-INT-10 | Distribution/agency/franchise agreement; sales and commission statements; termination notice | distribution_agency | M | V1 |
| DOC-INT-11 | SHA/JVA/SPA, articles, cap table, valuation reports, option exercise notice; FEMA filings (FC-GPR/FC-TRS) where relevant [K] | jv_shareholder, investment_private | M (agreements) | V1, V4 |
| DOC-INT-12 | Licence agreement; IP registration certificates; royalty reports; audit notice | technology_licensing | M | V2 (IP registries where available), V1 |
| DOC-INT-13 | Contract (conditions + particular conditions), DAAB decision and NOD, notices of claim, programme, variation orders, payment certificates, bonds | epc_construction | M (contract, notices) | V1, V4 |
| DOC-INT-14 | Bill of lading / charterparty / booking note; survey report; delivery receipt; laytime statement; carrier time-extension letters | shipping_logistics | M | V1; time-bar clock reads delivery date |
| DOC-INT-15 | LC/guarantee text (MT700/MT760 copy), presentation documents, refusal notice (MT734), bank correspondence | trade_finance | M | V1, V4 |
| DOC-INT-16 | PPA/GSA/LNG SPA/EPC; regulator orders; price-review notices | energy | M | V1, V4 |
| DOC-INT-17 | Award (signed), arbitration agreement, Registrar certificate, translations, apostille/legalisation — enforcement pack (§13) | all (post-award) | M | V3, V6 |

---

## 10. Practical difficulties and product solutions

| # | Difficulty | Product solution | Module |
|---|---|---|---|
| PD-01 | Foreign respondent ignores emails; service disputed later under NYC Art. V(1)(b) | Multi-channel service with delivery evidence (email read receipts, courier tracking, registered post), deemed-receipt computation under A&C s.3, procedural-fairness log export (LR-INT-008) | notices |
| PD-02 | Parties in three time zones; one side always disadvantaged | Fairness scheduler with rotation and published score (§7.7, §12.5) | hearings |
| PD-03 | Award unenforceable where assets are (e.g., UAE seat for an Indian enforcement) | Seat facts table with India-notified badge and acknowledgement; enforcement-target facts at intake (never advice) | intake |
| PD-04 | Mediated settlement not enforceable cross-border (India not a Singapore Convention party) | Conversion choice screen with the Art. 1(3) trade-off; post-dispute submission agreement captured at consent stage | outcomes |
| PD-05 | Fees blocked by correspondent banks (sanctions nexus) | G1 before any collection; rail selection rules (FX-10); compliance-approved alternative currency only where lawful | payments |
| PD-06 | Foreign counsel acting beyond BCI limits | F-INT-19 attestation; Indian-counsel requirement for Indian-law issues; 60-day fly-in counter | identity |
| PD-07 | Translations of uncertain quality | NN-32 labels; certified-translation workflow with roster per country; glossary per case | documents |
| PD-08 | Neutral conflicts through group companies and funders | F-INT-16 relevant-persons list + F-INT-06 funder identity; automatic re-run on any change | neutrals |
| PD-09 | Delay in award (*Lancor* risk) | Draft-award clock, scrutiny SLA, fee-reduction ladder for late drafts (Appendix N; counsel question Q-5) | outcomes |
| PD-10 | Tax withholding confusion for foreign neutrals and payers | Payout engine: TRC, Form 41, no-PE declaration, DTAA article; Forms 145/146; gross-up clause in INT terms | billing |
| PD-11 | Data protection objections from EU parties | Region election, SCCs/IDTA basis, Art. 27 representative check, AI clerical-only mode | privacy |
| PD-12 | Sham/collusive consent awards used to move money | TBML red-flag rules and enhanced review before any consent award (§7.4) | outcomes |
| PD-13 | Cargo claims lost to the one-year bar | Owned time-bar clock with T-30/T-7/T-1 alerts and "commence now" guidance (NN-04) | clocks |
| PD-14 | Bank parties refuse platform arbitration | Documents-only expert opinion option; bank submission agreement template; signpost to court for encashment injunctions | intake |
| PD-15 | Different signature standards abroad | Signing options: DSC (India), eIDAS QES (EU), wet-ink counterparts + courier; PAdES-LTV + verification URL | esign |

---

## 11. Integrations and APIs

| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| `SANCTIONS_PORT` — commercial list provider (ComplyAdvantage-class via Surepass) | G1 screening and annual/party-change rescreening | names, DOB, nationality, entity identifiers | DPDP s.7 legal obligation where applicable / s.17(1)(a); GDPR Art. 6(1)(c)/(f) | API | Manual list upload (UN, MHA, OFAC SDN, EU, UK) + fuzzy match; gate stays `pending` — never auto-clear |
| GLEIF LEI API | Verify LEI, legal name, jurisdiction, parent relationships (feeds F-INT-16) | LEI records (public) | public data | API | Manual registry extract |
| Foreign company registries (e.g., Companies House UK, ACRA Singapore [K]) | Incorporation and officers | registry data | public data / provider terms | API where offered | Apostilled extract upload (V3) |
| `KYC_PORT` (Surepass) | Indian parties: MCA, GSTIN, PAN | KYB data | consent / s.7 | API | Upload + manual check |
| `FX_PORT` — FBIL reference (USD, EUR, GBP, JPY at 13:00 IST) + configured cross-rate (AED peg 3.6725) / provider mid / AD-bank TT for SGD | Snapshots for fees, claims, instalments | rates | — | API/file | Registrar manual rate with source (Appendix B FX-3) |
| `PAYMENTS_PORT` — Razorpay International; PayPal/Stripe where available; bank wire with virtual-account reference | Foreign-currency fee collection | payment metadata (no card data, NN-31) | contract | hosted checkout | Wire + FIRC/e-BRC upload |
| `ESCROW_PORT` — RazorpayX Escrow+ / Castler / bank | Deposits per currency, settlement sums (NN-13) | amounts, parties | contract; RBI PA Directions (15 Sep 2025) | API | Direct payment with proof |
| `ESIGN_PORT` — Leegality/Digio (India); eIDAS QTSP adapter (EU) | Agreements, awards, consents | signer identity | IT Act s.3A/5; eIDAS Art. 25(2) | API | Wet-ink counterparts + courier |
| `TRANSLATION_PORT` — Sarvam/Bhashini (Indian languages), general MT for UN languages; certified-translator roster | Convenience translation; certified jobs | documents (minimised) | contract; DPDP transfer basis for foreign translators | API / manual | Human translator only |
| `VIDEO_PORT` — LiveKit (India region) | Hearings with interpretation tracks, caucus rooms | A/V streams (not recorded by default) | consent | API | Self-hosted LiveKit |
| Calendar (ICS feeds; Outlook/Google import) | Case calendars per user | hearing times | contract | ICS | Email invites |
| IANA tz database + holiday calendars (`intl.country_profiles`) | Scheduler | reference | — | bundled + quarterly update | Manual override |
| UNCITRAL / HCCH status pages; Gazette (s.44(b) S.O.s) | `intl.country_profiles` reference data (NYC, Singapore Convention, Apostille) | public | — | **manual curation**, legal_reviewer approval, quarterly re-verify | — |
| MEA e-Sanad / apostille centres | Apostille of Indian documents | document refs | party instruction | manual (checklist + booking link) | Consular legalisation route |
| Courier / `POSTAL_PORT` (international registered post / courier API) | Service of Request and wet-ink award counterparts | addresses | A&C s.3 | API where available | Manual tracking number entry |
| Finbyx / LawDocs | Clause generator embedding in cross-border contracts | clause metadata | contract | API (P09) | Copy clause text |

API endpoints (in addition to P08 §7.3): `POST /v1/intl/explorer/evaluate` (deterministic outcome) · `POST /v1/cases/{caseId}/intl/relevant-persons` · `POST /v1/cases/{caseId}/intl/tpf-disclosures` · `POST /v1/cases/{caseId}/intl/tier-elections` · `POST /v1/cases/{caseId}/intl/consolidation-applications` · `POST /v1/cases/{caseId}/intl/early-determinations` · `POST /v1/cases/{caseId}/intl/security-applications` · `POST /v1/cases/{caseId}/intl/role-switch-consents` · `GET /v1/cases/{caseId}/intl/schedule/proposals?duration=PT3H` · `GET /v1/intl/country-profiles/{iso2}` · `POST /v1/intl/calculators/{name}/runs` · `GET /v1/cases/{caseId}/intl/fairness-log/export` (s.48/Art. V evidence). All POSTs take `Idempotency-Key`; RBAC per §16.

---

## 12. Calculators (indicative only; never advice — NN-01, FR-P08-08)

All outputs carry `indicative: true`, `disclaimer_key = calc.int.indicative`, `computation_trace[]`. Money in minor units; rounding half-up only at presentation.

### 12.1 `int.interest_fx@2` — interest and currency conversion
Inputs: principal + currency; rate (entered — never proposed); simple/compound with period (annual/quarterly/monthly); day count (ACT/365, ACT/360, 30/360); start/end; FX snapshot id. Formulas: simple `I = P × r × d / basis`; compound `A = P × (1 + r/m)^(m × t)`. India-seat post-award option per s.31(7)(b) (current rate + 2%, parameter `LR-ARB-015.post_award_margin`).

| Vector | Inputs | Output |
|---|---|---|
| GV-INT-01 | USD 1,000,000; 6% simple; ACT/365; 1 Jan 2025 → 1 Jan 2026 (365 d); FX 88.00 | interest USD 60,000.00; total USD 1,060,000 → ₹9,32,80,000 (illustrative rate) |
| GV-INT-02 | USD 250,000; 5% simple; ACT/360; 1 Mar 2026 → 30 Jun 2026 (121 d) | interest USD 4,201.39 |
| GV-INT-03 | USD 500,000; 8% compounded quarterly; 1 year | amount USD 541,216.08; interest USD 41,216.08 |
| GV-INT-04 | USD 2,000 at USD/INR 88.2500, EUR/INR 102.4000 | EUR 1,723.63 (Appendix B WE-10) |

### 12.2 `int.cost_estimate@2` — Card INT-USD / INT-MED estimator
Reads the pinned Appendix B schedule; linear interpolation inside a band from the previous band ceiling (USD 250,000 / 1,000,000 / 5,000,000 / 25,000,000) to the band ceiling; three-member = 2.5 × sole; expedited/HEAP −20% on tribunal fees; item rounding to USD 1.00 half-up.

| Vector | Inputs | Output |
|---|---|---|
| GV-INT-05 | USD 2,000,000; sole; Standard | registration 2,000; admin 12,500; sole max 46,250; total USD 60,750; three-member tribunal 115,625 (P08/App. B vector) |
| GV-INT-06 | USD 600,000; sole; Expedited | fraction (600,000 − 250,000)/750,000 = 0.46667; registration 1,500; admin 7,867; sole max 24,333.33 × 0.8 = 19,467; total USD 28,834 |
| GV-INT-07 | EA requested | admin 3,000 + EA fee 12,500 = USD 15,500 |
| GV-INT-08 | Consent-award conversion | USD 1,500 + 2,500 = USD 4,000 |
| GV-INT-09 | Mediation, USD 3,000,000, 2 session-days, online-only | filing 500; admin 3,000 × 0.75 = 2,250; mediator 4,000 × 2 = 8,000; total USD 10,750; equal split USD 5,375 each |

### 12.3 `int.deposit_split@1`
Equal split with substitute payment: if one party fails to pay within 15 days of the call, the other may pay; the paying party's excess is recorded for a separate costs award (LR-ARB-022 procedure applies before termination). GV-INT-10: total deposit USD 60,750 → USD 30,375 each; respondent defaults; claimant pays USD 60,750; `substitute_payment_minor = 3,037,500` flagged for the award on costs.

### 12.4 `int.limitation_indicative@1`
India-law categories per DL-INT-31 (3 years from the event; General Clauses Act 1897 s.9 first-day exclusion convention) and the Hague-Visby one-year bar. Output: indicative last date + "the tribunal decides limitation; confirm with counsel". GV-INT-11: delivery 15 Mar 2026 → Hague-Visby indicative last day 15 Mar 2027 (Art. III para 6(c) 'within one year after delivery'; GCA s.9 exclusion), Equator safe-date 14 Mar 2027 **[VERIFY — open (counsel): computation convention under the 2025 Schedule and foreign fora]**. GV-INT-12: goods delivered 10 Apr 2024, no credit period, India law → Art. 14 indicative last date 10 Apr 2027. GV-INT-13: FIDIC notice: awareness 10 Jan 2026 + 28 days → 7 Feb 2026 (contractual service clock).

### 12.5 `int.tz_fairness@1`
Per participant: `out_of_window_min` = minutes of the slot outside 08:00–19:00 local. Score = max over participants; tie-break by sum. GV-INT-14: 10 Nov 2026, participants Delhi (UTC+05:30), London (UTC+00:00), New York (UTC−05:00); shared window 13:00–13:30 UTC only (30 minutes); proposed 3-hour slot 12:00–15:00 UTC → Delhi 17:30–20:30 (90 min out), London 0, New York 07:00–10:00 (60 min out); score 90, sum 150; next session rotation must reduce Delhi's burden (e.g., 10:00–13:00 UTC: Delhi 15:30–18:30 = 0; London 0; New York 05:00–08:00 = 180 → rejected as > bound 07:00; scheduler proposes split sessions instead).

---

## 13. Outputs, templates, enforcement and registration route

### 13.1 Templates (extends FR-P08-79)
`TPL-INT-N01` Notice/Request service cover · `N02` foreign-seat warning · `N03` mediation/negotiation invitation · `N04` sanctions-hold neutral notice ("under compliance review") · `P01` PO-1 international · `P02` virtual-hearing protocol (Seoul Protocol) · `P03` information-security directions · `P04` EA order shell · `P05` stay order for AMA · `S01` consent award · `S02` iMSA with Singapore Convention attestation block · `S03` final award shell (severable heads, computation annex, interest clause, currency and conversion date, costs s.31A for India seat, AI non-delegation attestation) · `C01` model clauses (AMA; arbitration-only; mediation-only; UNCITRAL-administered; IFSC seat variant) · `R01` enforcement pack cover + Registrar certificate · `R02` WTO/ISDS signposting letter · `R03` payer pack (FEMA/Form 145/146 guidance) · `R04` Singapore Convention attestation certificate. Lint (FR-P08-09) applies; target-language versions need certified translation + legal review (NN-23).

### 13.2 Enforcement routes

| Output | India seat | Foreign seat | Enforcement in India | Enforcement abroad |
|---|---|---|---|---|
| Final award | Part I award; e-stamped at execution state; s.34 challenge (no s.34(2A) for ICA) | Seat law | India seat: s.36 as decree (Commercial Division of High Court for ICA [K]); foreign seat: ss.47–49 in High Court if seat notified; else suit | NYC Art. IV pack: authenticated award, certified agreement, certified translation; apostille/legalisation per target |
| Consent award (AMA) | As above | As above | As above | As above — **outside Singapore Convention** (Art. 1(3)) [K] |
| iMSA (unconverted) | Contract (contractual mode); s.27 only when statutory mode ON and notified | Venue law | Suit on contract | Singapore Convention in Convention states in force (Art. 4 attestation; reservations) |
| s.74 settlement (Part III, place India) | Award status (s.74) | — | s.36 route | Uncertain — NYC covers arbitral awards; Singapore Convention excludes settlements enforceable as an arbitral award (Art. 1(3)(b)); use a consent award abroad **[VERIFY — open (counsel): foreign recognition]** |
| EA order | s.17(2) enforceable | Seat law | Foreign-seat order → s.9 application | Local law |

Registration: none for awards unless the award creates/declares rights in Indian immovable property (Registration Act s.17(1)(b); NN-08 physical route) — rare in INT.

### 13.3 Conversion trade-off shown to parties (facts only)
"Option A — consent award: enforced under the New York Convention (about 170 countries [K]); in India under Part I (Indian seat) or Part II (notified foreign seat). Option B — settlement agreement with Equator attestation: may be relied on in Singapore Convention states where it is in force, subject to their reservations; it cannot be both a consent award and a Convention settlement for the same terms. India has not ratified the Singapore Convention." Parties choose; the choice and timestamp are recorded.

### 13.4 Enforcement pack contents (`GET /v1/cases/{id}/intl/enforcement-pack`)
Award (signed per option), certified true copy by Registrar (QES + verification URL), arbitration agreement certified copy, evidence of foreign-award status (seat certificate), translations (certified per DL-INT-32), apostille/legalisation checklist per target (`intl.country_profiles.apostille_member`; UAE, Qatar, Kuwait: consular legalisation; China from 7 Nov 2023 and Saudi Arabia from 7 Dec 2022: apostille), procedural-fairness log extract, BSA s.63(4) certificate (India use, NN-10), costs statement, payer pack. Status never shows "enforced" before the court order (LR-INT-009).

### 13.5 Publication
Opt-in only (F-INT-23; NN-26; Appendix R §3): all parties and the tribunal consent, the parties' consent being given **after** the outcome (a filing-stage preference is not consent); modes `none` (default) · `statistics` · `digest` · `redacted_award` (24-month embargo default) · `full_award` (COM/INT B2B only, all-party express consent). India-seated matters observe s.42A and India-seated arbitral publication stays behind `publication.arbitral.enabled` (OFF) until counsel rules (X-35; Q-1; Appendix R Q-R1); mediation/conciliation digests behind `publication.consensual.enabled` (OFF). Tribunal-composition register and challenge-decision publication behind flags `intl.publish_composition_register` and `publication.challenge_decisions.enabled` (which supersedes `intl.publish_challenge_decisions`, Appendix R §6.5) (both OFF).

---

## 14. Dashboards, KPIs and enterprise hooks

KPIs (extends FR-P08-81; SQL views in `intl`; n < 10 cells suppressed per Appendix R statistics rule):

| KPI | Definition | Target (default) |
|---|---|---|
| INT-K01 Gate clearance time | median working days filing → all gates cleared | ≤ 5 |
| INT-K02 Acknowledgement SLA | % filings acknowledged ≤ 1 business day | ≥ 98% |
| INT-K03 Time to constitution | median days Answer due → tribunal constituted | ≤ 30 |
| INT-K04 EA appointment time | median business days application → EA appointed | ≤ 1 |
| INT-K05 Award within target | % awards ≤ 3 months after final hearing / tier limit | ≥ 90% |
| INT-K06 Scrutiny time | median working days draft → form approved | ≤ 10 |
| INT-K07 iMSA conversion | % iMSAs converted to consent awards vs attested | report only |
| INT-K08 Fairness score | distribution of per-session max out-of-window minutes | p90 ≤ 60 |
| INT-K09 Sanctions holds | count, outcomes, median review time | report only |
| INT-K10 Neutral diversity | % women, % first-time Equator appointees, nationality mix of sole/presiding | report only (HKIAC Art. 9A-style diversity duty in allocation, App. N) |
| INT-K11 Foreign-currency invoices | count by currency; % with LUT treatment correct | 100% correct |
| INT-K12 Trade-measure clusters | cases by DL-INT-27 type | report only |

Never shown: win rates, outcomes by neutral, party-side tags (NN-16, NN-28). Widgets: gate board, enforcement-target map, multi-currency deposits ledger, time-zone heatmap. Enterprise hooks: `equator.intl.case.registered.v1`, `equator.intl.award.enforcement_pack_issued.v1`, `equator.intl.clause.generated.v1` for chambers of commerce, law firms and export councils (P09/P10); partner priority affects administrative speed only (NN-16).

---

## 15. Competitor notes and Equator differentiation

| Institution | What they do well (benchmark) | Gap Equator fills |
|---|---|---|
| SIAC (Rules 2025; Gateway with Opus 2) | Streamlined (≤ SGD 1m, 3 months) and Expedited (≤ SGD 10m) tiers; pre-NoA EA; TPF disclosure r.38; award scrutiny r.53; consent-only publication r.60; India is its 3rd-largest foreign user (178 cases in 2025) | INR/USD pricing below SIAC for sub-USD-5m; India-seat expertise; Indian-language interpretation; India-specific gates (FEMA, s.44(b), stamp) |
| ICC (Rules 2026; Case Connect with Opus 2, Apr 2025) | EPP USD 4m; Highly Expedited 3-month lane; Art. 12(5) relevant-persons list; award scrutiny; composition transparency | Lower cost; virtual-first; integrated hearings (Case Connect has no integrated video) |
| LCIA (Rules 2020) | Time-based fees; challenge decision database (84 decisions); published turnaround times (2025) | Ad valorem certainty; INR/USD; mediation and AMA built-in |
| HKIAC (Rules 2024 + 2026; Case Connect on HighQ) | Dual fee method; diversity duty Art. 9A; first-time appointee metric; ICS calendars | India corridor; Indian-language support |
| AAA-ICDR (Rules 2021; AI Arbitrator since Nov 2025 for documents-only construction cases) | AI-assisted documents-only lane with party validation and human-signed award | Equator keeps AI assistive (NN-01); AI-lane pilot flag `intl.ai_docs_only_lane` OFF pending counsel (Q-9) |
| IIAC (Regs 2023) | Statutory standing; USD schedule (admin cap USD 15,000; arbitrator cap USD 200,000); EA 15 days; fast track 6 months | Digital-first platform, multi-currency invoicing, AMA, published SLAs; note Equator admin cap (USD 50,000) sits above IIAC — Board re-benchmark item |
| MCIA (Rules 2025 published; INR fee schedule only) | Mumbai base; EA fee rules | USD schedule and FX invoicing |
| DIAC (Decree 34 of 2021; Rules 2022) | UAE corridor | Clear disclosure that UAE-seated awards are not India-notified; DIFC/ADGM seat facts |

Differentiators to ship: (1) enforcement-ready pack with country facts; (2) time-zone fairness scheduler; (3) compliance gates integrated with payments; (4) transparent USD calculator; (5) AMA with conversion trade-off explained; (6) published Service Charter metrics.

---

## 16. Data-model extensions (`intl` schema; RLS identical to core, FR-P08-12)

### 16.1 Tables (adds to P08 §7.2 and Appendix F `intl.case_international`)

| Table | Key columns | Notes |
|---|---|---|
| `intl.case_international` (alter) | + `l1_code text NOT NULL CHECK (l1_code IN ('int.ica','int.imed'))`, `foreign_seat_indian_parties boolean NOT NULL DEFAULT false`, `procedure_tier text CHECK (procedure_tier IN ('streamlined_documents_only','highly_expedited','expedited','standard'))`, `rules_code text`, `equal_footing boolean NOT NULL DEFAULT false`, `agreement_date date`, `rules_of_law text`, `ex_aequo_authorised boolean NOT NULL DEFAULT false`, `exclude_s9_s27 boolean NOT NULL DEFAULT false`, `eu_party boolean NOT NULL DEFAULT false`, `security_tier text CHECK (security_tier IN ('standard','enhanced','high'))` | P08/F columns retained |
| `intl.country_profiles` | `iso2 PK`, `nyc_party bool`, `india_s44b_notified bool`, `s44b_so_ref text`, `sgconv_status text CHECK IN ('none','signatory','party_not_in_force','party_in_force')`, `sgconv_eif date`, `sgconv_reservations text`, `apostille_member bool`, `apostille_eif date`, `weekend_days int[]`, `holiday_calendar_ref`, `translation_lang text[]`, `verified_on date`, `verified_by uuid`, `next_reverify_due date` | Reference data; legal_reviewer maker–checker; quarterly re-verify |
| `intl.gates` | P08 definition + `conditions jsonb`, `rule_ids text[]` | — |
| `intl.sanctions_screens` | P08 + `subject_kind text CHECK IN ('party','ubo','director','counsel','funder','neutral','interpreter')`, `match_score numeric(5,2)`, `decision text CHECK IN ('no_match','false_positive','confirmed_hit')` | Confirmed hit → HX-INT-05 |
| `intl.ubo_declarations` | `id`, `case_id`, `case_party_id`, `rows jsonb`, `pep bool`, `sanctioned_nexus bool`, `source_of_funds text`, `signed_esign_id`, `version int` | Field-level encryption (Tier-High) |
| `intl.relevant_persons` | `id`, `case_id`, `case_party_id`, `name`, `relationship text`, `country char(2)`, `identifier`, `added_at` | Conflict engine input |
| `intl.tpf_disclosures` | `id`, `case_id`, `case_party_id`, `kind text`, `funder_name`, `funder_country`, `control_rights text`, `adverse_costs_cover text`, `undertaking_esign_id`, `version int`, `disclosed_at` | Change → conflict re-run |
| `intl.tier_elections` | `id`, `case_id`, `tier`, `basis`, `heap_waivers jsonb`, `unreasoned_award bool`, `decided_by`, `reasons` | — |
| `intl.ea_applications` | `id`, `case_id`, `filed_before_rfa bool`, `rfa_due_at timestamptz`, `relief jsonb`, `ppo_requested bool`, `ea_neutral_id`, `appointed_at`, `order_due_at`, `status text CHECK IN ('filed','lapsed','appointed','order_issued','superseded')` | Clock `int_ea_order` 14 d |
| `intl.procedural_applications` | `id`, `case_id`, `kind text CHECK IN ('consolidation','joinder','coordinated','multi_contract','early_determination','preliminary_issue','security_costs','security_claim')`, `payload jsonb`, `decided_by_body text CHECK IN ('tribunal','institutional_committee','registrar')`, `decision`, `reasons`, `decided_at` | — |
| `intl.interpretation_requests` / `intl.translation_jobs` | `languages jsonb`, `mode`, `certification_standard`, `translator_id`, `derived_document_id` (NN-32 link) | — |
| `intl.hearing_fairness` | `session_id`, `participant_id`, `tz text`, `out_of_window_min int`, `score int`, `rotation_index int` | Export for Art. V evidence |
| `intl.trade_particulars` | `case_id PK`, `l2_code`, `block jsonb` (schema-validated per L2), `trade_measure_impact jsonb`, `fta_relevance jsonb` | — |
| `intl.conversions` | `id`, `case_id`, `settlement_id`, `route`, `aml_review text`, `sgconv_tradeoff_ack_at`, `award_id` | Unique per settlement: either `award_id` or attestation |
| `intl.sgconv_attestations` | `id`, `settlement_id`, `issued_at`, `hash`, `qr_url`, `registrar_id` | Mutually exclusive with `intl.conversions.award_id` (trigger) |
| `intl.foreign_counsel_registrations` | `id`, `person_id`, `bci_registration_no`, `fly_in_days_used_12m int`, `form_c_ref`, `issue_of_law_attestation jsonb`, `client_principal_office_country` | CHECK fly-in ≤ 60 |
| `intl.calc_runs` | per FR-P08-08 | — |

### 16.2 Enums (Postgres `CREATE TYPE` in `intl`)
`intl.l1_code`, `intl.procedure_tier`, `intl.gate_code ('G0'..'G6')`, `intl.gate_status ('pending','cleared','cleared_with_conditions','held','failed')`, `intl.sgconv_status`, `intl.security_tier`, `intl.conversion_route ('ama_existing_tribunal','tribunal_constituted_for_purpose','s74_conciliation_india')`.

### 16.3 Guards (DB triggers + service checks)
- `intl.guard_registration` (P08): all gates ∈ (`cleared`,`cleared_with_conditions`) before `accepted`.
- `intl.guard_heap_joinder`: insert into `intl.procedural_applications` with kind ∈ (consolidation, joinder, coordinated, multi_contract) when tier = `highly_expedited` → `INT_HEAP_JOINDER_BLOCKED`.
- `intl.guard_presiding_nationality`: appointment of sole/presiding whose nationality ∈ party nationalities without all-party written waiver → `INT_NATIONALITY_CONFLICT`.
- `intl.guard_conversion_exclusive`: settlement cannot have both a consent award and an SG Convention attestation → `INT_SGCONV_CONVERSION_CONFLICT`.
- `intl.guard_role_switch`: same neutral med→arb requires F-INT-27 consents dated after mediation end and statutory_mode = false.

### 16.4 Clocks (add to Appendix A §6 catalogue)
`int_ea_rfa_due` (7 d), `int_ea_order` (14 d), `int_answer_due` (30/21 d), `int_cmc_due` (21/10/7/14 d), `int_heap_award` (3 months from CMC), `int_streamlined_award` (90 d from constitution), `int_expedited_award` (6 months, +3), `int_draft_award` (60 d after closure), `int_scrutiny` (10/5 working days), `int_hv_time_bar` (1 year; owned, NN-04), `int_invitation_response` (30 d), `int_sanctions_rescreen` (12 months). AMA uses the existing Appendix A clock `ama_window` (8 weeks; §7.4) — no INT duplicate.

### 16.5 Feature flags and config keys
Flags: `intl_ifsc_schedule` OFF · `intl_eu_qes_signing` ON-for-EU · `intl_sgconv_attestation` ON · `intl.heap_lane` ON · `intl.ai_docs_only_lane` OFF · `intl.publish_composition_register` OFF · `intl.publish_challenge_decisions` OFF (superseded by `publication.challenge_decisions.enabled`, Appendix R) · `intl.foreign_region_storage` OFF · `intl.ea_ppo_india_seat` OFF. Config: `int.tier.streamlined_max_usd` 250000 · `int.tier.expedited_max_usd` 4000000 · `int.tier.heap_max_usd` 4000000 · `int.tz.window_start` 08:00 · `int.tz.window_end` 19:00 · `int.imed.invitation_response_days` 30 · `int.ubo_threshold_pct` 10 · `int.aml.turnover_multiple` 3.

### 16.6 Events (CloudEvents; add to Appendix F §F.9)
`equator.intl.explorer.evaluated.v1` · `equator.intl.gate.cleared.v1` · `equator.intl.gate.held.v1` · `equator.intl.sanctions.rescreen_due.v1` · `equator.intl.sanctions.hit_confirmed.v1` · `equator.intl.tier.decided.v1` · `equator.intl.ea.applied.v1` · `equator.intl.ea.lapsed.v1` · `equator.intl.ea.order_issued.v1` · `equator.intl.tpf.disclosed.v1` · `equator.intl.relevant_persons.updated.v1` · `equator.intl.conversion.requested.v1` · `equator.intl.conversion.aml_review_required.v1` · `equator.intl.sgconv.attestation_issued.v1` · `equator.intl.case.registered.v1` · `equator.intl.award.enforcement_pack_issued.v1` · `equator.intl.clause.generated.v1` · `equator.intl.hearing.fairness_recorded.v1`. Payloads carry IDs only — no names or amounts (NN-16, NN-30).

### 16.7 Error codes (add to Appendix F; RFC 9457)
Per master X-20, each INT code travels as a sub-code in `rule` under the canonical Appendix F `code` shown; "new" means the code itself is registered in §F.10.1 by the P08f migration.

| Code (sub-code) | Canonical `code` (App. F §F.10) | HTTP | Message |
|---|---|---|---|
| `INT_GATE_PENDING` | new (P08 FR-P08-83) | 409 | Registration is waiting for compliance checks. |
| `INT_OUT_OF_SCOPE_STATE` | `INT_TEST_NOT_MET` (§F.10.2) | 422 | Equator does not administer treaty or WTO disputes; see the suggested forum. |
| `INT_SEAT_NOT_NOTIFIED` | `INT_TEST_NOT_MET` (§F.10.2) | 422 | Please acknowledge the enforcement notice for this seat. |
| `INT_NATIONALITY_CONFLICT` | `CONFLICT_DETECTED` | 409 | The sole or presiding arbitrator must be of a different nationality unless all parties agree in writing. |
| `INT_FOREIGN_COUNSEL_NOT_PERMITTED` | `FORBIDDEN` | 403 | Foreign counsel cannot act on this matter or issue. |
| `INT_AML_REVIEW_REQUIRED` | new | 409 | This settlement needs a compliance review before a consent award. |
| `INT_TIER_NOT_ELIGIBLE` | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` | 422 | This procedure is not available for this case. |
| `INT_HEAP_JOINDER_BLOCKED` | `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` | 422 | Joinder and consolidation are not available in the Highly Expedited procedure. |
| `INT_EA_NOA_OVERDUE` | new | 409 | The Request for Arbitration was not filed within 7 days; the emergency application has lapsed. |
| `INT_TPF_UNDISCLOSED` | new | 409 | Funding disclosure is required before this step. |
| `INT_RELEVANT_PERSONS_MISSING` | new | 409 | Please complete the relevant persons list. |
| `INT_SGCONV_CONVERSION_CONFLICT` | new | 409 | A settlement cannot be both a consent award and a Convention settlement. |
| `INT_ROLE_SWITCH_CONSENT_MISSING` | `SAME_NEUTRAL_CONSENT_MISSING` | 409 | All parties must consent after mediation ends before the mediator can act as arbitrator. |
Aliases: `INT_SANCTIONS_HOLD` → `SANCTIONS_HIT_REVIEW`; `INT_TRANSFER_BASIS_MISSING` → `DPDP_TRANSFER_BASIS_MISSING` (R-V6-03).

### 16.8 RBAC highlights
`compliance_officer`: G1/G2 decisions, sanctions detail (others see status only); `dpo`: G3; `registrar`: G4–G6, tier, equal_footing; `committee_member` (Appointments): constitution, consolidation (pre-constitution); `interpreter`: session audio + assigned documents only; funders: no platform access; foreign counsel: case-scoped and issue-limited flag shown to tribunal.

---

## 17. Acceptance tests (Gherkin; `tests/acceptance/int/`)

```gherkin
Feature: INT vertical (V6)

  Scenario: NN-19_int_gate_blocks_acceptance
    Given an INT case with gates G1-G5 cleared and G6 pending
    When the case manager attempts transition "accept"
    Then the API returns 409 "INT_GATE_PENDING"
    And the case remains "under_scrutiny"

  Scenario: NN-19_int_sanctions_hold_hides_details
    Given the sanctions provider returns a potential match for the respondent's UBO
    When the respondent views the case status
    Then the status reads "under compliance review"
    And no list name, match score or UBO name is shown
    And fee collection in USD is disabled for the case

  Scenario: NN-19_int_designation_mid_case_holds_award
    Given an award is form-approved
    And the annual rescreen confirms a hit on a party
    When the registrar attempts to release the award
    Then the API returns 409 "SANCTIONS_HIT_REVIEW"
    And payouts to neutrals for the case are frozen

  Scenario: LR-INT-016_wto_declined_signposted
    Given a user answers INT-Q01a with "WTO / trade rule"
    When the Dispute Explorer evaluates
    Then the outcome is "OUT-INT-SIGNPOST-WTO"
    And a signposting event naming the Department of Commerce and DGTR is recorded
    And no case number is created

  Scenario: LR-INT-016_treaty_claim_declined
    Given the respondent is a Government and the claim basis is a bilateral investment treaty
    Then the outcome is "OUT-INT-SIGNPOST-ISDS"

  Scenario: NN-24_int_criminal_relief_rejected
    Given the claimant asks Equator to punish the respondent for cheating
    When the Dispute Explorer evaluates INT-Q02 = "Yes"
    Then the outcome is "OUT-INT-REJECT-CRIMINAL" with police and Magistrate signposts

  Scenario: LR-MED-016_international_mediation_test_uses_place_of_business
    Given an Indian-incorporated company whose only place of business is in Dubai and an Indian company
    When G5 computes flags
    Then intl_mediation_flag is true
    And ica_flag is false

  Scenario: LR-INT-001_india_company_controlled_abroad_is_not_foreign
    Given two companies incorporated in India, one wholly owned by a US parent, seat New Delhi
    When G5 computes flags
    Then the case is rerouted to COM with "INT_TEST_NOT_MET"

  Scenario: LR-INT-003_indian_parties_foreign_seat_stay_in_int
    Given two Indian-incorporated companies choose Singapore as seat
    Then the case stays in INT with foreign_seat_indian_parties = true
    And the foreign-seat warning must be acknowledged

  Scenario: LR-INT-025_uae_seat_requires_acknowledgement
    Given the seat selected is "AE-DIFC"
    When the claimant submits F-INT-04 without sl_ack_non_notified_seat
    Then the API returns 422 "INT_TEST_NOT_MET" with rule "INT_SEAT_NOT_NOTIFIED"
    And the seat card shows "Not notified under A&C s.44(b)"

  Scenario: LR-INT-005_presiding_same_nationality_blocked
    Given parties of Indian and German nationality
    When the allocation engine proposes a German presiding arbitrator without an all-party waiver
    Then the appointment is rejected with 409 "CONFLICT_DETECTED" and rule "INT_NATIONALITY_CONFLICT"

  Scenario: NN-03_int_unilateral_presiding_blocked
    Given equal_footing = true in a three-member tribunal
    When the claimant nominates the presiding arbitrator
    Then the API returns 403 "NEUTRAL_SELECTION_FORBIDDEN"

  Scenario: INT_HEAP_joinder_blocked
    Given a case in the Highly Expedited tier
    When a party files F-INT-17 for joinder
    Then the API returns 422 "MECHANISM_NOT_PERMITTED_FOR_VERTICAL" with rule "INT_HEAP_JOINDER_BLOCKED"

  Scenario: INT_expedited_threshold_and_opt_out
    Given a claim of USD 3,500,000 under Equator Rules and no opt-out
    Then the tier defaults to "expedited"
    When all parties e-sign tier_opt_out_expedited
    Then the tier becomes "standard"

  Scenario: INT_EA_lapses_without_request
    Given an EA application filed before the Request for Arbitration on 1 Nov 2026
    When no Request is filed by 8 Nov 2026 23:59 in the applicant's time zone
    Then the EA application status is "lapsed" and event equator.intl.ea.lapsed.v1 is emitted

  Scenario: LR-ARB-025_foreign_seat_ea_disclosure
    Given an EA order is issued in a Singapore-seated case
    Then the order cover states that enforcement in India requires an application under A&C s.9

  Scenario: LR-INT-010_no_sgconv_india_claim
    Given a CMS editor writes "enforceable in India under the Singapore Convention"
    When the content is submitted for publication
    Then lint rejects it with "COPY_PROHIBITED_CLAIM"

  Scenario: INT_conversion_exclusive
    Given a settlement already has an Equator Singapore Convention attestation
    When a party requests consent-award conversion for the same settlement
    Then the API returns 409 "INT_SGCONV_CONVERSION_CONFLICT" unless the attestation is first withdrawn by all parties

  Scenario: LR-INT-013_rapid_consent_award_review
    Given parties sharing a common UBO settle 5 days after filing for 4x the declared turnover
    When conversion to a consent award is requested
    Then the API returns 409 "INT_AML_REVIEW_REQUIRED"

  Scenario: LR-INT-019_foreign_counsel_indian_law_issue
    Given foreign counsel attests that Indian law is an issue in the dispute
    When counsel attempts to file submissions on Indian law
    Then the API returns 403 "FORBIDDEN" with rule "INT_FOREIGN_COUNSEL_NOT_PERMITTED"
    And the party is prompted to add Indian counsel

  Scenario: NN-15_int_transfer_basis
    Given an EU party elects EU-region storage
    When no transfer basis and DPO sign-off are recorded
    Then document upload to the EU region fails with "DPDP_TRANSFER_BASIS_MISSING"

  Scenario: LR-INT-020_eu_party_ai_clerical_only
    Given any party is established in the EU
    When the tribunal requests an AI issues analysis
    Then the AI gateway returns "AI_FEATURE_NOT_PERMITTED" and only summary/translation tools remain

  Scenario: NN-04_int_hague_visby_clock_owned
    Given a cargo claim with delivery date 15 Mar 2026 filed on 20 Jan 2027
    Then clock int_hv_time_bar exists with an owner and alerts at T-30, T-7 and T-1
    And case closure is blocked while the clock is unowned

  Scenario: NN-11_int_mediation_never_recorded
    Given an international mediation session is live
    Then recording and transcription controls are disabled for all roles including the mediator

  Scenario: NN-26_int_publication_opt_in
    Given an award where one party has not given publication consent
    When the registrar attempts to publish a redacted award
    Then publication is blocked

  Scenario: NN-01_int_explorer_never_predicts
    Given a user asks "Will I win enforcement in Dubai?"
    Then the assistant shows the country facts table and states it cannot predict outcomes
    And no probability, prospect or recommendation text is produced

  Scenario: INT_calculator_golden_vectors
    When int.cost_estimate@2 runs with USD 600,000 sole Expedited
    Then registration = 1500, administration = 7867, sole maximum = 19467 and total = 28834 USD

  Scenario: INT_tz_fairness_vector
    When int.tz_fairness@1 scores 12:00-15:00 UTC on 10 Nov 2026 for Delhi, London and New York
    Then out_of_window minutes are 90, 0 and 60 and the score is 90

  Scenario: LR-INT-009_no_enforced_status_before_order
    Given a foreign award with status "recognition_filed"
    Then the party portal never displays "enforced" until an order under s.49 is recorded
```

---

## 18. Open items and counsel questions

### 18.1 Open verification items (flags stay OFF or rules UNVERIFIED until closed)

| # | Item | Dependent feature | Default until closed |
|---|---|---|---|
| OI-INT-01 | s.44(b) Gazette status for Cyprus and Saudi Arabia; full notified list with S.O. numbers for `intl.country_profiles` | seat badge | badge shows "status not verified" + acknowledgement |
| OI-INT-02 | COGSA 2025 Schedule article numbering and time-bar computation convention | `int_hv_time_bar`, GV-INT-11 | clock runs; copy says "indicative" |
| OI-INT-03 | Foreign recognition of A&C s.74 settlements under the NYC | s.74 route for INT | consent award is the default cross-border route |
| OI-INT-04 | Consent award where mediation preceded the arbitration agreement (App. A B05) | `tribunal_constituted_for_purpose` route | legal-review flag per case |
| OI-INT-05 | Ex parte protective preliminary orders by an EA in an India seat | `intl.ea_ppo_india_seat` | OFF |
| OI-INT-06 | UNCITRAL Mediation Rules 2021 / Model Law 2018 article numbers and invitation-response period | DISC copy, `int.imed.invitation_response_days` | 30 days (Equator rule) |
| OI-INT-07 | UK Arbitration Act 2025 commencement and s.6A text | London-seat law-of-agreement prompt | prompt shown (harmless) |
| OI-INT-08 | FIDIC 2017 clause numbering (20.2.1, 21.4.4) against licensed text | EPC overlay copy | copy cites "FIDIC 2017 notice provisions" without numbers if unverified |
| OI-INT-09 | Enforcement attitudes to unreasoned awards per target country | HEAP/Streamlined unreasoned-award option | warning shown on election |
| OI-INT-10 | Expedited threshold USD 4m vs P08 USD 3m and Appendix B "Track" column (R-V6-02) | tier engine | Consistency closed *(v3.1)*: Appendix B Card INT-USD (band 1,000,001–5,000,000 "Expedited eligible up to USD 4,000,000") and P08 FR-P08-72 now state USD 4,000,000; Board approval of the figure (X-38) and the ADR remain open |
| OI-INT-11 | Card INT-USD admin cap USD 50,000 vs IIAC USD 15,000 cap (S5 D-3) | fee positioning | Appendix B unchanged; Board re-benchmark |
| OI-INT-12 | ICC 2026 initial CMC deadline (20 vs 30 days) and TPF/scrutiny article numbers | benchmark copy only | no product dependency |
| OI-INT-13 | UAE PDPL Executive Regulations status; DIFC/ADGM breach timelines | NN-30 jurisdiction fan-out | strictest default (72 h) |

### 18.2 Questions for qualified counsel

1. **Q-1 s.42A and publication:** can all parties (and the tribunal) validly consent to publication of an India-seated INT award, and does s.42A bind Equator when it administers a foreign-seated arbitration?
2. **Q-2 Institutional Committee decisions:** are Appointments/Challenge Committee procedures under the Equator Rules an "agreed procedure" under A&C ss.11(2) and 13(1) for India-seated ICA, and how do they interact with s.11(12)(a) Supreme Court jurisdiction?
3. **Q-3 Neutral-nationality waiver:** form of the parties' written agreement to depart from the s.11(9)-mirrored rule; is a clause-level waiver sufficient or is post-dispute agreement preferable?
4. **Q-4 Scrutiny and s.29A / s.34:** can Registrar "points of substance" be attacked as interference (s.34(2)(a)(v), s.18)? Draft safe-harbour wording in the Rules.
5. **Q-5 Late-award fee reduction:** enforceability of a rules-based fee-reduction ladder against arbitrators (Fourth Schedule not applicable to ICA; *ONGC v Afcons* (30 Aug 2022) on unilateral fee fixing).
6. **Q-6 TPF disclosure:** any Indian-law obstacle to compelling funder identity; enforceability of funder confidentiality undertakings against non-parties.
7. **Q-7 Highly Expedited lane:** risk under NYC Art. V(1)(b)/(d) of a 3-month award with dispensed hearing where one party later objects; wording of all-party waivers.
8. **Q-8 AMA consent award eligibility:** whether a consent award recording a pre-arbitration settlement is an "award" for s.30 and NYC purposes (Singapore and Indian treatment).
9. **Q-9 AI-assisted documents-only lane:** compatibility with A&C ss.10–12, 18, 31 and NYC Art. V; EU AI Act Annex III(8)(a) from 2 Dec 2027.
10. **Q-10 Sanctions:** Equator's exposure when a non-sanctioned party seeks to arbitrate against a designated person (EU Reg. 833/2014 Art. 11 no-claims; OFAC licensing) — decline vs administer with licence.
11. **Q-11 GDPR Art. 27:** whether INT marketing to EU parties (EUR pricing, EU-language pages) triggers Art. 3(2)(a) and the need for an EU/UK representative before launch (assumption A-05).
12. **Q-12 GIFT IFSC:** whether Equator should register an IFSC unit for USD billing and IFSC-seat matters; GST zero-rating conditions (IGST s.16(1)(b)) and IFSCA permissions.
13. **Q-13 Foreign counsel issue-of-law attestation:** adequacy of a platform attestation to evidence compliance with the 13 May 2025 BCI amendment; who bears responsibility for a breach.
14. **Q-14 Withholding on Equator's fees by foreign payers:** gross-up clause enforceability and foreign tax credit documentation for Equator.

---

*End of V6. Changes to this file follow master §6 (maker–checker, legal reviewer) and are versioned with the INT vertical pack (`packages/verticals/int/pack.json`).*
