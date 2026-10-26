# 23 — LAB-POSH Family Command: Labour Codes, Shops and Establishments, and POSH

**Template:** `templates/LDC-TPL-LAB-POSH-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-LAB-POSH-v2.0` · **Regulator / authority:** Ministry of Labour and Employment; State Labour Departments; Ministry of Women and Child Development (POSH) · **Named-range prefix:** `LAB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-LAB-POSH-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Law.** General Applicability (Layer) holds the law (each Labour Code, the POSH Act, State Shops and Establishments Act, State PT/LWF, Apprentices Act).

**General Applicability (Type) — Establishment Type / Threshold.** General Applicability (Type) holds the establishment type or headcount threshold that switches obligations on (10, 20, 50, 100, 300 employees; factory; shop; IT/ITES; contractor; inter-State migrants; gig/platform; BOCW; remote workforce). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (LAB_Sector):**
- Code on Wages, 2019
- Industrial Relations Code, 2020
- Code on Social Security, 2020
- Occupational Safety, Health and Working Conditions Code, 2020
- POSH Act, 2013
- Shops and Establishments Act (State)
- Professional Tax / Labour Welfare Fund (State)
- Apprentices Act, 1961
- All Labour Laws

**General Applicability (Type) (LAB_Entity):**
- All establishments
- Establishment with 10 or more employees
- Establishment with 20 or more employees
- Establishment with 50 or more employees
- Establishment with 100 or more employees
- Establishment with 300 or more workers (standing orders)
- Factory
- Shop / Commercial establishment
- IT / ITES establishment
- Contractor / Principal employer (contract labour)
- Inter-State migrant workers employer
- Gig / Platform aggregator
- Building and other construction work
- Remote / work-from-home workforce
- All (ALL)

**Due Date & Frequency (LAB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (LAB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Payroll, Administration & Facilities, Internal Committee (POSH). Family additions: Payroll, Administration & Facilities, Internal Committee (POSH).

**Compliance Type (LAB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Risk Category (LAB_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (LAB_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- Shram Suvidha Portal (MoLE)
- EPFO (Unified Portal)
- ESIC Portal
- State Labour Department (Shops and Establishments)
- Inspector-cum-Facilitator
- District Officer (POSH - annual report)
- Welfare Board (BOCW)
- Professional Tax Authority (State)
- Labour Welfare Fund Board (State)
- Employees (display / notice)
- Board (Directors' Report disclosure)
- Not Required

## 3. Applicability logic for this family

- All four Labour Codes took effect on 21 Nov 2025. Central and State rules are notified in stages, so check the State rule before writing State-specific registers and returns [VERIFY by State].
- Registers and returns under the Codes are prescribed by rules, mostly in electronic form. Each register is a "Registers & Records" row.
- POSH: IC constitution (s.4), annual report to the District Officer (s.21 read with r.14), display and awareness (s.19), Board report disclosure (Companies (Accounts) Rules r.8(5)(x)).

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Code on Wages, 2019; Industrial Relations Code, 2020; Code on Social Security, 2020; OSH Code, 2020 (all in force from 21 Nov 2025) and Central Rules [VERIFY]
- State rules under each Code and State Shops and Establishments Acts [select State]
- Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 and Rules, 2013
- Companies (Accounts) Rules, 2014 r.8(5)(x) (POSH disclosure in the Board report)
- Professional Tax and Labour Welfare Fund Acts of the State

## 5. Family-specific pitfalls

- Citing repealed Acts (Payment of Wages Act, Factories Act, etc.) after 21 Nov 2025 except for transitional matters.
- Missing State variation in thresholds.

## 6. File naming

`LAB-POSH - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Labour Code / Act | Code on Wages, 2019 · Industrial Relations Code, 2020 · Code on Social Security, 2020 · OSH Code, 2020 · POSH Act, 2013 · Shops and Establishments Act (State) · Other | Use where the sheet is cross-law (e.g., a register satisfying several codes). |
| State | <States and Union Territories, as in `Lists`> | The State whose rules apply. |
| Headcount Threshold | 10 or more · 20 or more · 50 or more · 100 or more · 300 or more · 500 or more | The employee or worker count that decides applicability; state the definition used (employees vs workers) in Conditional Applicability. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-LAB-POSH-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: HR → POSH / Registers / Leave; Payroll → Wages / PF / ESI; Internal Committee (POSH) → Complaints / Annual report; Administration & Facilities → Displays / Safety. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: People primary; add Legal for statutory registers, returns and inspections. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the Internal Committee prepared its annual report for the calendar year and has the employer submitted it to the District Officer? |
| 4 | Clause / Para No. (`clause_ref`) | Section 21, Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013, read with Rule 14, POSH Rules, 2013 |
| 5 | Department (`department`) | Internal Committee (POSH) |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | Medium |
| 10 | Regulator / Authority (`authority`) | Ministry of Women and Child Development |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 |
| 12 | Instrument Reference No. (`instrument_ref`) | Act No. 14 of 2013 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 22-Apr-2013 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 22-Apr-2013 |
| 15 | Actionable Last Updated On (`question_updated_date`) | 22-Apr-2013 |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | (blank) |
| 18 | Source Link (`source_url`) | https://www.indiacode.nic.in |
| 19 | General Applicability (Layer) (`applic_layer`) | POSH Act, 2013 |
| 20 | General Applicability (Type) (`applic_type`) | Establishment with 10 or more employees |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies where an Internal Committee is required (10 or more employees). [VERIFY State-specific due dates.] |
| 22 | Applicable From (`applic_from`) | 09-Dec-2013 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Labour Code / Act (`ext_*`) | POSH Act, 2013 |
| E2 | State (`ext_*`) | (blank — not a deciding factor here) |
| E3 | Headcount Threshold (`ext_*`) | 10 or more |
| 24 | Short Title (`short_title`) | POSH - annual report to the District Officer |
| 25 | Interpretation / Explanation (`explanation`) | Rule 14 lists the contents: number of complaints received, disposed of, pending beyond 90 days, workshops held and action taken. The employer also discloses the numbers in its annual report (s.22). (Abridged.) |
| 26 | Department Function (`dept_function`) | POSH |
| 27 | Department Sub-function (`dept_subfunction`) | Annual report |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | By 31 January each year [VERIFY State practice] |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | District Officer (POSH - annual report) |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | POSH Policy; Internal Committee; Directors' Report |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Fine up to ₹50,000 under s.26; higher penalty and possible cancellation of licence on repetition. |
| 36 | Penalty Provision (`penalty_ref`) | Section 26, POSH Act, 2013 |
| 37 | Risk Type (`risk_type`) | People; Legal |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | IC annual report; acknowledgement from the District Officer; Directors' Report extract |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | After 31 December, have the IC prepare the report with every Rule 14 item. Submit it to the District Officer and keep the acknowledgement. Give the numbers to the Secretarial team for the Directors' Report. |
| 42 | Checker Review Points (`checker_points`) | 1. Report covers every Rule 14 item. 2. Submitted and acknowledged. 3. Numbers match the complaint register. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect report and acknowledgement. 2. Agree numbers to the register. Exception: no report or mismatch. |
| 44 | Tags / Keywords (`tags`) | posh; internal committee; annual report; district officer |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

