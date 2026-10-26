# Appendix H — Risk Taxonomy, Basel Mapping, ICAAP, Stress Scenarios and Ratio Library

> **Binding for:** P08 (Enterprise Risk Management and CRO Workspace) and P09 (Risk Assessment Lab). Also read by P04 (control links), P10 (risk-based audit universe), P11 (shared return elements), P12 (cyber/TPRM KRIs), P13 (people metrics), P15 (entity-family profiles), P17 (Vidhi risk notebooks) and P23 ("i" glossary).
>
> **Status:** v1.0, 25 October 2026. Values marked **[VERIFY]** must be re-checked against the primary instrument before the rule pack that uses them is activated (NN-06; Appendix W). Metric IDs R1–R57 are the canonical Finbyx v1.5 RK6.2 identifiers and must not be renumbered; LDC extensions start at R58. The shared `infrabyx-risk-kernel` (P09 FR-P09-07) is the executable source of every formula in §H.6; this appendix is its human-readable specification.
>
> **Precedence:** primary regulation (as recorded in Appendix G) → this appendix → phase files. Where Finbyx v1.5 Part 7E and this appendix differ on a shared metric, raise a cross-product issue; until resolved the kernel fixture wins.

> **v1.1 changes (25 October 2026)** — §H.0A metric ownership between P09 and P28; §H.6.3 aggregation and currency rules for group metrics; §H.8.4 fifteen new KRIs (CCM coverage, automated-test failures, data quality, AI/model risk, cloud and co-lending concentration, high-risk non-compliance, regulator observations, projected capital headroom, physical-climate exposure, foreign-entity reds) bringing the seed library to 187; §H.8.5 early-warning trigger library used by P08 FR-P08-61; §H.9.1 sixteen new scenarios (ten named plus the six BCBS IRRBB shocks) bringing the library to 62; §H.2.5 international corporate taxonomy pack `TAX-INTL-CORP` (P25). All additions marked *(v1.1)*.

---

## H.0 How the pieces fit

```
Entity profile (P15) ──► Applicability resolver (P02 rule engine)
        │                       │
        ▼                       ▼
Taxonomy pack(s) §H.2   Governance requirements §H.4   Capital profile §H.7   Ratio set §H.6
        │                       │                            │                    │
        ▼                       ▼                            ▼                    ▼
Risk register / RCSA (P08)   Committees & policies (P06/P07)   Capital engine (P09)   KRIs §H.8 → RAS (P08)
        │                                                    │                    │
        └──────────────► Stress scenarios §H.9 ──► ICAAP §H.10 ◄─────────────────┘
                                   │
                                   ▼
                        Pillar 3 / public disclosures (P08 §4L)
```

Design rules: (1) Level-1 categories are locked per pack version; levels 2–3 are tenant-editable (NN-28). (2) Every regulatory threshold is typed `regulatory` and comes from a Governed rule pack; tenants add Board/management thresholds only. (3) A metric shows "compliant" only after applicability, completeness, data quality and certification (P09 FR-P09-18). (4) Pillar 3 is a disclosure framework, not a list of risk types.

### H.0A Metric ownership and exposure *(v1.1)*

| Layer | Owner | What it does | What it never does |
|---|---|---|---|
| Kernel formulas and regulatory thresholds | `infrabyx-risk-kernel` (D-22) | Formulas R1–R125, capital rules, ALM maths, PCA thresholds | Tenant edits |
| Metric definitions, versions, runs, certification | P09 (`ral`) | Computes, validates, certifies values with lineage; internal metrics by tenants (P09 FR-P09-60) | Display-only shortcuts |
| KRIs, thresholds, breach episodes | P08 (`erm`) | Observes metrics against appetite; EWS (§H.8.5) | Computing regulatory metrics |
| Semantic layer, dashboards, packs | P28 (`rpt`) | Exposes certified/indicative values read-only with version, provenance and certification badge; composes dashboards and packs | Computing or overriding a metric value |

---

## H.1 Basel framework primer and Indian implementation

### H.1.1 The three pillars

| Pillar | What it is (BCBS Basel Framework) | Product implication |
|---|---|---|
| **Pillar 1 — minimum capital requirements** | Capital charges for credit risk (standardised or IRB), counterparty credit risk and CVA, market risk (FRTB standardised/IMA), operational risk (standardised approach: Business Indicator Component × Internal Loss Multiplier), plus the leverage ratio and buffers (CCB, CCyB, G-SIB/D-SIB) | P09 capital engines by family; NBFCs carry **credit risk only** in Pillar 1 under RBI rules (no op/market charge) |
| **Pillar 2 — supervisory review process (SRP)** | Bank's ICAAP and supervisor's SREP; covers risks not (fully) captured in Pillar 1: concentration, IRRBB (SRP31), liquidity, residual (CRM), securitisation, reputational, strategic/business, model, pension, climate, and the quality of risk management; stress testing; capital planning | P09 ICAAP; Pillar 2 add-ons; P08 framework; RBI SREP for banks (Commercial Banks CA Directions 2025 Ch V A–D); NBFC-ML+ ICAAP (NBFC CAP Directions 2025 Ch V) |
| **Pillar 3 — market discipline (DIS)** | Public disclosure templates and tables: key metrics (KM1), overview of RWA (OV1), composition of capital (CC1/CC2), credit risk (CR1–CR10), CCR, securitisation (SEC), market risk (MR), operational risk (OR), IRRBB (IRRBB1), liquidity (LIQ1 LCR, LIQ2 NSFR), leverage (LR1/LR2), remuneration (REM), plus the voluntary climate disclosure framework (June 2025) [VERIFY template codes against current DIS] | P08 §4L disclosure workspace (banks); NBFCs use notes-to-accounts disclosures instead (no NBFC Pillar 3) |

**BCBS 239** (Principles for effective risk data aggregation and risk reporting, January 2013; 14 principles: governance and infrastructure (1–2), risk data aggregation capabilities — accuracy and integrity, completeness, timeliness, adaptability (3–6), risk reporting practices — accuracy, comprehensiveness, clarity and usefulness, frequency, distribution (7–11), supervisory review (12–14)). Formally addressed to G-SIBs/D-SIBs; LDC uses it as a design reference for the P09 data-quality dashboard and lineage, never as a compliance claim (NN-19).

### H.1.2 Indian implementation by entity family (as at 25 Oct 2026)

