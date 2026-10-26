# 16 — SEBI-INT Family Command: SEBI Market Intermediaries

**Template:** `templates/LDC-TPL-SEBI-INT-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-SEBI-INT-v2.0` · **Regulator / authority:** Securities and Exchange Board of India · **Named-range prefix:** `SEBI_INT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-SEBI-INT-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Intermediary Group.** General Applicability (Layer) holds the intermediary group (trading and clearing, depository, advisory and research, issue management and registry, portfolio and fund services, rating/trusteeship/custody, data and index services).

**General Applicability (Type) — Intermediary Type / CSCRF Category.** General Applicability (Type) names the intermediary type and, for cyber rows, the CSCRF category (Qualified, Mid-size, Small-size, Self-certification). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (SEBI_INT_Sector):**
- Trading and Clearing
- Depository Services
- Advisory and Research
- Issue Management and Registry
- Portfolio and Fund Services
- Rating, Trusteeship and Custody
- Data and Index Services
- All Intermediaries

**General Applicability (Type) (SEBI_INT_Entity):**
- Stock Broker
- Clearing Member
- Depository Participant
- Investment Adviser
- Research Analyst
- Portfolio Manager
- Merchant Banker
- Registrar to an Issue and Share Transfer Agent (RTA)
- Banker to an Issue
- Debenture Trustee
- Credit Rating Agency
- Custodian
- KYC Registration Agency (KRA)
- ESG Rating Provider
- Online Bond Platform Provider
- Vault Manager
- Index Provider
- CSCRF - Qualified RE
- CSCRF - Mid-size RE
- CSCRF - Small-size RE
- CSCRF - Self-certification RE
- All Intermediaries (ALL)

**Due Date & Frequency (SEBI_INT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (SEBI_INT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Client Onboarding & KYC, Surveillance, Investor Grievance, Internal Audit, Information Security. Family additions: Client Onboarding & KYC, Surveillance, Investor Grievance, Internal Audit, Information Security.

**Compliance Type (SEBI_INT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (SEBI_INT_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (SEBI_INT_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- SEBI (filing)
- SEBI (prior approval)
- SEBI (intimation)
- SEBI Intermediary Portal (SI Portal)
- SEBI SCORES / SMART ODR
- Stock Exchanges (supervising MII)
- Depositories
- Clearing Corporations
- KRA / CKYCR
- BSE Administration & Supervision Ltd (BASL) - IA / RA
- FIU-IND (FINnet 2.0)
- CERT-In
- Board / Management
- Statutory / Internal Auditor
- Not Required

## 3. Applicability logic for this family

- Each intermediary has its own activity regulations and master circular. Write one sheet per regulation.
- CSCRF rows should go in CYBER unless the obligation is intermediary-specific. If they go here, use the CSCRF category values in General Applicability (Type).
- IA/RA administration and supervision is delegated to BASL. Record the BASL filing route in Filing / Reporting / Intimation.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SEBI Act, 1992 s.12; SEBI (Intermediaries) Regulations, 2008
- Activity regulations: Stock Brokers [VERIFY current regulations], Depositories and Participants 2018, Investment Advisers 2013, Research Analysts 2014, Portfolio Managers 2020, Merchant Bankers, RTA, Debenture Trustees, Credit Rating Agencies, Custodians, KRA [VERIFY]
- SEBI CSCRF (20 Aug 2024) and clarifications
- SEBI master circulars by intermediary type [VERIFY dates]

## 5. Family-specific pitfalls

- Using pre-2025 stock broker or merchant banker regulation references where SEBI has issued replacement regulations [VERIFY].

## 6. File naming

`SEBI-INT - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| CSCRF Size Band | MII · Qualified RE · Mid-size RE · Small-size RE · Self-certification RE | Use for rows whose content or frequency depends on the CSCRF category. [VERIFY categorisation criteria in the CSCRF circular.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-SEBI-INT-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Investor Grievance → SCORES complaints / ODR; Client Onboarding & KYC → KYC / KRA upload; Surveillance → Alerts / STR; Information Security → CSCRF controls; Returns & Reporting → SEBI and MII reports. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Client-facing → Conduct & Consumer; CSCRF → IT & Cyber; surveillance → Fraud; Market. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the intermediary resolved each investor complaint received through SCORES within 21 calendar days of receipt? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], SEBI circular on SCORES 2.0 dated [VERIFY], read with the activity regulations |
| 5 | Department (`department`) | Investor Grievance |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | SEBI circular – Redressal of investor grievances through SEBI Complaints Redress System (SCORES) platform [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | SEBI/HO/OIAE/IGRD/CIR/P/2023/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY — Dec 2023] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Amended |
| 17 | Change Note / Previous Actionable (`change_note`) | Timeline reduced to 21 calendar days under SCORES 2.0 [VERIFY]; previous actionable: 'Has the intermediary resolved SCORES complaints within 30 days?' |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | All Intermediaries |
| 20 | General Applicability (Type) (`applic_type`) | All Intermediaries (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to all registered intermediaries on SCORES. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | CSCRF Size Band (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Investor grievances - SCORES resolution timeline |
| 25 | Interpretation / Explanation (`explanation`) | The timeline runs from receipt on SCORES; an action-taken report is uploaded on SCORES. Unresolved complaints escalate to the designated body and may go to ODR. (Abridged.) |
| 26 | Department Function (`dept_function`) | Grievance Redress |
| 27 | Department Sub-function (`dept_subfunction`) | SCORES complaints |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within 21 days of receipt of the complaint |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Customer complaint or grievance received |
| 31 | Filing / Reporting / Intimation (`filing_details`) | SEBI SCORES / SMART ODR — action-taken report |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Investor Grievance Policy; Compliance Officer |
| 34 | Reference Weblinks (`weblinks`) | https://scores.sebi.gov.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | SEBI may impose a penalty under s.15C, SEBI Act, for failure to redress investor grievances. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15C, SEBI Act, 1992 |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | SCORES action-taken reports with dates; complaint register; closure communications to investors |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Check SCORES daily. Investigate each complaint, reply to the investor and upload the action-taken report within 21 calendar days. Escalate any complaint at day 15 to the Compliance Officer. |
| 42 | Checker Review Points (`checker_points`) | 1. All complaints in the period are logged. 2. ATR uploaded ≤ 21 days. 3. ATR addresses the complaint substance. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Download the SCORES report for the period. 2. Sample 25 complaints. 3. Re-compute TAT. Exception: any ATR beyond 21 days. |
| 44 | Tags / Keywords (`tags`) | scores; investor grievance; complaint; 21 days; odr |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

