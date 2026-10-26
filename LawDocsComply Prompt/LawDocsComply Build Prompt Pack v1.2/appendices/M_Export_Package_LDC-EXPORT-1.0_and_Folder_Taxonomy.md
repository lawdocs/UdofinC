# Appendix M — Export Package `LDC-EXPORT-1.0` and Folder Taxonomy

**LawDocsComply Build Prompt Pack v1.0 · 25 October 2026 · Binding for P19 and for every module's export-map registration (NN-10).**

## M.0 Purpose and precedence

This appendix fixes the folder tree, file names, formats, manifest, README, certificate and verification rules of every LawDocsComply archive. `LDC-EXPORT-1.0` is LDC's **folder profile `ldc_tenant_v1` (version 1.0.0; 1.1.0 from v1.1 — folders 25–29 appended, additive only)** *(v1.1)* under the Infrabyx Ecosystem Integration Specification v1.1 §12.1 **archive standard 1.0**; where this appendix and Spec §12.1 differ, Spec §12.1 prevails and this appendix is corrected (NN-23). Design goal: a beginner with Windows Explorer or macOS Finder, Microsoft Office or LibreOffice, a PDF reader and a checksum tool can find, open, verify and understand every record without LawDocsComply; a successor system can load every dataset.

## M.1 Root folder

```
[Owner legal name] - LawDocsComply Archive - [Scope] - as of [YYYY-MM-DD]/
```
Examples:
- `ABC Finance Private Limited - LawDocsComply Archive - Full - as of 2026-10-31/`
- `ABC Finance Private Limited - LawDocsComply Archive - FY 2025-26 - as of 2026-05-15/`
- `XYZ Urban Co-operative Bank Ltd - LawDocsComply Archive - Audit Pack - Statutory Audit FY 2025-26 - as of 2026-06-10/`
- `ABC Finance Private Limited - LawDocsComply Archive - Exit - as of 2027-01-31/`

Scope words: `Full`, `Exit`, `FY 2025-26`, `Legal Entity - [name]`, `Module - [module name]`, `Department - [name]`, `Board Pack - [meeting]`, `Audit Pack - [engagement]`, `Regulator Pack - [inspection ref]`, `Backup - Monthly Full`, `Backup - Daily Incremental [seq]`, `Data Principal Access - [request ref]`, `Record - [record title]`.

## M.2 `00 Start Here/` (mandatory, identical structure in every package)

```
00 Start Here/
    README.pdf
    README.docx
    README.txt
    How to find things.pdf              ← one-page visual map of the folders (LDC addition)
    Folder guide.xlsx                    ← every folder: what it contains, typical questions, record types (LDC addition)
    export-manifest.csv
    manifest.json
    manifest.json.jws
    data-dictionary.xlsx
    data-dictionary.csv
    relationships.csv
    relationship-map.pdf
    CHANGES-SINCE-PREVIOUS.csv           ← for repeated/incremental exports (LDC addition)
    BSA-Section-63-Certificate.docx      ← pre-filled; to be signed (LDC addition)
    BSA-Section-63-Certificate.pdf
    LawDocsComply-Platform-Statement.pdf ← signed by LDC (DSC) (LDC addition)
    Open me - Viewer.html                ← optional offline viewer (LDC addition)
    code-tables/
        department.csv, compliance_status.csv, frequency.csv, compliance_type.csv,
        risk_rating.csv, entity_family.csv, regulator.csv, meeting_type.csv,
        resolution_type.csv, policy_status.csv, finding_rating.csv, grievance_category.csv, ...
    schemas/
        <dataset>.schema.json  (JSON Schema 2020-12, one per dataset)
    verify/
        ldc-verify (Windows .exe, macOS, Linux binaries), README-verify.txt, public-key.pem, LICENSE (Apache-2.0)
```

## M.3 Top-level folders and complete taxonomy

Default nesting inside content folders: **[Legal entity] → [Financial year] → [Department] → [Item]**. Single-entity tenants omit the entity level. `FY YYYY-YY` = Indian financial year (1 April – 31 March) unless the tenant's year differs (`CY YYYY` or a configured label). Department names come from the tenant's terminology (historical names by default; M.11). Items are named `YYYY-MM-DD - Title` for dated items or by their register/policy name. `[…]` = placeholder; `{id}` suffix used only when needed for uniqueness or path length.

### 01 Organisation and Entity Profile

```
01 Organisation and Entity Profile/
    Organisation profile.xlsx            (legal name, constitution, CIN/LLPIN/registration no., PAN masked, GSTINs, LEI, addresses, regulators, registrations, licences)
    Legal entities.xlsx / .csv
    Registrations and licences/
        [Regulator] - [Registration type] - [Number]/   (certificate PDFs, renewal history)
    Group structure.xlsx + Group structure.pdf
    Departments and functions.xlsx       (current + historical names with effective dates)
    Office locations and branches.xlsx
```

### 02 Regulatory Coverage and Applicability

```
02 Regulatory Coverage and Applicability/
    Applicable instruments.xlsx          (instrument, authority, version/date, last update, applicability basis, selected by, selected on)
    Instruments removed.xlsx             (with dates and reason; history kept — NN-29)
    Applicability decisions.xlsx         (rule trace from P15 engine; overrides with reasons)
    Content versions pinned.csv          (compliance instance ↔ content version)
    Tenant customisations of questions.xlsx (base text vs tenant text, author, date, reason — audit-linked)
    Tenant-authored questions.xlsx
    Source documents/
        [Authority]/[Instrument short name]/[Version date] - [Title].pdf
```

### 03 Compliance Register and Evidence

```
03 Compliance Register and Evidence/
    Compliance register - all years.xlsx / .csv     (one row per compliance instance; status; dates; maker; checker; auditor; evidence count)
    Obligations master.xlsx / .csv                    (base + overlay + tenant-authored; template contract v2.0 columns by machine key)
    Exceptions waivers and extensions.xlsx
    Issues register.xlsx
    Attestations/
        [YYYY-MM-DD] - [Campaign name]/ responses.xlsx, summary.pdf
    Controls and Control Executions/  *(v1.1, X1)*
        Control library.xlsx                       (control, linked obligations across instruments, owner, frequency, automated or manual)
        [Control name] - ctl_{id}/ Executions.xlsx, evidence of each execution
    Compliance Testing/  *(v1.1, X1; second line, P04)*
        [FY]/ [Cycle name] - [Status]/ test plan.pdf, population and sample.xlsx (seed recorded), results.xlsx, remediation tracker.xlsx, retest evidence/
    Request Lists/  *(v1.1, X1)*
        [YYYY-MM-DD] - [Request list name]/ items.xlsx, uploaded evidence/ (accepted items only)
    Automated Check Results/  *(v1.1, X1; continuous control monitoring)*
        [Test name] - [FY]/ runs.xlsx (PASS / FAIL / NO_DATA / INVALID with snapshot hashes), evidence snapshots/
    [Legal entity]/
        FY 2026-27/
            [Department]/
                [Instrument short name]/
                    [Obligation short title] - obl_{id}/
                        [Due date or period] - Q2 FY 2026-27 - [Status]/
                            Evidence/ (originals as uploaded; type copies; translations)
                            Compliance record.pdf            (maker submission, checker review, comments, dates — human-readable)
                            Compliance record.xlsx
                            Trail.xlsx                       (this instance's audit events)
```
Status words in folder names: `COMPLIED`, `COMPLIED LATE`, `NOT COMPLIED`, `NOT APPLICABLE`, `WAIVED`, `IN PROGRESS`, `OVERDUE` (as at the export date).

### 04 Regulatory Updates and Change Log

