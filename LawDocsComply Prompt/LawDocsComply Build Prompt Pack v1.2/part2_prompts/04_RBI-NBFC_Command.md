# 04 — RBI-NBFC Family Command: Non-Banking Financial Companies (all layers and types)

**Template:** `templates/LDC-TPL-RBI-NBFC-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-NBFC-v2.0` · **Regulator / authority:** Reserve Bank of India (NHB for HFC supervision) · **Named-range prefix:** `RBI_NBFC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-RBI-NBFC-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — NBFC Layer.** General Applicability (Layer) holds the Scale Based Regulation layer: Base, Middle, Upper or Top. Many governance and prudential provisions apply only from the Middle Layer upwards (for example the Compliance Function Directions, 2026 apply to ML and UL) or only to the Upper Layer (for example CET1 and the listing requirement). Use "All Layers" only where the paragraph does not distinguish.

**General Applicability (Type) — NBFC Type.** General Applicability (Type) holds the NBFC type: ICC, MFI, Factor, IFC, IDF, HFC, CIC, MGC, SPD, P2P, AA, NOFHC, NBFC-D, government NBFC, the two no-public-funds categories, and Factoring Act registrants. Several types have their own directions (HFC, CIC, MGC, NOFHC, SPD, MFI, P2P, AA). For those, write the sheet under the type-specific direction and set General Applicability (Type) precisely. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (RBI_NBFC_Sector):**
- Base Layer (NBFC-BL)
- Middle Layer (NBFC-ML)
- Upper Layer (NBFC-UL)
- Top Layer (NBFC-TL)
- All Layers

**General Applicability (Type) (RBI_NBFC_Entity):**
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

**Due Date & Frequency (RBI_NBFC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (RBI_NBFC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security. Family additions: Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security.

**Compliance Type (RBI_NBFC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (RBI_NBFC_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (RBI_NBFC_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
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
- Government-owned NBFCs have specific carve-outs (for example on some governance provisions). Record them in Conditional Applicability / Exemptions / Thresholds.
- The 31 July 2026 DoS directions (RBI/DoS/2026-27/460–468) add supervisory obligations: compliance function, cyber/tech risk, digital payment security, fraud risk, internal audit, statutory audit, supervisory returns, miscellaneous supervisory (incl. PCA), auditor's report. Write each as its own sheet. *(v1.1)* The NBFC DoR set has **35** directions (not 30): the 26 common directions plus HFC, CIC, MGC, SPD, NOFHC, AA, P2P, MFI and Miscellaneous.
- NBFC-ICC investment activity (equities, AIF units, REIT/InvIT units, IPO subscriptions) is governed by the Investment Portfolio Direction, the Concentration Risk Direction and the RBI instructions on investments in AIFs [VERIFY current text]. Write these rows with Type = "NBFC-Investment and Credit Company (NBFC-ICC)".

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Related Document / Policy / Committee "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order (Wave W1).** P1 DoR → re-verify and upload the nine owner-built DoS sheets (status "Drafted") → Internal Ombudsman → RB-IOS 2026 → P2 DoR → type-specific directions (HFC, MFI, CIC, P2P, AA, MGC, NOFHC, SPD) → P3. Appendix AB §AB.12 gives a direction-by-direction writing guide (what to capture, split hot-spots, reviewer).

**Legacy NBFC question banks.** Rows written before 28 Nov 2025 are not uploaded as they are. P05 re-cites them through the concordance (Appendix AB §AB.5); when you write a new sheet, ask for the concordance export for that subject and reuse rows whose substance is unchanged, re-citing Clause / Para No. to the new paragraph.

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
- RBI Act, 1934 Chapter III-B (ss. 45-IA, 45-IB, 45-IC, 45-IE, 45-JA, 45-L, 45-MA, 58B, 58G) — cite in Related Document / Policy / Committee; write a separate statutory sheet only on management instruction
- Factoring Regulation Act, 2011 (registered factors); SARFAESI Act, 2002 (notified NBFCs); PML Act 2002 and PML Rules (read with the KYC direction)

## 5. Family-specific pitfalls

- Using pre-2025 Master Direction paragraph numbers (e.g., the 2023 SBR Master Direction) or citing any circular withdrawn by RBI/2025-26/100. *(v1.1)*
- Writing ML/UL-only rows with Layer = "All Layers".
- Splitting too little. The Governance and Compliance Function directions contain long lists of Board and committee functions, and each element is its own row.
- Missing glide-path dates for NOF and other phased requirements.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` (rev 2)`, ` (rev 3)` *(v1.2: " v2" is now the template version)*. Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*. Record the upload date in catalogue column Z.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Customer Interface | With customer interface · Without customer interface | Use where the paragraph turns on customer interface (e.g., fair practices, grievance redress, the lighter regime for NBFCs without public funds and customer interface). |
| Public Funds / Deposits | Deposit-taking (NBFC-D) · Non-deposit-taking with public funds · No public funds | Use where the paragraph turns on public funds or deposits. |
| Asset Size Threshold | Below ₹1,000 crore · ₹1,000 crore and above · ₹5,000 crore and above · ₹10,000 crore and above | Use where an asset-size test inside a layer decides applicability. State the exact test and reference date in Conditional Applicability. [VERIFY each band against the direction text.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-RBI-NBFC-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Compliance → Regulatory Compliance / Compliance function; Credit → Sanction / Exposure norms; Collections & Recovery → Recovery agents / Repossession; Customer Service & Grievance → Grievance redress / Internal Ombudsman; Risk Management → ALM / Liquidity risk; Returns & Reporting → CIMS returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Lending conduct → Conduct & Consumer; prudential → Credit / Liquidity; KYC → Regulatory; Fraud; outsourcing → Third-party. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Take Name of Master Direction / Regulation and Instrument Reference No. from the catalogue row and the first page of the direction; Issue Date of Instrument = the issue date printed on the direction (28 Nov 2025 for the DoR consolidated set; 31 Jul 2026 for the DoS set; 14 Jan 2026 for the CEPD directions); Instrument Last Amended On = the "Updated as on" date on the RBI page. On a first sheet written from a consolidated direction, rows carried over from withdrawn circulars are **Re-cited** with the old circular and para in Change Note / Previous Actionable; rows changed by a later amendment are **Amended** with the amendment date in Actionable Last Updated On (master §6A).

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the NBFC appointed a Chief Compliance Officer (CCO) with the approval of the Board, for a minimum fixed tenure of not less than three years? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], Reserve Bank of India (Non-Banking Financial Companies – Compliance Function) Directions, 2026 [VERIFY title] |
| 5 | Department (`department`) | Compliance |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | RBI – DoS |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Reserve Bank of India (Non-Banking Financial Companies – Compliance Function) Directions, 2026 [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | RBI/DoS/2026-27/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 31-Jul-2026 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 31-Jul-2026 |
| 15 | Actionable Last Updated On (`question_updated_date`) | 31-Jul-2026 |
| 16 | Change Status (`change_status`) | Re-cited |
| 17 | Change Note / Previous Actionable (`change_note`) | Re-cited from RBI circular 'Compliance Function and Role of Chief Compliance Officer (CCO) – NBFCs' dated 11 Apr 2022 [VERIFY ref]; earlier actionable: 'Has the NBFC appointed a CCO for a minimum tenure of 3 years?' — substance unchanged [VERIFY against the 2026 text]. |
| 18 | Source Link (`source_url`) | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx |
| 19 | General Applicability (Layer) (`applic_layer`) | Middle Layer (NBFC-ML); Upper Layer (NBFC-UL) |
| 20 | General Applicability (Type) (`applic_type`) | All NBFCs (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to NBFCs in the Middle and Upper Layers. Base Layer NBFCs are outside this para. [VERIFY carve-outs for government-owned NBFCs.] |
| 22 | Applicable From (`applic_from`) | 31-Jul-2026 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Customer Interface (`ext_*`) | (blank — not a deciding factor here) |
| E2 | Public Funds / Deposits (`ext_*`) | (blank — not a deciding factor here) |
| E3 | Asset Size Threshold (`ext_*`) | ₹1,000 crore and above |
| 24 | Short Title (`short_title`) | Compliance function - appointment and tenure of CCO |
| 25 | Interpretation / Explanation (`explanation`) | 'The CCO shall be appointed for a minimum fixed tenure of not less than 3 years.' Three points govern: Board (or Board committee) approval; a minimum fixed tenure; and removal before the end of tenure only with Board approval and intimation to RBI [VERIFY]. An acting CCO for a long period, or a CCO with business targets, does not satisfy the para. (Abridged.) |
| 26 | Department Function (`dept_function`) | Regulatory Compliance |
| 27 | Department Sub-function (`dept_subfunction`) | Compliance function |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within [VERIFY] days of the vacancy in the office of CCO |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Cessation or resignation of director / KMP / officer |
| 31 | Filing / Reporting / Intimation (`filing_details`) | RBI (intimation) — appointment / premature removal of CCO to the Senior Supervisory Manager [VERIFY timing] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Compliance Policy; Board / Audit Committee; Nomination and Remuneration Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the Compliance Function Directions; RBI may impose a monetary penalty under s.58G, RBI Act, and issue supervisory directions; adverse supervisory rating. |
| 36 | Penalty Provision (`penalty_ref`) | Section 58G(1)(b), Reserve Bank of India Act, 1934 |
| 37 | Risk Type (`risk_type`) | Governance; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board resolution approving the CCO appointment and tenure; appointment letter stating tenure; RBI intimation acknowledgement |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | When the CCO office falls vacant, place a proposal with the candidate's fit-and-proper assessment before the Board. Record the fixed tenure in the Board resolution and the appointment letter. Send the RBI intimation and file the acknowledgement. Track the tenure end date in LawDocsComply. |
| 42 | Checker Review Points (`checker_points`) | 1. Board approval precedes the appointment date. 2. Tenure stated is at least three years. 3. Reporting line and independence match the Compliance Policy. 4. RBI intimation was made within the period [VERIFY]. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the CCO appointment records since the last audit. 2. Inspect the Board resolution, appointment letter and RBI intimation. 3. Inquire whether the CCO has any business targets and corroborate with the KRA document. Exception: tenure below three years, acting arrangement beyond the permitted period, or missing intimation. |
| 44 | Tags / Keywords (`tags`) | cco; chief compliance officer; compliance function; tenure; nbfc ml ul |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

