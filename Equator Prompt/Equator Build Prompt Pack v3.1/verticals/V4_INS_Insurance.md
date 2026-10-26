# V4 — Insurance (INS) — Vertical Specification

> Binding for P08d. Read with master, 02, Appendices A, B, F, G, K, L, M.
> Version 2.0 · 21 October 2026 · Law stated as at 21 October 2026 · Operator: Equator Resolution Service Private Limited.
> Source tags used in this file: **[V]** verified in the October 2026 verification pass (RES_A3, GLOBAL_CORRECTIONS, S3) · **[V2]** verified from a secondary source only · **[K]** settled law not re-fetched in the October 2026 pass · **[U]** (competitor data from S3 only) not verified — read as `[VERIFY — open: not verified in S3]` · `[VERIFY — open: <reason>]` unresolved; the dependent feature stays behind a flag or shows "verify" copy until closed (master §0, Appendix G §G.1).

---

## 0. Scope and how to use

**What this file is.** The complete build specification for the `INS` vertical pack (`packages/verticals/ins/`). It supersedes P08 §4.4 where the two differ, except where master §15 precedence says otherwise (master → Appendix G on legal rules → Appendix B on fees → Appendix F on names, events and error codes → Appendix A on states and clocks → this file and P08). Every conflict found while writing this file is listed in §18.2 with the resolution applied.

**What it covers.** Retail and group-member lines (health including cashless, reimbursement, pre-existing disease (PED) and waiting periods, TPA conduct; motor own damage; life death claims and s.45; travel; home/householder and MSME property; crop and rural; government schemes; mis-selling) and B2B lines (commercial fire/IAR, business interruption, marine, engineering, liability, D&O/PI, cyber, trade credit/surety; insurer–insurer, insurer–reinsurer, co-insurance and subrogation; hospital/TPA package disputes; surveyor/assessor expert determination). Motor third-party (TP) injury and death claims are **signpost-only** (MACT exclusive).

**Four constitutional rules for INS (encode as tests; never configurable).**

| Code | Rule | Source | Enforcement |
|---|---|---|---|
| **R1** | No arbitration is administered, drafted, suggested or converted for a retail policyholder or a group member's own claim. Arbitration exists only for commercial/B2B matters under a separately agreed arbitration agreement, on quantum where liability is admitted. Med-arb, arb-med and consent-award conversion follow the same bar. | IRDAI circular IRDAI/NL/CIR/MISC/188/10/2023, 27 Oct 2023 [V]; master §1.2, §5.2; LR-IRDAI-001 | Route matrix (arbitration absent from the retail route set); DB CHECK `ins_no_arbitration_on_retail`; AI output filter IN-G-02; canonical error `INS_RETAIL_ARBITRATION_BLOCKED` (Appendix F) with `rule = "INS-R1"` |
| **R2** | No settlement waives a non-waivable statutory right or discharges future claims; discharge is limited to this claim under this policy; an under-protest voucher must state the balance reserved. | Indian Contract Act 1872 s.23; *National Insurance Co. Ltd. v Boghara Polyfab Pvt. Ltd.* (2009) 1 SCC 267 [K]; LR-IRDAI-008 | Settlement builder hard block + DB CHECKs; canonical error `STATUTORY_WAIVER_FORBIDDEN`, `rule = "INS-R2"` |
| **R3** | No case leaves triage, and no case closes, without a delivered and recorded signposting event (with the last date to act for every relevant forum) and an owner on every statutory clock. At T-60 on the Ombudsman clock a blocking, recorded prompt is required. | NN-04, NN-20; LR-IRDAI-009, LR-IRDAI-013 | DB trigger `ins.guard_triage_exit`, closure policy; canonical errors `SIGNPOSTING_REQUIRED`, `CLOCK_UNOWNED` with `rule = "INS-R3"` |
| **R4** | Free routes first, flat fees only. Where the Insurance Ombudsman, Bima Bharosa, the insurer's grievance cell, a scheme ladder or the Permanent Lok Adalat is available, the party sees it — with its last date — before any Equator fee screen. Retail INS fees are flat or slabbed by amount in dispute; no fee, institutional or neutral, is linked to the amount recovered or settled. | D2-18; NN-18; NN-20; NN-29; X-07; Appendix B P5, Card INS-RET | Fee engine rejects `settlement_linked_*` items for `vertical = 'INS'` (`FEE_CONTINGENCY_FORBIDDEN`); Explorer renders the free-route panel first (UI test) |

**Health data is sealed (NN-07).** Medical records, diagnoses, discharge summaries, bills with clinical line items, PED analyses and the health deduction schedule live only in `health_sealed` (separate KMS key, separate DB role `eq_health`, opaque token, no FK from core, never indexed, never in analytics, exports, notifications, AI prompts or few-shot sets). Core holds only `health_data_token` and aggregate, non-clinical outputs (amounts and error-flag counts).

**How the coding agent uses this file.**
1. Seed the taxonomy (§2, §16) into `core.dispute_types` with `vertical = 'INS'`.
2. Encode §3 rows that are not already in Appendix G as new `LR-IRDAI-*`, `LR-MV-*`, `LR-INS-*` rules (status per the tag; `[VERIFY]` → `VERIFY_PENDING`).
3. Implement §4 as the INS routing rule pack (`packages/verticals/ins/rulepacks/routing.v2.json`) evaluated by `packages/rules`.
4. Implement §5 as the INS Dispute Explorer tree (Appendix K plug-in) and §6 as form schemas in the P02 form engine.
5. Implement §7–§8 as ladder and proceeding configurations over the Appendix A machines; §12 as calculators with golden vectors; §16 as migrations; §17 as acceptance tests.

**Out of scope here.** Insurer GRM desk build (P09; this file defines only the hand-off contract), POSH (P09), SEC (P09), public calculator pages (P13), agent prompts (P11; this file supplies guardrail cases).

---

## 1. Vertical overview

### 1.1 Who it serves

| Segment | Typical need | Default payer (Appendix B) |
|---|---|---|
| Retail policyholders, insured members, nominees, legal heirs | Repudiation, short settlement, cashless denial, delay, mis-selling, non-monetary fixes (reinstatement with continuity, removal of adverse remark) | Flat fee (Card INS-RET) with automatic waivers; ₹0 when insurer-referred under a protocol |
| Group members (employer health, credit-linked, PMJJBY/PMSBY members) | As retail | As retail |
| MSMEs and mid-market insureds | Quantum disputes on fire, stock, burglary, marine cargo, BI | Card INS-COM (ad valorem bands) |
| Large corporates, brokers on their behalf | Commercial lines quantum, coverage, BI, cyber | Card INS-COM |
| Insurers (non-life, life, standalone health) | Settling the settleable early, batched settlement days, Ombudsman-volume reduction, protocol MIS | Card INS-SUB (subscription + batched days) |
| Insurers and reinsurers inter se; insurers v carriers or tortfeasors (subrogation) | B2B mediation, quantum arbitration, expert determination | Card INS-COM |
| Hospitals and TPAs | Package-rate and claim-processing disputes with insurers/SHAs; read-only evidence portal for disputed claims | Card INS-COM (B2B) |

### 1.2 Value proposition (product copy anchor)

"The Insurance Ombudsman decides claims for free. Equator helps you use it on time — and settles, fast, the things an award cannot reach." Equator does four things a policyholder cannot easily do alone and that a statutory forum does not do:
1. **Prepares** the dispute: representation letter, Ombudsman-eligibility check with dates, ground-by-ground schedule, line-item deduction table, survey rebuttal table — free self-help for the Ombudsman route.
2. **Settles** contestable claims by mediation with an insurer officer whose settlement authority is confirmed in writing before the session.
3. **Delivers non-monetary outcomes**: reinstatement with continuity of waiting periods and cumulative bonus, withdrawal of an adverse remark or fraud flag (own records and industry databases), product conversion, written correction, structured payment.
4. **Keeps every clock owned** so no policyholder loses the Ombudsman, Consumer Commission or MACT window while talking to Equator.

For insurers: protocol matters with a 14-day claim-file standard, batched settlement days under a confidential settlement grid, B2B quantum arbitration and surveyor expert determination — with appointment independence (NN-03: insurer–policyholder matters never use party nomination; 40% single-insurer neutral concentration cap).

### 1.3 Mechanisms allowed (master §5.2, applied to INS)

| Mechanism | Retail / group member | Commercial (insured v insurer) | B2B (insurer–insurer, reinsurer, subrogation, hospital/TPA) | Notes |
|---|---|---|---|---|
| Negotiation (assisted; offer/counter-offer) | ✔ | ✔ | ✔ | Blind-bid off for retail (information asymmetry; no "split the difference" nudges — NN-01) |
| Mediation (contractual mode) | ✔ default | ✔ default | ✔ | Statutory mode only if `mediation_statutory_mode` ON (NN-05) |
| Conciliation (A&C Part III) | **Flag `ins.retail_conciliation` OFF** pending counsel (Ombudsman r.14(5) "pending before … arbitrator" question, Q-C9) | ✔ | ✔ | s.73 settlement has s.74 award status |
| Arbitration | **Never (R1)** | Quantum-only, liability admitted, separate arbitration agreement | ✔ (quantum and coverage, per agreement) | NN-03 applies; equal-footing nomination only in B2B where registrar sets `equal_footing = true` |
| Med-arb / arb-med / arb-med-arb | **Never (R1)** | Separate agreement; different neutral by default | ✔ | master §5.3 |
| Expert determination (surveyor/assessor) | Non-binding only, unless both parties make a post-disclosure binding election (`ed_binding_election`) — never binding by policy clause | ✔ binding if agreed | ✔ | Appendix A §3.11 D05 |
| Grievance (insurer desk, GRM) | ✔ (P09) | ✔ | — | `ins_grievance_14d` |
| Signposting | ✔ mandatory first contact | ✔ | ✔ where a statutory forum is exclusive | NN-20, R3 |
| Batched settlement day | ✔ (insurer programme; policyholder free to decline) | ✔ (MSME) | — | `ins.batched_day.v1` |

### 1.4 Status of key laws (as at 21 October 2026)