```
04 Regulatory Updates and Change Log/
    Updates received.xlsx                (date, authority, title, type: new/amendment/repeal/FAQ/consultation, impact assessment, decision, tasks)
    Content change log.xlsx              (old actionable → new actionable, effective date, publisher, tenant impact)
    [YYYY-MM-DD] - [Authority] - [Short title]/
        Source.pdf, What changed.pdf, Impact assessment.pdf / .docx, Tasks created.xlsx
```

### 05 Governance - Board, Committees and Meetings

```
05 Governance - Board, Committees and Meetings/
    Board and committee composition - history.xlsx
    Terms of reference/
        [Committee name] - Terms of Reference v[x] - APPROVED [date].pdf / .docx
    [Legal entity]/
        FY 2026-27/
            Board of Directors/
                2026-08-14 - Board Meeting 3 of FY 2026-27/
                    01 Notice and Agenda.pdf / .docx
                    02 Board Papers/ (each agenda item: "Item 05 - [title].pdf")
                    03 Attendance and Quorum.xlsx
                    04 Minutes - SIGNED.pdf  (+ .docx draft history in "Drafts" if exported)
                    05 Resolutions passed.xlsx + each resolution PDF
                    06 Action items.xlsx
                    07 Recording or transcript/ (only if retained and permitted)
            Audit Committee/  … same structure
            Nomination and Remuneration Committee/
            Risk Management Committee/
            IT Strategy Committee/
            [Other committees as named by the tenant]/
            General Meetings/
                2026-09-25 - Annual General Meeting/  (notice, explanatory statement, attendance, scrutiniser report, minutes, results)
            Circular Resolutions/
                2026-07-02 - [subject].pdf
```

### 06 Company Secretarial - Registers, Filings and Resolutions

```
06 Company Secretarial - Registers, Filings and Resolutions/
    Statutory Registers/
        Register of Members - MGT-1.xlsx / .pdf
        Register of Directors and KMP.xlsx / .pdf
        Index of Directors Interest Disclosures - MBP-1 (not a register).xlsx
        Register of Loans Investments Guarantees - MBP-2.xlsx / .pdf
        Register of Contracts with Related Parties - MBP-4.xlsx / .pdf
        Register of Charges - CHG-7.xlsx / .pdf
        Register of Significant Beneficial Owners - BEN-3.xlsx / .pdf
        Register of Employee Stock Options - SH-6.xlsx / .pdf
        Register of Deposits.xlsx (if applicable)
        Register of Penalties Strictures and Warnings.xlsx
    MCA Filings/
        FY 2026-27/
            [YYYY-MM-DD] - [Form] - [Purpose] - SRN [number]/  (form PDF, attachments, challan, acknowledgement)
    Listed Company Compliance/ (if applicable)
        LODR Filings/ FY 2026-27/ [YYYY-MM-DD] - [Regulation] - [Subject]/
        Insider Trading - Structured Digital Database/  → only in 99 Restricted
    Director KYC and Declarations/
        DIR-8, MBP-1, DIR-2 by director id (no personal data in names)
    Fit and Proper/
        [FY]/ declarations and NRC/Board assessments (by person id)
    Annual Reports/
        FY 2026-27/ Draft and approved Annual Report, Board's Report, AOC-4 and MGT-7 data workbooks, approval minutes reference
    Secretarial Audit/ → see folder 10
```

### 07 Policies and Procedures

```
07 Policies and Procedures/
    Policy register.xlsx                 (policy, owner department, current version, Board approval date, effective date, next review date, status)
    [Policy name]/
        [Policy name] v3.0 - APPROVED 2026-05-12.pdf
        [Policy name] v3.0 - APPROVED 2026-05-12.docx
        [Policy name] v3.0 - Board approval - 2026-05-12.pdf   (scanned approval/extract of minutes)
        [Policy name] v3.0 - Changes from v2.1 - REDLINE.docx  (tracked changes)
        Earlier versions/
            [Policy name] v2.1 - SUPERSEDED 2026-05-12.pdf / .docx
        Attestations v3.0.xlsx
    Procedures and SOPs/
        [SOP name] v[x] - [status].pdf / .docx
```

### 08 Risk Management

```
08 Risk Management/
    Risk register - current.xlsx / .csv
    Risk register - history.xlsx
    Risk appetite statement/
        RAS v[x] - APPROVED [date].pdf / .docx, thresholds.xlsx
    RCSA/
        [YYYY-MM-DD] - [Campaign]/ responses.xlsx, results.pdf
    Key Risk Indicators/
        KRI definitions.xlsx, KRI observations - FY 2026-27.xlsx, breaches.xlsx
    Loss events.xlsx
    CRO reports/
        [YYYY-MM] - CRO report to Risk Management Committee.pdf / .xlsx
```

### 09 Risk Assessments - ICAAP, Stress Tests and Ratios

```
09 Risk Assessments - ICAAP, Stress Tests and Ratios/
    Financial ratios - monthly.xlsx      (ratio, definition, value, limit, status, source run, as-of)
    Capital adequacy/
        [YYYY-MM-DD] - Capital computation.xlsx / .pdf  (with rule-pack version)
    ICAAP/
        FY 2026-27/
            ICAAP document v1.0 - APPROVED [date].pdf / .docx
            Board approval.pdf
            Supporting computations.xlsx
    Stress tests and scenario analysis/
        [YYYY-MM-DD] - [Scenario name] v[x]/
            Assumptions.xlsx, Results.xlsx, Report.pdf / .docx, Approval.pdf
    Liquidity and ALM/
        [YYYY-MM-DD] - Structural liquidity.xlsx, Interest rate sensitivity.xlsx
```

### 10 Audits and Inspections

```
10 Audits and Inspections/
    Audit universe and plans/
        Audit universe.xlsx, Annual audit plan FY 2026-27 - APPROVED [date].pdf / .xlsx
    Internal Audit/
        FY 2026-27/
            [Engagement name] - [Period]/
                01 Planning/ (scope, risk assessment, program)
                02 Fieldwork/ (workpapers by area, samples, evidence)
                03 Findings.xlsx
                04 Management responses.xlsx
                05 Report - FINAL [date].pdf / .docx
                06 Follow-up and closure.xlsx
    Risk Based Internal Audit/ …
    Concurrent Audit/ …
    IS Audit/ …
    Secretarial Audit/ (MR-3 report, annual secretarial compliance report where applicable)
    Statutory Audit support/ (PBC lists, information provided, auditor queries and replies)
    Regulatory Inspections/  *(v1.1, X1: index only — the inspection and observation records are owned by P26 and exported under `26 Legal Matters, Contracts and Licences/Regulator inspections/`; this folder holds the audit team's working papers on closure testing)*
        [YYYY-MM-DD] - [Regulator] - [Inspection type]/ (closure-test workpapers; link file to folder 26)
    Findings tracker - all audits.xlsx
```

### 11 Returns and Regulatory Reporting

```
11 Returns and Regulatory Reporting/
    Return calendar FY 2026-27.xlsx      (return code, regulator, portal, frequency, due date, status, filed on, acknowledgement)
    [Regulator]/
        [Return code] - [Return name]/
            FY 2026-27/
                [Period] - [Status]/
                    Upload file (exactly as submitted).[xml|xlsx|csv|json|txt]
                    Validation report.xlsx
                    Sign-off.pdf
                    Acknowledgement.pdf
                    Source data and mapping.xlsx
    Credit Information Companies/
        [CIC]/ [Cycle code] - [Reference date]/ submitted file (byte-identical), rejection report, DQI
    Accounts and Tax/
        FY 2026-27/
            01 Trial balances and mappings/
            02 Financial statements/ Draft/ Approved/  ([Entity] - [Framework] - [Statements|Notes|Schedules].[docx|xlsx|pdf])
            03 GST/ [GSTIN]/ [Period]/  (GSTR-1, GSTR-3B, GSTR-9/9C utility files exactly as generated, working papers)
            04 TDS/ [TAN]/ [Quarter]/ [Form]/
            05 MCA filings data/
            06 Tax audit data/
```

