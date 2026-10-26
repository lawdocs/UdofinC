# 03 — RBI-RCB Family Command: Rural Co-operative Banks (StCBs and DCCBs)

**Template:** `templates/LDC-TPL-RBI-RCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-RCB-v1.0` · **Regulator / authority:** Reserve Bank of India (regulation); NABARD (supervision) · **Named-range prefix:** `RBI_RCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — RCB Category.** Column C distinguishes State Co-operative Banks from District Central Co-operative Banks.

**Column D — RCB Type / Overlay.** Column D adds scheduled status and supervisory overlays. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_RCB_Sector):**
- State Co-operative Bank (StCB)
- District Central Co-operative Bank (DCCB)
- All Rural Co-operative Banks

**Column D (RBI_RCB_Entity):**
- StCB - Scheduled
- StCB - Non-Scheduled
- DCCB
- RCB under Supervisory Action / s.35A Directions
- RCB with CBS / Shared Service Entity arrangement
- All RCBs (ALL)

**Column H (RBI_RCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_RCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_RCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_RCB_Risk):** High, Medium, Low.

**Column P reference list (RBI_RCB_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- NABARD (ENSURE)
- NABARD (Department of Supervision)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- Registrar of Co-operative Societies (State)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- DICGC
- General Body / Members
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- RBI regulates rural co-operative banks under the BR Act. NABARD supervises them and receives most returns (ENSURE portal) [VERIFY current portal per return].
- PACS are not banks. Put PACS obligations in COOP-CCS.
- Where a direction says "StCBs and DCCBs", use C = "All Rural Co-operative Banks".

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Wave W2, after the UCB set (clone from UCB where the subject exists). Supervision of StCBs and DCCBs rests largely with NABARD; RBI issued only three DoS directions for RCBs.

- P1 · Reserve Bank of India (Rural Co-operative Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/310 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/299 [confirm reference on document], 28 Nov 2025; updated as on 25 Aug 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/306 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/302 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/304 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/305 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/314 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/298 [confirm reference on document], 28 Nov 2025; updated as on 25 May 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/311 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/316 [confirm reference on document], 28 Nov 2025; updated as on 18 Sep 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/318 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/300 [confirm reference on document], 28 Nov 2025; updated as on 15 May 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/317 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/451 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Rural Co-operative Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/453 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Rural Co-operative Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/452 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Rural Co-operative Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/296 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/309 [confirm reference on document], 28 Nov 2025; updated as on 18 May 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/303 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/301 [confirm reference on document], 28 Nov 2025; updated as on 25 Aug 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/308 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/319 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Prudential Norms on Declaration of Dividends) Directions, 2025 — RBI/DOR/2025-26/315 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/312 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/307 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/313 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/297 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Rural Co-operative Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/386 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Rural Co-operative Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/295 [confirm reference on document], 28 Nov 2025

**Read with:** Banking Regulation Act, 1949 (s.56); NABARD supervisory instructions (cite in Column N/P where they set the reporting route) [VERIFY current NABARD circulars]; State Co-operative Societies Acts.

## 5. Family-specific pitfalls

- Citing UCB directions for RCBs. The 2025 sets are separate.
- Missing the NABARD filing route in Column P.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