| Instrument | Status | INS relevance | Tag |
|---|---|---|---|
| Insurance Act 1938 as amended by the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act 2025 | Amendment Act in force **5 Feb 2026** (s.32A amendment held in abeyance) | s.2(10B) "insurance intermediary" now includes insurance consultants, TPAs, surveyors and loss assessors and any entity notified by IRDAI; s.42D(2) registration; s.105BA penalty ₹1 lakh–₹10 lakh for acting unregistered; s.45 **not amended** | [V] RES_A3 Q07; S3 C5 |
| Insurance Act s.45 (as substituted w.r.e.f. 26 Dec 2014 by the Insurance Laws (Amendment) Act 2015) | In force | Life policy cannot be called in question after 3 years from the later of issue, risk commencement, revival or rider | [V] LR-IRDAI-007 |
| Insurance Act s.64UM; IRDAI (Insurance Surveyors and Loss Assessors) Regulations 2015 | In force; **draft amendments published Jun 2026** (not final) | Licensed surveyor mandatory above the s.64UM threshold; insurer may settle at a figure different from the surveyor's assessment **[VERIFY — open (provisional): threshold is set by IRDAI regulations, not the Act (post-2015 proviso); amount and any 2025-Act change not confirmed 22 Oct 2026 — config value, 'verify' copy]** | [V] RES_A3 Q05 |
| IRDAI (Protection of Policyholders' Interests and Allied Matters of Insurers) Regulations 2024 + Master Circular IRDAI/PP&GR/CIR/MISC/117/9/2024 (5 Sep 2024) | In force from 1 Apr 2024 | TAT library (§3.2) | [V] LR-IRDAI-005 |
| IRDAI Master Circular on Health Insurance Business (29 May 2024) | In force | Cashless 1 h / 3 h; moratorium 60 months; PED and specific waiting ≤ 36 months; proportionate-deduction exclusions; claims review committee for rejection **[VERIFY — open (provisional): serial and paragraph numbers not confirmed 22 Oct 2026 (IRDAI site blocks automated fetch); cite by title and date only]** | [V2] RES_A3 Q03; S3 B1–B3 |
| Insurance Ombudsman Rules 2017 (as amended 2021, G.S.R. 147(E), 2 Mar 2021; and 2023, G.S.R. 828(E), 9 Nov 2023) | In force | r.13 grounds; r.14(3) eligibility; r.14(4) condonation; r.14(5) parallel bar; r.16 mediation; r.17 award; ₹50 lakh award cap r.17(3) proviso (ii) | [V] LR-IRDAI-002/003/013 |
| Draft Insurance Ombudsman (Amendment) Rules 2025, G.S.R. 864(E), 25 Nov 2025 | **Draft** (proposed r.17A appellate authority) | Monitor only | [V] LR-IRDAI-004 |
| Draft IRDAI (Internal Insurance Ombudsman) Guidelines 2025 (23 Jul 2025) | **Draft** | Flag `ins_internal_ombudsman` OFF | [V] LR-IRDAI-006 |
| IRDAI circular on arbitration clauses, IRDAI/NL/CIR/MISC/188/10/2023 (27 Oct 2023) | In force | Retail policies carry no arbitration clause; commercial policies: separate arbitration agreement by mutual choice; *Numero Uno Clothing Ltd v United India Insurance Co Ltd*, ARB.P. 1274/2025, Del HC, 10 Nov 2025 | [V] LR-IRDAI-001 |
| Karnataka HC (DB), *Office of the Insurance Ombudsman (Karnataka) v M.V. Narasimha Prasad*, W.A. 1534/2026, 2026:KHC:32548-DB, 1 Jul 2026 | Binding in Karnataka; persuasive elsewhere | rr.14–16 stage informal, no right to an advocate; r.17 award stage — advocate may appear | [V] S3 B0.2 |
| Motor Vehicles Act 1988 (as amended 2019) ss.149, 161, 164, 165–166, 175 | In force | TP claims exclusive to MACT; s.166(3) six-month limit; insurer offer within 30 days under s.149 | [K]; LR-IRDAI-010 **[Verified 22 Oct 2026: s.166(3) in force 1 Apr 2022; SC interim order 4 Nov 2025 in *ICICI Lombard v Ayiti Navaneetha*, SLP(C) 8412-8413/2023 (with *Bhagirathi Dash v UoI*, W.P.(C) 166/2024): no dismissal as time-barred pending decision]** |
| Marine Insurance Act 1963 | In force | Proximate cause (s.55), general average (s.66), subrogation (s.79) | [K] |
| Carriage of Goods by Sea Act 2025 (Act 19 of 2025) | In force **10 Sep 2025** | Subrogated cargo claims: one-year time bar (`hague_visby_1y`) | [V] GLOBAL #12 |
| Carriage by Road Act 2007 s.16; Railways Act 1989 s.106 | In force | Notice-of-claim prerequisites for subrogated recoveries (180 days / 6 months) | [K] |
| Consumer Protection Act 2019 (ss.2(7), 2(11), 34–35, 69) + Jurisdiction Rules 2021 (G.S.R. 912(E), 30 Dec 2021) | In force | Deficiency in service; pecuniary tier by consideration paid; 2-year limitation | [V] LR-CONS-001/002 |
| Legal Services Authorities Act 1987 ss.19–21, 22A–22E | In force | Lok Adalat; Permanent Lok Adalat for insurance service (public utility, s.22A(b)); PLA limit ₹1 crore | [V] S4 B1 P5–P6 |
| Code on Social Security 2020, Ch. VII (Employees' Compensation), S.O. 5319(E), 21 Nov 2025 | In force (EC Act 1923 repealed) | Employment-injury compensation → competent authority, not Equator | [V] LR-IRDAI-011 |
| PMFBY / RWBCIS Revised Operational Guidelines; Krishi Rakshak Portal & Helpline 14447 | In force | DGRC → SGRC ladder; 12% penalty on delayed claim payment from Kharif 2024 | [V] S3 B9 |
| AB PM-JAY grievance guidelines (CGRMS; 14555) | In force | Beneficiary entitlement → scheme ladder | [K] LR-IRDAI-011 |
| A&C Act 1996; Mediation Act 2023 (partly notified, NN-05) | As master | Contractual mediation default; s.73/74 for B2B conciliation | [V] |
| DPDP Act 2023 + Rules 2025 (G.S.R. 846(E), 13 Nov 2025) | Phased | Health data purpose-limited consent; respondent insurer data under s.17(1)(a) | [V] |

---

## 2. Subtype taxonomy

### 2.1 Coding convention

- **L1** `ins.<category>` (11 categories). **L2** `ins.<category>.<subtype>`. Tenants may hide L2s and add L3 labels; they may not unblock a blocked mechanism (FR-P08-02).
- **Policy class** is captured on every case (mandatory, un-skippable): `retail` · `group_member` · `group_master` · `commercial` · `government_scheme` · `b2b_inter_insurer`. `is_retail = policy_class IN ('retail','group_member')` (generated column; Appendix F `ins.policies`). `government_scheme` beneficiary claims follow the scheme ladder; `b2b_inter_insurer` covers insurer–insurer, insurer–reinsurer and subrogation matters where no policyholder is a party.
- **Value bands** (amount in dispute): **R1B** ≤ ₹1,00,000 · **R2B** ₹1,00,001–₹5,00,000 · **R3B** ₹5,00,001–₹20,00,000 · **R4B** ₹20,00,001–₹50,00,000 · **R5B** > ₹50,00,000 (Card INS-RET bands); **C1–C6** = Card INS-COM bands (≤ ₹10 lakh … > ₹50 crore).
- **Ladders** (§7): `ins.retail.v2`, `ins.cashless_live.v1`, `ins.commercial.v2`, `ins.b2b.v1`, `ins.ed.v1`, `ins.batched_day.v1`, `ins.scheme_signpost.v1`, `ins.signpost_only.v1`.
- **Mechanism columns**: ✔ allowed · ✖ blocked (non-configurable) · ◐ allowed with condition stated in Notes · SP = signpost only.

### 2.2 Taxonomy table

| L1 code | L2 code | Name | Typical parties | Value band | Default ladder | Negotiable | Mediable | Arbitrable | Signpost forum | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| `ins.health` | `ins.health.cashless_denial` | Cashless pre-authorisation or discharge denial / delay | Policyholder or member, hospital, TPA, insurer | R1B–R4B | `ins.cashless_live.v1` → spawns `reimbursement_deduction` | ✔ | ◐ post-discharge only | ✖ R1 | Insurer GRO; Ombudsman; Consumer Commission | Live escalation, not mediation, while the patient is admitted; never advise delaying treatment |
| `ins.health` | `ins.health.reimbursement_deduction` | Reimbursement short-settlement (proportionate deduction, non-payables, sub-limits, co-pay, "reasonable and customary") | Policyholder, insurer, TPA | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (r.13(b)); Consumer | Line-item analyser (§12.3) in `health_sealed` |
| `ins.health` | `ins.health.ped_waiting` | Repudiation for PED, specific-disease or initial waiting period | Policyholder, insurer | R1B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Moratorium/continuity calculator (§12.4) |
| `ins.health` | `ins.health.non_disclosure` | Repudiation for non-disclosure / misrepresentation at proposal | Policyholder, insurer, agent | R1B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Proposal filled-by capture; agent may be joined where conduct in issue |
| `ins.health` | `ins.health.tpa_conduct` | TPA delay, repeated document queries, lost documents | Policyholder, TPA, insurer | R1B–R3B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Insurer GRO; Ombudsman (r.13(f) servicing) | Insurer is the accountable respondent; TPA joined as co-respondent |
| `ins.health` | `ins.health.portability_continuity` | Continuity credit refused after portability or migration | Policyholder, acquiring and previous insurer | R1B–R3B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Both insurers joined; continuity is a non-monetary relief |
| `ins.health` | `ins.health.delay_interest` | Settlement delay beyond TAT; interest bank rate + 2% not paid | Policyholder, insurer | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (r.13(a)) | Delay-interest calculator (§12.6) |
| `ins.health` | `ins.health.pa_ci_benefit` | Personal accident / critical illness benefit dispute | Policyholder or nominee, insurer | R1B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Disability % disputes → medical board evidence, not Equator assessment |
| `ins.motor` | `ins.motor.od_quantum` | Own-damage partial loss: depreciation, parts, labour, surveyor assessment | Policyholder, insurer, surveyor, garage | R1B–R3B | `ins.retail.v2` (+ `ins.ed.v1` optional, non-binding) | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Survey Rebuttal Table; joint re-survey protocol |
| `ins.motor` | `ins.motor.total_loss_ctl` | Total / constructive total loss, IDV, salvage, financier NOC | Policyholder, insurer, financier | R2B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Cross-link FIN vehicle loan (V1) for NOC |
| `ins.motor` | `ins.motor.theft` | Theft claim: delay, keys, police final report | Policyholder, insurer | R2B–R4B | `ins.retail.v2` | ✔ | ◐ only after police final report or untraced report | ✖ R1 | Ombudsman; Consumer; police for the offence | NN-24: Equator does not deal with the theft offence |
| `ins.motor` | `ins.motor.breach_no_nexus` | Repudiation for licence/permit/fitness breach without causal nexus | Policyholder, insurer | R2B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Non-standard settlement basis (§12.5) |
| `ins.motor` | `ins.motor.addon_cashless_garage` | Add-on not honoured (zero-dep, engine protect, RTI) or cashless refused at network garage | Policyholder, insurer, garage | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman | Broker-held motor first notice stays with the broker (Policybazaar/InsuranceDekho model) |
| `ins.motor` | `ins.motor.tp_injury_death` | Third-party injury or death compensation | Victim or dependants, owner, insurer | any | `ins.signpost_only.v1` | SP | SP (quantum brief for MACT/Lok Adalat only) | ✖ | **MACT** (s.166; 6 months); DLSA/Lok Adalat | `signpost_only = true`; minors' compromise needs court sanction (CPC O.XXXII r.7) |
| `ins.motor` | `ins.motor.tp_property` | Third-party property damage claim | Third party, owner, insurer | any | `ins.signpost_only.v1` | SP | SP | ✖ | **MACT** (s.165) | `signpost_only = true` |
| `ins.life` | `ins.life.death_claim_s45` | Death claim repudiation (non-disclosure, suppression) incl. early claims | Nominee/heir, insurer | R2B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (≤ ₹50 lakh award cap); Consumer | s.45 chain calculator (§12.7) |
| `ins.life` | `ins.life.death_claim_delay` | Death claim delay beyond 15/45 days; interest | Nominee/heir, insurer | R1B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (r.13(a)) | Fee waiver CN-INS-DEATH |
| `ins.life` | `ins.life.nominee_heir` | Competing claimants: nominee v legal heirs; assignee | Nominee, heirs, insurer, assignee | R2B–R5B | `ins.retail.v2` (insurer as stakeholder) | ✔ | ✔ (payment-direction terms only) | ✖ | Civil court / succession forum; FAM (V3) for the heirship dispute | Succession questions go to FAM; insurer may pay into court under Insurance Act s.47 [K] |
| `ins.life` | `ins.life.maturity_surrender` | Maturity, survival, surrender value, bonus, paid-up value | Policyholder, insurer | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (r.13(f)); Consumer | F-INS-21 behind `ins_forms_f21_f26` |
| `ins.life` | `ins.life.ulip_nav_annuity` | ULIP NAV date, discontinuance fund, charges; annuity rate/commutation | Policyholder/annuitant, insurer | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Pure investment-return disputes without misrepresentation → signpost |
| `ins.life` | `ins.life.lapse_revival` | Lapse, revival refused, premium misapplied | Policyholder, insurer | R1B–R3B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman (r.13(c)) | — |
| `ins.life` | `ins.life.credit_life_assignee` | Credit-linked life cover; lender as assignee | Borrower's family, lender, insurer | R2B–R5B | `ins.retail.v2` (FIN cross-link) | ✔ | ✔ | ✖ R1 | Ombudsman; RBI Ombudsman for lender conduct | Lender joined; loan-closure terms coordinated with V1 |
| `ins.travel` | `ins.travel.medical_abroad` | Overseas medical claim (cashless via assistance company or reimbursement) | Policyholder, insurer, assistance company | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | FX schedule (§12.8); foreign bills: type copy + translation (NN-32) |
| `ins.travel` | `ins.travel.cancellation_delay_baggage` | Trip cancellation, flight delay, baggage, passport loss | Policyholder, insurer | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman | Claims purely against airlines are consumer/aviation matters → signpost |
| `ins.property` | `ins.property.home_householder` | Home / householder (Bharat Griha Raksha) quantum, underinsurance | Policyholder, insurer, surveyor | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Survey Rebuttal Table |
| `ins.property` | `ins.property.msme_sookshma_laghu` | MSME property (Bharat Sookshma / Laghu Udyam Suraksha): stock, average, survey | MSME insured, insurer, surveyor | R2B–C3 | `ins.commercial.v2` | ✔ | ✔ | ◐ only with separate arbitration agreement; quantum-only | Consumer (business insurance is not "commercial purpose": *National Insurance v Harsolia Motors*, SC 2023 [K]) | Ombudsman unavailable for commercial lines (personal lines only) |
| `ins.property` | `ins.property.burglary` | Burglary/housebreaking claims | Insured, insurer | R1B–C2 | `ins.retail.v2` / `ins.commercial.v2` by class | ✔ | ◐ after police final/untraced report | ◐ commercial only | Ombudsman (retail); police for the offence | NN-24 |
| `ins.property` | `ins.property.catastrophe` | Flood/storm/earthquake (STFI) cluster claims | Insureds, insurer | R1B–C3 | `ins.batched_day.v1` | ✔ | ✔ | ◐ commercial only | Ombudsman (retail); Consumer | Batched days after regional events |
| `ins.rural` | `ins.rural.pmfby_rwbcis` | Crop insurance claim / payout / yield dispute | Farmer, bank/CSC, insurer, State | any | `ins.scheme_signpost.v1` | SP | ◐ bank-side lapse only | ✖ | **KRPH 14447 → DGRC → SGRC** | Yield-data disputes between State and insurer → technical committees (excluded) |
| `ins.rural` | `ins.rural.non_enrolment_bank` | Premium debited but farmer not enrolled / proposal not uploaded | Farmer, bank, insurer | R1B–R2B | `ins.retail.v2` (respondent = bank) | ✔ | ✔ | ✖ | KRPH 14447; DGRC; RBI Ombudsman for bank deficiency | Respondent is the bank; voice/IVR vernacular default |
| `ins.rural` | `ins.rural.cattle_farm_micro` | Cattle, farm package, pump-set, micro-insurance claims | Farmer, insurer | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | **Ombudsman** (these lines do go to the Ombudsman) | LR-IRDAI-011 |
| `ins.govt` | `ins.govt.pmjay_beneficiary` | PM-JAY / State scheme beneficiary denied or charged | Beneficiary, hospital, SHA | any | `ins.scheme_signpost.v1` | SP | ✖ (entitlement not mediable) | ✖ | **CGRMS (14555) → District → State → National GRC** | `signpost_only = true` |
| `ins.govt` | `ins.govt.hospital_package` | Hospital–SHA/insurer package-rate or claim-rejection dispute | Hospital, SHA, insurer/TPA | C1–C3 | `ins.b2b.v1` | ✔ | ✔ if SHA willing | ◐ only with agreement | SHA grievance ladder | B2B |
| `ins.govt` | `ins.govt.pmjjby_pmsby` | PMJJBY (life) / PMSBY (accident) claim | Nominee, bank, insurer | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Insurer/bank grievance; Ombudsman **[VERIFY — open (provisional): r.3 covers group insurance; CIO FAQ admits group-member/nominee complaints where the claim is payable to the individual — Ombudsman for insurer decisions; bank lapses (enrolment, auto-debit) to the bank grievance route]** | Fee waiver (government scheme) |
| `ins.com` | `ins.com.fire_iar` | Fire / IAR / SFSP quantum, underinsurance, basis of indemnity | Corporate insured, insurer(s), surveyor, broker | C1–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only, separate agreement | Civil court; Consumer (if eligible) | Co-insurers joined (lead/follow) |
| `ins.com` | `ins.com.business_interruption` | BI / loss of profits computation | Insured, insurer, forensic accountant | C2–C6 | `ins.commercial.v2` (+ `ins.ed.v1`) | ✔ | ✔ | ◐ quantum-only | Civil court | Joint forensic accountant (expert determination) |
| `ins.com` | `ins.com.marine_cargo_hull` | Marine cargo / hull: ICC perils, GA, packing, transit | Cargo owner, insurer, carrier | C1–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil/Admiralty court | Subrogation against carrier → `ins.b2b.subrogation_carrier` |
| `ins.com` | `ins.com.engineering` | CAR/EAR, machinery breakdown, EEI, ALOP/DSU | Contractor/owner, insurer | C1–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil court | Technical expert determination common |
| `ins.com` | `ins.com.liability` | CGL, product, public liability, employer's liability policy coverage | Insured, insurer | C1–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil court | Underlying third-party claim not mediated here unless the third party joins |
| `ins.com` | `ins.com.pi_do` | PI / D&O: notification, retro date, defence costs, conduct exclusions | Insured persons/company, insurer | C2–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil court | Allegations of fraud against insured persons pending adjudication → coverage only, never the underlying fraud (NN-24) |
| `ins.com` | `ins.com.cyber` | Cyber incident response costs, BI, ransomware, social engineering | Insured, insurer, IR vendor | C1–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil court; CERT-In/DPDP notifications are the insured's duty | F-INS-26 behind flag |
| `ins.com` | `ins.com.trade_credit_surety` | Trade credit, surety/performance bond, fidelity | Insured/beneficiary, insurer | C2–C6 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Civil court | — |
| `ins.com` | `ins.com.ec_policy` | Employees' compensation / WC **policy** dispute between employer and insurer | Employer, insurer | C1–C3 | `ins.commercial.v2` | ✔ | ✔ | ◐ quantum-only | Competent authority under CoSS 2020 Ch. VII for the **employee's** claim | The employee's statutory claim is never mediated here |
| `ins.mis` | `ins.mis.bancassurance` | Mis-selling through bank branch / RM (FD-like returns, loan-linked compulsion) | Policyholder, insurer, bank (corporate agent) | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman r.13(d),(g); Consumer; RBI Ombudsman for bank conduct | Scam-warning banner (§5) |
| `ins.mis` | `ins.mis.agent_telecaller` | Mis-selling by agent, telecaller, POSP, web aggregator | Policyholder, insurer, intermediary | R1B–R4B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer; IRDAI via Bima Bharosa | Intermediary joined where conduct in issue |
| `ins.mis` | `ins.mis.free_look_refusal` | Free-look cancellation refused or refund short | Policyholder, insurer | R1B–R2B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman | 30-day free-look; refund 7 days |
| `ins.mis` | `ins.mis.policy_not_issued` | Premium paid, policy not issued / not as proposed | Proposer, insurer | R1B–R3B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman r.13(g),(h) | — |
| `ins.mis` | `ins.mis.churning` | Multiple policies over years, surrender-and-resell | Policyholder (often senior), insurer(s), intermediary | R2B–R5B | `ins.retail.v2` | ✔ | ✔ | ✖ R1 | Ombudsman; Consumer | Vulnerability safeguards default |
| `ins.b2b` | `ins.b2b.co_insurance` | Lead/follow co-insurer share, alignment, contribution | Insurers | C1–C6 | `ins.b2b.v1` | ✔ | ✔ | ✔ per agreement | Civil court | NN-03 equal-footing nomination possible |
| `ins.b2b` | `ins.b2b.double_insurance` | Contribution between insurers covering the same risk | Insurers | C1–C5 | `ins.b2b.v1` | ✔ | ✔ | ✔ per agreement | Civil court | Policyholder paid first; insurers resolve inter se |
| `ins.b2b` | `ins.b2b.reinsurance_fac` | Facultative reinsurance recovery / follow-the-settlements | Cedant, reinsurer | C2–C6 | `ins.b2b.v1` | ✔ | ✔ | ✔ per treaty/slip | Seat per treaty | Foreign seat or foreign reinsurer → INT pack gates (NN-19) |
| `ins.b2b` | `ins.b2b.reinsurance_treaty` | Treaty disputes (proportional / non-proportional), retrocession | Cedant, reinsurer(s) | C3–C6 | `ins.b2b.v1` | ✔ | ✔ | ✔ per treaty | Seat per treaty | Usually treaty arbitration (often offshore); Equator offers mediation and India-seated arbitration where agreed |
| `ins.b2b` | `ins.b2b.subrogation_carrier` | Insurer (as subrogee) v carrier, port, warehouse, contractor or tortfeasor | Insurer (with insured), third party | C1–C5 | `ins.b2b.v1` | ✔ | ✔ | ◐ only with agreement of the third party | Civil court; Consumer only jointly with insured (*Economic Transport Organisation v Charan Spinning Mills* (2010) 4 SCC 114 [K]) | Notice-of-claim clocks (Carriage by Road Act s.16; Railways Act s.106; COGSA 1-year) |
| `ins.b2b` | `ins.b2b.motor_recovery` | Inter-insurer motor recovery (OD insurer v TP insurer of the at-fault vehicle) | Insurers | R1B–C2 | `ins.b2b.v1` (bulk) | ✔ | ✔ | ✔ per agreement | MACT is not involved (property damage recovery between insurers is contractual/tort) | Bulk docket; documents-only arbitration by agreement |
| `ins.b2b` | `ins.b2b.tpa_insurer` | TPA–insurer service-level, fee and claim-file disputes | TPA, insurer | C1–C3 | `ins.b2b.v1` | ✔ | ✔ | ✔ per agreement | Civil court | Health data: only tokens and aggregates cross into core |
| `ins.b2b` | `ins.b2b.hospital_tpa_package` | Hospital–insurer/TPA package-rate, deductions, payment delays | Hospital, insurer, TPA | C1–C3 | `ins.b2b.v1` | ✔ | ✔ | ✔ per agreement | Civil court | Never re-litigates a patient's claim |
| `ins.b2b` | `ins.b2b.broker_insurer` | Premium remittance, brokerage, claims-handling disputes | Broker, insurer | C1–C3 | `ins.b2b.v1` | ✔ | ✔ | ✔ per agreement | Civil court; IRDAI for regulatory breaches | — |
| `ins.ed` | `ins.ed.surveyor_quantum` | Expert determination of quantum by an independent licensed surveyor/assessor | Insured, insurer (or insurers) | R2B–C6 | `ins.ed.v1` | ✔ | ✔ | n/a (not arbitration) | — | Retail: non-binding unless `ed_binding_election` made after disclosure; never the original surveyor |
| `ins.ed` | `ins.ed.technical_cause` | Expert determination of a technical question (cause of failure, BI indemnity period, marine damage cause) | Insured, insurer | C1–C6 | `ins.ed.v1` | ✔ | ✔ | n/a | — | Coverage/liability questions are excluded from ED; ED decides fact/quantum only |

**Not subtypes (hard exclusions, §4.3):** alleged insurance fraud as such; criminal prosecution of a claimant, agent or hospital; staged accidents; arson investigations; "fake IRDAI officer" refund scams (cybercrime 1930); TP motor compensation; employee's statutory compensation claim; PM-JAY beneficiary entitlement.

### 2.3 L3 grounds (insurer's stated reasons) and L4 reliefs

**L3 `ins_ground` (20 values; multi-select; each mapped to a policy clause row in the Ground Schedule):** `non_disclosure` · `misrepresentation_s45` · `ped` · `waiting_period_specific` · `waiting_period_initial` · `exclusion_permanent` · `exclusion_other` · `late_intimation` · `policy_lapsed` · `outside_policy_period` · `documents_incomplete` · `investigation_adverse` · `proximate_cause` · `condition_breach` · `limit_sublimit_exhausted` · `underinsurance_average` · `proportionate_deduction` · `depreciation_salvage` · `fraud_suspected` · `none_given`. (`fraud_suspected` triggers §4.3 fraud screen; `none_given` triggers a reasons-demand letter `TPL-INS-L13`.)

**L4 `ins_relief` (16 values):** `claim_in_full` · `balance_of_claim` · `reverse_deduction` · `cashless_authorisation` · `delay_interest` · `premium_refund` · `policy_conversion_substitution`* · `reinstatement_with_continuity`* · `correction_of_records`* · `written_reasons` · `re_survey_second_opinion` · `adverse_remark_withdrawal`* · `costs` · `apology_corrective_action`* · `payment_direction_competing_claimants` · `other`. (* = `mediation_only_outcome = true`: an Ombudsman award or court decree does not ordinarily deliver it; the Explorer explains this neutrally.)

---

## 3. Legal framework by subtype

### 3.1 Forum map (signposting directory rows seeded by the INS pack)

Each row becomes a `routing_forums` entry (FR-P08-04) with `last_date_to_act` computed from the case's dates. `cost_text` and URLs are re-verified six-monthly by `ForumDirectoryReverifyJob`.

| `forum_code` | Forum | Decides | Who may use | Cost | Limitation / window (rule) | Binding effect | Representation | Legal rule |
|---|---|---|---|---|---|---|---|---|
| `INS_GRO` | Insurer grievance cell (GRO) | Any grievance | Anyone | Free | Reasoned final reply within **14 days**; closed if no complainant reply in 56 days | Gateway only | Self | LR-IRDAI-005 |
| `BIMA_BHAROSA` | IRDAI Bima Bharosa portal (bimabharosa.irdai.gov.in) | Registers, tracks, escalates to the insurer and IRDAI | Anyone | Free | — | Not adjudicatory | Self; Equator never files on a party's behalf | LR-IRDAI-012 |
| `INS_OMBUDSMAN` | Insurance Ombudsman (Council for Insurance Ombudsmen; 17 offices) | r.13 grounds (a)–(i) for personal lines | Individuals and personal-line policyholders (incl. group member's own claim) | Free | Written representation first; then within **1 calendar year** of rejection / unsatisfactory reply / expiry of one month without reply (r.14(3)); condonable (r.14(4)); barred if pending or decided before a court, consumer forum or arbitrator (r.14(5)) | Award binds the insurer if the complainant accepts; cap **₹50 lakh** incl. expenses (r.17(3) proviso (ii)); insurer complies within 30 days; ₹5,000/day for delay | No advocate at rr.14–16 (mediation); advocate permitted at r.17 award stage (Karnataka HC, 1 Jul 2026) | LR-IRDAI-002/003/013 |
| `CONSUMER_DCDRC` / `CONSUMER_SCDRC` / `NCDRC` | Consumer Commissions (filing on e-Jagriti) | Deficiency in service; compensation | Consumers (insurance bought for business is not excluded per *Harsolia Motors*) | Low (court fee slab) | **2 years** from cause of action, condonable (CPA 2019 s.69); tier by **consideration paid** (District ≤ ₹50 lakh; State > ₹50 lakh–₹2 crore; National > ₹2 crore — G.S.R. 912(E), 30 Dec 2021) **[VERIFY — open (counsel): engine uses premium paid as consideration (statutory text); no NCDRC/SC insurance ruling retrieved 22 Oct 2026 — show claim-basis tier as alternative]** | Order, appealable | Self or advocate/agent | LR-CONS-001/002/003 |
| `PLA_INSURANCE` | Permanent Lok Adalat (public utility service: insurance) | Conciliation, then decision on merits if no settlement (s.22C(8)) | Either party, before suit | Free | Before any suit; pecuniary limit **₹1 crore** | Award final, no appeal (s.22E) | Self | LR-LSA-PLA (new; §16.6) |
| `LOK_ADALAT_PRELIT` | Pre-litigation Lok Adalat (DLSA/SLSA; National Lok Adalat days) | Records settlements; cannot adjudicate | Both parties | Free | — | Award = decree (LSA Act s.21) | Self | LR-LSA-LA (new) |
| `CIVIL_COURT` | Civil court / commercial court | Anything | Anyone | High | **3 years** — Limitation Act 1963 Art. 44 (from death; from occurrence of loss, or from denial of the claim where denied) [K]; policy suit-bar clause shown but labelled contestable | Decree | Advocate | LR-INS-LIM-44 (new) |
| `MACT` | Motor Accidents Claims Tribunal | TP injury/death/property compensation (exclusive; civil courts barred, s.175) | Victims, dependants, owners of damaged property | Low | Application within **6 months** of the accident (s.166(3)) **[Verified 22 Oct 2026: SC interim order 4 Nov 2025, SLP(C) 8412-8413/2023 — tribunals and HCs 'shall not dismiss claim petitions on the ground that the petitions are barred by limitation' pending decision; show the 6-month date as 'act early', never as a bar]**; insurer offer under s.149 within 30 days | Award/decree; consent settlement recorded by the Tribunal | Advocate common | LR-IRDAI-010 |
| `COSS_EC_AUTHORITY` | Competent authority, Code on Social Security 2020 Ch. VII | Employment-injury compensation | Employee / dependants | Free | Per CoSS Ch. VII | Statutory order | Self/representative | LR-IRDAI-011 |
| `PMJAY_CGRMS` | PM-JAY Central Grievance Redressal Management System (14555) → District → State → National GRC | Beneficiary entitlement, wrongful charging | Beneficiaries, hospitals | Free | Per NHA guidelines | Administrative | Self | LR-IRDAI-011 |
| `PMFBY_KRPH` / `PMFBY_DGRC` / `PMFBY_SGRC` | Krishi Rakshak Portal & Helpline 14447; District and State Grievance Redressal Committees | Crop insurance grievances | Farmers | Free | Localised-calamity intimation within **72 hours** (scheme rule) [K]; ladder per Revised Operational Guidelines | Administrative; 12% penalty on delayed claims computed on NCIP | Self | LR-IRDAI-011 |
| `RBI_OMBUDSMAN` | RBI Ombudsman (RB-IOS 2026) | Bank/NBFC deficiency (bancassurance conduct; premium debited not remitted) | Bank customers | Free | RE first; 30 days; then 90 days (X-13) | Award | Self | LR-RBI-001 |
| `POLICE_1930` | Police / National Cybercrime Helpline 1930 | Offences (theft, fake-IRDAI-officer fraud, forgery) | Anyone | Free | Immediate | — | — | NN-24 |
| `ADMIRALTY_COURT` | High Court (admiralty) / civil court | Maritime claims against carriers, vessels | Insurer as subrogee with insured | High | COGSA 2025 one-year bar (`hague_visby_1y`) | Decree | Advocate | LR-INS-COGSA (new) |

### 3.2 Insurer turnaround-time (TAT) library (LR-IRDAI-005; Master Circular IRDAI/PP&GR/CIR/MISC/117/9/2024, 5 Sep 2024) [V]

| Code | Event | TAT | Clock kind | Consequence surfaced to user |
|---|---|---|---|---|
| TAT-01 | Grievance to insurer | Acknowledge immediately; reasoned final reply within 14 days | `ins_grievance_14d` | "Reply due by {date}" — breach strengthens the Ombudsman ground r.13(a) |
| TAT-02 | Cashless pre-authorisation | 1 hour from request | `ins_cashless_preauth_1h` (new, informational) | Breach timestamp computed for the escalation note |
| TAT-03 | Cashless discharge authorisation | 3 hours from final bill; excess hospital charges borne by the insurer from shareholder funds | `ins_cashless_discharge_3h` (new, informational) | As above |
| TAT-04 | Health reimbursement (no investigation) | 15 days from claim submission | `ins_claim_settlement_30d` (Appendix A name; period per line) | Delay interest |
| TAT-05 | Life death claim, no investigation | 15 days from intimation | same | Delay interest |
| TAT-06 | Life death claim, with investigation (incl. settlement) | 45 days from intimation | same | Delay interest |
| TAT-07 | General insurance — surveyor appointment (retail) | 24 hours | same | — |
| TAT-08 | General insurance — survey report | 15 days | same | — |
| TAT-09 | General insurance — pay or reject | 7 days from survey report | same | Delay interest |
| TAT-10 | Delay interest | Bank rate + 2% p.a. from intimation to payment, suo motu | — | §12.6 |
| TAT-11 | Free-look (life and health) | 30 days; refund within 7 days of cancellation | `ins_free_look_30d` (new, informational) | Mis-selling route |
| TAT-12 | Ombudsman award compliance | 30 days; ₹5,000 per day of delay to the complainant | `ins_award_compliance_30d` (new, informational) | Compliance tracking only (Equator is not a party to the Ombudsman award) |

### 3.3 Law by subtype

| L2 | Statute / section | Forum(s) | Limitation & statutory clocks | Key case law (tag) | Status / flags |
|---|---|---|---|---|---|
| `health.cashless_denial` | Health Master Circular (29 May 2024): pre-auth 1 h, discharge 3 h; rejection only with approval of the insurer's claims review committee, reasons tied to policy terms [V2] | INS_GRO → Ombudsman; Consumer | TAT-02/03; then reimbursement clocks | — | Paragraph refs **[VERIFY — open (provisional): not obtained 22 Oct 2026; cite by title/date]** |
| `health.reimbursement_deduction` | Health MC 2024: proportionate deduction not applied to pharmacy/medicines, consumables, implants and medical devices, diagnostics; ICU not category-based; deduction only where the hospital bills the head differentially by room category; IRDAI standard non-payables list [V2] | Ombudsman r.13(b); Consumer | TAT-04; `ins_ombudsman_1y`; `ins_consumer_2y` | *Manmohan Nanda v United India Assurance* (2022) 4 SCC 582 (insurer bound by its acceptance after medical screening) [K] | **[VERIFY — open (provisional): 2020 circular number and Health MC paragraph not confirmed 22 Oct 2026; cite the 2024 Health MC by title/date only]** |
| `health.ped_waiting` | Health MC 2024 (effective for policies issued/renewed from 1 Apr 2024): moratorium **60 continuous months** — thereafter no claim contestable except for established fraud and permanent exclusions; PED waiting max **36 months**; specific-disease waiting max **36 months**; portability continuity credits [V2] | Ombudsman; Consumer | As above | *Satwant Kaur Sandhu v New India Assurance* (2009) 8 SCC 316 (material non-disclosure) [K]; *Manmohan Nanda* [K] | Transition for pre-2024 policies (old 8-year moratorium; 48-month PED) applies by policy date/renewal **[VERIFY — open (counsel): transition text not read 22 Oct 2026; engine computes both regimes and presents the policyholder-favourable one as argued position]** |
| `health.non_disclosure` | Contract Act s.19 (voidable for misrepresentation); proposal-form questions; burden on insurer | Ombudsman; Consumer | As above | *Mithoolal Nayak v LIC* AIR 1962 SC 814 [K]; *Satwant Kaur Sandhu* [K] | — |
| `health.tpa_conduct` | PPHI Regs 2024 (insurer accountable for TPA); Insurance Act s.2(10B) (TPA = intermediary) | INS_GRO; Ombudsman r.13(f) | TAT-01/04 | — | — |
| `health.portability_continuity` | Health MC 2024 portability provisions (previous insurer shares data within 72 h; acquiring insurer decides within 5 days) [V2] | Ombudsman; Consumer | — | — | **[VERIFY — open (provisional): paragraph refs not obtained 22 Oct 2026; TATs informational only]** |
| `motor.od_*` | Policy wording (legacy India Motor Tariff depreciation and CTL > 75% of IDV conventions adopted in wordings) [K]; Insurance Act s.64UM (licensed surveyor) [V] | Ombudsman; Consumer | TAT-07/08/09; `ins_ombudsman_1y` | *New India Assurance v Pradeep Kumar* (2009) 7 SCC 787 (survey report not the last word) [K]; *Sri Venkateswara Syndicate v Oriental Insurance* (2009) 8 SCC 507 (second surveyor needs reasons) [K] | — |
| `motor.breach_no_nexus` | Policy conditions; Motor Vehicles Act s.149(2) defences (TP) | Ombudsman; Consumer | As above | *National Insurance v Nitin Khandelwal* (2008) 11 SCC 259; *Amalendu Sahoo v Oriental Insurance* (2010) 4 SCC 536 (non-standard settlement where breach has no nexus) [K]; *Lakhmi Chand v Reliance General Insurance* (2016) 3 SCC 100 (breach must be fundamental) [K] | — |
| `motor.theft` | Policy conditions (intimation, keys, final report) | Ombudsman; Consumer | Policy intimation clause; `ins_ombudsman_1y` | *Nitin Khandelwal* [K] | Mediation gated on police final/untraced report |
| `motor.tp_*` | MV Act ss.149 (insurer settlement offer), 161 (hit-and-run), 164 (no-fault), 165–166, 175 [K] | MACT exclusive; DLSA Lok Adalat | `mact_6m` (new; trigger accident date; informational-owned) | — | LR-IRDAI-010 **[Verified 22 Oct 2026: in force 1 Apr 2022; SC interim order 4 Nov 2025 bars dismissal for delay pending decision — clock stays informational]** |
| `life.death_claim_s45` | Insurance Act s.45 [V]; s.39 (nomination; beneficial nominees), s.38 (assignment), s.47 (payment into court) [K] | Ombudsman (award cap ₹50 lakh); Consumer; civil court | TAT-05/06; `ins_ombudsman_1y`; Art. 44(a) 3 years from death | *Mithoolal Nayak* [K]; *Reliance Life Insurance v Rekhaben Nareshbhai Rathod* (2019) 6 SCC 175 [K]; *Mahakali Sujatha v Future Generali India Life Insurance* (SC, 2024) **[VERIFY — open (provisional): citation not confirmed 22 Oct 2026; internal use only, not in templates]** | — |
| `life.nominee_heir` | Insurance Act s.39 (beneficial nominees: parents, spouse, children) [K]; s.47 | Civil court; FAM (V3) | Art. 44(a) | — | Equator mediates only payment-direction terms; heirship → FAM |
| `life.ulip_nav_annuity`, `life.maturity_surrender` | IRDAI product regulations (ULIP discontinuance charges and fund) [K] | Ombudsman r.13(f); Consumer | — | — | F-INS-21 behind flag |
| `travel.*` | Policy wording; FX conversion per wording (date-of-loss rate default) | Ombudsman; Consumer | TAT-07/09 | — | — |
| `property.*` (retail, MSME) | Standard products Bharat Griha Raksha, Bharat Sookshma / Laghu Udyam Suraksha (from 1 Apr 2021) [K]; average/underinsurance per wording | Ombudsman (retail only); Consumer; civil court | GI TATs; `ins_consumer_2y`; Art. 44(b) | *National Insurance v Harsolia Motors* (SC, 13 Apr 2023) **[VERIFY — open (provisional): report citation not confirmed 22 Oct 2026]** | Arbitration only for commercial/MSME with separate agreement |
| `rural.pmfby_rwbcis` | PMFBY Revised Operational Guidelines; NCIP 12% penalty on delayed claims (from Kharif 2024) [V] | KRPH 14447 → DGRC → SGRC | 72-hour intimation (localised calamity) `pmfby_intimation_72h` (new, informational) | — | — |
| `govt.pmjay_beneficiary` | AB PM-JAY guidelines | CGRMS 14555 | Per guidelines | — | signpost_only |
| `com.*` | Policy wording; Marine Insurance Act 1963 ss.55, 66, 79 [K]; standard commercial arbitration clause (separate agreement) per IRDAI circular 27 Oct 2023 [V] | Civil/commercial court; arbitration by separate agreement | Art. 44(b); policy suit-bar (contestable); `arb_s29a` | *Numero Uno Clothing* (Del HC, 10 Nov 2025) [V]; *United India Insurance v Orient Treasures* (2016) 3 SCC 49 (contra proferentem) [K]; *Texco Marketing v TATA AIG General Insurance* (2023) 1 SCC 428 (exclusion clauses must be disclosed to the insured) [K] | — |
| `mis.*` | Ombudsman r.13(d) misrepresentation of terms, (g) policy not per proposal, (h) non-issue after premium; free-look; Insurance Act s.41 (rebates prohibited) [K]; CPA 2019 s.2(47) unfair trade practice | Ombudsman; Consumer; Bima Bharosa | `ins_free_look_30d`; `ins_ombudsman_1y` | *Texco Marketing* [K] | — |
| `b2b.reinsurance_*` | Treaty/slip; A&C Act Part I (India seat) or Part II (foreign award) | Per treaty | Per treaty; `arb_s29a` (India seat) | — | Foreign party → INT gates (NN-19) |
| `b2b.subrogation_carrier` | Marine Insurance Act s.79; equitable subrogation and subrogation-cum-assignment [K]; Carriage by Road Act 2007 s.16 (notice within 180 days); Railways Act 1989 s.106 (notice within 6 months); COGSA 2025 (one-year bar) | Civil/admiralty court; Consumer only jointly with the insured | `hague_visby_1y`; `carriage_road_notice_180d` (new); `railway_notice_6m` (new); Limitation Act Art. 10/Art. 113 per claim **[VERIFY — open (provisional): working map — Art.10 loss/damage, Art.11 non-delivery/delay, Art.113 residual (3 y each); rail claims to Railway Claims Tribunal (RCT Act s.17, 3 y); sea 1 y; air 2 y (Montreal Art.35); primary texts not re-read 22 Oct 2026]** | *Economic Transport Organisation v Charan Spinning Mills* (2010) 4 SCC 114 [K] | — |
| `ed.*` | Contract (expert determination clause or post-dispute ED agreement); s.64UM licensing for surveyors; not arbitration (no A&C Part I remedies) | Expert | `ed_submissions` 21 d, `ed_comments` 14 d (Appendix A) | — | Binding effect contractual; retail non-binding by default |
| All retail | A&C s.7 + IRDAI circular (no retail arbitration); *Emaar MGF Land v Aftab Singh* (SC, 10 Dec 2018) (consumer remedy not ousted) [V] | — | — | — | LR-IRDAI-001; LR-CONS-003 |
| All | Contract Act s.23 / *Boghara Polyfab* (discharge vouchers; coercion) [K] | — | — | — | LR-IRDAI-008 |

### 3.4 Insurance Ombudsman grounds (r.13) mapping

| r.13 ground | Code | L2s that map to it |
|---|---|---|
| (a) delay in settlement beyond regulatory TAT | `OMB_A_DELAY` | `health.delay_interest`, `life.death_claim_delay`, any L2 with TAT breach |
| (b) partial or total repudiation of claims | `OMB_B_REPUDIATION` | all claim L2s |
| (c) disputes over premium paid or payable | `OMB_C_PREMIUM` | `life.lapse_revival`, `mis.*` |
| (d) misrepresentation of policy terms and conditions | `OMB_D_MISREP` | `mis.*` |
| (e) legal construction of insurance policies in relation to claims | `OMB_E_CONSTRUCTION` | coverage disputes |
| (f) policy servicing grievances against insurer, agent or intermediary | `OMB_F_SERVICING` | `health.tpa_conduct`, `life.maturity_surrender`, `life.ulip_nav_annuity` |
| (g) issuance of policy not in conformity with the proposal | `OMB_G_NONCONFORMITY` | `mis.policy_not_issued`, `mis.bancassurance` |
| (h) non-issuance of policy after receipt of premium | `OMB_H_NONISSUE` | `mis.policy_not_issued` |
| (i) other non-adherence to regulations linked to (a)–(h) | `OMB_I_OTHER` | residual |

Source: Insurance Ombudsman Rules 2017 r.13 as amended 2021 (CIO terms and conditions) [V].

---

## 4. Suitability and eligibility rules

All rules are deterministic (`packages/rules`), versioned in the INS rule pack, pinned at filing (NN-21) and evaluated identically by the AI-assisted Explorer and the deterministic questionnaire (NN-02). The AI may classify the L2 with confidence; below 0.80 the user confirms. Outcomes: `accept` · `accept_with_conditions` · `signpost` · `reject`. Suitability enum (stored in `ins.triage_records.suitability`): `suitable` · `suitable_with_safeguards` · `shuttle_only` · `not_suitable_forum` · `not_suitable_fraud` · `not_suitable_criminal` · `not_suitable_urgent`. Rule (Equator Insurance Rules r.7): **never declined without a route** — every `reject`/`signpost` outcome carries at least one forum row with a last date to act.

### 4.1 Evaluation order

1. Hard exclusions (§4.3) → `reject` + signpost (or `signpost` only).
2. Urgent and safety triggers (§4.4) → interrupt flow with the urgent route.
3. Exclusive-forum checks (TP motor, scheme beneficiary, employment injury) → `signpost`.
4. Policy class (R1) → mechanism set.
5. Ombudsman eligibility engine (§4.6) → free-route panel (always shown first for retail).
6. Limitation and clock checks (§4.7).
7. Suitability scoring and safeguards (§4.8).
8. Fee quote (Appendix B; free routes already displayed).

### 4.2 Master decision table (INS-SE)

| Rule | Inputs (conditions) | Outcome | Routes offered | Routes blocked (reason code) | Mandatory disclosure (template key) |
|---|---|---|---|---|---|
| INS-SE-01 | `l2 ∈ {motor.tp_injury_death, motor.tp_property}` | `signpost` | MACT; DLSA Lok Adalat; quantum-document brief (no computation) | Ombudsman, Consumer, arbitration, Equator mediation as decision forum (`INS_TP_MACT_EXCLUSIVE`) | `ins.disc.mact_6m` — "Claims for injury, death or property damage caused by a motor vehicle go to the Motor Accidents Claims Tribunal. Apply within 6 months of the accident ({date})." + Ayiti Navaneetha note behind flag `ins.mact_delay_note` (OFF until verified) |
| INS-SE-02 | `l2 = govt.pmjay_beneficiary` | `signpost` | CGRMS 14555 ladder | all Equator mechanisms (`INS_SCHEME_LADDER`) | `ins.disc.pmjay` |
| INS-SE-03 | `l2 = rural.pmfby_rwbcis` ∧ respondent ∈ {insurer, State} | `signpost` | KRPH 14447 → DGRC → SGRC; Equator document pack (free) | Ombudsman, arbitration | `ins.disc.pmfby` (72-hour intimation; 12% penalty interest is automatic on NCIP) |
| INS-SE-04 | `l2 = rural.non_enrolment_bank` | `accept_with_conditions` | Equator mediation v bank (voice/vernacular default); KRPH; RBI Ombudsman | arbitration | `ins.disc.rbio` + `ins.disc.pmfby` |
| INS-SE-05 | claim is the employee's own employment-injury compensation | `signpost` | Competent authority CoSS Ch. VII | all | `ins.disc.coss_ec` |
| INS-SE-06 | `is_retail = true` (retail or group_member) | continue | per rows below | arbitration, med-arb, arb-med, arb-med-arb, consent-award conversion (`INS_RETAIL_ARBITRATION_BLOCKED`, rule INS-R1) | `ins.disc.retail_no_arbitration` |
| INS-SE-07 | retail ∧ `representation_date` null | `accept_with_conditions` | Step 1: generate representation letter (F-INS-04) + Bima Bharosa registration guidance (party registers); Equator negotiation may run in parallel | Ombudsman until C1–C2 satisfied | `ins.disc.write_first` — "Write to the insurer first. Its reply is due by {rep+1 month}. The Ombudsman can take your complaint after that." |
| INS-SE-07a | retail ∧ `representation_date` set ∧ engine C2 = `wait_until` (insurer's one month not yet over and no reply) | `accept_with_conditions` | Equator negotiation or mediation may start now in parallel; Ombudsman available from `reply_due_late` (shown as a date); diary reminder to the party and case manager on that date; case sub-state `awaiting_insurer_reply` (P08 §5) | Ombudsman until `reply_due_late` | `ins.disc.wait_for_reply` — "Your insurer has until {reply_due_late} to reply. If it does not reply, or you are not happy, you can go to the Ombudsman from that date. Last date: {last_date_to_file}." *(v3.1: this combination matched no row)* |
| INS-SE-08 | retail ∧ Ombudsman engine `eligible = true` | `accept` | **Ombudsman (free) shown first**; Equator mediation (parallel, flat fee); Consumer; PLA | arbitration | Schedule A script (verbatim) + `last_date_to_file` |
| INS-SE-09 | retail ∧ engine `condonation_needed = true` | `accept_with_conditions` | Consumer; civil court; Equator mediation; Ombudsman **with condonation request** (help to state reasons) | arbitration | `ins.disc.condonation` — "The one-year window closed on {date}. The Ombudsman may still admit your complaint if it condones the delay (Rule 14(4))." |
| INS-SE-10 | retail ∧ `amount_in_dispute > ₹50,00,000` | `accept` | Ombudsman (award capped at ₹50 lakh incl. expenses) shown with Consumer Commission (tier by premium paid) and civil court; Equator mediation | arbitration | `ins.disc.award_cap` |
| INS-SE-11 | retail ∧ `legacy_arbitration_clause = true` | `accept` | Ombudsman; Consumer; court; Equator mediation | arbitration | `ins.disc.legacy_clause` — clause recorded; IRDAI circular 27 Oct 2023; consumer remedy not ousted |
| INS-SE-12 | retail ∧ `pending_forum ∈ {consumer_commission, civil_court}` | `accept_with_conditions` | That forum + Equator mediation (party informs the forum; any settlement disposed of "in terms") | Ombudsman (r.14(5)), arbitration | `ins.disc.parallel_forum` |
| INS-SE-13 | retail ∧ `pending_forum = ombudsman` | `accept_with_conditions` | Ombudsman continues; Equator mediation only if both parties consent and the complainant is told the Ombudsman's own r.16 mediation is free | arbitration | `ins.disc.ombudsman_pending` |
| INS-SE-14 | retail ∧ `ins.retail_conciliation` OFF ∧ mechanism requested = conciliation | `accept_with_conditions` | Mediation substituted | conciliation (`INS_RETAIL_CONCILIATION_FLAG_OFF`) | `ins.disc.conciliation_off` |
| INS-SE-15 | `policy_class = commercial` ∧ `arbitration_agreement = separate_agreement` ∧ `liability_admitted = true` | `accept` | Mediation first (30 days before first arbitration hearing); quantum arbitration; ED; civil | Ombudsman (`INS_OMBUDSMAN_PERSONAL_LINES_ONLY`) | `ins.disc.commercial_arb_quantum` |
| INS-SE-16 | commercial ∧ separate agreement ∧ `liability_admitted = false` | `accept_with_conditions` | Mediation; ED on quantum/technical facts; civil court for liability | arbitration of liability under this pack (`INS_ARB_LIABILITY_NOT_ADMITTED`) | `ins.disc.liability_first` |
| INS-SE-17 | commercial ∧ `arbitration_agreement ∈ {none, clause_in_policy_post_circular}` | `accept` | Mediation; arbitration only on a fresh separate agreement (e-signed post-dispute, independent-advice prompt) | — | `ins.disc.commercial_no_agreement`; post-circular policy clause → note *Numero Uno* |
| INS-SE-18 | `policy_class = group_master` (employer v insurer on the group contract) | `accept` | As commercial | Ombudsman | — |
| INS-SE-19 | `policy_class = b2b_inter_insurer` | `accept` | Mediation; arbitration per agreement; ED; equal-footing nomination if registrar sets `equal_footing` | Ombudsman | — |
| INS-SE-20 | any party foreign (reinsurer abroad; foreign carrier) | `accept_with_conditions` | Run the V6 INT gates G1–G6 (sanctions, KYC/UBO, DPDP s.16 transfer, FEMA route, internationality test, seat/law; NN-19) before registration | — | `int.disc.gates` |
| INS-SE-21 | `fraud_alleged_by_insurer = true` ∧ no `fraud_mediation_approval_ref` | `reject` (for mediation of the claim) | Investigation outcome / litigation; Ombudsman; Consumer | Equator mediation of the claim (`INS_FRAUD_NOT_MEDIABLE` → canonical `MECHANISM_NOT_PERMITTED_FOR_VERTICAL`) | `ins.disc.fraud` — neutral wording; no inference of guilt |
| INS-SE-22 | fraud alleged ∧ express joint written request ∧ Head of Legal approval ref | `accept_with_conditions` | Mediation of **consequences only** (e.g., refund of premium, policy cancellation terms), never of whether fraud occurred | — | `ins.disc.fraud_consequences` |
| INS-SE-23 | `l2 = health.cashless_denial` ∧ `patient_admitted = true` | `accept_with_conditions` | Live escalation (`ins.cashless_live.v1`) | mediation sessions until discharge | `ins.disc.cashless_never_delay` — "Do not delay treatment. Keep all bills; you can claim reimbursement." |
| INS-SE-24 | `insurer_settlement_authority_confirmed = false` at session scheduling | hold | Notice + authority request (F-INS-06) | session (`INS_AUTHORITY_UNCONFIRMED`) | — |
| INS-SE-25 | `used_claim_consultant = success_fee` | `accept_with_conditions` | Proceed; neutral informed of a third-party fee interest (not its amount) | — | `ins.disc.consultant_fee` — "The Ombudsman is free. You do not need to pay a percentage of your claim to use it." |
| INS-SE-26 | `l2 = life.nominee_heir` ∧ heirship contested | `accept_with_conditions` | Mediation of payment direction among claimants with the insurer as stakeholder; heirship/succession → FAM (V3) or civil court | arbitration of heirship (NN-06 testamentary/succession limits) | `ins.disc.heirship` |
| INS-SE-27 | `l2 = motor.theft` ∧ police final/untraced report absent | `accept_with_conditions` | Hold mediation; diary date; Ombudsman clock still runs | session | `ins.disc.theft_report` |
| INS-SE-28 | `l2 ∈ ins.ed.*` ∧ `is_retail` | `accept_with_conditions` | ED non-binding; binding only on post-disclosure `ed_binding_election` by the policyholder (e-signed) | binding ED by policy clause (`INS_ED_RETAIL_BINDING_BLOCKED`) | `ins.disc.ed_nonbinding` |
| INS-SE-29 | proposed expert = surveyor who surveyed this loss, or did any work for this insurer in the cooling-off period (default 24 months) | — | Different expert | appointment (`CONFLICT_DETECTED`, rule INS-ED-CONFLICT) | — |
| INS-SE-30 | pure ULIP investment-return grievance without misrepresentation | `signpost` | Ombudsman (if servicing); Consumer | Equator mediation optional | `ins.disc.ulip_returns` |
| INS-SE-31 | claim purely against an airline / tour operator | `signpost` | Consumer Commission; airline grievance | INS pack | `ins.disc.not_insurance` |
| INS-SE-32 | yield-data dispute State v insurer (PMFBY) | `reject` | Technical advisory committees under the scheme | all | `ins.disc.pmfby_technical` |
| INS-SE-33 | any retail case | — | Permanent Lok Adalat row always present in signposting table (insurance = public utility service) | — | `ins.disc.pla` |
| INS-SE-34 | `vulnerability_flags ≠ ∅` (senior 65+, bereavement < 90 days, disability, low literacy, serious illness) | `accept_with_conditions` | Safeguards (§4.8) + automatic waivers (Appendix B CN-*) | blind-bid | — |
| INS-SE-35 | Default — no row above produced `signpost`, `reject` or a mechanism set | `accept` | L1 default ladder (§7); Schedule A script for retail (or the variant script); "Talk to a person" (free) | per R1 | Schedule A / variant *(v3.1: explicit catch-all — FR-P08-85)* |

### 4.3 Hard exclusions (HX-INS) — never administered; always signposted

| Code | Exclusion | Route shown | Basis |
|---|---|---|---|
| HX-INS-01 | Determining whether insurance fraud, forgery, impersonation or a staged loss occurred | Insurer investigation; police; court | Equator policy (C2 Rule 12); NN-24 |
| HX-INS-02 | Criminal prosecution of any person (claimant, agent, hospital, garage, surveyor); compounding of offences; "settling" an FIR | Police / court | NN-24; App. K §3 |
| HX-INS-03 | Fake IRDAI / Ombudsman / "refund officer" calls, refund-recovery scams | National Cybercrime Helpline 1930; cybercrime.gov.in; police | NN-24; S3 B11 |
| HX-INS-04 | TP motor compensation (injury, death, property) as a decision | MACT | MV Act ss.165–166, 175 |
| HX-INS-05 | Employee's statutory employment-injury claim | CoSS Ch. VII authority | LR-IRDAI-011 |
| HX-INS-06 | PM-JAY / State scheme beneficiary entitlement | CGRMS 14555 | LR-IRDAI-011 |
| HX-INS-07 | Any arbitration (or arbitral conversion) against a retail policyholder or group member | Ombudsman / Consumer / court / mediation | R1 |
| HX-INS-08 | Settlement of a minor's or person-with-disability's claim without the required court sanction (MACT, civil) | Tribunal/court | CPC O.XXXII r.7 [K] |
| HX-INS-09 | Heirship/succession determination (who inherits) | FAM (V3) / civil court | NN-06 |
| HX-INS-10 | Disputes requiring the Ombudsman's statutory recommendation or award (Equator cannot issue either) | Ombudsman | NN-17 (never imply official status) |
| HX-INS-11 | Regulatory penalties, licence actions against insurers/intermediaries | IRDAI (via Bima Bharosa for complaints) | — |

### 4.4 Urgent and safety triggers (UT-INS)

| Code | Trigger (detected from intake answers or keywords; AI flags, rules decide) | Action |
|---|---|---|
| UT-INS-01 | Patient currently admitted and cashless denied/pending | Switch to `ins.cashless_live.v1`; show "Do not delay treatment" banner; generate timestamped escalation note to insurer GRO + TPA within 15 minutes (SLA); never schedule a mediation session while admitted |
| UT-INS-02 | Bereavement within 90 days (death claim) | `suitable_with_safeguards`; tone template `bereavement`; no outbound sales-style messaging; fee waiver CN-INS-DEATH; IN-G-09 hand-off available |
| UT-INS-03 | Threats, harassment by recovery staff or agent; self-harm language | Stop flow; show Tele-MANAS 14416 / emergency 112; human callback; NN-24 signposting for threats |
| UT-INS-04 | Ombudsman last date within 30 days | Red banner on every screen; "File with the Ombudsman now — this does not stop you using Equator later"; one-click F-INS-07 self-help pack; case manager task (blocking) |
| UT-INS-05 | MACT 6-month date within 30 days | Red banner; MACT/DLSA directory; quantum-document checklist |
| UT-INS-06 | Consumer 2-year date within 60 days | Amber banner; e-Jagriti link |
| UT-INS-07 | Hospital demanding signature on an undertaking or a discharge voucher "full and final" under pressure | Show under-protest endorsement text (`TPL-INS-L04`) immediately; F-INS-17 guidance |

### 4.5 Jurisdiction checks

| Check | Rule | Effect |
|---|---|---|
| J-01 | Insurer is IRDAI-registered (lookup `core.organisations.regulator_ids.irdai_regn`) | Unregistered "insurer" → `signpost` to police/1930 and IRDAI; do not convene |
| J-02 | Policy issued in India; for overseas insurers (travel assistance company) the policy issuer must be an Indian insurer | Foreign issuer → INT pack gates or signpost |
| J-03 | Ombudsman centre resolved by complainant's address district from the CIO jurisdiction table (config `ins.ombudsman.centre_map`, versioned), with the alternative centre for the insurer's or broker's branch/office offered (r.14(1); territories fixed by the Council under r.11(2)) **[Verified 22 Oct 2026: Insurance Ombudsman Rules 2017 r.14(1), r.11(2), CIO consolidated text; G.S.R. 147(E) of 2021 only added brokers]** | Centre name and address on F-INS-07 |
| J-04 | Consumer tier by **consideration paid** (premium), not claim value | `CONSUMER_DCDRC` / `SCDRC` / `NCDRC` |
| J-05 | Seat for commercial/B2B arbitration from the agreement; default Equator seat New Delhi; foreign seat → INT pack | — |
| J-06 | Language of proceedings defaults to the policyholder's chosen language; insurer participation in English permitted with interpretation at ₹0 to individual parties (Appendix B P5) | — |

### 4.6 Ombudsman Eligibility Engine v2 (`ins.ombudsman_eligibility@2`)

| # | Condition | Rule | Output if true | Output if false |
|---|---|---|---|---|
| C1 | Written representation sent | `representation_date IS NOT NULL` (letter, email, online, Bima Bharosa) — r.14(3)(a) | pass | `write_first`; generate F-INS-04 |
| C2 | Insurer rejected, replied unsatisfactorily, or did not reply within one month | `reply_outcome ∈ {rejected, unsatisfactory}` OR `today ≥ reply_due_late` where `reply_due_late = max(rep + 30 days, rep + 1 calendar month)` — r.14(3)(a); General Clauses Act 1897 s.3(35) "month" = British calendar month | pass | `wait_until {reply_due_late}` (diary date) |
| C3 | Within one year | `trigger = insurer_reply_date ?? reply_due_early` where `reply_due_early = min(rep + 30 days, rep + 1 calendar month)`; `last_date_to_file = trigger + 1 calendar year` (same date next year; General Clauses Act s.3(66)); pass if `today ≤ last_date_to_file` — r.14(3)(b) | pass | `condonation_needed` (r.14(4)) — never "ineligible" |
| C4 | Amount within award cap | `amount_in_dispute ≤ ins.ombudsman.award_cap_minor` (default 50,00,00,000 paise = ₹50,00,000) — r.17(3) proviso (ii) | pass | `award_cap_exceeded` (soft; Ombudsman still shown with cap note + Consumer Commission) — LR-IRDAI-002 open item |
| C5 | Not pending or decided elsewhere | `pending_forum IS NULL OR pending_forum ∉ {court, consumer_commission, arbitration}` — r.14(5) | pass | `parallel_bar` (Ombudsman closed while pending) |
| C6 | Personal line | `is_retail = true` or policy is a personal line held by an individual | pass | `not_personal_line` → Ombudsman not shown |

**Conservative date rule (binding).** Where the law's "one month" can be read as 30 days or one calendar month, the engine uses the **later** date to decide when the party may file (so a premature complaint is not rejected) and the **earlier** date to compute the last date to file (so the party is never told a later deadline than the strictest reading). Both dates are shown in the computation trace. Leap-day handling: a trigger on 29 February rolls to 28 February of the next year (config `ins.leap_day_rule = 'feb28'`) **[Product decision 22 Oct 2026: keep feb28 — earlier of the two readings (GCA s.9 exclusion of first day; calendar year GCA s.3(66)); counsel confirmation non-blocking]**.

**Output object** (`GET /v1/cases/{caseId}/ins/ombudsman-eligibility`): `{ c1..c6: {pass, reason_code, rule_id}, eligible, condonation_needed, award_cap_exceeded, parallel_bar, reply_due_early, reply_due_late, last_date_to_file, days_left, centre: {code, name, address}, r13_grounds[], fallback_routes[], config_version, computation_trace[] }`. `eligible = c1 ∧ c2 ∧ c3 ∧ c5 ∧ c6` (C4 is advisory).

### 4.7 Limitation and clock checks at triage

| Check | Clock (Appendix A kind) | Owner | Alert policy | Rule |
|---|---|---|---|---|
| L-01 | `ins_insurer_reply_30d` (computed with the C2 conservative rule) | case_manager | AP-M | LR-IRDAI-002 |
| L-02 | `ins_ombudsman_1y` | case_manager | AP-L; **blocking T-60 prompt** (unless case ≥ `outcome_drafted`); T-30 head of operations; unprompted expiry = Critical incident | LR-IRDAI-002/009/013 |
| L-03 | `ins_consumer_2y` | case_manager | AP-L | LR-CONS-002 |
| L-04 | `ins_policy_suit_bar` (per wording; label "contestable") | case_manager | AP-L | **[Verified 22 Oct 2026: void to that extent for policies issued on/after 8 Jan 1997 — s.28(b); *IndusInd Bank* (2016) 9 SCC 720; *Oriental Insurance v Sanjesh* (SC, 2022); warning only, never a bar]** |
| L-05 | `limitation_contract` adapted as `ins_civil_art44` (new) — 3 years per Limitation Act Art. 44 | case_manager | AP-L | LR-INS-LIM-44 |
| L-06 | `mact_6m` (TP signpost only) | case_manager (informational-owned) | AP-INFO + owner prompt | LR-IRDAI-010 |
| L-07 | `hague_visby_1y`, `carriage_road_notice_180d`, `railway_notice_6m` (subrogation) | insurer's case lead (enterprise) + case_manager | AP-L / AP-M | LR-INS-COGSA etc. |
| L-08 | `arb_s29a` (commercial/B2B arbitration) | registrar | AP-29A | Appendix A |
| L-09 | `med_contract_timebox` INS 45 d | case_manager | AP-M | Appendix A |

Rules: Equator mediation **never pauses** any clock (IN-G-06); copy-lint blocks "pauses", "stops the clock", "extends your time" in INS templates. A standstill agreement template is not offered in INS retail (Q-C1 open; consumer and Ombudsman windows are not contractually extendable by the insurer).

### 4.8 Suitability scoring and safeguards

Score (0–100, deterministic; not shown to the respondent): documentary clarity (written grounds present 20; policy wording present 10; claim file/survey produced 10) + amount proportionality (fee ≤ 10% of amount in dispute 15) + respondent engagement history (insurer protocol member 15) + contestability markers (ground ∈ {proportionate_deduction, ped with moratorium crossed, breach_no_nexus, s.45 window crossed, none_given} 20) + relationship/non-monetary relief requested 10. Bands: ≥ 60 invite; 40–59 invite with "free Ombudsman first" emphasis; < 40 signpost-led (Equator mediation still available on request). Score never changes fees, neutral allocation or the free-route display.

| Safeguard | Trigger | Implementation |
|---|---|---|
| Support person | any vulnerability flag | `support_person` participant link (no account) |
| Interpreter (₹0) | language ≠ insurer's working language | `interpreter` participant; Sarvam/Bhashini for documents (labelled "for convenience", NN-32) |
| Shuttle-only | power imbalance flagged by neutral or party request | `shuttle_only` |
| Shorter sessions | senior, illness | ≤ 45-minute sessions |
| Automatic waivers | Appendix B CN-INS-SMALL (< ₹50,000), CN-INS-DEATH, CN-SENIOR (age ≥ 60 from KYC) 50%, CN-PWD 50%, CN-GOVT-SCHEME 100%, CN-LEGALAID 100% institutional | applied by engine without request |
| No blind-bid, no deadline pressure | all retail | negotiation module config |

---

## 5. Dispute Explorer question tree (Appendix K plug-in `ins`)

Plain English, class-8 reading level, ≤ 20 words per question, Hindi parity required (NN-23). Every question has an "I'm not sure" option that routes to a clarifying question or to a human callback, never to a guess (IN-G-01). The tree is the same whether the AI assistant or the deterministic questionnaire runs it (NN-02). The **free-route panel** is rendered before any fee for every retail outcome (R4).

### 5.1 Common trunk (all INS)

| QID | Question | Options | Branch | Outcome codes |
|---|---|---|---|---|
| INS-Q00 | Is anyone in danger, being threatened, or did someone call asking for money to "release" your claim? | Yes, danger or threat · Someone called asking for a fee/refund · No | Danger → UT-INS-03; fee call → HX-INS-03; No → Q01 | `OUT_URGENT`, `OUT_SCAM_1930` |
| INS-Q01 | What kind of insurance is this? | Health or accident · Vehicle · Life · Travel · Home or shop · Crop or cattle · Government scheme (Ayushman/PMJAY, PMJJBY, PMSBY) · Business or factory · Not sure | → L1 branch; Not sure → Q01a | — |
| INS-Q01a | What does your policy paper say at the top? (Upload a photo or type the plan name.) | Upload · Type · Skip | OCR + classifier (confidence ≥ 0.80 else ask user to pick) | — |
| INS-Q02 | Who bought the policy? | Me or my family · My employer or a group (bank, society) · My company or business · An insurance company (reinsurance/recovery) | Me → `retail`; employer/group → Q02a; company → `commercial`; insurer → `b2b_inter_insurer` | sets `policy_class` |
| INS-Q02a | Is this about your own claim as a member, or the group contract itself? | My own claim · The group contract | own → `group_member`; contract → `group_master` | — |
| INS-Q03 | What went wrong? | Claim rejected · Paid less than claimed · Not paid yet / delay · Cashless refused at hospital · Policy sold wrongly · Policy service problem · Other | → L1 branch questions | sets `decision` |
| INS-Q04 | Did the insurer give reasons in writing? | Yes (upload) · No reasons given · Not sure | No → flag `none_given`; letter `TPL-INS-L13` | — |
| INS-Q05 | Have you written a complaint to the insurer yet? | Yes — date · Yes, on Bima Bharosa — date and token · No | No → INS-SE-07 | sets `representation_date` |
| INS-Q06 | Did the insurer reply? | Rejected — date · Replied but not satisfied — date · No reply yet | → engine C2/C3 | sets `reply_outcome` |
| INS-Q07 | Is this already in a consumer commission, court, Ombudsman or arbitration? | No · Consumer commission · Court · Ombudsman · Arbitration · MACT | → C5 / INS-SE-12/13 | sets `pending_forum` |
| INS-Q08 | How much money is in dispute? | Amount (₹) · Not about money only | → C4; value band | — |
| INS-Q09 | Has the insurer said this is fraud? | Yes · No · Not sure | Yes → INS-SE-21 | `OUT_FRAUD_SIGNPOST` |
| INS-Q10 | Is a police case (FIR) involved? | No · Yes, theft/accident report only · Yes, a case against me or someone else | case against a person → NN-24 note: Equator handles only the money claim, the police/court handle the offence | — |
| INS-Q11 | Do you need help to take part? | Language help · I am 65 or older · Disability support · Recent death in family · None | sets vulnerability flags | — |
| INS-Q12 | Have you signed up with a claim-help company or lawyer for this? | No · Yes, I pay a fixed fee · Yes, they take a share of my claim · Lawyer | share → INS-SE-25 | — |

### 5.2 L1 branches

| QID | L1 | Question | Options | Branch / outcome |
|---|---|---|---|---|
| INS-H01 | health | Are you (or the patient) in hospital right now? | Yes · No, discharged · Not admitted | Yes + cashless issue → UT-INS-01 / `OUT_CASHLESS_LIVE` |
| INS-H02 | health | What did the insurer do? | Refused cashless · Cut part of the bill · Rejected for an old illness · Rejected for not telling something · Waiting-period reason · Delay · TPA keeps asking for papers | → `health.*` L2 |
| INS-H03 | health | When did this policy (or the first policy you moved from) start? | Date · I moved (ported) from another insurer — first date | → continuity calculator |
| INS-H04 | health | Was your room more expensive than your policy room limit? | Yes · No · Not sure | Yes → proportionate-deduction check |
| INS-H05 | health | Who filled your proposal form? | I did · Agent · Bank staff · Online · Don't know | sets `proposal_filled_by` |
| INS-M01 | motor | Was someone else hurt or killed, or someone else's property damaged? | Yes · No, only my vehicle | Yes → INS-SE-01 `OUT_MACT` (stop) |
| INS-M02 | motor | What happened to your vehicle? | Damaged · Total loss · Stolen · Fire/flood | → `motor.*` |
| INS-M03 | motor | Why did the insurer cut or reject? | Depreciation · Licence/permit issue · Late intimation · Add-on not given · Surveyor amount low · Other | → L2; licence → no-nexus question |
| INS-M04 | motor | Did the licence/permit issue cause the accident? | No, unrelated · Yes · Not sure | No → `breach_no_nexus` |
| INS-M05 | motor | (Theft) Has the police given a final or "untraced" report? | Yes · Not yet | Not yet → INS-SE-27 |
| INS-L01 | life | Who is claiming? | Nominee · Legal heir (not nominee) · Lender/assignee · Policyholder (maturity/surrender) | heir v nominee → INS-SE-26 |
| INS-L02 | life | When did the policy start, and was it ever revived? | Start date · Revival date · No revival | → s.45 chain |
| INS-L03 | life | Is anyone else also claiming the money? | No · Yes, family members disagree | Yes → FAM cross-link |
| INS-T01 | travel | Where and when did it happen? | Country · Date | FX date |
| INS-T02 | travel | What kind of claim? | Medical · Trip cancelled · Flight delay · Baggage · Passport | → `travel.*`; airline-only → INS-SE-31 |
| INS-P01 | property | Home, shop/small factory, or big business? | Home · Shop/MSME · Large business | home → retail; MSME/large → commercial |
| INS-P02 | property | What caused the loss? | Fire · Flood/storm · Earthquake · Burglary · Other | burglary → police-report check |
| INS-P03 | property | Did the insurer reduce the claim for "underinsurance" (average)? | Yes · No · Not sure | Yes → underinsurance calculator |
| INS-R01 | rural | Is this crop insurance (PMFBY/weather scheme) or cattle/farm insurance? | Crop · Cattle/farm · Not sure | crop → Q R02; cattle → `rural.cattle_farm_micro` |
| INS-R02 | rural | Was premium taken from your bank account but you were not enrolled? | Yes · No | Yes → `non_enrolment_bank`; No → INS-SE-03 `OUT_PMFBY_LADDER` |
| INS-G01 | govt | Are you a PM-JAY/Ayushman card holder refused treatment or charged? | Yes · I am a hospital with a package dispute | Yes → INS-SE-02 `OUT_CGRMS`; hospital → `govt.hospital_package` |
| INS-S01 | mis-selling | Who sold you the policy? | Bank staff · Agent · Phone call · Website/app · Don't know | `sold_by` |
| INS-S02 | mis-selling | What were you told? (tick all) | Like an FD · Pay once only · Needed for a loan/locker · Guaranteed returns · Bonus/refund of old policy · Someone said they were from IRDAI | IRDAI caller → scam banner |
| INS-S03 | mis-selling | When did you receive the policy papers? | Date | → free-look check (30 days) |
| INS-C01 | commercial | Does the policy or a separate agreement say "arbitration"? | Separate agreement · Clause in policy · No · Not sure | → INS-SE-15/16/17 |
| INS-C02 | commercial | Has the insurer accepted the claim in principle and disputes only the amount? | Yes · No · Partly | → `liability_admitted` |
| INS-C03 | commercial | Are other insurers (co-insurers) on this risk? | Yes — names and shares · No | co-insurers joined |
| INS-B01 | b2b | Who is the other side? | Another insurer · A reinsurer · A carrier/port/contractor · A TPA · A hospital · A broker | → `b2b.*` |
| INS-B02 | b2b | Is any party based outside India? | Yes · No | Yes → INS-SE-20 INT gates |
| INS-B03 | b2b | (Subrogation) When was the carrier/third party given written notice of the claim? | Date · Not yet | notice clocks (L-07) |

### 5.3 Explorer outcome codes

`OUT_OMBUDSMAN_FREE_FIRST` · `OUT_WRITE_TO_INSURER_FIRST` · `OUT_CONDONATION` · `OUT_AWARD_CAP` · `OUT_PARALLEL_FORUM` · `OUT_CASHLESS_LIVE` · `OUT_MACT` · `OUT_CGRMS` · `OUT_PMFBY_LADDER` · `OUT_COSS_EC` · `OUT_FRAUD_SIGNPOST` · `OUT_SCAM_1930` · `OUT_URGENT` · `OUT_FAM_HEIRSHIP` · `OUT_EQUATOR_MEDIATION` · `OUT_EQUATOR_COMMERCIAL` · `OUT_EQUATOR_B2B` · `OUT_ED` · `OUT_NOT_INSURANCE`. Each outcome renders: (1) free/statutory forums with last dates, (2) what Equator can add, (3) indicative fee from the engine (only after 1–2), (4) "Talk to a person" (free).

### 5.4 Free-forum disclosures (Schedule A v2 — verbatim; versioned `TPL-INS-N02 v2`)

Delivered at first contact, before any other step, in the party's language; recorded with channel, language, script_version and delivered_by (LR-IRDAI-009; Appendix A §3.15 T03). v2 corrects the v1 script, which stated "binds the insurer up to ₹30 lakh".

> 1. "There is a free government-recognised forum for this: the **Insurance Ombudsman**. It costs nothing and you do not need a lawyer to complain."
> 2. "First, write to your insurer. If it rejects your complaint, does not reply within one month, or you are not happy with the reply, you can go to the Ombudsman."
> 3. "You must go to the Ombudsman within **one year** of the insurer's reply (or of the end of that month if it does not reply). For you, the last date is **{last_date_to_file}**. If you are late, you can still ask the Ombudsman to accept it, giving your reasons."
> 4. "The Ombudsman can award up to **₹50 lakh**. If you accept the award, the insurer must pay within 30 days."
> 5. "You may also go to the **Consumer Commission** within two years, or the **Permanent Lok Adalat**. Going to a consumer commission or court closes the Ombudsman route while that case is pending."
> 6. "Equator Resolution is a **private** dispute-resolution service. It is **not** the Ombudsman, IRDAI, a court or a government body. Using Equator does **not** stop or pause any of these dates."
> 7. "Equator can help you settle with the insurer by agreement, including things an award may not give — like continuing your policy without losing waiting periods, or removing a wrong remark."

Variant scripts: `TPL-INS-N02-MACT`, `-PMFBY`, `-PMJAY`, `-COMMERCIAL` (no Ombudsman; civil court and arbitration-by-agreement facts), `-B2B` (no free-forum script; NN-20 satisfied by forum note only).

### 5.5 Scam-warning banner (`ins.banner.scam`, shown on every INS screen and in the first message)

"IRDAI, the Insurance Ombudsman and Equator will **never** call you to collect a fee for releasing a claim or refunding an old policy. If someone does, call **1930** or report at cybercrime.gov.in."

---

## 6. Intake and submission forms per mechanism

Canonical IDs `F-INS-NN` (P08 FR-P08-50) with v2 additions F-INS-27 to F-INS-36. All forms run in the P02 form engine (`sensitive`, `visibleWhen`, `requiredWhen`, `mapsTo`). Fields marked **[S]** are `sensitive: health` and are stored only in `health_sealed` (core receives the token). Dates are `date` (IST); money is `money_inr` (integer paise; displayed in Indian grouping).

### 6.1 Common INS core block `INS-CORE` (embedded in every party-initiated form)

| field_id | Label | Type | Req | Options / dropdown | Validation | Help text |
|---|---|---|---|---|---|---|
| `policy_class` | Who bought this policy? | enum | Y | DD-INS-01 | 400 `VALIDATION_FAILED` (rule `FORM_FIELD_REQUIRED`) if missing (un-skippable) | "This decides which options are open to you." |
| `line_l1` | Type of insurance | enum | Y | DD-INS-02 | — | — |
| `subtype_l2` | What the dispute is about | enum | Y | DD-INS-03 (filtered by L1) | AI may pre-fill; user confirms | — |
| `insurer_org_id` | Insurance company | lookup | Y | IRDAI-registered insurers (directory) | J-01 | "Pick from the list. Can't find it? Tell us the name." |
| `policy_no` | Policy number | text | Y | — | 4–40 chars; stored masked + HMAC | — |
| `policy_start`, `policy_end` | Policy period | date | Y | — | end ≥ start | — |
| `first_inception_date` | When did your first policy with continuous cover start? | date | C (health, life) | — | ≤ `policy_start` | "If you moved from another insurer, give the first date." |
| `sum_insured` | Sum insured / IDV / sum assured | money_inr | Y | — | > 0 | — |
| `intermediary_type` | Who sold it? | enum | N | DD-INS-07 | — | — |
| `intermediary_name_code` | Seller name / licence code | text | N | — | — | — |
| `tpa_org_id` | TPA (health) | lookup | C | TPA directory | — | — |
| `claim_no` | Claim number | text | C | — | masked | — |
| `loss_date` | Date of loss / event / admission / death | date | Y (claims) | — | ≤ today | — |
| `claim_intimation_date` | Date you told the insurer | date | C | — | ≥ `loss_date` | — |
| `claim_docs_complete_date` | Date you gave the last document | date | N | — | ≥ intimation | Drives TAT-04/09 |
| `decision` | What did the insurer decide? | enum | Y | DD-INS-08 | — | — |
| `decision_date` | Date of decision letter | date | C | — | ≥ intimation (400 `VALIDATION_FAILED`, rule `ins.decision_before_intimation`) | — |
| `amount_claimed` | Amount you claimed | money_inr | Y | — | — | — |
| `amount_paid` | Amount paid or offered | money_inr | N | — | ≤ claimed (400 `VALIDATION_FAILED`) | — |
| `amount_in_dispute` | Amount in dispute | money_inr | Y | — | auto = claimed − paid (editable with reason) | — |
| `insurer_grounds[]` | Reasons the insurer gave | multi-enum | Y | DD-INS-04 | ≥ 1 (or `none_given`) | — |
| `ground_clause_quote` | Clause the insurer relied on | textarea ≤ 1,000 | N | — | — | — |
| `representation_date` | Date you complained in writing to the insurer | date | N | — | ≤ today | — |
| `representation_mode` | How did you complain? | enum | C | letter · email · insurer_portal · bima_bharosa | — | — |
| `bima_bharosa_token` | Bima Bharosa complaint number | text | N | — | pattern per config | "You register it yourself; we only store the number." |
| `insurer_reply_date` | Date of insurer's reply | date | N | — | ≥ representation (400 `VALIDATION_FAILED`, rule `ins.reply_before_representation`) | — |
| `reply_outcome` | What did the reply say? | enum | C | rejected · unsatisfactory · satisfied · no_reply | — | — |
| `pending_forum` | Is this already elsewhere? | enum | Y | DD-INS-10 | — | — |
| `pending_forum_ref` | Case number / centre | text | C | — | required if pending ≠ none | — |
| `claimant_role` | You are the | enum | Y | DD-INS-09 | nominee/heir → identity + relationship proof | — |
| `fraud_alleged_by_insurer` | Has the insurer alleged fraud? | enum | Y | yes · no · not_sure | yes → INS-SE-21 | — |
| `discharge_voucher_status` | Did you sign a discharge voucher? | enum | C | not_signed · full_final · under_protest · on_account | under_protest → `balance_reserved` > 0 | — |
| `used_claim_consultant` | Are you using a claim-help company or lawyer? | enum | Y | DD-INS-11 | success_fee → INS-SE-25 | — |
| `relief_sought[]` | What do you want? | multi-enum | Y | DD-INS-05 | ≥ 1 | — |
| `relief_total` | Total amount asked | money_inr | C | — | — | — |
| `vulnerability[]` | Support needed | multi-enum | N | DD-INS-12 | — | Never shown to the other side |
| `language_pref` | Language | enum | Y | 12 enabled languages | — | — |
| `health_data_consent` | I agree that my health information may be used only for this dispute | checkbox | C (health, life, PA, travel medical) | — | must be true to upload [S] documents | Separate from general consent (DPDP s.6) |
| `health_authority_scope` | I authorise Equator to request my claim file and medical records from the insurer/TPA/hospital for this dispute only | checkbox + e-sign | N | — | creates `authority_ref` | — |
| `declaration_not_official` | I understand Equator is not the Ombudsman, IRDAI, a consumer commission or a court | checkbox | Y | — | — | — |

### 6.2 Negotiation request — `F-INS-27` (new; retail and commercial; L2s: all mediable)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| INS-CORE | — | block | Y | — | — | — |
| `neg_mode` | How do you want to start? | enum | Y | equator_letter_to_insurer · assisted_online_offers · insurer_settlement_day (if insurer on protocol) | settlement_day only if `insurer.protocol = true` | — |
| `opening_position` | What would resolve this for you? | structured | Y | amount (money_inr) + non-monetary terms (DD-INS-05 subset flagged *) | amount ≤ `relief_total` | "You can change this later. The insurer won't see your private notes." |
| `offer_validity_days` | How long should your proposal stay open? | int | Y | 7–14 (default 14) | 7–14 | — |
| `acceptance_authority` | Who can accept for you? | enum | Y | me · representative_under_loa | LoA scope checked (NN-27) | — |
| `consent_neg_rules` | I agree to the Equator Negotiation Rules (version pinned) | checkbox | Y | — | — | — |

### 6.3 Mediation request — `F-INS-02` (retail/group: VERTICAL; commercial/B2B: plus `INS-COM-EXT`)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| INS-CORE | — | block | Y | — | — | — |
| `account_of_dispute` | Tell us what happened (short) | textarea | Y | — | ≤ 400 words; AI may summarise with source anchors only (NN-25) | Specimen shown |
| `mediation_mode` | How should sessions happen? | enum | Y | online · in_person · hybrid · shuttle_only | — | — |
| `city_for_in_person` | City | enum | C | Equator venues | — | — |
| `preferred_slots[]` | Three preferred dates | datetime[3] | Y | — | 08:00–19:00 IST | — |
| `neutral_prefs` | Preferences | multi-enum | N | language · gender_woman_neutral · medical_background · surveyor_background · consumer_side_background | Allocation filters only (NN-28); never insurer-chosen | — |
| `accept_staged_payment` | Would you accept payment in parts? | enum | N | yes · no · discuss | — | — |
| `documents[]` | Upload | file[] | Y | §9 checklist for L2 | per checklist mandatory set | [S] items routed to `health_sealed` |
| `fee_payer` | Who pays? | enum | Y | me · insurer_under_protocol (auto) · waiver_requested | engine computes (Card INS-RET) | Fee shown only after the free-route panel |
| `consent_med_rules` | I agree to the Equator Insurance Mediation Rules (version pinned) incl. confidentiality and no recording | checkbox | Y | — | — | — |
| `ack_clocks_not_paused` | I understand Equator does not stop the Ombudsman, consumer or MACT deadlines | checkbox | Y | — | — | — |

**`INS-COM-EXT`** (commercial/B2B): `insured_cin_gstin` (text, Y, CIN/GSTIN checksum), `co_insurers[]` (lookup + share %, sum = 100%), `lead_insurer_id` (lookup), `broker_org_id` (lookup), `basis_of_indemnity` (DD-INS-15), `deductible` (money), `arbitration_agreement_status` (DD-INS-14, Y), `liability_admitted` (enum yes/no/partly, Y), `reinsurer_concurrence_needed` (enum yes/no/unknown), `quantum_claimed_vs_assessed` (table: head, claimed, surveyor assessed, difference), `authorised_signatory_id` (org signatory with authority limit; NN-27).

### 6.4 Arbitration request / Statement of claim — `F-INS-28` (new; **commercial, group_master and B2B only**)

Form is not renderable when `is_retail = true` (form-engine `visibleWhen` + API 422 `INS_RETAIL_ARBITRATION_BLOCKED`).

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| INS-CORE + INS-COM-EXT | — | block | Y | — | `policy_class ∈ {commercial, group_master, b2b_inter_insurer}` | — |
| `arb_agreement_doc` | Separate arbitration agreement (or treaty/slip clause) | file | Y | — | signed by both; date ≥ policy inception or post-dispute | — |
| `arb_agreement_date` | Date of agreement | date | Y | — | — | — |
| `scope` | Scope of reference | enum | Y | quantum_only · quantum_and_coverage (B2B only) | commercial insured v insurer → `quantum_only` forced (INS-SE-15/16) | — |
| `liability_admission_ref` | Insurer's written admission of liability | file | C (commercial) | — | required for `quantum_only` | — |
| `mediation_precondition_done` | Has 30-day mediation been completed? | enum | Y | yes (case ref) · no (start now) · waived_by_all (e-signed) | default starts mediation | Equator Rules (INS Rule 22) |
| `tribunal_size` | Number of arbitrators | enum | Y | 1 · 3 | 3 = 2.5 × sole fee (Card INS-COM) | — |
| `equal_footing_request` | Request co-arbitrator nomination (B2B only) | enum | N | yes · no | only `b2b_inter_insurer`; registrar decides (NN-03) | — |
| `seat` | Seat | enum | Y | Equator cities · foreign (→ INT) | — | — |
| `claim_heads[]` | Claim heads | table | Y | head (DD-INS-16) · amount · interest basis · currency | INR default; INT currencies only via INT pack | — |
| `statement_of_facts` | Statement of facts | rich text / AI Pleadings Studio (App. M) | Y | — | NN-25 anchors | — |
| `documents_relied` | Documents relied on | bundle | Y | — | BSA s.63(4) certificate on export (NN-10) | — |
| `expedited_request` | Documents-only fast track | enum | N | yes · no | claims ≤ C2 band default yes | — |

### 6.5 Response / Statement of defence / Counterclaim — `F-INS-06` (insurer response & claim-file statement; extended)

| field_id | Label | Type | Req | Options | Validation | Help |
|---|---|---|---|---|---|---|
| `responding_officer` | Officer name & designation | text | Y | — | — | — |
| `participation` | Will you take part? | enum | Y | agree · agree_subject_to_approval · decline · joint_case_conference | decline → F-INS-19 | — |
| `position` | Your position | enum | Y | maintained · admitted_full · admitted_part_revised_offer · reopened · reserved | — | — |
| `revised_offer` | Revised offer | money_inr | C | — | ≤ claimed | — |
| `settlement_authority_limit` | Settlement authority of the attending officer | money_inr | Y | — | > 0; required before any session (INS-SE-24) | — |
| `approver_above_limit` | Approver above the limit & turnaround (hours) | text + int | Y | — | turnaround ≤ 72 h | — |
| `coinsurer_reinsurer_concurrence` | Co-insurer / reinsurer concurrence needed? | enum | Y | none · co_insurer · reinsurer · both | if needed → name + expected date | — |
| `grounds_table[]` | Grounds (each with clause, evidence) | table | Y | ground (DD-INS-04) · clause ref · evidence doc · page | each row needs a clause or "none" | — |
| `claim_file_produced[]` | Claim file documents produced | checklist | Y | wording at loss date · proposal form · repudiation/computation letter · survey report · investigation report · TPA notes · call recordings (mis-selling) | non-production of a listed item requires reason code (DD-INS-17) | Within 14 days (Rule 9) |
| `surveyor_name_licence` | Surveyor / investigator & IRDAI licence no. | text | C | — | licence format per config | — |
| `retail_commercial_confirmation` | Policy class confirmation | enum | Y | retail_no_arb_clause · commercial_no_agreement · commercial_separate_agreement_enclosed | mismatch with claimant's class → registrar review | — |
| `counterclaim` | Counterclaim (commercial/B2B only) | table | N | head · amount | blocked for retail (premium refund set-off allowed as a defence note only) | — |
| `fraud_allegation` | Do you allege fraud? | enum | Y | no · yes_with_evidence_summary | yes → INS-SE-21 hold | — |
| `declaration_no_voucher_conflict` | No discharge voucher will be demanded inconsistent with any settlement | checkbox | Y | — | — | Protocol clause C-1 |

**Statement of defence (arbitration, commercial/B2B)** = F-INS-28 mirror: `admissions`, `denials[]` per claim head, `quantum_position` table, `documents_relied`, `counterclaim_heads[]`.

### 6.6 Vertical-specific forms

| ID | Form | Key fields (beyond INS-CORE) | Store |
|---|---|---|---|
| F-INS-04 | Policyholder grievance to insurer (representation) | `to_gro_email`, `subject`, `facts` (≤ 300 words), `why_decision_wrong` (per ground), `relief`, `documents_list`, `request_reasoned_reply_14d` (fixed text), Bima Bharosa registration steps | core (health facts as summary only; no diagnosis text unless user types it — then [S]) |
| F-INS-05 | Repudiation / short-settlement particulars | ground-by-ground table (ground, clause, answer, proving doc); four-tests grid (materiality, proximate cause, contra proferentem, fair dealing); delay block (docs completed, decision date, days elapsed) | core |
| F-INS-07 | Ombudsman complaint pack (self-help; party files) | six-condition panel (§4.6); centre; r.13 ground(s); facts; relief (amount ≤ cap note, interest, expenses); declarations (not pending; one office only; will attend) | core; [S] attachments sealed |
| F-INS-08 | Mis-selling particulars | `sold_by` (DD-INS-07), `seller_code`, `bank_branch`, `proposal_filled_by` (DD-INS-13), `signed_blank` (y/n), `promises_made[]` (DD-INS-18), `actual_product`, `premium_term`, `lock_in`, `docs_received_date`, `free_look_request_date`, `buyer_profile[]` (senior · low_income · low_literacy), `premiums_paid_total`, `policies_count`, `relief` (DD-INS-19) | core |
| F-INS-09 | Health claim schedule [S] | hospital, network (y/n), admit/discharge, diagnosis [S], procedure [S], room category entitled/used, rent/day, line items (head DD-INS-20, billed, allowed, reason, `hospital_differential_billing` yes/no/unknown), co-pay %, sub-limits, PED condition [S] + first-diagnosed date [S], cashless timestamps | `health_sealed` |
| F-INS-10 | Motor claim schedule | reg no., make/model/year, IDV, excesses, add-ons (DD-INS-21), incident type, DL valid for class, permit/fitness/PUC, head table (claimed/surveyor/paid), TL block (repair %, salvage, financier NOC), ground (DD-INS-22) | core |
| F-INS-11 | Life claim schedule | plan, issue/risk commencement/revival/rider dates, date of death, cause (summary; detail [S]), date called in question, grounds & materials communicated (y/n), non-disclosure table (fact, question, answer, material?, evidence), nominee/assignee/competing claimants | core + [S] |
| F-INS-12 | Commercial lines schedule (fire, marine, engineering, liability) | as INS-COM-EXT + peril, survey dates, quantum table, VaR/SI/average, BI block (GP rate, indemnity period, ICOW, savings), arbitration status | core |
| F-INS-21..26 | Life/ULIP servicing; marine & transit; liability (CGL/PI/D&O); crop & rural; government health scheme grievance; cyber & BI | per P08 FR-P08-50 | flag `ins_forms_f21_f26` OFF until legal review |
| F-INS-29 | **Cashless live escalation** (new) | `patient_admitted_at`, `hospital`, `network_hospital`, `preauth_submitted_at` (timestamp), `insurer_response_at`, `denial_or_query_text`, `query_count`, `discharge_bill_ready_at`, `discharge_auth_at`, `emergency` (y/n), `undertaking_demanded` (y/n) → computes TAT-02/03 breach minutes | core (timestamps) + [S] (clinical text) |
| F-INS-30 | **Moratorium / PED / waiting-period worksheet** (new) [S] | `first_inception_date`, `ported_from[]` (insurer, start, end, continuity confirmed), `policy_issue_regime` (pre_apr_2024 · post_apr_2024), `ped_waiting_months`, `specific_waiting_months`, `condition_alleged` [S], `diagnosis_date_alleged` [S], `nexus_with_claim` | `health_sealed` (outputs to core: months, crossed flags) |
| F-INS-31 | **Expert determination request** (new) | `ed_type` (surveyor_quantum · technical_cause · bi_forensic), `questions_for_expert[]` (fact/quantum only; coverage questions blocked), `expert_qualifications` (IRDAI licence category; forensic accountant ICAI), `binding` (non_binding default · binding_by_agreement · retail_binding_election), `site_visit_needed`, `fee_payer`, `ToR_draft` | core |
| F-INS-32 | **Retail binding-election for ED** (new) | disclosure acknowledgement (expert's role; non-appealable fact finding; Ombudsman/consumer rights preserved for issues outside the ED), e-sign by policyholder **after** expert disclosure | core |
| F-INS-33 | **Subrogation recovery claim** (new; B2B) | `subrogation_basis` (DD-INS-23), `insured_letter_of_subrogation` (file), `amount_paid_to_insured`, `payment_date`, `third_party_type` (carrier_road · railway · sea_carrier · port · warehouse · contractor · tortfeasor · at_fault_vehicle_insurer), `notice_of_claim_date`, `bill_of_lading_lr_awb`, `joint_with_insured` (y/n; required for consumer forum) | core |
| F-INS-34 | **Reinsurance / co-insurance dispute** (new; B2B) | `contract_type` (fac · treaty_prop · treaty_xol · retro · co_insurance), `treaty_ref`, `cedant`, `reinsurers[]` (share %), `follow_settlement_clause` (y/n), `claims_cooperation_clause` (y/n), `seat_and_law`, `foreign_party` (→ INT gates) | core |
| F-INS-35 | **Crop / scheme ladder pack** (new; signpost) | `ncip_application_id`, `season`, `crop`, `notified_area`, `loss_type` (DD-INS-24), `intimation_datetime`, `krph_docket_no`, `dgrc_status`, `bank_premium_debit_ref` | core; voice/IVR capture default |
| F-INS-36 | **Consultant-fee disclosure** (new) | `consultant_name`, `fee_type` (fixed · percentage · none), `percentage` (sealed from insurer; disclosed to neutral as "third-party fee interest exists" only) | core (restricted field) |
| F-INS-13 | Route & suitability triage record (never optional) | six conditions; clock table with owners; suitability; safeguards; signposting delivered; classifier + reviewer (must differ) | core |
| F-INS-14 / 15 / 16 / 17 / 18 / 19 / 20 | Agreement to mediate (authority section); neutral disclosure (5-year insurer relationships; 24-month counts; % income); settlement; discharge voucher; escrow milestones; non-commencement & signposting report (never optional); closure | per P08 FR-P08-50 | core |

### 6.7 Dropdown Master List (seeded as `core.form_option_lists`, versioned; EN + HI labels)

| List | Values (code → label) |
|---|---|
| **DD-INS-01 policy_class** | `retail` My family or me · `group_member` I'm a member of a group policy (employer/bank/society) · `group_master` The group contract itself · `commercial` My company or business · `government_scheme` Government scheme · `b2b_inter_insurer` Between insurance companies |
| **DD-INS-02 line_l1** | `health` · `motor` · `life` · `travel` · `property` · `rural` · `govt` · `com` · `mis` · `b2b` · `ed` |
| **DD-INS-03 subtype_l2** | all 59 L2 codes in §2.2 (filtered by L1) |
| **DD-INS-04 insurer_grounds** | the 20 L3 codes in §2.3 |
| **DD-INS-05 relief** | the 16 L4 codes in §2.3 |
| **DD-INS-06 line_of_business (L1-detail, 61)** | life: `term` `endowment` `money_back` `ulip` `annuity_pension` `group_life` `credit_life` `pmjjby` `child` `keyman` · health: `individual` `family_floater` `group_health` `senior_citizen` `top_up` `super_top_up` `critical_illness` `personal_accident` `hospital_cash` `opd` `pmjay_state` · motor: `private_car_od` `two_wheeler_od` `commercial_vehicle_od` `motor_tp` `standalone_od` · travel: `travel_domestic` `travel_international` `student_travel` · property: `bharat_griha_raksha` `householder` `bharat_sookshma` `bharat_laghu` `burglary` `shopkeeper` · rural: `pmfby` `rwbcis` `cattle` `farm_package` `micro` · commercial: `sfsp_iar` `business_interruption` `marine_cargo` `marine_hull` `car_ear` `machinery_breakdown` `eei` `cgl` `product_liability` `public_liability` `pi` `d_and_o` `cyber` `trade_credit` `surety` `fidelity` `employees_compensation` · b2b: `co_insurance` `reinsurance_fac` `reinsurance_treaty` `retrocession` |
| **DD-INS-07 intermediary_type / sold_by** | `agent` · `corporate_agent_bank` · `bank_rm` · `broker` · `web_aggregator` · `posp` · `telecaller` · `insurer_direct_online` · `insurance_marketing_firm` · `unknown` |
| **DD-INS-08 decision** | `repudiated` · `partially_settled` · `pending` · `cashless_denied` · `cashless_query_pending` · `closed_documents` · `no_decision` |
| **DD-INS-09 claimant_role** | `policyholder` · `insured_member` · `nominee` · `legal_heir` · `assignee` · `employer_group` · `hospital_cashless` · `insurer_subrogee` · `cedant` |
| **DD-INS-10 pending_forum** | `none` · `ombudsman` · `consumer_commission` · `civil_court` · `arbitration` · `mact` · `pmjay_grc` · `pmfby_dgrc_sgrc` · `pla` · `lok_adalat` · `irdai_bima_bharosa` (does not bar) |
| **DD-INS-11 used_claim_consultant** | `none` · `broker` · `claim_assistance_fixed_fee` · `claim_assistance_success_fee` · `advocate` · `family_friend` |
| **DD-INS-12 vulnerability** | `senior_65_plus` · `bereaved_90d` · `disability` · `serious_illness` · `low_literacy` · `language_support` · `financial_hardship` |
| **DD-INS-13 proposal_filled_by** | `self` · `agent` · `bank_staff` · `online_self` · `telecaller` · `unknown` |
| **DD-INS-14 arbitration_agreement_status** | `none` · `clause_in_policy_pre_circular` · `clause_in_policy_post_circular` · `separate_agreement` · `treaty_slip_clause` · `willing_to_agree_now` |
| **DD-INS-15 basis_of_indemnity** | `reinstatement` · `market_value` · `agreed_value` · `indemnity_depreciated` · `first_loss` |
| **DD-INS-16 claim_head (commercial/B2B)** | `material_damage` · `stock` · `business_interruption` · `icow` · `debris_removal` · `professional_fees` · `general_average` · `sue_and_labour` · `defence_costs` · `third_party_liability` · `ir_costs` · `ransom` · `contribution_share` · `reinsurance_recovery` · `subrogated_amount` · `interest` · `costs` |
| **DD-INS-17 non_production_reason** | `privileged_legal_advice` · `statutory_confidentiality` · `not_in_possession` · `third_party_document` · `will_produce_by_date` |
| **DD-INS-18 promises_made** | `fd_like_returns` · `single_premium_only` · `needed_for_loan_locker_account` · `guaranteed_returns_pct` · `bonus_refund_old_policy` · `no_lock_in` · `no_medicals_needed` · `ped_covered_day_one` · `fake_irdai_officer_call` · `other` |
| **DD-INS-19 mis_selling_relief** | `full_refund` · `refund_plus_interest` · `free_look_cancellation` · `paid_up_conversion` · `single_premium_conversion` · `waiver_future_premiums` · `product_substitution` · `cancel_linked_loan_product` · `compensation` |
| **DD-INS-20 health_bill_head** | `room_rent` · `nursing` · `icu` · `surgeon_fee` · `anaesthetist_fee` · `consultant_visits` · `ot_charges` · `implant_device` · `pharmacy_medicines` · `consumables` · `diagnostics_investigations` · `blood` · `physiotherapy` · `ambulance` · `pre_hospitalisation` · `post_hospitalisation` · `non_medical_items` · `package` · `other` (statutory no-proportionate set: `implant_device`, `pharmacy_medicines`, `consumables`, `diagnostics_investigations`, `icu`) |
| **DD-INS-21 motor_add_on** | `zero_depreciation` · `engine_protect` · `return_to_invoice` · `consumables` · `ncb_protect` · `roadside_assistance` · `key_replacement` · `tyre_protect` |
| **DD-INS-22 motor_ground** | `idv_low` · `depreciation` · `salvage_value` · `survey_delay` · `payment_delay` · `late_intimation` · `dl_invalid_or_class` · `use_beyond_permit` · `alcohol_alleged` · `fitness_puc` · `addon_not_honoured` · `cashless_refused` · `parts_not_damaged` · `pre_existing_damage` |
| **DD-INS-23 subrogation_basis** | `marine_s79` · `equitable_subrogation` · `letter_of_subrogation` · `subrogation_cum_assignment` · `contractual_indemnity` |
| **DD-INS-24 crop_loss_type** | `prevented_sowing` · `mid_season_adversity` · `localised_calamity` · `post_harvest` · `yield_based_cce` · `weather_trigger_basis_risk` · `enrolment_premium` |
| **DD-INS-25 suitability** | `suitable` · `suitable_with_safeguards` · `shuttle_only` · `not_suitable_forum` · `not_suitable_fraud` · `not_suitable_criminal` · `not_suitable_urgent` |
| **DD-INS-26 voucher_basis** | `full_final` · `under_protest` · `on_account` |
| **DD-INS-27 non_commencement_reason (F-INS-19)** | `no_response_14d` · `declined` · `applicant_withdrew` · `attended_not_settled` · `partial_settlement` · `not_suitable` · `terminated_by_neutral` · `authority_not_confirmed` |
| **DD-INS-28 neutral_background (allocation filter)** | `retired_insurer_officer` · `surveyor_loss_assessor` · `insurance_lawyer` · `consumer_side_advocate` · `financial_counsellor` · `former_ombudsman_staff` · `medical_professional` · `forensic_accountant` · `marine_engineer` |

---

## 7. Modus operandi per subtype

Proceeding machines are Appendix A §3 (mediation §3.3, conciliation §3.2, arbitration §3.5, expert determination §3.11, signposting §3.15). INS-specific sub-states (P08 §5): `under_scrutiny.signposting`, `under_scrutiny.triage_review`, `in_proceedings.claim_file_collection`, `in_proceedings.preparation`. SLAs below are Equator service clocks unless marked **(stat)**.

### 7.1 `ins.retail.v2` — base sequence (all retail/group-member claim L2s)

| Step | Actor | Action | SLA / clock | Documents | Notices | Decision point |
|---|---|---|---|---|---|---|
| R-1 | Party / AI Explorer | Explorer (§5); free-route panel; Schedule A delivered | first contact | — | `TPL-INS-N02 v2` (signposting event) | Signpost-only outcome? → T-closure via F-INS-19 |
| R-2 | Party | Register (KYC per App. S; DPDP consent; separate `health_data_consent`) | same day | ID; nominee/heir proof | consent receipts | — |
| R-3 | Party | File F-INS-02 (or F-INS-27 negotiation) | — | §9 mandatory set | filing receipt | Representation missing → R-3a |
| R-3a | Party (self-help) | Generate F-INS-04 representation; party sends it and registers on Bima Bharosa | `ins_insurer_reply_30d` (stat; conservative rule) | — | — | Negotiation may run in parallel |
| R-4 | Case manager + registrar | Triage F-INS-13: class (classifier ≠ reviewer), six conditions, clock table with owners, suitability, signposting recorded | `sla_scrutiny` 1 WD | — | triage summary to party | R3 guard on exit |
| R-5 | Case manager | Notice to insurer SPOC (`TPL-INS-N01`) + claim-file request | ≤ 3 WD from triage | — | notice (email + portal; speed post if no SPOC) | — |
| R-6 | Insurer | F-INS-06 response; produce claim file | `response_window` 14 d | wording at loss date; proposal; letters; survey/investigation/TPA reports | reminders D3/D7/D10 | Decline/no response → F-INS-19 (non-commencement, signposting with last dates) |
| R-7 | Case manager (+ neutral) | Preparation: Ground Schedule, line-item table, s.45 chain, survey rebuttal (calculators §12) | 3–5 WD | — | schedules shared with both sides | Authority confirmed? (INS-SE-24) |
| R-8 | Registrar | Appoint neutral (rotation; 40% insurer cap; F-INS-15 disclosure) | `sla_neutral_appointment` 3 WD | — | appointment notice; 3-WD objection window | Objection → replace once |
| R-9 | Neutral | Agreement to Mediate F-INS-14 signed (authority section, no recording, clocks not paused) | — | — | — | — |
| R-10 | Neutral | Sessions: joint → caucus → package (insurer grounds → policyholder answers per ground → line items → non-monetary levers) | first session ≤ 21 d from response; `med_contract_timebox` 45 d | — | T-48h/T-2h reminders (08:00–19:00) | Ombudsman T-60 reached? → blocking prompt (help to file F-INS-07; record) |
| R-11 | Neutral + parties | Settlement F-INS-16 drafted, read back in party's language, e-signed before session ends; e-stamped (NN-09) | same day | — | signed copies | R2 checks (422) |
| R-12 | Insurer | Pay direct to policyholder account (NN-13) or escrow (F-INS-18); voucher F-INS-17 basis recorded | per settlement (default 7 d) | UTR | payment confirmation | Miss → `escrow_milestone_miss` 2 WD notice |
| R-13 | Insurer | Non-monetary obligations: reinstatement with continuity; adverse-remark withdrawal (own + industry records) | `ins_adverse_remark_withdrawal` 15 d | written confirmation | — | Breach → return-to-mediation (C39) |
| R-14 | Case manager | Closure F-INS-20: compliance verified; health-data erasure scheduled; feedback ("felt pressured?") | ≤ 7 d from performance | evidence | closure notice | R3: every clock owned/closed; signposting recorded |
| R-X | Case manager | Not settled → F-INS-19 signposting report (each forum row with last date to act) | same day | — | report to party | — |

### 7.2 Deltas by subtype group

| Subtype group | Steps added / changed |
|---|---|
| `health.cashless_denial` (`ins.cashless_live.v1`) | C-1 F-INS-29 captured (timestamps) → C-2 escalation note to insurer GRO + TPA with TAT-02/03 breach minutes within **15 min** (service SLA) → C-3 hospital document request via hospital/TPA evidence portal (read-only, consent-scoped) → C-4 if still denied at discharge: under-protest guidance + reimbursement-preservation checklist → C-5 auto-spawn `health.reimbursement_deduction` case (linked) at discharge. No mediation session while admitted. |
| `health.reimbursement_deduction`, `health.ped_waiting`, `health.non_disclosure` | R-7 runs `ins.health_deductions@2` and `ins.moratorium_ped@1` inside `health_sealed`; neutral and assigned case manager access with step-up MFA only; insurer sees the same schedule (both sides equal access). |
| `health.tpa_conduct`, `health.portability_continuity` | TPA / previous insurer joined as co-respondent at R-5; relief is often non-monetary (continuity confirmation letter). |
| `motor.od_*`, `property.*` | R-6 must include the survey report; R-7 Survey Rebuttal Table; optional joint re-survey (both pay per Card INS-RET or insurer under protocol) or `ins.ed.v1` (non-binding for retail). Total loss: financier NOC milestone (FIN cross-link) and RC/keys/subrogation-letter handover as escrow conditions. |
| `motor.theft`, `property.burglary` | Gate before R-10: police final/untraced report uploaded (INS-SE-27). |
| `life.*` | R-7 s.45 chain (§12.7); bereavement safeguards; CN-INS-DEATH waiver; competing claimants → insurer as stakeholder, payment-direction terms only; heirship → FAM. |
| `travel.*` | R-7 FX schedule (§12.8); foreign documents: type copy + translation labelled "for convenience" (NN-32); assistance company joined as information source. |
| `mis.*` | R-6 adds sales-call recordings and benefit illustration; R-7 Mis-selling Ground Schedule (promise checklist v policy terms); bank/corporate agent joined; reliefs from DD-INS-19. |
| `rural.non_enrolment_bank` | Respondent = bank; voice/IVR vernacular default; KRPH docket recorded; RBI Ombudsman row in signposting. |
| `com.*` (`ins.commercial.v2`) | R-4 registrar classification; INS-COM-EXT authority (incl. reinsurer concurrence) before R-10; R-10 mediation **30 days** before any arbitration hearing; arbitration on quantum (liability admitted) under F-INS-28 → Appendix A §3.5 (PO1 ≤ 21 d of constitution; `arb_s29a`); ED for BI/technical questions. |
| `b2b.co_insurance`, `b2b.double_insurance` | Policyholder is paid first under any settlement; inter-insurer contribution resolved after (separate proceeding, linked). |
| `b2b.reinsurance_*` | INT gates for foreign parties; treaty seat respected; Equator offers India-seated arbitration or mediation only where agreed; claims-cooperation clause compliance checklist. |
| `b2b.subrogation_carrier`, `b2b.motor_recovery` | S-1 F-INS-33 with letter of subrogation and proof of payment to insured → S-2 notice-of-claim clock check (L-07) → S-3 invitation to carrier/insurer (corporate cadence D30) → S-4 mediation or documents-only arbitration (if agreed) → S-5 bulk docket for motor recovery (CSV/API intake, P09). |
| `ins.ed.v1` | E-1 F-INS-31 (fact/quantum questions only) → E-2 expert from panel (IRDAI-licensed surveyor in the right category; never the original surveyor or one who worked for the insurer in 24 months) with disclosure → E-3 ToR → `ed_submissions` 21 d → site visit (geotagged media) → draft `ed_comments` 14 d → determination (retail non-binding unless F-INS-32 election) → compliance tracking. |
| `ins.batched_day.v1` | B-1 insurer uploads ≤ 30 files + standing confidential settlement grid (insurer-only view; `TPL-INS-S02`) → B-2 policyholders invited with Schedule A; free to decline; fee ₹0 → B-3 one neutral, timed slots (online default) → B-4 settlements e-signed same day → B-5 compliance tracking; outcome MIS. Grid figures are never shown to policyholders or the neutral as a "recommendation". |
| `ins.signpost_only.v1` / `ins.scheme_signpost.v1` | SP-1 signposting script variant → SP-2 forum pack (MACT/DLSA, CGRMS, KRPH/DGRC) with last dates → SP-3 F-INS-19 report → close (fee ₹0; refunds 100% if anything was paid — RP-INS-RET "outside the Rules"). |

---

## 8. Pre-litigation journey (INS)

INS pre-litigation runs on the S4 §B5 `prelit_case` machine with these INS bindings. Mandatory s.12A PIMS does not apply to insurance claims by consumers; for **commercial** insurance disputes of specified value that are "commercial disputes" under the Commercial Courts Act 2015 s.2(1)(c)(xii) (insurance and re-insurance) [K], the COM PIMS-assistance pack (Form-1 to the Legal Services Authority) is offered and copy-lint blocks any claim that Equator's process satisfies s.12A (M-06; flag `com.s12a_equator_authorised` OFF).

| Stage | INS rule |
|---|---|
| Invite | Sender: "Equator Resolution Service Private Limited — Case Administrator" with verify-notice URL and QR. To the insurer **SPOC/GRO** (protocol) or registered office. Retail invitations from Equator to the policyholder (insurer-initiated cases) carry Schedule A first. Calls: **insurer-number mode (1600 series) default** for insurer-referred matters with written tenant authorisation; Equator DID only behind `voice.equator_service_number.enabled` (NN-12, M-05). Contact cap ≤ 6 pre-consent; 08:00–19:00. |
| Consent | Agreement to Mediate F-INS-14 (OTP/Aadhaar eSign for individuals; DSC or e-sign + authority letter for insurers). Sub-consents: online mode, no recording, language, interpreter, fee allocation. **No arbitration sub-consent is ever offered to a retail party** (R1). |
| Session | Insurer authority in writing before the first session (INS-SE-24); claim file on the table (non-production recorded, no adverse inference by the neutral); opening statement (verbatim): "What is said here cannot be used against you. Nothing here is an admission. Your rights and dates are on the sheet in front of you. I will not tell you who is right." |
| Settlement | F-INS-16 builder (§13); read back; e-signed and e-stamped by state of execution (NN-09). Pending complaint: joint request to the forum to dispose of it **"in terms of the settlement"** (not "withdrawn"). |
| Conversion | Retail: **contractual MSA only** (no consent award — R1); optional Lok Adalat recording pack (joint application to DLSA under LSA Act s.20) for a decree-status record; PLA recording where the PLA is seized. Commercial/B2B: s.73/74 conciliation settlement (if run as conciliation) or consent award (s.30) by a tribunal constituted under the separate arbitration agreement (arbitrator ≠ mediator by default, master §5.3). |
| Compliance | Payment direct or escrow; adverse-remark withdrawal in 15 days; reinstatement certificate; breach → 7-day cure → return-to-mediation (retail) or enforcement pack (commercial: award s.36; MSA: suit on contract; Lok Adalat award: execution as decree). |

---

## 9. Document checklists per subtype

Formats accepted for all uploads: PDF, JPG/PNG, HEIC, DOCX, XLSX, EML/MSG, MP3/M4A/WAV (call recordings), MP4 (≤ 200 MB). OCR and type copies are derived versions linked to the original (NN-32). [S] = sealed in `health_sealed`.

| Code | Document | L2 scope | M/O | Formats | Verification |
|---|---|---|---|---|---|
| D-INS-01 | Policy schedule + wording (as at loss date) + CIS | all | M | PDF/JPG | OCR policy no./dates vs INS-CORE; insurer to produce wording if missing (R-6) |
| D-INS-02 | Claim intimation acknowledgement | claim L2s | M | any | date vs `claim_intimation_date` |
| D-INS-03 | Insurer decision letter (repudiation / settlement / deduction sheet) | claim L2s | M (or "none received" declaration) | any | ground extraction (AI, human-confirmed) |
| D-INS-04 | Written representation + insurer reply (or proof of sending) | retail | M for Ombudsman pack | any; EML | dates feed C1–C3 |
| D-INS-05 | Bima Bharosa token screenshot | retail | O | JPG/PDF | token pattern |
| D-INS-06 | ID proof of claimant; nominee/heir relationship proof; legal-heir/succession certificate if claimant ≠ nominee | all; life | M | PDF/JPG | KYC per App. S (Aadhaar masked; OVSE) |
| D-INS-07 | Discharge summary, final bill with break-up, pharmacy bills, investigation reports, prescriptions [S] | health | M | PDF/JPG | sealed; line-item OCR into F-INS-09 |
| D-INS-08 | Pre-authorisation request, denial/query messages with timestamps [S] | cashless | M | any | timestamp extraction for TAT-02/03 |
| D-INS-09 | Previous policies / portability documents | health (continuity) | M if ported | PDF | continuity months |
| D-INS-10 | Proposal form copy (as filled) | non-disclosure, s.45, mis-selling | M (request from insurer if not held) | PDF | `proposal_filled_by`; signature comparison flag (human) |
| D-INS-11 | Hospital tariff showing room-category differential billing | reimbursement deduction | O (needed to contest doctor-fee proportionate deduction) | PDF/JPG | sets `hospital_differential_billing` |
| D-INS-12 | RC, DL, permit/fitness/PUC; FIR (theft/major); photos; garage estimate and final invoice; survey report | motor | M (survey report via insurer if not shared) | any | DL class vs vehicle; police final report for theft |
| D-INS-13 | Financier NOC / loan statement | motor TL; credit life | C | PDF | FIN cross-link |
| D-INS-14 | Death certificate; claim forms; medical attendant's certificate [S]; FIR/post-mortem (unnatural death) | life death | M | PDF/JPG | dates feed s.45 chain |
| D-INS-15 | Insurer's materials relied on for s.45 repudiation | life s.45 | M (insurer, R-6) | PDF | "materials communicated in writing" flag |
| D-INS-16 | Tickets/boarding passes, PIR, airline delay letter, foreign medical bills [S], assistance-company case number | travel | M per incident type | any | translation "for convenience" |
| D-INS-17 | Photos/videos of loss, fire-brigade report, stock registers, invoices, valuation basis | property, com.fire | M | any | geotag/time metadata preserved |
| D-INS-18 | Books of accounts, GP computation, CA certificate | BI | M | XLSX/PDF | forensic accountant (ED) |
| D-INS-19 | B/L, LR, AWB, survey (marine), packing list, GA bond | marine; subrogation | M | PDF | COGSA clock |
| D-INS-20 | Benefit illustration, sales-call recordings (request), bank RM communications, premium receipts, age/income proof of buyer | mis-selling | M (recordings via insurer) | PDF/MP3/EML | promise checklist |
| D-INS-21 | NCIP application ID, bank premium debit entry, land records, sowing certificate, loss intimation, KRPH docket | crop | M | any | voice capture allowed |
| D-INS-22 | Letter of subrogation, proof of payment to insured (UTR), notice of claim to carrier | subrogation | M | PDF | notice date vs L-07 clocks |
| D-INS-23 | Treaty/slip wording, bordereaux, cash-call correspondence | reinsurance | M | PDF/XLSX | foreign party → INT gates |
| D-INS-24 | Separate arbitration agreement / admission of liability | commercial arbitration | M | PDF | dates; signatory authority |
| D-INS-25 | Authority letter / board resolution for insurer officer; settlement authority limit | insurer respondent | M before session | PDF | `authority_limit_minor` |
| D-INS-26 | Consultant agreement (if any) | where used | O | PDF | F-INS-36 |

---

## 10. Practical difficulties and product solutions

| # | Difficulty (evidence) | Product solution | Owner phase |
|---|---|---|---|
| PD-01 | ~1 in 6 disposed Ombudsman health complaints non-entertainable (4,928 of 29,017 in FY25) — no representation, window missed, pending elsewhere [V2 S3 B0.2] | Eligibility engine v2 + representation-letter generator + owned clocks + T-60 blocking prompt | P08d |
| PD-02 | Deduction sheets are cryptic; proportionate deduction applied to excluded heads | Line-item analyser with statutory no-proportionate set and differential-billing evidence flag | P08d |
| PD-03 | Insurer queries used as stalling; hospital desk sends partial documents (ClaimBuddy lesson) | Cashless live escalation with timestamped breach note; hospital/TPA read-only evidence portal (consent-scoped, no referral fees) | P08d / P09 |
| PD-04 | Survey report not shared | R-6 mandatory production item; non-production recorded; joint re-survey / ED option | P08d |
| PD-05 | Proposal filled by agent; signature disputes | `proposal_filled_by` capture; signature-mismatch flag for human review (no AI forensic finding) | P08d |
| PD-06 | Insurer officer lacks authority; reinsurer/co-insurer approval delays | Authority confirmation before session (hard block); concurrence field with expected date | P08d |
| PD-07 | Discharge vouchers signed "full and final" under pressure | Under-protest endorsement template; voucher basis captured; *Boghara Polyfab* note in neutral brief | P08d |
| PD-08 | Success-fee shock from claim-help firms (9% model, 2020) for a free route | Free-route-first rendering; flat fees; consultant-fee disclosure; "the Ombudsman is free" copy | P08d / P13 |
| PD-09 | Fake IRDAI/Ombudsman officer refund scams | Scam banner; verify-notice page; Equator never asks for fees by phone; 1930 signposting | P07 / P08d |
| PD-10 | Bereaved nominees; low literacy farmers | Bereavement tone pack; voice/IVR vernacular; waivers; support person | P07 / P08d |
| PD-11 | Foreign-language travel bills; FX disputes | Type copy + translation "for convenience"; FX schedule at date-of-loss rate with source snapshot | P06 / P08d |
| PD-12 | Repeat-player capture risk (insurer funds many cases) | 40% concentration cap; rotation; F-INS-15 counts; funding-neutrality disclosure; quarterly anonymised outcome data | P03 / P08d |
| PD-13 | Co-insurance: follow insurers wait for lead | Lead/follow shares mandatory; both joined; settlement binds each per share | P08d |
| PD-14 | BI computations need forensic accounting | ED track with forensic accountant panel; BI calculator schedule | P08d |
| PD-15 | Subrogated claims lost on notice-of-claim technicalities | Notice clocks seeded at payment to insured; bulk docket for motor recovery | P08d / P09 |
| PD-16 | Claims above ₹50 lakh: Ombudsman award cap | Cap shown as advisory; Consumer tier by premium; PLA ₹1 crore | P08d |
| PD-17 | Pre-2024 policies under old moratorium/PED rules | `policy_issue_regime` parameter; transition rule flagged **[VERIFY — open (counsel): transition text not read 22 Oct 2026; dual computation meanwhile (see V4 health.ped_waiting)]** | P08d |
| PD-18 | Insurers fear "paying rejected claims" looks like admission | Without-prejudice framing; settlement states no admission; batched days | P09 |

---

## 11. Integrations and APIs

| Provider / system | Purpose | Data | Legal basis / permission | Mode | Fallback |
|---|---|---|---|---|---|
| IRDAI insurer and intermediary registers | Verify insurer, broker, surveyor licence | name, registration no., licence category | public data | scheduled scrape/manual import (config) | manual verification task |
| Bima Bharosa | Party's complaint token only | token, status (party-entered) | party consent; LR-IRDAI-012 (never file on behalf) | manual (party enters) | — |
| CIO / Ombudsman office directory | Centre lookup, addresses, F-INS-07 format | centre map | public | config table, six-monthly re-verify | manual |
| Insurer claims systems (protocol tenants) | Claim-file production, authority confirmation, settlement status | claim file items, authority, payment UTR | protocol contract; DPDP s.17(1)(a) for respondent data; party authority for health data | API (P09 insurer portal, `equator.ins.*` webhooks) / SFTP | portal upload by SPOC |
| TPAs and hospitals | Disputed-claim records | bills, pre-auth timestamps [S] | party's `health_authority_scope` (this dispute only) | read-only evidence portal (P09) / upload | party upload |
| Bima Sugam (IRDAI marketplace) | Policy/claim reference alignment | policy and claim IDs | — | watch-list; align entity model only **[VERIFY — open (vendor): no public API documentation retrievable 22 Oct 2026; no dependency — watch quarterly]** | — |
| e-Jagriti | Consumer filing deep link | none sent | — | link | — |
| NCIP / KRPH 14447 | Crop docket references | docket no. (party-entered) | — | manual | voice capture |
| PM-JAY CGRMS 14555 | Signpost only | none | — | link/phone | — |
| Leegality / Digio (`ESIGN_PORT`, `ESTAMP_PORT`) | Agreements, settlements, election forms | documents | IT Act s.3A; state stamp laws | API | alternate provider |
| Razorpay / RazorpayX Escrow+ / Castler (`PAYMENTS_PORT`, `ESCROW_PORT`) | Equator fees; escrow for milestone settlements | amounts, UTR | RBI PA Directions (15 Sep 2025); NN-13 | API | direct payment with proof |
| Sarvam / Bhashini (`TRANSLATION_PORT`, `DOC_AI_PORT`) | OCR, translation, type copies | documents ([S] processed in sealed enclave with no retention) | DPDP consent; processor contract | API | manual type copy |
| Exotel / Plivo + ElevenLabs/Sarvam voice (`TELEPHONY_PORT`, `VOICE_PORT`) | Reminders, slot booking; insurer-number (1600) mode | contact, schedule (no health data in calls) | TCCCPR as amended; NN-12; tenant authorisation | API | SMS/WhatsApp |
| FBIL / AD bank TT rates (`FX_PORT`) | Travel FX schedule | rate, timestamp, source | — | API | manual rate with source |
| Credit/industry databases (insurer-side) | Confirmation of adverse-remark withdrawal | confirmation letter only | settlement term | manual evidence upload | — |
| INT pack (`SANCTIONS_PORT`, KYC/UBO) | Foreign reinsurers, carriers | KYC/UBO | NN-19 | API | manual list check |
| Finbyx / Udofin (FIN cross-link) | Vehicle-loan NOC, credit-life assignee | loan status | lender tenant consent | API | upload |

**INS API surface (all `/v1`, OpenAPI 3.1, Idempotency-Key on POST):**

| Method & path | Purpose | Roles |
|---|---|---|
| GET `/v1/cases/{caseId}/ins/ombudsman-eligibility` | Engine v2 output (§4.6) | party, case_manager, registrar |
| POST `/v1/cases/{caseId}/ins/clocks/ins_ombudsman_1y/prompt` | Record T-60 prompt (body: channel, script_version, outcome `filed`/`declined`/`help_requested`) | case_manager |
| POST `/v1/cases/{caseId}/ins/representation-letters` | Generate F-INS-04 draft (party sends) | party |
| POST `/v1/cases/{caseId}/ins/ombudsman-packs` | Generate F-INS-07 self-help pack (₹0) | party |
| POST `/v1/cases/{caseId}/ins/cashless-escalations` | F-INS-29; returns breach minutes and note | party, case_manager |
| POST `/v1/cases/{caseId}/ins/triage` | F-INS-13 (403 `MAKER_CHECKER_SAME_USER` if classifier = reviewer; 422 retail arbitration) | case_manager, registrar |
| POST `/v1/cases/{caseId}/ins/authority-confirmations` | Insurer officer authority | insurer org user |
| POST/GET `/v1/cases/{caseId}/ins/ground-schedule` | Ground Schedule rows | parties, neutral |
| POST `/v1/cases/{caseId}/ins/health/deductions` | Health deduction lines (sealed service; returns aggregates only) | assigned case_manager/neutral (step-up), party |
| POST `/v1/cases/{caseId}/ins/survey-rebuttals` | Survey Rebuttal Table | parties |
| POST `/v1/cases/{caseId}/ins/expert-determinations` | F-INS-31 | parties, registrar |
| POST `/v1/cases/{caseId}/ins/expert-determinations/{edId}/binding-election` | F-INS-32 (retail; after disclosure) | policyholder |
| POST `/v1/cases/{caseId}/ins/vouchers` | F-INS-17 basis | insurer org user, policyholder |
| POST `/v1/cases/{caseId}/ins/signpost-report` | F-INS-19 (422 if any forum lacks `last_date_to_act`) | case_manager |
| POST `/v1/cases/{caseId}/ins/remark-withdrawals/{id}/evidence` | Adverse-remark withdrawal proof | insurer org user |
| POST `/v1/ins/batched-days` · POST `/v1/ins/batched-days/{id}/files` | Batched day + file upload (≤ 30) | enterprise_admin (insurer) |
| POST `/v1/ins/subrogation-dockets` | Bulk subrogation/motor-recovery intake (CSV/API) | enterprise_operator |
| POST `/v1/calculators/ins/{name}/runs` | Calculator runs (`calc:run` scope) | any (public runs store no PII) |
| GET `/v1/ins/reports/outcomes?quarter=YYYY-Qn` | Anonymised outcomes by insurer (n ≥ 20) | public (flag), institution_admin |

**Events (CloudEvents; Appendix F catalogue additions):** `equator.ins.eligibility.evaluated.v1` · `equator.ins.clock.prompted.v1` · `equator.ins.representation.generated.v1` · `equator.ins.cashless.escalated.v1` · `equator.ins.claim_file.requested.v1` · `equator.ins.claim_file.produced.v1` · `equator.ins.authority.confirmation_requested.v1` · `equator.ins.authority.confirmed.v1` · `equator.ins.settlement.agreed.v1` · `equator.ins.remark_withdrawal.due.v1` · `equator.ins.remark_withdrawal.confirmed.v1` · `equator.ins.ed.determination_issued.v1` · `equator.ins.batched_day.completed.v1` · `equator.ins.subrogation.docket_received.v1` · `equator.ins.signposting.report_issued.v1`. Payloads never carry health fields (only `health_data_token` presence boolean).

---

## 12. Calculators (indicative only; never advice — NN-01)

Framework per FR-P08-08: pure TypeScript in `packages/rules/calculators/ins/`, Zod inputs, parameters from the pinned ruleset, `indicative: true`, `computation_trace[]`, `disclaimer_key = 'ins.calc.disclaimer'` ("Computed from the facts and policy terms you entered. This is not legal advice, a valuation or a prediction of what any forum will decide."). Output labels never say "you will get", "fair value" or "recommended amount" (IN-G-04). Health calculators execute inside the `health_sealed` service and return only aggregates to core.

### 12.1 `ins.ombudsman_eligibility@2`
Inputs: `today`, `representation_date`, `insurer_reply_date`, `reply_outcome`, `amount_in_dispute_minor`, `pending_forum`, `is_retail`, `district_code`. Parameters: `ins.ombudsman.award_cap_minor` = 50,00,00,000; `ins.ombudsman.window` = `P1Y` (calendar); `ins.leap_day_rule` = `feb28`. Formulas: §4.6.

| Vector | Inputs | Expected |
|---|---|---|
| OE-01 | rep 20 Mar 2026; reply 2 Apr 2026 `rejected`; today 15 Oct 2026; ₹4,80,000; none | eligible; last_date_to_file **2 Apr 2027**; days_left 169 |
| OE-02 | rep 20 Mar 2026; no reply; today 25 Apr 2026 | reply_due_early 19 Apr 2026; reply_due_late 20 Apr 2026; C2 pass; last_date_to_file **19 Apr 2027** |
| OE-03 | rep 20 Mar 2026; no reply; today 19 Apr 2026 | C2 fail (`wait_until 2026-04-20`) |
| OE-04 | reply 1 Mar 2027 `rejected` | last_date_to_file **1 Mar 2028** (calendar year; a 365-day method would give 29 Feb 2028 — test asserts 1 Mar 2028) |
| OE-05 | as OE-01; today 10 Apr 2027 | eligible false; `condonation_needed` true; disclosure `ins.disc.condonation` |
| OE-06 | as OE-01; ₹62,00,000 | eligible true; `award_cap_exceeded` true; Consumer Commission row added |
| OE-07 | as OE-01; pending `consumer_commission` | `parallel_bar` true; eligible false |
| OE-08 | rep 20 Mar 2026; reply 10 Mar 2026 | 400 `VALIDATION_FAILED` (rule `ins.reply_before_representation`) |
| OE-09 | reply 29 Feb 2028 | last_date_to_file **28 Feb 2029** |
| OE-10 | `is_retail = false` (commercial) | Ombudsman not offered (`not_personal_line`) |

### 12.2 `ins.tat_breach@1` (TAT library §3.2) and `ins.delay_interest@2`
`interest = principal × (bank_rate + 2%) × days/365`, days from **intimation** to payment (LR-IRDAI-005); `bank_rate` read from config (5.75% w.e.f. 7 Oct 2026 → 7.75%).

| Vector | Inputs | Expected |
|---|---|---|
| TB-01 | Cashless pre-auth submitted 10:05, response 12:20 | 135 min; breach **75 min** (TAT 60) |
| TB-02 | Discharge bill ready 14:00, authorisation 18:30 | 270 min; breach **90 min** (TAT 180) |
| TB-03 | Health reimbursement submitted 5 Jan 2026, no investigation | due **20 Jan 2026** |
| TB-04 | Death claim ₹10,00,000 intimated 1 Jul 2026, no investigation, paid 30 Aug 2026 | due 16 Jul 2026; interest 60 days × 7.75% = **₹12,739.73** |
| TB-05 | P08 fixture: ₹6,00,000 × 8.5% × 48/365 | ₹6,706.85; current config 7.75% → **₹6,115.07** |
| TB-06 | GI survey report 3 Feb 2026 | decision due **10 Feb 2026** (7 days) |

### 12.3 `ins.health_deductions@2` (sealed) — supersedes the P08 v1 vector
Inputs: SI, eligible and charged room rent/day, days, co-pay %, line items (`head` DD-INS-20, `billed`, `allowed`, `reason_code`, `hospital_differential_billing` ∈ {yes, no, unknown}). `factor = eligible/charged`. Flags: **E1A** proportionate deduction on a statutory no-proportionate head (`implant_device`, `pharmacy_medicines`, `consumables`, `diagnostics_investigations`, `icu`); **E1B** proportionate deduction on another head where `hospital_differential_billing ≠ yes` (contestable subject to tariff evidence; `no` = flag, `unknown` = evidence request); **E2** PED/waiting disallowance where continuity months ≥ waiting months (from §12.4); **E3** co-pay applied before proportionate deduction or on a non-co-pay head; **E4** deduction without a reason code.

Golden vector HD-01 (eligible ₹5,000/day; charged ₹8,000/day; factor 0.625):

| Head | Billed | Allowed | Deducted | Reason | Flag |
|---|---|---|---|---|---|
| room_rent | 32,000 | 20,000 | 12,000 | room_rent_cap | — (lawful) |
| nursing | 18,000 | 11,250 | 6,750 | proportionate | — (varies with room) |
| surgeon_fee | 1,50,000 | 93,750 | 56,250 | proportionate | **E1B** (differential billing `unknown` → request tariff) |
| anaesthetist_fee | 45,000 | 28,125 | 16,875 | proportionate | **E1B** |
| implant_device | 1,65,000 | 1,03,125 | 61,875 | proportionate | **E1A** |
| diagnostics_investigations | 40,000 | 25,000 | 15,000 | proportionate | **E1A** |
| pharmacy_medicines | 38,000 | 28,000 | 10,000 | non_payable_items | check list (not proportionate) |
| consumables | 12,000 | 0 | 12,000 | non_payable_items | check list |
| **Total** | **5,00,000** | **3,09,250** | **1,90,750 (38.15%)** | | |

Expected outputs: E1A **₹76,875**; E1B **₹73,125** (evidence-dependent); recomputed per terms entered: ₹3,86,125 if E1A items are restored; ₹4,59,250 if E1A and E1B items are restored (both before co-pay). The P08 v1 vector treated surgeon and anaesthetist fees as categorically excluded from proportionate deduction; v2 treats them as evidence-dependent because the exclusion list covers pharmacy, consumables, implants/devices and diagnostics (and ICU), and deduction on other heads depends on whether the hospital bills them by room category (§18.2 C-03).

### 12.4 `ins.moratorium_ped@1` (sealed)
`continuity_months = completed calendar months from first_inception_date (incl. ported continuity) to admission_date`; `moratorium_crossed = continuity_months ≥ 60` (post-1 Apr 2024 regime; legacy regime parameterised); `ped_complete = continuity_months ≥ ped_waiting_months (≤ 36)`; `specific_complete = continuity_months ≥ specific_waiting_months (≤ 36)`.

| Vector | Inputs | Expected |
|---|---|---|
| MP-01 | first inception 1 Jun 2019 (ported 1 Jun 2022, continuity confirmed); admission 12 Mar 2026; PED 36 | 81 months; moratorium crossed; PED complete → E2 if PED disallowed; non-disclosure contest only for established fraud / permanent exclusion |
| MP-02 | first inception 1 Nov 2023; admission 15 Jun 2026; PED 36 | 31 months; PED not complete; no E2 |
| MP-03 | as MP-01 but continuity break of 45 days at porting (not confirmed) | continuity from 1 Jun 2022 → 45 months; moratorium not crossed; flag "continuity disputed — portability documents needed" |

### 12.5 `ins.motor@2`
`repair_pct = repair/IDV`; `ctl_candidate = repair_pct ≥ ctl_threshold (0.75, config)`; `repair_basis = repair − depreciation (0 if zero-dep) − compulsory_excess − voluntary_excess`; `tl_basis = IDV − salvage − compulsory_excess`; `nss_basis = base × nss_pct (0.75 config)` where breach without nexus is alleged. **No midpoint or "range" output** (v1 midpoint removed — NN-01 GX-3).

| Vector | Inputs | Expected |
|---|---|---|
| MO-01 | IDV ₹6,50,000; repair ₹4,10,000; dep ₹46,000; excess ₹2,000; salvage ₹92,000; breach alleged | repair 63.08% (not CTL); repair basis **₹3,62,000**; TL basis ₹5,56,000; NSS basis **₹2,71,500** |
| MO-02 | as MO-01; repair ₹5,10,000 | 78.46% → CTL candidate; TL basis **₹5,56,000** |
| MO-03 | as MO-01; zero-dep add-on | repair basis **₹4,08,000** |

### 12.6 `ins.underinsurance_bi@1` (P08 vector retained; verified)
SI ₹2,00,00,000; VaR ₹3,20,00,000 → adequacy 62.5%; gross ₹84,00,000 − depreciation ₹6,20,000 = net ₹77,80,000; average ₹29,17,500; deductible ₹2,50,000 → **₹46,12,500**. BI: turnover lost ₹2,40,00,000 × 32% = ₹76,80,000 + ICOW ₹18,00,000 − savings ₹4,00,000 = ₹90,80,000; BI SI ₹5,50,00,000 / annual GP ₹6,00,00,000 = 91.67% → **₹83,23,333**; interruption 5 ≤ indemnity 12 months ✓. Sensitivity grid on agreed VaR (−10% → ₹2,88,00,000: adequacy 69.44%; payable **₹51,52,778**).

(Check: net ₹77,80,000 × (1 − 0.694444) = ₹23,77,222 average; ₹77,80,000 − ₹23,77,222 − ₹2,50,000 = ₹51,52,778.)

### 12.7 `ins.s45_chain@1`
`chain_date = max(issue, risk_commencement, revival, rider_date)`; `window_end = chain_date + 3 calendar years`; `inside = called_in_question_date < window_end`.

| Vector | Inputs | Expected |
|---|---|---|
| S45-01 | issue = risk 10 Jan 2023; revival 5 Aug 2024; death 15 Jul 2025; repudiation 20 Oct 2025 | chain 5 Aug 2024; window end 5 Aug 2027; **inside** → only fraud / material suppression with grounds and materials in writing; check `materials_communicated` |
| S45-02 | issue = risk 1 Apr 2021; no revival; repudiation 2 Apr 2024 | window end 1 Apr 2024; **outside** → "cannot be called in question on any ground" (s.45(1)) |
| S45-03 | as S45-01; materials not communicated | inside; flag `s45_materials_not_communicated` |

### 12.8 `ins.travel_fx@1`
`inr = foreign_amount × rate(date_of_loss, source)` with FX snapshot (source, timestamp; FBIL for USD/GBP/EUR/JPY at 13:00 IST; other currencies via cross-rates — GLOBAL #14). Vector FX-01 (fixture rate, not a real quote): USD 3,200 × 86.50 = **₹2,76,800**; snapshot `{source:'FIXTURE', at:'2026-08-12T07:30Z'}`.

### 12.9 `ins.notice_clocks@1` (subrogation)
Road: `notice_by = booking_date + 180 days` (Carriage by Road Act 2007 s.16) [K]; Rail: `entrustment + 6 months` (Railways Act 1989 s.106) [K]; Sea: `suit_by = delivery_date + 1 year` (COGSA 2025). Vector NC-01: booking 5 Jan 2026 → road notice by **4 Jul 2026**; NC-02: entrustment 5 Jan 2026 → rail notice by **5 Jul 2026**; NC-03: delivery 10 Sep 2026 → sea suit by **10 Sep 2027**.

### 12.10 Fee estimator (reads Appendix B Card INS-RET; display GST-inclusive to consumers — NN-29)
FE-01: retail claim ₹3,20,000, no protocol: registration ₹1,500 (filer) + mediation ₹6,000 (`equal_split` → ₹3,000 each). Policyholder pays ₹4,500 + GST per Appendix B §B.4 (18% default → ₹810) = **₹5,310**. FE-02: claim ₹45,000 → CN-INS-SMALL → **₹0**. FE-03: death claim by nominee, ₹8,00,000 → registration waived (CN-INS-DEATH); mediation ₹15,000 split → policyholder ₹7,500 + GST. FE-04: insurer-referred under protocol → policyholder **₹0**. FE-05: any attempt to add a percentage-of-recovery line → 422 `FEE_CONTINGENCY_FORBIDDEN`.

---

## 13. Outputs, templates, enforcement and registration route

| Template | Purpose | Allowed legal label (copy-lint) | Enforcement / registration route |
|---|---|---|---|
| `TPL-INS-N01` | Notice / invitation to insurer | "Invitation to mediation under the Equator Insurance Mediation Rules" | — |
| `TPL-INS-N02 v2` (+ variants) | Schedule A signposting script | — | Signposting event (NN-20) |
| `TPL-INS-L01–L12` | Policyholder letters library (P08 FR-P08-52) | Party's own letter ("You send this") | — |
| `TPL-INS-L13` (new) | Demand for written reasons ("none given") | Party's own letter | — |
| `TPL-INS-L14` (new) | Cashless escalation note (timestamps, TAT breach) | "Request for urgent review" | — |
| `TPL-INS-L15` (new) | Hospital/TPA records request under party authority | — | — |
| `TPL-INS-R01` | F-INS-19 Non-commencement / signposting report | "Equator Mediation Closure Report" (no reasons, no conduct comments) | — |
| `TPL-INS-R03` (new) | Ombudsman self-help pack (F-INS-07 + chronology + index) | "Prepared by you with Equator's free tool. File it yourself." | Party files with the Ombudsman |
| `TPL-INS-R04` (new) | MACT/DLSA quantum-document brief (TP; documents only, no computation) | "Document checklist for your Tribunal claim" | MACT |
| `TPL-INS-S01` | Settlement agreement (retail) | "Mediated Settlement Agreement (contract) under the Equator Insurance Mediation Rules" | Suit on contract; optional Lok Adalat recording pack (LSA Act s.20) → award deemed decree (s.21); e-stamp per state of execution (NN-09); **no registration** needed (no immovable property) — NN-08 gate still evaluated |
| `TPL-INS-S01-COM` (new) | Settlement (commercial/B2B) | MSA (contract) or, if conciliation, "Settlement Agreement under section 73 … status of an arbitral award (section 74)" | s.36 A&C execution (s.74); consent award (s.30) where a separate arbitration agreement exists |
| `TPL-INS-S02` | Batched-day settlement grid annex (insurer-only, confidential) | "Insurer internal authority grid" — never shown to policyholder or used as a recommendation | — |
| `TPL-INS-S03` (new) | Non-monetary term library (B-1 reinstatement with continuity; B-2 adverse-remark withdrawal incl. industry databases within 15 days; B-3 product conversion; B-4 written correction; B-5 premium refund/waiver; B-6 pending complaint "disposed of in terms"; B-7 salvage/RC/keys/subrogation letter) | — | Compliance obligations tracked (P06) |
| `TPL-INS-S04` (new) | Under-protest discharge-voucher endorsement: "Received ₹__ on account and under protest. I reserve my right to claim the balance of ₹__." | — | F-INS-17 (`balance_reserved > 0`) |
| `TPL-INS-A01` (new) | Award skeleton (commercial/B2B quantum) | "Arbitral award" | s.31; stamping (NN-09); s.34 window; s.36 execution |
| `TPL-INS-E01` (new) | Expert determination | "Expert Determination (not an arbitral award)" | Contractual; retail non-binding unless election |
| `TPL-INS-R02` | Quarterly outcomes by insurer (anonymised; n ≥ 20 per insurer per quarter; methodology published; no health data) | — | Flag `ins.outcome_publication` (OFF until legal review) |

**Prohibited terms (settlement builder hard blocks, R2):** release of future claims or other policies; waiver of the Ombudsman, consumer or MACT remedy for matters outside the settlement; confidentiality that bars a regulatory complaint to IRDAI; "withdrawn" for pending complaints (must be "disposed of in terms"); any fee to Equator linked to the amount; arbitration clause in any retail instrument.

**Publication (NN-26):** health, life-death and PA settlements are never published in full; digest publication only with all-party consent and redaction profile `INS-HEALTH-MAX`.

---

## 14. Dashboards, KPIs and enterprise hooks

| KPI | Definition | Target | Widget |
|---|---|---|---|
| K-01 Signposting delivery | retail cases with recorded Schedule A before triage exit / retail cases | 100% (compliance) | compliance tile |
| K-02 Clock integrity | statutory clocks expired unprompted while open at Equator | 0 ("zero expired on our watch") | clock-risk board |
| K-03 Non-entertainable avoidance | Equator-prepared Ombudsman packs returned non-entertainable / packs filed (party-reported) | < 5% (benchmark 1 in 6) | trend |
| K-04 Claim-file production | insurer production within 14 days | ≥ 90% (protocol) | insurer protocol performance |
| K-05 Median time to settle | consent → signature | ≤ 45 days | — |
| K-06 Non-monetary outcomes | settlements with ≥ 1 `mediation_only_outcome` term / settlements | report | — |
| K-07 Compliance | settlements performed on time / settlements | ≥ 90% | compliance tracker |
| K-08 Remark withdrawal | confirmed within 15 days | ≥ 95% | — |
| K-09 Neutral concentration | max share of any neutral's INS appointments with one insurer (24 months) | ≤ 40% | concentration heatmap |
| K-10 "Felt pressured" | mean of F-INS-20 pressure item (1 = not at all) | ≤ 1.5 | — |
| K-11 Batched-day yield | files settled / files listed | report | batched-day yield |
| K-12 Cashless escalation SLA | escalation note within 15 min | ≥ 95% | — |
| K-13 Fee fairness | retail cases fully waived / retail cases | report | — |

KPIs are SQL views in `ins` over pinned data and exclude `health_sealed` (FR-P08-11). No KPI shows neutral win-rates, settlement rates per neutral or party-side tags (NN-16, NN-28). Enterprise hooks: insurer portal (P09) scoped to the insurer's matters; events in §11; MIS pack monthly (counts, TAT, compliance, no health fields).

---

## 15. Competitor notes and Equator differentiation

### 15.1 Competitor profiles (S3 Part C; tags as in S3)

| Dimension | ClaimBuddy | Insurance Samadhan | Policybazaar claim support | InsuranceDekho claim support |
|---|---|---|---|---|
| Form / licence | Private company (Delhi NCR), founded 2020; no IRDAI licence found [U] | Grievance-redressal company, founded 2018 [V2] | IRDAI-registered broker [K]; IRDAI ₹5 crore penalty, order 4 Aug 2025 (unsupported "Top/Best" labels, outsourcing payments, record-keeping, premium remittance) [V2] | IRDAI direct broker (licence no. 505 shown; entity naming inconsistent on page) [V] |
| Journey | Hospital-side claims digitisation + patient help; hospital desk liaison | Web form + call-back; company drafts "techno-legal" complaint, liaises with insurer, escalates to Ombudsman/consumer forum | In-house post-sale claims team; Claim Samadhaan Diwas (in-person settlement days with insurers); Claim Kavach (motor) | EDGE motor claim assistance (garage, cashless, pickup) |
| Fees | Not retrievable [U] | ₹999 registration incl. GST (after case acceptance) + **20% + GST success fee** on amount received (22% + GST at legal level); withdrawal 10% / 15% + GST [V] (insurancesamadhan.com, read 22 Oct 2026; entity Fastsurance Consultants Private Limited) | Free to customer (broker remuneration) [K] | Not stated [V] |
| Scale (self-reported) | 35,000+ patients; 250+ hospitals (Apr 2024) [V] | 20,000+ grievances / ₹220 crore+ since 2019 (Sep 2025) [V2] | 2,00,000+ customers assisted (Sep 2025) [V2] | 1,45,000+ claims served [V] |
| Regulatory exposure | Possible "insurance consultant"/intermediary question under s.2(10B)/s.42D (unsettled; s.105BA penalty) [U] | Same; plus practice-of-law question for paid legal drafting (*BCI v A.K. Balaji*) [U] | Advertising/conduct exposure demonstrated by the 2025 order | Disclaimers shift garage delay risk to customer |

**Legality of success fees (analysis for counsel, S3 C5).** A non-lawyer's percentage fee is not void per se in India unless extortionate or unconscionable (*Ram Coomar Coondoo v Chunder Canto Mookerjee* (1876) PC; *BCI v A.K. Balaji* (2018)) [K]; advocates are barred from contingency fees (BCI Rules Part VI Ch. II Section II r.20) [V]. The open questions are (i) whether a post-sale claim-assistance firm is an "insurance consultant" or a notified "insurance intermediary" needing registration (s.2(10B), s.42D(2); penalty s.105BA) and (ii) whether a percentage fee for a claim the Ombudsman handles free is an unfair contract term (CPA 2019 s.2(46)). **Equator position (binding):** Equator is a neutral institution and charges **no success fee in any INS matter** (NN-18, X-07, Equator Insurance Rules r.27), does not act as the policyholder's representative before the Ombudsman (PI-INS-08), and offers the Ombudsman pack as free self-help. Any human-assisted "Claim Prep" service stays behind flag `ins.claim_prep_assisted` (OFF) until counsel answers OLQ-1–OLQ-3 (§18).

### 15.2 Differentiation (what Equator ships that competitors do not)

| # | Equator capability | ClaimBuddy | Insurance Samadhan | Policybazaar / InsuranceDekho | Ombudsman (free state forum) |
|---|---|---|---|---|---|
| X-1 | **Free routes first**: Ombudsman/PLA/Consumer panel with computed last dates before any fee | No | Escalates to Ombudsman as part of a paid service | Within broker relationship | Is the free route |
| X-2 | **Eligibility engine v2** (six conditions; condonation; parallel bar; cap) + owned clocks + T-60 blocking prompt | No | Manual | No | Decides eligibility itself |
| X-3 | **Flat, published, slabbed fees; automatic waivers; ₹0 when insurer-referred** | [U] | % of recovery | Free (broker-funded; sales relationship) | Free |
| X-4 | **Neutral institution**: independent mediator, 40% concentration cap, disclosure, no insurer-chosen neutrals | Claimant-side | Claimant-side | Seller-side | Statutory, quasi-judicial |
| X-5 | **Non-monetary outcomes** (continuity, remark withdrawal, conversion) in an enforceable instrument | — | Occasionally via negotiation | — | Not ordinarily (award is money) |
| X-6 | **Line-item, s.45, moratorium, motor, BI calculators** with traceable computation, equal access for both sides | — | Internal "techno-legal" drafting | — | — |
| X-7 | **Cashless live escalation** with TAT breach timestamps; hospital/TPA evidence portal | Hospital-desk model (closest) | — | On-ground teams | — |
| X-8 | **Sealed health data** (separate store, keys, no analytics/AI) | [U] | [U] | [U] | — |
| X-9 | **Insurer B2B**: protocol, batched days with confidential grid, quantum arbitration, surveyor ED, subrogation dockets, reinsurance mediation | — | — | Settlement days (closest benchmark) | — |
| X-10 | **Truth-in-marketing**: no "Top/Best" or settlement-ratio claims without basis (NN-17; IRDAI–Policybazaar lesson) | — | — | Penalised for labels | — |

**Partner stance.** Equator does not pay or accept referral fees from insurers, hospitals, TPAs or claim-assistance firms for steering cases (PI-CMP-04). Claim-assistance firms may file for their clients only as disclosed representatives under an e-signed Letter of Authority (NN-27); the consultant-fee disclosure (F-INS-36) applies.

---

## 16. Data-model extensions

Schemas: `ins` (tenant RLS + case RLS, FR-P08-12) and `health_sealed` (role `eq_health` only; `ai_svc` has no grant; opaque token; no FK). Canonical names extend Appendix F `ins.policies`, `ins.claims` and P08 `ins.case_ext`, `ins.triage_records`, `ins.settlement_ext`, `ins.vouchers`.

### 16.1 Enums

```sql
CREATE TYPE ins.policy_class AS ENUM ('retail','group_member','group_master','commercial','government_scheme','b2b_inter_insurer');
CREATE TYPE ins.l1 AS ENUM ('health','motor','life','travel','property','rural','govt','com','mis','b2b','ed');
CREATE TYPE ins.suitability AS ENUM ('suitable','suitable_with_safeguards','shuttle_only','not_suitable_forum','not_suitable_fraud','not_suitable_criminal','not_suitable_urgent');
CREATE TYPE ins.eligibility_state AS ENUM ('eligible','write_first','wait_reply','condonation_needed','parallel_bar','not_personal_line');
CREATE TYPE ins.ed_binding AS ENUM ('non_binding','binding_by_agreement','retail_binding_election');
CREATE TYPE ins.voucher_basis AS ENUM ('full_final','under_protest','on_account');
-- policy_class on ins.policies (Appendix F) is migrated from text CHECK to this enum; values 'government_scheme','b2b_inter_insurer' added.
```

### 16.2 New tables (key columns and constraints)

| Table | Key columns | Constraints / notes |
|---|---|---|
| `ins.eligibility_runs` | id, case_id, tenant_id, run_at, c1..c6 bool, state `ins.eligibility_state`, reply_due_early, reply_due_late, last_date_to_file, award_cap_exceeded, config_version, trace jsonb | immutable (append-only); latest pointer on `ins.case_ext` |
| `ins.signposting_scripts` | id, variant, version, language, text_hash, approved_by, effective_from | maker–checker; legal review required (NN-23) |
| `ins.cashless_escalations` | id, case_id, preauth_submitted_at, insurer_response_at, discharge_bill_at, discharge_auth_at, preauth_breach_min GENERATED, discharge_breach_min GENERATED, note_document_id, spawned_case_id | breach_min = greatest(0, minutes − TAT) |
| `ins.ground_schedule_rows` | id, case_id, seq, ground `text` (DD-INS-04), clause_ref, policyholder_answer, proof_document_id, materiality, proximate_cause, contra_proferentem, fair_dealing | UNIQUE (case_id, seq) |
| `ins.deduction_lines` | id, case_id, head, billed_minor, allowed_minor, deducted_minor GENERATED, reason_code, flag | motor/commercial only; CHECK allowed ≤ billed; CHECK reason_code IS NOT NULL OR billed = allowed |
| `health_sealed.deduction_lines` | id, case_token_ref, head, billed_minor, allowed_minor, reason_code, hospital_differential_billing, flag | same CHECKs; no FK |
| `health_sealed.continuity_worksheets` | id, case_token_ref, first_inception_date, ported_from jsonb, regime, ped_months, specific_months, condition_enc, diagnosis_date_enc | — |
| `ins.authority_confirmations` | id, case_id, insurer_org_id, officer_signatory_id, authority_limit_minor, approver_name, turnaround_hours, concurrence_needed, confirmed_at, evidence_document_id | session insert trigger requires a row with confirmed_at (`INS_AUTHORITY_UNCONFIRMED`) |
| `ins.survey_reports` | id, case_id, surveyor_name, irdai_licence_no, category, report_date, assessed_minor, shared_with_insured bool | — |
| `ins.expert_determinations` | id, case_id, proceeding_id, ed_type, binding `ins.ed_binding`, expert_neutral_id, questions jsonb, election_esign_id | CHECK `NOT (is_retail AND binding = 'binding_by_agreement')`; CHECK `binding <> 'retail_binding_election' OR election_esign_id IS NOT NULL` |
| `ins.mis_selling_particulars` | id, case_id, sold_by, seller_code, proposal_filled_by, promises text[], docs_received_date, free_look_request_date, policies_count | — |
| `ins.s45_chains` | id, case_id, issue_date, risk_commencement_date, revival_date, rider_date, chain_date GENERATED, window_end, called_in_question_date, inside bool GENERATED, materials_communicated | — |
| `ins.b2b_matters` | id, case_id, contract_type, treaty_ref, cedant_org_id, shares jsonb, follow_settlements bool, claims_cooperation bool, seat, governing_law, intl_case_id | CHECK shares sum = 1.0 |
| `ins.subrogation_claims` | id, case_id, basis, amount_paid_to_insured_minor, paid_on, third_party_type, notice_of_claim_on, booking_or_delivery_on, joint_with_insured bool | clocks seeded on insert |
| `ins.batched_days` / `ins.batched_day_files` | id, tenant_id, insurer_org_id, date, neutral_id, grid_document_id (insurer-only ACL), file_case_ids uuid[] | CHECK cardinality(file_case_ids) ≤ 30 |
| `ins.remark_withdrawals` | id, case_id, settlement_id, due_on, confirmed_on, evidence_document_id, databases text[] | clock `ins_adverse_remark_withdrawal` |
| `ins.consultant_disclosures` | id, case_id, consultant_name, fee_type, percentage numeric(5,2) (column ACL: neutral sees `fee_type <> 'none'` only) | — |
| `ins.calc_runs` | id, case_id, calculator, version, inputs_hash, outputs jsonb (no health fields), trace jsonb | sealed calculators write only aggregates |

### 16.3 Critical DDL

```sql
-- R1 backstop (extends P08): no arbitration-family proceeding on a retail INS case
CREATE OR REPLACE FUNCTION ins.guard_retail_arbitration() RETURNS trigger AS $$
BEGIN
  IF NEW.mechanism IN ('arbitration','emergency_arbitration','med_arb','arb_med','arb_med_arb')
     AND EXISTS (SELECT 1 FROM ins.policies p WHERE p.case_id = NEW.case_id AND p.is_retail) THEN
    RAISE EXCEPTION 'INS_RETAIL_ARBITRATION_BLOCKED' USING ERRCODE = 'check_violation';
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_ins_retail_arb BEFORE INSERT OR UPDATE OF mechanism ON core.proceedings
  FOR EACH ROW EXECUTE FUNCTION ins.guard_retail_arbitration();  -- core.proceedings has no vertical column; the ins.policies join scopes the guard to INS

-- R4 backstop: no outcome-linked fee item on an INS schedule (basis/outcome_linked live on core.tariff_items, vertical on core.fee_schedules)
CREATE OR REPLACE FUNCTION ins.guard_no_contingency() RETURNS trigger AS $$
BEGIN
  IF (NEW.outcome_linked OR (NEW.basis = 'PCT_OF_AMOUNT' AND NEW.rule->>'on' ~ '^(settlement|award|outcome)\.'))
     AND EXISTS (SELECT 1 FROM core.fee_schedules s WHERE s.id = NEW.schedule_id AND s.vertical = 'INS') THEN
    RAISE EXCEPTION 'FEE_CONTINGENCY_FORBIDDEN' USING ERRCODE = 'check_violation';
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;
CREATE TRIGGER trg_ins_no_contingency BEFORE INSERT OR UPDATE ON core.tariff_items
  FOR EACH ROW EXECUTE FUNCTION ins.guard_no_contingency();
-- cross-vertical schedules (vertical IS NULL): fee engine rejects outcome-linked items on INS quotes (HB, FEE_CONTINGENCY_FORBIDDEN)
```
**[Corrected 22 Oct 2026 against Appendix F §4 and P05 `core.tariff_items`: vertical is on `core.cases`/`core.fee_schedules`; basis and `outcome_linked` are on `core.tariff_items`]**

### 16.4 RLS and access
All `ins.*` tables: `USING (tenant_id = current_setting('app.tenant_id')::uuid AND core.is_case_member(case_id))`. Insurer org users see only their insurer's cases (`case_parties.org_id`). `TPL-INS-S02` grid documents: ACL = insurer org + registrar. `health_sealed.*`: `eq_health` role; access requires case assignment + step-up MFA + purpose; every read → `audit.access_log`; monthly DPO review.

### 16.5 Config keys and feature flags

| Key / flag | Default | Notes |
|---|---|---|
| `ins.ombudsman.award_cap_minor` | 50,00,00,000 | r.17(3) proviso (ii) |
| `ins.ombudsman.window` | `P1Y` calendar | r.14(3)(b); GCA s.3(66) |
| `ins.leap_day_rule` | `feb28` | **[Product decision 22 Oct 2026: feb28 (conservative); INS-Q-06 closed]** |
| `ins.concentration_cap` | 0.40 | tenants may only lower |
| `ins.ed.cooling_off_months` | 24 | surveyor conflict |
| `ins.cashless.escalation_sla_min` | 15 | service SLA |
| `ins.tat.*` | §3.2 values | LR-IRDAI-005 |
| `ins.retail_conciliation` | OFF | Q-C9 |
| `ins.claim_prep_assisted` | OFF | OLQ-1–3 |
| `ins.outcome_publication` | OFF | legal review of per-insurer publication |
| `ins.mact_delay_note` | OFF | Ayiti Navaneetha verification |
| `ins_forms_f21_f26` | OFF | legal review |
| `ins_internal_ombudsman` | OFF | draft guidelines |
| `ins.pla_signpost` | ON | LSA s.22A(b) |

### 16.6 New legal-rule rows (Appendix G additions, status per tag)
`LR-INS-LIM-44` (Limitation Act Art. 44; [K] → `VERIFY_PENDING` until re-fetched) · `LR-LSA-PLA` (LSA Act ss.22A–22E; PLA ₹1 crore; IN_FORCE) · `LR-LSA-LA` (LSA s.20–21) · `LR-INS-COGSA` (COGSA 2025, one-year bar; IN_FORCE) · `LR-INS-CBR16` (Carriage by Road Act s.16) · `LR-INS-RLY106` (Railways Act s.106) · `LR-INS-HEALTH-MC-2024` (moratorium/PED/proportionate deduction; `VERIFY_PENDING` paragraph refs — non-permissive, so calculators run with "verify" banner) · `LR-INS-S64UM` (surveyor licensing; threshold VERIFY) · `LR-INS-CCA-2-1-C-XII` (commercial dispute definition incl. insurance/reinsurance).

---

## 17. Acceptance tests (Gherkin; `tests/acceptance/ins/`)

```gherkin
Feature: INS vertical pack v2

Scenario: NN-06_ins_R1_retail_arbitration_blocked_api_and_db
  Given an INS case with policy_class "group_member"
  When the case manager requests an arbitration proceeding
  Then the API returns 422 with code "INS_RETAIL_ARBITRATION_BLOCKED" and rule "INS-R1"
  And a direct INSERT into core.proceedings with mechanism "med_arb" for that case fails with check_violation
  And form F-INS-28 is not renderable for the case

Scenario: INS_R1_no_consent_award_conversion_for_retail
  Given a retail INS mediation that has settled
  When a user selects output conversion "CONSENT_AWARD_S30"
  Then the option is absent from the conversion list
  And only "MSA_CONTRACT" and "LOK_ADALAT_RECORDING_PACK" are offered

Scenario: INS_commercial_quantum_arbitration_requires_admitted_liability
  Given an INS case with policy_class "commercial" and arbitration_agreement_status "separate_agreement"
  And liability_admitted is "no"
  When arbitration with scope "quantum_only" is requested
  Then the API returns 422 with rule "INS_ARB_LIABILITY_NOT_ADMITTED"
  And mediation and expert determination remain offered

Scenario: NN-20_ins_R3_triage_exit_blocked_without_signposting
  Given a retail INS case in under_scrutiny with no recorded signposting event
  When triage is completed
  Then the API returns 409 "SIGNPOSTING_REQUIRED" with rule "INS-R3"

Scenario: NN-04_ins_R3_closure_blocked_with_unowned_clock
  Given an INS case whose ins_ombudsman_1y clock has no owner
  When closure is requested
  Then the API returns 409 "CLOCK_UNOWNED"

Scenario: NN-04_ins_t60_blocking_prompt
  Given ins_ombudsman_1y expires in 59 days and the case is in_proceedings
  When the case manager attempts to schedule a session
  Then the action is blocked until POST /v1/cases/{caseId}/ins/clocks/ins_ombudsman_1y/prompt is recorded
  And event "equator.ins.clock.prompted.v1" is emitted

Scenario Outline: INS_ombudsman_engine_v2_golden_vectors
  Given the eligibility inputs of vector <vector>
  When GET /v1/cases/{caseId}/ins/ombudsman-eligibility is called
  Then state is <state> and last_date_to_file is <last_date>
  Examples:
    | vector | state              | last_date  |
    | OE-01  | eligible           | 2027-04-02 |
    | OE-02  | eligible           | 2027-04-19 |
    | OE-04  | eligible           | 2028-03-01 |
    | OE-05  | condonation_needed | 2027-04-02 |
    | OE-07  | parallel_bar       | 2027-04-02 |
    | OE-09  | eligible           | 2029-02-28 |

Scenario: LR-IRDAI-013_late_complaint_is_never_ineligible
  Given the one-year window closed 10 days ago
  When the Explorer renders the outcome
  Then the text contains "may still admit your complaint if it condones the delay"
  And the word "ineligible" does not appear

Scenario: LR-IRDAI-008_R2_waiver_rejected
  When a settlement containing a release of future claims under other policies is submitted
  Then the API returns 422 "STATUTORY_WAIVER_FORBIDDEN" with rule "INS-R2"

Scenario: INS_R2_under_protest_requires_balance
  When a discharge voucher with basis "under_protest" and balance_reserved_minor 0 is submitted
  Then the API returns 422 and the DB CHECK on ins.vouchers rejects a direct insert

Scenario: NN-18_ins_no_success_fee
  Given an INS retail quote request
  When a tariff item with outcome_linked = true (or basis "PCT_OF_AMOUNT" on settlement.*) is added
  Then the fee engine returns 422 "FEE_CONTINGENCY_FORBIDDEN"
  And trigger trg_ins_no_contingency rejects a direct insert

Scenario: D2-18_free_routes_rendered_before_fee
  Given a retail health case where the Ombudsman engine returns eligible
  When the outcome page renders
  Then the first panel lists "Insurance Ombudsman — free" with the last date to file
  And the Equator fee quote appears only after the free-route panel
  And the quote shows the total including GST

Scenario: NN-07_ins_health_data_sealed
  Given a discharge summary uploaded to an INS case
  Then the document is stored in health_sealed with a token and no FK to core
  And GET /v1/cases/{caseId}/documents does not list it for an unassigned case manager
  And no row referencing the token appears in any analytics view, OpenSearch index or AI prompt log
  And the ai_svc database role has no privilege on schema health_sealed

Scenario: NN-07_ins_health_not_in_notifications
  When any INS notification template containing a health field in the subject or preview is submitted for activation
  Then template lint blocks activation

Scenario: NN-24_ins_criminal_exclusion
  Given an intake where the user states a police case alleges the claimant staged the accident
  When the routing rule pack is evaluated
  Then the outcome is "reject" for mediation of the fraud question with HX-INS-01 and HX-INS-02
  And the signposting table lists the police/court and the Ombudsman with last dates

Scenario: INS_scam_call_signposted_to_1930
  Given INS-Q00 answer "Someone called asking for a fee/refund"
  Then the Explorer shows the 1930 helpline and cybercrime.gov.in
  And no Equator fee screen is shown

Scenario: INS_TP_motor_signpost_only
  Given INS-M01 answer "Yes"
  Then the outcome is OUT_MACT with the 6-month date
  And no Equator mediation, arbitration or fee is offered
  And the case closes via F-INS-19 with fee 0

Scenario: INS_cashless_live_no_session_while_admitted
  Given a cashless_denial case with patient_admitted true
  When a mediation session is scheduled
  Then the API returns 409 and the "Do not delay treatment" banner is shown
  And an escalation note with breach minutes is generated within 15 minutes

Scenario: INS_session_without_insurer_authority_blocked
  Given no ins.authority_confirmations row with confirmed_at for the insurer
  When a session is created
  Then the API returns 409 "INS_AUTHORITY_UNCONFIRMED"

Scenario: INS_neutral_concentration_cap
  Given neutral N has 8 of 18 INS appointments in 24 months with insurer X
  When the allocation engine proposes N for a new insurer X case
  Then N is excluded with reason "INS_NEUTRAL_CONCENTRATION"

Scenario: INS_ED_retail_binding_requires_post_disclosure_election
  Given a retail motor OD case with an expert determination
  When binding is set to "binding_by_agreement"
  Then the DB CHECK rejects it
  And binding "retail_binding_election" is accepted only with an e-signed F-INS-32 dated after the expert's disclosure

Scenario: INS_ED_original_surveyor_conflict
  Given the proposed expert surveyed the same loss for the insurer
  Then appointment fails with "CONFLICT_DETECTED" rule "INS-ED-CONFLICT"

Scenario: NN-01_ins_no_valuation
  When a user asks the assistant "₹1.1 lakh is offered, is that fair?"
  Then the assistant refuses with guardrail IN-G-04 and offers the line-item schedule
  And the motor calculator output contains no midpoint or recommended amount

Scenario: NN-02_ins_deterministic_parity
  Given the LLM is disabled
  When the same 20 INS intakes are completed via the questionnaire in English and Hindi
  Then routes, blocked routes and clock dates equal those of the AI-assisted runs

Scenario: INS_health_deductions_v2_vector
  Given vector HD-01
  When ins.health_deductions@2 runs
  Then E1A equals 7687500 paise and E1B equals 7312500 paise
  And core receives only aggregate amounts and flag counts

Scenario: NN-26_ins_no_publication_of_health_settlement
  Given a settled health case where all parties consented to publication
  Then only a redacted digest under profile INS-HEALTH-MAX can be published

Scenario: NN-12_ins_insurer_number_mode
  Given an insurer-referred INS case with tenant 1600-series authorisation on file
  When the voice agent places a reminder call at 19:30 IST
  Then the call is blocked as outside 08:00–19:00
  And a call at 10:00 presents the insurer's 1600-series number and discloses AI and recording
Scenario: v3.1_INS_waiting_for_insurer_reply_is_routed
  Given a retail policyholder wrote to the insurer on 20 Mar 2026 and today is 5 Apr 2026 with no reply
  When triage runs
  Then rule INS-SE-07a applies with mediation offered now
  And the Ombudsman is shown as available from 20 Apr 2026 with last date 19 Apr 2027
  And the case sub-state is awaiting_insurer_reply with a diary reminder on 20 Apr 2026
```

---

## 18. Open items and counsel questions

### 18.1 Counsel questions (INS)

| # | Question | Blocks |
|---|---|---|
| OLQ-1 | Is a post-sale claim-assistance service (Equator "Claim Prep" or partners) an "insurance consultant" or other "insurance intermediary" under Insurance Act s.2(10B) as amended, requiring s.42D registration? Any IRDAI notification under the residual clause? | `ins.claim_prep_assisted` |
| OLQ-2 | Does preparing Ombudsman complaints or representations for a flat fee by non-advocate staff amount to the practice of law (*A.K. Balaji*; Advocates Act s.33)? Is an advocate-supervised model needed? (02 §5 Q10) | Card INS-RET line I7 |
| OLQ-3 | Can a neutral institution also offer a claimant-side preparation service without breaching impartiality (A&C Fifth/Seventh Schedules)? Conflict-wall design | same |
| Q-C9 | Does a pending Equator Part III conciliation count as "pending before … arbitrator" for Ombudsman r.14(5), or make RB-IOS complaints non-maintainable? | `ins.retail_conciliation` |
| OLQ-8 | Date, bench and text of the SC order in *ICICI Lombard v Ayiti Navaneetha* on MV Act s.166(3); can Equator facilitate TP quantum talks outside the MACT/Lok Adalat at all? | `ins.mact_delay_note`; `TPL-INS-R04` copy |
| OLQ-9 | Health Master Circular 2024 reference number and paragraphs (moratorium, PED/specific waiting, proportionate-deduction exclusions, claims review committee); transition rules for pre-1 Apr 2024 policies | `LR-INS-HEALTH-MC-2024` |
| OLQ-13 | Karnataka HC (1 Jul 2026) on advocates before the Ombudsman — appeal or contrary HC views? | PI-INS-08 copy |
| INS-Q-01 | Enforceability of 12-month policy suit-bar clauses after Contract Act s.28 (1997 amendment) | `ins_policy_suit_bar` label |
| INS-Q-02 | Ombudsman territorial jurisdiction rule after the 2021 amendment (complainant residence vs insurer branch) | centre map |
| INS-Q-03 | Consumer pecuniary tier for insurance claims: "consideration paid" = premium? | J-04 |
| INS-Q-04 | Ombudsman jurisdiction over PMJJBY/PMSBY claims administered through banks | `govt.pmjjby_pmsby` routing |
| INS-Q-05 | Per-insurer quarterly outcome publication: confidentiality under the Agreement to Mediate, defamation exposure, n-threshold | `ins.outcome_publication` |
| INS-Q-06 | Leap-day computation of the one-year window (29 Feb trigger) | `ins.leap_day_rule` |
| INS-Q-07 | Current s.64UM(2) surveyor threshold and the proviso allowing settlement at a figure different from the surveyor's assessment; status of the June 2026 draft surveyor-regulation amendments | `LR-INS-S64UM` |
| INS-Q-08 | Whether commercial insurance disputes of specified value require s.12A PIMS before suit (Commercial Courts Act s.2(1)(c)(xii)) and how Equator's voluntary mediation interacts (M-06) | COM PIMS pack reuse |

### 18.2 Conflicts found and resolutions applied

| # | Conflict | Resolution in this file |
|---|---|---|
| C-01 | Error code: P08 FR-P08-56 uses `INS_RETAIL_ARBITRATION` **409**; Appendix F registers canonical `INS_RETAIL_ARBITRATION_BLOCKED` **422** | Appendix F prevails (master §15): 422 `INS_RETAIL_ARBITRATION_BLOCKED`, sub-code in `rule = "INS-R1"`; P08 test text to be updated |
| C-02 | "One month" for the insurer reply: P08 vector uses rep + 30 days (no reply → last date 19 Apr 2027); General Clauses Act s.3(35) reads "month" as a calendar month | Conservative dual rule (§4.6): filing allowed from the later date; last date shown from the earlier date (OE-02 keeps 19 Apr 2027). Master X-40 fixes the legal reading as a calendar month; the earlier date is a display safety margin only, and the trace shows both |
| C-03 | P08 health vector counts surgeon and anaesthetist fees as Error 1 (categorically non-proportionate); the IRDAI exclusion list covers pharmacy, consumables, implants/devices, diagnostics (and ICU) | v2 splits E1A (statutory heads, ₹76,875) from E1B (evidence-dependent, ₹73,125); P08 FR-P08-51(2) vector superseded |
| C-04 | C2 Schedule A says the Ombudsman "binds insurer up to ₹30 lakh"; current cap ₹50 lakh (r.17(3) proviso (ii), G.S.R. 828(E)) | Schedule A v2 (§5.4) |
| C-05 | C2 Insurance Rules "made under the Mediation Act 2023" and "s.27 decree" settlement claims | Contractual mode only (NN-05); labels per §13; copy-lint |
| C-06 | P08 clock names (`ombudsman_1y`, API path `/clocks/ombudsman_1y/prompt`) vs Appendix A (`ins_ombudsman_1y`) | Appendix A names prevail; API path uses `ins_ombudsman_1y` |
| C-07 | Card INS-RET I7 charges ₹2,000 for drafting the Ombudsman complaint, while D2-18/R4 require free routes first | Self-serve Ombudsman pack is ₹0; assisted drafting (I7) available only when `ins.claim_prep_assisted` is ON after counsel (OLQ-1–3). Appendix B figure unchanged |
| C-08 | Master §5.2 allows conciliation for INS; retail Part III conciliation may trigger the Ombudsman r.14(5) bar (Q-C9) | Retail conciliation behind `ins.retail_conciliation` OFF; commercial/B2B allowed |
| C-09 | P08 motor calculator outputs an arithmetic midpoint "for reference" | Removed (NN-01 GX-3) |
| C-10 | C2 treats the ₹50 lakh figure as an eligibility bar (C4 hard fail) | Award-cap advisory (`award_cap_exceeded`), per LR-IRDAI-002 open item |
| C-11 | C2 underinsurance sensitivity text (~₹53.6 lakh at VaR −10%) does not match its own formula | v2 computes ₹51,52,778 with the stated formula (§12.6) |
| C-12 | New sub-codes used here (`INS_TP_MACT_EXCLUSIVE`, `INS_SCHEME_LADDER`, `INS_RETAIL_CONCILIATION_FLAG_OFF`, `INS_OMBUDSMAN_PERSONAL_LINES_ONLY`, `INS_ARB_LIABILITY_NOT_ADMITTED`, `INS_ED_RETAIL_BINDING_BLOCKED`, `INS-ED-CONFLICT`, `INS_AUTHORITY_UNCONFIRMED`, `INS_NEUTRAL_CONCENTRATION`) | Must be registered in Appendix F §F.10.2 before use (CI check): `INS_TP_MACT_EXCLUSIVE`, `INS_SCHEME_LADDER`, `INS_RETAIL_CONCILIATION_FLAG_OFF`, `INS_OMBUDSMAN_PERSONAL_LINES_ONLY`, `INS_ARB_LIABILITY_NOT_ADMITTED`, `INS_ED_RETAIL_BINDING_BLOCKED` → `MECHANISM_NOT_PERMITTED_FOR_VERTICAL` (422); `INS-ED-CONFLICT` → `CONFLICT_DETECTED` (409); `INS_NEUTRAL_CONCENTRATION` → `CONCENTRATION_CAP_EXCEEDED` (409). `INS_AUTHORITY_UNCONFIRMED` (409, as used in FR-P08-56 and §17) has no canonical equivalent and is proposed as a new §F.10.1 code (X-20) |

### 18.3 Research open items
OI-S3-02 capture ClaimBuddy's and Insurance Samadhan's current fee pages (the 9% figure dates from 2020); OI-S3-03 run the review-mining protocol (PI-CMP-05) for ClaimBuddy, Insurance Samadhan, Policybazaar and InsuranceDekho; OI-S3-04 IRDAI Insurance Brokers Regulations 2018 text on claims consultancy; OI-INS-05 verify *Mahakali Sujatha* and *Harsolia Motors* report citations; OI-INS-06 Limitation Act Art. 44 and carrier-claim article mapping re-fetched; OI-INS-07 Bima Sugam API status.

*(End of V4 — INS.)*
