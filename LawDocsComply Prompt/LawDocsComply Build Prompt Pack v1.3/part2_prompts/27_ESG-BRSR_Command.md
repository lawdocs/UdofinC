# 27 — ESG-BRSR Family Command: ESG, BRSR / BRSR Core, CSR and GHG *(v1.1)*

**Template:** `templates/LDC-TPL-ESG-BRSR-v2.0 - ESG BRSR and CSR.xlsx` · **Template code:** `LDC-TPL-ESG-BRSR-v2.0` · **Regulator / authority:** SEBI; MCA; stock exchanges; RBI (climate-related financial risk); voluntary standards bodies (ISSB, GHG Protocol, GRI); EU (CSRD/ESRS) for EU-facing groups · **Named-range prefix:** `ESG_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. The importer blocks any row that still carries `[VERIFY]`.

**Why this family exists.** Sustainability reporting has become a statutory disclosure for the top 1,000 listed entities (BRSR, with BRSR Core assurance phased in), CSR is a statutory spend-and-report obligation for every company above the s.135 thresholds, and RBI-regulated lenders face climate-risk disclosure expectations. This family turns those obligations into checkpoints that feed the ESG module (P27) and the BRSR drafting workflow. It is an overlay (`OV_ESG`) that attaches to the MCA-CO, SEBI-LISTED and RBI families (P15).

**v1.2 changes** *(v1.2)* — Rewritten for template contract v2.0 (`LDC-TPL-ESG-BRSR-v2.0`, sheet `Compliance Register`, 62 base columns read by header and machine key; v1.0 sheets still import through the legacy map, see `00A_Migrating_v1_Sheets_to_v2.md`). Column letters replaced by header names; `Lists` replaces `Rough`; due-date rules move to Due Date Rule and form codes to Portal / Form / Return Code; new §7 adds this family's extension columns, Department Function / Sub-function and Risk Type guidance, and a complete v2.0 example row; file names end "- Compliance Questions v2.xlsx". The family lists in the v2.0 template's `Lists` sheet are authoritative where they differ from this file.

## 1. How General Applicability (Layer) and (Type) work in this family *(v1.2: formerly Columns C and D)*

**General Applicability (Layer) — Framework / Instrument.** The instrument the checkpoint comes from. Where one control satisfies several frameworks (for example, a Scope 1 and 2 emissions inventory satisfies BRSR Principle 6, BRSR Core and ISSB IFRS S2), write the row once under the binding Indian instrument and list the others in Related Document / Policy / Committee ("Also satisfies: …").

**General Applicability (Type) — Entity category.** The category that triggers the obligation: market-cap tier for BRSR and BRSR Core (top 1,000; top 250 for value-chain disclosures), the s.135 threshold for CSR, the RE category for climate risk. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Lists` sheet) *(v1.2: `Lists` replaces `Rough`)*

**General Applicability (Layer) (ESG_Sector):** SEBI LODR Reg 34(2)(f) - BRSR · SEBI BRSR Core and Assurance · SEBI BRSR Value Chain Disclosures · SEBI ESG Rating Providers and ESG Debt / ESG Schemes · Companies Act 2013 s.135 and CSR Rules 2014 · Companies Act 2013 Board Report (s.134) sustainability items · RBI Climate-related Financial Risk · GHG Protocol (Scope 1, 2 and 3) · ISSB IFRS S1 and S2 · EU CSRD / ESRS (EU-facing groups) · Board-approved internal ESG / Sustainability Policy · All Frameworks

**General Applicability (Type) (ESG_Entity):** Listed entity - Top 1000 by market capitalisation · Listed entity - Top 250 (value-chain scope) · Listed entity - other (voluntary BRSR) · Company meeting s.135 CSR thresholds · Company with CSR obligation below Rs 50 lakh (no CSR Committee required) · Regulated Entity - Bank / NBFC / UCB (RBI climate risk) · Asset Management Company / ESG scheme · Issuer of green / ESG debt securities · Unlisted company - voluntary sustainability reporting · Group with EU operations (CSRD scope) · All Entities (ALL)

