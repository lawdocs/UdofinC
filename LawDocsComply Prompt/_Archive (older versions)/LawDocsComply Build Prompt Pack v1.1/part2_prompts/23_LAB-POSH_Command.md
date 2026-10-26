# 23 — LAB-POSH Family Command: Labour Codes, Shops and Establishments, and POSH

**Template:** `templates/LDC-TPL-LAB-POSH-v1.0 - *.xlsx` · **Template code:** `LDC-TPL-LAB-POSH-v1.0` · **Regulator / authority:** Ministry of Labour and Employment; State Labour Departments; Ministry of Women and Child Development (POSH) · **Named-range prefix:** `LAB_*`
**Use with:** `00_Part2_Master_Command.md` (paste first), then this file, then the instrument line. As of 25 October 2026; items marked [VERIFY] must be re-checked against the primary source before writing rows that depend on them.

## 1. How Columns C and D work in this family

**Column C — Law.** Column C holds the law (each Labour Code, the POSH Act, State Shops and Establishments Act, State PT/LWF, Apprentices Act).

**Column D — Establishment Type / Threshold.** Column D holds the establishment type or headcount threshold that switches obligations on (10, 20, 50, 100, 300 employees; factory; shop; IT/ITES; contractor; inter-State migrants; gig/platform; BOCW; remote workforce). Several values are separated by "; ".

## 2. Dropdown values (exactly as in the template's `Rough` sheet)

**Column C (LAB_Sector):**
- Code on Wages, 2019
- Industrial Relations Code, 2020
- Code on Social Security, 2020
- Occupational Safety, Health and Working Conditions Code, 2020
- POSH Act, 2013
- Shops and Establishments Act (State)
- Professional Tax / Labour Welfare Fund (State)
- Apprentices Act, 1961
- All Labour Laws

**Column D (LAB_Entity):**
- All establishments
- Establishment with 10 or more employees
- Establishment with 20 or more employees
- Establishment with 50 or more employees
- Establishment with 100 or more employees
- Establishment with 300 or more workers (standing orders)
- Factory
- Shop / Commercial establishment
- IT / ITES establishment
- Contractor / Principal employer (contract labour)
- Inter-State migrant workers employer
- Gig / Platform aggregator
- Building and other construction work
- Remote / work-from-home workforce
- All (ALL)

**Column H (LAB_Freq):** Annually, Half Yearly, Quarterly, Monthly, Fortnightly, Weekly, Daily, Event Based, Immediately, Ongoing/Continuous, One-time, Every 2 Years, Every 3 Years, Every 5 Years. Family additions to the base list: Every 2 Years, Every 3 Years, Every 5 Years.

**Column M (LAB_Dept):** Governance & Administration, Finance, Treasury and Accounts, Legal & Litigation, IT, Operations & Management, HR, Compliance, Returns & Reporting, Risk Management, Payroll, Administration & Facilities, Internal Committee (POSH). Family additions: Payroll, Administration & Facilities, Internal Committee (POSH).

**Column O (LAB_CompType):** Policies, Compliance, Returns & Reporting, Committee, Internal Compliance, Suggestive Compliance, Registers & Records. Family additions: Registers & Records.

**Column R (LAB_Risk):** High, Medium, Low.

**Column P reference list (LAB_Filing — start Column P with one of these, then optional " — detail" and "Due: <rule>"):**
- Shram Suvidha Portal (MoLE)
- EPFO (Unified Portal)
- ESIC Portal
- State Labour Department (Shops and Establishments)
- Inspector-cum-Facilitator
- District Officer (POSH - annual report)
- Welfare Board (BOCW)
- Professional Tax Authority (State)
- Labour Welfare Fund Board (State)
- Employees (display / notice)
- Board (Directors' Report disclosure)
- Not Required

## 3. Applicability logic for this family

- All four Labour Codes took effect on 21 Nov 2025. Central and State rules are notified in stages, so check the State rule before writing State-specific registers and returns [VERIFY by State].
- Registers and returns under the Codes are prescribed by rules, mostly in electronic form. Each register is a "Registers & Records" row.
- POSH: IC constitution (s.4), annual report to the District Officer (s.21 read with r.14), display and awareness (s.19), Board report disclosure (Companies (Accounts) Rules r.8(5)(x)).

## 4. Instruments to cover (inventory to verify before writing; one sheet per instrument)

- Code on Wages, 2019; Industrial Relations Code, 2020; Code on Social Security, 2020; OSH Code, 2020 (all in force from 21 Nov 2025) and Central Rules [VERIFY]
- State rules under each Code and State Shops and Establishments Acts [select State]
- Sexual Harassment of Women at Workplace (Prevention, Prohibition and Redressal) Act, 2013 and Rules, 2013
- Companies (Accounts) Rules, 2014 r.8(5)(x) (POSH disclosure in the Board report)
- Professional Tax and Labour Welfare Fund Acts of the State

## 5. Family-specific pitfalls

- Citing repealed Acts (Payment of Wages Act, Factories Act, etc.) after 21 Nov 2025 except for transitional matters.
- Missing State variation in thresholds.

## 6. File naming

`LAB-POSH - <Instrument short title> <Year>.xlsx` (for revisions add ` vN`). Keep the template's `_Template_Info` sheet in the file; the importer reads it.
