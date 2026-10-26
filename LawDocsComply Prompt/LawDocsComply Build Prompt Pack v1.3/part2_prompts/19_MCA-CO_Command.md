# 19 — MCA-CO Family Command: Companies (Companies Act, 2013)

**Template:** `templates/LDC-TPL-MCA-CO-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-MCA-CO-v2.0` · **Regulator / authority:** Ministry of Corporate Affairs / Registrar of Companies · **Named-range prefix:** `MCA_CO_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-MCA-CO-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Company Class.** General Applicability (Layer) holds the company class. Many provisions differ for private, OPC, small, Section 8, producer, Nidhi and government companies through exemption notifications (for example the 5 June 2015 notifications for private and government companies). Use the class value and record the exemption in Conditional Applicability / Exemptions / Thresholds.

**General Applicability (Type) — Threshold / Overlay.** General Applicability (Type) holds thresholds and overlays that switch obligations on: paid-up capital, turnover and borrowing thresholds (s.149, s.177, s.178, s.203, s.204), CSR thresholds (s.135(1)), deposits, foreign investment, dormant status. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (MCA_CO_Sector):**
- Private Limited Company
- Public Limited Company (Unlisted)
- Public Limited Company (Listed)
- One Person Company (OPC)
- Small Company
- Section 8 Company
- Producer Company
- Nidhi Company
- Government Company
- Foreign Company
- All Companies

**General Applicability (Type) (MCA_CO_Entity):**
- Paid-up capital ≥ ₹10 crore
- Turnover ≥ ₹100 crore
- Outstanding borrowings/deposits ≥ ₹50 crore
- CSR applicable (s.135(1) thresholds)
- Ind AS applicable
- Holding / Subsidiary company
- Company accepting deposits (Chapter V)
- Company with foreign investment (FEMA)
- Dormant company (s.455)
- Start-up (DPIIT recognised)
- Company required to appoint KMP (s.203)
- Company requiring secretarial audit (s.204)
- Company requiring cost audit (s.148)
- All Companies (ALL)

**Due Date & Frequency (MCA_CO_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (MCA_CO_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Secretarial, Internal Audit, Tax. Family additions: Secretarial, Internal Audit, Tax.

**Compliance Type (MCA_CO_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Risk Category (MCA_CO_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (MCA_CO_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- MCA (ROC) - e-Form
- MCA - Regional Director
- NCLT
- IEPF Authority
- Central Government (MCA)
- RBI (FEMA) / AD Bank
- SEBI / Stock Exchanges (listed)
- Income Tax Department
- Members (general meeting / website)
- Board / Management
- Statutory Auditor
- Secretarial Auditor / PCS
- Cost Auditor
- Not Required

## 3. Applicability logic for this family

- Write one sheet per Chapter or Rule set (Meetings of Board; Management and Administration; Accounts; Audit and Auditors; Appointment of Directors; Share Capital; Deposits; CSR; SBO), plus SS-1 and SS-2.
- Every e-form filing is a Returns & Reporting row with a Due Date Rule and the e-form in Portal / Form / Return Code *(v1.2)* (for example AOC-4 within 30 days of the AGM; MGT-7 within 60 days of the AGM).
- Registers (MBP-1, MBP-2, MBP-4, MGT-1, CHG-7, SH-6, BEN-3) are "Registers & Records" rows.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Companies Act, 2013 and Rules (Incorporation; Management and Administration; Meetings of Board; Accounts; Audit and Auditors; Appointment and Qualification of Directors …)
- Exemption notifications for private, government, Section 8 and Nidhi companies (5 Jun 2015 and later) [VERIFY]
- ICSI Secretarial Standards SS-1 and SS-2 (revised, effective 1 Apr 2024)
- MCA21 V3 e-forms (all Companies Act e-forms on V3 since 14 Jul 2025)
- FEMA (Non-debt Instruments) Rules, 2019 (companies with foreign investment)
- Companies (Auditor's Report) Order, 2020 (auditor-side; write company-side preparation rows only)

## 5. Family-specific pitfalls

- Missing the private-company exemptions in Conditional Applicability / Exemptions / Thresholds.
- Writing form numbers from MCA21 V2 that have changed in V3 [VERIFY].

## 6. File naming

`MCA-CO - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Company Class Flags | Listed · Unlisted public · Private · OPC · Small company · Section 8 · Nidhi · Government company · Producer company | Use where the row turns on a class flag that General Applicability (Layer) does not capture alone (e.g., private company that is a subsidiary of a public company). |
| Financial Threshold | CSR threshold (s.135(1)) · Independent director threshold (Rule 4, ACMD Rules) · Woman director threshold (Rule 3, ACMD Rules) · Internal audit threshold (Rule 13, Accounts Rules) · Secretarial audit threshold (s.204) · Whole-time CS / KMP threshold (Rule 8 / 8A) · Cost audit threshold (s.148) | Name the threshold that decides applicability; write the numbers and the reference date in Conditional Applicability. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-MCA-CO-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Secretarial → Board meetings / General meetings / RoC filings / Statutory registers / Director KYC; Finance, Treasury and Accounts → Financial statements / CSR spend; Governance & Administration → Board composition / Committees. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Filings → Regulatory; board and committee rows → Governance; deposits and loans to directors → Legal; Governance. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the company filed Form DIR-12 with the Registrar within 30 days of the appointment of a director? |
| 4 | Clause / Para No. (`clause_ref`) | Section 170(2), Companies Act, 2013, read with Rule 18, Companies (Appointment and Qualification of Directors) Rules, 2014 |
| 5 | Department (`department`) | Secretarial |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | MCA |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Companies Act, 2013 |
| 12 | Instrument Reference No. (`instrument_ref`) | Act No. 18 of 2013 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 29-Aug-2013 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amending Act] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY date of the amendment to s.172 penalties] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.mca.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | All Companies |
| 20 | General Applicability (Type) (`applic_type`) | All Companies (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to every company. Also applies on change in designation and on cessation. |
| 22 | Applicable From (`applic_from`) | 01-Apr-2014 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Company Class Flags (`ext_*`) | (blank — not a deciding factor here) |
| E2 | Financial Threshold (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Directors - return of appointment (DIR-12) |
| 25 | Interpretation / Explanation (`explanation`) | The return of particulars is filed for appointment, change in designation and cessation. Late filing attracts additional fees and the penalty under s.172. (Abridged.) |
| 26 | Department Function (`dept_function`) | RoC Filings |
| 27 | Department Sub-function (`dept_subfunction`) | Director changes |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 30 days of the appointment |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Appointment of director / KMP / officer |
| 31 | Filing / Reporting / Intimation (`filing_details`) | MCA (ROC) - e-Form — return of appointment of director |
| 32 | Portal / Form / Return Code (`filing_form`) | Form DIR-12 |
| 33 | Related Document / Policy / Committee (`related_docs`) | Register of Directors and KMP; Board resolution |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Penalty on the company and every officer in default under s.172; additional fees on late filing. |
| 36 | Penalty Provision (`penalty_ref`) | Section 172, Companies Act, 2013 |
| 37 | Risk Type (`risk_type`) | Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | SRN and challan for DIR-12; Board resolution; consent in DIR-2 |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | After the Board appoints a director, collect DIR-2 and the declarations. File DIR-12 within 30 days and update the Register of Directors and KMP. Save the SRN. |
| 42 | Checker Review Points (`checker_points`) | 1. DIR-12 SRN date ≤ appointment + 30 days. 2. Attachments include DIR-2 and the resolution. 3. Register updated. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. List director changes from the Register. 2. Match each to a DIR-12 SRN. Exception: missing or late filing. |
| 44 | Tags / Keywords (`tags`) | dir-12; director appointment; section 170; roc filing |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

