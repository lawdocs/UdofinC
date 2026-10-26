# 09 — IFSCA-GEN Family Command: IFSCA Regulated Entities (all types)

**Template:** `templates/LDC-TPL-IFSCA-GEN-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-IFSCA-GEN-v2.0` · **Regulator / authority:** International Financial Services Centres Authority · **Named-range prefix:** `IFSCA_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-IFSCA-GEN-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Sector.** General Applicability (Layer) holds the IFSCA sector, exactly as in the owner's existing IFSCA sheets (Banking, Finance Company, Fund Management, Capital Markets, Insurance, Bullion, Payments, FinTech, Ancillary Services, GIC, Education, Trade Finance, Cross-cutting).

**General Applicability (Type) — Entity Type.** General Applicability (Type) holds the IFSCA entity type from the owner's 40-entry list, for example "IFSC Banking Unit (IBU)" or "Recognised Stock Exchange (RSEX); Recognised Clearing Corporation (RCCP); Recognised Depository (RDEP)". Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (IFSCA_Sector):**
- Banking
- Finance Company
- Fund Management
- Capital Markets
- Insurance
- Metals & Commodities (Bullion)
- Payments
- FinTech
- Ancillary Services
- Global In-House Centre
- Education
- Trade Finance
- Cross-cutting / All REs

**General Applicability (Type) (IFSCA_Entity):**
- IFSC Banking Unit (IBU)
- IFSC Banking Company (IBC)
- Finance Company / Finance Unit (FCFU)
- Aircraft Lessor (ACL)
- Ship Lessor (SHL)
- Fund Management Entity (FME)
- Pension Fund (PENF)
- Market Infrastructure Institution (MII)
- Capital Market Intermediary (CMI)
- Recognised Stock Exchange (RSEX)
- Recognised Clearing Corporation (RCCP)
- Recognised Depository (RDEP)
- Broker Dealer / Clearing Member (BDCM)
- Custodian / Depository Participant (CUDP)
- Investment Adviser / Portfolio Manager (IAPM)
- Investment Banker (INVB)
- Distributor (DIST)
- Debenture Trustee (DTEE)
- Credit Rating Agency (CRA)
- Research Entity (RESE)
- ESG Ratings & Data Products Provider (ERDP)
- KYC Registration Agency (KRA)
- Issuer / Listed Entity (ISSU)
- IFSC Insurance Office (IIO)
- IFSC Insurance Intermediary Office (IIIO)
- Insurance Web Aggregator (IWA)
- Managing General Agent (MGA)
- Bullion Exchange / Clearing Corp / Depository (BMII)
- Vault Manager (VM)
- Bullion Trading / Clearing Member (BTCM)
- Payment Service Provider (PSP)
- Payment System Operator (PSO)
- FinTech Entity (FE)
- TechFin Entity (TFIN)
- Ancillary Service Provider (ASP)
- Book-keeping/Accounting/Taxation/FCC Provider (BATF)
- Global In-House Centre (GIC)
- International Branch Campus / Offshore Education Centre (EDU)
- ITFS Platform Operator (ITFS)
- All Regulated Entities (ALL)

**Due Date & Frequency (IFSCA_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time. (Base list only; this family is a byte-exact replica of the owner's IFSCA vocabulary.)

**Department (IFSCA_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management.

**Compliance Type (IFSCA_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (IFSCA_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (IFSCA_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- IFSCA
- IFSCA (prior approval)
- IFSCA (intimation)
- IFSCA / FIU-IND
- Home country regulator (NOC)
- MCA
- RBI (FEMA)
- Central Registry (CERSAI)
- Management
- Not Required

## 3. Applicability logic for this family

- This template is a byte-exact replica of the owner's IFSCA vocabulary, so existing IFSCA sheets remain valid. Continue the established method: one sheet per regulation, handbook, guideline or circular, with the depth of the existing sheets (11–389 rows; mean about 65).
- Use IFSCA-FCFU or IFSCA-FME instead when a finer activity or scheme classification is needed.
- The org egress allowlist blocks ifsca.gov.in from the automation shell. Download source PDFs on the Mac and attach them.

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- IFSCA Act, 2019
- IFSCA (Banking) Regulations, 2020 and Banking Handbook (GEN, COB, PRU)
- IFSCA (Finance Company) Regulations, 2021
- IFSCA (Fund Management) Regulations, 2025 (as amended up to 10 Sep 2026)
- IFSCA (Capital Market Intermediaries) Regulations, 2025; MII Regulations, 2021; Listing Regulations, 2024; KRA Regulations, 2025; Prohibition of Market Abuse Regulations, 2026
- IFSCA insurance regulations (Registration of Insurance Business 2021; Insurance Intermediary 2021; Managing General Agents 2026; Re-insurance 2023; solvency, investment, actuarial and records regulations)
- IFSCA (AML, CFT and KYC) Guidelines, 2022 — master as on 3 Aug 2026
- IFSCA (Payment Services) Regulations, 2024; Bullion Market Regulations, 2025; TechFin and Ancillary Services Regulations, 2025; BATF Regulations, 2024; GIC Regulations, 2025

## 5. Family-specific pitfalls

- Using the old "IFSCA Format for Question Final" vocabulary (it has typos and no named ranges).
- Missing the consolidated "as amended up to" text for FM, Insurance Registration and TechFin.

## 6. File naming

`IFSCA-GEN - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Form of Set-up | Company · Branch · LLP · Trust | Use where the obligation differs by legal form (e.g., net-worth tests for a branch measured at parent level; LLP or trust structures for FMEs and schemes). |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-IFSCA-GEN-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Compliance → KYC & AML / Regulatory compliance / Registration conditions; Returns & Reporting → IFSCA returns; Governance & Administration → KMP and Principal Officer appointments; IT → Cyber security. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: AML rows → Regulatory; Fraud; licensing conditions → Regulatory; client-facing → Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the Regulated Entity appointed a Principal Officer and a Designated Director and communicated their details to FIU-IND and IFSCA? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], IFSCA (Anti Money Laundering, Counter-Terrorist Financing and Know Your Customer) Guidelines, 2022 |
| 5 | Department (`department`) | Compliance |
| 6 | Due Date & Frequency (`frequency`) | Event Based |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | IFSCA |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | IFSCA (Anti Money Laundering, Counter-Terrorist Financing and Know Your Customer) Guidelines, 2022 |
| 12 | Instrument Reference No. (`instrument_ref`) | IFSCA/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | [VERIFY] |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY] |
| 16 | Change Status (`change_status`) | New |
| 17 | Change Note / Previous Actionable (`change_note`) | [VERIFY] instrument dates. |
| 18 | Source Link (`source_url`) | https://www.ifsca.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | Cross-cutting / All REs |
| 20 | General Applicability (Type) (`applic_type`) | All Regulated Entities (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to all IFSCA Regulated Entities that are reporting entities under PMLA. |
| 22 | Applicable From (`applic_from`) | [VERIFY] |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Form of Set-up (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | AML - Principal Officer and Designated Director |
| 25 | Interpretation / Explanation (`explanation`) | The Principal Officer files reports with FIU-IND; the Designated Director is responsible for overall AML compliance. Both appointments, and any change, are communicated to FIU-IND and IFSCA. (Abridged.) |
| 26 | Department Function (`dept_function`) | KYC & AML |
| 27 | Department Sub-function (`dept_subfunction`) | AML governance |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Within [VERIFY] days of the appointment or change |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | Appointment of director / KMP / officer |
| 31 | Filing / Reporting / Intimation (`filing_details`) | IFSCA / FIU-IND — communication of Principal Officer and Designated Director details |
| 32 | Portal / Form / Return Code (`filing_form`) | FIU-IND FINnet 2.0 registration [VERIFY] |
| 33 | Related Document / Policy / Committee (`related_docs`) | AML / CFT Policy; Board |
| 34 | Reference Weblinks (`weblinks`) | https://fiuindia.gov.in |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the IFSCA AML Guidelines and PMLA; action by IFSCA under the IFSCA Act and by FIU-IND under s.13 PMLA. |
| 36 | Penalty Provision (`penalty_ref`) | Section 13, PMLA, 2002; IFSCA Act, 2019 [VERIFY section] |
| 37 | Risk Type (`risk_type`) | Regulatory; Fraud |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board resolution appointing the PO and DD; FIU-IND registration acknowledgement; intimation to IFSCA |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | On appointment or change of the PO or DD, pass a Board resolution, update the FINnet registration and intimate IFSCA. Save both acknowledgements. |
| 42 | Checker Review Points (`checker_points`) | 1. Board resolution names both officers. 2. FINnet registration shows the current PO. 3. IFSCA intimation made within the period. 4. Officers meet the eligibility conditions. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Inspect the resolution, FINnet record and IFSCA intimation. 2. Compare appointment and intimation dates. Exception: missing or late intimation. |
| 44 | Tags / Keywords (`tags`) | principal officer; designated director; aml; ifsca; fiu-ind |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

