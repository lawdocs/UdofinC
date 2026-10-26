# Appendix K — Export Package `LD-EXPORT-1.0` and Folder Taxonomy

> **Status:** Binding. LawDocs Build Prompt Pack v1.0, 25 October 2026. Owner: P20.
> **Used by:** P20 (builder, import, BYO storage), P03 (configuration bundle), P04 (folder views and categories), every phase that registers record types in `xpt.export_map` (NN-11), P21 (help articles on exports), P23 (golden archives).
>
> **How to use.** This appendix fixes every top-level folder, sub-folder pattern, file name, file format, manifest column and README section of a LawDocs export, and the reverse rules used to import folders. It implements the Infrabyx Ecosystem Integration Specification v1.1 §12.1 archive standard 1.0 (which prevails on conflict) as four LawDocs **folder profiles**. A module adding a record type adds an export-map entry (§K.11) in the same pull request; CI rejects the PR otherwise. Paths are computed at export time from canonical IDs; they are never storage keys (NN-12).

---

## K.0 Profiles, versions and precedence

| Profile | Used for | Year label default | Person-naming default |
|---|---|---|---|
| `ld_company_v1` | Company workspace (any company, LLP, firm, society or other organisation) | `FY 2026-27` (Indian FY, April–March) | `masked_name` |
| `ld_individual_v1` | Personal workspace (individual and family) | `2026` (calendar year) | `full_name` (own archive) |
| `ld_professional_v1` | Practice workspace of an advocate, CA, CS, tax practitioner or firm | `FY 2026-27` | `masked_name` |
| `ld_consumer_help_v1` | A user's cases under `[Consumer Help Brand]` | `2026` | `ids_only` (LOCKED) |

Version: `LD-EXPORT-1.0` = archive standard 1.0 + each profile at 1.0.0. Semantic versioning per profile (P20 FR-P20-41): patch (wording), minor (additive folders, files, columns), major (any change to an existing path template or column meaning; compatibility map required). The four profiles are proposed for registration in Ecosystem Spec v1.2 through Appendix Y; until registered, any archive shared with another Infrabyx product uses `ids_only` naming.

**Reconciliation with conventions §14 and Appendix Y §Y.11.2 (X-07: this appendix governs; conventions §14 is superseded).** Conventions §14 summarises the root as `LawDocs Export – <Name> – <YYYY-MM-DD>/` with `manifest.json` and `checksums.sha256` at the root; Ecosystem Spec §12.1 requires `[Owner legal name] - [Product] Archive - [scope] - as of [YYYY-MM-DD]/` and a mandatory `00 Start Here/`. Following the resolution proposed in Appendix Y §Y.11.2, this appendix uses the Spec root name (ASCII hyphens), adds the full `00 Start Here/` (with `manifest.json`), and keeps `00 READ ME FIRST.pdf`, `00 Index.xlsx` and `checksums.sha256` at the root for beginners and `sha256sum -c` users. Names: archives delivered to the data owner's own destination use the Appendix Y naming mode **`owner_readable`** (counterparty names and titles allowed; natural persons per `xpt.naming.person_mode`); archives for anyone else (auditor, court bundle, ecosystem share, regulator) use `ids_only` or `id_and_masked_name` per Spec §12.1.

---

## K.1 Root folder

```
<Owner name> - LawDocs Archive - <Scope> - as of <YYYY-MM-DD>/
├── 00 READ ME FIRST.pdf                 plain-language guide + one-page folder map
├── 00 Index.xlsx                        every record and file, with clickable links
├── checksums.sha256                     SHA-256 of every file, for `sha256sum -c` (Appendix Y §Y.11.2)
├── 00 Start Here/                       mandatory (Spec §12.1), identical in every profile
├── 01 … 12                              profile folders (§K.3; `12 Tax` in the company profile only)
└── 99 System Data (CSV and JSON)/       datasets, audit trail, settings, items
```

- `<Owner name>`: the organisation's legal name (Company, Professional) or the account holder's display name (Individual; option `account_ref` instead of the name via `xpt.naming.root_owner_label`); Consumer Help uses `LD-CH account <ref>`.
- `<Scope>`: `Full`, `Exit`, `FY 2026-27`, `2026`, `Department - Legal`, `Agreement LD-AGR-2026-000123`, `Case LD-CAS-2026-000045`, `Court Bundle LD-CAS-…`, `Audit Pack - <grant ref>`, `Backup YYYY-MM-DD`, `Incremental YYYY-MM-DD HHmm`.
- Multi-part downloads: `… - Part 01 of 07.zip`; `parts-manifest.csv` lists parts with SHA-256.

---

## K.2 `00 Start Here/` (mandatory, identical structure in every profile)

| File or folder | Content |
|---|---|
| `README.pdf`, `README.docx`, `README.txt` | Template §K.7; English, plus one optional D-07 language as a labelled machine translation |
| `export-manifest.csv` | One row per file (§K.6.1) |
| `manifest.json` | Archive metadata and control totals (§K.6.2) |
| `manifest.json.jws` | Detached JWS over `manifest.json` (RFC 7515/7797; ES256 or EdDSA) |
| `data-dictionary.xlsx`, `data-dictionary.csv` | Datasets, fields, types, code tables, data classes (§K.6.6) |
| `relationships.csv`, `relationship-map.pdf` | How datasets join (§K.6.7) |
| `code-tables/` | One CSV per code table (statuses, item types, party types, document types, forums, States, reason codes) with `code,label,canonical_meaning,valid_from,valid_to` |
| `schemas/` | JSON Schema 2020-12 per dataset |
| `verify/` | `ld-verify` (Windows, macOS, Linux builds), `public-key.pem`, `HOW-TO-VERIFY.txt`, licence (Apache-2.0) |
| `Folder guide.xlsx` | Every folder: what it holds, typical questions it answers, record types, count |
| `CHANGES-SINCE-PREVIOUS.csv` | For repeat, scheduled and incremental exports: added, changed and removed records; new folders or columns (minor profile changes) |
| `path-map.csv` | Only after a profile major: `old_path,new_path,record_id` |
| `BSA Section 63 Certificate (draft).docx` / `.pdf` | Pre-filled Part A and Part B drafts with hash values; LawDocs Platform Statement annex (NN-10) [VERIFY wording against the Schedule] |
| `Restricted archives.txt` | List of encrypted archives included, recipients, how passwords were delivered (never the passwords) |
| `Deletion certificate.pdf` | Exit packages only, after deletion completes (issued later and re-signed) |

---

## K.3 Folder taxonomy

Notation: `<…>` placeholders; `{…}` optional level controlled by folder policy (§K.8); `[R]` restricted part produced as an encrypted archive (P20 FR-P20-08). Every record folder ends with ` (<business reference>)` when a reference exists. Each record folder contains a one-page summary PDF and, where items exist, `Open and Waiting Items.xlsx`.

### K.3.1 Company profile `ld_company_v1`

