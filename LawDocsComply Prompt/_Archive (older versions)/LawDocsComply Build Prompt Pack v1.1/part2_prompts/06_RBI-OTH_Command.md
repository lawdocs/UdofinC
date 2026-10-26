# 06 — RBI-OTH Family Command: Other RBI-regulated entities (AIFIs, CICs, payment system operators, FEMA authorised persons)

**Template:** `templates/LDC-TPL-RBI-OTH-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-OTH-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_OTH_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Entity Category.** Column C holds the category of RBI regulated entity outside banks, NBFCs and ARCs: AIFIs, Credit Information Companies, payment system operators and participants, and FEMA authorised persons.

**Column D — Entity Type.** Column D names the entity: EXIM, NABARD, NHB, SIDBI, NaBFID; the four CICs; PA, PA-P, PA-CB, PPI issuers, BBPOUs, TReDS, WLAOs, card networks; MTSS agents; AD-II, FFMC. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_OTH_Sector):**
- All India Financial Institution (AIFI)
- Credit Information Company (CIC)
- Payment System Operator / Participant
- Authorised Person (FEMA)
- All Other RBI Regulated Entities

**Column D (RBI_OTH_Entity):**
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

**Column H (RBI_OTH_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_OTH_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Internal Audit, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Internal Audit, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_OTH_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_OTH_Risk):** High, Medium, Low.

**Column P reference list (RBI_OTH_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
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
- AIFIs have 19 topic directions (28 Nov 2025). Treat them like bank directions with C = AIFI.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

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

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
