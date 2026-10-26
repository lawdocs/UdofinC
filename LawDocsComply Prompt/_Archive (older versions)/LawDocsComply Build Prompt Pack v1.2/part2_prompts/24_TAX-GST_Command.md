# 24 — TAX-GST Family Command: GST, Income-tax, TDS/TCS and State Taxes

**Template:** `templates/LDC-TPL-TAX-GST-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-TAX-GST-v2.0` · **Regulator / authority:** CBIC / GSTN; CBDT; State tax departments · **Named-range prefix:** `TAX_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-TAX-GST-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Law.** General Applicability (Layer) holds the tax law (GST Acts; Income-tax Act, 2025; Income-tax Act, 1961 for earlier years; TDS/TCS; State PT; stamp duty).

**General Applicability (Type) — Taxpayer Type.** General Applicability (Type) holds the taxpayer type that changes obligations (regular, composition, ISD, GST TDS deductor, e-commerce operator, NRTP, OIDAR, financial institution with the rule 38 ITC option, SEZ, e-invoicing applicable, company, co-operative, LLP, tax-audit applicable). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (TAX_Sector):**
- CGST / SGST / IGST Acts, 2017
- Income-tax Act, 2025
- Income-tax Act, 1961 (transition / earlier years)
- TDS / TCS
- Professional Tax (State)
- Stamp Duty (State)
- All Tax Laws

**General Applicability (Type) (TAX_Entity):**
- Regular GST taxpayer
- Composition taxpayer
- Input Service Distributor (ISD)
- GST TDS deductor
- E-commerce operator (TCS)
- Non-resident taxable person
- OIDAR service provider
- Banking company / financial institution / NBFC (rule 38 ITC option)
- SEZ unit / developer
- E-invoicing applicable taxpayer
- Company assessee
- Co-operative society assessee
- LLP / Firm assessee
- Tax audit applicable
- All (ALL)

**Due Date & Frequency (TAX_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (TAX_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Tax, Accounts Payable, Billing & Receivables. Family additions: Tax, Accounts Payable, Billing & Receivables.

**Compliance Type (TAX_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (TAX_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (TAX_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- GSTN Portal (GSTR)
- E-invoice IRP
- E-way Bill Portal
- Income-tax e-Filing Portal
- TRACES (TDS / TCS)
- Protean (TIN)
- State Professional Tax Portal
- GST / Income-tax Authorities (notices / appeals)
- Tax Auditor (CA)
- Board / Management
- Not Required

## 3. Applicability logic for this family

- The Income-tax Act, 2025 applies from tax year 2026-27 (1 Apr 2026). Earlier years stay under the 1961 Act. Section and form numbers changed, so cite the new numbers [VERIFY].
- Banking companies, financial institutions and NBFCs may avail 50% ITC under rule 38 of the CGST Rules. Write this as a choice row.
- GST return due dates are set by notification and may be staggered by State. Put the rule in Due Date Rule *(v1.2)* and mark [VERIFY] where a notification changes it.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- CGST Act, 2017; IGST Act, 2017; CGST Rules, 2017 (incl. GST rate rationalisation of Sep 2025) [VERIFY]
- Income-tax Act, 2025 (in force from 1 Apr 2026) and Income-tax Rules [VERIFY form numbers]
- State Professional Tax Acts

## 5. Family-specific pitfalls

- Using 1961 Act section numbers for FY 2026-27 obligations.

## 6. File naming

`TAX-GST - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Tax Law | CGST / SGST / IGST · Income-tax Act, 2025 · Income-tax Act, 1961 · TDS / TCS · Professional Tax · Stamp Duty | Use where a sheet covers several tax laws. |
| Registration Type | Regular · Composition · ISD · TDS deductor (GST) · TCS collector (e-commerce) · Non-resident taxable person · OIDAR · Casual taxable person | The GST registration type the row applies to. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-TAX-GST-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Tax → GST returns / TDS returns / Income-tax returns / Tax audit; Accounts Payable → TDS deduction / ITC reconciliation; Billing & Receivables → E-invoicing / E-way bills. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Regulatory primary; add Legal for notices and appeals and Operational for e-invoicing systems. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the registered person furnished the monthly return in Form GSTR-3B and paid the tax due by the 20th day of the following month? |
| 4 | Clause / Para No. (`clause_ref`) | Section 39(1), CGST Act, 2017, read with Rule 61, CGST Rules, 2017 |
| 5 | Department (`department`) | Tax |
| 6 | Due Date & Frequency (`frequency`) | Monthly |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | CBIC |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Central Goods and Services Tax Act, 2017 |
| 12 | Instrument Reference No. (`instrument_ref`) | Act No. 12 of 2017 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 12-Apr-2017 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest Finance Act amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | Due date may be changed by notification; check before each month [VERIFY]. |
| 18 | Source Link (`source_url`) | https://cbic-gst.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | CGST / SGST / IGST Acts, 2017 |
| 20 | General Applicability (Type) (`applic_type`) | Regular GST taxpayer |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | QRMP taxpayers file quarterly (22nd / 24th by State) [VERIFY]; write as a separate row. |
| 22 | Applicable From (`applic_from`) | 01-Jul-2017 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Tax Law (`ext_*`) | CGST / SGST / IGST |
| E2 | Registration Type (`ext_*`) | Regular |
| 24 | Short Title (`short_title`) | GST returns - GSTR-3B monthly |
| 25 | Interpretation / Explanation (`explanation`) | GSTR-3B is the summary return and payment; late filing attracts late fee and interest and blocks later returns. (Abridged.) |
| 26 | Department Function (`dept_function`) | GST Compliance |
| 27 | Department Sub-function (`dept_subfunction`) | GSTR-3B |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | By the 20th day of the following month |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | GSTN Portal (GSTR) — GSTR-3B with payment |
| 32 | Portal / Form / Return Code (`filing_form`) | GSTR-3B |
| 33 | Related Document / Policy / Committee (`related_docs`) | ITC reconciliation with GSTR-2B |
| 34 | Reference Weblinks (`weblinks`) | https://www.gst.gov.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Late fee under s.47 and interest under s.50, CGST Act; blocking of e-way bills and later returns. |
| 36 | Penalty Provision (`penalty_ref`) | Sections 47 and 50, CGST Act, 2017 |
| 37 | Risk Type (`risk_type`) | Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | GSTR-3B ARN; challan / cash ledger debit; ITC reconciliation working |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Reconcile ITC with GSTR-2B. Compute liability, have the Tax Head approve, pay and file GSTR-3B by the 20th. Save the ARN. |
| 42 | Checker Review Points (`checker_points`) | 1. Filed by the 20th. 2. ITC claimed ≤ GSTR-2B eligible ITC. 3. Payment matches liability. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain ARNs for 12 months. 2. Compare filing dates. 3. Re-perform ITC reconciliation for one month. Exception: late filing or excess ITC. |
| 44 | Tags / Keywords (`tags`) | gstr-3b; gst return; section 39; monthly return |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