```
01 Company Profile/
    Company details.pdf · Company details.xlsx (names, CIN/LLPIN, GSTIN, PAN masked except last 4, addresses, entities)
    {<Entity name>/} Registrations and Licences/ · Authorised Signatories and Delegations/
    Departments and Teams.xlsx · Users and Roles summary.xlsx
    Reports and Dashboards/<YYYY-MM-DD> - <Dashboard name>.pdf + .xlsx
    DigiLocker references.xlsx + .csv (KYB documents held as URI and verification result only — NN-42; P04)
    Credential Vault (metadata only)/ (register, grants, reveal log — never secrets; P18, NN-16)
    Change History/ (master-data requests and Correction Entries made by LawDocs; P18, CH-26)
    System of record changes/ (LDC/LawDocs SoR switches and reconciliation reports; P19)
    Onboarding/ (the company's own onboarding invitation and checklist; P19)
    Account and Exit/ (plan history, exit records, deletion certificates)

02 Agreements and Contracts/
    {<Entity>/}<FY>/{<Department>/}<Counterparty> - <Agreement title> (LD-AGR-2026-000123)/
        Agreement summary.pdf
        01 Drafts/                      <YYYY-MM-DD> - v<n> - DRAFT.docx (+ .pdf)
        02 Negotiation and Redlines/    Round <nn> - <YYYY-MM-DD> - <From party> - REDLINE.docx (+ .pdf); Negotiation log.xlsx
        03 Signed and Stamped/          <Title> - v<n> - SIGNED.pdf; Stamp certificate - <State> - <UIN>.pdf; Stamp details.pdf;
                                        Registration and formalities/ (appointments, registration receipts, notarised copies; P08)
        04 Evidence and Certificates/   Evidence pack.pdf; Signing record.xlsx; signature-events.jsonl; provider responses/;
                                        BSA s63 certificate (draft).docx; Rule decisions.xlsx
        05 Amendments and Renewals/     <YYYY-MM-DD> - Amendment <n> (LD-AGR-…)/ (same sub-structure, nested); Renewal history.xlsx
        06 Correspondence/              Conversation - <thread>.pdf; Signing messages.pdf; emails as .eml + .pdf; notices
    Drafts not yet negotiated/<YYYY>/<Title> (<draft ref>)/   template drafts that never became an agreement (P06 §13; G3 K-2)
        (Unattached document versions elsewhere in the vault keep earlier versions in a `_versions/` sub-folder of the document's folder — P04.)
        Obligations.xlsx · Open and Waiting Items.xlsx
    Agreements register <FY>.xlsx (one per FY at this level)

03 Litigation and Disputes/
    <Year>/<Forum>/<Case title> (LD-CAS-2026-000045)/
        Case summary.pdf · Case status history.xlsx (source and fetched-at for each status — no "real-time" claim)
        01 Pleadings and Filings/       <YYYY-MM-DD> - <Pleading type> - v<n> - FILED.pdf (+ .docx)
        02 Orders and Judgments/        <YYYY-MM-DD> - Order - <short description>.pdf; certified copies
        03 Hearings/                    <YYYY-MM-DD> - Hearing - <purpose>.pdf (notes, outcome)
        04 Evidence and Annexures/      originals; <name> (Type copy - <status>).docx/.pdf; <name> (Translation - English - Machine).docx;
                                        <name> (Certified translation - English).pdf; WhatsApp chats: <chat> (Messages).xlsx beside the original ZIP; s63 certificates
        05 Notices and Correspondence/
        06 Counsel and Costs/           engagement letters, invoices (legal spend)
        Open and Waiting Items.xlsx
    <Year>/Other Matters/<Matter title> (LD-MAT-2026-000067)/  (pre-litigation, advisory, arbitration, mediation — same sub-structure where relevant)
    Litigation register <Year>.xlsx · Hearings calendar.ics + .xlsx
    (<Forum> examples: "Supreme Court of India", "Delhi High Court", "District Court - Jaipur", "NCLT - Mumbai Bench", "Consumer Commission - District - Pune", "Arbitration", "Mediation")

04 Trademarks and IP/
    <Mark or asset name> (LD-TMK-2026-000012)/
        Application and Filings/ · Examination and Replies/ · Opposition/ · Registration Certificate/ · Renewals/ · Watch Reports/ · Correspondence/
        Asset summary.pdf · Status history.xlsx (source and fetched-at)
    IP register.xlsx

05 Board and Governance/        (only when governance runs in LawDocs; when LDC is system of record, a reference file points to the LDC archive — D-10)
    {<Entity>/}<FY>/
        Board Meetings/<YYYY-MM-DD> - Board Meeting <n> of <FY>/ (Notice and Agenda, Papers, Minutes - SIGNED, Attendance, Resolutions)
        Committee Meetings/<Committee>/<YYYY-MM-DD> - …/
        General Meetings/<YYYY-MM-DD> - AGM|EGM …/
        Resolutions by Circulation/
        Filings/<Form> - <YYYY-MM-DD> - SRN <ref>.pdf
    Registers/ (Members, Directors and KMP, Charges, other statutory registers in prescribed layouts) [VERIFY formats]

06 Policies and Registers/
    Policies/<Policy name>/<v<n> - APPROVED YYYY-MM-DD>.docx + .pdf; superseded versions labelled; Approval records.pdf
    Contract Templates and Playbooks/ (X-12; P06/P07)
        Templates/<Template name> (tpl_…)/<v<n> - PUBLISHED YYYY-MM-DD>.docx + questionnaire.json + reviewer-of-record.pdf
        Clause Library/<Clause family>.xlsx (+ .docx per clause with fallback positions)
        Playbooks/<Playbook name>/<v<n> - APPROVED YYYY-MM-DD>.xlsx + .pdf (position ladders, approval triggers)
        Intake Forms/<Request type>.json + .pdf
    Custom Registers/<Register name>.xlsx (+ attachments/)
    Licences and Permits/

07 People and HR/                (only when HRMS runs in LawDocs; LDC SoR → reference file)
    Employees [R]/EMP-<number>/ (appointment letter, KMP/director records, duties) — ids only in names
    Departments and Positions.xlsx · Duties and Delegations.xlsx · Policy Acknowledgements.xlsx
    <Year>/Bulk letters - <batch>/ (bulk-signed letters with status report; P08)
    Training Certificates/<Year>/ (FinLegal Academy certificates; P16)
    Payroll [R]/<FY>/

08 Notices and Correspondence/
    Notices Sent/<Year>/<YYYY-MM-DD> - <Type> - <Recipient org or masked name> (LD-NTC-…)/ (notice, dispatch proof, reply)
    Notices Received/<Year>/…/
    Messages/<Thread title>.pdf (+ .jsonl)

09 Services and Engagements/
    <FY>/<Service title> (LD-ENG-…)/                      one-time engagements (P16)
        01 Engagement Letter and SOW/ · 02 Inputs/ · 03 Deliverables/ · 04 Correspondence/ · 05 Invoices and Receipts/ · 06 Change Requests/ · 07 Disputes/
    <FY>/Retainers/<Package> (LD-ENG-…)/                  retainers, including LawDocs-delivered retainers (P16 + P18)
        01 Agreement and SLA Schedule/ · 02 Monthly Reports/ · 03 Deliverables/ · 04 Hour Bank and SLA Statements/ · 05 Invoices/ ·
        06 Messages/ (transcripts with the LawDocs team) · 07 Meetings/ (agenda, notes, attendees)
    Business Services/<FY>/<Service> (LD-ENG-…)/ (applications, government acknowledgements, certificates)
    Tax and Filings/<FY>/ (engagement working papers only; the filed returns themselves sit in `12 Tax/` with a link file here)
    Legal Requests (internal)/<FY>/<YYYY-MM-DD> - <Request title> (<ref>)/

10 Billing and Invoices/
    <FY>/Invoices/<Invoice no>.pdf (tax invoices as issued by OH8) · Credit Notes/ · Receipts/ · Statements and Usage/ ·
         Contracts and Order Forms/ · TDS Certificates/ · Value Reports/ (savings and value reports — formula, inputs, evidence class; NN-36; P17)
    Subscriptions and Credits.xlsx

11 AI Work Products (labelled)/
    Conversations/<YYYY>/<YYYY-MM-DD> - <title> (cnv_…)/ (PDF + JSON)
    Outputs/<YYYY>/<record ref>/ (accepted and rejected outputs: <title> (AI draft - not reviewed).docx/.pdf + sources and provenance JSON)
    Agent Activity/<Agent name>/<YYYY-MM>.xlsx (+ CSV)
    Missions/<msn_…>/ (PDF summary + JSON: model, date, tools, approvals, sponsor)
    Notebooks/<name>/ (JSON + source list CSV)
    (Professional reviews of AI drafts sit with the reviewed document under `01 Drafts/Reviews/` — P09.)

12 Tax/                           (X-12; company tax folder; P14 `tax`; part of `ld_company_v1` 1.0.0)
    {<Entity>/}<FY>/
        Income Tax/ (returns and acknowledgements, tax audit report, advance tax challans, computation) · 
        GST/<GSTIN last 4 - State>/ (GSTR returns and acknowledgements, annual return, reconciliations, e-invoice and e-way bill reports) ·
        TDS and TCS/ (quarterly statements, certificates issued, challans) · Professional Tax/<State>/ ·
        Notices, Assessments and Appeals/<YYYY-MM-DD> - <Authority> - <Notice type> (ref)/ (notice, reply, order; link file to 03 when litigated)
    Tax register <FY>.xlsx (filing, due date, filed date, acknowledgement no., filed by — never portal credentials or OTPs; CH-10)

99 System Data (CSV and JSON)/   (§K.3.5)
```