### 12 Data Protection and Cyber Security

```
12 Data Protection and Cyber Security/
    Records of processing activities.xlsx
    DPIAs/ [YYYY-MM-DD] - [Processing]/ DPIA.pdf / .docx
    Consent records - summary.xlsx (detail in 99 Restricted if personal)
    Data principal requests - log.xlsx
    Incidents and breaches/
        [YYYY-MM-DD] - INC-[ref]/ incident report.pdf, notifications (CERT-In, RBI, Data Protection Board), timeline.xlsx, RCA.pdf
    ISMS controls and tests.xlsx
    Cyber security policies → see 07
    Third parties and outsourcing/
        Vendor register.xlsx, Outsourcing register.xlsx, assessments/[vendor id]/
    VAPT and security assessments/ [YYYY-MM-DD] - [Scope]/ report.pdf, remediation.xlsx
```

### 13 People - HR and Labour Compliance

```
13 People - HR and Labour Compliance/
    Organisation chart.pdf, Positions.xlsx (no personal data beyond role holders' names where permitted)
    KMP and senior management.xlsx
    Labour Code registers/
        FY 2026-27/ [Register name as prescribed].xlsx / .pdf
    Labour returns and filings/ [Return]/[Period]/
    Committees/ (Works Committee, Grievance Redressal Committee, Safety Committee as applicable)
    Training records - summary.xlsx
    Employment agreements - index.xlsx (agreements themselves in 99 Restricted/HR)
    → Employee files, payroll, attendance, leave, POSH case files: 99 Restricted
```

### 14 Grievances and Customer Support

```
14 Grievances and Customer Support/
    Grievance register FY 2026-27.xlsx   (case ref, received, channel, category, level, status, TAT, closure, escalation, ombudsman reference — complainant identity masked)
    MIS and analysis/ monthly reports, trend analysis, root cause
    Grievance Redressal Officer reports/
    Support tickets - summary.xlsx
    → Case files with complainant identity: 99 Restricted/Grievances (when sealed mode on)
```

### 15 Co-operative Society Records (co-operative tenants only)

```
15 Co-operative Society Records/
    Bye-laws/ (versions, amendments, registrar approvals)
    Members register.xlsx (masked) and share capital.xlsx
    General Body Meetings/ [date] - [type]/ notice, attendance, minutes, resolutions
    Managing Committee/ [date] - Meeting/ …
    Elections/ [year]/ election programme, nominations, results, returning officer reports
    Statutory audit by co-operative auditor/ [FY]/ audit report, rectification report
        Audit paras tracker.xlsx  *(v1.1, X1)*       (para, classification, action taken, Registrar acceptance)
    Registrar inspections and inquiries/ [YYYY-MM-DD] - [type]/  *(v1.1, X1)* (requests, submissions, findings, compliance)
    Members' inspection requests.xlsx  *(v1.1, X1)*
    Returns to Registrar/ [FY]/
    Complaints and disputes/
```

### 16 Tasks, Calendar and Approvals

```
16 Tasks, Calendar and Approvals/
    Tasks - all.xlsx / .csv              (task, source, owner, assigned by, due, status, completed)
    Approvals - all.xlsx                 (request, maker, approver, decision, time)
    Calendar/ [Legal entity].ics, Board and committees.ics, Deadlines.ics, Calendar list.xlsx
    Delegations.xlsx
```

### 17 Documents Library

```
17 Documents Library/
    Library index.xlsx                   (every document: id, title, folder, type, versions, owner, tags, hash, retention class, legal hold)
    [Tenant DMS folders as configured]/  (originals and versions; type copies and translations next to originals)
    Custom Registers/  *(v1.1, X1; P02 custom registers builder)*
        [Register name]/ register.xlsx (current rows + version history sheet), attachments/, definition.json (fields, owner, retention)
```

### 18 Vidhi AI - Notebooks, Outputs and Activity

```
18 Vidhi AI - Notebooks, Outputs and Activity/
    AI activity log.xlsx                 (run ledger metadata: who, skill, model, provider, region, sources, accepted/rejected)
    Accepted AI outputs/ (as accepted into records — also present in their record folders)
    Tenant notebooks/ [Notebook title]/ sources list.xlsx, notes.docx, studio outputs
    Schedules.xlsx
    What Vidhi remembers - tenant.xlsx
```
(Platform notebooks are platform content and are listed by reference only.)

### 19 Contracts, Marketplace Engagements and Retainers

```
19 Contracts, Marketplace Engagements and Retainers/
    Engagements register.xlsx
    [YYYY-MM-DD] - [Provider] - [Service]/ engagement letter / SLA (signed), deliverables, acceptance, invoices
```

### 20 Billing, Subscription and Invoices

```
20 Billing, Subscription and Invoices/
    Subscription history.xlsx (plans, components, prices, discounts, trial, changes)
    Invoices/ FY 2026-27/ [Invoice number] - [date].pdf (GST tax invoices) + Invoices.xlsx
    Payments and refunds.xlsx
    Savings report.pdf / .xlsx
```

### 21 Users, Roles and Access History

```
21 Users, Roles and Access History/
    Users.xlsx (business contact data), Role assignments - history.xlsx, Access reviews/, External access grants.xlsx, Break-glass sessions.xlsx
```

### 22 Settings and Customisations

```
22 Settings and Customisations/
    Settings.json (signed bundle), Settings.xlsx (human), Terminology.xlsx, Folder policy.json, Menus.json, Workflow configurations.xlsx, Rule pack versions in use.xlsx
```

### 23 Integrations and Data Exchanges

```
23 Integrations and Data Exchanges/
    Connectors.xlsx (connector, version, state, data moved, dates), Mapping packs/ (YAML + overrides), Webhook subscriptions.xlsx, Exchange reconciliation reports.xlsx
    Data Room/
        [Source]/ [Dataset]/ [Period]/ batch-[id]/  (original files exactly as received from Finbyx, Udofin, Tally, LMS dumps or Excel, with hashes and the mapping used — P11 Data Room)
```

### 24 Audit Trail

```
24 Audit Trail/
    audit-events-2026-10.jsonl            (one per month; hash-chained; machine)
    Audit trail 2026-10.xlsx              (human digest: time, user, role, action, record, before → after, reason, correction link)
    Corrections register.xlsx             (D-02 correction entries with approvals)
    chain-anchors.csv                     (daily anchors)
```

### 25 Global Entities and Jurisdictions *(v1.1; P25)*

```
25 Global Entities and Jurisdictions/
    Group structure - global.xlsx + .pdf     (all entities, ownership %, home region, functional currency, FYE, registered agent)
    Jurisdictions in use.xlsx                (country/subdivision, pack id and version, tier, reviewer of record, coverage statement date)
    [Country] - [Entity name]/
        Entity record.xlsx                   (registration no., registry, incorporation date, registered office, officers, auditors, licences)
        Officers and directors.xlsx          (appointments, resignations, residency; personal data minimised)
        Statutory registers - [jurisdiction format]/
        Filings/ [FY or CY]/ [YYYY-MM-DD] - [Filing] - [Authority]/   (filed copy, acknowledgement, translation if any)
        Expert notes.xlsx                    (on-call answers from local partners; tenant-private)
    Coverage statements/ [Country] - [Pack version].pdf
    Group compliance map.xlsx                (entity × status aggregates; same view as SCR-GEM-08)
```
Official-language source text and its reviewed translation are both kept for every foreign clause cited in this folder (NN-54).

