# Phase P19 — Data Preservation, Portability and Bring-Your-Own Storage

> Paste after `01_MASTER_PROMPT.md` and `02_REQUIREMENTS_MAP_AND_DECISION_LOG.md`.
>
> **Dependencies:** P00 (stable identifiers, audit ledger with daily anchors, object storage with Object Lock, migration framework), P01 (roles, step-up), P02 (settings, folder policy, terminology registry — department and function names), P07 (DMS: documents, versions, renditions, evidence vault), P18 (connector framework, `StorageTarget` base, on-premises agent, Microsoft Graph and Google adapters). Every module that stores records (P03–P16, P17, P20–P22) must register its record types in the **export map** (§4E) before its exit gate — this is a cross-phase obligation enforced by CI (NN-10).
>
> **Sequencing:** The export map registry, the export-mapping contract test and the storage key scheme ship in sprint 1 so that every module built after P00 is portable by construction. Full/partial exports and the verifier ship in sprints 2–4; BYO storage targets and scheduled backups in sprints 4–6; folder-tree intake in sprints 5–7; exit plan, rehydration tool and infrastructure-move runbooks in sprints 7–8.
>
> **Binding appendices:** M (export package `LDC-EXPORT-1.0` and folder taxonomy — binding for every path and file name), L (`StorageTarget` adapters), Q (security), U (settings), B (data model conventions). The **Infrabyx Ecosystem Integration Specification v1.1 §12.1 archive standard 1.0** and **§12.2 storage connector contract** prevail on any conflict (NN-23); `LDC-EXPORT-1.0` is LDC's registered **folder profile** `ldc_tenant_v1` within that standard.
>
> **Requirements covered:** R-021, R-043 (folder export, Office formats), R-076, R-081, R-082 (storage parts), R-046 (backups, restore tests — engineering parts in P24), R-047 (cross-product sharing of packages), R-055 (audit-readable exports), R-051 (exports follow accounting/audit/corporate practice — format rules), R-088 (audit trail export).
>
> **Estimated effort:** 8 two-week sprints, squad of 7 (portability core 3, storage connectors 2, intake 1, verification and tooling 1). *(v1.1: +2 sprints for v1.1 scope (new folders, multi-cell exports, migration, escrow, undo) — 10 in total)*


**v1.1 changes (25 October 2026)** *(v1.1)*

- New §4K exports for the v1.1 modules — folders 25–29 (global entities, legal matters/contracts/licences, ESG/BRSR, reports/MIS/board packs, AI governance); profile `ldc_tenant_v1` 1.1.0 (FR-P19-42–FR-P19-45).
- New §4L multi-region exports and group index, and §4M home-cell migration between cells with a verified manifest (NN-24 as amended; Appendix Y §Y.7; Appendix M §M.19–§M.20) (FR-P19-46–FR-P19-51).
- New §4N published exit runbook with optional data and source-code escrow for regulated customers (G5 gap TM-404; Appendix M §M.21) (FR-P19-52–FR-P19-53).
- New §4O reversible intake: every folder intake and bulk import has a 24-hour undo window (NN-49) and recognises the new folders (FR-P19-54–FR-P19-56).
- New §4P agent-era portability: Vidhi agent cards, missions, autonomy settings and MCP/A2A access logs are exportable; exports can be requested by an AI assistant only as a draft request that a human confirms (NN-14, NN-52) (FR-P19-57–FR-P19-58).
- Settings, screens, events, acceptance scenarios and open items extended accordingly.

---

## 1. Objective and business outcome

A company that uses LawDocsComply must never feel trapped. On any day — while subscribed, during a regulator's inspection, at the auditor's request, or when it leaves — it can take **all of its data** as an ordinary folder tree of Word, Excel, PDF and CSV files whose folder and file names explain themselves to a beginner, verify that nothing was altered, open everything with Microsoft Office or LibreOffice, and load it into another system. It can also keep a **continuous copy in its own storage** (its S3 bucket, Azure or Google storage, SharePoint/OneDrive, SFTP server, NAS or hard disk in its own data centre). And because the structure is defined by a versioned contract rather than by today's code, the folders do not move when LDC ships new features, changes its database, moves data centre or changes cloud: **no customer ever has to migrate their own data because LDC changed**.

The same folder taxonomy works in reverse: instead of uploading hundreds of compliance documents one by one, a company can drop a structured folder (or its existing SharePoint library) and LDC files each document against the right entity, year, department, obligation, committee or policy.

| Outcome | Exit-gate measure |
|---|---|
| Everything is exportable | The export-coverage test passes: every persisted record type in every module has an export mapping; a seeded tenant with every record type produces an `LDC-EXPORT-1.0` package in which 100% of records are present (count reconciliation per type) and 100% of documents are byte-identical to the stored originals (SHA-256) |
| Understandable without LDC | Usability test: 5 of 5 non-technical participants (a junior accountant, an office manager, a new compliance executive, a director, an external auditor) find a named Board resolution, a policy's approved version, the evidence for a specific compliance and the audit trail of a status change within 3 minutes each using only Windows Explorer/macOS Finder and Office |
| Verifiable offline | The open-source verifier (Apache-2.0) confirms hashes, the detached JWS signature, control totals and audit-chain continuity offline; it fails on a single changed byte or missing file |
| Stable across releases and infrastructure moves | Golden-tenant test: the same synthetic tenant exported before and after (a) a release with schema changes, (b) a database engine major upgrade, (c) a storage-provider swap, (d) a region move rehearsal produces **identical folder paths and file names** for unchanged records and identical record IDs; differences appear only as additive files declared in the package's `CHANGES-SINCE-PREVIOUS.csv` |
| Bring-your-own storage | A tenant connects at least one target (S3, Azure Blob, GCS, SharePoint/OneDrive, SFTP, on-premises agent to NAS/disk); residency verified; canary passes; daily incremental and monthly full copies arrive by 06:00 IST; restore test from the tenant's own copy passes |
| Folder intake | A 5,000-file structured folder is imported with ≥ 95% automatic placement on a well-structured tree (100% on a tree previously exported by LDC), duplicates detected by hash, every unplaced file listed in a review queue, nothing overwritten |
| Exit without friction | Exit export (scope EXIT) completes for a 500 GB tenant within 48 hours, followed by a read-only period, a deletion workflow that respects retention and legal hold, and a signed deletion certificate |

---

## 2. Scope (in / out)

**In scope**

