# 04 — RBI-NBFC Family Command: Non-Banking Financial Companies (all layers and types)

**Template:** `templates/LDC-TPL-RBI-NBFC-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-NBFC-v1.0` · **Regulator / authority:** Reserve Bank of India (NHB for HFC supervision) · **Named-range prefix:** `RBI_NBFC_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — NBFC Layer.** Column C holds the Scale Based Regulation layer: Base, Middle, Upper or Top. Many governance and prudential provisions apply only from the Middle Layer upwards (for example the Compliance Function Directions, 2026 apply to ML and UL) or only to the Upper Layer (for example CET1 and the listing requirement). Use "All Layers" only where the paragraph does not distinguish.

**Column D — NBFC Type.** Column D holds the NBFC type: ICC, MFI, Factor, IFC, IDF, HFC, CIC, MGC, SPD, P2P, AA, NOFHC, NBFC-D, government NBFC, the two no-public-funds categories, and Factoring Act registrants. Several types have their own directions (HFC, CIC, MGC, NOFHC, SPD, MFI, P2P, AA). For those, write the sheet under the type-specific direction and set Column D precisely. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_NBFC_Sector):**
- Base Layer (NBFC-BL)
- Middle Layer (NBFC-ML)
- Upper Layer (NBFC-UL)
- Top Layer (NBFC-TL)
- All Layers

**Column D (RBI_NBFC_Entity):**
- NBFC-Investment and Credit Company (NBFC-ICC)
- NBFC-Microfinance Institution (NBFC-MFI)
- NBFC-Factor
- NBFC-Infrastructure Finance Company (NBFC-IFC)
- Infrastructure Debt Fund (IDF-NBFC)
- Housing Finance Company (HFC)
- Core Investment Company (CIC)
- Mortgage Guarantee Company (MGC)
- Standalone Primary Dealer (SPD)
- NBFC-Peer to Peer Lending Platform (NBFC-P2P)
- NBFC-Account Aggregator (NBFC-AA)
- Non-Operative Financial Holding Company (NOFHC)
- Deposit-taking NBFC (NBFC-D)
- Government-owned NBFC
- NBFC without public funds and without customer interface
- NBFC with customer interface, without public funds
- Registered Factor under Factoring Regulation Act, 2011
- All NBFCs (ALL)

**Column H (RBI_NBFC_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_NBFC_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security. Family additions: Credit, Collections & Recovery, Internal Audit, Customer Service & Grievance, Information Security.

**Column O (RBI_NBFC_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_NBFC_Risk):** High, Medium, Low.

**Column P reference list (RBI_NBFC_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- RBI - CIMS (Supervisory Returns)
- RBI - DAKSH (Supervisory Compliance)
- RBI - PRAVAAH (Applications / Approvals)
- RBI (prior approval)
- RBI (intimation)
- RBI - Department of Regulation
- RBI - Department of Supervision
- NHB (HFC supervision)
- FIU-IND (FINnet 2.0)
- Credit Information Companies (CICs)
- CERSAI / CKYCR
- CERT-In
- MCA (ROC)
- SEBI / Stock Exchanges (listed NBFCs / NCD issuers)
- Debenture Trustee
- Credit Rating Agency
- IRDAI (corporate agency)
- Board / Management
- Statutory / Central Auditor
- Not Required

## 3. Applicability logic for this family

- The layer is set by asset size and the RBI Upper Layer list [VERIFY thresholds in the SBR Directions 2025]. Some types are always Base Layer (P2P, AA, NOFHC, and NBFCs without public funds and customer interface). Some are never Base Layer (deposit-taking NBFCs, HFCs above the threshold). Write applicability rows for layer determination.
- Each topic direction repeats a "Applicability" chapter. Read it first and set C/D from it, not from memory.
- Government-owned NBFCs have specific carve-outs (for example on some governance provisions). Record them in Column S.
- The 31 July 2026 DoS directions (460–468) add supervisory obligations: compliance function, cyber/tech risk, digital payment security, fraud risk, internal audit, statutory audit, supervisory returns, miscellaneous supervisory, auditor's report. Write each as its own sheet.
- NBFC-ICC investment activity (equities, AIF units, REIT/InvIT units, IPO subscriptions) is governed by the Investment Portfolio Direction, the Concentration Risk Direction and the RBI instructions on investments in AIFs [VERIFY current text]. Write these rows with D = "NBFC-Investment and Credit Company (NBFC-ICC)".

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- RBI Act, 1934 Chapter III-B (ss. 45-IA, 45-IB, 45-IC, 45-IE, 45-JA, 45-L, 45-MA, 58B, 58G)
- RBI (Non-Banking Financial Companies – <topic>) Directions, 2025: the 30 directions of 28 Nov 2025 listed in the template's _Template_Info (Registration, Exemptions and Framework for Scale Based Regulation; Governance; Capital Adequacy; IRACP; ALM; Concentration Risk; Outsourcing …)
- RBI (Housing Finance Companies), (Core Investment Companies), (Mortgage Guarantee Companies), (NOFHC) and (Standalone Primary Dealers) Directions, 2025
- RBI (NBFC – Compliance Function) Directions, 2026 (RBI/DoS/2026-27/460, 31 Jul 2026) and DoS directions 461–468 (Cybersecurity and Technology Risk; Digital Payment Security; Fraud Risk Management; Internal Audit; Statutory Audit; Supervisory Returns (/466); Miscellaneous Supervisory incl. PCA (/467); Auditor's Report) [VERIFY titles and numbers]
- Reserve Bank – Integrated Ombudsman Scheme, 2026 and RBI (NBFC – Internal Ombudsman) Directions, 2026 (RBI/CEPD/2025-26/384)
- Factoring Regulation Act, 2011 (registered factors); SARFAESI Act, 2002 (notified NBFCs)

## 5. Family-specific pitfalls

- Using pre-2025 Master Direction paragraph numbers (e.g., the 2023 SBR Master Direction).
- Writing ML/UL-only rows with C = "All Layers".
- Splitting too little. The Governance and Compliance Function directions contain long lists of Board and committee functions, and each element is its own row.
- Missing glide-path dates for NOF and other phased requirements.

## 6. File naming

`RBI-NBFC - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
