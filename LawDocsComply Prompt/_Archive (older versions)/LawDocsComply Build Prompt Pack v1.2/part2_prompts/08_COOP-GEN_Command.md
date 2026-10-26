# 08 — COOP-GEN Family Command: Other Co-operative Societies and Registered Societies

**Template:** `templates/LDC-TPL-COOP-GEN-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-COOP-GEN-v2.0` · **Regulator / authority:** Central Registrar / State Registrars of Co-operative Societies; Registrar of Societies (SRA 1860) · **Named-range prefix:** `COOP_GEN_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-COOP-GEN-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Registration Law.** General Applicability (Layer) records the registration law (MSCS Act, State Act, MACS Act, federal/apex society, or Societies Registration Act 1860 for non-co-operative societies).

**General Applicability (Type) — Society Type.** General Applicability (Type) records the society type: housing, consumer, dairy, marketing, sugar/agro-processing, fisheries, weavers/industrial, labour, multipurpose, transport, health, tourism, national MSCS (seeds/organic/exports), federations, SRA educational or charitable societies. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (COOP_GEN_Sector):**
- Multi-State Co-operative Society (MSCS Act, 2002)
- State Co-operative Society (State Act)
- Mutually Aided Co-operative (State MACS Act)
- Federal / Apex Co-operative
- Society under Societies Registration Act, 1860 (non-co-operative)
- All

**General Applicability (Type) (COOP_GEN_Entity):**
- Housing Co-operative Society
- Consumer Co-operative
- Dairy / Milk Producers' Co-operative
- Marketing Co-operative
- Agro-processing / Sugar Co-operative
- Fisheries Co-operative
- Weavers' / Industrial Co-operative
- Labour Contract Co-operative
- Multipurpose Co-operative
- Transport Co-operative
- Health / Hospital Co-operative
- Tourism Co-operative
- National-level MSCS (Seeds / Organic / Exports)
- Federation / Union
- Educational / Charitable Society (SRA 1860)
- All (ALL)

**Due Date & Frequency (COOP_GEN_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (COOP_GEN_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Membership & Elections, Audit, Member Services & Grievance, Business Operations. Family additions: Membership & Elections, Audit, Member Services & Grievance, Business Operations.

**Compliance Type (COOP_GEN_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Risk Category (COOP_GEN_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (COOP_GEN_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- Central Registrar of Co-operative Societies (CRCS Portal)
- Registrar of Co-operative Societies (State)
- Co-operative Election Authority (MSCS)
- State Co-operative Election Commission / Authority
- Co-operative Ombudsman (MSCS)
- Statutory Auditor (Panel)
- Department / Government Auditor
- General Body / Members
- Board of Directors / Committee of Management
- FIU-IND (FINnet 2.0)
- Income Tax / GST Authorities
- Registrar of Societies (SRA 1860)
- NCDC
- Not Required

## 3. Applicability logic for this family

- Governance rows (general body, board, elections, audit, annual return, registers, bye-law amendments) are common to all types. Sector rows (for example housing-society maintenance and transfer rules under State housing bye-laws, dairy FSSAI licensing) are written as separate sheets.
- SRA 1860 societies follow the central Act as amended by their State. Annual list of governing body members filing applies [VERIFY State].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- MSCS Act, 2002 (as amended 2023) and MSCS Rules
- State Co-operative Societies Acts and Rules
- Societies Registration Act, 1860 and State amendments
- State model bye-laws for housing societies [VERIFY]
- Income-tax Act, 2025 (co-operative society provisions) [VERIFY section numbers]

## 5. Family-specific pitfalls

- Writing credit-society deposit rules for non-credit societies.
- Treating SRA societies as co-operatives. Use the SRA value in General Applicability (Layer).

## 6. File naming

`COOP-GEN - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Governing Act (State / MSCS) | State Co-operative Societies Act · Multi-State Co-operative Societies Act, 2002 · State Mutually Aided Co-operative Societies Act | The Act under which the society is registered, where the row depends on it. |
| State | <States and Union Territories, as in `Lists`> | The State whose Act or rules create the obligation. Blank for MSCS rows. |
| Society Size Class | Small · Medium · Large | Use where a size test (turnover, deposits, members) in the Act or rules decides applicability; write the exact test in Conditional Applicability. [VERIFY class definitions per State.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-COOP-GEN-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Governance & Administration → General body meetings / Committee meetings; Membership & Elections → Elections / Member register; Audit → Statutory audit / Audit rectification; Returns & Reporting → Registrar returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: General body, committee and election rows → Governance; member services → Conduct & Consumer; business operations → Operational. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the society held its annual general meeting within six months of the close of the financial year? |
| 4 | Clause / Para No. (`clause_ref`) | Section 75(1), Maharashtra Co-operative Societies Act, 1960 [VERIFY] |
| 5 | Department (`department`) | Governance & Administration |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | Registrar of Co-operative Societies |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Maharashtra Co-operative Societies Act, 1960 |
| 12 | Instrument Reference No. (`instrument_ref`) | Maharashtra Act No. XXIV of 1961 [VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | [VERIFY] dates: issue and last-amendment dates to be confirmed from the official Maharashtra text. |
| 18 | Source Link (`source_url`) | https://www.indiacode.nic.in |
| 19 | General Applicability (Layer) (`applic_layer`) | State Co-operative Society (State Act) |
| 20 | General Applicability (Type) (`applic_type`) | All (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to societies registered under the Maharashtra Act. [VERIFY any extension of time granted by the Registrar.] |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Governing Act (State / MSCS) (`ext_*`) | State Co-operative Societies Act |
| E2 | State (`ext_*`) | Maharashtra |
| E3 | Society Size Class (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Annual general meeting - within six months |
| 25 | Interpretation / Explanation (`explanation`) | The AGM adopts the audited accounts, the audit report and the plan for distributing surplus. The six-month window is fixed by the Act; holding the AGM later without an extension is a breach even if accounts are adopted. (Abridged.) |
| 26 | Department Function (`dept_function`) | General Meetings |
| 27 | Department Sub-function (`dept_subfunction`) | Annual general meeting |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within six months of the close of the financial year |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Registrar of Co-operative Societies (State) — AGM-related returns [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Bye-laws; Managing Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Committee members may be disqualified and the Registrar may act under the Act [VERIFY section]. |
| 36 | Penalty Provision (`penalty_ref`) | [VERIFY penalty section] |
| 37 | Risk Type (`risk_type`) | Governance; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | AGM notice with dispatch proof; AGM minutes; attendance register |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Fix the AGM date in the Managing Committee meeting held after the audit. Send notice as per the bye-laws. Hold the AGM by 30 September and record the minutes. If an extension is needed, apply to the Registrar before the deadline. |
| 42 | Checker Review Points (`checker_points`) | 1. AGM held on or before 30 September (or within an approved extension). 2. Notice period met. 3. Quorum recorded. 4. Minutes signed. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect AGM notice, minutes and attendance for the year. 2. Compare the AGM date with the deadline. Exception: late AGM without a Registrar extension. |
| 44 | Tags / Keywords (`tags`) | agm; general meeting; co-operative society; maharashtra; section 75 |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

