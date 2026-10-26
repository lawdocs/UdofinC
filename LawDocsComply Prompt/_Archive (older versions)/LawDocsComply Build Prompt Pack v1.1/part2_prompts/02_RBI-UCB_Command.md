# 02 — RBI-UCB Family Command: Urban Co-operative Banks

**Template:** `templates/LDC-TPL-RBI-UCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-UCB-v1.0` · **Regulator / authority:** Reserve Bank of India (with RCS / CRCS for registration matters) · **Named-range prefix:** `RBI_UCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026 (*v1.1*: instrument list rebuilt from the RBI directions catalogue); items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — UCB Tier.** Column C holds the UCB tier under the revised regulatory framework: Tier 1 to Tier 4 by deposit size, with unit and salary-earners' UCBs in Tier 1. Many prudential provisions (CRAR, exposure limits, director qualifications, branch expansion) differ by tier. Write separate rows per tier.

**Column D — UCB Type / Overlay.** Column D records the structural type (unit, multi-district, multi-State under the MSCS Act), scheduled status, FSWM status, and supervisory overlays (SAF, s.35A All-Inclusive Directions). These change permissions, so use them. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_UCB_Sector):**
- Tier 1 UCB
- Tier 2 UCB
- Tier 3 UCB
- Tier 4 UCB
- All UCBs

**Column D (RBI_UCB_Entity):**
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

**Column H (RBI_UCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_UCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_UCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_UCB_Risk):** High, Medium, Low.

**Column P reference list (RBI_UCB_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
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
- FSWM status unlocks permissions such as new branches and certain products. Record the FSWM criteria in Column S.

## 4. Instruments to cover *(v1.1 — rebuilt from `catalogue/LDC_RBI_Directions_Catalogue_v1.1.xlsx`)*

**Content base (management instruction, 25 Oct 2026).** For this family write sheets **only** against: (a) the Department of Regulation consolidated Master Directions of 28 November 2025 as amended to date (RBI/DOR/2025-26/143–/386; 238 function-wise directions per RBI's press release, 244 Master Directions per RBI/2025-26/100; 240 live), (b) DoR directions issued since, (c) the Department of Supervision directions of 31 July 2026 (RBI/DoS/2026-27/408–/471), and (d) the CEPD Internal Ombudsman directions of 14 January 2026 and RB-IOS 2026. Never write against a circular or Master Direction withdrawn by RBI/2025-26/100; use it only to fill Column N "SUPERSEDES:" and the concordance note (master command §3A).

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

`RBI-<CAT> - <Direction short title>[ (DoS 2026)| (CEPD 2026)] - Compliance Questions.xlsx`, where `<CAT>` is the catalogue abbreviation (NBFC, UCB, RCB, ARC, CIC-CI, SCB, SFB, PB, LAB, RRB, AIFI, PPI). The proposed name for every direction is in catalogue column V. Revisions: append ` v2`, ` v3`. Keep the template's `_Template_Info` sheet in the file; the importer reads it. Record the upload date in catalogue column Z.
