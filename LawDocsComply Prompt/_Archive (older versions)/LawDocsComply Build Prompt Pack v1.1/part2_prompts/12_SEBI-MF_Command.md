# 12 — SEBI-MF Family Command: Mutual Funds (AMCs, Trustees, Schemes)

**Template:** `templates/LDC-TPL-SEBI-MF-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-MF-v1.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_MF_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Entity Role.** Column C holds the role that bears the obligation: AMC, trustees, sponsor, the scheme, or all MF entities.

**Column D — Scheme / Framework.** Column D holds the scheme category per SEBI's categorisation (equity, debt, hybrid, solution-oriented, index/ETF, FoF, close-ended/interval), plus newer frameworks (Specialised Investment Funds, MF Lite) [VERIFY current status]. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (SEBI_MF_Sector):**
- Asset Management Company (AMC)
- Trustee Company / Board of Trustees
- Sponsor
- Mutual Fund Scheme
- All MF Entities

**Column D (SEBI_MF_Entity):**
- Equity Scheme
- Debt Scheme
- Hybrid Scheme
- Solution-oriented Scheme
- Index Fund / ETF
- Fund of Funds
- Close-ended / Interval Scheme
- Specialized Investment Fund (SIF)
- Mutual Fund Lite (MF Lite - passive)
- Overseas Investment Scheme
- All Schemes (ALL)

**Column H (SEBI_MF_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (SEBI_MF_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Fund Management & Investments, Investor Services, Internal Audit, Information Security. Family additions: Fund Management & Investments, Investor Services, Internal Audit, Information Security.

**Column O (SEBI_MF_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Column R (SEBI_MF_Risk):** High, Medium, Low.

**Column P reference list (SEBI_MF_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- AMFI
- Stock Exchanges
- Depositories / RTA
- Trustees
- Unitholders (website / disclosure)
- FIU-IND (FINnet 2.0)
- CERT-In
- KRA / CKYCR
- Board of AMC
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Trustee obligations (reg. 18) and AMC obligations (reg. 25) are separate rows, even where they mirror each other.
- The SEBI Master Circular for Mutual Funds carries most operational requirements. Cite its paragraph numbers and date.
- CSCRF obligations for AMCs and RTAs belong in the CYBER family unless SEBI writes them into an MF circular.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Mutual Funds) Regulations, 2026 (notified 14 Jan 2026; in force 1 Apr 2026; replaced the 1996 Regulations — cite 1996 numbers only for periods before 1 Apr 2026)
- SEBI Master Circular for Mutual Funds [VERIFY latest date and whether re-issued under the 2026 Regulations]
- SEBI (Prohibition of Insider Trading) Regulations, 2015 (as applicable to AMCs; code of conduct for AMC staff)
- SEBI CSCRF (20 Aug 2024, as clarified)
- AMFI code and best-practice guidelines (Suggestive Compliance)

## 5. Family-specific pitfalls

- Citing superseded individual circulars that are now part of the master circular.
- Treating AMFI guidelines as binding unless SEBI mandates them.

## 6. File naming

`SEBI-MF - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
