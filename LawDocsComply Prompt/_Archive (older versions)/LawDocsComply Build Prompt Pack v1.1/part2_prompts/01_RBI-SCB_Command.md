# 01 — RBI-SCB Family Command: Commercial Banks, SFBs, Payments Banks, LABs and RRBs

**Template:** `templates/LDC-TPL-RBI-SCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-SCB-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_SCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Bank Category.** Column C holds the bank category, matching RBI's regulated-entity categories in the 28 November 2025 consolidated directions. Commercial Banks, SFBs, PBs, LABs and RRBs each have their own set of topic directions. Write one sheet per direction per category. Where the same topic direction exists for several categories and the text is the same, you may write one sheet with several C values ("Commercial Bank; Small Finance Bank (SFB)"). Do this only after checking that the paragraphs are identical.

**Column D — Bank Type / Overlay.** Column D refines the bank type or adds an overlay that changes applicability: PSB vs private, foreign bank in branch mode vs WOS, D-SIB, listed bank, bank under PCA. Use "All Banks (ALL)" when the paragraph applies regardless of type. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_SCB_Sector):**
- Commercial Bank
- Small Finance Bank (SFB)
- Payments Bank (PB)
- Local Area Bank (LAB)
- Regional Rural Bank (RRB)
- All Banks

**Column D (RBI_SCB_Entity):**
- Public Sector Bank (PSB)
- Private Sector Bank (Old)
- Private Sector Bank (New)
- Universal Bank (On-tap Licence)
- Foreign Bank - Branch Mode
- Foreign Bank - Wholly Owned Subsidiary (WOS)
- Domestic Systemically Important Bank (D-SIB)
- Listed Bank
- Bank with Overseas Branches / Subsidiaries
- Bank under Prompt Corrective Action (PCA)
- Small Finance Bank (SFB)
- Payments Bank (PB)
- Local Area Bank (LAB)
- Regional Rural Bank (RRB)
- All Banks (ALL)

**Column H (RBI_SCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_SCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_SCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_SCB_Risk):** High, Medium, Low.

**Column P reference list (RBI_SCB_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- RBI - Foreign Exchange Department (FEMA)
- RBI - Department of Payment & Settlement Systems
- NABARD (ENSURE) - RRBs
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- DICGC
- SEBI / Stock Exchanges (listed banks)
- Ministry of Finance (DFS) - PSBs
- MCA
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- Decide the category from the licence: banking company (commercial), SFB, PB, LAB or RRB.
- PSB-specific provisions mostly come from the Bank Nationalisation Acts / SBI Act and DFS guidelines, not RBI directions. Use D = "Public Sector Bank (PSB)" and cite the statute.
- Foreign banks in branch mode are exempt from several Companies Act-linked governance provisions. Record the exemption in Column S.
- D-SIB surcharges and other systemic requirements apply only to banks notified as D-SIBs. Name the list date in Column S.
- RRBs file with NABARD (ENSURE) for several returns. Check the return owner in the supervisory-returns direction.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Write the Commercial Banks set first as the bank master; clone to SFB, PB, LAB and RRB (Appendix AB §AB.7.4, §AB.14). Wave W3.

### 4.1 Commercial Banks
- P1 · Reserve Bank of India (Commercial Banks – Asset Classification, Provisioning and Income Recognition) Directions, 2026 — RBI/DOR/2026-27/398 [VERIFY] [confirm reference on document], 27 Apr 2026
- P1 · Reserve Bank of India (Commercial Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/163 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Commercial Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/150 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/158 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/154 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/156 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/157 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/167 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/149 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/164 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/169 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/171 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Commercial Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/151 [confirm reference on document], 28 Nov 2025; updated as on 07 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/170 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Commercial Banks – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/408 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Concurrent Audit) Directions, 2026 — RBI/DoS/2026-27/409 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/410 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Digital Payment Security Controls) Directions, 2026 — RBI/DoS/2026-27/411 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/412 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/413 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/380 [VERIFY] [confirm reference on document], 14 Jan 2026
- P1 · Reserve Bank of India (Commercial Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/416 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/414 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Commercial Banks – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/415 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Commercial Banks – Acquisition and Holding of Shares or Voting Rights) Directions, 2025 — RBI/DOR/2025-26/145 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/147 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/162 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Climate Finance and Management of Climate Change Risks) Directions, 2025 — RBI/DOR/2025-26/172 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Credit Cards and Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/155 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/153 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/161 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Commercial Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/174 [confirm reference on document], 28 Nov 2025; updated as on 19 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Prudential Norms on Declaration of Dividend and Remittances of Profits) Directions, 2026 — RBI/DOR/2025-26/387 [VERIFY] [confirm reference on document], 10 Mar 2026
- P2 · Reserve Bank of India (Commercial Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/165 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Resource Raising Norms) Directions, 2025 — RBI/DOR/2025-26/152 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Commercial Banks – Securitisation Transactions) Directions, 2025 — RBI/DOR/2025-26/160 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Commercial Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/159 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Commercial Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/166 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Commercial Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/148 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Commercial Banks – Capital Charge for Credit Risk – Standardised Approach (effective 1 Apr 2027)) Directions, 2026 — RBI/DOR/2026-27/397 [VERIFY] [confirm reference on document], 27 Apr 2026
- P3 · Reserve Bank of India (Commercial Banks – Credit Valuation Adjustment Framework) Directions, 2026 — RBI/DOR/2026-27/474 [VERIFY] [confirm reference on document], 07 Oct 2026
- P3 · Reserve Bank of India (Commercial Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/380 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Commercial Banks – Forthcoming Instructions) Directions, 2025 — RBI/DOR/2025-26/173 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Commercial Banks – Minimum Capital Requirements for Market Risk) Directions, 2026 — RBI/DOR/2026-27/472 [VERIFY] [confirm reference on document], 21 Sep 2026
- P3 · Reserve Bank of India (Setting Up of Wholly Owned Subsidiaries by Foreign Banks) Guidelines, 2025 — RBI/DOR/2025-26/144 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P3 · Reserve Bank of India (Universal Banks – Licensing) Guidelines, 2025 — RBI/DOR/2025-26/143 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Commercial Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/146 [confirm reference on document], 28 Nov 2025

### 4.2 Small Finance Banks
- P1 · Reserve Bank of India (Small Finance Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/194 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Small Finance Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/181 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/189 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/185 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/187 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/188 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/198 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/180 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/195 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/200 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/202 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Small Finance Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/182 [confirm reference on document], 28 Nov 2025; updated as on 07 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/201 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Small Finance Banks – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/417 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Concurrent Audit) Directions, 2026 — RBI/DoS/2026-27/418 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/419 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Digital Payment Security Controls) Directions, 2026 — RBI/DoS/2026-27/420 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/421 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/422 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/381 [VERIFY] [confirm reference on document], 14 Jan 2026
- P1 · Reserve Bank of India (Small Finance Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/425 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/423 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Small Finance Banks – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/424 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Small Finance Banks – Acquisition and Holding of Shares or Voting Rights) Directions, 2025 — RBI/DOR/2025-26/176 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/178 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/193 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Climate Finance and Management of Climate Change Risks) Directions, 2025 — RBI/DOR/2025-26/203 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Credit Cards and Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/186 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/184 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/192 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Small Finance Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/204 [confirm reference on document], 28 Nov 2025; updated as on 19 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Prudential Norms on Declaration of Dividend) Directions, 2026 — RBI/DOR/2025-26/391 [VERIFY] [confirm reference on document], 10 Mar 2026
- P2 · Reserve Bank of India (Small Finance Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/196 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Resource Raising Norms) Directions, 2025 — RBI/DOR/2025-26/183 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Small Finance Banks – Securitisation Transactions) Directions, 2025 — RBI/DOR/2025-26/191 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Small Finance Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/190 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Small Finance Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/197 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Small Finance Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/179 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Small Finance Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/381 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Small Finance Banks – Licensing) Guidelines, 2025 — RBI/DOR/2025-26/175 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Small Finance Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/177 [confirm reference on document], 28 Nov 2025

### 4.3 Payments Banks
- P1 · Reserve Bank of India (Payments Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/215 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Payments Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/210 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/216 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/209 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/218 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/220 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Payments Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/211 [confirm reference on document], 28 Nov 2025; updated as on 07 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/219 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Payments Banks – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/426 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Concurrent Audit) Directions, 2026 — RBI/DoS/2026-27/427 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/428 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Digital Payment Security Controls) Directions, 2026 — RBI/DoS/2026-27/429 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/430 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/431 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Internal Ombudsman) Directions, 2026 — RBI/CEPD/2025-26/382 [VERIFY] [confirm reference on document], 14 Jan 2026
- P1 · Reserve Bank of India (Payments Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/434 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/432 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Payments Banks – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/433 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Payments Banks – Acquisition and Holding of Shares or Voting Rights) Directions, 2025 — RBI/DOR/2025-26/205 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/207 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/214 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/213 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/212 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/221 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Payments Banks – Prudential Norms on Declaration of Dividend) Directions, 2026 — RBI/DOR/2025-26/388 [VERIFY] [confirm reference on document], 10 Mar 2026
- P2 · Reserve Bank of India (Payments Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/208 [confirm reference on document], 28 Nov 2025; updated as on 05 Dec 2025 (RBI page)
- P3 · Reserve Bank of India (Payments Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/382 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Payments Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/206 [confirm reference on document], 28 Nov 2025

### 4.4 Local Area Banks
- P1 · Reserve Bank of India (Local Area Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/237 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Local Area Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/226 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/233 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Local Area Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/229 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/231 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/232 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/241 [confirm reference on document], 28 Nov 2025; updated as on 18 May 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/225 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/238 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/243 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/245 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Local Area Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/227 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Local Area Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/244 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Local Area Banks – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/444 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Concurrent Audit) Directions, 2026 — RBI/DoS/2026-27/445 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/446 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/447 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/450 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/448 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Local Area Banks – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/449 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Local Area Banks – Acquisition and Holding of Shares or Voting Rights) Directions, 2025 — RBI/DOR/2025-26/222 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/224 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/236 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/230 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/228 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/235 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Local Area Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/246 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Prudential Norms on Declaration of Dividend) Directions, 2026 — RBI/DOR/2025-26/389 [VERIFY] [confirm reference on document], 10 Mar 2026
- P2 · Reserve Bank of India (Local Area Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/239 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/234 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Local Area Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/240 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Local Area Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/383 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Local Area Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/223 [confirm reference on document], 28 Nov 2025

### 4.5 Regional Rural Banks
- P1 · Reserve Bank of India (Regional Rural Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/261 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Regional Rural Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/250 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/257 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Regional Rural Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/253 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/255 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/256 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/265 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/249 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Regional Rural Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/262 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/266 [confirm reference on document], 28 Nov 2025; updated as on 18 Sep 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/251 [confirm reference on document], 28 Nov 2025; updated as on 16 Jun 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/267 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Regional Rural Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/454 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Regional Rural Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/455 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Regional Rural Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/247 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/260 [confirm reference on document], 28 Nov 2025; updated as on 18 May 2026 (RBI page)
- P2 · Reserve Bank of India (Regional Rural Banks – Credit Cards and Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/254 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/252 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Regional Rural Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/259 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/268 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Prudential Norms on Declaration of Dividend) Directions, 2026 — RBI/DOR/2025-26/390 [VERIFY] [confirm reference on document], 10 Mar 2026
- P2 · Reserve Bank of India (Regional Rural Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/263 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Regional Rural Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/258 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/264 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Regional Rural Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/248 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Regional Rural Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/384 [confirm reference on document], 28 Nov 2025

### 4.6 Statutes and schemes read with the directions
- Banking Regulation Act, 1949 and RBI Act, 1934 provisions cited by each direction (cite the section in Column N, not as a separate sheet unless management asks)
- Reserve Bank – Integrated Ombudsman Scheme, 2026 (effective 1 Jul 2026) — one sheet per category (file "RBI-<CAT> - Integrated Ombudsman Scheme - Compliance Questions.xlsx")
- Deposit Insurance and Credit Guarantee Corporation Act, 1961 (premium, disclosure)

**Superseded (do not write):** the 2025 dividend directions of Commercial Banks (/168), SFBs (/199), Payments Banks (/217) and LABs (/242), replaced on 10 Mar 2026.

## 5. Family-specific pitfalls

- Mixing Basel III capital rows for commercial banks with SFB rows. SFB minimum capital and CRAR rules differ.
- Using repealed master circular paragraph numbers after the 2025 consolidation.
- Treating guidance in RBI FAQs as binding rows. Put it in Column L unless it states an obligation.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
