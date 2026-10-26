# 05 — RBI-ARC Family Command: Asset Reconstruction Companies

**Template:** `templates/LDC-TPL-RBI-ARC-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-ARC-v1.0` · **Regulator / authority:** Reserve Bank of India · **Named-range prefix:** `RBI_ARC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

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

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- SARFAESI Act, 2002 (Chapter II)
- RBI (Asset Reconstruction Companies – <topic>) Directions, 2025: 4 directions of 28 Nov 2025 incl. KYC and Credit Information Reporting [VERIFY]
- RBI Master Direction – Asset Reconstruction Companies (Reserve Bank) Directions, 2024 [VERIFY whether consolidated]
- RBI (Asset Reconstruction Companies – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/469, 31 Jul 2026) [VERIFY number]
- Security Interest (Enforcement) Rules, 2002
- IBC, 2016 and IBBI regulations (where the ARC acts as resolution applicant)

## 5. Family-specific pitfalls

- Ignoring trust-level obligations (separate books per trust, NAV).
- Using the old ₹100 crore NOF figure. RBI has raised it; read the current text [VERIFY].

## 6. File naming

`RBI-ARC - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
