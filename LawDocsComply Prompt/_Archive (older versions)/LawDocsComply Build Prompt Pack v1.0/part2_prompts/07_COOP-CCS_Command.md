# 07 — COOP-CCS Family Command: Credit Co-operative Societies (multi-State, State, PACS)

**Template:** `templates/LDC-TPL-COOP-CCS-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-COOP-CCS-v1.0` · **Regulator / authority:** Central Registrar (MSCS Act, 2002) / State Registrars of Co-operative Societies · **Named-range prefix:** `COOP_CCS_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Registration Law.** Column C records the registration law, which decides the regulator: multi-State societies under the MSCS Act 2002 (Central Registrar), State societies under the State Act (State Registrar), mutually aided co-operatives under State MACS Acts, and PACS (State Act, with Ministry of Cooperation model bye-laws).

**Column D — Society Type.** Column D records the society type: urban/nagari credit society (patsanstha), employees' or salary-earners' credit society, thrift and credit society, PACS, LAMPS, FSS, women's credit society, and societies above the concurrent-audit threshold. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (COOP_CCS_Sector):**
- Multi-State Credit Co-operative Society (MSCS Act, 2002)
- State Credit Co-operative Society (State Co-operative Societies Act)
- Mutually Aided / Self-reliant Co-operative (State MACS Act)
- Primary Agricultural Credit Society (PACS)
- All Credit Co-operative Societies

**Column D (COOP_CCS_Entity):**
- Urban / Nagari Credit Co-operative Society (Patsanstha)
- Employees' / Salary Earners' Credit Co-operative Society
- Thrift and Credit Co-operative Society
- Primary Agricultural Credit Society (PACS)
- Large-sized Adivasi Multipurpose Society (LAMPS)
- Farmers' Service Society (FSS)
- Multi-State Credit Co-operative Society
- Women's Credit Co-operative Society
- Society subject to concurrent audit (State Act threshold)
- All (ALL)

**Column H (COOP_CCS_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (COOP_CCS_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit & Recovery, Membership & Elections, Audit, Member Services & Grievance. Family additions: Credit & Recovery, Membership & Elections, Audit, Member Services & Grievance.

**Column O (COOP_CCS_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Column R (COOP_CCS_Risk):** High, Medium, Low.

**Column P reference list (COOP_CCS_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Central Registrar of Co-operative Societies (CRCS Portal)
- Registrar of Co-operative Societies (State)
- Co-operative Election Authority (MSCS)
- State Co-operative Election Commission / Authority
- Co-operative Ombudsman (MSCS)
- Statutory Auditor (Panel)
- Department / Government Auditor
- General Body / Members
- Board of Directors / Committee of Management
- FIU-IND (FINnet 2.0)
- Income Tax / GST Authorities
- Credit Information Companies (CICs)
- NABARD (PACS)
- Not Required

## 3. Applicability logic for this family

- First decide the governing statute. A society operating in more than one State is a multi-State society under the MSCS Act. Otherwise the State Act of the registration State applies. Write one sheet per Act and per State. State Acts differ (for example Maharashtra 1960, Uttar Pradesh 1965, Rajasthan 2001, Gujarat 1961, Karnataka 1959, Delhi 2003).
- Credit societies may accept deposits only from members and may not use the words "bank", "banker" or "banking" (BR Act s.7) [VERIFY State-specific deposit rules].
- The 2023 MSCS amendments introduced the Co-operative Election Authority, the Co-operative Ombudsman, the Co-operative Rehabilitation, Reconstruction and Development Fund, board composition requirements (seats for women and SC/ST), concurrent audit above a turnover/deposit threshold, and information-officer duties. Write each as its own rows [VERIFY section numbers].
- Loan operations (sanction, interest, recovery) are run in Finbyx. Write the regulatory obligations here (lending limits, member-only lending, recovery under the Act, audit classification).

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Multi-State Co-operative Societies Act, 2002 as amended by the MSCS (Amendment) Act, 2023 (Act 11 of 2023); MSCS Rules, 2002 as amended 2023 [VERIFY]
- State Co-operative Societies Acts and Rules of the selected State (e.g., Maharashtra 1960, Uttar Pradesh 1965, Rajasthan 2001, Delhi 2003, Gujarat 1961, Karnataka 1959)
- Model bye-laws for PACS (Ministry of Cooperation) [VERIFY]
- Banking Regulation Act, 1949 s.7 and s.56 (prohibition on use of the word "bank")
- PMLA, 2002 (where the society is a reporting entity) [VERIFY applicability]
- Income-tax Act, 2025 provisions on co-operative societies [VERIFY]

## 5. Family-specific pitfalls

- Writing RBI UCB rules for a credit society. A credit society is not a bank.
- Mixing two States' Acts in one sheet.
- Missing election-cycle rows (board term of five years, election before expiry).

## 6. File naming

`COOP-CCS - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
