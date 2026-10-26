# 06 — RBI-OTH Family Command: Other RBI-regulated entities (AIFIs, CICs, payment system operators, FEMA authorised persons)

**Template:** `templates/LDC-TPL-RBI-OTH-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-OTH-v2.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_OTH_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-RBI-OTH-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Entity Category.** General Applicability (Layer) holds the category of RBI regulated entity outside banks, NBFCs and ARCs: AIFIs, Credit Information Companies, payment system operators and participants, and FEMA authorised persons.

**General Applicability (Type) — Entity Type.** General Applicability (Type) names the entity: EXIM, NABARD, NHB, SIDBI, NaBFID; the four CICs; PA, PA-P, PA-CB, PPI issuers, BBPOUs, TReDS, WLAOs, card networks; MTSS agents; AD-II, FFMC. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (RBI_OTH_Sector):**
- All India Financial Institution (AIFI)
- Credit Information Company (CIC)
- Payment System Operator / Participant
- Authorised Person (FEMA)
- All Other RBI Regulated Entities

**General Applicability (Type) (RBI_OTH_Entity):**
- EXIM Bank
- NABARD
- National Housing Bank (NHB)
- SIDBI
- NaBFID
- Credit Information Company (TransUnion CIBIL / Equifax / Experian / CRIF High Mark)
- Payment Aggregator - Online (PA)
- Payment Aggregator - Physical (PA-P)
- Payment Aggregator - Cross Border (PA-CB)
- Prepaid Payment Instrument Issuer (non-bank PPI)
- Bharat Bill Payment Operating Unit (BBPOU)
- Trade Receivables Discounting System (TReDS)
- White Label ATM Operator (WLAO)
- Card Network
- Money Transfer Service Scheme (MTSS) Indian Agent
- Authorised Dealer Category II (AD-II)
- Full Fledged Money Changer (FFMC)
- All (ALL)

**Due Date & Frequency (RBI_OTH_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (RBI_OTH_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Internal Audit, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Internal Audit, Customer Service & Grievance, Information Security, KYC & AML.

**Compliance Type (RBI_OTH_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (RBI_OTH_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (RBI_OTH_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- RBI - Department of Payment & Settlement Systems
- RBI - Foreign Exchange Department (FEMA)
- NPCI
- Ministry of Finance
- SEBI / Stock Exchanges (listed bonds)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- PSS Act s.4 authorisation and conditions are the base rows for payment entities. Directions on PAs (2025) and PPIs carry net worth, escrow and governance rows [VERIFY current titles].
- CIC obligations come from CICRA 2005, the CIC Rules/Regulations 2006 and the RBI CIC directions. Lender-side credit-reporting obligations belong in the lender family.
- AIFIs have 19 topic directions (28 Nov 2025). Treat them like bank directions with Layer = AIFI.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Related Document / Policy / Committee "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Credit information companies in Wave W2; AIFIs and non-bank PPI issuers (Internal Ombudsman only) in Wave W3. Payment-system operators (PA, PPI, card networks, BBPOU, TReDS) and FEMA authorised persons (AD Cat-II, FFMC) are **outside** the 28 Nov 2025 DoR set: catalogue them from the DPSS and FED Master Direction pages in v1.2 (Appendix AB OI-AB-06) and write their sheets from those directions.

### 4.1 All India Financial Institutions
- P1 · Reserve Bank of India (All India Financial Institutions – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/330 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (All India Financial Institutions – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/326 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (All India Financial Institutions – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/323 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/324 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/325 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/334 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/331 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/335 [confirm reference on document], 28 Nov 2025; updated as on 29 Dec 2025 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/337 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (All India Financial Institutions – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/321 [confirm reference on document], 28 Nov 2025; updated as on 07 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/336 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (All India Financial Institutions – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/456 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (All India Financial Institutions – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/457 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (All India Financial Institutions – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/459 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (All India Financial Institutions – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/458 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (All India Financial Institutions – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/329 [confirm reference on document], 28 Nov 2025; updated as on 22 Sep 2026 (RBI page)
- P2 · Reserve Bank of India (All India Financial Institutions – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/338 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (All India Financial Institutions – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/332 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (All India Financial Institutions – Resource Raising Norms) Directions, 2025 — RBI/DOR/2025-26/322 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (All India Financial Institutions – Securitisation Transactions) Directions, 2025 — RBI/DOR/2025-26/328 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (All India Financial Institutions – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/327 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (All India Financial Institutions – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/333 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (All India Financial Institutions – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/320 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)

### 4.2 Credit Information Companies (CICRA 2005 companies — catalogue code CIC-CI)
- P1 · Reserve Bank of India (Credit Information Companies – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/379 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Credit Information Companies – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/470 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Credit Information Companies – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/385 [VERIFY] [confirm reference on document], 14 Jan 2026
- P1 · Reserve Bank of India (Credit Information Companies – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/471 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Credit Information Companies) Directions, 2025 — RBI/DOR/2025-26/378 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)

### 4.3 Non-bank PPI issuers
- P1 · Reserve Bank of India (Non-Bank Prepaid Payment Instruments Issuers – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/384 [VERIFY] [confirm reference on document], 14 Jan 2026

## 5. Family-specific pitfalls

- Writing lender-side CIC reporting rows here. They belong in the lender families.
- Missing card-network and PA-CB cross-border rows.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` (rev 2)`, ` (rev 3)` *(v1.2: " v2" is now the template version)*. Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*. Record the upload date in catalogue column Z.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

This family has **no extension columns** (spec §5). Use General Applicability (Layer), General Applicability (Type) and Conditional Applicability / Exemptions / Thresholds only.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Customer Service & Grievance → Grievance redress / Compensation; Information Security → Cyber incident reporting; KYC & AML → CDD; Returns & Reporting → DPSS / CIMS returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Customer rows → Conduct & Consumer; payment security → IT & Cyber; Fraud; AIFI prudential rows → Credit / Liquidity. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Take Name of Master Direction / Regulation and Instrument Reference No. from the catalogue row and the first page of the direction; Issue Date of Instrument = the issue date printed on the direction (28 Nov 2025 for the DoR consolidated set; 31 Jul 2026 for the DoS set; 14 Jan 2026 for the CEPD directions); Instrument Last Amended On = the "Updated as on" date on the RBI page. On a first sheet written from a consolidated direction, rows carried over from withdrawn circulars are **Re-cited** with the old circular and para in Change Note / Previous Actionable; rows changed by a later amendment are **Amended** with the amendment date in Actionable Last Updated On (master §6A).

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the Credit Information Company resolved each customer complaint on correction of credit information within 30 calendar days of receipt, and paid the prescribed compensation where it did not? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], Reserve Bank of India (Credit Information Companies) Directions, 2025 [VERIFY title] |
| 5 | Department (`department`) | Customer Service & Grievance |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | RBI – DoR |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Reserve Bank of India (Credit Information Companies) Directions, 2025 [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | RBI/DOR/2025-26/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 28-Nov-2025 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 28-Nov-2025 — replace with the "Updated as on" date shown on the RBI page |
| 15 | Actionable Last Updated On (`question_updated_date`) | 28-Nov-2025 |
| 16 | Change Status (`change_status`) | Re-cited |
| 17 | Change Note / Previous Actionable (`change_note`) | Re-cited from RBI circular 'Framework for compensation to customers for delayed updation / rectification of credit information' dated 26 Oct 2023 [VERIFY ref]; substance unchanged. |
| 18 | Source Link (`source_url`) | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx |
| 19 | General Applicability (Layer) (`applic_layer`) | Credit Information Company (CIC) |
| 20 | General Applicability (Type) (`applic_type`) | Credit Information Company (TransUnion CIBIL / Equifax / Experian / CRIF High Mark) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to all CICs. The 30-day period runs from the date the complaint is received by the CIC [VERIFY treatment of time taken by the credit institution]. |
| 22 | Applicable From (`applic_from`) | 28-Nov-2025 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| 24 | Short Title (`short_title`) | Grievance redress - resolution of complaints and compensation |
| 25 | Interpretation / Explanation (`explanation`) | The complainant is entitled to compensation for each day of delay beyond 30 calendar days. Two points govern: the 30-day clock and the split of compensation between the credit institution and the CIC by the cause of delay [VERIFY]. (Abridged.) |
| 26 | Department Function (`dept_function`) | Grievance Redress |
| 27 | Department Sub-function (`dept_subfunction`) | Compensation |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within 30 days of receipt of the complaint |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Customer complaint or grievance received |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Not Required |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Grievance Redressal Policy; Internal Ombudsman |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the CIC Directions; compensation payable to the complainant; RBI may impose a penalty under CICRA [VERIFY section]. |
| 36 | Penalty Provision (`penalty_ref`) | Section 23, Credit Information Companies (Regulation) Act, 2005 [VERIFY] |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Complaint register with receipt and resolution dates; compensation payment proofs; monthly TAT report to management |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Log every complaint with its receipt date. Resolve within 30 calendar days. Where resolution is late, compute and pay compensation, recording who caused the delay. Report TAT breaches monthly to senior management. |
| 42 | Checker Review Points (`checker_points`) | 1. All complaints in the period are logged with dates. 2. Resolution date minus receipt ≤ 30 days, or compensation paid. 3. Compensation amount is correctly computed. 4. Delay attribution is documented. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the complaint register. 2. Sample 25 complaints or 10%, whichever is lower. 3. Re-compute TAT and compensation. Exception: late resolution without compensation, or wrong amount. |
| 44 | Tags / Keywords (`tags`) | cic; credit information; complaint; compensation; tat |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

