# 25 — INTL-GEN Family Command: International Jurisdictions *(v1.1)*

**Template:** `templates/LDC-TPL-INTL-GEN-v1.0 - International Jurisdictions.xlsx` · **Template code:** `LDC-TPL-INTL-GEN-v1.0` · **Regulator / authority:** foreign authorities by jurisdiction · **Named-range prefix:** `INTL_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. **International content is never written from secondary sources alone:** every sheet needs a named in-country reviewer (law firm or licensed professional) recorded in Column N as `REVIEWER: <firm>, <city>, <date>` before upload (Appendix Y §Y.4.6 and §Y.5; proposed rule NN-53).

## 1. How Columns C and D work in this family

**Column C — Jurisdiction.** The country, sub-national unit (US state, Canadian province) or special zone (DIFC, ADGM, QFC) whose law creates the obligation. Use "European Union (supranational)" only for directly applicable EU regulations (GDPR, DORA, AI Act); national transpositions of directives (NIS2) go under the member state. Several jurisdictions may be typed separated by "; " only where the text of the obligation is genuinely identical (for example, an EU regulation applying in several member states).

**Column D — Entity form.** The legal form or regulated status to which the obligation applies. Use "Subsidiary of an Indian parent (ODI)" for obligations that arise only because the parent is Indian (for example, information the subsidiary must supply for the parent's Annual Performance Report under India's overseas investment framework). Use "Group parent (consolidated obligations)" for group-level filings (consolidated accounts, group registers). Several forms are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (INTL_Sector):**
- United Arab Emirates - Mainland (Federal)
- United Arab Emirates - DIFC
- United Arab Emirates - ADGM
- Saudi Arabia
- Qatar (incl. QFC)
- Bahrain
- Oman
- Kuwait
- Singapore
- Hong Kong SAR
- Malaysia
- Indonesia
- Thailand
- Vietnam
- Philippines
- Japan
- South Korea
- China (Mainland)
- Australia
- New Zealand
- Sri Lanka
- Bangladesh
- Nepal
- Mauritius
- Kenya
- Nigeria
- South Africa
- Egypt
- United Kingdom
- Ireland
- Netherlands
- Germany
- France
- Luxembourg
- Switzerland
- Cyprus
- Spain
- Italy
- Belgium
- Poland
- European Union (supranational)
- United States - Federal
- United States - Delaware
- United States - New York
- United States - California
- United States - Texas
- Canada - Federal
- Canada - Ontario
- Mexico
- Brazil
- Other jurisdiction
- All jurisdictions (ALL)

**Column D (INTL_Entity):**
- Private company limited by shares
- Public company (unlisted)
- Listed company
- Branch of a foreign company
- Representative / liaison office
- Limited liability partnership (LLP)
- Partnership
- Limited Liability Company (LLC)
- Corporation (C-Corp / S-Corp)
- Free zone company (FZCO / FZ-LLC / FZE)
- Civil-law company (GmbH / AG / SARL / SAS / BV / NV / SpA)
- Bank / deposit-taking institution
- Non-bank lender / finance company
- Investment fund / fund manager
- Insurance entity
- Payment / e-money institution
- Holding company / SPV
- Non-profit / foundation / charity
- Group parent (consolidated obligations)
- Subsidiary of an Indian parent (ODI)
- All entity forms (ALL)

**Column H (INTL_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (INTL_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Tax, Privacy Office (DPO), Information Security, KYC & AML, Payroll. Family additions: Secretarial, Tax, Privacy Office (DPO), Information Security, KYC & AML, Payroll (all mapped to canonical codes in Appendix U §U.9.0).

**Column O (INTL_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Licences & Registrations. Family additions: Licences & Registrations.

**Column R (INTL_Risk):** High, Medium, Low.

**Column P reference list (INTL_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Company Registry (e.g., Companies House, ACRA, Registrar of Companies)
- Tax Authority (corporate income tax)
- Tax Authority (VAT / GST / sales tax)
- Financial Regulator / Central Bank
- Securities Regulator / Stock Exchange
- Data Protection Authority
- Labour / Social Security Authority
- Beneficial Ownership Register
- Financial Intelligence Unit (AML)
- Statistics / Foreign Investment Reporting
- Registered Agent / Corporate Service Provider
- Local Statutory Auditor
- Parent reporting - India (RBI ODI / FEMA, e.g., APR)
- Board / Management
- Not Required

## 3. Applicability logic for this family

- **Local law first, Indian overlay second.** Write the foreign obligation as the foreign law states it. Where an Indian rule also applies to the same subsidiary (FEMA ODI reporting, Indian parent's consolidation under Ind AS 110, RBI approval for an NBFC's overseas investment), write it in the Indian family sheet and cross-reference it in Column N as `INDIA-LINK: <template code> / <instrument>`.
- **Language.** Where the official text is not in English (e.g., German, French, Arabic, Japanese, Portuguese, Mandarin), quote the official-language words that define the duty in Column L in quotation marks, followed by the English translation and the translation source (`TRANSLATION: official / partner / machine-reviewed`). Never cite a machine translation as the law (Appendix Y §Y.4.4).
- **Sub-national law.** US state, Canadian province, Australian state, Swiss canton, German Land and Indian-style state rules are separate rows with the sub-national unit in Column C.
- **Free zones.** DIFC, ADGM and QFC have their own company, employment and data laws distinct from the federal/mainland regime. Never merge them.
- **Due dates.** Put the exact rule in Column P after "Due:" using the jurisdiction's own anchor (e.g., "Due: within 14 days after the end of each review period", "Due: by the anniversary of incorporation", "Due: 9 months after financial year end"). The importer computes the date with the jurisdiction's holiday calendar and time zone (P25).
- **Thresholds and exemptions** (small company audit exemptions, dormant company relief, de minimis tax registration thresholds) go in Column S with the currency in ISO code (GBP, SGD, AED, USD, EUR).
- **Currency in Column Q.** Penalties in local currency with ISO code; do not convert to INR.

## 4. Instruments to cover first (priority corridors; verify current versions)

- United Kingdom: Companies Act 2006 (confirmation statement s.853A; PSC register Part 21A; accounts filing ss.441-442); Economic Crime and Corporate Transparency Act 2023 (identity verification) [VERIFY commencement dates]
- Singapore: Companies Act 1967 (annual return s.197; Register of Registrable Controllers); Income Tax Act 1947; PDPA 2012
- United Arab Emirates: Federal Decree-Law No. 32 of 2021 on Commercial Companies; Cabinet Decision No. 109 of 2023 (beneficial owner); Federal Decree-Law No. 45 of 2021 (PDPL); DIFC Data Protection Law No. 5 of 2020 as amended 2025; ADGM Data Protection Regulations 2021
- European Union: GDPR (Regulation (EU) 2016/679); DORA (Regulation (EU) 2022/2554); NIS2 (Directive (EU) 2022/2555); EU AI Act (Regulation (EU) 2024/1689) [VERIFY national transposition]
- United States: Delaware General Corporation Law (annual franchise tax report); Corporate Transparency Act BOI reporting (scope narrowed by the 2025 interim final rule) [VERIFY]; state privacy laws (e.g., CCPA/CPRA)
- India (parent side): FEMA (Overseas Investment) Rules and Regulations, 2022 and RBI Master Direction on Overseas Investment - Annual Performance Report for each overseas entity [VERIFY current para]
- Corridor packs (Appendix Y §Y.10): UAE (mainland, DIFC, ADGM), Singapore, United Kingdom, United States (Delaware + California + New York), Saudi Arabia, Netherlands/Ireland/Germany (EU holding and services entities), Mauritius, Kenya/Nigeria/South Africa.
- For every corridor: company law annual cycle (annual return / confirmation statement, accounts filing, AGM or written resolutions, registers, beneficial ownership), corporate tax and indirect tax registration and returns, payroll/social security, data protection, AML (where regulated), licences, economic substance (where still in force [VERIFY]), and sectoral financial regulation for regulated subsidiaries.

## 5. Family-specific pitfalls

- Writing Indian concepts into foreign rows (for example "DIN", "ROC", "MCA") — use the local equivalents (director identification / identity verification, Companies House / ACRA / Registrar, etc.).
- Treating an EU directive as directly applicable; cite the national transposing law.
- Mixing UAE federal, DIFC and ADGM regimes.
- Assuming a US federal obligation applies uniformly; most company-law and privacy obligations are state-level.
- Citing secondary sources (law-firm notes, vendor blogs) as the source; they may be used to find the law, never as the citation in Column K.
- Using English convenience translations without stating so.
- Leaving out the in-country reviewer line in Column N.

## 6. File naming

`INTL-GEN - <ISO country code> - <Instrument short title> <Year>.xlsx` (e.g., `INTL-GEN - GB - Companies Act 2006 Annual Cycle 2026.xlsx`; for sub-national units add the subdivision code, e.g., `US-DE`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
