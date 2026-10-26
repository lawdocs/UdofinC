# Phase P09 — Risk Assessment Lab: ICAAP, Stress Testing, Capital and Ratios

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:**
> - **P08** (taxonomy, RAS, KRI engine, breach episodes, committee packs, dashboard/widget shell — mandatory);
> - **P11** (accounting bridge: trial balance, Tally Prime/Excel import, Ind AS/AS mapping, financial statements; returns kernel client) — the Lab's non-Finbyx data path;
> - **P02** (rule packs: capital, ALM, PCA, ratio thresholds as effective-dated Governed packs);
> - **P07** (DMS and Word generation with tracked changes for the ICAAP document);
> - **P06** (Board/RMC/ALCO meetings, approvals and minute references);
> - **P18** (Finbyx/Udofin `risk` events and the proposed stress-run API).
>
> **Sequencing:** starts when P08 exits and P11's trial-balance import is available (P11 sprint 2). Capital and ratio engines first (sprints 1–3), ALM and liquidity (3–4), stress studio (4–6), ICAAP (6–7), KMP dashboards and exports (7–8). Banks' 1 April 2027 rule packs run in parallel mode from go-live (§4C.4).
>
> **Binding appendices:** H (ratio library, scenario library, ICAAP outline, KRI library, Basel mapping), A (ICAAP, stress-run and certification state machines), I (return elements that share metrics, e.g., DNBS03/DNBS04A/B), J (Ind AS/AS and Schedule III mapping), U, L.
>
> **Requirements covered:** R-010, R-011, R-012, R-052, R-058, R-059, R-060, R-061, R-064 (investment-entity ratios), R-065 (ARC capital), R-077, R-078, R-021 (exports), R-024, R-028, R-086.
>
> **Estimated effort:** 8 two-week sprints, squad of 8 (backend/quant engineers 3, frontend 2, risk/treasury domain analyst 1, chartered accountant/actuarial reviewer 0.5, QA 1.5).

> **v1.1 changes (25 October 2026)**
> - New §4N *(v1.1)*: clear split of metric ownership between P09 (definition, computation, certification) and P28 (semantic layer, dashboards, packs); tenant-defined internal metrics; 16 new stress scenarios (climate transition/physical chronic, third-party/cloud and payment-system outage, co-lending/LSP failure with DLG, social-media-driven digital run, model failure, geopolitical/FX, pandemic, and the six BCBS IRRBB standardised shocks for banks) bringing the library to 62 (Appendix H §H.9 *(v1.1)*); narrative-ready result cards for boards (IMP-127); one-click roll-forward and reproducible "as-at" re-runs; what-if sandbox; capital-planning early warnings feeding P08; shared data intake and mapping memory with P11 (IMP-128); Risk Analyst agent scope under autonomy ceilings (NN-47, NN-50); group and multi-currency consolidation and later foreign-subsidiary packs (P25).
> - KMP, committee and Board dashboards (§4K) are rendered by **P28** (module `rpt`, D-47); P09 supplies certified metrics and role-template content.
> - New screens SCR-RAL-23 to SCR-RAL-26, settings, events, Gherkin scenarios and OI-P09-17 to OI-P09-22.

---

## 1. Objective and business outcome

Risk managers at Indian regulated entities run capital, liquidity and stress tests in spreadsheets that break every quarter, are hard to audit and cannot show where a number came from. Finbyx solves this for lenders whose books are on Finbyx (Finbyx Part 7E). LawDocsComply must solve it for **every** tenant: Finbyx lenders (by consuming certified Finbyx runs), lenders on other LMSs, banks and UCBs, ARCs, CICs, insurers (as reported), investment companies, listed corporates and co-operatives — from their trial balance, loan-book extracts and portfolio files. The Lab delivers transparent, reproducible engines and a Board-ready ICAAP, with every figure traceable to its input and rule version (NN-22).

| Outcome | Exit-gate measure |
|---|---|
| Right engine for each entity | The capital profile resolver selects the correct engine and minimums for 12 seeded profiles (NBFC-BL leverage only; NBFC-ML CRAR 15%/T1 10%; NBFC-UL + CET1 9%; gold-primary T1 12%; HFC; CIC ANW/RWA 30%; commercial bank CET1 5.5%/T1 7%/total 9% + CCB 2.5%; UCB Tier 1 9% / Tiers 2–4 12%; ARC CRAR 15%; insurer solvency 150% as reported; corporate Schedule III ratios; credit co-operative management indicators) with citations |
| One number, one lineage | Any certified ratio drills to source rows (TB line, loan-book segment, Finbyx event) in ≤ 3 clicks; recomputing a frozen snapshot reproduces identical results bit-for-bit |
| Finbyx clients never re-key | For a Finbyx tenant in `LDC_EXTERNAL` mode, `CapitalRatioComputed`, `RiskSnapshotPublished` and `StressTestCompleted` populate the Lab within the Ecosystem Spec SLA, with provenance `FX` and no LDC recomputation of certified values |
| Non-Finbyx clients self-serve | An NBFC on a third-party LMS uploads the TB (Tally Prime XML/Excel), the loan-book segment template and the borrowings template and gets CRAR, Tier 1, leverage, SLS, IRS, LCR (where applicable), concentration and 40+ ratios within 30 minutes of upload, with data-quality results |
| Stress tests a Board can trust | Scenario library (46 seeded scenarios) covering credit, collateral, interest-rate, liquidity, concentration, operational, cyber, macro and reverse stress; a multi-period run (up to 12 quarters) completes in < 2 minutes for a 50-segment book; approved scenarios are immutable |
| ICAAP in weeks, not months | ICAAP cycle from data freeze to Board-ready Word/PDF in ≤ 15 working days on the pilot NBFC-ML, with tracked changes against last year's document (P07), every table bound to the frozen snapshot |
| KMP dashboards | 15 role templates (CEO, MD, CFO, CRO, CCrO, CCO, CS, IA head, Board, Audit Committee, RMC, ALCO, ITSC, Treasurer/co-op Secretary, Insurer CFO/Appointed Actuary view) render with only governed metrics; users customise without a super admin |
| Exports that stand alone | ICAAP, stress results, capital and ratio packs export as Word, Excel (values plus an assumptions sheet and lineage sheet) and PDF/A into LDC-EXPORT-1.0 `09 Risk Assessments - ICAAP, Stress Tests and Ratios/<FY>/…` and open without LDC |

---

## 2. Scope (in / out)

**In scope**

- Compute modes and data intake (Finbyx-sourced, Udofin LSP metrics, LDC-computed from templates, manual attested) with a frozen, hashed **risk data snapshot** and BCBS 239-style data-quality governance (§4A).
- Use of the shared `infrabyx-risk-kernel` (metric formulas, capital rule packs, ALM maths, PCA thresholds, stress primitives) so that Finbyx and LDC compute identically (§4B).
- Capital adequacy engines per entity family (§4C).
- Governed ratio engine and metric layer (ratio library in Appendix H §H.6) (§4D).
- ALM, liquidity and interest-rate risk tools (§4E).
- Concentration and large-exposure analytics (§4F).
- Investment-portfolio analytics for NBFC-ICC/CIC and investment entities (classification, valuation buckets, sensitive-sector exposure, AIF investment rules) (§4G).
- Stress testing and scenario studio, including reverse stress and multi-period projections (§4H).
- ICAAP workflow and document generator (§4I).
- PCA and supervisory-action monitoring (NBFC; bank PCA and UCB SAF as rule packs) (§4J).
- KMP, committee and Board dashboards with certification and customisation (§4K).
- Lab model governance (registry entries, validation, back-testing) (§4L).
- Exports and evidence (§4M).

**Out of scope**

