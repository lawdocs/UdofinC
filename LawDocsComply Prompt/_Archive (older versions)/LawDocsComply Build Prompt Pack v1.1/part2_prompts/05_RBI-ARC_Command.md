# 05 — RBI-ARC Family Command: Asset Reconstruction Companies

**Template:** `templates/LDC-TPL-RBI-ARC-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-ARC-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_ARC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — ARC Level.** Column C separates obligations of the ARC as a company from obligations at the trust/scheme level (SR issuance, trust accounts, NAV declaration, QB disclosures).

**Column D — ARC Type / Activity.** Column D adds activity overlays: resolution applicant under IBC, trustee/manager role, sponsor and FDI structures, listed SRs. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_ARC_Sector):**
- ARC - Company Level
- ARC - Trust / Scheme Level
- All ARCs

**Column D (RBI_ARC_Entity):**
- ARC (all)
- ARC eligible for additional permitted activities (NOF-based)
- ARC acting as Resolution Applicant (IBC)
- ARC acting as Trustee / Manager of Trusts
- ARC with Sponsor Bank / FI
- ARC with FPI / FDI investment
- Listed ARC / ARC with listed SRs
- Security Receipt (SR) Scheme
- All ARCs (ALL)

**Column H (RBI_ARC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_ARC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Acquisition & Resolution, Trusteeship & SR Management, Internal Audit, Customer Service & Grievance. Family additions: Acquisition & Resolution, Trusteeship & SR Management, Internal Audit, Customer Service & Grievance.

**Column O (RBI_ARC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_ARC_Risk):** High, Medium, Low.

**Column P reference list (RBI_ARC_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
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
- Additional permitted activities depend on the NOF threshold [VERIFY]. Write the threshold in Column S.
- SR investment by the transferor bank and provisioning on SRs are bank-side obligations. Put them in RBI-SCB, not here.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

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

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