The company year label is the Indian FY (`FY 2026-27`). From tax year 2026-27 the Income-tax Act 2025 uses "tax year" for the period whose income is taxed [VERIFY: Income-tax Act 2025 definition and commencement 1 Apr 2026; TAX MEMO]; `Income Tax/` sub-folders of FY 2026-27 onwards carry the label `Tax Year 2026-27`, and earlier years carry the legacy alias `AY <YYYY-YY>` in brackets (e.g., `FY 2025-26 (AY 2026-27)`) so both vocabularies sort and search.

### K.3.2 Individual profile `ld_individual_v1`

Default `xpt.folder.individual_agreements_mode = by_life_area`: an agreement is filed under the life area it belongs to (rent and sale → Property; vehicle sale → Vehicles; employment → Employment; loan → Finance); everything else under `08 Agreements`. Option `all_in_08` keeps all agreements together. `00 Index.xlsx` always lists all agreements on one sheet.

```
01 My Profile and IDs (masked)/
    My profile.pdf · ID documents/ (Aadhaar shown masked; PAN last 4 in index; originals as uploaded with masked derived text — NN-04)
    DigiLocker references.xlsx + .csv (where only URI and verification result are held — NN-42; P04)
    Nominees and Trusted Helpers.pdf

02 Property/
    <Property label>/                 e.g. "Flat 402 - Jaipur" (the user's own label)
        Ownership and Title/ · Agreements/<Counterparty> - <Title> (LD-AGR-…)/ (six sub-folders as company) ·
        Registration and Stamp/ · Tax and Utility Bills/<Year>/ · Society and Maintenance/ · Disputes/ (link file to 07)

03 Family and Succession/
    Will and Succession Papers/ (wet-ink execution packs — never eSigned, NN-07) · Nominations/ · Family Agreements/ · Guardianship/ · Certificates/ (birth, marriage, death)

04 Employment/
    <Employer>/ Offer and Appointment/ · Salary and Tax Documents/<Year>/ · Exit and Settlement/
    Training Certificates/ (FinLegal Academy certificates; P16)

05 Finance, Loans and Insurance/
    Bank and Investments/ · Loans/<Lender> - <Loan type>/ · Insurance/<Insurer> - <Policy type>/ · Credit Reports (uploaded by me)/<Year>/ · Complaints and Grievances/ (link files to 07)

06 Vehicles/
    <Vehicle label>/ Registration (RC)/ · Insurance/ · Purchase or Sale Agreement (LD-AGR-…)/ · Challans/<Year>/ · Loan/ · Service and PUC/

07 Disputes and Court Cases/
    <Year>/<Forum>/<Case title> (LD-CAS-…)/ (company sub-structure)
    Complaints and Grievances/<Year>/<YYYY-MM-DD> - <Institution> - <Topic> (LD-GRV-…)/

08 Agreements/
    <Year>/<Category>/<Counterparty> - <Title> (LD-AGR-…)/ (six sub-folders)

09 Tax/
    Tax Year <YYYY-YY>/ Returns and Acknowledgements/ · Form 16 and Statements/ · Notices/ · Proofs and Investments/
        (X-12: `Tax Year 2026-27` onwards under the Income-tax Act 2025 [VERIFY: term and commencement; TAX MEMO];
         years before 2026-27 use `Tax Year <YYYY-YY> (AY <YYYY-YY>)`, e.g. `Tax Year 2025-26 (AY 2026-27)`, the AY being the
         legacy alias under the Income-tax Act 1961; the index carries both labels in separate columns)

10 Receipts and Invoices/
    <Year>/ LawDocs invoices/ · Statements/ · Plan Terms/ · Services/<Service title> (LD-ENG-…)/ (incl. Disputes/) ·
            Professional fees/ · Stamp duty and government fees/ · Certified translations/ · Other receipts/

11 AI Work Products (labelled)/       (as company; added to the conventions summary as an additive folder)

99 System Data (CSV and JSON)/        (§K.3.5; same name in every profile — G3 K-1)
```

### K.3.3 Professional profile `ld_professional_v1`

Client-owned material in a client's own LawDocs workspace is exported by the client, not by the professional; the professional's export includes it only where the engagement grant allows copies, otherwise as reference rows (`Client material references.xlsx`).

```
01 Practice Profile and Registrations/   enrolment/membership certificates, practice details, firm members, white-label settings
02 Clients and Matters/
    <Client org name or masked name> (<client ref>)/<Matter or engagement title> (LD-MAT-… or LD-ENG-…)/
        01 Engagement and Terms/ (engagement letter, SLA - SIGNED, conflict check record)
        02 Client Documents/ (copies permitted by the client)
        03 Work Product/ (drafts, opinions, filings — versions labelled)
        04 Court Filings and Orders/
        05 Correspondence/
        06 Invoices and Payouts/
03 Calendar and Hearings/                Hearings and deadlines.xlsx + .ics
04 Templates and Precedents/             practice templates (non-client), clause notes
05 Marketplace Engagements and Retainers/<FY>/
06 Invoices and Payouts/<FY>/            invoices, payout statements (Razorpay Route settlements as received from OH8)
07 Correspondence/
11 AI Work Products (labelled)/
99 System Data (CSV and JSON)/
```

### K.3.4 Consumer Help profile `ld_consumer_help_v1`

Natural-person names never appear in paths (LOCKED `ids_only`); institutions are named.

```
01 My Profile (masked)/
02 Loan and Lending Complaints/
    <Year>/<YYYY-MM-DD> - LD-GRV-2026-000456 - <Institution> - <Product>/
        01 Complaint to the Institution/ · 02 Institution Replies/ · 03 Ombudsman or Forum/ (RB-IOS filing copy, acknowledgement, status history with source) ·
        04 Evidence/ (originals, type copies, translations — labelled) · 05 Outcome and Compliance/ · Case timeline.pdf · Open and Waiting Items.xlsx
03 Insurance Complaints/<Year>/<…LD-GRV-… - <Insurer> - <Policy type>>/ (same sub-structure; Insurance Ombudsman)
04 Credit Report Disputes/<Year>/<… - <Bureau>>/ (reports uploaded by the user; dispute letters; responses)
05 Challans/<Year>/<YYYY-MM-DD> - Challan <last 4 of challan no.> - <State>/ (challan copy, official-portal payment receipt uploaded by the user, court-date records)
06 Vehicles/<Vehicle label>/ (sale agreement, RC transfer checklist, Vahan status records)
07 Fees and Receipts/<Year>/ (Consumer Help fees as invoiced; never fines or dues — CH-22)
99 System Data (CSV and JSON)/
```

### K.3.5 `99 System Data (CSV and JSON)/` (all profiles)

```
Datasets/                 <dataset>.csv + <dataset>.xlsx + <dataset>.schema.json (+ .jsonl in FULL/EXIT)
Audit Trail/              audit-events-YYYY-MM.jsonl · Audit trail YYYY-MM.xlsx · chain-anchors.csv
Settings and Customisations/  Settings and customisations.xlsx · settings.csv · customisations.xlsx · Rules in use.xlsx ·
                          Configuration bundle (ld-config-1.0).json · Change history/ (setting changes, change requests)
Open and Waiting Items/   items.csv · tasks.csv (`wf.tasks`, R-A-08) · item-waits.csv · item-clocks.csv · item-interims.csv · chase-log.csv · Open and waiting items.xlsx
Rule Decisions/           rule-evaluations-YYYY.csv (rule set, version, inputs hash, output, object)
Users, Roles and Access/  users.csv (no passwords), roles.csv, grants.csv, sessions summary (attendance-style counts only — NN-33)
access_transparency/      delivery grants, sessions and access log (P18; NN-17)
Exports, Imports and Storage/ Export and import history.xlsx · Import reports/ · storage-targets.csv (no credentials)
Integrations/             sharing-ledger.csv · api-clients.csv · webhooks.csv · webhook-deliveries.csv · ecosystem-links.csv · connectors.csv · mapping-overrides/ · connected-apps.csv (P19)
Platform Notices/         release notes and maintenance notices received
documents.csv · relationships.csv · folders.json · reminders.csv · health_findings.csv · family_and_nominees.csv (Individual) · sharing/ · retention/   (P04)
document_intelligence/    lines, corrections, attestations, translations/, extractions.csv (P05)
signing/                  signing requests, participants, events, consents (P08)
ai_memory.json · ai_runs.csv   (P09; metadata and hashes, no provider secrets)
marketplace/              reviews.csv (own) · practitioner/ (practitioner exports) (P16)
billing/ · savings/       credit ledger, billing history; savings ledger (formula, inputs, evidence class — NN-36) (P17)
Help Notes.csv · Accessibility Preferences.csv · Accessibility Feedback.csv · Testimonials and Consents.json   (P21)
Devices.csv · Notification Preferences.csv · Capture Metadata.csv   (P22)
```

