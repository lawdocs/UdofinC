# 03 — RBI-RCB Family Command: Rural Co-operative Banks (StCBs and DCCBs)

**Template:** `templates/LDC-TPL-RBI-RCB-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-RBI-RCB-v1.0` · **Regulator / authority:** Reserve Bank of India (regulation); NABARD (supervision) · **Named-range prefix:** `RBI_RCB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — RCB Category.** Column C distinguishes State Co-operative Banks from District Central Co-operative Banks.

**Column D — RCB Type / Overlay.** Column D adds scheduled status and supervisory overlays. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (RBI_RCB_Sector):**
- State Co-operative Bank (StCB)
- District Central Co-operative Bank (DCCB)
- All Rural Co-operative Banks

**Column D (RBI_RCB_Entity):**
- StCB - Scheduled
- StCB - Non-Scheduled
- DCCB
- RCB under Supervisory Action / s.35A Directions
- RCB with CBS / Shared Service Entity arrangement
- All RCBs (ALL)

**Column H (RBI_RCB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (RBI_RCB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML. Family additions: Credit, Internal Audit & Inspection, Customer Service & Grievance, Information Security, KYC & AML.

**Column O (RBI_RCB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance.

**Column R (RBI_RCB_Risk):** High, Medium, Low.

**Column P reference list (RBI_RCB_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
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
- Where a direction says "StCBs and DCCBs", use C = "All Rural Co-operative Banks".

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Banking Regulation Act, 1949 (Part V, s.56)
- RBI (Rural Co-operative Banks – <topic>) Directions, 2025: 26 directions of 28 Nov 2025 [VERIFY topic list]
- NABARD supervisory instructions, circulars and returns (ENSURE) [VERIFY]
- State Co-operative Societies Acts and Rules

## 5. Family-specific pitfalls

- Citing UCB directions for RCBs. The 2025 sets are separate.
- Missing the NABARD filing route in Column P.

## 6. File naming

`RBI-RCB - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