- Account-level loan servicing, ECL computation from loan-level PD/LGD models (system of record: Finbyx Part 7C or the tenant's LMS/finance system; the Lab imports ECL by stage). A simplified ECL *overlay* for stress projections is in scope (§4H.4).
- Regulatory return filing (P11 prepares return-ready files; NN-08).
- Actuarial valuation for insurers (Appointed Actuary's systems) — the Lab imports solvency and ALM results.
- Scheme-level NAV and fund accounting for MFs/AIFs (imported).
- Trading/treasury front-office systems; VaR models beyond the transparent historical/parametric calculators in §4E.6.

---

## 3. Personas and permissions touched

| Role code (sub-type) | Use of the Lab | Key permissions |
|---|---|---|
| `ten_kmp` (CRO) | Owns stress library, ICAAP cycle, model registry; certifies risk metrics | `ral.scenario.approve`, `ral.icaap.*`, `ral.metric.certify` (risk metrics) |
| `ten_kmp` (CFO) | Owns capital and financial ratios; certifies capital runs; capital plan | `ral.capital.certify`, `ral.metric.certify` (financial metrics) |
| `ten_maker` (risk analyst, finance analyst, treasury) | Uploads data, runs engines, prepares scenarios and ICAAP sections | `ral.data.upload`, `ral.run.execute`, `ral.icaap.section.edit` |
| `ten_checker` (data steward / reviewer) | Validates data quality, reviews runs and scenarios | `ral.*.validate` (never own submissions, NN-05) |
| `ten_kmp` (CEO, MD, CCrO, CCO, CS, CISO) | Dashboards; CS manages ICAAP Board approval | Role templates |
| `ten_committee_member` (RMC, ALCO, Audit Committee), `ten_board_member` | Review, recommend, approve | Committee-scoped |
| `ten_internal_auditor` | Independent review of ICAAP and models (third line) | Read-all Lab; review notes |
| `ten_external_auditor`, `ten_supervisor_view` | Grant-scoped read (D-12) | Watermarked exports |
| `dlv_professional` (LawDocs risk consultant via retainer or marketplace engagement) | Prepares ICAAP drafts and stress runs as maker for the client | Tenant grant (D-03, R-072); never certifies |
| `svc_vidhi` | Drafts narratives, scenario rationales, data-quality explanations | On behalf of user; cannot run certification or approve (NN-14) |

---

## 4. Functional requirements

### 4A. Compute modes, data intake and the risk data snapshot

**FR-P09-01 — Compute mode per metric family.** For each legal entity and metric family (capital, liquidity, IRRBB, concentration, asset quality, profitability, investments, insurance solvency, people/ops), the tenant sets a compute mode (Tenant tier, maker-checker):

| Mode | Meaning | Provenance badge | Typical tenant |
|---|---|---|---|
| `FX_SOURCED` | Values come from Finbyx certified runs (`CapitalRatioComputed`, `RiskSnapshotPublished`, `StressTestCompleted`, `LimitBreached`) — LDC does not recompute certified values | `FX` | Finbyx lender in `LDC_EXTERNAL` / `LDC_GROUP` mode (Ecosystem Spec §9.1) |
| `UD_SOURCED` | LSP-side metrics from Udofin (Udofin never computes RE prudential ratios — Ecosystem §6.22) | `UD` | Udofin's own LDC tenant; RE's LSP oversight KRIs |
| `LDC_COMPUTED` | LDC runs the shared kernel on imported data (P11 TB + Lab templates or third-party LMS via P18 connector) | `LDC` | Non-Finbyx lenders, banks, UCBs, ARCs, CICs, corporates |
| `IMPORTED_RESULT` | Results computed elsewhere (actuarial system, fund accounting, treasury system) uploaded with evidence | `IMP` | Insurers, AMCs, AIFs, banks with their own ALM engine |
| `MANUAL_ATTESTED` | Value entered by a maker with evidence; checker approval | `MAN` | Small co-operatives, one-off metrics |

A family can mix modes (for example, capital `FX_SOURCED` and people risk `LDC_COMPUTED`). The dashboard never blends provenance silently: each tile shows its badge.

**FR-P09-02 — Lab data templates (Excel, versioned).** For `LDC_COMPUTED`, the Lab publishes templates (Appendix H §H.8.3; all with a protected `_Template_Info` sheet as in D-08):

| Template code | Grain | Key fields | Feeds |
|---|---|---|---|
| `LDC-DT-TB-v1.0` | GL account × period (or P11 import) | account, Ind AS/AS line mapping, debit, credit, closing | Capital components, profitability, stock ratios |
| `LDC-DT-RAL-LOANSEG-v1.0` | Segment = product × asset class (Stage 1/2/3; IRACP Standard/SMA-0/1/2/Sub-standard/Doubtful/Loss) × sector × state × secured flag × risk-weight class × rate type | count, outstanding principal, interest accrued, undisbursed, provisions (IRACP), ECL by stage, collateral value, LTV band, residual maturity bucket, repricing bucket | Credit RWA, asset quality, stress, SLS/IRS slotting |
| `LDC-DT-LOAN-v1.0` (optional loan-level) | Loan, pseudonymised id (no name, PAN, phone — NN-12) | as segment + counterparty group id (pseudonymised), sanction, DPD, rating | Concentration, top-N stress, migration |
| `LDC-DT-EXPO-v1.0` | Counterparty/group (pseudonymised) | on-BS, off-BS by CCF class, CRM, sector, connected flag | Concentration (CON), large exposures |
| `LDC-DT-BORROWINGS-v1.0` + `LDC-DT-DEPOSITS-v1.0` | Borrowing/deposit instrument | lender type, instrument, amount, rate, reset, maturity, covenants, rating triggers | SLS, IRS, funding concentration, run-off stress |
| `LDC-DT-INVEST-v1.0` | Security/holding | ISIN, category (HTM/AFS/FVTPL or amortised cost/FVOCI/FVTPL), listing, rating, issuer group, quantity, cost, fair value, level, AIF/REIT/InvIT flags | Investment analytics, market stress, sensitive-sector exposure |
| `LDC-DT-RAL-HQLA-v1.0` | HQLA holding | level, haircut class, encumbrance, monetisation test date | LCR |
| `LDC-DT-RAL-OBS-v1.0` | Off-balance-sheet item | type, CCF class, counterparty group, maturity | RWA, liquidity outflows |
| `LDC-DT-CAPITAL-v1.0` | Capital instrument | type (equity, PCPS, PDI, sub-debt), amount, issue/maturity dates, amortisation, eligibility | Tier 1/Tier 2 build-up |
| `LDC-DT-RAL-INS-v1.0` | Insurer solvency/ALM result | ASM, RSM, solvency ratio, line-of-business RSM, ALM duration gap | Insurer dashboards |
| `LDC-DT-RAL-COOP-v1.0` | Society return | own funds, deposits, loans, overdue, demand, reserve fund, investments in co-op banks | Co-op indicators |

**Shared intake with P11 (review R4, 25 Oct 2026).** Trial balance, loan tape, exposures, borrowings, deposits, investments and capital instruments use the P11 data templates (`LDC-DT-TB`, `LDC-DT-LOAN`, `LDC-DT-EXPO`, `LDC-DT-BORROWINGS`, `LDC-DT-DEPOSITS`, `LDC-DT-INVEST`, `LDC-DT-CAPITAL`, FR-P11-16) — one upload feeds both the Return Studio and the Lab; P11 owns their field definitions and the columns listed above are the minimum the Lab reads. Only the Lab-specific datasets keep the `LDC-DT-RAL-*` prefix (`LOANSEG`, `HQLA`, `OBS`, `INS`, `COOP`). The names `LDC-DT-RAL-TB` (master X-09 example) and `LDC-DT-INVESTMENTS` (P15 FR-P15-34) are aliases of `LDC-DT-TB` and `LDC-DT-INVEST`.

Templates follow the D-08 discipline: exact headers, dropdowns from a `Rough` sheet with named ranges, validation rules documented in Appendix H §H.8.3; uploads pass preview → row-level errors → commit (same importer framework as P03/P11).

**FR-P09-03 — Third-party LMS and accounting connectors.** Through P18 connectors (generic LMS CSV/API adapter, Tally Prime via P11, Excel), the same canonical tables are filled. A mapping profile per source is saved and reused each period.

**FR-P09-04 — Risk data snapshot.** Every regulatory or ICAAP run works on a **snapshot**: `as_of`, source batches (with file hashes, connector run ids, Finbyx event ids), reconciliation results, data-quality results, frozen state and SHA-256 hash over canonical rows. States: `ASSEMBLING → DQ_PASSED | DQ_FAILED → FROZEN → SUPERSEDED`. A frozen snapshot is immutable; a fix creates a new snapshot with reason and diff (NN-07, NN-22).

**FR-P09-05 — Reconciliation and data-quality rules (BCBS 239 inspired).** Mandatory checks before `DQ_PASSED` for regulatory metrics: (a) loan-book outstanding reconciles to TB loan accounts within tolerance (default ₹1 lakh or 0.01%, Tenant floor); (b) provisions reconcile to TB; (c) funding template reconciles to borrowings in TB; (d) every segment has a risk-weight class; unclassified EAD ≤ 0.1% (mirrors Finbyx RK3.3 quality gate); (e) maturity and repricing buckets complete; (f) period closed (TB locked in P11); (g) no negative balances where not allowed; (h) ECL by stage ≥ 0 and consistent with stage totals. Warnings vs blocking per metric type (blocking for regulatory, warning for market metrics). The DQ dashboard reports completeness, accuracy, timeliness, adaptability indicators (BCBS 239 Principles 3–6) with trend — a supervisory-quality story the CRO can show (BCBS 239 is labelled "design reference", not a legal obligation for Indian NBFCs).

**FR-P09-06 — Finbyx-sourced path.** For `FX_SOURCED`, the Lab stores inbound events as `fx_capital_run`, `fx_metric_value`, `fx_stress_result` with signature, `contenthash`/`prevhash` chain, rule-pack version and certification state; dashboards show them as certified only if the producer marked them certified. Drill-down offers a deep link to Finbyx (`View lineage in Finbyx`); LDC holds no account-level data (NN-23).

### 4B. Shared risk kernel

**FR-P09-07 — `infrabyx-risk-kernel`.** A versioned, deterministic TypeScript package (with a Python reference implementation for validation notebooks) maintained in the `infrabyx-contracts` monorepo alongside `@infrabyx/returns-kernel` and `infrabyx-returns-packs` (D-05 pattern). Contents: metric definitions (formula AST + plain-English text + fixtures; metric ids R1–R57 from Finbyx RK6.2 are canonical and LDC extensions start at R58, Appendix H §H.6), capital rule packs per profile (minimums, risk-weight tables, CCF tables, deductions, Ind AS filters — effective-dated), ALM maths (SLS slotting, cumulative mismatch, LCR stress factors and caps, TGA/EaR/DGAP/ΔEVE), PCA thresholds, concentration limits, stress primitives (shock application, propagation, reverse-stress bisection). Both Finbyx and LDC pin a kernel version per run; results record it. Golden fixtures (Finbyx RK3/RK4/RK6/RK7 acceptance values, e.g., LCR 115%/75% example) run in both CI pipelines. *(Adopted as management decision D-22, `02` §2.3.)*

**FR-P09-08 — No formula push into Finbyx.** LDC never sends formula logic to Finbyx (Ecosystem §6.22). Tenant-defined metrics in LDC are computed only in LDC (`LDC_COMPUTED`) or on Finbyx-supplied aggregates; to have Finbyx compute a new metric, the tenant raises a metric request in Finbyx.

### 4C. Capital adequacy engines by entity family

**FR-P09-09 — Capital profile resolver.** Reads the P15 entity profile (regulator, family, layer/tier, gold-primary test, deposit-taking, listed) and selects the engine and minimums (Governed rule packs; Appendix H §H.7 has the full table):

| Profile | Engine | Minimums (regulatory floor) | Source |
|---|---|---|---|
| NBFC-BL (non-gold-primary) | Leverage | Outside liabilities ÷ owned fund ≤ 7 | NBFC CAP Directions 2025 (RBI/DOR/2025-26/345) paras 4(7), 17 |
| NBFC-ML and above (non-gold-primary): ICC, Factor, IFC, IDF | CRAR (credit RWA only; no Pillar 1 op/market charge) | CRAR ≥ 15%; Tier 1 ≥ 10%; Tier 2 ≤ 100% of Tier 1 | paras 6(2)–(3) |
| NBFC-UL | CRAR + CET1 | + CET1 ≥ 9% | para 6(4) |
| NBFC-TL | CRAR + bespoke | Higher charge as communicated | para 6(5) |
| Gold-loan NBFC (gold loans ≥ 50% of financial assets), any layer | CRAR | Tier 1 ≥ 12%; CRAR ≥ 15%; Tier 2 ≤ 100% Tier 1 | para 6(1) (gold-primary definition para 4(8) per Finbyx [VERIFY]) |
| NBFC-MFI | CRAR | CRAR ≥ 15% every layer; paras 6(1), 6(2), 17 not applicable (para 3(1) proviso) | CAP para 3; MFI Directions 2025 (RBI/DOR/2025-26/371) [VERIFY paras] |
| HFC | CRAR (partial CAP application, para 3(2)) | CRAR ≥ 15%; Tier 1 ≥ 10% | HFC Directions 2025 (RBI/DOR/2025-26/365) [VERIFY para] |
| CIC | ANW/RWA, leverage | ANW ≥ 30% of RWA; outside liabilities ≤ 2.5 × ANW | CIC Directions 2025 (RBI/DOR/2025-26/367); CAP para 3(4) |
| MGC | Per MGC Directions | NOF ₹100 crore; capital per MGC Directions [VERIFY] | RBI/DOR/2025-26/369 |
| Commercial bank | Basel III: credit RWA (SA), market RWA (SA), operational RWA | CET1 ≥ 5.5%, Tier 1 ≥ 7% (AT1 ≤ 1.5%), total ≥ 9% (Tier 2 ≤ 2%); CCB 2.5% CET1 (CET1+CCB 8%; total+CCB 11.5%); D-SIB surcharge; CCyB (rate as announced); leverage ratio [VERIFY: 4% D-SIB / 3.5% others] | Commercial Banks CA Directions 2025 (RBI/DOR/2025-26/151) para 11 Table 1; paras 250–252; Ch VI.B–C; Ch VII |
| Commercial bank from 1 Apr 2027 | Revised SA credit, revised market risk, new operational-risk standardised approach (BIC × ILM) | As effective-dated rule pack [VERIFY dates and coefficients] | Finbyx RK3.6 reading; RBI 2026 bank directions [VERIFY] |
| SFB / PB / RRB / LAB | Bank engine with family overrides | [VERIFY] SFB minimums | SFB Prudential Norms on Capital Adequacy Directions 2025 [VERIFY] |
| UCB | CRAR (credit RWA; UCB weights) | Tier 1 UCB CRAR ≥ 9%; Tiers 2–4 ≥ 12% (glide completed 31 Mar 2026); net worth ₹2 crore (Tier 1 single district) / ₹5 crore (50% by 31 Mar 2026; 100% by 31 Mar 2028); Tier 2 ≤ 100% Tier 1 | UCB CA Directions 2025 (RBI/DOR/2025-26/275) paras 6, 7, 9, 10 |
| ARC | CRAR + NOF | NOF ≥ ₹300 crore (existing ARCs by 31 Mar 2026); CRAR ≥ 15% of RWA | ARC Directions 2025 [VERIFY ref and paras] |
| IFSCA FC/FU | Per IFSCA banking directions applied mutatis mutandis | [VERIFY] numbers (IFSCA circulars 3 May 2021 and 6 May 2021) | IFSCA |
| Insurer | Imported solvency | Solvency ratio (ASM ÷ RSM) ≥ 150% control level | Insurance Act s.64VA; IRDAI (AFIF) Regulations 2024 |
| MF AMC | Net-worth monitor | AMC net worth floor per SEBI MF Regulations [VERIFY] | SEBI |
| Insurance broker / other intermediaries | Net-worth monitor | Per IRDAI/SEBI registration regulations [VERIFY] | — |
| Company / LLP | Financial-ratio engine (no capital adequacy) | Schedule III ratio disclosures (§4D.6) and lender covenants | Companies Act 2013 Schedule III |
| Credit co-operative society | Management indicators | No RBI capital norm; State Act/MSCS Act reserve-fund rules [VERIFY per state] | MSCS Act 2002 s.63 [VERIFY]; State Acts |

**FR-P09-10 — NBFC CRAR computation (LDC_COMPUTED).** Implements the CAP Directions structure: owned fund and NOF; CET1 elements and deductions (goodwill and intangibles, DTA treated as intangible, excess investments in group/other NBFCs above 10% of owned fund, impairment reserve not recognised — paras 7–8, 14); Tier 1 (paras 10–11, PDIs ≤ 15% of Tier 1); Tier 2 (para 13: general provisions/loss reserves ≤ 1.25% of RWA, revaluation reserves at 55% discount, sub-debt with amortisation ≤ 50% of Tier 1); Ind AS adjustments (para 16, e.g., Stage 1 ECL to Tier 2 within the 1.25% cap, unrealised gains); AIF subordinated units, co-lending unrealised profit and DLG adjustments (para 15); credit RWA from the para 18(1) table (0% cash/approved securities/loans against own deposits/staff loans; 20% PSB bonds; 75%/50% high-quality infrastructure after 2%/5% repaid; 100% others; 125% consumer credit excluding housing, education, vehicle, gold and microfinance/SHG, and credit-card receivables) plus 18(2)(iv) CGTMSE/CRGFTLIH/NCGTC 0% within cover; off-balance-sheet CCF classes; securitisation exposures (Chapter III-B, paras 19–51). Output: capital build-up, RWA by class, ratios, headroom vs `max(regulatory minimum, Board minimum)`, RWA walk, top-20 RWA contributors.

**FR-P09-11 — Bank engine (LDC_COMPUTED or IMPORTED_RESULT).** Banks usually run RWA in their own systems. The Lab supports: (a) `IMPORTED_RESULT` of the capital return or Pillar 3 tables (capital components, RWA by risk type), validated for internal consistency; (b) a transparent standardised-approach calculator for credit RWA on segment data (for smaller banks, UCBs moving to SA, and ICAAP projections); (c) operational risk: current approach per bank directions and the from-2027 BIC × ILM calculator behind `ral.bank.oprisk_2027.enabled` [VERIFY]; (d) market risk: duration-based and simple equity/FX capital calculators for projection only; (e) buffers (CCB, D-SIB, CCyB) and leverage. Pillar 3 tables are produced for P08 §4L from certified values.

**FR-P09-12 — Run types and states.** Daily/weekly shadow (management), monthly management, quarterly regulatory (DNBS03 elements via P11 — Appendix I), annual audited, ad hoc what-if. States `DRAFT → COMPUTED → VALIDATED (checker) → CERTIFIED (CFO eSign; CRO concurrence for regulatory runs) → FILED (link to P11 return package)`. Corrections create a new `run_no` with reason and diff; a filed run opens a P11 revision task (mirrors Finbyx RK3.3). A failed run never overwrites the last certified value on dashboards.

**FR-P09-13 — Capital what-if and planning.** What-if on proposed exposures (amount, product, collateral, guarantee) returns incremental RWA, CRAR impact (bps), concentration impact and RAS utilisation; capital plan (3–5 years) with growth, mix, profitability, dividends and capital raises; links to ICAAP §4I.

**FR-P09-14 — Alerts.** Headroom bands (green above Board buffer; amber at/below Board buffer; red within 100 bps of the regulatory minimum, Tenant setting) generate P08 KRI observations; actual breach of the regulatory minimum opens a P08 limit-breach episode with the citation; BL leverage alert at 6.5 (Tenant) and breach at 7; gold-primary detector quarterly (R50) switching to Tier 1 12% with a CFO/CRO confirmation task.

### 4D. Ratio engine and governed metric layer

**FR-P09-15 — Metric records.** `metric_definition` (id, name, category, owner role, citation, description, "i"-help) → `metric_version` (formula AST + plain text, numerator/denominator source fields, grain, filters, applicability rule, thresholds typed `regulatory` / `board` / `management` / `market` per profile, effective dates, fixtures, status `DRAFT → VALIDATED → APPROVED → RETIRED`). Regulatory formulas and thresholds come only from the kernel rule packs and cannot be edited by tenants (Governed/Locked).

**FR-P09-16 — Library scope.** Appendix H §H.6 lists 125 metrics: the Finbyx canonical set R1–R57 (capital, liquidity, ALM, asset quality, concentration, profitability, product-specific caps, PCA proximity, ops/fraud/cyber/complaints) and LDC extensions R58+ for banks (NSFR, LCR bank variant, leverage, CD ratio, PSL, CASA, IRRBB ΔEVE/Tier 1, NIM), UCBs (CRAR tier, net-worth glide, PSL 60% [VERIFY], CD ratio, CRR/SLR compliance), ARCs (NOF, CRAR, SR investment ratio, resolution period ageing, recovery rate), CICs (ANW/RWA, leverage, group-company asset tests ≥ 90% / ≥ 60% [VERIFY]), insurers (solvency ratio, ASM/RSM, expense of management ratio [VERIFY], claims ratio, combined ratio, persistency, ALM duration gap), MFs/AIFs (scheme liquidity, concentration vs SEBI limits — imported), listed/corporate Schedule III ratios (current ratio, debt-equity, DSCR, ROE, inventory turnover, trade receivables turnover, trade payables turnover, net capital turnover, net profit ratio, ROCE, return on investment — with the "explain change > 25%" rule), co-operative indicators, people-risk metrics (attrition, key-person vacancy, training completion, overtime breaches — aggregates from P13), conduct metrics.

**FR-P09-17 — Change control.** Changed formula = new version; impact analysis lists every tile, KRI, RAS metric, return cell (P11), ICAAP table and frozen pack using the metric with value differences on the last three period-ends; validation by a data steward other than the requester; parallel run ≥ one period-end for regulatory metrics; approval by owner role (CRO and CFO jointly for regulatory metrics; CCO if a return element changes); dashboards show "definition changed on [date]" for two periods (Finbyx RK6.1 pattern).

**FR-P09-18 — Quality gates.** A value displays as "compliant" only if applicability resolved, completeness met (period closed, feeds received), DQ rules passed and certified by the owner role; otherwise "indicative" with the reason.

**FR-P09-19 — Lineage.** Source field → transform → metric version → value → tile, stored as OpenLineage-compatible records; visible to auditors and supervisors; three-click drill-down.

**FR-P09-20 — Schedule III ratios for companies (corporate pack).** For tenants filing under Companies Act Schedule III (Division I, II or III), the Lab computes the prescribed ratios from the P11 financial statements with prior-year comparison and flags changes > 25% requiring an explanation in the notes [VERIFY: current Schedule III text]; Vidhi drafts the explanation from the variance analysis for human edit. NBFC Division III and RBI NBFC Financial Statements Directions 2025 (RBI/DOR/2025-26/359) disclosures (capital, asset quality, liquidity, concentration) are produced for P11 notes-to-accounts.

### 4E. ALM, liquidity and interest-rate risk

**FR-P09-21 — Applicability.** NBFC ALM Directions 2025 (RBI/DoR/2025-26/355): Chapter II for assets ≥ ₹100 crore (voluntary below); Chapter III LCR for all NBFC-D and NBFC-ND with assets ≥ ₹5,000 crore, not CICs (para 4; Chapter III preamble); exclusions per para 5. Banks, SFBs, UCBs per their liquidity directions [VERIFY references]. Co-operative societies: management indicators.

**FR-P09-22 — Structural Liquidity Statement.** Slotting of inflows/outflows into the Directions' buckets (1–7, 8–14, 15–30/31 days, over 1 month to 2 months … over 5 years) using versioned slotting rules (contractual by default; behavioural assumptions only after ALCO/Board approval); cumulative mismatch % = −min(0, cumulative gap) ÷ cumulative outflows tested against 10% / 10% / 20% for the first three buckets (para 39) and Board limits to one year (para 40); solo and consolidated; early warning at 80% of limit (Tenant).

**FR-P09-23 — LCR.** HQLA ÷ net 30-day stressed outflows ≥ 100% (paras 60–62); haircuts 0%/15%/50% (para 68); NBFC-D statutory liquid assets count up to 80% of required holding (para 71); stressed outflows = outflows × 115%, stressed inflows = inflows × 75%, inflows capped at 75% of stressed outflows (para 76); downgraded asset grace 30 days (para 74); monetisation tests (para 73); HQLA use below 100% → P08 limit-breach episode with "report to DoS immediately" sub-task (para 62). Bank LCR/NSFR via bank rule packs (including bank LCR run-off changes effective 1 Apr 2026 per RBI press release 21 Apr 2025, as read in Finbyx RK4.7 [VERIFY]).

**FR-P09-24 — Interest rate sensitivity.** Traditional Gap Analysis (RSA − RSL per bucket plus non-sensitive bucket, para 49), earnings at risk on NIM for ±100/±200 bps (EaR = Σ gapᵢ × Δr × tᵢ over buckets ≤ 1 year — optional per para 52, labelled internal), duration gap DGAP = D_A − (L/A) × D_L and ΔEVE ≈ −DGAP × A × Δr ÷ (1 + r) (paras 45–46, internal); prudential gap limits vs total assets / earning assets / equity per Board (para 52). Banks: IRRBB per bank directions (EVE and NII under prescribed shock scenarios) [VERIFY RBI IRRBB instrument and shocks].

**FR-P09-25 — Stock ratios, funding concentration, disclosures.** Six stock ratios (para 43: short-term liabilities/total assets; short-term liabilities/long-term assets; CPs/total assets; NCDs < 1 year original maturity/total assets; short-term liabilities/total liabilities; long-term assets/total assets) with Board limits; funding concentration (significant counterparties, top-20 deposits, top-10 borrowings, by instrument) and the public disclosure set (paras 15, 78; Annex I) produced quarterly for P08 §4L and P11.

**FR-P09-26 — Contingency Funding Plan and liquidity stress.** CFP register (sources, amounts, lead times, owners, triggers mapped to KRIs; default triggers LCR < 110%, 1–7 day mismatch > 7%, single-lender concentration > 25% of borrowings, negative rating outlook — Tenant defaults); CFP states `MONITORING → TRIGGERED → ACTIVATED → STAND_DOWN` with decisions recorded (para 29); annual drill evidence; liquidity stress scenarios (para 28) run through §4H with survival-horizon output.

**FR-P09-27 — Behavioural assumptions.** Versioned assumption sets (prepayment, rollover of deposits/CPs, undrawn drawdown, collection efficiency) with ALCO/Board approval and back-testing; regulatory runs use only approved sets; a copy-to-RBI-RO task is generated where the rule pack requires (Finbyx reads ALM para 54 [VERIFY]).

**FR-P09-28 — Market risk calculators (transparent).** For investment books: modified duration and PV01 by bucket; equity beta-adjusted exposure; historical-simulation VaR (250/500 days, 99%, 1-day and 10-day scaling) and parametric VaR on supplied price histories — labelled "internal measure" for non-bank tenants; inputs and price sources recorded.

### 4F. Concentration and large exposures

**FR-P09-29 — Limits by profile (LDC_COMPUTED).** NBFC Concentration Risk Management Directions 2025 (RBI/DOR/2025-26/351): ML single counterparty 25% of Tier 1 (+5% infrastructure), group 40% (+10% infrastructure); IFC 30%/50%; UL large-exposure framework (20% single, +5% with Board approval and reasons, cap 25%; group 25% (+10% infrastructure); IFC variants); BL Board-approved limits; sensitive-sector Board limits (capital market, CRE), IPO financing ≤ ₹1 crore per borrower — as read in Finbyx RK5.1 (CON paras 13–14, 33–35, 39, 11–12, 24) [VERIFY each para]. Banks: LEF per bank directions [VERIFY]. UCBs: UCB exposure norms [VERIFY].

**FR-P09-30 — Analytics.** Utilisation by counterparty and group (pseudonymised), top-20 advances and exposures, sector/state/product/channel HHI, related-party exposure aggregates, intra-group exposure, LSP/co-lender concentration, funding concentration. For `FX_SOURCED` tenants, Finbyx `LimitBreached` (LE, SSE, CME) and snapshot aggregates populate the views; LDC cannot resolve pseudonyms.

### 4G. Investment-portfolio analytics (NBFC-ICC, CIC, investment entities)

**FR-P09-31 — Portfolio view.** From `LDC-DT-INVEST` or Finbyx `investment_position` aggregates (Ecosystem entity 36): classification per NBFC Investment Portfolio Directions 2025 (RBI/DOR/2025-26/354) [VERIFY categories under Ind AS], valuation level, listed/unlisted, rating, issuer group, sector, market-cap band (large/mid/small cap per AMFI classification), instrument type (equity, IPO allotments — mainboard and SME, debt, G-sec, CP, AIF units by category, REIT/InvIT units, MF units), holding period, realised/unrealised gains.

**FR-P09-32 — Investment limits and tests.** Board investment-policy limits; investments in group/other NBFCs above 10% of owned fund deducted from Tier 1 (CAP para 10); capital-market exposure (CON sensitive sector); AIF investment rules for REs (RBI circulars on investments in AIFs, 19 Dec 2023 and 27 Mar 2024, as revised [VERIFY 2025 revision]) — exposure to AIF schemes with downstream investment in debtor companies, provisioning/deduction for subordinated units (CAP para 15) — flagged as compliance checks linking to P04 obligations; CIC asset composition tests (≥ 90% in group companies; ≥ 60% equity — CIC Directions [VERIFY]).

**FR-P09-33 — Market stress on investments.** Equity shocks by market-cap band (default −20%/−30%/−40%), credit-spread shocks by rating, rate shocks (PV01), IPO lock-in and liquidity haircuts, AIF NAV markdowns — feeding P&L, OCI, capital (unrealised gains treatment under CAP para 16) and liquidity.

### 4H. Stress testing and scenario studio

**FR-P09-34 — Scenario object.** `{scenario_id, version, name, type: sensitivity | macro | liquidity | concentration | operational | cyber | climate | combined | reverse, family_applicability[], horizon (1–12 quarters), severity: baseline | adverse | severe | extreme, shocks: [{factor, segment_filter, magnitude, path: [per period], unit}], propagation_model_id, management_actions[], narrative, approver, approval_ref, status}`. Approved scenarios are immutable (new version required) (Finbyx RK7.4 rule).

**FR-P09-35 — Factor catalogue (Appendix H §H.9).** Credit: default-rate multiplier, PD shift, migration to SMA/NPA by bucket, LGD increase, recovery-rate cut, restructuring share, write-off acceleration; collateral: gold price −10/−20/−30%, property −20/−30%, vehicle resale −15/−25%, equity collateral −30/−50%; interest rates: parallel ±100/±200/±250 bps, steepener/flattener, funding-spread widening; liquidity: deposit/CP run-off %, undrawn drawdown %, rollover failure of top-N lenders, rating downgrade triggers, collection-efficiency drop; concentration: default of top-1/top-5/top-20 borrowers or groups, sector shock (MSME, microfinance, CRE, NBFC on-lending), state shock (floods, drought); operational: loss event 1-in-20 and 1-in-100 from P08 loss data/scenario analysis; cyber: core-system outage 3/5/10 days (collections stop, fraud loss, regulatory fine, customer compensation); conduct/regulatory: business restriction (e.g., embargo on new lending in a product for N months), penalty; macro: GDP growth shock mapped through a transparent satellite model (elasticities) to GNPA, credit growth and rates; climate (voluntary): physical event in exposed states, transition shock to carbon-intensive sectors.

**FR-P09-36 — Propagation engine (transparent and reproducible).** Per period: balance-sheet roll-forward (disbursement growth, run-off, prepayment), asset-quality transitions (bucket matrix), provisions (IRACP floors and/or ECL stage multipliers — simplified overlay, labelled), income (NII from yields/costs and repricing, fee income, opex, credit cost, tax), capital (retained earnings, dividends, raises, RWA from kernel), liquidity (cash-flow ladder, HQLA, LCR, survival horizon), metrics (CRAR, Tier 1, CET1, leverage, NNPA, PCA proximity, LCR, SLS mismatch, ROA). Every parameter is visible; no opaque model. Each run stores scenario version, snapshot hash, kernel version, model version and parameter values; re-running reproduces identical outputs (NN-22).

**FR-P09-37 — Reverse stress.** Bisection on a shock multiplier (or a chosen factor) until the target metric equals its threshold (CRAR at regulatory minimum; Tier 1 at minimum; PCA RT1; LCR = 100%; 30-day cumulative gap negative; NOF below floor for ARCs), within ±1 bp tolerance, with a plausibility narrative (Vidhi draft; CRO edits).

**FR-P09-38 — Run modes for Finbyx tenants.** `LOCAL_RUN` on Finbyx segment aggregates (proposed Finbyx event `RiskSegmentSnapshotPublished` — aggregated, pseudonymised segment-level data, no PII) or `REMOTE_RUN` (LDC posts a scenario *definition as data* to the proposed Finbyx API `POST /v1/risk/stress-runs`; Finbyx runs on its book and returns `StressTestCompleted`). Both are proposals to the Ecosystem Spec change process (Spec §14.2) — until accepted, Finbyx tenants run stress in Finbyx and LDC consumes `StressTestCompleted` (default `ral.stress.fx_mode = CONSUME_ONLY`).

**FR-P09-39 — Bank stress-testing coverage.** For banks, the library and governance follow the Commercial Banks CA Directions 2025 Annex IV Guidelines on Stress Testing (sections on governance, design, coverage and sensitivity shocks) [VERIFY section-level mapping in Appendix H §H.9.4]: sensitivity tests (credit, interest rate, liquidity, equity, FX), scenario tests, reverse stress, Board-approved stress-testing policy, frequency per bank size, use of results.

**FR-P09-40 — Results and use.** Results by period and metric with RAG vs thresholds; comparison of runs; waterfall from baseline to stressed CRAR; mandatory management actions where thresholds are breached; outputs flow to ICAAP (§4I), RMC/ALCO packs (P08) and the CRO dashboard. Labels: "Stress outcome — not a forecast".

**FR-P09-41 — Scenario library governance.** Seeded 46 scenarios (62 from v1.1, FR-P09-61) across families (Appendix H §H.9); tenant copies and edits drafts; approval by CRO and RMC (Board for ICAAP scenarios); annual review reminder; scenario "applicability" restricts which tenants see which scenarios (e.g., gold-price shock only for gold-loan books).

**FR-P09-42 — Non-financial-sector scenario analysis.** For companies/LLPs: revenue shock, margin squeeze, receivable delays, FX shock, key-customer loss, supply-chain disruption, interest-rate rise on borrowings — projecting cash runway, DSCR, ICR, covenant headroom and going-concern indicators (supports Board's going-concern assessment and lender covenant monitoring). For co-operatives: deposit withdrawal run, overdue spike, investment in a failed co-operative bank.

### 4I. ICAAP workflow and document generator

**FR-P09-43 — Scope and host.** ICAAP required: commercial banks (Pillar 2; Commercial Banks CA Directions 2025 Chapter V — Board-approved ICAAP, annual Board assessment, paras 6–7; ICAAP format Chapter V.D); NBFC-ML and above including HFCs, MGCs, CICs and SPDs per layer-wise applicability (NBFC CAP Directions 2025 Chapter V; Pillar 2 capital "not insisted upon" — para 54 as read in Finbyx [VERIFY]); others voluntary (UCBs [VERIFY], ARCs, IFSCA FCs [VERIFY], insurers have own-risk and solvency processes under IRDAI [VERIFY]). Setting `ral.icaap.host`: `LDC` (default for non-Finbyx tenants and Finbyx tenants in `LDC_EXTERNAL`/`LDC_GROUP` mode) or `FINBYX` (Finbyx `EMBEDDED` mode — Finbyx RK7.3 runs the cycle; LDC receives `EvidenceSubmitted`). A tenant cannot have two hosts for the same cycle.

**FR-P09-44 — Document structures (templates, versioned).**

- *NBFC template (nine parts, Finbyx RK7.2 aligned):* (1) executive summary and Board attestation; (2) business model and 3-year plan; (3) governance — RMC, CRO, three lines, RAS and limits; (4) material-risk inventory with materiality scoring; (5) capital per risk (credit Pillar 1 RWA + concentration add-on via HHI-based granularity adjustment; operational internal proxy — default 15% of 3-year average positive gross income or a BI-analogue, labelled "ICAAP internal"; IRRBB ΔEVE at ±200 bps; liquidity as buffer not capital; strategic and reputational scenario-based buffers; model-risk buffer optional); (6) stress testing (sensitivity, macro, liquidity, reverse); (7) capital plan and management actions; internal capital target = regulatory minimum + stress buffer; (8) validation, internal-audit review and use test; (9) appendices — data lineage, model inventory, assumptions register.
- *Bank template:* sections per Commercial Banks CA Directions 2025 Chapter V.D "Format of the ICAAP document" [VERIFY headings] mapped one-to-one; includes Pillar 1 vs Pillar 2 capital, SREP risks (IRRBB, liquidity, concentration, residual — para 9), stress testing per Annex IV.
- *Light template* (UCB/ARC/IFSCA/voluntary): six sections.

**FR-P09-45 — Materiality assessment.** Each P08 Level-1 risk is scored for materiality (likelihood/impact, capital sensitivity, regulatory significance) with rationale; material risks require a capital treatment or a documented reason why capital is not the mitigant (e.g., liquidity → buffer).

**FR-P09-46 — Workflow states (Appendix A §A.9).** `DRAFT → DATA_FROZEN (snapshot hash) → ASSESSED → STRESS_RUN → CRO_REVIEW → RMC_RECOMMENDED → BOARD_APPROVED → SHARED_WITH_SUPERVISOR (on request; via D-12 grant or export) → ARCHIVED`. Return paths to `ASSESSED`/`STRESS_RUN` with comments; re-freeze only with CRO approval (new hash, reason). Section owners with due dates derived from the Board calendar (P06). Off-cycle triggers: headroom below Board buffer; new business line; merger; layer migration (ML → UL); PCA RT1 projection; material RAS change; persistent KRI breaches feeding Pillar 2 add-ons (owner baseline RAF breach rule).

**FR-P09-47 — Document generation.** Each section is a DOCX template (docxtemplater) with live tables and charts bound to the frozen snapshot and narrative fields; Vidhi drafts narratives aligned to the template and to last year's approved ICAAP (P07 policy-drafting engine), output in Word with **tracked changes** vs last year (NN-04: draft until approved); Board approval captured with minute reference; signed PDF/A of the approved version stored in DMS; `EvidenceSubmitted` and `IcaapApproved` events. Internal-audit review notes attach to the cycle.

**FR-P09-48 — Supervisor interaction.** Banks submit ICAAP to RBI per SREP practice [VERIFY submission timeline]; NBFCs produce on request. LDC prepares the submission package (PDF/A + annexure Excel) and records submission evidence (NN-08); supervisory queries are logged as tasks with responses.

### 4J. PCA and supervisory-action monitoring

**FR-P09-49 — NBFC PCA.** Per RBI (NBFC – Miscellaneous) Supervisory Directions 2026 (RBI/DoS/2026-27/467) Chapter V: applicability (para 3: NBFC-D and NBFC-ND in ML/UL/TL incl. ICC, CIC, IDF, IFC, MFI, Factors; excluding NBFCs not accepting public funds, PDs and HFCs); indicators (para 16: CRAR, Tier 1, NNPA incl. NPIs; CICs ANW/RWA, leverage, NNPA); thresholds (para 17) stored as offsets below the entity's minimum and "currently" values (CRAR RT1 < 15% ≥ 12%, RT2 < 12% ≥ 9%, RT3 < 9%; Tier 1 RT1 < 10% ≥ 8%, RT2 < 8% ≥ 6%, RT3 < 6%; NNPA RT1 > 6% ≤ 9%, RT2 > 9% ≤ 12%, RT3 > 12%; CIC ANW/RWA RT1 < 30% ≥ 24%, RT2 < 24% ≥ 18%, RT3 < 18%; CIC leverage RT1 ≥ 2.5× < 3×, RT2 ≥ 3× < 3.5×, RT3 ≥ 3.5×); mandatory actions per threshold (para 19: RT1 dividend/remittance restriction, equity infusion and leverage reduction, CIC guarantee restriction; RT2 + branch-expansion restriction; RT3 + capex (except technology within Board limits) and variable-opex restrictions); discretionary menu (para 20); exit (para 18: four consecutive quarterly statements without breach incl. one audited annual, plus supervisory comfort); press release (para 21).

**FR-P09-50 — PCA states.** `NOT_UNDER_PCA → PROXIMITY (R52 within 150 bps of RT1, Tenant) → PROJECTED (forecast crossing at next FY-end or under an adverse scenario) → THRESHOLD_CROSSED (internal) → UNDER_PCA_RTn (only on recording RBI's letter by the CS) → EXIT_ELIGIBLE (tracker satisfied) → NOT_UNDER_PCA (only on RBI's withdrawal letter)`. The system never places or lifts PCA itself; restrictions (dividend proposals, branch openings, capex approvals) are checked as P04/P06 compliance gates once RBI's letter is recorded (mirrors Finbyx RK7.5).

**FR-P09-51 — Banks and UCBs.** Bank PCA framework and UCB Supervisory Action Framework as Governed rule packs [VERIFY thresholds]; same state machine.

### 4K. KMP, committee and Board dashboards

**FR-P09-52 — Role templates.** Built on the P28 dashboard framework *(v1.1; previously "P08 widget framework")*; P09 supplies certified metrics and the role-template content below; tiles only from governed metrics; each tile shows value, RAG text, metric version, as-of, provenance and certification state.

| Template | Headline content (defaults; families vary) |
|---|---|
| CEO | AUM/disbursement vs plan, NIM, ROA/ROE, CRAR headroom, GNPA/NNPA, LCR, PCA proximity, RAS scorecard, complaints, top risks, compliance status |
| MD / WTD | As CEO plus Board-agenda readiness, regulatory inspection actions |
| CFO | CRAR/Tier 1/CET1 and RWA walk, leverage, SLS and IRS, LCR, cost of funds, maturity wall, covenants, ECL vs IRACP and impairment reserve, profitability ratios, Schedule III ratios (corporates), tax and return deadlines (P11) |
| CRO | RAS utilisation, credit heat map, concentration, EWS ageing (from Finbyx), stress results, model inventory, operational losses, RCSA coverage, KRIs, impact tolerances, third-party risk |
| CCrO (Chief Credit Officer) | Sanction TAT and deviation rate (from Finbyx), early delinquency by cohort, sector caps, related-party sanctions, collateral LTV compliance (gold, shares) |
| CCO | Obligations status, returns calendar, compliance testing, inspection observations, penalties, regulatory changes pending impact |
| CS | Board/committee calendar and composition, ICAAP Board approval status, PCA restriction register, fit-and-proper declarations, listed disclosures |
| IA head | Audit plan progress, High findings ageing, RBIA heat map, model and ICAAP review status |
| Board | One-page RAS RAG, capital, liquidity, asset quality, concentration, top 10 risks, compliance, frauds, cyber, ICAAP, PCA |
| Audit Committee | ECL overlays, IS audit, internal-audit findings, related-party deviations |
| RMC | All CRO items plus liquidity, EWS effectiveness, cyber review, outsourcing |
| ALCO | SLS, IRS, LCR, stock ratios, funding plan, CFP triggers, behavioural assumption status |
| ITSC | Cyber incidents, VAPT status, DR drills, vendor risk (from P12) |
| Co-operative Secretary / Treasurer | Own funds ratio, reserve-fund compliance, overdue-to-demand, liquidity per by-laws, deposits concentration, audit observations, AGM/election calendar (P16) |
| Insurer CFO / Appointed Actuary view | Solvency ratio vs 150% control level, ASM/RSM trend, ALM duration gap, claims/combined ratios, investment limits (imported) |

**FR-P09-53 — Customisation.** Add/remove/arrange tiles, saved filters, personal thresholds (tighter only), subscriptions (in-app, e-mail, Teams/Google Chat), "view as" delegation (logged); template changes to Board/committee packs require chair approval; sandbox analysis watermarked "uncertified" and barred from packs (Finbyx RK8.2–8.3 rules).

**FR-P09-54 — Certification workflow.** Per metric value: `COMPUTED → VALIDATED (data steward) → REVIEWED (checker) → CERTIFIED (owner eSign) → PUBLISHED`; restatement revokes certification and notifies owner and CS; frozen packs keep original hash (P08 §5.9).

### 4L. Lab model governance

**FR-P09-55 — Registry entries.** Every Lab model (stress propagation model, satellite macro model, behavioural assumption set, concentration add-on method, op-risk proxy, VaR calculator, ECL overlay) is registered in the P08 model inventory with owner, tier, version, validation status, back-testing results and approval. Version bumps require validation by someone other than the developer; results record model versions.

**FR-P09-56 — Back-testing.** Annual back-test of behavioural assumptions (actual vs assumed run-off/prepayment), satellite model (predicted vs actual GNPA), VaR (exceptions count, traffic-light) — results to RMC pack.

### 4M. Exports and evidence

**FR-P09-57 — Export formats.** Capital run pack (Excel: capital build-up, RWA by class, lineage sheet, assumptions sheet; PDF/A summary), ratio pack, ALM pack (SLS, IRS, LCR, stock ratios), stress run report (Excel results by period + Word narrative), ICAAP (DOCX with tracked-changes history + PDF/A approved), KMP dashboard snapshots (PDF with watermark). All placed in LDC-EXPORT-1.0 `09 Risk Assessments - ICAAP, Stress Tests and Ratios/<FY>/<Capital|Ratios|ALM and Liquidity|Stress Tests|ICAAP|Dashboards>/` with a CSV index and SHA-256 manifest (NN-09, NN-10; Appendix M).

**FR-P09-58 — Get expert help.** Each Lab area shows a "Get help from a professional" link to the P21 marketplace (ICAAP drafting, stress-testing engagement, ALM review); purchase does not require a SaaS subscription (R-035). Engaged professionals work as `dlv_professional` makers under a tenant grant.

### 4N. Faster, reproducible and configurable risk assessment *(v1.1)*

**FR-P09-59 — Metric ownership (P09 vs P28).** P09 owns every financial and risk **metric definition, formula version, computation run and certification** (`ral.metric_definitions`, `ral.metric_versions`, `ral.metric_values`). P28's semantic layer (module `rpt`) exposes certified and indicative values **read-only** with their version, provenance and certification badge; P28 can never compute a regulatory metric itself and never shows a value without its metric version (NN-22, NN-37). Dashboards, packs and Vidhi narration call `T-rpt-get_figures`, which resolves to P09 values.

**FR-P09-60 — Tenant-defined internal metrics.** A tenant may define internal metrics (for example "collection efficiency excluding restructured", "disbursement per branch", "cost of risk by product") in a **formula builder** over Canonical Financial Data Model fields (P11 §4D) and existing metrics, using CEL with unit and grain checks. Rules: internal metrics carry an "Internal" badge, can never replace or redefine a regulatory metric, require checker approval (data steward ≠ author), keep version history and fixtures, and may be used as KRIs (P08) and RAS metrics at Board level only when the Board approves them. Typical build time: under 10 minutes for a ratio of two existing fields.

**FR-P09-61 — Scenario library extensions.** Sixteen scenarios (ten named scenarios plus the six BCBS IRRBB standardised shocks) are added to Appendix H §H.9 *(v1.1)*, bringing the seed library to 62: SCN-CLM-03 (orderly/disorderly transition, NGFS-style, voluntary), SCN-CLM-04 (chronic physical — heat stress on labour-intensive borrowers), SCN-CYB-03 (critical cloud/SaaS provider outage — third-party concentration), SCN-CYB-04 (payment-system/UPI rail outage for 72 hours), SCN-TPR-01 (co-lending partner or LSP failure with DLG invocation and servicing transfer), SCN-DIG-01 (social-media-driven digital run: 30-day outflows compressed into 5 days), SCN-AI-01 (credit-scoring model failure: approval quality degrades for one quarter before detection), SCN-GEO-01 (geopolitical commodity shock: crude +40%, INR −10%), SCN-FX-01 (foreign-currency borrowing/ECB shock: INR −15%, hedge-cost spike), SCN-PAN-01 (pandemic-style lockdown: collections −40% for two months), and SCN-IRR-05 to SCN-IRR-10 grouped as one family entry "BCBS IRRBB six standardised shocks" for banks (parallel up/down, steepener, flattener, short up, short down) [VERIFY: Indian implementation in the Commercial Banks directions]. Each ships with default magnitudes marked [REC], applicability codes and propagation defaults; approval rules of FR-P09-41 apply.

**FR-P09-62 — Narrative-ready result cards (IMP-127).** Every certified stress, capital or ALM run produces result cards: headline metric before/after with threshold and RAG text; waterfall from baseline to stressed position; list of breached limits; management actions and their effect; a two-sentence plain-language summary written by template from bound values. Vidhi may rephrase the summary, but every number in the text is a bound placeholder resolved from the run (NN-37); a card with an unresolved or altered figure cannot be exported. Cards export to the P28 pack studio (DOCX/PPTX/PDF) and to the ICAAP document.

**FR-P09-63 — One-click roll-forward and reproducible re-runs.** "Roll forward" re-runs the last approved scenario set and capital/ALM runs on the newest frozen snapshot with the same kernel and rule-pack versions (or the current ones, by choice), shows a comparison with the previous period and highlights movements beyond the tenant's materiality threshold. "Re-run as at" reproduces any historical run byte-for-byte from its snapshot hash, kernel version and model versions (NN-22); a mismatch raises a Critical incident.

**FR-P09-64 — What-if sandbox.** Sliders and inputs for the main shock factors recompute key metrics on a cached aggregated snapshot (target ≤ 5 seconds for a portfolio of up to 2 million accounts at segment level). Sandbox results are watermarked "Uncertified — sandbox", cannot enter packs or returns, and can be saved as a draft scenario for approval with one click.

**FR-P09-65 — Capital-planning early warning.** The ICAAP capital plan (FR-P09-44) and business-plan growth inputs project CRAR/Tier 1/leverage/LCR four quarters ahead after each roll-forward; if projected headroom falls below the Board buffer, an EWS card (P08 FR-P08-61, trigger family "capital plan") is raised with the driver analysis; projections are labelled "projection — not a forecast of regulatory status" (NN-38).

**FR-P09-66 — Shared data intake with P11 (IMP-128).** One upload of an `LDC-DT-*` template or one Tally/LMS feed lands once in the P11 Data Room and feeds both the Return Studio and the Lab. Mapping memory (P11 FR-P11-81 *(v1.1)*) is shared, so a mapping confirmed for a return is reused by the Lab and vice versa. The Lab shows a data-quality score per snapshot before compute (completeness, reconciliation to TB, outliers) and blocks certification below the tenant's minimum.

**FR-P09-67 — Risk Analyst agent in the Lab (NN-37, NN-47, NN-50).** The Risk Analyst agent may: draft scenario narratives and plausibility statements; draft ICAAP section text from frozen results; propose calibration of propagation parameters from the tenant's own history (presented as a suggestion with back-test statistics); draft explanations of Schedule III ratio movements. It may not: set or change any figure, approve a scenario, certify a value, or change a threshold. Autonomy ceiling: L2 for drafting text, L1 for calibration proposals (`ral.ai.autonomy_ceiling`). Every draft lists the run ids it used.

**FR-P09-68 — Group and multi-currency consolidation.** For groups (P15 group mode), the Lab shows a consolidated view where the law defines one (for example NBFC group exposures, CIC group-company tests) and an informational group view otherwise; monetary values convert at the snapshot FX rate from `FX_RATE_PORT` (P25) with source and date. Foreign subsidiaries' prudential ratios run in `IMPORTED_RESULT` mode until a reviewed jurisdiction pack (NN-53) provides local rules (for example IFRS 9 ECL and local Basel implementation); results from other regional cells arrive as aggregates (NN-24 amended).

**FR-P09-69 — Customisation without a super admin.** Tenants configure: KMP dashboard layouts and personal views (via P28), internal metrics (FR-P09-60), custom scenarios and management actions (approval rules apply), ICAAP Word templates of their own (P07 template upload) mapped to the platform section model, certification chains within SoD, materiality thresholds for roll-forward highlights, and the schedule of automatic monthly runs.


### 4X. Cross-file hooks *(v1.1, X1 — added at cross-file resolution)*

**FR-P09-X01 — Climate scenarios from P27.** The scenario studio accepts climate scenario parameter sets (transition and physical shocks by sector and geography) published by P27 as versioned rule-pack data; results are labelled "exploratory" unless an RBI framework makes them supervisory [VERIFY status].

---

## 5. Workflows and state machines

### 5.1 Risk data snapshot

`ASSEMBLING → DQ_RUNNING → DQ_PASSED | DQ_FAILED → FROZEN → SUPERSEDED`. `DQ_FAILED` shows blocking and warning rules with row references and a "fix and re-run" path; a data steward may waive a *warning* with reason (never a blocking rule). `FROZEN` computes SHA-256 over canonical rows ordered by key and stores source batch hashes. Superseding requires reason; runs keep the snapshot they used.

### 5.2 Capital / ratio / ALM run

`DRAFT → COMPUTED → VALIDATED → CERTIFIED → FILED`, with `FAILED` (stays draft with reason) and correction runs (`run_no + 1`). Certification requires a `FROZEN` snapshot for regulatory runs.

### 5.3 Scenario version

`DRAFT → SUBMITTED → CRO_APPROVED → RMC_APPROVED (or BOARD_APPROVED for ICAAP scenarios) → ACTIVE → RETIRED`. Edits after approval create version n+1.

### 5.4 Stress run

`QUEUED → RUNNING → COMPLETED → REVIEWED → APPROVED → PUBLISHED (to packs/ICAAP)`; `FAILED` with error; reproducibility check job re-runs approved runs monthly on the stored inputs and alerts on any difference (should never occur).

### 5.5 ICAAP cycle (Appendix A §A.9)

| State | Owner | Exit guard |
|---|---|---|
| `DRAFT` | Risk function | Cycle plan, section owners, Board date |
| `DATA_FROZEN` | Data steward | Snapshot `FROZEN`; hash recorded |
| `ASSESSED` | Risk function | Materiality complete; capital per risk computed |
| `STRESS_RUN` | Risk function | Approved scenarios run; reverse stress done |
| `CRO_REVIEW` | CRO | All sections complete; IA review note attached (or waived with reason for first cycle) |
| `RMC_RECOMMENDED` | RMC chair (via P06 minutes) | Resolution recorded |
| `BOARD_APPROVED` | CS (minute reference) | Approved DOCX locked; PDF/A signed |
| `SHARED_WITH_SUPERVISOR` | CS/CCO | Submission evidence (bank) or on-request grant |
| `ARCHIVED` | System | Next cycle started |

Return paths from `CRO_REVIEW`, `RMC_RECOMMENDED`, `BOARD_APPROVED`-pending to `ASSESSED` or `STRESS_RUN`; re-freeze only with CRO approval. SLA timers derive from the Board meeting date (default: data freeze T−45 days, CRO review T−20, RMC T−14, Board pack T−7).

### 5.6 PCA monitor

As FR-P09-50. Transitions into or out of `UNDER_PCA_RTn` require a recorded RBI letter (document + date + threshold) entered by the CS and approved by the CCO (maker-checker).

### 5.7 Pseudo-code — LCR and reverse stress

```ts
function lcr(hqla: HqlaHolding[], outflows: Decimal, inflows: Decimal, pack: AlmPack): Decimal {
  const hqlaAdj = sum(hqla.filter(h => h.unencumbered).map(h => h.value.mul(one.minus(pack.haircut(h.level)))));
  const stressedOut = outflows.mul(pack.outflowFactor);            // 1.15 (ALM para 76)
  const stressedIn  = Decimal.min(inflows.mul(pack.inflowFactor),  // 0.75
                                  stressedOut.mul(pack.inflowCap)); // 0.75 of stressed outflows
  return hqlaAdj.div(stressedOut.minus(stressedIn));
}

function reverseStress(run: (k: Decimal) => Metrics, target: (m: Metrics) => Decimal, threshold: Decimal): Decimal {
  let lo = new Decimal(0), hi = new Decimal(50);       // shock multiplier bounds
  for (let i = 0; i < 60; i++) {
    const mid = lo.plus(hi).div(2);
    (target(run(mid)).gt(threshold) ? (lo = mid) : (hi = mid));
    if (hi.minus(lo).lt('0.0001')) break;
  }
  return lo.plus(hi).div(2);                            // stored with convergence log
}
```

Golden fixture (from Finbyx RK4 acceptance): contractual outflows 100, inflows 120 → stressed outflows 115, stressed inflows capped at 86.25, net outflows 28.75; inflows 80 → stressed inflows 60, net outflows 55.

---

## 6. Screens and UX

Menu: **Risk Lab** (top-level; entitlement `ral`). Mobile: read-only dashboards; data upload and runs are desktop-first.

| Screen ID | Name | Menu path | Key content and actions |
|---|---|---|---|
| SCR-RAL-01 | Lab home | Risk Lab › Home | Capital headroom, liquidity, asset quality, PCA proximity, latest runs, data-feed provenance mix, DQ status, upcoming ICAAP milestones |
| SCR-RAL-02 | Data & snapshots | Risk Lab › Data | Compute-mode matrix per metric family; template downloads; uploads (preview, errors, commit); connector runs; snapshots list with DQ results; freeze |
| SCR-RAL-03 | Data quality | Risk Lab › Data › Quality | Rules, results, reconciliation breaks, waivers, BCBS 239-style indicators |
| SCR-RAL-04 | Capital runs | Risk Lab › Capital | Run list; build-up (CET1/Tier 1/Tier 2 with deductions); RWA by class; RWA walk; top-20 contributors; quality gates; certify; correction run |
| SCR-RAL-05 | Capital drill-down | Risk Lab › Capital › Drill-down | Ratio → class → rule → segment/loan (3 clicks); Finbyx deep link |
| SCR-RAL-06 | What-if & capital plan | Risk Lab › Capital › Planning | Exposure what-if; 3–5 year plan; scenario overlays |
| SCR-RAL-07 | Ratio library | Risk Lab › Metrics | Library with filters (category, owner, regulatory/board/market, family); metric detail (formula text and tree, versions, fixtures, lineage, consumers); change requests |
| SCR-RAL-08 | ALM & liquidity | Risk Lab › Liquidity | SLS grid (solo/consolidated), cumulative mismatch chart, LCR trend and components, HQLA register, stock ratios, funding concentration, maturity wall, CFP, behavioural assumptions |
| SCR-RAL-09 | Interest-rate risk | Risk Lab › IRRBB | TGA gaps, EaR, DGAP, ΔEVE; bank IRRBB scenarios |
| SCR-RAL-10 | Concentration | Risk Lab › Concentration | Limit utilisation (pseudonymised), groups, top-20, HHI, sensitive sectors |
| SCR-RAL-11 | Investments | Risk Lab › Investments | Portfolio by category/valuation level/market-cap band; limits; AIF/REIT/InvIT/IPO views; market stress |
| SCR-RAL-12 | Scenario library | Risk Lab › Stress › Scenarios | Seeded and tenant scenarios; applicability; versions; approvals; compare |
| SCR-RAL-13 | Run builder | Risk Lab › Stress › New run | Choose snapshot, scenarios (multi-select), horizon, management actions; run; progress |
| SCR-RAL-14 | Stress results | Risk Lab › Stress › Results | Metrics by period with RAG; waterfall; comparison; reverse-stress result; export |
| SCR-RAL-15 | ICAAP cycles | Risk Lab › ICAAP | Cycle list; workspace with sections, live tables, narratives, comments, tracked changes; timeline; approvals |
| SCR-RAL-16 | PCA monitor | Risk Lab › PCA | Indicators current/projected; thresholds; state; restriction register; exit tracker |
| SCR-RAL-17 | KMP dashboards | Dashboards › My dashboard | Role template; customise; subscriptions |
| SCR-RAL-18 | Certification queue | Dashboards › Sign-off | Values to validate/review/certify; mark indicative; freeze packs |
| SCR-RAL-19 | Model registry (Lab) | Risk Lab › Models | Lab models, versions, validation, back-tests |
| SCR-RAL-20 | Schedule III ratios | Risk Lab › Financial ratios | Corporate ratio table with prior year, change % and explanations |
| SCR-RAL-21 | Co-operative indicators | Risk Lab › Society indicators | Management indicators per State Act/by-laws |
| SCR-RAL-22 | Insurer solvency | Risk Lab › Solvency | Imported ASM/RSM, ratio vs control level, trend |

UX rules: every number has a provenance badge and "i" explainer (formula, inputs, threshold, citation); run buttons show estimated time; long runs continue in the background with a Notification on completion (P04); keyboard shortcuts `R` run, `F` freeze, `C` compare; empty states point to the template or connector to use; error messages cite the failed DQ rule and row.

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Key content and actions | Fewer-click design |
|---|---|---|---|---|
| SCR-RAL-23 | What-if sandbox | Risk Lab › Sandbox | Shock sliders, instant metrics, save as draft scenario | Defaults from last approved scenario |
| SCR-RAL-24 | Result cards | Risk Lab › Runs › [run] › Cards | Headline, waterfall, breaches, actions; send to P28 pack | "Add to board pack" in one click |
| SCR-RAL-25 | Internal metric builder | Risk Lab › Metrics › New internal metric | CEL formula with field picker, unit check, fixtures, preview on last snapshot | Templates for common ratios |
| SCR-RAL-26 | Group capital view | Risk Lab › Group | Entity contributions, FX note, consolidated where defined | Entity switcher keeps filters |

---

## 7. Backend design

### 7.1 Modules touched

`ral` (owner), `erm` (KRIs, breaches, packs, model inventory), `acc` (TB, financial statements — P11), `ret` (return elements — P11), `int` (Finbyx/Udofin events; connectors), `wf`, `gov`, `dms`, `rpt`, `ai`, `cfg`.

### 7.2 Tables (schema `ral`; tenant- and entity-scoped; RLS)

| Table | Key columns |
|---|---|
| `compute_mode` | legal_entity_id, metric_family, mode, effective_from, approved_by |
| `source_batch` | id, template_code/version or connector_run_id or fx_event_id, file_hash, rows, received_at |
| `snapshot` | id, as_of, state, batch_ids[], dq_result_id, hash, frozen_at, superseded_by, reason |
| `canon_*` (tb_line, loan_segment, loan, exposure, funding, investment, hqla, obs_item, capital_instrument, ins_solvency, coop_return) | snapshot_id + typed columns; NUMERIC; pseudonymised ids only |
| `dq_rule` / `dq_result` | rule id, severity, metric families, expression; results per snapshot with row refs, waivers |
| `capital_run` / `capital_line` | run_no, type, profile, kernel_version, rule_pack_version, snapshot_id, state, components jsonb, rwa_by_class jsonb, ratios jsonb, certified_by; lines with source refs |
| `metric_definition` / `metric_version` / `metric_value` | per FR-P09-15; value numeric(24,8), provenance, certification_state, lineage_id |
| `alm_run` / `alm_bucket` / `lcr_component` | buckets, flows, gaps, cumulative mismatch, HQLA, outflow/inflow categories |
| `behavioural_assumption_set` | version, parameters jsonb, approvals, back-test results |
| `cfp` / `cfp_event` | sources, triggers, state history |
| `scenario` / `scenario_version` / `stress_run` / `stress_result` | per FR-P09-34/36; results per period × metric |
| `icaap_cycle` / `icaap_section` / `icaap_material_risk` / `icaap_capital_requirement` | state, snapshot_id, template_version, docx_ref, board_ref, submission evidence |
| `pca_status` / `pca_restriction` | state, threshold, RBI letter doc ref, restrictions, exit tracker |
| `fx_capital_run`, `fx_metric_value`, `fx_stress_result` | inbound copies with signature, contenthash, prevhash, certification state |

### 7.3 APIs (`/v1/ral/...`)

`GET/PUT /compute-modes`; `GET /templates/{code}`; `POST /uploads` (multipart, idempotent) → `GET /uploads/{id}/preview` → `POST /uploads/{id}:commit`; `POST /snapshots`, `POST /snapshots/{id}:dq|:freeze|:supersede`; `POST /capital-runs`, `POST /capital-runs/{id}:validate|:certify|:correct`; `GET /capital-runs/{id}/lines?class=`; `POST /what-if`; `GET /metrics`, `POST /metrics/{id}/versions`, `POST /metric-changes/{id}:approve`; `GET /metric-values?metric=&entity=&from=&to=`; `POST /alm-runs`; `GET /alm-runs/{id}/sls|lcr|irs`; `GET/POST /scenarios`, `POST /scenarios/{id}/versions/{v}:approve`; `POST /stress-runs`; `GET /stress-runs/{id}/results`; `POST /reverse-stress`; `GET/POST /icaap-cycles`, `POST /icaap-cycles/{id}:freeze|:submit|:approve`; `GET /icaap-cycles/{id}/document?format=docx|pdf`; `GET /pca`, `POST /pca/letters`. All writes need `Idempotency-Key`; certification endpoints require step-up MFA and reject self-approval (NN-05).

### 7.4 Domain events

Outbound (`in.lawdocscomply.ral.<Name>.v1`): `SnapshotFrozen`, `CapitalRunCertified`, `MetricValueCertified`, `MetricDefinitionChanged`, `AlmRunCertified`, `LcrBelowMinimum` (→ P08 limit episode), `StressRunApproved`, `ReverseStressCompleted`, `IcaapStateChanged`, `IcaapApproved` (also `EvidenceSubmitted` to the tenant's GRC destination in group mode), `PcaStateChanged`, `ScenarioApproved`. Inbound: `in.infrabyx.risk.CapitalRatioComputed`, `RiskSnapshotPublished`, `StressTestCompleted`, `LimitBreached`, proposed `RiskSegmentSnapshotPublished` (Ecosystem change request).

**Event naming (X-01; review R4).** `in.lawdocscomply.ral.*` events are internal. `IcaapApproved` → `EvidenceSubmitted`, certified metric values sent to Finbyx/Udofin or an RE GRC destination, and any future `RiskSegmentSnapshotPublished` consumption are mapped by `int` to `in.infrabyx.risk.*` / `in.infrabyx.grc.*` types (Ecosystem Spec §3.2, §6.15, §6.22).

### 7.5 Jobs and workflows

`SnapshotAssemblyWorkflow` (per upload/connector), `DqWorkflow`, `CapitalRunWorkflow`, `AlmRunWorkflow` (daily LCR where data supports), `StressRunWorkflow` (parallel per scenario; deterministic seeds where Monte Carlo options exist), `ReverseStressWorkflow`, `IcaapCycleWorkflow` (Temporal; timers from Board date), `ReproducibilityCheck` (monthly), `MetricImpactAnalysis` (on change request), `PcaProjection` (quarterly and on plan change), `GoldPrimaryTest` (quarterly), `ThresholdProximity` (monthly; R51 → P08 governance readiness).

### 7.6 Backend additions *(v1.1)*

Tables: `ral.internal_metric_defs` (metric_id, formula_cel, unit, grain, author, approver, status, fixtures jsonb); `ral.result_cards` (card_id, run_id, card_type, bound_values jsonb, summary_template_id, narrative_text, narrative_check_status); `ral.sandbox_sessions` (session_id, snapshot_id, shocks jsonb, results jsonb, saved_scenario_id); `ral.rollforward_jobs` (job_id, source_runs[], target_snapshot_id, version_policy, status, diff_ref).

APIs: `POST /v1/ral/runs/{id}:rerun-as-at` · `POST /v1/ral/rollforward` · `POST /v1/ral/sandbox` · `POST /v1/ral/sandbox/{id}:save-scenario` · `GET /v1/ral/runs/{id}/cards` · `POST /v1/ral/internal-metrics` · `POST /v1/ral/internal-metrics/{id}:approve`.

Events (internal): `ResultCardsGenerated`, `RollforwardCompleted`, `InternalMetricApproved`, `CapitalPlanWarningRaised` (→ P08 EWS), `RerunMismatchDetected` (Critical).

---

## 8. Integrations

| Port | Adapter | Notes |
|---|---|---|
| `RISK_FEED_PORT` | Finbyx, Udofin | Ecosystem Spec §6.22 events; signature and hash-chain verification; reconciliation |
| `STRESS_RUN_PORT` *(proposed)* | Finbyx `POST /v1/risk/stress-runs` | Scenario definition as data; flag `ral.stress.fx_mode` (`CONSUME_ONLY` default) |
| `ACCOUNTING_PORT` | P11 (Tally Prime XML/ODBC export, Excel TB, Zoho/other via P18) | TB with Ind AS/AS mapping |
| `LMS_PORT` | Generic CSV/API LMS adapter (P18), third-party LOS/LMS | Fills canonical loan/segment tables |
| `MARKET_DATA_PORT` | Tenant-supplied price files; licensed feeds by tenant contract [VERIFY licensing] | For VaR and investment stress |
| `RETURNS_KERNEL` | `infrabyx-returns-kernel` (D-05) | Shares element definitions with DNBS03/DNBS04A/B |
| `DOC_PORT` | P07 docxtemplater/Gotenberg | ICAAP DOCX with tracked changes; PDF/A |
| `EXPORT_PORT` | P19 | `09 Risk Assessments - ICAAP, Stress Tests and Ratios/…` |

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `ral.compute_mode.<family>` | T | `LDC_COMPUTED` (non-Finbyx) / `FX_SOURCED` (Finbyx LDC modes) | Enum | CFO + CRO (maker-checker) |
| `ral.capital.profile` | G | Resolved | Override only CCO + CFO with reason | — |
| `ral.capital.board_buffer_bps` | T | CRAR 200, Tier 1 100 | ≥ 0 | Board via RAS |
| `ral.capital.red_band_bps` | T | 100 | 25–300 | CRO |
| `ral.capital.bl_leverage_alert` | T | 6.5 | < 7 | CRO |
| `ral.capital.shadow_frequency` | T | WEEKLY (LDC), DAILY (FX) | DAILY/WEEKLY/MONTHLY | CFO |
| `ral.dq.tb_tolerance_inr` | T | 100000 | ≥ 0; floor via G pack | Data steward |
| `ral.dq.unclassified_ead_max_pct` | G | 0.1 | ≤ 0.1 for regulatory runs | — |
| `ral.alm.early_warning_pct` | T | 80 | 50–95 | ALCO |
| `ral.alm.lcr_internal_floor_pct` | T | 110 | ≥ 100 | ALCO |
| `ral.alm.sls_limits` | L | 10/10/20 | — | Rule pack |
| `ral.alm.behavioural_requires_approval` | G | true | — | — |
| `ral.concentration.early_warning_pct` | T | 90 | 50–99 | CRO |
| `ral.stress.fx_mode` | G | CONSUME_ONLY | CONSUME_ONLY / LOCAL_RUN / REMOTE_RUN | Platform (after Ecosystem change) |
| `ral.stress.max_horizon_quarters` | T | 12 | 1–20 | CRO |
| `ral.stress.approved_immutable` | L | true | — | — |
| `ral.icaap.host` | T | per FR-P09-43 | LDC / FINBYX | CRO + CFO |
| `ral.icaap.cycle` | T | ANNUAL as of 31 Mar | — | Board |
| `ral.icaap.oprisk_proxy` | T | 15% of 3-yr avg positive gross income | Labelled internal | CRO |
| `ral.icaap.timers_days_before_board` | T | freeze 45, CRO 20, RMC 14, pack 7 | — | CS |
| `ral.pca.proximity_bps` | T | 150 | 50–300 | CRO |
| `ral.pca.forecast_horizon` | T | NEXT_FY_END | — | CRO |
| `ral.bank.oprisk_2027.enabled` | G | OFF → parallel from 1 Oct 2026 [REC] | — | Platform content |
| `ral.dashboard.personal_threshold_direction` | L | tighter_only | — | — |
| `ral.export.watermark` | T | ON | — | Tenant admin |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `ral.ai.autonomy_ceiling` | G | L2 (text) / L1 (calibration) | L0–L2 | CRO with `ten_admin` |
| `ral.rollforward.version_policy` | T | SAME_VERSIONS | SAME_VERSIONS / CURRENT_VERSIONS | CRO |
| `ral.rollforward.materiality_bps` | T | 50 bps | 10–200 bps | CRO, CFO |
| `ral.auto_runs.schedule` | T | monthly, T+5 working days | cron within business days | CRO |
| `ral.dq.min_score_to_certify` | T | 90 | 70–100 | CFO |
| `ral.internal_metrics.max_per_tenant` | G | 200 | 50–1,000 | Platform |
| `ral.capital_plan.warning_horizon_quarters` | T | 4 | 2–8 | CRO |
| `ral.sandbox.enabled` | T | ON | ON/OFF | CRO |

---

## 10. Security, privacy and audit

- Lab data is financial and, for loan-level uploads, potentially personal: loan-level templates accept only pseudonymised ids (hash with tenant salt in the browser before upload, or tenant-side), no names/PAN/phone/Aadhaar; schema validation rejects PII patterns (NN-12, NN-23).
- RLS and ABAC by legal entity; ICAAP and capital plans are "board-confidential" by default until approved (NN-13 class) — visible to CRO, CFO, CEO/MD, CS, committee members and named analysts.
- Every run, certification, scenario approval, metric change and PCA state change is ledgered (NN-02); corrections via new runs or Correction Entries (D-02).
- Reproducibility (NN-22): runs pin kernel, rule-pack, model and scenario versions and the snapshot hash; monthly reproducibility job.
- Supervisor/auditor access by D-12 grants; exports watermarked; download events logged.
- India residency (NN-24); market-data licences respected (no redistribution).

---

## 11. AI touchpoints and guardrails

| Touchpoint | Vidhi action | Guardrail |
|---|---|---|
| Data-quality explanation | Explains failed DQ rules in plain language with row references | Read-only; suggestions only |
| Template mapping | Proposes column mapping for a new LMS export to the canonical template | Human confirms; saved as mapping profile version |
| Scenario design | Drafts scenario rationale and suggests shock calibrations from the tenant's history and library defaults with citations (RBI FSR, BCBS) | Numbers proposed, never auto-applied; CRO approves scenario version |
| ICAAP narratives | Drafts section text aligned to template and last approved ICAAP; tracked changes are written by the P07 deterministic redline engine, not by Vidhi | Draft; tables are bound to certified runs, not generated; any figure quoted in text must match lineage or the paragraph is blocked (NN-37); Board approval required |
| Variance explanations | Drafts Schedule III > 25% change explanations and ratio commentary | Human edit; linked to computed values |
| Reverse-stress plausibility | Drafts plausibility narrative | CRO edits |
| "Ask the Lab" | Answers "why did CRAR fall 80 bps?" from RWA walk and capital build-up | Answers only from computed lineage; cites run ids |

Vidhi never certifies a value, approves a scenario, changes a threshold or sets PCA state (NN-14, NN-38), and no Vidhi-generated figure enters a capital run, ratio, stress result or ICAAP table (NN-37). All Lab functions work with Vidhi disabled.

---

## 12. Acceptance criteria (Gherkin; `tests/acceptance/p09/*.feature`)

```gherkin
Feature: Capital profile resolution
  Scenario Outline: Minimums by profile
    Given a tenant with profile "<profile>"
    When the capital engine resolves minimums
    Then the binding ratio is "<ratio>" with minimum "<min>" and citation "<cite>"
    Examples:
      | profile                   | ratio            | min   | cite                              |
      | NBFC-BL non-gold          | Leverage         | 7     | RBI/DOR/2025-26/345 para 17       |
      | NBFC-ML ICC               | Tier 1           | 10%   | RBI/DOR/2025-26/345 para 6(2)     |
      | NBFC-UL ICC               | CET1             | 9%    | RBI/DOR/2025-26/345 para 6(4)     |
      | Gold-loan NBFC BL         | Tier 1           | 12%   | RBI/DOR/2025-26/345 para 6(1)     |
      | UCB Tier 3                | CRAR             | 12%   | RBI/DOR/2025-26/275 para 9        |
      | Commercial bank           | CET1 + CCB       | 8%    | RBI/DOR/2025-26/151 para 11       |

  Scenario: BL tenant shows no CRAR and no op-risk RWA
    Given an NBFC-BL non-gold tenant
    Then the capital screen shows leverage and no CRAR
    And no operational-risk RWA line exists for any NBFC profile

Feature: Snapshot reproducibility
  Scenario: Re-running a certified run on its snapshot reproduces it
    Given capital run 1 certified on frozen snapshot S with hash H
    When the run is recomputed with the same kernel and rule-pack versions
    Then every output equals run 1 to the last decimal

  Scenario: Editing source after freeze does not change ICAAP tables
    Given ICAAP cycle C in state "DATA_FROZEN" on snapshot S
    When a new TB upload arrives for the same as-of date
    Then ICAAP tables still bind to S and a banner offers "Re-freeze (CRO approval required)"

Feature: Data quality gate
  Scenario: Unreconciled loan book blocks regulatory certification
    Given loan-segment outstanding differs from TB loan accounts by ₹25,00,000 with tolerance ₹1,00,000
    When the CFO tries to certify the quarterly capital run
    Then certification fails with "LDC-RAL-012 Reconciliation break above tolerance"

Feature: LCR arithmetic
  Scenario: Inflow cap applied
    Given HQLA after haircuts 50, outflows 100 and inflows 120 for the next 30 days
    When LCR is computed
    Then net outflows are 28.75 and LCR is 173.91%

Feature: Finbyx-sourced values
  Scenario: Certified Finbyx CRAR is displayed, not recomputed
    Given compute mode "capital" is FX_SOURCED
    When CapitalRatioComputed arrives with CRAR 17.42% and certification CERTIFIED
    Then the CFO tile shows 17.42% with badge "FX" and no LDC capital run is created

Feature: Stress testing
  Scenario: Approved scenario is immutable
    Given scenario "SCN-CRD-03 v2" is RMC_APPROVED
    When an analyst edits a shock magnitude
    Then version 3 is created in DRAFT and v2 stays unchanged

  Scenario: Reverse stress converges
    Given a seeded NBFC-ML book with CRAR 19.0%
    When reverse stress targets CRAR = 15.0% on factor "default-rate multiplier"
    Then the result converges within ±1 bp and the convergence log is stored

Feature: ICAAP
  Scenario: Cannot reach CRO review without frozen data
    Given an ICAAP cycle in "ASSESSED" without a frozen snapshot
    When the risk function submits to CRO
    Then the transition is rejected with "LDC-RAL-031"

  Scenario: Tracked changes against last year
    Given last year's ICAAP v2025 is approved
    When Vidhi drafts section 4 for FY2026-27
    Then the DOCX contains tracked insertions and deletions against v2025 and is marked "Draft — not approved"

Feature: PCA
  Scenario: Threshold boundary values
    Given an NBFC-ML ICC in scope of PCA
    Then CRAR 12.0% maps to RT1 and 11.99% to RT2
    And NNPA 6.0% is outside PCA and 6.01% is RT1
    And for a CIC, leverage 2.5x is RT1

  Scenario: System never places PCA
    Given computed CRAR crosses RT1
    Then PCA state becomes THRESHOLD_CROSSED and a limit episode opens
    And no restriction applies until the CS records RBI's letter
```

NN tests: `NN-22_capital_reproducible`, `NN-22_decimal_precision`, `NN-07_snapshot_immutable`, `NN-12_loan_template_rejects_pii`, `NN-13_icaap_board_confidential`, `NN-14_vidhi_cannot_certify`, `NN-23_no_formula_push_to_finbyx`, `NN-05_certifier_not_preparer`, `NN-08_no_auto_submission_icaap`.

```gherkin
# v1.1 scenarios
Feature: Result cards bind figures (NN-37)
  Scenario: Edited figure blocks export
    Given a certified stress run with stressed CRAR 14.2%
    And Vidhi rephrases the card summary
    When a user edits the summary text to say "CRAR remains above 15%"
    Then the narrative check fails because "15%" is not a bound value of the run
    And the card cannot be added to a board pack

Feature: Reproducible re-run
  Scenario: Re-run as at
    Given capital run CR-2026-09 with snapshot hash H1 and kernel 3.4.1
    When "Re-run as at" is executed
    Then every output value equals the original to the last decimal place

Feature: Internal metrics never override regulatory metrics
  Scenario: Attempt to redefine CRAR
    When a tenant creates an internal metric with code "R1"
    Then the request is rejected with "LDC-RAL-060"

Feature: Sandbox isolation
  Scenario: Sandbox results excluded from packs
    Given a sandbox session with gold price −35%
    When the CRO tries to add the sandbox chart to the RMC pack
    Then the action is blocked with message "Uncertified sandbox results cannot enter packs"

Feature: Capital-plan early warning
  Scenario: Projected headroom below buffer
    Given a Board buffer of 200 bps above the CRAR minimum
    When the roll-forward projects headroom of 120 bps in Q3
    Then an EWS card with trigger family "capital plan" appears for the CRO in P08
```

---

## 13. Deliverables and exit gate

- `ral` module; kernel integration (`infrabyx-risk-kernel` pinned) with golden fixtures shared with Finbyx CI; rule packs: NBFC CAP 2025, UCB CAP 2025, Bank CAP 2025 (+ 2027 parallel pack), NBFC ALM 2025, NBFC CON 2025, NBFC MSD 2026 PCA, CIC, HFC, ARC, insurer solvency; Lab templates (11) with `_Template_Info`; ratio library of 125 metrics; scenario library of 46; ICAAP templates (NBFC nine-part, bank, light); 15 KMP role templates.
- Screens SCR-RAL-01 to SCR-RAL-22; user guides and P23 tutorial scripts ("Your first capital run", "Running a stress test", "ICAAP in 15 days", "Reading the ALM statement").
- `docs/phases/P09-plan.md` with inventories; model-validation file for each Lab model; reproducibility report.
- **Exit gate:** §12 scenarios and NN tests green; three pilots end to end — (1) NBFC-ML on a third-party LMS: upload → certified CRAR, SLS, IRS, concentration, 40 ratios, stress (5 scenarios + reverse), ICAAP Board-approved DOCX/PDF; (2) Finbyx NBFC in `LDC_EXTERNAL`: values flow from events, ICAAP hosted in LDC, no recomputation; (3) listed corporate: Schedule III ratios and scenario analysis; ICAAP export opens in Word/Excel without LDC; reviewer (CA/actuarial) sign-off on engines.

- *(v1.1)* Internal-metric builder; 16 additional scenarios with fixtures; result cards with narrative check; roll-forward and re-run-as-at; what-if sandbox; capital-plan EWS feed to P08; shared intake with P11; group view. **Exit gate addition:** the pilot NBFC-ML rolls forward one quarter in one click, exports result cards into the RMC pack via P28, and a re-run-as-at reproduces the prior quarter exactly.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P09-01 | NBFC CAP Directions 2025 Chapter V ICAAP paragraph numbers (para 54 cited via Finbyx) | Chapter V text not retrieved | Platform content (RBI) | Cite "Chapter V" until verified |
| OI-P09-02 | Bank leverage-ratio minimums, D-SIB surcharges, CCyB rate, Pillar 3 templates and ICAAP format headings in RBI/DOR/2025-26/151 | Not extracted | Platform content (RBI) | Bank rule pack ships `[VERIFY]` values behind `ral.bank.enabled = OFF` until verified |
| OI-P09-03 | Bank 1 Apr 2027 credit/market/operational-risk rule changes (effective dates, BI coefficients) | Read from Finbyx v1.5 | Platform content (RBI) | Parallel pack only; not used for regulatory output |
| OI-P09-04 | SFB, PB, RRB capital minimums | Not verified | Platform content (RBI) | Family disabled until verified |
| OI-P09-05 | ARC Directions 2025 reference number, CRAR paras and SR investment rule | Secondary source only | Platform content (RBI) | ARC pack [VERIFY] |
| OI-P09-06 | IFSCA FC/FU capital adequacy numbers (circular 6 May 2021; banking directions 4 Dec 2020) | Not extracted | Platform content (IFSCA) | IFSCA capital as `IMPORTED_RESULT` |
| OI-P09-07 | Insurer Ind-RBC timeline and IRDAI stress-testing/FCR requirements | Ind-RBC not final | Platform content (IRDAI) | Solvency imported; control level 150% |
| OI-P09-08 | CIC asset composition tests and leverage definitions in CIC Directions 2025 (RBI/DOR/2025-26/367, updated 10 Mar 2026) | Not re-fetched | Platform content (RBI) | [VERIFY] |
| OI-P09-09 | RBI AIF-investment circulars as revised (2023, 2024, 2025) | Revisions after mid-2025 not verified | Platform content (RBI) | Compliance check flagged [VERIFY] |
| OI-P09-10 | NBFC Concentration Directions paras (13–14, 33–35, 39, 11–12, 24) | Read via Finbyx | Platform content (RBI) | [VERIFY] |
| OI-P09-11 | Bank IRRBB instrument and prescribed shock scenarios | Not verified | Platform content (RBI) | Bank IRRBB behind flag |
| OI-P09-12 | Schedule III ratio list and > 25% explanation rule (MCA notification 24 Mar 2021) as currently in force | Verify current text | Platform content (MCA) | Corporate ratio pack [VERIFY] |
| OI-P09-13 | Ecosystem change requests: `RiskSegmentSnapshotPublished` event and Finbyx `POST /v1/risk/stress-runs` | Requires Spec §14.2 change process and Finbyx approval | Integration lead + owner | `ral.stress.fx_mode = CONSUME_ONLY` |
| OI-P09-14 | Shared `infrabyx-risk-kernel` package ownership and release process | D-22 adopted (`02` §2.3); ownership, repository and release cadence still to be set | Owner / CTO | LDC vendors a pinned copy of Finbyx RK6 formulas with shared fixtures |
| OI-P09-15 | Market-data licensing for VaR/investment stress | Vendor licence terms | Procurement | Tenant-supplied prices only |
| OI-P09-16 | UCB PSL target and UCB liquidity/ALM directions references | Not verified | Platform content (RBI) | [VERIFY] |
| OI-P09-17 *(v1.1)* | Indian implementation of BCBS IRRBB standardised shock scenarios in the Commercial Banks directions | Not verified | Platform content (RBI) | Scenarios available as "voluntary/management" |
| OI-P09-18 *(v1.1)* | NGFS scenario parameters licence and version for SCN-CLM-03 | Licence/terms to check | CRO pilot, legal | Generic transition shock only |
| OI-P09-19 *(v1.1)* | Sandbox performance target on large books (2 million accounts) | Needs load test | Platform engineering | Segment-level aggregation only |
| OI-P09-20 *(v1.1)* | Group consolidation rules for NBFC groups/CIC groups | Legal definitions per directions | Platform content (RBI) | Informational view only |
| OI-P09-21 *(v1.1)* | Foreign-subsidiary prudential packs (IFRS 9, local Basel) | Depends on P25 reviewed packs | P25 content partners | IMPORTED_RESULT mode |
| OI-P09-22 *(v1.1)* | Calibration back-test thresholds for AI-proposed parameters | Methodology to approve | CRO, model validator | Proposals disabled until approved |

---

## 15. Sources (accessed 25 October 2026)

1. RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/345 — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=12959
2. RBI (Commercial Banks – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/151 (updated 7 Oct 2026) — https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13159 ; PDF https://rbidocs.rbi.org.in/rdocs/notification/PDFs/151MD.PDF
3. RBI (UCB – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/275 — https://rbi.org.in/SCRIPTS/BS_ViewMasDirections.aspx?id=13030
4. RBI (NBFC – Asset Liability Management) Directions, 2025, RBI/DoR/2025-26/355 — https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=12949
5. RBI (NBFC – Concentration Risk Management) Directions, 2025, RBI/DOR/2025-26/351 — https://rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=12953
6. RBI (NBFC – Miscellaneous) Supervisory Directions, 2026, RBI/DoS/2026-27/467 — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13586
7. RBI (NBFC – Fraud Risk Management) Directions, 2026, RBI/DoS/2026-27/463 — https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13590
8. RBI draft Guidance on Regulatory Principles for Model Risk Management (24 Jun 2026) — https://rbi.org.in/ScriptS/BS_PressReleaseDisplay.aspx?prid=63006
9. IFSCA circular on FC prudential regulation (3 May 2021) — https://www.ifsca.gov.in/Document/Legal/circular-on-fc-prudential-regulation-and-activity-specific-regulation03052021072520.pdf ; capital requirement circular (6 May 2021) — https://www.ifsca.gov.in/Document/Legal/circular-on-fc-capital-requirement06052021092840.pdf
10. IRDAI (Actuarial, Finance and Investment Functions of Insurers) Regulations, 2024 — summary https://www.oquilia.com/news/irdai-actuarial-finance-investment-functions-regulations-2024 ; Ind-RBC QIS — https://mallowstreet.com/Article/b72602
11. ARC Directions 2025 summary — https://ksandk.com/newsletter/rbi-asset-reconstruction-companies-2025/
12. BCBS Basel Framework (SRP, DIS) — https://www.bis.org/basel_framework/ ; BCBS 239 progress report — https://www.bis.org/bcbs/publ/d559.htm
13. RBI Financial Stability Report, June 2026 (30 Jun 2026) — summary https://elplaw.in/wp-content/uploads/2026/07/Financial-stability-report-June-2026-some-important-takeaways.pdf
14. Finbyx Master Prompt v1.5 Part 7E RK3–RK8; Infrabyx Ecosystem Integration Specification v1.1 §6.22, §6.25, §9 — owner's corpus.
15. Vinod Kothari Consultants, "Mind the Gap: Plugging Risk Blind Spots with ICAAP for NBFCs" (Jul 2025) — https://vinodkothari.com/2025/07/mind-the-gap-plugging-risk-blind-spots-with-icaap-for-nbfcs/ ; KPMG India ICAAP tool — https://kpmg.com/in/en/services/advisory/consulting/risk-and-finance-advisory/unlocking-value-with-technology/financial-risk.html

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-37, NN-38, NN-39; X-16, X-25; MFI qualifying-asset value per OI-H-01 (master §7).

**Added in v1.1:** NN-47; X-43.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
