# 22 — CYBER Family Command: Cyber Security and IT Governance

**Template:** `templates/LDC-TPL-CYBER-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-CYBER-v2.0` · **Regulator / authority:** CERT-In / MeitY; sectoral regulators (RBI, SEBI, IRDAI, IFSCA) · **Named-range prefix:** `CYBER_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-CYBER-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Framework.** General Applicability (Layer) holds the framework (CERT-In Directions, IT Act s.70/NCIIPC, RBI IT/cyber directions, SEBI CSCRF, IRDAI guidelines, IFSCA guidelines, DPDP Rule 6, ISO 27001, NIST CSF, PCI DSS).

**General Applicability (Type) — Entity Category.** General Applicability (Type) holds the entity category that changes the requirement (all body corporates, data centre/cloud/VPN providers, CII, bank, NBFC by layer, UCB by tier, SEBI CSCRF categories, insurer, IFSCA RE, payment entity). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (CYBER_Sector):**
- CERT-In Directions, 2022 (IT Act s.70B)
- IT Act s.70 / NCIIPC (CII / Protected Systems)
- RBI IT and Cyber Security Directions
- SEBI CSCRF
- IRDAI Information and Cyber Security Guidelines, 2023
- IFSCA Cyber Security Guidelines
- DPDP security safeguards (Rule 6)
- ISO/IEC 27001:2022
- NIST CSF 2.0
- PCI DSS v4.0.1
- All Frameworks

**General Applicability (Type) (CYBER_Entity):**
- All body corporates / service providers
- Data centre / cloud / VPS / VPN provider
- Critical Information Infrastructure / Protected System
- Bank
- NBFC (by layer)
- UCB (by tier)
- SEBI MII
- SEBI Qualified RE
- SEBI Mid-size RE
- SEBI Small-size RE
- SEBI Self-certification RE
- Insurer / Insurance Intermediary
- IFSCA Regulated Entity
- Payment entity (card data)
- All (ALL)

**Due Date & Frequency (CYBER_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (CYBER_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Information Security, IT Infrastructure, Application Development, Business Continuity. Family additions: Information Security, IT Infrastructure, Application Development, Business Continuity.

**Compliance Type (CYBER_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (CYBER_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (CYBER_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- CERT-In (incident report)
- NCIIPC
- RBI (CSITE / Department of Supervision)
- SEBI (CSCRF reporting / SI Portal)
- IRDAI
- IFSCA
- Stock Exchanges / Depositories (MIIs)
- Data Protection Board of India
- Board / IT Strategy Committee
- CISO / Information Security Steering Committee
- Auditor (CERT-In empanelled)
- Not Required

## 3. Applicability logic for this family

- Statutory rows (CERT-In, NCIIPC, DPDP) are Compliance. ISO, NIST and PCI rows are "Suggestive Compliance" unless a regulator or contract mandates them.
- Write sector cyber directions here only where the owner wants a single cyber view. Otherwise put them in the sector family and cross-reference.
- Log retention (180 days in India), NTP synchronisation, and incident reporting within 6 hours are key CERT-In rows.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- CERT-In Directions No. 20(3)/2022-CERT-In dated 28 Apr 2022 and FAQs
- IT Act, 2000 ss.43, 66, 70, 70A, 70B, 72A; IT (CERT-In and manner of performing functions) Rules, 2013
- RBI cyber/IT directions for banks, UCBs and NBFCs (incl. RBI (NBFC – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026, RBI/DoS/2026-27/461) [VERIFY]
- SEBI CSCRF (20 Aug 2024) and clarifications
- IRDAI Information and Cyber Security Guidelines, 2023
- IFSCA cyber security guidelines (effective 1 Apr 2025) [VERIFY]
- ISO/IEC 27001:2022; NIST CSF 2.0; PCI DSS v4.0.1 (Suggestive Compliance unless contractually required)

## 5. Family-specific pitfalls

- Making ISO controls mandatory rows.
- Missing the 180-day log retention and NTP rows.

## 6. File naming

`CYBER - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Framework | CERT-In Directions 2022 · RBI IT / cyber directions · SEBI CSCRF · IRDAI guidelines · IFSCA guidelines · ISO/IEC 27001 · NIST CSF 2.0 · PCI DSS | Use where one control row satisfies several frameworks; list all, primary first. |
| Control Domain | Governance · Identify · Protect · Detect · Respond · Recover · Third-party · Data security · Logging and monitoring | The control domain the row belongs to; used to group cyber rows for the CISO. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-CYBER-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Information Security → Incident response / Logging / Access control / VAPT; IT Infrastructure → Time synchronisation / Backups; Business Continuity → BCP / DR drills; Governance & Administration → IT Strategy Committee. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: IT & Cyber primary on every row; add Third-party for vendor controls and Data Privacy for data-security controls. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the entity reported every cyber incident of the types listed in Annexure I to CERT-In within 6 hours of noticing it or being brought to notice? |
| 4 | Clause / Para No. (`clause_ref`) | Direction (ii), CERT-In Directions under Section 70B(6), IT Act, 2000, dated 28 April 2022 |
| 5 | Department (`department`) | Information Security |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | CERT-In |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Directions under sub-section (6) of section 70B of the Information Technology Act, 2000 relating to information security practices, procedure, prevention, response and reporting of cyber incidents |
| 12 | Instrument Reference No. (`instrument_ref`) | No. 20(3)/2022-CERT-In |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 28-Apr-2022 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 28-Apr-2022 |
| 15 | Actionable Last Updated On (`question_updated_date`) | 28-Apr-2022 |
| 16 | Change Status (`change_status`) | Unchanged |
| 17 | Change Note / Previous Actionable (`change_note`) | Read with CERT-In FAQs of 18 May 2022 [VERIFY]. |
| 18 | Source Link (`source_url`) | https://www.cert-in.org.in |
| 19 | General Applicability (Layer) (`applic_layer`) | CERT-In Directions, 2022 (IT Act s.70B) |
| 20 | General Applicability (Type) (`applic_type`) | All body corporates / service providers |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to service providers, intermediaries, data centres, body corporates and Government organisations. |
| 22 | Applicable From (`applic_from`) | 28-Jun-2022 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Framework (`ext_*`) | CERT-In Directions 2022; RBI IT / cyber directions; SEBI CSCRF |
| E2 | Control Domain (`ext_*`) | Respond |
| 24 | Short Title (`short_title`) | Incident reporting - CERT-In within 6 hours |
| 25 | Interpretation / Explanation (`explanation`) | The 6-hour clock starts on noticing the incident. Reporting to sectoral regulators runs in parallel. (Abridged.) |
| 26 | Department Function (`dept_function`) | Incident Response |
| 27 | Department Sub-function (`dept_subfunction`) | Regulatory incident reporting |
| 28 | Compliance Type (`compliance_type`) | Returns & Reporting |
| 29 | Due Date Rule (`due_rule`) | Within 6 hours of noticing the incident |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Cyber or data security incident detected |
| 31 | Filing / Reporting / Intimation (`filing_details`) | CERT-In (incident report) — incident@cert-in.org.in / portal |
| 32 | Portal / Form / Return Code (`filing_form`) | CERT-In incident reporting form |
| 33 | Related Document / Policy / Committee (`related_docs`) | Cyber Crisis Management Plan; CISO |
| 34 | Reference Weblinks (`weblinks`) | https://www.cert-in.org.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Punishment under s.70B(7), IT Act (imprisonment up to one year or fine up to ₹1 lakh, or both). |
| 36 | Penalty Provision (`penalty_ref`) | Section 70B(7), Information Technology Act, 2000 |
| 37 | Risk Type (`risk_type`) | IT & Cyber; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | CERT-In acknowledgement with timestamp; incident ticket showing detection time |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Record the detection time in the incident ticket. Classify against Annexure I. Report to CERT-In within 6 hours and to the sectoral regulator as required. Save the acknowledgement. |
| 42 | Checker Review Points (`checker_points`) | 1. Detection and report times recorded. 2. Report ≤ 6 hours. 3. Classification against Annexure I documented. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the incident register. 2. For every reportable incident, compare times. Exception: report beyond 6 hours or unreported incident. |
| 44 | Tags / Keywords (`tags`) | cert-in; incident reporting; 6 hours; section 70b |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

