# Appendix G — Legal and Regulatory Rules Register

> **Binding for:** P03 (content library), P04 (compliance instances), P05 (change management), P06 (governance), P08–P11 (risk, audit, returns), P12–P16 (data/cyber, HRMS/labour, grievance, sector packs, co-operatives), P20–P21 (billing and marketplace conduct).
> **Prepared:** 25 October 2026 (LawDocsComply Build Prompt Pack v1.0). **Owner:** LDC regulatory content team (CS + CA + counsel).
> **Precedence:** this appendix is the authority for *what the law says* where the product's logic depends on it; P15 parameters (`pack.parameter`) must cite an `LR-*` row; a conflict between a phase file and this appendix is resolved in favour of this appendix, then corrected in the phase file.

>
> **v1.1 changes (25 October 2026)**
> - New **§G.16A rules for v1.1 modules** — AI governance (`OV_AI`, P12 §4P), ESG/BRSR/CSR (P27), litigation provisioning and disclosure (P26), AML_RE and MSME_FIRM families (P15 §4P), and international stubs for P25 (all status-tagged; VERIFY rows advisory only, NN-38). New authority codes: `STD` (international standards), `LAW` (general statutes), `UK`, `AE`, `SG`.
> - LR-RBI-101 count wording reconciled (238 function-wise per press release; 244 serials /143–/386 under RBI/2025-26/100, 240 live after 10 Mar 2026; 9,445 circulars withdrawn) and pointed to the v1.1 catalogue (D-39).
> - LR-RBI-055 Internal Ombudsman reference: RBI/CEPD/2025-26/383 or /384 [VERIFY] (catalogue lists /383 for NBFCs); sibling IO directions for banks (/380–/382) and credit information companies (/385) added as LR-RBI-056.
> - Rule 1 for engineers cites NN-38; withdrawn instruments can never be current citations (NN-55).
---

## G.0 How to use this register

**Purpose.** The compliance *questions* (Part 2 Excel sheets) cover every obligation in every instrument. This register is narrower: it lists the rules that **drive product behaviour** — applicability thresholds, classification tests, clocks, limits, composition rules, hard blocks, disclosure and filing timelines, and conduct constraints — so that engineers can encode them as data (rule packs and parameters, P02/P15) with a citation and a test.

**Fields.**

| Field | Meaning |
|---|---|
| LR ID | `LR-<AUTH>-<NNN>`; never reused; superseded rows stay with status `SUPERSEDED` and a pointer |
| Rule | The product-relevant statement of the rule |
| Citation | Instrument, number, date and paragraph/section |
| Effective | Effective date or period (and transition) |
| Product behaviour | What LDC does: parameter, detector, clock, block, seed, disclosure, return |
| Tier | **L** Locked (law; no tenant may loosen), **G** Governed (content team parameterises; changes by versioned release with maker-checker), **T** Tenant may tighten (never loosen below the L/G floor) |
| Status | **V-OFF** verified against the official text supplied to the Infrabyx programme (Finbyx v1.5 Part 8A); **V-WEB** checked against the regulator's own web page; **SEC** reputable secondary source; **VERIFY** not yet checked — must be verified before the dependent feature leaves its flag |

**Rules for engineers.**
1. A row with status `VERIFY` may seed content and tasks but must not drive a **hard block** *(NN-38)* or a **Critical** issue until verified; it drives a `HIGH` advisory instead (flag `rules.unverified_as_advisory = true`, Locked; master NN-38).
2. Every row used in code has a golden test referencing its LR ID (`LR-RBI-012_*`).
3. Amendments create a new row version (`LR-RBI-012 v2`) with effective dates; old versions remain for replay (NN-07).
4. Paragraph numbers for RBI 2025–26 Directions come from the copies verified in Finbyx v1.5 Part 8A unless marked otherwise; later amendments are checked separately.

---