- `xpt` module: export map registry, export jobs, package builder, folder policy, manifest, signing, verifier, download service, scheduled exports and backups to customer targets, intake (folder/zip/library) with mapping rules and review queue, rehydration/loader tool, exit workflow, deletion certificates, data-principal access exports (for P12 DSR responses), regulator/auditor/board packs (scoped exports used by P06, P10, P11, P15 and external-access grants).
- `StorageTarget` adapters (built on P18's connector framework): Amazon S3 (and S3-compatible: MinIO, Wasabi India, on-prem object stores), Azure Blob, Google Cloud Storage, SharePoint/OneDrive (Graph `Sites.Selected`), Google Drive (shared drive; non-regulated data only), SFTP, on-premises agent (NAS/SMB share, local disk, USB/external disk on the agent host, on-prem object store).
- Storage-key scheme and object metadata independent of code layout; content addressing; immutable versions.
- **Durability guarantees** across releases and infrastructure changes (§4E): stable IDs, expand-contract migrations, export-mapping contract tests, data contract versioning, infrastructure-move runbooks.
- Cross-product package sharing using the shared archive standard (Finbyx/Udofin evidence references, Equator referral packs by reference), and the `portability` ecosystem events (Spec §6.26).

**Out of scope**

- Platform disaster recovery, internal backups, PITR and DR drills of LDC's own infrastructure (P24; this phase only consumes their evidence). Customer copies are **in addition to**, never a replacement for, LDC's own backups.
- Business rules on what each module retains (each module and P12 retention schedules); P19 enforces retention classes and legal holds on exports and targets.
- Ops Hub exit-project tracking (OH4 receives status and counts only).

---

## 3. Personas and permissions touched

| Role | P19 permissions |
|---|---|
| `ten_admin` | Request full-tenant and exit exports (step-up + second approver), connect storage targets (with CISO approval for CONFIDENTIAL+ classes), configure scheduled exports/backups, configure folder policy (renames within bounds), run intake jobs tenant-wide, view export history |
| `ten_cco`, `ten_cs`, `ten_cfo`, `ten_cro`, `ten_dept_head` | Scoped exports within their permissions (module, department, period), board/audit/regulator packs for their areas; intake into their areas |
| `ten_maker`, `ten_checker`, other users | Personal exports of records they can see (single record or saved view), "Download as folder" on a record (e.g. a committee with all meetings) |
| `ten_internal_auditor`, `ten_external_auditor`, `ten_secretarial_auditor`, `ten_is_auditor` | Audit packs within engagement scope; watermarked; capped per grant (Spec §4.7) |
| `ten_supervisor_view` | Regulator packs within the grant's dataset catalogue; watermarked; export level per grant (`NONE`, `AGGREGATE`, `CAPPED_RECORDS`, `FULL` with second RE approval) |
| `ten_hr_admin` + DPO | Approve inclusion of restricted HR/payroll folders |
| Tenant DPO | Approve restricted folders, DSR exports, cross-border targets (blocked for regulated classes) |
| `plt_super_admin` | Platform folder-profile versions (Governed), emergency export on court/regulator order (break-glass, tenant notified unless legally barred), deletion certificates after exit |
| `plt_support` | Job status metadata only |

---

## 4. Functional requirements

### 4A. Export package `LDC-EXPORT-1.0`

**FR-P19-01 — Package standard.** Every export is an archive under Ecosystem Spec §12.1 `archive_standard_version` 1.0 with folder profile `ldc_tenant_v1` (full tree in Appendix M). Top-level folder name: `[Owner legal name] - LawDocsComply Archive - [scope] - as of [YYYY-MM-DD]/`. Mandatory `00 Start Here/` (README.pdf/.docx/.txt, `export-manifest.csv`, `manifest.json`, `manifest.json.jws`, `data-dictionary.xlsx/.csv`, `relationships.csv`, `relationship-map.pdf`, `code-tables/`, `schemas/`, `verify/`), plus LDC additions inside `00 Start Here/`: `How to find things.pdf` (one-page visual guide), `Folder guide.xlsx` (every folder, what it contains, typical questions it answers), `CHANGES-SINCE-PREVIOUS.csv` (for incremental or repeated exports), `BSA-Section-63-Certificate.pdf` and `.docx` (pre-filled certificate, §4C).

**FR-P19-02 — Top-level folders (summary; Appendix M is binding).**

```
00 Start Here
01 Organisation and Entity Profile
02 Regulatory Coverage and Applicability
03 Compliance Register and Evidence
04 Regulatory Updates and Change Log
05 Governance - Board, Committees and Meetings
06 Company Secretarial - Registers, Filings and Resolutions
07 Policies and Procedures
08 Risk Management
09 Risk Assessments - ICAAP, Stress Tests and Ratios
10 Audits and Inspections
11 Returns and Regulatory Reporting
12 Data Protection and Cyber Security
13 People - HR and Labour Compliance          (restricted parts as encrypted archives)
14 Grievances and Customer Support             (restricted parts as encrypted archives)
15 Co-operative Society Records                (only for co-operative tenants)
16 Tasks, Calendar and Approvals
17 Documents Library (all other documents)
18 Vidhi AI - Notebooks, Outputs and Activity
19 Contracts, Marketplace Engagements and Retainers
20 Billing, Subscription and Invoices
21 Users, Roles and Access History
22 Settings and Customisations
23 Integrations and Data Exchanges
24 Audit Trail
99 Restricted (encrypted archives with separate manifests)
```

Within content folders the default hierarchy is **Legal entity → Financial year → Department → item**, with the item folder named for what a person would look for (e.g. `05 Governance - Board, Committees and Meetings/ABC Finance Ltd/FY 2026-27/Audit Committee/2026-08-14 - Meeting 3 of FY 2026-27/`). Single-entity tenants omit the entity level (`folder_policy.entity_level = auto`). Financial year format `FY 2026-27` (April–March) by default; calendar-year tenants (e.g. IFSCA entities with a different accounting year, foreign parents) use `CY 2026` or their configured year (P02 setting `core.financial_year.start_month`).

**FR-P19-03 — Naming rules (binding; Spec §12.1 plus LDC rules).** Plain English; numbered top-level folders; Windows-safe (no `\ / : * ? " < > |`, no trailing dot or space, no reserved names `CON`, `PRN`, `AUX`, `NUL`, `COM1–9`, `LPT1–9`); Unicode NFC; full path ≤ 240 characters (long titles shortened with an ID suffix, e.g. `… - obl_01JB2K`); ISO 8601 dates at the start of dated items (`2026-08-14 - …`) so files sort chronologically; version suffix `v2.1` and status words (`APPROVED`, `DRAFT`, `SUPERSEDED`) in file names for documents with lifecycles; **no personal data in any folder or file name** (default `ids_only` for people-related items — e.g. employee files named by employee number, complainant files by case reference; `id_and_masked_name` only for internal archives with DPO approval); department and committee names come from the tenant's terminology registry (P02) — renaming a department changes **future** export names only, and the manifest keeps the canonical department ID so old and new names map (FR-P19-28).

**FR-P19-04 — File formats per record type (summary; Appendix M §M.4 binding).**

| Content | Files |
|---|---|
| Registers and lists (obligations, compliance instances, risks, KRIs, findings, tasks, users, registers under the Companies Act) | `.xlsx` (human; formatted, frozen header, filters, column descriptions as comments, typed cells, leading zeros preserved, "Read me" sheet) **and** `.csv` (RFC 4180, UTF-8 with BOM) **and** `.schema.json` |
| Narrative documents generated by LDC (minutes, policies, reports, ICAAP, audit reports, notices, letters) | `.docx` (editable) **and** `.pdf` (PDF/A-2b; XMP with `document_id` and source hash) |
| Original uploaded documents and evidence | As stored, byte-identical (SHA-256 equals the vault hash), with signature evidence (PAdES/eSign audit certificate) alongside |
| Type copies and translations (P17) | `.docx` + `.pdf` next to the original, named `… - TYPE COPY v1.docx`, `… - ENGLISH TRANSLATION v1.docx` |
| Regulatory/bureau/tax files generated by P11 | Exactly as generated and submitted (byte-identical), plus validation report (`.xlsx`), sign-off (`.pdf`) and acknowledgement |
| Dashboards and analytics snapshots | `.xlsx` with the underlying numbers + `.pdf` rendition |
| Calendar | `.ics` per user group and per entity + `.xlsx` list |
| Audit trail | `audit-events-YYYY-MM.jsonl` (machine) + `Audit trail YYYY-MM.xlsx` (human digest: who, what, when, before → after, reason, correction links) + chain anchors |
| Structured data for successor systems | `.jsonl` per dataset (optional, ON for full and exit exports) |
| Email and chat evidence | Original `.eml`/`.msg`/WhatsApp export + transcript `.docx`/`.pdf` |

Accounting and audit practice (R-051): financial statements and schedules exported from P09/P11/P10 keep the presentation of the applicable framework (Schedule III Division I/II/III to the Companies Act 2013 for companies; the RBI formats for banks/UCBs; IRDAI formats for insurers) as generated by those modules; audit working papers keep the engagement file structure required by SQC 1/SA 230 documentation principles (P10 owns content; Appendix J references); registers under the Companies Act keep the prescribed form layouts (MGT-1, MBP-2, MBP-4, CHG-7, BEN-3, SH-6 etc. — P06).

**FR-P19-05 — Manifest.** `export-manifest.csv` one row per file with Spec §12.1 columns (`path`, `sha256`, `bytes`, `media_type`, `record_count`, `legal_entity`, `dataset`, `schema_version`, `as_of`, `created_at`, `source_ids`, `restricted`, `retention_class`, `legal_hold`, `upsi`) plus LDC columns `record_type`, `canonical_path` (path under the canonical folder profile, unchanged by tenant renames), `department_id`, `fy`, `module`, `obligation_refs`, `content_version` (for regulatory content pins). `manifest.json` adds archive id (ULID), standard version, folder profile and version, producer release, tenant and `reid`, scope definition, requester and approvers, as-of instant, control totals per legal entity (counts per record type; documents count and bytes; audit-event count and last chain anchor; for financial datasets trial-balance totals), `predecessor_archive_id`, pack-level SHA-256 and signing key id. `manifest.json.jws` is a detached JWS with the tenant's export-signing key (public key and fingerprint printed in the README).

**FR-P19-06 — Control totals reconcile before signing.** The job snapshots data at a consistent instant (database snapshot / repeatable-read export transaction + object-version pinning) and reconciles counts and totals to the live system at that instant; any difference fails the job (no partial signed package). Large tenants export from a read replica at an agreed as-of time.

**FR-P19-07 — Restricted folders.** HR/payroll (folder 13 restricted parts), POSH Internal Committee case files, whistle-blower reports, sealed grievance complainant identity (folder 14 restricted parts), privileged legal material, UPSI, credentials (never exported — the credential vault is excluded by design; an export lists only credential metadata: portal, user ID owner, last rotated), and health data are produced as separate AES-256 encrypted ZIP archives (or age/OpenPGP to a recipient public key) each with its own manifest, included only when the requester holds `export.restricted.[class]` and a second approver (HR head or General Counsel, plus DPO) approves; the password is generated per archive and delivered out of band to the named recipient, never stored with the archive or by LDC after delivery. Aadhaar numbers and card data never appear in any export.

**FR-P19-08 — README and guides.** README (PDF, DOCX, TXT; English; Hindi optional by tenant setting) covers purpose and scope; as-of time and time zone; requester and approvers; folder guide; how to open CSV files without losing leading zeros (Excel "From Text/CSV" with column types; LibreOffice); how to verify checksums (`sha256sum -c`, PowerShell `Get-FileHash`, `CertUtil -hashfile`) and the signature (`verify/` tool); how to join tables (`relationships.csv` and the relationship map); glossary of LDC terms (obligation, compliance instance, maker, checker, evidence, correction entry, content version, overlay); restricted-folder handling; retention and legal-hold notes; contacts. A CI test asserts every folder the README names exists and every top-level folder is described.

### 4B. Export scopes, triggers and delivery

**FR-P19-09 — Scopes.**

| Scope code | What it contains | Who can request | Approvals |
|---|---|---|---|
| `RECORD` | One record and its children (e.g. one compliance instance with evidence and trail; one meeting with papers, minutes, attendance, resolutions) | Any user who can read it | None |
| `VIEW` | Records in a saved view or filter | Any user (own permissions) | None (cap 10,000 records; above needs dept head) |
| `MODULE` | One module for selected entities/periods | Module owner roles | Dept head or admin |
| `DEPARTMENT` | All modules' records owned by a department | Dept head | Admin |
| `PERIOD` | Everything for one or more financial years | `ten_admin`, CCO, CS | Admin + second approver |
| `LEGAL_ENTITY` | Everything for one legal entity | `ten_admin` | Admin + second approver |
| `BOARD_PACK` | A meeting's papers and minutes, or a period's board reports | CS, chairperson's office | CS |
| `AUDIT_PACK` | Engagement-scoped evidence and registers (Spec §4.7 grant scope) | Auditor role under grant; CCO | Per grant |
| `REGULATOR_PACK` | Inspection-scoped dataset catalogue | Supervisor under grant; CCO prepares | Per grant (second RE approval for FULL) |
| `DSR_ACCESS` | A data principal's personal data across modules (P12 DSR) | DPO | DPO + legal check |
| `FULL_TENANT` | Everything | `ten_admin` | Step-up + second approver (CCO/CISO/MD delegate) |
| `EXIT` | Full tenant + exit artefacts (FR-P19-35) | `ten_admin` | Step-up + second approver; counter-signed by LDC delivery lead for tracking |
| `BACKUP_INCREMENTAL` / `BACKUP_FULL` | Scheduled copies to a BYO target | Configured by admin | Configuration approval only |

**FR-P19-10 — Triggers.** On demand (screen action), scheduled (RRULE; e.g. monthly full on the 1st at 02:00 IST; FY-full on 30 April), event-driven (e.g. "after each Board meeting's minutes are signed, export the meeting folder to SharePoint"), on detach of a module (export before `DETACHED`, Spec §11.1), on exit request, and on court/regulator order (break-glass). Export and read access are **never** suspended for non-payment (Spec §6.26, §6.27; NN-10).

**FR-P19-10A — Never blocked (NN-42).** On-demand, scheduled and exit exports, BYO backup mirroring and restore-verification runs never depend on subscription, trial or dunning state; a tenant in `RESTRICTED` or `TERMINATION_NOTICE` (P20 §4J) keeps every export function, and the exit pack is prepared automatically on `TERMINATION_NOTICE`. Only operational capacity limits (queueing of very large jobs) apply, never a payment check.

**FR-P19-11 — Delivery options.** (a) **Download**: resumable HTTPS download from the export portal, split into parts (default 4 GB ZIP64 parts with a parts manifest) and a single-file option for small packages; links valid 7 days (T tier, 1–30), downloadable only by the requester after re-authentication; (b) **BYO storage target** (FR-P19-17); (c) **SFTP pull** from LDC's export SFTP (per-tenant chroot) for very large exports; (d) **Physical media** only for exit exports > 2 TB on request, via the on-premises agent at the tenant's site (LDC never ships disks). Progress view shows stages (snapshot, collect, render, package, reconcile, sign, deliver) with ETA; the job is resumable after interruption without restarting completed stages.

**FR-P19-12 — Watermarking and caps for external recipients.** Exports to auditors and supervisors are watermarked on PDFs and XLSX "Read me" sheets ("Confidential — supplied to [grantee] under [basis] — grant [id] — [time]"), hashed, capped per grant, and delivered only through the workspace (never by e-mail) (Spec §4.7).

**FR-P19-13 — Preview and dry run.** Before running a large export the user sees the folder tree preview with counts and estimated size, restricted items that will be excluded or encrypted, and the approvals needed; a dry run produces only the manifest and folder guide.

### 4C. Evidence integrity and legal admissibility

**FR-P19-14 — Hashes and chain.** Every document's SHA-256 is computed at upload (P07) and re-verified at export; the audit trail export includes the hash chain with daily anchors (P00) so a recipient can verify that the trail is complete for the period; correction entries (D-02) appear as their own events with links to the superseded values — the export never shows only the corrected value.

**FR-P19-15 — BSA 2023 section 63 certificate.** Each package includes a pre-filled certificate in the form prescribed under section 63(4) of the Bharatiya Sakshya Adhiniyam 2023 (Schedule form; Part A to be signed by the person in charge of the device/system on the tenant's side; Part B by an expert) describing the computer system, the process of production, the hash values (SHA-256 of `manifest.json` and the pack-level hash) and the date/time [VERIFY form wording against the official Schedule; counsel to confirm who signs Part B for SaaS-held records]. LDC provides a **platform statement** (signed by LDC's designated officer with DSC) describing the hosting, controls, hashing and ledger, which the tenant's expert may rely on. The certificate generator is also available per record (e.g. for a single evidence item needed in proceedings).

**FR-P19-16 — PDF/A and render gates.** Every generated PDF is validated as PDF/A-2b (veraPDF) and every Office file renders headless (LibreOffice) in CI and at export time on a sample; a rendering failure fails the job with an actionable error (Spec §12.1 quality gates).

### 4D. Bring-your-own storage targets

**FR-P19-17 — `StorageTarget` implementation.** Each adapter implements the Spec §12.2 interface (`describe`, `verifyResidency`, `testWrite`, `put` (resumable; `writeOnce`, `retainUntil`), `head`, `list`, `retentionInfo`, `healthCheck`) and passes certification before production.

| Provider | Authentication | India residency check | Write-once |
|---|---|---|---|
| Amazon S3 | Cross-account IAM role with `ExternalId`; bucket policy limited to the LDC role | `GetBucketLocation` = ap-south-1 or ap-south-2 | S3 Object Lock (compliance/governance) |
| S3-compatible (MinIO, on-prem object stores, Indian clouds) | Access key in tenant vault (rotate ≤ 90 days) or on-prem agent | Signed tenant attestation of site in India | Object lock where supported [VERIFY per product] |
| Azure Blob | Entra workload identity federation or user-delegation SAS ≤ 7 days | Storage account in Central/South/West India | Immutability policy (time-based retention, legal hold) |
| Google Cloud Storage | Workload identity federation | asia-south1 or asia-south2 | Retention policy with bucket lock |
| SharePoint / OneDrive (Graph) | Entra app with `Sites.Selected` for granted site only | Tenant data location for the workload is India — evidence signed by tenant IT head, re-attested annually [VERIFY Graph property] | Retention label declaring records [VERIFY per plan] |
| Google Drive (shared drive) | Service account with minimal Drive scope on a shared drive | No India data region → **non-regulated data only** | Not offered |
| SFTP | ed25519 keys, pinned host key, yearly rotation | Signed attestation of server location in India | Only if server enforces WORM (attested) |
| On-premises agent (NAS/SMB, local disk, external disk, on-prem object store) | Outbound mTLS device certificate | Signed attestation of site in India | As underlying store |

**FR-P19-18 — Data-class policy per target.** Each target declares the data classes it may hold (Spec §13.2). Regulated classes — personal data of customers/borrowers/members, KYC, grievance, HR, books of account, regulatory returns, board-confidential papers — require an India-resident target (Companies (Accounts) Rules 2014 r.3(5) for books kept in electronic mode: back-up on servers physically located in India [LAW; VERIFY current text]; RBI outsourcing/IT directions; DPDP s.16 and sector rules). Google Drive can only be configured for `PUBLIC`/`INTERNAL` and `CONFIDENTIAL` documents without personal data, books or returns (e.g. approved policies, brochures); attempts otherwise fail with `residency-blocked`. A write of a class not allowed is refused before upload.

**FR-P19-19 — Residency and health.** Residency verified at registration, weekly, and before every full or exit export; daily `healthCheck()` and canary write; credential-expiry warnings 30 days ahead; one missed backup → P2 alert, two consecutive → P1 alert and tenant notice; failures published as `ControlTestResultPublished` (control `STORAGE_TARGET_HEALTH`, result FAIL) to the tenant's compliance destination (Spec §6.26); jobs pause and are never silently retried against another target. Event `StorageTargetConnected` after checks pass.

**FR-P19-20 — Keys.** Default: per-tenant platform-managed KMS key. Options: **BYOK** (cross-account key grant or imported key material) and client-side archive encryption to the tenant's public key (age X25519 or OpenPGP); HYOK via external key store only with written risk acceptance by the tenant's CISO and CTO. Revoking a BYOK grant makes reads and exports fail closed (`key_unavailable`) with alerts to tenant and LDC operations. Regulated tenants in RBI middle/upper layers must be **offered** tenant-controlled keys (Spec §12.2 citing OUT para 97(vii)(b)).

**FR-P19-21 — Write-once.** When selected, every `put` sets the provider lock with `retainUntil` = the longest retention class in the archive (e.g. books of account 8 financial years — Companies Act 2013 s.128(5); KYC 5 years after relationship ends — PMLA; minutes permanently — s.118 read with SS-1 [P06 confirms]; tenant-configured classes) [REC]; targets that cannot honour the lock are not offered the option.

**FR-P19-22 — Backup copies to customer storage.** Schedules: `DAILY_INCREMENTAL` (changed records and new document versions since last successful copy, chained by `predecessor_archive_id`), `WEEKLY` (optional), `MONTHLY_FULL`, `FY_FULL` (after FY close + 30 days). Each copy is a valid `LDC-EXPORT-1.0` package (incremental packages carry deltas plus a cumulative manifest so the latest state can be assembled offline by the loader). `BackupCompleted` event per copy (Spec §6.26). Retention of copies in the tenant's store is the tenant's choice; LDC prunes only objects it wrote and only according to the tenant's configured policy (never beyond locks). **No promise of recovery after a customer purges its own store** (Spec §12.2).

**FR-P19-23 — Restore tests from customer copies.** Quarterly (T tier, monthly–annually) automated restore test: the verifier runs against the latest full + incrementals in the tenant's store (integrity), a sample of files is opened headless (readability), and — optionally — a rehydration into an isolated scratch tenant (rehydration) with count reconciliation; `RestoreTested` event and a report for the tenant's BCP evidence (P12/P24).

### 4E. Durability across code changes, database changes and infrastructure moves

**FR-P19-24 — Stable identifiers.** Every record has an immutable prefixed ULID (`obl_`, `cmi_`, `evd_`, `doc_`, `ver_`, `pol_`, `mtg_`, `res_`, `rsk_`, `kri_`, `aud_`, `fnd_`, `ret_`, `grv_`, `emp_`, `usr_` …) assigned at creation, never reused, never derived from database sequences or table names, preserved across exports, imports, migrations and region moves. External references (obligation_ref like `RBI/DOR/2025-26/352#124`, CIN, registration numbers) are stored as attributes, never as keys.

**FR-P19-25 — Export map registry (`xpt.export_map`).** Each record type registers, per version: record type code, owning module, canonical folder path template (e.g. `05 Governance - Board, Committees and Meetings/{entity}/{fy}/{committee_name}/{meeting_date} - {meeting_title}/`), file naming template, dataset name and columns (with JSON Pointer to the canonical model, data class, code table), document attachments rule, restricted class, retention class, and the **path stability key** (the fields that determine the path; e.g. meeting date, committee ID — never mutable display fields alone). The map is versioned under the folder profile version; a change to an existing path template is a **major** profile change requiring a Governed approval, a migration note, and dual paths in the manifest (`canonical_path` stays for one major version as `legacy_path`).

**FR-P19-26 — Export-mapping contract test (CI gate, NN-10).** CI introspects the database schema and the module registries: every persisted table/collection annotated as a business record must map to an export-map entry (or be explicitly marked `x-export: derived` with the source it is derived from, or `x-export: excluded` with a reason approved by the data architect, e.g. caches). A migration that adds a column to a mapped table must declare its export column or `x-export: internal`. A pull request that adds a record type without an export mapping fails. A golden-tenant export is diffed against the previous release's golden export: unexpected path or file-name changes fail the build.

**FR-P19-27 — Storage key scheme independent of code layout.** Object keys are `t/{tenant_id}/o/{sha256[0:2]}/{sha256[2:4]}/{doc_id}/{ver_id}` (content-addressed under the tenant prefix) with metadata `{record_type, record_id, doc_id, ver_id, sha256, media_type, created_at, data_class, retention_class, legal_hold}`; the human folder path is computed at export time from the export map — never stored as the object key. Renaming a module, department, or code package therefore never moves an object. Objects are immutable; new versions are new objects; deletion is a retention workflow with a ledger event.

**FR-P19-28 — Terminology changes and tenant renames.** Department, function, committee and policy names are tenant terminology (P02) referenced by stable IDs; a rename creates a dated alias. Exports use the name valid at the record's date by default (historical fidelity, e.g. "Credit Risk Committee" for 2025 meetings even if renamed to "Risk Management Committee" in 2026) with a tenant option to use current names; the manifest always carries the ID, so both views map. Folder policy (`folder_policy`) lets a tenant rename or split folders within bounds (top-level numbers and `00 Start Here` locked); the canonical path stays in the manifest so relationships never break (Spec §12.1).

**FR-P19-29 — Database and schema evolution.** All schema changes follow expand → migrate → contract (P00): additive columns/tables first, backfill with idempotent jobs, dual-write/dual-read where needed, contract only after a full release cycle and after the export map no longer references the old shape; no destructive migration without a verified backup and a reversible plan (NN-11). Data contracts (`packages/contracts`) for exports are semantically versioned; the loader (FR-P19-37) reads every past `ldc_tenant_v1.x` minor without loss.

**FR-P19-30 — Infrastructure moves.** Runbooks and automated tooling for: (a) database engine/provider move (Supabase → Amazon RDS/Aurora PostgreSQL): logical replication, row-count and checksum reconciliation per table, cut-over with read-only window, golden-tenant export diff = empty; (b) object storage move (bucket/provider/region within India): copy with checksum verification per object (S3 batch operations or equivalent), dual-read during migration, key re-wrap for KMS changes, Object Lock re-application where the destination supports it; (c) region pair change (ap-south-1 ↔ ap-south-2 for DR or a new India region): same as (a)+(b) with residency attestation; (d) cloud change (to another India-resident cloud): data exported in `LDC-EXPORT-1.0` + database logical dump, re-imported with ID preservation, verified by the same diff. Each move produces a **migration evidence pack** (counts, hashes, diffs, approvals) stored as control evidence (P24) and notified to tenants in advance where the sub-processor or location changes (Appendix Q sub-processor notice).

**FR-P19-31 — Release safety for customer data.** A release cannot ship if it: changes canonical export paths without a profile major; drops or renames columns still in the export map; changes ID formats; changes the meaning of a code-table value (new values allowed, existing never redefined); or fails the golden-tenant diff. New features land their data in new folders or new files declared in `CHANGES-SINCE-PREVIOUS.csv`; customers' existing copies remain valid and continue to receive incrementals without any action on their side.

### 4F. Folder-tree intake (bulk upload by folder structure)

**FR-P19-32 — Sources for intake.** (a) Browser folder upload (drag-and-drop a folder; directory upload API) or a `.zip`; (b) a connected SharePoint/OneDrive library or Google shared drive folder (P18); (c) a watched folder on the on-premises agent (NAS/disk); (d) an earlier `LDC-EXPORT-1.0` package (round-trip import into the same or a new tenant).

**FR-P19-33 — Mapping rules and placement.** Intake runs in four steps:
1. **Scan**: inventory, hashing, malware scan, file-type sniffing, duplicate detection (same SHA-256 already in the tenant → link, do not duplicate), oversized/unsupported files listed.
2. **Recognise structure**: if the tree is an LDC package (manifest present and signature valid), placement is exact by `canonical_path` and record IDs; otherwise the **mapping wizard** proposes rules from path segments using the LDC folder taxonomy and the tenant's terminology (entity names, FY patterns like `2025-26`, `FY26`, `FY 2025-2026`; department names and aliases; committee names; policy names; obligation references and short titles; regulator names), plus file-name patterns (dates, `Minutes`, `Notice`, `Agenda`, `Resolution`, `Policy`, `v2.1`, `Approved`, form numbers like `MGT-7`, `AOC-4`, `DIR-12`, `DPT-3`) and content classification (P17 intake pipeline, P07 document types). Rules are expressions like `/{entity}/{fy}/{department}/Policies/{policy_name}*.docx → policy version (status from name, date from metadata)`.
3. **Preview**: a table of every file with proposed destination (record type, record, entity, FY, department), confidence, conflicts (e.g. a policy version number already exists with a different hash), and actions (accept, change destination, skip, create new record — e.g. create a historical meeting record from a folder of minutes); bulk-accept by rule.
4. **Commit**: creates documents/versions and links; never overwrites an existing version (conflicts become new versions labelled `IMPORTED` with original file timestamps recorded as `source_created_at`; D-02 bitemporal); produces an **intake report** (`.xlsx`) and a review queue for unplaced files; everything is reversible for 7 days (T tier) through an intake rollback that removes only what that intake created.
Vidhi assistance (V-SK-02, V-SK-04) may propose classifications and extract dates/parties; a human confirms rules before commit.

**FR-P19-34 — Historical records import.** Intake can create historical records with their original dates (past meetings and minutes, past policy versions with Board approval dates, past audit reports, past returns and acknowledgements) flagged `imported_historical = true`, so registers and timelines are complete from day one without pretending the events happened in LDC.

### 4G. Exit, read-only period and deletion

**FR-P19-35 — Exit workflow.** `EXIT_REQUESTED` (admin + second approver) → **exit export** (scope EXIT: full tenant + restricted archives as approved + all versions + full audit trail + configuration + integration mapping history + AI ledger) → **tenant confirmation** that the package was received and verified (the verifier report is uploaded or confirmed) → **read-only period** (default 90 days after contract end, T tier 30–180; G tier minimum 30) during which users can log in read-only and re-download → **deletion** of tenant data from LDC primary stores, search indexes, AI stores, caches and replicas, and scheduled purge from backups at their natural expiry (backups are immutable; data in them expires with the backup retention, documented in the certificate) → **deletion certificate** (PDF signed by LDC with DSC: scope, dates, systems, backup expiry dates, exceptions) → `CLOSED`. Exceptions: legal holds, statutory retention that LDC itself must keep (e.g. LDC's own invoices and tax records for the tenant's subscription), records under a pending court or regulator order; each exception listed with its basis. For regulated entities, exit cooperates with the RE's outsourcing exit plan (RBI outsourcing directions require continuity and return of data on termination [VERIFY paras]); LDC provides transition assistance as a marketplace service (P21) if requested.

**FR-P19-36 — Exit events and Ops Hub.** `ExportRequested`/`ExportCompleted` (scope EXIT) to the tenant's compliance destination; Ops Hub OH4 receives exit-project status and counts only (Spec §6.26). Billing (P20) never blocks export.

### 4H. Rehydration and successor-system tooling

**FR-P19-37 — Loader and verifier.** Open-source (Apache-2.0) command-line and desktop tools shipped in `verify/` and on the developer portal: `ldc-verify` (hashes, JWS, control totals, chain anchors, CSV schema conformance) and `ldc-load` (loads datasets into PostgreSQL, SQLite or SQL Server with generated DDL from the JSON Schemas; reassembles incremental chains; produces a load report). A reference "viewer" (static HTML generated inside the package, optional, offline) lets non-technical users browse registers with links to documents [REC; flag `xpt.offline_viewer.enabled`, default ON for full and exit exports].

**FR-P19-38 — Re-import into LDC.** An `LDC-EXPORT-1.0` package can be imported into a new LDC tenant (e.g. a company re-joining, a demerger, a group restructuring) with ID preservation and the audit trail kept as imported history; signatures validated; restricted archives imported only with their passwords and approvals.

### 4I. Cross-product sharing

**FR-P19-39 — Shared archive standard across the ecosystem.** Because Finbyx, Udofin and LDC use the same archive standard, an RE can assemble an inspection or audit package that references Finbyx and Udofin archives (by `archive_id` and manifest hash) without duplicating files. LDC packages reference evidence that lives in an operating product's India store by `evidence_id` + SHA-256 + producer (Spec §9.2: evidence stored in the producing product); the tenant may choose "include copies" (if the producer allows and the grant permits) or "include references".

**FR-P19-40 — Sharing packages with other products and parties.** A package (or a folder within it) can be shared to: another LDC tenant under a `tenant_link` (e.g. a group company, a successor), an Equator referral (by reference, with consent), a marketplace engagement (P21: e.g. sharing the policy folder with the professional drafting the ICAAP), or an external auditor workspace; every share is a scoped, expiring grant with access logging, never an open link.

### 4J. Fewer clicks

**FR-P19-41 — One-click actions.** "Download as folder" on every list and record; "Export this year for the auditor" preset; "Send to my SharePoint" on any document set after the target is connected; "Copy this meeting's folder path" for staff who keep a mirror; intake from "Upload folder" button on DMS, committee pages, policy library and compliance register with automatic context (the current page pre-sets the mapping root).

### 4K. Exports for the v1.1 modules *(v1.1)*

**FR-P19-42 — New folders.** The export map gains folders `25 Global Entities and Jurisdictions` (P25), `26 Legal Matters, Contracts and Licences` (P26), `27 ESG, BRSR and Sustainability` (P27), `28 Reports, MIS and Board Packs` (P28) and `29 AI Governance - Systems, Assessments and Incidents` (OV_AI, P12) exactly as Appendix M §M.3 defines them. Folders are appended; existing numbers never change (NN-45). Profile `ldc_tenant_v1` becomes 1.1.0; a reader built for 1.0.0 ignores unknown folders without error.

**FR-P19-43 — Module export registration.** P25–P28 and the OV_AI module register every record type in `xpt.export_map` before their exit gates (OP-3; Appendix M §M.15 v1.1 rows). Privileged legal advice, regulator-confidential inspection material flagged by the tenant, and officers' personal data beyond what registers require go to `99 Restricted` only.

**FR-P19-44 — Report reproducibility in exports.** Report runs (P28) export with `parameters.json`, the data-snapshot hash and the template version so that a successor system can confirm the figures; board packs export as the frozen, hashed pack.

**FR-P19-45 — Bilingual sources.** For foreign checkpoints and filings, exports carry both the official-language source text and the reviewed English translation (NN-54); machine translations are labelled as such.

### 4L. Multi-region exports and the group index *(v1.1)*

**FR-P19-46 — Per-cell packages.** A tenant with legal entities in more than one cell receives one package per cell, produced, checksummed and signed in that cell (Appendix M §M.19). The export wizard shows each package's cell and its storage target; choosing a target outside the cell requires a recorded transfer basis (LDC-INT-131).

**FR-P19-47 — Group index.** A `00 Group Index` package built from aggregates in the group home cell lists every per-cell package, entities, checksums and download locations; it never contains personal data or document content from other cells.

**FR-P19-48 — Scheduled group exports.** A single schedule ("monthly group export to our storage") fans out into per-cell jobs and a group index; failures in one cell do not block others and are reported per cell.

### 4M. Home-cell migration *(v1.1; D-42)*

**FR-P19-49 — Governed migration.** Changing a legal entity's home cell is a Governed change (tenant admin request + platform security officer approval + DPO note of the transfer basis) executed as a Temporal workflow: freeze writes for the entity → source-cell export with `migration-manifest.json` → transfer over the inter-cell link → destination import with per-file hash and per-type count verification → audit-chain continuation with a migration anchor → routing switch (`CellRoutingChanged`) → source retention and deletion certificate. Rollback is automatic if any verification fails.

**FR-P19-50 — Indian entities.** An Indian entity's home cell is IN and cannot be migrated without a recorded legal basis and the client's written instruction (NN-24 as amended); the request screen states this before the user starts.

**FR-P19-51 — Downtime budget.** Entity-level freeze ≤ 2 hours for entities up to 20 GB [REC]; users of other entities in the same tenant are unaffected; the migration evidence pack is filed under `24 Audit Trail/Migrations/`.

### 4N. Exit runbook and escrow *(v1.1; G5 TM-404)*

**FR-P19-52 — Published exit runbook.** The runbook of Appendix M §M.21 is generated per tenant (contract dates, notice period, read-only window, export schedule, transition-assistance hours, contacts) and downloadable from Settings → Data → Exit plan, so RE customers can attach it to their outsourcing exit plans.

**FR-P19-53 — Escrow.** Optional data escrow (encrypted LDC-EXPORT package deposited with an escrow agent on a schedule, with deposit receipts) and source-code escrow (Enterprise) are commercial add-ons in P20; deposits are logged and verified (test restore once a year).

### 4O. Reversible intake *(v1.1; NN-49)*

**FR-P19-54 — Undo window.** Every folder intake, zip intake and bulk import is one change set with a default 24-hour undo window (`xpt.intake.undo_window_hours`, T, 1–168). Undo applies compensating changes (documents moved back to staging, links removed, records created by the intake retired); items already checked or approved are listed and require explicit confirmation; after the window, corrections use Correction Entries.

**FR-P19-55 — New-folder recognition.** The mapper recognises folders 25–29 and their sub-folders (Appendix M §M.22) and proposes targets (matters, contracts, licences, BRSR, reports, AI systems).

**FR-P19-56 — Tracker import assist.** For customers arriving with spreadsheets and folder dumps from another tool, Vidhi proposes a mapping plan (folder → module, columns → fields, unknown columns → custom fields) that a human reviews; nothing is written until the plan is approved, and the whole import remains undoable (IMP-005, IMP-009 alignment with P03).

### 4P. Agent-era portability *(v1.1; Appendix AA)*

**FR-P19-57 — Agent artefacts.** Agent cards, autonomy settings, mission definitions and histories, agent review records, MCP client approvals and A2A peer settings export to folder 18 (`18 Vidhi AI - Notebooks, Outputs and Activity/Agents/`) and `22 Settings and Customisations/`; external-AI access logs (`ExternalAiAccessed`) to folder 18.

**FR-P19-58 — Exports requested by AI.** An external AI assistant (MCP) or a Vidhi agent can only *propose* an export (a draft request in the user's Work Inbox); a human starts it; the download link is never returned to the AI client (NN-14, NN-52).

---

## 5. Workflows and state machines

### 5.1 Export job (`xpt.jobs.state`)

```
REQUESTED → AWAITING_APPROVAL (scopes needing approval; step-up recorded) → APPROVED
→ SNAPSHOTTING (consistent as-of instant; object versions pinned)
→ COLLECTING (per record type via export map; parallel by module)
→ RENDERING (DOCX/PDF/XLSX generation; PDF/A validation; headless render sample)
→ PACKAGING (folder tree, naming, restricted archives, offline viewer)
→ RECONCILING (control totals vs snapshot) ─ mismatch → FAILED_RECONCILIATION (no signed output)
→ SIGNING (manifest, JWS, BSA s.63 pre-fill) → DELIVERING (download / target / SFTP)
→ DELIVERED → CONFIRMED (recipient or target acknowledges; ExportCompleted emitted)
any stage → FAILED_RETRYABLE (resume from last completed stage) | FAILED (non-retryable; reason) | CANCELLED
links: EXPIRED after download window; package retained in LDC export store for 30 days (T tier 7–90) then purged
```

### 5.2 Storage target lifecycle

```
DRAFT → CREDENTIALS_PROVIDED → RESIDENCY_VERIFIED → CANARY_PASSED → APPROVED (CISO for ≥ CONFIDENTIAL)
→ ACTIVE ⇄ DEGRADED (health fail) → SUSPENDED (credential revoked, residency fail, key unavailable)
→ DECOMMISSIONED (no new writes; tenant keeps its data)
weekly: re-verify residency; daily: canary; 30 days before credential expiry: warn
```

### 5.3 Scheduled backup copy

```
schedule tick → check target ACTIVE and residency fresh (< 7 days) → build incremental since last CONFIRMED copy
→ put objects (resumable; writeOnce/retainUntil if set) → put manifest last (commit marker)
→ head/verify checksums → BackupCompleted → if failure: P2 alert; second consecutive failure: P1 + tenant notice + ControlTestResultPublished(FAIL)
```

### 5.4 Folder intake

```
UPLOADED/CONNECTED → SCANNING → STRUCTURE_RECOGNISED (LDC package | mapped by rules | unknown)
→ RULES_DRAFTED (wizard + Vidhi proposals) → PREVIEW_READY → COMMITTING (by batch; idempotent per file hash + destination)
→ COMMITTED (intake report; review queue for unplaced) → [within 7 days] ROLLED_BACK (only items created by this intake)
```

### 5.5 Exit

```
EXIT_REQUESTED → APPROVED → EXIT_EXPORTING → EXIT_DELIVERED → TENANT_VERIFIED (verifier report)
→ READ_ONLY (90 days default) → DELETION_PLANNED (exceptions listed) → DELETING (primary, indexes, AI stores, caches, replicas)
→ DELETION_VERIFIED (sampling + counts zero) → CERTIFICATE_ISSUED → CLOSED
legal hold at any point → pause deletion for held records; certificate lists them
```

### 5.6 Release gate for portability (CI)

```
on PR: schema introspection → export-map coverage check → golden-tenant export → diff vs main
  unexpected path/name change → FAIL
  new record type without mapping → FAIL
  column dropped while mapped → FAIL
  render/PDF-A failures → FAIL
  CHANGES-SINCE-PREVIOUS entries generated for additive changes → PASS with report
```

---

## 6. Screens and UX

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-XPT-01 | Data & exports home | Settings → Data & exports | Cards: Download my data, Scheduled copies, Storage targets, Import folders, Exit & deletion, Export history |
| SCR-XPT-02 | New export wizard | Settings → Data & exports → New export | Scope → filters (entity, FY, module, department) → restricted items → delivery → preview tree with counts/size → approvals |
| SCR-XPT-03 | Export job detail | Settings → Data & exports → History → [job] | Stage progress, ETA, reconciliation report, download parts, verifier instructions, BSA certificate |
| SCR-XPT-04 | Storage targets | Settings → Data & exports → Storage targets | Add target wizard per provider; residency status; canary; data classes allowed; keys; write-once |
| SCR-XPT-05 | Scheduled copies | Settings → Data & exports → Scheduled copies | Schedules, last success, next run, restore tests, alerts |
| SCR-XPT-06 | Folder policy | Settings → Data & exports → Folder naming | Renames within bounds, entity level, FY format, name mode (historical/current), language of README |
| SCR-XPT-07 | Import folders | DMS → Import → Folder / Settings → Data & exports → Import | Source choice, scan results, mapping wizard, preview table, commit, rollback |
| SCR-XPT-08 | Intake review queue | DMS → Import → Review queue | Unplaced files, suggestions, bulk actions |
| SCR-XPT-09 | Exit & deletion | Settings → Data & exports → Exit | Exit request, read-only status, deletion plan, certificate download |
| SCR-XPT-10 | Download as folder (contextual) | Any list/record → ⋯ → Download as folder | Instant for small scopes; job for large |
| SCR-XPT-11 | Package viewer (offline, inside export) | `00 Start Here/Open me - Viewer.html` | Static, accessible, no network calls |
| SCR-CON-XPT-01 | Platform export operations | Console → Data → Exports | Metadata only; break-glass exports; deletion certificates |
| SCR-CON-XPT-02 | Folder profile registry | Console → Data → Folder profiles | Versions, export map, golden diffs |

UX: the export wizard always shows "What you will get" as a folder tree with sample file names; size and time estimates; and plain-language explanations of restricted items. "i" help keys: `help.xpt.folder_tree`, `help.xpt.verify`, `help.xpt.restricted`, `help.xpt.residency`, `help.xpt.write_once`, `help.xpt.intake_rules`, `help.xpt.exit`.

**Screens added in v1.1** *(v1.1)*

| Screen ID | Name | Menu path | Notes |
|---|---|---|---|
| SCR-XPT-20 | Group export (multi-cell) | Settings → Data → Export → Group | Per-cell packages, targets, group index, status per cell |
| SCR-XPT-21 | Exit plan | Settings → Data → Exit plan | Generated runbook, escrow status, deposit receipts |
| SCR-XPT-22 | Intake undo | Settings → Data → Intake history | Change sets, undo countdown, confirmations needed |
| SCR-CELL-03 | Home-cell migration (P25 owner; P19 workflow) | Settings → Data residency → Move entity | Basis, approvals, progress, verification report |

---

## 7. Backend design

### 7.1 Modules touched

`xpt` (owner); `dms` (documents, versions, renditions); `core` (ledger anchors, snapshots, IDs); `cfg` (folder policy, terminology); `int` (connector host, agent, Graph/Google adapters); every record-owning module (export-map registrations); `bil` (no gating of exports); `ai` (intake assistance, AI artefact export).

### 7.2 Tables (schema `xpt`)

| Table | Key columns |
|---|---|
| `xpt.folder_profiles` (platform) | profile_id (`ldc_tenant_v1`), version (semver), archive_standard_version, status, released_at |
| `xpt.export_map` (platform) | record_type, owning_module, profile_version, path_template, file_template, dataset, columns_json, attachments_rule, restricted_class, retention_class, stability_keys[], status |
| `xpt.folder_policies` | tenant_id, version, renames_json, entity_level, fy_format, name_mode, readme_languages[], approved_by |
| `xpt.jobs` | job_id, tenant_id, scope_code, scope_filter_json, requester_id, approvers_json, as_of, state, stage_progress_json, archive_id, delivery_kind, target_id, sizes_json, error |
| `xpt.archives` | archive_id (ULID), tenant_id, job_id, profile_version, manifest_hash, pack_hash, jws_kid, predecessor_archive_id, bytes, file_count, created_at, expires_at |
| `xpt.restricted_archives` | archive_id, class, recipient_user_id, delivered_at, approvers_json (password never stored) |
| `xpt.storage_targets` | target_id, tenant_id, provider, config_ref (vault), region, residency_state, residency_checked_at, data_classes_allowed[], key_mode, write_once, retain_policy, state, cert_version |
| `xpt.schedules` | schedule_id, tenant_id, kind (BACKUP_INCREMENTAL, BACKUP_FULL, FY_FULL, EVENT_EXPORT), rrule, target_id, scope_filter_json, status, last_success_at |
| `xpt.restore_tests` | test_id, tenant_id, archive_id, type (INTEGRITY, READABILITY, REHYDRATION), result, discrepancies, report_ref |
| `xpt.intakes` | intake_id, tenant_id, source_kind, root_ref, state, rules_json, stats_json, committed_at, rollback_until |
| `xpt.intake_items` | intake_id, path, sha256, size, detected_type, proposed_dest_json, confidence, decision, created_record_ref |
| `xpt.exits` | exit_id, tenant_id, state, contract_end_at, read_only_until, exceptions_json, certificate_ref |
| `xpt.golden_diffs` (platform) | release, profile_version, diff_ref, verdict |

### 7.3 APIs

| Method & path | Purpose | Scope |
|---|---|---|
| `POST /v1/exports` | Create export job (scope, filters, delivery) | `xpt.export:create` (+ approvals) |
| `GET /v1/exports/{id}`; `GET /v1/exports/{id}/parts` | Status; signed download URLs | `xpt.export:read` |
| `POST /v1/exports/{id}/approve` / `/cancel` | Approvals | `xpt.export:approve` |
| `POST /v1/exports/preview` | Folder-tree preview with counts | `xpt.export:create` |
| `GET/POST/PATCH /v1/storage-targets`; `POST /v1/storage-targets/{id}/verify` | Targets | `xpt.target:manage` |
| `GET/POST/PATCH/DELETE /v1/export-schedules` | Scheduled copies | `xpt.schedule:manage` |
| `POST /v1/intakes`; `GET /v1/intakes/{id}`; `PUT /v1/intakes/{id}/rules`; `POST /v1/intakes/{id}/commit`; `POST /v1/intakes/{id}/rollback` | Folder intake | `xpt.intake:*` |
| `GET/PUT /v1/folder-policy` | Folder policy | `xpt.policy:admin` |
| `POST /v1/exits`; `GET /v1/exits/{id}`; `GET /v1/exits/{id}/certificate` | Exit | `xpt.exit:*` |
| `GET /v1/export-map` | Published export map (developer portal) | public (docs) |

### 7.4 Events

Ecosystem (Spec §6.26, exact names): `ExportRequested`, `ExportCompleted` (signed), `StorageTargetConnected`, `BackupCompleted`, `RestoreTested`; storage health failure → `ControlTestResultPublished` (`STORAGE_TARGET_HEALTH`). Internal (`in.lawdocscomply.xpt.*`): `ExportJobStateChanged`, `ExportReconciliationFailed`, `IntakeCommitted`, `IntakeRolledBack`, `ExitStateChanged`, `DeletionCertificateIssued`, `FolderProfileReleased`, `StorageTargetDegraded`.

### 7.5 Jobs and Temporal workflows

`ExportWorkflow` (stages as §5.1; resumable activities; per-module collectors; rendering pool with LibreOffice/Gotenberg and veraPDF), `BackupScheduleDispatcher`, `StorageTargetHealthProbe` (daily canary; weekly residency), `RestoreTestWorkflow` (quarterly), `IntakeWorkflow`, `ExitWorkflow`, `DeletionWorkflow` (with legal-hold checks; deletion verification sampling), `ExportStorePurge`, `GoldenTenantExportCI` (pipeline job), `InfraMoveReconciliation` (on demand, P24 runbooks).

---

## 8. Integrations

`StorageTarget` adapters (§4D) on the P18 connector host; Microsoft Graph and Google Drive adapters shared with P18 `WorkplaceProvider`; on-premises agent jobs `STORAGE_PUT` and `FOLDER_WATCH`; KMS (AWS KMS ap-south-1/2) for per-tenant keys, BYOK grants; Gotenberg/LibreOffice and veraPDF in the rendering pool; ecosystem `portability` events to Finbyx/Udofin (when the RE's register wants LDC archive evidence) and status/counts to the Ops Hub.

---

## 9. Settings and configuration

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `xpt.download.link_validity_days` | T | 7 | 1–30 | `ten_admin` |
| `xpt.download.part_size_gb` | T | 4 | 1–10 | `ten_admin` |
| `xpt.store.retention_days` | T | 30 | 7–90 | `ten_admin` |
| `xpt.full_export.requires_second_approver` | L | true | — | locked |
| `xpt.restricted.requires_dpo` | L | true | — | locked |
| `xpt.folder.entity_level` | T | auto | auto/always/never | `ten_admin` |
| `xpt.folder.fy_format` | T | `FY YYYY-YY` | enum | `ten_admin` |
| `xpt.folder.name_mode` | T | historical | historical/current | `ten_admin` |
| `xpt.folder.people_naming` | G | ids_only | ids_only / id_and_masked_name (DPO approval) | platform + tenant DPO |
| `xpt.readme.languages` | T | [en] | en, hi, others as available | `ten_admin` |
| `xpt.offline_viewer.enabled` | T | true | bool | `ten_admin` |
| `xpt.jsonl.include` | T | true for FULL/EXIT | bool | `ten_admin` |
| `xpt.backup.daily_incremental_time` | T | 01:30 IST | 00:00–05:00 | `ten_admin` |
| `xpt.restore_test.frequency` | T | quarterly | monthly–annually | `ten_admin` |
| `xpt.target.residency_recheck_days` | L | 7 | — | locked (Spec §12.2) |
| `xpt.intake.rollback_days` | T | 7 | 1–30 | `ten_admin` |
| `xpt.intake.max_files_per_job` | G | 50,000 | 1,000–500,000 | platform |
| `xpt.exit.read_only_days` | T | 90 | 30–180 | contract / `ten_admin` |
| `xpt.deletion.backup_expiry_disclosure` | L | true | — | locked |
| `xpt.bsa63.include` | T | true | bool | `ten_admin` |

**Settings added in v1.1** *(v1.1)*

| Key | Tier | Default | Bounds | Changed by |
|---|---|---|---|---|
| `xpt.intake.undo_window_hours` | T | 24 | 1–168 | `ten_admin` |
| `xpt.group_export.enabled` | T | true for multi-cell tenants | — | `ten_admin` |
| `xpt.cross_cell_target.require_basis` | L | true | — | — |
| `xpt.migration.max_freeze_hours` | G | 2 | 1–12 | `plt_security_officer` |
| `xpt.escrow.data.enabled` | T | false | requires P20 add-on | `ten_admin` |
| `xpt.escrow.data.frequency` | T | monthly | weekly–quarterly | `ten_admin` |
| `xpt.profile.version` | L | `ldc_tenant_v1` 1.1.0 | — | — |

---

## 10. Security, privacy and audit

- Exports are among the highest-risk operations: step-up authentication, second approver for broad scopes (NN-05), rate limits, anomaly alerts (exports > 10× the tenant's median, exports outside working hours by non-admins), watermarking for external recipients, and full ledger entries (who, scope, as-of, files, hashes, deliveries, downloads by IP/device).
- Download URLs are short-lived, single-user, bound to the session; packages encrypted at rest in the export store with the tenant key; purged after the retention window.
- Restricted classes encrypted separately with out-of-band passwords; credentials never exported (NN-17); Aadhaar and card data never exported (NN-12, NN-16).
- Residency enforced per target and class (NN-24); Google Drive limited to non-regulated data.
- DPDP: DSR access exports (P12) reuse the pipeline with a person-centric scope; erasure requests honour retention and legal hold and explain what was kept and why (Spec §13.3).
- Deletion: verified, certificated, with backup expiry dates disclosed; no silent retention.
- Certification evidence (Appendix Q): SOC 2 CC6/CC7/A1 (availability), ISO/IEC 27001:2022 A.5.33 (protection of records), A.8.13 (information backup), A.8.10 (information deletion), A.5.34 (privacy and PII protection), ISO 22301 continuity evidence from restore tests.

---

## 11. AI touchpoints and guardrails

Vidhi proposes intake mapping rules and classifications (P17 V-SK-02/V-SK-04); a human approves rules before commit. Vidhi drafts the README's "highlights" page for a package (counts and key items, figures bound to manifest totals). Vidhi never triggers exports, approves restricted inclusions, or receives restricted archive passwords (NN-14).

---

## 12. Acceptance criteria (`tests/acceptance/p19/*.feature`)

```gherkin
Feature: Complete, verifiable export
  Scenario: Full tenant export reconciles and verifies offline
    Given the golden synthetic tenant with every record type
    When the admin requests a FULL_TENANT export and a second approver approves
    Then the package contains "00 Start Here" with README, manifest, JWS, data dictionary and verifier
    And control totals equal the live counts at the as-of instant for every record type
    And every document is byte-identical to the vault original
    And "ldc-verify" reports PASS offline
    And changing one byte in any file makes "ldc-verify" report FAIL naming the file

  Scenario: Export never blocked for non-payment
    Given the tenant's subscription is in dunning
    When the admin requests a FULL_TENANT export
    Then the export runs without an entitlement error

Feature: Stable structure across releases
  Scenario: Release with schema change keeps paths
    Given golden exports from release N
    When release N+1 adds a column to compliance instances and a new record type "attestation_campaign"
    Then paths and file names of unchanged records are identical
    And "CHANGES-SINCE-PREVIOUS.csv" lists the new folder and the new column
    And record IDs are unchanged

  Scenario: Department rename does not break mapping
    Given the department "Credit Risk" (id dep_01) was renamed "Risk Management" on 2026-07-01
    When the admin exports FY 2025-26 and FY 2026-27 with name mode "historical"
    Then FY 2025-26 folders use "Credit Risk" and FY 2026-27 folders use "Risk Management"
    And the manifest maps both to department id dep_01

  Scenario: CI blocks an unmapped record type
    Given a pull request adds table "cmp.waiver_requests" without an export mapping
    Then the export-mapping contract test fails the build

Feature: BYO storage
  Scenario: Non-India bucket refused for regulated data
    Given a tenant registers an S3 bucket in us-east-1
    When the target is configured for data classes including PII
    Then residency verification fails with "residency-blocked"
    And the target cannot be activated for those classes

  Scenario: Google Drive limited to non-regulated data
    When the admin selects Google Drive and data class "FINANCIAL"
    Then the option is rejected with an explanation

  Scenario: Missed backups escalate
    Given daily incremental copies to target T
    When two consecutive copies fail
    Then a P1 alert and a tenant notice are raised
    And ControlTestResultPublished with control STORAGE_TARGET_HEALTH result FAIL is emitted

Feature: Folder intake
  Scenario: Round-trip of an LDC package
    Given an LDC-EXPORT-1.0 package exported from tenant A
    When it is imported into new tenant B
    Then 100% of documents are placed at their canonical destinations with original IDs
    And the audit trail is imported as history labelled with source archive id

  Scenario: Nothing is overwritten
    Given a policy version 2.1 exists with hash H1
    When an intake contains "Policy v2.1.docx" with hash H2
    Then a new version labelled IMPORTED is created
    And version 2.1 with hash H1 is unchanged

Feature: Restricted data
  Scenario: HR folder needs DPO approval
    Given the admin requests a FULL_TENANT export including HR restricted data
    Then the HR archive is produced only after HR head and DPO approve
    And the archive password is delivered out of band to the named recipient
    And no export contains an Aadhaar number

Feature: Exit
  Scenario: Exit with deletion certificate
    Given an exit request approved on 2026-11-01 with read-only period 90 days
    When the read-only period ends and no legal hold exists
    Then tenant data is deleted from primary stores, indexes and AI stores
    And a signed deletion certificate lists backup expiry dates
```

NN tests: `NN-10_export_coverage`, `NN-10_golden_path_stability`, `NN-11_no_destructive_migration`, `NN-09_export_hash_integrity`, `NN-12_no_aadhaar_in_exports`, `NN-17_no_credentials_in_exports`, `NN-24_target_residency`, `NN-29_detach_keeps_history`, `NN-05_full_export_second_approver`.

```gherkin
Feature: v1.1 — new folders, multi-region exports, migration, undo

  Scenario: New module records appear in their folders
    Given tenant T has a legal matter, a BRSR report, a board pack run and an AI system record
    When a full export runs
    Then they appear under folders 26, 27, 28 and 29 respectively
    And folders 01–24 keep their v1.0 names and numbers

  Scenario: Per-cell packages for a multi-region group
    Given tenant G has an Indian entity (cell IN) and a UAE entity (cell GCC)
    When the admin starts a group export
    Then two packages are produced, one in each cell, plus a group index without personal data

  Scenario: Indian entity cannot be moved without basis
    When an admin requests to move an Indian entity to the EU cell without a recorded legal basis
    Then the request is blocked with an explanation of NN-24

  Scenario: Migration verifies every file
    Given an approved migration of entity E from SG to IN
    When one file hash differs at the destination
    Then the migration rolls back automatically and the entity stays in SG with writes re-enabled

  Scenario: Intake can be undone within 24 hours
    Given a folder intake created 96 evidence links 5 hours ago, 4 of which were approved
    When the user clicks Undo
    Then 92 links are reverted, the 4 approved items are listed for explicit confirmation, and the ledger records the undo

  Scenario: AI cannot obtain an export link
    When an external AI assistant asks LDC to export the compliance register
    Then a draft export request lands in the user's Work Inbox and no download link is returned to the assistant
```

---

## 13. Deliverables and exit gate

**Deliverables**: `xpt` module; export map registry and registrations for all modules built so far (later phases add theirs before their exit gate); package builder; restricted-archive builder; BSA s.63 pre-fill generator and platform statement; offline viewer; `ldc-verify` and `ldc-load` (Apache-2.0, signed releases, Windows/macOS/Linux); storage adapters (S3, S3-compatible, Azure Blob, GCS, SharePoint/OneDrive, Google Drive, SFTP, on-prem agent jobs); scheduled copies and restore tests; folder intake with mapping wizard and review queue; exit and deletion workflows with certificate; CI gates (coverage, golden diff, render/PDF-A); runbooks (`docs/runbooks/export-failure.md`, `storage-target-incident.md`, `infra-move-database.md`, `infra-move-object-storage.md`, `region-move.md`, `tenant-exit.md`, `court-order-export.md`); usability test report (§1 measure).

**Exit gate**: §12 scenarios and NN tests green; Ecosystem Spec §14.3 "Archive and storage" group green; usability test passed; 500 GB synthetic tenant exit export ≤ 48 h; 50,000-document intake completes with rollback verified; infrastructure-move rehearsal (database provider and object-store move in staging) with empty golden diff and evidence pack.

---

## 14. Open items and verification flags

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P19-01 | BSA 2023 s.63 certificate form text and who signs Part B for SaaS-held records | Counsel | General Counsel | Platform statement + tenant-signed Part A; Part B by tenant's expert |
| OI-P19-02 | Companies (Accounts) Rules r.3(5) current text on India back-up servers and daily back-up | Verify latest amendment | Company Secretary | Treat as India-only for books and returns |
| OI-P19-03 | Microsoft Graph property/evidence for SharePoint data location India | Vendor | CTO | Signed IT-head attestation |
| OI-P19-04 | Retention labels and immutability on client M365 plans | Plan-dependent | CTO | No write-once option for SharePoint |
| OI-P19-05 | Object-lock support on Indian S3-compatible providers | Vendor | CTO | No write-once option |
| OI-P19-06 | RBI outsourcing directions — exit/termination and data return paragraphs for SaaS GRC providers | Counsel mapping | Compliance | Exit workflow as specified |
| OI-P19-07 | Statutory retention periods per record class (minutes permanent; registers; KYC; HR records under Labour Codes; tax) | Each module/P12 | Module owners | Longest-known retention applied to write-once |
| OI-P19-08 | Hindi README translation quality | AI/translation | Content team | English only |
| OI-P19-09 | Physical media exit handling via agent for > 2 TB | Operational | Delivery lead | Multi-part download / SFTP |

**Open items added in v1.1** *(v1.1)*

| OI ID | Item | Why open | Owner | Fallback / flag |
|---|---|---|---|---|
| OI-P19-21 | Inter-cell transfer mechanism and per-law transfer instruments (SCCs, UAE/DIFC, Singapore) | Counsel per cell | DPO / counsel | Cells other than IN disabled |
| OI-P19-22 | Escrow agent selection and release conditions | Commercial | Owner | Escrow OFF |
| OI-P19-23 | Migration downtime budget for large entities | Needs load test | CTO | Maintenance window agreed per case |

---

## 15. Sources (accessed 25 October 2026 unless stated)

1. Infrabyx Ecosystem Integration Specification v1.1 — §12 (formats), §12.1 (archive standard 1.0), §12.2 (customer-controlled storage connector contract), §6.26 (portability events), §6.27 (no suspension of export for non-payment), §11.1 (detach never deletes regulated records), §13.2–13.3 (classes, retention, legal hold).
2. Bharatiya Sakshya Adhiniyam 2023, s.63 and the Schedule (certificate) [LAW; VERIFY form].
3. Companies Act 2013, ss.118 (minutes), 128 (books of account; s.128(5) eight years), 120 (electronic records); Companies (Accounts) Rules 2014, r.3 (books in electronic form, back-up in India, audit trail) [LAW; VERIFY current amendments].
4. Prevention of Money-laundering Act 2002, s.12 (record retention) [LAW].
5. Digital Personal Data Protection Act 2023, ss.8(7) (erasure), 16 (cross-border); DPDP Rules 2025 [LAW].
6. ISO 19005-2 (PDF/A-2); ISO/IEC 29500 (OOXML); RFC 4180 (CSV); JSON Schema 2020-12; RFC 7515/7797 (JWS, detached payload).
7. veraPDF (PDF/A validation): https://verapdf.org ; LibreOffice headless conversion.
8. ISO/IEC 27001:2022 Annex A controls 5.33, 8.10, 8.13; ISO 22301:2019.
9. Microsoft Graph `Sites.Selected` (Microsoft 365 Developer Blog, 9 Feb 2024).

---

## 16. Master integration notes (pack lead, v1.1, 25 October 2026)

**From v1.0 integration:** NN-42, NN-45; X-27 (Appendix M folder names authoritative).

**Added in v1.1:** NN-24; X-47, X-50.

Where any text above conflicts with these rules and resolutions, master §4 and §18 prevail. Events that cross into another product use the Ecosystem Spec type `in.infrabyx.<domain>.<EventName>.v<major>` (X-01). Apply the Appendix Z backlog items and Appendix AC open rows that name this phase.
