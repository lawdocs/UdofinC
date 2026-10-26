# 21 — DATA-PRIV Family Command: Data Protection and Privacy (DPDP, IT Act, GDPR, CCPA)

**Template:** `templates/LDC-TPL-DATA-PRIV-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-DATA-PRIV-v2.0` · **Regulator / authority:** MeitY / Data Protection Board of India; EU supervisory authorities; California Privacy Protection Agency · **Named-range prefix:** `DATA_PRIV_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-DATA-PRIV-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Law / Jurisdiction.** General Applicability (Layer) holds the law or jurisdiction (DPDP Act and Rules; IT Act and SPDI Rules; EU GDPR; UK GDPR; CCPA/CPRA; sectoral data rules).

**General Applicability (Type) — Role.** General Applicability (Type) holds the privacy role (Data Fiduciary, SDF, Data Processor, Consent Manager; GDPR controller/processor/joint controller/representative; CCPA business/service provider/contractor/third party; data broker). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (DATA_PRIV_Sector):**
- DPDP Act, 2023 and DPDP Rules, 2025 (India)
- IT Act, 2000 and SPDI Rules, 2011 (India)
- EU GDPR (EU/EEA)
- UK GDPR and DPA 2018 (UK)
- CCPA as amended by CPRA (California)
- Sectoral data rules (RBI / SEBI / IRDAI / IFSCA)
- Other jurisdiction

**General Applicability (Type) (DATA_PRIV_Entity):**
- Data Fiduciary
- Significant Data Fiduciary (SDF)
- Data Processor
- Consent Manager
- Intermediary
- Controller (GDPR)
- Processor (GDPR)
- Joint Controller (GDPR)
- EU Representative (Art. 27)
- Business (CCPA)
- Service Provider / Contractor (CCPA)
- Third Party (CCPA)
- Data Broker
- Body corporate handling SPDI
- All Roles (ALL)

**Due Date & Frequency (DATA_PRIV_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (DATA_PRIV_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Privacy Office (DPO), Information Security, Marketing, Customer Service & Grievance, Product & Engineering. Family additions: Privacy Office (DPO), Information Security, Marketing, Customer Service & Grievance, Product & Engineering.

**Compliance Type (DATA_PRIV_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Notices & Consents. Family additions: Notices & Consents.

**Risk Category (DATA_PRIV_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (DATA_PRIV_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- Data Protection Board of India
- Affected Data Principals (intimation)
- Consent Manager
- CERT-In
- Sectoral Regulator (RBI / SEBI / IRDAI / IFSCA)
- EU / EEA Supervisory Authority (Lead SA)
- Affected Data Subjects (GDPR)
- California Privacy Protection Agency / Attorney General
- Consumers (CCPA notices)
- Board / DPO
- Independent Data Auditor
- Not Required

## 3. Applicability logic for this family

- DPDP obligations commence in phases: Rules 1, 2 and 17–21 from 13 Nov 2025; Rule 4 (Consent Managers) from 13 Nov 2026; Rules 3, 5–16, 22 and 23 from 13 May 2027. Put the commencement date in Conditional Applicability / Exemptions / Thresholds of every row.
- SDF obligations (DPO in India, independent data auditor, periodic DPIA and audit, algorithmic due diligence, data localisation of specified data) apply only on notification as an SDF. Use Type = SDF.
- Sectoral data rules (RBI, SEBI, IRDAI, IFSCA) override or add to DPDP. Write sectoral rows in the sectoral family and cross-reference them here.
- GDPR and CCPA rows apply only where territorial scope tests are met (GDPR Art. 3; CCPA thresholds). Write the test in Conditional Applicability / Exemptions / Thresholds.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Digital Personal Data Protection Act, 2023 and DPDP Rules, 2025 (G.S.R. 846(E), 13 Nov 2025; phased: 13 Nov 2025, 13 Nov 2026, 13 May 2027)
- Information Technology Act, 2000 ss.43A, 72A and IT (Reasonable Security Practices and SPDI) Rules, 2011 (until superseded)
- Regulation (EU) 2016/679 (GDPR)
- California Consumer Privacy Act as amended by CPRA (Cal. Civ. Code §1798.100 et seq.) and CCPA Regulations (2025 rules on risk assessments, cybersecurity audits and ADMT; effective 1 Jan 2026 with later phases) [VERIFY]

## 5. Family-specific pitfalls

- Stating DPDP obligations as already in force before 13 May 2027.
- Using the SPDI Rules after they are superseded [VERIFY].

## 6. File naming

`DATA-PRIV - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Law | DPDP Act and Rules · IT Act and SPDI Rules · EU GDPR · UK GDPR · CCPA / CPRA · Sectoral | Use where a row is written for one law but the sheet records several (cross-law rows). |
| Organisation Role | Data Fiduciary · Significant Data Fiduciary · Data Processor · Consent Manager · Controller · Processor · Business · Service Provider | The role that bears the obligation, where General Applicability (Type) lists several. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-DATA-PRIV-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Privacy Office (DPO) → Breach management / Data principal rights / Notices and consents; Information Security → Security safeguards; Product & Engineering → Privacy by design; Customer Service & Grievance → Grievance redress. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Breach and security rows → Data Privacy; IT & Cyber; notices and consents → Data Privacy; Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | On becoming aware of a personal data breach, has the Data Fiduciary intimated the Data Protection Board without delay and furnished the detailed report within 72 hours? |
| 4 | Clause / Para No. (`clause_ref`) | Rule 7(2), Digital Personal Data Protection Rules, 2025, read with Section 8(6), DPDP Act, 2023 |
| 5 | Department (`department`) | Privacy Office (DPO) |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | MeitY |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Digital Personal Data Protection Rules, 2025 |
| 12 | Instrument Reference No. (`instrument_ref`) | G.S.R. [VERIFY](E) |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 13-Nov-2025 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 13-Nov-2025 |
| 15 | Actionable Last Updated On (`question_updated_date`) | 13-Nov-2025 |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | First issued 13 Nov 2025; Rule 7 commences 13 May 2027. |
| 18 | Source Link (`source_url`) | https://www.meity.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | DPDP Act, 2023 and DPDP Rules, 2025 (India) |
| 20 | General Applicability (Type) (`applic_type`) | Data Fiduciary; Significant Data Fiduciary |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to every Data Fiduciary from 13 May 2027. Intimation to affected Data Principals is a separate row (Rule 7(1)). |
| 22 | Applicable From (`applic_from`) | 13-May-2027 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Law (`ext_*`) | DPDP Act and Rules |
| E2 | Organisation Role (`ext_*`) | Data Fiduciary |
| 24 | Short Title (`short_title`) | Breach - intimation to the Data Protection Board |
| 25 | Interpretation / Explanation (`explanation`) | Two limbs: an initial intimation without delay, and a detailed report within 72 hours (or a longer period the Board allows) covering facts, mitigation, findings on the cause and remedial action. (Abridged.) |
| 26 | Department Function (`dept_function`) | Breach Management |
| 27 | Department Sub-function (`dept_subfunction`) | Board intimation |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 72 hours of becoming aware of the breach |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Personal data breach |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Data Protection Board of India — intimation and detailed report |
| 32 | Portal / Form / Return Code (`filing_form`) | [VERIFY Board portal form] |
| 33 | Related Document / Policy / Committee (`related_docs`) | Personal Data Breach Response Plan; DPO |
| 34 | Reference Weblinks (`weblinks`) | https://www.meity.gov.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Penalty up to ₹200 crore under the Schedule to the DPDP Act for failure to intimate the Board or Data Principals. |
| 36 | Penalty Provision (`penalty_ref`) | Section 33 and Schedule item (5), DPDP Act, 2023 [VERIFY item number] |
| 37 | Risk Type (`risk_type`) | Data Privacy; IT & Cyber |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board intimation acknowledgement with timestamp; detailed report; breach log entry showing awareness time |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Log the time the organisation became aware of the breach. Send the initial intimation to the Board at once. Prepare and submit the detailed report within 72 hours. Coordinate with CERT-In reporting. |
| 42 | Checker Review Points (`checker_points`) | 1. Awareness time recorded. 2. Initial intimation sent without delay. 3. Detailed report within 72 hours and covers every required item. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the breach log. 2. For each breach, compare awareness time to submissions. Exception: late or incomplete report. |
| 44 | Tags / Keywords (`tags`) | personal data breach; dpdp; rule 7; data protection board; 72 hours |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