## G.1 RBI — Non-Banking Financial Companies

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-RBI-001 | Base Layer = non-deposit NBFCs with assets < ₹1,000 crore, plus P2P, AA, NOFHC and NBFCs with no public funds and no customer interface (these four always BL) | SBR Directions 2025, RBI/DOR/2025-26/339, paras 10, 15(1) | 28 Nov 2025 | Layer classifier; parameter `NBFC.ML_ASSET_THRESHOLD` | L | V-OFF |
| LR-RBI-002 | Middle Layer = all NBFC-D; non-deposit NBFCs with assets ≥ ₹1,000 crore; SPD, IDF, CIC, HFC, IFC (never BL; SPD and IDF always ML) | SBR paras 11, 15(2) | 28 Nov 2025 | Layer classifier | L | V-OFF |
| LR-RBI-003 | ICC, MFI, Factor and MGC can be in any layer | SBR para 15(3) | 28 Nov 2025 | Layer classifier | L | V-OFF |
| LR-RBI-004 | Upper Layer only as identified by RBI (top 10 by assets always UL; scoring of top 50); Government NBFCs not placed in UL until further notice | SBR paras 12, 15(4), 24–26 | 28 Nov 2025 | UL only on recorded RBI advice; never computed | L | V-OFF |
| LR-RBI-005 | UL transition: Board policy and implementation plan within 3 months of RBI advice; full compliance within 24 months; minimum 5 years in UL unless voluntary scale-down under Board policy | SBR paras 27–29 | 28 Nov 2025 | Milestone clocks from advice date; 5-year floor | L | V-OFF |
| LR-RBI-006 | Group consolidation for ML: consolidated assets of CoR-holding group NBFCs (incl. always-BL entities and certain unregistered CICs < ₹100 crore with public funds) ≥ ₹1,000 crore → every ICC, MFI, Factor and MGC in the group is ML; auditor certifies group asset size as on 31 March annually; not used for UL | SBR paras 17–21 | 28 Nov 2025 | Group-level classifier; annual auditor certificate task | L | V-OFF |
| LR-RBI-007 | ML rules apply from the date assets reach ₹1,000 crore, not the balance-sheet date | SBR para 22 | 28 Nov 2025 | `first_crossed` effective date | L | V-OFF |
| LR-RBI-008 | After a temporary dip below ₹1,000 crore an NBFC stays ML until its next audited balance sheet and a specific RBI dispensation | SBR para 23 | 28 Nov 2025 | Downgrade only with dispensation evidence | L | V-OFF |
| LR-RBI-009 | Principal business criteria: financial assets > 50% of total assets (net of intangibles) and income from financial assets > 50% of gross income, on last audited balance sheet | SBR para 38 | 28 Nov 2025 | Annual PBC test; issue on failure | L | V-OFF |
| LR-RBI-010 | NOF: ICC/MFI/Factor ₹10 crore (glide: ICC ₹5 crore by 31 Mar 2025 → ₹10 crore by 31 Mar 2027); P2P, AA, no-public-funds-no-interface ₹2 crore; IFC and IDF ₹300 crore | SBR paras 39–42 | Glide to 31 Mar 2027 | NOF monitor with glide-path milestones | L | V-OFF |
| LR-RBI-011 | NOF deductions: exposure to subsidiaries, group companies, other NBFCs above 10% of owned funds; look-through for group investments via an AIF where ≥ 50% of AIF funds from the NBFC | SBR paras 45–46 | 28 Nov 2025 | NOF computation input; investment monitor | L | V-OFF |
| LR-RBI-012 | New investors from FATF non-compliant jurisdictions together < 20% of voting power (incl. potential); existing grandfathered | SBR paras 47–48 | 28 Nov 2025 | Shareholding attribute check | L | V-OFF |
| LR-RBI-013 | Public funds exclude instruments compulsorily convertible into equity within 5 years; definitions of customer interface and group | SBR paras 6(3), 6(4), 6(18) | 28 Nov 2025 | Definitions for profile attributes ("i" help) | L | V-OFF |
| LR-RBI-014 | Unregistered Type I NBFC: no public funds (incl. indirect via associates/group), no customer interface, group assets < ₹1,000 crore → may operate unregistered, exempt from ss.45-IA/45-IC; application via PRAVAAH by 31 Dec 2026; annual Board resolution, disclosure, auditor exception reporting | SBR Amendment Directions 2026, RBI/2026-27/43, 29 Apr 2026 | 1 Jul 2026 | Type I eligibility detector; deregistration checklist (no filing) | L | SEC (Finbyx IV5.7) |
| LR-RBI-015 | Section 8 microfinance companies meeting conditions (microfinance only, household obligations ≤ 50% of income, no deposits, assets < ₹100 crore) exempt from ss.45-IA, 45-IB, 45-IC | SBR para 51 | 28 Nov 2025 | Type `S8_MFI_EXEMPT` applicability | L | V-OFF |
| LR-RBI-016 | Compliance Function Directions apply to Middle and Upper Layer only (CCO, compliance policy, compliance risk assessment, reporting to Board) | NBFC – Compliance Function Directions 2026, RBI/DoS/2026-27/460, para 3 | 31 Jul 2026 | Applicability rule; seeds CCO role and compliance policy | L | V-OFF |
| LR-RBI-017 | Cybersecurity, Technology Risk Directions: Ch II all NBFCs incl. HFC; Ch III BL < ₹500 crore and all CICs; Ch IV BL ≥ ₹500 crore; Ch V TL/UL/ML excluding CICs | NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework Directions 2026, RBI/DoS/2026-27/461, para 3 | 31 Jul 2026 (immediate) | Chapter-wise applicability; IT Strategy/Steering committees for Ch V | L | V-OFF |
| LR-RBI-018 | Digital Payment Security Controls apply only to credit-card-issuing NBFCs | RBI/DoS/2026-27/462 | 31 Jul 2026 | Attribute `credit_card_issuer` | L | V-OFF |
| LR-RBI-019 | Fraud Risk Management applies to UL, ML, and BL with assets ≥ ₹500 crore (audited 31 March), incl. HFCs (reporting to NHB) | RBI/DoS/2026-27/463, para 3 | 31 Jul 2026 | Applicability; seeds Special Committee for fraud monitoring | L | V-OFF |
| LR-RBI-020 | Internal Audit Function Directions apply to all NBFC-D and HFC-D and NBFC-ND/HFC-ND with assets ≥ ₹5,000 crore | RBI/DoS/2026-27/464, para 3 | 31 Jul 2026 | Applicability; RBIA seeds (P10) | L | V-OFF |
| LR-RBI-021 | Statutory Audit Directions: SCA/SA appointment rules for all NBFCs incl. HFCs; NBFC-ND < ₹1,000 crore may continue extant procedure | RBI/DoS/2026-27/465, para 3 | 31 Jul 2026 | Auditor appointment workflow (P10) | L | V-OFF |
| LR-RBI-022 | Supervisory Returns Directions apply to all NBFCs, all layers, HFCs excluded; return-wise applicability in para 21 | RBI/DoS/2026-27/466, paras 3, 21 | 31 Jul 2026 | Returns catalogue binding (Appendix I) | L | V-OFF |
| LR-RBI-023 | Owner reference "supervisory returns master directions of 28 Nov 2025" corresponds to the DoS Supervisory Returns Directions of 31 Jul 2026 (the 28 Nov 2025 set is the DoR prudential set) | Finbyx v1.5 Part 8A.37.1 item 1 | — | Errata note shown in content library | G | V-OFF |
| LR-RBI-024 | Miscellaneous Supervisory Directions: Ch II for UL/ML with ≥ 10 fixed-point service delivery units; Ch III incl. HFCs and MFIs; Ch IV NBFC-D excl. HFCs; Ch V NBFC-D and ML/UL/TL ND excl. no-public-funds NBFCs, PDs, HFCs | RBI/DoS/2026-27/467, para 3 | 31 Jul 2026 | Chapter applicability; attribute `fixed_point_units` | L | V-OFF |
| LR-RBI-025 | Auditor's Report Directions apply to every NBFC auditor (HFC auditors excluded); first for FY ending on/after 31 Jul 2026 | RBI/DoS/2026-27/468 | FY ending ≥ 31 Jul 2026 | Audit report checklist (P10) | L | V-OFF |
| LR-RBI-026 | DoS Directions of 31 Jul 2026 repeal earlier instructions through circular DoS.CO.PPG.66/11.01.005/2026-27 | Repeal circular | 31 Jul 2026 | Supersession records in content library | G | VERIFY (repeal list) |
| LR-RBI-027 | Governance Directions: BL Ch III; ML Ch II–IV; UL Ch II–V incl. HFC; partial for CIC/MGC/SPD/AA/P2P; paras 29–37 not for government-owned NBFCs | NBFC – Governance Directions 2025, RBI/DOR/2025-26/344, para 3 | 28 Nov 2025 | Seeds committees/KMP by layer (P15 §4F) | L | V-OFF |
| LR-RBI-028 | Capital adequacy by layer for NBFC-D, ICC, Factor, IFC, IDF, MFI; HFC/MGC/CIC/SPD listed paras only; not P2P, AA, NOFHC, no-public-funds | NBFC – Capital Adequacy Directions 2025, RBI/DOR/2025-26/345, para 3 | 28 Nov 2025 (upd. 1 Apr 2026) | CRAR monitor (P09); ratio library (App. H) | L | V-OFF |
| LR-RBI-029 | Concentration limits (ML): single ≤ 25% / group ≤ 40% of Tier 1 (+5/+10 for infrastructure); IFC 30%/50%; UL large-exposure 20% (+5% Board) single, 25% group of eligible capital base; CME within Board limit | NBFC – Concentration Risk Management Directions 2025, RBI/DOR/2025-26/351, paras 12–14, 24, 33–39 | 28 Nov 2025 (amend. 1 Jan and 10 Mar 2026) | Investment/credit concentration monitors (Finbyx feed) | L | V-OFF |
| LR-RBI-030 | Single/group limits not applied where the NBFC has no public funds and has issued no guarantees | CON para 16 | 28 Nov 2025 | Automatic exemption, re-tested monthly | L | V-OFF |
| LR-RBI-031 | IPO funding ≤ ₹1 crore per borrower | CON paras 11, 24(2); CF para 104 | 28 Nov 2025 | Monitor (Finbyx-enforced) | L | V-OFF |
| LR-RBI-032 | Investment portfolio classification/valuation; inter-class transfers only on 1 April/1 October with Board resolution; AS-13 category-wise depreciation | NBFC – Investment Portfolio Directions 2025, RBI/DOR/2025-26/354, paras 10, 14–24 | 28 Nov 2025 | Investment compliance view | L | V-OFF |
| LR-RBI-033 | ALM: all layers incl. HFC; Ch II only if assets ≥ ₹100 crore; Ch III (LCR) only for NBFC-D and NBFC-ND ≥ ₹5,000 crore | NBFC – ALM Directions 2025, RBI/DoR/2025-26/355, para 3 | 28 Nov 2025 | ALCO seed; LCR monitor applicability | L | V-OFF |
| LR-RBI-034 | IRACP: NBFC-D, ICC, Factor, IFC, IDF; HFC/MFI/MGC/CIC own Directions prevail; not P2P, AA, SPD, NOFHC | NBFC – IRACP Directions 2025, RBI/DOR/2025-26/356, paras 3–10 | 28 Nov 2025 (upd. 13 Feb 2026) | NPA/provision ratios (App. H); audit checks | L | V-OFF |
| LR-RBI-035 | Resolution of Stressed Assets: Part A for NBFC-D and ND ≥ ₹500 crore; Part B for ND < ₹500 crore | NBFC – RSA Directions 2025, RBI/DOR/2025-26/357, paras 7–8 | 28 Nov 2025 | Applicability; policy seed | L | V-OFF |
| LR-RBI-036 | Wilful/Large Defaulters: ML and above (bar on further finance and large-defaulter provisions apply to all REs); Review Committee | NBFC – WD Directions 2025, RBI/DOR/2025-26/358, paras 2–3 | 28 Nov 2025 | Committee seed; policy seed | L | V-OFF |
| LR-RBI-037 | Financial Statements disclosures: C.1 all, C.2 ML/UL, C.3 UL; CME disclosure lines para 21(8)(ii) | NBFC – FS Directions 2025, RBI/DOR/2025-26/359 | 28 Nov 2025 (upd. 1 Apr 2026) | Annual report checklist (P06/P11) | L | V-OFF |
| LR-RBI-038 | Dividend declaration prudential norms (all layers incl. HFC, MGC, SPD, CIC, P2P, AA; not NOFHC) | NBFC – DIV Directions 2025, RBI/DOR/2025-26/360 | 28 Nov 2025 | Board agenda checklist for dividend | L | V-OFF |
| LR-RBI-039 | KYC: all NBFC categories; not NBFCs without customer interface; Aadhaar e-KYC authentication only for NBFCs notified under PMLA s.11A; CKYCR reliance explanation | NBFC – KYC Directions 2025, RBI/DOR/2025-26/361, paras 3, 63(9) | 28 Nov 2025 (upd. 29 Dec 2025) | Applicability; KYC policy seed; periodic updation obligations | L | V-OFF |
| LR-RBI-040 | Responsible Business Conduct: applicable to NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC; P2P paras 98–100 only; GRO and grievance mechanism; contact hours 08:00–19:00 (para 100) | NBFC – RBC Directions 2025, RBI/DOR/2025-26/362, paras 3–5, 100 | 28 Nov 2025 (upd. 1 Apr 2026) | GRO role seed; grievance clocks (P14) | L | V-OFF |
| LR-RBI-041 | RBC Third Amendment (paras 100A–100AB) — recovery conduct additions | RBI/2026-27/230, 6 Aug 2026 | 1 Jan 2027 | Content pack version scheduled | L | SEC |
| LR-RBI-042 | Credit Facilities incl. digital lending (Ch III) for NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC; partial for BL with interface but no public funds, CICs, P2P | NBFC – Credit Facilities Directions 2025, RBI/DOR/2025-26/347, para 3 | 28 Nov 2025 (upd. 1 Apr 2026) | Applicability; LSP oversight obligations link to Udofin | L | V-OFF |
| LR-RBI-043 | Credit information reporting: incremental files on the 9th, 16th and 23rd within 4 calendar days and month-end full file by the 5th | NBFC – CIR Directions 2025 para 10(2) as substituted by RBI/DOR/2025-26/117 | 1 Jul 2026 | CIC submission calendar (P11) | L | V-OFF |
| LR-RBI-044 | Outsourcing: NBFC-D, ICC, Factor, MFI, IFC, IDF, HFC, SPD, CIC, P2P, AA; BL excludes Ch IV and IT parts of Ch II; existing IT agreements compliant by renewal or 10 Apr 2026 | NBFC – OUT Directions 2025, RBI/DOR/2025-26/363, paras 2–3 | 28 Nov 2025 | TPRM applicability (P12) | L | V-OFF |
| LR-RBI-045 | Climate finance Directions only for NBFC-D and deposit-taking HFCs | NBFC – CLM Directions 2025, RBI/DOR/2025-26/364 | 28 Nov 2025 | Applicability | L | V-OFF |
| LR-RBI-046 | NBFC-MFI: ≥ 60% qualifying assets; household-income cap 50% for microfinance loans; any NBFC's microfinance loans ≤ 25% of assets unless MFI | NBFC – MFI Directions 2025, RBI/DOR/2025-26/371, paras 8(3), 12, 49; CF paras 51, 55–57 | 28 Nov 2025 | Type test; monitor | L | V-OFF |
| LR-RBI-047 | Transfer and distribution of credit risk: co-lending Part B from 1 Jan 2026; acquired stressed loans held ≥ 6 months; no re-acquisition from ARC of own transferred loans; co-operatives excluded as co-lending partners | NBFC – TDCR Directions 2025, RBI/DOR/2025-26/352, paras 2, 7, 12(4), 74, 87, 95, 97 | 28 Nov 2025 | Guard-rail obligations (P15 §4H; P16) | L | V-OFF |
| LR-RBI-048 | Securitisation: NBFCs as originators/investors; MHP/MRR; recycling rules | NBFC – SEC Directions 2025, RBI/DOR/2025-26/353 | 28 Nov 2025 | Applicability; policy seed | L | V-OFF |
| LR-RBI-049 | Branch authorisation (deposit-taking specific paras 6, 12) | NBFC – BR Directions 2025, RBI/DOR/2025-26/342 | 28 Nov 2025 (upd. 15 Apr 2026) | Branch opening checklist | L | V-OFF |
| LR-RBI-050 | Miscellaneous Directions: Ch II all; Ch III ML+; Ch IV Factors; Ch V IDF; reporting of directors, principal officers, addresses (paras 6–7) | NBFC – MISC Directions 2025, RBI/DOR/2025-26/373 | 28 Nov 2025 (upd. 26 Feb 2026) | Event-based intimation obligations (change of director, address) | L | V-OFF |
| LR-RBI-051 | Account Aggregator Directions apply only to NBFC-AAs | RBI/DoR/2025-26/368 | 28 Nov 2025 | Applicability | L | V-OFF |
| LR-RBI-052 | HFC Directions 2025; HFCs report to NHB and are excluded from NBFC SR | HFC Directions, RBI/DoR/2025-26/365 | 28 Nov 2025 (upd. 1 Oct 2026) | HFC return set from NHB [VERIFY list] | L | SEC |
| LR-RBI-053 | Core Investment Companies: group investment ≥ 90% and group equity ≥ 60% of net assets; ANW/RWA ≥ 30%; outside liabilities ≤ 2.5 × ANW; ≤ 2 CIC layers; registration where assets ≥ ₹100 crore and public funds; GRMC | CIC Directions 2025, RBI/DOR/2025-26/367, paras 3, 11, 15–17, 19–20, 23, 69–71 | 28 Nov 2025 (upd. 10 Mar 2026) | CIC monitors (P15 §4G) | L | SEC [VERIFY paras] |
| LR-RBI-054 | Operational Risk Management and Operational Resilience — **guidance**, not a Direction; strength flag "guidance" | DOR.ORG.REC.301/14.10.001/2025-26 | 28 Nov 2025 | Shown as guidance; never a statutory breach | G | V-OFF |
| LR-RBI-055 | Internal Ombudsman for NBFCs (2026 Directions replacing 2023): automatic escalation of wholly/partly rejected complaints; HFCs excluded | NBFC – Internal Ombudsman Directions 2026, RBI/CEPD/2025-26/383 or /384 [VERIFY] *(v1.1)* | 14 Jan 2026 | IO role and escalation in P14 | L | SEC [VERIFY scope/number] |
| LR-RBI-056 | Gold-primary NBFC flag affects capital (CAP 4(8)) | CAP para 4(8) | 28 Nov 2025 | Profile attribute | L | V-OFF |
| LR-RBI-056 *(v1.1)* | Internal Ombudsman Directions 2026 issued in parallel for commercial banks, SFBs, payments banks, credit information companies and non-bank PPI issuers; IO review of partly/wholly rejected complaints before final reply | RBI/CEPD/2025-26/380 (CB), /381 (SFB), /382 (PB), /385 (CIC-CI), /384 (non-bank PPI) [VERIFY all] | 14 Jan 2026 | P14 ladders per family; NN-40 | L | VERIFY |

