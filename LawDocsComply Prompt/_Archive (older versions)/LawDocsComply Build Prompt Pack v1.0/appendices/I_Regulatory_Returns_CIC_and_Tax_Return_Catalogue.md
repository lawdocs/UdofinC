# Appendix I — Regulatory Returns, Credit-Bureau and Tax Return Catalogue

> **Binding for:** P11 (Return Studio), P04 (calendar and obligations), P10 (audit checks of returns), P15 (entity logic), P19 (export folders).
> **Status as of:** 25 October 2026. **Owner:** Head of Regulatory Reporting content (platform) with the Infrabyx returns-kernel maintainers.
> **How to use:** This appendix is the seed inventory for the shared returns kernel packs (D-05). Rows marked **VP** are verified against the primary instrument text (fetched on the date shown); **VS** verified against a secondary source or the Finbyx v1.5 extraction of the primary text; **AU** (`ACTIVE_UNVERIFIED`) are indicative and must not generate a filing until a named reviewer confirms them against the primary source and records `verified_at` (Finbyx RR1.5 rule). The binding Direction prevails over the RBI web list (P11 FR-P11-03).

---

## I.0 Correction to the brief — which "supervisory returns" Directions apply

The brief refers to "master directions for filing supervisory returns issued by RBI for different financial institutions on November 28, 2025". The record is:

| Date | Issuer | What was issued | Relevance |
|---|---|---|---|
| 27 Feb 2024 | RBI DoS | Master Direction – Filing of Supervisory Returns (RBI/DoS.DSG/2023-24/110; commercial banks, UCBs, select AIFIs, NBFCs, ARCs; RRBs and HFCs excluded) | **Repealed** by the 2026 set |
| 28 Nov 2025 | RBI DoR | 238 consolidated Master Directions (prudential, governance, KYC, IRACP, FS presentation, credit information reporting, outsourcing, etc.) (RBI press release 2025-26/1588) | Prudential and reporting-content rules (e.g., CIR RBI/DOR/2025-26/349; FS /359; IRACP /356) |
| 8 Apr 2026 | RBI DoS | Draft consolidated supervisory Directions for comment (767 comments received) | Superseded by finals |
| **31 Jul 2026** | RBI DoS | **64 Master Directions** consolidating all DoS instructions across 11 RE types (commercial banks, SFBs, payments banks, LABs, RRBs, UCBs, rural co-operative banks, AIFIs, NBFCs, ARCs, credit information companies), incl. **Supervisory Returns Directions per RE type**; 628 circulars repealed (RBI/DoS/2026-27/221 [VERIFY]; RBI press release 2026-2027/787) | **Binding source for this appendix** |

Record this in `docs/regulations/errata.md` (OI-P11-01).

---

## I.1 Regulators, portals and channels

| Regulator / body | Portal | URL | Channel(s) | Used for | Status |
|---|---|---|---|---|---|
| RBI (DoS, DoR, DSIM, DCM, FMRD) | CIMS Common Login | https://cims.rbi.org.in | Login hub | All CIMS returns | VP (platforms page, 23 Oct 2026) |
| RBI | CIMS DRM (Sankalan) | https://sankalan.rbi.org.in | Template upload (XLSX/XML), screen-based web form (record cap [VERIFY: 2,000]), system-to-system from ADF (documented for banks; not assumed for NBFCs/UCBs) | Supervisory and statistical returns | VS |
| RBI | DAKSH | https://daksh.rbi.org.in | Workflow | Compliance monitoring, inspection items, cyber incidents (6 h), supervisory communication | VS |
| RBI | PRAVAAH | https://pravaah.rbi.org.in | Web forms (108 forms; mandatory from 1 May 2025) | Applications, approvals, authorisations | VS |
| RBI FED | FIRMS | https://firms.rbi.org.in/firms | Web forms | FDI reporting (FC-GPR, FC-TRS, DI, etc.), ODI | VP (portal list) |
| RBI | FLAIR | https://flair.rbi.org.in | Web | Annual Return on Foreign Liabilities and Assets (FLA) | VP |
| RBI | BoP / FETERS | https://bop.rbi.org.in | Upload | Forex transaction reporting by AD banks | VP |
| RBI | SMS | https://sms.rbi.org.in | Web | Statistical surveys (PIP, FLA MF, ITES, ITBS, FCS) | VP |
| RBI | FED Portal | https://fed.rbi.org.in | Web | FEMA reporting | VP |
| RBI | CISBI | https://cisbi.rbi.org.in | Web | Central Information System for Banking Infrastructure (branch data) | VP |
| RBI | Data Collector | https://datacollector.rbi.org.in | Web | Ad hoc data collection | VP |
| RBI legacy | XBRL, DBIE, SAARC portals | — | — | To be discontinued once CIMS is complete | VP |
| NABARD | ENSURE | [VERIFY URL] | Upload | StCB/DCCB/RRB supervisory returns | AU |
| NHB | NHB returns portal | [VERIFY] | Upload | HFC returns | AU |
| FIU-IND | FINnet 2.0 / FINGate 2.0 | https://fingate.gov.in [VERIFY] | XML via report generation/validation utilities | STR, CTR, NTR, CCR, CBWTR | VS |
| CERSAI | CKYCR | https://www.ckycindia.in [VERIFY] | Bulk upload | KYC records (10 days), updates (7 days) | VS |
| CERSAI | Central Registry | https://www.cersai.org.in | Web | Security-interest registration (30 days) | VS |
| CBDT | e-filing / TRACES / reporting portal | https://www.incometax.gov.in ; https://www.tdscpc.gov.in | Upload | TDS/TCS statements, SFT, FATCA/CRS | VS |
| GSTN | GST portal | https://www.gst.gov.in | JSON upload (offline tool), GSP/ASP API | GSTR-1/1A/3B/9/9C, IMS | VS |
| MCA | MCA21 V3 | https://www.mca.gov.in | Web forms with DSC | AOC-4, MGT-7/7A, DPT-3, MSME-1, CSR-2, DIR-3 KYC, ADT-1, LLP Forms 8/11 | VS |
| SEBI | SI Portal (intermediaries) | https://siportal.sebi.gov.in [VERIFY] | Web/upload | Intermediary, AIF, MF reports | AU |
| SEBI (via exchanges) | NSE NEAPS / Digital Exchange; BSE Listing Centre | [VERIFY URLs] | Web, XBRL | LODR filings of listed entities | AU |
| IFSCA | IFSCA reporting portal(s) | [VERIFY] | Web/upload | RE reporting (USD) | AU |
| IRDAI | IRDAI portals (e.g., returns, Bima Sugam / Bima Bharosa for grievances) | [VERIFY] | Web/upload | Insurer and intermediary returns | AU |
| CRCS (Ministry of Cooperation) | CRCS portal | https://crcs.gov.in [VERIFY] | Web | Multi-state co-operative society returns | AU |
| State Registrars of Co-operative Societies | State portals | per State [VERIFY] | Web/hard copy | State co-operative returns | AU |
| CICs (TransUnion CIBIL, CRIF High Mark, Experian, Equifax) | Member SFTP | per member agreement | SFTP (commercial: SFTP only) | Consumer, commercial, MFI files | VS |