Inside `99 System Data (CSV and JSON)/`, machine-oriented groups registered by owner phases may use lower-case snake_case names (as above); human-facing folders everywhere else use Title Case. The credential-vault register is exported under `01 Company Profile/Credential Vault (metadata only)/` (P18), not here.

---

## K.4 File-format matrix per record type (binding)

| Record type (module) | Human files | Machine files | Rules |
|---|---|---|---|
| Agreement (`clm`) | Summary `.pdf`; drafts `.docx` + `.pdf`; register `.xlsx` | `agreements.csv` + schema | Versions and status in names |
| Negotiation round (`clm`, `msg`) | Redline `.docx` (tracked changes) + `.pdf`; `Negotiation log.xlsx` | `negotiation-rounds.csv`, `changes.jsonl` | Internal comments only in internal exports (NN-37) |
| Signing request and signature events (`sgn`) | `Evidence pack.pdf` | `signature-events.jsonl`, provider responses as received | Consent screen version, txn IDs, hashes, timestamps, IP/device class |
| Signed document (`dms`/`sgn`) | As stored, byte-identical | — | SHA-256 = vault hash; PAdES/PKCS#7 preserved |
| Stamp instrument (`sgn`) | Certificate as issued + `Stamp details.pdf` | `stamps.csv` | UIN verification result and document-hash link (NN-08) |
| Wet-ink / notary / registration pack (`sgn`) | Checklist `.pdf`, scans of executed originals, registration receipt | `formalities.csv` | Formality status from items (NN-40) |
| Obligation (`clm`) | `Obligations.xlsx` | `obligations.csv` | — |
| Document and version (`dms`) | Original as uploaded | `documents.csv`, `versions.csv` | Byte-identical; `is_original` flag |
| Derived rendition: OCR, type copy, translation, redaction, extract (`dix`, `dms`) | Beside the original: `(Type copy - <status>)`, `(Translation - English - Machine)`, `(Certified translation - English)`, `(OCR text).txt`, `(Redacted).pdf`, `(Extract p3-7).pdf` | `99 …/document_intelligence/` CSV + anchors JSON | Label in file name and first page; confidence summary (NN-09, NN-48; P04, P05) |
| Folder and category (`dms`) | Folder structure itself | `folders.csv` (canonical IDs, tenant labels) | Views over IDs (NN-12) |
| Template and clause versions used (`tpl`) | Listed in summaries | `content-versions.csv` | Versions pinned at drafting |
| AI draft or answer (`drf`, `ai`) | `.docx` + `.pdf` with AI label; sources `.xlsx` | `ai_runs.csv`, outputs JSON (model, date, sources) | Label in name: `(AI draft - not reviewed)` (NN-14; P09) |
| Agent mission (`agt`) | Mission report `.pdf` | `missions.jsonl` (tools, approvals, sponsor) | — |
| Pleading or notice (`pld`) | `.docx` + `.pdf`; filed copy as filed | `pleadings.csv`, `notices.csv` | Status `DRAFT`/`FILED`/`SENT` in name |
| Matter and case (`lit`) | Summary `.pdf`; register `.xlsx` | `matters.csv`, `cases.csv` | External numbers (CNR, case no.) as attributes |
| Hearing (`lit`) | Hearing note `.pdf`; calendar `.xlsx` | `hearings.csv`, `.ics` | — |
| Order (`lit`) | As obtained `.pdf` | `orders.csv` | Source and fetched-at |
| Court status snapshots (`lit`) | `Case status history.xlsx` | `case-status.csv` | Staleness shown; no "real-time" wording (NN-20) |
| Trademark / IP asset (`ipm`) | Summary `.pdf`; filings as obtained | `ip-assets.csv`, `ip-status.csv` | — |
| Meeting, minutes, resolution (`gov`) | Notice/agenda/minutes `.docx` + `.pdf`; signed minutes `.pdf` | `meetings.csv`, `resolutions.csv` | Prescribed register layouts where applicable [VERIFY] |
| Policy version (`gov`/`dms`) | `.docx` + `.pdf` | `policies.csv` | `APPROVED`/`SUPERSEDED` in name |
| Employee and KMP records (`hr`) [R] | `.pdf` | `employees.csv` | ids only in paths |
| Legal request (`lgo`) | Request summary `.pdf` | `legal-requests.csv` | — |
| Service order / engagement / retainer (`mkp`, `bsv`, `sdc`) | Terms and SLA `.pdf` (signed); deliverables as delivered | `engagements.csv`, `deliverables.csv` | — |
| Tax filing (`tax`) | Prepared files and acknowledgements as generated | `tax-filings.csv` | Byte-identical to filed files |
| Consumer case (`chp`) | Timeline `.pdf`; filings as filed | `consumer-cases.csv`, `case-events.csv` | ids-only paths |
| Challan and vehicle records (`chp`) | As uploaded | `challans.csv`, `vehicles.csv` | Payments only as user-uploaded official receipts |
| Messages and threads (`msg`) | `Conversation - <thread>.pdf` | `messages.jsonl` | Attachments beside the transcript |
| Open/interim/waiting items (`wf`) | `Open and Waiting Items.xlsx` per record + global | `items.csv` and related | Canonical state + tenant label columns |
| Settings and customisations (`cfg`, `rul`) | `.xlsx` | `ld-config-1.0.json` (signed), `.csv` | No secrets |
| Audit trail (`core`) | `Audit trail YYYY-MM.xlsx` | `audit-events-YYYY-MM.jsonl`, anchors | Corrections shown with originals (NN-02) |
| Invoices and payments mirrors (`bil`) | Tax invoices `.pdf` as issued by OH8 | `invoices.csv`, `payments.csv` | Never card data |
| Savings ledger (`sav`) | Savings report `.pdf` + `.xlsx` | `savings-ledger.csv` | Formula, inputs, evidence class (NN-36) |
| Credential vault entries (`cvl`) | — | `portals.csv` (metadata only) | No secrets ever |
| Calendars (all) | `.xlsx` | `.ics` | — |
| Dashboards (`rpt`) | `.pdf` snapshot + `.xlsx` numbers | `.csv` | As of export time |

**Typing rules (all CSV/XLSX):** UTF-8 with BOM; RFC 4180; dates ISO 8601 with offset (`2026-10-31T18:30:00+05:30`); dates without time as `YYYY-MM-DD`; amounts as fixed 2-decimal strings with a `currency` column; no thousands separators in CSV (XLSX cells typed as currency with Indian grouping display); code + label columns for every coded field; booleans `Y`/`N` in human files, `true`/`false` in machine files; leading zeros preserved (text-typed cells); XLSX "Read me" first sheet, frozen header row, filters, column notes from the dictionary, split at 1,000,000 rows.

**PDF rules:** PDF/A-2b for generated narratives (veraPDF-validated); PDF/A-3b where an embedded source file is required; XMP carries `document_id`, `version`, `status`, `source_sha256`; bookmarks for multi-section documents; tagged PDF for accessibility (headings, reading order, alt text for logos and charts) [REC].

---

## K.5 Naming rules (binding)

