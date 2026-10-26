# 13 — SEBI-AIF Family Command: Alternative Investment Funds

**Template:** `templates/LDC-TPL-SEBI-AIF-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-AIF-v1.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_AIF_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Entity Role.** Column C holds the role: the AIF or scheme, the manager, the sponsor or the trustee.

**Column D — AIF Category.** Column D holds the AIF category and sub-category: Category I (VCF, angel, SME, social impact, infrastructure, special situation), Category II, Category III, LVF for accredited investors, accredited-investor-only schemes, co-investment schemes [VERIFY]. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (SEBI_AIF_Sector):**
- AIF / Scheme
- Manager
- Sponsor
- Trustee
- All AIF Entities

**Column D (SEBI_AIF_Entity):**
- Category I - Venture Capital Fund
- Category I - Angel Fund
- Category I - SME Fund
- Category I - Social Impact Fund
- Category I - Infrastructure Fund
- Category I - Special Situation Fund
- Category II AIF
- Category III AIF
- Large Value Fund for Accredited Investors (LVF)
- Scheme for Accredited Investors only
- Co-investment Scheme (CIV)
- All AIFs (ALL)

**Column H (SEBI_AIF_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (SEBI_AIF_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Investment Team, Valuation, Investor Relations, Internal Audit. Family additions: Investment Team, Valuation, Investor Relations, Internal Audit.

**Column O (SEBI_AIF_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Column R (SEBI_AIF_Risk):** High, Medium, Low.

**Column P reference list (SEBI_AIF_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- Custodian
- Depositories (demat of units)
- Investors (disclosure / PPM)
- Performance Benchmarking Agency
- FIU-IND (FINnet 2.0)
- CERT-In
- Board / Investment Committee
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Many conditions differ by category (leverage, concentration, tenure, continuing interest of the sponsor/manager). Write separate rows per category.
- PPM audit, valuation, performance benchmarking and dematerialisation of units are master-circular obligations. Cite the master circular paragraph.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI (Alternative Investment Funds) Regulations, 2012 (as amended)
- SEBI Master Circular for AIFs [VERIFY latest date]
- SEBI CSCRF as applicable to AIF managers

## 5. Family-specific pitfalls

- Writing Category III leverage rules for Category I/II.
- Missing accredited-investor and LVF relaxations.

## 6. File naming

`SEBI-AIF - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
