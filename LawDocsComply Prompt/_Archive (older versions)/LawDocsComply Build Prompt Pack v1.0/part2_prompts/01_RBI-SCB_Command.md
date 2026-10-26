# 01 — RBI-SCB Family Command: Commercial Banks, SFBs, Payments Banks, LABs and RRBs

**Template:** `templates/LDC-TPL-RBI-SCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-SCB-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_SCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

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

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Banking Regulation Act, 1949 (ss. 10A, 10B, 11, 12, 17, 18, 24, 26A, 29, 35A, 35B, 36AA, 45Y)
- RBI Act, 1934 (s.42 CRR and other applicable provisions)
- RBI (Commercial Banks – <topic>) Directions, 2025: 31 topic directions of 28 Nov 2025 (Governance, Capital Adequacy, IRACP, KYC, Credit Information Reporting, Managing Risks in Outsourcing, Responsible Business Conduct, Interest Rate on Deposits, Credit Facilities …) [VERIFY topic list]
- Corresponding direction sets of 28 Nov 2025 for SFBs (31), Payments Banks (18), Local Area Banks (26) and RRBs (23)
- RBI (Commercial Banks – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/415) and the SFB set (/424), 31 Jul 2026 [VERIFY numbers]; the 2024 Master Direction on Filing of Supervisory Returns is repealed
- RBI IT governance, risk, controls and assurance practices and cyber security framework for banks [VERIFY consolidation]
- Reserve Bank – Integrated Ombudsman Scheme, 2026 (effective 1 Jul 2026)
- Deposit Insurance and Credit Guarantee Corporation Act, 1961 (premium, disclosure)

## 5. Family-specific pitfalls

- Mixing Basel III capital rows for commercial banks with SFB rows. SFB minimum capital and CRAR rules differ.
- Using repealed master circular paragraph numbers after the 2025 consolidation.
- Treating guidance in RBI FAQs as binding rows. Put it in Column L unless it states an obligation.

## 6. File naming

`RBI-SCB - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
