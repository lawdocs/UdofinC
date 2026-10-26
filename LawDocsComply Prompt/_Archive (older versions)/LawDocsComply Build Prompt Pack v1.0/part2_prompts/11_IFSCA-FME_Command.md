# 11 — IFSCA-FME Family Command: IFSCA Fund Management Entities and Schemes

**Template:** `templates/LDC-TPL-IFSCA-FME-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-FME-v1.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_FME_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — FME Category.** Column C holds the FME registration category under reg. 3(4) of the FM Regulations 2025: Authorised FME, Registered FME (Non-Retail), Registered FME (Retail). Higher categories may undertake activities of lower ones.

**Column D — Scheme / Activity.** Column D holds the scheme or activity: Venture Capital Scheme, Restricted Scheme, Retail Scheme, ETF, Family Investment Fund, PMS (incl. multi-family office), Special Situation Fund, FoF/feeder, Investment Trusts (REIT/InvIT, private or public), co-investment/SPV, Pension Fund. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (IFSCA_FME_Sector):**
- Authorised FME
- Registered FME (Non-Retail)
- Registered FME (Retail)
- All FMEs

**Column D (IFSCA_FME_Entity):**
- Fund Management Entity (FME)
- Venture Capital Scheme
- Restricted Scheme (Non-Retail)
- Retail Scheme
- Exchange Traded Fund (ETF)
- Family Investment Fund (FIF)
- Portfolio Management Services (PMS) incl. Multi-family Office
- Special Situation Fund
- Fund of Funds / Feeder Scheme
- Investment Trust - REIT (Private / Public)
- Investment Trust - InvIT (Private / Public)
- Co-investment / SPV / Segregated Portfolio
- Pension Fund (PENF)
- All FMEs and Schemes (ALL)

**Column H (IFSCA_FME_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (IFSCA_FME_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Investment Team, Valuation, Investor Relations, Internal Audit. Family additions: Investment Team, Valuation, Investor Relations, Internal Audit.

**Column O (IFSCA_FME_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Column R (IFSCA_FME_Risk):** High, Medium, Low.

**Column P reference list (IFSCA_FME_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- IFSCA
- IFSCA (prior approval)
- IFSCA (intimation)
- IFSCA / FIU-IND
- Home country regulator (NOC)
- MCA
- RBI (FEMA)
- Central Registry (CERSAI)
- Recognised Stock Exchange (IFSC)
- Custodian / Depository
- Investors (disclosure)
- Management
- Not Required

## 3. Applicability logic for this family

- Obligations of the FME (net worth, KMP, infrastructure) and of each scheme (placement memorandum, investors, valuation, NAV, disclosures) must be separated. Use D = "Fund Management Entity (FME)" for entity-level rows.
- Use the "as amended up to 10 September 2026" consolidated text.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- IFSCA (Fund Management) Regulations, 2025 (as amended up to 10 Sep 2026)
- IFSCA Guidelines on KMP Eligibility (25 Jul 2025)
- IFSCA (Pension Fund) Regulations, 2026
- IFSCA (AML, CFT and KYC) Guidelines, 2022

## 5. Family-specific pitfalls

- Applying retail-scheme investor protections to restricted schemes.
- Missing the USD 1 billion AUM trigger for additional KMP.

## 6. File naming

`IFSCA-FME - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
