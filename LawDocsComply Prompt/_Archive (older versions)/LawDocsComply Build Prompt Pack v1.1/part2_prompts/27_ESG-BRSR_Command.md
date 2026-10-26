# 27 — ESG-BRSR Family Command: ESG, BRSR / BRSR Core, CSR and GHG *(v1.1)*

**Template:** `templates/LDC-TPL-ESG-BRSR-v1.0 - ESG BRSR and CSR.xlsx` · **Template code:** `LDC-TPL-ESG-BRSR-v1.0` · **Regulator / authority:** SEBI; MCA; stock exchanges; RBI (climate-related financial risk); voluntary standards bodies (ISSB, GHG Protocol, GRI); EU (CSRD/ESRS) for EU-facing groups · **Named-range prefix:** `ESG_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them. The importer blocks any row that still carries `[VERIFY]`.

**Why this family exists.** Sustainability reporting has become a statutory disclosure for the top 1,000 listed entities (BRSR, with BRSR Core assurance phased in), CSR is a statutory spend-and-report obligation for every company above the s.135 thresholds, and RBI-regulated lenders face climate-risk disclosure expectations. This family turns those obligations into checkpoints that feed the ESG module (P27) and the BRSR drafting workflow. It is an overlay (`OV_ESG`) that attaches to the MCA-CO, SEBI-LISTED and RBI families (P15).

## 1. How Columns C and D work in this family

**Column C — Framework / Instrument.** The instrument the checkpoint comes from. Where one control satisfies several frameworks (for example, a Scope 1 and 2 emissions inventory satisfies BRSR Principle 6, BRSR Core and ISSB IFRS S2), write the row once under the binding Indian instrument and list the others in Column N ("Also satisfies: …").

**Column D — Entity category.** The category that triggers the obligation: market-cap tier for BRSR and BRSR Core (top 1,000; top 250 for value-chain disclosures), the s.135 threshold for CSR, the RE category for climate risk. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (ESG_Sector):** SEBI LODR Reg 34(2)(f) - BRSR · SEBI BRSR Core and Assurance · SEBI BRSR Value Chain Disclosures · SEBI ESG Rating Providers and ESG Debt / ESG Schemes · Companies Act 2013 s.135 and CSR Rules 2014 · Companies Act 2013 Board Report (s.134) sustainability items · RBI Climate-related Financial Risk · GHG Protocol (Scope 1, 2 and 3) · ISSB IFRS S1 and S2 · EU CSRD / ESRS (EU-facing groups) · Board-approved internal ESG / Sustainability Policy · All Frameworks

**Column D (ESG_Entity):** Listed entity - Top 1000 by market capitalisation · Listed entity - Top 250 (value-chain scope) · Listed entity - other (voluntary BRSR) · Company meeting s.135 CSR thresholds · Company with CSR obligation below Rs 50 lakh (no CSR Committee required) · Regulated Entity - Bank / NBFC / UCB (RBI climate risk) · Asset Management Company / ESG scheme · Issuer of green / ESG debt securities · Unlisted company - voluntary sustainability reporting · Group with EU operations (CSRD scope) · All Entities (ALL)

**Column M (ESG_Dept):** the nine base departments plus Secretarial, Investor Relations, Administration & Facilities, Internal Audit (codes per Appendix U §U.9.0).

**Column O (ESG_CompType):** the six base types plus *Disclosures* (code `DISCLOSURES`).

**Column P (ESG_Filing, reference):** Stock exchange (BRSR as part of Annual Report) · MCA (CSR-2 / AOC-4) · SEBI · RBI · Annual Report disclosure · Board / CSR Committee · Reasonable assurance provider · Website disclosure · Not Required

## 3. Applicability and status logic for this family

1. **BRSR.** Mandatory for the top 1,000 listed entities by market capitalisation (computed as on 31 March); write the tier in Column S. Others may report voluntarily; such rows use O = *Suggestive Compliance*.
2. **BRSR Core assurance and value chain.** Follow SEBI's circular of 28 March 2025: assurance or assessment of BRSR Core phased by market-cap tier; value-chain disclosures voluntary from FY 2025-26 for the top 250, covering partners above 2% of purchases or sales [VERIFY paragraph numbers and the phase-in table before writing]. The owner baseline's "75% value-chain boundary" is superseded.
3. **CSR.** Applies to a company with net worth ≥ ₹500 crore, turnover ≥ ₹1,000 crore or net profit ≥ ₹5 crore in the immediately preceding financial year (s.135(1)). Write separate rows for: CSR Committee (not required where the obligation is ≤ ₹50 lakh, s.135(9)); CSR policy and annual action plan; 2% spend computed on average net profit (s.198) of the three preceding years; unspent amounts (ongoing projects → Unspent CSR Account within 30 days of year-end, spend within three years; other amounts → Schedule VII fund within six months); impact assessment where the average obligation is ≥ ₹10 crore and project outlay ≥ ₹1 crore; CSR-2 filing; Board-report annexure; website disclosure.
4. **RBI climate risk.** Until RBI finalises the climate-related financial risk disclosure framework [VERIFY status], rows use O = *Suggestive Compliance* and S = "Draft; becomes binding on final issue".
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

`ESG-BRSR - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
