# 20 — MCA-LLP Family Command: Limited Liability Partnerships

**Template:** `templates/LDC-TPL-MCA-LLP-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-MCA-LLP-v2.0` · **Regulator / authority:** Ministry of Corporate Affairs / Registrar of Companies · **Named-range prefix:** `MCA_LLP_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-MCA-LLP-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — LLP Class.** General Applicability (Layer) holds the LLP class (LLP, small LLP, foreign LLP).

**General Applicability (Type) — Threshold / Overlay.** General Applicability (Type) holds thresholds and overlays (audit threshold, FDI, converted LLPs, body-corporate partners). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (MCA_LLP_Sector):**
- Limited Liability Partnership (LLP)
- Small LLP
- Foreign LLP
- All LLPs

**General Applicability (Type) (MCA_LLP_Entity):**
- Turnover above ₹40 lakh or contribution above ₹25 lakh (audit required)
- LLP with foreign investment (FEMA)
- LLP converted from company / firm
- LLP with body corporate partners
- All LLPs (ALL)

**Due Date & Frequency (MCA_LLP_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (MCA_LLP_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Tax. Family additions: Secretarial, Tax.

**Compliance Type (MCA_LLP_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Risk Category (MCA_LLP_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (MCA_LLP_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- MCA (ROC) - LLP e-Form
- MCA - Regional Director
- NCLT
- RBI (FEMA) / AD Bank
- Income Tax Department
- Partners / Designated Partners
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- Annual filings: Form 11 (annual return, within 60 days of FY end) and Form 8 (statement of account and solvency, within 30 days of six months from FY end) [VERIFY].
- Register of partners and SBO rules were added by the 2022–2024 amendments [VERIFY].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Limited Liability Partnership Act, 2008 (as amended 2021)
- LLP Rules, 2009 (incl. 2022–2024 amendments: Register of Partners, Significant Beneficial Ownership) [VERIFY]
- FEMA (Non-debt Instruments) Rules, 2019 (LLPs with FDI)

## 5. Family-specific pitfalls

- Applying company Board-meeting rules to LLPs.

## 6. File naming

`MCA-LLP - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Small LLP | Small LLP · Not a small LLP | Use where small-LLP relaxations (lower fees, lighter penalties) apply. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-MCA-LLP-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Secretarial → Annual filings / Partner changes; Finance, Treasury and Accounts → Statement of Accounts / Audit; Tax → Income-tax returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Filings → Regulatory; partner and contribution rows → Governance. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the LLP filed its annual return in Form 11 with the Registrar within 60 days of the close of the financial year? |
| 4 | Clause / Para No. (`clause_ref`) | Section 35(1), LLP Act, 2008, read with Rule 25, LLP Rules, 2009 |
| 5 | Department (`department`) | Secretarial |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | MCA |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Limited Liability Partnership Act, 2008 |
| 12 | Instrument Reference No. (`instrument_ref`) | Act No. 6 of 2009 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 07-Jan-2009 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY — LLP (Amendment) Act, 2021] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.mca.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | All LLPs |
| 20 | General Applicability (Type) (`applic_type`) | All LLPs (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Small LLPs pay lower penalties under s.76A [VERIFY]. |
| 22 | Applicable From (`applic_from`) | 31-Mar-2009 [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Small LLP (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Annual return - Form 11 |
| 25 | Interpretation / Explanation (`explanation`) | Form 11 is due by 30 May each year and is filed even if the LLP had no business. (Abridged.) |
| 26 | Department Function (`dept_function`) | RoC Filings |
| 27 | Department Sub-function (`dept_subfunction`) | Annual return |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 60 days of the close of the financial year |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | MCA (ROC) - LLP e-Form — annual return |
| 32 | Portal / Form / Return Code (`filing_form`) | Form 11 |
| 33 | Related Document / Policy / Committee (`related_docs`) | Designated Partners |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Additional fees per day of delay; penalty under s.35 [VERIFY]. |
| 36 | Penalty Provision (`penalty_ref`) | Section 35(4), LLP Act, 2008 [VERIFY] |
| 37 | Risk Type (`risk_type`) | Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | SRN and challan for Form 11 |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Prepare Form 11 after the year end with partner and contribution details. Have a designated partner sign it digitally and file it by 30 May. Save the SRN. |
| 42 | Checker Review Points (`checker_points`) | 1. Filed on or before 30 May. 2. Partner details match records. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect Form 11 SRN. Exception: late filing. |
| 44 | Tags / Keywords (`tags`) | form 11; llp annual return; section 35 |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