## G.2 RBI — Banks, co-operative banks and AIFIs

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-RBI-101 | RBI consolidated its regulations on 28 Nov 2025: 238 function-wise Master Directions per the press release, issued as 244 serials (RBI/DOR/2025-26/143–/386) under circular RBI/2025-26/100 for 11 categories of REs (commercial banks, SFBs, PBs, LABs, RRBs, UCBs, RCBs, AIFIs, NBFCs, ARCs, credit information companies), of which 240 are live after four 2025 dividend directions were replaced on 10 Mar 2026; 9,445 circulars withdrawn *(v1.1)* | RBI press release 2025-2026/1588; RBI/2025-26/100 and Annex; `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx` | 28 Nov 2025 | Content base for every RBI family (D-39); one sheet per direction per category with sibling links (D-40); concordance old→new (P05); NN-55 | G | V-WEB (titles) / VERIFY (serials) |
| LR-RBI-102 | Commercial bank capital: CET1 5.5%, Tier 1 7%, total 9% plus CCB 2.5%; leverage ratio 4% (D-SIBs), 3.5% (others) | Commercial Banks – Capital Adequacy Directions 2025 | 28 Nov 2025 | Ratio thresholds (App. H) | L | SEC [VERIFY paras] |
| LR-RBI-103 | Commercial banks — RBIA mandated; excludes SFBs, PBs, LABs | Commercial Banks – Internal Audit Function Directions 2026, RBI/DoS/2026-27/413, para 3 | 31 Jul 2026 (upd. 1 Oct 2026) | P10 applicability | L | V-WEB |
| LR-RBI-104 | Commercial banks — concurrent audit | Commercial Banks – Concurrent Audit Directions 2026 | 31 Jul 2026 | P10 concurrent audit module | L | VERIFY |
| LR-RBI-105 | Commercial banks — 37 supervisory returns with timelines in para 22 | Commercial Banks – Supervisory Returns Directions 2026, RBI/DoS/2026-27/415 | 31 Jul 2026 | Returns catalogue (App. I) | L | V-WEB [VERIFY rows] |
| LR-RBI-106 | ECL-based asset classification and provisioning for scheduled commercial banks | Commercial Banks – Asset Classification, Provisioning and Income Recognition Directions 2026, RBI/DOR/2026-27/398 | 1 Apr 2027 | Scheduled content version; ratio changes | L | SEC |
| LR-RBI-107 | Credit risk standardised approach revisions (excl. SFB, PB, LAB) | Commercial Banks – Capital Charge for Credit Risk – Standardised Approach Directions 2026 | 1 Apr 2027 | Scheduled content version | L | SEC |
| LR-RBI-108 | LCR and NSFR ≥ 100% for applicable banks | Bank liquidity directions (consolidated 2025) | in force | Ratio thresholds | L | VERIFY |
| LR-RBI-109 | PSL targets: SCBs 40% of ANBC/CEOBE; RRBs and SFBs 75% [VERIFY]; UCBs 60% from 1 Apr 2025 | PSL Directions | in force | PSL dashboard widget | L | VERIFY |
| LR-RBI-110 | UCB four tiers: Tier 1 (unit and salary-earner UCBs; others ≤ ₹100 cr deposits), Tier 2 (₹100–1,000 cr), Tier 3 (₹1,000–10,000 cr), Tier 4 (> ₹10,000 cr) | RBI circular of 1 Dec 2022; UCB Directions 2025 | in force | UCB tier classifier | L | SEC |
| LR-RBI-111 | UCB minimum CRAR: Tier 1 9%; Tiers 2–4 12% (glide completed FY 2025-26); minimum net worth ₹2 cr (single-district Tier 1) / ₹5 cr others | UCB Capital Adequacy Directions 2025 | in force | Ratio thresholds | L | SEC [VERIFY] |
| LR-RBI-112 | UCB Supervisory Action Framework triggers (capital, asset quality, profitability) | UCB SAF instructions (consolidated) | in force | SAF monitor | L | VERIFY |
| LR-RBI-113 | UCB returns on CIMS under UCB Supervisory Returns Directions 2026 | UCB SR Directions 2026 | 31 Jul 2026 | Returns catalogue | L | VERIFY |
| LR-RBI-114 | StCBs/DCCBs supervised by NABARD (BR Act s.35(6)); ENSURE returns (e.g., OSC-10 quarterly; cyber incident CSIR-01 within 6 hours) | BR Act s.35(6); NABARD instructions | in force | RCB returns; incident clock | L | SEC [VERIFY] |
| LR-RBI-115 | Co-operative banks may not co-lend with NBFCs; transfer stressed loans only as transferor | TDCR paras 7, 12(4), 58, 97 (NBFC side); UCB TDCR [VERIFY] | 28 Nov 2025 | Guard-rail obligations | L | V-OFF (NBFC side) |
| LR-RBI-116 | Director tenure in UCBs ≤ 10 years [VERIFY]; Board of Management for UCBs above threshold [VERIFY] | UCB Governance Directions 2025 | in force | Board composition checks | L | VERIFY |
| LR-RBI-117 | RBI regulates; State/MSCS Registrar handles registration, elections, audit for co-operative banks (dual control) | BR Act s.56 (AACS); State Acts; MSCS Act | in force | Multi-family membership `UCB` + co-op Act | L | SEC |
| LR-RBI-118 | AIFIs (NABARD, SIDBI, EXIM, NHB, NaBFID) have their own function-wise Directions | RBI Master Directions for AIFIs 2025 | 28 Nov 2025 | Family `AIFI` stub | G | SEC |

