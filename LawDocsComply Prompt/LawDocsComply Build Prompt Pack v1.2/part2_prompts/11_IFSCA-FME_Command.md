# 11 — IFSCA-FME Family Command: IFSCA Fund Management Entities and Schemes

**Template:** `templates/LDC-TPL-IFSCA-FME-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-FME-v2.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_FME_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-IFSCA-FME-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — FME Category.** General Applicability (Layer) holds the FME registration category under reg. 3(4) of the FM Regulations 2025: Authorised FME, Registered FME (Non-Retail), Registered FME (Retail). Higher categories may undertake activities of lower ones.

**General Applicability (Type) — Scheme / Activity.** General Applicability (Type) holds the scheme or activity: Venture Capital Scheme, Restricted Scheme, Retail Scheme, ETF, Family Investment Fund, PMS (incl. multi-family office), Special Situation Fund, FoF/feeder, Investment Trusts (REIT/InvIT, private or public), co-investment/SPV, Pension Fund. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (IFSCA_FME_Sector):**
- Authorised FME
- Registered FME (Non-Retail)
- Registered FME (Retail)
- All FMEs

**General Applicability (Type) (IFSCA_FME_Entity):**
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

**Due Date & Frequency (IFSCA_FME_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (IFSCA_FME_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Investment Team, Valuation, Investor Relations, Internal Audit. Family additions: Investment Team, Valuation, Investor Relations, Internal Audit.

**Compliance Type (IFSCA_FME_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Disclosures. Family additions: Disclosures.

**Risk Category (IFSCA_FME_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (IFSCA_FME_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
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

- Obligations of the FME (net worth, KMP, infrastructure) and of each scheme (placement memorandum, investors, valuation, NAV, disclosures) must be separated. Use Type = "Fund Management Entity (FME)" for entity-level rows.
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

`IFSCA-FME - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Form of Set-up | Company · Branch · LLP · Trust | Use where the obligation differs by legal form (e.g., net-worth tests for a branch measured at parent level; LLP or trust structures for FMEs and schemes). |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-IFSCA-FME-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Governance & Administration → KMP and Principal Officer; Investment Team → Investment restrictions; Valuation → NAV / Valuation policy; Investor Relations → Disclosures to investors; Returns & Reporting → IFSCA returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Investor-facing → Conduct & Consumer; valuation → Market; Model & AI where models are used; KMP → Governance. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the FME appointed a Principal Officer and a Compliance Officer who meet the qualification and experience requirements for its registration category? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation [VERIFY], IFSCA (Fund Management) Regulations, 2025 |
| 5 | Department (`department`) | Governance & Administration |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | IFSCA |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | International Financial Services Centres Authority (Fund Management) Regulations, 2025 |
| 12 | Instrument Reference No. (`instrument_ref`) | IFSCA/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | [VERIFY] instrument dates; the 2025 Regulations replaced the 2022 Regulations [VERIFY]. |
| 18 | Source Link (`source_url`) | https://www.ifsca.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | All FMEs |
| 20 | General Applicability (Type) (`applic_type`) | Fund Management Entity (FME) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Qualification and experience vary by category (Authorised / Registered Non-Retail / Registered Retail) [VERIFY]. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Form of Set-up (`ext_*`) | Company; LLP |
| 24 | Short Title (`short_title`) | KMP - Principal Officer and Compliance Officer |
| 25 | Interpretation / Explanation (`explanation`) | Both officers must be based in the IFSC and meet the qualification and experience tests; the Compliance Officer cannot hold investment responsibilities [VERIFY]. (Abridged.) |
| 26 | Department Function (`dept_function`) | KMP and Officers |
| 27 | Department Sub-function (`dept_subfunction`) | Appointment of KMP |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within [VERIFY] days of the vacancy |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Cessation or resignation of director / KMP / officer |
| 31 | Filing / Reporting / Intimation (`filing_details`) | IFSCA (intimation) — change in KMP [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Board; Compliance Policy |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the FM Regulations; IFSCA may impose a penalty or restrict business under the IFSCA Act [VERIFY]. |
| 36 | Penalty Provision (`penalty_ref`) | [VERIFY] |
| 37 | Risk Type (`risk_type`) | Governance; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board resolution; qualification and experience proofs; IFSCA intimation acknowledgement |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Before appointing, check the candidate against the qualification and experience tests for the FME's category. Obtain Board approval, intimate IFSCA and file the proofs. |
| 42 | Checker Review Points (`checker_points`) | 1. Qualification and experience proofs match the category test. 2. Officer is based in the IFSC. 3. IFSCA intimation made in time. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect appointment file and IFSCA intimation. Exception: unqualified officer or late intimation. |
| 44 | Tags / Keywords (`tags`) | principal officer; compliance officer; fme; kmp; ifsca |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

