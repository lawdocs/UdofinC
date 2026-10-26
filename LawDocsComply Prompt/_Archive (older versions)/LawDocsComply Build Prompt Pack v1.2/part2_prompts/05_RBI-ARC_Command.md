# 05 — RBI-ARC Family Command: Asset Reconstruction Companies

**Template:** `templates/LDC-TPL-RBI-ARC-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-ARC-v2.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_ARC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-RBI-ARC-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — ARC Level.** General Applicability (Layer) separates obligations of the ARC as a company from obligations at the trust/scheme level (SR issuance, trust accounts, NAV declaration, QB disclosures).

**General Applicability (Type) — ARC Type / Activity.** General Applicability (Type) adds activity overlays: resolution applicant under IBC, trustee/manager role, sponsor and FDI structures, listed SRs. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (RBI_ARC_Sector):**
- ARC - Company Level
- ARC - Trust / Scheme Level
- All ARCs

**General Applicability (Type) (RBI_ARC_Entity):**
- ARC (all)
- ARC eligible for additional permitted activities (NOF-based)
- ARC acting as Resolution Applicant (IBC)
- ARC acting as Trustee / Manager of Trusts
- ARC with Sponsor Bank / FI
- ARC with FPI / FDI investment
- Listed ARC / ARC with listed SRs
- Security Receipt (SR) Scheme
- All ARCs (ALL)

**Due Date & Frequency (RBI_ARC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (RBI_ARC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Acquisition & Resolution, Trusteeship & SR Management, Internal Audit, Customer Service & Grievance. Family additions: Acquisition & Resolution, Trusteeship & SR Management, Internal Audit, Customer Service & Grievance.

**Compliance Type (RBI_ARC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (RBI_ARC_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (RBI_ARC_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- CERSAI / CKYCR
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- Credit Rating Agency (SR rating)
- Qualified Buyers / SR holders (disclosure)
- NCLT / IBBI
- DRT / Courts
- SEBI / Stock Exchanges
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- SARFAESI Act ss.3–12 and the RBI ARC directions are the core. Measures under ss.13–15 belong to recovery workflows but carry compliance rows (notice formats, valuation, sale procedure) [INTERP].
- Additional permitted activities depend on the NOF threshold [VERIFY]. Write the threshold in Conditional Applicability / Exemptions / Thresholds.
- SR investment by the transferor bank and provisioning on SRs are bank-side obligations. Put them in RBI-SCB, not here.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Related Document / Policy / Committee "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Wave W2: the principal ARC direction first (XL), then KYC, Credit Information Reporting, Wilful Defaulters, then the DoS Supervisory Returns direction.

- P1 · Reserve Bank of India (Asset Reconstruction Companies – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/375 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Asset Reconstruction Companies – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/377 [confirm reference on document], 28 Nov 2025; updated as on 29 Dec 2025 (RBI page)
- P1 · Reserve Bank of India (Asset Reconstruction Companies – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/469 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Asset Reconstruction Companies) Directions, 2025 — RBI/DOR/2025-26/374 [confirm reference on document], 28 Nov 2025; updated as on 10 Mar 2026 (RBI page)
- P2 · Reserve Bank of India (Asset Reconstruction Companies – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/376 [confirm reference on document], 28 Nov 2025

**Read with:** SARFAESI Act, 2002 (ss. 3, 5, 7, 9, 12, 15) and the Security Interest (Enforcement) Rules, 2002; IBC 2016 where the ARC acts as resolution applicant.

## 5. Family-specific pitfalls

- Ignoring trust-level obligations (separate books per trust, NAV).
- Using the old ₹100 crore NOF figure. RBI has raised it; read the current text [VERIFY].

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` (rev 2)`, ` (rev 3)` *(v1.2: " v2" is now the template version)*. Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*. Record the upload date in catalogue column Z.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| NOF Band | Below ₹300 crore · ₹300 crore to below ₹1,000 crore · ₹1,000 crore and above | Use where the minimum NOF or eligibility for additional permitted activities decides applicability. [VERIFY bands and glide-path dates against the direction.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-RBI-ARC-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Acquisition & Resolution → Acquisition of assets / Resolution plans; Trusteeship & SR Management → SR issuance / NAV declaration / Trust accounts; Finance, Treasury and Accounts → NOF / Capital adequacy; Returns & Reporting → CIMS returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: NOF and capital → Credit / Regulatory; SR investor disclosures → Conduct & Consumer; borrower-facing recovery → Legal; Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Take Name of Master Direction / Regulation and Instrument Reference No. from the catalogue row and the first page of the direction; Issue Date of Instrument = the issue date printed on the direction (28 Nov 2025 for the DoR consolidated set; 31 Jul 2026 for the DoS set; 14 Jan 2026 for the CEPD directions); Instrument Last Amended On = the "Updated as on" date on the RBI page. On a first sheet written from a consolidated direction, rows carried over from withdrawn circulars are **Re-cited** with the old circular and para in Change Note / Previous Actionable; rows changed by a later amendment are **Amended** with the amendment date in Actionable Last Updated On (master §6A).

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the ARC maintained a minimum Net Owned Fund (NOF) of ₹300 crore on an ongoing basis? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], Reserve Bank of India (Asset Reconstruction Companies) Directions, 2025 [VERIFY title] |
| 5 | Department (`department`) | Finance, Treasury and Accounts |
| 6 | Due Date & Frequency (`frequency`) | Ongoing/Continuous |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | RBI – DoR |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Reserve Bank of India (Asset Reconstruction Companies) Directions, 2025 [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | RBI/DOR/2025-26/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 28-Nov-2025 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 28-Nov-2025 — replace with the "Updated as on" date shown on the RBI page |
| 15 | Actionable Last Updated On (`question_updated_date`) | 28-Nov-2025 |
| 16 | Change Status (`change_status`) | Re-cited |
| 17 | Change Note / Previous Actionable (`change_note`) | Re-cited from the RBI review of the regulatory framework for ARCs dated 11 Oct 2022 [VERIFY ref] (withdrawn by RBI/2025-26/100); glide path to ₹300 crore completed [VERIFY]. |
| 18 | Source Link (`source_url`) | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx |
| 19 | General Applicability (Layer) (`applic_layer`) | ARC - Company Level |
| 20 | General Applicability (Type) (`applic_type`) | ARC (all) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to every ARC registered under s.3, SARFAESI Act. [VERIFY any remaining glide-path relaxation.] |
| 22 | Applicable From (`applic_from`) | 28-Nov-2025 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | NOF Band (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Capital - minimum Net Owned Fund |
| 25 | Interpretation / Explanation (`explanation`) | 'Every ARC shall maintain, on an ongoing basis, a minimum NOF of ₹300 crore.' The NOF is computed as defined in the direction (owned funds less specified deductions); a fall below the minimum at any time is a breach and can restrict new acquisitions. (Abridged.) |
| 26 | Department Function (`dept_function`) | Capital Management |
| 27 | Department Sub-function (`dept_subfunction`) | NOF |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Test at the end of each quarter |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | RBI - CIMS (Supervisory Returns) — NOF in the periodic return [VERIFY] |
| 32 | Portal / Form / Return Code (`filing_form`) | [VERIFY return code] |
| 33 | Related Document / Policy / Committee (`related_docs`) | Capital plan; Audit Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the ARC Directions; RBI may cancel the certificate of registration under s.4, SARFAESI Act, or impose a penalty under s.30A [VERIFY]. |
| 36 | Penalty Provision (`penalty_ref`) | Section 30A, SARFAESI Act, 2002 [VERIFY] |
| 37 | Risk Type (`risk_type`) | Credit; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Quarterly NOF computation approved by the CFO; CIMS acknowledgement; auditor certificate on NOF where required [VERIFY] |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Compute NOF at each quarter end using the direction's definition. Have the CFO approve it and report it to the Audit Committee. If NOF is within 10% of the minimum, escalate to the Board with a capital-raising plan. |
| 42 | Checker Review Points (`checker_points`) | 1. NOF computation follows the direction's definition. 2. Figures tie to the balance sheet. 3. NOF ≥ ₹300 crore at each quarter end. 4. Early-warning escalation recorded where needed. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain quarterly NOF computations for the period. 2. Re-perform one computation. 3. Inspect the auditor certificate if required. Exception: any quarter below the minimum. |
| 44 | Tags / Keywords (`tags`) | nof; net owned fund; arc capital; sarfaesi |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