1. **Plain English, self-explanatory.** Folder names say what is inside ("Signed and Stamped", not "Exec"). Title Case for folders; sentence case allowed for files.
2. **Forbidden characters** (Windows, macOS Finder, OneDrive/SharePoint, Google Drive sync): `\ / : * ? " < > |`; control characters; leading or trailing spaces or dots; replace `/` and `\` in titles with `-`, `:` with ` -`, quotes with nothing, `&` kept, `#` and `%` replaced with `No.` and `pct` [REC: avoids SharePoint and URL issues — VERIFY current SharePoint restrictions].
3. **Reserved names:** `CON`, `PRN`, `AUX`, `NUL`, `COM1`–`COM9`, `LPT1`–`LPT9` (with any extension), `desktop.ini`, `.lock`, names starting `~$`, names containing `_vti_`; such titles get a ` (file)` suffix.
4. **Unicode NFC**; no emoji; non-Latin titles transliterated to Latin for paths by default (`xpt.folder.path_script = latin`), with the original-script title kept in `00 Index.xlsx` and the summary PDF.
5. **Lengths:** full path ≤ 240 characters from the root folder (Spec §12.1); each folder segment ≤ 80 characters and each file name ≤ 120 characters [REC]; shorten titles from the right at a word boundary and append ` - <short id>` (last 6 characters of the ULID).
6. **Dates first** for dated items: `2026-08-14 - Order - Interim stay granted.pdf`; ISO dates sort chronologically in every tool.
7. **Versions and status:** `v3 - SIGNED`, `v2 - DRAFT`, `v4 - APPROVED 2026-05-12`, `v1 - SUPERSEDED 2026-05-12`, `IMPORTED`. **Derived and AI labels** are parenthesised suffixes after the source name (P04/P05/P09 registrations): `(Type copy - <status>)`, `(Translation - English - Machine)`, `(Certified translation - English)`, `(OCR text)`, `(Redacted)`, `(Extract p3-7)`, `(AI draft - not reviewed)`. Phase name templates written with en dashes are rendered with ASCII ` - ` (rule 11).
8. **Business references** in parentheses at the end of record folders: `(LD-AGR-2026-000123)`.
9. **People:** in `owner_readable` archives (delivered to the data owner), organisations by name and natural persons by `xpt.naming.person_mode`: `full_name` ("Ramesh Kumar"), `masked_name` ("Ramesh K."), `ids_only` ("Party prs_…J4K2"). Archives for third parties use `ids_only` or `id_and_masked_name` (Spec §12.1). Never Aadhaar, PAN, phone, email, bank account or card numbers in any path (scanner enforced); challan, policy and loan numbers only as last 4 characters.
10. **Collisions:** names compared case-insensitively after NFC (Windows and macOS are case-insensitive by default); duplicates get ` (2)`, ` (3)` deterministically by record creation time; the suffix is stable across exports (stored per record and profile version).
11. **Spaces and dashes:** single spaces; ASCII hyphen-minus with spaces as the separator ` - `; en and em dashes in titles converted to ` - `.
12. **Numbered top-level folders** and `00 Start Here` are LOCKED; levels below follow folder policy (§K.8).

Examples:

| Input title | Path segment produced |
|---|---|
| `Lease: Shop No. 4/12 "Ground Floor" — Jaipur` | `Lease - Shop No. 4-12 Ground Floor - Jaipur` |
| `NDA – ABC Pvt. Ltd. & XYZ LLP (Mutual)` | `NDA - ABC Pvt. Ltd. & XYZ LLP (Mutual)` |
| `किराया अनुबंध` (Hindi title) | `Kiraya Anubandh` (original title in index) |
| `CON` | `CON (file)` |
| 300-character counterparty name | first ~70 characters at a word boundary + ` - 7Q4K2M` |

---

## K.6 Manifest, index and dataset schemas

### K.6.1 `export-manifest.csv`

Spec §12.1 columns, in order: `path, sha256, bytes, media_type, record_count, legal_entity, dataset, schema_version, as_of, created_at, source_ids, restricted, retention_class, legal_hold, upsi`; then LawDocs columns: `record_type, record_id, business_ref, canonical_path, department_id, year_label, module, version_label, status_canonical, is_original, derived_from, ai_generated, archive_part`.

- `path` is relative to the root; `canonical_path` is the path under the profile's default folder policy (unchanged by tenant renames and splits).
- `source_ids` lists the canonical IDs that produced the file (`;`-separated).
- `derived_from` holds the original `doc_`/`ver_` for renditions.

### K.6.2 `manifest.json` (excerpt)

```json
{
  "archive_id": "exp_01JCB7Q2W8K5M3N6P9R1S4T7V0",
  "archive_standard_version": "1.0",
  "product": "lawdocs",
  "folder_profile": "ld_company_v1",
  "folder_profile_version": "1.0.0",
  "folder_policy_version": 3,
  "producer": {"release": "2026.11.2", "environment": "production", "region": "ap-south-1"},
  "tenant": {"tenant_id": "ten_01J…", "legal_entities": ["ent_01J…"]},
  "scope": {"code": "FULL_TENANT", "filters": {}, "restricted_included": ["HR"]},
  "requested_by": {"user_ref": "usr_01J…", "role": "ORG_ADMIN"},
  "approvals": [{"user_ref": "usr_01J…", "role": "ORG_CLO", "at": "2026-10-31T17:02:11+05:30"}],
  "as_of": "2026-10-31T18:00:00+05:30",
  "control_totals": [{
    "legal_entity": "ent_01J…",
    "counts": {"agreement": 1240, "negotiation_round": 3810, "signing_request": 1192, "signature_event": 4470,
               "stamp_instrument": 860, "document": 18320, "version": 30115, "rendition": 2210, "case": 64,
               "hearing": 512, "order": 301, "ip_asset": 18, "item": 9120, "audit_event": 1840033},
    "documents": {"count": 30115, "bytes": 182334455667},
    "audit_chain": {"last_anchor_date": "2026-10-31", "last_anchor_hash": "…"}
  }],
  "predecessor_archive_id": null,
  "pack_sha256": "…",
  "signing_key_id": "ten_01J…-export-2026",
  "naming": {"person_mode": "masked_name", "path_script": "latin", "year_label": "FY_LONG"}
}
```

### K.6.3 `00 Index.xlsx`

| Sheet | Columns |
|---|---|
| `Start here` | What each sheet is; how links work; as-of time |
| `All records` | Record type, business ref, title, counterparty/party, year label, department, status (tenant label + canonical), key dates, folder link (relative hyperlink), summary link |
| `Agreements` | Ref, title, counterparty, type, value, currency, start, end, renewal date, status, signed (Y/N), stamped (Y/N + State), formalities pending, folder link |
| `Cases and hearings` | Ref, case title, forum, case number, CNR, next hearing, last order date, status, source and fetched-at, folder link |
| `Trademarks and IP` | Ref, mark, class, application number, status, next deadline, folder link |
| `Documents` | Document ID, file name, path link, type, original/derived, version, SHA-256, size, uploaded/created at |
| `Signatures and stamps` | Agreement ref, signer (per naming mode), method (Aadhaar eSign / DSC / e-acceptance), time, provider txn ID, stamp UIN (last 6), State, duty |
| `Open and waiting items` | Item, parent ref, canonical state, waiting party type, expected by, legal clock due, owner |
| `Folder guide` | Mirror of `Folder guide.xlsx` |

Hyperlinks are relative so they work after the archive is moved or synced; a test opens a sample in LibreOffice headless to confirm links resolve.

### K.6.4 Incremental files

`state-index.csv` (`record_id, record_type, latest_archive_id, latest_path, deleted`) and `deleted-records.csv` (`record_id, record_type, deleted_at, basis` — no content) in every incremental package; `predecessor_archive_id` links the chain.

### K.6.5 `CHANGES-SINCE-PREVIOUS.csv`

`change_kind (ADDED_RECORD|CHANGED_RECORD|REMOVED_RECORD|NEW_FOLDER|NEW_FILE_TYPE|NEW_COLUMN), record_type, record_id, path, previous_path, note`.

### K.6.6 Data dictionary