### 26 Legal Matters, Contracts and Licences *(v1.1; P26; D-41)*

```
26 Legal Matters, Contracts and Licences/
    Legal matters register.xlsx              (matter id, type: litigation/arbitration/notice/regulatory inspection/consumer/tax/labour, forum, case no., CNR, parties (masked where personal), counsel, stage, next date, exposure, provision, status)
    Matters/
        [YYYY] - [Matter id] - [Short title]/
            Pleadings and filings/  Orders and judgments/  Hearings and cause-list entries.xlsx
            Notices and replies/    Counsel engagement/   Cost and fee ledger.xlsx
            Board and Reg 30 disclosures/   (listed entities; links to 06)
    Regulator inspections/
        [Regulator] - [YYYY-MM-DD] - [Inspection]/  (inspection report, observations register.xlsx, compliance submissions, closure)
    Regulator correspondence log.xlsx
    Contracts register.xlsx                  (counterparty, type, value, start/end, renewal notice date, owner, key obligations, governing law)
    Contracts/ [Counterparty] - [Contract type] - [YYYY-MM-DD]/   (executed copy, amendments, obligations extracted.xlsx)
    Licences and permissions register.xlsx   (licence, issuer, number, conditions, validity, renewal due, linked checkpoints; certificates in 01/Registrations and licences)
    Ethics registers/
        Conflict of interest declarations.xlsx
        Gifts and hospitality register.xlsx
        Related-party approvals index.xlsx   (pointer to 06 RPTx records)
```
Privileged legal advice is exported only inside `99 Restricted/Legal - privileged.zip`.

### 27 ESG, BRSR and Sustainability *(v1.1; P27)*

```
27 ESG, BRSR and Sustainability/
    [Legal entity]/ [FY]/
        BRSR/                               (BRSR and BRSR Core workbook, XBRL instance, assurance report, board approval reference)
        CSR/                                (CSR policy, committee minutes pointers, annual action plan, projects register.xlsx, utilisation certificates, unspent account transfers, CSR-2 data, impact assessments)
        GHG inventory/                      (activity data by scope and category, emission-factor library version, calculation workbook, methodology note, assurance)
        Metrics/                            (energy, water, waste, people, governance KPIs with lineage)
        Materiality assessment/
        Climate risk/                       (scenario analysis, transition and physical risk register — links to 08/09)
        Data requests and evidence/         (supplier and site data submissions with hashes)
```

### 28 Reports, MIS and Board Packs *(v1.1; P28)*

```
28 Reports, MIS and Board Packs/
    Report catalogue.xlsx                    (report id, title, tier, owner, schedule, template version)
    [Report id] - [Title]/
        [YYYY-MM-DD] - run [id]/            (output PDF/XLSX/DOCX/PPTX, parameters.json, data snapshot hash, approval record)
    MIS packs/ [Tier L1–L4]/ [Period]/
    Board and committee packs/ [Body]/ [YYYY-MM-DD]/   (frozen, hashed pack — pointer to 05 for minutes)
    RBI inspection MIS file/ [Inspection]/
    Due-diligence snapshots/ [YYYY-MM-DD] - [Purpose]/  (frozen scope, watermarked PDF, access log)
    KPI dictionary.xlsx
```

### 29 AI Governance - Systems, Assessments and Incidents *(v1.1; OV_AI)*

```
29 AI Governance - Systems, Assessments and Incidents/
    AI system register.xlsx                  (system, owner, purpose, risk class, model/provider, data classes, autonomy level, status)
    [AI system]/
        Impact assessments/  Validation and testing/  Bias and fairness tests/
        Kill-switch tests.xlsx   Monitoring reports/   Approvals and board reporting/
    AI incidents register.xlsx
    Cross-framework control map.xlsx         (FREE-AI, MeitY guidelines, EU AI Act, ISO/IEC 42001, NIST AI RMF)
    Vendor AI assurance packs/               (including LawDocsComply's own pack — D-38)
```
LawDocsComply's own Vidhi agent activity, notebooks and MCP/A2A access logs remain in folder 18; folder 29 holds the client's governance of its own AI systems.

### 99 Restricted

```
99 Restricted/
    HR and Payroll.zip                   (AES-256; own manifest; employee files, payroll, attendance, leave, employment agreements)
    POSH Internal Committee.zip
    Whistle-blower.zip
    Grievances - complainant identity.zip
    Legal - privileged.zip
    Listed - UPSI and SDD.zip
    Health data.zip (if any)
    RESTRICTED-INDEX.csv                 (archive name, class, approvers, recipient, created — no contents)
```
Credentials are never exported (credential vault metadata only appears in `22 Settings and Customisations/Credential vault - metadata.xlsx`: portal, user-ID owner, last rotated, access grants — no secrets).

## M.4 File format matrix (binding)

| Record family | Human file(s) | Machine file(s) | Notes |
|---|---|---|---|
| Registers/lists | XLSX (formatted) | CSV + schema.json (+ JSONL in FULL/EXIT) | XLSX: "Read me" first sheet, frozen header, filters, typed cells, leading zeros, column comments from dictionary, split at 1,000,000 rows |
| Generated narratives | DOCX + PDF/A-2b | — | PDF XMP: `document_id`, source hash, version, status |
| Originals | as uploaded | — | byte-identical; `.sig`/audit certificate alongside |
| Type copies/translations | DOCX + PDF | — | next to original; label in name |
| Regulatory/bureau/tax files | exactly as submitted | — | + validation report XLSX, sign-off PDF, acknowledgement |
| Financial statements | XLSX (schedules) + PDF | CSV | presentation per applicable framework (Schedule III / RBI / IRDAI formats) |
| Calendars | XLSX list | ICS | — |
| Audit trail | XLSX digest per month | JSONL per month + anchors | hash chain verifiable offline |
| Emails/chats | original + DOCX/PDF transcript | XLSX table | — |
| Settings | XLSX | JSON (signed) | — |
| Dashboards | PDF snapshot + XLSX data | CSV | figures as of export |

Date/time: ISO 8601 with offset (`2026-10-31T18:30:00+05:30`); amounts as fixed 2-decimal strings with currency column; no thousands separators in CSV; code + label columns for coded fields; booleans `Y`/`N` in human files, `true`/`false` in machine files.

## M.5 Naming rules (binding; examples)

1. Plain English, Title Case for folders; files may use sentence case.
2. Windows-safe: forbidden characters `\ / : * ? " < > |`; no trailing dot/space; no reserved names (`CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9`); replace `/` in titles with `-`, `:` with ` -`.
3. Unicode NFC; non-Latin titles (e.g. Hindi) allowed but a transliterated English title is used for paths by default (`xpt.folder.path_script = latin`) to avoid tool incompatibilities.
4. Full path ≤ 240 characters; shorten titles from the right and append ` - {short id}`.
5. Dates first for dated items: `2026-08-14 - Board Meeting 3 of FY 2026-27`.
6. Versions and status: `v3.0 - APPROVED 2026-05-12`, `v3.1 - DRAFT`, `v2.1 - SUPERSEDED 2026-05-12`.
7. No personal data in names: employees by `EMP-000123`, complainants by `GRV-2026-000456`, directors by DIN only when the tenant enables `id_and_masked_name` (DIN is published data, but default remains id-only for portability to non-company contexts) [REC].
8. Duplicate names in one folder get ` (2)`, ` (3)` suffixes deterministically by creation time.
9. Numbered top-level folders and `00 Start Here` are locked; tenant renames below level 1 are allowed via folder policy (M.11).

