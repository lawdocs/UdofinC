# 16 — SEBI-INT Family Command: SEBI Market Intermediaries

**Template:** `templates/LDC-TPL-SEBI-INT-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-INT-v1.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_INT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Intermediary Group.** Column C holds the intermediary group (trading and clearing, depository, advisory and research, issue management and registry, portfolio and fund services, rating/trusteeship/custody, data and index services).

**Column D — Intermediary Type / CSCRF Category.** Column D names the intermediary type and, for cyber rows, the CSCRF category (Qualified, Mid-size, Small-size, Self-certification). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (SEBI_INT_Sector):**
- Trading and Clearing
- Depository Services
- Advisory and Research
- Issue Management and Registry
- Portfolio and Fund Services
- Rating, Trusteeship and Custody
- Data and Index Services
- All Intermediaries

**Column D (SEBI_INT_Entity):**
- Stock Broker
- Clearing Member
- Depository Participant
- Investment Adviser
- Research Analyst
- Portfolio Manager
- Merchant Banker
- Registrar to an Issue and Share Transfer Agent (RTA)
- Banker to an Issue
- Debenture Trustee
- Credit Rating Agency
- Custodian
- KYC Registration Agency (KRA)
- ESG Rating Provider
- Online Bond Platform Provider
- Vault Manager
- Index Provider
- CSCRF - Qualified RE
- CSCRF - Mid-size RE
- CSCRF - Small-size RE
- CSCRF - Self-certification RE
- All Intermediaries (ALL)

**Column H (SEBI_INT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (SEBI_INT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Client Onboarding & KYC, Surveillance, Investor Grievance, Internal Audit, Information Security. Family additions: Client Onboarding & KYC, Surveillance, Investor Grievance, Internal Audit, Information Security.

**Column O (SEBI_INT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (SEBI_INT_Risk):** High, Medium, Low.

**Column P reference list (SEBI_INT_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- Stock Exchanges (supervising MII)
- Depositories
- Clearing Corporations
- KRA / CKYCR
- BSE Administration & Supervision Ltd (BASL) - IA / RA
- FIU-IND (FINnet 2.0)
- CERT-In
- Board / Management
- Statutory / Internal Auditor
- Not Required

## 3. Applicability logic for this family

- Each intermediary has its own activity regulations and master circular. Write one sheet per regulation.
- CSCRF rows should go in CYBER unless the obligation is intermediary-specific. If they go here, use the CSCRF category values in Column D.
- IA/RA administration and supervision is delegated to BASL. Record the BASL filing route in Column P.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI Act, 1992 s.12; SEBI (Intermediaries) Regulations, 2008
- Activity regulations: Stock Brokers [VERIFY current regulations], Depositories and Participants 2018, Investment Advisers 2013, Research Analysts 2014, Portfolio Managers 2020, Merchant Bankers, RTA, Debenture Trustees, Credit Rating Agencies, Custodians, KRA [VERIFY]
- SEBI CSCRF (20 Aug 2024) and clarifications
- SEBI master circulars by intermediary type [VERIFY dates]

## 5. Family-specific pitfalls

- Using pre-2025 stock broker or merchant banker regulation references where SEBI has issued replacement regulations [VERIFY].

## 6. File naming

`SEBI-INT - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
