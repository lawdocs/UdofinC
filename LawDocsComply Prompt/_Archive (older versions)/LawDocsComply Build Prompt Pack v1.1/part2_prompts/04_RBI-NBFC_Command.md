# 04 — RBI-NBFC Family Command: Non-Banking Financial Companies (all layers and types)

**Template:** `templates/LDC-TPL-RBI-NBFC-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-NBFC-v1.0` · **Regulator / authority:** Reserve Bank of India (NHB for HFC supervision) · **Named-range prefix:** `RBI_NBFC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — NBFC Layer.** Column C holds the Scale Based Regulation layer: Base, Middle, Upper or Top. Many governance and prudential provisions apply only from the Middle Layer upwards (for example the Compliance Function Directions, 2026 apply to ML and UL) or only to the Upper Layer (for example CET1 and the listing requirement). Use "All Layers" only where the paragraph does not distinguish.

**Column D — NBFC Type.** Column D holds the NBFC type: ICC, MFI, Factor, IFC, IDF, HFC, CIC, MGC, SPD, P2P, AA, NOFHC, NBFC-D, government NBFC, the two no-public-funds categories, and Factoring Act registrants. Several types have their own directions (HFC, CIC, MGC, NOFHC, SPD, MFI, P2P, AA). For those, write the sheet under the type-specific direction and set Column D precisely. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_NBFC_Sector):**
- Base Layer (NBFC-BL)
- Middle Layer (NBFC-ML)
- Upper Layer (NBFC-UL)
- Top Layer (NBFC-TL)
- All Layers

**Column D (RBI_NBFC_Entity):**
- NBFC-Investment and Credit Company (NBFC-ICC)
- NBFC-Microfinance Institution (NBFC-MFI)
- NBFC-Factor
- NBFC-Infrastructure Finance Company (NBFC-IFC)
- Infrastructure Debt Fund (IDF-NBFC)
- Housing Finance Company (HFC)
- Core Investment Company (CIC)
- Mortgage Guarantee Company (MGC)
- Standalone Primary Dealer (SPD)
- NBFC-Peer to Peer Lending Platform (NBFC-P2P)
- NBFC-Account Aggregator (NBFC-AA)
- Non-Operative Financial Holding Company (NOFHC)
- Deposit-taking NBFC (NBFC-D)
- Government-owned NBFC
- NBFC without public funds and without customer interface
- NBFC with customer interface, without public funds
- Registered Factor under Factoring Regulation Act, 2011
- All NBFCs (ALL)

**Column H (RBI_NBFC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_NBFC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security. Family additions: Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security.

**Column O (RBI_NBFC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_NBFC_Risk):** High, Medium, Low.

**Column P reference list (RBI_NBFC_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- NHB (HFC supervision)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- MCA (ROC)
- SEBI / Stock Exchanges (listed NBFCs / NCD issuers)
- Debenture Trustee
- Credit Rating Agency
- IRDAI (corporate agency)
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- The layer is set by asset size and the RBI Upper Layer list [VERIFY thresholds in the SBR Directions 2025]. Some types are always Base Layer (P2P, AA, NOFHC, and NBFCs without public funds and customer interface). Some are never Base Layer (deposit-taking NBFCs, HFCs above the threshold). Write applicability rows for layer determination.
- Each topic direction repeats a "Applicability" chapter. Read it first and set C/D from it, not from memory.
- Government-owned NBFCs have specific carve-outs (for example on some governance provisions). Record them in Column S.
- The 31 July 2026 DoS directions (RBI/DoS/2026-27/460–468) add supervisory obligations: compliance function, cyber/tech risk, digital payment security, fraud risk, internal audit, statutory audit, supervisory returns, miscellaneous supervisory (incl. PCA), auditor's report. Write each as its own sheet. *(v1.1)* The NBFC DoR set has **35** directions (not 30): the 26 common directions plus HFC, CIC, MGC, SPD, NOFHC, AA, P2P, MFI and Miscellaneous.
- NBFC-ICC investment activity (equities, AIF units, REIT/InvIT units, IPO subscriptions) is governed by the Investment Portfolio Direction, the Concentration Risk Direction and the RBI instructions on investments in AIFs [VERIFY current text]. Write these rows with D = "NBFC-Investment and Credit Company (NBFC-ICC)".

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order (Wave W1).** P1 DoR → re-verify and upload the nine owner-built DoS sheets (status "Drafted") → Internal Ombudsman → RB-IOS 2026 → P2 DoR → type-specific directions (HFC, MFI, CIC, P2P, AA, MGC, NOFHC, SPD) → P3. Appendix AB §AB.12 gives a direction-by-direction writing guide (what to capture, split hot-spots, reviewer).

**Legacy NBFC question banks.** Rows written before 28 Nov 2025 are not uploaded as they are. P05 re-cites them through the concordance (Appendix AB §AB.5); when you write a new sheet, ask for the concordance export for that subject and reuse rows whose substance is unchanged, re-citing Column K to the new paragraph.

### 4.1 Department of Regulation — 28 Nov 2025 set (35 live)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/355 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/351 [confirm reference on document], 28 Nov 2025; updated as on 25 Aug 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/347 [confirm reference on document], 28 Nov 2025; updated as on 15 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/349 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/350 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/359 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Governance) Directions, 2025 — RBI/DOR/2025-26/344, 28 Nov 2025; updated as on 24 Jun 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/356 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/361 [confirm reference on document], 28 Nov 2025; updated as on 29 Dec 2025 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/363 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/345 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Registration, Exemptions and Framework for Scale Based Regulation) Directions, 2025 — RBI/DOR/2025-26/339 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/362 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Acceptance of Public Deposits) Directions, 2025 — RBI/DOR/2025-26/346 [confirm reference on document], 28 Nov 2025; updated as on 15 Apr 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Account Aggregator) Directions, 2025 — RBI/DOR/2025-26/368 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Acquisition of Shareholding or Control) Directions, 2025 — RBI/DOR/2025-26/340 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/342 [confirm reference on document], 28 Nov 2025; updated as on 15 Apr 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/354 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Climate Finance and Management of Climate Change Risks) Directions, 2025 — RBI/DOR/2025-26/364 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Core Investment Companies) Directions, 2025 — RBI/DOR/2025-26/367 [confirm reference on document], 28 Nov 2025; updated as on 10 Mar 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Credit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/348 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Housing Finance Companies) Directions, 2025 — RBI/DOR/2025-26/365 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Microfinance Institution) Directions, 2025 — RBI/DOR/2025-26/371 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/373 [confirm reference on document], 28 Nov 2025; updated as on 26 Feb 2026 (RBI page)
- P2 · Reserve Bank of India (Mortgage Guarantee Companies) Directions, 2025 — RBI/DOR/2025-26/369 [confirm reference on document], 28 Nov 2025; updated as on 10 Mar 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Operative Financial Holding Companies) Directions, 2025 — RBI/DOR/2025-26/372 [confirm reference on document], 28 Nov 2025; updated as on 05 Dec 2025 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Peer to Peer Lending Platform) Directions, 2025 — RBI/DOR/2025-26/370 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Prudential Norms on Declaration of Dividends) Directions, 2025 — RBI/DOR/2025-26/360 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/357 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Securitisation Transactions) Directions, 2025 — RBI/DOR/2025-26/353 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Standalone Primary Dealers) Directions, 2025 — RBI/DOR/2025-26/366 [confirm reference on document], 28 Nov 2025; updated as on 10 Mar 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/352 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/358 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P2 · Reserve Bank of India (Non-Banking Financial Companies – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/343 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Non-Banking Financial Companies – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/341 [confirm reference on document], 28 Nov 2025

### 4.2 Department of Supervision — 31 Jul 2026 set (9)
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Auditor's Report) Directions, 2026 — RBI/DoS/2026-27/468 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/460 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/461 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Digital Payment Security Controls) Directions, 2026 — RBI/DoS/2026-27/462 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/463 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/464 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/467 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/465 [confirm reference on document], 31 Jul 2026 — status: Drafted
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/466 [confirm reference on document], 31 Jul 2026 — status: Drafted

### 4.3 Consumer protection
- P1 · Reserve Bank of India (Non-Banking Financial Companies – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/383 [VERIFY] [confirm reference on document], 14 Jan 2026
- Reserve Bank – Integrated Ombudsman Scheme, 2026 (effective 1 Jul 2026) — NBFC version [confirm reference]

### 4.4 Statutes read with the directions
- RBI Act, 1934 Chapter III-B (ss. 45-IA, 45-IB, 45-IC, 45-IE, 45-JA, 45-L, 45-MA, 58B, 58G) — cite in Column N; write a separate statutory sheet only on management instruction
- Factoring Regulation Act, 2011 (registered factors); SARFAESI Act, 2002 (notified NBFCs); PML Act 2002 and PML Rules (read with the KYC direction)

## 5. Family-specific pitfalls

- Using pre-2025 Master Direction paragraph numbers (e.g., the 2023 SBR Master Direction) or citing any circular withdrawn by RBI/2025-26/100. *(v1.1)*
- Writing ML/UL-only rows with C = "All Layers".
- Splitting too little. The Governance and Compliance Function directions contain long lists of Board and committee functions, and each element is its own row.
- Missing glide-path dates for NOF and other phased requirements.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