## M.6 Manifest schemas

### M.6.1 `export-manifest.csv` columns

`path, sha256, bytes, media_type, record_count, legal_entity, dataset, schema_version, as_of, created_at, source_ids, restricted, retention_class, legal_hold, upsi` (Spec §12.1) **+** `record_type, canonical_path, department_id, fy, module, obligation_refs, content_version, archive_part`.

### M.6.2 `manifest.json` (excerpt)

```json
{
  "archive_id": "arc_01JC8Q4V6R3W2T7Y9X0Z1A2B3C",
  "archive_standard_version": "1.0",
  "folder_profile": "ldc_tenant_v1",
  "folder_profile_version": "1.0.0",
  "producer": {"product": "ldc", "release": "2026.11.2", "environment": "production"},
  "tenant": {"tenant_id": "ten_01J…", "reid": "re_01J…", "legal_entities": ["le_01J…"]},
  "scope": {"code": "FULL_TENANT", "filters": {}, "restricted_included": ["HR"]},
  "requested_by": {"user_ref": "usr_01J…", "role": "ten_admin"},
  "approvals": [{"user_ref": "usr_01J…", "role": "ten_cco", "at": "2026-10-31T17:02:11+05:30"}],
  "as_of": "2026-10-31T18:00:00+05:30",
  "control_totals": [{
    "legal_entity": "le_01J…",
    "counts": {"obligation": 1240, "compliance_instance": 18620, "evidence_document": 42110, "policy_version": 212, "meeting": 96, "resolution": 431, "risk": 188, "kri_observation": 9120, "audit_finding": 377, "return_run": 640, "grievance_case": 2210, "task": 30115, "audit_event": 1840033},
    "documents": {"count": 61022, "bytes": 182334455667},
    "audit_chain": {"last_anchor_date": "2026-10-31", "last_anchor_hash": "…"}
  }],
  "predecessor_archive_id": null,
  "files": "see export-manifest.csv",
  "pack_sha256": "…",
  "signing_key_id": "ten_01J…-export-2026"
}
```

`manifest.json.jws`: detached JWS (RFC 7515/7797), `alg` ES256 or EdDSA, `kid` = signing key id; public key in `00 Start Here/verify/public-key.pem` and fingerprint in the README.

## M.7 Data dictionary

`data-dictionary.xlsx` sheets: `Datasets` (dataset, description, file, record type, key, legal basis/retention class), `Fields` (dataset, field, label, description, type, length, mandatory, example, code table, data class, JSON Pointer to canonical model), `Code tables` (index), `Changes` (field-level changes since profile 1.0.0). CSV twin for machine use.

## M.8 `relationships.csv`

`from_dataset, from_field, to_dataset, to_field, cardinality, description` — e.g. `compliance_instance.obligation_id → obligation.obligation_id (many-to-one)`, `evidence_link.document_id → document.document_id`, `resolution.meeting_id → meeting.meeting_id`, `finding.engagement_id → engagement.engagement_id`, `policy_version.policy_id → policy.policy_id`, `audit_event.record_id → *.id (polymorphic by record_type)`.

## M.9 README template (sections)

