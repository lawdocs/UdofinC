# 07 — COOP-CCS Family Command: Credit Co-operative Societies (multi-State, State, PACS)

**Template:** `templates/LDC-TPL-COOP-CCS-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-COOP-CCS-v2.0` · **Regulator / authority:** Central Registrar (MSCS Act, 2002) / State Registrars of Co-operative Societies · **Named-range prefix:** `COOP_CCS_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-COOP-CCS-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Registration Law.** General Applicability (Layer) records the registration law, which decides the regulator: multi-State societies under the MSCS Act 2002 (Central Registrar), State societies under the State Act (State Registrar), mutually aided co-operatives under State MACS Acts, and PACS (State Act, with Ministry of Cooperation model bye-laws).

**General Applicability (Type) — Society Type.** General Applicability (Type) records the society type: urban/nagari credit society (patsanstha), employees' or salary-earners' credit society, thrift and credit society, PACS, LAMPS, FSS, women's credit society, and societies above the concurrent-audit threshold. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (COOP_CCS_Sector):**
- Multi-State Credit Co-operative Society (MSCS Act, 2002)
- State Credit Co-operative Society (State Co-operative Societies Act)
- Mutually Aided / Self-reliant Co-operative (State MACS Act)
- Primary Agricultural Credit Society (PACS)
- All Credit Co-operative Societies

**General Applicability (Type) (COOP_CCS_Entity):**
- Urban / Nagari Credit Co-operative Society (Patsanstha)
- Employees' / Salary Earners' Credit Co-operative Society
- Thrift and Credit Co-operative Society
- Primary Agricultural Credit Society (PACS)
- Large-sized Adivasi Multipurpose Society (LAMPS)
- Farmers' Service Society (FSS)
- Multi-State Credit Co-operative Society
- Women's Credit Co-operative Society
- Society subject to concurrent audit (State Act threshold)
- All (ALL)

**Due Date & Frequency (COOP_CCS_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (COOP_CCS_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit & Recovery, Membership & Elections, Audit, Member Services & Grievance. Family additions: Credit & Recovery, Membership & Elections, Audit, Member Services & Grievance.

**Compliance Type (COOP_CCS_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Risk Category (COOP_CCS_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (COOP_CCS_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
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
- Credit Information Companies (CICs)
- NABARD (PACS)
- Not Required

## 3. Applicability logic for this family

- First decide the governing statute. A society operating in more than one State is a multi-State society under the MSCS Act. Otherwise the State Act of the registration State applies. Write one sheet per Act and per State. State Acts differ (for example Maharashtra 1960, Uttar Pradesh 1965, Rajasthan 2001, Gujarat 1961, Karnataka 1959, Delhi 2003).
- Credit societies may accept deposits only from members and may not use the words "bank", "banker" or "banking" (BR Act s.7) [VERIFY State-specific deposit rules].
- The 2023 MSCS amendments introduced the Co-operative Election Authority, the Co-operative Ombudsman, the Co-operative Rehabilitation, Reconstruction and Development Fund, board composition requirements (seats for women and SC/ST), concurrent audit above a turnover/deposit threshold, and information-officer duties. Write each as its own rows [VERIFY section numbers].
- Loan operations (sanction, interest, recovery) are run in Finbyx. Write the regulatory obligations here (lending limits, member-only lending, recovery under the Act, audit classification).

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Multi-State Co-operative Societies Act, 2002 as amended by the MSCS (Amendment) Act, 2023 (Act 11 of 2023); MSCS Rules, 2002 as amended 2023 [VERIFY]
- State Co-operative Societies Acts and Rules of the selected State (e.g., Maharashtra 1960, Uttar Pradesh 1965, Rajasthan 2001, Delhi 2003, Gujarat 1961, Karnataka 1959)
- Model bye-laws for PACS (Ministry of Cooperation) [VERIFY]
- Banking Regulation Act, 1949 s.7 and s.56 (prohibition on use of the word "bank")
- PMLA, 2002 (where the society is a reporting entity) [VERIFY applicability]
- Income-tax Act, 2025 provisions on co-operative societies [VERIFY]

## 5. Family-specific pitfalls

- Writing RBI UCB rules for a credit society. A credit society is not a bank.
- Mixing two States' Acts in one sheet.
- Missing election-cycle rows (board term of five years, election before expiry).

## 6. File naming

`COOP-CCS - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Governing Act (State / MSCS) | State Co-operative Societies Act · Multi-State Co-operative Societies Act, 2002 · State Mutually Aided Co-operative Societies Act | The Act under which the society is registered, where the row depends on it. |
| State | <States and Union Territories, as in `Lists`> | The State whose Act or rules create the obligation. Blank for MSCS rows. |
| Society Size Class | Small · Medium · Large | Use where a size test (turnover, deposits, members) in the Act or rules decides applicability; write the exact test in Conditional Applicability. [VERIFY class definitions per State.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-COOP-CCS-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Membership & Elections → Member register / Elections; Audit → Statutory audit / Concurrent audit; Credit & Recovery → Loan sanction / Recovery; Returns & Reporting → Annual return / Registrar filings; Governance & Administration → General body / Board meetings. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Member deposits and lending → Credit / Liquidity; elections and general body → Governance; member grievances → Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the multi-State co-operative society filed its annual return with the Central Registrar within six months of the close of the financial year? |
| 4 | Clause / Para No. (`clause_ref`) | Section 120(1), Multi-State Co-operative Societies Act, 2002 |
| 5 | Department (`department`) | Returns & Reporting |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | Central Registrar of Co-operative Societies |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Multi-State Co-operative Societies Act, 2002 |
| 12 | Instrument Reference No. (`instrument_ref`) | Act No. 39 of 2002 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 03-Aug-2002 [VERIFY] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 03-Aug-2023 [VERIFY — MSCS (Amendment) Act, 2023] |
| 15 | Actionable Last Updated On (`question_updated_date`) | 03-Aug-2023 [VERIFY] |
| 16 | Change Status (`change_status`) | Amended |
| 17 | Change Note / Previous Actionable (`change_note`) | Section 120 substituted by the MSCS (Amendment) Act, 2023 [VERIFY]; previous actionable: 'Has the society filed its annual return …?' (contents of the return expanded). |
| 18 | Source Link (`source_url`) | https://www.indiacode.nic.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Multi-State Credit Co-operative Society (MSCS Act, 2002) |
| 20 | General Applicability (Type) (`applic_type`) | All (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to every multi-State co-operative society. |
| 22 | Applicable From (`applic_from`) | [VERIFY commencement of the 2023 amendment] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Governing Act (State / MSCS) (`ext_*`) | Multi-State Co-operative Societies Act, 2002 |
| E2 | State (`ext_*`) | (blank — not a deciding factor here) |
| E3 | Society Size Class (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Annual return - filing with the Central Registrar |
| 25 | Interpretation / Explanation (`explanation`) | The return lists the matters in s.120 (activities, audited accounts, plan for surplus, amendments to bye-laws, general-meeting and election details). It is filed on the CRCS portal. (Abridged.) |
| 26 | Department Function (`dept_function`) | Registrar Filings |
| 27 | Department Sub-function (`dept_subfunction`) | Annual return |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within six months of the close of the financial year |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Central Registrar of Co-operative Societies (CRCS Portal) — annual return |
| 32 | Portal / Form / Return Code (`filing_form`) | [VERIFY CRCS portal form] |
| 33 | Related Document / Policy / Committee (`related_docs`) | Audited financial statements; Annual general meeting |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Offence / penalty under the MSCS Act for failure to file returns; action by the Central Registrar. |
| 36 | Penalty Provision (`penalty_ref`) | Section 104, Multi-State Co-operative Societies Act, 2002 [VERIFY] |
| 37 | Risk Type (`risk_type`) | Regulatory; Governance |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | CRCS portal acknowledgement; copy of the filed return; audited accounts adopted at the AGM |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | After the accounts are audited and adopted, prepare the annual return with every item listed in s.120. Have the Chief Executive approve it and file it on the CRCS portal before 30 September. Save the acknowledgement. |
| 42 | Checker Review Points (`checker_points`) | 1. Return covers every item in s.120. 2. Figures match the audited accounts. 3. Filing date is on or before 30 September. 4. Acknowledgement saved. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect the CRCS acknowledgement for the year. 2. Agree the return to the audited accounts and AGM minutes. Exception: late or incomplete filing. |
| 44 | Tags / Keywords (`tags`) | annual return; crcs; mscs; section 120 |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

