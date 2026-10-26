# 17 — IRDAI-INS Family Command: Insurers (life, general, health, reinsurers, FRBs)

**Template:** `templates/LDC-TPL-IRDAI-INS-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-IRDAI-INS-v2.0` · **Regulator / authority:** Insurance Regulatory and Development Authority of India · **Named-range prefix:** `IRDAI_INS_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-IRDAI-INS-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Insurer Class.** General Applicability (Layer) holds the insurer class: life, general, standalone health, Indian reinsurer, FRB, Lloyd's India, composite/multi-line [VERIFY after the 2025 amendment].

**General Applicability (Type) — Insurer Overlay.** General Applicability (Type) holds overlays: public or private, listed, specialised insurer, bancassurance partner, ULIP, health products. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (IRDAI_INS_Sector):**
- Life Insurer
- General Insurer
- Standalone Health Insurer
- Indian Reinsurer
- Foreign Reinsurer Branch (FRB)
- Lloyd's India
- Composite Insurer (where licensed)
- All Insurers

**General Applicability (Type) (IRDAI_INS_Entity):**
- Public Sector Insurer
- Private Insurer
- Listed Insurer
- Specialised Insurer (e.g., agriculture, micro, export credit)
- Insurer with bancassurance / corporate agency tie-ups
- Insurer offering Unit Linked products
- Insurer offering Health products
- All Insurers (ALL)

**Due Date & Frequency (IRDAI_INS_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (IRDAI_INS_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Actuarial, Underwriting, Claims, Investments, Policyholder Servicing & Grievance, Internal Audit, Information Security. Family additions: Actuarial, Underwriting, Claims, Investments, Policyholder Servicing & Grievance, Internal Audit, Information Security.

**Compliance Type (IRDAI_INS_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (IRDAI_INS_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (IRDAI_INS_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- IRDAI (filing)
- IRDAI (prior approval / product filing)
- IRDAI (intimation)
- IRDAI Bima Bharosa (grievance)
- Insurance Ombudsman (CIO)
- Insurance Information Bureau (IIB)
- Life Insurance Council / General Insurance Council
- FIU-IND (FINnet 2.0)
- CERT-In
- SEBI / Stock Exchanges (listed insurers)
- MCA (ROC)
- Appointed Actuary
- Board / Management
- Statutory Auditor
- Not Required

## 3. Applicability logic for this family

- IRDAI moved to principle-based regulations in 2024 with master circulars. Cite both the regulation and the master circular paragraph.
- Check the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 for commencement of changed sections before citing amended section numbers [VERIFY].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Insurance Act, 1938 as amended by the Sabka Bima Sabki Raksha (Amendment of Insurance Laws) Act, 2025 [VERIFY commencement]
- IRDA Act, 1999
- IRDAI principle-based regulations, 2024 (Registration, Capital Structure, Transfer of Shares and Amalgamation; Corporate Governance; Protection of Policyholders' Interests; Actuarial, Finance and Investment Functions; Expenses of Management incl. Commission; Insurance Products; Rural, Social Sector and Motor Third Party Obligations) and master circulars [VERIFY exact titles]
- IRDAI Information and Cyber Security Guidelines, 2023

## 5. Family-specific pitfalls

- Citing repealed 2016/2017 regulations after the 2024 consolidation.
- Missing master-circular paragraph numbers.

## 6. File naming

`IRDAI-INS - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Line of Business | Life · General · Health · Reinsurance | Use where a provision differs by line; several values with "; ". |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-IRDAI-INS-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Policyholder Servicing & Grievance → Grievance redress / Claims TAT; Claims → Claim settlement; Underwriting → Product filing; Actuarial → Solvency / Reserving; Investments → Investment limits. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Policyholder rows → Conduct & Consumer; solvency → Credit / Market; claims → Operational; Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the insurer resolved each policyholder grievance within 14 days of receipt? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation [VERIFY], IRDAI (Protection of Policyholders' Interests and Allied Matters of Insurers) Regulations, 2024, read with the Master Circular [VERIFY] |
| 5 | Department (`department`) | Policyholder Servicing & Grievance |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | IRDAI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | IRDAI (Protection of Policyholders' Interests and Allied Matters of Insurers) Regulations, 2024 |
| 12 | Instrument Reference No. (`instrument_ref`) | IRDAI/Reg/[VERIFY]/2024 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY — 2024] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | Replaced the 2017 Policyholders' Interests Regulations [VERIFY]. |
| 18 | Source Link (`source_url`) | https://irdai.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | All Insurers |
| 20 | General Applicability (Type) (`applic_type`) | All Insurers (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to all insurers. [VERIFY separate TATs for specific grievance types.] |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Line of Business (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Grievance redress - resolution within 14 days |
| 25 | Interpretation / Explanation (`explanation`) | Grievances are registered on Bima Bharosa; the 14-day clock runs from receipt. A reply that does not address the grievance is not a resolution. (Abridged.) |
| 26 | Department Function (`dept_function`) | Grievance Redress |
| 27 | Department Sub-function (`dept_subfunction`) | Policyholder grievances |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within 14 days of receipt of the grievance |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Customer complaint or grievance received |
| 31 | Filing / Reporting / Intimation (`filing_details`) | IRDAI Bima Bharosa (grievance) — status update |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Grievance Redressal Policy; Policyholder Protection Committee |
| 34 | Reference Weblinks (`weblinks`) | https://bimabharosa.irdai.gov.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | IRDAI may impose a penalty under s.102, Insurance Act, 1938; Ombudsman awards. |
| 36 | Penalty Provision (`penalty_ref`) | Section 102, Insurance Act, 1938 |
| 37 | Risk Type (`risk_type`) | Conduct & Consumer; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Bima Bharosa status report; grievance register; resolution letters |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Register each grievance on Bima Bharosa. Resolve and update status within 14 days. Escalate any open grievance at day 10 to the Grievance Redressal Officer. |
| 42 | Checker Review Points (`checker_points`) | 1. All grievances registered. 2. Resolution ≤ 14 days. 3. Resolution letter addresses the grievance. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the Bima Bharosa report. 2. Sample 25 grievances. 3. Re-compute TAT. Exception: any beyond 14 days. |
| 44 | Tags / Keywords (`tags`) | grievance; bima bharosa; policyholder; 14 days |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