---

## I.2 NBFCs — RBI (Non-Banking Financial Companies – Supervisory Returns) Directions, 2026

**Instrument:** RBI/DoS/2026-27/466; DoS.CO.DSG.60/33.01.001/2026-27; 31 Jul 2026; immediate effect; all NBFCs in all layers; **HFCs excluded** (para 3). Returns in para 21; timelines paras 22–23 (quarterly 21 days; monthly 15 days; weekly by Wednesday of the following week; audited returns 5 working days from signing of the auditor's report; event-based as stated). Status: **VS** (Finbyx v1.5 RR1.2 extraction, 23 Oct 2026).

| Code | Return | Freq. | Reference date | Due | Applicability (SR para 21) | Portal / format | NIL | Citation |
|---|---|---|---|---|---|---|---|---|
| DNBS01 | Important Financial Parameters | Q | Quarter-end | 21 days | UL and ML, excluding core investment companies | CIMS; template | No | SR 21(1), 22 |
| DNBS02 | Important Financial Parameters | Q | Quarter-end | 21 days | BL, excluding P2Ps | CIMS; template | No | SR 21(2), 22 |
| DNBS03 | Important Prudential Parameters (CRAR, provisioning) | Q | Quarter-end | 21 days | UL excl. core investment cos; ML excl. core investment cos and SPDs | CIMS; template | No | SR 21(3), 22 |
| DNBS04A | Short Term Dynamic Liquidity | Q | Quarter-end | 21 days | UL; ML excl. SPDs; BL with assets ≥ ₹100 crore solely or at group level, excluding NBFCs without public funds and customer interface, NOFHCs, P2Ps, AAs, MGCs | CIMS; template (ALM Annex layout) | No | SR 21(4), 22 |
| DNBS04B | Structural Liquidity and Interest Rate Sensitivity | M | Month-end | 15 days | As DNBS04A | CIMS; template | No | SR 21(4), 22 |
| DNBS08 | CRILC – NBFCs (borrowers with aggregate exposure ≥ ₹5 crore, SMA status) | M | Month-end | 15 days | UL and ML excl. core investment cos; BL ICCs (excl. no public funds & no customer interface), MFIs and Factors with assets ≥ ₹500 crore | CIMS; template | Yes | SR 21(5), 22 |
| DNBS09 | Return on Defaulted Borrowers | W | Friday or preceding working day | Wednesday of following week | As DNBS08 | CIMS; template | Yes | SR 21(6), 22 |
| DNBS10 | Statutory Auditor Certificate (SAC) | A | 31 Mar | 5 working days of auditor's report signing; ≤ 31 Dec | All NBFCs (filed by statutory auditor with NBFC-created credentials) | CIMS | No | SR 21(7), 23; AUD |
| DNBS11 | Core investment cos – Important Financial Parameters | Q | Quarter-end | 21 days | Core investment companies | CIMS | No | SR 21(8) |
| DNBS12 | Core investment cos – Important Prudential Parameters | Q | Quarter-end | 21 days | Core investment companies | CIMS | No | SR 21(9) |
| DNBS13 | Overseas Investment Details | Q | Quarter-end | 21 days | All NBFCs | CIMS | Yes | SR 21(10) |
| DNBS14 | P2P – Important Financial and Prudential Parameters | Q | Quarter-end | 21 days | P2Ps | CIMS | No | SR 21(11) |
| LEF | Large Exposure Framework | Q | Quarter-end | 21 days | UL | CIMS [VERIFY template] | No | SR 21(12) |
| PDR-III | Statement on Capital Adequacy | Q | Quarter-end | 21 days | SPDs | CIMS | No | SR 21(13) |
| PDR-IV | Select Financial and Balance Sheet Indicators | Q | Quarter-end | 21 days | SPDs | CIMS | No | SR 21(14) |
| STRESS | Stress Test | M | Month-end | 15 days | SPDs | CIMS | No | SR 21(15) |
| IRS | Interest Rate Sensitivity Test | M | Month-end | 15 days | SPDs | CIMS | No | SR 21(16) |
| FMR | Fraud Monitoring Return | Event | Classification date | 14 days | UL; ML; BL with assets ≥ ₹500 crore | CIMS | No | SR 21(17), 23; FRM |
| FUA | FMR Update Application | Event | Update date | Immediate | As FMR | CIMS | No | SR 21(18), 23 |
| FMR4-RBR | Dacoity, robbery, theft, burglary | Q | Quarter-end | 15 days | As FMR | CIMS | No | SR 21(19), 23 |
| FORM-A-SA | Form A Certificate (appointment of SCA/SA) | Event/A | Appointment | 1 month of appointment | All NBFCs | [VERIFY mode: RBI list shows hard copy/digital PDF; SR para 18 online rule] | No | SR 21(20), 23; SA |

**Returns kept alive under other Directions (SR para 26)** [VS; channel per row VERIFY]: DLA register on CIMS template, CCO-certified (Digital Lending Directions — CF para 18); RBR incident by email within 7 days (FRM); group-entity fraud by email to RBI (FRM); cyber incident within 6 hours on DAKSH (CYB); NBFC-D nomination coverage on DAKSH (MSD); CFSS progress, LE breach, CDS/CRT, IRF statements to DoS RO as advised; securitisation quarterly report (format awaited); WD/LD and UCRF files to CICs by SFTP (CIR; §I.10).

**Known web-list variances (pre-loaded `registry_variance`):** (1) DNBS04A/04B BL threshold ₹100 crore per SR vs ₹500 crore on web list — follow SR; (2) DNBS08/09 BL qualifier placement — default ≥ ₹500 crore for ICC/MFI/Factor, union with RSA test, tenant toggle [VERIFY with RBI DoS]; (3) web list shows ARCs for DNBS10/13 — ARC rows belong to the ARC SR (§I.7); (4) Form A mode.

---

## I.3 Commercial banks — RBI (Commercial Banks – Supervisory Returns) Directions, 2026

**Instrument:** RBI/DoS/2026-27/415; DoS.CO.DSG.9/33.01.001/2026-27; 31 Jul 2026; banking companies other than SFBs, PBs, LABs, plus corresponding new banks and SBI; issued under BR Act ss.27, 35A and RBI Act Ch. IIIA. Timelines para 22: weekly → Wednesday of following week; fortnightly (15th) → 7 days; monthly → 15 days; quarterly/half-yearly/yearly → 21 days; audited → 5 working days of auditor's report (s.134). NIL required for CRILC and RDB. Filing online only (para 18), super-user creates maker/checker users (para 19). Penalties under BR Act (para 24). Status: **VP** (fetched 25 Oct 2026).

| # | Return | Frequency | Applies to | Timeline |
|---|---|---|---|---|
| 1 | Asset Liability & Off-Balance-Sheet Exposures (ALE) | M / Q | All | 15 / 21 days |
| 2 | Asset Quality (RAQ) | M (Sec 9) / Q / Y | All | Per periodicity |
| 3 | Operating Results (ROR) | Q | All | 21 days |
| 4 | Risk Based Supervision (RBS) | Q | All | 21 days |
| 5 | Liquidity Return (LR) | F (Part A) / M / Q | All | 7 / 15 / 21 days |
| 6 | Capital Adequacy (RCA-III) | Q | All | 21 days |
| 7 | Interest Rate Sensitivity (IRS) | M | All | 15 days |
| 8 | Large Credits (RLC) | Q | All | 21 days |
| 9 | CRILC | M | All | 15 days; NIL if no borrower ≥ ₹5 crore |
| 10 | Red Flagged Accounts (RFA) | As and when | All | 7 days (exception) |
| 11 | Defaulted Borrowers (RDB) | W | All | Wednesday of following week; NIL |
| 12 | Ownership and Control (ROC) | H | PSBs/PVBs full; foreign banks Sec 2(c),(d) | 21 days |
| 13 | Subsidiaries/JVs/Associates (RoS) | H | Banks with such entities | 21 days |
| 14 | Consolidated Prudential Return (CPR) | H | Banks with such entities | Provisional by end-June and audited by end-September (31 Mar ref); end-December (30 Sep ref) |
| 15 | Balance Sheet Analysis (BSA) | Y | All | 21 days |
| 16 | ALE – Overseas (ALO) | Q | PSBs/PVBs with overseas operations | 21 days |
| 17 | Large Exposures (RLE) | Q | Same | 21 days |
| 18 | Country Exposures and Maturity (CEM) | Q | Same | 21 days |
| 19 | Profitability (ROP) | Q | Same | 21 days |
| 20 | Equity Investment in Capital Market | W | 11 named banks | Wednesday of following week |
| 21 | Connected Exposure (RCE) | Q | All | 21 days |
| 22 | Leverage Ratio (LRR) | Q | All | 21 days |
| 23 | Large Exposure Framework (LEF) | Q | All | 21 days |
| 24 | Basel Liquidity Returns (BLR 1, 2, 4, 5, 6 monthly; BLR 3, 7 quarterly) | M / Q | All | 15 days (BLR 3 and 7: 15 days, exception) |
| 25 | Stressed MSME Sub-ordinate Debt (CGSSD) | M | All | 15 days |
| 26 | Financial Conglomerates (FINCON) | Q | FCs with RBI as principal regulator | 45 days (exception) |
| 27 | Half-yearly Investment Portfolio Review | H | All | 15 June / 15 December (exception) |
| 28 | Branch Allocation to Statutory Branch Auditors | Y | PSBs | Within 1 month of SBA appointment (exception) |
| 29 | Digital Banking Units (DBU) | M | Banks with DBUs | 15 days |
| 30 | Daily Liquidity Data | W | PSBs, PVBs, select FBs | Wednesday of following week |
| 31 | Financial Soundness Indicators (FSI) | Q | PSBs, PVBs | 21 days |
| 32 | Gold Metal Loans (GML) | Q | All | 7 days (exception) |
| 33 | FMR – SCBs | As and when classified | All | 14 days (exception) |
| 34 | FMR Update Application (FUA) | On development | All | Immediate |
| 35 | FMR4 / RBR | Q | All | 15 days (exception) |
| 36 | Vigilance Monitoring Return-I (VMR-I) | Q | PSBs | [VERIFY: not stated in para 23] |
| 37 | Vigilance Monitoring Return-II (VMR-II) | Q | PSBs | [VERIFY] |

**Statutory and statistical returns for banks on the RBI list (selected; VP rows 55–58 fetched; others VS/AU):** Form A (NDTL for CRR, RBI Act s.42) — fortnightly, CIMS; Form VIII (SLR, BR Act s.24) — monthly; Form IX (unclaimed deposits 10+ years, BR Act s.26) — annual, CIMS; Form X (assets and liabilities, DSIM) — monthly, CIMS; Balance Sheet of SCBs (DoR) — yearly, CIMS; BSR-1, BSR-2 — quarterly (annual for RRBs), CIMS; IBS return — quarterly; NRD-CSR — monthly; KCC — quarterly; DAY-NRLM — quarterly; collateral-free loans — quarterly; QPSA/APSA (priority sector) — quarterly/annual; credit to minorities — half-yearly; DRI advances — annual; MSME revival framework — half-yearly; payment of dividend — within a fortnight of declaration; capital issuance report — within 1 week; currency-management returns (defective notes, counterfeit notes by 7th, FNV cell) — DCM; FMRD forex returns for AD Cat-I (FTD daily, GPB daily, FX exposure and hedging quarterly, option transactions weekly, FC borrowings monthly, holdings of foreign currency fortnightly). Full row census from the RBI list is a P11 seeding task (OI-P11-02).

---

## I.4 Small finance banks, payments banks, LABs, RRBs

**SFBs:** RBI (Small Finance Banks – Supervisory Returns) Directions, 2026, RBI/DoS/2026-27/424; DoS.CO.DSG.18/33.01.001/2026-27; 31 Jul 2026 (VS). 33 returns: ALE (M/Q), RAQ (Q/Y), ROR (Q), LR (M Part A; Q Parts A, C), RCA-1 (Basel I capital, Q), IRS (M), RLC (Q), CRILC (M), RFA (7 days), RDB (W), ROC (H), RoS (H), CPR (H; provisional/audited exceptions), BSA (Y), ALO, RLE, CEM, ROP (Q), RCE (Q), BLR (M/Q; BLR 3 and 7 within 15 days), LRR (Q), LBFI – Additional Data on Loan Portfolio, Branch Profile and Financial Inclusion (Q), RoComp – Return on Complaints (Q), stressed MSME sub-debt (M), DBUs (M), FINCON (Q; 45 days), half-yearly investment portfolio review (15 June/15 December), daily liquidity data (W), FSI (Q), GML (Q; 7 days), FMR (14 days), FUA (immediate), FMR4/RBR (Q; 15 days). CPR uses RBI (SFB – Financial Statements: Presentation and Disclosures) Directions, 2025.

**Payments banks, LABs, RRBs:** separate 2026 Supervisory Returns Directions exist within the 64-direction set [AU: numbers and tables to be fetched]; LAB annual report with audited accounts by 30 June (hard copy) on the RBI list (VP row 59).

---

## I.5 Urban co-operative banks — RBI (UCBs – Supervisory Returns) Directions, 2026

**Instrument:** RBI/DoS/2026-27/442; DoS.CO.DSG.36/33.01.001/2026-27; 31 Jul 2026; Primary Co-operative Banks under BR Act (as applicable to co-operative societies, s.56). General timelines: fortnightly 7 days; monthly 15 days; quarterly/yearly 21 days; exceptions as stated (VP for rows with values; AU where marked).

| # | Return | Frequency | Timeline | Applicability |
|---|---|---|---|---|
| 1 | Form B (External Liabilities and Core Assets) | F | 5 days | Scheduled UCBs |
| 2 | Form I (CRR and SLR compliance) | M | 20 days | All UCBs |
| 3 | Form II (Unsecured loans to interested parties) | M | 15 days | All UCBs |
| 4 | Form VI (Offices in India) | Q | 21 days | All UCBs |
| 5 | Form VIII (Unclaimed deposit accounts) | Y (31 Dec) | 30 days | All UCBs |
| 6 | Form IX (Assets and Liabilities) | M | 30 days | All UCBs |
| 7 | Return on Assets and Liabilities (RAL) | Q | 21 days | All UCBs |
| 8 | Return on Earnings (ROE) | [AU] | [AU] | [AU] (RBI list: quarterly, all UCBs) |
| 9 | Return on Asset Quality (RAQ-UCB) | [AU] | [AU] | [AU] |
| 10 | Return on Connected Lending (RCL) | [AU] | [AU] | [AU] (RBI list: quarterly) |
| 11 | Return on Capital Position (RCP) | [AU] | [AU] | [AU] (RBI list: quarterly) |
| 12 | Priority Sector Advances (PSA) | Q (ST I-A) and Y (31 Mar) | 21 days | All UCBs except salary earners' UCBs |
| 13 | Return on Bank Profile (RBP) | Y (31 Mar) | 21 days | All UCBs |
| 14 | CRILC-UCBs | Q | 21 days; NIL | UCBs with total assets ≥ ₹500 crore (borrowers ≥ ₹5 crore) |
| 15 | ALM returns (ALM 1 IRS; term deposits; ALM 3 structural liquidity) | Scheduled: ALM 1 M, ALM 3 F; non-scheduled: all Q | 15 / 7 / 21 days | Scheduled and non-scheduled UCBs |
| 16 | Suit Filed Accounts and Wilful Defaulters (SFA-WD) | Q | 21 days | Scheduled UCBs |
| 17 | Select Advances/Investments (SAI) | Q | 21 days | All UCBs |
| 18 | Financial Soundness Indicators (FSI) | Q | 21 days | Scheduled UCBs |
| 19 | FMR – UCBs | As and when classified | 14 days | All UCBs |
| 20 | FUA | On development | Immediate | [AU] |
| 21 | FMR4 / RBR | Q | 15 days | [AU] |

Legacy RBI-list rows (Dir-I, Dir-IV, Planning-3 quarterly; Form II monthly loans to directors) map into SAI/Form II [VERIFY mapping]. Other UCB statistical returns on the RBI list (cards statistics, mobile banking, QPSA/APSA) are loaded AU.

---

## I.6 State co-operative banks and district central co-operative banks

RBI list rows 64–69 (VP, fetched 25 Oct 2026; DoR; CIMS): Form I (SLR of StCBs/DCCBs, monthly); Form II (unsecured loans, monthly); Form VIII (unclaimed deposits, as on 31 December); Sectoral Deposits (half-yearly June/December); Form B (CRR of StCBs, fortnightly); Form IX (assets and liabilities, monthly). Rural co-operative banks' Supervisory Returns Direction 2026 exists in the DoS set [AU: number]; NABARD ENSURE returns and cyber incident reporting (indicative: OSC returns, CSIR within 6 hours) [AU].

---

## I.7 Asset reconstruction companies — RBI (ARCs – Supervisory Returns) Directions, 2026

**Instrument:** RBI/DoS/2026-27/469; DoS.CO.DSG.63/33.01.001/2026-27; 31 Jul 2026; ARCs registered under SARFAESI s.3 (VP).

| Return | Periodicity | Reference dates | Timeline |
|---|---|---|---|
| DNBS07 – ARCs Important Financial Parameters | Q | 31 Mar, 30 Jun, 30 Sep, 31 Dec | 21 days |
| DNBS10 – Statutory Auditor Certificate | Y | 31 Mar | 5 working days of auditor's report; ≤ 31 Dec |
| DNBS13 – Overseas Investment Details | Q | Quarter-ends | 21 days |

Plus ARC Directions 2025 (DoR.FIN.REC.No.293/26.03.001/2025-26) reporting: audited balance sheet to RO within 1 month of AGM; monthly website list of possession; CERSAI/information-utility filings; CIC reporting where applicable [AU: paragraph numbers].

---

## I.8 HFCs, AIFIs, credit information companies

| Entity | Returns | Status |
|---|---|---|
| HFCs | NHB returns (excluded from NBFC SR) | AU |
| AIFIs (NABARD, SIDBI, EXIM, NHB, NaBFID) | Returns from AIFIs (fortnightly, CIMS — RBI list); capital issuance report; DoS AIFI SR Direction 2026 [AU] | AU (not in first-release target market) |
| Credit information companies | DoS Direction 2026 for CICs [AU] | Out of scope (LDC tenants are CIC members, not CICs) |

---

## I.9 Default approval matrix by return family (tenant-configurable within SoD)

| Family | Maker | Checker | Sign-off |
|---|---|---|---|
| NBFC DNBS01/02/03/11/12/14, PDR | Financial reporting | Head of finance | CFO |
| NBFC DNBS04A/04B, IRS, STRESS | Treasury/ALM | Head of treasury | CFO or ALCO convenor |
| NBFC DNBS08, DNBS09, LEF | Credit risk | Head of risk | CRO (CFO where no CRO) |
| NBFC DNBS13 | Treasury | Head of finance | CFO |
| FMR, FUA, FMR4-RBR | Fraud risk unit | Head of fraud risk | Authority under the Board fraud policy |
| FORM-A-SA | Company Secretary | CFO | MD & CEO |
| DLA register (CIMS) | Digital lending ops | Compliance | CCO certification |
| DNBS10 | Finance (data pack) | — | Statutory auditor files |
| Bank prudential (RCA, LR, BLR, LRR, LEF, RBS) | Regulatory reporting cell | Head of regulatory reporting | CFO / CRO per return |
| Bank CRILC, RFA, RDB | Credit monitoring | Head of credit monitoring | CRO / CCrO |
| UCB Form I/B/IX/VIII | Accounts | GM/Head of finance | CEO |
| UCB RAL/ROE/RCP/RCL/RAQ | Accounts | GM/Head of finance | CEO |
| UCB CRILC, SFA-WD | Credit | Head of credit | CEO |
| StCB/DCCB returns | Accounts | Head of accounts | MD/CEO |
| ARC DNBS07/13 | Finance | Head of finance | CFO |
| Co-operative society Registrar returns | Accountant | Secretary | President/Chairman (per by-laws) |
| CIC files | Bureau operations | — | CIC nodal officer |
| FIU-IND reports | AML analyst | — | Principal Officer |
| GST returns | Tax maker | Tax checker/Head of finance | CFO (or authorised signatory) |
| TDS statements | Tax maker | Head of finance | Authorised person (DDO) |
| SEBI LODR Reg 33 results | Finance | CFO | Board-approved signatory; CEO/CFO certification [VERIFY Reg 33(2)(a)] |
| SEBI LODR Reg 31, 27(2), 13(3) | Secretarial | CS | Compliance Officer (CS) |
| SEBI AIF/MF/intermediary reports | Compliance | Compliance officer | Principal Officer/CEO [VERIFY] |
| IRDAI returns | Finance/Actuarial | CFO / Appointed Actuary | Principal Officer/CEO [VERIFY] |
| IFSCA returns | Finance | Compliance officer | Principal Officer [VERIFY] |
| MCA forms | Secretarial | CS | Director/CS with DSC |

SoD floors: maker ≠ checker ≠ signatory; CRO and CCO never makers (GOV; CMP); sign-off with step-up MFA; delegation only time-boxed (P02).

---

## I.10 Credit-bureau submission catalogue

**Legal frame:** Credit Information Companies (Regulation) Act 2005; CIC Rules and Regulations 2006; RBI (NBFC – Credit Information Reporting) Directions, 2025 (RBI/DOR/2025-26/349) as amended on 4 Dec 2025 (RBI/DOR/2025-26/117; DoR.FIN.REC.No.324/20.16.056/2025-26 [VERIFY reference numbers]; in force 1 Jul 2026); CIC-side amendment RBI/DOR/2025-26/119 [VERIFY]; equivalent bank/UCB CIR Directions [VERIFY]. Membership of all four CICs (CIR para 6); no borrower consent (para 11). Status VS (Finbyx RR6).

| File | Format pack | Cycles (from 1 Jul 2026) | Due | Transport | Key rules |
|---|---|---|---|---|---|
| Consumer | UCRF Consumer v3.74 (4 Feb 2026; w.e.f. 1 Jul 2026) | W1 (9th), W2 (16th), W3 (23rd) incremental; ME full | W: 4 calendar days; ME: 5th of next month | SFTP or CIC portal per member spec; `.gpg` where required | TLV segments PN/ID/PT/EC/PA/TL/TH/ES; DPD cap 900; ID 09 CKYC |
| Commercial | UCRF Commercial v3.10 delimited (13 Apr 2026) | Same | Same | **SFTP only** (since v3.8) | Pipe-delimited; `~`/`^` reject file; relationship segment for accounts from 1 Jul 2018; written-off/settled amounts enforced from 1 Apr 2027 |
| MFI (incl. SHG) | UCRF MFI v3.3.1 (Apr 2026) | Same (+ DL daily for MFIN members by SRO directive) | Same | SFTP | Separate SHG and JLG+individual files; DPD 000–999 mandatory; household income mandatory |
| Correction (DC) | Same formats | On dispute/correction | 21 days to send corrections (CIR 35(2)); overall 30 days (CICRA s.21(3); CIR 35(1)) | As above (CIBIL corrections not encrypted per TransUnion note) | Compensation ₹100/day of delay, apportioned (CIR 35) |
| Rejection resubmission (RR) | Same | After rejection report (CICs within 3 days) | Before/with next reference-date file (Annex VI: 20th, 27th, 5th, 13th) | As above | Repair at source |
| Wilful/large defaulter (WD/LD) | Per CIC/RBI WD directions [VERIFY layout] | As prescribed | As prescribed | SFTP | ML+ for wilful defaulter classification |

**Annex VI timetable:** ref 9th → share by 13th, CIC rejections by 16th, CI correction by 20th; ref 16th → 20th / 23rd / 27th; ref 23rd → 27th / 30th / 5th next month; month-end → 5th / 8th / 13th. Half-yearly DQI review to top management within two months of half-year end (CIR 17). Nodal officer changes notified to every CIC within 5 days (CIR 34(2)(ii)).

---

## I.11 IFSCA-regulated entities (status AU unless stated)

| Entity (D-08 IFSCA list) | Reporting basis | Indicative returns | Currency |
|---|---|---|---|
| Finance Company / Finance Unit (FCFU) | IFSCA (Finance Company) Regulations 2021 reg 9 [VERIFY]; prudential and governance circulars | Periodic financial and prudential returns; owned-fund components; large exposures; top NPAs; ALM [VERIFY] | USD |
| IFSC Banking Unit (IBU) / IFSC Banking Company | IFSCA Banking Handbook (GEN/COB/PRU/etc.) [VERIFY versions — owner's IFSCA folder holds GEN Directions v5.0] | Prudential returns, liquidity, large exposures, statistical returns; FIU-IND | USD |
| Fund Management Entity (FME) and schemes | IFSCA (Fund Management) Regulations 2025 (as amended to 10 Sep 2026 in owner's folder) | Quarterly scheme reports, annual compliance reports, audited accounts [VERIFY] | USD |
| Capital market intermediaries (BDCM, CUDP, IAPM, INVB, DIST, DTEE, CRA, RESE, ERDP, KRA) | Respective IFSCA regulations 2025–26 | Periodic compliance and activity reports [VERIFY] | USD |
| Insurance (IIO, IIIO, MGA) | IFSCA insurance regulations 2021–2026 (Registration, Appointed Actuary, Solvency, Investment, Financial Statements, Records, MGA) | Solvency returns, actuarial reports, financial statements, investment returns [VERIFY] | USD |
| Payments, FinTech, TechFin, Ancillary, BATF, GIC, EDU, ITFS, Bullion | Respective regulations/frameworks | Periodic reports per framework [VERIFY] | USD |
| All REs | IFSCA AML/CFT/KYC Guidelines 2022 (Master Guidelines as on 3 Aug 2026 in owner's folder); FIU-IND | STR/CTR/CBWTR; FIU registration updates | — |

The owner's IFSCA compliance-question sheets (e.g., "SAMPLE – Finance Company Regulations 2021", "05 Insurance – Appointed Actuary Regulations 2022") already capture "Filing and Reporting details/Intimation" in column P; P11 imports those column-P values as candidate return definitions for verification (link P03 ↔ P11) [REC].

---

## I.12 SEBI-regulated entities (status AU unless stated)

**Listed entities (SEBI (LODR) Regulations 2015 as amended):**

| Filing | Regulation | Frequency / due | Notes |
|---|---|---|---|
| Financial results | Reg 33 | Quarterly within 45 days; annual audited within 60 days of FY end | Reg 33(2)(a) CEO/CFO certification; limited review/audit report [VERIFY] |
| Shareholding pattern | Reg 31 | Quarterly within 21 days [VERIFY]; also before listing and on capital restructuring | XBRL on exchange portals |
| Corporate governance report | Reg 27(2) | Quarterly within 21 days [VERIFY] | — |
| Investor grievance statement | Reg 13(3) | Quarterly within 21 days [VERIFY] | — |
| Related-party transactions disclosure | Reg 23(9) | Half-yearly, with results | — |
| Annual Secretarial Compliance Report | Reg 24A(2) | Within 60 days of FY end | Signed by secretarial auditor (from 1 Apr 2025) |
| Annual report incl. BRSR | Reg 34 | Not later than the day of dispatch to shareholders | BRSR Core assurance for top entities on glide path [VERIFY] |
| Event disclosures | Reg 30 + Schedule III | Within 24 hours (30 min for Board outcomes [VERIFY]) | P06 event engine |
| Reconciliation of share capital audit | SEBI (Depositories and Participants) Regulations 2018 reg 76 | Quarterly within 30 days [VERIFY] | PCS/CA certificate |
| Certificate of compliance (share transfer facilities) | Reg 7(3) | [VERIFY current applicability] | — |
| SAST disclosures | SAST Reg 29, 31 | Event / annual (Reg 31(4)) [VERIFY] | — |
| PIT disclosures | PIT Reg 7 | Event (within 2 trading days) | Structured digital database (Reg 3(5)) |
| Debt-listed entities | SEBI NCS Regulations / LODR Ch. V | Half-yearly results, asset cover, etc. [VERIFY] | — |

**Mutual funds / AMCs, AIFs, REITs/InvITs, intermediaries:** periodic reporting under the respective SEBI master circulars (e.g., AIF quarterly activity report within the prescribed days via the SI portal; MF monthly/half-yearly portfolio disclosures and AMFI data; REIT/InvIT quarterly/half-yearly reports and valuation reports; stock broker/DP periodic submissions and half-yearly internal audit reports to exchanges/depositories; IA/RA annual compliance audit) — every row AU until a SEBI analyst confirms the current master circular and paragraph.

---

## I.13 IRDAI-regulated entities (status AU)

| Entity | Indicative returns / disclosures | Basis [VERIFY] |
|---|---|---|
| Insurers (life, general, health, reinsurers) | Public disclosures (quarterly, NL/L forms); solvency returns (quarterly); actuarial valuation reports (annual); investment returns (quarterly/monthly); corporate governance compliance report (annual); RPT disclosures; fraud monitoring reports; grievance returns (Bima Bharosa) | IRDAI (Actuarial, Finance and Investment Functions of Insurers) Regulations 2024 and master circulars; IRDAI (Corporate Governance for Insurers) Regulations 2024; IRDAI (Protection of Policyholders' Interests…) Regulations 2024 |
| Insurance brokers | Annual audited accounts and returns; half-yearly business returns; compliance certificates | IRDAI (Registration of Intermediaries / Insurance Brokers) Regulations and 2024 master circular |
| Corporate agents, web aggregators, IMFs, TPAs, surveyors | Annual/half-yearly returns per regulations | Respective regulations and 2024 master circulars |

---

## I.14 Co-operative societies (status AU; per-State packs)

| Society type | Authority | Indicative returns |
|---|---|---|
| Multi-state co-operative society | Central Registrar (CRCS), MSCS Act 2002 (amended 2023) and MSCS Rules 2023 | Annual return within 6 months of FY end (s.120) incl. annual report, audited statements, plan for surplus disposal, list of amendments to by-laws, AGM date, election dates; quarterly/periodic returns as prescribed [VERIFY]; audit by CRCS-panel auditor (s.70); election through the Co-operative Election Authority (s.45) |
| State co-operative society (credit or other) | State Registrar under State Act (e.g., Maharashtra Co-operative Societies Act 1960; UP Co-operative Societies Act 1965; Rajasthan Co-operative Societies Act 2001; Delhi Co-operative Societies Act 2003; Gujarat Co-operative Societies Act 1961) | Annual return (e.g., Maharashtra s.79/79(1A) within six months), audit memo and rectification report, statutory registers, AGM proceedings, election filings with the State Co-operative Election Authority [VERIFY per Act] |
| Credit co-operative society as CIC member | CICs | CIC files (§I.10) only if admitted as member |

Late returns can disqualify directors in some regimes (e.g., MSCS s.43 [VERIFY]) — P16 governance alerts.

---

## I.14A AML, KYC-registry, security-interest and FEMA reporting (added in review R4; status VS/AU)

Serves P11 FR-P11-48 and FR-P11-49. Applies to every RE family with a PMLA reporting-entity status (banks, NBFCs, co-operative banks, ARCs, SEBI and IRDAI intermediaries, IFSCA REs) and, for FEMA rows, to any tenant with foreign investment, overseas investment or external commercial borrowing. LDC prepares, validates and packages; the Principal Officer, the AD bank or the tenant files (NN-08). For Finbyx tenants the files are mirrored, never regenerated (NN-39).

| Report | Basis | Frequency / due | Channel | Prepared from | Status |
|---|---|---|---|---|---|
| Cash Transaction Report (CTR) | PML (Maintenance of Records) Rules 2005 r.3, r.8 | Monthly, by the 15th of the following month | FIU-IND FINnet 2.0 (XML via report generation/validation utility) | Cash transactions of more than ₹10 lakh, or integrally connected series | VS [VERIFY current thresholds and utility version] |
| Suspicious Transaction Report (STR) | PML Rules r.3, r.8 | Within 7 days of concluding that a transaction is suspicious | FINnet 2.0 | AML alert disposition (P12/Finbyx) | VS — sealed to AML roles; tipping-off protection |
| Counterfeit Currency Report (CCR) | PML Rules r.3, r.8 | Monthly, by the 15th (cash-handling REs) | FINnet 2.0 | Branch/cash records | VS |
| Non-Profit Organisation Transaction Report (NTR) | PML Rules r.3, r.8 | Monthly, by the 15th | FINnet 2.0 | Receipts by NPOs of more than ₹10 lakh | VS [VERIFY] |
| Cross-Border Wire Transfer Report (CBWTR) | PML Rules r.3, r.8 | Monthly, by the 15th | FINnet 2.0 | Cross-border wires > ₹5 lakh (where the RE is a party) | VS [VERIFY threshold] |
| FIU-IND registration and Principal/Designated Officer updates | PMLA s.12; PML Rules r.7 | Event | FINnet 2.0 | P06/P13 KMP records | VS |
| CKYCR upload | PML Rules r.9(1A); KYC Directions of the RE family | KYC record within 10 days of commencement of the account-based relationship; updates within 7 days [VERIFY per family direction] | CKYCR bulk upload | Customer master (pseudonymised in LDC; clear identifiers only in the RE's own system) | VS |
| CERSAI security-interest registration | SARFAESI Act s.23; Security Interest (Enforcement) Rules | Within 30 days of creation, modification or satisfaction | CERSAI Central Registry | Collateral register | VS |
| Annual Return on Foreign Liabilities and Assets (FLA) | FEMA; RBI Master Direction on Reporting under FEMA | Annual, by 15 July [VERIFY] | RBI FLAIR | Audited (or provisional) balance sheet, FDI/ODI positions | VS |
| FC-GPR / FC-TRS / DI (downstream investment) | FEMA (Non-debt Instruments) Rules 2019; Reporting MD | FC-GPR within 30 days of allotment; FC-TRS within 60 days of transfer; DI within 30 days [VERIFY] | RBI FIRMS (via AD bank) | P06 share-capital register | VS |
| ECB-2 | FEMA ECB framework | Monthly, within 7 working days of month end [VERIFY] | Through AD bank | Borrowings data template (`LDC-DT-BORROWINGS`) | VS |
| ODI Annual Performance Report (APR) | FEMA (Overseas Investment) Rules/Regulations 2022 | Annual, by 31 December [VERIFY] | Through AD bank | Overseas investment register | VS |

---

## I.15 GST returns (status VS)

| Return | Content | Frequency / due | Notes |
|---|---|---|---|
| GSTR-1 | Outward supplies; HSN Table 12 (B2B and B2C tabs; digit rules by AATO) | Monthly by 11th (QRMP quarterly by 13th) [VERIFY] | JSON (offline-tool schema) |
| GSTR-1A | Amendments to current period GSTR-1 | After GSTR-1, before GSTR-3B | Only route to correct auto-filled liability |
| IFF | Invoice furnishing facility (QRMP) | Optional, first two months of quarter | — |
| GSTR-3B | Summary return; Table 3 auto-populated and locked from July 2025 period; Table 4 ITC incl. 4B(1) | Monthly by 20th (QRMP 22nd/24th) [VERIFY] | Banks/FIs/NBFCs may opt for 50% ITC (s.17(4), r.38) |
| GSTR-9 | Annual return | 31 Dec following FY [VERIFY] | From books, GSTR-1, GSTR-3B |
| GSTR-9C | Reconciliation statement (self-certified) | With GSTR-9 where AATO > ₹5 crore [VERIFY] | — |
| IMS | Invoice Management System actions | Continuous (live from 14 Oct 2024) | Accept/reject/pending; drives GSTR-2B |
| E-invoice (IRP) | IRN generation | Per invoice for AATO > ₹5 crore (Notification 10/2023-CT); **exempt for banking companies/FIs incl. NBFCs** (r.48(4)) | Not via LDC as IRP |
| Time bar | Returns cannot be filed > 3 years after due date (from July 2025) | — | Calendar flag |

---

## I.16 Income-tax (Income-tax Act 2025 in force 1 Apr 2026; status VS with [VERIFY] on every number)

| Obligation | Tax year 2026-27 onwards (ITA 2025) | FY 2025-26 and earlier (ITA 1961) | Due |
|---|---|---|---|
| Non-salary TDS statement | Form 140 (s.397(3)(b); Rule 219) | Form 26Q | 31 Jul, 31 Oct, 31 Jan, 31 May |
| Salary TDS statement | Form 138 | Form 24Q | Same |
| Non-resident TDS | Form 144 | Form 27Q | Same |
| TCS | Form 143 | Form 27EQ | Quarterly [VERIFY] |
| TDS certificates | Form 130 (salary), 131 (non-salary), 133 (TCS) | Forms 16, 16A, 27D | After statement processing |
| Declarations for no deduction | Form 121 | Forms 15G/15H | — |
| Lower/nil deduction certificate | Form 128 | Form 13 | — |
| SFT | s.508, Form 165 | s.285BA, Form 61A | 31 May [VERIFY] |
| FATCA/CRS | Form 166 | Form 61B | [VERIFY] |
| Tax credit statement | Form 168 [VERIFY] | Form 26AS | — |
| Tax audit | s.63, Form 26 | s.44AB, Forms 3CA/3CB/3CD | Per due date of return [VERIFY] |
| NPA interest on receipt basis | s.56 (notified NBFC classes) | s.43D | — |
| Bad debt / provision deduction | s.31 [VERIFY] | s.36(1)(vii)/(viia) | — |

---

## I.17 MCA and LLP filings (status VS/AU)

| Form | Purpose | Due | Data source |
|---|---|---|---|
| AOC-4 / AOC-4 CFS | Financial statements | 30 days of AGM | P11 accounting bridge |
| AOC-4 NBFC (Ind AS) / CFS NBFC (Ind AS) | Ind AS NBFC financial statements (substituted by Companies (Accounts) Second Amendment Rules 2025, in force 14 Jul 2025) [VERIFY] | 30 days of AGM | P11 |
| AOC-4 XBRL | Where XBRL triggers apply (not NBFCs; banks exempt till further order) | 30 days of AGM | P11 mapping workbook |
| MGT-7 / MGT-7A | Annual return | 60 days of AGM | P06 registers |
| ADT-1 | Auditor appointment | 15 days of AGM | P06/P10 |
| DPT-3 | Return of deposits / exempted deposits | 30 June annually [VERIFY] | P11 borrowings/deposits |
| MSME-1 | Outstanding payments to MSE suppliers > 45 days | Half-yearly (30 Apr / 31 Oct) [VERIFY current applicability] | P11 vendor ageing |
| CSR-2 | CSR report | [VERIFY: with/after AOC-4] | P06 |
| DIR-3 KYC | Director KYC | Once every three years from 31 Mar 2026 (next due 30 Jun 2028; master §7) and within 30 days of a change in contact details [VERIFY G.S.R.] | P06 |
| BEN-2 | Significant beneficial owner | 30 days of declaration | P06 |
| CRA-2 / CRA-4 | Cost auditor appointment / cost audit report | 30 days of Board meeting / 30 days of receipt | P06/P10 |
| MR-3 | Secretarial audit report (annexed to Board's report) | With Board's report | P10 |
| LLP Form 11 | LLP annual return | 30 May | P06 (LLP) |
| LLP Form 8 | Statement of account and solvency | 30 October | P11 (LLP) |

---

## I.18 Labour-law returns

Covered in Appendix T (Labour Codes in force from 21 Nov 2025; central and State rules; registers and returns, EPF/ESI/PT/LWF filings). P11 packages Form 138 TDS from P13 payroll; P13 owns labour returns.

---

## I.19 Data-definition mapping approach

1. **RBI harmonised definitions first.** Every kernel `data_element` stores a reference to the RBI harmonised definition where one exists (RBI Data Definitions page, updated 17 Jun 2026: Banking Statistics I — 189 definitions across assets 27, liabilities 43, off-balance-sheet 14, P&L 10, miscellaneous 95; Banking Statistics II incl. financial inclusion; Consumer Education and Protection; External Sector; Financial Markets; Payment Systems; Technical Guidance Note on Harmonisation of Banking Statistics, 30 Mar 2017) and to the "Validation rules/Taxonomy" page.
2. **Instrument definitions second.** Where a Direction defines a term (e.g., "public funds", "customer interface", "core investment company", "large exposure"), the element cites the paragraph.
3. **Accounting definitions third.** Schedule III line items, Ind AS/AS definitions (Appendix J).
4. **One element, many outputs.** An element (e.g., `ADV_GROSS`) feeds every return, statement and ratio that uses it, so a change in definition is a single versioned change with an impact list.
5. **LDC data templates** (P11 §4D) carry the element reference in each column's definition so that clients fill data to the regulator's meaning, not their own ledger names.
6. **Lineage** from cell to source line (P11 §4F).

---

## I.20 Maintenance

- Each row carries: instrument citation, source URL, fetch date, verifier, verified_at, status (VP/VS/AU), change log.
- Regulatory change (P05) monitors RBI DoS/DoR, SEBI, IFSCA, IRDAI, MCA, CBDT, GSTN, NABARD, NHB, CRCS and State Registrars; any new or amended return opens a kernel pack change request (Ecosystem Spec §14.2) and a P05 Update for affected tenants.
- Quarterly reconciliation of the registry against the RBI List of Returns page (row census and variance log).

## I.21 Sources (accessed 25 Oct 2026 unless stated)

- RBI List of Returns — https://rbi.org.in/scripts/BS_Listofallreturns.aspx ; Reporting Platforms — https://rbi.org.in/scripts/ReportingPlaform.aspx ; Data Definitions — https://rbi.org.in/scripts/DataDefinition.aspx ; Reporting FAQs — https://rbi.org.in/scripts/ReportingFAQ.aspx
- Commercial Banks SR 2026 — https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13638 ; SFB SR 2026 — https://taxguru.in/rbi/rbi-issues-small-finance-banks-supervisory-returns-directions-2026-effect.html ; UCB SR 2026 — https://rbi.org.in/scripts/BS_ViewMasDirections.aspx?id=13611 ; ARC SR 2026 — https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=13584
- RBI press release 31 Jul 2026 (64 DoS Directions) — https://rbi.org.in/scripts/BS_PressReleaseDisplay.aspx?prid=63265 ; repeal notification summary — https://taxguru.in/rbi/rbi-repeals-628-supervisory-circulars-issuing-64-consolidated-directions.html
- RBI 238 consolidated Directions (28 Nov 2025) — https://website.rbi.org.in/documents/d/rbi/pr1588rbiconsolidatedmasterdirections-1-
- Master Direction – Filing of Supervisory Returns 2024 (repealed) — https://website.rbi.org.in/documents/87730/39710850/Final+MD+on+Returns+filing+%28Governor+Approved%29+-+2024+%2827-2-2024%29.pdf
- Finbyx Master Prompt v1.5 Parts 7B and 7C (owner's corpus; NBFC SR table, CIR cadence, UCRF format packs, GST and ITA 2025 concordance)
- Owner's IFSCA Documents folder (regulations and compliance-question sheets, Sep–Oct 2026)

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular X-12, X-31, X-32, NN-39. Where text above conflicts with them, the master prevails.
