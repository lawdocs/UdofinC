# 18 — IRDAI-INT Family Command: Insurance Intermediaries

**Template:** `templates/LDC-TPL-IRDAI-INT-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-IRDAI-INT-v2.0` · **Regulator / authority:** Insurance Regulatory and Development Authority of India · **Named-range prefix:** `IRDAI_INT_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-IRDAI-INT-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Intermediary Class.** General Applicability (Layer) holds the intermediary class (broker, corporate agent, IMF, web aggregator, TPA, surveyor, CSC/POSP channel, MGA, insurance repository).

**General Applicability (Type) — Intermediary Type.** General Applicability (Type) refines it (direct life/general/composite broker, reinsurance broker, corporate agent by line, bank or NBFC as corporate agent, individual or corporate surveyor). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (IRDAI_INT_Sector):**
- Insurance Broker
- Corporate Agent
- Insurance Marketing Firm (IMF)
- Web Aggregator
- Third Party Administrator (TPA)
- Surveyor and Loss Assessor
- Common Service Centre / POSP channel
- Managing General Agent (MGA)
- Insurance Repository
- All Intermediaries

**General Applicability (Type) (IRDAI_INT_Entity):**
- Direct Broker - Life
- Direct Broker - General
- Direct Broker - Life and General
- Reinsurance Broker
- Composite Broker
- Corporate Agent - Life
- Corporate Agent - General
- Corporate Agent - Health
- Corporate Agent - Composite
- Bank / NBFC as Corporate Agent
- Insurance Marketing Firm
- Web Aggregator
- TPA - Health Services
- Surveyor (Individual)
- Surveyor (Corporate)
- Point of Sales Person (POSP) platform
- All Intermediaries (ALL)

**Due Date & Frequency (IRDAI_INT_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (IRDAI_INT_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Sales & Distribution, Claims Support, Policyholder Grievance, Internal Audit. Family additions: Sales & Distribution, Claims Support, Policyholder Grievance, Internal Audit.

**Compliance Type (IRDAI_INT_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (IRDAI_INT_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (IRDAI_INT_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- IRDAI (filing)
- IRDAI (prior approval)
- IRDAI (intimation)
- IRDAI Bima Bharosa (grievance)
- Partner Insurers
- FIU-IND (FINnet 2.0)
- CERT-In
- MCA (ROC)
- RBI (parent regulator - bank / NBFC CA)
- Board / Principal Officer
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- After the 2025 amendment, s.42D registration is perpetual subject to annual fee and conditions. Write an annual fee row and continuing-condition rows.
- Banks and NBFCs acting as corporate agents also follow RBI rules on third-party product distribution (Undertaking of Financial Services Direction for NBFCs). Note this in Conditional Applicability / Exemptions / Thresholds and write the RBI rows in the RBI family.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Insurance Act, 1938 s.42D (as amended 2025: perpetual registration; MGAs and insurance repositories included)
- IRDAI (Insurance Brokers) Regulations, 2018
- IRDAI (Registration of Corporate Agents) Regulations, 2015
- IRDAI (TPA – Health Services) Regulations, 2016; IRDAI (Insurance Surveyors and Loss Assessors) Regulations, 2015
- IRDAI (Expenses of Management, including Commission, of Insurers) Regulations, 2024
- Consolidated intermediary regulations and master circulars of 2024–26 [VERIFY]

## 5. Family-specific pitfalls

- Treating individual agents as intermediaries in this family. They are appointed by insurers.

## 6. File naming

`IRDAI-INT - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Intermediary Class | Insurance broker · Corporate agent · Insurance marketing firm · Web aggregator · TPA · Surveyor and loss assessor · POSP / MISP channel · Insurance repository | Use where the row applies to some classes only and General Applicability (Type) is more granular. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-IRDAI-INT-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Sales & Distribution → Licensing / Training of specified persons; Policyholder Grievance → Grievance redress; Governance & Administration → Principal Officer; Finance, Treasury and Accounts → Net worth / PI cover. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Sales conduct → Conduct & Consumer; PI cover and net worth → Operational; Credit. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the insurance broker maintained professional indemnity insurance cover of the amount prescribed for its category throughout the validity of its registration? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation [VERIFY], IRDAI (Insurance Brokers) Regulations, 2018 |
| 5 | Department (`department`) | Finance, Treasury and Accounts |
| 6 | Due Date & Frequency (`frequency`) | Ongoing/Continuous |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | IRDAI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | IRDAI (Insurance Brokers) Regulations, 2018 |
| 12 | Instrument Reference No. (`instrument_ref`) | IRDAI/Reg/[VERIFY]/2018 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY — 2018] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | [VERIFY] whether the 2024–25 IRDAI consolidation replaced these Regulations. |
| 18 | Source Link (`source_url`) | https://irdai.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Insurance Broker |
| 20 | General Applicability (Type) (`applic_type`) | Direct Broker - Life and General; Reinsurance Broker; Composite Broker |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Cover amount depends on the broker category and premium [VERIFY]. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Intermediary Class (`ext_*`) | Insurance broker |
| 24 | Short Title (`short_title`) | Professional indemnity insurance - maintenance |
| 25 | Interpretation / Explanation (`explanation`) | The cover must be in force at all times; a lapse between renewal dates is a breach. (Abridged.) |
| 26 | Department Function (`dept_function`) | Net Worth and Insurance Cover |
| 27 | Department Sub-function (`dept_subfunction`) | PI cover |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Renew before the policy expiry date each year |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | IRDAI (filing) — copy of PI policy with the annual return [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Board / Principal Officer |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | IRDAI may suspend or cancel registration or impose a penalty under s.102 / s.105C, Insurance Act [VERIFY]. |
| 36 | Penalty Provision (`penalty_ref`) | Section 102, Insurance Act, 1938 |
| 37 | Risk Type (`risk_type`) | Operational; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | PI policy schedule showing period and sum insured; renewal premium receipt |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Track PI expiry. Start renewal 30 days before expiry. Check the sum insured against the prescribed minimum and file a copy as required. |
| 42 | Checker Review Points (`checker_points`) | 1. Policy period has no gap. 2. Sum insured ≥ prescribed amount. 3. Copy filed where required. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect policy schedules covering the audit period. Exception: any gap or shortfall. |
| 44 | Tags / Keywords (`tags`) | professional indemnity; pi cover; insurance broker; irdai |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

