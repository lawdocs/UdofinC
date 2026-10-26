# 03 — RBI-RCB Family Command: Rural Co-operative Banks (StCBs and DCCBs)

**Template:** `templates/LDC-TPL-RBI-RCB-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-RCB-v2.0` · **Regulator / authority:** Reserve Bank of India (regulation); NABARD (supervision) · **Named-range prefix:** `RBI_RCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-RBI-RCB-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — RCB Category.** General Applicability (Layer) distinguishes State Co-operative Banks from District Central Co-operative Banks.

**General Applicability (Type) — RCB Type / Overlay.** General Applicability (Type) adds scheduled status and supervisory overlays. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (RBI_RCB_Sector):**
- State Co-operative Bank (StCB)
- District Central Co-operative Bank (DCCB)
- All Rural Co-operative Banks

**General Applicability (Type) (RBI_RCB_Entity):**
- StCB - Scheduled
- StCB - Non-Scheduled
- DCCB
- RCB under Supervisory Action / s.35A Directions
- RCB with CBS / Shared Service Entity arrangement
- All RCBs (ALL)

**Due Date & Frequency (RBI_RCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (RBI_RCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Compliance Type (RBI_RCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (RBI_RCB_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (RBI_RCB_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- NABARD (ENSURE)
- NABARD (Department of Supervision)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- Registrar of Co-operative Societies (State)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- DICGC
- General Body / Members
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- RBI regulates rural co-operative banks under the BR Act. NABARD supervises them and receives most returns (ENSURE portal) [VERIFY current portal per return].
- PACS are not banks. Put PACS obligations in COOP-CCS.
- Where a direction says "StCBs and DCCBs", use Layer = "All Rural Co-operative Banks".

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Related Document / Policy / Committee "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Wave W2, after the UCB set (clone from UCB where the subject exists). Supervision of StCBs and DCCBs rests largely with NABARD; RBI issued only three DoS directions for RCBs.

- P1 · Reserve Bank of India (Rural Co-operative Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/310 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/299 [confirm reference on document], 28 Nov 2025; updated as on 25 Aug 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/306 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/302 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/304 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/305 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/314 [confirm reference on document], 28 Nov 2025; updated as on 01 Apr 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/298 [confirm reference on document], 28 Nov 2025; updated as on 25 May 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/311 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/316 [confirm reference on document], 28 Nov 2025; updated as on 18 Sep 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/318 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Rural Co-operative Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/300 [confirm reference on document], 28 Nov 2025; updated as on 15 May 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/317 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Rural Co-operative Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/451 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Rural Co-operative Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/453 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Rural Co-operative Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/452 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Rural Co-operative Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/296 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/309 [confirm reference on document], 28 Nov 2025; updated as on 18 May 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/303 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/301 [confirm reference on document], 28 Nov 2025; updated as on 25 Aug 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/308 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/319 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Prudential Norms on Declaration of Dividends) Directions, 2025 — RBI/DOR/2025-26/315 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/312 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Rural Co-operative Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/307 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/313 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Rural Co-operative Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/297 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Rural Co-operative Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/386 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Rural Co-operative Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/295 [confirm reference on document], 28 Nov 2025

**Read with:** Banking Regulation Act, 1949 (s.56); NABARD supervisory instructions (cite in Related Document / Policy / Committee or Filing / Reporting / Intimation where they set the reporting route) [VERIFY current NABARD circulars]; State Co-operative Societies Acts.

## 5. Family-specific pitfalls

- Citing UCB directions for RCBs. The 2025 sets are separate.
- Missing the NABARD filing route in Filing / Reporting / Intimation.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` (rev 2)`, ` (rev 3)` *(v1.2: " v2" is now the template version)*. Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*. Record the upload date in catalogue column Z.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Tier (StCB / DCCB) | State Co-operative Bank (StCB) · District Central Co-operative Bank (DCCB) | Use where the paragraph differs between StCBs and DCCBs within the same direction; otherwise leave blank and rely on General Applicability (Layer). |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-RBI-RCB-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Finance, Treasury and Accounts → Capital adequacy / CRR-SLR; Credit → Exposure limits / Agricultural credit; Returns & Reporting → NABARD (ENSURE) returns; Compliance → Registrar correspondence. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Capital and liquidity rows → Credit / Liquidity; NABARD reporting → Regulatory. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Take Name of Master Direction / Regulation and Instrument Reference No. from the catalogue row and the first page of the direction; Issue Date of Instrument = the issue date printed on the direction (28 Nov 2025 for the DoR consolidated set; 31 Jul 2026 for the DoS set; 14 Jan 2026 for the CEPD directions); Instrument Last Amended On = the "Updated as on" date on the RBI page. On a first sheet written from a consolidated direction, rows carried over from withdrawn circulars are **Re-cited** with the old circular and para in Change Note / Previous Actionable; rows changed by a later amendment are **Amended** with the amendment date in Actionable Last Updated On (master §6A).

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the RCB maintained a minimum Capital to Risk-weighted Assets Ratio (CRAR) of 9% on an ongoing basis? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], Reserve Bank of India (Rural Co-operative Banks – Capital Adequacy) Directions, 2025 [VERIFY title] |
| 5 | Department (`department`) | Finance, Treasury and Accounts |
| 6 | Due Date & Frequency (`frequency`) | Ongoing/Continuous |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | RBI – DoR |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Reserve Bank of India (Rural Co-operative Banks – Capital Adequacy) Directions, 2025 [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | RBI/DOR/2025-26/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 28-Nov-2025 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 28-Nov-2025 — replace with the "Updated as on" date shown on the RBI page |
| 15 | Actionable Last Updated On (`question_updated_date`) | 28-Nov-2025 |
| 16 | Change Status (`change_status`) | Re-cited |
| 17 | Change Note / Previous Actionable (`change_note`) | Re-cited from the RBI capital adequacy circulars for StCBs and DCCBs [VERIFY refs] (withdrawn by RBI/2025-26/100); minimum CRAR unchanged at 9% [VERIFY]. |
| 18 | Source Link (`source_url`) | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx |
| 19 | General Applicability (Layer) (`applic_layer`) | All Rural Co-operative Banks |
| 20 | General Applicability (Type) (`applic_type`) | All RCBs (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to all StCBs and DCCBs. |
| 22 | Applicable From (`applic_from`) | 28-Nov-2025 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Tier (StCB / DCCB) (`ext_*`) | (blank — not a deciding factor here) |
| 24 | Short Title (`short_title`) | Capital adequacy - minimum CRAR |
| 25 | Interpretation / Explanation (`explanation`) | '…shall maintain a minimum CRAR of 9 per cent on an ongoing basis.' The test applies at all times, not only at the year end; a dip at any quarter end is a breach even if restored later. (Abridged.) |
| 26 | Department Function (`dept_function`) | Capital Management |
| 27 | Department Sub-function (`dept_subfunction`) | Capital adequacy |
| 28 | Compliance Type (`compliance_type`) | Compliance |
| 29 | Due Date Rule (`due_rule`) | Test at the end of each quarter |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | NABARD (ENSURE) — CRAR in the periodic return [VERIFY return] |
| 32 | Portal / Form / Return Code (`filing_form`) | [VERIFY NABARD return code] |
| 33 | Related Document / Policy / Committee (`related_docs`) | ICAAP / capital plan; Audit Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the Capital Adequacy Directions; supervisory action by RBI / NABARD including restrictions on business; monetary penalty under s.47A read with s.56, BR Act. |
| 36 | Penalty Provision (`penalty_ref`) | Section 47A read with Section 56, Banking Regulation Act, 1949 |
| 37 | Risk Type (`risk_type`) | Credit; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Quarterly CRAR computation approved by the CFO; ENSURE submission acknowledgement; Board note on capital position |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Compute CRAR at each quarter end from the trial balance and the risk-weight schedule. Have the computation reviewed by the CFO and placed before the Audit Committee. Escalate to the Board with a capital plan if CRAR falls within 1 percentage point of the minimum. |
| 42 | Checker Review Points (`checker_points`) | 1. CRAR computation ties to the audited / reviewed trial balance. 2. Risk weights match the direction's schedule. 3. CRAR ≥ 9% at every quarter end. 4. Early-warning escalation was made where required. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the four quarterly CRAR computations for the year. 2. Re-perform one quarter in full. 3. Trace capital elements to the balance sheet. 4. Any quarter below 9% is an exception. |
| 44 | Tags / Keywords (`tags`) | crar; capital adequacy; stcb; dccb; nabard |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