**Department (ESG_Dept):** the nine base departments plus Secretarial, Investor Relations, Administration & Facilities, Internal Audit (codes per Appendix U §U.9.0).

**Compliance Type (ESG_CompType):** the six base types plus *Disclosures* (code `DISCLOSURES`).

**Filing / Reporting / Intimation (ESG_Filing, reference):** Stock exchange (BRSR as part of Annual Report) · MCA (CSR-2 / AOC-4) · SEBI · RBI · Annual Report disclosure · Board / CSR Committee · Reasonable assurance provider · Website disclosure · Not Required

## 3. Applicability and status logic for this family

1. **BRSR.** Mandatory for the top 1,000 listed entities by market capitalisation (computed as on 31 March); write the tier in Conditional Applicability / Exemptions / Thresholds. Others may report voluntarily; such rows use Compliance Type = *Suggestive Compliance*.
2. **BRSR Core assurance and value chain.** Follow SEBI's circular of 28 March 2025: assurance or assessment of BRSR Core phased by market-cap tier; value-chain disclosures voluntary from FY 2025-26 for the top 250, covering partners above 2% of purchases or sales [VERIFY paragraph numbers and the phase-in table before writing]. The owner baseline's "75% value-chain boundary" is superseded.
3. **CSR.** Applies to a company with net worth ≥ ₹500 crore, turnover ≥ ₹1,000 crore or net profit ≥ ₹5 crore in the immediately preceding financial year (s.135(1)). Write separate rows for: CSR Committee (not required where the obligation is ≤ ₹50 lakh, s.135(9)); CSR policy and annual action plan; 2% spend computed on average net profit (s.198) of the three preceding years; unspent amounts (ongoing projects → Unspent CSR Account within 30 days of year-end, spend within three years; other amounts → Schedule VII fund within six months); impact assessment where the average obligation is ≥ ₹10 crore and project outlay ≥ ₹1 crore; CSR-2 filing; Board-report annexure; website disclosure.
4. **RBI climate risk.** Until RBI finalises the climate-related financial risk disclosure framework [VERIFY status], rows use Compliance Type = *Suggestive Compliance* and Conditions = "Draft; becomes binding on final issue".
5. **Figures.** GHG and other numeric checkpoints ask *whether the data were computed, reviewed and disclosed*; LDC's ESG module computes figures through versioned emission-factor rule packs. The sheet never contains figures (NN-37).

## 4. Instruments to cover (one sheet per instrument)

1. SEBI (LODR) Regulations 2015 — Reg 34(2)(f) and the BRSR format.
2. SEBI circular on BRSR Core, ESG disclosures for value chain and assurance (28 Mar 2025) and earlier BRSR Core circulars [VERIFY].
3. SEBI framework for ESG rating providers and ESG debt securities / ESG schemes of mutual funds (applicable categories only).
4. Companies Act 2013 s.135, Schedule VII and Companies (CSR Policy) Rules 2014 as amended; Form CSR-2.
5. Companies Act 2013 s.134(3)(m) with Companies (Accounts) Rules 2014 r.8(3) — energy conservation and technology absorption.
6. RBI disclosure framework on climate-related financial risks (draft 2024 or final) [VERIFY].
7. GHG Protocol Corporate Standard and Scope 3 Standard (methodology rows for tenants that adopt it).
8. ISSB IFRS S1 and S2 and EU CSRD/ESRS — only for tenants with foreign-group reporting (D-19 jurisdiction packs).

## 5. Family-specific pitfalls

- Writing a single "prepare BRSR" row. Split by section and principle (Section A general disclosures, Section B management and process, Section C nine principles with essential and leadership indicators), and split BRSR Core KPIs one per row.
- Mixing the CSR spend computation with the reporting obligation — keep computation (s.198 net profit), spend, unspent transfer and reporting as separate rows with their own evidence.
- Treating draft RBI climate expectations as binding.
- Using the superseded 75% value-chain boundary.
- Evidence must be concrete: Board/CSR Committee minutes, CSR policy, annual action plan, CSR-2 acknowledgement, Unspent CSR Account statement, impact-assessment report, emissions inventory with factor version, assurance report.