## G.3 RBI — ARCs, AIF investments, payments, credit information companies

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-RBI-151 | ARC NOF ≥ ₹300 crore (existing ARCs by 31 Mar 2026, else no new business); NOF ≥ ₹1,000 crore to act as IBC resolution applicant | ARC Directions 2025, DoR.FIN.REC.No.293/26.03.001/2025-26, paras 14–18 | 28 Nov 2025 (upd. 10 Mar 2026) | NOF band classifier | L | SEC [VERIFY paras] |
| LR-RBI-152 | ARC CRAR ≥ 15% | ARC para 93 | as above | Ratio threshold | L | SEC [VERIFY] |
| LR-RBI-153 | ARC: deposits prohibited; surplus funds ≤ 10% of NOF in short-term instruments; own-use property ≤ 10% of owned funds; acquired property sold within 5 years | ARC paras 21–23 | as above | Monitors | L | SEC [VERIFY] |
| LR-RBI-154 | ARC acquisition: Board policy within 90 days of CoR; DD ≥ 2 weeks; auction-only where seller is sponsor/its lenders/group | ARC paras 24, 27, 34 | as above | Policy and process obligations | L | SEC [VERIFY] |
| LR-RBI-155 | ARC trusts: one trust per scheme, ARC as trustee; SR issue only to QBs; self-investment ≥ max(15% of transferors' SRs, 2.5% of total SRs) | ARC paras 76, 79, 81; SARFAESI s.7 | as above | Per-scheme checks | L | SEC [VERIFY] |
| LR-RBI-156 | ARC clocks: planning ≤ 6 months; realisation 5 years extendable by Board to 8; rating within 6 months; NAV as on 30 Jun and 31 Dec | ARC paras 12, 35–36, 82–84, 90 | as above | Scheme clocks (P15 FR-P15-39) | L | SEC [VERIFY] |
| LR-RBI-157 | ARC settlement: Board policy; > ₹1 crore or any fraud/wilful-default case → IAC review then Board (≥ 2 IDs) or committee | ARC paras 60–67 | as above | IAC committee seed; routing obligation | L | SEC [VERIFY] |
| LR-RBI-158 | ARC management fees on NAV at lower end of range, capped at acquisition value; unrealised fees reversed 180 days after planning period | ARC paras 142–144 | as above | Accounting checklist | L | SEC [VERIFY] |
| LR-RBI-159 | NBFCs may invest in SRs as QBs (all RBI-regulated NBFCs and HFCs) | SARFAESI s.2(1)(u); MoF gazette notification 28 Feb 2025 | 28 Feb 2025 | QB basis attribute | L | SEC |
| LR-RBI-160 | Only an ARC registered under s.3 may form trusts, issue SRs, take s.9 measures | SARFAESI ss.3, 7, 9 | in force | Guard-rail obligation for NBFCs | L | SEC |
| LR-RBI-161 | RE investment in AIF: individual ≤ 10% of scheme corpus; all REs ≤ 20%; > 5% with downstream non-equity in debtor → 100% provision on look-through capped at direct exposure; subordinated units deducted from capital | RBI (Investment in AIF) Directions 2025, RBI/DOR/2025-26/138, para 6 | 1 Jan 2026 (or earlier by policy) | AIF monitors | L | SEC [VERIFY consolidated paras] |
| LR-RBI-162 | Commitments existing on 29 Jul 2025 or made before effective date follow old or new regime in full; regime tag irrevocable | AIF Directions paras 2, 8 | as above | Regime tag | L | SEC |
| LR-RBI-163 | Payment aggregators — authorisation and governance under PA Directions 2025 | RBI Regulation of Payment Aggregators Directions 2025 | 15 Sep 2025 | Family `PAY` stub; Razorpay is the PA for LDC billing | L | VERIFY |
| LR-RBI-164 | Credit Information Companies (Amendment) Directions 2025: CICs report CIs missing timelines on DAKSH half-yearly | RBI/DOR/2025-26/119 | 1 Jul 2026 | Content for `CIC_INFO`; motivation for CIC calendar | L | SEC |
| LR-RBI-165 | E-mandate Directions 2026 (cards, PPIs, UPI) — no charge to customer | RBI/DPSS/2026-27/396 | 21 Apr 2026 | Billing (P20) awareness for recurring card/UPI mandates | L | SEC |

## G.4 RBI — Customer protection and grievance

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-RBI-201 | Customer must complain to the RE first; RE reply period 30 days; Ombudsman complaint within 90 days thereafter; RE reply to Ombudsman within 15 days; 2021 Scheme for earlier complaints | Reserve Bank – Integrated Ombudsman Scheme 2026, cl.10(1)(f)–(g), 14(2), 20 | 1 Jul 2026 | Grievance clocks and signposting (P14) | L | SEC [VERIFY clause numbers] |
| LR-RBI-202 | Credit co-operative societies are outside RB-IOS 2026; RBI Ombudsman never shown to their members | Integration Spec §6.24; RB-IOS scope | 1 Jul 2026 | Signposting rule (P16) | L | SEC |
| LR-RBI-203 | GRO/nodal officer details and grievance mechanism displayed; escalation matrix | RBC Directions 2025 (grievance paras) | 28 Nov 2025 | Website grievance link (P14/P18) | L | V-OFF |

---

## G.5 SEBI

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-SEBI-001 | Listed entity board: at least half independent where chair is executive/promoter-related, one-third where chair is non-executive and unrelated; at least one woman ID for top 1,000 | LODR 2015 Reg 17(1) | in force | Composition check (P06) | L | SEC [VERIFY current text] |
| LR-SEBI-002 | Board meets at least four times a year, gap ≤ 120 days | LODR Reg 17(2) | in force | Meeting-gap clock | L | SEC |
| LR-SEBI-003 | Audit Committee: ≥ 3 members, two-thirds independent, chair independent; ≥ 4 meetings a year, gap ≤ 120 days | LODR Reg 18 | in force | Committee rules | L | SEC |
| LR-SEBI-004 | NRC (Reg 19) and Stakeholders Relationship Committee (Reg 20) composition and meetings | LODR Regs 19, 20 | in force | Committee rules | L | SEC |
| LR-SEBI-005 | Risk Management Committee for top 1,000 listed entities by market capitalisation and HVDLEs; meets at least twice a year | LODR Reg 21 | in force | Committee rules; rank attribute | L | SEC [VERIFY gap rule] |
| LR-SEBI-006 | Material RPTs need prior shareholder approval; materiality thresholds as amended by the 2025 Fifth Amendment (scale-based) | LODR Reg 23; LODR (Fifth Amendment) 2025 | 18 Nov 2025 | RPT approval workflow (P06) | L | SEC [VERIFY thresholds] |
| LR-SEBI-007 | Annual secretarial compliance report (Reg 24A) signed only by the secretarial auditor or a qualifying peer-reviewed CS | LODR Reg 24A as amended | 1 Apr 2025 | Calendar; signatory check | L | SEC |
| LR-SEBI-008 | Independent directors meet at least once a year without non-IDs | LODR Reg 25(3) | in force | Meeting obligation | L | SEC |
| LR-SEBI-009 | Disclosure of material events: board-meeting outcomes within 30 minutes of conclusion; events emanating within the entity within 12 hours; others within 24 hours | LODR Reg 30 and Schedule III | in force (2023 amendment) | Listed event register clocks | L | SEC [VERIFY] |
| LR-SEBI-010 | Shareholding pattern within 21 days of quarter end | LODR Reg 31 | in force | Calendar | L | SEC |
| LR-SEBI-011 | Quarterly results within 45 days of quarter end; annual within 60 days of FY end | LODR Reg 33 | in force | Calendar | L | SEC |
| LR-SEBI-012 | Corporate governance report within 21 days of quarter end; investor grievance statement within 21 days | LODR Regs 27(2), 13(3) | in force | Calendar | L | SEC |
| LR-SEBI-013 | BRSR for top 1,000 listed entities; BRSR Core assurance per SEBI glide path | LODR Reg 34(2)(f); SEBI BRSR circulars | in force | ESG overlay obligations | L | SEC [VERIFY glide] |
| LR-SEBI-014 | HVDLE threshold raised to listed NCDs outstanding ≥ ₹5,000 crore; exit after three consecutive FYs below, with relief for entities falling out only because of the higher threshold | LODR Reg 15(1A) as amended by LODR (Amendment) Regulations 2026, SEBI/NRO-GN/2026/295 | 20 Jan 2026 | HVDLE classifier | L | SEC |
| LR-SEBI-015 | Continuation of a director beyond 75 years requires shareholder approval (2026 amendment, extended to HVDLE context) | LODR as amended 2026 | 20 Jan 2026 | Director age check | L | SEC [VERIFY scope] |
| LR-SEBI-016 | Investor services in demat only (transfer, transmission, transposition); credit within 30 days for sub-division/consolidation/duplicate requests | LODR as amended 2026 | 20 Jan 2026 | Investor-services obligations | L | SEC |
| LR-SEBI-017 | PIT: structured digital database of UPSI sharing; code of conduct; trading window closure from end of quarter till 48 hours after results; pre-clearance above threshold | PIT 2015 Reg 3(5), Reg 9, Schedule B | in force (amend. 9 Jun 2025) | PIT module obligations; SDD log (P06) | L | SEC |
| LR-SEBI-018 | Continual disclosure by promoters/designated persons where trades exceed ₹10 lakh in a calendar quarter, within 2 trading days; company informs exchange within 2 trading days | PIT Reg 7(2) | in force | Disclosure clock | L | SEC |
| LR-SEBI-019 | SAST: acquisition reaching 5% and every 2% change thereafter disclosed within 2 working days | SAST 2011 Reg 29 | in force | Event register | L | SEC |
| LR-SEBI-020 | SAST encumbrance disclosure by promoters | SAST Reg 31 | in force | Event register | L | SEC [VERIFY 2022 changes] |
| LR-SEBI-021 | ICDR: monitoring agency for issue proceeds; lock-in tracker; SME IPO conditions (4 Mar 2025 amendment) | ICDR 2018 Regs 41, 16–17, 262 [VERIFY] | in force | Post-issue obligations | L | VERIFY |
| LR-SEBI-022 | SEBI (Mutual Funds) Regulations 2026 replace the 1996 Regulations; MF Lite and SIF frameworks consolidated; control at 10% voting rights; sponsor eligibility routes | SEBI (MF) Regulations 2026 | notified 14 Jan 2026; in force 1 Apr 2026 | MF pack instrument and family; legacy 1996 instrument `SUPERSEDED` | L | SEC [VERIFY regulation numbers] |
| LR-SEBI-023 | MF scheme categorisation and rationalisation (market-cap ranks via AMFI half-yearly list) | SEBI circular HO/24/13/15(2)2026-IMD-RAC4/I/5764/2026 | 26 Feb 2026 | MF investment-limit monitors | L | SEC |
| LR-SEBI-024 | REITs treated as equity-related instruments for MF investment from 1 Jan 2026 (grandfathering of holdings at 31 Dec 2025) | SEBI circular Nov 2025 | 1 Jan 2026 | MF/REIT pack content | L | SEC |
| LR-SEBI-025 | InvIT borrowing matrix: ≤ 25% of assets no conditions; 25–49% rating + 50% unitholder approval; 49–70% AAA rating, six-distribution record, 75% approval, use restricted | InvIT Regulations 2014 Reg 20(3) | in force | REIT_INVIT pack monitor | L | SEC |
| LR-SEBI-026 | AIF Regulations 2012: PPM, investment conditions by category, Category III leverage limits, annual audit of PPM compliance, investments held in demat from 1 Jul 2025 | AIF Regulations 2012 and Master Circular | in force | AIF pack | L | SEC [VERIFY current circulars] |
| LR-SEBI-027 | Cybersecurity and Cyber Resilience Framework for SEBI REs (categories MII, Qualified, Mid-size, Small-size, Self-certification) with later clarifications | SEBI CSCRF circular, 20 Aug 2024, and clarifications | in force (phased) | CYBER overlay applicability; CSCRF category attribute | L | SEC [VERIFY] |
| LR-SEBI-028 | Investor grievances via SCORES 2.0 with resolution timelines; SEBI ODR platform for disputes with market participants | SEBI SCORES circulars; ODR Master Circular | in force | P14 signposting for SEBI REs | L | SEC [VERIFY timelines] |
| LR-SEBI-029 | Portfolio Managers Regulations 2020; Investment Advisers Regulations 2013; Research Analysts Regulations 2014 | SEBI regulations | in force | SEBI_INT packs | L | SEC |
| LR-SEBI-030 | Stock brokers: client funds and securities segregation, Qualified Stock Broker obligations | SEBI Stock Brokers Regulations 1992/2026 [VERIFY]; QSB circulars | in force | SEBI_INT pack | L | VERIFY |

## G.6 IFSCA

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-IFSCA-001 | No entity may carry on business as FC/FU in the IFSC without a Certificate of Registration for the permissible activities; fresh registration for additional activities unless already authorised under another IFSCA framework | IFSCA (Finance Company) Regulations 2021, Reg 3(1) and Explanation (consolidated 2026) | in force (amend. 5 May 2026) | FCFU pack; seeds owner's sample sheet | L | SEC (owner's sheet) |
| LR-IFSCA-002 | FC/FU books and reporting in USD | IFSCA FC Regs reg 9 | in force | Base currency USD | L | SEC |
| LR-IFSCA-003 | IFSCA (Fund Management) Regulations 2025 replaced the 2022 Regulations | IFSCA FM Regulations 2025 (gazetted 19 Feb 2025; as amended to 10 Sep 2026) | in force | FME pack | L | SEC |
| LR-IFSCA-004 | IFSC Insurance Office: Board appoints an Appointed Actuary meeting eligibility; intimation to IFSCA within 7 days; AA authorised to report non-compliance directly | IFSCA (Appointed Actuary) Regulations 2022, Reg 4(1)–(5) | in force | INSURER-IFSC obligations | L | SEC (owner's sheet) |
| LR-IFSCA-005 | AML/CFT/KYC Guidelines 2022 (master guidelines as on 3 Aug 2026) apply across IFSCA REs, with FIU-IND reporting | IFSCA AML/CFT/KYC Guidelines 2022 and circulars | in force | `OV_AML` for IFSC | L | SEC |
| LR-IFSCA-006 | Liquidity risk management guidelines for FC/FU | IFSCA Guidelines on Liquidity Risk Management for FC/FU, 24 Jun 2021 | in force | Risk pack | L | SEC (owner's sheet) |
| LR-IFSCA-007 | IFSCA entity taxonomy (33 types in 13 sectors) per owner's IFSCA compliance knowledgebase | Owner's IFSCA format (Rough sheet) | — | `IFSC` family dropdowns | G | V-OFF (owner) |
| LR-IFSCA-008 | IFSCA TechFin and Ancillary Services Regulations 2025 (amended 12 May 2026); BATF Regulations 2024 (amended 8 Jan 2026) | IFSCA regulations | in force | IFSC pack | L | SEC |

## G.7 IRDAI

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-IRDAI-001 | Insurer governance: board and committee structure, KMP definitions, fit-and-proper, under the 2024 regulations and Master Circular | IRDAI (Corporate Governance for Insurers) Regulations 2024; Master Circular on Corporate Governance for Insurers 2024 | 2024 | INSURER committees/KMP seeds | L | SEC [VERIFY lists] |
| LR-IRDAI-002 | Protection of policyholders' interests (grievance timelines, claim settlement) | IRDAI (Protection of Policyholders' Interests and Allied Matters of Insurers) Regulations 2024 and Master Circular | 2024 | P14 timelines for insurers | L | VERIFY |
| LR-IRDAI-003 | Actuarial, finance and investment functions of insurers | IRDAI (Actuarial, Finance and Investment Functions of Insurers) Regulations 2024 | 2024 | INSURER pack | L | VERIFY |
| LR-IRDAI-004 | Registration, capital structure, transfer of shares and amalgamation of insurers | IRDAI Regulations 2024 | 2024 | Event obligations | L | VERIFY |
| LR-IRDAI-005 | Insurance intermediaries (brokers, corporate agents, IMFs, web aggregators) with 2026 amendment; corporate agents may tie up with up to 9 insurers per line | IRDAI (Insurance Intermediaries) Regulations 2024 [VERIFY year]; (Amendment) Regulations 2026, F. No. IRDAI/Reg/8/222/2026 | 30 Jul 2026 | INS_INT pack; tie-up count attribute | L | SEC |
| LR-IRDAI-006 | Information and cyber security guidelines for insurers and intermediaries; incident reporting to CERT-In within 6 hours | IRDAI IS&CS Guidelines 2023 | 2023 | CYBER overlay | L | VERIFY |
| LR-IRDAI-007 | Bima Bharosa grievance system; Insurance Ombudsman Rules 2017 (as amended) | IRDAI; Insurance Ombudsman Rules | in force | P14 signposting | L | SEC |
| LR-IRDAI-008 | Insurance Act 1938 key sections (s.2CB, s.40 commission restrictions, s.42 agents, s.42D) | Insurance Act 1938 as amended | in force | Content references | L | VERIFY |

## G.8 MCA — Companies Act 2013, LLP Act 2008

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-MCA-001 | Small company: paid-up capital ≤ ₹10 crore and turnover ≤ ₹100 crore (excluding public, holding/subsidiary, s.8, special-Act companies) | Companies Act s.2(85); Companies (Specification of Definitions Details) Amendment Rules (Dec 2025) | Dec 2025 | Small-company classifier | L | SEC [VERIFY G.S.R.] |
| LR-MCA-002 | Minimum directors: public 3, private 2, OPC 1; maximum 15 (more by special resolution); resident director ≥ 182 days in FY | s.149(1), (3) | in force | Board composition check | L | SEC |
| LR-MCA-003 | Woman director: every listed company and every public company with paid-up ≥ ₹100 crore or turnover ≥ ₹300 crore | s.149(1) proviso; Appointment and Qualification of Directors Rules 2014 r.3 | in force | Composition check | L | SEC |
| LR-MCA-004 | Independent directors: listed — one-third; public companies with paid-up ≥ ₹10 crore, or turnover ≥ ₹100 crore, or aggregate loans/debentures/deposits > ₹50 crore — at least two | s.149(4); r.4 | in force | Composition check | L | SEC |
| LR-MCA-005 | Audit Committee and NRC for listed companies and public companies meeting Rule 6 thresholds (paid-up ≥ ₹10 cr; turnover ≥ ₹100 cr; loans/borrowings/debentures/deposits > ₹50 cr) | ss.177, 178; Meetings of Board Rules r.6 | in force | Committee seed | L | SEC |
| LR-MCA-006 | Stakeholders Relationship Committee where > 1,000 shareholders/debenture/deposit/security holders | s.178(5) | in force | Committee seed | L | SEC |
| LR-MCA-007 | Board meetings: first within 30 days of incorporation; at least four a year with gap ≤ 120 days; OPC, small, dormant and s.8 companies at least one per half-year with gap ≥ 90 days | s.173(1), (5) | in force | Meeting clocks | L | SEC |
| LR-MCA-008 | Board meeting notice at least 7 days | s.173(3) | in force | Notice clock | L | SEC |
| LR-MCA-009 | Minutes prepared within 30 days of the meeting; SS-1/SS-2 compliance mandatory | s.118(1), (10) | in force | Minutes clock (P06) | L | SEC |
| LR-MCA-010 | AGM within 6 months of FY end and not later than 15 months from previous AGM; first AGM within 9 months of first FY end | s.96(1) | in force | AGM clock | L | SEC |
| LR-MCA-011 | AGM notice at least 21 clear days (shorter with consent of 95% members) | s.101(1) | in force | Notice clock | L | SEC |
| LR-MCA-012 | Financial statements filed in AOC-4 within 30 days of AGM; annual return MGT-7/7A within 60 days of AGM | ss.137, 92 | in force | Filing calendar (P11) | L | SEC |
| LR-MCA-013 | Auditor appointed for 5 years at AGM; ADT-1 within 15 days; rotation for listed and specified classes (individual 5 years, firm 10 years) | ss.139(1), (2) | in force | Auditor workflow | L | SEC |
| LR-MCA-014 | KMP: listed and public companies with paid-up ≥ ₹10 crore — MD/CEO/manager or WTD, CS, CFO; other companies with paid-up ≥ ₹10 crore — whole-time CS | s.203; Managerial Personnel Rules r.8, 8A | in force | KMP seed | L | SEC |
| LR-MCA-015 | Internal auditor: listed; unlisted public with paid-up ≥ ₹50 cr, or turnover ≥ ₹200 cr, or loans/borrowings ≥ ₹100 cr, or deposits ≥ ₹25 cr; private with turnover ≥ ₹200 cr or loans/borrowings ≥ ₹100 cr | s.138; Accounts Rules r.13 | in force | IA applicability (P10) | L | SEC |
| LR-MCA-016 | Secretarial audit: listed; public with paid-up ≥ ₹50 cr or turnover ≥ ₹250 cr; companies with loans/borrowings ≥ ₹100 cr | s.204; Managerial Personnel Rules r.9 | in force | Secretarial audit applicability | L | SEC [VERIFY 2025 amendment for listed under LODR Reg 24A tenure] |
| LR-MCA-017 | CSR: net worth ≥ ₹500 cr or turnover ≥ ₹1,000 cr or net profit ≥ ₹5 cr in preceding FY → spend 2% of average net profit of 3 FYs; CSR Committee not required where obligation ≤ ₹50 lakh; unspent amount for ongoing projects to Unspent CSR Account within 30 days of FY end; other unspent to Schedule VII fund within 6 months | s.135(1), (5), (6), (9); CSR Rules 2014 | in force | CSR detector; clocks | L | SEC |
| LR-MCA-018 | Books of account with audit trail (edit log) that cannot be disabled; daily backup on servers physically in India | Accounts Rules r.3(1), r.3(5) | 1 Apr 2023 | Platform's own design (D-02) and client checklist | L | SEC |
| LR-MCA-019 | Board's report to include POSH and maternity-benefit statements (Accounts Second Amendment Rules 2025) | Accounts Rules r.8 as amended 30 May 2025 | FY 2025-26 onwards | Board report checklist | L | SEC |
| LR-MCA-020 | Director disclosure of interest (MBP-1) at first board meeting of every FY and on change | s.184; MBP-1 | in force | Annual task | L | SEC |
| LR-MCA-021 | Related-party transactions — board/shareholder approval thresholds; register MBP-4 | s.188; Meetings of Board Rules r.15 | in force | RPT workflow | L | SEC |
| LR-MCA-022 | Loans, guarantees and investments limits (exemption for NBFCs in ordinary course of lending business, s.186(11)) | s.186 | in force | Applicability nuance for NBFCs | L | SEC |
| LR-MCA-023 | Director disqualification for non-filing of financial statements or annual returns for 3 consecutive FYs | s.164(2) | in force | Disqualification watch (P06) | L | SEC |
| LR-MCA-024 | DIR-3 KYC of directors by 30 September each year [VERIFY any 2025–26 change in frequency] | Appointment and Qualification of Directors Rules r.12A | in force | Calendar | L | VERIFY |
| LR-MCA-025 | Return of deposits/outstanding loans DPT-3 by 30 June | Acceptance of Deposits Rules r.16A | in force | Calendar | L | SEC |
| LR-MCA-026 | MSME-1 half-yearly return of dues to micro/small enterprises outstanding > 45 days | Specified Companies (Furnishing of Information about Payment to MSE Suppliers) Order | in force | Calendar | L | SEC |
| LR-MCA-027 | Significant beneficial owner declarations (BEN-1/BEN-2) and register BEN-3 | s.90; SBO Rules 2018 | in force | Register | L | SEC |
| LR-MCA-028 | Statutory registers maintained at registered office (members MGT-1, directors and KMP, charges CHG-7, MBP-2, MBP-4) | ss.85, 88, 170, 186(9), 189 | in force | Register engine (P06) | L | SEC |
| LR-MCA-029 | Charges registered within 30 days (extendable) — CHG-1 | s.77 | in force | Event clock | L | SEC |
| LR-MCA-030 | LLP annual return Form 11 within 60 days of FY end (30 May); statement of account and solvency Form 8 by 30 October | LLP Act 2008 ss.34–35; LLP Rules 2009 r.24–25 | in force | LLP calendar | L | SEC |
| LR-MCA-031 | LLP: at least two designated partners, one resident in India | LLP Act s.7 | in force | Composition check | L | SEC |
| LR-MCA-032 | Section 8 companies, Nidhi companies and producer companies have special compliance (Nidhi Rules 2014 NDH forms; producer company Part XXIA of the 1956 Act as saved) | Companies Act ss.8, 406, 465(1) proviso; Nidhi Rules | in force | Type-specific packs | L | VERIFY |
| LR-MCA-033 | One Person Company: board meeting requirement relaxed (s.173(5)); conversion rules | s.2(62), s.173(5), Incorporation Rules | in force | OPC pack | L | SEC |

## G.9 ICSI and ICAI standards

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-ICSI-001 | Secretarial Standard on Board Meetings (SS-1) mandatory — notice, agenda, quorum, minutes, preservation | ICSI SS-1 (revised); Companies Act s.118(10) | revised SS effective 1 Apr 2024 | Meeting and minutes engine (P06) | L | SEC |
| LR-ICSI-002 | Secretarial Standard on General Meetings (SS-2) mandatory | ICSI SS-2 (revised); s.118(10) | 1 Apr 2024 | General meeting engine | L | SEC |
| LR-ICSI-003 | CS Auditing Standards CSAS-1 to CSAS-4 for secretarial audit; CSAS Revised Edition 2026 approved 28 Aug 2026 (effective date not stated) | ICSI | [VERIFY] | P10 secretarial audit | G | SEC |
| LR-ICAI-001 | Standards on Auditing bind auditors; Guidance Notes and Technical Guides are recommendatory (strength flag "professional") | ICAI | in force | Strength flag; P10 | G | SEC |
| LR-ICAI-002 | Technical Guide on Risk-Based Internal Audit of NBFCs (2024); Technical Guide on Audit of NBFCs (rev. Sep 2023); Guidance Note on Audit of Banks (2026 Edition); Implementation Guide on Reporting on Audit Trail (rev. 2024) | ICAI publications | [VERIFY editions] | P10/P11 references (App. J) | G | SEC |
| LR-ICAI-003 | Ind AS applicability to NBFCs by net worth phases (Companies (Ind AS) Rules 2015 Rule 4); ARCs not in the Rule 2(g) NBFC list | Ind AS Rules as amended 2026 | in force | Accounting framework attribute (App. J) | L | SEC |

## G.10 Data protection, IT and cyber security (MeitY, CERT-In, EU, US)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-MEITY-001 | DPDP Rules notified; phased commencement — Consent Manager provisions 13 Nov 2026; substantive Data Fiduciary duties 13 May 2027 | DPDP Act 2023; DPDP Rules 2025, G.S.R. 846(E), 13 Nov 2025 | phased | Effective-dated obligations (`OV_DATA`); build compliant now | L | SEC [VERIFY any acceleration] |
| LR-MEITY-002 | Notice must be itemised, in clear language, with withdrawal and grievance routes; consent free, specific, informed, unambiguous; withdrawal as easy as giving | DPDP Act ss.5–6; Rule 3 | 13 May 2027 | Consent/notice obligations; platform's own notices | L | SEC |
| LR-MEITY-003 | Personal data breach intimation to the Board and affected principals; detailed report within 72 hours | DPDP Rule 7 | 13 May 2027 | Breach clocks (P12) | L | SEC |
| LR-MEITY-004 | Significant Data Fiduciary: DPO in India, independent data auditor, annual DPIA and audit | DPDP Act s.10; Rule 13 | 13 May 2027 (on notification as SDF) | SDF attribute; obligations | L | SEC |
| LR-MEITY-005 | Children's data: verifiable parental consent; no tracking/behavioural monitoring/targeted ads | DPDP Act s.9; Rule 10 | 13 May 2027 | Obligations; platform rejects minor accounts for B2B users | L | SEC |
| LR-MEITY-006 | Penalties up to ₹250 crore per instance (Schedule) | DPDP Act s.33, Schedule | 13 May 2027 | Consequence text in sheets; savings model (P20) | L | SEC |
| LR-MEITY-007 | Reasonable security practices for sensitive personal data (until DPDP s.44 repeal of s.43A takes effect) | IT Act 2000 s.43A; SPDI Rules 2011 | in force (transition) | `OV_DATA` legacy obligations, auto-sunset on DPDP commencement | L | SEC |
| LR-CERTIN-001 | Report specified cyber incidents to CERT-In within 6 hours of noticing; maintain ICT logs for 180 days within India; synchronise clocks to NTP (NIC/NPL); designate a point of contact | CERT-In Directions under IT Act s.70B(6), 28 Apr 2022 | in force | Incident clock (P12); platform's own logging (P24) | L | SEC |
| LR-EU-001 | GDPR applies to processing by non-EU controllers offering goods/services to, or monitoring, EU data subjects | GDPR Art. 3(2) | 25 May 2018 | EU overlay applicability attribute | L | SEC |
| LR-EU-002 | Personal data breach notified to the supervisory authority within 72 hours where feasible; ROPA (Art. 30); DPIA (Art. 35); DPO where required (Art. 37); EU representative (Art. 27) | GDPR Arts. 27, 30, 33, 35, 37 | in force | EU overlay obligations (jurisdiction pack gate D-19) | L | SEC |
| LR-US-001 | California CCPA/CPRA: notice at collection, rights to know/delete/correct/opt out of sale or sharing; response within 45 days; CPPA regulations on risk assessments, cybersecurity audits and ADMT (phased from 2026) | Cal. Civ. Code §1798.100 et seq.; CPPA regulations | in force (phased) | US overlay obligations (gate D-19) | L | SEC [VERIFY phase dates] |

## G.11 Labour and workplace (Ministry of Labour and Employment; POSH)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-MOLE-001 | Four Labour Codes in force; Central Rules notified; most State rules pending — obligations effective-dated per State | Code on Wages 2019; IR Code 2020; Code on Social Security 2020; OSHWC Code 2020 — S.O. 5319(E)–5322(E); Central Rules G.S.R. 342(E)–345(E), 8 May 2026 | 21 Nov 2025 | `OV_LABOUR` State-aware rule packs (P13); shared `infrabyx-labour-rulepack` | L | SEC |
| LR-MOLE-002 | "Wages" definition with 50% cap on excluded components | Code on Wages s.2(y) | 21 Nov 2025 | Payroll rule (P13) | L | SEC |
| LR-MOLE-003 | Wage payment timelines (monthly wage period: by 7th of following month); full and final settlement within 2 working days of removal, dismissal, retrenchment or resignation | Code on Wages s.17 | 21 Nov 2025 | Payroll clocks | L | SEC [VERIFY] |
| LR-MOLE-004 | Appointment letter to every employee | OSHWC Code s.6(1)(f) | 21 Nov 2025 | HR onboarding obligation; employment agreement eSign (P13) | L | SEC |
| LR-MOLE-005 | Grievance Redressal Committee in establishments with ≥ 20 workers | IR Code s.4 | 21 Nov 2025 | Committee seed | L | SEC |
| LR-MOLE-006 | Works Committee may be required in establishments with ≥ 100 workers | IR Code s.3 | 21 Nov 2025 | Committee seed (conditional) | L | SEC |
| LR-MOLE-007 | Standing orders for establishments with ≥ 300 workers; prior permission for lay-off/retrenchment/closure at ≥ 300 | IR Code ss.28, 77 | 21 Nov 2025 | Obligations by headcount | L | SEC |
| LR-MOLE-008 | Gratuity payable after 5 years (1 year for fixed-term employees) | SS Code s.53 | 21 Nov 2025 | Payroll provision | L | SEC |
| LR-MOLE-009 | EPF applicability (≥ 20 employees) and ESI (≥ 10 employees); EPF wage ceiling ₹15,000 re-notified 29 May 2026 | SS Code Schedules; notification 29 May 2026 | 21 Nov 2025 | Payroll parameters (signed rule pack, NN-26) | L | SEC |
| LR-MOLE-010 | Maternity benefit 26 weeks; crèche facility for establishments with ≥ 50 employees | SS Code Ch VI | 21 Nov 2025 | HR obligations | L | SEC |
| LR-MOLE-011 | Working hours 8 per day / 48 per week (as notified); overtime at twice the ordinary rate; women's consent for night work | OSHWC Code ss.25–27, 43 | 21 Nov 2025 | Attendance rules | L | SEC [VERIFY rules] |
| LR-MOLE-012 | Internal Committee at every office/branch with ≥ 10 employees: presiding officer a senior woman, at least half women, one external member; inquiry within 90 days; report within 10 days; annual report to District Officer | POSH Act 2013 ss.4, 11(4), 13, 21 | in force | IC committee seed; sealed case data (NN-13) | L | SEC |

## G.12 Co-operatives (MSCS Act, CRCS, State Acts)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-COOP-001 | Non-bank co-operative societies may not use "bank", "banker" or "banking" in their names | BR Act s.7 read with s.56 (as amended 2020) | 29 Sep 2020 [VERIFY] | GR-COOP-01 activation block | L | SEC |
| LR-COOP-002 | Deposits only from active voting members; deposits from nominal/associate members or non-members are unlicensed banking without DICGC cover | MSCS Act s.67 Explanation; MCS Act (MH) s.144-5A; BUDS Act First Schedule; RBI press release 22 Nov 2021 | in force | GR-COOP-02; exception register (P16) | L | SEC |
| LR-COOP-003 | No loans on the security of the society's own shares; no non-member security | MSCS s.66(1) | in force | GR-COOP-04 | L | SEC |
| LR-COOP-004 | Membership decision within 4 months and communication within 15 days, else deemed refused | MSCS s.25(4) as amended 2023 | Aug 2023 | Admission clock | L | SEC [VERIFY] |
| LR-COOP-005 | AGM within 6 months of close of financial year | MSCS s.39 | in force | AGM clock | L | SEC |
| LR-COOP-006 | Board term 5 years; inform the Co-operative Election Authority at least 6 months before term expiry | MSCS s.45; s.45J(8) as inserted 2023; Constitution Art. 243ZJ (for MSCS) | Aug 2023 | Election clocks | L | SEC [VERIFY] |
| LR-COOP-007 | Board size ≤ 21; reservation of one seat for SC/ST and two for women; co-opted experts | MSCS s.41 as amended 2023 | Aug 2023 | Composition check | L | VERIFY |
| LR-COOP-008 | Director disqualification grounds incl. board's failure to hold AGM, file returns or conduct elections (5 years) | MSCS s.43 | in force | Disqualification watch | L | SEC [VERIFY sub-clauses] |
| LR-COOP-009 | Appropriation: ≥ 25% of net profit to reserve fund; 1% to Co-operative Education Fund; ≥ 10% reserve for unforeseen losses; CRRD Fund lesser of ₹1 crore and 1% of net profit if profitable in each of preceding 3 years | MSCS ss.63, 63A | Aug 2023 | Appropriation validation (P16) | L | SEC |
| LR-COOP-010 | Audit by auditor from Central Registrar's panel; special panel where turnover/deposits > ₹500 crore; concurrent audit above ₹500 crore | MSCS ss.70, 70A | Aug 2023 | Audit workflow | L | SEC [VERIFY] |
| LR-COOP-011 | Disputes touching constitution/management/business referred to arbitration (arbitrator appointed by Central Registrar) | MSCS s.84 | in force | Signposting; block private arbitration (GR-COOP-05) | L | SEC [VERIFY] |
| LR-COOP-012 | Co-operative Ombudsman for member complaints (deposits, equitable benefits, individual rights) | MSCS s.85A; notification 5 Mar 2024 | 5 Mar 2024 | P14/P16 escalation | L | SEC |
| LR-COOP-013 | Annual return to Central Registrar within 6 months of FY close (online CRCS portal) | MSCS s.120 as amended 2023 | Aug 2023 | Return clock | L | SEC |
| LR-COOP-014 | Credit MSCS prudential norms by size class (Micro ≤ ₹10 cr; Small ≤ ₹100 cr; Medium ≤ ₹500 cr; Large > ₹500 cr deposits): CRAR 9%/9%/12%/12% (glide to 2028-29); cash ≥ 2%; liquid investments to 18%; leverage ≤ 10×; single 15%/group 25%; unsecured ≤ 15%; housing caps; quarterly return | CRCS order L-11012/01/2023-Reg, 22 Jan 2024 | 22 Jan 2024 | Prudential monitors (P16 FR-P16-38) | G | SEC [VERIFY order text] |
| LR-COOP-015 | MSCS branch expansion: prior approval; ≤ 10% of branches a year (max 10); GNPA < 7%, NNPA < 3%; profit 3 years; State Registrar certificate on no non-voting-member deposits | CRCS order, July 2025 | Jul 2025 | Branch eligibility checklist | G | VERIFY |
| LR-COOP-016 | Part IXB of the Constitution operative only for multi-State societies and UT societies | *Union of India v. Rajendra N. Shah* (SC, 20 Jul 2021) | 20 Jul 2021 | Rule attachment scope (P16 FR-P16-02) | L | SEC [VERIFY cite] |
| LR-COOP-017 | Maharashtra: AGM on or before 30 September; audit within 4 months; rectification report (Form O) within 3 months of audit report; audit class A–D (Rule 69, Form N-2) | MCS Act 1960 ss.75, 81, 82; MCS Rules 1961 r.69 | in force | MH pack clocks | L | SEC [VERIFY] |
| LR-COOP-018 | Maharashtra: reserve fund ≥ 25% of net profit (Registrar may permit ≥ 10%); dividend ≤ 15% without Registrar sanction; education fund to federation | MCS Act ss.66–68; Rule 52 | in force | MH appropriation validation | L | SEC [VERIFY rates] |
| LR-COOP-019 | Maharashtra: disputes to Co-operative Court (s.91), limitation (s.92), appeal (s.96), execution (s.98); recovery certificate (s.101) for notified classes | MCS Act ss.91–101 | in force | Signposting; matter tracking | L | SEC |
| LR-COOP-020 | Maharashtra credit societies (Chapter XI-1A): no non-member deposits; SLR ≥ 25% of deposits; administrative-expense cap; Regulatory Board; Stabilisation and Liquidity Support Fund | MCS Act ss.144-5A to 144-30A | in force | MH credit-society monitors | L | SEC [VERIFY %] |
| LR-COOP-021 | Maharashtra State Co-operative Election Authority conducts committee elections under the 2014 Election Rules | MCS Act s.73CB; MCS (Election to Committee) Rules 2014 | in force | Election support (P16) | L | VERIFY |
| LR-COOP-022 | Co-operatives are not RBI REs; RBI Directions (digital lending, co-lending, IRACP, capital, returns) do not bind credit societies | TDCR para 97; RBI press release 22 Nov 2021 | in force | Applicability (P15) | L | SEC |
| LR-COOP-023 | Credit societies cannot be co-lending partners, loan transferees/transferors, or DLG providers to NBFCs | TDCR paras 7, 12(4), 97; CF para 19 | 28 Nov 2025 | GR-COOP-03 | L | V-OFF |
| LR-COOP-024 | Deposits with credit co-operative societies are not insured by DICGC | DICGC Act 1961 | in force | Disclosure on member documents | L | SEC |

## G.13 Taxation

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-GST-001 | GSTR-1 monthly by the 11th (quarterly under QRMP by the 13th); GSTR-3B by the 20th (staggered 22nd/24th for QRMP) | CGST Act s.37, s.39; CGST Rules r.59, r.61 | in force | Tax calendar (`OV_TAX`) | L | SEC |
| LR-GST-002 | Annual return GSTR-9 by 31 December; reconciliation statement GSTR-9C where aggregate turnover > ₹5 crore | CGST Act s.44; r.80 | in force | Calendar | L | SEC [VERIFY threshold] |
| LR-GST-003 | E-invoicing mandatory above the notified AATO threshold (₹5 crore) | CGST Rules r.48(4); Notification 10/2023-CT | 1 Aug 2023 | LDC's own invoicing (P20) and client obligations | L | SEC |
| LR-GST-004 | Banking companies and financial institutions including NBFCs: option to avail 50% of eligible ITC each month | CGST Act s.17(4) | in force | NBFC tax pack | L | SEC |
| LR-GST-005 | Interest on loans exempt (Notification 12/2017-CT(Rate)); penal charges treatment per Circular 245/02/2025-GST | Notification 12/2017-CT(Rate); Circular 245/02/2025-GST | in force | NBFC tax pack | L | SEC |
| LR-IT-001 | Income-tax Act 2025 and Income-tax Rules 2026 apply from tax year 2026-27 (TDS s.393, statement Form 140, salary s.392 / Form 130, SFT s.508 / Form 165, tax audit s.63 / Form 26); 1961 Act for tax years up to 2025-26 | ITA 2025; IT Rules 2026 | 1 Apr 2026 | Tax calendar; form names [VERIFY serials] | L | SEC [VERIFY] |

## G.14 Anti-money laundering

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-FIU-001 | Reporting entities file CTR, CBWTR and NTR by the 15th of the following month; STR within 7 working days of being satisfied that a transaction is suspicious | PML (Maintenance of Records) Rules 2005 r.8 | in force | `OV_AML` calendar and event clocks | L | SEC [VERIFY r.8 text] |
| LR-FIU-002 | Principal Officer and Designated Director appointed and communicated to FIU-IND | PML Rules r.7; sector KYC Directions | in force | KMP seed | L | SEC |
| LR-FIU-003 | Reporting through FINGate 2.0 | FIU-IND | in force | Portal map (D-13) | G | SEC |

## G.15 Professional conduct, consumer and telecom rules affecting the platform

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-BCI-001 | Advocates may not solicit work or advertise; no fee-sharing or referral arrangements | Bar Council of India Rules Part VI Ch II r.36 et seq. | in force | Marketplace switches (D-06, NN-20) | L | SEC |
| LR-BCI-002 | CA and CS members' codes restrict referral fees, sharing of fees with non-members and solicitation | ICAI Code of Ethics; Chartered Accountants Act 1949 Schedules; ICSI Code of Conduct; Company Secretaries Act 1980 Schedules | in force | Marketplace switches | L | SEC [VERIFY current clauses] |
| LR-CCPA-001 | Dark patterns prohibited (false urgency, basket sneaking, subscription traps, etc.); misleading advertisements prohibited | CCPA Guidelines for Prevention and Regulation of Dark Patterns 2023; Guidelines on Misleading Advertisements 2022 | in force | Pricing/trial/checkout UX rules (P20, P23) | L | SEC |
| LR-TRAI-001 | Commercial communications via DLT-registered headers and templates; 1600-series for service/transactional calls by RBI/SEBI/IRDAI/PFRDA-regulated entities; 140-series for promotions | TRAI TCCCPR 2018 as amended; TRAI directions 2025–26 | in force | Notification channels (P04, P16) | L | SEC |

## G.16 Obligations of LawDocsComply itself (platform as a company and service provider)

| LR ID | Rule | Citation | Product behaviour | Tier | Status |
|---|---|---|---|---|---|
| LR-PLAT-001 | LDC is a Data Processor for client data and a Data Fiduciary for its own users/leads; DPA with each client; sub-processor list | DPDP Act ss.2(i), 8(2) | P12/P24 contracts and notices | L | SEC |
| LR-PLAT-002 | As a technology service provider to REs, LDC must allow RE and RBI access/audit rights and support RE's outsourcing controls | NBFC OUT Directions (contract clauses, audit and inspection rights) | Regulator view (D-12); audit rooms | L | V-OFF (OUT) |
| LR-PLAT-003 | CERT-In 6-hour reporting and 180-day India log retention apply to LDC's own systems | CERT-In Directions 2022 | P24 runbooks | L | SEC |
| LR-PLAT-004 | GST on SaaS and services; GST-compliant tax invoices (CGST Rules r.46) and e-invoicing above threshold | CGST Act; Rules r.46, r.48(4) | P20 invoices | L | SEC |
| LR-PLAT-005 | Books with non-disableable audit trail and India backup (LawDocs group companies) | Accounts Rules r.3 | Ops Hub accounting | L | SEC |

---


## G.16A Rules for v1.1 modules and families *(v1.1, 25 October 2026)*

New authority codes: `STD` (international standards such as ISO/IEC), `LAW` (general central statutes such as the Limitation Act), `UK`, `AE` (UAE), `SG` (Singapore). All rows below follow §G.0; VERIFY rows are advisory only (NN-38).

### G.16A.1 AI governance (`OV_AI`; P12 §4P; Appendix AA §AA.12)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-RBI-201 | FREE-AI framework: Board-approved AI policy, AI inventory, risk-based governance, consumer disclosure and human route, AI incident reporting, audits — **committee recommendations, not a direction** | RBI Committee report on Framework for Responsible and Ethical Enablement of AI (FREE-AI), 13 Aug 2025 | guidance | `aig` framework "FREE_AI (guidance)"; seeds AI-GOV checkpoints as "Suggestive Compliance"; never hard blocks | G | SEC [VERIFY recommendation numbering] |
| LR-RBI-202 | Model-risk management: central model inventory (no use unless registered), risk tiering reviewed annually, independent validation, adversarial testing and red-teaming of customer-facing tools, override/kill-switch, human oversight, Board-approved framework, retention of records for decommissioned models | RBI draft Guidance on Regulatory Principles for Model Risk Management, 2026 | draft (comments to 24 Jul 2026) | `aig` register gate, validation frequencies, `aig.retention_years` default 10 | G | VERIFY (draft) |
| LR-SEBI-031 | Responsible AI/ML usage by SEBI REs: designated senior officer, testing incl. shadow testing, drift monitoring, client disclosure, log retention ≥ 5 years, vendor responsibility | SEBI consultation paper, 20 Jun 2025 | consultation | Framework "SEBI_AI (draft)" for SEBI families | G | VERIFY |
| LR-MEITY-008 | India AI Governance Guidelines: principle-based, techno-legal approach; transparency across the AI value chain | MeitY, 5 Nov 2025 | guidelines | Framework "MEITY_AI" (voluntary) | G | SEC |
| LR-MEITY-009 | Synthetically generated information: labelling/provenance metadata; shorter takedown and grievance timelines for intermediaries | IT (Intermediary Guidelines and Digital Media Ethics Code) Amendment Rules 2026 | 20 Feb 2026 | Disclosure templates in `aig.disclosures`; applies to tenants that are intermediaries [VERIFY applicability] | L | SEC |
| LR-EU-003 | EU AI Act: prohibited practices; high-risk Annex III systems (e.g., creditworthiness of natural persons, life/health insurance pricing, employment) with deployer duties; Art. 50 transparency; GPAI obligations; Digital Omnibus defers Annex III obligations to 2 Dec 2027 | Regulation (EU) 2024/1689; Digital Omnibus political agreement 6 May 2026 | phased | EU class in `aig.risk_classifications` for EU-nexus entities; FRIA prompt | L | VERIFY (OJ publication, point numbering) |
| LR-STD-001 | AI management system requirements; Annex A controls; AI impact assessment guidance | ISO/IEC 42001:2023; ISO/IEC 42005 | voluntary | Control map; certification-readiness evidence | G | SEC |
| LR-STD-002 | AI risk management functions GOVERN, MAP, MEASURE, MANAGE; generative AI profile | NIST AI RMF 1.0; NIST AI 600-1 | voluntary | Framework "NIST_RMF" | G | SEC |

### G.16A.2 ESG, BRSR and CSR (P27)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-SEBI-032 | BRSR Core reasonable assurance/assessment glide path by market-cap rank and value-chain disclosures/assurance on a comply-or-explain basis, as revised | LODR Reg 34(2)(f); SEBI circular of 28 Mar 2025 on BRSR Core and value chain [VERIFY number and glide-path years] | phased | P27 assurance planning; replaces the "[VERIFY glide]" note on LR-SEBI-013 | L | VERIFY |
| LR-MCA-034 | CSR impact assessment by an independent agency for companies with average CSR obligation ≥ ₹10 crore in the three immediately preceding FYs, for projects with outlay ≥ ₹1 crore completed ≥ 1 year earlier; Annual Action Plan approval; CSR-1 registration of implementing agencies; CSR-2 reporting | CSR Policy Rules 2014 rr.4, 5, 8(3), 9 as amended [VERIFY] | in force | P27 CSR engine workflows and filing tracker | L | SEC |
| LR-MCA-035 | Unspent CSR: ongoing-project unspent → Unspent CSR Account within 30 days of FY end and spend within three FYs; other unspent → Schedule VII fund within six months of FY end; penalty for non-compliance | s.135(5), (6), (7) | in force | P27 timers (NN-33); links to LR-MCA-017 | L | SEC |

### G.16A.3 Litigation, provisions and disclosure (P26)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-ICAI-004 | Provisions recognised when a present obligation, probable outflow and reliable estimate exist; contingent liabilities disclosed unless remote; for non-Ind AS entities AS 29 applies | Ind AS 37; AS 29 (as notified) | in force | P26 matter provisioning fields (probability band, estimate, basis); P11 notes data; never computed by AI (NN-37) | L | SEC |
| LR-SEBI-033 | Listed entities disclose pendency/outcome of litigation or disputes that may have an impact, under materiality policy and Reg 30 timelines | LODR Reg 30 and Schedule III Part B [VERIFY item number]; Reg 30(4) materiality | in force | P26 → P06 event register disclosure clock | L | SEC |
| LR-LAW-001 | Limitation periods for suits, appeals and applications (e.g., three years for most contract suits from accrual) and exclusion of time | Limitation Act 1963, Schedule; ss.4–24 | in force | P26 limitation tracker as Governed rule pack; advisory pending counsel review | G | VERIFY (rule pack) |

### G.16A.4 New families (P15 §4P)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-FIU-004 | Reporting entities include banking companies, financial institutions, intermediaries and persons carrying on designated businesses or professions (e.g., real estate agents, dealers in precious metals/stones, VDA service providers and others notified) | PMLA 2002 s.2(1)(sa), (sb); notifications incl. VDA SPs (Mar 2023) [VERIFY list] | in force | `AML_RE` family types; `OV_AML` spine | L | VERIFY |
| LR-LAW-002 | Registration of firms and changes (constitution, place of business, partners) with the State Registrar of Firms; effect of non-registration on suits | Indian Partnership Act 1932 ss.58–69 | in force | `MSME_FIRM` partnership checkpoints | L | SEC |
| LR-LAW-003 | Udyam registration and classification of micro/small/medium enterprises; payment to MSE suppliers within the agreed period, not beyond 45 days | MSMED Act 2006 ss.7, 15; Udyam notification [VERIFY current thresholds] | in force | `MSME_FIRM` and company buyer obligations | L | VERIFY |

### G.16A.5 International stubs (P25; enablement only per NN-53)

| LR ID | Rule | Citation | Effective | Product behaviour | Tier | Status |
|---|---|---|---|---|---|---|
| LR-EU-004 | Transfers of personal data to third countries need adequacy, appropriate safeguards (SCCs) or derogations | GDPR Chapter V, Arts. 44–49; Decision (EU) 2021/914 | in force | Cross-region transfer checks for EU cell (D-42) | L | SEC |
| LR-UK-001 | Restricted transfers from the UK use the IDTA or the UK Addendum to EU SCCs | UK GDPR Art. 46; DPA 2018; ICO IDTA | in force | UK pack stub | L | SEC |
| LR-AE-001 | UAE federal personal data protection law and free-zone regimes (DIFC, ADGM) with their own transfer rules | Federal Decree-Law No. 45 of 2021; DIFC DP Law 2020; ADGM DP Regulations 2021 | in force [VERIFY executive regulations] | GCC cell and UAE pack stub | L | VERIFY |
| LR-SG-001 | Consent, purpose limitation, data-breach notification (3 calendar days after assessment) and transfer limitation obligations | Singapore PDPA 2012 as amended; PDP Regulations | in force | Singapore pack stub | L | SEC |

## G.17 Verification summary and change log

| Authority block | Rows | V-OFF | V-WEB | SEC | VERIFY |
|---|---|---|---|---|---|
| RBI (NBFC) | 56 | 50 | 0 | 5 | 1 |
| RBI (banks, co-op banks, AIFIs) | 18 | 1 | 2 | 9 | 6 |
| RBI (ARC, AIF, payments, CIC) | 15 | 0 | 0 | 14 | 1 |
| RBI (grievance) | 3 | 1 | 0 | 2 | 0 |
| SEBI | 30 | 0 | 0 | 28 | 2 |
| IFSCA | 8 | 1 | 0 | 7 | 0 |
| IRDAI | 8 | 0 | 0 | 3 | 5 |
| MCA | 33 | 0 | 0 | 31 | 2 |
| ICSI / ICAI | 6 | 0 | 0 | 6 | 0 |
| MeitY / CERT-In / EU / US | 11 | 0 | 0 | 11 | 0 |
| Labour / POSH | 12 | 0 | 0 | 12 | 0 |
| Co-operatives | 24 | 1 | 0 | 20 | 3 |
| Tax | 6 | 0 | 0 | 6 | 0 |
| AML | 3 | 0 | 0 | 3 | 0 |
| Professional / consumer / telecom | 4 | 0 | 0 | 4 | 0 |
| Platform-own | 5 | 1 | 0 | 4 | 0 |
| v1.1 additions (§G.16A, LR-RBI-056) | 22 | 0 | 0 | 13 | 9 |
| **Total** | **264** | **55** | **2** | **178** | **29** |

(Counts are of rows; many SEC rows also carry a `[VERIFY: …]` note on a specific paragraph number, which must be cleared before that rule drives a hard block — G.0 rule 1.)

**Change log.** v1.0 (25 Oct 2026): first issue; RBI NBFC rows imported from the Finbyx v1.5 Part 8A verified set; SEBI LODR 2026 amendment, SEBI MF Regulations 2026, small-company thresholds (Dec 2025), co-operative statistics (PIB Feb 2026) added from this session's research.

**Sources.** As listed in each row and in P15 §15 and P16 §15; secondary sources used this session: https://teamleaseregtech.com/updates/article/49882/ ; https://www.taxscan.in/top-stories/rbi-issues-238-consolidated-master-directions-9000-circulars-guidelines-reorganised-1439158 ; https://blog.ipleaders.in/sebi-lodr-amendment-regulations-2026/ ; https://blog.ipleaders.in/sebi-mutual-funds-regulations-2026/ ; https://vinodkothari.com/2026/02/invits-and-reits-regulatory-actions-for-more-enabling-environment/ ; https://www.taxmann.com/post/blog/mca-raises-small-company-thresholds-to-rs-10-cr-capital-and-rs-100-cr-turnover ; https://static.pib.gov.in/WriteReadData/specificdocs/documents/2026/feb/doc202624779801.pdf ; https://policyholder.gov.in/web/guest/regulations2 ; https://www.jsalaw.com/?p=50709 .

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular NN-38 (VERIFY rules advisory only), X-12. Where text above conflicts with them, the master prevails.
