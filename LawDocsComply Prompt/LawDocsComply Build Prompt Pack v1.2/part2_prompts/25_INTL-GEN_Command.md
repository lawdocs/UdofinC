# 25 — INTL-GEN Family Command: International Jurisdictions *(v1.1)*

**Template:** `templates/LDC-TPL-INTL-GEN-v2.0 - International Jurisdictions.xlsx` · **Template code:** `LDC-TPL-INTL-GEN-v2.0` · **Regulator / authority:** foreign authorities by jurisdiction · **Named-range prefix:** `INTL_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. **International content is never written from secondary sources alone:** every sheet needs a named in-country reviewer (law firm or licensed professional) recorded in Related Document / Policy / Committee as `REVIEWER: <firm>, <city>, <date>` before upload (Appendix Y §Y.4.6 and §Y.5; proposed rule NN-53).

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-INTL-GEN-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Jurisdiction.** The country, sub-national unit (US state, Canadian province) or special zone (DIFC, ADGM, QFC) whose law creates the obligation. Use "European Union (supranational)" only for directly applicable EU regulations (GDPR, DORA, AI Act); national transpositions of directives (NIS2) go under the member state. Several jurisdictions may be typed separated by "; " only where the text of the obligation is genuinely identical (for example, an EU regulation applying in several member states).

**General Applicability (Type) — Entity form.** The legal form or regulated status to which the obligation applies. Use "Subsidiary of an Indian parent (ODI)" for obligations that arise only because the parent is Indian (for example, information the subsidiary must supply for the parent's Annual Performance Report under India's overseas investment framework). Use "Group parent (consolidated obligations)" for group-level filings (consolidated accounts, group registers). Several forms are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (INTL_Sector):**
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

**General Applicability (Type) (INTL_Entity):**
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

**Due Date & Frequency (INTL_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (INTL_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Tax, Privacy Office (DPO), Information Security, KYC & AML, Payroll. Family additions: Secretarial, Tax, Privacy Office (DPO), Information Security, KYC & AML, Payroll (all mapped to canonical codes in Appendix U §U.9.0).

**Compliance Type (INTL_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Licences & Registrations. Family additions: Licences & Registrations.

**Risk Category (INTL_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (INTL_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
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

- **Local law first, Indian overlay second.** Write the foreign obligation as the foreign law states it. Where an Indian rule also applies to the same subsidiary (FEMA ODI reporting, Indian parent's consolidation under Ind AS 110, RBI approval for an NBFC's overseas investment), write it in the Indian family sheet and cross-reference it in Related Document / Policy / Committee as `INDIA-LINK: <template code> / <instrument>`.
- **Language.** Where the official text is not in English (e.g., German, French, Arabic, Japanese, Portuguese, Mandarin), quote the official-language words that define the duty in Interpretation / Explanation in quotation marks, followed by the English translation and the translation source (`TRANSLATION: official / partner / machine-reviewed`). Never cite a machine translation as the law (Appendix Y §Y.4.4).
- **Sub-national law.** US state, Canadian province, Australian state, Swiss canton, German Land and Indian-style state rules are separate rows with the sub-national unit in General Applicability (Layer).
- **Free zones.** DIFC, ADGM and QFC have their own company, employment and data laws distinct from the federal/mainland regime. Never merge them.
- **Due dates.** Put the exact rule in Due Date Rule *(v1.2: was Column P after "Due:")* using the jurisdiction's own anchor (e.g., "Within 14 days after the end of each review period", "By the anniversary of incorporation", "Within 9 months after the end of the financial year"). The importer computes the date with the jurisdiction's holiday calendar and time zone (P25).
- **Thresholds and exemptions** (small company audit exemptions, dormant company relief, de minimis tax registration thresholds) go in Conditional Applicability / Exemptions / Thresholds with the currency in ISO code (GBP, SGD, AED, USD, EUR).
- **Currency in Consequences of Non-Compliance / Penalty.** Penalties in local currency with ISO code; do not convert to INR.

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
- Citing secondary sources (law-firm notes, vendor blogs) as the source; they may be used to find the law, never as the citation in Clause / Para No..
- Using English convenience translations without stating so.
- Leaving out the in-country reviewer line (REVIEWER: token) in Related Document / Policy / Committee.

## 6. File naming

`INTL-GEN - <ISO country code> - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (e.g., `INTL-GEN - GB - Companies Act 2006 Annual Cycle 2026 - Compliance Questions v2.xlsx`; revisions add ` (rev N)`; for sub-national units add the subdivision code, e.g., `US-DE`). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Country | <ISO 3166-1 country, as in `Lists`> | The country of the law (use with General Applicability (Layer) where Layer names a zone such as DIFC). |
| Sub-national Unit | <ISO 3166-2 subdivision, e.g. US-DE, CA-ON> | Use for state / provincial law. |
| Official Language | <language of the official text> | The language of the authoritative text; quote defining words in that language in Interpretation / Explanation. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-INTL-GEN-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Secretarial → Registry filings / Registers; Tax → Corporate tax / VAT; Privacy Office (DPO) → Local privacy law; Payroll → Social security; KYC & AML → Local AML. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Regulatory primary; add Legal for local-law filings and Data Privacy / People where relevant. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the company delivered its confirmation statement to Companies House within 14 days after the end of each review period? |
| 4 | Clause / Para No. (`clause_ref`) | Section 853A, Companies Act 2006 (UK) |
| 5 | Department (`department`) | Secretarial |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | Companies House (UK) |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Companies Act 2006 (UK) |
| 12 | Instrument Reference No. (`instrument_ref`) | 2006 c. 46 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 08-Nov-2006 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY — Economic Crime and Corporate Transparency Act 2023 changes] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Amended |
| 17 | Change Note / Previous Actionable (`change_note`) | Confirmation statement contents expanded by the Economic Crime and Corporate Transparency Act 2023 (lawful-purpose statement, registered e-mail) [VERIFY commencement]. |
| 18 | Source Link (`source_url`) | https://www.legislation.gov.uk/ukpga/2006/46/section/853A |
| 19 | General Applicability (Layer) (`applic_layer`) | United Kingdom |
| 20 | General Applicability (Type) (`applic_type`) | Private company limited by shares; Subsidiary of an Indian parent (ODI) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to every UK company. Review period is 12 months from incorporation or the last statement. |
| 22 | Applicable From (`applic_from`) | 30-Jun-2016 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Country (`ext_*`) | United Kingdom (GB) |
| E2 | Sub-national Unit (`ext_*`) | (blank — not a deciding factor here) |
| E3 | Official Language (`ext_*`) | English |
| 24 | Short Title (`short_title`) | Annual filings - confirmation statement |
| 25 | Interpretation / Explanation (`explanation`) | The statement confirms that the information on the register is up to date and delivers any changes. Filing late is an offence by the company and every officer in default. (Abridged.) |
| 26 | Department Function (`dept_function`) | Registry Filings |
| 27 | Department Sub-function (`dept_subfunction`) | Confirmation statement |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 14 days after the end of each review period |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Company Registry (e.g., Companies House, ACRA, Registrar of Companies) — confirmation statement |
| 32 | Portal / Form / Return Code (`filing_form`) | CS01 |
| 33 | Related Document / Policy / Committee (`related_docs`) | REVIEWER: <in-country reviewer>; Register of members; PSC register |
| 34 | Reference Weblinks (`weblinks`) | https://www.gov.uk/government/organisations/companies-house |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Offence under s.853L; risk of strike-off. |
| 36 | Penalty Provision (`penalty_ref`) | Section 853L, Companies Act 2006 (UK) |
| 37 | Risk Type (`risk_type`) | Regulatory; Legal |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Companies House filing confirmation for CS01 |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Diary the review-period end date. Confirm officers, PSCs, shareholders and SIC codes. File CS01 within 14 days and save the confirmation. |
| 42 | Checker Review Points (`checker_points`) | 1. Filed within 14 days of the review-period end. 2. PSC and officer details match the registers. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect the Companies House filing history. Exception: late filing. |
| 44 | Tags / Keywords (`tags`) | confirmation statement; companies house; cs01; uk |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