## 6. File naming

`ESG-BRSR - <Instrument short title> <Year> - Compliance Questions v2.xlsx` *(v1.2)* (for revisions add ` (rev N)`; \" v2\" is the template version). Keep the template's `_Template_Info`, `Lists` and `Read Me` sheets in the file; the importer reads `_Template_Info` *(v1.2)*.

---

## 7. Template v2.0 additions for this family *(v1.2)*

Read with master command §6 (column rules), §6A (source-and-version rules), §7A–§7B (Due Date Rule, Event Trigger), §9A (checker and auditor guidance), §10A (Department Function / Sub-function) and §12.4–§12.5 (Risk Type, linked IDs).

### 7.1 Family extension columns (Applicability group, after Applicable Until)

| Header (row 2) | Expected values | When to fill |
|---|---|---|
| BRSR Principle | Section A - General disclosures · Section B - Management and process · Principle 1 · Principle 2 · Principle 3 · Principle 4 · Principle 5 · Principle 6 · Principle 7 · Principle 8 · Principle 9 · All | The BRSR section or principle the row feeds. |
| Indicator Class (Essential / Leadership / Core) | Essential · Leadership · Core | Essential indicators are mandatory; Leadership indicators are voluntary; BRSR Core items carry assurance requirements. |

Blank means "not a deciding factor for this row". Several values: separate with "; ". The values above are the expected v2.0 lists; the `Lists` sheet in `LDC-TPL-ESG-BRSR-v2.0` is authoritative where it differs. Never type a value that is not in the dropdown.

### 7.2 Department Function and Sub-function

Choose Department first, then a Function and Sub-function from the dependent lists in `Lists` (master §10A). Typical mapping for this family: Secretarial → BRSR filing / Board approval; Administration & Facilities → Energy and emissions data; HR → Workforce indicators; Finance, Treasury and Accounts → CSR spend; Investor Relations → ESG disclosures. Use the same Function and Sub-function for the same kind of obligation in every sheet of this family so that department-wise exports and the RAG heat map group correctly.

### 7.3 Risk Type

Primary type first, at most three (master §12.4). For this family: ESG & Climate primary; add Reputational for disclosures and Governance for Board oversight. Leave Linked RiskID and Linked GovID blank unless the platform library ID is known (master §12.5).

### 7.4 Source-and-version fields

Instrument name, reference and the two instrument dates are the same on every row. Actionable Last Updated On is per row: the issue date for rows untouched since the instrument was issued, and the date of the amending notification, circular or clarification for rows changed later (master §6A). For Acts, cite the Act number in Instrument Reference No. and use the latest amending Act or notification reflected in your text for Instrument Last Amended On.

### 7.5 Complete v2.0 example row (illustrative)

The row below shows every author column filled for one obligation in this family. It is a **format example**: confirm every citation, date and number against the primary text before reusing any of it; items marked [VERIFY] were not confirmed when this command was written. Interpretation / Explanation is abridged (real rows run 80–350 words).

| # | Header (key) | Example value |
|---|---|---|
| 1 | S. No. (`sno`) | 1 |
| 2 | CompID (`comp_id`) | (blank — the system generates it on import) |
| 3 | Compliance Question / Actionable (`question`) | Has the listed entity included a Business Responsibility and Sustainability Report in its annual report in the format specified by SEBI? |
| 4 | Clause / Para No. (`clause_ref`) | Regulation 34(2)(f), SEBI (LODR) Regulations, 2015 |
| 5 | Department (`department`) | Secretarial |
| 6 | Due Date & Frequency (`frequency`) | Annually |
| 7–8 | Date of Compliance; Status (`act_date; status`) | (blank — user / system) |
| 9 | Risk Category (`risk_level`) | High |
| 10 | Regulator / Authority (`authority`) | SEBI |
| 11 | Name of Master Direction / Regulation (`instrument_name`) | Securities and Exchange Board of India (Listing Obligations and Disclosure Requirements) Regulations, 2015 |
| 12 | Instrument Reference No. (`instrument_ref`) | No. SEBI/LAD-NRO/GN/2015-16/013 |
| 13 | Issue Date of Instrument (`instrument_issue_date`) | 02-Sep-2015 |
| 14 | Instrument Last Amended On (`instrument_amended_date`) | [VERIFY latest amendment] |
| 15 | Actionable Last Updated On (`question_updated_date`) | [VERIFY date of the amendment introducing BRSR] |
| 16 | Change Status (`change_status`) | Amended |
| 17 | Change Note / Previous Actionable (`change_note`) | BRSR replaced the Business Responsibility Report by the LODR amendment of 5 May 2021 [VERIFY]; previous actionable: 'Has the entity included a Business Responsibility Report …?' |
| 18 | Source Link (`source_url`) | https://www.sebi.gov.in |
| 19 | General Applicability (Layer) (`applic_layer`) | SEBI LODR Reg 34(2)(f) - BRSR |
| 20 | General Applicability (Type) (`applic_type`) | Listed entity - Top 1000 by market capitalisation |
| 21 | Conditional Applicability / Exemptions / Thresholds (`conditions`) | Mandatory for the top 1,000 listed entities by market capitalisation as on 31 March; others may report voluntarily. |
| 22 | Applicable From (`applic_from`) | 01-Apr-2022 |
| 23 | Applicable Until (`applic_to`) | (blank) |
| E1 | BRSR Principle (`ext_*`) | All |
| E2 | Indicator Class (Essential / Leadership / Core) (`ext_*`) | Essential |
| 24 | Short Title (`short_title`) | BRSR - inclusion in the annual report |
| 25 | Interpretation / Explanation (`explanation`) | The BRSR follows SEBI's format; Essential indicators are mandatory. BRSR Core assurance and value-chain disclosures apply on a glide path [VERIFY current dates]. (Abridged.) |
| 26 | Department Function (`dept_function`) | Annual Report |
| 27 | Department Sub-function (`dept_subfunction`) | BRSR |
| 28 | Compliance Type (`compliance_type`) | Disclosures |
| 29 | Due Date Rule (`due_rule`) | With the annual report, before the date of the annual general meeting |
| 30 | Event Trigger (for Event Based items) (`event_trigger`) | (blank) |
| 31 | Filing / Reporting / Intimation (`filing_details`) | Stock exchange (BRSR as part of Annual Report) |
| 32 | Portal / Form / Return Code (`filing_form`) | BRSR (XBRL) [VERIFY] |
| 33 | Related Document / Policy / Committee (`related_docs`) | Board; Sustainability / CSR Committee |
| 34 | Reference Weblinks (`weblinks`) | (blank) |
| 35 | Consequences of Non-Compliance / Penalty (`consequences`) | Exchange fines and SEBI penalty under s.15A(b), SEBI Act; reputational harm. |
| 36 | Penalty Provision (`penalty_ref`) | Section 15A(b), SEBI Act, 1992 |
| 37 | Risk Type (`risk_type`) | ESG & Climate; Reputational |
| 38 | Linked RiskID (`risk_ids`) | (blank — no library ID confirmed) |
| 39 | Linked GovID (`gov_ids`) | (blank — no library ID confirmed) |
| 40 | Evidence / Proof to Upload (`evidence`) | Annual report with BRSR; Board approval; exchange submission acknowledgement |
| 41 | Control Activity (Maker Guidance) (`control_activity`) | Collect indicator data from each owner, consolidate it in the SEBI format and have it reviewed. Place the BRSR before the Board with the annual report and file it with the exchanges. |
| 42 | Checker Review Points (`checker_points`) | 1. Every Essential indicator is answered. 2. Data owners signed off. 3. Board approved before filing. |
| 43 | Auditor Test Procedure (`audit_test`) | 1. Sample five indicators and trace to source data. 2. Inspect Board approval. Exception: unsupported figures or missing indicators. |
| 44 | Tags / Keywords (`tags`) | brsr; regulation 34; sustainability report; esg |
| 45–62 | Maker, Checker, Auditor and System groups (`maker … overlay`) | (blank — user / system) |