Sheets `Datasets` (dataset, description, file, record type, key, retention class), `Fields` (dataset, field, label, description, type, length, mandatory, example, code table, data class, JSON Pointer to the canonical model), `Code tables`, `Changes` (field-level changes since profile 1.0.0).

### K.6.7 `relationships.csv`

`from_dataset, from_field, to_dataset, to_field, cardinality, description`, e.g. `versions.document_id → documents.document_id (many-to-one)`; `signature_events.signing_request_id → signing_requests.id`; `stamps.agreement_id → agreements.id`; `hearings.case_id → cases.id`; `items.parent_id → *.id (polymorphic by parent_type)`; `audit_events.record_id → *.id (polymorphic by record_type)`.

---

## K.7 README template text (binding sections; English master)

> **What this is.** This folder is a complete copy of `<Owner name>`'s records from LawDocs (lawdocs.in), taken on `<as-of date and time IST>`. It was requested by `<role>` and approved by `<role>`. You do not need LawDocs to use it: every file opens with Microsoft Office, LibreOffice, Google Docs or a PDF reader.
>
> **Start here.** Open `00 Index.xlsx`. Every agreement, case, document and signature is listed with a link to its folder. Or browse the numbered folders: `02 Agreements and Contracts` holds every agreement by year and department; each agreement folder has six sub-folders, from drafts to signed and stamped copies, evidence and correspondence.
>
> **Finding common things.**
> - *A signed agreement and its proof:* `02 Agreements and Contracts/<year>/<department>/<counterparty> - <title> (<ref>)/03 Signed and Stamped/` and `04 Evidence and Certificates/Evidence pack.pdf`.
> - *A court order:* `03 Litigation and Disputes/<year>/<court>/<case>/02 Orders and Judgments/`.
> - *Who changed something and why:* `99 System Data (CSV and JSON)/Audit Trail/Audit trail <YYYY-MM>.xlsx`.
> - *What is still pending:* `Open and Waiting Items.xlsx` in each record folder, or the "Open and waiting items" sheet in `00 Index.xlsx`.
>
> **Labels you will see.** Files ending "(Type copy - …)" or "(Translation - English - Machine)" were prepared from an original that sits next to them — always rely on the original. "(AI draft - not reviewed)" means a draft produced with AI assistance that no professional has reviewed. "IMPORTED" means the file came from your own folders and was not signed or created in LawDocs.
>
> **Opening CSV files without losing zeros.** In Excel use *Data → From Text/CSV* and set ID and number columns to *Text*; in LibreOffice choose *Format quoted field as text*. The `.xlsx` twins are already formatted.
>
> **Checking nothing was changed.** On Windows PowerShell: `Get-FileHash -Algorithm SHA256 <file>`; on Windows Command Prompt: `CertUtil -hashfile <file> SHA256`; on macOS or Linux: `shasum -a 256 <file>` or, from the archive root, `sha256sum -c checksums.sha256`. To check everything including the digital signature, run `00 Start Here/verify/ld-verify`. The signing key fingerprint is `<fingerprint>`.
>
> **Joining tables.** Every record has a permanent ID (for example `agr_…`) and, where shown, a reference such as `LD-AGR-2026-000123`. `00 Start Here/relationships.csv` shows how files link.
>
> **Restricted parts.** `<list or "none">`. These are separate encrypted archives; passwords were given directly to `<recipient roles>` and are not stored by LawDocs.
>
> **Keeping and deleting.** Some records must be kept for a minimum period (for example signed-agreement evidence for at least 7 years after closure; tax records as the tax laws require). Records under legal hold are marked in `export-manifest.csv`.
>
> **Using this in court.** `00 Start Here/BSA Section 63 Certificate (draft)` is a pre-filled draft of the certificate under section 63(4) of the Bharatiya Sakshya Adhiniyam 2023, with hash values. Have it completed and signed as the law requires; ask your advocate.
>
> **Glossary.** Agreement · Counterparty · Redline · eSign (Aadhaar eSign through a licensed provider) · Electronic acceptance (click-to-accept; not an eSign) · DSC · eStamp certificate · Formalities (stamp, witness, notarisation, registration, approvals) · Evidence pack · Original vs derived copy · Open, interim and waiting items · Legal clock · Maker and checker · Correction entry · Canonical ID.
>
> **Contacts.** Your designated officer: `<name/role>`. LawDocs archive help: `<support contact>` (questions about the archive only).

A CI test asserts that every folder named in the README exists in the profile and every top-level folder is described.

---

## K.8 Folder policy — customisation bounds (P20 FR-P20-16)

| Element | Customisable? | Options and rule | Key |
|---|---|---|---|
| Top-level numbers and names | No | LOCKED for familiarity and tooling | — |
| `00 Start Here`, `00 READ ME FIRST.pdf`, `00 Index.xlsx` | No | Spec §12.1 + beginner files | — |
| Entity level | Yes | `auto` (omit for single entity) / `always` / `never` | `xpt.folder.entity_level` |
| Year label | Yes | `FY 2026-27` / `FY26-27` / `2026`; must sort chronologically | `xpt.folder.year_label` |
| Department level for agreements | Yes | on/off | `xpt.folder.department_level` |
| Department and committee names | From terminology (P03); `historical` or `current` | IDs in manifest | `xpt.folder.name_mode` |
| Split below level 2 | Yes | e.g., by branch, contract type, State; `canonical_path` unchanged | folder policy JSON |
| Individual agreements placement | Yes | `by_life_area` / `all_in_08` | `xpt.folder.individual_agreements_mode` |
| Person naming | DPO/owner-approved (GOVERNED) | `full_name` / `masked_name` / `ids_only`; Consumer Help LOCKED `ids_only` | `xpt.naming.person_mode` |
| Path script | Yes | `latin` / `original` | `xpt.folder.path_script` |
| README language | Yes | English + one D-07 language (labelled machine translation) | `xpt.readme.languages` |
| Custom sub-folders inside Documents and Custom Registers | Yes | Mirrors tenant DMS views | — |

Each folder-policy version is a ledger event; each archive records `folder_policy_version`.

---

## K.9 Incremental, scheduled and mirror packages

- **Scheduled full:** complete package; `predecessor_archive_id` = previous full of the same schedule.
- **Incremental:** changed and new records and new document versions since the predecessor; contains `state-index.csv`, `deleted-records.csv` and a delta `export-manifest.csv`; `ld-load` assembles the latest state from a full + chain.
- **Mirror (continuous):** increments applied to a BYO target under `LawDocs Archive/<root name without date>/`; the target tree equals the latest full layout; a monthly full anchors the chain; nightly reconciliation compares target listing with `state-index.csv`. Customer-modified files are never overwritten (P20 FR-P20-33).
- **Watch-folder intake** on the same target uses `LawDocs Inbox/` — never the mirror tree.

---

## K.10 Import mapping rules (reverse mapping; P20 FR-P20-26)

### K.10.1 Recognition order

1. **LD package:** `00 Start Here/manifest.json` + valid JWS → exact placement by `canonical_path`, `record_type`, `record_id`; IDs from another workspace kept as `external_ref`.
2. **Ecosystem archive** (archive standard 1.0 from LDC, Equator, Finbyx, Udofin): recognised by `archive_standard_version`; datasets mapped by layout registry; documents imported with producer references.
3. **Other trees:** path-segment and file-name rules (§K.10.2–§K.10.3), then content classification (`dix`), then the correction queue.

### K.10.2 Folder-name synonyms → destination

