# 08 — COOP-GEN Family Command: Other Co-operative Societies and Registered Societies

**Template:** `templates/LDC-TPL-COOP-GEN-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-COOP-GEN-v1.0` · **Regulator / authority:** Central Registrar / State Registrars of Co-operative Societies; Registrar of Societies (SRA 1860) · **Named-range prefix:** `COOP_GEN_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Registration Law.** Column C records the registration law (MSCS Act, State Act, MACS Act, federal/apex society, or Societies Registration Act 1860 for non-co-operative societies).

**Column D — Society Type.** Column D records the society type: housing, consumer, dairy, marketing, sugar/agro-processing, fisheries, weavers/industrial, labour, multipurpose, transport, health, tourism, national MSCS (seeds/organic/exports), federations, SRA educational or charitable societies. Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (COOP_GEN_Sector):**
- Multi-State Co-operative Society (MSCS Act, 2002)
- State Co-operative Society (State Act)
- Mutually Aided Co-operative (State MACS Act)
- Federal / Apex Co-operative
- Society under Societies Registration Act, 1860 (non-co-operative)
- All

**Column D (COOP_GEN_Entity):**
- Housing Co-operative Society
- Consumer Co-operative
- Dairy / Milk Producers' Co-operative
- Marketing Co-operative
- Agro-processing / Sugar Co-operative
- Fisheries Co-operative
- Weavers' / Industrial Co-operative
- Labour Contract Co-operative
- Multipurpose Co-operative
- Transport Co-operative
- Health / Hospital Co-operative
- Tourism Co-operative
- National-level MSCS (Seeds / Organic / Exports)
- Federation / Union
- Educational / Charitable Society (SRA 1860)
- All (ALL)

**Column H (COOP_GEN_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (COOP_GEN_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Membership & Elections, Audit, Member Services & Grievance, Business Operations. Family additions: Membership & Elections, Audit, Member Services & Grievance, Business Operations.

**Column O (COOP_GEN_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Column R (COOP_GEN_Risk):** High, Medium, Low.

**Column P reference list (COOP_GEN_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Central Registrar of Co-operative Societies (CRCS Portal)
- Registrar of Co-operative Societies (State)
- Co-operative Election Authority (MSCS)
- State Co-operative Election Commission / Authority
- Co-operative Ombudsman (MSCS)
- Statutory Auditor (Panel)
- Department / Government Auditor
- General Body / Members
- Board of Directors / Committee of Management
- FIU-IND (FINnet 2.0)
- Income Tax / GST Authorities
- Registrar of Societies (SRA 1860)
- NCDC
- Not Required

## 3. Applicability logic for this family

- Governance rows (general body, board, elections, audit, annual return, registers, bye-law amendments) are common to all types. Sector rows (for example housing-society maintenance and transfer rules under State housing bye-laws, dairy FSSAI licensing) are written as separate sheets.
- SRA 1860 societies follow the central Act as amended by their State. Annual list of governing body members filing applies [VERIFY State].

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- MSCS Act, 2002 (as amended 2023) and MSCS Rules
- State Co-operative Societies Acts and Rules
- Societies Registration Act, 1860 and State amendments
- State model bye-laws for housing societies [VERIFY]
- Income-tax Act, 2025 (co-operative society provisions) [VERIFY section numbers]

## 5. Family-specific pitfalls

- Writing credit-society deposit rules for non-credit societies.
- Treating SRA societies as co-operatives. Use the SRA value in Column C.

## 6. File naming

`COOP-GEN - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
