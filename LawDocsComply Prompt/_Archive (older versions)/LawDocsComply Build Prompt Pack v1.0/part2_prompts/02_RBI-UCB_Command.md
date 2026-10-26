# 02 — RBI-UCB Family Command: Urban Co-operative Banks

**Template:** `templates/LDC-TPL-RBI-UCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-UCB-v1.0` · **Regulator / authority:** Reserve Bank of India (with RCS / CRCS for registration matters) · **Named-range prefix:** `RBI_UCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

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

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Banking Regulation Act, 1949 as applicable to co-operative societies (s.56; BR (Amendment) Act, 2020)
- RBI (Urban Co-operative Banks – <topic>) Directions, 2025: 27 directions of 28 Nov 2025 [VERIFY topic list]
- Revised regulatory framework for UCBs (Tier 1–4) and Supervisory Action Framework [VERIFY consolidation]
- RBI (Urban Co-operative Banks – Supervisory Returns) Directions, 2026 (RBI/DoS/2026-27/442, 31 Jul 2026) [VERIFY number]
- Umbrella Organisation (NUCFDC) framework [VERIFY]
- State Co-operative Societies Acts / MSCS Act, 2002 (registration, elections, audit matters not covered by the BR Act)
- DICGC Act, 1961

## 5. Family-specific pitfalls

- Applying commercial-bank Basel III rows to UCBs. UCBs follow their own capital framework.
- Writing State co-operative law obligations (AGM, elections) in a UCB RBI sheet. Use the COOP families instead.
- Forgetting Tier-specific CRAR minimums and director-qualification rules.

## 6. File naming

`RBI-UCB - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