| Folder words (case-insensitive, any language transliteration) | Proposed destination |
|---|---|
| Agreements, Contracts, Deeds, MoU, NDA, Leases, Rent, Vendor contracts, Customer contracts, Signed | `02 Agreements and Contracts` (Company) / `08 Agreements` or life area (Individual) |
| Drafts, Draft, Working | `01 Drafts` within the matched agreement |
| Executed, Signed copies, Final signed, Stamped, E-stamp, Stamp paper | `03 Signed and Stamped` |
| Redlines, Comments, Negotiation, Mark-up | `02 Negotiation and Redlines` |
| Amendments, Addendum, Renewal, Extension | `05 Amendments and Renewals` |
| Litigation, Cases, Court, Suits, Petitions, Orders, Hearings, Vakalatnama, Cause list | `03 Litigation and Disputes` / `07 Disputes and Court Cases` |
| Notices, Legal notice, Reply, Show cause | `08 Notices and Correspondence` |
| Trademark, TM, Brand, IP, Copyright, Patent | `04 Trademarks and IP` |
| Board, BM, Minutes, AGM, EGM, Resolutions, ROC, MCA, Forms | `05 Board and Governance` |
| Policies, Policy manual, Registers | `06 Policies and Registers` |
| HR, Employees, Appointment letters, Payroll | `07 People and HR` (restricted) |
| Invoices, Bills, Receipts | `10 Billing and Invoices` / `10 Receipts and Invoices` |
| Property, Flat, House, Plot, Sale deed, Registry, Society | `02 Property` (Individual) |
| Will, Succession, Nomination, Family settlement | `03 Family and Succession` (Individual) |
| Car, Bike, Vehicle, RC, Challan, PUC | `06 Vehicles` |
| Loan, EMI, Insurance, Policy (insurance), Claim, CIBIL, Credit report | `05 Finance, Loans and Insurance` / Consumer Help folders |
| ITR, Income tax, Form 16, GST, TDS, AY, Assessment year, Tax year | `12 Tax` (Company) / `09 Tax` (Individual); AY folder names map to `Tax Year <YYYY-YY> (AY …)` |
| Templates, Precedents, Clause bank, Playbook, Standard forms | `06 Policies and Registers/Contract Templates and Playbooks` (Company) / `04 Templates and Precedents` (Professional) |

### K.10.3 Patterns in path segments and file names

| Pattern | Example | Use |
|---|---|---|
| Financial year | `FY 2025-26`, `FY25-26`, `2025-26`, `F.Y. 2025-2026` | Year label (Company) |
| Calendar year | `2025`, `CY2025` | Year label (Individual) |
| Date | `2026-08-14`, `14.08.2026`, `14-08-2026`, `14 Aug 2026`, `20260814` | Record or version date (DD-MM-YYYY assumed for ambiguous Indian formats; flagged when ambiguous) |
| Version and status | `v2`, `ver 3`, `final`, `final final`, `signed`, `executed`, `draft`, `clean`, `redline` | Version and status proposal (lowest confidence for "final") |
| Business reference | `LD-AGR-2026-000123` | Exact record match |
| CNR / case numbers | 16-character CNR [VERIFY format]; `CS(OS) 123/2024`, `W.P.(C) 4567/2025`, `CC/12/2026` | Case match or new case proposal |
| TM application number | 7-digit application number [VERIFY format] | IP asset match |
| CIN / LLPIN / GSTIN | 21-character CIN; `AAA-0000` LLPIN; 15-character GSTIN | Entity or counterparty match (never used in output paths) |
| Stamp certificate | `IN-DL…` style certificate numbers [VERIFY per State] | Stamp instrument proposal |
| PAN / Aadhaar / phone / email | — | Never used for placement; detection triggers masking and a privacy warning |

### K.10.4 Confidence and decisions

Confidence = weighted combination of structure match (0.4), file-name patterns (0.2), content classification (0.3) and existing-record match (0.1) [REC weights; tune on the golden import set]. ≥ `xpt.import.confidence_auto` (0.85) → auto-proposed; between `confidence_confirm` (0.50) and 0.85 → needs confirmation; below → correction queue. Duplicates by SHA-256 → link; same name, different hash → version candidate. Nothing is committed until the user commits (G-HUMAN; Appendix A §A.21; NN-12); nothing is overwritten (`xpt.import.never_overwrite`, LOCKED).

---

## K.11 Export-map registry format (`xpt.export_map`)

Each module ships `export-map/<record_type>.yaml`, validated by JSON Schema in CI and loaded into `xpt.export_map` per profile version.

```yaml
record_type: agreement
module: clm
profiles: [ld_company_v1, ld_individual_v1, ld_professional_v1]
profile_version: 1.0.0
canonical_path:
  ld_company_v1: "02 Agreements and Contracts/{entity?}/{year_label}/{department?}/{counterparty_label} - {title} ({business_ref})/"
  ld_individual_v1: "{life_area_path|08 Agreements/{year_label}/{category}}/{counterparty_label} - {title} ({business_ref})/"
stability_key: [record_id, business_ref, record_date]      # immutable fields that fix the path
display_parts:                                             # resolved as at record_date unless name_mode=current
  department: org.departments.name@record_date
  counterparty_label: party.display_name|person_mode
  title: clm.agreements.title|naming_rules
year_basis: clm.agreements.effective_date                  # falls back to created_at
artefacts:
  - kind: summary
    file: "Agreement summary.pdf"
  - kind: draft_version
    folder: "01 Drafts"
    file: "{version_date} - v{version_no} - DRAFT.{ext}"
    formats: [docx, pdf]
  - kind: signed_document
    folder: "03 Signed and Stamped"
    file: "{title} - v{version_no} - SIGNED.pdf"
    byte_identical: true
  - kind: items
    file: "Open and Waiting Items.xlsx"
dataset:
  name: agreements
  columns:
    - {name: agreement_id, pointer: /id, type: string, data_class: INTERNAL}
    - {name: business_ref, pointer: /business_ref, type: string}
    - {name: title, pointer: /title, type: string}
    - {name: status_code, pointer: /status/tenant_code, type: string, code_table: agreement_status}
    - {name: status_canonical, pointer: /status/canonical, type: string, code_table: agreement_canonical_state}
    - {name: value_amount, pointer: /value/amount, type: decimal_string}
    - {name: value_currency, pointer: /value/currency, type: string}
restricted_class: null
retention_class: CONTRACT_STD
include_when: "record.deleted_at == null || scope.code in ['EXIT','FULL_TENANT']"
notes: "Counterparty-only comments excluded from internal exports of the counterparty's workspace"
```

**Seed registry (record type → canonical path; Company profile unless stated).**