| Family | Pillar 1 in India | Pillar 2 | Pillar 3 / disclosure | Primary instrument(s) |
|---|---|---|---|---|
| Commercial banks (excl. SFB/PB/LAB variants) | Credit SA, market risk, op risk; CET1 5.5% / T1 7% / total 9% + CCB 2.5%; D-SIB; CCyB; leverage | ICAAP + SREP; stress testing (Annex IV) | Pillar 3 (Ch V.E, Annex III); leverage disclosure (Ch VII.E–F) | RBI (Commercial Banks – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/151 (updated 7 Oct 2026) |
| SFBs, PBs, RRBs, LABs | Family-specific capital directions | Per directions [VERIFY] | Per directions [VERIFY] | SFB Prudential Norms on Capital Adequacy Directions 2025 and others [VERIFY] |
| UCBs | Credit RWA; CRAR 9% (Tier 1 UCB) / 12% (Tiers 2–4); net worth floors | Not mandated as ICAAP [VERIFY] | Notes to accounts | RBI (UCB – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/275 |
| NBFC-ML and above | Credit RWA only; CRAR 15%, T1 10%; UL CET1 9% | ICAAP mandatory, Pillar 2 capital not insisted upon | Notes to accounts (FS Directions 2025, RBI/DOR/2025-26/359) | RBI (NBFC – Prudential Norms on Capital Adequacy) Directions, 2025, RBI/DOR/2025-26/345 |
| NBFC-BL | Leverage ≤ 7 (non-gold-primary) | Not mandated | Notes to accounts | same, paras 4(7), 17 |
| CIC | ANW/RWA ≥ 30%; leverage ≤ 2.5× | ICAAP per layer | Notes | RBI (Core Investment Companies) Directions, 2025, RBI/DOR/2025-26/367 |
| ARC | CRAR 15%; NOF ₹300 crore | Voluntary | Notes | RBI (Asset Reconstruction Companies) Directions, 2025 [VERIFY ref] |
| Insurers | Factor-based solvency (ASM/RSM ≥ 150% control level); Ind-RBC under development | Own risk and solvency practices [VERIFY] | IRDAI public disclosures | Insurance Act 1938 s.64VA; IRDAI (Actuarial, Finance and Investment Functions of Insurers) Regulations, 2024 |
| IFSCA FC/FU, IBUs | Per IFSCA banking directions applied mutatis mutandis [VERIFY numbers] | [VERIFY] | [VERIFY] | IFSCA circulars 3 May 2021, 6 May 2021; Directions 4 Dec 2020 |
| MF AMCs / AIFs / intermediaries | Net-worth floors; investment and leverage limits | Risk management frameworks (SEBI) | Scheme disclosures | SEBI (Mutual Funds) Regulations, 2026 (replaced the 1996 Regulations from 1 Apr 2026) and MF Master Circular; AIF Regulations 2012 and Master Circular [VERIFY] |
| Companies / LLPs | None | None | Board report risk statement; Schedule III ratios | Companies Act 2013 s.134(3)(n), Schedule III; LODR for listed |
| Credit co-operative societies | None (RBI) | None | State audit reports | MSCS Act 2002; State Co-operative Societies Acts |

---

## H.2 Risk taxonomy packs

### H.2.1 Master Level-1 / Level-2 catalogue

Codes are stable; packs (§H.2.2) select subsets. L3 is tenant-defined (seed examples given).

| L1 code | Level 1 | Level 2 (seed) | L3 examples (seed, tenant-editable) |
|---|---|---|---|
| CRD | Credit risk | CRD.01 Default risk (retail); CRD.02 Default risk (MSME/corporate); CRD.03 Migration/downgrade; CRD.04 Collateral/recovery (LGD); CRD.05 Restructuring and forbearance; CRD.06 Provisioning adequacy (IRACP/ECL); CRD.07 Underwriting/policy deviation; CRD.08 Co-lending/partner credit; CRD.09 Product-specific (gold, LAS, MFI, vehicle, LAP, HL, credit card) | Gold price fall; JLG group default; LAS margin shortfall |
| CON | Concentration risk | CON.01 Single counterparty; CON.02 Group/connected; CON.03 Sector; CON.04 Geography/state; CON.05 Product; CON.06 Funding source; CON.07 Channel/LSP/DSA; CON.08 Collateral type | Top-20 exposure; state > 30% of book |
| CCR | Counterparty credit risk | CCR.01 Derivatives; CCR.02 Securities financing; CCR.03 Settlement | Bank only by default |
| MKT | Market and investment risk | MKT.01 Equity price; MKT.02 Interest-rate (trading/investment); MKT.03 Credit spread; MKT.04 FX; MKT.05 Commodity (incl. gold inventory); MKT.06 Valuation (Level 3); MKT.07 IPO/lock-in; MKT.08 AIF/REIT/InvIT unit risk | SME IPO exposure; Cat III AIF units |
| IRB | Interest-rate risk in the banking book | IRB.01 Repricing gap; IRB.02 Yield curve; IRB.03 Basis; IRB.04 Optionality (prepayment, deposit withdrawal) | Floating-to-fixed mismatch |
| LIQ | Liquidity and funding risk | LIQ.01 Structural mismatch; LIQ.02 Short-term/LCR; LIQ.03 Funding concentration; LIQ.04 Rollover/refinancing; LIQ.05 Market liquidity of assets; LIQ.06 Intraday/settlement; LIQ.07 Contingent liquidity (undrawn, guarantees, DLG) | CP rollover failure |
| CAP | Capital and solvency risk | CAP.01 Capital adequacy; CAP.02 Leverage; CAP.03 Capital planning/raising; CAP.04 Solvency (insurers); CAP.05 Net-worth floor | Glide-path miss (UCB net worth) |
| OPR | Operational risk (Basel event types §H.5) | OPR.01–OPR.07 = Basel L1 event types | — |
| CYB | Cyber and technology risk | CYB.01 Cyber attack (ransomware, DDoS, intrusion); CYB.02 Data breach; CYB.03 IT availability/outage; CYB.04 Change and patch; CYB.05 Access management; CYB.06 Cloud and SaaS; CYB.07 Digital payments/channel security; CYB.08 AI system security | Core LMS outage > 4 hours |
| TPR | Third-party and outsourcing risk | TPR.01 Material outsourcing; TPR.02 IT outsourcing/cloud; TPR.03 LSP/DSA/recovery agents; TPR.04 Fourth-party; TPR.05 Vendor concentration; TPR.06 Intra-group outsourcing | Single cloud region |
| MOD | Model risk | MOD.01 Credit scoring/PD; MOD.02 ECL; MOD.03 Pricing; MOD.04 ALM behavioural; MOD.05 Fraud/AML; MOD.06 AI/LLM features; MOD.07 Stress/ICAAP models; MOD.08 Vendor models | Drift in scorecard Gini |
| CMP | Compliance and legal risk | CMP.01 Regulatory breach; CMP.02 Reporting/returns accuracy; CMP.03 KYC/AML compliance; CMP.04 Data-protection compliance; CMP.05 Litigation; CMP.06 Contractual; CMP.07 Licensing/registration; CMP.08 Tax | Late CIMS return |
| CND | Conduct risk | CND.01 Mis-selling; CND.02 Fair practices/pricing; CND.03 Recovery conduct; CND.04 Grievance handling; CND.05 Disclosure (KFS/MITC); CND.06 Vulnerable customers; CND.07 Market conduct (front-running, insider trading) | Recovery calls outside hours |
| FRD | Fraud and financial-crime risk | FRD.01 Internal fraud; FRD.02 External/borrower fraud; FRD.03 Identity/synthetic fraud; FRD.04 Digital payment fraud; FRD.05 Money laundering/terrorist financing; FRD.06 Sanctions; FRD.07 Bribery/corruption | Fake gold; mule accounts |
| STR | Strategic and business risk | STR.01 Business model; STR.02 Competition and pricing; STR.03 Growth/execution; STR.04 M&A; STR.05 Regulatory change (layer migration, new rules); STR.06 Technology disruption; STR.07 Earnings volatility | Upper-layer listing deadline |
| REP | Reputational risk | REP.01 Media/social media; REP.02 Customer trust; REP.03 Regulatory action publicity; REP.04 Partner association | Viral complaint |
| GRP | Group and contagion risk | GRP.01 Parent/sponsor support; GRP.02 Intra-group exposure; GRP.03 Shared services; GRP.04 Step-in risk | Sister-company default |
| PPL | People risk | PPL.01 Key-person dependency; PPL.02 Attrition/capacity; PPL.03 Competence and training; PPL.04 Conduct/integrity of staff; PPL.05 Labour-law compliance; PPL.06 Health and safety; PPL.07 Workplace harassment (POSH — counts only); PPL.08 Succession; PPL.09 Remote-work controls | CRO vacancy |
| DPR | Data-privacy risk | DPR.01 Lawful basis/consent; DPR.02 Notice and rights; DPR.03 Breach; DPR.04 Cross-border; DPR.05 Retention; DPR.06 Children's data; DPR.07 Processor management | DPDP consent gaps |
| RES | Resilience and continuity risk | RES.01 Critical operation disruption; RES.02 Impact-tolerance breach; RES.03 Site/branch disruption; RES.04 Pandemic/natural disaster; RES.05 Supplier disruption | Branch flood |
| ESG | ESG and climate risk | ESG.01 Physical climate; ESG.02 Transition climate; ESG.03 Environmental; ESG.04 Social; ESG.05 Governance/disclosure (BRSR) | Coastal-state exposure |
| GOV | Governance risk | GOV.01 Board effectiveness; GOV.02 Committee composition; GOV.03 Related-party transactions; GOV.04 Fit-and-proper; GOV.05 Election/office-bearer (co-op); GOV.06 Member relations (co-op) | Quorum failures |
| INS | Insurance risk | INS.01 Underwriting/pricing; INS.02 Reserving; INS.03 Catastrophe; INS.04 Mortality/longevity; INS.05 Morbidity; INS.06 Lapse/persistency; INS.07 Reinsurance; INS.08 Expense | Cat event in coastal states |
| ARC | Asset-reconstruction specific | ARC.01 Acquisition pricing/valuation; ARC.02 Resolution and realisation; ARC.03 SR investment and NAV; ARC.04 Legal enforcement (SARFAESI/IBC/DRT); ARC.05 Sponsor/originator conflicts | Resolution > 5 years |
| FND | Fund/scheme risk (AMC/AIF) | FND.01 Scheme liquidity/redemption; FND.02 Portfolio concentration; FND.03 Valuation; FND.04 Leverage (Cat III); FND.05 Investor-class/conflict; FND.06 Trustee oversight | Redemption pressure in credit fund |

### H.2.2 Pack membership (● core, ○ optional/if applicable, — not enabled)

| L1 | TAX-BANK | TAX-UCB | TAX-NBFC | TAX-ARC | TAX-COOP | TAX-IFSCA | TAX-SEBI-MF | TAX-SEBI-AIF | TAX-SEBI-LISTED | TAX-SEBI-INT | TAX-INS | TAX-INS-INT | TAX-CORP | TAX-LLP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| CRD | ● | ● | ● | ● | ● | ● | ○ | ○ | ○ | ○ | ○ | — | ○ | ○ |
| CON | ● | ● | ● | ● | ● | ● | ○ | ● | ○ | ○ | ○ | ○ | ○ | ○ |
| CCR | ● | ○ | ○ | — | — | ○ | ○ | ○ | ○ | ○ | ○ | — | — | — |
| MKT | ● | ○ | ● (ICC/CIC) / ○ | ○ | ○ | ● | ● | ● | ○ | ● | ● | — | ○ | ○ |
| IRB | ● | ● | ● | ○ | ○ | ● | ○ | — | ○ | — | ○ | — | ○ | — |
| LIQ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● | ● |
| CAP | ● | ● | ● | ● | ○ | ● | ○ | — | ○ | ○ | ● | ○ | — | — |
| OPR | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| CYB | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| TPR | ● | ● | ● | ● | ○ | ● | ● | ● | ● | ● | ● | ● | ● | ○ |
| MOD | ● | ○ | ● | ○ | — | ○ | ○ | ○ | ○ | ○ | ● | — | ○ | — |
| CMP | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| CND | ● | ● | ● | ● | ● | ● | ● | ○ | ○ | ● | ● | ● | ○ | ○ |
| FRD | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ○ |
| STR | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| REP | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| GRP | ● | ○ | ● | ○ | — | ● | ○ | ○ | ○ | ○ | ○ | ○ | ○ | — |
| PPL | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| DPR | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |
| RES | ● | ● | ● | ● | ○ | ● | ● | ○ | ● | ● | ● | ○ | ○ | ○ |
| ESG | ○ | ○ | ○ (ICAAP-internal) | ○ | ○ | ○ | ○ | ○ | ● | ○ | ○ | — | ○ | ○ |
| GOV | ● | ● | ● | ● | ● | ● | ● | ● | ● | ○ | ● | ○ | ● | ○ |
| INS | — | — | — | — | — | ○ | — | — | — | — | ● | ○ | — | — |
| ARC | — | — | — | ● | — | — | — | — | — | — | — | — | — | — |
| FND | — | — | — | — | — | ○ (FME) | ● | ● | ○ (REIT/InvIT) | ○ (PMS) | — | — | — | — |

### H.2.3 Family-specific adjustments

- **NBFC by category:** MFI adds CRD.09 microfinance household-income and repayment-obligation limits; gold-loan books add MKT.05 gold price and CND.03 auction conduct; HFCs add LTV by size and NHB returns; CICs emphasise GRP and MKT; P2P and AA focus on CYB, CND, CMP, TPR (no credit balance-sheet risk for platforms); NOFHC focuses on GRP.
- **NBFC by layer:** BL — credit, liquidity (voluntary ALM below ₹100 crore), compliance, cyber (baseline), conduct; ML adds capital, concentration, ALM, ICAAP, model, outsourcing; UL adds large exposures, CET1, listing-related governance, enhanced disclosures.
- **UCB by tier:** Tier 1 UCBs use the "simplified" register (quick RCSA permitted); Tiers 3–4 use the full register.
- **Co-operative societies:** governance (GOV.05 elections, GOV.06 member relations), FRD.01 misappropriation by staff/office bearers and audit-observation tracking are core; capital labelled "management practice".
- **Listed companies:** ESG and cyber become core; RMC pack includes BCP and ESG items (LODR Sch II Part D(C) [VERIFY]).

### H.2.4 Cross-walk for combined packs

When two packs are active on one legal entity (e.g., listed NBFC = `TAX-NBFC` + `TAX-SEBI-LISTED`), nodes with the same L1/L2 code merge; pack-specific L2s append; the governance requirement set is the union (§H.4) with the stricter frequency winning; KRIs deduplicate by metric id. The cross-walk table is part of the pack version and is reviewed by platform content.

### H.2.5 International taxonomy pack *(v1.1)*

`TAX-INTL-CORP` (foreign subsidiaries and global groups; P25): strategic, operational, financial (liquidity, FX, interest, credit), compliance and legal (local statute register), sanctions and export controls, tax (transfer pricing, permanent establishment), data protection (GDPR/UK GDPR/PDPA/PDPL/CCPA by jurisdiction), cyber and IT, third party, people and employment law, ESG, reputational, geopolitical and country risk. Prudential country packs (local Basel, IFRS 9, insurance solvency) are added only as reviewed jurisdiction packs (NN-53).

---

## H.3 Basel mapping of Level-1 categories

| L1 | Pillar 1 (where charged) | Pillar 2 (ICAAP treatment) | Pillar 3 / disclosure link | BCBS reference |
|---|---|---|---|---|
| CRD | Credit RWA (SA) — banks, UCBs, NBFC-ML+, ARCs | Residual/credit-model risk; downturn LGD; Pillar 1 adequacy check | CR1–CR5 (banks); NBFC FS notes asset quality | CRE; SRP |
| CON | Not separately (LEF limits for banks) | Concentration add-on (HHI/granularity adjustment; sector concentration) | LE return (NBFC-UL); notes top-20 | SRP; LEX |
| CCR | CCR/CVA (banks) | — | CCR1–CCR8 | CRE5x; MAR50 |
| MKT | Market RWA (banks) | NBFC investment MTM as ICAAP-internal | MR1 | MAR |
| IRB | — | IRRBB capital (ΔEVE; NII) | IRRBB1 (banks) | SRP31 |
| LIQ | — (LCR/NSFR are minimum standards, not capital) | Liquidity buffer, not capital; funding-cost stress in P&L | LIQ1, LIQ2 (banks); NBFC ALM disclosures | LCR; NSF |
| CAP | Minimum ratios and buffers | Capital planning, buffers above minimum | KM1, CC1, OV1, LR1/LR2 | CAP; LEV |
| OPR | Op-risk capital (banks) | NBFC: internal proxy labelled "ICAAP internal"; scenario-based losses | OR1–OR3 (banks) | OPE |
| CYB | Within op risk | Scenario-based (outage, breach) | — | OPE; operational-resilience principles (2021) |
| TPR | Within op risk | Scenario-based | — | BCBS third-party risk principles (2024–25) [VERIFY] |
| MOD | — | Model-risk buffer (optional) | — | SRP |
| CMP | Within op risk (clients, products and business practices) | Scenario-based (penalty, restriction) | — | — |
| CND | Within op risk | Scenario-based | — | — |
| FRD | Within op risk | Loss distribution / scenario | — | — |
| STR | — | Scenario-based (earnings, business restriction) | — | SRP |
| REP | — | Scenario-based; step-in | — | SRP |
| GRP | — | Contagion add-on; step-in | — | Step-in risk guidelines (2017) |
| PPL | Within op risk (employment practices) | Scenario-based | REM (remuneration) | — |
| DPR | Within op risk | Scenario-based (breach cost, penalties under DPDP Act 2023 Schedule) | — | — |
| RES | Within op risk | Scenario-based; impact tolerances | — | Operational resilience principles |
| ESG | — | Climate scenario (voluntary) | Climate disclosure framework (voluntary, June 2025) | Climate principles (June 2022) |
| GOV | — | Qualitative (risk-management quality) | Governance disclosures | SRP |
| INS | Insurer solvency (not Basel) | Own risk and solvency assessment practice | IRDAI public disclosures | IAIS ICP 16 (reference) |
| ARC / FND | Family rules | Scenario-based | Notes / scheme disclosures | — |

---

## H.4 Risk-governance requirements by family (seed rule pack; citations to verify)

| Requirement | Bank | UCB | NBFC-BL | NBFC-ML | NBFC-UL | HFC | CIC | ARC | Co-op society | Insurer | MF AMC | Listed co. | Company / LLP |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Board-approved risk policy / framework | Y | Y | Y | Y | Y | Y | Y | Y | By-law/best practice | Y | Y (RMF) | Y (risk-management plan, LODR Reg 17(9) [VERIFY]) | s.134(3)(n) statement |
| Risk Management Committee | Y | [VERIFY] | Y (GOV para 9) | Y | Y | Y | Y | [VERIFY] | — | Y [VERIFY IRDAI CG 2024] | Y (risk committee) [VERIFY] | Top 1,000 + HVDLE (LODR Reg 21) [VERIFY] | Optional |
| CRO | Y | [VERIFY] | — | Y if assets > ₹5,000 cr (GOV para 19) | same | same | same | [VERIFY] | — | Y [VERIFY] | Y (SEBI MF CXO) [VERIFY] | — | — |
| ALCO | Y | Y [VERIFY] | If ALM Ch II applies (assets ≥ ₹100 cr; ALM para 17) | Y | Y | Y | Y (ALM para 4) | ○ | — | ALM committee [VERIFY] | — | — | — |
| IT Strategy Committee | Y [VERIFY] | Y [VERIFY] | BL ≥ ₹500 cr (per Finbyx reading of CYB) [VERIFY] | Y | Y | Y | — (CIC excluded per Finbyx) [VERIFY] | [VERIFY] | — | Y [VERIFY] | Y (CSCRF) [VERIFY] | — | — |
| ICAAP | Y (Ch V) | [VERIFY] | — | Y | Y | Y | Y | ○ | — | Own practice | — | — | — |
| Stress-testing policy | Y (Annex IV) | ○ | ○ | Y (ICAAP; ALM para 28) | Y | Y | Y | ○ | ○ | Y [VERIFY] | Y (scheme stress tests) [VERIFY] | ○ | ○ |
| Liquidity stress test + CFP | Y | Y | If ALM Ch II | Y (ALM 28–29) | Y | Y | Y | ○ | ○ | Y | Y (LRM) | ○ | ○ |
| Fraud risk policy + SCBMF/CoE | Y | Y | ≥ ₹500 cr (FRM 2026 para 3) | Y | Y | NHB route | Y | Y [VERIFY] | By-law | Y [VERIFY] | Y | ○ | ○ |
| EWS framework | Y | Y | — | Y (FRM paras 13–23) | Y | NHB | Y | ○ | — | — | — | — | — |
| Model risk framework | Draft (2026) | Draft | Draft | Draft | Draft | Draft | Draft | Draft | — | — | — | — | — |
| Operational resilience (critical operations, impact tolerance) | Y (ORM GN) | Y | ○ | Y | Y | Y | Y | Y | — | — | — | — | — |
| PCA / SAF | Bank PCA | UCB SAF | — | Y (MSD 2026 Ch V) | Y | Excluded | Y | — | — | Solvency control level | — | — | — |
| Pillar 3 / public risk disclosure | Y | Notes | Notes | Notes + ALM/LCR | Notes + enhanced | Notes | Notes | Notes | Audit report | IRDAI disclosures | Scheme | Board report + MD&A | Board report |

Each "Y" becomes a resolver rule with citation and effective date; each "[VERIFY]" ships as `pending verification` (visible badge, does not block) until platform content confirms the text (Appendix W).

---

## H.5 Operational-risk event-type taxonomy (Basel L1/L2)

| L1 code | Level 1 event type | Level 2 categories |
|---|---|---|
| OPR.01 | Internal fraud | Unauthorised activity; theft and fraud (by staff) |
| OPR.02 | External fraud | Theft and fraud (by third parties); systems security (hacking, data theft) |
| OPR.03 | Employment practices and workplace safety | Employee relations; safe environment; diversity and discrimination |
| OPR.04 | Clients, products and business practices | Suitability, disclosure and fiduciary; improper business or market practices; product flaws; selection, sponsorship and exposure; advisory activities |
| OPR.05 | Damage to physical assets | Disasters and other events |
| OPR.06 | Business disruption and system failures | Systems (hardware, software, telecom, utility outage) |
| OPR.07 | Execution, delivery and process management | Transaction capture, execution and maintenance; monitoring and reporting; customer intake and documentation; customer/client account management; trade counterparties; vendors and suppliers |

Loss-event mandatory fields (P08 FR-P08-35): occurrence date, discovery date, accounting date, gross loss, recoveries (insurance/other), net loss, near-miss/gain flags, boundary flags (credit-related, market-related, legal), root cause (people/process/system/external), controls failed, business line. Boundary rule: a credit loss caused by an operational failure (e.g., forged documents) is recorded as an operational loss with boundary flag `credit_related` and is not double-counted in credit-risk loss statistics.

---

## H.6 Ratio and metric library

**Columns:** ID · metric · formula (plain text; kernel AST is authoritative) · source (GL = trial balance/general ledger via P11; LB = loan book/segments; ALM; CAP = capital run; ECL; COL = collections; REF = registers/limits; OPS = incidents, fraud, complaints, cyber; HR = P13 aggregates; INV = investment template; IMP = imported result) · threshold by profile (typed **reg** regulatory / **brd** Board / **mkt** market convention) · frequency (D/W/M/Q/Y/Event) · citation. "Avg" = average of opening and closing unless the metric version says daily average.

Abbreviations for citations: **CAP** NBFC Capital Adequacy Directions 2025 (RBI/DOR/2025-26/345); **ALM** NBFC ALM Directions 2025 (RBI/DoR/2025-26/355); **CON** NBFC Concentration Risk Management Directions 2025 (RBI/DOR/2025-26/351); **IRACP** NBFC IRACP Directions 2025 (RBI/DOR/2025-26/356); **FS** NBFC Financial Statements Directions 2025 (RBI/DOR/2025-26/359); **MSD** NBFC Miscellaneous Supervisory Directions 2026 (RBI/DoS/2026-27/467); **FRM** NBFC Fraud Risk Management Directions 2026 (RBI/DoS/2026-27/463); **CRM** NBFC Credit Risk Management Directions 2025 (RBI/DOR/2025-26/350); **CF** NBFC Credit Facilities Directions 2025 (RBI/DOR/2025-26/347); **MFI** NBFC-MFI Directions 2025 (RBI/DOR/2025-26/371); **HFC** HFC Directions 2025 (RBI/DOR/2025-26/365); **CICD** CIC Directions 2025 (RBI/DOR/2025-26/367); **CB-CAP** Commercial Banks Capital Adequacy Directions 2025 (RBI/DOR/2025-26/151); **UCB-CAP** UCB Capital Adequacy Directions 2025 (RBI/DOR/2025-26/275); **ORM** RBI Guidance Note on Operational Risk Management and Operational Resilience; **CYB** NBFC Cybersecurity/Technology Risk Directions 2026 (RBI/DoS/2026-27 series [VERIFY number]); **SBR/GOV/IAF/SA** as cited in Finbyx v1.5.

### H.6.1 Canonical metrics R1–R57 (Finbyx v1.5 RK6.2 — identical definitions in the kernel)

| ID | Metric | Formula | Source | Threshold by profile | Freq | Citation |
|---|---|---|---|---|---|---|
| R1 | CRAR | (Tier 1 + Tier 2) ÷ RWA | CAP | reg: NBFC ML+, MFI, HFC, gold-primary ≥ 15%; bank 9% (+2.5% CCB); UCB 9% (Tier 1) / 12% (Tiers 2–4); ARC 15% | M, Q | CAP 6; CB-CAP 11; UCB-CAP 9; MSD 16–17 |
| R2 | Tier 1 ratio | Tier 1 ÷ RWA | CAP | reg: ML+ ≥ 10%; gold-primary ≥ 12%; HFC ≥ 10%; bank ≥ 7% | M, Q | CAP 6(1)–(2); CB-CAP 11 |
| R3 | CET1 ratio | CET1 ÷ RWA | CAP | reg: NBFC-UL ≥ 9%; bank ≥ 5.5% (+CCB → 8%) | M, Q | CAP 6(4); CB-CAP 11 |
| R4 | Tier 2 to Tier 1 | Tier 2 ÷ Tier 1 | CAP | reg: ≤ 100% (NBFC ML+, gold-primary, MFI, HFC; UCB) | Q | CAP 6(1),(3); UCB-CAP 10 |
| R5 | BL leverage | Outside liabilities ÷ owned fund | GL | reg: NBFC-BL ≤ 7 | M | CAP 4(7), 17 |
| R6 | Bank leverage ratio | Tier 1 ÷ exposure measure | CAP | reg: [VERIFY] 4% D-SIB / 3.5% others | Q | CB-CAP Ch VII |
| R7 | CIC ANW/RWA and leverage | ANW ÷ RWA; outside liabilities ÷ ANW | GL, CAP | reg: ANW/RWA ≥ 30%; leverage ≤ 2.5× | Q | CICD; MSD 16–17 |
| R8 | LCR | Stock of HQLA ÷ net cash outflows over 30 days (stressed) | ALM | reg: ≥ 100% where applicable | D; disclosed Q | ALM 60–62, 68–76 |
| R9 | NSFR (banks) | Available stable funding ÷ required stable funding | ALM | reg: ≥ 100% | Q | Bank liquidity directions [VERIFY] |
| R10 | SLS cumulative mismatch % | −min(0, cumulative gap) ÷ cumulative outflows | ALM | reg: 1–7 d ≤ 10%; 8–14 d ≤ 10%; 15–30/31 d ≤ 20%; brd: later buckets to 1 year | M | ALM 39–40 |
| R11 | Stock ratios (6) | ST liabilities/total assets; ST liabilities/LT assets; CP/total assets; NCD < 1 yr original/total assets; ST liabilities/total liabilities; LT assets/total assets | GL, ALM | brd | M; disclosed Q | ALM 43 |
| R12 | Funding concentration | Significant counterparties ÷ total liabilities; top-10 borrowings; top-20 deposits | GL | brd | Q | ALM 15, Annex I |
| R13 | IRS gap, EaR, DGAP, ΔEVE | RSA − RSL per bucket; EaR = Σ gapᵢ × Δr × tᵢ (≤ 1 yr); DGAP = D_A − (L/A)·D_L; ΔEVE ≈ −DGAP·A·Δr/(1+r) | ALM | brd vs total assets/earning assets/equity | M | ALM 45–52 |
| R14 | GNPA % | Gross NPA ÷ gross advances | LB | brd | M | FS |
| R15 | NNPA % | (GNPA − NPA provisions) ÷ (gross advances − NPA provisions); incl. NPIs for PCA | LB, ECL | reg (PCA): RT1 > 6% ≤ 9%; RT2 > 9% ≤ 12%; RT3 > 12% | M, Q | MSD 16–17 |
| R16 | Provision coverage | NPA provisions ÷ GNPA (variant incl. technical write-offs) | LB, ECL | brd | M | mkt |
| R17 | SMA ratios | SMA-0, SMA-1, SMA-2 balances ÷ standard advances | LB | brd (EWS) | D | IRACP [VERIFY paras] |
| R18 | Slippage ratio | Fresh NPAs ÷ opening standard advances (annualised) | LB | brd | M | mkt |
| R19 | Credit cost | Impairment charge ÷ avg gross loans (annualised) | GL, LB | brd | M | mkt |
| R20 | Write-off ratio | Write-offs ÷ avg gross loans | GL | brd | Q | mkt |
| R21 | Restructured % | Restructured balances ÷ gross advances | LB | brd | M | FS |
| R22 | Collection efficiency | Current collections ÷ current demand (overall incl. arrears/prepayments reported separately) | COL | brd | D, M | mkt |
| R23 | Roll rates and vintage loss | Bucket transition matrix; cumulative loss by disbursal cohort | LB | brd | M | mkt |
| R24 | ECL coverage by stage | ECL of stage ÷ gross carrying amount of stage | ECL | brd; SICR backstop: Ind AS 109 rebuttable presumption at 30 DPD, any rebuttal capped as the applicable RBI direction requires [VERIFY cap — 60 DPD per Finbyx reading] | M, Q | FS Annex 1 [VERIFY] |
| R25 | Impairment-reserve requirement | max(0, IRACP provision − ECL) | ECL, LB | reg: appropriation required | Q, Y | FS Annex 2; IRACP |
| R26 | Single-counterparty exposure | Exposure ÷ Tier 1 (ML) or eligible capital base (UL) | LB, CAP | reg: ML 25% (+5% infra); IFC 30%; UL 20% (+5% Board), cap 25% (IFC 30%) | D, M | CON [VERIFY paras] |
| R27 | Group exposure | Group exposure ÷ Tier 1 | LB, REF | reg: ML 40% (+10% infra); IFC 50%; UL 25% (+10% infra); IFC UL 35% | D, M | CON [VERIFY] |
| R28 | Top-20 concentration | Top-20 advances (exposures) ÷ total | LB | brd | Q | FS |
| R29 | Sensitive-sector exposure | CME ÷ Tier 1; CRE ÷ Tier 1; land sub-limit | LB | brd; reg: IPO financing ≤ ₹1 crore per borrower | M | CON [VERIFY] |
| R30 | Sector/state HHI | Σ (share)² | LB | brd | M | mkt |
| R31 | Related-party lending | RP loans ÷ Tier 1; count above materiality | LB, REF | brd; materiality ceiling ₹10 cr (UL/TL), ₹5 cr (ML), ₹1 cr (BL) | M | CRM [VERIFY paras 13F–13G] |
| R32 | Intra-group exposure | Intra-group exposure ÷ total exposure | LB | brd | Q | FS |
| R33 | NIM | NII ÷ avg interest-earning assets | GL | brd | M, Q | mkt |
| R34 | Portfolio yield | Loan interest income ÷ avg gross loans | GL, LB | brd | M | mkt |
| R35 | Cost of funds | Interest expense ÷ avg interest-bearing liabilities | GL | brd | M | mkt |
| R36 | Spread | Yield − cost of funds | GL | brd | M | mkt |
| R37 | ROA | PAT ÷ avg total assets | GL | brd | Q | mkt |
| R38 | ROE | PAT ÷ avg net worth | GL | brd | Q | mkt |
| R39 | Cost-to-income | Opex ÷ (NII + other operating income) | GL | brd | M | mkt |
| R40 | Opex to AUM | Opex ÷ avg AUM (on- and off-book) | GL, LB | brd | M | mkt |
| R41 | Debt-equity / leverage multiple | Borrowings ÷ net worth; total assets ÷ net worth | GL | brd; lender covenants | M | FS |
| R42 | Credit-deposit ratio (bank, UCB) | Advances ÷ deposits | GL | brd | M | mkt |
| R43 | Priority-sector achievement | PSL ÷ ANBC or CEOBE | LB | reg: SCB 40%; SFB 60% of ANBC from FY 2025-26 (75% earlier); UCB 60% [VERIFY against current PSL Directions] | Q | PSL Directions [VERIFY] |
| R44 | Gold-loan LTV | Outstanding (bullet: total repayable) ÷ collateral value | LB | reg: consumption loans ≤ ₹2.5 lakh 85%; ₹2.5–5 lakh 80%; > ₹5 lakh 75% [VERIFY] | D | CF [VERIFY paras] |
| R45 | Share LTV | Loan ÷ value of shares | LB | reg: ≤ 50% at all times [VERIFY] | D | CF [VERIFY] |
| R46 | HFC LTV | Loan ÷ property value | LB | reg: 90% / 80% / 75% by loan size [VERIFY] | at sanction | HFC [VERIFY] |
| R47 | MFI qualifying assets | Microfinance loans ÷ (total assets − intangibles), excl. channelising book | LB, GL | reg: ≥ 60% of total assets (lowered from 75% by RBI in June 2025; the owner baseline's 75% is the pre-amendment value) [VERIFY para in MFI Directions 2025; OI-H-01] | M, Q | MFI [VERIFY] |
| R48 | Non-MFI microfinance share | Microfinance loans ÷ total assets | LB, GL | reg: ≤ 25% [VERIFY] | M | MFI [VERIFY] |
| R49 | DLG cover | DLG ÷ amount disbursed in the portfolio | REF | reg: ≤ 5% | D | CF [VERIFY para] |
| R50 | Gold-primary test | Gold loans ÷ financial assets | LB | reg: ≥ 50% → Tier 1 12% profile | Q | CAP 6(1) |
| R51 | Threshold proximity | Assets vs ₹100 / 500 / 1,000 / 5,000 / 15,000 crore | GL | applicability triggers | M | SBR; GOV; IAF; ALM; SA |
| R52 | PCA proximity | min(CRAR − min, Tier 1 − min, 6% − NNPA) in bps (CIC: ANW/RWA − 30%, 6% − NNPA, 2.5× − leverage shown separately) | CAP, LB | brd (red within 150 bps of RT1, REC) | M, Q | MSD 16–17 |
| R53 | Operational loss ratio | Net operational losses (12 months) ÷ gross income | OPS | brd (RAS) | Q | ORM [VERIFY para 42] |
| R54 | Impact-tolerance breaches | Count of critical operations breaching time/data/service tolerance | OPS | brd: zero | Event | ORM [VERIFY paras 32–33] |
| R55 | Fraud KRIs | Count and value; detection-to-classification days; % FMR within 14 days of classification | OPS | reg: 100% FMR within 14 days | M | FRM 43 |
| R56 | Cyber KRIs | Incidents; % reported within regulatory window (6 hours CERT-In/RBI) [VERIFY]; critical vulnerabilities open; patch SLA | OPS | reg: 100% within window | M | CYB [VERIFY]; CERT-In Directions 28 Apr 2022 |
| R57 | Complaint rate | Complaints per 10,000 accounts; % resolved within TAT | OPS | brd | M | RBC/grievance directions [VERIFY] |

### H.6.2 LDC extensions R58–R125

| ID | Metric | Formula | Source | Threshold / profile | Freq | Citation |
|---|---|---|---|---|---|---|
| R58 | CET1 headroom over combined buffer (bank) | CET1 ratio − (5.5% + CCB + D-SIB + CCyB) | CAP | reg ≥ 0; brd buffer | Q | CB-CAP 11, Ch VI |
| R59 | CASA ratio (bank, UCB) | (Current + savings deposits) ÷ total deposits | GL | brd | M | mkt |
| R60 | IRRBB ΔEVE to Tier 1 (bank) | Max ΔEVE across prescribed shocks ÷ Tier 1 | ALM | sup. outlier test (BCBS SRP31: 15% of Tier 1) [VERIFY RBI] | Q | Bank IRRBB directions [VERIFY] |
| R61 | NII sensitivity (bank) | ΔNII over 12 months under ±200 bps parallel | ALM | brd | Q | [VERIFY] |
| R62 | Bank large exposure | Exposure ÷ Tier 1 per counterparty/group | LB | reg: LEF [VERIFY 20%/25%] | Q | Bank LEF [VERIFY] |
| R63 | SLR compliance (bank, UCB) | SLR securities ÷ NDTL | GL | reg: [VERIFY current %] | Fortnightly | RBI CRR/SLR directions [VERIFY] |
| R64 | CRR compliance (bank, UCB) | Balance with RBI ÷ NDTL | GL | reg: [VERIFY current %] | Fortnightly | [VERIFY] |
| R65 | Gross slippage (bank) | Fresh NPAs ÷ opening standard advances | LB | brd | Q | mkt |
| R66 | UCB net worth vs floor | Net worth ÷ applicable floor (₹2 cr / ₹5 cr; 50% by 31 Mar 2026; 100% by 31 Mar 2028) | GL | reg ≥ 100% of applicable glide value | Q | UCB-CAP 6–7 |
| R67 | UCB CRAR by tier | as R1 with tier minimum | CAP | reg: Tier 1 9%; Tiers 2–4 12% | Q | UCB-CAP 9 |
| R68 | UCB PNCPS+PDI share | (PNCPS + PDI + IPDI) ÷ Tier 1 | CAP | reg ≤ 35%; PDI ≤ 15% | Q | UCB-CAP 12–13 |
| R69 | UCB exposure norms | Single/group exposure ÷ Tier 1 capital | LB | reg [VERIFY] | M | UCB exposure directions [VERIFY] |
| R70 | UCB housing/CRE share | Housing + CRE ÷ total loans | LB | reg [VERIFY] | Q | [VERIFY] |
| R71 | ARC NOF | Net owned fund | GL | reg ≥ ₹300 crore (₹1,000 crore for IBC resolution applicant) | Q | ARC Directions 2025 [VERIFY para] |
| R72 | ARC CRAR | Capital ÷ RWA | CAP | reg ≥ 15% | Q | ARC Directions 2025 [VERIFY] |
| R73 | ARC SR self-investment | ARC holding in each SR class ÷ SRs issued in class | REF | reg [VERIFY: higher of 15% of transferors' investment or 2.5% of total SRs] | Event, Q | ARC Directions [VERIFY] |
| R74 | ARC resolution-period ageing | Count/value of assets beyond 5 years (8 with Board approval) | REF | reg | Q | ARC Directions |
| R75 | ARC realisation rate | Cumulative realisation ÷ acquisition cost by vintage | REF | brd | Q | mkt |
| R76 | SR NAV / rating distribution | Share of SRs by rating grade | REF | brd | H | ARC Directions [VERIFY] |
| R77 | CIC group-company asset share | Investments in group companies ÷ net assets | INV, GL | reg ≥ 90% [VERIFY] | Q | CICD [VERIFY] |
| R78 | CIC equity share | Equity/CCPS in group companies ÷ net assets | INV, GL | reg ≥ 60% [VERIFY] | Q | CICD [VERIFY] |
| R79 | Insurer solvency ratio | ASM ÷ RSM | IMP | reg ≥ 150% (control level) | Q | Insurance Act s.64VA; IRDAI AFIF Regs 2024 |
| R80 | Claims (loss) ratio | Net incurred claims ÷ net earned premium | IMP | brd | Q | mkt |
| R81 | Combined ratio | (Claims + expenses + commission) ÷ net earned premium | IMP | brd | Q | mkt |
| R82 | Expense of management ratio | EoM ÷ gross written premium vs regulatory limits | IMP | reg [VERIFY IRDAI EoM regulations] | Q, Y | [VERIFY] |
| R83 | 13th-month persistency (life) | Policies in force at 13th month ÷ policies issued | IMP | brd | Q | mkt |
| R84 | Insurer ALM duration gap | Duration of assets − duration of liabilities | IMP | brd | Q | [VERIFY] |
| R85 | Investment-limit compliance (insurer) | Approved/other investments vs IRDAI limits | IMP | reg [VERIFY] | Q | IRDAI AFIF Regs 2024 [VERIFY] |
| R86 | Scheme liquidity cover (MF) | Liquid assets ÷ stressed redemption | IMP | reg/brd per SEBI LRM [VERIFY] | M | SEBI MF Master Circular [VERIFY] |
| R87 | Issuer concentration (MF scheme) | Exposure to issuer ÷ scheme NAV | IMP | reg per rating limits [VERIFY] | D | SEBI (Mutual Funds) Regulations, 2026 investment-restriction schedule (Seventh Schedule under the 1996 Regulations) [VERIFY schedule number] |
| R88 | AIF investee concentration | Investment in one investee ÷ investable funds | IMP | reg: Cat I/II 25%; Cat III 10% (listed variants) [VERIFY] | Event, Q | AIF Regulations 2012 Reg 15 [VERIFY] |
| R89 | AIF Cat III leverage | Gross exposure ÷ NAV | IMP | reg [VERIFY 2×] | D | AIF Regulations / Master Circular [VERIFY] |
| R90 | AMC / intermediary net worth | Net worth ÷ regulatory floor | GL | reg [VERIFY by registration category] | Q | SEBI regulations [VERIFY] |
| R91 | Current ratio | Current assets ÷ current liabilities | GL | Schedule III disclosure; brd | Y, Q | Companies Act Sch III [VERIFY] |
| R92 | Debt-equity ratio | Total debt ÷ shareholders' equity | GL | Sch III; covenants | Y, Q | Sch III |
| R93 | Debt service coverage ratio | Earnings available for debt service ÷ debt service | GL | Sch III; covenants | Y, Q | Sch III |
| R94 | Return on equity | Net profit after tax − preference dividend ÷ avg shareholders' equity | GL | Sch III | Y | Sch III |
| R95 | Inventory turnover | COGS (or sales) ÷ avg inventory | GL | Sch III | Y | Sch III |
| R96 | Trade receivables turnover | Net credit sales ÷ avg trade receivables | GL | Sch III | Y | Sch III |
| R97 | Trade payables turnover | Net credit purchases ÷ avg trade payables | GL | Sch III | Y | Sch III |
| R98 | Net capital turnover | Net sales ÷ working capital | GL | Sch III | Y | Sch III |
| R99 | Net profit ratio | Net profit ÷ net sales | GL | Sch III | Y | Sch III |
| R100 | Return on capital employed | EBIT ÷ capital employed | GL | Sch III | Y | Sch III |
| R101 | Return on investment | Income from investments ÷ avg investments (time-weighted where available) | GL, INV | Sch III | Y | Sch III |
| R102 | Interest coverage | EBIT ÷ finance costs | GL | brd; covenants | Q | mkt |
| R103 | Cash runway | Unrestricted cash ÷ avg monthly net burn | GL | brd | M | mkt |
| R104 | Co-op own funds ratio | (Share capital + reserves) ÷ total assets | GL | brd (management indicator) | Q | State Act / by-laws [VERIFY] |
| R105 | Co-op reserve-fund compliance | Transfer to reserve fund ÷ net profit vs statutory % | GL | reg per Act (MSCS s.63 [VERIFY]; State Acts) | Y | MSCS Act 2002; State Acts |
| R106 | Co-op overdue to demand | Overdue ÷ total demand | COL | brd / audit norms | M | [VERIFY state audit norms] |
| R107 | Co-op NPA % (audit norms) | NPA per State audit classification ÷ loans | LB | brd | Q | [VERIFY per state] |
| R108 | Co-op liquidity ratio | Liquid assets ÷ deposits per by-laws/Act | GL | per by-law/Act [VERIFY] | M | State Act / by-laws |
| R109 | Co-op deposit concentration | Top-20 member deposits ÷ total deposits | REF | brd | Q | mkt |
| R110 | Co-op non-permitted investments | Investments outside permitted avenues (count/value) | INV | reg: zero [VERIFY Act] | Q | State Act / MSCS Act s.64 [VERIFY] |
| R111 | Annualised attrition | Leavers (12 m) ÷ avg headcount | HR | brd | M | mkt |
| R112 | Key-person vacancy days | Days a KMP/control-function role is vacant | HR, REF | reg where a role is mandatory (e.g., CRO); brd | Event | GOV [VERIFY]; LODR |
| R113 | Mandatory training completion | Completed ÷ assigned mandatory trainings (KYC/AML, POSH, cyber, FPC) | HR | brd ≥ 95% | M | mkt |
| R114 | Labour-code working-time breaches | Count of overtime/working-hour limit breaches | HR | reg: zero (Labour Code rule packs) | M | OSH Code / State rules [VERIFY] |
| R115 | Background verification pending | Joiners without completed BGV ÷ joiners | HR | brd | M | mkt |
| R116 | POSH inquiry ageing (count only) | Open inquiries beyond 90 days (count) | HR (sealed → count) | reg: zero beyond 90 days | M | POSH Act 2013 s.11(4) |
| R117 | Absenteeism | Unplanned absence days ÷ scheduled days | HR | brd | M | mkt |
| R118 | Overdue high-risk obligations | Count of High-risk compliance instances past due (P04) | REF | brd: zero | D | — |
| R119 | Regulatory penalties YTD | Sum of penalties/compounding fees | GL, REF | brd | M | — |
| R120 | Repeat audit findings % | Repeat findings ÷ total findings (P10) | REF | brd | Q | — |
| R121 | Ombudsman escalation rate | Complaints escalated to RBI Ombudsman/other forum ÷ complaints | OPS | brd | M | RB-IOS [VERIFY] |
| R122 | Grievance TAT compliance | Complaints resolved within regulatory/Board TAT ÷ closed | OPS | reg/brd | M | P14 rule packs |
| R123 | Critical vendors without current assessment | Count (P12) | REF | brd: zero | M | Outsourcing Directions [VERIFY] |
| R124 | Critical vulnerabilities beyond SLA | Count (P12) | OPS | brd: zero | W | CYB [VERIFY] |
| R125 | DR test success | Successful DR drills ÷ planned (critical systems) | OPS | brd 100% | Q | CYB [VERIFY] |

Rules: (1) A metric typed **reg** with an unverified citation runs as **brd** until verified (shown "pending verification"). (2) Tenants may add metrics (R-tenant namespace `T-<tenant>-<seq>`), which enter `DRAFT` and need validation and owner approval. (3) Schedule III ratios use the definitions in the tenant's financial statements; the "explain change > 25%" check is applied to R91–R101 [VERIFY current Schedule III text].

### H.6.3 Aggregation and currency rules for group and multi-entity views *(v1.1)*

1. **Ratios are recomputed, never averaged**: group ratio = Σ numerators ÷ Σ denominators of the in-scope entities, using each metric's definition; where a regulation defines a consolidated measure (e.g., group exposures, CIC group tests), that definition prevails.
2. **Currency**: monetary components are translated to the reporting currency at the snapshot rate (closing rate for balances, average rate for flows) from `FX_RATE_PORT` (P25), with source and date stored in the result lineage.
3. **Thresholds**: group views compare against Board-set group appetite; entity regulatory floors are always shown per entity and never netted across entities (NN-38).
4. **Cross-region**: entities in other regional cells contribute aggregates only (NN-24 amended); the group result records which entities contributed aggregates.
5. **Mixed frameworks**: values computed under different accounting frameworks (Ind AS, AS, IFRS, local GAAP) are labelled per entity; a consolidated figure mixing frameworks is marked "informational" unless a reviewed conversion pack exists.

---

## H.7 Capital profiles — detailed rule-pack content

| Profile code | Engine | Components and deductions | Minimums | Buffers / special rules | Citations |
|---|---|---|---|---|---|
| `CAP-NBFC-BL` | Leverage | Owned fund; outside liabilities | Leverage ≤ 7 | Alert at 6.5 (REC) | CAP 4(7), 17 |
| `CAP-NBFC-ML` | CRAR (credit RWA only) | CET1 elements (para 7), deductions (8: goodwill/intangibles, DTA, excess investments, impairment reserve not recognised), Tier 1 (10: owned fund less investments > 10% of owned fund; PDI ≤ 15% of Tier 1), Tier 2 (13: general provisions ≤ 1.25% of RWA; revaluation reserves at 55% discount; sub-debt amortised, ≤ 50% of Tier 1); DTA (14); AIF subordinated units, co-lending unrealised profit, DLG (15); Ind AS adjustments (16); risk weights (18) incl. 125% consumer credit/credit cards; 75%/50% high-quality infra; CGTMSE/CRGFTLIH/NCGTC 0% within cover (18(2)(iv)); securitisation (19–51) | CRAR ≥ 15%; Tier 1 ≥ 10%; Tier 2 ≤ 100% of Tier 1 | No Pillar 1 op/market; ICAAP Ch V | CAP 6(2)–(3), 7–18 |
| `CAP-NBFC-UL` | as ML + CET1 | Tier 1 for UL (11: CET1, CCPS, PDI ≤ 15%) | + CET1 ≥ 9% | Enhanced disclosures | CAP 6(4), 11 |
| `CAP-NBFC-TL` | as UL + add-on | — | As communicated | — | CAP 6(5) |
| `CAP-NBFC-GOLD` | CRAR | as ML/BL | Tier 1 ≥ 12%; CRAR ≥ 15%; Tier 2 ≤ 100% Tier 1 | Gold-primary test R50 quarterly | CAP 6(1) |
| `CAP-NBFC-MFI` | CRAR | as ML | CRAR ≥ 15% in every layer; paras 6(1), 6(2), 17 not applicable | MFI-specific weights [VERIFY] | CAP 3(1) proviso; MFI |
| `CAP-HFC` | CRAR (partial CAP) | HFC risk weights by size and LTV [VERIFY] | CRAR ≥ 15%; Tier 1 ≥ 10% | — | CAP 3(2); HFC |
| `CAP-CIC` | ANW/RWA | ANW, RWA per CICD | ANW ≥ 30% RWA; leverage ≤ 2.5× | PCA RT thresholds §H.7.1 | CAP 3(4); CICD; MSD |
| `CAP-MGC` | Per MGC Directions | — | [VERIFY] | — | MGC Directions (RBI/DOR/2025-26/369) |
| `CAP-SPD` | Per SPD rules (partial CAP) | — | [VERIFY] | — | CAP 3(5) |
| `CAP-BANK` | Basel III | CET1/AT1/Tier 2 per CB-CAP; credit SA; market risk; operational risk | CET1 5.5%; Tier 1 7% (AT1 ≤ 1.5%); total 9% (Tier 2 ≤ 2%) | CCB 2.5% CET1; D-SIB surcharge; CCyB; leverage ratio [VERIFY] | CB-CAP 11, 250–252, Ch VI–VII |
| `CAP-BANK-2027` | Revised Basel III packs | Revised SA credit; revised market risk/CVA; op risk BIC × ILM | as above | Parallel run only until effective [VERIFY dates] | Finbyx RK3.6 reading [VERIFY] |
| `CAP-SFB` / `CAP-PB` / `CAP-RRB` / `CAP-LAB` | Bank variants | [VERIFY] | [VERIFY] | — | Family directions [VERIFY] |
| `CAP-UCB` | CRAR | Tier 1 (11: member capital, PNCPS, reserves, PDI, special reserve s.36(1)(viii), revaluation at 55% discount; deductions note 6); Tier 2 (14: general provisions ≤ 1.25% RWA, IFR, upper Tier 2 instruments, LTSB ≤ 50% Tier 1) | Tier 1 UCB 9%; Tiers 2–4 12%; Tier 2 ≤ 100% Tier 1; net worth ₹2 cr / ₹5 cr glide | No CCB | UCB-CAP 6–16 |
| `CAP-ARC` | CRAR + NOF | Per ARC Directions | CRAR ≥ 15%; NOF ≥ ₹300 cr | SR investment rule | ARC Directions 2025 [VERIFY] |
| `CAP-IFSCA-FC` | Per IFSCA | [VERIFY] | [VERIFY] | — | IFSCA circulars 2021 [VERIFY] |
| `CAP-INS` | Imported solvency | ASM, RSM by line | Solvency ≥ 150% | Ind-RBC future pack | s.64VA; AFIF Regs 2024 |
| `CAP-NETWORTH` | Net-worth monitor | Net worth per registration rules | Per category [VERIFY] | — | SEBI/IRDAI registration regulations |
| `CAP-CORP` | None (ratios R91–R103) | — | — | Covenants | Sch III |
| `CAP-COOP` | Management indicators (R104–R110) | — | Act/by-law | — | MSCS Act; State Acts |

### H.7.1 PCA thresholds (NBFC; MSD 2026 para 17) — stored as offsets and "currently" values

| Indicator | RT1 | RT2 | RT3 |
|---|---|---|---|
| CRAR | ≤ 300 bps below minimum (< 15% ≥ 12%) | > 300 to ≤ 600 bps below (< 12% ≥ 9%) | > 600 bps below (< 9%) |
| Tier 1 | ≤ 200 bps below (< 10% ≥ 8%) | > 200 to ≤ 400 bps (< 8% ≥ 6%) | > 400 bps (< 6%) |
| NNPA incl. NPIs | > 6% ≤ 9% | > 9% ≤ 12% | > 12% |
| CIC ANW/RWA | ≤ 600 bps below (< 30% ≥ 24%) | > 600 to ≤ 1,200 bps (< 24% ≥ 18%) | > 1,200 bps (< 18%) |
| CIC leverage | ≥ 2.5× < 3× | ≥ 3× < 3.5× | ≥ 3.5× |

Mandatory actions (para 19): RT1 — dividend/remittance restriction; promoter/shareholder equity infusion and leverage reduction; CICs: restriction on guarantees/contingent liabilities for group companies. RT2 — RT1 + branch-expansion restriction. RT3 — RT1 + RT2 + capex restriction (except technology upgrades within Board limits) and restriction/reduction of variable operating costs. Discretionary menu (para 20) across special supervisory actions, strategy, governance, capital, credit risk, market risk, HR, profitability, operations, others. Exit (para 18): no breach in four continuous quarterly financial statements (one audited annual) plus supervisory comfort. Scope (para 3): NBFC-D and NBFC-ND ML/UL/TL incl. ICC, CIC, IDF, IFC, MFI, Factors; excludes NBFCs not accepting/intending to accept public funds, PDs, HFCs. Boundary values for tests: CRAR 12.0% = RT1, 11.99% = RT2; NNPA 6.0% = outside, 6.01% = RT1; CIC leverage 2.5× = RT1.

---

## H.8 KRI library (seed, 172 KRIs; 187 from v1.1)

Defaults are **[REC]** starting points; tenants set thresholds through the RAS/KRI workflow (P08). Where a KRI is tied to a regulatory metric, the red threshold can never be looser than the regulatory floor. "Fam." codes: B bank, U UCB, N NBFC, A ARC, C co-op, I IFSCA, M MF/AMC, F AIF, L listed, S SEBI intermediary, Q insurer, Qi insurance intermediary, K company/LLP, * all.

### H.8.1 Library

| KRI ID | KRI | Metric / definition | G / A / R (default) | Freq | Fam. |
|---|---|---|---|---|---|
| KRI-CAP-001 | CRAR headroom | R1 − max(reg min, Board min) | > 200 bps / 100–200 / < 100 bps | M | B U N A |
| KRI-CAP-002 | Tier 1 headroom | R2 − min | > 150 / 50–150 / < 50 bps | M | B N |
| KRI-CAP-003 | CET1 headroom (UL/bank) | R3/R58 | > 150 / 50–150 / < 50 bps | M | B N |
| KRI-CAP-004 | BL leverage | R5 | < 6 / 6–6.5 / > 6.5 | M | N |
| KRI-CAP-005 | PCA proximity | R52 | > 300 / 150–300 / < 150 bps | Q | N |
| KRI-CAP-006 | CIC ANW/RWA headroom | R7 | > 5 pp / 2–5 / < 2 pp | Q | N |
| KRI-CAP-007 | UCB net-worth glide compliance | R66 | ≥ 110% / 100–110% / < 100% | Q | U |
| KRI-CAP-008 | Insurer solvency | R79 | > 180% / 160–180% / < 160% (reg 150%) | Q | Q |
| KRI-CAP-009 | ARC NOF headroom | R71 − ₹300 cr | > ₹50 cr / 0–50 / < 0 | Q | A |
| KRI-CAP-010 | Net-worth floor headroom (intermediary) | R90 | > 120% / 100–120% / < 100% | Q | M S Qi |
| KRI-CAP-011 | RWA growth vs plan | RWA growth − plan growth | < 2 pp / 2–5 / > 5 pp | M | B U N |
| KRI-CAP-012 | Tier 2 / Tier 1 | R4 | < 80% / 80–95% / > 95% | Q | B U N |
| KRI-LIQ-001 | LCR | R8 | > 120% / 110–120% / < 110% | D | B N |
| KRI-LIQ-002 | SLS 1–7 day mismatch | R10 bucket 1 | < 5% / 5–8% / > 8% (limit 10%) | M | N |
| KRI-LIQ-003 | SLS 8–14 day mismatch | R10 bucket 2 | < 5% / 5–8% / > 8% | M | N |
| KRI-LIQ-004 | SLS 15–30 day mismatch | R10 bucket 3 | < 12% / 12–16% / > 16% (limit 20%) | M | N |
| KRI-LIQ-005 | NSFR | R9 | > 115% / 105–115% / < 105% | Q | B |
| KRI-LIQ-006 | Top-10 lender concentration | R12 | < 40% / 40–55% / > 55% of borrowings | Q | N A |
| KRI-LIQ-007 | Single-lender share | largest lender ÷ borrowings | < 15% / 15–25% / > 25% | M | N |
| KRI-LIQ-008 | CP to total assets | R11 | < 5% / 5–10% / > 10% | M | N |
| KRI-LIQ-009 | Survival horizon (stress) | days until cumulative net outflow > liquid resources | > 60 / 30–60 / < 30 days | M | B U N C |
| KRI-LIQ-010 | Undrawn sanctioned lines | undrawn committed bank lines ÷ 3-month outflows | > 100% / 60–100% / < 60% | M | N |
| KRI-LIQ-011 | Deposit concentration (co-op/UCB) | R109 | < 20% / 20–30% / > 30% | Q | U C |
| KRI-LIQ-012 | Scheme liquidity cover (MF) | R86 | > 1.5× / 1.0–1.5× / < 1.0× | M | M |
| KRI-LIQ-013 | Covenant headroom (tightest) | min headroom across lender covenants | > 20% / 10–20% / < 10% | M | N K |
| KRI-LIQ-014 | Cash runway (corporate) | R103 | > 12 / 6–12 / < 6 months | M | K L |
| KRI-IRR-001 | EaR +200 bps | R13 EaR ÷ NII | < 5% / 5–10% / > 10% | M | B U N |
| KRI-IRR-002 | ΔEVE ±200 bps ÷ net worth | R13/R60 | < 10% / 10–15% / > 15% | Q | B U N |
| KRI-IRR-003 | Repricing gap ≤ 1 year ÷ total assets | R13 | < 10% / 10–20% / > 20% | M | N |
| KRI-CRD-001 | GNPA % | R14 | < 3% / 3–5% / > 5% | M | B U N C |
| KRI-CRD-002 | NNPA % | R15 | < 2% / 2–4% / > 4% (PCA RT1 > 6%) | M | B U N |
| KRI-CRD-003 | SMA-1 + SMA-2 share | R17 | < 4% / 4–7% / > 7% | W | B U N |
| KRI-CRD-004 | 30+ DPD (portfolio) | DPD 30+ ÷ AUM | < 4% / 4–6% / > 6% | W | N C |
| KRI-CRD-005 | Slippage ratio | R18 | < 2% / 2–4% / > 4% | M | B U N |
| KRI-CRD-006 | Credit cost | R19 | < 1.5% / 1.5–2.5% / > 2.5% | M | B N |
| KRI-CRD-007 | Provision coverage | R16 | > 70% / 55–70% / < 55% | M | B U N |
| KRI-CRD-008 | Collection efficiency | R22 | > 98% / 95–98% / < 95% | D | N C |
| KRI-CRD-009 | Restructured book | R21 | < 2% / 2–4% / > 4% | M | B N |
| KRI-CRD-010 | Early delinquency (FPD/3-MOB 30+) | first-payment default rate by cohort | < 1% / 1–2% / > 2% | M | N |
| KRI-CRD-011 | Policy deviation rate | approved deviations ÷ sanctions | < 5% / 5–10% / > 10% | M | B N |
| KRI-CRD-012 | Gold LTV breaches | accounts above R44 cap | 0 / 1–10 / > 10 | D | N |
| KRI-CRD-013 | LAS margin shortfall | accounts below required margin (R45) | 0 / 1–5 / > 5 | D | N |
| KRI-CRD-014 | MFI repayment-obligation breaches | loans with household obligation above cap | 0 / 1–10 / > 10 | M | N |
| KRI-CRD-015 | ECL Stage 2 share | Stage 2 GCA ÷ total | < 8% / 8–12% / > 12% | M | B N |
| KRI-CRD-016 | Impairment-reserve need | R25 > 0 | 0 / any / increase > 10% q/q | Q | N |
| KRI-CRD-017 | Write-off ratio | R20 | < 1% / 1–2% / > 2% | Q | B N |
| KRI-CRD-018 | Co-lending partner delinquency | partner pool 90+ ÷ pool | < 2% / 2–4% / > 4% | M | B N |
| KRI-CRD-019 | Co-op overdue to demand | R106 | < 5% / 5–10% / > 10% | M | C U |
| KRI-CRD-020 | ARC realisation vs plan | R75 vs plan | ≥ 100% / 80–100% / < 80% | Q | A |
| KRI-CON-001 | Largest single exposure ÷ Tier 1 | R26 | < 15% / 15–20% / > 20% (ML limit 25%) | D | B N |
| KRI-CON-002 | Largest group exposure ÷ Tier 1 | R27 | < 30% / 30–36% / > 36% (ML 40%) | D | B N |
| KRI-CON-003 | Top-20 share | R28 | < 15% / 15–25% / > 25% | Q | B N A |
| KRI-CON-004 | Sector HHI | R30 | < 0.15 / 0.15–0.25 / > 0.25 | M | B U N |
| KRI-CON-005 | State concentration | largest state ÷ AUM | < 25% / 25–35% / > 35% | M | N C |
| KRI-CON-006 | Capital-market exposure | R29 CME ÷ Tier 1 | < Board 70% / 70–90% / > 90% of Board limit | M | N B |
| KRI-CON-007 | CRE exposure | R29 CRE ÷ Tier 1 | as KRI-CON-006 | M | N B U |
| KRI-CON-008 | LSP/DSA channel concentration | largest channel ÷ disbursements | < 30% / 30–45% / > 45% | M | N |
| KRI-CON-009 | Related-party exposure | R31 | < 50% / 50–80% / > 80% of Board limit | M | N B U |
| KRI-CON-010 | AIF investee concentration | R88 vs limit | < 70% / 70–90% / > 90% of limit | Event | F |
| KRI-CON-011 | MF issuer concentration | R87 vs limit | < 80% / 80–95% / > 95% | D | M |
| KRI-CON-012 | Insurer reinsurer concentration | largest reinsurer share of ceded premium | < 30% / 30–50% / > 50% | Q | Q |
| KRI-MKT-001 | Investment MTM loss (QTD) | unrealised loss ÷ Tier 1 | < 1% / 1–3% / > 3% | W | N B Q |
| KRI-MKT-002 | Equity portfolio drawdown | peak-to-trough % | < 10% / 10–20% / > 20% | D | N F Q |
| KRI-MKT-003 | VaR utilisation | 99% 10-day VaR ÷ Board limit | < 70% / 70–90% / > 90% | D | B N |
| KRI-MKT-004 | Level 3 investments share | Level 3 FV ÷ total FV | < 10% / 10–20% / > 20% | Q | N F M |
| KRI-MKT-005 | SME IPO exposure | SME IPO holdings ÷ investments | < 5% / 5–10% / > 10% | M | N |
| KRI-MKT-006 | AIF Cat III leverage | R89 vs limit | < 70% / 70–90% / > 90% | D | F |
| KRI-MKT-007 | Open FX position | NOOP ÷ Tier 1 | < Board 70% / 70–90% / > 90% | D | B I |
| KRI-MKT-008 | Duration of investment book | modified duration vs Board range | within / ±0.5 yr / outside | M | B N Q |
| KRI-PRF-001 | NIM | R33 vs plan | ≥ plan / −25 bps / −50 bps | M | B U N |
| KRI-PRF-002 | ROA | R37 | > 2% / 1–2% / < 1% | Q | N B |
| KRI-PRF-003 | Cost-to-income | R39 | < 45% / 45–55% / > 55% | M | B U N |
| KRI-PRF-004 | Cost of funds vs plan | R35 − plan | < 10 bps / 10–30 / > 30 bps | M | N |
| KRI-PRF-005 | Combined ratio (GI) | R81 | < 100% / 100–105% / > 105% | Q | Q |
| KRI-PRF-006 | Net profit ratio change | R99 y/y change | < 10% / 10–25% / > 25% (Sch III explain) | Q | K L |
| KRI-OPR-001 | Operational loss ratio | R53 | < 0.5% / 0.5–1% / > 1% of gross income | Q | * |
| KRI-OPR-002 | Loss events reported late | events captured > SLA after discovery | 0 / 1–3 / > 3 per month | M | * |
| KRI-OPR-003 | Near-miss reporting rate | near misses ÷ losses | > 2 / 1–2 / < 1 | Q | * |
| KRI-OPR-004 | Impact-tolerance breaches | R54 | 0 / — / ≥ 1 | Event | B U N A |
| KRI-OPR-005 | Reconciliation breaks ageing | breaks > 30 days | 0 / 1–5 / > 5 | W | B N C |
| KRI-OPR-006 | Manual-entry share in returns | manual cells ÷ total return cells | < 5% / 5–15% / > 15% | M | B U N |
| KRI-OPR-007 | Process SLA breaches (disbursement TAT) | % beyond Board TAT | < 5% / 5–10% / > 10% | M | N |
| KRI-OPR-008 | Document deficiency | loans with missing mandatory documents | < 0.5% / 0.5–2% / > 2% | M | N C |
| KRI-OPR-009 | Branch audit rating | branches rated "unsatisfactory" | 0 / 1–5% / > 5% | Q | B U N C |
| KRI-OPR-010 | Suspense/clearing balances ageing | > 30 days ÷ total | < 1% / 1–3% / > 3% | M | B U N C |
| KRI-CYB-001 | Critical vulnerabilities beyond SLA | R124 | 0 / 1–3 / > 3 | W | * |
| KRI-CYB-002 | Incidents reported within window | R56 % | 100% / — / < 100% | M | * |
| KRI-CYB-003 | Privileged accounts without MFA | count | 0 / — / ≥ 1 | W | * |
| KRI-CYB-004 | Core-system unplanned downtime | minutes per month | < 60 / 60–240 / > 240 | M | B U N C |
| KRI-CYB-005 | Phishing simulation click rate | clicks ÷ recipients | < 5% / 5–10% / > 10% | Q | * |
| KRI-CYB-006 | Patch compliance (critical) | patched within SLA ÷ due | > 98% / 95–98% / < 95% | M | * |
| KRI-CYB-007 | Backup restore test success | R125 | 100% / — / < 100% | Q | * |
| KRI-CYB-008 | VAPT high findings open > 90 days | count | 0 / 1–2 / > 2 | M | * |
| KRI-CYB-009 | Digital payment fraud rate | fraud value ÷ digital volume | < 1 bp / 1–3 / > 3 bps | M | B N |
| KRI-CYB-010 | Unsupported (end-of-life) systems | count in production | 0 / 1 / > 1 | Q | * |
| KRI-TPR-001 | Critical vendors without current assessment | R123 | 0 / 1 / > 1 | M | * |
| KRI-TPR-002 | Vendor SLA breaches (material outsourcing) | breaches per quarter | 0 / 1–2 / > 2 | Q | * |
| KRI-TPR-003 | Outsourcing contracts missing mandatory clauses | count | 0 / — / ≥ 1 | Q | B U N |
| KRI-TPR-004 | Single-vendor dependency (critical service) | critical services with one vendor and no exit plan | 0 / 1 / > 1 | Q | * |
| KRI-TPR-005 | Recovery-agent complaints | complaints per 1,000 recovery cases | < 1 / 1–3 / > 3 | M | N B |
| KRI-TPR-006 | LSP/DLG cover utilisation | R49 vs 5% cap | < 3% / 3–4.5% / > 4.5% | D | N B |
| KRI-MOD-001 | Models overdue for validation | count (tier 1–2) | 0 / 1 / > 1 | M | B N Q |
| KRI-MOD-002 | Scorecard discrimination drift | Gini drop vs development | < 5 pts / 5–10 / > 10 pts | Q | B N |
| KRI-MOD-003 | PSI on scorecard input population | PSI | < 0.1 / 0.1–0.25 / > 0.25 | M | B N |
| KRI-MOD-004 | Model overrides | overrides ÷ decisions | < 5% / 5–10% / > 10% | M | B N |
| KRI-MOD-005 | AI feature incidents | hallucination/unsafe output incidents reported | 0 / 1–2 / > 2 | M | * |
| KRI-CMP-001 | Overdue high-risk obligations | R118 | 0 / 1–2 / > 2 | D | * |
| KRI-CMP-002 | Returns filed late | count per quarter | 0 / 1 / > 1 | Q | * |
| KRI-CMP-003 | Return resubmissions (data errors) | count | 0 / 1–2 / > 2 | Q | B U N |
| KRI-CMP-004 | Open regulatory inspection observations | past due | 0 / 1–3 / > 3 | M | * |
| KRI-CMP-005 | Penalties YTD | R119 | 0 / < ₹5 lakh / ≥ ₹5 lakh | M | * |
| KRI-CMP-006 | KYC periodic updation overdue | accounts overdue ÷ due | < 1% / 1–3% / > 3% | M | B U N C |
| KRI-CMP-007 | STR filing timeliness | STRs filed within prescribed time ÷ total | 100% / — / < 100% | M | B U N I |
| KRI-CMP-008 | Policies past review date | count | 0 / 1–2 / > 2 | M | * |
| KRI-CMP-009 | Repeat audit findings | R120 | < 10% / 10–20% / > 20% | Q | * |
| KRI-CMP-010 | Regulatory changes un-assessed > 30 days | count (P05) | 0 / 1–3 / > 3 | W | * |
| KRI-CMP-011 | Litigation provisions vs exposure | provisions ÷ probable exposure | ≥ 100% / 80–100% / < 80% | Q | * |
| KRI-CND-001 | Complaint rate | R57 | < 5 / 5–10 / > 10 per 10,000 accounts | M | B U N C Q M |
| KRI-CND-002 | Grievance TAT compliance | R122 | > 98% / 95–98% / < 95% | M | * |
| KRI-CND-003 | Ombudsman escalation rate | R121 | < 2% / 2–5% / > 5% | M | B U N Q |
| KRI-CND-004 | Recovery calls outside permitted hours | count | 0 / — / ≥ 1 | D | N B |
| KRI-CND-005 | KFS not acknowledged before execution | count | 0 / — / ≥ 1 | D | N B |
| KRI-CND-006 | Mis-selling complaints | count per quarter | 0–2 / 3–10 / > 10 | Q | Q Qi M B |
| KRI-CND-007 | Penal-charge reversals | count/value | trend down / flat / up | M | N B |
| KRI-CND-008 | Front-running/insider alerts unresolved | count > 30 days | 0 / 1–2 / > 2 | M | M S L |
| KRI-FRD-001 | Fraud count and value | R55 | 0 / per Board / above Board | M | * |
| KRI-FRD-002 | FMR within 14 days of classification | R55 % | 100% / — / < 100% | M | N |
| KRI-FRD-003 | EWS alerts ageing | alerts open > 30 days | < 5% / 5–15% / > 15% | W | B N |
| KRI-FRD-004 | Staff-accountability cases pending | > 6 months | 0 / 1–2 / > 2 | Q | B N U |
| KRI-FRD-005 | Cash/gold shortage at branches | incidents | 0 / 1 / > 1 | M | N C U |
| KRI-FRD-006 | Sanctions screening hits unresolved | > 2 days | 0 / 1–3 / > 3 | D | * |
| KRI-FRD-007 | Mule-account indicators | flagged accounts per 10,000 | < 1 / 1–3 / > 3 | M | B U |
| KRI-FRD-008 | Co-op misappropriation audit observations | count open | 0 / 1 / > 1 | Q | C |
| KRI-STR-001 | AUM growth vs plan | variance | ±10% / ±10–20% / > ±20% | M | N B U |
| KRI-STR-002 | Threshold proximity (layer/role triggers) | R51 within two quarters | none / 1 trigger / overdue readiness | M | N |
| KRI-STR-003 | New-product post-launch performance | products below approval assumptions | 0 / 1 / > 1 | Q | B N Q |
| KRI-STR-004 | Listing-deadline readiness (NBFC-UL) | readiness tasks overdue | 0 / 1–2 / > 2 | M | N |
| KRI-REP-001 | Negative media/social mentions | weighted score | baseline / +50% / +100% | W | * |
| KRI-REP-002 | Customer NPS / satisfaction | score | > 40 / 20–40 / < 20 | Q | * |
| KRI-REP-003 | Public regulatory actions | count | 0 / — / ≥ 1 | Event | * |
| KRI-GRP-001 | Intra-group exposure | R32 | < 10% / 10–20% / > 20% | Q | N B |
| KRI-GRP-002 | Parent rating outlook | negative outlooks | 0 / 1 / downgrade | Event | N B Q |
| KRI-PPL-001 | Attrition | R111 | < 15% / 15–25% / > 25% | M | * |
| KRI-PPL-002 | Key-person vacancy | R112 | 0 / ≤ 30 days / > 30 days | Event | * |
| KRI-PPL-003 | Mandatory training completion | R113 | > 95% / 90–95% / < 90% | M | * |
| KRI-PPL-004 | Working-time breaches | R114 | 0 / 1–5 / > 5 | M | * |
| KRI-PPL-005 | BGV pending | R115 | < 2% / 2–5% / > 5% | M | * |
| KRI-PPL-006 | POSH inquiries beyond 90 days (count) | R116 | 0 / — / ≥ 1 | M | * |
| KRI-PPL-007 | Absenteeism | R117 | < 3% / 3–6% / > 6% | M | * |
| KRI-PPL-008 | Succession coverage for KMP | KMP roles with ready successor ÷ KMP roles | > 80% / 50–80% / < 50% | Y | * |
| KRI-PPL-009 | Statutory dues late (PF/ESI/PT/LWF) | late remittances | 0 / — / ≥ 1 | M | * |
| KRI-DPR-001 | Personal-data breaches | count | 0 / — / ≥ 1 | Event | * |
| KRI-DPR-002 | Data-principal requests beyond SLA | count | 0 / 1–3 / > 3 | M | * |
| KRI-DPR-003 | Processing without recorded consent/legitimate use | records flagged | 0 / — / ≥ 1 | M | * |
| KRI-DPR-004 | Processors without DPA | count | 0 / 1 / > 1 | Q | * |
| KRI-RES-001 | BCP tests completed | completed ÷ planned | 100% / 80–99% / < 80% | Q | * |
| KRI-RES-002 | Critical operations without tested tolerance | count | 0 / 1 / > 1 | Q | B U N A |
| KRI-ESG-001 | Exposure to climate-vulnerable states | share of AUM | < 20% / 20–35% / > 35% | Q | B N C |
| KRI-ESG-002 | BRSR data completeness | indicators with assured data | > 90% / 70–90% / < 70% | Y | L |
| KRI-GOV-001 | Board/committee meetings below quorum or missed minimum frequency | count | 0 / — / ≥ 1 | Q | * |
| KRI-GOV-002 | Fit-and-proper declarations pending (31 March) | count after due | 0 / — / ≥ 1 | Y | B U N A Q |
| KRI-GOV-003 | RPTs without prior approval | count | 0 / — / ≥ 1 | Q | L K N |
| KRI-GOV-004 | Co-op election overdue | months overdue | 0 / ≤ 3 / > 3 | M | C |
| KRI-GOV-005 | Independent-director vacancy beyond allowed period | days | 0 / ≤ 30 / > 30 | Event | L N |
| KRI-INS-001 | Claims ratio vs pricing | R80 − priced | < 2 pp / 2–5 / > 5 pp | Q | Q |
| KRI-INS-002 | 13th-month persistency | R83 | > 80% / 70–80% / < 70% | Q | Q |
| KRI-INS-003 | Reserve deficiency (actuarial) | reported deficiency | 0 / — / > 0 | Y | Q |
| KRI-INS-004 | EoM compliance | R82 vs limit | < 90% / 90–100% / > 100% | Q | Q |
| KRI-ARC-001 | Assets beyond resolution period | R74 | 0 / 1–2 / > 2 | Q | A |
| KRI-ARC-002 | SRs rated below investment grade | R76 share | < 20% / 20–40% / > 40% | H | A |
| KRI-FND-001 | Redemption pressure | redemptions ÷ AUM (week) | < 2% / 2–5% / > 5% | W | M F |
| KRI-FND-002 | Valuation exceptions | prices overridden ÷ securities | < 1% / 1–3% / > 3% | M | M F |

Total: 172 KRIs. Each pack enables its family subset; seed counts per pack: TAX-NBFC ML 31 (core default set), TAX-BANK 45, TAX-UCB 30, TAX-ARC 18, TAX-COOP 20, TAX-SEBI-MF 22, TAX-SEBI-AIF 15, TAX-SEBI-LISTED 24, TAX-INS 25, TAX-CORP 18, TAX-LLP 12 (selection lists maintained in the pack file).

### H.8.2 People-risk data contract (from P13)

P13 publishes `PeopleMetricPublished` with aggregates only: `{legal_entity_id, department_id?, as_of, metric_id (R111–R117 etc.), value, population_size, suppression_applied}`; populations below 5 are suppressed to protect individuals (k-anonymity floor, Tenant may raise); POSH figures are counts only (NN-13). External HRMS feeds through P18 follow the same contract.

### H.8.3 Templates for KRI values and Lab data

| Template | Sheets | Key columns (row 1 group headers, row 2 column headers, data from row 3) | Validations |
|---|---|---|---|
| `LDC-DT-KRI-v1.0` | `KRI_Values`, `Rough`, `_Template_Info` | A Legal entity code · B KRI ID · C As-of date · D Value · E Unit · F Provenance note · G Evidence file name · H Comment | KRI ID from tenant list (named range `KRI_IDs`); date not in future; numeric value; unit must match definition |
| `LDC-DT-TB-v1.0` | `TB`, `Mapping`, `Rough`, `_Template_Info` | Entity · period end · account code · account name · Ind AS/AS line (dropdown) · opening · debit · credit · closing | Debits = credits; closing = opening + Dr − Cr; mapping complete |
| `LDC-DT-RAL-LOANSEG-v1.0` | `Segments`, `Rough`, `_Template_Info` | Product · asset class (Standard/SMA-0/SMA-1/SMA-2/Sub-standard/Doubtful-1/2/3/Loss) · ECL stage · sector · state · secured (Y/N) · risk-weight class · rate type · residual-maturity bucket · repricing bucket · count · principal · interest accrued · undisbursed · IRACP provision · ECL · collateral value · LTV band | Dropdowns from Rough; principal ≥ 0; ECL stage consistent with asset class (Stage 3 for NPA) |
| `LDC-DT-LOAN-v1.0` | `Loans`, `Rough`, `_Template_Info` | Pseudonymised loan id · pseudonymised counterparty id · group id · product · sanction date · sanction amount · outstanding · DPD · asset class · stage · rating · collateral · LTV · maturity · rate · reset | Rejects PII patterns (PAN regex, 10-digit mobile, e-mail, Aadhaar 12-digit) |
| `LDC-DT-EXPO-v1.0` | `Exposures` | Counterparty id · group id · on-BS · off-BS by CCF class · CRM type and amount · sector · connected flag · infrastructure flag | Exposure ≥ 0; CCF class valid |
| `LDC-DT-BORROWINGS-v1.0` + `LDC-DT-DEPOSITS-v1.0` | `Funding` | Instrument id · lender type (bank, NBFC, MF, insurer, public deposit, CP, NCD, ECB, sub-debt, PDI) · amount · rate · fixed/floating · reset date · maturity · put/call · rating trigger · covenant ids | Maturity ≥ as-of; covenant ids from list |
| `LDC-DT-INVEST-v1.0` | `Holdings` | ISIN/identifier · instrument type · classification (amortised cost/FVOCI/FVTPL) · listed · exchange · market-cap band · rating · issuer group · related party · quantity · cost · fair value · FV level · AIF category · lock-in end · acquisition route (IPO mainboard/SME, secondary, private placement) | FV level 1–3; AIF category I/II/III |
| `LDC-DT-RAL-HQLA-v1.0` | `HQLA` | Holding id · HQLA level (cash, Level 1, 2A, 2B equivalent per ALM para 68) · market value · haircut class · encumbered · monetisation test date | Haircut class matches level |
| `LDC-DT-RAL-OBS-v1.0` | `OBS` | Item id · type (undrawn, guarantee, LC, DLG, credit enhancement) · amount · CCF class · counterparty group · maturity | — |
| `LDC-DT-CAPITAL-v1.0` | `Instruments` | Instrument id · type (equity, CCPS, PNCPS, PDI, IPDI, sub-debt, LTSB) · amount · issue date · maturity · call date · step-up · eligibility tier | Sub-debt amortisation schedule computed |
| `LDC-DT-RAL-INS-v1.0` | `Solvency`, `ALM` | Period · line of business · ASM · RSM · solvency ratio · assets duration · liabilities duration | Ratio = ASM/RSM within rounding |
| `LDC-DT-RAL-COOP-v1.0` | `Society` | Period · share capital · reserves · deposits (members) · borrowings · loans (by type: against deposits, gold, personal surety, mortgage) · overdue · demand · investments (by avenue) · net profit · reserve-fund transfer | Investment avenue from State-specific list |

**Shared intake with P11 (review R4, 25 Oct 2026).** Trial balance, loan tape, exposures, borrowings, deposits, investments and capital instruments use the P11 data templates (`LDC-DT-TB`, `LDC-DT-LOAN`, `LDC-DT-EXPO`, `LDC-DT-BORROWINGS`, `LDC-DT-DEPOSITS`, `LDC-DT-INVEST`, `LDC-DT-CAPITAL`, FR-P11-16) — one upload feeds both the Return Studio and the Lab; P11 owns their field definitions and the columns listed above are the minimum the Lab reads. Only the Lab-specific datasets keep the `LDC-DT-RAL-*` prefix (`LOANSEG`, `HQLA`, `OBS`, `INS`, `COOP`). The names `LDC-DT-RAL-TB` (master X-09 example) and `LDC-DT-INVEST` (P15 FR-P15-34) are aliases of `LDC-DT-TB` and `LDC-DT-INVEST`.

All templates carry `_Template_Info` (template code, version, family, column-contract hash) and follow the importer framework (preview, row errors, commit, audit) used by P03/P11 (Appendix E conventions).

### H.8.4 KRIs added in v1.1 *(v1.1; seed library now 187)*

| KRI ID | KRI | Metric / definition | G / A / R (default) | Freq | Fam. |
|---|---|---|---|---|---|
| KRI-OPR-011 | CCM coverage of key controls | key controls with automated tests ÷ key controls | > 60% / 30–60% / < 30% | M | * |
| KRI-OPR-012 | Failed automated tests on key controls | count in period | 0 / 1–2 / > 2 | M | * |
| KRI-DQL-001 | Return data-quality score | average DQ score of runs due in period (P11 FR-P11-87) | > 95 / 85–95 / < 85 | M | B U N A C |
| KRI-DQL-002 | Manual share of KRI/RAS values | values with provenance MAN ÷ all values | < 10% / 10–25% / > 25% | Q | * |
| KRI-DQL-003 | Late data deliveries | data requests fulfilled after lead time ÷ requests | < 5% / 5–15% / > 15% | M | * |
| KRI-MOD-006 | AI suggestion acceptance without edit | accepted-unedited ÷ decided AI suggestions (band: too high may indicate automation bias) | 40–85% / 85–95% or 20–40% / > 95% or < 20% | Q | * |
| KRI-MOD-007 | AI guardrail incidents | guardrail violations + kill-switch activations | 0 / 1 / > 1 | Q | * |
| KRI-MOD-008 | Open model-drift alerts | drift alerts open > 30 days (credit, fraud, pricing models; Finbyx/Udofin feeds) | 0 / 1–2 / > 2 | M | B N |
| KRI-TPR-007 | Critical-process concentration on one cloud/SaaS provider | critical processes on top provider ÷ critical processes | < 50% / 50–75% / > 75% | Q | * |
| KRI-TPR-008 | Co-lending/LSP partner concentration | disbursement via top partner ÷ total disbursement | < 30% / 30–50% / > 50% | M | N B |
| KRI-CMP-012 | High-risk non-compliances | instances on High checkpoints ending not_complied or complied_late in period | 0 / 1–2 / > 2 | M | * |
| KRI-CMP-013 | Regulator observations past due | inspection/RBS observations past committed date (P26) | 0 / 1–2 / > 2 | M | B U N A C |
| KRI-STR-005 | Projected capital headroom (4 quarters) | min projected headroom − Board buffer (P09 FR-P09-65) | > 100 bps / 0–100 bps / < 0 | Q | B U N |
| KRI-ESG-003 | Physical-climate exposure share | portfolio in high-hazard districts ÷ portfolio (voluntary) | < 10% / 10–20% / > 20% | Q | B N C |
| KRI-GRP-003 | Red KRIs in foreign entities | count of red group-level KRIs contributed by other regional cells | 0 / 1 / > 1 | Q | groups |

### H.8.5 Early-warning trigger library *(v1.1; used by P08 FR-P08-61)*

| Trigger ID | Family | Rule (default; Tenant-adjustable within floors) | Inputs | Output |
|---|---|---|---|---|
| EWS-PRX-01 | Threshold proximity | KRI within 10% of red threshold and adverse for 2 observations | KRI observations | EWS card to risk owner |
| EWS-VEL-01 | Velocity | ≥ 2 RAG bands in one period, or 3-point slope above configured rate | KRI observations | EWS card |
| EWS-REG-01 | Regulatory change | P05 Update affecting obligations linked to High+ risks | P05 impact map | EWS card + ad hoc RCSA proposal |
| EWS-INC-01 | Incident cluster | ≥ 3 incidents/losses of same L2 type in 30 days | P08 §4G, P12 | EWS card |
| EWS-CMP-01 | Complaint spike | category volume ≥ 150% of 3-month average | P14 | EWS card to GRO and risk owner |
| EWS-AUD-01 | Repeat finding | same root cause in two consecutive audits | P10 | EWS card to CRO and IA |
| EWS-FND-01 | Funding/market | spread +100 bps, rating watch negative, or top-lender non-renewal signal | Finbyx, P09 | EWS card to CFO/ALCO |
| EWS-FRD-01 | Fraud EWS | red-flagged accounts per FRM Directions 2026 EWS framework [VERIFY para] | Finbyx/Udofin | EWS card to fraud monitoring |
| EWS-CAP-01 | Capital plan | projected headroom below Board buffer within horizon | P09 FR-P09-65 | EWS card to CRO/CFO |
| EWS-CCM-01 | Control failure | failed automated test on a key control | P04/P12 CCM | Control UNDER_REVIEW + EWS |

---

## H.9 Stress-scenario library (seed, 46 scenarios; 62 from v1.1)

Severity labels: **B** baseline, **A** adverse, **S** severe, **X** extreme/reverse. Magnitudes are **[REC]** defaults for tenant calibration; RBI FSR macro stress tests (baseline and adverse scenarios for SCBs, NBFCs, UCBs) and BCBS guidance are reference points, not prescriptions. Horizon default 4 quarters (ICAAP scenarios 12 quarters).

### H.9.1 Library

| ID | Name | Type | Sev. | Shocks (default) | Outputs emphasised | Applicability |
|---|---|---|---|---|---|---|
| SCN-CRD-01 | Default-rate stress — moderate | Sensitivity | A | Default rates × 1.5 across retail and MSME; LGD +10 pp | GNPA, NNPA, credit cost, CRAR | B U N C |
| SCN-CRD-02 | Default-rate stress — severe | Sensitivity | S | Default rates × 2.0; LGD +20 pp; recovery rate −20% | as above, PCA proximity | B U N C |
| SCN-CRD-03 | SMA migration shock | Sensitivity | A | 25% of SMA-1 and 50% of SMA-2 slip to NPA next quarter | NNPA, provisions | B U N |
| SCN-CRD-04 | Restructured-book relapse | Sensitivity | S | 40% of restructured book turns NPA | NNPA, CRAR | B N |
| SCN-CRD-05 | Unsecured retail stress | Sensitivity | S | Personal-loan and card default × 2.5; 125% RW book growth halted | Credit cost, CET1 | B N |
| SCN-CRD-06 | MSME sector shock | Sensitivity | S | MSME default × 2; CGTMSE claim delay 12 months | Liquidity, NNPA | B U N |
| SCN-CRD-07 | Microfinance event (state-level) | Sensitivity | S | 30% of portfolio in the most-concentrated state becomes 90+ DPD | Collection efficiency, NNPA, CRAR | N (MFI), B (SFB) |
| SCN-COL-01 | Gold price fall | Sensitivity | A/S | Gold −10% / −20% / −30%; auction realisation −5% | LTV breaches, margin calls, losses | N (gold), C, U |
| SCN-COL-02 | Property price fall | Sensitivity | A/S | Residential −20% / −30%; commercial −30% / −40% | LGD, HFC LTV | B U N |
| SCN-COL-03 | Equity collateral crash (LAS/LAMF) | Sensitivity | S | Equity −30% (large cap), −45% (mid), −60% (small); MF NAV −25% | Margin shortfall, losses | N B |
| SCN-COL-04 | Vehicle resale decline | Sensitivity | A | Resale values −15% / −25% | LGD | N |
| SCN-IRR-01 | Parallel +200 bps | Sensitivity | A | +200 bps all tenors; deposits/borrowings reprice per contract | EaR, ΔEVE, NIM | B U N C |
| SCN-IRR-02 | Parallel −200 bps | Sensitivity | A | −200 bps | EaR (asset-sensitive books) | B U N |
| SCN-IRR-03 | Steepener / funding-spread widening | Sensitivity | S | Short +100, long +250 bps; NBFC funding spread +150 bps | Cost of funds, NIM, ROA | N |
| SCN-IRR-04 | Investment book rate shock | Sensitivity | S | +250 bps (PV01-based) | MTM, OCI, capital | B N Q |
| SCN-LIQ-01 | Institution-specific run | Liquidity | S | No rollover of CP/ST borrowings for 30 days; 20% drawdown of undrawn commitments | Survival horizon, LCR, SLS | N B |
| SCN-LIQ-02 | Market-wide funding freeze | Liquidity | S | Bank lines frozen 60 days; MF/insurer funding halts; HQLA haircut +10 pp | Survival horizon, CFP | N |
| SCN-LIQ-03 | Deposit withdrawal (retail) | Liquidity | S | 10% retail and 20% digital-enabled deposits withdrawn in 30 days | LCR, survival | B U C N-D |
| SCN-LIQ-04 | Top-lender loss | Liquidity | A | Top-3 lenders do not renew maturing lines | SLS, funding plan | N A |
| SCN-LIQ-05 | Rating downgrade | Liquidity | S | Two-notch downgrade: covenant triggers, spread +200 bps, 30% CP not rolled | Liquidity, NIM | N |
| SCN-LIQ-06 | Collection-efficiency collapse | Liquidity | S | Collection efficiency −15 pp for 2 months | Inflows, survival | N C |
| SCN-LIQ-07 | MF scheme redemption stress | Liquidity | S | Redemption = max(historical worst, 20% of AUM in a week) | Liquid-asset cover | M |
| SCN-CON-01 | Largest borrower default | Concentration | S | Default of top-1 counterparty and its group | CRAR, NNPA | B N A |
| SCN-CON-02 | Top-5 default | Concentration | X | Default of top-5 counterparties/groups | CRAR, PCA | B N |
| SCN-CON-03 | Top-20 default (severe) | Concentration | X | Top-20 exposures: 50% default, LGD 50% | Capital, reverse-stress anchor | B N A |
| SCN-CON-04 | Sector collapse | Concentration | S | Largest sector default × 3 | NNPA, CRAR | B U N |
| SCN-CON-05 | State/geography shock (flood/drought) | Concentration | S | Most-concentrated state: collections −30% for 3 months; 15% default | Liquidity, NNPA | N C U |
| SCN-INV-01 | Equity market crash | Market | S | Large −20%, mid −30%, small −40%, SME IPO −50% | MTM, capital | N (ICC/CIC) F Q |
| SCN-INV-02 | AIF/REIT/InvIT markdown | Market | A | AIF NAV −20%; REIT/InvIT −15%; distribution cut 30% | Capital, income | N F |
| SCN-INV-03 | Credit-spread widening | Market | S | AAA +100, AA +200, A +350, BBB +500 bps | MTM, OCI | B N Q M |
| SCN-OPS-01 | Large operational loss (1-in-20) | Operational | A | Loss = P08 scenario-analysis 1-in-20 estimate | P&L, capital | * |
| SCN-OPS-02 | Severe operational loss (1-in-100) | Operational | S | Loss = 1-in-100 estimate; plus regulatory penalty | Capital | * |
| SCN-OPS-03 | Major internal fraud | Operational | S | Fraud loss = 1% of AUM (or Board-set); 50% provisioned in Q1 | Capital, reputation | N C U B |
| SCN-CYB-01 | Core-system outage | Cyber | S | 5-day core LMS/CBS outage: no collections, manual disbursal stop, customer compensation, forensic costs | Liquidity, P&L | * |
| SCN-CYB-02 | Ransomware with data breach | Cyber | X | 10-day outage + personal-data breach notification costs + DPDP penalty exposure (Schedule) + litigation | P&L, capital, reputation | * |
| SCN-REG-01 | Business restriction | Regulatory | S | Embargo on new disbursements in a product for 6 months (e.g., gold or digital lending) | Income, capital, liquidity | B N |
| SCN-REG-02 | Rule change (risk weight +25 pp) | Regulatory | A | Consumer-credit RW +25 pp (scenario) | CRAR | B N |
| SCN-MAC-01 | Macro adverse (FSR-style) | Macro | A | GDP growth −250 bps vs baseline; inflation +150 bps; repo +100 bps; unemployment up → GNPA via satellite elasticities | All key metrics, 4–12 quarters | B U N C |
| SCN-MAC-02 | Macro severe (FSR-style) | Macro | S | GDP growth −450 bps; repo +200 bps; asset prices −20% | All key metrics | B U N C |
| SCN-CLM-01 | Physical climate event (voluntary) | Climate | S | Cyclone/flood in coastal or flood-prone states: 20% default, collateral −15% in affected districts | NNPA, capital | B N C |
| SCN-CLM-02 | Transition shock (voluntary) | Climate | A | Carbon-intensive sectors: default × 2; valuation −20% | Credit, investments | B N |
| SCN-CORP-01 | Revenue and receivable shock | Corporate | S | Revenue −30%, receivable days +45, input costs +10% | Cash runway, DSCR, ICR, covenants | K L |
| SCN-COOP-01 | Society run and overdue spike | Co-operative | S | 15% member-deposit withdrawal in 30 days; overdue +10 pp; loss on deposit with a failed co-op bank | Liquidity, own funds | C U |
| SCN-INS-01 | Insurance catastrophe (imported) | Insurance | S | Cat loss as per actuarial scenario; reinsurer default of largest panel member | Solvency ratio | Q |
| SCN-REV-01 | Reverse stress — CRAR to minimum | Reverse | X | Solve default-rate multiplier so that CRAR = regulatory minimum | Breaking point, plausibility | B U N A |
| SCN-REV-02 | Reverse stress — liquidity failure | Reverse | X | Solve run-off % so that 30-day cumulative gap turns negative / LCR = 100% | Breaking point | B N C |
| SCN-CLM-03 *(v1.1)* | Transition pathway — orderly/disorderly (NGFS-style; voluntary) | Climate | A/S | Carbon-intensive sector defaults × 1.5 (orderly) / × 2.5 (disorderly); collateral values in affected sectors −15/−30% over 3 years | Credit cost, capital path | B N |
| SCN-CLM-04 *(v1.1)* | Chronic physical — heat stress | Climate | A | Labour-intensive MSME and agri borrowers in heat-exposed districts: collections −10% for 2 quarters; default × 1.3 | Collections, NNPA | N C B |
| SCN-CYB-03 *(v1.1)* | Critical cloud/SaaS provider outage | Cyber / third party | S | 7-day outage of the top hosting/LMS provider; manual fallback at 30% capacity; customer compensation | Liquidity, P&L, complaints | * |
| SCN-CYB-04 *(v1.1)* | Payment-rail outage | Cyber | A | UPI/NACH collection rail unavailable 72 hours; collections deferred; liquidity gap | Liquidity, collection efficiency | B N C |
| SCN-TPR-01 *(v1.1)* | Co-lending partner / LSP failure | Third party | S | Top co-lending partner or LSP exits; DLG invoked to cap; servicing transfer cost; 20% of pool slips one bucket | NNPA, liquidity, P&L | N B |
| SCN-DIG-01 *(v1.1)* | Social-media-driven digital run | Liquidity | X | 30-day outflow assumptions compressed into 5 days (deposits/CP/undrawn) | Survival horizon, LCR | B U N-D |
| SCN-AI-01 *(v1.1)* | Credit-model failure | Model | S | Approval quality degrades for one quarter before detection: new-vintage default × 2 | Vintage NPA, credit cost | B N |
| SCN-GEO-01 *(v1.1)* | Geopolitical commodity shock | Macro | S | Crude +40%, INR −10%, repo +75 bps; transport and import-dependent sectors default × 1.5 | All key metrics | B N K |
| SCN-FX-01 *(v1.1)* | Foreign-currency borrowing shock | Market | S | INR −15%; hedge cost +300 bps; unhedged ECB servicing stress | Capital, NIM, liquidity | N B K |
| SCN-PAN-01 *(v1.1)* | Pandemic-style lockdown | Macro | S | Collections −40% for 2 months; moratorium requests 20% of book; disbursements −60% | Liquidity, NNPA, capital | B U N C |
| SCN-IRR-05 to SCN-IRR-10 *(v1.1)* | BCBS IRRBB six standardised shocks | Sensitivity | A/S | Parallel up, parallel down, steepener, flattener, short up, short down (currency-specific magnitudes per BCBS IRRBB standard) [VERIFY Indian implementation] | ΔEVE, ΔNII | B |

### H.9.2 Propagation model defaults (transparent; tenant-calibrated)

- **Credit:** quarterly bucket-transition matrix (Standard → SMA-0 → SMA-1 → SMA-2 → NPA sub-classes) estimated from 8–12 quarters of tenant history (or Finbyx roll-rate aggregates); shocks scale transition probabilities; provisions = max(IRACP floor, ECL overlay) where both regimes apply; ECL overlay = stage-wise coverage × stressed stage balances (labelled "stress overlay").
- **Collateral:** LTV recomputation; accounts above caps trigger margin calls (cured share configurable) or auction losses.
- **Income:** NII = Σ (balance × yield) − Σ (funding × cost) with repricing per bucket; fees ∝ disbursement; opex fixed + variable; credit cost from provisions; tax at effective rate.
- **Capital:** retained earnings − dividends + raises; RWA via kernel on stressed balances; deductions updated.
- **Liquidity:** contractual ladder + stressed behaviour; HQLA after haircuts; survival horizon = first day cumulative net outflow > liquid resources.
- **Macro satellite:** GNPA_t = GNPA_{t−1} + β₁·ΔGDP + β₂·Δrate + β₃·Δunemployment proxy, with βs from tenant regression on ≥ 20 quarters where available, else conservative defaults from published RBI FSR sensitivities (documented in the model card) [REC]; flagged "model — requires validation" (P08 model inventory).

### H.9.3 Management-action library

Raise equity/compulsorily convertible instruments; issue sub-debt/PDI; securitise or direct-assign pools; slow disbursement growth; tighten underwriting; increase pricing; cut dividends; sell investments; draw committed lines; activate CFP; reduce opex; obtain parent support letter. Each action has lead time, feasibility under stress, capital/liquidity effect and approval body; actions appear in ICAAP §7 with credibility assessment.

### H.9.4 Bank stress-testing alignment (Commercial Banks CA Directions 2025, Annex IV)

The bank pack maps the Annex IV structure — governance (Board-approved policy, roles), design (sensitivity vs scenario; severity calibration), coverage (credit, market, interest-rate, liquidity, concentration and others), sensitivity shocks, frequency by size, use of results and documentation — to library entries and governance tasks [VERIFY section letters A–N and their exact headings before activation; OI-P09-02]. Banks below the size threshold set in Annex IV use the simple sensitivity set (SCN-CRD-01/02, SCN-IRR-01/04, SCN-LIQ-03, SCN-INV-03) [VERIFY].

---

## H.10 ICAAP document outlines

### H.10.1 NBFC template (nine parts; aligned with Finbyx RK7.2; NBFC CAP Directions 2025 Chapter V)

1. **Executive summary and Board attestation** — capital position, internal capital target, key risks, stress outcomes, conclusions, Board approval statement (date, minute reference).
2. **Business model and strategy** — products, channels, geographies, funding; 3-year plan (AUM, mix, profitability); strategic risks; growth vs capital.
3. **Governance and risk management** — Board, RMC, CRO (where mandatory), three lines, RAS and limits, policies, risk culture, remuneration alignment, use test.
4. **Material-risk inventory** — all P08 Level-1 categories scored for materiality; for each: definition, exposure, controls, KRIs, materiality conclusion and treatment (capital / buffer / management).
5. **Capital assessment per risk** — credit (Pillar 1 RWA + concentration add-on: HHI-based granularity adjustment or LGD multiplier method); operational (internal proxy, "ICAAP internal"); IRRBB (ΔEVE ±200 bps); market/investment (stress MTM); liquidity (buffer, not capital); strategic/reputational/compliance (scenario-based); model risk buffer (optional); group/contagion; climate (voluntary); aggregation (simple sum by default; diversification only with documented justification) → internal capital requirement vs available capital.
6. **Stress testing** — scenarios, assumptions, results by period, reverse stress, liquidity stress and survival horizon, PCA proximity under stress.
7. **Capital planning** — projected ratios per scenario (3 years), capital sources, management actions with credibility, internal capital target = regulatory minimum + stress buffer, dividend policy linkage, contingency capital plan.
8. **Validation, review and use test** — independent review (IA or external), model validations, data-quality statement (P09 DQ results), limitations, action plan from last year's review.
9. **Appendices** — data lineage (snapshot hash, sources), model inventory, assumptions register, glossary, Board/RMC minutes extracts, list of tables.

### H.10.2 Bank template

Maps one-to-one to the "Format of the ICAAP document" in Commercial Banks CA Directions 2025 Chapter V.D [VERIFY headings], covering at minimum: overview and governance; Pillar 1 and Pillar 2 risk assessment (credit concentration, IRRBB, liquidity, residual, securitisation, reputational, strategic, model, others — SREP risks in para 9); stress testing per Annex IV; capital planning and buffers (CCB, D-SIB, CCyB); risk data aggregation; internal review; Board approval (paras 6–7).

### H.10.3 Light template (UCB, ARC, IFSCA FC, voluntary)

(1) Summary and approval; (2) business and risk profile; (3) material risks and controls; (4) capital adequacy now and projected; (5) stress tests (5–8 scenarios); (6) actions and conclusions.

### H.10.4 ICAAP tables generated automatically

Capital build-up; RWA by class; internal capital by risk; available vs required capital; stress results per scenario and period; reverse-stress breaking points; capital plan; KRI/RAS status; loss-event summary; model inventory summary; DQ statement. All bound to the frozen snapshot; narrative fields only for text.

---

## H.11 Default scales and matrix

| Score | Likelihood (12 months) | Financial impact (default bands, % of net worth or Tier 1) | Regulatory | Customer | Reputational |
|---|---|---|---|---|---|
| 1 Rare | < 5% | < 0.25% | No breach | < 100 customers, no harm | Internal only |
| 2 Unlikely | 5–25% | 0.25–1% | Minor breach, self-reported | Limited inconvenience | Local/limited |
| 3 Possible | 25–50% | 1–2.5% | Reportable breach | Moderate harm, compensation | Regional media |
| 4 Likely | 50–75% | 2.5–5% | Penalty / supervisory action | Widespread harm | National media |
| 5 Almost certain | > 75% | > 5% | Licence restriction / PCA / prosecution | Systemic customer detriment | Sustained national/international |

Severity bands (L × I): 1–4 Low; 5–9 Medium; 10–15 High; 16–25 Critical (owner baseline Architecture Part 2 Tables 2-3/2-4). Corporate/LLP default financial bands use % of revenue or net worth (tenant choice).

---

## H.12 Glossary for "i" help (P23 keys `hlp.erm.*`, `hlp.ral.*`)

**Inherent risk** — level of risk before considering controls. **Residual risk** — level after the effect of controls. **Risk appetite** — the amount and type of risk the Board is willing to take to meet objectives; **tolerance** — acceptable variation around appetite; **limit** — hard boundary. **RAS** — Risk Appetite Statement approved by the Board. **KRI** — metric that signals rising risk; **KPI** — performance measure. **RCSA** — Risk and Control Self-Assessment by the first line, challenged by the second line. **Three lines of defence** — business (first), risk and compliance (second), internal audit (third). **CRAR** — capital to risk-weighted assets ratio. **CET1 / Tier 1 / Tier 2** — layers of regulatory capital by loss-absorbing quality. **RWA** — exposures weighted by risk. **Leverage (NBFC-BL)** — outside liabilities ÷ owned fund. **LCR** — high-quality liquid assets ÷ stressed 30-day net outflows. **NSFR** — stable funding available ÷ required. **SLS** — structural liquidity statement showing maturity mismatches by time bucket. **IRS / TGA / DGA** — interest-rate sensitivity via traditional gap and duration gap. **EaR / ΔEVE** — earnings-at-risk and change in economic value of equity. **IRRBB** — interest-rate risk in the banking book. **HQLA** — high-quality liquid assets. **CFP** — contingency funding plan. **ICAAP** — Internal Capital Adequacy Assessment Process. **SREP** — supervisor's review of the ICAAP. **Pillar 1/2/3** — minimum capital, supervisory review, market disclosure. **PCA** — Prompt Corrective Action framework. **Stress test** — what-if analysis under adverse conditions; **reverse stress test** — finds the conditions that break a threshold. **HHI** — Herfindahl-Hirschman Index of concentration. **Loss event / near miss** — operational failure with/without financial loss. **Impact tolerance** — maximum tolerable disruption of a critical operation. **Model risk** — risk of loss from incorrect models or misuse. **Provenance badge** — source of a number (FX Finbyx, UD Udofin, LDC computed, IMP imported, MAN manual). **Certified** — value validated, reviewed and signed by its owner.

---

## H.13 Sources (accessed 25 October 2026)

See `_research/S4_risk_capital_icaap.md` for notes. Primary: RBI Directions RBI/DOR/2025-26/345 (https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=12959), /151 (https://rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13159), /275 (https://rbi.org.in/SCRIPTS/BS_ViewMasDirections.aspx?id=13030), /355 (https://rbi.org.in/scriptS/BS_ViewMasDirections.aspx?id=12949), /351 (https://rbi.org.in/ScriptS/BS_ViewMasDirections.aspx?id=12953); RBI/DoS/2026-27/467 (https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13586) and /463 (https://rbi.org.in/SCRIPTs/BS_ViewMasDirections.aspx?id=13590); RBI draft MRM guidance press release 24 Jun 2026 (https://rbi.org.in/ScriptS/BS_PressReleaseDisplay.aspx?prid=63006); RBI ORM Guidance Note (https://www.rbi.org.in/Scripts/NotificationUser.aspx?Id=12679); RBI draft NBFC climate directions (https://rbi.org.in/Scripts/BS_ViewREwiseDraftDirections.aspx?id=207); IFSCA FC prudential circular (https://www.ifsca.gov.in/Document/Legal/circular-on-fc-prudential-regulation-and-activity-specific-regulation03052021072520.pdf); BCBS Basel Framework (https://www.bis.org/basel_framework/), BCBS 239 progress (https://www.bis.org/bcbs/publ/d559.htm); Insurance Act 1938 s.64VA and IRDAI AFIF Regulations 2024 (summary https://www.oquilia.com/news/irdai-actuarial-finance-investment-functions-regulations-2024). Internal: Finbyx Master Prompt v1.5 Part 7E; Infrabyx Ecosystem Integration Specification v1.1 §6.22; owner's LawDocs Comply Architecture Part 2. Practitioner: Vinod Kothari (Jul 2025) ICAAP for NBFCs (https://vinodkothari.com/2025/07/mind-the-gap-plugging-risk-blind-spots-with-icaap-for-nbfcs/).

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular D-22, X-16, X-25, NN-38, NN-39. Where text above conflicts with them, the master prevails.
