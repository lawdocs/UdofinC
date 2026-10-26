# 02 — RBI-UCB Family Command: Urban Co-operative Banks

**Template:** `templates/LDC-TPL-RBI-UCB-v2.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-UCB-v2.0` · **Regulator / authority:** Reserve Bank of India (with RCS / CRCS for registration matters) · **Named-range prefix:** `RBI_UCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-RBI-UCB-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — UCB Tier.** General Applicability (Layer) holds the UCB tier under the revised regulatory framework: Tier 1 to Tier 4 by deposit size, with unit and salary-earners' UCBs in Tier 1. Many prudential provisions (CRAR, exposure limits, director qualifications, branch expansion) differ by tier. Write separate rows per tier.

**General Applicability (Type) — UCB Type / Overlay.** General Applicability (Type) records the structural type (unit, multi-district, multi-State under the MSCS Act), scheduled status, FSWM status, and supervisory overlays (SAF, s.35A All-Inclusive Directions). These change permissions, so use them. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (RBI_UCB_Sector):**
- Tier 1 UCB
- Tier 2 UCB
- Tier 3 UCB
- Tier 4 UCB
- All UCBs

**General Applicability (Type) (RBI_UCB_Entity):**
- Unit UCB (single district)
- Salary Earners' UCB
- Multi-district / State-wide UCB (State Act)
- Multi-State UCB (MSCS Act, 2002)
- Scheduled UCB
- Non-Scheduled UCB
- Financially Sound and Well Managed (FSWM) UCB
- UCB under Supervisory Action Framework (SAF)
- UCB under All-Inclusive Directions (s.35A, BR Act)
- All UCBs (ALL)

**Due Date & Frequency (RBI_UCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Department (RBI_UCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Compliance Type (RBI_UCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Risk Category (RBI_UCB_Risk):** High, Medium, Low.

**Filing / Reporting / Intimation reference list (RBI_UCB_Filing — start the cell with one of these, then optional " — detail". *(v1.2)* The due-date rule goes in Due Date Rule and the form or return code in Portal / Form / Return Code, not in this cell):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- Registrar of Co-operative Societies (State)
- Central Registrar of Co-operative Societies (MSCS)
- NUCFDC (Umbrella Organisation)
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

- Tier is decided by deposits as on 31 March of the previous year [VERIFY tier thresholds in the 2025 UCB directions]. Write a one-time row for tier determination and an annual row for re-determination.
- Matters under the Banking Regulation Act (Part V, s.56) are RBI's. Elections, registration and bye-laws stay with the State Act or the MSCS Act. Those rows go to COOP-GEN / COOP-CCS sheets, not here.
- Board of Management (BoM) requirements apply to UCBs above the deposit threshold set by RBI [VERIFY].
- FSWM status unlocks permissions such as new branches and certain products. Record the FSWM criteria in Conditional Applicability / Exemptions / Thresholds.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.2.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Related Document / Policy / Committee "SUPERSEDES:" and the concordance note (master command §3A).

Each line: priority (P1 first) · title — reference, date of issue; "updated as on" date shown on the RBI page at 25 Oct 2026. Lines marked "[confirm reference on document]" carry a reference derived from RBI's PDF serial; read the first page and confirm before publishing (Appendix AB-D7). Proposed file names, size classes and status are in the catalogue.

**Order.** Wave W2. Clone KYC, RBC, IRACP, Outsourcing, CIR, Credit/Concentration Risk, Investment Portfolio, Financial Statements, Wilful Defaulters and Stressed Assets from the reviewed NBFC sheets; write CRR/SLR, Interest Rate on Deposits, Interest Rates on Advances, Cards, Digital Banking Channels and the Licensing, Scheduling and Regulatory Classification guidelines fresh — they become the lead sheets for the bank families in W3.

- P1 · Reserve Bank of India (Urban Co-operative Banks – Asset Liability Management) Directions, 2025 — RBI/DOR/2025-26/285 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Urban Co-operative Banks – Cash Reserve Ratio and Statutory Liquidity Ratio) Directions, 2025 — RBI/DOR/2025-26/274 [confirm reference on document], 28 Nov 2025; updated as on 09 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Concentration Risk Management) Directions, 2025 — RBI/DOR/2025-26/281 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Credit Facilities) Directions, 2025 — RBI/DOR/2025-26/277 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Credit Information Reporting) Directions, 2025 — RBI/DOR/2025-26/279 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Credit Risk Management) Directions, 2025 — RBI/DOR/2025-26/280 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Financial Statements: Presentation and Disclosures) Directions, 2025 — RBI/DOR/2025-26/289 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Governance) Directions, 2025 — RBI/DOR/2025-26/273 [confirm reference on document], 28 Nov 2025; updated as on 25 May 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Income Recognition, Asset Classification and Provisioning) Directions, 2025 — RBI/DOR/2025-26/286 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Know Your Customer) Directions, 2025 — RBI/DOR/2025-26/291 [confirm reference on document], 28 Nov 2025; updated as on 18 Sep 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Managing Risks in Outsourcing) Directions, 2025 — RBI/DOR/2025-26/293 [confirm reference on document], 28 Nov 2025
- P1 · Reserve Bank of India (Urban Co-operative Banks – Prudential Norms on Capital Adequacy) Directions, 2025 — RBI/DOR/2025-26/275 [confirm reference on document], 28 Nov 2025; updated as on 16 Jun 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Responsible Business Conduct) Directions, 2025 — RBI/DOR/2025-26/292 [confirm reference on document], 28 Nov 2025; updated as on 01 Jul 2026 (RBI page)
- P1 · Reserve Bank of India (Urban Co-operative Banks – Compliance Function) Directions, 2026 — RBI/DoS/2026-27/435 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Concurrent Audit) Directions, 2026 — RBI/DoS/2026-27/436 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Cybersecurity, Technology: Risk, Resilience and Assurance Framework) Directions, 2026 — RBI/DoS/2026-27/437 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Digital Payment Security Controls) Directions, 2026 — RBI/DoS/2026-27/438 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Fraud Risk Management) Directions, 2026 — RBI/DoS/2026-27/439 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Internal Audit Function) Directions, 2026 — RBI/DoS/2026-27/440 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Miscellaneous) Supervisory Directions, 2026 — RBI/DoS/2026-27/443 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Statutory Audit) Directions, 2026 — RBI/DoS/2026-27/441 [confirm reference on document], 31 Jul 2026
- P1 · Reserve Bank of India (Urban Co-operative Banks – Supervisory Returns) Directions, 2026 — RBI/DoS/2026-27/442 [confirm reference on document], 31 Jul 2026
- P2 · Reserve Bank of India (Urban Co-operative Banks – Branch Authorisation) Directions, 2025 — RBI/DOR/2025-26/271 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Classification, Valuation and Operation of Investment Portfolio) Directions, 2025 — RBI/DOR/2025-26/284 [confirm reference on document], 28 Nov 2025; updated as on 02 Sep 2026 (RBI page)
- P2 · Reserve Bank of India (Urban Co-operative Banks – Credit Cards and Debit Cards: Issuance and Conduct) Directions, 2025 — RBI/DOR/2025-26/278 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Interest Rate on Deposits) Directions, 2025 — RBI/DOR/2025-26/276 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Urban Co-operative Banks – Interest Rates on Advances) Directions, 2025 — RBI/DOR/2025-26/283 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Miscellaneous) Directions, 2025 — RBI/DOR/2025-26/294 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Prudential Norms on Declaration of Dividends) Directions, 2025 — RBI/DOR/2025-26/290 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Resolution of Stressed Assets) Directions, 2025 — RBI/DOR/2025-26/287 [confirm reference on document], 28 Nov 2025; updated as on 01 Oct 2026 (RBI page)
- P2 · Reserve Bank of India (Urban Co-operative Banks – Transfer and Distribution of Credit Risk) Directions, 2025 — RBI/DOR/2025-26/282 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Treatment of Wilful Defaulters and Large Defaulters) Directions, 2025 — RBI/DOR/2025-26/288 [confirm reference on document], 28 Nov 2025
- P2 · Reserve Bank of India (Urban Co-operative Banks – Undertaking of Financial Services) Directions, 2025 — RBI/DOR/2025-26/272 [confirm reference on document], 28 Nov 2025; updated as on 05 Oct 2026 (RBI page)
- P3 · Reserve Bank of India (Urban Co-operative Banks – Digital Banking Channels Authorisation) Directions, 2025 — RBI/DOR/2025-26/385 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Urban Co-operative Banks – Licensing, Scheduling and Regulatory Classification) Guidelines, 2025 — RBI/DOR/2025-26/269 [confirm reference on document], 28 Nov 2025
- P3 · Reserve Bank of India (Urban Co-operative Banks – Voluntary Amalgamation) Directions, 2025 — RBI/DOR/2025-26/270 [confirm reference on document], 28 Nov 2025

**Read with:** Banking Regulation Act, 1949 as applicable to co-operative societies (s.56); the State Co-operative Societies Act or MSCS Act 2002 for corporate matters (P16 handles society affairs); RB-IOS 2026 coverage for UCBs [VERIFY].

## 5. Family-specific pitfalls

- Applying commercial-bank Basel III rows to UCBs. UCBs follow their own capital framework.
- Writing State co-operative law obligations (AGM, elections) in a UCB RBI sheet. Use the COOP families instead.
- Forgetting Tier-specific CRAR minimums and director-qualification rules.

## 6. File naming *(v1.1)*

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions v2.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` (rev 2)`, ` (rev 3)` *(v1.2: " v2" is now the template version)*. Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*. Record the upload date in catalogue column Z.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| Registration (State / Multi-State) | State-registered UCB (State Co-operative Societies Act) · Multi-State UCB (MSCS Act, 2002) | Use where the paragraph or the parallel registrar obligation differs by registration law (registrar filings, elections, audit appointment). |
| Deposit Band | Up to ₹100 crore · Above ₹100 crore up to ₹1,000 crore · Above ₹1,000 crore up to ₹10,000 crore · Above ₹10,000 crore | Use where a threshold inside a tier decides applicability (for example the Board of Management threshold). State the exact test and the reference date in Conditional Applicability. [VERIFY bands against the tier definitions in the consolidated direction.] |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-RBI-UCB-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Governance & Administration → Board & Committees / Board of Management; Credit → Exposure limits / Priority sector; KYC & AML → CDD / STR; Finance, Treasury and Accounts → CRAR / CRR-SLR; Returns & Reporting → CIMS returns / Registrar returns. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: Prudential rows → Credit / Liquidity; governance and BoM rows → Governance; member-facing rows → Conduct & Consumer. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Take Name of Master Direction / Regulation and Instrument Reference No. from the catalogue row and the first page of the direction; Issue Date of Instrument = the issue date printed on the direction (28 Nov 2025 for the DoR consolidated set; 31 Jul 2026 for the DoS set; 14 Jan 2026 for the CEPD directions); Instrument Last Amended On = the "Updated as on" date on the RBI page. On a first sheet written from a consolidated direction, rows carried over from withdrawn circulars are **Re-cited** with the old circular and para in Change Note / Previous Actionable; rows changed by a later amendment are **Amended** with the amendment date in Actionable Last Updated On (master §6A).

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the UCB constituted a Board of Management (BoM) with the composition, member qualifications and tenure required by the direction? |
| 4 | Clause / Para No. (`clause_ref`) | Para [VERIFY], Reserve Bank of India (Urban Co-operative Banks – Governance) Directions, 2025 [VERIFY title] |
| 5 | Department (`department`) | Governance & Administration |
| 6 | Due Date & Frequency (`frequency`) | Ongoing/Continuous |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | RBI – DoR |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Reserve Bank of India (Urban Co-operative Banks – Governance) Directions, 2025 [VERIFY exact title] |
| 12 | Instrument Reference No. (`instrument_ref`) | RBI/DOR/2025-26/[VERIFY] |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 28-Nov-2025 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | 28-Nov-2025 — replace with the "Updated as on" date shown on the RBI page |
| 15 | Actionable Last Updated On (`question_updated_date`) | 28-Nov-2025 |
| 16 | Change Status (`change_status`) | Re-cited |
| 17 | Change Note / Previous Actionable (`change_note`) | Re-cited from RBI circular on Board of Management in UCBs dated 31 Dec 2019 [VERIFY ref] (withdrawn by RBI/2025-26/100); substance unchanged. |
| 18 | Source Link (`source_url`) | https://www.rbi.org.in/Scripts/BS_ViewMasterDirections.aspx |
| 19 | General Applicability (Layer) (`applic_layer`) | Tier 2 UCB; Tier 3 UCB; Tier 4 UCB |
| 20 | General Applicability (Type) (`applic_type`) | All UCBs (ALL) |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Applies to UCBs with deposits of ₹100 crore and above [VERIFY threshold and reference date]. UCBs below the threshold may constitute a BoM voluntarily. |
| 22 | Applicable From (`applic_from`) | 28-Nov-2025 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | Registration (State / Multi-State) (`ext_*`) | (blank — not a deciding factor here) |
| E2 | Deposit Band (`ext_*`) | Above ₹100 crore up to ₹1,000 crore; Above ₹1,000 crore up to ₹10,000 crore; Above ₹10,000 crore |
| 24 | Short Title (`short_title`) | Board of Management - constitution and composition |
| 25 | Interpretation / Explanation (`explanation`) | The BoM is a professional body separate from the elected Board that oversees banking functions. Three points govern: minimum and maximum members, the professional qualification of members, and the fit-and-proper declaration. A BoM that exists on paper but does not meet, or whose members lack the prescribed qualifications, does not satisfy the para. (Abridged.) |
| 26 | Department Function (`dept_function`) | Board & Committees |
| 27 | Department Sub-function (`dept_subfunction`) | Committee constitution |
| 28 | Compliance Type (`compliance_type`) | Committee |
| 29 | Due Date Rule (`due_rule`) | Review composition at the end of each quarter and within 30 days of any vacancy [VERIFY vacancy period] |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | RBI (intimation) — BoM constitution and changes [VERIFY whether intimation is required] |
| 32 | Portal / Form / Return Code (`filing_form`) | (blank) |
| 33 | Related Document / Policy / Committee (`related_docs`) | Board resolution constituting the BoM; Fit and proper declarations; Bye-laws |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Breach of the Governance Directions; RBI may issue directions, supersede the Board or impose a monetary penalty under s.47A read with s.56, BR Act. |
| 36 | Penalty Provision (`penalty_ref`) | Section 47A read with Section 56, Banking Regulation Act, 1949 |
| 37 | Risk Type (`risk_type`) | Governance; Regulatory |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Board resolution constituting the BoM; list of BoM members with qualifications; fit and proper declarations; BoM meeting minutes for the period |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Keep a register of BoM members with their qualification, appointment date and tenure. Check composition at each quarter end and after every vacancy. Put any shortfall to the Board within 30 days with a proposal to fill it. File the declarations in the BoM folder. |
| 42 | Checker Review Points (`checker_points`) | 1. BoM size is within the prescribed range. 2. Each member holds a qualification listed in the direction. 3. Fit and proper declarations are current. 4. Vacancies were filled within the period allowed. 5. BoM met at the prescribed frequency. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Obtain the BoM register and minutes for the audit period. 2. Inspect qualification proofs for all members. 3. Compare vacancy dates to filling dates; any gap beyond the limit is an exception. 4. Inspect evidence that BoM recommendations reached the Board. |
| 44 | Tags / Keywords (`tags`) | board of management; bom; ucb governance; professional directors |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