1. What this archive is (scope, organisation, as-of time, who requested and approved)
2. How the folders are organised (with the one-page map)
3. Finding common things (worked examples: "the evidence for a compliance item", "the approved version of a policy and its Board approval", "minutes of a meeting", "who changed a status and why")
4. Opening files (Excel/LibreOffice tips: CSV import with text columns to keep leading zeros; PDFs; Word files with tracked changes)
5. Verifying the archive (checksums and signature: `sha256sum -c`, `Get-FileHash -Algorithm SHA256`, `CertUtil -hashfile <file> SHA256`; `ldc-verify` usage)
6. Joining tables (keys, `relationships.csv`)
7. Restricted archives (what they are, who received passwords, how to handle)
8. Retention and legal holds (what must be kept and for how long; holds present)
9. Glossary (obligation, compliance instance, maker, checker, evidence, correction entry, content version, overlay, applicability, attestation, KRI, RCSA, ICAAP, return run, acknowledgement)
10. Contacts (tenant's designated officer; LawDocsComply support for archive questions)
A CI test asserts every folder named in the README exists and every top-level folder is described.

## M.10 BSA 2023 section 63 certificate (pre-filled template outline)

Prepared as DOCX (editable) and PDF. Contents [VERIFY against the Schedule form under the Bharatiya Sakshya Adhiniyam 2023]:
- **Part A — by the party** (tenant's authorised officer): identity and designation; description of the electronic records (this archive, `archive_id`, scope, as-of); the computer system/device and the service (LawDocsComply, hosted in India by [hosting entity]); statement that the records were produced in the ordinary course of activities; that information was regularly fed; that the system operated properly or any defects did not affect accuracy; hash values (SHA-256 of `manifest.json`, pack hash) and hash algorithm; date, place, signature.
- **Part B — by the expert**: identity and qualifications of the expert; verification performed (hash recomputation, signature validation, chain-anchor checks with `ldc-verify` report reference); hash values; signature.
- **Annex**: `ldc-verify` report; LawDocsComply Platform Statement (hosting, access controls, audit ledger, hashing, timekeeping source — NTP/time-stamping; signed by LDC's designated officer with DSC).

## M.11 Folder policy — tenant customisation bounds

| Element | Customisable? | Rule |
|---|---|---|
| Top-level numbers and names | No (locked) | Ensures cross-tenant familiarity and tooling |
| `00 Start Here` | No | Spec §12.1 |
| Entity level | Yes (`auto`/`always`/`never`) | — |
| FY label format | Yes (`FY 2026-27`, `FY26-27`, `CY 2026`, custom) | Must sort chronologically |
| Department names | From terminology registry; historical or current mode | IDs in manifest |
| Splitting a folder (e.g. by branch) | Yes, below level 2 | `canonical_path` unchanged |
| Language of README | English + optional Hindi | — |
| People naming mode | DPO-approved only | default ids_only |
| Custom subfolders in Documents Library | Yes | Mirrors tenant DMS |

Every folder-policy version is a ledger event; exports record the policy version used.

## M.12 Incremental packages

Daily incrementals contain only changed/new records and new document versions since the predecessor archive, plus: full `export-manifest.csv` for the delta, a cumulative `state-index.csv` (record id → latest archive id containing it) and deletions/retention events (`deleted-records.csv` with retention basis; no content). `ldc-load` assembles the latest state from a full archive + chain of incrementals; `ldc-verify` validates the chain (`predecessor_archive_id` links, no gaps).

## M.13 Reverse mapping for intake (P19 §4F)

- An LDC package is recognised by `00 Start Here/manifest.json` + valid JWS → exact placement by `canonical_path`, `record_type` and record ids.
- Non-LDC trees: path segments matched against (in order) legal-entity names/CIN, FY patterns (`FY ?\d{2,4}-\d{2,4}`, `\d{4}-\d{2}`, `F\.?Y\.? ?\d{2}`), department names and aliases, LDC top-level folder names and common synonyms (e.g. "Board Meetings", "BM", "Minutes" → folder 05; "Policies", "Policy Manual" → 07; "Audit", "IA", "Concurrent" → 10; "Returns", "RBI Returns", "CIMS", "XBRL" → 11; "ROC", "MCA", "Forms" → 06), committee names, policy names, instrument short names and obligation short titles; file-name patterns for dates, versions, statuses and form numbers; content classification as fallback.
- Confidence = weighted combination; ≥ 0.85 auto-proposed; 0.5–0.85 needs confirmation; < 0.5 to review queue.

## M.14 Verification tests (CI and quarterly)

1. Full synthetic archive verifies; one changed byte fails; one missing file fails; a renamed file fails (path not in manifest).
2. README names every folder; every top-level folder described.
3. All Office files render headless; all PDFs pass PDF/A-2b (veraPDF).
4. CSV files open in Excel with leading zeros preserved when imported as text per README instructions (manual check quarterly) and schema-validate against `schemas/`.
5. No personal data in paths (scanner for PAN, Aadhaar, phone, email, names in people folders).
6. No Aadhaar numbers anywhere; no credentials anywhere.
7. Restricted archives open only with the delivered password; their manifests verify.
8. Control totals match live counts at as-of.
9. Golden-tenant path stability across releases (P19 FR-P19-26).
10. Round-trip import into a new tenant yields 100% placement and equal counts.

## M.15 Export-map seed — record type → canonical path and files

Seed of `xpt.export_map` for profile `ldc_tenant_v1` 1.0.0 (v1.1 rows below raise it to 1.1.0). Placeholders: `{E}` legal entity, `{FY}` financial year label, `{D}` department (terminology, historical by default), `{date}` ISO date, `{id}` short id. Every module adds its record types here before its exit gate (NN-10).

| Record type | Module | Canonical path template | Files | Restricted |
|---|---|---|---|---|
| `organisation_profile` | core | `01 …/` | `Organisation profile.xlsx` | — |
| `legal_entity` | core | `01 …/` | `Legal entities.xlsx/.csv` | — |
| `registration` | core | `01 …/Registrations and licences/{regulator} - {type} - {number}/` | certificates | — |
| `department` | cfg | `01 …/` | `Departments and functions.xlsx` | — |
| `instrument_selection` | cmp | `02 …/` | `Applicable instruments.xlsx`, `Instruments removed.xlsx` | — |
| `applicability_decision` | pack | `02 …/` | `Applicability decisions.xlsx` | — |
| `obligation_overlay` | cmp | `02 …/` | `Tenant customisations of questions.xlsx` | — |
| `obligation` | cmp | `03 …/` | `Obligations master.xlsx/.csv` | — |
| `compliance_instance` | cmp | `03 …/{E}/{FY}/{D}/{instrument}/{obligation title} - obl_{id}/{period} - {status}/` | `Compliance record.pdf/.xlsx`, `Trail.xlsx`, `Evidence/` | — |
| `evidence_link` | cmp | (inside instance) `Evidence/` | originals + renditions | per document class |
| `exception` | cmp | `03 …/` | `Exceptions waivers and extensions.xlsx` | — |
| `compliance_issue` | cmp | `03 …/` | `Issues register.xlsx` | — |
| `attestation_campaign` | cmp | `03 …/Attestations/{date} - {name}/` | `responses.xlsx`, `summary.pdf` | — |
| `regulatory_update` | chg | `04 …/{date} - {authority} - {title}/` | `Source.pdf`, `What changed.pdf`, `Impact assessment.docx/.pdf`, `Tasks created.xlsx` | — |
| `content_change` | cnt | `04 …/` | `Content change log.xlsx` | — |
| `board_body` / `committee` | gov | `05 …/` | `Board and committee composition - history.xlsx`; `Terms of reference/` | — |
| `meeting` | gov | `05 …/{E}/{FY}/{body}/{date} - {meeting title}/` | `01 Notice and Agenda`, `02 Board Papers/`, `03 Attendance and Quorum.xlsx`, `04 Minutes - SIGNED.pdf`, `05 Resolutions passed.xlsx`, `06 Action items.xlsx` | board-confidential papers flagged |
| `circular_resolution` | gov | `05 …/{E}/{FY}/Circular Resolutions/{date} - {subject}.pdf` | PDF + XLSX index | — |
| `general_meeting` | gov | `05 …/{E}/{FY}/General Meetings/{date} - {type}/` | notice, explanatory statement, minutes, results | — |
| `statutory_register` | gov | `06 …/Statutory Registers/` | `{register name} - {form}.xlsx/.pdf` | members register PII masked |
| `mca_filing` | gov | `06 …/MCA Filings/{FY}/{date} - {form} - {purpose} - SRN {srn}/` | form, attachments, challan, acknowledgement | — |
| `lodr_filing` | gov | `06 …/Listed Company Compliance/LODR Filings/{FY}/{date} - {reg} - {subject}/` | filing + acknowledgement | — |
| `upsi_sdd_entry` | gov | `99 Restricted/Listed - UPSI and SDD.zip` | XLSX | UPSI |
| `director_declaration` | gov | `06 …/Director KYC and Declarations/{person id}/` | DIR-8, MBP-1, DIR-2 | PII |
| `fit_and_proper` | gov | `06 …/Fit and Proper/{FY}/` | declarations, assessments | PII |
| `policy` / `policy_version` | pol | `07 …/{policy name}/` | `v{x} - {status} {date}.pdf/.docx`, `Board approval`, `REDLINE.docx`, `Earlier versions/` | — |
| `policy_attestation` | pol | `07 …/{policy name}/` | `Attestations v{x}.xlsx` | — |
| `sop` | pol | `07 …/Procedures and SOPs/` | PDF/DOCX | — |
| `risk` | erm | `08 …/` | `Risk register - current.xlsx`, `- history.xlsx` | — |
| `risk_appetite` | erm | `08 …/Risk appetite statement/` | RAS PDF/DOCX + thresholds XLSX | — |
| `rcsa_campaign` | erm | `08 …/RCSA/{date} - {name}/` | responses, results | — |
| `kri`, `kri_observation` | erm | `08 …/Key Risk Indicators/` | definitions, observations by FY, breaches | — |
| `loss_event` | erm | `08 …/` | `Loss events.xlsx` | pseudonymised |
| `ratio_value` | ral | `09 …/` | `Financial ratios - monthly.xlsx` | — |
| `capital_run` | ral | `09 …/Capital adequacy/{date} - Capital computation.xlsx/.pdf` | — | — |
| `icaap_cycle` | ral | `09 …/ICAAP/{FY}/` | document, approval, computations | — |
| `stress_run` | ral | `09 …/Stress tests and scenario analysis/{date} - {scenario} v{x}/` | assumptions, results, report, approval | — |
| `alm_snapshot` | ral | `09 …/Liquidity and ALM/` | SLS, IRS | — |
| `audit_universe`, `audit_plan` | aud | `10 …/Audit universe and plans/` | XLSX/PDF | — |
| `engagement` | aud | `10 …/{audit type}/{FY}/{engagement} - {period}/` | `01 Planning/`…`06 Follow-up and closure.xlsx` | workpapers may be restricted (privileged) |
| `finding` | aud | `10 …/` | `Findings tracker - all audits.xlsx` + in engagement | — |
| `inspection` (projection) *(X1)* | aud | `10 …/Regulatory Inspections/{date} - {regulator} - {type}/` | closure-test workpapers + link file; owner record exported by `lit` under `26 …/Regulator inspections/` | — |
| `return_definition` | ret | `11 …/` | `Return calendar {FY}.xlsx` | — |
| `return_run` | ret | `11 …/{regulator}/{code} - {name}/{FY}/{period} - {status}/` | upload file (byte-identical), validation, sign-off, ack, source mapping | — |
| `bureau_file` | ret | `11 …/Credit Information Companies/{CIC}/{cycle} - {ref date}/` | submitted file, rejection, DQI | file contains personal data → restricted if exported outside an RE-only scope |
| `tax_export` | ret | `11 …/GST and Tax/{return}/{period}/` | utility file, working papers | — |
| `trial_balance`, `financial_statements` | acc | `09 …/` or `11 …/` per use; master copy `10 …/Statutory Audit support/{FY}/` | XLSX/PDF | — |
| `ropa`, `dpia` | dpc | `12 …/` | XLSX; `DPIAs/{date} - {processing}/` | — |
| `consent_record` | dpc | `12 …/` summary; details `99 Restricted` | — | PII |
| `dsr` | dpc | `12 …/` | log | PII masked |
| `incident` | dpc | `12 …/Incidents and breaches/{date} - INC-{ref}/` | report, notifications, timeline, RCA | — |
| `control`, `control_test` | dpc | `12 …/` | `ISMS controls and tests.xlsx` | — |
| `cmp_control`, `control_execution` *(X1)* | cmp | `03 …/Controls and Control Executions/` | XLSX + evidence | — |
| `test_cycle`, `test_sample`, `remediation_item` *(X1)* | cmp | `03 …/Compliance Testing/{FY}/{cycle} - {status}/` | PDF, XLSX | — |
| `request_list`, `request_item` *(X1)* | cmp | `03 …/Request Lists/{date} - {name}/` | XLSX + accepted evidence | — |
| `ccm_test`, `ccm_run` *(X1)* | cmp | `03 …/Automated Check Results/{test} - {FY}/` | XLSX + snapshots | — |
| `coop_audit_para`, `registrar_inspection` *(X1)* | coop | `15 …/` | XLSX, PDF | — |
| `vendor`, `outsourcing_arrangement`, `vendor_assessment` | tpr | `12 …/Third parties and outsourcing/` | registers, assessments | — |
| `vapt_report` | dpc | `12 …/VAPT and security assessments/{date} - {scope}/` | report, remediation | — |
| `employee`, `payroll_run`, `attendance`, `leave` | hr | `99 Restricted/HR and Payroll.zip` | XLSX/PDF | HR |
| `org_unit`, `position` | hr | `13 …/` | org chart, positions | — |
| `labour_register` | lab | `13 …/Labour Code registers/{FY}/` | prescribed registers | PII per register (masked in non-restricted copy) |
| `labour_return` | lab | `13 …/Labour returns and filings/{return}/{period}/` | files | — |
| `posh_case` | lab | `99 Restricted/POSH Internal Committee.zip` | — | POSH |
| `employment_agreement` | lab | `99 Restricted/HR and Payroll.zip` (index in 13) | signed PDFs | HR |
| `grievance_case` | grv | `14 …/` register (masked); files `99 Restricted/Grievances - complainant identity.zip` when sealed | — | PII |
| `support_ticket` | grv | `14 …/` | summary | PII masked |
| `society_member`, `share_capital` | coop | `15 …/` | registers (masked) | PII |
| `society_meeting`, `election` | coop | `15 …/General Body Meetings/`, `Managing Committee/`, `Elections/{year}/` | notices, minutes, results | — |
| `task`, `approval`, `delegation` | wf | `16 …/` | XLSX/CSV | — |
| `calendar_item` | wf | `16 …/Calendar/` | ICS + XLSX | — |
| `document` | dms | `17 …/{tenant folder path}/` | originals + versions + renditions | per class |
| `ai_run`, `ai_output`, `notebook`, `ai_schedule`, `memory_item` | ai | `18 …/` | XLSX, DOCX | — |
| `engagement_order`, `retainer`, `sla` | mkp | `19 …/{date} - {provider} - {service}/` | signed SLA, deliverables, invoices | — |
| `subscription`, `invoice`, `payment`, `savings_entry` | bil | `20 …/` | XLSX, invoice PDFs | — |
| `user`, `role_assignment`, `access_review`, `external_access_grant`, `breakglass_session` | iam | `21 …/` | XLSX | business contact PII |
| `setting`, `terminology`, `folder_policy`, `nav_config`, `rule_pack_pin` | cfg/xpt | `22 …/` | JSON (signed) + XLSX | — |
| `credential_vault_entry` | sdc | `22 …/Credential vault - metadata.xlsx` (metadata only) | — | secrets never exported |
| `connector_instance`, `mapping_override`, `webhook_subscription`, `reconciliation_report` | int | `23 …/` | XLSX/YAML | — |
| `audit_event`, `correction_entry`, `chain_anchor` | core | `24 …/` | JSONL + XLSX + CSV | — |
| `cell_migration` | core/xpt | `24 …/Migrations/{date} - {entity} - {from}-{to}/` | `migration-manifest.json`, deletion certificate | — |

**Export-map rows added in v1.1** *(v1.1)*

| Record type | Module | Canonical path template | Files | Restricted |
|---|---|---|---|---|
| `group_entity`, `ownership_link` | gem | `25 …/` | `Group structure - global.xlsx/.pdf` | — |
| `foreign_entity`, `officer`, `foreign_register`, `foreign_filing` | gem | `25 …/{country} - {entity}/…` | XLSX, filed copies | officer personal data minimised |
| `jurisdiction_pack_pin`, `coverage_statement` | cnt/gem | `25 …/Jurisdictions in use.xlsx`, `Coverage statements/` | XLSX, PDF | — |
| `expert_note` | prt | `25 …/{country} - {entity}/Expert notes.xlsx` | XLSX | tenant-private |
| `legal_matter`, `hearing`, `order`, `matter_cost` | lit | `26 …/Matters/{yyyy} - {id} - {title}/` | register XLSX, PDFs | privileged advice → 99 |
| `regulator_inspection`, `inspection_observation` | lit | `26 …/Regulator inspections/{regulator} - {date} - {name}/` | PDFs, XLSX | regulator-confidential → 99 if flagged |
| `contract`, `contract_obligation` | lit | `26 …/Contracts/{counterparty} - {type} - {date}/` | executed copy, XLSX | — |
| `licence` | lit | `26 …/Licences and permissions register.xlsx` | XLSX | — |
| `coi_declaration`, `gift_entry` | lit | `26 …/Ethics registers/` | XLSX | personal data minimised |
| `brsr_report`, `csr_project`, `ghg_inventory`, `esg_metric`, `materiality_assessment` | esg | `27 …/{E}/{FY}/…` | XLSX, XBRL, PDF | — |
| `report_definition`, `report_run`, `mis_pack`, `board_pack`, `dd_snapshot`, `kpi_definition` | rpt | `28 …/` | outputs + parameters.json + snapshot hash | per report confidentiality |
| `ai_system`, `ai_assessment`, `ai_validation`, `ai_incident`, `ai_control_map` | aig | `29 …/` | XLSX, PDF | — |

## M.16 "Where do I find…?" (included in `Folder guide.xlsx` and the README)

| Question | Where |
|---|---|
| Was a particular compliance done, by whom, with what proof? | `03 …/{entity}/{FY}/{department}/{instrument}/{obligation}/{period}/` → `Compliance record.pdf` and `Evidence/` |
| What was the text of the requirement at the time, and what changed later? | `02 …/Content versions pinned.csv` and `04 …/Content change log.xlsx` |
| Which regulations did we decide applied to us, and when did we remove any? | `02 …/Applicable instruments.xlsx`, `Instruments removed.xlsx` |
| Did we change the standard question text for our company? | `02 …/Tenant customisations of questions.xlsx` |
| What did the Board decide on a date? | `05 …/{entity}/{FY}/Board of Directors/{date} - …/04 Minutes - SIGNED.pdf` and `05 Resolutions passed.xlsx` |
| Who were the committee members in a year? | `05 …/Board and committee composition - history.xlsx` |
| Which version of a policy was in force on a date, and when did the Board approve it? | `07 …/Policy register.xlsx` → `{policy}/` files with `APPROVED {date}` |
| What changed between policy versions? | `07 …/{policy}/… REDLINE.docx` |
| What were our capital adequacy and key ratios each month? | `09 …/Financial ratios - monthly.xlsx`, `Capital adequacy/` |
| What did the internal auditor find and is it closed? | `10 …/Findings tracker - all audits.xlsx` |
| What exactly did we file with the regulator and did they acknowledge it? | `11 …/{regulator}/{return}/{FY}/{period}/` |
| Which complaints did we receive and how fast did we resolve them? | `14 …/Grievance register {FY}.xlsx` |
| Who had access to the system and who approved it? | `21 …/Role assignments - history.xlsx`, `Access reviews/` |
| Who changed anything, when and why? | `24 Audit Trail/Audit trail {YYYY-MM}.xlsx`; corrections in `Corrections register.xlsx` |
| How do I know nothing was altered? | `00 Start Here/README` → "Verifying the archive"; run `verify/ldc-verify` |
| Where are employee and payroll files? | `99 Restricted/HR and Payroll.zip` (password with the named recipient) |

**"Where do I find…?" rows added in v1.1** *(v1.1)*

| Question | Where |
|---|---|
| Our foreign subsidiaries and what they must file | `25 Global Entities and Jurisdictions/[Country] - [Entity]/Filings/` and `Group compliance map.xlsx` |
| The status of a court case or notice | `26 Legal Matters, Contracts and Licences/Legal matters register.xlsx` → matter folder |
| What RBI observed in the last inspection and what we did | `26 …/Regulator inspections/` |
| Which contracts renew next quarter | `26 …/Contracts register.xlsx` (filter on renewal notice date) |
| Our BRSR and its assurance report | `27 ESG, BRSR and Sustainability/[Entity]/[FY]/BRSR/` |
| A board pack exactly as circulated | `28 Reports, MIS and Board Packs/Board and committee packs/` |
| Which AI systems we use and how they were assessed | `29 AI Governance - …/AI system register.xlsx` |

## M.19 Multi-region packaging *(v1.1; Appendix Y §Y.7; NN-24 as amended)*

1. **One package per cell.** A tenant whose legal entities sit in several cells receives one LDC-EXPORT package per cell, each produced and checksummed in that cell; packages are never merged server-side across cells unless a transfer basis is recorded.
2. **Group index.** A small `00 Group Index/` package (produced in the group home cell from aggregates only) lists every per-cell package, its cell, entities, checksum, period and download location, plus the group-level folders that live in the group home cell (group policies, group risk appetite, 25 group structure).
3. **Root naming.** `LawDocsComply Export - [Organisation] - [Cell] - [YYYY-MM-DD]` (cell in plain words: India, European Union, Gulf, Singapore, United States).
4. **README.** States the cell, the governing data-protection regime, and that the other cells' packages are needed for a complete group record.
5. **Storage targets.** Each per-cell package may go to a different customer storage target (e.g., EU package to an EU-region bucket); the export wizard warns if a chosen target sits outside the package's cell and requires a recorded basis (LDC-INT-131).

## M.20 Home-cell migration manifest *(v1.1)*

When a legal entity's home cell changes (Governed migration, P19 FR-P19-49), the source cell produces a complete LDC-EXPORT package for that entity plus `migration-manifest.json` (entity id, from/to cell, record counts per type, per-file hashes, ledger chain head, transfer basis id, approvers). The destination cell imports it, verifies every hash and count, continues the audit chain with a migration anchor, and the source cell keeps only the legally required minimum (with deletion certificate after the retention period). The manifest and certificates appear in `24 Audit Trail/Migrations/`.

## M.21 Exit runbook and escrow *(v1.1; G5 gap TM-404)*

A published **Exit Runbook** (customer-facing, linked from the Trust Centre and every contract) supports RBI outsourcing exit-plan expectations for RE customers: (a) notice and the 90-day post-termination read-only window (NN-42); (b) full LDC-EXPORT package plus database-schema documentation and a reference loader for PostgreSQL; (c) transition assistance (hours and rate card in Appendix N, delivered through P22); (d) optional **data escrow** (periodic encrypted package deposited with an escrow agent) and **source-code escrow** for Enterprise contracts (commercial add-on in P20; escrow agent and release conditions [OWNER TO SET]); (e) deletion certificate after the agreed retention, except legal-hold data. The runbook is a sales asset and a regulator-ready document.

## M.22 Intake reverse-mapping for the new folders *(v1.1; NN-49)*

The folder-intake mapper (P19 §4F) recognises folders 25–29 and their sub-folders when a customer re-imports an LDC package or uploads a folder tree that follows the same names; unknown sub-folders become proposed custom registers or document folders. Every intake is a single change set reversible for 24 hours (`xpt.intake.undo_window_hours`).

## M.17 Open items

| OI | Item | Owner | Fallback |
|---|---|---|---|
| OI-M-01 | BSA s.63 Schedule form exact text and Part B signatory practice | General Counsel | Template marked "to be settled by counsel" |
| OI-M-02 | Statutory form layouts for registers (MGT-1, MBP-2, MBP-4, CHG-7, BEN-3, SH-6) — confirm current forms | Company Secretary (P06) | XLSX with prescribed columns; PDF rendering per form |
| OI-M-03 | Labour Code register names and formats under central/state rules | P13 owner | Names as per rule pack |
| OI-M-04 | Hindi README and path-script policy | Content team | English, Latin paths |

## M.18 Sources

Ecosystem Integration Specification v1.1 §12, §12.1, §12.2, §13.2, §6.26; Bharatiya Sakshya Adhiniyam 2023 s.63 and Schedule [VERIFY]; Companies Act 2013 ss.88, 118, 128, 170, 186, 189 and the Companies (Management and Administration) Rules 2014 / (Meetings of Board and its Powers) Rules 2014 forms (MGT-1, MBP-1, MBP-2, MBP-4), Companies (Registration of Charges) Rules 2014 (CHG-7), Companies (Significant Beneficial Owners) Rules 2018 (BEN-3), Companies (Share Capital and Debentures) Rules 2014 (SH-6) [LAW; P06 confirms]; ICSI SS-1 and SS-2; ISO 19005-2 (PDF/A-2); ISO/IEC 29500; RFC 4180, 7515, 7797; JSON Schema 2020-12; Microsoft Windows file-naming conventions (reserved names and characters).


**v1.1 changes (25 October 2026)** *(v1.1)*

- Five new top-level folders appended after 24 (never renumbered): **25 Global Entities and Jurisdictions** (P25), **26 Legal Matters, Contracts and Licences** (P26), **27 ESG, BRSR and Sustainability** (P27), **28 Reports, MIS and Board Packs** (P28), **29 AI Governance - Systems, Assessments and Incidents** (OV_AI in P12; Appendix AA §AA.12). Vidhi's own notebooks and agent activity stay in folder 18.
- Export profile `ldc_tenant_v1` moves to **1.1.0** (additive only; a v1.0 package remains readable; golden-export gate NN-45).
- New §M.19 multi-region packaging (per-cell packages + group index) and §M.20 home-cell migration manifest (NN-24 as amended; Appendix Y §Y.7).
- New §M.21 exit runbook and optional escrow (G5 gap TM-404) and §M.22 intake reverse-mapping for the new folders with the 24-hour undo window (NN-49).
- Export-map seed (§M.15) and the 'Where do I find…?' table (§M.16) extended for the new record types; MBP-1 file relabelled as a disclosure index (X-37); Annual Reports sub-folder under 06.

---

**Master integration note (pack lead, 25 October 2026).** This appendix is read with master §4 and §18, in particular X-27 (these folder names are authoritative), NN-10, NN-45. Where text above conflicts with them, the master prevails.