| Record type | Module | Canonical path (summary) |
|---|---|---|
| `organisation_profile` | `org` | `01 Company Profile/` |
| `legal_entity` | `org` | `01 Company Profile/{entity}/` |
| `department`, `position` | `org` | `01 Company Profile/Departments and Teams.xlsx` + datasets |
| `agreement` | `clm` | `02 Agreements and Contracts/{entity?}/{FY}/{dept?}/{cp} - {title} ({ref})/` |
| `negotiation_round` | `clm` | `…/02 Negotiation and Redlines/` |
| `obligation` | `clm` | `…/Obligations.xlsx` |
| `signing_request`, `signature_event` | `sgn` | `…/04 Evidence and Certificates/` |
| `stamp_instrument` | `sgn` | `…/03 Signed and Stamped/` |
| `evidence_pack` | `sgn` | `…/04 Evidence and Certificates/Evidence pack.pdf` |
| `document`, `version` | `dms` | Parent record folder; unattached documents → `06 Policies and Registers/Documents/{folder view}/` (Company) or the mapped life-area folder (Individual) |
| `rendition` | `dix` | Beside the original |
| `template_use` | `tpl` | Dataset only |
| `draft` (AI), `ai_output` | `drf`, `ai` | `11 AI Work Products (labelled)/Outputs/{YYYY}/{record ref}/` (and linked from the agreement) |
| `ai_conversation`, `ai_notebook` | `ai` | `11 AI Work Products (labelled)/Conversations/{YYYY}/…` · `Notebooks/{name}/` |
| `agent_mission`, `agt_activity_log` | `agt` | `11 AI Work Products (labelled)/Missions/{msn_id}/` · `Agent Activity/{agent}/{YYYY-MM}.xlsx` |
| `pleading` | `pld` | `03 Litigation and Disputes/…/01 Pleadings and Filings/` |
| `notice` | `pld` | `08 Notices and Correspondence/Notices Sent|Received/{Year}/…` |
| `matter` | `lit` | `03 Litigation and Disputes/{Year}/Other Matters/{title} ({ref})/` |
| `court_case`, `hearing`, `order` | `lit` | `03 Litigation and Disputes/{Year}/{Forum}/{case} ({ref})/…` |
| `ip_asset` | `ipm` | `04 Trademarks and IP/{mark} ({ref})/` |
| `meeting`, `resolution`, `register` | `gov` | `05 Board and Governance/{entity?}/{FY}/…` |
| `policy_version` | `gov`/`dms` | `06 Policies and Registers/Policies/{policy}/` |
| `custom_register_record` | `cfg` | `06 Policies and Registers/Custom Registers/{register}.xlsx` |
| `employee`, `kmp_record` | `hr` | `07 People and HR/Employees [R]/EMP-{no}/` |
| `message`, `thread` | `msg` | Parent record `06 Correspondence/` or `08 Notices and Correspondence/Messages/` |
| `legal_request` | `lgo` | `09 Services and Engagements/Legal Requests (internal)/{FY}/` |
| `engagement`, `retainer`, `deliverable`, `sdc_meeting` | `mkp`/`sdc` | `09 Services and Engagements/{FY}/{title} ({ref})/…` · `{FY}/Retainers/{package} ({ref})/…` |
| `service_order` | `bsv` | `09 Services and Engagements/Business Services/{FY}/` |
| `tax_filing`, `tax_notice` | `tax` | `12 Tax/{entity?}/{FY}/{Income Tax|GST/{gstin}|TDS and TCS|Professional Tax/{state}|Notices, Assessments and Appeals}/` (Company) · `09 Tax/Tax Year {YYYY-YY}{ (AY …) for pre-2026-27}/` (Individual) |
| `tenant_template`, `clause`, `playbook`, `intake_form` | `tpl`/`clm` | `06 Policies and Registers/Contract Templates and Playbooks/{Templates|Clause Library|Playbooks|Intake Forms}/` (Company) · `04 Templates and Precedents/` (Professional) |
| `consumer_case` | `chp` | `ld_consumer_help_v1` folders 02–04 by vertical |
| `challan_record`, `vehicle_record` | `chp` | `05 Challans/…`, `06 Vehicles/…` (Consumer Help) · `06 Vehicles/…` (Individual) |
| `invoice_mirror`, `credit_note`, `receipt`, `statement`, `tds_certificate` | `bil` | `10 Billing and Invoices/{FY}/{Invoices|Credit Notes|Receipts|Statements and Usage|TDS Certificates}/` |
| `savings_entry`, `value_report` | `sav` | `10 Billing and Invoices/{FY}/Value Reports/` + `99 …/savings/` |
| `item`, `item_wait`, `item_clock`, `chase`, `task` | `wf` | Parent record `Open and Waiting Items.xlsx` + `99 …/Open and Waiting Items/` (`tasks.csv` for `wf.tasks`) |
| `share` | `dms` | Parent record `Sharing log.xlsx` + `99 …/sharing/` |
| `legal_hold` | `dms` | `99 …/retention/legal-holds.csv` (+ hold notice PDF in the held record's folder) |
| `nominee` | `kyc`/`dms` | `01 My Profile and IDs (masked)/Nominees and Trusted Helpers.pdf` + `99 …/family_and_nominees.csv` (Individual) |
| `signatory_authority` | `kyc` | `01 Company Profile/{entity}/Authorised Signatories and Delegations/` |
| `guardianship` | `kyc` | `03 Family and Succession/Guardianship/` (Individual) |
| `signing_assistance` | `sgn` | `…/04 Evidence and Certificates/Signing assistance.pdf` (assistance mode, masked helper and witness, declarations; no health data — P08 FR-P08-57) |
| `ai_qrg_review` | `ai`/`drf` | Beside the reviewed document `01 Drafts/Reviews/` + `11 AI Work Products (labelled)/Outputs/{YYYY}/{record ref}/` |
| `ai_memory_item` · `ai_run_ledger_extract` | `ai` | `99 …/ai_memory.json` · `99 …/ai_runs.csv` |
| `hr_posh_case` | `hr_posh` | Never in an owner, admin or auditor export: `07 People and HR/POSH Internal Committee [R]/` is produced only on request of `ORG_POSH_IC_PRESIDING` as a separately encrypted archive (POSH Act 2013 s.16); owner exports carry the IC constitution and annual reports only |
| `review` | `mkp` | `99 …/marketplace/reviews.csv` (own reviews) |
| `aca_certificate` | `aca` | `07 People and HR/Training Certificates/{Year}/` (Company) · `04 Employment/Training Certificates/` (Individual) |
| `testimonial` | `web` | `99 …/Testimonials and Consents.json` |
| `a11y_issue` | `hlp` | `99 …/Accessibility Feedback.csv` |
| `mob_device` · `mob_push_preferences` | `mob` | `99 …/Devices.csv` · `99 …/Notification Preferences.csv` |
| `setting_value`, `customisation`, `change_request` | `cfg` | `99 …/Settings and Customisations/` |
| `rule_evaluation` | `rul` | Parent `04 Evidence and Certificates/Rule decisions.xlsx` + `99 …/Rule Decisions/` |
| `user`, `role_grant` · `delivery_grant`, `access_log` | `iam` · `sdc` | `99 …/Users, Roles and Access/` · `99 …/access_transparency/` |
| `credential_entry` | `cvl` | `01 Company Profile/Credential Vault (metadata only)/` (metadata only) |
| `consent_artefact`, `verification` | `kyc` | `01 Company Profile/Registrations and Licences/` (KYB results) · `01 My Profile and IDs (masked)/` (Individual) + dataset |
| `export_job`, `import_job`, `storage_target` | `xpt` | `99 …/Exports, Imports and Storage/` |
| `connector`, `ecosystem_share` | `int` | `99 …/Integrations/` |
| `audit_event` | `core` | `99 …/Audit Trail/` |
| `platform_notice` | `eng` | `99 …/Platform Notices/` |

---

## K.12 Verification tests (CI and quarterly manual)

1. A full synthetic archive per profile verifies; one changed byte fails; one missing file fails; a renamed file fails (not in manifest).
2. README names every folder; every top-level folder is described; `Folder guide.xlsx` covers every folder present.
3. All Office files render headless; all generated PDFs pass PDF/A-2b; tagged-PDF check on a sample.
4. CSVs schema-validate against `schemas/`; XLSX keeps leading zeros; relative hyperlinks in `00 Index.xlsx` resolve after the archive is moved.
5. Path scanner: no forbidden characters, reserved names, path > 240, Aadhaar, PAN, phone, email or full challan/loan numbers; person names follow the naming mode.
6. Content scan: no unmasked Aadhaar anywhere; no credentials; no card data.
7. Restricted archives open only with the delivered password; their manifests verify.
8. Control totals equal live counts at `as_of`.
9. Golden-archive path stability across releases (P20 FR-P20-40).
10. Round trip: importing an LD package into a new workspace places 100% by `canonical_path` with equal counts.
11. Sync safety: the archive copied to OneDrive, SharePoint, Google Drive, a Windows NTFS disk, a macOS APFS disk and an SMB share has no rename, rejection or collision (manual quarterly; automated where test tenants exist).

---

## K.13 Open items

| ID | Item | Owner | Fallback |
|---|---|---|---|
| OI-K-01 | **Closed (X-07, X-08):** Appendix Y §Y.11.1 now registers all four profiles and §Y.11.2 the `owner_readable` naming mode; acceptance by other archive producers tracked as OI-Y-07 | — | `ids_only` for cross-product archives |
| OI-K-02 | BSA 2023 s.63 Schedule wording and signatories for Part B | [COUNSEL] | Draft labelled for advocate review |
| OI-K-03 | Current SharePoint/OneDrive and Google Drive naming restrictions and path limits | P19 lead | Rules in §K.5 (stricter set) |
| OI-K-04 | CNR, TM application and State eStamp certificate number formats for import patterns | P11, P12, P08 | Patterns disabled; content classification only |
| OI-K-05 | Prescribed layouts of statutory registers in `05 Board and Governance` | P13 content | Plain register XLSX |
| OI-K-06 | Tax-year label under the Income-tax Act 2025 for `09 Tax/` and `12 Tax/` (X-12 adopted `Tax Year <YYYY-YY>` with legacy `AY` alias); confirm the statutory term and the mapping for transition years | [TAX MEMO] | `Tax Year YYYY-YY (AY …)` |
